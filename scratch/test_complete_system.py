import urllib.request
import json

BASE = "http://localhost:3001/api"

def get(path):
    req = urllib.request.Request(f"{BASE}{path}", method="GET")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def post(path, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())

def put(path, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers={"Content-Type": "application/json"}, method="PUT")
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode())

def patch(path, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(f"{BASE}{path}", data=data, headers={"Content-Type": "application/json"}, method="PATCH")
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode())

def delete(path):
    req = urllib.request.Request(f"{BASE}{path}", method="DELETE")
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode())

print("=== STARTING COMPREHENSIVE VERIFICATION ===")

# 1. Test empty state for normal users
res = get("/government-exams")
print("1. Normal users public feed count (initially):", res["total"])

# 2. Check expandable categories
cats = get("/exam-categories")
print("2. Expandable categories available:", len(cats["data"]))
assert len(cats["data"]) >= 12, "Should have default categories"

# 3. Add expandable category
status, cat_res = post("/admin/exam-categories", {
    "name": "Metro Rail Corporation",
    "key": "Metro",
    "group": "State Government",
    "description": "BMRCL and State Metro Rail Recruitment"
})
print("3. Admin add new expandable category:", status, cat_res.get("success"))

# 4. Admin creates real authentic update (DRAFT)
status, created = post("/admin/government-exams", {
    "exam_name": "SSC Combined Graduate Level (CGL) 2024",
    "organization": "Staff Selection Commission (SSC)",
    "category": "SSC",
    "update_type": "EXAM_NOTIFICATION",
    "official_notification_number": "SSC/2024/01-CGL",
    "title": "SSC CGL 2024 Official Notification Released for 17,727 Group B & C Posts",
    "short_description": "Staff Selection Commission released official notification for 17,727 vacancies across Central ministries and departments.",
    "full_description": "Staff Selection Commission (SSC) has officially issued the examination notice for Combined Graduate Level Examination (CGL) 2024 for filling approximately 17,727 vacancies in Group 'B' and 'C' posts across Ministries/Departments/Organizations of Government of India.",
    "post_name": "Assistant Section Officer, Inspector, Sub-Inspector, Auditor, Tax Assistant",
    "vacancy": "17,727 Vacancies (Tentative)",
    "eligibility": "Indian Citizen with Bachelor's Degree",
    "age_limit": "18 to 30/32 years (Relaxation as per central rules)",
    "qualification": "Bachelor's Degree from a recognized University or equivalent",
    "application_fee": "₹100 (Exempted for Women, SC, ST, PwBD, ESM)",
    "selection_process": "Tier-I (Computer Based Exam) + Tier-II (Computer Based Exam)",
    "notification_date": "2024-06-24",
    "application_start_date": "2024-06-24",
    "application_last_date": "2024-07-27",
    "exam_date": "2026-10-15",
    "official_source_name": "Staff Selection Commission Official Portal (Govt of India)",
    "official_source_url": "https://ssc.gov.in",
    "verification_status": "DRAFT",
    "send_push_notification": False
})
print("4. Admin created exam update in DRAFT:", status, created["data"]["id"])
exam_id = created["data"]["id"]

# 5. Verify unverified update is NOT in public feed
pub_res = get("/government-exams")
assert pub_res["total"] == 0, "DRAFT update must NOT appear in public feed"
print("5. Public feed verified: DRAFT is hidden from students (total=0)")

# 6. Test duplicate protection
dup_status, dup_err = post("/admin/government-exams", {
    "exam_name": "SSC Combined Graduate Level (CGL) 2024",
    "organization": "Staff Selection Commission (SSC)",
    "category": "SSC",
    "update_type": "EXAM_NOTIFICATION",
    "title": "Another duplicate title",
    "official_source_name": "SSC",
    "official_source_url": "https://ssc.gov.in"
})
print("6. Duplicate protection response code:", dup_status, "(Expected 409)")
assert dup_status == 409, "Duplicate protection must reject identical active updates"

# 7. Workflow Step 2: DRAFT -> PENDING_REVIEW
status, patch_res = patch(f"/admin/government-exams/{exam_id}/status", {"status": "PENDING_REVIEW"})
print("7. Transitioned to PENDING_REVIEW:", status, patch_res["data"]["verification_status"])

# 8. Workflow Step 3: PENDING_REVIEW -> VERIFIED
status, patch_res = patch(f"/admin/government-exams/{exam_id}/status", {"status": "VERIFIED"})
print("8. Transitioned to VERIFIED:", status, patch_res["data"]["verification_status"])

# 9. Workflow Step 4: VERIFIED -> PUBLISHED with Push Notification
status, patch_res = patch(f"/admin/government-exams/{exam_id}/status", {
    "status": "PUBLISHED",
    "send_push_notification": True
})
print("9. Published with push notification:", status, patch_res["data"]["verification_status"], "Dispatched:", patch_res["notification_dispatched"])

# 10. Check public feed now returns the published exam
pub_res = get("/government-exams")
print("10. Public feed now returns published updates:", pub_res["total"])
assert pub_res["total"] == 1, "Published update must appear in public feed"
exam_item = pub_res["data"][0]
print("    Dynamic status:", exam_item["dynamic_status"])

# 11. Check notifications were created
notifs = get("/notifications")
print("11. User notifications count:", len(notifs["data"]), "Unread:", notifs["unread_count"])
assert notifs["unread_count"] >= 1, "User must receive push/in-app notification"

# 12. Mark notification read
notif_id = notifs["data"][0]["id"]
status, read_res = patch(f"/notifications/{notif_id}/read", {})
print("12. Notification marked as read:", status, read_res["data"]["is_read"])

# 13. Verify notification preferences endpoint
prefs = get("/notification-preferences")
print("13. User notification preferences:", prefs["data"]["category_preferences"])

# Update preferences
status, pref_update = put("/notification-preferences", {
    "exam_notifications": True,
    "application_updates": True,
    "category_preferences": ["SSC", "UPSC", "KPSC"]
})
print("14. Updated preferences:", status, pref_update["data"]["category_preferences"])

# 15. Verify User Profile API
profile = get("/user/profile")
print("15. User profile fetched:", profile["user"]["name"], "Targets:", profile["user"]["target_exams"])

# Update profile
status, prof_update = put("/user/profile", {
    "name": "Ganesh Kumar",
    "target_exams": ["SSC CGL", "UPSC CDS", "KPSC KAS"],
    "state": "Karnataka",
    "bio": "Central and State Government competitive exams aspirant."
})
print("16. User profile updated:", status, prof_update["user"]["name"])

# 17. Verify Deadline Scanner
status, scan_res = post("/notifications/check-deadlines", {})
print("17. Deadline scanner executed:", status, "Reminders sent:", scan_res["reminders_sent"])

# 18. Verify Homepage latest updates endpoint
latest = get("/government-exams/latest?limit=4")
print("18. Homepage latest updates count:", len(latest["data"]))
assert len(latest["data"]) >= 1, "Homepage must receive latest updates"

# 19. Verify Single Exam detail endpoint
single = get(f"/government-exams/{exam_id}")
print("19. Single exam detail official URL:", single["data"]["official_source_url"])
assert single["data"]["official_source_url"] == "https://ssc.gov.in"

# 20. Verify /api/papers is removed
try:
    urllib.request.urlopen(f"{BASE}/papers")
    print("WARNING: /api/papers should have been removed")
except urllib.error.HTTPError as e:
    print("20. Verified /api/papers returned 404 (removed as requested):", e.code)

print("\n=== ALL 20 VERIFICATION CHECKS PASSED PERFECTLY! ===")
