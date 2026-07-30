#!/usr/bin/env python3
"""Grade 11, Days 121-130 -- extends Grade 11 from 120 to 130 days. Topics
chosen after dumping the existing Day 1-120 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap: motif and
recurring symbols, the ballad, the process essay, active versus passive
voice, the roman a clef, clickbait headlines, the personal narrative
speech, narrative distance and point of view, and the encomium; the
derivative as a limit, trees and spanning trees, Diophantine equations,
vector equations of lines in three dimensions, roots of unity, the
Poisson distribution, sinking funds, the handshake lemma, and the
central limit theorem; the cytoskeleton, endocrine disruptors,
polyploidy, the blood-brain barrier, hibernation and torpor, quorum
sensing, the diving reflex, RNA interference, and allelopathy; chelation
therapy, vulcanization, reverse osmosis, catalytic converters, adhesive
chemistry, enthalpy of solution, leather tanning, antacid effervescence,
and the chemistry of composting.

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided entirely.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E11 = 'https://tvolearn.com/pages/grade-11-english'
F11 = 'https://tvolearn.com/pages/grade-11-functions'
B11 = 'https://tvolearn.com/pages/grade-11-biology'
C11 = 'https://tvolearn.com/pages/grade-11-chemistry'
RE, RF, RB, RC = (
    'TVO Learn: Grade 11 English',
    'TVO Learn: Grade 11 Functions',
    'TVO Learn: Grade 11 Biology',
    'TVO Learn: Grade 11 Chemistry',
)


def E(t, s, q):
    return sub('English', t, s, RE, E11, q)


def F(t, s, q):
    return sub('Functions', t, s, RF, F11, q)


def B(t, s, q):
    return sub('Biology', t, s, RB, B11, q)


def C(t, s, q):
    return sub('Chemistry', t, s, RC, C11, q)


def _rebalance_answer_positions(days, seed=20260730):
    import random
    rng = random.Random(seed)
    quizzes = [sub_entry[5] for _, subs in days for sub_entry in subs]
    n = sum(len(q) for q in quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in quizzes:
        for i, (q, opts, ans) in enumerate(quiz):
            correct_text = opts[ans]
            wrong_texts = [o for j, o in enumerate(opts) if j != ans]
            rng.shuffle(wrong_texts)
            target = targets[idx]
            idx += 1
            new_opts = [None, None, None, None]
            new_opts[target] = correct_text
            wi = 0
            for slot in range(4):
                if new_opts[slot] is None:
                    new_opts[slot] = wrong_texts[wi]
                    wi += 1
            quiz[i] = (q, new_opts, target)
    return days


g11_121_130 = [
day(121, [
E('Reading: Analyzing Motif and Recurring Symbols in Fiction',
  'Grade 11 English strand: a motif is a recurring image, phrase, or idea that repeats throughout a text, reinforcing central themes and creating structural and thematic unity across a narrative.',
  [('What is a motif?', ['A recurring image, phrase, or idea repeated throughout a text', 'A single event that happens only once in a story', 'A type of punctuation mark', 'A formal citation style'], 0),
   ('What does a motif typically reinforce in a text?', ['Central themes and structural unity', 'Random unrelated details', 'Grammar rules only', 'The page numbering of a book'], 0),
   ('How does a motif differ from a one-time symbol?', ['A motif repeats across the text, while a single symbol may appear only once', 'A motif appears only in poetry, never in prose', 'A motif has no connection to meaning', 'A motif is always a literal object with no symbolic value'], 0),
   ('Which is an example of a motif in a novel?', ['Repeated references to birds or flight throughout the story', 'A single mention of rain in one chapter', 'The title page of the book', 'The page count of the novel'], 0),
   ('Why might a reader track a recurring motif while reading?', ['To notice how the pattern deepens or shifts the meaning of the text over time', 'Motifs have no effect on interpretation', 'To count how many words are in the chapter', 'To identify grammatical errors only'], 0)]),
F('Calculus Preview: An Introduction to the Derivative as a Limit',
  'Grade 11 Functions strand: the derivative of a function at a point is defined as the limit of the average rate of change as the interval shrinks toward zero, giving the instantaneous rate of change and the slope of the tangent line.',
  [('How is the derivative of a function at a point defined?', ['As the limit of the average rate of change as the interval shrinks toward zero', 'As the sum of all function values', 'As a fixed number unrelated to the function', 'As the total area under the curve'], 0),
   ('What does the derivative represent geometrically?', ['The slope of the tangent line at a point', 'The length of the curve', 'The area enclosed by the curve', 'The y-intercept of the function'], 0),
   ('What earlier concept is the formal definition of the derivative built upon?', ['The limit', 'Basic addition', 'The Pythagorean Theorem', 'Simple counting'], 0),
   ('What does the derivative measure at a specific point?', ['The instantaneous rate of change of the function', 'The average value of the function over its entire domain', 'The total distance travelled by a graph', 'The number of times a graph crosses the x-axis'], 0),
   ('Why is a function generally required to be continuous at a point before a derivative can exist there?', ['A break or jump at a point prevents a well-defined tangent line from being formed', 'Continuity has no relationship to derivatives at all', 'Discontinuous functions always have derivatives everywhere', 'Derivatives only exist for straight lines'], 0)]),
B('Biology: The Cytoskeleton — Structure and Cellular Movement',
  'Grade 11 Biology strand: the cytoskeleton is a dynamic network of protein filaments, including microtubules, microfilaments, and intermediate filaments, that maintains cell shape, enables intracellular transport, and drives cellular movement.',
  [('What is the cytoskeleton?', ['A dynamic network of protein filaments within a cell', 'A rigid outer shell surrounding the cell membrane', 'A type of carbohydrate stored in the nucleus', 'A structure found only in bacterial cells'], 0),
   ('Which of these is a component of the cytoskeleton?', ['Microtubules', 'Ribosomes', 'Mitochondria', 'The nucleolus'], 0),
   ('What role does the cytoskeleton play in cellular movement?', ['It provides the structural framework that enables movement such as muscle contraction and cell migration', 'It prevents all movement within or by the cell', 'It only functions in plant cells', 'It has no connection to movement of any kind'], 0),
   ('How does the cytoskeleton help maintain cell shape?', ['It forms an internal scaffold of filaments that supports the cell structure', 'It surrounds the cell in a hard mineral shell', 'It dissolves the cell membrane to allow flexibility', 'It has no role in shape at all'], 0),
   ('What is one function of microtubules within the cytoskeleton?', ['Guiding the separation of chromosomes during cell division', 'Producing energy through cellular respiration', 'Storing genetic information', 'Digesting waste products in the cell'], 0)]),
C('Chemistry: Chelation Therapy — Medical Applications of Coordination Chemistry',
  'Grade 11 Chemistry strand: chelation therapy uses chelating agents, molecules that bind tightly to metal ions through multiple coordinate covalent bonds, to remove toxic heavy metals such as lead or mercury from the body.',
  [('What is a chelating agent?', ['A molecule that binds tightly to metal ions through multiple coordinate bonds', 'A gas used only in refrigeration', 'An acid with no metal-binding ability', 'A type of radioactive isotope'], 0),
   ('What is the main purpose of chelation therapy?', ['Removing toxic heavy metals from the body', 'Adding more heavy metals to the bloodstream', 'Curing viral infections directly', 'Replacing red blood cells'], 0),
   ('Which of these might chelation therapy be used to treat?', ['Lead or mercury poisoning', 'A common cold', 'A broken bone', 'A sunburn'], 0),
   ('How does a chelating agent typically bind to a metal ion?', ['Through multiple coordinate covalent bonds, forming a ring-like structure', 'Through a single ionic bond only', 'Through no chemical bond at all', 'Through a covalent bond with another chelating agent only'], 0),
   ('Chelation therapy is a medical application of which broader area of chemistry?', ['Coordination chemistry', 'Organic polymer chemistry', 'Nuclear chemistry', 'Photochemistry'], 0)]),
]),
day(122, [
E('Poetry: The Ballad — Narrative Poetry and Oral Tradition',
  'Grade 11 English strand: a ballad is a narrative poem, often set to music, that tells a story through simple language, repetition, and a regular rhythm, rooted in an oral tradition of passing stories between generations.',
  [('What does a ballad primarily do?', ['Tells a story through verse, often set to music', 'Presents a list of unrelated facts', 'Avoids any use of rhythm or repetition', 'Functions only as a formal legal document'], 0),
   ('What tradition is the ballad form rooted in?', ['Oral storytelling passed between generations', 'Modern digital publishing only', 'Formal academic essay writing', 'Legal contract writing'], 0),
   ('Which literary technique is commonly used in ballads to aid memorization and musicality?', ['Repetition and regular rhythm', 'Complete absence of rhyme or rhythm', 'Only footnotes and citations', 'Random line lengths with no pattern'], 0),
   ('What kind of language does a ballad typically use?', ['Simple, direct language accessible to a wide audience', 'Highly technical, scientific vocabulary only', 'Language understood only by scholars', 'No language at all, only music'], 0),
   ('Why might a ballad be considered a bridge between poetry and music?', ['Ballads were traditionally sung and passed down orally before being written', 'Ballads have no connection to music whatsoever', 'Music was invented after the ballad form disappeared', 'Ballads are always performed silently with no sound'], 0)]),
F('Discrete Math: Trees and Spanning Trees in Graph Theory',
  'Grade 11 Functions strand: a tree is a connected graph with no cycles, and a spanning tree of a graph is a subgraph that connects all vertices using the minimum number of edges, with important applications in network design.',
  [('What defines a tree in graph theory?', ['A connected graph with no cycles', 'A graph with every vertex connected to every other vertex', 'A graph containing only isolated vertices with no edges', 'A graph that must contain at least one cycle'], 0),
   ('What is a spanning tree of a graph?', ['A subgraph that connects all vertices using the minimum number of edges and no cycles', 'A graph with no vertices at all', 'A tree that only includes half of the vertices', 'A cycle that visits every edge exactly once'], 0),
   ('How many edges does a spanning tree with n vertices contain?', ['n minus 1', 'n plus 1', 'Exactly n squared', 'Exactly 2n'], 0),
   ('Where might spanning trees be applied in real-world problems?', ['Designing efficient networks, such as minimizing cable length in a network', 'Measuring the temperature of a room', 'Calculating the area of a circle', 'Determining the colour of a traffic light'], 0),
   ('Why can a tree with n vertices never contain a cycle?', ['Adding an edge that would create a cycle would mean the graph is no longer a tree by definition', 'Trees always contain at least one cycle by definition', 'Cycles have no relationship to the structure of a tree', 'Trees require exactly two cycles per vertex'], 0)]),
B('Biology: Endocrine Disruptors and Hormonal Health',
  'Grade 11 Biology strand: endocrine disruptors are chemical compounds that interfere with the normal function of the hormonal system by mimicking, blocking, or altering natural hormone signalling, with potential effects on growth, reproduction, and development.',
  [('What is an endocrine disruptor?', ['A chemical compound that interferes with normal hormone signalling', 'A hormone naturally produced by the pancreas', 'A type of vitamin required for healthy bones', 'A protein that has no interaction with the endocrine system'], 0),
   ('How might an endocrine disruptor affect the body?', ['By mimicking, blocking, or altering natural hormone signals', 'By replacing all cells in the body instantly', 'By having no measurable biological effect', 'By permanently increasing bone density only'], 0),
   ('Which body system do endocrine disruptors primarily target?', ['The hormonal (endocrine) system', 'The skeletal system only', 'The digestive system exclusively', 'The integumentary system only'], 0),
   ('What kinds of biological processes might be affected by exposure to endocrine disruptors?', ['Growth, reproduction, and development', 'Only eye colour', 'Only hair texture', 'Only the sense of taste'], 0),
   ('Why are scientists concerned about environmental sources of endocrine disruptors?', ['Because they may accumulate in the environment and affect wildlife and human hormonal health over time', 'Endocrine disruptors have no environmental sources at all', 'They only exist in a laboratory setting with no real-world presence', 'They immediately and completely dissolve with no lasting effect'], 0)]),
C('Chemistry: Vulcanization — Cross-Linking in Rubber Polymers',
  'Grade 11 Chemistry strand: vulcanization is a chemical process in which sulfur atoms form cross-links between polymer chains in rubber, converting a soft, sticky material into a stronger, more elastic, and heat-resistant product.',
  [('What is vulcanization?', ['A chemical process that forms cross-links between polymer chains in rubber using sulfur', 'A process that removes all polymer chains from rubber', 'A physical process with no chemical reaction involved', 'A method of melting rubber into a liquid permanently'], 0),
   ('What element is commonly used to cross-link rubber polymer chains during vulcanization?', ['Sulfur', 'Oxygen', 'Helium', 'Chlorine'], 0),
   ('How does vulcanized rubber differ from untreated natural rubber?', ['It is stronger, more elastic, and more heat-resistant', 'It is softer and much stickier than untreated rubber', 'It loses all elasticity and becomes brittle', 'It becomes a liquid at room temperature'], 0),
   ('What structural change occurs to the polymer chains during vulcanization?', ['Cross-links form between separate polymer chains', 'All polymer chains are broken into individual monomers', 'The polymer chains disappear entirely', 'The chains rearrange into a crystal lattice with no bonds'], 0),
   ('Why is vulcanized rubber used in products like tires?', ['Its added strength and heat resistance make it more durable under stress', 'It is far more fragile than untreated rubber', 'It cannot withstand any temperature change', 'It has no practical advantage over untreated rubber'], 0)]),
]),
day(123, [
E('Writing: The Process Essay — Explaining How Something Works',
  'Grade 11 English strand: a process essay explains how to complete a task or how something works through a clear sequence of steps, relying on precise chronological order and transitional language to guide the reader.',
  [('What is the main purpose of a process essay?', ['To explain how to complete a task or how something works', 'To argue a single controversial opinion', 'To describe a personal memory with no instructional purpose', 'To summarize a work of fiction'], 0),
   ('What structural feature is essential to a process essay?', ['A clear, chronological sequence of steps', 'A completely random order of ideas', 'No structure of any kind', 'A rhyme scheme'], 0),
   ('What kind of language helps guide a reader through a process essay?', ['Transitional language, such as first, next, and finally', 'Language with no connection between steps', 'Only technical jargon with no explanation', 'Poetic imagery with no clear steps'], 0),
   ('Which of these topics would suit a process essay?', ['How to brew a cup of tea', 'A personal reflection on a childhood memory', 'An argument about a political issue', 'A comparison of two novels'], 0),
   ('Why is precision important in a process essay?', ['Missing or unclear steps can prevent the reader from successfully completing the task', 'Precision has no importance in this type of writing', 'Vague instructions are always more effective', 'Process essays do not require any specific details'], 0)]),
F('Number Theory: An Introduction to Diophantine Equations',
  'Grade 11 Functions strand: a Diophantine equation is a polynomial equation for which only integer solutions are sought, building on earlier work with modular arithmetic and the Euclidean algorithm to determine whether integer solutions exist.',
  [('What is a Diophantine equation?', ['A polynomial equation for which only integer solutions are sought', 'An equation with no solutions of any kind', 'An equation that only allows decimal solutions', 'A geometric formula for area'], 0),
   ('Which earlier concept helps determine whether a linear Diophantine equation has integer solutions?', ['The greatest common divisor, found using the Euclidean algorithm', 'The Pythagorean Theorem', 'Basic multiplication tables', 'Trigonometric ratios'], 0),
   ('For the linear equation ax + by = c to have integer solutions, what must be true?', ['The greatest common divisor of a and b must divide c', 'The values a and b must both equal zero', 'c must always be a negative number', 'The equation must contain no variables'], 0),
   ('Diophantine equations are named after which historical figure?', ['Diophantus, an ancient Greek mathematician', 'Isaac Newton', 'Pythagoras', 'Leonhard Euler'], 0),
   ('Why might a Diophantine equation have no solution even though the corresponding real-number equation does?', ['Restricting solutions to integers can eliminate valid real-number answers', 'Diophantine equations always have identical solutions to real-number equations', 'Integer solutions are always easier to find than real-number ones', 'Diophantine equations never involve integers'], 0)]),
B('Biology: Polyploidy and Chromosome Number Variation in Plants',
  'Grade 11 Biology strand: polyploidy is a condition in which an organism has more than two complete sets of chromosomes, a common phenomenon in plants that can lead to increased size, hybrid vigour, and the formation of new species.',
  [('What is polyploidy?', ['A condition in which an organism has more than two complete sets of chromosomes', 'A condition where an organism has no chromosomes at all', 'A type of asexual reproduction with no genetic change', 'A disease affecting only animal cells'], 0),
   ('In which group of organisms is polyploidy especially common?', ['Plants', 'Mammals exclusively', 'Insects exclusively', 'Bacteria exclusively'], 0),
   ('What effect can polyploidy have on a plant?', ['It can increase size and lead to greater hybrid vigour', 'It always causes immediate death of the plant', 'It has no measurable effect on the organism at all', 'It permanently removes all genetic material'], 0),
   ('How can polyploidy contribute to the formation of new plant species?', ['Changes in chromosome number can create reproductive barriers with the original species', 'Polyploidy always produces offspring identical to a single parent species', 'Polyploidy prevents any reproduction from occurring', 'It has no role in speciation whatsoever'], 0),
   ('Which of these is an example of a polyploid crop plant?', ['Bread wheat', 'A haploid bacterial cell', 'A single-celled amoeba', 'A virus'], 0)]),
C('Chemistry: Reverse Osmosis and Water Purification',
  'Grade 11 Chemistry strand: reverse osmosis is a water purification process that applies external pressure to force water molecules through a semi-permeable membrane, leaving dissolved salts and other impurities behind.',
  [('What does reverse osmosis use to purify water?', ['External pressure forcing water through a semi-permeable membrane', 'Boiling the water at extremely high temperatures', 'Freezing the water into solid ice', 'Adding large amounts of salt to the water'], 0),
   ('What is left behind by the semi-permeable membrane during reverse osmosis?', ['Dissolved salts and other impurities', 'Pure water molecules only', 'Oxygen gas exclusively', 'Nothing is left behind at all'], 0),
   ('Why is the process called reverse osmosis?', ['Pressure forces water against its natural direction of osmotic flow, from a more concentrated to a less concentrated solution', 'Water naturally flows this way with no pressure required', 'It refers to boiling rather than filtering water', 'It describes water freezing into a solid'], 0),
   ('What is a common application of reverse osmosis technology?', ['Desalinating seawater to produce fresh drinking water', 'Producing table salt from freshwater', 'Cooling industrial machinery only', 'Generating electricity directly'], 0),
   ('What property of a semi-permeable membrane makes reverse osmosis possible?', ['It allows small water molecules to pass through while blocking larger dissolved particles', 'It blocks all molecules, including water, completely', 'It allows all substances to pass through equally', 'It dissolves completely when exposed to water'], 0)]),
]),
day(124, [
E('Grammar: Active versus Passive Voice for Rhetorical Effect',
  'Grade 11 English strand: in active voice the subject performs the action, while in passive voice the subject receives the action, and skilled writers choose deliberately between the two to control emphasis, clarity, and tone.',
  [('In active voice, what does the subject of a sentence do?', ['Performs the action of the verb', 'Always receives the action', 'Is never mentioned in the sentence', 'Only appears in questions'], 0),
   ('In passive voice, what happens to the subject of a sentence?', ['The subject receives the action rather than performing it', 'The subject always performs the action', 'The subject disappears completely from the sentence', 'The subject becomes a verb'], 0),
   ('Which sentence is written in passive voice?', ['The report was written by the committee.', 'The committee wrote the report.', 'The committee is writing the report.', 'The committee will write the report.'], 0),
   ('Why might a writer deliberately choose passive voice?', ['To emphasize the action or result rather than who performed it', 'Passive voice is always a grammatical error to avoid completely', 'Passive voice removes all meaning from a sentence', 'Passive voice is required in every sentence of formal writing'], 0),
   ('Why is active voice often preferred in clear, direct writing?', ['It tends to be more concise and identifies who is performing the action', 'Active voice always obscures the subject of a sentence', 'Active voice is grammatically incorrect in formal writing', 'Active voice removes the need for a verb'], 0)]),
F('Geometry: Vector Equations of Lines in Three Dimensions',
  'Grade 11 Functions strand: a line in three-dimensional space can be described using a vector equation involving a point on the line and a single direction vector, extending the two-dimensional case to model motion and geometry in 3D.',
  [('What is needed to write the vector equation of a line in three dimensions?', ['A point on the line and a direction vector', 'Two direction vectors with no point', 'Only the origin, with nothing else needed', 'A single number with no vectors at all'], 0),
   ('How does a vector equation of a line in three dimensions extend the two-dimensional case?', ['It uses a third coordinate component, typically z, in addition to x and y', 'It removes the need for a direction vector entirely', 'It only applies to curves, never straight lines', 'It has no connection to the two-dimensional case'], 0),
   ('What geometric object does the vector equation of a line describe?', ['A straight, one-dimensional path extending infinitely in both directions', 'A flat, two-dimensional surface', 'A three-dimensional solid shape', 'A single fixed point only'], 0),
   ('Why is only one direction vector needed to define a line, while two are needed to define a plane?', ['A line requires only a single direction to extend along, while a plane requires two independent directions to form a flat surface', 'Lines and planes both always require exactly the same number of direction vectors', 'A line requires infinitely many direction vectors to be defined', 'Direction vectors are never used to describe lines'], 0),
   ('Vector equations of lines in three dimensions are useful for modelling ___.', ['The path of an object moving through space, such as in physics or engineering', 'Only two-dimensional drawings', 'Only counting problems with no geometry', 'Only measuring temperature'], 0)]),
B('Biology: The Blood-Brain Barrier — Structure and Function',
  'Grade 11 Biology strand: the blood-brain barrier is a selectively permeable layer of tightly joined cells lining the brain capillaries, protecting neural tissue by restricting the passage of pathogens, toxins, and many large molecules from the bloodstream.',
  [('What is the blood-brain barrier?', ['A selectively permeable layer of tightly joined cells lining the brain capillaries', 'A bone structure that surrounds the entire brain', 'A type of muscle found only in the heart', 'A layer of skin on the outside of the skull'], 0),
   ('What is the main function of the blood-brain barrier?', ['Protecting neural tissue by restricting harmful substances from entering the brain', 'Allowing all substances in the blood to enter the brain freely', 'Producing new neurons continuously', 'Pumping blood throughout the entire body'], 0),
   ('Which of these might the blood-brain barrier typically block from entering brain tissue?', ['Many pathogens and toxins circulating in the blood', 'Oxygen needed for cellular respiration', 'Glucose needed for energy', 'Water molecules entirely'], 0),
   ('Why can the blood-brain barrier make treating certain brain diseases with medication difficult?', ['It can prevent many drugs from reaching brain tissue effectively', 'It always allows every drug to pass through with no resistance', 'It has no effect on medication delivery at all', 'It only exists in animals, never in humans'], 0),
   ('What structural feature of the cells lining brain capillaries helps form the blood-brain barrier?', ['Tight junctions between adjacent cells that limit what can pass between them', 'Large gaps between cells that allow anything to pass freely', 'A complete absence of any cell membrane', 'Cells that constantly divide and never connect to each other'], 0)]),
C('Chemistry: Catalytic Converters and Automotive Emission Control',
  'Grade 11 Chemistry strand: a catalytic converter uses metal catalysts such as platinum, palladium, and rhodium to speed up reactions that convert harmful engine exhaust gases, including carbon monoxide and nitrogen oxides, into less harmful substances.',
  [('What is the main purpose of a catalytic converter?', ['Converting harmful exhaust gases into less harmful substances', 'Increasing the amount of pollution released by a vehicle', 'Storing fuel before it reaches the engine', 'Cooling the engine during operation'], 0),
   ('Which metals are commonly used as catalysts in a catalytic converter?', ['Platinum, palladium, and rhodium', 'Only pure carbon', 'Only sodium and potassium', 'Only iron and copper'], 0),
   ('Which harmful gas is commonly converted by a catalytic converter?', ['Carbon monoxide', 'Pure oxygen', 'Water vapour only', 'Argon gas'], 0),
   ('What role does a catalyst play in the reactions occurring in a catalytic converter?', ['It speeds up the reaction without being consumed in the process', 'It slows down the reaction significantly', 'It is fully consumed and destroyed by the reaction', 'It has no effect on the rate of the reaction'], 0),
   ('Why are catalytic converters considered important for environmental protection?', ['They reduce the release of harmful pollutants from vehicle exhaust into the atmosphere', 'They increase the release of pollutants into the atmosphere', 'They have no measurable effect on air quality', 'They only function underwater'], 0)]),
]),
day(125, [
E('Literature: The Roman a Clef — Fiction Rooted in Reality',
  'Grade 11 English strand: a roman a clef is a novel in which real people or events are thinly disguised as fictional characters and situations, inviting readers familiar with the source material to recognize the hidden real-world references.',
  [('What is a roman a clef?', ['A novel in which real people or events are thinly disguised as fiction', 'A novel with no connection to reality whatsoever', 'A type of formal legal document', 'A poem written entirely in French'], 0),
   ('What might a reader familiar with the real events behind a roman a clef recognize?', ['Hidden references to real people or situations disguised as fiction', 'Nothing, since the novel bears no resemblance to reality', 'Only grammatical errors in the text', 'A complete absence of characters'], 0),
   ('Why might an author choose to write a roman a clef rather than a straightforward memoir?', ['Fiction can offer legal protection and creative freedom while still commenting on real events', 'Fiction always removes the connection to any real events', 'A roman a clef must always be entirely factual with no invention', 'Authors are legally required to disguise every memoir as fiction'], 0),
   ('Which of these best describes the relationship between a roman a clef and real life?', ['Real people and events form the basis for fictionalized characters and plot', 'The novel is entirely unrelated to any real person or event', 'The novel is a word-for-word transcript of true events', 'The novel exists only as an oral tradition with no written text'], 0),
   ('The term roman a clef comes from a phrase meaning ___.', ['Novel with a key, since knowledge of real events unlocks its meaning', 'A novel written entirely in verse', 'A story with no characters at all', 'A play performed only once'], 0)]),
F('Complex Numbers: Roots of Unity and nth Roots',
  'Grade 11 Functions strand: the nth roots of a complex number can be found using an extension of De Moivres Theorem, revealing that a nonzero complex number has exactly n distinct nth roots evenly spaced around a circle in the complex plane.',
  [('How many distinct nth roots does a nonzero complex number have?', ['Exactly n', 'Exactly 1', 'Exactly 2, regardless of n', 'Infinitely many'], 0),
   ('What theorem is extended to find the nth roots of a complex number?', ['De Moivres Theorem', 'The Pythagorean Theorem', 'The Fundamental Theorem of Arithmetic', 'The Binomial Theorem'], 0),
   ('How are the nth roots of a complex number arranged in the complex plane?', ['Evenly spaced around a circle', 'Arranged along a single straight line only', 'Clustered at a single point', 'Scattered with no pattern at all'], 0),
   ('What are the nth roots of unity?', ['The n distinct solutions to the equation z^n = 1', 'Only the number 1 itself', 'Numbers that have no solutions at all', 'Only negative real numbers'], 0),
   ('Why is polar form especially useful for finding roots of complex numbers?', ['It expresses the angle and magnitude needed to evenly divide the roots around a circle', 'Polar form cannot be used for this purpose at all', 'Polar form only applies to real numbers, not complex ones', 'Polar form eliminates the need for any angle measurement'], 0)]),
B('Biology: Hibernation and Torpor — Physiological Adaptations',
  'Grade 11 Biology strand: hibernation and torpor are physiological states in which an animal dramatically lowers its metabolic rate, heart rate, and body temperature to conserve energy during periods of cold or food scarcity.',
  [('What happens to an animals metabolic rate during hibernation?', ['It drops dramatically to conserve energy', 'It increases significantly above normal levels', 'It remains completely unchanged', 'It stops entirely with no biological activity'], 0),
   ('What is torpor?', ['A short-term state of reduced metabolic activity, often lasting hours to a day', 'A permanent state that never ends once it begins', 'A behaviour found only in plants', 'A type of active hunting strategy'], 0),
   ('Why might an animal enter hibernation or torpor?', ['To conserve energy during periods of cold temperatures or food scarcity', 'To increase its body temperature to dangerous levels', 'To attract more predators to its location', 'To grow significantly larger in a short period of time'], 0),
   ('How does an animals heart rate typically change during hibernation?', ['It slows down significantly compared to its normal active rate', 'It speeds up far beyond its normal active rate', 'It stays exactly the same as when the animal is active', 'It stops permanently and never restarts'], 0),
   ('Which of these animals is well known for entering true hibernation?', ['The ground squirrel', 'A shark', 'An eagle', 'A dolphin'], 0)]),
C('Chemistry: The Chemistry of Adhesives and Molecular Bonding',
  'Grade 11 Chemistry strand: adhesives bond materials together through a combination of mechanical interlocking and chemical forces, such as covalent bonding, hydrogen bonding, and van der Waals forces, between the adhesive and the surfaces it joins.',
  [('How do adhesives generally bond materials together?', ['Through a combination of mechanical interlocking and chemical forces', 'Through the complete melting of both surfaces into one', 'Through a process that removes all molecules from the surfaces', 'Through gravity alone with no chemical interaction'], 0),
   ('Which type of intermolecular force can contribute to how an adhesive sticks to a surface?', ['Van der Waals forces', 'Nuclear forces between atomic nuclei', 'Only gravitational force', 'Only magnetic force'], 0),
   ('What does it mean for an adhesive to cure?', ['The adhesive undergoes a chemical or physical change that hardens and strengthens the bond', 'The adhesive instantly evaporates and disappears', 'The adhesive becomes a gas with no bonding ability', 'The adhesive loses all of its bonding strength permanently'], 0),
   ('Why might hydrogen bonding contribute to adhesive strength between certain materials?', ['It forms attractive forces between molecules containing hydrogen bonded to electronegative atoms like oxygen or nitrogen', 'Hydrogen bonding never occurs in adhesive materials', 'Hydrogen bonding only affects the colour of an adhesive', 'Hydrogen bonding is exclusive to metallic bonding'], 0),
   ('What is mechanical interlocking in the context of adhesives?', ['The adhesive flowing into microscopic surface irregularities and hardening in place', 'A process where two surfaces are welded together using heat only', 'A chemical reaction that dissolves both bonded surfaces', 'A magnetic attraction between the two surfaces'], 0)]),
]),
day(126, [
E('Media Literacy: Clickbait Headlines and Digital Virality',
  'Grade 11 English strand: clickbait headlines use sensational language, curiosity gaps, and emotional triggers to maximize clicks and shares, often prioritizing virality over accuracy, requiring readers to critically evaluate a headline before trusting its content.',
  [('What is the primary goal of a clickbait headline?', ['Maximizing clicks and shares, often through sensational language', 'Providing a fully accurate summary of the article', 'Avoiding any emotional language whatsoever', 'Following strict academic citation standards'], 0),
   ('What is a curiosity gap in a clickbait headline?', ['A withheld piece of information designed to make readers want to click to find out more', 'A headline that fully explains the entire story upfront', 'A grammatical error found in a headline', 'A citation missing from the end of an article'], 0),
   ('Why should readers be cautious about trusting clickbait headlines?', ['The headline may prioritize sensationalism over the accuracy of the actual content', 'Clickbait headlines are always completely accurate', 'Clickbait headlines never appear on social media platforms', 'Clickbait headlines are required by law to be truthful'], 0),
   ('What kind of language do clickbait headlines commonly use to trigger a reaction?', ['Emotionally charged or sensational language', 'Only neutral, purely factual language with no emotional appeal', 'Only technical, scientific terminology', 'Language with no connection to the article content at all'], 0),
   ('What skill helps readers resist being misled by clickbait headlines?', ['Media literacy and critical evaluation before clicking or sharing', 'Ignoring every headline on the internet completely', 'Sharing every headline immediately without reading it', 'Trusting all headlines equally with no evaluation'], 0)]),
F('Statistics: An Introduction to the Poisson Distribution',
  'Grade 11 Functions strand: the Poisson distribution models the probability of a given number of independent events occurring within a fixed interval of time or space, when those events happen at a known constant average rate.',
  [('What does the Poisson distribution model?', ['The probability of a given number of independent events occurring in a fixed interval', 'The exact outcome of a single guaranteed event', 'The average height of a population', 'The area under a triangle'], 0),
   ('What must be known about the events being modelled by a Poisson distribution?', ['Their known constant average rate of occurrence over the interval', 'Their exact colour and shape', 'Their location on a coordinate plane', 'Their relationship to a persons age'], 0),
   ('Which of these situations could be modelled using a Poisson distribution?', ['The number of emails received in an hour', 'The exact height of a single building', 'The colour of a single card drawn from a deck', 'The temperature on a given day'], 0),
   ('How does the Poisson distribution differ from the binomial distribution in typical use?', ['The Poisson distribution models counts of events over a continuous interval rather than a fixed number of discrete trials', 'The two distributions are always mathematically identical with no differences', 'The Poisson distribution can never be used to model real events', 'The binomial distribution only applies to continuous intervals'], 0),
   ('The Poisson distribution assumes that events occur ___.', ['Independently of one another at a constant average rate', 'Only in pairs, never individually', 'At a rate that constantly doubles every second', 'Only during a single fixed moment in time'], 0)]),
B('Biology: Quorum Sensing — Bacterial Cell-to-Cell Communication',
  'Grade 11 Biology strand: quorum sensing is a form of cell-to-cell communication in which bacteria release and detect signalling molecules to coordinate group behaviours, such as biofilm formation, once the bacterial population reaches a critical density.',
  [('What is quorum sensing?', ['A form of cell-to-cell communication that lets bacteria coordinate group behaviours', 'A process where bacteria are permanently destroyed', 'A type of photosynthesis found only in plants', 'A structure used exclusively for bacterial movement'], 0),
   ('What triggers bacteria to begin coordinated group behaviours through quorum sensing?', ['Reaching a critical population density that raises signalling molecule concentration', 'A sudden and complete absence of any bacteria', 'Exposure to bright sunlight alone', 'A drop in signalling molecule concentration to zero'], 0),
   ('Which of these bacterial behaviours can be coordinated through quorum sensing?', ['Biofilm formation', 'Random, uncoordinated individual movement only', 'The complete cessation of all bacterial activity', 'Photosynthesis using chlorophyll'], 0),
   ('What do bacteria release and detect during quorum sensing?', ['Signalling molecules', 'Only pure water', 'Solid mineral particles', 'Radioactive isotopes'], 0),
   ('Why is quorum sensing of interest to researchers studying antibiotic resistance?', ['Disrupting quorum sensing signals could potentially prevent harmful coordinated bacterial behaviours like biofilm formation', 'Quorum sensing has no connection to bacterial behaviour or resistance', 'Antibiotic resistance always eliminates the need for any communication between bacteria', 'Quorum sensing is a phenomenon found only in animal cells'], 0)]),
C('Chemistry: Enthalpy of Solution and Hydration Energy',
  'Grade 11 Chemistry strand: the enthalpy of solution describes the net energy change when an ionic compound dissolves in water, resulting from the balance between the energy required to break the crystal lattice and the energy released as ions become hydrated.',
  [('What does the enthalpy of solution describe?', ['The net energy change when a compound dissolves in a solvent', 'The temperature at which a compound melts', 'The total mass of a dissolved compound', 'The colour change of a solution'], 0),
   ('What two energy processes are balanced when calculating enthalpy of solution for an ionic compound?', ['Breaking the crystal lattice and hydrating the released ions', 'Only the boiling of the solvent', 'Only the freezing of the solvent', 'The combustion of the solvent'], 0),
   ('What is hydration energy?', ['The energy released when ions become surrounded by water molecules', 'The energy required to boil a liquid completely', 'The energy needed to freeze a solution', 'The energy absorbed during a nuclear reaction'], 0),
   ('If the energy released during hydration is greater than the energy required to break the lattice, what type of process results?', ['An exothermic dissolving process', 'An endothermic dissolving process with no energy release at all', 'A process where no dissolving occurs', 'A purely physical change with no energy involved'], 0),
   ('Why might dissolving certain salts in water cause the surrounding water to feel colder?', ['The dissolving process is endothermic, absorbing more energy than it releases', 'The dissolving process always releases a large amount of heat', 'Dissolving a salt never involves any energy change', 'Cold temperatures prevent any salt from dissolving'], 0)]),
]),
day(127, [
E('Oral Communication: The Personal Narrative Speech',
  'Grade 11 English strand: a personal narrative speech recounts a meaningful experience from the speakers own life, using vivid detail, reflection, and a clear structure to connect the specific story to a broader, relatable insight.',
  [('What does a personal narrative speech typically recount?', ['A meaningful experience from the speakers own life', 'A completely fictional story with no connection to the speaker', 'A list of unrelated statistics', 'A formal legal argument'], 0),
   ('Why is vivid detail important in a personal narrative speech?', ['It helps the audience visualize and connect emotionally with the experience being described', 'Detail has no effect on how an audience receives a speech', 'Vivid detail always distracts from the main point', 'Personal narratives should avoid any specific description'], 0),
   ('What broader goal does a personal narrative speech typically aim to achieve beyond simply telling a story?', ['Connecting the specific experience to a broader, relatable insight or lesson', 'Providing only a chronological list of events with no reflection', 'Avoiding any connection to the audience', 'Presenting a purely statistical report'], 0),
   ('What structural element helps organize a personal narrative speech?', ['A clear sequence that builds toward a meaningful reflection or insight', 'A completely random order with no organization', 'Only a list of dates with no narrative content', 'A structure that ignores the audience entirely'], 0),
   ('A personal narrative speech is different from a purely informative speech because it ___.', ['Centers on a specific personal experience and its meaning', 'Never includes the speakers own perspective', 'Only presents statistics with no story', 'Avoids any structure or organization'], 0)]),
F('Financial Mathematics: Sinking Funds and Systematic Saving',
  'Grade 11 Functions strand: a sinking fund is a savings plan in which equal periodic deposits earn compound interest over time to accumulate a specific target amount, commonly used to plan for a future large expense or debt repayment.',
  [('What is a sinking fund?', ['A savings plan of equal periodic deposits that grow with compound interest toward a target amount', 'A one-time payment with no future growth', 'A type of loan that must be repaid immediately', 'An investment that guarantees a loss of value over time'], 0),
   ('What role does compound interest play in a sinking fund?', ['It allows the periodic deposits to grow over time toward the target amount', 'It has no effect on the growth of the fund', 'It is always fixed and never accumulates', 'It reduces the total value of each deposit'], 0),
   ('Why might an organization set up a sinking fund?', ['To systematically save for a known future expense or debt repayment', 'To immediately spend all available funds with no plan', 'To avoid saving any money at all', 'To guarantee an instant financial loss'], 0),
   ('How do the periodic deposits in a typical sinking fund compare to each other?', ['They are generally equal in amount and made at regular intervals', 'They are always random and unpredictable in size', 'They only occur a single time with no repetition', 'They decrease to zero after the first deposit'], 0),
   ('A sinking fund is most similar to which other financial concept covered earlier?', ['An annuity, since both involve regular deposits or payments over time', 'A single lump-sum payment with no future value', 'A perpetuity that never has a target amount', 'A simple, one-time discount on a purchase'], 0)]),
B('Biology: The Diving Reflex in Marine Mammals',
  'Grade 11 Biology strand: the mammalian diving reflex is a set of physiological responses triggered by submersion in cold water, including a slowed heart rate and redirected blood flow, that allow marine mammals to conserve oxygen during deep, prolonged dives.',
  [('What triggers the mammalian diving reflex?', ['Submersion in water, especially cold water', 'Exposure to bright sunlight', 'An increase in body temperature', 'A sudden loud noise'], 0),
   ('What happens to heart rate during the diving reflex?', ['It slows down significantly', 'It increases dramatically', 'It remains completely unchanged', 'It stops permanently'], 0),
   ('How does the diving reflex help conserve oxygen during a dive?', ['By redirecting blood flow toward essential organs like the heart and brain', 'By stopping all blood flow throughout the entire body', 'By increasing oxygen consumption in the limbs', 'By causing the animal to immediately surface'], 0),
   ('Which of these animals shows a particularly strong diving reflex adapted for deep, prolonged dives?', ['The seal', 'A songbird', 'A desert lizard', 'A garden snail'], 0),
   ('Why is the diving reflex considered an important physiological adaptation for marine mammals?', ['It allows them to spend extended periods underwater while conserving limited oxygen supplies', 'It allows them to breathe underwater without ever surfacing', 'It has no connection to survival underwater', 'It prevents the animal from ever diving below the surface'], 0)]),
C('Chemistry: The Chemistry of Tanning — Preserving Leather',
  'Grade 11 Chemistry strand: tanning is a chemical process that converts raw animal hide into stable, durable leather by using agents such as chromium salts or plant-derived tannins to cross-link collagen fibres and prevent decomposition.',
  [('What does the tanning process convert raw animal hide into?', ['Stable, durable leather', 'A liquid solution with no remaining fibres', 'A type of synthetic plastic', 'A form of pure protein powder'], 0),
   ('Which of these is a traditional plant-derived tanning agent?', ['Tannins', 'Table salt', 'Liquid nitrogen', 'Pure oxygen gas'], 0),
   ('What structural change do tanning agents cause within the hide?', ['They cross-link collagen fibres, stabilizing the structure', 'They completely dissolve all collagen fibres', 'They remove all protein from the hide entirely', 'They convert the hide into a gas'], 0),
   ('Why is tanning necessary to preserve animal hide as leather?', ['Untreated hide would otherwise decompose due to microbial and enzymatic breakdown', 'Untreated hide never decomposes under any conditions', 'Tanning has no effect on the durability of the hide', 'Raw hide is already fully stable without any treatment'], 0),
   ('Which metal is commonly used in modern chromium tanning processes?', ['Chromium', 'Gold', 'Mercury', 'Lead'], 0)]),
]),
day(128, [
E('Reading: Narrative Distance and Point of View',
  'Grade 11 English strand: narrative distance describes how close or removed a narrator seems from the thoughts, feelings, and events of a story, shaped by choices in point of view that influence how much intimacy or objectivity a reader experiences.',
  [('What does narrative distance describe?', ['How close or removed a narrator seems from the events and characters of a story', 'The physical length of a novel measured in pages', 'The number of characters in a story', 'The setting in which a story takes place'], 0),
   ('Which point of view often creates a close narrative distance, immersing the reader in a characters thoughts?', ['First-person point of view', 'An entirely absent narrator with no perspective', 'A narrator who only lists historical dates', 'A narrator with no access to any character'], 0),
   ('How might a distant, objective narrator affect a reader experience of a story?', ['It can create a sense of detachment or objectivity toward the events described', 'It always makes the reader feel emotionally closer to every character', 'It removes the possibility of the reader understanding the plot', 'It eliminates the need for any point of view at all'], 0),
   ('Why might an author vary narrative distance within a single text?', ['To control how intimately or objectively the reader experiences particular scenes or characters', 'Varying narrative distance is always a grammatical mistake', 'Narrative distance never changes within a single text', 'To remove all meaning from the narrative'], 0),
   ('Which point of view typically creates the greatest narrative distance from a single characters inner thoughts?', ['An objective third-person point of view that reports only observable actions', 'A first-person point of view narrated by the main character', 'A stream-of-consciousness narration from inside a characters mind', 'A confessional first-person diary entry'], 0)]),
F('Discrete Math: The Handshake Lemma and Vertex Degree',
  'Grade 11 Functions strand: the handshake lemma states that the sum of the degrees of all vertices in a graph equals twice the number of edges, since every edge contributes exactly two to the total degree count, one for each endpoint.',
  [('What does the handshake lemma state?', ['The sum of the degrees of all vertices equals twice the number of edges', 'The sum of all vertex degrees always equals the number of vertices', 'Every graph must have an odd number of edges', 'The number of edges always equals the number of vertices'], 0),
   ('What is the degree of a vertex in a graph?', ['The number of edges connected to that vertex', 'The total number of vertices in the entire graph', 'The distance between two vertices', 'The colour assigned to that vertex'], 0),
   ('Why does each edge contribute exactly two to the total sum of vertex degrees?', ['Each edge has two endpoints, adding one to the degree of each connected vertex', 'Each edge only connects to a single vertex', 'Edges have no relationship to vertex degree at all', 'Every edge always connects to exactly ten vertices'], 0),
   ('According to the handshake lemma, what must be true about the sum of all vertex degrees in any graph?', ['It must always be an even number', 'It must always be an odd number', 'It must always equal exactly zero', 'It can never be calculated'], 0),
   ('If a graph has 6 edges, what is the sum of the degrees of all its vertices?', ['12', '6', '3', '18'], 0)]),
B('Biology: RNA Interference and Gene Silencing',
  'Grade 11 Biology strand: RNA interference is a natural cellular mechanism in which small RNA molecules bind to complementary messenger RNA, blocking or degrading it and effectively silencing the expression of a specific gene.',
  [('What is RNA interference?', ['A natural mechanism in which small RNA molecules silence the expression of a specific gene', 'A process that always increases the expression of every gene', 'A type of DNA replication error', 'A structure found only in the cell nucleus with no function'], 0),
   ('How does RNA interference silence a gene?', ['Small RNA molecules bind to complementary messenger RNA, blocking or degrading it', 'It permanently deletes the gene from the DNA sequence', 'It increases the number of copies of the targeted messenger RNA', 'It has no interaction with messenger RNA at all'], 0),
   ('What must be true about the small RNA molecule and its messenger RNA target for RNA interference to occur?', ['Their sequences must be complementary to each other', 'They must have completely unrelated sequences', 'The small RNA must be identical to a protein', 'The messenger RNA must be located outside the cell'], 0),
   ('Why is RNA interference of interest for potential medical therapies?', ['It offers a way to selectively silence genes responsible for disease', 'It has no potential medical applications at all', 'It can only be used to increase gene expression, never decrease it', 'It only functions in plant cells, never in humans'], 0),
   ('RNA interference is considered a mechanism of gene regulation that occurs ___.', ['After messenger RNA has already been produced, rather than at the DNA level', 'Only before DNA replication begins', 'Only within the mitochondria', 'Only in cells that are actively dividing'], 0)]),
C('Chemistry: Effervescence — The Chemistry of Antacid Tablets',
  'Grade 11 Chemistry strand: effervescent antacid tablets combine a solid acid, such as citric acid, with a carbonate or bicarbonate base, so that when dissolved in water the two react to release carbon dioxide gas as visible bubbles while neutralizing stomach acid.',
  [('What two general classes of compounds are typically combined in an effervescent antacid tablet?', ['A solid acid and a carbonate or bicarbonate base', 'Two different metals with no acid or base present', 'Only pure water and salt', 'Two identical acids with no base'], 0),
   ('What gas is released as bubbles when an effervescent tablet dissolves in water?', ['Carbon dioxide', 'Pure oxygen', 'Hydrogen gas', 'Nitrogen gas'], 0),
   ('What is the main therapeutic purpose of an antacid tablet?', ['Neutralizing excess stomach acid', 'Increasing the acidity of the stomach', 'Replacing water lost through dehydration', 'Providing a source of dietary sugar'], 0),
   ('Which of these is a common solid acid used in effervescent tablets?', ['Citric acid', 'Table salt', 'Liquid mercury', 'Pure carbon'], 0),
   ('Why does the fizzing reaction only occur once the tablet is dissolved in water?', ['Water allows the acid and base components to dissolve and react with each other', 'The tablet reacts the same way whether or not it is dissolved in water', 'Water prevents any reaction from occurring at all', 'The dry tablet already contains free carbon dioxide gas'], 0)]),
]),
day(129, [
E('Writing: The Encomium — Praise Writing and Tribute',
  'Grade 11 English strand: an encomium is a formal piece of writing or speech that praises a person, achievement, or quality, using vivid examples and elevated language to celebrate its subject with genuine admiration rather than casual flattery.',
  [('What is the main purpose of an encomium?', ['To formally praise a person, achievement, or quality', 'To criticize a public figure', 'To provide a neutral, purely factual report', 'To argue against a popular opinion'], 0),
   ('What kind of language does an encomium typically use?', ['Elevated, celebratory language', 'Only plain, technical vocabulary', 'Language with no emotional content at all', 'Casual slang with no formal structure'], 0),
   ('How does an encomium differ from casual flattery?', ['It is grounded in specific, genuine examples rather than empty compliments', 'It always avoids using any specific examples', 'It is always insincere and exaggerated', 'It never focuses on a specific subject'], 0),
   ('Which of these might be the subject of an encomium?', ['A retiring colleagues career achievements', 'A weather report for the week', 'A grocery list', 'A set of driving directions'], 0),
   ('Why might specific examples strengthen an encomium?', ['They make the praise feel credible and rooted in real achievement', 'Specific examples always weaken the praise being given', 'Encomiums are more effective without any examples', 'Specific examples are irrelevant to this form of writing'], 0)]),
F('Statistics: The Central Limit Theorem',
  'Grade 11 Functions strand: the central limit theorem states that the distribution of sample means approaches a normal distribution as the sample size increases, regardless of the shape of the original population distribution.',
  [('What does the central limit theorem describe?', ['How the distribution of sample means approaches a normal distribution as sample size increases', 'The exact value of a single data point', 'The colour of a graph', 'The area of a triangle inscribed in a circle'], 0),
   ('According to the central limit theorem, what happens as sample size increases?', ['The distribution of sample means becomes increasingly close to a normal distribution', 'The distribution of sample means becomes increasingly random with no pattern', 'Sample means always become identical to the population maximum', 'The population distribution itself changes shape completely'], 0),
   ('Does the original population distribution need to be normal for the central limit theorem to apply?', ['No, the theorem applies regardless of the shape of the original population distribution', 'Yes, the population must always be perfectly normal to begin with', 'The theorem only applies to distributions with exactly two possible outcomes', 'The theorem cannot be applied to any real data'], 0),
   ('Why is the central limit theorem considered foundational to statistical inference?', ['It justifies using the normal distribution to make inferences about population means from sample data', 'It has no practical application in statistics', 'It only applies to extremely small sample sizes', 'It eliminates the need for collecting any sample data'], 0),
   ('The central limit theorem is closely related to which earlier statistical concept?', ['The normal distribution and z-scores', 'The chromatic number of a graph', 'The Euclidean algorithm', 'Modular arithmetic'], 0)]),
B('Biology: Allelopathy — Chemical Warfare Between Plants',
  'Grade 11 Biology strand: allelopathy is a biological phenomenon in which a plant releases chemical compounds into the environment that inhibit the germination, growth, or survival of neighbouring plant species, reducing competition for resources.',
  [('What is allelopathy?', ['A phenomenon in which a plant releases chemicals that inhibit nearby plant species', 'A process where two plants merge into a single organism', 'A type of pollination strategy involving insects', 'A disease that only affects animal cells'], 0),
   ('What is the main ecological benefit of allelopathy for the plant releasing the chemicals?', ['Reduced competition for resources like light, water, and nutrients', 'Increased competition from every neighbouring plant species', 'A guaranteed increase in local animal populations', 'The complete elimination of the need for sunlight'], 0),
   ('What might an allelopathic chemical inhibit in a neighbouring plant?', ['Seed germination or root growth', 'The colour of the neighbouring plants flowers only', 'The neighbouring plants ability to photosynthesize sunlight directly', 'Nothing, since allelopathic chemicals have no biological effect'], 0),
   ('Where might allelopathic compounds be released from a plant?', ['From its roots, leaves, or decomposing plant material', 'Only from the flowers, and nowhere else', 'Only after the entire plant has died with no other release point', 'From the surrounding soil with no involvement from the plant itself'], 0),
   ('Why might allelopathy be considered a form of chemical competition among plants?', ['It allows a plant to indirectly suppress nearby competitors without direct physical contact', 'It always requires two plants to physically touch to have any effect', 'Allelopathy has no connection to competition between organisms', 'It only occurs between plants and animals, never between two plants'], 0)]),
C('Chemistry: The Chemistry of Composting and Organic Decomposition',
  'Grade 11 Chemistry strand: composting relies on microbial decomposition reactions that break down complex organic molecules such as cellulose and proteins into simpler compounds, releasing carbon dioxide, water, and heat while forming nutrient-rich humus.',
  [('What process drives the breakdown of organic material during composting?', ['Microbial decomposition reactions', 'A single non-biological chemical reaction with no microorganisms involved', 'Nuclear fission of the organic material', 'Complete evaporation of all organic matter'], 0),
   ('Which complex organic molecules are broken down during composting?', ['Cellulose and proteins', 'Only pure metals', 'Only inorganic salts', 'Only noble gases'], 0),
   ('What gas is commonly released during the decomposition process in composting?', ['Carbon dioxide', 'Pure hydrogen gas only', 'Chlorine gas', 'Neon gas'], 0),
   ('What nutrient-rich material is formed as a result of composting?', ['Humus', 'Pure crystalline salt', 'Liquid mercury', 'Synthetic plastic'], 0),
   ('Why does a compost pile often feel warm during active decomposition?', ['The microbial breakdown reactions release heat as a byproduct', 'Decomposition always absorbs heat from the surrounding environment', 'Compost piles have no chemical reactions occurring within them', 'The warmth comes only from direct sunlight exposure'], 0)]),
]),
day(130, [
E('English Review: Motif, Genre, Voice, and Persuasion',
  'Grade 11 English strand review: students revisit motif and recurring symbols, the ballad, the process essay, active and passive voice, the roman a clef, clickbait headlines, the personal narrative speech, narrative distance, and the encomium.',
  [('What is a motif?', ['A recurring image, phrase, or idea repeated throughout a text', 'A single event that happens only once in a story', 'A type of punctuation mark', 'A formal citation style'], 0),
   ('What does a ballad primarily do?', ['Tells a story through verse, often set to music', 'Presents a list of unrelated facts', 'Avoids any use of rhythm or repetition', 'Functions only as a formal legal document'], 0),
   ('What is the main purpose of a process essay?', ['To explain how to complete a task or how something works', 'To argue a single controversial opinion', 'To describe a personal memory with no instructional purpose', 'To summarize a work of fiction'], 0),
   ('What is a roman a clef?', ['A novel in which real people or events are thinly disguised as fiction', 'A novel with no connection to reality whatsoever', 'A type of formal legal document', 'A poem written entirely in French'], 0),
   ('What is the main purpose of an encomium?', ['To formally praise a person, achievement, or quality', 'To criticize a public figure', 'To provide a neutral, purely factual report', 'To argue against a popular opinion'], 0)]),
F('Functions Review: Calculus, Discrete Math, Geometry, and Statistics',
  'Grade 11 Functions strand review: students revisit the derivative as a limit, trees and spanning trees, Diophantine equations, vector equations of lines in three dimensions, roots of unity, the Poisson distribution, sinking funds, the handshake lemma, and the central limit theorem.',
  [('How is the derivative of a function at a point defined?', ['As the limit of the average rate of change as the interval shrinks toward zero', 'As the sum of all function values', 'As a fixed number unrelated to the function', 'As the total area under the curve'], 0),
   ('What defines a tree in graph theory?', ['A connected graph with no cycles', 'A graph with every vertex connected to every other vertex', 'A graph containing only isolated vertices with no edges', 'A graph that must contain at least one cycle'], 0),
   ('What is a Diophantine equation?', ['A polynomial equation for which only integer solutions are sought', 'An equation with no solutions of any kind', 'An equation that only allows decimal solutions', 'A geometric formula for area'], 0),
   ('How many distinct nth roots does a nonzero complex number have?', ['Exactly n', 'Exactly 1', 'Exactly 2, regardless of n', 'Infinitely many'], 0),
   ('What does the central limit theorem describe?', ['How the distribution of sample means approaches a normal distribution as sample size increases', 'The exact value of a single data point', 'The colour of a graph', 'The area of a triangle inscribed in a circle'], 0)]),
B('Biology Review: Cell Biology, Genetics, Physiology, and Ecology',
  'Grade 11 Biology strand review: students revisit the cytoskeleton, endocrine disruptors, polyploidy, the blood-brain barrier, hibernation and torpor, quorum sensing, the diving reflex, RNA interference, and allelopathy.',
  [('What is the cytoskeleton?', ['A dynamic network of protein filaments within a cell', 'A rigid outer shell surrounding the cell membrane', 'A type of carbohydrate stored in the nucleus', 'A structure found only in bacterial cells'], 0),
   ('What is an endocrine disruptor?', ['A chemical compound that interferes with normal hormone signalling', 'A hormone naturally produced by the pancreas', 'A type of vitamin required for healthy bones', 'A protein that has no interaction with the endocrine system'], 0),
   ('What is polyploidy?', ['A condition in which an organism has more than two complete sets of chromosomes', 'A condition where an organism has no chromosomes at all', 'A type of asexual reproduction with no genetic change', 'A disease affecting only animal cells'], 0),
   ('What is the blood-brain barrier?', ['A selectively permeable layer of tightly joined cells lining the brain capillaries', 'A bone structure that surrounds the entire brain', 'A type of muscle found only in the heart', 'A layer of skin on the outside of the skull'], 0),
   ('What is allelopathy?', ['A phenomenon in which a plant releases chemicals that inhibit nearby plant species', 'A process where two plants merge into a single organism', 'A type of pollination strategy involving insects', 'A disease that only affects animal cells'], 0)]),
C('Chemistry Review: Coordination Chemistry, Materials, and Applied Reactions',
  'Grade 11 Chemistry strand review: students revisit chelation therapy, vulcanization, reverse osmosis, catalytic converters, adhesive chemistry, enthalpy of solution, leather tanning, antacid effervescence, and the chemistry of composting.',
  [('What is a chelating agent?', ['A molecule that binds tightly to metal ions through multiple coordinate bonds', 'A gas used only in refrigeration', 'An acid with no metal-binding ability', 'A type of radioactive isotope'], 0),
   ('What is vulcanization?', ['A chemical process that forms cross-links between polymer chains in rubber using sulfur', 'A process that removes all polymer chains from rubber', 'A physical process with no chemical reaction involved', 'A method of melting rubber into a liquid permanently'], 0),
   ('What does reverse osmosis use to purify water?', ['External pressure forcing water through a semi-permeable membrane', 'Boiling the water at extremely high temperatures', 'Freezing the water into solid ice', 'Adding large amounts of salt to the water'], 0),
   ('What is the main purpose of a catalytic converter?', ['Converting harmful exhaust gases into less harmful substances', 'Increasing the amount of pollution released by a vehicle', 'Storing fuel before it reaches the engine', 'Cooling the engine during operation'], 0),
   ('What process drives the breakdown of organic material during composting?', ['Microbial decomposition reactions', 'A single non-biological chemical reaction with no microorganisms involved', 'Nuclear fission of the organic material', 'Complete evaporation of all organic matter'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_121_130)
    append_to(11, g11_121_130)
