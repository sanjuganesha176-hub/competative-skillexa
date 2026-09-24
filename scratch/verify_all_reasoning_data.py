# scratch/verify_all_reasoning_data.py
import sys
sys.path.append('.')

from scratch.reasoning_part1 import REASONING_PART1_DATA
from scratch.reasoning_part2 import REASONING_PART2_DATA
from scratch.reasoning_part3 import REASONING_PART3_DATA

all_reasoning = {**REASONING_PART1_DATA, **REASONING_PART2_DATA, **REASONING_PART3_DATA}

print(f"Total topics: {len(all_reasoning)}")
for tid in sorted([int(k) for k in all_reasoning.keys()]):
    data = all_reasoning[str(tid)]
    c = data["content"]
    title = data["title"]
    types_count = len(c.get("types", []))
    rules_count = len(c.get("rules", []))
    mistakes_count = len(c.get("common_mistakes", []))
    rev_count = len(c.get("quick_revision_points", []))
    pyq_count = len(data.get("previous_year_questions", []))
    prac_count = len(data.get("practice_questions", []))
    quiz_count = len(data.get("quiz_questions", []))
    print(f"Topic {tid:02d}: {title[:32]:<32} | Types:{types_count} Rules:{rules_count} Mistakes:{mistakes_count} Rev:{rev_count} | PYQs:{pyq_count} Prac:{prac_count} Quiz:{quiz_count}")
