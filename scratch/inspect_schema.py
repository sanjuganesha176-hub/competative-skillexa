import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print("=== KEYS IN DB ===")
print(list(db.keys()))

print("\n=== SAMPLE LESSON (Topic 1) ===")
l1 = next((l for l in db.get('lessons', []) if l.get('topic_id') == 1), {})
print(json.dumps(l1, indent=2)[:500])

print("\n=== SAMPLE PYQ (Topic 1) ===")
pyq1 = next((p for p in db.get('previous_year_questions', []) if p.get('topic_id') == 1), {})
print(json.dumps(pyq1, indent=2))

print("\n=== SAMPLE PRACTICE QUESTION (Topic 1) ===")
pr1 = next((p for p in db.get('practice_questions', []) if p.get('topic_id') == 1), {})
print(json.dumps(pr1, indent=2))

print("\n=== SAMPLE QUIZ QUESTION (Topic 1) ===")
q1 = next((q for q in db.get('quiz_questions', []) if q.get('topic_id') == 1), {})
print(json.dumps(q1, indent=2))
