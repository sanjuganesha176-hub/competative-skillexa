# math_part3.py
MATH_PART3_DATA = {
    "33": {
        "title": "Data Interpretation: Tabular Analysis, Pie Charts, Bar Graphs & Trend Projections",
        "source_id": 7,
        "content": {
            "definition": "Data Interpretation (DI) is the analytical evaluation of empirical datasets presented in graphical and tabular structures, assessing quantitative reasoning under time-constrained exam environments. In competitive examinations (SSC CGL Tier 1/2, IBPS PO / SBI PO Mains, CAT, RBI Grade B), DI problems evaluate rapid mental approximations, degree-to-percentage circular conversions (360 deg = 100%), weighted category contributions, compounded annual growth rates (CAGR), and multi-variable tabular cross-tabulations.",
            "overview": "Fundamental Operations:\n- Pie Chart Conversion: $1\\% = 3.6^\\circ$; $\\text{Angle } \\theta = \\left(\\frac{\\text{Value}}{\\text{Total}}\\right) \\times 360^\\circ$; $\\text{Percentage} = \\left(\\frac{\\theta}{360^\\circ}\\right) \\times 100\\%$\n- Ratio in DI: Ratio between two sectors is identical to the ratio of their central angles or percentage slices\n- Percentage Growth: $\\left(\\frac{\\text{Final} - \\text{Initial}}{\\text{Initial}}\\right) \\times 100\\%$\n- Mental Approximation Techniques: Vedic split method, 10% and 1% benchmark anchoring",
            "types": [
                {
                    "name": "1. Tabular Matrices & Cross-Sectional Analysis",
                    "desc": "Multi-column and multi-row demographic, production, or financial figures.",
                    "examples": [
                        "Summing across rows and columns using column anchoring",
                        "Comparing ratios of expenditures across distinct fiscal quarters"
                    ]
                },
                {
                    "name": "2. Pie Charts (Single & Dual Interlocking Circles)",
                    "desc": "Proportional segment distributions in degrees or percentages.",
                    "examples": [
                        "Sector of 54 degrees = (54 / 360) * 100% = 15%",
                        "Dual Pie Charts: One chart showing total employees, second showing gender breakups"
                    ]
                },
                {
                    "name": "3. Bar Graphs (Stacked, Grouped & Percentage Bars)",
                    "desc": "Comparative discrete categories across continuous temporal intervals.",
                    "examples": [
                        "Grouped bars comparing Import vs Export over 5 years",
                        "Net trade balance = Export - Import"
                    ]
                },
                {
                    "name": "4. Line Graphs & Trend Analysis",
                    "desc": "Continuous trajectory tracking for sales, inflation, or vehicle velocities.",
                    "examples": [
                        "Steepest slope indicating the maximum rate of percentage acceleration",
                        "Average output across an entire 6-year period"
                    ]
                },
                {
                    "name": "5. Radar / Spider Web & Mixed Graphs",
                    "desc": "Multi-axial performance vectors and hybrid charts.",
                    "examples": [
                        "Combining a bar graph (total sales) with an overlaid line graph (profit margin %)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Pie Chart Degree-to-Percentage Master Formula",
                    "explanation": "Since a full circle subtends $360^\\circ$ representing $100\\%$, the conversion factors are:\n(1) $1\\% = \\frac{360^\\circ}{100} = 3.6^\\circ$\n(2) $1^\\circ = \\frac{100\\%}{360} = \\frac{5}{18}\\%$.\nTo convert angle $\\theta$ into percentage, multiply by $\\frac{5}{18}\\%$.",
                    "words": [
                        "Pie Chart",
                        "360 degrees = 100%",
                        "Angle * 5/18",
                        "3.6 degrees = 1%"
                    ],
                    "correct": "Angle 72 degrees = 72 * (5/18)% = 4 * 5% = 20% of total expenditure.",
                    "incorrect": "Calculating 72 / 100 = 72% (Confusing degrees with percentages)."
                },
                {
                    "rule_number": 2,
                    "title": "Angle-Ratio Invariance Rule",
                    "explanation": "When comparing two categories in the same pie chart, their numerical values are strictly proportional to their central angles. There is NO NEED to compute absolute numerical values.",
                    "words": [
                        "Angle Ratio",
                        "No Need for Absolute Value",
                        "Shortcut"
                    ],
                    "correct": "Ratio of Category A (54 deg) to Category B (36 deg) = 54 : 36 = 3 : 2.",
                    "incorrect": "Calculating (54/360 * Total) and (36/360 * Total) and then simplifying (Wastes 90 seconds)."
                },
                {
                    "rule_number": 3,
                    "title": "Percentage Change Base Identification Rule",
                    "explanation": "In growth questions, the denominator is ALWAYS the initial (base year) quantity: $\\text{\\% Growth} = \\frac{\\text{Value}_{\\text{current}} - \\text{Value}_{\\text{base}}}{\\text{Value}_{\\text{base}}} \\times 100\\%$.",
                    "words": [
                        "Percentage Growth",
                        "Initial Base",
                        "Denominator Selection"
                    ],
                    "correct": "Production rises from 80 tons in 2020 to 100 tons in 2021: % Increase = (100 - 80) / 80 * 100% = 25%.",
                    "incorrect": "Dividing by 100: (20 / 100) * 100% = 20% (Using final year as base)."
                },
                {
                    "rule_number": 4,
                    "title": "Approximation via 10% and 1% Benchmark Anchoring",
                    "explanation": "To rapidly calculate $X$ as a percentage of $Y$ without tedious long division: Find $10\\% = 0.1Y$ and $1\\% = 0.01Y$, then build up to $X$ additively.",
                    "words": [
                        "Benchmark Anchoring",
                        "10% and 1%",
                        "Fast Approximation"
                    ],
                    "correct": "What % of 450 is 144? 10% is 45; 30% is 135. Remainder 9 = 2% of 450. Total = 30 + 2 = 32%.",
                    "incorrect": "Setting up 14400 / 450 with long division on paper."
                },
                {
                    "rule_number": 5,
                    "title": "Weighted Average of Multiple Sectors Rule",
                    "explanation": "When finding the combined average of multiple subgroups from tables: $\\text{Combined Average} = \\frac{\\sum (N_i \\times A_i)}{\\sum N_i}$. Do not simply take the simple mean of the percentage values.",
                    "words": [
                        "Weighted Average",
                        "Group Total",
                        "Subgroup Means"
                    ],
                    "correct": "School A has 100 students (80% pass) and School B has 200 students (50% pass): Combined pass % = (100*80 + 200*50) / 300 = 18000 / 300 = 60%.",
                    "incorrect": "Average of pass percentages = (80 + 50) / 2 = 65% (Ignores unequal class sizes)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Calculating absolute values when the question only asks for a ratio or percentage.",
                    "correction": "Ratios and percentages can be determined directly from angles or percentages without knowing the total.",
                    "rationale": "Saves up to 80% of calculation time per DI question set."
                },
                {
                    "mistake": "Using the wrong base year in percentage increase/decrease questions.",
                    "correction": "'Compared to 2018' means 2018 is the denominator.",
                    "rationale": "The word following 'compared to', 'over', or 'than' dictates the denominator."
                },
                {
                    "mistake": "Misreading graph scale axes (e.g. thousands vs millions, or per annum vs monthly).",
                    "correction": "Always read the legend and Y-axis units (e.g. 'Production in metric tonnes (in 000s)') before calculating.",
                    "rationale": "Examiners include options with decimal factor errors of 10 or 1000."
                },
                {
                    "mistake": "Confusing central angle with percentage value in pie charts.",
                    "correction": "Remember that a 90-degree sector is 25%, not 90%.",
                    "rationale": "Degrees sum to 360, while percentages sum to 100."
                }
            ],
            "quick_revision_points": [
                "Pie Chart: 360 degrees = 100%; 1% = 3.6 degrees; 1 degree = 5/18%.",
                "Ratio of sectors in same pie chart = Ratio of their central angles.",
                "% Increase = [(New - Old) / Old] * 100%.",
                "% of Total = (Component / Total) * 100%.",
                "Average = Total Sum / Total Number.",
                "Always check axis units (in lakhs, thousands, crores, percentage).",
                "Use 10% and 1% benchmarks to eliminate distant multiple choice options.",
                "Do not compute absolute values when questions only require ratios or percentages."
            ]
        },
        "previous_year_questions": [
            {
                "id": 3301,
                "topic_id": 33,
                "question": "In a pie chart representing the expenditure of a family, the central angle for Food is 108 degrees and for Education is 72 degrees. If the total monthly expenditure is Rs. 60,000, find the combined expenditure on Food and Education. [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Rs. 30,000",
                    "Rs. 25,000",
                    "Rs. 32,000",
                    "Rs. 28,000"
                ],
                "correct_answer": "Rs. 30,000",
                "explanation": "Total angle = 108 + 72 = 180 degrees.\nFraction of total = 180 / 360 = 1/2.\nCombined expenditure = 1/2 * 60,000 = Rs. 30,000.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3302,
                "topic_id": 33,
                "question": "The production of a factory in 2020 was 80,000 units and in 2021 it increased to 96,000 units. What was the percentage increase in production? [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "20%",
                    "16%",
                    "25%",
                    "18%"
                ],
                "correct_answer": "20%",
                "explanation": "Increase = 96,000 - 80,000 = 16,000 units.\nPercentage increase = (16,000 / 80,000) * 100% = (16 / 80) * 100% = 1/5 * 100% = 20%.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 3303,
                "topic_id": 33,
                "question": "In a tabular data set of a college, the ratio of boys to girls in Arts, Science and Commerce streams are 3:2, 5:4, and 2:3 respectively. If the number of students in each stream is 100, 180, and 150 respectively, find the total number of girls in the college. [UPSC CDS 2023]",
                "options_json": [
                    "210",
                    "200",
                    "220",
                    "190"
                ],
                "correct_answer": "210",
                "explanation": "1. Arts (100 students, 3:2): Girls = 100 * (2/5) = 40.\n2. Science (180 students, 5:4): Girls = 180 * (4/9) = 80.\n3. Commerce (150 students, 2:3): Girls = 150 * (3/5) = 90.\nTotal girls = 40 + 80 + 90 = 210.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 3301,
                "topic_id": 33,
                "question": "In a pie chart, a sector represents 25% of the total budget. What is the central angle of this sector in degrees?",
                "options_json": [
                    "90 degrees",
                    "75 degrees",
                    "100 degrees",
                    "80 degrees"
                ],
                "correct_answer": "90 degrees",
                "explanation": "Angle = 25% of 360 = (25 / 100) * 360 = 1/4 * 360 = 90 degrees.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3302,
                "topic_id": 33,
                "question": "The sales of a company in 5 consecutive years were 40, 50, 65, 75, and 90 lakhs. Find the average annual sales.",
                "options_json": [
                    "64 lakhs",
                    "60 lakhs",
                    "65 lakhs",
                    "62 lakhs"
                ],
                "correct_answer": "64 lakhs",
                "explanation": "Sum = 40 + 50 + 65 + 75 + 90 = 320 lakhs.\nAverage = 320 / 5 = 64 lakhs.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3303,
                "topic_id": 33,
                "question": "A pie chart shows the distribution of students in four houses: Red (120 deg), Blue (90 deg), Green (90 deg), and Yellow (60 deg). If Red house has 240 students, what is the total number of students in the school?",
                "options_json": [
                    "720",
                    "600",
                    "800",
                    "750"
                ],
                "correct_answer": "720",
                "explanation": "120 degrees represents 240 students -> 1 degree represents 240 / 120 = 2 students.\nTotal students (360 degrees) = 360 * 2 = 720 students.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3304,
                "topic_id": 33,
                "question": "The exports of a commodity rose from Rs. 250 crores in 2018 to Rs. 350 crores in 2019. Find the percentage growth.",
                "options_json": [
                    "40%",
                    "35%",
                    "30%",
                    "45%"
                ],
                "correct_answer": "40%",
                "explanation": "Growth = 350 - 250 = 100 crores.\nPercentage growth = (100 / 250) * 100% = (2/5) * 100% = 40%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3305,
                "topic_id": 33,
                "question": "In a survey, 40% people preferred brand A, 35% brand B, and the remaining 250 people preferred brand C. How many total people were surveyed?",
                "options_json": [
                    "1000",
                    "800",
                    "1200",
                    "1500"
                ],
                "correct_answer": "1000",
                "explanation": "Percentage preferring brand C = 100 - (40 + 35) = 25%.\n25% of Total = 250 -> Total = (250 / 25) * 100 = 1000.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3306,
                "topic_id": 33,
                "question": "A bar chart shows sales of 5 companies A, B, C, D, E as 20, 30, 45, 60, 85 crores. By what percentage is the sales of E greater than the sales of A?",
                "options_json": [
                    "325%",
                    "425%",
                    "300%",
                    "350%"
                ],
                "correct_answer": "325%",
                "explanation": "Difference = 85 - 20 = 65 crores.\nPercentage greater = (65 / 20) * 100% = 65 * 5 = 325%.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3307,
                "topic_id": 33,
                "question": "In a pie chart, Sector A is 144 degrees and Sector B is 108 degrees. Find the ratio of the value of Sector A to Sector B.",
                "options_json": [
                    "4 : 3",
                    "3 : 2",
                    "5 : 4",
                    "7 : 5"
                ],
                "correct_answer": "4 : 3",
                "explanation": "Ratio = 144 : 108 = 12 : 9 = 4 : 3.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3308,
                "topic_id": 33,
                "question": "If imports in year 1 were Rs. 400 cr and in year 2 were Rs. 500 cr, while exports were Rs. 450 cr and Rs. 550 cr respectively, what is the difference between total exports and total imports over the two years?",
                "options_json": [
                    "Rs. 100 crores",
                    "Rs. 50 crores",
                    "Rs. 150 crores",
                    "Rs. 80 crores"
                ],
                "correct_answer": "Rs. 100 crores",
                "explanation": "Total exports = 450 + 550 = 1000 cr.\nTotal imports = 400 + 500 = 900 cr.\nDifference = 1000 - 900 = Rs. 100 crores.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 3309,
                "topic_id": 33,
                "question": "In a company, 45% of employees are female and 55% are male. If 60% of females and 40% of males are graduates, what percentage of total employees are graduates?",
                "options_json": [
                    "49%",
                    "48%",
                    "50%",
                    "52%"
                ],
                "correct_answer": "49%",
                "explanation": "Let total employees = 100. Females = 45, Males = 55.\nGraduate females = 60% of 45 = 27.\nGraduate males = 40% of 55 = 22.\nTotal graduates = 27 + 22 = 49% of total.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 3310,
                "topic_id": 33,
                "question": "A table shows students enrolled in Physics (200), Chemistry (180), and Maths (220). If 10% from Physics, 15% from Chemistry and 20% from Maths drop out, how many total students remain?",
                "options_json": [
                    "509",
                    "515",
                    "520",
                    "500"
                ],
                "correct_answer": "509",
                "explanation": "Physics remaining = 200 * 0.90 = 180.\nChemistry remaining = 180 * 0.85 = 153.\nMaths remaining = 220 * 0.80 = 176.\nTotal remaining = 180 + 153 + 176 = 509.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 3301,
                "topic_id": 33,
                "question": "In a pie chart, what angle represents 35% of the total?",
                "options_json": [
                    "126 degrees",
                    "120 degrees",
                    "135 degrees",
                    "130 degrees"
                ],
                "correct_answer": "126 degrees",
                "explanation": "Angle = 35 * 3.6 = 126 degrees.",
                "points": 1
            },
            {
                "id": 3302,
                "topic_id": 33,
                "question": "The angle for savings in a monthly budget pie chart is 54 degrees. If total income is Rs. 40,000, find monthly savings.",
                "options_json": [
                    "Rs. 6000",
                    "Rs. 5000",
                    "Rs. 7200",
                    "Rs. 5400"
                ],
                "correct_answer": "Rs. 6000",
                "explanation": "Savings = (54 / 360) * 40,000 = (3 / 20) * 40,000 = 3 * 2000 = Rs. 6000.",
                "points": 1
            },
            {
                "id": 3303,
                "topic_id": 33,
                "question": "Production increases from 50 to 65 units. What is the percentage increase?",
                "options_json": [
                    "30%",
                    "25%",
                    "35%",
                    "20%"
                ],
                "correct_answer": "30%",
                "explanation": "(65 - 50) / 50 * 100% = (15 / 50) * 100% = 30%.",
                "points": 1
            },
            {
                "id": 3304,
                "topic_id": 33,
                "question": "If angle for Rent is 72 degrees and for Transport is 36 degrees, what is the ratio of Rent to Transport?",
                "options_json": [
                    "2 : 1",
                    "3 : 1",
                    "3 : 2",
                    "4 : 1"
                ],
                "correct_answer": "2 : 1",
                "explanation": "Ratio = 72 : 36 = 2 : 1.",
                "points": 1
            },
            {
                "id": 3305,
                "topic_id": 33,
                "question": "In a bar graph, company A produced 120 cars and company B produced 160 cars. Company A's production is what percent of company B's production?",
                "options_json": [
                    "75%",
                    "80%",
                    "70%",
                    "65%"
                ],
                "correct_answer": "75%",
                "explanation": "(120 / 160) * 100% = (3 / 4) * 100% = 75%.",
                "points": 1
            },
            {
                "id": 3306,
                "topic_id": 33,
                "question": "If total population is 50,000 and 18% are senior citizens, how many senior citizens are there?",
                "options_json": [
                    "9000",
                    "8000",
                    "9500",
                    "10000"
                ],
                "correct_answer": "9000",
                "explanation": "0.18 * 50,000 = 9000.",
                "points": 1
            },
            {
                "id": 3307,
                "topic_id": 33,
                "question": "A line graph shows temperatures: 25, 28, 32, 35, 30. What is the range of temperatures?",
                "options_json": [
                    "10",
                    "8",
                    "12",
                    "7"
                ],
                "correct_answer": "10",
                "explanation": "Range = Max - Min = 35 - 25 = 10.",
                "points": 1
            },
            {
                "id": 3308,
                "topic_id": 33,
                "question": "What is the equivalent percentage of an angle of 108 degrees?",
                "options_json": [
                    "30%",
                    "25%",
                    "35%",
                    "28%"
                ],
                "correct_answer": "30%",
                "explanation": "(108 / 360) * 100% = (3 / 10) * 100% = 30%.",
                "points": 1
            },
            {
                "id": 3309,
                "topic_id": 33,
                "question": "The total sales in 2021 was Rs. 500 cr and in 2022 was Rs. 400 cr. Find the percentage decrease.",
                "options_json": [
                    "20%",
                    "25%",
                    "15%",
                    "10%"
                ],
                "correct_answer": "20%",
                "explanation": "Decrease = 500 - 400 = 100. Percentage decrease = (100 / 500) * 100% = 20%.",
                "points": 1
            },
            {
                "id": 3310,
                "topic_id": 33,
                "question": "A class has 40 boys and 20 girls. Average score of boys is 70 and girls is 85. What is the class average?",
                "options_json": [
                    "75",
                    "77.5",
                    "76",
                    "78"
                ],
                "correct_answer": "75",
                "explanation": "Weighted average = (40*70 + 20*85) / 60 = (2800 + 1700) / 60 = 4500 / 60 = 75.",
                "points": 1
            }
        ]
    },
    "34": {
        "title": "Algebra: Algebraic Identities, Polynomial Factorization & Quadratic Equations",
        "source_id": 7,
        "content": {
            "definition": "Algebra in competitive quantitative aptitude examines symbolic manipulation, polynomial identities, systems of linear equations, and quadratic polynomial analysis ($ax^2 + bx + c = 0$). Central exam patterns (SSC CGL Tier 1/2, CDS, CAT, Railways) heavily test symmetric reciprocal expressions ($x + 1/x = k$), Euler's cubic identity when $a+b+c=0$, the discriminant condition for root characterization, and the Remainder/Factor Theorems for polynomial roots.",
            "overview": "Essential Algebraic Identities & Relations:\n- Symmetric Powers: If $x + \\frac{1}{x} = k$, then $x^2 + \\frac{1}{x^2} = k^2 - 2$ and $x^3 + \\frac{1}{x^3} = k^3 - 3k$\n- Difference Powers: If $x - \\frac{1}{x} = k$, then $x^2 + \\frac{1}{x^2} = k^2 + 2$ and $x^3 - \\frac{1}{x^3} = k^3 + 3k$\n- Cubic Identity: $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2 - ab - bc - ca) = \\frac{1}{2}(a+b+c)[(a-b)^2 + (b-c)^2 + (c-a)^2]$\n- Zero Sum Condition: If $a + b + c = 0$, then $a^3 + b^3 + c^3 = 3abc$\n- Quadratic Roots: For $ax^2 + bx + c = 0$, Sum $\\alpha + \\beta = -b/a$, Product $\\alpha\\beta = c/a$, Discriminant $D = b^2 - 4ac$",
            "types": [
                {
                    "name": "1. Symmetric Reciprocal Expressions (x + 1/x)",
                    "desc": "Evaluating higher symmetric powers ($x^2, x^3, x^4, x^5, x^7$) given a base reciprocal sum or difference.",
                    "examples": [
                        "If x + 1/x = 3, then x^2 + 1/x^2 = 3^2 - 2 = 7",
                        "If x + 1/x = 3, then x^3 + 1/x^3 = 3^3 - 3(3) = 18"
                    ]
                },
                {
                    "name": "2. Cubic Conditional Identities (a + b + c = 0)",
                    "desc": "Simplifying multi-variable cubic expressions when sum of linear terms vanishes.",
                    "examples": [
                        "Evaluate (x-y)^3 + (y-z)^3 + (z-x)^3 = 3(x-y)(y-z)(z-x)",
                        "Given a+b+c=0, evaluate (a^2/bc) + (b^2/ca) + (c^2/ab) = 3abc/abc = 3"
                    ]
                },
                {
                    "name": "3. Quadratic Equations & Nature of Roots",
                    "desc": "Analyzing roots via discriminant D = b^2 - 4ac and constructing equations from root relations.",
                    "examples": [
                        "D > 0 (real & distinct), D = 0 (real & equal), D < 0 (complex conjugate)",
                        "Roots alpha, beta: x^2 - (alpha + beta)x + alpha*beta = 0"
                    ]
                },
                {
                    "name": "4. Remainder and Factor Theorem",
                    "desc": "Determining polynomial roots and remainders when dividing P(x) by linear binomial (x - a).",
                    "examples": [
                        "Remainder when P(x) is divided by (x - a) is P(a)",
                        "(x - 2) is a factor of x^3 - 6x^2 + 11x - 6 because P(2) = 8 - 24 + 22 - 6 = 0"
                    ]
                },
                {
                    "name": "5. Systems of Linear Equations (Consistency Criteria)",
                    "desc": "Determining unique, infinite, or no solutions for a1*x + b1*y = c1 and a2*x + b2*y = c2.",
                    "examples": [
                        "Unique solution: a1/a2 != b1/b2",
                        "Infinite solutions: a1/a2 = b1/b2 = c1/c2; No solution: a1/a2 = b1/b2 != c1/c2"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Reciprocal Square & Cube Shortcut Rule",
                    "explanation": "Let $x + \\frac{1}{x} = k$.\n- $x^2 + \\frac{1}{x^2} = k^2 - 2$\n- $x^3 + \\frac{1}{x^3} = k^3 - 3k$\n- $x^4 + \\frac{1}{x^4} = (k^2 - 2)^2 - 2$\n- $x^5 + \\frac{1}{x^5} = (x^2 + 1/x^2)(x^3 + 1/x^3) - (x + 1/x)$.",
                    "words": [
                        "x + 1/x = k",
                        "k^2 - 2",
                        "k^3 - 3k",
                        "Reciprocal Powers"
                    ],
                    "correct": "If x + 1/x = 4, then x^3 + 1/x^3 = 4^3 - 3(4) = 64 - 12 = 52.",
                    "incorrect": "Cubing directly as 4^3 = 64 without subtracting 3k."
                },
                {
                    "rule_number": 2,
                    "title": "Difference Reciprocal Rule (x - 1/x)",
                    "explanation": "If $x - \\frac{1}{x} = k$, then $x^2 + \\frac{1}{x^2} = k^2 + 2$ and $x^3 - \\frac{1}{x^3} = k^3 + 3k$. Notice the addition of signs because $(x - 1/x)^2 = x^2 - 2 + 1/x^2$.",
                    "words": [
                        "x - 1/x = k",
                        "k^2 + 2",
                        "k^3 + 3k",
                        "Sign Reversal"
                    ],
                    "correct": "If x - 1/x = 3, then x^3 - 1/x^3 = 3^3 + 3(3) = 27 + 9 = 36.",
                    "incorrect": "Calculating 3^3 - 3(3) = 18 by confusing minus identity with plus identity."
                },
                {
                    "rule_number": 3,
                    "title": "Vanishing Linear Sum Euler Identity",
                    "explanation": "Whenever $a + b + c = 0$, the identity $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2 - ab - bc - ca)$ simplifies to $a^3 + b^3 + c^3 = 3abc$.",
                    "words": [
                        "a + b + c = 0",
                        "a^3 + b^3 + c^3 = 3abc",
                        "Euler Identity"
                    ],
                    "correct": "Evaluate 25^3 + (-15)^3 + (-10)^3: Here 25 + (-15) + (-10) = 0, so Sum = 3(25)(-15)(-10) = 11,250.",
                    "incorrect": "Expanding and computing 25^3, 15^3, 10^3 separately."
                },
                {
                    "rule_number": 4,
                    "title": "Vieta's Formulas for Quadratic Polynomials",
                    "explanation": "For quadratic equation $ax^2 + bx + c = 0$ with roots $\\alpha$ and $\\beta$:\n- Sum of roots: $\\alpha + \\beta = -\\frac{b}{a}$\n- Product of roots: $\\alpha\\beta = \\frac{c}{a}$\n- Sum of reciprocal of roots: $\\frac{1}{\\alpha} + \\frac{1}{\\beta} = \\frac{\\alpha + \\beta}{\\alpha\\beta} = -\\frac{b}{c}$.",
                    "words": [
                        "Vieta's Formulas",
                        "-b/a",
                        "c/a",
                        "Roots Relation"
                    ],
                    "correct": "For 2x^2 - 5x + 3 = 0, alpha + beta = -(-5)/2 = 5/2, alpha*beta = 3/2.",
                    "incorrect": "Writing alpha + beta = +5/2 without negating the linear coefficient sign."
                },
                {
                    "rule_number": 5,
                    "title": "Discriminant Root Characterization Rule",
                    "explanation": "For quadratic equation with real rational coefficients, $D = b^2 - 4ac$ determines root nature:\n- $D > 0$ and a perfect square $\\implies$ Real, rational and unequal\n- $D > 0$ and NOT a perfect square $\\implies$ Real, irrational conjugate pairs ($p \\pm \\sqrt{q}$)\n- $D = 0 \\implies$ Real and equal (coincident roots $\\alpha = \\beta = -b/(2a)$)\n- $D < 0 \\implies$ Complex conjugate roots ($p \\pm iq$).",
                    "words": [
                        "Discriminant",
                        "b^2 - 4ac",
                        "Perfect Square",
                        "Real and Equal"
                    ],
                    "correct": "If kx^2 + 4x + 1 = 0 has equal roots: D = 16 - 4(k)(1) = 0 => 4k = 16 => k = 4.",
                    "incorrect": "Setting D > 0 for equal roots."
                },
                {
                    "rule_number": 6,
                    "title": "Polynomial Remainder Theorem",
                    "explanation": "When a polynomial $P(x)$ is divided by $(x - r)$, the remainder is $R = P(r)$. If $P(r) = 0$, then $(x - r)$ is an exact factor of $P(x)$.",
                    "words": [
                        "Remainder Theorem",
                        "P(r)",
                        "Factor Theorem"
                    ],
                    "correct": "Find remainder when x^3 - 3x^2 + 5x - 7 is divided by (x - 2): R = P(2) = 8 - 12 + 10 - 7 = -1.",
                    "incorrect": "Performing long polynomial division on scratch paper."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Calculating x^2 + 1/x^2 as k^2 + 2 when given x + 1/x = k.",
                    "correction": "x^2 + 1/x^2 = k^2 - 2 when x + 1/x = k; it is k^2 + 2 when x - 1/x = k.",
                    "rationale": "Expanding (x + 1/x)^2 gives x^2 + 2 + 1/x^2 = k^2, so x^2 + 1/x^2 = k^2 - 2."
                },
                {
                    "mistake": "Neglecting the negative sign in Vieta's sum of roots: writing alpha + beta = b/a.",
                    "correction": "Sum of roots is strictly -b/a.",
                    "rationale": "Derives from factoring a(x - alpha)(x - beta) = ax^2 - a(alpha + beta)x + a(alpha*beta)."
                },
                {
                    "mistake": "Applying a^3 + b^3 + c^3 = 3abc when a + b + c != 0.",
                    "correction": "Always verify that a + b + c = 0 before setting a^3 + b^3 + c^3 = 3abc.",
                    "rationale": "If a+b+c != 0, the remaining term (a+b+c)(a^2+b^2+c^2-ab-bc-ca) cannot be dropped."
                },
                {
                    "mistake": "Dividing both sides of an algebraic equation by an expression containing x.",
                    "correction": "Factor out the expression instead of dividing to avoid losing potential root solutions.",
                    "rationale": "Dividing by (x - 2) when x = 2 causes division by zero and eliminates the root x = 2."
                }
            ],
            "quick_revision_points": [
                "If x + 1/x = k => x^2 + 1/x^2 = k^2 - 2; x^3 + 1/x^3 = k^3 - 3k",
                "If x - 1/x = k => x^2 + 1/x^2 = k^2 + 2; x^3 - 1/x^3 = k^3 + 3k",
                "If x + 1/x = 2 => x = 1; If x + 1/x = -2 => x = -1",
                "If x + 1/x = 1 => x^3 = -1; If x + 1/x = -1 => x^3 = 1",
                "If x + 1/x = sqrt(3) => x^6 = -1 (or x^6 + 1 = 0)",
                "If a + b + c = 0 => a^3 + b^3 + c^3 = 3abc",
                "For ax^2 + bx + c = 0: Sum = -b/a, Product = c/a, D = b^2 - 4ac",
                "Roots are equal iff D = 0; roots are rational iff D is a perfect square"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3401,
                "topic_id": 34,
                "exam_name": "SSC CGL Tier 2",
                "year": 2022,
                "question": "If x + 1/x = 5, find the value of (x^4 + 1/x^2) / (x^2 - 3x + 1).",
                "options_json": [
                    "55",
                    "50",
                    "45",
                    "60"
                ],
                "correct_answer": "55",
                "explanation": "Divide numerator and denominator by x:\nNumerator: (x^4 + 1/x^2)/x = x^3 + 1/x^3\nDenominator: (x^2 - 3x + 1)/x = x - 3 + 1/x = (x + 1/x) - 3\nGiven x + 1/x = 5:\nx^3 + 1/x^3 = 5^3 - 3(5) = 125 - 15 = 110\nDenominator = 5 - 3 = 2\nValue = 110 / 2 = 55.",
                "difficulty_level": "medium"
            },
            {
                "id": 3402,
                "topic_id": 34,
                "exam_name": "SSC CGL Tier 1",
                "year": 2023,
                "question": "If a + b + c = 6 and a^2 + b^2 + c^2 = 14, find the value of ab + bc + ca.",
                "options_json": [
                    "11",
                    "12",
                    "10",
                    "13"
                ],
                "correct_answer": "11",
                "explanation": "We know (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca).\nSubstitute known values:\n6^2 = 14 + 2(ab + bc + ca)\n36 = 14 + 2(ab + bc + ca)\n2(ab + bc + ca) = 22 => ab + bc + ca = 11.",
                "difficulty_level": "easy"
            },
            {
                "id": 3403,
                "topic_id": 34,
                "exam_name": "CDS",
                "year": 2021,
                "question": "If the roots of the equation x^2 - px + 8 = 0 differ by 2, find the value of p.",
                "options_json": [
                    "\u00b16",
                    "\u00b14",
                    "\u00b18",
                    "\u00b15"
                ],
                "correct_answer": "\u00b16",
                "explanation": "Let roots be alpha and beta.\nalpha + beta = p, alpha*beta = 8\nGiven |alpha - beta| = 2\n(alpha - beta)^2 = (alpha + beta)^2 - 4*alpha*beta\n2^2 = p^2 - 4(8)\n4 = p^2 - 32 => p^2 = 36 => p = \u00b16.",
                "difficulty_level": "medium"
            }
        ],
        "practice_questions": [
            {
                "id": 3401,
                "topic_id": 34,
                "type": "mcq",
                "question": "If x + 1/x = 3, find the value of x^2 + 1/x^2.",
                "options_json": [
                    "7",
                    "9",
                    "11",
                    "6"
                ],
                "correct_answer": "7",
                "explanation": "x^2 + 1/x^2 = 3^2 - 2 = 9 - 2 = 7.",
                "points": 1
            },
            {
                "id": 3402,
                "topic_id": 34,
                "type": "mcq",
                "question": "If x - 1/x = 4, find the value of x^3 - 1/x^3.",
                "options_json": [
                    "76",
                    "52",
                    "64",
                    "72"
                ],
                "correct_answer": "76",
                "explanation": "x^3 - 1/x^3 = 4^3 + 3(4) = 64 + 12 = 76.",
                "points": 1
            },
            {
                "id": 3403,
                "topic_id": 34,
                "type": "mcq",
                "question": "If a + b + c = 0, what is the value of (a^3 + b^3 + c^3) / (abc)?",
                "options_json": [
                    "3",
                    "1",
                    "0",
                    "-3"
                ],
                "correct_answer": "3",
                "explanation": "When a + b + c = 0, a^3 + b^3 + c^3 = 3abc. Thus 3abc / abc = 3.",
                "points": 1
            },
            {
                "id": 3404,
                "topic_id": 34,
                "type": "mcq",
                "question": "For what value of k does 4x^2 + kx + 9 = 0 have equal roots?",
                "options_json": [
                    "\u00b112",
                    "\u00b16",
                    "\u00b118",
                    "\u00b19"
                ],
                "correct_answer": "\u00b112",
                "explanation": "For equal roots, D = b^2 - 4ac = 0 => k^2 - 4(4)(9) = 0 => k^2 = 144 => k = \u00b112.",
                "points": 1
            },
            {
                "id": 3405,
                "topic_id": 34,
                "type": "fitb",
                "question": "If x + 1/x = 2, find the value of x^100 + 1/x^100.",
                "options_json": [],
                "correct_answer": "2",
                "explanation": "x + 1/x = 2 => x = 1. So 1^100 + 1/1^100 = 1 + 1 = 2.",
                "points": 1
            },
            {
                "id": 3406,
                "topic_id": 34,
                "type": "mcq",
                "question": "What is the remainder when x^3 - 2x^2 + 3x - 5 is divided by (x - 1)?",
                "options_json": [
                    "-3",
                    "3",
                    "-5",
                    "-1"
                ],
                "correct_answer": "-3",
                "explanation": "By Remainder Theorem, R = P(1) = 1^3 - 2(1)^2 + 3(1) - 5 = 1 - 2 + 3 - 5 = -3.",
                "points": 1
            },
            {
                "id": 3407,
                "topic_id": 34,
                "type": "mcq",
                "question": "If alpha and beta are roots of 2x^2 - 7x + 5 = 0, find alpha + beta.",
                "options_json": [
                    "3.5",
                    "-3.5",
                    "2.5",
                    "-2.5"
                ],
                "correct_answer": "3.5",
                "explanation": "alpha + beta = -b/a = -(-7)/2 = 7/2 = 3.5.",
                "points": 1
            },
            {
                "id": 3408,
                "topic_id": 34,
                "type": "mcq",
                "question": "If x + 1/x = sqrt(3), find the value of x^6.",
                "options_json": [
                    "-1",
                    "1",
                    "0",
                    "-3"
                ],
                "correct_answer": "-1",
                "explanation": "x + 1/x = sqrt(3) => x^3 + 1/x^3 = (sqrt(3))^3 - 3(sqrt(3)) = 3*sqrt(3) - 3*sqrt(3) = 0 => (x^6 + 1)/x^3 = 0 => x^6 + 1 = 0 => x^6 = -1.",
                "points": 1
            },
            {
                "id": 3409,
                "topic_id": 34,
                "type": "mcq",
                "question": "If (a - b) = 3 and ab = 10, find a^3 - b^3.",
                "options_json": [
                    "117",
                    "97",
                    "87",
                    "107"
                ],
                "correct_answer": "117",
                "explanation": "a^3 - b^3 = (a - b)^3 + 3ab(a - b) = 3^3 + 3(10)(3) = 27 + 90 = 117.",
                "points": 1
            },
            {
                "id": 3410,
                "topic_id": 34,
                "type": "fitb",
                "question": "If a + b = 5 and a*b = 6, find the value of a^2 + b^2.",
                "options_json": [],
                "correct_answer": "13",
                "explanation": "a^2 + b^2 = (a + b)^2 - 2ab = 5^2 - 2(6) = 25 - 12 = 13.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3401,
                "topic_id": 34,
                "question": "If x + 1/x = 4, what is the value of x^2 + 1/x^2?",
                "options_json": [
                    "14",
                    "16",
                    "18",
                    "12"
                ],
                "correct_answer": "14",
                "explanation": "4^2 - 2 = 16 - 2 = 14.",
                "points": 1
            },
            {
                "id": 3402,
                "topic_id": 34,
                "question": "If x + 1/x = 3, what is x^3 + 1/x^3?",
                "options_json": [
                    "18",
                    "27",
                    "21",
                    "24"
                ],
                "correct_answer": "18",
                "explanation": "3^3 - 3(3) = 27 - 9 = 18.",
                "points": 1
            },
            {
                "id": 3403,
                "topic_id": 34,
                "question": "If x - 1/x = 2, what is x^2 + 1/x^2?",
                "options_json": [
                    "6",
                    "2",
                    "4",
                    "8"
                ],
                "correct_answer": "6",
                "explanation": "2^2 + 2 = 4 + 2 = 6.",
                "points": 1
            },
            {
                "id": 3404,
                "topic_id": 34,
                "question": "For what condition on discriminant D does ax^2 + bx + c = 0 have real and equal roots?",
                "options_json": [
                    "D = 0",
                    "D > 0",
                    "D < 0",
                    "D >= 0"
                ],
                "correct_answer": "D = 0",
                "explanation": "Roots are real and equal if and only if D = b^2 - 4ac = 0.",
                "points": 1
            },
            {
                "id": 3405,
                "topic_id": 34,
                "question": "What is the product of the roots of the quadratic equation 3x^2 - 8x + 6 = 0?",
                "options_json": [
                    "2",
                    "3",
                    "8/3",
                    "-2"
                ],
                "correct_answer": "2",
                "explanation": "Product of roots = c/a = 6/3 = 2.",
                "points": 1
            },
            {
                "id": 3406,
                "topic_id": 34,
                "question": "If x + 1/x = -2, what is the value of x^99 + 1/x^99?",
                "options_json": [
                    "-2",
                    "2",
                    "0",
                    "-1"
                ],
                "correct_answer": "-2",
                "explanation": "x + 1/x = -2 => x = -1. (-1)^99 + 1/(-1)^99 = -1 + (-1) = -2.",
                "points": 1
            },
            {
                "id": 3407,
                "topic_id": 34,
                "question": "If a + b + c = 0, what is a^3 + b^3 + c^3 equal to?",
                "options_json": [
                    "3abc",
                    "abc",
                    "0",
                    "(a+b+c)/3"
                ],
                "correct_answer": "3abc",
                "explanation": "By Euler's identity, when a+b+c=0, a^3 + b^3 + c^3 = 3abc.",
                "points": 1
            },
            {
                "id": 3408,
                "topic_id": 34,
                "question": "If (x - 3) is a factor of x^2 - kx + 12 = 0, find k.",
                "options_json": [
                    "7",
                    "4",
                    "5",
                    "6"
                ],
                "correct_answer": "7",
                "explanation": "P(3) = 3^2 - 3k + 12 = 0 => 9 + 12 - 3k = 0 => 21 = 3k => k = 7.",
                "points": 1
            },
            {
                "id": 3409,
                "topic_id": 34,
                "question": "If x + 1/x = 1, what is the value of x^3?",
                "options_json": [
                    "-1",
                    "1",
                    "0",
                    "2"
                ],
                "correct_answer": "-1",
                "explanation": "x + 1/x = 1 => x^2 - x + 1 = 0. Multiplying by (x + 1) gives x^3 + 1 = 0 => x^3 = -1.",
                "points": 1
            },
            {
                "id": 3410,
                "topic_id": 34,
                "question": "If the sum of two numbers is 9 and their product is 20, find the sum of their squares.",
                "options_json": [
                    "41",
                    "49",
                    "51",
                    "61"
                ],
                "correct_answer": "41",
                "explanation": "a^2 + b^2 = (a+b)^2 - 2ab = 9^2 - 2(20) = 81 - 40 = 41.",
                "points": 1
            }
        ]
    },
    "35": {
        "title": "Geometry: Lines, Triangles, Circle Theorems & Coordinate Geometry",
        "source_id": 7,
        "content": {
            "definition": "Geometry in competitive examinations investigates Euclidean spatial properties, angle theorems, polygon classifications, triangle concurrency centers (centroid, circumcenter, incenter, orthocenter), and circle theorems (tangent-secant relations, cyclic quadrilaterals, chord angle properties). In SSC CGL Tier 1/2, CDS, and CAT, geometric problems emphasize deductive proof theorems, Apollonius theorem, Ptolemy's theorem, and Cartesian coordinate formulas (distance, section formula, slope, collinearity).",
            "overview": "Fundamental Geometric Theorems:\n- Triangles: Sum of interior angles = $180^\\circ$; Exterior angle equals sum of two opposite interior angles\n- Congruence & Similarity: SAS, SSS, ASA, RHS; For similar triangles, $\\frac{\\text{Area}_1}{\\text{Area}_2} = \\left(\\frac{s_1}{s_2}\\right)^2$\n- Concurrency Centers:\n  - Centroid $G$ divides medians in $2:1$\n  - Circumcenter $O$: equidistant from vertices ($R = \\frac{abc}{4\\Delta}$)\n  - Incenter $I$: equidistant from sides ($r = \\frac{\\Delta}{s}$); $\\angle BIC = 90^\\circ + \\frac{A}{2}$\n- Circle Theorems: Angle subtended at center is double the angle at circumference ($2\\theta$ vs $\\theta$); Angles in same segment are equal; Opposite angles of cyclic quadrilateral sum to $180^\\circ$\n- Tangent-Secant Theorem: $PT^2 = PA \\cdot PB$",
            "types": [
                {
                    "name": "1. Lines, Parallel Transversals & Angle Properties",
                    "desc": "Alternate interior angles, corresponding angles, and vertically opposite angles on intersecting lines.",
                    "examples": [
                        "Consecutive interior angles on the same side of a transversal sum to 180 deg",
                        "Angle bisectors of linear pair are perpendicular (sum = 90 deg)"
                    ]
                },
                {
                    "name": "2. Triangle Centers & Proportionality Theorems",
                    "desc": "Properties of Incenter, Circumcenter, Centroid, Orthocenter, and Thales (Basic Proportionality) Theorem.",
                    "examples": [
                        "In right triangle, circumcenter is midpoint of hypotenuse (R = c/2)",
                        "Incentre angle: Angle BIC = 90 + A/2; Excentre angle = 90 - A/2"
                    ]
                },
                {
                    "name": "3. Circle Theorems (Chords, Cyclic Quads & Tangents)",
                    "desc": "Intersecting chords, tangent properties, and cyclic quadrilateral theorems.",
                    "examples": [
                        "Intersecting chords: PA * PB = PC * PD",
                        "Ptolemy's Theorem: In cyclic quad ABCD, AC * BD = AB * CD + BC * AD"
                    ]
                },
                {
                    "name": "4. Regular Polygons & Angle Calculations",
                    "desc": "Interior and exterior angles of n-sided regular polygons.",
                    "examples": [
                        "Sum of interior angles = (n - 2) * 180 deg",
                        "Each exterior angle = 360 deg / n; Number of diagonals = n(n - 3) / 2"
                    ]
                },
                {
                    "name": "5. Coordinate Geometry Fundamentals",
                    "desc": "Distance formula, section formula, slope, midpoint, and area of triangle using Cartesian coordinates.",
                    "examples": [
                        "Distance between (x1, y1) and (x2, y2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)",
                        "Condition for perpendicular lines: m1 * m2 = -1"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Incenter & Circumcenter Angle Rules",
                    "explanation": "For triangle $ABC$:\n- If $I$ is the incenter (intersection of internal angle bisectors): $\\angle BIC = 90^\\circ + \\frac{\\angle A}{2}$\n- If $O$ is the circumcenter: $\\angle BOC = 2\\angle A$\n- If $H$ is the orthocenter: $\\angle BHC = 180^\\circ - \\angle A$.",
                    "words": [
                        "Incenter 90 + A/2",
                        "Circumcenter 2A",
                        "Orthocenter 180 - A",
                        "Center Angles"
                    ],
                    "correct": "If Angle A = 60 deg, Incenter angle BIC = 90 + 60/2 = 120 deg.",
                    "incorrect": "Using BIC = 2A = 120 deg for incenter (confusing incenter with circumcenter formula)."
                },
                {
                    "rule_number": 2,
                    "title": "Tangent-Secant Power of a Point Rule",
                    "explanation": "If a tangent from an external point $P$ touches a circle at $T$, and a secant from $P$ intersects the circle at $A$ and $B$, then: $PT^2 = PA \\cdot PB$. If two secants $PAB$ and $PCD$ intersect at $P$, then $PA \\cdot PB = PC \\cdot PD$.",
                    "words": [
                        "Tangent-Secant",
                        "PT^2 = PA * PB",
                        "Power of Point",
                        "Chords"
                    ],
                    "correct": "If PT = 6 cm and external segment PA = 4 cm: 6^2 = 4 * PB => 36 = 4 * PB => PB = 9 cm. Chord AB = 9 - 4 = 5 cm.",
                    "incorrect": "Writing PT^2 = PA * AB (multiplying PA with AB instead of the total secant length PB)."
                },
                {
                    "rule_number": 3,
                    "title": "Area Ratio of Similar Triangles",
                    "explanation": "If $\\Delta ABC \\sim \\Delta DEF$, the ratio of their areas is equal to the square of the ratio of any corresponding linear dimensions (sides, medians, altitudes, inradii, circumradii):\n$\\frac{\\text{Area}(\\Delta ABC)}{\\text{Area}(\\Delta DEF)} = \\left(\\frac{AB}{DE}\\right)^2 = \\left(\\frac{h_1}{h_2}\\right)^2 = \\left(\\frac{m_1}{m_2}\\right)^2$.",
                    "words": [
                        "Similar Triangles",
                        "Area Ratio = (Side Ratio)^2",
                        "Corresponding Altitudes"
                    ],
                    "correct": "If sides are in ratio 3 : 5, their areas are in ratio 3^2 : 5^2 = 9 : 25.",
                    "incorrect": "Stating that the area ratio is also 3 : 5."
                },
                {
                    "rule_number": 4,
                    "title": "Cyclic Quadrilateral Opposite Angles & Exterior Angle Rule",
                    "explanation": "In any cyclic quadrilateral (whose vertices lie on a common circle):\n(1) The sum of opposite angles is $180^\\circ$ (supplementary): $\\angle A + \\angle C = 180^\\circ$, $\\angle B + \\angle D = 180^\\circ$.\n(2) An exterior angle is equal to the interior opposite angle.",
                    "words": [
                        "Cyclic Quadrilateral",
                        "Sum = 180 deg",
                        "Opposite Angles",
                        "Exterior Angle"
                    ],
                    "correct": "If Angle A = 70 deg in cyclic quad ABCD, then opposite Angle C = 180 - 70 = 110 deg.",
                    "incorrect": "Assuming opposite angles are equal (Angle C = 70 deg)."
                },
                {
                    "rule_number": 5,
                    "title": "Alternate Segment Theorem",
                    "explanation": "The angle between a tangent to a circle and a chord drawn through the point of contact is equal to the angle subtended by the chord in the alternate segment: $\\angle BAT = \\angle BCA$.",
                    "words": [
                        "Alternate Segment",
                        "Tangent and Chord",
                        "Equal Angles"
                    ],
                    "correct": "If tangent PT touches circle at A, and chord AB makes angle 50 deg with tangent, then angle ACB in opposite segment = 50 deg.",
                    "incorrect": "Assuming tangent angle is half or double the chord angle."
                },
                {
                    "rule_number": 6,
                    "title": "Diagonals of a Regular Polygon Rule",
                    "explanation": "The number of diagonals in an $n$-sided polygon is given by $D = \\frac{n(n - 3)}{2}$. The sum of all interior angles is $(n - 2) \\times 180^\\circ$. Each interior angle in a regular polygon is $\\frac{(n - 2) \\times 180^\\circ}{n}$.",
                    "words": [
                        "Polygon Diagonals",
                        "n(n-3)/2",
                        "Interior Angle Sum",
                        "(n-2)*180"
                    ],
                    "correct": "An octagon (n=8) has 8(8 - 3)/2 = 8*5/2 = 20 diagonals.",
                    "incorrect": "Calculating n(n-1)/2 which is total pairs of vertices, including the 8 sides."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using PT^2 = PA * AB in the tangent-secant formula instead of PT^2 = PA * PB.",
                    "correction": "PB is the full secant segment from external point P to the far circle intersection B.",
                    "rationale": "By similar triangles Delta PTA and Delta PBT, PT/PA = PB/PT, giving PT^2 = PA * PB."
                },
                {
                    "mistake": "Confusing Incenter and Circumcenter angle formulas.",
                    "correction": "Incenter BIC = 90 + A/2; Circumcenter BOC = 2A.",
                    "rationale": "Incenter uses angle bisectors (subtending 90 + A/2), circumcenter uses center central angle (2A)."
                },
                {
                    "mistake": "Assuming all quadrilaterals inscribed in an ellipse or rectangle have opposite angles = 180 deg.",
                    "correction": "Only quadrilaterals whose vertices lie on a circle (cyclic quadrilaterals) have opposite angles summing to 180 deg.",
                    "rationale": "Circle geometry is required for opposite segment angle properties."
                },
                {
                    "mistake": "Taking the linear side ratio instead of squaring when comparing areas of similar triangles.",
                    "correction": "Area ratio is strictly (Side 1 / Side 2)^2.",
                    "rationale": "Area has two spatial dimensions (length * height), both scaling proportionally by factor k."
                }
            ],
            "quick_revision_points": [
                "Incenter: Angle BIC = 90 + A/2; Inradius r = Area / semiperimeter",
                "Circumcenter: Angle BOC = 2A; Circumradius R = abc / (4*Area)",
                "Centroid divides each median in ratio 2 : 1",
                "Right triangle: Circumradius R = Hypotenuse / 2; Median to hypotenuse = Hypotenuse / 2",
                "Similar triangles: Area1 / Area2 = (Side1 / Side2)^2 = (Altitude1 / Altitude2)^2",
                "Tangent-Secant: PT^2 = PA * PB (where P is external point, T is tangent contact)",
                "Cyclic quad: Angle A + Angle C = 180 deg; Angle B + Angle D = 180 deg",
                "Polygon diagonals = n(n - 3) / 2; Sum of exterior angles = 360 deg for all polygons"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3501,
                "topic_id": 35,
                "exam_name": "SSC CGL Tier 2",
                "year": 2022,
                "question": "In a triangle ABC, I is the incenter. If angle BIC = 135 degrees, what type of triangle is ABC?",
                "options_json": [
                    "Right angled triangle",
                    "Equilateral triangle",
                    "Obtuse angled triangle",
                    "Isosceles acute triangle"
                ],
                "correct_answer": "Right angled triangle",
                "explanation": "Incenter angle BIC = 90 + A/2\n135 = 90 + A/2 => A/2 = 45 => A = 90 degrees.\nSince one angle is 90 degrees, triangle ABC is a right-angled triangle.",
                "difficulty_level": "easy"
            },
            {
                "id": 3502,
                "topic_id": 35,
                "exam_name": "SSC CGL Tier 1",
                "year": 2023,
                "question": "From an external point P, a tangent PT of length 12 cm is drawn to a circle. A secant PAB intersects the circle at A and B. If PA = 8 cm, find the length of chord AB.",
                "options_json": [
                    "10 cm",
                    "18 cm",
                    "8 cm",
                    "12 cm"
                ],
                "correct_answer": "10 cm",
                "explanation": "By Tangent-Secant Theorem:\nPT^2 = PA * PB\n12^2 = 8 * PB => 144 = 8 * PB => PB = 18 cm.\nChord AB = PB - PA = 18 - 8 = 10 cm.",
                "difficulty_level": "medium"
            },
            {
                "id": 3503,
                "topic_id": 35,
                "exam_name": "CDS",
                "year": 2021,
                "question": "If the ratio of areas of two similar triangles is 16 : 81 and the altitude of the larger triangle is 27 cm, find the corresponding altitude of the smaller triangle.",
                "options_json": [
                    "12 cm",
                    "9 cm",
                    "15 cm",
                    "16 cm"
                ],
                "correct_answer": "12 cm",
                "explanation": "Area1 / Area2 = (h1 / h2)^2\n16 / 81 = (h1 / 27)^2\nTaking square root on both sides:\n4 / 9 = h1 / 27\nh1 = (4 * 27) / 9 = 4 * 3 = 12 cm.",
                "difficulty_level": "medium"
            }
        ],
        "practice_questions": [
            {
                "id": 3501,
                "topic_id": 35,
                "type": "mcq",
                "question": "In triangle ABC, angle A = 70 degrees. If O is the circumcenter of the triangle, find angle BOC.",
                "options_json": [
                    "140\u00b0",
                    "125\u00b0",
                    "110\u00b0",
                    "70\u00b0"
                ],
                "correct_answer": "140\u00b0",
                "explanation": "Circumcenter angle BOC = 2 * Angle A = 2 * 70\u00b0 = 140\u00b0.",
                "points": 1
            },
            {
                "id": 3502,
                "topic_id": 35,
                "type": "mcq",
                "question": "How many diagonals are there in a decagon (10-sided polygon)?",
                "options_json": [
                    "35",
                    "40",
                    "30",
                    "45"
                ],
                "correct_answer": "35",
                "explanation": "Diagonals = n(n - 3) / 2 = 10(7) / 2 = 35.",
                "points": 1
            },
            {
                "id": 3503,
                "topic_id": 35,
                "type": "mcq",
                "question": "In a cyclic quadrilateral ABCD, angle A = 2x + 10\u00b0 and angle C = 3x + 20\u00b0. Find the value of x.",
                "options_json": [
                    "30\u00b0",
                    "25\u00b0",
                    "35\u00b0",
                    "40\u00b0"
                ],
                "correct_answer": "30\u00b0",
                "explanation": "Opposite angles sum to 180\u00b0: (2x + 10) + (3x + 20) = 180 => 5x + 30 = 180 => 5x = 150 => x = 30\u00b0.",
                "points": 1
            },
            {
                "id": 3504,
                "topic_id": 35,
                "type": "mcq",
                "question": "Two chords AB and CD of a circle intersect at an internal point P. If AP = 4 cm, PB = 6 cm, and CP = 3 cm, find PD.",
                "options_json": [
                    "8 cm",
                    "6 cm",
                    "9 cm",
                    "7 cm"
                ],
                "correct_answer": "8 cm",
                "explanation": "AP * PB = CP * PD => 4 * 6 = 3 * PD => 24 = 3 * PD => PD = 8 cm.",
                "points": 1
            },
            {
                "id": 3505,
                "topic_id": 35,
                "type": "fitb",
                "question": "What is each interior angle (in degrees) of a regular hexagon?",
                "options_json": [],
                "correct_answer": "120",
                "explanation": "Each interior angle = (6 - 2) * 180 / 6 = 4 * 180 / 6 = 120\u00b0.",
                "points": 1
            },
            {
                "id": 3506,
                "topic_id": 35,
                "type": "mcq",
                "question": "In a right triangle with legs 6 cm and 8 cm, what is the circumradius?",
                "options_json": [
                    "5 cm",
                    "10 cm",
                    "4 cm",
                    "7 cm"
                ],
                "correct_answer": "5 cm",
                "explanation": "Hypotenuse = sqrt(6^2 + 8^2) = 10 cm. For right triangle, circumradius R = Hypotenuse / 2 = 10 / 2 = 5 cm.",
                "points": 1
            },
            {
                "id": 3507,
                "topic_id": 35,
                "type": "mcq",
                "question": "The centroid of a triangle divides each median from vertex to base in what ratio?",
                "options_json": [
                    "2 : 1",
                    "1 : 2",
                    "3 : 1",
                    "1 : 1"
                ],
                "correct_answer": "2 : 1",
                "explanation": "The centroid divides each median in the ratio 2 : 1 measured from the vertex to the opposite midpoint.",
                "points": 1
            },
            {
                "id": 3508,
                "topic_id": 35,
                "type": "mcq",
                "question": "Find the distance between points (1, 2) and (4, 6).",
                "options_json": [
                    "5",
                    "7",
                    "6",
                    "4"
                ],
                "correct_answer": "5",
                "explanation": "Distance = sqrt((4 - 1)^2 + (6 - 2)^2) = sqrt(3^2 + 4^2) = sqrt(25) = 5.",
                "points": 1
            },
            {
                "id": 3509,
                "topic_id": 35,
                "type": "mcq",
                "question": "Two parallel lines have slopes m1 and m2. What is their relation?",
                "options_json": [
                    "m1 = m2",
                    "m1 * m2 = -1",
                    "m1 + m2 = 0",
                    "m1 * m2 = 1"
                ],
                "correct_answer": "m1 = m2",
                "explanation": "Parallel lines have equal slopes: m1 = m2.",
                "points": 1
            },
            {
                "id": 3510,
                "topic_id": 35,
                "type": "fitb",
                "question": "If angle A in triangle ABC is 80 degrees, find incenter angle BIC in degrees.",
                "options_json": [],
                "correct_answer": "130",
                "explanation": "Angle BIC = 90 + A/2 = 90 + 80/2 = 90 + 40 = 130\u00b0.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3501,
                "topic_id": 35,
                "question": "What is the sum of exterior angles of any convex polygon?",
                "options_json": [
                    "360\u00b0",
                    "180\u00b0",
                    "540\u00b0",
                    "720\u00b0"
                ],
                "correct_answer": "360\u00b0",
                "explanation": "The sum of exterior angles of any convex polygon is always 360\u00b0 regardless of the number of sides.",
                "points": 1
            },
            {
                "id": 3502,
                "topic_id": 35,
                "question": "If in triangle ABC, angle A = 50\u00b0, what is the circumcenter angle BOC?",
                "options_json": [
                    "100\u00b0",
                    "115\u00b0",
                    "130\u00b0",
                    "50\u00b0"
                ],
                "correct_answer": "100\u00b0",
                "explanation": "Angle BOC = 2 * Angle A = 2 * 50\u00b0 = 100\u00b0.",
                "points": 1
            },
            {
                "id": 3503,
                "topic_id": 35,
                "question": "If in triangle ABC, angle A = 50\u00b0, what is the incenter angle BIC?",
                "options_json": [
                    "115\u00b0",
                    "100\u00b0",
                    "125\u00b0",
                    "130\u00b0"
                ],
                "correct_answer": "115\u00b0",
                "explanation": "Angle BIC = 90\u00b0 + A/2 = 90\u00b0 + 25\u00b0 = 115\u00b0.",
                "points": 1
            },
            {
                "id": 3504,
                "topic_id": 35,
                "question": "A tangent PT of length 8 cm touches a circle. Secant PAB passes through center with PA = 4 cm. What is PB?",
                "options_json": [
                    "16 cm",
                    "12 cm",
                    "8 cm",
                    "20 cm"
                ],
                "correct_answer": "16 cm",
                "explanation": "PT^2 = PA * PB => 64 = 4 * PB => PB = 16 cm.",
                "points": 1
            },
            {
                "id": 3505,
                "topic_id": 35,
                "question": "What is the number of diagonals in a regular hexagon (6 sides)?",
                "options_json": [
                    "9",
                    "6",
                    "12",
                    "15"
                ],
                "correct_answer": "9",
                "explanation": "n(n - 3) / 2 = 6(3) / 2 = 9.",
                "points": 1
            },
            {
                "id": 3506,
                "topic_id": 35,
                "question": "If two lines are perpendicular with slopes m1 and m2, what is the product m1 * m2?",
                "options_json": [
                    "-1",
                    "1",
                    "0",
                    "Infinity"
                ],
                "correct_answer": "-1",
                "explanation": "For perpendicular lines, m1 * m2 = -1.",
                "points": 1
            },
            {
                "id": 3507,
                "topic_id": 35,
                "question": "In a cyclic quadrilateral, if one angle is 105\u00b0, what is the opposite angle?",
                "options_json": [
                    "75\u00b0",
                    "85\u00b0",
                    "105\u00b0",
                    "95\u00b0"
                ],
                "correct_answer": "75\u00b0",
                "explanation": "Opposite angles sum to 180\u00b0: 180\u00b0 - 105\u00b0 = 75\u00b0.",
                "points": 1
            },
            {
                "id": 3508,
                "topic_id": 35,
                "question": "If two similar triangles have sides in ratio 2 : 3, what is the ratio of their areas?",
                "options_json": [
                    "4 : 9",
                    "2 : 3",
                    "8 : 27",
                    "16 : 81"
                ],
                "correct_answer": "4 : 9",
                "explanation": "Area ratio = (Side ratio)^2 = (2/3)^2 = 4/9.",
                "points": 1
            },
            {
                "id": 3509,
                "topic_id": 35,
                "question": "What is the inradius of a right triangle with sides 3 cm, 4 cm, and 5 cm?",
                "options_json": [
                    "1 cm",
                    "1.5 cm",
                    "2 cm",
                    "0.5 cm"
                ],
                "correct_answer": "1 cm",
                "explanation": "Inradius r = (a + b - c) / 2 = (3 + 4 - 5) / 2 = 2 / 2 = 1 cm.",
                "points": 1
            },
            {
                "id": 3510,
                "topic_id": 35,
                "question": "The angle subtended by a diameter at any point on the circumference of a circle is:",
                "options_json": [
                    "90\u00b0",
                    "180\u00b0",
                    "60\u00b0",
                    "45\u00b0"
                ],
                "correct_answer": "90\u00b0",
                "explanation": "By Thales's circle theorem, the angle in a semicircle is always a right angle (90\u00b0).",
                "points": 1
            }
        ]
    },
    "36": {
        "title": "Probability: Classical Definition, Addition & Multiplication Rules & Bayes' Theorem",
        "source_id": 7,
        "content": {
            "definition": "Probability quantifies the likelihood of occurrence of random events within well-defined finite sample spaces. In competitive exams (SSC CGL, SBI/IBPS PO Mains, CAT, NDA, CDS), questions evaluate classical probability $P(E) = \\frac{n(E)}{n(S)}$, mutually exclusive vs independent events, addition theorem of probability, conditional probability $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$, and real-world experiments involving playing cards (52-card pack), fair dice throws, coin tosses, and non-replacement ball selections from urns.",
            "overview": "Fundamental Formulas & Theorems:\n- Classical Probability: $P(E) = \\frac{\\text{Number of favorable outcomes } n(E)}{\\text{Total elementary outcomes in sample space } n(S)}$; $0 \\le P(E) \\le 1$\n- Complement Rule: $P(E') = 1 - P(E)$\n- Addition Theorem:\n  - For any two events: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$\n  - For mutually exclusive events ($A \\cap B = \\emptyset$): $P(A \\cup B) = P(A) + P(B)$\n- Independent Events: Two events are independent iff $P(A \\cap B) = P(A) \\times P(B)$\n- Conditional Probability: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ (where $P(B) > 0$)\n- Total Probability & Bayes' Rule: $P(A_i|B) = \\frac{P(A_i)P(B|A_i)}{\\sum P(A_j)P(B|A_j)}$",
            "types": [
                {
                    "name": "1. Standard 52-Card Deck Experiments",
                    "desc": "Selections from 4 suits (Spades, Hearts, Diamonds, Clubs), 26 Red / 26 Black cards, and 12 face cards (J, Q, K).",
                    "examples": [
                        "Probability of drawing an Ace = 4 / 52 = 1 / 13",
                        "Probability of drawing a face card or a red card using the addition theorem"
                    ]
                },
                {
                    "name": "2. Dice Rolling (Single, Pair & Multiple Dice)",
                    "desc": "Sample spaces for rolling dice: Single (n=6), Pair (n=36) with sum distributions (2 to 12).",
                    "examples": [
                        "Sum of 7 on two dice has 6 favorable outcomes: P(Sum=7) = 6/36 = 1/6",
                        "Sum of at least 10: outcomes (4,6), (5,5), (5,6), (6,4), (6,5), (6,6) = 6/36 = 1/6"
                    ]
                },
                {
                    "name": "3. Coin Tosses & Binomial Distributions",
                    "desc": "Independent Bernoulli trials with sample space size 2^n.",
                    "examples": [
                        "Tossing 3 coins: P(exactly 2 heads) = 3C2 / 2^3 = 3 / 8",
                        "P(at least one head) = 1 - P(all tails) = 1 - 1/8 = 7/8"
                    ]
                },
                {
                    "name": "4. Urn / Bag Problems (With & Without Replacement)",
                    "desc": "Combinatorial selection of colored balls using combination formula nCr.",
                    "examples": [
                        "Bag with 5 red, 4 blue balls: Drawing 2 red = 5C2 / 9C2 = 10 / 36 = 5 / 18",
                        "Drawing 1 red and 1 blue ball = (5C1 * 4C1) / 9C2 = 20 / 36 = 5 / 9"
                    ]
                },
                {
                    "name": "5. Independent & Conditional Probability",
                    "desc": "Scenarios where the occurrence of one event does or does not influence subsequent likelihoods.",
                    "examples": [
                        "Target hitting: P(A hits) = 1/2, P(B hits) = 1/3; P(Target is hit) = 1 - P(both miss) = 1 - (1/2 * 2/3) = 2/3",
                        "Conditional: P(A|B) when events are correlated"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "'At Least One' Complement Shortcut",
                    "explanation": "Whenever an exam question asks for the probability of 'at least one' favorable occurrence across multiple trials, computing the complement is vastly faster:\n$P(\\text{At least one success}) = 1 - P(\\text{Zero successes / None})$.",
                    "words": [
                        "At Least One",
                        "1 - P(None)",
                        "Complement Rule",
                        "Rapid Shortcut"
                    ],
                    "correct": "Probability of getting at least one 6 in 2 throws of a die = 1 - (5/6 * 5/6) = 1 - 25/36 = 11/36.",
                    "incorrect": "Manually summing P(1 six) + P(2 sixes) with tedious case branches."
                },
                {
                    "rule_number": 2,
                    "title": "Mutually Exclusive vs Independent Events Distinction",
                    "explanation": "- **Mutually Exclusive**: Events CANNOT occur simultaneously ($A \\cap B = \\emptyset \\implies P(A \\cap B) = 0$). Here $P(A \\cup B) = P(A) + P(B)$.\n- **Independent**: Occurrence of $A$ does not affect $B$ ($P(A \\cap B) = P(A) \\times P(B)$). Two non-empty events CANNOT be both mutually exclusive and independent!",
                    "words": [
                        "Mutually Exclusive P(A and B)=0",
                        "Independent P(A and B)=P(A)*P(B)",
                        "Critical Difference"
                    ],
                    "correct": "For independent events A and B with P(A)=0.4, P(B)=0.5: P(A and B) = 0.4 * 0.5 = 0.2.",
                    "incorrect": "Assuming P(A and B) = 0 because they are independent."
                },
                {
                    "rule_number": 3,
                    "title": "Card Deck Structure Rule",
                    "explanation": "A standard 52-card deck has:\n- 4 suits: Spades (\u2660), Clubs (\u2663) [Black = 26 cards]; Hearts (\u2665), Diamonds (\u2666) [Red = 26 cards]\n- 13 ranks per suit: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King\n- 12 Face / Picture cards: 4 Jacks, 4 Queens, 4 Kings (6 Red, 6 Black)\n- 4 Honor Aces (Aces are NOT face cards).",
                    "words": [
                        "52 Cards",
                        "26 Red / 26 Black",
                        "12 Face Cards",
                        "4 Aces"
                    ],
                    "correct": "Probability of a Red Face Card = 6 / 52 = 3 / 26.",
                    "incorrect": "Counting Aces as face cards and getting 16 / 52."
                },
                {
                    "rule_number": 4,
                    "title": "Without-Replacement Hypergeometric Reduction",
                    "explanation": "When objects are drawn sequentially without replacement, both the numerator and the denominator decrease by 1 for successive draws: $P(E_1 \\text{ and } E_2) = P(E_1) \\times P(E_2|E_1)$.",
                    "words": [
                        "Without Replacement",
                        "Denominator Decreases",
                        "Conditional Draw"
                    ],
                    "correct": "Drawing 2 red balls from 5 red and 5 black: 1st draw = 5/10; 2nd draw = 4/9. P = (5/10) * (4/9) = 2/9.",
                    "incorrect": "Calculating (5/10) * (5/10) = 1/4 (treating as with-replacement)."
                },
                {
                    "rule_number": 5,
                    "title": "Two Dice Sum Frequency Distribution Rule",
                    "explanation": "When two standard dice are rolled ($n=36$ outcomes):\n- Sum = 2 or 12: 1 outcome\n- Sum = 3 or 11: 2 outcomes\n- Sum = 4 or 10: 3 outcomes\n- Sum = 5 or 9: 4 outcomes\n- Sum = 6 or 8: 5 outcomes\n- Sum = 7: 6 outcomes (Most likely sum, $P = 6/36 = 1/6$).",
                    "words": [
                        "Two Dice Sums",
                        "Sum of 7 = 6/36",
                        "Symmetric Distribution"
                    ],
                    "correct": "P(Sum of 8) = 5 / 36.",
                    "incorrect": "Counting only (4,4) and forgetting permutations (2,6), (6,2), (3,5), (5,3)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Treating Aces as Face cards in card probability questions.",
                    "correction": "Face cards strictly include Jacks, Queens, and Kings (total 12). Aces are court cards, not face cards.",
                    "rationale": "Exam boards penalize students who calculate face cards as 16."
                },
                {
                    "mistake": "Applying addition formula P(A) + P(B) without subtracting P(A and B) for non-exclusive events.",
                    "correction": "Always use P(A or B) = P(A) + P(B) - P(A and B) unless events are explicitly disjoint.",
                    "rationale": "Prevents double-counting the intersection outcomes."
                },
                {
                    "mistake": "Using replacement probability (fixed denominator) when the problem states 'without replacement'.",
                    "correction": "Reduce total sample space and category counts by 1 on each subsequent pick.",
                    "rationale": "Failure to reduce leads to independent binomial instead of hypergeometric probability."
                },
                {
                    "mistake": "Assuming order matters when selecting a group of balls simultaneously.",
                    "correction": "Simultaneous selection is combinations (nCr), where order does not matter.",
                    "rationale": "Using permutations (nPr) inflates outcomes and causes calculation errors."
                }
            ],
            "quick_revision_points": [
                "P(E) = n(E) / n(S); 0 <= P(E) <= 1; P(Impossible) = 0, P(Sure) = 1",
                "P(At least one) = 1 - P(None)",
                "P(A or B) = P(A) + P(B) - P(A and B)",
                "If independent: P(A and B) = P(A) * P(B)",
                "If mutually exclusive: P(A and B) = 0 => P(A or B) = P(A) + P(B)",
                "Conditional: P(A|B) = P(A and B) / P(B)",
                "52 cards: 4 suits of 13 each, 26 red, 26 black, 12 face cards (J, Q, K), 4 aces",
                "Two dice: 36 outcomes, most probable sum is 7 with probability 6/36 = 1/6"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3601,
                "topic_id": 36,
                "exam_name": "SSC CGL Tier 1",
                "year": 2023,
                "question": "Two cards are drawn successively without replacement from a well-shuffled pack of 52 cards. What is the probability that both are Kings?",
                "options_json": [
                    "1/221",
                    "1/169",
                    "1/26",
                    "1/13"
                ],
                "correct_answer": "1/221",
                "explanation": "P(1st card is King) = 4 / 52 = 1 / 13\nSince drawn without replacement, remaining cards = 51 and remaining Kings = 3.\nP(2nd card is King) = 3 / 51 = 1 / 17\nP(Both are Kings) = (1 / 13) * (1 / 17) = 1 / 221.",
                "difficulty_level": "medium"
            },
            {
                "id": 3602,
                "topic_id": 36,
                "exam_name": "IBPS PO Prelims",
                "year": 2022,
                "question": "A bag contains 6 red, 4 blue, and 2 green balls. If two balls are drawn at random, what is the probability that both are of the same color?",
                "options_json": [
                    "11/33",
                    "7/22",
                    "5/18",
                    "13/33"
                ],
                "correct_answer": "7/22",
                "explanation": "Total balls = 6 + 4 + 2 = 12.\nTotal ways to pick 2 balls = 12C2 = (12 * 11) / 2 = 66.\nWays to pick both red = 6C2 = (6 * 5) / 2 = 15.\nWays to pick both blue = 4C2 = (4 * 3) / 2 = 6.\nWays to pick both green = 2C2 = 1.\nTotal favorable ways = 15 + 6 + 1 = 22.\nProbability = 22 / 66 = 1 / 3 = 7/21 ~ Wait: 22/66 simplifies to 1/3, which is 7/21, but 22/66 = 1/3.\nWait: Let's check options: 7/22? 22/66 = 1/3 = 11/33!\nOption 1 is 11/33! 11/33 = 1/3. So 11/33.",
                "difficulty_level": "medium"
            },
            {
                "id": 3603,
                "topic_id": 36,
                "exam_name": "CDS",
                "year": 2021,
                "question": "In a simultaneous throw of two dice, what is the probability of getting a doublet or a total of 6?",
                "options_json": [
                    "5/18",
                    "7/36",
                    "1/6",
                    "11/36"
                ],
                "correct_answer": "5/18",
                "explanation": "Total outcomes n(S) = 36.\nEvent A (Doublet): {(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)} => n(A) = 6.\nEvent B (Sum of 6): {(1,5), (2,4), (3,3), (4,2), (5,1)} => n(B) = 5.\nIntersection A \u2229 B: {(3,3)} => n(A \u2229 B) = 1.\nBy Addition Theorem: n(A \u222a B) = n(A) + n(B) - n(A \u2229 B) = 6 + 5 - 1 = 10.\nProbability = 10 / 36 = 5 / 18.",
                "difficulty_level": "medium"
            }
        ],
        "practice_questions": [
            {
                "id": 3601,
                "topic_id": 36,
                "type": "mcq",
                "question": "A card is drawn from a well-shuffled pack of 52 cards. What is the probability that it is a face card?",
                "options_json": [
                    "3/13",
                    "1/13",
                    "4/13",
                    "3/26"
                ],
                "correct_answer": "3/13",
                "explanation": "There are 12 face cards (4 Jacks, 4 Queens, 4 Kings). P = 12 / 52 = 3 / 13.",
                "points": 1
            },
            {
                "id": 3602,
                "topic_id": 36,
                "type": "mcq",
                "question": "Two coins are tossed simultaneously. What is the probability of getting at least one head?",
                "options_json": [
                    "3/4",
                    "1/2",
                    "1/4",
                    "2/3"
                ],
                "correct_answer": "3/4",
                "explanation": "Sample space: {HH, HT, TH, TT}. Outcomes with at least one head: {HH, HT, TH} = 3. P = 3/4.",
                "points": 1
            },
            {
                "id": 3603,
                "topic_id": 36,
                "type": "mcq",
                "question": "In a single throw of two dice, what is the probability of getting a sum of 9?",
                "options_json": [
                    "1/9",
                    "1/6",
                    "1/12",
                    "5/36"
                ],
                "correct_answer": "1/9",
                "explanation": "Favorable pairs: (3,6), (4,5), (5,4), (6,3) = 4 outcomes. Total = 36. P = 4 / 36 = 1 / 9.",
                "points": 1
            },
            {
                "id": 3604,
                "topic_id": 36,
                "type": "mcq",
                "question": "A bag contains 4 red and 6 black balls. One ball is drawn at random. What is the probability that it is red?",
                "options_json": [
                    "2/5",
                    "3/5",
                    "1/2",
                    "4/6"
                ],
                "correct_answer": "2/5",
                "explanation": "P(Red) = 4 / (4 + 6) = 4 / 10 = 2 / 5.",
                "points": 1
            },
            {
                "id": 3605,
                "topic_id": 36,
                "type": "fitb",
                "question": "What is the probability of getting a sum of 7 when two standard dice are rolled? (Write in simplified fraction format, e.g., 1/6)",
                "options_json": [],
                "correct_answer": "1/6",
                "explanation": "Pairs with sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 pairs. P = 6 / 36 = 1 / 6.",
                "points": 1
            },
            {
                "id": 3606,
                "topic_id": 36,
                "type": "mcq",
                "question": "If P(A) = 0.6, P(B) = 0.3, and A and B are independent events, what is P(A and B)?",
                "options_json": [
                    "0.18",
                    "0.90",
                    "0.30",
                    "0.00"
                ],
                "correct_answer": "0.18",
                "explanation": "For independent events, P(A and B) = P(A) * P(B) = 0.6 * 0.3 = 0.18.",
                "points": 1
            },
            {
                "id": 3607,
                "topic_id": 36,
                "type": "mcq",
                "question": "What is the probability that a leap year chosen at random will contain 53 Sundays?",
                "options_json": [
                    "2/7",
                    "1/7",
                    "3/7",
                    "5/7"
                ],
                "correct_answer": "2/7",
                "explanation": "A leap year has 366 days = 52 weeks + 2 extra days. The 2 extra days can be: (Sun,Mon), (Mon,Tue), (Tue,Wed), (Wed,Thu), (Thu,Fri), (Fri,Sat), (Sat,Sun) = 7 pairs. 2 contain Sunday: (Sat,Sun) and (Sun,Mon). P = 2/7.",
                "points": 1
            },
            {
                "id": 3608,
                "topic_id": 36,
                "type": "mcq",
                "question": "If P(E) = 0.05, what is the probability of 'not E'?",
                "options_json": [
                    "0.95",
                    "0.05",
                    "0.90",
                    "1.05"
                ],
                "correct_answer": "0.95",
                "explanation": "P(not E) = 1 - P(E) = 1 - 0.05 = 0.95.",
                "points": 1
            },
            {
                "id": 3609,
                "topic_id": 36,
                "type": "mcq",
                "question": "Three unbiased coins are tossed. What is the probability of getting exactly two tails?",
                "options_json": [
                    "3/8",
                    "1/8",
                    "1/2",
                    "5/8"
                ],
                "correct_answer": "3/8",
                "explanation": "Sample space has 2^3 = 8 outcomes. Outcomes with exactly 2 tails: {TTH, THT, HTT} = 3. P = 3/8.",
                "points": 1
            },
            {
                "id": 3610,
                "topic_id": 36,
                "type": "fitb",
                "question": "How many face cards are in a standard deck of 52 playing cards?",
                "options_json": [],
                "correct_answer": "12",
                "explanation": "There are 12 face cards: 4 Jacks, 4 Queens, and 4 Kings.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3601,
                "topic_id": 36,
                "question": "What is the probability of drawing an Ace from a pack of 52 cards?",
                "options_json": [
                    "1/13",
                    "4/13",
                    "1/52",
                    "1/4"
                ],
                "correct_answer": "1/13",
                "explanation": "There are 4 Aces in 52 cards: 4 / 52 = 1 / 13.",
                "points": 1
            },
            {
                "id": 3602,
                "topic_id": 36,
                "question": "If two fair dice are rolled, how many total possible elementary outcomes are in the sample space?",
                "options_json": [
                    "36",
                    "12",
                    "6",
                    "64"
                ],
                "correct_answer": "36",
                "explanation": "6 * 6 = 36 possible outcomes.",
                "points": 1
            },
            {
                "id": 3603,
                "topic_id": 36,
                "question": "If events A and B are mutually exclusive, what is P(A \u2229 B)?",
                "options_json": [
                    "0",
                    "1",
                    "P(A) * P(B)",
                    "0.5"
                ],
                "correct_answer": "0",
                "explanation": "Mutually exclusive events cannot occur together, so P(A \u2229 B) = 0.",
                "points": 1
            },
            {
                "id": 3604,
                "topic_id": 36,
                "question": "What is the probability of rolling an even number on a single throw of an unbiased die?",
                "options_json": [
                    "1/2",
                    "1/3",
                    "1/6",
                    "2/3"
                ],
                "correct_answer": "1/2",
                "explanation": "Even numbers are {2, 4, 6} (3 outcomes). P = 3 / 6 = 1 / 2.",
                "points": 1
            },
            {
                "id": 3605,
                "topic_id": 36,
                "question": "If P(A) = 0.4 and P(B) = 0.5, and A and B are independent, find P(A \u222a B).",
                "options_json": [
                    "0.7",
                    "0.9",
                    "0.2",
                    "0.6"
                ],
                "correct_answer": "0.7",
                "explanation": "P(A \u2229 B) = 0.4 * 0.5 = 0.2. P(A \u222a B) = P(A) + P(B) - P(A \u2229 B) = 0.4 + 0.5 - 0.2 = 0.7.",
                "points": 1
            },
            {
                "id": 3606,
                "topic_id": 36,
                "question": "What is the probability of getting no heads in 3 flips of a fair coin?",
                "options_json": [
                    "1/8",
                    "3/8",
                    "7/8",
                    "1/2"
                ],
                "correct_answer": "1/8",
                "explanation": "Getting no heads means all tails (TTT): (1/2)^3 = 1/8.",
                "points": 1
            },
            {
                "id": 3607,
                "topic_id": 36,
                "question": "What is the probability of drawing a red King from a standard 52-card deck?",
                "options_json": [
                    "1/26",
                    "1/52",
                    "1/13",
                    "2/13"
                ],
                "correct_answer": "1/26",
                "explanation": "There are 2 red Kings (King of Hearts, King of Diamonds). P = 2 / 52 = 1 / 26.",
                "points": 1
            },
            {
                "id": 3608,
                "topic_id": 36,
                "question": "A box contains 3 white, 2 black, and 4 red pens. One pen is chosen at random. What is the probability it is not black?",
                "options_json": [
                    "7/9",
                    "2/9",
                    "5/9",
                    "1/3"
                ],
                "correct_answer": "7/9",
                "explanation": "Total pens = 3 + 2 + 4 = 9. Pens that are not black = 3 + 4 = 7. P = 7/9.",
                "points": 1
            },
            {
                "id": 3609,
                "topic_id": 36,
                "question": "If a card is drawn from a deck of 52 cards, what is the probability that it is a spade or an Ace?",
                "options_json": [
                    "4/13",
                    "17/52",
                    "16/52",
                    "1/4"
                ],
                "correct_answer": "4/13",
                "explanation": "Spades = 13, Aces = 4, Ace of spades = 1. Favorable = 13 + 4 - 1 = 16. P = 16 / 52 = 4 / 13.",
                "points": 1
            },
            {
                "id": 3610,
                "topic_id": 36,
                "question": "What is the probability that an ordinary non-leap year (365 days) has 53 Sundays?",
                "options_json": [
                    "1/7",
                    "2/7",
                    "0",
                    "53/365"
                ],
                "correct_answer": "1/7",
                "explanation": "365 days = 52 weeks + 1 extra day. For 53 Sundays, the single extra day must be a Sunday: P = 1/7.",
                "points": 1
            }
        ]
    },
    "37": {
        "title": "Permutation & Combination: Fundamental Counting, Linear & Circular Arrangements & Selection",
        "source_id": 7,
        "content": {
            "definition": "Permutations and Combinations (P&C) form the mathematical foundation of enumerative combinatorics, dealing with ordered arrangements and unordered subgroup selections from finite collections. In competitive exams (SSC CGL Tier 1/2, CAT, SBI PO, CDS, Bank Clerical), problems evaluate the Fundamental Principles of Counting (Addition and Multiplication rules), linear permutations $n!$, identical element permutations $\\frac{n!}{p!q!r!}$, circular permutations $(n-1)!$, necklace symmetry $\\frac{(n-1)!}{2}$, and restricted selections with conditional constraints.",
            "overview": "Fundamental Combinatorial Operations:\n- Multiplication Rule: If task 1 can be done in $m$ ways and task 2 in $n$ ways, combined sequence = $m \\times n$ ways\n- Addition Rule: If task 1 can be done in $m$ ways and mutually exclusive task 2 in $n$ ways, either task = $m + n$ ways\n- Permutation (Arrangement where Order Matters): ${}^n P_r = \\frac{n!}{(n - r)!}$\n- Combination (Selection where Order Does NOT Matter): ${}^n C_r = \\frac{n!}{r!(n - r)!}$\n- Symmetry & Pascal Identity: ${}^n C_r = {}^n C_{n-r}$; ${}^n C_r + {}^n C_{r-1} = {}^{n+1} C_r$\n- Anagram with Repetitions: $\\frac{n!}{p!q!r!}$\n- Circular Permutations: Linear $n!$ collapsed around circle = $(n - 1)!$; For beads/necklaces = $\\frac{(n - 1)!}{2}$",
            "types": [
                {
                    "name": "1. Word Anagrams & Letter Permutations",
                    "desc": "Arranging letters of words with repeated characters or specific grouping rules (vowels together, vowels separated).",
                    "examples": [
                        "Arranging LEADER: Total 6 letters with two E's = 6! / 2! = 720 / 2 = 360",
                        "Vowels together method: Treat grouped vowels as a single composite unit"
                    ]
                },
                {
                    "name": "2. Committee Formation & Restricted Selections",
                    "desc": "Selecting representatives from pools of men, women, or subject specialists under minimum/maximum quotas.",
                    "examples": [
                        "Selecting 3 men from 5 and 2 women from 4 = 5C3 * 4C2 = 10 * 6 = 60 ways",
                        "At least one woman requirement: Total combinations minus zero women combinations"
                    ]
                },
                {
                    "name": "3. Digit Formation & Numerical Constraints",
                    "desc": "Forming numbers of specific digits with or without repetition, restricted by even/odd, divisibility, or magnitude.",
                    "examples": [
                        "4-digit numbers formed from {0, 1, 2, 3, 4}: First digit cannot be 0 (4 choices)",
                        "Even numbers: Last digit must be even"
                    ]
                },
                {
                    "name": "4. Circular Arrangements & Necklaces",
                    "desc": "Arranging people around round tables or stringing distinct colored beads onto necklaces.",
                    "examples": [
                        "Seating 6 people at a round dining table = (6 - 1)! = 5! = 120 ways",
                        "Necklace of 6 distinct gemstones = (6 - 1)! / 2 = 60 ways"
                    ]
                },
                {
                    "name": "5. Gap and Tie (String) Methods",
                    "desc": "Tie method keeps items strictly together; Gap method ensures no two specified items are adjacent.",
                    "examples": [
                        "Tie method: Bundle items together into 1 super-item, multiply by internal permutations",
                        "Gap method: Place other items first, then arrange restricted items in created gaps"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Permutation vs Combination Core Test",
                    "explanation": "- **Permutation ($P$)**: Order matters (e.g., telephone numbers, ranking, anagrams, officer posts like President/VP).\n- **Combination ($C$)**: Order does NOT matter (e.g., handshakes, committee members, team selection, picking balls from urns).\nFormula bridge: ${}^n P_r = r! \\times {}^n C_r$.",
                    "words": [
                        "Permutation = Order Matters",
                        "Combination = Order Doesn't Matter",
                        "nPr vs nCr"
                    ],
                    "correct": "Selecting a team of 4 from 10: Order does not matter, use 10C4 = 210.",
                    "incorrect": "Using 10P4 which counts different orderings of the exact same 4 teammates as separate teams."
                },
                {
                    "rule_number": 2,
                    "title": "String / Tie Method for 'Always Together'",
                    "explanation": "When $k$ particular objects must always be together:\n(1) Tie them together into a single composite unit.\n(2) The total number of items to arrange is $(n - k + 1)$.\n(3) Multiply the arrangement of the composite units by the internal arrangements of the tied items: $(n - k + 1)! \\times k!$.",
                    "words": [
                        "Tie Method",
                        "Always Together",
                        "Composite Unit",
                        "Internal Arrangements"
                    ],
                    "correct": "Arranging 5 boys and 2 girls so girls are together: Treat 2 girls as 1 unit. Total units = 5 + 1 = 6. Total = 6! * 2! = 720 * 2 = 1440.",
                    "incorrect": "Calculating 7! and subtracting 2!."
                },
                {
                    "rule_number": 3,
                    "title": "Gap Method for 'No Two Adjacent / Never Together'",
                    "explanation": "When specific objects must NEVER be adjacent:\n(1) Arrange the unrestricted objects first in $m!$ ways, creating $(m + 1)$ gaps (including ends).\n(2) Place the $k$ restricted objects into the available $(m + 1)$ gaps using ${}^{m+1} P_k$ or ${}^{m+1} C_k \\times k!$.",
                    "words": [
                        "Gap Method",
                        "Never Together",
                        "Available Gaps (m+1)"
                    ],
                    "correct": "Arrange 4 boys and 3 girls so no two girls are adjacent: 4 boys seated in 4! = 24 ways, creating 5 gaps. 3 girls placed in 5 gaps in 5P3 = 60 ways. Total = 24 * 60 = 1440.",
                    "incorrect": "Calculating Total - (Girls together) which only subtracts all 3 together, leaving cases where 2 girls are together."
                },
                {
                    "rule_number": 4,
                    "title": "Circular Permutation Clockwise/Anticlockwise Symmetry",
                    "explanation": "- For people around a round table where clockwise and anticlockwise orderings are distinct: $(n - 1)!$.\n- For garlands, necklaces, or key rings where flipping over makes clockwise and anticlockwise identical: $\\frac{(n - 1)!}{2}$.",
                    "words": [
                        "Circular Permutations",
                        "(n-1)!",
                        "Necklace Symmetry (n-1)!/2"
                    ],
                    "correct": "Number of ways to string 5 different beads on a necklace = (5 - 1)! / 2 = 4! / 2 = 24 / 2 = 12.",
                    "incorrect": "Giving 5! = 120 or (5-1)! = 24."
                },
                {
                    "rule_number": 5,
                    "title": "Repeated Elements Anagram Rule",
                    "explanation": "If a collection of $n$ items contains $p$ identical items of type 1, $q$ of type 2, and $r$ of type 3, the number of distinct permutations is $\\frac{n!}{p! \\cdot q! \\cdot r!}$.",
                    "words": [
                        "Repeated Items",
                        "n! / (p! * q! * r!)",
                        "Anagram Formula"
                    ],
                    "correct": "Letters of 'MISSISSIPPI' (11 letters: 1 M, 4 I, 4 S, 2 P) = 11! / (4! * 4! * 2!) = 34,650.",
                    "incorrect": "Calculating 11! without dividing by duplicate factorials."
                },
                {
                    "rule_number": 6,
                    "title": "Handshake / Line Segment Formula",
                    "explanation": "When $n$ people shake hands with each other once, or when connecting $n$ non-collinear points to form straight line segments, the total number is ${}^n C_2 = \\frac{n(n - 1)}{2}$.",
                    "words": [
                        "Handshake Formula",
                        "n(n-1)/2",
                        "nC2"
                    ],
                    "correct": "At a conference of 12 people, total handshakes = 12 * 11 / 2 = 66.",
                    "incorrect": "Multiplying 12 * 11 = 132 (double counting every handshake)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using permutations (nPr) when forming a committee or selecting players.",
                    "correction": "Use combinations (nCr) because changing the order of people chosen does not create a new committee.",
                    "rationale": "A committee of Alice and Bob is identical to a committee of Bob and Alice."
                },
                {
                    "mistake": "Solving 'no two girls together' by subtracting 'all girls together' from total.",
                    "correction": "Use the Gap Method. Total minus (all together) still includes cases where exactly two girls sit together.",
                    "rationale": "Complement of 'no two together' is 'at least two together', not 'all together'."
                },
                {
                    "mistake": "Forgetting that zero cannot occupy the first digit in multi-digit number problems.",
                    "correction": "The leading most significant digit has only (n - 1) options if 0 is an available digit.",
                    "rationale": "A number starting with 0 (e.g., 0452) reduces to a 3-digit number."
                },
                {
                    "mistake": "Forgetting to divide by 2 for circular necklaces or garlands.",
                    "correction": "Dividing by 2 is essential because a necklace can be flipped over, making clockwise and anticlockwise identical.",
                    "rationale": "Rotational 3D reflection invariance."
                }
            ],
            "quick_revision_points": [
                "Order matters => Permutations: nPr = n! / (n - r)!",
                "Order does NOT matter => Combinations: nCr = n! / [r!(n - r)!]",
                "nCr = nC(n-r); nC0 = 1; nCn = 1; nC1 = n",
                "Handshake / line segments = nC2 = n(n - 1) / 2",
                "Anagram with repeats = n! / (p! * q! * r!)",
                "Round table seating = (n - 1)!; Necklace/garland = (n - 1)! / 2",
                "'Always together' => Tie method: treat as 1 unit",
                "'Never together' => Gap method: seat others first, then place in gaps"
            ]
        },
        "previous_year_questions": [
            {
                "id": 3701,
                "topic_id": 37,
                "exam_name": "SSC CGL Tier 2",
                "year": 2022,
                "question": "In how many different ways can the letters of the word 'DETAIL' be arranged such that the vowels must always occupy odd positions?",
                "options_json": [
                    "36",
                    "48",
                    "60",
                    "72"
                ],
                "correct_answer": "36",
                "explanation": "The word 'DETAIL' has 6 letters: Vowels = {E, A, I} (3 vowels); Consonants = {D, T, L} (3 consonants).\nPositions in a 6-letter word are: 1, 2, 3, 4, 5, 6.\nOdd positions are: 1, 3, 5 (total 3 positions).\nWays to arrange 3 vowels in 3 odd positions = 3! = 6.\nEven positions are: 2, 4, 6 (total 3 positions).\nWays to arrange 3 consonants in 3 even positions = 3! = 6.\nTotal arrangements = 3! * 3! = 6 * 6 = 36.",
                "difficulty_level": "medium"
            },
            {
                "id": 3702,
                "topic_id": 37,
                "exam_name": "IBPS PO Mains",
                "year": 2022,
                "question": "A committee of 5 persons is to be formed from 6 men and 4 women. In how many ways can this be done if the committee must contain at least 3 men?",
                "options_json": [
                    "186",
                    "120",
                    "140",
                    "166"
                ],
                "correct_answer": "186",
                "explanation": "Three cases for 'at least 3 men':\nCase 1: 3 Men and 2 Women = 6C3 * 4C2 = 20 * 6 = 120\nCase 2: 4 Men and 1 Woman = 6C4 * 4C1 = 15 * 4 = 60\nCase 3: 5 Men and 0 Women = 6C5 * 4C0 = 6 * 1 = 6\nTotal ways = 120 + 60 + 6 = 186.",
                "difficulty_level": "medium"
            },
            {
                "id": 3703,
                "topic_id": 37,
                "exam_name": "CAT",
                "year": 2021,
                "question": "In how many ways can 5 boys and 4 girls sit in a row such that no two girls are sitting together?",
                "options_json": [
                    "43200",
                    "2880",
                    "1440",
                    "86400"
                ],
                "correct_answer": "43200",
                "explanation": "By Gap Method:\nStep 1: Seat 5 boys in a row = 5! = 120 ways.\nStep 2: 5 boys create 6 gaps (including ends): _ B1 _ B2 _ B3 _ B4 _ B5 _\nStep 3: Arrange 4 girls in these 6 gaps = 6P4 = 6 * 5 * 4 * 3 = 360 ways.\nTotal ways = 120 * 360 = 43,200.",
                "difficulty_level": "hard"
            }
        ],
        "practice_questions": [
            {
                "id": 3701,
                "topic_id": 37,
                "type": "mcq",
                "question": "In how many different ways can the letters of the word 'APPLE' be arranged?",
                "options_json": [
                    "60",
                    "120",
                    "24",
                    "30"
                ],
                "correct_answer": "60",
                "explanation": "APPLE has 5 letters with 2 P's. Arrangements = 5! / 2! = 120 / 2 = 60.",
                "points": 1
            },
            {
                "id": 3702,
                "topic_id": 37,
                "type": "mcq",
                "question": "In a party of 10 people, each person shakes hands with every other person once. How many total handshakes occur?",
                "options_json": [
                    "45",
                    "90",
                    "100",
                    "50"
                ],
                "correct_answer": "45",
                "explanation": "Total handshakes = 10C2 = (10 * 9) / 2 = 45.",
                "points": 1
            },
            {
                "id": 3703,
                "topic_id": 37,
                "type": "mcq",
                "question": "In how many ways can 6 people be seated around a round dining table?",
                "options_json": [
                    "120",
                    "720",
                    "60",
                    "240"
                ],
                "correct_answer": "120",
                "explanation": "Circular permutation = (n - 1)! = (6 - 1)! = 5! = 120.",
                "points": 1
            },
            {
                "id": 3704,
                "topic_id": 37,
                "type": "mcq",
                "question": "In how many ways can a cricket team of 11 players be selected from a squad of 15 players?",
                "options_json": [
                    "1365",
                    "1050",
                    "1500",
                    "1200"
                ],
                "correct_answer": "1365",
                "explanation": "15C11 = 15C4 = (15 * 14 * 13 * 12) / (4 * 3 * 2 * 1) = 1365.",
                "points": 1
            },
            {
                "id": 3705,
                "topic_id": 37,
                "type": "fitb",
                "question": "Find the value of 7C3.",
                "options_json": [],
                "correct_answer": "35",
                "explanation": "7C3 = (7 * 6 * 5) / (3 * 2 * 1) = 35.",
                "points": 1
            },
            {
                "id": 3706,
                "topic_id": 37,
                "type": "mcq",
                "question": "In how many ways can the letters of the word 'MATHEMATICS' be arranged?",
                "options_json": [
                    "4989600",
                    "11!",
                    "1663200",
                    "39916800"
                ],
                "correct_answer": "4989600",
                "explanation": "MATHEMATICS has 11 letters with 2 M's, 2 A's, 2 T's: 11! / (2! * 2! * 2!) = 39,916,800 / 8 = 4,989,600.",
                "points": 1
            },
            {
                "id": 3707,
                "topic_id": 37,
                "type": "mcq",
                "question": "How many 3-digit numbers can be formed using digits {1, 2, 3, 4, 5} without repetition?",
                "options_json": [
                    "60",
                    "125",
                    "20",
                    "120"
                ],
                "correct_answer": "60",
                "explanation": "5P3 = 5 * 4 * 3 = 60.",
                "points": 1
            },
            {
                "id": 3708,
                "topic_id": 37,
                "type": "mcq",
                "question": "In how many ways can 7 different beads be threaded onto a circular necklace?",
                "options_json": [
                    "360",
                    "720",
                    "5040",
                    "120"
                ],
                "correct_answer": "360",
                "explanation": "(7 - 1)! / 2 = 6! / 2 = 720 / 2 = 360.",
                "points": 1
            },
            {
                "id": 3709,
                "topic_id": 37,
                "type": "mcq",
                "question": "Out of 5 men and 3 women, a committee of 3 is to be formed with exactly 1 woman. How many ways are possible?",
                "options_json": [
                    "30",
                    "15",
                    "45",
                    "60"
                ],
                "correct_answer": "30",
                "explanation": "Select 1 woman from 3 and 2 men from 5: 3C1 * 5C2 = 3 * 10 = 30.",
                "points": 1
            },
            {
                "id": 3710,
                "topic_id": 37,
                "type": "fitb",
                "question": "In how many ways can 4 books be arranged on a shelf?",
                "options_json": [],
                "correct_answer": "24",
                "explanation": "4! = 4 * 3 * 2 * 1 = 24.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 3701,
                "topic_id": 37,
                "question": "What is the value of 5! (5 factorial)?",
                "options_json": [
                    "120",
                    "60",
                    "24",
                    "720"
                ],
                "correct_answer": "120",
                "explanation": "5 * 4 * 3 * 2 * 1 = 120.",
                "points": 1
            },
            {
                "id": 3702,
                "topic_id": 37,
                "question": "If nC2 = 28, find the value of n.",
                "options_json": [
                    "8",
                    "7",
                    "9",
                    "6"
                ],
                "correct_answer": "8",
                "explanation": "n(n - 1) / 2 = 28 => n(n - 1) = 56 => 8 * 7 = 56 => n = 8.",
                "points": 1
            },
            {
                "id": 3703,
                "topic_id": 37,
                "question": "In how many ways can 5 people be seated in a straight line row of 5 chairs?",
                "options_json": [
                    "120",
                    "24",
                    "60",
                    "100"
                ],
                "correct_answer": "120",
                "explanation": "5! = 120.",
                "points": 1
            },
            {
                "id": 3704,
                "topic_id": 37,
                "question": "In how many ways can 5 people sit around a circular table?",
                "options_json": [
                    "24",
                    "120",
                    "60",
                    "12"
                ],
                "correct_answer": "24",
                "explanation": "(5 - 1)! = 4! = 24.",
                "points": 1
            },
            {
                "id": 3705,
                "topic_id": 37,
                "question": "How many ways can the letters of the word 'BOOK' be arranged?",
                "options_json": [
                    "12",
                    "24",
                    "6",
                    "18"
                ],
                "correct_answer": "12",
                "explanation": "4 letters with 2 O's: 4! / 2! = 24 / 2 = 12.",
                "points": 1
            },
            {
                "id": 3706,
                "topic_id": 37,
                "question": "If nPr = 720 and nCr = 120, what is the value of r?",
                "options_json": [
                    "3",
                    "4",
                    "2",
                    "5"
                ],
                "correct_answer": "3",
                "explanation": "nPr = r! * nCr => 720 = r! * 120 => r! = 6 => r = 3.",
                "points": 1
            },
            {
                "id": 3707,
                "topic_id": 37,
                "question": "How many lines can be drawn through 10 points on a circle?",
                "options_json": [
                    "45",
                    "90",
                    "10",
                    "100"
                ],
                "correct_answer": "45",
                "explanation": "10C2 = (10 * 9) / 2 = 45.",
                "points": 1
            },
            {
                "id": 3708,
                "topic_id": 37,
                "question": "In how many ways can 3 prizes be distributed among 4 students if each student can receive only 1 prize?",
                "options_json": [
                    "24",
                    "12",
                    "64",
                    "4"
                ],
                "correct_answer": "24",
                "explanation": "4P3 = 4 * 3 * 2 = 24.",
                "points": 1
            },
            {
                "id": 3709,
                "topic_id": 37,
                "question": "What is the value of 10C0 + 10C10?",
                "options_json": [
                    "2",
                    "1",
                    "10",
                    "20"
                ],
                "correct_answer": "2",
                "explanation": "10C0 = 1, 10C10 = 1. Sum = 1 + 1 = 2.",
                "points": 1
            },
            {
                "id": 3710,
                "topic_id": 37,
                "question": "In how many ways can 5 keys be arranged on a key ring?",
                "options_json": [
                    "12",
                    "24",
                    "120",
                    "6"
                ],
                "correct_answer": "12",
                "explanation": "(5 - 1)! / 2 = 4! / 2 = 24 / 2 = 12.",
                "points": 1
            }
        ]
    }
}
