import React, { useState, useEffect } from 'react';
import { 
  Check, 
  Lock, 
  Unlock, 
  ArrowLeft, 
  ArrowRight, 
  Award, 
  BookOpen, 
  HelpCircle, 
  Sparkles,
  ChevronRight,
  Clock,
  RotateCcw
} from 'lucide-react';

export default function CourseRoadmapPage({ slug = 'english', navigateTo }) {
  const [courseData, setCourseData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeModuleFilter, setActiveModuleFilter] = useState('all');

  useEffect(() => {
    fetchCourseRoadmap();
  }, [slug]);

  const fetchCourseRoadmap = async () => {
    try {
      setLoading(true);
      const res = await fetch(`http://localhost:3001/api/courses/${slug}`);
      const data = await res.json();
      setCourseData(data);
    } catch (err) {
      console.error('Error fetching course roadmap:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    if (window.confirm('Reset progress back to default seed?')) {
      await fetch('http://localhost:3001/api/user/progress/reset', { method: 'POST' });
      fetchCourseRoadmap();
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '80px 20px', color: 'var(--text-secondary)' }}>
        <Sparkles size={32} className="spin" color="var(--cyan)" style={{ marginBottom: '16px' }} />
        <h3>Loading Course Pathway...</h3>
      </div>
    );
  }

  if (!courseData || courseData.error) {
    return (
      <div style={{ textAlign: 'center', padding: '60px 20px' }}>
        <h3>Course not found</h3>
        <button className="btn btn-primary" onClick={() => navigateTo('home')} style={{ marginTop: '16px' }}>
          Back to Home
        </button>
      </div>
    );
  }

  const { title, description, modules = [], topics = [], completed_topics_count = 0, total_topics_count = 0, completion_percentage = 0 } = courseData;

  const filteredTopics = activeModuleFilter === 'all'
    ? topics
    : topics.filter(t => String(t.module_id) === String(activeModuleFilter));

  return (
    <div className="roadmap-container">
      {/* Back Button & Breadcrumbs */}
      <div>
        <button 
          className="btn btn-subtle"
          onClick={() => navigateTo('home')}
          style={{ marginBottom: '16px', paddingLeft: 0 }}
        >
          <ArrowLeft size={16} />
          <span>Back to Courses</span>
        </button>

        <div className="breadcrumb">
          <span onClick={() => navigateTo('home')} style={{ cursor: 'pointer' }}>Home</span>
          <ChevronRight size={14} />
          <span onClick={() => navigateTo('home')} style={{ cursor: 'pointer' }}>Courses</span>
          <ChevronRight size={14} />
          <span className="breadcrumb-active">{title}</span>
        </div>
      </div>

      {/* Course Header & Progress Status */}
      <div className="roadmap-header">
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', flexWrap: 'wrap', gap: '20px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
              <h1 style={{ fontSize: '28px', fontWeight: 800 }}>{title}</h1>
              <span className="badge badge-cyan">{courseData.category}</span>
            </div>
            <p style={{ color: 'var(--text-secondary)', fontSize: '15px', maxWidth: '700px', lineHeight: 1.5 }}>
              {description}
            </p>
          </div>

          <div style={{
            padding: '16px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(13, 21, 39, 0.8)',
            border: '1px solid var(--border-subtle)',
            minWidth: '220px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
              <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>Progress</span>
              <span style={{ fontWeight: 700, color: completion_percentage > 0 ? 'var(--emerald)' : 'var(--text-secondary)' }}>
                {completion_percentage}%
              </span>
            </div>
            <div className="progress-bar-container" style={{ marginBottom: '8px' }}>
              <div 
                className={`progress-bar-fill ${completion_percentage > 0 ? 'emerald' : ''}`}
                style={{ width: `${Math.max(completion_percentage, 5)}%` }}
              />
            </div>
            <div style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
              <strong>{completed_topics_count}</strong> of <strong>{total_topics_count}</strong> Topics Completed
            </div>
          </div>
        </div>

        {/* Module Filter Tabs */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '24px', flexWrap: 'wrap' }}>
          <button 
            className={`btn ${activeModuleFilter === 'all' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveModuleFilter('all')}
            style={{ fontSize: '13px', padding: '6px 14px' }}
          >
            All Modules ({topics.length})
          </button>
          {modules.map(mod => (
            <button 
              key={mod.id}
              className={`btn ${activeModuleFilter === String(mod.id) ? 'btn-primary' : 'btn-secondary'}`}
              onClick={() => setActiveModuleFilter(String(mod.id))}
              style={{ fontSize: '13px', padding: '6px 14px' }}
            >
              {mod.title}
            </button>
          ))}
        </div>
      </div>

      {/* Unlock Notice Banner */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '14px 20px',
        borderRadius: 'var(--radius-md)',
        background: 'rgba(99, 102, 241, 0.08)',
        border: '1px solid rgba(99, 102, 241, 0.25)',
        fontSize: '13px',
        color: 'var(--text-secondary)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Sparkles size={18} color="var(--cyan)" />
          <span>
            <strong>Sequential Unlock Rule:</strong> Score at least <strong>70%</strong> on the current topic quiz to unlock the next level.
          </span>
        </div>
        <button 
          onClick={handleReset} 
          className="btn btn-subtle" 
          style={{ fontSize: '12px', padding: '4px 8px', gap: '4px' }}
          title="Reset progress to test unlocking from Level 1"
        >
          <RotateCcw size={12} />
          Reset Demo
        </button>
      </div>

      {/* ==========================================
          TOPICS BOX / CARD GRID
          ========================================== */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))',
        gap: '18px',
        marginTop: '24px'
      }}>
        {filteredTopics.map((topic, index) => {
          const isCompleted = topic.status === 'completed';
          const isUnlocked = topic.status === 'unlocked';
          const isLocked = topic.status === 'locked';

          return (
            <div 
              key={topic.id}
              onClick={() => {
                if (!isLocked) {
                  navigateTo('topic', { id: topic.id });
                }
              }}
              style={{
                background: isCompleted ? 'rgba(16, 185, 129, 0.05)' : isUnlocked ? 'rgba(56, 189, 248, 0.05)' : 'var(--bg-card)',
                border: isCompleted 
                  ? '1.5px solid rgba(16, 185, 129, 0.4)' 
                  : isUnlocked 
                  ? '1.5px solid rgba(56, 189, 248, 0.45)' 
                  : '1px solid var(--border-color)',
                borderRadius: '14px',
                padding: '18px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                minHeight: '160px',
                cursor: isLocked ? 'not-allowed' : 'pointer',
                opacity: isLocked ? 0.75 : 1,
                transition: 'all 0.2s ease',
                boxShadow: isUnlocked ? '0 4px 16px rgba(56, 189, 248, 0.12)' : '0 4px 12px rgba(0,0,0,0.12)'
              }}
            >
              <div>
                {/* Header: Topic N */}
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                    Topic {topic.order_index || index + 1}
                  </span>
                  {isCompleted ? (
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '11px', fontWeight: 700, color: '#34d399', background: 'rgba(52, 211, 153, 0.12)', padding: '3px 8px', borderRadius: '6px' }}>
                      <Check size={12} />
                      COMPLETED ✓
                    </span>
                  ) : isUnlocked ? (
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '11px', fontWeight: 700, color: '#38bdf8', background: 'rgba(56, 189, 248, 0.12)', padding: '3px 8px', borderRadius: '6px' }}>
                      <Unlock size={12} />
                      UNLOCKED
                    </span>
                  ) : (
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '11px', fontWeight: 600, color: 'var(--text-muted)', background: 'rgba(255, 255, 255, 0.04)', padding: '3px 8px', borderRadius: '6px' }}>
                      <Lock size={12} />
                      LOCKED 🔒
                    </span>
                  )}
                </div>

                {/* Topic Name */}
                <h3 style={{ fontSize: '17px', fontWeight: 700, color: isLocked ? 'var(--text-muted)' : '#ffffff', marginBottom: '6px' }}>
                  {topic.title}
                </h3>

                {/* Short Description */}
                <p style={{ color: 'var(--text-secondary)', fontSize: '12.5px', lineHeight: 1.45, margin: 0 }}>
                  {topic.description}
                </p>
              </div>

              {/* Card Footer: Status & Action */}
              <div style={{ marginTop: '14px', paddingTop: '10px', borderTop: '1px solid rgba(255, 255, 255, 0.05)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span style={{ fontSize: '12px', color: isCompleted ? '#34d399' : 'var(--text-muted)' }}>
                  {isCompleted ? `Score: ${topic.best_score || 80}%` : isUnlocked ? 'Ready to Learn' : 'Locked'}
                </span>
                {!isLocked && (
                  <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--cyan)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    {isCompleted ? 'Review' : 'Start'} <ArrowRight size={13} />
                  </span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
