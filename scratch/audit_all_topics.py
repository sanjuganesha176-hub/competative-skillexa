import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

courses = db.get('courses', [])
modules = db.get('modules', [])
topics = db.get('topics', [])
lessons = db.get('lessons', [])
pyqs = db.get('previous_year_questions', [])
practice = db.get('practice_questions', [])
quiz_qs = db.get('quiz_questions', [])

print(f"Total Courses: {len(courses)}")
print(f"Total Modules: {len(modules)}")
print(f"Total Topics: {len(topics)}")
print(f"Total Lessons: {len(lessons)}")
print(f"Total PYQs: {len(pyqs)}")
print(f"Total Practice Questions: {len(practice)}")
print(f"Total Quiz Questions: {len(quiz_qs)}")

print("\n=== AUDIT PER COURSE ===")
for c in courses:
    c_topics = [t for t in topics if t.get('course_id') == c['id']]
    t_with_lessons = 0
    t_with_pyqs = 0
    t_with_practice = 0
    t_with_quiz = 0
    
    missing_lesson_topics = []
    
    for t in c_topics:
        tid = t['id']
        t_l = [l for l in lessons if l.get('topic_id') == tid and l.get('content_json')]
        t_p = [p for p in pyqs if p.get('topic_id') == tid]
        t_pr = [pr for pr in practice if pr.get('topic_id') == tid]
        t_q = [q for q in quiz_qs if q.get('topic_id') == tid]
        
        if t_l: t_with_lessons += 1
        else: missing_lesson_topics.append((tid, t['title']))
        if t_p: t_with_pyqs += 1
        if t_pr: t_with_practice += 1
        if t_q: t_with_quiz += 1
        
    print(f"Course {c['id']}: \"{c['title']}\" ({c.get('slug')}) -> Total Topics: {len(c_topics)} | Lessons: {t_with_lessons}/{len(c_topics)} | PYQs: {t_with_pyqs}/{len(c_topics)} | Practice: {t_with_practice}/{len(c_topics)} | Quiz: {t_with_quiz}/{len(c_topics)}")
    if missing_lesson_topics:
        print(f"   MISSING LESSONS in {len(missing_lesson_topics)} topics:")
        for mt in missing_lesson_topics:
            print(f"     - Topic {mt[0]}: {mt[1]}")
