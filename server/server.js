import express from 'express';
import cors from 'cors';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import multer from 'multer';
import { initDatabase, dbService } from './db.js';
import { seedData } from './seedData.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const UPLOAD_DIR = path.join(__dirname, 'uploads', 'notes');
if (!fs.existsSync(UPLOAD_DIR)) {
  fs.mkdirSync(UPLOAD_DIR, { recursive: true });
}

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());
// Serve uploaded PDF files statically
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Multer Storage Configuration for PDF notes
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    if (!fs.existsSync(UPLOAD_DIR)) {
      fs.mkdirSync(UPLOAD_DIR, { recursive: true });
    }
    cb(null, UPLOAD_DIR);
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const ext = path.extname(file.originalname);
    const base = path.basename(file.originalname, ext).replace(/[^a-zA-Z0-9_-]/g, '_');
    cb(null, `${base}-${uniqueSuffix}${ext}`);
  }
});

const upload = multer({
  storage,
  limits: { fileSize: 50 * 1024 * 1024 }, // 50MB max per PDF
  fileFilter: (req, file, cb) => {
    if (file.mimetype === 'application/pdf' || file.originalname.toLowerCase().endsWith('.pdf')) {
      cb(null, true);
    } else {
      cb(new Error('Only PDF files (.pdf) are supported.'));
    }
  }
});

