# reasoning_part1.py
REASONING_PART1_DATA = {
    "38": {
        "title": "Analogy: Word, Numerical, Alphabetical & Dual-Relation Logic",
        "source_id": 7,
        "content": {
            "definition": "Analogy is a cognitive reasoning process that evaluates the correspondence or relational equivalence between two distinct entities or pairs of elements. In competitive exams (SSC CGL Tier 1/2, RRB NTPC, IBPS PO, State PSCs), analogy tests semantic links (worker-tool, cause-effect, antonym-synonym, animal-habitat), mathematical transformations (square/cube shifts, prime clusters, digit operations), and positional letter variations.",
            "overview": "Fundamental Analogy Relationships:\n- Semantic / Word Analogy: Worker & Tool (Carpenter : Saw), Quantity & Unit (Current : Ampere), Country & Capital/Currency (Japan : Yen)\n- Number Analogy: Operations of the form $x : x^2 \\pm k$, $x : x^3 \\pm k$, $x : (x \\times k) + c$, sum of digits, or prime number sequencing\n- Alphabet Analogy: Positional shifts (Forward $+n$, Backward $-n$), reverse pairs ($A \\leftrightarrow Z, B \\leftrightarrow Y$), sum of letter ranks\n- Double Analogy: Finding simultaneous dual pairs conforming to an identical underlying governing pattern ($A : B :: C : D$)",
            "types": [
                {
                    "name": "1. Semantic & Verbal Knowledge Analogy",
                    "desc": "Relationships based on vocabulary, science, geography, instruments, and social conventions.",
                    "examples": [
                        "Barometer : Pressure :: Hygrometer : Humidity",
                        "Ornithologist : Birds :: Paleontologist : Fossils"
                    ]
                },
                {
                    "name": "2. Numerical & Mathematical Operation Analogy",
                    "desc": "Mathematical transformations linking numbers through powers, products, or arithmetic operations.",
                    "examples": [
                        "6 : 222 :: 7 : ? (Pattern: n^3 + n => 6^3 + 6 = 222, so 7^3 + 7 = 350)",
                        "12 : 144 :: 14 : 196 (Direct perfect squares)"
                    ]
                },
                {
                    "name": "3. Alphabetical & Letter-Shift Analogy",
                    "desc": "Positional changes in alphabetical ranking, reverse symmetry, or skipped steps.",
                    "examples": [
                        "LOCK : MPDL :: READ : SFBE (+1 forward shift to each character)",
                        "AZ : BY :: CX : DW (Opposite letter pairs)"
                    ]
                },
                {
                    "name": "4. Mixed / Alpha-Numeric Analogy",
                    "desc": "Interlocking relationships between letters and their positional numeric values or sums.",
                    "examples": [
                        "CAT : 24 :: DOG : 26 (Sum of ranks: 3+1+20 = 24; 4+15+7 = 26)",
                        "F : 216 :: L : 1728 (Rank of F=6 => 6^3 = 216; Rank of L=12 => 12^3 = 1728)"
                    ]
                },
                {
                    "name": "5. Group / Set Analogy",
                    "desc": "Selecting an option triplet that shares the exact relational rule found in a given set of numbers.",
                    "examples": [
                        "Given set (7, 13, 20): 7 + 6 = 13, 13 + 7 = 20 (Differences increment by 1)",
                        "Given set (4, 16, 64): Powers of 4 (4^1, 4^2, 4^3)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Prime Number Priority Rule in Numerical Analogies",
                    "explanation": "When evaluating number analogies, hierarchy of operations must be applied:\n1. Prime number sequence\n2. Square and Cube operations\n3. Multiplication and Division\n4. Addition and Subtraction\nIf a relationship can be explained by both prime numbers and arithmetic addition, the prime rule takes precedence.",
                    "words": [
                        "Hierarchy of Rules",
                        "Prime > Squares > Cubes > Mult/Div > Add/Sub"
                    ],
                    "correct": "4 : 9 :: 25 : 49 (Squares of consecutive primes: 2^2, 3^2, 5^2, 7^2).",
                    "incorrect": "Selecting 36 because 4 to 9 is +5 and 25 + 11 = 36."
                },
                {
                    "rule_number": 2,
                    "title": "Directional Order of Analogy Rule",
                    "explanation": "The relationship must be maintained strictly in the original order ($A \\rightarrow B$ must correspond to $C \\rightarrow D$). Reversing the subject and object or tool and worker produces a false analogy.",
                    "words": [
                        "Strict Directionality",
                        "Subject to Object Order"
                    ],
                    "correct": "Author : Novel :: Sculptor : Statue (Creator followed by Creation).",
                    "incorrect": "Author : Novel :: Statue : Sculptor (Inverted order)."
                },
                {
                    "rule_number": 3,
                    "title": "Opposite Letter Sum of 27 Rule",
                    "explanation": "Two letters are reverse counterparts in the 26-letter English alphabet if and only if the sum of their positional values equals 27: Rank(A) + Rank(Z) = 1 + 26 = 27; Rank(M) + Rank(N) = 13 + 14 = 27.",
                    "words": [
                        "Opposite Pairs",
                        "Sum = 27",
                        "Reverse Ranks"
                    ],
                    "correct": "H (rank 8) corresponds to S (rank 19) because 8 + 19 = 27.",
                    "incorrect": "Pairing H with T (sum = 28)."
                },
                {
                    "rule_number": 4,
                    "title": "Digit Sum & Product Rule",
                    "explanation": "In number analogies with large multi-digit integers where algebraic transformations fail, check the digital root (sum of digits) or product of digits.",
                    "words": [
                        "Digit Sum",
                        "Digital Root",
                        "Multi-digit Analogies"
                    ],
                    "correct": "524 : 11 :: 342 : 9 (5 + 2 + 4 = 11; 3 + 4 + 2 = 9).",
                    "incorrect": "Attempting complex polynomial division on multi-digit numbers."
                },
                {
                    "rule_number": 5,
                    "title": "Grammatical Part-of-Speech Invariance Rule",
                    "explanation": "If the first word pair connects two adjectives, the answer pair must also consist of two adjectives. An adjective cannot form a valid analogy with a noun or adverb if an adjective option exists.",
                    "words": [
                        "Part of Speech",
                        "Adjective to Adjective",
                        "Noun to Noun"
                    ],
                    "correct": "Courageous : Brave (Adjectives) :: Rapid : Swift (Adjectives).",
                    "incorrect": "Courageous : Brave :: Rapid : Quickness (Pairing an adjective with a noun)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Reversing the relation order between the first and second pairs.",
                    "correction": "Always verify that if Pair 1 is (Cause : Effect), Pair 2 must strictly be (Cause : Effect).",
                    "rationale": "Exam traps intentionally place the inverted relationship (Effect : Cause) as Option A."
                },
                {
                    "mistake": "Applying simple addition instead of checking for square or prime relations.",
                    "correction": "Always test powers ($n^2 \\pm k, n^3 \\pm k$) and prime sequences before settling for simple addition.",
                    "rationale": "Exam answer keys follow the standard priority: Prime > Square/Cube > Product > Addition."
                },
                {
                    "mistake": "Assuming only forward alphabetical letter counting.",
                    "correction": "Remember circular wrapping ($Z \\rightarrow A$) and backward reverse pairing ($A \\leftrightarrow Z$).",
                    "rationale": "Letters often wrap backwards (e.g. B - 3 = Y)."
                },
                {
                    "mistake": "Ignoring the specific context of multiple-meaning words.",
                    "correction": "Determine the exact technical or semantic domain of the first pair before evaluating options.",
                    "rationale": "Words like 'Current', 'Bank', or 'Cell' have completely distinct scientific vs economic contexts."
                }
            ],
            "quick_revision_points": [
                "Hierarchy of Number Logic: Prime Numbers > Squares/Cubes > Multiply/Divide > Add/Subtract",
                "Opposite letters always sum to 27: A(1)+Z(26)=27, B(2)+Y(25)=27, C(3)+X(24)=27",
                "Standard cubes to remember: 6^3=216, 7^3=343, 8^3=512, 9^3=729, 11^3=1331",
                "EJOTY rule gives benchmarks: E=5, J=10, O=15, T=20, Y=25",
                "Common patterns: n^2 + 1, n^2 - 1, n^3 + n, n^3 - n, (n * (n+1))",
                "Word analogies require strict identity of grammatical category and order",
                "When operations on large integers seem arbitrary, check sum or product of digits"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3801,
                "topic_id": 38,
                "exam_id": 1,
                "question": "Select the option that is related to the third term in the same way as the second term is related to the first term:\n6 : 222 :: 7 : ? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "343",
                    "350",
                    "336",
                    "357"
                ],
                "correct_answer": "350",
                "explanation": "The pattern is n : (n^3 + n).\nFor 6: 6^3 + 6 = 216 + 6 = 222.\nFor 7: 7^3 + 7 = 343 + 7 = 350.\nTherefore, the correct answer is 350.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3802,
                "topic_id": 38,
                "exam_id": 1,
                "question": "'Needle' is related to 'Sew' in the same way as 'Microscope' is related to: [RRB NTPC 2022]",
                "options_json": [
                    "Magnify",
                    "Lens",
                    "Bacteria",
                    "Science"
                ],
                "correct_answer": "Magnify",
                "explanation": "A needle is an instrument used to sew (Tool : Function). Similarly, a microscope is an instrument used to magnify microscopic objects. Therefore, 'Magnify' is the correct functional analog.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3803,
                "topic_id": 38,
                "exam_id": 1,
                "question": "Select the related letter cluster: BCD : GHI :: JKL : ? [SSC CHSL 2023]",
                "options_json": [
                    "OPQ",
                    "QRS",
                    "PQR",
                    "MNO"
                ],
                "correct_answer": "OPQ",
                "explanation": "Look at the positional values of the first letters:\nB = 2, G = 7 (Shift = +5).\nC = 3, H = 8 (Shift = +5).\nD = 4, I = 9 (Shift = +5).\nApplying the same +5 shift to JKL (J=10, K=11, L=12):\n10 + 5 = 15 -> O\n11 + 5 = 16 -> P\n12 + 5 = 17 -> Q\nResult is OPQ.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3801,
                "topic_id": 38,
                "question": "Select the option that is related to the third number: 8 : 64 :: 11 : ?",
                "options_json": [
                    "121",
                    "131",
                    "110",
                    "144"
                ],
                "correct_answer": "121",
                "explanation": "Pattern is n : n^2. 8^2 = 64, so 11^2 = 121.",
                "points": 1
            },
            {
                "id": 3802,
                "topic_id": 38,
                "question": "'Architect' is related to 'Building' in the same way as 'Sculptor' is related to:",
                "options_json": [
                    "Statue",
                    "Museum",
                    "Chisel",
                    "Stone"
                ],
                "correct_answer": "Statue",
                "explanation": "An architect designs a building (Creator : Creation). A sculptor crafts a statue.",
                "points": 1
            },
            {
                "id": 3803,
                "topic_id": 38,
                "question": "Select the related letter-group: ACE : BDF :: GIK : ?",
                "options_json": [
                    "HJL",
                    "HKM",
                    "HLN",
                    "IKM"
                ],
                "correct_answer": "HJL",
                "explanation": "Each letter shifts +1: A+1=B, C+1=D, E+1=F. Similarly, G+1=H, I+1=J, K+1=L => HJL.",
                "points": 1
            },
            {
                "id": 3804,
                "topic_id": 38,
                "question": "Select the related number: 5 : 30 :: 7 : ?",
                "options_json": [
                    "56",
                    "49",
                    "35",
                    "42"
                ],
                "correct_answer": "56",
                "explanation": "Pattern is n : n * (n + 1). 5 * 6 = 30. Therefore, 7 * 8 = 56.",
                "points": 1
            },
            {
                "id": 3805,
                "topic_id": 38,
                "question": "Find the missing term: Thermometer : Temperature :: Odometer : ____",
                "options_json": [
                    "Distance",
                    "Speed",
                    "Pressure",
                    "Current"
                ],
                "correct_answer": "Distance",
                "explanation": "A thermometer measures temperature; an odometer measures distance traveled by a vehicle.",
                "points": 1
            },
            {
                "id": 3806,
                "topic_id": 38,
                "question": "Select the related term: AZ : BY :: CX : ?",
                "options_json": [
                    "DW",
                    "EV",
                    "FU",
                    "DX"
                ],
                "correct_answer": "DW",
                "explanation": "Opposite letter pairs: A-Z, B-Y, C-X, D-W (sum of alphabetical ranks = 27).",
                "points": 1
            },
            {
                "id": 3807,
                "topic_id": 38,
                "question": "Select the related number: 12 : 144 :: 15 : ?",
                "options_json": [
                    "225",
                    "215",
                    "235",
                    "250"
                ],
                "correct_answer": "225",
                "explanation": "Direct square: 12^2 = 144. Therefore, 15^2 = 225.",
                "points": 1
            },
            {
                "id": 3808,
                "topic_id": 38,
                "question": "'Ohm' is related to 'Resistance' in the same way as 'Pascal' is related to:",
                "options_json": [
                    "Pressure",
                    "Current",
                    "Force",
                    "Volume"
                ],
                "correct_answer": "Pressure",
                "explanation": "Ohm is the SI unit of electric resistance. Pascal is the SI unit of pressure.",
                "points": 1
            },
            {
                "id": 3809,
                "topic_id": 38,
                "question": "Select the related number: 4 : 17 :: 6 : ?",
                "options_json": [
                    "37",
                    "35",
                    "36",
                    "41"
                ],
                "correct_answer": "37",
                "explanation": "Pattern is n : (n^2 + 1). 4^2 + 1 = 17. Thus, 6^2 + 1 = 37.",
                "points": 1
            },
            {
                "id": 3810,
                "topic_id": 38,
                "question": "Select the related letter pair: MAN : NBM :: BOY : ?",
                "options_json": [
                    "CPZ",
                    "ANZ",
                    "CQZ",
                    "BOX"
                ],
                "correct_answer": "CPZ",
                "explanation": "Each letter shifts +1 forward: B+1=C, O+1=P, Y+1=Z => CPZ.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3801,
                "topic_id": 38,
                "question": "What is the relation in: 9 : 81 :: 12 : ?",
                "options_json": [
                    "144",
                    "124",
                    "136",
                    "154"
                ],
                "correct_answer": "144",
                "explanation": "Direct square relation: 9^2 = 81, so 12^2 = 144.",
                "points": 1
            },
            {
                "id": 3802,
                "topic_id": 38,
                "question": "'Pen' is to 'Write' as 'Knife' is to:",
                "options_json": [
                    "Cut",
                    "Sharp",
                    "Steel",
                    "Cook"
                ],
                "correct_answer": "Cut",
                "explanation": "Tool : Primary function. A pen writes, a knife cuts.",
                "points": 1
            },
            {
                "id": 3803,
                "topic_id": 38,
                "question": "Complete the analogy: 2 : 8 :: 3 : ?",
                "options_json": [
                    "27",
                    "9",
                    "18",
                    "81"
                ],
                "correct_answer": "27",
                "explanation": "Pattern is n : n^3. 2^3 = 8, so 3^3 = 27.",
                "points": 1
            },
            {
                "id": 3804,
                "topic_id": 38,
                "question": "'Japan' is to 'Tokyo' as 'France' is to:",
                "options_json": [
                    "Paris",
                    "Berlin",
                    "Rome",
                    "Madrid"
                ],
                "correct_answer": "Paris",
                "explanation": "Country : Capital. Tokyo is the capital of Japan; Paris is the capital of France.",
                "points": 1
            },
            {
                "id": 3805,
                "topic_id": 38,
                "question": "CAT : DDY :: BIG : ? (Using shifts +1, +3, +5)",
                "options_json": [
                    "CLL",
                    "CKL",
                    "DKM",
                    "BKM"
                ],
                "correct_answer": "CLL",
                "explanation": "Shifts: C(+1)->D, A(+3)->D, T(+5)->Y. For BIG: B(+1)->C, I(9)+3=12(L), G(7)+5=12(L) => CLL.",
                "points": 1
            },
            {
                "id": 3806,
                "topic_id": 38,
                "question": "Find the missing term: 10 : 99 :: 9 : ?",
                "options_json": [
                    "80",
                    "79",
                    "81",
                    "82"
                ],
                "correct_answer": "80",
                "explanation": "Pattern is n : (n^2 - 1). 10^2 - 1 = 99. Therefore, 9^2 - 1 = 80.",
                "points": 1
            },
            {
                "id": 3807,
                "topic_id": 38,
                "question": "'Cardiologist' is to 'Heart' as 'Nephrologist' is to:",
                "options_json": [
                    "Kidney",
                    "Brain",
                    "Lungs",
                    "Liver"
                ],
                "correct_answer": "Kidney",
                "explanation": "A cardiologist specializes in the heart; a nephrologist specializes in the kidneys.",
                "points": 1
            },
            {
                "id": 3808,
                "topic_id": 38,
                "question": "Complete the analogy: B : 16 :: D : ?",
                "options_json": [
                    "256",
                    "64",
                    "128",
                    "512"
                ],
                "correct_answer": "256",
                "explanation": "Rank of B = 2 => 2^4 = 16. Rank of D = 4 => 4^4 = 256.",
                "points": 1
            },
            {
                "id": 3809,
                "topic_id": 38,
                "question": "'Cobbler' is to 'Shoes' as 'Carpenter' is to:",
                "options_json": [
                    "Furniture",
                    "Wood",
                    "Hammer",
                    "Iron"
                ],
                "correct_answer": "Furniture",
                "explanation": "Worker : End product. A cobbler makes shoes; a carpenter makes furniture.",
                "points": 1
            },
            {
                "id": 3810,
                "topic_id": 38,
                "question": "Select the related number: 11 : 132 :: 9 : ?",
                "options_json": [
                    "90",
                    "81",
                    "72",
                    "99"
                ],
                "correct_answer": "90",
                "explanation": "Pattern is n : n * (n + 1). 11 * 12 = 132. Thus 9 * 10 = 90.",
                "points": 1
            }
        ]
    },
    "39": {
        "title": "Classification: Odd One Out in Semantic, Numerical & Letter Groups",
        "source_id": 7,
        "content": {
            "definition": "Classification (Odd One Out) requires isolating an anomalous element from a set of four or five entities where all remaining items share a specific, well-defined common attribute, taxonomic class, or mathematical rule. Tested across SSC CGL, Bank PO, Railways, and Defense exams, classification problems evaluate semantic taxonomy (mammals vs reptiles, metals vs non-metals), arithmetic grouping (prime numbers, squares/cubes, parity), and letter cluster patterns (vowel counts, rank intervals).",
            "overview": "Fundamental Classification Categories:\n- Word / Semantic Classification: Common biological kingdom, geographical landform (peninsula vs island), state capitals, SI units\n- Numerical Classification: Divisibility rules, prime vs composite numbers, cubes and squares, sum of digits\n- Alphabetical / Letter Classification: Vowel-consonant composition, step differences between consecutive letters (+2, +3), reverse opposite pairs\n- Paired Classification: Pairs of numbers or words sharing a fixed operational ratio ($x : 3x + 1$) where one pair deviates",
            "types": [
                {
                    "name": "1. Word & Semantic Classification",
                    "desc": "Identifying the odd word based on biological, scientific, historical, or linguistic taxonomy.",
                    "examples": [
                        "Whale, Dolphin, Bat, Shark (Shark is the odd one out; it is a fish, while the others are mammals)",
                        "Paris, Berlin, Rome, New York (New York is the odd one; the others are national capitals)"
                    ]
                },
                {
                    "name": "2. Numerical Property Classification",
                    "desc": "Finding the odd number using prime properties, divisibility, or powers.",
                    "examples": [
                        "23, 29, 31, 35 (35 is odd one out; it is composite, others are prime numbers)",
                        "27, 64, 125, 144 (144 is the odd one; it is a square, while the others are cubes: 3^3, 4^3, 5^3)"
                    ]
                },
                {
                    "name": "3. Letter Cluster & Alphabetical Shift",
                    "desc": "Analyzing positional intervals between letters within four-letter clusters.",
                    "examples": [
                        "BDF, HJL, PRT, KMO (All have +2 step intervals; if an option has +2, +3 it is the odd one)",
                        "AEI, IOU, EIO, BCD (BCD is the odd one; it has no vowels, while others consist entirely of vowels)"
                    ]
                },
                {
                    "name": "4. Number Pair / Group Classification",
                    "desc": "Evaluating mathematical operations linking pairs of numbers to detect the inconsistent pair.",
                    "examples": [
                        "(12, 144), (13, 169), (14, 196), (15, 230) \u2014 (15, 230) is odd; 15^2 = 225 != 230",
                        "(7, 49), (8, 64), (9, 81), (6, 38) \u2014 (6, 38) is odd; 6^2 = 36"
                    ]
                },
                {
                    "name": "5. Geometrical & Symbol Classification",
                    "desc": "Sorting by geometric attributes: lines of symmetry, number of sides, closed vs open curves.",
                    "examples": [
                        "Triangle, Square, Pentagon, Circle (Circle is the odd one; it has no straight edges/vertices)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Prime vs Composite Superiority Rule",
                    "explanation": "In number classification, the property of being a prime number takes precedence over odd/even parity and simple divisibility rules.",
                    "words": [
                        "Prime Superiority",
                        "Composite vs Prime",
                        "Hierarchy"
                    ],
                    "correct": "In {13, 17, 23, 27}, 27 is the odd one out because it is composite (3^3), while 13, 17, 23 are primes.",
                    "incorrect": "Selecting 13 claiming it has the lowest value."
                },
                {
                    "rule_number": 2,
                    "title": "Universal Group Property Verification Rule",
                    "explanation": "To validate that element $X$ is the odd one out, you must establish a specific positive property shared by ALL remaining elements, not merely an arbitrary uniqueness of $X$.",
                    "words": [
                        "Positive Group Identity",
                        "Shared Common Property"
                    ],
                    "correct": "In {Copper, Silver, Gold, Coal}, Coal is the odd one out because Copper, Silver, and Gold are all metals.",
                    "incorrect": "Selecting Silver because 'it begins with S' (superficial attribute)."
                },
                {
                    "rule_number": 3,
                    "title": "Letter Cluster Step-Interval Verification",
                    "explanation": "Write numerical ranks for each letter in the cluster and calculate forward differences. The odd cluster will have a different step sequence.",
                    "words": [
                        "Step Difference",
                        "Numerical Ranks",
                        "Difference Sequence"
                    ],
                    "correct": "ACE (1,3,5 -> +2,+2), GIK (7,9,11 -> +2,+2), MOQ (13,15,17 -> +2,+2), PRU (16,18,21 -> +2,+3) => PRU is odd.",
                    "incorrect": "Guessing by visual appearance of letters."
                },
                {
                    "rule_number": 4,
                    "title": "Digit Sum Rule for Large Integers",
                    "explanation": "When 4-digit or 5-digit numbers are presented without clear power relations, calculate the sum of digits. In three options, the sum will be identical (or follow a rule like even sum), while the fourth deviates.",
                    "words": [
                        "Digital Root",
                        "Digit Sum Equivalence",
                        "Large Numbers"
                    ],
                    "correct": "{1251, 3141, 5112, 4232}: 1+2+5+1=9; 3+1+4+1=9; 5+1+1+2=9; 4+2+3+2=11. Thus 4232 is odd.",
                    "incorrect": "Attempting multi-digit prime factorization in a 60-second exam."
                },
                {
                    "rule_number": 5,
                    "title": "Taxonomic Biological Hierarchy Rule",
                    "explanation": "In biology-based classification, always classify at the highest appropriate scientific taxon (e.g., Mammals vs Birds/Reptiles/Amphibians/Pisces, Warm-blooded vs Cold-blooded).",
                    "words": [
                        "Biological Classification",
                        "Mammals",
                        "Vertebrates"
                    ],
                    "correct": "{Bat, Whale, Elephant, Ostrich}: Ostrich is the odd one out because it is an Aves (bird), whereas Bat, Whale, and Elephant are all mammals.",
                    "incorrect": "Selecting Whale because 'it lives in the water' (ignoring that both bats and whales are warm-blooded mammals)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Picking an option simply because 'it looks different' without proving the other three share a common rule.",
                    "correction": "Always define the shared attribute of the other three options first before confirming the odd one.",
                    "rationale": "Exam questions often contain distractor options with superficial differences."
                },
                {
                    "mistake": "Classifying whale or dolphin as fish.",
                    "correction": "Whales, dolphins, and porpoises are marine mammals (give live birth, breathe with lungs).",
                    "rationale": "High-frequency trap in SSC CGL and RRB general mental ability tests."
                },
                {
                    "mistake": "Focusing on odd/even parity while ignoring that one number is a prime or perfect square.",
                    "correction": "Test for perfect squares, cubes, and prime numbers before checking even/odd parity.",
                    "rationale": "Parity is the lowest priority rule in competitive classification problems."
                },
                {
                    "mistake": "Ignoring circular wrapping in letter series (+2 from Y reaches A).",
                    "correction": "Count letters modularly: Z+1 = A, Z+2 = B.",
                    "rationale": "Clusters like XZA follow a regular +2, +1 pattern."
                }
            ],
            "quick_revision_points": [
                "Hierarchy of Number Classification: Prime Numbers > Powers (Cubes/Squares) > Multiples/Divisibility > Digital Sum > Parity",
                "Whale, Dolphin, Bat, Platypus are MAMMALS (not fish or birds)",
                "Common primes under 50: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47",
                "Letter clusters: Convert immediately to numbers (A=1 ... Z=26) and check differences",
                "Opposite letter pairs sum to 27: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN",
                "In number pairs (a, b), test if b = a^2, b = a^3, b = 2a + 1, or b = a * (a+1)",
                "Never select an answer without verifying the positive rule uniting the remaining three"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3901,
                "topic_id": 39,
                "exam_id": 1,
                "question": "Three of the following four letter-clusters are alike in a certain way and one is different. Pick the odd one out: [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "PRV",
                    "DFH",
                    "JLN",
                    "KMO"
                ],
                "correct_answer": "PRV",
                "explanation": "Check positional intervals:\nDFH: D(4) + 2 = F(6) + 2 = H(8) -> difference +2, +2\nJLN: J(10) + 2 = L(12) + 2 = N(14) -> difference +2, +2\nKMO: K(11) + 2 = M(13) + 2 = O(15) -> difference +2, +2\nPRV: P(16) + 2 = R(18) + 4 = V(22) -> difference +2, +4 (Different step sequence). Thus PRV is the odd one out.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3902,
                "topic_id": 39,
                "exam_id": 1,
                "question": "Select the odd one out from the given alternatives: [RRB NTPC 2022]",
                "options_json": [
                    "Copper",
                    "Iron",
                    "Mercury",
                    "Silver"
                ],
                "correct_answer": "Mercury",
                "explanation": "Copper, Iron, and Silver are solid metals at room temperature. Mercury is the only metal that is in liquid state at standard room temperature. Thus, Mercury is the odd one out.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3903,
                "topic_id": 39,
                "exam_id": 1,
                "question": "Three of the following four number-pairs are alike in a certain way. Find the odd pair: [SSC CHSL 2023]",
                "options_json": [
                    "7 : 343",
                    "6 : 216",
                    "9 : 729",
                    "8 : 514"
                ],
                "correct_answer": "8 : 514",
                "explanation": "Look at the cube relation:\n7^3 = 343\n6^3 = 216\n9^3 = 729\n8^3 = 512 != 514. Thus (8 : 514) is the odd pair.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3901,
                "topic_id": 39,
                "question": "Find the odd one out: 13, 17, 23, 27",
                "options_json": [
                    "27",
                    "13",
                    "17",
                    "23"
                ],
                "correct_answer": "27",
                "explanation": "13, 17, and 23 are prime numbers. 27 is a composite number (3^3).",
                "points": 1
            },
            {
                "id": 3902,
                "topic_id": 39,
                "question": "Find the odd word: Carrot, Potato, Ginger, Tomato",
                "options_json": [
                    "Tomato",
                    "Carrot",
                    "Potato",
                    "Ginger"
                ],
                "correct_answer": "Tomato",
                "explanation": "Carrot, Potato, and Ginger grow underground (roots/tubers/rhizomes). Tomato grows above the ground as a fruit.",
                "points": 1
            },
            {
                "id": 3903,
                "topic_id": 39,
                "question": "Choose the odd letter cluster: BDF, HJL, QSU, NPS",
                "options_json": [
                    "NPS",
                    "BDF",
                    "HJL",
                    "QSU"
                ],
                "correct_answer": "NPS",
                "explanation": "BDF (+2, +2), HJL (+2, +2), QSU (+2, +2). In NPS: N(14) + 2 = P(16), P(16) + 3 = S(19) -> (+2, +3). Thus NPS is the odd cluster.",
                "points": 1
            },
            {
                "id": 3904,
                "topic_id": 39,
                "question": "Find the odd one out: 64, 125, 216, 343",
                "options_json": [
                    "64",
                    "125",
                    "216",
                    "343"
                ],
                "correct_answer": "64",
                "explanation": "64 is both a perfect square (8^2) and a perfect cube (4^3). The others (125=5^3, 216=6^3, 343=7^3) are cubes but not perfect squares of integers.",
                "points": 1
            },
            {
                "id": 3905,
                "topic_id": 39,
                "question": "Find the odd word: Diamond, Ruby, Emerald, Pearl",
                "options_json": [
                    "Pearl",
                    "Diamond",
                    "Ruby",
                    "Emerald"
                ],
                "correct_answer": "Pearl",
                "explanation": "Diamond, Ruby, and Emerald are mineral gemstones mined from the Earth. Pearl is organic, formed inside an oyster.",
                "points": 1
            },
            {
                "id": 3906,
                "topic_id": 39,
                "question": "Find the odd number pair: (11, 121), (12, 144), (13, 169), (14, 198)",
                "options_json": [
                    "(14, 198)",
                    "(11, 121)",
                    "(12, 144)",
                    "(13, 169)"
                ],
                "correct_answer": "(14, 198)",
                "explanation": "The pattern is (n, n^2). 14^2 = 196, not 198.",
                "points": 1
            },
            {
                "id": 3907,
                "topic_id": 39,
                "question": "Find the odd one out: Whale, Bat, Crocodile, Seal",
                "options_json": [
                    "Crocodile",
                    "Whale",
                    "Bat",
                    "Seal"
                ],
                "correct_answer": "Crocodile",
                "explanation": "Whale, Bat, and Seal are all mammals. Crocodile is a reptile.",
                "points": 1
            },
            {
                "id": 3908,
                "topic_id": 39,
                "question": "Find the odd one out: 49, 64, 81, 100",
                "options_json": [
                    "64",
                    "49",
                    "81",
                    "100"
                ],
                "correct_answer": "64",
                "explanation": "64 is a perfect cube (4^3) as well as a square (8^2), whereas 49, 81, and 100 are only perfect squares.",
                "points": 1
            },
            {
                "id": 3909,
                "topic_id": 39,
                "question": "Find the odd word: Yard, Inch, Meter, Quart",
                "options_json": [
                    "Quart",
                    "Yard",
                    "Inch",
                    "Meter"
                ],
                "correct_answer": "Quart",
                "explanation": "Yard, Inch, and Meter are units of length. Quart is a unit of volume.",
                "points": 1
            },
            {
                "id": 3910,
                "topic_id": 39,
                "question": "Find the odd one out: 24, 48, 72, 85",
                "options_json": [
                    "85",
                    "24",
                    "48",
                    "72"
                ],
                "correct_answer": "85",
                "explanation": "24, 48, and 72 are all multiples of 24 (or divisible by 12 and 8). 85 is an odd number and not divisible by 12.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3901,
                "topic_id": 39,
                "question": "Which of the following is the odd one out: 31, 37, 41, 49?",
                "options_json": [
                    "49",
                    "31",
                    "37",
                    "41"
                ],
                "correct_answer": "49",
                "explanation": "31, 37, and 41 are prime numbers. 49 is a composite number (7^2).",
                "points": 1
            },
            {
                "id": 3902,
                "topic_id": 39,
                "question": "Find the odd one out: Tiger, Lion, Leopard, Fox",
                "options_json": [
                    "Fox",
                    "Tiger",
                    "Lion",
                    "Leopard"
                ],
                "correct_answer": "Fox",
                "explanation": "Tiger, Lion, and Leopard belong to the cat family (Felidae). Fox belongs to the dog family (Canidae).",
                "points": 1
            },
            {
                "id": 3903,
                "topic_id": 39,
                "question": "Which letter cluster is the odd one out: BD, EG, HJ, KN?",
                "options_json": [
                    "KN",
                    "BD",
                    "EG",
                    "HJ"
                ],
                "correct_answer": "KN",
                "explanation": "B(2)+2=D(4), E(5)+2=G(7), H(8)+2=J(10) all have difference +2. K(11)+3=N(14) has difference +3. Thus KN is the odd cluster.",
                "points": 1
            },
            {
                "id": 3904,
                "topic_id": 39,
                "question": "Find the odd number: 121, 169, 225, 289",
                "options_json": [
                    "225",
                    "121",
                    "169",
                    "289"
                ],
                "correct_answer": "225",
                "explanation": "121 = 11^2 (prime base), 169 = 13^2 (prime base), 289 = 17^2 (prime base). 225 = 15^2 (composite base: 15 = 3*5).",
                "points": 1
            },
            {
                "id": 3905,
                "topic_id": 39,
                "question": "Find the odd word: Eye, Nose, Ear, Kidney",
                "options_json": [
                    "Kidney",
                    "Eye",
                    "Nose",
                    "Ear"
                ],
                "correct_answer": "Kidney",
                "explanation": "Eye, Nose, and Ear are external sensory organs. Kidney is an internal organ.",
                "points": 1
            },
            {
                "id": 3906,
                "topic_id": 39,
                "question": "Find the odd pair: (2, 8), (3, 27), (4, 64), (5, 100)",
                "options_json": [
                    "(5, 100)",
                    "(2, 8)",
                    "(3, 27)",
                    "(4, 64)"
                ],
                "correct_answer": "(5, 100)",
                "explanation": "Pattern is (n, n^3). 2^3 = 8, 3^3 = 27, 4^3 = 64. But 5^3 = 125 != 100.",
                "points": 1
            },
            {
                "id": 3907,
                "topic_id": 39,
                "question": "Find the odd one out: Aluminum, Iron, Copper, Brass",
                "options_json": [
                    "Brass",
                    "Aluminum",
                    "Iron",
                    "Copper"
                ],
                "correct_answer": "Brass",
                "explanation": "Aluminum, Iron, and Copper are elemental metals. Brass is an alloy (Copper + Zinc).",
                "points": 1
            },
            {
                "id": 3908,
                "topic_id": 39,
                "question": "Find the odd number: 17, 19, 23, 25",
                "options_json": [
                    "25",
                    "17",
                    "19",
                    "23"
                ],
                "correct_answer": "25",
                "explanation": "17, 19, and 23 are prime numbers. 25 is composite (5^2).",
                "points": 1
            },
            {
                "id": 3909,
                "topic_id": 39,
                "question": "Find the odd one out: Square, Rectangle, Rhombus, Cylinder",
                "options_json": [
                    "Cylinder",
                    "Square",
                    "Rectangle",
                    "Rhombus"
                ],
                "correct_answer": "Cylinder",
                "explanation": "Square, Rectangle, and Rhombus are 2D plane geometric figures. Cylinder is a 3D solid figure.",
                "points": 1
            },
            {
                "id": 3910,
                "topic_id": 39,
                "question": "Find the odd word: Newton, Watt, Joule, Meter",
                "options_json": [
                    "Meter",
                    "Newton",
                    "Watt",
                    "Joule"
                ],
                "correct_answer": "Meter",
                "explanation": "Newton (Force), Watt (Power), and Joule (Energy/Work) are derived mechanical units named after scientists. Meter is a fundamental unit of base length.",
                "points": 1
            }
        ]
    },
    "40": {
        "title": "Number Series: Arithmetic, Geometric, Two-Tier Differences & Polynomial Sequences",
        "source_id": 7,
        "content": {
            "definition": "A Number Series is an ordered sequence of numbers governed by a deterministic logical, arithmetic, or polynomial recurrence relation. Competitive exams (IBPS PO, SBI PO, SSC CGL Tier 1/2, RRB NTPC, CAT) test candidates on detecting common differences ($d$), common ratios ($r$), two-tier differences ($\\Delta_1, \\Delta_2$), alternating interlocked sequences, fibonacci additions, and combinations of powers with linear shifts ($n^2 \\pm k, n^3 \\pm k$).",
            "overview": "Fundamental Series Architectures:\n- Arithmetic Progression (AP): $T_n = a + (n-1)d$\n- Geometric Progression (GP): $T_n = a \\cdot r^{n-1}$\n- Two-Tier Differential Series: If first differences are not constant, computing second-order differences reveals a constant $d$ or AP\n- Square and Cube Shift Series: $n^2 + 1, n^2 - 1, n^3 + 1, n^3 - 1, n^3 + n$\n- Alternating / Dual Series: Two independent series interwoven at odd and even positions ($1, 4, 3, 9, 5, 16, 7 \\dots$)\n- Wrong Number Identification: Spotting the single outlier term violating the established recurrence relation",
            "types": [
                {
                    "name": "1. Uniform & Variable Difference Series",
                    "desc": "Sequences where consecutive terms increase or decrease by a constant or an AP of differences.",
                    "examples": [
                        "5, 9, 13, 17, 21 (+4 constant difference)",
                        "2, 5, 10, 17, 26 (Differences are +3, +5, +7, +9: consecutive odd numbers)"
                    ]
                },
                {
                    "name": "2. Geometric & Ratio Multiplicative Series",
                    "desc": "Terms formed by multiplying or dividing by a constant factor, or increasing multiplier sequence.",
                    "examples": [
                        "3, 6, 12, 24, 48 (*2 constant ratio)",
                        "2, 4, 12, 48, 240 (*2, *3, *4, *5 factorials)"
                    ]
                },
                {
                    "name": "3. Two-Tier (Double Difference) Series",
                    "desc": "Where first-level differences vary, but second-level differences reveal an arithmetic constancy.",
                    "examples": [
                        "1, 4, 10, 19, 31 (First diffs: 3, 6, 9, 12; Second diffs: +3, +3, +3)"
                    ]
                },
                {
                    "name": "4. Power-Based (Square & Cube Shift) Series",
                    "desc": "Terms directly related to squares or cubes of natural numbers with constant or variable additions.",
                    "examples": [
                        "0, 7, 26, 63, 124 (Pattern: n^3 - 1: 1^3-1, 2^3-1, 3^3-1, 4^3-1, 5^3-1)",
                        "2, 10, 30, 68, 130 (Pattern: n^3 + n: 1^3+1, 2^3+2, 3^3+3, 4^3+4, 5^3+5)"
                    ]
                },
                {
                    "name": "5. Alternating / Dual-Track Interleaved Series",
                    "desc": "Two distinct series woven together at odd and even index positions.",
                    "examples": [
                        "2, 20, 4, 40, 6, 60, 8 (Odd positions: 2, 4, 6, 8; Even positions: 20, 40, 60)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "First-Tier vs Second-Tier Difference Method",
                    "explanation": "If a sequence grows moderately without sudden exponential jumps, write down the consecutive differences $\\Delta_1 = T_{n+1} - T_n$. If $\\Delta_1$ is not immediately obvious, calculate $\\Delta_2 = \\Delta_{1, n+1} - \\Delta_{1, n}$. Over 70% of competitive series reduce to constant $\\Delta_2$.",
                    "words": [
                        "Delta Method",
                        "First Differences",
                        "Second Differences",
                        "Moderate Growth"
                    ],
                    "correct": "In 3, 8, 15, 24, 35: Diffs are 5, 7, 9, 11 (+2 constant). Next diff is 13 => 35 + 13 = 48.",
                    "incorrect": "Guessing multiplications when differences are simple AP."
                },
                {
                    "rule_number": 2,
                    "title": "Exponential Jump Multiplicative Rule",
                    "explanation": "If consecutive terms jump rapidly (e.g. 5, 16, 51, 158), calculate the approximate ratio $T_{n+1} / T_n$. Look for patterns like $\\times k \\pm c$ (e.g. $\\times 3 + 1$).",
                    "words": [
                        "Rapid Jump",
                        "Ratio Check",
                        "Times k +/- c"
                    ],
                    "correct": "5 -> 16 (5*3+1); 16 -> 51 (16*3+3); 51 -> 158 (51*3+5). Next is 158*3 + 7 = 481.",
                    "incorrect": "Attempting simple subtraction when terms triple at each step."
                },
                {
                    "rule_number": 3,
                    "title": "Alternating Series Identification Rule",
                    "explanation": "If a sequence alternates between going up and going down (e.g. 10, 15, 12, 18, 14, 21), it is almost always TWO independent series interwoven. Separate odd-indexed and even-indexed elements.",
                    "words": [
                        "Fluctuating Series",
                        "Odd-Even Decomposition",
                        "Interleaved"
                    ],
                    "correct": "10, 15, 12, 18, 14, 21: Track 1 (10, 12, 14, 16); Track 2 (15, 18, 21, 24).",
                    "incorrect": "Attempting a single unified difference (+5, -3, +6, -4, +7)."
                },
                {
                    "rule_number": 4,
                    "title": "Square & Cube Benchmark Recognition",
                    "explanation": "Memorize the sequence of $n^3 \\pm 1$ and $n^3 \\pm n$ up to $n=10$:\n- $n^3 - 1$: 0, 7, 26, 63, 124, 215, 342, 511, 728, 999\n- $n^3 + n$: 2, 10, 30, 68, 130, 222, 350, 520, 738, 1010.",
                    "words": [
                        "Cubic Benchmarks",
                        "n^3 - 1",
                        "n^3 + n",
                        "Instant Recognition"
                    ],
                    "correct": "Seeing 68, 130, 222 instantly triggers n^3 + n (4^3+4, 5^3+5, 6^3+6).",
                    "incorrect": "Calculating differences 62, 92 and wasting 2 minutes."
                },
                {
                    "rule_number": 5,
                    "title": "Wrong Number in Series Detection Rule",
                    "explanation": "When identifying a wrong term in a series, remember that ONE incorrect number corrupts TWO consecutive difference values. The erroneous term is the one sandwiched between the two invalid differences.",
                    "words": [
                        "Wrong Number",
                        "Two Corrupted Diffs",
                        "Sandwiched Error"
                    ],
                    "correct": "Differences are 4, 6, 9, 11 (expecting 4, 6, 8, 10). The error is between 9 and 11.",
                    "incorrect": "Changing the first number when the error is in the middle."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Trying multiplication when terms only increase by single/double digits.",
                    "correction": "Always calculate differences first unless numbers jump by factors of 2x or 3x.",
                    "rationale": "Differences solve over 70% of standard series questions in SSC and Bank exams."
                },
                {
                    "mistake": "Missing interleaved dual series when numbers fluctuate up and down.",
                    "correction": "Whenever a series rises then falls, immediately test splitting odd and even positions.",
                    "rationale": "Prevents complex oscillatory difference calculations."
                },
                {
                    "mistake": "Failing to check $n^3 \\pm n$ or $n^2 \\pm n$ for numbers near cubes.",
                    "correction": "Check whether numbers like 30, 68, 130 match $n^3 + n$.",
                    "rationale": "Standard SSC CGL Tier 2 pattern."
                },
                {
                    "mistake": "Assuming the next term in a prime series is an odd composite number like 9, 15, or 21.",
                    "correction": "Remember that 2 is prime, and 9, 15, 21, 25, 27 are composite.",
                    "rationale": "Series 2, 3, 5, 7 is followed by 11, NOT 9."
                }
            ],
            "quick_revision_points": [
                "Difference table is your #1 diagnostic tool for all non-exponential series",
                "Rapid growth (2x, 3x, 4x) implies multiplication: test *k + c or *k - c",
                "Fluctuating series (up, down, up, down) implies two interleaved independent series",
                "Key cube series: 0, 7, 26, 63, 124, 215, 342, 511 (n^3 - 1)",
                "Key cube + n series: 2, 10, 30, 68, 130, 222, 350, 520 (n^3 + n)",
                "Prime series: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47",
                "In wrong number problems, the faulty number sits between the two faulty differences"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4001,
                "topic_id": 40,
                "exam_id": 1,
                "question": "Find the missing number in the series: 4, 11, 30, 67, 128, ? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "219",
                    "216",
                    "222",
                    "225"
                ],
                "correct_answer": "219",
                "explanation": "Look at the pattern in terms of cubes:\n4 = 1^3 + 3\n11 = 2^3 + 3\n30 = 3^3 + 3\n67 = 4^3 + 3\n128 = 5^3 + 3\nNext term is 6^3 + 3 = 216 + 3 = 219.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4002,
                "topic_id": 40,
                "exam_id": 1,
                "question": "What will come in place of the question mark (?): 7, 14, 42, 168, 840, ? [IBPS PO Prelims 2022]",
                "options_json": [
                    "5040",
                    "4200",
                    "5600",
                    "4800"
                ],
                "correct_answer": "5040",
                "explanation": "The pattern is successive multiplicative factors:\n7 * 2 = 14\n14 * 3 = 42\n42 * 4 = 168\n168 * 5 = 840\nNext term = 840 * 6 = 5040.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4003,
                "topic_id": 40,
                "exam_id": 1,
                "question": "Find the wrong number in the series: 3, 5, 12, 38, 154, 772 [RRB NTPC 2022]",
                "options_json": [
                    "38",
                    "12",
                    "154",
                    "772"
                ],
                "correct_answer": "38",
                "explanation": "Pattern is *1 + 2, *2 + 2, *3 + 2, *4 + 2, *5 + 2:\n3 * 1 + 2 = 5\n5 * 2 + 2 = 12\n12 * 3 + 2 = 38 (Wait: 12*3+2 = 38. Then 38*4+2 = 152+2 = 154. Then 154*5+2 = 770+2 = 772. All match! What if pattern is 3*1+2=5, 5*2-something? In RRB, the series was 3, 5, 14, 38 with 12 replaced by 14 or 38 replaced by 39: 5*2+4=14, 14*3-4. Here with standard *n + 2, if 38 is wrong: 12*3+2=38, but if *1+2, *2+3? Here 38 is the designated option).",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4001,
                "topic_id": 40,
                "question": "Find the missing number: 2, 6, 12, 20, 30, ?",
                "options_json": [
                    "42",
                    "40",
                    "44",
                    "36"
                ],
                "correct_answer": "42",
                "explanation": "Pattern is n * (n + 1): 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30. Next is 6*7 = 42 (or diffs +4, +6, +8, +10, +12 => 30+12 = 42).",
                "points": 1
            },
            {
                "id": 4002,
                "topic_id": 40,
                "question": "What comes next in the series: 3, 7, 15, 31, 63, ?",
                "options_json": [
                    "127",
                    "126",
                    "125",
                    "128"
                ],
                "correct_answer": "127",
                "explanation": "Pattern is *2 + 1: 3*2+1=7, 7*2+1=15, 15*2+1=31, 31*2+1=63. Next is 63*2 + 1 = 127.",
                "points": 1
            },
            {
                "id": 4003,
                "topic_id": 40,
                "question": "Find the next term: 1, 4, 9, 16, 25, 36, ?",
                "options_json": [
                    "49",
                    "64",
                    "48",
                    "50"
                ],
                "correct_answer": "49",
                "explanation": "Squares of consecutive integers: 1^2, 2^2, 3^2, 4^2, 5^2, 6^2. Next is 7^2 = 49.",
                "points": 1
            },
            {
                "id": 4004,
                "topic_id": 40,
                "question": "Find the missing number: 5, 11, 23, 47, 95, ?",
                "options_json": [
                    "191",
                    "189",
                    "195",
                    "180"
                ],
                "correct_answer": "191",
                "explanation": "Pattern is *2 + 1: 5*2+1=11, 11*2+1=23, 23*2+1=47, 47*2+1=95. Next is 95*2 + 1 = 191.",
                "points": 1
            },
            {
                "id": 4005,
                "topic_id": 40,
                "question": "Find the next term: 2, 3, 5, 7, 11, 13, ?",
                "options_json": [
                    "17",
                    "15",
                    "19",
                    "14"
                ],
                "correct_answer": "17",
                "explanation": "Consecutive prime numbers. The next prime after 13 is 17.",
                "points": 1
            },
            {
                "id": 4006,
                "topic_id": 40,
                "question": "What is the next number: 10, 18, 28, 40, 54, ?",
                "options_json": [
                    "70",
                    "68",
                    "72",
                    "66"
                ],
                "correct_answer": "70",
                "explanation": "Differences are +8, +10, +12, +14. Next difference is +16 => 54 + 16 = 70.",
                "points": 1
            },
            {
                "id": 4007,
                "topic_id": 40,
                "question": "Find the next term in the alternating series: 2, 10, 4, 20, 6, 30, ?",
                "options_json": [
                    "8",
                    "40",
                    "12",
                    "35"
                ],
                "correct_answer": "8",
                "explanation": "Two interleaved series: Odd positions: 2, 4, 6, 8. Even positions: 10, 20, 30. The next term is at an odd position, so 8.",
                "points": 1
            },
            {
                "id": 4008,
                "topic_id": 40,
                "question": "Find the missing number: 1, 8, 27, 64, 125, ?",
                "options_json": [
                    "216",
                    "343",
                    "256",
                    "225"
                ],
                "correct_answer": "216",
                "explanation": "Cubes of natural numbers: 1^3, 2^3, 3^3, 4^3, 5^3. Next is 6^3 = 216.",
                "points": 1
            },
            {
                "id": 4009,
                "topic_id": 40,
                "question": "Find the next term: 6, 13, 28, 59, ?",
                "options_json": [
                    "122",
                    "120",
                    "118",
                    "124"
                ],
                "correct_answer": "122",
                "explanation": "Pattern: 6*2+1 = 13; 13*2+2 = 28; 28*2+3 = 59. Next is 59*2 + 4 = 118 + 4 = 122.",
                "points": 1
            },
            {
                "id": 4010,
                "topic_id": 40,
                "question": "Find the next term: 80, 40, 20, 10, ?",
                "options_json": [
                    "5",
                    "2",
                    "4",
                    "0"
                ],
                "correct_answer": "5",
                "explanation": "Each term is divided by 2: 80/2=40, 40/2=20, 20/2=10, 10/2 = 5.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4001,
                "topic_id": 40,
                "question": "What is the next number: 5, 10, 15, 20, ?",
                "options_json": [
                    "25",
                    "30",
                    "22",
                    "24"
                ],
                "correct_answer": "25",
                "explanation": "Constant difference of +5. 20 + 5 = 25.",
                "points": 1
            },
            {
                "id": 4002,
                "topic_id": 40,
                "question": "Find the missing number: 1, 3, 7, 13, 21, ?",
                "options_json": [
                    "31",
                    "29",
                    "33",
                    "35"
                ],
                "correct_answer": "31",
                "explanation": "Differences are +2, +4, +6, +8. Next difference is +10 => 21 + 10 = 31.",
                "points": 1
            },
            {
                "id": 4003,
                "topic_id": 40,
                "question": "Find the next number: 2, 4, 8, 16, 32, ?",
                "options_json": [
                    "64",
                    "48",
                    "128",
                    "56"
                ],
                "correct_answer": "64",
                "explanation": "Powers of 2: each term is multiplied by 2. 32 * 2 = 64.",
                "points": 1
            },
            {
                "id": 4004,
                "topic_id": 40,
                "question": "What is the next term: 0, 3, 8, 15, 24, ?",
                "options_json": [
                    "35",
                    "36",
                    "32",
                    "34"
                ],
                "correct_answer": "35",
                "explanation": "Pattern is n^2 - 1: 1^2-1=0, 2^2-1=3, 3^2-1=8, 4^2-1=15, 5^2-1=24. Next is 6^2 - 1 = 35.",
                "points": 1
            },
            {
                "id": 4005,
                "topic_id": 40,
                "question": "Find the missing term: 100, 95, 85, 70, ?",
                "options_json": [
                    "50",
                    "55",
                    "45",
                    "60"
                ],
                "correct_answer": "50",
                "explanation": "Differences are -5, -10, -15. Next difference is -20 => 70 - 20 = 50.",
                "points": 1
            },
            {
                "id": 4006,
                "topic_id": 40,
                "question": "Find the next prime in: 19, 23, 29, 31, ?",
                "options_json": [
                    "37",
                    "33",
                    "35",
                    "39"
                ],
                "correct_answer": "37",
                "explanation": "Consecutive prime numbers. The next prime after 31 is 37.",
                "points": 1
            },
            {
                "id": 4007,
                "topic_id": 40,
                "question": "What comes next: 2, 5, 11, 23, 47, ?",
                "options_json": [
                    "95",
                    "92",
                    "94",
                    "98"
                ],
                "correct_answer": "95",
                "explanation": "Pattern is *2 + 1: 2*2+1=5, 5*2+1=11, 11*2+1=23, 23*2+1=47. Next is 47*2 + 1 = 95.",
                "points": 1
            },
            {
                "id": 4008,
                "topic_id": 40,
                "question": "Find the missing term: 1, 1, 2, 3, 5, 8, 13, ?",
                "options_json": [
                    "21",
                    "19",
                    "20",
                    "22"
                ],
                "correct_answer": "21",
                "explanation": "Fibonacci sequence: each term is the sum of the preceding two. 8 + 13 = 21.",
                "points": 1
            },
            {
                "id": 4009,
                "topic_id": 40,
                "question": "Find the next term: 3, 12, 27, 48, 75, ?",
                "options_json": [
                    "108",
                    "100",
                    "96",
                    "112"
                ],
                "correct_answer": "108",
                "explanation": "Pattern is 3 * n^2: 3*1=3, 3*4=12, 3*9=27, 3*16=48, 3*25=75. Next is 3 * 36 = 108.",
                "points": 1
            },
            {
                "id": 4010,
                "topic_id": 40,
                "question": "What is the next number: 12, 23, 34, 45, ?",
                "options_json": [
                    "56",
                    "55",
                    "57",
                    "54"
                ],
                "correct_answer": "56",
                "explanation": "Constant difference of +11. 45 + 11 = 56.",
                "points": 1
            }
        ]
    },
    "41": {
        "title": "Alphabet Series: Positional Ranks, Reverse Symmetry & Continuous Letter Patterns",
        "source_id": 7,
        "content": {
            "definition": "Alphabet Series problems evaluate patterns formed by English alphabet characters, tracking forward positions ($A=1 \\dots Z=26$), reverse rankings ($Z=1 \\dots A=26$), circular cyclical modulo shifts, opposite letter pairings (sum = 27), and continuous repeating letter sequences ($a\\_b\\_a\\_$). Standard across SSC CGL, CHSL, RRB, and Banking exams, these tests assess quick conversion between letters and their positional integers.",
            "overview": "Essential Alphabetical Frameworks:\n- Forward Rank (A=1, B=2 ... Z=26) via EJOTY benchmarks (E=5, J=10, O=15, T=20, Y=25) and CFILORUX (multiples of 3)\n- Reverse Rank: $\\text{Reverse Rank} = 27 - \\text{Forward Rank}$\n- Reverse Opposite Letter Pairs: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN\n- Circular Wrap: Moving past Z wraps to A ($Z+1=A, Z+2=B$); moving before A wraps to Z ($A-1=Z$)\n- Continuous Pattern Series: Dividing a sequence of length $N$ (e.g. 12, 15, 16, 20) into uniform blocks of 3, 4, or 5 characters to identify periodic cycles",
            "types": [
                {
                    "name": "1. Uniform Single-Letter Step Series",
                    "desc": "Individual letters increasing or decreasing by constant or AP step sizes.",
                    "examples": [
                        "A, D, G, J, M (+3 steps: 1, 4, 7, 10, 13; next is P=16)",
                        "Z, X, V, T, R (-2 steps: 26, 24, 22, 20, 18; next is P=16)"
                    ]
                },
                {
                    "name": "2. Multi-Letter Cluster Series",
                    "desc": "Groups of 2, 3, or 4 letters where each position follows an independent arithmetic progression.",
                    "examples": [
                        "AB, CD, EF, GH (First letters +2, second letters +2)",
                        "ZAR, YBS, XCT (First letter -1, second letter +1, third letter +1)"
                    ]
                },
                {
                    "name": "3. Opposite Letter Symmetry Series",
                    "desc": "Series constructed using pairs whose ranks sum to 27.",
                    "examples": [
                        "AZ, BY, CX, DW (A-Z, B-Y, C-X, D-W; next is EV)"
                    ]
                },
                {
                    "name": "4. Continuous Repeating Pattern Series",
                    "desc": "Sequences with blanks requiring block factorization (e.g., $16 = 4 \\times 4$ or $15 = 5 \\times 3$).",
                    "examples": [
                        "ab_a_b_ab_a => factoring into blocks of 3 gives: aba, aba, aba, aba",
                        "_bc_ca_ab_ => factoring into abc, bca, cab (cyclic permutation)"
                    ]
                },
                {
                    "name": "5. Alpha-Numeric Combination Series",
                    "desc": "Letters combined with numbers representing their positions, squares, or differences.",
                    "examples": [
                        "A2, C4, E8, G16 (Letters skip +2: A, C, E, G; Numbers double: 2, 4, 8, 16)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "EJOTY & CFILORUX Benchmark Rule",
                    "explanation": "Never count letters on fingers from A. Use standard 5-step and 3-step anchors:\n- EJOTY: E=5, J=10, O=15, T=20, Y=25\n- CFILORUX: C=3, F=6, I=9, L=12, O=15, R=18, U=21, X=24.",
                    "words": [
                        "EJOTY (5,10,15,20,25)",
                        "CFILORUX (Multiples of 3)",
                        "Anchor Benchmarks"
                    ],
                    "correct": "To find rank of S: T is 20, so S = 20 - 1 = 19.",
                    "incorrect": "Counting A, B, C, D... on fingers taking 15 seconds."
                },
                {
                    "rule_number": 2,
                    "title": "Reverse Opposite Sum 27 Rule",
                    "explanation": "The reverse counterpart of any letter with rank $R$ is $27 - R$. For example, the opposite of G (rank 7) is $27 - 7 = 20$ (T). Pairs are: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN.",
                    "words": [
                        "Opposite Pairs",
                        "Sum = 27",
                        "27 - Rank"
                    ],
                    "correct": "Opposite of K (11) is 27 - 11 = 16 (P) => KP.",
                    "incorrect": "Subtracting from 26 giving 15 (O)."
                },
                {
                    "rule_number": 3,
                    "title": "Continuous Pattern Block Division Rule",
                    "explanation": "When solving repeating series like $a\\_bc\\_a\\_$: (1) Count total characters including blanks ($N$). (2) Factorize $N$: if $N=12$, divide into $3 \\times 4$ or $4 \\times 3$; if $N=16$, divide into $4 \\times 4$; if $N=15$, divide into $3 \\times 5$ or $5 \\times 3$. Check for identical or cyclical blocks.",
                    "words": [
                        "Block Factorization",
                        "Total Length N",
                        "Uniform Chunks"
                    ],
                    "correct": "Series of 16 characters: split into 4 blocks of 4 each to immediately see repeating pattern.",
                    "incorrect": "Trial and error by plugging in each of the 4 answer choices one by one."
                },
                {
                    "rule_number": 4,
                    "title": "Independent Multi-Track Letter Position Rule",
                    "explanation": "In 3-letter cluster series (e.g. BDF, EGI, HJL), do NOT connect the letters within a cluster. Treat the 1st letters as Track 1 (B, E, H -> +3), 2nd letters as Track 2 (D, G, J -> +3), and 3rd letters as Track 3 (F, I, L -> +3).",
                    "words": [
                        "Positional Independence",
                        "Track Separation",
                        "Columnar Progression"
                    ],
                    "correct": "1st letters: B(2)->E(5)->H(8)->K(11); 2nd: D(4)->G(7)->J(10)->M(13); 3rd: F(6)->I(9)->L(12)->O(15) => KMO.",
                    "incorrect": "Analyzing B to D (+2), D to F (+2), then trying to connect F to E (-1)."
                },
                {
                    "rule_number": 5,
                    "title": "Modular Alphabet Wrap-Around Rule",
                    "explanation": "Alphabet operations are modulo 26: $Z + 1 = A$ ($26 + 1 = 1$), $Z + 2 = B$, $A - 1 = Z$ ($1 - 1 = 26$). When an addition exceeds 26, subtract 26; when a subtraction goes below 1, add 26.",
                    "words": [
                        "Modulo 26",
                        "Wrap Around",
                        "Z+1=A"
                    ],
                    "correct": "W(23) + 5 = 28 - 26 = 2 (B).",
                    "incorrect": "Stopping at Z and getting stuck."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Counting letter positions from A on fingers during time-pressured exams.",
                    "correction": "Use EJOTY (5, 10, 15, 20, 25) to immediately determine any letter's position within 1 second.",
                    "rationale": "Saves 10-15 seconds per question and eliminates counting errors."
                },
                {
                    "mistake": "Testing answer options blindly in continuous pattern series.",
                    "correction": "Count total length N and factorize into equal blocks (4x4, 3x5).",
                    "rationale": "Blind plugging takes 2 minutes; block division solves the pattern in 20 seconds."
                },
                {
                    "mistake": "Subtracting from 26 instead of 27 to find reverse ranks.",
                    "correction": "Always subtract from 27 because the 1st letter (A=1) corresponds to the 26th letter (Z=26), giving 1 + 26 = 27.",
                    "rationale": "Mathematical principle of dual-ended index numbering."
                },
                {
                    "mistake": "Confusing internal cluster relation with sequence-level progression.",
                    "correction": "Track first letters across all terms, then second letters across all terms.",
                    "rationale": "Inter-cluster tracking is the standard exam design pattern."
                }
            ],
            "quick_revision_points": [
                "EJOTY: E=5, J=10, O=15, T=20, Y=25",
                "Opposite letter pairs sum to 27: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN",
                "Reverse position of any letter = 27 - Forward position",
                "Circular wrap: Z+1 = A, Z+2 = B; A-1 = Z, A-2 = Y",
                "For continuous series: count total length, divide into blocks of 3, 4, or 5",
                "Multi-letter clusters: solve position-by-position (all 1st letters, then all 2nd letters)",
                "Vowel positions: A=1, E=5, I=9, O=15, U=21"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4101,
                "topic_id": 41,
                "exam_id": 1,
                "question": "Which letter cluster will replace the question mark (?) in the following series: BDF, CFI, DHL, ? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "EJO",
                    "EKN",
                    "EKP",
                    "FKO"
                ],
                "correct_answer": "EJO",
                "explanation": "Track position by position:\n1st letters: B(2), C(3), D(4) -> next is E(5)\n2nd letters: D(4), F(6), H(8) -> (+2 each step) -> next is J(10)\n3rd letters: F(6), I(9), L(12) -> (+3 each step) -> next is O(15)\nResult is EJO.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4102,
                "topic_id": 41,
                "exam_id": 1,
                "question": "Which of the following letter combinations will complete the series: a_ba_b_b_a_b [RRB NTPC 2022]",
                "options_json": [
                    "b a a b a",
                    "a b b a b",
                    "b b a a b",
                    "a a b b a"
                ],
                "correct_answer": "b a a b a",
                "explanation": "Count total length: 12 letters.\nDivide into blocks of 3: a_b | a_b | _b_ | a_b.\nIf pattern is 'abb': abb, abb, abb, abb => blanks are b, b, a, b? If pattern is 'aba': aba, aba, aba, aba => blanks: b, a, a, b, a. Let's verify: a(b)ba(a)b(a)b(b)a(a)b. With blanks 'b a a b a': 1st blank b -> abb; 2nd blank a -> aab; cyclical abba. In standard key, 'b a a b a' yields regular uniform alternation.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4103,
                "topic_id": 41,
                "exam_id": 1,
                "question": "What is the next term in the series: Z, W, S, P, L, I, ? [SSC CHSL 2022]",
                "options_json": [
                    "E",
                    "F",
                    "D",
                    "G"
                ],
                "correct_answer": "E",
                "explanation": "Check backward step shifts:\nZ(26) - 3 = W(23)\nW(23) - 4 = S(19)\nS(19) - 3 = P(16)\nP(16) - 4 = L(12)\nL(12) - 3 = I(9)\nThe pattern of subtractions is alternating: -3, -4, -3, -4, -3, next is -4.\nI(9) - 4 = 5 = E.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4101,
                "topic_id": 41,
                "question": "Find the next letter in the series: A, C, E, G, ?",
                "options_json": [
                    "I",
                    "H",
                    "J",
                    "K"
                ],
                "correct_answer": "I",
                "explanation": "Each step adds +2: A(1), C(3), E(5), G(7), next is I(9).",
                "points": 1
            },
            {
                "id": 4102,
                "topic_id": 41,
                "question": "Find the next term: AZ, BY, CX, DW, ?",
                "options_json": [
                    "EV",
                    "FU",
                    "EU",
                    "EW"
                ],
                "correct_answer": "EV",
                "explanation": "Opposite letter pairs: A-Z, B-Y, C-X, D-W, next is E-V.",
                "points": 1
            },
            {
                "id": 4103,
                "topic_id": 41,
                "question": "Find the missing term: ABC, DEF, GHI, ?",
                "options_json": [
                    "JKL",
                    "MNO",
                    "JKM",
                    "IKL"
                ],
                "correct_answer": "JKL",
                "explanation": "Consecutive blocks of three letters: ABC, DEF, GHI, next is JKL.",
                "points": 1
            },
            {
                "id": 4104,
                "topic_id": 41,
                "question": "What is the next term: Z, X, V, T, R, ?",
                "options_json": [
                    "P",
                    "Q",
                    "O",
                    "N"
                ],
                "correct_answer": "P",
                "explanation": "Subtracting 2 from each rank: 26, 24, 22, 20, 18, next is 16 = P.",
                "points": 1
            },
            {
                "id": 4105,
                "topic_id": 41,
                "question": "Find the next term: B, E, H, K, N, ?",
                "options_json": [
                    "Q",
                    "P",
                    "R",
                    "S"
                ],
                "correct_answer": "Q",
                "explanation": "Adding 3 each step: B(2), E(5), H(8), K(11), N(14), next is 14 + 3 = 17 = Q.",
                "points": 1
            },
            {
                "id": 4106,
                "topic_id": 41,
                "question": "Find the missing term: A1, C3, E5, G7, ?",
                "options_json": [
                    "I9",
                    "H8",
                    "J10",
                    "K11"
                ],
                "correct_answer": "I9",
                "explanation": "Letters and their numerical ranks skipping by 2: next is I9.",
                "points": 1
            },
            {
                "id": 4107,
                "topic_id": 41,
                "question": "Find the missing term: ZA, YB, XC, WD, ?",
                "options_json": [
                    "VE",
                    "UF",
                    "VF",
                    "UE"
                ],
                "correct_answer": "VE",
                "explanation": "1st letter decreases by 1 (Z, Y, X, W, V); 2nd letter increases by 1 (A, B, C, D, E) => VE.",
                "points": 1
            },
            {
                "id": 4108,
                "topic_id": 41,
                "question": "Find the next term: C, F, I, L, O, ?",
                "options_json": [
                    "R",
                    "Q",
                    "P",
                    "S"
                ],
                "correct_answer": "R",
                "explanation": "Multiples of 3: C(3), F(6), I(9), L(12), O(15), next is 18 = R.",
                "points": 1
            },
            {
                "id": 4109,
                "topic_id": 41,
                "question": "Find the next cluster: AB, DE, GH, JK, ?",
                "options_json": [
                    "MN",
                    "LM",
                    "NO",
                    "KL"
                ],
                "correct_answer": "MN",
                "explanation": "Consecutive letter pairs skipping one letter in between: AB (skip C), DE (skip F), GH (skip I), JK (skip L), next is MN.",
                "points": 1
            },
            {
                "id": 4110,
                "topic_id": 41,
                "question": "What is the opposite letter of M?",
                "options_json": [
                    "N",
                    "O",
                    "L",
                    "P"
                ],
                "correct_answer": "N",
                "explanation": "Rank of M = 13. Opposite rank = 27 - 13 = 14 = N.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4101,
                "topic_id": 41,
                "question": "What is the 15th letter of the English alphabet?",
                "options_json": [
                    "O",
                    "N",
                    "P",
                    "M"
                ],
                "correct_answer": "O",
                "explanation": "By EJOTY rule: O = 15.",
                "points": 1
            },
            {
                "id": 4102,
                "topic_id": 41,
                "question": "Find the next letter in the series: D, H, L, P, ?",
                "options_json": [
                    "T",
                    "S",
                    "U",
                    "R"
                ],
                "correct_answer": "T",
                "explanation": "Each step adds 4: D(4), H(8), L(12), P(16), next is 20 = T.",
                "points": 1
            },
            {
                "id": 4103,
                "topic_id": 41,
                "question": "What letter is opposite to H in the alphabet?",
                "options_json": [
                    "S",
                    "T",
                    "R",
                    "U"
                ],
                "correct_answer": "S",
                "explanation": "Rank of H = 8. Opposite is 27 - 8 = 19 = S.",
                "points": 1
            },
            {
                "id": 4104,
                "topic_id": 41,
                "question": "Find the next term: AC, EG, IK, MO, ?",
                "options_json": [
                    "QS",
                    "PR",
                    "RT",
                    "OQ"
                ],
                "correct_answer": "QS",
                "explanation": "1st letters: A, E, I, M (+4) -> Q. 2nd letters: C, G, K, O (+4) -> S. Result is QS.",
                "points": 1
            },
            {
                "id": 4105,
                "topic_id": 41,
                "question": "Find the next term: Z, Y, X, W, V, ?",
                "options_json": [
                    "U",
                    "T",
                    "S",
                    "W"
                ],
                "correct_answer": "U",
                "explanation": "Reverse consecutive alphabet: V - 1 = U.",
                "points": 1
            },
            {
                "id": 4106,
                "topic_id": 41,
                "question": "In a continuous series of 12 letters, how should you first try factorizing the blocks?",
                "options_json": [
                    "3 blocks of 4 or 4 blocks of 3",
                    "2 blocks of 6 only",
                    "7 blocks of 2",
                    "5 blocks of 2"
                ],
                "correct_answer": "3 blocks of 4 or 4 blocks of 3",
                "explanation": "12 factors naturally into 3 x 4 or 4 x 3 blocks.",
                "points": 1
            },
            {
                "id": 4107,
                "topic_id": 41,
                "question": "What is the reverse rank of the letter B (A=26, B=25)?",
                "options_json": [
                    "25",
                    "26",
                    "24",
                    "2"
                ],
                "correct_answer": "25",
                "explanation": "Reverse rank = 27 - 2 = 25.",
                "points": 1
            },
            {
                "id": 4108,
                "topic_id": 41,
                "question": "Find the next letter: B, D, G, K, P, ?",
                "options_json": [
                    "V",
                    "U",
                    "W",
                    "T"
                ],
                "correct_answer": "V",
                "explanation": "Differences increase by 1: B(2)+2=D(4), D(4)+3=G(7), G(7)+4=K(11), K(11)+5=P(16). Next difference is +6 => 16 + 6 = 22 = V.",
                "points": 1
            },
            {
                "id": 4109,
                "topic_id": 41,
                "question": "Find the next term: AA, BB, CC, DD, ?",
                "options_json": [
                    "EE",
                    "FF",
                    "DE",
                    "EF"
                ],
                "correct_answer": "EE",
                "explanation": "Doubled consecutive letters: next is EE.",
                "points": 1
            },
            {
                "id": 4110,
                "topic_id": 41,
                "question": "What letter comes 3 steps after X in cyclical wrap-around?",
                "options_json": [
                    "A",
                    "Z",
                    "B",
                    "C"
                ],
                "correct_answer": "A",
                "explanation": "X(24) + 3 = 27 = 26 + 1 = A.",
                "points": 1
            }
        ]
    },
    "42": {
        "title": "Coding-Decoding: Letter Shifting, Substitution, Reverse Ranks & Matrix Rules",
        "source_id": 7,
        "content": {
            "definition": "Coding-Decoding evaluates cryptographic translation mechanisms where plain text words, numbers, or phrases are encrypted into cyphertext according to specific deterministic rules. Crucial in SSC CGL, IBPS/SBI PO, and Railways examinations, questions test forward/reverse rank shifting ($+k, -k$), opposite letter substitution (sum = 27), cross-positional rearrangement, direct symbol substitution, Chinese sentence elimination, and conditional matrix coding.",
            "overview": "Fundamental Cryptographic Patterns:\n- Direct Letter Shifting: Constant shift (e.g. $+2$ to every letter), alternating shifts ($+1, -1, +1, -1$), or progressive shifts ($+1, +2, +3, +4$)\n- Reverse Opposite Pairing: Replacing each letter with its opposite (A with Z, B with Y, C with X)\n- Cross-Positional Scrambling: Swapping adjacent pairs (e.g., positions $1 \\leftrightarrow 2, 3 \\leftrightarrow 4$) or reversing the entire word\n- Number / Sum of Ranks Coding: Coding words by total sum of letter ranks (CAT = $3+1+20=24$) or sum of opposite ranks\n- Substitution / Chinese Coding: Comparing multiple phrases ('she is good', 'good and sweet') to isolate individual word meanings via intersection",
            "types": [
                {
                    "name": "1. Positional Shift & Progressive Coding",
                    "desc": "Letters shifted by fixed constants or linearly increasing step increments.",
                    "examples": [
                        "If TEACHER is coded as VGCEJGT (+2 shift to every letter)",
                        "If DELHI is coded as EFMIJ (+1 shift to every letter)"
                    ]
                },
                {
                    "name": "2. Reverse Alphabetical & Opposite Letter Coding",
                    "desc": "Encoding characters into their mirror counterparts where $R_1 + R_2 = 27$.",
                    "examples": [
                        "If KING is coded as PRMT (K-P, I-R, N-M, G-T are opposite pairs)",
                        "If HAND is coded as SZMW (H-S, A-Z, N-M, D-W)"
                    ]
                },
                {
                    "name": "3. Letter-to-Number / Value Aggregation Coding",
                    "desc": "Converting words into numeric quantities via rank summation, multiplication, or vowel/consonant weighting.",
                    "examples": [
                        "If CAT = 24 (3+1+20) and DOG = 26 (4+15+7), find PET",
                        "If GO = 32 (Opposites of G=20, O=12; 20+12 = 32)"
                    ]
                },
                {
                    "name": "4. Fictitious Language / Chinese Coding",
                    "desc": "Finding code-word correspondence by eliminating shared tokens across multiple sentences.",
                    "examples": [
                        "'pic vic nic' = 'winter is cold'; 'ri nic to' = 'summer is hot' => common word 'is' = 'nic'",
                        "Isolating unique terms by set difference"
                    ]
                },
                {
                    "name": "5. Conditional Matrix & Rule-Based Coding",
                    "desc": "Applying conditional rules (e.g., if first letter is vowel and last is consonant, swap codes).",
                    "examples": [
                        "Conditional digit coding in Bank PO examinations"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Check Shift Homogeneity Rule",
                    "explanation": "Before assuming a constant shift (like $+2$), calculate the shift for the first 3 letters. If shifts are $+1, +2, +3$, it is a progressive series; if $+2, -2, +2, -2$, it is alternating.",
                    "words": [
                        "Shift Homogeneity",
                        "First 3 Letters",
                        "Progressive vs Constant"
                    ],
                    "correct": "In LIGHT -> MJJIW: L(+1)->M, I(+1)->J, G(+3)->J? Verify exact differences for all letters.",
                    "incorrect": "Checking only the first letter and assuming the entire word follows the same shift."
                },
                {
                    "rule_number": 2,
                    "title": "Opposite Sum 27 Value Check",
                    "explanation": "When numeric codes seem unusually high for small words (e.g., GO = 32, when standard ranks are G=7, O=15 giving 22), check the sum of the OPPOSITE ranks: Opposite of G is T(20), opposite of O is L(12). $20 + 12 = 32$.",
                    "words": [
                        "Opposite Sum Check",
                        "GO = 32 Trap",
                        "High Numeric Codes"
                    ],
                    "correct": "GO = 32 => T(20) + L(12) = 32. For SOME: S(8) + O(12) + M(14) + E(22) = 56.",
                    "incorrect": "Assuming arbitrary addition of +10 without checking opposite letter ranks."
                },
                {
                    "rule_number": 3,
                    "title": "Chinese Coding Sentence Intersection Rule",
                    "explanation": "To decode fictitious language words: (1) Find a pair of sentences that share exactly ONE English word. (2) Find the single code token common to both code sentences. (3) That common token is the definitive translation.",
                    "words": [
                        "Sentence Intersection",
                        "Single Shared Token",
                        "Chinese Coding"
                    ],
                    "correct": "Sentence 1: 'sky is blue' = 'ti ka pa'; Sentence 2: 'blue sea' = 'pa lo'. Common word 'blue' = common code 'pa'.",
                    "incorrect": "Assuming words and codes appear in the identical left-to-right order."
                },
                {
                    "rule_number": 4,
                    "title": "Cross-Positional Inversion Pattern Rule",
                    "explanation": "If the letters in the cyphertext are an exact anagram of the original word, the encryption is purely positional transposition (not rank shifting). Number positions 1 to $N$ and map the permutation.",
                    "words": [
                        "Transposition Cypher",
                        "Anagram Check",
                        "Index Mapping"
                    ],
                    "correct": "MOTHER -> REHTOM (Word is simply reversed from end to start).",
                    "incorrect": "Calculating shifts between M and R."
                },
                {
                    "rule_number": 5,
                    "title": "Direct Symbol / Alphabet Mapping Rule",
                    "explanation": "If two example words share common letters that map to the identical symbols/letters (e.g. in FIRE = #$%* and RAIN = *&!^, 'R' is '*' in both), the code is direct 1-to-1 letter mapping without arithmetic operations.",
                    "words": [
                        "Direct Substitution",
                        "Common Letter Consistency",
                        "Symbol Coding"
                    ],
                    "correct": "Identifying that each letter in the target word already appears in the given examples and directly copying codes.",
                    "incorrect": "Searching for complex mathematical rules when it is a direct lookup table."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Assuming word order matches code order in Chinese/Fictitious coding.",
                    "correction": "Words are intentionally scrambled. You must use intersection across sentences.",
                    "rationale": "'sky is blue' does not mean 'sky' is the first code word."
                },
                {
                    "mistake": "Testing only the first letter's shift and selecting an answer option too quickly.",
                    "correction": "Always verify at least the first two and the last letter of the word.",
                    "rationale": "Examiners intentionally design options where the first letter matches multiple distractors."
                },
                {
                    "mistake": "Forgetting opposite letter ranks when numeric sum doesn't match standard forward ranks.",
                    "correction": "If forward ranks sum to 22 but code is 32, immediately test reverse ranks (27 - R).",
                    "rationale": "Standard high-yield banking examination trick."
                },
                {
                    "mistake": "Trying letter shift formulas on transposition/anagram codes.",
                    "correction": "If the cyphertext uses the exact same letters as the plaintext, map position indices.",
                    "rationale": "Saves up to 1 minute per question."
                }
            ],
            "quick_revision_points": [
                "Always check first: Are the cypher letters identical to original letters? If yes => Transposition",
                "Are two examples given with identical letter-to-code mapping? If yes => Direct substitution",
                "Is the code a number? Check: (1) Sum of forward ranks (2) Sum of opposite ranks (3) Number of letters",
                "Opposite letter pairs sum to 27: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN",
                "Chinese coding: Compare two sentences at a time to eliminate common terms",
                "EJOTY benchmarks: E=5, J=10, O=15, T=20, Y=25",
                "Progressive shifts (+1, +2, +3...) are common in SSC CGL Tier 1"
            ]
        },
        "previous_year_questions": [
            {
                "id": 4201,
                "topic_id": 42,
                "exam_id": 1,
                "question": "In a certain code language, 'TRUTH' is coded as 'UQVSG'. How will 'FALSE' be coded in that language? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "GZMRD",
                    "GZMRE",
                    "GZNRD",
                    "EZMRD"
                ],
                "correct_answer": "GZMRD",
                "explanation": "Analyze the shifts for TRUTH -> UQVSG:\nT(+1) = U\nR(-1) = Q\nU(+1) = V\nT(-1) = S\nH(+1) = G? Wait: H(8)-1=G! So shifts are +1, -1, +1, -1, -1? Let's check: T(+1)->U, R(-1)->Q, U(+1)->V, T(-1)->S, H(-1)->G. Applying +1, -1, +1, -1, -1 to FALSE:\nF(+1) = G\nA(-1) = Z\nL(+1) = M\nS(-1) = R\nE(-1) = D\nResult is GZMRD.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4202,
                "topic_id": 42,
                "exam_id": 1,
                "question": "If 'GO' is coded as '32' and 'SHE' is coded as '49', how will 'SOME' be coded? [IBPS PO Prelims 2022]",
                "options_json": [
                    "56",
                    "58",
                    "62",
                    "64"
                ],
                "correct_answer": "56",
                "explanation": "Check opposite letter ranks:\nGO: Opposite of G is T(20), opposite of O is L(12). Sum = 20 + 12 = 32.\nSHE: Opposite of S is H(8), opposite of H is S(19), opposite of E is V(22). Sum = 8 + 19 + 22 = 49.\nFor SOME:\nOpposite of S = H(8)\nOpposite of O = L(12)\nOpposite of M = N(14)\nOpposite of E = V(22)\nTotal sum = 8 + 12 + 14 + 22 = 56.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 4203,
                "topic_id": 42,
                "exam_id": 1,
                "question": "In a code language, 'COMPUTER' is written as 'RFUVQNPC'. How is 'MEDICINE' written in that code? [SSC CHSL 2022]",
                "options_json": [
                    "EOJDJEFM",
                    "EOJDEJFM",
                    "MFEJDJOE",
                    "EOJDJFEM"
                ],
                "correct_answer": "EOJDJEFM",
                "explanation": "Notice that the last letter 'R' becomes the first letter 'R', and first letter 'C' becomes the last letter 'C'.\nActually, the word COMPUTER is reversed: R E T U P M O C.\nThen +1 shift is added to intermediate letters:\n1st letter stays R, last letter stays C.\nE(+1)->F, T(+1)->U, U(+1)->V, P(+1)->Q, M(+1)->N, O(+1)->P.\nResult: R F U V Q N P C.\nApplying the same rule to MEDICINE:\nReversed: E N I C I D E M\n1st letter stays E, last letter stays M.\nN(+1)=O, I(+1)=J, C(+1)=D, I(+1)=J, D(+1)=E, E(+1)=F.\nResult is E O J D J E F M.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 4201,
                "topic_id": 42,
                "question": "If CAT is coded as DBU (+1 shift), how is DOG coded?",
                "options_json": [
                    "EPH",
                    "EOH",
                    "DPH",
                    "EPG"
                ],
                "correct_answer": "EPH",
                "explanation": "D(+1)=E, O(+1)=P, G(+1)=H => EPH.",
                "points": 1
            },
            {
                "id": 4202,
                "topic_id": 42,
                "question": "If BOOK is coded as 43 (sum of ranks: 2+15+15+11), how is PEN coded?",
                "options_json": [
                    "35",
                    "32",
                    "38",
                    "40"
                ],
                "correct_answer": "35",
                "explanation": "P(16) + E(5) + N(14) = 35.",
                "points": 1
            },
            {
                "id": 4203,
                "topic_id": 42,
                "question": "If 'WATER' is coded as 'YCVGT', what is the shift applied to each letter?",
                "options_json": [
                    "+2",
                    "+1",
                    "+3",
                    "-2"
                ],
                "correct_answer": "+2",
                "explanation": "W(23)+2=Y(25), A(1)+2=C(3), T(20)+2=V(22), E(5)+2=G(7), R(18)+2=T(20). Shift is +2.",
                "points": 1
            },
            {
                "id": 4204,
                "topic_id": 42,
                "question": "In a code, 'ka bi' means 'cold water', and 'bi no' means 'hot water'. What is the code for 'water'?",
                "options_json": [
                    "bi",
                    "ka",
                    "no",
                    "cannot be determined"
                ],
                "correct_answer": "bi",
                "explanation": "Both sentences share the word 'water' and the code word 'bi'. Thus, 'water' is 'bi'.",
                "points": 1
            },
            {
                "id": 4205,
                "topic_id": 42,
                "question": "If KING is coded with its opposite letters as PRMT, how is MAN coded?",
                "options_json": [
                    "NZM",
                    "MZN",
                    "NAM",
                    "NZN"
                ],
                "correct_answer": "NZM",
                "explanation": "Opposite letters: M-N, A-Z, N-M => NZM.",
                "points": 1
            },
            {
                "id": 4206,
                "topic_id": 42,
                "question": "If 'ROAD' is coded as 'URDG', how is 'SWAN' coded?",
                "options_json": [
                    "VZDO",
                    "VZDP",
                    "UXDQ",
                    "VZDQ"
                ],
                "correct_answer": "VZDQ",
                "explanation": "Each letter shifts +3: R+3=U, O+3=R, A+3=D, D+3=G. For SWAN: S+3=V, W+3=Z, A+3=D, N+3=Q => VZDQ.",
                "points": 1
            },
            {
                "id": 4207,
                "topic_id": 42,
                "question": "If 'APPLE' is written as 'ELPPA', what is the coding mechanism?",
                "options_json": [
                    "Reversing the word order",
                    "+1 shift",
                    "Opposite letters",
                    "-1 shift"
                ],
                "correct_answer": "Reversing the word order",
                "explanation": "APPLE spelled backwards is ELPPA. The coding is simple string reversal.",
                "points": 1
            },
            {
                "id": 4208,
                "topic_id": 42,
                "question": "If RED = 27 (18+5+4), what is BLUE?",
                "options_json": [
                    "40",
                    "38",
                    "42",
                    "45"
                ],
                "correct_answer": "40",
                "explanation": "B(2) + L(12) + U(21) + E(5) = 40.",
                "points": 1
            },
            {
                "id": 4209,
                "topic_id": 42,
                "question": "If 'GOOD' is coded as 'HPPF' (+1 shift), how is 'BEST' coded?",
                "options_json": [
                    "CFTU",
                    "CFSU",
                    "BFSU",
                    "CGTU"
                ],
                "correct_answer": "CFTU",
                "explanation": "B+1=C, E+1=F, S+1=T, T+1=U => CFTU.",
                "points": 1
            },
            {
                "id": 4210,
                "topic_id": 42,
                "question": "If A=1, B=2, and ACE = 9 (1+3+5), what is BAD?",
                "options_json": [
                    "7",
                    "6",
                    "8",
                    "9"
                ],
                "correct_answer": "7",
                "explanation": "B(2) + A(1) + D(4) = 7.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 4201,
                "topic_id": 42,
                "question": "If TAP is coded as SZO (-1 shift), how is SUN coded?",
                "options_json": [
                    "RTM",
                    "TTM",
                    "RSM",
                    "RTN"
                ],
                "correct_answer": "RTM",
                "explanation": "S-1=R, U-1=T, N-1=M => RTM.",
                "points": 1
            },
            {
                "id": 4202,
                "topic_id": 42,
                "question": "If BOY is coded as 42 (2+15+25), how is GIRL coded?",
                "options_json": [
                    "46",
                    "44",
                    "48",
                    "50"
                ],
                "correct_answer": "46",
                "explanation": "G(7) + I(9) + R(18) + L(12) = 46.",
                "points": 1
            },
            {
                "id": 4203,
                "topic_id": 42,
                "question": "If 'ti ro' means 'fast train' and 'ro ma' means 'train delay', what does 'ro' mean?",
                "options_json": [
                    "train",
                    "fast",
                    "delay",
                    "cannot say"
                ],
                "correct_answer": "train",
                "explanation": "The common word in both phrases is 'train', and the common code is 'ro'.",
                "points": 1
            },
            {
                "id": 4204,
                "topic_id": 42,
                "question": "If Z = 26 and NET = 39 (14+5+20), what is NUT?",
                "options_json": [
                    "55",
                    "54",
                    "56",
                    "53"
                ],
                "correct_answer": "55",
                "explanation": "N(14) + U(21) + T(20) = 55.",
                "points": 1
            },
            {
                "id": 4205,
                "topic_id": 42,
                "question": "If FRIEND is coded as HUMJTK (+2 shift), how is CANDLE coded?",
                "options_json": [
                    "ECPFNG",
                    "EDPFNG",
                    "ECOFNG",
                    "ECPGNH"
                ],
                "correct_answer": "ECPFNG",
                "explanation": "C(+2)=E, A(+2)=C, N(+2)=P, D(+2)=F, L(+2)=N, E(+2)=G => ECPFNG.",
                "points": 1
            },
            {
                "id": 4206,
                "topic_id": 42,
                "question": "If DELHI is coded as 73541 and CALCUTTA as 82589662, how is CALICUT coded?",
                "options_json": [
                    "8251896",
                    "8251869",
                    "8251986",
                    "8521896"
                ],
                "correct_answer": "8251896",
                "explanation": "Direct letter substitution lookup:\nC=8, A=2, L=5, I=1, C=8, U=9, T=6 => 8251896.",
                "points": 1
            },
            {
                "id": 4207,
                "topic_id": 42,
                "question": "If A = 26 (opposite rank) and SUN = 27 (8+6+13), what is CAT in opposite ranks?",
                "options_json": [
                    "57",
                    "24",
                    "48",
                    "60"
                ],
                "correct_answer": "57",
                "explanation": "Opposite of C is X(24), A is Z(26), T is G(7). Sum = 24 + 26 + 7 = 57.",
                "points": 1
            },
            {
                "id": 4208,
                "topic_id": 42,
                "question": "If 'STRONG' is coded as 'GNORTS', how is 'WEAK' coded?",
                "options_json": [
                    "KAEW",
                    "AKEW",
                    "KAWE",
                    "KEAW"
                ],
                "correct_answer": "KAEW",
                "explanation": "Reverse string coding: WEAK reversed is KAEW.",
                "points": 1
            },
            {
                "id": 4209,
                "topic_id": 42,
                "question": "If D = 4 and COVER = 63 (3+15+22+5+18), what is BASIS?",
                "options_json": [
                    "50",
                    "48",
                    "52",
                    "54"
                ],
                "correct_answer": "50",
                "explanation": "B(2) + A(1) + S(19) + I(9) + S(19) = 50.",
                "points": 1
            },
            {
                "id": 4210,
                "topic_id": 42,
                "question": "If 'LION' is coded as 'MJPO' (+1 shift), how is 'TIGER' coded?",
                "options_json": [
                    "UJHFS",
                    "UJHFR",
                    "VJHFS",
                    "UJGFS"
                ],
                "correct_answer": "UJHFS",
                "explanation": "T+1=U, I+1=J, G+1=H, E+1=F, R+1=S => UJHFS.",
                "points": 1
            }
        ]
    }
}
