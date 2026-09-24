import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  FileText, 
  HelpCircle, 
  Award, 
  CheckCircle2, 
  XCircle, 
  ArrowLeft, 
  ArrowRight, 
  ExternalLink, 
  ShieldCheck, 
  Sparkles, 
  Clock, 
  RotateCcw, 
  Lock, 
  Unlock,
  ChevronRight,
  Info,
  Check,
  X
} from 'lucide-react';

export default function TopicLearningPage({ topicId = 1, navigateTo }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('learn'); // 'learn' | 'pyqs' | 'practice' | 'quiz'

  // PYQ Interactive State
  const [pyqSelectedAnswers, setPyqSelectedAnswers] = useState({});
  const [pyqRevealed, setPyqRevealed] = useState({});

  // Practice Interactive State
  const [practiceSelectedAnswers, setPracticeSelectedAnswers] = useState({});
  const [practiceRevealed, setPracticeRevealed] = useState({});

  // Quiz Engine State
  const [quizStarted, setQuizStarted] = useState(false);
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);
  const [userQuizAnswers, setUserQuizAnswers] = useState({});
  const [quizTimer, setQuizTimer] = useState(0);
  const [quizTimerActive, setQuizTimerActive] = useState(false);
  const [quizSubmitting, setQuizSubmitting] = useState(false);
  const [quizResult, setQuizResult] = useState(null);

  useEffect(() => {
    fetchTopicData();
    // Reset states
    setActiveTab('learn');
    setQuizStarted(false);
    setQuizResult(null);
    setCurrentQuizIndex(0);
    setUserQuizAnswers({});
    setQuizTimer(0);
    setQuizTimerActive(false);
  }, [topicId]);

  // Quiz countdown / elapsed timer
  useEffect(() => {
    let interval = null;
    if (quizTimerActive) {
      interval = setInterval(() => {
        setQuizTimer(prev => prev + 1);
      }, 1000);
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [quizTimerActive]);

  const fetchTopicData = async () => {
    try {
      setLoading(true);
      const res = await fetch(`http://localhost:3001/api/topics/${topicId}`);
      const result = await res.json();
      setData(result);
    } catch (err) {
      console.error('Error fetching topic:', err);
    } finally {
      setLoading(false);
    }
  };

  const startQuiz = () => {
    setQuizStarted(true);
    setCurrentQuizIndex(0);
    setUserQuizAnswers({});
    setQuizResult(null);
    setQuizTimer(0);
    setQuizTimerActive(true);
  };

  const handleSelectQuizOption = (questionId, option) => {
    setUserQuizAnswers(prev => ({
      ...prev,
      [questionId]: option
    }));
  };

  const submitQuiz = async () => {
    setQuizTimerActive(false);
    setQuizSubmitting(true);

    try {
      const res = await fetch(`http://localhost:3001/api/quizzes/${topicId}/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          answers: userQuizAnswers,
          timeSpentSeconds: quizTimer
        })
      });
      const result = await res.json();
      setQuizResult(result);
      // Refresh topic data to update unlock status of next topic
      fetchTopicData();
    } catch (err) {
      console.error('Error submitting quiz:', err);
      alert('Error submitting quiz. Please try again.');
    } finally {
      setQuizSubmitting(false);
    }
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '80px 20px', color: 'var(--text-secondary)' }}>
        <Sparkles size={32} className="spin" color="var(--cyan)" style={{ marginBottom: '16px' }} />
        <h3>Loading Topic Dashboard...</h3>
      </div>
    );
  }

  if (!data || data.error) {
    return (
      <div style={{ textAlign: 'center', padding: '60px 20px' }}>
        <h3>Topic not found</h3>
        <button className="btn btn-primary" onClick={() => navigateTo('home')} style={{ marginTop: '16px' }}>
          Back to Home
        </button>
      </div>
    );
  }

  const { topic, course, module, lessons = [], previous_year_questions = [], practice_questions = [], quiz, next_topic } = data;
  const lesson = lessons[0] || null;
  const content = lesson?.content_json || {};

  return (
    <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
      {/* ==========================================
          HEADER & BREADCRUMBS
          ========================================== */}
      <div style={{ marginBottom: '24px' }}>
        <button 
          className="btn btn-subtle"
          onClick={() => navigateTo('course', { slug: course.slug })}
          style={{ marginBottom: '14px', paddingLeft: 0 }}
        >
          <ArrowLeft size={16} />
          <span>Back to {course.title} Path</span>
        </button>

        <div className="breadcrumb">
          <span onClick={() => navigateTo('home')} style={{ cursor: 'pointer' }}>Home</span>
          <ChevronRight size={14} />
          <span onClick={() => navigateTo('course', { slug: course.slug })} style={{ cursor: 'pointer' }}>{course.title}</span>
          <ChevronRight size={14} />
          <span>{module.title}</span>
          <ChevronRight size={14} />
          <span className="breadcrumb-active">{topic.title}</span>
        </div>

        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '16px',
          marginTop: '12px',
          paddingBottom: '20px',
          borderBottom: '1px solid var(--border-subtle)'
        }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '6px' }}>
              <h1 style={{ fontSize: '32px', fontWeight: 800 }}>{topic.title}</h1>
              {topic.status === 'completed' ? (
                <span className="badge badge-emerald">
                  <Check size={14} /> Completed ({topic.best_score || 80}%)
                </span>
              ) : (
                <span className="badge badge-primary">
                  <Unlock size={14} /> Level {topic.order_index} Unlocked
                </span>
              )}
            </div>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14px' }}>
              {topic.description}
            </p>
          </div>

          <div style={{ display: 'flex', gap: '8px' }}>
            <span className="badge badge-cyan">
              <ShieldCheck size={12} />
              {previous_year_questions.length} Verified PYQs
            </span>
            <span className="badge badge-amber">
              <Award size={12} />
              Quiz Pass: 70%
            </span>
          </div>
        </div>
      </div>

      {/* ==========================================
          TOPIC NAVIGATION TABS
          ========================================== */}
      <div className="topic-tabs">
        <button 
          className={`topic-tab-btn ${activeTab === 'learn' ? 'active' : ''}`}
          onClick={() => setActiveTab('learn')}
        >
          <BookOpen size={16} />
          <span>1. Learn & Information</span>
        </button>

        <button 
          className={`topic-tab-btn ${activeTab === 'pyqs' ? 'active' : ''}`}
          onClick={() => setActiveTab('pyqs')}
        >
          <FileText size={16} />
          <span>2. Previous Year Questions ({previous_year_questions.length})</span>
        </button>

        <button 
          className={`topic-tab-btn ${activeTab === 'practice' ? 'active' : ''}`}
          onClick={() => setActiveTab('practice')}
        >
          <Sparkles size={16} />
          <span>3. Practice Questions ({practice_questions.length})</span>
        </button>

        <button 
          className={`topic-tab-btn ${activeTab === 'quiz' ? 'active' : ''}`}
          onClick={() => setActiveTab('quiz')}
          style={{ marginLeft: 'auto', background: activeTab === 'quiz' ? 'var(--grad-primary)' : 'rgba(99, 102, 241, 0.15)', color: activeTab === 'quiz' ? '#fff' : '#c7d2fe' }}
        >
          <Award size={16} />
          <span>4. Take Quiz & Unlock</span>
        </button>
      </div>

      {/* ==========================================
          TAB 1: LEARN / INFORMATION
          ========================================== */}
      {activeTab === 'learn' && (
        <div>
          {/* Definition Box */}
          <div className="glass-card" style={{ padding: '28px', marginBottom: '24px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
              <span className="badge badge-cyan">Foundational Concept</span>
              <h2 style={{ fontSize: '20px', fontWeight: 700 }}>{topic.title}: Concept & Definition</h2>
            </div>
            <p style={{ color: 'var(--text-primary)', fontSize: '15.5px', lineHeight: 1.7, marginBottom: '16px' }}>
              {content.definition}
            </p>
          </div>

          {/* Types of Nouns Cards */}
          {content.types && content.types.length > 0 && (
          <div style={{ marginBottom: '32px' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span>{topic.title} Classifications & Core Concepts</span>
              {content.types && <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>({content.types.length} Key Categories)</span>}
            </h3>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px' }}>
              {content.types?.map((type, idx) => (
                <div key={idx} className="glass-card" style={{ padding: '20px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <h4 style={{ fontSize: '16px', fontWeight: 700, color: 'var(--cyan)' }}>{type.name}</h4>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Type {idx + 1}</span>
                  </div>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '13px', lineHeight: 1.5, marginBottom: '12px' }}>
                    {type.desc}
                  </p>
                  <div style={{ background: 'rgba(0, 0, 0, 0.25)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', fontSize: '12px', color: '#cbd5e1' }}>
                    <strong>Examples:</strong> {type.examples?.join(' • ')}
                  </div>
                </div>
              ))}
            </div>
          </div>

          )}

          {/* Countable vs Uncountable Rule Box */}
          {content.countable_vs_uncountable && (
          <div className="glass-card" style={{ padding: '26px', marginBottom: '32px', borderLeft: '4px solid var(--amber)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
              <span className="badge badge-amber">Major Exam Trap</span>
              <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Countable vs. Uncountable Nouns</h3>
            </div>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14.5px', lineHeight: 1.6, marginBottom: '16px' }}>
              {content.countable_vs_uncountable?.overview}
            </p>

            <div style={{ marginBottom: '16px' }}>
              <div style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '8px', textTransform: 'uppercase' }}>
                High-Frequency Uncountable Nouns in Exams:
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                {content.countable_vs_uncountable?.uncountable_list?.map((word, wIdx) => (
                  <span key={wIdx} style={{
                    padding: '4px 10px',
                    borderRadius: 'var(--radius-sm)',
                    background: 'rgba(245, 158, 11, 0.12)',
                    border: '1px solid rgba(245, 158, 11, 0.25)',
                    color: '#fcd34d',
                    fontSize: '12.5px',
                    fontWeight: 600
                  }}>
                    {word}
                  </span>
                ))}
              </div>
            </div>

            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '12px 16px', borderRadius: 'var(--radius-sm)', fontSize: '13px', color: '#e2e8f0', lineHeight: 1.5 }}>
              💡 <strong>Gold Rule:</strong> {content.countable_vs_uncountable?.exam_rule}
            </div>
          </div>

          )}

          {/* Important Competitive Exam Rules */}
          <div style={{ marginBottom: '32px' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>
              Core Concepts & Rules for {topic.title}
            </h3>

            {content.rules?.map((rule, rIdx) => (
              <div key={rIdx} className="rule-card">
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
                  <span className="badge badge-primary">Rule {rule.rule_number}</span>
                  <h4 style={{ fontSize: '16px', fontWeight: 700 }}>{rule.title}</h4>
                </div>
                <p style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.5, marginBottom: '12px' }}>
                  {rule.explanation}
                </p>

                {rule.words && (
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                    {rule.words.map((w, wi) => (
                      <span key={wi} style={{ fontSize: '12px', padding: '2px 8px', borderRadius: '4px', background: 'rgba(255, 255, 255, 0.05)', color: '#cbd5e1' }}>
                        {w}
                      </span>
                    ))}
                  </div>
                )}

                <div className="example-box">
                  <div className="example-correct">
                    <CheckCircle2 size={16} />
                    <span><strong>Correct:</strong> {rule.correct}</span>
                  </div>
                  <div className="example-incorrect">
                    <XCircle size={16} />
                    <span><strong>Incorrect:</strong> {rule.incorrect}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Common Mistakes Table */}
          <div className="glass-card" style={{ padding: '24px', marginBottom: '32px' }}>
            <h3 style={{ fontSize: '17px', fontWeight: 700, marginBottom: '16px' }}>
              Common Exam Traps & Error Corrections
            </h3>
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13.5px' }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--border-subtle)', textAlign: 'left', color: 'var(--text-muted)' }}>
                    <th style={{ padding: '10px 14px' }}>Common Error</th>
                    <th style={{ padding: '10px 14px' }}>Correct Construction</th>
                    <th style={{ padding: '10px 14px' }}>Conceptual Rationale</th>
                  </tr>
                </thead>
                <tbody>
                  {content.common_mistakes?.map((item, mIdx) => (
                    <tr key={mIdx} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.04)' }}>
                      <td style={{ padding: '12px 14px', color: '#fda4af' }}>{item.mistake}</td>
                      <td style={{ padding: '12px 14px', color: '#6ee7b7', fontWeight: 600 }}>{item.correction}</td>
                      <td style={{ padding: '12px 14px', color: 'var(--text-secondary)' }}>{item.rationale}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Quick Revision Points */}
          <div className="glass-card" style={{ padding: '24px', marginBottom: '32px' }}>
            <h3 style={{ fontSize: '17px', fontWeight: 700, marginBottom: '14px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Sparkles size={18} color="var(--cyan)" />
              <span>Quick Revision Points</span>
            </h3>
            <ul style={{ paddingLeft: '20px', color: 'var(--text-secondary)', display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '14px' }}>
              {content.quick_revision_points?.map((pt, pIdx) => (
                <li key={pIdx}>{pt}</li>
              ))}
            </ul>
          </div>

          {/* Verified Source Reference Box */}
          {lesson?.source && (
            <div className="source-box">
              <ShieldCheck size={24} color="var(--cyan)" style={{ flexShrink: 0, marginTop: '2px' }} />
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                  <span style={{ fontWeight: 700, fontSize: '13.5px', color: '#f8fafc' }}>
                    Verified Source Attribution
                  </span>
                  <span className="badge badge-cyan" style={{ fontSize: '11px', padding: '1px 6px' }}>
                    {lesson.source.type}
                  </span>
                </div>
                <p style={{ color: 'var(--text-secondary)', fontSize: '12.5px', lineHeight: 1.4 }}>
                  {lesson.source.title} — Published by {lesson.source.publisher}. Verified by Skillexa editorial standards.
                </p>
                <a 
                  href={lesson.source.url} 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: 'var(--cyan)', fontSize: '12px', marginTop: '6px' }}
                >
                  <span>Official Reference Link</span>
                  <ExternalLink size={12} />
                </a>
              </div>
            </div>
          )}

          {/* Navigation to PYQs */}
          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '32px' }}>
            <button className="btn btn-primary" onClick={() => setActiveTab('pyqs')}>
              <span>Next: Practice Previous Year Questions</span>
              <ArrowRight size={16} />
            </button>
          </div>
        </div>
      )}

      {/* ==========================================
          TAB 2: PREVIOUS YEAR QUESTIONS (PYQs)
          ========================================== */}
      {activeTab === 'pyqs' && (
        <div>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '16px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(6, 182, 212, 0.08)',
            border: '1px solid rgba(6, 182, 212, 0.25)',
            marginBottom: '24px'
          }}>
            <div>
              <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#f8fafc' }}>
                Authentic Previous Year Examination Questions
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginTop: '2px' }}>
                These questions have appeared in actual official competitive exams. Select an option to test your understanding, then reveal the verified explanation.
              </p>
            </div>
            <span className="badge badge-cyan">Verified Exam Authority</span>
          </div>

          {previous_year_questions.map((pyq, index) => {
            const options = pyq.options_json || [];
            const selected = pyqSelectedAnswers[pyq.id];
            const isRevealed = pyqRevealed[pyq.id];

            return (
              <div key={pyq.id} className="pyq-card">
                <div className="pyq-header">
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span className="badge badge-primary">Q{index + 1}</span>
                    <span className="pyq-exam-tag">
                      {pyq.exam?.name || 'SSC CGL'} {pyq.exam?.year || 2024} ({pyq.exam?.tier || 'Tier 1'})
                    </span>
                    <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                      Subject: {course?.title || 'General'} • Topic: {topic.title}
                    </span>
                  </div>

                  {pyq.source && (
                    <span style={{ fontSize: '11.5px', color: 'var(--text-muted)' }}>
                      Source: {pyq.source.publisher}
                    </span>
                  )}
                </div>

                <div style={{ fontSize: '15px', fontWeight: 600, color: '#f8fafc', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                  {pyq.question}
                </div>

                {/* Options or Answer Input */}
                {(() => {
                  const isFillInTheBlank = pyq.question_type === 'FILL_IN_THE_BLANK' || (!options || options.length === 0);
                  if (isFillInTheBlank) {
                    const cleanUser = String(selected || '').trim().toLowerCase();
                    const cleanCorrect = String(pyq.correct_answer || '').trim().toLowerCase();
                    const isCorrect = isRevealed && cleanUser.length > 0 && cleanUser === cleanCorrect;

                    return (
                      <div style={{ margin: '16px 0 20px' }}>
                        <div style={{ maxWidth: '440px', marginBottom: '10px' }}>
                          <input
                            type="text"
                            disabled={isRevealed}
                            placeholder="Enter your answer"
                            value={selected || ''}
                            onChange={(e) => setPyqSelectedAnswers(prev => ({ ...prev, [pyq.id]: e.target.value }))}
                            style={{
                              width: '100%',
                              padding: '10px 14px',
                              fontSize: '14.5px',
                              background: 'rgba(15, 23, 42, 0.7)',
                              border: isRevealed 
                                ? (isCorrect ? '1px solid var(--emerald)' : '1px solid var(--rose)')
                                : '1px solid rgba(255, 255, 255, 0.2)',
                              borderRadius: 'var(--radius-md)',
                              color: '#ffffff',
                              outline: 'none'
                            }}
                          />
                        </div>
                        {isRevealed && (
                          <div style={{ fontSize: '13px', marginBottom: '8px', color: isCorrect ? 'var(--emerald)' : 'var(--rose)' }}>
                            Your Answer: <strong>{selected || '(None)'}</strong> — {isCorrect ? 'Correct ✓' : 'Incorrect ✗'}
                          </div>
                        )}
                      </div>
                    );
                  }

                  return (
                    <div className="options-grid">
                      {options.map((opt, oIdx) => {
                        const letters = ['A', 'B', 'C', 'D'];
                        let btnClass = 'option-btn';
                        if (selected === opt) btnClass += ' selected';
                        if (isRevealed) {
                          if (opt === pyq.correct_answer) btnClass += ' correct';
                          else if (selected === opt && selected !== pyq.correct_answer) btnClass += ' wrong';
                        }

                        return (
                          <button 
                            key={oIdx}
                            className={btnClass}
                            onClick={() => {
                              if (!isRevealed) {
                                setPyqSelectedAnswers(prev => ({ ...prev, [pyq.id]: opt }));
                              }
                            }}
                          >
                            <span className="option-letter">{letters[oIdx]}</span>
                            <span>{opt}</span>
                          </button>
                        );
                      })}
                    </div>
                  );
                })()}

                {/* Reveal Answer Action */}
                {!isRevealed ? (
                  <button 
                    className="btn btn-secondary"
                    onClick={() => setPyqRevealed(prev => ({ ...prev, [pyq.id]: true }))}
                    style={{ fontSize: '13px', padding: '8px 16px' }}
                  >
                    <span>Check Answer & Explanation</span>
                  </button>
                ) : (
                  <div className="explanation-card">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                      <CheckCircle2 size={18} color="var(--emerald)" />
                      <span style={{ fontWeight: 700, fontSize: '14px', color: 'var(--emerald)' }}>
                        Correct Answer: {pyq.correct_answer}
                      </span>
                    </div>
                    <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', lineHeight: 1.6 }}>
                      {pyq.explanation}
                    </p>
                    {pyq.source && (
                      <div style={{ marginTop: '10px', fontSize: '12px', color: 'var(--text-muted)' }}>
                        <strong>Reference:</strong> {pyq.source.title} ({pyq.source.publisher})
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}

          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '32px' }}>
            <button className="btn btn-secondary" onClick={() => setActiveTab('learn')}>
              <ArrowLeft size={16} />
              <span>Back to Learn</span>
            </button>
            <button className="btn btn-primary" onClick={() => setActiveTab('practice')}>
              <span>Next: Additional Practice Questions</span>
              <ArrowRight size={16} />
            </button>
          </div>
        </div>
      )}

      {/* ==========================================
          TAB 3: PRACTICE QUESTIONS
          ========================================== */}
      {activeTab === 'practice' && (
        <div>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '16px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(99, 102, 241, 0.08)',
            border: '1px solid rgba(99, 102, 241, 0.25)',
            marginBottom: '24px'
          }}>
            <div>
              <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#f8fafc' }}>
                Curated Practice Questions
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginTop: '2px' }}>
                These are supplementary exercise problems designed to reinforce your mastery of tricky rules before taking the official unlock quiz.
              </p>
            </div>
            <span className="badge badge-primary">Practice Exercises</span>
          </div>

          {practice_questions.map((pq, index) => {
            const options = pq.options_json || [];
            const selected = practiceSelectedAnswers[pq.id];
            const isRevealed = practiceRevealed[pq.id];

            return (
              <div key={pq.id} className="pyq-card">
                <div className="pyq-header">
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span className="badge badge-primary">Practice {index + 1}</span>
                    <span className="badge badge-amber">{pq.difficulty || 'Intermediate'}</span>
                  </div>
                </div>

                <div style={{ fontSize: '15px', fontWeight: 600, color: '#f8fafc', lineHeight: 1.6 }}>
                  {pq.question}
                </div>

                {(() => {
                  const isFillInTheBlank = pq.question_type === 'FILL_IN_THE_BLANK' || (!options || options.length === 0);
                  if (isFillInTheBlank) {
                    const cleanUser = String(selected || '').trim().toLowerCase();
                    const cleanCorrect = String(pq.correct_answer || '').trim().toLowerCase();
                    const isCorrect = isRevealed && cleanUser.length > 0 && cleanUser === cleanCorrect;

                    return (
                      <div style={{ margin: '16px 0 20px' }}>
                        <div style={{ maxWidth: '440px', marginBottom: '10px' }}>
                          <input
                            type="text"
                            disabled={isRevealed}
                            placeholder="Enter your answer"
                            value={selected || ''}
                            onChange={(e) => setPracticeSelectedAnswers(prev => ({ ...prev, [pq.id]: e.target.value }))}
                            style={{
                              width: '100%',
                              padding: '10px 14px',
                              fontSize: '14.5px',
                              background: 'rgba(15, 23, 42, 0.7)',
                              border: isRevealed 
                                ? (isCorrect ? '1px solid var(--emerald)' : '1px solid var(--rose)')
                                : '1px solid rgba(255, 255, 255, 0.2)',
                              borderRadius: 'var(--radius-md)',
                              color: '#ffffff',
                              outline: 'none'
                            }}
                          />
                        </div>
                        {isRevealed && (
                          <div style={{ fontSize: '13px', marginBottom: '8px', color: isCorrect ? 'var(--emerald)' : 'var(--rose)' }}>
                            Your Answer: <strong>{selected || '(None)'}</strong> — {isCorrect ? 'Correct ✓' : 'Incorrect ✗'}
                          </div>
                        )}
                      </div>
                    );
                  }

                  return (
                    <div className="options-grid">
                      {options.map((opt, oIdx) => {
                        const letters = ['A', 'B', 'C', 'D'];
                        let btnClass = 'option-btn';
                        if (selected === opt) btnClass += ' selected';
                        if (isRevealed) {
                          if (opt === pq.correct_answer) btnClass += ' correct';
                          else if (selected === opt && selected !== pq.correct_answer) btnClass += ' wrong';
                        }

                        return (
                          <button 
                            key={oIdx}
                            className={btnClass}
                            onClick={() => {
                              if (!isRevealed) {
                                setPracticeSelectedAnswers(prev => ({ ...prev, [pq.id]: opt }));
                              }
                            }}
                          >
                            <span className="option-letter">{letters[oIdx]}</span>
                            <span>{opt}</span>
                          </button>
                        );
                      })}
                    </div>
                  );
                })()}

                {!isRevealed ? (
                  <button 
                    className="btn btn-secondary"
                    onClick={() => setPracticeRevealed(prev => ({ ...prev, [pq.id]: true }))}
                    style={{ fontSize: '13px', padding: '8px 16px' }}
                  >
                    <span>Check Solution</span>
                  </button>
                ) : (
                  <div className="explanation-card">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                      <CheckCircle2 size={18} color="var(--emerald)" />
                      <span style={{ fontWeight: 700, fontSize: '14px', color: 'var(--emerald)' }}>
                        Correct: {pq.correct_answer}
                      </span>
                    </div>
                    <p style={{ color: 'var(--text-secondary)', fontSize: '13px', lineHeight: 1.5 }}>
                      {pq.explanation}
                    </p>
                  </div>
                )}
              </div>
            );
          })}

          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '32px' }}>
            <button className="btn btn-secondary" onClick={() => setActiveTab('pyqs')}>
              <ArrowLeft size={16} />
              <span>Back to PYQs</span>
            </button>
            <button className="btn btn-emerald" onClick={() => setActiveTab('quiz')}>
              <span>Start Level Quiz & Unlock</span>
              <ArrowRight size={16} />
            </button>
          </div>
        </div>
      )}

      {/* ==========================================
          TAB 4: QUIZ ENGINE & UNLOCK SYSTEM
          ========================================== */}
      {activeTab === 'quiz' && (
        <div className="quiz-container">
          {/* State 1: Quiz Not Started Yet */}
          {!quizStarted && !quizResult && (
            <div className="glass-card" style={{ padding: '36px', textAlign: 'center' }}>
              <div style={{
                width: '64px',
                height: '64px',
                borderRadius: '50%',
                background: 'rgba(99, 102, 241, 0.15)',
                border: '1px solid var(--border-glow)',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'var(--primary-light)',
                marginBottom: '16px'
              }}>
                <Award size={32} />
              </div>

              <h2 style={{ fontSize: '24px', fontWeight: 800, marginBottom: '8px' }}>
                {topic.title} Mastery Quiz
              </h2>
              <p style={{ color: 'var(--text-secondary)', fontSize: '15px', maxWidth: '540px', margin: '0 auto 24px', lineHeight: 1.6 }}>
                Test your understanding of {topic.title} across 10 multiple-choice questions. Score at least <strong>70%</strong> (7/10) to complete this level and unlock <strong>{next_topic?.title || 'the next topic'}</strong>.
              </p>

              <div style={{
                display: 'inline-grid',
                gridTemplateColumns: 'repeat(3, 1fr)',
                gap: '16px',
                padding: '16px 24px',
                borderRadius: 'var(--radius-md)',
                background: 'rgba(0, 0, 0, 0.3)',
                marginBottom: '28px'
              }}>
                <div>
                  <div style={{ fontSize: '18px', fontWeight: 700, color: '#ffffff' }}>10</div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Questions</div>
                </div>
                <div>
                  <div style={{ fontSize: '18px', fontWeight: 700, color: 'var(--cyan)' }}>70%</div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Passing Score</div>
                </div>
                <div>
                  <div style={{ fontSize: '18px', fontWeight: 700, color: 'var(--amber)' }}>10 Mins</div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Recommended Time</div>
                </div>
              </div>

              <div>
                <button className="btn btn-primary" onClick={startQuiz} style={{ padding: '12px 32px', fontSize: '16px' }}>
                  <span>Begin Quiz Now</span>
                  <ArrowRight size={18} />
                </button>
              </div>
            </div>
          )}

          {/* State 2: Active Quiz In Progress */}
          {quizStarted && !quizResult && quiz?.questions && (
            <div>
              {/* Quiz Header with Timer & Progress */}
              <div className="quiz-header">
                <div>
                  <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
                    Question {currentQuizIndex + 1} of {quiz.questions.length}
                  </span>
                  <div style={{ fontSize: '12px', color: 'var(--cyan)', fontWeight: 600 }}>
                    Passing Requirement: 70%
                  </div>
                </div>

                <div className="quiz-timer">
                  <Clock size={16} />
                  <span>{formatTime(quizTimer)}</span>
                </div>
              </div>

              {/* Progress Bar */}
              <div className="progress-bar-container" style={{ marginBottom: '24px' }}>
                <div 
                  className="progress-bar-fill"
                  style={{ width: `${((currentQuizIndex + 1) / quiz.questions.length) * 100}%` }}
                />
              </div>

              {/* Current Question Card */}
              {(() => {
                const currentQ = quiz.questions[currentQuizIndex];
                const selected = userQuizAnswers[currentQ.id];

                return (
                  <div className="glass-card" style={{ padding: '32px' }}>
                    <div style={{ fontSize: '17px', fontWeight: 700, lineHeight: 1.6, marginBottom: '24px', color: '#ffffff' }}>
                      {currentQ.question}
                    </div>

                    {(() => {
                      const isFillInTheBlank = currentQ.question_type === 'FILL_IN_THE_BLANK' || 
                        (!currentQ.options || currentQ.options.length === 0) || 
                        currentQ.question?.includes('____') || 
                        currentQ.question?.includes('______');

                      if (isFillInTheBlank) {
                        return (
                          <div style={{ margin: '20px 0 28px' }}>
                            <label 
                              htmlFor={`fitb-input-${currentQ.id}`}
                              style={{ display: 'block', fontSize: '13.5px', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '8px' }}
                            >
                              Enter your answer:
                            </label>
                            <div style={{ maxWidth: '440px' }}>
                              <input
                                id={`fitb-input-${currentQ.id}`}
                                type="text"
                                placeholder="Enter your answer"
                                value={selected || ''}
                                onChange={(e) => handleSelectQuizOption(currentQ.id, e.target.value)}
                                style={{
                                  width: '100%',
                                  padding: '12px 16px',
                                  fontSize: '15px',
                                  background: 'rgba(15, 23, 42, 0.7)',
                                  border: selected ? '1px solid var(--primary)' : '1px solid rgba(255, 255, 255, 0.2)',
                                  borderRadius: 'var(--radius-md)',
                                  color: '#ffffff',
                                  outline: 'none',
                                  boxShadow: selected ? '0 0 0 2px rgba(99, 102, 241, 0.25)' : 'none',
                                  transition: 'border-color 0.2s, box-shadow 0.2s'
                                }}
                                autoFocus
                              />
                            </div>
                            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '8px' }}>
                              Note: Capitalization and extra leading/trailing spaces will be ignored during evaluation.
                            </div>
                          </div>
                        );
                      }

                      return (
                        <div className="options-grid">
                          {currentQ.options?.map((opt, oIdx) => {
                            const letters = ['A', 'B', 'C', 'D'];
                            const isSelected = selected === opt;

                            return (
                              <button
                                key={oIdx}
                                className={`option-btn ${isSelected ? 'selected' : ''}`}
                                onClick={() => handleSelectQuizOption(currentQ.id, opt)}
                              >
                                <span className="option-letter">{letters[oIdx]}</span>
                                <span>{opt}</span>
                              </button>
                            );
                          })}
                        </div>
                      );
                    })()}

                    {/* Navigation Buttons */}
                    <div className="quiz-nav-row">
                      <button
                        className="btn btn-secondary"
                        onClick={() => setCurrentQuizIndex(prev => Math.max(0, prev - 1))}
                        disabled={currentQuizIndex === 0}
                        style={{ opacity: currentQuizIndex === 0 ? 0.4 : 1 }}
                      >
                        <ArrowLeft size={16} />
                        <span>Previous</span>
                      </button>

                      {currentQuizIndex < quiz.questions.length - 1 ? (
                        <button
                          className="btn btn-primary"
                          onClick={() => setCurrentQuizIndex(prev => prev + 1)}
                        >
                          <span>Next Question</span>
                          <ArrowRight size={16} />
                        </button>
                      ) : (
                        <button
                          className="btn btn-emerald"
                          onClick={submitQuiz}
                          disabled={quizSubmitting}
                          style={{ padding: '10px 24px' }}
                        >
                          <span>{quizSubmitting ? 'Evaluating...' : 'Submit Quiz'}</span>
                          <Check size={16} />
                        </button>
                      )}
                    </div>
                  </div>
                );
              })()}
            </div>
          )}

          {/* State 3: Quiz Result View (Backend Evaluated) */}
          {quizResult && (
            <div className="quiz-result-card">
              {/* Passed or Failed Badge */}
              <div 
                className="result-badge-big"
                style={{
                  background: quizResult.passed ? 'rgba(16, 185, 129, 0.15)' : 'rgba(244, 63, 94, 0.15)',
                  border: quizResult.passed ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid rgba(244, 63, 94, 0.4)',
                  color: quizResult.passed ? '#6ee7b7' : '#fda4af'
                }}
              >
                {quizResult.passed ? <CheckCircle2 size={20} /> : <XCircle size={20} />}
                <span>{quizResult.passed ? 'PASSED ✓' : 'NOT PASSED'}</span>
              </div>

              <div className="result-score-number" style={{ color: quizResult.passed ? 'var(--emerald)' : 'var(--rose)' }}>
                {quizResult.score} <span style={{ fontSize: '32px', color: 'var(--text-muted)' }}>/ {quizResult.total}</span>
              </div>

              <div style={{ fontSize: '18px', fontWeight: 700, marginBottom: '8px' }}>
                Score: {quizResult.percentage}%
              </div>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14.5px', maxWidth: '520px', margin: '0 auto 20px' }}>
                {quizResult.message}
              </p>

              {/* Time taken and accuracy */}
              <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', fontSize: '13px', color: 'var(--text-muted)', marginBottom: '24px' }}>
                <span>Time: <strong>{formatTime(quizTimer)}</strong></span>
                <span>Accuracy: <strong>{quizResult.percentage}%</strong></span>
                <span>Required: <strong>≥70%</strong></span>
              </div>

              {/* Core Feature: Unlocked Next Topic Banner */}
              {quizResult.passed && quizResult.unlocked_next_topic && (
                <div className="unlock-celebration-banner">
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', marginBottom: '8px' }}>
                    <Sparkles size={20} color="var(--cyan)" />
                    <h3 style={{ fontSize: '18px', fontWeight: 800, color: '#ffffff' }}>
                      Next Level Unlocked: {quizResult.unlocked_next_topic.title} 🔓
                    </h3>
                  </div>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginBottom: '16px' }}>
                    Your score of {quizResult.percentage}% meets the threshold! The backend has unlocked <strong>{quizResult.unlocked_next_topic.title}</strong> in the learning path.
                  </p>
                  <button 
                    className="btn btn-emerald"
                    onClick={() => navigateTo('topic', { id: quizResult.unlocked_next_topic.id })}
                    style={{ padding: '12px 28px', fontSize: '15px' }}
                  >
                    <span>Continue to {quizResult.unlocked_next_topic.title}</span>
                    <ArrowRight size={16} />
                  </button>
                </div>
              )}

              {/* Failed Action */}
              {!quizResult.passed && (
                <div style={{ margin: '24px 0' }}>
                  <button 
                    className="btn btn-primary"
                    onClick={startQuiz}
                    style={{ padding: '12px 28px' }}
                  >
                    <RotateCcw size={16} />
                    <span>Retry Quiz</span>
                  </button>
                </div>
              )}

              {/* Question by Question Detailed Breakdown */}
              <div style={{ textAlign: 'left', marginTop: '36px', borderTop: '1px solid var(--border-subtle)', paddingTop: '28px' }}>
                <h4 style={{ fontSize: '16px', fontWeight: 700, marginBottom: '16px' }}>
                  Question-by-Question Solution Review:
                </h4>

                {quizResult.breakdown?.map((item, idx) => (
                  <div 
                    key={idx}
                    style={{
                      padding: '16px 20px',
                      borderRadius: 'var(--radius-md)',
                      background: item.is_correct ? 'rgba(16, 185, 129, 0.05)' : 'rgba(244, 63, 94, 0.05)',
                      border: item.is_correct ? '1px solid rgba(16, 185, 129, 0.2)' : '1px solid rgba(244, 63, 94, 0.2)',
                      marginBottom: '12px'
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '10px', marginBottom: '6px' }}>
                      <span style={{ fontWeight: 600, fontSize: '14px', color: '#f8fafc' }}>
                        {idx + 1}. {item.question}
                      </span>
                      {item.is_correct ? (
                        <span className="badge badge-emerald" style={{ flexShrink: 0 }}>Correct</span>
                      ) : (
                        <span className="badge" style={{ background: 'rgba(244, 63, 94, 0.15)', color: '#fda4af', flexShrink: 0 }}>Incorrect</span>
                      )}
                    </div>

                    <div style={{ fontSize: '13px', color: 'var(--text-secondary)', marginBottom: '4px' }}>
                      Your Answer: <strong style={{ color: item.is_correct ? 'var(--emerald)' : 'var(--rose)' }}>{item.user_answer || 'None'}</strong>
                    </div>

                    {!item.is_correct && (
                      <div style={{ fontSize: '13px', color: 'var(--emerald)', marginBottom: '4px' }}>
                        Correct Answer: <strong>{item.correct_answer}</strong>
                      </div>
                    )}

                    <div style={{ fontSize: '12.5px', color: 'var(--text-muted)', background: 'rgba(0,0,0,0.2)', padding: '8px 12px', borderRadius: '4px', marginTop: '6px' }}>
                      💡 <strong>Explanation:</strong> {item.explanation}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
