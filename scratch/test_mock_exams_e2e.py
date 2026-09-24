import urllib.request
import urllib.error
import json
import sys

BASE_URL = "http://localhost:3001"
ADMIN_HEADERS = {
    "Content-Type": "application/json",
    "x-user-role": "admin"
}

def make_req(endpoint, method="GET", data=None, headers=None):
    url = f"{BASE_URL}{endpoint}"
    req_headers = headers or {}
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req_headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, data=body, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            resp_body = resp.read().decode("utf-8")
            return status, json.loads(resp_body) if resp_body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        try:
            parsed = json.loads(err_body)
        except Exception:
            parsed = {"error": err_body}
        return e.code, parsed

def run_tests():
    print("==================================================")
    print("SKILLEXA E2E TEST: MOCK EXAMS & MIN 50 QUESTIONS")
    print("==================================================")

    # 1. Test public mock exams listing
    status, res = make_req("/api/mock-exams")
    assert status == 200, f"Expected 200, got {status}"
    exams = res.get("data", [])
    print(f"[OK] GET /api/mock-exams: Found {len(exams)} published exams")
    for ex in exams:
        q_count = len(ex.get("question_ids", []))
        print(f"   - Exam #{ex['id']}: '{ex['title']}' | Questions: {q_count}")
        assert q_count >= 50, f"Violation: Exam #{ex['id']} has {q_count} questions (< 50)!"

    # 2. Test single mock exam hydration
    exam_id = exams[0]["id"]
    status, res = make_req(f"/api/mock-exams/{exam_id}")
    assert status == 200, f"Expected 200, got {status}"
    exam_data = res.get("data", {})
    qs = exam_data.get("questions", [])
    print(f"[OK] GET /api/mock-exams/{exam_id}: Hydrated {len(qs)} questions (min 50 verified)")
    assert len(qs) >= 50, f"Expected at least 50 hydrated questions, got {len(qs)}"

    # 3. Test ADMIN validation: Rejection when < 50 questions
    print("\nTesting Strict Admin Constraint: Reject mock creation with < 50 questions...")
    invalid_payload = {
        "title": "Invalid Short Mock Exam (10 Qs)",
        "category": "SSC",
        "target_exam": "Test",
        "duration_minutes": 30,
        "passing_percentage": 70,
        "negative_marking": 0.25,
        "auto_generate": False,
        "question_ids": [1, 2, 3, 4, 5] # Only 5 questions!
    }
    status, res = make_req("/api/admin/mock-exams", method="POST", data=invalid_payload, headers=ADMIN_HEADERS)
    print(f"   Status returned: {status} (Expected 400)")
    print(f"   Response message: {res.get('error')}")
    assert status == 400, f"Expected 400 Bad Request, got {status}"
    assert "minimum of 50 questions" in res.get("error", "").lower(), "Expected error message enforcing minimum 50 questions"
    print("[OK] Successfully rejected mock exam with < 50 questions (HTTP 400)")

    # 4. Test ADMIN creation with Auto-Assembly of 50 questions
    print("\nTesting Admin Creation with Auto-Assembly of 50+ questions...")
    valid_payload = {
        "title": "Admin E2E Verification 50-Q Full Mock Exam",
        "category": "Banking",
        "target_exam": "IBPS PO 2026",
        "description": "Automated verification exam testing 50-question assembly engine",
        "duration_minutes": 60,
        "passing_percentage": 70,
        "negative_marking": 0.25,
        "instructions": "Standard test instructions",
        "auto_generate": True,
        "subject_distribution": {
            "english": 15,
            "math": 15,
            "reasoning": 10,
            "general_awareness": 10
        },
        "status": "published"
    }
    status, res = make_req("/api/admin/mock-exams", method="POST", data=valid_payload, headers=ADMIN_HEADERS)
    assert status == 201, f"Expected 201 Created, got {status}: {res}"
    created_exam = res.get("data", {})
    created_id = created_exam.get("id")
    q_len = len(created_exam.get("question_ids", []))
    print(f"[OK] POST /api/admin/mock-exams: Created Exam #{created_id} with {q_len} questions (Min 50 met!)")
    assert q_len >= 50, f"Created exam only has {q_len} questions, expected >= 50"

    # 5. Test Student Submission on the new 50-question mock exam
    print(f"\nTesting Student Submission on Exam #{created_id}...")
    # Answer 40 questions correctly, 5 incorrectly, 5 unattempted
    # Hydrate questions to get IDs
    status, res = make_req(f"/api/mock-exams/{created_id}")
    exam_questions = res["data"]["questions"]
    answers = {}
    for i, q in enumerate(exam_questions):
        opts = q.get("options") or []
        if i < 40:
            answers[str(q["id"])] = opts[0] if len(opts) > 0 else "SampleAnswer"
        elif i < 45:
            answers[str(q["id"])] = "WRONG_ANSWER_CHOICE"

    submit_payload = {
        "answers": answers,
        "timeSpentSeconds": 1800
    }
    status, res = make_req(f"/api/mock-exams/{created_id}/submit", method="POST", data=submit_payload)
    assert status == 200, f"Expected 200, got {status}: {res}"
    print(f"[OK] POST /api/mock-exams/{created_id}/submit:")
    print(f"   Score: {res.get('score')} / {res.get('max_marks')}")
    print(f"   Accuracy: {res.get('percentage')}%")
    print(f"   Correct: {res.get('correct_count')} | Incorrect: {res.get('incorrect_count')} | Unattempted: {res.get('unattempted_count')}")
    print(f"   Breakdown items: {len(res.get('breakdown', []))}")
    assert len(res.get("breakdown", [])) >= 50, "Expected at least 50 breakdown items"

    # 6. Test Admin Delete
    print(f"\nCleaning up test exam #{created_id}...")
    status, res = make_req(f"/api/admin/mock-exams/{created_id}", method="DELETE", headers=ADMIN_HEADERS)
    assert status == 200, f"Expected 200, got {status}: {res}"
    print(f"[OK] DELETE /api/admin/mock-exams/{created_id}: Cleaned up successfully")

    print("\n==================================================")
    print("ALL MOCK EXAM & 50-QUESTION TESTS PASSED (100% SUCCESS)!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
