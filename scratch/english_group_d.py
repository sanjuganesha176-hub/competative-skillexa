# English Group D: Topics 12, 13, 14, 15
# 12: Active and Passive Voice, 13: Direct and Indirect Speech, 14: Sentence Correction, 15: Error Detection

GROUP_D_DATA = {
    12: {
        "title": "Active and Passive Voice: Transformation Matrix, Modal Passives & Imperatives",
        "source_id": 1,
        "content": {
            "definition": "Voice is the grammatical category that denotes whether the grammatical subject of a clause performs the action (Active Voice) or is the recipient of the action (Passive Voice). In competitive examinations (SSC CGL Tier-2, CDS), voice transformation questions test passive constructions across all tenses, ditransitive verbs with dual objects, imperative commands, and verbs that take prepositions other than 'by'.",
            "overview": "Passive voice is formulated using the auxiliary verb 'be' in the appropriate tense followed by the Past Participle (V3) of the main verb: Object -> Subject + Be-form + V3 + by + Original Subject. Note that four tenses do NOT admit standard passive conversions: Present Perfect Continuous, Past Perfect Continuous, Future Continuous, and Future Perfect Continuous.",
            "types": [
                {
                    "name": "1. Standard Tense Transformation Matrix",
                    "desc": "Conversions across the 8 tenses that permit passive voice.",
                    "examples": [
                        "Simple Present: is/am/are + V3 ('He writes a report' -> 'A report is written by him')",
                        "Present Continuous: is/am/are + being + V3 ('She is drafting a letter' -> 'A letter is being drafted by her')",
                        "Present Perfect: has/have + been + V3 ('They have sealed the border' -> 'The border has been sealed by them')",
                        "Simple Past: was/were + V3 ('The police arrested the thief' -> 'The thief was arrested by the police')",
                        "Past Continuous: was/were + being + V3 ('He was driving the car' -> 'The car was being driven by him')",
                        "Past Perfect: had + been + V3 ('They had signed the treaty' -> 'The treaty had been signed by them')",
                        "Simple Future: will/shall + be + V3 ('She will conduct the audit' -> 'The audit will be conducted by her')",
                        "Future Perfect: will have + been + V3 ('He will have published the paper' -> 'The paper will have been published by him')"
                    ]
                },
                {
                    "name": "2. Imperative Sentence Transformations",
                    "desc": "Converting commands, requests, and advice into passive constructions.",
                    "examples": [
                        "Command/Order (Let + Object + be + V3): 'Shut the door' -> 'Let the door be shut'",
                        "Advice/Moral Duty (Object + should be + V3): 'Help the poor' -> 'The poor should be helped'",
                        "Request (You are requested to + V1): 'Please maintain silence' -> 'You are requested to maintain silence'"
                    ]
                },
                {
                    "name": "3. Verbs Taking Prepositions Other than 'By'",
                    "desc": "Certain stative and psychological verbs govern fixed prepositions in passive voice.",
                    "examples": [
                        "Known to (NOT by): 'I know him' -> 'He is known to me'",
                        "Surprised at: 'His behavior surprised everyone' -> 'Everyone was surprised at his behavior'",
                        "Pleased with: 'Her performance pleased the panel' -> 'The panel was pleased with her performance'",
                        "Filled with / Contained in: 'The jar contains milk' -> 'Milk is contained in the jar'"
                    ]
                },
                {
                    "name": "4. Ditransitive Verbs (Two Objects)",
                    "desc": "Verbs with both a Direct Object (thing) and an Indirect Object (person).",
                    "examples": [
                        "Active: 'The governor gave the soldier a medal'",
                        "Passive Option 1 (Personal/Indirect Object as Subject): 'The soldier was given a medal by the governor' (Preferred)",
                        "Passive Option 2 (Direct Object as Subject): 'A medal was given to the soldier by the governor'"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Formula for Passive Voice: Auxiliary 'Be' + V3",
                    "explanation": "Every passive sentence MUST contain a conjugated form of the auxiliary verb 'be' (is, am, are, was, were, be, being, been) paired with the past participle (V3) of the principal transitive verb.",
                    "words": ["Be + V3", "Auxiliary Be", "Past Participle"],
                    "correct": "The new constitutional amendment was passed by the parliament.",
                    "incorrect": "The new constitutional amendment was pass by the parliament."
                },
                {
                    "rule_number": 2,
                    "title": "'Known' Takes 'To', Never 'By'",
                    "explanation": "In passive transformations of the verb 'know', the agent is linked with the preposition 'to', NEVER 'by'. Similarly, 'surprised', 'shocked', and 'astonished' take 'at'.",
                    "words": ["Known to", "Surprised at", "Fixed Passive Preposition"],
                    "correct": "His integrity and selfless devotion to duty are known to all.",
                    "incorrect": "His integrity and selfless devotion to duty are known by all."
                },
                {
                    "rule_number": 3,
                    "title": "Imperative Voice with 'Let + Object + Be + V3'",
                    "explanation": "Direct orders in the imperative mood are passivized using the structure: 'Let + Object + be + V3'. If expressing moral advice, use 'Object + should be + V3'.",
                    "words": ["Let", "Imperative Passive", "Should be"],
                    "correct": "Let the emergency alert be transmitted immediately.",
                    "incorrect": "Let the emergency alert transmitted immediately."
                },
                {
                    "rule_number": 4,
                    "title": "Modal Auxiliary Passive: 'Modal + Be + V3'",
                    "explanation": "When transforming active sentences with modal verbs (can, could, may, might, shall, should, will, would, must, ought to), the passive structure is 'Modal + be + V3'.",
                    "words": ["Modal + be + V3", "Modal Passive", "Auxiliary"],
                    "correct": "This urgent diplomatic crisis must be resolved peacefully.",
                    "incorrect": "This urgent diplomatic crisis must resolved peacefully."
                },
                {
                    "rule_number": 5,
                    "title": "Omission of Vague Agents (By someone / By people)",
                    "explanation": "In natural passive voice, vague, redundant, or universal agents (by people, by someone, by them, by police) are omitted unless the specific identity of the agent adds vital information.",
                    "words": ["Agent Omission", "Redundant Agent", "Passive Style"],
                    "correct": "The stolen treasury bonds have been recovered.",
                    "incorrect": "The stolen treasury bonds have been recovered by somebody."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Saying 'He is known by me'",
                    "correction": "Use 'to': 'He is known to me.'",
                    "rationale": "The stative verb 'know' requires the preposition 'to' in passive voice."
                },
                {
                    "mistake": "Attempting to passivize intransitive verbs ('He was arrived on time')",
                    "correction": "Keep in active voice: 'He arrived on time.'",
                    "rationale": "Intransitive verbs have no direct object to become the grammatical subject in a passive construction."
                },
                {
                    "mistake": "Forgetting 'being' in continuous passive ('The bridge is constructed now')",
                    "correction": "Include 'being': 'The bridge is being constructed now.'",
                    "rationale": "Present continuous passive strictly requires 'is/are + being + V3'."
                },
                {
                    "mistake": "Changing the tense of the sentence during active-passive transformation",
                    "correction": "Preserve the original tense precisely in the passive voice.",
                    "rationale": "Voice transformation changes grammatical perspective, NOT the temporal tense of the action."
                }
            ],
            "quick_revision_points": [
                "Passive formula: Object + form of 'Be' + V3 (Past Participle) + by + Subject.",
                "Continuous tenses use 'being': is/are/was/were + being + V3.",
                "Perfect tenses use 'been': has/have/had + been + V3.",
                "Modal passive: Modal + be + V3 (e.g., 'must be done', 'can be solved').",
                "Imperative passive: 'Let + object + be + V3' (e.g., 'Let it be done').",
                "Fixed prepositions in passive: known to, pleased with, surprised at, contained in.",
                "Tenses that CANNOT be passivized: all three perfect continuous tenses + future continuous."
            ]
        },
        "practice": [
            {
                "question": "Transform the following active sentence into the correct passive voice:\n'The executive committee has approved the revised municipal budget.'",
                "options_json": [
                    "The revised municipal budget has been approved by the executive committee.",
                    "The revised municipal budget had been approved by the executive committee.",
                    "The revised municipal budget was approved by the executive committee.",
                    "The revised municipal budget is approved by the executive committee."
                ],
                "correct_answer": "The revised municipal budget has been approved by the executive committee.",
                "explanation": "Present perfect active ('has approved') transforms into present perfect passive ('has been approved').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Convert into passive voice: 'Everyone knows Dr. Kalam.'",
                "options_json": [
                    "Dr. Kalam is known to everyone.",
                    "Dr. Kalam is known by everyone.",
                    "Dr. Kalam was known to everyone.",
                    "Dr. Kalam has been known with everyone."
                ],
                "correct_answer": "Dr. Kalam is known to everyone.",
                "explanation": "In the passive voice, the verb 'know' takes the fixed preposition 'to', never 'by'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the correct passive transformation of the imperative sentence: 'Do not disclose this confidential information.'",
                "options_json": [
                    "Let this confidential information not be disclosed.",
                    "Let not this confidential information disclose.",
                    "You are told to not disclose.",
                    "This confidential information cannot be disclosed."
                ],
                "correct_answer": "Let this confidential information not be disclosed.",
                "explanation": "Negative imperatives are passivized using: 'Let + Object + not + be + V3'.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Transform into passive: 'The military engineers were constructing the pontoon bridge across the river.'",
                "options_json": [
                    "The pontoon bridge was being constructed across the river by the military engineers.",
                    "The pontoon bridge was constructed across the river by the military engineers.",
                    "The pontoon bridge had been constructed by the military engineers.",
                    "The pontoon bridge is being constructed across the river."
                ],
                "correct_answer": "The pontoon bridge was being constructed across the river by the military engineers.",
                "explanation": "Past continuous active ('were constructing') transforms to past continuous passive ('was being constructed').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why can the sentence 'The express train arrived at the junction at midnight' NOT be transformed into passive voice?",
                "options_json": [
                    "'Arrived' is an intransitive verb and takes no direct object to become the passive subject.",
                    "The sentence contains a time phrase.",
                    "'Junction' is a masculine noun.",
                    "Past tense sentences cannot be made passive."
                ],
                "correct_answer": "'Arrived' is an intransitive verb and takes no direct object to become the passive subject.",
                "explanation": "Intransitive verbs cannot form passive voice because there is no direct object to receive the action.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Convert into passive: 'The sudden announcement surprised the entire delegation.'",
                "options_json": [
                    "The entire delegation was surprised at the sudden announcement.",
                    "The entire delegation was surprised by the sudden announcement.",
                    "The entire delegation is surprised at the announcement.",
                    "The entire delegation had been surprised by the announcement."
                ],
                "correct_answer": "The entire delegation was surprised at the sudden announcement.",
                "explanation": "The passive form of 'surprise' takes the preposition 'at' when reacting to an event or announcement.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct passive voice for the modal sentence: 'We must preserve historical monuments.'",
                "options_json": [
                    "Historical monuments must be preserved.",
                    "Historical monuments must preserved by us.",
                    "Historical monuments should been preserved.",
                    "Historical monuments ought to preserved."
                ],
                "correct_answer": "Historical monuments must be preserved.",
                "explanation": "Modal passive: 'must + be + V3' ('must be preserved'). The general agent 'by us' is properly omitted.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Transform into passive: 'Who wrote this monumental literary classic?'",
                "options_json": [
                    "By whom was this monumental literary classic written?",
                    "By who was this monumental literary classic written?",
                    "Whom wrote this monumental literary classic?",
                    "Who was this monumental literary classic written?"
                ],
                "correct_answer": "By whom was this monumental literary classic written?",
                "explanation": "'Who' transforms into the objective prepositional phrase 'By whom' at the start of interrogative passive clauses.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "In the passive voice, the verb 'know' takes the fixed preposition '______' instead of 'by'.",
                "correct_answer": "to",
                "explanation": "Known to someone.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The continuous passive voice requires the auxiliary participle '______' (e.g., 'is ______ prepared').",
                "correct_answer": "being",
                "explanation": "Continuous passive uses 'being' + V3.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    13: {
        "title": "Direct and Indirect Speech: Narration Back-Shift, Pronoun Shifts & Sentence Conversions",
        "source_id": 1,
        "content": {
            "definition": "Narration (Direct and Indirect Speech) describes the linguistic process of reporting the words of a speaker either verbatim within quotation marks (Direct Speech) or reported in the narrator's own syntactic framework without quotation marks (Indirect/Reported Speech). In competitive exams (SSC CGL Tier-1 & Tier-2, Bank PO), narration questions evaluate Tense Back-Shift rules, personal pronoun conversions based on SON rules, changes in adverbs of time and place, and reporting across Assertive, Interrogative, Imperative, Optative, and Exclamatory sentences.",
            "overview": "When the reporting verb is in the Past Tense (said, told, remarked), the verb in the reported speech undergoes a systematic Tense Back-Shift (Simple Present -> Simple Past; Simple Past -> Past Perfect; Present Perfect -> Past Perfect). Modals shift accordingly (can -> could; may -> might; will/shall -> would).",
            "types": [
                {
                    "name": "1. The SON Pronoun Shift Formula",
                    "desc": "The universal mnemonic governing personal pronoun transformations in reported speech.",
                    "examples": [
                        "S (First Person pronouns: I, we, my, our) -> changes according to the SUBJECT of the reporting verb",
                        "O (Second Person pronouns: you, your) -> changes according to the OBJECT of the reporting verb",
                        "N (Third Person pronouns: he, she, it, they, his, their) -> NO CHANGE (remains in third person)"
                    ]
                },
                {
                    "name": "2. Systematic Tense Back-Shift Matrix",
                    "desc": "How verb tenses shift when the reporting verb is in the past tense.",
                    "examples": [
                        "Simple Present (V1) -> Simple Past (V2) ('I work' -> he worked)",
                        "Present Continuous (is/am/are + V-ing) -> Past Continuous (was/were + V-ing)",
                        "Present Perfect (has/have + V3) -> Past Perfect (had + V3)",
                        "Simple Past (V2) -> Past Perfect (had + V3) ('I saw him' -> he had seen him)",
                        "Past Continuous (was/were + V-ing) -> Past Perfect Continuous (had been + V-ing)",
                        "Past Perfect & Past Perfect Continuous -> NO TENSE CHANGE"
                    ]
                },
                {
                    "name": "3. Adverbial Shifts of Time & Distance",
                    "desc": "Words expressing geographical or temporal proximity convert to distant equivalents.",
                    "examples": [
                        "Now -> then; Here -> there; This -> that; These -> those",
                        "Today -> that day; Tonight -> that night; Yesterday -> the previous day / the day before",
                        "Tomorrow -> the next day / the following day; Ago -> before; Last night -> the previous night"
                    ]
                },
                {
                    "name": "4. Interrogative, Imperative & Exclamatory Conversions",
                    "desc": "Handling distinct sentence moods in indirect speech.",
                    "examples": [
                        "Yes/No Questions: Use 'if' or 'whether' with assertive word order (Subject + Verb, NO question mark): He asked me if I was ready",
                        "WH-Questions: Retain the WH-word (who, where, why) with assertive word order: He asked where I lived",
                        "Imperative Sentences: Convert main verb to to-infinitive (to + V1), change reporting verb to ordered, requested, advised, warned",
                        "Exclamatory Sentences: Use 'exclaimed with joy/sorrow/surprise' and convert to assertive structure"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "No Tense Change if Reporting Verb is Present or Future",
                    "explanation": "If the reporting verb is in the Present Tense (says, tells) or Future Tense (will say), the tense of the reported speech DOES NOT CHANGE at all. Only pronoun shifts occur.",
                    "words": ["Present Reporting Verb", "Future Reporting Verb", "No Tense Change"],
                    "correct": "He says, 'I am ready' -> He says that he is ready.",
                    "incorrect": "He says, 'I am ready' -> He says that he was ready."
                },
                {
                    "rule_number": 2,
                    "title": "Assertive Word Order in Reported Questions (No Inversion)",
                    "explanation": "When transforming direct questions into indirect speech, the interrogative inversion (Auxiliary + Subject) MUST convert to normal assertive word order (Subject + Verb). The question mark is omitted.",
                    "words": ["Assertive Order", "No Inversion", "Omission of Question Mark"],
                    "correct": "She asked me where I lived.",
                    "incorrect": "She asked me where did I live."
                },
                {
                    "rule_number": 3,
                    "title": "Universal Truths Exempt from Tense Back-Shift",
                    "explanation": "Even if the reporting verb is in the past tense, universal scientific truths, historical facts, and habitual routines in reported speech REMAIN in the Simple Present.",
                    "words": ["Universal Truth", "Historical Fact", "No Back-Shift"],
                    "correct": "The professor said, 'Water freezes at zero degrees Celsius' -> The professor said that water freezes at zero degrees Celsius.",
                    "incorrect": "The professor said that water froze at zero degrees Celsius."
                },
                {
                    "rule_number": 4,
                    "title": "Imperative Negative: 'Not to + V1' (or 'Forbade + to + V1')",
                    "explanation": "Negative imperatives ('Do not touch the wire') become 'ordered/warned... not to touch the wire'. If the reporting verb 'forbade' is used, NEVER include 'not' because 'forbade' is already negative.",
                    "words": ["Forbade", "Not to", "Imperative Reporting"],
                    "correct": "The sentry forbade the intruder to cross the boundary.",
                    "incorrect": "The sentry forbade the intruder not to cross the boundary."
                },
                {
                    "rule_number": 5,
                    "title": "'Told' Requires an Indirect Object; 'Said' Does Not",
                    "explanation": "The transitive reporting verb 'told' MUST be followed directly by a personal object without 'to' (told me, told him). 'Said' can stand alone or take 'to + object' ('said to me'). Saying 'He told to me' is an error.",
                    "words": ["Told", "Said to", "Indirect Object"],
                    "correct": "The detective told the suspect that the evidence was conclusive.",
                    "incorrect": "The detective told to the suspect that the evidence was conclusive."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using interrogative word order in indirect questions ('He asked me what was my name')",
                    "correction": "Use assertive order: 'He asked me what my name was.'",
                    "rationale": "Indirect questions are declarative noun clauses and must follow Subject + Verb order."
                },
                {
                    "mistake": "Saying 'He told to me that he was tired'",
                    "correction": "Say 'He told me that he was tired' or 'He said to me that he was tired.'",
                    "rationale": "'Told' is a transitive verb that directly takes the personal object without 'to'."
                },
                {
                    "mistake": "Adding 'not' after 'forbade' ('The officer forbade him not to enter')",
                    "correction": "Omit 'not': 'The officer forbade him to enter.'",
                    "rationale": "'Forbade' has an intrinsic negative meaning; adding 'not' creates a double negative."
                },
                {
                    "mistake": "Using 'that' with 'if/whether' ('He asked that if I was coming')",
                    "correction": "Omit 'that': 'He asked if I was coming.'",
                    "rationale": "'If' or 'whether' already serves as the subordinating conjunction; combining it with 'that' is redundant."
                }
            ],
            "quick_revision_points": [
                "SON formula: 1st person changes with Subject; 2nd with Object; 3rd does Not change.",
                "Tense back-shift: Present -> Past; Simple Past -> Past Perfect; Present Perfect -> Past Perfect.",
                "No tense change if reporting verb is in Present (says) or Future (will say).",
                "Universal truths and scientific facts never undergo tense back-shift.",
                "Indirect questions use assertive order (Subject + Verb) without question marks.",
                "'Told' takes a direct object without 'to'; 'Forbade' takes 'to + V1' without 'not'.",
                "Time shifts: today -> that day, tomorrow -> the next day, yesterday -> the previous day."
            ]
        },
        "practice": [
            {
                "question": "Transform the following direct speech into correct indirect narration:\n'The judge said to the witness, \"Do you recognize the accused person in this courtroom?\"'",
                "options_json": [
                    "The judge asked the witness if he recognized the accused person in that courtroom.",
                    "The judge asked to the witness whether did he recognize the accused person.",
                    "The judge asked the witness that if he recognized the accused person.",
                    "The judge asked the witness whether he recognizes the accused person."
                ],
                "correct_answer": "The judge asked the witness if he recognized the accused person in that courtroom.",
                "explanation": "Interrogative question transforms with 'if', assertive order ('he recognized'), and proximity shift ('this' -> 'that').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Convert into indirect speech: 'The scientist said, \"The Earth rotates on its geographical axis from west to east.\"'",
                "options_json": [
                    "The scientist said that the Earth rotates on its geographical axis from west to east.",
                    "The scientist said that the Earth rotated on its geographical axis from west to east.",
                    "The scientist said that the Earth had rotated on its axis.",
                    "The scientist told that the Earth rotates on its axis."
                ],
                "correct_answer": "The scientist said that the Earth rotates on its geographical axis from west to east.",
                "explanation": "Universal scientific facts remain in the Simple Present tense regardless of a past reporting verb.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the grammatically correct indirect transformation of the negative command:\n'The commanding officer said to the soldiers, \"Do not fire until I give the command.\"'",
                "options_json": [
                    "The commanding officer ordered the soldiers not to fire until he gave the command.",
                    "The commanding officer ordered the soldiers to not fire until he gives the command.",
                    "The commanding officer forbade the soldiers not to fire until he gave the command.",
                    "The commanding officer told that the soldiers do not fire."
                ],
                "correct_answer": "The commanding officer ordered the soldiers not to fire until he gave the command.",
                "explanation": "Imperatives convert using 'ordered... not to fire', and the present 'give' back-shifts to past 'gave'.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error in the following indirect sentence:\n'The tourist asked the police constable where was the nearest foreign exchange bureau.'",
                "options_json": [
                    "'where was the nearest' should be 'where the nearest foreign exchange bureau was'",
                    "'The tourist asked' should be 'The tourist told'",
                    "'nearest' should be 'nearer'",
                    "There is no error in the sentence"
                ],
                "correct_answer": "'where was the nearest' should be 'where the nearest foreign exchange bureau was'",
                "explanation": "Indirect questions require assertive word order (Subject + Verb), meaning the verb 'was' must come at the end after the subject.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct indirect conversion: 'He says, \"I am preparing for the civil services examination.\"'",
                "options_json": [
                    "He says that he is preparing for the civil services examination.",
                    "He says that he was preparing for the civil services examination.",
                    "He said that he is preparing for the civil services examination.",
                    "He says that I am preparing for the civil services examination."
                ],
                "correct_answer": "He says that he is preparing for the civil services examination.",
                "explanation": "Because the reporting verb 'says' is in the Present Tense, the tense in the reported clause does not change.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'The general forbade the troops not to surrender' considered an error?",
                "options_json": [
                    "'Forbade' is already negative and cannot be paired with 'not', creating an ungrammatical double negative.",
                    "'Forbade' must be followed by a gerund.",
                    "'Troops' cannot take an infinitive.",
                    "The sentence is completely correct."
                ],
                "correct_answer": "'Forbade' is already negative and cannot be paired with 'not', creating an ungrammatical double negative.",
                "explanation": "'Forbade' means ordered not to; adding 'not' inverts the meaning.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "In indirect speech, the time adverbial 'yesterday' correctly transforms into:",
                "options_json": ["the previous day / the day before", "the next day", "that day", "tomorrow"],
                "correct_answer": "the previous day / the day before",
                "explanation": "'Yesterday' converts to 'the previous day' or 'the day before'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "What happens to the Simple Past tense (V2) in reported speech when the reporting verb is in the past?",
                "options_json": [
                    "It shifts to the Past Perfect tense (had + V3)",
                    "It remains in the Simple Past tense",
                    "It shifts to the Present Perfect tense",
                    "It shifts to the Future in the Past (would + V1)"
                ],
                "correct_answer": "It shifts to the Past Perfect tense (had + V3)",
                "explanation": "Simple Past (V2) back-shifts to Past Perfect (had + V3).",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The universal mnemonic for personal pronoun shifts in narration is the ______ formula.",
                "correct_answer": "SON",
                "explanation": "SON stands for Subject (1st person), Object (2nd person), No change (3rd person).",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "When converting an imperative sentence into indirect speech, the main verb is placed in the ______-infinitive form.",
                "correct_answer": "to",
                "explanation": "To-infinitive (e.g., 'ordered him to go').",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    14: {
        "title": "Sentence Correction: Parallelism, Dangling Modifiers, Redundancy & Tone",
        "source_id": 1,
        "content": {
            "definition": "Sentence Correction is an integrated verbal aptitude discipline where candidates evaluate complex sentences to detect and rectify structural, grammatical, rhetorical, and idiomatic errors, ensuring syntactical precision, grammatical parallelism, logical clarity, and conciseness. In competitive exams (SSC CGL, Bank PO, UPSC CDS), sentence correction questions test Dangling Modifiers, Parallel Construction, Pleonasms/Redundancies, and Pronoun Reference clarity.",
            "overview": "Effective sentence correction requires a disciplined analytical method: checking the grammatical skeleton (Subject-Verb agreement), validating modifier attachment (avoiding dangling participles), ensuring parallel syntactic structures, stripping away redundant phrasing (e.g., 'return back', 'revert back'), and ensuring correct idiomatic usage.",
            "types": [
                {
                    "name": "1. Dangling & Misplaced Modifiers",
                    "desc": "A modifier must logically attach to the noun it immediately precedes or follows.",
                    "examples": [
                        "Dangling Participle: 'Walking through the forest, the snake bit him' (implies the snake was walking)",
                        "Correction: 'While he was walking through the forest, a snake bit him'",
                        "Misplaced Modifier: 'The vendor sold a bicycle to the boy with defective brakes' -> 'The vendor sold a bicycle with defective brakes to the boy'"
                    ]
                },
                {
                    "name": "2. Faulty Parallelism in Series & Comparisons",
                    "desc": "Items in a list or balanced comparison must share identical grammatical structures.",
                    "examples": [
                        "Faulty: 'He likes swimming, to jog, and reading' (mixes gerunds with infinitives)",
                        "Parallel: 'He likes swimming, jogging, and reading'",
                        "Faulty: 'The climate of New Delhi is hotter than Mumbai' (compares climate with a city)",
                        "Parallel: 'The climate of New Delhi is hotter than that of Mumbai'"
                    ]
                },
                {
                    "name": "3. Redundancy & Pleonasms (Superfluous Expressions)",
                    "desc": "Unnecessary repetition of words conveying identical semantic content.",
                    "examples": [
                        "Incorrect: 'Return back' -> Correct: 'Return'",
                        "Incorrect: 'Revert back' -> Correct: 'Revert'",
                        "Incorrect: 'Reiterate again' -> Correct: 'Reiterate'",
                        "Incorrect: 'Consensus of opinion' -> Correct: 'Consensus'",
                        "Incorrect: 'Sufficient enough' -> Correct: 'Sufficient' or 'Enough'",
                        "Incorrect: 'Supposing if' -> Correct: 'Supposing' or 'If'"
                    ]
                },
                {
                    "name": "4. Ambiguous & Faulty Pronoun Reference",
                    "desc": "Pronouns that lack a clear, singular antecedent.",
                    "examples": [
                        "Ambiguous: 'The doctor met the patient and told him that his surgery was delayed' (Whose surgery?)",
                        "Clear: 'Meeting the patient, the doctor explained that the scheduled surgery was delayed'"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Logical Subject for Participial Modifiers",
                    "explanation": "An introductory participial phrase (e.g., 'Being a rainy day...', 'Having completed the investigation...') MUST be logically performed by the grammatical subject that follows the comma. If the subject cannot perform the action, supply an explicit subject for the participle.",
                    "words": ["Dangling Participle", "Introductory Modifier", "Logical Subject"],
                    "correct": "It being a rainy day, we decided to postpone the botanical expedition.",
                    "incorrect": "Being a rainy day, we decided to postpone the botanical expedition."
                },
                {
                    "rule_number": 2,
                    "title": "Comparative Symmetry: 'That of' / 'Those of'",
                    "explanation": "When comparing attributes of two entities, you must compare attribute with attribute, not attribute with entity. Use 'that of' for singular nouns and 'those of' for plural nouns.",
                    "words": ["Comparative Symmetry", "That of", "Those of", "Logical Comparison"],
                    "correct": "The streets of Tokyo are cleaner and wider than those of London.",
                    "incorrect": "The streets of Tokyo are cleaner and wider than London."
                },
                {
                    "rule_number": 3,
                    "title": "Elimination of Redundant Words with 'Re-' Verbs",
                    "explanation": "Verbs containing the prefix 're-' (meaning back or again)—such as return, revert, recall, repeat, reiterate, refund—must NEVER be paired with 'back' or 'again'.",
                    "words": ["Redundancy", "Return", "Revert", "Pleonasm"],
                    "correct": "The company will refund the advance security deposit within thirty days.",
                    "incorrect": "The company will refund back the advance security deposit within thirty days."
                },
                {
                    "rule_number": 4,
                    "title": "Parallelism in Coordinated Structures",
                    "explanation": "Whenever items are coordinated by conjunctions (and, but, or) or correlative conjunctions (not only... but also), all elements must maintain identical parts of speech and grammatical form.",
                    "words": ["Parallelism", "Coordination", "Syntactic Balance"],
                    "correct": "The newly elected governor pledged to lower taxes, create jobs, and improve public education.",
                    "incorrect": "The newly elected governor pledged to lower taxes, creating jobs, and improvement of public education."
                },
                {
                    "rule_number": 5,
                    "title": "Prohibition of 'Supposing If'",
                    "explanation": "'Supposing' and 'if' have identical conditional meanings. Using 'supposing if' in the same clause is a redundant pleonasm. Use either 'supposing' or 'if', never both.",
                    "words": ["Supposing", "If", "Pleonasm", "Conditional"],
                    "correct": "Supposing he loses his passport abroad, what protocol should he follow?",
                    "incorrect": "Supposing if he loses his passport abroad, what protocol should he follow?"
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Saying 'The population of China is greater than India'",
                    "correction": "Say 'The population of China is greater than that of India.'",
                    "rationale": "Without 'that of', you are comparing a population with an entire geographical landmass."
                },
                {
                    "mistake": "Using 'Being a hot day, the cattle sought shade'",
                    "correction": "Use 'It being a hot day, the cattle sought shade.'",
                    "rationale": "Without 'it', 'cattle' becomes the grammatical subject of 'being a hot day', meaning the cattle were a hot day."
                },
                {
                    "mistake": "Writing 'Kindly revert back to me at the earliest'",
                    "correction": "Write 'Kindly revert to me at the earliest.'",
                    "rationale": "'Revert' already means reply back; adding 'back' is a pleonasm."
                },
                {
                    "mistake": "Writing 'He is both an intellectual and he is athletic'",
                    "correction": "Write 'He is both an intellectual and an athlete' or 'He is both intellectual and athletic.'",
                    "rationale": "Correlative conjunctions require balanced grammatical parts of speech."
                }
            ],
            "quick_revision_points": [
                "Introductory participles must match the subject after the comma ('It being a stormy night...').",
                "Comparisons of attributes require 'that of' (singular) or 'those of' (plural).",
                "Eliminate pleonasms: return (not return back), revert (not revert back), sufficient (not sufficient enough).",
                "Never combine 'supposing' with 'if'.",
                "Maintain strict parallel structure across series joined by 'and', 'or', and 'not only... but also'."
            ]
        },
        "practice": [
            {
                "question": "Identify the sentence that correctly resolves the dangling participle:\n'Entering the abandoned laboratory, the shattered glass cut his shoe.'",
                "options_json": [
                    "As he entered the abandoned laboratory, the shattered glass cut his shoe.",
                    "Entering the abandoned laboratory, his shoe was cut by shattered glass.",
                    "Entering the laboratory, the glass was cutting his shoe.",
                    "Being entered the laboratory, the shattered glass cut his shoe."
                ],
                "correct_answer": "As he entered the abandoned laboratory, the shattered glass cut his shoe.",
                "explanation": "In the original sentence, 'shattered glass' was the dangling subject of 'Entering'. Converting to a temporal clause ('As he entered') provides the logical agent.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the sentence with logically accurate comparative symmetry:",
                "options_json": [
                    "The defense expenditure of the United States is greater than that of any other nation.",
                    "The defense expenditure of the United States is greater than any other nation.",
                    "The defense expenditure of the United States is greater than those of other nations.",
                    "The defense expenditure of the United States is more great than other nations."
                ],
                "correct_answer": "The defense expenditure of the United States is greater than that of any other nation.",
                "explanation": "Comparing an expenditure with an expenditure requires the singular pronoun 'that of'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the redundant pleonasm in the following business memorandum:\n'Please kindly revert back to the human resources department with your signed contract.'",
                "options_json": [
                    "revert back",
                    "human resources department",
                    "signed contract",
                    "Please kindly"
                ],
                "correct_answer": "revert back",
                "explanation": "'Revert' already means reply/respond back; adding 'back' is a redundant error.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following sentences exhibits flawless grammatical parallelism?",
                "options_json": [
                    "The fitness instructor emphasized running regularly, eating wholesome meals, and sleeping eight hours nightly.",
                    "The fitness instructor emphasized running regularly, to eat wholesome meals, and sleep eight hours nightly.",
                    "The fitness instructor emphasized to run regularly, eating wholesome meals, and sleeping eight hours nightly.",
                    "The fitness instructor emphasized running regularly, eating wholesome meals, and that you should sleep."
                ],
                "correct_answer": "The fitness instructor emphasized running regularly, eating wholesome meals, and sleeping eight hours nightly.",
                "explanation": "All three items in the coordinated series are structured identically as gerundial phrases ('running...', 'eating...', 'sleeping...').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the sentence that corrects the pleonasm 'supposing if':",
                "options_json": [
                    "Supposing the trade embargo is lifted, domestic industries will expand rapidly.",
                    "Supposing if the trade embargo is lifted, domestic industries will expand rapidly.",
                    "Supposing that if the trade embargo is lifted, domestic industries will expand.",
                    "If supposing the trade embargo is lifted, domestic industries will expand."
                ],
                "correct_answer": "Supposing the trade embargo is lifted, domestic industries will expand rapidly.",
                "explanation": "Use either 'supposing' or 'if', never combine them into 'supposing if'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'The climate of Chennai is warmer than Bangalore' grammatically defective?",
                "options_json": [
                    "It compares the climate of one city directly with the geographical territory of another city.",
                    "Chennai must be spelled Madras.",
                    "'Warmer' should be 'more warm'.",
                    "'Bangalore' cannot be compared with other cities."
                ],
                "correct_answer": "It compares the climate of one city directly with the geographical territory of another city.",
                "explanation": "Logical comparison requires: 'The climate of Chennai is warmer than that of Bangalore.'",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the sentence that properly corrects the misplaced modifier:\n'The executive served dinner to the foreign dignitaries on paper plates.'",
                "options_json": [
                    "The executive served dinner on paper plates to the foreign dignitaries.",
                    "On paper plates the executive served dinner to the foreign dignitaries.",
                    "The executive on paper plates served dinner to the foreign dignitaries.",
                    "Serving on paper plates dinner to the foreign dignitaries was the executive."
                ],
                "correct_answer": "The executive served dinner on paper plates to the foreign dignitaries.",
                "explanation": "The modifier 'on paper plates' modifies 'dinner', not 'the foreign dignitaries'.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Select the sentence free of redundant language:",
                "options_json": [
                    "The committee reached a consensus regarding the new infrastructure roadmap.",
                    "The committee reached a consensus of opinion regarding the new infrastructure roadmap.",
                    "The committee reached a mutual consensus of opinion regarding the roadmap.",
                    "The committee unanimously reached a consensus of opinion."
                ],
                "correct_answer": "The committee reached a consensus regarding the new infrastructure roadmap.",
                "explanation": "'Consensus' inherently means general agreement of opinion; adding 'of opinion' or 'mutual' is redundant.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "When comparing plural attributes of two entities (such as roads or salaries), use the comparative phrase 'those ______'.",
                "correct_answer": "of",
                "explanation": "'Those of' is used for plural comparisons (e.g., 'the roads of Paris are wider than those of London').",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "Verbs with the prefix 're-' like return, revert, and recall must never be combined with the redundant word '______'.",
                "correct_answer": "back",
                "explanation": "Never say 'return back' or 'revert back'.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    15: {
        "title": "Error Detection: Systematic Diagnostic Protocol for Competitive Examinations",
        "source_id": 1,
        "content": {
            "definition": "Error Detection (Spotting the Error) is the master diagnostic exercise in competitive examinations where a complex sentence is partitioned into segments (A, B, C, D) and candidates must identify the segment containing a violation of standard English grammar, usage, idiom, or syntax. If the sentence is entirely correct, option (D) or (E) 'No Error' is selected.",
            "overview": "Success in error spotting requires an orderly, systematic 6-step diagnostic protocol rather than relying on intuition or 'sound'. The examiner systematically tests: 1) Subject-Verb Agreement, 2) Pronoun Reference & Case, 3) Verb Tense & Sequence, 4) Prepositional Collocations & Omissions, 5) Conjunction Pairings, and 6) Modifier Placement & Parallelism.",
            "types": [
                {
                    "name": "1. The 6-Step Systematic Diagnostic Protocol",
                    "desc": "The methodical sequence every candidate must follow when analyzing an error spotting item.",
                    "examples": [
                        "Step 1 - Isolate the Core Subject and Finite Verb: Check number (singular vs. plural) and discard parenthetical prepositional phrases (as well as, along with)",
                        "Step 2 - Verify Pronoun Concord & Case: Ensure pronouns agree with antecedents and check subjective vs. objective case after prepositions",
                        "Step 3 - Check Tense Consistency: Verify timeline markers (ago, since, by next year) and sequence of tenses across dependent clauses",
                        "Step 4 - Inspect Prepositions & Phrasal Collocations: Check fixed prepositions (congratulate on, superior to) and redundant additions (discuss about)",
                        "Step 5 - Inspect Conjunctions & Correlatives: Check pairings (hardly... when, no sooner... than, neither... nor, lest... should)",
                        "Step 6 - Check Modifiers & Parallelism: Check dangling participles, OSASCOMP order, and comparative balance (that of)"
                    ]
                },
                {
                    "name": "2. High-Frequency Trap: Plural Nouns with Singular Meaning",
                    "desc": "Nouns ending in '-s' that are singular in meaning and require a singular verb.",
                    "examples": [
                        "Academic Disciplines: Mathematics, Physics, Economics, Politics, Statistics (when meaning the subject)",
                        "Diseases: Measles, Mumps, Rickets",
                        "Games: Billiards, Darts, Chess",
                        "Example: 'Economics is a rigorous behavioral science' (NOT 'Economics are')"
                    ]
                },
                {
                    "name": "3. High-Frequency Trap: Singular Nouns with Plural Meaning",
                    "desc": "Nouns with no plural '-s' suffix that are always plural in function and take plural verbs.",
                    "examples": [
                        "Nouns: Cattle, clergy, gentry, poultry, folk, peasantry, people, police",
                        "Example: 'The cattle are grazing in the meadow' (NOT 'The cattle is', and NEVER 'cattles')"
                    ]
                },
                {
                    "name": "4. The 'No Error' Confidence Barrier",
                    "desc": "Statistical analysis of competitive exams indicates that approximately 15-20% of questions contain no error.",
                    "examples": [
                        "Rule: Never invent an imaginary error simply because a sentence appears formal, literary, or long",
                        "If the sentence passes all 6 diagnostic steps, confidently select 'No Error'"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "The Subject Isolation Technique",
                    "explanation": "When an error spotting sentence has a long intervening prepositional phrase between the subject and the verb, bracket and ignore the phrase to verify agreement with the genuine head noun.",
                    "words": ["Subject Isolation", "Parenthetical Phrase", "Head Noun"],
                    "correct": "The quality [of the imported organic fruits] was exceptional.",
                    "incorrect": "The quality [of the imported organic fruits] were exceptional."
                },
                {
                    "rule_number": 2,
                    "title": "Verifying Prepositional Idioms over Literal Meaning",
                    "explanation": "Examiners frequently replace standard fixed prepositions with literal translations (e.g., substituting 'congratulate for' instead of 'congratulate on', or 'die from cancer' instead of 'die of cancer').",
                    "words": ["Fixed Preposition", "Collocation", "Idiomatic Accuracy"],
                    "correct": "The patient died of malaria after contracting the parasite.",
                    "incorrect": "The patient died from malaria after contracting the parasite."
                },
                {
                    "rule_number": 3,
                    "title": "Checking Correlative Symmetry at the Margins",
                    "explanation": "Whenever you spot 'not only', 'either', or 'neither', immediately scan ahead to verify that the second half of the pair ('but also', 'or', 'nor') is present and that both halves precede identical parts of speech.",
                    "words": ["Correlative Scan", "Parallelism Check", "Pair Verification"],
                    "correct": "He was accused of not only perjury but also embezzlement.",
                    "incorrect": "He was not only accused of perjury but also embezzlement."
                },
                {
                    "rule_number": 4,
                    "title": "Adverbial vs. Adjectival Confusion after Copular Verbs",
                    "explanation": "Copular / linking verbs of sensation (feel, smell, taste, look, sound, seem, appear) are modified by ADJECTIVES, NOT adverbs of manner (e.g., 'The soup smells delicious', NOT 'deliciously').",
                    "words": ["Linking Verbs", "Copular Verbs", "Sensory Modifiers", "Adjectives"],
                    "correct": "The roses in the Mughal gardens smell sweet in the morning.",
                    "incorrect": "The roses in the Mughal gardens smell sweetly in the morning."
                },
                {
                    "rule_number": 5,
                    "title": "Superfluous Relative Pronoun 'Which' in Independent Clauses",
                    "explanation": "Do not insert 'and which' or 'and who' unless an earlier relative clause has already been established; coordinate conjunctions cannot link a relative clause with an independent main clause.",
                    "words": ["And which", "Superfluous Relative", "Clause Coordination"],
                    "correct": "He submitted a brilliant thesis, which was highly acclaimed by the committee.",
                    "incorrect": "He submitted a brilliant thesis, and which was highly acclaimed by the committee."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Relying on how a sentence 'sounds' to the ear rather than applying grammar rules",
                    "correction": "Apply the 6-step grammatical protocol systematically.",
                    "rationale": "Colloquial spoken English is filled with grammatical errors that sound natural but are penalized in competitive exams."
                },
                {
                    "mistake": "Failing to check the number of the subject when separated by prepositional phrases",
                    "correction": "Isolate the primary subject noun preceding the preposition.",
                    "rationale": "The object of a preposition can never function as the grammatical subject of a sentence."
                },
                {
                    "mistake": "Using 'sweetly' instead of 'sweet' after linking verbs ('The food tastes deliciously')",
                    "correction": "Use predicate adjectives: 'The food tastes delicious.'",
                    "rationale": "Sensory linking verbs require predicate adjectives, not adverbs of manner."
                },
                {
                    "mistake": "Assuming that long sentences must contain an error",
                    "correction": "Evaluate each clause objectively; select 'No Error' when all rules are satisfied.",
                    "rationale": "Competitive examination papers intentionally include flawless long sentences to test candidate confidence."
                }
            ],
            "quick_revision_points": [
                "6-Step Protocol: Subject-Verb, Pronoun, Tense, Prepositions, Conjunctions, Modifiers.",
                "Isolate the true subject by mentally removing intervening prepositional phrases.",
                "Linking verbs of sense (smell, taste, feel, look) take adjectives, not adverbs ('smells sweet').",
                "Nouns plural in form but singular in use: Mathematics, Physics, News, Politics, Innings.",
                "Nouns singular in form but plural in use: Cattle, Clergy, Gentry, Poultry, Police, People.",
                "Die OF a disease; Die FROM an external wound or overwork; Die FOR a noble cause.",
                "Approximately 15-20% of exam sentences are correct: do not hesitate to choose 'No Error'."
            ]
        },
        "practice": [
            {
                "question": "Identify the part of the sentence containing the grammatical error:\n(A) The introduction of digital welfare transfers / (B) and automated payment gateways / (C) have dramatically minimized financial leakage / (D) No Error",
                "options_json": [
                    "(A) The introduction of digital welfare transfers",
                    "(B) and automated payment gateways",
                    "(C) have dramatically minimized financial leakage",
                    "(D) No Error"
                ],
                "correct_answer": "(C) have dramatically minimized financial leakage",
                "explanation": "The head noun subject is singular: 'The introduction' (the subsequent phrases are prepositional modifiers). Therefore, the verb must be singular: 'has dramatically minimized'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) Neither the financial regulator / (B) nor the commercial bank executives / (C) was able to foresee the liquidity crisis / (D) No Error",
                "options_json": [
                    "(A) Neither the financial regulator",
                    "(B) nor the commercial bank executives",
                    "(C) was able to foresee the liquidity crisis",
                    "(D) No Error"
                ],
                "correct_answer": "(C) was able to foresee the liquidity crisis",
                "explanation": "According to the Law of Proximity with 'neither... nor', the verb agrees with the nearest subject 'commercial bank executives' (plural). Hence, it must be 'were able to foresee'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) The veteran botanist observed / (B) that the nocturnal jasmine blossoms / (C) smelled very sweetly in the humid air / (D) No Error",
                "options_json": [
                    "(A) The veteran botanist observed",
                    "(B) that the nocturnal jasmine blossoms",
                    "(C) smelled very sweetly in the humid air",
                    "(D) No Error"
                ],
                "correct_answer": "(C) smelled very sweetly in the humid air",
                "explanation": "'Smell' is a sensory linking verb that takes a predicate adjective ('sweet'), not an adverb of manner ('sweetly').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) Scarcely had the international delegates / (B) assembled inside the conference chamber / (C) than the fire alarm sounded / (D) No Error",
                "options_json": [
                    "(A) Scarcely had the international delegates",
                    "(B) assembled inside the conference chamber",
                    "(C) than the fire alarm sounded",
                    "(D) No Error"
                ],
                "correct_answer": "(C) than the fire alarm sounded",
                "explanation": "'Scarcely' and 'Hardly' must strictly pair with 'when', not 'than'. Part (C) should read: 'when the fire alarm sounded'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) One of the most renowned / (B) architectural monuments in northern India / (C) are undergoing extensive restoration / (D) No Error",
                "options_json": [
                    "(A) One of the most renowned",
                    "(B) architectural monuments in northern India",
                    "(C) are undergoing extensive restoration",
                    "(D) No Error"
                ],
                "correct_answer": "(C) are undergoing extensive restoration",
                "explanation": "The subject of the clause is the singular pronoun 'One', which demands the singular auxiliary verb 'is undergoing', not 'are undergoing'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) The economic research institute / (B) has collected valuable datas / (C) on rural employment trends / (D) No Error",
                "options_json": [
                    "(A) The economic research institute",
                    "(B) has collected valuable datas",
                    "(C) on rural employment trends",
                    "(D) No Error"
                ],
                "correct_answer": "(B) has collected valuable datas",
                "explanation": "'Data' is uncountable in modern formal English, and the plural form 'datas' is strictly non-existent.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) The courageous firefighter entered into the burning building / (B) to rescue the trapped children / (C) without hesitating for a moment / (D) No Error",
                "options_json": [
                    "(A) The courageous firefighter entered into the burning building",
                    "(B) to rescue the trapped children",
                    "(C) without hesitating for a moment",
                    "(D) No Error"
                ],
                "correct_answer": "(A) The courageous firefighter entered into the burning building",
                "explanation": "'Enter' when referring to a physical structure is transitive and takes a direct object without 'into'. Part (A) should be: 'entered the burning building'.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error:\n(A) Having lived in the coastal city / (B) for over two decades, / (C) the monsoon climate is completely familiar to him / (D) No Error",
                "options_json": [
                    "(A) Having lived in the coastal city",
                    "(B) for over two decades,",
                    "(C) the monsoon climate is completely familiar to him",
                    "(D) No Error"
                ],
                "correct_answer": "(C) the monsoon climate is completely familiar to him",
                "explanation": "Dangling participle! 'Having lived...' must modify a person. In (C), the subject is 'the monsoon climate', meaning the climate lived in the city. Correction: '...he is completely familiar with the monsoon climate'.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "When an individual dies as a result of an internal disease (such as cholera or cancer), use the preposition 'die ______'.",
                "correct_answer": "of",
                "explanation": "Die of a disease; die from an external injury/wound.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "Linking verbs of perception like smell, taste, feel, and look take ______ adjectives rather than adverbs of manner.",
                "correct_answer": "predicate",
                "explanation": "Predicate adjectives qualify the subject through linking verbs.",
                "difficulty": "Medium",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    }
}
