# scratch/inject_ga_all.py
import json
import os
import sys

sys.path.append('.')

from scratch.ga_part1 import GA_PART1_DATA
from scratch.ga_part2 import GA_PART2_DATA
from scratch.ga_part3 import GA_PART3_DATA

all_ga = {}
for k, v in GA_PART1_DATA.items():
    all_ga[int(k)] = v
for k, v in GA_PART2_DATA.items():
    all_ga[int(k)] = v
for k, v in GA_PART3_DATA.items():
    all_ga[int(k)] = v

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Build topic title map from existing topics
topic_title_map = {}
for t in db.get('topics', []):
    topic_title_map[t['id']] = t.get('title', f"Topic {t['id']}")

# 1. Update/Add Lessons
non_ga_lessons = [l for l in db.get('lessons', []) if not (52 <= l.get('topic_id', 0) <= 62)]
new_ga_lessons = []
for tid in sorted(all_ga.keys()):
    m = all_ga[tid]
    new_ga_lessons.append({
        "id": 100 + tid,
        "topic_id": tid,
        "title": m["title"],
        "source_id": m.get("source_id", 7),
        "status": "published",
        "order_index": 1,
        "content_json": m["content"]
    })

db['lessons'] = non_ga_lessons + new_ga_lessons
print(f"Lessons updated: {len(non_ga_lessons)} non-GA + {len(new_ga_lessons)} GA = {len(db['lessons'])} total.")

# 2. Update/Add Previous Year Questions
non_ga_pyqs = [p for p in db.get('previous_year_questions', []) if not (52 <= p.get('topic_id', 0) <= 62)]
new_ga_pyqs = []
for tid in sorted(all_ga.keys()):
    m = all_ga[tid]
    pyqs = m.get("previous_year_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pyqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_ga_pyqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "exam_id": p.get("exam_id", 1),
            "question": p["question"],
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "source_id": p.get("source_id", 7),
            "status": "published",
            "subject": "General Awareness",
            "topic": topic_name,
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ"
        })

db['previous_year_questions'] = non_ga_pyqs + new_ga_pyqs
print(f"PYQs updated: {len(non_ga_pyqs)} non-GA + {len(new_ga_pyqs)} GA = {len(db['previous_year_questions'])} total.")

# 3. Update/Add Practice Questions
non_ga_pqs = [p for p in db.get('practice_questions', []) if not (52 <= p.get('topic_id', 0) <= 62)]
new_ga_pqs = []
for tid in sorted(all_ga.keys()):
    m = all_ga[tid]
    pqs = m.get("practice_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_ga_pqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": p["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "points": p.get("points", 1),
            "subject": "General Awareness",
            "topic": topic_name
        })

db['practice_questions'] = non_ga_pqs + new_ga_pqs
print(f"Practice Questions updated: {len(non_ga_pqs)} non-GA + {len(new_ga_pqs)} GA = {len(db['practice_questions'])} total.")

# 4. Update/Add Quiz Questions
non_ga_qqs = [q for q in db.get('quiz_questions', []) if not (52 <= q.get('topic_id', 0) <= 62)]
new_ga_qqs = []
for tid in sorted(all_ga.keys()):
    m = all_ga[tid]
    qqs = m.get("quiz_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, q in enumerate(qqs):
        is_fitb = q.get('type') == 'fitb' or not q.get('options_json') or len(q.get('options_json')) == 0
        new_ga_qqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": q["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": q.get("options_json", []),
            "correct_answer": str(q["correct_answer"]),
            "explanation": q["explanation"],
            "points": q.get("points", 1),
            "subject": "General Awareness",
            "topic": topic_name
        })

db['quiz_questions'] = non_ga_qqs + new_ga_qqs
print(f"Quiz Questions updated: {len(non_ga_qqs)} non-GA + {len(new_ga_qqs)} GA = {len(db['quiz_questions'])} total.")

# 5. Save skillexa.json
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {data_path}.")

# 6. Synchronize seedData.js
seed_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'seedData.js')
json_str = json.dumps(db, indent=2, ensure_ascii=False)
with open(seed_path, 'w', encoding='utf-8') as f:
    f.write(f"export const seedData = {json_str};\n")

print(f"Successfully synchronized {seed_path} ({len(json_str)} characters).")
