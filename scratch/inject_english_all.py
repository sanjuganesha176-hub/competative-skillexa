# inject_english_all.py
# Injects rich educational content and 10 practice questions for Topics 3 to 22 into skillexa.json and syncs seedData.js

import json
import os
import subprocess

# Import all groups
import english_group_a
import english_group_b
import english_group_c
import english_group_d
import english_group_e
import english_group_f

ALL_GROUPS = {}

# Merge Groups A-D
for grp, mod in [('A', english_group_a), ('B', english_group_b), ('C', english_group_c), ('D', english_group_d)]:
    data = getattr(mod, f'GROUP_{grp}_DATA')
    for tid_raw, val in data.items():
        tid = int(tid_raw)
        ALL_GROUPS[tid] = {
            'title': val['title'],
            'source_id': val.get('source_id', 1),
            'content': val['content'],
            'practice': val.get('practice', [])
        }

# Merge Groups E-F
for grp, mod in [('E', english_group_e), ('F', english_group_f)]:
    data = getattr(mod, f'GROUP_{grp}_DATA')
    for tid_raw, val in data.items():
        tid = int(tid_raw)
        pqs = val.get('practice_questions', [])
        ALL_GROUPS[tid] = {
            'title': val['title'],
            'source_id': val.get('source_id', 1),
            'content': val['content'],
            'practice': pqs
        }

print(f"Total topics prepared for injection: {len(ALL_GROUPS)} (Topics: {sorted(ALL_GROUPS.keys())})")

# Load skillexa.json
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json'))
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# Build a lookup for topic names
topics_lookup = {t['id']: t['title'] for t in db.get('topics', [])}

# Process each topic 3 to 22
for tid, tdata in ALL_GROUPS.items():
    topic_name = topics_lookup.get(tid, f"Topic {tid}")
    
    # 1. Update Lesson
    existing_lessons = [l for l in db['lessons'] if l.get('topic_id') == tid]
    if existing_lessons:
        target_lesson = existing_lessons[0]
        target_lesson['title'] = tdata['title']
        target_lesson['source_id'] = tdata['source_id']
        target_lesson['status'] = 'published'
        target_lesson['content_json'] = tdata['content']
    else:
        max_lid = max([l.get('id', 0) for l in db['lessons']], default=0)
        db['lessons'].append({
            'id': max_lid + 1,
            'topic_id': tid,
            'title': tdata['title'],
            'source_id': tdata['source_id'],
            'status': 'published',
            'created_at': '2026-09-23T12:00:00.000Z',
            'content_json': tdata['content']
        })
    
    # 2. Update Practice Questions
    raw_practice = tdata['practice']
    normalized_pqs = []
    
    for idx, q in enumerate(raw_practice, start=1):
        pq_id = tid * 100 + idx
        q_text = q.get('question') or q.get('question_text') or ''
        raw_options = q.get('options_json') if 'options_json' in q else q.get('options', [])
        q_type_raw = str(q.get('question_type', 'MCQ')).upper()
        
        is_fitb = (q_type_raw in ['FITB', 'FILL_IN_THE_BLANK']) or (not raw_options) or ('____' in q_text)
        options = [] if is_fitb else list(raw_options)
        
        diff = q.get('difficulty', 'Medium')
        if isinstance(diff, str):
            diff = diff.capitalize()
        else:
            diff = 'Medium'
            
        normalized_pqs.append({
            'id': pq_id,
            'topic_id': tid,
            'question': q_text,
            'options_json': options,
            'correct_answer': q['correct_answer'],
            'explanation': q['explanation'],
            'difficulty': diff,
            'subject': 'English',
            'topic': topic_name,
            'question_type': 'FILL_IN_THE_BLANK' if is_fitb else 'MCQ'
        })
    
    # Remove existing practice questions for this topic and add new 10
    db['practice_questions'] = [pq for pq in db['practice_questions'] if pq.get('topic_id') != tid]
    db['practice_questions'].extend(normalized_pqs)
    print(f"Topic {tid:02d} ({topic_name}): Updated lesson and injected {len(normalized_pqs)} practice questions.")

# Save skillexa.json
with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Saved updated skillexa.json successfully.")

# Run sync_seed.py
sync_script = os.path.join(os.path.dirname(__file__), "sync_seed.py")
subprocess.run(["python", sync_script], check=True)
print("Synced seedData.js successfully!")
