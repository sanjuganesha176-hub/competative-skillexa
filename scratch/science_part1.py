"""General Science Part 1: Topics 63 (Physics) & 64 (Chemistry)"""

SCIENCE_PART1_DATA = {
    "63": {
        "title": "Physics: Mechanics, Newton's Laws, Gravitation, Thermodynamics, Optics & Electricity",
        "source_id": 7,
        "content": {
            "definition": "Physics in competitive examinations (UPSC CSE, SSC CGL/CHSL Tier 1/2, RRB NTPC/JE, CDS, NDA, State PSCs) investigates the fundamental physical laws governing matter, energy, space, and time. Core areas include classical mechanics, kinematics, gravitation, fluid statics and dynamics, heat and thermodynamics, wave mechanics, geometrical and physical optics, electrostatics, electromagnetism, and atomic-nuclear physics.",
            "overview": "Comprehensive Physical Principles Framework:\n- Mechanics & Dynamics: Scalar vs Vector quantities; Newton's Three Laws of Motion ($F = ma$, Action-Reaction); Conservation of Linear Momentum; Work ($W = F d \\cos\\theta$), Kinetic Energy ($E_k = \\frac{1}{2}mv^2$), Potential Energy ($E_p = mgh$); Power ($P = W/t$ in Watts)\n- Gravitation & Planetary Motion: Newton's Universal Law of Gravitation ($F = G\\frac{m_1 m_2}{r^2}$); Acceleration due to gravity ($g \\approx 9.8\\text{ m/s}^2$, varies from minimum at equator to maximum at poles, zero at Earth center); Escape Velocity ($v_e = \\sqrt{2gR} \\approx 11.2\\text{ km/s}$ for Earth); Kepler's Laws of Planetary Motion\n- Properties of Matter & Fluids: Hooke's Law; Pascal's Principle (hydraulic press); Archimedes' Principle (buoyancy, law of floatation); Bernoulli's Principle (aerodynamic lift, venturimeter); Surface Tension (capillarity, spherical water drops); Viscosity (Poiseuille's flow)\n- Heat & Thermodynamics: Temperature scales ($C/5 = (F-32)/9 = (K-273)/5$); Anomalous expansion of water ($4^\\circ\\text{C}$ maximum density); Triple point of water ($273.16\\text{ K}$); Laws of Thermodynamics (Zeroth law defines temperature, First law defines internal energy conservation $\\Delta Q = \\Delta U + W$, Second law defines entropy and impossibility of perpetual motion machine of second kind)\n- Waves, Sound & Acoustics: Transverse vs Longitudinal waves; Audible sound ($20\\text{ Hz} - 20,000\\text{ Hz}$), Infrasonic ($<20\\text{ Hz}$), Ultrasonic ($>20,000\\text{ Hz}$, SONAR, bat echolocation); Speed of sound is fastest in solids, slower in liquids, slowest in gases, zero in vacuum; Doppler Effect\n- Optics & Light: Speed of light in vacuum ($c = 3 \\times 10^8\\text{ m/s}$); Laws of Reflection ($i = r$); Refraction (Snell's Law $n_1\\sin i = n_2\\sin r$); Total Internal Reflection (optical fibres, mirage, diamond brilliance; condition: denser to rarer medium and $i > \\theta_c$); Dispersion (rainbow); Scattering (Rayleigh scattering $\\propto 1/\\lambda^4$, blue sky, red sunset); Human eye defects (Myopia corrected by concave lens, Hypermetropia corrected by convex lens, Presbyopia by bifocal lens)\n- Electricity & Magnetism: Coulomb's Law; Ohm's Law ($V = IR$); Electric Power ($P = VI = I^2R = V^2/R$, $1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}$); Resistors in series ($R = R_1 + R_2$) vs parallel ($1/R = 1/R_1 + 1/R_2$); Fleming's Left-Hand Rule (electric motors) and Right-Hand Rule (electric generators); Faraday's Laws of Electromagnetic Induction; Transformer (mutual induction, works on AC only)\n- Modern Physics: Photoelectric Effect ($E = h\\nu$, Einstein 1905 Nobel Prize 1921); Radioactivity (Becquerel, Curie; alpha, beta, gamma rays); Nuclear Fission (U-235, nuclear power plants, atomic bombs) vs Nuclear Fusion (Hydrogen bomb, Sun's energy generation via proton-proton chain)",
            "types": [
                {
                    "name": "1. Classical Mechanics & Kinematics",
                    "desc": "Fundamental laws of motion, force systems, energy conservation, and gravitation.",
                    "examples": [
                        "Newton's 1st Law (Inertia) • Newton's 2nd Law (F = ma) • Newton's 3rd Law (Action = Reaction)",
                        "Escape velocity from Earth surface = 11.2 km/s • g value is maximum at poles and zero at Earth's center"
                    ]
                },
                {
                    "name": "2. Fluid Mechanics & Atmospheric Physics",
                    "desc": "Pressure distributions, buoyancy, surface tension, and aerodynamic lift.",
                    "examples": [
                        "Archimedes' Principle: Floating body displaces liquid equal to its own weight",
                        "Bernoulli's Theorem: Explains dynamic lift in airplanes and spinning ball curve",
                        "Surface Tension: Spherical shape of rain drops and oil spreading on water"
                    ]
                },
                {
                    "name": "3. Thermal Physics & Thermodynamics",
                    "desc": "Heat transfer mechanisms, anomalous expansion, and thermodynamic laws.",
                    "examples": [
                        "Conduction (solids) • Convection (fluids) • Radiation (vacuum via electromagnetic waves)",
                        "Anomalous expansion of water: Density is maximum and volume is minimum at 4°C"
                    ]
                },
                {
                    "name": "4. Wave Optics, Sound & Acoustics",
                    "desc": "Wave propagation, acoustic frequencies, reflection, refraction, and optical phenomena.",
                    "examples": [
                        "Total Internal Reflection (TIR): Optical fibers, mirages in deserts, sparkling diamonds",
                        "Scattering of Light: Blue color of sky due to Rayleigh scattering (Intensity ∝ 1/λ⁴)",
                        "Ultrasonic waves (>20 kHz) used in SONAR and medical ultrasonography"
                    ]
                },
                {
                    "name": "5. Electricity, Electromagnetism & Modern Physics",
                    "desc": "Circuits, magnetic effects of current, induction, and nuclear reactions.",
                    "examples": [
                        "Ohm's Law: V = IR • 1 kWh commercial unit of electricity = 3.6 × 10⁶ Joules",
                        "Transformers operate strictly on Alternating Current (AC) via Mutual Induction",
                        "Nuclear Fusion: Source of stellar energy in the Sun (conversion of Hydrogen into Helium)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Variation of Acceleration Due to Gravity (g) Rule",
                    "explanation": "Acceleration due to gravity ($g = GM/R^2$) is NOT constant over Earth's surface. Because Earth is an oblate spheroid, $R$ is smaller at the poles and larger at the equator: $g_{\\text{poles}} > g_{\\text{equator}}$. Moreover, $g$ decreases with both altitude ($h$) and depth ($d$), becoming exactly ZERO at the center of the Earth.",
                    "words": [
                        "Gravity",
                        "g maximum at poles",
                        "g minimum at equator",
                        "g zero at center",
                        "Altitude",
                        "Depth"
                    ],
                    "correct": "A person weighs maximum at the North/South poles and minimum at the equator; weight becomes zero at the center of the Earth.",
                    "incorrect": "A body weighs the same everywhere on Earth, or weight is maximum at the equator."
                },
                {
                    "rule_number": 2,
                    "title": "Total Internal Reflection (TIR) Conditions Rule",
                    "explanation": "TIR occurs ONLY when two strict conditions are met: (1) Light must travel from an optically denser medium to an optically rarer medium (e.g., glass to air, water to air); and (2) The angle of incidence ($i$) must exceed the critical angle ($\\theta_c$) for that pair of media.",
                    "words": [
                        "Total Internal Reflection",
                        "Denser to Rarer",
                        "Angle of Incidence > Critical Angle",
                        "Optical Fiber",
                        "Mirage"
                    ],
                    "correct": "Optical fibers transmit data with near-zero loss using Total Internal Reflection as light moves inside the denser core.",
                    "incorrect": "Total internal reflection occurs when light travels from air into water (rarer to denser)."
                },
                {
                    "rule_number": 3,
                    "title": "Speed of Sound Medium Dependency Rule",
                    "explanation": "Sound is a mechanical longitudinal wave requiring a material medium for propagation. It CANNOT travel through vacuum. The velocity of sound depends on the medium's elasticity and density: $v_{\\text{solids}} > v_{\\text{liquids}} > v_{\\text{gases}}$. Speed of sound in steel is $\\approx 5100\\text{ m/s}$, in water $\\approx 1480\\text{ m/s}$, and in dry air at $20^\\circ\\text{C}$ is $\\approx 343\\text{ m/s}$.",
                    "words": [
                        "Sound",
                        "Cannot travel in vacuum",
                        "Fastest in solids",
                        "Slowest in gases",
                        "Longitudinal wave"
                    ],
                    "correct": "Sound travels faster in steel (solid) than in water (liquid) and cannot propagate in a vacuum.",
                    "incorrect": "Sound travels faster in air than in steel, or sound can propagate through vacuum."
                },
                {
                    "rule_number": 4,
                    "title": "Eye Vision Defects & Lens Correction Rule",
                    "explanation": "Myopia (Short-sightedness): Distant objects appear blurry because image forms in front of the retina; corrected using a CONCAVE (diverging) lens. Hypermetropia (Long-sightedness): Near objects appear blurry because image forms behind the retina; corrected using a CONVEX (converging) lens.",
                    "words": [
                        "Myopia Concave",
                        "Hypermetropia Convex",
                        "Presbyopia Bifocal",
                        "Retina",
                        "Vision Correction"
                    ],
                    "correct": "Myopia is corrected by using a concave lens of appropriate focal length.",
                    "incorrect": "Myopia is corrected by wearing convex spectacles (convex lenses correct hypermetropia)."
                },
                {
                    "rule_number": 5,
                    "title": "Nuclear Energy: Fission vs. Fusion Distinction Rule",
                    "explanation": "Nuclear Fission: Heavy unstable nucleus (like Uranium-235 or Plutonium-239) splits into lighter nuclei with release of neutrons and energy (used in commercial Nuclear Reactors and Atomic Bombs). Nuclear Fusion: Light nuclei (Hydrogen isotopes like Deuterium and Tritium) combine at extremely high temperatures to form a heavier nucleus like Helium (source of energy in the Sun, stars, and Hydrogen Bombs).",
                    "words": [
                        "Fission heavy splits",
                        "Fusion light combines",
                        "Sun nuclear fusion",
                        "Nuclear reactor fission"
                    ],
                    "correct": "The energy radiated by the Sun and stars is generated by thermonuclear fusion of hydrogen into helium.",
                    "incorrect": "Solar energy is generated by nuclear fission of uranium in the solar core."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Believing that mass of an object changes when taken to the Moon.",
                    "correction": "Mass ($m$) is an invariant scalar quantity and remains constant everywhere in the universe. Only Weight ($W = mg$) changes because Moon's gravity is 1/6th of Earth's gravity.",
                    "rationale": "Candidates frequently confuse the fundamental quantity mass (kg) with the force weight (Newtons)."
                },
                {
                    "mistake": "Thinking that a transformer can be used to step up Direct Current (DC) voltage.",
                    "correction": "Transformers operate strictly on the principle of Mutual Induction, which requires a continuously changing magnetic flux produced only by Alternating Current (AC). In DC, flux is constant, so induced EMF is zero.",
                    "rationale": "Exam questions test the core working principle of electrical transformers."
                },
                {
                    "mistake": "Assuming sound travels faster in dry air than in humid air.",
                    "correction": "Sound travels faster in humid air than in dry air because humid air contains water vapor, which reduces the effective molecular mass of air, thereby reducing density and increasing acoustic velocity ($v \\propto 1/\\sqrt{\\rho}$).",
                    "rationale": "Density of water vapor ($18\\text{ g/mol}$) is less than dry air ($\u0007pprox 29\\text{ g/mol}$)."
                },
                {
                    "mistake": "Confusing the color of sky at sunset with dispersion instead of scattering.",
                    "correction": "The red/orange sky during sunset and sunrise is caused by Rayleigh scattering of light, where shorter blue wavelengths are scattered away over the long atmospheric path, leaving longer red wavelengths to reach our eyes.",
                    "rationale": "Dispersion splits white light into a spectrum via prism/raindrop, while scattering redirects wavelengths according to particle size."
                }
            ],
            "quick_revision_points": [
                "SI Fundamental Units: Length (m), Mass (kg), Time (s), Electric Current (A), Temperature (K), Amount of Substance (mol), Luminous Intensity (cd).",
                "Derived Units: Force = Newton (N = kg·m/s²), Work/Energy = Joule (J = N·m), Power = Watt (W = J/s), Pressure = Pascal (Pa = N/m²), Frequency = Hertz (Hz = 1/s).",
                "1 Horsepower (HP) = 746 Watts | 1 Commercial Unit of Electricity (1 kWh) = 3.6 × 10⁶ Joules.",
                "Acceleration due to gravity: g ≈ 9.8 m/s² on Earth; g_moon ≈ g_earth / 6. Value of g is maximum at poles, minimum at equator, zero at center of Earth.",
                "Escape Velocity: From Earth = 11.2 km/s; From Moon = 2.4 km/s (explaining why Moon has no atmosphere).",
                "Anomalous Expansion of Water: Water attains maximum density and minimum volume at 4°C (enabling aquatic life survival under frozen lakes).",
                "Speed of Light: In vacuum c = 3 × 10⁸ m/s; In water = 2.25 × 10⁸ m/s; In glass = 2 × 10⁸ m/s. Refractive index n = c/v.",
                "Total Internal Reflection (TIR): Requires light moving from denser to rarer medium and angle of incidence > critical angle. Explains optical fibers, mirages, and diamond sparkle.",
                "Scattering of Light: Rayleigh Scattering Intensity ∝ 1/λ⁴. Shorter blue wavelengths scatter most (blue sky), longer red wavelengths penetrate dust/fog (danger signals are red).",
                "Human Eye: Least distance of distinct vision = 25 cm. Myopia (nearsightedness) corrected by concave lens; Hypermetropia (farsightedness) corrected by convex lens.",
                "Electric Circuit Laws: Ohm's Law V = IR. In series, Current (I) remains constant; in parallel, Voltage (V) remains constant.",
                "Transformers: Operate exclusively on AC through mutual induction. Step-up transformer increases voltage, step-down decreases voltage.",
                "Nuclear Physics: Nuclear Fission powers nuclear reactors (U-235, controlled chain reaction with cadmium control rods and heavy water/graphite moderator). Nuclear Fusion powers the Sun."
            ]
        },
        "previous_year_questions": [
            {
                "id": 6301,
                "topic_id": 63,
                "exam_id": 1,
                "question": "Which of the following optical phenomena is primarily responsible for the sparkling and brilliance of diamonds? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Total Internal Reflection",
                    "Diffraction of light",
                    "Scattering of light",
                    "Polarization of light"
                ],
                "correct_answer": "Total Internal Reflection",
                "explanation": "Diamonds have an extraordinarily high refractive index (approx 2.42) and a very small critical angle (approx 24.4°). Light entering a properly cut diamond undergoes multiple total internal reflections before exiting, producing dazzling brilliance.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6302,
                "topic_id": 63,
                "exam_id": 1,
                "question": "What is the escape velocity of an object projected from the surface of the Earth? [UPSC CDS 2022]",
                "options_json": [
                    "7.9 km/s",
                    "9.8 km/s",
                    "11.2 km/s",
                    "15.4 km/s"
                ],
                "correct_answer": "11.2 km/s",
                "explanation": "The escape velocity from the surface of the Earth is given by v_e = sqrt(2gR), which calculates to approximately 11.2 km/s. Any projectile launched at or above this speed overcomes Earth's gravitational field without further propulsion.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6303,
                "topic_id": 63,
                "exam_id": 1,
                "question": "At what temperature does water exhibit its maximum density? [RRB NTPC 2021]",
                "options_json": [
                    "0°C",
                    "4°C",
                    "-4°C",
                    "100°C"
                ],
                "correct_answer": "4°C",
                "explanation": "Due to the anomalous expansion of water, as water cools from 10°C, it contracts until it reaches 4°C where its density is maximum (1.000 g/cm³). Below 4°C, it expands, causing ice at 0°C to be less dense and float on water.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 6301,
                "topic_id": 63,
                "question": "Which type of lens is prescribed to correct the eye defect known as Myopia (short-sightedness)?",
                "options_json": [
                    "Convex lens",
                    "Concave lens",
                    "Bifocal lens",
                    "Cylindrical lens"
                ],
                "correct_answer": "Concave lens",
                "explanation": "Myopia occurs when the eyeball is too long or the cornea is too curved, causing rays to focus in front of the retina. A diverging (concave) lens is used to diverge the incoming light rays so they focus properly on the retina.",
                "points": 1
            },
            {
                "id": 6302,
                "topic_id": 63,
                "question": "Why are danger signal lights always red in color?",
                "options_json": [
                    "Red light has the shortest wavelength and scatters most",
                    "Red light has the longest wavelength and scatters least",
                    "Red light is absorbed completely by atmospheric moisture",
                    "Red light moves faster than all other colors in air"
                ],
                "correct_answer": "Red light has the longest wavelength and scatters least",
                "explanation": "According to Rayleigh's law of scattering, scattering intensity is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴). Since red light has the longest visible wavelength (~700 nm), it scatters the least through fog and dust and remains visible from large distances.",
                "points": 1
            },
            {
                "id": 6303,
                "topic_id": 63,
                "question": "A hydraulic press or hydraulic brake system operates on which fundamental physical principle?",
                "options_json": [
                    "Archimedes' Principle",
                    "Pascal's Law",
                    "Bernoulli's Principle",
                    "Boyle's Law"
                ],
                "correct_answer": "Pascal's Law",
                "explanation": "Pascal's Law states that pressure applied to an enclosed fluid is transmitted undiminished in all directions to all portions of the fluid and walls of the container, enabling hydraulic lift and braking systems.",
                "points": 1
            },
            {
                "id": 6304,
                "topic_id": 63,
                "question": "One kilowatt-hour (1 kWh) of commercial electrical energy is equivalent to how many Joules?",
                "options_json": [
                    "3.6 × 10⁵ J",
                    "3.6 × 10⁶ J",
                    "1.0 × 10³ J",
                    "7.46 × 10² J"
                ],
                "correct_answer": "3.6 × 10⁶ J",
                "explanation": "1 kWh = 1,000 Watts × 3,600 seconds = 3,600,000 Joules = 3.6 × 10⁶ J.",
                "points": 1
            },
            {
                "id": 6305,
                "topic_id": 63,
                "question": "Why does a spinning cricket ball or an aircraft wing experience aerodynamic lift?",
                "options_json": [
                    "Archimedes' Principle",
                    "Bernoulli's Theorem",
                    "Kepler's Law",
                    "Newton's Law of Cooling"
                ],
                "correct_answer": "Bernoulli's Theorem",
                "explanation": "Bernoulli's Theorem states that an increase in the speed of a fluid occurs simultaneously with a decrease in static pressure. The curved upper surface creates higher air speed and lower pressure above, generating upward lift (Magnus effect in balls, airfoil lift in planes).",
                "points": 1
            },
            {
                "id": 6306,
                "topic_id": 63,
                "question": "In which medium does sound travel with the highest velocity?",
                "options_json": [
                    "Vacuum",
                    "Dry Air",
                    "Water",
                    "Steel"
                ],
                "correct_answer": "Steel",
                "explanation": "Sound velocity is highest in elastic solids like steel (approx 5,100 m/s), lower in liquids like water (approx 1,480 m/s), lowest in gases like air (approx 343 m/s), and strictly zero in a vacuum.",
                "points": 1
            },
            {
                "id": 6307,
                "topic_id": 63,
                "question": "What is the primary source of nuclear energy continuously produced in the core of the Sun?",
                "options_json": [
                    "Nuclear Fission of Uranium",
                    "Nuclear Fusion of Hydrogen into Helium",
                    "Combustion of Methane Gas",
                    "Radioactive Beta Decay"
                ],
                "correct_answer": "Nuclear Fusion of Hydrogen into Helium",
                "explanation": "The core of the Sun operates as a massive thermonuclear reactor where hydrogen nuclei fuse to form helium under tremendous gravitational pressure and temperature (approx 15 million Kelvin), releasing vast energy.",
                "points": 1
            },
            {
                "id": 6308,
                "topic_id": 63,
                "question": "What is the value of acceleration due to gravity (g) at the center of the Earth?",
                "options_json": [
                    "9.8 m/s²",
                    "Infinite",
                    "Zero",
                    "4.9 m/s²"
                ],
                "correct_answer": "Zero",
                "explanation": "At the center of the Earth, gravitational attraction from surrounding mass in all directions cancels out symmetrically, resulting in a net gravitational acceleration of exactly zero.",
                "points": 1
            },
            {
                "id": 6309,
                "topic_id": 63,
                "question": "Which device transforms mechanical energy into alternating electrical energy using electromagnetic induction?",
                "options_json": [
                    "Electric Motor",
                    "Electric Generator (Dynamo)",
                    "Transformer",
                    "Galvanometer"
                ],
                "correct_answer": "Electric Generator (Dynamo)",
                "explanation": "An electric generator (dynamo) converts mechanical rotational energy into electrical energy based on Faraday's law of electromagnetic induction.",
                "points": 1
            },
            {
                "id": 6310,
                "topic_id": 63,
                "question": "What is the least distance of distinct vision (near point) for a healthy normal human eye?",
                "options_json": [
                    "10 cm",
                    "25 cm",
                    "50 cm",
                    "Infinite"
                ],
                "correct_answer": "25 cm",
                "explanation": "For an average healthy adult human eye, the closest distance at which an object can be clearly focused without eye strain is 25 cm.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 6301,
                "topic_id": 63,
                "question": "Newton's First Law of Motion is also widely known as the Law of:",
                "options_json": [
                    "Inertia",
                    "Momentum",
                    "Conservation of Energy",
                    "Action and Reaction"
                ],
                "correct_answer": "Inertia",
                "explanation": "Newton's First Law states that an object remains at rest or in uniform motion unless acted upon by an external unbalanced force. This tendency to resist changes in state of motion is termed inertia.",
                "points": 1
            },
            {
                "id": 6302,
                "topic_id": 63,
                "question": "Where on Earth's surface is the acceleration due to gravity (g) maximum?",
                "options_json": [
                    "At the Equator",
                    "At the North and South Poles",
                    "At the Tropic of Cancer",
                    "At 45° latitude"
                ],
                "correct_answer": "At the North and South Poles",
                "explanation": "Since Earth is flattened at the poles, polar radius is approximately 21 km less than equatorial radius. Since g = GM/R², g is maximum at the poles and minimum at the equator.",
                "points": 1
            },
            {
                "id": 6303,
                "topic_id": 63,
                "question": "A device used to step up or step down alternating voltage based on mutual induction is a:",
                "options_json": [
                    "Rectifier",
                    "Transformer",
                    "Transistor",
                    "Capacitor"
                ],
                "correct_answer": "Transformer",
                "explanation": "A transformer changes AC voltage levels through electromagnetic mutual induction between its primary and secondary coils. It does not work on DC.",
                "points": 1
            },
            {
                "id": 6304,
                "topic_id": 63,
                "question": "Optical fibers communicate signals over long distances with minimal loss using:",
                "options_json": [
                    "Total Internal Reflection",
                    "Light Dispersion",
                    "Diffraction",
                    "Refraction"
                ],
                "correct_answer": "Total Internal Reflection",
                "explanation": "Light rays enter the optical fiber core at an angle greater than the critical angle, undergoing continuous total internal reflection along the fiber length.",
                "points": 1
            },
            {
                "id": 6305,
                "topic_id": 63,
                "question": "The blue color of the clear daytime sky is caused by which optical phenomenon?",
                "options_json": [
                    "Rayleigh Scattering",
                    "Light Dispersion",
                    "Total Internal Reflection",
                    "Polarization"
                ],
                "correct_answer": "Rayleigh Scattering",
                "explanation": "Molecules in the atmosphere scatter sunlight. Because blue light has a shorter wavelength, it is scattered much more strongly across the sky than longer wavelengths.",
                "points": 1
            },
            {
                "id": 6306,
                "topic_id": 63,
                "question": "What happens to the weight of an astronaut on the Moon compared to Earth?",
                "options_json": [
                    "Increases by 6 times",
                    "Remains exactly the same",
                    "Reduces to 1/6th of Earth weight",
                    "Becomes zero"
                ],
                "correct_answer": "Reduces to 1/6th of Earth weight",
                "explanation": "Because the Moon's mass and radius produce a surface gravity that is roughly 1/6th of Earth's gravity, weight (W = mg) becomes 1/6th, while mass remains unchanged.",
                "points": 1
            },
            {
                "id": 6307,
                "topic_id": 63,
                "question": "In a nuclear reactor, what material is commonly used as a moderator to slow down fast neutrons?",
                "options_json": [
                    "Heavy water (D₂O) or Graphite",
                    "Cadmium rods",
                    "Liquid Sodium",
                    "Lead"
                ],
                "correct_answer": "Heavy water (D₂O) or Graphite",
                "explanation": "Heavy water (Deuterium oxide) and high-purity graphite are used as moderators to slow down fission neutrons to thermal energies so they can trigger further fission in U-235.",
                "points": 1
            },
            {
                "id": 6308,
                "topic_id": 63,
                "question": "The audible sound frequency range perceptible to normal human hearing is:",
                "options_json": [
                    "2 Hz to 200 Hz",
                    "20 Hz to 20,000 Hz",
                    "200 Hz to 200,000 Hz",
                    "Above 25,000 Hz"
                ],
                "correct_answer": "20 Hz to 20,000 Hz",
                "explanation": "Human hearing spans approximately 20 Hz to 20,000 Hz (20 kHz). Frequencies below 20 Hz are infrasonic, and those above 20 kHz are ultrasonic.",
                "points": 1
            },
            {
                "id": 6309,
                "topic_id": 63,
                "question": "Which eye condition is characterized by difficulty in viewing nearby objects clearly and corrected by convex lenses?",
                "options_json": [
                    "Myopia",
                    "Hypermetropia",
                    "Astigmatism",
                    "Cataract"
                ],
                "correct_answer": "Hypermetropia",
                "explanation": "Hypermetropia (far-sightedness) causes images of near objects to focus behind the retina. A convex converging lens brings the focal point forward onto the retina.",
                "points": 1
            },
            {
                "id": 6310,
                "topic_id": 63,
                "question": "Why does rain take the shape of spherical drops in free fall?",
                "options_json": [
                    "Atmospheric Viscosity",
                    "Surface Tension",
                    "Gravitational Collapse",
                    "Centrifugal Force"
                ],
                "correct_answer": "Surface Tension",
                "explanation": "Surface tension pulls the surface molecules of a liquid inward to minimize surface area. For a given volume, a sphere has the minimum surface area.",
                "points": 1
            },
            {
                "id": 6311,
                "topic_id": 63,
                "question": "What is the SI unit of electric potential difference (voltage)?",
                "options_json": [
                    "Ampere",
                    "Volt",
                    "Ohm",
                    "Coulomb"
                ],
                "correct_answer": "Volt",
                "explanation": "The Volt (V) is the SI unit of electric potential and electromotive force, defined as one Joule per Coulomb.",
                "points": 1
            },
            {
                "id": 6312,
                "topic_id": 63,
                "question": "When a ship sails from a freshwater river into the salty ocean, what happens to its floatation level?",
                "options_json": [
                    "It sinks slightly deeper",
                    "It rises slightly higher",
                    "It remains at the exact same level",
                    "It capsizes"
                ],
                "correct_answer": "It rises slightly higher",
                "explanation": "Sea water has dissolved salts and higher density than fresh river water. Because buoyant force equals weight of displaced liquid, less volume of denser sea water is displaced, making the ship rise.",
                "points": 1
            },
            {
                "id": 6313,
                "topic_id": 63,
                "question": "The apparent shift in frequency of sound or light due to relative motion between source and observer is called the:",
                "options_json": [
                    "Compton Effect",
                    "Doppler Effect",
                    "Raman Effect",
                    "Zeeman Effect"
                ],
                "correct_answer": "Doppler Effect",
                "explanation": "The Doppler Effect describes how observed frequency increases when source and observer approach each other and decreases when they move apart.",
                "points": 1
            },
            {
                "id": 6314,
                "topic_id": 63,
                "question": "Which of the following is a fundamental scalar physical quantity?",
                "options_json": [
                    "Velocity",
                    "Acceleration",
                    "Mass",
                    "Force"
                ],
                "correct_answer": "Mass",
                "explanation": "Mass has only magnitude and no spatial direction, making it a scalar quantity. Velocity, acceleration, and force are vector quantities having both magnitude and direction.",
                "points": 1
            },
            {
                "id": 6315,
                "topic_id": 63,
                "question": "What is the power of a convex lens whose focal length is 50 cm (+0.5 m)?",
                "options_json": [
                    "+1.0 Dioptre",
                    "+2.0 Dioptre",
                    "+0.5 Dioptre",
                    "+4.0 Dioptre"
                ],
                "correct_answer": "+2.0 Dioptre",
                "explanation": "Power P (in Dioptres) = 1 / f(in meters). Here f = +0.5 m, so P = 1 / 0.5 = +2.0 D.",
                "points": 1
            },
            {
                "id": 6316,
                "topic_id": 63,
                "question": "In a household electric circuit, domestic appliances are wired in:",
                "options_json": [
                    "Series circuit",
                    "Parallel circuit",
                    "Combination with alternating current bridge",
                    "Open loop circuit"
                ],
                "correct_answer": "Parallel circuit",
                "explanation": "Household circuits are connected in parallel so each appliance receives the full rated voltage (220 V in India) and can operate independently without affecting others.",
                "points": 1
            },
            {
                "id": 6317,
                "topic_id": 63,
                "question": "Einstein was awarded the 1921 Nobel Prize in Physics specifically for his explanation of:",
                "options_json": [
                    "Special Theory of Relativity",
                    "General Theory of Relativity",
                    "Photoelectric Effect",
                    "Brownian Motion"
                ],
                "correct_answer": "Photoelectric Effect",
                "explanation": "Albert Einstein received the 1921 Nobel Prize in Physics 'for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect' using quantum packets (photons).",
                "points": 1
            },
            {
                "id": 6318,
                "topic_id": 63,
                "question": "Which instrument is used to measure atmospheric pressure?",
                "options_json": [
                    "Barometer",
                    "Hydrometer",
                    "Manometer",
                    "Anemometer"
                ],
                "correct_answer": "Barometer",
                "explanation": "The mercury or aneroid barometer, invented by Evangelista Torricelli, measures atmospheric pressure.",
                "points": 1
            },
            {
                "id": 6319,
                "topic_id": 63,
                "question": "Cadmium rods are inserted into a nuclear reactor core to serve what purpose?",
                "options_json": [
                    "To accelerate neutrons",
                    "To absorb excess neutrons and control the chain reaction",
                    "To cool the reactor fuel",
                    "To produce tritium"
                ],
                "correct_answer": "To absorb excess neutrons and control the chain reaction",
                "explanation": "Cadmium and Boron have high neutron absorption cross-sections. Control rods are lowered or raised to capture neutrons and safely control the rate of fission.",
                "points": 1
            },
            {
                "id": 6320,
                "topic_id": 63,
                "question": "The twinkling of stars in the night sky is an optical effect produced by:",
                "options_json": [
                    "Atmospheric Refraction through layers of varying air density",
                    "Internal reflection within interstellar clouds",
                    "Periodic solar flares",
                    "Diffraction of light by cosmic dust"
                ],
                "correct_answer": "Atmospheric Refraction through layers of varying air density",
                "explanation": "Starlight enters Earth's atmosphere and bends continuously through shifting layers of air of varying refractive indices, causing the apparent position and intensity to fluctuate (twinkle).",
                "points": 1
            }
        ]
    },
    "64": {
        "title": "Chemistry: Atomic Structure, Periodic Table Trends, Chemical Bonding, Acids, Bases, Salts, Metallurgy & Everyday Polymers",
        "source_id": 7,
        "content": {
            "definition": "Chemistry in competitive examinations (UPSC, SSC CGL/CHSL Tier 1/2, RRB NTPC/JE, CDS, State PSCs) examines the composition, structure, properties, and reactions of matter. The syllabus encompasses fundamental atomic models, modern periodic table classifications and periodic trends, chemical bonding, acid-base-salt equilibria and pH scales, extraction of metals and metallurgy, alloys, electrochemistry, and organic chemistry applications including polymers, soaps, detergents, fuels, and daily household compounds.",
            "overview": "Comprehensive Chemical Science Framework:\n- Atomic Structure & Models: Subatomic particles (Electron discovered by J.J. Thomson, Proton by E. Goldstein/Rutherford, Neutron by James Chadwick 1932); Thomson's Plum Pudding Model; Rutherford's Alpha Scattering Experiment (discovery of dense positive nucleus); Bohr's Model (quantized energy levels); Quantum numbers; Isotopes (same atomic number $Z$, different mass number $A$, e.g., Protium, Deuterium, Tritium), Isobars (same $A$, different $Z$), Isotones (same number of neutrons)\n- Modern Periodic Table & Trends: Moseley's Modern Periodic Law (properties are periodic functions of atomic numbers); 7 Periods and 18 Groups; Periodic Trends: Atomic radius decreases across a period (left to right) and increases down a group; Ionization energy and Electronegativity increase across a period and decrease down a group; Fluorine is the most electronegative element; Francium/Cesium are the most electropositive\n- Chemical Bonding: Ionic/Electrovalent bond (complete electron transfer, high melting/boiling points, conduct in molten/aqueous states); Covalent bond (electron sharing); Coordinate/Dative bond; Hydrogen bonding (explains high boiling point of water and double helix structure of DNA)\n- Acids, Bases & Salts: Arrhenius, Bronsted-Lowry, and Lewis concepts; pH scale ($0-14$, Sorenson 1909; $\\text{pH} = -\\log_{10}[\\text{H}^+]$); Universal and natural indicators (Litmus turns red in acid and blue in base; Phenolphthalein is colorless in acid and pink in base; Methyl orange is red in acid and yellow in base); Common salts: Baking Soda ($\\text{NaHCO}_3$, Sodium hydrogen carbonate), Washing Soda ($\\text{Na}_2\\text{CO}_3\\cdot 10\\text{H}_2\\text{O}$), Bleaching Powder ($\\text{CaOCl}_2$, Calcium hypochlorite), Plaster of Paris ($\\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O}$), Gypsum ($\\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O}$)\n- Metals, Non-Metals & Metallurgy: Reactivity series of metals (K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au); Ores (Bauxite for Aluminium, Haematite/Magnetite for Iron, Cinnabar for Mercury, Galena for Lead); Extraction processes (Roasting, Calcination, Smelting); Important Alloys (Brass = $\\text{Cu} + \\text{Zn}$; Bronze = $\\text{Cu} + \\text{Sn}$; Solder = $\\text{Pb} + \\text{Sn}$; Stainless Steel = $\\text{Fe} + \\text{Cr} + \\text{Ni} + \\text{C}$; German Silver = $\\text{Cu} + \\text{Zn} + \\text{Ni}$ containing NO silver!)\n- Electrochemistry & Corrosion: Galvanic/Voltaic cell; Rusting of iron ($2\\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O}$, requires both oxygen and water); Prevention: Galvanization (coating iron with Zinc); Cathodic protection\n- Organic Chemistry & Daily Materials: Hydrocarbons (Alkanes $C_n H_{2n+2}$, Alkenes $C_n H_{2n}$, Alkynes $C_n H_{2n-2}$, Aromatic Benzene $C_6H_6$); Commercial fuels (LPG mainly Butane + Propane with Ethyl Mercaptan odorant; CNG mainly Methane $\\text{CH}_4$); Polymers: Natural (cellulose, natural rubber with isoprene monomer) vs Synthetic (Polythene, PVC, Teflon / PTFE, Nylon 6,6, Bakelite, Rayon / artificial silk); Soaps (sodium/potassium salts of fatty acids) vs Detergents (cleans in hard water containing $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions)",
            "types": [
                {
                    "name": "1. Atomic Structure & Subatomic Particles",
                    "desc": "Particle discoveries, nuclear structure, electron configurations, and isotopes.",
                    "examples": [
                        "Electron (J.J. Thomson) • Proton (Goldstein/Rutherford) • Neutron (James Chadwick 1932)",
                        "Isotopes of Hydrogen: Protium (¹H), Deuterium (²H - heavy water D₂O), Tritium (³H - radioactive)"
                    ]
                },
                {
                    "name": "2. Modern Periodic Table & Periodic Trends",
                    "desc": "Arrangement by atomic number (Moseley) and systematic property trends.",
                    "examples": [
                        "Electronegativity: Maximum in Fluorine (F), minimum in Francium/Cesium",
                        "Atomic Radius: Decreases across a period (left to right), increases down a group",
                        "Noble Gases (Group 18): Chemically inert full valence shell (Helium, Neon, Argon, Radon)"
                    ]
                },
                {
                    "name": "3. Acids, Bases, Salts & pH Chemistry",
                    "desc": "pH scale, neutralization, chemical indicators, and commercial inorganic salts.",
                    "examples": [
                        "Baking Soda (NaHCO₃) • Washing Soda (Na₂CO₃·10H₂O) • Bleaching Powder (CaOCl₂)",
                        "Plaster of Paris (CaSO₄·½H₂O) prepared by heating Gypsum (CaSO₄·2H₂O) at 373 K",
                        "Acid Rain: Rainwater with pH < 5.6 caused by SO₂ and NO₂ atmospheric emissions"
                    ]
                },
                {
                    "name": "4. Metallurgy, Ores & Commercial Alloys",
                    "desc": "Metal extraction, reactivity series, and widely used industrial alloys.",
                    "examples": [
                        "Brass: Copper + Zinc • Bronze: Copper + Tin • Solder: Lead + Tin",
                        "German Silver: Copper + Zinc + Nickel (Note: Contains 0% Silver!)",
                        "Galvanization: Coating steel or iron with a sacrificial layer of Zinc to prevent rust"
                    ]
                },
                {
                    "name": "5. Organic Compounds, Fuels & Daily Polymers",
                    "desc": "Hydrocarbons, cooking gases, thermosetting plastics, and detergents.",
                    "examples": [
                        "LPG (Liquefied Petroleum Gas): Primarily Butane and Propane with Ethyl Mercaptan odorant",
                        "CNG (Compressed Natural Gas): Primarily Methane (CH₄, 85-90%)",
                        "Teflon (PTFE): Non-stick cookware coating • Bakelite: Electrical switches (thermosetting)"
                    ]
                }
            ],
            "rules": [
                {
                    "rule_number": 1,
                    "title": "Modern Periodic Law & Atomic Number Basis Rule",
                    "explanation": "Mendeleev organized elements by Atomic Mass, leading to anomalies. Henry Moseley (1913) formulated the Modern Periodic Law: properties of elements are periodic functions of their ATOMIC NUMBER (nuclear charge Z). This placed elements strictly by electronic configuration into 7 periods and 18 groups.",
                    "words": [
                        "Modern Periodic Law",
                        "Atomic Number",
                        "Henry Moseley",
                        "Periods 7",
                        "Groups 18"
                    ],
                    "correct": "The Modern Periodic Table is arranged in increasing order of atomic numbers, not atomic masses.",
                    "incorrect": "The modern periodic table is classified on the basis of increasing atomic masses."
                },
                {
                    "rule_number": 2,
                    "title": "Periodic Table Trends Directionality Rule",
                    "explanation": "Remember the diagonal trend: Ionization Energy, Electron Affinity, and Electronegativity INCREASE from bottom-left to top-right (Fluorine is highest). Conversely, Atomic Radius and Metallic Character INCREASE from top-right to bottom-left (Cesium/Francium is largest and most metallic).",
                    "words": [
                        "Electronegativity increases across period",
                        "Atomic radius increases down group",
                        "Fluorine highest",
                        "Cesium lowest"
                    ],
                    "correct": "Across a period from left to right, electronegativity increases and atomic size decreases.",
                    "incorrect": "Atomic radius increases across a period from left to right."
                },
                {
                    "rule_number": 3,
                    "title": "Gypsum to Plaster of Paris Dehydration Rule",
                    "explanation": "Gypsum is Calcium Sulphate Dihydrate ($CaSO_4 \\cdot 2H_2O$). When carefully heated to $373\\text{ K}$ ($100^\\circ\\text{C}$), it loses three-fourths of its water of crystallization to form Plaster of Paris (POP, Calcium Sulphate Hemihydrate $CaSO_4 \\cdot \\frac{1}{2}H_2O$). When mixed with water, POP sets into a hard solid mass by reverting to Gypsum.",
                    "words": [
                        "Gypsum CaSO4.2H2O",
                        "Plaster of Paris CaSO4.1/2H2O",
                        "373 K heating",
                        "Hemihydrate"
                    ],
                    "correct": "Plaster of Paris is calcium sulphate hemihydrate ($CaSO_4 \\cdot 0.5H_2O$).",
                    "incorrect": "Plaster of Paris is calcium sulphate dihydrate ($CaSO_4 \\cdot 2H_2O$)."
                },
                {
                    "rule_number": 4,
                    "title": "Alloy Composition Disambiguation Rule",
                    "explanation": "Brass = Copper ($70\\%$) + Zinc ($30\\%$); Bronze = Copper ($90\\%$) + Tin ($10\\%$); German Silver = Copper + Zinc + Nickel (contains ZERO percent silver!); Solder = Lead + Tin (low melting point for electronics).",
                    "words": [
                        "Brass Copper Zinc",
                        "Bronze Copper Tin",
                        "German Silver No Silver",
                        "Solder Lead Tin"
                    ],
                    "correct": "German Silver is an alloy composed of Copper, Zinc, and Nickel with no silver present.",
                    "incorrect": "German Silver contains 25% elemental silver."
                },
                {
                    "rule_number": 5,
                    "title": "LPG Odorant & Fuel Composition Rule",
                    "explanation": "Liquefied Petroleum Gas (LPG) consists mainly of butane and propane, which are naturally odorless. To detect dangerous gas leaks, a foul-smelling sulfur compound called Ethyl Mercaptan ($C_2H_5SH$) is deliberately added.",
                    "words": [
                        "LPG Butane Propane",
                        "Ethyl Mercaptan Odorant",
                        "CNG Methane"
                    ],
                    "correct": "Ethyl mercaptan is added to domestic LPG cylinders to provide a strong detectable odor for leak detection.",
                    "incorrect": "Pure butane has a naturally pungent rotting smell."
                }
            ],
            "common_mistakes": [
                {
                    "mistake": "Thinking 'German Silver' contains silver.",
                    "correction": "German Silver contains Copper (50%), Zinc (30%), and Nickel (20%). It is named solely for its silvery appearance and contains 0% silver.",
                    "rationale": "Examiners routinely include 'Silver' in MCQ options to trap unwary candidates."
                },
                {
                    "mistake": "Confusing Baking Soda with Washing Soda formulas.",
                    "correction": "Baking Soda is Sodium Hydrogen Carbonate ($NaHCO_3$), while Washing Soda is Sodium Carbonate Decahydrate ($Na_2CO_3 \\cdot 10H_2O$).",
                    "rationale": "Both are sodium carbonate salts, but baking soda contains hydrogen ('bi-carbonate')."
                },
                {
                    "mistake": "Assuming rust formation requires only oxygen.",
                    "correction": "Rusting of iron requires BOTH oxygen ($O_2$) and moisture/water ($H_2O$). In dry air or air-free boiled water, iron does not rust.",
                    "rationale": "Rusting is an electrochemical corrosion process needing both oxidizing agent and electrolytic medium."
                },
                {
                    "mistake": "Believing hard water can be effectively cleaned using ordinary soap.",
                    "correction": "Ordinary soaps react with $Ca^{2+}$ and $Mg^{2+}$ ions in hard water to form an insoluble white precipitate called 'scum', wasting soap. Synthetic detergents do not form scum and clean efficiently in hard water.",
                    "rationale": "Soaps form insoluble calcium and magnesium stearates, whereas alkyl benzene sulfonates in detergents remain soluble."
                }
            ],
            "quick_revision_points": [
                "Atomic Particles: Electron (J.J. Thomson), Proton (E. Goldstein/Rutherford), Neutron (James Chadwick 1932).",
                "Atomic Number (Z) = Number of protons in nucleus. Mass Number (A) = Protons + Neutrons.",
                "Modern Periodic Law (Moseley 1913): Elements are arranged in 7 periods and 18 groups by increasing atomic number.",
                "Periodic Trends: Electronegativity and Ionization Energy increase from left to right; Atomic Radius increases from top to bottom.",
                "Most Electronegative element = Fluorine (F). Most Electropositive element = Cesium (Cs) / Francium (Fr).",
                "pH Scale: Acidic < 7, Neutral = 7 (pure water at 25°C), Basic > 7. Human blood pH is strictly maintained around 7.35 - 7.45.",
                "Litmus Indicator: Red in acidic solution, Blue in basic solution. Phenolphthalein: Colorless in acid, Pink in base.",
                "Baking Soda = Sodium Bicarbonate (NaHCO₃). Washing Soda = Sodium Carbonate Decahydrate (Na₂CO₃·10H₂O).",
                "Bleaching Powder = Calcium Hypochlorite (CaOCl₂). Quicklime = CaO. Slaked Lime = Ca(OH)₂.",
                "Plaster of Paris (POP) = CaSO₄·½H₂O (Calcium sulphate hemihydrate), prepared by heating Gypsum (CaSO₄·2H₂O) to 373 K.",
                "Key Alloys: Brass (Cu + Zn), Bronze (Cu + Sn), German Silver (Cu + Zn + Ni, NO silver), Solder (Pb + Sn), Amalgam (alloy with Mercury).",
                "Galvanization: Coating iron or steel with a protective layer of Zinc to prevent rusting.",
                "LPG = Liquefied Petroleum Gas (Butane + Propane; Ethyl Mercaptan odorant added for leak detection). CNG = Compressed Natural Gas (mainly Methane CH₄).",
                "Polymers: Teflon (Polytetrafluoroethylene - non-stick cookware), Bakelite (thermosetting plastic - electrical switches), PVC (polyvinyl chloride - pipes)."
            ]
        },
        "previous_year_questions": [
            {
                "id": 6401,
                "topic_id": 64,
                "exam_id": 1,
                "question": "Which of the following elements is the most electronegative element in the Modern Periodic Table? [SSC CGL 2023 Tier 1]",
                "options_json": [
                    "Chlorine",
                    "Fluorine",
                    "Oxygen",
                    "Nitrogen"
                ],
                "correct_answer": "Fluorine",
                "explanation": "Fluorine (F, atomic number 9) has the highest electronegativity of all elements on the Pauling scale (approx 3.98), owing to its small atomic radius and high effective nuclear charge.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6402,
                "topic_id": 64,
                "exam_id": 1,
                "question": "What is the chemical formula of Plaster of Paris? [UPSC CDS 2022]",
                "options_json": [
                    "CaSO₄ · 2H₂O",
                    "CaSO₄ · ½H₂O",
                    "CaSO₄ · 5H₂O",
                    "CaSO₄ · 10H₂O"
                ],
                "correct_answer": "CaSO₄ · ½H₂O",
                "explanation": "Plaster of Paris is calcium sulphate hemihydrate, represented by the formula CaSO₄ · ½H₂O (or 2CaSO₄ · H₂O). It is produced by heating gypsum (CaSO₄ · 2H₂O) to 373 K.",
                "source_id": 7,
                "status": "published"
            },
            {
                "id": 6403,
                "topic_id": 64,
                "exam_id": 1,
                "question": "German Silver is an alloy consisting of which of the following combinations of metals? [RRB NTPC 2021]",
                "options_json": [
                    "Copper, Silver, and Nickel",
                    "Copper, Zinc, and Nickel",
                    "Silver, Zinc, and Tin",
                    "Copper, Lead, and Silver"
                ],
                "correct_answer": "Copper, Zinc, and Nickel",
                "explanation": "German Silver is composed of approximately 50% Copper, 30% Zinc, and 20% Nickel. Despite its deceptive name, it contains zero percent elemental silver.",
                "source_id": 7,
                "status": "published"
            }
        ],
        "practice_questions": [
            {
                "id": 6401,
                "topic_id": 64,
                "question": "What chemical compound is added to commercial domestic LPG cylinders to provide a distinct warning odor during gas leaks?",
                "options_json": [
                    "Methane",
                    "Ethyl Mercaptan",
                    "Carbon Monoxide",
                    "Sulfur Dioxide"
                ],
                "correct_answer": "Ethyl Mercaptan",
                "explanation": "Butane and propane are odorless gases. Ethyl mercaptan (ethanethiol, C₂H₅SH) is a strongly scented sulfur compound blended in minute amounts to warn of gas leaks.",
                "points": 1
            },
            {
                "id": 6402,
                "topic_id": 64,
                "question": "What is the common chemical name of Baking Soda?",
                "options_json": [
                    "Sodium Carbonate",
                    "Sodium Hydrogen Carbonate (Sodium Bicarbonate)",
                    "Calcium Carbonate",
                    "Sodium Hydroxide"
                ],
                "correct_answer": "Sodium Hydrogen Carbonate (Sodium Bicarbonate)",
                "explanation": "Baking Soda is sodium hydrogen carbonate (NaHCO₃). Upon heating, it releases carbon dioxide gas, causing dough and batter to rise and become spongy.",
                "points": 1
            },
            {
                "id": 6403,
                "topic_id": 64,
                "question": "Galvanization is the industrial process of protecting iron from corrosion by coating it with a thin layer of which metal?",
                "options_json": [
                    "Tin",
                    "Zinc",
                    "Copper",
                    "Aluminium"
                ],
                "correct_answer": "Zinc",
                "explanation": "Galvanization coats iron with metallic zinc. Zinc acts as a physical barrier and sacrificial anode because zinc oxidizes preferentially over iron even if scratched.",
                "points": 1
            },
            {
                "id": 6404,
                "topic_id": 64,
                "question": "What is the normal physiological pH range of healthy human arterial blood?",
                "options_json": [
                    "6.00 - 6.50",
                    "7.35 - 7.45",
                    "7.80 - 8.20",
                    "5.50 - 6.00"
                ],
                "correct_answer": "7.35 - 7.45",
                "explanation": "Human blood is slightly basic, strictly regulated between 7.35 and 7.45 by the carbonic acid-bicarbonate buffer system.",
                "points": 1
            },
            {
                "id": 6405,
                "topic_id": 64,
                "question": "Which polymer is widely utilized in the manufacturing of non-stick coatings on cooking utensils?",
                "options_json": [
                    "Bakelite",
                    "PVC",
                    "Teflon (PTFE)",
                    "Polystyrene"
                ],
                "correct_answer": "Teflon (PTFE)",
                "explanation": "Teflon (Polytetrafluoroethylene or PTFE) has exceptional heat resistance, high chemical inertness, and an extremely low coefficient of friction, making it ideal for non-stick cookware.",
                "points": 1
            },
            {
                "id": 6406,
                "topic_id": 64,
                "question": "Which neutral gas constitutes the primary chemical component (approx 85-90%) of Compressed Natural Gas (CNG)?",
                "options_json": [
                    "Methane",
                    "Propane",
                    "Butane",
                    "Ethane"
                ],
                "correct_answer": "Methane",
                "explanation": "CNG is predominantly composed of methane (CH₄), which burns cleanly with low emissions compared to diesel or petrol.",
                "points": 1
            },
            {
                "id": 6407,
                "topic_id": 64,
                "question": "What is an amalgam?",
                "options_json": [
                    "An alloy of Iron and Carbon",
                    "An alloy where one of the constituent metals is Mercury",
                    "A radioactive isotope of Uranium",
                    "A colloidal solution of sulfur"
                ],
                "correct_answer": "An alloy where one of the constituent metals is Mercury",
                "explanation": "An amalgam is an alloy of mercury with another metal (e.g., silver-tin amalgam historically used in dental fillings). Iron, platinum, and tungsten do not readily form amalgams.",
                "points": 1
            },
            {
                "id": 6408,
                "topic_id": 64,
                "question": "Which subatomic particle was discovered by James Chadwick in 1932?",
                "options_json": [
                    "Electron",
                    "Proton",
                    "Neutron",
                    "Positron"
                ],
                "correct_answer": "Neutron",
                "explanation": "James Chadwick discovered the uncharged subatomic particle with mass approximately equal to that of a proton in 1932, naming it the neutron, for which he received the 1935 Nobel Prize.",
                "points": 1
            },
            {
                "id": 6409,
                "topic_id": 64,
                "question": "Brass is an alloy consisting of which two primary elemental metals?",
                "options_json": [
                    "Copper and Tin",
                    "Copper and Zinc",
                    "Iron and Chromium",
                    "Lead and Tin"
                ],
                "correct_answer": "Copper and Zinc",
                "explanation": "Brass is an alloy composed of Copper and Zinc. Bronze, by contrast, is composed of Copper and Tin.",
                "points": 1
            },
            {
                "id": 6410,
                "topic_id": 64,
                "question": "What is the chemical name and formula of Bleaching Powder?",
                "options_json": [
                    "Calcium Carbonate (CaCO₃)",
                    "Calcium Hypochlorite / Oxychloride (CaOCl₂)",
                    "Calcium Hydroxide (Ca(OH)₂)",
                    "Calcium Oxide (CaO)"
                ],
                "correct_answer": "Calcium Hypochlorite / Oxychloride (CaOCl₂)",
                "explanation": "Bleaching powder is calcium oxychloride (CaOCl₂), prepared by the action of dry chlorine gas on dry slaked lime Ca(OH)₂.",
                "points": 1
            }
        ],
        "quiz_questions": [
            {
                "id": 6401,
                "topic_id": 64,
                "question": "The Modern Periodic Table is arranged in increasing order of which atomic property?",
                "options_json": [
                    "Atomic Mass",
                    "Atomic Number",
                    "Valency",
                    "Number of Neutrons"
                ],
                "correct_answer": "Atomic Number",
                "explanation": "Henry Moseley established that properties of elements are periodic functions of their atomic numbers (number of protons Z), forming the foundation of the modern periodic table.",
                "points": 1
            },
            {
                "id": 6402,
                "topic_id": 64,
                "question": "Which of the following acids is naturally present in sour milk and yogurt (curd)?",
                "options_json": [
                    "Citric Acid",
                    "Acetic Acid",
                    "Lactic Acid",
                    "Oxalic Acid"
                ],
                "correct_answer": "Lactic Acid",
                "explanation": "Lactic acid (CH₃CH(OH)COOH) is produced in milk by lactic acid bacteria (Lactobacillus) during curdling.",
                "points": 1
            },
            {
                "id": 6403,
                "topic_id": 64,
                "question": "What color does blue litmus paper turn when dipped into an acidic solution?",
                "options_json": [
                    "Remains Blue",
                    "Turns Red",
                    "Turns Yellow",
                    "Turns Green"
                ],
                "correct_answer": "Turns Red",
                "explanation": "Acids turn blue litmus paper red, while bases turn red litmus paper blue.",
                "points": 1
            },
            {
                "id": 6404,
                "topic_id": 64,
                "question": "Which gas is primarily responsible for the greenhouse effect and ocean acidification?",
                "options_json": [
                    "Oxygen",
                    "Carbon Dioxide",
                    "Nitrogen",
                    "Argon"
                ],
                "correct_answer": "Carbon Dioxide",
                "explanation": "Carbon dioxide (CO₂) is the principal greenhouse gas emitted by fossil fuel combustion, trapping infrared radiation and dissolving in seawater to form carbonic acid.",
                "points": 1
            },
            {
                "id": 6405,
                "topic_id": 64,
                "question": "What is the chemical name of common table salt used in cooking?",
                "options_json": [
                    "Sodium Hydroxide",
                    "Sodium Chloride",
                    "Potassium Chloride",
                    "Sodium Sulfate"
                ],
                "correct_answer": "Sodium Chloride",
                "explanation": "Common table salt is Sodium Chloride (NaCl), formed by the neutralization reaction of hydrochloric acid (HCl) with sodium hydroxide (NaOH).",
                "points": 1
            },
            {
                "id": 6406,
                "topic_id": 64,
                "question": "Which metal remains liquid at normal room temperature (25°C)?",
                "options_json": [
                    "Gallium",
                    "Mercury",
                    "Bromine",
                    "Cesium"
                ],
                "correct_answer": "Mercury",
                "explanation": "Mercury (Hg, atomic number 80) is the only metallic element that is liquid at standard room temperature and pressure. (Bromine is a liquid non-metal).",
                "points": 1
            },
            {
                "id": 6407,
                "topic_id": 64,
                "question": "What is the main chemical compound that constitutes the scale or rust formed on iron?",
                "options_json": [
                    "Ferrous oxide (FeO)",
                    "Hydrated ferric oxide (Fe₂O₃·xH₂O)",
                    "Iron sulfide (FeS)",
                    "Iron carbonate (FeCO₃)"
                ],
                "correct_answer": "Hydrated ferric oxide (Fe₂O₃·xH₂O)",
                "explanation": "Rust is formed when iron reacts with oxygen in the presence of water, producing reddish-brown hydrated iron(III) oxide Fe₂O₃·xH₂O.",
                "points": 1
            },
            {
                "id": 6408,
                "topic_id": 64,
                "question": "Stainless steel is manufactured by alloying iron with carbon and which two key metals to resist corrosion?",
                "options_json": [
                    "Chromium and Nickel",
                    "Copper and Zinc",
                    "Tin and Lead",
                    "Manganese and Cobalt"
                ],
                "correct_answer": "Chromium and Nickel",
                "explanation": "Stainless steel contains iron with carbon, chromium (at least 10.5%), and nickel. Chromium forms a self-healing invisible chromium oxide passivation layer that blocks rust.",
                "points": 1
            },
            {
                "id": 6409,
                "topic_id": 64,
                "question": "Which of the following is a thermosetting plastic commonly used for electrical switches and handles?",
                "options_json": [
                    "Polythene",
                    "Bakelite",
                    "PVC",
                    "Nylon"
                ],
                "correct_answer": "Bakelite",
                "explanation": "Bakelite (phenol-formaldehyde resin) is a thermosetting plastic that does not soften upon heating once molded, possessing excellent non-conducting and heat-resistant properties.",
                "points": 1
            },
            {
                "id": 6410,
                "topic_id": 64,
                "question": "What is the pH of a completely neutral aqueous solution at 25°C?",
                "options_json": [
                    "0",
                    "7",
                    "14",
                    "1"
                ],
                "correct_answer": "7",
                "explanation": "At 25°C, pure water has [H⁺] = 10⁻⁷ M, resulting in pH = -log(10⁻⁷) = 7.",
                "points": 1
            },
            {
                "id": 6411,
                "topic_id": 64,
                "question": "Which noble gas is filled in electric incandescent bulbs and filament lamps to prevent tungsten oxidation?",
                "options_json": [
                    "Argon",
                    "Helium",
                    "Radon",
                    "Chlorine"
                ],
                "correct_answer": "Argon",
                "explanation": "Argon is an inert noble gas used with small amounts of nitrogen in incandescent bulbs to prevent evaporation and oxidation of the glowing tungsten filament.",
                "points": 1
            },
            {
                "id": 6412,
                "topic_id": 64,
                "question": "What is the isotope of hydrogen that contains one proton and one neutron in its nucleus?",
                "options_json": [
                    "Protium",
                    "Deuterium",
                    "Tritium",
                    "Hydronium"
                ],
                "correct_answer": "Deuterium",
                "explanation": "Deuterium (²H or D) is the heavy hydrogen isotope having 1 proton and 1 neutron (mass number 2). Its oxide (D₂O) is known as heavy water.",
                "points": 1
            },
            {
                "id": 6413,
                "topic_id": 64,
                "question": "Hardness in water caused by dissolved bicarbonates of calcium and magnesium is known as:",
                "options_json": [
                    "Temporary Hardness",
                    "Permanent Hardness",
                    "Alkaline Hardness",
                    "Radioactive Hardness"
                ],
                "correct_answer": "Temporary Hardness",
                "explanation": "Temporary hardness is caused by calcium and magnesium bicarbonates and can be removed simply by boiling. Permanent hardness is caused by chlorides and sulfates of calcium and magnesium.",
                "points": 1
            },
            {
                "id": 6414,
                "topic_id": 64,
                "question": "Which non-metal is an exceptional conductor of electricity due to free delocalized electrons between its carbon layers?",
                "options_json": [
                    "Diamond",
                    "Graphite",
                    "Fullerene",
                    "Sulfur"
                ],
                "correct_answer": "Graphite",
                "explanation": "In graphite, each carbon atom is bonded to three others in planar hexagonal sheets, leaving one free delocalized electron per carbon atom, which permits electrical conduction.",
                "points": 1
            },
            {
                "id": 6415,
                "topic_id": 64,
                "question": "The process of heating an ore strongly in the presence of excess air below its melting point is termed:",
                "options_json": [
                    "Calcination",
                    "Roasting",
                    "Smelting",
                    "Refining"
                ],
                "correct_answer": "Roasting",
                "explanation": "Roasting is heating sulfide ores in excess air to convert them into metal oxides and volatile sulfur dioxide. Calcination is heating in absence/limited air (used for carbonate ores).",
                "points": 1
            },
            {
                "id": 6416,
                "topic_id": 64,
                "question": "What chemical is widely used in commercial fire extinguishers to produce a foam of carbon dioxide gas?",
                "options_json": [
                    "Sodium Bicarbonate and Sulfuric Acid",
                    "Calcium Carbonate and Nitric Acid",
                    "Sodium Hydroxide and Hydrochloric Acid",
                    "Ammonium Nitrate and Water"
                ],
                "correct_answer": "Sodium Bicarbonate and Sulfuric Acid",
                "explanation": "In chemical soda-acid fire extinguishers, sodium bicarbonate solution reacts with sulfuric acid upon activation to liberate voluminous CO₂ gas that smothers fires.",
                "points": 1
            },
            {
                "id": 6417,
                "topic_id": 64,
                "question": "Which organic acid is found in ant stings and nettle hairs, causing sharp burning pain?",
                "options_json": [
                    "Methanoic Acid (Formic Acid)",
                    "Acetic Acid",
                    "Tartaric Acid",
                    "Benzoic Acid"
                ],
                "correct_answer": "Methanoic Acid (Formic Acid)",
                "explanation": "Ant bites inject methanoic acid (HCOOH, commonly known as formic acid from Latin 'formica' for ant), which can be neutralized with mild bases like baking soda.",
                "points": 1
            },
            {
                "id": 6418,
                "topic_id": 64,
                "question": "What is the commercial name of solid carbon dioxide (CO₂) that sublimates directly into gas at -78.5°C?",
                "options_json": [
                    "Dry Ice",
                    "Liquid Ice",
                    "Frost Ice",
                    "Soft Carbon"
                ],
                "correct_answer": "Dry Ice",
                "explanation": "Solid carbon dioxide is called 'Dry Ice' because it sublimates directly from solid to gas at atmospheric pressure without leaving any liquid residue.",
                "points": 1
            },
            {
                "id": 6419,
                "topic_id": 64,
                "question": "Which metal ore is the principal commercial source for the industrial extraction of Aluminium?",
                "options_json": [
                    "Haematite",
                    "Bauxite",
                    "Cinnabar",
                    "Galena"
                ],
                "correct_answer": "Bauxite",
                "explanation": "Bauxite (hydrated aluminium oxide, Al₂O₃·2H₂O) is the primary ore from which aluminium is extracted using the Bayer process and Hall-Héroult electrolytic cell.",
                "points": 1
            },
            {
                "id": 6420,
                "topic_id": 64,
                "question": "Solder, the alloy utilized by electricians to join electrical wiring components, is composed of:",
                "options_json": [
                    "Lead and Tin",
                    "Copper and Tin",
                    "Zinc and Nickel",
                    "Iron and Lead"
                ],
                "correct_answer": "Lead and Tin",
                "explanation": "Solder is an alloy of lead (approx 37%) and tin (approx 63%) having a notably low melting point (~183°C), enabling quick fusion without damaging delicate electronic circuits.",
                "points": 1
            }
        ]
    }
}
