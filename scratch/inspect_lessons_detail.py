import json
import os

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

for tid in range(1, 23):
    l = [les for les in db['lessons'] if les['topic_id'] == tid]
    t = [top for top in db['topics'] if top['id'] == tid][0]
    if l:
        c = l[0].get('content_json', {})
        t_count = len(c.get('types', []))
        rules = c.get('rules', [])
        r_type = type(rules[0]).__name__ if rules else 'empty'
        print(f"Topic {tid:2d} ({t['title']:<25}): types={t_count}, rules={len(rules)} ({r_type}), mistakes={len(c.get('common_mistakes', []))}, rev={len(c.get('quick_revision_points', []))}")
    else:
        print(f"Topic {tid:2d} ({t['title']:<25}): NO LESSON")
