#!/usr/bin/env python3
"""Grade 11, Days 111-120 -- extends Grade 11 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade11.json)
extensively to avoid any overlap: juxtaposition, the prose poem, letters
of recommendation, the dash and parenthetical elements, ekphrastic poetry,
native advertising, extended metaphor and conceit, the TED-style talk,
and foil characters; limits, continuity, recurrence relations, the
Chinese Remainder Theorem, graph colouring, vector equations of planes,
De Moivre's Theorem, Bayes Theorem, and perpetuities; desert ecosystems,
bioluminescence, camouflage and mimicry, the placenta, telomeres,
apoptosis, the gut-brain axis, bioremediation, and hydrothermal vent
ecosystems; molecular orbital theory, orbital hybridization, coordination
compounds, chemiluminescence, fermentation/winemaking, sports drink
electrolytes, perfume chemistry, lachrymatory agents (tear gas/onions),
and the chemistry of photography.

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
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


g11_111_120 = [
day(111, [
E('Reading: Analyzing Juxtaposition in Literature',
  'Grade 11 English strand: juxtaposition places two contrasting elements side by side in a text, highlighting their differences and creating deeper meaning, tension, or thematic emphasis.',
  [('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('What effect does juxtaposition typically create in a text?', ['It highlights differences and creates deeper meaning or tension', 'It removes all meaning from a text', 'It always confuses the reader with no purpose', 'It eliminates the need for description'], 0),
   ('Which is an example of juxtaposition in a novel?', ['Describing a lavish celebration immediately followed by a scene of poverty', 'Describing only one setting throughout the story', 'Listing facts with no comparison', 'Using only dialogue with no description'], 0),
   ('Why might an author juxtapose two characters?', ['To emphasize how different the characters are from each other', 'To make the characters seem identical', 'To avoid describing either character', 'To remove conflict from the story'], 0),
   ('Juxtaposition is often used by authors to explore contrasts such as ___.', ['Wealth and poverty, or innocence and corruption', 'Only numbers and equations', 'Only weather patterns', 'Only geographic locations with no thematic meaning'], 0)]),
F('Calculus Preview: An Introduction to Limits',
  'Grade 11 Functions strand: a limit describes the value a function approaches as its input approaches a certain number, a foundational idea used to formally define the derivative and analyze function behaviour near a point.',
  [('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('Why are limits considered foundational to calculus?', ['They are used to formally define the derivative', 'They have no connection to any other calculus concept', 'They only apply to whole numbers', 'They eliminate the need to study functions'], 0),
   ('As x approaches 4, if f(x) gets closer and closer to 16, what is the limit of f(x) as x approaches 4?', ['16', '4', '0', 'Undefined in all cases'], 0),
   ('Can a limit exist at a point even if the function is undefined there?', ['Yes, a limit can exist even if the function itself is undefined at that point', 'No, a limit only exists where the function is defined', 'Limits never exist for undefined functions under any circumstance', 'Limits are unrelated to function values'], 0),
   ('Understanding limits helps mathematicians analyze ___.', ['How a function behaves as it approaches specific values', 'Only the colour of a graph', 'Only whole number arithmetic', 'Only basic geometry'], 0)]),
B('Biology: Desert Ecosystems and Xerophytic Adaptations',
  'Grade 11 Biology strand: desert ecosystems receive very little precipitation, and xerophytic plants and desert animals have evolved specialized physiological adaptations, such as water storage and reduced water loss, to survive extreme aridity.',
  [('What defines a desert ecosystem?', ['Very little precipitation', 'Extremely high precipitation', 'Constant freezing temperatures only', 'No sunlight at all'], 0),
   ('What does the term xerophytic describe?', ['Plants adapted to survive in very dry conditions', 'Plants that require constant flooding', 'Animals that live only underwater', 'A type of rock formation'], 0),
   ('What is one common adaptation in xerophytic plants?', ['Thick, water-storing tissues like those in a cactus', 'Thin leaves that maximize water loss', 'A requirement for daily flooding', 'An inability to survive any sunlight'], 0),
   ('Why might many desert animals be nocturnal?', ['To avoid the extreme heat and water loss associated with daytime activity', 'Nocturnal behaviour has no survival advantage', 'To avoid finding food entirely', 'Because deserts have no daytime at all'], 0),
   ('Desert ecosystems can be found in which types of climates?', ['Both hot and cold regions with low precipitation', 'Only underwater locations', 'Only areas with constant rainfall', 'Only areas near the equator'], 0)]),
C('Chemistry: Molecular Orbital Theory — An Introduction',
  'Grade 11 Chemistry strand: molecular orbital theory describes how atomic orbitals combine to form bonding and antibonding molecular orbitals, offering a more detailed model of chemical bonding than simple Lewis structures.',
  [('What does molecular orbital theory describe?', ['How atomic orbitals combine to form molecular orbitals', 'Only the shape of a single atom', 'The colour of a chemical compound', 'The temperature at which a substance boils'], 0),
   ('What are the two main types of molecular orbitals formed when atomic orbitals combine?', ['Bonding and antibonding orbitals', 'Only positive orbitals', 'Only negative orbitals', 'Only neutral orbitals'], 0),
   ('How does a bonding molecular orbital generally affect stability?', ['It increases stability by lowering the overall energy of the molecule', 'It always destabilizes the molecule completely', 'It has no effect on molecular stability', 'It only exists in unstable molecules'], 0),
   ('What advantage does molecular orbital theory offer over simple Lewis structures?', ['It provides a more detailed, quantum-based model of bonding', 'It ignores electrons entirely', 'It only applies to single atoms with no bonding', 'It cannot explain any chemical bonds'], 0),
   ('Molecular orbital theory is especially useful for explaining properties such as ___.', ['Magnetic behaviour and bond order in molecules', 'The taste of a substance', 'The colour of the sky', 'The price of a chemical compound'], 0)]),
]),
day(112, [
E('Poetry: The Prose Poem',
  'Grade 11 English strand: a prose poem is written in continuous prose paragraphs rather than in verse lines, yet still relies on poetic techniques like imagery, rhythm, and compression of meaning.',
  [('How is a prose poem structured?', ['In continuous prose paragraphs rather than verse lines', 'Only in strict rhyming couplets', 'Only as a list of single words', 'Only as a series of questions'], 0),
   ('What poetic techniques might a prose poem still use?', ['Imagery, rhythm, and compression of meaning', 'None at all, since it uses no poetic devices', 'Only formal citations', 'Only mathematical notation'], 0),
   ('How does a prose poem differ from a traditional poem in form?', ['It lacks line breaks and is written like a paragraph', 'It always has a strict rhyme scheme', 'It is always exactly fourteen lines long', 'It cannot contain any imagery'], 0),
   ('Why might a poet choose the prose poem form?', ['To blend the density of poetry with the flow of prose', 'To avoid using any literary devices', 'Prose poems are never used by serious writers', 'To eliminate all meaning from the writing'], 0),
   ('A prose poem still shares which quality with traditional poetry?', ['A focus on carefully chosen, compressed language', 'A strict requirement for line breaks', 'A requirement to always rhyme', 'A complete absence of imagery'], 0)]),
F('Calculus Preview: Continuity of Functions',
  'Grade 11 Functions strand: a function is continuous at a point if its limit exists there, the function is defined there, and the limit equals the function value, meaning the graph has no breaks, holes, or jumps at that point.',
  [('What does it mean for a function to be continuous at a point?', ['The limit exists, the function is defined, and the limit equals the function value', 'The function is always undefined at that point', 'The graph must have a break at that point', 'Continuity has no formal definition'], 0),
   ('What might indicate a function is NOT continuous at a certain point?', ['A hole, jump, or break in the graph at that point', 'A perfectly smooth curve with no interruptions', 'A straight line with no curves', 'A function defined for all real numbers'], 0),
   ('Why is continuity an important concept before studying derivatives?', ['A function generally needs to be continuous to have a derivative at a point', 'Continuity has no connection to derivatives at all', 'Discontinuous functions always have derivatives everywhere', 'Continuity only applies to whole numbers'], 0),
   ('Which of these commonly causes a discontinuity in a rational function?', ['A value that makes the denominator equal to zero', 'Any positive numerator', 'Any function with a straight-line graph', 'A function with no variables'], 0),
   ('A continuous function can generally be sketched ___.', ['Without lifting your pencil from the paper', 'Only using a ruler and no curves', 'Only as a series of disconnected points', 'Only if it has no domain at all'], 0)]),
B('Biology: Bioluminescence in Marine and Terrestrial Organisms',
  'Grade 11 Biology strand: bioluminescence is the production of light by living organisms through a chemical reaction involving the molecule luciferin and the enzyme luciferase, used for purposes like predation, defence, and communication.',
  [('What is bioluminescence?', ['The production of light by living organisms through a chemical reaction', 'The absorption of light by an organism with no light produced', 'A process only found in plants', 'A type of camouflage using colour change alone'], 0),
   ('What molecule and enzyme are commonly involved in bioluminescence?', ['Luciferin and luciferase', 'Chlorophyll and glucose', 'Hemoglobin and insulin', 'DNA and RNA'], 0),
   ('Which environment is especially rich in bioluminescent organisms?', ['The deep ocean', 'The Sahara Desert', 'The Arctic tundra ice sheet interior', 'The upper atmosphere'], 0),
   ('What is one purpose bioluminescence can serve for an organism?', ['Attracting prey or deterring predators', 'It always harms the organism producing it', 'It has no biological function at all', 'It only occurs after an organism has died'], 0),
   ('Besides marine organisms, which other group can exhibit bioluminescence?', ['Certain terrestrial insects, like fireflies', 'Only mammals', 'Only birds', 'Only reptiles'], 0)]),
C('Chemistry: Orbital Hybridization (sp, sp2, sp3)',
  'Grade 11 Chemistry strand: orbital hybridization describes how atomic orbitals mix to form new hybrid orbitals, such as sp, sp2, and sp3, which explain molecular geometry and bonding patterns in covalent compounds.',
  [('What does orbital hybridization describe?', ['How atomic orbitals mix to form new hybrid orbitals', 'The colour of a chemical compound', 'The temperature at which a substance freezes', 'The mass of a single atom'], 0),
   ('What geometry is typically associated with sp3 hybridization?', ['Tetrahedral', 'Linear', 'Trigonal planar only', 'Spherical with no defined shape'], 0),
   ('What geometry is typically associated with sp hybridization?', ['Linear', 'Tetrahedral', 'Octahedral', 'Trigonal bipyramidal'], 0),
   ('How many hybrid orbitals form from sp2 hybridization?', ['Three', 'One', 'Five', 'Seven'], 0),
   ('Why is understanding hybridization useful in chemistry?', ['It helps explain and predict the shapes of molecules', 'It has no connection to molecular shape', 'It only applies to ionic compounds', 'It eliminates the need to understand bonding'], 0)]),
]),
day(113, [
E('Writing: Writing a Letter of Recommendation',
  'Grade 11 English strand: a letter of recommendation highlights a persons strengths, skills, and achievements through specific examples, written to support their application for a job, program, or opportunity.',
  [('What is the purpose of a letter of recommendation?', ['To highlight a persons strengths and support their application', 'To criticize a person without any specific reason', 'To provide unrelated general information', 'To replace the persons own application entirely'], 0),
   ('What should a strong letter of recommendation include?', ['Specific examples of the persons skills and achievements', 'Only vague, general praise with no examples', 'No mention of the persons abilities at all', 'Only negative comments about the person'], 0),
   ('Who typically writes a letter of recommendation?', ['Someone who knows the persons work or character well, like a teacher or employer', 'A random stranger with no connection to the person', 'The person being recommended, about themselves', 'An anonymous source with no name'], 0),
   ('Why is specificity important in a letter of recommendation?', ['Specific examples make the praise more credible and convincing', 'Specific details are never useful in this type of letter', 'Vague statements are always more persuasive', 'Specificity makes the letter less believable'], 0),
   ('A letter of recommendation is often required for which of these?', ['A job application, scholarship, or academic program', 'A grocery list', 'A weather report', 'A restaurant menu'], 0)]),
F('Discrete Math: An Introduction to Recurrence Relations',
  'Grade 11 Functions strand: a recurrence relation defines each term of a sequence based on one or more previous terms, providing a recursive way to model growth patterns, algorithms, and sequences like the Fibonacci numbers.',
  [('What does a recurrence relation define?', ['Each term of a sequence based on one or more previous terms', 'Only a single fixed value with no pattern', 'A relation between two unrelated sequences', 'A rule with no connection to sequences'], 0),
   ('Which sequence is a classic example defined by a recurrence relation?', ['The Fibonacci sequence', 'A sequence of random unrelated numbers', 'A sequence with no defined terms', 'A sequence containing only zeros'], 0),
   ('What information is typically needed to fully define a recurrence relation?', ['The recursive rule and one or more initial terms', 'Only the final term of the sequence', 'No information is needed at all', 'Only the sum of all terms'], 0),
   ('Recurrence relations are useful for modelling ___.', ['Growth patterns and algorithms that build on previous steps', 'Only static, unchanging values', 'Only random, unrelated events', 'Only geometric shapes with no numeric pattern'], 0),
   ('If a(n) = a(n-1) + 2 and a(1) = 3, what is a(2)?', ['5', '3', '6', '2'], 0)]),
B('Biology: Camouflage and Mimicry as Survival Strategies',
  'Grade 11 Biology strand: camouflage allows organisms to blend into their surroundings to avoid detection, while mimicry involves an organism resembling another species or object, both serving as evolved survival strategies against predators.',
  [('What is camouflage?', ['An adaptation allowing an organism to blend into its surroundings', 'A behaviour where an organism attacks its predator directly', 'A process where an organism changes species entirely', 'A method of long-distance migration'], 0),
   ('What is mimicry?', ['When an organism resembles another species or object', 'When an organism hides underground permanently', 'A type of digestive process', 'A form of asexual reproduction'], 0),
   ('What is the main survival benefit of camouflage?', ['Avoiding detection by predators or prey', 'Increasing an organisms visibility to attract predators', 'Making an organism grow larger', 'Eliminating the need for any food'], 0),
   ('In Batesian mimicry, a harmless species resembles ___.', ['A harmful or unpalatable species to deter predators', 'A completely unrelated inanimate object only', 'Another harmless species with no survival benefit', 'Its own predator exactly'], 0),
   ('Camouflage and mimicry are both considered results of ___.', ['Natural selection favouring traits that improve survival', 'Random chance with no evolutionary basis', 'Deliberate choices made by the organism', 'A process unrelated to evolution'], 0)]),
C('Chemistry: Coordination Compounds and Complex Ions',
  'Grade 11 Chemistry strand: a coordination compound consists of a central metal ion surrounded by molecules or ions called ligands, forming a complex ion held together by coordinate covalent bonds.',
  [('What is a coordination compound built around?', ['A central metal ion surrounded by ligands', 'Only carbon atoms with no metal present', 'A single isolated electron', 'A pure element with no other atoms'], 0),
   ('What is a ligand?', ['A molecule or ion that binds to a central metal ion', 'A type of acid with no metal involvement', 'A unit of temperature measurement', 'A type of radioactive particle'], 0),
   ('What type of bond typically holds a ligand to the central metal ion?', ['A coordinate covalent bond', 'An ionic bond only', 'A metallic bond only', 'No bond is formed at all'], 0),
   ('Coordination compounds are often known for having ___.', ['Vivid, distinctive colours', 'No colour whatsoever', 'Only a gaseous state at room temperature', 'A complete absence of any metal'], 0),
   ('Where might coordination compounds be found in biological systems?', ['In molecules like hemoglobin, which contains iron', 'Nowhere, since living things never contain coordination compounds', 'Only in synthetic laboratory chemicals', 'Only in radioactive materials'], 0)]),
]),
day(114, [
E('Grammar: The Dash and Parenthetical Elements',
  'Grade 11 English strand: the em dash sets off parenthetical information, an abrupt shift, or emphasis within a sentence, offering a more dramatic alternative to commas or parentheses for inserting extra detail.',
  [('What is one common use of the em dash in a sentence?', ['Setting off parenthetical information or creating emphasis', 'Ending every sentence in a paragraph', 'Replacing all periods in an essay', 'Indicating a question is being asked'], 0),
   ('How does an em dash compare to commas or parentheses for inserting extra information?', ['It offers a more dramatic, attention-grabbing alternative', 'It has the exact same effect with no difference at all', 'It can never be used for this purpose', 'It is only used in mathematical equations'], 0),
   ('Which sentence correctly uses a dash for emphasis?', ['She had only one goal — to win.', 'She had only one goal, to win, — the end.', 'She had — only one goal to win.', 'She — had only one goal to win —.'], 0),
   ('What can a dash indicate besides parenthetical information?', ['An abrupt shift in thought or tone', 'Only a grammatical error', 'The end of an entire essay', 'A citation format'], 0),
   ('Why might a writer choose a dash instead of a comma in certain sentences?', ['To create a stronger, more dramatic pause or emphasis', 'Dashes and commas always function identically with no stylistic difference', 'Dashes are grammatically forbidden in formal writing', 'To remove all meaning from the sentence'], 0)]),
F('Number Theory: The Chinese Remainder Theorem',
  'Grade 11 Functions strand: the Chinese Remainder Theorem provides a method for solving systems of simultaneous modular congruences, finding a single number that satisfies multiple remainder conditions at once.',
  [('What does the Chinese Remainder Theorem help solve?', ['Systems of simultaneous modular congruences', 'A single linear equation with no remainders', 'The area of a triangle', 'A system of quadratic equations only'], 0),
   ('What does the theorem find when given multiple remainder conditions?', ['A single number that satisfies all the conditions simultaneously', 'A number that satisfies none of the conditions', 'An answer that changes randomly each time', 'Only the largest of the given remainders'], 0),
   ('The Chinese Remainder Theorem is part of which broader field of mathematics?', ['Number theory', 'Geometry', 'Trigonometry', 'Statistics'], 0),
   ('Where might the Chinese Remainder Theorem be applied in modern technology?', ['In areas of cryptography and computer science', 'Only in ancient historical calculations with no modern use', 'Only in measuring physical distances', 'It has no practical applications today'], 0),
   ('The Chinese Remainder Theorem builds on which earlier concept?', ['Modular arithmetic', 'Basic addition of fractions', 'The Pythagorean Theorem', 'Simple linear graphing'], 0)]),
B('Biology: The Placenta and Mammalian Reproductive Strategies',
  'Grade 11 Biology strand: the placenta is a specialized organ that develops during pregnancy in most mammals, allowing nutrient and gas exchange between mother and developing offspring while providing a key evolutionary reproductive strategy.',
  [('What is the placenta?', ['A specialized organ that allows nutrient and gas exchange between mother and offspring', 'A type of bone found only in adult mammals', 'A structure used only for producing sound', 'A part of the digestive system unrelated to reproduction'], 0),
   ('When does the placenta typically develop?', ['During pregnancy in most mammals', 'Only after birth has occurred', 'Only in reptiles, never in mammals', 'It never develops in any species'], 0),
   ('What is exchanged between mother and offspring through the placenta?', ['Nutrients and gases like oxygen and carbon dioxide', 'Only sound vibrations', 'Only light signals', 'Nothing is exchanged at all'], 0),
   ('Placental mammals are one of several reproductive strategies among mammals; which group instead carries offspring in a pouch after a short gestation?', ['Marsupials', 'Reptiles', 'Amphibians', 'Fish'], 0),
   ('Why is the placenta considered an important evolutionary adaptation?', ['It allows extended, protected development of offspring before birth', 'It has no evolutionary significance at all', 'It prevents any nutrient exchange between mother and offspring', 'It only exists in a single mammal species'], 0)]),
C('Chemistry: Chemiluminescence — The Chemistry of Glow Sticks',
  'Grade 11 Chemistry strand: chemiluminescence is the emission of light resulting from a chemical reaction rather than heat, as seen in glow sticks, where mixing chemicals triggers an energy-releasing reaction that produces visible light.',
  [('What is chemiluminescence?', ['The emission of light resulting from a chemical reaction', 'The absorption of light with no emission at all', 'A process that only occurs in living organisms', 'A physical change with no chemical reaction involved'], 0),
   ('How does a glow stick typically produce light?', ['Mixing chemicals inside triggers a light-releasing chemical reaction', 'By absorbing sunlight during the day', 'By using a small battery and light bulb', 'By heating the stick with an external flame'], 0),
   ('How does chemiluminescence differ from incandescence, which produces light from heat?', ['Chemiluminescence produces light through a chemical reaction, not heat', 'Chemiluminescence always requires extremely high temperatures', 'They are identical processes with no difference', 'Incandescence never involves any light production'], 0),
   ('What happens when the internal capsule of a glow stick is broken?', ['Two chemicals mix and react, releasing energy as light', 'The chemicals instantly evaporate with no reaction', 'Nothing happens because no reaction occurs', 'The stick becomes permanently unusable with no light produced'], 0),
   ('Chemiluminescence is closely related to which similar biological phenomenon?', ['Bioluminescence, seen in organisms like fireflies', 'Photosynthesis', 'Cellular respiration', 'Osmosis'], 0)]),
]),
day(115, [
E('Literature: Ekphrastic Poetry — Writing About Art',
  'Grade 11 English strand: ekphrastic poetry vividly describes or responds to a work of visual art, using language to interpret, animate, or reflect on the meaning and emotion captured within the artwork.',
  [('What is ekphrastic poetry?', ['Poetry that vividly describes or responds to a work of visual art', 'Poetry written only about nature', 'Poetry with no descriptive language at all', 'A type of poem with a strict rhyme scheme only'], 0),
   ('What might an ekphrastic poem attempt to do with a painting or sculpture?', ['Interpret, animate, or reflect on its meaning and emotion', 'Ignore the artwork completely', 'Simply state the artworks title with no further detail', 'Replace the artwork entirely with unrelated content'], 0),
   ('Why might poets be drawn to writing ekphrastic poetry?', ['To explore how language and visual art can interact and inform each other', 'Ekphrastic poetry has no connection to visual art', 'It removes the need for any artistic interpretation', 'It always criticizes the original artwork'], 0),
   ('Which is an example of an ekphrastic poem topic?', ['A poem written in response to a famous painting', 'A poem about mathematical equations only', 'A poem with no subject matter at all', 'A grocery list written in verse'], 0),
   ('Ekphrastic poetry connects which two art forms?', ['Visual art and written poetry', 'Only music and dance', 'Only architecture and film', 'Only sculpture and mathematics'], 0)]),
F('Discrete Math: An Introduction to Graph Colouring',
  'Grade 11 Functions strand: graph colouring assigns colours to the nodes of a graph so that no two connected nodes share the same colour, with the minimum number of colours needed called the chromatic number.',
  [('What is the goal of graph colouring?', ['Assigning colours to nodes so no two connected nodes share the same colour', 'Assigning the exact same colour to every node', 'Removing all colours from a graph', 'Counting the total number of edges only'], 0),
   ('What is the chromatic number of a graph?', ['The minimum number of colours needed to properly colour it', 'The total number of nodes in the graph', 'The total number of edges in the graph', 'A number that is always equal to zero'], 0),
   ('What real-world problem can graph colouring help solve?', ['Scheduling conflicts, such as assigning exam time slots', 'The freezing point of water', 'The colour of the sky', 'The taste of a particular food'], 0),
   ('If two nodes in a graph are connected by an edge, what must be true about their colours?', ['They must be different colours', 'They must always be the same colour', 'Colour has no meaning in graph theory', 'Only one of the two nodes can have any colour'], 0),
   ('Graph colouring is a key topic within which broader field of mathematics?', ['Discrete mathematics and graph theory', 'Basic arithmetic', 'Trigonometry', 'Financial mathematics'], 0)]),
B('Biology: Telomeres and Cellular Aging',
  'Grade 11 Biology strand: telomeres are protective caps at the ends of chromosomes that shorten with each cell division, a process linked to cellular aging and playing a role in limiting how many times a cell can divide.',
  [('What are telomeres?', ['Protective caps at the ends of chromosomes', 'A type of protein found only in muscle tissue', 'A structure located outside the cell entirely', 'A type of sugar molecule used in digestion'], 0),
    ('What happens to telomeres with each cell division?', ['They gradually shorten', 'They grow longer indefinitely', 'They remain exactly the same length forever', 'They disappear completely after a single division'], 0),
    ('What biological process is telomere shortening linked to?', ['Cellular aging', 'Immediate cell death with no aging process', 'Cellular growth with no limit', 'Digestion of nutrients'], 0),
    ('What role do telomeres play in how many times a cell can divide?', ['They help limit the total number of divisions a cell can undergo', 'They allow unlimited cell division with no restriction', 'They have no connection to cell division at all', 'They immediately stop all cell division from the start'], 0),
    ('Why are telomeres of interest in aging and cancer research?', ['Their length and behaviour are linked to cellular lifespan and abnormal cell growth', 'Telomeres have no connection to human health', 'They are only found in plant cells', 'They play no role in any disease research'], 0)]),
C('Chemistry: Fermentation and the Chemistry of Winemaking',
  'Grade 11 Chemistry strand: fermentation in winemaking involves yeast converting sugars in grape juice into ethanol and carbon dioxide through anaerobic respiration, a chemical process central to producing wine.',
  [('What does fermentation convert sugars into during winemaking?', ['Ethanol and carbon dioxide', 'Only pure water', 'Only oxygen gas', 'Only table salt'], 0),
   ('What organism carries out the fermentation process in winemaking?', ['Yeast', 'Bacteria found only in soil', 'A type of algae', 'A synthetic chemical catalyst'], 0),
   ('Is fermentation an aerobic or anaerobic process?', ['Anaerobic (occurring without oxygen)', 'Aerobic (requiring oxygen)', 'It requires neither oxygen nor any chemical reaction', 'It occurs only in extremely high temperatures'], 0),
   ('What gas is released as a byproduct during fermentation?', ['Carbon dioxide', 'Nitrogen gas', 'Pure oxygen', 'Hydrogen gas'], 0),
   ('Why is understanding the chemistry of fermentation useful beyond winemaking?', ['Similar processes are used in producing beer, bread, and other fermented foods', 'Fermentation has no other applications beyond wine', 'Fermentation is a purely modern invention', 'Fermentation only occurs in laboratory settings'], 0)]),
]),
day(116, [
E('Media Literacy: Analyzing Native Advertising and Sponsored Content',
  'Grade 11 English strand: native advertising and sponsored content are designed to blend in with regular articles or posts, so critical readers must learn to identify when content is actually paid promotion rather than independent journalism.',
  [('What is native advertising?', ['Paid content designed to blend in with regular articles or posts', 'Content that is always clearly labeled as an advertisement in bold letters', 'A type of grammar rule', 'A form of punctuation'], 0),
   ('Why can native advertising be difficult to identify?', ['It is designed to look like regular editorial content', 'It always appears in a completely different format from articles', 'It is required by law to be clearly marked in giant red text', 'It never appears near real articles'], 0),
   ('What skill helps readers identify sponsored content?', ['Media literacy and critical reading', 'Ignoring all content on a webpage', 'Reading only headlines and nothing else', 'Believing all content is equally trustworthy'], 0),
   ('Why do companies use native advertising?', ['To promote products in a way that feels less like a traditional ad', 'To ensure their content is entirely and obviously an advertisement', 'Because they are legally required to disguise their promotions', 'To avoid attracting any customers'], 0),
   ('What should readers look for to identify sponsored content?', ['Small labels like Sponsored or Paid Content near the article', 'Nothing, since sponsored content cannot be identified', 'Only the length of the article', 'Only the colour of the website'], 0)]),
F('Geometry: Vector Equations of Planes in Three Dimensions',
  'Grade 11 Functions strand: a plane in three dimensions can be described using a vector equation involving a point on the plane and two direction vectors that lie within it, extending the earlier study of vector equations of lines.',
  [('What is needed to write the vector equation of a plane?', ['A point on the plane and two direction vectors lying within it', 'Only a single point with no direction vectors', 'Only the origin, with nothing else needed', 'A single number with no vectors at all'], 0),
   ('How does the vector equation of a plane extend the vector equation of a line?', ['It uses two direction vectors instead of just one', 'It removes the need for any direction vectors', 'It only works in two dimensions, not three', 'It is completely unrelated to vector equations of lines'], 0),
   ('What geometric object does a vector equation of a plane describe?', ['A flat, two-dimensional surface extending infinitely in three-dimensional space', 'A single point in space', 'A one-dimensional line only', 'A three-dimensional solid shape'], 0),
   ('Why are two direction vectors needed to define a plane, rather than just one?', ['A single direction vector could only define a line, not a full flat surface', 'One vector is always sufficient to define an entire plane', 'Direction vectors are not used when describing planes', 'Planes do not require any vectors at all'], 0),
   ('Vector equations of planes are useful in fields such as ___.', ['3D modelling, physics, and engineering', 'Only basic arithmetic', 'Only simple counting problems', 'Only measuring temperature'], 0)]),
B('Biology: Apoptosis — Programmed Cell Death',
  'Grade 11 Biology strand: apoptosis is a regulated, programmed process by which cells self-destruct in a controlled manner, essential for normal development, tissue maintenance, and preventing the growth of damaged or cancerous cells.',
  [('What is apoptosis?', ['A regulated, programmed process by which cells self-destruct', 'An uncontrolled process where cells burst open randomly', 'A process where cells grow uncontrollably forever', 'A type of cell division unrelated to cell death'], 0),
   ('Why is apoptosis important for normal development?', ['It helps remove unnecessary or damaged cells in a controlled way', 'It has no role in development at all', 'It only occurs after an organism has died', 'It prevents any cells from ever being removed'], 0),
   ('How does apoptosis differ from necrosis, an uncontrolled form of cell death?', ['Apoptosis is a controlled, regulated process, while necrosis is often due to injury or damage', 'Apoptosis and necrosis are identical processes', 'Necrosis is always a planned, regulated process', 'Apoptosis always results from external injury only'], 0),
   ('What can happen if apoptosis fails to occur properly in damaged cells?', ['Damaged or abnormal cells may survive and potentially become cancerous', 'The damaged cells are always instantly repaired with no consequence', 'Nothing happens, since apoptosis has no biological importance', 'The organism immediately dies in every case'], 0),
   ('Apoptosis plays an important role in shaping structures during ___.', ['Embryonic development, such as forming separate fingers and toes', 'Only the aging process, with no role in development', 'Only wound healing, with no other function', 'Only plant growth, never in animals'], 0)]),
C('Chemistry: Electrolytes and the Chemistry of Sports Drinks',
  'Grade 11 Chemistry strand: electrolytes are ions like sodium, potassium, and chloride that conduct electrical signals in the body, and sports drinks are formulated to replace electrolytes and fluids lost through sweating during exercise.',
  [('What is an electrolyte?', ['An ion that helps conduct electrical signals in the body', 'A type of solid mineral with no electrical function', 'A molecule found only in plants', 'A gas released during respiration'], 0),
   ('Which of these is a common electrolyte found in sports drinks?', ['Sodium', 'Only pure water with no ions', 'Only sugar with no ions present', 'Only carbon dioxide'], 0),
   ('Why do athletes lose electrolytes during intense exercise?', ['Electrolytes are lost through sweating', 'Electrolytes are never lost through any bodily process', 'Exercise increases electrolyte levels with no loss occurring', 'Only water is lost during exercise, never electrolytes'], 0),
   ('What is the purpose of a sports drink from a chemistry standpoint?', ['To help replace fluids and electrolytes lost through sweating', 'To remove all electrolytes from the body', 'To eliminate the need for water entirely', 'To prevent the body from ever sweating'], 0),
   ('Electrolytes dissolved in water are important because they allow the solution to ___.', ['Conduct electricity', 'Freeze at a much higher temperature always', 'Become a solid at room temperature', 'Lose all its chemical properties'], 0)]),
]),
day(117, [
E('Reading: Analyzing Extended Metaphor and Conceit',
  'Grade 11 English strand: an extended metaphor develops a single comparison across an entire passage, while a conceit is an especially elaborate or surprising extended metaphor, often connecting two very different ideas in an intellectually striking way.',
  [('What is an extended metaphor?', ['A comparison developed across an entire passage or text', 'A comparison used only once in a single sentence', 'A literal statement with no comparison', 'A type of punctuation'], 0),
   ('What distinguishes a conceit from a typical extended metaphor?', ['A conceit is especially elaborate or surprising, connecting very different ideas', 'A conceit never involves any comparison at all', 'A conceit is always exactly one word long', 'A conceit is identical to a simple simile'], 0),
   ('Which of these best describes a metaphysical conceit?', ['An intellectually striking comparison between seemingly unrelated concepts', 'A completely literal, non-figurative statement', 'A short list with no descriptive language', 'A citation format used in essays'], 0),
   ('Why might a poet use a conceit in their writing?', ['To surprise the reader and deepen the meaning of a comparison', 'To avoid using any figurative language whatsoever', 'To confuse the reader with no literary purpose', 'To remove all imagery from the poem'], 0),
   ('An extended metaphor and a conceit both rely on ___.', ['Sustaining a comparison beyond a single, brief mention', 'Using no comparison of any kind', 'Strict adherence to a rhyme scheme', 'Avoiding all figurative language'], 0)]),
F('Complex Numbers: De Moivres Theorem',
  'Grade 11 Functions strand: De Moivres Theorem provides a method for raising a complex number in polar form to a power, using the formula (r(cos θ + i sin θ))^n = r^n(cos nθ + i sin nθ).',
  [('What does De Moivres Theorem help calculate?', ['A complex number in polar form raised to a power', 'The area of a triangle', 'The slope of a line', 'The volume of a sphere'], 0),
   ('De Moivres Theorem builds on which earlier concept?', ['Complex numbers in polar form', 'Basic addition of whole numbers', 'The Pythagorean Theorem', 'Simple linear equations'], 0),
   ('In De Moivres formula, what happens to the angle θ when raising to the power n?', ['It is multiplied by n', 'It is divided by n', 'It stays exactly the same', 'It becomes zero'], 0),
   ('Why is De Moivres Theorem useful for working with complex numbers?', ['It simplifies the process of raising complex numbers to large powers', 'It eliminates the need for complex numbers entirely', 'It only works for real numbers, never complex ones', 'It has no mathematical application'], 0),
   ('De Moivres Theorem connects which two areas of mathematics?', ['Trigonometry and complex numbers', 'Only basic arithmetic and geometry', 'Only statistics and probability', 'Only financial literacy and algebra'], 0)]),
B('Biology: The Gut-Brain Axis and the Enteric Nervous System',
  'Grade 11 Biology strand: the gut-brain axis is the bidirectional communication network linking the digestive system and the brain, involving the enteric nervous system, hormones, and gut microbiota that can influence mood and behaviour.',
  [('What is the gut-brain axis?', ['A bidirectional communication network linking the digestive system and the brain', 'A one-way connection with no communication between organs', 'A structure found only in the brain, unrelated to digestion', 'A type of muscle found in the digestive tract with no nerve connection'], 0),
   ('What is the enteric nervous system?', ['A network of neurons embedded in the lining of the digestive tract', 'A part of the brain unrelated to digestion', 'A type of hormone released only by the kidneys', 'A structure found exclusively in the lungs'], 0),
   ('What role can gut microbiota play in the gut-brain axis?', ['They can influence mood and behaviour through chemical signalling', 'They have no connection to the brain whatsoever', 'They only affect digestion, with no other bodily influence', 'They exist without any interaction with the nervous system'], 0),
   ('Why is the gut sometimes referred to as a second brain?', ['It contains a large, complex network of neurons capable of independent function', 'The gut is scientifically identical to the brain in every way', 'The gut has no nervous tissue at all', 'This description has no scientific basis whatsoever'], 0),
   ('Research on the gut-brain axis has explored potential links to which of these?', ['Mood disorders and mental health', 'Only bone density, with no other connection', 'Only eye colour, with no other connection', 'Only hair growth, with no other connection'], 0)]),
C('Chemistry: The Chemistry of Perfumes and Fragrances',
  'Grade 11 Chemistry strand: perfumes are complex mixtures of volatile organic compounds, including esters and essential oils, carefully blended and diluted in a solvent to create layered scents that evaporate at different rates.',
  [('What are perfumes chemically composed of?', ['Complex mixtures of volatile organic compounds', 'A single pure element with no other compounds', 'Only inorganic salts', 'Only water with no other chemicals'], 0),
   ('Which class of organic compounds is commonly used to create pleasant scents in perfumes?', ['Esters', 'Only strong acids', 'Only strong bases', 'Only noble gases'], 0),
   ('Why do different scent notes in a perfume evaporate at different rates?', ['Different compounds have different volatilities', 'All compounds in a perfume evaporate at the exact same rate', 'Perfumes contain no volatile compounds at all', 'Evaporation rate has no connection to scent'], 0),
   ('What is typically used to dilute the concentrated fragrance compounds in perfume?', ['A solvent, such as alcohol', 'Pure solid metal', 'Concentrated acid with no dilution', 'Liquid nitrogen'], 0),
   ('The layered structure of a perfumes scent, changing over time as it is worn, is due to ___.', ['Compounds with different evaporation rates being released at different times', 'All ingredients evaporating instantly and simultaneously', 'The perfume having no chemical structure at all', 'A single unchanging compound with no variation'], 0)]),
]),
day(118, [
E('Oral Communication: The TED-Style Talk',
  'Grade 11 English strand: a TED-style talk delivers a single, focused idea to a general audience using clear structure, storytelling, and engaging delivery, typically within a concise, well-rehearsed time limit.',
  [('What is a defining feature of a TED-style talk?', ['Delivering a single, focused idea clearly to a general audience', 'Covering as many unrelated topics as possible', 'Reading directly from a dense, technical script with no engagement', 'Avoiding any structure or preparation'], 0),
   ('Why do TED-style talks often use storytelling?', ['To make complex ideas more relatable and engaging for the audience', 'Storytelling is never used in this format', 'To confuse the audience about the main idea', 'To avoid connecting with the audience emotionally'], 0),
   ('What is typically true about the length of a TED-style talk?', ['It is concise and well-rehearsed, often under a set time limit', 'It has no time limit and can last for many hours', 'It is always exactly one minute long', 'Length is never a consideration in this format'], 0),
   ('Why is clear structure important in a TED-style talk?', ['It helps the audience follow and remember the central idea', 'Structure is unnecessary since audiences never need guidance', 'A talk with structure is always less effective', 'Clear structure only matters in written essays, not speeches'], 0),
   ('What is a common goal of a TED-style talk?', ['To inspire, inform, or persuade an audience about a single idea', 'To provide no clear takeaway for the audience', 'To read a list of unrelated facts with no theme', 'To avoid any audience engagement whatsoever'], 0)]),
F('Statistics: An Introduction to Bayes Theorem',
  'Grade 11 Functions strand: Bayes Theorem updates the probability of an event based on new information, combining prior knowledge with new evidence to calculate a more accurate conditional probability.',
  [('What does Bayes Theorem help calculate?', ['An updated probability based on new evidence', 'A fixed probability that never changes', 'The average of a data set', 'The volume of a 3D shape'], 0),
   ('What two things does Bayes Theorem combine?', ['Prior knowledge and new evidence', 'Only random guesses', 'Only historical data with no update', 'Only geometric shapes'], 0),
   ('Bayes Theorem is closely related to which earlier probability concept?', ['Conditional probability', 'The Pythagorean theorem', 'Surface area', 'Linear equations'], 0),
   ('Why is Bayes Theorem useful in fields like medicine?', ['It helps update the likelihood of a diagnosis as new test results come in', 'It has no real-world applications', 'It only applies to games of chance', 'It eliminates the need for any testing'], 0),
   ('If new evidence strongly supports an event, Bayes Theorem would typically ___.', ['Increase the probability estimate for that event', 'Always decrease the probability to zero', 'Have no effect on the probability at all', 'Make the event impossible'], 0)]),
B('Biology: Bioremediation — Using Organisms to Clean Pollution',
  'Grade 11 Biology strand: bioremediation uses living organisms, such as bacteria and fungi, to break down or remove pollutants from contaminated soil, water, or air, offering an environmentally friendly cleanup strategy.',
  [('What is bioremediation?', ['Using living organisms to break down or remove pollutants', 'A process that always increases pollution levels', 'A method of building new factories', 'A type of chemical warfare technology'], 0),
   ('Which organisms are commonly used in bioremediation?', ['Bacteria and fungi', 'Only large mammals', 'Only birds', 'Only reptiles'], 0),
   ('What can bioremediation help clean up?', ['Contaminated soil, water, or air', 'Only clean, unpolluted environments', 'Only outer space debris', 'Only man-made structures with no pollutants'], 0),
   ('Why is bioremediation often considered an environmentally friendly cleanup method?', ['It uses natural biological processes rather than harsh chemical treatments', 'It always requires more toxic chemicals than traditional methods', 'It destroys the environment further', 'It has no connection to environmental cleanup at all'], 0),
   ('Which pollutant might certain bacteria be used to break down through bioremediation?', ['Oil from an oil spill', 'Pure oxygen gas', 'Fresh drinking water', 'Sunlight'], 0)]),
C('Chemistry: The Chemistry of Tears — Lachrymatory Agents',
  'Grade 11 Chemistry strand: lachrymatory agents, such as the compound released when cutting an onion, are volatile chemicals that irritate the eyes and trigger tear production through a reaction with enzymes in plant cells.',
  [('What is a lachrymatory agent?', ['A volatile chemical that irritates the eyes and triggers tears', 'A compound that has no effect on the eyes', 'A solid mineral with no chemical reactivity', 'A gas used only in refrigeration'], 0),
   ('What triggers the release of a lachrymatory compound when cutting an onion?', ['Damage to the onions cells releases enzymes that react to form the irritant', 'The onion releases the compound only when fully intact and uncut', 'Heat alone causes the reaction with no cutting required', 'The compound is released only after the onion is cooked'], 0),
   ('Why do lachrymatory compounds cause eyes to water?', ['They irritate sensitive tissue in the eyes, triggering a tear reflex', 'They have no chemical interaction with the eyes at all', 'They only affect the sense of taste, not the eyes', 'They cause a permanent change in eye colour'], 0),
   ('What might reduce the tear-inducing effect when cutting an onion?', ['Chilling the onion beforehand to slow the chemical reaction', 'Cutting the onion at a much higher temperature to speed up the reaction', 'Avoiding cutting the onion cells at all is impossible when slicing', 'Adding more of the irritant compound directly'], 0),
   ('Studying lachrymatory agents connects chemistry to which everyday experience?', ['Common kitchen chemistry, like preparing food', 'Only industrial manufacturing, with no connection to daily life', 'Only astronomy', 'Only nuclear physics'], 0)]),
]),
day(119, [
E('Reading: Analyzing Foil Characters',
  'Grade 11 English strand: a foil character has traits that contrast sharply with a main character, and this contrast helps highlight and clarify the main characters own qualities, choices, and moral position.',
  [('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0),
   ('What is the purpose of a foil character?', ['To highlight and clarify the main characters qualities through contrast', 'To confuse the reader about the plot', 'To replace the main character entirely', 'To remove all conflict from the story'], 0),
   ('If a protagonist is idealistic, a foil character might be ___.', ['Pragmatic and cynical', 'Also idealistic in the exact same way', 'Nonexistent in the story', 'A narrator only'], 0),
   ('Foil characters are most useful for revealing ___.', ['Personality traits and moral positions through comparison', 'Only the setting of a story', 'Only the time period of a story', 'Nothing about the characters'], 0),
   ('Which is an example of a foil relationship?', ['A morally rigid character paired with a morally flexible character', 'Two identical characters with no differences', 'A character and the weather', 'A character and a map'], 0)]),
F('Financial Mathematics: Perpetuities and Present Value',
  'Grade 11 Functions strand: a perpetuity is a financial instrument that pays a fixed amount of money at regular intervals forever, and its present value can be calculated by dividing the periodic payment by the interest rate.',
  [('What is a perpetuity?', ['A financial instrument that pays a fixed amount forever at regular intervals', 'A loan that must be paid off within one year', 'A one-time lump-sum payment with no future payments', 'An investment that guarantees no return at all'], 0),
   ('How is the present value of a perpetuity typically calculated?', ['By dividing the periodic payment by the interest rate', 'By multiplying the payment by an infinite number of years', 'Present value cannot be calculated for a perpetuity', 'By subtracting the interest rate from the payment amount'], 0),
   ('Why can a perpetuity that pays forever still have a finite present value?', ['Future payments are discounted more heavily the further into the future they occur', 'All future payments are worth exactly the same amount as todays dollar', 'Perpetuities always have an infinite present value with no exception', 'Present value calculations do not apply to perpetuities'], 0),
   ('If a perpetuity pays $100 per year and the interest rate is 5%, what is its present value?', ['$2,000', '$100', '$500', '$20'], 0),
   ('Perpetuities are a useful concept for understanding ___.', ['Long-term financial instruments and valuation', 'Only short-term loans with no long-term application', 'Only physical measurements with no financial connection', 'Only geometry problems'], 0)]),
B('Biology: Hydrothermal Vent Ecosystems and Chemosynthesis',
  'Grade 11 Biology strand: hydrothermal vent ecosystems exist on the deep ocean floor, where specialized bacteria use chemosynthesis to convert chemicals like hydrogen sulfide into energy, supporting entire food webs without sunlight.',
  [('Where are hydrothermal vent ecosystems typically found?', ['On the deep ocean floor', 'On mountain peaks', 'In shallow freshwater lakes', 'In desert regions with no water'], 0),
   ('What process do bacteria at hydrothermal vents use to produce energy?', ['Chemosynthesis', 'Photosynthesis, using direct sunlight', 'Cellular respiration using oxygen from the surface only', 'A process requiring constant sunlight exposure'], 0),
   ('What chemical is commonly used by chemosynthetic bacteria at hydrothermal vents?', ['Hydrogen sulfide', 'Pure oxygen gas only', 'Table salt', 'Liquid nitrogen'], 0),
   ('How can hydrothermal vent ecosystems support life without sunlight?', ['Chemosynthetic bacteria form the base of the food web, replacing the role of sunlight-driven photosynthesis', 'These ecosystems actually require significant sunlight to function', 'Life cannot exist in these ecosystems at all', 'Sunlight has no connection to any ecosystems energy source'], 0),
   ('Why are hydrothermal vent ecosystems significant to scientists studying the origins of life?', ['They demonstrate that life can thrive in extreme conditions without sunlight', 'They prove that sunlight is required for all forms of life everywhere', 'They have no scientific significance at all', 'They were discovered before any other ecosystem on Earth'], 0)]),
C('Chemistry: The Chemistry of Photography — Silver Halides',
  'Grade 11 Chemistry strand: traditional photographic film relies on the light sensitivity of silver halide compounds, which undergo a chemical reaction when exposed to light, forming the basis of the image before further chemical development.',
  [('What compounds are traditional photographic film coated with to capture images?', ['Silver halides', 'Pure carbon', 'Table salt only', 'Liquid mercury'], 0),
   ('What happens to silver halide compounds when exposed to light?', ['They undergo a chemical reaction that begins forming the image', 'They remain completely unaffected by light exposure', 'They instantly evaporate with no chemical change', 'They turn into a gas with no further reaction'], 0),
   ('Why are silver halides useful for photography?', ['They are highly sensitive to light, allowing them to capture an image', 'They are completely insensitive to light of any kind', 'They react only to sound waves, not light', 'They cannot be chemically developed after exposure'], 0),
   ('What additional step is needed after light exposure to fully reveal a photographic image?', ['Chemical development in a darkroom process', 'No further steps are needed after light exposure', 'Exposing the film to additional direct sunlight only', 'Freezing the film at extremely low temperatures'], 0),
   ('The chemistry of photography connects to which broader concept in chemistry?', ['Photochemistry, the study of light-induced chemical reactions', 'Only nuclear chemistry, with no connection to light', 'Only organic chemistry, with no connection to light', 'Only thermochemistry, with no connection to light'], 0)]),
]),
day(120, [
E('English Review: Poetry, Rhetoric, and Literary Devices',
  'Grade 11 English strand review: students revisit juxtaposition, the prose poem, letters of recommendation, the dash, ekphrastic poetry, native advertising, extended metaphor and conceit, TED-style talks, and foil characters.',
  [('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('How is a prose poem structured?', ['In continuous prose paragraphs rather than verse lines', 'Only in strict rhyming couplets', 'Only as a list of single words', 'Only as a series of questions'], 0),
   ('What is ekphrastic poetry?', ['Poetry that vividly describes or responds to a work of visual art', 'Poetry written only about nature', 'Poetry with no descriptive language at all', 'A type of poem with a strict rhyme scheme only'], 0),
   ('What distinguishes a conceit from a typical extended metaphor?', ['A conceit is especially elaborate or surprising, connecting very different ideas', 'A conceit never involves any comparison at all', 'A conceit is always exactly one word long', 'A conceit is identical to a simple simile'], 0),
   ('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0)]),
F('Functions Review: Calculus Foundations, Discrete Math, and Finance',
  'Grade 11 Functions strand review: students revisit limits, continuity, recurrence relations, the Chinese Remainder Theorem, graph colouring, vector equations of planes, De Moivres Theorem, Bayes Theorem, and perpetuities.',
  [('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('What does it mean for a function to be continuous at a point?', ['The limit exists, the function is defined, and the limit equals the function value', 'The function is always undefined at that point', 'The graph must have a break at that point', 'Continuity has no formal definition'], 0),
   ('What is the chromatic number of a graph?', ['The minimum number of colours needed to properly colour it', 'The total number of nodes in the graph', 'The total number of edges in the graph', 'A number that is always equal to zero'], 0),
   ('What does De Moivres Theorem help calculate?', ['A complex number in polar form raised to a power', 'The area of a triangle', 'The slope of a line', 'The volume of a sphere'], 0),
   ('What is a perpetuity?', ['A financial instrument that pays a fixed amount forever at regular intervals', 'A loan that must be paid off within one year', 'A one-time lump-sum payment with no future payments', 'An investment that guarantees no return at all'], 0)]),
B('Biology Review: Adaptations, Cell Biology, and Ecosystems',
  'Grade 11 Biology strand review: students revisit desert ecosystems, bioluminescence, camouflage and mimicry, the placenta, telomeres, apoptosis, the gut-brain axis, bioremediation, and hydrothermal vent ecosystems.',
  [('What defines a desert ecosystem?', ['Very little precipitation', 'Extremely high precipitation', 'Constant freezing temperatures only', 'No sunlight at all'], 0),
   ('What is bioluminescence?', ['The production of light by living organisms through a chemical reaction', 'The absorption of light by an organism with no light produced', 'A process only found in plants', 'A type of camouflage using colour change alone'], 0),
   ('What is apoptosis?', ['A regulated, programmed process by which cells self-destruct', 'An uncontrolled process where cells burst open randomly', 'A process where cells grow uncontrollably forever', 'A type of cell division unrelated to cell death'], 0),
   ('What is bioremediation?', ['Using living organisms to break down or remove pollutants', 'A process that always increases pollution levels', 'A method of building new factories', 'A type of chemical warfare technology'], 0),
   ('What process do bacteria at hydrothermal vents use to produce energy?', ['Chemosynthesis', 'Photosynthesis, using direct sunlight', 'Cellular respiration using oxygen from the surface only', 'A process requiring constant sunlight exposure'], 0)]),
C('Chemistry Review: Bonding, Applied Chemistry, and Everyday Reactions',
  'Grade 11 Chemistry strand review: students revisit molecular orbital theory, orbital hybridization, coordination compounds, chemiluminescence, fermentation, sports drink electrolytes, perfume chemistry, lachrymatory agents, and photographic chemistry.',
  [('What does molecular orbital theory describe?', ['How atomic orbitals combine to form molecular orbitals', 'Only the shape of a single atom', 'The colour of a chemical compound', 'The temperature at which a substance boils'], 0),
   ('What does orbital hybridization describe?', ['How atomic orbitals mix to form new hybrid orbitals', 'The colour of a chemical compound', 'The temperature at which a substance freezes', 'The mass of a single atom'], 0),
   ('What is a ligand?', ['A molecule or ion that binds to a central metal ion', 'A type of acid with no metal involvement', 'A unit of temperature measurement', 'A type of radioactive particle'], 0),
   ('What is chemiluminescence?', ['The emission of light resulting from a chemical reaction', 'The absorption of light with no emission at all', 'A process that only occurs in living organisms', 'A physical change with no chemical reaction involved'], 0),
   ('What is a lachrymatory agent?', ['A volatile chemical that irritates the eyes and triggers tears', 'A compound that has no effect on the eyes', 'A solid mineral with no chemical reactivity', 'A gas used only in refrigeration'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_111_120)
    append_to(11, g11_111_120)
