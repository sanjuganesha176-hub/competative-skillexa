# reasoning_part2.py
REASONING_PART2_DATA = {
    "43": {
        "title": "Blood Relations: Family Tree Diagrams, Coded Genealogies & Conversational Puzzles",
        "source_id": 7,
        "content": {
            "definition": "Blood Relations in competitive examinations evaluate the capacity to trace and decode multi-generational biological and matrimonial lineages through symbolic representations or conversational references. Evaluated across SSC CGL, IBPS/SBI PO, RRB, and State PSCs, problems encompass generation-level hierarchies, gender determination rules, coded algebraic relationships ($P \\times Q \\implies P \\text{ is mother of } Q$), and direct pointing/portrait conversational deductions.",
            "overview": "Essential Lineage Rules & Standard Notation:\n- Gender Notation: Square / Plus sign $[+]$ for Male; Circle / Minus sign $[-]$ for Female\n- Matrimonial Link: Double horizontal line $(=)$ between husband and wife\n- Sibling Link: Single horizontal line $(-)$ with bracket\n- Generational Step: Vertical line $(\\mid)$ descending from parent to child\n- Generation Levels:\n  - Level +2: Grandparents (Paternal / Maternal grandfather & grandmother)\n  - Level +1: Parents, Uncles, Aunts (Paternal: Chacha, Tau, Bua; Maternal: Mama, Mami, Mausi)\n  - Level 0: Self, Spouse, Siblings, Cousins, Brother-in-law, Sister-in-law\n  - Level -1: Children, Nephews, Nieces\n  - Level -2: Grandchildren (Grandson, Granddaughter)",
            "types": [
                {
                    "name": "1. Pointing / Portrait Conversational Questions",
                    "desc": "Deducing relationships when a speaker points to a photograph or person ('He is the only son of my father's father').",
                    "examples": [
                        "'The only son of my grandfather' = Speaker's Father",
                        "'Daughter of the only son of my grandfather' = Speaker's Sister (or Self if female)"
                    ]
                },
                {
                    "name": "2. Coded Blood Relations",
                    "desc": "Lineage chains described using mathematical or punctuation operators (e.g. $A + B$ means $A$ is sister of $B$).",
                    "examples": [
                        "Evaluate $P \\div Q - R + S$ by decoding step-by-step from left to right",
                        "Determine which expression proves $M$ is the maternal uncle of $N$"
                    ]
                },
                {
                    "name": "3. Multi-Member Family Tree Puzzles",
                    "desc": "Complex family structures involving 6-8 members across 3 generations with married couples and professions.",
                    "examples": [
                        "3 married couples in a 7-member family: building the complete generational tree",
                        "Identifying the number of male and female members in the household"
                    ]
                },
                {
                    "name": "4. Maternal vs Paternal Relationship Distinctions",
                    "desc": "Distinguishing relations on the father's side (Paternal) versus the mother's side (Maternal).",
                    "examples": [
                        "Father's brother = Paternal Uncle; Mother's brother = Maternal Uncle",
                        "Father's sister's son = Paternal Cousin; Mother's sister = Maternal Aunt"
                    ]
                },
                {
                    "name": "5. In-Law Matrimonial Relationships",
                    "desc": "Relations formed through marriage (Spouse's siblings, Sibling's spouses, Children's spouses).",
                    "examples": [
                        "Sister-in-law: Husband's sister, Wife's sister, Brother's wife",
                        "Brother-in-law: Husband's brother, Wife's brother, Sister's husband"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Never Assume Gender from a Name Rule",
                    "explanation": "In competitive exams, gender CANNOT be inferred from traditional human names (e.g., 'Kiran', 'Suman', 'Bobby', 'Raman'). Gender MUST be explicitly stated through pronouns (he/she), titles (father, sister), or matrimonial pairing (husband implies the other spouse is female).",
                    "words": [
                        "No Name Assumptions",
                        "Explicit Gender Proof",
                        "Pronoun Validation"
                    ],
                    "correct": "'A is the child of B' leaves A's gender undetermined unless 'A is the son' or 'A is brother' is stated.",
                    "incorrect": "Assuming 'Pooja' is female without explicit textual proof."
                },
                {
                    "rule_number": 2,
                    "title": "'Only Son / Daughter' Deductive Rule",
                    "explanation": "- 'Only son of my father' = The speaker himself (if speaker is male) or the speaker's brother (if speaker is female).\n- 'Only child of my father' = The speaker himself/herself (strictly unique offspring).\n- 'My father's only son's wife' = Speaker's wife (if male) or Sister-in-law (if female).",
                    "words": [
                        "Only Son vs Only Child",
                        "Self Substitution",
                        "Deduction"
                    ],
                    "correct": "Male speaker says: 'His mother is the only daughter of my mother.' My mother's only daughter = My sister. Thus, his mother is my sister => I am his Maternal Uncle.",
                    "incorrect": "Equating 'only son' with 'only child' (ignoring potential sisters)."
                },
                {
                    "rule_number": 3,
                    "title": "Coded Relations Gender and Generation Gap Elimination",
                    "explanation": "When asked 'Which option proves $M$ is female?':\n1. Eliminate options where $M$ is at the very end of an expression without a following operator (gender usually unknown).\n2. Eliminate options where $M$'s operator assigns a male gender ($M$ is father/brother).\n3. Check generation gap: $Father (+1), Son (-1), Sister (0)$. Total sum must match the target gap.",
                    "words": [
                        "Option Elimination",
                        "Gender Check",
                        "Generation Gap Calculation"
                    ],
                    "correct": "If $M$ must be female, eliminate option $M \\times K$ where '$\\times$' means 'is brother of'.",
                    "incorrect": "Drawing complete family trees for all 4 options, wasting 3 minutes."
                },
                {
                    "rule_number": 4,
                    "title": "Backward Parsing in Pointing Problems",
                    "explanation": "In statements like 'He is the son of the daughter of the father of my wife': Start parsing from the end ('my wife') backwards step-by-step:\n1. 'My wife'\n2. 'Father of my wife' = Father-in-law\n3. 'Daughter of my father-in-law' = Wife (or Sister-in-law)\n4. 'Son of my wife' = Son.",
                    "words": [
                        "Backward Parsing",
                        "Start from 'My'",
                        "Deconstruction"
                    ],
                    "correct": "Parsing backwards from 'my' breaks the sentence into 4 instant simplifications.",
                    "incorrect": "Trying to translate the sentence from the first word forward."
                },
                {
                    "rule_number": 5,
                    "title": "Matrimonial Implied Gender Complementarity",
                    "explanation": "In standard biological family reasoning problems, marriage is heterosexual. If member $A$ is the husband, spouse $B$ is definitively female (wife). Conversely, if $B$ is the wife, $A$ is definitively male (husband).",
                    "words": [
                        "Matrimonial Complementarity",
                        "Husband implies Wife",
                        "Gender Proof"
                    ],
                    "correct": "If A is married to B and A is the father of C, then B is definitively the mother of C (Female).",
                    "incorrect": "Leaving B's gender as unknown."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Assuming the speaker is male when not specified.",
                    "correction": "Always check both possibilities (speaker is male or female) if gender is not fixed.",
                    "rationale": "'The only daughter of my mother' is the speaker herself if female, but the speaker's sister if male."
                },
                {
                    "mistake": "Confusing Paternal and Maternal relatives.",
                    "correction": "Paternal relates to Father (Chacha/Bua); Maternal relates to Mother (Mama/Mausi).",
                    "rationale": "High-frequency trap in bilingual SSC and State exams."
                },
                {
                    "mistake": "Treating 'Cousin' as having a gender.",
                    "correction": "Cousin is a gender-neutral term covering both male and female relatives.",
                    "rationale": "Never say 'Cousin brother' or 'Cousin sister' in formal reasoning."
                },
                {
                    "mistake": "Drawing whole trees instead of using gender elimination in coded relations.",
                    "correction": "Check the candidate's immediate gender operator first to eliminate 2-3 options in 10 seconds.",
                    "rationale": "Saves 80% of test time in Bank PO / SSC Tier 2."
                }
            ],
            "quick_revision_points": [
                "Use standard tree symbols: Square = Male, Circle = Female, '=' = Married, '|' = Generation shift",
                "Never assume gender from a proper name without an explicit relationship tag",
                "'Only child' means zero brothers and zero sisters; 'Only son' allows multiple sisters",
                "Backward parsing: start from 'my' and simplify right-to-left",
                "Generation Gaps: Grandparents (+2), Parents (+1), Siblings/Spouse/Cousins (0), Children (-1)",
                "Nephew = Brother's or Sister's Son; Niece = Brother's or Sister's Daughter",
                "Uncle's or Aunt's child is always a COUSIN"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4301,
                "topic_id": 43,
                "exam_id": 1,
                "question": "Pointing to a photograph of a lady, a man said, 'The only daughter of her brother is the sister of my wife.' How is the lady related to the man's wife? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Father's sister (Aunt)",
                    "Mother",
                    "Sister",
                    "Sister-in-law"
                ],
                "correct_answer": "Father's sister (Aunt)",
                "explanation": "Let us deconstruct from the man's perspective:\n- 'Sister of my wife' = Wife's sister.\n- So, 'the only daughter of her brother' = Wife's sister.\n- This implies the lady's brother is the father of the man's wife.\n- Since the lady is the sister of the father of the man's wife, the lady is the Father's sister (Paternal Aunt) of the man's wife.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4302,
                "topic_id": 43,
                "exam_id": 1,
                "question": "If 'A + B' means 'A is the father of B', 'A - B' means 'A is the wife of B', 'A * B' means 'A is the brother of B', which of the following shows that 'P is the mother of R'? [IBPS PO Prelims 2022]",
                "options_json": [
                    "P - Q + R",
                    "Q + P - R",
                    "P * Q + R",
                    "R - P + Q"
                ],
                "correct_answer": "P - Q + R",
                "explanation": "In option 'P - Q + R':\n- P - Q means P is the wife of Q (P is female, Q is male).\n- Q + R means Q is the father of R.\n- Since P is the wife of Q and Q is the father of R, P is definitively the mother of R.\nThus, P - Q + R is correct.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4303,
                "topic_id": 43,
                "exam_id": 1,
                "question": "A is the brother of B. C is the father of A. D is the brother of E. E is the daughter of B. Who is the uncle of D? [RRB NTPC 2022]",
                "options_json": [
                    "A",
                    "B",
                    "C",
                    "E"
                ],
                "correct_answer": "A",
                "explanation": "- E is the daughter of B, and D is the brother of E. So D and E are children of B.\n- A is the brother of B.\n- Since A is the brother of D's parent B, A is the uncle of D.\nTherefore, the correct answer is A.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4301,
                "topic_id": 43,
                "question": "Pointing to a man, a woman says, 'He is the only son of my mother's father.' How is the man related to the woman?",
                "options_json": [
                    "Maternal Uncle",
                    "Father",
                    "Brother",
                    "Cousin"
                ],
                "correct_answer": "Maternal Uncle",
                "explanation": "Mother's father = Maternal Grandfather. The only son of maternal grandfather = Maternal Uncle (Mama).",
                "points": 1
            },
            {
                "id": 4302,
                "topic_id": 43,
                "question": "If A is the son of B, and B is the daughter of C, how is A related to C?",
                "options_json": [
                    "Grandson",
                    "Son",
                    "Nephew",
                    "Uncle"
                ],
                "correct_answer": "Grandson",
                "explanation": "C is the grandparent of A. Since A is male (son), A is the grandson of C.",
                "points": 1
            },
            {
                "id": 4303,
                "topic_id": 43,
                "question": "P is the brother of Q. R is the sister of P. S is the sister of T. T is the son of Q. How is P related to T?",
                "options_json": [
                    "Uncle",
                    "Father",
                    "Brother",
                    "Grandfather"
                ],
                "correct_answer": "Uncle",
                "explanation": "Q is the parent of T. P is the brother of Q. Therefore, P is the uncle of T.",
                "points": 1
            },
            {
                "id": 4304,
                "topic_id": 43,
                "question": "Pointing to a photograph, Rohit said, 'She is the daughter of my grandfather's only son.' How is she related to Rohit?",
                "options_json": [
                    "Sister",
                    "Mother",
                    "Aunt",
                    "Cousin"
                ],
                "correct_answer": "Sister",
                "explanation": "Grandfather's only son = Rohit's Father. The daughter of Rohit's father = Rohit's sister.",
                "points": 1
            },
            {
                "id": 4305,
                "topic_id": 43,
                "question": "If X is the brother of Y's husband, how is X related to Y?",
                "options_json": [
                    "Brother-in-law",
                    "Husband",
                    "Brother",
                    "Father-in-law"
                ],
                "correct_answer": "Brother-in-law",
                "explanation": "The brother of one's husband is one's Brother-in-law.",
                "points": 1
            },
            {
                "id": 4306,
                "topic_id": 43,
                "question": "A and B are married. A is the husband. C is the son of A. How is C related to B?",
                "options_json": [
                    "Son",
                    "Nephew",
                    "Brother",
                    "Husband"
                ],
                "correct_answer": "Son",
                "explanation": "Since A and B are husband and wife, the son of A is also the son of B.",
                "points": 1
            },
            {
                "id": 4307,
                "topic_id": 43,
                "question": "What is the relation of your father's sister's daughter to you?",
                "options_json": [
                    "Cousin",
                    "Niece",
                    "Sister",
                    "Aunt"
                ],
                "correct_answer": "Cousin",
                "explanation": "Father's sister is your aunt (Bua). Her daughter is your Cousin.",
                "points": 1
            },
            {
                "id": 4308,
                "topic_id": 43,
                "question": "M is the sister of N. N is married to O. O is the father of P. How is M related to P?",
                "options_json": [
                    "Maternal Aunt",
                    "Mother",
                    "Sister",
                    "Paternal Aunt"
                ],
                "correct_answer": "Maternal Aunt",
                "explanation": "O is father, so N (married to O) is the mother of P. M is the sister of mother N. Thus M is the Maternal Aunt of P.",
                "points": 1
            },
            {
                "id": 4309,
                "topic_id": 43,
                "question": "A woman introduces a man as the son of the brother of her mother. How is the man related to her?",
                "options_json": [
                    "Cousin",
                    "Nephew",
                    "Brother",
                    "Uncle"
                ],
                "correct_answer": "Cousin",
                "explanation": "Brother of mother = Maternal Uncle. Son of maternal uncle = Maternal Cousin.",
                "points": 1
            },
            {
                "id": 4310,
                "topic_id": 43,
                "question": "If your sister's daughter is calling you, she is your:",
                "options_json": [
                    "Niece",
                    "Nephew",
                    "Cousin",
                    "Daughter"
                ],
                "correct_answer": "Niece",
                "explanation": "A sibling's daughter is a Niece.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4301,
                "topic_id": 43,
                "question": "Who is the son of your father's brother?",
                "options_json": [
                    "Cousin",
                    "Brother",
                    "Nephew",
                    "Uncle"
                ],
                "correct_answer": "Cousin",
                "explanation": "Father's brother = Uncle. Uncle's son = Cousin.",
                "points": 1
            },
            {
                "id": 4302,
                "topic_id": 43,
                "question": "If A is B's brother, and B is C's sister, how is A related to C?",
                "options_json": [
                    "Brother",
                    "Sister",
                    "Cousin",
                    "Cannot say"
                ],
                "correct_answer": "Brother",
                "explanation": "A, B, and C are all siblings. Since A is male, A is the brother of C.",
                "points": 1
            },
            {
                "id": 4303,
                "topic_id": 43,
                "question": "A man says: 'The father of the girl in the photo is my only son.' Who is the man to the girl?",
                "options_json": [
                    "Grandfather",
                    "Father",
                    "Uncle",
                    "Brother"
                ],
                "correct_answer": "Grandfather",
                "explanation": "The girl's father is the man's son. So the man is the girl's Grandfather.",
                "points": 1
            },
            {
                "id": 4304,
                "topic_id": 43,
                "question": "How is your mother's brother's wife related to you?",
                "options_json": [
                    "Maternal Aunt",
                    "Mother",
                    "Grandmother",
                    "Paternal Aunt"
                ],
                "correct_answer": "Maternal Aunt",
                "explanation": "Mother's brother = Maternal Uncle (Mama). His wife = Maternal Aunt (Mami).",
                "points": 1
            },
            {
                "id": 4305,
                "topic_id": 43,
                "question": "If P is the daughter of Q, and Q is the son of R, what is P to R?",
                "options_json": [
                    "Granddaughter",
                    "Daughter",
                    "Grandmother",
                    "Niece"
                ],
                "correct_answer": "Granddaughter",
                "explanation": "R -> Q (Son) -> P (Daughter). P is the granddaughter of R.",
                "points": 1
            },
            {
                "id": 4306,
                "topic_id": 43,
                "question": "What is the relation of your brother's wife to you?",
                "options_json": [
                    "Sister-in-law",
                    "Sister",
                    "Cousin",
                    "Aunt"
                ],
                "correct_answer": "Sister-in-law",
                "explanation": "Brother's wife is Sister-in-law (Bhabhi).",
                "points": 1
            },
            {
                "id": 4307,
                "topic_id": 43,
                "question": "Can you determine the gender of a person named 'Taylor' if the problem only states 'Taylor is the child of Morgan'?",
                "options_json": [
                    "No",
                    "Yes, female",
                    "Yes, male",
                    "Yes, parent"
                ],
                "correct_answer": "No",
                "explanation": "Gender cannot be assumed without explicit pronouns or kinship descriptors.",
                "points": 1
            },
            {
                "id": 4308,
                "topic_id": 43,
                "question": "Pointing to a boy, Priya says, 'He is the only son of my husband.' Who is the boy to Priya?",
                "options_json": [
                    "Son",
                    "Brother",
                    "Nephew",
                    "Uncle"
                ],
                "correct_answer": "Son",
                "explanation": "Her husband's son is also her son.",
                "points": 1
            },
            {
                "id": 4309,
                "topic_id": 43,
                "question": "If X is the father of Y, but Y is not the son of X, what is Y to X?",
                "options_json": [
                    "Daughter",
                    "Father",
                    "Mother",
                    "Grandson"
                ],
                "correct_answer": "Daughter",
                "explanation": "If Y is a child of X but not the son, Y must be the daughter.",
                "points": 1
            },
            {
                "id": 4310,
                "topic_id": 43,
                "question": "How many generations are spanned between a Great-Grandfather and a Child?",
                "options_json": [
                    "3 generations apart (4 levels)",
                    "2 generations",
                    "1 generation",
                    "4 generations apart"
                ],
                "correct_answer": "3 generations apart (4 levels)",
                "explanation": "Level 0 (Child), Level 1 (Parent), Level 2 (Grandparent), Level 3 (Great-Grandparent). They are 3 generations apart across 4 generation levels.",
                "points": 1
            }
        ]
    },
    "44": {
        "title": "Direction Sense: Compass Navigation, Pythagoras Displacement & Shadow Logic",
        "source_id": 7,
        "content": {
            "definition": "Direction Sense tests spatial orientation, path tracing across an 8-point Cartesian compass, net displacement calculation via the Pythagorean Theorem, and solar shadow position deductions. Prominent in SSC CGL Tier 1/2, IBPS/SBI PO, and Railways examinations, questions examine sequential right/left turns, clockwise/counter-clockwise angular rotations ($45^\\circ, 90^\\circ, 135^\\circ, 180^\\circ$), and sunrise/sunset shadow angles.",
            "overview": "Essential Compass System & Rules:\n- 4 Main Cardinal Directions: North (Up / $0^\\circ$), East (Right / $90^\\circ$), South (Down / $180^\\circ$), West (Left / $270^\\circ$)\n- 4 Intercardinal Directions: North-East (NE / $45^\\circ$), South-East (SE / $135^\\circ$), South-West (SW / $225^\\circ$), North-West (NW / $315^\\circ$)\n- Turn Conventions:\n  - Right Turn = $90^\\circ$ Clockwise (CW)\n  - Left Turn = $90^\\circ$ Anti-Clockwise (ACW)\n- Pythagorean Shortest Distance: $\\text{Displacement } D = \\sqrt{(\\Sigma X)^2 + (\\Sigma Y)^2}$\n- Shadow Rules:\n  - At Sunrise (Sun in East): Shadows fall strictly to the WEST\n  - At Sunset (Sun in West): Shadows fall strictly to the EAST\n  - At 12:00 Noon: The sun is directly overhead; NO horizontal shadow is cast",
            "types": [
                {
                    "name": "1. Multi-Step Distance & Path Trajectory",
                    "desc": "Walking successive distances in cardinal directions to determine final position relative to start point.",
                    "examples": [
                        "Walks 10m North, turns right walks 5m, turns right walks 10m => 5m East of start point",
                        "Net coordinate cancellation: +10 North and -10 South cancel out"
                    ]
                },
                {
                    "name": "2. Shortest Distance (Pythagoras Theorem)",
                    "desc": "Calculating straight-line Euclidean displacement between starting point and endpoint.",
                    "examples": [
                        "Walks 3 km East, then 4 km North: D = sqrt(3^2 + 4^2) = sqrt(25) = 5 km North-East",
                        "Walks 6 km West, then 8 km South: D = sqrt(6^2 + 8^2) = 10 km South-West"
                    ]
                },
                {
                    "name": "3. Angular Rotation & Headings",
                    "desc": "Person turns through specific angles clockwise or counter-clockwise from an initial heading.",
                    "examples": [
                        "Facing North, turns 90 deg CW (East), then 135 deg ACW (North-West)",
                        "Net rotation = Sum of CW - Sum of ACW"
                    ]
                },
                {
                    "name": "4. Sunrise and Sunset Shadow Problems",
                    "desc": "Deducing facing direction from the orientation of a shadow (to one's left, right, front, or back).",
                    "examples": [
                        "At sunrise, if shadow is to your right => You are facing South",
                        "At sunrise, if shadow is to your left => You are facing North"
                    ]
                },
                {
                    "name": "5. Coded Direction & Distance Puzzles",
                    "desc": "Direction relationships encoded using symbols (e.g. $P @ Q$ means $P$ is 6m North of $Q$).",
                    "examples": [
                        "High-level Bank PO puzzles mapping multiple points in a coordinate grid"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Turn Relativity Depends on Current Facing Heading",
                    "explanation": "- Facing North: Right = East, Left = West\n- Facing South: Right = West, Left = East (Reversed!)\n- Facing East: Right = South, Left = North\n- Facing West: Right = North, Left = South.",
                    "words": [
                        "Heading Dependent Turns",
                        "South Reversal Trap",
                        "Right=CW, Left=ACW"
                    ],
                    "correct": "When facing South, taking a Right turn points you WEST.",
                    "incorrect": "Assuming Right turn is always East regardless of facing direction."
                },
                {
                    "rule_number": 2,
                    "title": "Pythagoras Displacement Formula",
                    "explanation": "The straight-line shortest distance $D$ between origin $(0,0)$ and final coordinates $(x, y)$ is given by $D = \\sqrt{x^2 + y^2}$. Memorize common Pythagorean triplets: $(3, 4, 5)$, $(5, 12, 13)$, $(6, 8, 10)$, $(8, 15, 17)$, $(7, 24, 25)$.",
                    "words": [
                        "Pythagoras Theorem",
                        "Triplets (3,4,5), (5,12,13)",
                        "Shortest Distance"
                    ],
                    "correct": "Net displacement 5m East and 12m North => D = sqrt(25 + 144) = 13m.",
                    "incorrect": "Adding distances arithmetically (5 + 12 = 17m)."
                },
                {
                    "rule_number": 3,
                    "title": "Sunrise & Sunset Shadow Matrix Rule",
                    "explanation": "- **At Sunrise (Sun in East => Shadow falls West)**:\n  - Facing North $\\implies$ Shadow to Left\n  - Facing South $\\implies$ Shadow to Right\n  - Facing East $\\implies$ Shadow Behind\n  - Facing West $\\implies$ Shadow in Front\n- **At Sunset (Sun in West => Shadow falls East)**:\n  - Facing North $\\implies$ Shadow to Right\n  - Facing South $\\implies$ Shadow to Left.",
                    "words": [
                        "Shadow Matrix",
                        "Sunrise = Shadow West",
                        "Sunset = Shadow East"
                    ],
                    "correct": "One morning, Amit's shadow was exactly to his left. Thus, Amit was facing North.",
                    "incorrect": "Saying Amit was facing East."
                },
                {
                    "rule_number": 4,
                    "title": "Net Angular Rotation Shortcut",
                    "explanation": "When multiple turns are made:\n$\\text{Net Rotation} = \\sum (\\text{Clockwise Angles}) - \\sum (\\text{Anti-Clockwise Angles})$.\nIf the result is positive, turn that angle Clockwise from the starting heading. If negative, turn Anti-Clockwise.",
                    "words": [
                        "Net Angle",
                        "Sum(CW) - Sum(ACW)",
                        "Rapid Angle Shortcut"
                    ],
                    "correct": "Facing East. Turns 45 CW, then 90 CW, then 180 ACW: Net = (45 + 90) - 180 = 135 - 180 = -45 (45 ACW). East rotated 45 ACW = North-East.",
                    "incorrect": "Redrawing the entire figure 3 times."
                },
                {
                    "rule_number": 5,
                    "title": "Origin vs Current Heading Distinction",
                    "explanation": "Exams ask two distinct questions:\n(1) 'In which direction is he from the STARTING point?' (Requires vector from origin $(0,0)$ to final $(x,y)$).\n(2) 'In which direction is he now FACING?' (Requires only the last heading after the final turn).",
                    "words": [
                        "Starting Point vs Facing Heading",
                        "Crucial Distinction",
                        "Exam Trap"
                    ],
                    "correct": "Final position is (5m East, 0m North), but person turned South at the end: From start point = East; Facing = South.",
                    "incorrect": "Confusing the direction from start point with the facing direction."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Adding path distances linearly when asked for 'shortest distance'.",
                    "correction": "Shortest distance is the hypotenuse $D = \\sqrt{\\Delta x^2 + \\Delta y^2}$, not total path traveled.",
                    "rationale": "Exam questions deliberately offer total path distance as Option A."
                },
                {
                    "mistake": "Turning Right towards East when facing South.",
                    "correction": "When facing South, turning Right moves you WEST.",
                    "rationale": "Turning Right is clockwise. From South ($180^\\circ$), CW brings you to West ($270^\\circ$)."
                },
                {
                    "mistake": "Assuming shadows fall in the direction of the sun.",
                    "correction": "Shadows fall strictly in the direction OPPOSITE to the sun (Sun in East => Shadow in West).",
                    "rationale": "Light travel physics rule."
                },
                {
                    "mistake": "Confusing 'Facing direction' with 'Direction from starting point'.",
                    "correction": "Check the exact question prompt: 'facing' vs 'with respect to starting position'.",
                    "rationale": "High-frequency trap in competitive reasoning tests."
                }
            ],
            "quick_revision_points": [
                "Cardinal: North (Up), South (Down), East (Right), West (Left)",
                "Intercardinal: NE, SE, SW, NW (each at 45 degrees)",
                "Right turn = 90 deg Clockwise; Left turn = 90 deg Anti-Clockwise",
                "Pythagorean triplets: (3,4,5), (5,12,13), (6,8,10), (8,15,17), (7,24,25)",
                "Sunrise: Sun = East, Shadow = West. Facing North => Shadow to Left; Facing South => Shadow to Right",
                "Sunset: Sun = West, Shadow = East. Facing North => Shadow to Right; Facing South => Shadow to Left",
                "Net angle = Total CW - Total ACW"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4401,
                "topic_id": 44,
                "exam_id": 1,
                "question": "A man walks 5 km toward South and then turns to the right. After walking 3 km, he turns to the left and walks 5 km. Now in which direction is he from the starting place? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "South-West",
                    "South-East",
                    "North-East",
                    "North-West"
                ],
                "correct_answer": "South-West",
                "explanation": "Trace coordinates from origin (0, 0):\n1. Walks 5 km South: (0, -5)\n2. Turns right (facing South, right is West) and walks 3 km: (-3, -5)\n3. Turns left (facing West, left is South) and walks 5 km: (-3, -10)\nFinal coordinates: x = -3 (West), y = -10 (South).\nRelative to starting position, he is in the South-West direction.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4402,
                "topic_id": 44,
                "exam_id": 1,
                "question": "One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. In which direction was Suresh facing? [IBPS PO Prelims 2022]",
                "options_json": [
                    "South",
                    "North",
                    "East",
                    "West"
                ],
                "correct_answer": "South",
                "explanation": "At sunrise, the sun is in the East, so all shadows fall toward the WEST.\nThe shadow of the pole fell to Suresh's right, meaning Suresh's right side is facing WEST.\nWhen a person's right side is West, the person is facing SOUTH.\nTherefore, Suresh was facing South.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4403,
                "topic_id": 44,
                "exam_id": 1,
                "question": "A person walks 12 km North, then 5 km East. What is the shortest distance between his starting point and final point? [RRB NTPC 2022]",
                "options_json": [
                    "13 km",
                    "17 km",
                    "15 km",
                    "11 km"
                ],
                "correct_answer": "13 km",
                "explanation": "By Pythagoras Theorem:\nShortest distance D = sqrt((12)^2 + (5)^2) = sqrt(144 + 25) = sqrt(169) = 13 km.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4401,
                "topic_id": 44,
                "question": "A person walks 3 km North, then turns right and walks 4 km. Find the shortest distance from the starting point.",
                "options_json": [
                    "5 km",
                    "7 km",
                    "6 km",
                    "4 km"
                ],
                "correct_answer": "5 km",
                "explanation": "D = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 km.",
                "points": 1
            },
            {
                "id": 4402,
                "topic_id": 44,
                "question": "A boy facing North turns 90 degrees clockwise, then 180 degrees clockwise. Which direction is he now facing?",
                "options_json": [
                    "West",
                    "South",
                    "East",
                    "North"
                ],
                "correct_answer": "West",
                "explanation": "Total CW rotation = 90 + 180 = 270 degrees CW. From North, 270 degrees CW points West.",
                "points": 1
            },
            {
                "id": 4403,
                "topic_id": 44,
                "question": "If you are facing East and turn left, which direction do you face?",
                "options_json": [
                    "North",
                    "South",
                    "West",
                    "North-East"
                ],
                "correct_answer": "North",
                "explanation": "Left turn is 90 degrees counter-clockwise. From East, turning left points North.",
                "points": 1
            },
            {
                "id": 4404,
                "topic_id": 44,
                "question": "At sunset, a woman finds her shadow falling directly behind her. Which direction is she facing?",
                "options_json": [
                    "West",
                    "East",
                    "North",
                    "South"
                ],
                "correct_answer": "West",
                "explanation": "At sunset, the sun is in the West, so shadows fall toward the EAST. For her shadow to be behind her, she must be facing WEST (towards the sun).",
                "points": 1
            },
            {
                "id": 4405,
                "topic_id": 44,
                "question": "A car travels 10 km East, turns right and travels 10 km South. What is the direction from start?",
                "options_json": [
                    "South-East",
                    "North-East",
                    "South-West",
                    "North-West"
                ],
                "correct_answer": "South-East",
                "explanation": "Coordinates: (+10, -10). The direction is South-East.",
                "points": 1
            },
            {
                "id": 4406,
                "topic_id": 44,
                "question": "Walking towards South, turning right means turning towards:",
                "options_json": [
                    "West",
                    "East",
                    "North",
                    "South-West"
                ],
                "correct_answer": "West",
                "explanation": "When facing South, turning right (clockwise 90 deg) points West.",
                "points": 1
            },
            {
                "id": 4407,
                "topic_id": 44,
                "question": "A person walks 8 km West, turns left and walks 6 km. What is the shortest distance from origin?",
                "options_json": [
                    "10 km",
                    "14 km",
                    "12 km",
                    "8 km"
                ],
                "correct_answer": "10 km",
                "explanation": "D = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km.",
                "points": 1
            },
            {
                "id": 4408,
                "topic_id": 44,
                "question": "Facing North-West, a person turns 90 degrees clockwise. Which direction is he facing?",
                "options_json": [
                    "North-East",
                    "South-East",
                    "South-West",
                    "East"
                ],
                "correct_answer": "North-East",
                "explanation": "North-West (315 deg) + 90 deg CW = 45 deg = North-East.",
                "points": 1
            },
            {
                "id": 4409,
                "topic_id": 44,
                "question": "At 12:00 noon on the equator, where does a person's shadow fall?",
                "options_json": [
                    "Directly beneath / No horizontal shadow",
                    "To the West",
                    "To the East",
                    "To the North"
                ],
                "correct_answer": "Directly beneath / No horizontal shadow",
                "explanation": "The sun is directly overhead at zenith, so no horizontal shadow is cast.",
                "points": 1
            },
            {
                "id": 4410,
                "topic_id": 44,
                "question": "A man walks 15 km North, then 20 km East. What is the straight line distance?",
                "options_json": [
                    "25 km",
                    "35 km",
                    "30 km",
                    "20 km"
                ],
                "correct_answer": "25 km",
                "explanation": "D = sqrt(15^2 + 20^2) = sqrt(225 + 400) = sqrt(625) = 25 km (3-4-5 triplet scaled by 5).",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4401,
                "topic_id": 44,
                "question": "Which direction is opposite to South-East?",
                "options_json": [
                    "North-West",
                    "North-East",
                    "South-West",
                    "North"
                ],
                "correct_answer": "North-West",
                "explanation": "Opposite of South is North, opposite of East is West => North-West.",
                "points": 1
            },
            {
                "id": 4402,
                "topic_id": 44,
                "question": "What angle is between North and East?",
                "options_json": [
                    "90\u00b0",
                    "45\u00b0",
                    "180\u00b0",
                    "135\u00b0"
                ],
                "correct_answer": "90\u00b0",
                "explanation": "Adjacent cardinal directions are at 90 degrees to each other.",
                "points": 1
            },
            {
                "id": 4403,
                "topic_id": 44,
                "question": "If you walk 6 m East, then 8 m North, what is the straight line distance from start?",
                "options_json": [
                    "10 m",
                    "14 m",
                    "12 m",
                    "8 m"
                ],
                "correct_answer": "10 m",
                "explanation": "sqrt(6^2 + 8^2) = sqrt(36 + 64) = 10 m.",
                "points": 1
            },
            {
                "id": 4404,
                "topic_id": 44,
                "question": "One morning at sunrise, if a boy's shadow is to his left, which direction is he facing?",
                "options_json": [
                    "North",
                    "South",
                    "East",
                    "West"
                ],
                "correct_answer": "North",
                "explanation": "Shadow is in the West. If West is to his left, he must be facing North.",
                "points": 1
            },
            {
                "id": 4405,
                "topic_id": 44,
                "question": "Facing East, you turn 180 degrees. What is your new facing direction?",
                "options_json": [
                    "West",
                    "North",
                    "South",
                    "East"
                ],
                "correct_answer": "West",
                "explanation": "A 180-degree turn reverses your heading: East becomes West.",
                "points": 1
            },
            {
                "id": 4406,
                "topic_id": 44,
                "question": "Facing South, taking two consecutive left turns (90\u00b0 each) makes you face:",
                "options_json": [
                    "North",
                    "South",
                    "East",
                    "West"
                ],
                "correct_answer": "North",
                "explanation": "Two left turns = 180 degrees turn. South + 180 deg = North.",
                "points": 1
            },
            {
                "id": 4407,
                "topic_id": 44,
                "question": "What is the angle between North-East and North-West?",
                "options_json": [
                    "90\u00b0",
                    "45\u00b0",
                    "135\u00b0",
                    "180\u00b0"
                ],
                "correct_answer": "90\u00b0",
                "explanation": "North-East is 45\u00b0 CW from North, North-West is 45\u00b0 ACW from North. Total angle = 45 + 45 = 90\u00b0.",
                "points": 1
            },
            {
                "id": 4408,
                "topic_id": 44,
                "question": "A traveler goes 4 km North, then 3 km West. In which direction is he from starting point?",
                "options_json": [
                    "North-West",
                    "North-East",
                    "South-West",
                    "South-East"
                ],
                "correct_answer": "North-West",
                "explanation": "Displacement has positive North component and negative West component => North-West.",
                "points": 1
            },
            {
                "id": 4409,
                "topic_id": 44,
                "question": "In the evening before sunset, shadows fall towards which direction?",
                "options_json": [
                    "East",
                    "West",
                    "North",
                    "South"
                ],
                "correct_answer": "East",
                "explanation": "Sun is in the West in the evening, so shadows fall toward the East.",
                "points": 1
            },
            {
                "id": 4410,
                "topic_id": 44,
                "question": "If you start at point A, walk 10 m North, 10 m East, 10 m South, and 10 m West, where are you?",
                "options_json": [
                    "Back at point A",
                    "10 m North of A",
                    "10 m East of A",
                    "20 m away from A"
                ],
                "correct_answer": "Back at point A",
                "explanation": "The movements form a closed square: net displacement is zero, returning to point A.",
                "points": 1
            }
        ]
    },
    "45": {
        "title": "Ranking & Order: Linear Queues, Position Interchanging & Overlapping Logic",
        "source_id": 7,
        "content": {
            "definition": "Ranking and Order evaluates positional logic within finite ordered sequences (queues, classroom merit lists, seating rows). Tested rigorously in SSC CGL, IBPS/SBI Clerk, RRB, and State PSCs, problems require calculating total strength $T = (L + R) - 1$, finding rank from opposite ends, determining person counts between two ranked individuals, solving position interchanging dilemmas, and analyzing overlapping vs non-overlapping queue configurations.",
            "overview": "Fundamental Ranking Formulas:\n- Total Number in a Single Row: $T = \\text{Rank from Left } (L) + \\text{Rank from Right } (R) - 1$\n- Rank from Opposite End:\n  - $L = (T - R) + 1$\n  - $R = (T - L) + 1$\n- Persons Between Two Individuals (Non-Overlapping): $\\text{Middle} = T - (L_A + R_B)$ (Valid when $T > L_A + R_B$)\n- Persons Between Two Individuals (Overlapping Case): $\\text{Middle} = (L_A + R_B) - T - 2$ (Valid when $L_A + R_B > T$)\n- Minimum Number of Persons in Row: $T_{\\text{min}} = (L_A + R_B) - \\text{Middle} - 2$",
            "types": [
                {
                    "name": "1. Single Person Bidirectional Ranking",
                    "desc": "Calculating total persons or rank from one end when a single person's rank from both ends is known.",
                    "examples": [
                        "Ravi is 10th from left and 15th from right: Total = 10 + 15 - 1 = 24",
                        "Total 50 students, Priya is 18th from top: Rank from bottom = (50 - 18) + 1 = 33"
                    ]
                },
                {
                    "name": "2. Position Interchanging Dilemmas",
                    "desc": "Two individuals swap positions, revealing a new rank that allows determining total strength.",
                    "examples": [
                        "A (10th from left) swaps with B (9th from right). A is now 15th from left => Total = 15 + 9 - 1 = 23"
                    ]
                },
                {
                    "name": "3. Between / Middle Count (Non-Overlapping vs Overlapping)",
                    "desc": "Finding the number of individuals seated between two distinct people.",
                    "examples": [
                        "Total 40. A is 10th from left, B is 12th from right. Between = 40 - (10 + 12) = 18",
                        "Total 20. A is 14th from left, B is 12th from right. Overlapping between = (14 + 12) - 20 - 2 = 4"
                    ]
                },
                {
                    "name": "4. Comparative Vertical Order Ranking",
                    "desc": "Ordering individuals by height, weight, marks, or age using inequality chains ($A > B \\ge C$).",
                    "examples": [
                        "A is taller than B but shorter than C. D is shorter than B. Tallest is C"
                    ]
                },
                {
                    "name": "5. Maximum and Minimum Row Strength",
                    "desc": "Calculating theoretical extreme queue capacities given two ranks and intermediate people.",
                    "examples": [
                        "Max capacity = L + R + Middle",
                        "Min capacity = (L + R) - Middle - 2"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Minus One Double-Counting Rule",
                    "explanation": "When summing a person's rank from the left and right ($L + R$), that specific person is counted TWICE (once in the left group and once in the right group). Therefore, 1 must ALWAYS be subtracted: $T = L + R - 1$.",
                    "words": [
                        "Double Counting",
                        "Minus One Formula",
                        "T = L + R - 1"
                    ],
                    "correct": "Rank 7th from left and 12th from right: Total = 7 + 12 - 1 = 18.",
                    "incorrect": "Adding 7 + 12 = 19 (counting the student twice)."
                },
                {
                    "rule_number": 2,
                    "title": "Plus One Opposite Rank Conversion Rule",
                    "explanation": "To find rank from the opposite end given total $T$ and rank $R$: $\\text{Opposite Rank} = (T - R) + 1$. You must add 1 back because subtracting $R$ removes the person themselves from the remaining count.",
                    "words": [
                        "Opposite Rank",
                        "Plus One",
                        "(T - R) + 1"
                    ],
                    "correct": "In a row of 30, rank from left is 8: Rank from right = (30 - 8) + 1 = 23.",
                    "incorrect": "Calculating 30 - 8 = 22."
                },
                {
                    "rule_number": 3,
                    "title": "Position Interchanging Master Rule",
                    "explanation": "When person $A$ and person $B$ interchange seats, the NEW position of $A$ coincides with the ORIGINAL position of $B$. Therefore: $\\text{Total} = \\text{New Rank of } A + \\text{Old Rank of } B - 1$.",
                    "words": [
                        "Interchange Seats",
                        "New A + Old B - 1",
                        "Total Capacity"
                    ],
                    "correct": "A is 12th left, B is 18th right. They swap. A is now 20th left: Total = 20 + 18 - 1 = 37.",
                    "incorrect": "Adding old A and old B."
                },
                {
                    "rule_number": 4,
                    "title": "Overlapping Condition Test $(L + R > T)$",
                    "explanation": "Check if $(L_A + R_B) > T$:\n- If $L_A + R_B < T \\implies$ Simple non-overlapping queue: $\\text{Between} = T - (L_A + R_B)$.\n- If $L_A + R_B > T \\implies$ Overlapping queue where $A$ and $B$ cross each other: $\\text{Between} = (L_A + R_B) - T - 2$. (The 2 accounts for $A$ and $B$ being recounted).",
                    "words": [
                        "Overlapping Test",
                        "Subtract 2",
                        "(L + R) - T - 2"
                    ],
                    "correct": "Total 25. A is 16th left, B is 14th right. 16+14=30 > 25 (Overlapping!). Between = 30 - 25 - 2 = 3.",
                    "incorrect": "Calculating 30 - 25 = 5 (forgetting to subtract 2 for the cross-count of A and B)."
                },
                {
                    "rule_number": 5,
                    "title": "Shift / Insertion Shift Rule",
                    "explanation": "If a person is shifted by $k$ places towards the left, their rank from the left DECREASES by $k$, and their rank from the right INCREASES by $k$. Total number in row remains unchanged.",
                    "words": [
                        "Positional Shifting",
                        "Conservation of Total",
                        "Rank Delta"
                    ],
                    "correct": "P is 14th from left. Shifted 3 places left => New left rank = 14 - 3 = 11.",
                    "incorrect": "Adding 3 when shifting left."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Forgetting the '- 1' in Total = Left + Right.",
                    "correction": "Always apply T = L + R - 1 because the anchor person is counted in both directions.",
                    "rationale": "Most common source of +1 mark deductions in competitive ranking tests."
                },
                {
                    "mistake": "Forgetting the '- 2' in overlapping between-count formula.",
                    "correction": "Between = (L + R) - T - 2. You must subtract 2 because both individuals are counted in both spans.",
                    "rationale": "Crucial distinction between standard and overlapping queues."
                },
                {
                    "mistake": "Calculating rank from right as simply Total - Left.",
                    "correction": "Right rank = (Total - Left) + 1.",
                    "rationale": "Subtracting Left eliminates the person, so you must add 1 to place them in the queue."
                },
                {
                    "mistake": "Assuming non-overlapping without checking L + R against Total.",
                    "correction": "Always compare (L + R) with Total first before choosing the formula.",
                    "rationale": "Prevents negative values or incorrect between counts."
                }
            ],
            "quick_revision_points": [
                "Total T = Left + Right - 1",
                "Left = (Total - Right) + 1; Right = (Total - Left) + 1",
                "Non-overlapping (T > L + R): Between = T - (L + R)",
                "Overlapping (L + R > T): Between = (L + R) - T - 2",
                "Minimum strength: T_min = (L + R) - Between - 2",
                "Maximum strength: T_max = L + R + Between",
                "Position Swap: Total = New Rank of A + Old Rank of B - 1"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4501,
                "topic_id": 45,
                "exam_id": 1,
                "question": "In a row of boys, Srinath is 7th from the left and Venkat is 12th from the right. If they interchange their positions, Srinath becomes 22nd from the left. How many boys are there in the row? [SSC CGL 2022 Tier 1]",
                "options_json": [
                    "33",
                    "34",
                    "31",
                    "32"
                ],
                "correct_answer": "33",
                "explanation": "After interchanging, Srinath sits in Venkat's original position.\nSrinath's new rank from left = 22.\nVenkat's original rank from right = 12.\nTotal boys = New Rank + Old Rank - 1 = 22 + 12 - 1 = 33.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4502,
                "topic_id": 45,
                "exam_id": 1,
                "question": "In a class of 45 students, a boy is ranked 20th. When two boys joined, his rank dropped by one. What is his new rank from the end? [RRB NTPC 2022]",
                "options_json": [
                    "27th",
                    "26th",
                    "28th",
                    "25th"
                ],
                "correct_answer": "27th",
                "explanation": "Original rank from top = 20.\nTwo boys joined, rank dropped by 1 => New rank from top = 20 + 1 = 21.\nNew total students = 45 + 2 = 47.\nNew rank from bottom = (Total - Rank from top) + 1 = (47 - 21) + 1 = 26 + 1 = 27th.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4503,
                "topic_id": 45,
                "exam_id": 1,
                "question": "In a row of 30 students, Mahesh is 14th from the left and Ramesh is 20th from the right. How many students are sitting between Mahesh and Ramesh? [IBPS Clerk 2022]",
                "options_json": [
                    "2",
                    "4",
                    "3",
                    "1"
                ],
                "correct_answer": "2",
                "explanation": "Check for overlapping:\nLeft rank (Mahesh) = 14, Right rank (Ramesh) = 20.\nSum = 14 + 20 = 34.\nTotal students = 30.\nSince Sum (34) > Total (30), this is an OVERLAPPING case.\nBetween = (L + R) - Total - 2 = (14 + 20) - 30 - 2 = 34 - 32 = 2 students.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4501,
                "topic_id": 45,
                "question": "Raju is 10th from the left and 15th from the right in a row. How many people are in the row?",
                "options_json": [
                    "24",
                    "25",
                    "23",
                    "26"
                ],
                "correct_answer": "24",
                "explanation": "Total = L + R - 1 = 10 + 15 - 1 = 24.",
                "points": 1
            },
            {
                "id": 4502,
                "topic_id": 45,
                "question": "In a class of 40 students, Priya is ranked 12th from the top. What is her rank from the bottom?",
                "options_json": [
                    "29th",
                    "28th",
                    "30th",
                    "31st"
                ],
                "correct_answer": "29th",
                "explanation": "Rank from bottom = (40 - 12) + 1 = 28 + 1 = 29th.",
                "points": 1
            },
            {
                "id": 4503,
                "topic_id": 45,
                "question": "In a row of 50 people, A is 15th from left and B is 20th from right. How many people sit between A and B?",
                "options_json": [
                    "15",
                    "16",
                    "14",
                    "17"
                ],
                "correct_answer": "15",
                "explanation": "Sum = 15 + 20 = 35 < 50 (Non-overlapping). Between = 50 - 35 = 15.",
                "points": 1
            },
            {
                "id": 4504,
                "topic_id": 45,
                "question": "A is 8th from left, B is 10th from right. They swap seats. A is now 14th from left. What is the total strength?",
                "options_json": [
                    "23",
                    "24",
                    "22",
                    "25"
                ],
                "correct_answer": "23",
                "explanation": "Total = New A + Old B - 1 = 14 + 10 - 1 = 23.",
                "points": 1
            },
            {
                "id": 4505,
                "topic_id": 45,
                "question": "In a row of 20 children, Aman is 12th from left and Raman is 11th from right. How many sit between them?",
                "options_json": [
                    "1",
                    "2",
                    "3",
                    "0"
                ],
                "correct_answer": "1",
                "explanation": "Sum = 12 + 11 = 23 > 20 (Overlapping). Between = 23 - 20 - 2 = 1.",
                "points": 1
            },
            {
                "id": 4506,
                "topic_id": 45,
                "question": "Kavita is 25th from both ends of a line. How many girls are in the line?",
                "options_json": [
                    "49",
                    "50",
                    "48",
                    "51"
                ],
                "correct_answer": "49",
                "explanation": "Total = 25 + 25 - 1 = 49.",
                "points": 1
            },
            {
                "id": 4507,
                "topic_id": 45,
                "question": "In a row of 35 students, when Mohan shifted 4 places to the left, he became 10th from the left. What was his original rank from the right?",
                "options_json": [
                    "22nd",
                    "21st",
                    "23rd",
                    "20th"
                ],
                "correct_answer": "22nd",
                "explanation": "Original left rank = 10 + 4 = 14th. Rank from right = (35 - 14) + 1 = 21 + 1 = 22nd.",
                "points": 1
            },
            {
                "id": 4508,
                "topic_id": 45,
                "question": "A is taller than B, B is taller than C, and D is taller than A. Who is the tallest?",
                "options_json": [
                    "D",
                    "A",
                    "B",
                    "C"
                ],
                "correct_answer": "D",
                "explanation": "Order: D > A > B > C. The tallest is D.",
                "points": 1
            },
            {
                "id": 4509,
                "topic_id": 45,
                "question": "What is the minimum number of persons in a row where A is 9th from left, B is 8th from right, and 2 persons sit between them?",
                "options_json": [
                    "13",
                    "15",
                    "19",
                    "11"
                ],
                "correct_answer": "13",
                "explanation": "T_min = (L + R) - Between - 2 = (9 + 8) - 2 - 2 = 17 - 4 = 13.",
                "points": 1
            },
            {
                "id": 4510,
                "topic_id": 45,
                "question": "What is the maximum number of persons in the row in the previous question (A=9th left, B=8th right, 2 between)?",
                "options_json": [
                    "19",
                    "18",
                    "20",
                    "17"
                ],
                "correct_answer": "19",
                "explanation": "T_max = L + R + Between = 9 + 8 + 2 = 19.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4501,
                "topic_id": 45,
                "question": "If Rohan is 18th from the front and 18th from the back of a line, how many people are in the line?",
                "options_json": [
                    "35",
                    "36",
                    "34",
                    "37"
                ],
                "correct_answer": "35",
                "explanation": "Total = 18 + 18 - 1 = 35.",
                "points": 1
            },
            {
                "id": 4502,
                "topic_id": 45,
                "question": "In a class of 60 students, Sunita is ranked 15th from top. What is her rank from bottom?",
                "options_json": [
                    "46th",
                    "45th",
                    "47th",
                    "44th"
                ],
                "correct_answer": "46th",
                "explanation": "(60 - 15) + 1 = 45 + 1 = 46th.",
                "points": 1
            },
            {
                "id": 4503,
                "topic_id": 45,
                "question": "If L=10, R=12, and Total=30, how many people sit in between?",
                "options_json": [
                    "8",
                    "7",
                    "9",
                    "6"
                ],
                "correct_answer": "8",
                "explanation": "Non-overlapping: Between = 30 - (10 + 12) = 30 - 22 = 8.",
                "points": 1
            },
            {
                "id": 4504,
                "topic_id": 45,
                "question": "In an overlapping row, if L=15, R=16, and Total=25, how many sit between them?",
                "options_json": [
                    "4",
                    "5",
                    "6",
                    "3"
                ],
                "correct_answer": "4",
                "explanation": "Between = (15 + 16) - 25 - 2 = 31 - 27 = 4.",
                "points": 1
            },
            {
                "id": 4505,
                "topic_id": 45,
                "question": "Why do we subtract 1 in Total = Left + Right - 1?",
                "options_json": [
                    "Because the anchor person is counted twice",
                    "Because of zero indexing",
                    "Because the first person is excluded",
                    "It is an approximation"
                ],
                "correct_answer": "Because the anchor person is counted twice",
                "explanation": "The person is included in both the left count and the right count, so one duplicate must be subtracted.",
                "points": 1
            },
            {
                "id": 4506,
                "topic_id": 45,
                "question": "In a row, X is 11th from left and Y is 14th from right. After swapping, X becomes 17th from left. How many are in the row?",
                "options_json": [
                    "30",
                    "31",
                    "29",
                    "28"
                ],
                "correct_answer": "30",
                "explanation": "Total = 17 + 14 - 1 = 30.",
                "points": 1
            },
            {
                "id": 4507,
                "topic_id": 45,
                "question": "If A is older than B, B is older than C, and C is older than D, who is the youngest?",
                "options_json": [
                    "D",
                    "C",
                    "B",
                    "A"
                ],
                "correct_answer": "D",
                "explanation": "A > B > C > D. The youngest is D.",
                "points": 1
            },
            {
                "id": 4508,
                "topic_id": 45,
                "question": "In a row of 22 students, what is the right rank of the 7th student from the left?",
                "options_json": [
                    "16th",
                    "15th",
                    "17th",
                    "14th"
                ],
                "correct_answer": "16th",
                "explanation": "Right rank = (22 - 7) + 1 = 15 + 1 = 16th.",
                "points": 1
            },
            {
                "id": 4509,
                "topic_id": 45,
                "question": "If (L + R) > Total in a ranking problem, what does it indicate?",
                "options_json": [
                    "Overlapping queue configuration",
                    "Invalid question data",
                    "Circular queue",
                    "Empty queue"
                ],
                "correct_answer": "Overlapping queue configuration",
                "explanation": "When the sum of ranks from opposite ends exceeds the total, the individuals have crossed each other (overlapping case).",
                "points": 1
            },
            {
                "id": 4510,
                "topic_id": 45,
                "question": "What is the formula for minimum total in a row with L, R, and Middle given?",
                "options_json": [
                    "(L + R) - Middle - 2",
                    "(L + R) + Middle",
                    "L + R - Middle",
                    "L + R - 1"
                ],
                "correct_answer": "(L + R) - Middle - 2",
                "explanation": "Minimum total occurs under the overlapping case: T_min = (L + R) - Middle - 2.",
                "points": 1
            }
        ]
    },
    "46": {
        "title": "Syllogism: Aristotelian Deductions, 'Only a Few', Possibility Cases & Complementary Pairs",
        "source_id": 7,
        "content": {
            "definition": "Syllogism evaluates deductive logical consequence where definite or probabilistic conclusions are evaluated strictly against given premises, irrespective of empirical real-world facts. Extensively tested across IBPS/SBI PO, SSC CGL Tier 1/2, CAT, and State Exams, modern syllogism incorporates traditional quantifiers (All, Some, No, Some Not), contemporary banking quantifiers ('Only a few', 'Only', 'At least'), possibility scenarios, and Either-Or complementary pairs.",
            "overview": "Core Propositions & Distribution Logic:\n- A-Type (Universal Affirmative): 'All $S$ are $P$' (Subject distributed, Predicate undistributed)\n- E-Type (Universal Negative): 'No $S$ is $P$' (Both distributed)\n- I-Type (Particular Affirmative): 'Some $S$ are $P$' (Neither distributed)\n- O-Type (Particular Negative): 'Some $S$ are not $P$' (Predicate distributed)\n- Modern Quantifier Translations:\n  - 'Only a few A are B' $\\equiv$ 'Some A are B' AND 'Some A are NOT B' (Dual statement!)\n  - 'Only A are B' $\\equiv$ 'All B are A' (Reversed universal affirmative)\n  - 'At least some A are B' $\\equiv$ 'Some A are B'\n- Either-Or Complementary Pairs:\n  - Pair 1: I + E ('Some A are B' + 'No A is B')\n  - Pair 2: A + O ('All A are B' + 'Some A are not B')",
            "types": [
                {
                    "name": "1. Standard Universal & Particular Categorical Syllogisms",
                    "desc": "Traditional two-premise syllogisms with 'All', 'Some', and 'No'.",
                    "examples": [
                        "Statements: All apples are fruits. All fruits are sweet. Conclusion: All apples are sweet (Definite True)",
                        "Statements: Some pens are books. Some books are pencils. Conclusion: Some pens are pencils (False/Doubtful)"
                    ]
                },
                {
                    "name": "2. Modern Banking 'Only a Few' & 'Only' Syllogisms",
                    "desc": "Propositions incorporating negative restriction alongside affirmative overlap.",
                    "examples": [
                        "'Only a few roses are red' implies (1) Some roses are red, AND (2) Some roses are definitely NOT red",
                        "'Only kings are brave' translates strictly to 'All brave are kings'"
                    ]
                },
                {
                    "name": "3. Possibility & Can-Be Scenarios",
                    "desc": "Evaluating whether a conclusion is feasible in at least one valid Venn diagram without violating premises.",
                    "examples": [
                        "If 'Some A are B', then 'All A being B is a possibility' is TRUE",
                        "If 'No A is B', then 'Some A being B is a possibility' is FALSE"
                    ]
                },
                {
                    "name": "4. Either-Or Complementary Pairs",
                    "desc": "Two conclusions where both cannot be true together and both cannot be false together.",
                    "examples": [
                        "1. Some cats are dogs. 2. No cat is a dog. (Subject & Predicate same, one +ve one -ve, both doubtful => Either 1 or 2 follows)"
                    ]
                },
                {
                    "name": "5. Negative / Does Not Follow Syllogisms",
                    "desc": "Identifying which conclusion definitively FAILS or cannot hold under any interpretation.",
                    "examples": [
                        "Testing which statement violates the minimum overlapping Venn boundary"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "'Only a Few' Dual-Statement Rule",
                    "explanation": "The quantifier 'Only a few $A$ are $B$' contains TWO simultaneous premises:\n(1) **Some $A$ are $B$** (Positive overlap)\n(2) **Some $A$ are NOT $B$** (Definite negative exclusion).\nTherefore: The conclusion 'All $A$ can be $B$' is ALWAYS FALSE, while 'All $B$ can be $A$' is a valid possibility.",
                    "words": [
                        "Only a Few = Some + Some Not",
                        "All A can be B is FALSE"
                    ],
                    "correct": "Given 'Only a few cats are dogs': 'All dogs being cats is a possibility' is TRUE; 'All cats being dogs is a possibility' is FALSE.",
                    "incorrect": "Treating 'Only a few' as identical to regular 'Some'."
                },
                {
                    "rule_number": 2,
                    "title": "Either-Or Three Golden Conditions",
                    "explanation": "Either-Or applies between Conclusion 1 and Conclusion 2 if and only if:\n1. Both individual conclusions are **Indeterminate / Doubtful** (cannot be definitely proved from premises).\n2. They share the **identical Subject and Predicate**.\n3. They form a valid **Complementary Pair**: (Some + No) or (All + Some Not).\n*(Note: All + No is NOT an either-or pair!)*",
                    "words": [
                        "Either-Or Rule",
                        "Some + No",
                        "All + Some Not",
                        "Both Doubtful"
                    ],
                    "correct": "1. Some P are Q (Doubtful). 2. No P is Q (Doubtful). Result: Either 1 or 2 follows.",
                    "incorrect": "Applying Either-Or to 'All P are Q' and 'No P is Q' (both can be false simultaneously)."
                },
                {
                    "rule_number": 3,
                    "title": "Possibility Validity Rule",
                    "explanation": "A conclusion stating '$X$ being $Y$ is a possibility' is **TRUE** if there is no direct contradiction in the premises. However:\n- If a statement is ALREADY definitely true, its possibility is technically redundant/false in modern banking logic.\n- If a statement is definitely impossible (violates a 'No' rule), its possibility is FALSE.",
                    "words": [
                        "Possibility Rule",
                        "No Contradiction",
                        "Can Be True"
                    ],
                    "correct": "If Some A are B: 'All A being B is a possibility' is TRUE.",
                    "incorrect": "If No A is B: Claiming 'Some A being B is a possibility'."
                },
                {
                    "rule_number": 4,
                    "title": "Universal Negative Definitive Boundary Rule",
                    "explanation": "If 'No $A$ is $B$', then no part of circle $A$ can ever intersect with circle $B$. Furthermore, if 'All $C$ are $A$', then automatically 'No $C$ is $B$'.",
                    "words": [
                        "No A is B",
                        "Restricted Zone",
                        "Inherited Negation"
                    ],
                    "correct": "Statements: All cars are vehicles. No vehicle is a boat. Conclusion: No car is a boat (Definitively True).",
                    "incorrect": "Assuming cars could possibly intersect with boats."
                },
                {
                    "rule_number": 5,
                    "title": "Disregard Real-World Empirical Truth Rule",
                    "explanation": "You must accept the premises as 100% indisputable facts, even if they contradict known physical reality (e.g., 'All dogs are trees'). Never reject a conclusion because it sounds absurd in real life.",
                    "words": [
                        "Strict Formalism",
                        "Ignore Real World",
                        "Abstract Logic"
                    ],
                    "correct": "All cats are chairs. All chairs are tables => All cats are tables (Valid logical conclusion).",
                    "incorrect": "Rejecting the conclusion because cats cannot be tables in real life."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Treating 'Only a few A are B' as simple 'Some A are B'.",
                    "correction": "Remember that 'Only a few' mandates that some A are strictly excluded from B.",
                    "rationale": "'All A being B' is completely impossible under 'Only a few'."
                },
                {
                    "mistake": "Selecting Either-Or for 'All A are B' and 'No A is B'.",
                    "correction": "All + No is contrary, not contradictory (both can be false). Valid pairs are (Some + No) and (All + Some Not).",
                    "rationale": "Classical formal logic rule."
                },
                {
                    "mistake": "Assuming two 'Some' premises yield a definite conclusion.",
                    "correction": "Some + Some = No Definite Conclusion (only possibility conclusions can hold).",
                    "rationale": "Venn circles may or may not overlap."
                },
                {
                    "mistake": "Allowing common sense or scientific facts to overrule stated premises.",
                    "correction": "Only evaluate formal deductive truth strictly based on the stated statements.",
                    "rationale": "Syllogism tests formal deductive validity, not factual accuracy."
                }
            ],
            "quick_revision_points": [
                "'Only a few A are B' = Some A are B + Some A are NOT B",
                "'Only A are B' = All B are A",
                "Either-Or pairs: (Some + No) or (All + Some Not)",
                "All + No is NEVER an Either-Or pair",
                "Some + Some gives NO definite conclusion",
                "No + No gives NO definite conclusion",
                "If a conclusion is already definitely true, it is not just a possibility"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4601,
                "topic_id": 46,
                "exam_id": 1,
                "question": "Statements:\nI. All cups are plates.\nII. Some plates are bowls.\nConclusions:\n1. Some bowls are cups.\n2. All bowls are plates.\n[SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Neither conclusion follows",
                    "Only conclusion 1 follows",
                    "Only conclusion 2 follows",
                    "Both conclusions follow"
                ],
                "correct_answer": "Neither conclusion follows",
                "explanation": "- Cups are inside Plates (All cups are plates).\n- Some Plates are Bowls. The circle of Bowls intersects Plates, but does not necessarily touch Cups.\n- Conclusion 1 (Some bowls are cups): Not necessarily true (uncertain/doubtful).\n- Conclusion 2 (All bowls are plates): Only 'some' plates are bowls, so 'all bowls are plates' cannot be definitively inferred.\nTherefore, neither conclusion follows.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4602,
                "topic_id": 46,
                "exam_id": 1,
                "question": "Statements:\nOnly a few teachers are professors.\nAll professors are researchers.\nConclusions:\nI. All teachers being researchers is a possibility.\nII. All researchers being teachers is a possibility.\n[SBI PO Prelims 2022]",
                "options_json": [
                    "Both I and II follow",
                    "Only I follows",
                    "Only II follows",
                    "Neither follows"
                ],
                "correct_answer": "Both I and II follow",
                "explanation": "- 'Only a few teachers are professors' means: Some teachers are professors AND Some teachers are NOT professors.\n- 'All professors are researchers' means: The entire circle of professors is inside researchers.\n- Can All teachers be inside researchers? YES! Teachers cannot be fully inside professors, but researchers is a bigger circle. So Conclusion I is a valid possibility.\n- Can All researchers be inside teachers? YES, researchers can be placed inside teachers. So Conclusion II is also a valid possibility.\nThus, both I and II follow.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4603,
                "topic_id": 46,
                "exam_id": 1,
                "question": "Statements:\nNo tree is a flower.\nSome flowers are plants.\nConclusions:\nI. Some plants are not trees.\nII. All plants can never be trees.\n[IBPS PO 2022]",
                "options_json": [
                    "Both I and II follow",
                    "Only I follows",
                    "Only II follows",
                    "Neither follows"
                ],
                "correct_answer": "Both I and II follow",
                "explanation": "- Some flowers are plants: The common region between flowers and plants cannot be trees because No tree is a flower.\n- That specific portion of plants which are flowers can NEVER be trees.\n- Therefore, 'Some plants are not trees' is definitely TRUE (Conclusion I follows).\n- Since that portion of plants can never be trees, 'All plants can never be trees' is also definitely TRUE (Conclusion II follows).\nThus, both conclusions follow.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4601,
                "topic_id": 46,
                "question": "Statements: All dogs are cats. All cats are animals. Conclusion: All dogs are animals.",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "Either follows or not"
                ],
                "correct_answer": "Follows",
                "explanation": "Dogs are inside Cats, and Cats are inside Animals. Thus All dogs are Animals follows definitely.",
                "points": 1
            },
            {
                "id": 4602,
                "topic_id": 46,
                "question": "Statements: Some pens are papers. No paper is ink. Conclusion: Some pens are not ink.",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "The portion of pens that are papers can never touch ink. Thus 'Some pens are not ink' definitely follows.",
                "points": 1
            },
            {
                "id": 4603,
                "topic_id": 46,
                "question": "Statements: Some books are pens. Some pens are pencils. Conclusions: 1. Some books are pencils. 2. No book is a pencil.",
                "options_json": [
                    "Either 1 or 2 follows",
                    "Only 1 follows",
                    "Only 2 follows",
                    "Neither follows"
                ],
                "correct_answer": "Either 1 or 2 follows",
                "explanation": "Both individual conclusions are doubtful, have identical subject and predicate, and form a Some + No complementary pair. Thus Either 1 or 2 follows.",
                "points": 1
            },
            {
                "id": 4604,
                "topic_id": 46,
                "question": "What does 'Only a few A are B' imply?",
                "options_json": [
                    "Some A are B and Some A are not B",
                    "All A are B",
                    "No A is B",
                    "Some A are B only"
                ],
                "correct_answer": "Some A are B and Some A are not B",
                "explanation": "'Only a few' is a dual statement meaning Some A are B and simultaneously Some A are not B.",
                "points": 1
            },
            {
                "id": 4605,
                "topic_id": 46,
                "question": "Statements: All cars are bikes. No bike is train. Conclusion: No car is train.",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "Cannot say"
                ],
                "correct_answer": "Follows",
                "explanation": "Since all cars are inside bikes and no bike can touch trains, no car can ever touch trains.",
                "points": 1
            },
            {
                "id": 4606,
                "topic_id": 46,
                "question": "Can 'All A being B is a possibility' be true if 'Only a few A are B'?",
                "options_json": [
                    "No, it is definitely false",
                    "Yes, it is true",
                    "It is doubtful",
                    "Depends on other statements"
                ],
                "correct_answer": "No, it is definitely false",
                "explanation": "Because 'Only a few' requires that some A are definitely NOT B, so All A can never be B.",
                "points": 1
            },
            {
                "id": 4607,
                "topic_id": 46,
                "question": "Statements: Some mangoes are apples. Some apples are bananas. Conclusion: All bananas are mangoes.",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Possibility is false"
                ],
                "correct_answer": "Does not follow",
                "explanation": "No definite universal connection exists between bananas and mangoes.",
                "points": 1
            },
            {
                "id": 4608,
                "topic_id": 46,
                "question": "Which of the following is NOT an Either-Or pair?",
                "options_json": [
                    "All + No",
                    "Some + No",
                    "All + Some Not",
                    "None of these"
                ],
                "correct_answer": "All + No",
                "explanation": "All + No is contrary, not contradictory (both statements can be false together), so it cannot form an Either-Or pair.",
                "points": 1
            },
            {
                "id": 4609,
                "topic_id": 46,
                "question": "Statement: Only kings are rich. What is the equivalent universal statement?",
                "options_json": [
                    "All rich are kings",
                    "All kings are rich",
                    "Some kings are rich",
                    "No king is rich"
                ],
                "correct_answer": "All rich are kings",
                "explanation": "'Only A are B' converts to 'All B are A'. Thus 'Only kings are rich' = 'All rich are kings'.",
                "points": 1
            },
            {
                "id": 4610,
                "topic_id": 46,
                "question": "Statements: All stars are moons. All moons are planets. Conclusion: Some planets are stars.",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Since all stars are inside planets, some portion of planets is certainly occupied by stars.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4601,
                "topic_id": 46,
                "question": "Statements: All lions are animals. All tigers are animals. Conclusion: All lions are tigers.",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "True",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Both lions and tigers are inside animals, but their circles do not necessarily touch or overlap.",
                "points": 1
            },
            {
                "id": 4602,
                "topic_id": 46,
                "question": "What is the complementary pair to 'Some A are B' for Either-Or?",
                "options_json": [
                    "No A is B",
                    "All A are B",
                    "Some A are not B",
                    "All B are A"
                ],
                "correct_answer": "No A is B",
                "explanation": "Some + No is the classic complementary pair.",
                "points": 1
            },
            {
                "id": 4603,
                "topic_id": 46,
                "question": "Statements: No dog is a cat. No cat is a mouse. Can we conclude: No dog is a mouse?",
                "options_json": [
                    "No, it does not follow",
                    "Yes, it follows definitely",
                    "Yes, by transitivity",
                    "Always true"
                ],
                "correct_answer": "No, it does not follow",
                "explanation": "Two negative statements yield no definite logical relation between the outer terms.",
                "points": 1
            },
            {
                "id": 4604,
                "topic_id": 46,
                "question": "If 'Some A are B' is given, is 'All B being A is a possibility' true?",
                "options_json": [
                    "Yes",
                    "No",
                    "Cannot be determined",
                    "False"
                ],
                "correct_answer": "Yes",
                "explanation": "Venn circle B can be completely inside circle A without violating 'Some A are B'.",
                "points": 1
            },
            {
                "id": 4605,
                "topic_id": 46,
                "question": "Statements: All pens are blue. Some blue are caps. Conclusion: Some pens are caps.",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definite true",
                    "Cannot say"
                ],
                "correct_answer": "Does not follow",
                "explanation": "The caps circle may only intersect the blue area outside pens.",
                "points": 1
            },
            {
                "id": 4606,
                "topic_id": 46,
                "question": "Under 'Only a few men are doctors', can 'All doctors being men' be a possibility?",
                "options_json": [
                    "Yes",
                    "No",
                    "Never",
                    "Contradictory"
                ],
                "correct_answer": "Yes",
                "explanation": "Yes, all doctors can be men, as long as some men are still outside the doctor circle.",
                "points": 1
            },
            {
                "id": 4607,
                "topic_id": 46,
                "question": "In Syllogism, should conclusions be evaluated based on real-world facts or given premises?",
                "options_json": [
                    "Strictly given premises",
                    "Real-world scientific facts",
                    "Combination of both",
                    "Personal intuition"
                ],
                "correct_answer": "Strictly given premises",
                "explanation": "Syllogism is formal deductive logic evaluated exclusively based on stated premises.",
                "points": 1
            },
            {
                "id": 4608,
                "topic_id": 46,
                "question": "Statements: All roses are flowers. All flowers are plants. Conclusion: All roses are plants.",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Roses are inside flowers, flowers are inside plants => Roses are inside plants.",
                "points": 1
            },
            {
                "id": 4609,
                "topic_id": 46,
                "question": "If 'No A is B' is stated, can 'Some A being B is a possibility' ever be true?",
                "options_json": [
                    "No, impossible",
                    "Yes, always",
                    "Sometimes",
                    "Doubtful"
                ],
                "correct_answer": "No, impossible",
                "explanation": "A direct universal negative rules out any possibility of intersection.",
                "points": 1
            },
            {
                "id": 4610,
                "topic_id": 46,
                "question": "Statement: 'At least some boys are students'. How is this interpreted?",
                "options_json": [
                    "Some boys are students",
                    "All boys are students",
                    "Only a few boys are students",
                    "No boy is a student"
                ],
                "correct_answer": "Some boys are students",
                "explanation": "'At least some' is semantically identical to standard 'Some'.",
                "points": 1
            }
        ]
    },
    "47": {
        "title": "Venn Diagrams: Three-Entity Sets, Geometrical Regions & Set-Theoretic Deductions",
        "source_id": 7,
        "content": {
            "definition": "Venn Diagrams represent logical and set-theoretic relationships among classes or finite groups using enclosed plane figures (circles, squares, triangles, rectangles). Prominent across SSC CGL, RRB NTPC, State PSCs, and Defence exams, questions require mapping conceptual entity hierarchies (e.g. Earth, Asia, India) into representative topological figures, as well as reading multi-figure intersections to compute exact numerical populations ($n(A \\cup B \\cup C)$).",
            "overview": "Essential Venn Archetypes & Set Formulas:\n- Inclusive Subsets (Nested Circles): $A \\subset B \\subset C$ (e.g., Seconds $\\subset$ Minutes $\\subset$ Hours)\n- Mutually Exclusive / Disjoint Sets: Completely separated circles (e.g., Cat, Dog, Bird)\n- Partial Overlap (Intersection): Some elements shared (e.g., Doctors, Musicians, Teachers)\n- Two-Group Set Formula: $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$\n- Three-Group Set Formula:\n  $n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - [n(A \\cap B) + n(B \\cap C) + n(C \\cap A)] + n(A \\cap B \\cap C)$\n- Geometrical Diagram Analysis: Identifying numbers situated inside a triangle (e.g. Doctors) and square (e.g. Hardworking), but outside circle (e.g. Rural)",
            "types": [
                {
                    "name": "1. Categorical / Taxonomic Class Representation",
                    "desc": "Selecting the correct diagram illustrating relationships among three real-world entities.",
                    "examples": [
                        "Mammals, Cow, Crow (Cow is inside Mammals; Crow is a disjoint bird circle)",
                        "State, Country, Continent (Three concentric nested circles)"
                    ]
                },
                {
                    "name": "2. Intersecting Multi-Professional Sets",
                    "desc": "Three partially overlapping circles depicting overlapping skills or professions.",
                    "examples": [
                        "Authors, Teachers, Women (All three can partially intersect: a woman can be both an author and a teacher)"
                    ]
                },
                {
                    "name": "3. Geometrical Figure Region Identification",
                    "desc": "Reading labels from intersecting geometric shapes (Triangle = Teachers, Circle = Doctors, Rectangle = Rural).",
                    "examples": [
                        "Find the number representing 'Doctors who are neither teachers nor rural'",
                        "Find the number representing 'Rural teachers who are also doctors'"
                    ]
                },
                {
                    "name": "4. Set-Theoretic Arithmetic Equations",
                    "desc": "Calculating 'Only A', 'Only B', or 'All three' given total demographic survey figures.",
                    "examples": [
                        "In a class of 100: 60 play Cricket, 50 play Football, 20 play both. How many play neither?",
                        "Formula: 100 - (60 + 50 - 20) = 100 - 90 = 10"
                    ]
                },
                {
                    "name": "5. Two Enclosed and One Separated Group",
                    "desc": "Two categories possessing an overlap while both being completely disjoint from a third.",
                    "examples": [
                        "Dogs, Pets, Tables (Dogs and Pets overlap; Tables is completely separate)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Concentric Containment Rule",
                    "explanation": "If entity $A$ is a strict subset of $B$ and $B$ is a strict subset of $C$ ($A \\subset B \\subset C$), the diagram MUST be three concentric nested circles.",
                    "words": [
                        "Concentric Circles",
                        "Strict Containment",
                        "Nested"
                    ],
                    "correct": "Seconds, Minutes, Hours: Seconds are inside Minutes, which are inside Hours.",
                    "incorrect": "Drawing three partially overlapping circles."
                },
                {
                    "rule_number": 2,
                    "title": "Universal Disjoint Separation Rule",
                    "explanation": "If no member of entity $A$ can ever be a member of $B$ or $C$, and no members are shared among any pairs, the diagram MUST consist of three mutually separated, non-touching circles.",
                    "words": [
                        "Mutually Disjoint",
                        "Zero Overlap",
                        "Separate Circles"
                    ],
                    "correct": "Chair, Table, Bed (All three are distinct pieces of furniture with zero common elements).",
                    "incorrect": "Intersecting chair and table."
                },
                {
                    "rule_number": 3,
                    "title": "'Only' Region Isolation Rule in Geometric Venn",
                    "explanation": "When asked for 'Only category $A$', look exclusively inside the region bounded by shape $A$ that does NOT intersect with ANY other geometric boundary.",
                    "words": [
                        "Only Region",
                        "Pure Shape",
                        "Exclude Other Boundaries"
                    ],
                    "correct": "In Circle (Athletes) and Triangle (Scholars): 'Only Athletes' is the crescent of the circle outside the triangle.",
                    "incorrect": "Including the intersection region."
                },
                {
                    "rule_number": 4,
                    "title": "Two-Set Union Calculation Rule",
                    "explanation": "To find the number of people belonging to at least one of two groups: $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$. People belonging to 'Neither' = $\\text{Total} - n(A \\cup B)$.",
                    "words": [
                        "Two Set Formula",
                        "Subtract Intersection",
                        "Neither Count"
                    ],
                    "correct": "In a group of 50: 30 like tea, 25 like coffee, 10 like both. Neither = 50 - (30 + 25 - 10) = 50 - 45 = 5.",
                    "incorrect": "Subtracting 30 + 25 directly from 50 (yielding negative number)."
                },
                {
                    "rule_number": 5,
                    "title": "Cross-Professional Compatibility Check",
                    "explanation": "When evaluating entities like 'Doctors, Engineers, Writers, Women': Ask 'Can a Woman be a Doctor?' (Yes). 'Can a Doctor be a Writer?' (Yes). If all pairs can coexist, use three mutually intersecting circles.",
                    "words": [
                        "Compatibility Test",
                        "Mutual Intersection",
                        "Universal Tri-Overlap"
                    ],
                    "correct": "Men, Doctors, Authors: Three partially overlapping circles with a common central triple intersection.",
                    "incorrect": "Drawing them as isolated circles."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Drawing partially overlapping circles for concentric hierarchical categories.",
                    "correction": "Biological/geographical subsets (e.g., India, Asia, Earth) are nested concentric circles, not overlapping.",
                    "rationale": "Every Indian is an Asian, so the entire India circle must sit inside Asia."
                },
                {
                    "mistake": "Double counting the central triple intersection in demographic surveys.",
                    "correction": "Use $n(A \\cup B \\cup C) = \\sum n(A) - \\sum n(A \\cap B) + n(A \\cap B \\cap C)$.",
                    "rationale": "The triple overlap is subtracted three times in pairwise subtractions, so it must be added back once."
                },
                {
                    "mistake": "Confusing 'Doctors who are Teachers' with 'ONLY Doctors who are Teachers'.",
                    "correction": "'Doctors who are Teachers' includes those who might also be Rural, unless 'Only' or 'Neither' is stated.",
                    "rationale": "Failure to notice the omission of 'Only' leads to picking the wrong numerical region."
                },
                {
                    "mistake": "Assuming all animals can be pets.",
                    "correction": "Pet overlaps with Dog and Cat, but is completely disjoint from Wild animals like Tiger.",
                    "rationale": "Realistic taxonomical classification."
                }
            ],
            "quick_revision_points": [
                "Concentric circles = Subsets (India in Asia in World)",
                "Disjoint circles = Mutually exclusive categories (Doctor, Lawyer, Engineer)",
                "3 partially overlapping circles = Entities with mutual compatibility (Women, Teachers, Authors)",
                "Two sets: n(A or B) = n(A) + n(B) - n(A and B)",
                "Neither = Total - n(A or B)",
                "In geometric diagrams: 'Only' means strictly inside one shape, outside all others",
                "'Both A and B' means the intersection of shapes A and B"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4701,
                "topic_id": 47,
                "exam_id": 1,
                "question": "Which of the following Venn diagrams best represents the relationship between: 'Factory, Machinery, Product'? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Two separate circles inside a large circle",
                    "Three concentric circles",
                    "Three intersecting circles",
                    "Three completely disjoint circles"
                ],
                "correct_answer": "Two separate circles inside a large circle",
                "explanation": "Machinery and Product are both found inside a Factory, but Machinery (equipment) and Product (output) are completely distinct categories from each other.\nTherefore, the correct diagram shows two separate circles (Machinery, Product) both enclosed inside a large circle (Factory).",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4702,
                "topic_id": 47,
                "exam_id": 1,
                "question": "In a group of 80 students, 45 like cricket, 35 like football, and 15 like both. How many students like neither cricket nor football? [RRB NTPC 2022]",
                "options_json": [
                    "15",
                    "10",
                    "20",
                    "25"
                ],
                "correct_answer": "15",
                "explanation": "Total students = 80.\nn(Cricket) = 45, n(Football) = 35, n(Both) = 15.\nStudents who like at least one game = n(Cricket U Football) = 45 + 35 - 15 = 65.\nStudents who like neither = Total - 65 = 80 - 65 = 15.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4703,
                "topic_id": 47,
                "exam_id": 1,
                "question": "Which diagram correctly represents: 'Reptile, Snake, Lizard'? [SSC CHSL 2022]",
                "options_json": [
                    "Two separate circles inside a large circle",
                    "Three concentric circles",
                    "Three intersecting circles",
                    "Three separate circles"
                ],
                "correct_answer": "Two separate circles inside a large circle",
                "explanation": "Both Snake and Lizard belong to the class Reptilia (Reptiles), but Snake and Lizard are distinct organisms with zero overlap.\nTherefore, they are two separate circles inside the large Reptile circle.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4701,
                "topic_id": 47,
                "question": "Which diagram represents: 'Earth, Sea, Sun'?",
                "options_json": [
                    "Sea is inside Earth, Sun is separate",
                    "Three concentric circles",
                    "Three separate circles",
                    "Three intersecting circles"
                ],
                "correct_answer": "Sea is inside Earth, Sun is separate",
                "explanation": "Sea is entirely on Earth (circle inside circle), while Sun is an independent celestial star completely separate.",
                "points": 1
            },
            {
                "id": 4702,
                "topic_id": 47,
                "question": "In a survey of 50 people, 30 drink tea, 25 drink coffee, and 10 drink both. How many drink neither?",
                "options_json": [
                    "5",
                    "10",
                    "15",
                    "0"
                ],
                "correct_answer": "5",
                "explanation": "Total = 50. Union = 30 + 25 - 10 = 45. Neither = 50 - 45 = 5.",
                "points": 1
            },
            {
                "id": 4703,
                "topic_id": 47,
                "question": "Which diagram represents: 'Seconds, Minutes, Hours'?",
                "options_json": [
                    "Three concentric circles",
                    "Three separate circles",
                    "Three intersecting circles",
                    "Two inside one"
                ],
                "correct_answer": "Three concentric circles",
                "explanation": "Seconds are within Minutes, and Minutes are within Hours: three nested concentric circles.",
                "points": 1
            },
            {
                "id": 4704,
                "topic_id": 47,
                "question": "Which diagram represents: 'Women, Mothers, Doctors'?",
                "options_json": [
                    "Mothers inside Women, Doctors intersecting both",
                    "Three concentric circles",
                    "Three disjoint circles",
                    "Two separate circles inside one"
                ],
                "correct_answer": "Mothers inside Women, Doctors intersecting both",
                "explanation": "All Mothers are Women (Mothers circle inside Women). Some Women and some Mothers are Doctors (Doctors circle partially intersects both).",
                "points": 1
            },
            {
                "id": 4705,
                "topic_id": 47,
                "question": "In a club of 100 members, 60 play chess, 50 play carrom, and 20 play both. How many play ONLY chess?",
                "options_json": [
                    "40",
                    "50",
                    "30",
                    "20"
                ],
                "correct_answer": "40",
                "explanation": "Only chess = Total chess - Both = 60 - 20 = 40.",
                "points": 1
            },
            {
                "id": 4706,
                "topic_id": 47,
                "question": "Which diagram represents: 'Dog, Pet, Cat'?",
                "options_json": [
                    "Dog and Cat are separate circles intersecting Pet",
                    "Three separate circles",
                    "Two inside one",
                    "Three concentric circles"
                ],
                "correct_answer": "Dog and Cat are separate circles intersecting Pet",
                "explanation": "Some dogs are pets, some cats are pets, but dogs and cats do not overlap with each other.",
                "points": 1
            },
            {
                "id": 4707,
                "topic_id": 47,
                "question": "Which diagram represents: 'India, Asia, Europe'?",
                "options_json": [
                    "India inside Asia, Europe separate",
                    "Three concentric circles",
                    "Three intersecting circles",
                    "All three separate"
                ],
                "correct_answer": "India inside Asia, Europe separate",
                "explanation": "India is in Asia (nested). Europe is a completely separate continent.",
                "points": 1
            },
            {
                "id": 4708,
                "topic_id": 47,
                "question": "In a class of 60: 35 pass Math, 30 pass Science, 15 pass both. How many fail both?",
                "options_json": [
                    "10",
                    "15",
                    "5",
                    "20"
                ],
                "correct_answer": "10",
                "explanation": "Pass at least one = 35 + 30 - 15 = 50. Fail both = 60 - 50 = 10.",
                "points": 1
            },
            {
                "id": 4709,
                "topic_id": 47,
                "question": "Which diagram represents: 'Sparrow, Bird, Mouse'?",
                "options_json": [
                    "Sparrow inside Bird, Mouse separate",
                    "Three separate circles",
                    "Two intersecting circles inside one",
                    "Three concentric circles"
                ],
                "correct_answer": "Sparrow inside Bird, Mouse separate",
                "explanation": "Sparrow is a Bird (nested). Mouse is a mammal and completely separate.",
                "points": 1
            },
            {
                "id": 4710,
                "topic_id": 47,
                "question": "In a geometric Venn diagram, Triangle is Artists, Circle is Doctors, Square is Singers. What represents 'Doctors who are both Artists and Singers'?",
                "options_json": [
                    "The region common to Triangle, Circle, and Square",
                    "Only Circle",
                    "Intersection of Triangle and Square only",
                    "Outside all shapes"
                ],
                "correct_answer": "The region common to Triangle, Circle, and Square",
                "explanation": "Belonging to all three categories corresponds to the central triple intersection of all three shapes.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4701,
                "topic_id": 47,
                "question": "Which diagram represents: 'Father, Brother, Male'?",
                "options_json": [
                    "Father and Brother overlap, both inside Male",
                    "Three concentric circles",
                    "Three separate circles",
                    "Two separate inside one"
                ],
                "correct_answer": "Father and Brother overlap, both inside Male",
                "explanation": "All fathers and all brothers are male (inside Male). A father can also be a brother (they overlap).",
                "points": 1
            },
            {
                "id": 4702,
                "topic_id": 47,
                "question": "In a group of 50 students, 20 like English, 30 like Hindi, and 5 like both. How many like neither?",
                "options_json": [
                    "5",
                    "10",
                    "15",
                    "0"
                ],
                "correct_answer": "5",
                "explanation": "Union = 20 + 30 - 5 = 45. Neither = 50 - 45 = 5.",
                "points": 1
            },
            {
                "id": 4703,
                "topic_id": 47,
                "question": "Which diagram best represents: 'Mammal, Bat, Pigeon'?",
                "options_json": [
                    "Bat inside Mammal, Pigeon separate",
                    "Both inside Mammal",
                    "Three separate circles",
                    "Three concentric circles"
                ],
                "correct_answer": "Bat inside Mammal, Pigeon separate",
                "explanation": "Bat is a mammal (enclosed). Pigeon is a bird (disjoint circle).",
                "points": 1
            },
            {
                "id": 4704,
                "topic_id": 47,
                "question": "Which diagram best represents: 'Table, Chair, Furniture'?",
                "options_json": [
                    "Table and Chair are separate circles inside Furniture",
                    "Three concentric circles",
                    "Three intersecting circles",
                    "Three disjoint circles"
                ],
                "correct_answer": "Table and Chair are separate circles inside Furniture",
                "explanation": "Both Table and Chair are furniture, but Table and Chair are distinct items.",
                "points": 1
            },
            {
                "id": 4705,
                "topic_id": 47,
                "question": "In a class of 40: 25 play Tennis, 20 play Cricket, 10 play both. How many play ONLY Tennis?",
                "options_json": [
                    "15",
                    "25",
                    "10",
                    "20"
                ],
                "correct_answer": "15",
                "explanation": "Only Tennis = Total Tennis - Both = 25 - 10 = 15.",
                "points": 1
            },
            {
                "id": 4706,
                "topic_id": 47,
                "question": "Which diagram represents: 'Vegetable, Potato, Cabbage'?",
                "options_json": [
                    "Potato and Cabbage separate inside Vegetable",
                    "Three concentric circles",
                    "Three disjoint circles",
                    "Three overlapping circles"
                ],
                "correct_answer": "Potato and Cabbage separate inside Vegetable",
                "explanation": "Potato and Cabbage are vegetables, but separate items.",
                "points": 1
            },
            {
                "id": 4707,
                "topic_id": 47,
                "question": "What is the formula for the union of two sets A and B?",
                "options_json": [
                    "n(A) + n(B) - n(A \u2229 B)",
                    "n(A) + n(B)",
                    "n(A) + n(B) + n(A \u2229 B)",
                    "n(A) * n(B)"
                ],
                "correct_answer": "n(A) + n(B) - n(A \u2229 B)",
                "explanation": "Intersection must be subtracted to prevent double counting.",
                "points": 1
            },
            {
                "id": 4708,
                "topic_id": 47,
                "question": "Which diagram represents: 'Gold, Silver, Metal'?",
                "options_json": [
                    "Gold and Silver separate inside Metal",
                    "Three concentric circles",
                    "Three intersecting circles",
                    "Three disjoint circles"
                ],
                "correct_answer": "Gold and Silver separate inside Metal",
                "explanation": "Gold and Silver are both metals, but separate elements.",
                "points": 1
            },
            {
                "id": 4709,
                "topic_id": 47,
                "question": "Which diagram represents: 'Author, Lawyer, Singer'?",
                "options_json": [
                    "Three partially intersecting circles",
                    "Three concentric circles",
                    "Three separate circles",
                    "Two inside one"
                ],
                "correct_answer": "Three partially intersecting circles",
                "explanation": "A person can be an author, lawyer, and singer simultaneously: all three categories can overlap.",
                "points": 1
            },
            {
                "id": 4710,
                "topic_id": 47,
                "question": "In a group of 30, 18 like Apple, 15 like Mango, and 5 like neither. How many like both?",
                "options_json": [
                    "8",
                    "5",
                    "10",
                    "7"
                ],
                "correct_answer": "8",
                "explanation": "Total liking at least one = 30 - 5 = 25. Union formula: 25 = 18 + 15 - Both => 25 = 33 - Both => Both = 8.",
                "points": 1
            }
        ]
    }
}
