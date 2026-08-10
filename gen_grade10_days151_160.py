#!/usr/bin/env python3
"""Grade 10, Days 151-160 -- extends Grade 10 from 150 to 160 days. Topics
chosen after grepping the existing Day 1-150 title list (data/grade10.json)
extensively to avoid any overlap: subordinate clauses and complex sentences,
tone shifts in poetry, the character sketch, the picaresque novel, analyzing
reality television, simple/compound/complex/compound-complex sentences,
pastoral and nature imagery, the news report and objective style, and the
verse novel; the second derivative and concavity, perfect numbers and
Mersenne primes, an introduction to the t-distribution, graph colouring and
chromatic number, vector equations of lines and planes, an introduction to
Markov chains, even and odd functions and symmetry, an introduction to
Taylor and Maclaurin series, and solving systems of nonlinear equations;
population genetics and the Hardy-Weinberg principle, thermochemistry and
enthalpy of reaction, diffraction and interference of light, the aurora
borealis and space weather, sleep and circadian rhythms, corrosion and the
electrochemistry of rusting, resonance and standing waves, mining and
mineral resource management, and pollinators and colony collapse disorder;
the Dieppe Raid of 1942, the Battle of the Atlantic, the 1942 national
plebiscite on conscription, the Italian Campaign and the Battle of Ortona,
D-Day and the Normandy Campaign, the Battle of the Scheldt, the liberation
of the Netherlands, VE Day and the end of the war in Europe, and the
Canadian Womens Army Corps, continuing the Second World War combat sequence
begun with the eve-of-war review that closed Days 141-150.

None of the thirty-six new subject titles above, nor the four Day 160
review titles, duplicate any (subject, title) pair found in Days 1-150 --
confirmed by dumping and grepping the full existing title list before
writing this script.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used anywhere
in title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-150 convention.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


def _rebalance_answer_positions(days, seed=20260809):
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


g10_151_160 = [
day(151, [
E('Grammar: Subordinate Clauses and Complex Sentences',
  'Grade 10 English strand: a subordinate clause contains a subject and a verb but cannot stand alone as a complete sentence, and when joined to an independent clause using a subordinating conjunction such as although, because, or while, it forms a complex sentence.',
  [('What is a subordinate clause?', ['A group of words with a subject and a verb that cannot stand alone as a complete sentence', 'A complete sentence that can stand alone with no other clause', 'A single word with no subject or verb', 'A punctuation mark used to separate two independent clauses'], 0),
   ('What is required to join a subordinate clause to an independent clause?', ['A subordinating conjunction such as although, because, or while', 'A comma splice with no connecting word', 'A period placed in the middle of the clause', 'A second unrelated subordinate clause with no connection'], 0),
   ('What kind of sentence is formed when a subordinate clause is joined to an independent clause?', ['A complex sentence', 'A single isolated word', 'A sentence fragment with no verb', 'A list with no grammatical structure'], 0),
   ('Which sentence contains a subordinate clause?', ['Because the storm arrived early, the game was postponed.', 'The storm arrived early.', 'The game was postponed.', 'Storm, game, postponed, early.'], 0),
   ('Why might a writer use a subordinate clause?', ['To show a relationship such as cause, time, or contrast between two ideas', 'To remove all meaning from a sentence', 'To ensure a sentence has no independent clause at all', 'To avoid using any conjunction whatsoever'], 0)]),
M('Calculus: The Second Derivative and Concavity',
  'Grade 10 Math strand: the second derivative of a function measures how the rate of change itself is changing, and its sign indicates concavity, with a positive second derivative showing the graph curves upward and a negative second derivative showing the graph curves downward.',
  [('What does the second derivative of a function measure?', ['How the rate of change of the function is itself changing', 'The exact value of the function at a single point', 'The total area under the graph of the function', 'The number of times the function crosses the x-axis'], 0),
   ('What does a positive second derivative indicate about a graph?', ['The graph is concave up, curving upward', 'The graph is concave down, curving downward', 'The graph is a perfectly straight line', 'The graph has no defined slope anywhere'], 0),
   ('What does a negative second derivative indicate about a graph?', ['The graph is concave down, curving downward', 'The graph is concave up, curving upward', 'The function has no first derivative', 'The function is undefined at every point'], 0),
   ('What is an inflection point?', ['A point where the concavity of a graph changes from up to down or down to up', 'A point where a graph reaches its highest possible value forever', 'A point where a function is never continuous', 'A point that only exists on a straight line'], 0),
   ('How is the second derivative typically calculated?', ['By taking the derivative of the first derivative', 'By multiplying the function by zero', 'By taking the square root of the original function', 'By evaluating the function at x equals zero only'], 0)]),
Sc('Biology: Population Genetics and the Hardy-Weinberg Principle',
   'Grade 10 Science strand: population genetics studies how allele and genotype frequencies change within a population, and the Hardy-Weinberg principle describes the condition under which those frequencies remain stable across generations in the absence of evolutionary forces such as mutation, migration, or selection.',
   [('What does population genetics study?', ['How allele and genotype frequencies change within a population', 'The individual behaviour of a single organism only', 'The chemical composition of nonliving rocks', 'The formation of new mountain ranges over time'], 0),
    ('What does the Hardy-Weinberg principle describe?', ['The condition under which allele frequencies remain stable across generations', 'A process that always causes rapid genetic change in every population', 'A method for building a family tree of a single organism', 'A rule that applies only to nonliving matter'], 0),
    ('Which factor would disrupt the stable condition described by the Hardy-Weinberg principle?', ['Natural selection acting on a population', 'A population remaining perfectly isolated with no change at all', 'A population with no reproduction occurring', 'A population existing in a vacuum with no organisms'], 0),
    ('What term describes the proportion of a particular allele within a population gene pool?', ['Allele frequency', 'Cellular respiration rate', 'Photosynthetic yield', 'Atomic mass'], 0),
    ('Why is the Hardy-Weinberg principle useful to biologists even though real populations rarely meet its exact conditions?', ['It provides a baseline for detecting when evolutionary forces are actually acting on a population', 'It proves that evolution never occurs in any population', 'It eliminates the need to study genetics entirely', 'It applies only to nonliving chemical systems'], 0)]),
H('The Dieppe Raid of 1942',
  'Grade 10 History strand: the Dieppe Raid was a largely Canadian amphibious assault on the German-occupied French port of Dieppe on August 19, 1942, that resulted in heavy Canadian casualties within a single day and provided costly lessons later applied to the planning of the Normandy landings.',
  [('In what year did the Dieppe Raid take place?', ['1942', '1917', '1938', '1949'], 0),
   ('Which nations troops made up the majority of the attacking force at Dieppe?', ['Canadian troops', 'American troops', 'Soviet troops', 'Australian troops'], 0),
   ('What was the outcome of the Dieppe Raid for the attacking force?', ['Heavy casualties within a single day', 'A complete and lasting capture of the port with no losses', 'An immediate German surrender', 'A peaceful withdrawal with no combat at all'], 0),
   ('What later operation is often said to have benefited from lessons learned at Dieppe?', ['The Normandy landings', 'The Battle of Vimy Ridge', 'The Klondike Gold Rush', 'The Suez Crisis'], 0),
   ('What type of military operation was the Dieppe Raid?', ['An amphibious assault launched from the sea', 'A purely aerial bombing campaign with no ground troops', 'A diplomatic negotiation with no combat', 'A naval blockade with no landing force'], 0)]),
]),
day(152, [
E('Reading: Analyzing Tone Shifts in Poetry',
  'Grade 10 English strand: tone is the attitude a speaker or writer conveys toward a subject, and a tone shift occurs when that attitude changes within a poem, often signalled by changes in diction, imagery, punctuation, or line structure.',
  [('What is tone in a poem?', ['The attitude a speaker or writer conveys toward a subject', 'The exact number of lines contained in a poem', 'The physical size of the printed page', 'The publication date of a poem'], 0),
   ('What is a tone shift?', ['A change in the attitude conveyed within a poem', 'A change in the font used to print a poem', 'A change in the title of an unrelated poem', 'A change in the authors legal name'], 0),
   ('Which element might signal a tone shift in a poem?', ['A noticeable change in diction, imagery, or punctuation', 'The total page count of the book containing the poem', 'The colour of the book cover', 'The price listed on the back of the book'], 0),
   ('Why might a poet include a tone shift?', ['To reflect a change in emotion, perspective, or realization within the poem', 'To ensure the poem has no emotional content at all', 'To make the poem impossible to read aloud', 'To remove all imagery from the poem entirely'], 0),
   ('Where in a poem might a tone shift most often be noticed?', ['At a stanza break or turning point in the poems argument or narrative', 'Only in the title of the poem', 'Only in the name of the publisher', 'Only in a footnote unrelated to the poem'], 0)]),
M('Number Theory: Perfect Numbers and Mersenne Primes',
  'Grade 10 Math strand: a perfect number is a positive integer that equals the sum of its proper divisors, such as 6, which equals 1 plus 2 plus 3, and every known even perfect number is closely linked to a Mersenne prime through the Euclid-Euler theorem.',
  [('What is a perfect number?', ['A positive integer that equals the sum of its proper divisors', 'Any integer that is divisible by exactly two numbers', 'A number that has no divisors other than itself', 'A number that is always negative'], 0),
   ('Which of the following is an example of a perfect number?', ['6, since 1 plus 2 plus 3 equals 6', '10, since its divisors do not sum to 10', '7, since it has only two divisors', '15, since its divisors do not sum to 15'], 0),
   ('What theorem links even perfect numbers to Mersenne primes?', ['The Euclid-Euler theorem', 'The Pythagorean Theorem', 'The Fundamental Theorem of Algebra', 'The Chinese Remainder Theorem'], 0),
   ('What is a Mersenne prime?', ['A prime number that is one less than a power of two', 'A number that is always even and never prime', 'A number with no divisors of any kind', 'A number equal to the sum of its multiples'], 0),
   ('Why are perfect numbers still of interest to mathematicians today?', ['It remains unknown whether any odd perfect number exists', 'Every property of perfect numbers has been completely solved with no open questions', 'Perfect numbers have no connection to any other area of number theory', 'Perfect numbers are no longer studied in modern mathematics'], 0)]),
Sc('Chemistry: Thermochemistry and Enthalpy of Reaction',
   'Grade 10 Science strand: thermochemistry studies the heat energy absorbed or released during a chemical reaction, measured as the enthalpy of reaction, with exothermic reactions releasing heat to the surroundings and endothermic reactions absorbing heat from the surroundings.',
   [('What does thermochemistry study?', ['The heat energy absorbed or released during a chemical reaction', 'The colour changes that occur in a solution', 'The speed at which a solid dissolves in water', 'The electrical conductivity of a metal wire'], 0),
    ('What term describes the heat energy change during a reaction?', ['The enthalpy of reaction', 'The atomic number', 'The molar mass', 'The pH value'], 0),
    ('What happens during an exothermic reaction?', ['Heat is released to the surroundings', 'Heat is absorbed from the surroundings', 'No energy change occurs at all', 'Light is absorbed but no heat is involved'], 0),
    ('What happens during an endothermic reaction?', ['Heat is absorbed from the surroundings', 'Heat is released to the surroundings', 'The reaction produces no chemical change', 'The temperature of the surroundings always rises'], 0),
    ('Which everyday example illustrates an exothermic reaction?', ['Burning wood in a campfire', 'Melting an ice cube at room temperature', 'Dissolving a cold pack that draws in heat', 'Evaporating water on a cool day'], 0)]),
H('The Battle of the Atlantic',
  'Grade 10 History strand: the Battle of the Atlantic was the longest continuous military campaign of the Second World War, lasting from 1939 to 1945, in which the Royal Canadian Navy played a major role escorting merchant convoys across the ocean while defending them from German submarine attacks.',
  [('What was the Battle of the Atlantic?', ['The longest continuous military campaign of the Second World War, fought largely over merchant shipping', 'A single one-day naval battle fought near Halifax', 'A land battle fought entirely within continental Europe', 'A diplomatic conference held in a neutral country'], 0),
   ('From what years did the Battle of the Atlantic last?', ['1939 to 1945', '1914 to 1918', '1929 to 1933', '1950 to 1953'], 0),
   ('What role did the Royal Canadian Navy play in the Battle of the Atlantic?', ['Escorting merchant convoys across the ocean and defending them from attack', 'Refusing to participate in any naval operations', 'Serving only as a training fleet with no combat role', 'Operating exclusively in the Pacific Ocean'], 0),
   ('What was the main threat to Allied convoys during the Battle of the Atlantic?', ['German submarine attacks', 'Volcanic eruptions along shipping routes', 'Piracy from unrelated nations', 'Severe drought affecting ocean levels'], 0),
   ('Why was the Battle of the Atlantic strategically important to the Allied war effort?', ['It protected the supply lines of food, fuel, and troops needed to sustain the war in Europe', 'It had no connection to any other theatre of the war', 'It was fought entirely for symbolic reasons with no material stakes', 'It focused only on capturing uninhabited islands'], 0)]),
]),
day(153, [
E('Writing: The Character Sketch',
  'Grade 10 English strand: a character sketch is a short piece of writing that vividly portrays a characters physical appearance, personality traits, and motivations without necessarily including a complete plot, allowing a writer to practise close observation and descriptive detail.',
  [('What is a character sketch?', ['A short piece of writing that vividly portrays a characters appearance, personality, and motivations', 'A full-length novel with multiple complete subplots', 'A formal legal document describing a real person', 'A diagram showing the setting of a story with no characters'], 0),
   ('Does a character sketch typically require a complete plot?', ['No, it can focus purely on describing a character without a full plot', 'Yes, it must always contain a beginning, middle, and end', 'Yes, it must include several unrelated subplots', 'No, it must contain no descriptive detail whatsoever'], 0),
   ('What skill does writing a character sketch help a writer practise?', ['Close observation and descriptive detail', 'Solving mathematical equations', 'Memorizing historical dates', 'Designing a scientific experiment'], 0),
   ('Which detail would most likely appear in a character sketch?', ['A description of the characters habitual gestures and manner of speaking', 'A list of unrelated chemical formulas', 'A schedule of upcoming sporting events', 'A table of stock market prices'], 0),
   ('Why might a character sketch be useful before writing a longer story?', ['It helps a writer develop a clear, consistent sense of a character before placing them in a plot', 'It removes any need to ever think about character again', 'It guarantees the story will have no conflict', 'It replaces the need for any dialogue in the final story'], 0)]),
M('Statistics: An Introduction to the t-Distribution',
  'Grade 10 Math strand: the t-distribution is a probability distribution used when working with small sample sizes and an unknown population standard deviation, resembling the normal distribution but with heavier tails that account for the added uncertainty of a smaller sample.',
  [('When is the t-distribution typically used instead of the normal distribution?', ['When working with a small sample size and an unknown population standard deviation', 'When the entire population has already been measured exactly', 'When no data has been collected at all', 'When a distribution has no variability whatsoever'], 0),
   ('How does the shape of the t-distribution compare to the normal distribution?', ['It has heavier tails to account for added uncertainty from a smaller sample', 'It has no tails at all', 'It is always identical to the normal distribution in every case', 'It has a shape that cannot be graphed'], 0),
   ('What happens to the t-distribution as sample size increases?', ['It becomes increasingly similar to the normal distribution', 'It becomes increasingly different from the normal distribution', 'It disappears entirely once a sample is collected', 'It always becomes perfectly flat with no peak'], 0),
   ('What is degrees of freedom most closely related to when using the t-distribution?', ['The sample size used in the calculation', 'The colour of the graph produced', 'The location where data was collected', 'The name of the researcher conducting the study'], 0),
   ('In what type of study might a researcher rely on the t-distribution?', ['A study with a small sample where the population standard deviation is not known', 'A census that measures every member of an entire population', 'A study involving no numerical data at all', 'A purely qualitative interview with no statistics involved'], 0)]),
Sc('Physics: Diffraction and Interference of Light',
   'Grade 10 Science strand: diffraction is the bending of light waves as they pass around an obstacle or through a narrow opening, and interference occurs when two or more light waves overlap, combining constructively to increase brightness or destructively to reduce it.',
   [('What is diffraction?', ['The bending of light waves as they pass around an obstacle or through a narrow opening', 'The complete absorption of light by a solid object', 'The reflection of light directly back toward its source', 'The conversion of light into sound energy'], 0),
    ('What is interference in the context of light waves?', ['The combination of two or more overlapping light waves', 'The complete disappearance of a light wave with no cause', 'A single light wave travelling in a straight line with no other waves present', 'The conversion of light into heat with no wave behaviour involved'], 0),
    ('What is constructive interference?', ['When overlapping waves combine to increase brightness', 'When overlapping waves combine to eliminate all light entirely', 'When a single wave splits into two unrelated colours', 'When light waves refuse to interact with one another'], 0),
    ('What is destructive interference?', ['When overlapping waves combine to reduce brightness', 'When overlapping waves combine to increase brightness beyond any limit', 'When a wave travels through a vacuum with no medium', 'When two waves always produce identical results to constructive interference'], 0),
    ('What everyday phenomenon demonstrates diffraction and interference of light?', ['The pattern of colours seen on the surface of a soap bubble', 'The steady glow of a light bulb filament', 'The straight shadow cast by a solid wall on a sunny day', 'The heating of a metal surface left in direct sunlight'], 0)]),
H('The 1942 National Plebiscite on Conscription',
  'Grade 10 History strand: in 1942, Prime Minister Mackenzie King held a national plebiscite asking Canadians to release his government from its earlier promise not to introduce overseas conscription, resulting in a majority yes vote nationally but strong opposition in Quebec, deepening tensions over wartime policy.',
  [('In what year was the national plebiscite on conscription held?', ['1942', '1917', '1938', '1949'], 0),
   ('What was the plebiscite asking Canadians to release the government from?', ['An earlier promise not to introduce overseas conscription', 'A promise to lower income taxes', 'A promise to build a new national railway', 'A promise to join a new international alliance'], 0),
   ('Which prime minister held the 1942 plebiscite?', ['Mackenzie King', 'Robert Borden', 'Lester Pearson', 'Wilfrid Laurier'], 0),
   ('What was the overall national result of the plebiscite?', ['A majority voted yes to releasing the government from its promise', 'A majority voted no across every region of the country', 'The vote ended in an exact national tie', 'The plebiscite was cancelled before any votes were counted'], 0),
   ('How did voters in Quebec generally respond to the plebiscite?', ['A strong majority voted no, opposing the release from the promise', 'A strong majority voted yes, matching the national result exactly', 'Quebec was excluded entirely from voting', 'Quebec recorded the highest yes vote of any province'], 0)]),
]),
day(154, [
E('Literature: The Picaresque Novel',
  'Grade 10 English strand: a picaresque novel is an episodic narrative that follows a resourceful, low-born hero known as a picaro through a loosely connected series of adventures, often using humour and social observation to satirize the customs of the society the picaro travels through.',
  [('What type of hero does a picaresque novel typically follow?', ['A resourceful, low-born hero known as a picaro', 'A powerful monarch ruling over a vast empire', 'A retired scientist working alone in a laboratory', 'A committee of unnamed government officials'], 0),
   ('How is the plot of a picaresque novel typically structured?', ['As a loosely connected series of episodic adventures', 'As a single tightly plotted event with no digressions', 'As a strict step-by-step scientific procedure', 'As a formal legal argument with numbered clauses'], 0),
   ('What literary purpose does a picaresque novel often serve?', ['Satirizing the customs and social classes of the society the picaro travels through', 'Providing a technical manual with no narrative content', 'Recording precise historical statistics with no characters', 'Avoiding any commentary on society whatsoever'], 0),
   ('What tone does a picaresque novel often adopt?', ['A humorous and observational tone', 'A strictly formal legal tone', 'A tone with no emotional or descriptive content', 'A tone limited entirely to scientific terminology'], 0),
   ('Why might a picaresque novel use a low-born protagonist rather than a noble one?', ['A low-born wanderer can move freely across social classes, offering a wide view of society', 'A low-born character cannot appear in any story according to literary convention', 'A low-born protagonist eliminates the possibility of humour', 'A low-born protagonist prevents any social commentary from appearing'], 0)]),
M('Discrete Math: Graph Colouring and Chromatic Number',
  'Grade 10 Math strand: graph colouring assigns a colour to each vertex of a graph so that no two adjacent vertices share the same colour, and the chromatic number of a graph is the smallest number of colours needed to achieve this, with applications such as scheduling and map colouring.',
  [('What does graph colouring assign to each vertex of a graph?', ['A colour, so that no two adjacent vertices share the same colour', 'A random number with no rule attached', 'A fixed weight equal to the number of edges', 'A name matching an unrelated historical figure'], 0),
   ('What is the chromatic number of a graph?', ['The smallest number of colours needed so no two adjacent vertices share a colour', 'The total number of vertices in the graph', 'The total number of edges in the graph', 'The largest possible number of colours that could ever be used'], 0),
   ('Why must adjacent vertices receive different colours in a proper graph colouring?', ['To ensure that connected vertices can be distinguished from one another', 'Because graph colouring requires every vertex to be identical', 'Because adjacent vertices are not allowed to exist in a graph', 'Because colour has no meaningful role in graph theory'], 0),
   ('Which real-world problem can be modelled using graph colouring?', ['Scheduling exams so that no student has two exams at the same time', 'Measuring the exact temperature of a room', 'Calculating the volume of a three-dimensional solid', 'Finding the derivative of a polynomial function'], 0),
   ('How is graph colouring connected to map colouring problems?', ['Regions on a map can be represented as vertices, with shared borders as edges requiring different colours', 'Maps have no connection to graph theory of any kind', 'Map colouring requires an infinite number of colours for any map', 'Graph colouring can only apply to perfectly straight lines'], 0)]),
Sc('Earth Science: The Aurora Borealis and Space Weather',
   'Grade 10 Science strand: the aurora borealis, or northern lights, occurs when charged particles from the sun interact with gases in Earths upper atmosphere near the magnetic poles, a visible effect of space weather driven by solar activity such as solar flares and coronal mass ejections.',
   [('What causes the aurora borealis?', ['Charged particles from the sun interacting with gases in Earths upper atmosphere', 'Reflections of city lights bouncing off low clouds', 'A chemical reaction occurring entirely within the ocean', 'A permanent feature unrelated to solar activity'], 0),
    ('Near what part of Earth is the aurora borealis most commonly visible?', ['Near the magnetic poles', 'Near the equator only', 'Only over large bodies of fresh water', 'Only in desert regions'], 0),
    ('What term describes the broader field of solar-driven effects on Earths space environment?', ['Space weather', 'Ocean acidification', 'Plate tectonics', 'The rock cycle'], 0),
    ('Which solar event is closely linked to increased auroral activity?', ['A coronal mass ejection or solar flare', 'A lunar eclipse', 'A meteor shower unrelated to the sun', 'A change in ocean tides'], 0),
    ('Why can strong space weather events pose risks to modern technology?', ['They can disrupt satellites, power grids, and radio communication', 'They have no measurable effect on any technology', 'They only affect technology located underground', 'They exclusively affect handwritten paper records'], 0)]),
H('The Italian Campaign and the Battle of Ortona',
  'Grade 10 History strand: Canadian troops fought in the Italian Campaign from 1943 to 1945, including the brutal house-to-house fighting of the Battle of Ortona in December 1943, an intense urban battle that became one of the wars most difficult engagements for Canadian forces.',
  [('From what years did Canadian troops fight in the Italian Campaign?', ['1943 to 1945', '1914 to 1918', '1929 to 1933', '1950 to 1953'], 0),
   ('What made the Battle of Ortona especially difficult for Canadian troops?', ['Brutal house-to-house urban fighting', 'A battle fought entirely at sea with no ground troops', 'A negotiation conducted with no combat at all', 'An uncontested advance with no enemy resistance'], 0),
   ('In what month and year did the Battle of Ortona take place?', ['December 1943', 'August 1942', 'June 1944', 'May 1945'], 0),
   ('What type of combat characterized the fighting at Ortona?', ['Close-quarters combat within a densely built town', 'Long-range naval artillery exchanges only', 'Aerial dogfights with no ground engagement', 'Diplomatic negotiations between generals'], 0),
   ('Why is the Italian Campaign significant to the study of Canadian military history?', ['It demonstrated the endurance of Canadian forces in prolonged and difficult combat conditions', 'It involved no Canadian participation of any kind', 'It ended before any fighting actually occurred', 'It had no connection to the broader Second World War'], 0)]),
]),
day(155, [
E('Media Literacy: Analyzing Reality Television',
  'Grade 10 English strand: reality television presents seemingly unscripted footage of real people in constructed situations, edited and structured by producers to build narrative tension, conflict, and character arcs for entertainment rather than to provide an unfiltered record of events.',
  [('What does reality television present to viewers?', ['Seemingly unscripted footage of real people in constructed situations', 'Fully scripted dialogue performed by professional actors only', 'A live unedited broadcast with no post-production of any kind', 'A purely animated program with no real participants'], 0),
   ('What role do producers typically play in shaping reality television?', ['They edit and structure footage to build narrative tension and conflict', 'They have no involvement in the final broadcast whatsoever', 'They appear on screen as the only visible participants', 'They eliminate all editing from the final program'], 0),
   ('Why might reality television not provide an unfiltered record of events?', ['Because editing choices shape which moments are shown and how they are framed', 'Because reality television is always broadcast completely live with no editing', 'Because participants are never aware they are being filmed', 'Because reality television contains no editing decisions at all'], 0),
   ('What is a common narrative technique used in reality television editing?', ['Building a character arc or storyline through selective editing across episodes', 'Removing every participant from the final broadcast', 'Presenting footage in a random order with no structure', 'Avoiding any depiction of conflict whatsoever'], 0),
   ('Why is media literacy useful when watching reality television?', ['It helps viewers recognize the constructed and edited nature of what appears to be unscripted content', 'It guarantees that reality television contains no editing of any kind', 'It removes any need to think critically about televised content', 'It proves that reality television is always a fully accurate record'], 0)]),
M('Vectors: Vector Equations of Lines and Planes',
  'Grade 10 Math strand: a line in space can be described using a vector equation built from a known point and a direction vector, while a plane can be described using a known point and a normal vector, extending vector concepts to represent geometric objects algebraically.',
  [('What two pieces of information define the vector equation of a line?', ['A known point on the line and a direction vector', 'Only the length of the line with no other information', 'The colour used to draw the line on a graph', 'The name of the mathematician who first drew the line'], 0),
   ('What two pieces of information define the vector equation of a plane?', ['A known point on the plane and a normal vector', 'Only the area of the plane with no other information', 'The temperature of the room where the plane is drawn', 'A single unrelated scalar with no direction'], 0),
   ('What does a normal vector to a plane represent?', ['A vector that is perpendicular to every line lying within the plane', 'A vector that lies flat within the plane itself', 'A vector with no defined direction', 'A vector that changes length depending on where it is measured'], 0),
   ('What does a direction vector for a line indicate?', ['The direction in which the line extends through space', 'The exact colour of the line', 'The total number of points on the line', 'The name of the plane containing the line'], 0),
   ('Why are vector equations useful for describing lines and planes?', ['They allow geometric objects in space to be represented and manipulated algebraically', 'They eliminate the need to ever graph a line or plane', 'They can only describe objects in exactly two dimensions', 'They have no connection to points or directions at all'], 0)]),
Sc('Biology: Sleep and Circadian Rhythms',
   'Grade 10 Science strand: circadian rhythms are roughly twenty-four-hour internal cycles that regulate sleep and wakefulness, influenced by external cues such as light and darkness, and coordinated by a region of the brain that helps synchronize bodily processes with the day-night cycle.',
   [('What is a circadian rhythm?', ['A roughly twenty-four-hour internal cycle that regulates sleep and wakefulness', 'A random pattern of behaviour with no regular timing', 'A cycle that repeats exactly once per year', 'A pattern found only in plants, never in animals'], 0),
    ('What external cue most strongly influences the circadian rhythm?', ['Light and darkness', 'Air pressure changes', 'Ocean tide patterns', 'Background noise levels'], 0),
    ('What role does the brain play in circadian rhythms?', ['A specific brain region helps synchronize bodily processes with the day-night cycle', 'The brain has no role in regulating sleep at all', 'The brain only regulates digestion, not sleep patterns', 'The brain prevents any internal cycle from forming'], 0),
    ('What might happen if a persons circadian rhythm is disrupted, such as by shift work or long-distance travel?', ['Sleep quality and alertness can be negatively affected', 'The persons height will permanently change', 'Circadian disruption has no effect on the body whatsoever', 'The persons eye colour will change over time'], 0),
    ('Why do circadian rhythms continue even in the absence of external light cues?', ['They are driven by an internal biological clock that persists even without external timing signals', 'They stop functioning completely without any light present', 'They are entirely created by external light with no internal component', 'They only exist in organisms that never sleep'], 0)]),
H('D-Day and the Normandy Campaign, 1944',
  'Grade 10 History strand: on June 6, 1944, Allied forces launched the D-Day invasion of Normandy, with Canadian troops landing at Juno Beach as part of the assault, beginning a campaign that pushed German forces out of France over the following months.',
  [('On what date did the D-Day invasion of Normandy begin?', ['June 6, 1944', 'August 19, 1942', 'December 1943', 'May 8, 1945'], 0),
   ('At which beach did Canadian troops land during the D-Day invasion?', ['Juno Beach', 'Omaha Beach', 'Utah Beach', 'Sword Beach'], 0),
   ('What broader military action did D-Day begin?', ['The Normandy Campaign to push German forces out of France', 'A purely naval blockade with no ground invasion', 'A diplomatic conference with no military action', 'A withdrawal of all Allied troops from Europe'], 0),
   ('What type of military operation was the D-Day landing?', ['A large-scale amphibious invasion', 'A purely underground tunnel assault', 'A single-pilot reconnaissance flight', 'A negotiation carried out entirely by letter'], 0),
   ('Why is D-Day considered a major turning point in the Second World War in Europe?', ['It established a major Allied foothold in western Europe that led to the liberation of France', 'It ended the war immediately with no further fighting', 'It had no lasting effect on the outcome of the war', 'It occurred entirely outside of the European theatre'], 0)]),
]),
day(156, [
E('Grammar: Simple, Compound, Complex, and Compound-Complex Sentences',
  'Grade 10 English strand: sentences can be classified by structure as simple, containing one independent clause; compound, containing two or more independent clauses; complex, containing an independent clause and at least one subordinate clause; or compound-complex, combining both features.',
  [('What defines a simple sentence?', ['It contains exactly one independent clause', 'It contains no subject or verb at all', 'It always contains at least three independent clauses', 'It can never contain any punctuation'], 0),
   ('What defines a compound sentence?', ['It contains two or more independent clauses joined together', 'It contains only a single word with no clause', 'It always ends without any punctuation', 'It can never be joined by a conjunction'], 0),
   ('What defines a complex sentence?', ['It contains an independent clause and at least one subordinate clause', 'It contains no independent clause of any kind', 'It always contains exactly two subordinate clauses and no independent clause', 'It can never include a subordinating conjunction'], 0),
   ('What defines a compound-complex sentence?', ['It combines two or more independent clauses with at least one subordinate clause', 'It contains exactly one word with no clause structure', 'It can never contain more than one clause', 'It excludes all independent clauses entirely'], 0),
   ('Why is understanding these four sentence types useful for a writer?', ['It allows a writer to vary sentence structure deliberately for clarity and effect', 'It guarantees that a writer will never make a grammatical error', 'It eliminates any need to ever use punctuation', 'It prevents a writer from ever combining two ideas'], 0)]),
M('Probability: An Introduction to Markov Chains',
  'Grade 10 Math strand: a Markov chain models a sequence of events in which the probability of moving to the next state depends only on the current state, not on the sequence of events that preceded it, a property known as memorylessness.',
  [('What does a Markov chain model?', ['A sequence of events where the probability of the next state depends only on the current state', 'A sequence where every future event is completely fixed with no randomness', 'A sequence where each event depends on every prior event in full detail', 'A single isolated event with no sequence involved'], 0),
   ('What property describes the defining feature of a Markov chain?', ['Memorylessness, since only the current state matters for predicting the next', 'Infinite memory of every past event in the sequence', 'Complete independence from any current state', 'A guarantee that no transition between states can ever occur'], 0),
   ('What is a state in the context of a Markov chain?', ['A possible condition or position the system can occupy at a given step', 'A fixed numerical constant with no connection to probability', 'The exact time of day an event occurs', 'The name of the person analyzing the chain'], 0),
   ('What term describes the probability of moving from one state to another in a Markov chain?', ['A transition probability', 'A derivative', 'A determinant', 'An asymptote'], 0),
   ('Which real-world scenario could be modelled using a Markov chain?', ['Predicting tomorrows weather condition based only on todays weather condition', 'Calculating the exact area of a triangle', 'Measuring the length of a fixed physical object', 'Finding the slope of a straight line between two points'], 0)]),
Sc('Chemistry: Corrosion and the Electrochemistry of Rusting',
   'Grade 10 Science strand: corrosion is the gradual deterioration of a metal caused by chemical reactions with its environment, and rusting is a common form of corrosion in which iron reacts with oxygen and water through an electrochemical process to form hydrated iron oxide.',
   [('What is corrosion?', ['The gradual deterioration of a metal caused by chemical reactions with its environment', 'The instant destruction of a metal with no chemical process involved', 'A process that only affects nonmetal materials', 'A permanent and unchangeable property of every metal'], 0),
    ('What is rusting a common example of?', ['Corrosion', 'Combustion', 'Distillation', 'Sublimation'], 0),
    ('Which two substances does iron react with to form rust?', ['Oxygen and water', 'Nitrogen and helium', 'Only pure hydrogen gas', 'Only solid carbon'], 0),
    ('What type of process underlies the formation of rust?', ['An electrochemical process', 'A purely mechanical process with no chemical change', 'A nuclear process involving atomic fission', 'A process that occurs only at extremely low temperatures'], 0),
    ('Why might coating a metal surface with paint or oil help prevent rusting?', ['It blocks direct contact between the metal and oxygen or water', 'It permanently changes the metal into a different element', 'It has no effect on the rate of corrosion whatsoever', 'It increases the rate at which the metal reacts with oxygen'], 0)]),
H('The Battle of the Scheldt, 1944',
  'Grade 10 History strand: the Battle of the Scheldt was a series of difficult operations in the fall of 1944 in which the First Canadian Army fought to clear the Scheldt Estuary of German forces, a campaign essential to opening the port of Antwerp for vital Allied supply shipments.',
  [('In what year did the Battle of the Scheldt take place?', ['1944', '1917', '1938', '1949'], 0),
   ('Which army led the effort to clear the Scheldt Estuary?', ['The First Canadian Army', 'The United States Marine Corps', 'The Soviet Red Army', 'The Royal Australian Navy'], 0),
   ('What geographic feature did Allied forces need to clear of German troops during this battle?', ['The Scheldt Estuary', 'The Rocky Mountains', 'The Great Lakes', 'The Prairie grasslands'], 0),
   ('What port did clearing the Scheldt Estuary allow the Allies to use?', ['The port of Antwerp', 'The port of Halifax', 'The port of Vancouver', 'The port of Liverpool'], 0),
   ('Why was opening the port important to the Allied war effort in late 1944?', ['It provided a vital route for delivering supplies closer to the front lines in western Europe', 'It had no strategic value to the Allied campaign', 'It was used exclusively for civilian tourism', 'It ended all fighting in the region immediately'], 0)]),
]),
day(157, [
E('Reading: Analyzing Pastoral and Nature Imagery',
  'Grade 10 English strand: pastoral literature idealizes rural life and the natural world, often using vivid nature imagery to contrast the simplicity of the countryside with the complexity or corruption of urban or courtly life, inviting reflection on humanitys relationship with nature.',
  [('What does pastoral literature typically idealize?', ['Rural life and the natural world', 'The complexity of urban courtly politics', 'The mechanics of industrial factories', 'The structure of a modern legal system'], 0),
   ('What contrast does pastoral literature often draw?', ['A contrast between the simplicity of the countryside and the complexity of urban or courtly life', 'A contrast between two unrelated mathematical formulas', 'A contrast between two identical settings with no differences', 'A contrast between silence and complete darkness only'], 0),
   ('What literary device is central to pastoral writing?', ['Vivid nature imagery', 'Strictly technical scientific vocabulary', 'Legal terminology with no descriptive language', 'A complete absence of any descriptive detail'], 0),
   ('What deeper theme might pastoral literature invite readers to reflect on?', ['Humanitys relationship with the natural world', 'The precise mechanics of a combustion engine', 'The history of international trade tariffs', 'The rules of a formal courtroom procedure'], 0),
   ('Which image would most likely appear in a pastoral poem?', ['A shepherd resting beneath a tree in a quiet meadow', 'A crowded stock exchange trading floor', 'A busy highway interchange at rush hour', 'A server room filled with computer equipment'], 0)]),
M('Functions: Even and Odd Functions and Symmetry',
  'Grade 10 Math strand: an even function is symmetric about the y-axis and satisfies f(-x) equals f(x), while an odd function is symmetric about the origin and satisfies f(-x) equals negative f(x), with many functions being neither even nor odd.',
  [('What condition defines an even function?', ['f(-x) equals f(x) for every x in the domain', 'f(-x) always equals zero for every x', 'f(x) is always a negative number', 'f(x) has no defined domain at all'], 0),
   ('What condition defines an odd function?', ['f(-x) equals negative f(x) for every x in the domain', 'f(-x) always equals f(x) for every x', 'f(x) is undefined for all values of x', 'f(x) must always be a whole number'], 0),
   ('What type of symmetry does an even function display?', ['Symmetry about the y-axis', 'Symmetry about the x-axis only', 'No symmetry of any kind', 'Symmetry about a single fixed point unrelated to the origin'], 0),
   ('What type of symmetry does an odd function display?', ['Symmetry about the origin', 'Symmetry about the y-axis only', 'Symmetry about a horizontal line above the graph', 'No symmetry that can ever be identified'], 0),
   ('Is every function either even or odd?', ['No, many functions are neither even nor odd', 'Yes, every possible function must be either even or odd', 'Yes, but only functions with a single term', 'No, because even and odd functions cannot exist mathematically'], 0)]),
Sc('Physics: Resonance and Standing Waves',
   'Grade 10 Science strand: resonance occurs when an object or system is driven at its natural frequency, causing a dramatic increase in the amplitude of vibration, a phenomenon closely related to standing waves, which form when two waves of the same frequency travel in opposite directions and interfere to create fixed points of no displacement.',
   [('What is resonance?', ['A dramatic increase in vibration amplitude that occurs when a system is driven at its natural frequency', 'A permanent reduction of vibration to exactly zero', 'A process that only occurs in complete silence', 'A phenomenon unrelated to frequency of any kind'], 0),
    ('What is a standing wave?', ['A wave pattern formed when two waves of the same frequency travelling in opposite directions interfere', 'A wave that travels only in a single fixed direction with no interference', 'A wave that exists without any frequency at all', 'A wave found only in solid objects, never in air or water'], 0),
    ('What are the fixed points of no displacement in a standing wave called?', ['Nodes', 'Crests', 'Troughs', 'Wavelengths'], 0),
    ('What happens to a systems vibration amplitude at resonance?', ['It increases dramatically', 'It decreases to exactly zero permanently', 'It remains completely unchanged in every case', 'It becomes impossible to measure'], 0),
    ('Which everyday example demonstrates resonance?', ['A singer shattering a glass by matching its natural frequency', 'A book resting motionless on a table', 'A cold object placed in a warm room', 'A stationary rock sitting in a field'], 0)]),
H('The Liberation of the Netherlands, 1945',
  'Grade 10 History strand: in the final months of the Second World War in early 1945, Canadian troops played a leading role in liberating the Netherlands from German occupation, an effort that relieved widespread famine and forged a lasting bond of friendship between Canada and the Dutch people.',
  [('In what year did the liberation of the Netherlands largely occur?', ['1945', '1917', '1938', '1949'], 0),
   ('Which countrys troops played a leading role in liberating the Netherlands?', ['Canada', 'Australia', 'Brazil', 'Japan'], 0),
   ('What humanitarian crisis in the Netherlands was relieved by the liberation?', ['Widespread famine', 'A major earthquake', 'A severe drought lasting a decade', 'A large-scale volcanic eruption'], 0),
   ('What lasting bond did the liberation help forge between Canada and the Netherlands?', ['A lasting friendship between the two countries', 'A permanent military rivalry', 'A trade embargo lasting several decades', 'A complete severing of all diplomatic contact'], 0),
   ('During what broader period of the war did the liberation of the Netherlands take place?', ['The final months of the war in Europe', 'The opening days of the war in 1939', 'The interwar period before the war began', 'A period entirely after the wars conclusion'], 0)]),
]),
day(158, [
E('Writing: The News Report and Objective Style',
  'Grade 10 English strand: a news report presents factual information in an objective style, typically structured as an inverted pyramid that answers who, what, when, where, and why in the opening lines, avoiding personal opinion and relying on verified sources.',
  [('What style is a news report expected to use?', ['An objective style that avoids personal opinion', 'A style filled entirely with the writers personal feelings', 'A purely fictional and imaginative style', 'A style with no factual content at all'], 0),
   ('What structure is commonly used to organize a news report?', ['The inverted pyramid, placing the most important information first', 'A structure that saves the most important information for the very last line', 'A structure with no clear order of information', 'A structure based entirely on rhyme and meter'], 0),
   ('Which questions does the opening of a news report typically answer?', ['Who, what, when, where, and why', 'Only the writers personal opinion of the event', 'Only unrelated historical background with no current event', 'Only a list of unrelated statistics with no context'], 0),
   ('Why does a news report rely on verified sources?', ['To ensure the reported information is accurate and trustworthy', 'Because verified sources are never necessary in journalism', 'To ensure the report contains no factual content', 'Because a report with no sources is always more reliable'], 0),
   ('What should a news report generally avoid including?', ['The reporters personal opinion about the event', 'A clear statement of who was involved in the event', 'The location where the event occurred', 'The approximate time the event took place'], 0)]),
M('Calculus: An Introduction to Taylor and Maclaurin Series',
  'Grade 10 Math strand: a Taylor series represents a function as an infinite sum of terms calculated from the values of its derivatives at a single point, and a Maclaurin series is the special case of a Taylor series centred at zero.',
  [('What does a Taylor series represent a function as?', ['An infinite sum of terms calculated from the functions derivatives at a single point', 'A single finite value with no additional terms', 'A graph with no algebraic expression attached', 'A random sequence with no relationship to the original function'], 0),
   ('What is a Maclaurin series?', ['A special case of a Taylor series centred at zero', 'A series that can only be centred at a nonzero point', 'A series unrelated to derivatives of any kind', 'A series that only applies to whole numbers'], 0),
   ('What mathematical objects are used to build the terms of a Taylor series?', ['Derivatives of the function evaluated at the chosen centre point', 'Only the original function value with no derivatives involved', 'Randomly chosen constants with no connection to the function', 'The area under a completely unrelated curve'], 0),
   ('Why might a Taylor series be useful for approximating a function?', ['It can approximate complicated functions using a sum of simpler polynomial terms', 'It always produces an answer with no relationship to the original function', 'It eliminates the need to ever evaluate a function at any point', 'It only works for functions with no derivatives'], 0),
   ('What happens to the approximation of a Taylor series as more terms are included?', ['It generally becomes a more accurate approximation of the original function near the centre point', 'It always becomes less accurate no matter how many terms are added', 'It becomes completely unrelated to the original function', 'It stops being defined after exactly two terms'], 0)]),
Sc('Earth Science: Mining and Mineral Resource Management',
   'Grade 10 Science strand: mineral resource management involves extracting valuable minerals from the earth through mining while balancing economic benefits against environmental impacts such as habitat disturbance, water contamination, and land reclamation needs after a mine closes.',
   [('What does mineral resource management primarily involve?', ['Extracting valuable minerals while balancing economic benefit against environmental impact', 'Extracting minerals with no consideration of environmental effects at all', 'Preventing any mineral extraction from occurring anywhere', 'Studying minerals only after they have been fully depleted'], 0),
    ('Which of the following is a potential environmental impact of mining?', ['Habitat disturbance and water contamination', 'A guaranteed improvement in local water quality', 'The complete elimination of all environmental risk', 'An automatic increase in biodiversity near the mine site'], 0),
    ('What term describes restoring land to a usable or natural state after a mine closes?', ['Land reclamation', 'Sedimentation', 'Crystallization', 'Precipitation'], 0),
    ('Why is mineral resource management important to modern economies?', ['Many technologies and industries depend on minerals extracted through mining', 'No modern technology requires any mineral resources', 'Mining has no economic value in any country', 'Mineral resources are considered entirely renewable with no limits'], 0),
    ('Which practice would be considered part of responsible mineral resource management?', ['Monitoring and reducing water contamination near a mine site', 'Ignoring all environmental regulations during extraction', 'Abandoning a mine site with no plan for land reclamation', 'Extracting minerals with no regard for long-term supply'], 0)]),
H('VE Day and the End of the War in Europe',
  'Grade 10 History strand: VE Day, or Victory in Europe Day, on May 8, 1945, marked the formal end of fighting in Europe after Germanys surrender, prompting widespread celebrations across Canada and recognition of the enormous contributions and sacrifices made by Canadian forces throughout the war.',
  [('What does VE Day stand for?', ['Victory in Europe Day', 'Victory in Egypt Day', 'Veterans Enlistment Day', 'Victory Election Day'], 0),
   ('On what date did VE Day occur?', ['May 8, 1945', 'August 19, 1942', 'December 1943', 'June 6, 1944'], 0),
   ('What event did VE Day mark the formal end of?', ['Fighting in Europe following Germanys surrender', 'The entire Second World War worldwide with no fighting remaining anywhere', 'The First World War in Europe', 'A single regional battle with no broader significance'], 0),
   ('How did Canadians generally respond to the announcement of VE Day?', ['With widespread public celebrations', 'With a nationwide period of complete silence and no public reaction', 'With an immediate declaration of a new war', 'With a total halt of all public activity for a full year'], 0),
   ('What did VE Day prompt recognition of regarding Canadian forces?', ['Their enormous contributions and sacrifices throughout the war', 'Their complete absence from the European theatre of war', 'Their refusal to participate in any wartime effort', 'Their responsibility for starting the conflict'], 0)]),
]),
day(159, [
E('Literature: The Verse Novel',
  'Grade 10 English strand: a verse novel is a novel-length narrative told primarily through poetry rather than prose, combining the storytelling scope of a novel with the condensed, rhythmic, and imagistic qualities of poetic form.',
  [('What is a verse novel?', ['A novel-length narrative told primarily through poetry rather than prose', 'A short poem with no narrative content at all', 'A legal document written entirely in verse', 'A textbook chapter formatted as a numbered list'], 0),
   ('What two literary qualities does a verse novel combine?', ['The storytelling scope of a novel and the rhythmic, imagistic qualities of poetry', 'The structure of a scientific report and a grocery list', 'A phone directory and a weather almanac', 'A legal contract and a technical manual'], 0),
   ('How does a verse novel typically differ from a traditional prose novel in form?', ['It is composed primarily of poems or verse rather than continuous prose paragraphs', 'It contains no chapters, characters, or narrative progression of any kind', 'It must always rhyme in every single line with no exception', 'It cannot contain any dialogue between characters'], 0),
   ('What effect might the condensed language of a verse novel create for readers?', ['A heightened emotional intensity delivered through fewer, carefully chosen words', 'A complete absence of any emotional content', 'An excessively long and repetitive narrative style', 'A style that eliminates any character development'], 0),
   ('Why might an author choose the verse novel form to tell a story?', ['To use the rhythm, imagery, and white space of poetry to shape how a reader experiences the narrative', 'Because verse novels are required to have no plot whatsoever', 'Because prose is no longer permitted in modern literature', 'Because verse novels cannot address serious or emotional subject matter'], 0)]),
M('Algebra: Solving Systems of Nonlinear Equations',
  'Grade 10 Math strand: a system of nonlinear equations includes at least one equation that is not linear, such as a quadratic or circle equation, and can be solved using substitution or graphing, often producing more than one solution where the curves intersect.',
  [('What makes a system of equations nonlinear?', ['At least one equation in the system is not linear, such as a quadratic or circle equation', 'Every equation in the system must be a straight line', 'The system contains no equations at all', 'The system can only ever have exactly one variable'], 0),
   ('Which method can be used to solve a system of nonlinear equations?', ['Substitution or graphing', 'Ignoring one of the equations entirely', 'Randomly guessing values with no verification', 'Converting every equation into an unrelated word problem'], 0),
   ('How many solutions can a system involving a line and a circle potentially have?', ['Zero, one, or two solutions, depending on where the curves intersect', 'Always exactly one solution in every possible case', 'An infinite number of solutions in every possible case', 'Exactly three solutions with no exceptions'], 0),
   ('What does a solution to a system of nonlinear equations represent graphically?', ['A point where the graphs of the equations intersect', 'A point located far outside both graphed curves', 'The exact centre of only one of the two curves', 'A point where neither curve is defined'], 0),
   ('Why might solving a system of nonlinear equations produce more solutions than a similar linear system?', ['Curved graphs such as parabolas and circles can intersect a line at more than one point', 'Nonlinear equations can never intersect with any other equation', 'Every nonlinear system always has exactly zero solutions', 'Curves are not allowed to intersect straight lines under any circumstance'], 0)]),
Sc('Biology: Pollinators and Colony Collapse Disorder',
   'Grade 10 Science strand: pollinators such as bees transfer pollen between flowers, supporting the reproduction of many food crops and wild plants, and colony collapse disorder is a phenomenon in which worker bees abruptly disappear from a hive, threatening pollination services and agricultural productivity.',
   [('What role do pollinators such as bees play in ecosystems?', ['They transfer pollen between flowers, supporting plant reproduction', 'They remove pollen entirely from an ecosystem with no benefit', 'They have no connection to the reproduction of plants', 'They exclusively consume plants without any pollination occurring'], 0),
    ('What is colony collapse disorder?', ['A phenomenon in which worker bees abruptly disappear from a hive', 'A steady, planned increase in the size of a bee colony', 'A disease that affects only plants, never insects', 'A natural and harmless yearly migration of bees'], 0),
    ('Why is colony collapse disorder a concern for agriculture?', ['It threatens the pollination services that many food crops depend on', 'It has no effect on any agricultural crop whatsoever', 'It only affects crops that require no pollination at all', 'It guarantees an increase in crop yields every year'], 0),
    ('Which of the following is considered a possible contributing factor to pollinator decline?', ['Pesticide exposure and habitat loss', 'An overabundance of flowering plants with no other factors involved', 'A complete absence of any environmental stress', 'A guaranteed increase in natural predators with no negative effects'], 0),
    ('Why are pollinators considered important beyond agricultural crops?', ['They also support the reproduction of many wild plant species within natural ecosystems', 'They have no role in any ecosystem outside of farmland', 'They exclusively pollinate a single species of plant worldwide', 'They prevent all plant reproduction from occurring'], 0)]),
H('The Canadian Womens Army Corps and Wartime Service',
  'Grade 10 History strand: the Canadian Womens Army Corps was formed in 1941 to allow women to serve in official non-combat roles such as clerical work, communications, and vehicle maintenance, freeing more men for combat duty and marking a significant expansion of womens participation in the Canadian war effort.',
  [('In what year was the Canadian Womens Army Corps formed?', ['1941', '1917', '1938', '1949'], 0),
   ('What type of roles did members of the Canadian Womens Army Corps typically serve in?', ['Non-combat roles such as clerical work, communications, and vehicle maintenance', 'Front-line combat roles identical to infantry soldiers', 'Roles limited entirely to elected political office', 'Roles restricted only to unpaid volunteer work with no military structure'], 0),
   ('What was one stated purpose of forming the Corps?', ['To free more men for combat duty by having women fill support roles', 'To completely replace the entire Canadian military with women', 'To end Canadian participation in the war effort', 'To prevent women from holding any position within the military'], 0),
   ('What broader trend did the formation of the Corps reflect?', ['An expansion of womens participation in the Canadian war effort', 'A reduction in womens participation in any wartime activity', 'A complete absence of women from Canadian society during the war', 'A policy that excluded women from all forms of paid work'], 0),
   ('Why is the Canadian Womens Army Corps significant to the study of the home front and wartime service?', ['It illustrates how the demands of total war expanded opportunities for women in official military roles', 'It shows that women played no role in Canada during the Second World War', 'It proves that the military structure remained completely unchanged throughout the war', 'It demonstrates that only men were permitted to support the war effort in any capacity'], 0)]),
]),
day(160, [
E('English Review: Grammar, Reading, and Literary Forms (Days 151-159)',
  'Grade 10 English strand review: students revisit subordinate clauses and complex sentences, tone shifts in poetry, the character sketch, the picaresque novel, reality television, sentence types, pastoral imagery, the news report, and the verse novel.',
  [('What is a subordinate clause?', ['A group of words with a subject and a verb that cannot stand alone as a complete sentence', 'A complete sentence that can stand alone with no other clause', 'A single word with no subject or verb', 'A punctuation mark used to separate two independent clauses'], 0),
   ('What is a tone shift?', ['A change in the attitude conveyed within a poem', 'A change in the font used to print a poem', 'A change in the title of an unrelated poem', 'A change in the authors legal name'], 0),
   ('What type of hero does a picaresque novel typically follow?', ['A resourceful, low-born hero known as a picaro', 'A powerful monarch ruling over a vast empire', 'A retired scientist working alone in a laboratory', 'A committee of unnamed government officials'], 0),
   ('What structure is commonly used to organize a news report?', ['The inverted pyramid, placing the most important information first', 'A structure that saves the most important information for the very last line', 'A structure with no clear order of information', 'A structure based entirely on rhyme and meter'], 0),
   ('What is a verse novel?', ['A novel-length narrative told primarily through poetry rather than prose', 'A short poem with no narrative content at all', 'A legal document written entirely in verse', 'A textbook chapter formatted as a numbered list'], 0)]),
M('Math Review: Calculus, Vectors, Probability, and Number Theory (Days 151-159)',
  'Grade 10 Math strand review: students revisit the second derivative and concavity, perfect numbers and Mersenne primes, the t-distribution, graph colouring, vector equations of lines and planes, Markov chains, even and odd functions, Taylor and Maclaurin series, and nonlinear systems.',
  [('What does the second derivative of a function measure?', ['How the rate of change of the function is itself changing', 'The exact value of the function at a single point', 'The total area under the graph of the function', 'The number of times the function crosses the x-axis'], 0),
   ('What is a perfect number?', ['A positive integer that equals the sum of its proper divisors', 'Any integer that is divisible by exactly two numbers', 'A number that has no divisors other than itself', 'A number that is always negative'], 0),
   ('What is the chromatic number of a graph?', ['The smallest number of colours needed so no two adjacent vertices share a colour', 'The total number of vertices in the graph', 'The total number of edges in the graph', 'The largest possible number of colours that could ever be used'], 0),
   ('What does a Markov chain model?', ['A sequence of events where the probability of the next state depends only on the current state', 'A sequence where every future event is completely fixed with no randomness', 'A sequence where each event depends on every prior event in full detail', 'A single isolated event with no sequence involved'], 0),
   ('What is a Maclaurin series?', ['A special case of a Taylor series centred at zero', 'A series that can only be centred at a nonzero point', 'A series unrelated to derivatives of any kind', 'A series that only applies to whole numbers'], 0)]),
Sc('Science Review: Genetics, Chemistry, Physics, and Earth Science (Days 151-159)',
   'Grade 10 Science strand review: students revisit population genetics and Hardy-Weinberg, thermochemistry, diffraction and interference of light, the aurora borealis, sleep and circadian rhythms, corrosion, resonance and standing waves, mineral resource management, and pollinator decline.',
   [('What does the Hardy-Weinberg principle describe?', ['The condition under which allele frequencies remain stable across generations', 'A process that always causes rapid genetic change in every population', 'A method for building a family tree of a single organism', 'A rule that applies only to nonliving matter'], 0),
    ('What is a Mersenne prime most closely linked to in number theory?', ['Perfect numbers, through the Euclid-Euler theorem', 'The pH scale', 'The rock cycle', 'The immune system'], 0),
    ('What is diffraction?', ['The bending of light waves as they pass around an obstacle or through a narrow opening', 'The complete absorption of light by a solid object', 'The reflection of light directly back toward its source', 'The conversion of light into sound energy'], 0),
    ('What is resonance?', ['A dramatic increase in vibration amplitude that occurs when a system is driven at its natural frequency', 'A permanent reduction of vibration to exactly zero', 'A process that only occurs in complete silence', 'A phenomenon unrelated to frequency of any kind'], 0),
    ('What is colony collapse disorder?', ['A phenomenon in which worker bees abruptly disappear from a hive', 'A steady, planned increase in the size of a bee colony', 'A disease that affects only plants, never insects', 'A natural and harmless yearly migration of bees'], 0)]),
H('History Review: Canada in the Second World War, 1942-1945 (Days 151-159)',
  'Grade 10 History strand review: students revisit the Dieppe Raid, the Battle of the Atlantic, the 1942 conscription plebiscite, the Italian Campaign and Ortona, D-Day and Normandy, the Battle of the Scheldt, the liberation of the Netherlands, VE Day, and the Canadian Womens Army Corps.',
  [('What was the outcome of the Dieppe Raid for the attacking force?', ['Heavy casualties within a single day', 'A complete and lasting capture of the port with no losses', 'An immediate German surrender', 'A peaceful withdrawal with no combat at all'], 0),
   ('What was the Battle of the Atlantic?', ['The longest continuous military campaign of the Second World War, fought largely over merchant shipping', 'A single one-day naval battle fought near Halifax', 'A land battle fought entirely within continental Europe', 'A diplomatic conference held in a neutral country'], 0),
   ('At which beach did Canadian troops land during the D-Day invasion?', ['Juno Beach', 'Omaha Beach', 'Utah Beach', 'Sword Beach'], 0),
   ('What port did clearing the Scheldt Estuary allow the Allies to use?', ['The port of Antwerp', 'The port of Halifax', 'The port of Vancouver', 'The port of Liverpool'], 0),
   ('On what date did VE Day occur?', ['May 8, 1945', 'August 19, 1942', 'December 1943', 'June 6, 1944'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_151_160)
    append_to(10, g10_151_160)
