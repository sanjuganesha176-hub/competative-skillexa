# English Group C: Topics 9, 10, 11
# 9: Tenses, 10: Articles, 11: Subject-Verb Agreement

GROUP_C_DATA = {
    9: {
        "title": "Tenses: Timeline Logic, Aspectual Nuances, Sequence of Tenses & Conditionals",
        "source_id": 1,
        "content": {
            "definition": "Tense is a verbal category that anchors an action, event, or state of being in time (Past, Present, or Future) while portraying its grammatical aspect (Simple/Indefinite, Continuous/Progressive, Perfect, or Perfect Continuous). In competitive examinations, tenses form the core of error detection, testing Sequence of Tenses, past perfect precedence, and the Four Types of Conditional Sentences.",
            "overview": "The 12 English tenses combine three time dimensions with four aspectual states. Critical competitive exam principles include: the Sequence of Tenses (a past principal clause demands a past subordinate clause), the Past Perfect requirement for the earlier of two completed past events, and the strict structural formulas governing Zero, First, Second, and Third Conditionals.",
            "types": [
                {
                    "name": "1. Present Tense Family (4 Aspects)",
                    "desc": "Grounding events in the present timeline.",
                    "examples": [
                        "Simple Present (V1/V-s): Habitual actions, scientific universal truths, scheduled futures ('Water boils at 100°C')",
                        "Present Continuous (is/am/are + V-ing): Actions ongoing at the moment of speech ('The committee is drafting the bill')",
                        "Present Perfect (has/have + V3): Past actions with current relevance, signaled by 'already', 'yet', 'just' ('She has cleared the exam')",
                        "Present Perfect Continuous (has/have been + V-ing): Action commenced in past and continuing into present, signaled by since/for ('He has been studying since dawn')"
                    ]
                },
                {
                    "name": "2. Past Tense Family (4 Aspects)",
                    "desc": "Representing concluded historical or narrative actions.",
                    "examples": [
                        "Simple Past (V2): Completed action at a definite past time, signaled by yesterday, in 1947, ago ('India achieved independence in 1947')",
                        "Past Continuous (was/were + V-ing): Action in progress at a past moment ('I was reading when the lights failed')",
                        "Past Perfect (had + V3): The 'Past of the Past' - completed PRIOR to another past event ('The train had departed before we reached the platform')",
                        "Past Perfect Continuous (had been + V-ing): Action sustained up to a specific past milestone"
                    ]
                },
                {
                    "name": "3. Future Tense Family (4 Aspects)",
                    "desc": "Conveying prospective intentions, projections, and scheduled deadlines.",
                    "examples": [
                        "Simple Future (will/shall + V1): Spontaneous decisions, predictions ('The inflation rate will stabilize')",
                        "Future Continuous (will be + V-ing): Ongoing action at a future time ('Tomorrow at noon, she will be interviewing candidates')",
                        "Future Perfect (will have + V3): Action that WILL BE COMPLETED by a specified future deadline, signaled by 'by + time' ('By next December, he will have completed his doctorate')",
                        "Future Perfect Continuous (will have been + V-ing): Duration sustained up to a future point"
                    ]
                },
                {
                    "name": "4. The Four Conditional Sentences",
                    "desc": "Hypothetical frameworks linking condition clauses (If-clause) with result clauses.",
                    "examples": [
                        "Zero Conditional (General Truths): If + Simple Present -> Simple Present ('If you heat ice, it melts')",
                        "First Conditional (Real/Probable Future): If + Simple Present -> will/shall/can + V1 ('If he works diligently, he will clear the tier-1 exam')",
                        "Second Conditional (Unreal/Hypothetical Present): If + Simple Past (were/V2) -> would/could + V1 ('If I possessed the authority, I would approve the project')",
                        "Third Conditional (Unfulfilled Past Opportunity): If + had + V3 -> would have + V3 ('If you had informed me earlier, I would have attended the hearing')"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Past Perfect Precedence Rule (Two Past Actions)",
                    "explanation": "When two past actions occurred consecutively, the EARLIER action must be rendered in the Past Perfect (had + V3), while the SUBSEQUENT action must be in the Simple Past (V2).",
                    "words": ["Past Perfect", "Simple Past", "Before", "Earlier Action"],
                    "correct": "The patient had died before the ambulance arrived at the scene.",
                    "incorrect": "The patient died before the ambulance arrived at the scene."
                },
                {
                    "rule_number": 2,
                    "title": "Universal Truths Exempt from Past Sequence of Tenses",
                    "explanation": "Although a past-tense principal clause generally turns the subordinate clause past, universal scientific truths, mathematical facts, and geographic axioms REMAIN in the Simple Present.",
                    "words": ["Sequence of Tenses", "Universal Truth", "Simple Present"],
                    "correct": "The teacher stated that the Earth revolves around the Sun.",
                    "incorrect": "The teacher stated that the Earth revolved around the Sun."
                },
                {
                    "rule_number": 3,
                    "title": "Third Conditional Formula: 'If + had + V3, would have + V3'",
                    "explanation": "In an unfulfilled past condition, the conditional clause requires 'had + V3' and the main clause requires 'would have + V3'. A common exam trap is writing 'would have' in the if-clause.",
                    "words": ["Third Conditional", "Had + V3", "Would have + V3"],
                    "correct": "If the fire brigade had responded promptly, they would have saved the warehouse.",
                    "incorrect": "If the fire brigade would have responded promptly, they would have saved the warehouse."
                },
                {
                    "rule_number": 4,
                    "title": "Future Tense Prohibited in Time & Conditional Clauses",
                    "explanation": "In complex sentences projecting future events, the subordinate time or conditional clause (introduced by if, when, as soon as, until, unless, before) MUST be in the Simple Present, NEVER in the future (will/shall).",
                    "words": ["Conditional Clause", "Time Clause", "Simple Present", "Prohibition of Will"],
                    "correct": "When the president arrives tomorrow, the military guard of honor will salute him.",
                    "incorrect": "When the president will arrive tomorrow, the military guard of honor will salute him."
                },
                {
                    "rule_number": 5,
                    "title": "Future Perfect Triggered by 'By + Future Time'",
                    "explanation": "Whenever a sentence specifies a future deadline marked by 'by + time' (by next month, by 2030, by the end of the day), the main clause must use the Future Perfect tense (will have + V3).",
                    "words": ["By + time", "Future Perfect", "Will have + V3"],
                    "correct": "By the end of this financial year, the corporation will have opened fifty new retail outlets.",
                    "incorrect": "By the end of this financial year, the corporation will open fifty new retail outlets."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using 'would have' in the conditional If-clause ('If I would have known, I would have helped')",
                    "correction": "Use 'had + V3' in the If-clause: 'If I had known, I would have helped.'",
                    "rationale": "'Would have' is restricted to the main result clause; the conditional condition clause requires 'had + V3'."
                },
                {
                    "mistake": "Using 'will' in subordinate time clauses ('I will call you when I will reach home')",
                    "correction": "Use simple present: 'I will call you when I reach home.'",
                    "rationale": "Subordinate temporal clauses take simple present to express future contingencies."
                },
                {
                    "mistake": "Using present perfect with definite past time markers ('He has graduated in 2020')",
                    "correction": "Use simple past: 'He graduated in 2020.'",
                    "rationale": "Specific past time expressions (in 2020, yesterday, five days ago) strictly require the simple past."
                },
                {
                    "mistake": "Changing universal truths to past tense in indirect speech ('Copernicus proved that the Earth was round')",
                    "correction": "Keep simple present: 'Copernicus proved that the Earth is round.'",
                    "rationale": "Universal scientific facts remain timelessly true and resist past tense back-shifting."
                }
            ],
            "quick_revision_points": [
                "Two past actions: Earlier action = Had + V3 (Past Perfect); Later action = V2 (Simple Past).",
                "Third conditional: 'If + had + V3, ... would have + V3'. Never put 'would have' in the if-clause.",
                "Subordinate clauses of time and condition (when, if, as soon as, unless) take Simple Present, not will/shall.",
                "Universal truths and scientific laws never change to past tense in subordinate clauses.",
                "Deadlines marked by 'By + time' require Future Perfect (will have + V3).",
                "Past time markers (yesterday, ago, in 1947) mandate Simple Past (V2), not Present Perfect."
            ]
        },
        "practice": [
            {
                "question": "Spot the error in the following conditional sentence:\n'If the chief engineer would have calibrated the instruments properly, the launch would not have failed.'",
                "options_json": [
                    "If the chief engineer would have calibrated",
                    "the instruments properly",
                    "the launch would not have",
                    "failed"
                ],
                "correct_answer": "If the chief engineer would have calibrated",
                "explanation": "In an unfulfilled past conditional, the 'if'-clause requires 'had + V3' ('If the chief engineer had calibrated'), never 'would have'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the sentence that correctly applies the Past Perfect precedence rule for two sequential past events:",
                "options_json": [
                    "The express train had already departed before we reached the railway terminal.",
                    "The express train already departed before we had reached the railway terminal.",
                    "The express train departed before we reached the railway terminal.",
                    "The express train has departed before we had reached the terminal."
                ],
                "correct_answer": "The express train had already departed before we reached the railway terminal.",
                "explanation": "The train departure occurred prior to our reaching the platform; hence the earlier action requires Past Perfect ('had departed') and the latter requires Simple Past ('reached').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Fill in the blank with the appropriate future tense form:\n'By next November, the construction consortium ______ the transnational railway corridor.'",
                "options_json": ["will have completed", "will complete", "is completing", "completes"],
                "correct_answer": "will have completed",
                "explanation": "The deadline marker 'By next November' denotes a future completion milestone, strictly mandating Future Perfect ('will have completed').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Select the correct sentence observing the prohibition of 'will' in subordinate time clauses:",
                "options_json": [
                    "As soon as the governor signs the proclamation, it will become constitutional law.",
                    "As soon as the governor will sign the proclamation, it will become constitutional law.",
                    "As soon as the governor would sign the proclamation, it becomes law.",
                    "As soon as the governor is signing the proclamation, it will become law."
                ],
                "correct_answer": "As soon as the governor signs the proclamation, it will become constitutional law.",
                "explanation": "Subordinate clauses introduced by 'as soon as' must use the Simple Present ('signs') to reference future time.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following sentences correctly preserves the present tense for an eternal scientific truth?",
                "options_json": [
                    "The astronomer demonstrated that light travels faster than sound in a vacuum.",
                    "The astronomer demonstrated that light traveled faster than sound in a vacuum.",
                    "The astronomer demonstrated that light had traveled faster than sound in a vacuum.",
                    "The astronomer demonstrated that light will travel faster than sound."
                ],
                "correct_answer": "The astronomer demonstrated that light travels faster than sound in a vacuum.",
                "explanation": "Universal scientific realities remain in the Simple Present ('light travels faster') despite a past principal verb ('demonstrated').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error: 'The renowned archaeologist has discovered the ancient bronze relics two years ago.'",
                "options_json": [
                    "'has discovered' should be 'discovered'",
                    "'ancient' should be 'antique'",
                    "'two years ago' should be 'since two years'",
                    "There is no error in the sentence"
                ],
                "correct_answer": "'has discovered' should be 'discovered'",
                "explanation": "The specific past time indicator 'two years ago' precludes the Present Perfect; it requires the Simple Past 'discovered'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "What is the structural formula for a Second Conditional sentence (unreal/hypothetical present)?",
                "options_json": [
                    "If + Simple Past (V2/were) -> would/could + base verb (V1)",
                    "If + had + V3 -> would have + V3",
                    "If + Simple Present -> will + V1",
                    "If + Present Continuous -> would + V1"
                ],
                "correct_answer": "If + Simple Past (V2/were) -> would/could + base verb (V1)",
                "explanation": "Second conditional uses Simple Past in the If-clause and 'would/could + V1' in the main clause.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'I am having two cars' considered incorrect in formal English when expressing ownership?",
                "options_json": [
                    "'Have' is a stative verb of possession and cannot take continuous form in this sense; say 'I have two cars'.",
                    "'Cars' cannot be quantified.",
                    "'Am' is an ungrammatical auxiliary.",
                    "The sentence is completely correct."
                ],
                "correct_answer": "'Have' is a stative verb of possession and cannot take continuous form in this sense; say 'I have two cars'.",
                "explanation": "When 'have' denotes ownership, it is stative and cannot be used in continuous tenses.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "In the third conditional formula, the 'if'-clause takes 'had + ______'.",
                "correct_answer": "V3",
                "explanation": "Past perfect: had + past participle (V3).",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "When an action began in the past and is still ongoing with 'since' or 'for', use the Present Perfect ______ tense.",
                "correct_answer": "Continuous",
                "explanation": "Present Perfect Continuous (has/have been + V-ing).",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    10: {
        "title": "Articles: Definite, Indefinite, Phonetic Vowel Sounds & Zero Article Rules",
        "source_id": 1,
        "content": {
            "definition": "Articles are specialized determiners categorized into Indefinite (A, An) and Definite (The) that indicate whether a noun refers to a specific, unique entity or to an unparticularized member of a class. In competitive examinations, articles are heavily tested through phonetic initial sounds ('an honest man' vs. 'a European'), geographic names, and the rigorous rules governing the Omission of Articles (Zero Article).",
            "overview": "The choice between 'a' and 'an' is determined entirely by phonetic sound (vowel vs. consonant phoneme), NOT by orthographic spelling. The definite article 'the' is used with unique entities, superlative degrees, holy scriptures, geographical features (oceans, mountain ranges, archipelagos), and ordinal numbers, while being strictly omitted before abstract nouns, materials, meals, languages, and proper nouns in general statements.",
            "types": [
                {
                    "name": "1. Indefinite Articles: 'A' vs. 'An' (Phonetic Sound Rule)",
                    "desc": "Used before singular countable nouns mentioned for the first time.",
                    "examples": [
                        "'A' precedes CONSONANT SOUNDS: a book, a university (starts with /j/ consonant sound), a European, a one-rupee coin (starts with /w/ sound), a union",
                        "'An' precedes VOWEL SOUNDS (/æ/, /e/, /ɪ/, /ɒ/, /ʌ/): an apple, an elephant, an honest officer (silent 'h'), an hourly rate, an MP, an FIR, an MBBS doctor (letters pronounced with initial vowel sounds: /em/, /ef/)"
                    ]
                },
                {
                    "name": "2. Definite Article: 'The' (Mandatory Usage)",
                    "desc": "Specifies a particularized noun known to speaker and listener.",
                    "examples": [
                        "Unique Celestial Entities: The Sun, the Moon, the Earth, the Equator",
                        "Oceans, Seas, Rivers & Gulfs: The Indian Ocean, the Arabian Sea, the Ganges, the Persian Gulf",
                        "Mountain Ranges & Archipelagos: The Himalayas, the Alps, the Andaman and Nicobar Islands (NEVER with individual peaks like Mount Everest)",
                        "Countries with plural or political union titles: The United States, the United Kingdom, the Netherlands, the Philippines",
                        "Superlatives & Ordinals: The highest mountain, the first chapter, the only survivor",
                        "Sacred Scriptures & Historic Monuments: The Vedas, the Bible, the Taj Mahal, the Red Fort"
                    ]
                },
                {
                    "name": "3. Omission of Articles (Zero Article / Ø)",
                    "desc": "Contexts where standard grammar strictly prohibits the inclusion of any article.",
                    "examples": [
                        "Before Abstract & Material Nouns used in general: 'Honesty is the best policy' (NOT 'The honesty'), 'Gold is a precious metal'",
                        "Before Names of Languages: 'She speaks English fluently' (Note: 'The English' means the English people)",
                        "Before Names of Meals: 'Breakfast is served at 8:00 AM' (unless specific: 'The dinner hosted by the president was lavish')",
                        "Before Names of Diseases: 'Cholera broke out in the valley' (Exceptions: the measles, the mumps, the flu, the plague)",
                        "Before School, College, Church, Hospital, Bed when visited for their primary institutional purpose: 'He goes to school every day'"
                    ]
                },
                {
                    "name": "4. Repeating vs. Single Article with Dual Nouns",
                    "desc": "Grammatical marker distinguishing whether one person or two people are described.",
                    "examples": [
                        "Single Article (ONE person holding two posts): 'The director and producer has arrived' (Singular verb)",
                        "Double Article (TWO distinct persons): 'The director and the producer have arrived' (Plural verb)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Phonetic Sound Determines 'A' vs. 'An'",
                    "explanation": "Use 'an' before words beginning with a vowel SOUND regardless of spelling (an honest man, an heir, an honor, an MP, an SP, an MBA). Use 'a' before words beginning with a consonant SOUND (a European, a university, a utensil, a one-eyed man).",
                    "words": ["Phonetic Vowel Sound", "Consonant Sound", "Silent H", "Acronyms"],
                    "correct": "He registered an FIR at the local police station.",
                    "incorrect": "He registered a FIR at the local police station."
                },
                {
                    "rule_number": 2,
                    "title": "'The' with Mountain Ranges, but NEVER with Individual Peaks",
                    "explanation": "Use 'the' before chains or ranges of mountains (The Himalayas, the Andes, the Alps). NEVER use 'the' before single individual peaks or mountains (Mount Everest, Mount Abu, Kanchenjunga).",
                    "words": ["The Himalayas", "Mount Everest", "Mountain Range", "Single Peak"],
                    "correct": "Mount Everest is the highest mountain peak in the Himalayas.",
                    "incorrect": "The Mount Everest is the highest mountain peak in Himalayas."
                },
                {
                    "rule_number": 3,
                    "title": "Dual Comparison: 'The more... The more'",
                    "explanation": "When two parallel clauses express proportional increase or decrease using comparative adjectives, BOTH comparatives must be preceded by the definite article 'the'.",
                    "words": ["The more... the more", "Proportional Comparison", "Parallelism"],
                    "correct": "The higher you ascend up the mountain, the cooler you feel.",
                    "incorrect": "Higher you ascend up the mountain, cooler you feel."
                },
                {
                    "rule_number": 4,
                    "title": "Omission of Articles with Places Visited for Primary Purpose",
                    "explanation": "Do not use 'the' before school, college, university, church, temple, hospital, prison, or bed when visited for their primary inherent purpose (e.g., studying, worship, medical treatment, incarceration). Use 'the' ONLY when visiting for an incidental secondary purpose.",
                    "words": ["School", "Hospital", "Temple", "Prison", "Primary Purpose"],
                    "correct": "The injured pedestrian was rushed to hospital for emergency surgery.",
                    "incorrect": "The injured pedestrian was rushed to the hospital for emergency surgery."
                },
                {
                    "rule_number": 5,
                    "title": "Single vs. Repeated Article Governing Subject Number",
                    "explanation": "When two nouns connected by 'and' represent the same individual or office, use an article before the first noun only; the verb must be singular. If an article precedes both nouns, two distinct individuals are indicated, requiring a plural verb.",
                    "words": ["Single Article", "Double Article", "Subject Agreement"],
                    "correct": "The secretary and treasurer has submitted his annual audit report.",
                    "incorrect": "The secretary and the treasurer has submitted his annual audit report."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using 'a' before acronyms starting with vowel sounds ('a FIR', 'a MP', 'a NGO')",
                    "correction": "Use 'an': 'an FIR', 'an MP', 'an NGO'.",
                    "rationale": "Letters F, M, N, R, S, X are pronounced with initial vowel sounds (/ef/, /em/, /en/, /ar/, /es/, /eks/)."
                },
                {
                    "mistake": "Adding 'the' before individual mountain peaks ('The Mount Everest is majestic')",
                    "correction": "Omit 'the': 'Mount Everest is majestic.'",
                    "rationale": "Single peaks do not take the definite article; only entire mountain ranges take 'the'."
                },
                {
                    "mistake": "Using 'the' before abstract nouns used generally ('The honesty is a virtue')",
                    "correction": "Omit 'the': 'Honesty is a virtue.'",
                    "rationale": "Abstract nouns in general statements take the zero article."
                },
                {
                    "mistake": "Saying 'He is learning the English language' vs. 'He speaks the English'",
                    "correction": "Say 'He speaks English.'",
                    "rationale": "'English' refers to the language; 'The English' refers to the English people."
                }
            ],
            "quick_revision_points": [
                "A vs. An is based on initial pronunciation sound, NOT written alphabet letter.",
                "Use 'an' before: honest, hour, heir, MP, FIR, MBA, SP, NRI, X-ray.",
                "Use 'a' before: university, European, one-rupee note, uniform, utensil.",
                "Use 'The' with: mountain ranges, rivers, oceans, holy books, unique bodies, superlatives.",
                "Never use 'The' with: individual mountain peaks, abstract nouns in general, names of languages.",
                "Parallel comparatives require 'The': 'The higher we go, the colder it becomes'.",
                "Single article before two coordinated nouns = 1 person (singular verb); Double article = 2 persons (plural verb)."
            ]
        },
        "practice": [
            {
                "question": "Spot the error in the following sentence:\n'The victim walked to the local police headquarters to lodge a FIR against the cyber fraudsters.'",
                "options_json": [
                    "The victim walked",
                    "to the local police headquarters",
                    "to lodge a FIR",
                    "against the cyber fraudsters"
                ],
                "correct_answer": "to lodge a FIR",
                "explanation": "The letter 'F' in FIR is phonetically pronounced /ef/, beginning with a short vowel sound /e/. Therefore, the correct indefinite article is 'an FIR', not 'a FIR'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the sentence that correctly applies the rule of articles to mountain geography:",
                "options_json": [
                    "Mount Everest is the highest mountain peak in the Himalayas.",
                    "The Mount Everest is the highest mountain peak in the Himalayas.",
                    "Mount Everest is the highest mountain peak in Himalayas.",
                    "The Mount Everest is highest peak in Himalayas."
                ],
                "correct_answer": "Mount Everest is the highest mountain peak in the Himalayas.",
                "explanation": "Individual mountain peaks (Mount Everest) take no article; mountain ranges (the Himalayas) take the definite article 'the'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Fill in the blank with the appropriate article:\n'He has been appointed as ______ executive director of the national monetary authority.'",
                "options_json": ["an", "a", "the", "No article needed"],
                "correct_answer": "the",
                "explanation": "A unique, prestigious executive title or specific administrative post takes the definite article 'the'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the sentence observing the rule of parallel double comparatives:",
                "options_json": [
                    "The more you practice solving numerical problems, the faster you become.",
                    "More you practice solving numerical problems, faster you become.",
                    "The more you practice solving numerical problems, faster you become.",
                    "More you practice solving numerical problems, the faster you become."
                ],
                "correct_answer": "The more you practice solving numerical problems, the faster you become.",
                "explanation": "In dual comparative proportional structures, both clauses must open with 'the + comparative' ('The more... the faster').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'The gold is a malleable and precious metal' grammatically incorrect in standard English?",
                "options_json": [
                    "Material nouns used in a general, universal sense take no article (Zero Article).",
                    "'Gold' cannot be modified by adjectives.",
                    "'Precious' requires the definite article.",
                    "'Metal' must always be plural."
                ],
                "correct_answer": "Material nouns used in a general, universal sense take no article (Zero Article).",
                "explanation": "Material and abstract nouns used universally take no article: 'Gold is a malleable and precious metal.'",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "What is the distinction between 'The director and producer has arrived' and 'The director and the producer have arrived'?",
                "options_json": [
                    "The first describes one person holding both titles; the second describes two distinct individuals.",
                    "The first is ungrammatical.",
                    "The second describes one person.",
                    "Both sentences mean exactly the same thing."
                ],
                "correct_answer": "The first describes one person holding both titles; the second describes two distinct individuals.",
                "explanation": "Repeating the article indicates two separate individuals requiring a plural verb; a single article denotes a single individual requiring a singular verb.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following words correctly takes the indefinite article 'a' rather than 'an'?",
                "options_json": ["University (pronounced with initial consonant /j/)", "Honest", "Heir", "MP"],
                "correct_answer": "University (pronounced with initial consonant /j/)",
                "explanation": "'University' begins phonetically with the consonant glide /j/ (yoo-ni-ver-si-ty), taking 'a'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct sentence when referring to the primary purpose of an institution:",
                "options_json": [
                    "The prisoner was sentenced to three years in prison.",
                    "The prisoner was sentenced to three years in the prison.",
                    "The prisoner was sentenced to three years in a prison.",
                    "The prisoner was sentenced to three years in this prison."
                ],
                "correct_answer": "The prisoner was sentenced to three years in prison.",
                "explanation": "Places like prison, school, and hospital take no article when used for their primary institutional purpose.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Before words beginning with a vowel sound (such as 'honest' or 'hour'), we use the indefinite article '______'.",
                "correct_answer": "an",
                "explanation": "An honest man, an hour.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The definite article 'The' is used before mountain ranges like the Himalayas, but never before individual mountain ______.",
                "correct_answer": "peaks",
                "explanation": "Single mountain peaks (like Mount Everest) take no article.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    11: {
        "title": "Subject-Verb Agreement: Proximity Rules, Compound Subjects & Inversion Concord",
        "source_id": 1,
        "content": {
            "definition": "Subject-Verb Agreement (Grammatical Concord) is the fundamental syntactical requirement that a finite verb must correspond in person (First, Second, Third) and number (Singular, Plural) with its grammatical subject. In competitive examinations, subject-verb agreement is the single most tested grammar topic across SSC CGL, Bank PO, and CDS.",
            "overview": "While simple sentences pair singular subjects with singular verbs, complexity arises in competitive exams when intervening parenthetical phrases ('along with', 'as well as') separate the subject from the verb, when correlative disjunctions ('either... or', 'neither... nor') trigger the Law of Proximity, when collective nouns shift between corporate unity and individual fraction, and when indefinite pronouns govern agreement.",
            "types": [
                {
                    "name": "1. Intervening Parenthetical Phrases",
                    "desc": "Phrases inserted between the subject and verb that DO NOT affect the number of the subject.",
                    "examples": [
                        "Connectors: as well as, along with, together with, accompanied by, in addition to, besides, with, rather than, like, unlike",
                        "Rule: The verb agrees STRICTLY with the primary FIRST subject preceding these phrases",
                        "Example: 'The captain, along with all his sailors, was drowned' (subject is singular 'captain')"
                    ]
                },
                {
                    "name": "2. Correlative Disjunctions & The Law of Proximity",
                    "desc": "Conjunctions linking two subjects where proximity to the verb determines concord.",
                    "examples": [
                        "Pairs: Either... or, Neither... nor, Not only... but also, Or, Nor",
                        "Law of Proximity: The verb agrees in number and person with the subject NEAREST to it",
                        "Example: 'Neither the manager nor his assistants were present' vs. 'Neither the assistants nor the manager was present'"
                    ]
                },
                {
                    "name": "3. Collective Nouns (Unanimity vs. Division)",
                    "desc": "Nouns denoting groups of individuals (jury, committee, team, board, parliament, crowd).",
                    "examples": [
                        "Unanimous Unit (Singular verb): 'The jury has reached its verdict' (acting as one cohesive body)",
                        "Divided Members (Plural verb): 'The jury were divided in their opinions' (individual members in conflict)"
                    ]
                },
                {
                    "name": "4. Indefinite Pronouns, Quantities & Fractions",
                    "desc": "Pronouns and fractional expressions governing agreement.",
                    "examples": [
                        "Always Singular: Each, every, either, neither, everyone, somebody, nobody, one",
                        "Always Plural: Both, few, many, several",
                        "Fractions & Percentages (SANAM rule): Governed by the following noun ('Two-thirds of the book is read' vs. 'Two-thirds of the books are sold')"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "First Subject Governs 'As Well As / Along With' Structures",
                    "explanation": "When two subjects are joined by 'as well as', 'along with', 'together with', 'with', 'accompanied by', 'in addition to', 'besides', 'no less than', or 'rather than', the verb must agree in number and person strictly with the FIRST subject.",
                    "words": ["As well as", "Along with", "Together with", "In addition to", "First Subject"],
                    "correct": "The Prime Minister, accompanied by senior cabinet ministers, has arrived in Geneva.",
                    "incorrect": "The Prime Minister, accompanied by senior cabinet ministers, have arrived in Geneva."
                },
                {
                    "rule_number": 2,
                    "title": "Law of Proximity with 'Either... Or' and 'Neither... Nor'",
                    "explanation": "When two subjects are connected by 'either... or', 'neither... nor', 'not only... but also', or 'or', the verb must agree in number and person with the NEAREST subject.",
                    "words": ["Either... or", "Neither... nor", "Proximity Rule", "Nearest Subject"],
                    "correct": "Neither the teacher nor the students were satisfied with the revised syllabus.",
                    "incorrect": "Neither the teacher nor the students was satisfied with the revised syllabus."
                },
                {
                    "rule_number": 3,
                    "title": "'More than one' Takes Singular; 'More than two' Takes Plural",
                    "explanation": "'More than one' is followed by a singular countable noun and a SINGULAR verb (e.g., 'More than one candidate was disqualified'). However, 'More candidates than one were disqualified' takes a plural verb.",
                    "words": ["More than one", "Singular Verb", "Number Concord"],
                    "correct": "More than one proposal was submitted to the investment committee.",
                    "incorrect": "More than one proposals were submitted to the investment committee."
                },
                {
                    "rule_number": 4,
                    "title": "Plural Expressions Denoting a Single Fixed Quantity",
                    "explanation": "When a plural noun denotes a specific, single collective quantity or unit of time, money, distance, or weight, it takes a SINGULAR verb.",
                    "words": ["Distance", "Sum of Money", "Fixed Unit", "Singular Verb"],
                    "correct": "Ten kilometers is a grueling distance to run in sweltering heat.",
                    "incorrect": "Ten kilometers are a grueling distance to run in sweltering heat."
                },
                {
                    "rule_number": 5,
                    "title": "The Relative Clause Antecedent Concord Rule",
                    "explanation": "In structures like 'one of the [plural noun] who/that...', the relative pronoun refers back to the PLURAL noun antecedent; therefore, the verb inside the relative clause must be PLURAL. However, with 'the ONLY one of the [plural noun] who...', the verb is SINGULAR.",
                    "words": ["One of the", "The only one of the", "Relative Clause Concord"],
                    "correct": "He is one of the brightest scientists who have graduated from this institute.",
                    "incorrect": "He is one of the brightest scientists who has graduated from this institute."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using a plural verb after 'as well as' when the first subject is singular ('The king as well as his courtiers were captured')",
                    "correction": "Use singular verb: 'The king as well as his courtiers was captured.'",
                    "rationale": "'Courtiers' is part of an intervening parenthetical prepositional phrase; the primary subject is singular 'king'."
                },
                {
                    "mistake": "Using a singular verb in 'He is one of those men who does not cheat'",
                    "correction": "Use plural verb: 'He is one of those men who do not cheat.'",
                    "rationale": "The antecedent of 'who' is the plural noun 'men', which requires the plural verb 'do'."
                },
                {
                    "mistake": "Treating fixed distances or monetary amounts as plural ('Fifty thousand rupees are a huge sum')",
                    "correction": "Use singular verb: 'Fifty thousand rupees is a huge sum.'",
                    "rationale": "A single collective sum of money or fixed unit of measurement acts as a singular concept."
                },
                {
                    "mistake": "Violating the proximity rule in 'Neither the players nor the coach were present'",
                    "correction": "Use singular: 'Neither the players nor the coach was present.'",
                    "rationale": "The verb must agree with the nearest subject, which is the singular 'coach'."
                }
            ],
            "quick_revision_points": [
                "Subjects joined by 'as well as', 'along with', 'with', 'together with': Verb agrees with the FIRST subject.",
                "Subjects joined by 'either... or', 'neither... nor': Verb agrees with the NEAREST subject (Proximity Rule).",
                "'One of the + plural noun + who/that' takes a PLURAL verb.",
                "'The only one of the + plural noun + who/that' takes a SINGULAR verb.",
                "Fixed amounts of distance, time, and money take a SINGULAR verb (e.g., '10 miles is...').",
                "Collective nouns take singular verbs when united, and plural verbs when divided in opinion."
            ]
        },
        "practice": [
            {
                "question": "Spot the error in the following sentence:\n'The commanding general, accompanied by three senior intelligence officers, have arrived at the frontline bunker.'",
                "options_json": [
                    "The commanding general",
                    "accompanied by three senior intelligence officers",
                    "have arrived at",
                    "the frontline bunker"
                ],
                "correct_answer": "have arrived at",
                "explanation": "When a subject is joined with other nouns using 'accompanied by', the verb agrees strictly with the first subject ('The commanding general' - singular). Hence, it should read: 'has arrived at'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Apply the Law of Proximity to identify the correct sentence with 'Neither... nor':",
                "options_json": [
                    "Neither the chief editor nor the journalists were convinced by the government press release.",
                    "Neither the chief editor nor the journalists was convinced by the government press release.",
                    "Neither the journalists nor the chief editor were convinced by the government press release.",
                    "Neither the journalists nor the chief editor are convinced yesterday."
                ],
                "correct_answer": "Neither the chief editor nor the journalists were convinced by the government press release.",
                "explanation": "The nearest subject to the verb is the plural noun 'journalists', requiring the plural auxiliary 'were'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the correct sentence illustrating the relative clause antecedent rule with 'one of the':",
                "options_json": [
                    "Dr. Raman is one of the most distinguished professors who have ever taught at this university.",
                    "Dr. Raman is one of the most distinguished professors who has ever taught at this university.",
                    "Dr. Raman is one of the most distinguished professor who has ever taught at this university.",
                    "Dr. Raman is the one of distinguished professors who has taught."
                ],
                "correct_answer": "Dr. Raman is one of the most distinguished professors who have ever taught at this university.",
                "explanation": "The relative pronoun 'who' refers back to the plural antecedent 'professors', mandating the plural verb 'have taught'.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the sentence that correctly treats a fixed distance as a singular unit:",
                "options_json": [
                    "Twenty kilometers is an arduous distance to march carrying heavy tactical gear.",
                    "Twenty kilometers are an arduous distance to march carrying heavy tactical gear.",
                    "Twenty kilometers were an arduous distance for the single mile march.",
                    "Twenty kilometers have been an arduous distance."
                ],
                "correct_answer": "Twenty kilometers is an arduous distance to march carrying heavy tactical gear.",
                "explanation": "A collective unit of distance regarded as a single measurement takes a singular verb ('is').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Fill in the blank with the appropriate verb form:\n'More than one candidate ______ disqualified for violating the electronic device protocol.'",
                "options_json": ["was", "were", "are", "have been"],
                "correct_answer": "was",
                "explanation": "The standard construction 'More than one + singular noun' strictly takes a singular verb ('was disqualified').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the sentence that correctly reflects the division within a collective noun:",
                "options_json": [
                    "The parliamentary committee were divided in their opinions regarding the tax amendment.",
                    "The parliamentary committee was divided in their opinions regarding the tax amendment.",
                    "The parliamentary committee has divided in their opinions.",
                    "The parliamentary committee is divided in their opinions."
                ],
                "correct_answer": "The parliamentary committee were divided in their opinions regarding the tax amendment.",
                "explanation": "When members of a collective noun act individually or disagree in opinion, the noun takes a plural verb ('were divided') and plural possessive pronoun ('their').",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'The only one of the applicants who have been selected is Amit' incorrect?",
                "options_json": [
                    "Because 'the only one' restricts the antecedent to a single individual, requiring singular 'has been selected'.",
                    "'Applicants' must be singular.",
                    "'Amit' cannot follow the verb is.",
                    "The sentence is completely correct."
                ],
                "correct_answer": "Because 'the only one' restricts the antecedent to a single individual, requiring singular 'has been selected'.",
                "explanation": "The modifier 'the only one' makes the subject singular, requiring singular agreement: 'who has been selected'.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct sentence with 'as well as':",
                "options_json": [
                    "The ship, as well as its crew, was lost in the Bermuda Triangle.",
                    "The ship, as well as its crew, were lost in the Bermuda Triangle.",
                    "The ship, as well as its crew, have been lost.",
                    "The ship, as well as its crew, are lost."
                ],
                "correct_answer": "The ship, as well as its crew, was lost in the Bermuda Triangle.",
                "explanation": "The verb agrees with the first subject 'The ship' (singular), requiring 'was lost'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "When two subjects are joined by 'neither... nor', the verb must agree with the ______ subject.",
                "correct_answer": "nearest",
                "explanation": "The Law of Proximity mandates agreement with the nearest subject.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "In 'More than one soldier ______ injured in the combat operation', the correct singular auxiliary is 'was'.",
                "correct_answer": "was",
                "explanation": "'More than one' takes a singular verb.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    }
}
