import React, { useState, useEffect, useRef } from 'react';
import { Search, X, BookOpen, ArrowRight, FileText, CheckCircle2 } from 'lucide-react';

export default function SearchModal({ isOpen, onClose, navigateTo }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const inputRef = useRef(null);

  const searchableItems = [
    { type: 'topic', title: 'Noun', course: 'English', slug: 'english', id: 1, desc: 'Rules, collective concord, uncountable nouns & SSC 2024 questions' },
    { type: 'topic', title: 'Pronoun', course: 'English', slug: 'english', id: 2, desc: 'Personal, relative, reflexive pronouns & antecedent agreement' },
    { type: 'topic', title: 'Subject-Verb Agreement', course: 'English', slug: 'english', id: 11, desc: 'Singular/plural agreement rules & compound subjects' },
    { type: 'topic', title: 'Number System', course: 'Mathematics', slug: 'mathematics', id: 23, desc: 'Divisibility rules, unit digits, remainders & factors' },
    { type: 'topic', title: 'Percentage', course: 'Mathematics', slug: 'mathematics', id: 24, desc: 'Base values, successive calculations & fractions' },
    { type: 'topic', title: 'Syllogism', course: 'Reasoning Ability', slug: 'reasoning', id: 46, desc: 'Venn diagrams, Some/All statements & conclusions' },
    { type: 'course', title: 'English Course', course: 'English', slug: 'english', desc: '22 Unlockable learning levels' },
    { type: 'course', title: 'Mathematics Course', course: 'Mathematics', slug: 'mathematics', desc: '15 Quantitative aptitude levels' },
    { type: 'pyq', title: 'SSC CGL 2024 Tier-1 Noun Questions', course: 'English', slug: 'english', id: 1, desc: 'Official verified questions on uncountable nouns and scissors' }
  ];

  useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
    }
  }, [isOpen]);

  useEffect(() => {
    if (!query.trim()) {
      setResults(searchableItems.slice(0, 5));
    } else {
      const q = query.toLowerCase();
      const filtered = searchableItems.filter(item => 
        item.title.toLowerCase().includes(q) || 
        item.course.toLowerCase().includes(q) ||
        item.desc.toLowerCase().includes(q)
      );
      setResults(filtered);
    }
  }, [query]);

  if (!isOpen) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {/* Search Input Bar */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          padding: '18px 24px',
          borderBottom: '1px solid var(--border-subtle)'
        }}>
          <Search size={20} color="var(--cyan)" />
          <input 
            ref={inputRef}
            type="text" 
            placeholder="Search topics, courses, exams, or rules (e.g. Noun, SSC CGL, Percentage)..." 
            value={query}
            onChange={e => setQuery(e.target.value)}
            style={{
              flex: 1,
              fontSize: '16px',
              border: 'none',
              outline: 'none',
              color: '#ffffff'
            }}
          />
          <button className="btn-icon" onClick={onClose} style={{ width: '32px', height: '32px' }}>
            <X size={16} />
          </button>
        </div>

        {/* Results List */}
        <div style={{ maxHeight: '380px', overflowY: 'auto', padding: '12px' }}>
          <div style={{ fontSize: '11.5px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', padding: '6px 12px', letterSpacing: '0.05em' }}>
            {query.trim() ? 'Matching Results' : 'Recommended Topics & Pathways'}
          </div>

          {results.length === 0 ? (
            <div style={{ padding: '32px 16px', textAlign: 'center', color: 'var(--text-muted)' }}>
              No matches found for "{query}". Try searching for "Noun", "English", or "SSC CGL".
            </div>
          ) : (
            results.map((item, idx) => (
              <div 
                key={idx}
                onClick={() => {
                  if (item.type === 'topic' || item.type === 'pyq') {
                    navigateTo('topic', { id: item.id });
                  } else {
                    navigateTo('course', { slug: item.slug });
                  }
                  onClose();
                }}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '12px 16px',
                  borderRadius: 'var(--radius-md)',
                  cursor: 'pointer',
                  transition: 'background 0.15s ease',
                  marginBottom: '4px'
                }}
                onMouseEnter={e => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.05)'}
                onMouseLeave={e => e.currentTarget.style.background = 'transparent'}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
                  <div style={{
                    width: '36px',
                    height: '36px',
                    borderRadius: 'var(--radius-sm)',
                    background: item.type === 'topic' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(6, 182, 212, 0.15)',
                    color: item.type === 'topic' ? 'var(--primary-light)' : 'var(--cyan)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    {item.type === 'topic' ? <BookOpen size={18} /> : <FileText size={18} />}
                  </div>
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontWeight: 600, color: '#f8fafc', fontSize: '14px' }}>{item.title}</span>
                      <span className="badge badge-cyan" style={{ fontSize: '10px', padding: '1px 6px' }}>{item.course}</span>
                    </div>
                    <div style={{ color: 'var(--text-secondary)', fontSize: '12px', marginTop: '2px' }}>{item.desc}</div>
                  </div>
                </div>
                <ArrowRight size={16} color="var(--text-muted)" />
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
