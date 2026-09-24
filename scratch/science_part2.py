"""General Science Part 2: Topics 65 (Biology) & 66 (Human Body)"""

SCIENCE_PART2_DATA = {
    "65": {
        "title": "Biology: Cell Biology, Whittaker's Five Kingdoms, Plant Physiology, Genetics & Evolution",
        "source_id": 7,
        "content": {
            "definition": "Biology in competitive examinations (UPSC, SSC CGL/CHSL Tier 1/2, RRB NTPC, State PSCs, CDS, NDA) examines living systems, cellular architecture, taxonomy and biological diversity, plant metabolic physiology, molecular genetics, and mechanisms of inheritance and evolutionary adaptation.",
            "overview": "Comprehensive Biological Sciences Framework:\n- Cell Biology (Cytology): Cell Theory (Schleiden, Schwann, Virchow); Prokaryotic vs Eukaryotic cells; Cell Organelles: Nucleus (brain of the cell, contains chromatin & nucleolus), Mitochondria ('Powerhouse of the cell', site of ATP synthesis via Krebs cycle), Chloroplasts ('Kitchen of the cell', site of photosynthesis in plants), Ribosomes ('Protein factories', site of translation, non-membrane bound), Endoplasmic Reticulum (Rough ER with ribosomes synthesizes proteins, Smooth ER synthesizes lipids and detoxifies drugs), Golgi Apparatus (packaging and secretional dispatch), Lysosomes ('Suicide bags' with hydrolytic enzymes), Vacuoles; Cell division: Mitosis (equational division, somatic growth, 2 diploid daughter cells) vs Meiosis (reductional division, gametogenesis, 4 haploid daughter cells, crossing over in Pachytene)\n- Biological Taxonomy & Classification: Carl Linnaeus (Father of Taxonomy, Binomial Nomenclature: *Genus species*); R.H. Whittaker's 5-Kingdom Classification (1969): Monera (unicellular prokaryotes like bacteria, cyanobacteria), Protista (unicellular eukaryotes like Amoeba, Paramecium, Plasmodium), Fungi (heterotrophic, chitinous cell walls, saprophytic molds/mushrooms), Plantae (autotrophic, cellulose cell walls), Animalia (heterotrophic, no cell walls); Plant Kingdom divisions: Thallophyta (algae), Bryophyta (amphibians of plant kingdom, e.g., moss, Riccia), Pteridophyta (ferns, first vascular plants), Gymnosperms (naked seeds, e.g., Cycas, Pinus), Angiosperms (flowering plants with enclosed seeds in fruit)\n- Plant Physiology & Transport: Xylem (conducts water and minerals upward via transpiration pull; dead tracheids and vessels) vs Phloem (translocates organic food bidirectionally; living sieve tubes and companion cells); Photosynthesis ($6\\text{CO}_2 + 12\\text{H}_2\\text{O} \\xrightarrow{\\text{Light, Chlorophyll}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{H}_2\\text{O} + 6\\text{O}_2$; Light reaction in thylakoid grana releasing $\\text{O}_2$ from photolysis of water; Dark/Calvin cycle in stroma fixing $\\text{CO}_2$); Plant Hormones: Auxins (apical dominance, phototropism, discovered by Went), Gibberellins (stem elongation, seed germination), Cytokinins (cell division, delay senescence), Abscisic Acid (ABA, 'stress hormone', causes stomatal closure and leaf abscission), Ethylene (only gaseous plant hormone, promotes fruit ripening)\n- Genetics & Molecular Biology: Gregor Johann Mendel (Father of Genetics, experiments on garden pea *Pisum sativum*, Laws of Segregation and Independent Assortment); DNA Structure (Watson and Crick 1953 double helix; nitrogenous bases: Adenine pairs with Thymine via 2 H-bonds, Guanine pairs with Cytosine via 3 H-bonds); RNA (Ribose sugar, Uracil replaces Thymine); Central Dogma: $\\text{DNA} \\xrightarrow{\\text{Transcription}} \\text{mRNA} \\xrightarrow{\\text{Translation}} \\text{Protein}$; Genetic code is triplet, universal, degenerate; Sex determination in humans (Male XY, Female XX; Y chromosome determines male sex); Genetic disorders (Down syndrome: Trisomy 21; Turner syndrome: 45,XO; Klinefelter syndrome: 47,XXY; Hemophilia & Color Blindness: X-linked recessive)",
            "types": [
                {
                    "name": "1. Cytology & Cell Organelles",
                    "desc": "Cell theory, ultrastructure of plant/animal cells, and specialized organelle functions.",
                    "examples": [
                        "Mitochondria: Powerhouse of the cell (produces ATP through cellular respiration)",
                        "Lysosomes: Suicidal bags (contain acid hydrolytic enzymes for intracellular digestion)",
                        "Ribosomes: Protein factories of the cell (found free or bound to Rough ER)"
                    ]
                },
                {
                    "name": "2. Whittaker's 5 Kingdoms & Taxonomy",
                    "desc": "Classification of living organisms based on cell structure, body organization, and nutrition.",
                    "examples": [
                        "Monera (Bacteria, prokaryotic) • Protista (Amoeba, eukaryotic unicellular)",
                        "Fungi (Molds, mushrooms, chitin wall) • Plantae (Autotrophic) • Animalia (Heterotrophic)"
                    ]
                },
                {
                    "name": "3. Plant Tissues & Vascular Transport",
                    "desc": "Complex permanent tissues responsible for conduction of water, minerals, and nutrients.",
                    "examples": [
                        "Xylem: Transports water and inorganic minerals unidirectionally from roots to leaves",
                        "Phloem: Transports synthesized organic sugars bidirectionally from source to sink"
                    ]
                },
                {
                    "name": "4. Photosynthesis & Plant Phytohormones",
                    "desc": "Light-driven energy capture, water photolysis, and growth regulators.",
                    "examples": [
                        "Oxygen released during photosynthesis originates from water (H₂O), NOT from CO₂",
                        "Auxins (stem elongation, phototropism) • Ethylene (gaseous hormone, fruit ripening)"
                    ]
                },
                {
                    "name": "5. Mendelian Genetics & Molecular DNA",
                    "desc": "Inheritance laws, double-helix structure, protein synthesis, and chromosomal mutations.",
                    "examples": [
                        "DNA Base Pairing: Adenine = Thymine (2 H-bonds), Guanine ≡ Cytosine (3 H-bonds)",
                        "Down Syndrome: Caused by chromosomal non-disjunction resulting in Trisomy 21"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Origin of Photosynthetic Oxygen Rule",
                    "explanation": "In green plant photosynthesis, the oxygen gas ($O_2$) released into the atmosphere is derived strictly from the photolysis (light-dependent cleavage) of WATER ($H_2O$), and NOT from carbon dioxide ($CO_2$). Carbon dioxide is reduced to synthesize glucose.",
                    "words": [
                        "Photosynthesis",
                        "Oxygen from H2O",
                        "Photolysis of water",
                        "CO2 reduced to glucose"
                    ],
                    "correct": "The oxygen liberated during photosynthesis comes from the splitting of water molecules.",
                    "incorrect": "The oxygen released during photosynthesis comes from carbon dioxide molecules."
                },
                {
                    "rule_number": 2,
                    "title": "Mitochondria & Chloroplast Semi-Autonomous Nature Rule",
                    "explanation": "Mitochondria and Chloroplasts are semi-autonomous double-membraned organelles that possess their OWN circular DNA and 70S ribosomes. They can synthesize some of their own proteins and replicate independently within the host cell (Endosymbiotic Theory).",
                    "words": [
                        "Mitochondria",
                        "Chloroplasts",
                        "Semi-autonomous",
                        "Own circular DNA",
                        "70S ribosomes"
                    ],
                    "correct": "Mitochondria and chloroplasts contain their own circular DNA and protein-synthesizing ribosomes.",
                    "incorrect": "Mitochondria and chloroplasts rely entirely on nuclear DNA and have no genetic material of their own."
                },
                {
                    "rule_number": 3,
                    "title": "Plant Phytohormone Functional Specificity Rule",
                    "explanation": "Auxin promotes apical dominance and causes bending towards light (phototropism); Gibberellins break seed dormancy and cause internode elongation; Cytokinins promote cell division; Abscisic acid (ABA) is a growth inhibitor ('stress hormone' closing stomata); Ethylene is the UNIQUE GASEOUS hormone causing fruit ripening.",
                    "words": [
                        "Auxin phototropism",
                        "Ethylene gaseous ripening",
                        "ABA stress hormone",
                        "Cytokinin cell division"
                    ],
                    "correct": "Ethylene is the only gaseous phytohormone naturally responsible for ripening of fruits.",
                    "incorrect": "Auxin is a gaseous hormone used for fruit ripening."
                },
                {
                    "rule_number": 4,
                    "title": "Xylem vs. Phloem Directional Transport Rule",
                    "explanation": "Xylem transports water and dissolved mineral nutrients UNIDIRECTIONALLY from roots upwards to stems and leaves via negative pressure transpiration pull. Phloem translocates dissolved organic solutes (sucrose) BIDIRECTIONALLY from leaves (source) to storage organs or growing buds (sink).",
                    "words": [
                        "Xylem water unidirectional",
                        "Phloem food bidirectional",
                        "Transpiration pull",
                        "Source to sink"
                    ],
                    "correct": "Water transport in xylem is strictly unidirectional (upward), whereas translocation in phloem is bidirectional.",
                    "incorrect": "Xylem transports organic food bidirectionally, while phloem transports water only downwards."
                },
                {
                    "rule_number": 5,
                    "title": "DNA vs. RNA Nitrogenous Base Complementarity Rule",
                    "explanation": "DNA contains four nitrogenous bases: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C). In RNA, THYMINE IS REPLACED BY URACIL (U). Complementary pairing: In DNA, A pairs with T (2 H-bonds) and G with C (3 H-bonds). In RNA, A pairs with U.",
                    "words": [
                        "DNA ATGC",
                        "RNA AUGC",
                        "Thymine replaced by Uracil",
                        "Watson Crick pairing"
                    ],
                    "correct": "RNA contains Uracil in place of Thymine.",
                    "incorrect": "RNA contains Thymine in place of Uracil, or Guanine is absent in RNA."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Thinking that all plant cells have chloroplasts.",
                    "correction": "Chloroplasts are present only in green photosynthetic cells (like leaf mesophyll). Non-green plant cells, such as underground root cells and internal bark cells, do not contain chloroplasts (they contain non-pigmented leucoplasts).",
                    "rationale": "Candidates mistakenly generalize green leaf characteristics to every anatomical cell of a plant."
                },
                {
                    "mistake": "Confusing Mitosis with Meiosis daughter cell chromosome numbers.",
                    "correction": "Mitosis produces 2 genetically identical diploid ($2n$) daughter cells. Meiosis produces 4 genetically varied haploid ($n$) daughter cells.",
                    "rationale": "Meiosis is a reductional division essential for gamete formation, whereas mitosis is an equational division for growth."
                },
                {
                    "mistake": "Believing viruses belong to Whittaker's Monera kingdom.",
                    "correction": "Viruses are acellular and non-living outside a host cell. Because they lack cellular structure and metabolic machinery, they are NOT placed in any of Whittaker's 5 kingdoms.",
                    "rationale": "Viruses occupy a twilight zone between living and non-living matter and are excluded from cellular classification."
                },
                {
                    "mistake": "Assuming human male sex is determined by the mother's egg.",
                    "correction": "All human female ova carry an X chromosome ($22+X$). Human male sperm cells carry either an X ($22+X$) or a Y ($22+Y$) chromosome in equal proportion (50:50). The father's sperm cell determines the chromosomal sex of the offspring.",
                    "rationale": "The presence or absence of the Y chromosome (specifically the SRY gene) determines male testicular development."
                }
            ],
            "quick_revision_points": [
                "Cell Theory: Proposed by Matthias Schleiden and Theodor Schwann (1838-39); Rudolf Virchow added 'Omnis cellula e cellula' (all cells arise from pre-existing cells).",
                "Mitochondria: Powerhouse of the cell; produces ATP via cellular respiration. Contains own circular DNA and 70S ribosomes.",
                "Chloroplasts: Kitchen of the cell; site of photosynthesis. Contains green pigment Chlorophyll (which contains Magnesium ion at its center).",
                "Ribosomes: Protein factories; synthesized in nucleolus. Lack membrane; 70S in prokaryotes, 80S in eukaryotes.",
                "Lysosomes: Suicidal bags containing acid hydrolytic enzymes (active at pH ~5.0) that digest foreign pathogens and worn-out organelles.",
                "Whittaker's 5 Kingdoms (1969): Monera (prokaryotes), Protista (unicellular eukaryotes), Fungi (chitin wall), Plantae (cellulose wall), Animalia (no cell wall).",
                "Bryophytes: Known as the 'Amphibians of the Plant Kingdom' because they live in soil but depend on water for sexual reproduction (e.g., Mosses, Marchantia).",
                "Xylem vs Phloem: Xylem conducts water/minerals upward unidirectionally. Phloem translocates sucrose bidirectionally.",
                "Photosynthesis: Oxygen liberated is released by the photolysis of water ($H_2O$), driven by sunlight captured by chlorophyll.",
                "Phytohormones: Auxin (phototropism/apical dominance), Gibberellin (seed germination/stem elongation), Cytokinin (cell division), ABA (stress hormone/stomata closure), Ethylene (fruit ripening gas).",
                "Father of Genetics: Gregor Johann Mendel (worked on garden peas, *Pisum sativum*).",
                "DNA Structure: Discovered by Watson and Crick (1953 double helix). Bases: A pairs with T (2 H-bonds); G pairs with C (3 H-bonds).",
                "RNA: Single-stranded; contains ribose sugar and Uracil (U) instead of Thymine (T).",
                "Human Karyotype: 23 pairs of chromosomes (46 total): 22 pairs of autosomes and 1 pair of allosomes/sex chromosomes (XX female, XY male)."
            ]
        },
        "previous_year_questions": [
            {
                "id": 6501,
                "topic_id": 65,
                "exam_id": 1,
                "question": "Which cell organelle is commonly referred to as the 'Powerhouse of the Cell' due to its generation of ATP? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Endoplasmic Reticulum",
                    "Mitochondria",
                    "Golgi Apparatus",
                    "Ribosome"
                ],
                "correct_answer": "Mitochondria",
                "explanation": "Mitochondria generate most of the chemical energy required by the cell through cellular aerobic respiration, storing it in the form of Adenosine Triphosphate (ATP), which is why they are called the powerhouses of the cell.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6502,
                "topic_id": 65,
                "exam_id": 1,
                "question": "The oxygen liberated into the atmosphere during green plant photosynthesis originates from which of the following? [UPSC CDS 2022]",
                "options_json": [
                    "Water (H₂O)",
                    "Carbon Dioxide (CO₂)",
                    "Glucose",
                    "Chlorophyll"
                ],
                "correct_answer": "Water (H₂O)",
                "explanation": "During the light reaction of photosynthesis, water molecules undergo photolysis in the thylakoid lumen of chloroplasts: 2H₂O -> 4H⁺ + 4e⁻ + O₂. The released oxygen originates entirely from water, as demonstrated experimentally by Ruben and Kamen using oxygen isotope O-18.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6503,
                "topic_id": 65,
                "exam_id": 1,
                "question": "Which of the following plant hormones is unique in existing naturally in a gaseous state and promoting fruit ripening? [RRB NTPC 2021]",
                "options_json": [
                    "Auxin",
                    "Gibberellin",
                    "Ethylene",
                    "Abscisic Acid"
                ],
                "correct_answer": "Ethylene",
                "explanation": "Ethylene (C₂H₄) is the only naturally occurring gaseous plant hormone. It stimulates fruit ripening, breaking of dormancy, and abscission of leaves and flowers.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 6501,
                "topic_id": 65,
                "question": "Which metallic mineral element is present as an essential component in the central porphyrin ring of the chlorophyll molecule?",
                "options_json": [
                    "Iron",
                    "Magnesium",
                    "Calcium",
                    "Zinc"
                ],
                "correct_answer": "Magnesium",
                "explanation": "Magnesium (Mg²⁺) is the central metal ion coordinated within the porphyrin ring of the green photosynthetic pigment chlorophyll. Its deficiency causes chlorosis (yellowing of leaves).",
                "points": 1
            },
            {
                "id": 6502,
                "topic_id": 65,
                "question": "Which plant group is commonly referred to as the 'Amphibians of the Plant Kingdom'?",
                "options_json": [
                    "Thallophyta (Algae)",
                    "Bryophyta (Mosses)",
                    "Pteridophyta (Ferns)",
                    "Gymnosperms"
                ],
                "correct_answer": "Bryophyta (Mosses)",
                "explanation": "Bryophytes (mosses and liverworts) grow on land in damp, shaded habitats but rely on external water for the flagellated antherozoids to swim to the archegonium for fertilization, earning them the title 'amphibians of the plant kingdom'.",
                "points": 1
            },
            {
                "id": 6503,
                "topic_id": 65,
                "question": "In the DNA double helix, the purine base Adenine pairs with which pyrimidine base through two hydrogen bonds?",
                "options_json": [
                    "Cytosine",
                    "Thymine",
                    "Guanine",
                    "Uracil"
                ],
                "correct_answer": "Thymine",
                "explanation": "According to Chargaff's rules and Watson-Crick model, Adenine (A) always pairs with Thymine (T) via two hydrogen bonds (A=T), and Guanine (G) pairs with Cytosine (C) via three hydrogen bonds (G≡C).",
                "points": 1
            },
            {
                "id": 6504,
                "topic_id": 65,
                "question": "Which specialized cell organelle contains digestive hydrolytic enzymes capable of digesting worn-out cellular parts, earning the name 'Suicidal Bag'?",
                "options_json": [
                    "Ribosome",
                    "Lysosome",
                    "Peroxisome",
                    "Centrosome"
                ],
                "correct_answer": "Lysosome",
                "explanation": "Lysosomes are spherical membrane-bound vesicles filled with hydrolytic enzymes. If a cell is damaged or starves, lysosomes can rupture and digest their own host cell, hence termed 'suicidal bags'.",
                "points": 1
            },
            {
                "id": 6505,
                "topic_id": 65,
                "question": "Which plant vascular tissue is responsible for transporting dissolved organic nutrients (sugars) bidirectionally from photosynthetic leaves to other tissues?",
                "options_json": [
                    "Xylem",
                    "Phloem",
                    "Cambium",
                    "Collenchyma"
                ],
                "correct_answer": "Phloem",
                "explanation": "Phloem conducts synthesized organic solutes (sucrose) through its living sieve tube elements and companion cells in a bidirectional manner from source (leaves) to sink (roots, fruits, buds).",
                "points": 1
            },
            {
                "id": 6506,
                "topic_id": 65,
                "question": "Down syndrome in humans is caused by which chromosomal anomaly?",
                "options_json": [
                    "Monosomy of X chromosome",
                    "Trisomy of chromosome 21",
                    "Trisomy of chromosome 18",
                    "Deletion of chromosome 5"
                ],
                "correct_answer": "Trisomy of chromosome 21",
                "explanation": "Down syndrome (mongolism) is a genetic disorder caused by the presence of all or part of a third copy of chromosome 21 (Trisomy 21), leading to characteristic physical features and intellectual disability.",
                "points": 1
            },
            {
                "id": 6507,
                "topic_id": 65,
                "question": "Who is globally recognized as the 'Father of Genetics' for formulating the fundamental laws of biological inheritance?",
                "options_json": [
                    "Charles Darwin",
                    "Gregor Johann Mendel",
                    "Thomas Hunt Morgan",
                    "Hugo de Vries"
                ],
                "correct_answer": "Gregor Johann Mendel",
                "explanation": "Gregor Johann Mendel conducted hybridization experiments on garden pea plants (Pisum sativum) between 1856 and 1863, establishing the basic principles of heredity.",
                "points": 1
            },
            {
                "id": 6508,
                "topic_id": 65,
                "question": "Which plant hormone acts as a growth inhibitor and 'stress hormone' by inducing stomatal closure during drought?",
                "options_json": [
                    "Gibberellin",
                    "Cytokinin",
                    "Abscisic Acid (ABA)",
                    "Auxin"
                ],
                "correct_answer": "Abscisic Acid (ABA)",
                "explanation": "Abscisic acid (ABA) is called the stress hormone because it inhibits plant growth, induces bud dormancy, and stimulates rapid closure of stomata to prevent excessive transpirational water loss during water scarcity.",
                "points": 1
            },
            {
                "id": 6509,
                "topic_id": 65,
                "question": "Which nitrogenous base is present in ribonucleic acid (RNA) in place of Thymine?",
                "options_json": [
                    "Uracil",
                    "Guanine",
                    "Cytosine",
                    "Adenine"
                ],
                "correct_answer": "Uracil",
                "explanation": "In RNA, the pyrimidine base Uracil (U) replaces Thymine (T) and pairs complementarily with Adenine (A).",
                "points": 1
            },
            {
                "id": 6510,
                "topic_id": 65,
                "question": "How many total daughter cells are produced at the completion of a full meiotic cell division cycle?",
                "options_json": [
                    "2 Diploid daughter cells",
                    "4 Haploid daughter cells",
                    "2 Haploid daughter cells",
                    "8 Diploid daughter cells"
                ],
                "correct_answer": "4 Haploid daughter cells",
                "explanation": "Meiosis consists of two successive nuclear divisions (Meiosis I and Meiosis II) following a single round of DNA replication, yielding 4 haploid (n) daughter cells from one diploid (2n) parent germ cell.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 6501,
                "topic_id": 65,
                "question": "Who proposed the Five-Kingdom classification system of living organisms in 1969?",
                "options_json": [
                    "Carl Linnaeus",
                    "Robert H. Whittaker",
                    "Ernst Haeckel",
                    "Carl Woese"
                ],
                "correct_answer": "Robert H. Whittaker",
                "explanation": "R.H. Whittaker proposed the Five-Kingdom classification (Monera, Protista, Fungi, Plantae, Animalia) in 1969 based on cell structure, body organization, and mode of nutrition.",
                "points": 1
            },
            {
                "id": 6502,
                "topic_id": 65,
                "question": "Which cell organelle is the primary site of biological protein synthesis in living cells?",
                "options_json": [
                    "Ribosome",
                    "Centrosome",
                    "Peroxisome",
                    "Lysosome"
                ],
                "correct_answer": "Ribosome",
                "explanation": "Ribosomes read mRNA transcripts and translate nucleotide codons into polypeptide chains of amino acids, earning them the title of 'protein factories'.",
                "points": 1
            },
            {
                "id": 6503,
                "topic_id": 65,
                "question": "The bending of plant stems toward light (phototropism) is primarily mediated by the redistribution of which plant hormone?",
                "options_json": [
                    "Auxin",
                    "Gibberellin",
                    "Ethylene",
                    "Cytokinin"
                ],
                "correct_answer": "Auxin",
                "explanation": "Auxins synthesized at the shoot apex migrate to the shaded side of the stem, stimulating faster cell elongation on the shaded side and causing the stem to bend toward the light.",
                "points": 1
            },
            {
                "id": 6504,
                "topic_id": 65,
                "question": "Which cell wall constituent is the primary polysaccharide found in plant cell walls?",
                "options_json": [
                    "Cellulose",
                    "Chitin",
                    "Peptidoglycan",
                    "Glycogen"
                ],
                "correct_answer": "Cellulose",
                "explanation": "Plant cell walls are primarily constructed of cellulose (a polymer of beta-D-glucose). Fungal cell walls are made of chitin, and bacterial walls of peptidoglycan.",
                "points": 1
            },
            {
                "id": 6505,
                "topic_id": 65,
                "question": "Who is credited with discovering the double-helical structure of DNA in 1953?",
                "options_json": [
                    "James Watson and Francis Crick",
                    "Gregor Mendel and Hugo de Vries",
                    "Robert Brown and Antonie van Leeuwenhoek",
                    "Louis Pasteur and Robert Koch"
                ],
                "correct_answer": "James Watson and Francis Crick",
                "explanation": "James Watson and Francis Crick proposed the double helix model of DNA in 1953, utilizing X-ray crystallography data produced by Rosalind Franklin and Maurice Wilkins.",
                "points": 1
            },
            {
                "id": 6506,
                "topic_id": 65,
                "question": "Which organism exhibits prokaryotic cellular organization?",
                "options_json": [
                    "Bacteria",
                    "Amoeba",
                    "Spirogyra",
                    "Yeast"
                ],
                "correct_answer": "Bacteria",
                "explanation": "Bacteria are prokaryotes lacking a membrane-bound nucleus and membrane-bound organelles. Amoeba, Spirogyra, and Yeast are all eukaryotic.",
                "points": 1
            },
            {
                "id": 6507,
                "topic_id": 65,
                "question": "Which stage of meiotic cell division is characterized by crossing over and genetic recombination between non-sister chromatids?",
                "options_json": [
                    "Pachytene",
                    "Leptotene",
                    "Zygotene",
                    "Diplotene"
                ],
                "correct_answer": "Pachytene",
                "explanation": "Crossing over, where non-sister chromatids exchange genetic segments via the recombinase enzyme complex, occurs during the Pachytene substage of Prophase I.",
                "points": 1
            },
            {
                "id": 6508,
                "topic_id": 65,
                "question": "The conversion of atmospheric nitrogen gas into usable nitrates by Rhizobium bacteria in leguminous root nodules is called:",
                "options_json": [
                    "Nitrogen Fixation",
                    "Nitrification",
                    "Denitrification",
                    "Ammonification"
                ],
                "correct_answer": "Nitrogen Fixation",
                "explanation": "Nitrogen fixation is the biological reduction of inert atmospheric N₂ into ammonia (NH₃) and nitrates by the nitrogenase enzyme in diazotrophic bacteria like Rhizobium.",
                "points": 1
            },
            {
                "id": 6509,
                "topic_id": 65,
                "question": "Which of the following is an example of an insectivorous (carnivorous) plant?",
                "options_json": [
                    "Pitcher plant (Nepenthes)",
                    "Cuscuta (Dodder)",
                    "Sandalwood tree",
                    "Mistletoe"
                ],
                "correct_answer": "Pitcher plant (Nepenthes)",
                "explanation": "Nepenthes (Pitcher plant), Venus flytrap (Dionaea), and Sundew (Drosera) trap and digest insects to obtain nitrogen in nutrient-poor acidic bog soils.",
                "points": 1
            },
            {
                "id": 6510,
                "topic_id": 65,
                "question": "How many total chromosomes are present in a normal human diploid somatic cell?",
                "options_json": [
                    "23",
                    "46",
                    "44",
                    "48"
                ],
                "correct_answer": "46",
                "explanation": "Human somatic cells contain 23 pairs of chromosomes, totaling 46 chromosomes (44 autosomes and 2 sex chromosomes).",
                "points": 1
            },
            {
                "id": 6511,
                "topic_id": 65,
                "question": "The cell organelle that packages, modifies, and sorts macromolecules for cellular secretion is the:",
                "options_json": [
                    "Golgi Apparatus",
                    "Peroxisome",
                    "Centriole",
                    "Mitochondrion"
                ],
                "correct_answer": "Golgi Apparatus",
                "explanation": "The Golgi apparatus (discovered by Camillo Golgi in 1898) packages proteins and lipids synthesized in the ER and directs them to their target destinations.",
                "points": 1
            },
            {
                "id": 6512,
                "topic_id": 65,
                "question": "Which cellular component is found in plant cells but strictly absent in animal cells?",
                "options_json": [
                    "Cell Wall and Chloroplasts",
                    "Mitochondria",
                    "Ribosomes",
                    "Endoplasmic Reticulum"
                ],
                "correct_answer": "Cell Wall and Chloroplasts",
                "explanation": "Plant cells have a rigid cellulose cell wall and plastids (chloroplasts), whereas animal cells have only a flexible plasma membrane and lack plastids.",
                "points": 1
            },
            {
                "id": 6513,
                "topic_id": 65,
                "question": "In humans, sex-linked genetic disorders such as Hemophilia and Red-Green Color Blindness are inherited as:",
                "options_json": [
                    "X-linked recessive traits",
                    "Y-linked dominant traits",
                    "Autosomal dominant traits",
                    "Mitochondrial traits"
                ],
                "correct_answer": "X-linked recessive traits",
                "explanation": "Hemophilia and Red-Green Color Blindness are caused by recessive mutations on the X chromosome. Males (XY) expressing the mutant allele show the condition because they have only one X chromosome.",
                "points": 1
            },
            {
                "id": 6514,
                "topic_id": 65,
                "question": "Which of the following is considered an acellular infectious agent excluded from the Whittaker classification?",
                "options_json": [
                    "Virus",
                    "Cyanobacteria",
                    "Paramecium",
                    "Algae"
                ],
                "correct_answer": "Virus",
                "explanation": "Viruses consist only of a nucleic acid core (DNA or RNA) wrapped in a protein capsid, lacking cellular machinery, and are not placed in any kingdom.",
                "points": 1
            },
            {
                "id": 6515,
                "topic_id": 65,
                "question": "Which enzyme in saliva begins the chemical digestion of dietary starches into maltose sugar in the mouth?",
                "options_json": [
                    "Salivary Amylase (Ptyalin)",
                    "Pepsin",
                    "Lipase",
                    "Trypsin"
                ],
                "correct_answer": "Salivary Amylase (Ptyalin)",
                "explanation": "Salivary amylase (ptyalin), secreted by salivary glands, hydrolyzes complex starches into maltose at an optimum pH of approximately 6.8.",
                "points": 1
            },
            {
                "id": 6516,
                "topic_id": 65,
                "question": "The loss of water in the form of water vapor from aerial plant parts, primarily through stomata, is termed:",
                "options_json": [
                    "Transpiration",
                    "Guttation",
                    "Exudation",
                    "Precipitation"
                ],
                "correct_answer": "Transpiration",
                "explanation": "Transpiration is the evaporative loss of water from plant leaves through open stomata, generating the suction force (transpiration pull) that drives upward water transport in xylem.",
                "points": 1
            },
            {
                "id": 6517,
                "topic_id": 65,
                "question": "Yeast, widely used in baking bread and brewing alcoholic beverages, belongs to which biological kingdom?",
                "options_json": [
                    "Fungi",
                    "Plantae",
                    "Monera",
                    "Protista"
                ],
                "correct_answer": "Fungi",
                "explanation": "Yeast (such as Saccharomyces cerevisiae) is a unicellular fungus capable of anaerobic alcoholic fermentation of sugars into ethanol and carbon dioxide.",
                "points": 1
            },
            {
                "id": 6518,
                "topic_id": 65,
                "question": "Which plant tissue retains the persistent capacity for continuous mitotic cell division and growth throughout the plant's life?",
                "options_json": [
                    "Meristematic tissue",
                    "Parenchyma tissue",
                    "Sclerenchyma tissue",
                    "Collenchyma tissue"
                ],
                "correct_answer": "Meristematic tissue",
                "explanation": "Meristematic tissues (apical, intercalary, and lateral meristems) consist of actively dividing undifferentiated cells responsible for primary and secondary plant growth.",
                "points": 1
            },
            {
                "id": 6519,
                "topic_id": 65,
                "question": "In Carl Linnaeus's system of Binomial Nomenclature, the scientific name of an organism consists of which two designations?",
                "options_json": [
                    "Genus and Species",
                    "Family and Order",
                    "Class and Phylum",
                    "Kingdom and Variety"
                ],
                "correct_answer": "Genus and Species",
                "explanation": "Binomial nomenclature gives every organism a two-part Latinized name: the capitalized Genus name followed by the lowercase specific epithet (Species), e.g., Homo sapiens.",
                "points": 1
            },
            {
                "id": 6520,
                "topic_id": 65,
                "question": "What is the primary function of stomata located on the epidermal surface of plant leaves?",
                "options_json": [
                    "Gas exchange (CO₂ and O₂) and transpirational water loss",
                    "Absorption of mineral ions from rain",
                    "Mechanical support against wind",
                    "Secretion of defensive alkaloids"
                ],
                "correct_answer": "Gas exchange (CO₂ and O₂) and transpirational water loss",
                "explanation": "Stomata are microscopic pores flanked by guard cells that regulate the intake of CO₂ for photosynthesis, release of O₂, and vapor loss during transpiration.",
                "points": 1
            }
        ]
    },
    "66": {
        "title": "Human Body: Organ Systems, Circulation, Nervous System, Endocrine Hormones, Nutrition & Deficiency Diseases",
        "source_id": 7,
        "content": {
            "definition": "Human Anatomy and Physiology in competitive examinations (UPSC, SSC CGL/CHSL Tier 1/2, RRB NTPC, State PSCs, CDS, NDA) covers the structure and integrated functioning of human organ systems: circulatory and blood groups, nervous coordination and brain architecture, digestive enzymes, endocrine glands and hormonal homeostasis, respiratory gas exchange, renal excretion, and nutritional vitamins and deficiency disorders.",
            "overview": "Comprehensive Human Physiology Framework:\n- Circulatory System & Blood: Four-chambered heart (2 atria, 2 ventricles); Double circulation (systemic and pulmonary); Pacemaker of heart is SA Node (Sinoatrial node) generating electrical impulses; Blood composition: Plasma ($55\\%$), Formed elements ($45\\%$ - RBCs/Erythrocytes [contain iron-rich Haemoglobin, lifespan ~120 days, graveyard is Spleen], WBCs/Leukocytes [defense, granular vs agranular], Platelets/Thrombocytes [blood clotting with Prothrombin, Fibrinogen, Calcium and Vitamin K]); Blood Groups (Karl Landsteiner 1900): ABO system (Type O is Universal Donor, Type AB is Universal Recipient); Rh Factor (Rhesus factor, Rh incompatibility causes Erythroblastosis Fetalis in second Rh-positive child of Rh-negative mother)\n- Nervous System & Sense Organs: Central Nervous System (Brain and Spinal Cord) vs Peripheral Nervous System; Human Brain: Forebrain (Cerebrum [largest part, seat of intelligence, memory, voluntary actions], Thalamus, Hypothalamus [regulates body temperature, hunger, thirst, sleep, pituitary control]), Midbrain (vision and hearing reflexes), Hindbrain (Cerebellum [coordinates voluntary movement, posture, and balance], Pons, Medulla Oblongata [involuntary cardiac, respiratory, swallowing, and vomiting centers]); Structural unit: Neuron (Dendrite -> Cyton -> Axon -> Synapse with neurotransmitters like Acetylcholine); Reflex Arc\n- Digestive System & Enzymatic Hydrolysis: Alimentary canal (Mouth -> Pharynx -> Esophagus -> Stomach -> Small Intestine [Duodenum, Jejunum, Ileum, longest segment, site of complete digestion and nutrient absorption via villi] -> Large Intestine -> Rectum); Digestive Glands: Salivary glands (Salivary amylase/ptyalin digests starch into maltose), Stomach gastric juice (HCl provides acidic pH ~1.5-2.0 and kills microbes; Pepsin digests proteins into peptones; Mucus protects stomach lining), Liver (largest gland, secretes Bile juice which has NO enzymes but emulsifies fats; stores glycogen), Pancreas (dual endocrine/exocrine gland; Trypsin digests proteins, Pancreatic Amylase digests starch, Lipase digests emulsified fats)\n- Endocrine System & Hormones: Pituitary Gland ('Master Gland', secretes Growth Hormone / GH [dwarfism/gigantism], TSH, ACTH, Oxytocin [milk ejection, labor contractions], Vasopressin/ADH [water reabsorption in kidney tubules]); Thyroid Gland (secretes Thyroxine requiring Iodine; deficiency causes Goitre and Cretinism); Adrenal Glands ('Emergency glands' on top of kidneys, secrete Adrenaline / Epinephrine for 'Fight-or-Flight' response); Pancreas Islets of Langerhans (Beta cells secrete Insulin [lowers blood glucose by converting it to glycogen; deficiency causes Diabetes Mellitus], Alpha cells secrete Glucagon [raises blood glucose]); Parathyroid (PTH, regulates blood calcium)\n- Excretory & Respiratory Systems: Functional unit of Kidney is Nephron (~1 million per kidney; Bowman's capsule, Glomerulus [ultrafiltration], Henle's loop, Collecting duct); Primary nitrogenous waste in humans is Urea (synthesized in liver via Ornithine cycle); Lungs (Alveoli are structural units of gas exchange; Haemoglobin carries oxygen as Oxyhaemoglobin)\n- Vitamins & Deficiency Diseases: Fat-Soluble (A, D, E, K) vs Water-Soluble (B-Complex, C); Vitamin A (Retinol - Night Blindness / Xerophthalmia), Vitamin B1 (Thiamine - Beriberi), Vitamin B2 (Riboflavin - Cheilosis/glossitis), Vitamin B3 (Niacin - Pellagra), Vitamin B12 (Cyanocobalamin [contains Cobalt] - Pernicious Anemia), Vitamin C (Ascorbic Acid - Scurvy, bleeding gums; destroyed by heating), Vitamin D (Calciferol - Rickets in children, Osteomalacia in adults; synthesized in skin under sunlight), Vitamin E (Tocopherol - sterility/muscle weakness), Vitamin K (Phylloquinone - impaired blood clotting)",
            "types": [
                {
                    "name": "1. Circulatory System & Blood Components",
                    "desc": "Cardiac cycle, heart chambers, blood cellular constituents, and ABO/Rh groups.",
                    "examples": [
                        "RBCs: Lifespan ~120 days, contain iron-rich hemoglobin, destroyed in the Spleen",
                        "Blood Groups: Type O negative is Universal Donor; Type AB positive is Universal Recipient",
                        "Pacemaker: SA Node initiates normal rhythmic cardiac contractions"
                    ]
                },
                {
                    "name": "2. Nervous System & Brain Anatomy",
                    "desc": "Functional divisions of brain, voluntary control, involuntary centers, and reflex arcs.",
                    "examples": [
                        "Cerebrum: Seat of consciousness, intelligence, memory, and cognitive thought",
                        "Cerebellum: Coordinates voluntary muscle movements, posture, and bodily balance",
                        "Medulla Oblongata: Controls involuntary cardiovascular and respiratory reflexes"
                    ]
                },
                {
                    "name": "3. Digestive Glands & Enzymatic Catalysis",
                    "desc": "Gastrointestinal tract organs, digestive secretions, and nutrient absorption.",
                    "examples": [
                        "Liver: Largest internal organ/gland; produces bile to emulsify dietary fats",
                        "Small Intestine: Complete digestion occurs here, nutrients absorbed through villi",
                        "Stomach: Secretes HCl (pH 1.5-2.0) and pepsin for protein breakdown"
                    ]
                },
                {
                    "name": "4. Endocrine Glands & Hormonal Homeostasis",
                    "desc": "Ductless glands secreting chemical messengers directly into the bloodstream.",
                    "examples": [
                        "Pituitary: Master endocrine gland controlling thyroid, adrenals, and gonads",
                        "Insulin: Secreted by Beta cells of pancreatic islets to lower blood glucose",
                        "Adrenaline: Fight-or-flight emergency hormone secreted by adrenal medulla"
                    ]
                },
                {
                    "name": "5. Vitamins, Minerals & Deficiency Diseases",
                    "desc": "Essential micronutrients, biochemical roles, and pathological deficiency states.",
                    "examples": [
                        "Vitamin C (Ascorbic Acid): Prevents Scurvy; readily destroyed by cooking heat",
                        "Vitamin D (Calciferol): Sunlight vitamin preventing Rickets and Osteomalacia",
                        "Vitamin B12 (Cobalamin): Contains Cobalt; prevents Pernicious Anemia"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Universal Blood Donor vs. Recipient Rule",
                    "explanation": "Type O Negative ($O^-$) is the true Universal Donor because its RBCs lack A, B, and Rh surface antigens, avoiding agglutination in any recipient. Type AB Positive ($AB^+$) is the true Universal Recipient because its plasma lacks Anti-A, Anti-B, and Anti-Rh antibodies.",
                    "words": [
                        "O Negative Universal Donor",
                        "AB Positive Universal Recipient",
                        "No Antigens",
                        "No Antibodies"
                    ],
                    "correct": "Blood group O-negative is the universal donor, and AB-positive is the universal recipient.",
                    "incorrect": "Blood group AB is the universal donor, and group O is the universal recipient."
                },
                {
                    "rule_number": 2,
                    "title": "Brain Region Functional Allocation Rule",
                    "explanation": "Cerebrum controls intelligence, thinking, memory, and voluntary decisions. Cerebellum coordinates muscle balance, posture, and motor coordination (affected by alcohol intoxication). Medulla Oblongata controls vital involuntary autonomic reflexes (heartbeat, breathing, blood pressure). Hypothalamus controls body temperature (thermostat), hunger, thirst, and pituitary hormone release.",
                    "words": [
                        "Cerebrum intelligence",
                        "Cerebellum balance posture",
                        "Medulla involuntary",
                        "Hypothalamus temperature"
                    ],
                    "correct": "The cerebellum is responsible for maintaining body balance and coordinating voluntary motor movement.",
                    "incorrect": "The cerebrum is responsible for maintaining physical posture and balance."
                },
                {
                    "rule_number": 3,
                    "title": "Bile Juice Unique Composition Rule",
                    "explanation": "Bile juice, synthesized continuously by the LIVER and stored/concentrated in the GALLBLADDER, contains NO DIGESTIVE ENZYMES. Its active ingredients are bile salts (sodium glycocholate and taurocholate) that emulsify large fat globules into tiny droplets for lipase action, and bile pigments (bilirubin and biliverdin).",
                    "words": [
                        "Bile synthesized in Liver",
                        "Stored in Gallbladder",
                        "Contains NO enzymes",
                        "Emulsifies fats"
                    ],
                    "correct": "Bile juice contains no enzymes but is essential for emulsifying fats in the duodenum.",
                    "incorrect": "Bile juice is secreted by the pancreas and contains powerful protein-digesting enzymes."
                },
                {
                    "rule_number": 4,
                    "title": "Fat-Soluble vs. Water-Soluble Vitamins Rule",
                    "explanation": "Vitamins A, D, E, and K are FAT-SOLUBLE (stored in liver and adipose tissue; excess can cause hypervitaminosis). Vitamins B-Complex and C are WATER-SOLUBLE (cannot be stored in the body and must be supplied regularly in the diet; excess is excreted in urine).",
                    "words": [
                        "ADEK fat-soluble stored in liver",
                        "B and C water-soluble excreted in urine"
                    ],
                    "correct": "Vitamins A, D, E, and K are fat-soluble, whereas Vitamins B and C are water-soluble.",
                    "incorrect": "Vitamin C is a fat-soluble vitamin stored long-term in the liver."
                },
                {
                    "rule_number": 5,
                    "title": "Insulin vs. Glucagon Glycemic Control Rule",
                    "explanation": "Both are secreted by the Islets of Langerhans in the Pancreas. INSULIN (from Beta cells) LOWERS blood glucose by stimulating cellular uptake and converting excess glucose into glycogen (glycogenesis). GLUCAGON (from Alpha cells) RAISES blood glucose by breaking down glycogen into glucose (glycogenolysis).",
                    "words": [
                        "Insulin Beta cells lowers glucose",
                        "Glucagon Alpha cells raises glucose",
                        "Diabetes Mellitus"
                    ],
                    "correct": "Insulin lowers blood sugar by converting glucose into liver glycogen; deficiency causes Diabetes Mellitus.",
                    "incorrect": "Insulin raises blood glucose levels when the body is fasting."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Thinking the heart's left ventricle pumps deoxygenated blood to the lungs.",
                    "correction": "The Right Ventricle pumps deoxygenated blood through the pulmonary artery to the lungs. The Left Ventricle pumps oxygenated blood through the aorta to the entire systemic body under high pressure.",
                    "rationale": "Candidates confuse the right and left sides of the heart: Right side = Deoxygenated, Left side = Oxygenated."
                },
                {
                    "mistake": "Assuming Vitamin C deficiency causes Rickets.",
                    "correction": "Vitamin C deficiency causes Scurvy (bleeding gums, skin spots, delayed wound healing). Vitamin D deficiency causes Rickets in growing children.",
                    "rationale": "Associating the wrong letter vitamin with skeletal vs. connective tissue collagen disorders."
                },
                {
                    "mistake": "Believing that insulin is secreted by the liver.",
                    "correction": "Insulin is an endocrine peptide hormone produced exclusively by the Beta cells of the Islets of Langerhans in the Pancreas (the liver only responds to insulin by storing glycogen).",
                    "rationale": "Liver is the target organ for glucose storage, but pancreas is the endocrine glandular source."
                },
                {
                    "mistake": "Confusing Endocrine with Exocrine glands.",
                    "correction": "Endocrine glands are ductless glands secreting hormones directly into the blood (e.g., thyroid, pituitary, adrenal). Exocrine glands have ducts secreting fluids onto surfaces (e.g., salivary, sweat, sebaceous glands).",
                    "rationale": "The presence or absence of a duct system defines the anatomical classification."
                }
            ],
            "quick_revision_points": [
                "Circulatory: Human heart has 4 chambers. Normal resting blood pressure = 120/80 mmHg (systolic/diastolic, measured using a Sphygmomanometer).",
                "Pacemaker of Heart: Sinoatrial Node (SA Node) located in right atrium. Average adult resting pulse = 72 beats/minute.",
                "RBCs (Erythrocytes): Biconcave, lack nucleus (in humans), lifespan ~120 days. Spleen is called the 'Graveyard of RBCs'.",
                "Blood Groups: Discovered by Karl Landsteiner. Group O is Universal Donor; Group AB is Universal Recipient.",
                "Largest Organ of Human Body = Skin. Largest Internal Organ/Gland = Liver. Smallest Bone = Stapes (in middle ear). Longest Bone = Femur (thigh).",
                "Human Brain: Weighs ~1.3 to 1.4 kg. Cerebrum (cognition/memory), Cerebellum (balance/posture), Medulla (involuntary centers), Hypothalamus (body thermostat).",
                "Digestive Tract: Digestion begins in the mouth (salivary amylase). Stomach has HCl (pH ~1.5-2.0). Complete digestion and absorption occur in Small Intestine.",
                "Pancreas: Dual gland (endocrine + exocrine). Beta cells secrete Insulin (lowers blood sugar); Alpha cells secrete Glucagon.",
                "Thyroid Gland: Butterfly-shaped gland in neck; secretes Thyroxine containing Iodine. Deficiency causes Goitre.",
                "Adrenal Glands: Sit atop kidneys; secrete Adrenaline (the '3F' Emergency Hormone: Fight, Flight, or Freeze).",
                "Master Gland: Pituitary gland, situated in the sella turcica at the base of the brain, regulated by the Hypothalamus.",
                "Excretory Unit: Nephron. Humans are ureotelic (excrete urea, produced in liver from toxic ammonia).",
                "Vitamins: Fat-soluble (A, D, E, K); Water-soluble (B, C).",
                "Deficiency Diseases: Vit A -> Night Blindness; Vit B1 -> Beriberi; Vit B3 -> Pellagra; Vit B12 -> Pernicious Anemia; Vit C -> Scurvy; Vit D -> Rickets; Vit K -> Bleeding diathesis."
            ]
        },
        "previous_year_questions": [
            {
                "id": 6601,
                "topic_id": 66,
                "exam_id": 1,
                "question": "Which gland in the human body is referred to as the 'Master Gland' because its hormones regulate several other endocrine glands? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Thyroid Gland",
                    "Pituitary Gland",
                    "Adrenal Gland",
                    "Pancreas"
                ],
                "correct_answer": "Pituitary Gland",
                "explanation": "The Pituitary Gland (hypophysis) is called the Master Gland because its anterior and posterior lobes secrete tropic hormones (such as TSH, ACTH, FSH, and LH) that control the functioning of other endocrine glands.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6602,
                "topic_id": 66,
                "exam_id": 1,
                "question": "Which vitamin deficiency is responsible for causing the disease Scurvy, characterized by bleeding gums and poor wound healing? [UPSC CDS 2022]",
                "options_json": [
                    "Vitamin A",
                    "Vitamin B1",
                    "Vitamin C",
                    "Vitamin D"
                ],
                "correct_answer": "Vitamin C",
                "explanation": "Vitamin C (ascorbic acid) is a vital cofactor required for the enzymatic hydroxylation of proline and lysine in collagen synthesis. Its deficiency causes Scurvy, characterized by fragile capillaries and bleeding gums.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6603,
                "topic_id": 66,
                "exam_id": 1,
                "question": "Which organ of the human body acts as the 'Graveyard of Red Blood Cells (RBCs)' where aged erythrocytes are filtered and destroyed? [RRB NTPC 2021]",
                "options_json": [
                    "Liver",
                    "Spleen",
                    "Bone Marrow",
                    "Kidney"
                ],
                "correct_answer": "Spleen",
                "explanation": "The Spleen contains specialized reticular cords and sinusoidal capillaries where old, inflexible RBCs (after their ~120-day lifespan) are destroyed by resident macrophages, earning it the title 'graveyard of RBCs'.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 6601,
                "topic_id": 66,
                "question": "Which part of the human brain is primarily responsible for maintaining posture, equilibrium, and the coordination of voluntary movements?",
                "options_json": [
                    "Cerebrum",
                    "Cerebellum",
                    "Medulla Oblongata",
                    "Hypothalamus"
                ],
                "correct_answer": "Cerebellum",
                "explanation": "The Cerebellum (little brain) coordinates precision, timing, and smooth execution of voluntary muscle contractions and maintains posture and body balance.",
                "points": 1
            },
            {
                "id": 6602,
                "topic_id": 66,
                "question": "Which hormone, secreted by the Beta cells of the Pancreas, lowers elevated blood glucose concentrations?",
                "options_json": [
                    "Glucagon",
                    "Insulin",
                    "Somatostatin",
                    "Thyroxine"
                ],
                "correct_answer": "Insulin",
                "explanation": "Insulin is a peptide hormone produced by pancreatic beta cells. It enables cellular glucose uptake and converts excess glucose into stored glycogen in the liver and skeletal muscle.",
                "points": 1
            },
            {
                "id": 6603,
                "topic_id": 66,
                "question": "What is the normal blood pressure of an adult human measured under standard resting conditions?",
                "options_json": [
                    "80/120 mmHg",
                    "120/80 mmHg",
                    "100/60 mmHg",
                    "140/90 mmHg"
                ],
                "correct_answer": "120/80 mmHg",
                "explanation": "Standard normal human blood pressure is 120 mmHg systolic (during ventricular contraction) over 80 mmHg diastolic (during ventricular relaxation).",
                "points": 1
            },
            {
                "id": 6604,
                "topic_id": 66,
                "question": "Which metal ion is incorporated as an essential constituent in the molecular structure of Vitamin B12 (Cyanocobalamin)?",
                "options_json": [
                    "Iron",
                    "Magnesium",
                    "Cobalt",
                    "Copper"
                ],
                "correct_answer": "Cobalt",
                "explanation": "Vitamin B12 is chemically named cyanocobalamin because it contains a central cobalt atom within a corrin ring, essential for red blood cell maturation and myelin sheath maintenance.",
                "points": 1
            },
            {
                "id": 6605,
                "topic_id": 66,
                "question": "What is the functional and microscopic filtration unit of the human kidney?",
                "options_json": [
                    "Nephron",
                    "Neuron",
                    "Alveolus",
                    "Hepatic Lobule"
                ],
                "correct_answer": "Nephron",
                "explanation": "Each human kidney contains approximately 1 million nephrons, which carry out ultrafiltration, selective tubular reabsorption, and tubular secretion to produce urine.",
                "points": 1
            },
            {
                "id": 6606,
                "topic_id": 66,
                "question": "Which blood group is universally accepted as the 'Universal Donor' in clinical blood transfusions?",
                "options_json": [
                    "Group AB positive",
                    "Group O negative",
                    "Group A positive",
                    "Group B negative"
                ],
                "correct_answer": "Group O negative",
                "explanation": "Group O negative blood has neither A nor B antigens nor the Rh antigen on its red blood cell surfaces, preventing immune agglutination in all recipients.",
                "points": 1
            },
            {
                "id": 6607,
                "topic_id": 66,
                "question": "Deficiency of which trace dietary mineral causes enlargement of the thyroid gland, clinically known as Goitre?",
                "options_json": [
                    "Iron",
                    "Calcium",
                    "Iodine",
                    "Phosphorus"
                ],
                "correct_answer": "Iodine",
                "explanation": "Iodine is an indispensable chemical constituent of thyroid hormones (T3 and T4). Dietary deficiency of iodine causes compensatory hypertrophy of the thyroid gland (Goitre).",
                "points": 1
            },
            {
                "id": 6608,
                "topic_id": 66,
                "question": "Which digestive juice, produced by the liver, contains no enzymes yet is critical for emulsifying dietary fats?",
                "options_json": [
                    "Gastric Juice",
                    "Pancreatic Juice",
                    "Bile Juice",
                    "Intestinal Juice"
                ],
                "correct_answer": "Bile Juice",
                "explanation": "Bile juice is synthesized by hepatocytes in the liver. Although devoid of enzymes, its bile salts disperse large hydrophobic lipid globules into micro-droplets, facilitating lipase action.",
                "points": 1
            },
            {
                "id": 6609,
                "topic_id": 66,
                "question": "What is the smallest bone in the human body?",
                "options_json": [
                    "Malleus",
                    "Incus",
                    "Stapes",
                    "Phalanges"
                ],
                "correct_answer": "Stapes",
                "explanation": "The stapes (stirrup bone) in the middle ear is the smallest and lightest bone in the human skeleton, measuring approximately 3 mm in length.",
                "points": 1
            },
            {
                "id": 6610,
                "topic_id": 66,
                "question": "Which vitamin, also called the 'Sunlight Vitamin', is synthesized endogenously in the human skin upon exposure to ultraviolet rays?",
                "options_json": [
                    "Vitamin A",
                    "Vitamin C",
                    "Vitamin D",
                    "Vitamin E"
                ],
                "correct_answer": "Vitamin D",
                "explanation": "7-dehydrocholesterol in the epidermal layer of human skin is converted into cholecalciferol (Vitamin D3) upon exposure to solar UV-B radiation.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 6601,
                "topic_id": 66,
                "question": "What is the average lifespan of a human red blood cell (erythrocyte) in normal circulation?",
                "options_json": [
                    "10 to 15 days",
                    "120 days",
                    "365 days",
                    "30 days"
                ],
                "correct_answer": "120 days",
                "explanation": "Human red blood cells lack nuclei and organelles and circulate in the bloodstream for approximately 120 days before being sequestered and recycled by the spleen and liver.",
                "points": 1
            },
            {
                "id": 6602,
                "topic_id": 66,
                "question": "Which region of the human brain regulates autonomic body temperature, hunger, and thirst?",
                "options_json": [
                    "Cerebrum",
                    "Hypothalamus",
                    "Cerebellum",
                    "Pons"
                ],
                "correct_answer": "Hypothalamus",
                "explanation": "The Hypothalamus acts as the body's internal thermostat and neuroendocrine integration center, regulating temperature, appetite, fluid balance, and sleep-wake cycles.",
                "points": 1
            },
            {
                "id": 6603,
                "topic_id": 66,
                "question": "In which segment of the human gastrointestinal tract does the complete digestion and maximum absorption of nutrients occur?",
                "options_json": [
                    "Stomach",
                    "Small Intestine",
                    "Large Intestine",
                    "Esophagus"
                ],
                "correct_answer": "Small Intestine",
                "explanation": "The small intestine (particularly the duodenum and jejunum) receives pancreatic and intestinal enzymes and bile, completing food digestion. Its millions of microscopic villi provide a vast surface area for nutrient absorption.",
                "points": 1
            },
            {
                "id": 6604,
                "topic_id": 66,
                "question": "Deficiency of Vitamin A in the human diet causes which clinical eye condition?",
                "options_json": [
                    "Night Blindness (Nyctalopia)",
                    "Glaucoma",
                    "Myopia",
                    "Cataract"
                ],
                "correct_answer": "Night Blindness (Nyctalopia)",
                "explanation": "Vitamin A (retinol) is an essential precursor of rhodopsin, the visual pigment in retinal rod cells required for vision in low light. Deficiency causes poor dark adaptation (night blindness).",
                "points": 1
            },
            {
                "id": 6605,
                "topic_id": 66,
                "question": "The natural biological pacemaker that initiates electrical impulses governing the human heartbeat is the:",
                "options_json": [
                    "Sinoatrial Node (SA Node)",
                    "Atrioventricular Node (AV Node)",
                    "Bundle of His",
                    "Purkinje Fibers"
                ],
                "correct_answer": "Sinoatrial Node (SA Node)",
                "explanation": "The SA node, located in the upper wall of the right atrium, spontaneously generates rhythmic electrical impulses (~72/min) that cause atrial and ventricular contractions.",
                "points": 1
            },
            {
                "id": 6606,
                "topic_id": 66,
                "question": "Which endocrine hormone is secreted by the adrenal glands to prepare the human body for 'Fight or Flight' during acute emergency situations?",
                "options_json": [
                    "Adrenaline (Epinephrine)",
                    "Insulin",
                    "Melatonin",
                    "Calcitonin"
                ],
                "correct_answer": "Adrenaline (Epinephrine)",
                "explanation": "Adrenaline (epinephrine), secreted by the adrenal medulla during stress, elevates heart rate, dilates bronchioles, and mobilizes blood glucose for emergency response.",
                "points": 1
            },
            {
                "id": 6607,
                "topic_id": 66,
                "question": "Which blood group is known as the 'Universal Recipient' because its plasma contains neither Anti-A nor Anti-B antibodies?",
                "options_json": [
                    "Group O",
                    "Group A",
                    "Group B",
                    "Group AB"
                ],
                "correct_answer": "Group AB",
                "explanation": "Individuals with blood group AB express both A and B antigens on their red blood cells and produce neither Anti-A nor Anti-B antibodies in their plasma, permitting safe receipt of all ABO blood types.",
                "points": 1
            },
            {
                "id": 6608,
                "topic_id": 66,
                "question": "Deficiency of Vitamin B1 (Thiamine) leads to which nutritional deficiency disorder?",
                "options_json": [
                    "Scurvy",
                    "Beriberi",
                    "Pellagra",
                    "Rickets"
                ],
                "correct_answer": "Beriberi",
                "explanation": "Vitamin B1 (thiamine) deficiency causes Beriberi, characterized by neurological impairment, peripheral neuropathy (dry beriberi), and cardiovascular failure (wet beriberi).",
                "points": 1
            },
            {
                "id": 6609,
                "topic_id": 66,
                "question": "What is the main nitrogenous excretory waste substance eliminated by the human urinary system?",
                "options_json": [
                    "Ammonia",
                    "Uric Acid",
                    "Urea",
                    "Creatinine"
                ],
                "correct_answer": "Urea",
                "explanation": "Humans are ureotelic organisms. Highly toxic ammonia generated from protein deamination is converted into less toxic, water-soluble urea in the liver via the urea (ornithine) cycle and excreted by the kidneys.",
                "points": 1
            },
            {
                "id": 6610,
                "topic_id": 66,
                "question": "Which instrument is routinely employed by healthcare professionals to measure arterial blood pressure?",
                "options_json": [
                    "Stethoscope",
                    "Sphygmomanometer",
                    "Electrocardiograph (ECG)",
                    "Spirometer"
                ],
                "correct_answer": "Sphygmomanometer",
                "explanation": "A sphygmomanometer, comprising an inflatable cuff and mercury or aneroid manometer, measures arterial blood pressure in mmHg.",
                "points": 1
            },
            {
                "id": 6611,
                "topic_id": 66,
                "question": "Which of the following is a water-soluble vitamin that is not stored in the body and must be regularly replenished?",
                "options_json": [
                    "Vitamin A",
                    "Vitamin D",
                    "Vitamin C",
                    "Vitamin K"
                ],
                "correct_answer": "Vitamin C",
                "explanation": "Vitamin C and the B-complex vitamins are water-soluble. They dissolve in body fluids and are excreted in urine, necessitating daily dietary intake.",
                "points": 1
            },
            {
                "id": 6612,
                "topic_id": 66,
                "question": "Which part of the respiratory system contains tiny air sacs surrounded by capillaries where gas exchange between blood and air takes place?",
                "options_json": [
                    "Bronchi",
                    "Trachea",
                    "Alveoli",
                    "Larynx"
                ],
                "correct_answer": "Alveoli",
                "explanation": "The lungs contain hundreds of millions of microscopic alveoli, providing a massive surface area where oxygen diffuses into the pulmonary capillaries and CO₂ diffuses out.",
                "points": 1
            },
            {
                "id": 6613,
                "topic_id": 66,
                "question": "Which vitamin is indispensable for the normal hepatic synthesis of prothrombin and factors essential for blood clotting?",
                "options_json": [
                    "Vitamin K",
                    "Vitamin E",
                    "Vitamin D",
                    "Vitamin A"
                ],
                "correct_answer": "Vitamin K",
                "explanation": "Vitamin K (phylloquinone) is an essential cofactor for the post-translational carboxylation of clotting factors II (prothrombin), VII, IX, and X in the liver.",
                "points": 1
            },
            {
                "id": 6614,
                "topic_id": 66,
                "question": "What is the longest and strongest bone in the human body?",
                "options_json": [
                    "Tibia",
                    "Fibula",
                    "Femur (Thigh bone)",
                    "Humerus"
                ],
                "correct_answer": "Femur (Thigh bone)",
                "explanation": "The femur (thigh bone) is the longest, heaviest, and strongest bone in the human skeleton, supporting the entire upper body weight during locomotion.",
                "points": 1
            },
            {
                "id": 6615,
                "topic_id": 66,
                "question": "Which enzyme present in gastric juice breaks down dietary proteins into peptones in an acidic environment?",
                "options_json": [
                    "Pepsin",
                    "Trypsin",
                    "Amylase",
                    "Lipase"
                ],
                "correct_answer": "Pepsin",
                "explanation": "Gastric chief cells secrete pepsinogen, which is activated by hydrochloric acid (HCl) into pepsin, initiating the digestion of dietary proteins in the stomach.",
                "points": 1
            },
            {
                "id": 6616,
                "topic_id": 66,
                "question": "Pernicious anemia is caused by the chronic nutritional deficiency or malabsorption of which vitamin?",
                "options_json": [
                    "Vitamin B12 (Cyanocobalamin)",
                    "Vitamin B6 (Pyridoxine)",
                    "Vitamin B1 (Thiamine)",
                    "Vitamin C"
                ],
                "correct_answer": "Vitamin B12 (Cyanocobalamin)",
                "explanation": "Lack of intrinsic factor in the stomach prevents absorption of Vitamin B12, causing Pernicious Anemia characterized by immature, oversized erythrocytes (megaloblasts).",
                "points": 1
            },
            {
                "id": 6617,
                "topic_id": 66,
                "question": "What is the largest internal solid organ and gland in the human body?",
                "options_json": [
                    "Pancreas",
                    "Liver",
                    "Spleen",
                    "Kidney"
                ],
                "correct_answer": "Liver",
                "explanation": "The liver is the largest internal organ and largest gland in the human body, weighing approximately 1.5 kg in an adult and executing over 500 vital metabolic functions.",
                "points": 1
            },
            {
                "id": 6618,
                "topic_id": 66,
                "question": "Which mineral element binds directly with oxygen inside erythrocytes as an integral part of hemoglobin?",
                "options_json": [
                    "Copper",
                    "Iron",
                    "Zinc",
                    "Magnesium"
                ],
                "correct_answer": "Iron",
                "explanation": "Each hemoglobin molecule contains four heme prosthetic groups containing iron (Fe²⁺) ions, each capable of reversibly binding one oxygen molecule.",
                "points": 1
            },
            {
                "id": 6619,
                "topic_id": 66,
                "question": "Which of the following is an autoimmune condition caused by the failure of the pancreas to secrete adequate insulin?",
                "options_json": [
                    "Type 1 Diabetes Mellitus",
                    "Diabetes Insipidus",
                    "Addison's Disease",
                    "Cushing's Syndrome"
                ],
                "correct_answer": "Type 1 Diabetes Mellitus",
                "explanation": "Type 1 Diabetes Mellitus is an autoimmune disorder where the immune system destroys insulin-secreting beta cells in the pancreas, leading to severe hyperglycemia.",
                "points": 1
            },
            {
                "id": 6620,
                "topic_id": 66,
                "question": "Which section of the human brain controls vital involuntary autonomic reflex actions including respiration, heartbeat, and swallowing?",
                "options_json": [
                    "Medulla Oblongata",
                    "Cerebrum",
                    "Thalamus",
                    "Olfactory Lobe"
                ],
                "correct_answer": "Medulla Oblongata",
                "explanation": "The Medulla Oblongata contains the vital cardiovascular, vasomotor, and respiratory rhythmicity centers, as well as reflex centers for coughing, sneezing, and swallowing.",
                "points": 1
            }
        ]
    }
}
