# scratch/inspect_ga.py
import json

data = json.load(open('server/data/skillexa.json', encoding='utf-8'))
for c in data.get('courses', []):
    if 'aware' in c.get('title', '').lower() or 'general' in c.get('title', '').lower() or 'ga' in c.get('slug', '').lower():
        print('Course:', c)
        modules = [m for m in data.get('modules', []) if m.get('course_id') == c['id']]
        for m in modules:
            topics = [t for t in data.get('topics', []) if t.get('module_id') == m['id']]
            print(f"\nModule {m['id']} - {m['title']} ({len(topics)} topics):")
            for t in sorted(topics, key=lambda x: x.get('order_index', 0)):
                tid = t['id']
                lessons = [l for l in data.get('lessons', []) if l.get('topic_id') == tid]
                pyqs = [p for p in data.get('previous_year_questions', []) if p.get('topic_id') == tid]
                practice = [pr for pr in data.get('practice_questions', []) if pr.get('topic_id') == tid]
                quiz = [q for q in data.get('quiz_questions', []) if q.get('topic_id') == tid]
                print(f"  Topic {tid:02d} (Order {t.get('order_index')}): {t.get('title'):<24} | Lessons: {len(lessons)} | PYQs: {len(pyqs)} | Practice: {len(practice)} | QuizQs: {len(quiz)}")
