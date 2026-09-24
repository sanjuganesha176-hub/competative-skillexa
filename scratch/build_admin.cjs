const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '..', 'client', 'src', 'pages', 'AdminDashboardPage.jsx');
let content = fs.readFileSync(filePath, 'utf8');

// 1. Update imports
const oldImport = `import { 
  ShieldCheck, 
  CheckCircle, 
  FileText, 
  Plus, 
  Upload, 
  Award, 
  BookOpen, 
  ExternalLink, 
  Layers, 
  Sparkles, 
  AlertCircle, 
  Edit2, 
  Trash2, 
  Globe, 
  Calendar, 
  Eye, 
  EyeOff
} from 'lucide-react';`;

const newImport = `import { 
  ShieldCheck, 
  CheckCircle, 
  FileText, 
  Plus, 
  Upload, 
  Award, 
  BookOpen, 
  ExternalLink, 
  Layers, 
  Sparkles, 
  AlertCircle, 
  Edit2, 
  Trash2, 
  Globe, 
  Calendar, 
  Eye, 
  EyeOff,
  Building2,
  Bell,
  Send,
  AlertTriangle,
  CheckCircle2,
  Filter,
  Search,
  X,
  ChevronRight
} from 'lucide-react';`;

content = content.replace(oldImport, newImport);

// 2. Change default activeTab to 'govt-exams' and add state
const oldStateStart = `export default function AdminDashboardPage({ navigateTo }) {
  const [activeTab, setActiveTab] = useState('pyqs'); // 'pyqs' | 'current-affairs'
  const [adminData, setAdminData] = useState(null);
  const [statusFilter, setStatusFilter] = useState('');
  const [loading, setLoading] = useState(true);`;

const newStateStart = `export default function AdminDashboardPage({ navigateTo }) {
  const [activeTab, setActiveTab] = useState('govt-exams'); // 'govt-exams' | 'pyqs' | 'current-affairs'
  const [adminData, setAdminData] = useState(null);
  const [statusFilter, setStatusFilter] = useState('');
  const [loading, setLoading] = useState(true);

  // Government Exams State
  const [govtExams, setGovtExams] = useState([]);
  const [govtCounts, setGovtCounts] = useState({ total: 0, draft: 0, pending_review: 0, verified: 0, published: 0, rejected: 0, archived: 0 });
  const [govtStatusFilter, setGovtStatusFilter] = useState('All');
  const [govtCategoryFilter, setGovtCategoryFilter] = useState('All');
  const [govtSearchQuery, setGovtSearchQuery] = useState('');
  const [examCategories, setExamCategories] = useState([]);
  const [showGovtModal, setShowGovtModal] = useState(false);
  const [editingGovt, setEditingGovt] = useState(null);
  const [govtDuplicateWarning, setGovtDuplicateWarning] = useState(null);
  const [showPublishConfirm, setShowPublishConfirm] = useState(null);
  const [sendPushOnPublish, setSendPushOnPublish] = useState(true);
  const [newCatName, setNewCatName] = useState('');
  const [newCatGroup, setNewCatGroup] = useState('Central Government');
  const [showAddCatInline, setShowAddCatInline] = useState(false);

  const defaultGovtForm = {
    exam_name: '',
    organization: 'Staff Selection Commission (SSC)',
    category: 'SSC',
    update_type: 'EXAM_NOTIFICATION',
    official_notification_number: '',
    title: '',
    short_description: '',
    full_description: '',
    post_name: '',
    vacancy: '',
    eligibility: '',
    age_limit: '',
    qualification: '',
    application_fee: '',
    selection_process: '',
    notification_date: new Date().toISOString().split('T')[0],
    application_start_date: '',
    application_last_date: '',
    correction_date: '',
    exam_date: '',
    admit_card_date: '',
    answer_key_date: '',
    result_date: '',
    official_source_name: 'Official Commission Portal',
    official_source_url: 'https://ssc.gov.in',
    verification_status: 'DRAFT',
    send_push_notification: false
  };

  const [govtForm, setGovtForm] = useState(defaultGovtForm);`;

content = content.replace(oldStateStart, newStateStart);

// 3. Update useEffect and add Government Exam Handlers
const oldEffect = `  useEffect(() => {
    fetchAdminData();
  }, [statusFilter]);`;

