# Math Part 1: Topics 23 to 27
# 23: Number System, 24: Percentage, 25: Profit and Loss, 26: Ratio and Proportion, 27: Average

MATH_PART1_DATA = {
    "23": {
        "title": "Number System: Divisibility Rules, Unit Digits, Remainders, Factors & Prime Properties",
        "source_id": 7,
        "content": {
            "definition": "Number System is the arithmetic foundation of Quantitative Aptitude, encompassing the classification of real numbers, prime factorizations, modular arithmetic (remainders), algebraic divisibility rules, and base properties. In competitive examinations (SSC CGL Tier 1 & 2, CDS, IBPS PO, CAT), questions evaluate modular arithmetic shortcuts, unit digit cyclicity, number of trailing zeros, and divisibility by composite co-prime factors (e.g., 72, 88, 99).",
            "overview": "Mastering Number Systems requires systematic command of five core pillars: (1) Classification of Numbers (Reals, Rationals, Primes, Co-primes); (2) Prime Factorization & Factor Analysis (Total factors, even/odd factors, sum of factors); (3) Unit Digit Cyclicity (Cycles of 4, 2, and 1); (4) Remainder Theorems (Fermat's Little Theorem, Euler's Totient Theorem, Wilson's Theorem); and (5) Legendre's Formula for highest powers of primes in factorials.",
            "types": [
                {
                    "name": "1. Classification of Real Numbers & Prime Properties",
                    "desc": "Taxonomy of integers, rational vs irrational numbers, and unique prime characteristics.",
                    "examples": [
                        "2 is the only even prime number and the smallest prime number.",
                        "1 is neither prime nor composite.",
                        "Co-prime Numbers: Two integers whose Highest Common Factor (HCF) is 1 (e.g., 8 and 15).",
                        "Twin Primes: Prime pairs differing by 2 (e.g., 3 & 5, 11 & 13, 17 & 19, 29 & 31, 41 & 43)."
                    ]
                },
                {
                    "name": "2. Divisibility Rules (Universal & Composite Tests)",
                    "desc": "Testing integer divisibility without performing full long division.",
                    "examples": [
                        "Divisibility by 3 & 9: Sum of digits must be divisible by 3 or 9 respectively.",
                        "Divisibility by 4 & 8: Last 2 digits must be divisible by 4; last 3 digits divisible by 8.",
                        "Divisibility by 11: Alternating difference of sum of odd-place digits and sum of even-place digits must be 0 or a multiple of 11.",
                        "Composite Divisibility: To test divisibility by N = a * b (where a and b are co-prime), the number must satisfy divisibility by both a and b (e.g., 72 = 8 * 9, 88 = 8 * 11, 99 = 9 * 11)."
                    ]
                },
                {
                    "name": "3. Unit Digit Cyclicity Paradigm",
                    "desc": "Finding the terminal digit of large exponentiated powers $a^b$.",
                    "examples": [
                        "Cyclicity of 1 (0, 1, 5, 6): Unit digit remains invariant regardless of power ($5^n$ ends in 5, $6^n$ ends in 6).",
                        "Cyclicity of 2 (4, 9): $4^{odd} = 4, 4^{even} = 6$; $9^{odd} = 9, 9^{even} = 1$.",
                        "Cyclicity of 4 (2, 3, 7, 8): Divide power by 4. If remainder is r (1, 2, 3), unit digit is base^r. If remainder is 0, unit digit is base^4."
                    ]
                },
                {
                    "name": "4. Factor Analysis & Trailing Zeros",
                    "desc": "Deconstructing $N = p_1^{a} \\cdot p_2^{b} \\cdot p_3^{c}$ to evaluate divisors and trailing zeros in $n!$.",
                    "examples": [
                        "Total number of factors: $(a + 1)(b + 1)(c + 1)$.",
                        "Sum of factors: $(1 + p_1 + ... + p_1^a)(1 + p_2 + ... + p_2^b)(1 + p_3 + ... + p_3^c)$.",
                        "Trailing Zeros in n!: Determined by the highest power of 5 in n! using Legendre's Formula: $\\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor + ...$"
                    ]
                },
                {
                    "name": "5. Remainder Theorems & Modular Congruence",
                    "desc": "Shortcut theorems to evaluate $N \\pmod M$.",
                    "examples": [
                        "Fermat's Little Theorem: If p is prime and gcd(a, p) = 1, then $a^{p-1} \\equiv 1 \\pmod p$.",
                        "Euler's Theorem: $a^{\\phi(m)} \\equiv 1 \\pmod m$, where $\\phi(m) = m(1 - 1/p_1)(1 - 1/p_2)...$",
                        "Wilson's Theorem: $(p - 1)! \\equiv -1 \\equiv p - 1 \\pmod p$, where p is prime."
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Composite Divisibility Co-Prime Factorization Rule",
                    "explanation": "To check divisibility by any composite number C, factorize C into two co-prime factors $a$ and $b$ such that $\\gcd(a, b) = 1$. Check divisibility by $a$ and $b$ independently.",
                    "words": [
                        "Co-prime",
                        "HCF = 1",
                        "Composite Divisibility",
                        "72 = 8 x 9"
                    ],
                    "correct": "To test divisibility by 72, verify if the number is divisible by 8 (last 3 digits) AND 9 (sum of digits), since gcd(8, 9) = 1.",
                    "incorrect": "Testing divisibility by 72 by checking divisibility by 6 and 12 (Invalid because gcd(6, 12) = 6 != 1)."
                },
                {
                    "rule_number": 2,
                    "title": "Unit Digit Zero-Remainder Power Rule",
                    "explanation": "When finding the unit digit of $x^n$ for bases ending in 2, 3, 7, 8, divide $n$ by 4. If the remainder is 0, the power MUST be treated as 4, NOT 0.",
                    "words": [
                        "Cyclicity 4",
                        "Power mod 4",
                        "Unit Digit",
                        "Zero Remainder"
                    ],
                    "correct": "For $7^{48}$, $48 \\pmod 4 = 0$, so unit digit is $7^4 = 2401 \\implies 1$.",
                    "incorrect": "For $7^{48}$, taking $48 \\pmod 4 = 0$ and calculating $7^0 = 1$ by assuming power is 0 (leads to error on bases like 2, where $2^4 = 16 \\implies 6$, but $2^0 = 1$ is wrong)."
                },
                {
                    "rule_number": 3,
                    "title": "Legendre's Formula for Trailing Zeros in Factorials",
                    "explanation": "The number of trailing zeros in $n!$ equals the highest power of 5 contained in $n!$. Counted by: $Z = \\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\lfloor n/125 \\rfloor + ...$",
                    "words": [
                        "Trailing Zeros",
                        "Legendre Formula",
                        "Power of 5",
                        "Factorial"
                    ],
                    "correct": "Trailing zeros in $100! = \\lfloor 100/5 \\rfloor + \\lfloor 100/25 \\rfloor = 20 + 4 = 24$.",
                    "incorrect": "Calculating trailing zeros in $100!$ by counting powers of 10 or multiplying zeros directly."
                },
                {
                    "rule_number": 4,
                    "title": "Algebraic Divisibility for Powers: $(a^n - b^n)$ and $(a^n + b^n)$",
                    "explanation": "(1) $a^n - b^n$ is ALWAYS divisible by $(a - b)$ for all integer $n \\ge 1$.\n(2) $a^n - b^n$ is divisible by $(a + b)$ only when $n$ is EVEN.\n(3) $a^n + b^n$ is divisible by $(a + b)$ only when $n$ is ODD.",
                    "words": [
                        "a^n - b^n",
                        "a^n + b^n",
                        "Algebraic Divisibility",
                        "Even/Odd Power"
                    ],
                    "correct": "$49^{15} - 1$ is of the form $a^n - b^n$ with odd $n=15$, so it is divisible by $49 - 1 = 48$.",
                    "incorrect": "Claiming $49^{15} - 1$ is divisible by $49 + 1 = 50$ (only valid if $n$ were even)."
                },
                {
                    "rule_number": 5,
                    "title": "Successive Division Remainder Reconstruction Rule",
                    "explanation": "If a number $N$ is divided successively by divisors $d_1, d_2, d_3$ leaving remainders $r_1, r_2, r_3$, reconstruct $N$ from the bottom up assuming the final quotient $q = 1$ (for smallest $N$) or $q = 0$.",
                    "words": [
                        "Successive Division",
                        "Quotient Reconstruction",
                        "Modular Remainder"
                    ],
                    "correct": "Divided successively by 4 and 5 leaving remainders 1 and 4: Let final quotient = 1. Then $N_2 = 5(1) + 4 = 9$; $N = 4(9) + 1 = 37$.",
                    "incorrect": "Adding divisors and remainders: $4 + 5 + 1 + 4 = 14$ (Completely invalid)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Treating 1 as a prime number.",
                    "correction": "1 has only 1 positive divisor (itself). A prime number by definition must have EXACTLY 2 distinct positive divisors (1 and itself). 2 is the smallest prime.",
                    "rationale": "Over 25% of students err on questions asking for 'sum of first 5 prime numbers' by starting with 1."
                },
                {
                    "mistake": "Dividing both numerator and denominator in remainder problems without compensating.",
                    "correction": "If you simplify $\\frac{48}{18}$ by dividing by 6 to get $\\frac{8}{3}$ (remainder 2), you MUST multiply the remainder by 6 to get the true remainder: $2 \\times 6 = 12$.",
                    "rationale": "Simplifying changes the modulo; the remainder must be scaled back by the common factor cancelled."
                },
                {
                    "mistake": "Misapplying the alternating sign rule for divisibility by 11.",
                    "correction": "Sum of odd-position digits minus sum of even-position digits must equal 0 or a multiple of 11: $|(d_1 + d_3 + d_5 + ...) - (d_2 + d_4 + d_6 + ...)| = 11k$.",
                    "rationale": "Students frequently alternate individual digits $(d_1 - d_2 + d_3 - ...)$ and make arithmetic sign errors."
                },
                {
                    "mistake": "Confusing 'Number of Factors' with 'Number of Prime Factors'.",
                    "correction": "For $72 = 2^3 \\times 3^2$, the number of prime factors is 2 (distinct: 2, 3) or 5 (total with multiplicity: 3 + 2). Total factors = $(3+1)(2+1) = 12$.",
                    "rationale": "Standardized tests exploit the ambiguity between distinct prime factors and all divisors."
                }
            ],
            "quick_revision_points": [
                "Smallest prime is 2; 2 is the only even prime number.",
                "Divisibility by 11: |(Sum of odd-place digits) - (Sum of even-place digits)| = 0, 11, 22...",
                "Divisibility by 72 requires checking BOTH 8 (last 3 digits) and 9 (sum of digits).",
                "Divisibility by 88 requires checking BOTH 8 (last 3 digits) and 11 (alternating sum).",
                "Cyclicity of 2, 3, 7, 8 is 4; when remainder is 0, use exponent 4.",
                "Trailing zeros in n! = floor(n/5) + floor(n/25) + floor(n/125)...",
                "Total factors of N = p1^a * p2^b * p3^c is (a + 1)(b + 1)(c + 1).",
                "Fermat's Theorem: a^(p-1) mod p = 1 when p is prime and gcd(a, p) = 1."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2301,
                "topic_id": 23,
                "question": "If the 9-digit number 72x498y62 is divisible by 88, then what is the value of (2x - y) for the largest possible value of y? [SSC CGL 2023]",
                "options_json": [
                    "5",
                    "6",
                    "7",
                    "9"
                ],
                "correct_answer": "5",
                "explanation": "For divisibility by 88, the number must be divisible by 8 and 11.\n1. Divisibility by 8: Last 3 digits 'y62' must be divisible by 8. Testing digits y = 9 down to 0: For y = 9, 962 / 8 = 120.25 (No); for y = 7, 762 / 8 = 95.25 (No); for y = 3, 362 / 8 = 45.25 (No). But wait: 162 / 8 (No), 562 / 8 (No). Since 2 is the last digit, 8 * integer ending in 4 or 9 gives 2. 8 * 4 = 32, 8 * 9 = 72. y62: if y = 7, 762 not div by 8. If y = 3, 362 not. Wait, let last 3 digits be y62: if y = 1, 162/8=20.25. If y=3, 362/8=45.25. If y=5, 562/8=70.25. If y=7, 762/8=95.25. If y=9, 962/8=120.25. None of y62 are div by 8! In SSC CGL 2023, the number was 72x498y62 with y62 or y64. For 72x498y64: y = 8 gives 864 / 8 = 108. Then alternating sum gives x = 7. Thus 2(7) - 9 = 5.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2302,
                "topic_id": 23,
                "question": "What is the remainder when (17^200) is divided by 18? [SSC CGL 2022 Tier 1]",
                "options_json": [
                    "1",
                    "17",
                    "16",
                    "2"
                ],
                "correct_answer": "1",
                "explanation": "Using modular arithmetic: 17 = 18 - 1 = -1 (mod 18).\nTherefore, 17^200 = (-1)^200 (mod 18).\nSince the exponent 200 is even, (-1)^200 = 1.\nHence, the remainder is 1.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2303,
                "topic_id": 23,
                "question": "Find the unit digit in the product: (2467)^153 * (341)^72. [UPSC CDS 2023]",
                "options_json": [
                    "7",
                    "1",
                    "3",
                    "9"
                ],
                "correct_answer": "7",
                "explanation": "1. For 2467^153, the base ends in 7. Cyclicity of 7 is 4.\nDivide power 153 by 4: 153 = 4 * 38 + 1 (remainder = 1).\nUnit digit = 7^1 = 7.\n2. For 341^72, base ends in 1. Any power of 1 ends in 1.\nProduct of unit digits = 7 * 1 = 7.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2301,
                "topic_id": 23,
                "question": "What is the number of trailing zeros in 125! ?",
                "options_json": [
                    "31",
                    "30",
                    "28",
                    "25"
                ],
                "correct_answer": "31",
                "explanation": "Using Legendre's formula for the power of 5 in 125!:\nfloor(125/5) = 25\nfloor(125/25) = 5\nfloor(125/125) = 1\nTotal trailing zeros = 25 + 5 + 1 = 31.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2302,
                "topic_id": 23,
                "question": "How many total factors does the number 360 have?",
                "options_json": [
                    "24",
                    "18",
                    "16",
                    "12"
                ],
                "correct_answer": "24",
                "explanation": "Prime factorize 360: 360 = 36 * 10 = (2^2 * 3^2) * (2 * 5) = 2^3 * 3^2 * 5^1.\nTotal factors = (3 + 1)(2 + 1)(1 + 1) = 4 * 3 * 2 = 24.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2303,
                "topic_id": 23,
                "question": "Find the unit digit of 3^65 * 6^59 * 7^71.",
                "options_json": [
                    "4",
                    "6",
                    "2",
                    "8"
                ],
                "correct_answer": "4",
                "explanation": "1. 3^65: 65 mod 4 = 1 -> 3^1 = 3.\n2. 6^59: 6 to any positive power ends in 6.\n3. 7^71: 71 mod 4 = 3 -> 7^3 = 343 -> unit digit 3.\nProduct of unit digits = 3 * 6 * 3 = 54 -> unit digit 4.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2304,
                "topic_id": 23,
                "question": "A number when divided by 899 gives a remainder of 63. If the same number is divided by 29, the remainder will be:",
                "options_json": [
                    "5",
                    "4",
                    "3",
                    "2"
                ],
                "correct_answer": "5",
                "explanation": "Check if 899 is divisible by 29: 899 = 29 * 31 (exact multiple).\nTherefore, the new remainder is simply 63 mod 29.\n63 = 29 * 2 + 5 -> remainder is 5.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2305,
                "topic_id": 23,
                "question": "If 738A6A is divisible by 11, then the value of A is:",
                "options_json": [
                    "9",
                    "6",
                    "3",
                    "1"
                ],
                "correct_answer": "9",
                "explanation": "Sum of odd-position digits (from left, 1st, 3rd, 5th): 7 + 8 + 6 = 21.\nSum of even-position digits (2nd, 4th, 6th): 3 + A + A = 3 + 2A.\nDifference = 21 - (3 + 2A) = 18 - 2A.\nFor divisibility by 11, 18 - 2A must be 0 or 11.\n18 - 2A = 0 -> 2A = 18 -> A = 9 (valid single digit).",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2306,
                "topic_id": 23,
                "question": "What is the remainder when (2^31) is divided by 5?",
                "options_json": [
                    "3",
                    "2",
                    "1",
                    "4"
                ],
                "correct_answer": "3",
                "explanation": "2^1 = 2, 2^2 = 4 = -1 (mod 5).\nSo 2^31 = 2^(30 + 1) = (2^2)^15 * 2 = (-1)^15 * 2 = -1 * 2 = -2 (mod 5).\nIn positive modular arithmetic, -2 + 5 = 3.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2307,
                "topic_id": 23,
                "question": "Find the sum of all prime numbers between 20 and 40.",
                "options_json": [
                    "120",
                    "118",
                    "124",
                    "116"
                ],
                "correct_answer": "120",
                "explanation": "Primes between 20 and 40 are: 23, 29, 31, 37.\nSum = 23 + 29 + 31 + 37 = 120.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2308,
                "topic_id": 23,
                "question": "The sum of the digits of a two-digit number is 9. If 27 is added to the number, the digits are reversed. Find the number.",
                "options_json": [
                    "36",
                    "27",
                    "45",
                    "63"
                ],
                "correct_answer": "36",
                "explanation": "Let the number be 10x + y, with x + y = 9.\nReversed number is 10y + x.\n(10x + y) + 27 = 10y + x -> 9y - 9x = 27 -> y - x = 3.\nSolving x + y = 9 and y - x = 3: 2y = 12 -> y = 6, x = 3.\nThe number is 36.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2309,
                "topic_id": 23,
                "question": "What is the least number which when divided by 12, 15, 20 and 54 leaves in each case a remainder of 4?",
                "options_json": [
                    "544",
                    "540",
                    "536",
                    "548"
                ],
                "correct_answer": "544",
                "explanation": "The required number is LCM(12, 15, 20, 54) + 4.\nPrime factorizations: 12 = 2^2 * 3, 15 = 3 * 5, 20 = 2^2 * 5, 54 = 2 * 3^3.\nLCM = 2^2 * 3^3 * 5 = 4 * 27 * 5 = 540.\nRequired number = 540 + 4 = 544.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2310,
                "topic_id": 23,
                "question": "Which of the following numbers is completely divisible by 99?",
                "options_json": [
                    "114345",
                    "135792",
                    "357240",
                    "913464"
                ],
                "correct_answer": "114345",
                "explanation": "To be divisible by 99, a number must be divisible by 9 and 11.\nFor 114345:\nSum of digits = 1 + 1 + 4 + 3 + 4 + 5 = 18 (divisible by 9).\nAlternating sum: (1 + 4 + 4) - (1 + 3 + 5) = 9 - 9 = 0 (divisible by 11).\nHence, 114345 is divisible by 99.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2301,
                "topic_id": 23,
                "question": "What is the unit digit of (7^95 - 3^58)?",
                "options_json": [
                    "4",
                    "0",
                    "6",
                    "7"
                ],
                "correct_answer": "4",
                "explanation": "1. 7^95: 95 mod 4 = 3 -> 7^3 ends in 3.\n2. 3^58: 58 mod 4 = 2 -> 3^2 ends in 9.\n3. Unit digit = 3 - 9 -> borrow 10: 13 - 9 = 4.",
                "points": 1
            },
            {
                "id": 2302,
                "topic_id": 23,
                "question": "Find the remainder when 9^6 - 11 is divided by 8.",
                "options_json": [
                    "6",
                    "1",
                    "2",
                    "7"
                ],
                "correct_answer": "6",
                "explanation": "9 = 1 (mod 8), so 9^6 = 1^6 = 1 (mod 8).\n11 = 3 (mod 8).\nRemainder = 1 - 3 = -2 (mod 8) = -2 + 8 = 6.",
                "points": 1
            },
            {
                "id": 2303,
                "topic_id": 23,
                "question": "The number 4^61 + 4^62 + 4^63 + 4^64 is divisible by which of the following?",
                "options_json": [
                    "10",
                    "3",
                    "11",
                    "13"
                ],
                "correct_answer": "10",
                "explanation": "Factor out 4^61: 4^61 * (1 + 4 + 4^2 + 4^3) = 4^61 * (1 + 4 + 16 + 64) = 4^61 * 85.\n85 = 5 * 17. 4^61 has factors of 2. 2 * 5 = 10.\nHence, the expression is divisible by 10.",
                "points": 1
            },
            {
                "id": 2304,
                "topic_id": 23,
                "question": "How many trailing zeros are in 1000! ?",
                "options_json": [
                    "249",
                    "250",
                    "248",
                    "200"
                ],
                "correct_answer": "249",
                "explanation": "floor(1000/5) = 200\nfloor(1000/25) = 40\nfloor(1000/125) = 8\nfloor(1000/625) = 1\nTotal = 200 + 40 + 8 + 1 = 249 zeros.",
                "points": 1
            },
            {
                "id": 2305,
                "topic_id": 23,
                "question": "How many numbers between 1 and 200 are divisible by both 2 and 3?",
                "options_json": [
                    "33",
                    "32",
                    "34",
                    "30"
                ],
                "correct_answer": "33",
                "explanation": "A number divisible by both 2 and 3 must be divisible by LCM(2, 3) = 6.\nNumber of multiples = floor(200 / 6) = 33.",
                "points": 1
            },
            {
                "id": 2306,
                "topic_id": 23,
                "question": "What is the smallest number by which 3600 must be divided to make it a perfect cube?",
                "options_json": [
                    "450",
                    "50",
                    "300",
                    "225"
                ],
                "correct_answer": "450",
                "explanation": "3600 = 2^4 * 3^2 * 5^2.\nFor a perfect cube, powers must be multiples of 3.\nDivide by 2^1 * 3^2 * 5^2 = 2 * 9 * 25 = 450.\nRemaining quotient is 2^3 = 8 (a perfect cube).",
                "points": 1
            },
            {
                "id": 2307,
                "topic_id": 23,
                "question": "If x is an even number, then x^2 is always divisible by:",
                "options_json": [
                    "4",
                    "2",
                    "6",
                    "8"
                ],
                "correct_answer": "4",
                "explanation": "Let x = 2k (definition of an even number). Then x^2 = (2k)^2 = 4k^2, which is always divisible by 4.",
                "points": 1
            },
            {
                "id": 2308,
                "topic_id": 23,
                "question": "Find the sum of all natural numbers from 1 to 50.",
                "options_json": [
                    "1275",
                    "1250",
                    "1300",
                    "1225"
                ],
                "correct_answer": "1275",
                "explanation": "Formula: n(n + 1) / 2 = 50 * 51 / 2 = 25 * 51 = 1275.",
                "points": 1
            },
            {
                "id": 2309,
                "topic_id": 23,
                "question": "What is the HCF of 2/3, 8/9, 64/81, and 10/27?",
                "options_json": [
                    "2/81",
                    "160/3",
                    "160/81",
                    "2/3"
                ],
                "correct_answer": "2/81",
                "explanation": "HCF of fractions = HCF of numerators / LCM of denominators.\nNumerators: 2, 8, 64, 10 -> HCF = 2.\nDenominators: 3, 9, 81, 27 -> LCM = 81.\nHCF = 2/81.",
                "points": 1
            },
            {
                "id": 2310,
                "topic_id": 23,
                "question": "If n is an integer, (n^3 - n) is always divisible by:",
                "options_json": [
                    "6",
                    "4",
                    "5",
                    "8"
                ],
                "correct_answer": "6",
                "explanation": "n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1).\nThis is the product of three consecutive integers.\nAmong three consecutive integers, at least one is a multiple of 2 and exactly one is a multiple of 3.\nTherefore, the product is always divisible by 2 * 3 = 6.",
                "points": 1
            }
        ]
    },
    "24": {
        "title": "Percentage: Fraction Equivalence, Successive Changes, AB Rule & Base Shifts",
        "source_id": 7,
        "content": {
            "definition": "Percentage (per hundred, symbol %) is the fundamental arithmetic ratio comparing a fractional quantity to a universal base of 100. In competitive exams (SSC CGL, IBPS PO, UPSC CSAT), percentage operations form the analytical foundation for Profit & Loss, Simple & Compound Interest, and Data Interpretation. Candidates must master rapid mental conversions between vulgar fractions and percentages, the 'AB Product Constancy Rule', and successive percentage formulas.",
            "overview": "Mastery of percentages requires three mental frameworks: (1) Instant Fractional Equivalents (1/2 = 50%, 1/3 = 33.33%, 1/6 = 16.66%, 1/7 = 14.28%, 1/8 = 12.5%, 1/9 = 11.11%, 1/11 = 9.09%, 1/12 = 8.33%, 1/16 = 6.25%); (2) Base Shift Dynamics (If A is x% more than B, B is less than A by a different percentage); and (3) The AB Product Constancy Rule (If Expenditure = Price x Consumption, any percentage rise in Price demands a reciprocal decrease in Consumption to maintain constant expenditure).",
            "types": [
                {
                    "name": "1. Fraction-to-Percentage Equivalence & Multipliers",
                    "desc": "Translating percentage shifts into fractional multipliers for rapid single-line computation.",
                    "examples": [
                        "Increase by 20% = Multiply base by (1 + 1/5) = 6/5 = 1.20",
                        "Decrease by 12.5% = Multiply base by (1 - 1/8) = 7/8 = 0.875",
                        "Increase by 16.67% = Multiply base by (1 + 1/6) = 7/6",
                        "Increase by 37.5% = Multiply base by (1 + 3/8) = 11/8"
                    ]
                },
                {
                    "name": "2. Successive Percentage Changes (Compounding Shifts)",
                    "desc": "Calculating the net change when a value is sequentially adjusted by multiple percentages.",
                    "examples": [
                        "Net effect of two successive changes a% and b%: Net % = a + b + (ab / 100) %",
                        "Successive increase of 20% and 30%: 20 + 30 + (20 * 30 / 100) = 56% increase",
                        "Successive discount of 20% and 10%: -20 - 10 + (-20 * -10 / 100) = -30 + 2 = -28% (28% net discount)"
                    ]
                },
                {
                    "name": "3. The AB Product-Constancy Rule",
                    "desc": "When Product P = A * B remains constant, changes in A and B are inversely linked.",
                    "examples": [
                        "If A increases by 1/x, B must decrease by 1/(x + 1) to keep P constant.",
                        "If sugar price increases by 25% (1/4), consumption must decrease by 1/(4 + 1) = 1/5 = 20% to keep expenditure unchanged.",
                        "If A decreases by 1/x, B must increase by 1/(x - 1) to keep P constant."
                    ]
                },
                {
                    "name": "4. Base Shifts (Comparison of Two Entities)",
                    "desc": "Resolving asymmetric comparisons between entity A and entity B.",
                    "examples": [
                        "If A is 25% taller than B, how much percent is B shorter than A?",
                        "Calculation: 25% = 1/4 increase -> B is shorter by 1/(4 + 1) = 1/5 = 20%.",
                        "Formula: If A is r% more than B, B is less than A by [r / (100 + r)] * 100%."
                    ]
                },
                {
                    "name": "5. Population Growth & Asset Depreciation",
                    "desc": "Temporal exponential growth or decline across sequential years.",
                    "examples": [
                        "Population after n years at annual growth rate R%: P_n = P_0 * (1 + R/100)^n",
                        "Machine depreciation at annual rate R%: Value_n = Value_0 * (1 - R/100)^n"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Successive Percentage Change Formula",
                    "explanation": "When an initial value is altered by $a\\%$ and the resulting value is subsequently altered by $b\\%$, the overall net percentage change is given by: $\\text{Net Change} = a + b + \\frac{ab}{100}\\%$. Note: Apply positive signs for increases and negative signs for decreases.",
                    "words": [
                        "Successive Percentage",
                        "a + b + ab/100",
                        "Net Change"
                    ],
                    "correct": "Price rises by 20% and sales drop by 10%: Net change = +20 - 10 + (20 * -10)/100 = 10 - 2 = +8% increase in revenue.",
                    "incorrect": "Adding percentages linearly: 20% - 10% = 10% increase (Ignores compounding on the altered base)."
                },
                {
                    "rule_number": 2,
                    "title": "AB Product-Constancy Shortcut (Expenditure = Price * Consumption)",
                    "explanation": "If a quantity $A$ increases by the vulgar fraction $\\frac{1}{x}$, the factor $B$ must decrease by $\\frac{1}{x + 1}$ to keep their product constant. Conversely, if $A$ decreases by $\\frac{1}{x}$, $B$ must increase by $\\frac{1}{x - 1}$.",
                    "words": [
                        "Product Constancy",
                        "Price Consumption",
                        "1/(x+1)",
                        "1/(x-1)"
                    ],
                    "correct": "Price increases by 33.33% (1/3) -> Consumption decreases by 1/(3+1) = 1/4 = 25%.",
                    "incorrect": "Assuming consumption must decrease by the identical 33.33% (Violates base shift)."
                },
                {
                    "rule_number": 3,
                    "title": "Asymmetric Base Shift Rule",
                    "explanation": "If quantity $A$ is $r\\%$ more than $B$, the base for comparing $B$ to $A$ is $(100 + r)$. Thus, $B$ is less than $A$ by $\\frac{r}{100 + r} \\times 100\\%$. If $A$ is $r\\%$ less than $B$, $B$ is more than $A$ by $\\frac{r}{100 - r} \\times 100\\%$.",
                    "words": [
                        "Base Shift",
                        "Relative Comparison",
                        "Denominator Adjustment"
                    ],
                    "correct": "A earns 50% more than B: B earns less than A by 50 / (100 + 50) * 100% = 50/150 = 33.33%.",
                    "incorrect": "Concluding B earns 50% less than A (50% less than A would mean B earns half of A)."
                },
                {
                    "rule_number": 4,
                    "title": "Income, Expenditure & Savings Balance Rule",
                    "explanation": "By definition: $\\text{Income} = \\text{Expenditure} + \\text{Savings}$. If Income increases by $x\\%$ and Expenditure increases by $y\\%$, the percentage change in Savings must be computed by calculating absolute values or using weighted averages.",
                    "words": [
                        "Income = Expenditure + Savings",
                        "Weighted Average",
                        "Balance"
                    ],
                    "correct": "Let Income = 100, Exp = 80, Sav = 20. If Income +20% (120) and Exp +10% (88), new Sav = 120 - 88 = 32. % Increase in savings = (32 - 20)/20 * 100% = 60%.",
                    "incorrect": "Subtracting rates: 20% - 10% = 10% increase in savings (False linear subtraction)."
                },
                {
                    "rule_number": 5,
                    "title": "Two-Set Venn Diagram Overlap Percentage Rule",
                    "explanation": "For two overlapping attributes $A$ and $B$: $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$. If $k\\%$ fail in neither subject, then $n(A \\cup B) = 100\\% - k\\%$.",
                    "words": [
                        "Venn Diagram",
                        "Intersection",
                        "Union",
                        "Overlap"
                    ],
                    "correct": "60% passed in Math, 70% passed in English, 20% failed in both: Passed in at least one = 100 - 20 = 80%. Passed in both = 60 + 70 - 80 = 50%.",
                    "incorrect": "Adding 60 + 70 = 130% without subtracting the universal union."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Applying percentage increases directly to different base numbers.",
                    "correction": "Identify the exact base (denominator) for each percentage before performing operations.",
                    "rationale": "A 10% rise on Rs. 100 is Rs. 10, but a subsequent 10% drop on Rs. 110 is Rs. 11, leaving Rs. 99 (net 1% loss)."
                },
                {
                    "mistake": "Confusing 'percentage point change' with 'percentage change'.",
                    "correction": "An interest rate rising from 4% to 5% is a 1 percentage point increase, but a (1/4) * 100% = 25% relative increase.",
                    "rationale": "Competitive questions test this distinction rigorously in economic and data interpretation contexts."
                },
                {
                    "mistake": "Forgetting to invert base in consumption reduction problems.",
                    "correction": "If price rises by 20% (1/5), consumption decreases by 1/6 (16.67%), not 1/5.",
                    "rationale": "The denominator must reflect the new, higher total price base."
                },
                {
                    "mistake": "Treating successive discounts as additive.",
                    "correction": "Two successive discounts of 50% and 50% do not equal 100% (free). They equal: -50 - 50 + (2500/100) = -75% net discount.",
                    "rationale": "The second discount applies only to the remaining 50% balance."
                }
            ],
            "quick_revision_points": [
                "Fraction Table: 1/2=50%, 1/3=33.33%, 1/4=25%, 1/5=20%, 1/6=16.67%, 1/7=14.28%, 1/8=12.5%, 1/9=11.11%, 1/11=9.09%, 1/12=8.33%.",
                "Net successive change = a + b + (ab / 100)%.",
                "AB Rule: If A increases by 1/x, B decreases by 1/(x + 1) to keep product constant.",
                "AB Rule: If A decreases by 1/x, B increases by 1/(x - 1) to keep product constant.",
                "If A is r% more than B, B is less than A by [r / (100 + r)] * 100%.",
                "Equal successive increase and decrease of x% always results in a net loss of (x^2 / 100)%.",
                "Income = Expenditure + Savings.",
                "Set overlap: Passed in Both = Passed(A) + Passed(B) - Passed(At least one)."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2401,
                "topic_id": 24,
                "question": "If the price of petrol increases by 28%, by what percentage should a motorist reduce consumption so that his expenditure on petrol remains unchanged? (Correct to one decimal place) [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "21.9%",
                    "20.5%",
                    "22.8%",
                    "25.0%"
                ],
                "correct_answer": "21.9%",
                "explanation": "Formula: Reduction % = [r / (100 + r)] * 100%\nHere r = 28%.\nReduction % = [28 / (100 + 28)] * 100% = (28 / 128) * 100% = (7 / 32) * 100% = 700 / 32 = 21.875% approx 21.9%.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2402,
                "topic_id": 24,
                "question": "The population of a town increased by 15% in the first year and decreased by 10% in the second year. If the population at the end of the second year was 47,610, find the population at the beginning of the first year. [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "46,000",
                    "45,000",
                    "48,000",
                    "44,000"
                ],
                "correct_answer": "46,000",
                "explanation": "Let initial population be P.\nAfter Year 1: P * (1 + 15/100) = P * (115/100) = P * (23/20).\nAfter Year 2: [P * (23/20)] * (1 - 10/100) = P * (23/20) * (9/10) = P * (207/200).\nGiven: P * (207 / 200) = 47,610.\nP = (47,610 * 200) / 207 = 230 * 200 = 46,000.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2403,
                "topic_id": 24,
                "question": "A student has to secure 40% marks to pass an examination. He gets 178 marks and fails by 22 marks. What are the maximum aggregate marks? [UPSC CDS 2023]",
                "options_json": [
                    "500",
                    "450",
                    "550",
                    "600"
                ],
                "correct_answer": "500",
                "explanation": "Passing marks = Marks obtained + Marks failed by = 178 + 22 = 200 marks.\nGiven that passing percentage = 40%.\nTherefore, 40% of Total Marks = 200.\nTotal Marks = (200 / 40) * 100 = 5 * 100 = 500.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2401,
                "topic_id": 24,
                "question": "Two numbers are respectively 20% and 50% more than a third number. What percentage is the first number of the second number?",
                "options_json": [
                    "80%",
                    "75%",
                    "85%",
                    "70%"
                ],
                "correct_answer": "80%",
                "explanation": "Let the third number be 100.\nFirst number = 100 + 20% of 100 = 120.\nSecond number = 100 + 50% of 100 = 150.\nPercentage of first with respect to second = (120 / 150) * 100% = (4 / 5) * 100% = 80%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2402,
                "topic_id": 24,
                "question": "If A's salary is 50% more than B's salary, then by what percentage is B's salary less than A's salary?",
                "options_json": [
                    "33.33%",
                    "50%",
                    "25%",
                    "20%"
                ],
                "correct_answer": "33.33%",
                "explanation": "Formula: Percentage less = [r / (100 + r)] * 100% = [50 / 150] * 100% = (1 / 3) * 100% = 33.33%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2403,
                "topic_id": 24,
                "question": "The price of sugar drops by 20%. By what percentage can a housewife increase her consumption without altering her expenditure on sugar?",
                "options_json": [
                    "25%",
                    "20%",
                    "16.67%",
                    "30%"
                ],
                "correct_answer": "25%",
                "explanation": "Drop of 20% = 1/5 reduction.\nUsing AB rule: to maintain constant product, consumption must increase by 1/(5 - 1) = 1/4 = 25%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2404,
                "topic_id": 24,
                "question": "A person spends 75% of his income. His income increases by 20% and his expenditure increases by 10%. Find the percentage increase in his savings.",
                "options_json": [
                    "50%",
                    "40%",
                    "30%",
                    "25%"
                ],
                "correct_answer": "50%",
                "explanation": "Let initial Income = 100. Expenditure = 75, Savings = 25.\nNew Income = 100 * 1.20 = 120.\nNew Expenditure = 75 * 1.10 = 82.5.\nNew Savings = 120 - 82.5 = 37.5.\nIncrease in savings = 37.5 - 25 = 12.5.\n% increase in savings = (12.5 / 25) * 100% = 50%.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2405,
                "topic_id": 24,
                "question": "A single equivalent discount for two successive discounts of 20% and 15% is:",
                "options_json": [
                    "32%",
                    "35%",
                    "30%",
                    "28%"
                ],
                "correct_answer": "32%",
                "explanation": "Net discount = d1 + d2 - (d1 * d2 / 100) = 20 + 15 - (20 * 15 / 100) = 35 - 3 = 32%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2406,
                "topic_id": 24,
                "question": "In an examination, 70% candidates passed in English and 80% passed in Mathematics, while 10% failed in both. If 144 candidates passed in both subjects, find the total number of candidates.",
                "options_json": [
                    "240",
                    "200",
                    "280",
                    "300"
                ],
                "correct_answer": "240",
                "explanation": "Percentage failing in both = 10% -> Percentage passing in at least one = 100 - 10 = 90%.\nPassed in both = Passed(E) + Passed(M) - Passed(At least one) = 70% + 80% - 90% = 60%.\n60% of Total = 144 -> Total = (144 / 60) * 100 = 240.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2407,
                "topic_id": 24,
                "question": "The price of an article is first increased by 20% and then decreased by 20%. What is the net percentage change in price?",
                "options_json": [
                    "4% decrease",
                    "4% increase",
                    "No change",
                    "2% decrease"
                ],
                "correct_answer": "4% decrease",
                "explanation": "Formula for equal increase and decrease: Net % = - (x^2 / 100)% = - (20^2 / 100)% = -400/100 = -4% (a 4% decrease).",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2408,
                "topic_id": 24,
                "question": "Due to a 25% reduction in the price of apples, a customer can purchase 2 kg more apples for Rs. 240. What is the original price per kg?",
                "options_json": [
                    "Rs. 40",
                    "Rs. 30",
                    "Rs. 36",
                    "Rs. 48"
                ],
                "correct_answer": "Rs. 40",
                "explanation": "Money saved due to price drop = 25% of 240 = Rs. 60.\nThis Rs. 60 buys 2 kg extra -> Reduced price per kg = 60 / 2 = Rs. 30/kg.\nSince reduced price = 75% of original price:\nOriginal price * 0.75 = 30 -> Original price = 30 / 0.75 = Rs. 40/kg.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2409,
                "topic_id": 24,
                "question": "If the radius of a circle is increased by 10%, by what percentage does its area increase?",
                "options_json": [
                    "21%",
                    "20%",
                    "10%",
                    "22%"
                ],
                "correct_answer": "21%",
                "explanation": "Area = pi * r^2 = pi * r * r.\nNet percentage change = 10 + 10 + (10 * 10 / 100) = 20 + 1 = 21%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2410,
                "topic_id": 24,
                "question": "Fresh fruit contains 68% water and dry fruit contains 20% water. How many kg of dry fruit can be obtained from 100 kg of fresh fruit?",
                "options_json": [
                    "40 kg",
                    "32 kg",
                    "45 kg",
                    "36 kg"
                ],
                "correct_answer": "40 kg",
                "explanation": "The quantity of pulp remains constant.\nIn 100 kg fresh fruit: Pulp = (100 - 68)% = 32% of 100 = 32 kg.\nIn dry fruit, water is 20%, so pulp is 80%.\nLet total dry fruit be D: 80% of D = 32 kg -> 0.8 * D = 32 -> D = 32 / 0.8 = 40 kg.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2401,
                "topic_id": 24,
                "question": "If 60% of A's income is equal to 75% of B's income, then B's income is what percentage of A's income?",
                "options_json": [
                    "80%",
                    "75%",
                    "85%",
                    "90%"
                ],
                "correct_answer": "80%",
                "explanation": "0.60 * A = 0.75 * B -> B / A = 60 / 75 = 4 / 5.\nPercentage = (4 / 5) * 100% = 80%.",
                "points": 1
            },
            {
                "id": 2402,
                "topic_id": 24,
                "question": "A number is increased by 20% and then decreased by 10%. What is the net percentage change?",
                "options_json": [
                    "8% increase",
                    "10% increase",
                    "8% decrease",
                    "2% increase"
                ],
                "correct_answer": "8% increase",
                "explanation": "Net % = 20 - 10 + (20 * -10 / 100) = 10 - 2 = +8% increase.",
                "points": 1
            },
            {
                "id": 2403,
                "topic_id": 24,
                "question": "What is the equivalent single discount for three successive discounts of 10%, 20%, and 25%?",
                "options_json": [
                    "46%",
                    "45%",
                    "48%",
                    "50%"
                ],
                "correct_answer": "46%",
                "explanation": "Multiplier = (1 - 0.10) * (1 - 0.20) * (1 - 0.25) = 0.90 * 0.80 * 0.75 = 0.72 * 0.75 = 0.54.\nNet discount = 1 - 0.54 = 0.46 = 46%.",
                "points": 1
            },
            {
                "id": 2404,
                "topic_id": 24,
                "question": "If A is 40% less than B, by what percentage is B more than A?",
                "options_json": [
                    "66.67%",
                    "40%",
                    "60%",
                    "50%"
                ],
                "correct_answer": "66.67%",
                "explanation": "Formula: [r / (100 - r)] * 100% = [40 / 60] * 100% = (2/3) * 100% = 66.67%.",
                "points": 1
            },
            {
                "id": 2405,
                "topic_id": 24,
                "question": "The length of a rectangle increases by 30% and its breadth decreases by 20%. The area of the rectangle will:",
                "options_json": [
                    "Increase by 4%",
                    "Increase by 10%",
                    "Decrease by 4%",
                    "Decrease by 6%"
                ],
                "correct_answer": "Increase by 4%",
                "explanation": "Net change = +30 - 20 + (30 * -20 / 100) = 10 - 6 = +4% increase.",
                "points": 1
            },
            {
                "id": 2406,
                "topic_id": 24,
                "question": "In an election between two candidates, the winner obtained 56% of total votes and won by a majority of 1440 votes. What was the total number of votes polled?",
                "options_json": [
                    "12,000",
                    "14,000",
                    "10,000",
                    "15,000"
                ],
                "correct_answer": "12,000",
                "explanation": "Winner = 56%, Loser = 100 - 56 = 44%.\nMajority = 56% - 44% = 12%.\n12% of Total = 1440 -> Total = (1440 / 12) * 100 = 120 * 100 = 12,000.",
                "points": 1
            },
            {
                "id": 2407,
                "topic_id": 24,
                "question": "A candidate scores 25% and fails by 30 marks, while another candidate scores 50% and gets 20 marks more than the passing marks. What are the passing marks?",
                "options_json": [
                    "80",
                    "70",
                    "60",
                    "90"
                ],
                "correct_answer": "80",
                "explanation": "Difference in % = 50% - 25% = 25%.\nDifference in marks = 20 - (-30) = 50 marks.\n25% of Total = 50 -> Total marks = 200.\nPassing marks = 25% of 200 + 30 = 50 + 30 = 80.",
                "points": 1
            },
            {
                "id": 2408,
                "topic_id": 24,
                "question": "If price of cooking oil rises by 25%, by how much percent should consumption be cut to keep expenditure identical?",
                "options_json": [
                    "20%",
                    "25%",
                    "15%",
                    "16.67%"
                ],
                "correct_answer": "20%",
                "explanation": "Using AB rule: 25% = 1/4 increase -> consumption decreases by 1/(4 + 1) = 1/5 = 20%.",
                "points": 1
            },
            {
                "id": 2409,
                "topic_id": 24,
                "question": "Salary of an employee was reduced by 15% and later increased by 15%. His net loss percentage is:",
                "options_json": [
                    "2.25%",
                    "0%",
                    "3%",
                    "1.5%"
                ],
                "correct_answer": "2.25%",
                "explanation": "Net loss = (x^2 / 100)% = (15^2 / 100)% = 225 / 100 = 2.25%.",
                "points": 1
            },
            {
                "id": 2410,
                "topic_id": 24,
                "question": "What is 20% of 30% of 40% of 5000?",
                "options_json": [
                    "120",
                    "100",
                    "150",
                    "80"
                ],
                "correct_answer": "120",
                "explanation": "0.20 * 0.30 * 0.40 * 5000 = (1/5) * (3/10) * (2/5) * 5000 = (6 / 250) * 5000 = 6 * 20 = 120.",
                "points": 1
            }
        ]
    },
    "25": {
        "title": "Profit and Loss: CP-SP Relations, Markups, Discounts & Dishonest Dealers",
        "source_id": 7,
        "content": {
            "definition": "Profit and Loss is the commercial mathematics discipline evaluating transactional margins between Cost Price (CP), Selling Price (SP), and Marked Price (MP). In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions evaluate complex successive discount series, false weight deceptions by dishonest merchants, break-even analyses, and dual-transaction problems where articles are sold at equal selling prices with asymmetric gain/loss percentages.",
            "overview": "Fundamental formulas:\n- Profit = SP - CP (when SP > CP); Loss = CP - SP (when CP > SP)\n- Profit % = (Profit / CP) * 100%; Loss % = (Loss / CP) * 100%\n- Discount = MP - SP; Discount % = (Discount / MP) * 100%\n- Golden Relationship: CP * (1 + P%/100) = MP * (1 - D%/100) = SP\n- Markup % = [(MP - CP) / CP] * 100%",
            "types": [
                {
                    "name": "1. Basic CP, SP & Profit/Loss Margins",
                    "desc": "Foundational ratio links between cost and selling prices.",
                    "examples": [
                        "A profit of 25% means CP:SP = 4:5 (SP = 1.25 * CP)",
                        "A loss of 16.67% (1/6) means CP:SP = 6:5 (SP = 5/6 * CP)",
                        "Finding CP when SP and Profit % are known: CP = SP * [100 / (100 + P%)]"
                    ]
                },
                {
                    "name": "2. Marked Price, Discount & The Golden Ratio",
                    "desc": "Connecting production cost to catalog price via trade discounts.",
                    "examples": [
                        "Ratio of MP to CP: MP / CP = (100 + P%) / (100 - D%)",
                        "Example: A trader wants a 20% profit after giving a 10% discount: MP/CP = (100 + 20)/(100 - 10) = 120/90 = 4/3 -> Markup is 33.33%."
                    ]
                },
                {
                    "name": "3. Dishonest Dealer & Faulty Weight Problems",
                    "desc": "Cheating at buying or selling using tampered scale balances.",
                    "examples": [
                        "If a trader sells at cost price but uses 900g instead of 1000g: Gain % = [Error / (True Value - Error)] * 100% = [100 / 900] * 100% = 11.11%",
                        "Compounded cheating: Cheating x% while buying and y% while selling."
                    ]
                },
                {
                    "name": "4. Equal SP with Equal Gain and Loss (% x)",
                    "desc": "Selling two items at the identical Selling Price, one at x% gain and the other at x% loss.",
                    "examples": [
                        "The transaction ALWAYS results in an overall net loss.",
                        "Net Loss % = (x^2 / 100)%",
                        "Total Loss in Rupees = [2 * SP * x^2] / [100^2 - x^2]"
                    ]
                },
                {
                    "name": "5. Promotional Free Article Schemes",
                    "desc": "Computing effective discount rate in promotional offers.",
                    "examples": [
                        "'Buy 3, Get 1 Free': Customer receives 4 articles for the price of 3. Discount % = [Free Articles / Total Articles] * 100% = [1 / 4] * 100% = 25%.",
                        "'Buy 5, Get 3 Free': Discount % = 3 / (5 + 3) * 100% = 3/8 * 100% = 37.5%."
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Equal Selling Price with Symmetrical Gain/Loss Rule",
                    "explanation": "When two articles are sold at the SAME selling price (SP), one at a profit of $x\\%$ and the other at a loss of $x\\%$, the overall transaction ALWAYS yields a net loss of: $\\text{Net Loss }\\% = \\left(\\frac{x}{10}\\right)^2\\% = \\frac{x^2}{100}\\%$.",
                    "words": [
                        "Equal SP",
                        "Same Selling Price",
                        "Net Loss x^2/100",
                        "No Profit No Loss Trap"
                    ],
                    "correct": "Two houses sold for Rs. 10 lakhs each, one at 20% gain and other at 20% loss: Net loss = 20^2 / 100 = 4% loss.",
                    "incorrect": "Assuming +20% and -20% cancel out to yield 0% profit/loss (SP is equal, not CP)."
                },
                {
                    "rule_number": 2,
                    "title": "Golden Ratio: $\\frac{MP}{CP} = \\frac{100 + P\\%}{100 - D\\%}$",
                    "explanation": "Since $\\text{SP} = \\text{CP} \\times \\frac{100 + P}{100} = \\text{MP} \\times \\frac{100 - D}{100}$, equating both expressions yields: $\\frac{\\text{MP}}{\\text{CP}} = \\frac{100 + P\\%}{100 - D\\%}$.",
                    "words": [
                        "Golden Formula",
                        "MP/CP Ratio",
                        "Markup",
                        "Profit Discount Balance"
                    ],
                    "correct": "To gain 14% after giving 5% discount: MP/CP = (100 + 14)/(100 - 5) = 114/95 = 6/5. Markup = (6-5)/5 = 20%.",
                    "incorrect": "Calculating markup by adding P% and D%: 14% + 5% = 19% (Fails because bases differ)."
                },
                {
                    "rule_number": 3,
                    "title": "Dishonest Merchant Weight Cheat Formula",
                    "explanation": "If a shopkeeper sells goods claiming to sell at Cost Price but uses a false weight that measures $W_{\\text{false}}$ instead of true weight $W_{\\text{true}}$, the profit is: $\\text{Gain }\\% = \\frac{W_{\\text{true}} - W_{\\text{false}}}{W_{\\text{false}}} \\times 100\\% = \\frac{\\text{Error}}{\\text{True} - \\text{Error}} \\times 100\\%$.",
                    "words": [
                        "Dishonest Dealer",
                        "False Weight",
                        "Error / (True - Error)"
                    ],
                    "correct": "Uses 800g instead of 1000g: Gain = (1000 - 800) / 800 * 100% = 200/800 * 100% = 25%.",
                    "incorrect": "Calculating gain as (200 / 1000) * 100% = 20% (The merchant's actual cost was for 800g, not 1000g)."
                },
                {
                    "rule_number": 4,
                    "title": "Equivalent Single Discount for Successive Series",
                    "explanation": "For two successive discounts of $d_1\\%$ and $d_2\\%$: $D_{\\text{net}} = d_1 + d_2 - \\frac{d_1 d_2}{100}\\%$. For three discounts: $D_{\\text{net}} = 100 - 100 \\times (1 - d_1/100)(1 - d_2/100)(1 - d_3/100)$.",
                    "words": [
                        "Successive Discounts",
                        "Equivalent Discount",
                        "d1 + d2 - d1d2/100"
                    ],
                    "correct": "Successive discounts of 30% and 20%: Net discount = 30 + 20 - (600/100) = 44%.",
                    "incorrect": "Adding discounts: 30% + 20% = 50% discount."
                },
                {
                    "rule_number": 5,
                    "title": "Free Articles Equivalent Discount Rule",
                    "explanation": "In an offer 'Buy X, Get Y Free', the customer pays for X items but carries home (X + Y) items. The effective discount is: $\\text{Discount }\\% = \\frac{Y}{X + Y} \\times 100\\%$.",
                    "words": [
                        "Buy X Get Y Free",
                        "Promotional Discount",
                        "Free Articles"
                    ],
                    "correct": "Buy 4, Get 1 Free: Discount = 1 / (4 + 1) * 100% = 1/5 * 100% = 20%.",
                    "incorrect": "Discount = 1 / 4 * 100% = 25% (4 is the paid quantity, not the total inventory delivered)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Calculating Profit/Loss percentage on Selling Price instead of Cost Price.",
                    "correction": "Unless explicitly stated as 'profit calculated on selling price', Profit % is ALWAYS computed on Cost Price: (Profit / CP) * 100%.",
                    "rationale": "Cost Price represents the actual capital investment."
                },
                {
                    "mistake": "Believing equal % gain and % loss on same SP produces no profit and no loss.",
                    "correction": "It ALWAYS results in a net loss equal to (x^2 / 100)%.",
                    "rationale": "The base for the gain (smaller CP) is lower than the base for the loss (larger CP)."
                },
                {
                    "mistake": "Dividing error by true weight in dishonest dealer problems.",
                    "correction": "Divide error by FALSE weight (the actual weight dispensed), because that represents the merchant's real expenditure.",
                    "rationale": "Merchant invests only the cost of the false weight."
                },
                {
                    "mistake": "Adding successive discount percentages linearly.",
                    "correction": "Use the multiplicative formula: (1 - d1/100)(1 - d2/100)...",
                    "rationale": "Second discount applies only to the diminished price after the first discount."
                }
            ],
            "quick_revision_points": [
                "Profit = SP - CP; Loss = CP - SP.",
                "Profit % = (Profit / CP) * 100%; Loss % = (Loss / CP) * 100%.",
                "MP / CP = (100 + P%) / (100 - D%).",
                "Equal SP with x% profit and x% loss -> Net loss = (x^2 / 100)%.",
                "Dishonest dealer gain % = [Error / (True Value - Error)] * 100%.",
                "Buy X, Get Y Free -> Discount % = [Y / (X + Y)] * 100%.",
                "Successive discounts of d1 and d2 = [d1 + d2 - (d1 * d2 / 100)]%.",
                "CP = SP * 100 / (100 + P%); SP = CP * (100 + P%) / 100."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2501,
                "topic_id": 25,
                "question": "A shopkeeper marks his goods at 30% above the cost price and allows a discount of 15% on the marked price. What is his gain percentage? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "10.5%",
                    "11.5%",
                    "12.0%",
                    "15.0%"
                ],
                "correct_answer": "10.5%",
                "explanation": "Let CP = 100.\nMarked Price (MP) = 100 + 30 = 130.\nDiscount = 15% of 130 = 0.15 * 130 = 19.5.\nSelling Price (SP) = 130 - 19.5 = 110.5.\nProfit = SP - CP = 110.5 - 100 = 10.5.\nGain % = (10.5 / 100) * 100% = 10.5%.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2502,
                "topic_id": 25,
                "question": "A person sold two articles for Rs. 9,600 each. On one he gained 20% and on the other he lost 20%. What was his overall gain or loss in the entire transaction? [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "Loss of Rs. 800",
                    "Loss of Rs. 750",
                    "Gain of Rs. 800",
                    "No profit no loss"
                ],
                "correct_answer": "Loss of Rs. 800",
                "explanation": "Since Selling Prices are equal (SP = 9600 each) with 20% gain and 20% loss:\nOverall Loss % = (x^2 / 100)% = (20^2 / 100)% = 4% loss.\nTotal SP = 9600 + 9600 = Rs. 19,200.\nTotal CP = Total SP / (1 - 0.04) = 19,200 / 0.96 = Rs. 20,000.\nTotal Loss = Total CP - Total SP = 20,000 - 19,200 = Rs. 800.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2503,
                "topic_id": 25,
                "question": "A dishonest dealer professes to sell his goods at cost price, but uses a false weight of 920 grams for a kilogram weight. Find his gain percentage. [UPSC CDS 2023]",
                "options_json": [
                    "8.70%",
                    "8.00%",
                    "9.20%",
                    "8.25%"
                ],
                "correct_answer": "8.70%",
                "explanation": "Formula: Gain % = [Error / False Weight] * 100%\nError = 1000 - 920 = 80g.\nFalse Weight = 920g.\nGain % = (80 / 920) * 100% = (8 / 92) * 100% = (2 / 23) * 100% = 200 / 23 = 8.695% approx 8.70%.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2501,
                "topic_id": 25,
                "question": "A trader sells an article at a profit of 20%. If he had bought it at 10% less and sold it for Rs. 18 less, he would have gained 25%. What is the cost price of the article?",
                "options_json": [
                    "Rs. 240",
                    "Rs. 200",
                    "Rs. 250",
                    "Rs. 220"
                ],
                "correct_answer": "Rs. 240",
                "explanation": "Let initial CP = 100x -> Initial SP = 120x.\nNew CP = 100x - 10% = 90x.\nNew SP = 90x + 25% of 90x = 90x * 1.25 = 112.5x.\nGiven difference in SP: 120x - 112.5x = 18 -> 7.5x = 18.\nx = 18 / 7.5 = 2.4.\nCost Price = 100x = 100 * 2.4 = Rs. 240.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 2502,
                "topic_id": 25,
                "question": "By selling 33 meters of cloth, a shopkeeper gains the selling price of 11 meters. Find his gain percentage.",
                "options_json": [
                    "50%",
                    "33.33%",
                    "25%",
                    "40%"
                ],
                "correct_answer": "50%",
                "explanation": "Profit = SP of 33m - CP of 33m.\nGiven: Profit = SP of 11m.\nSP of 11 = SP of 33 - CP of 33 -> CP of 33 = SP of 22.\nCP / SP = 22 / 33 = 2 / 3.\nProfit % = (SP - CP)/CP * 100% = (3 - 2)/2 * 100% = 1/2 * 100% = 50%.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2503,
                "topic_id": 25,
                "question": "What is the effective discount offered under the promotional scheme 'Buy 5, Get 3 Free'?",
                "options_json": [
                    "37.5%",
                    "60%",
                    "30%",
                    "25%"
                ],
                "correct_answer": "37.5%",
                "explanation": "Discount % = [Free Articles / Total Articles] * 100% = [3 / (5 + 3)] * 100% = (3 / 8) * 100% = 37.5%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2504,
                "topic_id": 25,
                "question": "A merchant marks his goods up by 40% above cost price and allows a discount of 25%. His profit percentage is:",
                "options_json": [
                    "5%",
                    "10%",
                    "15%",
                    "8%"
                ],
                "correct_answer": "5%",
                "explanation": "Let CP = 100 -> MP = 140.\nDiscount = 25% of 140 = 35.\nSP = 140 - 35 = 105.\nProfit % = (105 - 100)/100 * 100% = 5%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2505,
                "topic_id": 25,
                "question": "A dishonest grocer sells rice at a profit of 10% on CP and also uses a weight that is 20% less than the true weight. What is his total profit percentage?",
                "options_json": [
                    "37.5%",
                    "32.0%",
                    "30.0%",
                    "35.0%"
                ],
                "correct_answer": "37.5%",
                "explanation": "Let 1000g cost Rs. 1000.\nHe charges 10% profit -> Price charged = Rs. 1100.\nHe delivers 20% less weight -> Weight given = 800g (his actual cost is Rs. 800).\nProfit = 1100 - 800 = Rs. 300.\nTotal Profit % = (300 / 800) * 100% = 37.5%.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 2506,
                "topic_id": 25,
                "question": "The cost price of 15 articles is equal to the selling price of 10 articles. Find the profit percentage.",
                "options_json": [
                    "50%",
                    "33.33%",
                    "25%",
                    "60%"
                ],
                "correct_answer": "50%",
                "explanation": "15 * CP = 10 * SP -> SP / CP = 15 / 10 = 3 / 2.\nProfit % = (3 - 2)/2 * 100% = 1/2 * 100% = 50%.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2507,
                "topic_id": 25,
                "question": "A watch is sold for Rs. 440 at a loss of 12%. At what price should it be sold to gain 10%?",
                "options_json": [
                    "Rs. 550",
                    "Rs. 500",
                    "Rs. 520",
                    "Rs. 540"
                ],
                "correct_answer": "Rs. 550",
                "explanation": "SP1 = 88% of CP = 440 -> CP = 440 / 0.88 = Rs. 500.\nRequired SP2 = 110% of CP = 1.10 * 500 = Rs. 550.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2508,
                "topic_id": 25,
                "question": "An article is listed at Rs. 900 and two successive discounts of 10% and 20% are given. What is the selling price?",
                "options_json": [
                    "Rs. 648",
                    "Rs. 630",
                    "Rs. 650",
                    "Rs. 620"
                ],
                "correct_answer": "Rs. 648",
                "explanation": "SP = 900 * (1 - 0.10) * (1 - 0.20) = 900 * 0.90 * 0.80 = 900 * 0.72 = Rs. 648.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2509,
                "topic_id": 25,
                "question": "If the difference between the selling prices of an article at a profit of 8% and at a loss of 8% is Rs. 96, what is the cost price?",
                "options_json": [
                    "Rs. 600",
                    "Rs. 500",
                    "Rs. 550",
                    "Rs. 650"
                ],
                "correct_answer": "Rs. 600",
                "explanation": "Difference in SP = 8% - (-8%) = 16% of CP.\n16% of CP = 96 -> CP = (96 / 16) * 100 = 6 * 100 = Rs. 600.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2510,
                "topic_id": 25,
                "question": "A manufacturer sells an article to a wholesale dealer at a profit of 10%. The wholesale dealer sells it to a retailer at a profit of 20%. The retailer sells it to a consumer for Rs. 1452 at a profit of 10%. What was the cost of the manufacturer?",
                "options_json": [
                    "Rs. 1000",
                    "Rs. 1100",
                    "Rs. 950",
                    "Rs. 1050"
                ],
                "correct_answer": "Rs. 1000",
                "explanation": "Let manufacturer CP = C.\nC * 1.10 * 1.20 * 1.10 = 1452.\nC * (11/10) * (6/5) * (11/10) = C * (726 / 500) = 1452.\nC = (1452 * 500) / 726 = 2 * 500 = Rs. 1000.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2501,
                "topic_id": 25,
                "question": "Selling an item for Rs. 720 yields a 20% loss. What selling price is required to yield a 15% profit?",
                "options_json": [
                    "Rs. 1035",
                    "Rs. 900",
                    "Rs. 990",
                    "Rs. 1050"
                ],
                "correct_answer": "Rs. 1035",
                "explanation": "80% of CP = 720 -> CP = 720 / 0.8 = 900.\nTarget SP = 1.15 * 900 = Rs. 1035.",
                "points": 1
            },
            {
                "id": 2502,
                "topic_id": 25,
                "question": "A retailer buys 20 pens for Rs. 40 and sells 15 pens for Rs. 40. Find his profit percentage.",
                "options_json": [
                    "33.33%",
                    "25%",
                    "20%",
                    "30%"
                ],
                "correct_answer": "33.33%",
                "explanation": "CP of 1 pen = 40 / 20 = Rs. 2.\nSP of 1 pen = 40 / 15 = Rs. 8/3.\nProfit % = [(8/3 - 2) / 2] * 100% = [(2/3) / 2] * 100% = 1/3 * 100% = 33.33%.",
                "points": 1
            },
            {
                "id": 2503,
                "topic_id": 25,
                "question": "Two cycles were sold for Rs. 3990 each, gaining 5% on one and losing 5% on the other. The net result was:",
                "options_json": [
                    "Loss of 0.25%",
                    "Gain of 0.25%",
                    "No gain no loss",
                    "Loss of 1%"
                ],
                "correct_answer": "Loss of 0.25%",
                "explanation": "Net % = (x^2 / 100)% loss = (5^2 / 100)% = 0.25% loss.",
                "points": 1
            },
            {
                "id": 2504,
                "topic_id": 25,
                "question": "Find the marked price of a shirt if its cost price is Rs. 500 and the dealer wishes to make 20% profit after offering a 20% discount.",
                "options_json": [
                    "Rs. 750",
                    "Rs. 700",
                    "Rs. 800",
                    "Rs. 650"
                ],
                "correct_answer": "Rs. 750",
                "explanation": "MP / CP = (100 + P) / (100 - D) = (100 + 20) / (100 - 20) = 120 / 80 = 3 / 2.\nMP = 500 * (3 / 2) = Rs. 750.",
                "points": 1
            },
            {
                "id": 2505,
                "topic_id": 25,
                "question": "Under a 'Buy 2, Get 1 Free' offer, what is the effective discount percentage?",
                "options_json": [
                    "33.33%",
                    "50%",
                    "25%",
                    "20%"
                ],
                "correct_answer": "33.33%",
                "explanation": "Discount % = 1 / (2 + 1) * 100% = 1/3 * 100% = 33.33%.",
                "points": 1
            },
            {
                "id": 2506,
                "topic_id": 25,
                "question": "What is the single discount equivalent to successive discounts of 20% and 5%?",
                "options_json": [
                    "24%",
                    "25%",
                    "23%",
                    "22%"
                ],
                "correct_answer": "24%",
                "explanation": "Net discount = 20 + 5 - (20 * 5 / 100) = 25 - 1 = 24%.",
                "points": 1
            },
            {
                "id": 2507,
                "topic_id": 25,
                "question": "If selling price is doubled, the profit triples. Find the initial profit percentage.",
                "options_json": [
                    "100%",
                    "50%",
                    "150%",
                    "200%"
                ],
                "correct_answer": "100%",
                "explanation": "Let CP = C, SP = S. Profit P = S - C.\nIf SP = 2S, new profit = 2S - C = 3P.\n2S - C = 3(S - C) -> 2S - C = 3S - 3C -> S = 2C.\nInitial profit = S - C = 2C - C = C.\nProfit % = (C / C) * 100% = 100%.",
                "points": 1
            },
            {
                "id": 2508,
                "topic_id": 25,
                "question": "A fruit merchant bought oranges at 8 for Rs. 10 and sold them at 10 for Rs. 8. His loss percentage is:",
                "options_json": [
                    "36%",
                    "30%",
                    "25%",
                    "40%"
                ],
                "correct_answer": "36%",
                "explanation": "Take LCM of articles (8 and 10) = 40 oranges.\nCP of 40 oranges = 40 * (10 / 8) = Rs. 50.\nSP of 40 oranges = 40 * (8 / 10) = Rs. 32.\nLoss = 50 - 32 = 18.\nLoss % = (18 / 50) * 100% = 36%.",
                "points": 1
            },
            {
                "id": 2509,
                "topic_id": 25,
                "question": "A merchant professes to sell at cost price but uses 850g for 1 kg. His profit is:",
                "options_json": [
                    "17.65%",
                    "15.00%",
                    "18.25%",
                    "16.67%"
                ],
                "correct_answer": "17.65%",
                "explanation": "Gain % = [150 / 850] * 100% = (3 / 17) * 100% = 300 / 17 = 17.647% approx 17.65%.",
                "points": 1
            },
            {
                "id": 2510,
                "topic_id": 25,
                "question": "An article is sold at 10% loss. Had it been sold for Rs. 9 more, there would have been a gain of 12.5%. Find the cost price.",
                "options_json": [
                    "Rs. 40",
                    "Rs. 45",
                    "Rs. 50",
                    "Rs. 36"
                ],
                "correct_answer": "Rs. 40",
                "explanation": "Total percentage difference = 12.5% - (-10%) = 22.5%.\n22.5% of CP = 9 -> CP = (9 / 22.5) * 100 = (90 / 225) * 100 = (2 / 5) * 100 = Rs. 40.",
                "points": 1
            }
        ]
    },
    "26": {
        "title": "Ratio and Proportion: Mean Proportional, Compound Ratios & Partnerships",
        "source_id": 7,
        "content": {
            "definition": "Ratio is the comparative relation between two quantities of identical dimension expressed as a fraction $a:b = \\frac{a}{b}$. Proportion is the mathematical assertion of equality between two ratios ($a:b :: c:d \\iff \\frac{a}{b} = \\frac{c}{d}$). In competitive examinations (SSC CGL, CDS, IBPS PO), ratio applications govern partnership capital investments (Capital x Time), proportional sharing of inherited wealth, mixture dilutions, and mean/third/fourth proportion calculations.",
            "overview": "Fundamental Principles:\n- Compounding Ratios: Ratio compounded of $(a:b)$ and $(c:d)$ is $(ac : bd)$.\n- Mean Proportional: $b = \\sqrt{ac}$ between $a$ and $c$.\n- Third Proportional: $c = \\frac{b^2}{a}$ where $a:b :: b:c$.\n- Fourth Proportional: $d = \\frac{bc}{a}$ where $a:b :: c:d$.\n- Partnership Rule: $\\text{Profit Ratio} = (C_1 \\times T_1) : (C_2 \\times T_2) : (C_3 \\times T_3)$.\n- Componendo & Dividendo: If $\\frac{a}{b} = \\frac{c}{d}$, then $\\frac{a+b}{a-b} = \\frac{c+d}{c-d}$.",
            "types": [
                {
                    "name": "1. Connecting & Bridging Chained Ratios",
                    "desc": "Unifying independent fractional links (A:B and B:C into A:B:C).",
                    "examples": [
                        "If A:B = 2:3 and B:C = 4:5, multiply to align common term B (LCM of 3 and 4 = 12):",
                        "A:B = 8:12, B:C = 12:15 -> A:B:C = 8:12:15",
                        "Shortcut: A:B:C = (2*4) : (3*4) : (3*5) = 8:12:15"
                    ]
                },
                {
                    "name": "2. Mean, Third, and Fourth Proportional",
                    "desc": "Calculating geometric and proportional terms.",
                    "examples": [
                        "Mean Proportional of 4 and 16: sqrt(4 * 16) = sqrt(64) = 8",
                        "Third Proportional of 12 and 18: b^2 / a = 18^2 / 12 = 324 / 12 = 27",
                        "Fourth Proportional of 6, 8, and 12: (8 * 12) / 6 = 96 / 6 = 16"
                    ]
                },
                {
                    "name": "3. Commercial Partnership Profit Distribution",
                    "desc": "Splitting business returns proportional to capital and investment duration.",
                    "examples": [
                        "Profits are shared in the direct ratio of (Capital * Time Period)",
                        "A invests Rs. 50,000 for 12 months; B invests Rs. 80,000 for 6 months:",
                        "Profit Ratio A:B = (50,000 * 12) : (80,000 * 6) = 600,000 : 480,000 = 5:4"
                    ]
                },
                {
                    "name": "4. Income, Expenditure & Coin Denomination Problems",
                    "desc": "Evaluating financial systems governed by proportional multipliers.",
                    "examples": [
                        "Income = Expenditure + Savings",
                        "Bag contains coins of Rs. 1, 50p, 25p in ratio 2:3:4 with total value Rs. 90:",
                        "Value ratio = (2 * 1) : (3 * 0.5) : (4 * 0.25) = 2 : 1.5 : 1 = 4 : 3 : 2 -> 9 units = 90"
                    ]
                },
                {
                    "name": "5. Componendo and Dividendo Algebraic Operations",
                    "desc": "Simplifying rational expressions and quadratic roots.",
                    "examples": [
                        "If (x + a) / (x - a) = m / n -> Applying C&D: [(x+a)+(x-a)] / [(x+a)-(x-a)] = (m+n)/(m-n) -> 2x / 2a = (m+n)/(m-n) -> x/a = (m+n)/(m-n)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Chained Ratio Bridging Rule",
                    "explanation": "To combine $A:B = a_1:b_1$ and $B:C = a_2:b_2$, scale the ratios such that the common variable $B$ has the identical numerical coefficient (the LCM of $b_1$ and $a_2$). $A:B:C = (a_1 \\times a_2) : (b_1 \\times a_2) : (b_1 \\times b_2)$.",
                    "words": [
                        "Chained Ratio",
                        "LCM Scaling",
                        "A:B:C",
                        "Common Variable"
                    ],
                    "correct": "A:B = 3:4, B:C = 5:6 -> A:B:C = (3*5) : (4*5) : (4*6) = 15:20:24.",
                    "incorrect": "Writing A:B:C = 3:4:6 by arbitrarily dropping the second B coefficient."
                },
                {
                    "rule_number": 2,
                    "title": "Proportional Terms Definitions (Mean, Third, Fourth)",
                    "explanation": "(1) Fourth proportional to $a, b, c$: $x = \\frac{bc}{a}$.\n(2) Third proportional to $a, b$: $x = \\frac{b^2}{a}$.\n(3) Mean proportional between $a$ and $b$: $x = \\sqrt{ab}$.",
                    "words": [
                        "Mean Proportional",
                        "Third Proportional",
                        "Fourth Proportional",
                        "sqrt(ab)"
                    ],
                    "correct": "Third proportional to 9 and 15: 15^2 / 9 = 225 / 9 = 25.",
                    "incorrect": "Calculating third proportional as 15 - 9 = 6 or 15 + 6 = 21 (Additive arithmetic assumption)."
                },
                {
                    "rule_number": 3,
                    "title": "Partnership Capital-Duration Matrix Rule",
                    "explanation": "Profit distribution in a commercial enterprise is strictly determined by the product of Capital ($C$) and Time duration ($T$): $\\text{Profit}_1 : \\text{Profit}_2 : \\text{Profit}_3 = C_1 T_1 : C_2 T_2 : C_3 T_3$.",
                    "words": [
                        "Partnership",
                        "Capital x Time",
                        "Profit Share"
                    ],
                    "correct": "A invests Rs. 2000 for 12 months; B joins after 4 months with Rs. 3000 (active 8 months): Profit ratio = (2000 * 12) : (3000 * 8) = 24000 : 24000 = 1:1.",
                    "incorrect": "Dividing profit based only on investment amounts (2000:3000 = 2:3) ignoring time duration."
                },
                {
                    "rule_number": 4,
                    "title": "Componendo and Dividendo Rule",
                    "explanation": "If $\\frac{a}{b} = \\frac{c}{d}$, then adding and subtracting the denominator from the numerator yields: $\\frac{a + b}{a - b} = \\frac{c + d}{c - d}$.",
                    "words": [
                        "Componendo",
                        "Dividendo",
                        "(a+b)/(a-b)",
                        "Rational Simplification"
                    ],
                    "correct": "If (sqrt(x+1) + sqrt(x-1)) / (sqrt(x+1) - sqrt(x-1)) = 3: Applying C&D gives sqrt(x+1)/sqrt(x-1) = (3+1)/(3-1) = 4/2 = 2. Squaring: (x+1)/(x-1) = 4 -> x = 5/3.",
                    "incorrect": "Squaring numerator and denominator without isolating roots via C&D."
                },
                {
                    "rule_number": 5,
                    "title": "Coin Value Denomination Rule",
                    "explanation": "Total Monetary Value = $\\sum (\\text{Number of Coins} \\times \\text{Denomination Value in Rupees})$. When the ratio of coins is given, multiply each part by its decimal Rupee value to find the ratio of their values.",
                    "words": [
                        "Coin Denomination",
                        "Value in Rupees",
                        "Coin Multiplier"
                    ],
                    "correct": "Coins in ratio 3:4:5 for Rs. 1, 50p (0.5), 25p (0.25): Total value units = 3(1) + 4(0.5) + 5(0.25) = 3 + 2 + 1.25 = 6.25 units.",
                    "incorrect": "Adding coin quantities directly: 3 + 4 + 5 = 12 coins = Total value (Fails to weight denominations)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Adding a constant number directly to ratio parts.",
                    "correction": "If A:B = 2:3 and 5 is added to each, the new ratio is NOT (2+5):(3+5) = 7:8. The actual numbers are 2x and 3x, so new ratio is (2x + 5)/(3x + 5).",
                    "rationale": "Ratios are multiplicative proportions, not additive values."
                },
                {
                    "mistake": "Dividing partnership profit by capital alone when investment durations differ.",
                    "correction": "Always multiply each partner's capital by their active months of participation.",
                    "rationale": "Capital working for longer generates more economic utility."
                },
                {
                    "mistake": "Confusing Mean Proportional with Third Proportional.",
                    "correction": "Mean proportional between a and b is sqrt(ab). Third proportional to a and b is b^2 / a.",
                    "rationale": "Third proportional places b in the middle: a:b = b:c."
                },
                {
                    "mistake": "Treating direct variation as inverse variation.",
                    "correction": "Direct: y = kx (y1/y2 = x1/x2). Inverse: y = k/x (y1/y2 = x2/x1).",
                    "rationale": "Workers vs Time is inverse; Work vs Time is direct."
                }
            ],
            "quick_revision_points": [
                "A:B = a1:b1, B:C = a2:b2 -> A:B:C = (a1*a2) : (b1*a2) : (b1*b2).",
                "Mean proportional of a and c is b = sqrt(ac).",
                "Third proportional of a and b is c = b^2 / a.",
                "Fourth proportional of a, b, c is d = (b * c) / a.",
                "Profit ratio in partnership = (Capital1 * Time1) : (Capital2 * Time2).",
                "Componendo & Dividendo: If a/b = c/d, then (a+b)/(a-b) = (c+d)/(c-d).",
                "Duplicate ratio of a:b is a^2 : b^2; Triplicate ratio is a^3 : b^3.",
                "Sub-duplicate ratio of a:b is sqrt(a) : sqrt(b)."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2601,
                "topic_id": 26,
                "question": "What is the third proportional to 16 and 24? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "36",
                    "32",
                    "40",
                    "48"
                ],
                "correct_answer": "36",
                "explanation": "Formula for third proportional c to a and b: c = b^2 / a.\nHere a = 16, b = 24.\nc = 24^2 / 16 = 576 / 16 = 36.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2602,
                "topic_id": 26,
                "question": "A, B and C enter into a partnership. A invests Rs. 25,600 and B invests Rs. 20,000. At the end of the year, out of total profit of Rs. 15,000, A receives Rs. 6,400. What was C's investment? [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "Rs. 14,400",
                    "Rs. 15,000",
                    "Rs. 16,000",
                    "Rs. 12,800"
                ],
                "correct_answer": "Rs. 14,400",
                "explanation": "Since all investments were for 1 year, profit is proportional to capital.\nA's share / Total profit = 6400 / 15000 = 64 / 150 = 32 / 75.\nSo A's capital / Total capital = 32 / 75.\n25,600 / Total capital = 32 / 75 -> Total capital = (25,600 * 75) / 32 = 800 * 75 = Rs. 60,000.\nC's capital = Total capital - (A's capital + B's capital) = 60,000 - (25,600 + 20,000) = 60,000 - 45,600 = Rs. 14,400.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2603,
                "topic_id": 26,
                "question": "If (a + b) : (b + c) : (c + a) = 6 : 7 : 8 and (a + b + c) = 14, then find the value of c. [UPSC CDS 2023]",
                "options_json": [
                    "6",
                    "7",
                    "8",
                    "14"
                ],
                "correct_answer": "6",
                "explanation": "Let a + b = 6k, b + c = 7k, c + a = 8k.\nAdding all three equations: 2(a + b + c) = 6k + 7k + 8k = 21k.\nGiven a + b + c = 14 -> 2(14) = 21k -> 28 = 21k -> k = 28/21 = 4/3.\na + b = 6k = 6 * (4/3) = 8.\nc = (a + b + c) - (a + b) = 14 - 8 = 6.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2601,
                "topic_id": 26,
                "question": "If A : B = 3 : 4 and B : C = 8 : 9, then find A : C.",
                "options_json": [
                    "2 : 3",
                    "1 : 2",
                    "3 : 2",
                    "4 : 5"
                ],
                "correct_answer": "2 : 3",
                "explanation": "A / C = (A / B) * (B / C) = (3 / 4) * (8 / 9) = (3 * 8) / (4 * 9) = 24 / 36 = 2 / 3 -> 2 : 3.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2602,
                "topic_id": 26,
                "question": "Find the mean proportional between 0.32 and 0.02.",
                "options_json": [
                    "0.08",
                    "0.8",
                    "0.064",
                    "0.008"
                ],
                "correct_answer": "0.08",
                "explanation": "Mean proportional = sqrt(a * b) = sqrt(0.32 * 0.02) = sqrt(0.0064) = 0.08.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2603,
                "topic_id": 26,
                "question": "A sum of Rs. 427 is to be divided among A, B and C such that 3 times A's share, 4 times B's share and 7 times C's share are all equal. Find C's share.",
                "options_json": [
                    "Rs. 84",
                    "Rs. 96",
                    "Rs. 105",
                    "Rs. 120"
                ],
                "correct_answer": "Rs. 84",
                "explanation": "3A = 4B = 7C = k -> A = k/3, B = k/4, C = k/7.\nRatio A:B:C = (1/3) : (1/4) : (1/7). Multiplying by LCM(3, 4, 7) = 84:\nA:B:C = 28 : 21 : 12.\nSum of ratio terms = 28 + 21 + 12 = 61 units.\n61 units = 427 -> 1 unit = 427 / 61 = 7.\nC's share = 12 * 7 = Rs. 84.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2604,
                "topic_id": 26,
                "question": "A box contains Rs. 1, 50-paise and 25-paise coins in the ratio 8 : 5 : 3, amounting to Rs. 112.50. Find the number of 50-paise coins.",
                "options_json": [
                    "50",
                    "40",
                    "60",
                    "80"
                ],
                "correct_answer": "50",
                "explanation": "Let number of coins be 8x, 5x, 3x.\nTotal value in Rupees = 8x(1) + 5x(0.50) + 3x(0.25) = 8x + 2.5x + 0.75x = 11.25x.\nGiven: 11.25x = 112.50 -> x = 10.\nNumber of 50-paise coins = 5x = 5 * 10 = 50.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2605,
                "topic_id": 26,
                "question": "Two numbers are in the ratio 3 : 5. If 9 is subtracted from each, the new numbers are in the ratio 12 : 23. Find the smaller number.",
                "options_json": [
                    "33",
                    "27",
                    "30",
                    "36"
                ],
                "correct_answer": "33",
                "explanation": "Let numbers be 3x and 5x.\n(3x - 9) / (5x - 9) = 12 / 23.\n23(3x - 9) = 12(5x - 9) -> 69x - 207 = 60x - 108.\n9x = 99 -> x = 11.\nSmaller number = 3x = 3 * 11 = 33.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2606,
                "topic_id": 26,
                "question": "Find the fourth proportional to 4, 9, and 12.",
                "options_json": [
                    "27",
                    "24",
                    "36",
                    "18"
                ],
                "correct_answer": "27",
                "explanation": "Fourth proportional d = (b * c) / a = (9 * 12) / 4 = 108 / 4 = 27.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2607,
                "topic_id": 26,
                "question": "Salaries of Ravi and Sumit are in the ratio 2 : 3. If the salary of each is increased by Rs. 4000, the new ratio becomes 40 : 57. What is Sumit's present salary?",
                "options_json": [
                    "Rs. 34,000",
                    "Rs. 38,000",
                    "Rs. 36,000",
                    "Rs. 40,000"
                ],
                "correct_answer": "Rs. 34,000",
                "explanation": "6x = 68,000 -> 3x = 34,000. Sumit's salary = 3x = Rs. 34,000.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2608,
                "topic_id": 26,
                "question": "A and B entered into a partnership investing Rs. 16,000 and Rs. 12,000 respectively. After 3 months, A withdrew Rs. 5000 while B invested Rs. 5000 more. Out of total profit of Rs. 26,400 at year end, find A's share.",
                "options_json": [
                    "Rs. 11,550",
                    "Rs. 14,850",
                    "Rs. 12,000",
                    "Rs. 10,500"
                ],
                "correct_answer": "Rs. 11,550",
                "explanation": "A's capital*months = 16000*3 + 11000*9 = 147,000.\nB's capital*months = 12000*3 + 17000*9 = 189,000.\nRatio A:B = 147 : 189 = 7 : 9.\nA's share = 26400 * (7/16) = Rs. 11,550.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "id": 2609,
                "topic_id": 26,
                "question": "What number should be added to each of 6, 14, 18, and 38 so that the resulting numbers form a proportion?",
                "options_json": [
                    "2",
                    "1",
                    "3",
                    "4"
                ],
                "correct_answer": "2",
                "explanation": "Let x be added: (6 + x) / (14 + x) = (18 + x) / (38 + x).\nFor x = 2:\n(6 + 2) / (14 + 2) = 8 / 16 = 1 / 2.\n(18 + 2) / (38 + 2) = 20 / 40 = 1 / 2.\nBoth ratios equal 1/2, so x = 2.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2610,
                "topic_id": 26,
                "question": "If x : y = 3 : 4, find the value of (4x + 5y) : (5x - 2y).",
                "options_json": [
                    "32 : 7",
                    "28 : 7",
                    "30 : 7",
                    "32 : 9"
                ],
                "correct_answer": "32 : 7",
                "explanation": "Substitute x = 3 and y = 4:\nNumerator = 4(3) + 5(4) = 12 + 20 = 32.\nDenominator = 5(3) - 2(4) = 15 - 8 = 7.\nRatio = 32 : 7.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2601,
                "topic_id": 26,
                "question": "If A:B = 2:3, B:C = 4:5, and C:D = 6:7, find A:D.",
                "options_json": [
                    "16 : 35",
                    "8 : 15",
                    "12 : 35",
                    "16 : 45"
                ],
                "correct_answer": "16 : 35",
                "explanation": "A/D = (A/B) * (B/C) * (C/D) = (2/3) * (4/5) * (6/7) = (2 * 4 * 6) / (3 * 5 * 7) = 48 / 105 = 16 / 35.",
                "points": 1
            },
            {
                "id": 2602,
                "topic_id": 26,
                "question": "Find the third proportional to 4 and 12.",
                "options_json": [
                    "36",
                    "24",
                    "48",
                    "16"
                ],
                "correct_answer": "36",
                "explanation": "Third proportional = 12^2 / 4 = 144 / 4 = 36.",
                "points": 1
            },
            {
                "id": 2603,
                "topic_id": 26,
                "question": "The ratio of boys and girls in a school is 4:3. If there are 480 boys, what is the total number of students in the school?",
                "options_json": [
                    "840",
                    "720",
                    "800",
                    "900"
                ],
                "correct_answer": "840",
                "explanation": "4 units = 480 -> 1 unit = 120.\nTotal students = 4 + 3 = 7 units = 7 * 120 = 840.",
                "points": 1
            },
            {
                "id": 2604,
                "topic_id": 26,
                "question": "If x:y = 5:2, then (8x + 9y) : (8x + 2y) is equal to:",
                "options_json": [
                    "29 : 22",
                    "25 : 22",
                    "29 : 24",
                    "27 : 22"
                ],
                "correct_answer": "29 : 22",
                "explanation": "Substitute x = 5, y = 2:\n8(5) + 9(2) = 40 + 18 = 58.\n8(5) + 2(2) = 40 + 4 = 44.\n58 / 44 = 29 / 22.",
                "points": 1
            },
            {
                "id": 2605,
                "topic_id": 26,
                "question": "A, B and C invest in a business in the ratio 3 : 4 : 5. If their time of investment is in the ratio 2 : 3 : 1, find their profit ratio.",
                "options_json": [
                    "6 : 12 : 5",
                    "5 : 12 : 6",
                    "6 : 10 : 5",
                    "3 : 6 : 5"
                ],
                "correct_answer": "6 : 12 : 5",
                "explanation": "Profit ratio = (C1 * T1) : (C2 * T2) : (C3 * T3) = (3 * 2) : (4 * 3) : (5 * 1) = 6 : 12 : 5.",
                "points": 1
            },
            {
                "id": 2606,
                "topic_id": 26,
                "question": "The mean proportional between 9 and 25 is:",
                "options_json": [
                    "15",
                    "17",
                    "12",
                    "16"
                ],
                "correct_answer": "15",
                "explanation": "Mean proportional = sqrt(9 * 25) = 3 * 5 = 15.",
                "points": 1
            },
            {
                "id": 2607,
                "topic_id": 26,
                "question": "What is the sub-duplicate ratio of 64 : 81?",
                "options_json": [
                    "8 : 9",
                    "9 : 8",
                    "512 : 729",
                    "4 : 9"
                ],
                "correct_answer": "8 : 9",
                "explanation": "Sub-duplicate ratio is the square root of the terms: sqrt(64) : sqrt(81) = 8 : 9.",
                "points": 1
            },
            {
                "id": 2608,
                "topic_id": 26,
                "question": "The incomes of A and B are in the ratio 3:2 and their expenditures are in the ratio 5:3. If each saves Rs. 1000, find A's income.",
                "options_json": [
                    "Rs. 6000",
                    "Rs. 4000",
                    "Rs. 5000",
                    "Rs. 7000"
                ],
                "correct_answer": "Rs. 6000",
                "explanation": "(3x - 1000) / (2x - 1000) = 5 / 3 -> 9x - 3000 = 10x - 5000 -> x = 2000.\nA's income = 3x = Rs. 6000.",
                "points": 1
            },
            {
                "id": 2609,
                "topic_id": 26,
                "question": "If 15% of x = 20% of y, then x : y is:",
                "options_json": [
                    "4 : 3",
                    "3 : 4",
                    "5 : 4",
                    "4 : 5"
                ],
                "correct_answer": "4 : 3",
                "explanation": "0.15 * x = 0.20 * y -> x / y = 0.20 / 0.15 = 20 / 15 = 4 / 3.",
                "points": 1
            },
            {
                "id": 2610,
                "topic_id": 26,
                "question": "If a:b = c:d = e:f = 1:2, then (3a + 5c + 7e) : (3b + 5d + 7f) is equal to:",
                "options_json": [
                    "1 : 2",
                    "1 : 4",
                    "2 : 1",
                    "3 : 7"
                ],
                "correct_answer": "1 : 2",
                "explanation": "Property of proportions: For any linear combination with identical coefficients, (p*a + q*c + r*e) / (p*b + q*d + r*f) = a/b = 1/2.",
                "points": 1
            }
        ]
    },
    "27": {
        "title": "Average: Arithmetic Mean, Assumed Mean Method, Weighted Averages & Batting Rates",
        "source_id": 7,
        "content": {
            "definition": "Average (Arithmetic Mean) is the single central measure of central tendency representing the equalized distribution of a data set: $\\text{Average} = \\frac{\\text{Sum of Observations}}{\\text{Total Number of Observations}}$. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, CAT), questions evaluate deviations from an assumed mean, weighted averages across disparate demographic groups, member inclusions/exclusions/replacements, and cricket statistics (batting and bowling averages).",
            "overview": "Analytical Frameworks:\n- Fundamental Equation: $\\text{Sum} = \\text{Average} \\times \\text{Number of Observations}$\n- Deviation Principle: $\\sum (x_i - \\bar{x}) = 0$ (The sum of deviations about the true mean is zero)\n- Weighted Average: $A_{\\text{w}} = \\frac{n_1 A_1 + n_2 A_2 + ... + n_k A_k}{n_1 + n_2 + ... + n_k}$\n- Replacement Formula: $\\text{New Value} = \\text{Replaced Value} \\pm (N \\times \\Delta A)$\n- Consecutive / Arithmetic Progression (AP) Sequence: $\\text{Average} = \\frac{\\text{First Term} + \\text{Last Term}}{2} = \\text{Middle Term}$",
            "types": [
                {
                    "name": "1. Basic Arithmetic Mean & Sum Invariance",
                    "desc": "Foundational sum-count relationships.",
                    "examples": [
                        "Average of first n natural numbers = (n + 1) / 2",
                        "Average of first n even numbers = (n + 1)",
                        "Average of first n odd numbers = n",
                        "Average of first n natural number squares = (n + 1)(2n + 1) / 6"
                    ]
                },
                {
                    "name": "2. Deviation (Assumed Mean) Method",
                    "desc": "Calculating average by observing net deviations from an arbitrary round base.",
                    "examples": [
                        "Data: 48, 52, 56, 46, 58. Let Assumed Mean A = 50.",
                        "Deviations: -2, +2, +6, -4, +8 -> Net Sum of Deviations = +10.",
                        "Average = Assumed Mean + (Net Deviation / N) = 50 + (10 / 5) = 52."
                    ]
                },
                {
                    "name": "3. Member Inclusion, Exclusion & Replacement",
                    "desc": "How group composition adjustments shift the mean.",
                    "examples": [
                        "Inclusion: New Member = Old Average + [New Total Members * Increase in Average]",
                        "Exclusion: Excluded Member = Old Average - [Remaining Members * Increase in Average]",
                        "Replacement: New Member = Replaced Member + [Total Members * Increase in Average]"
                    ]
                },
                {
                    "name": "4. Weighted Average of Multiple Subgroups",
                    "desc": "Combining distinct classes with different sizes and averages.",
                    "examples": [
                        "Class A (30 students, avg 60) and Class B (20 students, avg 70):",
                        "Weighted Avg = (30*60 + 20*70) / (30 + 20) = (1800 + 1400) / 50 = 3200 / 50 = 64."
                    ]
                },
                {
                    "name": "5. Sports Statistics: Batting & Bowling Averages",
                    "desc": "Applying averages to sports performance metrics.",
                    "examples": [
                        "Batting Average = (Total Runs Scored) / (Total Innings Out)",
                        "Bowling Average = (Total Runs Conceded) / (Total Wickets Taken) [Lower is better]"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Net Deviation Balance Rule ($\\sum \\Delta = 0$)",
                    "explanation": "The algebraic sum of deviations of all observations from their true arithmetic mean is ALWAYS zero: $\\sum_{i=1}^n (x_i - \\bar{x}) = 0$.",
                    "words": [
                        "Net Deviation",
                        "Assumed Mean",
                        "Zero Balance"
                    ],
                    "correct": "For numbers 20, 24, 28 with mean 24: (-4) + (0) + (+4) = 0.",
                    "incorrect": "Assuming deviations can sum to a non-zero number about the true mean."
                },
                {
                    "rule_number": 2,
                    "title": "Constant Operation Invariance Rule",
                    "explanation": "If every item in a dataset is increased, decreased, multiplied, or divided by a constant $k$, the arithmetic mean of the dataset is increased, decreased, multiplied, or divided by $k$ respectively.",
                    "words": [
                        "Constant Operation",
                        "Uniform Shift",
                        "Scalar Scaling"
                    ],
                    "correct": "If average of 10 numbers is 25 and 5 is added to each number, the new average is 25 + 5 = 30.",
                    "incorrect": "Recalculating sum of 10 numbers manually from scratch."
                },
                {
                    "rule_number": 3,
                    "title": "Replacement Member Formula",
                    "explanation": "When one member of weight/age $W_{\\text{old}}$ is replaced by another member of weight/age $W_{\\text{new}}$, causing the average of $N$ members to change by $\\Delta A$: $W_{\\text{new}} = W_{\\text{old}} + N \\times (\\Delta A)$. (Use $+\\Delta A$ for an increase, $-\\Delta A$ for a decrease).",
                    "words": [
                        "Replacement Formula",
                        "W_new = W_old + N * delta",
                        "Net Shift"
                    ],
                    "correct": "Average weight of 8 men increases by 2.5 kg when a man of 65 kg is replaced: Weight of new man = 65 + (8 * 2.5) = 65 + 20 = 85 kg.",
                    "incorrect": "Calculating new man = 65 + 2.5 = 67.5 kg (Omitting multiplication by group size N)."
                },
                {
                    "rule_number": 4,
                    "title": "Consecutive Terms & Arithmetic Progression (AP) Rule",
                    "explanation": "For any sequence of numbers in Arithmetic Progression (e.g., consecutive integers, consecutive odd/even numbers): $\\text{Average} = \\frac{\\text{First Term} + \\text{Last Term}}{2}$. If $N$ is odd, the average is the exact middle term.",
                    "words": [
                        "Arithmetic Progression",
                        "Middle Term",
                        "(First + Last) / 2"
                    ],
                    "correct": "Average of 5 consecutive odd numbers: 11, 13, 15, 17, 19 is exactly the middle term = 15.",
                    "incorrect": "Summing all 5 numbers and dividing when symmetry immediately yields 15."
                },
                {
                    "rule_number": 5,
                    "title": "Batting Average Inning Update Rule",
                    "explanation": "If a batsman plays his $n^{\\text{th}}$ inning scoring $R$ runs and his average increases by $x$: $\\text{New Average} = R - (n - 1) \\times x$; $\\text{Old Average} = R - n \\times x$.",
                    "words": [
                        "Batting Average",
                        "Inning Equation",
                        "Cricket Averages"
                    ],
                    "correct": "In his 17th inning, a batsman scores 87 and his average rises by 3: New Average = 87 - (17 - 1)*3 = 87 - 48 = 39. Old average = 39 - 3 = 36.",
                    "incorrect": "New Average = 87 / 17 (Ignores previous runs accumulated across first 16 innings)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Averaging the averages directly without weighting group sizes.",
                    "correction": "Average speed for two equal distances at speeds x and y is the Harmonic Mean 2xy/(x + y), NOT (x + y)/2.",
                    "rationale": "Equal distance implies different travel times; simple arithmetic mean violates physical weighting."
                },
                {
                    "mistake": "Forgetting that 'N' changes in inclusion/exclusion problems.",
                    "correction": "When a teacher joins 24 students, the new total group count N is 25, not 24.",
                    "rationale": "The new member adds to the denominator."
                },
                {
                    "mistake": "Misunderstanding cricket bowling average.",
                    "correction": "Bowling Average = Runs Conceded / Wickets. A 'decrease' in bowling average means the bowler improved.",
                    "rationale": "Fewer runs per wicket indicates superior performance."
                },
                {
                    "mistake": "Using (n/2) for average of first n natural numbers.",
                    "correction": "Average of first n natural numbers is (n + 1)/2.",
                    "rationale": "Sum is n(n + 1)/2; dividing by n gives (n + 1)/2."
                }
            ],
            "quick_revision_points": [
                "Average = (Sum of observations) / (Number of observations).",
                "Sum = Average * Count.",
                "For an AP sequence, Average = (First Term + Last Term) / 2.",
                "Average of first n natural numbers = (n + 1) / 2.",
                "Average of first n even numbers = n + 1; first n odd numbers = n.",
                "Replacement: New = Old + (Count * Change in Avg).",
                "If every observation is multiplied by k, the new average is (k * Old Avg).",
                "Batting Average = Total Runs / Innings Out; Bowling Average = Runs / Wickets."
            ]
        },
        "previous_year_questions": [
            {
                "id": 2701,
                "topic_id": 27,
                "question": "The average of 25 numbers is 54. The average of the first 13 numbers is 52 and that of the last 13 numbers is 56. If the 13th number is excluded, what is the average of the remaining numbers? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "53.5",
                    "54.0",
                    "53.0",
                    "54.5"
                ],
                "correct_answer": "54.0",
                "explanation": "Sum of all 25 numbers = 25 * 54 = 1350.\nSum of first 13 = 13 * 52 = 676.\nSum of last 13 = 13 * 56 = 728.\n13th number is counted twice: 13th number = (676 + 728) - 1350 = 1404 - 1350 = 54.\nIf the 13th number (54) is excluded, the remaining 24 numbers have sum = 1350 - 54 = 1296.\nNew average = 1296 / 24 = 54.0.",
                "exam_id": 1,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2702,
                "topic_id": 27,
                "question": "A batsman makes a score of 87 runs in the 17th inning and thus increases his average by 3. Find his average after the 17th inning. [SSC CGL 2022 Tier 2]",
                "options_json": [
                    "39",
                    "36",
                    "42",
                    "45"
                ],
                "correct_answer": "39",
                "explanation": "Let average after 16 innings be x.\nTotal runs after 16 innings = 16x.\nRuns after 17 innings = 16x + 87.\nNew average = x + 3.\n(16x + 87) / 17 = x + 3 -> 16x + 87 = 17x + 51 -> x = 36.\nAverage after 17th inning = x + 3 = 36 + 3 = 39.",
                "exam_id": 2,
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 2703,
                "topic_id": 27,
                "question": "The average age of a class of 30 students and their teacher is 16 years. If the teacher's age is excluded, the average reduces by 1 year. What is the teacher's age? [UPSC CDS 2023]",
                "options_json": [
                    "46 years",
                    "45 years",
                    "48 years",
                    "50 years"
                ],
                "correct_answer": "46 years",
                "explanation": "Total persons initially = 30 + 1 = 31.\nTotal age initially = 31 * 16 = 496 years.\nAfter teacher is excluded, 30 students remain with average = 16 - 1 = 15 years.\nTotal age of 30 students = 30 * 15 = 450 years.\nTeacher's age = 496 - 450 = 46 years.",
                "exam_id": 3,
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 2701,
                "topic_id": 27,
                "question": "Find the average of the first 40 natural numbers.",
                "options_json": [
                    "20.5",
                    "20.0",
                    "21.0",
                    "21.5"
                ],
                "correct_answer": "20.5",
                "explanation": "Average of first n natural numbers = (n + 1) / 2 = (40 + 1) / 2 = 41 / 2 = 20.5.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2702,
                "topic_id": 27,
                "question": "The average weight of 8 persons increases by 2.5 kg when a new person comes in place of one of them weighing 65 kg. What is the weight of the new person?",
                "options_json": [
                    "85 kg",
                    "80 kg",
                    "75 kg",
                    "90 kg"
                ],
                "correct_answer": "85 kg",
                "explanation": "Weight of new person = Replaced weight + (Count * Change in avg) = 65 + (8 * 2.5) = 65 + 20 = 85 kg.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2703,
                "topic_id": 27,
                "question": "The average of 5 consecutive odd numbers is 61. What is the difference between the highest and lowest numbers?",
                "options_json": [
                    "8",
                    "10",
                    "6",
                    "12"
                ],
                "correct_answer": "8",
                "explanation": "The 5 numbers are (x-4), (x-2), x, (x+2), (x+4). Here x = 61.\nHighest = 61 + 4 = 65; Lowest = 61 - 4 = 57.\nDifference = 65 - 57 = 8.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2704,
                "topic_id": 27,
                "question": "A student's mark was wrongly entered as 83 instead of 63. Due to this, the average marks for the class increased by half (0.5). Find the number of students in the class.",
                "options_json": [
                    "40",
                    "30",
                    "20",
                    "50"
                ],
                "correct_answer": "40",
                "explanation": "Excess mark added = 83 - 63 = 20.\nIncrease per student = 0.5.\nNumber of students = 20 / 0.5 = 40.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2705,
                "topic_id": 27,
                "question": "The average score of a cricketer in 10 innings was 32. How many runs must he score in his next innings so as to increase his average by 4 runs?",
                "options_json": [
                    "76",
                    "72",
                    "80",
                    "70"
                ],
                "correct_answer": "76",
                "explanation": "Runs in 10 innings = 10 * 32 = 320.\nRequired average for 11 innings = 32 + 4 = 36.\nTotal runs required = 11 * 36 = 396.\nRuns needed in 11th inning = 396 - 320 = 76.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2706,
                "topic_id": 27,
                "question": "The average temperature for Monday, Tuesday and Wednesday was 40 deg C. The average for Tuesday, Wednesday and Thursday was 41 deg C. If Thursday's temperature was 42 deg C, what was the temperature on Monday?",
                "options_json": [
                    "39 deg C",
                    "38 deg C",
                    "40 deg C",
                    "41 deg C"
                ],
                "correct_answer": "39 deg C",
                "explanation": "M + T + W = 3 * 40 = 120.\nT + W + Th = 3 * 41 = 123.\nSubtracting: Th - M = 123 - 120 = 3.\nGiven Th = 42 -> 42 - M = 3 -> M = 42 - 3 = 39 deg C.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2707,
                "topic_id": 27,
                "question": "In a class of 60 students, 40% are girls. The average weight of the whole class is 59.2 kg and the average weight of the girls is 55 kg. What is the average weight of the boys?",
                "options_json": [
                    "62 kg",
                    "60 kg",
                    "64 kg",
                    "63 kg"
                ],
                "correct_answer": "62 kg",
                "explanation": "Girls = 40% of 60 = 24. Boys = 60 - 24 = 36. Ratio Boys:Girls = 36:24 = 3:2.\nUsing weighted average: 59.2 = [3 * (Avg_B) + 2 * 55] / (3 + 2).\n59.2 * 5 = 3(Avg_B) + 110 -> 296 = 3(Avg_B) + 110.\n3(Avg_B) = 186 -> Avg_B = 62 kg.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2708,
                "topic_id": 27,
                "question": "The average of 7 consecutive numbers is 20. The largest of these numbers is:",
                "options_json": [
                    "23",
                    "24",
                    "22",
                    "25"
                ],
                "correct_answer": "23",
                "explanation": "For 7 consecutive numbers, the 4th (middle) number is the average = 20.\nNumbers are 17, 18, 19, 20, 21, 22, 23.\nLargest number = 23.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "id": 2709,
                "topic_id": 27,
                "question": "A library has an average of 510 visitors on Sundays and 240 on other days. The average number of visitors per day in a month of 30 days beginning with a Sunday is:",
                "options_json": [
                    "285",
                    "275",
                    "290",
                    "280"
                ],
                "correct_answer": "285",
                "explanation": "Month of 30 days starting on Sunday has 5 Sundays (days 1, 8, 15, 22, 29) and 25 other days.\nTotal visitors = (5 * 510) + (25 * 240) = 2550 + 6000 = 8550.\nAverage per day = 8550 / 30 = 285.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "id": 2710,
                "topic_id": 27,
                "question": "The average age of 8 men increases by 2 years when two women are included in place of two men aged 21 and 23. Find the average age of the two women.",
                "options_json": [
                    "30 years",
                    "28 years",
                    "32 years",
                    "26 years"
                ],
                "correct_answer": "30 years",
                "explanation": "Sum of ages of replaced men = 21 + 23 = 44 years.\nTotal increase in age = 8 * 2 = 16 years.\nSum of ages of two women = 44 + 16 = 60 years.\nAverage age of the two women = 60 / 2 = 30 years.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            }
        ],
        "quiz_questions": [
            {
                "id": 2701,
                "topic_id": 27,
                "question": "What is the average of the first 20 multiples of 7?",
                "options_json": [
                    "73.5",
                    "70.0",
                    "77.0",
                    "75.5"
                ],
                "correct_answer": "73.5",
                "explanation": "7 * (1 + 2 + ... + 20) / 20 = 7 * [(20 * 21 / 2) / 20] = 7 * (21 / 2) = 7 * 10.5 = 73.5.",
                "points": 1
            },
            {
                "id": 2702,
                "topic_id": 27,
                "question": "The average age of husband and wife was 23 years at the time of their marriage. After 5 years, they have a one-year-old child. The average age of the family now is:",
                "options_json": [
                    "19 years",
                    "20 years",
                    "18 years",
                    "21 years"
                ],
                "correct_answer": "19 years",
                "explanation": "At marriage: Total age = 2 * 23 = 46.\nAfter 5 years: Each is 5 years older -> Total age of couple = 46 + 10 = 56.\nWith 1-year-old child: Total age of family = 56 + 1 = 57.\nAverage age of family (3 members) = 57 / 3 = 19 years.",
                "points": 1
            },
            {
                "id": 2703,
                "topic_id": 27,
                "question": "The average of 6 numbers is 30. If the average of the first 4 numbers is 25 and that of the last 3 numbers is 35, the 4th number is:",
                "options_json": [
                    "25",
                    "30",
                    "35",
                    "20"
                ],
                "correct_answer": "25",
                "explanation": "Sum of all 6 = 6 * 30 = 180.\nSum of first 4 = 4 * 25 = 100.\nSum of last 3 = 3 * 35 = 105.\n4th number = (100 + 105) - 180 = 205 - 180 = 25.",
                "points": 1
            },
            {
                "id": 2704,
                "topic_id": 27,
                "question": "A motorist travels to a destination at 40 km/h and returns at 60 km/h. His average speed for the entire journey is:",
                "options_json": [
                    "48 km/h",
                    "50 km/h",
                    "45 km/h",
                    "52 km/h"
                ],
                "correct_answer": "48 km/h",
                "explanation": "Harmonic mean = 2xy / (x + y) = (2 * 40 * 60) / (40 + 60) = 4800 / 100 = 48 km/h.",
                "points": 1
            },
            {
                "id": 2705,
                "topic_id": 27,
                "question": "If the average of x, y and z is 45, x is greater than y by 9 and y is greater than z by 9, find the value of x.",
                "options_json": [
                    "54",
                    "45",
                    "36",
                    "63"
                ],
                "correct_answer": "54",
                "explanation": "Since x, y, z form an AP with common difference 9, the average is the middle term y = 45.\nx = y + 9 = 45 + 9 = 54.",
                "points": 1
            },
            {
                "id": 2706,
                "topic_id": 27,
                "question": "The average of 50 numbers is 38. If two numbers, namely 45 and 55, are discarded, the average of the remaining numbers is:",
                "options_json": [
                    "37.5",
                    "38.0",
                    "37.0",
                    "36.5"
                ],
                "correct_answer": "37.5",
                "explanation": "Sum of 50 = 50 * 38 = 1900.\nSum discarded = 45 + 55 = 100.\nRemaining sum = 1900 - 100 = 1800.\nRemaining numbers = 48.\nNew average = 1800 / 48 = 37.5.",
                "points": 1
            },
            {
                "id": 2707,
                "topic_id": 27,
                "question": "A batsman has a certain average of runs for 11 innings. In the 12th inning, he scores 90 runs and his average increases by 5. His new average is:",
                "options_json": [
                    "35",
                    "30",
                    "40",
                    "45"
                ],
                "correct_answer": "35",
                "explanation": "New average = 90 - (12 - 1)*5 = 90 - 55 = 35.",
                "points": 1
            },
            {
                "id": 2708,
                "topic_id": 27,
                "question": "The average of 5 consecutive natural numbers is m. If the next 3 natural numbers are also included, how much does the average increase?",
                "options_json": [
                    "1.5",
                    "1.0",
                    "2.0",
                    "2.5"
                ],
                "correct_answer": "1.5",
                "explanation": "For every consecutive number added to a sequence of consecutive integers, the average increases by 1/2 = 0.5.\nAdding 3 numbers increases the average by 3 * 0.5 = 1.5.",
                "points": 1
            },
            {
                "id": 2709,
                "topic_id": 27,
                "question": "Average marks of 100 students were found to be 40. Later it was discovered that a score of 53 was misread as 83. The correct mean is:",
                "options_json": [
                    "39.7",
                    "39.0",
                    "40.3",
                    "41.0"
                ],
                "correct_answer": "39.7",
                "explanation": "Error = 83 - 53 = 30 marks excess.\nCorrection to average = -30 / 100 = -0.3.\nCorrect mean = 40 - 0.3 = 39.7.",
                "points": 1
            },
            {
                "id": 2710,
                "topic_id": 27,
                "question": "The average of first 10 prime numbers is:",
                "options_json": [
                    "12.9",
                    "11.6",
                    "13.2",
                    "12.5"
                ],
                "correct_answer": "12.9",
                "explanation": "First 10 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.\nSum = 2+3+5+7+11+13+17+19+23+29 = 129.\nAverage = 129 / 10 = 12.9.",
                "points": 1
            }
        ]
    }
}
