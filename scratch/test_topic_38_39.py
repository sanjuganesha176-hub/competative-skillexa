import urllib.request
import json

for tid in [38, 39]:
    try:
        resp = urllib.request.urlopen(f'http://localhost:3001/api/topics/{tid}')
        data = json.loads(resp.read().decode('utf-8'))
        print(f"\n=== TOPIC {tid}: {data['topic']['title']} ===")
        print("Lessons count:", len(data.get('lessons', [])))
        print("PYQs count:", len(data.get('previous_year_questions', [])))
        print("Practice count:", len(data.get('practice_questions', [])))
        print("Quiz questions count:", len(data.get('quiz', {}).get('questions', [])))
    except Exception as e:
        print(f"Error topic {tid}:", e)
