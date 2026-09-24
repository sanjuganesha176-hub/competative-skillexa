import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const DB_FILE = path.join(__dirname, 'data', 'skillexa.json');

// In-memory cache + persistent JSON backing
let db = {
  users: [],
  courses: [],
  modules: [],
  topics: [],
  lessons: [],
  sources: [],
  exams: [],
  previous_year_questions: [],
  practice_questions: [],
  quiz_questions: [],
  quiz_attempts: [],
  user_topic_progress: [],
  current_affairs: [],
  government_exam_updates: [],
  notifications: [],
  notification_preferences: [],
  user_notification_tokens: [],
  exam_categories: [],
  notes: [],
  mock_exams: []
};

const DEFAULT_CATEGORIES = [
  { id: 1, key: 'SSC', name: 'SSC', group: 'Central Government', description: 'Staff Selection Commission (CGL, CHSL, MTS, CPO, GD)' },
  { id: 2, key: 'UPSC', name: 'UPSC', group: 'Central Government', description: 'Union Public Service Commission (CSE, CDS, NDA, CAPF)' },
  { id: 3, key: 'Railway', name: 'Railway / RRB', group: 'Central Government', description: 'Railway Recruitment Board (NTPC, Group D, ALP, JE)' },
  { id: 4, key: 'Banking', name: 'Banking', group: 'Central Government', description: 'IBPS, SBI, RBI (PO, Clerk, SO, Assistant)' },
  { id: 5, key: 'Defence', name: 'Defence', group: 'Central Government', description: 'Indian Army, Navy, Air Force, AFCAT, Coast Guard' },
  { id: 6, key: 'Teaching', name: 'Teaching', group: 'Central Government', description: 'CTET, KVS, NVS, UGC NET' },
  { id: 7, key: 'Other Central', name: 'Other Central Government Exams', group: 'Central Government', description: 'ISRO, DRDO, Intelligence Bureau, SSC Scientific' },
  { id: 8, key: 'KPSC', name: 'KPSC', group: 'State Government', description: 'Karnataka Public Service Commission (KAS, FDA, SDA, Gazetted Probationers)' },
  { id: 9, key: 'Karnataka State', name: 'Karnataka Government Jobs', group: 'State Government', description: 'Karnataka State Departmental Recruitment & Boards' },
  { id: 10, key: 'Police', name: 'Police', group: 'State Government', description: 'State Police Sub-Inspector, Constable, Armed Police' },
  { id: 11, key: 'State Teaching', name: 'State Teaching Exams', group: 'State Government', description: 'State Teacher Eligibility Test, High School Teacher Recruitment' },
  { id: 12, key: 'Other State', name: 'Other State Government Exams', group: 'State Government', description: 'Other State Public Service Commissions & Departmental Exams' }
];

