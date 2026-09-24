import React from 'react';
import { ShieldCheck, BookOpen, ExternalLink, Sparkles, Building2 } from 'lucide-react';

export default function Footer({ navigateTo }) {
  return (
    <footer style={{
      borderTop: '1px solid var(--border-subtle)',
      background: 'rgba(8, 13, 26, 0.9)',
      padding: '48px 24px 32px',
      marginTop: 'auto'
    }}>
      <div style={{
        maxWidth: 'var(--max-width)',
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
        gap: '36px',
        marginBottom: '40px'
      }}>
        {/* Col 1: Brand & Mission */}
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '14px' }}>
            <div className="logo-icon" style={{ width: '32px', height: '32px' }}>
              <svg width="20" height="20" viewBox="0 0 32 32" fill="none">
                <path d="M7 23L16 9L25 23M16 13V23" stroke="#06B6D4" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </div>
            <span style={{ fontSize: '18px', fontWeight: 800, color: '#fff' }}>
              Skillexa<span style={{ color: 'var(--cyan)' }}>.</span>
            </span>
          </div>
          <p style={{ color: 'var(--text-secondary)', fontSize: '13.5px', lineHeight: 1.6, marginBottom: '16px' }}>
            A next-generation educational and competitive examination preparation platform. Learn structured concepts, track verified government exams, and unlock advanced topic milestones.
          </p>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span className="badge badge-cyan">
              <ShieldCheck size={12} />
              100% Verified Sources
            </span>
            <span className="badge badge-primary">
              <Sparkles size={12} />
              SSC • UPSC • Banking • KPSC
            </span>
          </div>
        </div>

        {/* Col 2: Quick Links */}
        <div>
          <h4 style={{ fontSize: '14px', fontWeight: 700, color: '#fff', marginBottom: '16px', letterSpacing: '0.04em' }}>
            EXPLORE PLATFORM
          </h4>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '13.5px', color: 'var(--text-secondary)' }}>
            <li>
              <a href="#courses" onClick={(e) => { e.preventDefault(); navigateTo('course', { slug: 'english' }); }} style={{ transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = '#fff'} onMouseLeave={e => e.target.style.color = 'var(--text-secondary)'}>
                English Mastery (22 Unlockable Levels)
              </a>
            </li>
            <li>
              <a href="#math" onClick={(e) => { e.preventDefault(); navigateTo('course', { slug: 'mathematics' }); }} style={{ transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = '#fff'} onMouseLeave={e => e.target.style.color = 'var(--text-secondary)'}>
                Mathematics (15 Core Topics)
              </a>
            </li>
            <li>
              <a href="#reasoning" onClick={(e) => { e.preventDefault(); navigateTo('course', { slug: 'reasoning' }); }} style={{ transition: 'color 0.2s' }} onMouseEnter={e => e.target.style.color = '#fff'} onMouseLeave={e => e.target.style.color = 'var(--text-secondary)'}>
                Reasoning & Analytical Ability
              </a>
            </li>
            <li>
              <a href="#govexams" onClick={(e) => { e.preventDefault(); navigateTo('government-exams'); }} style={{ transition: 'color 0.2s', color: 'var(--cyan)' }} onMouseEnter={e => e.target.style.color = '#fff'} onMouseLeave={e => e.target.style.color = 'var(--cyan)'}>
                Verified Government Exams & Job Updates →
              </a>
            </li>
          </ul>
        </div>

        {/* Col 3: Source Verification Standards */}
        <div>
          <h4 style={{ fontSize: '14px', fontWeight: 700, color: '#fff', marginBottom: '16px', letterSpacing: '0.04em' }}>
            VERIFICATION STANDARD
          </h4>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px', lineHeight: 1.6, marginBottom: '12px' }}>
            All exam notifications are validated against official government portals (Staff Selection Commission, UPSC, KPSC, Railway RRB). Grammar lessons reference authoritative academic databases including British Council and Cambridge.
          </p>
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
            <span style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '4px', background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-secondary)' }}>
              SSC (ssc.gov.in)
            </span>
            <span style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '4px', background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-secondary)' }}>
              UPSC (upsc.gov.in)
            </span>
            <span style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '4px', background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-secondary)' }}>
              KPSC Karnataka
            </span>
            <span style={{ fontSize: '11px', padding: '3px 8px', borderRadius: '4px', background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-secondary)' }}>
              Press Information Bureau
            </span>
          </div>
        </div>
      </div>

      {/* Bottom bar */}
      <div style={{
        maxWidth: 'var(--max-width)',
        margin: '0 auto',
        paddingTop: '20px',
        borderTop: '1px solid var(--border-subtle)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px',
        fontSize: '12.5px',
        color: 'var(--text-muted)'
      }}>
        <div>
          © {new Date().getFullYear()} Skillexa EdTech. All rights reserved. • Learn • Practice • Grow
        </div>
        <div style={{ display: 'flex', gap: '16px' }}>
          <span style={{ cursor: 'pointer', color: '#a5b4fc' }} onClick={() => navigateTo('admin')}>
            Admin Management
          </span>
          <span style={{ cursor: 'pointer' }} onClick={() => navigateTo('profile')}>
            User Profile & Settings
          </span>
        </div>
      </div>
    </footer>
  );
}
