import requests
import os
import sys

BASE_URL = 'http://localhost:3001'

def run_tests():
    print("==================================================")
    print("STARTING COMPLETE END-TO-END TEST FOR NOTES FEATURE")
    print("==================================================")

    # 1. Test student access to admin API (MUST BE 403 FORBIDDEN)
    print("\n[TEST 1] Testing role security on Admin Notes API...")
    res_no_role = requests.get(f"{BASE_URL}/api/admin/notes")
    print(f"Request without admin headers -> Status code: {res_no_role.status_code}")
    assert res_no_role.status_code == 403, f"Expected 403, got {res_no_role.status_code}"

    res_student_role = requests.get(f"{BASE_URL}/api/admin/notes", headers={'x-user-role': 'student'})
    print(f"Request with x-user-role: student -> Status code: {res_student_role.status_code}")
    assert res_student_role.status_code == 403, f"Expected 403, got {res_student_role.status_code}"
    print("[PASS] Admin endpoint is strictly secured with 403 Forbidden.")

    # 2. Test admin access to Admin Notes API
    print("\n[TEST 2] Testing admin access to Admin Notes API...")
    res_admin = requests.get(f"{BASE_URL}/api/admin/notes", headers={'x-user-role': 'admin'})
    print(f"Request with x-user-role: admin -> Status code: {res_admin.status_code}")
    assert res_admin.status_code == 200, f"Expected 200, got {res_admin.status_code}"
    admin_data = res_admin.json()
    assert 'counts' in admin_data, "Response missing 'counts'"
    assert 'total' in admin_data, "Response missing 'total'"
    print(f"[PASS] Admin successfully retrieved notes list. Current total notes: {admin_data['total']}")

    # 3. Test Student Public Notes API
    print("\n[TEST 3] Testing public Notes API for students...")
    res_public = requests.get(f"{BASE_URL}/api/notes")
    assert res_public.status_code == 200, f"Expected 200, got {res_public.status_code}"
    public_data = res_public.json()
    print(f"Public published notes count: {public_data.get('total', 0)}")
    print("[PASS] Public API responds cleanly.")

    # 4. Test Real PDF Upload via Admin API
    print("\n[TEST 4] Testing real PDF upload to Notes Management...")
    test_pdf_path = os.path.join(os.path.dirname(__file__), 'temp_test_note.pdf')
    with open(test_pdf_path, 'wb') as f:
        f.write(b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>>>endobj\nxref\n0 4\n0000000000 65535 f\n0000000009 00000 n\n0000000052 00000 n\n0000000101 00000 n\ntrailer<</Size 4/Root 1 0 R>>\nstartxref\n178\n%%EOF\n")

    try:
        with open(test_pdf_path, 'rb') as f:
            files = {'pdf': ('English_Grammar_Mastery.pdf', f, 'application/pdf')}
            data = {
                'title': 'English Grammar Mastery - Parts of Speech',
                'subject_name': 'English',
                'topic_name': 'Parts of Speech',
                'subtopic_name': 'Nouns & Pronouns',
                'description': 'Comprehensive master notes covering all 8 parts of speech with solved exam examples.',
                'source': 'Faculty Curriculum Reference',
                'page_count': '18',
                'status': 'DRAFT'
            }
            res_upload = requests.post(
                f"{BASE_URL}/api/admin/notes",
                headers={'x-user-role': 'admin'},
                files=files,
                data=data
            )
        
        print(f"Upload response status: {res_upload.status_code}")
        assert res_upload.status_code == 201, f"Expected 201, got {res_upload.status_code}: {res_upload.text}"
        uploaded_note = res_upload.json()['data']
        note_id = uploaded_note['id']
        file_url = uploaded_note['file_url']
        print(f"[PASS] Uploaded note ID: {note_id}, file_url: {file_url}, status: {uploaded_note['status']}")

        # 5. Verify PDF file was saved on disk and can be fetched via HTTP static route
        print("\n[TEST 5] Testing uploaded static PDF file delivery...")
        res_file = requests.get(f"{BASE_URL}{file_url}")
        print(f"Static file fetch status: {res_file.status_code}, content-type: {res_file.headers.get('content-type')}")
        assert res_file.status_code == 200, f"Expected 200, got {res_file.status_code}"
        assert b'%PDF' in res_file.content[:10], "Expected PDF binary header"
        print("[PASS] Actual PDF file delivered accurately.")

        # 6. Verify DRAFT note is NOT visible in student feed (Requirement 8)
        print("\n[TEST 6] Testing student feed exclusion for DRAFT note...")
        res_feed = requests.get(f"{BASE_URL}/api/notes")
        published_ids = [n['id'] for n in res_feed.json()['data']]
        assert note_id not in published_ids, f"DRAFT note {note_id} should not appear in student feed!"
        print("[PASS] DRAFT note is NOT visible in public student feed.")

        # 7. Test status workflow transition: DRAFT -> PENDING_REVIEW -> VERIFIED -> PUBLISHED
        print("\n[TEST 7] Testing workflow transition to VERIFIED...")
        res_verify = requests.patch(
            f"{BASE_URL}/api/admin/notes/{note_id}/status",
            headers={'x-user-role': 'admin', 'Content-Type': 'application/json'},
            json={'status': 'VERIFIED'}
        )
        assert res_verify.status_code == 200
        # Verify still not in student feed
        res_feed2 = requests.get(f"{BASE_URL}/api/notes")
        published_ids2 = [n['id'] for n in res_feed2.json()['data']]
        assert note_id not in published_ids2, "VERIFIED (un-published) note should not appear in student feed!"
        print("[PASS] VERIFIED status alone does not expose note until PUBLISHED.")

        print("\n[TEST 8] Testing publishing note (VERIFIED -> PUBLISHED)...")
        res_publish = requests.patch(
            f"{BASE_URL}/api/admin/notes/{note_id}/status",
            headers={'x-user-role': 'admin', 'Content-Type': 'application/json'},
            json={'status': 'PUBLISHED'}
        )
        assert res_publish.status_code == 200
        res_feed3 = requests.get(f"{BASE_URL}/api/notes")
        published_notes = res_feed3.json()['data']
        found = any(n['id'] == note_id for n in published_notes)
        assert found, f"PUBLISHED note {note_id} must appear in student feed!"
        print("[PASS] Note is now live in Student's Notes feed.")

        # 8. Test Search and Filter
        print("\n[TEST 9] Testing search and filter in public Notes feed...")
        res_search = requests.get(f"{BASE_URL}/api/notes?search=Speech")
        assert any(n['id'] == note_id for n in res_search.json()['data']), "Search failed to match topic"

        res_subj = requests.get(f"{BASE_URL}/api/notes?subject=English")
        assert any(n['id'] == note_id for n in res_subj.json()['data']), "Subject filter failed"

        res_subj_mismatch = requests.get(f"{BASE_URL}/api/notes?subject=Mathematics")
        assert not any(n['id'] == note_id for n in res_subj_mismatch.json()['data']), "Subject filter should not match Mathematics"
        print("[PASS] Search and filter work as expected.")

        # 9. Clean up test note and file so no test data remains
        print("\n[TEST 10] Testing Admin note deletion & file cleanup...")
        res_del = requests.delete(
            f"{BASE_URL}/api/admin/notes/{note_id}",
            headers={'x-user-role': 'admin'}
        )
        assert res_del.status_code == 200
        # Verify file is deleted from server disk
        res_file_after = requests.get(f"{BASE_URL}{file_url}")
        assert res_file_after.status_code == 404, "File should have been removed from server"
        print("[PASS] Note and physical PDF file cleaned up cleanly.")

    finally:
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)

    print("\n==================================================")
    print("ALL 10 TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
