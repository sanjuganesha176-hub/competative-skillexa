import React, { useState, useEffect } from 'react';
import { 
  Award, 
  Calendar, 
  Search, 
  ShieldCheck, 
  ExternalLink, 
  Sparkles,
  Tag,
  Building
} from 'lucide-react';

export default function CurrentAffairsPage() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [categoryFilter, setCategoryFilter] = useState('All');
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchCurrentAffairs();
  }, [categoryFilter]);

  const fetchCurrentAffairs = async () => {
    try {
      setLoading(true);
      const url = categoryFilter === 'All'
        ? 'http://localhost:3001/api/current-affairs'
        : `http://localhost:3001/api/current-affairs?category=${encodeURIComponent(categoryFilter)}`;
      const res = await fetch(url);
      const data = await res.json();
      setItems(data);
    } catch (err) {
      console.error('Error fetching current affairs:', err);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['All', 'Science & Technology', 'Economy & Energy', 'Defense & Security', 'Governance & Tech'];

  const filteredItems = items.filter(item => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase();
    return item.title.toLowerCase().includes(q) || item.summary.toLowerCase().includes(q);
  });

  return (
    <div>
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
          <span className="badge badge-cyan">
            <ShieldCheck size={14} />
            PIB & Official Press Releases
          </span>
        </div>
        <h1 style={{ fontSize: '32px', fontWeight: 800, marginBottom: '8px' }}>
          Competitive Exam Current Affairs
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '15px', maxWidth: '750px', lineHeight: 1.5 }}>
          Time-sensitive national developments, government missions, science breakthroughs, and defense achievements curated directly from the Press Information Bureau (PIB) and official government publications.
        </p>

        {/* Search & Categories */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginTop: '24px', flexWrap: 'wrap' }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            padding: '8px 14px',
            borderRadius: 'var(--radius-md)',
            background: 'var(--bg-card)',
            border: '1px solid var(--border-subtle)',
            flex: '1',
            minWidth: '240px'
          }}>
            <Search size={16} color="var(--text-muted)" />
            <input 
              type="text"
              placeholder="Search current affairs by title or keyword..."
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              style={{ border: 'none', outline: 'none', width: '100%', fontSize: '14px', color: '#fff' }}
            />
          </div>

          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
            {categories.map(cat => (
              <button
                key={cat}
                className={`btn ${categoryFilter === cat ? 'btn-primary' : 'btn-secondary'}`}
                onClick={() => setCategoryFilter(cat)}
                style={{ fontSize: '12.5px', padding: '6px 12px' }}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '60px 20px', color: 'var(--text-secondary)' }}>
          <Sparkles size={28} className="spin" color="var(--cyan)" style={{ marginBottom: '12px' }} />
          <div>Fetching official current affairs...</div>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {filteredItems.map(item => (
            <div key={item.id} className="glass-card" style={{ padding: '24px' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span className="badge badge-primary">{item.category}</span>
                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '12px', color: 'var(--text-muted)' }}>
                    <Calendar size={13} />
                    {item.date}
                  </span>
                </div>

                {item.source && (
                  <span style={{ fontSize: '12px', color: 'var(--cyan)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                    <ShieldCheck size={14} />
                    {item.source.publisher}
                  </span>
                )}
              </div>

              <h3 style={{ fontSize: '18px', fontWeight: 700, color: '#f8fafc', marginBottom: '10px', lineHeight: 1.4 }}>
                {item.title}
              </h3>

              <p style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6, marginBottom: '16px' }}>
                {item.summary}
              </p>

              {item.source && (
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  paddingTop: '12px',
                  borderTop: '1px solid var(--border-subtle)',
                  fontSize: '12px',
                  color: 'var(--text-muted)'
                }}>
                  <span>Source: {item.source.title}</span>
                  <a 
                    href={item.source.url} 
                    target="_blank" 
                    rel="noopener noreferrer" 
                    style={{ color: 'var(--cyan)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
                  >
                    <span>View PIB Release</span>
                    <ExternalLink size={12} />
                  </a>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
