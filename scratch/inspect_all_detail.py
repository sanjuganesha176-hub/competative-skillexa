import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

topics = db.get('topics', [])
lessons = db.get('lessons', [])
pyqs = db.get('previous_year_questions', [])
practice = db.get('practice_questions', [])
quiz_qs = db.get('quiz_questions', [])

print("=== CHECKING ALL TOPICS 1 TO 77 ===")
empty_topics = []
populated_topics = []

for t in topics:
    tid = t['id']
    t_lessons = [l for l in lessons if l.get('topic_id') == tid and l.get('content_json')]
    t_pyqs = [p for p in pyqs if p.get('topic_id') == tid]
    t_practice = [pr for pr in practice if pr.get('topic_id') == tid]
    t_quiz = [q for q in quiz_qs if q.get('topic_id') == tid]
    
    has_content = bool(t_lessons)
    
    if not has_content or len(t_practice) < 10 or len(t_quiz) < 10:
        empty_topics.append({
            "id": tid,
            "course_id": t.get('course_id'),
            "title": t.get('title'),
            "lessons": len(t_lessons),
            "pyqs": len(t_pyqs),
            "practice": len(t_practice),
            "quiz": len(t_quiz)
        })
    else:
        populated_topics.append({
            "id": tid,
            "course_id": t.get('course_id'),
            "title": t.get('title')
        })

print(f"Populated Topics: {len(populated_topics)}")
print(f"Incomplete / Missing Topics: {len(empty_topics)}")

print("\n--- INCOMPLETE / MISSING TOPICS LIST ---")
for et in empty_topics:
    print(f"Course {et['course_id']} | Topic {et['id']:2d}: {et['title']:<30} | Lessons: {et['lessons']} | PYQs: {et['pyqs']} | Practice: {et['practice']} | Quiz: {et['quiz']}")