function formatBytes(bytes, decimals = 1) {
  if (!+bytes) return '0 Bytes';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`;
}

// Role-based security middleware for Admin endpoints (Requirement 7)
function requireAdmin(req, res, next) {
  const roleHeader = req.headers['x-user-role'];
  const userIdHeader = req.headers['x-user-id'];
  let role = roleHeader;

  if (userIdHeader) {
    const user = dbService.findById('users', parseInt(userIdHeader, 10));
    if (user) role = user.role;
  }

  if (role === 'admin') {
    return next();
  }

  return res.status(403).json({ error: 'Access denied: Administrator privileges required.' });
}

// Initialize Database with Seed Data
initDatabase(seedData);

// Healthcheck
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', name: 'Skillexa API Server', timestamp: new Date().toISOString() });
});

// ==========================================
// 1. COURSES & MODULES
// ==========================================
app.get('/api/courses', (req, res) => {
  const courses = dbService.find('courses');
  const userId = 1; // active user

  // Calculate course completion percentages dynamically
  const enrichedCourses = courses.map(course => {
    const courseTopics = dbService.find('topics', { course_id: course.id });
    const totalTopics = courseTopics.length;

    let completedCount = 0;
    courseTopics.forEach(topic => {
      const progress = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: topic.id });
      if (progress && progress.status === 'completed') {
        completedCount++;
      }
    });

    const completionPercentage = totalTopics > 0 ? Math.round((completedCount / totalTopics) * 100) : 0;

    return {
      ...course,
      topics_count: totalTopics,
      completed_count: completedCount,
      completion_percentage: completionPercentage
    };
  });

  res.json(enrichedCourses);
});

app.get('/api/courses/:slugOrId', (req, res) => {
  const { slugOrId } = req.params;
  const userId = 1;

  let course = dbService.findOne('courses', { slug: slugOrId });
  if (!course) {
    course = dbService.findById('courses', slugOrId);
  }

  if (!course) {
    return res.status(404).json({ error: 'Course not found' });
  }

  const modules = dbService.find('modules', { course_id: course.id })
    .sort((a, b) => a.order_index - b.order_index);

  const topics = dbService.find('topics', { course_id: course.id })
    .sort((a, b) => a.order_index - b.order_index);

  // Attach dynamic user progress and unlock status
  const topicsWithProgress = topics.map((topic, index) => {
    let progress = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: topic.id });

    // If no progress record exists yet, the first topic is unlocked by default; others locked
    let status = 'locked';
    let bestScore = 0;

    if (progress) {
      status = progress.status;
      bestScore = progress.best_score || 0;
    } else if (topic.order_index === 1 || topic.is_default_unlocked) {
      status = 'unlocked';
      dbService.insert('user_topic_progress', {
        user_id: userId,
        topic_id: topic.id,
        status: 'unlocked',
        best_score: 0,
        attempts_count: 0,
        unlocked_at: new Date().toISOString(),
        completed_at: null
      });
    }

    return {
      ...topic,
      status, // 'locked' | 'unlocked' | 'completed'
      best_score: bestScore
    };
  });

  const completedTopicsCount = topicsWithProgress.filter(t => t.status === 'completed').length;
  const completionPercentage = topics.length > 0 ? Math.round((completedTopicsCount / topics.length) * 100) : 0;

  res.json({
    ...course,
    modules,
    topics: topicsWithProgress,
    completed_topics_count: completedTopicsCount,
    total_topics_count: topics.length,
    completion_percentage: completionPercentage
  });
});

// ==========================================
// 2. TOPIC DETAILS (Learn, PYQs, Practice, Quiz)
// ==========================================
app.get('/api/topics/:id', (req, res) => {
  const topicId = parseInt(req.params.id, 10);
  const userId = 1;

  const topic = dbService.findById('topics', topicId);
  if (!topic) {
    return res.status(404).json({ error: 'Topic not found' });
  }

  const course = dbService.findById('courses', topic.course_id);
  const moduleItem = dbService.findById('modules', topic.module_id);

  // Check user unlock status
  let userProgress = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: topicId });
  if (!userProgress) {
    if (topic.order_index === 1 || topic.is_default_unlocked) {
      userProgress = dbService.insert('user_topic_progress', {
        user_id: userId,
        topic_id: topicId,
        status: 'unlocked',
        best_score: 0,
        attempts_count: 0,
        unlocked_at: new Date().toISOString(),
        completed_at: null
      });
    } else {
      userProgress = { status: 'locked', best_score: 0 };
    }
  }

  // Fetch verified published lessons with source citation
  const lessons = dbService.find('lessons', { topic_id: topicId, status: 'published' }).map(lesson => {
    const source = lesson.source_id ? dbService.findById('sources', lesson.source_id) : null;
    return { ...lesson, source };
  });

  // Fetch verified published Previous Year Questions
  const pyqs = dbService.find('previous_year_questions', { topic_id: topicId, status: 'published' }).map(pyq => {
    const exam = pyq.exam_id ? dbService.findById('exams', pyq.exam_id) : null;
    const source = pyq.source_id ? dbService.findById('sources', pyq.source_id) : null;
    return {
      ...pyq,
      exam,
      source
    };
  });

  // Fetch Practice Questions (distinctly labeled)
  const practiceQuestions = dbService.find('practice_questions', { topic_id: topicId });

  // Fetch Quiz Questions (do NOT expose correct answer if querying test mode, or provide for client grading)
  const quizQuestions = dbService.find('quiz_questions', { topic_id: topicId }).map(q => {
    const isBlank = q.question_type === 'FILL_IN_THE_BLANK' || (!q.options_json || q.options_json.length === 0) || q.question.includes('____') || q.question.includes('______');
    return {
      id: q.id,
      topic_id: q.topic_id,
      question: q.question,
      question_type: isBlank ? 'FILL_IN_THE_BLANK' : (q.question_type || 'MCQ'),
      options: isBlank ? [] : (q.options_json || []),
      subject: q.subject,
      topic: q.topic,
      points: q.points || 1
    };
  });

  // Find next topic in sequence
  const allCourseTopics = dbService.find('topics', { course_id: topic.course_id })
    .sort((a, b) => a.order_index - b.order_index);
  const currentIndex = allCourseTopics.findIndex(t => t.id === topic.id);
  const nextTopic = (currentIndex >= 0 && currentIndex < allCourseTopics.length - 1) ? allCourseTopics[currentIndex + 1] : null;

  let nextTopicStatus = 'locked';
  if (nextTopic) {
    const nextProg = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: nextTopic.id });
    if (nextProg) nextTopicStatus = nextProg.status;
  }

  res.json({
    topic: {
      ...topic,
      status: userProgress.status,
      best_score: userProgress.best_score || 0
    },
    course,
    module: moduleItem,
    lessons,
    previous_year_questions: pyqs,
    practice_questions: practiceQuestions,
    quiz: {
      total_questions: quizQuestions.length,
      passing_percentage: 70,
      questions: quizQuestions
    },
    next_topic: nextTopic ? { ...nextTopic, status: nextTopicStatus } : null
  });
});

// ==========================================
// 3. OVERALL COMPETITIVE QUIZ ENGINE
// ==========================================
app.get('/api/quizzes/overall', (req, res) => {
  const count = parseInt(req.query.count, 10) || 50;
  const allQuestions = dbService.find('quiz_questions');

  const grouped = {};
  for (const q of allQuestions) {
    const subj = q.subject || 'General';
    if (!grouped[subj]) grouped[subj] = [];
    grouped[subj].push(q);
  }

  const selected = [];
  const subjects = Object.keys(grouped);
  const perSubject = Math.max(1, Math.ceil(count / (subjects.length || 1)));

  for (const subj of subjects) {
    const list = [...grouped[subj]].sort(() => Math.random() - 0.5);
    selected.push(...list.slice(0, perSubject));
  }

  const randomized = selected.sort(() => Math.random() - 0.5).slice(0, count);

  const clientQuestions = randomized.map(q => {
    const isBlank = q.question_type === 'FILL_IN_THE_BLANK' || (!q.options_json || q.options_json.length === 0) || q.question.includes('____') || q.question.includes('______');
    return {
      id: q.id,
      topic_id: q.topic_id,
      question: q.question,
      question_type: isBlank ? 'FILL_IN_THE_BLANK' : (q.question_type || 'MCQ'),
      options: isBlank ? [] : (q.options_json || []),
      subject: q.subject,
      topic: q.topic,
      points: q.points || 1
    };
  });

  res.json({
    title: "Overall Competitive Comprehensive Mock Examination",
    total_questions: clientQuestions.length,
    passing_percentage: 70,
    questions: clientQuestions
  });
});

app.post('/api/quizzes/overall/submit', (req, res) => {
  const { answers, timeSpentSeconds, questionIds, questions } = req.body;
  const userId = 1;

  const ids = questionIds || (Array.isArray(questions) ? questions.map(q => q.id) : (answers ? Object.keys(answers) : []));

  if (!ids || ids.length === 0) {
    return res.status(400).json({ error: 'Question IDs required for overall evaluation' });
  }

  const officialQuestions = ids.map(id => dbService.findById('quiz_questions', parseInt(id, 10))).filter(Boolean);
  if (officialQuestions.length === 0) {
    return res.status(400).json({ error: 'No matching questions found' });
  }

  let correctCount = 0;
  const breakdown = officialQuestions.map(q => {
    const userAnswer = answers ? answers[q.id] : null;
    const cleanUser = userAnswer !== null && userAnswer !== undefined
      ? String(userAnswer).trim().toLowerCase()
      : '';
    const cleanCorrect = q.correct_answer !== null && q.correct_answer !== undefined
      ? String(q.correct_answer).trim().toLowerCase()
      : '';
    const isCorrect = cleanUser.length > 0 && cleanUser === cleanCorrect;
    if (isCorrect) correctCount++;

    return {
      question_id: q.id,
      question: q.question,
      question_type: q.question_type || (q.options_json?.length ? 'MCQ' : 'FILL_IN_THE_BLANK'),
      user_answer: userAnswer,
      correct_answer: q.correct_answer,
      is_correct: isCorrect,
      explanation: q.explanation,
      subject: q.subject,
      topic: q.topic
    };
  });

  const totalQuestions = officialQuestions.length;
  const percentage = Math.round((correctCount / totalQuestions) * 100);
  const passingRequirement = 70;
  const passed = percentage >= passingRequirement;

  const attempt = dbService.insert('quiz_attempts', {
    user_id: userId,
    topic_id: null,
    is_overall: true,
    score: correctCount,
    total: totalQuestions,
    percentage,
    passed,
    time_spent_seconds: timeSpentSeconds || 0,
    answers_json: answers
  });

  res.json({
    attempt_id: attempt.id,
    score: correctCount,
    total: totalQuestions,
    percentage,
    passed,
    passing_requirement: passingRequirement,
    breakdown,
    results: breakdown,
    message: passed 
      ? `Outstanding performance! You passed the Overall Competitive Mock with ${percentage}%.`
      : `You scored ${percentage}%. A minimum of ${passingRequirement}% is recommended. Review the solutions below and try again!`
  });
});

// ==========================================
// 3B. FULL-LENGTH MOCK EXAMS ENGINE (MINIMUM 50 QUESTIONS)
// ==========================================

// 1. Public list of published Mock Exams for students
app.get('/api/mock-exams', (req, res) => {
  const { category, search } = req.query;
  let exams = dbService.find('mock_exams', { status: 'published' });

  if (category && category !== 'All') {
    exams = exams.filter(e => (e.category || '').toLowerCase() === category.toLowerCase());
  }

  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    exams = exams.filter(e => 
      (e.title || '').toLowerCase().includes(q) ||
      (e.description || '').toLowerCase().includes(q) ||
      (e.target_exam || '').toLowerCase().includes(q)
    );
  }

  exams.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

  res.json({
    success: true,
    total: exams.length,
    data: exams
  });
});

// 2. Public details of a single Mock Exam (hydrated with questions)
app.get('/api/mock-exams/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const exam = dbService.findById('mock_exams', id);
  if (!exam) {
    return res.status(404).json({ error: 'Mock Exam not found' });
  }

  const qIds = exam.question_ids || [];
  const questions = qIds.map(qid => dbService.findById('quiz_questions', parseInt(qid, 10))).filter(Boolean);

  const clientQuestions = questions.map(q => {
    const isBlank = q.question_type === 'FILL_IN_THE_BLANK' || (!q.options_json || q.options_json.length === 0) || (q.question && q.question.includes('____'));
    return {
      id: q.id,
      topic_id: q.topic_id,
      question: q.question,
      question_type: isBlank ? 'FILL_IN_THE_BLANK' : (q.question_type || 'MCQ'),
      options: isBlank ? [] : (q.options_json || []),
      subject: q.subject || 'General',
      topic: q.topic || 'General',
      points: q.points || 1
    };
  });

  res.json({
    success: true,
    data: {
      ...exam,
      total_questions: clientQuestions.length,
      questions: clientQuestions
    }
  });
});

// 3. Submit Mock Exam Attempt
app.post('/api/mock-exams/:id/submit', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const exam = dbService.findById('mock_exams', id);
  if (!exam) {
    return res.status(404).json({ error: 'Mock Exam not found' });
  }

  const { answers, timeSpentSeconds } = req.body; // answers: { [qid]: value }
  const userId = 1;

  const qIds = exam.question_ids || [];
  const officialQuestions = qIds.map(qid => dbService.findById('quiz_questions', parseInt(qid, 10))).filter(Boolean);

  let correctCount = 0;
  let incorrectCount = 0;
  let unattemptedCount = 0;

  const breakdown = officialQuestions.map(q => {
    const userAnswer = answers ? answers[q.id] : null;
    const hasAnswered = userAnswer !== null && userAnswer !== undefined && String(userAnswer).trim().length > 0;
    
    let isCorrect = false;
    if (hasAnswered) {
      const cleanUser = String(userAnswer).trim().toLowerCase();
      const cleanCorrect = q.correct_answer !== null && q.correct_answer !== undefined
        ? String(q.correct_answer).trim().toLowerCase()
        : '';
      isCorrect = cleanUser === cleanCorrect;
      if (isCorrect) correctCount++;
      else incorrectCount++;
    } else {
      unattemptedCount++;
    }

    return {
      question_id: q.id,
      question: q.question,
      question_type: q.question_type || (q.options_json?.length ? 'MCQ' : 'FILL_IN_THE_BLANK'),
      options: q.options_json || [],
      user_answer: userAnswer,
      correct_answer: q.correct_answer,
      is_correct: isCorrect,
      is_unattempted: !hasAnswered,
      explanation: q.explanation,
      subject: q.subject || 'General',
      topic: q.topic || 'General'
    };
  });

  const totalQuestions = officialQuestions.length;
  const negativeMarkingPerQuestion = exam.negative_marking || 0.25;
  const marksPerQuestion = 2; // Standard 2 marks per question (total 100 for 50 questions)
  const rawScore = (correctCount * marksPerQuestion) - (incorrectCount * negativeMarkingPerQuestion);
  const finalScore = Math.max(0, Math.round(rawScore * 100) / 100);
  const totalMaxMarks = totalQuestions * marksPerQuestion;
  const percentage = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
  const passingRequirement = exam.passing_percentage || 70;
  const passed = percentage >= passingRequirement;

  const attempt = dbService.insert('quiz_attempts', {
    user_id: userId,
    mock_exam_id: exam.id,
    topic_id: null,
    is_overall: true,
    score: finalScore,
    correct_count: correctCount,
    incorrect_count: incorrectCount,
    unattempted_count: unattemptedCount,
    total: totalQuestions,
    max_marks: totalMaxMarks,
    percentage,
    passed,
    time_spent_seconds: timeSpentSeconds || 0,
    answers_json: answers,
    created_at: new Date().toISOString()
  });

  res.json({
    success: true,
    attempt_id: attempt.id,
    exam_title: exam.title,
    score: finalScore,
    max_marks: totalMaxMarks,
    correct_count: correctCount,
    incorrect_count: incorrectCount,
    unattempted_count: unattemptedCount,
    total_questions: totalQuestions,
    percentage,
    passed,
    passing_requirement: passingRequirement,
    breakdown,
    message: passed
      ? `Congratulations! You passed "${exam.title}" with ${percentage}% score.`
      : `You scored ${percentage}%. Passing criteria is ${passingRequirement}%. Review your weak areas and re-attempt.`
  });
});

// 4. Admin: Get all mock exams with attempt statistics
app.get('/api/admin/mock-exams', requireAdmin, (req, res) => {
  const exams = dbService.find('mock_exams');
  const attempts = dbService.find('quiz_attempts');

  const enriched = exams.map(e => {
    const examAttempts = attempts.filter(a => a.mock_exam_id === e.id);
    const totalAttempts = examAttempts.length;
    const avgScore = totalAttempts > 0 
      ? Math.round(examAttempts.reduce((sum, a) => sum + (a.percentage || 0), 0) / totalAttempts)
      : 0;

    return {
      ...e,
      total_questions: (e.question_ids || []).length,
      attempts_count: totalAttempts,
      average_score: avgScore
    };
  });

  enriched.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

  res.json({
    success: true,
    total: enriched.length,
    data: enriched
  });
});

// 5. Admin: Browse question bank for mock exam creation
app.get('/api/admin/mock-exams/question-bank', requireAdmin, (req, res) => {
  const { subject, search, limit = 600 } = req.query;
  let questions = dbService.find('quiz_questions');

  if (subject && subject !== 'All') {
    questions = questions.filter(q => (q.subject || '').toLowerCase().includes(subject.toLowerCase()));
  }

  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    questions = questions.filter(item => 
      (item.question || '').toLowerCase().includes(q) ||
      (item.topic || '').toLowerCase().includes(q) ||
      (item.subject || '').toLowerCase().includes(q)
    );
  }

  res.json({
    success: true,
    total: questions.length,
    data: questions.slice(0, parseInt(limit, 10))
  });
});

// 6. Admin: Create New Mock Exam (ENFORCES MINIMUM 50 QUESTIONS)
app.post('/api/admin/mock-exams', requireAdmin, (req, res) => {
  const {
    title,
    category,
    target_exam,
    description,
    duration_minutes,
    passing_percentage,
    negative_marking,
    instructions,
    question_ids,
    auto_generate,
    subject_distribution,
    status
  } = req.body;

  if (!title || !title.trim()) {
    return res.status(400).json({ error: 'Mock Exam Title is required' });
  }

  let finalQuestionIds = Array.isArray(question_ids) ? [...question_ids] : [];

  // If auto-generation requested or list is empty
  if (auto_generate || finalQuestionIds.length === 0) {
    const allQ = dbService.find('quiz_questions');
    const englishQs = allQ.filter(q => (q.subject || '').includes('English'));
    const mathQs = allQ.filter(q => (q.subject || '').includes('Math'));
    const reasonQs = allQ.filter(q => (q.subject || '').includes('Reason'));
    const gaQs = allQ.filter(q => (q.subject || '').includes('Awareness'));
    const sciQs = allQ.filter(q => (q.subject || '').includes('Science'));

    const counts = subject_distribution || {
      english: 15,
      math: 15,
      reasoning: 10,
      general_awareness: 10
    };

    const sampled = [
      ...englishQs.sort(() => Math.random() - 0.5).slice(0, counts.english || 15).map(q => q.id),
      ...mathQs.sort(() => Math.random() - 0.5).slice(0, counts.math || 15).map(q => q.id),
      ...reasonQs.sort(() => Math.random() - 0.5).slice(0, counts.reasoning || 10).map(q => q.id),
      ...gaQs.sort(() => Math.random() - 0.5).slice(0, counts.general_awareness || 10).map(q => q.id)
    ];

    finalQuestionIds = Array.from(new Set(sampled));
    // Pad to 50 if needed
    if (finalQuestionIds.length < 50) {
      const remaining = allQ.filter(q => !finalQuestionIds.includes(q.id));
      for (const r of remaining) {
        finalQuestionIds.push(r.id);
        if (finalQuestionIds.length >= 50) break;
      }
    }
  }

  // MANDATORY CONSTRAINT: Minimum 50 questions
  if (finalQuestionIds.length < 50) {
    return res.status(400).json({
      error: `Mock exams must contain a minimum of 50 questions. Current selection only has ${finalQuestionIds.length} questions.`
    });
  }

  const now = new Date().toISOString();
  const created = dbService.insert('mock_exams', {
    title: title.trim(),
    category: category || 'SSC',
    target_exam: target_exam || 'Competitive Exams',
    description: (description || '').trim(),
    duration_minutes: parseInt(duration_minutes, 10) || 60,
    total_questions: finalQuestionIds.length,
    total_marks: finalQuestionIds.length * 2,
    passing_percentage: parseInt(passing_percentage, 10) || 70,
    negative_marking: parseFloat(negative_marking) || 0.25,
    instructions: instructions || '1. This mock exam contains a minimum of 50 objective questions.\n2. Negative marking applies for wrong answers.',
    question_ids: finalQuestionIds,
    status: status === 'draft' ? 'draft' : 'published',
    created_by: 'Administrator',
    created_at: now,
    updated_at: now
  });

  res.status(201).json({
    success: true,
    data: created,
    message: `Mock Exam "${created.title}" with ${finalQuestionIds.length} questions created successfully.`
  });
});

// 7. Admin: Update Mock Exam
app.put('/api/admin/mock-exams/:id', requireAdmin, (req, res) => {
  const id = parseInt(req.params.id, 10);
  const exam = dbService.findById('mock_exams', id);
  if (!exam) {
    return res.status(404).json({ error: 'Mock Exam not found' });
  }

  const {
    title,
    category,
    target_exam,
    description,
    duration_minutes,
    passing_percentage,
    negative_marking,
    instructions,
    question_ids,
    status
  } = req.body;

  const updates = {
    updated_at: new Date().toISOString()
  };

  if (title !== undefined) updates.title = title.trim();
  if (category !== undefined) updates.category = category;
  if (target_exam !== undefined) updates.target_exam = target_exam;
  if (description !== undefined) updates.description = (description || '').trim();
  if (duration_minutes !== undefined) updates.duration_minutes = parseInt(duration_minutes, 10) || 60;
  if (passing_percentage !== undefined) updates.passing_percentage = parseInt(passing_percentage, 10) || 70;
  if (negative_marking !== undefined) updates.negative_marking = parseFloat(negative_marking) || 0.25;
  if (instructions !== undefined) updates.instructions = instructions;
  if (status !== undefined) updates.status = status;

  if (question_ids !== undefined) {
    if (!Array.isArray(question_ids) || question_ids.length < 50) {
      return res.status(400).json({
        error: `Mock exams must contain a minimum of 50 questions. (Attempted to save ${Array.isArray(question_ids) ? question_ids.length : 0})`
      });
    }
    updates.question_ids = question_ids;
    updates.total_questions = question_ids.length;
    updates.total_marks = question_ids.length * 2;
  }

  const updated = dbService.update('mock_exams', id, updates);
  res.json({
    success: true,
    data: updated,
    message: 'Mock Exam updated successfully'
  });
});

// 8. Admin: Toggle Status
app.patch('/api/admin/mock-exams/:id/status', requireAdmin, (req, res) => {
  const id = parseInt(req.params.id, 10);
  const exam = dbService.findById('mock_exams', id);
  if (!exam) {
    return res.status(404).json({ error: 'Mock Exam not found' });
  }

  const newStatus = req.body.status || (exam.status === 'published' ? 'draft' : 'published');
  const updated = dbService.update('mock_exams', id, {
    status: newStatus,
    updated_at: new Date().toISOString()
  });

  res.json({
    success: true,
    data: updated,
    message: `Mock Exam status changed to ${newStatus}`
  });
});

// 9. Admin: Delete Mock Exam
app.delete('/api/admin/mock-exams/:id', requireAdmin, (req, res) => {
  const id = parseInt(req.params.id, 10);
  const deleted = dbService.delete('mock_exams', id);
  if (!deleted) {
    return res.status(404).json({ error: 'Mock Exam not found' });
  }
  res.json({ success: true, message: 'Mock Exam deleted successfully' });
});

// ==========================================
// 4. TOPIC QUIZ SUBMISSION & UNLOCK ENGINE
// ==========================================
app.post('/api/quizzes/:topicId/submit', (req, res) => {
  const topicId = parseInt(req.params.topicId, 10);
  const { answers, timeSpentSeconds } = req.body; // answers: { [questionId]: "Selected Option" }
  const userId = 1;

  const topic = dbService.findById('topics', topicId);
  if (!topic) {
    return res.status(404).json({ error: 'Topic not found' });
  }

  const officialQuestions = dbService.find('quiz_questions', { topic_id: topicId });
  if (officialQuestions.length === 0) {
    return res.status(400).json({ error: 'No quiz questions configured for this topic' });
  }

  let correctCount = 0;
  const breakdown = officialQuestions.map(q => {
    const userAnswer = answers ? answers[q.id] : null;
    const cleanUser = userAnswer !== null && userAnswer !== undefined
      ? String(userAnswer).trim().toLowerCase()
      : '';
    const cleanCorrect = q.correct_answer !== null && q.correct_answer !== undefined
      ? String(q.correct_answer).trim().toLowerCase()
      : '';
    const isCorrect = cleanUser.length > 0 && cleanUser === cleanCorrect;
    if (isCorrect) correctCount++;

    return {
      question_id: q.id,
      question: q.question,
      question_type: q.question_type || (q.options_json?.length ? 'MCQ' : 'FILL_IN_THE_BLANK'),
      user_answer: userAnswer,
      correct_answer: q.correct_answer,
      is_correct: isCorrect,
      explanation: q.explanation
    };
  });

  const totalQuestions = officialQuestions.length;
  const percentage = Math.round((correctCount / totalQuestions) * 100);
  const passingRequirement = 70;
  const passed = percentage >= passingRequirement;

  // Record attempt in database
  const attempt = dbService.insert('quiz_attempts', {
    user_id: userId,
    topic_id: topicId,
    score: correctCount,
    total: totalQuestions,
    percentage,
    passed,
    time_spent_seconds: timeSpentSeconds || 0,
    answers_json: answers
  });

  // Update User Topic Progress
  let progress = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: topicId });
  const newBestScore = progress ? Math.max(progress.best_score || 0, percentage) : percentage;
  const newAttemptsCount = (progress?.attempts_count || 0) + 1;

  if (!progress) {
    progress = dbService.insert('user_topic_progress', {
      user_id: userId,
      topic_id: topicId,
      status: passed ? 'completed' : 'unlocked',
      best_score: newBestScore,
      attempts_count: newAttemptsCount,
      unlocked_at: new Date().toISOString(),
      completed_at: passed ? new Date().toISOString() : null
    });
  } else {
    dbService.updateWhere('user_topic_progress', { user_id: userId, topic_id: topicId }, {
      status: passed ? 'completed' : progress.status,
      best_score: newBestScore,
      attempts_count: newAttemptsCount,
      completed_at: passed ? (progress.completed_at || new Date().toISOString()) : progress.completed_at
    });
  }

  // CORE BACKEND UNLOCK SYSTEM:
  // If passed (percentage >= 70%), unlock the NEXT topic in sequential order!
  let unlockedNextTopic = null;
  if (passed) {
    const courseTopics = dbService.find('topics', { course_id: topic.course_id })
      .sort((a, b) => a.order_index - b.order_index);
    const currentIndex = courseTopics.findIndex(t => t.id === topic.id);

    if (currentIndex >= 0 && currentIndex < courseTopics.length - 1) {
      const nextTopic = courseTopics[currentIndex + 1];
      let nextProg = dbService.findOne('user_topic_progress', { user_id: userId, topic_id: nextTopic.id });

      if (!nextProg) {
        nextProg = dbService.insert('user_topic_progress', {
          user_id: userId,
          topic_id: nextTopic.id,
          status: 'unlocked',
          best_score: 0,
          attempts_count: 0,
          unlocked_at: new Date().toISOString(),
          completed_at: null
        });
      } else if (nextProg.status === 'locked') {
        dbService.updateWhere('user_topic_progress', { user_id: userId, topic_id: nextTopic.id }, {
          status: 'unlocked',
          unlocked_at: new Date().toISOString()
        });
      }

      unlockedNextTopic = {
        id: nextTopic.id,
        title: nextTopic.title,
        slug: nextTopic.slug,
        order_index: nextTopic.order_index
      };
    }
  }

  res.json({
    attempt_id: attempt.id,
    score: correctCount,
    total: totalQuestions,
    percentage,
    passed,
    passing_requirement: passingRequirement,
    unlocked_next_topic: unlockedNextTopic,
    breakdown,
    message: passed
      ? (unlockedNextTopic ? `Outstanding! You scored ${percentage}% and unlocked ${unlockedNextTopic.title}!` : `Superb! You completed this topic with ${percentage}%!`)
      : `You scored ${percentage}%. Score at least 70% to unlock the next level.`
  });
});

// ==========================================
// 4. GOVERNMENT EXAMS & VERIFIED NOTIFICATIONS ENGINE
// ==========================================

// Helper to compute live dynamic status
function computeExamStatus(exam) {
  const now = new Date();
  const todayStr = now.toISOString().split('T')[0];

  // 1. Result Released
  if (exam.update_type === 'RESULT' || (exam.result_date && exam.result_date <= todayStr)) {
    return {
      status_key: 'RESULT_RELEASED',
      status_label: 'Result Released',
      badge_class: 'badge-cyan',
      is_expired: false
    };
  }

  // 2. Application Closed (Expired)
  if (exam.application_last_date && todayStr > exam.application_last_date) {
    return {
      status_key: 'APPLICATION_CLOSED',
      status_label: 'Application Closed',
      badge_class: 'badge-rose',
      is_expired: true
    };
  }

  // 3. Applications Open
  if (exam.application_start_date && todayStr >= exam.application_start_date && (!exam.application_last_date || todayStr <= exam.application_last_date)) {
    let daysRemaining = null;
    if (exam.application_last_date) {
      const diffMs = new Date(exam.application_last_date + 'T23:59:59') - now;
      daysRemaining = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));
    }
    return {
      status_key: 'APPLICATIONS_OPEN',
      status_label: daysRemaining !== null && daysRemaining <= 3 ? `Closing in ${daysRemaining} day${daysRemaining === 1 ? '' : 's'}` : 'Applications Open',
      badge_class: daysRemaining !== null && daysRemaining <= 3 ? 'badge-amber' : 'badge-emerald',
      is_expired: false,
      days_remaining: daysRemaining
    };
  }

  // 4. Upcoming Exam Date
  if (exam.exam_date && exam.exam_date >= todayStr) {
    const diffMs = new Date(exam.exam_date + 'T00:00:00') - now;
    const diffDays = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));
    return {
      status_key: 'EXAM_SCHEDULED',
      status_label: diffDays > 0 ? `Upcoming Exam in ${diffDays} day${diffDays === 1 ? '' : 's'}` : 'Exam Scheduled Today',
      badge_class: 'badge-primary',
      is_expired: false,
      days_until_exam: diffDays
    };
  }

  // 5. Coming Soon
  if (exam.application_start_date && todayStr < exam.application_start_date) {
    const diffMs = new Date(exam.application_start_date + 'T00:00:00') - now;
    const diffDays = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));
    return {
      status_key: 'COMING_SOON',
      status_label: diffDays > 0 ? `Opens in ${diffDays} day${diffDays === 1 ? '' : 's'}` : 'Coming Soon',
      badge_class: 'badge-amber',
      is_expired: false,
      days_until_open: diffDays
    };
  }

  // 6. Active Notice / Fallback
  return {
    status_key: 'ACTIVE',
    status_label: 'Verified Notice',
    badge_class: 'badge-primary',
    is_expired: false
  };
}

// User-facing Government Exams Updates (ONLY VERIFIED + PUBLISHED)
app.get('/api/government-exams', (req, res) => {
  const { category, update_type, status, search } = req.query;

  // Rule: Draft, Pending Review, Rejected must NEVER appear to normal users
  let exams = dbService.find('government_exam_updates', { verification_status: 'PUBLISHED' });

  // Enrich with dynamic status calculations
  exams = exams.map(exam => {
    const computed = computeExamStatus(exam);
    return {
      ...exam,
      dynamic_status: computed
    };
  });

  // Category filter
  if (category && category !== 'All') {
    exams = exams.filter(e => {
      const cat = (e.category || '').toLowerCase();
      const target = category.toLowerCase();
      return cat.includes(target) || (target === 'railway' && cat.includes('rrb'));
    });
  }

  // Update Type filter
  if (update_type && update_type !== 'All') {
    exams = exams.filter(e => e.update_type === update_type || (e.update_type || '').toLowerCase().includes(update_type.toLowerCase()));
  }

  // Status filter (Applications Open, Closed, Upcoming, Result, etc.)
  if (status && status !== 'All') {
    const s = status.toLowerCase();
    exams = exams.filter(e => {
      const key = (e.dynamic_status?.status_key || '').toLowerCase();
      if (s.includes('open') || s === 'applications open') return key === 'applications_open';
      if (s.includes('close') || s === 'closed') return key === 'application_closed';
      if (s.includes('upcoming') || s.includes('scheduled')) return key === 'exam_scheduled';
      if (s.includes('result')) return key === 'result_released';
      if (s.includes('coming') || s.includes('soon')) return key === 'coming_soon';
      return true;
    });
  }

  // Search filter
  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    exams = exams.filter(e => 
      (e.exam_name || '').toLowerCase().includes(q) ||
      (e.organization || '').toLowerCase().includes(q) ||
      (e.title || '').toLowerCase().includes(q) ||
      (e.short_description || '').toLowerCase().includes(q) ||
      (e.category || '').toLowerCase().includes(q) ||
      (e.post_name || '').toLowerCase().includes(q) ||
      (e.official_notification_number || '').toLowerCase().includes(q)
    );
  }

  // Sort by published_at or created_at descending
  exams.sort((a, b) => new Date(b.published_at || b.created_at || 0) - new Date(a.published_at || a.created_at || 0));

  res.json({
    success: true,
    total: exams.length,
    data: exams
  });
});

// Latest 3-5 Government Exams for Homepage integration
app.get('/api/government-exams/latest', (req, res) => {
  const limit = parseInt(req.query.limit, 10) || 4;
  let exams = dbService.find('government_exam_updates', { verification_status: 'PUBLISHED' });
  
  exams = exams.map(exam => ({
    ...exam,
    dynamic_status: computeExamStatus(exam)
  }));

  exams.sort((a, b) => new Date(b.published_at || b.created_at || 0) - new Date(a.published_at || a.created_at || 0));

  res.json({
    success: true,
    data: exams.slice(0, limit)
  });
});

// Single Government Exam Details
app.get('/api/government-exams/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const exam = dbService.findById('government_exam_updates', id);

  if (!exam) {
    return res.status(404).json({ error: 'Government Exam update not found' });
  }

  const enriched = {
    ...exam,
    dynamic_status: computeExamStatus(exam)
  };

  res.json({
    success: true,
    data: enriched
  });
});

// Expandable Exam Categories list
app.get('/api/exam-categories', (req, res) => {
  const categories = dbService.find('exam_categories');
  res.json({ success: true, data: categories });
});

// Admin add expandable category
app.post('/api/admin/exam-categories', (req, res) => {
  const { name, key, group, description } = req.body;
  if (!name || !group) {
    return res.status(400).json({ error: 'Category name and group are required' });
  }

  const existing = dbService.findOne('exam_categories', { name });
  if (existing) {
    return res.status(409).json({ error: 'Category already exists' });
  }

  const created = dbService.insert('exam_categories', {
    name,
    key: key || name,
    group,
    description: description || ''
  });

  res.status(201).json({ success: true, data: created });
});

// Admin: Get all Government Exam Updates across all workflows (DRAFT, PENDING_REVIEW, VERIFIED, PUBLISHED, REJECTED, ARCHIVED)
app.get('/api/admin/government-exams/all', (req, res) => {
  const { status, category, search } = req.query;
  let list = dbService.find('government_exam_updates');

  if (status && status !== 'All') {
    list = list.filter(item => item.verification_status === status);
  }

  if (category && category !== 'All') {
    list = list.filter(item => (item.category || '').toLowerCase().includes(category.toLowerCase()));
  }

  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    list = list.filter(item => 
      (item.exam_name || '').toLowerCase().includes(q) ||
      (item.organization || '').toLowerCase().includes(q) ||
      (item.title || '').toLowerCase().includes(q)
    );
  }

  list = list.map(item => ({
    ...item,
    dynamic_status: computeExamStatus(item)
  }));

  list.sort((a, b) => new Date(b.updated_at || b.created_at || 0) - new Date(a.updated_at || a.created_at || 0));

  // Compute status metrics for admin review dashboard
  const allItems = dbService.find('government_exam_updates');
  const counts = {
    total: allItems.length,
    draft: allItems.filter(i => i.verification_status === 'DRAFT').length,
    pending_review: allItems.filter(i => i.verification_status === 'PENDING_REVIEW').length,
    verified: allItems.filter(i => i.verification_status === 'VERIFIED').length,
    published: allItems.filter(i => i.verification_status === 'PUBLISHED').length,
    rejected: allItems.filter(i => i.verification_status === 'REJECTED').length,
    archived: allItems.filter(i => i.verification_status === 'ARCHIVED').length
  };

  res.json({
    success: true,
    counts,
    data: list
  });
});

// Admin: Create Government Exam Update with duplicate protection
app.post('/api/admin/government-exams', (req, res) => {
  const {
    exam_name,
    organization,
    category,
    update_type,
    title,
    short_description,
    full_description,
    post_name,
    vacancy,
    eligibility,
    age_limit,
    qualification,
    application_fee,
    selection_process,
    official_notification_number,
    notification_date,
    application_start_date,
    application_last_date,
    correction_date,
    exam_date,
    admit_card_date,
    answer_key_date,
    result_date,
    official_source_name,
    official_source_url,
    image_url,
    verification_status,
    send_push_notification,
    force_duplicate
  } = req.body;

  // Validation
  if (!exam_name || !organization || !category || !update_type || !title) {
    return res.status(400).json({ error: 'Exam Name, Organization, Category, Update Type, and Title are mandatory.' });
  }

  if (!official_source_name || !official_source_url) {
    return res.status(400).json({ error: 'Official Source Name and Official Source URL are mandatory for government exam verification.' });
  }

  // Duplicate Protection Rule (Organization + Exam Name + Update Type)
  if (!force_duplicate) {
    const existing = dbService.find('government_exam_updates').find(e => 
      e.organization?.toLowerCase().trim() === organization.toLowerCase().trim() &&
      e.exam_name?.toLowerCase().trim() === exam_name.toLowerCase().trim() &&
      e.update_type === update_type &&
      e.verification_status !== 'ARCHIVED' &&
      e.verification_status !== 'REJECTED'
    );

    if (existing) {
      return res.status(409).json({
        error: 'Duplicate Warning: An active update with this Exam Name, Organization, and Update Type already exists in the system.',
        existing_id: existing.id,
        is_duplicate: true
      });
    }
  }

  const initialStatus = verification_status || 'DRAFT';
  const now = new Date().toISOString();

  const created = dbService.insert('government_exam_updates', {
    exam_name,
    organization,
    category,
    update_type,
    title,
    short_description: short_description || '',
    full_description: full_description || short_description || '',
    post_name: post_name || '',
    vacancy: vacancy || '',
    eligibility: eligibility || '',
    age_limit: age_limit || '',
    qualification: qualification || '',
    application_fee: application_fee || '',
    selection_process: selection_process || '',
    official_notification_number: official_notification_number || '',
    notification_date: notification_date || '',
    application_start_date: application_start_date || '',
    application_last_date: application_last_date || '',
    correction_date: correction_date || '',
    exam_date: exam_date || '',
    admit_card_date: admit_card_date || '',
    answer_key_date: answer_key_date || '',
    result_date: result_date || '',
    official_source_name,
    official_source_url,
    image_url: image_url || '',
    verification_status: initialStatus,
    published_at: initialStatus === 'PUBLISHED' ? now : null,
    created_at: now,
    updated_at: now
  });

  // If directly published and send_push_notification enabled:
  let notificationResult = null;
  if (initialStatus === 'PUBLISHED' && send_push_notification) {
    notificationResult = dispatchPushNotificationForExam(created);
  }

  res.status(201).json({
    success: true,
    data: created,
    notification_dispatched: !!notificationResult
  });
});

// Admin: Edit Government Exam Update
app.put('/api/admin/government-exams/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const existing = dbService.findById('government_exam_updates', id);
  if (!existing) {
    return res.status(404).json({ error: 'Government Exam update not found' });
  }

  const updates = { ...req.body };
  delete updates.id;
  updates.updated_at = new Date().toISOString();

  if (updates.verification_status === 'PUBLISHED' && !existing.published_at) {
    updates.published_at = new Date().toISOString();
  }

  const updated = dbService.update('government_exam_updates', id, updates);

  if (req.body.send_push_notification && updated.verification_status === 'PUBLISHED') {
    dispatchPushNotificationForExam(updated);
  }

  res.json({ success: true, data: updated });
});

// Admin: Delete Government Exam Update
app.delete('/api/admin/government-exams/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const deleted = dbService.delete('government_exam_updates', id);
  if (!deleted) {
    return res.status(404).json({ error: 'Government Exam update not found' });
  }
  res.json({ success: true, message: `Government exam update #${id} deleted successfully.` });
});

