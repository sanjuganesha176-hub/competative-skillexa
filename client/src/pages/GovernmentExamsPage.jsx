import React, { useState, useEffect } from 'react';
import { 
  Award, 
  Search, 
  Filter, 
  Calendar, 
  Clock, 
  ExternalLink, 
  ShieldCheck, 
  Building2, 
  Briefcase, 
  CheckCircle2, 
  AlertCircle, 
  Bell, 
  ChevronRight, 
  X, 
  RefreshCw, 
  SlidersHorizontal,
  ChevronDown,
  Info
} from 'lucide-react';

export default function GovernmentExamsPage({ navigateTo, viewExamId = null }) {
  const [exams, setExams] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [selectedType, setSelectedType] = useState('All');
  const [selectedStatus, setSelectedStatus] = useState('All');

  // Detail Modal
  const [selectedExam, setSelectedExam] = useState(null);
  const [detailLoading, setDetailLoading] = useState(false);

  // Notification Preferences Shortcut Modal
  const [showPrefModal, setShowPrefModal] = useState(false);
  const [preferences, setPreferences] = useState(null);
  const [prefSaving, setPrefSaving] = useState(false);

  useEffect(() => {
    fetchExams();
    fetchCategories();
    fetchPreferences();
  }, [selectedCategory, selectedType, selectedStatus]);

  // If opened directly with an examId (from a push notification)
  useEffect(() => {
    if (viewExamId) {
      openExamDetail(viewExamId);
    }
  }, [viewExamId]);

  const fetchExams = async () => {
    try {
      setLoading(true);
      setError(null);

      const params = new URLSearchParams();
      if (selectedCategory !== 'All') params.append('category', selectedCategory);
      if (selectedType !== 'All') params.append('update_type', selectedType);
      if (selectedStatus !== 'All') params.append('status', selectedStatus);
      if (searchQuery.trim()) params.append('search', searchQuery.trim());

      const res = await fetch(`http://localhost:3001/api/government-exams?${params.toString()}`);
      if (!res.ok) throw new Error('Failed to load exam updates');
      const data = await res.json();
      setExams(data.data || []);
    } catch (err) {
      console.error('Error fetching exams:', err);
      setError('Unable to load exam updates.');
    } finally {
      setLoading(false);
    }
  };

  const fetchCategories = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/exam-categories');
      if (res.ok) {
        const data = await res.json();
        setCategories(data.data || []);
      }
    } catch (err) {
      console.error('Error loading categories:', err);
    }
  };

  const fetchPreferences = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/notification-preferences');
      if (res.ok) {
        const data = await res.json();
        setPreferences(data.data);
      }
    } catch (err) {
      console.error('Error loading notification preferences:', err);
    }
  };

  const openExamDetail = async (id) => {
    try {
      setDetailLoading(true);
      const res = await fetch(`http://localhost:3001/api/government-exams/${id}`);
      if (res.ok) {
        const data = await res.json();
        setSelectedExam(data.data);
      }
    } catch (err) {
      console.error('Error opening exam details:', err);
    } finally {
      setDetailLoading(false);
    }
  };

  const handleSavePreferences = async () => {
    if (!preferences) return;
    try {
      setPrefSaving(true);
      const res = await fetch('http://localhost:3001/api/notification-preferences', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(preferences)
      });
      if (res.ok) {
        alert('Notification preferences updated successfully!');
        setShowPrefModal(false);
      }
    } catch (err) {
      console.error('Error saving preferences:', err);
    } finally {
      setPrefSaving(false);
    }
  };

  // Helper for human-readable update type label & icon
  const getUpdateTypeInfo = (type) => {
    switch (type) {
      case 'EXAM_NOTIFICATION':
        return { label: '🔔 Exam Notification', badgeClass: 'badge-primary' };
      case 'APPLICATION_OPEN':
        return { label: '📝 Application Open', badgeClass: 'badge-emerald' };
      case 'APPLICATION_CLOSING':
        return { label: '⏳ Application Closing', badgeClass: 'badge-amber' };
      case 'ADMIT_CARD':
        return { label: '🎟️ Admit Card Released', badgeClass: 'badge-cyan' };
      case 'EXAM_DATE':
        return { label: '📅 Exam Date Announced', badgeClass: 'badge-primary' };
      case 'ANSWER_KEY':
        return { label: '🔑 Answer Key Released', badgeClass: 'badge-cyan' };
      case 'RESULT':
        return { label: '🏆 Result Released', badgeClass: 'badge-emerald' };
      case 'CUTOFF':
        return { label: '📊 Cut-off / Merit List', badgeClass: 'badge-cyan' };
      case 'MERIT_LIST':
        return { label: '📜 Merit List', badgeClass: 'badge-emerald' };
      case 'IMPORTANT_NOTICE':
        return { label: '⚠️ Important Official Notice', badgeClass: 'badge-amber' };
      case 'JOB_NOTIFICATION':
        return { label: '💼 Recruitment Notification', badgeClass: 'badge-primary' };
      default:
        return { label: '📢 Exam Update', badgeClass: 'badge-primary' };
    }
  };

  // Helper to format date cleanly
  const formatDate = (dateStr) => {
    if (!dateStr) return null;
    try {
      const d = new Date(dateStr);
      if (isNaN(d.getTime())) return dateStr;
      return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
    } catch {
      return dateStr;
    }
  };

  // Client-side search filtering if user types in search box
  const filteredExams = exams.filter(exam => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      (exam.exam_name || '').toLowerCase().includes(q) ||
      (exam.organization || '').toLowerCase().includes(q) ||
      (exam.title || '').toLowerCase().includes(q) ||
      (exam.category || '').toLowerCase().includes(q) ||
      (exam.post_name || '').toLowerCase().includes(q) ||
      (exam.official_notification_number || '').toLowerCase().includes(q)
    );
  });

  const categoryOptions = [
    'All',
    'SSC',
    'UPSC',
    'Railway',
    'Banking',
    'KPSC',
    'Defence',
    'Teaching',
    'Police',
    'Other'
  ];

  const updateTypeOptions = [
    { key: 'All', label: 'All Updates' },
    { key: 'EXAM_NOTIFICATION', label: 'Exam Notification' },
    { key: 'APPLICATION_OPEN', label: 'Application Open' },
    { key: 'ADMIT_CARD', label: 'Admit Card' },
    { key: 'EXAM_DATE', label: 'Exam Date' },
    { key: 'ANSWER_KEY', label: 'Answer Key' },
    { key: 'RESULT', label: 'Result' },
    { key: 'JOB_NOTIFICATION', label: 'Government Job' }
  ];

  const statusOptions = [
    { key: 'All', label: 'All Statuses' },
    { key: 'APPLICATIONS_OPEN', label: 'Applications Open' },
    { key: 'COMING_SOON', label: 'Coming Soon' },
    { key: 'EXAM_SCHEDULED', label: 'Exam Scheduled' },
    { key: 'RESULT_RELEASED', label: 'Result Released' },
    { key: 'APPLICATION_CLOSED', label: 'Application Closed' }
  ];

  return (
    <div style={{ maxWidth: 'var(--max-width)', margin: '0 auto', paddingBottom: '60px' }}>
      
      {/* ==========================================
          HEADER SECTION
          ========================================== */}
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
              <span className="badge badge-primary">
                <ShieldCheck size={14} />
                Official Govt Portals Only • 100% Admin Verified
              </span>
              <span className="badge badge-cyan">
                Live Recruitment Feed
              </span>
            </div>
            <h1 style={{ fontSize: '32px', fontWeight: 800, color: '#ffffff', letterSpacing: '-0.02em' }}>
              Government Exams Updates
            </h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '15px', marginTop: '6px' }}>
              Stay updated with verified government exam and recruitment notifications.
            </p>
          </div>

          {/* Quick Notification Settings Button */}
          <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
            <button 
              className="btn btn-secondary"
              onClick={() => setShowPrefModal(true)}
              style={{ fontSize: '13px', padding: '8px 16px', gap: '6px' }}
            >
              <Bell size={15} color="var(--cyan)" />
              <span>Notification Settings</span>
            </button>
            <button 
              className="btn btn-subtle"
              onClick={fetchExams}
              title="Refresh updates"
              style={{ fontSize: '13px', padding: '8px 12px' }}
            >
              <RefreshCw size={15} className={loading ? 'spin' : ''} />
            </button>
          </div>
        </div>
      </div>

      {/* ==========================================
          SEARCH & FILTER TOOLBAR
          ========================================== */}
      <div className="glass-card" style={{ padding: '20px', marginBottom: '28px' }}>
        {/* Search Bar */}
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center', marginBottom: '16px' }}>
          <div style={{
            flex: 1,
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            background: 'rgba(255, 255, 255, 0.04)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-md)',
            padding: '10px 16px'
          }}>
            <Search size={18} color="var(--text-muted)" />
            <input 
              type="text" 
              placeholder="Search Exam (e.g., 'SSC CGL', 'UPSC CDS', 'KPSC', 'RRB NTPC')..."
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              style={{
                width: '100%',
                background: 'transparent',
                border: 'none',
                outline: 'none',
                color: '#ffffff',
                fontSize: '14px'
              }}
            />
            {searchQuery && (
              <button 
                onClick={() => setSearchQuery('')}
                style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer' }}
              >
                <X size={16} />
              </button>
            )}
          </div>
        </div>

        {/* Category Pills */}
        <div style={{ marginBottom: '14px' }}>
          <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '8px', letterSpacing: '0.04em' }}>
            Exam Category
          </div>
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
            {categoryOptions.map(cat => (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                style={{
                  padding: '6px 14px',
                  borderRadius: '20px',
                  fontSize: '13px',
                  fontWeight: 600,
                  border: selectedCategory === cat ? '1px solid var(--cyan)' : '1px solid var(--border-subtle)',
                  background: selectedCategory === cat ? 'rgba(6, 182, 212, 0.15)' : 'rgba(255, 255, 255, 0.03)',
                  color: selectedCategory === cat ? '#ffffff' : 'var(--text-secondary)',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>

        {/* Secondary Filters: Update Type & Status */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px', paddingTop: '14px', borderTop: '1px solid var(--border-subtle)' }}>
          {/* Update Type */}
          <div>
            <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
              Update Type
            </label>
            <select
              value={selectedType}
              onChange={e => setSelectedType(e.target.value)}
              className="admin-select"
              style={{ width: '100%', fontSize: '13px', padding: '8px 12px' }}
            >
              {updateTypeOptions.map(opt => (
                <option key={opt.key} value={opt.key}>{opt.label}</option>
              ))}
            </select>
          </div>

          {/* Status */}
          <div>
            <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600, marginBottom: '6px' }}>
              Application / Exam Status
            </label>
            <select
              value={selectedStatus}
              onChange={e => setSelectedStatus(e.target.value)}
              className="admin-select"
              style={{ width: '100%', fontSize: '13px', padding: '8px 12px' }}
            >
              {statusOptions.map(opt => (
                <option key={opt.key} value={opt.key}>{opt.label}</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* ==========================================
          LOADING & ERROR STATES
          ========================================== */}
      {loading && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '20px' }}>
          {[1, 2, 3, 4, 5, 6].map(i => (
            <div key={i} className="glass-card" style={{ padding: '24px', opacity: 0.6 }}>
              <div style={{ height: '18px', width: '40%', background: 'rgba(255,255,255,0.08)', borderRadius: '4px', marginBottom: '12px' }} />
              <div style={{ height: '24px', width: '75%', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', marginBottom: '10px' }} />
              <div style={{ height: '14px', width: '90%', background: 'rgba(255,255,255,0.06)', borderRadius: '4px', marginBottom: '16px' }} />
              <div style={{ height: '40px', background: 'rgba(255,255,255,0.04)', borderRadius: '6px' }} />
            </div>
          ))}
        </div>
      )}

      {error && !loading && (
        <div className="glass-card" style={{ padding: '48px 24px', textAlign: 'center', borderColor: 'rgba(244, 63, 94, 0.3)' }}>
          <AlertCircle size={36} color="var(--rose)" style={{ margin: '0 auto 12px' }} />
          <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#f8fafc', marginBottom: '6px' }}>{error}</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginBottom: '16px' }}>
            Check your network connection or try refreshing the exam updates list.
          </p>
          <button className="btn btn-secondary" onClick={fetchExams}>
            <RefreshCw size={15} />
            <span>Retry</span>
          </button>
        </div>
      )}

      {/* ==========================================
          EMPTY STATES
          ========================================== */}
      {!loading && !error && filteredExams.length === 0 && (
        <div className="glass-card" style={{ padding: '64px 24px', textAlign: 'center' }}>
          <div style={{
            width: '64px',
            height: '64px',
            borderRadius: '50%',
            background: 'rgba(99, 102, 241, 0.1)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 16px'
          }}>
            <Building2 size={30} color="var(--cyan)" />
          </div>
          {searchQuery || selectedCategory !== 'All' || selectedType !== 'All' || selectedStatus !== 'All' ? (
            <>
              <h3 style={{ fontSize: '20px', fontWeight: 700, color: '#f8fafc', marginBottom: '8px' }}>
                No matching exam updates found.
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '440px', margin: '0 auto 20px' }}>
                No verified government exam updates matched your current filters. Try resetting the search or category filters.
              </p>
              <button 
                className="btn btn-secondary"
                onClick={() => {
                  setSearchQuery('');
                  setSelectedCategory('All');
                  setSelectedType('All');
                  setSelectedStatus('All');
                }}
              >
                Reset All Filters
              </button>
            </>
          ) : (
            <>
              <h3 style={{ fontSize: '20px', fontWeight: 700, color: '#f8fafc', marginBottom: '8px' }}>
                No verified government exam updates available right now.
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '480px', margin: '0 auto 20px' }}>
                Our editorial team verifies official notifications directly from commission gazettes before publishing. Verified updates will appear here once approved in the Admin Console.
              </p>
              <button 
                className="btn btn-primary"
                onClick={() => navigateTo('admin')}
              >
                Open Admin Console
              </button>
            </>
          )}
        </div>
      )}

      {/* ==========================================
          GOVERNMENT EXAM UPDATE CARDS GRID
          ========================================== */}
      {!loading && !error && filteredExams.length > 0 && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(360px, 1fr))', gap: '22px' }}>
          {filteredExams.map(exam => {
            const typeInfo = getUpdateTypeInfo(exam.update_type);
            const dynamicStatus = exam.dynamic_status || {};
            const isExpired = dynamicStatus.is_expired;

            return (
              <div 
                key={exam.id} 
                className="glass-card"
                style={{
                  padding: '24px',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  transition: 'all 0.2s ease',
                  border: isExpired ? '1px solid rgba(244, 63, 94, 0.2)' : '1px solid var(--border-glow)'
                }}
              >
                <div>
                  {/* Top Bar: Organization & Category Badge */}
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <Building2 size={16} color="var(--cyan)" />
                      <span style={{ fontSize: '13px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
                        {exam.organization}
                      </span>
                    </div>
                    <span className="badge badge-primary" style={{ fontSize: '11px', padding: '2px 8px' }}>
                      {exam.category}
                    </span>
                  </div>

                  {/* Exam Name */}
                  <h3 style={{ fontSize: '19px', fontWeight: 700, color: '#f8fafc', marginBottom: '8px', lineHeight: 1.3 }}>
                    {exam.exam_name}
                  </h3>

                  {/* Update Type Badge */}
                  <div style={{ marginBottom: '12px' }}>
                    <span className={`badge ${typeInfo.badgeClass}`} style={{ fontSize: '12px', padding: '4px 10px' }}>
                      {typeInfo.label}
                    </span>
                  </div>

                  {/* Short Title / Description */}
                  <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', lineHeight: 1.55, marginBottom: '16px' }}>
                    {exam.short_description || exam.title}
                  </p>

                  {/* Key Dates Box */}
                  <div style={{
                    background: 'rgba(255, 255, 255, 0.03)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '12px 14px',
                    marginBottom: '16px',
                    fontSize: '12.5px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '6px'
                  }}>
                    {exam.application_start_date && (
                      <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-secondary)' }}>
                        <span>Application Start:</span>
                        <strong style={{ color: '#f8fafc' }}>{formatDate(exam.application_start_date)}</strong>
                      </div>
                    )}
                    {exam.application_last_date && (
                      <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-secondary)' }}>
                        <span>Last Date:</span>
                        <strong style={{ color: isExpired ? 'var(--rose)' : '#f8fafc' }}>
                          {formatDate(exam.application_last_date)}
                        </strong>
                      </div>
                    )}
                    {exam.exam_date && (
                      <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-secondary)' }}>
                        <span>Exam Date:</span>
                        <strong style={{ color: 'var(--cyan)' }}>{formatDate(exam.exam_date)}</strong>
                      </div>
                    )}
                    {exam.result_date && (
                      <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-secondary)' }}>
                        <span>Result Date:</span>
                        <strong style={{ color: 'var(--emerald)' }}>{formatDate(exam.result_date)}</strong>
                      </div>
                    )}
                  </div>
                </div>

                {/* Card Footer: Status & View Details Button */}
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '14px', paddingTop: '10px', borderTop: '1px solid var(--border-subtle)' }}>
                    <div>
                      <span className={`badge ${dynamicStatus.badge_class || 'badge-primary'}`} style={{ fontSize: '11.5px', padding: '3px 8px' }}>
                        {dynamicStatus.status_label || 'Verified Update'}
                      </span>
                    </div>
                    {exam.published_at && (
                      <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                        Published {formatDate(exam.published_at)}
                      </span>
                    )}
                  </div>

                  <button 
                    className="btn btn-primary"
                    style={{ width: '100%', justifyContent: 'center', fontSize: '13.5px' }}
                    onClick={() => openExamDetail(exam.id)}
                  >
                    <span>View Details</span>
                    <ChevronRight size={16} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* ==========================================
          EXAM DETAIL MODAL / PAGE VIEW
          ========================================== */}
      {selectedExam && (
        <div className="modal-backdrop" onClick={() => setSelectedExam(null)}>
          <div 
            className="modal-content" 
            onClick={e => e.stopPropagation()}
            style={{ maxWidth: '780px', maxHeight: '90vh', overflowY: 'auto', padding: '0' }}
          >
            {/* Modal Header */}
            <div style={{
              padding: '24px 28px',
              borderBottom: '1px solid var(--border-subtle)',
              position: 'relative',
              background: 'linear-gradient(180deg, rgba(99, 102, 241, 0.08) 0%, rgba(8, 13, 26, 0.9) 100%)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Building2 size={18} color="var(--cyan)" />
                  <span style={{ fontSize: '14px', fontWeight: 700, color: 'var(--cyan)' }}>
                    {selectedExam.organization}
                  </span>
                  <span className="badge badge-primary">{selectedExam.category}</span>
                </div>
                <button 
                  onClick={() => setSelectedExam(null)}
                  className="btn-icon"
                  style={{ width: '32px', height: '32px' }}
                >
                  <X size={18} />
                </button>
              </div>

              <h2 style={{ fontSize: '24px', fontWeight: 800, color: '#ffffff', marginBottom: '8px', lineHeight: 1.3 }}>
                {selectedExam.exam_name}
              </h2>
              
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
                <span className={`badge ${getUpdateTypeInfo(selectedExam.update_type).badgeClass}`}>
                  {getUpdateTypeInfo(selectedExam.update_type).label}
                </span>
                <span className={`badge ${selectedExam.dynamic_status?.badge_class || 'badge-primary'}`}>
                  {selectedExam.dynamic_status?.status_label}
                </span>
                {selectedExam.official_notification_number && (
                  <span className="badge badge-subtle">
                    Ref: {selectedExam.official_notification_number}
                  </span>
                )}
              </div>
            </div>

            {/* Modal Body */}
            <div style={{ padding: '28px', display: 'flex', flexDirection: 'column', gap: '24px' }}>
              
              {/* Short Title & Full Description */}
              <div>
                <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#f8fafc', marginBottom: '8px' }}>
                  {selectedExam.title}
                </h4>
                <p style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                  {selectedExam.full_description || selectedExam.short_description}
                </p>
              </div>

              {/* Exam Information Table (ONLY fields with verified values!) */}
              <div>
                <h4 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: '12px' }}>
                  Exam & Recruitment Information
                </h4>
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
                  gap: '12px',
                  background: 'rgba(255, 255, 255, 0.02)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-md)',
                  padding: '16px'
                }}>
                  {selectedExam.post_name && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Post / Job Name</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.post_name}</div>
                    </div>
                  )}

                  {selectedExam.vacancy && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Number of Vacancies</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--emerald)' }}>{selectedExam.vacancy}</div>
                    </div>
                  )}

                  {selectedExam.eligibility && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Eligibility</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.eligibility}</div>
                    </div>
                  )}

                  {selectedExam.age_limit && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Age Limit</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.age_limit}</div>
                    </div>
                  )}

                  {selectedExam.qualification && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Educational Qualification</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.qualification}</div>
                    </div>
                  )}

                  {selectedExam.application_fee && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Application Fee</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.application_fee}</div>
                    </div>
                  )}

                  {selectedExam.selection_process && (
                    <div style={{ gridColumn: '1 / -1' }}>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Selection Process</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{selectedExam.selection_process}</div>
                    </div>
                  )}
                </div>
              </div>

              {/* Important Dates Table (ONLY fields with verified values!) */}
              <div>
                <h4 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: '12px' }}>
                  Important Verified Dates
                </h4>
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                  gap: '12px',
                  background: 'rgba(255, 255, 255, 0.02)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-md)',
                  padding: '16px'
                }}>
                  {selectedExam.notification_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Notification Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{formatDate(selectedExam.notification_date)}</div>
                    </div>
                  )}
                  {selectedExam.application_start_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Application Start Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{formatDate(selectedExam.application_start_date)}</div>
                    </div>
                  )}
                  {selectedExam.application_last_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Application Last Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: selectedExam.dynamic_status?.is_expired ? 'var(--rose)' : 'var(--amber)' }}>
                        {formatDate(selectedExam.application_last_date)}
                      </div>
                    </div>
                  )}
                  {selectedExam.correction_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Application Correction Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#f8fafc' }}>{formatDate(selectedExam.correction_date)}</div>
                    </div>
                  )}
                  {selectedExam.admit_card_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Admit Card Release Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--cyan)' }}>{formatDate(selectedExam.admit_card_date)}</div>
                    </div>
                  )}
                  {selectedExam.exam_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Examination Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--primary-light)' }}>{formatDate(selectedExam.exam_date)}</div>
                    </div>
                  )}
                  {selectedExam.answer_key_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Answer Key Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--cyan)' }}>{formatDate(selectedExam.answer_key_date)}</div>
                    </div>
                  )}
                  {selectedExam.result_date && (
                    <div>
                      <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Result Announcement Date</div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: 'var(--emerald)' }}>{formatDate(selectedExam.result_date)}</div>
                    </div>
                  )}
                </div>
              </div>

              {/* Official Source Reference Box */}
              <div style={{
                padding: '18px 20px',
                borderRadius: 'var(--radius-md)',
                background: 'rgba(6, 182, 212, 0.08)',
                border: '1px solid rgba(6, 182, 212, 0.25)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: '16px'
              }}>
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '4px' }}>
                    <ShieldCheck size={16} />
                    Verified Official Reference
                  </div>
                  <div style={{ fontSize: '14px', fontWeight: 600, color: '#f8fafc' }}>
                    {selectedExam.official_source_name}
                  </div>
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '2px' }}>
                    Every date and vacancy number is validated directly against the issuing authority's publication.
                  </div>
                </div>

                <a 
                  href={selectedExam.official_source_url} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="btn btn-primary"
                  style={{ textDecoration: 'none', gap: '8px' }}
                >
                  <span>View Official Notification</span>
                  <ExternalLink size={15} />
                </a>
              </div>

            </div>

            {/* Modal Footer */}
            <div style={{
              padding: '16px 28px',
              borderTop: '1px solid var(--border-subtle)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              background: 'rgba(0, 0, 0, 0.2)'
            }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                Verification ID: #{selectedExam.id} • Status: {selectedExam.verification_status}
              </span>
              <button 
                className="btn btn-secondary"
                onClick={() => setSelectedExam(null)}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ==========================================
          NOTIFICATION PREFERENCES MODAL
          ========================================== */}
      {showPrefModal && preferences && (
        <div className="modal-backdrop" onClick={() => setShowPrefModal(false)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '640px' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Bell size={20} color="var(--cyan)" />
                <h3 style={{ fontSize: '18px', fontWeight: 700 }}>Government Exam Notification Settings</h3>
              </div>
              <button className="btn-icon" onClick={() => setShowPrefModal(false)}>
                <X size={16} />
              </button>
            </div>

            <div style={{ padding: '24px', maxHeight: '70vh', overflowY: 'auto' }}>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', marginBottom: '18px' }}>
                Customize which alerts and exams you want to receive instant notifications and deadline reminders for.
              </p>

              {/* Notification Types */}
              <div style={{ marginBottom: '22px' }}>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  Update Types
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '10px' }}>
                  {[
                    { key: 'exam_notifications', label: 'New Exam Notifications' },
                    { key: 'application_updates', label: 'Application Started & Deadlines' },
                    { key: 'admit_card_updates', label: 'Admit Card Released' },
                    { key: 'exam_date_updates', label: 'Exam Date Announced' },
                    { key: 'answer_key_updates', label: 'Answer Key Released' },
                    { key: 'result_updates', label: 'Results & Merit Lists' },
                    { key: 'job_notifications', label: 'Government Job Recruitment' }
                  ].map(item => (
                    <label key={item.key} style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: '#f8fafc', cursor: 'pointer' }}>
                      <input 
                        type="checkbox"
                        checked={!!preferences[item.key]}
                        onChange={e => setPreferences({ ...preferences, [item.key]: e.target.checked })}
                        style={{ accentColor: 'var(--cyan)', width: '16px', height: '16px' }}
                      />
                      <span>{item.label}</span>
                    </label>
                  ))}
                </div>
              </div>

              {/* Category Preferences */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  Category Preferences
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
                  {['SSC', 'UPSC', 'Railway', 'Banking', 'KPSC', 'Defence', 'Teaching', 'Police'].map(cat => {
                    const isChecked = (preferences.category_preferences || []).includes(cat);
                    return (
                      <label key={cat} style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: '#f8fafc', cursor: 'pointer' }}>
                        <input 
                          type="checkbox"
                          checked={isChecked}
                          onChange={e => {
                            const current = preferences.category_preferences || [];
                            const updated = e.target.checked 
                              ? [...current, cat] 
                              : current.filter(c => c !== cat);
                            setPreferences({ ...preferences, category_preferences: updated });
                          }}
                          style={{ accentColor: 'var(--cyan)', width: '16px', height: '16px' }}
                        />
                        <span>{cat}</span>
                      </label>
                    );
                  })}
                </div>
              </div>
            </div>

            <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setShowPrefModal(false)}>
                Cancel
              </button>
              <button className="btn btn-primary" onClick={handleSavePreferences} disabled={prefSaving}>
                {prefSaving ? 'Saving...' : 'Save Preferences'}
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
