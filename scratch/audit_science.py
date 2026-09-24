import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

courses = [c for c in db.get('courses', []) if 'science' in c.get('title', '').lower() or 'science' in c.get('slug', '').lower()]
print('Courses:', [(c['id'], c['title'], c['slug']) for c in courses])

course_ids = [c['id'] for c in courses]
modules = [m for m in db.get('modules', []) if m.get('course_id') in course_ids]
print('Modules:', [(m['id'], m['course_id'], m['title']) for m in modules])

mod_ids = [m['id'] for m in modules]
topics = [t for t in db.get('topics', []) if t.get('module_id') in mod_ids]
print('Topics count:', len(topics))
for t in topics:
    tid = t['id']
    lessons = [l for l in db.get('lessons', []) if l.get('topic_id') == tid]
    pyqs = [p for p in db.get('previous_year_questions', []) if p.get('topic_id') == tid]
    practice = [pr for pr in db.get('practice_questions', []) if pr.get('topic_id') == tid]
    quizzes = [q for q in db.get('quizzes', []) if q.get('topic_id') == tid]
    quiz_questions = []
    if quizzes:
        qid = quizzes[0]['id']
        quiz_questions = [qq for qq in db.get('quiz_questions', []) if qq.get('quiz_id') == qid]
    else:
        quiz_questions = [qq for qq in db.get('quiz_questions', []) if qq.get('topic_id') == tid]
    print(f'Topic {tid}: "{t["title"]}" (order {t.get("order")}) -> Lessons: {len(lessons)}, PYQs: {len(pyqs)}, Practice: {len(practice)}, Quizzes: {len(quizzes)}, QuizQuestions: {len(quiz_questions)}')
