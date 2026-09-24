# scratch/test_reasoning_api.py
import urllib.request
import json

for tid in range(38, 52):
    url = f"http://localhost:3001/api/topics/{tid}"
    try:
        req = urllib.request.urlopen(url)
        res = json.loads(req.read().decode('utf-8'))
        topic = res.get('topic', {})
        lessons = res.get('lessons', [])
        pyqs = res.get('previous_year_questions', [])
        practice = res.get('practice_questions', [])
        quiz = res.get('quiz', {})
        title = topic.get('title', 'Unknown')
        print(f"Topic {tid:02d} ({title:<26}): Lessons={len(lessons)}, PYQs={len(pyqs)}, Practice={len(practice)}, QuizQs={quiz.get('total_questions')}")
    except Exception as e:
        print(f"Error fetching topic {tid}: {e}")
