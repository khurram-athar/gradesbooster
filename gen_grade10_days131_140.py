#!/usr/bin/env python3
"""Grade 10, Days 131-140 -- extends Grade 10 from 130 to 140 days. Topics
chosen after grepping the existing Day 1-130 title list (data/grade10.json)
extensively to avoid any overlap: correlative conjunctions, extended
metaphor and conceit, the public service announcement, utopian fiction,
clickbait and the attention economy, absolute phrases, narrative distance,
the abstract and executive summary, and the doppelganger motif; the chain
rule, Fermats Little Theorem, confidence intervals, implicit
differentiation, polar coordinates, the pigeonhole principle, related
rates, Diophantine equations, and the Poisson distribution; osmosis and
diffusion, chromatography, aerodynamics and the physics of flight,
sinkholes and karst topography, vaccines and immunization, water
purification, superconductivity, wetlands, and bioluminescence; the
founding of the North-West Mounted Police, the Naval Aid Bill, the Income
War Tax Act of 1917, the formation of Canadian National Railways, the
founding of the United Church of Canada, the Old Age Pensions Act of 1927,
the Canadian Radio Broadcasting Act and the founding of the CBC,
Newfoundlands Commission of Government, and the founding of the Bank of
Canada.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used anywhere
in title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-120 and 121-130 convention.
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


def _rebalance_answer_positions(days, seed=20260801):
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


g10_131_140 = [
day(131, [
E('Grammar: Correlative Conjunctions',
  'Grade 10 English strand: correlative conjunctions are paired words such as either/or, neither/nor, both/and, and not only/but also that link balanced words, phrases, or clauses within a sentence.',
  [('What is a correlative conjunction?', ['A paired word set that links balanced words, phrases, or clauses', 'A single word that ends a sentence', 'A word that replaces a noun entirely', 'A punctuation mark used in dialogue'], 0),
   ('Which of the following is a correlative conjunction pair?', ['Either/or', 'Run/jump', 'Quickly/slowly', 'Book/pen'], 0),
   ('Which sentence correctly uses a correlative conjunction pair?', ['Neither the teacher nor the students were ready for the test.', 'Neither the teacher or the students were ready for the test.', 'Either the teacher and the students were ready for the test.', 'Both the teacher or the students were ready for the test.'], 0),
   ('Why do correlative conjunctions require parallel structure?', ['The elements joined should match grammatically for the sentence to read smoothly', 'They never need to match in form', 'They only ever join single letters', 'They replace the need for a subject entirely'], 0),
   ('Which pair means both things are true?', ['Both/and', 'Either/or', 'Neither/nor', 'Whether/or'], 0)]),
M('Calculus: The Chain Rule for Derivatives',
  'Grade 10 Math strand: the chain rule provides a method for differentiating a composite function, one function nested inside another, by multiplying the derivative of the outer function by the derivative of the inner function.',
  [('What does the chain rule allow you to differentiate?', ['A composite function, one function nested inside another', 'Only a single constant term', 'Only a sum of two unrelated functions', 'Only whole numbers with no variables'], 0),
   ('How is the chain rule generally applied?', ['By multiplying the derivative of the outer function by the derivative of the inner function', 'By adding the two functions together first', 'By dividing the outer function by the inner function', 'By ignoring the inner function entirely'], 0),
   ('Which type of function most clearly requires the chain rule to differentiate?', ['A composite function such as the square of a trigonometric expression', 'A single constant with no variable', 'A simple linear function like y equals x', 'A function with no inner expression at all'], 0),
   ('The chain rule builds directly on which earlier differentiation rules?', ['The power rule and the basic derivative rules', 'Only the Pythagorean Theorem', 'Only the quadratic formula', 'Only basic arithmetic with no calculus involved'], 0),
   ('Why is the chain rule essential in calculus?', ['Many real functions are composite functions that cannot be differentiated with simpler rules alone', 'It eliminates the need for the power rule entirely', 'It only applies to functions with no variables', 'It replaces the need to ever find a derivative'], 0)]),
Sc('Biology: Osmosis, Diffusion, and Cell Transport',
   'Grade 10 Science strand: diffusion is the movement of particles from an area of higher concentration to lower concentration, and osmosis is the specific diffusion of water across a semi-permeable membrane, both essential processes for moving materials into and out of cells.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles only against a concentration gradient', 'A process that occurs only in solids', 'A process requiring the cell to use energy at all times'], 0),
    ('What is osmosis?', ['The diffusion of water across a semi-permeable membrane', 'The diffusion of solid particles through a rigid wall', 'A process that only occurs in the absence of water', 'The movement of proteins out of a cell'], 0),
    ('What property of a cell membrane allows osmosis to occur?', ['It is semi-permeable, allowing water but not all solutes through', 'It is completely impermeable to everything', 'It allows every substance through equally', 'It has no effect on which substances pass through'], 0),
    ('What happens to a cell placed in a highly concentrated salt solution?', ['Water tends to leave the cell, causing it to shrink', 'Water tends to enter the cell rapidly with no limit', 'The cell membrane instantly dissolves', 'No water movement occurs under any condition'], 0),
    ('Why are diffusion and osmosis important to living cells?', ['They allow essential materials like nutrients and water to move into and out of cells', 'They prevent cells from ever exchanging any materials', 'They are only relevant to non-living matter', 'They stop all cellular processes from occurring'], 0)]),
H('The Founding of the North-West Mounted Police in 1873',
  'Grade 10 History strand: the North-West Mounted Police was established in 1873 by the Canadian government to maintain order, assert Canadian sovereignty, and regulate relations with Indigenous peoples and settlers across the newly acquired western territories.',
  [('In what year was the North-West Mounted Police established?', ['1873', '1867', '1905', '1949'], 0),
   ('Why did the Canadian government establish the North-West Mounted Police?', ['To maintain order and assert Canadian sovereignty over the western territories', 'To defend against an invasion from the United States', 'To replace the entire federal parliament', 'To administer the province of Quebec exclusively'], 0),
   ('What present-day Canadian institution evolved from the North-West Mounted Police?', ['The Royal Canadian Mounted Police', 'The Canadian Armed Forces', 'The Supreme Court of Canada', 'The Bank of Canada'], 0),
   ('The North-West Mounted Police was tasked with regulating relations between settlers and ___.', ['Indigenous peoples across the western territories', 'Foreign diplomats in Ottawa', 'Provincial legislatures in the east', 'International shipping companies'], 0),
   ('The founding of the North-West Mounted Police is often studied alongside which other western expansion topic?', ['The settlement of the Canadian Prairies', 'The Halifax Explosion', 'The Quebec Referendum of 1995', 'The Suez Crisis'], 0)]),
]),
day(132, [
E('Reading: Analyzing Extended Metaphor and Conceit',
  'Grade 10 English strand: an extended metaphor sustains a single comparison across multiple lines or an entire text, and a conceit is an especially elaborate or unconventional extended metaphor that develops a surprising connection between two very different things.',
  [('What is an extended metaphor?', ['A single comparison sustained across multiple lines or an entire text', 'A comparison that lasts only a single word', 'A metaphor that uses like or as', 'A metaphor that is stated only once and never returned to'], 0),
   ('What is a conceit in literary terms?', ['An especially elaborate or unconventional extended metaphor', 'A short simile used only once', 'A grammatical error in a poem', 'A type of rhyme scheme'], 0),
   ('Why might a poet choose an extended metaphor over a simple comparison?', ['It allows the writer to develop a comparison in greater depth and complexity', 'It forces the writer to abandon the comparison after one line', 'It removes any figurative meaning from the text', 'It eliminates the need for imagery entirely'], 0),
   ('What makes a conceit feel surprising to a reader?', ['It connects two very different things in an unexpected way', 'It only compares extremely similar things', 'It avoids any figurative language', 'It restates the literal meaning directly'], 0),
   ('Extended metaphors and conceits are most useful for ___.', ['Deepening a texts thematic meaning through a sustained comparison', 'Simplifying a text to a single literal statement', 'Removing all imagery from a poem', 'Replacing dialogue in a narrative'], 0)]),
M('Number Theory: Fermats Little Theorem',
  'Grade 10 Math strand: Fermats Little Theorem states that if p is a prime number, then for any integer a not divisible by p, a raised to the power of p minus 1 is congruent to 1 modulo p, a result with important applications in modular arithmetic and cryptography.',
  [('What condition must p satisfy in Fermats Little Theorem?', ['p must be a prime number', 'p must be a perfect square', 'p must be an even number only', 'p must be equal to zero'], 0),
   ('What does Fermats Little Theorem state about a raised to the power p minus 1?', ['It is congruent to 1 modulo p, when a is not divisible by p', 'It always equals exactly p', 'It is always equal to zero', 'It is never a whole number'], 0),
   ('Fermats Little Theorem builds on which earlier number theory concept?', ['Modular arithmetic', 'The quadratic formula', 'The Pythagorean Theorem', 'Basic long division only'], 0),
   ('What modern field commonly applies Fermats Little Theorem?', ['Cryptography and computer security', 'Ancient astronomy with no modern use', 'Elementary counting with no further application', 'Basic geometry with no numbers involved'], 0),
   ('Why is the condition that a is not divisible by p important in the theorem?', ['Without it, the congruence relationship described by the theorem does not hold', 'It has no effect on the theorem at all', 'It only matters when p is not prime', 'It applies only when a equals zero'], 0)]),
Sc('Chemistry: Chromatography and Separation Techniques',
   'Grade 10 Science strand: chromatography is a laboratory technique used to separate the components of a mixture based on how differently each component travels through a stationary medium carried by a moving solvent, revealing the number and identity of substances present.',
   [('What is the main purpose of chromatography?', ['To separate the components of a mixture', 'To combine several substances into a single compound', 'To measure the temperature of a solution', 'To determine the mass of a solid object'], 0),
    ('What causes different components to separate during chromatography?', ['Each component travels a different distance through the stationary medium at a different rate', 'All components always travel at exactly the same rate', 'Components separate only by changing colour randomly', 'Separation occurs due to gravity alone with no medium involved'], 0),
    ('What carries the mixture through the stationary medium in chromatography?', ['A moving solvent', 'A block of ice', 'A magnetic field', 'A beam of light only'], 0),
    ('What can scientists learn from a completed chromatography experiment?', ['The number and identity of substances present in a mixture', 'The exact temperature of the room', 'The atomic number of every element involved', 'The electrical charge of the container'], 0),
    ('Chromatography is commonly used in which real-world application?', ['Forensic analysis of ink or drug samples', 'Measuring the speed of a moving vehicle', 'Calculating the area of a triangle', 'Predicting tomorrows weather'], 0)]),
H('The Naval Aid Bill and Canadas Pre-World War I Naval Debate',
  'Grade 10 History strand: the Naval Aid Bill of 1912-13, proposed by Prime Minister Robert Borden to fund British dreadnoughts directly rather than build a Canadian navy, sparked a bitter national debate over Canadas military relationship with Britain and was ultimately defeated in the Senate.',
  [('Who proposed the Naval Aid Bill?', ['Prime Minister Robert Borden', 'Prime Minister Mackenzie King', 'Prime Minister Wilfrid Laurier', 'Prime Minister Lester Pearson'], 0),
   ('What did the Naval Aid Bill propose to fund?', ['British dreadnoughts directly instead of building a Canadian navy', 'A new Canadian air force', 'The construction of the Canadian Pacific Railway', 'A national system of highways'], 0),
   ('What ultimately happened to the Naval Aid Bill?', ['It was defeated in the Senate', 'It passed unanimously in Parliament', 'It was approved directly by the King', 'It was never debated at all'], 0),
   ('What broader issue did the Naval Aid Bill debate reflect?', ['Disagreement over Canadas military relationship with Britain', 'A dispute over provincial boundaries', 'A conflict over railway construction routes', 'A disagreement over agricultural tariffs only'], 0),
   ('The Naval Aid Bill debate occurred in the years immediately before which major conflict?', ['World War I', 'World War II', 'The Korean War', 'The Boer War'], 0)]),
]),
day(133, [
E('Writing: The Public Service Announcement',
  'Grade 10 English strand: a public service announcement, or PSA, is a brief persuasive message designed to inform or influence public behaviour on an issue of social importance, using a clear call to action, a defined target audience, and a concise, memorable structure.',
  [('What is the primary purpose of a public service announcement?', ['To inform or influence public behaviour on an issue of social importance', 'To sell a specific commercial product', 'To entertain readers with unrelated fiction', 'To provide a lengthy academic analysis'], 0),
   ('What is an essential feature of an effective PSA?', ['A clear call to action for the audience', 'A complete absence of any purpose', 'An extremely long and detailed narrative', 'A focus on private, unrelated matters'], 0),
   ('Why must a PSA writer define a target audience?', ['To tailor the language, tone, and message to the people most likely to act on it', 'Because a PSA should never be shown to anyone', 'Because a target audience is irrelevant to persuasive writing', 'Because PSAs are never meant to be understood'], 0),
   ('Which of the following is a typical topic for a PSA?', ['Encouraging safe driving habits', 'Reviewing a recent novel', 'Summarizing a historical battle', 'Explaining a mathematical proof'], 0),
   ('Why do PSAs typically use concise, memorable language?', ['To ensure the message is retained and easily understood by a broad audience', 'To make the message as confusing as possible', 'Because concise writing has no persuasive value', 'Because PSAs are always read privately with no time limit'], 0)]),
M('Statistics: Confidence Intervals and Margin of Error',
  'Grade 10 Math strand: a confidence interval is a range of values, calculated from sample data, that is likely to contain the true population parameter, with the margin of error indicating how much the sample estimate might differ from that true value.',
  [('What does a confidence interval estimate?', ['A range of values likely to contain the true population parameter', 'The exact value of a population parameter with total certainty', 'A single number with no range at all', 'The size of a sample only'], 0),
   ('What does the margin of error indicate?', ['How much a sample estimate might differ from the true population value', 'The exact size of the entire population', 'Whether a hypothesis test was conducted correctly', 'The colour used in a data visualization'], 0),
   ('How does increasing the sample size typically affect the margin of error?', ['It generally decreases the margin of error', 'It always increases the margin of error', 'It has no effect on the margin of error', 'It makes the margin of error undefined'], 0),
   ('A 95 percent confidence level means ___.', ['We expect about 95 percent of similarly constructed intervals to contain the true value', 'The result is true with absolute certainty', 'Only 5 percent of the data was collected', 'The sample size must always be exactly 95'], 0),
   ('Confidence intervals are commonly used alongside which other statistical concept?', ['Hypothesis testing', 'The Pythagorean Theorem', 'The quadratic formula', 'Basic long division'], 0)]),
Sc('Physics: Aerodynamics and the Physics of Flight',
   'Grade 10 Science strand: aerodynamics studies how air interacts with moving objects, and flight depends on four key forces, lift, weight, thrust, and drag, with an aircrafts wing shape generating lift by causing air to move faster over the curved upper surface.',
   [('What are the four key forces involved in flight?', ['Lift, weight, thrust, and drag', 'Only gravity and friction', 'Only speed and mass', 'Only temperature and pressure'], 0),
    ('What force allows an aircraft to overcome gravity and rise?', ['Lift', 'Drag', 'Weight', 'Density'], 0),
    ('How does a typical wing shape help generate lift?', ['It causes air to move faster over the curved upper surface, lowering pressure above the wing', 'It blocks all airflow around the wing completely', 'It has no effect on the airflow at all', 'It only works when the aircraft is stationary'], 0),
    ('What force acts opposite to thrust during flight?', ['Drag', 'Lift', 'Weight', 'Density'], 0),
    ('Why do engineers study aerodynamics when designing aircraft?', ['To maximize lift and minimize drag for efficient, stable flight', 'To make aircraft as heavy as possible', 'To eliminate the need for any wings', 'To increase drag as much as possible'], 0)]),
H('The Income War Tax Act of 1917',
  'Grade 10 History strand: the Income War Tax Act of 1917 introduced a federal personal income tax in Canada as a temporary wartime measure to help fund Canadas participation in World War I, though the tax was never repealed and became a permanent feature of Canadian federal finances.',
  [('In what year was the Income War Tax Act passed?', ['1917', '1867', '1949', '1905'], 0),
   ('What was the original stated purpose of the Income War Tax Act?', ['A temporary wartime measure to help fund Canadas participation in World War I', 'A permanent replacement for all provincial taxes', 'A tax designed to fund the Canadian Pacific Railway', 'A tax created to fund Confederation celebrations'], 0),
   ('What happened to the income tax after World War I ended?', ['It was never repealed and became a permanent feature of federal finances', 'It was immediately cancelled once the war ended', 'It was transferred entirely to provincial governments', 'It was replaced by a sales tax only'], 0),
   ('What type of tax did the Income War Tax Act introduce federally?', ['A personal income tax', 'A tax on imported goods only', 'A property tax on farmland only', 'A tax on foreign travel only'], 0),
   ('The Income War Tax Act is often studied as an example of ___.', ['A wartime emergency measure that became a lasting government policy', 'A policy with no lasting effect on Canada', 'A tax that was ruled unconstitutional', 'A measure that only applied to Quebec'], 0)]),
]),
day(134, [
E('Literature: Utopian Fiction and Ideal Societies',
  'Grade 10 English strand: utopian fiction imagines a society organized around an ideal system of government, technology, or social values, often used by authors to explore what a better world might look like while implicitly critiquing the flaws of contemporary society.',
  [('What does utopian fiction typically imagine?', ['A society organized around an ideal system of government or social values', 'A society with no organization of any kind', 'A world with no characters or setting', 'A purely factual historical account'], 0),
   ('How does utopian fiction differ from dystopian fiction?', ['Utopian fiction presents an idealized society, while dystopian fiction presents a flawed or oppressive one', 'The two genres are identical with no differences', 'Utopian fiction always avoids any social commentary', 'Dystopian fiction always presents a perfect society'], 0),
   ('Why might an author write utopian fiction?', ['To explore what a better world might look like and implicitly critique present society', 'To avoid making any statement about society', 'To provide a purely factual scientific report', 'To eliminate the need for any imaginative elements'], 0),
   ('Which of the following might a utopian novel explore?', ['An imagined system of governance believed to solve real social problems', 'Only a detailed description of weather patterns', 'Only a biography of a historical figure', 'Only a list of unrelated statistics'], 0),
   ('Utopian fiction is often discussed alongside which related genre?', ['Dystopian fiction', 'Epistolary fiction', 'Detective fiction', 'Historical fiction exclusively'], 0)]),
M('Calculus: Implicit Differentiation',
  'Grade 10 Math strand: implicit differentiation is a technique for finding the derivative of a relation in which y is not isolated as a function of x, by differentiating both sides of an equation with respect to x and applying the chain rule to terms involving y.',
  [('When is implicit differentiation typically used?', ['When y is not isolated as a function of x in an equation', 'Only when an equation has no variables at all', 'Only when a function is already fully simplified for y', 'Only when working with whole numbers'], 0),
   ('What technique is applied to terms involving y during implicit differentiation?', ['The chain rule', 'The Pythagorean Theorem', 'The quadratic formula', 'Basic long division'], 0),
   ('What is the general first step in implicit differentiation?', ['Differentiating both sides of the equation with respect to x', 'Solving the equation for y before differentiating anything', 'Ignoring one side of the equation entirely', 'Substituting a specific numerical value for x first'], 0),
   ('Why is implicit differentiation useful for curves like circles?', ['Such curves are not easily written as a single function of x, so implicit methods are needed', 'Circles never have a defined derivative', 'Implicit differentiation only works for straight lines', 'Circles require no differentiation at all'], 0),
   ('Implicit differentiation is closely related to which other calculus rule?', ['The chain rule', 'The Fundamental Theorem of Arithmetic', 'The Binomial Theorem', 'The Euclidean Algorithm'], 0)]),
Sc('Earth Science: Sinkholes and Karst Topography',
   'Grade 10 Science strand: karst topography forms when slightly acidic groundwater slowly dissolves soluble bedrock such as limestone, creating underground caves and channels that can collapse suddenly to form sinkholes at the surface.',
   [('What type of bedrock is most associated with karst topography?', ['Soluble rock such as limestone', 'Solid granite with no soluble minerals', 'Metallic ore deposits only', 'Volcanic ash with no groundwater involved'], 0),
    ('What causes karst landscapes to form over time?', ['Slightly acidic groundwater slowly dissolving soluble bedrock', 'Sudden volcanic eruptions', 'Rapid freezing of surface water', 'Wind erosion of sand dunes only'], 0),
    ('What often forms underground in karst regions before a sinkhole appears?', ['Caves and channels created by dissolved rock', 'Layers of solid ice', 'Large deposits of coal', 'A permanent lake with no connection to the surface'], 0),
    ('What is a sinkhole?', ['A surface depression formed when underground rock collapses', 'A type of volcanic mountain', 'A permanent structure built by humans', 'A large body of standing ocean water'], 0),
    ('Why can sinkholes form suddenly and pose a hazard?', ['Underground erosion can weaken rock until it can no longer support the surface above it', 'Sinkholes always form gradually over centuries with visible warning signs', 'Sinkholes have no connection to underground rock structure', 'Sinkholes only occur in areas with no groundwater at all'], 0)]),
H('The Formation of Canadian National Railways in 1919',
  'Grade 10 History strand: Canadian National Railways was formed in 1919 when the federal government consolidated several financially struggling private railway companies into a single publicly owned corporation, creating a major state-run competitor to the privately owned Canadian Pacific Railway.',
  [('In what year was Canadian National Railways formed?', ['1919', '1867', '1885', '1949'], 0),
   ('Why did the federal government create Canadian National Railways?', ['To consolidate several financially struggling private railway companies into one public corporation', 'To replace the Canadian Pacific Railway entirely and shut it down', 'To build the first railway ever constructed in Canada', 'To transfer all rail service to the United States'], 0),
   ('What type of ownership did Canadian National Railways represent?', ['Public, government-owned ownership', 'Entirely private, shareholder-only ownership', 'Ownership by a foreign government', 'Ownership by a single individual investor'], 0),
   ('Canadian National Railways became a major competitor to which existing railway?', ['The Canadian Pacific Railway', 'The Grand Trunk Pacific Railway exclusively with no other rivals', 'The Trans-Canada Highway', 'The St. Lawrence Seaway'], 0),
   ('What economic condition among private railways led to the creation of Canadian National Railways?', ['Several private railway companies were in serious financial difficulty', 'All private railways were extremely profitable with no need for support', 'There were no private railways operating in Canada at the time', 'Private railways had already been fully nationalized decades earlier'], 0)]),
]),
day(135, [
E('Media Literacy: Clickbait and the Attention Economy',
  'Grade 10 English strand: clickbait refers to headlines or content designed primarily to attract clicks rather than to inform accurately, a strategy shaped by the attention economy, in which media companies compete for limited audience attention often at the expense of depth or accuracy.',
  [('What is clickbait?', ['Headlines or content designed primarily to attract clicks rather than inform accurately', 'A type of formal citation used in academic essays', 'A method of fact-checking a news article', 'A grammatical structure used in headlines only'], 0),
   ('What is the attention economy?', ['A system in which media companies compete for limited audience attention', 'An economic system based only on physical currency', 'A method of teaching mathematics', 'A style of formal academic writing'], 0),
   ('Why might clickbait sacrifice accuracy?', ['Its main goal is to generate clicks, which can come at the expense of depth or accuracy', 'Clickbait always prioritizes factual accuracy above all else', 'Clickbait has no relationship to how content is written', 'Clickbait never uses headlines of any kind'], 0),
   ('What is one strategy for identifying clickbait headlines?', ['Noticing exaggerated or vague language designed to provoke curiosity', 'Assuming every headline is completely accurate', 'Ignoring the headline and reading only the images', 'Assuming clickbait never appears on social media'], 0),
   ('Why is understanding the attention economy important for media literacy?', ['It helps readers recognize how content is designed to capture and hold their attention', 'It has no relevance to how people consume media', 'It only applies to printed newspapers from the past', 'It guarantees that all online content is trustworthy'], 0)]),
M('Geometry: An Introduction to Polar Coordinates',
  'Grade 10 Math strand: the polar coordinate system locates a point using a distance from a fixed origin and an angle from a fixed direction, rather than the horizontal and vertical distances used in the Cartesian system, offering a natural way to describe curves with rotational symmetry.',
  [('What two values define a point in the polar coordinate system?', ['A distance from the origin and an angle from a fixed direction', 'Two perpendicular horizontal and vertical distances only', 'Three separate coordinate values', 'A single value with no direction involved'], 0),
   ('How does the polar coordinate system differ from the Cartesian system?', ['It uses distance and angle instead of horizontal and vertical distances', 'It uses only negative numbers', 'It cannot represent any curves at all', 'It is identical to the Cartesian system in every way'], 0),
   ('What is the fixed reference point in the polar coordinate system called?', ['The pole, or origin', 'The vertex of a triangle', 'The y-intercept', 'The slope'], 0),
   ('Polar coordinates are especially useful for describing which type of curve?', ['Curves with rotational symmetry, such as spirals or circles', 'Only straight vertical lines', 'Only straight horizontal lines', 'Only single isolated points with no curve at all'], 0),
   ('The angle in a polar coordinate is typically measured from ___.', ['The positive horizontal axis', 'The negative vertical axis only', 'A randomly chosen point with no fixed reference', 'The center of the y-axis only'], 0)]),
Sc('Biology: Vaccines and Immunization',
   'Grade 10 Science strand: a vaccine introduces a weakened, inactivated, or partial form of a pathogen into the body, training the immune system to recognize and respond quickly to that pathogen in the future without causing the actual disease.',
   [('What does a vaccine typically introduce into the body?', ['A weakened, inactivated, or partial form of a pathogen', 'A fully active, disease-causing pathogen at full strength', 'A completely unrelated substance with no biological effect', 'Only antibiotics with no connection to pathogens'], 0),
    ('What is the main goal of vaccination?', ['To train the immune system to recognize and respond quickly to a specific pathogen', 'To immediately cause the full disease in every recipient', 'To eliminate the need for an immune system entirely', 'To weaken the immune system permanently'], 0),
    ('How does the immune system typically respond after vaccination?', ['It produces memory cells that allow a faster response upon future exposure', 'It forgets the pathogen immediately after exposure', 'It becomes permanently unable to respond to any pathogen', 'It attacks only healthy body cells instead'], 0),
    ('Why do vaccines not typically cause the full disease they protect against?', ['They use a weakened, inactivated, or partial form of the pathogen rather than the full active version', 'They always contain the complete, fully active pathogen', 'Vaccines have no connection to the pathogen at all', 'Vaccines only work after a person has already recovered from the disease'], 0),
    ('What public health benefit can widespread vaccination provide to a community?', ['Reduced spread of disease through increased population immunity', 'An immediate increase in disease transmission', 'No measurable effect on disease spread', 'A guaranteed elimination of all diseases instantly'], 0)]),
H('The Formation of the United Church of Canada in 1925',
  'Grade 10 History strand: the United Church of Canada was formed in 1925 through the union of the Methodist, Congregationalist, and most Presbyterian churches in Canada, creating the largest Protestant denomination in the country and reflecting a broader movement toward Canadian religious and institutional independence.',
  [('In what year was the United Church of Canada formed?', ['1925', '1867', '1905', '1949'], 0),
   ('Which churches united to form the United Church of Canada?', ['The Methodist, Congregationalist, and most Presbyterian churches', 'The Catholic and Anglican churches', 'The Baptist and Lutheran churches only', 'A union of every religious denomination in Canada'], 0),
   ('What did the United Church of Canada become after its formation?', ['The largest Protestant denomination in the country', 'A small, minor religious group with few members', 'An officially government-run institution', 'A branch of the Catholic Church'], 0),
   ('The formation of the United Church of Canada reflected a broader trend toward ___.', ['Canadian religious and institutional independence', 'Continued dependence on British religious authority', 'The elimination of all religious institutions in Canada', 'A merger with an American religious denomination'], 0),
   ('Which decade saw the formation of the United Church of Canada?', ['The 1920s', 'The 1860s', 'The 1940s', 'The 1980s'], 0)]),
]),
day(136, [
E('Grammar: Absolute Phrases',
  'Grade 10 English strand: an absolute phrase consists of a noun followed by a participle or modifier and describes the surrounding sentence as a whole rather than modifying a single word, adding vivid detail without forming a complete independent clause.',
  [('What does an absolute phrase typically consist of?', ['A noun followed by a participle or modifier', 'A verb followed directly by a conjunction', 'A single adjective with no noun', 'A complete independent clause only'], 0),
   ('What does an absolute phrase usually modify?', ['The entire sentence rather than a single word', 'Only a single pronoun', 'Only a preposition', 'Nothing at all within the sentence'], 0),
   ('Which sentence contains an absolute phrase?', ['Her hands trembling, she opened the letter slowly.', 'She opened the letter slowly.', 'She opened the letter because she was curious.', 'The letter, which arrived yesterday, was opened.'], 0),
   ('Why might a writer use an absolute phrase?', ['To add vivid, specific detail without forming a full independent clause', 'To avoid using any nouns in a sentence', 'To replace the main verb of the sentence entirely', 'To make the sentence grammatically incomplete on purpose'], 0),
   ('How is an absolute phrase typically set off in a sentence?', ['With a comma separating it from the rest of the sentence', 'With no punctuation of any kind', 'With a semicolon connecting two full clauses', 'With a colon introducing a formal list'], 0)]),
M('Discrete Math: The Pigeonhole Principle',
  'Grade 10 Math strand: the pigeonhole principle states that if more items are placed into containers than there are containers, at least one container must hold more than one item, a simple idea with surprisingly powerful applications in proofs and problem solving.',
  [('What does the pigeonhole principle state?', ['If more items are placed into containers than there are containers, at least one container holds more than one item', 'Every container must hold exactly one item at all times', 'No container can ever hold more than one item', 'The number of items must always equal the number of containers'], 0),
   ('What is required for the pigeonhole principle to guarantee a container with multiple items?', ['The number of items must exceed the number of containers', 'The number of items must be exactly equal to the number of containers', 'The number of containers must exceed the number of items', 'There must be zero items in total'], 0),
   ('The pigeonhole principle is especially useful for ___.', ['Proving that a certain outcome must occur without needing to check every case', 'Measuring the exact area of a shape', 'Calculating a derivative directly', 'Finding the exact probability of a single event'], 0),
   ('Which scenario illustrates the pigeonhole principle?', ['If 13 people are in a room, at least two must share a birth month', 'If 12 people are in a room, each must have a different birth month', 'If zero people are in a room, two must share a birth month', 'The principle only applies to numbers larger than one million'], 0),
   ('Why is the pigeonhole principle considered powerful despite its simplicity?', ['It can prove certain results must be true without exhaustively checking every possibility', 'It requires checking every single case individually with no shortcuts', 'It only applies to geometry problems', 'It has no real mathematical applications'], 0)]),
Sc('Chemistry: Water Purification and Treatment',
   'Grade 10 Science strand: water purification uses physical and chemical processes such as filtration, coagulation, and disinfection to remove contaminants, pathogens, and particulates from water, making it safe for human consumption and other uses.',
   [('What is the main goal of water purification?', ['To remove contaminants, pathogens, and particulates from water', 'To add as many impurities to water as possible', 'To convert all water into a solid state', 'To eliminate water entirely from a supply system'], 0),
    ('What process uses a physical barrier to remove larger particles from water?', ['Filtration', 'Combustion', 'Sublimation', 'Titration'], 0),
    ('What is coagulation used for in water treatment?', ['Clumping together small particles so they can be more easily removed', 'Adding colour to clear water', 'Removing all oxygen from the water supply', 'Increasing the temperature of the water rapidly'], 0),
    ('What is the purpose of disinfection in water treatment?', ['To kill or inactivate harmful pathogens in the water', 'To make the water less safe to drink', 'To add more bacteria to the water supply', 'To remove all minerals from the water permanently'], 0),
    ('Why is safe drinking water treatment important for public health?', ['It helps prevent the spread of waterborne diseases', 'It has no effect on human health at all', 'It always increases the risk of illness', 'It is only relevant in areas with no population'], 0)]),
H('The Old Age Pensions Act of 1927',
  'Grade 10 History strand: the Old Age Pensions Act of 1927 established Canadas first federal old age pension program, providing modest, means-tested financial support to low-income seniors and marking an early step toward the modern Canadian social welfare system.',
  [('In what year was the Old Age Pensions Act passed?', ['1927', '1867', '1949', '1905'], 0),
   ('What did the Old Age Pensions Act establish?', ['Canadas first federal old age pension program', 'A national healthcare system for all Canadians', 'A federal minimum wage law', 'A national unemployment insurance program'], 0),
   ('Who was eligible to receive support under the original Old Age Pensions Act?', ['Low-income seniors, based on a means test', 'All Canadians regardless of age or income', 'Only wealthy retired business owners', 'Only federal government employees'], 0),
   ('The Old Age Pensions Act is considered an early step toward what broader system?', ['The modern Canadian social welfare system', 'The Canadian military justice system', 'The provincial court system', 'The Canadian tax appeals system'], 0),
   ('What term describes a program that provides benefits based on an applicants income level?', ['Means-tested', 'Universally funded with no conditions', 'Privately insured only', 'Available only to corporations'], 0)]),
]),
day(137, [
E('Reading: Analyzing Narrative Distance and Psychic Distance',
  'Grade 10 English strand: narrative distance, sometimes called psychic distance, describes how close or removed a narrator feels from a characters inner thoughts and emotions, ranging from an intimate, close perspective to a detached, observational one.',
  [('What does narrative distance describe?', ['How close or removed a narrator feels from a characters inner thoughts and emotions', 'The physical distance between two settings in a story', 'The number of pages in a chapter', 'The time period in which a story is set'], 0),
   ('What is another common term for narrative distance?', ['Psychic distance', 'Plot structure', 'Rising action', 'Dramatic irony'], 0),
   ('What characterizes a close narrative distance?', ['An intimate perspective that closely follows a characters inner thoughts and feelings', 'A perspective with no connection to any character at all', 'A narrator who never describes any emotion', 'A viewpoint that only reports distant historical facts'], 0),
   ('What characterizes a far or detached narrative distance?', ['A more observational, removed perspective on events and characters', 'An extremely close, intimate view of a single characters emotions', 'A total absence of any narration', 'A perspective that only exists in dialogue'], 0),
   ('Why might an author shift narrative distance within a text?', ['To control how intimately readers connect with a character at different moments', 'To confuse readers with no clear purpose', 'To remove the narrator from the story entirely', 'To eliminate the need for a plot'], 0)]),
M('Calculus: Related Rates',
  'Grade 10 Math strand: related rates problems use implicit differentiation to determine how the rate of change of one quantity relates to the rate of change of another quantity, when both are connected by an equation and changing with respect to time.',
  [('What do related rates problems determine?', ['How the rate of change of one quantity relates to the rate of change of another', 'The exact value of a single unrelated quantity', 'Only the area of a fixed, unchanging shape', 'The colour of an object in a diagram'], 0),
   ('What technique is central to solving related rates problems?', ['Implicit differentiation with respect to time', 'Basic addition of two constants', 'Simple counting with no equations involved', 'Measuring an object directly with a ruler only'], 0),
   ('In a related rates problem, quantities are typically connected by ___.', ['An equation relating the two changing quantities', 'No mathematical relationship at all', 'A relationship that never changes over time', 'A relationship involving only whole numbers'], 0),
   ('Why is time often the variable with respect to which related rates are differentiated?', ['Because the quantities involved are described as changing over time', 'Because time never appears in these problems', 'Because related rates problems never involve change', 'Because time is always held constant in these problems'], 0),
   ('A classic example of a related rates problem involves ___.', ['Finding how fast the radius of a balloon increases as it is inflated', 'Finding the exact colour of a balloon', 'Counting the total number of balloons in a room', 'Measuring the weight of a balloon at rest'], 0)]),
Sc('Physics: Superconductivity and Zero Electrical Resistance',
   'Grade 10 Science strand: superconductivity is a phenomenon in which certain materials, when cooled below a critical temperature, conduct electricity with zero electrical resistance, allowing current to flow without energy loss and enabling powerful applications like magnetic levitation.',
   [('What defines a superconducting material?', ['It conducts electricity with zero electrical resistance below a critical temperature', 'It always resists electrical current completely at every temperature', 'It never conducts electricity under any condition', 'It only conducts electricity at extremely high temperatures'], 0),
    ('What condition must typically be met for a material to become superconducting?', ['The material must be cooled below a critical temperature', 'The material must be heated to an extremely high temperature', 'The material must be exposed to direct sunlight', 'The material must be placed in a vacuum with no other conditions'], 0),
    ('What happens to electrical energy loss in a superconductor carrying current?', ['Energy loss from resistance is eliminated', 'Energy loss increases dramatically', 'Energy loss remains exactly the same as in a normal conductor', 'All electrical energy is instantly converted to heat'], 0),
    ('Which application relies on the properties of superconductivity?', ['Magnetic levitation systems', 'Ordinary incandescent light bulbs', 'Basic wooden furniture construction', 'Simple mechanical pulleys with no electricity involved'], 0),
    ('Why is superconductivity considered scientifically significant?', ['It allows electrical current to flow without the energy losses seen in normal conductors', 'It has no practical or scientific significance at all', 'It only occurs in materials that cannot conduct electricity', 'It eliminates the need for electricity entirely'], 0)]),
H('The Canadian Radio Broadcasting Act and the Founding of the CBC',
  'Grade 10 History strand: the Canadian Radio Broadcasting Act of 1932 created a national public broadcaster to counter growing American radio influence and unify the country through shared programming, a role later expanded when the Canadian Broadcasting Corporation was formally established in 1936.',
  [('What did the Canadian Radio Broadcasting Act of 1932 create?', ['A national public broadcaster', 'A new national police force', 'A national railway system', 'A federal income tax'], 0),
   ('Why did the federal government establish a national public broadcaster?', ['To counter growing American radio influence and unify the country through shared programming', 'To eliminate all radio broadcasting in Canada permanently', 'To transfer all broadcasting control to private American companies', 'To fund the construction of a national railway'], 0),
   ('In what year was the Canadian Broadcasting Corporation formally established?', ['1936', '1867', '1905', '1949'], 0),
   ('What common national concern motivated the creation of a public broadcaster in the 1930s?', ['Concern that American radio signals were dominating Canadian audiences', 'A shortage of newspapers across the country', 'A lack of any interest in radio technology', 'A dispute over provincial voting rights'], 0),
   ('The founding of the CBC reflects a broader theme of which era in Canadian history?', ['Efforts to strengthen Canadian cultural identity and institutions', 'The complete rejection of all modern technology', 'The end of federal government involvement in communications', 'A return to exclusively British-run institutions'], 0)]),
]),
day(138, [
E('Writing: The Abstract and Executive Summary',
  'Grade 10 English strand: an abstract or executive summary is a concise overview placed at the start of a longer document that summarizes its purpose, key findings, and conclusions, allowing readers to quickly understand the content without reading the entire text.',
  [('What is the main purpose of an abstract or executive summary?', ['To provide a concise overview of a longer documents purpose, findings, and conclusions', 'To replace the entire document with no other content needed', 'To provide a detailed, page-by-page retelling of the document', 'To introduce unrelated information not found in the document'], 0),
   ('Where is an abstract or executive summary typically placed in a document?', ['At the start of the document', 'Only in a footnote at the very end', 'Scattered randomly throughout the middle of the text', 'Only in a separate, unrelated document'], 0),
   ('Why do readers value a well-written abstract or executive summary?', ['It allows them to quickly understand the content without reading the entire text', 'It forces them to read the full document twice', 'It removes the need for the document to have any conclusion', 'It intentionally omits the main purpose of the document'], 0),
   ('Which of the following should typically be included in an abstract?', ['The key findings and conclusions of the document', 'Only unrelated personal opinions', 'A list of every sentence in the original document', 'Advertisements unrelated to the documents topic'], 0),
   ('Why should an abstract or executive summary be concise?', ['So readers can grasp the essential content efficiently before deciding to read further', 'Because concise writing has no value in professional communication', 'Because it must always be longer than the original document', 'Because conciseness prevents any information from being understood'], 0)]),
M('Number Theory: Diophantine Equations',
  'Grade 10 Math strand: a Diophantine equation is a polynomial equation for which only integer solutions are sought, a concept named after the ancient mathematician Diophantus that connects algebra and number theory in problems ranging from simple linear equations to complex modern applications.',
  [('What distinguishes a Diophantine equation from a typical algebraic equation?', ['Only integer solutions are sought for a Diophantine equation', 'A Diophantine equation has no variables at all', 'A Diophantine equation can never be solved', 'A Diophantine equation only allows decimal solutions'], 0),
   ('Who is the Diophantine equation named after?', ['The ancient mathematician Diophantus', 'The mathematician Euclid', 'The mathematician Pythagoras', 'The mathematician Fermat'], 0),
   ('What branches of mathematics does the study of Diophantine equations connect?', ['Algebra and number theory', 'Only basic geometry with no algebra involved', 'Only statistics with no algebra involved', 'Only trigonometry with no number theory involved'], 0),
   ('Which of the following is an example of a simple linear Diophantine equation?', ['3x + 5y = 7, solved for integer x and y', 'A single equation with no variables', 'An equation requiring only decimal answers', 'An equation with no possible integer solutions defined by its structure'], 0),
   ('Why are Diophantine equations still studied in modern mathematics?', ['They connect to important applications, including areas of modern cryptography', 'They have no remaining relevance to any field', 'They were fully solved by ancient mathematicians with nothing left to study', 'They apply only to ancient historical problems with no modern use'], 0)]),
Sc('Earth Science: Wetlands and Their Ecological Role',
   'Grade 10 Science strand: wetlands are transitional ecosystems where land is saturated with water for significant periods, supporting high biodiversity while providing critical services such as filtering pollutants, controlling floods, and storing carbon.',
   [('What defines a wetland ecosystem?', ['Land that is saturated with water for significant periods of time', 'Land that is always completely dry with no water present', 'A region located only at the top of a mountain', 'An area made entirely of solid rock with no vegetation'], 0),
    ('Why are wetlands known for high biodiversity?', ['They provide a unique habitat that supports a wide range of plant and animal species', 'They support no living organisms at all', 'They contain only a single species of plant', 'They are entirely devoid of water and nutrients'], 0),
    ('What water-related service do wetlands provide to surrounding areas?', ['Filtering pollutants and helping control floods', 'Increasing the risk of flooding in every case', 'Adding pollutants directly into groundwater', 'Removing all water from a region permanently'], 0),
    ('How do wetlands contribute to addressing climate change?', ['They store significant amounts of carbon', 'They release stored carbon with no absorption at all', 'They have no relationship to carbon storage', 'They only affect local temperature and nothing else'], 0),
    ('Why might human development pose a threat to wetlands?', ['Draining or building over wetlands can destroy their unique ecological functions', 'Human development always improves wetland health', 'Wetlands are unaffected by any human activity', 'Wetlands cannot be altered by construction of any kind'], 0)]),
H('Newfoundland and the Commission of Government of 1934',
  'Grade 10 History strand: facing financial collapse during the Great Depression, the Dominion of Newfoundland suspended its own self-government in 1934 and was administered by an appointed Commission of Government under British oversight until Newfoundland eventually joined Canada in 1949.',
  [('Why did Newfoundland suspend its self-government in 1934?', ['It faced financial collapse during the Great Depression', 'It had just won a major war', 'It had just joined Confederation', 'It had discovered a large new source of wealth'], 0),
   ('What replaced Newfoundlands elected government in 1934?', ['An appointed Commission of Government under British oversight', 'A newly elected democratic parliament', 'A government run entirely by the United States', 'An immediate merger with the province of Quebec'], 0),
   ('What was Newfoundlands political status before 1934?', ['A self-governing Dominion', 'A Canadian province', 'A colony of France', 'An independent republic with no ties to Britain'], 0),
   ('What eventually happened to Newfoundland after this period of commission government?', ['It joined Canada as a province in 1949', 'It became fully independent with no ties to any nation', 'It was annexed permanently by the United States', 'It remained under commission government indefinitely with no change'], 0),
   ('The Commission of Government period illustrates the impact of which global economic event?', ['The Great Depression', 'The Klondike Gold Rush', 'World War I', 'The 1918-1920 Spanish Flu Pandemic'], 0)]),
]),
day(139, [
E('Literature: The Doppelganger Motif in Fiction',
  'Grade 10 English strand: a doppelganger is a characters double or look-alike, often representing a hidden or opposing side of the original characters personality, and the motif is frequently used to explore themes of identity, morality, and psychological duality.',
  [('What is a doppelganger in literature?', ['A characters double or look-alike', 'A minor character who never returns after one scene', 'A narrator who addresses the reader directly', 'A setting that changes throughout a story'], 0),
   ('What does a doppelganger often represent in a text?', ['A hidden or opposing side of the original characters personality', 'A completely unrelated character with no connection to the protagonist', 'A change in the storys physical setting', 'A summary of the entire plot'], 0),
   ('Which theme is the doppelganger motif frequently used to explore?', ['Identity and psychological duality', 'The geography of a fictional country', 'The economics of a fictional marketplace', 'The chronology of historical events'], 0),
   ('Why might an author use a doppelganger to develop a character?', ['To externalize inner conflict or hidden aspects of the characters identity', 'To avoid developing the main character at all', 'To eliminate the need for any conflict in the story', 'To simplify the plot into a single, unbroken line'], 0),
   ('The doppelganger motif often creates a sense of ___.', ['Unease or psychological tension between the double and the original character', 'Complete comfort with no tension whatsoever', 'A purely comedic and lighthearted tone in every case', 'A total absence of thematic meaning'], 0)]),
M('Probability: The Poisson Distribution',
  'Grade 10 Math strand: the Poisson distribution models the probability of a given number of events occurring in a fixed interval of time or space, when those events happen independently and at a known constant average rate.',
  [('What does the Poisson distribution model?', ['The probability of a given number of events occurring in a fixed interval of time or space', 'The exact height of a geometric shape', 'The area under a straight line only', 'The probability of an event that never occurs'], 0),
   ('What condition must the events satisfy for a Poisson distribution to apply?', ['The events must occur independently and at a known constant average rate', 'The events must always occur at the exact same instant', 'The events must be entirely dependent on one another', 'The events must occur with no defined average rate at all'], 0),
   ('Which of the following is a typical real-world example modeled by a Poisson distribution?', ['The number of customer arrivals at a store in one hour', 'The exact height of a single building', 'The colour of a randomly selected object', 'The temperature of a room at a single moment'], 0),
   ('How does the Poisson distribution differ from the binomial distribution?', ['The Poisson distribution models counts of events over a continuous interval rather than a fixed number of trials', 'The two distributions are mathematically identical in every way', 'The Poisson distribution only applies to exactly two possible outcomes', 'The binomial distribution cannot be used to model any real event'], 0),
   ('Why is the average rate parameter important in a Poisson distribution?', ['It determines the expected number of events in the given interval', 'It has no effect on the resulting probabilities', 'It only matters when the average rate equals zero', 'It replaces the need for any probability calculation'], 0)]),
Sc('Biology: Bioluminescence in Living Organisms',
   'Grade 10 Science strand: bioluminescence is the production of light by a living organism through a chemical reaction, most commonly involving the molecule luciferin and the enzyme luciferase, and is used by many marine and terrestrial species for communication, predation, or defense.',
   [('What is bioluminescence?', ['The production of light by a living organism through a chemical reaction', 'The absorption of light by a completely inanimate object', 'A process found only in plants with no animals involved', 'A permanent change in an organisms skeletal structure'], 0),
    ('Which molecule is most commonly involved in producing bioluminescent light?', ['Luciferin', 'Chlorophyll', 'Hemoglobin', 'Glucose'], 0),
    ('What role does the enzyme luciferase play in bioluminescence?', ['It catalyzes the chemical reaction that produces light', 'It prevents any chemical reaction from occurring', 'It has no connection to light production at all', 'It converts light directly into heat with no reaction involved'], 0),
    ('Which environment is well known for a high number of bioluminescent species?', ['The deep ocean', 'The surface of the moon', 'A completely dry desert with no other adaptations', 'The inside of a volcano'], 0),
    ('What is one reason organisms use bioluminescence?', ['To attract prey, communicate, or deter predators', 'To permanently blind themselves with no other purpose', 'To increase their body temperature significantly', 'To eliminate their need for any other senses'], 0)]),
H('The Founding of the Bank of Canada in 1934-1935',
  'Grade 10 History strand: the Bank of Canada was established through legislation passed in 1934 and began operations in 1935 as the countrys central bank, tasked with managing monetary policy, issuing currency, and stabilizing the economy in the aftermath of the Great Depression.',
  [('When did the Bank of Canada begin operations?', ['1935', '1867', '1905', '1949'], 0),
   ('What role does the Bank of Canada serve?', ['It functions as the countrys central bank', 'It functions as a private commercial bank only', 'It functions as a provincial tax collection agency', 'It functions as a national railway company'], 0),
   ('What economic crisis contributed to the founding of the Bank of Canada?', ['The Great Depression', 'The Klondike Gold Rush', 'World War I', 'The 1918-1920 Spanish Flu Pandemic'], 0),
   ('Which of the following is a key responsibility of the Bank of Canada?', ['Managing monetary policy and issuing currency', 'Building and maintaining national highways', 'Administering provincial elections', 'Operating public schools across the country'], 0),
   ('Why might a country establish a central bank during a major economic crisis?', ['To help stabilize the economy through coordinated monetary policy', 'To eliminate the need for any currency at all', 'To transfer all economic control to a foreign government', 'To ensure that no economic policy is ever coordinated nationally'], 0)]),
]),
day(140, [
E('English Review: Grammar, Rhetoric, and Contemporary Literacy',
  'Grade 10 English strand review: students revisit correlative conjunctions, extended metaphor and conceit, the public service announcement, utopian fiction, clickbait and the attention economy, absolute phrases, narrative distance, the abstract and executive summary, and the doppelganger motif.',
  [('What is a correlative conjunction?', ['A paired word set that links balanced words, phrases, or clauses', 'A single word that ends a sentence', 'A word that replaces a noun entirely', 'A punctuation mark used in dialogue'], 0),
   ('What is a conceit in literary terms?', ['An especially elaborate or unconventional extended metaphor', 'A short simile used only once', 'A grammatical error in a poem', 'A type of rhyme scheme'], 0),
   ('What is clickbait?', ['Headlines or content designed primarily to attract clicks rather than inform accurately', 'A type of formal citation used in academic essays', 'A method of fact-checking a news article', 'A grammatical structure used in headlines only'], 0),
   ('What does an absolute phrase typically consist of?', ['A noun followed by a participle or modifier', 'A verb followed directly by a conjunction', 'A single adjective with no noun', 'A complete independent clause only'], 0),
   ('What is a doppelganger in literature?', ['A characters double or look-alike', 'A minor character who never returns after one scene', 'A narrator who addresses the reader directly', 'A setting that changes throughout a story'], 0)]),
M('Math Review: Calculus, Number Theory, and Advanced Concepts',
  'Grade 10 Math strand review: students revisit the chain rule, Fermats Little Theorem, confidence intervals, implicit differentiation, polar coordinates, the pigeonhole principle, related rates, Diophantine equations, and the Poisson distribution.',
  [('What does the chain rule allow you to differentiate?', ['A composite function, one function nested inside another', 'Only a single constant term', 'Only a sum of two unrelated functions', 'Only whole numbers with no variables'], 0),
   ('What condition must p satisfy in Fermats Little Theorem?', ['p must be a prime number', 'p must be a perfect square', 'p must be an even number only', 'p must be equal to zero'], 0),
   ('What does a confidence interval estimate?', ['A range of values likely to contain the true population parameter', 'The exact value of a population parameter with total certainty', 'A single number with no range at all', 'The size of a sample only'], 0),
   ('What does the pigeonhole principle state?', ['If more items are placed into containers than there are containers, at least one container holds more than one item', 'Every container must hold exactly one item at all times', 'No container can ever hold more than one item', 'The number of items must always equal the number of containers'], 0),
   ('What does the Poisson distribution model?', ['The probability of a given number of events occurring in a fixed interval of time or space', 'The exact height of a geometric shape', 'The area under a straight line only', 'The probability of an event that never occurs'], 0)]),
Sc('Science Review: Cell Processes, Chemistry, and Earth Systems',
   'Grade 10 Science strand review: students revisit osmosis and diffusion, chromatography, aerodynamics and the physics of flight, sinkholes and karst topography, vaccines and immunization, water purification, superconductivity, wetlands, and bioluminescence.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles only against a concentration gradient', 'A process that occurs only in solids', 'A process requiring the cell to use energy at all times'], 0),
    ('What is the main purpose of chromatography?', ['To separate the components of a mixture', 'To combine several substances into a single compound', 'To measure the temperature of a solution', 'To determine the mass of a solid object'], 0),
    ('What are the four key forces involved in flight?', ['Lift, weight, thrust, and drag', 'Only gravity and friction', 'Only speed and mass', 'Only temperature and pressure'], 0),
    ('What defines a superconducting material?', ['It conducts electricity with zero electrical resistance below a critical temperature', 'It always resists electrical current completely at every temperature', 'It never conducts electricity under any condition', 'It only conducts electricity at extremely high temperatures'], 0),
    ('What is bioluminescence?', ['The production of light by a living organism through a chemical reaction', 'The absorption of light by a completely inanimate object', 'A process found only in plants with no animals involved', 'A permanent change in an organisms skeletal structure'], 0)]),
H('History Review: Institution-Building in Early Twentieth-Century Canada',
  'Grade 10 History strand review: students revisit the founding of the North-West Mounted Police, the Naval Aid Bill, the Income War Tax Act of 1917, the formation of Canadian National Railways, the founding of the United Church of Canada, the Old Age Pensions Act, the founding of the CBC, Newfoundlands Commission of Government, and the founding of the Bank of Canada.',
  [('In what year was the North-West Mounted Police established?', ['1873', '1867', '1905', '1949'], 0),
   ('What did the Naval Aid Bill propose to fund?', ['British dreadnoughts directly instead of building a Canadian navy', 'A new Canadian air force', 'The construction of the Canadian Pacific Railway', 'A national system of highways'], 0),
   ('What was the original stated purpose of the Income War Tax Act?', ['A temporary wartime measure to help fund Canadas participation in World War I', 'A permanent replacement for all provincial taxes', 'A tax designed to fund the Canadian Pacific Railway', 'A tax created to fund Confederation celebrations'], 0),
   ('What did the Old Age Pensions Act establish?', ['Canadas first federal old age pension program', 'A national healthcare system for all Canadians', 'A federal minimum wage law', 'A national unemployment insurance program'], 0),
   ('What role does the Bank of Canada serve?', ['It functions as the countrys central bank', 'It functions as a private commercial bank only', 'It functions as a provincial tax collection agency', 'It functions as a national railway company'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_131_140)
    append_to(10, g10_131_140)
