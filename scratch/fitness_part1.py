# Physical Fitness Part 1: Topics 69, 70, 71
# 69: Basic Fitness, 70: Strength, 71: Endurance

PART1_DATA = {
    69: {
        "lesson": {
            "title": "Foundations of Physical Fitness: Health-Related vs. Skill-Related Components",
            "source_id": 8, # ACSM
            "content": {
                "definition": "Physical fitness is defined by the World Health Organization (WHO) and American College of Sports Medicine (ACSM) as the ability to execute daily activities with optimal performance, endurance, and strength while managing disease, fatigue, stress, and reducing sedentary behavior.",
                "overview": "Physical fitness is divided into two primary categories: Health-Related Components (essential for disease prevention, functional longevity, and metabolic health) and Skill-Related Components (critical for athletic performance, tactical defense operations, and neuromuscular coordination). Effective conditioning requires applying the FITT-VP principle: Frequency, Intensity, Time, Type, Volume, and Progression.",
                "types": [
                    {
                        "name": "Health-Related Fitness Components (5 Core)",
                        "desc": "Foundational physiological qualities that enhance longevity and reduce chronic disease risk.",
                        "examples": [
                            "Cardiorespiratory Endurance (heart & lung oxygen transport)",
                            "Muscular Strength (maximum force generation in 1-RM)",
                            "Muscular Endurance (repetitive submaximal contractions)",
                            "Flexibility (joint range of motion without tissue strain)",
                            "Body Composition (relative ratio of fat mass to lean body mass)"
                        ]
                    },
                    {
                        "name": "Skill-Related Fitness Components (6 Tactical)",
                        "desc": "Neuromuscular capabilities that govern athletic agility and combat/sports performance.",
                        "examples": [
                            "Agility (rapid change of direction with control)",
                            "Balance (maintenance of equilibrium dynamic/static)",
                            "Coordination (integrating sensory input with motor execution)",
                            "Power (work rate: force multiplied by velocity)",
                            "Reaction Time (latency between stimulus and physical movement)",
                            "Speed (rapidity of linear or multidirectional movement)"
                        ]
                    },
                    {
                        "name": "Physical Activity vs. Exercise",
                        "desc": "Physical activity includes any skeletal muscle contraction expending energy above resting levels; Exercise is planned, structured, repetitive physical activity designed specifically to improve or maintain physical fitness.",
                        "examples": [
                            "Physical Activity: Casual walking, climbing stairs, gardening",
                            "Structured Exercise: 5 km tempo run, progressive resistance training, interval swimming"
                        ]
                    },
                    {
                        "name": "The FITT-VP Principle",
                        "desc": "Scientific framework prescribed by ACSM for individual training load dosage.",
                        "examples": [
                            "Frequency: Days per week (e.g., 3-5 days/week)",
                            "Intensity: Physiological effort (% of 1-RM, % of HRmax, RPE)",
                            "Time: Duration of session (e.g., 30-60 minutes)",
                            "Type: Specific modality (aerobic, resistance, neuromotor)",
                            "Volume: Total weekly work (Frequency x Intensity x Time)",
                            "Progression: Systematic upward adjustment of training stimulus"
                        ]
                    }
                ],
                "rules": [
                    {
                        "rule_number": 1,
                        "title": "Principle of Specificity (SAID Principle)",
                        "explanation": "Specific Adaptations to Imposed Demands (SAID): The body adapts specifically to the physiological stressors placed upon it. Aerobic training improves mitochondrial density; heavy resistance training stimulates motor unit recruitment.",
                        "correct": "Prescribing 1.6 km pacing and VO2 max intervals for a candidate preparing for the Army 1.6 km endurance run.",
                        "incorrect": "Relying exclusively on heavy bicep curls and bench presses to improve a candidate's 5 km running endurance."
                    },
                    {
                        "rule_number": 2,
                        "title": "Principle of Progressive Overload",
                        "explanation": "To achieve continuous adaptation and avoid fitness plateaus, training stimulus (load, volume, density, or frequency) must be systematically increased within physiological tolerance.",
                        "correct": "Increasing running distance by 5-10% weekly or adding 2.5 kg to barbell squats once target rep ranges are mastered.",
                        "incorrect": "Doubling running mileage in a single week, leading directly to shin splints or tendonitis."
                    },
                    {
                        "rule_number": 3,
                        "title": "Principle of Reversibility (Detraining)",
                        "explanation": "Fitness adaptations are transient; when regular training ceases, cardiovascular endurance drops rapidly within 1-2 weeks, followed by muscular strength declines over 4-8 weeks.",
                        "correct": "Maintaining minimum stimulus with 1-2 weekly maintenance sessions during exam travel or taper weeks.",
                        "incorrect": "Assuming that achieving peak 1.6 km run timing remains permanent after 3 months of complete physical inactivity."
                    },
                    {
                        "rule_number": 4,
                        "title": "SMART Fitness Goal Setting",
                        "explanation": "Fitness goals must be Specific, Measurable, Achievable, Relevant, and Time-bound to facilitate sustainable progress and objective tracking.",
                        "correct": "'Improve 1.6 km run time from 6:30 to 5:45 in 12 weeks through 3 weekly aerobic interval sessions.'",
                        "incorrect": "'Get fit and run fast whenever I feel like training without a timetable.'"
                    },
                    {
                        "rule_number": 5,
                        "title": "Health Assessment & PAR-Q+ Screening",
                        "explanation": "Prior to starting any high-intensity conditioning program, candidates must undergo Physical Activity Readiness Questionnaire (PAR-Q+) screening to identify occult cardiovascular or musculoskeletal contraindications.",
                        "correct": "Administering PAR-Q+ screening and medical clearance if a candidate reports chest pain or unexplained dizziness.",
                        "incorrect": "Forcing an untrained individual with chest tightness into maximum-effort sprint intervals."
                    }
                ],
                "common_mistakes": [
                    {
                        "mistake": "Conflating health-related fitness with skill-related sports performance",
                        "correction": "Recognize that health-related fitness governs disease prevention, whereas skill-related components govern competitive athletics.",
                        "rationale": "An elite golfer has superb skill-related coordination but may lack cardiorespiratory endurance; an endurance runner has high health-related fitness."
                    },
                    {
                        "mistake": "Neglecting the principle of progression by using identical weights and distances for months",
                        "correction": "Apply systematic progressive overload through load, repetitions, or reduced rest intervals.",
                        "rationale": "Homeostatic adaptation stabilizes unless the body is challenged with a novel, progressive stimulus."
                    },
                    {
                        "mistake": "Believing spot reduction of body fat is possible through isolated exercises",
                        "correction": "Understand that body fat loss occurs systemically through a sustained caloric deficit and metabolic conditioning.",
                        "rationale": "Performing 500 abdominal crunches strengthens the rectus abdominis but does not selectively oxidize subcutaneous abdominal adipose tissue."
                    }
                ],
                "quick_revision_points": [
                    "Health-related fitness components: Cardiorespiratory endurance, Muscular strength, Muscular endurance, Flexibility, Body composition.",
                    "Skill-related fitness components: Agility, Balance, Coordination, Power, Reaction time, Speed.",
                    "FITT-VP stands for Frequency, Intensity, Time, Type, Volume, and Progression.",
                    "The SAID principle stands for Specific Adaptations to Imposed Demands.",
                    "Reversibility dictates that physiological adaptations degrade when training stimulus is completely removed."
                ]
            }
        },
        "pyqs": [
            {
                "exam_id": 5, # Indian Army Agniveer / NDA PET
                "question": "Which of the following is categorized strictly as a HEALTH-RELATED component of physical fitness, rather than a skill-related component?",
                "options_json": ["Flexibility", "Agility", "Reaction time", "Power"],
                "correct_answer": "Flexibility",
                "explanation": "Flexibility is one of the five health-related components of physical fitness (along with cardiorespiratory endurance, muscular strength, muscular endurance, and body composition). Agility, reaction time, and power are skill-related components.",
                "source_id": 8,
                "question_type": "MCQ"
            },
            {
                "exam_id": 6, # SSC CPO CAPF PET
                "question": "According to sports training methodology, what does the acronym 'SAID' stand for in the context of the principle of specificity?",
                "options_json": [
                    "Specific Adaptations to Imposed Demands",
                    "Standard Aerobic Intensity Distribution",
                    "Systematic Acceleration of Individual Dynamics",
                    "Skeletal Alignment and Isometric Development"
                ],
                "correct_answer": "Specific Adaptations to Imposed Demands",
                "explanation": "The SAID principle (Specific Adaptations to Imposed Demands) states that the human body places physiological adaptations specifically matching the types of demands and stressors placed on it.",
                "source_id": 8,
                "question_type": "MCQ"
            },
            {
                "exam_id": 5,
                "question": "In exercise prescription, what does the letter 'T' stand for in the classic FITT formula when paired with Frequency, Intensity, and Type?",
                "options_json": ["Time (Duration)", "Tension", "Target heart rate", "Tolerated load"],
                "correct_answer": "Time (Duration)",
                "explanation": "In the FITT principle, F stands for Frequency, I for Intensity, T for Time (duration of the session), and T for Type (mode of exercise).",
                "source_id": 9,
                "question_type": "MCQ"
            }
        ],
        "practice": [
            {
                "question": "Which physiological component represents the ability of the circulatory and respiratory systems to supply oxygen to skeletal muscles during sustained moderate-to-vigorous physical activity?",
                "options_json": ["Cardiorespiratory endurance", "Muscular power", "Static balance", "Anaerobic speed"],
                "correct_answer": "Cardiorespiratory endurance",
                "explanation": "Cardiorespiratory endurance measures the capacity of the heart, lungs, and vascular network to deliver oxygenated blood to working muscles over an extended duration.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which skill-related fitness component is defined as the rate at which an individual can perform work, combining both force production and movement velocity?",
                "options_json": ["Power", "Flexibility", "Endurance", "Body composition"],
                "correct_answer": "Power",
                "explanation": "Power is defined mechanically as Work / Time or Force x Velocity. In sports, explosive jumping or shot-put delivery are classic manifestations of muscular power.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "A defense candidate runs 5 km every alternate day at a fixed pace for 6 months but notices zero further improvements in race pace. Which training principle has been violated?",
                "options_json": ["Principle of Progressive Overload", "Principle of Specificity", "Principle of Reversibility", "Principle of Individual Differences"],
                "correct_answer": "Principle of Progressive Overload",
                "explanation": "Without systematically advancing the stimulus (speed, intervals, volume, or hill elevation), the body adapts to the fixed stress and reaches an adaptation plateau.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "What is the primary conceptual distinction between 'physical activity' and 'exercise'?",
                "options_json": [
                    "Exercise is structured, planned, and repetitive with the goal of improving fitness, while physical activity is any bodily movement expending energy.",
                    "Physical activity always requires gym equipment, while exercise does not.",
                    "Exercise only involves anaerobic systems, whereas physical activity is always aerobic.",
                    "There is no scientific difference between physical activity and exercise."
                ],
                "correct_answer": "Exercise is structured, planned, and repetitive with the goal of improving fitness, while physical activity is any bodily movement expending energy.",
                "explanation": "As defined by WHO and ACSM, physical activity encompasses all bodily movements expending energy (walking, chores), whereas exercise is a planned, purposeful subset intended to maintain or enhance fitness.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which fitness assessment tool is a standard self-guided pre-participation health screening questionnaire used globally before initiating exercise?",
                "options_json": ["PAR-Q+ (Physical Activity Readiness Questionnaire)", "VO2 max spirometry", "Dual-Energy X-ray Absorptiometry (DEXA)", "1-RM Bench Press test"],
                "correct_answer": "PAR-Q+ (Physical Activity Readiness Questionnaire)",
                "explanation": "The PAR-Q+ is a globally recognized evidence-based questionnaire designed to identify individuals who require medical clearance prior to initiating an exercise regimen.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following is considered a SKILL-RELATED component of physical fitness rather than a health-related component?",
                "options_json": ["Coordination", "Muscular endurance", "Body composition", "Cardiorespiratory endurance"],
                "correct_answer": "Coordination",
                "explanation": "Coordination is a skill-related component. The five health-related components are body composition, cardiorespiratory endurance, flexibility, muscular endurance, and muscular strength.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The time elapsed between the presentation of an external sensory stimulus and the initiation of a motor response is known as:",
                "options_json": ["Reaction time", "Movement velocity", "Agility index", "Acceleration latency"],
                "correct_answer": "Reaction time",
                "explanation": "Reaction time is the latency interval between the onset of a stimulus (such as a starter pistol in a sprint) and the initiation of muscular movement.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "When a trained athlete ceases all physical conditioning, which physiological attribute typically shows the earliest measurable decline within 10 to 14 days?",
                "options_json": ["Cardiorespiratory endurance (blood volume & VO2 max)", "Absolute bone mineral density", "Maximum tendon tensile strength", "Gross motor skill coordination"],
                "correct_answer": "Cardiorespiratory endurance (blood volume & VO2 max)",
                "explanation": "Cardiorespiratory detraining occurs rapidly: plasma volume drops within 48-72 hours, reducing stroke volume and maximal oxygen uptake (VO2 max) within 1-2 weeks.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "In the SMART goal framework, what does the letter 'M' denote?",
                "correct_answer": "Measurable",
                "explanation": "SMART stands for Specific, Measurable, Achievable, Relevant, and Time-bound.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The loss of physiological and performance adaptations following the cessation of training is governed by the principle of ______.",
                "correct_answer": "reversibility",
                "explanation": "The principle of reversibility (colloquially 'use it or lose it') dictates that training adaptations diminish when regular physical exercise stops.",
                "difficulty": "Medium",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ],
        "quiz": [
            {
                "question": "Which of the following is NOT one of the five health-related components of physical fitness?",
                "options_json": ["Agility", "Cardiorespiratory endurance", "Muscular strength", "Body composition"],
                "correct_answer": "Agility",
                "explanation": "Agility is a skill-related fitness component. The five health-related components are cardiorespiratory endurance, muscular strength, muscular endurance, flexibility, and body composition.",
                "question_type": "MCQ"
            },
            {
                "question": "The principle of Specific Adaptations to Imposed Demands is widely known in exercise science by the acronym:",
                "options_json": ["SAID", "FITT", "RAMP", "SMART"],
                "correct_answer": "SAID",
                "explanation": "SAID stands for Specific Adaptations to Imposed Demands, stating that adaptations strictly mirror the physiological stressors applied.",
                "question_type": "MCQ"
            },
            {
                "question": "According to the ACSM FITT-VP principle, what does the letter 'V' stand for?",
                "options_json": ["Volume", "Velocity", "Ventilation", "Vascularity"],
                "correct_answer": "Volume",
                "explanation": "In FITT-VP, V stands for Volume (total quantity of exercise, such as total distance run or total tonnage lifted per week).",
                "question_type": "MCQ"
            },
            {
                "question": "Which fitness component represents the ability of a joint to move through its full, unrestricted range of motion?",
                "options_json": ["Flexibility", "Muscular endurance", "Agility", "Coordination"],
                "correct_answer": "Flexibility",
                "explanation": "Flexibility is defined as the unrestricted physiological range of motion available at a joint or series of joints.",
                "question_type": "MCQ"
            },
            {
                "question": "The ability to maintain equilibrium while either stationary or moving is known as:",
                "options_json": ["Balance", "Power", "Reaction time", "Speed"],
                "correct_answer": "Balance",
                "explanation": "Balance is the skill-related component of fitness that involves maintaining the body's center of mass over its base of support.",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following describes the systematic increase in resistance, volume, or intensity required to stimulate ongoing adaptation?",
                "options_json": ["Progressive overload", "Supercompensation denial", "Overtraining syndrome", "Specificity deviation"],
                "correct_answer": "Progressive overload",
                "explanation": "Progressive overload requires gradually increasing the training stress to continually stimulate physiological adaptation and muscle development.",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following is a classic example of a skill-related fitness component essential for tactical obstacle courses?",
                "options_json": ["Power", "Resting metabolic rate", "Vital capacity", "Body fat percentage"],
                "correct_answer": "Power",
                "explanation": "Power combines explosive strength with high velocity, allowing candidates to clear 9-foot ditches, scale high walls, and sprint through obstacles.",
                "question_type": "MCQ"
            },
            {
                "question": "What is the recommended weekly physical activity duration of moderate-intensity aerobic exercise recommended by WHO for adults?",
                "options_json": [
                    "At least 150 to 300 minutes per week",
                    "30 minutes per month",
                    "At least 600 minutes per week",
                    "Exactly 15 minutes per day of sprinting"
                ],
                "correct_answer": "At least 150 to 300 minutes per week",
                "explanation": "The World Health Organization (WHO) recommends 150-300 minutes of moderate-intensity or 75-150 minutes of vigorous-intensity aerobic physical activity weekly for adults.",
                "question_type": "MCQ"
            },
            {
                "question": "In the FITT framework, the letter 'F' stands for ______.",
                "correct_answer": "Frequency",
                "explanation": "F stands for Frequency, representing how many training sessions are completed per unit of time (typically days per week).",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The time elapsed between a starter's gun sound and a runner's first movement off the blocks is called ______ time.",
                "correct_answer": "reaction",
                "explanation": "Reaction time is the latency between external sensory stimulation and the initiation of muscular contraction.",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    70: {
        "lesson": {
            "title": "Muscular Strength & Resistance Training: Biomechanics and Progressive Overload",
            "source_id": 8, # ACSM
            "content": {
                "definition": "Muscular strength is the maximum force that a muscle or muscle group can generate at a specified velocity during a single maximal voluntary contraction (commonly assessed as 1-Repetition Maximum, 1-RM).",
                "overview": "Strength development forms the cornerstone of physical conditioning, injury resilience, and tactical performance. Skeletal muscle adapts through mechanical tension, muscle protein breakdown and resynthesis (hypertrophy), and neural adaptations (increased motor unit recruitment, rate coding, and synchronization). Resistance training incorporates bodyweight movements (calisthenics), free weights, and resistance machines.",
                "types": [
                    {
                        "name": "Types of Muscle Contractions",
                        "desc": "Muscle actions categorized by changes in muscle fiber length during tension generation.",
                        "examples": [
                            "Concentric: Muscle shortens while generating tension (e.g., upward phase of a bicep curl or pull-up)",
                            "Eccentric: Muscle lengthens while under tension (e.g., lowering phase of a squat or push-up; generates highest muscle damage and hypertrophy stimulus)",
                            "Isometric: Muscle produces tension without changing joint angle or muscle length (e.g., holding a plank or wall sit)"
                        ]
                    },
                    {
                        "name": "Repetition Ranges & Training Adaptations",
                        "desc": "Different load intensities dictate specific neuromuscular and physiological adaptations.",
                        "examples": [
                            "Maximal Strength: 1 to 5 repetitions at 85-100% of 1-RM (high neural recruitment, long rest 3-5 min)",
                            "Hypertrophy (Muscle Size): 6 to 12 repetitions at 67-85% of 1-RM (mechanical tension & metabolic stress, rest 60-90 sec)",
                            "Muscular Endurance: 15+ repetitions at <67% of 1-RM (capillarization and mitochondrial buffering, rest 30-45 sec)"
                        ]
                    },
                    {
                        "name": "Calisthenics vs. Free Weights",
                        "desc": "Foundational strength modalities utilized in defense physical training.",
                        "examples": [
                            "Bodyweight (Calisthenics): Push-ups, pull-ups, dips, bodyweight squats (develops relative strength and kinesthetic awareness)",
                            "Free Weights: Barbells and dumbbells (allows precise incremental micro-loading and axial loading of major kinetic chains)"
                        ]
                    },
                    {
                        "name": "Mechanisms of Hypertrophy & Strength",
                        "desc": "The triad of physiological triggers driving skeletal muscle remodeling.",
                        "examples": [
                            "Mechanical Tension: Force applied across muscle fibers during heavy loaded contractions",
                            "Muscle Damage: Micro-tears in sarcomeres stimulating satellite cell activation and repair",
                            "Metabolic Stress: Accumulation of metabolites (lactate, H+, inorganic phosphate) stimulating anabolic signaling"
                        ]
                    }
                ],
                "rules": [
                    {
                        "rule_number": 1,
                        "title": "Maintain Neutral Spine Alignment",
                        "explanation": "During compound loaded movements (squat, deadlift, overhead press), the lumbar spine must maintain its natural lordotic curve to distribute axial loads across intervertebral discs evenly.",
                        "correct": "Bracing the core with intra-abdominal pressure while keeping the chest elevated and lower back neutral.",
                        "incorrect": "Rounding the lumbar spine (flexion under load) during heavy deadlifts, placing shearing stress on the L4-L5 discs."
                    },
                    {
                        "rule_number": 2,
                        "title": "Prioritize Full Range of Motion (ROM)",
                        "explanation": "Training through a complete joint range of motion enhances muscle hypertrophy, improves joint mobility, and builds strength at terminal joint angles.",
                        "correct": "Performing deep bodyweight squats with hips dropping below knees while maintaining heel contact.",
                        "incorrect": "Performing 'quarter squats' with excessive weight, loading the patellar tendon without full quadriceps or glute recruitment."
                    },
                    {
                        "rule_number": 3,
                        "title": "Controlled Eccentric Cadence",
                        "explanation": "Controlling the lowering (eccentric) phase for 2-3 seconds enhances motor unit recruitment and reduces relying on bounce momentum.",
                        "correct": "Lowering the body smoothly to the floor in a push-up before explosively driving upward.",
                        "incorrect": "Dropping uncontrollably and bouncing off joints or the floor to complete repetitions."
                    },
                    {
                        "rule_number": 4,
                        "title": "Proper Breathing Technique & Valsalva Precaution",
                        "explanation": "Exhale during the exertion/concentric phase and inhale during the eccentric/lowering phase. The Valsalva maneuver (holding breath against a closed glottis) must be used judiciously by healthy individuals for heavy lifts, as it spikes arterial blood pressure.",
                        "correct": "Inhaling on the way down in a bench press, exhaling as the barbell is pressed upward off the chest.",
                        "incorrect": "Holding breath continuously across multiple repetitions, risking lightheadedness or syncope."
                    },
                    {
                        "rule_number": 5,
                        "title": "Adequate Inter-Set Recovery for Strength",
                        "explanation": "High-intensity maximal strength sets (1-5 reps) require 2 to 3 minutes of rest to replenish intramuscular phosphocreatine (PCr) stores.",
                        "correct": "Resting 2-3 minutes between maximum pull-up attempts to achieve maximal motor unit output.",
                        "incorrect": "Rushing back into heavy sets with only 15 seconds of rest, forcing premature fatigue and deteriorating technique."
                    }
                ],
                "common_mistakes": [
                    {
                        "mistake": "Sacrificing biomechanical form to lift heavier weight ('ego lifting')",
                        "correction": "Select a load where every repetition can be completed with strict form through full range of motion.",
                        "rationale": "Compensatory movement patterns load connective tissues unsafely, drastically elevating acute tear risks."
                    },
                    {
                        "mistake": "Ignoring the eccentric (lowering) portion of the exercise",
                        "correction": "Lower the weight or body under deliberate muscular control for 2 to 3 seconds.",
                        "rationale": "Eccentric contractions generate high mechanical tension and are primary drivers of muscle growth and tendon remodeling."
                    },
                    {
                        "mistake": "Training identical muscle groups to failure on consecutive days",
                        "correction": "Allow 48 hours of recovery between high-intensity sessions targeting the same muscle group.",
                        "rationale": "Muscle protein synthesis peaks 24-36 hours post-exercise; inadequate rest impairs supercompensation and leads to overuse injury."
                    }
                ],
                "quick_revision_points": [
                    "Muscular strength is assessed through 1-RM (One Repetition Maximum).",
                    "Three muscle contraction types: Concentric (shortening), Eccentric (lengthening), Isometric (static length).",
                    "Strength rep range: 1-5 reps (>85% 1-RM); Hypertrophy: 6-12 reps (67-85%); Endurance: 15+ reps (<67%).",
                    "Eccentric contractions generate the greatest mechanical tension and sarcomere micro-tears.",
                    "Skeletal muscle requires 48 hours of recovery before intense retraining of the same group."
                ]
            }
        },
        "pyqs": [
            {
                "exam_id": 5, # Indian Army Agniveer / NDA PET
                "question": "During a standard beam pull-up test, what type of muscular contraction occurs in the biceps and latissimus dorsi when the candidate lowers themselves slowly from chin-above-bar to full arm extension?",
                "options_json": ["Eccentric contraction", "Concentric contraction", "Isometric contraction", "Isokinetic contraction"],
                "correct_answer": "Eccentric contraction",
                "explanation": "During the controlled descent phase, the contracting muscles lengthen under tension to decelerate the downward momentum of the body, which is the definition of an eccentric contraction.",
                "source_id": 10,
                "question_type": "MCQ"
            },
            {
                "exam_id": 6, # SSC CPO CAPF PET
                "question": "A plank exercise, where the body is held in a rigid prone position off the ground without joint motion, is an example of which type of muscle contraction?",
                "options_json": ["Isometric contraction", "Concentric contraction", "Eccentric contraction", "Ballistic contraction"],
                "correct_answer": "Isometric contraction",
                "explanation": "An isometric contraction occurs when muscle tension is generated without any change in muscle fiber length or joint angle.",
                "source_id": 8,
                "question_type": "MCQ"
            },
            {
                "exam_id": 5,
                "question": "To maximize absolute muscular strength according to exercise science principles, what repetition range per set is recommended?",
                "options_json": ["1 to 5 repetitions", "15 to 25 repetitions", "30 to 50 repetitions", "8 to 10 repetitions with zero rest"],
                "correct_answer": "1 to 5 repetitions",
                "explanation": "Loads greater than 85% of 1-RM (corresponding to 1 to 5 repetitions with 2-5 minutes rest) maximize neural drive, motor unit recruitment, and maximal strength.",
                "source_id": 8,
                "question_type": "MCQ"
            }
        ],
        "practice": [
            {
                "question": "Which of the following describes the maximum weight an individual can lift for exactly one repetition through the full range of motion with proper form?",
                "options_json": ["1-Repetition Maximum (1-RM)", "Basal Metabolic Rate", "Maximum Aerobic Capacity", "Anaerobic Threshold"],
                "correct_answer": "1-Repetition Maximum (1-RM)",
                "explanation": "1-RM is the gold standard benchmark in strength assessment, representing the maximal load that can be lifted once with valid technique.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "During the upward pushing phase of a standard push-up, what type of contraction is performed by the triceps and pectoralis major muscles?",
                "options_json": ["Concentric contraction", "Eccentric contraction", "Isometric contraction", "Passive relaxation"],
                "correct_answer": "Concentric contraction",
                "explanation": "In the upward phase, the muscle fibers shorten as they overcome external gravity and push the body up, which is a concentric contraction.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "What is the primary cellular mechanism that causes skeletal muscle fibers to increase in cross-sectional area following chronic resistance training?",
                "options_json": ["Muscular hypertrophy (synthesis of actin and myosin filaments)", "Muscular hyperplasia (doubling number of muscle fibers)", "Increase in subcutaneous adipose tissue", "Lengthening of long bones"],
                "correct_answer": "Muscular hypertrophy (synthesis of actin and myosin filaments)",
                "explanation": "Muscular hypertrophy refers to the enlargement of existing muscle fibers through increased myofibrillar protein synthesis (actin and myosin filament addition).",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Why is the eccentric phase of resistance training critical for maximizing athletic development and muscle remodeling?",
                "options_json": [
                    "It produces the highest mechanical tension and recruits motor units while lengthening, stimulating structural adaptation.",
                    "It consumes zero cellular energy and requires no oxygen.",
                    "It eliminates the need for rest days between workouts.",
                    "It completely prevents any delayed onset muscle soreness."
                ],
                "correct_answer": "It produces the highest mechanical tension and recruits motor units while lengthening, stimulating structural adaptation.",
                "explanation": "Eccentric muscle actions generate higher force per unit muscle area than concentric actions, stimulating satellite cells, structural protein remodeling, and tendon stiffness.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "What is the minimum recommended rest interval between heavy, high-intensity training sessions targeting the same muscle group to allow complete muscle protein synthesis and recovery?",
                "options_json": ["48 hours", "6 hours", "12 hours", "14 days"],
                "correct_answer": "48 hours",
                "explanation": "Skeletal muscle protein synthesis remains elevated for 24-48 hours post-workout. Retraining too soon impedes recovery and can precipitate overtraining.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Which basic calisthenic exercise is universally tested in Indian Armed Forces and Police physical tests to measure upper-body pulling strength?",
                "options_json": ["Pull-up (Beam)", "Bench press", "Leg extension", "Bicep curl"],
                "correct_answer": "Pull-up (Beam)",
                "explanation": "Pull-ups on a horizontal beam test relative upper-body strength and muscular endurance of the latissimus dorsi, rhomboids, and biceps.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Holding one's breath against a closed airway while exerting maximal effort under a heavy barbell load is known as the:",
                "options_json": ["Valsalva maneuver", "Bohr effect", "Heimlich maneuver", "Karvonen method"],
                "correct_answer": "Valsalva maneuver",
                "explanation": "The Valsalva maneuver involves forced exhalation against a closed glottis, increasing intra-abdominal pressure to stabilize the spine, but transiently elevating arterial blood pressure.",
                "difficulty": "Hard",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following repetition ranges is specifically recognized for optimizing local muscular endurance rather than maximal 1-RM strength?",
                "options_json": ["15 or more repetitions with lighter loads", "1 to 3 repetitions with maximum loads", "4 to 6 repetitions with heavy loads", "Single repetition isometric holds only"],
                "correct_answer": "15 or more repetitions with lighter loads",
                "explanation": "Performing 15 or more repetitions with lighter loads (<67% 1-RM) targets Type I slow-twitch muscle fibers and mitochondrial enzymatic endurance.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "A muscle contraction where tension is generated while the muscle lengthens under load is called an ______ contraction.",
                "correct_answer": "eccentric",
                "explanation": "An eccentric muscle contraction occurs when the muscle lengthens while developing tension.",
                "difficulty": "Medium",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The abbreviation 1-RM in resistance training stands for One ______ Maximum.",
                "correct_answer": "Repetition",
                "explanation": "1-RM stands for One Repetition Maximum, denoting the greatest load lifted once with proper form.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ],
        "quiz": [
            {
                "question": "What type of muscle contraction occurs when muscle length remains completely unchanged during tension generation, such as pushing against an immovable wall?",
                "options_json": ["Isometric", "Concentric", "Eccentric", "Isokinetic"],
                "correct_answer": "Isometric",
                "explanation": "Isometric contractions involve tension generation without change in muscle fiber length or joint angle.",
                "question_type": "MCQ"
            },
            {
                "question": "Which repetition range is classically prescribed for maximizing muscular hypertrophy (muscle size)?",
                "options_json": ["6 to 12 repetitions", "1 to 3 repetitions", "25 to 50 repetitions", "100 continuous repetitions"],
                "correct_answer": "6 to 12 repetitions",
                "explanation": "The 6-12 repetition range at 67-85% 1-RM provides optimal balance between mechanical tension and metabolic stress for hypertrophy.",
                "question_type": "MCQ"
            },
            {
                "question": "Which muscle group is the primary agonist (prime mover) during the standard horizontal push-up?",
                "options_json": ["Pectoralis major", "Latissimus dorsi", "Biceps brachii", "Hamstrings"],
                "correct_answer": "Pectoralis major",
                "explanation": "The pectoralis major (chest) acts as the prime mover during horizontal pushing movements like the push-up and bench press.",
                "question_type": "MCQ"
            },
            {
                "question": "In the human skeletal muscle, which muscle fiber type is characterized by fast contraction speed, high anaerobic capacity, but rapid fatigue?",
                "options_json": ["Type II (Fast-twitch) fibers", "Type I (Slow-twitch) fibers", "Cardiac fibers", "Smooth muscle fibers"],
                "correct_answer": "Type II (Fast-twitch) fibers",
                "explanation": "Type II fast-twitch fibers produce high force and contract rapidly via glycolytic anaerobic pathways, but fatigue quickly.",
                "question_type": "MCQ"
            },
            {
                "question": "What is the primary risk of hyper-extending or rounding the lumbar spine while lifting heavy objects off the floor?",
                "options_json": [
                    "Excessive shear stress and herniation risk on intervertebral discs",
                    "Rapid loss of lung capacity",
                    "Decreased heart rate",
                    "Immediate atrophy of the quadriceps"
                ],
                "correct_answer": "Excessive shear stress and herniation risk on intervertebral discs",
                "explanation": "Spinal flexion under axial load exposes the lumbar discs to hazardous shear forces, risking disc herniation and ligamentous strain.",
                "question_type": "MCQ"
            },
            {
                "question": "What is the recommended rest interval between maximal strength sets (1-5 reps at >85% 1-RM)?",
                "options_json": ["2 to 5 minutes", "10 to 15 seconds", "30 seconds", "Zero rest"],
                "correct_answer": "2 to 5 minutes",
                "explanation": "ATP and phosphocreatine (PCr) stores require 2 to 5 minutes of rest to replenish fully between heavy, near-maximal efforts.",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following is a multi-joint (compound) exercise?",
                "options_json": ["Barbell Squat", "Dumbbell Bicep Curl", "Wrist Curl", "Leg Extension"],
                "correct_answer": "Barbell Squat",
                "explanation": "Compound exercises involve movement across multiple joints; the squat articulates the hip, knee, and ankle joints simultaneously.",
                "question_type": "MCQ"
            },
            {
                "question": "The increase in skeletal muscle mass resulting from an increase in the size of individual muscle fibers is called:",
                "options_json": ["Hypertrophy", "Atrophy", "Hyperplasia", "Sarcopenia"],
                "correct_answer": "Hypertrophy",
                "explanation": "Hypertrophy refers to the enlargement of existing cells or tissues, particularly the cross-sectional area of skeletal muscle fibers.",
                "question_type": "MCQ"
            },
            {
                "question": "During the upward lifting phase of a bicep curl, the biceps undergo a ______ contraction.",
                "correct_answer": "concentric",
                "explanation": "A concentric contraction involves the shortening of the muscle as it produces tension to lift the weight.",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "The three primary mechanisms of muscle hypertrophy are mechanical tension, metabolic stress, and muscle ______.",
                "correct_answer": "damage",
                "explanation": "Muscle damage (micro-tears in sarcomeres that trigger satellite cell activation and repair) is one of the three primary hypertrophy mechanisms.",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    },

    71: {
        "lesson": {
            "title": "Cardiovascular Endurance & Aerobic Conditioning: Energy Systems and Training Zones",
            "source_id": 8, # ACSM
            "content": {
                "definition": "Cardiovascular endurance (cardiorespiratory fitness) is the capacity of the heart, blood vessels, and lungs to deliver oxygenated blood to working skeletal muscles during prolonged physical activity, and the muscles' capacity to utilize oxygen to generate adenosine triphosphate (ATP) aerobically.",
                "overview": "Cardiovascular fitness determines performance in defense endurance runs (such as the Indian Army 1.6 km test and CAPF 5 km run). The human body relies on three distinct energy systems: the Phosphagen (ATP-PC) system (0-10s), the Glycolytic (anaerobic lactic) system (10s-2min), and the Oxidative (aerobic) system (>2min). Training cardiorespiratory endurance involves mastering heart rate zones, calculating Maximum Heart Rate (HRmax), and understanding Maximal Oxygen Uptake (VO2 max).",
                "types": [
                    {
                        "name": "The Three Bioenergetic Pathways",
                        "desc": "How muscle cells generate ATP across varying intensities and durations.",
                        "examples": [
                            "ATP-PC (Phosphagen) System: Anaerobic alactic, utilizes intramuscular phosphocreatine for 0-10 seconds of all-out effort (100m sprint)",
                            "Glycolytic (Lactic) System: Anaerobic breakdown of glycogen into lactate for 10-120 seconds (400m sprint)",
                            "Oxidative (Aerobic) System: Mitochondrial breakdown of carbohydrates and fats in the presence of oxygen for sustained efforts >2 minutes (1.6 km run, marathon)"
                        ]
                    },
                    {
                        "name": "Cardiovascular Training Modalities",
                        "desc": "Training methodologies to build aerobic capacity and lactate threshold.",
                        "examples": [
                            "Long Slow Distance (LSD): Sustained steady-state running at 60-70% HRmax to build mitochondrial density and stroke volume",
                            "Tempo / Threshold Runs: Running at or near lactate threshold (~80-88% HRmax) for 20-30 minutes to improve lactate clearance",
                            "High-Intensity Interval Training (HIIT): Alternating brief bouts of near-maximal effort (90-95% HRmax) with active recovery periods",
                            "Fartlek Training: 'Speed play' combining continuous running with random speed bursts across terrain"
                        ]
                    },
                    {
                        "name": "Heart Rate Training Zones (5 Zones)",
                        "desc": "Intensity zones based on percentage of Maximum Heart Rate (% HRmax).",
                        "examples": [
                            "Zone 1 (50-60% HRmax): Active recovery and warm-up",
                            "Zone 2 (60-70% HRmax): Aerobic base building and fat oxidation (can hold a comfortable conversation)",
                            "Zone 3 (70-80% HRmax): Aerobic fitness and tempo pace",
                            "Zone 4 (80-90% HRmax): Anaerobic threshold and lactate tolerance",
                            "Zone 5 (90-100% HRmax): VO2 max intervals and maximal sprint capacity"
                        ]
                    },
                    {
                        "name": "Key Physiological Benchmarks",
                        "desc": "Scientific parameters measuring cardiorespiratory conditioning.",
                        "examples": [
                            "VO2 Max: Maximal volume of oxygen (in mL/kg/min) the body can transport and utilize during exhaustive exercise",
                            "Stroke Volume: Volume of blood pumped per ventricular contraction (increases with aerobic adaptation)",
                            "Cardiac Output (Q): Q = Heart Rate x Stroke Volume; total volume of blood pumped per minute",
                            "Resting Heart Rate (RHR): Decreases with endurance conditioning (athletes often exhibit resting bradycardia <60 bpm)"
                        ]
                    }
                ],
                "rules": [
                    {
                        "rule_number": 1,
                        "title": "Calculate Maximum Heart Rate (HRmax) Accurately",
                        "explanation": "A common standard baseline estimate for Maximum Heart Rate is the Fox formula: HRmax = 220 - Age. For targeted training, use the Karvonen formula (Heart Rate Reserve = HRmax - RHR; Target HR = (HRR x % intensity) + RHR).",
                        "correct": "For a 20-year-old: HRmax is approximately 200 bpm; a Zone 2 workout is between 120 and 140 bpm (60-70%).",
                        "incorrect": "Sprinting at 195 bpm every single day and wondering why chronic fatigue and injuries occur."
                    },
                    {
                        "rule_number": 2,
                        "title": "Build the Aerobic Base First (The 80/20 Rule)",
                        "explanation": "Approximately 80% of weekly running volume should be completed at low-to-moderate intensity (Zone 2), and only 20% at high intensity (Zone 4/5).",
                        "correct": "Running 4 days a week at an easy conversational Zone 2 pace, with 1 day dedicated to track intervals.",
                        "incorrect": "Treating every single training run as a maximal race effort to beat personal records daily."
                    },
                    {
                        "rule_number": 3,
                        "title": "Respect the Lactate Threshold",
                        "explanation": "Lactate threshold is the exercise intensity at which blood lactate accumulation exceeds clearance rate. Training slightly below or at this threshold elevates race pace without early fatigue.",
                        "correct": "Performing 20-minute tempo runs at a 'comfortably hard' pace where breathing is deep but controlled.",
                        "incorrect": "Sprinting the first 400m of a 1.6 km test at maximum speed, accumulating severe acidosis, and walking the remaining 1200m."
                    },
                    {
                        "rule_number": 4,
                        "title": "Apply The 10% Weekly Mileage Rule",
                        "explanation": "To prevent stress fractures, shin splints, and plantar fasciitis, total weekly running distance should not increase by more than 10% from the previous week.",
                        "correct": "Progressing from 20 km total weekly distance to 22 km in the following week.",
                        "incorrect": "Jumping from 15 km in week 1 to 35 km in week 2, causing acute overuse trauma to lower extremity connective tissues."
                    },
                    {
                        "rule_number": 5,
                        "title": "Maintain Proper Running Mechanics",
                        "explanation": "Maintain an upright posture with a slight forward lean from the ankles, midfoot strike beneath the center of mass, relaxed shoulders, and a cadence around 170-180 steps/min.",
                        "correct": "Landing softly with feet landing under hips rather than over-striding ahead of the torso.",
                        "incorrect": "Severe heel-striking with locked knees far ahead of the body, creating massive braking forces and knee joint impact."
                    }
                ],
                "common_mistakes": [
                    {
                        "mistake": "Running too fast on easy/recovery days",
                        "correction": "Run at a true conversational pace in Zone 2 where full sentences can be spoken without gasping.",
                        "rationale": "High-intensity running on recovery days prevents muscular recovery and stimulates excessive sympathetic nervous system strain."
                    },
                    {
                        "mistake": "Starting endurance tests at an unsustainable sprint pace",
                        "correction": "Pace evenly across all laps of the 1.6 km run to preserve glycogen stores and avoid early lactic acid accumulation.",
                        "rationale": "Going out too fast triggers rapid anaerobic glycolysis, dropping muscle pH and inducing early muscular shutdown."
                    },
                    {
                        "mistake": "Relying solely on running without cross-training",
                        "correction": "Incorporate non-impact aerobic conditioning like cycling, rowing, or swimming.",
                        "rationale": "Cross-training develops cardiorespiratory endurance while sparing lower extremity joints from repetitive ground impact."
                    }
                ],
                "quick_revision_points": [
                    "Cardiovascular endurance relies on the oxidative (aerobic) energy system utilizing oxygen in mitochondria.",
                    "The Fox formula for estimated Maximum Heart Rate is: HRmax = 220 - Age.",
                    "VO2 Max is the gold standard benchmark for cardiorespiratory fitness (mL of O2/kg/min).",
                    "Zone 2 training (60-70% HRmax) builds aerobic base, mitochondrial density, and fat oxidation efficiency.",
                    "The 80/20 rule: 80% low-intensity base running, 20% high-intensity interval training."
                ]
            }
        },
        "pyqs": [
            {
                "exam_id": 5, # Indian Army Agniveer / NDA PET
                "question": "For the Indian Army Physical Fitness Test (PFT), what is the qualifying distance and target time for Group I excellence in the endurance run?",
                "options_json": [
                    "1.6 km (1600 meters) in up to 5 minutes 30 seconds",
                    "5.0 km in 30 minutes",
                    "800 meters in 4 minutes",
                    "2.4 km in 12 minutes"
                ],
                "correct_answer": "1.6 km (1600 meters) in up to 5 minutes 30 seconds",
                "explanation": "In the Indian Army Soldier General Duty recruitment rally, Group I candidates must complete the 1.6 km run in up to 5 minutes 30 seconds (awarded 60 marks).",
                "source_id": 10,
                "question_type": "MCQ"
            },
            {
                "exam_id": 6, # SSC CPO CAPF PET
                "question": "What is the primary bioenergetic energy pathway utilized by skeletal muscle during sustained aerobic exercise lasting longer than 3 minutes?",
                "options_json": [
                    "Aerobic (Oxidative) system",
                    "ATP-PC (Phosphagen) system",
                    "Anaerobic glycolytic system only",
                    "Creatine kinase pathway exclusively"
                ],
                "correct_answer": "Aerobic (Oxidative) system",
                "explanation": "For physical activity lasting longer than 2-3 minutes, the aerobic (oxidative) system in the mitochondria becomes the predominant supplier of ATP through carbohydrate and fatty acid oxidation.",
                "source_id": 8,
                "question_type": "MCQ"
            },
            {
                "exam_id": 5,
                "question": "Using the standard age-predicted formula (220 - Age), what is the estimated Maximum Heart Rate (HRmax) for a 20-year-old defense aspirant?",
                "options_json": ["200 beats per minute", "180 beats per minute", "220 beats per minute", "160 beats per minute"],
                "correct_answer": "200 beats per minute",
                "explanation": "Using the classic Fox formula: HRmax = 220 - Age = 220 - 20 = 200 beats per minute (bpm).",
                "source_id": 8,
                "question_type": "MCQ"
            }
        ],
        "practice": [
            {
                "question": "Which physiological metric represents the maximum volume of oxygen that an individual can consume and utilize per kilogram of body weight per minute during maximal exercise?",
                "options_json": ["VO2 max", "Stroke volume index", "Vital capacity", "Tidal volume"],
                "correct_answer": "VO2 max",
                "explanation": "VO2 max (expressed in mL/kg/min) is the definitive physiological measurement of maximal cardiorespiratory fitness and aerobic capacity.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "An athlete with a high level of cardiovascular endurance often displays a lower resting heart rate (sometimes below 60 bpm). What is this clinical adaptation called?",
                "options_json": ["Athletic bradycardia", "Tachycardia", "Arrhythmia", "Hypertension"],
                "correct_answer": "Athletic bradycardia",
                "explanation": "Aerobic training enlarges ventricular volume and increases stroke volume, allowing the heart to pump more blood per beat, resulting in resting bradycardia (<60 bpm).",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "Which training method alternates short bursts of intense anaerobic exercise (at 90-95% HRmax) with low-intensity active recovery periods?",
                "options_json": [
                    "High-Intensity Interval Training (HIIT)",
                    "Continuous long slow distance walking",
                    "Static isometric training",
                    "Passive stretching"
                ],
                "correct_answer": "High-Intensity Interval Training (HIIT)",
                "explanation": "HIIT involves repeated bouts of high-intensity work interspersed with recovery periods, efficiently boosting VO2 max and anaerobic capacity.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "During steady-state running in Heart Rate Zone 2 (60-70% HRmax), what is the primary fuel source oxidized by working muscles?",
                "options_json": ["Fatty acids (lipids)", "Muscle protein", "Creatine phosphate", "Inorganic minerals"],
                "correct_answer": "Fatty acids (lipids)",
                "explanation": "At lower-to-moderate aerobic intensities (Zone 2), the body predominantly relies on beta-oxidation of fatty acids, sparing glycogen stores.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "What is the recommended guideline known as the 'talk test' for verifying that a runner is training in the aerobic base building zone?",
                "options_json": [
                    "Being able to speak in complete sentences comfortably without gasping for breath",
                    "Being completely unable to utter any words",
                    "Speaking only single-syllable words between deep gasps",
                    "Holding breath for 30 seconds while running"
                ],
                "correct_answer": "Being able to speak in complete sentences comfortably without gasping for breath",
                "explanation": "The talk test is a validated field marker: an individual exercising in Zone 2 can carry on a comfortable conversation without being breathless.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "Cardiac output (Q) is defined mathematically as the product of Heart Rate (HR) and which other cardiovascular factor?",
                "options_json": ["Stroke Volume (SV)", "Systolic blood pressure", "Respiratory rate", "Hemoglobin concentration"],
                "correct_answer": "Stroke Volume (SV)",
                "explanation": "Cardiac Output = Heart Rate x Stroke Volume (Q = HR x SV), measuring the total volume of blood pumped by the ventricles per minute.",
                "difficulty": "Medium",
                "question_type": "MCQ"
            },
            {
                "question": "A runner increases weekly running mileage from 20 km to 40 km in a single week. Which training guideline has been severely violated?",
                "options_json": [
                    "The 10% rule of progressive volume increase",
                    "The SAID principle",
                    "The Fartlek interval protocol",
                    "The Karvonen formula"
                ],
                "correct_answer": "The 10% rule of progressive volume increase",
                "explanation": "The 10% rule advises that weekly running distance should not expand by more than 10% in one week to prevent overuse injuries like shin splints.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The Swedish term 'Fartlek', widely used in cross-country and track training, literally translates to:",
                "options_json": ["Speed play", "Long run", "Fast heartbeat", "Muscle endurance"],
                "correct_answer": "Speed play",
                "explanation": "'Fartlek' is a Swedish word meaning 'speed play', describing an unstructured training session combining continuous running with varying speed bursts.",
                "difficulty": "Easy",
                "question_type": "MCQ"
            },
            {
                "question": "The gold standard metric for cardiorespiratory fitness measuring maximum oxygen utilization is known as ______ max.",
                "correct_answer": "VO2",
                "explanation": "VO2 max stands for maximal oxygen consumption, expressing the maximum rate of oxygen utilized during intense exercise.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "Using the standard formula (220 - Age), an individual who is 30 years old has an estimated Maximum Heart Rate of ______ beats per minute.",
                "correct_answer": "190",
                "explanation": "220 - 30 = 190 beats per minute.",
                "difficulty": "Easy",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ],
        "quiz": [
            {
                "question": "Which of the following energy systems produces adenosine triphosphate (ATP) with the highest rate of speed but exhausts its fuel supply within approximately 10 seconds?",
                "options_json": ["Phosphagen (ATP-PC) system", "Aerobic glycolysis", "Beta-oxidation", "Krebs cycle"],
                "correct_answer": "Phosphagen (ATP-PC) system",
                "explanation": "The ATP-PC (phosphagen) system utilizes stored intracellular ATP and phosphocreatine to generate rapid power for 0-10 seconds of all-out effort.",
                "question_type": "MCQ"
            },
            {
                "question": "Which heart rate training zone (60-70% of HRmax) is considered the optimal foundation for developing mitochondrial density and aerobic base?",
                "options_json": ["Zone 2", "Zone 5", "Zone 1", "Zone 4"],
                "correct_answer": "Zone 2",
                "explanation": "Zone 2 (60-70% HRmax) develops capillary density, mitochondrial biogenesis, and fatty acid oxidation without excessive systemic fatigue.",
                "question_type": "MCQ"
            },
            {
                "question": "What is the standard qualifying time for male candidates in the SSC CPO CAPF 100-meter sprint test?",
                "options_json": ["16 seconds", "25 seconds", "10 seconds", "12 seconds"],
                "correct_answer": "16 seconds",
                "explanation": "In the SSC CPO (Sub-Inspector in CAPFs & Delhi Police) PET, male candidates must complete the 100-meter sprint within 16 seconds.",
                "question_type": "MCQ"
            },
            {
                "question": "What organelle in skeletal muscle cells is primarily responsible for generating ATP through oxidative aerobic metabolism?",
                "options_json": ["Mitochondria", "Ribosome", "Endoplasmic reticulum", "Lysosome"],
                "correct_answer": "Mitochondria",
                "explanation": "Mitochondria are the 'cellular powerhouses' where the Krebs cycle and electron transport chain produce ATP via oxidative phosphorylation.",
                "question_type": "MCQ"
            },
            {
                "question": "The volume of blood ejected from the left ventricle into the aorta during a single cardiac cycle is termed:",
                "options_json": ["Stroke volume", "Cardiac output", "End-systolic volume", "Ejection fraction"],
                "correct_answer": "Stroke volume",
                "explanation": "Stroke volume is the milliliters of blood pumped per ventricular contraction; endurance athletes develop elevated stroke volumes.",
                "question_type": "MCQ"
            },
            {
                "question": "In the context of the 80/20 training rule popularized in endurance physiology, what percentage of weekly training should be performed at low, aerobic intensity?",
                "options_json": ["80%", "20%", "50%", "100%"],
                "correct_answer": "80%",
                "explanation": "The 80/20 rule states that 80% of total weekly volume should be at low aerobic intensity (Zone 1-2) to promote adaptation without overtraining.",
                "question_type": "MCQ"
            },
            {
                "question": "What physiological threshold marks the exercise intensity above which blood lactate begins to accumulate exponentially faster than it can be cleared?",
                "options_json": ["Lactate threshold (Anaerobic threshold)", "Aerobic base minimum", "Resting heart rate threshold", "Respiratory arrest point"],
                "correct_answer": "Lactate threshold (Anaerobic threshold)",
                "explanation": "The lactate threshold is the point at which systemic lactate production outpaces buffering and clearance, leading to acidosis and rapid fatigue.",
                "question_type": "MCQ"
            },
            {
                "question": "Which of the following is considered an effective low-impact aerobic cross-training exercise that minimizes ground reaction force on the knees?",
                "options_json": ["Swimming", "Downhill pavement sprinting", "Plyometric depth jumps", "Box jump rebounds"],
                "correct_answer": "Swimming",
                "explanation": "Swimming provides whole-body cardiovascular conditioning in a buoyant, non-impact medium that eliminates joint impact shock.",
                "question_type": "MCQ"
            },
            {
                "question": "Cardiac output is calculated by multiplying heart rate by ______ volume.",
                "correct_answer": "stroke",
                "explanation": "Cardiac Output = Heart Rate x Stroke Volume.",
                "question_type": "FILL_IN_THE_BLANK"
            },
            {
                "question": "A resting heart rate below 60 beats per minute commonly found in well-trained endurance runners is called athletic ______.",
                "correct_answer": "bradycardia",
                "explanation": "Sinus bradycardia (RHR < 60 bpm) is a benign, healthy adaptation resulting from increased stroke volume and elevated vagal tone in athletes.",
                "question_type": "FILL_IN_THE_BLANK"
            }
        ]
    }
}
