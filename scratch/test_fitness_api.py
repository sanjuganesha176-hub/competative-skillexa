import urllib.request
import json
import sys
import os

BASE_URL = "http://localhost:3001/api"

def get(endpoint):
    req = urllib.request.Request(f"{BASE_URL}{endpoint}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def post(endpoint, data):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(f"{BASE_URL}{endpoint}", data=body, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

print("\n=== 1. AUDITING COURSE: PHYSICAL FITNESS ===")
course_data = get("/courses/physical-fitness")
print(f"Course: {course_data.get('title')} (ID: {course_data.get('id')})")
print(f"Total Topics: {course_data.get('total_topics_count')}")
print(f"Modules: {len(course_data.get('modules', []))}")

topics = course_data.get('topics', [])
print(f"Retrieved {len(topics)} topics from course response.")

print("\n=== 2. AUDITING TOPICS 69 TO 77 (CONTENT & DEDICATED QUIZZES) ===")
audit_results = []
for t in topics:
    tid = t['id']
    topic_data = get(f"/topics/{tid}")
    
    lessons = topic_data.get('lessons', [])
    pyqs = topic_data.get('previous_year_questions', [])
    practice = topic_data.get('practice_questions', [])
    quiz = topic_data.get('quiz', {})
    quiz_qs = quiz.get('questions', [])
    
    mcq_count = sum(1 for q in quiz_qs if q.get('question_type') == 'MCQ')
    fitb_count = sum(1 for q in quiz_qs if q.get('question_type') == 'FILL_IN_THE_BLANK')
    
    status = topic_data.get('topic', {}).get('status')
    lesson = lessons[0] if lessons else {}
    content = lesson.get('content_json', {})
    
    res = {
        "id": tid,
        "title": t['title'],
        "status": status,
        "lesson_title": lesson.get('title'),
        "source": lesson.get('source', {}).get('title') if lesson.get('source') else None,
        "types_count": len(content.get('types', [])),
        "rules_count": len(content.get('rules', [])),
        "mistakes_count": len(content.get('common_mistakes', [])),
        "revision_points_count": len(content.get('quick_revision_points', [])),
        "pyqs_count": len(pyqs),
        "practice_count": len(practice),
        "quiz_total": len(quiz_qs),
        "mcqs": mcq_count,
        "fitbs": fitb_count,
        "next_topic": topic_data.get('next_topic', {}).get('title') if topic_data.get('next_topic') else None
    }
    audit_results.append(res)
    print(f"Topic {tid}: \"{t['title']}\" (Status: {status})")
    print(f"  Lesson: \"{res['lesson_title']}\"")
    print(f"  Source: {res['source']}")
    print(f"  Content: {res['types_count']} Types, {res['rules_count']} Rules, {res['mistakes_count']} Traps, {res['revision_points_count']} Revision Pts")
    print(f"  PYQs: {res['pyqs_count']} | Practice: {res['practice_count']} | Quiz: {res['quiz_total']} ({mcq_count} MCQ, {fitb_count} FITB)")
    print(f"  Next: {res['next_topic']}")

print("\n=== 3. TESTING FAILURE / LOCK INTEGRITY ===")
# Verify Topic 69 is initially unlocked and Topic 70 is locked
t69_init = get("/topics/69")
assert t69_init.get('topic', {}).get('status') == 'unlocked', "Topic 69 must be initially unlocked!"
t70_init = get("/topics/70")
assert t70_init.get('topic', {}).get('status') == 'locked', "Topic 70 must be initially locked!"

# Test that a failing score (<70%) on Topic 69 does NOT unlock Topic 70
q69_list = t69_init['quiz']['questions']
fail_answers = {q['id']: "Completely Wrong Answer" for q in q69_list}
fail_res = post("/quizzes/69/submit", {"answers": fail_answers, "timeSpentSeconds": 60})
print(f"Failing submission: percentage={fail_res.get('percentage')}%, passed={fail_res.get('passed')}")
assert fail_res.get('passed') is False, "Failed quiz must not pass!"
assert fail_res.get('unlocked_next_topic') is None, "Failed quiz must not unlock next topic!"

# Verify Topic 70 remains locked
t70_check = get("/topics/70")
assert t70_check.get('topic', {}).get('status') == 'locked', "Topic 70 should still be locked!"
print("Lock integrity verified: Topic 70 remains locked after failing quiz.")

print("\n=== 4. TESTING SUCCESSFUL QUIZ SUBMISSIONS & SEQUENTIAL UNLOCKING (69 -> 77) ===")

db_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(db_path, 'r', encoding='utf-8') as f:
    local_db = json.load(f)
quiz_q_answers = {q['id']: q['correct_answer'] for q in local_db.get('quiz_questions', [])}

for tid in range(69, 78):
    topic_data = get(f"/topics/{tid}")
    curr_status = topic_data.get('topic', {}).get('status')
    topic_title = topic_data.get('topic', {}).get('title')
    print(f"\n--- Testing Topic {tid}: \"{topic_title}\" ---")
    print(f"Status before quiz: {curr_status}")
    assert curr_status == 'unlocked', f"Topic {tid} must be unlocked!"

    quiz_qs = topic_data['quiz']['questions']
    assert len(quiz_qs) == 10, f"Topic {tid} must have 10 quiz questions!"

    # Create correct answers with whitespace and case variations on FITBs
    answers = {}
    for q in quiz_qs:
        ans = quiz_q_answers[q['id']]
        if q['question_type'] == 'FILL_IN_THE_BLANK':
            ans = f"  {ans.upper()}  " # Test whitespace trim & case insensitivity
        answers[q['id']] = ans

    res = post(f"/quizzes/{tid}/submit", {"answers": answers, "timeSpentSeconds": 150})
    print(f"Submission: Score {res.get('score')}/{res.get('total')} ({res.get('percentage')}%), Passed: {res.get('passed')}")
    assert res.get('passed') is True, f"Quiz for topic {tid} should pass with 100%!"
    assert res.get('percentage') == 100, f"Percentage should be 100%!"

    if tid < 77:
        unlocked = res.get('unlocked_next_topic')
        print(f"Unlocked: {unlocked.get('title')} (ID: {unlocked.get('id')})")
        assert unlocked is not None, f"Topic {tid} must unlock topic {tid+1}!"
        assert unlocked.get('id') == tid + 1, f"Unlocked topic ID must be {tid+1}!"

        # Verify via GET /topics/:id
        next_data = get(f"/topics/{tid+1}")
        assert next_data.get('topic', {}).get('status') == 'unlocked', f"Topic {tid+1} must be unlocked!"
    else:
        print("Final topic in Physical Fitness completed!")

print("\n=======================================================")
print("ALL TESTS PASSED! 100% VALIDATED PHYSICAL FITNESS SECTION")
print("=======================================================")
