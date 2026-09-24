import React, { useState, useEffect } from 'react';
import { 
  ShieldCheck, 
  CheckCircle, 
  FileText, 
  Plus, 
  Upload, 
  Award, 
  BookOpen, 
  ExternalLink,
  Layers,
  Sparkles,
  AlertCircle,
  Edit2,
  Trash2,
  Globe,
  Calendar,
  Eye,
  EyeOff,
  Building2,
  Bell,
  Send,
  AlertTriangle,
  CheckCircle2,
  Filter,
  Search,
  X,
  ChevronRight,
  Download,
  Target,
  Clock,
  HelpCircle,
  Check
} from 'lucide-react';

export default function AdminDashboardPage({ navigateTo }) {
  const [activeTab, setActiveTab] = useState('notes'); // 'notes' | 'mock-exams' | 'govt-exams' | 'pyqs' | 'current-affairs'
  const [adminData, setAdminData] = useState(null);
  const [statusFilter, setStatusFilter] = useState('');
  const [loading, setLoading] = useState(true);

  // Security Role Check
  const [userRole, setUserRole] = useState(() => localStorage.getItem('skillexa_user_role') || 'admin');

  useEffect(() => {
    const handleRoleChanged = () => {
      setUserRole(localStorage.getItem('skillexa_user_role') || 'admin');
    };
    window.addEventListener('skillexa_role_changed', handleRoleChanged);
    return () => window.removeEventListener('skillexa_role_changed', handleRoleChanged);
  }, []);

  // Notes Management State
  const [notesList, setNotesList] = useState([]);
  const [noteCounts, setNoteCounts] = useState({ total: 0, draft: 0, pending_review: 0, verified: 0, published: 0, archived: 0 });
  const [noteStatusFilter, setNoteStatusFilter] = useState('All');
  const [noteSubjectFilter, setNoteSubjectFilter] = useState('All');
  const [noteSearchQuery, setNoteSearchQuery] = useState('');
  const [showNoteModal, setShowNoteModal] = useState(false);
  const [editingNote, setEditingNote] = useState(null);
  const [previewingNote, setPreviewingNote] = useState(null);
  const [notePdfFile, setNotePdfFile] = useState(null);
  const [noteUploading, setNoteUploading] = useState(false);
  const [noteFormError, setNoteFormError] = useState('');

  const defaultNoteForm = {
    title: '',
    subject_name: 'English',
    topic_name: '',
    subtopic_name: '',
    description: '',
    source: 'Official Faculty Curriculum',
    page_count: '',
    status: 'DRAFT'
  };
  const [noteForm, setNoteForm] = useState(defaultNoteForm);

  // Mock Exams State (Minimum 50 Questions Policy)
  const [mockExamsList, setMockExamsList] = useState([]);
  const [mockCategoryFilter, setMockCategoryFilter] = useState('All');
  const [mockStatusFilter, setMockStatusFilter] = useState('All');
  const [mockSearchQuery, setMockSearchQuery] = useState('');
  const [showCreateMockModal, setShowCreateMockModal] = useState(false);
  const [editingMockExam, setEditingMockExam] = useState(null);
  const [previewingMockExam, setPreviewingMockExam] = useState(null);
  const [questionBank, setQuestionBank] = useState([]);
  const [qbSubjectFilter, setQbSubjectFilter] = useState('All');
  const [qbSearchQuery, setQbSearchQuery] = useState('');
  const [mockFormError, setMockFormError] = useState('');
  const [mockSaving, setMockSaving] = useState(false);
  const [autoAssembling, setAutoAssembling] = useState(false);
  const [activePreparedTab, setActivePreparedTab] = useState('auto'); // 'auto' | 'bank' | 'author'
  const [mockSubTab, setMockSubTab] = useState('exams'); // 'exams' | 'questions'

  // Question Authoring & Management State
  const [showAddQuestionModal, setShowAddQuestionModal] = useState(false);
  const [questionSaving, setQuestionSaving] = useState(false);
  const [questionFormError, setQuestionFormError] = useState('');

  const defaultQuestionForm = {
    question: '',
    question_type: 'MCQ', // 'MCQ' | 'FILL_IN_THE_BLANK'
    option_a: '',
    option_b: '',
    option_c: '',
    option_d: '',
    correct_answer: 'A',
    explanation: '',
    subject: 'Quantitative Aptitude',
    topic: 'General Practice',
    points: 2,
    attach_to_current_mock: true
  };
  const [questionForm, setQuestionForm] = useState(defaultQuestionForm);

  const defaultMockForm = {
    title: '',
    category: 'SSC',
    target_exam: 'SSC CGL / CHSL',
    description: '',
    duration_minutes: 60,
    passing_percentage: 70,
    negative_marking: 0.25,
    instructions: '1. This mock exam contains a minimum of 50 objective questions.\n2. Total time allotted is 60 minutes.\n3. Each question carries 2 marks (total 100 marks).\n4. Negative marking of 0.25 marks applies to incorrect responses.',
    creation_mode: 'auto', // 'auto' | 'manual'
    subject_distribution: {
      english: 15,
      math: 15,
      reasoning: 10,
      general_awareness: 10
    },
    selected_question_ids: [],
    status: 'published'
  };
  const [mockForm, setMockForm] = useState(defaultMockForm);

  // Government Exams State
  const [govtExams, setGovtExams] = useState([]);
  const [govtCounts, setGovtCounts] = useState({ total: 0, draft: 0, pending_review: 0, verified: 0, published: 0, rejected: 0, archived: 0 });
  const [govtStatusFilter, setGovtStatusFilter] = useState('All');
  const [govtCategoryFilter, setGovtCategoryFilter] = useState('All');
  const [govtSearchQuery, setGovtSearchQuery] = useState('');
  const [examCategories, setExamCategories] = useState([]);
  const [showGovtModal, setShowGovtModal] = useState(false);
  const [editingGovt, setEditingGovt] = useState(null);
  const [govtDuplicateWarning, setGovtDuplicateWarning] = useState(null);
  const [showPublishConfirm, setShowPublishConfirm] = useState(null);
  const [sendPushOnPublish, setSendPushOnPublish] = useState(true);
  const [newCatName, setNewCatName] = useState('');
  const [newCatGroup, setNewCatGroup] = useState('Central Government');
  const [showAddCatInline, setShowAddCatInline] = useState(false);

  const defaultGovtForm = {
    exam_name: '',
    organization: 'Staff Selection Commission (SSC)',
    category: 'SSC',
    update_type: 'EXAM_NOTIFICATION',
    official_notification_number: '',
    title: '',
    short_description: '',
    full_description: '',
    post_name: '',
    vacancy: '',
    eligibility: '',
    age_limit: '',
    qualification: '',
    application_fee: '',
    selection_process: '',
    notification_date: new Date().toISOString().split('T')[0],
    application_start_date: '',
    application_last_date: '',
    correction_date: '',
    exam_date: '',
    admit_card_date: '',
    answer_key_date: '',
    result_date: '',
    official_source_name: 'Official Commission Portal',
    official_source_url: 'https://ssc.gov.in',
    verification_status: 'DRAFT',
    send_push_notification: false
  };

  const [govtForm, setGovtForm] = useState(defaultGovtForm);

  // PYQ Modal & Form State
  const [showAddModal, setShowAddModal] = useState(false);
  const [newPyq, setNewPyq] = useState({
    topic_id: '1',
    exam_id: '1',
    question: '',
    optionA: '',
    optionB: '',
    optionC: '',
    optionD: '',
    correct_answer: '',
    explanation: '',
    source_id: '3',
    status: 'published'
  });

  // Current Affairs Modal & Form State
  const [showCaModal, setShowCaModal] = useState(false);
  const [editingCa, setEditingCa] = useState(null);
  const [caForm, setCaForm] = useState({
    title: '',
    category: 'Science & Technology',
    date: new Date().toISOString().split('T')[0],
    summary: '',
    important_facts: '',
    source_name: 'Press Information Bureau (PIB)',
    source_url: 'https://pib.gov.in',
    status: 'published'
  });

  useEffect(() => {
    if (activeTab === 'mock-exams') {
      fetchAdminMockExams();
    } else if (activeTab === 'notes') {
      fetchAdminNotes();
    } else if (activeTab === 'govt-exams') {
      fetchGovtExams();
      fetchCategories();
    } else {
      fetchAdminData();
    }
  }, [activeTab, statusFilter, govtStatusFilter, govtCategoryFilter, noteStatusFilter, noteSubjectFilter, mockCategoryFilter, mockStatusFilter]);

  const fetchAdminMockExams = async () => {
    try {
      setMockLoading(true);
      const res = await fetch('http://localhost:3001/api/admin/mock-exams', {
        headers: { 'x-user-role': 'admin' }
      });
      if (res.ok) {
        const json = await res.json();
        setMockExamsList(json.data || []);
      }
    } catch (err) {
      console.error('Error fetching admin mock exams:', err);
    } finally {
      setMockLoading(false);
    }
  };

  const fetchQuestionBank = async (subject = qbSubjectFilter, search = qbSearchQuery) => {
    try {
      const params = new URLSearchParams();
      if (subject !== 'All') params.append('subject', subject);
      if (search.trim()) params.append('search', search.trim());
      const res = await fetch(`http://localhost:3001/api/admin/mock-exams/question-bank?${params.toString()}`, {
        headers: { 'x-user-role': 'admin' }
      });
      if (res.ok) {
        const json = await res.json();
        setQuestionBank(json.data || []);
      }
    } catch (err) {
      console.error('Error loading question bank:', err);
    }
  };

  const handleOpenCreateMockModal = () => {
    setEditingMockExam(null);
    const newTitle = `SSC CGL Tier-1 Grand Full-Length Mock Exam #${mockExamsList.length + 1}`;
    setMockForm({
      ...defaultMockForm,
      title: newTitle,
      selected_question_ids: []
    });
    setMockFormError('');
    setShowCreateMockModal(true);
    setActivePreparedTab('auto');
    fetchQuestionBank('All', '');
    // Auto-assemble a full 50-question set immediately so it's ready right away
    handleApplyPreset('ssc');
  };

  const handleApplyPreset = async (presetName) => {
    try {
      setAutoAssembling(true);
      const res = await fetch('http://localhost:3001/api/admin/mock-exams/generate-set', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-role': 'admin'
        },
        body: JSON.stringify({ preset: presetName })
      });
      if (res.ok) {
        const json = await res.json();
        const ids = json.question_ids || [];
        setMockForm(prev => ({
          ...prev,
          selected_question_ids: ids,
          subject_distribution: presetName === 'ssc'
            ? { english: 15, math: 15, reasoning: 10, general_awareness: 10 }
            : presetName === 'railway'
              ? { english: 10, math: 15, reasoning: 15, general_awareness: 10 }
              : presetName === 'banking'
                ? { english: 20, math: 15, reasoning: 15, general_awareness: 0 }
                : { english: 12, math: 13, reasoning: 13, general_awareness: 12 }
        }));
      }
    } catch (err) {
      console.error('Error auto-assembling set:', err);
    } finally {
      setAutoAssembling(false);
    }
  };

  const handleOpenAddQuestionModal = (defaultSubject = 'Quantitative Aptitude') => {
    setQuestionForm({
      ...defaultQuestionForm,
      subject: defaultSubject,
      attach_to_current_mock: showCreateMockModal || !!editingMockExam
    });
    setQuestionFormError('');
    setShowAddQuestionModal(true);
  };

  const handleSaveNewQuestion = async (e) => {
    e.preventDefault();
    setQuestionFormError('');

    if (!questionForm.question.trim()) {
      setQuestionFormError('Question prompt is required.');
      return;
    }

    let finalOptions = [];
    let finalAnswer = questionForm.correct_answer;

    if (questionForm.question_type === 'MCQ') {
      if (!questionForm.option_a.trim() || !questionForm.option_b.trim()) {
        setQuestionFormError('At least Option A and Option B are required for MCQ questions.');
        return;
      }
      finalOptions = [
        questionForm.option_a.trim(),
        questionForm.option_b.trim(),
        questionForm.option_c.trim(),
        questionForm.option_d.trim()
      ].filter(Boolean);

      const map = {
        'A': questionForm.option_a.trim(),
        'B': questionForm.option_b.trim(),
        'C': questionForm.option_c.trim(),
        'D': questionForm.option_d.trim()
      };
      finalAnswer = map[questionForm.correct_answer] || questionForm.correct_answer;
    } else {
      if (!questionForm.correct_answer.trim()) {
        setQuestionFormError('Correct answer is required.');
        return;
      }
      finalAnswer = questionForm.correct_answer.trim();
    }

    try {
      setQuestionSaving(true);
      const payload = {
        question: questionForm.question.trim(),
        question_type: questionForm.question_type,
        options: finalOptions,
        correct_answer: finalAnswer,
        explanation: questionForm.explanation.trim(),
        subject: questionForm.subject,
        topic: questionForm.topic.trim(),
        points: parseInt(questionForm.points, 10) || 2,
        mock_exam_id: (editingMockExam && questionForm.attach_to_current_mock) ? editingMockExam.id : undefined
      };

      const res = await fetch('http://localhost:3001/api/admin/mock-exams/questions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-role': 'admin'
        },
        body: JSON.stringify(payload)
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.error || 'Failed to save question');
      }

      const createdQ = resData.data;

      // Immediately add this new question to current mock exam selection!
      if (showCreateMockModal || questionForm.attach_to_current_mock) {
        setMockForm(prev => ({
          ...prev,
          selected_question_ids: Array.from(new Set([createdQ.id, ...prev.selected_question_ids]))
        }));
      }

      setShowAddQuestionModal(false);
      setQuestionForm(defaultQuestionForm);
      fetchQuestionBank(qbSubjectFilter, qbSearchQuery);
      if (editingMockExam) fetchAdminMockExams();
    } catch (err) {
      setQuestionFormError(err.message || 'Error saving question');
    } finally {
      setQuestionSaving(false);
    }
  };

  const handleDeleteQuestion = async (qid, qText) => {
    if (!window.confirm(`Delete this question from question bank?\n"${(qText || '').substring(0, 60)}..."`)) return;
    try {
      const res = await fetch(`http://localhost:3001/api/admin/mock-exams/questions/${qid}`, {
        method: 'DELETE',
        headers: { 'x-user-role': 'admin' }
      });
      if (res.ok) {
        fetchQuestionBank(qbSubjectFilter, qbSearchQuery);
      }
    } catch (err) {
      console.error('Error deleting question:', err);
    }
  };

  const handleOpenEditMockModal = (exam) => {
    setEditingMockExam(exam);
    setMockForm({
      title: exam.title || '',
      category: exam.category || 'SSC',
      target_exam: exam.target_exam || 'SSC CGL / CHSL',
      description: exam.description || '',
      duration_minutes: exam.duration_minutes || 60,
      passing_percentage: exam.passing_percentage || 70,
      negative_marking: exam.negative_marking !== undefined ? exam.negative_marking : 0.25,
      instructions: exam.instructions || '',
      creation_mode: 'manual',
      subject_distribution: { english: 15, math: 15, reasoning: 10, general_awareness: 10 },
      selected_question_ids: exam.question_ids || [],
      status: exam.status || 'published'
    });
    setMockFormError('');
    setShowCreateMockModal(true);
    setActivePreparedTab('bank');
    fetchQuestionBank('All', '');
  };

  const handleSaveMockExam = async (e) => {
    e.preventDefault();
    setMockFormError('');

    if (!mockForm.title.trim()) {
      setMockFormError('Mock Exam Title is required.');
      return;
    }

    const selectedIds = mockForm.selected_question_ids || [];

    // Strictly validate minimum 50 questions
    if (selectedIds.length < 50) {
      setMockFormError(`A minimum of 50 questions is required for a complete competitive mock exam. Currently selected: ${selectedIds.length} / 50 questions. Please add ${50 - selectedIds.length} more questions or click one of the 1-Click Presets.`);
      return;
    }

    try {
      setMockSaving(true);
      const payload = {
        title: mockForm.title.trim(),
        category: mockForm.category,
        target_exam: mockForm.target_exam,
        description: mockForm.description.trim(),
        duration_minutes: parseInt(mockForm.duration_minutes, 10) || 60,
        passing_percentage: parseInt(mockForm.passing_percentage, 10) || 70,
        negative_marking: parseFloat(mockForm.negative_marking) || 0.25,
        instructions: mockForm.instructions,
        status: mockForm.status,
        question_ids: selectedIds
      };

      const url = editingMockExam
        ? `http://localhost:3001/api/admin/mock-exams/${editingMockExam.id}`
        : 'http://localhost:3001/api/admin/mock-exams';
      const method = editingMockExam ? 'PUT' : 'POST';

      const res = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'x-user-role': 'admin'
        },
        body: JSON.stringify(payload)
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.error || 'Failed to save mock exam');
      }

      setShowCreateMockModal(false);
      fetchAdminMockExams();
    } catch (err) {
      setMockFormError(err.message || 'Error creating mock exam');
    } finally {
      setMockSaving(false);
    }
  };

  const handleToggleMockStatus = async (examId, currentStatus) => {
    try {
      const newStatus = currentStatus === 'published' ? 'draft' : 'published';
      const res = await fetch(`http://localhost:3001/api/admin/mock-exams/${examId}/status`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'x-user-role': 'admin'
        },
        body: JSON.stringify({ status: newStatus })
      });
      if (res.ok) {
        fetchAdminMockExams();
      }
    } catch (err) {
      console.error('Error toggling mock exam status:', err);
    }
  };

  const handleDeleteMockExam = async (examId, title) => {
    if (!window.confirm(`Are you sure you want to delete mock exam "${title}"?`)) return;
    try {
      const res = await fetch(`http://localhost:3001/api/admin/mock-exams/${examId}`, {
        method: 'DELETE',
        headers: { 'x-user-role': 'admin' }
      });
      if (res.ok) {
        fetchAdminMockExams();
      }
    } catch (err) {
      console.error('Error deleting mock exam:', err);
    }
  };

  const handlePreviewMockExam = async (exam) => {
    try {
      const res = await fetch(`http://localhost:3001/api/mock-exams/${exam.id}`);
      if (res.ok) {
        const json = await res.json();
        setPreviewingMockExam(json.data || exam);
      }
    } catch (err) {
      console.error('Error previewing mock exam:', err);
    }
  };

  const fetchAdminNotes = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (noteStatusFilter !== 'All') params.append('status', noteStatusFilter);
      if (noteSubjectFilter !== 'All') params.append('subject', noteSubjectFilter);
      if (noteSearchQuery.trim()) params.append('search', noteSearchQuery.trim());

      const res = await fetch(`http://localhost:3001/api/admin/notes?${params.toString()}`, {
        headers: { 'x-user-role': 'admin' }
      });
      if (res.ok) {
        const json = await res.json();
        setNotesList(json.data || []);
        setNoteCounts(json.counts || { total: 0, draft: 0, pending_review: 0, verified: 0, published: 0, archived: 0 });
      }
    } catch (err) {
      console.error('Error fetching admin notes:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleOpenAddNoteModal = () => {
    setEditingNote(null);
    setNotePdfFile(null);
    setNoteForm(defaultNoteForm);
    setNoteFormError('');
    setShowNoteModal(true);
  };

  const handleOpenEditNoteModal = (note) => {
    setEditingNote(note);
    setNotePdfFile(null);
    setNoteForm({
      title: note.title || '',
      subject_name: note.subject_name || 'English',
      topic_name: note.topic_name || '',
      subtopic_name: note.subtopic_name || '',
      description: note.description || '',
      source: note.source || '',
      page_count: note.page_count ? String(note.page_count) : '',
      status: note.status || 'DRAFT'
    });
    setNoteFormError('');
    setShowNoteModal(true);
  };

  const handleSaveNote = async (e) => {
    e.preventDefault();
    setNoteFormError('');

    if (!noteForm.title.trim()) {
      setNoteFormError('Note Title is required.');
      return;
    }
    if (!noteForm.subject_name.trim()) {
      setNoteFormError('Subject is required.');
      return;
    }
    if (!noteForm.topic_name.trim()) {
      setNoteFormError('Topic is required.');
      return;
    }

    if (!editingNote && !notePdfFile) {
      setNoteFormError('Please select a real PDF file to upload.');
      return;
    }

    try {
      setNoteUploading(true);
      const formData = new FormData();
      formData.append('title', noteForm.title.trim());
      formData.append('subject_name', noteForm.subject_name.trim());
      formData.append('topic_name', noteForm.topic_name.trim());
      formData.append('subtopic_name', (noteForm.subtopic_name || '').trim());
      formData.append('description', (noteForm.description || '').trim());
      formData.append('source', (noteForm.source || '').trim());
      if (noteForm.page_count) formData.append('page_count', noteForm.page_count);
      formData.append('status', noteForm.status);

      if (notePdfFile) {
        formData.append('pdf', notePdfFile);
      }

      const url = editingNote 
        ? `http://localhost:3001/api/admin/notes/${editingNote.id}`
        : 'http://localhost:3001/api/admin/notes';
      const method = editingNote ? 'PUT' : 'POST';

      const res = await fetch(url, {
        method,
        headers: {
          'x-user-role': 'admin'
        },
        body: formData
      });

      const resData = await res.json();
      if (!res.ok) {
        throw new Error(resData.error || 'Failed to save note');
      }

      setShowNoteModal(false);
      fetchAdminNotes();
    } catch (err) {
      setNoteFormError(err.message || 'Error uploading and saving PDF note');
    } finally {
      setNoteUploading(false);
    }
  };

  const handleUpdateNoteStatus = async (noteId, newStatus) => {
    try {
      const res = await fetch(`http://localhost:3001/api/admin/notes/${noteId}/status`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'x-user-role': 'admin'
        },
        body: JSON.stringify({ status: newStatus })
      });
      if (res.ok) {
        fetchAdminNotes();
      } else {
        const err = await res.json();
        alert(err.error || 'Failed to update note status');
      }
    } catch (err) {
      console.error('Error updating note status:', err);
    }
  };

  const handleDeleteNote = async (noteId, noteTitle) => {
    if (!window.confirm(`Are you sure you want to permanently delete "${noteTitle}" and its PDF file?`)) {
      return;
    }
    try {
      const res = await fetch(`http://localhost:3001/api/admin/notes/${noteId}`, {
        method: 'DELETE',
        headers: {
          'x-user-role': 'admin'
        }
      });
      if (res.ok) {
        fetchAdminNotes();
      } else {
        const err = await res.json();
        alert(err.error || 'Failed to delete note');
      }
    } catch (err) {
      console.error('Error deleting note:', err);
    }
  };

  const fetchGovtExams = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (govtStatusFilter !== 'All') params.append('status', govtStatusFilter);
      if (govtCategoryFilter !== 'All') params.append('category', govtCategoryFilter);
      if (govtSearchQuery.trim()) params.append('search', govtSearchQuery.trim());

      const res = await fetch(`http://localhost:3001/api/admin/government-exams/all?${params.toString()}`);
      if (res.ok) {
        const data = await res.json();
        setGovtExams(data.data || []);
        setGovtCounts(data.counts || {});
      }
    } catch (err) {
      console.error('Error fetching admin govt exams:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchCategories = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/exam-categories');
      if (res.ok) {
        const data = await res.json();
        setExamCategories(data.data || []);
      }
    } catch (err) {
      console.error('Error loading categories:', err);
    }
  };

  const handleOpenGovtModal = (exam = null) => {
    setGovtDuplicateWarning(null);
    if (exam) {
      setEditingGovt(exam);
      setGovtForm({
        exam_name: exam.exam_name || '',
        organization: exam.organization || '',
        category: exam.category || 'SSC',
        update_type: exam.update_type || 'EXAM_NOTIFICATION',
        official_notification_number: exam.official_notification_number || '',
        title: exam.title || '',
        short_description: exam.short_description || '',
        full_description: exam.full_description || '',
        post_name: exam.post_name || '',
        vacancy: exam.vacancy || '',
        eligibility: exam.eligibility || '',
        age_limit: exam.age_limit || '',
        qualification: exam.qualification || '',
        application_fee: exam.application_fee || '',
        selection_process: exam.selection_process || '',
        notification_date: exam.notification_date || '',
        application_start_date: exam.application_start_date || '',
        application_last_date: exam.application_last_date || '',
        correction_date: exam.correction_date || '',
        exam_date: exam.exam_date || '',
        admit_card_date: exam.admit_card_date || '',
        answer_key_date: exam.answer_key_date || '',
        result_date: exam.result_date || '',
        official_source_name: exam.official_source_name || '',
        official_source_url: exam.official_source_url || '',
        verification_status: exam.verification_status || 'DRAFT',
        send_push_notification: false
      });
    } else {
      setEditingGovt(null);
      setGovtForm(defaultGovtForm);
    }
    setShowGovtModal(true);
  };

  const handleSaveGovtExam = async (e, force = false) => {
    if (e && e.preventDefault) e.preventDefault();
    if (!govtForm.exam_name || !govtForm.organization || !govtForm.title) {
      alert('Exam Name, Organization, and Title are mandatory.');
      return;
    }
    if (!govtForm.official_source_name || !govtForm.official_source_url) {
      alert('Official Source Name and Official Source URL are mandatory.');
      return;
    }

    try {
      const payload = { ...govtForm, force_duplicate: force };
      let res;
      if (editingGovt) {
        res = await fetch(`http://localhost:3001/api/admin/government-exams/${editingGovt.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } else {
        res = await fetch('http://localhost:3001/api/admin/government-exams', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }

      const resData = await res.json();
      if (res.status === 409 && resData.is_duplicate) {
        setGovtDuplicateWarning(resData.error);
        return;
      }

      if (res.ok) {
        alert(editingGovt ? 'Exam update updated successfully!' : 'Exam update created successfully!');
        setShowGovtModal(false);
        setGovtDuplicateWarning(null);
        fetchGovtExams();
      } else {
        alert(resData.error || 'Failed to save exam update.');
      }
    } catch (err) {
      console.error(err);
      alert('Error saving exam update.');
    }
  };

  const handleTransitionStatus = async (id, newStatus, sendPush = false) => {
    try {
      const res = await fetch(`http://localhost:3001/api/admin/government-exams/${id}/status`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus, send_push_notification: sendPush })
      });
      const data = await res.json();
      if (res.ok) {
        if (data.notification_dispatched) {
          alert(`Status transitioned to ${newStatus}. Push notification dispatched to eligible students!`);
        } else {
          alert(`Status transitioned to ${newStatus}.`);
        }
        setShowPublishConfirm(null);
        fetchGovtExams();
      } else {
        alert(data.error || 'Failed to transition status.');
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteGovtExam = async (id, name) => {
    if (!window.confirm(`Are you sure you want to delete exam update: "${name}"?`)) return;
    try {
      const res = await fetch(`http://localhost:3001/api/admin/government-exams/${id}`, {
        method: 'DELETE'
      });
      if (res.ok) {
        alert('Deleted successfully.');
        fetchGovtExams();
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleCheckDeadlines = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/notifications/check-deadlines', { method: 'POST' });
      const data = await res.json();
      alert(`Deadline scan completed! ${data.reminders_sent || 0} deadline reminders sent to students.`);
    } catch (err) {
      console.error(err);
    }
  };

  const handleAddCategory = async (e) => {
    e.preventDefault();
    if (!newCatName.trim()) return;
    try {
      const res = await fetch('http://localhost:3001/api/admin/exam-categories', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newCatName.trim(), group: newCatGroup })
      });
      if (res.ok) {
        alert('Category added successfully!');
        setNewCatName('');
        setShowAddCatInline(false);
        fetchCategories();
      } else {
        const d = await res.json();
        alert(d.error || 'Failed to add category');
      }
    } catch (err) {
      console.error(err);
    }
  };

  const fetchAdminData = async () => {
    try {
      setLoading(true);
      const url = statusFilter 
        ? `http://localhost:3001/api/admin/content?status=${statusFilter}`
        : 'http://localhost:3001/api/admin/content';
      const res = await fetch(url);
      const data = await res.json();
      setAdminData(data);
    } catch (err) {
      console.error('Error fetching admin data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyAndPublish = async (entityType, id) => {
    try {
      const res = await fetch('http://localhost:3001/api/admin/verify-and-publish', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ entity_type: entityType, id })
      });
      const resData = await res.json();
      alert(resData.message || 'Item published successfully!');
      fetchAdminData();
    } catch (err) {
      console.error('Error updating status:', err);
    }
  };

  const handleCreatePyq = async (e) => {
    e.preventDefault();
    if (!newPyq.question || !newPyq.correct_answer) {
      alert('Question and correct answer are required.');
      return;
    }

    try {
      const options = [newPyq.optionA, newPyq.optionB, newPyq.optionC, newPyq.optionD].filter(Boolean);
      const res = await fetch('http://localhost:3001/api/admin/pyqs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          topic_id: newPyq.topic_id,
          exam_id: newPyq.exam_id,
          question: newPyq.question,
          options,
          correct_answer: newPyq.correct_answer,
          explanation: newPyq.explanation,
          source_id: newPyq.source_id,
          status: newPyq.status
        })
      });

      if (res.ok) {
        alert('Verified PYQ created successfully and added to topic repository!');
        setShowAddModal(false);
        setNewPyq({
          topic_id: '1',
          exam_id: '1',
          question: '',
          optionA: '',
          optionB: '',
          optionC: '',
          optionD: '',
          correct_answer: '',
          explanation: '',
          source_id: '3',
          status: 'published'
        });
        fetchAdminData();
      }
    } catch (err) {
      console.error('Error creating PYQ:', err);
    }
  };

  // Current Affairs Handlers
  const handleOpenCaModal = (ca = null) => {
    if (ca) {
      setEditingCa(ca);
      setCaForm({
        title: ca.title || '',
        category: ca.category || 'Science & Technology',
        date: ca.date || new Date().toISOString().split('T')[0],
        summary: ca.summary || '',
        important_facts: Array.isArray(ca.important_facts) ? ca.important_facts.join('\n') : (ca.important_facts || ''),
        source_name: ca.source_name || ca.source?.publisher || 'Press Information Bureau (PIB)',
        source_url: ca.source_url || ca.source?.url || 'https://pib.gov.in',
        status: ca.status || 'published'
      });
    } else {
      setEditingCa(null);
      setCaForm({
        title: '',
        category: 'Science & Technology',
        date: new Date().toISOString().split('T')[0],
        summary: '',
        important_facts: '',
        source_name: 'Press Information Bureau (PIB)',
        source_url: 'https://pib.gov.in',
        status: 'published'
      });
    }
    setShowCaModal(true);
  };

  const handleSaveCa = async (e) => {
    e.preventDefault();
    if (!caForm.title || !caForm.summary) {
      alert('Title and Summary are required.');
      return;
    }

    const factsArray = caForm.important_facts
      .split('\n')
      .map(f => f.trim())
      .filter(f => f.length > 0);

    const payload = {
      title: caForm.title,
      category: caForm.category,
      date: caForm.date,
      summary: caForm.summary,
      important_facts: factsArray,
      source_name: caForm.source_name,
      source_url: caForm.source_url,
      status: caForm.status
    };

    try {
      if (editingCa) {
        // Update
        const res = await fetch(`http://localhost:3001/api/admin/current-affairs/${editingCa.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (res.ok) {
          alert('Current Affair updated successfully!');
          setShowCaModal(false);
          fetchAdminData();
        }
      } else {
        // Create
        const res = await fetch('http://localhost:3001/api/admin/current-affairs', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (res.ok) {
          alert('Current Affair added successfully!');
          setShowCaModal(false);
          fetchAdminData();
        }
      }
    } catch (err) {
      console.error('Error saving current affair:', err);
      alert('Failed to save current affair.');
    }
  };

  const handleToggleCaStatus = async (id, currentStatus) => {
    const newStatus = currentStatus === 'published' ? 'draft' : 'published';
    try {
      const res = await fetch(`http://localhost:3001/api/admin/current-affairs/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus })
      });
      if (res.ok) {
        fetchAdminData();
      }
    } catch (err) {
      console.error('Error updating status:', err);
    }
  };

  const handleDeleteCa = async (id) => {
    if (!window.confirm(`Are you sure you want to delete Current Affair #${id}?`)) return;
    try {
      const res = await fetch(`http://localhost:3001/api/admin/current-affairs/${id}`, {
        method: 'DELETE'
      });
      if (res.ok) {
        alert('Deleted successfully.');
        fetchAdminData();
      }
    } catch (err) {
      console.error('Error deleting current affair:', err);
    }
  };

  const stats = adminData?.stats || {
    total_courses: 6,
    total_topics: 77,
    total_pyqs: 66,
    published_items: 72,
    verified_sources: 12
  };

  if (userRole !== 'admin') {
    return (
      <div style={{ padding: '80px 24px', textAlign: 'center', maxWidth: '600px', margin: '0 auto' }}>
        <div style={{
          width: '72px',
          height: '72px',
          borderRadius: '50%',
          background: 'rgba(244, 63, 94, 0.12)',
          color: 'var(--rose)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          margin: '0 auto 20px'
        }}>
          <ShieldCheck size={36} />
        </div>
        <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#fff', marginBottom: '12px' }}>
          Access Denied (403 Forbidden)
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '15px', lineHeight: 1.5, marginBottom: '24px' }}>
          Only users with administrator privileges can access the Admin Console and Notes Management system. Normal users cannot view or modify administrative data.
        </p>
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
          <button className="btn btn-primary" onClick={() => navigateTo('notes')}>
            Go to 📚 Published Notes
          </button>
          <button className="btn btn-secondary" onClick={() => navigateTo('home')}>
            Return to Home
          </button>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
          <span className="badge badge-primary">
            <ShieldCheck size={14} />
            Editorial Review & Verification Console
          </span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h1 style={{ fontSize: '32px', fontWeight: 800 }}>Admin Content Console</h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14.5px', marginTop: '4px' }}>
              Verify syllabus questions, approve question papers, publish/unpublish current affairs, and manage official sources.
            </p>
          </div>
          <div style={{ display: 'flex', gap: '10px' }}>
            {activeTab === 'mock-exams' && (
              <div style={{ display: 'flex', gap: '8px' }}>
                <button 
                  className="btn btn-secondary"
                  onClick={() => handleOpenAddQuestionModal()}
                  style={{ gap: '6px' }}
                >
                  <Plus size={16} />
                  <span>+ Add New Question</span>
                </button>
                <button 
                  className="btn btn-primary"
                  onClick={handleOpenCreateMockModal}
                  style={{ gap: '6px' }}
                >
                  <Target size={16} />
                  <span>+ Prepare Mock Exam (50+ Qs)</span>
                </button>
              </div>
            )}
            {activeTab === 'notes' && (
              <button 
                className="btn btn-primary"
                onClick={handleOpenAddNoteModal}
              >
                <Plus size={16} />
                <span>+ Add New Note</span>
              </button>
            )}
            {activeTab === 'govt-exams' && (
              <>
                <button 
                  className="btn btn-secondary"
                  onClick={handleCheckDeadlines}
                  title="Check application deadlines closing in 1-3 days"
                  style={{ fontSize: '13px', gap: '6px' }}
                >
                  <Bell size={15} color="var(--amber)" />
                  <span>Scan Deadlines</span>
                </button>
                <button 
                  className="btn btn-primary"
                  onClick={() => handleOpenGovtModal()}
                >
                  <Plus size={16} />
                  <span>Create Exam Update</span>
                </button>
              </>
            )}
            {activeTab === 'pyqs' && (
              <button 
                className="btn btn-primary"
                onClick={() => setShowAddModal(true)}
              >
                <Plus size={16} />
                <span>Add Verified PYQ</span>
              </button>
            )}
            {activeTab === 'current-affairs' && (
              <button 
                className="btn btn-emerald"
                onClick={() => handleOpenCaModal()}
              >
                <Plus size={16} />
                <span>Add Current Affair</span>
              </button>
            )}
          </div>
        </div>

        {/* Tab Switcher */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '20px', flexWrap: 'wrap' }}>
          <button
            className={`btn ${activeTab === 'mock-exams' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('mock-exams')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Target size={15} />
            <span>🎯 Mock Exams (50+ Qs)</span>
          </button>
          <button
            className={`btn ${activeTab === 'notes' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('notes')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <FileText size={15} />
            <span>📚 Notes Management</span>
          </button>
          <button
            className={`btn ${activeTab === 'govt-exams' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('govt-exams')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Building2 size={15} />
            <span>Government Exams Management</span>
          </button>
          <button
            className={`btn ${activeTab === 'pyqs' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('pyqs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <BookOpen size={15} />
            <span>Curriculum PYQs & Lessons</span>
          </button>
          <button
            className={`btn ${activeTab === 'current-affairs' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('current-affairs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Award size={15} />
            <span>Current Affairs Management</span>
          </button>
        </div>

        {/* Workflow Pipeline Explanation */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          padding: '14px 20px',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(99, 102, 241, 0.08)',
          border: '1px solid rgba(99, 102, 241, 0.25)',
          marginTop: '16px',
          fontSize: '13px',
          color: 'var(--text-secondary)',
          flexWrap: 'wrap'
        }}>
          <span style={{ fontWeight: 700, color: '#fff' }}>Editorial Pipeline:</span>
          <span>Draft</span>
          <span>→</span>
          <span>Add Official Source</span>
          <span>→</span>
          <span>Editorial Review</span>
          <span>→</span>
          <span className="badge badge-cyan">Verified</span>
          <span>→</span>
          <span className="badge badge-emerald">Published (Active in App)</span>
        </div>

        {/* Quick Stats */}
        <div className="stats-grid" style={{ marginTop: '20px' }}>
          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
              <BookOpen size={20} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.total_courses}</div>
              <div className="stat-label">Active Courses</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
              <Layers size={20} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.total_topics}</div>
              <div className="stat-label">Total Topics</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
              <FileText size={20} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{stats.total_pyqs}</div>
              <div className="stat-label">Verified PYQs</div>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
              <Award size={20} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{adminData?.current_affairs?.length || 4}</div>
              <div className="stat-label">Current Affairs</div>
            </div>
          </div>
        </div>
      </div>

      {/* ==========================================
          TAB: MOCK EXAMS MANAGEMENT (MINIMUM 50 QUESTIONS)
          ========================================== */}
      {activeTab === 'mock-exams' && (
        <div>
          {/* Mock Exams Stats Bar */}
          <div className="stats-grid" style={{ marginBottom: '24px' }}>
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <Target size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{mockExamsList.length}</div>
                <div className="stat-label">Total Mock Exams</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">
                  {mockExamsList.filter(e => e.status === 'published').length}
                </div>
                <div className="stat-label">Published Live</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
                <Edit2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">
                  {mockExamsList.filter(e => e.status === 'draft').length}
                </div>
                <div className="stat-label">Draft Mocks</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <HelpCircle size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">50 Qs</div>
                <div className="stat-label">Mandatory Minimum</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <Layers size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">830+</div>
                <div className="stat-label">Question Bank Pool</div>
              </div>
            </div>
          </div>

          {/* Policy Banner */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '12px',
            padding: '14px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(6, 182, 212, 0.08)',
            border: '1px solid rgba(6, 182, 212, 0.25)',
            marginBottom: '20px',
            fontSize: '13px',
            color: 'var(--text-secondary)',
            flexWrap: 'wrap'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span className="badge badge-cyan" style={{ fontSize: '11px', padding: '3px 8px' }}>
                Standard Policy
              </span>
              <span style={{ color: '#fff', fontWeight: 600 }}>
                Minimum 50 Questions Full-Length Mock Exams:
              </span>
              <span>All competitive mock exams are strictly enforced with at least 50 questions and negative marking.</span>
            </div>
            <div style={{ display: 'flex', gap: '8px' }}>
              <button
                className="btn btn-secondary"
                onClick={() => handleOpenAddQuestionModal()}
                style={{ fontSize: '12.5px', padding: '6px 14px', gap: '6px' }}
              >
                <Plus size={15} />
                <span>+ Add Question</span>
              </button>
              <button
                className="btn btn-primary"
                onClick={handleOpenCreateMockModal}
                style={{ fontSize: '12.5px', padding: '6px 14px', gap: '6px' }}
              >
                <Target size={15} />
                <span>+ Prepare 50-Q Mock</span>
              </button>
            </div>
          </div>

          {/* Sub-Tabs: Mock Exams List vs Question Bank Management */}
          <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
            <button
              className={`btn ${mockSubTab === 'exams' ? 'btn-primary' : 'btn-secondary'}`}
              onClick={() => setMockSubTab('exams')}
              style={{ fontSize: '13px', padding: '8px 18px', gap: '6px' }}
            >
              <Target size={16} />
              <span>Full-Length Mock Exams ({mockExamsList.length})</span>
            </button>
            <button
              className={`btn ${mockSubTab === 'questions' ? 'btn-primary' : 'btn-secondary'}`}
              onClick={() => {
                setMockSubTab('questions');
                fetchQuestionBank(qbSubjectFilter, qbSearchQuery);
              }}
              style={{ fontSize: '13px', padding: '8px 18px', gap: '6px' }}
            >
              <HelpCircle size={16} />
              <span>Question Bank & Custom Questions ({questionBank.length > 0 ? questionBank.length : '830+'})</span>
            </button>
          </div>

          {/* VIEW A: MOCK EXAMS LIST */}
          {mockSubTab === 'exams' && (
            <div>
              {/* Filters Bar */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                gap: '14px',
                marginBottom: '20px',
                flexWrap: 'wrap'
              }}>
                <div style={{ display: 'flex', gap: '12px', flex: '1', minWidth: '280px', flexWrap: 'wrap' }}>
                  {/* Search */}
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px',
                    padding: '8px 12px',
                    borderRadius: 'var(--radius-sm)',
                    background: 'var(--bg-card)',
                    border: '1px solid var(--border-subtle)',
                    flex: '1',
                    minWidth: '220px'
                  }}>
                    <Search size={15} color="var(--text-muted)" />
                    <input 
                      type="text"
                      placeholder="Search mock exams by title, exam, or category..."
                      value={mockSearchQuery}
                      onChange={e => setMockSearchQuery(e.target.value)}
                      style={{ border: 'none', outline: 'none', background: 'transparent', color: '#fff', fontSize: '13px', width: '100%' }}
                    />
                  </div>

                  {/* Category Filter */}
                  <select
                    value={mockCategoryFilter}
                    onChange={e => setMockCategoryFilter(e.target.value)}
                    style={{
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      color: '#fff',
                      fontSize: '13px',
                      outline: 'none'
                    }}
                  >
                    <option value="All">All Categories</option>
                    <option value="SSC">SSC (CGL, CHSL)</option>
                    <option value="UPSC">UPSC / Civil Services</option>
                    <option value="Railway">Railway / RRB NTPC</option>
                    <option value="Banking">Banking (IBPS, SBI)</option>
                    <option value="Defence">Defence / Police</option>
                    <option value="KPSC">KPSC / State Exams</option>
                    <option value="Central Government">Central Government</option>
                  </select>

                  {/* Status Filter */}
                  <select
                    value={mockStatusFilter}
                    onChange={e => setMockStatusFilter(e.target.value)}
                    style={{
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      color: '#fff',
                      fontSize: '13px',
                      outline: 'none'
                    }}
                  >
                    <option value="All">All Statuses</option>
                    <option value="published">Published (Live in App)</option>
                    <option value="draft">Drafts Only</option>
                  </select>
                </div>
              </div>

              {/* Mock Exams List */}
              {mockLoading ? (
                <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  Loading mock exams...
                </div>
              ) : mockExamsList.length === 0 ? (
                <div style={{
                  padding: '60px 24px',
                  textAlign: 'center',
                  borderRadius: 'var(--radius-lg)',
                  background: 'var(--bg-card)',
                  border: '1px dashed var(--border-subtle)',
                  margin: '20px 0'
                }}>
                  <div style={{
                    width: '60px',
                    height: '60px',
                    borderRadius: '50%',
                    background: 'rgba(6, 182, 212, 0.1)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    margin: '0 auto 16px',
                    color: 'var(--cyan)'
                  }}>
                    <Target size={28} />
                  </div>
                  <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>
                    No Mock Exams Found
                  </h3>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '440px', margin: '0 auto 20px', lineHeight: 1.5 }}>
                    Create your first full-length mock exam with at least 50 questions across key competitive subjects.
                  </p>
                  <button
                    className="btn btn-primary"
                    onClick={handleOpenCreateMockModal}
                  >
                    <Plus size={16} />
                    <span>Create 50-Question Mock Exam</span>
                  </button>
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                  {mockExamsList
                    .filter(exam => {
                      if (mockCategoryFilter !== 'All' && (exam.category || '').toLowerCase() !== mockCategoryFilter.toLowerCase()) return false;
                      if (mockStatusFilter !== 'All' && exam.status !== mockStatusFilter) return false;
                      if (mockSearchQuery.trim()) {
                        const q = mockSearchQuery.toLowerCase();
                        return (exam.title || '').toLowerCase().includes(q) || (exam.target_exam || '').toLowerCase().includes(q);
                      }
                      return true;
                    })
                    .map(exam => (
                      <div
                        key={exam.id}
                        className="card"
                        style={{
                          padding: '20px 24px',
                          borderRadius: 'var(--radius-md)',
                          background: 'var(--bg-card)',
                          border: '1px solid var(--border-subtle)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '14px'
                        }}
                      >
                        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '16px', flexWrap: 'wrap' }}>
                          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '14px' }}>
                            <div style={{
                              width: '44px',
                              height: '44px',
                              borderRadius: '10px',
                              background: 'rgba(99, 102, 241, 0.12)',
                              color: 'var(--cyan)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              flexShrink: 0
                            }}>
                              <Target size={24} />
                            </div>
                            <div>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: '6px' }}>
                                <h4 style={{ fontSize: '17px', fontWeight: 700, color: '#fff', margin: 0 }}>
                                  {exam.title}
                                </h4>
                                <span className={`badge ${exam.status === 'published' ? 'badge-emerald' : 'badge-amber'}`}>
                                  {exam.status === 'published' ? 'Published Live' : 'Draft'}
                                </span>
                              </div>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', fontSize: '12px' }}>
                                <span className="badge badge-primary" style={{ padding: '2px 8px' }}>
                                  {exam.category || 'General'}
                                </span>
                                {exam.target_exam && (
                                  <span className="badge badge-cyan" style={{ padding: '2px 8px' }}>
                                    {exam.target_exam}
                                  </span>
                                )}
                              </div>
                            </div>
                          </div>

                          {/* Action buttons */}
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <button
                              className="btn btn-secondary"
                              onClick={() => handlePreviewMockExam(exam)}
                              style={{ fontSize: '12.5px', padding: '6px 12px', gap: '5px' }}
                              title="Preview full 50 questions & answers"
                            >
                              <Eye size={14} />
                              <span>Preview ({exam.total_questions || (exam.question_ids || []).length} Qs)</span>
                            </button>
                            <button
                              className="btn btn-secondary"
                              onClick={() => handleOpenEditMockModal(exam)}
                              style={{ fontSize: '12.5px', padding: '6px 12px', gap: '5px' }}
                              title="Edit exam settings and questions"
                            >
                              <Edit2 size={14} />
                              <span>Edit Exam</span>
                            </button>
                            <button
                              className={`btn ${exam.status === 'published' ? 'btn-secondary' : 'btn-emerald'}`}
                              onClick={() => handleToggleMockStatus(exam.id, exam.status)}
                              style={{ fontSize: '12px', padding: '6px 12px' }}
                              title="Toggle live publication status"
                            >
                              {exam.status === 'published' ? 'Unpublish' : 'Publish Live'}
                            </button>
                            <button
                              className="btn btn-secondary"
                              onClick={() => handleDeleteMockExam(exam.id, exam.title)}
                              style={{ fontSize: '12px', padding: '6px 10px', color: 'var(--rose)' }}
                              title="Delete mock exam"
                            >
                              <Trash2 size={14} />
                            </button>
                          </div>
                        </div>

                        {exam.description && (
                          <p style={{ fontSize: '13.5px', color: 'var(--text-secondary)', margin: 0, lineHeight: 1.45 }}>
                            {exam.description}
                          </p>
                        )}

                        {/* Metadata strip */}
                        <div style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          paddingTop: '12px',
                          borderTop: '1px solid rgba(255, 255, 255, 0.04)',
                          fontSize: '12.5px',
                          color: 'var(--text-muted)',
                          flexWrap: 'wrap',
                          gap: '12px'
                        }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '16px', flexWrap: 'wrap' }}>
                            <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                              <HelpCircle size={14} color="var(--cyan)" />
                              <strong style={{ color: 'var(--cyan)' }}>{exam.total_questions || (exam.question_ids || []).length} Questions</strong> (Min 50 ✓)
                            </span>
                            <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                              <Clock size={14} />
                              <strong style={{ color: '#fff' }}>{exam.duration_minutes || 60} Mins</strong>
                            </span>
                            <span>
                              Total Marks: <strong style={{ color: '#fff' }}>{exam.total_marks || (exam.total_questions * 2) || 100}</strong>
                            </span>
                            <span>
                              Negative: <strong style={{ color: 'var(--amber)' }}>-{exam.negative_marking !== undefined ? exam.negative_marking : 0.25}</strong>
                            </span>
                            <span>
                              Pass Req: <strong style={{ color: 'var(--emerald)' }}>{exam.passing_percentage || 70}%</strong>
                            </span>
                          </div>

                          <div style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                            Attempts: <strong style={{ color: '#fff' }}>{exam.attempts_count || 0}</strong>
                            {exam.attempts_count > 0 && ` • Avg Score: ${exam.average_score}%`}
                          </div>
                        </div>
                      </div>
                    ))}
                </div>
              )}
            </div>
          )}

          {/* VIEW B: QUESTION BANK & CUSTOM QUESTIONS CONSOLE */}
          {mockSubTab === 'questions' && (
            <div>
              {/* Question Bank Filter & Action Bar */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                gap: '14px',
                marginBottom: '20px',
                flexWrap: 'wrap'
              }}>
                <div style={{ display: 'flex', gap: '12px', flex: 1, minWidth: '280px', flexWrap: 'wrap' }}>
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px',
                    padding: '8px 12px',
                    borderRadius: 'var(--radius-sm)',
                    background: 'var(--bg-card)',
                    border: '1px solid var(--border-subtle)',
                    flex: '1',
                    minWidth: '220px'
                  }}>
                    <Search size={15} color="var(--text-muted)" />
                    <input 
                      type="text"
                      placeholder="Search questions by text, subject, or topic..."
                      value={qbSearchQuery}
                      onChange={e => {
                        setQbSearchQuery(e.target.value);
                        fetchQuestionBank(qbSubjectFilter, e.target.value);
                      }}
                      style={{ border: 'none', outline: 'none', background: 'transparent', color: '#fff', fontSize: '13px', width: '100%' }}
                    />
                  </div>

                  <select
                    value={qbSubjectFilter}
                    onChange={e => {
                      setQbSubjectFilter(e.target.value);
                      fetchQuestionBank(e.target.value, qbSearchQuery);
                    }}
                    style={{
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      color: '#fff',
                      fontSize: '13px',
                      outline: 'none'
                    }}
                  >
                    <option value="All">All Subjects (830+ Qs)</option>
                    <option value="English">English Language</option>
                    <option value="Math">Quantitative Aptitude</option>
                    <option value="Reason">Reasoning Ability</option>
                    <option value="Awareness">General Awareness</option>
                    <option value="Science">General Science</option>
                  </select>
                </div>

                <button
                  className="btn btn-primary"
                  onClick={() => handleOpenAddQuestionModal(qbSubjectFilter !== 'All' ? qbSubjectFilter : 'Quantitative Aptitude')}
                  style={{ gap: '6px', fontSize: '13px' }}
                >
                  <Plus size={16} />
                  <span>+ Add New Question</span>
                </button>
              </div>

              {/* Questions List */}
              {questionBank.length === 0 ? (
                <div style={{ padding: '60px 20px', textAlign: 'center', color: 'var(--text-muted)', background: 'var(--bg-card)', borderRadius: 'var(--radius-md)', border: '1px dashed var(--border-subtle)' }}>
                  Loading question bank questions...
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                  {questionBank.map((q, idx) => (
                    <div
                      key={q.id || idx}
                      style={{
                        padding: '18px 22px',
                        borderRadius: 'var(--radius-md)',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)'
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{
                            width: '24px',
                            height: '24px',
                            borderRadius: '50%',
                            background: 'rgba(6, 182, 212, 0.12)',
                            color: 'var(--cyan)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            fontSize: '11.5px',
                            fontWeight: 700
                          }}>
                            {idx + 1}
                          </span>
                          <span className="badge badge-primary" style={{ fontSize: '11px' }}>
                            {q.subject || 'General'}
                          </span>
                          {q.topic && (
                            <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                              {q.topic}
                            </span>
                          )}
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                            ID #{q.id} • {q.points || 2} Marks
                          </span>
                        </div>

                        <button
                          className="btn btn-secondary"
                          onClick={() => handleDeleteQuestion(q.id, q.question)}
                          style={{ fontSize: '11.5px', padding: '4px 10px', color: 'var(--rose)' }}
                          title="Delete question from database"
                        >
                          <Trash2 size={13} />
                          <span>Delete</span>
                        </button>
                      </div>

                      <h4 style={{ fontSize: '14.5px', fontWeight: 600, color: '#fff', margin: '0 0 12px', lineHeight: 1.5 }}>
                        {q.question}
                      </h4>

                      {/* Options */}
                      {Array.isArray(q.options_json) && q.options_json.length > 0 ? (
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '8px', marginBottom: '10px' }}>
                          {q.options_json.map((opt, oIdx) => {
                            const isCorrect = opt === q.correct_answer || (q.correct_answer && String(opt).startsWith(q.correct_answer));
                            return (
                              <div
                                key={oIdx}
                                style={{
                                  padding: '7px 12px',
                                  borderRadius: '6px',
                                  background: isCorrect ? 'rgba(16, 185, 129, 0.1)' : 'rgba(255, 255, 255, 0.02)',
                                  border: `1px solid ${isCorrect ? 'rgba(16, 185, 129, 0.35)' : 'rgba(255, 255, 255, 0.05)'}`,
                                  color: isCorrect ? 'var(--emerald)' : 'var(--text-secondary)',
                                  fontSize: '12.5px',
                                  display: 'flex',
                                  alignItems: 'center',
                                  gap: '8px'
                                }}
                              >
                                <span style={{ fontWeight: 700, width: '16px' }}>{String.fromCharCode(65 + oIdx)}.</span>
                                <span>{opt}</span>
                                {isCorrect && <Check size={14} style={{ marginLeft: 'auto' }} />}
                              </div>
                            );
                          })}
                        </div>
                      ) : (
                        <div style={{ fontSize: '12.5px', color: 'var(--text-muted)', marginBottom: '10px' }}>
                          Direct Answer / Fill-in-the-blank: <strong style={{ color: 'var(--emerald)' }}>{q.correct_answer}</strong>
                        </div>
                      )}

                      {q.explanation && (
                        <div style={{
                          padding: '8px 12px',
                          borderRadius: '6px',
                          background: 'rgba(6, 182, 212, 0.06)',
                          border: '1px solid rgba(6, 182, 212, 0.15)',
                          fontSize: '12px',
                          color: 'var(--text-secondary)'
                        }}>
                          <strong style={{ color: 'var(--cyan)' }}>Explanation: </strong>
                          {q.explanation}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* ==========================================
          TAB: NOTES MANAGEMENT CONSOLE
          ========================================== */}
      {activeTab === 'notes' && (
        <div>
          {/* Notes Stats Bar */}
          <div className="stats-grid" style={{ marginBottom: '24px' }}>
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <FileText size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.total || 0}</div>
                <div className="stat-label">Total PDF Notes</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
                <Edit2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.draft || 0}</div>
                <div className="stat-label">Drafts (Step 1)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <Layers size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.pending_review || 0}</div>
                <div className="stat-label">Pending Review (Step 2)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <ShieldCheck size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.verified || 0}</div>
                <div className="stat-label">Verified (Step 3)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.published || 0}</div>
                <div className="stat-label">Published (Live in App)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--text-muted)' }}>
                <EyeOff size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{noteCounts.archived || 0}</div>
                <div className="stat-label">Archived</div>
              </div>
            </div>
          </div>

          {/* Workflow Pipeline Banner */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '14px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(99, 102, 241, 0.08)',
            border: '1px solid rgba(99, 102, 241, 0.25)',
            marginBottom: '20px',
            fontSize: '13px',
            color: 'var(--text-secondary)',
            flexWrap: 'wrap'
          }}>
            <span style={{ fontWeight: 700, color: '#fff' }}>Publication Workflow:</span>
            <span className="badge badge-subtle">1. DRAFT</span>
            <span>→</span>
            <span className="badge badge-amber">2. PENDING REVIEW</span>
            <span>→</span>
            <span className="badge badge-cyan">3. VERIFIED</span>
            <span>→</span>
            <span className="badge badge-emerald">4. PUBLISHED (Visible in 📚 Notes)</span>
            <span>→</span>
            <span className="badge" style={{ background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-muted)' }}>5. ARCHIVED</span>
          </div>

          {/* Filters & Actions Bar */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '16px',
            marginBottom: '20px',
            flexWrap: 'wrap'
          }}>
            <div style={{ display: 'flex', gap: '12px', flex: '1', minWidth: '300px', flexWrap: 'wrap' }}>
              {/* Search */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '8px 12px',
                borderRadius: 'var(--radius-sm)',
                background: 'var(--bg-card)',
                border: '1px solid var(--border-subtle)',
                flex: '1',
                minWidth: '220px'
              }}>
                <Search size={15} color="var(--text-muted)" />
                <input 
                  type="text"
                  placeholder="Search notes by title, subject, topic, or file..."
                  value={noteSearchQuery}
                  onChange={e => setNoteSearchQuery(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && fetchAdminNotes()}
                  style={{ border: 'none', outline: 'none', background: 'transparent', color: '#fff', fontSize: '13px', width: '100%' }}
                />
              </div>

              {/* Status Filter */}
              <select
                value={noteStatusFilter}
                onChange={e => setNoteStatusFilter(e.target.value)}
                style={{
                  padding: '8px 12px',
                  borderRadius: 'var(--radius-sm)',
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-subtle)',
                  color: '#fff',
                  fontSize: '13px',
                  outline: 'none'
                }}
              >
                <option value="All">All Statuses ({noteCounts.total || 0})</option>
                <option value="DRAFT">Drafts ({noteCounts.draft || 0})</option>
                <option value="PENDING_REVIEW">Pending Review ({noteCounts.pending_review || 0})</option>
                <option value="VERIFIED">Verified ({noteCounts.verified || 0})</option>
                <option value="PUBLISHED">Published Live ({noteCounts.published || 0})</option>
                <option value="ARCHIVED">Archived ({noteCounts.archived || 0})</option>
              </select>

              {/* Subject Filter */}
              <select
                value={noteSubjectFilter}
                onChange={e => setNoteSubjectFilter(e.target.value)}
                style={{
                  padding: '8px 12px',
                  borderRadius: 'var(--radius-sm)',
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-subtle)',
                  color: '#fff',
                  fontSize: '13px',
                  outline: 'none'
                }}
              >
                <option value="All">All Subjects</option>
                <option value="English">English</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Reasoning">Reasoning</option>
                <option value="General Awareness">General Awareness</option>
                <option value="General Science">General Science</option>
                <option value="Computer Knowledge">Computer Knowledge</option>
              </select>
            </div>

            <button
              className="btn btn-primary"
              onClick={handleOpenAddNoteModal}
              style={{ fontSize: '13.5px', padding: '8px 16px', gap: '6px' }}
            >
              <Plus size={16} />
              <span>+ Add New Note</span>
            </button>
          </div>

          {/* Notes List */}
          {loading ? (
            <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
              Loading study notes...
            </div>
          ) : notesList.length === 0 ? (
            <div style={{
              padding: '60px 24px',
              textAlign: 'center',
              borderRadius: 'var(--radius-lg)',
              background: 'var(--bg-card)',
              border: '1px dashed var(--border-subtle)',
              margin: '20px 0'
            }}>
              <div style={{
                width: '60px',
                height: '60px',
                borderRadius: '50%',
                background: 'rgba(99, 102, 241, 0.1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 16px',
                color: 'var(--cyan)'
              }}>
                <FileText size={28} />
              </div>
              <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>
                No Study Notes Found
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '440px', margin: '0 auto 20px', lineHeight: 1.5 }}>
                {noteSearchQuery || noteStatusFilter !== 'All' || noteSubjectFilter !== 'All'
                  ? 'No uploaded notes match your current filters. Clear filters to see all notes.'
                  : 'Start by uploading your real PDF notes (e.g., English_Notes.pdf, Mathematics_Notes.pdf, Reasoning_Notes.pdf).'}
              </p>
              <button
                className="btn btn-primary"
                onClick={handleOpenAddNoteModal}
              >
                <Plus size={16} />
                <span>Upload First PDF Note</span>
              </button>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {notesList.map(note => {
                const getStatusBadge = (st) => {
                  switch (st) {
                    case 'DRAFT':
                      return <span className="badge badge-subtle">Draft</span>;
                    case 'PENDING_REVIEW':
                      return <span className="badge badge-amber">Pending Review</span>;
                    case 'VERIFIED':
                      return <span className="badge badge-cyan">Verified</span>;
                    case 'PUBLISHED':
                      return <span className="badge badge-emerald">Published (Live)</span>;
                    case 'ARCHIVED':
                      return <span className="badge" style={{ background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-muted)' }}>Archived</span>;
                    default:
                      return <span className="badge">{st}</span>;
                  }
                };

                return (
                  <div
                    key={note.id}
                    className="card"
                    style={{
                      padding: '18px 22px',
                      borderRadius: 'var(--radius-md)',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '12px'
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '16px', flexWrap: 'wrap' }}>
                      <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
                        <div style={{
                          width: '40px',
                          height: '40px',
                          borderRadius: '8px',
                          background: 'rgba(244, 63, 94, 0.12)',
                          color: 'var(--rose)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          flexShrink: 0
                        }}>
                          <FileText size={22} />
                        </div>
                        <div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: '4px' }}>
                            <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#fff', margin: 0 }}>
                              {note.title}
                            </h4>
                            {getStatusBadge(note.status)}
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', fontSize: '12.5px' }}>
                            <span className="badge badge-primary" style={{ padding: '2px 7px', fontSize: '11px' }}>
                              {note.subject_name}
                            </span>
                            <span className="badge badge-cyan" style={{ padding: '2px 7px', fontSize: '11px' }}>
                              {note.topic_name}
                            </span>
                            {note.subtopic_name && (
                              <span style={{ color: 'var(--text-muted)' }}>
                                Subtopic: <strong style={{ color: 'var(--text-secondary)' }}>{note.subtopic_name}</strong>
                              </span>
                            )}
                          </div>
                        </div>
                      </div>

                      {/* Top Action Buttons */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <button
                          className="btn btn-secondary"
                          onClick={() => setPreviewingNote(note)}
                          style={{ fontSize: '12px', padding: '6px 12px', gap: '5px' }}
                          title="Preview actual PDF"
                        >
                          <Eye size={14} />
                          <span>Preview</span>
                        </button>
                        <button
                          className="btn btn-secondary"
                          onClick={() => handleOpenEditNoteModal(note)}
                          style={{ fontSize: '12px', padding: '6px 12px', gap: '5px' }}
                          title="Edit note details or replace PDF"
                        >
                          <Edit2 size={14} />
                          <span>Edit</span>
                        </button>
                        <button
                          className="btn btn-secondary"
                          onClick={() => handleDeleteNote(note.id, note.title)}
                          style={{ fontSize: '12px', padding: '6px 10px', color: 'var(--rose)' }}
                          title="Delete note and PDF file"
                        >
                          <Trash2 size={14} />
                        </button>
                      </div>
                    </div>

                    {/* Description if present */}
                    {note.description && (
                      <p style={{ fontSize: '13px', color: 'var(--text-secondary)', margin: 0, lineHeight: 1.45 }}>
                        {note.description}
                      </p>
                    )}

                    {/* Metadata & Workflow Strip */}
                    <div style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      paddingTop: '10px',
                      borderTop: '1px solid rgba(255, 255, 255, 0.04)',
                      fontSize: '12px',
                      color: 'var(--text-muted)',
                      flexWrap: 'wrap',
                      gap: '12px'
                    }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap' }}>
                        <span>
                          File: <strong style={{ color: '#fff' }}>{note.file_name}</strong> ({note.file_size || 'PDF'})
                        </span>
                        {note.source && (
                          <span>
                            Source: <strong style={{ color: 'var(--text-secondary)' }}>{note.source}</strong>
                          </span>
                        )}
                        <span>
                          Uploaded: {new Date(note.created_at).toLocaleDateString()}
                        </span>
                      </div>

                      {/* Workflow Step Transition Buttons */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        {note.status === 'DRAFT' && (
                          <button
                            className="btn btn-secondary"
                            onClick={() => handleUpdateNoteStatus(note.id, 'PENDING_REVIEW')}
                            style={{ fontSize: '11.5px', padding: '4px 10px', color: 'var(--amber)', borderColor: 'rgba(245, 158, 11, 0.4)' }}
                          >
                            Submit for Review →
                          </button>
                        )}
                        {note.status === 'PENDING_REVIEW' && (
                          <button
                            className="btn btn-secondary"
                            onClick={() => handleUpdateNoteStatus(note.id, 'VERIFIED')}
                            style={{ fontSize: '11.5px', padding: '4px 10px', color: 'var(--cyan)', borderColor: 'rgba(6, 182, 212, 0.4)' }}
                          >
                            ✓ Verify Note
                          </button>
                        )}
                        {note.status === 'VERIFIED' && (
                          <button
                            className="btn btn-emerald"
                            onClick={() => handleUpdateNoteStatus(note.id, 'PUBLISHED')}
                            style={{ fontSize: '11.5px', padding: '4px 10px' }}
                          >
                            🚀 Publish Live to App
                          </button>
                        )}
                        {note.status === 'PUBLISHED' && (
                          <button
                            className="btn btn-secondary"
                            onClick={() => handleUpdateNoteStatus(note.id, 'ARCHIVED')}
                            style={{ fontSize: '11.5px', padding: '4px 10px' }}
                          >
                            Archive Note
                          </button>
                        )}
                        {note.status === 'ARCHIVED' && (
                          <button
                            className="btn btn-secondary"
                            onClick={() => handleUpdateNoteStatus(note.id, 'DRAFT')}
                            style={{ fontSize: '11.5px', padding: '4px 10px' }}
                          >
                            Restore to Draft
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* ==========================================
          TAB: GOVERNMENT EXAMS UPDATES CONSOLE
          ========================================== */}
      {activeTab === 'govt-exams' && (
        <div>
          {/* Stats Bar */}
          <div className="stats-grid" style={{ marginBottom: '24px' }}>
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <Building2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.total || 0}</div>
                <div className="stat-label">Total Exam Updates</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
                <Edit2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.draft || 0}</div>
                <div className="stat-label">Drafts (Step 1)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <FileText size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.pending_review || 0}</div>
                <div className="stat-label">Pending Review (Step 2)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <ShieldCheck size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.verified || 0}</div>
                <div className="stat-label">Verified (Step 3)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.published || 0}</div>
                <div className="stat-label">Published (Step 4 Live)</div>
              </div>
            </div>
          </div>

          {/* Workflow Banner */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '14px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(6, 182, 212, 0.08)',
            border: '1px solid rgba(6, 182, 212, 0.25)',
            marginBottom: '20px',
            fontSize: '13px',
            color: 'var(--text-secondary)',
            flexWrap: 'wrap'
          }}>
            <span style={{ fontWeight: 700, color: '#fff' }}>Mandatory Verification Workflow:</span>
            <span className="badge badge-subtle">1. DRAFT</span>
            <span>→</span>
            <span className="badge badge-amber">2. PENDING REVIEW</span>
            <span>→</span>
            <span className="badge badge-cyan">3. VERIFIED</span>
            <span>→</span>
            <span className="badge badge-emerald">4. PUBLISHED (Visible to Students)</span>
            <span style={{ marginLeft: 'auto', fontSize: '12px', color: 'var(--text-muted)' }}>
              Normal users only see VERIFIED + PUBLISHED updates.
            </span>
          </div>

          {/* Filters Toolbar */}
          <div className="glass-card" style={{ padding: '18px 24px', marginBottom: '20px' }}>
            <div style={{ display: 'flex', gap: '16px', alignItems: 'center', flexWrap: 'wrap', justifyContent: 'space-between' }}>
              
              {/* Search */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255,255,255,0.04)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', minWidth: '260px' }}>
                <Search size={15} color="var(--text-muted)" />
                <input 
                  type="text" 
                  placeholder="Search exam, org, title..."
                  value={govtSearchQuery}
                  onChange={e => setGovtSearchQuery(e.target.value)}
                  style={{ background: 'transparent', border: 'none', color: '#fff', fontSize: '13px', outline: 'none', width: '100%' }}
                />
              </div>

              {/* Status Filter */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>Status:</span>
                <select
                  value={govtStatusFilter}
                  onChange={e => setGovtStatusFilter(e.target.value)}
                  className="admin-select"
                  style={{ fontSize: '12.5px', padding: '6px 10px' }}
                >
                  <option value="All">All Statuses</option>
                  <option value="DRAFT">DRAFT</option>
                  <option value="PENDING_REVIEW">PENDING_REVIEW</option>
                  <option value="VERIFIED">VERIFIED</option>
                  <option value="PUBLISHED">PUBLISHED</option>
                  <option value="REJECTED">REJECTED</option>
                  <option value="ARCHIVED">ARCHIVED</option>
                </select>
              </div>

              {/* Category Filter */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>Category:</span>
                <select
                  value={govtCategoryFilter}
                  onChange={e => setGovtCategoryFilter(e.target.value)}
                  className="admin-select"
                  style={{ fontSize: '12.5px', padding: '6px 10px' }}
                >
                  <option value="All">All Categories</option>
                  {examCategories.map(c => (
                    <option key={c.id} value={c.name}>{c.name}</option>
                  ))}
                </select>
              </div>

              {/* Add category shortcut */}
              <button 
                className="btn btn-subtle"
                onClick={() => setShowAddCatInline(!showAddCatInline)}
                style={{ fontSize: '12px', padding: '6px 10px' }}
              >
                + New Category
              </button>
            </div>

            {/* Inline Add Category Form */}
            {showAddCatInline && (
              <form onSubmit={handleAddCategory} style={{ display: 'flex', gap: '10px', alignItems: 'center', marginTop: '14px', paddingTop: '14px', borderTop: '1px solid var(--border-subtle)' }}>
                <input 
                  type="text" 
                  placeholder="Category Name (e.g. Metro Rail, Police Sub-Inspector)"
                  value={newCatName}
                  onChange={e => setNewCatName(e.target.value)}
                  style={{ padding: '6px 12px', background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '13px', flex: 1 }}
                  required
                />
                <select 
                  value={newCatGroup}
                  onChange={e => setNewCatGroup(e.target.value)}
                  style={{ padding: '6px 12px', background: 'var(--bg-dark)', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '13px' }}
                >
                  <option value="Central Government">Central Government</option>
                  <option value="State Government">State Government</option>
                </select>
                <button type="submit" className="btn btn-primary" style={{ fontSize: '12.5px', padding: '6px 14px' }}>
                  Add Category
                </button>
              </form>
            )}
          </div>

          {/* Updates Table */}
          <div className="glass-card" style={{ padding: '24px' }}>
            {govtExams.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '48px 20px', color: 'var(--text-muted)' }}>
                <Building2 size={36} color="var(--text-muted)" style={{ margin: '0 auto 12px' }} />
                <h4 style={{ fontSize: '16px', fontWeight: 600, color: '#f8fafc', marginBottom: '6px' }}>
                  No Government Exam Updates Found
                </h4>
                <p style={{ fontSize: '13.5px', maxWidth: '440px', margin: '0 auto 16px' }}>
                  Create a new update following the official gazette to start the Source → Review → Verification → Publish workflow.
                </p>
                <button className="btn btn-primary" onClick={() => handleOpenGovtModal()}>
                  <Plus size={15} />
                  <span>Create First Exam Update</span>
                </button>
              </div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table className="admin-table">
                  <thead>
                    <tr>
                      <th>Exam & Org</th>
                      <th>Category & Type</th>
                      <th>Key Dates</th>
                      <th>Official Source</th>
                      <th>Status</th>
                      <th>Workflow Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {govtExams.map(exam => {
                      const status = exam.verification_status;
                      return (
                        <tr key={exam.id}>
                          <td>
                            <div style={{ fontWeight: 700, color: '#f8fafc', fontSize: '14px' }}>
                              {exam.exam_name}
                            </div>
                            <div style={{ fontSize: '12px', color: 'var(--cyan)' }}>
                              {exam.organization}
                            </div>
                            {exam.official_notification_number && (
                              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                                Ref: {exam.official_notification_number}
                              </div>
                            )}
                          </td>
                          <td>
                            <span className="badge badge-primary" style={{ fontSize: '11px', marginBottom: '4px', display: 'inline-block' }}>
                              {exam.category}
                            </span>
                            <div style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                              {exam.update_type}
                            </div>
                          </td>
                          <td style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                            {exam.application_last_date && (
                              <div>Last Date: <strong style={{ color: '#fff' }}>{exam.application_last_date}</strong></div>
                            )}
                            {exam.exam_date && (
                              <div>Exam: <strong style={{ color: 'var(--cyan)' }}>{exam.exam_date}</strong></div>
                            )}
                            {exam.result_date && (
                              <div>Result: <strong style={{ color: 'var(--emerald)' }}>{exam.result_date}</strong></div>
                            )}
                          </td>
                          <td>
                            <div style={{ fontSize: '12px', color: '#f8fafc' }}>
                              {exam.official_source_name}
                            </div>
                            <a 
                              href={exam.official_source_url} 
                              target="_blank" 
                              rel="noopener noreferrer" 
                              style={{ fontSize: '11.5px', color: 'var(--cyan)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
                            >
                              <span>Official Link</span>
                              <ExternalLink size={11} />
                            </a>
                          </td>
                          <td>
                            <span className={`badge ${
                              status === 'PUBLISHED' ? 'badge-emerald' :
                              status === 'VERIFIED' ? 'badge-cyan' :
                              status === 'PENDING_REVIEW' ? 'badge-amber' :
                              status === 'REJECTED' ? 'badge-rose' : 'badge-subtle'
                            }`}>
                              {status}
                            </span>
                            {status === 'PUBLISHED' && (
                              <div style={{ fontSize: '11px', color: 'var(--emerald)', marginTop: '2px' }}>
                                Live in student app ✓
                              </div>
                            )}
                          </td>
                          <td>
                            <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', alignItems: 'center' }}>
                              {/* Workflow Step Transitions */}
                              {status === 'DRAFT' && (
                                <button 
                                  className="btn btn-secondary" 
                                  onClick={() => handleTransitionStatus(exam.id, 'PENDING_REVIEW')}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Submit to editorial review"
                                >
                                  Submit for Review →
                                </button>
                              )}

                              {status === 'PENDING_REVIEW' && (
                                <button 
                                  className="btn btn-primary" 
                                  onClick={() => handleTransitionStatus(exam.id, 'VERIFIED')}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Confirm verification against official gazette"
                                >
                                  Verify Data ✓
                                </button>
                              )}

                              {status === 'VERIFIED' && (
                                <button 
                                  className="btn btn-emerald" 
                                  onClick={() => setShowPublishConfirm(exam)}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Publish to students with optional push notification"
                                >
                                  Publish 🚀
                                </button>
                              )}

                              {status === 'PUBLISHED' && (
                                <button 
                                  className="btn btn-subtle" 
                                  onClick={() => handleTransitionStatus(exam.id, 'DRAFT')}
                                  style={{ fontSize: '11px', padding: '4px 8px' }}
                                  title="Unpublish back to draft"
                                >
                                  Unpublish
                                </button>
                              )}

                              {/* Edit & Delete */}
                              <button 
                                className="btn-icon" 
                                onClick={() => handleOpenGovtModal(exam)}
                                title="Edit update details"
                                style={{ width: '28px', height: '28px' }}
                              >
                                <Edit2 size={13} />
                              </button>
                              <button 
                                className="btn-icon" 
                                onClick={() => handleDeleteGovtExam(exam.id, exam.exam_name)}
                                title="Delete update"
                                style={{ width: '28px', height: '28px', color: 'var(--rose)' }}
                              >
                                <Trash2 size={13} />
                              </button>
                            </div>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      )}

      {/* ==========================================
          TAB 1: CURRICULUM PYQS & LESSONS
          ========================================== */}
      {activeTab === 'pyqs' && (
        <div className="glass-card" style={{ padding: '24px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Curriculum & Verified Questions</h3>
            <div style={{ display: 'flex', gap: '8px' }}>
              {['', 'published', 'verified', 'under_review', 'draft'].map(st => (
                <button
                  key={st}
                  className={`btn ${statusFilter === st ? 'btn-primary' : 'btn-secondary'}`}
                  onClick={() => setStatusFilter(st)}
                  style={{ fontSize: '12px', padding: '5px 12px' }}
                >
                  {st ? st.replace('_', ' ').toUpperCase() : 'ALL'}
                </button>
              ))}
            </div>
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
              Loading content...
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table className="admin-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Title / Question Snippet</th>
                    <th>Status</th>
                    <th>Source Reference</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  {adminData?.pyqs?.map(p => (
                    <tr key={`pyq-${p.id}`}>
                      <td style={{ color: 'var(--text-muted)', fontSize: '12px' }}>PYQ #{p.id}</td>
                      <td><span className="badge badge-cyan">PYQ</span></td>
                      <td style={{ maxWidth: '340px', color: '#f8fafc', fontWeight: 500 }}>
                        {p.question?.slice(0, 75)}...
                      </td>
                      <td>
                        <span className="badge badge-emerald">{p.status}</span>
                      </td>
                      <td style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                        Source ID #{p.source_id} (Official Key)
                      </td>
                      <td>
                        {p.status !== 'published' ? (
                          <button 
                            className="btn btn-emerald"
                            onClick={() => handleVerifyAndPublish('pyq', p.id)}
                            style={{ fontSize: '11px', padding: '4px 10px' }}
                          >
                            Approve & Publish
                          </button>
                        ) : (
                          <span style={{ fontSize: '12px', color: 'var(--emerald)' }}>Active in App ✓</span>
                        )}
                      </td>
                    </tr>
                  ))}

                  {adminData?.lessons?.map(l => (
                    <tr key={`les-${l.id}`}>
                      <td style={{ color: 'var(--text-muted)', fontSize: '12px' }}>LES #{l.id}</td>
                      <td><span className="badge badge-primary">Lesson</span></td>
                      <td style={{ maxWidth: '340px', color: '#f8fafc', fontWeight: 500 }}>
                        {l.title}
                      </td>
                      <td>
                        <span className="badge badge-emerald">{l.status}</span>
                      </td>
                      <td style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                        British Council / Cambridge
                      </td>
                      <td>
                        <span style={{ fontSize: '12px', color: 'var(--emerald)' }}>Active in App ✓</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {/* ==========================================
          TAB 2: CURRENT AFFAIRS MANAGEMENT
          ========================================== */}
      {activeTab === 'current-affairs' && (
        <div className="glass-card" style={{ padding: '24px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Current Affairs Management</h3>
              <p style={{ fontSize: '13px', color: 'var(--text-secondary)', marginTop: '2px' }}>
                Only published items appear in the student app. Unpublished items remain drafts visible only to administrators.
              </p>
            </div>
            <button 
              className="btn btn-emerald"
              onClick={() => handleOpenCaModal()}
              style={{ fontSize: '13px', padding: '8px 16px' }}
            >
              <Plus size={15} />
              <span>Add New Current Affair</span>
            </button>
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
              Loading Current Affairs...
            </div>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table className="admin-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Category</th>
                    <th>Title & Summary</th>
                    <th>Date</th>
                    <th>Source</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {adminData?.current_affairs?.map(ca => {
                    const isPub = ca.status === 'published';
                    return (
                      <tr key={`ca-${ca.id}`}>
                        <td style={{ color: 'var(--text-muted)', fontSize: '12px' }}>#{ca.id}</td>
                        <td>
                          <span className="badge badge-cyan" style={{ fontSize: '11px' }}>
                            {ca.category}
                          </span>
                        </td>
                        <td style={{ maxWidth: '320px' }}>
                          <div style={{ fontWeight: 600, color: '#f8fafc', fontSize: '13.5px', marginBottom: '4px' }}>
                            {ca.title}
                          </div>
                          <div style={{ color: 'var(--text-secondary)', fontSize: '12px', lineHeight: 1.4 }}>
                            {ca.summary?.slice(0, 90)}...
                          </div>
                        </td>
                        <td style={{ fontSize: '12px', color: 'var(--text-muted)', whiteSpace: 'nowrap' }}>
                          {ca.date}
                        </td>
                        <td style={{ fontSize: '12px', color: 'var(--text-secondary)', maxWidth: '140px' }}>
                          <div>{ca.source_name || ca.source?.publisher || 'Official'}</div>
                          {ca.source_url && (
                            <a 
                              href={ca.source_url} 
                              target="_blank" 
                              rel="noreferrer" 
                              style={{ color: 'var(--cyan)', fontSize: '11px', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '3px' }}
                            >
                              <span>Link</span>
                              <ExternalLink size={10} />
                            </a>
                          )}
                        </td>
                        <td>
                          <span className={`badge ${isPub ? 'badge-emerald' : 'badge-amber'}`} style={{ fontSize: '11.5px' }}>
                            {isPub ? 'Published' : 'Draft / Unpublished'}
                          </span>
                        </td>
                        <td>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                            {/* Toggle Publish / Unpublish */}
                            <button
                              className={`btn ${isPub ? 'btn-secondary' : 'btn-emerald'}`}
                              onClick={() => handleToggleCaStatus(ca.id, ca.status)}
                              title={isPub ? 'Unpublish to draft' : 'Publish to app'}
                              style={{ fontSize: '11px', padding: '4px 8px' }}
                            >
                              {isPub ? <EyeOff size={13} /> : <Eye size={13} />}
                              <span>{isPub ? 'Unpublish' : 'Publish'}</span>
                            </button>

                            {/* Edit */}
                            <button
                              className="btn btn-secondary"
                              onClick={() => handleOpenCaModal(ca)}
                              title="Edit Current Affair"
                              style={{ fontSize: '11px', padding: '4px 8px' }}
                            >
                              <Edit2 size={13} />
                              <span>Edit</span>
                            </button>

                            {/* Delete */}
                            <button
                              className="btn btn-rose"
                              onClick={() => handleDeleteCa(ca.id)}
                              title="Delete Current Affair"
                              style={{ fontSize: '11px', padding: '4px 8px' }}
                            >
                              <Trash2 size={13} />
                            </button>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

{/* ==========================================
          MODAL: CREATE / EDIT GOVERNMENT EXAM UPDATE
          ========================================== */}
      {showGovtModal && (
        <div className="modal-backdrop" onClick={() => setShowGovtModal(false)}>
          <div 
            className="modal-content" 
            onClick={e => e.stopPropagation()} 
            style={{ maxWidth: '820px', maxHeight: '90vh', overflowY: 'auto' }}
          >
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Building2 size={20} color="var(--cyan)" />
                <h3 style={{ fontSize: '18px', fontWeight: 700 }}>
                  {editingGovt ? `Edit Exam Update: ${editingGovt.exam_name}` : 'Create Government Exam Update'}
                </h3>
              </div>
              <button className="btn-icon" onClick={() => setShowGovtModal(false)}>
                <X size={16} />
              </button>
            </div>

            {/* Duplicate Warning Alert */}
            {govtDuplicateWarning && (
              <div style={{
                margin: '16px 24px 0',
                padding: '12px 16px',
                borderRadius: 'var(--radius-sm)',
                background: 'rgba(245, 158, 11, 0.15)',
                border: '1px solid var(--amber)',
                color: '#fef3c7',
                fontSize: '13px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                gap: '12px'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <AlertTriangle size={18} color="var(--amber)" />
                  <span>{govtDuplicateWarning}</span>
                </div>
                <button 
                  type="button" 
                  className="btn btn-secondary" 
                  onClick={(e) => handleSaveGovtExam(e, true)}
                  style={{ fontSize: '11.5px', padding: '4px 10px', background: 'rgba(0,0,0,0.3)' }}
                >
                  Force Save Anyway
                </button>
              </div>
            )}

            <form onSubmit={handleSaveGovtExam} style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              
              {/* Section 1: Basic Classification */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  1. Examination Classification
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Exam Name *</label>
                    <input 
                      type="text" 
                      value={govtForm.exam_name}
                      onChange={e => setGovtForm({ ...govtForm, exam_name: e.target.value })}
                      placeholder="e.g., SSC CGL 2026, UPSC CDS II 2026"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Organization *</label>
                    <input 
                      type="text" 
                      value={govtForm.organization}
                      onChange={e => setGovtForm({ ...govtForm, organization: e.target.value })}
                      placeholder="e.g., Staff Selection Commission (SSC)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Category *</label>
                    <select
                      value={govtForm.category}
                      onChange={e => setGovtForm({ ...govtForm, category: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    >
                      {examCategories.map(c => (
                        <option key={c.id} value={c.name}>{c.name} ({c.group})</option>
                      ))}
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Update Type *</label>
                    <select
                      value={govtForm.update_type}
                      onChange={e => setGovtForm({ ...govtForm, update_type: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    >
                      <option value="EXAM_NOTIFICATION">🔔 Exam Notification</option>
                      <option value="APPLICATION_OPEN">📝 Application Open</option>
                      <option value="APPLICATION_CLOSING">⏳ Application Closing</option>
                      <option value="ADMIT_CARD">🎟️ Admit Card Released</option>
                      <option value="EXAM_DATE">📅 Exam Date Announced</option>
                      <option value="ANSWER_KEY">🔑 Answer Key Released</option>
                      <option value="RESULT">🏆 Result Released</option>
                      <option value="CUTOFF">📊 Cut-off / Merit List</option>
                      <option value="JOB_NOTIFICATION">💼 Government Job Recruitment</option>
                      <option value="IMPORTANT_NOTICE">⚠️ Important Official Notice</option>
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Notification Number (Ref)</label>
                    <input 
                      type="text" 
                      value={govtForm.official_notification_number}
                      onChange={e => setGovtForm({ ...govtForm, official_notification_number: e.target.value })}
                      placeholder="e.g., SSC/2026/01-CGL"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 2: Titles & Descriptions */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  2. Headline & Descriptions
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Short Title *</label>
                    <input 
                      type="text" 
                      value={govtForm.title}
                      onChange={e => setGovtForm({ ...govtForm, title: e.target.value })}
                      placeholder="e.g., SSC CGL 2026 Application Notification Released"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Short Summary (Card View)</label>
                    <input 
                      type="text" 
                      value={govtForm.short_description}
                      onChange={e => setGovtForm({ ...govtForm, short_description: e.target.value })}
                      placeholder="Application form is now active on the official SSC portal. Apply before deadline."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Full Verified Notice Text</label>
                    <textarea 
                      rows={3}
                      value={govtForm.full_description}
                      onChange={e => setGovtForm({ ...govtForm, full_description: e.target.value })}
                      placeholder="Enter verified description, exam stages, syllabus reference, and official instructions..."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff', fontSize: '13.5px' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 3: Recruitment & Eligibility Information */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  3. Job & Eligibility Information (Only Verified Data)
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Post / Job Name</label>
                    <input 
                      type="text" 
                      value={govtForm.post_name}
                      onChange={e => setGovtForm({ ...govtForm, post_name: e.target.value })}
                      placeholder="e.g., Assistant Section Officer, Inspector"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Number of Vacancies</label>
                    <input 
                      type="text" 
                      value={govtForm.vacancy}
                      onChange={e => setGovtForm({ ...govtForm, vacancy: e.target.value })}
                      placeholder="e.g., 17,727 Vacancies"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Age Limit</label>
                    <input 
                      type="text" 
                      value={govtForm.age_limit}
                      onChange={e => setGovtForm({ ...govtForm, age_limit: e.target.value })}
                      placeholder="e.g., 18 - 30 Years (Age relaxation applicable)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Educational Qualification</label>
                    <input 
                      type="text" 
                      value={govtForm.qualification}
                      onChange={e => setGovtForm({ ...govtForm, qualification: e.target.value })}
                      placeholder="e.g., Bachelor's Degree in any discipline"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Application Fee</label>
                    <input 
                      type="text" 
                      value={govtForm.application_fee}
                      onChange={e => setGovtForm({ ...govtForm, application_fee: e.target.value })}
                      placeholder="e.g., ₹100 (SC/ST/Female: Exempted)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Selection Process</label>
                    <input 
                      type="text" 
                      value={govtForm.selection_process}
                      onChange={e => setGovtForm({ ...govtForm, selection_process: e.target.value })}
                      placeholder="Tier-1 (CBE) + Tier-2 (CBE) + Document Verification"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 4: Important Dates */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  4. Important Verified Dates (Leave blank if unannounced)
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Notification Date</label>
                    <input 
                      type="date" 
                      value={govtForm.notification_date}
                      onChange={e => setGovtForm({ ...govtForm, notification_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Application Start Date</label>
                    <input 
                      type="date" 
                      value={govtForm.application_start_date}
                      onChange={e => setGovtForm({ ...govtForm, application_start_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--amber)', marginBottom: '4px' }}>Application Last Date</label>
                    <input 
                      type="date" 
                      value={govtForm.application_last_date}
                      onChange={e => setGovtForm({ ...govtForm, application_last_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Admit Card Date</label>
                    <input 
                      type="date" 
                      value={govtForm.admit_card_date}
                      onChange={e => setGovtForm({ ...govtForm, admit_card_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--primary-light)', marginBottom: '4px' }}>Exam Date</label>
                    <input 
                      type="date" 
                      value={govtForm.exam_date}
                      onChange={e => setGovtForm({ ...govtForm, exam_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--emerald)', marginBottom: '4px' }}>Result Date</label>
                    <input 
                      type="date" 
                      value={govtForm.result_date}
                      onChange={e => setGovtForm({ ...govtForm, result_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 5: Official Source Reference */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  5. Mandatory Official Source Reference
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Source Name *</label>
                    <input 
                      type="text" 
                      value={govtForm.official_source_name}
                      onChange={e => setGovtForm({ ...govtForm, official_source_name: e.target.value })}
                      placeholder="e.g., Staff Selection Commission Official Notification"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Portal / Notification URL *</label>
                    <input 
                      type="url" 
                      value={govtForm.official_source_url}
                      onChange={e => setGovtForm({ ...govtForm, official_source_url: e.target.value })}
                      placeholder="https://ssc.gov.in/notice/..."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>
                </div>
              </div>

              {/* Section 6: Workflow Status & Push */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px', alignItems: 'center' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Workflow Stage</label>
                  <select
                    value={govtForm.verification_status}
                    onChange={e => setGovtForm({ ...govtForm, verification_status: e.target.value })}
                    style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                  >
                    <option value="DRAFT">DRAFT (Initial entry)</option>
                    <option value="PENDING_REVIEW">PENDING_REVIEW (Awaiting fact-check)</option>
                    <option value="VERIFIED">VERIFIED (Fact-checked against gazette)</option>
                    <option value="PUBLISHED">PUBLISHED (Live in student app)</option>
                  </select>
                </div>

                {govtForm.verification_status === 'PUBLISHED' && (
                  <div style={{ marginTop: '16px' }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', color: '#f8fafc', cursor: 'pointer' }}>
                      <input 
                        type="checkbox"
                        checked={govtForm.send_push_notification}
                        onChange={e => setGovtForm({ ...govtForm, send_push_notification: e.target.checked })}
                        style={{ accentColor: 'var(--cyan)', width: '16px', height: '16px' }}
                      />
                      <span>Send Push Notification to eligible users upon publishing</span>
                    </label>
                  </div>
                )}
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px', marginTop: '12px', borderTop: '1px solid var(--border-subtle)', paddingTop: '16px' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowGovtModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  <span>{editingGovt ? 'Update Exam Update' : 'Save Exam Update'}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ==========================================
          MODAL: CONFIRM PUBLISHING & PUSH NOTIFICATION
          ========================================== */}
      {showPublishConfirm && (
        <div className="modal-backdrop" onClick={() => setShowPublishConfirm(null)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '520px' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Send size={18} color="var(--emerald)" />
                <h3 style={{ fontSize: '17px', fontWeight: 700 }}>Confirm Publishing Update</h3>
              </div>
              <button className="btn-icon" onClick={() => setShowPublishConfirm(null)}>
                <X size={16} />
              </button>
            </div>

            <div style={{ padding: '24px' }}>
              <p style={{ color: '#f8fafc', fontSize: '14.5px', marginBottom: '8px' }}>
                Are you ready to publish <strong>{showPublishConfirm.exam_name}</strong> to the student feed?
              </p>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginBottom: '20px' }}>
                This will make the update immediately visible to all students on the home screen and Government Exams section.
              </p>

              <div style={{
                background: 'rgba(255, 255, 255, 0.03)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-sm)',
                padding: '14px',
                marginBottom: '16px'
              }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13.5px', color: '#f8fafc', cursor: 'pointer' }}>
                  <input 
                    type="checkbox"
                    checked={sendPushOnPublish}
                    onChange={e => setSendPushOnPublish(e.target.checked)}
                    style={{ accentColor: 'var(--cyan)', width: '18px', height: '18px' }}
                  />
                  <span>
                    <strong>Send Push Notification</strong> to students interested in {showPublishConfirm.category} exams
                  </span>
                </label>
              </div>
            </div>

            <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setShowPublishConfirm(null)}>
                Cancel
              </button>
              <button 
                className="btn btn-emerald" 
                onClick={() => handleTransitionStatus(showPublishConfirm.id, 'PUBLISHED', sendPushOnPublish)}
              >
                Confirm & Publish
              </button>
            </div>
          </div>
        </div>
      )}
      
            {/* Add Verified PYQ Modal */}
      {showAddModal && (
        <div className="modal-backdrop" onClick={() => setShowAddModal(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '600px', maxHeight: '90vh', overflowY: 'auto' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Add Verified Previous Year Question</h3>
              <button className="btn-icon" onClick={() => setShowAddModal(false)} style={{ width: '32px', height: '32px' }}>✕</button>
            </div>

            <form onSubmit={handleCreatePyq} style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Question Text:
                </label>
                <textarea 
                  rows={3} 
                  value={newPyq.question}
                  onChange={e => setNewPyq({ ...newPyq, question: e.target.value })}
                  placeholder="Enter the verified question text..."
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', color: '#fff', fontSize: '14px' }}
                  required
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Option A</label>
                  <input 
                    type="text" 
                    value={newPyq.optionA} 
                    onChange={e => setNewPyq({ ...newPyq, optionA: e.target.value })} 
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }} 
                    required 
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Option B</label>
                  <input 
                    type="text" 
                    value={newPyq.optionB} 
                    onChange={e => setNewPyq({ ...newPyq, optionB: e.target.value })} 
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }} 
                    required 
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Option C</label>
                  <input 
                    type="text" 
                    value={newPyq.optionC} 
                    onChange={e => setNewPyq({ ...newPyq, optionC: e.target.value })} 
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }} 
                    required 
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Option D</label>
                  <input 
                    type="text" 
                    value={newPyq.optionD} 
                    onChange={e => setNewPyq({ ...newPyq, optionD: e.target.value })} 
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }} 
                    required 
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--emerald)' }}>
                  Correct Answer (Must match one option exactly):
                </label>
                <input 
                  type="text" 
                  value={newPyq.correct_answer}
                  onChange={e => setNewPyq({ ...newPyq, correct_answer: e.target.value })}
                  placeholder="Paste the exact correct option string..."
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-emerald-glow)', color: '#fff', fontSize: '14px' }}
                  required
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Detailed Grammatical / Conceptual Explanation:
                </label>
                <textarea 
                  rows={2} 
                  value={newPyq.explanation}
                  onChange={e => setNewPyq({ ...newPyq, explanation: e.target.value })}
                  placeholder="Explain the syntactic rule or formula..."
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', color: '#fff', fontSize: '14px' }}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Exam Authority</label>
                  <select 
                    value={newPyq.exam_id} 
                    onChange={e => setNewPyq({ ...newPyq, exam_id: e.target.value })}
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                  >
                    <option value="1">SSC CGL 2024 Tier-1</option>
                    <option value="2">SSC CGL 2023 Tier-1</option>
                    <option value="3">UPSC CDS 2023</option>
                    <option value="4">IBPS PO 2024</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Verified Source Citation</label>
                  <select 
                    value={newPyq.source_id} 
                    onChange={e => setNewPyq({ ...newPyq, source_id: e.target.value })}
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                  >
                    <option value="3">Staff Selection Commission Official Key</option>
                    <option value="5">UPSC Official Portal</option>
                    <option value="1">British Council LearnEnglish</option>
                  </select>
                </div>
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px', marginTop: '12px' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowAddModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  <span>Save & Publish PYQ</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Add / Edit Current Affair Modal */}
      {showCaModal && (
        <div className="modal-backdrop" onClick={() => setShowCaModal(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '640px', maxHeight: '90vh', overflowY: 'auto' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '18px', fontWeight: 700 }}>
                {editingCa ? `Edit Current Affair #${editingCa.id}` : 'Add Official Current Affair'}
              </h3>
              <button className="btn-icon" onClick={() => setShowCaModal(false)} style={{ width: '32px', height: '32px' }}>✕</button>
            </div>

            <form onSubmit={handleSaveCa} style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Title / Headline:
                </label>
                <input 
                  type="text" 
                  value={caForm.title}
                  onChange={e => setCaForm({ ...caForm, title: e.target.value })}
                  placeholder="e.g., Gaganyaan Mission: Second Uncrewed Orbital Flight Scheduled"
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', color: '#fff', fontSize: '14px' }}
                  required
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Category</label>
                  <select 
                    value={caForm.category}
                    onChange={e => setCaForm({ ...caForm, category: e.target.value })}
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                  >
                    <option value="Science & Technology">Science & Technology</option>
                    <option value="Economy & Energy">Economy & Energy</option>
                    <option value="Defense & Security">Defense & Security</option>
                    <option value="Governance & Tech">Governance & Tech</option>
                    <option value="National Initiatives">National Initiatives</option>
                    <option value="International Relations">International Relations</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Date</label>
                  <input 
                    type="date"
                    value={caForm.date}
                    onChange={e => setCaForm({ ...caForm, date: e.target.value })}
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    required
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Comprehensive Summary / Background:
                </label>
                <textarea 
                  rows={3} 
                  value={caForm.summary}
                  onChange={e => setCaForm({ ...caForm, summary: e.target.value })}
                  placeholder="Provide an objective, syllabus-relevant summary..."
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', color: '#fff', fontSize: '14px' }}
                  required
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Important Facts (One fact per line):
                </label>
                <textarea 
                  rows={3} 
                  value={caForm.important_facts}
                  onChange={e => setCaForm({ ...caForm, important_facts: e.target.value })}
                  placeholder="LVM3 rocket to carry the orbital module&#10;Key environmental life-support systems (ECLSS) tested&#10;Recovery operations led by Indian Navy and Coast Guard"
                  style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', color: '#fff', fontSize: '13.5px' }}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Source Authority Name</label>
                  <input 
                    type="text" 
                    value={caForm.source_name}
                    onChange={e => setCaForm({ ...caForm, source_name: e.target.value })}
                    placeholder="e.g., Press Information Bureau (PIB)"
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    required
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Source Verification URL</label>
                  <input 
                    type="url" 
                    value={caForm.source_url}
                    onChange={e => setCaForm({ ...caForm, source_url: e.target.value })}
                    placeholder="https://pib.gov.in/..."
                    style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    required
                  />
                </div>
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Publication Status</label>
                <select 
                  value={caForm.status}
                  onChange={e => setCaForm({ ...caForm, status: e.target.value })}
                  style={{ width: '100%', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                >
                  <option value="published">Published (Live in student app)</option>
                  <option value="draft">Draft / Unpublished (Internal review only)</option>
                </select>
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px', marginTop: '12px' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowCaModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-emerald">
                  <span>{editingCa ? 'Update Current Affair' : 'Save & Publish'}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
      {/* Add / Edit Study Note Modal (Requirement 4) */}
      {showNoteModal && (
        <div className="modal-backdrop" onClick={() => !noteUploading && setShowNoteModal(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '680px', maxHeight: '92vh', overflowY: 'auto' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{ width: '32px', height: '32px', borderRadius: '6px', background: 'rgba(99, 102, 241, 0.15)', color: 'var(--cyan)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <FileText size={18} />
                </div>
                <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', margin: 0 }}>
                  {editingNote ? `Edit Note #${editingNote.id}` : 'Add New Note (Upload Real PDF)'}
                </h3>
              </div>
              <button 
                className="btn-icon" 
                onClick={() => !noteUploading && setShowNoteModal(false)} 
                style={{ width: '32px', height: '32px' }}
                disabled={noteUploading}
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleSaveNote} style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '18px' }}>
              {noteFormError && (
                <div style={{
                  padding: '10px 14px',
                  borderRadius: 'var(--radius-sm)',
                  background: 'rgba(244, 63, 94, 0.12)',
                  border: '1px solid rgba(244, 63, 94, 0.3)',
                  color: 'var(--rose)',
                  fontSize: '13px'
                }}>
                  {noteFormError}
                </div>
              )}

              {/* PDF File Upload Input (Requirement 4 & 5) */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 700, marginBottom: '6px', color: '#fff' }}>
                  PDF File <span style={{ color: 'var(--rose)' }}>*</span>
                </label>
                <div style={{
                  padding: '16px',
                  borderRadius: 'var(--radius-sm)',
                  border: '2px dashed var(--border-light)',
                  background: 'rgba(255, 255, 255, 0.02)',
                  textAlign: 'center'
                }}>
                  <input
                    type="file"
                    id="admin-pdf-upload-input"
                    accept=".pdf,application/pdf"
                    onChange={e => {
                      const file = e.target.files?.[0];
                      if (file) {
                        setNotePdfFile(file);
                        if (!noteForm.title) {
                          const cleanTitle = file.name
                            .replace(/\.[^/.]+$/, '')
                            .replace(/_/g, ' ')
                            .replace(/-/g, ' ');
                          setNoteForm(prev => ({ ...prev, title: cleanTitle }));
                        }
                      }
                    }}
                    style={{ display: 'none' }}
                  />
                  <label
                    htmlFor="admin-pdf-upload-input"
                    className="btn btn-secondary"
                    style={{ cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}
                  >
                    <Upload size={16} />
                    <span>{notePdfFile ? 'Change Selected PDF' : 'Choose PDF File'}</span>
                  </label>
                  
                  {notePdfFile ? (
                    <div style={{ marginTop: '8px', fontSize: '13px', color: 'var(--emerald)', fontWeight: 600 }}>
                      ✓ Selected: {notePdfFile.name} ({(notePdfFile.size / (1024 * 1024)).toFixed(2)} MB)
                    </div>
                  ) : editingNote ? (
                    <div style={{ marginTop: '8px', fontSize: '12.5px', color: 'var(--text-secondary)' }}>
                      Current File: <strong style={{ color: '#fff' }}>{editingNote.file_name}</strong> ({editingNote.file_size}).
                      <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                        (Choose a new PDF above only if you wish to replace the current file)
                      </div>
                    </div>
                  ) : (
                    <p style={{ color: 'var(--text-muted)', fontSize: '12.5px', margin: '4px 0 0' }}>
                      Upload real study material in .pdf format (e.g. English_Notes.pdf, Mathematics_Notes.pdf).
                    </p>
                  )}
                </div>
              </div>

              {/* Title */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, marginBottom: '6px', color: 'var(--text-secondary)' }}>
                  Note Title <span style={{ color: 'var(--rose)' }}>*</span>
                </label>
                <input 
                  type="text" 
                  value={noteForm.title}
                  onChange={e => setNoteForm({ ...noteForm, title: e.target.value })}
                  placeholder="e.g. English Grammar - Complete Parts of Speech Notes"
                  style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-dark)', color: '#fff', fontSize: '14px' }}
                  required
                />
              </div>

              {/* Subject, Topic, Subtopic */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Subject <span style={{ color: 'var(--rose)' }}>*</span>
                  </label>
                  <select
                    value={noteForm.subject_name}
                    onChange={e => setNoteForm({ ...noteForm, subject_name: e.target.value })}
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                    required
                  >
                    <option value="English">English</option>
                    <option value="Mathematics">Mathematics</option>
                    <option value="Reasoning">Reasoning</option>
                    <option value="General Awareness">General Awareness</option>
                    <option value="General Science">General Science</option>
                    <option value="Computer Knowledge">Computer Knowledge</option>
                    <option value="Other">Other</option>
                  </select>
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Topic <span style={{ color: 'var(--rose)' }}>*</span>
                  </label>
                  <input
                    type="text"
                    value={noteForm.topic_name}
                    onChange={e => setNoteForm({ ...noteForm, topic_name: e.target.value })}
                    placeholder="e.g. Parts of Speech or Algebra"
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                    required
                  />
                </div>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Subtopic (Optional)
                  </label>
                  <input
                    type="text"
                    value={noteForm.subtopic_name}
                    onChange={e => setNoteForm({ ...noteForm, subtopic_name: e.target.value })}
                    placeholder="e.g. Nouns, Pronouns, & Prepositions"
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                  />
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Estimated Page Count (Optional)
                  </label>
                  <input
                    type="number"
                    min="1"
                    value={noteForm.page_count}
                    onChange={e => setNoteForm({ ...noteForm, page_count: e.target.value })}
                    placeholder="e.g. 15"
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                  />
                </div>
              </div>

              {/* Description */}
              <div>
                <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                  Description / Note Summary
                </label>
                <textarea 
                  rows={3}
                  value={noteForm.description}
                  onChange={e => setNoteForm({ ...noteForm, description: e.target.value })}
                  placeholder="Key concepts, formula summaries, exam hints covered in this document..."
                  style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                />
              </div>

              {/* Source & Status */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Source / Reference
                  </label>
                  <input
                    type="text"
                    value={noteForm.source}
                    onChange={e => setNoteForm({ ...noteForm, source: e.target.value })}
                    placeholder="e.g. Official Faculty Curriculum / NCERT"
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                  />
                </div>

                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                    Publication Status (Workflow Step)
                  </label>
                  <select
                    value={noteForm.status}
                    onChange={e => setNoteForm({ ...noteForm, status: e.target.value })}
                    style={{ width: '100%', padding: '9px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff', fontSize: '13.5px' }}
                  >
                    <option value="DRAFT">1. Draft</option>
                    <option value="PENDING_REVIEW">2. Pending Review</option>
                    <option value="VERIFIED">3. Verified</option>
                    <option value="PUBLISHED">4. Published (Live in User's 📚 Notes)</option>
                    <option value="ARCHIVED">5. Archived</option>
                  </select>
                </div>
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px', marginTop: '8px' }}>
                <button 
                  type="button" 
                  className="btn btn-secondary" 
                  onClick={() => setShowNoteModal(false)}
                  disabled={noteUploading}
                >
                  Cancel
                </button>
                <button 
                  type="submit" 
                  className="btn btn-primary"
                  disabled={noteUploading}
                  style={{ minWidth: '140px' }}
                >
                  {noteUploading ? 'Uploading & Saving...' : editingNote ? 'Update Note' : 'Upload & Save'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Admin Real PDF Preview Modal */}
      {previewingNote && (
        <div className="modal-backdrop" onClick={() => setPreviewingNote(null)}>
          <div 
            className="modal-content" 
            onClick={e => e.stopPropagation()} 
            style={{ 
              width: '92vw', 
              maxWidth: '1100px', 
              height: '88vh', 
              display: 'flex', 
              flexDirection: 'column', 
              padding: 0,
              overflow: 'hidden'
            }}
          >
            {/* Header */}
            <div style={{
              padding: '14px 20px',
              background: 'var(--bg-card)',
              borderBottom: '1px solid var(--border-subtle)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              gap: '12px',
              flexWrap: 'wrap'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{ width: '32px', height: '32px', borderRadius: '6px', background: 'rgba(244, 63, 94, 0.15)', color: 'var(--rose)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <FileText size={18} />
                </div>
                <div>
                  <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#fff' }}>
                    {previewingNote.title}
                  </h4>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                    {previewingNote.file_name} • {previewingNote.file_size} • Status: <strong style={{ color: 'var(--cyan)' }}>{previewingNote.status}</strong>
                  </div>
                </div>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <a
                  href={`http://localhost:3001${previewingNote.file_url}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-secondary"
                  style={{ padding: '6px 12px', fontSize: '12.5px', gap: '6px', textDecoration: 'none' }}
                  title="Open in Browser New Tab"
                >
                  <ExternalLink size={14} />
                  <span>Open Tab</span>
                </a>
                <a
                  href={`http://localhost:3001${previewingNote.file_url}`}
                  download={previewingNote.file_name || `${previewingNote.title}.pdf`}
                  className="btn btn-secondary"
                  style={{ padding: '6px 12px', fontSize: '12.5px', gap: '6px', textDecoration: 'none' }}
                  title="Download File"
                >
                  <Download size={14} />
                  <span>Download</span>
                </a>
                <button
                  className="btn btn-secondary"
                  onClick={() => setPreviewingNote(null)}
                  style={{ padding: '6px 12px', fontSize: '12.5px' }}
                >
                  ✕ Close
                </button>
              </div>
            </div>

            {/* Viewer Iframe */}
            <div style={{ flex: 1, background: '#1e293b', width: '100%', height: '100%' }}>
              <iframe
                src={`http://localhost:3001${previewingNote.file_url}#toolbar=1`}
                title={previewingNote.title}
                style={{ width: '100%', height: '100%', border: 'none' }}
              />
            </div>
          </div>
        </div>
      )}

      {/* ==========================================
          MODAL: CREATE / EDIT MOCK EXAM (MINIMUM 50 QUESTIONS)
          ========================================== */}
      {showCreateMockModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000,
          padding: '20px'
        }}>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-lg)',
            width: '100%',
            maxWidth: '920px',
            maxHeight: '92vh',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.6)'
          }}>
            {/* Header */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '18px 24px',
              borderBottom: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{
                  width: '36px',
                  height: '36px',
                  borderRadius: '8px',
                  background: 'rgba(6, 182, 212, 0.15)',
                  color: 'var(--cyan)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  <Target size={20} />
                </div>
                <div>
                  <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 700, color: '#fff' }}>
                    {editingMockExam ? 'Edit Mock Exam (50+ Questions)' : 'Create Full-Length Mock Exam (Min 50 Questions)'}
                  </h3>
                  <p style={{ margin: '2px 0 0', fontSize: '12.5px', color: 'var(--text-muted)' }}>
                    Admin Console • Strict Competitive Standard (Minimum 50 questions mandatory)
                  </p>
                </div>
              </div>
              <button
                className="btn btn-secondary"
                onClick={() => setShowCreateMockModal(false)}
                style={{ padding: '6px 10px', fontSize: '14px' }}
              >
                ✕
              </button>
            </div>

            {/* Modal Body */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '24px' }}>
              {mockFormError && (
                <div style={{
                  padding: '12px 16px',
                  borderRadius: 'var(--radius-sm)',
                  background: 'rgba(239, 68, 68, 0.12)',
                  border: '1px solid rgba(239, 68, 68, 0.3)',
                  color: 'var(--rose)',
                  fontSize: '13px',
                  marginBottom: '20px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '10px'
                }}>
                  <AlertCircle size={18} />
                  <span>{mockFormError}</span>
                </div>
              )}

              {/* Policy Banner inside Modal */}
              <div style={{
                padding: '12px 16px',
                borderRadius: 'var(--radius-sm)',
                background: 'rgba(6, 182, 212, 0.08)',
                border: '1px solid rgba(6, 182, 212, 0.25)',
                marginBottom: '20px',
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                fontSize: '12.5px',
                color: 'var(--text-secondary)'
              }}>
                <span className="badge badge-cyan" style={{ fontSize: '11px', flexShrink: 0 }}>
                  Mandatory Rule
                </span>
                <span>
                  Every mock exam <strong>must contain at least 50 questions</strong> to maintain real-world exam standards (Tier-1 full simulation). Submissions with fewer than 50 questions are blocked.
                </span>
              </div>

              <form id="mockExamForm" onSubmit={handleSaveMockExam}>
                {/* Basic Meta Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '16px', marginBottom: '20px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Mock Exam Title *
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      placeholder="e.g. SSC CGL Tier-1 All-India Mock Test #3"
                      value={mockForm.title}
                      onChange={e => setMockForm({ ...mockForm, title: e.target.value })}
                      required
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Category *
                    </label>
                    <select
                      className="form-control"
                      value={mockForm.category}
                      onChange={e => setMockForm({ ...mockForm, category: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    >
                      <option value="SSC">SSC (CGL, CHSL, MTS, CPO)</option>
                      <option value="UPSC">UPSC / Civil Services</option>
                      <option value="Railway">Railway / RRB NTPC</option>
                      <option value="Banking">Banking (IBPS, SBI, RBI)</option>
                      <option value="Defence">Defence / Armed Forces</option>
                      <option value="KPSC">KPSC / State PSC</option>
                      <option value="Central Government">Central Government Overall</option>
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Target Exam Name
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      placeholder="e.g. SSC CGL 2026 / RRB NTPC"
                      value={mockForm.target_exam}
                      onChange={e => setMockForm({ ...mockForm, target_exam: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>
                </div>

                {/* Exam Settings Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '16px', marginBottom: '20px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Duration (Minutes)
                    </label>
                    <input
                      type="number"
                      min="15"
                      max="180"
                      className="form-control"
                      value={mockForm.duration_minutes}
                      onChange={e => setMockForm({ ...mockForm, duration_minutes: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Passing Cut-off (%)
                    </label>
                    <input
                      type="number"
                      min="35"
                      max="100"
                      className="form-control"
                      value={mockForm.passing_percentage}
                      onChange={e => setMockForm({ ...mockForm, passing_percentage: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Negative Marking / Wrong
                    </label>
                    <input
                      type="number"
                      step="0.05"
                      min="0"
                      max="1"
                      className="form-control"
                      value={mockForm.negative_marking}
                      onChange={e => setMockForm({ ...mockForm, negative_marking: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Publication Status
                    </label>
                    <select
                      className="form-control"
                      value={mockForm.status}
                      onChange={e => setMockForm({ ...mockForm, status: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    >
                      <option value="published">Published (Live for Students)</option>
                      <option value="draft">Draft (Admin Only)</option>
                    </select>
                  </div>
                </div>

                {/* Description & Instructions */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', marginBottom: '24px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Exam Description
                    </label>
                    <textarea
                      rows={2}
                      className="form-control"
                      placeholder="Brief overview of what this mock covers..."
                      value={mockForm.description}
                      onChange={e => setMockForm({ ...mockForm, description: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13px',
                        resize: 'vertical'
                      }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '13px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Test Instructions (Shown to Students)
                    </label>
                    <textarea
                      rows={2}
                      className="form-control"
                      placeholder="Guidelines, marking rules, timing..."
                      value={mockForm.instructions}
                      onChange={e => setMockForm({ ...mockForm, instructions: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        background: 'var(--bg-card)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        color: '#fff',
                        fontSize: '13px',
                        resize: 'vertical'
                      }}
                    />
                  </div>
                </div>

                {/* 50-QUESTION COMPOSITION ENGINE */}
                <div style={{
                  padding: '20px',
                  borderRadius: 'var(--radius-md)',
                  background: 'rgba(255, 255, 255, 0.02)',
                  border: '1px solid var(--border-subtle)',
                  marginBottom: '20px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px', flexWrap: 'wrap', gap: '12px' }}>
                    <div>
                      <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#fff', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span>Prepare Mock Exam Questions</span>
                        <span className={`badge ${mockForm.selected_question_ids.length >= 50 ? 'badge-emerald' : 'badge-amber'}`} style={{ fontSize: '11px' }}>
                          {mockForm.selected_question_ids.length} / 50 Minimum Mandatory
                        </span>
                      </h4>
                      <div style={{ fontSize: '12.5px', color: 'var(--text-secondary)', marginTop: '3px' }}>
                        Combine fast 1-click competitive presets, select from 830+ bank questions, and compose custom questions.
                      </div>
                    </div>

                    {/* Mode / Method Selector Tabs */}
                    <div style={{ display: 'flex', gap: '6px', background: 'var(--bg-card)', padding: '4px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                      <button
                        type="button"
                        className={`btn ${activePreparedTab === 'auto' ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setActivePreparedTab('auto')}
                        style={{ padding: '6px 12px', fontSize: '12px', gap: '5px' }}
                      >
                        <Sparkles size={13} />
                        <span>⚡ 1-Click Fast Presets (50 Qs)</span>
                      </button>
                      <button
                        type="button"
                        className={`btn ${activePreparedTab === 'bank' ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => {
                          setActivePreparedTab('bank');
                          if (questionBank.length === 0) fetchQuestionBank('All', '');
                        }}
                        style={{ padding: '6px 12px', fontSize: '12px', gap: '5px' }}
                      >
                        <BookOpen size={13} />
                        <span>📋 Question Bank ({questionBank.length > 0 ? questionBank.length : '830+'})</span>
                      </button>
                      <button
                        type="button"
                        className={`btn ${activePreparedTab === 'author' ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setActivePreparedTab('author')}
                        style={{ padding: '6px 12px', fontSize: '12px', gap: '5px' }}
                      >
                        <Edit2 size={13} />
                        <span>✍️ Author Questions</span>
                      </button>
                    </div>
                  </div>

                  {/* TAB 1: 1-CLICK FAST PRESETS */}
                  {activePreparedTab === 'auto' && (
                    <div style={{ background: 'rgba(255, 255, 255, 0.02)', padding: '16px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', marginBottom: '16px' }}>
                      <div style={{ fontSize: '12px', color: 'var(--cyan)', marginBottom: '10px', fontWeight: 700, letterSpacing: '0.5px' }}>
                        CLICK A PRESET TO INSTANTLY LOAD 50 VERIFIED QUESTIONS:
                      </div>
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: '10px', marginBottom: '16px' }}>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleApplyPreset('ssc')}
                          disabled={autoAssembling}
                          style={{ fontSize: '12px', padding: '10px 14px', justifyContent: 'flex-start', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '3px' }}
                        >
                          <span style={{ fontWeight: 700, color: '#fff' }}>🎯 SSC Tier-1 Pattern</span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>15 Eng + 15 Math + 10 Reas + 10 GA = 50 Qs</span>
                        </button>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleApplyPreset('railway')}
                          disabled={autoAssembling}
                          style={{ fontSize: '12px', padding: '10px 14px', justifyContent: 'flex-start', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '3px' }}
                        >
                          <span style={{ fontWeight: 700, color: '#fff' }}>🚂 Railway RRB NTPC Pattern</span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>10 Eng + 15 Math + 15 Reas + 10 GA = 50 Qs</span>
                        </button>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleApplyPreset('banking')}
                          disabled={autoAssembling}
                          style={{ fontSize: '12px', padding: '10px 14px', justifyContent: 'flex-start', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '3px' }}
                        >
                          <span style={{ fontWeight: 700, color: '#fff' }}>🏦 Banking Prelims Pattern</span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>20 Eng + 15 Math + 15 Reas = 50 Qs</span>
                        </button>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleApplyPreset('balanced')}
                          disabled={autoAssembling}
                          style={{ fontSize: '12px', padding: '10px 14px', justifyContent: 'flex-start', textAlign: 'left', display: 'flex', flexDirection: 'column', gap: '3px' }}
                        >
                          <span style={{ fontWeight: 700, color: '#fff' }}>⚖️ Balanced 4-Subject</span>
                          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>12 Eng + 13 Math + 13 Reas + 12 GA = 50 Qs</span>
                        </button>
                      </div>

                      {/* Custom Distribution Adjusters */}
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '8px', fontWeight: 600 }}>
                        Or customize subject questions balance:
                      </div>
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '10px', marginBottom: '12px' }}>
                        <div style={{ padding: '8px 12px', borderRadius: '4px', background: 'var(--bg-card)', border: '1px solid var(--border-subtle)' }}>
                          <label style={{ display: 'block', fontSize: '11px', color: 'var(--cyan)', fontWeight: 600, marginBottom: '4px' }}>English</label>
                          <input
                            type="number"
                            min="0"
                            max="50"
                            value={mockForm.subject_distribution.english}
                            onChange={e => setMockForm({
                              ...mockForm,
                              subject_distribution: { ...mockForm.subject_distribution, english: parseInt(e.target.value, 10) || 0 }
                            })}
                            style={{ width: '100%', padding: '4px 8px', background: '#0f172a', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '12.5px' }}
                          />
                        </div>
                        <div style={{ padding: '8px 12px', borderRadius: '4px', background: 'var(--bg-card)', border: '1px solid var(--border-subtle)' }}>
                          <label style={{ display: 'block', fontSize: '11px', color: 'var(--primary-light)', fontWeight: 600, marginBottom: '4px' }}>Math / Quant</label>
                          <input
                            type="number"
                            min="0"
                            max="50"
                            value={mockForm.subject_distribution.math}
                            onChange={e => setMockForm({
                              ...mockForm,
                              subject_distribution: { ...mockForm.subject_distribution, math: parseInt(e.target.value, 10) || 0 }
                            })}
                            style={{ width: '100%', padding: '4px 8px', background: '#0f172a', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '12.5px' }}
                          />
                        </div>
                        <div style={{ padding: '8px 12px', borderRadius: '4px', background: 'var(--bg-card)', border: '1px solid var(--border-subtle)' }}>
                          <label style={{ display: 'block', fontSize: '11px', color: 'var(--amber)', fontWeight: 600, marginBottom: '4px' }}>Reasoning</label>
                          <input
                            type="number"
                            min="0"
                            max="50"
                            value={mockForm.subject_distribution.reasoning}
                            onChange={e => setMockForm({
                              ...mockForm,
                              subject_distribution: { ...mockForm.subject_distribution, reasoning: parseInt(e.target.value, 10) || 0 }
                            })}
                            style={{ width: '100%', padding: '4px 8px', background: '#0f172a', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '12.5px' }}
                          />
                        </div>
                        <div style={{ padding: '8px 12px', borderRadius: '4px', background: 'var(--bg-card)', border: '1px solid var(--border-subtle)' }}>
                          <label style={{ display: 'block', fontSize: '11px', color: 'var(--emerald)', fontWeight: 600, marginBottom: '4px' }}>General Aware.</label>
                          <input
                            type="number"
                            min="0"
                            max="50"
                            value={mockForm.subject_distribution.general_awareness}
                            onChange={e => setMockForm({
                              ...mockForm,
                              subject_distribution: { ...mockForm.subject_distribution, general_awareness: parseInt(e.target.value, 10) || 0 }
                            })}
                            style={{ width: '100%', padding: '4px 8px', background: '#0f172a', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '12.5px' }}
                          />
                        </div>
                      </div>

                      <button
                        type="button"
                        className="btn btn-secondary"
                        onClick={async () => {
                          try {
                            setAutoAssembling(true);
                            const res = await fetch('http://localhost:3001/api/admin/mock-exams/generate-set', {
                              method: 'POST',
                              headers: { 'Content-Type': 'application/json', 'x-user-role': 'admin' },
                              body: JSON.stringify({ subject_distribution: mockForm.subject_distribution })
                            });
                            if (res.ok) {
                              const json = await res.json();
                              setMockForm(prev => ({ ...prev, selected_question_ids: json.question_ids || [] }));
                            }
                          } catch (err) {
                            console.error('Error generating custom set:', err);
                          } finally {
                            setAutoAssembling(false);
                          }
                        }}
                        disabled={autoAssembling}
                        style={{ fontSize: '12px', padding: '6px 14px', gap: '6px' }}
                      >
                        <Sparkles size={14} color="var(--cyan)" />
                        <span>{autoAssembling ? 'Assembling 50 Questions...' : 'Assemble Questions from Distribution'}</span>
                      </button>
                    </div>
                  )}

                  {/* TAB 2: QUESTION BANK BROWSER */}
                  {activePreparedTab === 'bank' && (
                    <div style={{ background: 'rgba(255, 255, 255, 0.02)', padding: '16px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', marginBottom: '16px' }}>
                      <div style={{ display: 'flex', gap: '10px', marginBottom: '12px', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between' }}>
                        <div style={{ display: 'flex', gap: '8px', flex: 1, minWidth: '240px' }}>
                          <div style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: '6px',
                            padding: '6px 10px',
                            background: 'var(--bg-card)',
                            borderRadius: 'var(--radius-sm)',
                            border: '1px solid var(--border-subtle)',
                            flex: 1
                          }}>
                            <Search size={14} color="var(--text-muted)" />
                            <input
                              type="text"
                              placeholder="Search questions by text or topic..."
                              value={qbSearchQuery}
                              onChange={e => {
                                setQbSearchQuery(e.target.value);
                                fetchQuestionBank(qbSubjectFilter, e.target.value);
                              }}
                              style={{ border: 'none', outline: 'none', background: 'transparent', color: '#fff', fontSize: '12.5px', width: '100%' }}
                            />
                          </div>

                          <select
                            value={qbSubjectFilter}
                            onChange={e => {
                              setQbSubjectFilter(e.target.value);
                              fetchQuestionBank(e.target.value, qbSearchQuery);
                            }}
                            style={{
                              padding: '6px 10px',
                              background: 'var(--bg-card)',
                              borderRadius: 'var(--radius-sm)',
                              border: '1px solid var(--border-subtle)',
                              color: '#fff',
                              fontSize: '12px'
                            }}
                          >
                            <option value="All">All Subjects (830+ Qs)</option>
                            <option value="English">English</option>
                            <option value="Math">Quantitative Aptitude</option>
                            <option value="Reason">Reasoning</option>
                            <option value="Awareness">General Awareness</option>
                          </select>
                        </div>

                        <div style={{ display: 'flex', gap: '8px' }}>
                          <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={() => {
                              const first50 = questionBank.slice(0, 50).map(q => q.id);
                              setMockForm(prev => ({
                                ...prev,
                                selected_question_ids: Array.from(new Set([...prev.selected_question_ids, ...first50]))
                              }));
                            }}
                            style={{ fontSize: '11.5px', padding: '5px 10px' }}
                          >
                            + Select Top 50
                          </button>
                          <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={() => setMockForm(prev => ({ ...prev, selected_question_ids: [] }))}
                            style={{ fontSize: '11.5px', padding: '5px 10px', color: 'var(--text-muted)' }}
                          >
                            Clear All
                          </button>
                        </div>
                      </div>

                      {/* Scrollable list */}
                      <div style={{
                        maxHeight: '220px',
                        overflowY: 'auto',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        background: '#0b1120',
                        padding: '6px'
                      }}>
                        {questionBank.length === 0 ? (
                          <div style={{ padding: '20px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '12.5px' }}>
                            Loading question bank questions...
                          </div>
                        ) : (
                          questionBank.map(q => {
                            const isSelected = mockForm.selected_question_ids.includes(q.id);
                            return (
                              <div
                                key={q.id}
                                onClick={() => {
                                  if (isSelected) {
                                    setMockForm(prev => ({
                                      ...prev,
                                      selected_question_ids: prev.selected_question_ids.filter(id => id !== q.id)
                                    }));
                                  } else {
                                    setMockForm(prev => ({
                                      ...prev,
                                      selected_question_ids: [...prev.selected_question_ids, q.id]
                                    }));
                                  }
                                }}
                                style={{
                                  display: 'flex',
                                  alignItems: 'flex-start',
                                  gap: '10px',
                                  padding: '7px 10px',
                                  borderRadius: '4px',
                                  background: isSelected ? 'rgba(6, 182, 212, 0.12)' : 'transparent',
                                  borderBottom: '1px solid rgba(255, 255, 255, 0.03)',
                                  cursor: 'pointer'
                                }}
                              >
                                <input
                                  type="checkbox"
                                  checked={isSelected}
                                  onChange={() => {}}
                                  style={{ marginTop: '3px', cursor: 'pointer' }}
                                />
                                <div style={{ flex: 1, minWidth: 0 }}>
                                  <div style={{ fontSize: '12.5px', color: isSelected ? '#fff' : 'var(--text-secondary)', lineHeight: 1.4 }}>
                                    {q.question}
                                  </div>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '3px', fontSize: '11px', color: 'var(--text-muted)' }}>
                                    <span style={{ color: 'var(--cyan)' }}>{q.subject || 'General'}</span>
                                    <span>•</span>
                                    <span>{q.topic || 'General'}</span>
                                    <span>•</span>
                                    <span style={{ color: 'var(--emerald)' }}>Ans: {q.correct_answer}</span>
                                  </div>
                                </div>
                              </div>
                            );
                          })
                        )}
                      </div>
                    </div>
                  )}

                  {/* TAB 3: ADMIN QUESTION AUTHORING */}
                  {activePreparedTab === 'author' && (
                    <div style={{ background: 'rgba(255, 255, 255, 0.02)', padding: '16px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', marginBottom: '16px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px' }}>
                        <div>
                          <div style={{ fontWeight: 700, fontSize: '13.5px', color: '#fff', marginBottom: '3px' }}>
                            ✍️ Author Custom Questions for this Mock Exam
                          </div>
                          <div style={{ fontSize: '12px', color: 'var(--text-secondary)', maxWidth: '520px', lineHeight: 1.4 }}>
                            Write your own question prompt, MCQ choices A/B/C/D, correct answer, subject, marks, and explanation. Newly composed questions are saved to the persistent Question Bank and automatically added to this mock exam.
                          </div>
                        </div>
                        <button
                          type="button"
                          className="btn btn-primary"
                          onClick={() => handleOpenAddQuestionModal()}
                          style={{ padding: '8px 16px', fontSize: '13px', gap: '6px' }}
                        >
                          <Plus size={16} />
                          <span>+ Write & Add New Question</span>
                        </button>
                      </div>
                    </div>
                  )}

                  {/* CURRENTLY PREPARED QUESTIONS LIST & LIVE VALIDATION */}
                  <div style={{
                    padding: '14px 18px',
                    borderRadius: 'var(--radius-sm)',
                    background: mockForm.selected_question_ids.length >= 50 ? 'rgba(16, 185, 129, 0.08)' : 'rgba(245, 158, 11, 0.08)',
                    border: `1px solid ${mockForm.selected_question_ids.length >= 50 ? 'rgba(16, 185, 129, 0.3)' : 'rgba(245, 158, 11, 0.3)'}`
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        {mockForm.selected_question_ids.length >= 50 ? (
                          <CheckCircle2 size={18} color="var(--emerald)" />
                        ) : (
                          <AlertTriangle size={18} color="var(--amber)" />
                        )}
                        <span style={{ fontSize: '13.5px', fontWeight: 700, color: mockForm.selected_question_ids.length >= 50 ? 'var(--emerald)' : 'var(--amber)' }}>
                          Prepared Questions: {mockForm.selected_question_ids.length} / 50 Minimum Mandatory
                        </span>
                        {mockForm.selected_question_ids.length >= 50 ? (
                          <span style={{ fontSize: '12px', color: 'var(--emerald)' }}>✓ Full 50-Question Mock Ready!</span>
                        ) : (
                          <span style={{ fontSize: '12px', color: 'var(--amber)' }}>
                            (Requires at least {50 - mockForm.selected_question_ids.length} more questions)
                          </span>
                        )}
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleOpenAddQuestionModal()}
                          style={{ fontSize: '11.5px', padding: '4px 10px', gap: '4px' }}
                        >
                          <Plus size={13} />
                          <span>Add Question</span>
                        </button>
                        {mockForm.selected_question_ids.length > 0 && (
                          <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={() => setMockForm(prev => ({ ...prev, selected_question_ids: [] }))}
                            style={{ fontSize: '11.5px', padding: '4px 10px', color: 'var(--text-muted)' }}
                          >
                            Clear All ({mockForm.selected_question_ids.length})
                          </button>
                        )}
                      </div>
                    </div>

                    {/* Preview of Prepared Questions with Remove Buttons */}
                    {mockForm.selected_question_ids.length === 0 ? (
                      <div style={{ padding: '16px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '12.5px' }}>
                        No questions prepared yet. Click one of the <strong>⚡ 1-Click Fast Presets</strong> above to instantly load 50 questions, or select from the Question Bank.
                      </div>
                    ) : (
                      <div style={{
                        maxHeight: '180px',
                        overflowY: 'auto',
                        background: '#070d18',
                        borderRadius: '6px',
                        padding: '6px',
                        border: '1px solid rgba(255, 255, 255, 0.05)'
                      }}>
                        {mockForm.selected_question_ids.map((qid, idx) => {
                          const qData = questionBank.find(q => q.id === qid);
                          return (
                            <div
                              key={`${qid}-${idx}`}
                              style={{
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'space-between',
                                gap: '10px',
                                padding: '6px 10px',
                                borderRadius: '4px',
                                background: 'rgba(255, 255, 255, 0.02)',
                                borderBottom: '1px solid rgba(255, 255, 255, 0.03)',
                                fontSize: '12px'
                              }}
                            >
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', minWidth: 0, flex: 1 }}>
                                <span style={{
                                  width: '20px',
                                  height: '20px',
                                  borderRadius: '50%',
                                  background: 'rgba(6, 182, 212, 0.15)',
                                  color: 'var(--cyan)',
                                  display: 'flex',
                                  alignItems: 'center',
                                  justifyContent: 'center',
                                  fontSize: '10.5px',
                                  fontWeight: 700,
                                  flexShrink: 0
                                }}>
                                  {idx + 1}
                                </span>
                                {qData?.subject && (
                                  <span className="badge badge-primary" style={{ fontSize: '10px', padding: '1px 6px', flexShrink: 0 }}>
                                    {qData.subject}
                                  </span>
                                )}
                                <span style={{ color: '#fff', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                  {qData?.question || `Verified Bank Question #${qid}`}
                                </span>
                              </div>

                              <button
                                type="button"
                                onClick={() => {
                                  setMockForm(prev => ({
                                    ...prev,
                                    selected_question_ids: prev.selected_question_ids.filter((_, i) => i !== idx)
                                  }));
                                }}
                                style={{
                                  background: 'none',
                                  border: 'none',
                                  color: 'var(--rose)',
                                  cursor: 'pointer',
                                  padding: '2px 6px',
                                  fontSize: '11px',
                                  borderRadius: '4px',
                                  flexShrink: 0
                                }}
                                title="Remove from this mock exam"
                              >
                                ✕ Remove
                              </button>
                            </div>
                          );
                        })}
                      </div>
                    )}
                  </div>
                </div>
              </form>
            </div>

            {/* Modal Footer */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '16px 24px',
              borderTop: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <div style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>
                {mockForm.creation_mode === 'auto' ? (
                  <span>Auto-generates verified 50+ question mock from real competitive bank.</span>
                ) : (
                  <span>Selected: <strong style={{ color: mockForm.selected_question_ids.length >= 50 ? 'var(--emerald)' : 'var(--amber)' }}>{mockForm.selected_question_ids.length} questions</strong> (Min 50)</span>
                )}
              </div>

              <div style={{ display: 'flex', gap: '10px' }}>
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowCreateMockModal(false)}
                  disabled={mockSaving}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  form="mockExamForm"
                  className="btn btn-primary"
                  disabled={mockSaving}
                  style={{ gap: '6px' }}
                >
                  {mockSaving ? (
                    <span>Saving Mock Exam...</span>
                  ) : (
                    <>
                      <Check size={16} />
                      <span>{editingMockExam ? 'Save Changes' : 'Create 50-Question Mock Exam'}</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ==========================================
          MODAL: PREVIEW 50-QUESTION MOCK EXAM
          ========================================== */}
      {previewingMockExam && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0, 0, 0, 0.8)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000,
          padding: '20px'
        }}>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-lg)',
            width: '100%',
            maxWidth: '960px',
            maxHeight: '90vh',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)'
          }}>
            {/* Header */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '18px 24px',
              borderBottom: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                  <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 700, color: '#fff' }}>
                    {previewingMockExam.title}
                  </h3>
                  <span className="badge badge-cyan" style={{ fontSize: '11px' }}>
                    {(previewingMockExam.questions || []).length || previewingMockExam.total_questions || 50} Questions (Min 50 ✓)
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '12px', color: 'var(--text-muted)' }}>
                  <span>Category: <strong style={{ color: '#fff' }}>{previewingMockExam.category}</strong></span>
                  <span>•</span>
                  <span>Target: <strong style={{ color: '#fff' }}>{previewingMockExam.target_exam || 'General'}</strong></span>
                  <span>•</span>
                  <span>Duration: <strong style={{ color: '#fff' }}>{previewingMockExam.duration_minutes || 60} mins</strong></span>
                  <span>•</span>
                  <span>Marks: <strong style={{ color: '#fff' }}>{previewingMockExam.total_marks || 100}</strong></span>
                  <span>•</span>
                  <span>Negative: <strong style={{ color: 'var(--amber)' }}>-{previewingMockExam.negative_marking || 0.25}</strong></span>
                </div>
              </div>
              <button
                className="btn btn-secondary"
                onClick={() => setPreviewingMockExam(null)}
                style={{ padding: '6px 12px', fontSize: '13px' }}
              >
                ✕ Close
              </button>
            </div>

            {/* Questions List */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '24px' }}>
              {(!previewingMockExam.questions || previewingMockExam.questions.length === 0) ? (
                <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-muted)' }}>
                  Loading all 50 questions for this mock exam...
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
                  {previewingMockExam.questions.map((q, idx) => (
                    <div
                      key={q.id || idx}
                      style={{
                        padding: '16px 20px',
                        borderRadius: 'var(--radius-md)',
                        background: 'rgba(255, 255, 255, 0.02)',
                        border: '1px solid var(--border-subtle)'
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{
                            width: '26px',
                            height: '26px',
                            borderRadius: '50%',
                            background: 'rgba(99, 102, 241, 0.15)',
                            color: 'var(--cyan)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            fontSize: '12px',
                            fontWeight: 700
                          }}>
                            {idx + 1}
                          </span>
                          <span className="badge badge-primary" style={{ fontSize: '10.5px', padding: '2px 8px' }}>
                            {q.subject || 'General'}
                          </span>
                          {q.topic && (
                            <span style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
                              {q.topic}
                            </span>
                          )}
                        </div>
                        <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                          2 Marks • -{previewingMockExam.negative_marking || 0.25} Negative
                        </span>
                      </div>

                      <h5 style={{ fontSize: '14.5px', fontWeight: 600, color: '#fff', margin: '0 0 12px', lineHeight: 1.45 }}>
                        {q.question}
                      </h5>

                      {/* Options */}
                      {Array.isArray(q.options) && q.options.length > 0 ? (
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '8px', marginBottom: '8px' }}>
                          {q.options.map((opt, oIdx) => {
                            const isCorrect = opt === q.correct_answer || (q.correct_answer && String(opt).startsWith(q.correct_answer));
                            return (
                              <div
                                key={oIdx}
                                style={{
                                  padding: '8px 12px',
                                  borderRadius: '6px',
                                  background: isCorrect ? 'rgba(16, 185, 129, 0.12)' : 'rgba(255, 255, 255, 0.02)',
                                  border: `1px solid ${isCorrect ? 'rgba(16, 185, 129, 0.4)' : 'rgba(255, 255, 255, 0.05)'}`,
                                  color: isCorrect ? 'var(--emerald)' : 'var(--text-secondary)',
                                  fontSize: '13px',
                                  display: 'flex',
                                  alignItems: 'center',
                                  gap: '8px'
                                }}
                              >
                                <span style={{ fontWeight: 600, width: '16px' }}>{String.fromCharCode(65 + oIdx)}.</span>
                                <span>{opt}</span>
                                {isCorrect && <Check size={14} style={{ marginLeft: 'auto' }} />}
                              </div>
                            );
                          })}
                        </div>
                      ) : (
                        <div style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '8px' }}>
                          Fill-in-the-blank / Direct answer format. Correct Answer: <strong style={{ color: 'var(--emerald)' }}>{q.correct_answer}</strong>
                        </div>
                      )}

                      {q.explanation && (
                        <div style={{
                          marginTop: '8px',
                          padding: '8px 12px',
                          borderRadius: '6px',
                          background: 'rgba(6, 182, 212, 0.06)',
                          border: '1px solid rgba(6, 182, 212, 0.15)',
                          fontSize: '12px',
                          color: 'var(--text-secondary)'
                        }}>
                          <strong style={{ color: 'var(--cyan)' }}>Explanation: </strong>
                          {q.explanation}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Footer */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '14px 24px',
              borderTop: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>
                Viewing all {(previewingMockExam.questions || []).length} questions of {previewingMockExam.title}
              </span>
              <button
                className="btn btn-secondary"
                onClick={() => setPreviewingMockExam(null)}
                style={{ padding: '6px 14px', fontSize: '13px' }}
              >
                Close Preview
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ==========================================
          MODAL: ADD / AUTHOR NEW QUESTION
          ========================================== */}
      {showAddQuestionModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1100,
          padding: '20px'
        }}>
          <div style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-lg)',
            width: '100%',
            maxWidth: '720px',
            maxHeight: '92vh',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)'
          }}>
            {/* Header */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '18px 24px',
              borderBottom: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div style={{
                  width: '36px',
                  height: '36px',
                  borderRadius: '8px',
                  background: 'rgba(6, 182, 212, 0.15)',
                  color: 'var(--cyan)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  <Plus size={20} />
                </div>
                <div>
                  <h3 style={{ margin: 0, fontSize: '17px', fontWeight: 700, color: '#fff' }}>
                    ✍️ Prepare & Author Question
                  </h3>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                    Add questions to the verified database question bank & current mock exam
                  </div>
                </div>
              </div>

              <button
                type="button"
                className="btn-icon"
                onClick={() => setShowAddQuestionModal(false)}
                disabled={questionSaving}
                style={{ width: '32px', height: '32px' }}
              >
                ✕
              </button>
            </div>

            {/* Form */}
            <div style={{ padding: '24px', overflowY: 'auto', flex: 1 }}>
              <form id="addQuestionForm" onSubmit={handleSaveNewQuestion} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                {questionFormError && (
                  <div style={{
                    padding: '10px 14px',
                    borderRadius: 'var(--radius-sm)',
                    background: 'rgba(244, 63, 94, 0.12)',
                    border: '1px solid rgba(244, 63, 94, 0.3)',
                    color: 'var(--rose)',
                    fontSize: '13px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px'
                  }}>
                    <AlertCircle size={16} />
                    <span>{questionFormError}</span>
                  </div>
                )}

                {/* Subject & Topic */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Subject / Section *
                    </label>
                    <select
                      value={questionForm.subject}
                      onChange={e => setQuestionForm({ ...questionForm, subject: e.target.value })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-subtle)',
                        background: 'var(--bg-dark)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                      required
                    >
                      <option value="Quantitative Aptitude">Quantitative Aptitude / Math</option>
                      <option value="Reasoning Ability">Reasoning Ability & Logic</option>
                      <option value="English Language">English Language & Comprehension</option>
                      <option value="General Awareness">General Awareness / GK</option>
                      <option value="General Science">General Science</option>
                      <option value="Computer Knowledge">Computer Knowledge</option>
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Topic / Concept
                    </label>
                    <input
                      type="text"
                      value={questionForm.topic}
                      onChange={e => setQuestionForm({ ...questionForm, topic: e.target.value })}
                      placeholder="e.g. Percentages, Syllogisms, Cloze Test, Constitution"
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-subtle)',
                        background: 'var(--bg-dark)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>
                </div>

                {/* Question Type & Marks */}
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 120px', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Question Format
                    </label>
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <button
                        type="button"
                        className={`btn ${questionForm.question_type === 'MCQ' ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setQuestionForm({ ...questionForm, question_type: 'MCQ' })}
                        style={{ padding: '6px 14px', fontSize: '12.5px' }}
                      >
                        Multiple Choice (4 Options)
                      </button>
                      <button
                        type="button"
                        className={`btn ${questionForm.question_type === 'FILL_IN_THE_BLANK' ? 'btn-primary' : 'btn-secondary'}`}
                        onClick={() => setQuestionForm({ ...questionForm, question_type: 'FILL_IN_THE_BLANK' })}
                        style={{ padding: '6px 14px', fontSize: '12.5px' }}
                      >
                        Direct / Fill in the blank
                      </button>
                    </div>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                      Marks / Points
                    </label>
                    <input
                      type="number"
                      min="1"
                      max="10"
                      value={questionForm.points}
                      onChange={e => setQuestionForm({ ...questionForm, points: parseInt(e.target.value, 10) || 2 })}
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-subtle)',
                        background: 'var(--bg-dark)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                    />
                  </div>
                </div>

                {/* Question Prompt */}
                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                    Question Statement / Prompt *
                  </label>
                  <textarea
                    rows={3}
                    value={questionForm.question}
                    onChange={e => setQuestionForm({ ...questionForm, question: e.target.value })}
                    placeholder="Enter the full question text here (e.g. Which constitutional amendment introduced GST in India?)..."
                    style={{
                      width: '100%',
                      padding: '10px 12px',
                      borderRadius: 'var(--radius-sm)',
                      border: '1px solid var(--border-subtle)',
                      background: 'var(--bg-dark)',
                      color: '#fff',
                      fontSize: '13.5px',
                      lineHeight: 1.5
                    }}
                    required
                  />
                </div>

                {/* MCQ Options A, B, C, D */}
                {questionForm.question_type === 'MCQ' ? (
                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '8px' }}>
                      Options (Select the correct option via radio button):
                    </label>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      {[
                        { key: 'option_a', label: 'A', value: questionForm.option_a },
                        { key: 'option_b', label: 'B', value: questionForm.option_b },
                        { key: 'option_c', label: 'C', value: questionForm.option_c },
                        { key: 'option_d', label: 'D', value: questionForm.option_d }
                      ].map(opt => (
                        <div
                          key={opt.key}
                          style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: '10px',
                            background: questionForm.correct_answer === opt.label ? 'rgba(16, 185, 129, 0.08)' : 'rgba(255, 255, 255, 0.02)',
                            padding: '8px 12px',
                            borderRadius: '6px',
                            border: `1px solid ${questionForm.correct_answer === opt.label ? 'rgba(16, 185, 129, 0.4)' : 'var(--border-subtle)'}`
                          }}
                        >
                          <label style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', margin: 0, fontWeight: 700, fontSize: '13px', color: questionForm.correct_answer === opt.label ? 'var(--emerald)' : 'var(--text-secondary)' }}>
                            <input
                              type="radio"
                              name="mcqCorrectAnswer"
                              value={opt.label}
                              checked={questionForm.correct_answer === opt.label}
                              onChange={() => setQuestionForm({ ...questionForm, correct_answer: opt.label })}
                              style={{ cursor: 'pointer' }}
                            />
                            <span>Option {opt.label}:</span>
                          </label>
                          <input
                            type="text"
                            value={opt.value}
                            onChange={e => setQuestionForm({ ...questionForm, [opt.key]: e.target.value })}
                            placeholder={`Enter text for Option ${opt.label}...`}
                            style={{
                              flex: 1,
                              padding: '6px 10px',
                              background: 'var(--bg-dark)',
                              border: '1px solid var(--border-subtle)',
                              borderRadius: '4px',
                              color: '#fff',
                              fontSize: '13px'
                            }}
                          />
                        </div>
                      ))}
                    </div>
                  </div>
                ) : (
                  <div>
                    <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--emerald)', fontWeight: 600, marginBottom: '6px' }}>
                      Exact Correct Answer *
                    </label>
                    <input
                      type="text"
                      value={questionForm.correct_answer}
                      onChange={e => setQuestionForm({ ...questionForm, correct_answer: e.target.value })}
                      placeholder="Enter the exact answer string or number..."
                      style={{
                        width: '100%',
                        padding: '9px 12px',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-emerald-glow)',
                        background: 'var(--bg-dark)',
                        color: '#fff',
                        fontSize: '13.5px'
                      }}
                      required
                    />
                  </div>
                )}

                {/* Explanation */}
                <div>
                  <label style={{ display: 'block', fontSize: '12.5px', color: 'var(--text-secondary)', marginBottom: '6px' }}>
                    Explanation / Solution Notes (Shown during student result review)
                  </label>
                  <textarea
                    rows={2}
                    value={questionForm.explanation}
                    onChange={e => setQuestionForm({ ...questionForm, explanation: e.target.value })}
                    placeholder="Explain the step-by-step formula or rule behind the correct answer..."
                    style={{
                      width: '100%',
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      border: '1px solid var(--border-subtle)',
                      background: 'var(--bg-dark)',
                      color: '#fff',
                      fontSize: '13px'
                    }}
                  />
                </div>

                {/* Checkbox: Attach to current mock */}
                {(showCreateMockModal || !!editingMockExam) && (
                  <div style={{
                    padding: '10px 14px',
                    borderRadius: '6px',
                    background: 'rgba(99, 102, 241, 0.08)',
                    border: '1px solid rgba(99, 102, 241, 0.2)'
                  }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', margin: 0, fontSize: '13px', color: '#fff' }}>
                      <input
                        type="checkbox"
                        checked={questionForm.attach_to_current_mock}
                        onChange={e => setQuestionForm({ ...questionForm, attach_to_current_mock: e.target.checked })}
                        style={{ cursor: 'pointer' }}
                      />
                      <span>
                        <strong>Include immediately in this Mock Exam</strong> (Adds directly into the 50-question set)
                      </span>
                    </label>
                  </div>
                )}
              </form>
            </div>

            {/* Modal Footer */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'flex-end',
              gap: '10px',
              padding: '16px 24px',
              borderTop: '1px solid var(--border-subtle)',
              background: 'rgba(255, 255, 255, 0.02)'
            }}>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => setShowAddQuestionModal(false)}
                disabled={questionSaving}
              >
                Cancel
              </button>
              <button
                type="submit"
                form="addQuestionForm"
                className="btn btn-primary"
                disabled={questionSaving}
                style={{ gap: '6px' }}
              >
                {questionSaving ? (
                  <span>Saving Question...</span>
                ) : (
                  <>
                    <Check size={16} />
                    <span>Save & Add Question</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

