# English Group A: Topics 3, 4, 5
# 3: Verb, 4: Adjective, 5: Adverb

GROUP_A_DATA = {
    3: {
        "title": "Verbs: Finite, Non-Finite, Modals, Transitive & Subject-Verb Interactions",
        "source_id": 1,
        "content": {
            "definition": "A verb is an essential part of speech that expresses an action, occurrence, state of being, or condition of a subject. In competitive English grammar, verbs form the structural backbone of every clause, categorized into Finite (governed by tense, number, and person) and Non-Finite (infinitives, gerunds, and participles), as well as Transitive (requiring direct objects) and Intransitive verbs.",
            "overview": "Verbal accuracy is heavily tested through modal auxiliaries, causatives, subjunctive mood constructions, confusing verb pairs (lie vs. lay, rise vs. raise), and the critical distinction between gerunds (verb + ing acting as a noun) and present participles (verb + ing acting as an adjective or continuous tense).",
            "types": [
                {
                    "name": "1. Finite vs. Non-Finite Verbs",
                    "desc": "Finite verbs change form according to tense, number, and person; Non-finite verbs do not change form with tense or subject changes.",
                    "examples": [
                        "Finite: 'She speaks fluent French' vs. 'They speak fluent French' (verb changes with subject number)",
                        "Infinitive (to + base verb): 'He decided to resign' (acts as noun/complement)",
                        "Gerund (verb + ing as noun): 'Swimming develops lung capacity' (acts as subject/object)",
                        "Participle (verb acting as adjective): 'A rolling stone' (present), 'The broken vase' (past)"
                    ]
                },
                {
                    "name": "2. Transitive vs. Intransitive Verbs",
                    "desc": "Transitive verbs transfer action to a direct object; Intransitive verbs do not take a direct object.",
                    "examples": [
                        "Transitive: 'The committee approved the budget' ('budget' is the direct object)",
                        "Intransitive: 'The sun rises in the east' (no direct object; 'in the east' is a prepositional adverbial)",
                        "Exam Rule: Only transitive verbs can be transformed into passive voice"
                    ]
                },
                {
                    "name": "3. Primary & Modal Auxiliary Verbs",
                    "desc": "Helping verbs that combine with main verbs to convey tense, mood, permission, necessity, or probability.",
                    "examples": [
                        "Primary Auxiliaries: Be (is, am, are, was, were), Do (do, does, did), Have (has, have, had)",
                        "Modal Auxiliaries: Can/Could (ability), May/Might (possibility/permission), Must/Ought to (obligation), Shall/Will, Should/Would",
                        "Rule: Modals are always followed directly by the bare infinitive (base form: V1 without 'to')"
                    ]
                },
                {
                    "name": "4. Stative vs. Dynamic Verbs",
                    "desc": "Dynamic verbs describe physical actions; Stative verbs express thoughts, emotions, senses, or possession.",
                    "examples": [
                        "Dynamic: Run, write, build, jump (can be used in continuous -ing tenses)",
                        "Stative: Know, believe, understand, love, belong, smell, taste, possess",
                        "Exam Trap: Stative verbs are NEVER used in continuous tenses in their primary stative sense (say 'I know him', NOT 'I am knowing him')"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Confusing Verb Pairs: 'Lie' vs. 'Lay' and 'Rise' vs. 'Raise'",
                    "explanation": "'Lie' (intransitive: lie, lay, lain, lying) means to recline; 'Lay' (transitive: lay, laid, laid, laying) means to place something down and REQUIRES a direct object. 'Rise' (intransitive) means to ascend; 'Raise' (transitive) means to lift something and REQUIRES an object.",
                    "words": ["Lie", "Lay", "Lain", "Rise", "Raise", "Transitive"],
                    "correct": "He laid the legal documents on the director's desk.",
                    "incorrect": "He lay the legal documents on the director's desk."
                },
                {
                    "rule_number": 2,
                    "title": "Gerund Preceded by Possessive Case",
                    "explanation": "A gerund (verbal noun ending in -ing) must be preceded by a noun or pronoun in the possessive case (my, his, her, their, Ram's), NOT the objective case (me, him, them).",
                    "words": ["Gerund", "Possessive Case", "Verbal Noun"],
                    "correct": "The manager objected to his arriving late to the strategic briefing.",
                    "incorrect": "The manager objected to him arriving late to the strategic briefing."
                },
                {
                    "rule_number": 3,
                    "title": "Bare Infinitive after Causative and Sensory Verbs",
                    "explanation": "Verbs of sensation (see, hear, watch, notice) and causative verbs (make, let, bid) are followed by a bare infinitive (V1 without 'to') in the active voice.",
                    "words": ["Make", "Let", "Bid", "Hear", "See", "Bare Infinitive"],
                    "correct": "The strict drill instructor made the cadets run five miles.",
                    "incorrect": "The strict drill instructor made the cadets to run five miles."
                },
                {
                    "rule_number": 4,
                    "title": "Stative Verbs Prohibited in Continuous Tenses",
                    "explanation": "Verbs expressing mental perception, senses, emotions, or possession (know, understand, believe, love, hear, smell, own, belong) cannot take the continuous (-ing) form when used in their primary stative sense.",
                    "words": ["Stative Verbs", "Continuous Tense", "Mental State"],
                    "correct": "I understand the complex macroeconomic principles clearly.",
                    "incorrect": "I am understanding the complex macroeconomic principles clearly."
                },
                {
                    "rule_number": 5,
                    "title": "Subjunctive Mood in Hypothetical & Mandatory Clauses",
                    "explanation": "In hypothetical/unreal conditions introduced by 'as if', 'if only', or 'wish', use 'were' regardless of whether the subject is singular or plural. In mandates after demand/insist/suggest, use the base verb (subjunctive).",
                    "words": ["Subjunctive", "Were", "Hypothetical", "Mandatory"],
                    "correct": "She speaks as if she were the sovereign monarch of the state.",
                    "incorrect": "She speaks as if she was the sovereign monarch of the state."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Using 'was' instead of 'were' in unreal hypothetical wishes ('I wish I was a pilot')",
                    "correction": "Use 'were': 'I wish I were a pilot.'",
                    "rationale": "Unreal or hypothetical subjunctive clauses universally mandate 'were' for all persons and numbers."
                },
                {
                    "mistake": "Using 'to' after modal verbs (e.g., 'He can to speak four international languages')",
                    "correction": "Omit 'to': 'He can speak four international languages.'",
                    "rationale": "Modal auxiliary verbs (can, could, may, might, shall, should, will, would, must) take a bare infinitive."
                },
                {
                    "mistake": "Placing an objective pronoun before a gerund ('I don't like you coming late')",
                    "correction": "Use possessive pronoun: 'I don't like your coming late.'",
                    "rationale": "Because a gerund functions as a verbal noun, it must be qualified by a possessive determiner."
                },
                {
                    "mistake": "Confusing 'laid' with 'lay' (e.g., 'The wounded soldier laid on the battlefield for hours')",
                    "correction": "Use past tense of intransitive lie: 'The wounded soldier lay on the battlefield for hours.'",
                    "rationale": "'Lay' is the past tense of intransitive 'lie' (recline); 'laid' is the past tense of transitive 'lay' (place)."
                }
            ],
            "quick_revision_points": [
                "Transitive verbs require direct objects and can be passivized; Intransitive verbs take no direct object.",
                "Lie (recline) -> Past: lay, Past Participle: lain. Lay (place) -> Past: laid, Past Participle: laid.",
                "Gerunds must be preceded by a possessive case noun/pronoun (e.g., 'my going', 'his asking').",
                "Bare infinitive (V1 without 'to') follows make, let, bid, see, hear in active voice.",
                "Stative verbs (know, believe, understand, smell, belong) cannot be used in continuous (-ing) tenses.",
                "Subjunctive mood requires 'were' for all subjects in unreal conditions: 'If I were you'."
            ]
        },
        "practice": [
            {
                "question": "Spot the error in the following sentence:\n'The executive committee made the auditor to recalculate the entire annual balance sheet.'",
                "options_json": [
                    "The executive committee",
                    "made the auditor to recalculate",
                    "the entire annual",
                    "balance sheet"
                ],
                "correct_answer": "made the auditor to recalculate",
                "explanation": "Causative verb 'make' is followed by a bare infinitive (without 'to') in the active voice. It should read: 'made the auditor recalculate'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the grammatically correct sentence using the appropriate verb form of 'lie' or 'lay':",
                "options_json": [
                    "The weary traveler lay down under the shade of the banyan tree.",
                    "The weary traveler laid down under the shade of the banyan tree.",
                    "The weary traveler has laid under the tree for three hours.",
                    "The weary traveler is laying down to rest."
                ],
                "correct_answer": "The weary traveler lay down under the shade of the banyan tree.",
                "explanation": "'Lay' is the simple past tense of the intransitive verb 'lie' (to recline). 'Laid' is the past tense of transitive 'lay' (to place an object).",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Fill in the blank with the correct pronoun form preceding the gerund:\n'The principal was pleased with ______ securing the first rank in the national scholarship test.'",
                "options_json": ["his", "him", "he", "himself"],
                "correct_answer": "his",
                "explanation": "A gerund ('securing') must be preceded by a possessive case pronoun ('his securing'), not the objective case ('him').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following sentences correctly applies the subjunctive mood for an unreal condition?",
                "options_json": [
                    "If I were the prime minister, I would prioritize primary education.",
                    "If I was the prime minister, I would prioritize primary education.",
                    "If I am the prime minister, I would prioritize primary education.",
                    "If I will be the prime minister, I would prioritize primary education."
                ],
                "correct_answer": "If I were the prime minister, I would prioritize primary education.",
                "explanation": "In hypothetical subjunctive clauses, 'were' is universally used for all subjects (even singular 'I') to express an unreal or contrary-to-fact condition.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the sentence that erroneously uses a stative verb in the continuous form:",
                "options_json": [
                    "I am understanding the nuances of the new corporate tax reform.",
                    "I understand the nuances of the new corporate tax reform.",
                    "She knows the answer to that challenging question.",
                    "This historic palace belongs to the royal trust."
                ],
                "correct_answer": "I am understanding the nuances of the new corporate tax reform.",
                "explanation": "'Understand' is a stative verb of mental cognition and should not be used in continuous tenses. It should correctly read: 'I understand'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "What is the grammatical function of 'barking' in the sentence: 'A barking dog seldom bites'?",
                "options_json": ["Present Participle functioning as an adjective", "Gerund functioning as a subject", "Finite main verb", "Bare infinitive"],
                "correct_answer": "Present Participle functioning as an adjective",
                "explanation": "'Barking' is a present participle (V + ing) modifying the noun 'dog', functioning as a verbal adjective.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct sentence regarding modal auxiliaries:",
                "options_json": [
                    "You ought to respect the constitutional institutions of the republic.",
                    "You ought respect the constitutional institutions of the republic.",
                    "You can to clear the examination with disciplined study.",
                    "You must to submit the documents by tomorrow."
                ],
                "correct_answer": "You ought to respect the constitutional institutions of the republic.",
                "explanation": "'Ought' is uniquely followed by the to-infinitive ('ought to respect'). Other modals (can, must) take a bare infinitive without 'to'.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "In the passive voice, which type of verb can NEVER form a valid passive construction?",
                "options_json": ["Intransitive verbs (e.g., sleep, arrive, laugh)", "Transitive verbs", "Ditransitive verbs", "Causative verbs"],
                "correct_answer": "Intransitive verbs (e.g., sleep, arrive, laugh)",
                "explanation": "Passive voice requires a direct object to become the new grammatical subject; therefore, intransitive verbs cannot be made passive.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The past participle of the intransitive verb 'lie' (meaning to recline) is ______.",
                "correct_answer": "lain",
                "explanation": "Principal parts of lie: lie (present), lay (past), lain (past participle).",
                "difficulty": "Hard",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "Verbs that describe states, feelings, or mental conditions rather than physical actions are known as ______ verbs.",
                "correct_answer": "stative",
                "explanation": "Stative verbs denote non-physical states and are generally not used in continuous aspect.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    4: {
        "title": "Adjectives: Degrees of Comparison, Order of Modifiers & Determinative Rules",
        "source_id": 1,
        "content": {
            "definition": "An adjective is a qualifying word that modifies, quantifies, or describes a noun or pronoun, providing specific details regarding quality, quantity, size, shape, age, color, origin, or material. In competitive examinations, questions test the Degrees of Comparison (Positive, Comparative, Superlative), the Royal Order of Cumulative Adjectives, and non-comparable adjectives.",
            "overview": "Adjectives function either Attributively (placed directly before the noun: 'a diligent student') or Predicatively (linked via a copular verb: 'the student is diligent'). Essential competitive concepts include Latin comparatives ending in '-ior', the correct use of 'older/oldest' vs. 'elder/eldest', and avoiding double comparatives and double superlatives.",
            "types": [
                {
                    "name": "1. Classifications of Adjectives",
                    "desc": "Functional categories qualifying nominal entities.",
                    "examples": [
                        "Adjective of Quality (Descriptive): brave, honest, cold, brilliant ('an honest officer')",
                        "Adjective of Quantity: some, much, little, enough, whole ('drank much water')",
                        "Adjective of Number: Definite (cardinal: one, two; ordinal: first, second) vs. Indefinite (few, many, several)",
                        "Demonstrative Adjectives: this, that, these, those ('this historical manuscript')",
                        "Distributive Adjectives: each, every, either, neither ('each participant')"
                    ]
                },
                {
                    "name": "2. Degrees of Comparison",
                    "desc": "The three morphological levels of comparative scale.",
                    "examples": [
                        "Positive Degree: Denotes simple quality without comparison ('Ramesh is tall')",
                        "Comparative Degree: Compares two entities; formed with '-er' or 'more' followed by 'than' ('Ramesh is taller than Suresh')",
                        "Superlative Degree: Compares more than two entities; preceded by 'the' and formed with '-est' or 'most' ('Ramesh is the tallest boy in the academy')"
                    ]
                },
                {
                    "name": "3. The Royal Order of Cumulative Adjectives (OSASCOMP)",
                    "desc": "Universal linguistic hierarchy when multiple adjectives precede a single noun.",
                    "examples": [
                        "O - Opinion: beautiful, charming, ugly, magnificent",
                        "S - Size: enormous, tiny, huge, compact",
                        "A - Age: ancient, modern, youthful, antique",
                        "S - Shape: circular, square, rectangular, oval",
                        "C - Color: scarlet, golden, azure, black",
                        "O - Origin: Indian, Venetian, Persian, Swiss",
                        "M - Material: wooden, silk, ceramic, steel",
                        "P - Purpose: sleeping (bag), running (shoes), dining (table)"
                    ]
                },
                {
                    "name": "4. Non-Comparable / Absolute Adjectives",
                    "desc": "Adjectives expressing absolute conditions that cannot logically admit degrees of comparison.",
                    "examples": [
                        "Absolute Words: Unique, perfect, universal, round, square, dead, supreme, complete, ideal, eternal",
                        "Exam Rule: Never say 'more unique', 'most perfect', or 'very complete'; say 'unique', 'perfect', or 'nearly complete'"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Latin Comparatives Take 'To', Not 'Than'",
                    "explanation": "Comparative adjectives borrowed from Latin ending in '-ior' (senior, junior, superior, inferior, prior, anterior, posterior) as well as 'prefer' and 'preferable' take the preposition 'to', NEVER the conjunction 'than'.",
                    "words": ["Senior", "Junior", "Superior", "Inferior", "Prior", "Preferable", "To"],
                    "correct": "He is senior to me in government administrative service.",
                    "incorrect": "He is senior than me in government administrative service."
                },
                {
                    "rule_number": 2,
                    "title": "'Elder/Eldest' vs. 'Older/Oldest'",
                    "explanation": "'Elder' and 'eldest' are used exclusively for human members of the same immediate family and are never followed by 'than'. 'Older' and 'oldest' are used for unrelated persons, animals, and inanimate objects, and can be followed by 'than'.",
                    "words": ["Elder", "Eldest", "Older", "Oldest", "Family"],
                    "correct": "His elder brother is a civil judge; this temple is older than that palace.",
                    "incorrect": "His older brother is a civil judge; he is elder than me."
                },
                {
                    "rule_number": 3,
                    "title": "Comparison Between Two Qualities in the Same Person",
                    "explanation": "When comparing two different qualities of the SAME person or object, use 'more + positive degree', NOT the '-er' inflected comparative form.",
                    "words": ["More", "Positive Degree", "Dual Qualities"],
                    "correct": "He is more brave than wise.",
                    "incorrect": "He is braver than wise."
                },
                {
                    "rule_number": 4,
                    "title": "Prohibition of Double Comparatives and Double Superlatives",
                    "explanation": "English grammar strictly prohibits combining two comparative or two superlative markers for the same adjective (e.g., 'more taller' or 'most brightest').",
                    "words": ["Double Comparative", "Double Superlative", "Redundancy"],
                    "correct": "Mount Everest is the highest mountain peak in the world.",
                    "incorrect": "Mount Everest is the most highest mountain peak in the world."
                },
                {
                    "rule_number": 5,
                    "title": "Exclusion of Antecedent with 'Any Other' in Comparisons",
                    "explanation": "When comparing an entity with the rest of its group in the comparative degree, use 'any other' to exclude the subject from the group being compared. In superlative degree, do NOT use 'other'.",
                    "words": ["Any other", "Exclusion", "Comparative", "Superlative"],
                    "correct": "Iron is more useful than any other metal.",
                    "incorrect": "Iron is more useful than any metal."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Saying 'This scheme is more preferable than that one'",
                    "correction": "Say 'This scheme is preferable to that one.'",
                    "rationale": "'Preferable' already contains comparative force and requires 'to'; adding 'more' creates an erroneous double comparative."
                },
                {
                    "mistake": "Writing 'She is elder than her colleague'",
                    "correction": "Write 'She is older than her colleague.'",
                    "rationale": "'Elder' is restricted to biological family members and cannot be followed by 'than'."
                },
                {
                    "mistake": "Saying 'Shakespeare is greater than any dramatist'",
                    "correction": "Say 'Shakespeare is greater than any other dramatist.'",
                    "rationale": "Without 'other', Shakespeare would be compared with himself, creating an illogical comparison."
                },
                {
                    "mistake": "Using 'more unique' or 'most unique'",
                    "correction": "Use 'unique' or 'wholly unique'.",
                    "rationale": "'Unique' is an absolute adjective meaning one of a kind; degrees of uniqueness are semantically invalid."
                }
            ],
            "quick_revision_points": [
                "Latin comparatives (senior, junior, superior, inferior, prior, preferable) take 'to', never 'than'.",
                "Elder/eldest is for biological family members without 'than'; older/oldest is for unrelated persons/things with 'than'.",
                "Comparing two qualities of the SAME entity: use 'more + positive degree' (e.g., 'more brave than wise').",
                "Comparative degree with class members requires 'any other': 'Diamond is harder than any other substance'.",
                "Never use double comparatives ('more faster') or double superlatives ('most greatest').",
                "Absolute adjectives: unique, perfect, universal, round, dead, complete cannot take comparative degrees."
            ]
        },
        "practice": [
            {
                "question": "Identify the sentence that correctly applies the preposition with Latin comparative adjectives:",
                "options_json": [
                    "This newly developed semiconductor chip is superior to the imported model.",
                    "This newly developed semiconductor chip is superior than the imported model.",
                    "This newly developed semiconductor chip is more superior to the imported model.",
                    "This newly developed semiconductor chip is superior from the imported model."
                ],
                "correct_answer": "This newly developed semiconductor chip is superior to the imported model.",
                "explanation": "Comparative adjectives ending in '-ior' (superior, inferior, senior, junior) strictly require the preposition 'to', not 'than'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Spot the error in the following sentence:\n'The veteran diplomat is elder than all the other delegates attending the summit.'",
                "options_json": [
                    "The veteran diplomat",
                    "is elder than",
                    "all the other delegates",
                    "attending the summit"
                ],
                "correct_answer": "is elder than",
                "explanation": "'Elder' is reserved for family relations and cannot take 'than'. For unrelated persons in comparative contexts, use 'older than'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the correct sentence comparing two qualities of the same individual:",
                "options_json": [
                    "The military officer was more courageous than prudent.",
                    "The military officer was more courageouser than prudent.",
                    "The military officer was courageouser than prudent.",
                    "The military officer was most courageous than prudent."
                ],
                "correct_answer": "The military officer was more courageous than prudent.",
                "explanation": "When comparing two different attributes in the same subject, use 'more + positive degree' ('more courageous than prudent').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following phrases is grammatically correct according to the rule of absolute adjectives?",
                "options_json": [
                    "His architectural blueprint is wholly unique.",
                    "His architectural blueprint is the most unique.",
                    "His architectural blueprint is more unique than yours.",
                    "His architectural blueprint is highly unique."
                ],
                "correct_answer": "His architectural blueprint is wholly unique.",
                "explanation": "'Unique' is an absolute adjective that cannot logically admit comparative degrees ('more unique' or 'most unique'). Adverbs like 'wholly' or 'nearly' are acceptable.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why is the sentence 'Gold is more precious than any metal' grammatically defective?",
                "options_json": [
                    "It lacks 'other', thereby including gold in the group of metals to which it is being compared.",
                    "Gold cannot be compared using the comparative degree.",
                    "'Precious' requires the suffix '-er'.",
                    "'More' should be replaced with 'most'."
                ],
                "correct_answer": "It lacks 'other', thereby including gold in the group of metals to which it is being compared.",
                "explanation": "To avoid comparing an entity with itself, 'other' must be inserted: 'Gold is more precious than any other metal.'",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Arrange the adjectives in the correct Royal Order (OSASCOMP): 'He bought a ______ table.'",
                "options_json": [
                    "beautiful round antique Italian wooden",
                    "wooden beautiful antique round Italian",
                    "Italian antique round beautiful wooden",
                    "round wooden beautiful Italian antique"
                ],
                "correct_answer": "beautiful round antique Italian wooden",
                "explanation": "Order: Opinion (beautiful) -> Shape (round) -> Age (antique) -> Origin (Italian) -> Material (wooden).",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Which determinative adjective should be used with uncountable nouns to denote an almost negligible, insufficient quantity?",
                "options_json": ["Little", "A little", "Few", "A few"],
                "correct_answer": "Little",
                "explanation": "'Little' is used with uncountable nouns in a negative sense meaning almost none; 'few' is used with plural countable nouns.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the sentence free from redundant comparative modification:",
                "options_json": [
                    "This highway is faster and safer than the coastal route.",
                    "This highway is more faster and more safer than the coastal route.",
                    "This highway is more fast and safer than the coastal route.",
                    "This highway is the most fastest route."
                ],
                "correct_answer": "This highway is faster and safer than the coastal route.",
                "explanation": "'Faster' and 'safer' are already inflected comparatives; prefixing 'more' creates an ungrammatical double comparative.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Latin comparative adjectives ending in '-ior' require the preposition ______ instead of 'than'.",
                "correct_answer": "to",
                "explanation": "Senior, junior, superior, inferior take 'to'.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "When ordering multiple adjectives before a noun, the acronym OSASCOMP begins with the letter 'O', which stands for ______.",
                "correct_answer": "Opinion",
                "explanation": "OSASCOMP starts with Opinion (e.g., lovely, ugly, fine).",
                "difficulty": "Medium",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    5: {
        "title": "Adverbs: Types, Inversion Rules, Position of Modifiers & Degree Nuances",
        "source_id": 1,
        "content": {
            "definition": "An adverb is a versatile modifying word that qualifies a verb, an adjective, another adverb, a preposition, or an entire sentence, answering questions such as How? (Manner), Where? (Place), When? (Time), How often? (Frequency), and To what extent? (Degree). In competitive examinations, adverbial testing concentrates on Grammatical Inversion after negative adverbs, split infinitives, and the critical distinction between 'fairly' vs. 'rather' and 'too' vs. 'very'.",
            "overview": "Adverbs exhibit strict positional rules: the standard sequence of adverbs following a verb is M-P-T (Manner -> Place -> Time). Furthermore, placing restrictive or negative adverbs (hardly, scarcely, seldom, rarely, never, neither) at the head of a clause triggers Subject-Auxiliary Inversion, where the helping verb precedes the subject.",
            "types": [
                {
                    "name": "1. Adverbs of Manner, Place & Time (MPT Rule)",
                    "desc": "The primary circumstantial modifiers of verbal actions.",
                    "examples": [
                        "Manner (How): diligently, gracefully, swiftly, bravely ('He fought bravely')",
                        "Place (Where): here, there, outside, everywhere ('She looked outside')",
                        "Time (When): yesterday, now, soon, tomorrow, recently ('He arrived yesterday')",
                        "Royal Order: Manner -> Place -> Time ('The orchestra played brilliantly (M) in the hall (P) last night (T)')"
                    ]
                },
                {
                    "name": "2. Adverbs of Frequency & Degree",
                    "desc": "Indicate repetition rates and qualitative intensity.",
                    "examples": [
                        "Frequency: always, never, seldom, rarely, often, frequently (placed before the main verb, but after 'be')",
                        "Degree / Intensity: very, fairly, rather, quite, extremely, too, enough",
                        "Position of 'Enough': Unlike other adverbs of degree, 'enough' is placed IMMEDIATELY AFTER the adjective/adverb it modifies ('strong enough', NOT 'enough strong')"
                    ]
                },
                {
                    "name": "3. Negative & Restrictive Adverbs",
                    "desc": "Adverbs carrying intrinsic negative or restrictive semantic force.",
                    "examples": [
                        "Words: Hardly, scarcely, barely, seldom, rarely, neither, nor, never, little",
                        "Rule: Never combine these with another negative word (avoid double negatives like 'He scarcely had no money')",
                        "Correlative Pairing: 'Hardly/Scarcely... when' and 'No sooner... than'"
                    ]
                },
                {
                    "name": "4. Interrogative & Relative Adverbs",
                    "desc": "Used to ask questions or link relative clauses denoting time, place, or reason.",
                    "examples": [
                        "Interrogative: 'When did the treaty take effect?'",
                        "Relative: 'This is the laboratory where the vaccine was developed' ('where' modifies 'laboratory')"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Grammatical Inversion with Initial Negative Adverbs",
                    "explanation": "When a sentence begins with a negative or restrictive adverb (hardly, scarcely, seldom, rarely, barely, no sooner, neither, nor, little, never), the sentence MUST employ subject-auxiliary inversion (Auxiliary Verb + Subject + Main Verb).",
                    "words": ["Hardly", "Scarcely", "Seldom", "No Sooner", "Inversion"],
                    "correct": "Seldom have I witnessed such profound diplomatic statesmanship.",
                    "incorrect": "Seldom I have witnessed such profound diplomatic statesmanship."
                },
                {
                    "rule_number": 2,
                    "title": "Position of 'Enough' as an Adverb",
                    "explanation": "When 'enough' functions as an adverb modifying an adjective or another adverb, it MUST be positioned immediately AFTER the modified word, and the modified adjective must be in the positive degree.",
                    "words": ["Enough", "Post-position", "Positive Degree"],
                    "correct": "He was brave enough to confront the armed infiltrators.",
                    "incorrect": "He was enough brave to confront the armed infiltrators."
                },
                {
                    "rule_number": 3,
                    "title": "'Fairly' vs. 'Rather'",
                    "explanation": "'Fairly' is generally used with pleasant, favorable adjectives in the positive degree (fairly good, fairly clever). 'Rather' is used with unpleasant, unfavorable adjectives (rather dull, rather late) or with comparative degrees (rather better).",
                    "words": ["Fairly", "Rather", "Pleasant", "Unpleasant"],
                    "correct": "The weather today is fairly pleasant, though the room is rather damp.",
                    "incorrect": "The weather today is rather pleasant, though the room is fairly damp."
                },
                {
                    "rule_number": 4,
                    "title": "'Too' vs. 'Very' and the 'Too... To' Construction",
                    "explanation": "'Very' emphasizes intensity in a positive or neutral sense; 'Too' signifies an excessive, objectionable degree beyond an acceptable limit. 'Too... to' has an intrinsic negative implication meaning 'so... that cannot'.",
                    "words": ["Too", "Very", "Too... To", "Excessive"],
                    "correct": "He is very intelligent, but he was too exhausted to continue working.",
                    "incorrect": "He is too intelligent to solve this problem easily."
                },
                {
                    "rule_number": 5,
                    "title": "Adverbs with and without '-ly' (Hard vs. Hardly, Late vs. Lately)",
                    "explanation": "Certain adverbs have two distinct forms with completely different meanings: 'Hard' (with great energy/effort) vs. 'Hardly' (almost not/scarcely); 'Late' (after the due time) vs. 'Lately' (recently); 'Near' (close in distance) vs. 'Nearly' (almost).",
                    "words": ["Hard", "Hardly", "Late", "Lately", "Near", "Nearly"],
                    "correct": "He worked hard all evening, but he could hardly finish the assignment.",
                    "incorrect": "He worked hardly all evening, but he could hard finish the assignment."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Failing to invert after negative adverbs ('Hardly he had arrived when the storm began')",
                    "correction": "Use inversion: 'Hardly had he arrived when the storm began.'",
                    "rationale": "Initial negative adverbs grammatically mandate the auxiliary verb to precede the grammatical subject."
                },
                {
                    "mistake": "Placing 'enough' before the adjective ('She is enough intelligent to clear the exam')",
                    "correction": "Place 'enough' after: 'She is intelligent enough to clear the exam.'",
                    "rationale": "Adverbial 'enough' follows the adjective it modifies, unlike determinative 'enough' which precedes nouns ('enough money')."
                },
                {
                    "mistake": "Pairing 'No sooner' with 'when' instead of 'than'",
                    "correction": "Use 'than': 'No sooner had the bell rung than the students entered.'",
                    "rationale": "'No sooner' is a comparative structure and must be paired with 'than'; 'hardly/scarcely' pairs with 'when'."
                },
                {
                    "mistake": "Using double negatives ('He does not know nothing about the case')",
                    "correction": "Use single negative: 'He knows nothing about the case' or 'He does not know anything about the case.'",
                    "rationale": "Two negative words cancel each other and create an ungrammatical double negative in standard English."
                }
            ],
            "quick_revision_points": [
                "Negative adverbs at sentence start (hardly, scarcely, seldom, rarely, no sooner) require inversion (Auxiliary + Subject + Verb).",
                "Pairing rules: 'Hardly/Scarcely... when' and 'No sooner... than'.",
                "The adverb 'enough' always follows the adjective/adverb it modifies ('smart enough').",
                "'Fairly' modifies favorable qualities; 'rather' modifies unfavorable qualities or comparatives.",
                "Hard = with intense effort; Hardly = almost not. Late = not on time; Lately = recently.",
                "Royal order of adverbs: Manner -> Place -> Time (MPT)."
            ]
        },
        "practice": [
            {
                "question": "Spot the error in the following sentence:\n'Scarcely he had stepped out of the office when the torrential downpour began.'",
                "options_json": [
                    "Scarcely he had stepped",
                    "out of the office",
                    "when the torrential",
                    "downpour began"
                ],
                "correct_answer": "Scarcely he had stepped",
                "explanation": "When a sentence starts with 'scarcely', grammatical inversion is mandatory: 'Scarcely had he stepped'.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Identify the correct correlative conjunction pairing for 'No sooner':",
                "options_json": [
                    "No sooner had the minister arrived than the press conference commenced.",
                    "No sooner had the minister arrived when the press conference commenced.",
                    "No sooner had the minister arrived then the press conference commenced.",
                    "No sooner had the minister arrived but the press conference commenced."
                ],
                "correct_answer": "No sooner had the minister arrived than the press conference commenced.",
                "explanation": "'No sooner' is a comparative adverbial construction and must strictly pair with 'than' (not 'when' or 'then').",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Select the sentence with the correct positioning of the adverb 'enough':",
                "options_json": [
                    "The naval officer was experienced enough to navigate through the perilous storm.",
                    "The naval officer was enough experienced to navigate through the perilous storm.",
                    "The naval officer was more enough experienced to navigate.",
                    "The naval officer was experienced enough more to navigate."
                ],
                "correct_answer": "The naval officer was experienced enough to navigate through the perilous storm.",
                "explanation": "As an adverb modifying an adjective ('experienced'), 'enough' must follow the adjective directly ('experienced enough').",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Choose the correct sentence distinguishing 'hard' from 'hardly':",
                "options_json": [
                    "The research team worked hard, but they could hardly find any reproducible results.",
                    "The research team worked hardly, but they could hard find any reproducible results.",
                    "The research team worked hard, but they could hard find any reproducible results.",
                    "The research team worked hardly, but they could hardly find any reproducible results."
                ],
                "correct_answer": "The research team worked hard, but they could hardly find any reproducible results.",
                "explanation": "'Hard' means diligently with effort; 'hardly' means scarcely or almost not.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "In what order should multiple adverbs (manner, time, place) be arranged after a verb?",
                "options_json": [
                    "Manner -> Place -> Time (MPT)",
                    "Time -> Place -> Manner",
                    "Place -> Manner -> Time",
                    "Time -> Manner -> Place"
                ],
                "correct_answer": "Manner -> Place -> Time (MPT)",
                "explanation": "The standard sequence of adverbs modifying a verb is Manner (How) -> Place (Where) -> Time (When).",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which sentence correctly uses 'fairly' or 'rather'?",
                "options_json": [
                    "The candidate performed fairly well, but the interview panel was rather hostile.",
                    "The candidate performed rather well, but the interview panel was fairly hostile.",
                    "The examination was fairly impossible to complete in two hours.",
                    "The weather is rather pleasant today."
                ],
                "correct_answer": "The candidate performed fairly well, but the interview panel was rather hostile.",
                "explanation": "'Fairly' is typically paired with pleasant/favorable qualities (well), while 'rather' is paired with unfavorable attributes (hostile).",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "What is the meaning of the adverbial construction 'too... to' in 'He is too frail to walk unaided'?",
                "options_json": [
                    "He is so frail that he cannot walk unaided.",
                    "He is very frail, but he walks unaided.",
                    "He is frail, yet he walks easily.",
                    "He can walk unaided because he is frail."
                ],
                "correct_answer": "He is so frail that he cannot walk unaided.",
                "explanation": "The 'too... to' construction carries an inherent negative semantic meaning: so frail that it is impossible for him to walk unaided.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why is 'Seldom I have seen such magnificent architecture' incorrect?",
                "options_json": [
                    "Initial negative adverbs mandate subject-auxiliary inversion: 'Seldom have I seen'.",
                    "'Seldom' cannot modify verbs.",
                    "'Seen' should be changed to 'saw'.",
                    "'Architecture' is an ungrammatical noun."
                ],
                "correct_answer": "Initial negative adverbs mandate subject-auxiliary inversion: 'Seldom have I seen'.",
                "explanation": "Sentence-initial negative/restrictive adverbs require the auxiliary verb to precede the subject.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The adverbial correlative for 'Hardly' is '______', while for 'No sooner' it is 'than'.",
                "correct_answer": "when",
                "explanation": "'Hardly/Scarcely' pairs with 'when'.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "When an adverb qualifies an adjective, the adverb 'enough' must be placed ______ the adjective it modifies.",
                "correct_answer": "after",
                "explanation": "'Enough' follows the adjective (e.g., 'rich enough', 'strong enough').",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    }
}