const newEffectAndHandlers = `  useEffect(() => {
    if (activeTab === 'govt-exams') {
      fetchGovtExams();
      fetchCategories();
    } else {
      fetchAdminData();
    }
  }, [activeTab, statusFilter, govtStatusFilter, govtCategoryFilter]);

  const fetchGovtExams = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (govtStatusFilter !== 'All') params.append('status', govtStatusFilter);
      if (govtCategoryFilter !== 'All') params.append('category', govtCategoryFilter);
      if (govtSearchQuery.trim()) params.append('search', govtSearchQuery.trim());

      const res = await fetch(\`http://localhost:3001/api/admin/government-exams/all?\${params.toString()}\`);
      if (res.ok) {
        const data = await res.json();
        setGovtExams(data.data || []);
        setGovtCounts(data.counts || {});
      }
    } catch (err) {
      console.error('Error fetching admin govt exams:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchCategories = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/exam-categories');
      if (res.ok) {
        const data = await res.json();
        setExamCategories(data.data || []);
      }
    } catch (err) {
      console.error('Error loading categories:', err);
    }
  };

  const handleOpenGovtModal = (exam = null) => {
    setGovtDuplicateWarning(null);
    if (exam) {
      setEditingGovt(exam);
      setGovtForm({
        exam_name: exam.exam_name || '',
        organization: exam.organization || '',
        category: exam.category || 'SSC',
        update_type: exam.update_type || 'EXAM_NOTIFICATION',
        official_notification_number: exam.official_notification_number || '',
        title: exam.title || '',
        short_description: exam.short_description || '',
        full_description: exam.full_description || '',
        post_name: exam.post_name || '',
        vacancy: exam.vacancy || '',
        eligibility: exam.eligibility || '',
        age_limit: exam.age_limit || '',
        qualification: exam.qualification || '',
        application_fee: exam.application_fee || '',
        selection_process: exam.selection_process || '',
        notification_date: exam.notification_date || '',
        application_start_date: exam.application_start_date || '',
        application_last_date: exam.application_last_date || '',
        correction_date: exam.correction_date || '',
        exam_date: exam.exam_date || '',
        admit_card_date: exam.admit_card_date || '',
        answer_key_date: exam.answer_key_date || '',
        result_date: exam.result_date || '',
        official_source_name: exam.official_source_name || '',
        official_source_url: exam.official_source_url || '',
        verification_status: exam.verification_status || 'DRAFT',
        send_push_notification: false
      });
    } else {
      setEditingGovt(null);
      setGovtForm(defaultGovtForm);
    }
    setShowGovtModal(true);
  };

  const handleSaveGovtExam = async (e, force = false) => {
    if (e && e.preventDefault) e.preventDefault();
    if (!govtForm.exam_name || !govtForm.organization || !govtForm.title) {
      alert('Exam Name, Organization, and Title are mandatory.');
      return;
    }
    if (!govtForm.official_source_name || !govtForm.official_source_url) {
      alert('Official Source Name and Official Source URL are mandatory.');
      return;
    }

    try {
      const payload = { ...govtForm, force_duplicate: force };
      let res;
      if (editingGovt) {
        res = await fetch(\`http://localhost:3001/api/admin/government-exams/\${editingGovt.id}\`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } else {
        res = await fetch('http://localhost:3001/api/admin/government-exams', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }

      const resData = await res.json();
      if (res.status === 409 && resData.is_duplicate) {
        setGovtDuplicateWarning(resData.error);
        return;
      }

      if (res.ok) {
        alert(editingGovt ? 'Exam update updated successfully!' : 'Exam update created successfully!');
        setShowGovtModal(false);
        setGovtDuplicateWarning(null);
        fetchGovtExams();
      } else {
        alert(resData.error || 'Failed to save exam update.');
      }
    } catch (err) {
      console.error(err);
      alert('Error saving exam update.');
    }
  };

  const handleTransitionStatus = async (id, newStatus, sendPush = false) => {
    try {
      const res = await fetch(\`http://localhost:3001/api/admin/government-exams/\${id}/status\`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus, send_push_notification: sendPush })
      });
      const data = await res.json();
      if (res.ok) {
        if (data.notification_dispatched) {
          alert(\`Status transitioned to \${newStatus}. Push notification dispatched to eligible students!\`);
        } else {
          alert(\`Status transitioned to \${newStatus}.\`);
        }
        setShowPublishConfirm(null);
        fetchGovtExams();
      } else {
        alert(data.error || 'Failed to transition status.');
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteGovtExam = async (id, name) => {
    if (!window.confirm(\`Are you sure you want to delete exam update: "\${name}"?\`)) return;
    try {
      const res = await fetch(\`http://localhost:3001/api/admin/government-exams/\${id}\`, {
        method: 'DELETE'
      });
      if (res.ok) {
        alert('Deleted successfully.');
        fetchGovtExams();
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleCheckDeadlines = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/notifications/check-deadlines', { method: 'POST' });
      const data = await res.json();
      alert(\`Deadline scan completed! \${data.reminders_sent || 0} deadline reminders sent to students.\`);
    } catch (err) {
      console.error(err);
    }
  };

  const handleAddCategory = async (e) => {
    e.preventDefault();
    if (!newCatName.trim()) return;
    try {
      const res = await fetch('http://localhost:3001/api/admin/exam-categories', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newCatName.trim(), group: newCatGroup })
      });
      if (res.ok) {
        alert('Category added successfully!');
        setNewCatName('');
        setShowAddCatInline(false);
        fetchCategories();
      } else {
        const d = await res.json();
        alert(d.error || 'Failed to add category');
      }
    } catch (err) {
      console.error(err);
    }
  };`;