export function initDatabase(initialSeed) {
  try {
    if (fs.existsSync(DB_FILE)) {
      const data = fs.readFileSync(DB_FILE, 'utf-8');
      db = JSON.parse(data);
      console.log('Loaded database from', DB_FILE);
    } else {
      console.log('Initializing database with seed data...');
      db = initialSeed || {};
    }

    // Ensure all tables exist in memory
    const requiredTables = [
      'users', 'courses', 'modules', 'topics', 'lessons', 'sources', 'exams',
      'previous_year_questions', 'practice_questions', 'quiz_questions',
      'quiz_attempts', 'user_topic_progress', 'current_affairs',
      'government_exam_updates', 'notifications', 'notification_preferences',
      'user_notification_tokens', 'exam_categories', 'notes', 'mock_exams'
    ];

    requiredTables.forEach(table => {
      if (!Array.isArray(db[table])) {
        db[table] = [];
      }
    });

    // Populate expandable exam categories if missing
    if (!db.exam_categories || db.exam_categories.length === 0) {
      db.exam_categories = DEFAULT_CATEGORIES;
    }

    // Populate default notification preferences for existing users if missing
    if (!db.notification_preferences || db.notification_preferences.length === 0) {
      db.notification_preferences = [
        {
          id: 1,
          user_id: 1,
          exam_notifications: true,
          application_updates: true,
          admit_card_updates: true,
          exam_date_updates: true,
          answer_key_updates: true,
          result_updates: true,
          job_notifications: true,
          category_preferences: ['SSC', 'UPSC', 'Railway', 'Banking', 'KPSC', 'Defence', 'Teaching', 'Police'],
          updated_at: new Date().toISOString()
        }
      ];
    }

    // Seed full-length 50-question mock exams if missing
    if (!db.mock_exams || db.mock_exams.length === 0) {
      const qList = db.quiz_questions || [];
      const englishQs = qList.filter(q => (q.subject || '').includes('English'));
      const mathQs = qList.filter(q => (q.subject || '').includes('Math'));
      const reasonQs = qList.filter(q => (q.subject || '').includes('Reason'));
      const gaQs = qList.filter(q => (q.subject || '').includes('Awareness'));
      const sciQs = qList.filter(q => (q.subject || '').includes('Science'));

      const set1 = [
        ...englishQs.slice(0, 15),
        ...mathQs.slice(0, 15),
        ...reasonQs.slice(0, 10),
        ...gaQs.slice(0, 10)
      ];

      const set2 = [
        ...englishQs.slice(15, 25),
        ...mathQs.slice(15, 25),
        ...reasonQs.slice(10, 20),
        ...sciQs.slice(0, 10),
        ...gaQs.slice(10, 20)
      ];

      const now = new Date().toISOString();
      db.mock_exams = [
        {
          id: 1,
          title: "SSC CGL Tier-1 Grand Full-Length Mock Exam #1",
          category: "SSC",
          target_exam: "SSC CGL / CHSL",
          description: "Full-length 50-question comprehensive mock examination following the official Staff Selection Commission pattern covering English Comprehension, Quantitative Aptitude, General Intelligence & Reasoning, and General Awareness.",
          duration_minutes: 60,
          total_questions: set1.length >= 50 ? set1.length : 50,
          total_marks: 100,
          passing_percentage: 70,
          negative_marking: 0.25,
          instructions: "1. The exam contains exactly 50 objective multiple-choice questions.\n2. Total time allotted is 60 minutes.\n3. Each question carries 2 marks (total 100 marks).\n4. Negative marking of 0.25 marks applies to incorrect responses.\n5. You can navigate between questions and review marked answers before final submission.",
          question_ids: set1.map(q => q.id),
          status: "published",
          created_by: "Administrator",
          created_at: now,
          updated_at: now
        },
        {
          id: 2,
          title: "All-India Competitive Multi-Subject Speed Mock Test #2",
          category: "Central Government",
          target_exam: "UPSC / Railway / Banking / State PSC",
          description: "Curated 50-question high-yield mock test designed to benchmark speed and accuracy across English Language, Numerical Ability, Logical Reasoning, General Science, and Current National Awareness.",
          duration_minutes: 60,
          total_questions: set2.length >= 50 ? set2.length : 50,
          total_marks: 100,
          passing_percentage: 70,
          negative_marking: 0.25,
          instructions: "1. Exam contains 50 questions across 5 core competitive subjects.\n2. Time duration: 60 minutes.\n3. Passing cutoff: 70%.\n4. Recommended for Banking PO/Clerk, Railway RRB NTPC, and State PSC aspirants.",
          question_ids: set2.map(q => q.id),
          status: "published",
          created_by: "Administrator",
          created_at: now,
          updated_at: now
        }
      ];
    }

    // Enrich user 1 profile if missing extra profile fields
    const user1 = db.users?.find(u => u.id === 1);
    if (user1) {
      if (!user1.target_exams) user1.target_exams = ['SSC CGL', 'UPSC CDS', 'KPSC KAS'];
      if (!user1.state) user1.state = 'Karnataka';
      if (!user1.bio) user1.bio = 'Aspirant preparing for Central and State government competitive exams. Focusing on English, Quantitative Aptitude, and General Awareness.';
      if (!user1.phone) user1.phone = '+91 98765 43210';
      if (!user1.education) user1.education = 'Bachelor of Science (B.Sc)';
    }

    saveDatabase();
  } catch (err) {
    console.error('Error initializing database, using seed:', err);
    db = initialSeed || {};
    saveDatabase();
  }
}

export function saveDatabase() {
  try {
    const dir = path.dirname(DB_FILE);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFileSync(DB_FILE, JSON.stringify(db, null, 2), 'utf-8');
  } catch (err) {
    console.error('Failed to save database to disk:', err);
  }
}

export const dbService = {
  find(table, filter = {}) {
    const items = db[table] || [];
    return items.filter(item => {
      for (const key in filter) {
        if (filter[key] !== undefined && item[key] !== filter[key]) {
          return false;
        }
      }
      return true;
    });
  },

  findOne(table, filter = {}) {
    const items = this.find(table, filter);
    return items.length > 0 ? items[0] : null;
  },

  findById(table, id) {
    return (db[table] || []).find(item => String(item.id) === String(id)) || null;
  },

  insert(table, item) {
    if (!db[table]) db[table] = [];
    const maxId = db[table].reduce((max, cur) => {
      const curId = typeof cur.id === 'number' ? cur.id : parseInt(cur.id, 10) || 0;
      return curId > max ? curId : max;
    }, 0);
    
    const newItem = {
      id: item.id !== undefined ? item.id : maxId + 1,
      ...item,
      created_at: item.created_at || new Date().toISOString()
    };
    db[table].push(newItem);
    saveDatabase();
    return newItem;
  },

  update(table, id, updates) {
    if (!db[table]) return null;
    const index = db[table].findIndex(item => String(item.id) === String(id));
    if (index === -1) return null;
    db[table][index] = {
      ...db[table][index],
      ...updates,
      updated_at: new Date().toISOString()
    };
    saveDatabase();
    return db[table][index];
  },

  updateWhere(table, filter, updates) {
    if (!db[table]) return [];
    const updated = [];
    db[table] = db[table].map(item => {
      let match = true;
      for (const key in filter) {
        if (item[key] !== filter[key]) {
          match = false;
          break;
        }
      }
      if (match) {
        const newItem = {
          ...item,
          ...updates,
          updated_at: new Date().toISOString()
        };
        updated.push(newItem);
        return newItem;
      }
      return item;
    });
    saveDatabase();
    return updated;
  },

  delete(table, id) {
    if (!db[table]) return false;
    const initialLen = db[table].length;
    db[table] = db[table].filter(item => String(item.id) !== String(id));
    if (db[table].length !== initialLen) {
      saveDatabase();
      return true;
    }
    return false;
  },

  resetToSeed(seed) {
    db = JSON.parse(JSON.stringify(seed));
    saveDatabase();
    return true;
  },

  raw() {
    return db;
  }
};
