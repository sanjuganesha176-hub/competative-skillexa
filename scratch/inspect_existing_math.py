import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

for tid in [23, 24, 28]:
    l = [x for x in db.get('lessons', []) if x.get('topic_id') == tid]
    p = [x for x in db.get('previous_year_questions', []) if x.get('topic_id') == tid]
    pr = [x for x in db.get('practice_questions', []) if x.get('topic_id') == tid]
    q = [x for x in db.get('quiz_questions', []) if x.get('topic_id') == tid]
    print(f"Topic {tid}:")
    print(f"  Lessons: {len(l)}, PYQs: {len(p)}, Practice: {len(pr)}, Quiz: {len(q)}")
    if l:
        print(f"  Lesson title: {l[0].get('title')}")
        cj = l[0].get('content_json', {})
        print(f"  Lesson keys: {list(cj.keys())}")
    if q:
        for item in q:
            print(f"    Q: {item.get('question')[:50]}... Ans: {item.get('correct_answer')}")
