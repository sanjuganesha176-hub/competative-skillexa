import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Total courses: {len(db.get('courses', []))}")
for c in db.get('courses', []):
    c_topics = [t for t in db.get('topics', []) if t.get('course_id') == c['id']]
    print(f"Course {c['id']}: {c['title']} (slug: {c['slug']}) -> {len(c_topics)} topics (IDs: {[t['id'] for t in c_topics[:3]]}...{[t['id'] for t in c_topics[-3:]]})")
