# Math Part 2: Topics 28 to 32
# 28: Time and Work, 29: Time Speed and Distance, 30: Simple Interest, 31: Compound Interest, 32: Mensuration

MATH_PART2_DATA = {
    "28": {
        "title": "Time and Work: Efficiency Method, LCM Approach, Alternate Work & Pipes/Cisterns",
        "source_id": 7,
        "content": {
            "definition": "Time and Work is the operational mathematics domain modeling resource allocation, task throughput rates, and human efficiency. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions evaluate reciprocal work rates, LCM total-work models, alternating work cycles, negative work (destructive workers or leak pipes), and demographic equivalence equations (M1*D1*H1 / W1 = M2*D2*H2 / W2).",
            "overview": "Fundamental Principles:\n- Work = Efficiency x Time (Total Work = Rate * Days)\n- Inverse Relation: Efficiency is inversely proportional to Time taken when work is constant: E1/E2 = T2/T1.\n- LCM Total Work Method: Assume total work to be the LCM of individual completion times. Each worker's daily rate = (Total Units / Days).\n- Compound Proportion: (M1 * D1 * H1 * E1) / W1 = (M2 * D2 * H2 * E2) / W2.\n- Negative Work in Cisterns: Net Filling Rate = Inlet Rate - Outlet (Leak) Rate.",
            "types": [
                {
                    "name": "1. LCM Total-Work & Unit Efficiency Model",
                    "desc": "Converting fractional rates into discrete integer work units.",
                    "examples": [
                        "A completes in 10 days, B in 15 days: LCM(10, 15) = 30 units total work.",
                        "A's daily efficiency = 30/10 = 3 units/day; B's daily efficiency = 30/15 = 2 units/day.",
                        "Combined efficiency = 3 + 2 = 5 units/day -> Time taken together = 30 / 5 = 6 days."
                    ]
                },
                {
                    "name": "2. Alternate Day Work Cycles",
                    "desc": "Workers taking turns on successive days.",
                    "examples": [
                        "A takes 12 days (efficiency 5 units), B takes 15 days (efficiency 4 units), Work = 60 units.",
                        "In 1 cycle of 2 days: Work completed = 5 + 4 = 9 units.",
                        "6 cycles (12 days) = 54 units. Day 13: A does 5 units (59 units). Day 14: B does remaining 1 unit in 1/4 day. Total = 13.25 days."
                    ]
                },
                {
                    "name": "3. Demographic Equivalence (Men, Women & Children)",
                    "desc": "Equating group outputs to a unified single worker efficiency.",
                    "examples": [
                        "If 2 Men = 3 Women = 4 Boys can finish in 44 days: Find combined daily rate.",
                        "Convert all to Boy units: 1 Man = 2 Boys, 1 Woman = 4/3 Boys."
                    ]
                },
                {
                    "name": "4. Workers Leaving Before or After Commencement",
                    "desc": "Adjusting remaining work when personnel depart mid-task.",
                    "examples": [
                        "If A leaves 3 days before scheduled completion: Add A's 3 days of theoretical work to total work and divide by combined efficiency."
                    ]
                },
                {
                    "name": "5. Pipes and Cisterns (Inlet & Leak Dynamics)",
                    "desc": "Applying time and work logic to fluid filling and emptying reservoirs.",
                    "examples": [
                        "Pipe A fills in 6 hrs (+ units), Pipe B fills in 8 hrs (+ units), Waste Pipe C empties in 12 hrs (- units).",
                        "Net efficiency = E_A + E_B - E_C."
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Compound Proportion Formula (MDH / W)",
                    "explanation": "Work output across disparate workforce groups satisfies: $\\frac{M_1 \\times D_1 \\times H_1 \\times E_1}{W_1} = \\frac{M_2 \\times D_2 \\times H_2 \\times E_2}{W_2}$, where $M = \\text{men}, D = \\text{days}, H = \\text{hours/day}, E = \\text{efficiency}, W = \\text{work done}$.",
                    "words": [
                        "MDH Formula",
                        "Compound Proportion",
                        "M1 D1 H1 / W1"
                    ],
                    "correct": "15 men working 8 hours/day complete 1 bridge in 20 days: How many days for 20 men working 6 hours/day? (15*8*20)/1 = (20*6*D2)/1 -> D2 = 20 days.",
                    "incorrect": "Equating M1*D1 = M2*D2 directly while omitting unequal daily working hours."
                },
                {
                    "rule_number": 2,
                    "title": "LCM Total Work Shortcut",
                    "explanation": "Assume Total Work = $\\text{LCM}(t_1, t_2, ...)$. Efficiency of each person = $\\frac{\\text{Total Units}}{t_i}$. Avoid working with fractions (1/a + 1/b).",
                    "words": [
                        "LCM Method",
                        "Efficiency Units",
                        "Avoid Fractions"
                    ],
                    "correct": "A in 12 days, B in 18 days: Total work = 36 units. Rate A = 3, Rate B = 2. Together = 36 / (3 + 2) = 7.2 days.",
                    "incorrect": "Using 1/12 + 1/18 = 5/36 and inverting, prone to arithmetic errors."
                },
                {
                    "rule_number": 3,
                    "title": "'Leaving Before Completion' Compensation Trick",
                    "explanation": "If worker $A$ leaves $k$ days BEFORE the work is completed, add $(k \\times E_A)$ to the Total Work, and divide the inflated work by the COMBINED efficiency of all initial workers.",
                    "words": [
                        "Leaving Before",
                        "Work Compensation",
                        "Virtual Units"
                    ],
                    "correct": "Total work = 60 units. A (eff 3) leaves 2 days before completion. Add 2*3 = 6 units. Total = 66 units. Divide by (E_A + E_B).",
                    "incorrect": "Working backwards day-by-day with variables, which takes 3x more time."
                },
                {
                    "rule_number": 4,
                    "title": "Efficiency-Time Inversion Rule",
                    "explanation": "Ratio of efficiencies is the reciprocal of the ratio of times taken: $\\frac{E_1}{E_2} = \\frac{T_2}{T_1}$. If A is $50\\%$ more efficient than B, $E_A : E_B = 3 : 2 \\implies T_A : T_B = 2 : 3$.",
                    "words": [
                        "Efficiency Inversion",
                        "E1/E2 = T2/T1",
                        "Time Ratio"
                    ],
                    "correct": "A is twice as fast as B (E_A/E_B = 2/1): Time taken T_A/T_B = 1/2.",
                    "incorrect": "Assuming time taken is in the same ratio as efficiency (2:1)."
                },
                {
                    "rule_number": 5,
                    "title": "Negative Work Drain Rule for Leaks",
                    "explanation": "A leak empties a tank at rate $E_{\\text{leak}}$ (negative efficiency). If a tank fills in $T_{\\text{in}}$ without leak and $T_{\\text{net}}$ with leak, the leak's solo emptying time is: $T_{\\text{leak}} = \\frac{T_{\\text{in}} \\times T_{\\text{net}}}{T_{\\text{net}} - T_{\\text{in}}}$.",
                    "words": [
                        "Leak Formula",
                        "Negative Work",
                        "Emptying Rate"
                    ],
                    "correct": "Pipe fills in 6 hrs, with leak it takes 8 hrs: Leak empties in (6 * 8) / (8 - 6) = 48 / 2 = 24 hrs.",
                    "incorrect": "Subtracting times directly: 8 - 6 = 2 hrs (False linear time subtraction)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Adding days directly: 'A takes 10 days, B takes 15 days, so together they take 25 days'.",
                    "correction": "Together they must take LESS time than the fastest individual: 10 * 15 / (10 + 15) = 6 days.",
                    "rationale": "More workers increase the collective rate, decreasing elapsed time."
                },
                {
                    "mistake": "Dividing work equally in alternate day problems without checking residual units.",
                    "correction": "Always calculate integer cycles first, then assign residual fractional units to the person whose turn it is.",
                    "rationale": "The cycle might terminate midway through a specific person's turn."
                },
                {
                    "mistake": "Forgetting to invert time when converting to efficiency.",
                    "correction": "If A is twice as efficient as B, A takes HALF the time of B, not double.",
                    "rationale": "High efficiency translates to lower duration."
                },
                {
                    "mistake": "Confusing 'Men or Women' with 'Men and Women'.",
                    "correction": "'4 Men OR 6 Women' means 4M = 6W. '4 Men AND 6 Women' means (4M + 6W) working simultaneously.",
                    "rationale": "'Or' signifies equivalence; 'And' signifies addition."
                }
            ],
            "quick_revision_points": [
                "Total Work = Efficiency * Time.",
                "LCM Method: Assume Total Work = LCM of individual times.",
                "MDH / W = Constant: (M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2.",
                "If A does work in x days, B in y days: Together = (x * y) / (x + y) days.",
                "Efficiency is inversely proportional to time taken.",
                "Leaving before completion: Add (Departing worker's rate * Days left) to total work.",
                "Leak emptying time = (Filling time * Net time) / (Net time - Filling time).",
                "Wages are distributed in proportion to the total work units done by each worker."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2801,
                "topic_id": 28,
                "question": "A can complete a piece of work in 25 days and B can complete the same work in 30 days. They worked together for 5 days and then A left. In how many days will B finish the remaining work? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "19 days",
                    "18 days",
                    "20 days",
                    "22 days"
                ],
                "correct_answer": "19 days",
                "explanation": "LCM(25, 30) = 150 units total work.\nRate of A = 150 / 25 = 6 units/day.\nRate of B = 150 / 30 = 5 units/day.\nTogether in 5 days, work done = 5 * (6 + 5) = 5 * 11 = 55 units.\nRemaining work = 150 - 55 = 95 units.\nTime taken by B alone = 95 / 5 = 19 days.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2802,
                "topic_id": 28,
                "question": "A is twice as efficient as B and together they can complete a work in 14 days. In how many days can A alone finish the work? [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "21 days",
                    "28 days",
                    "18 days",
                    "24 days"
                ],
                "correct_answer": "21 days",
                "explanation": "Ratio of efficiencies A : B = 2 : 1.\nCombined efficiency = 2 + 1 = 3 units/day.\nTotal work = Combined efficiency * Days = 3 * 14 = 42 units.\nTime taken by A alone = Total work / Efficiency of A = 42 / 2 = 21 days.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2803,
                "topic_id": 28,
                "question": "Two pipes A and B can fill a cistern in 12 hours and 15 hours respectively, while a third pipe C can empty it in 20 hours. If all three pipes are opened together, the cistern will be full in: [UPSC CDS 2023]",
                "options_json": [
                    "10 hours",
                    "8 hours",
                    "12 hours",
                    "15 hours"
                ],
                "correct_answer": "10 hours",
                "explanation": "LCM(12, 15, 20) = 60 units total capacity.\nInlet rate A = 60 / 12 = +5 units/hr.\nInlet rate B = 60 / 15 = +4 units/hr.\nOutlet rate C = 60 / 20 = -3 units/hr.\nNet rate when all open = 5 + 4 - 3 = 6 units/hr.\nTime taken = 60 / 6 = 10 hours.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2801,
                "topic_id": 28,
                "question": "A and B can do a piece of work in 12 days, B and C in 15 days, and C and A in 20 days. How long would A take to complete the work alone?",
                "options_json": [
                    "30 days",
                    "20 days",
                    "40 days",
                    "24 days"
                ],
                "correct_answer": "30 days",
                "explanation": "LCM(12, 15, 20) = 60 units total work.\nRate(A + B) = 60/12 = 5 units/day.\nRate(B + C) = 60/15 = 4 units/day.\nRate(C + A) = 60/20 = 3 units/day.\nAdding all: 2(A + B + C) = 5 + 4 + 3 = 12 -> Rate(A + B + C) = 6 units/day.\nRate of A = Rate(A + B + C) - Rate(B + C) = 6 - 4 = 2 units/day.\nTime for A alone = 60 / 2 = 30 days.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2802,
                "topic_id": 28,
                "question": "A can do a work in 10 days and B in 20 days. If they work on alternate days with A beginning, in how many days will the work be completed?",
                "options_json": [
                    "13 days",
                    "13(1/2) days",
                    "14 days",
                    "12 days"
                ],
                "correct_answer": "13 days",
                "explanation": "Total work = 20 units. Rate A = 2, Rate B = 1.\n2 days = 3 units. 6 cycles (12 days) = 18 units.\nDay 13: A completes the remaining 2 units in 1 full day.\nTotal time = 13 days.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2803,
                "topic_id": 28,
                "question": "3 men or 5 women can do a piece of work in 43 days. In how many days can 5 men and 6 women finish the same work?",
                "options_json": [
                    "15 days",
                    "18 days",
                    "12 days",
                    "20 days"
                ],
                "correct_answer": "15 days",
                "explanation": "3 Men = 5 Women -> 1 Man = 5/3 Women.\n5 Men + 6 Women = 5*(5/3) + 6 = 25/3 + 18/3 = 43/3 Women.\nUsing M1 * D1 = M2 * D2:\n5 Women * 43 days = (43/3 Women) * D2.\n5 * 43 = (43/3) * D2 -> D2 = 5 * 3 = 15 days.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2804,
                "topic_id": 28,
                "question": "A and B can complete a work in 15 days and 10 days respectively. They started together, but B left after 2 days. The remaining work was completed by A. Total days taken to finish the work is:",
                "options_json": [
                    "12 days",
                    "14 days",
                    "10 days",
                    "15 days"
                ],
                "correct_answer": "12 days",
                "explanation": "Total work = LCM(15, 10) = 30 units. Rate A = 2, Rate B = 3.\nIn 2 days together: 2 * (2 + 3) = 10 units.\nRemaining work = 30 - 10 = 20 units.\nTime for A to finish remaining = 20 / 2 = 10 days.\nTotal days = 2 + 10 = 12 days.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2805,
                "topic_id": 28,
                "question": "A leak in the bottom of a tank can empty it in 8 hours. An electric pump fills the tank at 6 liters per minute. When the tank is full, the pump is opened and the tank is emptied in 12 hours. What is the capacity of the tank?",
                "options_json": [
                    "8640 liters",
                    "7200 liters",
                    "9000 liters",
                    "8000 liters"
                ],
                "correct_answer": "8640 liters",
                "explanation": "Leak alone empties in 8 hrs (rate = -1/8).\nLeak + Pump empties in 12 hrs (net rate = -1/12).\nPump filling rate = Net rate - Leak rate = -1/12 - (-1/8) = -1/12 + 1/8 = 1/24 per hour.\nSo the pump can fill the tank in 24 hours.\nPump fills 6 liters/min = 6 * 60 = 360 liters/hour.\nCapacity of tank = 24 hours * 360 liters/hr = 8,640 liters.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 2806,
                "topic_id": 28,
                "question": "If 12 men and 16 boys can do a piece of work in 5 days, while 13 men and 24 boys can do it in 4 days, compare the daily work done by a man to that of a boy.",
                "options_json": [
                    "2 : 1",
                    "3 : 1",
                    "3 : 2",
                    "4 : 1"
                ],
                "correct_answer": "2 : 1",
                "explanation": "(12M + 16B) * 5 = (13M + 24B) * 4.\n60M + 80B = 52M + 96B.\n8M = 16B -> M / B = 2 / 1.\nDaily work ratio = 2 : 1.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2807,
                "topic_id": 28,
                "question": "A is 30% more efficient than B. How much time will they, working together, take to complete a job which A alone could have done in 23 days?",
                "options_json": [
                    "13 days",
                    "11 days",
                    "15 days",
                    "12 days"
                ],
                "correct_answer": "13 days",
                "explanation": "Rate of B = 10, Rate of A = 13.\nTotal work = Rate of A * Days = 13 * 23 = 299 units.\nCombined rate of A + B = 13 + 10 = 23 units/day.\nTime together = 299 / 23 = 13 days.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2808,
                "topic_id": 28,
                "question": "A can build a wall in 30 days and B can demolish it in 40 days. If they work on alternate days with A starting, in how many days will the wall be built?",
                "options_json": [
                    "78.75 days",
                    "80 days",
                    "75 days",
                    "72 days"
                ],
                "correct_answer": "78.75 days",
                "explanation": "LCM = 120 units. Rate A = +4, Rate B = -1.\n2 days = +3 units.\nIn 38 cycles (76 days) = 114 units.\nDay 77: A does +4 (118 units).\nDay 78: B does -1 (117 units).\nDay 79: A does remaining 3 units in 3/4 day = 0.75 day.\nTotal = 78.75 days.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 2809,
                "topic_id": 28,
                "question": "P, Q and R can complete a work in 20, 30 and 60 days respectively. In how many days can P finish the work if he is assisted by Q and R on every third day?",
                "options_json": [
                    "15 days",
                    "16 days",
                    "12 days",
                    "18 days"
                ],
                "correct_answer": "15 days",
                "explanation": "Total work = LCM(20, 30, 60) = 60 units.\nRate P = 3, Rate Q = 2, Rate R = 1.\nDay 1: P works alone = 3 units.\nDay 2: P works alone = 3 units.\nDay 3: P + Q + R work = 3 + 2 + 1 = 6 units.\nIn a 3-day cycle: Work done = 3 + 3 + 6 = 12 units.\nNumber of 3-day cycles to finish 60 units = 60 / 12 = 5 cycles.\nTotal days = 5 * 3 = 15 days.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2810,
                "topic_id": 28,
                "question": "A contract is to be completed in 46 days and 117 men were set to work, each working 8 hours a day. After 33 days, 4/7 of the work is completed. How many additional men may be employed so that the work may be completed in time, each working 9 hours a day?",
                "options_json": [
                    "81 men",
                    "75 men",
                    "80 men",
                    "90 men"
                ],
                "correct_answer": "81 men",
                "explanation": "Remaining days = 46 - 33 = 13 days. Remaining work = 1 - 4/7 = 3/7.\nUsing M1 * D1 * H1 / W1 = M2 * D2 * H2 / W2:\n(117 * 33 * 8) / (4/7) = (M2 * 13 * 9) / (3/7).\n(117 * 33 * 8) / 4 = (M2 * 13 * 9) / 3.\n117 * 33 * 2 = M2 * 39.\n39 divides 117 exactly 3 times: 3 * 33 * 2 = M2 -> M2 = 198 men.\nAdditional men required = 198 - 117 = 81 men.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2801,
                "topic_id": 28,
                "question": "A can do a piece of work in 4 hours; B and C together can do it in 3 hours, while A and C together can do it in 2 hours. How long will B alone take to do it?",
                "options_json": [
                    "12 hours",
                    "8 hours",
                    "10 hours",
                    "6 hours"
                ],
                "correct_answer": "12 hours",
                "explanation": "Total work = LCM(4, 3, 2) = 12 units.\nRate A = 12/4 = 3.\nRate(A + C) = 12/2 = 6 -> Rate C = 6 - 3 = 3.\nRate(B + C) = 12/3 = 4 -> Rate B = 4 - Rate C = 4 - 3 = 1 unit/hr.\nTime for B alone = 12 / 1 = 12 hours.",
                "points": 1
            },
            {
                "id": 2802,
                "topic_id": 28,
                "question": "If 10 men can do a piece of work in 12 days, how many men will be needed to complete the same work in 8 days?",
                "options_json": [
                    "15",
                    "16",
                    "14",
                    "18"
                ],
                "correct_answer": "15",
                "explanation": "M1 * D1 = M2 * D2 -> 10 * 12 = M2 * 8 -> M2 = 120 / 8 = 15 men.",
                "points": 1
            },
            {
                "id": 2803,
                "topic_id": 28,
                "question": "Pipe A fills a tank in 20 minutes and Pipe B fills it in 30 minutes. If both pipes are opened together, how long will it take to fill the tank?",
                "options_json": [
                    "12 minutes",
                    "15 minutes",
                    "10 minutes",
                    "14 minutes"
                ],
                "correct_answer": "12 minutes",
                "explanation": "Together time = (20 * 30) / (20 + 30) = 600 / 50 = 12 minutes.",
                "points": 1
            },
            {
                "id": 2804,
                "topic_id": 28,
                "question": "A and B undertake to do a piece of work for Rs. 600. A alone can do it in 6 days while B alone can do it in 8 days. With the help of C, they finish it in 3 days. Find C's share of wages.",
                "options_json": [
                    "Rs. 75",
                    "Rs. 100",
                    "Rs. 80",
                    "Rs. 90"
                ],
                "correct_answer": "Rs. 75",
                "explanation": "Total work = LCM(6, 8, 3) = 24 units.\nRate A = 4 units/day (In 3 days, A does 4 * 3 = 12 units).\nRate B = 3 units/day (In 3 days, B does 3 * 3 = 9 units).\nWork done by C = 24 - (12 + 9) = 24 - 21 = 3 units.\nC's share = (3 / 24) * 600 = (1 / 8) * 600 = Rs. 75.",
                "points": 1
            },
            {
                "id": 2805,
                "topic_id": 28,
                "question": "A can finish a work in 18 days and B can do the same work in half the time taken by A. Working together, what part of the same work can they finish in a day?",
                "options_json": [
                    "1/6",
                    "1/9",
                    "2/9",
                    "1/12"
                ],
                "correct_answer": "1/6",
                "explanation": "A takes 18 days, B takes 18/2 = 9 days.\nRate A = 1/18, Rate B = 1/9 = 2/18.\nCombined daily work = 1/18 + 2/18 = 3/18 = 1/6 of total work.",
                "points": 1
            },
            {
                "id": 2806,
                "topic_id": 28,
                "question": "Two pipes can fill a tank in 15 hours and 20 hours respectively, while a third empties it in 30 hours. If all three are opened, the tank fills in:",
                "options_json": [
                    "12 hours",
                    "10 hours",
                    "14 hours",
                    "15 hours"
                ],
                "correct_answer": "12 hours",
                "explanation": "LCM(15, 20, 30) = 60 units. Rate A = +4, Rate B = +3, Rate C = -2.\nNet rate = 4 + 3 - 2 = 5 units/hr.\nTime = 60 / 5 = 12 hours.",
                "points": 1
            },
            {
                "id": 2807,
                "topic_id": 28,
                "question": "If 5 men or 9 women can do a piece of work in 19 days, then in how many days will 3 men and 6 women do it?",
                "options_json": [
                    "15 days",
                    "18 days",
                    "12 days",
                    "14 days"
                ],
                "correct_answer": "15 days",
                "explanation": "5M = 9W -> 1M = 9/5 W.\n3M + 6W = 3(9/5) + 6 = 27/5 + 30/5 = 57/5 W.\n9W * 19 = (57/5 W) * D -> D = (9 * 19 * 5) / 57 = (9 * 5) / 3 = 15 days.",
                "points": 1
            },
            {
                "id": 2808,
                "topic_id": 28,
                "question": "A is thrice as good a workman as B and therefore able to finish a job in 60 days less than B. Working together, they can do it in:",
                "options_json": [
                    "22.5 days",
                    "25 days",
                    "20 days",
                    "30 days"
                ],
                "correct_answer": "22.5 days",
                "explanation": "Efficiency A:B = 3:1 -> Time ratio A:B = 1:3.\nDifference in time = 3x - x = 2x = 60 days -> x = 30 days.\nA takes 30 days, B takes 90 days.\nTogether time = (30 * 90) / (30 + 90) = 2700 / 120 = 22.5 days.",
                "points": 1
            },
            {
                "id": 2809,
                "topic_id": 28,
                "question": "A and B can do a piece of work in 45 and 40 days respectively. They began the work together, but A left after some days and B finished the remaining work in 23 days. After how many days did A leave?",
                "options_json": [
                    "9 days",
                    "8 days",
                    "10 days",
                    "12 days"
                ],
                "correct_answer": "9 days",
                "explanation": "Total work = LCM(45, 40) = 360 units. Rate A = 8, Rate B = 9.\nB worked alone for 23 days: 23 * 9 = 207 units.\nWork done together before A left = 360 - 207 = 153 units.\nCombined rate = 8 + 9 = 17 units/day.\nDays worked together = 153 / 17 = 9 days.",
                "points": 1
            },
            {
                "id": 2810,
                "topic_id": 28,
                "question": "8 men can dig a pit in 20 days. If a man works half as efficiently as a boy, how many days will 4 men and 4 boys take?",
                "options_json": [
                    "13.33 days",
                    "15 days",
                    "12 days",
                    "16 days"
                ],
                "correct_answer": "13.33 days",
                "explanation": "1 Man = 0.5 Boy -> 1 Boy = 2 Men.\nTotal work = 8 Men * 20 days = 160 Man-days.\n4 Men + 4 Boys = 4 Men + 4(2 Men) = 4 + 8 = 12 Men.\nTime = 160 / 12 = 40 / 3 = 13.33 days.",
                "points": 1
            }
        ]
    },
    "29": {
        "title": "Time, Speed and Distance: Relative Speed, Train Mechanics & Boats/Streams",
        "source_id": 7,
        "content": {
            "definition": "Time, Speed and Distance (TSD) is the kinematic branch of arithmetic governing uniform motion, differential rates, relative frames of reference, and fluid velocity vectors. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions rigorously test unit conversions (km/h <-> m/s), trains crossing objects of negligible vs substantial lengths, relative velocity in head-on and overtaking trajectories, and upstream/downstream river currents.",
            "overview": "Fundamental Relations:\n- Distance = Speed x Time (D = S * T)\n- Conversion: 1 km/h = 5/18 m/s; 1 m/s = 18/5 km/h\n- Average Speed: For equal distances = 2xy / (x + y); for variable journeys = Total Distance / Total Time\n- Relative Speed: Same direction = S1 - S2; Opposite direction = S1 + S2\n- Trains: Crossing stationary point = L_train / S; Crossing platform = (L_train + L_platform) / S\n- Boats & Streams: Downstream = u + v; Upstream = u - v; Speed of boat in still water = (Downstream + Upstream) / 2; Speed of stream = (Downstream - Upstream) / 2",
            "types": [
                {
                    "name": "1. Unit Conversion & Average Speed",
                    "desc": "Foundational unit harmony and non-arithmetic harmonic means.",
                    "examples": [
                        "72 km/h in m/s = 72 * (5/18) = 20 m/s",
                        "25 m/s in km/h = 25 * (18/5) = 90 km/h",
                        "Average Speed over equal distance: 2xy / (x + y)"
                    ]
                },
                {
                    "name": "2. Relative Speed Frameworks",
                    "desc": "Evaluating moving frames of reference.",
                    "examples": [
                        "Overtaking (Same Direction): Relative Speed = S_fast - S_slow",
                        "Colliding / Meeting (Opposite Direction): Relative Speed = S1 + S2",
                        "Time to meet = Initial Distance between them / Relative Speed"
                    ]
                },
                {
                    "name": "3. Train Mechanics (Points vs Extended Platforms)",
                    "desc": "Accounting for vehicular physical length in transit equations.",
                    "examples": [
                        "Crossing pole/man/tree (negligible length): Distance = Length of Train",
                        "Crossing platform/bridge/tunnel: Distance = Length of Train + Length of Platform",
                        "Crossing another train in opposite direction: Distance = L1 + L2; Speed = S1 + S2"
                    ]
                },
                {
                    "name": "4. Boats and Streams (River Fluid Vector Motion)",
                    "desc": "Superposition of vessel velocity and stream current velocity.",
                    "examples": [
                        "Downstream Speed (with current) D = u + v",
                        "Upstream Speed (against current) U = u - v",
                        "Speed of boat u = (D + U) / 2; Speed of stream v = (D - U) / 2"
                    ]
                },
                {
                    "name": "5. Late and Early Arrival Proportions",
                    "desc": "Resolving distance when speeds yield differing arrival time margins.",
                    "examples": [
                        "At speed S1, student is t1 late; at speed S2, student is t2 early:",
                        "Distance = [S1 * S2 / |S1 - S2|] * (Total Time Difference in hours)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Speed-Time Inversion Rule for Constant Distance",
                    "explanation": "When the distance $D$ is constant, speed is inversely proportional to time: $\\frac{S_1}{S_2} = \\frac{T_2}{T_1}$. If a person travels at $\\frac{3}{4}$ of his usual speed, he takes $\\frac{4}{3}$ of his usual time.",
                    "words": [
                        "Constant Distance",
                        "Speed Time Inversion",
                        "3/4 speed -> 4/3 time"
                    ],
                    "correct": "At 3/4 usual speed, time taken is 4/3 usual time. Excess time = 4/3 - 1 = 1/3 of usual time.",
                    "incorrect": "Assuming time taken is 3/4 of usual time (confusing direct and inverse variation)."
                },
                {
                    "rule_number": 2,
                    "title": "Late-Early Constant Distance Shortcut Formula",
                    "explanation": "If an object travels at speed $S_1$ and arrives $t_1$ minutes late, and travels at $S_2$ arriving $t_2$ minutes early: $\\text{Distance} = \\frac{S_1 \\times S_2}{|S_1 - S_2|} \\times \\left(\\frac{\\Delta T}{60}\\right)$, where $\\Delta T = t_1 + t_2$ (late + early) in minutes.",
                    "words": [
                        "Late Early Formula",
                        "Product / Difference * Delta T",
                        "Distance Shortcut"
                    ],
                    "correct": "At 4 km/h, 10 min late; at 5 km/h, 5 min early: Dist = (4*5)/(5-4) * (15/60) = 20 * (1/4) = 5 km.",
                    "incorrect": "Subtracting 10 - 5 = 5 min instead of adding late + early = 15 min."
                },
                {
                    "rule_number": 3,
                    "title": "Extended Object Traversal Rule for Trains",
                    "explanation": "When a train of length $L_1$ crosses an object of length $L_2$, the effective distance covered is ALWAYS $L_1 + L_2$. The speed is the train's speed (if object is stationary) or the relative speed (if object is moving).",
                    "words": [
                        "Train Length",
                        "Platform Length",
                        "L1 + L2",
                        "Distance Covered"
                    ],
                    "correct": "A 200m train crossing a 300m platform covers Distance = 200 + 300 = 500m.",
                    "incorrect": "Using only platform length 300m or train length 200m."
                },
                {
                    "rule_number": 4,
                    "title": "Boats and Streams Canonical Equations",
                    "explanation": "If speed of boat in still water is $u$ and current velocity is $v$:\n(1) Downstream speed $D = u + v$\n(2) Upstream speed $U = u - v$\n(3) $u = \\frac{D + U}{2}$\n(4) $v = \\frac{D - U}{2}$",
                    "words": [
                        "Boats and Streams",
                        "u = (D+U)/2",
                        "v = (D-U)/2",
                        "Upstream Downstream"
                    ],
                    "correct": "A boat goes 24 km downstream in 2 hrs (D = 12 km/h) and 24 km upstream in 4 hrs (U = 6 km/h): Still water speed u = (12 + 6)/2 = 9 km/h; Stream v = (12 - 6)/2 = 3 km/h.",
                    "incorrect": "Calculating stream speed as 12 - 6 = 6 km/h without dividing by 2."
                },
                {
                    "rule_number": 5,
                    "title": "Post-Meeting Travel Equation (Fischer's Rule)",
                    "explanation": "Two trains start at the same time from $A$ and $B$ towards each other. After crossing each other, they take $T_1$ and $T_2$ hours respectively to reach their destinations. Then: $\\frac{S_1}{S_2} = \\sqrt{\\frac{T_2}{T_1}}$.",
                    "words": [
                        "Crossing Formula",
                        "S1/S2 = sqrt(T2/T1)",
                        "Post-Meeting Time"
                    ],
                    "correct": "After meeting, Train A takes 4 hours and Train B takes 9 hours: S_A / S_B = sqrt(9 / 4) = 3 / 2.",
                    "incorrect": "Setting S1/S2 = T2/T1 = 9/4 without the square root."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Calculating average speed as arithmetic mean (x + y)/2.",
                    "correction": "For equal distances, Average Speed is the harmonic mean: 2xy / (x + y).",
                    "rationale": "More time is spent traveling at the slower speed, weighting the average downward."
                },
                {
                    "mistake": "Mixing km/h and m/s units in the same calculation.",
                    "correction": "Always convert speeds to m/s when distances are in meters: multiply by 5/18.",
                    "rationale": "Formula D = S * T requires dimensional homogeneity."
                },
                {
                    "mistake": "Subtracting stream velocity when boat travels downstream.",
                    "correction": "Downstream means traveling WITH the river flow (add: u + v); Upstream means AGAINST the flow (subtract: u - v).",
                    "rationale": "Water velocity assists downstream transit and resists upstream transit."
                },
                {
                    "mistake": "Forgetting train length when crossing a person on a platform.",
                    "correction": "When crossing a person on a platform, distance is ONLY the train length (the person has negligible length), not train + platform.",
                    "rationale": "The question specifies the person, not the platform structure."
                }
            ],
            "quick_revision_points": [
                "Distance = Speed * Time.",
                "1 km/h = 5/18 m/s; 1 m/s = 18/5 km/h.",
                "Average speed for equal distances = 2xy / (x + y).",
                "Relative speed: Same direction = S1 - S2; Opposite direction = S1 + S2.",
                "Train crossing a pole: Distance = Length of Train.",
                "Train crossing a platform: Distance = Length of Train + Length of Platform.",
                "Boats: Speed of boat in still water = (Downstream + Upstream) / 2.",
                "Boats: Speed of stream = (Downstream - Upstream) / 2.",
                "After meeting time formula: S1 / S2 = sqrt(T2 / T1)."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2901,
                "topic_id": 29,
                "question": "A train 240 m long passes a pole in 24 seconds. How long will it take to pass a platform 650 m long? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "89 seconds",
                    "100 seconds",
                    "85 seconds",
                    "90 seconds"
                ],
                "correct_answer": "89 seconds",
                "explanation": "Speed of train = Length of train / Time = 240 / 24 = 10 m/s.\nTotal distance to cross platform = Length of train + Length of platform = 240 + 650 = 890 m.\nTime taken = 890 / 10 = 89 seconds.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2902,
                "topic_id": 29,
                "question": "A man can row 6 km/h in still water. If the speed of the current is 2 km/h, it takes him 3 hours more in upstream than in downstream for the same distance. Find the distance. [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "24 km",
                    "18 km",
                    "30 km",
                    "36 km"
                ],
                "correct_answer": "24 km",
                "explanation": "Downstream speed D = 6 + 2 = 8 km/h.\nUpstream speed U = 6 - 2 = 4 km/h.\nLet distance be d.\nTime difference: (d / 4) - (d / 8) = 3.\n(2d - d) / 8 = 3 -> d / 8 = 3 -> d = 24 km.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2903,
                "topic_id": 29,
                "question": "Two trains start at the same time from Aligarh and Delhi and proceed towards each other at 14 km/h and 21 km/h respectively. When they meet, it is found that one train has traveled 70 km more than the other. What is the distance between two stations? [UPSC CDS 2023]",
                "options_json": [
                    "350 km",
                    "300 km",
                    "420 km",
                    "280 km"
                ],
                "correct_answer": "350 km",
                "explanation": "Let time of travel until meeting be t hours.\nDistance by first train = 14t; Distance by second train = 21t.\nDifference in distance = 21t - 14t = 7t = 70 km -> t = 10 hours.\nTotal distance between stations = 14t + 21t = 35t = 35 * 10 = 350 km.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2901,
                "topic_id": 29,
                "question": "A car travels from A to B at 60 km/h and returns from B to A at 40 km/h. Find its average speed for the whole journey.",
                "options_json": [
                    "48 km/h",
                    "50 km/h",
                    "45 km/h",
                    "52 km/h"
                ],
                "correct_answer": "48 km/h",
                "explanation": "Harmonic mean = 2xy / (x + y) = (2 * 60 * 40) / (60 + 40) = 4800 / 100 = 48 km/h.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2902,
                "topic_id": 29,
                "question": "Walking at 3/4 of his usual speed, a man reaches his office 20 minutes late. Find his usual time to cover the distance.",
                "options_json": [
                    "60 minutes",
                    "50 minutes",
                    "80 minutes",
                    "45 minutes"
                ],
                "correct_answer": "60 minutes",
                "explanation": "Speed = 3/4 of usual -> Time = 4/3 of usual time T.\nDelay = (4/3)T - T = (1/3)T = 20 minutes.\nT = 20 * 3 = 60 minutes.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2903,
                "topic_id": 29,
                "question": "Two trains 140 m and 160 m long run at the speeds of 60 km/h and 40 km/h respectively in opposite directions on parallel tracks. What is the time (in seconds) they take to clear each other?",
                "options_json": [
                    "10.8 seconds",
                    "12.0 seconds",
                    "9.6 seconds",
                    "10.0 seconds"
                ],
                "correct_answer": "10.8 seconds",
                "explanation": "Total distance = 140 + 160 = 300 m.\nRelative speed (opposite) = 60 + 40 = 100 km/h = 100 * (5/18) = 250 / 9 m/s.\nTime = 300 / (250 / 9) = (300 * 9) / 250 = 2700 / 250 = 10.8 seconds.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2904,
                "topic_id": 29,
                "question": "A boat can travel with a speed of 13 km/h in still water. If the speed of the stream is 4 km/h, find the time taken by the boat to go 68 km downstream.",
                "options_json": [
                    "4 hours",
                    "5 hours",
                    "3 hours",
                    "4.5 hours"
                ],
                "correct_answer": "4 hours",
                "explanation": "Downstream speed = 13 + 4 = 17 km/h.\nTime taken = 68 / 17 = 4 hours.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2905,
                "topic_id": 29,
                "question": "If a person walks at 14 km/h instead of 10 km/h, he would have walked 20 km more. The actual distance traveled by him is:",
                "options_json": [
                    "50 km",
                    "70 km",
                    "60 km",
                    "80 km"
                ],
                "correct_answer": "50 km",
                "explanation": "Let actual distance be d. Time t is constant.\nd / 10 = (d + 20) / 14 -> 14d = 10d + 200 -> 4d = 200 -> d = 50 km.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2906,
                "topic_id": 29,
                "question": "A thief is spotted by a policeman from a distance of 100 meters. When the policeman starts the chase, the thief also starts running. If the speed of the thief is 8 km/h and that of the policeman is 10 km/h, how far will the thief have run before he is overtaken?",
                "options_json": [
                    "400 meters",
                    "500 meters",
                    "350 meters",
                    "450 meters"
                ],
                "correct_answer": "400 meters",
                "explanation": "Relative speed = 10 - 8 = 2 km/h = 2 * (5/18) = 5/9 m/s.\nTime to overtake = Distance / Relative speed = 100 / (5/9) = (100 * 9) / 5 = 180 seconds.\nDistance run by thief = Speed of thief * Time = [8 * (5/18)] * 180 = (40 / 18) * 180 = 400 meters.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2907,
                "topic_id": 29,
                "question": "Two stations A and B are 110 km apart on a straight line. One train starts from A at 7 a.m. and travels towards B at 20 km/h. Another train starts from B at 8 a.m. and travels towards A at 25 km/h. At what time will they meet?",
                "options_json": [
                    "10 a.m.",
                    "9 a.m.",
                    "10:30 a.m.",
                    "11 a.m."
                ],
                "correct_answer": "10 a.m.",
                "explanation": "At 8 a.m., the first train has traveled for 1 hour at 20 km/h = 20 km.\nDistance remaining at 8 a.m. = 110 - 20 = 90 km.\nRelative speed (opposite direction) = 20 + 25 = 45 km/h.\nTime to meet after 8 a.m. = 90 / 45 = 2 hours.\nMeeting time = 8 a.m. + 2 hours = 10 a.m.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2908,
                "topic_id": 29,
                "question": "A train passes two bridges of lengths 800 m and 400 m in 100 seconds and 60 seconds respectively. The length of the train is:",
                "options_json": [
                    "200 m",
                    "150 m",
                    "250 m",
                    "300 m"
                ],
                "correct_answer": "200 m",
                "explanation": "Let train length be L and speed be S.\n(L + 800) / 100 = S and (L + 400) / 60 = S.\n(L + 800) / 5 = (L + 400) / 3 -> 3L + 2400 = 5L + 2000.\n2L = 400 -> L = 200 m.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2909,
                "topic_id": 29,
                "question": "Two trains start at the same time from points A and B and arrive at their respective destinations 4 hours and 9 hours after they pass each other. Find the ratio of their speeds.",
                "options_json": [
                    "3 : 2",
                    "2 : 3",
                    "9 : 4",
                    "4 : 9"
                ],
                "correct_answer": "3 : 2",
                "explanation": "Formula: S1 / S2 = sqrt(T2 / T1) = sqrt(9 / 4) = 3 / 2.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2910,
                "topic_id": 29,
                "question": "In a 100 m race, A can beat B by 25 m and B can beat C by 4 m. In the same race, A can beat C by:",
                "options_json": [
                    "28 m",
                    "29 m",
                    "26 m",
                    "27 m"
                ],
                "correct_answer": "28 m",
                "explanation": "When A covers 100 m, B covers 75 m.\nWhen B covers 100 m, C covers 96 m.\nWhen B covers 75 m, C covers (96 / 100) * 75 = 96 * (3/4) = 72 m.\nTherefore, when A covers 100 m, C covers 72 m.\nA beats C by 100 - 72 = 28 m.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2901,
                "topic_id": 29,
                "question": "Convert 54 km/h into meters per second.",
                "options_json": [
                    "15 m/s",
                    "12 m/s",
                    "18 m/s",
                    "20 m/s"
                ],
                "correct_answer": "15 m/s",
                "explanation": "54 * (5/18) = 3 * 5 = 15 m/s.",
                "points": 1
            },
            {
                "id": 2902,
                "topic_id": 29,
                "question": "A train 125 m long passes a man running at 5 km/h in the same direction in 10 seconds. What is the speed of the train?",
                "options_json": [
                    "50 km/h",
                    "45 km/h",
                    "55 km/h",
                    "40 km/h"
                ],
                "correct_answer": "50 km/h",
                "explanation": "Relative speed = 125 / 10 = 12.5 m/s = 12.5 * (18/5) = 45 km/h.\nSince traveling in same direction: S_train - S_man = 45 -> S_train = 45 + 5 = 50 km/h.",
                "points": 1
            },
            {
                "id": 2903,
                "topic_id": 29,
                "question": "A boat goes 16 km upstream and 24 km downstream in 6 hours each. Find the speed of the current.",
                "options_json": [
                    "0.67 km/h",
                    "1 km/h",
                    "2 km/h",
                    "1.5 km/h"
                ],
                "correct_answer": "0.67 km/h",
                "explanation": "Downstream speed = 24 / 6 = 4 km/h. Upstream speed = 16 / 6 = 2.67 km/h.\nSpeed of current = (D - U) / 2 = (4 - 2.67) / 2 = 1.33 / 2 = 0.67 km/h.",
                "points": 1
            },
            {
                "id": 2904,
                "topic_id": 29,
                "question": "If a train 150 m long crosses an electric post in 5 seconds, what is its speed in km/h?",
                "options_json": [
                    "108 km/h",
                    "90 km/h",
                    "100 km/h",
                    "72 km/h"
                ],
                "correct_answer": "108 km/h",
                "explanation": "Speed = 150 / 5 = 30 m/s = 30 * (18/5) = 108 km/h.",
                "points": 1
            },
            {
                "id": 2905,
                "topic_id": 29,
                "question": "A man covers half of his journey at 6 km/h and the remaining half at 3 km/h. His average speed is:",
                "options_json": [
                    "4 km/h",
                    "4.5 km/h",
                    "5 km/h",
                    "3.5 km/h"
                ],
                "correct_answer": "4 km/h",
                "explanation": "Average speed = 2(6)(3) / (6 + 3) = 36 / 9 = 4 km/h.",
                "points": 1
            },
            {
                "id": 2906,
                "topic_id": 29,
                "question": "Two cars travel towards each other at 45 km/h and 63 km/h. By how much does the distance between them decrease in 1 minute?",
                "options_json": [
                    "1.8 km",
                    "2.0 km",
                    "1.5 km",
                    "1.2 km"
                ],
                "correct_answer": "1.8 km",
                "explanation": "Relative speed = 45 + 63 = 108 km/h.\nDistance in 1 minute = 108 / 60 = 1.8 km.",
                "points": 1
            },
            {
                "id": 2907,
                "topic_id": 29,
                "question": "A speed of 14 meters per second is the same as:",
                "options_json": [
                    "50.4 km/h",
                    "48 km/h",
                    "52 km/h",
                    "54 km/h"
                ],
                "correct_answer": "50.4 km/h",
                "explanation": "14 * (18/5) = 252 / 5 = 50.4 km/h.",
                "points": 1
            },
            {
                "id": 2908,
                "topic_id": 29,
                "question": "A train running at 54 km/h crosses a 250 m long platform in 30 seconds. What is the length of the train?",
                "options_json": [
                    "200 m",
                    "250 m",
                    "150 m",
                    "180 m"
                ],
                "correct_answer": "200 m",
                "explanation": "Speed = 54 * (5/18) = 15 m/s.\nTotal distance = 15 * 30 = 450 m.\nLength of train = 450 - 250 = 200 m.",
                "points": 1
            },
            {
                "id": 2909,
                "topic_id": 29,
                "question": "If a man walks 20 km at 5 km/h, he will be 40 minutes late. If he walks at 8 km/h, how early from the scheduled time will he arrive?",
                "options_json": [
                    "50 minutes",
                    "40 minutes",
                    "30 minutes",
                    "60 minutes"
                ],
                "correct_answer": "50 minutes",
                "explanation": "Time at 5 km/h = 20 / 5 = 4 hours = 240 minutes.\nSince he is 40 min late: Scheduled time = 240 - 40 = 200 minutes.\nTime at 8 km/h = 20 / 8 = 2.5 hours = 150 minutes.\nHe arrives early by: 200 - 150 = 50 minutes early.",
                "points": 1
            },
            {
                "id": 2910,
                "topic_id": 29,
                "question": "In a race of 200 m, B can give a start of 10 m to A and C can give a start of 20 m to B. What start can C give to A in the same race?",
                "options_json": [
                    "29 m",
                    "30 m",
                    "28 m",
                    "25 m"
                ],
                "correct_answer": "29 m",
                "explanation": "B:A = 200:190 = 20:19.\nC:B = 200:180 = 10:9 = 20:18? Wait: C gives 20m start to B in 200m race -> when C covers 200m, B covers 180m. Ratio C:B = 200:180 = 10:9.\nB:A = 200:190 = 20:19.\nWhen C covers 200m, B covers 180m.\nWhen B covers 200m, A covers 190m -> When B covers 180m, A covers (190/200)*180 = 171m.\nC beats A by 200 - 171 = 29m. So C can give A a start of 29m.",
                "points": 1
            }
        ]
    },
    "30": {
        "title": "Simple Interest: Principal Growth, Annual Rate Calculations & Installment Formulas",
        "source_id": 7,
        "content": {
            "definition": "Simple Interest (SI) is the linear mathematical model of capital growth where interest is computed exclusively on the original Principal ($P$) for the entire investment duration ($T$ at rate $R\\%$ per annum): $\\text{SI} = \\frac{P \\times R \\times T}{100}$. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions evaluate doubling periods, splitting capital across unequal rate brackets, monthly installment loan repayments, and changes in interest rates over elapsed time.",
            "overview": "Fundamental Equations:\n- $\\text{SI} = \\frac{P \\times R \\times T}{100}$\n- $\\text{Amount } A = P + \\text{SI} = P \\left(1 + \\frac{RT}{100}\\right)$\n- Principal: $P = \\frac{100 \\times \\text{SI}}{R \\times T} = \\frac{100 \\times A}{100 + RT}$\n- Doubling Rule: If a sum becomes $n$ times itself in $T$ years: $R = \\frac{(n - 1) \\times 100}{T}$.\n- Installment Debt Formula: $A = n \\times x + \\frac{x \\times R \\times n(n - 1)}{200}$, where $x = \\text{installment amount}$.",
            "types": [
                {
                    "name": "1. Standard Principal, Rate & Time Calculations",
                    "desc": "Linear proportional interest evaluation over integer and fractional years.",
                    "examples": [
                        "SI on Rs. 5000 at 8% per annum for 3 years: (5000 * 8 * 3) / 100 = Rs. 1200.",
                        "Amount = 5000 + 1200 = Rs. 6200."
                    ]
                },
                {
                    "name": "2. Sum Multiplier Rule (Doubling / Tripling of Capital)",
                    "desc": "Evaluating temporal cycles when principal scales to n-fold value.",
                    "examples": [
                        "A sum doubles (n = 2) in 8 years: Rate R = (2 - 1) * 100 / 8 = 100 / 8 = 12.5%.",
                        "A sum triples in 12 years: (3 - 1) * 100 / 12 = 200 / 12 = 16.67%."
                    ]
                },
                {
                    "name": "3. Piecewise Variable Rates Over Time",
                    "desc": "Evaluating interest across tiered chronological rate windows.",
                    "examples": [
                        "Rate is 6% for first 2 years, 9% for next 3 years, 14% for period beyond 5 years.",
                        "Total SI % for 8 years = (2*6) + (3*9) + (3*14) = 12 + 27 + 42 = 81%."
                    ]
                },
                {
                    "name": "4. Splitting Capital into Proportional Parts",
                    "desc": "Dividing sum S into parts such that interests or amounts are equal.",
                    "examples": [
                        "Divide Rs. 2600 into two parts such that SI on 1st part at 10% for 5 years = SI on 2nd part at 9% for 6 years.",
                        "P1 * 50 = P2 * 54 -> P1 / P2 = 54 / 50 = 27 / 25."
                    ]
                },
                {
                    "name": "5. Annual Equal Installments for Discharging Debt",
                    "desc": "Clearing an accumulated future debt through equal periodic payments.",
                    "examples": [
                        "Annual installment x to discharge debt A in n years at R%: A = n*x + [x * R * n(n - 1)] / 200."
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Simple Interest Formula",
                    "explanation": "Simple interest is strictly constant each year: $\\text{SI} = \\frac{P \\times R \\times T}{100}$. Interest does not compound upon itself.",
                    "words": [
                        "PTR / 100",
                        "Linear Interest",
                        "Constant Annual Interest"
                    ],
                    "correct": "At 10% on Rs. 1000: Year 1 = Rs. 100, Year 2 = Rs. 100, Year 3 = Rs. 100. Total = Rs. 300.",
                    "incorrect": "Calculating Year 2 interest on Rs. 1100 (confusing SI with Compound Interest)."
                },
                {
                    "rule_number": 2,
                    "title": "Capital Scaling Shortcut: $T = \\frac{(n - 1) \\times 100}{R}$",
                    "explanation": "If a sum of money becomes $n$ times itself, the Interest accrued is $(n - 1)P$. Therefore: $(n - 1)P = \\frac{P \\times R \\times T}{100} \\implies T = \\frac{(n - 1) \\times 100}{R}$.",
                    "words": [
                        "Sum Doubles",
                        "(n - 1) * 100 / R",
                        "Capital Multiplier"
                    ],
                    "correct": "A sum becomes 4 times itself: Interest = 3P. Time T = (4 - 1)*100 / R = 300 / R.",
                    "incorrect": "Using 4P as the interest: 4 * 100 / R (Treats total amount as interest)."
                },
                {
                    "rule_number": 3,
                    "title": "Two-Period Amount Subtraction Trick",
                    "explanation": "If a principal amounts to $A_1$ in $T_1$ years and $A_2$ in $T_2$ years, the interest accrued between the two periods is: $\\text{SI for } (T_2 - T_1) \\text{ years} = A_2 - A_1$. Hence, annual interest = $\\frac{A_2 - A_1}{T_2 - T_1}$.",
                    "words": [
                        "Amount Difference",
                        "Annual SI",
                        "A2 - A1"
                    ],
                    "correct": "Amounts to Rs. 750 in 3 yrs and Rs. 850 in 5 yrs: SI for 2 yrs = 850 - 750 = 100 -> SI/year = 50. Principal = 750 - 3(50) = Rs. 600.",
                    "incorrect": "Setting 750 / 3 = 250 as annual interest (Amount contains principal)."
                },
                {
                    "rule_number": 4,
                    "title": "Equal Amount Division Shortcut",
                    "explanation": "If a sum is divided into parts such that the amounts are equal after $T_1, T_2, ...$ at rates $R_1, R_2, ...$, the ratio of capitals is: $P_1 : P_2 : P_3 = \\frac{1}{100 + R_1 T_1} : \\frac{1}{100 + R_2 T_2} : \\frac{1}{100 + R_3 T_3}$.",
                    "words": [
                        "Equal Amounts",
                        "Inverse Proportional",
                        "1 / (100 + RT)"
                    ],
                    "correct": "Dividing sum into two parts yielding equal amounts: P1 : P2 = 1/(100 + R1 T1) : 1/(100 + R2 T2).",
                    "incorrect": "Using P1 : P2 = 1/(R1 T1) : 1/(R2 T2) (This ratio is only valid when interests are equal, not amounts)."
                },
                {
                    "rule_number": 5,
                    "title": "Debt Installment Formula",
                    "explanation": "To discharge a debt of amount $A$ due in $n$ years at $R\\%$ simple interest, the annual installment $x$ is: $x = \\frac{100 A}{100n + \\frac{R n (n - 1)}{2}}$.",
                    "words": [
                        "Installment",
                        "Discharging Debt",
                        "Annual Payment"
                    ],
                    "correct": "Debt of Rs. 848 due in 4 years at 4%: x = (100 * 848) / [100(4) + 4*4*3/2] = 84800 / (400 + 24) = 84800 / 424 = Rs. 200.",
                    "incorrect": "Dividing total debt by 4 directly: 848 / 4 = Rs. 212 (Omits accrued interest on paid installments)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Treating Amount as Interest when calculating rate.",
                    "correction": "Always subtract Principal from Amount to obtain the true Interest: SI = A - P.",
                    "rationale": "Formulas like PRT/100 solve for Interest, not Amount."
                },
                {
                    "mistake": "Using months directly in formula without converting to years.",
                    "correction": "If time is given in months (e.g. 9 months), divide by 12: T = 9/12 = 3/4 years.",
                    "rationale": "Rate R is defined per annum (annually)."
                },
                {
                    "mistake": "Applying Compound Interest formula to Simple Interest problems.",
                    "correction": "SI increases linearly by equal arithmetic increments each year.",
                    "rationale": "SI does not compound on past interest."
                },
                {
                    "mistake": "Confusing 'equal interest' with 'equal amount' in capital split questions.",
                    "correction": "Equal interest: P1*R1*T1 = P2*R2*T2. Equal amount: P1*(100 + R1*T1) = P2*(100 + R2*T2).",
                    "rationale": "Amounts include the initial principal."
                }
            ],
            "quick_revision_points": [
                "SI = (P * R * T) / 100.",
                "Amount = P + SI = P[1 + (RT/100)].",
                "Rate when sum becomes n-fold in T years: R = (n - 1) * 100 / T.",
                "Annual SI between two amounts = (A2 - A1) / (T2 - T1).",
                "Time in months must be divided by 12; days divided by 365.",
                "Equal interest ratio: P1 : P2 = (1 / R1*T1) : (1 / R2*T2).",
                "Equal amount ratio: P1 : P2 = [1 / (100 + R1*T1)] : [1 / (100 + R2*T2)].",
                "Installment x = (100 * A) / [100n + R*n*(n-1)/2]."
            ]
        },
        "previous_year_questions": [
            {
                "id": 3001,
                "topic_id": 30,
                "question": "A sum of money amounts to Rs. 7,560 in 3 years and to Rs. 8,748 in 5 years at simple interest. Find the rate of interest. [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "10.27%",
                    "10.00%",
                    "9.50%",
                    "10.50%"
                ],
                "correct_answer": "10.27%",
                "explanation": "SI for 2 years (5 - 3) = 8748 - 7560 = Rs. 1188.\nSI for 1 year = 1188 / 2 = Rs. 594.\nSI for 3 years = 3 * 594 = Rs. 1782.\nPrincipal P = Amount after 3 years - SI for 3 years = 7560 - 1782 = Rs. 5778.\nRate R = (SI * 100) / (P * T) = (594 * 100) / (5778 * 1) = 59400 / 5778 = 10.28% approx 10.27%.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3002,
                "topic_id": 30,
                "question": "A sum of money doubles itself in 7 years at simple interest. In how many years will it become 4 times of itself? [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "21 years",
                    "14 years",
                    "28 years",
                    "18 years"
                ],
                "correct_answer": "21 years",
                "explanation": "When sum doubles, Interest = P in 7 years.\nTo become 4 times itself, Interest = 3P.\nSince Simple Interest is directly proportional to time:\nTime = 3 * 7 = 21 years.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3003,
                "topic_id": 30,
                "question": "What annual payment will discharge a debt of Rs. 6,450 due in 4 years at 5% simple interest? [UPSC CDS 2023]",
                "options_json": [
                    "Rs. 1,500",
                    "Rs. 1,450",
                    "Rs. 1,600",
                    "Rs. 1,550"
                ],
                "correct_answer": "Rs. 1,500",
                "explanation": "Formula: x = (100 * A) / [100n + R*n*(n-1)/2]\nHere A = 6450, n = 4, R = 5%.\nDenominator = 100(4) + [5 * 4 * 3 / 2] = 400 + 30 = 430.\nx = (100 * 6450) / 430 = 645000 / 430 = Rs. 1500.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3001,
                "topic_id": 30,
                "question": "A sum of Rs. 12,500 amounts to Rs. 15,500 in 4 years at simple interest. What is the rate of interest?",
                "options_json": [
                    "6%",
                    "5%",
                    "7%",
                    "8%"
                ],
                "correct_answer": "6%",
                "explanation": "SI = 15500 - 12500 = Rs. 3000.\nR = (SI * 100) / (P * T) = (3000 * 100) / (12500 * 4) = 300,000 / 50,000 = 6%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3002,
                "topic_id": 30,
                "question": "A sum becomes 3 times itself in 10 years at simple interest. What is the rate of interest per annum?",
                "options_json": [
                    "20%",
                    "25%",
                    "15%",
                    "30%"
                ],
                "correct_answer": "20%",
                "explanation": "R = (n - 1) * 100 / T = (3 - 1) * 100 / 10 = 200 / 10 = 20%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3003,
                "topic_id": 30,
                "question": "If the simple interest on a certain sum for 3 years at the rate of 4% per annum is Rs. 100 less than the simple interest on the same sum for 4 years at 5% per annum, find the sum.",
                "options_json": [
                    "Rs. 1250",
                    "Rs. 1000",
                    "Rs. 1500",
                    "Rs. 1200"
                ],
                "correct_answer": "Rs. 1250",
                "explanation": "SI1 = P * 4 * 3 / 100 = 12P / 100.\nSI2 = P * 5 * 4 / 100 = 20P / 100.\nSI2 - SI1 = 8P / 100 = 100 -> P = (100 * 100) / 8 = 10,000 / 8 = Rs. 1250.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3004,
                "topic_id": 30,
                "question": "A sum was put at simple interest at a certain rate for 2 years. Had it been put at 3% higher rate, it would have fetched Rs. 300 more. Find the sum.",
                "options_json": [
                    "Rs. 5000",
                    "Rs. 4500",
                    "Rs. 6000",
                    "Rs. 4000"
                ],
                "correct_answer": "Rs. 5000",
                "explanation": "Extra interest = P * Delta_R * T / 100 = P * 3 * 2 / 100 = 6P / 100 = 300.\nP = 300 * 100 / 6 = Rs. 5000.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3005,
                "topic_id": 30,
                "question": "A person borrows Rs. 5000 for 2 years at 4% per annum simple interest. He immediately lends it to another person at 6.25% per annum simple interest for 2 years. Find his gain in the transaction per year.",
                "options_json": [
                    "Rs. 112.50",
                    "Rs. 225.00",
                    "Rs. 125.00",
                    "Rs. 150.00"
                ],
                "correct_answer": "Rs. 112.50",
                "explanation": "Gain per year = Difference in rates * Principal = (6.25% - 4%) of 5000 = 2.25% of 5000 = 2.25 * 50 = Rs. 112.50.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3006,
                "topic_id": 30,
                "question": "In how many years will a sum of money triple itself at 12% per annum simple interest?",
                "options_json": [
                    "16 years 8 months",
                    "16 years 6 months",
                    "15 years",
                    "18 years"
                ],
                "correct_answer": "16 years 8 months",
                "explanation": "T = (n - 1) * 100 / R = (3 - 1) * 100 / 12 = 200 / 12 = 50 / 3 = 16(2/3) years = 16 years and 8 months.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3007,
                "topic_id": 30,
                "question": "Rs. 2100 is divided into two parts such that simple interest on the first part for 4 years at 8% per annum is equal to simple interest on the second part for 2 years at 9% per annum. Find the second part.",
                "options_json": [
                    "Rs. 1344",
                    "Rs. 756",
                    "Rs. 1200",
                    "Rs. 1400"
                ],
                "correct_answer": "Rs. 1344",
                "explanation": "P1 * 4 * 8 = P2 * 2 * 9 -> 32 P1 = 18 P2 -> P1 / P2 = 18 / 32 = 9 / 16.\nSum of ratio terms = 9 + 16 = 25.\nSecond part P2 = (16 / 25) * 2100 = 16 * 84 = Rs. 1344.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3008,
                "topic_id": 30,
                "question": "A sum of money at simple interest amounts to Rs. 815 in 3 years and to Rs. 854 in 4 years. The sum is:",
                "options_json": [
                    "Rs. 698",
                    "Rs. 700",
                    "Rs. 690",
                    "Rs. 710"
                ],
                "correct_answer": "Rs. 698",
                "explanation": "SI for 1 year = 854 - 815 = Rs. 39.\nSI for 3 years = 3 * 39 = Rs. 117.\nPrincipal = 815 - 117 = Rs. 698.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3009,
                "topic_id": 30,
                "question": "At what rate percent per annum will a sum of Rs. 4000 produce Rs. 720 as simple interest in 2 years 6 months?",
                "options_json": [
                    "7.2%",
                    "7.5%",
                    "6.8%",
                    "8.0%"
                ],
                "correct_answer": "7.2%",
                "explanation": "Time T = 2.5 years = 5/2 years.\nR = (SI * 100) / (P * T) = (720 * 100) / (4000 * 2.5) = 72,000 / 10,000 = 7.2%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3010,
                "topic_id": 30,
                "question": "The rate of simple interest for the first 3 years is 6% p.a., for the next 4 years it is 8% p.a., and for the period beyond 7 years it is 13% p.a. If a person gets Rs. 1,520 as simple interest after 9 years, how much money did he deposit?",
                "options_json": [
                    "Rs. 2000",
                    "Rs. 2500",
                    "Rs. 1800",
                    "Rs. 2200"
                ],
                "correct_answer": "Rs. 2000",
                "explanation": "Total SI % = (3 * 6%) + (4 * 8%) + (2 * 13%) = 18% + 32% + 26% = 76%.\n76% of P = 1520 -> P = (1520 / 76) * 100 = 20 * 100 = Rs. 2000.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 3001,
                "topic_id": 30,
                "question": "How much simple interest will Rs. 2000 earn in 18 months at 6% per annum?",
                "options_json": [
                    "Rs. 180",
                    "Rs. 160",
                    "Rs. 200",
                    "Rs. 240"
                ],
                "correct_answer": "Rs. 180",
                "explanation": "T = 18/12 = 1.5 years. SI = (2000 * 6 * 1.5) / 100 = 20 * 9 = Rs. 180.",
                "points": 1
            },
            {
                "id": 3002,
                "topic_id": 30,
                "question": "A sum of money doubles itself in 5 years at simple interest. What is the annual rate of interest?",
                "options_json": [
                    "20%",
                    "25%",
                    "15%",
                    "10%"
                ],
                "correct_answer": "20%",
                "explanation": "R = (2 - 1) * 100 / 5 = 100 / 5 = 20%.",
                "points": 1
            },
            {
                "id": 3003,
                "topic_id": 30,
                "question": "Find the simple interest on Rs. 7300 at 5% per annum from 5th January to 31st May (non-leap year).",
                "options_json": [
                    "Rs. 146",
                    "Rs. 150",
                    "Rs. 140",
                    "Rs. 156"
                ],
                "correct_answer": "Rs. 146",
                "explanation": "Days: Jan 26 + Feb 28 + Mar 31 + Apr 30 + May 31 = 146 days = 146 / 365 years = 2 / 5 years.\nSI = (7300 * 5 * 2/5) / 100 = 73 * 2 = Rs. 146.",
                "points": 1
            },
            {
                "id": 3004,
                "topic_id": 30,
                "question": "A sum amounts to Rs. 9800 in 5 years and Rs. 12005 in 8 years at the same rate of simple interest. The rate of interest per annum is:",
                "options_json": [
                    "12%",
                    "10%",
                    "8%",
                    "15%"
                ],
                "correct_answer": "12%",
                "explanation": "SI for 3 years = 12005 - 9800 = 2205 -> SI for 1 year = 735.\nSI for 5 years = 5 * 735 = 3675.\nP = 9800 - 3675 = 6125.\nR = (735 * 100) / 6125 = 73500 / 6125 = 12%.",
                "points": 1
            },
            {
                "id": 3005,
                "topic_id": 30,
                "question": "What sum of money will amount to Rs. 520 in 5 years and to Rs. 568 in 7 years at simple interest?",
                "options_json": [
                    "Rs. 400",
                    "Rs. 450",
                    "Rs. 380",
                    "Rs. 420"
                ],
                "correct_answer": "Rs. 400",
                "explanation": "SI for 2 years = 568 - 520 = 48 -> SI/year = 24.\nSI for 5 years = 5 * 24 = 120.\nP = 520 - 120 = Rs. 400.",
                "points": 1
            },
            {
                "id": 3006,
                "topic_id": 30,
                "question": "In how many years will the simple interest on a sum of money be equal to the principal at 16(2/3)% per annum?",
                "options_json": [
                    "6 years",
                    "5 years",
                    "8 years",
                    "7 years"
                ],
                "correct_answer": "6 years",
                "explanation": "SI = P -> P = (P * 50/3 * T) / 100 -> 1 = T / 6 -> T = 6 years.",
                "points": 1
            },
            {
                "id": 3007,
                "topic_id": 30,
                "question": "If Rs. 64 amounts to Rs. 83.20 in 2 years, what will Rs. 86 amount to in 4 years at the same rate?",
                "options_json": [
                    "Rs. 137.60",
                    "Rs. 135.00",
                    "Rs. 140.20",
                    "Rs. 130.50"
                ],
                "correct_answer": "Rs. 137.60",
                "explanation": "SI = 83.20 - 64 = 19.20. R = (19.20 * 100) / (64 * 2) = 1920 / 128 = 15%.\nNew SI on 86 for 4 yrs at 15% = (86 * 15 * 4) / 100 = 86 * 0.60 = Rs. 51.60.\nAmount = 86 + 51.60 = Rs. 137.60.",
                "points": 1
            },
            {
                "id": 3008,
                "topic_id": 30,
                "question": "A sum of money triples itself in 16 years. In how many years will it become 5 times itself at the same rate of simple interest?",
                "options_json": [
                    "32 years",
                    "24 years",
                    "30 years",
                    "28 years"
                ],
                "correct_answer": "32 years",
                "explanation": "Triples (Interest = 2P) in 16 years -> Rate produces P in 8 years.\n5 times itself (Interest = 4P) -> Time = 4 * 8 = 32 years.",
                "points": 1
            },
            {
                "id": 3009,
                "topic_id": 30,
                "question": "The simple interest on a sum of money is 4/9 of the principal. Find the rate percent and time if both are numerically equal.",
                "options_json": [
                    "6.67%",
                    "6.00%",
                    "7.50%",
                    "8.00%"
                ],
                "correct_answer": "6.67%",
                "explanation": "SI = (4/9)P. Since R = T: (4/9)P = (P * R * R) / 100 -> R^2 = 400 / 9 -> R = 20 / 3 = 6.67%.",
                "points": 1
            },
            {
                "id": 3010,
                "topic_id": 30,
                "question": "What annual payment will discharge a debt of Rs. 770 due in 5 years at 5% simple interest?",
                "options_json": [
                    "Rs. 140",
                    "Rs. 150",
                    "Rs. 135",
                    "Rs. 145"
                ],
                "correct_answer": "Rs. 140",
                "explanation": "x = (100 * 770) / [100(5) + 5*5*4/2] = 77000 / [500 + 50] = 77000 / 550 = Rs. 140.",
                "points": 1
            }
        ]
    },
    "31": {
        "title": "Compound Interest: Effective Rate Tree, CI-SI Differences & Compounding Intervals",
        "source_id": 7,
        "content": {
            "definition": "Compound Interest (CI) is the exponential geometric model of capital accumulation where accrued interest is periodically capitalized into the principal, earning interest upon interest across successive intervals: $A = P \\left(1 + \\frac{R}{100}\\right)^t$. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions evaluate non-annual compounding (half-yearly, quarterly, 8-monthly), CI-SI difference shortcuts, effective rate tree diagrams (Pascal triangle multipliers: 2:1 for 2 years, 3:3:1 for 3 years), and annual installment calculations.",
            "overview": "Fundamental Principles:\n- Annual Compounding: $A = P(1 + R/100)^t; \\quad CI = A - P = P[(1 + R/100)^t - 1]$\n- Half-Yearly Compounding: Rate becomes $R/2\\%$, Time becomes $2t$ periods\n- Quarterly Compounding: Rate becomes $R/4\\%$, Time becomes $4t$ periods\n- CI - SI Difference for 2 Years: $\\text{Diff}_2 = P \\left(\\frac{R}{100}\\right)^2$\n- CI - SI Difference for 3 Years: $\\text{Diff}_3 = P \\left(\\frac{R}{100}\\right)^2 \\left(\\frac{300 + R}{100}\\right)$\n- Tree Method Ratio Multipliers:\n  - 2 Years: $2A + B$ (where $A = P \\times R\\%$, $B = A \\times R\\%$)\n  - 3 Years: $3A + 3B + C$ (where $C = B \\times R\\%$)",
            "types": [
                {
                    "name": "1. Compounding Frequency Shifts (Half-Yearly & Quarterly)",
                    "desc": "Adjusting the nominal annual rate and temporal compounding cycles.",
                    "examples": [
                        "Half-yearly: R' = R/2, n' = 2n",
                        "Quarterly: R' = R/4, n' = 4n",
                        "8-Monthly: R' = R * (8/12), n' = n * (12/8)"
                    ]
                },
                {
                    "name": "2. CI - SI Difference Shortcuts",
                    "desc": "Direct algebraic formulas relating 2-year and 3-year divergence between CI and SI.",
                    "examples": [
                        "2-Year Difference: Diff = P * (R/100)^2",
                        "3-Year Difference: Diff = P * (R/100)^2 * [(300 + R) / 100]"
                    ]
                },
                {
                    "name": "3. The Effective Rate Tree Method (Pascal Multipliers)",
                    "desc": "Fast mental calculation bypassing binomial powers.",
                    "examples": [
                        "P = 10,000, R = 10%, T = 3 years:",
                        "A = 10% of 10,000 = 1000",
                        "B = 10% of 1000 = 100",
                        "C = 10% of 100 = 10",
                        "Total CI = 3A + 3B + C = 3(1000) + 3(100) + 10 = Rs. 3310"
                    ]
                },
                {
                    "name": "4. Capital Scaling in Equal Time Intervals (Geometric Progression)",
                    "desc": "Under CI, a principal scales by equal multiplicative factors over equal durations.",
                    "examples": [
                        "If sum amounts to A1 in t years and A2 in 2t years: P = (A1^2) / A2",
                        "Example: Sum amounts to 4500 in 2 years and 6750 in 4 years: P = 4500^2 / 6750 = Rs. 3000"
                    ]
                },
                {
                    "name": "5. Compound Interest Installments",
                    "desc": "Loan amortizations repaid in equal annual compound installments.",
                    "examples": [
                        "Principal P borrowed at R% repaid in 2 equal annual installments x:",
                        "P = x / (1 + R/100) + x / (1 + R/100)^2"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Two-Year CI - SI Difference Formula",
                    "explanation": "The difference between Compound Interest and Simple Interest on a principal $P$ for 2 years at an annual rate $R\\%$ is given by: $\\text{Diff}_2 = P \\left(\\frac{R}{100}\\right)^2$.",
                    "words": [
                        "CI - SI Difference",
                        "P(R/100)^2",
                        "2-Year Difference"
                    ],
                    "correct": "If Diff = Rs. 45 for 2 years at 15%: 45 = P * (15/100)^2 = P * (225 / 10000) -> P = (45 * 10000) / 225 = Rs. 2000.",
                    "incorrect": "Calculating 2-year CI and 2-year SI separately and subtracting, wasting exam minutes."
                },
                {
                    "rule_number": 2,
                    "title": "Three-Year CI - SI Difference Formula",
                    "explanation": "The difference between Compound Interest and Simple Interest for 3 years is: $\\text{Diff}_3 = P \\left(\\frac{R}{100}\\right)^2 \\times \\left(\\frac{300 + R}{100}\\right) = \\text{Diff}_2 \\times \\left(3 + \\frac{R}{100}\\right)$.",
                    "words": [
                        "3-Year Difference",
                        "(300 + R)/100",
                        "Three Year Gap"
                    ],
                    "correct": "At 10% on Rs. 1000 for 3 yrs: Diff = 1000 * (1/10)^2 * (310/100) = 1000 * (1/100) * 3.1 = Rs. 31.",
                    "incorrect": "Assuming 3-year difference is simply 3 times the 2-year difference (Omits interest on interest)."
                },
                {
                    "rule_number": 3,
                    "title": "Geometric Progression of Sum under Compound Interest",
                    "explanation": "Under constant compound interest, the amounts form a geometric progression across equal time intervals. If a sum amounts to $A_1$ in $T$ years and $A_2$ in $2T$ years, the initial principal is: $P = \\frac{A_1^2}{A_2}$.",
                    "words": [
                        "Geometric Growth",
                        "A1^2 / A2",
                        "Equal Time Intervals"
                    ],
                    "correct": "Rs. 650 in 1 year and Rs. 676 in 2 years: P = 650^2 / 676 = 422500 / 676 = Rs. 625.",
                    "incorrect": "Assuming arithmetic difference: 650 - (676 - 650) = 624 (SI assumption)."
                },
                {
                    "rule_number": 4,
                    "title": "Equal Annual Compound Installment Rule",
                    "explanation": "A loan of principal $P$ repaid in $n$ equal annual installments $x$ at $R\\%$ compound interest satisfies: $P = \\frac{x}{\\left(1 + \\frac{R}{100}\\right)} + \\frac{x}{\\left(1 + \\frac{R}{100}\\right)^2} + ... + \\frac{x}{\\left(1 + \\frac{R}{100}\\right)^n}$.",
                    "words": [
                        "Amortization",
                        "Compound Installment",
                        "Present Value of Installments"
                    ],
                    "correct": "Borrow Rs. 2100 at 10% for 2 equal installments: 2100 = x/(1.1) + x/(1.21) = (1.1x + x)/1.21 = 2.1x / 1.21 -> x = Rs. 1210.",
                    "incorrect": "Using simple interest installment formula on a compound interest loan."
                },
                {
                    "rule_number": 5,
                    "title": "Tree Ratio Multiplier Method (Pascal 2:1 and 3:3:1)",
                    "explanation": "For 2 years, $\\text{CI} = 2A + B$. For 3 years, $\\text{CI} = 3A + 3B + C$, where $A = P \\times R\\%$, $B = A \\times R\\%$, and $C = B \\times R\\%$. Note that Simple Interest is simply $2A$ or $3A$, making the difference $\\text{Diff}_2 = B$ and $\\text{Diff}_3 = 3B + C$.",
                    "words": [
                        "Tree Method",
                        "Pascal Multiplier",
                        "3A + 3B + C",
                        "Fast CI"
                    ],
                    "correct": "For 3 years at 5% on 8000: A = 400, B = 20, C = 1. CI = 3(400) + 3(20) + 1 = 1200 + 60 + 1 = Rs. 1261. Difference = 61.",
                    "incorrect": "Calculating 8000 * (1.05)^3 = 8000 * 1.157625 manually with heavy decimals."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Failing to halve the rate and double the periods for half-yearly compounding.",
                    "correction": "For 10% p.a. compounded half-yearly for 1 year: R = 5% per half-year, and periods n = 2.",
                    "rationale": "Compounding frequency alters the discrete calculation period."
                },
                {
                    "mistake": "Confusing the 2-year difference formula with the 3-year difference formula.",
                    "correction": "2-year diff is P(R/100)^2. 3-year diff is P(R/100)^2 * [(300 + R)/100].",
                    "rationale": "The 3-year formula includes an additional factor for the 3rd year interest on B."
                },
                {
                    "mistake": "Assuming CI doubles at the same pace as SI.",
                    "correction": "If a sum doubles in 3 years at CI, it becomes 4 times in 6 years and 8 times in 9 years (powers of 2, not multiples).",
                    "rationale": "Compound interest scales exponentially: 2^k."
                },
                {
                    "mistake": "Applying linear subtraction to consecutive year amounts.",
                    "correction": "Interest of year 2 minus interest of year 1 is the interest earned ON the interest of year 1.",
                    "rationale": "CI base expands dynamically every period."
                }
            ],
            "quick_revision_points": [
                "A = P(1 + R/100)^t; CI = A - P.",
                "Half-yearly: Rate = R/2, Time = 2t; Quarterly: Rate = R/4, Time = 4t.",
                "CI - SI for 2 years = P * (R / 100)^2.",
                "CI - SI for 3 years = P * (R / 100)^2 * [(300 + R) / 100].",
                "If a sum becomes n-fold in t years, it becomes n^k-fold in (k * t) years at CI.",
                "If sum amounts to A1 in t years and A2 in 2t years: P = A1^2 / A2.",
                "Tree multipliers: 2 Years = 2A + B; 3 Years = 3A + 3B + C.",
                "2 Equal installments: P = x/(1 + R/100) + x/(1 + R/100)^2."
            ]
        },
        "previous_year_questions": [
            {
                "id": 3101,
                "topic_id": 31,
                "question": "The difference between compound interest and simple interest on an amount of Rs. 15,000 for 2 years is Rs. 96. What is the rate of interest per annum? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "8%",
                    "6%",
                    "7%",
                    "9%"
                ],
                "correct_answer": "8%",
                "explanation": "Formula: Diff = P * (R / 100)^2\n96 = 15,000 * (R^2 / 10,000)\n96 = 1.5 * R^2\nR^2 = 96 / 1.5 = 64\nR = 8%.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3102,
                "topic_id": 31,
                "question": "A sum of money amounts to Rs. 4,840 in 2 years and to Rs. 5,324 in 3 years at compound interest compounded annually. Find the rate of interest per annum. [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "10%",
                    "8%",
                    "9%",
                    "12%"
                ],
                "correct_answer": "10%",
                "explanation": "Interest accrued in the 3rd year = Amount after 3 yrs - Amount after 2 yrs\nInterest = 5324 - 4840 = Rs. 484.\nThis Rs. 484 is the 1-year interest on the 2nd year balance (Rs. 4840).\nRate R = (Interest * 100) / Principal = (484 * 100) / 4840 = 10%.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3103,
                "topic_id": 31,
                "question": "A sum of money placed at compound interest doubles itself in 4 years. In how many years will it amount to 8 times itself? [UPSC CDS 2023]",
                "options_json": [
                    "12 years",
                    "16 years",
                    "8 years",
                    "10 years"
                ],
                "correct_answer": "12 years",
                "explanation": "At compound interest, if a sum becomes 2 times in 4 years, then it becomes 2^k times in (k * 4) years.\nHere 8 = 2^3 -> k = 3.\nTime required = 3 * 4 = 12 years.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3101,
                "topic_id": 31,
                "question": "Find the compound interest on Rs. 10,000 at 10% per annum for 3 years, compounded annually.",
                "options_json": [
                    "Rs. 3310",
                    "Rs. 3000",
                    "Rs. 3200",
                    "Rs. 3400"
                ],
                "correct_answer": "Rs. 3310",
                "explanation": "A = 10,000 * (1 + 10/100)^3 = 10,000 * (1.1)^3 = 10,000 * 1.331 = Rs. 13,310.\nCI = 13,310 - 10,000 = Rs. 3310.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3102,
                "topic_id": 31,
                "question": "What is the difference between CI and SI on Rs. 5000 for 2 years at 6% per annum?",
                "options_json": [
                    "Rs. 18",
                    "Rs. 15",
                    "Rs. 20",
                    "Rs. 12"
                ],
                "correct_answer": "Rs. 18",
                "explanation": "Diff = P * (R/100)^2 = 5000 * (6/100)^2 = 5000 * (36 / 10,000) = 5000 * 0.0036 = Rs. 18.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3103,
                "topic_id": 31,
                "question": "Find the compound interest on Rs. 16,000 at 20% per annum for 9 months, compounded quarterly.",
                "options_json": [
                    "Rs. 2522",
                    "Rs. 2400",
                    "Rs. 2500",
                    "Rs. 2600"
                ],
                "correct_answer": "Rs. 2522",
                "explanation": "Quarterly rate = 20% / 4 = 5% per quarter.\nTime = 9 months = 3 quarters.\nA = 16,000 * (1 + 5/100)^3 = 16,000 * (21/20)^3 = 16,000 * (9261 / 8000) = 2 * 9261 = Rs. 18,522.\nCI = 18,522 - 16,000 = Rs. 2522.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3104,
                "topic_id": 31,
                "question": "At what rate percent per annum will a sum of Rs. 1000 amount to Rs. 1331 in 3 years, interest compounded annually?",
                "options_json": [
                    "10%",
                    "11%",
                    "9%",
                    "12%"
                ],
                "correct_answer": "10%",
                "explanation": "A / P = (1 + R/100)^3 -> 1331 / 1000 = (1 + R/100)^3.\n(11 / 10)^3 = (1 + R/100)^3 -> 1 + R/100 = 11/10 = 1.1 -> R/100 = 0.1 -> R = 10%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3105,
                "topic_id": 31,
                "question": "A sum of money amounts to Rs. 6690 after 3 years and to Rs. 10,035 after 6 years on compound interest. Find the sum.",
                "options_json": [
                    "Rs. 4460",
                    "Rs. 4500",
                    "Rs. 4200",
                    "Rs. 4600"
                ],
                "correct_answer": "Rs. 4460",
                "explanation": "Formula: P = A1^2 / A2\nP = (6690 * 6690) / 10035 = (6690 * 2) / 3 = 2230 * 2 = Rs. 4460.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3106,
                "topic_id": 31,
                "question": "If the compound interest on a certain sum for 2 years at 10% per annum is Rs. 525, the simple interest on the same sum for double the time at half the rate percent per annum is:",
                "options_json": [
                    "Rs. 500",
                    "Rs. 520",
                    "Rs. 480",
                    "Rs. 550"
                ],
                "correct_answer": "Rs. 500",
                "explanation": "Effective CI for 2 yrs at 10% = 10 + 10 + (10*10/100) = 21%.\n21% of P = 525 -> P = (525 / 21) * 100 = 25 * 100 = Rs. 2500.\nNew time = 2 * 2 = 4 years; New rate = 10% / 2 = 5%.\nNew SI = (2500 * 5 * 4) / 100 = 2500 * 0.20 = Rs. 500.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3107,
                "topic_id": 31,
                "question": "The difference between simple interest and compound interest on Rs. 1200 for one year at 10% per annum reckoned half-yearly is:",
                "options_json": [
                    "Rs. 3",
                    "Rs. 2.50",
                    "Rs. 4",
                    "Rs. 5"
                ],
                "correct_answer": "Rs. 3",
                "explanation": "Annual SI for 1 year at 10% = 1200 * 0.10 = Rs. 120.\nFor CI reckoned half-yearly: R = 5%, n = 2 periods.\nCI = 1200 * [(1 + 0.05)^2 - 1] = 1200 * (1.1025 - 1) = 1200 * 0.1025 = Rs. 123.\nDifference = 123 - 120 = Rs. 3.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3108,
                "topic_id": 31,
                "question": "A loan of Rs. 25,500 is to be paid back in two equal half-yearly installments at 8% per annum compounded half-yearly. Find the value of each installment.",
                "options_json": [
                    "Rs. 13,520",
                    "Rs. 13,000",
                    "Rs. 14,000",
                    "Rs. 13,200"
                ],
                "correct_answer": "Rs. 13,520",
                "explanation": "Half-yearly rate = 8% / 2 = 4% = 1/25. Multiplier = 26/25.\nPresent value = x / (26/25) + x / (26/25)^2 = x * (25/26) * [1 + 25/26] = x * (25/26) * (51/26) = x * (1275 / 676).\n25,500 = x * (1275 / 676) -> x = (25,500 * 676) / 1275 = 20 * 676 = Rs. 13,520.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 3109,
                "topic_id": 31,
                "question": "The difference between CI and SI on a certain sum for 3 years at 5% per annum is Rs. 122. Find the sum.",
                "options_json": [
                    "Rs. 16,000",
                    "Rs. 15,000",
                    "Rs. 18,000",
                    "Rs. 20,000"
                ],
                "correct_answer": "Rs. 16,000",
                "explanation": "Formula: Diff = P * (R/100)^2 * [(300 + R)/100]\n122 = P * (5/100)^2 * (305 / 100) = P * (1/400) * (305 / 100) = P * (305 / 40,000).\nP = (122 * 40,000) / 305 = (2 * 40,000) / 5 = 2 * 8000 = Rs. 16,000.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3110,
                "topic_id": 31,
                "question": "A sum of money invested at compound interest doubles in 5 years. In how many years will it become 16 times itself?",
                "options_json": [
                    "20 years",
                    "25 years",
                    "15 years",
                    "18 years"
                ],
                "correct_answer": "20 years",
                "explanation": "16 = 2^4 -> Time = 4 * 5 = 20 years.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 3101,
                "topic_id": 31,
                "question": "What is the compound interest on Rs. 5000 for 2 years at 4% per annum, interest compounded annually?",
                "options_json": [
                    "Rs. 408",
                    "Rs. 400",
                    "Rs. 416",
                    "Rs. 420"
                ],
                "correct_answer": "Rs. 408",
                "explanation": "A = 5000 * (1.04)^2 = 5000 * 1.0816 = Rs. 5408. CI = 5408 - 5000 = Rs. 408.",
                "points": 1
            },
            {
                "id": 3102,
                "topic_id": 31,
                "question": "Find the difference between CI and SI on Rs. 8000 for 2 years at 5% per annum.",
                "options_json": [
                    "Rs. 20",
                    "Rs. 15",
                    "Rs. 25",
                    "Rs. 10"
                ],
                "correct_answer": "Rs. 20",
                "explanation": "Diff = 8000 * (5/100)^2 = 8000 * (1/400) = Rs. 20.",
                "points": 1
            },
            {
                "id": 3103,
                "topic_id": 31,
                "question": "A sum of money amounts to Rs. 1200 in 2 years and Rs. 1440 in 3 years at compound interest. What is the rate of interest?",
                "options_json": [
                    "20%",
                    "25%",
                    "15%",
                    "18%"
                ],
                "correct_answer": "20%",
                "explanation": "Interest in 3rd year = 1440 - 1200 = 240. Rate = (240 / 1200) * 100 = 20%.",
                "points": 1
            },
            {
                "id": 3104,
                "topic_id": 31,
                "question": "If a sum of money doubles itself at compound interest in 6 years, it will become 8 times itself in:",
                "options_json": [
                    "18 years",
                    "24 years",
                    "12 years",
                    "16 years"
                ],
                "correct_answer": "18 years",
                "explanation": "8 = 2^3 -> Time = 3 * 6 = 18 years.",
                "points": 1
            },
            {
                "id": 3105,
                "topic_id": 31,
                "question": "The simple interest on a certain sum for 2 years at 10% is Rs. 400. The compound interest on the same sum for the same period and rate is:",
                "options_json": [
                    "Rs. 420",
                    "Rs. 410",
                    "Rs. 430",
                    "Rs. 440"
                ],
                "correct_answer": "Rs. 420",
                "explanation": "SI for 1 yr = 200. CI for 2 yrs = SI + 10% of Year 1 interest = 400 + (10% of 200) = 400 + 20 = Rs. 420.",
                "points": 1
            },
            {
                "id": 3106,
                "topic_id": 31,
                "question": "In what time will Rs. 64,000 produce Rs. 10,088 as compound interest at 5% per annum, interest being compounded annually?",
                "options_json": [
                    "3 years",
                    "2 years",
                    "4 years",
                    "2.5 years"
                ],
                "correct_answer": "3 years",
                "explanation": "A = 64000 + 10088 = 74088. 74088 / 64000 = 9261 / 8000 = (21/20)^3 = (1 + 5/100)^3. Time = 3 years.",
                "points": 1
            },
            {
                "id": 3107,
                "topic_id": 31,
                "question": "If the rate of interest is 4% per annum for the first year, 5% for the second year and 6% for the third year, what is the compound interest on Rs. 10,000 for 3 years?",
                "options_json": [
                    "Rs. 1575.20",
                    "Rs. 1500.00",
                    "Rs. 1600.50",
                    "Rs. 1550.00"
                ],
                "correct_answer": "Rs. 1575.20",
                "explanation": "A = 10000 * 1.04 * 1.05 * 1.06 = 10000 * 1.15752 = Rs. 11,575.20. CI = 11,575.20 - 10000 = Rs. 1575.20.",
                "points": 1
            },
            {
                "id": 3108,
                "topic_id": 31,
                "question": "What is the effective annual rate of interest corresponding to a nominal rate of 6% per annum payable half-yearly?",
                "options_json": [
                    "6.09%",
                    "6.00%",
                    "6.12%",
                    "6.15%"
                ],
                "correct_answer": "6.09%",
                "explanation": "Effective rate = 3 + 3 + (3*3 / 100) = 6 + 0.09 = 6.09%.",
                "points": 1
            },
            {
                "id": 3109,
                "topic_id": 31,
                "question": "A sum of money amounts to Rs. 2420 in 2 years and Rs. 2662 in 3 years at compound interest. The principal is:",
                "options_json": [
                    "Rs. 2000",
                    "Rs. 2100",
                    "Rs. 1900",
                    "Rs. 2200"
                ],
                "correct_answer": "Rs. 2000",
                "explanation": "Interest in 3rd year = 2662 - 2420 = 242. Rate = 242/2420 = 10%.\nP = 2420 / (1.1)^2 = 2420 / 1.21 = Rs. 2000.",
                "points": 1
            },
            {
                "id": 3110,
                "topic_id": 31,
                "question": "The value of a machine depreciates at 10% per annum. If its present value is Rs. 1,62,000, what will be its value after 2 years?",
                "options_json": [
                    "Rs. 1,31,220",
                    "Rs. 1,30,000",
                    "Rs. 1,32,400",
                    "Rs. 1,29,600"
                ],
                "correct_answer": "Rs. 1,31,220",
                "explanation": "Value = 162,000 * (1 - 0.10)^2 = 162,000 * 0.81 = Rs. 131,220.",
                "points": 1
            }
        ]
    },
    "32": {
        "title": "Mensuration: 2D Plane Areas, Perimeters & 3D Solid Surface Areas / Volumes",
        "source_id": 7,
        "content": {
            "definition": "Mensuration is the branch of applied geometry that computes perimeter, surface area, and volume of two-dimensional and three-dimensional geometric figures. In competitive examinations (SSC CGL Tier 1/2, CDS, CAPF, IBPS PO), questions test equilateral triangles, circles and ring pathways, trapeziums, rhombuses, cuboids, cylinders, cones, spheres, hemispheres, and mass/volume conservation during melting and recasting.",
            "overview": "Fundamental Formulations:\n- 2D Figures:\n  - Equilateral Triangle: $\\text{Area} = \\frac{\\sqrt{3}}{4} a^2$; $\\text{Height} = \\frac{\\sqrt{3}}{2} a$\n  - Heron's Formula (Scalene): $\\text{Area} = \\sqrt{s(s-a)(s-b)(s-c)}$ where $s = \\frac{a+b+c}{2}$\n  - Circle: $\\text{Area} = \\pi r^2$; $\\text{Circumference} = 2\\pi r$\n  - Rhombus: $\\text{Area} = \\frac{1}{2} d_1 d_2$; $\\text{Side} = \\frac{1}{2} \\sqrt{d_1^2 + d_2^2}$\n  - Trapezium: $\\text{Area} = \\frac{1}{2} (a + b) \\times h$\n- 3D Figures:\n  - Cylinder: $\\text{Volume} = \\pi r^2 h$; $\\text{CSA} = 2\\pi rh$; $\\text{TSA} = 2\\pi r(h + r)$\n  - Cone: $\\text{Volume} = \\frac{1}{3} \\pi r^2 h$; $\\text{CSA} = \\pi r l$ where $l = \\sqrt{r^2 + h^2}$\n  - Sphere: $\\text{Volume} = \\frac{4}{3} \\pi r^3$; $\\text{Surface Area} = 4\\pi r^2$\n  - Hemisphere: $\\text{Volume} = \\frac{2}{3} \\pi r^3$; $\\text{CSA} = 2\\pi r^2$; $\\text{TSA} = 3\\pi r^2$",
            "types": [
                {
                    "name": "1. 2D Polygons (Triangles & Quadrilaterals)",
                    "desc": "Planar calculations for scalene, isosceles, right-angled, and equilateral forms.",
                    "examples": [
                        "Equilateral Triangle of side 6 cm: Area = (sqrt(3)/4) * 36 = 9*sqrt(3) cm^2",
                        "Rhombus with diagonals 16 and 12 cm: Area = 1/2 * 16 * 12 = 96 cm^2; Side = sqrt(8^2 + 6^2) = 10 cm",
                        "Trapezium with parallel sides 12 and 18 cm, height 8 cm: Area = 1/2 * (12 + 18) * 8 = 120 cm^2"
                    ]
                },
                {
                    "name": "2. Circular Geometries & Annular Pathways",
                    "desc": "Circles, sectors, segments, and pathways constructed inside or outside lawns.",
                    "examples": [
                        "Area of Ring (Annulus) = pi * (R^2 - r^2) = pi * (R + r)(R - r)",
                        "Area of Sector = (theta / 360) * pi * r^2",
                        "Arc Length = (theta / 360) * 2 * pi * r"
                    ]
                },
                {
                    "name": "3. Prismatic Solids: Cubes, Cuboids & Cylinders",
                    "desc": "Uniform cross-sectional 3D objects.",
                    "examples": [
                        "Cuboid: Volume = l*b*h; Total Surface Area = 2(lb + bh + hl); Diagonal = sqrt(l^2 + b^2 + h^2)",
                        "Cube: Volume = a^3; TSA = 6a^2; Diagonal = a*sqrt(3)",
                        "Cylinder: Volume = pi * r^2 * h; Curved Surface = 2*pi*r*h; Total Surface = 2*pi*r*(r + h)"
                    ]
                },
                {
                    "name": "4. Conical & Spherical Geometries",
                    "desc": "Tapered and curved solid enclosures.",
                    "examples": [
                        "Cone: Slant height l = sqrt(r^2 + h^2); Volume = (1/3)*pi*r^2*h; CSA = pi*r*l",
                        "Sphere: Volume = (4/3)*pi*r^3; Surface Area = 4*pi*r^2",
                        "Hemisphere: Volume = (2/3)*pi*r^3; Curved Surface = 2*pi*r^2; Total Surface = 3*pi*r^2"
                    ]
                },
                {
                    "name": "5. Melting, Recasting & Volume Conservation",
                    "desc": "Reshaping solids without changing total mass/volume.",
                    "examples": [
                        "Number of small spheres formed by melting a large sphere: N = Volume_large / Volume_small = (R / r)^3",
                        "Melting a cylinder into a cone: pi * r_cyl^2 * h_cyl = (1/3) * pi * r_cone^2 * h_cone"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Volume Conservation Law in Melting and Recasting",
                    "explanation": "When a solid is melted and recast into another shape (or multiple smaller objects), the total volume remains invariant: $\\text{Volume}_{\\text{initial}} = n \\times \\text{Volume}_{\\text{final}}$.",
                    "words": [
                        "Volume Conservation",
                        "Melting and Recasting",
                        "Invariant Volume"
                    ],
                    "correct": "Melting a metallic sphere of radius R into n small spheres of radius r: (4/3)*pi*R^3 = n * (4/3)*pi*r^3 -> n = (R / r)^3.",
                    "incorrect": "Equating surface areas instead of volumes (Surface area is NOT conserved during melting)."
                },
                {
                    "rule_number": 2,
                    "title": "Rhombus Diagonal-Side Relation ($4a^2 = d_1^2 + d_2^2$)",
                    "explanation": "Diagonals of a rhombus bisect each other perpendicularly at right angles. Applying the Pythagorean theorem to one quarter-triangle yields: $a = \\sqrt{(d_1/2)^2 + (d_2/2)^2} \\implies 4a^2 = d_1^2 + d_2^2$.",
                    "words": [
                        "Rhombus",
                        "4a^2 = d1^2 + d2^2",
                        "Perpendicular Diagonals"
                    ],
                    "correct": "Diagonals 24 and 10: a = sqrt(12^2 + 5^2) = sqrt(169) = 13 cm. Perimeter = 4 * 13 = 52 cm.",
                    "incorrect": "Perimeter = 2(d1 + d2) (Diagonals are not sides)."
                },
                {
                    "rule_number": 3,
                    "title": "Hemisphere Total vs Curved Surface Area Distinction",
                    "explanation": "For a solid hemisphere of radius $r$:\n(1) Curved Surface Area (CSA) $= 2\\pi r^2$\n(2) Flat Circular Base Area $= \\pi r^2$\n(3) Total Surface Area (TSA) $= 2\\pi r^2 + \\pi r^2 = 3\\pi r^2$.",
                    "words": [
                        "Hemisphere TSA",
                        "3*pi*r^2",
                        "Flat Base Area"
                    ],
                    "correct": "TSA of solid hemisphere of radius 7 cm: 3 * (22/7) * 7^2 = 3 * 22 * 7 = 462 cm^2.",
                    "incorrect": "Using 2*pi*r^2 (308 cm^2) for total surface area, omitting the circular base."
                },
                {
                    "rule_number": 4,
                    "title": "Pathway Area Around Rectangular and Circular Fields",
                    "explanation": "(1) Pathway of width $w$ INSIDE a rectangle of $L \\times B$: $\\text{Area} = 2w(L + B - 2w)$.\n(2) Pathway of width $w$ OUTSIDE a rectangle of $L \\times B$: $\\text{Area} = 2w(L + B + 2w)$.\n(3) Ring between concentric circles: $\\text{Area} = \\pi(R^2 - r^2) = \\pi(R + r)(R - r)$.",
                    "words": [
                        "Pathway Formula",
                        "Annulus Ring",
                        "2w(L + B +- 2w)"
                    ],
                    "correct": "Path of width 2m outside 20m x 15m field: Area = 2(2) * [20 + 15 + 2(2)] = 4 * 39 = 156 m^2.",
                    "incorrect": "Calculating Area as perimeter * width = 2(20 + 15) * 2 = 140 m^2 (Neglects the 4 corner squares of area w^2)."
                },
                {
                    "rule_number": 5,
                    "title": "Scaling of Linear Dimensions on Area and Volume",
                    "explanation": "If every linear dimension of a 2D or 3D object is scaled by a factor $k$:\n(1) Perimeter scales by $k$\n(2) Surface Area scales by $k^2$\n(3) Volume scales by $k^3$.",
                    "words": [
                        "Dimensional Scaling",
                        "Area ~ k^2",
                        "Volume ~ k^3"
                    ],
                    "correct": "If the radius of a sphere is doubled (k = 2), its volume increases by 2^3 = 8 times (700% increase).",
                    "incorrect": "Assuming volume doubles when radius doubles (fails to account for 3D scaling)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using Curved Surface Area when question asks for Total Surface Area.",
                    "correction": "Cylinder TSA = 2*pi*r(r + h); Cone TSA = pi*r(l + r); Hemisphere TSA = 3*pi*r^2.",
                    "rationale": "Total Surface includes closed circular bases."
                },
                {
                    "mistake": "Confusing height (h) with slant height (l) in cone formulas.",
                    "correction": "Slant height l = sqrt(r^2 + h^2). Volume uses vertical height h; CSA uses slant height l.",
                    "rationale": "Volume depends on perpendicular depth; surface depends on hypotenuse boundary."
                },
                {
                    "mistake": "Assuming surface area is conserved during melting.",
                    "correction": "Only VOLUME is conserved. When one big sphere is melted into smaller spheres, total surface area INCREASES.",
                    "rationale": "More smaller bodies expose significantly more surface."
                },
                {
                    "mistake": "Forgetting to take square roots of diagonal halves in rhombus side calculation.",
                    "correction": "Side a = sqrt[(d1/2)^2 + (d2/2)^2].",
                    "rationale": "The diagonals bisect each other, forming legs of half-lengths."
                }
            ],
            "quick_revision_points": [
                "Equilateral triangle: Area = (sqrt(3)/4) * a^2; Height = (sqrt(3)/2) * a.",
                "Circle: Area = pi * r^2; Circumference = 2 * pi * r.",
                "Rhombus: Area = 1/2 * d1 * d2; 4a^2 = d1^2 + d2^2.",
                "Trapezium: Area = 1/2 * (Sum of parallel sides) * Height.",
                "Cylinder: Volume = pi * r^2 * h; CSA = 2 * pi * r * h; TSA = 2 * pi * r * (r + h).",
                "Cone: Volume = (1/3) * pi * r^2 * h; CSA = pi * r * l (where l = sqrt(r^2 + h^2)).",
                "Sphere: Volume = (4/3) * pi * r^3; Surface Area = 4 * pi * r^2.",
                "Hemisphere: Volume = (2/3) * pi * r^3; CSA = 2 * pi * r^2; TSA = 3 * pi * r^2."
            ]
        },
        "previous_year_questions": [
            {
                "id": 3201,
                "topic_id": 32,
                "question": "The radius of the base of a right circular cylinder is 7 cm and its height is 15 cm. Find its total surface area. (Take pi = 22/7) [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "968 cm^2",
                    "880 cm^2",
                    "1024 cm^2",
                    "920 cm^2"
                ],
                "correct_answer": "968 cm^2",
                "explanation": "Formula: TSA = 2 * pi * r * (h + r)\nTSA = 2 * (22/7) * 7 * (15 + 7) = 44 * 22 = 968 cm^2.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3202,
                "topic_id": 32,
                "question": "A solid metallic sphere of radius 6 cm is melted and recast into small spheres of radius 2 cm each. Find the number of small spheres formed. [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "27",
                    "18",
                    "36",
                    "24"
                ],
                "correct_answer": "27",
                "explanation": "Number of spheres n = Volume of large sphere / Volume of small sphere\nn = [(4/3) * pi * R^3] / [(4/3) * pi * r^3] = (R / r)^3\nn = (6 / 2)^3 = 3^3 = 27.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3203,
                "topic_id": 32,
                "question": "The perimeter of a rhombus is 40 cm and the length of one of its diagonals is 12 cm. What is the area of the rhombus? [UPSC CDS 2023]",
                "options_json": [
                    "96 cm^2",
                    "80 cm^2",
                    "120 cm^2",
                    "100 cm^2"
                ],
                "correct_answer": "96 cm^2",
                "explanation": "Side of rhombus a = 40 / 4 = 10 cm.\nOne diagonal d1 = 12 cm -> half diagonal = 6 cm.\nBy Pythagoras theorem: (d2 / 2) = sqrt(a^2 - (d1 / 2)^2) = sqrt(10^2 - 6^2) = sqrt(64) = 8 cm.\nOther diagonal d2 = 2 * 8 = 16 cm.\nArea = 1/2 * d1 * d2 = 1/2 * 12 * 16 = 96 cm^2.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3201,
                "topic_id": 32,
                "question": "The side of an equilateral triangle is 8 cm. Find its area.",
                "options_json": [
                    "16*sqrt(3) cm^2",
                    "32*sqrt(3) cm^2",
                    "24*sqrt(3) cm^2",
                    "64*sqrt(3) cm^2"
                ],
                "correct_answer": "16*sqrt(3) cm^2",
                "explanation": "Area = (sqrt(3)/4) * a^2 = (sqrt(3)/4) * 8^2 = (sqrt(3)/4) * 64 = 16*sqrt(3) cm^2.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3202,
                "topic_id": 32,
                "question": "Find the volume of a right circular cone whose radius is 6 cm and height is 7 cm. (Take pi = 22/7)",
                "options_json": [
                    "264 cm^3",
                    "288 cm^3",
                    "252 cm^3",
                    "275 cm^3"
                ],
                "correct_answer": "264 cm^3",
                "explanation": "Volume = (1/3) * pi * r^2 * h = (1/3) * (22/7) * 36 * 7 = (1/3) * 22 * 36 = 22 * 12 = 264 cm^3.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3203,
                "topic_id": 32,
                "question": "A room is 12 m long, 9 m broad and 8 m high. Find the length of the longest rod that can be placed in this room.",
                "options_json": [
                    "17 m",
                    "15 m",
                    "16 m",
                    "18 m"
                ],
                "correct_answer": "17 m",
                "explanation": "Diagonal of cuboid = sqrt(l^2 + b^2 + h^2) = sqrt(12^2 + 9^2 + 8^2) = sqrt(144 + 81 + 64) = sqrt(289) = 17 m.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3204,
                "topic_id": 32,
                "question": "The total surface area of a solid hemisphere of radius 7 cm is: (Take pi = 22/7)",
                "options_json": [
                    "462 cm^2",
                    "308 cm^2",
                    "616 cm^2",
                    "450 cm^2"
                ],
                "correct_answer": "462 cm^2",
                "explanation": "TSA of solid hemisphere = 3 * pi * r^2 = 3 * (22/7) * 49 = 3 * 22 * 7 = 462 cm^2.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3205,
                "topic_id": 32,
                "question": "If the radius of a sphere is increased by 50%, find the percentage increase in its surface area.",
                "options_json": [
                    "125%",
                    "100%",
                    "150%",
                    "75%"
                ],
                "correct_answer": "125%",
                "explanation": "Surface Area is proportional to r^2.\nNet percentage increase = 50 + 50 + (50 * 50 / 100) = 100 + 25 = 125%.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3206,
                "topic_id": 32,
                "question": "The ratio between the length and breadth of a rectangular field is 3 : 2. If the area of the field is 216 sq m, find its perimeter.",
                "options_json": [
                    "60 m",
                    "50 m",
                    "72 m",
                    "48 m"
                ],
                "correct_answer": "60 m",
                "explanation": "Let length = 3x, breadth = 2x.\nArea = 3x * 2x = 6x^2 = 216 -> x^2 = 36 -> x = 6.\nLength = 18 m, Breadth = 12 m.\nPerimeter = 2(18 + 12) = 2 * 30 = 60 m.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3207,
                "topic_id": 32,
                "question": "The area of a trapezium is 384 cm^2. If its parallel sides are in the ratio 3 : 5 and the perpendicular distance between them is 12 cm, find the smaller parallel side.",
                "options_json": [
                    "24 cm",
                    "40 cm",
                    "20 cm",
                    "28 cm"
                ],
                "correct_answer": "24 cm",
                "explanation": "Area = 1/2 * (3x + 5x) * 12 = 384.\n4x * 12 = 384 -> 48x = 384 -> x = 8.\nSmaller parallel side = 3x = 3 * 8 = 24 cm.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3208,
                "topic_id": 32,
                "question": "How many bullets can be made out of a lead cylinder 28 cm high and with base radius 6 cm, each bullet being a sphere of diameter 1.5 cm?",
                "options_json": [
                    "1792",
                    "1800",
                    "1750",
                    "1820"
                ],
                "correct_answer": "1792",
                "explanation": "Volume of cylinder = pi * 6^2 * 28 = pi * 36 * 28 = 1008 * pi cm^3.\nRadius of bullet = 1.5 / 2 = 0.75 cm = 3/4 cm.\nVolume of 1 bullet = (4/3) * pi * (3/4)^3 = (4/3) * pi * (27 / 64) = (9 / 16) * pi cm^3.\nNumber of bullets = (1008 * pi) / [(9/16) * pi] = (1008 * 16) / 9 = 112 * 16 = 1792.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 3209,
                "topic_id": 32,
                "question": "A circular wire of radius 42 cm is bent into the shape of a rectangle whose sides are in the ratio 6 : 5. Find the smaller side of the rectangle.",
                "options_json": [
                    "60 cm",
                    "72 cm",
                    "50 cm",
                    "55 cm"
                ],
                "correct_answer": "60 cm",
                "explanation": "Circumference of circle = 2 * (22/7) * 42 = 2 * 22 * 6 = 264 cm.\nPerimeter of rectangle = 2(6x + 5x) = 2(11x) = 22x = 264 -> x = 12.\nSmaller side = 5x = 5 * 12 = 60 cm.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3210,
                "topic_id": 32,
                "question": "A cone and a hemisphere have equal bases and equal volumes. Find the ratio of their heights.",
                "options_json": [
                    "2 : 1",
                    "1 : 2",
                    "3 : 1",
                    "4 : 1"
                ],
                "correct_answer": "2 : 1",
                "explanation": "Equal bases mean equal radius r.\nVolume of cone = (1/3) * pi * r^2 * h.\nVolume of hemisphere = (2/3) * pi * r^3.\nHeight of hemisphere = r.\n(1/3) * pi * r^2 * h = (2/3) * pi * r^3 -> h = 2r.\nRatio of height of cone to hemisphere = 2r : r = 2 : 1.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 3201,
                "topic_id": 32,
                "question": "Find the circumference of a circle whose area is 1386 cm^2. (Take pi = 22/7)",
                "options_json": [
                    "132 cm",
                    "144 cm",
                    "126 cm",
                    "138 cm"
                ],
                "correct_answer": "132 cm",
                "explanation": "pi * r^2 = 1386 -> (22/7) * r^2 = 1386 -> r^2 = (1386 * 7) / 22 = 63 * 7 = 441 -> r = 21 cm.\nCircumference = 2 * (22/7) * 21 = 2 * 22 * 3 = 132 cm.",
                "points": 1
            },
            {
                "id": 3202,
                "topic_id": 32,
                "question": "The diagonal of a cube is 6*sqrt(3) cm. Its total surface area is:",
                "options_json": [
                    "216 cm^2",
                    "180 cm^2",
                    "240 cm^2",
                    "196 cm^2"
                ],
                "correct_answer": "216 cm^2",
                "explanation": "Diagonal of cube = a*sqrt(3) = 6*sqrt(3) -> side a = 6 cm.\nTSA = 6 * a^2 = 6 * 36 = 216 cm^2.",
                "points": 1
            },
            {
                "id": 3203,
                "topic_id": 32,
                "question": "The radii of two cylinders are in the ratio 2 : 3 and their heights are in the ratio 5 : 3. The ratio of their volumes is:",
                "options_json": [
                    "20 : 27",
                    "10 : 9",
                    "4 : 9",
                    "25 : 27"
                ],
                "correct_answer": "20 : 27",
                "explanation": "Volume ratio = (r1^2 * h1) / (r2^2 * h2) = (2^2 * 5) / (3^2 * 3) = (4 * 5) / (9 * 3) = 20 / 27.",
                "points": 1
            },
            {
                "id": 3204,
                "topic_id": 32,
                "question": "Find the slant height of a cone whose base radius is 8 cm and vertical height is 15 cm.",
                "options_json": [
                    "17 cm",
                    "16 cm",
                    "18 cm",
                    "19 cm"
                ],
                "correct_answer": "17 cm",
                "explanation": "l = sqrt(r^2 + h^2) = sqrt(8^2 + 15^2) = sqrt(64 + 225) = sqrt(289) = 17 cm.",
                "points": 1
            },
            {
                "id": 3205,
                "topic_id": 32,
                "question": "The area of a circle is 154 cm^2. Find the area of the square inscribed in this circle.",
                "options_json": [
                    "98 cm^2",
                    "100 cm^2",
                    "96 cm^2",
                    "108 cm^2"
                ],
                "correct_answer": "98 cm^2",
                "explanation": "(22/7) * r^2 = 154 -> r^2 = 49 -> r = 7 cm.\nDiagonal of inscribed square = Diameter of circle = 2r = 14 cm.\nArea of square = d^2 / 2 = 14^2 / 2 = 196 / 2 = 98 cm^2.",
                "points": 1
            },
            {
                "id": 3206,
                "topic_id": 32,
                "question": "The curved surface area of a cylinder is 440 cm^2 and its base circumference is 44 cm. What is its height?",
                "options_json": [
                    "10 cm",
                    "12 cm",
                    "8 cm",
                    "15 cm"
                ],
                "correct_answer": "10 cm",
                "explanation": "CSA = (2 * pi * r) * h = 44 * h = 440 -> h = 10 cm.",
                "points": 1
            },
            {
                "id": 3207,
                "topic_id": 32,
                "question": "If the side of a square is increased by 20%, its area increases by:",
                "options_json": [
                    "44%",
                    "40%",
                    "42%",
                    "48%"
                ],
                "correct_answer": "44%",
                "explanation": "Net increase = 20 + 20 + (20 * 20 / 100) = 40 + 4 = 44%.",
                "points": 1
            },
            {
                "id": 3208,
                "topic_id": 32,
                "question": "The volume of a sphere is (4/3) * pi * 27 cm^3. Find its surface area.",
                "options_json": [
                    "36*pi cm^2",
                    "27*pi cm^2",
                    "54*pi cm^2",
                    "18*pi cm^2"
                ],
                "correct_answer": "36*pi cm^2",
                "explanation": "(4/3)*pi*r^3 = (4/3)*pi*27 -> r^3 = 27 -> r = 3 cm.\nSurface area = 4 * pi * r^2 = 4 * pi * 9 = 36*pi cm^2.",
                "points": 1
            },
            {
                "id": 3209,
                "topic_id": 32,
                "question": "The lengths of the diagonals of a rhombus are 8 cm and 6 cm. Find the length of its side.",
                "options_json": [
                    "5 cm",
                    "6 cm",
                    "4 cm",
                    "7 cm"
                ],
                "correct_answer": "5 cm",
                "explanation": "Side = sqrt[(8/2)^2 + (6/2)^2] = sqrt(4^2 + 3^2) = sqrt(25) = 5 cm.",
                "points": 1
            },
            {
                "id": 3210,
                "topic_id": 32,
                "question": "A wire in the form of a square encloses an area of 121 cm^2. If the same wire is bent into a circle, find the area of the circle.",
                "options_json": [
                    "154 cm^2",
                    "144 cm^2",
                    "160 cm^2",
                    "136 cm^2"
                ],
                "correct_answer": "154 cm^2",
                "explanation": "Side of square a = sqrt(121) = 11 cm.\nLength of wire = Perimeter of square = 4 * 11 = 44 cm.\nCircumference of circle = 2 * (22/7) * r = 44 -> r = 7 cm.\nArea of circle = (22/7) * 49 = 154 cm^2.",
                "points": 1
            }
        ]
    }
}
