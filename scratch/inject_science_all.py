# scratch/inject_science_all.py
import json
import os
import sys

sys.path.append('.')

from scratch.science_part1 import SCIENCE_PART1_DATA
from scratch.science_part2 import SCIENCE_PART2_DATA
from scratch.science_part3 import SCIENCE_PART3_DATA

all_science = {}
for k, v in SCIENCE_PART1_DATA.items():
    all_science[int(k)] = v
for k, v in SCIENCE_PART2_DATA.items():
    all_science[int(k)] = v
for k, v in SCIENCE_PART3_DATA.items():
    all_science[int(k)] = v

data_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(data_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Build topic title map from existing topics
topic_title_map = {}
for t in db.get('topics', []):
    topic_title_map[t['id']] = t.get('title', f"Topic {t['id']}")

# 1. Update/Add Lessons
non_sci_lessons = [l for l in db.get('lessons', []) if not (63 <= l.get('topic_id', 0) <= 68)]
new_sci_lessons = []
for tid in sorted(all_science.keys()):
    m = all_science[tid]
    new_sci_lessons.append({
        "id": 100 + tid,
        "topic_id": tid,
        "title": m["title"],
        "source_id": m.get("source_id", 7),
        "status": "published",
        "order_index": 1,
        "content_json": m["content"]
    })

db['lessons'] = non_sci_lessons + new_sci_lessons
print(f"Lessons updated: {len(non_sci_lessons)} non-Science + {len(new_sci_lessons)} Science = {len(db['lessons'])} total.")

# 2. Update/Add Previous Year Questions
non_sci_pyqs = [p for p in db.get('previous_year_questions', []) if not (63 <= p.get('topic_id', 0) <= 68)]
new_sci_pyqs = []
for tid in sorted(all_science.keys()):
    m = all_science[tid]
    pyqs = m.get("previous_year_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pyqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_sci_pyqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "exam_id": p.get("exam_id", 1),
            "question": p["question"],
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "source_id": p.get("source_id", 7),
            "status": "published",
            "subject": "General Science",
            "topic": topic_name,
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ"
        })

db['previous_year_questions'] = non_sci_pyqs + new_sci_pyqs
print(f"PYQs updated: {len(non_sci_pyqs)} non-Science + {len(new_sci_pyqs)} Science = {len(db['previous_year_questions'])} total.")

# 3. Update/Add Practice Questions
non_sci_pqs = [p for p in db.get('practice_questions', []) if not (63 <= p.get('topic_id', 0) <= 68)]
new_sci_pqs = []
for tid in sorted(all_science.keys()):
    m = all_science[tid]
    pqs = m.get("practice_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, p in enumerate(pqs):
        is_fitb = p.get('type') == 'fitb' or not p.get('options_json') or len(p.get('options_json')) == 0
        new_sci_pqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": p["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": p.get("options_json", []),
            "correct_answer": str(p["correct_answer"]),
            "explanation": p["explanation"],
            "points": p.get("points", 1),
            "subject": "General Science",
            "topic": topic_name
        })

db['practice_questions'] = non_sci_pqs + new_sci_pqs
print(f"Practice Questions updated: {len(non_sci_pqs)} non-Science + {len(new_sci_pqs)} Science = {len(db['practice_questions'])} total.")

# 4. Update/Add Quiz Questions (20 questions each!)
non_sci_qqs = [q for q in db.get('quiz_questions', []) if not (63 <= q.get('topic_id', 0) <= 68)]
new_sci_qqs = []
for tid in sorted(all_science.keys()):
    m = all_science[tid]
    qqs = m.get("quiz_questions", [])
    topic_name = topic_title_map.get(tid, f"Topic {tid}")
    for idx, q in enumerate(qqs):
        is_fitb = q.get('type') == 'fitb' or not q.get('options_json') or len(q.get('options_json')) == 0
        new_sci_qqs.append({
            "id": tid * 100 + (idx + 1),
            "topic_id": tid,
            "question": q["question"],
            "question_type": "FILL_IN_THE_BLANK" if is_fitb else "MCQ",
            "options_json": q.get("options_json", []),
            "correct_answer": str(q["correct_answer"]),
            "explanation": q["explanation"],
            "points": q.get("points", 1),
            "subject": "General Science",
            "topic": topic_name
        })

db['quiz_questions'] = non_sci_qqs + new_sci_qqs
print(f"Quiz Questions updated: {len(non_sci_qqs)} non-Science + {len(new_sci_qqs)} Science = {len(db['quiz_questions'])} total.")

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
