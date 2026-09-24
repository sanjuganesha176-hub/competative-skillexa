# scratch/inject_math_all.py
import json
import os
import sys

sys.path.append('.')

from scratch.math_part1 import MATH_PART1_DATA
from scratch.math_part2 import MATH_PART2_DATA
from scratch.math_part3 import MATH_PART3_DATA

all_math = {**MATH_PART1_DATA, **MATH_PART2_DATA, **MATH_PART3_DATA}

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Build topic title map from existing topics or math data
topic_title_map = {}
for t in db.get('topics', []):
    topic_title_map[t['id']] = t.get('title', f"Topic {t['id']}")

# 1. Update/Add Lessons
non_math_lessons = [l for l in db.get('lessons', []) if not (23 <= l.get('topic_id', 0) <= 37)]
new_math_lessons = []
for tid in sorted([int(k) for k in all_math.keys()]):
    m = all_math[str(tid)]
    new_math_lessons.append({
        "id": 100 + tid,
        "topic_id": tid,
        "title": m["title"],
        "source_id": m.get("source_id", 7),
        "status": "published",
        "order_index": 1,
        "content_json": m["content"]
    })

db['lessons'] = non_math_lessons + new_math_lessons
print(f"Lessons updated: {len(non_math_lessons)} non-math + {len(new_math_lessons)} math = {len(db['lessons'])} total.")

# 2. Update/Add Previous Year Questions
non_math_pyqs = [p for p in db.get('previous_year_questions', []) if not (23 <= p.get('topic_id', 0) <= 37)]
new_math_pyqs = []
for tid in sorted([int(k) for k in all_math.keys()]):
    m = all_math[str(tid)]
    pyqs = m.get("previous_year_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pyqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_math_pyqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "exam_id": p.get("exam_id", 1),
            "question": p["question"],
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "source_id": p.get("source_id", 7),
            "status": "published",
            "subject": "Mathematics",
            "topic": topic_name,
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ"
        })

db['previous_year_questions'] = non_math_pyqs + new_math_pyqs
print(f"PYQs updated: {len(non_math_pyqs)} non-math + {len(new_math_pyqs)} math = {len(db['previous_year_questions'])} total.")

# 3. Update/Add Practice Questions
non_math_pqs = [p for p in db.get('practice_questions', []) if not (23 <= p.get('topic_id', 0) <= 37)]
new_math_pqs = []
for tid in sorted([int(k) for k in all_math.keys()]):
    m = all_math[str(tid)]
    pqs = m.get("practice_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_math_pqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": p["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "points": p.get("points", 1),
            "subject": "Mathematics",
            "topic": topic_name
        })

db['practice_questions'] = non_math_pqs + new_math_pqs
print(f"Practice Questions updated: {len(non_math_pqs)} non-math + {len(new_math_pqs)} math = {len(db['practice_questions'])} total.")

# 4. Update/Add Quiz Questions
non_math_qqs = [q for q in db.get('quiz_questions', []) if not (23 <= q.get('topic_id', 0) <= 37)]
new_math_qqs = []
for tid in sorted([int(k) for k in all_math.keys()]):
    m = all_math[str(tid)]
    qqs = m.get("quiz_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, q in enumerate(qqs):
        is_fitb = q.get('type') == 'fitb' or not q.get('options_json') or len(q.get('options_json')) == 0
        new_math_qqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": q["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": q.get("options_json", []),
            "correct_answer": str(q["correct_answer"]),
            "explanation": q["explanation"],
            "points": q.get("points", 1),
            "subject": "Mathematics",
            "topic": topic_name
        })

db['quiz_questions'] = non_math_qqs + new_math_qqs
print(f"Quiz Questions updated: {len(non_math_qqs)} non-math + {len(new_math_qqs)} math = {len(db['quiz_questions'])} total.")

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
