import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

courses = db.get('courses', [])
english_courses = [c for c in courses if 'english' in c.get('slug', '').lower() or 'english' in c.get('title', '').lower()]
print('=== ENGLISH COURSES ===')
for c in english_courses:
    print(f"ID: {c.get('id')}, Title: {c.get('title')}, Slug: {c.get('slug')}")

english_course_ids = [c['id'] for c in english_courses]

modules = [m for m in db.get('modules', []) if m.get('course_id') in english_course_ids]
print(f"\n=== ENGLISH MODULES ({len(modules)}) ===")
for m in modules:
    print(f"Module ID: {m.get('id')}, Title: {m.get('title')}, Order: {m.get('order_index')}")

topics = [t for t in db.get('topics', []) if t.get('course_id') in english_course_ids]
print(f"\n=== ENGLISH TOPICS ({len(topics)}) ===")

lessons = db.get('lessons', [])
pyqs = db.get('previous_year_questions', [])
practice = db.get('practice_questions', [])
quiz_qs = db.get('quiz_questions', [])

print(f"{'ID':<4} | {'Title':<30} | {'Module':<25} | {'Lessons':<7} | {'PYQs':<5} | {'Practice':<8} | {'QuizQs':<7}")
print("-" * 95)

for t in sorted(topics, key=lambda x: x.get('order_index', 0)):
    tid = t.get('id')
    t_lessons = [l for l in lessons if l.get('topic_id') == tid]
    t_pyqs = [p for p in pyqs if p.get('topic_id') == tid]
    t_practice = [pr for pr in practice if pr.get('topic_id') == tid]
    t_quiz = [q for q in quiz_qs if q.get('topic_id') == tid]
    
    mod = next((m for m in modules if m['id'] == t.get('module_id')), {})
    mod_title = mod.get('title', 'Unknown')
    
    print(f"{tid:<4} | {t.get('title'):<30} | {mod_title[:24]:<25} | {len(t_lessons):<7} | {len(t_pyqs):<5} | {len(t_practice):<8} | {len(t_quiz):<7}")
