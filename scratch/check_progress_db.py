import json

with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

progs = [p for p in data.get('user_topic_progress', []) if p.get('user_id') == 1 and p.get('topic_id') in [1, 2, '1', '2']]
print("user_topic_progress for 1 and 2:")
print(json.dumps(progs, indent=2))
