import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

courses = db.get('courses', [])
ga_courses = [c for c in courses if 'general' in c.get('slug', '').lower() or 'awareness' in c.get('slug', '').lower() or 'gk' in c.get('slug', '').lower()]
print("=== GENERAL AWARENESS COURSES ===")
for c in ga_courses:
    print(f"ID: {c.get('id')}, Title: {c.get('title')}, Slug: {c.get('slug')}, Category: {c.get('category')}")

c_ids = [c['id'] for c in ga_courses]
modules = [m for m in db.get('modules', []) if m.get('course_id') in c_ids]
print(f"\n=== GENERAL AWARENESS MODULES ({len(modules)}) ===")
for m in modules:
    print(f"Module ID: {m.get('id')}, Title: {m.get('title')}, Order: {m.get('order_index')}, Course ID: {m.get('course_id')}")

topics = [t for t in db.get('topics', []) if t.get('course_id') in c_ids]
print(f"\n=== GENERAL AWARENESS TOPICS ({len(topics)}) ===")

lessons = db.get('lessons', [])
pyqs = db.get('previous_year_questions', [])
practice = db.get('practice_questions', [])
quiz_qs = db.get('quiz_questions', [])

print(f"{'ID':<4} | {'Title':<32} | {'Module':<25} | {'Lessons':<7} | {'PYQs':<5} | {'Practice':<8} | {'QuizQs':<7}")
print("-" * 100)

for t in sorted(topics, key=lambda x: (x.get('module_id', 0), x.get('order_index', 0))):
    tid = t.get('id')
    t_lessons = [l for l in lessons if l.get('topic_id') == tid]
    t_pyqs = [p for p in pyqs if p.get('topic_id') == tid]
    t_practice = [pr for pr in practice if pr.get('topic_id') == tid]
    t_quiz = [q for q in quiz_qs if q.get('topic_id') == tid]
    
    mod = next((m for m in modules if m['id'] == t.get('module_id')), {})
    mod_title = mod.get('title', 'Unknown')
    
    print(f"{tid:<4} | {t.get('title'):<32} | {mod_title[:24]:<25} | {len(t_lessons):<7} | {len(t_pyqs):<5} | {len(t_practice):<8} | {len(t_quiz):<7}")
