import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Search, 
  Bell, 
  Flame, 
  CheckCircle, 
  FileText, 
  ShieldCheck, 
  BarChart3, 
  Menu, 
  X, 
  Compass, 
  Award,
  ExternalLink,
  Check,
  Building2
} from 'lucide-react';

export default function Header({ currentView, navigateTo, onOpenSearch }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [showNotifications, setShowNotifications] = useState(false);
  const [notifications, setNotifications] = useState([]);
  const [unreadCount, setUnreadCount] = useState(0);
  const [userRole, setUserRole] = useState(() => localStorage.getItem('skillexa_user_role') || 'admin');

  useEffect(() => {
    const handleRoleChanged = () => {
      setUserRole(localStorage.getItem('skillexa_user_role') || 'admin');
    };
    window.addEventListener('skillexa_role_changed', handleRoleChanged);
    return () => window.removeEventListener('skillexa_role_changed', handleRoleChanged);
  }, []);

  const toggleUserRole = () => {
    const newRole = userRole === 'admin' ? 'user' : 'admin';
    setUserRole(newRole);
    localStorage.setItem('skillexa_user_role', newRole);
    window.dispatchEvent(new Event('skillexa_role_changed'));
    if (newRole !== 'admin' && currentView === 'admin') {
      navigateTo('home');
    }
  };

  useEffect(() => {
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 10000);
    return () => clearInterval(interval);
  }, []);

  const fetchNotifications = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/notifications');
      if (res.ok) {
        const data = await res.json();
        setNotifications(data.data || []);
        setUnreadCount(data.unread_count || 0);
      }
    } catch (err) {
      console.error('Error fetching notifications:', err);
    }
  };

  const handleNotificationClick = async (notif) => {
    try {
      if (!notif.is_read) {
        await fetch(`http://localhost:3001/api/notifications/${notif.id}/read`, { method: 'PATCH' });
      }
      setShowNotifications(false);
      fetchNotifications();
      
      // Navigate to Government Exam detail if linked
      if (notif.update_id) {
        navigateTo('government-exams', { examId: notif.update_id });
      } else {
        navigateTo('government-exams');
      }
    } catch (err) {
      console.error('Error handling notification click:', err);
    }
  };

  const handleMarkAllRead = async () => {
    try {
      await fetch('http://localhost:3001/api/notifications/mark-all-read', { method: 'POST' });
      fetchNotifications();
    } catch (err) {
      console.error(err);
    }
  };

  // Check if there are any unread government exam notifications
  const hasUnreadGovtExams = notifications.some(n => !n.is_read && (
    n.notification_type === 'EXAM_NOTIFICATION' ||
    n.notification_type === 'APPLICATION_OPEN' ||
    n.notification_type === 'APPLICATION_CLOSING' ||
    n.notification_type === 'ADMIT_CARD' ||
    n.notification_type === 'EXAM_DATE' ||
    n.notification_type === 'ANSWER_KEY' ||
    n.notification_type === 'RESULT' ||
    n.notification_type === 'JOB_NOTIFICATION' ||
    n.update_id
  ));

  return (
    <header className="app-header">
      <div className="header-inner">
        {/* Brand Logo */}
        <div 
          className="logo-group" 
          onClick={() => { navigateTo('home'); setMobileMenuOpen(false); }}
          style={{ cursor: 'pointer' }}
        >
          <div className="logo-icon">
            <svg width="24" height="24" viewBox="0 0 32 32" fill="none">
              <path d="M7 23L16 9L25 23M16 13V23" stroke="#06B6D4" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
              <circle cx="16" cy="7" r="2.5" fill="#6366F1" />
            </svg>
          </div>
          <div className="logo-text-wrap">
            <span className="logo-title">
              Skillexa<span style={{ color: 'var(--cyan)' }}>.</span>
            </span>
            <span className="logo-tagline">Learn • Practice • Grow</span>
          </div>
        </div>

        {/* Desktop Navigation */}
        <nav className="nav-links">
          <button 
            className={`nav-link ${currentView === 'home' ? 'active' : ''}`}
            onClick={() => navigateTo('home')}
          >
            <Compass size={16} />
            <span>Home</span>
          </button>
          
          <button 
            className={`nav-link ${currentView === 'course' || currentView === 'courses' ? 'active' : ''}`}
            onClick={() => navigateTo('course', { slug: 'english' })}
          >
            <BookOpen size={16} />
            <span>Courses</span>
          </button>

          {/* Government Exams Nav with Unread Badge Indicator */}
          <button 
            className={`nav-link ${currentView === 'government-exams' ? 'active' : ''}`}
            onClick={() => navigateTo('government-exams')}
            style={{ position: 'relative' }}
          >
            <Building2 size={16} />
            <span>Gov Exams</span>
            {hasUnreadGovtExams && (
              <span 
                style={{
                  display: 'inline-block',
                  width: '7px',
                  height: '7px',
                  borderRadius: '50%',
                  background: 'var(--rose)',
                  boxShadow: '0 0 6px var(--rose)',
                  marginLeft: '2px'
                }}
                title="Unread government exam updates available"
              />
            )}
          </button>

          {/* Notes Top-Level Option */}
          <button 
            className={`nav-link ${currentView === 'notes' ? 'active' : ''}`}
            onClick={() => navigateTo('notes')}
          >
            <FileText size={16} />
            <span>Notes</span>
          </button>

          <button 
            className={`nav-link ${currentView === 'current-affairs' ? 'active' : ''}`}
            onClick={() => navigateTo('current-affairs')}
          >
            <Award size={16} />
            <span>Current Affairs</span>
          </button>

          <button 
            className={`nav-link ${currentView === 'overall-quiz' ? 'active' : ''}`}
            onClick={() => navigateTo('overall-quiz')}
          >
            <CheckCircle size={16} />
            <span>Mock Exam</span>
          </button>

          <button 
            className={`nav-link ${currentView === 'profile' || currentView === 'progress' ? 'active' : ''}`}
            onClick={() => navigateTo('profile')}
          >
            <BarChart3 size={16} />
            <span>Profile & Progress</span>
          </button>

          {userRole === 'admin' && (
            <button 
              className={`nav-link ${currentView === 'admin' ? 'active' : ''}`}
              onClick={() => navigateTo('admin')}
              style={{ color: '#a5b4fc' }}
            >
              <ShieldCheck size={16} />
              <span>Admin</span>
            </button>
          )}
        </nav>

        {/* Actions & Profile */}
        <div className="header-actions">
          {/* Search Trigger */}
          <button 
            className="btn-icon" 
            onClick={onOpenSearch} 
            title="Search topics & exams (Cmd/Ctrl + K)"
            aria-label="Search"
          >
            <Search size={18} />
          </button>

          {/* Notifications Trigger */}
          <div style={{ position: 'relative' }}>
            <button 
              className="btn-icon" 
              onClick={() => setShowNotifications(!showNotifications)} 
              title="Notifications"
              aria-label="Notifications"
            >
              <Bell size={18} />
              {unreadCount > 0 && (
                <span style={{
                  position: 'absolute',
                  top: '6px',
                  right: '6px',
                  minWidth: '15px',
                  height: '15px',
                  padding: '0 4px',
                  borderRadius: '10px',
                  background: 'var(--rose)',
                  color: '#fff',
                  fontSize: '10px',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: '0 0 6px rgba(244, 63, 94, 0.6)'
                }}>
                  {unreadCount > 9 ? '9+' : unreadCount}
                </span>
              )}
            </button>

            {/* Live Notification Dropdown */}
            {showNotifications && (
              <div style={{
                position: 'absolute',
                top: 'calc(100% + 12px)',
                right: '0',
                width: '340px',
                maxHeight: '440px',
                overflowY: 'auto',
                background: 'var(--bg-dark)',
                border: '1px solid var(--border-light)',
                borderRadius: 'var(--radius-lg)',
                boxShadow: 'var(--shadow-lg)',
                padding: '16px',
                zIndex: 150
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '8px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h4 style={{ fontSize: '14px', fontWeight: 700, color: '#fff' }}>Notifications</h4>
                    {unreadCount > 0 && (
                      <span className="badge badge-rose" style={{ fontSize: '11px', padding: '1px 6px' }}>
                        {unreadCount} New
                      </span>
                    )}
                  </div>
                  {unreadCount > 0 && (
                    <button 
                      onClick={handleMarkAllRead}
                      style={{ background: 'transparent', border: 'none', color: 'var(--cyan)', fontSize: '11.5px', cursor: 'pointer' }}
                    >
                      Mark all as read
                    </button>
                  )}
                </div>

                {notifications.length === 0 ? (
                  <div style={{ padding: '24px 12px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
                    You're all caught up!
                  </div>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {notifications.map(n => (
                      <div 
                        key={n.id} 
                        onClick={() => handleNotificationClick(n)}
                        style={{
                          padding: '10px 12px',
                          background: n.is_read ? 'rgba(255, 255, 255, 0.02)' : 'rgba(99, 102, 241, 0.08)',
                          borderRadius: 'var(--radius-sm)',
                          borderLeft: n.is_read ? '3px solid var(--border-subtle)' : '3px solid var(--cyan)',
                          fontSize: '12.5px',
                          cursor: 'pointer',
                          transition: 'background 0.15s ease'
                        }}
                        onMouseEnter={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.06)'}
                        onMouseLeave={e => e.currentTarget.style.background = n.is_read ? 'rgba(255, 255, 255, 0.02)' : 'rgba(99, 102, 241, 0.08)'}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '2px' }}>
                          <span style={{ fontWeight: 600, color: '#f8fafc' }}>{n.title}</span>
                          {!n.is_read && (
                            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: 'var(--cyan)' }} />
                          )}
                        </div>
                        <div style={{ color: 'var(--text-secondary)', fontSize: '12px', lineHeight: 1.4 }}>
                          {n.message}
                        </div>
                        <div style={{ color: 'var(--text-muted)', fontSize: '11px', marginTop: '4px' }}>
                          {new Date(n.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} • Tap to view details →
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Learning Streak Badge */}
          <div 
            className="streak-pill" 
            title="7-Day Active Learning Streak"
            onClick={() => navigateTo('profile')}
            style={{ cursor: 'pointer' }}
          >
            <Flame size={16} color="#f59e0b" fill="#f59e0b" />
            <span>7 Days</span>
          </div>

          {/* Role Indicator & Testing Switcher */}
          <button
            onClick={toggleUserRole}
            style={{
              background: userRole === 'admin' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(16, 185, 129, 0.12)',
              border: userRole === 'admin' ? '1px solid rgba(99, 102, 241, 0.35)' : '1px solid rgba(16, 185, 129, 0.3)',
              color: userRole === 'admin' ? '#c7d2fe' : 'var(--emerald)',
              cursor: 'pointer',
              padding: '5px 10px',
              fontSize: '11px',
              fontWeight: 700,
              borderRadius: '16px',
              display: 'flex',
              alignItems: 'center',
              gap: '5px'
            }}
            title="Click to toggle between Admin and Student role to test access permissions"
          >
            <span>{userRole === 'admin' ? '🛡️ Admin Role' : '👤 Student Role'}</span>
          </button>

          {/* User Profile Pill */}
          <div 
            style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}
            onClick={() => navigateTo('profile')}
            title="View & Edit Profile & Settings"
          >
            <img 
              src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80" 
              alt="Ganesh Kumar" 
              className="user-avatar"
            />
          </div>

          {/* Mobile Menu Toggle */}
          <button 
            className="btn-icon"
            style={{ display: 'none' }}
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle mobile menu"
          >
            {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>
      </div>
    </header>
  );
}
