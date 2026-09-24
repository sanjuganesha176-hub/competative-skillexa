import React, { useState, useEffect } from 'react';
import { 
  User, 
  Flame, 
  Award, 
  CheckCircle2, 
  TrendingUp, 
  Bell, 
  Settings, 
  Save, 
  ShieldCheck, 
  BookOpen, 
  Calendar, 
  Smartphone, 
  MapPin, 
  GraduationCap, 
  Mail, 
  FileText,
  RotateCcw,
  Check
} from 'lucide-react';

export default function ProfilePage({ navigateTo }) {
  const [activeTab, setActiveTab] = useState('profile'); // 'profile' | 'notifications' | 'progress'
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  // Profile Form State
  const [profileForm, setProfileForm] = useState({
    name: '',
    email: '',
    phone: '',
    state: '',
    education: '',
    bio: '',
    target_exams: []
  });

  // Notification Preferences State
  const [notificationPrefs, setNotificationPrefs] = useState({
    exam_notifications: true,
    application_updates: true,
    admit_card_updates: true,
    exam_date_updates: true,
    answer_key_updates: true,
    result_updates: true,
    job_notifications: true,
    category_preferences: ['SSC', 'UPSC', 'Railway', 'Banking', 'KPSC', 'Defence', 'Teaching', 'Police']
  });

  const availableTargetExams = [
    'SSC CGL',
    'SSC CHSL',
    'UPSC CSE',
    'UPSC CDS',
    'UPSC NDA',
    'Railway RRB NTPC',
    'IBPS PO / Clerk',
    'SBI PO',
    'KPSC KAS',
    'Karnataka Police SI',
    'State TET / CTET',
    'AFCAT / Defence'
  ];

  const categoryOptions = [
    'SSC',
    'UPSC',
    'Railway',
    'Banking',
    'KPSC',
    'Defence',
    'Teaching',
    'Police'
  ];

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      setLoading(true);
      const res = await fetch('http://localhost:3001/api/user/profile');
      if (res.ok) {
        const data = await res.json();
        setProfileData(data);
        if (data.user) {
          setProfileForm({
            name: data.user.name || '',
            email: data.user.email || '',
            phone: data.user.phone || '',
            state: data.user.state || 'Karnataka',
            education: data.user.education || '',
            bio: data.user.bio || '',
            target_exams: data.user.target_exams || []
          });
        }
        if (data.notification_preferences) {
          setNotificationPrefs(data.notification_preferences);
        }
      }
    } catch (err) {
      console.error('Error loading profile:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    try {
      setSaving(true);
      setSaveSuccess(false);
      const res = await fetch('http://localhost:3001/api/user/profile', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(profileForm)
      });
      if (res.ok) {
        setSaveSuccess(true);
        setTimeout(() => setSaveSuccess(false), 3000);
        fetchProfile();
      }
    } catch (err) {
      console.error('Error updating profile:', err);
    } finally {
      setSaving(false);
    }
  };

  const handleSavePreferences = async () => {
    try {
      setSaving(true);
      setSaveSuccess(false);
      const res = await fetch('http://localhost:3001/api/notification-preferences', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(notificationPrefs)
      });
      if (res.ok) {
        setSaveSuccess(true);
        setTimeout(() => setSaveSuccess(false), 3000);
      }
    } catch (err) {
      console.error('Error saving notification preferences:', err);
    } finally {
      setSaving(false);
    }
  };

  const handleToggleTargetExam = (exam) => {
    setProfileForm(prev => {
      const exists = prev.target_exams.includes(exam);
      return {
        ...prev,
        target_exams: exists 
          ? prev.target_exams.filter(e => e !== exam)
          : [...prev.target_exams, exam]
      };
    });
  };

  const handleToggleCategoryPref = (cat) => {
    setNotificationPrefs(prev => {
      const list = prev.category_preferences || [];
      const exists = list.includes(cat);
      return {
        ...prev,
        category_preferences: exists 
          ? list.filter(c => c !== cat)
          : [...list, cat]
      };
    });
  };

  const handleEnableBrowserPush = async () => {
    if ('Notification' in window) {
      try {
        const permission = await Notification.requestPermission();
        if (permission === 'granted') {
          // Register mock/token with backend
          await fetch('http://localhost:3001/api/notifications/token', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              push_token: `web-push-token-${Date.now()}`,
              platform: 'browser'
            })
          });
          new Notification('Skillexa Alerts Activated', {
            body: 'You will now receive instant verified government exam & deadline updates.',
            icon: '/favicon.ico'
          });
          alert('Browser notifications enabled successfully!');
        } else {
          alert('Browser notifications permission was not granted.');
        }
      } catch (err) {
        console.error(err);
      }
    } else {
      alert('Push notifications are not supported in this browser.');
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '80px 20px', color: 'var(--text-secondary)' }}>
        Loading user profile and settings...
      </div>
    );
  }

  const { user = {}, performance_summary = {} } = profileData || {};

  return (
    <div style={{ maxWidth: 'var(--max-width)', margin: '0 auto', paddingBottom: '60px' }}>
      
      {/* ==========================================
          PROFILE HEADER CARD
          ========================================== */}
      <div className="glass-card" style={{ padding: '28px', marginBottom: '28px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '20px' }}>
          
          <div style={{ display: 'flex', alignItems: 'center', gap: '22px' }}>
            <img 
              src={user.avatar || "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80"} 
              alt={user.name} 
              style={{
                width: '76px',
                height: '76px',
                borderRadius: '50%',
                border: '2px solid var(--border-glow)',
                objectFit: 'cover'
              }}
            />
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <h1 style={{ fontSize: '24px', fontWeight: 800, color: '#ffffff' }}>
                  {user.name}
                </h1>
                <span className="badge badge-primary" style={{ textTransform: 'capitalize' }}>
                  {user.role}
                </span>
              </div>
              <div style={{ fontSize: '13.5px', color: 'var(--text-secondary)', marginTop: '2px' }}>
                {user.email} • {user.state || 'Karnataka'}
              </div>

              {/* Target exams chips */}
              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', marginTop: '8px' }}>
                {(user.target_exams || []).map(exam => (
                  <span key={exam} className="badge badge-cyan" style={{ fontSize: '11px' }}>
                    {exam}
                  </span>
                ))}
              </div>
            </div>
          </div>

          {/* Quick Streak & Performance Badges */}
          <div style={{ display: 'flex', gap: '14px', alignItems: 'center' }}>
            <div style={{
              background: 'rgba(245, 158, 11, 0.1)',
              border: '1px solid rgba(245, 158, 11, 0.25)',
              borderRadius: 'var(--radius-md)',
              padding: '12px 18px',
              textAlign: 'center'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', justifyContent: 'center', color: '#f59e0b', fontWeight: 700, fontSize: '18px' }}>
                <Flame size={20} fill="#f59e0b" />
                <span>{user.streak_days || 7} Days</span>
              </div>
              <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                Learning Streak
              </div>
            </div>

            <div style={{
              background: 'rgba(6, 182, 212, 0.1)',
              border: '1px solid rgba(6, 182, 212, 0.25)',
              borderRadius: 'var(--radius-md)',
              padding: '12px 18px',
              textAlign: 'center'
            }}>
              <div style={{ color: 'var(--cyan)', fontWeight: 700, fontSize: '18px' }}>
                {performance_summary.completion_percentage || 0}%
              </div>
              <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '2px' }}>
                Syllabus Mastered
              </div>
            </div>
          </div>

        </div>

        {/* Tab Bar */}
        <div style={{ display: 'flex', gap: '8px', borderTop: '1px solid var(--border-subtle)', paddingTop: '20px', marginTop: '24px' }}>
          <button
            className={`btn ${activeTab === 'profile' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('profile')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <User size={15} />
            <span>Profile & Aspirations</span>
          </button>
          
          <button
            className={`btn ${activeTab === 'notifications' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('notifications')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Bell size={15} />
            <span>Gov Exam Notifications & Alerts</span>
          </button>

          <button
            className={`btn ${activeTab === 'progress' ? 'btn-primary' : 'btn-secondary'}`}
            onClick={() => setActiveTab('progress')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <TrendingUp size={15} />
            <span>Learning Analytics</span>
          </button>
        </div>
      </div>

      {/* Save Success Alert */}
      {saveSuccess && (
        <div style={{
          padding: '12px 20px',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(16, 185, 129, 0.15)',
          border: '1px solid var(--emerald)',
          color: 'var(--emerald)',
          fontSize: '13.5px',
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          marginBottom: '20px'
        }}>
          <CheckCircle2 size={16} />
          <span>Profile changes saved successfully!</span>
        </div>
      )}

      {/* ==========================================
          TAB 1: EDIT PROFILE & TARGET EXAMS
          ========================================== */}
      {activeTab === 'profile' && (
        <div className="glass-card" style={{ padding: '28px' }}>
          <div style={{ marginBottom: '24px' }}>
            <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#f8fafc' }}>
              Personal Details & Examination Aspirations
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginTop: '4px' }}>
              Keep your examination targets updated so Skillexa can prioritize relevant syllabus milestones and notifications.
            </p>
          </div>

          <form onSubmit={handleSaveProfile} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
              
              {/* Full Name */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  Full Name
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '10px 14px' }}>
                  <User size={16} color="var(--text-muted)" />
                  <input 
                    type="text" 
                    value={profileForm.name}
                    onChange={e => setProfileForm({ ...profileForm, name: e.target.value })}
                    style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', color: '#fff', fontSize: '14px' }}
                    required
                  />
                </div>
              </div>

              {/* Email */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  Email Address
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '10px 14px' }}>
                  <Mail size={16} color="var(--text-muted)" />
                  <input 
                    type="email" 
                    value={profileForm.email}
                    onChange={e => setProfileForm({ ...profileForm, email: e.target.value })}
                    style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', color: '#fff', fontSize: '14px' }}
                    required
                  />
                </div>
              </div>

              {/* Phone */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  Mobile / Phone Number
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '10px 14px' }}>
                  <Smartphone size={16} color="var(--text-muted)" />
                  <input 
                    type="tel" 
                    value={profileForm.phone}
                    onChange={e => setProfileForm({ ...profileForm, phone: e.target.value })}
                    style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', color: '#fff', fontSize: '14px' }}
                  />
                </div>
              </div>

              {/* State / Region */}
              <div>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  State / Jurisdiction
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '10px 14px' }}>
                  <MapPin size={16} color="var(--text-muted)" />
                  <input 
                    type="text" 
                    value={profileForm.state}
                    onChange={e => setProfileForm({ ...profileForm, state: e.target.value })}
                    style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', color: '#fff', fontSize: '14px' }}
                  />
                </div>
              </div>

              {/* Qualification */}
              <div style={{ gridColumn: '1 / -1' }}>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  Highest Educational Qualification
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-md)', padding: '10px 14px' }}>
                  <GraduationCap size={16} color="var(--text-muted)" />
                  <input 
                    type="text" 
                    value={profileForm.education}
                    onChange={e => setProfileForm({ ...profileForm, education: e.target.value })}
                    placeholder="e.g., Bachelor of Science (B.Sc), B.Tech, B.Com, Post Graduate"
                    style={{ flex: 1, background: 'transparent', border: 'none', outline: 'none', color: '#fff', fontSize: '14px' }}
                  />
                </div>
              </div>

              {/* Bio */}
              <div style={{ gridColumn: '1 / -1' }}>
                <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
                  Preparation Goal / Bio
                </label>
                <textarea 
                  rows={3}
                  value={profileForm.bio}
                  onChange={e => setProfileForm({ ...profileForm, bio: e.target.value })}
                  style={{
                    width: '100%',
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: 'var(--radius-md)',
                    padding: '10px 14px',
                    color: '#fff',
                    fontSize: '14px',
                    resize: 'vertical',
                    outline: 'none'
                  }}
                />
              </div>

            </div>

            {/* Target Exams Selector */}
            <div style={{ paddingTop: '10px' }}>
              <label style={{ display: 'block', fontSize: '13px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '10px' }}>
                Select Your Target Competitive Examinations
              </label>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {availableTargetExams.map(exam => {
                  const selected = profileForm.target_exams.includes(exam);
                  return (
                    <button
                      type="button"
                      key={exam}
                      onClick={() => handleToggleTargetExam(exam)}
                      style={{
                        padding: '7px 14px',
                        borderRadius: '20px',
                        fontSize: '12.5px',
                        fontWeight: 600,
                        border: selected ? '1px solid var(--cyan)' : '1px solid var(--border-subtle)',
                        background: selected ? 'rgba(6, 182, 212, 0.15)' : 'rgba(255, 255, 255, 0.03)',
                        color: selected ? '#ffffff' : 'var(--text-secondary)',
                        cursor: 'pointer',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      {selected && '✓ '}
                      {exam}
                    </button>
                  );
                })}
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '12px' }}>
              <button className="btn btn-primary" type="submit" disabled={saving}>
                <Save size={16} />
                <span>{saving ? 'Saving...' : 'Save Profile Changes'}</span>
              </button>
            </div>
          </form>
        </div>
      )}

      {/* ==========================================
          TAB 2: NOTIFICATION PREFERENCES & PUSH
          ========================================== */}
      {activeTab === 'notifications' && (
        <div className="glass-card" style={{ padding: '28px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px', marginBottom: '24px' }}>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#f8fafc' }}>
                Government Exam Push Notification Settings
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginTop: '4px' }}>
                Choose which types of alerts, examination boards, and reminders you want to receive.
              </p>
            </div>

            <button 
              className="btn btn-secondary" 
              onClick={handleEnableBrowserPush}
              style={{ fontSize: '13px', padding: '8px 16px' }}
            >
              <Smartphone size={15} color="var(--cyan)" />
              <span>Enable Browser Push</span>
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            
            {/* Update Types Toggles */}
            <div>
              <h4 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: '14px' }}>
                Notification Event Types
              </h4>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                {[
                  { key: 'exam_notifications', label: 'New Exam Notifications', desc: 'When new recruitment notices are announced' },
                  { key: 'application_updates', label: 'Application Started & Deadlines', desc: 'Forms opening and 2-day deadline reminders' },
                  { key: 'admit_card_updates', label: 'Admit Card Released', desc: 'Hall ticket and entry pass releases' },
                  { key: 'exam_date_updates', label: 'Exam Date Announced', desc: 'Confirmed examination scheduling' },
                  { key: 'answer_key_updates', label: 'Answer Key Released', desc: 'Provisional & final answer key updates' },
                  { key: 'result_updates', label: 'Results & Merit Lists', desc: 'Cut-off marks and official selections' },
                  { key: 'job_notifications', label: 'Government Job Recruitment', desc: 'Vacancies across central and state departments' }
                ].map(item => (
                  <div 
                    key={item.key} 
                    style={{
                      padding: '14px',
                      background: 'rgba(255, 255, 255, 0.02)',
                      border: '1px solid var(--border-subtle)',
                      borderRadius: 'var(--radius-sm)',
                      display: 'flex',
                      alignItems: 'flex-start',
                      gap: '12px',
                      cursor: 'pointer'
                    }}
                    onClick={() => setNotificationPrefs({ ...notificationPrefs, [item.key]: !notificationPrefs[item.key] })}
                  >
                    <input 
                      type="checkbox"
                      checked={!!notificationPrefs[item.key]}
                      onChange={() => {}}
                      style={{ accentColor: 'var(--cyan)', width: '18px', height: '18px', marginTop: '2px', cursor: 'pointer' }}
                    />
                    <div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{item.label}</div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px' }}>{item.desc}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Category Preferences */}
            <div>
              <h4 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: '14px' }}>
                Category Filter Preferences
              </h4>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginBottom: '12px' }}>
                Only receive notifications for examinations matching the categories you select:
              </p>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {categoryOptions.map(cat => {
                  const selected = (notificationPrefs.category_preferences || []).includes(cat);
                  return (
                    <button
                      type="button"
                      key={cat}
                      onClick={() => handleToggleCategoryPref(cat)}
                      style={{
                        padding: '7px 16px',
                        borderRadius: '20px',
                        fontSize: '13px',
                        fontWeight: 600,
                        border: selected ? '1px solid var(--cyan)' : '1px solid var(--border-subtle)',
                        background: selected ? 'rgba(6, 182, 212, 0.15)' : 'rgba(255, 255, 255, 0.03)',
                        color: selected ? '#ffffff' : 'var(--text-secondary)',
                        cursor: 'pointer',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      {selected && '✓ '}
                      {cat}
                    </button>
                  );
                })}
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '12px' }}>
              <button className="btn btn-primary" onClick={handleSavePreferences} disabled={saving}>
                <Save size={16} />
                <span>{saving ? 'Saving...' : 'Save Notification Preferences'}</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ==========================================
          TAB 3: LEARNING ANALYTICS
          ========================================== */}
      {activeTab === 'progress' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          
          {/* Performance Stats Cards */}
          <div className="stats-grid">
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <TrendingUp size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{performance_summary.completion_percentage || 0}%</div>
                <div className="stat-label">Syllabus Completion</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{performance_summary.completed_topics || 0} <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>/ {performance_summary.total_topics || 77}</span></div>
                <div className="stat-label">Topics Mastered</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <Award size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{performance_summary.quizzes_passed || 0} <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>/ {performance_summary.total_attempts || 0}</span></div>
                <div className="stat-label">Quizzes Passed (≥70%)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <Flame size={22} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{performance_summary.average_score || 0}%</div>
                <div className="stat-label">Average Score</div>
              </div>
            </div>
          </div>

          {/* Quick link back to roadmap */}
          <div className="glass-card" style={{ padding: '24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
            <div>
              <h4 style={{ fontSize: '16px', fontWeight: 700, color: '#f8fafc' }}>
                Full Course Milestone Roadmap
              </h4>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginTop: '4px' }}>
                Continue sequential topic unlocks across English, Mathematics, General Intelligence, and Sciences.
              </p>
            </div>
            <button 
              className="btn btn-primary"
              onClick={() => navigateTo('course', { slug: 'english' })}
            >
              <span>Resume Study</span>
            </button>
          </div>

        </div>
      )}

    </div>
  );
}