// Admin Workflow State Transitions: DRAFT -> PENDING_REVIEW -> VERIFIED -> PUBLISHED / REJECTED / ARCHIVED
app.patch('/api/admin/government-exams/:id/status', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const { status, send_push_notification } = req.body;

  const validStatuses = ['DRAFT', 'PENDING_REVIEW', 'VERIFIED', 'PUBLISHED', 'REJECTED', 'ARCHIVED'];
  if (!validStatuses.includes(status)) {
    return res.status(400).json({ error: `Invalid status. Must be one of: ${validStatuses.join(', ')}` });
  }

  const exam = dbService.findById('government_exam_updates', id);
  if (!exam) {
    return res.status(404).json({ error: 'Government Exam update not found' });
  }

  const updates = {
    verification_status: status,
    updated_at: new Date().toISOString()
  };

  if (status === 'PUBLISHED') {
    updates.published_at = exam.published_at || new Date().toISOString();
  }

  const updated = dbService.update('government_exam_updates', id, updates);

  let notificationDispatched = false;
  if (status === 'PUBLISHED' && send_push_notification) {
    dispatchPushNotificationForExam(updated);
    notificationDispatched = true;
  }

  res.json({
    success: true,
    data: updated,
    notification_dispatched: notificationDispatched,
    message: `Exam status transitioned to ${status}.`
  });
});

