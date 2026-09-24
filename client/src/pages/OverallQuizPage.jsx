import React, { useState, useEffect } from 'react';
import { 
  Award, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  ArrowLeft, 
  ArrowRight, 
  RotateCcw, 
  Sparkles, 
  Check, 
  BookOpen,
  Layers,
  HelpCircle,
  Target,
  Bookmark,
  AlertTriangle,
  ChevronRight,
  Filter
} from 'lucide-react';

export default function OverallQuizPage({ navigateTo }) {
  // Mock exams listing state
  const [mockExams, setMockExams] = useState([]);
  const [loadingExams, setLoadingExams] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('All');

  // Active exam session state
  const [activeExam, setActiveExam] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [loadingQuestions, setLoadingQuestions] = useState(false);
  const [quizStarted, setQuizStarted] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({}); // { [qid]: optionValue }
  const [markedForReview, setMarkedForReview] = useState(new Set());
  const [activeSubjectFilter, setActiveSubjectFilter] = useState('All');
  
  // Timer (counts DOWN from duration in minutes, e.g. 60 mins = 3600 seconds)
  const [timeRemaining, setTimeRemaining] = useState(3600);
  const [timerActive, setTimerActive] = useState(false);
  
  // Submission & Results
  const [submitting, setSubmitting] = useState(false);
  const [quizResult, setQuizResult] = useState(null);
  const [showSubmitConfirm, setShowSubmitConfirm] = useState(false);

  useEffect(() => {
    fetchMockExams();
  }, []);

  // Timer countdown
  useEffect(() => {
    let interval = null;
    if (timerActive) {
      interval = setInterval(() => {
        setTimeRemaining(prev => {
          if (prev <= 1) {
            clearInterval(interval);
            handleAutoSubmit();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [timerActive]);

  const fetchMockExams = async () => {
    try {
      setLoadingExams(true);
      const res = await fetch('http://localhost:3001/api/mock-exams');
      if (res.ok) {
        const json = await res.json();
        setMockExams(json.data || []);
      }
    } catch (err) {
      console.error('Error fetching mock exams:', err);
    } finally {
      setLoadingExams(false);
    }
  };

  const handleStartExam = async (exam) => {
    try {
      setLoadingQuestions(true);
      const res = await fetch(`http://localhost:3001/api/mock-exams/${exam.id}`);
      if (!res.ok) throw new Error('Failed to load mock exam questions');
      const json = await res.json();
      
      const loadedQuestions = json.data?.questions || [];
      setActiveExam(json.data || exam);
      setQuestions(loadedQuestions);
      setCurrentIndex(0);
      setUserAnswers({});
      setMarkedForReview(new Set());
      setQuizResult(null);
      setActiveSubjectFilter('All');
      
      const durationSecs = (json.data?.duration_minutes || exam.duration_minutes || 60) * 60;
      setTimeRemaining(durationSecs);
      setQuizStarted(true);
      setTimerActive(true);
    } catch (err) {
      console.error('Error starting mock exam:', err);
      alert('Could not start mock exam: ' + err.message);
    } finally {
      setLoadingQuestions(false);
    }
  };

  const handleSelectOption = (questionId, value) => {
    setUserAnswers(prev => ({
      ...prev,
      [questionId]: value
    }));
  };

  const handleClearAnswer = (questionId) => {
    setUserAnswers(prev => {
      const copy = { ...prev };
      delete copy[questionId];
      return copy;
    });
  };

  const handleToggleReview = (questionId) => {
    setMarkedForReview(prev => {
      const next = new Set(prev);
      if (next.has(questionId)) {
        next.delete(questionId);
      } else {
        next.add(questionId);
      }
      return next;
    });
  };

  const handleAutoSubmit = () => {
    alert('Time has expired! Automatically submitting your mock examination.');
    handleSubmitExam();
  };

  const handleSubmitExam = async () => {
    if (!activeExam) return;
    setShowSubmitConfirm(false);
    setTimerActive(false);
    setSubmitting(true);

    try {
      const durationTotalSecs = (activeExam.duration_minutes || 60) * 60;
      const timeSpent = Math.max(0, durationTotalSecs - timeRemaining);

      const res = await fetch(`http://localhost:3001/api/mock-exams/${activeExam.id}/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          answers: userAnswers,
          timeSpentSeconds: timeSpent
        })
      });

      const result = await res.json();
      if (!res.ok) {
        throw new Error(result.error || 'Failed to evaluate mock exam');
      }

      setQuizResult(result);
      setQuizStarted(false);
    } catch (err) {
      console.error('Error submitting mock exam:', err);
      alert('Error submitting mock exam: ' + err.message);
    } finally {
      setSubmitting(false);
    }
  };

  const formatTimer = (secs) => {
    const hours = Math.floor(secs / 3600);
    const mins = Math.floor((secs % 3600) / 60);
    const rem = secs % 60;
    if (hours > 0) {
      return `${hours}:${mins < 10 ? '0' : ''}${mins}:${rem < 10 ? '0' : ''}${rem}`;
    }
    return `${mins < 10 ? '0' : ''}${mins}:${rem < 10 ? '0' : ''}${rem}`;
  };

  // Distinct subjects in the active 50 questions
  const availableSubjects = ['All', ...new Set(questions.map(q => q.subject).filter(Boolean))];

  // Filtered question indices according to subject tab
  const filteredQuestionIndices = questions
    .map((q, idx) => ({ ...q, originalIndex: idx }))
    .filter(q => activeSubjectFilter === 'All' || q.subject === activeSubjectFilter);

  // Stats for confirmation
  const answeredCount = Object.keys(userAnswers).length;
  const unattemptedCount = Math.max(0, questions.length - answeredCount);

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', paddingBottom: '60px' }}>
      {/* Top Breadcrumb & Back */}
      <div style={{ marginBottom: '24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '14px' }}>
        <button 
          className="btn btn-secondary" 
          onClick={() => {
            if (quizStarted && !window.confirm('Leave mock exam? Your current progress will be lost.')) return;
            setQuizStarted(false);
            setQuizResult(null);
            navigateTo('home');
          }}
          style={{ fontSize: '13px', padding: '6px 14px', gap: '6px' }}
        >
          <ArrowLeft size={14} />
          <span>Back to Home</span>
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-cyan" style={{ fontSize: '12px', padding: '4px 10px' }}>
            <Target size={13} style={{ marginRight: '4px' }} />
            Tier-1 Standard • Minimum 50 Questions Mandatory
          </span>
        </div>
      </div>

      {/* ==========================================
          STATE 1: BROWSE AVAILABLE MOCK EXAMS (50 QUESTIONS)
          ========================================== */}
      {!quizStarted && !quizResult && (
        <div>
          {/* Hero Banner */}
          <div className="glass-card" style={{
            padding: '32px 36px',
            marginBottom: '32px',
            background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%)',
            border: '1px solid rgba(6, 182, 212, 0.25)',
            position: 'relative',
            overflow: 'hidden'
          }}>
            <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '24px', flexWrap: 'wrap' }}>
              <div style={{ maxWidth: '720px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                  <span className="badge badge-primary">
                    <Sparkles size={13} />
                    Official Competitive Simulation
                  </span>
                  <span className="badge badge-emerald">
                    50 Questions Minimum
                  </span>
                </div>
                <h1 style={{ fontSize: '32px', fontWeight: 800, color: '#fff', margin: '0 0 10px', letterSpacing: '-0.5px' }}>
                  Competitive Full-Length Mock Exams
                </h1>
                <p style={{ color: 'var(--text-secondary)', fontSize: '15px', lineHeight: 1.6, margin: 0 }}>
                  Practice real-time speed examinations designed by educators and administrators. Every mock test is strictly built with at least 50 verified questions, 60-minute countdown timers, and standard competitive negative marking.
                </p>
              </div>

              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(2, 1fr)',
                gap: '12px',
                background: 'rgba(0, 0, 0, 0.3)',
                padding: '16px 20px',
                borderRadius: 'var(--radius-md)',
                border: '1px solid rgba(255, 255, 255, 0.05)',
                minWidth: '240px'
              }}>
                <div>
                  <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--cyan)' }}>50 Qs</div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>Min Questions / Mock</div>
                </div>
                <div>
                  <div style={{ fontSize: '22px', fontWeight: 800, color: '#fff' }}>60 Mins</div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>Standard Timer</div>
                </div>
                <div>
                  <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--amber)' }}>-0.25</div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>Negative Marking</div>
                </div>
                <div>
                  <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--emerald)' }}>70%</div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>Pass Benchmark</div>
                </div>
              </div>
            </div>
          </div>

          {/* Category Filter Pills */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '24px', overflowX: 'auto', paddingBottom: '6px' }}>
            <span style={{ fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginRight: '4px' }}>
              Category:
            </span>
            {['All', 'SSC', 'Central Government', 'Railway', 'Banking', 'Defence', 'KPSC'].map(cat => (
              <button
                key={cat}
                className={`btn ${selectedCategory === cat ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setSelectedCategory(cat)}
                style={{ fontSize: '12.5px', padding: '6px 14px', borderRadius: '20px' }}
              >
                {cat}
              </button>
            ))}
          </div>

          {/* Mock Exams List */}
          {loadingExams ? (
            <div style={{ textAlign: 'center', padding: '60px', color: 'var(--text-muted)' }}>
              Loading available 50-question mock exams...
            </div>
          ) : mockExams.length === 0 ? (
            <div className="glass-card" style={{ textAlign: 'center', padding: '60px 20px' }}>
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
                <Target size={30} />
              </div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>
                No Published Mock Exams
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '420px', margin: '0 auto 20px' }}>
                Admin has not published any mock exams yet. Administrators can create full 50-question mock tests in the Admin Panel.
              </p>
            </div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))', gap: '20px' }}>
              {mockExams
                .filter(e => selectedCategory === 'All' || (e.category || '').toLowerCase().includes(selectedCategory.toLowerCase()))
                .map(exam => (
                  <div
                    key={exam.id}
                    className="card"
                    style={{
                      padding: '24px',
                      borderRadius: 'var(--radius-lg)',
                      background: 'var(--bg-card)',
                      border: '1px solid var(--border-subtle)',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between',
                      transition: 'all 0.2s ease',
                      boxShadow: '0 8px 24px rgba(0, 0, 0, 0.2)'
                    }}
                  >
                    <div>
                      {/* Category & Status */}
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '10px', marginBottom: '12px' }}>
                        <span className="badge badge-primary" style={{ fontSize: '11px', padding: '3px 8px' }}>
                          {exam.category || 'General'}
                        </span>
                        <span className="badge badge-cyan" style={{ fontSize: '11.5px', padding: '3px 9px', fontWeight: 700 }}>
                          {(exam.question_ids || []).length || exam.total_questions || 50} Questions (Min 50 ✓)
                        </span>
                      </div>

                      <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', margin: '0 0 8px', lineHeight: 1.4 }}>
                        {exam.title}
                      </h3>

                      {exam.target_exam && (
                        <div style={{ fontSize: '12.5px', color: 'var(--cyan)', fontWeight: 600, marginBottom: '10px' }}>
                          Target: {exam.target_exam}
                        </div>
                      )}

                      <p style={{ fontSize: '13px', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: '20px' }}>
                        {exam.description || 'Full-length 50-question comprehensive mock exam covering core competitive domains.'}
                      </p>
                    </div>

                    <div>
                      {/* Exam Specs Strip */}
                      <div style={{
                        display: 'grid',
                        gridTemplateColumns: 'repeat(3, 1fr)',
                        gap: '8px',
                        padding: '12px',
                        background: 'rgba(255, 255, 255, 0.02)',
                        borderRadius: 'var(--radius-sm)',
                        border: '1px solid var(--border-subtle)',
                        textAlign: 'center',
                        marginBottom: '16px'
                      }}>
                        <div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Duration</div>
                          <div style={{ fontSize: '13.5px', fontWeight: 700, color: '#fff' }}>
                            {exam.duration_minutes || 60}m
                          </div>
                        </div>
                        <div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Marks</div>
                          <div style={{ fontSize: '13.5px', fontWeight: 700, color: '#fff' }}>
                            {exam.total_marks || ((exam.question_ids || []).length * 2) || 100}
                          </div>
                        </div>
                        <div>
                          <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Negative</div>
                          <div style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--amber)' }}>
                            -{exam.negative_marking !== undefined ? exam.negative_marking : 0.25}
                          </div>
                        </div>
                      </div>

                      {/* Start Button */}
                      <button
                        className="btn btn-primary"
                        onClick={() => handleStartExam(exam)}
                        disabled={loadingQuestions}
                        style={{ width: '100%', justifyContent: 'center', padding: '10px 16px', gap: '8px', fontSize: '14px', fontWeight: 600 }}
                      >
                        <Target size={16} />
                        <span>Start 50-Question Mock Exam</span>
                        <ChevronRight size={16} />
                      </button>
                    </div>
                  </div>
                ))}
            </div>
          )}
        </div>
      )}

      {/* ==========================================
          STATE 2: ACTIVE 50-QUESTION TEST IN PROGRESS
          ========================================== */}
      {quizStarted && !quizResult && questions.length > 0 && (
        <div>
          {/* Active Test Sticky Header */}
          <div style={{
            position: 'sticky',
            top: '16px',
            zIndex: 100,
            background: 'rgba(15, 23, 42, 0.95)',
            backdropFilter: 'blur(12px)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-md)',
            padding: '14px 20px',
            marginBottom: '20px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '16px',
            flexWrap: 'wrap',
            boxShadow: '0 10px 30px rgba(0, 0, 0, 0.4)'
          }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 700, color: '#fff' }}>
                  {activeExam?.title}
                </h3>
                <span className="badge badge-cyan" style={{ fontSize: '11px' }}>
                  {questions.length} Questions
                </span>
              </div>
              <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px' }}>
                Question <strong>{currentIndex + 1}</strong> of {questions.length} • Subject: <span style={{ color: 'var(--cyan)' }}>{questions[currentIndex]?.subject || 'General'}</span>
              </div>
            </div>

            {/* Timer Display */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                padding: '8px 16px',
                borderRadius: '8px',
                background: timeRemaining < 300 ? 'rgba(239, 68, 68, 0.15)' : 'rgba(6, 182, 212, 0.12)',
                border: `1px solid ${timeRemaining < 300 ? 'rgba(239, 68, 68, 0.4)' : 'rgba(6, 182, 212, 0.3)'}`,
                color: timeRemaining < 300 ? 'var(--rose)' : 'var(--cyan)',
                fontWeight: 800,
                fontSize: '16px',
                letterSpacing: '0.5px'
              }}>
                <Clock size={18} />
                <span>{formatTimer(timeRemaining)}</span>
              </div>

              <button
                className="btn btn-emerald"
                onClick={() => setShowSubmitConfirm(true)}
                style={{ padding: '8px 18px', fontSize: '13px', fontWeight: 600, gap: '6px' }}
              >
                <Check size={16} />
                <span>Finish & Submit</span>
              </button>
            </div>
          </div>

          {/* Test Layout Grid: Left Question, Right 50-Question Palette */}
          <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 300px', gap: '20px', alignItems: 'start' }}>
            {/* Left: Active Question Card */}
            <div>
              {/* Subject Tabs */}
              <div style={{ display: 'flex', gap: '6px', marginBottom: '14px', overflowX: 'auto', paddingBottom: '4px' }}>
                {availableSubjects.map(subj => (
                  <button
                    key={subj}
                    className={`btn ${activeSubjectFilter === subj ? 'btn-primary' : 'btn-secondary'}`}
                    onClick={() => setActiveSubjectFilter(subj)}
                    style={{ fontSize: '11.5px', padding: '5px 12px', borderRadius: '14px', whiteSpace: 'nowrap' }}
                  >
                    {subj}
                  </button>
                ))}
              </div>

              {(() => {
                const currentQ = questions[currentIndex];
                const selected = userAnswers[currentQ.id];
                const isMarked = markedForReview.has(currentQ.id);
                const isFillInTheBlank = currentQ.question_type === 'FILL_IN_THE_BLANK' || 
                  (!currentQ.options || currentQ.options.length === 0) || 
                  currentQ.question?.includes('____');

                return (
                  <div className="glass-card" style={{ padding: '28px', background: 'var(--bg-card)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-lg)' }}>
                    {/* Question Header */}
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px', flexWrap: 'wrap', gap: '10px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span style={{
                          width: '30px',
                          height: '30px',
                          borderRadius: '50%',
                          background: 'rgba(6, 182, 212, 0.15)',
                          color: 'var(--cyan)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '13px',
                          fontWeight: 700
                        }}>
                          {currentIndex + 1}
                        </span>
                        <span className="badge badge-primary" style={{ fontSize: '11px' }}>
                          {currentQ.subject || 'General'}
                        </span>
                        {currentQ.topic && (
                          <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                            {currentQ.topic}
                          </span>
                        )}
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '12px', color: 'var(--text-muted)' }}>
                        <span>+2.0 Marks</span>
                        <span>•</span>
                        <span style={{ color: 'var(--amber)' }}>-{activeExam?.negative_marking || 0.25} Negative</span>
                      </div>
                    </div>

                    {/* Question Prompt */}
                    <div style={{ fontSize: '17px', fontWeight: 600, color: '#fff', lineHeight: 1.6, marginBottom: '24px' }}>
                      {currentQ.question}
                    </div>

                    {/* Options */}
                    {isFillInTheBlank ? (
                      <div style={{ margin: '20px 0 28px' }}>
                        <label 
                          style={{ display: 'block', fontSize: '13.5px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '8px' }}
                        >
                          Enter your answer:
                        </label>
                        <div style={{ maxWidth: '440px' }}>
                          <input
                            type="text"
                            placeholder="Type answer here..."
                            value={selected || ''}
                            onChange={(e) => handleSelectOption(currentQ.id, e.target.value)}
                            style={{
                              width: '100%',
                              padding: '12px 16px',
                              fontSize: '15px',
                              background: 'rgba(15, 23, 42, 0.7)',
                              border: selected ? '1px solid var(--primary)' : '1px solid rgba(255, 255, 255, 0.2)',
                              borderRadius: 'var(--radius-md)',
                              color: '#ffffff',
                              outline: 'none'
                            }}
                          />
                        </div>
                      </div>
                    ) : (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '24px' }}>
                        {currentQ.options?.map((opt, oIdx) => {
                          const letters = ['A', 'B', 'C', 'D'];
                          const isSelected = selected === opt;
                          return (
                            <button
                              key={oIdx}
                              onClick={() => handleSelectOption(currentQ.id, opt)}
                              style={{
                                display: 'flex',
                                alignItems: 'center',
                                gap: '12px',
                                padding: '12px 18px',
                                borderRadius: 'var(--radius-md)',
                                background: isSelected ? 'rgba(99, 102, 241, 0.16)' : 'rgba(255, 255, 255, 0.02)',
                                border: `1px solid ${isSelected ? 'var(--primary)' : 'var(--border-subtle)'}`,
                                color: isSelected ? '#fff' : 'var(--text-secondary)',
                                textAlign: 'left',
                                fontSize: '14px',
                                cursor: 'pointer',
                                transition: 'all 0.15s ease'
                              }}
                            >
                              <span style={{
                                width: '24px',
                                height: '24px',
                                borderRadius: '50%',
                                background: isSelected ? 'var(--primary)' : 'rgba(255, 255, 255, 0.06)',
                                color: isSelected ? '#fff' : 'var(--text-muted)',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                fontSize: '12px',
                                fontWeight: 700,
                                flexShrink: 0
                              }}>
                                {letters[oIdx]}
                              </span>
                              <span style={{ flex: 1 }}>{opt}</span>
                              {isSelected && <Check size={16} color="var(--cyan)" />}
                            </button>
                          );
                        })}
                      </div>
                    )}

                    {/* Navigation and Review Bar */}
                    <div style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      paddingTop: '20px',
                      borderTop: '1px solid var(--border-subtle)',
                      flexWrap: 'wrap',
                      gap: '12px'
                    }}>
                      <div style={{ display: 'flex', gap: '8px' }}>
                        <button
                          type="button"
                          className="btn btn-secondary"
                          onClick={() => handleToggleReview(currentQ.id)}
                          style={{
                            fontSize: '12.5px',
                            padding: '7px 14px',
                            gap: '6px',
                            color: isMarked ? '#c084fc' : 'var(--text-secondary)',
                            background: isMarked ? 'rgba(192, 132, 252, 0.12)' : undefined,
                            border: isMarked ? '1px solid rgba(192, 132, 252, 0.3)' : undefined
                          }}
                        >
                          <Bookmark size={14} />
                          <span>{isMarked ? 'Marked for Review' : 'Mark for Review'}</span>
                        </button>

                        {selected && (
                          <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={() => handleClearAnswer(currentQ.id)}
                            style={{ fontSize: '12.5px', padding: '7px 12px', color: 'var(--text-muted)' }}
                          >
                            Clear Answer
                          </button>
                        )}
                      </div>

                      <div style={{ display: 'flex', gap: '8px' }}>
                        <button
                          className="btn btn-secondary"
                          onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
                          disabled={currentIndex === 0}
                          style={{ fontSize: '13px', padding: '7px 14px', opacity: currentIndex === 0 ? 0.4 : 1 }}
                        >
                          <ArrowLeft size={15} />
                          <span>Previous</span>
                        </button>

                        {currentIndex < questions.length - 1 ? (
                          <button
                            className="btn btn-primary"
                            onClick={() => setCurrentIndex(prev => prev + 1)}
                            style={{ fontSize: '13px', padding: '7px 16px', gap: '6px' }}
                          >
                            <span>Next Question</span>
                            <ArrowRight size={15} />
                          </button>
                        ) : (
                          <button
                            className="btn btn-emerald"
                            onClick={() => setShowSubmitConfirm(true)}
                            style={{ fontSize: '13px', padding: '7px 18px', gap: '6px' }}
                          >
                            <span>Finish & Review</span>
                            <Check size={15} />
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })()}
            </div>

            {/* Right: 50-Question Interactive Palette */}
            <div className="glass-card" style={{
              padding: '20px',
              background: 'var(--bg-card)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-lg)',
              position: 'sticky',
              top: '90px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '14px' }}>
                <h4 style={{ margin: 0, fontSize: '14.5px', fontWeight: 700, color: '#fff' }}>
                  Question Palette ({questions.length})
                </h4>
                <span style={{ fontSize: '12px', color: 'var(--emerald)', fontWeight: 600 }}>
                  {answeredCount}/{questions.length} Answered
                </span>
              </div>

              {/* Legend */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '6px', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ width: '10px', height: '10px', borderRadius: '2px', background: 'var(--emerald)' }} />
                  <span>Answered ({answeredCount})</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ width: '10px', height: '10px', borderRadius: '2px', background: 'rgba(255, 255, 255, 0.1)' }} />
                  <span>Unanswered ({unattemptedCount})</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ width: '10px', height: '10px', borderRadius: '2px', background: '#c084fc' }} />
                  <span>Review ({markedForReview.size})</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ width: '10px', height: '10px', borderRadius: '2px', border: '1.5px solid var(--cyan)' }} />
                  <span>Current Q</span>
                </div>
              </div>

              {/* 50-Button Palette Grid */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(5, 1fr)',
                gap: '6px',
                maxHeight: '360px',
                overflowY: 'auto',
                padding: '4px'
              }}>
                {questions.map((q, idx) => {
                  const isCurrent = idx === currentIndex;
                  const isAnswered = !!userAnswers[q.id];
                  const isMarked = markedForReview.has(q.id);

                  let bgColor = 'rgba(255, 255, 255, 0.04)';
                  let textColor = 'var(--text-secondary)';

                  if (isMarked) {
                    bgColor = 'rgba(192, 132, 252, 0.25)';
                    textColor = '#c084fc';
                  } else if (isAnswered) {
                    bgColor = 'rgba(16, 185, 129, 0.25)';
                    textColor = 'var(--emerald)';
                  }

                  return (
                    <button
                      key={q.id || idx}
                      onClick={() => setCurrentIndex(idx)}
                      style={{
                        padding: '8px 0',
                        fontSize: '12px',
                        fontWeight: 700,
                        borderRadius: '6px',
                        background: bgColor,
                        color: isCurrent ? '#fff' : textColor,
                        border: isCurrent ? '2px solid var(--cyan)' : '1px solid rgba(255, 255, 255, 0.06)',
                        cursor: 'pointer',
                        transition: 'all 0.15s ease',
                        boxShadow: isCurrent ? '0 0 10px rgba(6, 182, 212, 0.3)' : 'none'
                      }}
                      title={`Q${idx + 1}: ${q.subject || 'General'} - ${isAnswered ? 'Answered' : 'Unanswered'}`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>

              {/* Quick Submit inside palette */}
              <button
                className="btn btn-emerald"
                onClick={() => setShowSubmitConfirm(true)}
                style={{ width: '100%', justifyContent: 'center', marginTop: '16px', fontSize: '13px', padding: '10px' }}
              >
                Submit Mock Test
              </button>
            </div>
          </div>

          {/* Confirmation Modal */}
          {showSubmitConfirm && (
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
                maxWidth: '460px',
                padding: '28px',
                boxShadow: '0 25px 50px rgba(0, 0, 0, 0.7)',
                textAlign: 'center'
              }}>
                <div style={{
                  width: '56px',
                  height: '56px',
                  borderRadius: '50%',
                  background: 'rgba(6, 182, 212, 0.12)',
                  color: 'var(--cyan)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  margin: '0 auto 16px'
                }}>
                  <Award size={28} />
                </div>

                <h3 style={{ fontSize: '20px', fontWeight: 800, color: '#fff', marginBottom: '8px' }}>
                  Submit 50-Question Mock Exam?
                </h3>
                <p style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.5, marginBottom: '20px' }}>
                  You are about to complete your examination. Once submitted, your score will be calculated with competitive negative marking.
                </p>

                {/* Summary Grid */}
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(3, 1fr)',
                  gap: '10px',
                  padding: '14px',
                  background: 'rgba(0, 0, 0, 0.3)',
                  borderRadius: 'var(--radius-md)',
                  marginBottom: '24px'
                }}>
                  <div>
                    <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--emerald)' }}>{answeredCount}</div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Answered</div>
                  </div>
                  <div>
                    <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--rose)' }}>{unattemptedCount}</div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Unanswered</div>
                  </div>
                  <div>
                    <div style={{ fontSize: '18px', fontWeight: 800, color: '#c084fc' }}>{markedForReview.size}</div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Marked Review</div>
                  </div>
                </div>

                <div style={{ display: 'flex', gap: '10px', justifyContent: 'center' }}>
                  <button
                    className="btn btn-secondary"
                    onClick={() => setShowSubmitConfirm(false)}
                    style={{ flex: 1, padding: '10px' }}
                  >
                    Resume Test
                  </button>
                  <button
                    className="btn btn-emerald"
                    onClick={handleSubmitExam}
                    disabled={submitting}
                    style={{ flex: 1, padding: '10px', fontWeight: 700 }}
                  >
                    {submitting ? 'Submitting...' : 'Yes, Submit Test'}
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* ==========================================
          STATE 3: COMPREHENSIVE RESULT REPORT
          ========================================== */}
      {quizResult && (
        <div style={{ maxWidth: '900px', margin: '0 auto' }}>
          {/* Main Score Card */}
          <div className="glass-card" style={{
            padding: '36px',
            textAlign: 'center',
            borderRadius: 'var(--radius-lg)',
            border: `1px solid ${quizResult.passed ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`,
            marginBottom: '28px'
          }}>
            <div style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '8px',
              padding: '6px 16px',
              borderRadius: '20px',
              background: quizResult.passed ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
              color: quizResult.passed ? 'var(--emerald)' : 'var(--rose)',
              fontWeight: 800,
              fontSize: '13px',
              marginBottom: '16px'
            }}>
              {quizResult.passed ? <CheckCircle2 size={18} /> : <XCircle size={18} />}
              <span>{quizResult.passed ? 'EXAM PASSED ✓' : 'NEEDS PRACTICE'}</span>
            </div>

            <h2 style={{ fontSize: '26px', fontWeight: 800, color: '#fff', margin: '0 0 6px' }}>
              {quizResult.exam_title || 'Competitive Mock Exam'}
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14.5px', maxWidth: '560px', margin: '0 auto 24px', lineHeight: 1.5 }}>
              {quizResult.message}
            </p>

            {/* Score Metric Numbers */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))',
              gap: '14px',
              maxWidth: '680px',
              margin: '0 auto 28px'
            }}>
              <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', background: 'rgba(0, 0, 0, 0.3)', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
                <div style={{ fontSize: '24px', fontWeight: 800, color: quizResult.passed ? 'var(--emerald)' : 'var(--rose)' }}>
                  {quizResult.score} <span style={{ fontSize: '14px', color: 'var(--text-muted)' }}>/ {quizResult.max_marks || 100}</span>
                </div>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px' }}>Net Marks</div>
              </div>

              <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', background: 'rgba(0, 0, 0, 0.3)', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
                <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--cyan)' }}>
                  {quizResult.percentage}%
                </div>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px' }}>Accuracy Rate</div>
              </div>

              <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', background: 'rgba(0, 0, 0, 0.3)', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
                <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--emerald)' }}>
                  {quizResult.correct_count}
                </div>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px' }}>Correct (+2 ea)</div>
              </div>

              <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', background: 'rgba(0, 0, 0, 0.3)', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
                <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--rose)' }}>
                  {quizResult.incorrect_count}
                </div>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px' }}>Incorrect (-0.25 ea)</div>
              </div>

              <div style={{ padding: '16px', borderRadius: 'var(--radius-md)', background: 'rgba(0, 0, 0, 0.3)', border: '1px solid rgba(255, 255, 255, 0.05)' }}>
                <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--amber)' }}>
                  {quizResult.unattempted_count}
                </div>
                <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '4px' }}>Unattempted</div>
              </div>
            </div>

            {/* Action Buttons */}
            <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
              <button
                className="btn btn-primary"
                onClick={() => {
                  if (activeExam) handleStartExam(activeExam);
                }}
                style={{ padding: '10px 22px', fontSize: '13.5px', gap: '6px' }}
              >
                <RotateCcw size={16} />
                <span>Retake This Exam</span>
              </button>
              <button
                className="btn btn-secondary"
                onClick={() => {
                  setQuizResult(null);
                  setActiveExam(null);
                  setQuizStarted(false);
                  fetchMockExams();
                }}
                style={{ padding: '10px 22px', fontSize: '13.5px' }}
              >
                <span>Browse All Mock Exams</span>
              </button>
            </div>
          </div>

          {/* Question-by-Question Solution Analysis */}
          <div className="glass-card" style={{ padding: '28px', borderRadius: 'var(--radius-lg)' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '6px' }}>
              Detailed Question Solutions & Explanations ({quizResult.breakdown?.length || 0} Questions)
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginBottom: '24px' }}>
              Review the official answers, your responses, and complete rationale for every question.
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {quizResult.breakdown?.map((item, idx) => (
                <div
                  key={idx}
                  style={{
                    padding: '20px',
                    borderRadius: 'var(--radius-md)',
                    background: item.is_correct 
                      ? 'rgba(16, 185, 129, 0.04)' 
                      : item.is_unattempted 
                        ? 'rgba(255, 255, 255, 0.02)' 
                        : 'rgba(239, 68, 68, 0.04)',
                    border: `1px solid ${
                      item.is_correct 
                        ? 'rgba(16, 185, 129, 0.25)' 
                        : item.is_unattempted 
                          ? 'var(--border-subtle)' 
                          : 'rgba(239, 68, 68, 0.25)'
                    }`
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px', flexWrap: 'wrap', gap: '8px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{
                        width: '26px',
                        height: '26px',
                        borderRadius: '50%',
                        background: 'rgba(255, 255, 255, 0.08)',
                        color: '#fff',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '12px',
                        fontWeight: 700
                      }}>
                        {idx + 1}
                      </span>
                      <span className="badge badge-primary" style={{ fontSize: '11px' }}>
                        {item.subject || 'General'}
                      </span>
                      {item.topic && (
                        <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                          {item.topic}
                        </span>
                      )}
                    </div>

                    <span className={`badge ${item.is_correct ? 'badge-emerald' : item.is_unattempted ? 'badge-amber' : 'badge-rose'}`} style={{ fontSize: '11.5px' }}>
                      {item.is_correct ? 'Correct (+2.0)' : item.is_unattempted ? 'Skipped (0.0)' : 'Incorrect (-0.25)'}
                    </span>
                  </div>

                  <h5 style={{ fontSize: '15px', fontWeight: 600, color: '#fff', margin: '0 0 14px', lineHeight: 1.5 }}>
                    {item.question}
                  </h5>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '10px', marginBottom: '12px' }}>
                    <div style={{ padding: '8px 12px', borderRadius: '6px', background: 'rgba(0, 0, 0, 0.25)', fontSize: '13px' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '2px' }}>Your Response:</div>
                      <strong style={{ color: item.is_correct ? 'var(--emerald)' : item.is_unattempted ? 'var(--text-muted)' : 'var(--rose)' }}>
                        {item.user_answer || '(Unattempted)'}
                      </strong>
                    </div>

                    <div style={{ padding: '8px 12px', borderRadius: '6px', background: 'rgba(0, 0, 0, 0.25)', fontSize: '13px' }}>
                      <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '2px' }}>Correct Answer:</div>
                      <strong style={{ color: 'var(--emerald)' }}>
                        {item.correct_answer}
                      </strong>
                    </div>
                  </div>

                  {item.explanation && (
                    <div style={{
                      padding: '10px 14px',
                      borderRadius: '6px',
                      background: 'rgba(6, 182, 212, 0.06)',
                      border: '1px solid rgba(6, 182, 212, 0.15)',
                      fontSize: '12.5px',
                      color: 'var(--text-secondary)',
                      lineHeight: 1.5
                    }}>
                      <strong style={{ color: 'var(--cyan)' }}>Explanation: </strong>
                      {item.explanation}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
