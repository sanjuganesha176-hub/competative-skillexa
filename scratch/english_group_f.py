# English Group F: Topics 21, 22
# 21: Reading Comprehension, 22: Fill in the Blanks

GROUP_F_DATA = {
    "21": {
        "title": "Reading Comprehension: Structural Skimming, Scanning, Inferential Logic & Tone Analysis",
        "source_id": 1,
        "content": {
            "definition": "Reading Comprehension (RC) evaluates a candidate's ability to decode written discourse, isolate central theses, extract specific factual assertions, deduce logical inferences, and evaluate an author's tone and rhetorical structure under strict timed conditions. In competitive examinations (SSC CGL Tier-2, IBPS PO Mains, UPSC CSAT, CDS, CAT), RC passages demand systematic skimming and scanning techniques over passive linear reading.",
            "overview": "Effective comprehension operates on a three-tier cognitive strategy: (1) Macro-Reading (Skimming the opening paragraph, concluding remarks, and topic sentences to capture the central argument and structural roadmap); (2) Micro-Targeting (Scanning for proper nouns, technical terms, and dates to locate precise factual data); and (3) Inferential Deduction (Synthesizing unstated assumptions, logical implications, and authorial attitudes without introducing extraneous external bias).",
            "types": [
                {
                    "name": "1. Main Idea & Central Theme Questions",
                    "desc": "Testing synthesis of the author's primary objective or overarching thesis.",
                    "examples": [
                        "What is the primary purpose of the passage?",
                        "Which of the following best captures the central argument of the author?",
                        "A suitable title for the passage would be...",
                        "Strategy: The main idea must be neither too broad (encompassing unmentioned domains) nor too narrow (focusing on a single illustrative paragraph)."
                    ]
                },
                {
                    "name": "2. Direct Factual & Detail Retrieval Questions",
                    "desc": "Assessing rapid, accurate retrieval of explicitly stated information.",
                    "examples": [
                        "According to paragraph 2, what caused the decline in agricultural yields?",
                        "Which of the following was NOT mentioned as a constraint in the report?",
                        "Strategy: Scan passage for exact keywords/synonyms, locate the reference sentence, and verify against options."
                    ]
                },
                {
                    "name": "3. Inferential & Extrapolative Questions",
                    "desc": "Requiring logical conclusions that must necessarily be true based on the passage premises.",
                    "examples": [
                        "It can be inferred from the passage that the author believes...",
                        "Which of the following would the author most likely agree with?",
                        "Strategy: An inference is an unstated truth logically deduced from stated facts; it is NEVER an ungrounded wild conjecture."
                    ]
                },
                {
                    "name": "4. Author's Tone, Attitude & Rhetorical Stance Questions",
                    "desc": "Analyzing stylistic adjectives, qualifiers, and figurative choices to determine attitude.",
                    "examples": [
                        "Objective / Analytical (Dispassionate presentation of scientific facts and data)",
                        "Critical / Cynical / Derogatory (Highlighting flaws, pointing out hypocrisies or deficiencies)",
                        "Laudatory / Eulogistic (Praising achievements, expressing admiration)",
                        "Sarcastic / Caustic / Satirical (Using irony to mock or ridicule policies/behaviors)",
                        "Didactic / Pedagogical (Instructive, seeking to teach moral or practical lessons)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Passage-Bound Evidence Rule (Zero External Assumption)",
                    "explanation": "Every answer must be substantiated strictly by information explicitly stated or undeniably implied in the passage text. Even if an option is a universally acknowledged real-world scientific fact, if it is not supported by the passage, it must be rejected.",
                    "words": [
                        "Passage-Bound",
                        "Textual Evidence",
                        "No External Bias"
                    ],
                    "correct": "Select an answer because paragraph 3 explicitly documents the correlation.",
                    "incorrect": "Select an answer because you read a similar article in a newspaper last week (external bias)."
                },
                {
                    "rule_number": 2,
                    "title": "Extreme Language Elimination Rule",
                    "explanation": "Options containing absolute categorical terms ('always', 'never', 'solely', 'exclusively', 'completely impossible', 'undoubtedly') are almost always false in nuanced academic reading. Favor options phrased with moderate qualifiers ('tends to', 'can frequently', 'partially', 'is often associated with').",
                    "words": [
                        "Extreme Language",
                        "Categorical Qualifiers",
                        "Nuanced Options"
                    ],
                    "correct": "The policy may lead to unintended economic distress in rural sectors (Moderate).",
                    "incorrect": "The policy will invariably destroy every single rural business (Extreme categorical trap)."
                },
                {
                    "rule_number": 3,
                    "title": "Rhetorical Shift & Discourse Marker Sensitivity Rule",
                    "explanation": "Crucial authorial shifts occur immediately after contrastive discourse markers ('However', 'Nonetheless', 'Conversely', 'On the contrary', 'Despite this'). What precedes the connector is usually an opposing counterargument; what follows is the author's real thesis.",
                    "words": [
                        "Discourse Markers",
                        "However",
                        "Turn of Thought"
                    ],
                    "correct": "Focusing on the author's statement following 'Yet, recent archaeological excavations disprove this hypothesis.'",
                    "incorrect": "Adopting the preliminary hypothesis stated in line 1 before the 'Yet' reversal."
                },
                {
                    "rule_number": 4,
                    "title": "Main Idea Scope Rule: Neither Overly Broad Nor Overly Narrow",
                    "explanation": "When identifying the title or main idea, reject options that summarize only one supporting example (too narrow) or options that expand into sweeping universal philosophies not covered in the text (too broad).",
                    "words": [
                        "Main Idea",
                        "Scope",
                        "Broad vs Narrow"
                    ],
                    "correct": "The Impact of Artificial Intelligence on Contemporary Financial Auditing (Precisely covers text scope).",
                    "incorrect": "The Technological Evolution of Humanity (Too broad) OR Neural Networks in Fraud Alerts (Too narrow)."
                },
                {
                    "rule_number": 5,
                    "title": "Question-Stem Keyword Scanning Rule",
                    "explanation": "For factual questions, circle capitalized names, numbers, technical terminology, and distinct verbs in the question stem. Scan the passage vertically with your eyes to spot the anchor sentence before reading the options.",
                    "words": [
                        "Anchor Sentence",
                        "Scanning",
                        "Keyword Mapping"
                    ],
                    "correct": "Locating '1991 New Industrial Policy' in paragraph 2 and reading the surrounding 2 sentences.",
                    "incorrect": "Rereading the entire 600-word passage from paragraph 1 to answer a specific factual question."
                },
                {
                    "rule_number": 6,
                    "title": "Tone Vocabulary Accuracy Rule",
                    "explanation": "Distinguish between closely related tone descriptions: 'Skeptical' (doubting claims until evidence is presented) is distinct from 'Cynical' (believing people are purely motivated by selfish greed). 'Objective' is distinct from 'Indifferent'.",
                    "words": [
                        "Tone Analysis",
                        "Skeptical vs Cynical",
                        "Authorial Attitude"
                    ],
                    "correct": "The author's tone is skeptical because she questions the methodology and requests peer review.",
                    "incorrect": "The author's tone is cynical because she politely critiques the methodology."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Importing outside knowledge contrary to the passage.",
                    "correction": "Treat the passage as a closed, self-contained universe; if the author claims 'bats are reptiles', answer based on that premise within the test.",
                    "rationale": "Examiners specifically design questions where real-world knowledge contradicts the author's specific argument to catch careless readers."
                },
                {
                    "mistake": "Selecting an option that is factually true but does not answer the question asked.",
                    "correction": "Always re-read the question stem to verify what is being queried (e.g. cause vs consequence).",
                    "rationale": "An option can be a verbatim quote from paragraph 1, but if the question asks for the 'conclusion' in paragraph 4, it is incorrect."
                },
                {
                    "mistake": "Reading the passage too slowly word-by-word.",
                    "correction": "Use skimming (speed-reading for gist) for the first pass (60-90 seconds), then scan for specific questions.",
                    "rationale": "Spending 6 minutes reading a passage leaves inadequate time to solve the questions."
                },
                {
                    "mistake": "Failing to recognize negative question stems ('Which is NOT true', 'EXCEPT').",
                    "correction": "Underline 'NOT' or 'EXCEPT' in the question stem to avoid selecting the first true statement you see.",
                    "rationale": "Speed-induced oversight leads candidates to mark the first factually correct option they spot."
                }
            ],
            "quick_revision_points": [
                "Skimming = reading rapidly for general structure, main argument, and flow.",
                "Scanning = rapid eye sweep looking for specific keywords, numbers, names.",
                "Inference = an unstated conclusion that must logically follow from stated facts.",
                "Extreme words (always, never, all, impossible) are almost always incorrect.",
                "Look for pivot markers: 'However', 'Nonetheless', 'Yet' indicate the author's real view.",
                "Main idea must balance scope: reject too broad and too narrow choices.",
                "Tone: Objective (neutral facts), Critical (pointing out flaws), Didactic (teaching), Sarcastic (mocking).",
                "Passage-Bound: Never rely on outside assumptions or general knowledge."
            ]
        },
        "practice_questions": [
            {
                "id": 2101,
                "topic_id": 21,
                "question_text": "Read the short excerpt: 'While industrial automation undeniably boosts assembly-line throughput and eliminates physical drudgery, it concurrently threatens middle-tier clerical jobs. Policymakers who hail robotic adoption as an unalloyed blessing disregard the severe structural unemployment looming in legacy manufacturing belts.' What is the author's primary objective in this passage?",
                "question_type": "mcq",
                "options": [
                    "To advocate for the complete prohibition of robotic machinery in industry",
                    "To highlight the overlooked socioeconomic costs and employment disruptions of rapid automation",
                    "To celebrate the productivity gains achieved by manufacturing companies",
                    "To suggest that clerical workers should immediately retrain in computer programming"
                ],
                "correct_answer": "To highlight the overlooked socioeconomic costs and employment disruptions of rapid automation",
                "explanation": "The author presents both sides briefly but uses 'concurrently threatens' and critiques policymakers who view it as an 'unalloyed blessing', thereby emphasizing the neglected socioeconomic downsides.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2102,
                "topic_id": 21,
                "question_text": "Based on the sentence: 'The committee was not unimpressed by the candidate's credentials, yet doubts lingered regarding his administrative adaptability under crisis conditions.' What can be inferred about the committee's perception?",
                "question_type": "mcq",
                "options": [
                    "They completely rejected the candidate's academic qualifications.",
                    "They acknowledged his qualifications positively but harbored reservations about his crisis management capabilities.",
                    "They considered the candidate exceptionally skilled at handling crises.",
                    "They had no opinion regarding the candidate."
                ],
                "correct_answer": "They acknowledged his qualifications positively but harbored reservations about his crisis management capabilities.",
                "explanation": "'Not unimpressed' is a litotes meaning moderately impressed/positive, while 'yet doubts lingered regarding his administrative adaptability under crisis' indicates reservation about crisis handling.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2103,
                "topic_id": 21,
                "question_text": "What reading technique involves sweeping the eyes quickly across a passage looking specifically for dates, capitalized names, or isolated statistical figures without reading every word?",
                "question_type": "mcq",
                "options": [
                    "Skimming",
                    "Scanning",
                    "Intensive Reading",
                    "Extensive Reading"
                ],
                "correct_answer": "Scanning",
                "explanation": "'Scanning' is looking rapidly through text specifically to locate a particular piece of information (such as a date, name, or number). 'Skimming' is reading quickly to get the general idea or gist.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2104,
                "topic_id": 21,
                "question_text": "Identify the tone of the author in the following line: 'To proclaim that the municipal corporation has solved the city's monsoon flooding crisis simply because the mayor's own street remained dry is a triumph of political delusion over basic geography.'",
                "question_type": "mcq",
                "options": [
                    "Objective and detached",
                    "Laudatory and admiring",
                    "Sarcastic and biting",
                    "Didactic and spiritual"
                ],
                "correct_answer": "Sarcastic and biting",
                "explanation": "Phrases like 'simply because the mayor's own street remained dry' and 'a triumph of political delusion' convey sharp irony, sarcasm, and caustic critique.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2105,
                "topic_id": 21,
                "question_text": "Which of the following answer choices in an RC inference question should be viewed with MAXIMUM SKEPTICISM due to extreme language?",
                "question_type": "mcq",
                "options": [
                    "Technological innovations frequently alter consumer spending behaviors.",
                    "The proposed monetary reforms may occasionally lead to short-term inflation.",
                    "Every single developing nation will inevitably succumb to external debt defaults.",
                    "Certain regulatory interventions tend to mitigate systemic financial risks."
                ],
                "correct_answer": "Every single developing nation will inevitably succumb to external debt defaults.",
                "explanation": "Absolute categorical assertions containing 'Every single' and 'inevitably' represent classic extreme language traps that are rarely supported by nuanced texts.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2106,
                "topic_id": 21,
                "question_text": "Read the sentence: 'Notwithstanding the initial euphoria surrounding genomic therapy, clinical trials have revealed subtle immune-mediated adverse responses that necessitate circumspection before commercial rollout.' What does the word 'CIRCUMSPECTION' mean in this context?",
                "question_type": "mcq",
                "options": [
                    "Reckless speed",
                    "Careful deliberation and prudence",
                    "Outright prohibition",
                    "Public advertisement"
                ],
                "correct_answer": "Careful deliberation and prudence",
                "explanation": "'Circumspection' means thinking carefully about possible risks before doing or saying something; caution or prudence.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2107,
                "topic_id": 21,
                "question_text": "Fill in the blank with the appropriate strategy term: 'When approaching a long passage, an effective candidate uses __________ of the opening and closing paragraphs to quickly discern the author's thesis and structural roadmap.'",
                "question_type": "fitb",
                "options": [
                    "skimming",
                    "scanning",
                    "memorization",
                    "proofreading"
                ],
                "correct_answer": "skimming",
                "explanation": "'Skimming' is the technique of reading key structural parts rapidly to obtain the overarching thesis and organizational structure.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2108,
                "topic_id": 21,
                "question_text": "In a reading passage, if an author presents unbiased scientific data, details empirical methodologies, and avoids emotional adjectives, their tone is best characterized as:",
                "question_type": "mcq",
                "options": [
                    "Polemical",
                    "Objective",
                    "Patronizing",
                    "Nostalgic"
                ],
                "correct_answer": "Objective",
                "explanation": "An 'objective' tone presents facts, empirical data, and analysis without personal bias, emotional coloring, or prejudice.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2109,
                "topic_id": 21,
                "question_text": "When a question stem reads: 'Which of the following is NOT supported by the passage?', what is the most critical test-taking protocol?",
                "question_type": "mcq",
                "options": [
                    "Select the first fact that matches common knowledge",
                    "Verify each option against the text and select the one statement that is either contradicted or unmentioned",
                    "Skip the question as it contains an error",
                    "Select the longest option"
                ],
                "correct_answer": "Verify each option against the text and select the one statement that is either contradicted or unmentioned",
                "explanation": "In negative questions ('NOT supported' / 'EXCEPT'), three options will be true according to the passage; the correct answer is the single false or unmentioned claim.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2110,
                "topic_id": 21,
                "question_text": "Read the excerpt: 'The Renaissance was not merely an era of artistic rejuvenation; it fundamentally recalibrated philosophical inquiries into human agency.' What does the author imply?",
                "question_type": "mcq",
                "options": [
                    "The Renaissance produced no artistic masterpieces.",
                    "The impact of the Renaissance extended deeply into philosophy and humanism beyond its visual arts.",
                    "Human agency was invented during the Renaissance.",
                    "Artistic rejuvenation was the only significant achievement of the Renaissance."
                ],
                "correct_answer": "The impact of the Renaissance extended deeply into philosophy and humanism beyond its visual arts.",
                "explanation": "The 'not merely X; it fundamentally Y' rhetorical construction asserts that while X is true, Y is an equally or more profound dimension of the phenomenon.",
                "difficulty": "medium",
                "points": 1
            }
        ]
    },
    "22": {
        "title": "Fill in the Blanks: Syntactic Constraints, Collocations, Discourse Markers & Cloze Strategies",
        "source_id": 1,
        "content": {
            "definition": "Fill in the Blanks (FITB) and Cloze Test questions evaluate integrated grammatical and lexical competence. Candidates must evaluate a sentence or continuous paragraph containing missing words, utilizing syntactic constraints (part of speech, subject-verb concord, tense sequences, prepositional governance) and semantic indicators (contextual collocations, degree, discourse directionality, and tonal polarity) to identify the single correct lexical item.",
            "overview": "Solving FITB questions requires a systematic two-stage elimination model: (1) Syntactic Filtering (identifying what grammatical class and structural form must occupy the blank\u2014e.g., transitive verb in past participle, uncountable noun, adjective requiring the preposition 'of'); and (2) Semantic & Collocational Matching (evaluating which word among the grammatically viable candidates matches the exact tone, degree, and idiomatic pairing of the sentence).",
            "types": [
                {
                    "name": "1. Single-Blank Grammatical & Prepositional Determinations",
                    "desc": "Blanks governed by strict syntactic rules, phrasal verb structures, and fixed prepositions.",
                    "examples": [
                        "Fixed Preposition: 'He was acquitted _____ all criminal charges.' -> OF (Acquit of)",
                        "Subjunctive Mood: 'It is essential that she _____ present at the tribunal.' -> BE (Bare subjunctive, not 'is')",
                        "Gerund Governance: 'He is committed to _____ the rural electrification project.' -> EXPEDITING (to + V-ing)"
                    ]
                },
                {
                    "name": "2. Double-Blank Sentences with Polarity Signposts",
                    "desc": "Sentences requiring two words whose semantic relationship is defined by linking conjunctions.",
                    "examples": [
                        "Parallel/Agreement Connectors ('and', 'furthermore', 'moreover'): Both blanks must share identical positive or negative polarity.",
                        "Contrast/Reversal Connectors ('although', 'despite', 'yet', 'nevertheless'): Blank 1 and Blank 2 must exhibit contrasting or opposed polarities.",
                        "Cause & Effect Connectors ('because', 'therefore', 'consequently'): Blank 2 must logically result from the condition established in Blank 1."
                    ]
                },
                {
                    "name": "3. Natural English Collocations & Lexical Pairs",
                    "desc": "Testing combinations of words that naturally and conventionally co-occur in formal usage.",
                    "examples": [
                        "Verbs with Nouns: 'commit a crime' (not 'do a crime'), 'pay attention' (not 'give attention'), 'wreak havoc' (not 'make havoc')",
                        "Adverbs with Adjectives: 'diametrically opposed', 'blatantly obvious', 'bitterly disappointed', 'deeply concerned'",
                        "Adjectives with Nouns: 'grave concern', 'heavy rain', 'narrow escape', 'unmitigated disaster'"
                    ]
                },
                {
                    "name": "4. Cloze Test Paragraph Discourse Cohesion",
                    "desc": "Selecting words across a multi-sentence passage where choices depend on cross-sentence cohesion.",
                    "examples": [
                        "Tracking anaphoric reference pronouns ('this phenomenon', 'these considerations')",
                        "Maintaining consistency in tense throughout a narrative episode",
                        "Harmonizing semantic tone across an entire argumentative paragraph"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Syntactic Slot Diagnostic Rule",
                    "explanation": "Before reviewing the multiple-choice options, inspect the surrounding words to diagnose the required grammatical part of speech. If the blank is preceded by 'the' and followed by 'of', the blank must be a noun. If preceded by 'has been' and followed by 'by', it must be a past participle (V3) in the passive voice.",
                    "words": [
                        "Syntactic Diagnostic",
                        "Part of Speech",
                        "Grammatical Slot"
                    ],
                    "correct": "The government announced the [eradication] of extreme poverty (Noun).",
                    "incorrect": "The government announced the [eradicate] of extreme poverty (Verb in noun slot)."
                },
                {
                    "rule_number": 2,
                    "title": "Discourse Marker Polarity Calibration Rule",
                    "explanation": "Identify structural conjunctions. 'Although' signals that the two clauses will conflict in sentiment. If Clause 1 is positive (e.g. 'Although he was highly qualified...'), Clause 2 must express a limitation or negative outcome ('...he was [rejected] for the post').",
                    "words": [
                        "Discourse Markers",
                        "Polarity",
                        "Although / Despite"
                    ],
                    "correct": "Although the budget was meager, the team achieved [spectacular] success.",
                    "incorrect": "Although the budget was meager, the team achieved [poor] results (Lacks contrast)."
                },
                {
                    "rule_number": 3,
                    "title": "Fixed Preposition Verification Rule",
                    "explanation": "Always inspect the preposition immediately following the blank. If the sentence has '_____ in the enterprise', a verb like 'invest' fits ('invest in'), but 'participate' also fits ('participate in'), whereas 'refrain' requires 'from'. Eliminate any candidate word whose governing preposition clashes.",
                    "words": [
                        "Governing Preposition",
                        "Collocation",
                        "Prepositional Verb"
                    ],
                    "correct": "She resolved to abstain [from] intoxicating liquors.",
                    "incorrect": "She resolved to abstain [to / in] intoxicating liquors."
                },
                {
                    "rule_number": 4,
                    "title": "Simultaneous Option-Pair Validation for Double Blanks",
                    "explanation": "In double-blank questions, an option is only correct if BOTH words satisfy grammatical and contextual criteria. If Word 1 is brilliant but Word 2 fails prepositional agreement or logic, discard the entire option pair immediately.",
                    "words": [
                        "Double Blanks",
                        "Option Pair",
                        "Simultaneous Elimination"
                    ],
                    "correct": "The [austere] monk lived in complete [solitude].",
                    "incorrect": "The [austere] monk lived in complete [gregariousness] (Word 2 contradicts Word 1)."
                },
                {
                    "rule_number": 5,
                    "title": "Negative and Restrictive Adverb Awareness Rule",
                    "explanation": "Sentences containing covert negative adverbs ('hardly', 'scarcely', 'barely', 'seldom', 'rarely') already express negation. Do not insert a negative word into the blank, which would produce an ungrammatical double negative.",
                    "words": [
                        "Double Negative",
                        "Hardly / Scarcely",
                        "Restrictive Adverbs"
                    ],
                    "correct": "He had scarcely any money left to buy food.",
                    "incorrect": "He had scarcely no money left to buy food."
                },
                {
                    "rule_number": 6,
                    "title": "Natural Collocation Superiority Rule",
                    "explanation": "Between two dictionary synonyms that both fit grammatically, select the word that constitutes an established, high-frequency idiom or collocation in English prose: 'rancid butter' (not 'sour butter'); 'blatant lie' (not 'naked lie').",
                    "words": [
                        "Collocation Superiority",
                        "Rancid Butter",
                        "Established Pairing"
                    ],
                    "correct": "The witness committed blatant perjury before the jury.",
                    "incorrect": "The witness committed transparent perjury before the jury."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Selecting a word that fits the blank but clashes with the subsequent preposition.",
                    "correction": "Always read past the blank to see the following preposition before choosing your answer.",
                    "rationale": "'Adhered' requires 'to'; 'complied' requires 'with'; 'abided' requires 'by'; selecting without checking the preposition causes instant error."
                },
                {
                    "mistake": "Evaluating only the first word in double-blank questions.",
                    "correction": "Test both words in the sentence before locking your choice.",
                    "rationale": "Examiners purposefully put an ideal first word in Option A with an impossible second word."
                },
                {
                    "mistake": "Ignoring subtle contrast words like 'yet', 'though', 'nonetheless'.",
                    "correction": "Mark the contrast words; determine if the missing word needs to be positive or negative relative to the other clause.",
                    "rationale": "Contrast words dictate the exact emotional polarity of the missing word."
                },
                {
                    "mistake": "Confusing homophones when filling the blank.",
                    "correction": "Distinguish stationary (fixed) vs stationery (paper); principal (chief) vs principle (rule).",
                    "rationale": "Homophonic pairs are frequently deployed as distractors in single-blank questions."
                }
            ],
            "quick_revision_points": [
                "Always inspect the preposition following the blank (comply WITH, adhere TO, abstain FROM).",
                "In double blanks, both words MUST work together; eliminate the option if either word fails.",
                "Contrast connectors (although, however, yet, despite) require opposite polarities in clauses.",
                "Agreement connectors (and, moreover, furthermore) require matching polarities.",
                "Diagnose the syntactic part of speech before looking at the 4 options.",
                "Watch out for collocations: 'wreak havoc', 'cast a ballot', 'grave concern', 'unmitigated disaster'.",
                "Look out for covert negatives (hardly, scarcely, seldom) to avoid double negative traps.",
                "Beware of homophone traps: compliment/complement, stationary/stationery, principal/principle."
            ]
        },
        "practice_questions": [
            {
                "id": 2201,
                "topic_id": 22,
                "question_text": "Fill in the blank with the most appropriate word: 'All corporate entities operating within the jurisdiction are strictly obligated to comply __________ environmental safety regulations.'",
                "question_type": "fitb",
                "options": [
                    "with",
                    "to",
                    "by",
                    "for"
                ],
                "correct_answer": "with",
                "explanation": "The verb 'comply' takes the fixed preposition 'with' ('comply with rules/regulations'). Compare: 'adhere to', 'abide by'.",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2202,
                "topic_id": 22,
                "question_text": "Select the pair of words that best completes the sentence: 'Although the new manager was initially regarded as __________ and unapproachable, she soon proved to be remarkably __________ and receptive to employee feedback.'",
                "question_type": "mcq",
                "options": [
                    "austere \u2014 genial",
                    "affable \u2014 hostile",
                    "gregarious \u2014 outgoing",
                    "bellicose \u2014 aggressive"
                ],
                "correct_answer": "austere \u2014 genial",
                "explanation": "'Although' indicates a contrast. Blank 1 must mean strict/distant ('austere', matching 'unapproachable'), and Blank 2 must mean friendly/warm ('genial', matching 'receptive').",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2203,
                "topic_id": 22,
                "question_text": "Fill in the blank with the appropriate collocation: 'The unprecedented torrential rainfall caused the river to burst its banks and wreak __________ across the low-lying agricultural districts.'",
                "question_type": "fitb",
                "options": [
                    "havoc",
                    "damage",
                    "destruction",
                    "trouble"
                ],
                "correct_answer": "havoc",
                "explanation": "The standard English collocation is 'to wreak havoc' (meaning to cause widespread chaos, destruction, or turmoil).",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2204,
                "topic_id": 22,
                "question_text": "Select the appropriate word: 'The members of the audit committee decided to abstain __________ voting until supplementary documentation was furnished.'",
                "question_type": "mcq",
                "options": [
                    "from",
                    "to",
                    "against",
                    "in"
                ],
                "correct_answer": "from",
                "explanation": "The verb 'abstain' governs the preposition 'from' ('abstain from voting / alcohol').",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2205,
                "topic_id": 22,
                "question_text": "Choose the correct words to fill both blanks: 'The scientific community expressed __________ concern over the __________ depletion of Arctic permafrost.'",
                "question_type": "mcq",
                "options": [
                    "grave \u2014 rapid",
                    "trivial \u2014 hasty",
                    "minute \u2014 extensive",
                    "fleeting \u2014 persistent"
                ],
                "correct_answer": "grave \u2014 rapid",
                "explanation": "'Grave concern' is an established formal collocation expressing serious worry, and 'rapid depletion' logically describes the accelerating loss of permafrost.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2206,
                "topic_id": 22,
                "question_text": "Fill in the blank: 'Because the evidence presented by the prosecution was entirely __________, the magistrate dismissed the indictment without hesitation.'",
                "question_type": "mcq",
                "options": [
                    "inconclusive",
                    "compelling",
                    "irrefutable",
                    "substantive"
                ],
                "correct_answer": "inconclusive",
                "explanation": "The cause-and-effect connector 'Because' followed by 'dismissed the indictment' requires an adjective indicating defective or insufficient evidence ('inconclusive').",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2207,
                "topic_id": 22,
                "question_text": "Select the correct option to fill the blank: 'The new regional transport office has remained __________ at the same address for over twenty-five years.'",
                "question_type": "mcq",
                "options": [
                    "stationary",
                    "stationery",
                    "stationing",
                    "stationer"
                ],
                "correct_answer": "stationary",
                "explanation": "'Stationary' (with 'a') means not moving, staying in one place. 'Stationery' (with 'e') refers to writing materials (pens, paper, envelopes).",
                "difficulty": "easy",
                "points": 1
            },
            {
                "id": 2208,
                "topic_id": 22,
                "question_text": "Fill in the blank: 'She had __________ stepped outside when the thunderous deluge commenced, leaving her thoroughly soaked.'",
                "question_type": "fitb",
                "options": [
                    "scarcely",
                    "already",
                    "nearly",
                    "definitely"
                ],
                "correct_answer": "scarcely",
                "explanation": "Correlative conjunction rule: 'Scarcely / Hardly... when' is the required correlative structure.",
                "difficulty": "medium",
                "points": 1
            },
            {
                "id": 2209,
                "topic_id": 22,
                "question_text": "Choose the pair that completes the sentence logically: 'Far from being __________, the diplomat's remarks were deliberately calculated to be __________ and provocative.'",
                "question_type": "mcq",
                "options": [
                    "conciliatory \u2014 inflammatory",
                    "belligerent \u2014 hostile",
                    "moderate \u2014 peaceful",
                    "evasive \u2014 candid"
                ],
                "correct_answer": "conciliatory \u2014 inflammatory",
                "explanation": "'Far from being [X]' signals an antithesis with the subsequent description ('provocative'). 'Conciliatory' (peace-seeking) contrasts with 'inflammatory' (stirring up anger/provocative).",
                "difficulty": "hard",
                "points": 1
            },
            {
                "id": 2210,
                "topic_id": 22,
                "question_text": "Fill in the blank with the correct collocation: 'The defense attorney requested a brief recess to __________ consultation with his client.'",
                "question_type": "mcq",
                "options": [
                    "hold",
                    "do",
                    "make",
                    "create"
                ],
                "correct_answer": "hold",
                "explanation": "In formal legal and administrative English, one 'holds consultations' or 'enters into consultation', not 'does' or 'creates' consultation.",
                "difficulty": "medium",
                "points": 1
            }
        ]
    }
}