// Dispatcher helper for notifications
function dispatchPushNotificationForExam(exam) {
  try {
    const preferences = dbService.find('notification_preferences');
    const updateType = exam.update_type || 'EXAM_NOTIFICATION';
    const category = exam.category || 'Other';

    // Map update_type to preference key
    const typePrefMap = {
      EXAM_NOTIFICATION: 'exam_notifications',
      APPLICATION_OPEN: 'application_updates',
      APPLICATION_CLOSING: 'application_updates',
      ADMIT_CARD: 'admit_card_updates',
      EXAM_DATE: 'exam_date_updates',
      ANSWER_KEY: 'answer_key_updates',
      RESULT: 'result_updates',
      CUTOFF: 'result_updates',
      MERIT_LIST: 'result_updates',
      JOB_NOTIFICATION: 'job_notifications',
      IMPORTANT_NOTICE: 'exam_notifications'
    };

    const prefKey = typePrefMap[updateType] || 'exam_notifications';

    // Eligible users: check notification preferences
    const users = dbService.find('users');
    let count = 0;

    users.forEach(user => {
      const userPref = preferences.find(p => p.user_id === user.id) || {
        [prefKey]: true,
        category_preferences: ['SSC', 'UPSC', 'Railway', 'Banking', 'KPSC', 'Defence', 'Teaching', 'Police']
      };

      const typeAllowed = userPref[prefKey] !== false;
      const catAllowed = !userPref.category_preferences || userPref.category_preferences.length === 0 ||
        userPref.category_preferences.some(cp => category.toLowerCase().includes(cp.toLowerCase()));

      if (typeAllowed && catAllowed) {
        dbService.insert('notifications', {
          user_id: user.id,
          update_id: exam.id,
          title: `🔔 ${exam.exam_name} Update`,
          message: exam.short_description || `${exam.title} has been officially published. Check details and official source.`,
          notification_type: updateType,
          is_read: false,
          created_at: new Date().toISOString()
        });
        count++;
      }
    });

    return { sent_to_users_count: count };
  } catch (err) {
    console.error('Error dispatching push notifications:', err);
    return null;
  }
}