content = content.replace(oldEffect, newEffectAndHandlers);

// 4. Update Header actions and tab buttons
const oldTopButtons = `          <div style={{ display: 'flex', gap: '10px' }}>
            {activeTab === 'pyqs' ? (
              <button 
                className="btn btn-primary"
                onClick={() => setShowAddModal(true)}
              >
                <Plus size={16} />
                <span>Add Verified PYQ</span>
              </button>
            ) : (
              <button 
                className="btn btn-emerald"
                onClick={() => handleOpenCaModal()}
              >
                <Plus size={16} />
                <span>Add Current Affair</span>
              </button>
            )}
          </div>`;

const newTopButtons = `          <div style={{ display: 'flex', gap: '10px' }}>
            {activeTab === 'govt-exams' && (
              <>
                <button 
                  className="btn btn-secondary"
                  onClick={handleCheckDeadlines}
                  title="Check application deadlines closing in 1-3 days"
                  style={{ fontSize: '13px', gap: '6px' }}
                >
                  <Bell size={15} color="var(--amber)" />
                  <span>Scan Deadlines</span>
                </button>
                <button 
                  className="btn btn-primary"
                  onClick={() => handleOpenGovtModal()}
                >
                  <Plus size={16} />
                  <span>Create Exam Update</span>
                </button>
              </>
            )}
            {activeTab === 'pyqs' && (
              <button 
                className="btn btn-primary"
                onClick={() => setShowAddModal(true)}
              >
                <Plus size={16} />
                <span>Add Verified PYQ</span>
              </button>
            )}
            {activeTab === 'current-affairs' && (
              <button 
                className="btn btn-emerald"
                onClick={() => handleOpenCaModal()}
              >
                <Plus size={16} />
                <span>Add Current Affair</span>
              </button>
            )}
          </div>`;

content = content.replace(oldTopButtons, newTopButtons);

// 5. Update Tab Switcher
const oldTabSwitcher = `        {/* Tab Switcher */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '20px' }}>
          <button
            className={\`btn \${activeTab === 'pyqs' ? 'btn-primary' : 'btn-secondary'}\`}
            onClick={() => setActiveTab('pyqs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <BookOpen size={15} />
            <span>Curriculum PYQs & Lessons</span>
          </button>
          <button
            className={\`btn \${activeTab === 'current-affairs' ? 'btn-primary' : 'btn-secondary'}\`}
            onClick={() => setActiveTab('current-affairs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Award size={15} />
            <span>Current Affairs Management</span>
          </button>
        </div>`;

const newTabSwitcher = `        {/* Tab Switcher */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '20px', flexWrap: 'wrap' }}>
          <button
            className={\`btn \${activeTab === 'govt-exams' ? 'btn-primary' : 'btn-secondary'}\`}
            onClick={() => setActiveTab('govt-exams')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Building2 size={15} />
            <span>Government Exams Management</span>
          </button>
          <button
            className={\`btn \${activeTab === 'pyqs' ? 'btn-primary' : 'btn-secondary'}\`}
            onClick={() => setActiveTab('pyqs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <BookOpen size={15} />
            <span>Curriculum PYQs & Lessons</span>
          </button>
          <button
            className={\`btn \${activeTab === 'current-affairs' ? 'btn-primary' : 'btn-secondary'}\`}
            onClick={() => setActiveTab('current-affairs')}
            style={{ fontSize: '13.5px', padding: '8px 18px' }}
          >
            <Award size={15} />
            <span>Current Affairs Management</span>
          </button>
        </div>`;

content = content.replace(oldTabSwitcher, newTabSwitcher);

// 6. Insert Government Exams Tab View before activeTab === 'pyqs'
const pyqTabMarker = `{/* ==========================================
          TAB 1: CURRICULUM PYQS & LESSONS
          ========================================== */}`;

