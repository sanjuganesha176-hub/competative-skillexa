import json
import os
import subprocess

db_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Keep progress for non-course-6 topics, reset 69-77
db['user_topic_progress'] = [p for p in db.get('user_topic_progress', []) if p.get('topic_id') not in range(69, 78)]
db['user_topic_progress'].append({
    "id": 5,
    "user_id": 1,
    "topic_id": 69,
    "status": "unlocked",
    "best_score": 0,
    "attempts_count": 0,
    "unlocked_at": "2026-09-22T16:46:33.295Z",
    "completed_at": None,
    "created_at": "2026-09-22T16:46:33.295Z"
})

with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Sync with seedData
subprocess.run(["python", os.path.join(os.path.dirname(__file__), "sync_seed.py")], check=True)
print("Physical Fitness progress reset: Topic 69 is UNLOCKED, Topics 70-77 are LOCKED.")
