import React, { useState, useEffect } from 'react';
import { 
  Flame, 
  Award, 
  CheckCircle2, 
  TrendingUp, 
  Clock, 
  RotateCcw, 
  BookOpen, 
  ArrowRight,
  ShieldCheck,
  Calendar
} from 'lucide-react';

export default function ProgressAnalyticsPage({ navigateTo }) {
  const [progressData, setProgressData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProgress();
  }, []);

  const fetchProgress = async () => {
    try {
      setLoading(true);
      const res = await fetch('http://localhost:3001/api/user/progress');
      const data = await res.json();
      setProgressData(data);
    } catch (err) {
      console.error('Error fetching progress:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    if (window.confirm('Reset all progress back to default seed to test unlocking from Level 1?')) {
      await fetch('http://localhost:3001/api/user/progress/reset', { method: 'POST' });
      fetchProgress();
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '80px 20px', color: 'var(--text-secondary)' }}>
        <div>Loading your learning performance...</div>
      </div>
    );
  }

  const { user, overall = {}, course_breakdown = [], recent_attempts = [] } = progressData || {};

  return (
    <div>
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
              <span className="badge badge-cyan">
                <Flame size={14} color="#f59e0b" fill="#f59e0b" />
                {overall.streak_days} Day Learning Streak
              </span>
            </div>
            <h1 style={{ fontSize: '32px', fontWeight: 800 }}>User Learning Performance</h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '15px', marginTop: '4px' }}>
              Real-time synchronization with the Skillexa adaptive milestone engine.
            </p>
          </div>

          <button 
            className="btn btn-secondary"
            onClick={handleReset}
            style={{ fontSize: '13px' }}
          >
            <RotateCcw size={14} />
            <span>Reset Demo Progress</span>
          </button>
        </div>

        {/* User Card */}
        <div className="glass-card" style={{ padding: '24px', marginTop: '24px', display: 'flex', alignItems: 'center', gap: '20px', flexWrap: 'wrap' }}>
          <img 
            src={user?.avatar || "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80"} 
            alt={user?.name || "Student"} 
            style={{ width: '64px', height: '64px', borderRadius: '50%', border: '2px solid var(--border-glow)' }}
          />
          <div style={{ flex: 1 }}>
            <h3 style={{ fontSize: '20px', fontWeight: 700, color: '#ffffff' }}>{user?.name || "Ganesh Kumar"}</h3>
            <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>{user?.email || "ganesh@skillexa.edu"} • Candidate for SSC CGL & UPSC CDS</div>
            <div style={{ display: 'flex', gap: '8px', marginTop: '8px' }}>
              <span className="badge badge-primary">Rank: Aspirant Level 2</span>
              <span className="badge badge-emerald">Passing Threshold: 70%</span>
            </div>
          </div>
        </div>

        {/* 4 Stats Cards */}
        <div className="stats-grid" style={{ marginTop: '20px' }}>
          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
              <TrendingUp size={22} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{overall.completion_percentage}%</div>
              <div className="stat-label">Syllabus Completion</div>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
              <CheckCircle2 size={22} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{overall.topics_completed} <span style={{ fontSize: '14px', color: 'var(--text-muted)' }}>/ {overall.total_topics}</span></div>
              <div className="stat-label">Topics Mastered</div>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
              <Award size={22} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{overall.quizzes_completed} <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>/ {overall.total_attempts}</span></div>
              <div className="stat-label">Quizzes Passed</div>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
              <Award size={22} />
            </div>
            <div className="stat-info">
              <div className="stat-value">{overall.average_score}%</div>
              <div className="stat-label">Average Accuracy</div>
            </div>
          </div>
        </div>
      </div>

      {/* Subject-Wise Mastery Grid */}
      <div style={{ marginBottom: '36px' }}>
        <h3 style={{ fontSize: '20px', fontWeight: 700, marginBottom: '16px' }}>
          Course-by-Course Mastery Breakdown
        </h3>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '16px' }}>
          {course_breakdown.map(course => (
            <div 
              key={course.course_id}
              className="glass-card" 
              style={{ padding: '20px', cursor: 'pointer' }}
              onClick={() => navigateTo('course', { slug: course.slug })}
            >
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#f8fafc' }}>{course.title}</h4>
                <span style={{ fontSize: '13px', fontWeight: 700, color: course.percentage > 0 ? 'var(--emerald)' : 'var(--text-muted)' }}>
                  {course.percentage}%
                </span>
              </div>

              <div className="progress-bar-container" style={{ marginBottom: '12px' }}>
                <div 
                  className={`progress-bar-fill ${course.percentage > 0 ? 'emerald' : ''}`}
                  style={{ width: `${Math.max(course.percentage, 5)}%` }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', color: 'var(--text-secondary)' }}>
                <span>{course.completed_topics} of {course.total_topics} Topics Completed</span>
                <span style={{ color: 'var(--cyan)' }}>Open Pathway →</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Recent Quiz Attempts Log */}
      <div className="glass-card" style={{ padding: '24px' }}>
        <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>
          Recent Quiz Attempts & Verification Log
        </h3>

        {recent_attempts.length === 0 ? (
          <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>
            No quizzes completed yet. Complete the <strong>Noun Quiz</strong> to log your first attempt!
          </div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table className="admin-table">
              <thead>
                <tr>
                  <th>Topic</th>
                  <th>Score</th>
                  <th>Percentage</th>
                  <th>Result</th>
                  <th>Time Taken</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {recent_attempts.map(attempt => (
                  <tr key={attempt.id}>
                    <td style={{ fontWeight: 600, color: '#f8fafc' }}>{attempt.topic_title}</td>
                    <td>{attempt.score} / {attempt.total}</td>
                    <td><strong>{attempt.percentage}%</strong></td>
                    <td>
                      {attempt.passed ? (
                        <span className="badge badge-emerald">PASSED ✓</span>
                      ) : (
                        <span className="badge" style={{ background: 'rgba(244, 63, 94, 0.15)', color: '#fda4af' }}>FAILED</span>
                      )}
                    </td>
                    <td style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>
                      {attempt.time_spent_seconds}s
                    </td>
                    <td style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                      {new Date(attempt.created_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
