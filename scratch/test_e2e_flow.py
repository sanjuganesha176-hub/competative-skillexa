import urllib.request
import urllib.parse
import json
import sys

BASE_URL = "http://localhost:3001/api"

def make_request(path, method='GET', data=None):
    url = f"{BASE_URL}{path}"
    headers = {'Content-Type': 'application/json'}
    body = json.dumps(data).encode('utf-8') if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

print("=== STARTING E2E INTEGRATION TEST ===")

# 1. Reset user progress
print("\n--- 1. Reset Progress ---")
status, res = make_request("/user/progress/reset", method="POST")
print("Reset response:", res)

# Load server db answer key for testing
with open('server/data/skillexa.json', 'r', encoding='utf-8') as f:
    db_data = json.load(f)
quiz_answer_key = {str(q['id']): q['correct_answer'] for q in db_data.get('quiz_questions', [])}

# 2. Check Topic 1 (Noun) & its Quiz
print("\n--- 2. Fetch Topic 1 (Noun) ---")
status, t1 = make_request("/topics/1")
print(f"Topic 1: '{t1['topic']['title']}', status: {t1['topic']['status']}")
assert t1['topic']['status'] in ['unlocked', 'completed']
assert len(t1['quiz']['questions']) == 10
print(f"Topic 1 questions count: {len(t1['quiz']['questions'])}")

# Answer 8 out of 10 correctly for Topic 1
t1_answers = {}
for i, q in enumerate(t1['quiz']['questions']):
    qid = str(q['id'])
    if i < 8:
        t1_answers[qid] = quiz_answer_key.get(qid, "A")
    else:
        t1_answers[qid] = "Wrong answer"

status, submit1 = make_request("/quizzes/1/submit", method="POST", data={"answers": t1_answers, "timeSpentSeconds": 45})
print("Submit Topic 1 Quiz:", submit1['score'], "/", submit1['total'], f"({submit1['percentage']}%)", "Passed:", submit1['passed'])
assert submit1['passed'] == True
assert submit1['unlocked_next_topic'] is not None
print("Unlocked next topic:", submit1['unlocked_next_topic'])

# 3. Verify Topic 2 (Pronoun) is now unlocked and has real content
print("\n--- 3. Fetch Topic 2 (Pronoun) ---")
status, t2 = make_request("/topics/2")
print(f"Topic 2: '{t2['topic']['title']}', status: {t2['topic']['status']}")
assert t2['topic']['status'] in ['unlocked', 'completed']
assert "Noun" not in t2['lessons'][0]['title'], "Found Noun title in Pronoun lesson!"
assert len(t2['quiz']['questions']) == 10
print(f"Topic 2 questions count: {len(t2['quiz']['questions'])}")
print(f"Sample Q1 from Topic 2: {t2['quiz']['questions'][0]['question'][:60]}...")

# Submit Topic 2 with 9/10
t2_answers = {}
for i, q in enumerate(t2['quiz']['questions']):
    qid = str(q['id'])
    if i < 9:
        t2_answers[qid] = quiz_answer_key.get(qid, "A")
    else:
        t2_answers[qid] = "Wrong answer"

status, submit2 = make_request("/quizzes/2/submit", method="POST", data={"answers": t2_answers, "timeSpentSeconds": 50})
print("Submit Topic 2 Quiz:", submit2['score'], "/", submit2['total'], f"({submit2['percentage']}%)", "Passed:", submit2['passed'])
assert submit2['passed'] == True
assert submit2['unlocked_next_topic']['id'] == 3
print("Unlocked next topic:", submit2['unlocked_next_topic'])

# 4. Check Topic 3 (Verb)
print("\n--- 4. Fetch Topic 3 (Verb) ---")
status, t3 = make_request("/topics/3")
print(f"Topic 3: '{t3['topic']['title']}', status: {t3['topic']['status']}")
assert t3['topic']['status'] in ['unlocked', 'completed']
assert len(t3['quiz']['questions']) == 10

# 5. Test Overall Competitive Mock Quiz
print("\n--- 5. Test Overall Competitive Mock Quiz ---")
status, overall_quiz = make_request("/quizzes/overall?count=15")
print(f"Overall quiz returned {len(overall_quiz['questions'])} questions")
assert len(overall_quiz['questions']) >= 10

overall_answers = {}
for i, q in enumerate(overall_quiz['questions']):
    qid = str(q['id'])
    if i < 11:
        overall_answers[qid] = quiz_answer_key.get(qid, "A")
    else:
        overall_answers[qid] = "Incorrect"

status, overall_res = make_request("/quizzes/overall/submit", method="POST", data={
    "answers": overall_answers,
    "questions": overall_quiz['questions'],
    "timeSpentSeconds": 180
})
print("Overall Quiz Result:", overall_res['score'], "/", overall_res['total'], f"({overall_res['percentage']}%)", "Passed:", overall_res['passed'])
assert len(overall_res['results']) == len(overall_quiz['questions'])

# 6. Test Admin Current Affairs CRUD & Verification
print("\n--- 6. Test Admin Current Affairs CRUD ---")
new_ca = {
    "title": "E2E Test Mission: India Signs Major Renewable Accord",
    "category": "Economy & Energy",
    "date": "2026-09-23",
    "summary": "India has officially ratified a new clean energy and green hydrogen multilateral framework with global partners.",
    "important_facts": ["Green Hydrogen target of 5 MMT", "PIB Official Notification #8821"],
    "source_name": "Press Information Bureau (PIB)",
    "source_url": "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=882100",
    "status": "draft"
}
status, ca_create = make_request("/admin/current-affairs", method="POST", data=new_ca)
created_id = ca_create['item']['id']
print(f"Created Current Affair ID: {created_id}, status: {ca_create['item']['status']}")

# Check that draft does NOT show up in public student current affairs
status, public_ca = make_request("/current-affairs")
is_in_public = any(c['id'] == created_id for c in public_ca)
print("Is draft in public feed?", is_in_public)
assert is_in_public == False

# Update to published
status, ca_pub = make_request(f"/admin/current-affairs/{created_id}", method="PUT", data={"status": "published"})
print(f"Updated status to published: {ca_pub['item']['status']}")

# Check that published DOES show up in public student current affairs
status, public_ca2 = make_request("/current-affairs")
is_in_public2 = any(c['id'] == created_id for c in public_ca2)
print("Is published in public feed?", is_in_public2)
assert is_in_public2 == True

# Clean up / Delete
status, ca_del = make_request(f"/admin/current-affairs/{created_id}", method="DELETE")
print("Deleted test current affair:", ca_del)

print("\n=== ALL E2E INTEGRATION TESTS PASSED SUCCESSFULLY! ===")