// ==========================================
// 5. PUSH NOTIFICATIONS & USER PREFERENCES API
// ==========================================

// Get user notifications + unread count
app.get('/api/notifications', (req, res) => {
  const userId = 1; // active user
  const notifications = dbService.find('notifications', { user_id: userId })
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

  const unreadCount = notifications.filter(n => !n.is_read).length;

  res.json({
    success: true,
    unread_count: unreadCount,
    data: notifications
  });
});

// Mark single notification as read
app.patch('/api/notifications/:id/read', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const updated = dbService.update('notifications', id, { is_read: true });
  if (!updated) {
    return res.status(404).json({ error: 'Notification not found' });
  }
  res.json({ success: true, data: updated });
});

// Mark all user notifications as read
app.post('/api/notifications/mark-all-read', (req, res) => {
  const userId = 1;
  const updated = dbService.updateWhere('notifications', { user_id: userId }, { is_read: true });
  res.json({ success: true, count: updated.length });
});

// Get unread count for badge
app.get('/api/notifications/unread-count', (req, res) => {
  const userId = 1;
  const notifications = dbService.find('notifications', { user_id: userId });
  const unreadCount = notifications.filter(n => !n.is_read).length;
  res.json({ unread_count: unreadCount });
});

// Register push notification token (Expo / Web Push)
app.post('/api/notifications/token', (req, res) => {
  const { push_token, platform } = req.body;
  const userId = 1;

  if (!push_token) {
    return res.status(400).json({ error: 'Push token required' });
  }

  const existing = dbService.findOne('user_notification_tokens', { user_id: userId, push_token });
  if (!existing) {
    dbService.insert('user_notification_tokens', {
      user_id: userId,
      push_token,
      platform: platform || 'web',
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    });
  }

  res.json({ success: true, message: 'Push token registered successfully.' });
});

