"""
Verify all General Science data across Part 1, Part 2, and Part 3 before injection
"""
import sys
import os

sys.path.append(os.path.abspath("scratch"))

from science_part1 import SCIENCE_PART1_DATA
from science_part2 import SCIENCE_PART2_DATA
from science_part3 import SCIENCE_PART3_DATA

all_science = {}
for k, v in SCIENCE_PART1_DATA.items():
    all_science[int(k)] = v
for k, v in SCIENCE_PART2_DATA.items():
    all_science[int(k)] = v
for k, v in SCIENCE_PART3_DATA.items():
    all_science[int(k)] = v

print(f"Total Science topics loaded: {len(all_science)}")
expected_tids = list(range(63, 69))
assert sorted(all_science.keys()) == expected_tids, f"Mismatch in topic IDs: {sorted(all_science.keys())} vs {expected_tids}"

total_lessons = 0
total_pyqs = 0
total_practice = 0
total_quiz = 0

for tid in expected_tids:
    data = all_science[tid]
    
    # 1. Check Lesson components
    assert "title" in data and len(data["title"]) > 5, f"Topic {tid}: title missing or short"
    assert data.get("source_id") == 7, f"Topic {tid}: source_id is not 7"
    
    content = data["content"]
    assert len(content.get("definition", "")) > 20, f"Topic {tid}: definition too short"
    assert len(content.get("overview", "")) > 20, f"Topic {tid}: overview too short"
    
    types = content.get("types", [])
    assert len(types) >= 5, f"Topic {tid}: types count {len(types)} < 5"
    for t in types:
        assert "name" in t and "desc" in t and "examples" in t, f"Topic {tid}: type malformed {t.keys()}"
        assert len(t["examples"]) >= 1, f"Topic {tid}: type examples empty"
        
    rules = content.get("rules", [])
    assert len(rules) >= 5, f"Topic {tid}: rules count {len(rules)} < 5"
    for r in rules:
        assert "rule_number" in r and "title" in r and "explanation" in r, f"Topic {tid}: rule malformed {r.keys()}"
        assert "correct" in r and "incorrect" in r, f"Topic {tid}: rule missing correct/incorrect"
        assert "words" in r and isinstance(r["words"], list), f"Topic {tid}: rule missing words list"
        
    mistakes = content.get("common_mistakes", [])
    assert len(mistakes) >= 4, f"Topic {tid}: mistakes count {len(mistakes)} < 4"
    for m in mistakes:
        assert "mistake" in m and "correction" in m and "rationale" in m, f"Topic {tid}: mistake malformed {m.keys()}"
        
    revision = content.get("quick_revision_points", [])
    assert len(revision) >= 10, f"Topic {tid}: revision points count {len(revision)} < 10"
    
    total_lessons += 1
    
    # 2. Check PYQs
    pyqs = data.get("previous_year_questions", [])
    assert len(pyqs) == 3, f"Topic {tid}: PYQ count is {len(pyqs)} != 3"
    for i, p in enumerate(pyqs, 1):
        assert p["topic_id"] == tid
        assert p["id"] == tid * 100 + i
        assert len(p["options_json"]) == 4
        assert p["correct_answer"] in p["options_json"], f"Topic {tid} PYQ {p['id']}: correct_answer not in options_json"
        assert len(p["explanation"]) > 15
        total_pyqs += 1
        
    # 3. Check Practice Questions
    prac = data.get("practice_questions", [])
    assert len(prac) == 10, f"Topic {tid}: practice count is {len(prac)} != 10"
    for i, pq in enumerate(prac, 1):
        assert pq["topic_id"] == tid
        assert pq["id"] == tid * 100 + i
        assert len(pq["options_json"]) == 4
        assert pq["correct_answer"] in pq["options_json"], f"Topic {tid} practice {pq['id']}: correct_answer '{pq['correct_answer']}' not in options_json"
        assert len(pq["explanation"]) > 15
        total_practice += 1
        
    # 4. Check Quiz Questions (USER EXPLICIT REQUIREMENT: MINIMUM 20 EACH TOPIC)
    quiz = data.get("quiz_questions", [])
    assert len(quiz) >= 20, f"Topic {tid}: quiz count is {len(quiz)} < 20 (MUST BE >= 20)"
    assert len(quiz) == 20, f"Topic {tid}: quiz count is {len(quiz)} != 20"
    for i, q in enumerate(quiz, 1):
        assert q["topic_id"] == tid
        assert q["id"] == tid * 100 + i
        assert len(q["options_json"]) == 4
        assert q["correct_answer"] in q["options_json"], f"Topic {tid} quiz {q['id']}: correct_answer '{q['correct_answer']}' not in options_json"
        assert len(q["explanation"]) > 15
        total_quiz += 1

    print(f"Topic {tid} passed all verification checks! ({data['title'][:55]}...)")

print("\n--- ALL 6 GENERAL SCIENCE TOPICS FULLY VALIDATED ---")
print(f"Total verified lessons: {total_lessons} / 6")
print(f"Total verified PYQs: {total_pyqs} / 18")
print(f"Total verified Practice Questions: {total_practice} / 60")
print(f"Total verified Quiz Questions: {total_quiz} / 120 (Exactly 20 per topic!)")
