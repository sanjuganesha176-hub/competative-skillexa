import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Calculator, 
  Brain, 
  Globe, 
  Atom, 
  Activity, 
  ArrowRight, 
  Flame, 
  CheckCircle2, 
  Award, 
  TrendingUp, 
  Sparkles, 
  Lock, 
  Unlock, 
  ShieldCheck, 
  RotateCcw,
  Building2
} from 'lucide-react';

const iconMap = {
  BookOpen: BookOpen,
  Calculator: Calculator,
  Brain: Brain,
  Globe: Globe,
  Atom: Atom,
  Activity: Activity
};

export default function HomePage({ navigateTo }) {
  const [courses, setCourses] = useState([]);
  const [userProgress, setUserProgress] = useState(null);
  const [latestGovtExams, setLatestGovtExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [coursesRes, progressRes, govtRes] = await Promise.all([
        fetch('http://localhost:3001/api/courses'),
        fetch('http://localhost:3001/api/user/progress'),
        fetch('http://localhost:3001/api/government-exams/latest?limit=4')
      ]);

      const coursesData = await coursesRes.json();
      const progressData = await progressRes.json();
      const govtData = await govtRes.json();

      setCourses(coursesData);
      setUserProgress(progressData);
      setLatestGovtExams(govtData.data || []);
    } catch (err) {
      console.error('Error fetching home data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    if (window.confirm('Reset all progress back to initial default state for demonstration?')) {
      try {
        await fetch('http://localhost:3001/api/user/progress/reset', { method: 'POST' });
        fetchData();
      } catch (e) {
        console.error(e);
      }
    }
  };

  const overall = userProgress?.overall || {
    completion_percentage: 0,
    topics_completed: 0,
    total_topics: 77,
    quizzes_completed: 0,
    average_score: 0,
    streak_days: 7
  };

  return (
    <div>
      {/* ==========================================
          HERO SECTION
          ========================================== */}
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-tagline-badge">
            <Sparkles size={14} color="var(--cyan)" />
            <span>Competitive Exam Readiness • Verified Sourced Syllabus</span>
          </div>

          <h1 className="hero-title">
            Build Your Skills. <span className="text-gradient">Prepare With Confidence.</span>
          </h1>
          <p className="hero-subtitle">
            Learn concepts, practice real questions, and unlock your next level. Every topic is an unlockable mastery stage backed by official exam patterns.
          </p>

          <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap' }}>
            <button 
              className="btn btn-primary"
              onClick={() => navigateTo('course', { slug: 'english' })}
            >
              <span>Continue Learning: English</span>
              <ArrowRight size={16} />
            </button>
            <button 
              className="btn btn-secondary"
              onClick={() => navigateTo('government-exams')}
              style={{ gap: '6px' }}
            >
              <Building2 size={16} color="var(--cyan)" />
              <span>Gov Exams Updates</span>
            </button>
            <button 
              className="btn btn-emerald"
              onClick={() => navigateTo('overall-quiz')}
            >
              <Sparkles size={16} />
              <span>Take Full Mock Exam</span>
            </button>
            <button
              className="btn btn-subtle"
              onClick={handleReset}
              title="Reset progress to demo unlock flow"
              style={{ fontSize: '12px', gap: '6px' }}
            >
              <RotateCcw size={14} />
              <span>Reset Demo Progress</span>
            </button>
          </div>

          {/* User's Overall Progress Stats Row */}
          <div className="stats-grid">
            {/* 1. Overall Completion */}
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <TrendingUp size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{overall.completion_percentage}%</div>
                <div className="stat-label">Overall Completion</div>
              </div>
            </div>

            {/* 2. Topics Completed */}
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{overall.topics_completed} <span style={{ fontSize: '14px', color: 'var(--text-muted)' }}>/ {overall.total_topics}</span></div>
                <div className="stat-label">Topics Completed</div>
              </div>
            </div>

            {/* 3. Quizzes Completed */}
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <Award size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{overall.quizzes_completed}</div>
                <div className="stat-label">Quizzes Passed (≥70%)</div>
              </div>
            </div>

            {/* 4. Average Quiz Score */}
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <Sparkles size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{overall.average_score}%</div>
                <div className="stat-label">Average Quiz Score</div>
              </div>
            </div>

            {/* 5. Learning Streak */}
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
                <Flame size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{overall.streak_days} <span style={{ fontSize: '13px', color: 'var(--amber)' }}>Days</span></div>
                <div className="stat-label">Active Streak 🔥</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ==========================================
          LATEST GOVERNMENT EXAMS UPDATES (Requirement 18)
          ========================================== */}
      <section style={{ marginBottom: '48px' }}>
        <div className="section-header">
          <div>
            <h2 className="section-title">
              <span>Government Exam Updates</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14px', marginTop: '4px' }}>
              Latest verified recruitment and examination announcements from official government commissions.
            </p>
          </div>
          <button 
            className="btn btn-secondary"
            onClick={() => navigateTo('government-exams')}
            style={{ fontSize: '13px', gap: '6px' }}
          >
            <span>View All Updates →</span>
          </button>
        </div>

        {latestGovtExams.length === 0 ? (
          <div className="glass-card" style={{ padding: '32px 24px', textAlign: 'center' }}>
            <Building2 size={32} color="var(--cyan)" style={{ margin: '0 auto 10px' }} />
            <h4 style={{ fontSize: '15px', fontWeight: 600, color: '#f8fafc', marginBottom: '4px' }}>
              No verified government exam updates available right now.
            </h4>
            <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginBottom: '14px' }}>
              New updates will appear here once verified against official gazette notifications.
            </p>
            <button 
              className="btn btn-secondary" 
              onClick={() => navigateTo('government-exams')}
              style={{ fontSize: '12.5px' }}
            >
              Browse Government Exams Section →
            </button>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px' }}>
            {latestGovtExams.map((exam, idx) => (
              <div 
                key={exam.id}
                className="glass-card"
                style={{ padding: '20px', cursor: 'pointer', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transition: 'transform 0.15s ease' }}
                onClick={() => navigateTo('government-exams', { examId: exam.id })}
                onMouseEnter={e => e.currentTarget.style.transform = 'translateY(-2px)'}
                onMouseLeave={e => e.currentTarget.style.transform = 'translateY(0)'}
              >
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                    <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--cyan)' }}>
                      {exam.organization}
                    </span>
                    <span className={`badge ${exam.dynamic_status?.badge_class || 'badge-primary'}`} style={{ fontSize: '11px', padding: '2px 8px' }}>
                      {exam.dynamic_status?.status_label || 'Notice'}
                    </span>
                  </div>
                  <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#f8fafc', marginBottom: '6px', lineHeight: 1.35 }}>
                    {idx + 1}. {exam.exam_name}
                  </h4>
                  <p style={{ fontSize: '13px', color: 'var(--text-secondary)', lineHeight: 1.5, marginBottom: '12px' }}>
                    {exam.short_description || exam.title}
                  </p>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid var(--border-subtle)', paddingTop: '10px', fontSize: '12.5px', color: 'var(--cyan)', fontWeight: 600 }}>
                  <span>View Details</span>
                  <ArrowRight size={14} />
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* ==========================================
          COURSE SECTION (6 CORE COURSES)
          ========================================== */}
      <section style={{ marginBottom: '48px' }}>
        <div className="section-header">
          <div>
            <h2 className="section-title">
              <span>Structured Courses & Learning Paths</span>
            </h2>
            <p style={{ color: 'var(--text-secondary)', fontSize: '14px', marginTop: '4px' }}>
              Select a subject to access its sequential milestone roadmap and unlock your next level.
            </p>
          </div>
          <div className="badge badge-primary">
            <ShieldCheck size={14} />
            All Syllabi Aligned with SSC, UPSC & Banking
          </div>
        </div>

        <div className="courses-grid">
          {courses.map(course => {
            const IconComponent = iconMap[course.icon] || BookOpen;
            return (
              <div 
                key={course.id} 
                className="course-card"
                onClick={() => navigateTo('course', { slug: course.slug })}
                style={{ cursor: 'pointer' }}
              >
                <div className="course-header">
                  <div className="course-icon-wrap">
                    <IconComponent size={24} />
                  </div>
                  <span className="course-badge">
                    {course.category}
                  </span>
                </div>

                <h3 className="course-title">{course.title}</h3>
                <p className="course-desc">{course.description}</p>

                <div className="course-footer">
                  <div className="course-meta">
                    <span>{course.topics_count} Topics</span>
                    <span style={{ fontWeight: 700, color: course.completion_percentage > 0 ? 'var(--emerald)' : 'var(--text-muted)' }}>
                      {course.completion_percentage}% Completed
                    </span>
                  </div>

                  <div className="progress-bar-container">
                    <div 
                      className={`progress-bar-fill ${course.completion_percentage > 0 ? 'emerald' : ''}`}
                      style={{ width: `${Math.max(course.completion_percentage, 5)}%` }}
                    />
                  </div>

                  <button className="course-action-btn">
                    <span>Continue</span>
                    <ArrowRight size={16} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* ==========================================
          CORE HIGHLIGHT: UNLOCK SYSTEM SHOWCASE
          ========================================== */}
      <section style={{
        padding: '28px 32px',
        borderRadius: 'var(--radius-lg)',
        background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(6, 182, 212, 0.04) 100%)',
        border: '1px solid var(--border-glow)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '24px'
      }}>
        <div style={{ maxWidth: '640px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
            <span className="badge badge-cyan">Core Learning Engine</span>
            <span className="badge badge-amber">Passing Requirement: 70%</span>
          </div>
          <h3 style={{ fontSize: '20px', fontWeight: 700, marginBottom: '8px' }}>
            Sequential Topic Progression & Real Backend Unlock
          </h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', lineHeight: 1.6 }}>
            In Skillexa, every topic is an unlockable level. Start with <strong>Noun</strong>, practice verified SSC CGL previous year questions, and pass the topic quiz with at least 70% to automatically unlock <strong>Pronoun</strong> and proceed along the path.
          </p>
        </div>

        <div>
          <button 
            className="btn btn-primary"
            onClick={() => navigateTo('topic', { id: 1 })}
          >
            <Unlock size={16} />
            <span>Open Level 1: Noun</span>
          </button>
        </div>
      </section>
    </div>
  );
}