// Deadline Reminders Scanner (e.g. within 2-3 days of last date)
app.post('/api/notifications/check-deadlines', (req, res) => {
  const userId = 1;
  const now = new Date();
  const todayStr = now.toISOString().split('T')[0];

  const publishedExams = dbService.find('government_exam_updates', { verification_status: 'PUBLISHED' });
  let remindersSent = 0;

  publishedExams.forEach(exam => {
    if (exam.application_last_date && exam.application_last_date >= todayStr) {
      const diffMs = new Date(exam.application_last_date + 'T23:59:59') - now;
      const daysRemaining = Math.max(0, Math.ceil(diffMs / (1000 * 60 * 60 * 24)));

      // If closes in <= 3 days, send reminder if not already sent
      if (daysRemaining <= 3 && daysRemaining >= 0) {
        const existing = dbService.findOne('notifications', {
          user_id: userId,
          update_id: exam.id,
          notification_type: 'APPLICATION_CLOSING'
        });

        if (!existing) {
          dbService.insert('notifications', {
            user_id: userId,
            update_id: exam.id,
            title: `🔔 Application Deadline Reminder`,
            message: `${exam.exam_name} application closes in ${daysRemaining === 0 ? 'less than 24 hours' : daysRemaining + ' day(s)'}. Apply before ${exam.application_last_date}!`,
            notification_type: 'APPLICATION_CLOSING',
            is_read: false,
            created_at: new Date().toISOString()
          });
          remindersSent++;
        }
      }
    }
  });

  res.json({ success: true, reminders_sent: remindersSent });
});

// Get user notification preferences
app.get('/api/notification-preferences', (req, res) => {
  const userId = 1;
  let pref = dbService.findOne('notification_preferences', { user_id: userId });

  if (!pref) {
    pref = dbService.insert('notification_preferences', {
      user_id: userId,
      exam_notifications: true,
      application_updates: true,
      admit_card_updates: true,
      exam_date_updates: true,
      answer_key_updates: true,
      result_updates: true,
      job_notifications: true,
      category_preferences: ['SSC', 'UPSC', 'Railway', 'Banking', 'KPSC', 'Defence', 'Teaching', 'Police'],
      updated_at: new Date().toISOString()
    });
  }

  res.json({ success: true, data: pref });
});

// Update user notification preferences
app.put('/api/notification-preferences', (req, res) => {
  const userId = 1;
  const updates = req.body;
  updates.updated_at = new Date().toISOString();

  let pref = dbService.findOne('notification_preferences', { user_id: userId });
  if (pref) {
    pref = dbService.update('notification_preferences', pref.id, updates);
  } else {
    pref = dbService.insert('notification_preferences', {
      user_id: userId,
      ...updates
    });
  }

  res.json({ success: true, data: pref });
});

// ==========================================
// 6. USER PROFILE REPAIR & UPDATE API
// ==========================================
app.get('/api/user/profile', (req, res) => {
  const userId = 1;
  const user = dbService.findById('users', userId) || {
    id: 1,
    name: 'Ganesh Kumar',
    email: 'ganesh@skillexa.edu',
    role: 'student'
  };

  const pref = dbService.findOne('notification_preferences', { user_id: userId });
  const attempts = dbService.find('quiz_attempts', { user_id: userId });
  const userProgress = dbService.find('user_topic_progress', { user_id: userId });
  const allTopics = dbService.find('topics');

  const totalTopics = allTopics.length;
  const completedTopics = userProgress.filter(p => p.status === 'completed').length;
  const completionPercentage = totalTopics > 0 ? Math.round((completedTopics / totalTopics) * 100) : 0;

  res.json({
    success: true,
    user: {
      ...user,
      target_exams: user.target_exams || ['SSC CGL', 'UPSC CDS', 'KPSC KAS'],
      state: user.state || 'Karnataka',
      bio: user.bio || 'Aspiring candidate for competitive examinations.',
      phone: user.phone || '+91 98765 43210',
      education: user.education || 'Bachelor of Science (B.Sc)',
      streak_days: user.streak_days || 7
    },
    performance_summary: {
      total_topics: totalTopics,
      completed_topics: completedTopics,
      completion_percentage: completionPercentage,
      quizzes_passed: attempts.filter(a => a.passed).length,
      total_attempts: attempts.length,
      average_score: attempts.length > 0 ? Math.round(attempts.reduce((a, b) => a + b.percentage, 0) / attempts.length) : 0
    },
    notification_preferences: pref
  });
});

