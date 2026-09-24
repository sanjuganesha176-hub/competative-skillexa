# scratch/verify_all_math_data.py
import sys
sys.path.append('.')

from scratch.math_part1 import MATH_PART1_DATA
from scratch.math_part2 import MATH_PART2_DATA
from scratch.math_part3 import MATH_PART3_DATA

all_math = {**MATH_PART1_DATA, **MATH_PART2_DATA, **MATH_PART3_DATA}

print(f"Total topics: {len(all_math)}")
for tid in sorted([int(k) for k in all_math.keys()]):
    data = all_math[str(tid)]
    c = data["content"]
    title = data["title"]
    types_count = len(c.get("types", []))
    rules_count = len(c.get("rules", []))
    mistakes_count = len(c.get("common_mistakes", []))
    rev_count = len(c.get("quick_revision_points", []))
    pyq_count = len(data.get("previous_year_questions", []))
    prac_count = len(data.get("practice_questions", []))
    quiz_count = len(data.get("quiz_questions", []))
    print(f"Topic {tid:02d}: {title[:35]:<35} | Types:{types_count} Rules:{rules_count} Mistakes:{mistakes_count} Rev:{rev_count} | PYQs:{pyq_count} Prac:{prac_count} Quiz:{quiz_count}")
