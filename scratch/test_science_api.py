import urllib.request
import json
import time

time.sleep(1)

# 1. Course endpoint
resp = urllib.request.urlopen('http://localhost:3001/api/courses/general-science')
data = json.loads(resp.read().decode('utf-8'))
print('Course:', data.get('title'), 'Slug:', data.get('slug'))
print('Modules:', len(data.get('modules', [])))
print('Topics count:', len(data.get('topics', [])))

# 2. Test each topic endpoint from 63 to 68
all_passed = True
for tid in range(63, 69):
    url = f'http://localhost:3001/api/topics/{tid}'
    req = urllib.request.urlopen(url)
    tdata = json.loads(req.read().decode('utf-8'))
    
    t = tdata.get('topic', {})
    lessons = tdata.get('lessons', [])
    pyqs = tdata.get('previous_year_questions', [])
    prac = tdata.get('practice_questions', [])
    quiz = tdata.get('quiz', {}).get('questions', [])
    
    # Check lesson content
    has_content = False
    if len(lessons) > 0:
        c = lessons[0].get('content_json', {})
        if (c.get('definition') and 
            len(c.get('types', [])) >= 5 and 
            len(c.get('rules', [])) >= 5 and 
            len(c.get('common_mistakes', [])) >= 4 and 
            len(c.get('quick_revision_points', [])) >= 10):
            has_content = True
            
    is_ok = (len(lessons) == 1 and has_content and len(pyqs) == 3 and len(prac) == 10 and len(quiz) == 20)
    status = "OK" if is_ok else "FAILED"
    if not is_ok:
        all_passed = False
        
    print(f"Topic {tid:<2} ({t.get('title', 'Unknown')[:22]:<22}): Lessons={len(lessons)}, PYQs={len(pyqs)}, Practice={len(prac)}, Quiz={len(quiz)} (>=20) -> {status}")

if all_passed:
    print("\nSUCCESS: All 6 General Science topics have large content and exactly 20 quiz questions via the API!")
else:
    print("\nFAILURE: One or more topics failed API validation!")