const govtTabJSX = `{/* ==========================================
          TAB: GOVERNMENT EXAMS UPDATES CONSOLE
          ========================================== */}
      {activeTab === 'govt-exams' && (
        <div>
          {/* Stats Bar */}
          <div className="stats-grid" style={{ marginBottom: '24px' }}>
            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--primary-light)' }}>
                <Building2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.total || 0}</div>
                <div className="stat-label">Total Exam Updates</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--amber)' }}>
                <Edit2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.draft || 0}</div>
                <div className="stat-label">Drafts (Step 1)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--cyan)' }}>
                <FileText size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.pending_review || 0}</div>
                <div className="stat-label">Pending Review (Step 2)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: '#c084fc' }}>
                <ShieldCheck size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.verified || 0}</div>
                <div className="stat-label">Verified (Step 3)</div>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon-wrap" style={{ color: 'var(--emerald)' }}>
                <CheckCircle2 size={20} />
              </div>
              <div className="stat-info">
                <div className="stat-value">{govtCounts.published || 0}</div>
                <div className="stat-label">Published (Step 4 Live)</div>
              </div>
            </div>
          </div>

          {/* Workflow Banner */}
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '14px 20px',
            borderRadius: 'var(--radius-md)',
            background: 'rgba(6, 182, 212, 0.08)',
            border: '1px solid rgba(6, 182, 212, 0.25)',
            marginBottom: '20px',
            fontSize: '13px',
            color: 'var(--text-secondary)',
            flexWrap: 'wrap'
          }}>
            <span style={{ fontWeight: 700, color: '#fff' }}>Mandatory Verification Workflow:</span>
            <span className="badge badge-subtle">1. DRAFT</span>
            <span>→</span>
            <span className="badge badge-amber">2. PENDING REVIEW</span>
            <span>→</span>
            <span className="badge badge-cyan">3. VERIFIED</span>
            <span>→</span>
            <span className="badge badge-emerald">4. PUBLISHED (Visible to Students)</span>
            <span style={{ marginLeft: 'auto', fontSize: '12px', color: 'var(--text-muted)' }}>
              Normal users only see VERIFIED + PUBLISHED updates.
            </span>
          </div>

          {/* Filters Toolbar */}
          <div className="glass-card" style={{ padding: '18px 24px', marginBottom: '20px' }}>
            <div style={{ display: 'flex', gap: '16px', alignItems: 'center', flexWrap: 'wrap', justifyContent: 'space-between' }}>
              
              {/* Search */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255,255,255,0.04)', padding: '6px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', minWidth: '260px' }}>
                <Search size={15} color="var(--text-muted)" />
                <input 
                  type="text" 
                  placeholder="Search exam, org, title..."
                  value={govtSearchQuery}
                  onChange={e => setGovtSearchQuery(e.target.value)}
                  style={{ background: 'transparent', border: 'none', color: '#fff', fontSize: '13px', outline: 'none', width: '100%' }}
                />
              </div>

              {/* Status Filter */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>Status:</span>
                <select
                  value={govtStatusFilter}
                  onChange={e => setGovtStatusFilter(e.target.value)}
                  className="admin-select"
                  style={{ fontSize: '12.5px', padding: '6px 10px' }}
                >
                  <option value="All">All Statuses</option>
                  <option value="DRAFT">DRAFT</option>
                  <option value="PENDING_REVIEW">PENDING_REVIEW</option>
                  <option value="VERIFIED">VERIFIED</option>
                  <option value="PUBLISHED">PUBLISHED</option>
                  <option value="REJECTED">REJECTED</option>
                  <option value="ARCHIVED">ARCHIVED</option>
                </select>
              </div>

              {/* Category Filter */}
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '12.5px', color: 'var(--text-muted)' }}>Category:</span>
                <select
                  value={govtCategoryFilter}
                  onChange={e => setGovtCategoryFilter(e.target.value)}
                  className="admin-select"
                  style={{ fontSize: '12.5px', padding: '6px 10px' }}
                >
                  <option value="All">All Categories</option>
                  {examCategories.map(c => (
                    <option key={c.id} value={c.name}>{c.name}</option>
                  ))}
                </select>
              </div>

              {/* Add category shortcut */}
              <button 
                className="btn btn-subtle"
                onClick={() => setShowAddCatInline(!showAddCatInline)}
                style={{ fontSize: '12px', padding: '6px 10px' }}
              >
                + New Category
              </button>
            </div>

            {/* Inline Add Category Form */}
            {showAddCatInline && (
              <form onSubmit={handleAddCategory} style={{ display: 'flex', gap: '10px', alignItems: 'center', marginTop: '14px', paddingTop: '14px', borderTop: '1px solid var(--border-subtle)' }}>
                <input 
                  type="text" 
                  placeholder="Category Name (e.g. Metro Rail, Police Sub-Inspector)"
                  value={newCatName}
                  onChange={e => setNewCatName(e.target.value)}
                  style={{ padding: '6px 12px', background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '13px', flex: 1 }}
                  required
                />
                <select 
                  value={newCatGroup}
                  onChange={e => setNewCatGroup(e.target.value)}
                  style={{ padding: '6px 12px', background: 'var(--bg-dark)', border: '1px solid var(--border-subtle)', borderRadius: '4px', color: '#fff', fontSize: '13px' }}
                >
                  <option value="Central Government">Central Government</option>
                  <option value="State Government">State Government</option>
                </select>
                <button type="submit" className="btn btn-primary" style={{ fontSize: '12.5px', padding: '6px 14px' }}>
                  Add Category
                </button>
              </form>
            )}
          </div>

          {/* Updates Table */}
          <div className="glass-card" style={{ padding: '24px' }}>
            {govtExams.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '48px 20px', color: 'var(--text-muted)' }}>
                <Building2 size={36} color="var(--text-muted)" style={{ margin: '0 auto 12px' }} />
                <h4 style={{ fontSize: '16px', fontWeight: 600, color: '#f8fafc', marginBottom: '6px' }}>
                  No Government Exam Updates Found
                </h4>
                <p style={{ fontSize: '13.5px', maxWidth: '440px', margin: '0 auto 16px' }}>
                  Create a new update following the official gazette to start the Source → Review → Verification → Publish workflow.
                </p>
                <button className="btn btn-primary" onClick={() => handleOpenGovtModal()}>
                  <Plus size={15} />
                  <span>Create First Exam Update</span>
                </button>
              </div>
            ) : (
              <div style={{ overflowX: 'auto' }}>
                <table className="admin-table">
                  <thead>
                    <tr>
                      <th>Exam & Org</th>
                      <th>Category & Type</th>
                      <th>Key Dates</th>
                      <th>Official Source</th>
                      <th>Status</th>
                      <th>Workflow Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {govtExams.map(exam => {
                      const status = exam.verification_status;
                      return (
                        <tr key={exam.id}>
                          <td>
                            <div style={{ fontWeight: 700, color: '#f8fafc', fontSize: '14px' }}>
                              {exam.exam_name}
                            </div>
                            <div style={{ fontSize: '12px', color: 'var(--cyan)' }}>
                              {exam.organization}
                            </div>
                            {exam.official_notification_number && (
                              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                                Ref: {exam.official_notification_number}
                              </div>
                            )}
                          </td>
                          <td>
                            <span className="badge badge-primary" style={{ fontSize: '11px', marginBottom: '4px', display: 'inline-block' }}>
                              {exam.category}
                            </span>
                            <div style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                              {exam.update_type}
                            </div>
                          </td>
                          <td style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>
                            {exam.application_last_date && (
                              <div>Last Date: <strong style={{ color: '#fff' }}>{exam.application_last_date}</strong></div>
                            )}
                            {exam.exam_date && (
                              <div>Exam: <strong style={{ color: 'var(--cyan)' }}>{exam.exam_date}</strong></div>
                            )}
                            {exam.result_date && (
                              <div>Result: <strong style={{ color: 'var(--emerald)' }}>{exam.result_date}</strong></div>
                            )}
                          </td>
                          <td>
                            <div style={{ fontSize: '12px', color: '#f8fafc' }}>
                              {exam.official_source_name}
                            </div>
                            <a 
                              href={exam.official_source_url} 
                              target="_blank" 
                              rel="noopener noreferrer" 
                              style={{ fontSize: '11.5px', color: 'var(--cyan)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
                            >
                              <span>Official Link</span>
                              <ExternalLink size={11} />
                            </a>
                          </td>
                          <td>
                            <span className={\`badge \${
                              status === 'PUBLISHED' ? 'badge-emerald' :
                              status === 'VERIFIED' ? 'badge-cyan' :
                              status === 'PENDING_REVIEW' ? 'badge-amber' :
                              status === 'REJECTED' ? 'badge-rose' : 'badge-subtle'
                            }\`}>
                              {status}
                            </span>
                            {status === 'PUBLISHED' && (
                              <div style={{ fontSize: '11px', color: 'var(--emerald)', marginTop: '2px' }}>
                                Live in student app ✓
                              </div>
                            )}
                          </td>
                          <td>
                            <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', alignItems: 'center' }}>
                              {/* Workflow Step Transitions */}
                              {status === 'DRAFT' && (
                                <button 
                                  className="btn btn-secondary" 
                                  onClick={() => handleTransitionStatus(exam.id, 'PENDING_REVIEW')}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Submit to editorial review"
                                >
                                  Submit for Review →
                                </button>
                              )}

                              {status === 'PENDING_REVIEW' && (
                                <button 
                                  className="btn btn-primary" 
                                  onClick={() => handleTransitionStatus(exam.id, 'VERIFIED')}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Confirm verification against official gazette"
                                >
                                  Verify Data ✓
                                </button>
                              )}

                              {status === 'VERIFIED' && (
                                <button 
                                  className="btn btn-emerald" 
                                  onClick={() => setShowPublishConfirm(exam)}
                                  style={{ fontSize: '11.5px', padding: '4px 10px' }}
                                  title="Publish to students with optional push notification"
                                >
                                  Publish 🚀
                                </button>
                              )}

                              {status === 'PUBLISHED' && (
                                <button 
                                  className="btn btn-subtle" 
                                  onClick={() => handleTransitionStatus(exam.id, 'DRAFT')}
                                  style={{ fontSize: '11px', padding: '4px 8px' }}
                                  title="Unpublish back to draft"
                                >
                                  Unpublish
                                </button>
                              )}

                              {/* Edit & Delete */}
                              <button 
                                className="btn-icon" 
                                onClick={() => handleOpenGovtModal(exam)}
                                title="Edit update details"
                                style={{ width: '28px', height: '28px' }}
                              >
                                <Edit2 size={13} />
                              </button>
                              <button 
                                className="btn-icon" 
                                onClick={() => handleDeleteGovtExam(exam.id, exam.exam_name)}
                                title="Delete update"
                                style={{ width: '28px', height: '28px', color: 'var(--rose)' }}
                              >
                                <Trash2 size={13} />
                              </button>
                            </div>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      )}

      ` + pyqTabMarker;

