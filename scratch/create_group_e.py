# create_group_e.py
# Generates english_group_e.py with complete, authentic exam material for Topics 16, 17, 18, 19, 20

import json

topic_16 = {
    "title": "Vocabulary: Etymology, Root Words, Morphological Systems & Word Families",
    "source_id": 1,
    "content": {
        "definition": "Vocabulary mastery for competitive examinations (SSC CGL, UPSC CSAT, IBPS PO, CDS) relies on etymological analysis—deconstructing words into Greek and Latin morphemes (prefixes, roots, and suffixes). Rather than rote memorization, systematic understanding of morphological roots enables candidates to deduce the precise denotative and connotative meanings of thousands of advanced academic words.",
        "overview": "A word typically consists of a root (core semantic base), an optional prefix (modifies direction, degree, or polarity), and an optional suffix (determines grammatical part of speech). For instance, 'circumlocution' decomposes into 'circum-' (around), 'loqu/locut' (speak), and '-ion' (noun indicating action or condition)—literally 'speaking around in circles'.",
        "types": [
            {
                "name": "1. High-Frequency Latin & Greek Root Families",
                "desc": "Primary morphological stems governing competitive word banks.",
                "examples": [
                    "BENE (well/good) vs MAL (bad/evil): Benefactor, Benevolent, Benign vs Malefactor, Malevolent, Malign, Maladroit",
                    "CHRON (time): Chronological, Synchronize, Anachronism, Chronic",
                    "LOQU / LOCUT (talk/speak): Eloquent, Loquacious, Circumlocution, Soliloquy, Colloquial, Grandiloquent",
                    "PATH (feeling/disease): Sympathy, Empathy, Antipathy, Apathy, Pathological",
                    "LUC / LUM (light/clarity): Lucid, Elucidate, Pellucid, Luminous, Translucent",
                    "VOR / VOUR (eat/consume): Voracious, Carnivorous, Herbivorous, Omnivorous"
                ]
            },
            {
                "name": "2. Morphological Prefixes & Polarity Shifts",
                "desc": "Affixes that alter the semantic trajectory, negation, or degree of the root.",
                "examples": [
                    "Directional & Spatial: CIRCUM- (around: circumnavigate), PER- (through/thorough: permeate, perambulate), TRANS- (across: transient)",
                    "Temporal & Positional: ANTE- (before: antecedent), POST- (after: posterity), INTRA- (within: intramural), INTER- (between: international)",
                    "Intensifiers & Negators: PAN- (all/universal: panacea, pandemic), PROTO- (first: prototype), NON-/IN-/UN-/DIS- (negation: innocuous, disparage)"
                ]
            },
            {
                "name": "3. Morphological Suffixes & Syntactic Word-Classes",
                "desc": "Terminations that establish parts of speech and operational domains.",
                "examples": [
                    "Agent / Actor (-ist, -or, -er): Philanthropist, Connoisseur, Benefactor",
                    "State / Quality (-itude, -ity, -ness): Veracity, Magnanimity, Plenitude, Vicissitude",
                    "Action / Condition (-tion, -sion, -ment): Rectification, Dissension, Aggrandizement",
                    "Adjectival Qualifiers (-ous, -ic, -ive, -ful): Pernicious, Gregarious, Munificent, Vindictive"
                ]
            },
            {
                "name": "4. High-Yield Confusable & Homophonic Word Pairs",
                "desc": "Phonetically similar or semantically proximate words deliberately targeted in error detection and fill-in-the-blanks.",
                "examples": [
                    "Compliment (praise/regards) vs Complement (that which completes or balances)",
                    "Continuous (unbroken without interruption) vs Continual (recurring frequently with intervals)",
                    "Childlike (innocent, trustful - positive) vs Childish (silly, immature - pejorative)",
                    "Alternate (every other one in turn) vs Alternative (available as another choice)",
                    "Appraise (assess the value/quality) vs Apprise (inform or notify)"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Morphological Root Deconstruction Rule",
                "explanation": "When encountering an unfamiliar polysyllabic word, isolate the prefix, root, and suffix. If the root is 'PLAC' (please/calm) and prefix is 'IM-' (not), 'implacable' denotes someone who cannot be appeased or calmed.",
                "words": ["Root Analysis", "Prefix", "Suffix", "Etymology"],
                "correct": "The magistrate recognized the defendant's implacable animosity (im- + plac + able = cannot be appeased).",
                "incorrect": "The magistrate recognized the defendant's implacable enthusiasm (Misconstruing 'implacable' as positive vigor)."
            },
            {
                "rule_number": 2,
                "title": "Connotation (Polarity) Consistency Rule",
                "explanation": "Words sharing similar denotative definitions frequently possess distinct evaluative orientations (meliorative vs pejorative). Slender (positive) vs Scrawny (negative); Frugal (prudent) vs Miserly/Parsimonious (stingy). Never substitute a pejorative term in an appreciative context.",
                "words": ["Connotation", "Denotation", "Pejorative", "Meliorative"],
                "correct": "Her frugal financial management helped the NGO survive the funding shortfall.",
                "incorrect": "Her parsimonious financial management was celebrated by the grateful community (Parsimonious implies stinginess, clashing with celebration)."
            },
            {
                "rule_number": 3,
                "title": "Part-of-Speech Invariance in Vocabulary Application",
                "explanation": "Ensure that the derived form of a root strictly matches the syntactic slot required by the sentence. Do not substitute an abstract noun where an adjectival modifier or adverbial adjunct is required.",
                "words": ["Syntactic Slot", "Derivation", "Word Class"],
                "correct": "His explanation was delivered with consummate lucidity (adjective + noun).",
                "incorrect": "His explanation was delivered with consummate lucid (adjective + adjective modifying preposition)."
            },
            {
                "rule_number": 4,
                "title": "Confusable Word Discrimination: Contextual Precision",
                "explanation": "Homophones and paronyms must be selected based on their specific semantic definition. For example, 'censure' means official rebuke/condemnation, whereas 'censor' means to suppress objectionable content.",
                "words": ["Censure vs Censor", "Paronyms", "Homophones"],
                "correct": "The ethics committee voted to censure the senator for financial misconduct.",
                "incorrect": "The ethics committee voted to censor the senator for financial misconduct."
            },
            {
                "rule_number": 5,
                "title": "Collocational Naturalness Rule",
                "explanation": "Certain academic and formal adjectives strictly collocate with specific nouns: 'unmitigated disaster' (not 'unrelieved disaster'), 'blatant lie' (not 'transparent lie'), 'rancid butter' (not 'rotten butter').",
                "words": ["Collocation", "Natural Pairing", "Usage Norms"],
                "correct": "The newly launched initiative proved to be an unmitigated disaster.",
                "incorrect": "The newly launched initiative proved to be an unbearable disaster with heavy losses (improper collocation)."
            },
            {
                "rule_number": 6,
                "title": "Prefix Polarity Reversal & Negation Checks",
                "explanation": "Beware of pseudo-negatives: 'Invaluable' does not mean 'worthless'—it means priceless/beyond monetary value. Similarly, 'inflammable' means easily set on fire, not non-combustible (the opposite is non-flammable).",
                "words": ["Invaluable", "Inflammable", "Pseudo-Negation"],
                "correct": "The rare historical manuscripts donated by the scholar were deemed invaluable by the museum.",
                "incorrect": "The discarded papers were deemed invaluable and thrown into the incinerator."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Confusing 'Continuous' with 'Continual'.",
                "correction": "Use 'continuous' for uninterrupted flow ('continuous rain for 3 hours'); use 'continual' for repeated interruptions ('continual power cuts all day').",
                "rationale": "'Continuous' means unbroken continuity in time/space, while 'continual' implies frequent recurrences with intermittent breaks."
            },
            {
                "mistake": "Using 'Compliment' instead of 'Complement'.",
                "correction": "The wine nicely complements the cheese course (complements = enhances/completes; compliments = praises).",
                "rationale": "'Complement' with an 'e' relates to completion, whereas 'compliment' with an 'i' refers to expression of admiration."
            },
            {
                "mistake": "Misunderstanding 'Invaluable' as lacking value.",
                "correction": "His advice was invaluable to the research team (invaluable = priceless, extremely precious).",
                "rationale": "The prefix 'in-' functions as an intensifier of non-measurable worth, meaning value too immense to be measured."
            },
            {
                "mistake": "Treating 'Childish' and 'Childlike' as interchangeable.",
                "correction": "She possessed a childlike wonder for the cosmos; stop making childish tantrums during team meetings.",
                "rationale": "'Childlike' connotes innocence, sincerity, and purity (positive), whereas 'childish' connotes petulance and immaturity (negative)."
            }
        ],
        "quick_revision_points": [
            "Root BENE = good/well (beneficent); MAL = evil/bad (malevolent, malcontent).",
            "Root LOQU/LOCUT = speech/talking (eloquent, circumlocution, grandiloquent).",
            "Root CHRON = time (anachronistic, chronic, synchronous); PATH = feeling (antipathy, empathy).",
            "Compliment (praise with 'i') vs Complement (completes with 'e').",
            "Appraise = evaluate monetary/qualitative worth; Apprise = inform or update.",
            "Invaluable = priceless (NOT worthless); Inflammable = easily ignited (NOT fireproof).",
            "Censure = harsh reprimand/condemnation; Censor = delete or redact prohibited content.",
            "Frugal = prudent with money (positive); Parsimonious/Miserly = stingy (pejorative)."
        ]
    },
    "practice_questions": [
        {
            "id": 1601,
            "topic_id": 16,
            "question_text": "Select the word that correctly replaces the bracketed phrase: 'The prime minister addressed the gathering in a speech that was marked by [speaking around an issue in a needlessly indirect, roundabout manner]'.",
            "question_type": "mcq",
            "options": ["circumlocution", "grandiloquence", "soliloquy", "ventriloquism"],
            "correct_answer": "circumlocution",
            "explanation": "'Circumlocution' derives from 'circum-' (around) + 'loqu' (to speak), meaning the use of many words where fewer would do, especially in a deliberate attempt to be vague or indirect.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1602,
            "topic_id": 16,
            "question_text": "Fill in the blank with the most appropriate word: 'The senior architect was asked to __________ the newly constructed civic center to establish its fair market value.'",
            "question_type": "fitb",
            "options": ["appraise", "apprise", "condemn", "censure"],
            "correct_answer": "appraise",
            "explanation": "'Appraise' means to assess the monetary value or quality of something. 'Apprise' means to inform or notify.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1603,
            "topic_id": 16,
            "question_text": "Which word carries a PEJORATIVE (negative/critical) connotation, distinguishing it from neutral or appreciative equivalents?",
            "question_type": "mcq",
            "options": ["Frugal", "Thrifty", "Prudent", "Parsimonious"],
            "correct_answer": "Parsimonious",
            "explanation": "'Frugal', 'thrifty', and 'prudent' praise careful management of resources, whereas 'parsimonious' criticizes someone as excessively cheap or stingy.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1604,
            "topic_id": 16,
            "question_text": "Choose the correct sentence regarding confusable word pairs:",
            "question_type": "mcq",
            "options": [
                "The crisp white wine perfectly compliments the creamy seafood risotto.",
                "The crisp white wine perfectly complements the creamy seafood risotto.",
                "The professor paid her a gracious complement on her thesis defense.",
                "Both elements were entirely complementary, offering mutual praises."
            ],
            "correct_answer": "The crisp white wine perfectly complements the creamy seafood risotto.",
            "explanation": "'Complement' (with 'e') means to add to in a way that enhances or completes. 'Compliment' (with 'i') means an expression of praise.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1605,
            "topic_id": 16,
            "question_text": "Identify the word whose Latin root directly means 'light' or 'clarity':",
            "question_type": "mcq",
            "options": ["Pellucid", "Loquacious", "Voracious", "Malevolent"],
            "correct_answer": "Pellucid",
            "explanation": "'Pellucid' comes from 'lucere' (to shine/light), meaning translucently clear or easily understood. 'Loquacious' stems from loqu (speak), 'voracious' from vor (eat), and 'malevolent' from mal (evil).",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1606,
            "topic_id": 16,
            "question_text": "Fill in the blank with the correct confusable word: 'Due to __________ interruptions from the faulty transmission tower, the live broadcast could not maintain audio stability.'",
            "question_type": "fitb",
            "options": ["continual", "continuous", "contiguous", "contingent"],
            "correct_answer": "continual",
            "explanation": "'Continual' denotes recurring at frequent intervals with intermittent interruptions. 'Continuous' denotes uninterrupted progression without any break.",
            "difficulty": "hard",
            "points": 1
        },
        {
            "id": 1607,
            "topic_id": 16,
            "question_text": "What is the meaning of the word 'INVALUABLE' in formal English?",
            "question_type": "mcq",
            "options": [
                "Having no worth or practical utility",
                "Priceless, of incalculable value and high worth",
                "Capable of being accurately quantified",
                "Economically deprecated or devalued"
            ],
            "correct_answer": "Priceless, of incalculable value and high worth",
            "explanation": "'Invaluable' means having a value beyond any estimated price (priceless). It is not synonymous with 'worthless'.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1608,
            "topic_id": 16,
            "question_text": "Identify the word that correctly fits both contexts: (1) An official reprimand or expression of formal disapproval; (2) To criticize someone severely in an authoritative capacity.",
            "question_type": "mcq",
            "options": ["Censor", "Censure", "Sensure", "Sensor"],
            "correct_answer": "Censure",
            "explanation": "'Censure' means the expression of formal disapproval or harsh criticism. 'Censor' means an official who examines texts/media to suppress objectionable material.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1609,
            "topic_id": 16,
            "question_text": "Which prefix indicates 'across', 'beyond', or 'through' in words such as 'transitory', 'transcend', and 'transgress'?",
            "question_type": "mcq",
            "options": ["Trans-", "Circum-", "Ante-", "Intra-"],
            "correct_answer": "Trans-",
            "explanation": "The Latin prefix 'trans-' signifies across, beyond, or through.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1610,
            "topic_id": 16,
            "question_text": "Choose the most appropriate collocation to complete the sentence: 'The sudden bankruptcy of the regional banking institution came as an __________ shock to international investors.'",
            "question_type": "mcq",
            "options": ["unmitigated", "unbearable", "unwarranted", "unsolicited"],
            "correct_answer": "unmitigated",
            "explanation": "'Unmitigated' (absolute, unqualified) collocated with nouns describing disasters, shocks, or failures ('an unmitigated disaster/shock').",
            "difficulty": "hard",
            "points": 1
        }
    ]
}

topic_17 = {
    "title": "Synonyms: Contextual Equivalence, Register, Degree & Connotative Precision",
    "source_id": 1,
    "content": {
        "definition": "A synonym is a word or phrase that means exactly or nearly the same as another word in the same language. However, in advanced competitive examinations (SSC CGL Tier-2, IBPS PO, UPSC CSAT), questions do not merely test dictionary approximations; they evaluate contextual compatibility, degree of intensity, formal register, and connotative alignment within a given sentence frame.",
        "overview": "True absolute synonyms are exceptionally rare in English because historical layering (Anglo-Saxon, Norman French, Latin, and Greek) created subtle divisions of labor. For example, 'ask' (colloquial Anglo-Saxon), 'question' (formal French), and 'interrogate' (judicial/institutional Latin) share a core semantic axis but cannot be swapped arbitrarily without disrupting register and tone.",
        "types": [
            {
                "name": "1. Cognitive (Partial) vs Absolute Synonyms",
                "desc": "Distinguishing words sharing identical semantic cores versus those restricted by specific collocations.",
                "examples": [
                    "Absolute (Extremely rare): 'Gorse' / 'Furze' (botanical names for same shrub)",
                    "Cognitive/Partial: 'Mature' / 'Ripe' (Fruit is ripe; an adult or argument is mature, NOT 'ripe')",
                    "Syntactic constraint: 'Broad' / 'Wide' ('Broad shoulders', 'wide gap', but ONLY 'broad daylight' and 'wide awake')"
                ]
            },
            {
                "name": "2. Synonyms Differentiated by Connotative Polarity",
                "desc": "Words matching in denotation but diverging sharply into positive, neutral, or negative evaluative associations.",
                "examples": [
                    "Courageous (Positive) vs Reckless / Foolhardy (Negative, implies dangerous negligence)",
                    "Determined / Resolute (Positive) vs Stubborn / Pigheaded / Obstinate (Pejorative)",
                    "Curious / Inquisitive (Positive) vs Prying / Nosy (Intrusive, negative)",
                    "Shrewd / Astute (Positive intelligence) vs Cunning / Devious / Machiavellian (Dishonest intelligence)"
                ]
            },
            {
                "name": "3. Synonyms Differentiated by Scale of Intensity",
                "desc": "Exam questions frequently require selecting the synonym that matches the exact emotional or physical magnitude.",
                "examples": [
                    "Anger (Base) -> Indignation (Anger provoked by injustice) -> Wrath / Fury (Vengeful, devastating rage)",
                    "Dislike (Base) -> Aversion (Strong distaste) -> Loathing / Abhorrence (Visceral revulsion)",
                    "Poverty (Base) -> Destitution / Penury (Severe state where basic survival necessities are absent)",
                    "Surprise (Base) -> Astonishment -> Stupefaction (Shock so intense it paralyzes cognitive response)"
                ]
            },
            {
                "name": "4. Synonyms Differentiated by Stylistic Register and Formality",
                "desc": "Classifying words by institutional, literary, legal, or vernacular appropriateness.",
                "examples": [
                    "Die (Neutral) -> Pass away (Euphemistic) -> Expire / Decease (Formal/Legal) -> Perish (Literary/Catastrophic)",
                    "Forgive (General) -> Absolve (Ecclesiastical/Moral) -> Exonerate / Acquit (Judicial)",
                    "Lethal (Clinical/Physical) -> Pernicious (Gradual, insidious harm) -> Baleful (Menacing/Foreboding)"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Strict Part-of-Speech Concordance Rule",
                "explanation": "A synonym of an adjective must be an adjective; a synonym of a noun must be a noun; a synonym of a verb must be a verb. If the target word is 'Ephemeral' (adjective), you must choose 'Transient' (adjective), not 'Transience' (noun) or 'Transitorily' (adverb).",
                "words": ["Part of Speech", "Syntactic Category", "Morphological Match"],
                "correct": "The ephemeral nature of fame -> Transient (both are adjectives).",
                "incorrect": "The ephemeral nature of fame -> Evanescence (Noun substituted for an adjective)."
            },
            {
                "rule_number": 2,
                "title": "Connotative Alignment and Polarity Matching Rule",
                "explanation": "The correct synonym in a reading passage or sentence context must maintain the evaluative stance (approbative vs pejorative) of the original word. Replacing a positive word with a pejorative near-synonym is an automatic failure.",
                "words": ["Connotation", "Evaluative Stance", "Polarity"],
                "correct": "The general was renowned for his audacious strategy -> Daring / Bold (Positive).",
                "incorrect": "The general was renowned for his audacious strategy -> Insolent (Negative, misaligns praise)."
            },
            {
                "rule_number": 3,
                "title": "Secondary and Polysemous Meaning Identification",
                "explanation": "Many high-difficulty vocabulary items in competitive exams rely on secondary or tertiary definitions rather than primary ones. 'Table' (verb = to postpone discussion), 'Weather' (verb = to survive a storm), 'Harbor' (verb = to entertain a secret grudge).",
                "words": ["Polysemy", "Secondary Meaning", "Context Clue"],
                "correct": "The cabinet decided to table the contentious bill until the monsoon session -> Defer / Postpone.",
                "incorrect": "The cabinet decided to table the contentious bill -> Furnish / Display (Literal primary meaning)."
            },
            {
                "rule_number": 4,
                "title": "Intensity/Scale Preservation Rule",
                "explanation": "Do not replace an extreme adjective with a mild qualifier. 'Impeccable' means faultless/flawless, not merely 'satisfactory' or 'decent'. Similarly, 'excoriate' means to censure with intense venom, not simply 'to critique'.",
                "words": ["Intensity", "Magnitude", "Extreme Adjectives"],
                "correct": "Her impeccable reputation remained untarnished -> Flawless / Spotless.",
                "incorrect": "Her impeccable reputation remained untarnished -> Acceptable (Severely weakens intensity)."
            },
            {
                "rule_number": 5,
                "title": "Collocational Compatibility Constraint",
                "explanation": "Synonyms cannot be freely exchanged if the structural syntax forbids the target collocation. While 'cease' and 'quit' are synonyms, we say 'quit smoking' or 'cease to exist', but never 'quit to exist'.",
                "words": ["Collocation", "Syntactic Valence", "Usage Restriction"],
                "correct": "The armed hostilities ceased at midnight.",
                "incorrect": "The armed hostilities resigned at midnight."
            },
            {
                "rule_number": 6,
                "title": "Distinguishing 'Near-Synonym' Distractors in Multiple Choice Questions",
                "explanation": "Standardized test options intentionally insert words from the same conceptual field that fail subtle semantic nuances. 'Laconic' means concise to the point of seeming terse; 'Taciturn' means habitually disinclined to speak at all.",
                "words": ["Laconic vs Taciturn", "Nuance", "Distractor Elimination"],
                "correct": "His laconic telegram contained only three words: 'Mission successfully accomplished.' (Terse brevity).",
                "incorrect": "His taciturn telegram contained only three words (Taciturn applies to personality, not texts)."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Selecting an antonym under exam speed stress.",
                "correction": "Always re-verify whether the question prompt specifies 'SYNONYM' or 'ANTONYM' before locking your response.",
                "rationale": "Examiners routinely include the exact antonym as Option A to trap hasty candidates who recognize the word association immediately."
            },
            {
                "mistake": "Selecting the wrong part of speech (e.g. choosing a noun for an adjective).",
                "correction": "Ensure the selected option matches the grammatical function of the target word in the stem.",
                "rationale": "A sentence slot requiring a modifier cannot accept a nominal or adverbial form."
            },
            {
                "mistake": "Ignoring the secondary meaning in literary/editorial passages.",
                "correction": "Check the surrounding clause: 'He harbored suspicions' means 'entertained/nursed', not 'docked a boat'.",
                "rationale": "High-level tests deliberately utilize figurative and extended meanings of familiar words."
            },
            {
                "mistake": "Conflating words of different emotional intensity.",
                "correction": "Match 'devastated' with 'shattered', not with 'disappointed'.",
                "rationale": "'Disappointed' reflects mild dissatisfaction, while 'devastated' denotes catastrophic emotional ruin."
            }
        ],
        "quick_revision_points": [
            "Audacious = bold/daring (can also mean insolent contextually).",
            "Laconic = concise/using very few words (applies to speech/writing).",
            "Taciturn = habitually silent or uncommunicative (applies to disposition).",
            "Ephemeral = transient/fleeting (lasting a very short time).",
            "Mitigate = alleviate/lessen/ease (pain or severity).",
            "Militate = work against or hinder (always followed by 'against').",
            "Exonerate = acquit/absolve from blame or criminal charges.",
            "Fastidious = meticulous/exacting/hard to please."
        ]
    },
    "practice_questions": [
        {
            "id": 1701,
            "topic_id": 17,
            "question_text": "Select the most appropriate SYNONYM of the capitalized word: 'The CEO's LACONIC statement provided no unnecessary details about the impending merger.'",
            "question_type": "mcq",
            "options": ["Verbose", "Concise", "Garrulous", "Ambiguous"],
            "correct_answer": "Concise",
            "explanation": "'Laconic' means using very few words to express what is meant; concise or succinct. 'Verbose' and 'garrulous' are antonyms meaning excessively wordy.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1702,
            "topic_id": 17,
            "question_text": "Select the closest synonym for 'EPHEMERAL':",
            "question_type": "mcq",
            "options": ["Perpetual", "Transient", "Enduring", "Invariable"],
            "correct_answer": "Transient",
            "explanation": "'Ephemeral' means lasting for a very short time. 'Transient' (fleeting, short-lived) is the direct synonym. 'Perpetual' and 'enduring' are antonyms.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1703,
            "topic_id": 17,
            "question_text": "In the sentence: 'The defense attorney produced evidence that EXONERATED the falsely accused technician', which word is the most precise synonym?",
            "question_type": "mcq",
            "options": ["Inculpated", "Absolved", "Sentenced", "Indicted"],
            "correct_answer": "Absolved",
            "explanation": "'Exonerate' means to officially absolve or free from blame or guilt. 'Inculpate' and 'indict' mean to incriminate or formally accuse.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1704,
            "topic_id": 17,
            "question_text": "Choose the correct synonym of 'FASTIDIOUS':",
            "question_type": "mcq",
            "options": ["Careless", "Meticulous", "Indifferent", "Slapdash"],
            "correct_answer": "Meticulous",
            "explanation": "'Fastidious' means very attentive to and concerned about accuracy and detail; meticulous. 'Careless' and 'slapdash' are antonyms.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1705,
            "topic_id": 17,
            "question_text": "What is the SYNONYM of 'MITIGATE' in the context: 'Measures were undertaken to mitigate the environmental impact of the dam'?",
            "question_type": "mcq",
            "options": ["Aggravate", "Alleviate", "Exacerbate", "Intensify"],
            "correct_answer": "Alleviate",
            "explanation": "'Mitigate' means to make less severe, serious, or painful; to alleviate or assuage. 'Aggravate' and 'exacerbate' mean to make worse (antonyms).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1706,
            "topic_id": 17,
            "question_text": "Select the synonym of the word 'OBDURATE':",
            "question_type": "mcq",
            "options": ["Pliable", "Stubborn", "Amenable", "Docile"],
            "correct_answer": "Stubborn",
            "explanation": "'Obdurate' means stubbornly refusing to change one's opinion or course of action; intransigent. 'Pliable', 'amenable', and 'docile' mean compliant.",
            "difficulty": "hard",
            "points": 1
        },
        {
            "id": 1707,
            "topic_id": 17,
            "question_text": "In competitive examinations, secondary meanings are vital. What does 'TABLE' mean when used as a transitive verb in parliamentary proceedings ('The chairman moved to table the amendment')?",
            "question_type": "mcq",
            "options": ["Postpone consideration of", "Pass into statutory law", "Debate vigorously", "Publish in newspapers"],
            "correct_answer": "Postpone consideration of",
            "explanation": "In parliamentary usage, to 'table' a motion means to postpone or shelve consideration of it for a later date.",
            "difficulty": "hard",
            "points": 1
        },
        {
            "id": 1708,
            "topic_id": 17,
            "question_text": "Select the closest synonym for 'PERNICIOUS':",
            "question_type": "mcq",
            "options": ["Beneficial", "Deleterious", "Innocuous", "Salubrious"],
            "correct_answer": "Deleterious",
            "explanation": "'Pernicious' means having a harmful effect, especially in a gradual or subtle way; deleterious or destructive. 'Beneficial' and 'salubrious' mean healthful.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1709,
            "topic_id": 17,
            "question_text": "Fill in the blank with the synonym of 'CANDID': 'During the post-match conference, the coach offered a remarkably __________ assessment of the squad's tactical failures.'",
            "question_type": "fitb",
            "options": ["frank", "evasive", "deceptive", "hypocritical"],
            "correct_answer": "frank",
            "explanation": "'Candid' means truthful, straightforward, and frank. 'Evasive' and 'deceptive' are antonyms.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1710,
            "topic_id": 17,
            "question_text": "Select the synonym of 'SAGACIOUS':",
            "question_type": "mcq",
            "options": ["Foolish", "Judicious", "Credulous", "Ignorant"],
            "correct_answer": "Judicious",
            "explanation": "'Sagacious' means having or showing keen mental discernment and good judgment; wise, shrewd, or judicious.",
            "difficulty": "medium",
            "points": 1
        }
    ]
}

topic_18 = {
    "title": "Antonyms: Binary Opposites, Gradable Contrasts, Negation Prefixes & Traps",
    "source_id": 1,
    "content": {
        "definition": "An antonym is a word that expresses a meaning directly contrary to or contradictory with that of another word. In competitive examinations (SSC CGL Tier 1 & 2, CDS, NDA, Bank PO), antonym questions evaluate a candidate's grasp of semantic polarity, gradable versus absolute scales, morphological negation prefixes, and deceptive options where near-synonyms are planted as traps.",
        "overview": "Antonymy operates across distinct semantic categories: Complementary (binary/either-or: living/dead), Gradable (continuous scale with intermediate degrees: freezing/scorching), Relational (converse perspectives: teacher/pupil, predator/prey), and Directional (reverse motion/orientation: ascent/descent). Recognizing the exact category prevents selecting imprecise opposites.",
        "types": [
            {
                "name": "1. Complementary (Binary / Non-Gradable) Antonyms",
                "desc": "True dichotomies where asserting one term logically necessitates the denial of the other, with no intermediate state.",
                "examples": [
                    "Dead vs Alive (One cannot be moderately alive or somewhat dead in formal semantics)",
                    "Mortal vs Immortal",
                    "Pass vs Fail",
                    "True vs False",
                    "Guilty vs Innocent"
                ]
            },
            {
                "name": "2. Gradable Antonyms (Continuous Spectrum)",
                "desc": "Opposites positioned at extreme poles of an evaluative continuum, permitting degrees of intensity and intermediate steps.",
                "examples": [
                    "Freezing <-> Cold <-> Tepid <-> Warm <-> Boiling / Scorching",
                    "Tiny / Infinitesimal <-> Small <-> Medium <-> Large <-> Colossal / Gigantic",
                    "Destitute / Penurious <-> Poor <-> Comfortable <-> Wealthy <-> Opulent / Affluent"
                ]
            },
            {
                "name": "3. Relational (Converse) Antonyms",
                "desc": "Pairs that describe the same fundamental relationship or transaction from reciprocal, opposite viewpoints.",
                "examples": [
                    "Employer vs Employee",
                    "Lend vs Borrow",
                    "Doctor vs Patient",
                    "Above vs Below",
                    "Predecessor vs Successor"
                ]
            },
            {
                "name": "4. Morphologically Derived Antonyms (Prefix Systems)",
                "desc": "Formed by affixing negative or reversive prefixes, which must be distinguished from pseudo-negative traps.",
                "examples": [
                    "IN- / IM- / IL- / IR-: Inarticulate, Impeccable/Peccable, Illegitimate, Irrevocable",
                    "UN-: Unprecedented, Unassuming, Uncouth",
                    "DIS-: Disdain, Disseminate, Dispassionate",
                    "A- / AN-: Apathy, Anomaly, Asymmetrical",
                    "ANTI- / CONTRA-: Antipathy, Contradict, Contraindicate"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Scale-Magnitude Congruence Rule",
                "explanation": "When an extreme gradable adjective is tested, its correct antonym must occupy the opposite extreme end of the scale, not a mild midpoint. The opposite of 'Opulent' (extremely luxurious/wealthy) is 'Penurious' or 'Destitute', not merely 'Modest' or 'Average'.",
                "words": ["Gradable Scale", "Magnitude", "Extreme Polarity"],
                "correct": "Opulent lifestyle -> Destitute / Penurious (Matches extreme magnitude).",
                "incorrect": "Opulent lifestyle -> Moderate (Fails to match polar magnitude)."
            },
            {
                "rule_number": 2,
                "title": "Part-of-Speech and Syntactic Concordance Rule",
                "explanation": "The antonym must strictly match the grammatical category (word class) of the prompt word: noun to noun, verb to verb, adjective to adjective. The antonym of 'Frugality' (noun) is 'Extravagance' (noun), NOT 'Extravagant' (adjective).",
                "words": ["Part of Speech", "Grammatical Category", "Concordance"],
                "correct": "Frugality (noun) -> Prodigality / Extravagance (noun).",
                "incorrect": "Frugality (noun) -> Prodigal (adjective - incorrect class)."
            },
            {
                "rule_number": 3,
                "title": "Polysemous Context Discrimination Rule",
                "explanation": "If a word has multiple meanings, identify its contextual sense before determining the opposite. 'Light' opposed to 'Dark' (color/illumination); 'Light' opposed to 'Heavy' (weight); 'Light' opposed to 'Profound / Serious' (intellectual depth).",
                "words": ["Polysemy", "Contextual Sense", "Polarity Determination"],
                "correct": "A light commentary on geopolitical conflict -> Profound / Weighty.",
                "incorrect": "A light commentary on geopolitical conflict -> Dark / Black."
            },
            {
                "rule_number": 4,
                "title": "Asymmetric Prefix Traps Awareness Rule",
                "explanation": "Beware of false prefix antonymy. Adding 'in-' or 'un-' does not always produce an antonym. 'Valuable' and 'Invaluable' are NOT opposites (both describe great value). 'Flammable' and 'Inflammable' are synonyms (both catch fire). The antonym of 'Valuable' is 'Worthless'; the antonym of 'Inflammable' is 'Non-flammable'.",
                "words": ["False Prefix Antonymy", "Invaluable", "Inflammable"],
                "correct": "The antonym of 'Valuable' is 'Worthless'.",
                "incorrect": "The antonym of 'Valuable' is 'Invaluable' (Invaluable means priceless)."
            },
            {
                "rule_number": 5,
                "title": "Evaluative Polarity Flip Rule",
                "explanation": "If the prompt word conveys an approbative (positive) judgment, its antonym must convey a pejorative (negative) or deficiency judgment, and vice versa. 'Magnanimous' (noble, generous) opposes 'Pusillanimous' or 'Spiteful/Vindictive'.",
                "words": ["Evaluative Polarity", "Magnanimous", "Pusillanimous"],
                "correct": "Magnanimous victor -> Petty / Spiteful / Pusillanimous.",
                "incorrect": "Magnanimous victor -> Victorious (Synonymous) or Strong (Irrelevant)."
            },
            {
                "rule_number": 6,
                "title": "Elimination of Contextual Synonyms Posed as Distractors",
                "explanation": "Examiners consistently include the closest synonym among the 4 options. In speed reading, a candidate's mental lexicon fires synonym connections first. Mentally frame the phrase 'THE EXACT OPPOSITE OF [X] IS...' before reviewing the options.",
                "words": ["Distractor Elimination", "Synonym Trap", "Mental Framing"],
                "correct": "Prompt: LOQUACIOUS -> Opposite: TACITURN / RETICENT.",
                "incorrect": "Prompt: LOQUACIOUS -> Mistakenly selecting TALKATIVE (synonym trap)."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Selecting the synonym because it appears familiar.",
                "correction": "Circle the instruction 'ANTONYM' or 'OPPOSITE IN MEANING' on your scratch pad to maintain focus.",
                "rationale": "Over 40% of negative marks in vocabulary sections occur from selecting the synonym when the question demanded the antonym."
            },
            {
                "mistake": "Failing to match the extremity of the vocabulary word.",
                "correction": "Pair 'nadir' with 'zenith' or 'pinnacle', not with 'elevation'.",
                "rationale": "'Nadir' is the lowest possible point; its true antonym is the absolute highest apex ('zenith')."
            },
            {
                "mistake": "Confusing 'Disinterested' with 'Uninterested'.",
                "correction": "'Disinterested' means impartial/unbiased (antonym: Biased/Prejudiced); 'Uninterested' means bored/indifferent (antonym: Enthusiastic/Keen).",
                "rationale": "'Disinterested' does not mean lacking interest; it means having no self-serving stake in the outcome."
            },
            {
                "mistake": "Picking a word with an incorrect prefix without verifying existence.",
                "correction": "The antonym of 'couth' is 'uncouth'; the opposite of 'scathed' is 'unscathed'; avoid fabricated forms.",
                "rationale": "English prefixation is idiosyncratic; not all words take 'un-' or 'in-' uniformly."
            }
        ],
        "quick_revision_points": [
            "Zenith (highest point) <-> Nadir (lowest point).",
            "Disinterested (impartial) <-> Biased / Prejudiced / Partial.",
            "Ephemeral / Transient (fleeting) <-> Eternal / Perpetual / Permanent.",
            "Loquacious / Garrulous (talkative) <-> Taciturn / Reticent / Laconic.",
            "Magnanimous (noble/generous) <-> Pusillanimous / Petty / Vindictive.",
            "Alleviate / Mitigate (lessen) <-> Aggravate / Exacerbate (worsen).",
            "Candid (honest/frank) <-> Deceitful / Evasive / Insincere.",
            "Affluent / Opulent (wealthy) <-> Penurious / Destitute / Impoverished."
        ]
    },
    "practice_questions": [
        {
            "id": 1801,
            "topic_id": 18,
            "question_text": "Select the most appropriate ANTONYM of the word 'ZENITH':",
            "question_type": "mcq",
            "options": ["Apex", "Nadir", "Pinnacle", "Acme"],
            "correct_answer": "Nadir",
            "explanation": "'Zenith' means the highest point or culminating peak. Its exact antonym is 'Nadir' (the lowest point). 'Apex', 'pinnacle', and 'acme' are synonyms.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1802,
            "topic_id": 18,
            "question_text": "Select the correct ANTONYM of 'LOQUACIOUS':",
            "question_type": "mcq",
            "options": ["Garrulous", "Voluble", "Taciturn", "Eloquent"],
            "correct_answer": "Taciturn",
            "explanation": "'Loquacious' means talking a great deal; talkative. 'Taciturn' means habitually silent or disinclined to speak (the exact antonym).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1803,
            "topic_id": 18,
            "question_text": "What is the true ANTONYM of 'DISINTERESTED' when used in reference to an arbitrator or judge?",
            "question_type": "mcq",
            "options": ["Bored", "Partial", "Impartial", "Unconcerned"],
            "correct_answer": "Partial",
            "explanation": "'Disinterested' means unbiased and impartial. Its opposite is 'Partial' or 'Biased'. Note: 'Uninterested' means bored, not 'disinterested'.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1804,
            "topic_id": 18,
            "question_text": "Select the opposite of the underlined word: 'The state government launched policies to encourage [FRUGALITY] in departmental expenditure.'",
            "question_type": "mcq",
            "options": ["Parsimony", "Prodigality", "Providence", "Prudence"],
            "correct_answer": "Prodigality",
            "explanation": "'Frugality' means thriftiness and prudent spending. Its antonym is 'Prodigality' (reckless extravagance or wastefulness).",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1805,
            "topic_id": 18,
            "question_text": "Choose the most appropriate ANTONYM for 'EXACERBATE':",
            "question_type": "mcq",
            "options": ["Aggravate", "Worsen", "Alleviate", "Intensify"],
            "correct_answer": "Alleviate",
            "explanation": "'Exacerbate' means to make a problem, bad situation, or negative feeling worse. Its antonym is 'Alleviate' (to make less severe; relieve).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1806,
            "topic_id": 18,
            "question_text": "Select the opposite of 'CANDID':",
            "question_type": "mcq",
            "options": ["Frank", "Blunt", "Devious", "Forthright"],
            "correct_answer": "Devious",
            "explanation": "'Candid' means truthful, straightforward, and frank. Its antonym is 'Devious' (underhanded, deceitful, insincere).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1807,
            "topic_id": 18,
            "question_text": "Fill in the blank with the correct antonym of 'EPHEMERAL': 'Unlike the ephemeral fads of fast fashion, classical tailoring is designed to be __________.'",
            "question_type": "fitb",
            "options": ["perpetual", "transient", "momentary", "fleeting"],
            "correct_answer": "perpetual",
            "explanation": "'Ephemeral' means lasting a very short time. 'Perpetual' (everlasting, permanent) provides the exact semantic antithesis.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1808,
            "topic_id": 18,
            "question_text": "Select the antonym of 'PUSILLANIMOUS':",
            "question_type": "mcq",
            "options": ["Cowardly", "Craven", "Courageous", "Timid"],
            "correct_answer": "Courageous",
            "explanation": "'Pusillanimous' means showing a lack of courage or determination; timid/cowardly. Its antonym is 'Courageous' or 'Valiant'.",
            "difficulty": "hard",
            "points": 1
        },
        {
            "id": 1809,
            "topic_id": 18,
            "question_text": "What is the antonym of 'OPULENT' in terms of economic scale?",
            "question_type": "mcq",
            "options": ["Affluent", "Lavish", "Penurious", "Ostentatious"],
            "correct_answer": "Penurious",
            "explanation": "'Opulent' means ostentatiously rich, luxurious, or lavish. Its opposite at the extreme polar end of the spectrum is 'Penurious' (extremely poor, destitute).",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1810,
            "topic_id": 18,
            "question_text": "Select the word opposite in meaning to 'GREGARIOUS':",
            "question_type": "mcq",
            "options": ["Sociable", "Companionable", "Reclusive", "Extroverted"],
            "correct_answer": "Reclusive",
            "explanation": "'Gregarious' means fond of company and sociable. Its antonym is 'Reclusive' (avoiding the company of other people; solitary).",
            "difficulty": "easy",
            "points": 1
        }
    ]
}

topic_19 = {
    "title": "One Word Substitution: Systematic Categorization, Etymological Suffixes & Exam Lexicons",
    "source_id": 1,
    "content": {
        "definition": "One Word Substitution (OWS) is the syntactic and stylistic process of replacing a verbose, descriptive clause or phrase with a single, semantically precise lexical item. In Indian competitive examinations (SSC CGL, CHSL, CPO, CDS, NDA, State PSCs), OWS questions test specialized vocabulary organized into thematic clusters such as scientific disciplines, political systems, personality archetypes, phobias, manias, and types of killing.",
        "overview": "Mastery of OWS relies on identifying operational suffixes and classical root words. For instance, suffixes like '-logy' (study of), '-cracy' (rule by), '-cide' (act of killing), '-phil' (lover of), and '-phobia' (morbid fear) provide immediate semantic blueprints. Combining these with core nominal roots instantly decodes hundreds of competitive exam substitutions.",
        "types": [
            {
                "name": "1. Governance, Political Systems & Administration",
                "desc": "Terms categorizing structures of state power, rule, and bureaucratic authority.",
                "examples": [
                    "Rule by one person with unlimited authority -> Autocracy / Despotism",
                    "Rule by a small group of powerful elites -> Oligarchy",
                    "Rule by the wealthy classes -> Plutocracy",
                    "Rule by religious leaders claiming divine authority -> Theocracy",
                    "Absence of government and order; absolute lawlessness -> Anarchy",
                    "Rule by officials and unelected administrators -> Bureaucracy"
                ]
            },
            {
                "name": "2. Personality Archetypes, Behaviors & Habits",
                "desc": "Lexical descriptions of human psychological dispositions, traits, and eccentricities.",
                "examples": [
                    "One who loves and promotes the welfare of humanity (generous donor) -> Philanthropist",
                    "One who hates or distrusts humankind -> Misanthrope",
                    "One who hates or holds prejudice against women -> Misogynist",
                    "One who walks in their sleep -> Somnambulist (cf. Somniloquist = talks in sleep)",
                    "One who speaks many languages fluently -> Polyglot / Multilingual",
                    "A person obsessively absorbed in self-interest without regard for others -> Egoist (cf. Egotist = boasts constantly)"
                ]
            },
            {
                "name": "3. Fields of Scientific Study & Knowledge (-logy, -ics)",
                "desc": "Systematic scientific branches, scholastic pursuits, and collecting hobbies.",
                "examples": [
                    "The scientific study of birds -> Ornithology",
                    "The collection and study of postage stamps -> Philately (practitioner: Philatelist)",
                    "The collection and study of coins, banknotes, and medals -> Numismatics (practitioner: Numismatist)",
                    "The scientific study of insects -> Entomology",
                    "The study of the historical origin and evolution of words -> Etymology",
                    "The study of human cultures and physical evolution -> Anthropology"
                ]
            },
            {
                "name": "4. Morbid Fears (-phobia), Obsessions (-mania) & Killings (-cide)",
                "desc": "Psychological conditions and terminology for termination of life.",
                "examples": [
                    "Morbid fear of confined, enclosed spaces -> Claustrophobia",
                    "Morbid fear of open or crowded public places -> Agoraphobia",
                    "Obsessive desire to steal without economic motive -> Kleptomania",
                    "Obsession with setting fires -> Pyromania",
                    "Killing of a king or monarch -> Regicide",
                    "Killing of one's father -> Patricide (cf. Matricide = mother; Fratricide = brother; Uxoricide = wife)"
                ]
            },
            {
                "name": "5. Sanctuaries, Habitats & Enclosures",
                "desc": "Places specifically maintained for preservation, housing, or storage.",
                "examples": [
                    "A place where bees are kept and reared -> Apiary (Root: Apis = bee)",
                    "A large cage or building for keeping birds -> Aviary (Root: Avis = bird)",
                    "A place where weapons, munitions, and military equipment are stored -> Arsenal",
                    "A place where public, historical records are preserved -> Archives",
                    "A building where dead bodies are kept before burial or autopsy -> Mortuary / Morgue"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Suffix-Driven Etymological Decoding Rule",
                "explanation": "Identify the primary terminal morpheme: '-cide' indicates killing; '-gamy' indicates marriage; '-cracy' indicates government; '-mania' indicates obsessive compulsion; '-phobia' indicates morbid aversion.",
                "words": ["Suffix Decoding", "-cide", "-cracy", "-phobia", "-mania"],
                "correct": "Killing of a brother -> Frater (brother) + cide = Fratricide.",
                "incorrect": "Killing of a brother -> Sororicide (Soror = sister; incorrect root)."
            },
            {
                "rule_number": 2,
                "title": "Precision over Approximation Rule",
                "explanation": "One Word Substitutions represent exact conceptual definitions, not approximate synonyms. Distinguish 'Altruist' (one motivated by selfless regard for others) from 'Philanthropist' (specifically one who donates money and resources to charitable causes).",
                "words": ["Precision", "Altruist vs Philanthropist", "Exact Definition"],
                "correct": "One who donates immense wealth to build hospitals -> Philanthropist.",
                "incorrect": "One who donates immense wealth to build hospitals -> Altruist (Lacks the specific charitable endowment sense)."
            },
            {
                "rule_number": 3,
                "title": "Egoist vs Egotist Distinction",
                "explanation": "An 'Egoist' is a selfish person centered on personal advantage (thinking of self). An 'Egotist' (with 't' for 'talk') is a boastful, conceited person who talks incessantly about his own accomplishments.",
                "words": ["Egoist vs Egotist", "Boasting", "Self-Interest"],
                "correct": "He bored everyone at dinner by endlessly boasting about his triumphs; he is an insufferable egotist.",
                "incorrect": "He refused to share his food during the crisis; he is an insufferable egotist (Should be egoist)."
            },
            {
                "rule_number": 4,
                "title": "Faunal Root Alignment (Apiary vs Aviary)",
                "explanation": "Never confuse 'Apiary' with 'Aviary'. Latin 'Apis' = Bee (Apiary = bee yard); Latin 'Avis' = Bird (Aviary = bird enclosure). Similarly, 'Pisciculture' relates to fish, while 'Sericulture' relates to silkworms.",
                "words": ["Apiary", "Aviary", "Latin Faunal Roots"],
                "correct": "The beekeeper inspected the honeycombs in his apiary.",
                "incorrect": "The beekeeper inspected the honeycombs in his aviary."
            },
            {
                "rule_number": 5,
                "title": "Grammatical Part-of-Speech Alignment",
                "explanation": "The substitute word must match the part of speech implied in the descriptive prompt. If the prompt begins with 'A person who...', the substitute must be a noun designating a person ('Optimist', 'Misanthrope'), not an adjective ('Optimistic', 'Misanthropic').",
                "words": ["Grammatical Alignment", "Agent Noun", "Adjectival Descriptors"],
                "correct": "A person who looks on the bright side of things -> Optimist (Noun).",
                "incorrect": "A person who looks on the bright side of things -> Optimistic (Adjective)."
            },
            {
                "rule_number": 6,
                "title": "Temporal and Situational Invariance",
                "explanation": "Certain substitutions apply strictly to specific historical, biological, or institutional contexts. 'Posthumous' applies to an award, child, or book appearing after the death of the originator; it cannot be applied to an ongoing enterprise.",
                "words": ["Posthumous", "Temporal Context", "Situational Exactness"],
                "correct": "The Param Vir Chakra was awarded to the soldier posthumously.",
                "incorrect": "The retired officer accepted his award posthumously (The officer is still living)."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Confusing 'Apiary' (bees) with 'Aviary' (birds).",
                "correction": "Remember: 'Apis' = Bee (Apiary); 'Avis' = Bird (Aviary).",
                "rationale": "This single question has appeared in over 15 SSC and State PSC Tier-1 tests."
            },
            {
                "mistake": "Confusing 'Entomology' (insects) with 'Etymology' (word origins).",
                "correction": "Entomology = Study of insects (Entoma); Etymology = Study of true word origins (Etymos).",
                "rationale": "High phonetic resemblance leads candidates to misread the stem under time pressure."
            },
            {
                "mistake": "Conflating 'Oligarchy' and 'Plutocracy'.",
                "correction": "Oligarchy is rule by a small elite group (political/social); Plutocracy is specifically rule by the wealthy class.",
                "rationale": "'Ploutos' is Greek for wealth; 'Oligos' is Greek for few."
            },
            {
                "mistake": "Confusing 'Somnambulist' (sleepwalker) with 'Somniloquist' (sleeptalker).",
                "correction": "Somn- (sleep) + ambul (walk) = walker; Somn- (sleep) + loqu (talk) = speaker.",
                "rationale": "Both contain 'somn-' (sleep); the second root determines the specific physical action."
            }
        ],
        "quick_revision_points": [
            "Apiary = place where bees are kept; Aviary = place where birds are kept.",
            "Entomology = study of insects; Etymology = study of origins and history of words.",
            "Numismatist = collector of coins/medals; Philatelist = collector of postage stamps.",
            "Plutocracy = government by the wealthy; Oligarchy = government by a small cabal.",
            "Theocracy = government governed by divine/religious authorities; Anarchy = lawlessness.",
            "Somnambulist = one who walks in sleep; Somniloquist = one who talks in sleep.",
            "Misanthrope = hater of mankind; Philanthropist = lover of mankind / charitable benefactor.",
            "Regicide = murder of a king; Fratricide = murder of a brother; Patricide = murder of father."
        ]
    },
    "practice_questions": [
        {
            "id": 1901,
            "topic_id": 19,
            "question_text": "Select the option that can be used as a ONE-WORD substitute for the given group of words: 'A place where bees are kept and maintained for honey production.'",
            "question_type": "mcq",
            "options": ["Aviary", "Apiary", "Aquarium", "Sanctuary"],
            "correct_answer": "Apiary",
            "explanation": "An 'Apiary' is a place where bees and beehives are kept (from Latin apis = bee). An 'Aviary' is a place where birds are kept.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1902,
            "topic_id": 19,
            "question_text": "Give one word for: 'The scientific study of the origin, history, and development of words.'",
            "question_type": "mcq",
            "options": ["Entomology", "Etymology", "Epistemology", "Eschatology"],
            "correct_answer": "Etymology",
            "explanation": "'Etymology' is the study of the origin of words and the historical development of their forms and meanings. 'Entomology' is the study of insects.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1903,
            "topic_id": 19,
            "question_text": "What is the term for 'A person who collects or studies coins, banknotes, and medals'?",
            "question_type": "mcq",
            "options": ["Philatelist", "Numismatist", "Cartographer", "Anthropologist"],
            "correct_answer": "Numismatist",
            "explanation": "A 'Numismatist' is a specialist who collects or studies coins and currency. A 'Philatelist' collects postage stamps.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1904,
            "topic_id": 19,
            "question_text": "Select the one-word substitute: 'A form of government in which supreme power is held by the wealthiest social class.'",
            "question_type": "mcq",
            "options": ["Oligarchy", "Aristocracy", "Plutocracy", "Autocracy"],
            "correct_answer": "Plutocracy",
            "explanation": "A 'Plutocracy' is government by the wealthy (Greek ploutos = wealth). 'Oligarchy' is rule by a small elite group.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1905,
            "topic_id": 19,
            "question_text": "One who walks while sleeping is known as a:",
            "question_type": "mcq",
            "options": ["Somnambulist", "Somniloquist", "Insomniac", "Noctambulist"],
            "correct_answer": "Somnambulist",
            "explanation": "A 'Somnambulist' (somn- sleep + ambul- walk) is a sleepwalker. A 'Somniloquist' is someone who talks in sleep.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1906,
            "topic_id": 19,
            "question_text": "Select the correct term: 'An irrational, intense morbid fear of confined or enclosed spaces.'",
            "question_type": "mcq",
            "options": ["Agoraphobia", "Claustrophobia", "Hydrophobia", "Acrophobia"],
            "correct_answer": "Claustrophobia",
            "explanation": "'Claustrophobia' is the extreme or irrational fear of confined places. 'Agoraphobia' is fear of open or crowded spaces.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1907,
            "topic_id": 19,
            "question_text": "Fill in the blank with the appropriate one-word substitute: 'Because of his selfless devotion to human welfare, the industrialist was hailed as a great __________ after donating his fortunes to cancer research.'",
            "question_type": "fitb",
            "options": ["philanthropist", "misanthrope", "misogynist", "mercenary"],
            "correct_answer": "philanthropist",
            "explanation": "A 'Philanthropist' (phil- love + anthropos- human) is a person who seeks to promote the welfare of others, especially by the generous donation of money to good causes.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1908,
            "topic_id": 19,
            "question_text": "What is the one-word substitution for 'The act of killing a king or reigning monarch'?",
            "question_type": "mcq",
            "options": ["Homicide", "Regicide", "Patricide", "Fratricide"],
            "correct_answer": "Regicide",
            "explanation": "'Regicide' is the action of killing a king (Latin rex/regis = king + -cide = killing).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 1909,
            "topic_id": 19,
            "question_text": "A person who is excessively boastful and constantly talks about their own achievements and importance is an:",
            "question_type": "mcq",
            "options": ["Egoist", "Egotist", "Altruist", "Introvert"],
            "correct_answer": "Egotist",
            "explanation": "An 'Egotist' is a person who talks excessively about themselves. An 'Egoist' is a self-centered or selfish person who prioritizes self-interest.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 1910,
            "topic_id": 19,
            "question_text": "Select the one-word substitution: 'A child born after the death of its father, or a book published after the author's death.'",
            "question_type": "mcq",
            "options": ["Post-facto", "Posthumous", "Posterior", "Premature"],
            "correct_answer": "Posthumous",
            "explanation": "'Posthumous' describes something occurring, awarded, or appearing after the death of the originator or parent.",
            "difficulty": "medium",
            "points": 1
        }
    ]
}

topic_20 = {
    "title": "Idioms and Phrases: Etymological Origins, Metaphorical Logic & Exam Applications",
    "source_id": 1,
    "content": {
        "definition": "An idiom is a conventionalized multi-word figurative expression whose overarching semantic meaning cannot be directly deduced from the literal definitions of its constituent words. In competitive examinations (SSC CGL Tier 1/2, IBPS PO, CDS, NDA), candidates must demonstrate a comprehensive knowledge of idiomatic origins (nautical, classical, agricultural, biblical, and historical), structural rigidity (no arbitrary synonym substitutions), and proper situational application.",
        "overview": "Idioms have fixed grammatical configurations. Swapping prepositions, altering noun numbers, or substituting synonyms destroys idiomatic validity (e.g., 'kick the bucket' cannot become 'strike the pail'; 'at a stone's throw' cannot be 'at a rock's throw'). Questions test candidate ability to recognize genuine idiomatic meanings and avoid literal distractors.",
        "types": [
            {
                "name": "1. Nautical, Maritime & Military Origin Idioms",
                "desc": "Expressions derived from naval operations, warfare, and seafaring command.",
                "examples": [
                    "Burn one's boats / bridges -> Cut off all possibilities of retreat; commit irrevocably to a course",
                    "Show one's true colors -> Reveal one's real character or intentions (from naval battle flags)",
                    "At loggerheads -> In violent dispute or persistent disagreement",
                    "Bite the bullet -> Face a grim or painful situation with fortitude (from battlefield surgery before anesthesia)",
                    "Steal someone's thunder -> Win praise by preempting or copying someone else's idea or achievement"
                ]
            },
            {
                "name": "2. Animal, Nature & Agricultural Metaphors",
                "desc": "Idioms rooted in biological observations, farming practices, and animal lore.",
                "examples": [
                    "A wild goose chase -> A foolish, futile, and hopeless search or pursuit",
                    "Let the cat out of the bag -> Disclose a secret carelessly or prematurely",
                    "Separate the wheat from the chaff -> Distinguish valuable items/people from worthless ones",
                    "Smell a rat -> Suspect deceit, foul play, or treachery",
                    "Barking up the wrong tree -> Directing efforts or accusations toward the wrong target"
                ]
            },
            {
                "name": "3. Anatomical (Body Part) Idioms",
                "desc": "Expressions utilizing eyes, ears, hands, tongue, or feet to convey abstract social conditions.",
                "examples": [
                    "Turn a blind eye -> Deliberately refuse to acknowledge or notice something objectionable",
                    "Keep someone at arm's length -> Avoid developing intimacy or close familiarity with someone",
                    "Pay through the nose -> Pay an exorbitant, unreasonably high price",
                    "By the skin of one's teeth -> Barely escape or succeed by a very narrow margin",
                    "A feather in one's cap -> An achievement, honor, or distinction to be proud of"
                ]
            },
            {
                "name": "4. Classical Mythology, Biblical & Historical Idioms",
                "desc": "Phrases referencing ancient lore, Greek tragedy, or historical turning points.",
                "examples": [
                    "Achilles' heel -> A vulnerable point in an otherwise strong situation or person",
                    "Pyrrhic victory -> A victory won at such devastating cost that it equals defeat",
                    "Damocles' sword -> An imminent, ever-present peril or impending disaster",
                    "Cross the Rubicon -> Take an irreversible step that commits one to a specific destiny",
                    "Apple of discord -> A foundational cause of dispute, rivalry, or war"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Syntactic and Lexical Fixity Rule",
                "explanation": "Idiomatic expressions possess immutable lexical structures. You cannot pluralize singular nouns, change prepositions, or substitute synonyms. It is 'at the eleventh hour', NEVER 'at the eleventh time' or 'in the eleventh hour'.",
                "words": ["Lexical Rigidity", "Syntactic Fixity", "Fixed Phrase"],
                "correct": "The committee reached a consensus at the eleventh hour.",
                "incorrect": "The committee reached a consensus in the final eleventh hour."
            },
            {
                "rule_number": 2,
                "title": "Literal Interpretation Trap Elimination",
                "explanation": "If a multiple-choice option interprets an idiom using the literal objects mentioned in the stem (e.g. interpreting 'spill the beans' as dropping vegetables on the floor), it is an intentional distractor. Eliminate it immediately.",
                "words": ["Literal Trap", "Figurative Meaning", "Distractor Elimination"],
                "correct": "'Spill the beans' means to reveal confidential information prematurely.",
                "incorrect": "'Spill the beans' means to waste agricultural produce during harvest."
            },
            {
                "rule_number": 3,
                "title": "Strict Prepositional Congruence in Phrasal Idioms",
                "explanation": "Ensure the accompanying preposition strictly adheres to idiomatic convention: 'in hot water' (in trouble), 'on cloud nine' (ecstatic), 'under the weather' (slightly unwell), 'at daggers drawn' (bitterly hostile).",
                "words": ["Prepositional Congruence", "In hot water", "At daggers drawn"],
                "correct": "The neighboring factions have been at daggers drawn for three generations.",
                "incorrect": "The neighboring factions have been with daggers drawn for three generations."
            },
            {
                "rule_number": 4,
                "title": "Valence and Connotative Polarity Preservation",
                "explanation": "Idioms convey specific emotional polarity. 'Pyrrhic victory' cannot be used to celebrate an unmitigated triumph; it emphasizes catastrophic cost. 'White elephant' denotes a burdensome possession, never a magnificent asset.",
                "words": ["Pyrrhic Victory", "White Elephant", "Connotative Polarity"],
                "correct": "The prolonged patent litigation was a Pyrrhic victory; the firm went bankrupt paying legal fees.",
                "incorrect": "Winning the championship without conceding a single goal was a Pyrrhic victory for the team."
            },
            {
                "rule_number": 5,
                "title": "Register and Pragmatic Fittingness Rule",
                "explanation": "Select idioms that correspond to the pragmatic register of the sentence. Do not combine overly informal idioms into formal statutory reports unless specifically quoted.",
                "words": ["Pragmatic Fittingness", "Register", "Context"],
                "correct": "The audit revealed that several executives had feathered their own nests.",
                "incorrect": "The official treaty declared that both countries would chill out."
            },
            {
                "rule_number": 6,
                "title": "Avoiding Redundant Idiomatic Stacking",
                "explanation": "Do not duplicate the literal meaning of an idiom immediately following it in the same independent clause: 'He was at his wits' end and completely did not know what to do' creates clumsy tautology.",
                "words": ["Tautology", "Redundancy", "Conciseness"],
                "correct": "Faced with conflicting telemetry data, the flight controller was at his wits' end.",
                "incorrect": "Faced with conflicting telemetry data, the flight controller was at his wits' end and had no brain left."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Altering the fixed noun form (e.g. writing 'burn the midnight oils').",
                "correction": "Burn the midnight oil (uncountable singular noun).",
                "rationale": "Idioms preserve archaic or fixed nominal morphology that rejects modern pluralization."
            },
            {
                "mistake": "Selecting literal options on standardized exam papers.",
                "correction": "Reject any option that describes physical cats, beans, stones, or dogs literally.",
                "rationale": "Idioms are metaphorical by definition; literal interpretations are 100% incorrect on exam papers."
            },
            {
                "mistake": "Confusing 'A blessing in disguise' with unrelated fortuitous phrases.",
                "correction": "A blessing in disguise means an apparent misfortune that eventually produces fortunate results.",
                "rationale": "Candidates miss the initial negative aspect necessary to make it a 'disguise'."
            },
            {
                "mistake": "Misunderstanding 'Pyrrhic Victory'.",
                "correction": "A victory won at too high a cost, leaving the victor crippled.",
                "rationale": "Candidates frequently select 'an easy or glorious victory' due to unfamiliarity with King Pyrrhus of Epirus."
            }
        ],
        "quick_revision_points": [
            "Achilles' heel = a single fatal weakness or vulnerability.",
            "Pyrrhic victory = a victory won at ruinous and devastating cost.",
            "At daggers drawn = bitterly hostile towards one another.",
            "Bite the bullet = endure a painful or unavoidable situation bravely.",
            "By the skin of one's teeth = narrowly or barely escaping disaster.",
            "Burn the midnight oil = study or work hard late into the night.",
            "A white elephant = a costly, burdensome possession that yields no profit.",
            "At the eleventh hour = at the very last moment, just before the deadline."
        ]
    },
    "practice_questions": [
        {
            "id": 2001,
            "topic_id": 20,
            "question_text": "Select the most appropriate meaning of the given idiom: 'At the eleventh hour'",
            "question_type": "mcq",
            "options": [
                "At eleven o'clock sharp in the night",
                "At the very last moment before a deadline",
                "Early in the morning during business hours",
                "After the deadline has completely passed"
            ],
            "correct_answer": "At the very last moment before a deadline",
            "explanation": "'At the eleventh hour' means at the last possible moment, just before it is too late to act.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2002,
            "topic_id": 20,
            "question_text": "What does the idiom 'A PYRRHIC VICTORY' mean in competitive exam vocabulary?",
            "question_type": "mcq",
            "options": [
                "A glorious and effortless triumph",
                "A victory achieved through dishonest deception",
                "A victory won at such devastating cost that it is tantamount to defeat",
                "A triumph celebrated across an entire nation"
            ],
            "correct_answer": "A victory won at such devastating cost that it is tantamount to defeat",
            "explanation": "A 'Pyrrhic victory' is a triumph gained at such devastating cost that the victor is left crippled (derived from King Pyrrhus who defeated the Romans at Heraclea with catastrophic losses).",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 2003,
            "topic_id": 20,
            "question_text": "Select the meaning of the idiom: 'To bite the bullet'",
            "question_type": "mcq",
            "options": [
                "To surrender arms on the battlefield",
                "To endure a painful or grim situation with fortitude",
                "To engage in reckless physical combat",
                "To act hastily without prior planning"
            ],
            "correct_answer": "To endure a painful or grim situation with fortitude",
            "explanation": "'To bite the bullet' means to face a grim, unpleasant, or painful situation with bravery and stoicism.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2004,
            "topic_id": 20,
            "question_text": "In the sentence: 'The luxurious marble palace proved to be a WHITE ELEPHANT for the impoverished estate', what does 'WHITE ELEPHANT' signify?",
            "question_type": "mcq",
            "options": [
                "A sacred religious animal",
                "A rare and priceless antique treasure",
                "A burdensome possession that is extremely costly to maintain without generating utility",
                "A modern architectural masterpiece"
            ],
            "correct_answer": "A burdensome possession that is extremely costly to maintain without generating utility",
            "explanation": "A 'white elephant' is a possession that is useless or troublesome, especially one that is expensive to maintain or difficult to dispose of.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2005,
            "topic_id": 20,
            "question_text": "Select the idiom that correctly completes the sentence: 'After three months of fierce litigation, the two business partners were __________ and refused to sit in the same boardroom.'",
            "question_type": "mcq",
            "options": ["at daggers drawn", "on cloud nine", "in the pink", "of one mind"],
            "correct_answer": "at daggers drawn",
            "explanation": "'At daggers drawn' means in a state of open and bitter hostility. 'On cloud nine' means ecstatic; 'in the pink' means in good health.",
            "difficulty": "medium",
            "points": 1
        },
        {
            "id": 2006,
            "topic_id": 20,
            "question_text": "What is the meaning of the idiom: 'By the skin of one's teeth'?",
            "question_type": "mcq",
            "options": [
                "With utmost dental hygiene",
                "By a very narrow margin; barely",
                "Through forceful and violent means",
                "With complete confidence and ease"
            ],
            "correct_answer": "By a very narrow margin; barely",
            "explanation": "'By the skin of one's teeth' means barely, by the narrowest of margins, or just managing to avoid disaster.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2007,
            "topic_id": 20,
            "question_text": "Fill in the blank with the appropriate idiom: 'He spent the entire weekend searching through archives for a non-existent treaty, realizing only on Monday that his supervisor had sent him on a __________.'",
            "question_type": "fitb",
            "options": ["wild goose chase", "feather in his cap", "bolt from the blue", "bed of roses"],
            "correct_answer": "wild goose chase",
            "explanation": "A 'wild goose chase' is a foolish, fruitless, and hopeless search or endeavor.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2008,
            "topic_id": 20,
            "question_text": "Select the meaning of 'ACHILLES' HEEL':",
            "question_type": "mcq",
            "options": [
                "A soldier's footwear",
                "A weakness or vulnerable point in an otherwise strong situation",
                "A swift runner who wins marathon races",
                "A classical musical composition"
            ],
            "correct_answer": "A weakness or vulnerable point in an otherwise strong situation",
            "explanation": "'Achilles' heel' refers to a vulnerable spot or weakness in an otherwise invulnerable person or system (originating from the Greek myth of Achilles).",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2009,
            "topic_id": 20,
            "question_text": "What does the expression 'TO BURN THE MIDNIGHT OIL' mean?",
            "question_type": "mcq",
            "options": [
                "To waste fuel carelessly",
                "To work or study late into the night",
                "To set an oil lamp on fire in an emergency",
                "To engage in nocturnal espionage"
            ],
            "correct_answer": "To work or study late into the night",
            "explanation": "'To burn the midnight oil' means to work, read, or study late into the night.",
            "difficulty": "easy",
            "points": 1
        },
        {
            "id": 2010,
            "topic_id": 20,
            "question_text": "Select the correct sentence using the idiom 'BLESSING IN DISGUISE':",
            "question_type": "mcq",
            "options": [
                "Losing his corporate job forced him to establish his own startup, which proved to be a blessing in disguise.",
                "Winning the multimillion lottery jackpot on his birthday was a blessing in disguise.",
                "The sudden earthquake destroyed the entire neighborhood, proving to be a blessing in disguise.",
                "His high fever and illness during the final exam was a blessing in disguise because he failed."
            ],
            "correct_answer": "Losing his corporate job forced him to establish his own startup, which proved to be a blessing in disguise.",
            "explanation": "A 'blessing in disguise' refers to an apparent misfortune or problem that ultimately produces an unexpected positive benefit or advantage.",
            "difficulty": "medium",
            "points": 1
        }
    ]
}

data = {
    16: topic_16,
    17: topic_17,
    18: topic_18,
    19: topic_19,
    20: topic_20
}

with open("c:/Users/Ganesh/.antigravity-ide/skillexa/scratch/english_group_e.py", "w", encoding="utf-8") as f:
    f.write("# English Group E: Topics 16, 17, 18, 19, 20\n")
    f.write("# 16: Vocabulary, 17: Synonyms, 18: Antonyms, 19: One Word Substitution, 20: Idioms and Phrases\n\n")
    f.write("GROUP_E_DATA = ")
    f.write(json.dumps(data, indent=4))
    f.write("\n")

print("Created english_group_e.py successfully with topics 16-20!")
