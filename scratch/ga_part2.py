# ga_part2.py
GA_PART2_DATA = {
    "56": {
        "title": "Economy: Macroeconomic Principles, Monetary Policy, Inflation & National Income",
        "source_id": 7,
        "content": {
            "definition": "Economics in competitive examinations (UPSC, SSC CGL Tier 1/2, IBPS PO, RBI Grade B, State PSCs) examines macroeconomic stability, fiscal administration, monetary policy transmission by the Reserve Bank of India, national income accounting, banking sector health, inflation dynamics, and development planning from Five-Year Plans to NITI Aayog.",
            "overview": "Fundamental Macroeconomic Frameworks:\n- National Income Accounting: Gross Domestic Product (GDP, total monetary value of goods & services produced within domestic territory in a year); Gross National Product ($GNP = GDP + \\text{NFIA}$); Net Domestic Product ($NDP = GDP - \\text{Depreciation}$); Net National Product ($NNP = GNP - \\text{Depreciation}$); Per Capita Income = $NNP / \\text{Total Population}$\n- Monetary Policy Instruments (RBI Act 1934, MPC): Quantitative tools (Repo Rate, Reverse Repo Rate, Standing Deposit Facility / SDF, Cash Reserve Ratio / CRR, Statutory Liquidity Ratio / SLR, Bank Rate, Open Market Operations / OMO)\n- Inflation Indices: Consumer Price Index (CPI, base year 2012, compiled by NSO, used by RBI for inflation targeting $4\\% \\pm 2\\%$); Wholesale Price Index (WPI, base year 2011-12, compiled by Office of Economic Adviser)\n- Fiscal Policy & Budgeting: Revenue Deficit, Fiscal Deficit (Total Expenditure - Total Receipts excluding borrowings), Primary Deficit (Fiscal Deficit - Interest Payments)\n- Planning in India: Planning Commission (1950\u20132014) and 12 Five-Year Plans; NITI Aayog established on 1 January 2015 as a policy think tank",
            "types": [
                {
                    "name": "1. National Income Aggregates & Output Metrics",
                    "desc": "Relationships connecting GDP at Factor Cost, Market Price, Depreciation, and Net Indirect Taxes.",
                    "examples": [
                        "GDP at Market Price = GDP at Factor Cost + Indirect Taxes - Subsidies",
                        "Real GDP (adjusted for inflation using GDP deflator) vs Nominal GDP"
                    ]
                },
                {
                    "name": "2. RBI Monetary Policy & Liquidity Adjustment",
                    "desc": "Policy interest rates and statutory bank reserve obligations.",
                    "examples": [
                        "Repo Rate: The interest rate at which RBI lends short-term liquidity to commercial banks against government securities",
                        "CRR: Percentage of Net Demand and Time Liabilities (NDTL) commercial banks must hold in cash reserves with RBI"
                    ]
                },
                {
                    "name": "3. Inflation Dynamics & Price Measurement",
                    "desc": "Demand-pull inflation, cost-push inflation, stagflation, and index composition.",
                    "examples": [
                        "Stagflation: Unfavorable economic phenomenon characterized by stagnant growth, high unemployment, and high inflation",
                        "Headline Inflation (comprehensive basket) vs Core Inflation (excluding volatile food and energy)"
                    ]
                },
                {
                    "name": "4. Fiscal Administration & Government Budgeting",
                    "desc": "Direct taxes (Income tax, Corporate tax) vs Indirect taxes (GST), deficit formulas, and FRBM Act.",
                    "examples": [
                        "Fiscal Deficit = Total Budget Expenditure - (Revenue Receipts + Non-debt Capital Receipts)",
                        "Primary Deficit = Fiscal Deficit - Interest Payments on prior sovereign debt"
                    ]
                },
                {
                    "name": "5. Five-Year Plans & Economic Planning Architecture",
                    "desc": "Historic 5-year plans, Harrod-Domar model, Mahalanobis heavy industry model, and NITI Aayog.",
                    "examples": [
                        "1st Five-Year Plan (1951-56): Harrod-Domar Model focused on agriculture and irrigation",
                        "2nd Five-Year Plan (1956-61): PC Mahalanobis Model emphasizing rapid industrialization and heavy industries"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "National Income Depreciation and Tax Formula",
                    "explanation": "Remember two fundamental identities:\n1. **Net = Gross - Depreciation** (e.g. $NDP = GDP - \\text{Depreciation}$; $NNP = GNP - \\text{Depreciation}$).\n2. **Market Price = Factor Cost + Net Indirect Taxes (NIT)** (where $NIT = \\text{Indirect Taxes} - \\text{Subsidies}$).\nNational Income ($NI$) in economics strictly refers to **NNP at Factor Cost**.",
                    "words": [
                        "Net = Gross - Depreciation",
                        "Market Price = Factor Cost + NIT",
                        "National Income = NNP at FC"
                    ],
                    "correct": "National Income is defined as Net National Product at Factor Cost (NNP at FC).",
                    "incorrect": "Equating National Income directly with Gross Domestic Product at Market Price."
                },
                {
                    "rule_number": 2,
                    "title": "Inflation Control via Monetary Tightening",
                    "explanation": "To curb high inflation in the economy, the RBI implements a **tight/dear monetary policy**:\n- **Hikes Repo Rate**: Borrowing becomes costlier for commercial banks, leading to higher retail lending rates, reduced credit supply, and subdued consumer demand.\n- **Increases CRR & SLR**: Absorbs excess liquidity from the banking sector.\n- Sells Government Securities via Open Market Operations (OMO).",
                    "words": [
                        "Fight Inflation",
                        "Hike Repo Rate",
                        "Increase CRR",
                        "Contract Liquidity"
                    ],
                    "correct": "When inflation is high, the RBI raises the Repo Rate to make credit expensive and absorb liquidity.",
                    "incorrect": "Reducing Repo Rate to fight inflation (cutting repo rate stimulates spending and increases inflation!)."
                },
                {
                    "rule_number": 3,
                    "title": "Stagflation Definition Rule",
                    "explanation": "Stagflation is an abnormal macroeconomic condition consisting of a lethal combination of THREE simultaneous factors:\n1. **Stagnant economic growth** (or GDP contraction)\n2. **High unemployment**\n3. **Persistently high inflation**.\nIt defies the traditional Phillips Curve relationship which posited an inverse link between inflation and unemployment.",
                    "words": [
                        "Stagflation",
                        "Stagnant Growth + High Unemployment + High Inflation",
                        "Defies Phillips Curve"
                    ],
                    "correct": "Stagflation combines slow economic growth, high unemployment, and rising inflation.",
                    "incorrect": "Confusing stagflation with deflation (falling prices)."
                },
                {
                    "rule_number": 4,
                    "title": "Primary Deficit = Fiscal Deficit - Interest Payments",
                    "explanation": "- **Fiscal Deficit**: Total borrowing requirements of the government during a financial year.\n- **Primary Deficit**: Fiscal Deficit minus Interest Payments ($PD = FD - IP$). It reflects the government's current-year fiscal stance excluding the burden of past debts.\n*If Primary Deficit is zero, it means total borrowing is used solely to pay interest on past sovereign debt!*",
                    "words": [
                        "Primary Deficit = Fiscal Deficit - Interest Payments",
                        "Current Fiscal Stance"
                    ],
                    "correct": "Primary Deficit indicates the government's borrowing needs excluding past interest payment liabilities.",
                    "incorrect": "Subtracting subsidies instead of interest payments."
                },
                {
                    "rule_number": 5,
                    "title": "CPI vs WPI Institutional and Basket Distinction",
                    "explanation": "- **CPI (Consumer Price Index)**: Base year 2012; compiled by NSO (MoSPI); measures retail inflation at consumer level; includes services; used by the RBI Monetary Policy Committee (target: $4\\% \\pm 2\\%$).\n- **WPI (Wholesale Price Index)**: Base year 2011-12; compiled by Office of Economic Adviser (DPIIT); measures wholesale goods transactions; DOES NOT INCLUDE SERVICES!",
                    "words": [
                        "CPI (NSO, Services Included, RBI Target 4%)",
                        "WPI (DPIIT, No Services)"
                    ],
                    "correct": "The RBI uses CPI Combined as the official metric for inflation targeting.",
                    "incorrect": "Believing WPI includes service sector inflation."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Thinking National Income equals GDP.",
                    "correction": "National Income is technically Net National Product at Factor Cost (NNP at FC).",
                    "rationale": "Gross includes depreciation, and Domestic excludes net factor income from abroad."
                },
                {
                    "mistake": "Believing reducing interest rates controls inflation.",
                    "correction": "Raising interest rates (hiking Repo Rate) is what cools down inflation by curbing borrowing and aggregate demand.",
                    "rationale": "Lowering rates injects liquidity and increases inflation."
                },
                {
                    "mistake": "Assuming WPI measures service inflation.",
                    "correction": "WPI measures only physical manufactured, primary, and fuel goods. Services are measured exclusively by CPI.",
                    "rationale": "High-frequency question in economic aptitude tests."
                },
                {
                    "mistake": "Confusing NITI Aayog with a constitutional or statutory body.",
                    "correction": "NITI Aayog is a non-constitutional, non-statutory body created via a Cabinet Executive Resolution on 1 January 2015.",
                    "rationale": "Standard constitutional/administrative distinction."
                }
            ],
            "quick_revision_points": [
                "National Income = NNP at Factor Cost (NNP at FC = GNP - Depreciation - Net Indirect Taxes)",
                "Repo Rate: Rate at which RBI lends short-term to banks; Reverse Repo: Rate at which RBI absorbs funds",
                "Inflation target in India: 4% with a tolerance band of +/- 2% (2% to 6%) measured by CPI Combined",
                "Fiscal Deficit = Total Expenditure - Total Receipts excluding borrowings",
                "Primary Deficit = Fiscal Deficit - Interest Payments",
                "NITI Aayog (National Institution for Transforming India): Formed 1 Jan 2015, Chairperson is Prime Minister",
                "Mahalanobis Model was the basis of the 2nd Five-Year Plan (1956-61)",
                "Gresham's Law: 'Bad money drives out good money' from circulation"
            ]
        },
        "previous_year_questions": [
            {
                "id": 5601,
                "topic_id": 56,
                "exam_id": 1,
                "question": "Which of the following is technically termed as 'National Income' in economic accounting? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Net National Product at Factor Cost (NNP at FC)",
                    "Gross Domestic Product at Market Price (GDP at MP)",
                    "Net Domestic Product at Factor Cost (NDP at FC)",
                    "Gross National Product at Factor Cost (GNP at FC)"
                ],
                "correct_answer": "Net National Product at Factor Cost (NNP at FC)",
                "explanation": "In national income accounting, National Income (NI) is formally defined as the Net National Product at Factor Cost (NNP at FC), representing the total net earnings of all factors of production residing in the nation.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5602,
                "topic_id": 56,
                "exam_id": 1,
                "question": "The rate at which the Reserve Bank of India lends short-term money to commercial banks against government securities is called: [IBPS PO Prelims 2022]",
                "options_json": [
                    "Repo Rate",
                    "Reverse Repo Rate",
                    "Bank Rate",
                    "Cash Reserve Ratio"
                ],
                "correct_answer": "Repo Rate",
                "explanation": "The Repo Rate (Repurchase Option Rate) is the key policy interest rate at which the central bank (RBI) lends money to commercial banks against approved government collateral in case of liquidity shortages.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5603,
                "topic_id": 56,
                "exam_id": 1,
                "question": "On which date was the NITI Aayog (National Institution for Transforming India) officially established, replacing the Planning Commission? [RRB NTPC 2022]",
                "options_json": [
                    "1 January 2015",
                    "15 August 2014",
                    "1 April 2015",
                    "26 January 2015"
                ],
                "correct_answer": "1 January 2015",
                "explanation": "NITI Aayog was formed on 1 January 2015 via an executive resolution of the Union Cabinet to serve as a policy think tank fostering cooperative federalism, replacing the 65-year-old Planning Commission.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 5601,
                "topic_id": 56,
                "question": "What is the formula for calculating Net Domestic Product (NDP)?",
                "options_json": [
                    "GDP - Depreciation",
                    "GNP - Depreciation",
                    "GDP + Net Factor Income from Abroad",
                    "GDP + Subsidies"
                ],
                "correct_answer": "GDP - Depreciation",
                "explanation": "Net Domestic Product is obtained by subtracting the consumption of fixed capital (Depreciation) from Gross Domestic Product (NDP = GDP - Depreciation).",
                "points": 1
            },
            {
                "id": 5602,
                "topic_id": 56,
                "question": "What is the official inflation target mandated for the RBI Monetary Policy Committee?",
                "options_json": [
                    "4% with a tolerance band of \u00b1 2%",
                    "5% with a tolerance band of \u00b1 1%",
                    "3% with a tolerance band of \u00b1 2%",
                    "6% fixed"
                ],
                "correct_answer": "4% with a tolerance band of \u00b1 2%",
                "explanation": "Under the Flexible Inflation Targeting framework, the target is 4% CPI inflation with an upper tolerance limit of 6% and a lower tolerance limit of 2%.",
                "points": 1
            },
            {
                "id": 5603,
                "topic_id": 56,
                "question": "What does 'Stagflation' describe in macroeconomics?",
                "options_json": [
                    "High inflation combined with high unemployment and stagnant economic growth",
                    "Low inflation with rapid growth",
                    "Falling prices across all sectors",
                    "Zero unemployment with high inflation"
                ],
                "correct_answer": "High inflation combined with high unemployment and stagnant economic growth",
                "explanation": "Stagflation is the paradoxical combination of stagnant economic output, high unemployment, and persistent inflation.",
                "points": 1
            },
            {
                "id": 5604,
                "topic_id": 56,
                "question": "The Second Five-Year Plan (1956\u20131961) of India was based on which economic model?",
                "options_json": [
                    "Mahalanobis Model",
                    "Harrod-Domar Model",
                    "Gadgil Yojana",
                    "Rao-Manmohan Model"
                ],
                "correct_answer": "Mahalanobis Model",
                "explanation": "The 2nd Five-Year Plan was formulated by Professor Prasanta Chandra Mahalanobis, emphasizing rapid industrialization with a focus on heavy industries.",
                "points": 1
            },
            {
                "id": 5605,
                "topic_id": 56,
                "question": "What is subtracted from the Fiscal Deficit to calculate the Primary Deficit?",
                "options_json": [
                    "Interest Payments",
                    "Subsidies",
                    "Disinvestment receipts",
                    "Tax revenues"
                ],
                "correct_answer": "Interest Payments",
                "explanation": "Primary Deficit = Fiscal Deficit - Interest Payments. It indicates the current year's budgetary imbalance excluding past debt obligations.",
                "points": 1
            },
            {
                "id": 5606,
                "topic_id": 56,
                "question": "Who is the ex-officio Chairperson of the NITI Aayog?",
                "options_json": [
                    "Prime Minister of India",
                    "Finance Minister",
                    "President of India",
                    "Governor of RBI"
                ],
                "correct_answer": "Prime Minister of India",
                "explanation": "The Prime Minister of India serves as the ex-officio Chairperson of NITI Aayog.",
                "points": 1
            },
            {
                "id": 5607,
                "topic_id": 56,
                "question": "What is the base year currently used for calculating the Consumer Price Index (CPI) in India?",
                "options_json": [
                    "2012",
                    "2011-12",
                    "2004-05",
                    "2015"
                ],
                "correct_answer": "2012",
                "explanation": "The base year for CPI (Combined, Urban, Rural) compiled by the National Statistical Office (NSO) is 2012.",
                "points": 1
            },
            {
                "id": 5608,
                "topic_id": 56,
                "question": "Which economic law states that 'Bad money drives out good money' from circulation?",
                "options_json": [
                    "Gresham's Law",
                    "Say's Law",
                    "Okun's Law",
                    "Engel's Law"
                ],
                "correct_answer": "Gresham's Law",
                "explanation": "Gresham's Law, named after Sir Thomas Gresham, posits that if two types of money circulate with equal legal face value, the undervalued/debased currency will drive the higher intrinsic value currency out of circulation.",
                "points": 1
            },
            {
                "id": 5609,
                "topic_id": 56,
                "question": "What percentage of a commercial bank's deposits must be kept with the RBI as Cash Reserve Ratio (CRR)?",
                "options_json": [
                    "A specified percentage in cash without interest earnings",
                    "A percentage in gold",
                    "A percentage in government bonds",
                    "Zero percentage"
                ],
                "correct_answer": "A specified percentage in cash without interest earnings",
                "explanation": "CRR is the share of Net Demand and Time Liabilities (NDTL) that banks must deposit with the RBI in cash, on which no interest is earned.",
                "points": 1
            },
            {
                "id": 5610,
                "topic_id": 56,
                "question": "Which curve illustrates the theoretical relationship between tax rates and resulting tax revenue collected?",
                "options_json": [
                    "Laffer Curve",
                    "Phillips Curve",
                    "Lorenz Curve",
                    "Kuznets Curve"
                ],
                "correct_answer": "Laffer Curve",
                "explanation": "The Laffer Curve, conceived by economist Arthur Laffer, depicts how tax revenues increase with rising tax rates up to an optimal rate, beyond which higher rates discourage work and shrink revenue.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 5601,
                "topic_id": 56,
                "question": "Who was the first Governor of the Reserve Bank of India in 1935?",
                "options_json": [
                    "Sir Osborne Smith",
                    "C.D. Deshmukh",
                    "Sir James Braid Taylor",
                    "Dr. Manmohan Singh"
                ],
                "correct_answer": "Sir Osborne Smith",
                "explanation": "Sir Osborne Smith was the first Governor of the RBI (1935\u20131937). Sir C.D. Deshmukh was the first Indian Governor of the RBI (appointed in 1943).",
                "points": 1
            },
            {
                "id": 5602,
                "topic_id": 56,
                "question": "What does a Lorenz Curve graphically represent?",
                "options_json": [
                    "Income or wealth inequality distribution",
                    "Inflation vs unemployment",
                    "Tax rates vs tax revenue",
                    "Demand vs supply"
                ],
                "correct_answer": "Income or wealth inequality distribution",
                "explanation": "The Lorenz Curve shows the cumulative percentage of income earned against the cumulative percentage of the population, used to calculate the Gini Coefficient.",
                "points": 1
            },
            {
                "id": 5603,
                "topic_id": 56,
                "question": "Which sector contributes the highest share to India's Gross Value Added (GVA)?",
                "options_json": [
                    "Services Sector (Tertiary)",
                    "Agriculture (Primary)",
                    "Manufacturing (Secondary)",
                    "Mining"
                ],
                "correct_answer": "Services Sector (Tertiary)",
                "explanation": "The Services sector is the largest component of India's economy, accounting for over 53% of total Gross Value Added.",
                "points": 1
            },
            {
                "id": 5604,
                "topic_id": 56,
                "question": "In which year were 14 major commercial banks nationalized in India under Prime Minister Indira Gandhi?",
                "options_json": [
                    "1969",
                    "1980",
                    "1955",
                    "1975"
                ],
                "correct_answer": "1969",
                "explanation": "On 19 July 1969, the Government of India issued an ordinance nationalizing 14 major commercial banks having deposits of over Rs. 50 crore.",
                "points": 1
            },
            {
                "id": 5605,
                "topic_id": 56,
                "question": "What is the primary indicator of economic growth across countries?",
                "options_json": [
                    "Growth rate of Real GDP",
                    "Growth rate of Nominal GDP",
                    "Foreign exchange reserves",
                    "Gold reserves"
                ],
                "correct_answer": "Growth rate of Real GDP",
                "explanation": "Real GDP measures physical volume of output adjusted for inflation, making it the universally recognized metric for genuine economic growth.",
                "points": 1
            },
            {
                "id": 5606,
                "topic_id": 56,
                "question": "What does 'Core Inflation' exclude from the headline inflation basket?",
                "options_json": [
                    "Volatile food and energy components",
                    "Manufacturing goods",
                    "Services",
                    "Transport equipment"
                ],
                "correct_answer": "Volatile food and energy components",
                "explanation": "Core inflation excludes highly volatile food and fuel/energy commodity price fluctuations to capture the underlying durable trend.",
                "points": 1
            },
            {
                "id": 5607,
                "topic_id": 56,
                "question": "Which of the following is a Direct Tax in India?",
                "options_json": [
                    "Corporate Tax",
                    "Goods and Services Tax (GST)",
                    "Customs Duty",
                    "Excise Duty"
                ],
                "correct_answer": "Corporate Tax",
                "explanation": "Corporate Income Tax is paid directly by corporations on their net earnings, making it a Direct Tax, unlike GST which is indirect.",
                "points": 1
            },
            {
                "id": 5608,
                "topic_id": 56,
                "question": "What is the term for an increase in the general price level caused by rising costs of wages and raw materials?",
                "options_json": [
                    "Cost-Push Inflation",
                    "Demand-Pull Inflation",
                    "Deflation",
                    "Disinflation"
                ],
                "correct_answer": "Cost-Push Inflation",
                "explanation": "Cost-Push inflation occurs when aggregate supply decreases due to escalating production costs (labor wages, raw materials, import oil tariffs).",
                "points": 1
            },
            {
                "id": 5609,
                "topic_id": 56,
                "question": "Which organization compiles and publishes the Index of Industrial Production (IIP) in India?",
                "options_json": [
                    "National Statistical Office (NSO)",
                    "Reserve Bank of India",
                    "NITI Aayog",
                    "Ministry of Finance"
                ],
                "correct_answer": "National Statistical Office (NSO)",
                "explanation": "The Index of Industrial Production (IIP) is compiled and released monthly by the National Statistical Office (NSO) under MoSPI.",
                "points": 1
            },
            {
                "id": 5610,
                "topic_id": 56,
                "question": "The First Five-Year Plan of India (1951\u20131956) was based on which economic model?",
                "options_json": [
                    "Harrod-Domar Model",
                    "Mahalanobis Model",
                    "Feldman Model",
                    "Solow-Swan Model"
                ],
                "correct_answer": "Harrod-Domar Model",
                "explanation": "The 1st Five-Year Plan adapted the Harrod-Domar economic growth model to boost capital accumulation and revitalize agricultural productivity.",
                "points": 1
            }
        ]
    },
    "57": {
        "title": "Static GK: UNESCO Heritage, National Parks, River Valley Dams & Cultural Arts",
        "source_id": 7,
        "content": {
            "definition": "Static General Knowledge encompasses persistent, unchanging factual knowledge across geography, biological conservation, national heritage, civil engineering landmarks, and performing art traditions. A major scoring section across SSC CGL, RRB NTPC, State PSCs, and Defence exams, questions evaluate UNESCO World Heritage Sites in India, National Parks and Tiger Reserves, Major Dams and Hydroelectric Projects, Nuclear and Thermal Power Stations, Classical Dance forms recognized by Sangeet Natak Akademi, and Folk Music traditions.",
            "overview": "Fundamental Static GK Pillars:\n- UNESCO World Heritage Sites in India (42 sites as of 2024; 34 Cultural, 7 Natural, 1 Mixed - Khangchendzonga National Park, Sikkim; latest additions: Santiniketan, West Bengal and Sacred Ensembles of the Hoysalas, Karnataka)\n- Wildlife Protected Areas: Jim Corbett (Oldest NP, 1936, Uttarakhand); Kaziranga (One-horned rhino, Assam); Gir (Asiatic Lions, Gujarat); Keibul Lamjao (Only floating national park in the world, Loktak Lake, Manipur, Sangai deer); Project Tiger launched in 1973\n- Major Dams: Tehri Dam (Highest dam in India, 260.5 m, Bhagirathi river, Uttarakhand); Hirakud Dam (Longest earthen dam in India, 25.8 km, Mahanadi river, Odisha); Bhakra Nangal Dam (Highest gravity dam, Sutlej river, Himachal/Punjab); Sardar Sarovar Dam (Narmada river, Gujarat)\n- 8 Classical Dance Forms (Sangeet Natak Akademi): Bharatanatyam (Tamil Nadu), Kathak (Uttar Pradesh/North India), Kathakali (Kerala), Mohiniyattam (Kerala), Odissi (Odisha), Kuchipudi (Andhra Pradesh), Manipuri (Manipur), Sattriya (Assam, introduced by Sankaradeva)\n- Nuclear Power Stations: Tarapur (Oldest, Maharashtra), Kudankulam (Largest capacity, Tamil Nadu), Kalpakkam (Tamil Nadu), Narora (Uttar Pradesh), Kaiga (Karnataka), Kakrapar (Gujarat), Rawatbhata (Rajasthan)",
            "types": [
                {
                    "name": "1. UNESCO World Heritage Sites in India",
                    "desc": "Cultural, natural, and mixed sites recognized for outstanding universal value.",
                    "examples": [
                        "Ajanta, Ellora, and Elephanta Caves (Maharashtra); Sun Temple (Konark, Odisha)",
                        "Mixed Site: Khangchendzonga National Park (Sikkim) is India's only mixed UNESCO site"
                    ]
                },
                {
                    "name": "2. National Parks, Biosphere & Tiger Reserves",
                    "desc": "Key habitat reserves protecting endangered endemic species.",
                    "examples": [
                        "Keibul Lamjao National Park (Manipur): Only floating national park in the world (phumdis)",
                        "Sundarbans National Park (West Bengal): World's largest mangrove delta forest and Royal Bengal Tiger habitat"
                    ]
                },
                {
                    "name": "3. Major Multipurpose Dams & Reservoirs",
                    "desc": "Civil hydroelectric and irrigation structures built across major river basins.",
                    "examples": [
                        "Tehri Dam on Bhagirathi River (Highest dam in India, Uttarakhand)",
                        "Hirakud Dam on Mahanadi River (Longest dam in India, Odisha)"
                    ]
                },
                {
                    "name": "4. Classical Dances & Regional Folk Heritage",
                    "desc": "The 8 classical dance traditions and vibrant regional folk performances.",
                    "examples": [
                        "Sattriya: Classical dance of Assam created by saint Mahapurusha Sankaradeva (15th century)",
                        "Kerala possesses TWO classical dance forms: Kathakali and Mohiniyattam"
                    ]
                },
                {
                    "name": "5. Strategic Energy Infrastructure & Superlatives",
                    "desc": "Nuclear power stations, international boundaries, and national superlatives.",
                    "examples": [
                        "Tarapur Atomic Power Station (Maharashtra): First nuclear power plant in India (1969)",
                        "Kudankulam Nuclear Power Plant (Tamil Nadu): Highest capacity reactor built with Russian cooperation"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Tehri vs Hirakud Dam Superlatives Distinction",
                    "explanation": "- **Highest Dam in India**: **Tehri Dam** (height 260.5 m) on the **Bhagirathi River** in Uttarakhand.\n- **Longest Dam in India**: **Hirakud Dam** (total length 25.8 km) on the **Mahanadi River** in Odisha.\n- **Highest Straight Gravity Dam**: **Bhakra Dam** (height 226 m) on the **Sutlej River** in Himachal Pradesh.",
                    "words": [
                        "Tehri = Highest (Bhagirathi)",
                        "Hirakud = Longest (Mahanadi)",
                        "Bhakra = Gravity (Sutlej)"
                    ],
                    "correct": "Tehri is the highest dam; Hirakud is the longest dam in India.",
                    "incorrect": "Confusing highest with longest."
                },
                {
                    "rule_number": 2,
                    "title": "8 Recognized Classical Dances of India",
                    "explanation": "The Sangeet Natak Akademi officially recognizes strictly **8 Classical Dance Forms**:\n1. **Bharatanatyam** \u2014 Tamil Nadu\n2. **Kathakali** \u2014 Kerala\n3. **Mohiniyattam** \u2014 Kerala\n4. **Kathak** \u2014 Uttar Pradesh / North India\n5. **Odissi** \u2014 Odisha\n6. **Kuchipudi** \u2014 Andhra Pradesh\n7. **Manipuri** \u2014 Manipur\n8. **Sattriya** \u2014 Assam (added in 2000).\n*(Note: Ministry of Culture also considers Chhau, but Sangeet Natak Akademi recognizes these 8).*",
                    "words": [
                        "8 Classical Dances",
                        "Kerala has Two (Kathakali & Mohiniyattam)",
                        "Sattriya (Assam)"
                    ],
                    "correct": "Sattriya is the classical dance of Assam, developed by Sankaradeva in the 15th century.",
                    "incorrect": "Classifying Bhangra, Garba, or Lavani as classical dances (they are folk dances!)."
                },
                {
                    "rule_number": 3,
                    "title": "India's Only Mixed UNESCO World Heritage Site",
                    "explanation": "Out of India's 42 UNESCO World Heritage Sites (34 Cultural, 7 Natural, 1 Mixed):\n**Khangchendzonga National Park** in **Sikkim** is the **ONLY Mixed Heritage Site** in India, inscribed in 2016 for both its exceptional biodiversity and its sacred Tibetan Buddhist mythological cultural landscapes.",
                    "words": [
                        "Khangchendzonga National Park (Sikkim)",
                        "Only Mixed UNESCO Site in India"
                    ],
                    "correct": "Khangchendzonga National Park in Sikkim is India's sole mixed natural and cultural UNESCO site.",
                    "incorrect": "Selecting Sundarbans or Western Ghats as a mixed site (they are strictly natural sites)."
                },
                {
                    "rule_number": 4,
                    "title": "World's Only Floating National Park (Keibul Lamjao)",
                    "explanation": "**Keibul Lamjao National Park** in **Manipur** is the only floating national park on Earth. It is situated on **Loktak Lake** (the largest freshwater lake in Northeast India) and consists of floating biomass decomposed vegetation mats called **Phumdis**. It is the last natural refuge of the endangered brow-antlered deer known as **Sangai** (dancing deer).",
                    "words": [
                        "Keibul Lamjao (Manipur)",
                        "Loktak Lake",
                        "Phumdis",
                        "Sangai Deer"
                    ],
                    "correct": "Keibul Lamjao is a floating national park on Loktak Lake in Manipur, home to the Sangai deer.",
                    "incorrect": "Placing Keibul Lamjao in Assam or Meghalaya."
                },
                {
                    "rule_number": 5,
                    "title": "Oldest vs Largest National Park in India",
                    "explanation": "- **Oldest National Park in India**: **Jim Corbett National Park** (established in 1936 as Hailey National Park) in Uttarakhand.\n- **Largest National Park in India**: **Hemis National Park** (area ~4,400 sq km) in Ladakh, famous for the highest snow leopard density.",
                    "words": [
                        "Jim Corbett (Oldest, 1936, Uttarakhand)",
                        "Hemis (Largest, 4400 km\u00b2, Ladakh)"
                    ],
                    "correct": "Jim Corbett is India's oldest national park (1936); Hemis in Ladakh is India's largest.",
                    "incorrect": "Naming Kaziranga as the oldest or largest national park."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Confusing classical dances with folk dances.",
                    "correction": "Bhangra (Punjab), Garba (Gujarat), Ghoomar (Rajasthan), Bihu (Assam), and Lavani (Maharashtra) are FOLK dances, not classical dances.",
                    "rationale": "Sangeet Natak Akademi officially recognizes only 8 classical forms."
                },
                {
                    "mistake": "Confusing the highest dam (Tehri) with the longest dam (Hirakud).",
                    "correction": "Tehri is the highest (tallest); Hirakud is the longest (length across the river).",
                    "rationale": "High-frequency trap in competitive examinations."
                },
                {
                    "mistake": "Believing India has multiple mixed UNESCO sites.",
                    "correction": "India has strictly ONE mixed site: Khangchendzonga National Park in Sikkim.",
                    "rationale": "UNESCO category distinction between Natural, Cultural, and Mixed."
                },
                {
                    "mistake": "Thinking Project Tiger started in 1980.",
                    "correction": "Project Tiger was launched on 1 April 1973 under Prime Minister Indira Gandhi at Corbett National Park.",
                    "rationale": "Historic conservation timeline milestone."
                }
            ],
            "quick_revision_points": [
                "Tehri Dam (Highest, Bhagirathi, Uttarakhand); Hirakud Dam (Longest, Mahanadi, Odisha)",
                "8 Classical Dances: Bharatanatyam (TN), Kathakali (KL), Mohiniyattam (KL), Kathak (UP), Odissi (OD), Kuchipudi (AP), Manipuri (MN), Sattriya (AS)",
                "Only floating National Park: Keibul Lamjao (Loktak Lake, Manipur, Sangai deer)",
                "Oldest NP: Jim Corbett (1936, Uttarakhand); Largest NP: Hemis (Ladakh, Snow Leopard)",
                "India's only Mixed UNESCO Site: Khangchendzonga National Park (Sikkim)",
                "Oldest Nuclear Power Plant: Tarapur (Maharashtra, 1969); Largest: Kudankulam (Tamil Nadu)",
                "Kaziranga (Assam) is world-famous for the Great Indian One-horned Rhinoceros",
                "Sardar Sarovar Dam is built on the Narmada River in Gujarat"
            ]
        },
        "previous_year_questions": [
            {
                "id": 5701,
                "topic_id": 57,
                "exam_id": 1,
                "question": "Which of the following is the only 'floating' National Park in the world? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Keibul Lamjao National Park (Manipur)",
                    "Kaziranga National Park (Assam)",
                    "Sundarbans National Park (West Bengal)",
                    "Namdapha National Park (Arunachal Pradesh)"
                ],
                "correct_answer": "Keibul Lamjao National Park (Manipur)",
                "explanation": "Keibul Lamjao National Park, located on the Loktak Lake in the Bishnupur district of Manipur, is the world's only floating national park, characterized by floating decomposed vegetative masses called 'Phumdis'. It is the exclusive natural habitat of the endangered Sangai deer.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5702,
                "topic_id": 57,
                "exam_id": 1,
                "question": "The classical dance form 'Sattriya' originated in which Indian state? [UPSC CDS 2022]",
                "options_json": [
                    "Assam",
                    "Manipur",
                    "Odisha",
                    "West Bengal"
                ],
                "correct_answer": "Assam",
                "explanation": "Sattriya is a major classical Indian dance form that originated in the Sattras (monasteries) of Assam, created by the 15th-century Vaishnavite saint and polymath Srimanta Sankaradeva.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5703,
                "topic_id": 57,
                "exam_id": 1,
                "question": "On which river is the Hirakud Dam, the longest earthen dam in India, constructed? [RRB NTPC 2022]",
                "options_json": [
                    "Mahanadi River",
                    "Godavari River",
                    "Bhagirathi River",
                    "Narmada River"
                ],
                "correct_answer": "Mahanadi River",
                "explanation": "The Hirakud Dam is built across the Mahanadi River near Sambalpur in Odisha. Built in 1957, it is one of the longest dams in the world, spanning about 25.8 km across the river valley.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 5701,
                "topic_id": 57,
                "question": "What is the highest dam in India, built on the Bhagirathi River?",
                "options_json": [
                    "Tehri Dam",
                    "Hirakud Dam",
                    "Bhakra Dam",
                    "Sardar Sarovar Dam"
                ],
                "correct_answer": "Tehri Dam",
                "explanation": "Tehri Dam, standing at a height of 260.5 m on the Bhagirathi River in Uttarakhand, is the highest dam in India.",
                "points": 1
            },
            {
                "id": 5702,
                "topic_id": 57,
                "question": "Which Indian state has TWO classical dance forms recognized by the Sangeet Natak Akademi?",
                "options_json": [
                    "Kerala (Kathakali and Mohiniyattam)",
                    "Tamil Nadu",
                    "Odisha",
                    "Andhra Pradesh"
                ],
                "correct_answer": "Kerala (Kathakali and Mohiniyattam)",
                "explanation": "Kerala is the only Indian state with two distinct classical dance traditions: Kathakali and Mohiniyattam.",
                "points": 1
            },
            {
                "id": 5703,
                "topic_id": 57,
                "question": "Which is India's oldest national park, established in 1936 as Hailey National Park?",
                "options_json": [
                    "Jim Corbett National Park",
                    "Kaziranga National Park",
                    "Kanha National Park",
                    "Gir National Park"
                ],
                "correct_answer": "Jim Corbett National Park",
                "explanation": "Jim Corbett National Park in Nainital/Pauri Garhwal district of Uttarakhand was established in 1936 as Hailey National Park.",
                "points": 1
            },
            {
                "id": 5704,
                "topic_id": 57,
                "question": "Which is the only 'Mixed' UNESCO World Heritage Site in India?",
                "options_json": [
                    "Khangchendzonga National Park",
                    "Manas Wildlife Sanctuary",
                    "Sundarbans National Park",
                    "Western Ghats"
                ],
                "correct_answer": "Khangchendzonga National Park",
                "explanation": "Khangchendzonga National Park in Sikkim was inscribed as a Mixed UNESCO World Heritage Site in 2016 for its natural biodiversity and cultural significance.",
                "points": 1
            },
            {
                "id": 5705,
                "topic_id": 57,
                "question": "Where was India's first commercial atomic/nuclear power station established in 1969?",
                "options_json": [
                    "Tarapur (Maharashtra)",
                    "Kudankulam (Tamil Nadu)",
                    "Narora (Uttar Pradesh)",
                    "Rawatbhata (Rajasthan)"
                ],
                "correct_answer": "Tarapur (Maharashtra)",
                "explanation": "Tarapur Atomic Power Station in Palghar district of Maharashtra was the first commercial nuclear power station in India, commissioned in 1969.",
                "points": 1
            },
            {
                "id": 5706,
                "topic_id": 57,
                "question": "Gir National Park in Gujarat is internationally celebrated as the last natural sanctuary of which animal?",
                "options_json": [
                    "Asiatic Lion",
                    "Royal Bengal Tiger",
                    "One-horned Rhinoceros",
                    "Snow Leopard"
                ],
                "correct_answer": "Asiatic Lion",
                "explanation": "Gir National Park and Wildlife Sanctuary in Gujarat is the only remaining natural habitat in the world of the Asiatic Lion (Panthera leo persica).",
                "points": 1
            },
            {
                "id": 5707,
                "topic_id": 57,
                "question": "In which state is the famous Sun Temple of Konark located?",
                "options_json": [
                    "Odisha",
                    "Andhra Pradesh",
                    "Karnataka",
                    "Tamil Nadu"
                ],
                "correct_answer": "Odisha",
                "explanation": "The 13th-century Konark Sun Temple (Black Pagoda), designed in the form of a gigantic chariot, is located in Puri district, Odisha.",
                "points": 1
            },
            {
                "id": 5708,
                "topic_id": 57,
                "question": "Which classical dance form originated in Tamil Nadu and is known for its geometric temple dance postures?",
                "options_json": [
                    "Bharatanatyam",
                    "Kathakali",
                    "Kuchipudi",
                    "Odissi"
                ],
                "correct_answer": "Bharatanatyam",
                "explanation": "Bharatanatyam is one of the oldest classical dance traditions of India, originating from the temple dancers (Devadasis) of Tamil Nadu.",
                "points": 1
            },
            {
                "id": 5709,
                "topic_id": 57,
                "question": "The Sardar Sarovar Dam is constructed across which major peninsular river in Gujarat?",
                "options_json": [
                    "Narmada River",
                    "Tapi River",
                    "Sabarmati River",
                    "Mahi River"
                ],
                "correct_answer": "Narmada River",
                "explanation": "The Sardar Sarovar Dam, one of the largest concrete gravity dams in the world, is built on the Narmada River near Kevadiya, Gujarat.",
                "points": 1
            },
            {
                "id": 5710,
                "topic_id": 57,
                "question": "In which Indian state or Union Territory is Hemis National Park, India's largest national park, situated?",
                "options_json": [
                    "Ladakh",
                    "Himachal Pradesh",
                    "Jammu and Kashmir",
                    "Uttarakhand"
                ],
                "correct_answer": "Ladakh",
                "explanation": "Hemis National Park is a high-altitude national park in eastern Ladakh, famous globally for being the premier sanctuary of the endangered snow leopard.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 5701,
                "topic_id": 57,
                "question": "Which National Park in Assam is world-famous as the home of the Great Indian One-Horned Rhinoceros?",
                "options_json": [
                    "Kaziranga National Park",
                    "Manas National Park",
                    "Jim Corbett National Park",
                    "Ranthambore National Park"
                ],
                "correct_answer": "Kaziranga National Park",
                "explanation": "Kaziranga National Park in Assam hosts two-thirds of the world's population of the Great Indian One-horned Rhinoceros.",
                "points": 1
            },
            {
                "id": 5702,
                "topic_id": 57,
                "question": "What is the classical dance form of Uttar Pradesh / North India characterized by intricate footwork and spins?",
                "options_json": [
                    "Kathak",
                    "Kathakali",
                    "Bharatanatyam",
                    "Sattriya"
                ],
                "correct_answer": "Kathak",
                "explanation": "Kathak (derived from 'Katha', meaning storytellers) is the classical dance of North India, nurtured in the courts of Awadh and Jaipur.",
                "points": 1
            },
            {
                "id": 5703,
                "topic_id": 57,
                "question": "Which is the largest nuclear power plant in India in terms of generation capacity?",
                "options_json": [
                    "Kudankulam Nuclear Power Plant",
                    "Tarapur Atomic Power Station",
                    "Kaiga Generating Station",
                    "Narora Atomic Power Station"
                ],
                "correct_answer": "Kudankulam Nuclear Power Plant",
                "explanation": "Kudankulam Nuclear Power Plant in Tirunelveli district of Tamil Nadu, built in technical collaboration with Russia, is the highest-capacity nuclear facility in India (2000 MW operational).",
                "points": 1
            },
            {
                "id": 5704,
                "topic_id": 57,
                "question": "In which state is the Nagarjuna Sagar Dam, built across the Krishna River, located?",
                "options_json": [
                    "Andhra Pradesh and Telangana border",
                    "Karnataka",
                    "Tamil Nadu",
                    "Maharashtra"
                ],
                "correct_answer": "Andhra Pradesh and Telangana border",
                "explanation": "Nagarjuna Sagar Dam is a masonry dam built across the Krishna River on the border between Guntur district (Andhra Pradesh) and Nalgonda district (Telangana).",
                "points": 1
            },
            {
                "id": 5705,
                "topic_id": 57,
                "question": "In which year was 'Project Tiger' launched in India to protect the endangered Royal Bengal Tiger?",
                "options_json": [
                    "1973",
                    "1972",
                    "1980",
                    "1986"
                ],
                "correct_answer": "1973",
                "explanation": "Project Tiger was launched on 1 April 1973 by the Government of India from Jim Corbett National Park in Uttarakhand.",
                "points": 1
            },
            {
                "id": 5706,
                "topic_id": 57,
                "question": "Kuchipudi is the classical dance tradition of which Indian state?",
                "options_json": [
                    "Andhra Pradesh",
                    "Karnataka",
                    "Kerala",
                    "Tamil Nadu"
                ],
                "correct_answer": "Andhra Pradesh",
                "explanation": "Kuchipudi originated in the village of Kuchipudi in the Krishna district of Andhra Pradesh.",
                "points": 1
            },
            {
                "id": 5707,
                "topic_id": 57,
                "question": "The historic Santiniketan, recently inscribed as a UNESCO World Heritage Site in 2023, was founded by whom?",
                "options_json": [
                    "Rabindranath Tagore",
                    "Swami Vivekananda",
                    "Raja Ram Mohan Roy",
                    "Aurobindo Ghose"
                ],
                "correct_answer": "Rabindranath Tagore",
                "explanation": "Santiniketan in Birbhum district of West Bengal was developed by Nobel laureate Rabindranath Tagore as an ashram and open-air educational institution (Visva-Bharati).",
                "points": 1
            },
            {
                "id": 5708,
                "topic_id": 57,
                "question": "On which river is the Bhakra Nangal Dam, the highest straight gravity dam in India, constructed?",
                "options_json": [
                    "Sutlej River",
                    "Beas River",
                    "Ravi River",
                    "Chenab River"
                ],
                "correct_answer": "Sutlej River",
                "explanation": "Bhakra Dam is a concrete gravity dam on the Sutlej River in Bilaspur, Himachal Pradesh, forming the Gobind Sagar reservoir.",
                "points": 1
            },
            {
                "id": 5709,
                "topic_id": 57,
                "question": "Bihu is the most prominent cultural folk festival and dance of which Indian state?",
                "options_json": [
                    "Assam",
                    "Meghalaya",
                    "Tripura",
                    "Nagaland"
                ],
                "correct_answer": "Assam",
                "explanation": "Bihu is the chief agricultural folk celebration of Assam (Rongali/Bohag Bihu, Kongali/Kati Bihu, and Bhogali/Magh Bihu).",
                "points": 1
            },
            {
                "id": 5710,
                "topic_id": 57,
                "question": "Ranthambore National Park and Tiger Reserve is located in which state of India?",
                "options_json": [
                    "Rajasthan",
                    "Madhya Pradesh",
                    "Gujarat",
                    "Maharashtra"
                ],
                "correct_answer": "Rajasthan",
                "explanation": "Ranthambore National Park is a prominent tiger reserve located near Sawai Madhopur in southeastern Rajasthan.",
                "points": 1
            }
        ]
    },
    "58": {
        "title": "Awards and Honours: Civilian, Military, Literary & International Accolades",
        "source_id": 7,
        "content": {
            "definition": "Awards and Honours evaluates the institutional conferrals recognizing outstanding national service, battlefield gallantry, literary mastery, scientific achievement, and cinematic excellence. Prominent across SSC CGL, RRB NTPC, State PSCs, and Defence exams, questions examine the hierarchy of Indian civilian awards (Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri), wartime and peacetime gallantry decorations (Param Vir Chakra, Ashok Chakra), literary prizes (Jnanpith, Sahitya Akademi, Saraswati Samman), and international accolades (Nobel Prizes, Booker Prize, Ramon Magsaysay).",
            "overview": "Fundamental Honours Architecture:\n- Civilian Honours of India (Instituted 1954):\n  - 1st Tier: Bharat Ratna (Highest civilian award of India; Peepal leaf shaped medallion; first recipients in 1954: C. Rajagopalachari, Dr. S. Radhakrishnan, Dr. C.V. Raman)\n  - 2nd Tier: Padma Vibhushan (For exceptional and distinguished service)\n  - 3rd Tier: Padma Bhushan (For distinguished service of high order)\n  - 4th Tier: Padma Shri (For distinguished service in any field)\n- Military Gallantry Awards:\n  - Wartime: Param Vir Chakra (Highest military decoration for supreme valour; 1st recipient Major Somnath Sharma), Maha Vir Chakra, Vir Chakra\n  - Peacetime: Ashok Chakra (Highest peacetime gallantry award), Kirti Chakra, Shaurya Chakra\n- Literary Honours: Jnanpith Award (Highest literary award in India; 1st recipient G. Sankara Kurup, Malayalam in 1965); Sahitya Akademi Award; Saraswati Samman; Vyas Samman\n- Cinema & Performing Arts: Dadasaheb Phalke Award (India's highest award in cinema; 1st recipient Devika Rani in 1969)\n- International Accolades: Nobel Prize (instituted by Alfred Nobel, 6 categories: Physics, Chemistry, Physiology/Medicine, Literature, Peace, Economic Sciences); Booker Prize (Fiction written in English); International Booker Prize; Ramon Magsaysay Award ('Nobel of Asia')",
            "types": [
                {
                    "name": "1. Indian Civilian Honours (Bharat Ratna & Padma Awards)",
                    "desc": "Highest state decorations awarded on Republic Day for exceptional public service and arts.",
                    "examples": [
                        "Non-Indian Bharat Ratna recipients: Khan Abdul Ghaffar Khan (1987) and Nelson Mandela (1990)",
                        "Youngest Bharat Ratna recipient: Sachin Tendulkar (awarded at age 40 in 2014)"
                    ]
                },
                {
                    "name": "2. Military Gallantry Decorations (Wartime vs Peacetime)",
                    "desc": "Conferred for acts of conspicuous bravery in the presence of the enemy or peacetime valour.",
                    "examples": [
                        "Param Vir Chakra: First recipient was Major Somnath Sharma (Posthumous, 1947 Indo-Pak War, Battle of Badgam)",
                        "Ashok Chakra: India's highest peacetime military decoration for courage, valorous action or self-sacrifice"
                    ]
                },
                {
                    "name": "3. Indian Literary Accolades",
                    "desc": "Recognizing excellence in the 22 languages listed in the 8th Schedule of the Constitution plus English.",
                    "examples": [
                        "Jnanpith Award: Conferred by Bharatiya Jnanpith; consists of a bronze replica of Goddess Saraswati (Vagdevi)",
                        "First woman to win Jnanpith: Ashapurna Devi (Bengali, 1976 for 'Pratham Pratishruti')"
                    ]
                },
                {
                    "name": "4. Cinematic & Performing Arts Honours",
                    "desc": "Honouring lifetime contributions to the growth and development of Indian cinema.",
                    "examples": [
                        "Dadasaheb Phalke Award: First recipient was Devika Rani (1969); recent awardees include Waheeda Rehman and Asha Parekh"
                    ]
                },
                {
                    "name": "5. International Prizes & Indian Laureates",
                    "desc": "Global recognitions in science, literature, peace, and humanitarian service.",
                    "examples": [
                        "Nobel Prize: Rabindranath Tagore was the first Asian to win the Nobel Prize (Literature, 1913, 'Gitanjali')",
                        "C.V. Raman won Nobel Prize in Physics (1930) for discovery of the Raman Effect"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "First Recipients of the Bharat Ratna (1954 Triad)",
                    "explanation": "The Bharat Ratna was instituted on 2 January 1954 by President Dr. Rajendra Prasad. In its inaugural year (1954), it was conferred upon strictly **THREE individuals**:\n1. **C. Rajagopalachari** (Last Governor-General of India)\n2. **Dr. Sarvepalli Radhakrishnan** (First Vice President and philosopher)\n3. **Dr. C.V. Raman** (Nobel Laureate Physicist).\n*(Note: Jawaharlal Nehru received it in 1955).*",
                    "words": [
                        "1954 Triad",
                        "C. Rajagopalachari",
                        "Dr. S. Radhakrishnan",
                        "Dr. C.V. Raman"
                    ],
                    "correct": "The first recipients of the Bharat Ratna in 1954 were C. Rajagopalachari, Dr. S. Radhakrishnan, and Dr. C.V. Raman.",
                    "incorrect": "Stating that Jawaharlal Nehru or Mahatma Gandhi was the first recipient in 1954."
                },
                {
                    "rule_number": 2,
                    "title": "Wartime vs Peacetime Gallantry Hierarchy",
                    "explanation": "- **Wartime Gallantry** (in the face of enemy aggression):\n  1. Param Vir Chakra (PVC) \u2014 Supreme\n  2. Maha Vir Chakra (MVC)\n  3. Vir Chakra (VrC)\n- **Peacetime Gallantry** (acts of bravery other than in face of enemy):\n  1. Ashok Chakra (AC) \u2014 Equivalent in stature to PVC\n  2. Kirti Chakra (KC) \u2014 Equivalent to MVC\n  3. Shaurya Chakra (SC) \u2014 Equivalent to VrC.",
                    "words": [
                        "PVC > MVC > VrC (Wartime)",
                        "Ashok > Kirti > Shaurya (Peacetime)"
                    ],
                    "correct": "The Ashok Chakra is India's highest peacetime gallantry award; Param Vir Chakra is the highest wartime award.",
                    "incorrect": "Confusing Ashok Chakra with wartime awards."
                },
                {
                    "rule_number": 3,
                    "title": "Foreign Nationals Conferred the Bharat Ratna",
                    "explanation": "There is no constitutional bar on conferring the Bharat Ratna on non-citizens. Till date, exactly **TWO foreign nationals** have been honored:\n1. **Khan Abdul Ghaffar Khan** ('Frontier Gandhi', Pakistani national, 1987)\n2. **Nelson Mandela** (Former President of South Africa, 1990).\n*(Note: Mother Teresa was a naturalized Indian citizen when she received it in 1980).* ",
                    "words": [
                        "Khan Abdul Ghaffar Khan (1987)",
                        "Nelson Mandela (1990)",
                        "Two Foreigners"
                    ],
                    "correct": "Khan Abdul Ghaffar Khan and Nelson Mandela are the two non-Indian foreign nationals awarded the Bharat Ratna.",
                    "incorrect": "Classifying Mother Teresa as a foreigner at the time of award (she naturalized as an Indian in 1948)."
                },
                {
                    "rule_number": 4,
                    "title": "Indian Nobel Laureates Chronological Order",
                    "explanation": "1. **Rabindranath Tagore** (1913, Literature \u2014 'Gitanjali', 1st Asian laureate)\n2. **C.V. Raman** (1930, Physics \u2014 Raman Scattering)\n3. **Mother Teresa** (1979, Peace)\n4. **Amartya Sen** (1998, Economic Sciences \u2014 Welfare Economics)\n5. **Kailash Satyarthi** (2014, Peace \u2014 Child rights activist shared with Malala Yousafzai).\n*(Indian-origin laureates: Har Gobind Khorana 1968, Subrahmanyan Chandrasekhar 1983, Venkatraman Ramakrishnan 2009, Abhijit Banerjee 2019).* ",
                    "words": [
                        "Tagore (1913)",
                        "Raman (1930)",
                        "Teresa (1979)",
                        "Amartya Sen (1998)",
                        "Satyarthi (2014)"
                    ],
                    "correct": "Rabindranath Tagore was the first Indian/Asian Nobel laureate (1913); Amartya Sen won for Economic Sciences (1998).",
                    "incorrect": "Attributing C.V. Raman's Nobel to Chemistry (it was in Physics)."
                },
                {
                    "rule_number": 5,
                    "title": "Jnanpith Award Foundations Rule",
                    "explanation": "The Jnanpith Award (instituted 1961, first awarded 1965) is India's highest literary honour. Key facts:\n- 1st Recipient: **G. Sankara Kurup** (1965 for his Malayalam poetry collection 'Odakkuzhal')\n- 1st Woman Recipient: **Ashapurna Devi** (1976 for Bengali novel 'Pratham Pratishruti')\n- Conferred exclusively on Indian citizens for works in the 22 Eighth Schedule languages and English.",
                    "words": [
                        "Jnanpith (1965)",
                        "G. Sankara Kurup (Malayalam)",
                        "Ashapurna Devi (1976, Bengali)"
                    ],
                    "correct": "G. Sankara Kurup was the first recipient of the Jnanpith Award in 1965 for Malayalam literature.",
                    "incorrect": "Assuming Hindi was the language of the first Jnanpith winner (Sumitranandan Pant was the first in Hindi in 1968)."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Claiming Mother Teresa was a foreign citizen when she won the Bharat Ratna.",
                    "correction": "Mother Teresa became a full naturalized Indian citizen in 1948, decades before receiving the Bharat Ratna in 1980.",
                    "rationale": "Only Khan Abdul Ghaffar Khan and Nelson Mandela were non-citizens when awarded."
                },
                {
                    "mistake": "Confusing Ashok Chakra with the Kirti Chakra.",
                    "correction": "Ashok Chakra is the 1st tier (highest) peacetime gallantry award; Kirti Chakra is 2nd tier; Shaurya Chakra is 3rd tier.",
                    "rationale": "Direct parallel to PVC, MVC, and Vir Chakra in wartime."
                },
                {
                    "mistake": "Naming Mahatma Gandhi as a Bharat Ratna recipient.",
                    "correction": "Mahatma Gandhi was never conferred the Bharat Ratna (the government deemed his stature above national awards).",
                    "rationale": "Examiners often use Gandhi as a distractor option in Bharat Ratna questions."
                },
                {
                    "mistake": "Confusing Booker Prize with the International Booker Prize.",
                    "correction": "The Booker Prize is for a novel written originally in English. The International Booker Prize is for fiction translated into English (won by Geetanjali Shree for 'Tomb of Sand' in 2022).",
                    "rationale": "Crucial international literary distinction."
                }
            ],
            "quick_revision_points": [
                "Bharat Ratna instituted in 1954; first recipients: C. Rajagopalachari, S. Radhakrishnan, C.V. Raman",
                "Foreign Bharat Ratna awardees: Khan Abdul Ghaffar Khan (1987) and Nelson Mandela (1990)",
                "Param Vir Chakra: First recipient was Major Somnath Sharma (1947, 4 Kumaon Regiment)",
                "Ashok Chakra is the highest peacetime military gallantry decoration in India",
                "First Asian/Indian Nobel Laureate: Rabindranath Tagore (Literature, 1913, 'Gitanjali')",
                "First Jnanpith Award winner: G. Sankara Kurup (Malayalam, 1965); 1st woman: Ashapurna Devi (1976)",
                "Dadasaheb Phalke Award: Highest honor in Indian cinema; first recipient was Devika Rani (1969)",
                "Youngest Bharat Ratna recipient: Sachin Tendulkar (2014, age 40)"
            ]
        },
        "previous_year_questions": [
            {
                "id": 5801,
                "topic_id": 58,
                "exam_id": 1,
                "question": "Who was the first recipient of the prestigious Param Vir Chakra, India's highest wartime gallantry decoration? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Major Somnath Sharma",
                    "Captain Vikram Batra",
                    "Subedar Major Bana Singh",
                    "Company Havildar Major Abdul Hamid"
                ],
                "correct_answer": "Major Somnath Sharma",
                "explanation": "Major Somnath Sharma of the 4 Kumaon Regiment was posthumously awarded the first Param Vir Chakra for supreme bravery during the Battle of Badgam in the 1947 Indo-Pak War.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5802,
                "topic_id": 58,
                "exam_id": 1,
                "question": "Rabindranath Tagore was awarded the Nobel Prize in Literature in 1913 for which of his monumental works? [UPSC CDS 2022]",
                "options_json": [
                    "Gitanjali",
                    "Gora",
                    "Ghare Baire (The Home and the World)",
                    "Chokher Bali"
                ],
                "correct_answer": "Gitanjali",
                "explanation": "Rabindranath Tagore won the Nobel Prize in Literature in 1913 'because of his profoundly sensitive, fresh and beautiful verse' in his poetry collection 'Gitanjali' (Song Offerings), becoming the first non-European and first Asian Nobel laureate.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 5803,
                "topic_id": 58,
                "exam_id": 1,
                "question": "Who was the first recipient of the Dadasaheb Phalke Award, India's highest award in cinema, instituted in 1969? [RRB NTPC 2022]",
                "options_json": [
                    "Devika Rani",
                    "Prithviraj Kapoor",
                    "Raj Kapoor",
                    "Lata Mangeshkar"
                ],
                "correct_answer": "Devika Rani",
                "explanation": "Devika Rani Chaudhuri, widely acclaimed as the 'First Lady of Indian Cinema', was the inaugural recipient of the Dadasaheb Phalke Award in 1969.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 5801,
                "topic_id": 58,
                "question": "In which year was the Bharat Ratna, the highest civilian award of India, instituted?",
                "options_json": [
                    "1954",
                    "1950",
                    "1947",
                    "1952"
                ],
                "correct_answer": "1954",
                "explanation": "The Bharat Ratna was instituted on 2 January 1954 by Dr. Rajendra Prasad, the first President of India.",
                "points": 1
            },
            {
                "id": 5802,
                "topic_id": 58,
                "question": "Which of the following non-Indian foreign nationals was conferred the Bharat Ratna in 1987?",
                "options_json": [
                    "Khan Abdul Ghaffar Khan",
                    "Nelson Mandela",
                    "Mother Teresa",
                    "Martin Luther King Jr."
                ],
                "correct_answer": "Khan Abdul Ghaffar Khan",
                "explanation": "Khan Abdul Ghaffar Khan (popularly known as Frontier Gandhi or Badshah Khan) became the first non-Indian national to be awarded the Bharat Ratna in 1987.",
                "points": 1
            },
            {
                "id": 5803,
                "topic_id": 58,
                "question": "What is the highest peacetime military gallantry award in India?",
                "options_json": [
                    "Ashok Chakra",
                    "Param Vir Chakra",
                    "Kirti Chakra",
                    "Shaurya Chakra"
                ],
                "correct_answer": "Ashok Chakra",
                "explanation": "The Ashok Chakra is India's highest peacetime military decoration awarded for valor, courageous action, or self-sacrifice away from the battlefield.",
                "points": 1
            },
            {
                "id": 5804,
                "topic_id": 58,
                "question": "Who was the first Indian citizen to win the Nobel Prize in Economic Sciences in 1998?",
                "options_json": [
                    "Amartya Sen",
                    "Abhijit Banerjee",
                    "Manmohan Singh",
                    "Jagdish Bhagwati"
                ],
                "correct_answer": "Amartya Sen",
                "explanation": "Professor Amartya Sen was awarded the Nobel Memorial Prize in Economic Sciences in 1998 for his groundbreaking contributions to welfare economics and poverty measurement.",
                "points": 1
            },
            {
                "id": 5805,
                "topic_id": 58,
                "question": "Who was the first recipient of the Jnanpith Award, India's highest literary honour, in 1965?",
                "options_json": [
                    "G. Sankara Kurup",
                    "K.V. Puttappa",
                    "Uma Shankar Joshi",
                    "Sumitranandan Pant"
                ],
                "correct_answer": "G. Sankara Kurup",
                "explanation": "G. Sankara Kurup won the inaugural Jnanpith Award in 1965 for his Malayalam poetry collection 'Odakkuzhal' (The Bamboo Flute).",
                "points": 1
            },
            {
                "id": 5806,
                "topic_id": 58,
                "question": "Who is the youngest person and only sportsperson to receive the Bharat Ratna?",
                "options_json": [
                    "Sachin Tendulkar",
                    "Major Dhyan Chand",
                    "Viswanathan Anand",
                    "Kapil Dev"
                ],
                "correct_answer": "Sachin Tendulkar",
                "explanation": "Cricket legend Sachin Tendulkar was conferred the Bharat Ratna in 2014 at the age of 40, becoming both the youngest recipient and the first athlete to receive it.",
                "points": 1
            },
            {
                "id": 5807,
                "topic_id": 58,
                "question": "Which award is popularly celebrated as the 'Nobel Prize of Asia'?",
                "options_json": [
                    "Ramon Magsaysay Award",
                    "Booker Prize",
                    "Jnanpith Award",
                    "Gandhi Peace Prize"
                ],
                "correct_answer": "Ramon Magsaysay Award",
                "explanation": "The Ramon Magsaysay Award, established in 1957 in memory of the 7th Philippine President, is widely regarded as Asia's premier prize and equivalent to the Nobel Prize.",
                "points": 1
            },
            {
                "id": 5808,
                "topic_id": 58,
                "question": "Who was the first woman to win the Jnanpith Award in 1976?",
                "options_json": [
                    "Ashapurna Devi",
                    "Mahadevi Varma",
                    "Amrita Pritam",
                    "Mahasweta Devi"
                ],
                "correct_answer": "Ashapurna Devi",
                "explanation": "Bengali novelist Ashapurna Devi became the first woman to win the Jnanpith Award in 1976 for her landmark novel 'Pratham Pratishruti'.",
                "points": 1
            },
            {
                "id": 5809,
                "topic_id": 58,
                "question": "Dr. C.V. Raman won the Nobel Prize in Physics in 1930 for his discovery in which field of optics?",
                "options_json": [
                    "Scattering of light (Raman Effect)",
                    "Photoelectric effect",
                    "Nuclear magnetic resonance",
                    "Laser physics"
                ],
                "correct_answer": "Scattering of light (Raman Effect)",
                "explanation": "Sir C.V. Raman discovered that when light traverses a transparent material, some of the deflected light changes wavelength, known as Raman Scattering.",
                "points": 1
            },
            {
                "id": 5810,
                "topic_id": 58,
                "question": "The Shanti Swarup Bhatnagar Prize is awarded annually in India for outstanding achievements in which field?",
                "options_json": [
                    "Science and Technology",
                    "Literature",
                    "Classical Music",
                    "Cinema"
                ],
                "correct_answer": "Science and Technology",
                "explanation": "The Shanti Swarup Bhatnagar Prize, given by the Council of Scientific and Industrial Research (CSIR), is India's most prestigious award in Science and Technology for researchers under 45 years.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 5801,
                "topic_id": 58,
                "question": "How many civilian award tiers belong to the 'Padma Awards' series?",
                "options_json": [
                    "3 (Padma Vibhushan, Padma Bhushan, Padma Shri)",
                    "4",
                    "2",
                    "5"
                ],
                "correct_answer": "3 (Padma Vibhushan, Padma Bhushan, Padma Shri)",
                "explanation": "The Padma Awards hierarchy consists of three categories: Padma Vibhushan (highest), Padma Bhushan (second), and Padma Shri (third).",
                "points": 1
            },
            {
                "id": 5802,
                "topic_id": 58,
                "question": "Who was the first recipient of the prestigious Rajiv Gandhi Khel Ratna (now Major Dhyan Chand Khel Ratna) Award in 1991\u201392?",
                "options_json": [
                    "Viswanathan Anand",
                    "Geet Sethi",
                    "Sachin Tendulkar",
                    "Karnam Malleswari"
                ],
                "correct_answer": "Viswanathan Anand",
                "explanation": "Grandmaster Viswanathan Anand was the inaugural recipient of India's highest sporting honour, the Khel Ratna Award, in 1991\u201392.",
                "points": 1
            },
            {
                "id": 5803,
                "topic_id": 58,
                "question": "Which Nobel Prize is awarded in Oslo, Norway, unlike all other Nobel Prizes which are awarded in Stockholm, Sweden?",
                "options_json": [
                    "Nobel Peace Prize",
                    "Nobel Prize in Literature",
                    "Nobel Prize in Physics",
                    "Nobel Prize in Physiology or Medicine"
                ],
                "correct_answer": "Nobel Peace Prize",
                "explanation": "As dictated in Alfred Nobel's will, the Nobel Peace Prize is awarded in Oslo (Norway), while the other five categories are awarded in Stockholm (Sweden).",
                "points": 1
            },
            {
                "id": 5804,
                "topic_id": 58,
                "question": "What is the design of the medallion of the Bharat Ratna award?",
                "options_json": [
                    "A peepal leaf with a sunburst embossed on the obverse",
                    "A circular gold coin",
                    "A lotus flower",
                    "An ashoka pillar replica"
                ],
                "correct_answer": "A peepal leaf with a sunburst embossed on the obverse",
                "explanation": "The Bharat Ratna medallion is toned in bronze, cast in the shape of a peepal leaf, with a platinum sun emblem and the words 'Bharat Ratna' in Devanagari script.",
                "points": 1
            },
            {
                "id": 5805,
                "topic_id": 58,
                "question": "In which year did Mother Teresa win the Nobel Peace Prize?",
                "options_json": [
                    "1979",
                    "1980",
                    "1975",
                    "1982"
                ],
                "correct_answer": "1979",
                "explanation": "Mother Teresa was awarded the Nobel Peace Prize in 1979 for her humanitarian work helping suffering humanity through the Missionaries of Charity.",
                "points": 1
            },
            {
                "id": 5806,
                "topic_id": 58,
                "question": "The Saraswati Samman, an annual award for outstanding prose or poetry in any 22 Indian language, is instituted by which foundation?",
                "options_json": [
                    "K.K. Birla Foundation",
                    "Tata Trust",
                    "Sahitya Akademi",
                    "Bharatiya Jnanpith"
                ],
                "correct_answer": "K.K. Birla Foundation",
                "explanation": "The Saraswati Samman was instituted in 1991 by the K.K. Birla Foundation. Harivansh Rai Bachchan was its first recipient.",
                "points": 1
            },
            {
                "id": 5807,
                "topic_id": 58,
                "question": "Which wartime gallantry award is the second highest decoration after the Param Vir Chakra?",
                "options_json": [
                    "Maha Vir Chakra",
                    "Vir Chakra",
                    "Kirti Chakra",
                    "Sena Medal"
                ],
                "correct_answer": "Maha Vir Chakra",
                "explanation": "The Maha Vir Chakra (MVC) is the second highest military decoration in India, awarded for acts of conspicuous gallantry in the presence of the enemy.",
                "points": 1
            },
            {
                "id": 5808,
                "topic_id": 58,
                "question": "Geetanjali Shree won the International Booker Prize in 2022 for the translated novel 'Tomb of Sand', originally written in which language?",
                "options_json": [
                    "Hindi ('Ret Samadhi')",
                    "Bengali",
                    "Marathi",
                    "Urdu"
                ],
                "correct_answer": "Hindi ('Ret Samadhi')",
                "explanation": "Geetanjali Shree's novel 'Ret Samadhi', translated into English as 'Tomb of Sand' by Daisy Rockwell, was the first novel translated from Hindi to win the International Booker Prize.",
                "points": 1
            },
            {
                "id": 5809,
                "topic_id": 58,
                "question": "The prestigious Dronacharya Award in India is conferred upon:",
                "options_json": [
                    "Outstanding coaches in sports and games",
                    "Athletes with lifetime performance",
                    "Young aspiring athletes",
                    "University sports champions"
                ],
                "correct_answer": "Outstanding coaches in sports and games",
                "explanation": "Instituted in 1985, the Dronacharya Award is presented annually by the Ministry of Youth Affairs and Sports to outstanding sports coaches.",
                "points": 1
            },
            {
                "id": 5810,
                "topic_id": 58,
                "question": "Who was the first Indian woman to win the Booker Prize for Fiction in 1997?",
                "options_json": [
                    "Arundhati Roy ('The God of Small Things')",
                    "Kiran Desai ('The Inheritance of Loss')",
                    "Jhumpa Lahiri",
                    "Anita Desai"
                ],
                "correct_answer": "Arundhati Roy ('The God of Small Things')",
                "explanation": "Arundhati Roy won the Booker Prize in 1997 for her debut novel 'The God of Small Things', becoming the first resident Indian citizen to win the award.",
                "points": 1
            }
        ]
    }
}