content = content.replace(pyqTabMarker, govtTabJSX);

// 7. Insert Govt Modals before end of component
const componentEnd = `      {/* Add Verified PYQ Modal */}`;

const govtModalsJSX = `{/* ==========================================
          MODAL: CREATE / EDIT GOVERNMENT EXAM UPDATE
          ========================================== */}
      {showGovtModal && (
        <div className="modal-backdrop" onClick={() => setShowGovtModal(false)}>
          <div 
            className="modal-content" 
            onClick={e => e.stopPropagation()} 
            style={{ maxWidth: '820px', maxHeight: '90vh', overflowY: 'auto' }}
          >
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Building2 size={20} color="var(--cyan)" />
                <h3 style={{ fontSize: '18px', fontWeight: 700 }}>
                  {editingGovt ? \`Edit Exam Update: \${editingGovt.exam_name}\` : 'Create Government Exam Update'}
                </h3>
              </div>
              <button className="btn-icon" onClick={() => setShowGovtModal(false)}>
                <X size={16} />
              </button>
            </div>

            {/* Duplicate Warning Alert */}
            {govtDuplicateWarning && (
              <div style={{
                margin: '16px 24px 0',
                padding: '12px 16px',
                borderRadius: 'var(--radius-sm)',
                background: 'rgba(245, 158, 11, 0.15)',
                border: '1px solid var(--amber)',
                color: '#fef3c7',
                fontSize: '13px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                gap: '12px'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <AlertTriangle size={18} color="var(--amber)" />
                  <span>{govtDuplicateWarning}</span>
                </div>
                <button 
                  type="button" 
                  className="btn btn-secondary" 
                  onClick={(e) => handleSaveGovtExam(e, true)}
                  style={{ fontSize: '11.5px', padding: '4px 10px', background: 'rgba(0,0,0,0.3)' }}
                >
                  Force Save Anyway
                </button>
              </div>
            )}

            <form onSubmit={handleSaveGovtExam} style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              
              {/* Section 1: Basic Classification */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  1. Examination Classification
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Exam Name *</label>
                    <input 
                      type="text" 
                      value={govtForm.exam_name}
                      onChange={e => setGovtForm({ ...govtForm, exam_name: e.target.value })}
                      placeholder="e.g., SSC CGL 2026, UPSC CDS II 2026"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Organization *</label>
                    <input 
                      type="text" 
                      value={govtForm.organization}
                      onChange={e => setGovtForm({ ...govtForm, organization: e.target.value })}
                      placeholder="e.g., Staff Selection Commission (SSC)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Category *</label>
                    <select
                      value={govtForm.category}
                      onChange={e => setGovtForm({ ...govtForm, category: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    >
                      {examCategories.map(c => (
                        <option key={c.id} value={c.name}>{c.name} ({c.group})</option>
                      ))}
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Update Type *</label>
                    <select
                      value={govtForm.update_type}
                      onChange={e => setGovtForm({ ...govtForm, update_type: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    >
                      <option value="EXAM_NOTIFICATION">🔔 Exam Notification</option>
                      <option value="APPLICATION_OPEN">📝 Application Open</option>
                      <option value="APPLICATION_CLOSING">⏳ Application Closing</option>
                      <option value="ADMIT_CARD">🎟️ Admit Card Released</option>
                      <option value="EXAM_DATE">📅 Exam Date Announced</option>
                      <option value="ANSWER_KEY">🔑 Answer Key Released</option>
                      <option value="RESULT">🏆 Result Released</option>
                      <option value="CUTOFF">📊 Cut-off / Merit List</option>
                      <option value="JOB_NOTIFICATION">💼 Government Job Recruitment</option>
                      <option value="IMPORTANT_NOTICE">⚠️ Important Official Notice</option>
                    </select>
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Notification Number (Ref)</label>
                    <input 
                      type="text" 
                      value={govtForm.official_notification_number}
                      onChange={e => setGovtForm({ ...govtForm, official_notification_number: e.target.value })}
                      placeholder="e.g., SSC/2026/01-CGL"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 2: Titles & Descriptions */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  2. Headline & Descriptions
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Short Title *</label>
                    <input 
                      type="text" 
                      value={govtForm.title}
                      onChange={e => setGovtForm({ ...govtForm, title: e.target.value })}
                      placeholder="e.g., SSC CGL 2026 Application Notification Released"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Short Summary (Card View)</label>
                    <input 
                      type="text" 
                      value={govtForm.short_description}
                      onChange={e => setGovtForm({ ...govtForm, short_description: e.target.value })}
                      placeholder="Application form is now active on the official SSC portal. Apply before deadline."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Full Verified Notice Text</label>
                    <textarea 
                      rows={3}
                      value={govtForm.full_description}
                      onChange={e => setGovtForm({ ...govtForm, full_description: e.target.value })}
                      placeholder="Enter verified description, exam stages, syllabus reference, and official instructions..."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff', fontSize: '13.5px' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 3: Recruitment & Eligibility Information */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  3. Job & Eligibility Information (Only Verified Data)
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Post / Job Name</label>
                    <input 
                      type="text" 
                      value={govtForm.post_name}
                      onChange={e => setGovtForm({ ...govtForm, post_name: e.target.value })}
                      placeholder="e.g., Assistant Section Officer, Inspector"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Number of Vacancies</label>
                    <input 
                      type="text" 
                      value={govtForm.vacancy}
                      onChange={e => setGovtForm({ ...govtForm, vacancy: e.target.value })}
                      placeholder="e.g., 17,727 Vacancies"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Age Limit</label>
                    <input 
                      type="text" 
                      value={govtForm.age_limit}
                      onChange={e => setGovtForm({ ...govtForm, age_limit: e.target.value })}
                      placeholder="e.g., 18 - 30 Years (Age relaxation applicable)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Educational Qualification</label>
                    <input 
                      type="text" 
                      value={govtForm.qualification}
                      onChange={e => setGovtForm({ ...govtForm, qualification: e.target.value })}
                      placeholder="e.g., Bachelor's Degree in any discipline"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Application Fee</label>
                    <input 
                      type="text" 
                      value={govtForm.application_fee}
                      onChange={e => setGovtForm({ ...govtForm, application_fee: e.target.value })}
                      placeholder="e.g., ₹100 (SC/ST/Female: Exempted)"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Selection Process</label>
                    <input 
                      type="text" 
                      value={govtForm.selection_process}
                      onChange={e => setGovtForm({ ...govtForm, selection_process: e.target.value })}
                      placeholder="Tier-1 (CBE) + Tier-2 (CBE) + Document Verification"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 4: Important Dates */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  4. Important Verified Dates (Leave blank if unannounced)
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Notification Date</label>
                    <input 
                      type="date" 
                      value={govtForm.notification_date}
                      onChange={e => setGovtForm({ ...govtForm, notification_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Application Start Date</label>
                    <input 
                      type="date" 
                      value={govtForm.application_start_date}
                      onChange={e => setGovtForm({ ...govtForm, application_start_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--amber)', marginBottom: '4px' }}>Application Last Date</label>
                    <input 
                      type="date" 
                      value={govtForm.application_last_date}
                      onChange={e => setGovtForm({ ...govtForm, application_last_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Admit Card Date</label>
                    <input 
                      type="date" 
                      value={govtForm.admit_card_date}
                      onChange={e => setGovtForm({ ...govtForm, admit_card_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--primary-light)', marginBottom: '4px' }}>Exam Date</label>
                    <input 
                      type="date" 
                      value={govtForm.exam_date}
                      onChange={e => setGovtForm({ ...govtForm, exam_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--emerald)', marginBottom: '4px' }}>Result Date</label>
                    <input 
                      type="date" 
                      value={govtForm.result_date}
                      onChange={e => setGovtForm({ ...govtForm, result_date: e.target.value })}
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                    />
                  </div>
                </div>
              </div>

              {/* Section 5: Official Source Reference */}
              <div>
                <h4 style={{ fontSize: '13.5px', fontWeight: 700, color: 'var(--cyan)', textTransform: 'uppercase', marginBottom: '12px' }}>
                  5. Mandatory Official Source Reference
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px' }}>
                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Source Name *</label>
                    <input 
                      type="text" 
                      value={govtForm.official_source_name}
                      onChange={e => setGovtForm({ ...govtForm, official_source_name: e.target.value })}
                      placeholder="e.g., Staff Selection Commission Official Notification"
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>

                  <div>
                    <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Official Portal / Notification URL *</label>
                    <input 
                      type="url" 
                      value={govtForm.official_source_url}
                      onChange={e => setGovtForm({ ...govtForm, official_source_url: e.target.value })}
                      placeholder="https://ssc.gov.in/notice/..."
                      style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', color: '#fff' }}
                      required
                    />
                  </div>
                </div>
              </div>

              {/* Section 6: Workflow Status & Push */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '14px', alignItems: 'center' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', color: 'var(--text-muted)', marginBottom: '4px' }}>Workflow Stage</label>
                  <select
                    value={govtForm.verification_status}
                    onChange={e => setGovtForm({ ...govtForm, verification_status: e.target.value })}
                    style={{ width: '100%', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', background: 'var(--bg-dark)', color: '#fff' }}
                  >
                    <option value="DRAFT">DRAFT (Initial entry)</option>
                    <option value="PENDING_REVIEW">PENDING_REVIEW (Awaiting fact-check)</option>
                    <option value="VERIFIED">VERIFIED (Fact-checked against gazette)</option>
                    <option value="PUBLISHED">PUBLISHED (Live in student app)</option>
                  </select>
                </div>

                {govtForm.verification_status === 'PUBLISHED' && (
                  <div style={{ marginTop: '16px' }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', color: '#f8fafc', cursor: 'pointer' }}>
                      <input 
                        type="checkbox"
                        checked={govtForm.send_push_notification}
                        onChange={e => setGovtForm({ ...govtForm, send_push_notification: e.target.checked })}
                        style={{ accentColor: 'var(--cyan)', width: '16px', height: '16px' }}
                      />
                      <span>Send Push Notification to eligible users upon publishing</span>
                    </label>
                  </div>
                )}
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '12px', marginTop: '12px', borderTop: '1px solid var(--border-subtle)', paddingTop: '16px' }}>
                <button type="button" className="btn btn-secondary" onClick={() => setShowGovtModal(false)}>
                  Cancel
                </button>
                <button type="submit" className="btn btn-primary">
                  <span>{editingGovt ? 'Update Exam Update' : 'Save Exam Update'}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ==========================================
          MODAL: CONFIRM PUBLISHING & PUSH NOTIFICATION
          ========================================== */}
      {showPublishConfirm && (
        <div className="modal-backdrop" onClick={() => setShowPublishConfirm(null)}>
          <div className="modal-content" onClick={e => e.stopPropagation()} style={{ maxWidth: '520px' }}>
            <div style={{ padding: '20px 24px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Send size={18} color="var(--emerald)" />
                <h3 style={{ fontSize: '17px', fontWeight: 700 }}>Confirm Publishing Update</h3>
              </div>
              <button className="btn-icon" onClick={() => setShowPublishConfirm(null)}>
                <X size={16} />
              </button>
            </div>

            <div style={{ padding: '24px' }}>
              <p style={{ color: '#f8fafc', fontSize: '14.5px', marginBottom: '8px' }}>
                Are you ready to publish <strong>{showPublishConfirm.exam_name}</strong> to the student feed?
              </p>
              <p style={{ color: 'var(--text-secondary)', fontSize: '13px', marginBottom: '20px' }}>
                This will make the update immediately visible to all students on the home screen and Government Exams section.
              </p>

              <div style={{
                background: 'rgba(255, 255, 255, 0.03)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-sm)',
                padding: '14px',
                marginBottom: '16px'
              }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13.5px', color: '#f8fafc', cursor: 'pointer' }}>
                  <input 
                    type="checkbox"
                    checked={sendPushOnPublish}
                    onChange={e => setSendPushOnPublish(e.target.checked)}
                    style={{ accentColor: 'var(--cyan)', width: '18px', height: '18px' }}
                  />
                  <span>
                    <strong>Send Push Notification</strong> to students interested in {showPublishConfirm.category} exams
                  </span>
                </label>
              </div>
            </div>

            <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button className="btn btn-secondary" onClick={() => setShowPublishConfirm(null)}>
                Cancel
              </button>
              <button 
                className="btn btn-emerald" 
                onClick={() => handleTransitionStatus(showPublishConfirm.id, 'PUBLISHED', sendPushOnPublish)}
              >
                Confirm & Publish
              </button>
            </div>
          </div>
        </div>
      )}
      
      ` + componentEnd;

content = content.replace(componentEnd, govtModalsJSX);

fs.writeFileSync(filePath, content, 'utf8');
console.log('Successfully updated AdminDashboardPage.jsx!');
