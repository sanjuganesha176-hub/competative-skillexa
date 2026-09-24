import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

print("=== ALL COURSES ===")
for c in db.get('courses', []):
    print(f"Course ID {c['id']}: {c['title']} | slug: {c.get('slug')} | category: {c.get('category')}")

fitness_courses = [c for c in db.get('courses', []) if any(k in c.get('title', '').lower() or k in c.get('slug', '').lower() for k in ['fit', 'physical', 'sport', 'health'])]
print("\n=== MATCHING COURSES ===")
for c in fitness_courses:
    print(c)

course_ids = [c['id'] for c in fitness_courses]
modules = [m for m in db.get('modules', []) if m.get('course_id') in course_ids]
print("\n=== MODULES FOR MATCHING COURSES ===")
for m in modules:
    print(m)

mod_ids = [m['id'] for m in modules]
topics = [t for t in db.get('topics', []) if t.get('module_id') in mod_ids or t.get('course_id') in course_ids]
print(f"\n=== TOPICS ({len(topics)}) ===")
for t in topics:
    tid = t['id']
    lessons = [l for l in db.get('lessons', []) if l.get('topic_id') == tid]
    pyqs = [p for p in db.get('previous_year_questions', []) if p.get('topic_id') == tid]
    practice = [pr for pr in db.get('practice_questions', []) if pr.get('topic_id') == tid]
    quizzes = [q for q in db.get('quizzes', []) if q.get('topic_id') == tid]
    quiz_questions = [qq for qq in db.get('quiz_questions', []) if qq.get('topic_id') == tid]
    print(f"Topic {tid}: \"{t['title']}\" (order: {t.get('order_index')}, unlocked: {t.get('is_default_unlocked')}) -> Lessons: {len(lessons)}, PYQs: {len(pyqs)}, Practice: {len(practice)}, QuizQs: {len(quiz_questions)}")
