import json
import os
import sys

# Add scratch dir to path
sys.path.insert(0, os.path.dirname(__file__))

from fitness_part1 import PART1_DATA
from fitness_part2 import PART2_DATA
from fitness_part3 import PART3_DATA

ALL_FITNESS_DATA = {}
ALL_FITNESS_DATA.update(PART1_DATA)
ALL_FITNESS_DATA.update(PART2_DATA)
ALL_FITNESS_DATA.update(PART3_DATA)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Loaded DB. Current counts:")
print(f"  courses: {len(db.get('courses', []))}")
print(f"  modules: {len(db.get('modules', []))}")
print(f"  topics: {len(db.get('topics', []))}")
print(f"  lessons: {len(db.get('lessons', []))}")
print(f"  pyqs: {len(db.get('previous_year_questions', []))}")
print(f"  practice: {len(db.get('practice_questions', []))}")
print(f"  quiz_questions: {len(db.get('quiz_questions', []))}")

# 1. Ensure Sources
sources = db.setdefault('sources', [])
existing_source_ids = {s['id'] for s in sources}

new_sources = [
    {
        "id": 8,
        "title": "ACSM Guidelines for Exercise Testing and Prescription (11th Edition)",
        "type": "Sports Science Authority",
        "publisher": "American College of Sports Medicine",
        "url": "https://www.acsm.org/education-resources/books/guidelines-exercise-testing-prescription",
        "publication_date": "2021-02-01",
        "accessed_date": "2026-09-20",
        "verified_status": "verified"
    },
    {
        "id": 9,
        "title": "WHO Guidelines on Physical Activity and Sedentary Behaviour",
        "type": "Global Health Guidelines",
        "publisher": "World Health Organization (WHO)",
        "url": "https://www.who.int/publications/i/item/9789240015128",
        "publication_date": "2020-11-25",
        "accessed_date": "2026-09-20",
        "verified_status": "verified"
    },
    {
        "id": 10,
        "title": "Indian Armed Forces & CAPF Physical Efficiency Test (PET) Manual",
        "type": "Official Defense Standards",
        "publisher": "Ministry of Defence & Ministry of Home Affairs, Govt of India",
        "url": "https://joinindianarmy.nic.in",
        "publication_date": "2024-01-10",
        "accessed_date": "2026-09-20",
        "verified_status": "verified"
    }
]

for ns in new_sources:
    if ns['id'] not in existing_source_ids:
        sources.append(ns)
        existing_source_ids.add(ns['id'])
        print(f"Added Source {ns['id']}: {ns['title']}")
    else:
        # Update existing
        for idx, s in enumerate(sources):
            if s['id'] == ns['id']:
                sources[idx] = ns
                break

# 2. Ensure Exams
exams = db.setdefault('exams', [])
existing_exam_ids = {e['id'] for e in exams}

new_exams = [
    {
        "id": 5,
        "name": "Indian Army Agniveer / NDA PET",
        "year": 2024,
        "authority": "Indian Armed Forces",
        "tier": "Physical Fitness Test (PFT)"
    },
    {
        "id": 6,
        "name": "SSC CPO CAPF PET",
        "year": 2024,
        "authority": "Staff Selection Commission & CAPFs",
        "tier": "Paper 1 & PET"
    }
]

for ne in new_exams:
    if ne['id'] not in existing_exam_ids:
        exams.append(ne)
        existing_exam_ids.add(ne['id'])
        print(f"Added Exam {ne['id']}: {ne['name']}")
    else:
        for idx, e in enumerate(exams):
            if e['id'] == ne['id']:
                exams[idx] = ne
                break

# 3. Clean any existing items for topics 69 to 77
target_topic_ids = set(range(69, 78))

db['lessons'] = [l for l in db.get('lessons', []) if l.get('topic_id') not in target_topic_ids]
db['previous_year_questions'] = [p for p in db.get('previous_year_questions', []) if p.get('topic_id') not in target_topic_ids]
db['practice_questions'] = [pr for pr in db.get('practice_questions', []) if pr.get('topic_id') not in target_topic_ids]
db['quiz_questions'] = [qq for qq in db.get('quiz_questions', []) if qq.get('topic_id') not in target_topic_ids]

# Find max IDs
max_lesson_id = max([l['id'] for l in db['lessons']], default=0)
max_pyq_id = max([p['id'] for p in db['previous_year_questions']], default=0)
max_practice_id = max([pr['id'] for pr in db['practice_questions']], default=0)
max_quiz_q_id = max([qq['id'] for qq in db['quiz_questions']], default=0)

topics_map = {t['id']: t for t in db.get('topics', [])}

for tid in sorted(target_topic_ids):
    data = ALL_FITNESS_DATA.get(tid)
    if not data:
        print(f"WARNING: No data for topic {tid}")
        continue

    topic = topics_map.get(tid, {})
    topic_title = topic.get('title', f"Topic {tid}")

    # A. Add Lesson
    max_lesson_id += 1
    lesson_obj = {
        "id": max_lesson_id,
        "topic_id": tid,
        "title": data["lesson"]["title"],
        "source_id": data["lesson"]["source_id"],
        "status": "published",
        "content_json": data["lesson"]["content"]
    }
    db['lessons'].append(lesson_obj)

    # B. Add PYQs
    for pyq in data["pyqs"]:
        max_pyq_id += 1
        pyq_obj = {
            "id": max_pyq_id,
            "topic_id": tid,
            "exam_id": pyq["exam_id"],
            "question": pyq["question"],
            "options_json": pyq.get("options_json", []),
            "correct_answer": pyq["correct_answer"],
            "explanation": pyq["explanation"],
            "source_id": pyq.get("source_id", 8),
            "status": "published",
            "subject": "Physical Fitness",
            "topic": topic_title,
            "question_type": pyq.get("question_type", "MCQ")
        }
        db['previous_year_questions'].append(pyq_obj)

    # C. Add Practice Questions
    for pq in data["practice"]:
        max_practice_id += 1
        pq_obj = {
            "id": max_practice_id,
            "topic_id": tid,
            "question": pq["question"],
            "options_json": pq.get("options_json", []),
            "correct_answer": pq["correct_answer"],
            "explanation": pq["explanation"],
            "difficulty": pq.get("difficulty", "Medium"),
            "subject": "Physical Fitness",
            "topic": topic_title,
            "question_type": pq.get("question_type", "MCQ")
        }
        db['practice_questions'].append(pq_obj)

    # D. Add Dedicated Quiz Questions
    for qq in data["quiz"]:
        max_quiz_q_id += 1
        qq_obj = {
            "id": max_quiz_q_id,
            "topic_id": tid,
            "question": qq["question"],
            "options_json": qq.get("options_json", []),
            "correct_answer": qq["correct_answer"],
            "explanation": qq["explanation"],
            "points": 1,
            "subject": "Physical Fitness",
            "topic": topic_title,
            "question_type": qq.get("question_type", "MCQ")
        }
        db['quiz_questions'].append(qq_obj)

    print(f"Topic {tid} ({topic_title}) populated successfully.")

# Save back to skillexa.json
with open(DATA_PATH, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("\nSuccessfully updated skillexa.json!")
print(f"New counts:")
print(f"  lessons: {len(db['lessons'])}")
print(f"  pyqs: {len(db['previous_year_questions'])}")
print(f"  practice: {len(db['practice_questions'])}")
print(f"  quiz_questions: {len(db['quiz_questions'])}")
