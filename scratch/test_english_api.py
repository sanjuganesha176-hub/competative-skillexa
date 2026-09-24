import urllib.request
import json

topics_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

print(f"{'ID':<3} | {'Topic Title':<25} | {'Lesson Title':<45} | {'Types':<5} | {'Rules':<5} | {'Traps':<5} | {'Rev':<5} | {'PYQ':<4} | {'Prac':<4} | {'Quiz':<4}")
print("-" * 125)

for tid in topics_to_check:
    url = f"http://localhost:3001/api/topics/{tid}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            topic = data.get('topic', {})
            lessons = data.get('lessons', [])
            pqs = data.get('practice_questions', [])
            pyqs = data.get('previous_year_questions', [])
            quiz = data.get('quiz', {})
            
            lesson = lessons[0] if lessons else {}
            content = lesson.get('content_json', {})
            types = content.get('types', [])
            rules = content.get('rules', [])
            mistakes = content.get('common_mistakes', [])
            revision = content.get('quick_revision_points', [])
            
            print(f"{tid:<3} | {topic.get('title', ''):<25} | {lesson.get('title', '')[:45]:<45} | {len(types):<5} | {len(rules):<5} | {len(mistakes):<5} | {len(revision):<5} | {len(pyqs):<4} | {len(pqs):<4} | {len(quiz.get('questions', [])):<4}")
    except Exception as e:
        print(f"{tid:<3} | ERROR: {e}")
