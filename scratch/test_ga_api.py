import urllib.request
import json
import time

time.sleep(1)

# 1. Course endpoint
resp = urllib.request.urlopen('http://localhost:3001/api/courses/general-awareness')
data = json.loads(resp.read().decode('utf-8'))
print('Course:', data.get('title'), 'Slug:', data.get('slug'))
print('Modules:', len(data.get('modules', [])))
print('Topics count:', len(data.get('topics', [])))

# 2. Test each topic endpoint from 52 to 62
all_passed = True
for tid in range(52, 63):
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
        if c.get('definition') and len(c.get('types', [])) >= 4 and len(c.get('rules', [])) >= 4 and len(c.get('common_mistakes', [])) >= 4 and len(c.get('quick_revision_points', [])) >= 6:
            has_content = True
            
    status = "OK" if (len(lessons) == 1 and has_content and len(pyqs) == 3 and len(prac) == 10 and len(quiz) == 10) else "FAILED"
    if status == "FAILED":
        all_passed = False
        
    print(f"Topic {tid:<2} ({t.get('title', 'Unknown')[:25]:<25}): Lessons={len(lessons)}, PYQs={len(pyqs)}, Practice={len(prac)}, Quiz={len(quiz)} -> {status}")

if all_passed:
    print("\nSUCCESS: All 11 General Awareness topics are fully populated and returning valid data via the API!")
else:
    print("\nFAILURE: One or more topics failed API validation!")
