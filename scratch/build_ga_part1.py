# scratch/build_ga_part1.py
# Generates ga_part1.py for Topics 52 to 55:
# 52: Indian History
# 53: Geography
# 54: Indian Polity
# 55: Constitution

import json

topic_52 = {
    "title": "Indian History: Ancient Civilization, Medieval Dynasties & Modern Freedom Struggle",
    "source_id": 7,
    "content": {
        "definition": "Indian History in competitive examinations (UPSC, SSC CGL Tier 1/2, State PSCs, CDS, NDA, RRB) encompasses the comprehensive chronological evolution of the Indian subcontinent across Ancient, Medieval, and Modern eras. Key testing areas focus on Indus Valley Civilization urbanism, Vedic literature, Mauryan and Gupta administration, Delhi Sultanate and Mughal administrative systems, and the socio-religious and political trajectory of the Indian Freedom Struggle (1857 to 1947).",
        "overview": "Chronological Foundations of Indian History:\n- Ancient India: Indus Valley Civilization (c. 2500–1750 BCE; Harappa, Mohenjo-daro, Lothal dockyard); Vedic Period (Rigveda, Upanishads); Mahajanapadas and Buddhism/Jainism; Mauryan Empire (Chandragupta, Ashoka's Edicts, Arthashastra); Gupta Golden Age (Samudragupta, Chandragupta II, Kalidasa)\n- Medieval India: Delhi Sultanate (Slave, Khilji, Tughlaq, Sayyid, Lodi dynasties; Alauddin Khilji's market reforms); Mughal Empire (Babur, Akbar's Din-i-Ilahi and Mansabdari system, Shah Jahan, Aurangzeb); Vijayanagara Empire (Krishnadevaraya)\n- Modern India: Advent of Europeans (Battle of Plassey 1757, Buxar 1764); Revolt of 1857; Indian National Congress (1885); Partition of Bengal & Swadeshi Movement (1905); Gandhian Era (Non-Cooperation 1920, Civil Disobedience 1930, Quit India 1942); Independence & Partition (1947)",
        "types": [
            {
                "name": "1. Indus Valley Civilization & Vedic Age",
                "desc": "Bronze Age urban planning, grid street layouts, drainage architecture, and Vedic sacred texts.",
                "examples": [
                    "Lothal (Gujarat): World's earliest known tidal dockyard; Kalibangan: Ploughed field evidence",
                    "Four Vedas: Rigveda (hymns), Samaveda (music), Yajurveda (rituals), Atharvaveda (medicine/spells)"
                ]
            },
            {
                "name": "2. Mauryan & Gupta Classical Empires",
                "desc": "Imperial centralization, Ashokan rock edicts, administrative espionage, and classical Sanskrit literature.",
                "examples": [
                    "Kautilya's Arthashastra on statecraft; Megasthenes' Indica describing Pataliputra",
                    "Gupta Period: Aryabhata's astronomical treatises; Navaratnas of Chandragupta II Vikramaditya"
                ]
            },
            {
                "name": "3. Delhi Sultanate & Regional Kingdoms",
                "desc": "Turkish and Afghan rule (1206–1526 CE), Iqta administrative land assignments, and architectural monuments.",
                "examples": [
                    "Qutb Minar begun by Qutb-ud-din Aibak, completed by Iltutmish",
                    "Muhammad bin Tughlaq's token currency experiment and capital shift to Daulatabad"
                ]
            },
            {
                "name": "4. Mughal Empire & Mansabdari Administration",
                "desc": "Centralized imperial rule, revenue assessment (Zabt system of Todar Mal), and cultural synthesis.",
                "examples": [
                    "Akbar: Abolition of Jizya (1564), Ibadat Khana debates (1575), Sulh-i-Kul policy",
                    "Architecture: Taj Mahal and Red Fort by Shah Jahan; Buland Darwaza at Fatehpur Sikri"
                ]
            },
            {
                "name": "5. British Colonial Hegemony & Freedom Struggle",
                "desc": "Colonial revenue systems (Permanent Settlement, Ryotwari, Mahalwari) and national mass mobilizations.",
                "examples": [
                    "Doctrine of Lapse implemented by Lord Dalhousie (annexation of Satara, Jhansi, Nagpur)",
                    "Gandhian Satyagraha: Champaran (1917 Indigo), Kheda (1918), Dandi Salt March (1930)"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Governor-General vs Viceroy Chronology Rule",
                "explanation": "- **Governor of Bengal** (1757–1773): Robert Clive was first.\n- **Governor-General of Bengal** (Regulating Act 1773): Warren Hastings was first.\n- **Governor-General of India** (Charter Act 1833): Lord William Bentinck was first.\n- **Viceroy of India** (Government of India Act 1858): Lord Canning was first (and last Governor-General under EIC).\n- **First Governor-General of Independent India** (1947): Lord Mountbatten.\n- **First & Last Indian Governor-General** (1948–1950): C. Rajagopalachari.",
                "words": ["Hastings (1773)", "Bentinck (1833)", "Canning (1858)", "Rajagopalachari (1948)"],
                "correct": "First Governor-General of India was Lord William Bentinck (Charter Act 1833).",
                "incorrect": "Naming Warren Hastings as Governor-General of India (he was Governor-General of Bengal)."
            },
            {
                "rule_number": 2,
                "title": "Three Buddhist Councils Chronological Sequence",
                "explanation": "1. **1st Council (483 BCE)**: Rajgriha (Sattapanni Cave) — Patron: Ajatashatru (Haryanka) — Presided by Mahakassapa.\n2. **2nd Council (383 BCE)**: Vaishali — Patron: Kalashoka (Shishunaga) — Presided by Sabakami.\n3. **3rd Council (250 BCE)**: Pataliputra — Patron: Ashoka (Maurya) — Presided by Moggaliputta Tissa.\n4. **4th Council (72 CE)**: Kundalvana (Kashmir) — Patron: Kanishka (Kushan) — Presided by Vasumitra (division into Hinayana & Mahayana).",
                "words": ["Rajgriha -> Vaishali -> Pataliputra -> Kashmir", "Ajatashatru, Kalashoka, Ashoka, Kanishka"],
                "correct": "4th Buddhist Council was held in Kashmir under Kanishka, resulting in Hinayana/Mahayana division.",
                "incorrect": "Placing Ashoka at the 4th Buddhist Council."
            },
            {
                "rule_number": 3,
                "title": "Permanent Settlement vs Ryotwari Revenue Systems",
                "explanation": "- **Permanent Settlement (1793)**: Introduced by Lord Cornwallis in Bengal, Bihar, Orissa; Zamindars declared land owners with fixed 10/11th revenue share to British.\n- **Ryotwari System (1820)**: Introduced by Thomas Munro and Alexander Read in Madras and Bombay; direct settlement with peasant cultivators (Ryots).\n- **Mahalwari System (1822)**: Introduced by Holt Mackenzie in NWFP, Punjab, Central India; collective village community (Mahal) settlement.",
                "words": ["Cornwallis (Permanent/Zamindari)", "Munro (Ryotwari)", "Mackenzie (Mahalwari)"],
                "correct": "Ryotwari system settled tax directly with individual peasant cultivators in Madras and Bombay.",
                "incorrect": "Attributing Permanent Settlement to Lord Dalhousie."
            },
            {
                "rule_number": 4,
                "title": "INC Sessions and Landmark Presidents",
                "explanation": "- **First Session (1885)**: Bombay (Gokuldas Tejpal Sanskrit College) — W.C. Bonnerjee (72 delegates).\n- **First Muslim President**: Badruddin Tyabji (Madras, 1887).\n- **First British / Non-Indian President**: George Yule (Allahabad, 1888).\n- **First Woman President**: Annie Besant (Calcutta, 1917).\n- **First Indian Woman President**: Sarojini Naidu (Kanpur, 1925).\n- **Only Session Chaired by Mahatma Gandhi**: Belgaum Session (1924).\n- **Poorna Swaraj Resolution**: Lahore Session (1929) — Jawaharlal Nehru.",
                "words": ["Bonnerjee (1885)", "Besant (1917)", "Naidu (1925)", "Gandhi (Belgaum 1924)", "Nehru (Lahore 1929)"],
                "correct": "Sarojini Naidu was the first INDIAN woman president of INC (Kanpur, 1925); Annie Besant was the first woman overall (1917).",
                "incorrect": "Naming Sarojini Naidu as the first woman president of INC without specifying Indian."
            },
            {
                "rule_number": 5,
                "title": "Battle of Panipat Triad Dates",
                "explanation": "- **First Battle of Panipat (1526)**: Babur defeated Ibrahim Lodi (Founded Mughal Empire; first use of gunpowder field artillery and Tulghuma tactics in North India).\n- **Second Battle of Panipat (1556)**: Akbar's regent Bairam Khan defeated Hemu (Hemchandra Vikramaditya).\n- **Third Battle of Panipat (1761)**: Ahmad Shah Abdali (Durrani) defeated Marathas led by Sadashivrao Bhau.",
                "words": ["1526 (Babur-Lodi)", "1556 (Akbar-Hemu)", "1761 (Abdali-Maratha)"],
                "correct": "First Battle of Panipat (1526) ended the Delhi Sultanate and established the Mughal Dynasty.",
                "incorrect": "Confusing 2nd Panipat (1556) with Battle of Haldighati (1576, Maharana Pratap vs Man Singh)."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Confusing the first woman president of INC with the first Indian woman president.",
                "correction": "Annie Besant (British) was the first woman in 1917; Sarojini Naidu was the first Indian woman in 1925.",
                "rationale": "High-frequency trap in SSC CGL and State PCS examinations."
            },
            {
                "mistake": "Believing Mahatma Gandhi was president of INC multiple times.",
                "correction": "Mahatma Gandhi served as INC President only ONCE: at the Belgaum Session in 1924.",
                "rationale": "Exam boards frequently test this singular historical anomaly."
            },
            {
                "mistake": "Confusing the Treaty of Purandar (1665) with Treaty of Bassein (1802) or Salbai (1782).",
                "correction": "Treaty of Purandar (1665) was signed between Chhatrapati Shivaji Maharaj and Jai Singh I (on behalf of Aurangzeb).",
                "rationale": "Crucial landmark in Maratha-Mughal relations."
            },
            {
                "mistake": "Equating the Morley-Minto Reforms (1909) with Montagu-Chelmsford Reforms (1919).",
                "correction": "Morley-Minto (1909) introduced communal electorates for Muslims; Montagu-Chelmsford (1919) introduced provincial Dyarchy.",
                "rationale": "Core constitutional history distinction in UPSC and SSC exams."
            }
        ],
        "quick_revision_points": [
            "Indus Valley: Lothal (Dockyard), Harappa (Granary), Mohenjo-daro (Great Bath), Kalibangan (Ploughed field)",
            "Ashoka's Kalinga War occurred in 261 BCE (Rock Edict XIII describes his remorse and conversion to Dhamma)",
            "Gupta rulers: Chandragupta I (Gupta Era 319 CE), Samudragupta ('Napoleon of India' by V.A. Smith), Chandragupta II (Vikramaditya)",
            "Ibn Battuta visited India during Muhammad bin Tughlaq's reign (wrote 'Rihla')",
            "Akbar: Mansabdari system, Ibadat Khana (1575), Navaratnas (Birbal, Tansen, Todar Mal, Abul Fazl, Faizi, Man Singh, etc.)",
            "1857 Revolt: Started at Meerut on May 10, 1857; Bahadur Shah Zafar declared Emperor of Hindustan",
            "Gandhi's Movements: Non-Cooperation (1920-22, called off after Chauri Chaura), Civil Disobedience (1930, Dandi March), Quit India (1942)",
            "Cabinet Mission Plan (1946) recommended the formation of the Constituent Assembly"
        ]
    },
    "previous_year_questions": [
        {
            "id": 5201,
            "topic_id": 52,
            "exam_id": 1,
            "question": "At which Indian National Congress session was the historic 'Poorna Swaraj' (Complete Independence) resolution passed? [SSC CGL 2023 Tier 1]",
            "options_json": ["Lahore Session (1929)", "Karachi Session (1931)", "Calcutta Session (1928)", "Madras Session (1927)"],
            "correct_answer": "Lahore Session (1929)",
            "explanation": "At the historic Lahore Session of the Indian National Congress in December 1929, under the presidency of Jawaharlal Nehru, the 'Poorna Swaraj' (Complete Independence) resolution was adopted. It declared 26 January 1930 as Independence Day.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5202,
            "topic_id": 52,
            "exam_id": 1,
            "question": "Which Indus Valley Civilization site has yielded evidence of a tidal dockyard? [UPSC CDS 2022]",
            "options_json": ["Lothal", "Kalibangan", "Dholavira", "Banawali"],
            "correct_answer": "Lothal",
            "explanation": "Lothal, situated along the Bhogava river in Gujarat, was an important port city of the Indus Valley Civilization featuring a massive brick basin identified as the world's earliest known tidal dockyard.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5203,
            "topic_id": 52,
            "exam_id": 1,
            "question": "Who was the only Indian to serve as the Governor-General of Independent India? [RRB NTPC 2022]",
            "options_json": ["C. Rajagopalachari", "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Jawaharlal Nehru"],
            "correct_answer": "C. Rajagopalachari",
            "explanation": "Chakravarti Rajagopalachari served as the Governor-General of India from June 1948 until the proclamation of the Indian Republic on 26 January 1950. He was the first and only Indian national to hold the post.",
            "source_id": 7,
            "status": "published"
        }
    ],
    "practice_questions": [
        {
            "id": 5201,
            "topic_id": 52,
            "question": "Who founded the Maurya Empire after defeating Dhana Nanda?",
            "options_json": ["Chandragupta Maurya", "Ashoka", "Bindusara", "Kanishka"],
            "correct_answer": "Chandragupta Maurya",
            "explanation": "Chandragupta Maurya, assisted by his mentor Chanakya (Kautilya), overthrew the Nanda dynasty in 322 BCE to establish the Maurya Empire.",
            "points": 1
        },
        {
            "id": 5202,
            "topic_id": 52,
            "question": "In which year was the Battle of Plassey fought?",
            "options_json": ["1757", "1764", "1857", "1761"],
            "correct_answer": "1757",
            "explanation": "The Battle of Plassey was fought on 23 June 1757 between the British East India Company led by Robert Clive and Nawab Siraj-ud-Daulah of Bengal.",
            "points": 1
        },
        {
            "id": 5203,
            "topic_id": 52,
            "question": "Who was the founder of the Slave (Mamluk) Dynasty in Delhi?",
            "options_json": ["Qutb-ud-din Aibak", "Iltutmish", "Balban", "Razia Sultan"],
            "correct_answer": "Qutb-ud-din Aibak",
            "explanation": "Qutb-ud-din Aibak, a general of Muhammad Ghori, founded the Slave Dynasty in 1206 CE.",
            "points": 1
        },
        {
            "id": 5204,
            "topic_id": 52,
            "question": "Which Mughal Emperor abolished the Jizya tax on non-Muslims in 1564?",
            "options_json": ["Akbar", "Babur", "Humayun", "Jahangir"],
            "correct_answer": "Akbar",
            "explanation": "Akbar abolished the pilgrim tax and Jizya tax in 1564 as part of his policy of religious tolerance (Sulh-i-Kul).",
            "points": 1
        },
        {
            "id": 5205,
            "topic_id": 52,
            "question": "Who presided over the first session of the Indian National Congress in 1885?",
            "options_json": ["W.C. Bonnerjee", "Dadabhai Naoroji", "A.O. Hume", "Surendranath Banerjee"],
            "correct_answer": "W.C. Bonnerjee",
            "explanation": "Womesh Chandra Bonnerjee was the President of the 1st INC session held at Bombay in December 1885 with 72 delegates.",
            "points": 1
        },
        {
            "id": 5206,
            "topic_id": 52,
            "question": "The Chauri Chaura incident led Mahatma Gandhi to call off which movement?",
            "options_json": ["Non-Cooperation Movement", "Civil Disobedience Movement", "Quit India Movement", "Rowlatt Satyagraha"],
            "correct_answer": "Non-Cooperation Movement",
            "explanation": "Following the violent incident at Chauri Chaura (Gorakhpur, UP) on 4 February 1922, Mahatma Gandhi called off the Non-Cooperation Movement.",
            "points": 1
        },
        {
            "id": 5207,
            "topic_id": 52,
            "question": "Who was called the 'Napoleon of India' by historian V.A. Smith?",
            "options_json": ["Samudragupta", "Chandragupta II", "Harshavardhana", "Skandagupta"],
            "correct_answer": "Samudragupta",
            "explanation": "Samudragupta of the Gupta Empire was called the 'Napoleon of India' due to his extensive military conquests recorded on the Prayag Prashasti (Allahabad Pillar inscription) by Harisena.",
            "points": 1
        },
        {
            "id": 5208,
            "topic_id": 52,
            "question": "The Permanent Settlement was introduced in Bengal by which Governor-General in 1793?",
            "options_json": ["Lord Cornwallis", "Lord Wellesley", "Warren Hastings", "Lord Dalhousie"],
            "correct_answer": "Lord Cornwallis",
            "explanation": "Lord Cornwallis introduced the Permanent Settlement (Zamindari system) in Bengal, Bihar, and Orissa in 1793.",
            "points": 1
        },
        {
            "id": 5209,
            "topic_id": 52,
            "question": "Who was the court physician of Kanishka famous for his medical treatise?",
            "options_json": ["Charaka", "Sushruta", "Dhanvantari", "Vagbhata"],
            "correct_answer": "Charaka",
            "explanation": "Charaka, the author of the foundational Ayurvedic treatise 'Charaka Samhita', was the court physician of the Kushan King Kanishka.",
            "points": 1
        },
        {
            "id": 5210,
            "topic_id": 52,
            "question": "In which INC session was Mahatma Gandhi elected President for the only time?",
            "options_json": ["Belgaum Session (1924)", "Calcutta Session (1920)", "Lahore Session (1929)", "Haripura Session (1938)"],
            "correct_answer": "Belgaum Session (1924)",
            "explanation": "Mahatma Gandhi presided over the Indian National Congress session only once, at the 39th session held in Belgaum (Karnataka) in 1924.",
            "points": 1
        }
    ],
    "quiz_questions": [
        {
            "id": 5201,
            "topic_id": 52,
            "question": "In which year did the First Battle of Panipat take place?",
            "options_json": ["1526", "1556", "1761", "1576"],
            "correct_answer": "1526",
            "explanation": "The First Battle of Panipat was fought on 21 April 1526 between Babur and Ibrahim Lodi, establishing the Mughal Empire in India.",
            "points": 1
        },
        {
            "id": 5202,
            "topic_id": 52,
            "question": "Who was the first woman President of the Indian National Congress?",
            "options_json": ["Annie Besant", "Sarojini Naidu", "Nellie Sengupta", "Indira Gandhi"],
            "correct_answer": "Annie Besant",
            "explanation": "Annie Besant presided over the Calcutta session of the INC in 1917, becoming its first woman president. (Sarojini Naidu was the first Indian woman president in 1925).",
            "points": 1
        },
        {
            "id": 5203,
            "topic_id": 52,
            "question": "The famous rock-cut Kailash temple at Ellora was built by which dynasty?",
            "options_json": ["Rashtrakutas", "Cholas", "Pallavas", "Chalukyas"],
            "correct_answer": "Rashtrakutas",
            "explanation": "The monolithic Kailash Temple (Cave 16) at Ellora was carved out of a single rock cliff during the reign of Rashtrakuta King Krishna I (8th century CE).",
            "points": 1
        },
        {
            "id": 5204,
            "topic_id": 52,
            "question": "Which Governor-General implemented the controversial 'Doctrine of Lapse'?",
            "options_json": ["Lord Dalhousie", "Lord Curzon", "Lord Canning", "Lord Wellesley"],
            "correct_answer": "Lord Dalhousie",
            "explanation": "Lord Dalhousie (1848–1856) used the Doctrine of Lapse to annex Indian princely states without natural male heirs (e.g. Satara, Sambalpur, Jhansi, Nagpur).",
            "points": 1
        },
        {
            "id": 5205,
            "topic_id": 52,
            "question": "Who was known as 'Lakh Baksh' (Giver of Lakhs) for his generosity?",
            "options_json": ["Qutb-ud-din Aibak", "Iltutmish", "Balban", "Alauddin Khilji"],
            "correct_answer": "Qutb-ud-din Aibak",
            "explanation": "Qutb-ud-din Aibak, the founder of the Delhi Sultanate, was conferred the title 'Lakh Baksh' due to his large donations and charitable munificence.",
            "points": 1
        },
        {
            "id": 5206,
            "topic_id": 52,
            "question": "The Great Bath was discovered in which archaeological excavation of the Indus Valley?",
            "options_json": ["Mohenjo-daro", "Harappa", "Kalibangan", "Rakhigarhi"],
            "correct_answer": "Mohenjo-daro",
            "explanation": "The Great Bath, an elaborate watertight public bathing reservoir lined with bitumen, was excavated at Mohenjo-daro in Sindh (now Pakistan).",
            "points": 1
        },
        {
            "id": 5207,
            "topic_id": 52,
            "question": "In which year did the Partition of Bengal take place under Lord Curzon?",
            "options_json": ["1905", "1911", "1906", "1919"],
            "correct_answer": "1905",
            "explanation": "The Partition of Bengal was announced by Viceroy Lord Curzon on 16 October 1905, triggering the nationwide Swadeshi and Boycott Movement.",
            "points": 1
        },
        {
            "id": 5208,
            "topic_id": 52,
            "question": "Who was the court poet of Harsha who wrote 'Harshacharita' and 'Kadambari'?",
            "options_json": ["Banabhatta", "Kalidasa", "Harisena", "Bhaviabhuti"],
            "correct_answer": "Banabhatta",
            "explanation": "Banabhatta was the Asthana Kavi in the court of King Harshavardhana of Kannauj and composed the biographical Sanskrit classic 'Harshacharita'.",
            "points": 1
        },
        {
            "id": 5209,
            "topic_id": 52,
            "question": "Who founded the Arya Samaj in Bombay in 1875?",
            "options_json": ["Swami Dayanand Saraswati", "Swami Vivekananda", "Raja Ram Mohan Roy", "Ishwar Chandra Vidyasagar"],
            "correct_answer": "Swami Dayanand Saraswati",
            "explanation": "Swami Dayanand Saraswati founded the Arya Samaj in 1875 with the slogan 'Back to the Vedas' and authored the treatise 'Satyarth Prakash'.",
            "points": 1
        },
        {
            "id": 5210,
            "topic_id": 52,
            "question": "The Gandhi-Irwin Pact was signed in which year prior to the Second Round Table Conference?",
            "options_json": ["1931", "1930", "1932", "1929"],
            "correct_answer": "1931",
            "explanation": "The Gandhi-Irwin Pact was signed on 5 March 1931, leading to the suspension of the Civil Disobedience Movement and Congress participation in the 2nd Round Table Conference.",
            "points": 1
        }
    ]
}

topic_53 = {
    "title": "Geography: Physical Landscapes, River Basins, Monsoon Climate & World Superlatives",
    "source_id": 7,
    "content": {
        "definition": "Geography in competitive aptitude examinations evaluates physical topography, drainage basins, atmospheric circulation and climatic patterns, pedology (soil classifications), and economic resource distribution across India and the globe. Core exam patterns (SSC CGL Tier 1/2, UPSC CDS/NDA, State PSCs, RRB NTPC) focus on Himalayan geological divisions, peninsular drainage divides, Indian monsoon dynamics (South-West and North-East retreats), and world physical geography superlatives.",
        "overview": "Fundamental Geographical Systems:\n- Physiographic Divisions of India: The Northern Mountains (Trans-Himalayas, Greater Himalayas/Himadri, Lesser Himalayas/Himachal, Outer Himalayas/Shiwaliks); Northern Plains (Bhabhar, Terai, Bhangar, Khadar); Peninsular Plateau (Malwa, Deccan, Chota Nagpur); Coastal Plains & Islands (Lakshadweep coral atolls, Andaman & Nicobar volcanic islands)\n- Drainage Systems: Himalayan Rivers (Perennial, antecedent drainage: Indus, Ganga, Brahmaputra); Peninsular Rivers (Epitome of graded profiles: West-flowing Narmada and Tapi in rift valleys; East-flowing Godavari, Krishna, Cauvery, Mahanadi)\n- Climate & Monsoon: Thermal contrast theory, ITCZ shift, Somali Jet Stream, El Nino/La Nina impacts; South-West Monsoon (Arabian Sea and Bay of Bengal branches); North-East Winter Retreating Monsoon (Tamil Nadu coast rainfall)\n- Soils of India (ICAR): Alluvial soil (most fertile, 40% area), Black soil (Regur, cotton soil of Deccan trap, self-ploughing), Red & Yellow soil, Laterite soil (leached, cashew/tea/coffee)",
        "types": [
            {
                "name": "1. Himalayan Geomorphology & Mountain Passes",
                "desc": "Parallel longitudinal ranges, tectonic syntaxial bends, and high-altitude strategic passes.",
                "examples": [
                    "Zojila Pass (Ladakh to Srinagar), Shipki La (Himachal to Tibet), Nathu La (Sikkim to Tibet)",
                    "Highest peak in India: Kanchenjunga (8,586 m in Sikkim; K2/Godwin-Austen is in PoK)"
                ]
            },
            {
                "name": "2. River Drainage Systems & Tributaries",
                "desc": "Dendritic, trellis, and radial river systems, origins, and major multipurpose river valley projects.",
                "examples": [
                    "Godavari: Longest peninsular river ('Dakshin Ganga'), originates at Trimbakeshwar (Nashik)",
                    "Narmada & Tapi: West-flowing rivers that flow through tectonic rift valleys and do NOT form deltas (form estuaries)"
                ]
            },
            {
                "name": "3. Climatology & Indian Monsoon Dynamics",
                "desc": "Inter-Tropical Convergence Zone (ITCZ) migration, Jet Streams, and rainfall distribution.",
                "examples": [
                    "Mawsynram (Khasi Hills, Meghalaya): Wettest place on Earth (funneling effect of topography)",
                    "Retreating Monsoon (Oct-Nov) brings bulk of annual precipitation to Coromandel Coast (Tamil Nadu)"
                ]
            },
            {
                "name": "4. Pedology & Major Soil Classifications (ICAR)",
                "desc": "Soil horizons, parent rock weathering, and crop associations.",
                "examples": [
                    "Black / Regur Soil: Formed by weathering of basaltic lava; high water retention; ideal for cotton",
                    "Laterite Soil: Formed under conditions of intense leaching due to heavy rainfall and high temperature"
                ]
            },
            {
                "name": "5. World Physical Geography Superlatives",
                "desc": "Continents, oceans, straits, ocean currents, and astronomical planetary constants.",
                "examples": [
                    "Strait of Malacca (links Andaman Sea & South China Sea); Strait of Gibraltar (Mediterranean & Atlantic)",
                    "Mariana Trench (Challenger Deep, ~11,034 m): Deepest oceanic trench on Earth in the Pacific Ocean"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "West-Flowing Peninsular Rivers (Rift Valley Estuaries)",
                "explanation": "Most major peninsular rivers flow East into the Bay of Bengal and form extensive deltas (Godavari, Krishna, Cauvery, Mahanadi). However:\n- **Narmada** (originates at Amarkantak) and **Tapi** (originates at Multai) flow **WEST** into the Arabian Sea through structural fault/rift valleys between the Vindhya and Satpura ranges.\n- Because of high velocity and rocky terrain, they form **ESTUARIES**, NOT deltas!",
                "words": ["Narmada & Tapi", "Rift Valley", "Flow West into Arabian Sea", "Estuaries, No Deltas"],
                "correct": "Narmada and Tapi flow westwards through rift valleys and empty into the Arabian Sea via estuaries.",
                "incorrect": "Stating that Narmada forms a fertile delta in the Bay of Bengal."
            },
            {
                "rule_number": 2,
                "title": "Bhabhar vs Terai vs Bhangar vs Khadar Soil Zones",
                "explanation": "From the Shiwalik foothills to the Indo-Gangetic floodplains, four distinct morphological zones emerge:\n1. **Bhabhar**: Narrow 8-10 km pebble/boulder belt along foothills where streams submerge and disappear underground.\n2. **Terai**: Marshy, damp, heavily forested zone immediately south of Bhabhar where underground streams re-emerge.\n3. **Bhangar**: Older alluvial terrace soil situated above flood levels; contains calcareous kankar deposits.\n4. **Khadar**: New, highly fertile alluvial silt deposited annually by river floodings in lowlands.",
                "words": ["Bhabhar (Pebbles/Streams Submerge)", "Terai (Marshy/Re-emerges)", "Bhangar (Old Alluvium)", "Khadar (New Silt)"],
                "correct": "Khadar is the newly deposited, most fertile river silt; Bhangar is older upland alluvium.",
                "incorrect": "Confusing Khadar with older alluvium."
            },
            {
                "rule_number": 3,
                "title": "Tropic of Cancer Indian States Mnemonic",
                "explanation": "The Tropic of Cancer ($23.5^\\circ$ N) passes through exactly **8 Indian States** from West to East:\n**Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram**.\n(Mnemonic: 'GR MC J WTM' or 'Mitra Par Gamchha Jhar').\n*Mahi River is the only river in India that crosses the Tropic of Cancer TWICE.*",
                "words": ["8 States", "Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, WB, Tripura, Mizoram", "Mahi River (Twice)"],
                "correct": "The Tropic of Cancer passes through 8 states; the Mahi River cuts it twice.",
                "incorrect": "Including Odisha or Bihar (Tropic of Cancer does NOT pass through Odisha or Bihar)."
            },
            {
                "rule_number": 4,
                "title": "Indian Standard Time (IST) 82.5° E Meridian",
                "explanation": "Indian Standard Time is calculated from the $82^\\circ 30' \\text{ E}$ longitude passing through Mirzapur (near Prayagraj, Uttar Pradesh). It passes through **5 states**: **Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Odisha, Andhra Pradesh**.\n$82.5^\\circ \\times 4 \\text{ mins/deg} = 330 \\text{ mins} = \\mathbf{+5 \\text{ hours } 30 \\text{ minutes}}$ ahead of Greenwich Mean Time (GMT/UTC).",
                "words": ["82° 30' E", "Mirzapur (UP)", "5 States: UP, MP, CG, Odisha, AP", "+5:30 GMT"],
                "correct": "IST is exactly 5 hours and 30 minutes ahead of GMT/UTC.",
                "incorrect": "Calculating IST as +5:00 hours."
            },
            {
                "rule_number": 5,
                "title": "Ten Degree Channel and Andaman Nicobar Separation",
                "explanation": "- **Ten Degree Channel ($10^\\circ$ N)**: Separates the **Little Andaman** island from the **Car Nicobar** island.\n- **Duncan Passage**: Separates South Andaman from Little Andaman.\n- **Indira Point** (Pygmalion Point): Southernmost point of the Republic of India at $6^\\circ 45' \\text{ N}$ on Great Nicobar island.",
                "words": ["10° Channel", "Little Andaman and Car Nicobar", "Duncan Passage", "Indira Point (6°45' N)"],
                "correct": "The Ten Degree Channel separates the Andaman Islands from the Nicobar Islands.",
                "incorrect": "Stating that the 10 Degree Channel separates India from Sri Lanka (that is Palk Strait!)."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Claiming the Tropic of Cancer passes through Odisha or Uttar Pradesh.",
                "correction": "Tropic of Cancer strictly passes through 8 states: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, WB, Tripura, Mizoram.",
                "rationale": "High-frequency negative mark trap in SSC CGL."
            },
            {
                "mistake": "Confusing Palk Strait with Ten Degree Channel.",
                "correction": "Palk Strait separates India (Tamil Nadu) and Sri Lanka. Ten Degree Channel separates Andaman and Nicobar.",
                "rationale": "Marine geography boundary distinction."
            },
            {
                "mistake": "Assuming all peninsular rivers flow East and form deltas.",
                "correction": "Narmada and Tapi flow West into the Arabian Sea and form estuaries, not deltas.",
                "rationale": "They flow through fault-line rift valleys that prevent delta formation."
            },
            {
                "mistake": "Naming Mt. K2 (Godwin-Austen) as the highest peak completely in Indian administered territory.",
                "correction": "Kanchenjunga (8,586 m in Sikkim) is the highest peak in undisputed Indian territory. K2 (8,611 m) is in Pakistan-occupied Kashmir (PoK).",
                "rationale": "Crucial distinction between highest peak of Indian territory vs administered territory."
            }
        ],
        "quick_revision_points": [
            "Tropic of Cancer (23.5° N) crosses 8 Indian states; Mahi River crosses it twice",
            "Indian Standard Meridian (82° 30' E) passes through Mirzapur (UP, MP, CG, Odisha, AP); +5:30 GMT",
            "Ten Degree Channel separates Andaman from Nicobar; Palk Strait separates India from Sri Lanka",
            "Narmada (Amarkantak) and Tapi (Multai) flow West through rift valleys, forming estuaries",
            "Godavari is the longest Peninsular river (1,465 km, 'Dakshin Ganga' / 'Vridha Ganga')",
            "Black/Regur soil is rich in clay, self-ploughing, moisture-retentive, ideal for cotton",
            "Mawsynram in Meghalaya (Khasi Hills) receives the world's highest annual rainfall (~11,872 mm)",
            "Deepest ocean trench: Mariana Trench in Pacific Ocean (~11,034 m)"
        ]
    },
    "previous_year_questions": [
        {
            "id": 5301,
            "topic_id": 53,
            "exam_id": 1,
            "question": "Through which of the following states does the Tropic of Cancer NOT pass? [SSC CGL 2023 Tier 1]",
            "options_json": ["Odisha", "Rajasthan", "Chhattisgarh", "Tripura"],
            "correct_answer": "Odisha",
            "explanation": "The Tropic of Cancer (23.5° N) passes through 8 Indian states: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram. It does NOT pass through Odisha.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5302,
            "topic_id": 53,
            "exam_id": 1,
            "question": "Which water body separates the Andaman Islands from the Nicobar Islands? [UPSC CDS 2022]",
            "options_json": ["Ten Degree Channel", "Nine Degree Channel", "Eight Degree Channel", "Palk Strait"],
            "correct_answer": "Ten Degree Channel",
            "explanation": "The Ten Degree Channel is a 150 km wide strait in the Bay of Bengal that lies along the 10° N latitude, separating the Little Andaman island to the north from the Car Nicobar island to the south.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5303,
            "topic_id": 53,
            "exam_id": 1,
            "question": "Which of the following Indian rivers flows through a rift valley into the Arabian Sea? [RRB NTPC 2022]",
            "options_json": ["Narmada", "Godavari", "Krishna", "Cauvery"],
            "correct_answer": "Narmada",
            "explanation": "The Narmada River originates from the Amarkantak plateau in Madhya Pradesh and flows westward through a linear rift valley between the Vindhya and Satpura mountain ranges, draining into the Gulf of Khambhat (Arabian Sea).",
            "source_id": 7,
            "status": "published"
        }
    ],
    "practice_questions": [
        {
            "id": 5301,
            "topic_id": 53,
            "question": "What is the standard time difference between Indian Standard Time (IST) and Greenwich Mean Time (GMT)?",
            "options_json": ["+5 hours 30 minutes", "+5 hours", "+6 hours", "+4 hours 30 minutes"],
            "correct_answer": "+5 hours 30 minutes",
            "explanation": "IST is based on the 82° 30' E meridian, which is exactly 5 hours and 30 minutes ahead of GMT (82.5 * 4 mins = 330 mins = 5.5 hrs).",
            "points": 1
        },
        {
            "id": 5302,
            "topic_id": 53,
            "question": "Which is the highest mountain peak located entirely within undisputed Indian territory?",
            "options_json": ["Kanchenjunga", "K2 (Godwin-Austen)", "Nanda Devi", "Kamet"],
            "correct_answer": "Kanchenjunga",
            "explanation": "Kanchenjunga (8,586 m), situated on the border of Sikkim and Nepal, is the highest mountain peak in undisputed Indian territory.",
            "points": 1
        },
        {
            "id": 5303,
            "topic_id": 53,
            "question": "Which river is popularly known as 'Dakshin Ganga' due to its size and length?",
            "options_json": ["Godavari", "Krishna", "Cauvery", "Mahanadi"],
            "correct_answer": "Godavari",
            "explanation": "The Godavari River, with a length of 1,465 km, is the longest peninsular river and is termed 'Dakshin Ganga' or 'Vridha Ganga'.",
            "points": 1
        },
        {
            "id": 5304,
            "topic_id": 53,
            "question": "Which place in India receives the highest average annual rainfall in the world?",
            "options_json": ["Mawsynram", "Cherrapunji", "Agumbe", "Mahabaleshwar"],
            "correct_answer": "Mawsynram",
            "explanation": "Mawsynram, situated in the East Khasi Hills of Meghalaya, receives the world's highest average annual rainfall (~11,872 mm).",
            "points": 1
        },
        {
            "id": 5305,
            "topic_id": 53,
            "question": "Black soil is predominantly known by which alternative name?",
            "options_json": ["Regur soil", "Bhangar soil", "Khadar soil", "Laterite soil"],
            "correct_answer": "Regur soil",
            "explanation": "Black soil is locally known as Regur soil, derived from the Telugu word 'Reguda'. It is also known as Black Cotton Soil.",
            "points": 1
        },
        {
            "id": 5306,
            "topic_id": 53,
            "question": "Which strait separates India from the island nation of Sri Lanka?",
            "options_json": ["Palk Strait", "Ten Degree Channel", "Duncan Passage", "Malacca Strait"],
            "correct_answer": "Palk Strait",
            "explanation": "The Palk Strait is a water body between Tamil Nadu state of India and the Jaffna District of Sri Lanka.",
            "points": 1
        },
        {
            "id": 5307,
            "topic_id": 53,
            "question": "Which is the only river in India that crosses the Tropic of Cancer twice?",
            "options_json": ["Mahi River", "Sabarmati River", "Chambal River", "Betwa River"],
            "correct_answer": "Mahi River",
            "explanation": "The Mahi River originates in Madhya Pradesh, flows into Rajasthan crossing the Tropic of Cancer, and turns into Gujarat crossing it again.",
            "points": 1
        },
        {
            "id": 5308,
            "topic_id": 53,
            "question": "The Majuli river island, the world's largest inhabited river island, is located on which river?",
            "options_json": ["Brahmaputra", "Ganga", "Indus", "Godavari"],
            "correct_answer": "Brahmaputra",
            "explanation": "Majuli is a fluvial river island in the Brahmaputra River in Assam, recognized by Guinness World Records as the world's largest river island.",
            "points": 1
        },
        {
            "id": 5309,
            "topic_id": 53,
            "question": "Which pass connects Srinagar with Leh (Ladakh)?",
            "options_json": ["Zojila Pass", "Shipki La", "Rohtang Pass", "Nathu La"],
            "correct_answer": "Zojila Pass",
            "explanation": "Zojila Pass is a strategic high-altitude mountain pass in the Himalayas (NH-1) connecting Srinagar with Dras and Leh.",
            "points": 1
        },
        {
            "id": 5310,
            "topic_id": 53,
            "question": "What is the southernmost point of India situated in the Nicobar Islands called?",
            "options_json": ["Indira Point", "Indira Col", "Kanyakumari", "Kibithu"],
            "correct_answer": "Indira Point",
            "explanation": "Indira Point (6° 45' N latitude), located on Great Nicobar island, is the southernmost geographic point of the territory of India.",
            "points": 1
        }
    ],
    "quiz_questions": [
        {
            "id": 5301,
            "topic_id": 53,
            "question": "How many Indian states lie along the coastline of mainland India?",
            "options_json": ["9 states", "7 states", "8 states", "10 states"],
            "correct_answer": "9 states",
            "explanation": "The 9 coastal states are: Gujarat, Maharashtra, Goa, Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Odisha, and West Bengal.",
            "points": 1
        },
        {
            "id": 5302,
            "topic_id": 53,
            "question": "Which state in India possesses the longest coastline?",
            "options_json": ["Gujarat", "Andhra Pradesh", "Tamil Nadu", "Maharashtra"],
            "correct_answer": "Gujarat",
            "explanation": "Gujarat has the longest coastline among all Indian states, spanning approximately 1,600 km.",
            "points": 1
        },
        {
            "id": 5303,
            "topic_id": 53,
            "question": "What is the older, less fertile alluvial soil found above flood plains called?",
            "options_json": ["Bhangar", "Khadar", "Bhabhar", "Terai"],
            "correct_answer": "Bhangar",
            "explanation": "Bhangar is the older alluvium containing calcareous kankar nodules, found in higher elevated terraces above regular flood lines.",
            "points": 1
        },
        {
            "id": 5304,
            "topic_id": 53,
            "question": "The Western Ghats and Eastern Ghats converge at which mountain range?",
            "options_json": ["Nilgiri Hills", "Cardamom Hills", "Anaimalai Hills", "Palani Hills"],
            "correct_answer": "Nilgiri Hills",
            "explanation": "The Western Ghats and Eastern Ghats meet at the Nilgiri Hills (Blue Mountains) where Dodabetta is a prominent high peak.",
            "points": 1
        },
        {
            "id": 5305,
            "topic_id": 53,
            "question": "What is the highest peak in the Western Ghats and in Peninsular India?",
            "options_json": ["Anamudi", "Doddabetta", "Kalsubai", "Guru Shikhar"],
            "correct_answer": "Anamudi",
            "explanation": "Anamudi (2,695 m), situated in the Anaimalai Hills in Kerala, is the highest peak in Peninsular India.",
            "points": 1
        },
        {
            "id": 5306,
            "topic_id": 53,
            "question": "Which ocean current is known as a warm ocean current?",
            "options_json": ["Gulf Stream", "Labrador Current", "Canary Current", "California Current"],
            "correct_answer": "Gulf Stream",
            "explanation": "The Gulf Stream is a powerful, warm Atlantic ocean current originating in the Gulf of Mexico, while Labrador and Canary are cold currents.",
            "points": 1
        },
        {
            "id": 5307,
            "topic_id": 53,
            "question": "Which state of India shares international borders with three foreign countries (Nepal, Bhutan, and China)?",
            "options_json": ["Sikkim", "Arunachal Pradesh", "West Bengal", "Assam"],
            "correct_answer": "Sikkim",
            "explanation": "Sikkim is bordered by Nepal to the west, Bhutan to the east, and the Tibet Autonomous Region of China to the north.",
            "points": 1
        },
        {
            "id": 5308,
            "topic_id": 53,
            "question": "The Chilika Lake, India's largest coastal lagoon, is located in which state?",
            "options_json": ["Odisha", "Andhra Pradesh", "Tamil Nadu", "Kerala"],
            "correct_answer": "Odisha",
            "explanation": "Chilika Lake is a brackish water coastal lagoon located across Puri, Khurda, and Ganjam districts of Odisha.",
            "points": 1
        },
        {
            "id": 5309,
            "topic_id": 53,
            "question": "Which planet in the solar system is known as the 'Morning Star' and 'Evening Star'?",
            "options_json": ["Venus", "Mars", "Mercury", "Jupiter"],
            "correct_answer": "Venus",
            "explanation": "Venus, the brightest planet in the night sky with high albedo from reflective sulfuric acid clouds, is known as the Morning and Evening Star.",
            "points": 1
        },
        {
            "id": 5310,
            "topic_id": 53,
            "question": "What is the boundary line between India and China called?",
            "options_json": ["McMahon Line", "Radcliffe Line", "Durand Line", "49th Parallel"],
            "correct_answer": "McMahon Line",
            "explanation": "The McMahon Line, established at the 1914 Simla Convention, serves as the boundary between Tibet/China and the northeastern region of India.",
            "points": 1
        }
    ]
}

topic_54 = {
    "title": "Indian Polity: Constitutional Governance, Parliament, Executive & Judiciary",
    "source_id": 7,
    "content": {
        "definition": "Indian Polity examines the operational architecture of the Indian constitutional democracy, including the division of powers between the Union and the States, executive governance, parliamentary lawmaking, judicial independence, and statutory/constitutional watchdogs. In competitive examinations (UPSC, SSC CGL Tier 1/2, CDS, State PCS, Banking), polity questions test articles, presidential powers, parliamentary motions, bicameral procedures, and landmark institutional functions (CAG, ECI, UPSC, Finance Commission).",
        "overview": "Fundamental Pillars of Indian Polity:\n- Union Executive (Part V): President (Head of State, Articles 52–62; veto powers, pardoning power Article 72, ordinance power Article 123); Vice President (Ex-officio Chairman of Rajya Sabha, Article 63–64); Prime Minister & Council of Ministers (Article 74–75, real executive, collective responsibility to Lok Sabha)\n- Union Legislature (Parliament, Article 79): Lok Sabha (House of the People, max 550, money bills initiate here); Rajya Sabha (Council of States, permanent house, 250 members, 1/3rd retire every 2 years); Parliamentary Proceedings (Question Hour, Zero Hour, Calling Attention, No-Confidence Motion)\n- Judiciary: Supreme Court of India (Articles 124–147, Guardian of Constitution, Court of Record Article 129, Judicial Review, Writs under Article 32); High Courts (Article 226 writ jurisdiction wider than SC)\n- Key Constitutional Bodies: Comptroller and Auditor General (CAG, Article 148); Election Commission of India (ECI, Article 324); Finance Commission (Article 280); Union Public Service Commission (UPSC, Article 315–323)",
        "types": [
            {
                "name": "1. Union Executive & Head of State",
                "desc": "Electoral College of President, emergency declarations, ordinance promulgation, and pardoning powers.",
                "examples": [
                    "President elected by elected members of both houses of Parliament and elected MLAs of States and UTs (Delhi, Puducherry, J&K)",
                    "Ordinance under Article 123: valid for max 6 months and 6 weeks unless approved by Parliament"
                ]
            },
            {
                "name": "2. Parliament & Legislative Procedures",
                "desc": "Ordinary Bills, Money Bills (Article 110), Financial Bills, Constitutional Amendment Bills (Article 368).",
                "examples": [
                    "Money Bill (Article 110): Speaker's certification is final; Rajya Sabha can only delay for max 14 days",
                    "Joint Sitting (Article 108): Summoned by President, presided over by Speaker of Lok Sabha"
                ]
            },
            {
                "name": "3. Union & State Judiciary",
                "desc": "Original, appellate, and advisory jurisdictions (Article 143), judicial review, and collegium system.",
                "examples": [
                    "Article 131: Original jurisdiction over inter-state and Centre-State disputes",
                    "Article 143: Advisory jurisdiction of Supreme Court on reference by President"
                ]
            },
            {
                "name": "4. Constitutional & Independent Watchdogs",
                "desc": "Autonomy, appointment, tenure, and constitutional mandates of oversight bodies.",
                "examples": [
                    "CAG (Article 148): 'Friend, philosopher and guide' of Public Accounts Committee (PAC)",
                    "Finance Commission (Article 280): Constituted every 5 years to recommend tax devolution ratios"
                ]
            },
            {
                "name": "5. Federal Relations & Emergency Provisions",
                "desc": "Distribution of legislative subjects (Union, State, Concurrent lists in 7th Schedule) and Emergency types.",
                "examples": [
                    "National Emergency (Article 352), President's Rule (Article 356), Financial Emergency (Article 360)"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Money Bill Exclusive Procedures (Article 110)",
                "explanation": "A Money Bill (Article 110) has strictly unique legislative rules:\n1. It can be introduced **ONLY in the Lok Sabha** and **ONLY with prior recommendation of the President**.\n2. The **Speaker of Lok Sabha** has final authority to certify whether a bill is a Money Bill.\n3. The Rajya Sabha has **NO power to amend or reject** it; it can only make recommendations within **14 days**.\n4. There is **NO provision for a Joint Sitting** (Article 108) on a Money Bill!",
                "words": ["Article 110", "Lok Sabha Only", "Speaker's Decision Final", "Rajya Sabha Max 14 Days", "No Joint Sitting"],
                "correct": "Rajya Sabha must return a Money Bill within 14 days, with or without recommendations.",
                "incorrect": "Believing Rajya Sabha can reject a Money Bill or trigger a Joint Sitting."
            },
            {
                "rule_number": 2,
                "title": "Joint Sitting of Parliament Rule (Article 108)",
                "explanation": "If an Ordinary Bill faces deadlock between the two Houses after 6 months:\n- The **President summons** the Joint Sitting.\n- The **Speaker of the Lok Sabha presides** over the Joint Sitting (in their absence, the Deputy Speaker, then Deputy Chairman of Rajya Sabha).\n- *The Chairman of Rajya Sabha (Vice President) can NEVER preside over a Joint Sitting because they are not a member of Parliament!*",
                "words": ["Article 108", "President Summons", "Speaker Presides", "Chairman of RS Never Presides"],
                "correct": "The Speaker of the Lok Sabha presides over the Joint Sitting of both Houses of Parliament.",
                "incorrect": "Selecting the Vice President / Chairman of Rajya Sabha as the presiding officer."
            },
            {
                "rule_number": 3,
                "title": "President's Pardoning Power vs Governor's Power (Article 72 vs 161)",
                "explanation": "- **President (Article 72)**: Can pardon, reprive, respite, or remit any sentence, including **Court Martial (military) sentences** and **Death Sentences**.\n- **Governor (Article 161)**: Can pardon or remit sentences under State laws, but **CANNOT pardon a Death Sentence** (only suspend or remit) and has **NO power regarding Court Martial**.",
                "words": ["Article 72 (President)", "Article 161 (Governor)", "Death Sentence Exclusively President", "Court Martial"],
                "correct": "Only the President can grant complete pardon in death penalty cases; a Governor cannot fully pardon death.",
                "incorrect": "Assuming Governors have identical pardoning power as the President."
            },
            {
                "rule_number": 4,
                "title": "Collective Responsibility Rule (Article 75(3))",
                "explanation": "Under Article 75(3), the Council of Ministers is collectively responsible **exclusively to the LOK SABHA** (House of the People), not to the Parliament as a whole and not to the Rajya Sabha. If a No-Confidence Motion passes in the Lok Sabha, the entire ministry must resign.",
                "words": ["Article 75(3)", "Collectively Responsible to Lok Sabha Only", "No-Confidence Motion"],
                "correct": "The Council of Ministers is collectively responsible to the Lok Sabha alone.",
                "incorrect": "Stating they are collectively responsible to the Parliament or Rajya Sabha."
            },
            {
                "rule_number": 5,
                "title": "Public Accounts Committee (PAC) Chairperson Convention",
                "explanation": "The Public Accounts Committee consists of **22 members** (15 Lok Sabha + 7 Rajya Sabha). By established convention since 1967, its **Chairperson is invariably appointed from the OPPOSITION** party in the Lok Sabha by the Speaker. Ministers cannot be members of the PAC!",
                "words": ["22 Members (15 LS + 7 RS)", "Chairperson from Opposition", "CAG is Guide"],
                "correct": "The Chairperson of the Public Accounts Committee is appointed by the Speaker from the Opposition.",
                "incorrect": "Assuming the Prime Minister or Finance Minister heads the Public Accounts Committee."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Believing the Vice President presides over a Joint Sitting of Parliament.",
                "correction": "The Speaker of Lok Sabha presides. The Vice President (Chairman of RS) is not a member of Parliament and can never preside.",
                "rationale": "One of the most frequently asked trick questions in UPSC and SSC exams."
            },
            {
                "mistake": "Thinking Rajya Sabha has equal power over Money Bills.",
                "correction": "Rajya Sabha has zero power to reject or amend a Money Bill; it can only delay for up to 14 days.",
                "rationale": "Constitutional supremacy of the directly elected Lok Sabha in financial matters."
            },
            {
                "mistake": "Believing a No-Confidence Motion can be moved in the Rajya Sabha.",
                "correction": "A No-Confidence Motion can ONLY be introduced in the Lok Sabha (requires support of at least 50 members).",
                "rationale": "Article 75(3) establishes collective responsibility strictly to the Lok Sabha."
            },
            {
                "mistake": "Confusing High Court writ jurisdiction with Supreme Court writ jurisdiction.",
                "correction": "High Court writ jurisdiction (Article 226) is WIDER than Supreme Court (Article 32) because High Courts can issue writs for legal rights as well as fundamental rights.",
                "rationale": "Supreme Court under Article 32 can issue writs ONLY for Fundamental Rights violations."
            }
        ],
        "quick_revision_points": [
            "President (Art 52-62), Ordinance power (Art 123), Pardoning power (Art 72)",
            "Money Bill (Art 110): Introduced in Lok Sabha only, Speaker certifies, Rajya Sabha max 14 days",
            "Joint Sitting (Art 108): Summoned by President, presided over by Speaker of Lok Sabha",
            "Council of Ministers is collectively responsible to the Lok Sabha only (Art 75(3))",
            "CAG (Art 148): 'Guardian of Public Purse', audited reports scrutinized by PAC (15 LS + 7 RS)",
            "Supreme Court (Art 124-147), Writs (Art 32); High Court Writs (Art 226)",
            "Three Emergencies: National (Art 352), President's Rule (Art 356), Financial (Art 360 - never imposed in India)",
            "Parliamentary sessions: Budget Session (longest), Monsoon Session, Winter Session (shortest)"
        ]
    },
    "previous_year_questions": [
        {
            "id": 5401,
            "topic_id": 54,
            "exam_id": 1,
            "question": "Who presides over the Joint Sitting of both Houses of Parliament in India? [SSC CGL 2023 Tier 1]",
            "options_json": ["Speaker of Lok Sabha", "President of India", "Vice President (Chairman of Rajya Sabha)", "Prime Minister"],
            "correct_answer": "Speaker of Lok Sabha",
            "explanation": "Under Article 118(4) of the Indian Constitution, the Speaker of the Lok Sabha presides over a joint sitting of both Houses. In the Speaker's absence, the Deputy Speaker presides, followed by the Deputy Chairman of Rajya Sabha. The Vice President can never preside.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5402,
            "topic_id": 54,
            "exam_id": 1,
            "question": "For how many days can the Rajya Sabha withhold a Money Bill passed by the Lok Sabha? [UPSC CDS 2022]",
            "options_json": ["14 days", "30 days", "6 months", "3 months"],
            "correct_answer": "14 days",
            "explanation": "Under Article 109, once a Money Bill is transmitted to the Rajya Sabha, it must be returned within a maximum period of 14 days with or without recommendations. If not returned within 14 days, it is deemed to have been passed by both Houses.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5403,
            "topic_id": 54,
            "exam_id": 1,
            "question": "Under which Article of the Constitution can the President promulgate an Ordinance when Parliament is not in session? [RRB NTPC 2022]",
            "options_json": ["Article 123", "Article 213", "Article 110", "Article 72"],
            "correct_answer": "Article 123",
            "explanation": "Article 123 empowers the President to promulgate Ordinances during the recess of Parliament. (Article 213 provides corresponding ordinance power to State Governors).",
            "source_id": 7,
            "status": "published"
        }
    ],
    "practice_questions": [
        {
            "id": 5401,
            "topic_id": 54,
            "question": "Under Article 75(3), the Union Council of Ministers is collectively responsible to whom?",
            "options_json": ["Lok Sabha only", "Both Houses of Parliament", "President of India", "Prime Minister"],
            "correct_answer": "Lok Sabha only",
            "explanation": "Article 75(3) explicitly mandates: 'The Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha).'",
            "points": 1
        },
        {
            "id": 5402,
            "topic_id": 54,
            "question": "What is the maximum strength of the Rajya Sabha as prescribed by the Constitution?",
            "options_json": ["250 members", "245 members", "252 members", "260 members"],
            "correct_answer": "250 members",
            "explanation": "The maximum permissible strength of the Rajya Sabha is 250 (238 representing States/UTs and 12 nominated by the President).",
            "points": 1
        },
        {
            "id": 5403,
            "topic_id": 54,
            "question": "Who decides whether a bill is a Money Bill or not?",
            "options_json": ["Speaker of Lok Sabha", "President", "Finance Minister", "Chairman of Rajya Sabha"],
            "correct_answer": "Speaker of Lok Sabha",
            "explanation": "Under Article 110(3), if any question arises whether a Bill is a Money Bill or not, the decision of the Speaker of the House of the People thereon shall be final.",
            "points": 1
        },
        {
            "id": 5404,
            "topic_id": 54,
            "question": "What is the minimum age required to contest election for the office of the President of India?",
            "options_json": ["35 years", "30 years", "25 years", "21 years"],
            "correct_answer": "35 years",
            "explanation": "Under Article 58, a candidate for the office of President must have completed 35 years of age.",
            "points": 1
        },
        {
            "id": 5405,
            "topic_id": 54,
            "question": "Which Article provides the Supreme Court with the power of judicial review and writ jurisdiction for fundamental rights?",
            "options_json": ["Article 32", "Article 226", "Article 136", "Article 143"],
            "correct_answer": "Article 32",
            "explanation": "Article 32 confers the Right to Constitutional Remedies, empowering the Supreme Court to issue writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto).",
            "points": 1
        },
        {
            "id": 5406,
            "topic_id": 54,
            "question": "How many members are nominated to the Rajya Sabha by the President for literature, science, art, and social service?",
            "options_json": ["12 members", "10 members", "2 members", "14 members"],
            "correct_answer": "12 members",
            "explanation": "Under Article 80, the President nominates 12 members to the Rajya Sabha having special knowledge or practical experience in literature, science, art, and social service.",
            "points": 1
        },
        {
            "id": 5407,
            "topic_id": 54,
            "question": "The Comptroller and Auditor General of India (CAG) is appointed under which Article?",
            "options_json": ["Article 148", "Article 280", "Article 324", "Article 76"],
            "correct_answer": "Article 148",
            "explanation": "Article 148 establishes the office of the Comptroller and Auditor General of India, appointed by the President.",
            "points": 1
        },
        {
            "id": 5408,
            "topic_id": 54,
            "question": "What is the quorum required to constitute a sitting of either House of Parliament?",
            "options_json": ["One-tenth of total members", "One-sixth of total members", "One-fifth of total members", "One-third of total members"],
            "correct_answer": "One-tenth of total members",
            "explanation": "Under Article 100(3), the quorum to constitute a meeting of either House of Parliament is one-tenth (10%) of the total number of members.",
            "points": 1
        },
        {
            "id": 5409,
            "topic_id": 54,
            "question": "Which Financial Emergency provision has NEVER been invoked in the history of Independent India?",
            "options_json": ["Article 360", "Article 352", "Article 356", "Article 365"],
            "correct_answer": "Article 360",
            "explanation": "Article 360 empowers the President to proclaim Financial Emergency if financial stability or credit is threatened. It has never been declared in India.",
            "points": 1
        },
        {
            "id": 5410,
            "topic_id": 54,
            "question": "Who acts as the 'Friend, Philosopher, and Guide' of the Public Accounts Committee (PAC)?",
            "options_json": ["Comptroller and Auditor General (CAG)", "Attorney General of India", "Finance Minister", "Speaker of Lok Sabha"],
            "correct_answer": "Comptroller and Auditor General (CAG)",
            "explanation": "The CAG acts as the friend, philosopher, and guide to the Public Accounts Committee by assisting in scrutinizing government audit reports.",
            "points": 1
        }
    ],
    "quiz_questions": [
        {
            "id": 5401,
            "topic_id": 54,
            "question": "Who is the ex-officio Chairman of the Rajya Sabha?",
            "options_json": ["Vice President of India", "President of India", "Prime Minister", "Speaker of Lok Sabha"],
            "correct_answer": "Vice President of India",
            "explanation": "Under Article 64, the Vice President of India is the ex-officio Chairman of the Council of States (Rajya Sabha).",
            "points": 1
        },
        {
            "id": 5402,
            "topic_id": 54,
            "question": "What is the maximum gap permitted between two consecutive sessions of Parliament?",
            "options_json": ["6 months", "3 months", "4 months", "1 year"],
            "correct_answer": "6 months",
            "explanation": "Under Article 85(1), six months shall not intervene between the last sitting in one session and the date appointed for its first sitting in the next session.",
            "points": 1
        },
        {
            "id": 5403,
            "topic_id": 54,
            "question": "Who was the first Chief Justice of Independent India?",
            "options_json": ["H.J. Kania", "M. Patanjali Sastri", "Mehar Chand Mahajan", "B.K. Mukherjea"],
            "correct_answer": "H.J. Kania",
            "explanation": "Sir Harilal Jekisundas Kania served as the first Chief Justice of India from 1950 to 1951.",
            "points": 1
        },
        {
            "id": 5404,
            "topic_id": 54,
            "question": "The Attorney General for India is appointed by the President under which Article?",
            "options_json": ["Article 76", "Article 148", "Article 165", "Article 280"],
            "correct_answer": "Article 76",
            "explanation": "Article 76 provides for the appointment of the Attorney General for India, who is the highest law officer in the country.",
            "points": 1
        },
        {
            "id": 5405,
            "topic_id": 54,
            "question": "What is the tenure of the Chief Election Commissioner of India?",
            "options_json": ["6 years or up to 65 years of age", "5 years or up to 62 years of age", "5 years or up to 65 years of age", "6 years or up to 62 years of age"],
            "correct_answer": "6 years or up to 65 years of age",
            "explanation": "The Chief Election Commissioner holds office for a term of 6 years or until reaching 65 years of age, whichever is earlier.",
            "points": 1
        },
        {
            "id": 5406,
            "topic_id": 54,
            "question": "Who administers the oath of office to the President of India?",
            "options_json": ["Chief Justice of India", "Vice President", "Prime Minister", "Speaker of Lok Sabha"],
            "correct_answer": "Chief Justice of India",
            "explanation": "Under Article 60, the oath of office to the President is administered by the Chief Justice of India (or senior-most judge of the Supreme Court available).",
            "points": 1
        },
        {
            "id": 5407,
            "topic_id": 54,
            "question": "The concept of 'Public Interest Litigation' (PIL) originated in which country?",
            "options_json": ["United States", "United Kingdom", "Australia", "Canada"],
            "correct_answer": "United States",
            "explanation": "PIL originated in the United States in the 1960s and was pioneered in India in the late 1970s and 1980s by Justice P.N. Bhagwati and Justice V.R. Krishna Iyer.",
            "points": 1
        },
        {
            "id": 5408,
            "topic_id": 54,
            "question": "How many members are in the Public Accounts Committee (PAC)?",
            "options_json": ["22 members (15 LS + 7 RS)", "30 members (all LS)", "15 members (all LS)", "25 members (15 LS + 10 RS)"],
            "correct_answer": "22 members (15 LS + 7 RS)",
            "explanation": "The Public Accounts Committee consists of 22 members: 15 elected from Lok Sabha and 7 from Rajya Sabha.",
            "points": 1
        },
        {
            "id": 5409,
            "topic_id": 54,
            "question": "What is the minimum age to be elected as a member of the Lok Sabha?",
            "options_json": ["25 years", "30 years", "21 years", "18 years"],
            "correct_answer": "25 years",
            "explanation": "Under Article 84, the minimum age required to contest election for the Lok Sabha is 25 years (for Rajya Sabha it is 30 years).",
            "points": 1
        },
        {
            "id": 5410,
            "topic_id": 54,
            "question": "Under which Article can the Parliament amend the Constitution?",
            "options_json": ["Article 368", "Article 356", "Article 370", "Article 352"],
            "correct_answer": "Article 368",
            "explanation": "Article 368 in Part XX of the Constitution outlines the constituent powers and procedures of Parliament to amend the Constitution.",
            "points": 1
        }
    ]
}

topic_55 = {
    "title": "Constitution of India: Preamble, Fundamental Rights, DPSP, Duties & Amendments",
    "source_id": 7,
    "content": {
        "definition": "The Constitution of India is the supreme lex (fundamental law) of the Republic of India, drafted by the Constituent Assembly under Dr. B.R. Ambedkar (Chairman of the Drafting Committee) and adopted on 26 November 1949 (effective 26 January 1950). In competitive exams (UPSC, SSC CGL Tier 1/2, CDS, NDA, State PCS), constitutional testing focuses on the Preamble's philosophical keywords, Fundamental Rights (Articles 12–35), Directive Principles of State Policy (Articles 36–51), Fundamental Duties (Article 51A), Constitutional Amendments (42nd, 44th, 73rd, 86th, 101st), and the Basic Structure Doctrine.",
        "overview": "Architectural Framework of the Indian Constitution:\n- Preamble: 'SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC' and securing 'JUSTICE, LIBERTY, EQUALITY, FRATERNITY' (Amended once by the 42nd Amendment 1976 adding Socialist, Secular, Integrity)\n- Fundamental Rights (Part III, Articles 12–35, Magna Carta of India):\n  - Right to Equality (Articles 14–18): Art 14 (Equality before law), Art 15 (No discrimination), Art 16 (Equal opportunity in public employment), Art 17 (Abolition of Untouchability), Art 18 (Abolition of Titles)\n  - Right to Freedom (Articles 19–22): Art 19 (6 democratic freedoms), Art 21 (Protection of life & personal liberty), Art 21A (Right to Education)\n  - Right against Exploitation (Articles 23–24): Human trafficking & child labor prohibition\n  - Right to Freedom of Religion (Articles 25–28)\n  - Cultural & Educational Rights (Articles 29–30)\n  - Right to Constitutional Remedies (Article 32): 'Heart and Soul' of the Constitution (Dr. Ambedkar)\n- Directive Principles of State Policy (Part IV, Articles 36–51): Non-justiciable ideals borrowed from Ireland\n- Fundamental Duties (Part IVA, Article 51A): 11 duties added by 42nd Amendment on Swaran Singh Committee recommendation (11th duty added by 86th Amendment 2002)",
        "types": [
            {
                "name": "1. Preamble & Philosophical Foundations",
                "desc": "Solemn resolve, adoption date (26 Nov 1949), key values, and Kesavananda Bharati judgment status.",
                "examples": [
                    "Keywords added by 42nd Amendment 1976: 'Socialist', 'Secular', and 'Integrity'",
                    "Kesavananda Bharati case (1973): SC ruled Preamble is an integral part of the Constitution and can be amended without violating Basic Structure"
                ]
            },
            {
                "name": "2. Six Core Fundamental Rights (Articles 12–35)",
                "desc": "Justiciable basic human liberties enforceable against the State.",
                "examples": [
                    "Article 17: Abolition of Untouchability (Absolute right with no exceptions)",
                    "Article 21: Right to Life and Personal Liberty (Maneka Gandhi case expanded to include dignity, privacy, clean environment)"
                ]
            },
            {
                "name": "3. Five Prerogative Writs (Articles 32 & 226)",
                "desc": "Judicial orders to protect rights: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto.",
                "examples": [
                    "Habeas Corpus ('To have the body'): Safeguard against illegal, arbitrary detention",
                    "Quo-Warranto ('By what authority'): Inquires into the legality of a claim to public office"
                ]
            },
            {
                "name": "4. Directive Principles of State Policy (Part IV)",
                "desc": "Socialist, Gandhian, and Liberal-Intellectual governance principles (Articles 36–51).",
                "examples": [
                    "Article 40: Organization of Village Panchayats (Gandhian principle)",
                    "Article 44: Uniform Civil Code (UCC) for the citizens"
                ]
            },
            {
                "name": "5. Landmark Constitutional Amendments",
                "desc": "Key amendments transforming the constitutional landscape.",
                "examples": [
                    "42nd Amendment (1976): 'Mini-Constitution'; added Fundamental Duties, Preamble keywords, transferred subjects to Concurrent List",
                    "44th Amendment (1978): Removed Right to Property from Fundamental Rights (made legal right under Art 300A)"
                ]
            }
        ],
        "rules": [
            {
                "rule_number": 1,
                "title": "Fundamental Rights That Cannot Be Suspended (Articles 20 & 21)",
                "explanation": "During a National Emergency declared under Article 352, the 44th Constitutional Amendment Act (1978) established that the rights guaranteed under **Article 20 (Protection in respect of conviction for offences)** and **Article 21 (Protection of life and personal liberty)** CAN NEVER BE SUSPENDED under any circumstances.",
                "words": ["Articles 20 & 21", "Cannot Be Suspended", "National Emergency (Art 352)", "44th Amendment 1978"],
                "correct": "Articles 20 and 21 remain enforceable even during the proclamation of a National Emergency.",
                "incorrect": "Assuming all Fundamental Rights are suspended during an emergency."
            },
            {
                "rule_number": 2,
                "title": "Justiciable (FRs) vs Non-Justiciable (DPSP) Rule",
                "explanation": "- **Fundamental Rights (Part III)** are **JUSTICIABLE**: If violated by the State, an individual can directly petition the Supreme Court (Art 32) or High Court (Art 226) for judicial enforcement.\n- **Directive Principles of State Policy (Part IV)** are **NON-JUSTICIABLE** (Article 37): No citizen can approach a court to force the government to implement a DPSP.",
                "words": ["FRs Justiciable (Art 32)", "DPSP Non-Justiciable (Art 37)", "Court Enforceability"],
                "correct": "DPSP are fundamental in governance, but are not enforceable by any court of law.",
                "incorrect": "Filing a writ petition claiming violation of a Directive Principle."
            },
            {
                "rule_number": 3,
                "title": "Borrowing Sources of the Indian Constitution",
                "explanation": "- **Government of India Act 1935**: Federal Scheme, Office of Governor, Judiciary, Public Service Commissions.\n- **UK (British)**: Parliamentary system, Rule of Law, Single Citizenship, Bicameralism, Cabinet system.\n- **USA**: Fundamental Rights, Judicial Review, Preamble, Impeachment of President, Removal of SC/HC judges.\n- **Ireland**: Directive Principles of State Policy (DPSP), Nomination of 12 RS members, Method of Presidential election.\n- **USSR (Russia)**: Fundamental Duties (Article 51A), Ideals of Justice in Preamble.\n- **Australia**: Concurrent List, Joint Sitting (Article 108), Freedom of trade/commerce.\n- **South Africa**: Procedure for Constitutional Amendment (Article 368).\n- **Germany (Weimar)**: Suspension of Fundamental Rights during Emergency.",
                "words": ["USA (FRs, Judicial Review)", "UK (Parliament, Single Citizenship)", "Ireland (DPSP)", "USSR (Duties)", "South Africa (Art 368)"],
                "correct": "Fundamental Duties were borrowed from the USSR; DPSP was borrowed from Ireland.",
                "incorrect": "Believing Fundamental Rights were borrowed from Britain (UK has no written bill of rights)."
            },
            {
                "rule_number": 4,
                "title": "Five Prerogative Writs Functions Rule",
                "explanation": "1. **Habeas Corpus** ('Produce the Body'): Against unlawful/illegal detention (can be issued against public AND private individuals).\n2. **Mandamus** ('We Command'): Orders a public official to perform a mandatory statutory duty (cannot be issued against private bodies, President, or Governor).\n3. **Prohibition**: Issued by higher court to lower court/tribunal to STOP exceeding its jurisdiction.\n4. **Certiorari** ('To be certified'): Issued by higher court to lower court/tribunal to QUASH an order passed without jurisdiction.\n5. **Quo-Warranto** ('By what authority'): Prevents unlawful usurpation of a public office.",
                "words": ["Habeas Corpus (Detention)", "Mandamus (Duty)", "Prohibition (Stop)", "Certiorari (Quash)", "Quo-Warranto (Authority)"],
                "correct": "Mandamus commands a public official to perform their official public duty.",
                "incorrect": "Filing Mandamus against a private company or private citizen."
            },
            {
                "rule_number": 5,
                "title": "86th Constitutional Amendment Act (2002) Triad",
                "explanation": "The 86th Amendment Act (2002) made Right to Education a universal priority by altering three parts of the Constitution simultaneously:\n1. Inserted **Article 21A** in Part III: Free and compulsory education for children aged 6 to 14 is a Fundamental Right.\n2. Substituted **Article 45** in Part IV (DPSP): Early childhood care and education for children below 6 years.\n3. Added 11th Fundamental Duty **Article 51A(k)** in Part IVA: Duty of parent/guardian to provide educational opportunities to child aged 6-14.",
                "words": ["86th Amendment (2002)", "Art 21A (Age 6-14)", "Art 45 (Below 6)", "11th Duty Art 51A(k)"],
                "correct": "The 86th Amendment added Article 21A making free education for ages 6-14 a Fundamental Right.",
                "incorrect": "Assuming Right to Education was originally present in the 1950 Constitution."
            }
        ],
        "common_mistakes": [
            {
                "mistake": "Believing Right to Property is still a Fundamental Right.",
                "correction": "Right to Property was deleted from Part III by the 44th Amendment Act in 1978 and is now only a Legal Right under Article 300A in Part XII.",
                "rationale": "High-frequency trap question across all competitive examinations."
            },
            {
                "mistake": "Confusing the date of adoption with the date of commencement of the Constitution.",
                "correction": "Adopted on 26 November 1949 (celebrated as Constitution Day); Commenced into force on 26 January 1950 (Republic Day).",
                "rationale": "Exam questions test the precise distinction between adoption and commencement."
            },
            {
                "mistake": "Thinking Fundamental Duties were in the original 1950 Constitution.",
                "correction": "Fundamental Duties were NOT part of the original Constitution. They were added in 1976 (42nd Amendment) on the recommendation of the Swaran Singh Committee.",
                "rationale": "Key historical fact frequently queried in prelims."
            },
            {
                "mistake": "Confusing Article 32 with Article 226 writ powers.",
                "correction": "Article 32 is a Fundamental Right itself and applies only to Fundamental Rights. Article 226 is a constitutional power of High Courts covering Fundamental Rights as well as ordinary legal rights.",
                "rationale": "High Courts have a wider writ jurisdiction than the Supreme Court."
            }
        ],
        "quick_revision_points": [
            "Constitution adopted: 26 Nov 1949 (Constitution Day); Commenced: 26 Jan 1950 (Republic Day)",
            "Drafting Committee Chairman: Dr. B.R. Ambedkar; Constitutional Advisor: Sir B.N. Rau",
            "Preamble amended once (42nd Amendment 1976): added 'Socialist', 'Secular', 'Integrity'",
            "Right to Property was deleted as a Fundamental Right by 44th Amendment (1978); now legal right (Art 300A)",
            "Article 21A (86th Amendment 2002): Free & compulsory education for children aged 6 to 14",
            "Articles 20 and 21 can NEVER be suspended during any Emergency",
            "Writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto (Art 32 SC, Art 226 HC)",
            "Article 44: Uniform Civil Code (DPSP); Article 40: Village Panchayats; Article 51: International Peace",
            "Fundamental Duties: 11 duties under Article 51A (Part IVA), added on Swaran Singh Committee advice"
        ]
    },
    "previous_year_questions": [
        {
            "id": 5501,
            "topic_id": 55,
            "exam_id": 1,
            "question": "Which Constitutional Amendment added the words 'Socialist', 'Secular', and 'Integrity' to the Preamble of the Indian Constitution? [SSC CGL 2023 Tier 1]",
            "options_json": ["42nd Amendment Act (1976)", "44th Amendment Act (1978)", "52nd Amendment Act (1985)", "86th Amendment Act (2002)"],
            "correct_answer": "42nd Amendment Act (1976)",
            "explanation": "The Preamble has been amended only once till date, by the 42nd Constitutional Amendment Act of 1976, which added three new words: 'Socialist', 'Secular', and 'Integrity'.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5502,
            "topic_id": 55,
            "exam_id": 1,
            "question": "Which of the following Fundamental Rights cannot be suspended even during a National Emergency declared under Article 352? [UPSC CDS 2022]",
            "options_json": ["Articles 20 and 21", "Articles 14 and 19", "Articles 19 and 20", "Articles 21 and 22"],
            "correct_answer": "Articles 20 and 21",
            "explanation": "By the 44th Constitutional Amendment Act (1978), the right to protection in respect of conviction for offences (Article 20) and the right to life and personal liberty (Article 21) cannot be suspended even during a National Emergency.",
            "source_id": 7,
            "status": "published"
        },
        {
            "id": 5503,
            "topic_id": 55,
            "exam_id": 1,
            "question": "Which Article of the Constitution of India provides for the Uniform Civil Code (UCC) for the citizens? [RRB NTPC 2022]",
            "options_json": ["Article 44", "Article 40", "Article 48", "Article 50"],
            "correct_answer": "Article 44",
            "explanation": "Article 44 of the Directive Principles of State Policy (Part IV) states that 'The State shall endeavour to secure for the citizens a Uniform Civil Code throughout the territory of India.'",
            "source_id": 7,
            "status": "published"
        }
    ],
    "practice_questions": [
        {
            "id": 5501,
            "topic_id": 55,
            "question": "Who was the Chairman of the Drafting Committee of the Constituent Assembly?",
            "options_json": ["Dr. B.R. Ambedkar", "Dr. Rajendra Prasad", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel"],
            "correct_answer": "Dr. B.R. Ambedkar",
            "explanation": "Dr. Bhimrao Ramji Ambedkar was appointed Chairman of the 7-member Drafting Committee on 29 August 1947.",
            "points": 1
        },
        {
            "id": 5502,
            "topic_id": 55,
            "question": "Which Article of the Constitution abolishes 'Untouchability' and forbids its practice in any form?",
            "options_json": ["Article 17", "Article 14", "Article 15", "Article 18"],
            "correct_answer": "Article 17",
            "explanation": "Article 17 of the Constitution explicitly abolishes Untouchability and makes its practice in any form punishable by law.",
            "points": 1
        },
        {
            "id": 5503,
            "topic_id": 55,
            "question": "The Fundamental Duties were incorporated into the Constitution on the recommendation of which Committee?",
            "options_json": ["Swaran Singh Committee", "Sarkaria Commission", "Verma Committee", "Kothari Commission"],
            "correct_answer": "Swaran Singh Committee",
            "explanation": "The Swaran Singh Committee (1976) recommended the inclusion of Fundamental Duties, which was enacted via the 42nd Amendment Act.",
            "points": 1
        },
        {
            "id": 5504,
            "topic_id": 55,
            "question": "Under which Article did Dr. B.R. Ambedkar describe as the 'Heart and Soul' of the Constitution?",
            "options_json": ["Article 32", "Article 21", "Article 14", "Article 19"],
            "correct_answer": "Article 32",
            "explanation": "Dr. Ambedkar termed Article 32 (Right to Constitutional Remedies) as the heart and soul of the Constitution because it guarantees the judicial enforcement of all Fundamental Rights.",
            "points": 1
        },
        {
            "id": 5505,
            "topic_id": 55,
            "question": "The Directive Principles of State Policy (DPSP) in the Indian Constitution were borrowed from which country?",
            "options_json": ["Ireland", "United States", "United Kingdom", "Canada"],
            "correct_answer": "Ireland",
            "explanation": "The concept of DPSP (Part IV, Articles 36–51) was borrowed from the Irish Constitution of 1937.",
            "points": 1
        },
        {
            "id": 5506,
            "topic_id": 55,
            "question": "By which Amendment Act was the Right to Property removed from the list of Fundamental Rights?",
            "options_json": ["44th Amendment Act (1978)", "42nd Amendment Act (1976)", "24th Amendment Act (1971)", "73rd Amendment Act (1992)"],
            "correct_answer": "44th Amendment Act (1978)",
            "explanation": "The Janata Party government under Morarji Desai enacted the 44th Amendment in 1978, converting Right to Property into a legal right under Article 300A.",
            "points": 1
        },
        {
            "id": 5507,
            "topic_id": 55,
            "question": "Which Article provides for 'Free and compulsory education to all children aged 6 to 14 years' as a Fundamental Right?",
            "options_json": ["Article 21A", "Article 19", "Article 24", "Article 45"],
            "correct_answer": "Article 21A",
            "explanation": "Article 21A was inserted by the 86th Constitutional Amendment Act (2002) to mandate free and compulsory education for children between 6 and 14 years.",
            "points": 1
        },
        {
            "id": 5508,
            "topic_id": 55,
            "question": "Which prerogative writ is issued to secure the release of a person who has been detained unlawfully?",
            "options_json": ["Habeas Corpus", "Mandamus", "Certiorari", "Quo-Warranto"],
            "correct_answer": "Habeas Corpus",
            "explanation": "Habeas Corpus literally means 'To have the body'. It is a powerful remedy against illegal or arbitrary confinement by state or private actors.",
            "points": 1
        },
        {
            "id": 5509,
            "topic_id": 55,
            "question": "How many Fundamental Duties are currently listed under Article 51A of the Indian Constitution?",
            "options_json": ["11", "10", "12", "9"],
            "correct_answer": "11",
            "explanation": "Originally 10 Fundamental Duties were added by the 42nd Amendment (1976). An 11th duty was added by the 86th Amendment in 2002, making the total 11.",
            "points": 1
        },
        {
            "id": 5510,
            "topic_id": 55,
            "question": "On which date was the Constitution of India formally adopted by the Constituent Assembly?",
            "options_json": ["26 November 1949", "26 January 1950", "15 August 1947", "9 December 1946"],
            "correct_answer": "26 November 1949",
            "explanation": "The Constitution was adopted on 26 November 1949, now celebrated annually across the nation as Constitution Day (Samvidhan Divas).",
            "points": 1
        }
    ],
    "quiz_questions": [
        {
            "id": 5501,
            "topic_id": 55,
            "question": "Which Part of the Indian Constitution is often described as the 'Magna Carta of India'?",
            "options_json": ["Part III (Fundamental Rights)", "Part IV (DPSP)", "Part IVA (Fundamental Duties)", "Part I (The Union)"],
            "correct_answer": "Part III (Fundamental Rights)",
            "explanation": "Part III (Articles 12 to 35) guarantees justiciable Fundamental Rights and is termed the Magna Carta of India.",
            "points": 1
        },
        {
            "id": 5502,
            "topic_id": 55,
            "question": "Which Article provides for the Organization of Village Panchayats as a Directive Principle?",
            "options_json": ["Article 40", "Article 44", "Article 48", "Article 45"],
            "correct_answer": "Article 40",
            "explanation": "Article 40 directs the State to take steps to organize village panchayats and endow them with powers as units of self-government.",
            "points": 1
        },
        {
            "id": 5503,
            "topic_id": 55,
            "question": "What is the legal status of the Directive Principles of State Policy under Article 37?",
            "options_json": ["Non-justiciable (not enforceable by courts)", "Justiciable (enforceable by Supreme Court)", "Absolute rights", "Supreme over Fundamental Rights"],
            "correct_answer": "Non-justiciable (not enforceable by courts)",
            "explanation": "Article 37 explicitly declares that the provisions contained in Part IV shall not be enforceable by any court.",
            "points": 1
        },
        {
            "id": 5504,
            "topic_id": 55,
            "question": "The 73rd Constitutional Amendment Act of 1992 gave constitutional status to which institution?",
            "options_json": ["Panchayati Raj Institutions", "Municipalities", "Cooperative Societies", "National Development Council"],
            "correct_answer": "Panchayati Raj Institutions",
            "explanation": "The 73rd Amendment Act 1992 inserted Part IX and the 11th Schedule, granting constitutional status to three-tier Panchayati Raj Institutions.",
            "points": 1
        },
        {
            "id": 5505,
            "topic_id": 55,
            "question": "Which writ literally translates to 'We Command' in Latin?",
            "options_json": ["Mandamus", "Habeas Corpus", "Quo-Warranto", "Certiorari"],
            "correct_answer": "Mandamus",
            "explanation": "Mandamus means 'We Command'. It is an order issued by a court to a public authority to perform a mandatory statutory duty.",
            "points": 1
        },
        {
            "id": 5506,
            "topic_id": 55,
            "question": "The idea of 'Concurrent List' in the Seventh Schedule was borrowed from which country's constitution?",
            "options_json": ["Australia", "Canada", "United States", "Ireland"],
            "correct_answer": "Australia",
            "explanation": "The Concurrent List concept was borrowed from the Australian Constitution.",
            "points": 1
        },
        {
            "id": 5507,
            "topic_id": 55,
            "question": "Who was the permanent President of the Constituent Assembly elected in December 1946?",
            "options_json": ["Dr. Rajendra Prasad", "Dr. Sachchidananda Sinha", "Dr. B.R. Ambedkar", "Jawaharlal Nehru"],
            "correct_answer": "Dr. Rajendra Prasad",
            "explanation": "Dr. Sachchidananda Sinha served as temporary chairman on 9 Dec 1946; on 11 Dec 1946, Dr. Rajendra Prasad was elected permanent President.",
            "points": 1
        },
        {
            "id": 5508,
            "topic_id": 55,
            "question": "In which landmark judgment did the Supreme Court propound the 'Basic Structure Doctrine'?",
            "options_json": ["Kesavananda Bharati case (1973)", "Golaknath case (1967)", "Minerva Mills case (1980)", "Maneka Gandhi case (1978)"],
            "correct_answer": "Kesavananda Bharati case (1973)",
            "explanation": "In Kesavananda Bharati v. State of Kerala (1973), a 13-judge bench ruled that Parliament's amending power under Article 368 cannot destroy or alter the 'Basic Structure' of the Constitution.",
            "points": 1
        },
        {
            "id": 5509,
            "topic_id": 55,
            "question": "Which Article provides for the separation of the Judiciary from the Executive in public services of the State?",
            "options_json": ["Article 50", "Article 48", "Article 51", "Article 45"],
            "correct_answer": "Article 50",
            "explanation": "Article 50 directs the State to take steps to separate the judiciary from the executive in the public services of the State.",
            "points": 1
        },
        {
            "id": 5510,
            "topic_id": 55,
            "question": "The 101st Constitutional Amendment Act (2016) is related to which major economic reform in India?",
            "options_json": ["Goods and Services Tax (GST)", "National Judicial Appointments Commission", "Economically Weaker Sections Quota", "Insolvency and Bankruptcy Code"],
            "correct_answer": "Goods and Services Tax (GST)",
            "explanation": "The 101st Amendment Act (2016) paved the way for the implementation of the Goods and Services Tax (GST) across India.",
            "points": 1
        }
    ]
}

ga_part1 = {
    52: topic_52,
    53: topic_53,
    54: topic_54,
    55: topic_55
}

with open("scratch/ga_part1.py", "w", encoding="utf-8") as f:
    f.write("# ga_part1.py\n")
    f.write("GA_PART1_DATA = " + json.dumps(ga_part1, indent=4) + "\n")

print("Successfully written scratch/ga_part1.py with Topics 52 to 55!")
