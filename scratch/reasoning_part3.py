# reasoning_part3.py
REASONING_PART3_DATA = {
    "48": {
        "title": "Statement and Conclusion: Critical Inferences, Formal Deductions & Argument Validity",
        "source_id": 7,
        "content": {
            "definition": "Statement and Conclusion evaluates verbal critical reasoning where candidates determine whether a proposed conclusion is an inevitable, direct logical consequence of a given premise, or an unwarranted assumption. Prominent in SSC CGL Tier 1/2, IBPS PO, RRB NTPC, and State PSCs, problems demand strict factual adherence to the text, elimination of extreme qualifiers ('always', 'never', 'only'), and distinguishing direct inferences from probabilistic opinions.",
            "overview": "Fundamental Principles of Critical Deduction:\n- The Absolute Text Boundary: Accept the statement as 100% indisputable truth; no external real-world knowledge may override the stated facts\n- Direct Implication vs Independent Assumption: A valid conclusion is an inevitable result of the statement; an assumption is an unstated prerequisite\n- Impact of Extreme Words: Conclusions containing extreme absolutist words ('only', 'all', 'never', 'always', 'everyone') are generally invalid unless the statement explicitly uses identical absolute terms\n- Moderate Expressions: Conclusions containing moderate qualifiers ('many', 'some', 'often', 'can', 'likely') are more likely to be logically sustainable\n- Cause-and-Effect Alignment: Conclusions suggesting an action must directly correlate with the stated dilemma without introducing extraneous external variables",
            "types": [
                {
                    "name": "1. Direct Factual Inferences",
                    "desc": "Conclusions that logically restate or directly synthesize the provided empirical data.",
                    "examples": [
                        "Statement: 'Only students who score above 90% receive scholarship. Anita received a scholarship.' Conclusion: 'Anita scored above 90%.' (Valid / Follows)",
                        "Statement: 'Most employees take the bus.' Conclusion: 'All employees take public transport.' (Invalid / Does not follow)"
                    ]
                },
                {
                    "name": "2. Conditional & If-Then Deductions",
                    "desc": "Evaluating hypothetical scenarios based on causal prerequisites.",
                    "examples": [
                        "Statement: 'If it rains, the cricket match is postponed. Today it rained.' Conclusion: 'The match was postponed.' (Valid)"
                    ]
                },
                {
                    "name": "3. Extreme Qualifier Trap Analysis",
                    "desc": "Testing whether absolutist terms distort a generalized or probabilistic statement.",
                    "examples": [
                        "Statement: 'Morning walks improve physical stamina.' Conclusion: 'Only morning walks can improve stamina.' (Invalid due to 'Only')"
                    ]
                },
                {
                    "name": "4. Comparative & Superlative Deductions",
                    "desc": "Validating comparisons between entities when baseline criteria are or are not given.",
                    "examples": [
                        "Statement: 'Company A increased its revenue by 15% this quarter.' Conclusion: 'Company A is the most profitable company in the sector.' (Invalid superlative)"
                    ]
                },
                {
                    "name": "5. Policy & Governance Cause-Effect",
                    "desc": "Evaluating policy decisions and their direct logical impacts.",
                    "examples": [
                        "Statement: 'Electric vehicle adoption reduces urban particulate emissions.' Conclusion: 'Replacing petrol vehicles with electric reduces urban pollution.' (Valid)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Strict Textual Boundary Rule",
                    "explanation": "Do not bring in outside general knowledge. Even if a conclusion is scientifically or historically true in the real world, if it CANNOT be directly deduced from the given statement, it DOES NOT FOLLOW.",
                    "words": [
                        "No Outside Knowledge",
                        "Strict Boundary",
                        "Textual Evidence"
                    ],
                    "correct": "Statement: 'The moon is made of green cheese.' Conclusion: 'The moon is cheese.' (Follows, based strictly on statement).",
                    "incorrect": "Rejecting the conclusion because the moon is rock in real science."
                },
                {
                    "rule_number": 2,
                    "title": "Extreme Qualifier Disqualification Rule",
                    "explanation": "Conclusions featuring extreme words like 'only', 'all', 'never', 'always', 'completely', 'best', 'sole' almost NEVER follow from a general statement, unless the statement itself uses that exact extreme term.",
                    "words": [
                        "Extreme Words",
                        "Only / All / Never",
                        "Invalidity Trap"
                    ],
                    "correct": "Statement: 'Many people enjoy coffee.' Conclusion: 'Everyone enjoys coffee.' (Does NOT follow due to 'Everyone').",
                    "incorrect": "Accepting 'everyone' when the statement only said 'many'."
                },
                {
                    "rule_number": 3,
                    "title": "Moderate Words Feasibility Rule",
                    "explanation": "Conclusions phrased with moderate words like 'some', 'many', 'often', 'can be', 'may' have a high probability of following if they capture the essence of the premise without over-generalizing.",
                    "words": [
                        "Moderate Qualifiers",
                        "Some / May / Can",
                        "Balanced Inferences"
                    ],
                    "correct": "Statement: 'Regular exercise reduces cardiovascular risk.' Conclusion: 'Some individuals who exercise regularly experience reduced cardiac risk.' (Follows).",
                    "incorrect": "Rejecting moderate conclusions."
                },
                {
                    "rule_number": 4,
                    "title": "One-Way Implication Non-Reversibility Rule",
                    "explanation": "If statement asserts $P \\implies Q$, it does NOT mean $Q \\implies P$. (e.g., 'All doctors study medicine' does not mean 'Everyone who studies medicine is a doctor').",
                    "words": [
                        "Non-Reversibility",
                        "P implies Q != Q implies P",
                        "Converse Error"
                    ],
                    "correct": "Statement: 'Severe storms cause power outages.' Outage occurs. Conclusion: 'A severe storm must have occurred.' (Does NOT follow: outage could have other causes).",
                    "incorrect": "Assuming reverse causation."
                },
                {
                    "rule_number": 5,
                    "title": "Assumption vs Conclusion Separation Rule",
                    "explanation": "A conclusion comes AFTER the statement (a consequence or deduction). An assumption comes BEFORE the statement (a presupposition that prompted the speaker). Do not confuse an assumption with a conclusion.",
                    "words": [
                        "Conclusion = Consequence",
                        "Assumption = Premise",
                        "Chronology"
                    ],
                    "correct": "Identifying that a valid conclusion must flow downward from the premise.",
                    "incorrect": "Selecting a background presupposition as a conclusion."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Importing outside general knowledge or personal moral opinions.",
                    "correction": "Evaluate conclusions strictly within the four corners of the provided text.",
                    "rationale": "Examiners specifically design statements that challenge intuitive real-world assumptions."
                },
                {
                    "mistake": "Accepting conclusions with extreme words like 'only' or 'always'.",
                    "correction": "Watch for words like 'only', 'all', 'never'. They immediately flag an over-generalized conclusion.",
                    "rationale": "Extreme words are the single most reliable marker of an invalid inference."
                },
                {
                    "mistake": "Treating a probable possibility as an inevitable definite conclusion.",
                    "correction": "A conclusion must be 100% inevitable. If it 'might' be true but isn't guaranteed, it does not follow.",
                    "rationale": "Competitive tests demand definite logical consequence."
                },
                {
                    "mistake": "Committing the converse error ($P \\implies Q \\implies Q \\implies P$).",
                    "correction": "Remember that effect does not guarantee one specific cause if alternatives exist.",
                    "rationale": "Classic formal logic fallacy."
                }
            ],
            "quick_revision_points": [
                "Stick strictly to the statement: zero outside knowledge allowed",
                "Extreme words ('only', 'all', 'never', 'always') almost always make a conclusion invalid",
                "Moderate words ('some', 'often', 'can be') usually signal valid conclusions",
                "P implies Q does NOT mean Q implies P (do not commit converse error)",
                "A conclusion must be 100% inevitable, not just a plausible possibility",
                "Never assume causality where only correlation is mentioned",
                "Distinguish: Assumption comes before statement; Conclusion follows after statement"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4801,
                "topic_id": 48,
                "exam_id": 1,
                "question": "Statement: 'In a one-day cricket match, the total runs scored by a team were 200. Out of these, 160 runs were scored by spinners.'\nConclusions:\nI. 80% of the team consists of spinners.\nII. The opening batsmen were spinners.\n[SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Neither I nor II follows",
                    "Only I follows",
                    "Only II follows",
                    "Both I and II follow"
                ],
                "correct_answer": "Neither I nor II follows",
                "explanation": "- Conclusion I: Just because 160/200 = 80% of the runs were scored by spinners does NOT mean 80% of the players in the team are spinners (a single spinner could have scored 160 runs). So I does not follow.\n- Conclusion II: The statement says nothing about which batting position the spinners played. So II does not follow.\nTherefore, neither I nor II follows.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4802,
                "topic_id": 48,
                "exam_id": 1,
                "question": "Statement: 'The national norm is 100 beds per 1,000 population, but in State X, only 65 beds per 1,000 population are available in government hospitals.'\nConclusions:\nI. The healthcare system in State X is inadequate compared to the national norm.\nII. The state government should allocate more funds to build hospital beds.\n[IBPS PO 2022]",
                "options_json": [
                    "Only conclusion I follows",
                    "Only conclusion II follows",
                    "Both I and II follow",
                    "Neither follows"
                ],
                "correct_answer": "Only conclusion I follows",
                "explanation": "- Conclusion I directly follows: 65 beds is less than the national benchmark of 100 beds, meaning it is inadequate compared to the norm.\n- Conclusion II is a 'Course of Action' or recommendation, rather than a factual logical deduction/conclusion directly implied by the statement itself.\nTherefore, only conclusion I follows.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4803,
                "topic_id": 48,
                "exam_id": 1,
                "question": "Statement: 'Government has decided to levy a 2% cess on the tax payable for building flood relief funds.'\nConclusions:\nI. The government needs additional financial resources for flood relief operations.\nII. People are willing to pay the 2% cess without objection.\n[RRB NTPC 2022]",
                "options_json": [
                    "Only conclusion I follows",
                    "Only conclusion II follows",
                    "Both I and II follow",
                    "Neither follows"
                ],
                "correct_answer": "Only conclusion I follows",
                "explanation": "- Conclusion I follows directly: The stated purpose of levying the cess is explicitly 'for building flood relief funds', proving the government requires additional funds for this purpose.\n- Conclusion II does not follow: The statement describes a government decision; it gives no information about public willingness or objections.\nTherefore, only conclusion I follows.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4801,
                "topic_id": 48,
                "question": "Statement: 'Most students in class X passed the examination.' Conclusion: 'Some students in class X failed the examination.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "'Most' means more than 50% but not all (not 100%). This logically implies that some students did not pass (failed).",
                "points": 1
            },
            {
                "id": 4802,
                "topic_id": 48,
                "question": "Statement: 'All successful business owners work long hours.' Conclusion: 'Everyone who works long hours is a successful business owner.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Converse error: All A are B does not mean all B are A. Working long hours does not guarantee successful business ownership.",
                "points": 1
            },
            {
                "id": 4803,
                "topic_id": 48,
                "question": "Statement: 'Smoking is injurious to health.' Conclusion: 'All non-smokers are healthy.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "True",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Smoking causes harm, but other diseases or factors can still affect non-smokers. 'All non-smokers are healthy' does not follow.",
                "points": 1
            },
            {
                "id": 4804,
                "topic_id": 48,
                "question": "Statement: 'Electric vehicles produce zero tailpipe emissions.' Conclusion: 'Adopting electric vehicles helps reduce local vehicle exhaust emissions.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Direct logical deduction from the statement: zero tailpipe emissions directly reduces exhaust pollution.",
                "points": 1
            },
            {
                "id": 4805,
                "topic_id": 48,
                "question": "Statement: 'Only candidates with a master's degree can apply for the post. Suresh applied for the post.' Conclusion: 'Suresh has a master's degree.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Since having a master's degree is the mandatory prerequisite to apply, Suresh must possess a master's degree.",
                "points": 1
            },
            {
                "id": 4806,
                "topic_id": 48,
                "question": "Statement: 'Sunlight is essential for plant photosynthesis.' Conclusion: 'Plants cannot perform photosynthesis without sunlight.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "'Essential' means strictly necessary. Without it, the process cannot occur.",
                "points": 1
            },
            {
                "id": 4807,
                "topic_id": 48,
                "question": "Statement: 'Company XYZ increased its marketing budget by 40%.' Conclusion: 'Company XYZ will become the market leader.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Increasing marketing budget does not automatically guarantee achieving market leadership.",
                "points": 1
            },
            {
                "id": 4808,
                "topic_id": 48,
                "question": "Statement: 'Regular exercise improves cardiovascular fitness.' Conclusion: 'Only exercise can improve cardiovascular fitness.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "True",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "The word 'Only' is an extreme qualifier not supported by the premise (diet and medication may also play roles).",
                "points": 1
            },
            {
                "id": 4809,
                "topic_id": 48,
                "question": "Statement: 'Heavy rains caused urban flooding in the city.' Conclusion: 'The city experienced heavy rainfall.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Direct factual deduction: the statement explicitly asserts that heavy rains occurred.",
                "points": 1
            },
            {
                "id": 4810,
                "topic_id": 48,
                "question": "Statement: 'All members of the committee voted in favor of the resolution.' Conclusion: 'The resolution was passed unanimously.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "When all members vote in favor, the decision is by definition unanimous.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4801,
                "topic_id": 48,
                "question": "Statement: 'The price of petroleum products rose by 10%.' Conclusion: 'All goods and services became 10% more expensive.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Petroleum price rise does not mean every good and service automatically increases by 10%.",
                "points": 1
            },
            {
                "id": 4802,
                "topic_id": 48,
                "question": "What is the general effect of extreme words like 'only', 'all', and 'never' on conclusions?",
                "options_json": [
                    "They usually make the conclusion invalid",
                    "They make the conclusion definitively true",
                    "They have no effect",
                    "They prove causality"
                ],
                "correct_answer": "They usually make the conclusion invalid",
                "explanation": "Extreme words over-generalize beyond what the premise stated.",
                "points": 1
            },
            {
                "id": 4803,
                "topic_id": 48,
                "question": "Statement: 'No student who failed the midterm can attend the field trip. Ravi attended the field trip.' Conclusion: 'Ravi did not fail the midterm.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "By contrapositive: If fail -> cannot attend. Ravi attended -> Ravi did not fail.",
                "points": 1
            },
            {
                "id": 4804,
                "topic_id": 48,
                "question": "Statement: 'A healthy diet reduces the risk of chronic illnesses.' Conclusion: 'Eating healthy eliminates all health risks.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Probable"
                ],
                "correct_answer": "Does not follow",
                "explanation": "'Reduces risk' does not mean 'eliminates all risks'.",
                "points": 1
            },
            {
                "id": 4805,
                "topic_id": 48,
                "question": "Statement: 'Many tech companies are investing in AI.' Conclusion: 'Some tech companies are investing in AI.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "'Many' mathematically implies that at least 'some' (more than a few) are investing.",
                "points": 1
            },
            {
                "id": 4806,
                "topic_id": 48,
                "question": "Can external real-world facts override the stated premises in Statement-Conclusion questions?",
                "options_json": [
                    "No, never",
                    "Yes, always",
                    "Only in science questions",
                    "Only in historical questions"
                ],
                "correct_answer": "No, never",
                "explanation": "The stated text is the sole source of factual truth.",
                "points": 1
            },
            {
                "id": 4807,
                "topic_id": 48,
                "question": "Statement: 'Company profits increased by 25% this year.' Conclusion: 'Company revenue also increased.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Certain"
                ],
                "correct_answer": "Does not follow",
                "explanation": "Profit = Revenue - Cost. Profit can increase even if revenue is flat, by cutting costs.",
                "points": 1
            },
            {
                "id": 4808,
                "topic_id": 48,
                "question": "Statement: 'All participants who completed the marathon received a medal. John received a medal.' Conclusion: 'John completed the marathon.'",
                "options_json": [
                    "Does not follow",
                    "Follows",
                    "Definitely true",
                    "Certain"
                ],
                "correct_answer": "Does not follow",
                "explanation": "The statement says finishers receive medals, but does not say ONLY finishers receive medals (volunteers or organizers might also receive medals).",
                "points": 1
            },
            {
                "id": 4809,
                "topic_id": 48,
                "question": "Statement: 'Water boils at 100\u00b0C at sea level.' Conclusion: 'Water at sea level heated to 100\u00b0C will boil.'",
                "options_json": [
                    "Follows",
                    "Does not follow",
                    "Doubtful",
                    "False"
                ],
                "correct_answer": "Follows",
                "explanation": "Direct logical consequence of the definition.",
                "points": 1
            },
            {
                "id": 4810,
                "topic_id": 48,
                "question": "What is the difference between an Assumption and a Conclusion?",
                "options_json": [
                    "Assumption comes before the statement; Conclusion follows from it",
                    "They are identical",
                    "Conclusion comes before; Assumption comes after",
                    "Assumptions are always false"
                ],
                "correct_answer": "Assumption comes before the statement; Conclusion follows from it",
                "explanation": "An assumption is an unstated prerequisite; a conclusion is a direct consequence.",
                "points": 1
            }
        ]
    },
    "49": {
        "title": "Puzzles: Multi-Floor Buildings, Box Stacking, Scheduling & Attribute Matrices",
        "source_id": 7,
        "content": {
            "definition": "Puzzles in reasoning assess the ability to cross-tabulate complex, unstructured conditions across multiple discrete entities (people, floors, professions, cities, colors, months) into unified consistent grid matrices. A dominant component of Bank PO/Clerk (Mains), SSC CGL Tier 2, and CAT, puzzle solving demands systematic case branching (Case 1 vs Case 2), negative constraint filtering, floor-based vertical numbering (Ground floor = 1 to top floor = N), and week/month scheduling.",
            "overview": "Fundamental Puzzle Typologies:\n- Floor & Flat Puzzles: Multi-storey building (Floors 1 to 8 numbered bottom-to-top) often paired with Flats (Flat A West of Flat B)\n- Box Stacking Puzzles: Stack of 7-9 boxes placed one above another with relative gap constraints ('Three boxes between P and Q')\n- Day / Month / Date Scheduling: Events scheduled across days (Monday to Sunday) or months with 30 vs 31 days (January, March, April, etc.)\n- Multi-Variable Attribute Matrix: Matching 6-8 people with their home state, favorite color, and profession using tick/cross grids\n- Comparison / Height / Weight Puzzles: Chaining descending inequalities ($P > Q > R$)",
            "types": [
                {
                    "name": "1. Multi-Storey Floor Puzzles",
                    "desc": "Arranging 7-9 people on floors numbered 1 (bottom) to N (top) with parity (even/odd floor) rules.",
                    "examples": [
                        "A lives on an odd-numbered floor above floor 4 (Floors 5 or 7)",
                        "Two people live between B and C"
                    ]
                },
                {
                    "name": "2. Box Stack Positioning",
                    "desc": "Relative vertical placement of boxes where absolute floor numbers are not predetermined.",
                    "examples": [
                        "Box T is placed immediately above Box R",
                        "As many boxes are above P as below Q"
                    ]
                },
                {
                    "name": "3. Date & Month Scheduling Puzzles",
                    "desc": "Scheduling seminars or interviews on specific dates (e.g., 7th and 14th) across 4 months.",
                    "examples": [
                        "Months with 30 days (April, June, Sept, Nov) vs 31 days (Jan, March, May, July, Aug, Oct, Dec)",
                        "Person attends seminar in a month having 30 days"
                    ]
                },
                {
                    "name": "4. Matrix / Cross-Tabulation Puzzles",
                    "desc": "Matching 3 or 4 attributes per person using systematic elimination tables.",
                    "examples": [
                        "A does not like Red and is not a Doctor",
                        "The engineer wears Green and lives in Mumbai"
                    ]
                },
                {
                    "name": "5. Order & Ranking Comparison Chains",
                    "desc": "Ranking 6 individuals by weight or salary with partial inequality clues.",
                    "examples": [
                        "Only two persons are heavier than M (M is 3rd from top in descending order)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Dual-Case Branching Method",
                    "explanation": "Never get stuck on an ambiguous clue. If a clue allows exactly two valid placements (e.g. 'A lives on floor 3 or floor 7'), immediately draw Case 1 and Case 2 side-by-side. Continue filling clues until one case encounters an explicit contradiction and is eliminated.",
                    "words": [
                        "Case 1 vs Case 2",
                        "Branching",
                        "Eliminate Contradictions"
                    ],
                    "correct": "Creating two parallel grids instantly resolves the puzzle without trial-and-error erasing.",
                    "incorrect": "Guessing one case on scratch paper and having to start over from scratch if it fails."
                },
                {
                    "rule_number": 2,
                    "title": "Floor Numbering Universal Convention",
                    "explanation": "In floor-based puzzles, unless explicitly stated otherwise:\n- Ground floor is ALWAYS Floor 1\n- Floor immediately above is Floor 2\n- Top floor of an 8-floor building is Floor 8\n- 'Three floors between A and B' means $|\\text{Floor}(A) - \\text{Floor}(B)| = 4$.",
                    "words": [
                        "Bottom Floor = 1",
                        "Top Floor = N",
                        "Between Count (|A - B| - 1)"
                    ],
                    "correct": "Two floors between A and B: If A is on floor 1, B is on floor 4 (Floors 2 and 3 are between them).",
                    "incorrect": "Placing B on floor 3 (that is only 1 floor between them)."
                },
                {
                    "rule_number": 3,
                    "title": "'Immediately Above' vs 'Above' Distinction",
                    "explanation": "- '$A$ lives **immediately above** $B$' $\\implies \\text{Floor}(A) = \\text{Floor}(B) + 1$ (Consecutive adjacent floors).\n- '$A$ lives **above** $B$' $\\implies \\text{Floor}(A) > \\text{Floor}(B)$ (Can be any floor above $B$, not necessarily adjacent!).",
                    "words": [
                        "Immediately Above vs Above",
                        "Critical Distinction"
                    ],
                    "correct": "Treating 'above' as an inequality ($A > B$) and 'immediately above' as adjacent ($A = B + 1$).",
                    "incorrect": "Assuming 'above' always means adjacent next door."
                },
                {
                    "rule_number": 4,
                    "title": "Definite Anchor Clues First Rule",
                    "explanation": "Scan the entire puzzle text first to locate DEFINITE ANCHOR clues (e.g., 'A lives on floor 1' or 'The topmost box is Red'). Fix anchor clues first before processing relative or conditional clues.",
                    "words": [
                        "Anchor Clues First",
                        "Fixed Positions",
                        "Sequential Flow"
                    ],
                    "correct": "Placing fixed elements on the grid to create reference points for relative clues.",
                    "incorrect": "Starting with vague clues like 'P lives on an odd floor'."
                },
                {
                    "rule_number": 5,
                    "title": "Symmetry Clue Shortcut ('As many above P as below Q')",
                    "explanation": "The condition 'The number of people above $P$ is equal to the number of people below $Q$' means $P$ and $Q$ occupy symmetric positions from opposite ends:\n$\\text{Floor}(P) + \\text{Floor}(Q) = N + 1$.\nIf $N=8$ and $P$ is on floor 7, then $Q$ is on floor $8 + 1 - 7 = 2$.",
                    "words": [
                        "Symmetry Shortcut",
                        "Floor(P) + Floor(Q) = N + 1",
                        "Rapid Placement"
                    ],
                    "correct": "In an 8-floor building, if P is 2nd from top (floor 7), Q must be 2nd from bottom (floor 2).",
                    "incorrect": "Manually counting floors every single time."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Confusing 'Three floors above' with 'Three floors between'.",
                    "correction": "'Three floors above' = Floor + 3. 'Three floors between' = Floor + 4.",
                    "rationale": "If A is on floor 1, 3 floors between places B on floor 5 (floors 2, 3, 4 are between them)."
                },
                {
                    "mistake": "Erasing and starting over instead of running 2 parallel cases.",
                    "correction": "Always run parallel case grids when a 2-way branch appears.",
                    "rationale": "Saves 50% of puzzle solving time in Bank PO / SSC Tier 2."
                },
                {
                    "mistake": "Ignoring the number of days in months (30 vs 31 days).",
                    "correction": "Know month lengths: April, June, Sept, Nov have 30; Feb has 28/29; others have 31.",
                    "rationale": "Month-scheduling puzzles always use 30 vs 31 days as the primary elimination filter."
                },
                {
                    "mistake": "Misinterpreting 'Only two persons are heavier than X'.",
                    "correction": "This means X is strictly the 3rd heaviest person in the group.",
                    "rationale": "Fixes X's absolute rank in the sequence."
                }
            ],
            "quick_revision_points": [
                "Floor numbering: Floor 1 is bottom, Floor N is top",
                "Between count = |Floor_A - Floor_B| - 1",
                "Immediately above = Floor + 1; Above = any floor greater",
                "Symmetry rule: Floor(P) + Floor(Q) = N + 1",
                "Months with 30 days: April, June, September, November",
                "Run 2 parallel cases whenever an anchor clue has two possibilities",
                "'Only X is taller than Y' means X is 1st (tallest) and Y is 2nd"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4901,
                "topic_id": 49,
                "exam_id": 1,
                "question": "Seven persons A, B, C, D, E, F, G live on seven different floors of a building (floors 1 to 7). E lives on an odd-numbered floor. Only three persons live between E and B. B lives above E. F lives immediately below B. On which floor does F live? [IBPS PO Prelims 2022]",
                "options_json": [
                    "Floor 6",
                    "Floor 5",
                    "Floor 4",
                    "Floor 3"
                ],
                "correct_answer": "Floor 6",
                "explanation": "- Total floors = 7 (1 at bottom, 7 at top).\n- E is on an odd-numbered floor, and B lives above E with exactly 3 persons between them.\n- If E is on Floor 3, 3 persons between means B is on Floor 3 + 4 = 7.\n- If E is on Floor 1, B is on Floor 1 + 4 = 5.\n- If E is on Floor 5, B would be on Floor 9 (impossible, only 7 floors).\n- Clue: 'F lives immediately below B'.\n  - If B is on Floor 7, F is on Floor 6.\n  - If B is on Floor 5, F is on Floor 4.\n- In the standard problem configuration where other clues eliminate B on Floor 5 (e.g., G lives on 4), B is on Floor 7 and F lives on Floor 6.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4902,
                "topic_id": 49,
                "exam_id": 1,
                "question": "Six boxes A, B, C, D, E, F are stacked one above another. Box C is placed immediately above Box D. Only two boxes are placed between Box D and Box A. Box A is placed at the bottom. Which box is on the top? [SSC CGL 2023 Tier 2]",
                "options_json": [
                    "Cannot be determined uniquely without remaining clues",
                    "Box C",
                    "Box B",
                    "Box E"
                ],
                "correct_answer": "Cannot be determined uniquely without remaining clues",
                "explanation": "- Box A is on the bottom (Position 1).\n- Only two boxes are between Box A and Box D => Box D is at Position 1 + 3 = 4.\n- Box C is immediately above Box D => Box C is at Position 5.\n- Positions 2, 3, and 6 (top) are occupied by B, E, and F in some order.\n- Without additional clues for B, E, and F, the topmost box cannot be uniquely determined among B, E, and F.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4903,
                "topic_id": 49,
                "exam_id": 1,
                "question": "Among five friends P, Q, R, S, T each having a different height: P is taller than Q but shorter than T. S is taller than T. R is the shortest. Who is the second tallest? [RRB NTPC 2022]",
                "options_json": [
                    "T",
                    "S",
                    "P",
                    "Q"
                ],
                "correct_answer": "T",
                "explanation": "Analyze the clues:\n1. P is taller than Q: P > Q\n2. P is shorter than T: T > P\n3. S is taller than T: S > T\n4. R is the shortest: R is at the very bottom.\nCombine the complete height order:\nS > T > P > Q > R.\nThe tallest is S.\nThe second tallest is T.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4901,
                "topic_id": 49,
                "question": "In a 7-floor building, which floor is the ground floor?",
                "options_json": [
                    "Floor 1",
                    "Floor 0",
                    "Floor 7",
                    "Basement"
                ],
                "correct_answer": "Floor 1",
                "explanation": "Standard competitive reasoning convention numbers the ground floor as Floor 1.",
                "points": 1
            },
            {
                "id": 4902,
                "topic_id": 49,
                "question": "If 3 persons live between A (Floor 2) and B (living above A), which floor does B live on?",
                "options_json": [
                    "Floor 6",
                    "Floor 5",
                    "Floor 7",
                    "Floor 4"
                ],
                "correct_answer": "Floor 6",
                "explanation": "Floor(B) = Floor(A) + Between + 1 = 2 + 3 + 1 = Floor 6 (floors 3, 4, 5 are between them).",
                "points": 1
            },
            {
                "id": 4903,
                "topic_id": 49,
                "question": "Among 5 friends, A is heavier than B, B is heavier than C, and D is heavier than A. E is the lightest. Who is the heaviest?",
                "options_json": [
                    "D",
                    "A",
                    "B",
                    "C"
                ],
                "correct_answer": "D",
                "explanation": "Order: D > A > B > C > E. The heaviest is D.",
                "points": 1
            },
            {
                "id": 4904,
                "topic_id": 49,
                "question": "In an 8-floor building, if P is on floor 2, which floor has as many floors above it as below P?",
                "options_json": [
                    "Floor 7",
                    "Floor 8",
                    "Floor 6",
                    "Floor 5"
                ],
                "correct_answer": "Floor 7",
                "explanation": "Below floor 2 is 1 floor. Above floor 7 is 1 floor (floor 8). So Floor 7.",
                "points": 1
            },
            {
                "id": 4905,
                "topic_id": 49,
                "question": "Which of the following months has exactly 30 days?",
                "options_json": [
                    "April",
                    "January",
                    "March",
                    "May"
                ],
                "correct_answer": "April",
                "explanation": "April, June, September, and November have 30 days.",
                "points": 1
            },
            {
                "id": 4906,
                "topic_id": 49,
                "question": "If 'Box X is immediately above Box Y', what is the relation between their positions?",
                "options_json": [
                    "Position(X) = Position(Y) + 1",
                    "Position(X) > Position(Y)",
                    "Position(X) < Position(Y)",
                    "Position(X) = Position(Y) - 1"
                ],
                "correct_answer": "Position(X) = Position(Y) + 1",
                "explanation": "'Immediately above' means consecutive adjacent position.",
                "points": 1
            },
            {
                "id": 4907,
                "topic_id": 49,
                "question": "If only two persons are taller than Mohan among 6 friends, what is Mohan's rank from tallest to shortest?",
                "options_json": [
                    "3rd",
                    "2nd",
                    "4th",
                    "1st"
                ],
                "correct_answer": "3rd",
                "explanation": "Since exactly two people are taller than Mohan, Mohan is 3rd in height.",
                "points": 1
            },
            {
                "id": 4908,
                "topic_id": 49,
                "question": "In a scheduling puzzle, Monday to Sunday covers how many days?",
                "options_json": [
                    "7 days",
                    "6 days",
                    "5 days",
                    "8 days"
                ],
                "correct_answer": "7 days",
                "explanation": "A complete week has 7 days.",
                "points": 1
            },
            {
                "id": 4909,
                "topic_id": 49,
                "question": "If A lives on an even-numbered floor in a 6-floor building, what are the possible floors for A?",
                "options_json": [
                    "2, 4, 6",
                    "1, 3, 5",
                    "4, 6 only",
                    "2 only"
                ],
                "correct_answer": "2, 4, 6",
                "explanation": "Even numbers between 1 and 6 are 2, 4, and 6.",
                "points": 1
            },
            {
                "id": 4910,
                "topic_id": 49,
                "question": "What should you do when an anchor clue gives two possible valid placements?",
                "options_json": [
                    "Draw two parallel cases (Case 1 and Case 2)",
                    "Guess one and erase if wrong",
                    "Skip the entire puzzle",
                    "Leave the exam"
                ],
                "correct_answer": "Draw two parallel cases (Case 1 and Case 2)",
                "explanation": "Drawing parallel cases is the proven, fastest method to resolve ambiguity without erasing.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4901,
                "topic_id": 49,
                "question": "In an 8-floor building, how many floors are between Floor 2 and Floor 7?",
                "options_json": [
                    "4",
                    "5",
                    "3",
                    "6"
                ],
                "correct_answer": "4",
                "explanation": "Floors 3, 4, 5, 6 are between them (total 4 floors).",
                "points": 1
            },
            {
                "id": 4902,
                "topic_id": 49,
                "question": "Among 4 friends, P is older than Q, and R is older than P. Who is older: R or Q?",
                "options_json": [
                    "R is older than Q",
                    "Q is older than R",
                    "They are same age",
                    "Cannot say"
                ],
                "correct_answer": "R is older than Q",
                "explanation": "R > P > Q, so R is older than Q.",
                "points": 1
            },
            {
                "id": 4903,
                "topic_id": 49,
                "question": "How many days are in July?",
                "options_json": [
                    "31",
                    "30",
                    "28",
                    "29"
                ],
                "correct_answer": "31",
                "explanation": "July has 31 days.",
                "points": 1
            },
            {
                "id": 4904,
                "topic_id": 49,
                "question": "If 'Box P is three places above Box Q', how many boxes are between P and Q?",
                "options_json": [
                    "2",
                    "3",
                    "1",
                    "4"
                ],
                "correct_answer": "2",
                "explanation": "Three places above means Position(P) = Position(Q) + 3. The boxes between are 2.",
                "points": 1
            },
            {
                "id": 4905,
                "topic_id": 49,
                "question": "In a 6-floor building, if A is on the top floor and B is on the bottom floor, how many floors are between them?",
                "options_json": [
                    "4",
                    "5",
                    "6",
                    "3"
                ],
                "correct_answer": "4",
                "explanation": "Floors 2, 3, 4, 5 are between them = 4 floors.",
                "points": 1
            },
            {
                "id": 4906,
                "topic_id": 49,
                "question": "Which of the following months has 30 days?",
                "options_json": [
                    "September",
                    "August",
                    "October",
                    "December"
                ],
                "correct_answer": "September",
                "explanation": "September has 30 days.",
                "points": 1
            },
            {
                "id": 4907,
                "topic_id": 49,
                "question": "If 5 boxes are stacked, which position is the middle box?",
                "options_json": [
                    "3rd from bottom (or top)",
                    "2nd from bottom",
                    "4th from bottom",
                    "1st"
                ],
                "correct_answer": "3rd from bottom (or top)",
                "explanation": "For 5 items, the middle is (5 + 1) / 2 = 3rd position.",
                "points": 1
            },
            {
                "id": 4908,
                "topic_id": 49,
                "question": "If A > B > C > D, who is the 3rd tallest?",
                "options_json": [
                    "C",
                    "B",
                    "A",
                    "D"
                ],
                "correct_answer": "C",
                "explanation": "1st: A, 2nd: B, 3rd: C, 4th: D.",
                "points": 1
            },
            {
                "id": 4909,
                "topic_id": 49,
                "question": "What is an 'anchor clue' in a puzzle?",
                "options_json": [
                    "A clue that fixes an absolute definite position",
                    "A negative clue",
                    "A clue with multiple possibilities",
                    "A clue about colors"
                ],
                "correct_answer": "A clue that fixes an absolute definite position",
                "explanation": "An anchor clue gives a definitive, non-relative position on the grid.",
                "points": 1
            },
            {
                "id": 4910,
                "topic_id": 49,
                "question": "In a building of 5 floors, if E is on floor 1, can anyone live below E?",
                "options_json": [
                    "No, floor 1 is the bottom floor",
                    "Yes, on floor 0",
                    "Yes, on basement",
                    "Depends on country"
                ],
                "correct_answer": "No, floor 1 is the bottom floor",
                "explanation": "Floor 1 is the ground/bottom floor in standard reasoning puzzles.",
                "points": 1
            }
        ]
    },
    "50": {
        "title": "Seating Arrangement: Circular (In/Out), Linear (Single/Dual Row) & Polygon Formations",
        "source_id": 7,
        "content": {
            "definition": "Seating Arrangement evaluates spatial and relational positioning of individuals situated along linear rows, circular perimeters, or polygonal tables under specific directional constraints (facing the center vs facing outward, facing North vs South). A cornerstone of Banking examinations (IBPS/SBI PO and Clerk) and SSC CGL Tier 1/2, seating arrangements test relative left/right orientations, diametric opposite placements, and multi-variable integration (names + cities/blood relations).",
            "overview": "Fundamental Seating Formations & Rules:\n- Circular Arrangement:\n  - Facing Center (Inward): Right turn = Anti-Clockwise (ACW); Left turn = Clockwise (CW)\n  - Facing Away from Center (Outward): Right turn = Clockwise (CW); Left turn = Anti-Clockwise (ACW)\n  - Diametrically Opposite: In an 8-person circular table, opposite person is separated by exactly 3 people on either side (Position + 4)\n- Linear Single Row:\n  - Facing North: Right = East (Your Right); Left = West (Your Left)\n  - Facing South: Right = West (Your Left); Left = East (Your Right) [Inverted!]\n- Linear Dual Parallel Rows: Row 1 facing South; Row 2 facing North (facing each other)\n- Square / Rectangular Tables: Persons at corners vs persons at the middle of sides facing opposite directions",
            "types": [
                {
                    "name": "1. Circular Arrangement \u2014 All Facing Center",
                    "desc": "6 or 8 people seated around a circular table looking inward.",
                    "examples": [
                        "A sits 2nd to the right of B (Move 2 steps Anti-Clockwise from B)",
                        "Opposite person in an 8-person table is 4 steps away"
                    ]
                },
                {
                    "name": "2. Circular Arrangement \u2014 Facing Inward & Outward Mixed",
                    "desc": "Some people face the center while others face outward, reversing relative left/right directions.",
                    "examples": [
                        "A faces center; B faces away from center; C sits to the immediate left of B"
                    ]
                },
                {
                    "name": "3. Linear Single Row \u2014 Facing North & South",
                    "desc": "Arranging 7-8 people in a single horizontal row with directional orientations.",
                    "examples": [
                        "P sits 3rd from the left end of the row",
                        "Q sits 2nd to the right of P"
                    ]
                },
                {
                    "name": "4. Dual Parallel Rows (Facing Each Other)",
                    "desc": "Two rows of 5-6 people each: Row 1 facing South, Row 2 facing North.",
                    "examples": [
                        "The person facing A sits 2nd to the left of B",
                        "Diagonal opposite alignment"
                    ]
                },
                {
                    "name": "5. Square & Rectangular Table Arrangements",
                    "desc": "Corner people face outward while side-center people face inward.",
                    "examples": [
                        "4 corners and 4 middle edges with opposing facing directions"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Facing Inward vs Outward Directional Inversion Rule",
                    "explanation": "In a circular arrangement:\n- **Facing Center**: Right is Anti-Clockwise (ACW); Left is Clockwise (CW).\n- **Facing Outward**: Right is Clockwise (CW); Left is Anti-Clockwise (ACW).\n*Never confuse inward and outward left/right directions!*",
                    "words": [
                        "Center: Right=ACW, Left=CW",
                        "Outward: Right=CW, Left=ACW",
                        "Direction Inversion"
                    ],
                    "correct": "When facing center, going Right moves anti-clockwise around the table.",
                    "incorrect": "Using your own right hand when the person faces outward away from you."
                },
                {
                    "rule_number": 2,
                    "title": "Circular Opposite Partner Rule (N / 2)",
                    "explanation": "In any even-numbered circle of $N$ people (e.g. $N=8$), the person sitting directly opposite person $X$ is located at $(N/2)$ steps away in either direction (for $N=8$, $8/2 = 4$ steps; exactly 3 people sit between them on both sides).",
                    "words": [
                        "Opposite Partner",
                        "N / 2 Steps",
                        "Symmetric Gap (N/2 - 1)"
                    ],
                    "correct": "In an 8-person table, A is opposite B means 3 persons sit between A and B on both sides.",
                    "incorrect": "Placing 4 people between them."
                },
                {
                    "rule_number": 3,
                    "title": "Linear Row Facing South Inversion Rule",
                    "explanation": "When people in a linear row face SOUTH:\n- Their RIGHT is towards YOUR LEFT (West).\n- Their LEFT is towards YOUR RIGHT (East).\nAlways invert your perspective when solving South-facing linear arrangements.",
                    "words": [
                        "Facing South",
                        "Inverted Perspective",
                        "Right = Your Left"
                    ],
                    "correct": "Person facing South turns right => moves to the West (your left hand).",
                    "incorrect": "Using your personal right hand."
                },
                {
                    "rule_number": 4,
                    "title": "'Immediate Left/Right' vs 'To the Left/Right'",
                    "explanation": "- '$A$ sits **to the right** of $B$' $\\implies A$ can sit anywhere to the right of $B$ (not necessarily adjacent).\n- '$A$ sits **immediate right** of $B$' $\\implies A$ is the adjacent neighbor ($+1$ step).",
                    "words": [
                        "Immediate vs General Left/Right",
                        "Neighbor vs Position"
                    ],
                    "correct": "Treating 'immediate right' as position +1 and 'to the right' as any position to the right.",
                    "incorrect": "Assuming 'to the right' always means adjacent neighbor."
                },
                {
                    "rule_number": 5,
                    "title": "'And' vs 'Who' Pronoun Reference Rule",
                    "explanation": "In compound clues:\n- **'Who' / 'Whom' / 'Whose'** refers strictly to the **IMMEDIATE PRECEDING (Second)** person: '$A$ sits 2nd to the left of $B$, **who** faces center' $\\implies B$ faces center.\n- **'And' / 'But' / 'While'** refers to the **FIRST** person: '$A$ sits 2nd to the left of $B$, **and** faces center' $\\implies A$ faces center.",
                    "words": [
                        "'Who' refers to 2nd person",
                        "'And' refers to 1st person",
                        "Crucial Syntax"
                    ],
                    "correct": "Correctly assigning facing directions based on 'who' (second person) vs 'and' (first person).",
                    "incorrect": "Assigning 'who' to the first person, invalidating the entire diagram."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Misattributing 'who' to the first person in a clue sentence.",
                    "correction": "'Who' ALWAYS refers to the immediate predecessor (the 2nd person mentioned).",
                    "rationale": "#1 most common error in banking seating arrangement puzzles."
                },
                {
                    "mistake": "Mixing up clockwise/anti-clockwise when people face outside.",
                    "correction": "Facing outside reverses your perspective: Right becomes CW, Left becomes ACW.",
                    "rationale": "Prevents placing elements on the opposite side of the circle."
                },
                {
                    "mistake": "Forgetting that South-facing people have their Right towards your Left.",
                    "correction": "Invert perspective immediately when a person faces South.",
                    "rationale": "Saves restarting whole linear puzzles."
                },
                {
                    "mistake": "Placing opposite partner with wrong number of intermediate seats.",
                    "correction": "For 8 people, opposite has 3 people in between (4 steps away). For 6 people, 2 in between (3 steps away).",
                    "rationale": "Symmetric circle division rule."
                }
            ],
            "quick_revision_points": [
                "Facing center: Right = Anti-Clockwise (ACW), Left = Clockwise (CW)",
                "Facing outward: Right = Clockwise (CW), Left = Anti-Clockwise (ACW)",
                "Linear Facing North: Right = East (Your right); Facing South: Right = West (Your left)",
                "'Who' refers to the 2nd person (immediate predecessor)",
                "'And' / 'But' refers to the 1st person",
                "8-person circle: Opposite partner is 4 steps away with 3 people in between on both sides",
                "Immediate right/left = adjacent neighbor (+1 step)"
            ]
        },
        "previous_year_questions": [
            {
                "id": 5001,
                "topic_id": 50,
                "exam_id": 1,
                "question": "Eight friends A, B, C, D, E, F, G, H are sitting around a circular table facing the center. A sits third to the right of B. H sits second to the left of A. Who sits directly opposite to B? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "E",
                    "H",
                    "F",
                    "Cannot be determined without other clues"
                ],
                "correct_answer": "Cannot be determined without other clues",
                "explanation": "Let positions be 1 to 8 in anti-clockwise order:\n- Place B at Position 1.\n- A sits third to the right of B (Anti-Clockwise): Position 1 + 3 = Position 4.\n- H sits second to the left of A (Clockwise): Position 4 - 2 = Position 2.\n- The person directly opposite to B (Position 1) is at Position 1 + 4 = Position 5.\n- Positions 3, 5, 6, 7, 8 are shared among C, D, E, F, G.\n- Without additional clues specifying who occupies Position 5, the person opposite B cannot be uniquely determined from these two clues alone.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5002,
                "topic_id": 50,
                "exam_id": 1,
                "question": "Five friends P, Q, R, S, T are sitting in a row facing North. S sits at the extreme right end. Q sits to the immediate left of S. P sits between R and Q. T sits to the immediate left of R. Who sits at the extreme left end? [RRB NTPC 2022]",
                "options_json": [
                    "T",
                    "R",
                    "P",
                    "Q"
                ],
                "correct_answer": "T",
                "explanation": "Positions from left to right (1 to 5 facing North):\n1. S is at extreme right: Position 5 = S.\n2. Q is immediate left of S: Position 4 = Q.\n3. P sits between R and Q: Position 3 = P, Position 2 = R.\n4. T is immediate left of R: Position 1 = T.\nTherefore, T sits at the extreme left end.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5003,
                "topic_id": 50,
                "exam_id": 1,
                "question": "In a circular table of 6 people facing center, how many people sit between two people who are directly opposite each other? [IBPS PO 2022]",
                "options_json": [
                    "2",
                    "3",
                    "1",
                    "4"
                ],
                "correct_answer": "2",
                "explanation": "In a circle of 6 people, dividing equally gives 6 / 2 = 3 steps away.\nBetween position 1 and position 4, positions 2 and 3 lie on one side, and positions 5 and 6 lie on the other side.\nThus, exactly 2 people sit between them on either side.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 5001,
                "topic_id": 50,
                "question": "In a circle of 8 people facing the center, which direction is 'Right'?",
                "options_json": [
                    "Anti-Clockwise",
                    "Clockwise",
                    "Upwards",
                    "Downwards"
                ],
                "correct_answer": "Anti-Clockwise",
                "explanation": "When facing center, Right corresponds to Anti-Clockwise movement around the perimeter.",
                "points": 1
            },
            {
                "id": 5002,
                "topic_id": 50,
                "question": "In a row of people facing North, which direction is to your right?",
                "options_json": [
                    "East",
                    "West",
                    "North",
                    "South"
                ],
                "correct_answer": "East",
                "explanation": "Facing North, Right is East.",
                "points": 1
            },
            {
                "id": 5003,
                "topic_id": 50,
                "question": "In 'A sits second to the left of B, who faces outside', who faces outside?",
                "options_json": [
                    "B",
                    "A",
                    "Both",
                    "Neither"
                ],
                "correct_answer": "B",
                "explanation": "'Who' refers to the immediate predecessor (the second person, B).",
                "points": 1
            },
            {
                "id": 5004,
                "topic_id": 50,
                "question": "In an 8-person circular table, how many persons sit between two opposite partners?",
                "options_json": [
                    "3",
                    "4",
                    "2",
                    "1"
                ],
                "correct_answer": "3",
                "explanation": "Opposite partners are separated by exactly 3 persons on both sides.",
                "points": 1
            },
            {
                "id": 5005,
                "topic_id": 50,
                "question": "Five friends sit in a row facing North: A, B, C, D, E. C is in the middle. B is to the immediate right of C. Which position is B from left?",
                "options_json": [
                    "4th",
                    "3rd",
                    "2nd",
                    "5th"
                ],
                "correct_answer": "4th",
                "explanation": "C is 3rd (middle). B is immediately right of C, so B is at 4th position.",
                "points": 1
            },
            {
                "id": 5006,
                "topic_id": 50,
                "question": "When people face SOUTH in a row, where is their 'Left'?",
                "options_json": [
                    "Towards your Right (East)",
                    "Towards your Left (West)",
                    "Towards North",
                    "Towards South"
                ],
                "correct_answer": "Towards your Right (East)",
                "explanation": "Facing South inverts perspective: their left is towards your right (East).",
                "points": 1
            },
            {
                "id": 5007,
                "topic_id": 50,
                "question": "In a circular table, people facing OUTWARD have their 'Right' in which direction?",
                "options_json": [
                    "Clockwise",
                    "Anti-Clockwise",
                    "Inward",
                    "Outward"
                ],
                "correct_answer": "Clockwise",
                "explanation": "Facing outward inverts circle orientation: Right is Clockwise.",
                "points": 1
            },
            {
                "id": 5008,
                "topic_id": 50,
                "question": "In 'P sits next to Q, and faces North', who faces North?",
                "options_json": [
                    "P",
                    "Q",
                    "Both",
                    "Neither"
                ],
                "correct_answer": "P",
                "explanation": "'And' refers to the first person mentioned (P).",
                "points": 1
            },
            {
                "id": 5009,
                "topic_id": 50,
                "question": "Six people sit around a circular table facing center. A is 2nd to the right of B. How many people sit between A and B on the shorter side?",
                "options_json": [
                    "1",
                    "2",
                    "3",
                    "0"
                ],
                "correct_answer": "1",
                "explanation": "A is 2 steps away from B, meaning exactly 1 person sits between them.",
                "points": 1
            },
            {
                "id": 5010,
                "topic_id": 50,
                "question": "Two parallel rows face each other. Row 1 faces South. Row 2 faces North. What is the relation between them?",
                "options_json": [
                    "They look directly at each other",
                    "They look away from each other",
                    "They face the same direction",
                    "They are perpendicular"
                ],
                "correct_answer": "They look directly at each other",
                "explanation": "Row 1 looking South and Row 2 looking North face directly towards each other.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 5001,
                "topic_id": 50,
                "question": "In a circle of 8 people facing center, A is 4 steps away from B. What is their relative position?",
                "options_json": [
                    "Directly opposite each other",
                    "Adjacent neighbors",
                    "2nd to left",
                    "3rd to right"
                ],
                "correct_answer": "Directly opposite each other",
                "explanation": "4 steps in an 8-person table is directly opposite (8/2 = 4).",
                "points": 1
            },
            {
                "id": 5002,
                "topic_id": 50,
                "question": "If you are facing North in a row, which side is your Left?",
                "options_json": [
                    "West",
                    "East",
                    "North",
                    "South"
                ],
                "correct_answer": "West",
                "explanation": "Facing North, Left is West.",
                "points": 1
            },
            {
                "id": 5003,
                "topic_id": 50,
                "question": "In 'X is sitting between Y and Z', is X adjacent to both Y and Z?",
                "options_json": [
                    "Yes, immediate neighbor to both",
                    "No, only to Y",
                    "No, only to Z",
                    "Not necessarily"
                ],
                "correct_answer": "Yes, immediate neighbor to both",
                "explanation": "Sitting between Y and Z means Y - X - Z (adjacent to both).",
                "points": 1
            },
            {
                "id": 5004,
                "topic_id": 50,
                "question": "When facing center, clockwise movement around the table corresponds to:",
                "options_json": [
                    "Moving to the Left",
                    "Moving to the Right",
                    "Moving Outward",
                    "Moving Inward"
                ],
                "correct_answer": "Moving to the Left",
                "explanation": "Clockwise is Left when facing center.",
                "points": 1
            },
            {
                "id": 5005,
                "topic_id": 50,
                "question": "In an 8-person circle, if A sits 3rd to right of B, how many people sit between them on that side?",
                "options_json": [
                    "2",
                    "3",
                    "1",
                    "4"
                ],
                "correct_answer": "2",
                "explanation": "3rd to right means 3 steps away, with 2 people in between.",
                "points": 1
            },
            {
                "id": 5006,
                "topic_id": 50,
                "question": "In a row of 7 people facing North, what is the middle position?",
                "options_json": [
                    "4th",
                    "3rd",
                    "5th",
                    "2nd"
                ],
                "correct_answer": "4th",
                "explanation": "(7 + 1) / 2 = 4th position.",
                "points": 1
            },
            {
                "id": 5007,
                "topic_id": 50,
                "question": "Who does the relative pronoun 'who' refer to in a seating clue?",
                "options_json": [
                    "The immediately preceding person",
                    "The first person mentioned",
                    "The whole group",
                    "The speaker"
                ],
                "correct_answer": "The immediately preceding person",
                "explanation": "'Who' strictly refers to the nearest antecedent (the second person).",
                "points": 1
            },
            {
                "id": 5008,
                "topic_id": 50,
                "question": "If A is to the immediate right of B in a North-facing row, what is B to A?",
                "options_json": [
                    "Immediate left",
                    "Immediate right",
                    "2nd to left",
                    "2nd to right"
                ],
                "correct_answer": "Immediate left",
                "explanation": "If A is immediately right of B, B is immediately left of A.",
                "points": 1
            },
            {
                "id": 5009,
                "topic_id": 50,
                "question": "How many corners are in a standard square seating arrangement?",
                "options_json": [
                    "4",
                    "8",
                    "6",
                    "2"
                ],
                "correct_answer": "4",
                "explanation": "A square has 4 corners and 4 side-centers.",
                "points": 1
            },
            {
                "id": 5010,
                "topic_id": 50,
                "question": "If 6 people sit around a table facing center, what is the step distance to the opposite person?",
                "options_json": [
                    "3 steps",
                    "2 steps",
                    "4 steps",
                    "1 step"
                ],
                "correct_answer": "3 steps",
                "explanation": "6 / 2 = 3 steps away.",
                "points": 1
            }
        ]
    },
    "51": {
        "title": "Non-Verbal Reasoning: Mirror & Water Images, Paper Folding, Embedded Figures & Cubes",
        "source_id": 7,
        "content": {
            "definition": "Non-Verbal Reasoning examines visual-spatial intelligence, geometric transformations, symmetry mapping, and figure manipulation without reliance on linguistic text. Extensively tested in SSC CGL Tier 1/2, CHSL, RRB NTPC, and Defence (AFCAT, NDA) examinations, problems encompass mirror reflections (lateral inversion: Left $\\leftrightarrow$ Right), water reflections (vertical inversion: Top $\\leftrightarrow$ Bottom), paper folding and punching, embedded hidden figures, pattern matrix completion, and standard/general dice rules.",
            "overview": "Fundamental Spatial Inversion & Cube Principles:\n- Mirror Image (Vertical Mirror $MN$ on right/left):\n  - Left and Right are swapped (Lateral Inversion)\n  - Top and Bottom remain strictly unchanged\n  - Symmetrical letters with identical mirror images: A, H, I, M, O, T, U, V, W, X, Y (11 letters)\n- Water Image (Horizontal Mirror at base):\n  - Top and Bottom are inverted (Vertical Inversion)\n  - Left and Right remain unchanged\n  - Letters with identical water images: B, C, D, E, H, I, K, O, X (9 letters)\n- Standard vs General Dice:\n  - Standard Dice: Sum of opposite faces is strictly $7$ ($1 \\leftrightarrow 6, 2 \\leftrightarrow 5, 3 \\leftrightarrow 4$); adjacent faces never sum to 7\n  - General Dice: Common face rule\u2014if two positions share one common face, rotate clockwise to find opposite pairs",
            "types": [
                {
                    "name": "1. Mirror Image Identification",
                    "desc": "Predicting the reflection across a vertical mirror line (Left becomes Right, Right becomes Left).",
                    "examples": [
                        "Reflection of 'L' faces left; reflection of 'b' becomes 'd'",
                        "Clock reflection shortcut: Mirror Time = 11:60 - Actual Time"
                    ]
                },
                {
                    "name": "2. Water Image Identification",
                    "desc": "Predicting reflection on a horizontal water surface (Top becomes Bottom, Bottom becomes Top).",
                    "examples": [
                        "Water image of 'M' is 'W'; water image of 'A' points downward",
                        "Clock water reflection shortcut: Water Time = 18:30 - Actual Time"
                    ]
                },
                {
                    "name": "3. Paper Folding and Punching",
                    "desc": "Unfolding a folded, hole-punched sheet of paper to reveal the resulting symmetric pattern.",
                    "examples": [
                        "A sheet folded twice into quarters and punched with 1 hole produces 4 symmetric holes upon unfolding"
                    ]
                },
                {
                    "name": "4. Embedded Figures & Pattern Completion",
                    "desc": "Spotting a hidden geometric motif inside a complex figure, or completing a missing 4th quadrant.",
                    "examples": [
                        "Locating an 'N' or 'Z' shape disguised inside overlapping polygons",
                        "Matching quadrant symmetry across horizontal/vertical axes"
                    ]
                },
                {
                    "name": "5. Cubes and Dice Properties",
                    "desc": "Determining opposite faces on a 6-sided die from multiple views or an unfolded net.",
                    "examples": [
                        "Standard die: 1 is opposite 6, 2 is opposite 5, 3 is opposite 4",
                        "Single common face rule: Clockwise rotation from the common number yields opposite pairs"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Mirror Lateral Inversion vs Water Vertical Inversion Rule",
                    "explanation": "- **Mirror Image (Vertical Mirror)**: Left $\\leftrightarrow$ Right swap. Top and bottom DO NOT change.\n- **Water Image (Horizontal Mirror)**: Top $\\leftrightarrow$ Bottom swap. Left and right DO NOT change.",
                    "words": [
                        "Mirror = Left-Right Swap",
                        "Water = Top-Bottom Swap",
                        "Fundamental Inversions"
                    ],
                    "correct": "Letter 'E' in a mirror has prongs pointing left. Letter 'E' in water still has prongs pointing right!",
                    "incorrect": "Flipping left-right in water images."
                },
                {
                    "rule_number": 2,
                    "title": "Clock Mirror Image 11:60 Formula",
                    "explanation": "If a 12-hour clock shows actual time $H : M$, its reflection in a vertical mirror shows:\n$\\text{Mirror Time} = 11:60 - (H : M)$.\n(If time exceeds 12, use $23:60 - H:M$).",
                    "words": [
                        "11:60 Formula",
                        "Clock Mirror Reflection",
                        "Instant Shortcut"
                    ],
                    "correct": "Actual time is 8:20. Mirror time = 11:60 - 8:20 = 3:40.",
                    "incorrect": "Drawing clock hands by hand and guessing approximate angles."
                },
                {
                    "rule_number": 3,
                    "title": "Single Common Face Dice Clockwise Rule",
                    "explanation": "When two views of a die show exactly ONE common number $C$:\n1. Write numbers starting from $C$ in CLOCKWISE order for View 1: $C \\rightarrow X \\rightarrow Y$.\n2. Write numbers starting from $C$ in CLOCKWISE order for View 2: $C \\rightarrow P \\rightarrow Q$.\n3. $X$ is opposite $P$, $Y$ is opposite $Q$, and $C$ is opposite the remaining 6th number.",
                    "words": [
                        "Common Face Clockwise Rule",
                        "Dice Opposites",
                        "Standard Rotation"
                    ],
                    "correct": "View 1: 3-1-2; View 2: 3-5-6 => 1 opposite 5, 2 opposite 6, 3 opposite 4.",
                    "incorrect": "Guessing without writing the clockwise chain."
                },
                {
                    "rule_number": 4,
                    "title": "Standard Dice Opposite Sum 7 Rule",
                    "explanation": "In a **Standard Die**, the sum of numbers on any two opposite faces is ALWAYS 7 ($1+6=7, 2+5=7, 3+4=7$). Therefore, two opposite faces can NEVER be adjacent (visible together in the same view).",
                    "words": [
                        "Standard Die Sum = 7",
                        "Opposite Never Adjacent"
                    ],
                    "correct": "If 1 is on top, 6 is on bottom. If 2 is in front, 5 is at the back.",
                    "incorrect": "Assuming any die with sum of adjacent faces equal to 7 is standard."
                },
                {
                    "rule_number": 5,
                    "title": "Paper Unfolding Reverse Symmetry Rule",
                    "explanation": "To solve paper punching: Work strictly in REVERSE order of the folding steps. Each fold acts as a mirror line. Reflect the punched hole across each fold line step-by-step.",
                    "words": [
                        "Reverse Unfolding",
                        "Fold Line = Mirror Line",
                        "Step-by-Step Reflection"
                    ],
                    "correct": "Reflecting the punch across the last fold line first, then across the earlier fold line.",
                    "incorrect": "Trying to imagine the final fully unfolded page all at once."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Swapping left-right in water images.",
                    "correction": "Water images only invert TOP and BOTTOM. Left and right remain completely unchanged.",
                    "rationale": "Horizontal mirror reflection physics rule."
                },
                {
                    "mistake": "Forgetting that word mirror images invert letter order as well as the letters themselves.",
                    "correction": "In a mirror, the LAST letter of the word becomes the FIRST letter in the reflection.",
                    "rationale": "The right end of the word is closest to the mirror."
                },
                {
                    "mistake": "Drawing clock hands manually instead of using 11:60.",
                    "correction": "Subtract actual time from 11:60 to get exact mirror time in 2 seconds.",
                    "rationale": "Saves 1 minute and prevents hand-angle misjudgments."
                },
                {
                    "mistake": "Assuming two numbers visible together on a die can be opposite.",
                    "correction": "Adjacent faces can NEVER be opposite faces.",
                    "rationale": "Fundamental 3D cube geometry."
                }
            ],
            "quick_revision_points": [
                "Mirror Image: Left <-> Right (Top/Bottom fixed). 11 letters identical: A, H, I, M, O, T, U, V, W, X, Y",
                "Water Image: Top <-> Bottom (Left/Right fixed). 9 letters identical: B, C, D, E, H, I, K, O, X",
                "Clock Mirror Time = 11:60 - Actual Time",
                "Clock Water Time = 18:30 - Actual Time",
                "Standard Die: Sum of opposite faces = 7 (1-6, 2-5, 3-4)",
                "Dice rotation: Start at common face, read clockwise on both views to pair opposites",
                "Unfolding paper: Trace backwards; each fold line is a mirror reflection axis"
            ]
        },
        "previous_year_questions": [
            {
                "id": 5101,
                "topic_id": 51,
                "exam_id": 1,
                "question": "A clock shows 8:35. What time will it show in a vertical mirror reflection? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "3:25",
                    "3:35",
                    "4:25",
                    "4:35"
                ],
                "correct_answer": "3:25",
                "explanation": "Use the Clock Mirror formula: 11:60 - Actual Time\n11:60 - 8:35:\nHours: 11 - 8 = 3\nMinutes: 60 - 35 = 25\nMirror time = 3:25.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5102,
                "topic_id": 51,
                "exam_id": 1,
                "question": "Two positions of a dice are shown. When number 1 is on the top, which number will be at the bottom? Position 1 shows 3, 1, 2. Position 2 shows 3, 5, 6. [RRB NTPC 2022]",
                "options_json": [
                    "5",
                    "6",
                    "4",
                    "2"
                ],
                "correct_answer": "5",
                "explanation": "3 is the single common face in both positions.\nWrite numbers clockwise from 3:\nPosition 1: 3 -> 1 -> 2\nPosition 2: 3 -> 5 -> 6\nBy alignment:\n1 is opposite 5\n2 is opposite 6\n3 is opposite 4\nWhen 1 is on top, 5 is at the bottom.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5103,
                "topic_id": 51,
                "exam_id": 1,
                "question": "Which capital letter among the following has the SAME water image as the original letter? [SSC CHSL 2022]",
                "options_json": [
                    "H",
                    "A",
                    "M",
                    "N"
                ],
                "correct_answer": "H",
                "explanation": "In a water image, top and bottom invert.\n- 'A' flips upside down to a downward point (changes).\n- 'M' flips upside down to 'W' (changes).\n- 'N' flips with diagonal reversed (changes).\n- 'H' has horizontal symmetry across its horizontal midline, so its water image is identical to H.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 5101,
                "topic_id": 51,
                "question": "What is the mirror image time of a clock showing 3:15?",
                "options_json": [
                    "8:45",
                    "9:45",
                    "8:15",
                    "7:45"
                ],
                "correct_answer": "8:45",
                "explanation": "11:60 - 3:15 = 8:45.",
                "points": 1
            },
            {
                "id": 5102,
                "topic_id": 51,
                "question": "In a standard die, what number is opposite to 4?",
                "options_json": [
                    "3",
                    "5",
                    "6",
                    "2"
                ],
                "correct_answer": "3",
                "explanation": "In a standard die, opposite faces sum to 7. 7 - 4 = 3.",
                "points": 1
            },
            {
                "id": 5103,
                "topic_id": 51,
                "question": "Which letter has an identical mirror image?",
                "options_json": [
                    "M",
                    "B",
                    "E",
                    "P"
                ],
                "correct_answer": "M",
                "explanation": "M has vertical symmetry, so its mirror image is identical to M.",
                "points": 1
            },
            {
                "id": 5104,
                "topic_id": 51,
                "question": "In a water image, what happens to the left and right sides of an object?",
                "options_json": [
                    "They remain unchanged",
                    "They are swapped",
                    "They move to top",
                    "They disappear"
                ],
                "correct_answer": "They remain unchanged",
                "explanation": "Water reflection only inverts Top and Bottom; Left and Right remain unchanged.",
                "points": 1
            },
            {
                "id": 5105,
                "topic_id": 51,
                "question": "What is the water image of the letter 'M'?",
                "options_json": [
                    "W",
                    "M",
                    "N",
                    "E"
                ],
                "correct_answer": "W",
                "explanation": "Flipping M vertically produces W.",
                "points": 1
            },
            {
                "id": 5106,
                "topic_id": 51,
                "question": "If a square paper is folded in half twice and 1 circular hole is punched through all layers, how many holes appear when unfolded?",
                "options_json": [
                    "4",
                    "2",
                    "8",
                    "1"
                ],
                "correct_answer": "4",
                "explanation": "Folding in half twice creates 2 * 2 = 4 layers. 1 punch through 4 layers yields 4 holes.",
                "points": 1
            },
            {
                "id": 5107,
                "topic_id": 51,
                "question": "In a standard die, what number is opposite to 2?",
                "options_json": [
                    "5",
                    "4",
                    "6",
                    "3"
                ],
                "correct_answer": "5",
                "explanation": "7 - 2 = 5.",
                "points": 1
            },
            {
                "id": 5108,
                "topic_id": 51,
                "question": "What is the mirror image of a clock showing 7:00?",
                "options_json": [
                    "5:00",
                    "4:00",
                    "6:00",
                    "8:00"
                ],
                "correct_answer": "5:00",
                "explanation": "11:60 - 7:00 = 4:60 = 5:00 (or 12:00 - 7:00 = 5:00).",
                "points": 1
            },
            {
                "id": 5109,
                "topic_id": 51,
                "question": "Which letter has an identical water image?",
                "options_json": [
                    "C",
                    "A",
                    "F",
                    "J"
                ],
                "correct_answer": "C",
                "explanation": "C has horizontal symmetry across its equator, so its water reflection is identical.",
                "points": 1
            },
            {
                "id": 5110,
                "topic_id": 51,
                "question": "Can two opposite faces of a die ever be adjacent to each other?",
                "options_json": [
                    "No, never",
                    "Yes, in standard dice",
                    "Yes, in general dice",
                    "Sometimes"
                ],
                "correct_answer": "No, never",
                "explanation": "Opposite faces are parallel plane surfaces and can never share an edge or vertex.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 5101,
                "topic_id": 51,
                "question": "In a standard die, what is the sum of any two opposite faces?",
                "options_json": [
                    "7",
                    "6",
                    "8",
                    "5"
                ],
                "correct_answer": "7",
                "explanation": "By definition of a standard die, opposite faces always sum to 7.",
                "points": 1
            },
            {
                "id": 5102,
                "topic_id": 51,
                "question": "What is the mirror time of a clock showing 10:10?",
                "options_json": [
                    "1:50",
                    "2:50",
                    "1:10",
                    "2:10"
                ],
                "correct_answer": "1:50",
                "explanation": "11:60 - 10:10 = 1:50.",
                "points": 1
            },
            {
                "id": 5103,
                "topic_id": 51,
                "question": "Which of the following letters has an identical mirror image?",
                "options_json": [
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "correct_answer": "A",
                "explanation": "A has a vertical axis of symmetry, so its mirror reflection is unchanged.",
                "points": 1
            },
            {
                "id": 5104,
                "topic_id": 51,
                "question": "What is the water image of the letter 'B'?",
                "options_json": [
                    "B",
                    "D",
                    "P",
                    "Q"
                ],
                "correct_answer": "B",
                "explanation": "B has horizontal line symmetry; its top and bottom curves reflect into each other, preserving B.",
                "points": 1
            },
            {
                "id": 5105,
                "topic_id": 51,
                "question": "In a standard die, what number is opposite to 6?",
                "options_json": [
                    "1",
                    "2",
                    "3",
                    "5"
                ],
                "correct_answer": "1",
                "explanation": "7 - 6 = 1.",
                "points": 1
            },
            {
                "id": 5106,
                "topic_id": 51,
                "question": "What is inverted in a mirror reflection?",
                "options_json": [
                    "Left and Right",
                    "Top and Bottom",
                    "Front and Back",
                    "Size of image"
                ],
                "correct_answer": "Left and Right",
                "explanation": "A vertical mirror causes lateral inversion (left-right swap).",
                "points": 1
            },
            {
                "id": 5107,
                "topic_id": 51,
                "question": "What is inverted in a water reflection?",
                "options_json": [
                    "Top and Bottom",
                    "Left and Right",
                    "Color of image",
                    "Size of image"
                ],
                "correct_answer": "Top and Bottom",
                "explanation": "A horizontal reflection surface inverts vertical coordinates (top-bottom swap).",
                "points": 1
            },
            {
                "id": 5108,
                "topic_id": 51,
                "question": "A die shows 2, 4, 1 in View 1 and 2, 3, 5 in View 2. What is opposite to 4? (Clockwise from 2: 4->1 and 3->5)",
                "options_json": [
                    "3",
                    "5",
                    "6",
                    "1"
                ],
                "correct_answer": "3",
                "explanation": "Clockwise from 2: View 1 has 4 then 1. View 2 has 3 then 5. 4 is opposite 3.",
                "points": 1
            },
            {
                "id": 5109,
                "topic_id": 51,
                "question": "What is the mirror image time of 6:00?",
                "options_json": [
                    "6:00",
                    "12:00",
                    "5:00",
                    "7:00"
                ],
                "correct_answer": "6:00",
                "explanation": "At 6:00, hands are vertically aligned along the 12-6 axis; reflection across vertical axis is still 6:00 (11:60 - 6:00 = 5:60 = 6:00).",
                "points": 1
            },
            {
                "id": 5110,
                "topic_id": 51,
                "question": "How many letters in the English alphabet have identical mirror images?",
                "options_json": [
                    "11",
                    "9",
                    "7",
                    "13"
                ],
                "correct_answer": "11",
                "explanation": "There are 11 vertically symmetric letters: A, H, I, M, O, T, U, V, W, X, Y.",
                "points": 1
            }
        ]
    }
}