app.put('/api/user/profile', (req, res) => {
  const userId = 1;
  const { name, email, target_exams, state, phone, education, bio, avatar } = req.body;

  const updates = {};
  if (name !== undefined) updates.name = name;
  if (email !== undefined) updates.email = email;
  if (target_exams !== undefined) updates.target_exams = target_exams;
  if (state !== undefined) updates.state = state;
  if (phone !== undefined) updates.phone = phone;
  if (education !== undefined) updates.education = education;
  if (bio !== undefined) updates.bio = bio;
  if (avatar !== undefined) updates.avatar = avatar;
  updates.last_active = new Date().toISOString();

  const updated = dbService.update('users', userId, updates);
  res.json({ success: true, user: updated, message: 'Profile updated successfully.' });
});

app.get('/api/pyqs', (req, res) => {
  const { exam_id, topic_id, year, subject } = req.query;

  let pyqs = dbService.find('previous_year_questions', { status: 'published' });

  if (exam_id) {
    pyqs = pyqs.filter(p => String(p.exam_id) === String(exam_id));
  }
  if (topic_id) {
    pyqs = pyqs.filter(p => String(p.topic_id) === String(topic_id));
  }

  const enriched = pyqs.map(p => {
    const exam = p.exam_id ? dbService.findById('exams', p.exam_id) : null;
    const source = p.source_id ? dbService.findById('sources', p.source_id) : null;
    const topic = p.topic_id ? dbService.findById('topics', p.topic_id) : null;
    const course = topic ? dbService.findById('courses', topic.course_id) : null;

    return {
      ...p,
      exam,
      source,
      topic,
      course
    };
  });

  // Optional filter by year or subject
  let filtered = enriched;
  if (year) {
    filtered = filtered.filter(p => p.exam && String(p.exam.year) === String(year));
  }
  if (subject) {
    filtered = filtered.filter(p => p.course && p.course.title.toLowerCase().includes(subject.toLowerCase()));
  }

  res.json(filtered);
});

// ==========================================
// 5. CURRENT AFFAIRS
// ==========================================
app.get('/api/current-affairs', (req, res) => {
  const { category } = req.query;
  let items = dbService.find('current_affairs', { status: 'published' });

  if (category && category !== 'All') {
    items = items.filter(i => i.category.toLowerCase().includes(category.toLowerCase()));
  }

  const enriched = items.map(item => {
    const source = item.source_id ? dbService.findById('sources', item.source_id) : null;
    return { ...item, source };
  });

  res.json(enriched);
});

// ==========================================
// 6. SOURCES & EXAMS REGISTRY
// ==========================================
app.get('/api/sources', (req, res) => {
  res.json(dbService.find('sources'));
});

app.get('/api/exams', (req, res) => {
  res.json(dbService.find('exams'));
});

// ==========================================
// 7. USER PROGRESS & MASTERY
// ==========================================
app.get('/api/user/progress', (req, res) => {
  const userId = 1;
  const user = dbService.findById('users', userId);
  const courses = dbService.find('courses');
  const allTopics = dbService.find('topics');
  const userProgress = dbService.find('user_topic_progress', { user_id: userId });
  const attempts = dbService.find('quiz_attempts', { user_id: userId });

  const totalTopics = allTopics.length;
  const completedTopics = userProgress.filter(p => p.status === 'completed').length;
  const overallPercentage = totalTopics > 0 ? Math.round((completedTopics / totalTopics) * 100) : 0;

  const totalQuizzesAttempted = attempts.length;
  const passedQuizzes = attempts.filter(a => a.passed).length;
  const avgQuizScore = attempts.length > 0
    ? Math.round(attempts.reduce((acc, a) => acc + a.percentage, 0) / attempts.length)
    : 0;

  // Course by course breakdown
  const courseBreakdown = courses.map(course => {
    const cTopics = allTopics.filter(t => t.course_id === course.id);
    const cCompleted = cTopics.filter(t => {
      const p = userProgress.find(up => up.topic_id === t.id);
      return p && p.status === 'completed';
    }).length;

    return {
      course_id: course.id,
      title: course.title,
      slug: course.slug,
      icon: course.icon,
      total_topics: cTopics.length,
      completed_topics: cCompleted,
      percentage: cTopics.length > 0 ? Math.round((cCompleted / cTopics.length) * 100) : 0
    };
  });

  res.json({
    user,
    overall: {
      completion_percentage: overallPercentage,
      topics_completed: completedTopics,
      total_topics: totalTopics,
      quizzes_completed: passedQuizzes,
      total_attempts: totalQuizzesAttempted,
      average_score: avgQuizScore,
      streak_days: user?.streak_days || 7
    },
    course_breakdown: courseBreakdown,
    recent_attempts: attempts.slice(-5).reverse().map(a => {
      const topic = dbService.findById('topics', a.topic_id);
      return {
        ...a,
        topic_title: topic?.title || 'Unknown Topic'
      };
    })
  });
});

// Progress Reset for Testing / Demo
app.post('/api/user/progress/reset', (req, res) => {
  dbService.resetToSeed(seedData);
  res.json({ success: true, message: 'Platform data and topic progression reset to default state.' });
});

// ==========================================
// 8. ADMIN CONTENT MANAGEMENT & VERIFICATION
// ==========================================
app.get('/api/admin/content', (req, res) => {
  const { status } = req.query; // 'draft' | 'under_review' | 'verified' | 'published'

  let pyqs = dbService.find('previous_year_questions');
  let lessons = dbService.find('lessons');
  let currentAffairs = dbService.find('current_affairs');

  if (status) {
    pyqs = pyqs.filter(p => p.status === status);
    lessons = lessons.filter(l => l.status === status);
    currentAffairs = currentAffairs.filter(c => c.status === status);
  }

  res.json({
    pyqs: pyqs.map(p => ({ ...p, type: 'PYQ' })),
    lessons: lessons.map(l => ({ ...l, type: 'Lesson' })),
    current_affairs: currentAffairs.map(c => ({ ...c, type: 'Current Affair' })),
    stats: {
      total_courses: dbService.find('courses').length,
      total_topics: dbService.find('topics').length,
      total_pyqs: dbService.find('previous_year_questions').length,
      published_items: dbService.find('previous_year_questions', { status: 'published' }).length +
                       dbService.find('lessons', { status: 'published' }).length,
      verified_sources: dbService.find('sources', { verified_status: 'verified' }).length
    }
  });
});

app.post('/api/admin/verify-and-publish', (req, res) => {
  const { entity_type, id } = req.body; // entity_type: 'pyq' | 'lesson' | 'current_affair'

  let table = 'previous_year_questions';
  if (entity_type === 'lesson') table = 'lessons';
  if (entity_type === 'current_affair') table = 'current_affairs';

  const updated = dbService.update(table, id, { status: 'published' });
  if (!updated) {
    return res.status(404).json({ error: 'Item not found' });
  }

  res.json({ success: true, item: updated, message: `Item #${id} verified and published successfully!` });
});

app.post('/api/admin/pyqs', (req, res) => {
  const { topic_id, exam_id, question, options, correct_answer, explanation, source_id, status } = req.body;

  if (!question || !options || !correct_answer || !source_id) {
    return res.status(400).json({ error: 'Question, options, correct answer and verified source are mandatory.' });
  }

  const created = dbService.insert('previous_year_questions', {
    topic_id: parseInt(topic_id, 10),
    exam_id: exam_id ? parseInt(exam_id, 10) : null,
    question,
    options_json: options,
    correct_answer,
    explanation: explanation || 'Official explanation pending review.',
    source_id: parseInt(source_id, 10),
    status: status || 'published'
  });

  res.status(201).json(created);
});

// ==========================================
// 10. ADMIN CURRENT AFFAIRS CRUD
// ==========================================
app.post('/api/admin/current-affairs', (req, res) => {
  const { title, category, summary, details, important_facts, date, source_name, source_url, questions, status } = req.body;
  if (!title || !category) {
    return res.status(400).json({ error: 'Title and category are required' });
  }

  let sourceId = 6;
  if (source_name) {
    const existingSource = dbService.findOne('sources', { publisher: source_name });
    if (existingSource) {
      sourceId = existingSource.id;
    } else {
      const newSource = dbService.insert('sources', {
        title: source_name,
        type: 'Official Portal',
        publisher: source_name,
        url: source_url || 'https://pib.gov.in',
        publication_date: date || new Date().toISOString().split('T')[0],
        accessed_date: new Date().toISOString().split('T')[0],
        verified_status: 'verified'
      });
      sourceId = newSource.id;
    }
  }

  const created = dbService.insert('current_affairs', {
    title,
    category,
    summary: summary || details || '',
    details: details || summary || '',
    important_facts: important_facts || [],
    date: date || new Date().toISOString().split('T')[0],
    source_id: sourceId,
    source_name: source_name || 'Press Information Bureau (PIB)',
    source_url: source_url || 'https://pib.gov.in',
    questions: questions || [],
    status: status || 'published'
  });

  res.status(201).json({ success: true, item: created });
});

