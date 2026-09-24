import json
import os
import subprocess

db_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'data', 'skillexa.json')
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

# 1. Structured Rich Lesson Content for Topic 2: Pronoun
pronoun_lesson_content = {
    "definition": "A pronoun is a grammatical word used in place of a noun or noun phrase to prevent awkward, monotonous repetition and to establish clear syntactic cohesion in sentences. The noun replaced by a pronoun is known as its 'antecedent'. In competitive examinations (SSC, CDS, Bank PO), questions test Pronoun-Antecedent Agreement in person, number, and gender, as well as strict grammatical case distinctions (Subjective, Objective, and Possessive).",
    "overview": "Mastering pronouns requires understanding the three grammatical cases (Subjective/Nominative, Objective/Accusative, and Possessive), navigating relative clauses (who vs. whom vs. that), applying the polite 2-3-1 order of personal pronouns, and avoiding the misuse of reflexive pronouns as sentence subjects.",
    "types": [
        {
            "name": "1. Personal Pronouns",
            "desc": "Represent specific persons or entities across three persons: 1st person (speaker), 2nd person (listener), and 3rd person (spoken of).",
            "examples": [
                "Subjective (Nominative): I, we, you, he, she, it, they (act as the grammatical subject performing the verb)",
                "Objective (Accusative): me, us, you, him, her, it, them (act as the direct/indirect object or prepositional complement)",
                "Example: 'He called her yesterday' vs. 'She called him yesterday'"
            ]
        },
        {
            "name": "2. Possessive Pronouns",
            "desc": "Indicate ownership or association without taking an accompanying noun (distinct from possessive adjectives like my, your, our).",
            "examples": [
                "Possessive Pronouns: mine, ours, yours, his, hers, theirs (stand alone as subjects or objects: 'This car is mine', 'Yours is parked outside')",
                "Contrast with Possessive Adjectives: 'This is my car' ('my' modifies noun 'car')",
                "Rule: Never write possessive pronouns with an apostrophe (write 'hers', 'ours', 'yours', 'theirs', never 'her's' or 'your's')"
            ]
        },
        {
            "name": "3. Reflexive & Emphatic Pronouns",
            "desc": "Formed by adding '-self' (singular) or '-selves' (plural): myself, yourself, himself, herself, itself, ourselves, yourselves, themselves.",
            "examples": [
                "Reflexive: Used when subject and object are the identical person/thing ('He hurt himself while training')",
                "Emphatic: Used immediately following a noun/pronoun for rhetorical emphasis ('I myself supervised the operation')",
                "Golden Rule: A reflexive pronoun can NEVER function as a sentence subject on its own"
            ]
        },
        {
            "name": "4. Relative Pronouns",
            "desc": "Join clauses and refer back to an immediately preceding antecedent noun.",
            "examples": [
                "Who: Subjective case for human beings ('The officer who led the patrol received a medal')",
                "Whom: Objective case for human beings ('The candidate whom the committee interviewed was selected')",
                "Whose: Possessive case for persons/entities ('The author whose novel won the Booker Prize')",
                "Which: For inanimate objects, animals, or non-restrictive information ('The report, which arrived late, was verified')",
                "That: For restrictive clauses and after superlatives, all, none, only, the same ('All that glitters is not gold')"
            ]
        },
        {
            "name": "5. Indefinite Pronouns",
            "desc": "Refer to non-specific persons, objects, or quantities.",
            "examples": [
                "Singular Indefinite: everyone, everybody, someone, somebody, anyone, anybody, no one, nobody, each, either, neither, one",
                "Plural Indefinite: both, few, many, several",
                "Singular or Plural (SANAM rule): some, any, none, all, more/most (depend on the noun in the prepositional phrase)"
            ]
        },
        {
            "name": "6. Distributive & Reciprocal Pronouns",
            "desc": "Refer to individuals taken one at a time (Distributive) or express mutual two-way actions (Reciprocal).",
            "examples": [
                "Distributive: Each, Either (one of two), Neither (none of two) - always singular in formal grammar ('Each of the participants was awarded a certificate')",
                "Reciprocal - 'Each other': Strictly between TWO persons or entities ('The two diplomats shook hands with each other')",
                "Reciprocal - 'One another': Strictly for MORE THAN TWO entities ('The five team members supported one another')"
            ]
        }
    ],
    "rules": [
        {
            "rule_number": 1,
            "title": "Order of Personal Pronouns (The 2-3-1 vs. 1-2-3 Rule)",
            "explanation": "When pronouns of different persons are compounded in a single sentence in ordinary positive contexts, courteous English grammar demands the 2-3-1 order (Second Person -> Third Person -> First Person). In confessions of guilt, mistakes, or when all pronouns are plural, use the 1-2-3 order (First Person -> Second Person -> Third Person).",
            "words": ["2-3-1 Rule", "1-2-3 Rule", "Polite Order", "Confession Order"],
            "correct": "You, he and I will present the budget analysis to the board.",
            "incorrect": "I, you and he will present the budget analysis to the board."
        },
        {
            "rule_number": 2,
            "title": "Compound Subject Case: 'Rahul and I' vs. 'Rahul and me'",
            "explanation": "When a personal pronoun is paired with a proper noun as the subject of a verb, it MUST be in the subjective case (I, he, she, we, they). A foolproof test: mentally remove the companion noun and read the sentence; if 'I' fits, the compound requires 'I'.",
            "words": ["Subjective Case", "Nominative", "Compound Subject"],
            "correct": "Rahul and I went to the central library to consult the archives.",
            "incorrect": "Rahul and me went to the central library to consult the archives."
        },
        {
            "rule_number": 3,
            "title": "Objective Case after Prepositions and 'Between... And'",
            "explanation": "Any pronoun that functions as the object of a preposition (between, except, but, like, with, for, to) MUST appear in the objective case (me, him, her, us, them). In competitive exams, 'between you and I' is one of the most frequently tested errors.",
            "words": ["Between", "Except", "Objective Case", "Prepositional Object"],
            "correct": "There is complete mutual understanding between you and me.",
            "incorrect": "There is complete mutual understanding between you and I."
        },
        {
            "rule_number": 4,
            "title": "Case of Pronouns in Comparisons with 'Than' and 'As'",
            "explanation": "When comparing two subjects linked by 'than' or 'as', the pronoun following the conjunction must be in the subjective case because the verb is grammatically implied/ellipted. Use objective case only when comparing two direct objects.",
            "words": ["Than", "As", "Ellipsis", "Comparative Case"],
            "correct": "He is more experienced in financial auditing than she (is).",
            "incorrect": "He is more experienced in financial auditing than her."
        },
        {
            "rule_number": 5,
            "title": "Strict Consistency of the Indefinite Pronoun 'One'",
            "explanation": "When the pronoun 'one' is used in the sense of 'any person in general', its possessive case must strictly be 'one's' and its reflexive case must be 'oneself'. It must NEVER be switched to 'his', 'her', or 'their'.",
            "words": ["One", "One's", "Oneself", "Antecedent Consistency"],
            "correct": "One must faithfully perform one's civic duties toward society.",
            "incorrect": "One must faithfully perform his civic duties toward society."
        },
        {
            "rule_number": 6,
            "title": "Mandatory Use of Relative Pronoun 'That' over 'Who/Which'",
            "explanation": "The relative pronoun 'that' (rather than 'who' or 'which') must be used after superlative adjectives (the tallest, the best) and after limiting determiners: all, only, the same, none, nothing, any, little, few, or when the antecedent combines a human with an animal/thing.",
            "words": ["That", "Superlative", "All", "Only", "None", "The Same"],
            "correct": "This is the best research paper that has been published this decade.",
            "incorrect": "This is the best research paper which has been published this decade."
        }
    ],
    "common_mistakes": [
        {
            "mistake": "Using reflexive pronouns as independent grammatical subjects (e.g., 'Myself Dr. Verma and I am the lead investigator')",
            "correction": "Use personal subjective pronouns: 'I am Dr. Verma, and I am the lead investigator.'",
            "rationale": "Reflexive pronouns (-self) cannot initiate a clause or serve as grammatical subjects without a primary noun or subjective pronoun antecedent."
        },
        {
            "mistake": "Saying 'Between you and I, this project lacks funding'",
            "correction": "Say 'Between you and me, this project lacks funding.'",
            "rationale": "'Between' is a preposition; prepositions always govern the objective case ('me', never 'I')."
        },
        {
            "mistake": "Confusing 'Each other' with 'One another' (e.g., 'The two political rivals attacked one another on television')",
            "correction": "Use 'each other' for two parties: 'The two political rivals attacked each other on television.'",
            "rationale": "In formal competitive English grammar, 'each other' is reserved strictly for two entities; 'one another' is applied to three or more."
        },
        {
            "mistake": "Confusing possessive pronoun 'its' with the contraction 'it's'",
            "correction": "Use 'its' for possession ('The company doubled its profits') and 'it's' only as a contraction for 'it is' ('It's a rainy morning').",
            "rationale": "Pronouns never form possessives with apostrophes (hers, ours, yours, its, theirs)."
        }
    ],
    "quick_revision_points": [
        "Polite personal pronoun sequence in normal contexts is 2-3-1 (You, he and I); in negative/guilt contexts it is 1-2-3 (I, you and he).",
        "Compound subjects require subjective pronouns: 'Rahul and I went', NOT 'Rahul and me went'.",
        "Prepositions (between, except, but, like, for, to) always require objective pronouns: 'between you and me'.",
        "In comparisons with 'than' or 'as', compare subjects using subjective pronouns: 'He is taller than I (am)'.",
        "The indefinite pronoun 'one' takes 'one's' in the possessive, never 'his' or 'their'.",
        "'Each other' is used strictly for two entities; 'one another' is used for more than two.",
        "Reflexive pronouns (myself, himself) can NEVER serve as subjects on their own."
    ]
}

