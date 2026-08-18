#!/usr/bin/env python3
"""Grade 7, Days 171-180 -- extends Grade 7 from 170 to 180 days. Topics
chosen after dumping the full (subject, title) list for Days 1-170 from
data/grade7.json (680 unique (subject, title) pairs, zero duplicates) and
grepping every candidate title/keyword below against that dump to confirm
zero overlap, since Grade 7's earlier 170 days already cover an
unusually exhaustive range of subject matter across all four subjects.

Fresh, non-duplicate topics picked this batch:
Language: adverb clauses of time, reason, and condition, analyzing
juxtaposition and contrast in literature, writing a historical fiction
narrative, false cognates and words that trick you, analyzing video game
narratives and design (media literacy), direct and indirect objects in a
sentence, analyzing personification and anthropomorphism, writing a radio
drama script, analyzing understatement and hyperbole as literary devices.
Math: solving systems of linear equations by graphing, multiples/factors
and the Sieve of Eratosthenes, the midsegment theorem for triangles,
solving absolute value equations (intro), constructing and interpreting
stacked bar graphs, budgeting for a class trip (cost-benefit analysis),
tangent lines and basic circle theorems (intro), modular arithmetic and
clock math, solving quadratic equations by factoring (intro).
Science: simple harmonic motion and springs, metamorphosis in insects and
amphibians, radial and bilateral symmetry in animal body plans, convection
currents in weather and plate tectonics, household chemical safety and
common reactions, wave energy converters and ocean power, noise pollution
and sound insulation, keystone species and ecosystem stability, sinkholes,
caves, and karst landscapes.
SocialStudies: the Northwest Passage and Arctic sovereignty, the Canadian
Football League and the Grey Cup, the Doukhobors and Mennonite settlement
on the Canadian prairies, the Panama Canal and its effect on Canadian
trade routes, the Springhill mining disaster and workplace safety reform,
the Trans-Canada Highway and national infrastructure, Canadas Supreme
Court and judicial review, the 1919 Paris Peace Conference and Canadas
independent voice, the CRTC and Canadian media regulation.

None of these titles or underlying topics duplicate anything appearing in
Days 1-170 of data/grade7.json (verified both by reading the full title
dump and by grepping every candidate title keyword against it before
writing this file). Day 180 is a cross-subject review day drawing quiz
content from Days 171-179 of this batch, with review titles kept
textually distinct from every earlier review day (including Day 170's
four review titles, and all earlier "(Days NN-NN)" review titles).

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py through gen_grade7_days161_170.py (e.g.
"Canadas" not "Canada's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days171_180.py
  cd ~/gradesbooster && python3 build_json.py --grade 7
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science and Technology',
    'TVO Learn: Grade 7 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L7, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M7, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S7, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS7, q)


def _rebalance_answer_positions(days, seed=20260818):
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


g7_171_180 = [
day(171, [
L('Grammar: Adverb Clauses of Time, Reason, and Condition',
  'Grade 7 Language strand: an adverb clause is a group of words with a subject and a verb that functions like an adverb, modifying a verb, adjective, or another adverb, and adverb clauses often begin with subordinating words such as when, because, although, or if to show time, reason, or condition.',
  [('What is an adverb clause?', ['A group of words with a subject and verb that functions like an adverb', 'A single word that describes a noun', 'A concept unrelated to grammar', 'A clause that can never begin a sentence'], 0),
   ('Which subordinating word could begin an adverb clause of reason?', ['Because', 'And', 'A concept unrelated to adverb clauses', 'Or'], 0),
   ('Which sentence contains an adverb clause of condition?', ['If it rains tomorrow, the game will be cancelled.', 'The tall red barn stood near the field.', 'A concept unrelated to grammar', 'Running quickly, she caught the bus.'], 0),
   ('What does an adverb clause of time typically tell the reader?', ['When an action takes place', 'What colour an object is', 'A concept unrelated to adverb clauses', 'How many nouns are in a sentence'], 0),
   ('Why might a writer use an adverb clause instead of two separate short sentences?', ['To show a clear relationship, such as cause and effect, between two ideas', 'Adverb clauses can never connect two ideas', 'A concept unrelated to grammar', 'Two separate sentences always show relationships more clearly than one combined sentence'], 0)]),
M('Algebra: Solving Systems of Linear Equations by Graphing',
  'Grade 7 Math strand: a system of linear equations can be solved by graphing both lines on the same coordinate plane, since the point where the two lines intersect represents the values of x and y that satisfy both equations at once.',
  [('What does the solution to a system of two linear equations represent on a graph?', ['The point where the two lines intersect', 'The point where either line crosses the x-axis', 'A concept unrelated to algebra', 'The steepness of just one of the lines'], 0),
   ('If two lines in a system are graphed and never cross, what does that mean about the system?', ['The system has no solution because the lines are parallel', 'The system always has exactly one solution', 'A concept unrelated to systems of equations', 'The lines must be the exact same line'], 0),
   ('If the graphs of two equations intersect at the point (2, 3), what is the solution to the system?', ['x equals 2 and y equals 3', 'x equals 3 and y equals 2', 'A concept unrelated to graphing systems', 'There is no solution at all'], 0),
   ('What does it mean if the graphs of two linear equations in a system are the same line?', ['The system has infinitely many solutions', 'The system has exactly one solution', 'A concept unrelated to algebra', 'The system can never be solved by graphing'], 0),
   ('Why might solving a system by graphing be less precise than solving it algebraically?', ['Reading an exact intersection point from a graph can be difficult if the coordinates are not whole numbers', 'Graphing always gives a more precise answer than algebra', 'A concept unrelated to systems of equations', 'Graphs can never show the solution to a system'], 0)]),
Sc('Physics: Simple Harmonic Motion and Springs',
   'Grade 7 Science strand: simple harmonic motion is a repeating back-and-forth motion, such as a spring stretching and compressing or a mass bouncing at the end of a spring, where the restoring force pulling the object back toward its resting position increases the farther the object moves away from that position.',
   [('What is simple harmonic motion?', ['A repeating back-and-forth motion around a resting position', 'Motion that only ever happens once and never repeats', 'A concept unrelated to physics', 'Motion that always speeds up forever without stopping'], 0),
    ('What force pulls a stretched or compressed spring back toward its resting position?', ['The restoring force', 'Friction alone', 'A concept unrelated to simple harmonic motion', 'Gravity acting sideways'], 0),
    ('What generally happens to the restoring force on a spring as it is stretched farther from its resting position?', ['The restoring force increases', 'The restoring force disappears completely', 'A concept unrelated to springs', 'The restoring force always stays at zero'], 0),
    ('What is one everyday example of simple harmonic motion?', ['A mass bouncing at the end of a spring', 'A car driving in a straight line at constant speed', 'A concept unrelated to physics', 'A ball resting motionless on a flat table'], 0),
    ('Why might a bouncing spring eventually stop moving even though its motion is described as repeating?', ['Friction and air resistance gradually remove energy from the system', 'Simple harmonic motion can never lose any energy over time', 'A concept unrelated to physics', 'Springs are physically incapable of ever coming to rest'], 0)]),
SS('Social Studies: The Northwest Passage and Arctic Sovereignty',
   'Grade 7 Social Studies strand: the Northwest Passage is a sea route through the Canadian Arctic connecting the Atlantic and Pacific Oceans, and as melting sea ice makes the route more navigable, Canada has worked to assert its sovereignty over these Arctic waters against competing international claims.',
   [('What is the Northwest Passage?', ['A sea route through the Canadian Arctic connecting the Atlantic and Pacific Oceans', 'A mountain pass located in British Columbia', 'A concept unrelated to Canadian geography', 'A railway line built across the prairies'], 0),
    ('Why has the Northwest Passage become more navigable in recent decades?', ['Melting sea ice has opened the route for longer periods each year', 'The passage has always been completely ice-free year round', 'A concept unrelated to Arctic geography', 'The route was recently dug out by construction crews'], 0),
    ('What has Canada worked to assert over the waters of the Northwest Passage?', ['Its sovereignty, or legal control, over the Arctic waters', 'Canada has no interest in the Northwest Passage at all', 'A concept unrelated to social studies', 'Complete ownership of the entire Atlantic Ocean'], 0),
    ('Why might increased shipping traffic through the Northwest Passage matter to Canada economically and environmentally?', ['It could bring new trade opportunities alongside risks to fragile Arctic ecosystems', 'Shipping traffic in the Arctic has no economic or environmental effects', 'A concept unrelated to Arctic sovereignty', 'The Northwest Passage is located far from any Canadian territory'], 0),
    ('Why might other countries dispute Canadas claim that the Northwest Passage is internal Canadian waters?', ['Some countries argue the passage should be treated as an international strait open to free passage', 'No other country has ever expressed any interest in the passage', 'This concept has no relevance to social studies', 'The passage is legally recognized by every country as belonging only to Canada'], 0)]),
]),
day(172, [
L('Reading: Analyzing Juxtaposition and Contrast in Literature',
  'Grade 7 Language strand: juxtaposition is a literary technique in which an author places two contrasting ideas, characters, or images side by side, and the resulting contrast can highlight differences and deepen a readers understanding of both elements.',
  [('What is juxtaposition?', ['Placing two contrasting ideas, characters, or images side by side', 'Repeating the exact same idea multiple times in a row', 'A concept unrelated to reading', 'Removing all conflict from a story'], 0),
   ('What effect can juxtaposition have on a reader?', ['It can highlight differences and deepen understanding of both contrasted elements', 'It always confuses the reader with no benefit at all', 'A concept unrelated to juxtaposition', 'It removes any need to think about the text'], 0),
   ('If an author describes a wealthy characters mansion right after describing a poor characters shack, what technique is being used?', ['Juxtaposition', 'Onomatopoeia', 'A concept unrelated to literary devices', 'Alliteration'], 0),
   ('Why might an author juxtapose a peaceful scene with a violent one?', ['To emphasize the shock or contrast between the two moods', 'Juxtaposing scenes can never create any contrast or emphasis', 'A concept unrelated to reading', 'To make both scenes feel exactly the same'], 0),
   ('How does juxtaposition differ from simply describing one idea after another with no connection?', ['Juxtaposition intentionally places contrasting elements together to create meaning', 'Juxtaposition never involves any intentional placement of ideas', 'This concept has no relevance to reading', 'Juxtaposition only ever involves describing identical ideas'], 0)]),
M('Number Theory: Multiples, Factors, and the Sieve of Eratosthenes',
  'Grade 7 Math strand: the Sieve of Eratosthenes is a method for finding all prime numbers up to a given limit by systematically crossing out the multiples of each prime, starting with 2, leaving only the primes uncrossed.',
  [('What is the Sieve of Eratosthenes used to find?', ['All prime numbers up to a given limit', 'The sum of every number in a list', 'A concept unrelated to number theory', 'Only even numbers within a range'], 0),
   ('In the Sieve of Eratosthenes, what happens to the multiples of each prime number?', ['They are crossed out, leaving only primes uncrossed', 'They are circled and added to a separate list of primes', 'A concept unrelated to the sieve method', 'They are multiplied together to form a new number'], 0),
   ('Which number is the first one used to begin crossing out multiples in the sieve method?', ['2', '1', 'A concept unrelated to the Sieve of Eratosthenes', '0'], 0),
   ('Why is 1 not included as a prime number when using the sieve method?', ['By definition, a prime number must have exactly two factors, and 1 has only one', '1 is actually the largest prime number', 'A concept unrelated to number theory', 'The sieve method always begins by crossing out the number 1 as a prime'], 0),
   ('Why might the Sieve of Eratosthenes be a useful strategy for finding primes compared to testing each number individually for divisibility?', ['It systematically eliminates composite numbers, which can be faster for finding many primes at once', 'Testing each number individually is always faster than any sieve method', 'A concept unrelated to number theory', 'The sieve method can only ever find a single prime number at a time'], 0)]),
Sc('Biology: Metamorphosis in Insects and Amphibians',
   'Grade 7 Science strand: metamorphosis is a dramatic change in body form during an organisms development, such as a caterpillar transforming into a butterfly through complete metamorphosis, or a tadpole gradually developing into a frog through a more gradual process.',
   [('What is metamorphosis?', ['A dramatic change in body form during an organisms development', 'A process in which an organism never changes its body form', 'A concept unrelated to biology', 'A type of rock formation'], 0),
    ('What does a caterpillar transform into through complete metamorphosis?', ['A butterfly', 'A beetle', 'A concept unrelated to metamorphosis', 'A spider'], 0),
    ('What stage comes between the caterpillar and adult butterfly in complete metamorphosis?', ['The pupa, or chrysalis, stage', 'The larval stage occurs after the adult stage', 'A concept unrelated to insect development', 'There is no intermediate stage at all'], 0),
    ('What does a tadpole gradually develop into?', ['A frog', 'A fish', 'A concept unrelated to amphibian development', 'A turtle'], 0),
    ('Why might undergoing metamorphosis be an evolutionary advantage for some species?', ['Different life stages can occupy different habitats and food sources, reducing competition among the same species', 'Metamorphosis always makes survival more difficult for a species', 'A concept unrelated to biology', 'Every species that undergoes metamorphosis eventually goes extinct'], 0)]),
SS('Social Studies: The Canadian Football League and the Grey Cup',
   'Grade 7 Social Studies strand: the Canadian Football League, founded in its modern form in 1958, is a professional sports league whose championship game, the Grey Cup, has been awarded since 1909 and remains one of Canadas most watched annual sporting events.',
   [('What is the Canadian Football League?', ['A professional sports league in Canada', 'A league that organizes only youth soccer teams', 'A concept unrelated to Canadian sports', 'An organization that regulates Canadian banking'], 0),
    ('What is the name of the CFL championship game?', ['The Grey Cup', 'The Stanley Cup', 'A concept unrelated to the CFL', 'The World Series'], 0),
    ('Since roughly what year has the Grey Cup been awarded?', ['1909', '1958', 'A concept unrelated to Canadian sports history', '1982'], 0),
    ('Why might a national sports championship like the Grey Cup be significant to Canadian communities?', ['It brings communities together and creates a shared sense of excitement and tradition', 'National championships have no connection to community identity', 'A concept unrelated to social studies', 'The Grey Cup is not followed by any Canadian communities'], 0),
    ('Why might professional sports leagues like the CFL be considered part of a countrys cultural identity?', ['Widely followed sports and their traditions can become woven into a countrys shared culture', 'Professional sports leagues have no connection to cultural identity of any kind', 'This concept has no relevance to social studies', 'Sports leagues can only ever exist in isolation from the broader culture'], 0)]),
]),
day(173, [
L('Writing: Writing a Historical Fiction Narrative',
  'Grade 7 Language strand: historical fiction blends invented characters and plot with real historical settings, events, or details, requiring a writer to research the time period carefully so the story feels authentic while still telling an original, imaginative tale.',
  [('What defines historical fiction?', ['A story that blends invented characters and plot with a real historical setting or events', 'A story that must be entirely true and contain no invented details', 'A concept unrelated to writing', 'A story that can only take place in the future'], 0),
   ('Why is research an important step before writing historical fiction?', ['It helps the writer accurately portray the setting, customs, and events of the chosen time period', 'Research is never necessary when writing any kind of fiction', 'A concept unrelated to historical fiction', 'Historical fiction is not allowed to include any real historical details'], 0),
   ('Which of these could realistically appear in a piece of historical fiction set during the building of the Canadian Pacific Railway?', ['A fictional worker character interacting with real historical events of the railway construction', 'A character using a smartphone to call a friend', 'A concept unrelated to writing historical fiction', 'A spaceship landing near the railway construction site'], 0),
   ('Why might an author choose to tell a historical event through the eyes of a fictional character rather than only stating the facts?', ['A personal, invented perspective can make historical events feel more vivid and relatable to readers', 'Fictional characters can never make a historical event feel more relatable', 'A concept unrelated to writing', 'Historical fiction is required to remove all emotion from the story'], 0),
   ('What is one challenge a writer might face when balancing historical accuracy with an engaging invented plot?', ['Making sure invented events still feel plausible within the real historical context', 'There is no challenge at all in balancing accuracy with an invented plot', 'This concept has no relevance to writing', 'Historical accuracy and an engaging plot can never be combined in the same story'], 0)]),
M('Geometry: The Midsegment Theorem for Triangles',
  'Grade 7 Math strand: a midsegment of a triangle connects the midpoints of two sides, and the midsegment theorem states that this midsegment is always parallel to the third side and exactly half its length.',
  [('What does a midsegment of a triangle connect?', ['The midpoints of two sides of the triangle', 'Two vertices of the triangle directly', 'A concept unrelated to geometry', 'The midpoint of one side to a vertex'], 0),
   ('According to the midsegment theorem, how does a midsegment relate to the third side of the triangle?', ['It is parallel to the third side and exactly half its length', 'It is perpendicular to the third side and twice its length', 'A concept unrelated to the midsegment theorem', 'It has no relationship to the third side at all'], 0),
   ('If the third side of a triangle measures 18 centimetres, how long is the midsegment parallel to it?', ['9 centimetres', '18 centimetres', '36 centimetres', '6 centimetres'], 0),
   ('How many midsegments does a single triangle have in total?', ['Three, one connecting the midpoints of each pair of sides', 'Only one midsegment per triangle', 'A concept unrelated to triangles', 'A triangle has no midsegments at all'], 0),
   ('Why is the midsegment theorem useful when a measurement of a triangles side is difficult to obtain directly?', ['It allows the length of a side to be found indirectly using half the length of a related midsegment, or vice versa', 'The midsegment theorem can never be used to find any missing length', 'A concept unrelated to geometry', 'Midsegments are always longer than the sides they relate to'], 0)]),
Sc('Biology: Radial and Bilateral Symmetry in Animal Body Plans',
   'Grade 7 Science strand: animals with radial symmetry, such as sea stars and jellyfish, have body parts arranged evenly around a central point, while animals with bilateral symmetry, such as most vertebrates and insects, have a left and right side that mirror each other.',
   [('What is radial symmetry?', ['A body plan with parts arranged evenly around a central point', 'A body plan with no repeating pattern of any kind', 'A concept unrelated to biology', 'A body plan found only in plants'], 0),
    ('What is bilateral symmetry?', ['A body plan where the left and right sides mirror each other', 'A body plan where every part of the body is identical in every direction', 'A concept unrelated to animal body plans', 'A body plan that only applies to single-celled organisms'], 0),
    ('Which of these animals is a common example of radial symmetry?', ['A sea star', 'A dog', 'A concept unrelated to radial symmetry', 'A grasshopper'], 0),
    ('Which of these animals is a common example of bilateral symmetry?', ['A human being', 'A jellyfish', 'A concept unrelated to bilateral symmetry', 'A sea anemone'], 0),
    ('Why might bilateral symmetry be considered advantageous for animals that move actively in a specific direction?', ['It supports a distinct head end for sensing the environment and a streamlined body for efficient movement', 'Bilateral symmetry makes directional movement impossible for an animal', 'A concept unrelated to biology', 'Radial symmetry is always better suited to fast, directional movement'], 0)]),
SS('Social Studies: The Doukhobors and Mennonite Settlement on the Canadian Prairies',
   'Grade 7 Social Studies strand: the Doukhobors and Mennonites were religious groups who immigrated to the Canadian prairies in significant numbers in the late 1800s, often seeking freedom from persecution and military conscription in their home countries, and they established distinct farming communities across the region.',
   [('Where did the Doukhobors and Mennonites primarily settle in Canada?', ['The Canadian prairies', 'The Atlantic coast', 'A concept unrelated to Canadian immigration history', 'Northern Ontario'], 0),
    ('What was one common reason the Doukhobors and Mennonites left their home countries?', ['Seeking freedom from persecution and military conscription', 'They were forced onto ships against their will with no stated reason', 'A concept unrelated to social studies', 'They were relocated by an international lottery system'], 0),
    ('Roughly when did significant numbers of Doukhobors and Mennonites settle on the prairies?', ['The late 1800s', 'The 1600s', 'A concept unrelated to prairie settlement history', 'The 1990s'], 0),
    ('What kind of communities did these groups typically establish on the prairies?', ['Distinct farming communities', 'Communities focused entirely on mining', 'A concept unrelated to Doukhobor and Mennonite settlement', 'Communities with no connection to agriculture'], 0),
    ('Why might a group emigrate specifically to avoid military conscription in their country of origin?', ['Their religious or personal beliefs may prevent them from participating in warfare', 'Military conscription has no connection to why groups choose to emigrate', 'This concept has no relevance to social studies', 'Avoiding conscription was never a factor in any historical immigration to Canada'], 0)]),
]),
day(174, [
L('Vocabulary: False Cognates and Words That Trick You',
  'Grade 7 Language strand: a false cognate is a word in one language that looks or sounds similar to a word in another language but actually has a different meaning, which can easily mislead someone who assumes the words share the same meaning.',
  [('What is a false cognate?', ['A word that looks or sounds similar to a word in another language but has a different meaning', 'A word that is spelled identically in every language in the world', 'A concept unrelated to vocabulary', 'A word that has no meaning in any language'], 0),
   ('Why can false cognates be tricky for someone learning a new language?', ['A learner may assume the similar-looking word shares the same meaning, leading to a mistake', 'False cognates always have the exact same meaning across every language', 'A concept unrelated to false cognates', 'False cognates never appear in any real language'], 0),
   ('What is the key difference between a true cognate and a false cognate?', ['A true cognate shares both a similar form and a related meaning, while a false cognate does not share the meaning', 'True cognates and false cognates are always identical concepts', 'A concept unrelated to vocabulary', 'False cognates only exist within a single language'], 0),
   ('Why might understanding false cognates be especially useful for a student learning French or Spanish alongside English?', ['It can prevent embarrassing or confusing misunderstandings caused by assuming shared meaning', 'False cognates have no impact on understanding a new language', 'This concept has no relevance to vocabulary', 'Every word that looks similar between two languages always means the same thing'], 0),
   ('How might a careful reader confirm whether a similar-looking foreign word is a true cognate or a false cognate?', ['By checking the words actual meaning in a dictionary rather than assuming based on appearance', 'By assuming that appearance alone always determines meaning', 'A concept unrelated to false cognates', 'There is no reliable way to ever confirm a words meaning'], 0)]),
M('Algebra: Solving Absolute Value Equations (Intro)',
  'Grade 7 Math strand: the absolute value of a number is its distance from zero on a number line, always expressed as a non-negative value, so an equation like the absolute value of x equals 5 has two possible solutions, x equals 5 and x equals negative 5.',
  [('What does the absolute value of a number represent?', ['Its distance from zero on a number line', 'The number multiplied by negative one', 'A concept unrelated to algebra', 'The number divided by two'], 0),
   ('Can the absolute value of a number ever be negative?', ['No, absolute value is always non-negative', 'Yes, absolute value is always negative', 'A concept unrelated to absolute value', 'Only when the original number is a fraction'], 0),
   ('How many solutions does the equation, the absolute value of x equals 5, generally have?', ['Two solutions, x equals 5 and x equals negative 5', 'Only one solution, x equals 5', 'A concept unrelated to absolute value equations', 'No solutions at all'], 0),
   ('What are the solutions to the equation, the absolute value of x equals 8?', ['x equals 8 and x equals negative 8', 'x equals 8 only', 'x equals negative 8 only', 'There are no solutions'], 0),
   ('Why does an absolute value equation typically produce two possible solutions instead of just one?', ['Both a positive and a negative number can be the same distance from zero', 'Absolute value equations can never have more than one solution', 'A concept unrelated to algebra', 'Negative numbers are never valid solutions to any equation'], 0)]),
Sc('Earth Science: Convection Currents in Weather and Plate Tectonics',
   'Grade 7 Science strand: a convection current is the circular movement of a fluid, such as air, water, or molten rock, caused by uneven heating, with warmer, less dense material rising and cooler, denser material sinking, driving processes from weather patterns to the slow movement of tectonic plates.',
   [('What causes a convection current to form?', ['Uneven heating of a fluid, causing warmer material to rise and cooler material to sink', 'A fluid that is heated evenly throughout with no temperature difference', 'A concept unrelated to earth science', 'The complete absence of any heat source'], 0),
    ('In a convection current, what generally happens to warmer, less dense material?', ['It rises', 'It sinks to the very bottom', 'A concept unrelated to convection currents', 'It stays perfectly still'], 0),
    ('What role do convection currents play in the movement of tectonic plates?', ['Convection currents in the mantle help drive the slow movement of the plates above them', 'Convection currents have no connection to tectonic plate movement', 'A concept unrelated to plate tectonics', 'Tectonic plates move only because of ocean tides'], 0),
    ('How do convection currents in the atmosphere help create weather patterns?', ['Rising warm air and sinking cool air create circulation patterns that influence wind and weather', 'Convection currents never occur in the atmosphere', 'A concept unrelated to earth science', 'Weather patterns are completely unrelated to air temperature'], 0),
    ('Why might a pot of soup heated on a stove be used as an everyday example of convection?', ['The heated liquid at the bottom rises while cooler liquid sinks, creating a visible circulating current', 'Boiling soup demonstrates that convection never actually occurs in liquids', 'This concept has no relevance to science', 'A pot of soup only ever demonstrates conduction, never convection'], 0)]),
SS('Social Studies: The Panama Canal and Its Effect on Canadian Trade Routes',
   'Grade 7 Social Studies strand: the Panama Canal, completed in 1914, connects the Atlantic and Pacific Oceans through Central America, dramatically shortening shipping routes and giving Canadian ports on both coasts a faster path for trade with countries around the world.',
   [('What does the Panama Canal connect?', ['The Atlantic and Pacific Oceans', 'The Arctic and Indian Oceans', 'A concept unrelated to world geography', 'Two rivers within Canada'], 0),
    ('In roughly what year was the Panama Canal completed?', ['1914', '1867', 'A concept unrelated to the Panama Canal', '1982'], 0),
    ('How did the completion of the Panama Canal affect shipping routes?', ['It dramatically shortened shipping routes between the Atlantic and Pacific Oceans', 'It made all shipping routes significantly longer', 'A concept unrelated to social studies', 'It closed off ocean shipping entirely'], 0),
    ('How might the Panama Canal benefit Canadian ports on the Atlantic and Pacific coasts?', ['It gives them a faster path for trade with countries around the world', 'Canadian ports gain no benefit at all from the Panama Canal', 'A concept unrelated to Canadian trade', 'The canal blocks Canadian ships from using it entirely'], 0),
    ('Why might a shorter shipping route through a canal like Panama reduce costs for international trade?', ['Shorter routes require less fuel and time, lowering the overall cost of shipping goods', 'Shorter shipping routes always increase the total cost of trade', 'This concept has no relevance to social studies', 'Shipping costs have no connection to the length of a trade route'], 0)]),
]),
day(175, [
L('Media Literacy: Analyzing Video Game Narratives and Design',
  'Grade 7 Language strand: video games can tell stories through methods unavailable to books or films, such as branching player choices, environmental storytelling embedded in a games setting, and interactive pacing controlled by the player, making media literacy skills important for analyzing how meaning is constructed in this interactive medium.',
  [('What is one storytelling method available to video games that is not typically available to books or films?', ['Branching player choices that affect the story', 'Printed text on a page', 'A concept unrelated to media literacy', 'A fixed, unchangeable sequence of events with no player input'], 0),
   ('What is environmental storytelling in a video game?', ['Conveying story or history through details embedded in the games setting', 'A story told entirely through spoken narration with no visuals', 'A concept unrelated to video game design', 'A method that never includes any visual details'], 0),
   ('How does interactive pacing in a video game differ from the pacing of a film?', ['The player, rather than a fixed timeline, often controls how quickly the story unfolds', 'Every video game moves at the exact same fixed pace as a film', 'A concept unrelated to media literacy', 'Interactive pacing means the story can never be paused or slowed down'], 0),
   ('Why might branching player choices make analyzing a video games narrative more complex than analyzing a novels plot?', ['Different players may experience different versions of the story based on their choices', 'Branching choices always produce the exact same story for every player', 'A concept unrelated to video game narratives', 'Video games never include any narrative elements at all'], 0),
   ('Why is media literacy useful when examining how a video games design shapes a players understanding of its story?', ['It helps players recognize how choices, pacing, and setting are intentionally constructed to convey meaning', 'Media literacy has no application to interactive media like video games', 'This concept has no relevance to media literacy', 'Video game design never involves any intentional storytelling choices'], 0)]),
M('Data Management: Constructing and Interpreting Stacked Bar Graphs',
  'Grade 7 Math strand: a stacked bar graph displays data by dividing each bar into segments that represent different categories, allowing a viewer to compare both the total amount for each bar and the relative size of each category within that total.',
  [('What does a stacked bar graph divide each bar into?', ['Segments representing different categories', 'A single unbroken colour with no divisions', 'A concept unrelated to data management', 'Randomly placed dots with no pattern'], 0),
   ('What can a viewer compare using a stacked bar graph that a simple bar graph does not easily show?', ['The relative size of each category within the total for each bar', 'The exact colour used for the background of the graph', 'A concept unrelated to stacked bar graphs', 'Nothing additional can ever be shown by a stacked bar graph'], 0),
   ('If a stacked bar for a class shows 12 students who prefer soccer and 8 who prefer basketball, what is the total height of that bar?', ['20 students', '12 students', '8 students', '4 students'], 0),
   ('Why might a stacked bar graph be a useful choice for comparing sales of several product types across multiple months?', ['It shows both the total sales per month and how each product type contributes to that total', 'Stacked bar graphs can only ever show a single category at once', 'A concept unrelated to data management', 'Stacked bar graphs cannot display more than one month of data'], 0),
   ('What is one potential drawback of a stacked bar graph when trying to compare the middle segments of several bars directly?', ['Middle segments do not all start at the same baseline, making direct comparison harder', 'Stacked bar graphs make every segment equally easy to compare with no drawbacks', 'A concept unrelated to stacked bar graphs', 'A stacked bar graph can never contain more than one segment per bar'], 0)]),
Sc('Chemistry: Household Chemical Safety and Common Reactions',
   'Grade 7 Science strand: many household products, such as bleach, ammonia-based cleaners, and vinegar, can react with each other in dangerous ways if mixed, so understanding basic chemical safety, reading warning labels, and never combining unknown cleaning products helps prevent harmful reactions in the home.',
   [('Why can mixing certain household cleaning products be dangerous?', ['Some combinations can produce harmful gases or other dangerous chemical reactions', 'Household cleaning products can never react with each other in any way', 'A concept unrelated to chemistry', 'Mixing cleaning products always makes them completely safe'], 0),
    ('What is one practical way to reduce the risk of a dangerous reaction when using household chemicals?', ['Reading warning labels and avoiding combining unknown products', 'Combining as many different cleaning products as possible', 'A concept unrelated to chemical safety', 'Ignoring all labels printed on cleaning product containers'], 0),
    ('Which two types of household products are commonly warned against mixing due to the risk of producing a harmful gas?', ['Bleach and ammonia-based cleaners', 'Water and dish soap', 'A concept unrelated to household chemical safety', 'Two different brands of the exact same product'], 0),
    ('Why might warning labels on household chemical products list specific substances not to mix with the product?', ['Certain combinations can trigger dangerous chemical reactions that manufacturers want to prevent', 'Warning labels are printed with no useful safety information at all', 'A concept unrelated to chemistry', 'Chemical products never require any warning labels of any kind'], 0),
    ('Why is proper ventilation recommended when using strong household cleaning chemicals?', ['It helps disperse potentially harmful fumes and reduces the concentration a person breathes in', 'Ventilation has no effect on the safety of using chemical products', 'This concept has no relevance to science', 'Strong chemical products never release any fumes at all'], 0)]),
SS('Social Studies: The Springhill Mining Disaster and Workplace Safety Reform',
   'Grade 7 Social Studies strand: the Springhill mining disasters in Nova Scotia, including a major explosion in 1958, killed many coal miners and drew national attention to dangerous underground working conditions, contributing to stronger workplace safety regulations in Canadian mining and industry.',
   [('In which province did the Springhill mining disasters occur?', ['Nova Scotia', 'Alberta', 'A concept unrelated to Canadian labour history', 'British Columbia'], 0),
    ('What industry were the Springhill disasters connected to?', ['Coal mining', 'Automobile manufacturing', 'A concept unrelated to the Springhill disasters', 'Commercial fishing'], 0),
    ('What did the Springhill disasters draw national attention to?', ['Dangerous underground working conditions for miners', 'The safety of office buildings in major cities', 'A concept unrelated to social studies', 'The condition of Canadian highways'], 0),
    ('What long-term effect did events like the Springhill disasters have on Canadian industry?', ['They contributed to stronger workplace safety regulations', 'They had no lasting effect on workplace safety at all', 'A concept unrelated to the Springhill mining disasters', 'They led to the complete shutdown of the mining industry nationwide'], 0),
    ('Why might a major workplace disaster lead governments to strengthen safety regulations afterward?', ['Public attention and loss of life can create pressure to prevent similar tragedies in the future', 'Workplace disasters never influence any government policy decisions', 'This concept has no relevance to social studies', 'Safety regulations are always written before any disaster ever occurs'], 0)]),
]),
day(176, [
L('Grammar: Direct and Indirect Objects in a Sentence',
  'Grade 7 Language strand: a direct object receives the action of a verb directly, answering the question what or whom, while an indirect object identifies to whom or for whom the action of the verb is done, typically appearing between the verb and the direct object.',
  [('What question does a direct object typically answer?', ['What or whom', 'Where or when', 'A concept unrelated to grammar', 'How or why'], 0),
   ('What does an indirect object typically identify?', ['To whom or for whom an action is done', 'The subject performing the action', 'A concept unrelated to direct and indirect objects', 'The location where an action takes place'], 0),
   ('In the sentence, She gave her friend a gift, what is the direct object?', ['Gift', 'She', 'Friend', 'Gave'], 0),
   ('In the sentence, She gave her friend a gift, what is the indirect object?', ['Friend', 'Gift', 'A concept unrelated to grammar', 'She'], 0),
   ('Why might identifying the direct and indirect objects in a sentence help a writer understand sentence structure more clearly?', ['It clarifies which parts of the sentence receive the action and who benefits from it', 'Direct and indirect objects never provide any useful information about a sentence', 'A concept unrelated to grammar', 'Every sentence must contain exactly one indirect object'], 0)]),
M('Financial Literacy: Budgeting for a Class Trip (Cost-Benefit Analysis)',
  'Grade 7 Math strand: budgeting for a group trip involves listing all expected costs, such as transportation, admission, and food, comparing total costs against available funds, and weighing the benefits of a purchase or activity against its cost, a process known as cost-benefit analysis.',
  [('What is the first general step when creating a budget for a class trip?', ['Listing all expected costs, such as transportation, admission, and food', 'Spending money first and figuring out the cost afterward', 'A concept unrelated to financial literacy', 'Ignoring all costs entirely'], 0),
   ('What does cost-benefit analysis involve?', ['Weighing the benefits of a purchase or activity against its cost', 'Only ever considering the benefits and ignoring the cost completely', 'A concept unrelated to budgeting', 'Only ever considering the cost and ignoring any benefits'], 0),
   ('If a class trip costs 45 dollars per student for transportation and 15 dollars per student for admission, what is the total cost per student?', ['60 dollars', '45 dollars', '15 dollars', '30 dollars'], 0),
   ('If a class of 25 students each pays 60 dollars for a trip, what is the total amount collected?', ['1500 dollars', '85 dollars', '1250 dollars', '600 dollars'], 0),
   ('Why might a class use cost-benefit analysis when deciding between two possible trip destinations?', ['It helps compare which option offers the most value relative to its cost', 'Cost-benefit analysis can never help compare two different options', 'A concept unrelated to financial literacy', 'The cheapest option is always guaranteed to be the best choice regardless of benefits'], 0)]),
Sc('Renewable Energy: Wave Energy Converters and Ocean Power',
   'Grade 7 Science strand: wave energy converters are devices that capture the kinetic energy of ocean waves and convert it into electricity, offering a renewable power source for coastal communities, though the technology still faces challenges related to cost, durability in harsh ocean conditions, and environmental impact.',
   [('What do wave energy converters capture and convert into electricity?', ['The kinetic energy of ocean waves', 'The heat energy stored in ocean sediment', 'A concept unrelated to renewable energy', 'The chemical energy found in seawater salt'], 0),
    ('What type of communities might particularly benefit from wave energy technology?', ['Coastal communities', 'Communities located deep inland with no ocean access', 'A concept unrelated to wave energy', 'Communities located in deserts'], 0),
    ('What is one challenge that wave energy converters face related to their ocean environment?', ['Durability, since harsh ocean conditions can damage equipment over time', 'Wave energy converters never face any challenges of any kind', 'A concept unrelated to renewable energy', 'Ocean waves never provide enough energy to be worth capturing'], 0),
    ('Why is wave energy considered a renewable source of power?', ['Ocean waves are continuously generated and do not get used up like fossil fuels', 'Ocean waves are a limited resource that will eventually run out completely', 'A concept unrelated to renewable energy', 'Wave energy converters create waves rather than capturing existing ones'], 0),
    ('Why might researchers study the environmental impact of wave energy converters before widespread use?', ['Large numbers of underwater devices could potentially affect marine ecosystems and wildlife', 'Wave energy converters have no possible effect on ocean ecosystems', 'This concept has no relevance to science', 'Environmental impact is never a consideration for any renewable energy technology'], 0)]),
SS('Social Studies: The Trans-Canada Highway and National Infrastructure',
   'Grade 7 Social Studies strand: the Trans-Canada Highway, officially opened in 1962, is one of the longest national highways in the world, stretching from coast to coast, and it was built to improve transportation, trade, and connection between Canadas provinces.',
   [('What is the Trans-Canada Highway?', ['One of the longest national highways in the world, stretching coast to coast across Canada', 'A short highway connecting only two Canadian cities', 'A concept unrelated to Canadian infrastructure', 'A railway line built in the 1800s'], 0),
    ('In roughly what year was the Trans-Canada Highway officially opened?', ['1962', '1867', 'A concept unrelated to Canadian infrastructure history', '1917'], 0),
    ('What was one main purpose of building the Trans-Canada Highway?', ['To improve transportation, trade, and connection between provinces', 'To completely replace all forms of rail travel in Canada', 'A concept unrelated to social studies', 'To connect Canada with countries outside North America by road'], 0),
    ('Why might a coast-to-coast highway be especially significant for a country as geographically large as Canada?', ['It helps link distant regions and communities that might otherwise be difficult to connect by road', 'A large highway system has no particular significance for a large country', 'A concept unrelated to national infrastructure', 'Highways only matter in countries with very small land areas'], 0),
    ('Why might major infrastructure projects like the Trans-Canada Highway require cooperation between the federal government and the provinces?', ['The highway passes through multiple provinces, each with its own jurisdiction over local roads and land', 'Infrastructure projects never require any cooperation between different levels of government', 'This concept has no relevance to social studies', 'Provinces have no involvement whatsoever in highways that cross their territory'], 0)]),
]),
day(177, [
L('Reading: Analyzing Personification and Anthropomorphism in Literature',
  'Grade 7 Language strand: personification gives human qualities to a non-human object or idea, such as saying the wind whispered, while anthropomorphism goes further by giving an animal or object human behaviours and consciousness, such as a talking, thinking animal character in a story.',
  [('What is personification?', ['Giving human qualities to a non-human object or idea', 'Giving an object no qualities of any kind', 'A concept unrelated to reading', 'Removing all descriptive language from a sentence'], 0),
   ('Which sentence is an example of personification?', ['The wind whispered through the trees.', 'The wind blew at 20 kilometres per hour.', 'A concept unrelated to personification', 'The trees measured ten metres tall.'], 0),
   ('What is anthropomorphism?', ['Giving an animal or object human behaviours and consciousness', 'Removing all human characteristics from a character', 'A concept unrelated to literary devices', 'A technique used only in scientific writing'], 0),
   ('Which of these is a strong example of anthropomorphism?', ['A talking mouse character who worries about paying rent', 'A factual description of a mouses diet', 'A concept unrelated to anthropomorphism', 'A chart showing average mouse populations'], 0),
   ('Why might an author use personification or anthropomorphism when writing a story for younger readers?', ['It can make non-human characters or objects feel relatable and easier to connect with emotionally', 'These techniques always make a story harder for readers to understand', 'A concept unrelated to reading', 'Personification and anthropomorphism are never used in stories written for any audience'], 0)]),
M('Geometry: Tangent Lines and Basic Circle Theorems (Intro)',
  'Grade 7 Math strand: a tangent line touches a circle at exactly one point, called the point of tangency, and one key circle theorem states that a tangent line is always perpendicular to the radius drawn to that point of tangency.',
  [('How many points does a tangent line touch on a circle?', ['Exactly one point', 'Exactly two points', 'A concept unrelated to geometry', 'Every point along the circles edge'], 0),
   ('What is the point where a tangent line touches a circle called?', ['The point of tangency', 'The centre of the circle', 'A concept unrelated to tangent lines', 'The diameter point'], 0),
   ('According to a key circle theorem, what is the relationship between a tangent line and the radius drawn to the point of tangency?', ['They are perpendicular to each other', 'They are always parallel to each other', 'A concept unrelated to circle theorems', 'They always overlap completely'], 0),
   ('If a radius drawn to a point of tangency forms a 90 degree angle with the tangent line, what does this confirm?', ['The tangent line is perpendicular to that radius, as the theorem predicts', 'The tangent line must actually pass through the centre of the circle', 'A concept unrelated to tangent lines', 'The circle does not actually have a defined radius'], 0),
   ('Why might understanding tangent lines be useful in real-world applications, such as designing gears or pulley systems?', ['Tangent lines describe how a straight edge or belt can touch a circular object at a single contact point', 'Tangent lines have no real-world applications of any kind', 'A concept unrelated to geometry', 'Gears and pulleys never involve any circular shapes'], 0)]),
Sc('Physics: Noise Pollution and Sound Insulation',
   'Grade 7 Science strand: noise pollution is excessive or disruptive sound in an environment that can negatively affect human health and wildlife, and sound insulation materials work by absorbing or blocking sound waves, reducing how much noise passes from one space into another.',
   [('What is noise pollution?', ['Excessive or disruptive sound in an environment', 'A pleasant, quiet sound with no negative effects', 'A concept unrelated to physics', 'A type of pollution that only affects water'], 0),
    ('What can noise pollution negatively affect?', ['Human health and wildlife', 'Nothing at all, since sound has no physical effects', 'A concept unrelated to noise pollution', 'Only the temperature of the surrounding air'], 0),
    ('How do sound insulation materials generally work?', ['By absorbing or blocking sound waves', 'By amplifying sound waves as loudly as possible', 'A concept unrelated to sound insulation', 'By converting sound waves directly into light'], 0),
    ('Why might a busy highway near a residential neighbourhood use sound barriers?', ['To reduce the amount of traffic noise that reaches nearby homes', 'Sound barriers have no effect on the amount of noise reaching an area', 'A concept unrelated to physics', 'Sound barriers are designed to increase noise levels for residents'], 0),
    ('Why might soft, textured materials such as foam panels reduce noise more effectively than hard, smooth surfaces?', ['Soft, textured materials absorb sound energy rather than reflecting it back into the room', 'Hard, smooth surfaces always absorb more sound than soft materials', 'This concept has no relevance to science', 'Sound waves are not affected by the texture of a surface'], 0)]),
SS('Social Studies: Canadas Supreme Court and Judicial Review',
   'Grade 7 Social Studies strand: the Supreme Court of Canada is the countrys highest court, with the final word on legal disputes, and through judicial review it has the power to determine whether laws passed by governments comply with the Canadian Charter of Rights and Freedoms and the Constitution.',
   [('What is the Supreme Court of Canada?', ['The countrys highest court, with the final word on legal disputes', 'A court that only handles minor traffic violations', 'A concept unrelated to Canadian government', 'A court that exists only at the municipal level'], 0),
    ('What is judicial review?', ['The power of a court to determine whether a law complies with the Constitution', 'A process in which judges are elected directly by the public', 'A concept unrelated to the Supreme Court', 'A review of a judges personal finances'], 0),
    ('Which document does the Supreme Court often reference when reviewing whether a law is constitutional?', ['The Canadian Charter of Rights and Freedoms', 'A private companys internal policy manual', 'A concept unrelated to judicial review', 'A foreign countrys constitution'], 0),
    ('What can happen if the Supreme Court finds that a law violates the Charter of Rights and Freedoms?', ['The law can be struck down or modified', 'The Supreme Court has no power to affect any law in any way', 'A concept unrelated to social studies', 'The law automatically becomes part of the Constitution permanently'], 0),
    ('Why is an independent judiciary, such as the Supreme Court, considered important in a democracy?', ['It can check the power of governments by ensuring their laws respect constitutional rights', 'An independent judiciary has no meaningful role in a democratic system', 'This concept has no relevance to social studies', 'Courts are only ever used to resolve disputes between private individuals'], 0)]),
]),
day(178, [
L('Writing: Writing a Radio Drama Script',
  'Grade 7 Language strand: a radio drama script tells a story using only dialogue, sound effects, and music, since there is no visual element, so writers must rely on descriptive dialogue and carefully chosen sound cues to help listeners imagine the setting and action.',
  [('What three elements does a radio drama primarily rely on to tell its story?', ['Dialogue, sound effects, and music', 'Only camera angles and lighting', 'A concept unrelated to writing', 'Only printed captions displayed on a screen'], 0),
   ('Why must a radio drama rely heavily on descriptive dialogue?', ['There is no visual element, so listeners must imagine the setting and action through sound and speech', 'Radio dramas always include a visual component alongside the audio', 'A concept unrelated to radio drama scripts', 'Descriptive dialogue is never necessary in any audio format'], 0),
   ('What is one purpose of sound effects in a radio drama?', ['To help listeners imagine the setting and action without seeing it', 'Sound effects serve no purpose in a radio drama', 'A concept unrelated to writing a radio script', 'To replace the need for any dialogue at all'], 0),
   ('Why might a radio drama script include a stage direction describing a door creaking open?', ['It cues the sound effects team to create that specific sound at the right moment in the story', 'Stage directions are never included in a radio drama script', 'A concept unrelated to radio drama writing', 'Creaking doors are always represented using dialogue instead of sound effects'], 0),
   ('How does writing for radio drama differ from writing a script meant to be filmed?', ['A radio script cannot rely on visuals, so it must convey everything through sound alone', 'Radio scripts and film scripts require exactly the same techniques with no differences', 'This concept has no relevance to writing', 'A radio drama script always includes detailed camera angle instructions'], 0)]),
M('Number Theory: Modular Arithmetic and Clock Math',
  'Grade 7 Math strand: modular arithmetic involves counting in a cycle that wraps back to zero after reaching a fixed number called the modulus, much like a 12-hour clock wraps back to 1 after reaching 12, and this wrap-around pattern is written using the phrase mod, as in 15 mod 12 equals 3.',
  [('What is modular arithmetic based on?', ['Counting in a cycle that wraps back to zero after reaching a fixed modulus', 'Counting that continues forever without ever repeating', 'A concept unrelated to number theory', 'Counting only with negative numbers'], 0),
   ('What everyday device is often used to explain modular arithmetic?', ['A 12-hour clock', 'A calculator with no display', 'A concept unrelated to modular arithmetic', 'A ruler measuring centimetres'], 0),
   ('What is 15 mod 12?', ['3', '12', '15', '27'], 0),
   ('If it is currently 10 oclock and 5 hours pass, what time will it be on a 12-hour clock?', ['3 oclock', '15 oclock', '5 oclock', '10 oclock'], 0),
   ('Why might modular arithmetic be useful for describing repeating patterns, such as days of the week?', ['It naturally models cycles that return to a starting point after a fixed number of steps', 'Modular arithmetic can never be used to describe any repeating pattern', 'A concept unrelated to number theory', 'Days of the week never repeat in any predictable pattern'], 0)]),
Sc('Biology: Keystone Species and Ecosystem Stability',
   'Grade 7 Science strand: a keystone species is a species that has a disproportionately large effect on its ecosystem relative to its population size, such that removing it can cause dramatic changes or even collapse in the structure of the entire ecosystem.',
   [('What is a keystone species?', ['A species with a disproportionately large effect on its ecosystem relative to its population size', 'A species that has absolutely no effect on its surrounding ecosystem', 'A concept unrelated to biology', 'A species that only exists in laboratory settings'], 0),
    ('What can happen to an ecosystem if a keystone species is removed?', ['The ecosystem can experience dramatic changes or even collapse', 'The ecosystem always remains completely unchanged', 'A concept unrelated to keystone species', 'Removing any species always improves ecosystem stability'], 0),
    ('Why is a keystone species effect described as disproportionate to its population size?', ['A relatively small population can still have an outsized influence on the rest of the ecosystem', 'Keystone species always have the largest population in their ecosystem', 'A concept unrelated to ecosystem stability', 'Population size has no connection to a species influence on an ecosystem'], 0),
    ('Why might sea otters be described as a keystone species in kelp forest ecosystems?', ['By preying on sea urchins, they help prevent urchins from destroying the kelp that many other species depend on', 'Sea otters have no measurable effect on kelp forest ecosystems', 'A concept unrelated to biology', 'Sea otters are the most numerous species in every kelp forest'], 0),
    ('Why is identifying keystone species useful for conservation efforts?', ['Protecting a keystone species can help preserve the stability of an entire ecosystem', 'Conservation efforts never focus on any particular species within an ecosystem', 'This concept has no relevance to science', 'Keystone species have no connection to conservation planning at all'], 0)]),
SS('Social Studies: The 1919 Paris Peace Conference and Canadas Independent Voice',
   'Grade 7 Social Studies strand: at the Paris Peace Conference following the First World War, Canada, though still legally part of the British Empire, signed the resulting treaty separately and gained its own seat at the League of Nations, marking an early step toward Canadian independence in foreign affairs.',
   [('What major international event followed the First World War, where Canada took part in negotiations?', ['The Paris Peace Conference', 'The Confederation Conference', 'A concept unrelated to Canadian history', 'The Quebec Conference'], 0),
    ('Roughly when did the Paris Peace Conference take place?', ['1919', '1867', 'A concept unrelated to the Paris Peace Conference', '1945'], 0),
    ('What significant step did Canada take at the Paris Peace Conference regarding international recognition?', ['It signed the resulting treaty separately from Britain', 'It refused to participate in the conference at all', 'A concept unrelated to social studies', 'It merged its foreign policy completely with the United States'], 0),
    ('What international organization did Canada gain its own seat in following the conference?', ['The League of Nations', 'The United Nations', 'A concept unrelated to the Paris Peace Conference', 'The Commonwealth Games Federation'], 0),
    ('Why is Canadas separate participation at the Paris Peace Conference considered an early step toward independence in foreign affairs?', ['It showed Canada acting with its own voice in international matters, distinct from Britain', 'Canada had no distinct role of any kind at the conference', 'This concept has no relevance to social studies', 'Independence in foreign affairs has no connection to international conferences'], 0)]),
]),
day(179, [
L('Reading: Analyzing Understatement and Hyperbole as Literary Devices',
  'Grade 7 Language strand: understatement deliberately makes something seem less important or smaller than it really is, often for ironic or humorous effect, while hyperbole is an extreme exaggeration used for emphasis, and skilled writers use both devices to shape how a reader reacts to an idea.',
  [('What is understatement?', ['Deliberately making something seem less important or smaller than it really is', 'Making something seem far more extreme than it really is', 'A concept unrelated to reading', 'Stating a fact with no emotional effect at all'], 0),
   ('What is hyperbole?', ['An extreme exaggeration used for emphasis', 'A statement that downplays the importance of an event', 'A concept unrelated to literary devices', 'A factual statement with no exaggeration of any kind'], 0),
   ('Which sentence is an example of hyperbole?', ['I have told you a million times to clean your room.', 'I have reminded you a few times to clean your room.', 'A concept unrelated to hyperbole', 'Please clean your room today.'], 0),
   ('Which sentence is an example of understatement, describing a huge storm as only mildly inconvenient?', ['It was a bit windy outside during the hurricane.', 'The hurricane was the most destructive storm in a century.', 'A concept unrelated to understatement', 'The storm caused no damage of any kind whatsoever.'], 0),
   ('Why might an author use understatement to describe a serious or dramatic event?', ['It can create an ironic or darkly humorous effect by downplaying something significant', 'Understatement always makes an event sound more dramatic than it really is', 'A concept unrelated to reading', 'Understatement can never be used to create any particular effect'], 0)]),
M('Algebra: Solving Quadratic Equations by Factoring (Intro)',
  'Grade 7 Math strand: some quadratic equations, written in the form x squared plus bx plus c equals zero, can be solved by factoring the expression into two binomials and then setting each factor equal to zero to find the possible values of x.',
  [('What general form does a basic quadratic equation take?', ['x squared plus bx plus c equals zero', 'x plus b equals zero', 'A concept unrelated to algebra', 'x squared equals negative one always'], 0),
   ('What is the first general step in solving a quadratic equation by factoring?', ['Factoring the expression into two binomials', 'Immediately guessing a random value for x with no calculation', 'A concept unrelated to quadratic equations', 'Dividing every term by zero'], 0),
   ('After factoring a quadratic equation into two binomials, what is the next step to find the solutions?', ['Setting each factor equal to zero and solving for x', 'Adding the two binomials together', 'A concept unrelated to factoring', 'Multiplying the two binomials back together and stopping'], 0),
   ('What are the solutions to the equation, the quantity x minus 2 times the quantity x minus 3 equals zero?', ['x equals 2 and x equals 3', 'x equals negative 2 and x equals negative 3', 'x equals 6 only', 'x equals 0 only'], 0),
   ('Why can a basic quadratic equation have up to two different solutions?', ['Setting each of the two factors equal to zero can produce two distinct values of x', 'A quadratic equation can never have more than one solution', 'A concept unrelated to algebra', 'Quadratic equations always have exactly zero solutions'], 0)]),
Sc('Earth Science: Sinkholes, Caves, and Karst Landscapes',
   'Grade 7 Science strand: karst landscapes form when slightly acidic water gradually dissolves soluble bedrock such as limestone, creating underground caves, and when a cave roof becomes too weak to support the ground above, the surface can suddenly collapse, forming a sinkhole.',
   [('What type of bedrock is commonly associated with the formation of karst landscapes?', ['Limestone', 'Granite', 'A concept unrelated to earth science', 'Basalt'], 0),
    ('What causes soluble bedrock to gradually dissolve and form caves?', ['Slightly acidic water dissolving the rock over time', 'Sudden volcanic eruptions melting the bedrock instantly', 'A concept unrelated to karst landscapes', 'Strong winds eroding solid rock from above'], 0),
    ('What can happen when a cave roof becomes too weak to support the ground above it?', ['The surface can suddenly collapse, forming a sinkhole', 'The cave automatically refills with solid rock', 'A concept unrelated to sinkholes', 'The ground above becomes permanently more stable'], 0),
    ('What is a sinkhole?', ['A sudden collapse of the surface into an underground cavity', 'A small pond formed entirely by rainfall', 'A concept unrelated to karst landscapes', 'A type of above-ground mountain formation'], 0),
    ('Why might regions with karst landscapes be more prone to sudden ground collapses than regions with more insoluble bedrock?', ['Soluble rock like limestone can be slowly eroded from below, leaving unstable underground cavities', 'Karst landscapes are always more geologically stable than any other landscape type', 'This concept has no relevance to science', 'Insoluble bedrock is always more likely to dissolve and collapse than soluble bedrock'], 0)]),
SS('Social Studies: The CRTC and Canadian Media Regulation',
   'Grade 7 Social Studies strand: the Canadian Radio-television and Telecommunications Commission, established in 1968, regulates and supervises Canadas broadcasting and telecommunications systems, including setting rules for Canadian content requirements intended to support domestic media and cultural production.',
   [('What does the CRTC stand for?', ['The Canadian Radio-television and Telecommunications Commission', 'The Canadian Rail Transportation Committee', 'A concept unrelated to Canadian institutions', 'The Central Revenue and Tax Collection Council'], 0),
    ('In roughly what year was the CRTC established?', ['1968', '1917', 'A concept unrelated to the CRTC', '1867'], 0),
    ('What two systems does the CRTC regulate and supervise?', ['Broadcasting and telecommunications', 'Only agriculture and fisheries', 'A concept unrelated to social studies', 'Only interprovincial highways'], 0),
    ('What is one purpose of Canadian content requirements set by the CRTC?', ['To support domestic media and cultural production', 'To eliminate all foreign media from being broadcast in Canada', 'A concept unrelated to the CRTC', 'Canadian content rules serve no cultural purpose at all'], 0),
    ('Why might a government create a regulatory body like the CRTC to oversee broadcasting?', ['To help ensure fair access, national standards, and support for domestic content across media systems', 'Broadcasting and telecommunications never require any government oversight', 'This concept has no relevance to social studies', 'Regulatory bodies have no role in supporting cultural production of any kind'], 0)]),
]),
day(180, [
L('Language Review: Grammar, Reading, and Media Literacy (Days 171-179)',
  'Grade 7 Language strand review: students revisit adverb clauses, juxtaposition and contrast, historical fiction narrative writing, personification and anthropomorphism, and understatement and hyperbole.',
  [('What is an adverb clause?', ['A group of words with a subject and verb that functions like an adverb', 'A single word that describes a noun', 'A concept unrelated to grammar', 'A clause that can never begin a sentence'], 0),
   ('What is juxtaposition?', ['Placing two contrasting ideas, characters, or images side by side', 'Repeating the exact same idea multiple times in a row', 'A concept unrelated to reading', 'Removing all conflict from a story'], 0),
   ('What defines historical fiction?', ['A story that blends invented characters and plot with a real historical setting or events', 'A story that must be entirely true and contain no invented details', 'A concept unrelated to writing', 'A story that can only take place in the future'], 0),
   ('What is personification?', ['Giving human qualities to a non-human object or idea', 'Giving an object no qualities of any kind', 'A concept unrelated to reading', 'Removing all descriptive language from a sentence'], 0),
   ('What is understatement?', ['Deliberately making something seem less important or smaller than it really is', 'Making something seem far more extreme than it really is', 'A concept unrelated to reading', 'Stating a fact with no emotional effect at all'], 0)]),
M('Math Review: Systems, Number Theory, and Geometry (Days 171-179)',
  'Grade 7 Math strand review: students revisit solving systems of linear equations by graphing, the Sieve of Eratosthenes, solving absolute value equations, tangent lines and circle theorems, and solving quadratic equations by factoring.',
  [('What does the solution to a system of two linear equations represent on a graph?', ['The point where the two lines intersect', 'The point where either line crosses the x-axis', 'A concept unrelated to algebra', 'The steepness of just one of the lines'], 0),
   ('What is the Sieve of Eratosthenes used to find?', ['All prime numbers up to a given limit', 'The sum of every number in a list', 'A concept unrelated to number theory', 'Only even numbers within a range'], 0),
   ('How many solutions does the equation, the absolute value of x equals 5, generally have?', ['Two solutions, x equals 5 and x equals negative 5', 'Only one solution, x equals 5', 'A concept unrelated to absolute value equations', 'No solutions at all'], 0),
   ('What is the point where a tangent line touches a circle called?', ['The point of tangency', 'The centre of the circle', 'A concept unrelated to tangent lines', 'The diameter point'], 0),
   ('What is the first general step in solving a quadratic equation by factoring?', ['Factoring the expression into two binomials', 'Immediately guessing a random value for x with no calculation', 'A concept unrelated to quadratic equations', 'Dividing every term by zero'], 0)]),
Sc('Science Review: Physics, Biology, and Earth Science (Days 171-179)',
   'Grade 7 Science strand review: students revisit simple harmonic motion, radial and bilateral symmetry, convection currents, keystone species, and sinkholes and karst landscapes.',
   [('What is simple harmonic motion?', ['A repeating back-and-forth motion around a resting position', 'Motion that only ever happens once and never repeats', 'A concept unrelated to physics', 'Motion that always speeds up forever without stopping'], 0),
    ('What is bilateral symmetry?', ['A body plan where the left and right sides mirror each other', 'A body plan where every part of the body is identical in every direction', 'A concept unrelated to animal body plans', 'A body plan that only applies to single-celled organisms'], 0),
    ('What causes a convection current to form?', ['Uneven heating of a fluid, causing warmer material to rise and cooler material to sink', 'A fluid that is heated evenly throughout with no temperature difference', 'A concept unrelated to earth science', 'The complete absence of any heat source'], 0),
    ('What is a keystone species?', ['A species with a disproportionately large effect on its ecosystem relative to its population size', 'A species that has absolutely no effect on its surrounding ecosystem', 'A concept unrelated to biology', 'A species that only exists in laboratory settings'], 0),
    ('What is a sinkhole?', ['A sudden collapse of the surface into an underground cavity', 'A small pond formed entirely by rainfall', 'A concept unrelated to karst landscapes', 'A type of above-ground mountain formation'], 0)]),
SS('Social Studies Review: Geography, History, and Canadian Institutions (Days 171-179)',
   'Grade 7 Social Studies strand review: students revisit the Northwest Passage and Arctic sovereignty, the Doukhobors and Mennonite prairie settlement, the Trans-Canada Highway, the Supreme Court of Canada, and the CRTC.',
   [('What is the Northwest Passage?', ['A sea route through the Canadian Arctic connecting the Atlantic and Pacific Oceans', 'A mountain pass located in British Columbia', 'A concept unrelated to Canadian geography', 'A railway line built across the prairies'], 0),
    ('Where did the Doukhobors and Mennonites primarily settle in Canada?', ['The Canadian prairies', 'The Atlantic coast', 'A concept unrelated to Canadian immigration history', 'Northern Ontario'], 0),
    ('What is the Trans-Canada Highway?', ['One of the longest national highways in the world, stretching coast to coast across Canada', 'A short highway connecting only two Canadian cities', 'A concept unrelated to Canadian infrastructure', 'A railway line built in the 1800s'], 0),
    ('What is the Supreme Court of Canada?', ['The countrys highest court, with the final word on legal disputes', 'A court that only handles minor traffic violations', 'A concept unrelated to Canadian government', 'A court that exists only at the municipal level'], 0),
    ('What does the CRTC stand for?', ['The Canadian Radio-television and Telecommunications Commission', 'The Canadian Rail Transportation Committee', 'A concept unrelated to Canadian institutions', 'The Central Revenue and Tax Collection Council'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_171_180)
    append_to(7, g7_171_180)