app.put('/api/admin/current-affairs/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const updates = req.body;
  const updated = dbService.update('current_affairs', id, updates);
  if (!updated) {
    return res.status(404).json({ error: 'Current Affair not found' });
  }
  res.json({ success: true, item: updated });
});

app.delete('/api/admin/current-affairs/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const deleted = dbService.delete('current_affairs', id);
  if (!deleted) {
    return res.status(404).json({ error: 'Current Affair not found' });
  }
  res.json({ success: true, message: 'Current Affair deleted successfully' });
});

// ==========================================
// 11. STUDY NOTES & PDF REPOSITORY ENGINE
// ==========================================

// Public Notes Feed for Students (ONLY VERIFIED + PUBLISHED)
app.get('/api/notes', (req, res) => {
  const { subject, topic, search } = req.query;

  // Requirement 8: Only VERIFIED + PUBLISHED PDFs appear in normal user's Notes section
  let notes = dbService.find('notes', { status: 'PUBLISHED' });

  // Filter by subject
  if (subject && subject !== 'All') {
    notes = notes.filter(n => (n.subject_name || '').toLowerCase() === subject.toLowerCase() || (n.subject_name || '').toLowerCase().includes(subject.toLowerCase()));
  }

  // Filter by topic
  if (topic && topic !== 'All') {
    notes = notes.filter(n => (n.topic_name || '').toLowerCase() === topic.toLowerCase() || (n.topic_name || '').toLowerCase().includes(topic.toLowerCase()));
  }

  // Filter by search query (title, subject, topic, description)
  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    notes = notes.filter(n => 
      (n.title || '').toLowerCase().includes(q) ||
      (n.subject_name || '').toLowerCase().includes(q) ||
      (n.topic_name || '').toLowerCase().includes(q) ||
      (n.subtopic_name || '').toLowerCase().includes(q) ||
      (n.description || '').toLowerCase().includes(q)
    );
  }

  // Sort by newest first
  notes.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

  res.json({
    success: true,
    total: notes.length,
    data: notes
  });
});

// Single Note Details
app.get('/api/notes/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const note = dbService.findById('notes', id);
  if (!note) {
    return res.status(404).json({ error: 'Study note not found' });
  }
  res.json({ success: true, data: note });
});

// Admin: Get All Notes with Status Breakdown
app.get('/api/admin/notes', requireAdmin, (req, res) => {
  const { status, subject, search } = req.query;
  let list = dbService.find('notes');

  if (status && status !== 'All') {
    list = list.filter(n => n.status === status);
  }

  if (subject && subject !== 'All') {
    list = list.filter(n => (n.subject_name || '').toLowerCase().includes(subject.toLowerCase()));
  }

  if (search && search.trim()) {
    const q = search.trim().toLowerCase();
    list = list.filter(n => 
      (n.title || '').toLowerCase().includes(q) ||
      (n.subject_name || '').toLowerCase().includes(q) ||
      (n.topic_name || '').toLowerCase().includes(q) ||
      (n.file_name || '').toLowerCase().includes(q)
    );
  }

  list.sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0));

  const allNotes = dbService.find('notes');
  const counts = {
    total: allNotes.length,
    draft: allNotes.filter(n => n.status === 'DRAFT').length,
    pending_review: allNotes.filter(n => n.status === 'PENDING_REVIEW').length,
    verified: allNotes.filter(n => n.status === 'VERIFIED').length,
    published: allNotes.filter(n => n.status === 'PUBLISHED').length,
    archived: allNotes.filter(n => n.status === 'ARCHIVED').length
  };

  res.json({
    success: true,
    counts,
    total: list.length,
    data: list
  });
});

// Admin: Upload New PDF Note
app.post('/api/admin/notes', requireAdmin, upload.single('pdf'), (req, res) => {
  const { title, subject_name, topic_name, subtopic_name, description, source, page_count, status } = req.body;

  if (!req.file) {
    return res.status(400).json({ error: 'Please choose an actual PDF file to upload.' });
  }

  if (!title || !subject_name || !topic_name) {
    // If validation fails, clean up the uploaded file
    try { fs.unlinkSync(req.file.path); } catch (e) {}
    return res.status(400).json({ error: 'Title, Subject, and Topic are mandatory.' });
  }

  const validStatuses = ['DRAFT', 'PENDING_REVIEW', 'VERIFIED', 'PUBLISHED', 'ARCHIVED'];
  const noteStatus = validStatuses.includes(status) ? status : 'DRAFT';
  const now = new Date().toISOString();

  const created = dbService.insert('notes', {
    title: title.trim(),
    file_name: req.file.originalname,
    file_url: `/uploads/notes/${req.file.filename}`,
    file_path: req.file.path,
    subject_name: subject_name.trim(),
    topic_name: topic_name.trim(),
    subtopic_name: (subtopic_name || '').trim(),
    description: (description || '').trim(),
    source: (source || 'Official Course Material').trim(),
    file_size: formatBytes(req.file.size),
    file_bytes: req.file.size,
    page_count: parseInt(page_count, 10) || null,
    status: noteStatus,
    uploaded_by: 'Administrator',
    created_at: now,
    updated_at: now
  });

  res.status(201).json({
    success: true,
    data: created,
    message: 'PDF note uploaded and saved successfully.'
  });
});

// Admin: Edit Note Metadata or Replace File
app.put('/api/admin/notes/:id', requireAdmin, upload.single('pdf'), (req, res) => {
  const id = parseInt(req.params.id, 10);
  const existing = dbService.findById('notes', id);
  if (!existing) {
    if (req.file) {
      try { fs.unlinkSync(req.file.path); } catch (e) {}
    }
    return res.status(404).json({ error: 'Study note not found' });
  }

  const { title, subject_name, topic_name, subtopic_name, description, source, page_count, status } = req.body;
  const updates = {
    updated_at: new Date().toISOString()
  };

  if (title !== undefined) updates.title = title.trim();
  if (subject_name !== undefined) updates.subject_name = subject_name.trim();
  if (topic_name !== undefined) updates.topic_name = topic_name.trim();
  if (subtopic_name !== undefined) updates.subtopic_name = (subtopic_name || '').trim();
  if (description !== undefined) updates.description = (description || '').trim();
  if (source !== undefined) updates.source = (source || '').trim();
  if (page_count !== undefined) updates.page_count = parseInt(page_count, 10) || null;
  if (status !== undefined) updates.status = status;

  // If a new replacement PDF was uploaded:
  if (req.file) {
    // Delete old file from disk
    if (existing.file_path && fs.existsSync(existing.file_path)) {
      try { fs.unlinkSync(existing.file_path); } catch (e) {}
    }
    updates.file_name = req.file.originalname;
    updates.file_url = `/uploads/notes/${req.file.filename}`;
    updates.file_path = req.file.path;
    updates.file_size = formatBytes(req.file.size);
    updates.file_bytes = req.file.size;
  }

  const updated = dbService.update('notes', id, updates);
  res.json({ success: true, data: updated, message: 'Study note updated successfully.' });
});

// Admin: Update Note Status (DRAFT -> PENDING_REVIEW -> VERIFIED -> PUBLISHED -> ARCHIVED)
app.patch('/api/admin/notes/:id/status', requireAdmin, (req, res) => {
  const id = parseInt(req.params.id, 10);
  const { status } = req.body;

  const validStatuses = ['DRAFT', 'PENDING_REVIEW', 'VERIFIED', 'PUBLISHED', 'ARCHIVED'];
  if (!validStatuses.includes(status)) {
    return res.status(400).json({ error: `Invalid status. Must be one of: ${validStatuses.join(', ')}` });
  }

  const note = dbService.findById('notes', id);
  if (!note) {
    return res.status(404).json({ error: 'Study note not found' });
  }

  const updated = dbService.update('notes', id, {
    status,
    updated_at: new Date().toISOString()
  });

  res.json({ success: true, data: updated, message: `Note status updated to ${status}.` });
});

// Admin: Delete Note and File
app.delete('/api/admin/notes/:id', requireAdmin, (req, res) => {
  const id = parseInt(req.params.id, 10);
  const note = dbService.findById('notes', id);
  if (!note) {
    return res.status(404).json({ error: 'Study note not found' });
  }

  // Remove actual PDF from disk if exists
  if (note.file_path && fs.existsSync(note.file_path)) {
    try {
      fs.unlinkSync(note.file_path);
    } catch (e) {
      console.error('Error removing PDF file:', e);
    }
  }

  dbService.delete('notes', id);
  res.json({ success: true, message: `Study note #${id} deleted successfully.` });
});


// Start listening
app.listen(PORT, () => {
  console.log(`Skillexa Backend API running at http://localhost:${PORT}`);
});