# 2. Update Lesson for Topic 2
lesson_found = False
for l in db.get('lessons', []):
    if l.get('topic_id') == 2:
        l['title'] = "Pronouns: Core Classifications, Syntactic Cases & Competitive Exam Rules"
        l['source_id'] = 1 # British Council
        l['status'] = "published"
        l['content_json'] = pronoun_lesson_content
        lesson_found = True
        print("Updated existing lesson for Topic 2.")
        break

if not lesson_found:
    max_lid = max([l['id'] for l in db['lessons']], default=0) + 1
    db['lessons'].append({
        "id": max_lid,
        "topic_id": 2,
        "title": "Pronouns: Core Classifications, Syntactic Cases & Competitive Exam Rules",
        "source_id": 1,
        "status": "published",
        "content_json": pronoun_lesson_content
    })
    print("Created new lesson for Topic 2.")

# 3. Comprehensive 10 Practice Questions for Topic 2 (Pronoun)
practice_questions_topic_2 = [
    {
        "id": 201,
        "topic_id": 2,
        "question": "Identify the grammatically correct sentence adhering to the standard order of personal pronouns in a polite, positive context:",
        "options_json": [
            "You, he and I have been selected to represent the university.",
            "I, you and he have been selected to represent the university.",
            "He, you and I have been selected to represent the university.",
            "You, I and he have been selected to represent the university."
        ],
        "correct_answer": "You, he and I have been selected to represent the university.",
        "explanation": "In standard English grammar, multiple personal pronouns of different persons in an affirmative context follow the 2-3-1 sequence: Second Person (You) -> Third Person (He) -> First Person (I).",
        "difficulty": "Easy",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 202,
        "topic_id": 2,
        "question": "Spot the grammatical error in the following sentence:\n'Between you and I, the proposed merger between the two commercial banks lacks regulatory approval.'",
        "options_json": [
            "Between you and I",
            "the proposed merger",
            "between the two commercial banks",
            "lacks regulatory approval"
        ],
        "correct_answer": "Between you and I",
        "explanation": "'Between' is a preposition, and prepositions must be followed by objective case pronouns. Therefore, the correct phrase is 'Between you and me', not 'Between you and I'.",
        "difficulty": "Easy",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 203,
        "topic_id": 2,
        "question": "Select the correct option to fill in the blank:\n'Rahul and ______ walked to the podium to receive the joint research award.'",
        "options_json": ["I", "me", "myself", "mine"],
        "correct_answer": "I",
        "explanation": "The pronoun forms part of the compound subject of the verb 'walked'. Since subjects require the subjective/nominative case, 'I' is correct ('Rahul and I walked').",
        "difficulty": "Easy",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 204,
        "topic_id": 2,
        "question": "Complete the sentence with the correct possessive form:\n'One should always remain faithful to ______ national duties during times of crisis.'",
        "options_json": ["one's", "his", "their", "her"],
        "correct_answer": "one's",
        "explanation": "The indefinite pronoun 'one' requires consistent agreement with 'one's' in the possessive case throughout the sentence. Using 'his' or 'their' is a grammatical error.",
        "difficulty": "Medium",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 205,
        "topic_id": 2,
        "question": "Which sentence correctly applies the reciprocal pronoun rule for two entities?",
        "options_json": [
            "The two rival boxing champions respected each other deeply.",
            "The two rival boxing champions respected one another deeply.",
            "The two rival boxing champions respected themselves deeply.",
            "The two rival boxing champions respected each others deeply."
        ],
        "correct_answer": "The two rival boxing champions respected each other deeply.",
        "explanation": "'Each other' is strictly used when referring to two entities, whereas 'one another' is applied when more than two entities are involved.",
        "difficulty": "Medium",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 206,
        "topic_id": 2,
        "question": "Fill in the blank with the appropriate relative pronoun:\n'This is the best documentary on wildlife conservation ______ has ever been produced.'",
        "options_json": ["that", "which", "who", "whom"],
        "correct_answer": "that",
        "explanation": "When an antecedent is modified by a superlative adjective (here, 'the best'), the relative pronoun 'that' must be used instead of 'which'.",
        "difficulty": "Medium",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 207,
        "topic_id": 2,
        "question": "Choose the correct subjective comparison:\n'She has accumulated far more experience in corporate litigation than ______.'",
        "options_json": ["he", "him", "his", "himself"],
        "correct_answer": "he",
        "explanation": "In formal English, when two subjects are compared with 'than', the subjective case pronoun is required because the verb is implied: 'than he (has accumulated)'.",
        "difficulty": "Hard",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 208,
        "topic_id": 2,
        "question": "Why is the sentence 'Myself and my colleague prepared the financial forecast' grammatically incorrect?",
        "options_json": [
            "A reflexive pronoun like 'myself' cannot serve as a grammatical subject without a preceding personal pronoun.",
            "The verb 'prepared' requires an objective pronoun.",
            "'Colleague' must always precede the pronoun 'I'.",
            "The sentence is completely grammatically correct."
        ],
        "correct_answer": "A reflexive pronoun like 'myself' cannot serve as a grammatical subject without a preceding personal pronoun.",
        "explanation": "Reflexive pronouns cannot stand as grammatical subjects. The sentence should correctly read: 'My colleague and I prepared the financial forecast.'",
        "difficulty": "Easy",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "MCQ"
    },
    {
        "id": 209,
        "topic_id": 2,
        "question": "The reciprocal pronoun used when referring strictly to three or more people interacting is 'one ______'.",
        "correct_answer": "another",
        "explanation": "'One another' is used for more than two entities, while 'each other' is used for exactly two.",
        "difficulty": "Easy",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "FILL_IN_THE_BLANK"
    },
    {
        "id": 210,
        "topic_id": 2,
        "question": "In negative contexts or admissions of guilt, personal pronouns follow the order: first person, second person, then ______ person.",
        "correct_answer": "third",
        "explanation": "The 1-2-3 rule applies to confessions of error: First person (I), Second person (you), and Third person (he/she/they).",
        "difficulty": "Medium",
        "subject": "English",
        "topic": "Pronoun",
        "question_type": "FILL_IN_THE_BLANK"
    }
]

# Clean existing practice questions for topic 2 and replace with full set of 10
db['practice_questions'] = [pq for pq in db.get('practice_questions', []) if pq.get('topic_id') != 2]
db['practice_questions'].extend(practice_questions_topic_2)
print("Updated practice questions for Topic 2 to 10 comprehensive questions.")

# 4. Save to skillexa.json
with open(db_path, 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# 5. Sync to seedData.js
subprocess.run(["python", os.path.join(os.path.dirname(__file__), "sync_seed.py")], check=True)
print("Successfully populated Topic 2: Pronoun!")
