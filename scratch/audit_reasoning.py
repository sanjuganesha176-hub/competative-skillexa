# scratch/audit_reasoning.py
import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

courses = db.get('courses', [])
rc = [c for c in courses if c['id'] == 3][0]
print(f"=== {rc.get('title').upper()} (Course ID: {rc['id']}) ===")

modules = [m for m in db.get('modules', []) if m.get('course_id') == 3]
topics = [t for t in db.get('topics', []) if t.get('course_id') == 3]

lessons = db.get('lessons', [])
pyqs = db.get('previous_year_questions', [])
practice = db.get('practice_questions', [])
quiz_qs = db.get('quiz_questions', [])

print(f"{'ID':<4} | {'Title':<28} | {'Lessons':<7} | {'PYQs':<5} | {'Practice':<8} | {'QuizQs':<7}")
print("-" * 75)

for t in sorted(topics, key=lambda x: x.get('order_index', 0)):
    tid = t.get('id')
    t_lessons = [l for l in lessons if l.get('topic_id') == tid]
    t_pyqs = [p for p in pyqs if p.get('topic_id') == tid]
    t_practice = [pr for pr in practice if pr.get('topic_id') == tid]
    t_quiz = [q for q in quiz_qs if q.get('topic_id') == tid]
    print(f"{tid:<4} | {t.get('title'):<28} | {len(t_lessons):<7} | {len(t_pyqs):<5} | {len(t_practice):<8} | {len(t_quiz):<7}")

print("-" * 75)
print(f"Total Topics: {len(topics)}")
print(f"Total Lessons: {sum(len([l for l in lessons if l.get('topic_id') == t['id']]) for t in topics)}")
print(f"Total PYQs: {sum(len([p for p in pyqs if p.get('topic_id') == t['id']]) for t in topics)}")
print(f"Total Practice: {sum(len([pr for pr in practice if pr.get('topic_id') == t['id']]) for t in topics)}")
print(f"Total QuizQs: {sum(len([q for q in quiz_qs if q.get('topic_id') == t['id']]) for t in topics)}")
