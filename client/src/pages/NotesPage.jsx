import React, { useState, useEffect } from 'react';
import { 
  FileText, 
  Search, 
  Download, 
  ExternalLink, 
  Maximize2, 
  Minimize2, 
  ZoomIn, 
  ZoomOut, 
  RotateCcw, 
  X, 
  BookOpen, 
  Layers, 
  ShieldCheck, 
  Calendar, 
  Filter,
  CheckCircle2,
  Sparkles,
  ArrowRight,
  Eye
} from 'lucide-react';

export default function NotesPage({ navigateTo }) {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedSubject, setSelectedSubject] = useState('All');
  const [selectedTopic, setSelectedTopic] = useState('All');
  
  // PDF Viewer Modal State
  const [activeNote, setActiveNote] = useState(null);
  const [zoomLevel, setZoomLevel] = useState(100);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [viewerKey, setViewerKey] = useState(0);

  useEffect(() => {
    fetchNotes();
  }, [selectedSubject, selectedTopic]);

  const fetchNotes = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (selectedSubject !== 'All') params.append('subject', selectedSubject);
      if (selectedTopic !== 'All') params.append('topic', selectedTopic);
      if (searchQuery.trim()) params.append('search', searchQuery.trim());

      const res = await fetch(`http://localhost:3001/api/notes?${params.toString()}`);
      if (res.ok) {
        const json = await res.json();
        setNotes(json.data || []);
      }
    } catch (err) {
      console.error('Error fetching published notes:', err);
    } finally {
      setLoading(false);
    }
  };

  // Extract unique subjects and topics for filtering
  const subjects = ['All', ...new Set(notes.map(n => n.subject_name).filter(Boolean))];
  const topics = ['All', ...new Set(
    notes
      .filter(n => selectedSubject === 'All' || n.subject_name === selectedSubject)
      .map(n => n.topic_name)
      .filter(Boolean)
  )];

  // Client-side search filtering
  const filteredNotes = notes.filter(note => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      (note.title || '').toLowerCase().includes(q) ||
      (note.subject_name || '').toLowerCase().includes(q) ||
      (note.topic_name || '').toLowerCase().includes(q) ||
      (note.subtopic_name || '').toLowerCase().includes(q) ||
      (note.description || '').toLowerCase().includes(q) ||
      (note.source || '').toLowerCase().includes(q)
    );
  });

  const handleOpenPdf = (note) => {
    setActiveNote(note);
    setZoomLevel(100);
    setIsFullscreen(false);
    setViewerKey(prev => prev + 1);
  };

  const handleCloseViewer = () => {
    setActiveNote(null);
  };

  const handleZoomIn = () => {
    setZoomLevel(prev => Math.min(prev + 25, 200));
  };

  const handleZoomOut = () => {
    setZoomLevel(prev => Math.max(prev - 25, 50));
  };

  const handleResetZoom = () => {
    setZoomLevel(100);
  };

  const toggleFullscreen = () => {
    setIsFullscreen(!isFullscreen);
  };

  return (
    <div className="notes-page-container" style={{ paddingBottom: '60px' }}>
      {/* Page Header */}
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
          <span className="badge badge-cyan" style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
            <ShieldCheck size={14} />
            Verified Faculty & Syllabus Notes
          </span>
        </div>
        <h1 style={{ fontSize: '32px', fontWeight: 800, marginBottom: '8px', color: '#fff' }}>
          📚 Study Notes & PDF Repository
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '15px', maxWidth: '780px', lineHeight: 1.5 }}>
          Access real, comprehensive revision notes, formula compendiums, topic breakdowns, and reference sheets uploaded and verified by subject matter experts.
        </p>

        {/* Search & Filter Controls */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginTop: '24px' }}>
          <div style={{ display: 'flex', gap: '16px', flexWrap: 'wrap', alignItems: 'center' }}>
            {/* Search Input */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              padding: '10px 16px',
              borderRadius: 'var(--radius-md)',
              background: 'var(--bg-card)',
              border: '1px solid var(--border-subtle)',
              flex: '1',
              minWidth: '280px'
            }}>
              <Search size={18} color="var(--text-muted)" />
              <input 
                type="text"
                placeholder="Search notes by title, subject, topic, or keyword..."
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                style={{ border: 'none', outline: 'none', width: '100%', fontSize: '14.5px', color: '#fff', background: 'transparent' }}
              />
              {searchQuery && (
                <button 
                  onClick={() => setSearchQuery('')}
                  style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: 0 }}
                  title="Clear search"
                >
                  <X size={16} />
                </button>
              )}
            </div>

            {/* Subject Dropdown Filter */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '13px', color: 'var(--text-secondary)', fontWeight: 600 }}>Subject:</span>
              <select
                value={selectedSubject}
                onChange={e => {
                  setSelectedSubject(e.target.value);
                  setSelectedTopic('All');
                }}
                style={{
                  padding: '9px 14px',
                  borderRadius: 'var(--radius-md)',
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-subtle)',
                  color: '#fff',
                  fontSize: '13.5px',
                  outline: 'none',
                  cursor: 'pointer'
                }}
              >
                <option value="All">All Subjects</option>
                {subjects.filter(s => s !== 'All').map(sub => (
                  <option key={sub} value={sub}>{sub}</option>
                ))}
              </select>
            </div>

            {/* Topic Dropdown Filter */}
            {topics.length > 1 && (
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '13px', color: 'var(--text-secondary)', fontWeight: 600 }}>Topic:</span>
                <select
                  value={selectedTopic}
                  onChange={e => setSelectedTopic(e.target.value)}
                  style={{
                    padding: '9px 14px',
                    borderRadius: 'var(--radius-md)',
                    background: 'var(--bg-card)',
                    border: '1px solid var(--border-subtle)',
                    color: '#fff',
                    fontSize: '13.5px',
                    outline: 'none',
                    cursor: 'pointer'
                  }}
                >
                  <option value="All">All Topics</option>
                  {topics.filter(t => t !== 'All').map(top => (
                    <option key={top} value={top}>{top}</option>
                  ))}
                </select>
              </div>
            )}
          </div>

          {/* Quick Subject Filter Pills */}
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center' }}>
            <span style={{ fontSize: '12px', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px', fontWeight: 700 }}>
              Quick Filters:
            </span>
            {['All', 'English', 'Mathematics', 'Reasoning', 'General Awareness', 'Science'].map(quickSub => {
              const isActive = selectedSubject.toLowerCase() === quickSub.toLowerCase();
              return (
                <button
                  key={quickSub}
                  onClick={() => {
                    setSelectedSubject(isActive && quickSub !== 'All' ? 'All' : quickSub);
                    setSelectedTopic('All');
                  }}
                  className={`btn ${isActive ? 'btn-primary' : 'btn-secondary'}`}
                  style={{
                    fontSize: '12.5px',
                    padding: '4px 12px',
                    borderRadius: '20px',
                    transition: 'all 0.15s ease'
                  }}
                >
                  {quickSub}
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Main Content Area */}
      {loading ? (
        <div style={{ padding: '60px 0', textAlign: 'center', color: 'var(--text-muted)' }}>
          <div className="spinner" style={{ margin: '0 auto 16px' }}></div>
          <p style={{ fontSize: '14.5px' }}>Loading verified study notes...</p>
        </div>
      ) : filteredNotes.length === 0 ? (
        /* Empty State */
        <div style={{
          padding: '64px 24px',
          textAlign: 'center',
          borderRadius: 'var(--radius-lg)',
          background: 'var(--bg-card)',
          border: '1px dashed var(--border-subtle)',
          margin: '20px 0'
        }}>
          <div style={{
            width: '64px',
            height: '64px',
            borderRadius: '50%',
            background: 'rgba(99, 102, 241, 0.1)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 16px',
            color: 'var(--cyan)'
          }}>
            <FileText size={32} />
          </div>
          {searchQuery || selectedSubject !== 'All' || selectedTopic !== 'All' ? (
            <>
              <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>
                No matching study notes found
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '440px', margin: '0 auto 20px' }}>
                We couldn't find any published notes matching your criteria. Try adjusting your search query or selecting a different subject.
              </p>
              <button 
                className="btn btn-secondary"
                onClick={() => {
                  setSearchQuery('');
                  setSelectedSubject('All');
                  setSelectedTopic('All');
                }}
              >
                Clear Filters
              </button>
            </>
          ) : (
            <>
              <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#fff', marginBottom: '8px' }}>
                No Study Notes Published Yet
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', maxWidth: '460px', margin: '0 auto 20px', lineHeight: 1.5 }}>
                Our faculty and administrators are currently compiling and verifying high-yield PDF notes. Check back soon or visit Courses to start learning.
              </p>
              <button 
                className="btn btn-primary"
                onClick={() => navigateTo('course', { slug: 'english' })}
              >
                Explore Syllabus Courses
              </button>
            </>
          )}
        </div>
      ) : (
        /* Notes Cards Grid */
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(360px, 1fr))',
          gap: '20px'
        }}>
          {filteredNotes.map(note => (
            <div 
              key={note.id}
              className="card"
              style={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                padding: '22px',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--border-subtle)',
                background: 'var(--bg-card)',
                transition: 'transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease'
              }}
              onMouseEnter={e => {
                e.currentTarget.style.borderColor = 'rgba(6, 182, 212, 0.4)';
                e.currentTarget.style.transform = 'translateY(-3px)';
                e.currentTarget.style.boxShadow = '0 12px 24px -10px rgba(6, 182, 212, 0.15)';
              }}
              onMouseLeave={e => {
                e.currentTarget.style.borderColor = 'var(--border-subtle)';
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = 'none';
              }}
            >
              <div>
                {/* Subject & Status Badges */}
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px' }}>
                  <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <span className="badge badge-primary" style={{ fontSize: '11.5px', padding: '3px 8px' }}>
                      {note.subject_name}
                    </span>
                    {note.topic_name && (
                      <span className="badge badge-cyan" style={{ fontSize: '11.5px', padding: '3px 8px' }}>
                        {note.topic_name}
                      </span>
                    )}
                  </div>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <CheckCircle2 size={12} color="var(--emerald)" /> Verified
                  </span>
                </div>

                {/* Card Title */}
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px', marginBottom: '10px' }}>
                  <div style={{
                    width: '36px',
                    height: '36px',
                    borderRadius: '8px',
                    background: 'rgba(244, 63, 94, 0.1)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
                    color: 'var(--rose)'
                  }}>
                    <FileText size={20} />
                  </div>
                  <div>
                    <h3 style={{ fontSize: '17px', fontWeight: 700, color: '#fff', lineHeight: 1.35 }}>
                      {note.title}
                    </h3>
                    {note.subtopic_name && (
                      <span style={{ fontSize: '12px', color: 'var(--cyan)', display: 'block', marginTop: '2px' }}>
                        Subtopic: {note.subtopic_name}
                      </span>
                    )}
                  </div>
                </div>

                {/* Description */}
                {note.description && (
                  <p style={{
                    color: 'var(--text-secondary)',
                    fontSize: '13.5px',
                    lineHeight: 1.5,
                    marginBottom: '16px',
                    display: '-webkit-box',
                    WebkitLineClamp: 3,
                    WebkitBoxOrient: 'vertical',
                    overflow: 'hidden'
                  }}>
                    {note.description}
                  </p>
                )}

                {/* Metadata Pill Strip */}
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px',
                  padding: '8px 12px',
                  background: 'rgba(255, 255, 255, 0.02)',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-subtle)',
                  fontSize: '12px',
                  color: 'var(--text-muted)',
                  marginBottom: '20px',
                  flexWrap: 'wrap'
                }}>
                  {note.file_size && (
                    <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <strong style={{ color: '#fff' }}>Size:</strong> {note.file_size}
                    </span>
                  )}
                  {note.page_count && (
                    <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <strong style={{ color: '#fff' }}>Pages:</strong> {note.page_count}
                    </span>
                  )}
                  {note.source && (
                    <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <strong style={{ color: '#fff' }}>Source:</strong> {note.source}
                    </span>
                  )}
                </div>
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', gap: '10px', alignItems: 'center', paddingTop: '12px', borderTop: '1px solid var(--border-subtle)' }}>
                <button
                  className="btn btn-primary"
                  onClick={() => handleOpenPdf(note)}
                  style={{
                    flex: '1',
                    fontSize: '13.5px',
                    padding: '9px 16px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '8px'
                  }}
                >
                  <Eye size={16} />
                  <span>Open PDF</span>
                </button>

                <a
                  href={`http://localhost:3001${note.file_url}`}
                  download={note.file_name || `${note.title}.pdf`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-secondary"
                  style={{
                    padding: '9px 12px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    textDecoration: 'none'
                  }}
                  title="Download PDF"
                >
                  <Download size={16} />
                </a>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* ==================================================== */}
      {/* 9. USER PDF VIEWER MODAL                             */}
      {/* ==================================================== */}
      {activeNote && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(5, 7, 15, 0.85)',
          backdropFilter: 'blur(8px)',
          zIndex: 1000,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: isFullscreen ? '0' : '20px'
        }}>
          <div style={{
            width: isFullscreen ? '100vw' : '92vw',
            maxWidth: isFullscreen ? '100vw' : '1200px',
            height: isFullscreen ? '100vh' : '90vh',
            background: 'var(--bg-dark)',
            border: isFullscreen ? 'none' : '1px solid var(--border-light)',
            borderRadius: isFullscreen ? '0' : 'var(--radius-lg)',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7)'
          }}>
            {/* Viewer Header / Toolbar */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '12px 20px',
              background: 'var(--bg-card)',
              borderBottom: '1px solid var(--border-subtle)',
              flexWrap: 'wrap',
              gap: '12px'
            }}>
              {/* Note Details */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', minWidth: '220px' }}>
                <div style={{
                  width: '32px',
                  height: '32px',
                  borderRadius: '6px',
                  background: 'rgba(244, 63, 94, 0.15)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: 'var(--rose)'
                }}>
                  <FileText size={18} />
                </div>
                <div>
                  <h4 style={{ fontSize: '15px', fontWeight: 700, color: '#fff', margin: 0 }}>
                    {activeNote.title}
                  </h4>
                  <div style={{ display: 'flex', gap: '6px', alignItems: 'center', marginTop: '2px' }}>
                    <span style={{ fontSize: '11px', color: 'var(--cyan)' }}>{activeNote.subject_name}</span>
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>•</span>
                    <span style={{ fontSize: '11px', color: 'var(--text-secondary)' }}>{activeNote.topic_name}</span>
                  </div>
                </div>
              </div>

              {/* Viewer Controls Toolbar */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                {/* Zoom Controls */}
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  background: 'rgba(255, 255, 255, 0.05)',
                  borderRadius: 'var(--radius-sm)',
                  border: '1px solid var(--border-subtle)',
                  padding: '2px 6px',
                  gap: '4px'
                }}>
                  <button
                    onClick={handleZoomOut}
                    style={{ background: 'transparent', border: 'none', color: '#fff', cursor: 'pointer', padding: '4px' }}
                    title="Zoom Out"
                  >
                    <ZoomOut size={15} />
                  </button>
                  <span style={{ fontSize: '12px', color: 'var(--text-secondary)', minWidth: '42px', textAlign: 'center' }}>
                    {zoomLevel}%
                  </span>
                  <button
                    onClick={handleZoomIn}
                    style={{ background: 'transparent', border: 'none', color: '#fff', cursor: 'pointer', padding: '4px' }}
                    title="Zoom In"
                  >
                    <ZoomIn size={15} />
                  </button>
                  <button
                    onClick={handleResetZoom}
                    style={{ background: 'transparent', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', padding: '4px' }}
                    title="Reset Zoom (100%)"
                  >
                    <RotateCcw size={13} />
                  </button>
                </div>

                {/* External Tab */}
                <a
                  href={`http://localhost:3001${activeNote.file_url}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-secondary"
                  style={{ padding: '6px 10px', fontSize: '12.5px', gap: '4px', textDecoration: 'none' }}
                  title="Open in Browser New Tab"
                >
                  <ExternalLink size={14} />
                  <span style={{ display: 'none' }}>Tab</span>
                </a>

                {/* Direct Download */}
                <a
                  href={`http://localhost:3001${activeNote.file_url}`}
                  download={activeNote.file_name || `${activeNote.title}.pdf`}
                  className="btn btn-secondary"
                  style={{ padding: '6px 10px', fontSize: '12.5px', gap: '4px', textDecoration: 'none' }}
                  title="Download File"
                >
                  <Download size={14} />
                </a>

                {/* Fullscreen Toggle */}
                <button
                  onClick={toggleFullscreen}
                  className="btn btn-secondary"
                  style={{ padding: '6px 10px', fontSize: '12.5px' }}
                  title={isFullscreen ? 'Exit Fullscreen' : 'Fullscreen'}
                >
                  {isFullscreen ? <Minimize2 size={14} /> : <Maximize2 size={14} />}
                </button>

                {/* Close Button */}
                <button
                  onClick={handleCloseViewer}
                  className="btn btn-secondary"
                  style={{
                    padding: '6px 12px',
                    fontSize: '12.5px',
                    background: 'rgba(244, 63, 94, 0.1)',
                    borderColor: 'rgba(244, 63, 94, 0.3)',
                    color: 'var(--rose)',
                    gap: '4px'
                  }}
                  title="Close PDF Viewer"
                >
                  <X size={15} />
                  <span>Close</span>
                </button>
              </div>
            </div>

            {/* Embedded PDF Viewer Container */}
            <div style={{
              flex: 1,
              width: '100%',
              height: '100%',
              background: '#1e293b',
              position: 'relative',
              overflow: 'hidden',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}>
              <iframe
                key={`${viewerKey}-${zoomLevel}`}
                src={`http://localhost:3001${activeNote.file_url}#toolbar=1&navpanes=1&scrollbar=1&zoom=${zoomLevel}`}
                title={activeNote.title}
                style={{
                  width: '100%',
                  height: '100%',
                  border: 'none',
                  transformOrigin: 'top center'
                }}
              />
            </div>

            {/* Viewer Bottom Info Bar */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '8px 20px',
              background: 'var(--bg-card)',
              borderTop: '1px solid var(--border-subtle)',
              fontSize: '12px',
              color: 'var(--text-muted)'
            }}>
              <span>
                File: <strong style={{ color: '#fff' }}>{activeNote.file_name}</strong> ({activeNote.file_size || 'PDF Document'})
              </span>
              <span>
                Use built-in viewer tools to navigate pages, rotate, or print.
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
