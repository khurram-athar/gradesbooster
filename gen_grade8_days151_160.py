#!/usr/bin/env python3
"""Grade 8, Days 151-160 -- extends Grade 8 from 150 to 160 days. Topics
chosen after dumping the existing Day 1-150 title list (data/grade8.json)
in full to avoid any overlap: inverted sentence structure, slang and
generational language, static and dynamic characters, the
problem-solution essay, photojournalism and image manipulation, split
infinitives, clipped words and abbreviated forms, parody and pastiche,
and the character sketch; the Central Limit Theorem, the Euclidean
Algorithm, topology and the Konigsberg Bridge Problem, function
composition, Markov chains, amicable numbers, Simpsons Paradox, vector
spaces, and related rates; electrolysis and electroplating, static
electricity and the triboelectric effect, ocean currents and
thermohaline circulation, decomposers and nutrient cycling, the
structure of the Milky Way galaxy, GPS satellites, catalysts and
reaction rates, the electromagnetic spectrum, and coevolution and
predator-prey adaptations; Agnes Macphail, the 1918 Spanish Flu
pandemic in Canada, the Rowell-Sirois Commission, the Padlock Law, the
National Housing Act, the Old Age Pensions Act of 1927, the formation
of Trans-Canada Air Lines, the prairie dust bowl of the 1930s, and the
Bank of Canada Act. Day 160 is a cross-subject review day drawing on
Days 151-159; each review title includes the Days 151-159 range so it
is textually distinct from every earlier review days title.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days141_150.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-history'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science and Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


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


g8_151_160 = [
day(151, [
L('Grammar: Inverted Sentence Structure and Emphasis',
  'Grade 8 Language strand: inverted sentence structure reverses the usual subject-verb order, placing a verb, adverb, or complement before the subject, and writers use this technique sparingly to create emphasis, formality, or a dramatic effect.',
  [('What does inverted sentence structure reverse?', ['The usual subject-verb order', 'The meaning of every word in a sentence', 'The spelling of a word', 'The tense of a verb only'], 0),
   ('Which sentence demonstrates inverted structure?', ['Never had she seen such a sight.', 'She had never seen such a sight.', 'She saw a sight she had never seen.', 'She never saw such a sight before.'], 0),
   ('Why might a writer choose to use inverted sentence structure?', ['To create emphasis, formality, or a dramatic effect', 'To make a sentence completely meaningless', 'To avoid using any verbs', 'To remove all punctuation from a sentence'], 0),
   ('Which part of a sentence is typically moved to the front in an inverted structure?', ['A verb, adverb, or complement', 'Only the final punctuation mark', 'The entire paragraph', 'A silent letter'], 0),
   ('Why should inverted sentence structure generally be used sparingly?', ['Overuse can make writing sound awkward or overly formal', 'It always makes writing clearer the more it is used', 'Inverted structure has no effect on tone', 'Readers never notice a change in sentence order'], 0)]),
M('Statistics: An Introduction to the Central Limit Theorem',
  'Grade 8 Math strand: the Central Limit Theorem states that as the sample size grows large, the distribution of sample means drawn from a population tends toward a normal distribution, regardless of the shape of the original population.',
  [('What does the Central Limit Theorem describe?', ['How the distribution of sample means tends toward a normal distribution as sample size grows', 'How to calculate the area of a triangle', 'A rule for rounding decimals', 'A method for factoring polynomials'], 0),
   ('According to the theorem, what happens as sample size increases?', ['The distribution of sample means becomes more closely normal', 'The distribution of sample means becomes more random', 'Sample means always become identical to each other', 'The population itself changes shape'], 0),
   ('Does the Central Limit Theorem require the original population to already be normally distributed?', ['No, it applies regardless of the shape of the original population', 'Yes, the population must always be normally distributed first', 'The theorem cannot be applied unless the population is uniform', 'The theorem only applies to populations with exactly ten members'], 0),
   ('Why is the Central Limit Theorem considered important in statistics?', ['It allows normal-distribution methods to be applied to many real-world sampling situations', 'It proves that all populations are identical', 'It eliminates the need to ever collect a sample', 'It has no practical use in statistical analysis'], 0),
   ('Which of these best describes a sample mean in this context?', ['The average value calculated from a single sample drawn from a larger population', 'The largest value found in an entire population', 'A value chosen at random with no calculation', 'The total sum of every value in a population'], 0)]),
Sc('Chemistry: Electrolysis and Electroplating',
   'Grade 8 Science strand: electrolysis uses an electric current to drive a chemical reaction that would not occur naturally, and electroplating applies this process to coat an object with a thin layer of metal, often to prevent corrosion or improve appearance.',
   [('What does electrolysis use to drive a chemical reaction?', ['An electric current', 'A magnetic field only', 'A change in air pressure', 'Sound waves'], 0),
    ('What does electroplating apply electrolysis to accomplish?', ['Coating an object with a thin layer of metal', 'Removing all metal from an object', 'Turning a liquid into a gas', 'Cooling an object rapidly'], 0),
    ('Why might an object be electroplated with a metal such as chromium or gold?', ['To prevent corrosion or improve its appearance', 'To make the object completely dissolve', 'To eliminate its electrical conductivity', 'To make the object magnetic'], 0),
    ('What type of reaction does electrolysis typically cause?', ['A reaction that would not occur naturally without an added electric current', 'A reaction that always occurs spontaneously with no energy input', 'A purely physical change with no chemical reaction', 'A nuclear reaction involving radioactive decay'], 0),
    ('Why is electrolysis considered a useful industrial process?', ['It allows chemical changes such as metal coating and purification to be precisely controlled', 'It has no practical applications outside a classroom', 'It can only be used to destroy metal objects', 'It prevents any chemical reaction from occurring'], 0)]),
H('Agnes Macphail and Canadas First Woman Member of Parliament',
  'Grade 8 History strand: in 1921 Agnes Macphail became the first woman elected to the Canadian House of Commons, where she advocated for farmers, workers, prison reform, and continued efforts toward equality for women in Canadian public life.',
  [('In what year was Agnes Macphail first elected to the Canadian House of Commons?', ['1921', '1867', '1929', '1949'], 0),
   ('What distinction did Agnes Macphail hold as a member of Parliament?', ['She was the first woman elected to the Canadian House of Commons', 'She was the first prime minister of Canada', 'She was the first woman appointed to the Senate', 'She was the first woman to serve as a provincial premier'], 0),
   ('Which group did Agnes Macphail advocate for as a member of Parliament?', ['Farmers and workers', 'Foreign diplomats only', 'Only wealthy landowners', 'Railway executives'], 0),
   ('What reform issue did Agnes Macphail become known for championing?', ['Prison reform', 'The abolition of all provincial governments', 'The elimination of public schools', 'A ban on all international trade'], 0),
   ('Why is Agnes Macphail considered an important figure in Canadian political history?', ['Her election opened the door for greater representation of women in Canadian federal politics', 'She opposed all efforts to expand political representation', 'She never influenced any policy during her time in office', 'Her election had no lasting significance for Canadian politics'], 0)]),
]),
day(152, [
L('Vocabulary: Slang and Informal Language Across Generations',
  'Grade 8 Language strand: slang is informal vocabulary that develops within a particular group or generation and often changes quickly over time, and recognizing slang helps readers understand a texts tone, audience, and time period.',
  [('What is slang?', ['Informal vocabulary that develops within a particular group or generation', 'A formal citation style used in academic writing', 'A grammatical rule about verb tense', 'A punctuation mark used to end a question'], 0),
   ('Why does slang often change quickly over time?', ['New words and expressions continually develop as trends and cultures shift', 'Slang words never change once they are created', 'Formal vocabulary changes faster than slang', 'Slang is identical across every generation'], 0),
   ('Which is an example of how slang might be used in writing?', ['To reflect the tone of a specific character or time period in dialogue', 'To replace all punctuation in a sentence', 'To make a formal report sound more academic', 'To remove any sense of character voice from a text'], 0),
   ('Why might slang used in dialogue not be appropriate in formal writing?', ['Formal writing generally requires standard vocabulary that a broad audience will understand', 'Formal writing always requires as much slang as possible', 'Slang and formal vocabulary are exactly the same thing', 'Formal writing never uses vocabulary of any kind'], 0),
   ('Why is recognizing slang a useful reading skill?', ['It helps a reader understand a texts tone, audience, and time period', 'Slang has no connection to a texts tone or setting', 'Recognizing slang prevents a reader from understanding a text', 'Slang words are always identical to formal vocabulary'], 0)]),
M('Number Theory: The Euclidean Algorithm and Greatest Common Divisors',
  'Grade 8 Math strand: the Euclidean Algorithm finds the greatest common divisor of two integers by repeatedly dividing and replacing the larger number with the remainder until the remainder reaches zero, at which point the last nonzero remainder is the greatest common divisor.',
  [('What does the Euclidean Algorithm find?', ['The greatest common divisor of two integers', 'The least common multiple of two integers only', 'The square root of a number', 'The average of two integers'], 0),
   ('What operation does the Euclidean Algorithm repeatedly use?', ['Division, replacing the larger number with the remainder', 'Multiplication of both numbers together', 'Addition of the two numbers repeatedly', 'Rounding both numbers to the nearest ten'], 0),
   ('When does the Euclidean Algorithm stop?', ['When the remainder reaches zero', 'When the numbers become negative', 'After exactly one division, regardless of the result', 'It never stops and repeats forever'], 0),
   ('In the Euclidean Algorithm, what is the greatest common divisor once the process ends?', ['The last nonzero remainder produced', 'The very first number in the original pair', 'Always the number one', 'The sum of all remainders produced'], 0),
   ('Why is the Euclidean Algorithm considered an efficient method for finding a greatest common divisor?', ['It reaches the answer in relatively few steps even for large numbers', 'It requires testing every possible divisor individually', 'It only works for numbers smaller than ten', 'It cannot be used on large integers'], 0)]),
Sc('Physics: Static Electricity and the Triboelectric Effect',
   'Grade 8 Science strand: static electricity builds up when electrons transfer between two objects through contact, often by rubbing, a process known as the triboelectric effect, leaving one object positively charged and the other negatively charged until the charge is discharged.',
   [('How does static electricity typically build up?', ['Electrons transfer between two objects through contact, often by rubbing', 'Protons are created out of nothing', 'Atoms disappear from an objects surface', 'Objects lose all of their mass'], 0),
    ('What is the transfer of electrons through rubbing known as?', ['The triboelectric effect', 'The photoelectric effect', 'Electromagnetic induction', 'Nuclear fission'], 0),
    ('What happens to the charge of the two objects after electrons transfer between them?', ['One becomes positively charged and the other becomes negatively charged', 'Both objects always remain completely neutral', 'Both objects become positively charged', 'Both objects lose all electrical charge entirely'], 0),
    ('What can happen when a strongly charged object comes near an oppositely charged surface?', ['The built-up charge can suddenly discharge, sometimes seen as a spark', 'Nothing happens under any circumstance', 'The object instantly becomes magnetic', 'The charge is permanently locked in place'], 0),
    ('Why do some materials build up static charge more easily than others?', ['Different materials hold onto or give up electrons more readily than others', 'All materials hold electrons with exactly equal strength', 'Static charge only forms in materials that conduct electricity perfectly', 'Static electricity has no connection to a materials properties'], 0)]),
H('The 1918 Spanish Flu Pandemic in Canada',
  'Grade 8 History strand: the 1918 influenza pandemic, often called the Spanish Flu, spread rapidly across Canada in the final months of World War I, overwhelming hospitals and prompting public health measures such as quarantines and the closure of schools and public gathering places.',
  [('What is the 1918 influenza pandemic commonly known as?', ['The Spanish Flu', 'The Asian Flu', 'The Black Death', 'The Great Fever'], 0),
   ('During what broader global event did the Spanish Flu spread across Canada?', ['The final months of World War I', 'The Great Depression', 'The Cold War', 'World War II'], 0),
   ('What public health measures were used to try to slow the spread of the Spanish Flu?', ['Quarantines and the closure of schools and public gathering places', 'Opening more schools and increasing public gatherings', 'A complete ban on all forms of medicine', 'Ignoring the outbreak entirely'], 0),
   ('What effect did the Spanish Flu have on Canadian hospitals?', ['It overwhelmed hospitals with a surge of patients', 'It had no effect on hospitals at all', 'Hospitals closed permanently with no patients arriving', 'It reduced hospital admissions to zero'], 0),
   ('Why is the 1918 pandemic still studied by historians and public health officials today?', ['It offers important lessons about how societies respond to widespread infectious disease', 'It has no relevance to modern public health', 'The pandemic never actually affected Canada', 'Historians have found no useful information from studying it'], 0)]),
]),
day(153, [
L('Reading: Analyzing Static and Dynamic Characters',
  'Grade 8 Language strand: a static character remains essentially unchanged throughout a story, while a dynamic character undergoes significant internal change, often as a result of a storys central conflict, and recognizing this distinction helps readers understand character development.',
  [('What defines a static character?', ['A character who remains essentially unchanged throughout a story', 'A character who changes completely every few pages', 'A character who never appears in the story', 'A character who only speaks in questions'], 0),
   ('What defines a dynamic character?', ['A character who undergoes significant internal change during a story', 'A character who has no personality traits at all', 'A character who appears in only one sentence', 'A character who is identical to every other character'], 0),
   ('What often causes a dynamic characters change?', ['The storys central conflict or major events', 'A change in the books cover design', 'The number of pages in the book', 'The font used to print the story'], 0),
   ('Which is an example of a dynamic character?', ['A character who begins selfish but learns compassion by the storys end', 'A character who behaves identically from the first page to the last', 'A character who is mentioned once and never again', 'A character with no name in the story'], 0),
   ('Why is recognizing static versus dynamic characters a valuable reading skill?', ['It helps readers understand how and why a story develops its characters over time', 'This distinction has no connection to understanding a story', 'Every character in every story is exactly the same type', 'Recognizing character types prevents readers from understanding a plot'], 0)]),
M('Geometry: An Introduction to Topology and the Konigsberg Bridge Problem',
  'Grade 8 Math strand: topology studies properties of shapes that remain unchanged under stretching or bending, and the historic Konigsberg Bridge Problem, which asked whether a walker could cross seven bridges exactly once, helped establish the foundations of graph theory and topology.',
  [('What does topology study?', ['Properties of shapes that remain unchanged under stretching or bending', 'The exact colour of every geometric shape', 'Only the area of a circle', 'The weight of a three-dimensional solid'], 0),
   ('What question did the Konigsberg Bridge Problem originally ask?', ['Whether a walker could cross seven bridges exactly once without repeating any', 'How many bridges could be built in a single city', 'What the shortest possible bridge length was', 'How many rivers flowed through Konigsberg'], 0),
   ('What field of mathematics did the Konigsberg Bridge Problem help establish?', ['Graph theory and topology', 'Basic addition and subtraction', 'The study of decimals', 'Elementary probability'], 0),
   ('What did the solution to the Konigsberg Bridge Problem ultimately show?', ['That such a walk was impossible given the arrangement of the bridges', 'That the walk was easy and could be done in many ways', 'That the bridges did not actually exist', 'That the problem had no mathematical solution of any kind'], 0),
   ('Why is the Konigsberg Bridge Problem considered a landmark in the history of mathematics?', ['It showed how a real-world puzzle could be solved using an entirely new mathematical approach', 'It proved that mathematics could never solve real-world problems', 'It was solved using only basic arithmetic with no new ideas', 'It has no connection to any branch of mathematics'], 0)]),
Sc('Earth Science: Ocean Currents and Thermohaline Circulation',
   'Grade 8 Science strand: ocean currents move vast amounts of water around the globe, driven partly by wind at the surface and partly by differences in water temperature and salinity that drive a deep, slow-moving global conveyor known as thermohaline circulation.',
   [('What are two factors that help drive ocean currents?', ['Wind at the surface and differences in temperature and salinity', 'Only the colour of the water', 'Only the depth of the seafloor', 'The number of ships crossing the ocean'], 0),
    ('What is thermohaline circulation?', ['A deep, slow-moving global conveyor of ocean water driven by temperature and salinity differences', 'A fast-moving surface current found only near the equator', 'A process that only occurs in freshwater lakes', 'A current caused entirely by tides alone'], 0),
    ('What does the word thermohaline refer to?', ['Temperature and salt content of ocean water', 'The colour and clarity of ocean water', 'The depth and pressure of the ocean floor', 'The speed of surface waves'], 0),
    ('Why can ocean currents affect regional climate?', ['They transport heat from warmer regions of the ocean to cooler regions', 'Ocean currents have no connection to climate at all', 'Currents only move sand, never heat', 'Currents remain perfectly still and never move heat'], 0),
    ('Why do scientists study changes in ocean currents when researching climate change?', ['Shifts in current patterns can significantly affect global weather and temperature distribution', 'Ocean currents never change over time', 'Currents have no influence on weather patterns', 'Studying currents provides no useful climate information'], 0)]),
H('The Rowell-Sirois Commission and Dominion-Provincial Relations',
  'Grade 8 History strand: established in 1937, the Rowell-Sirois Commission examined the financial relationship between the federal and provincial governments after the strain of the Great Depression, recommending changes intended to give the federal government a stronger role in economic and social policy.',
  [('In what year was the Rowell-Sirois Commission established?', ['1937', '1867', '1905', '1949'], 0),
   ('What relationship did the Rowell-Sirois Commission examine?', ['The financial relationship between the federal and provincial governments', 'Canadas relationship with the United Nations', 'The relationship between Canada and France', 'The structure of Canadas court system'], 0),
   ('What economic event prompted the creation of the Rowell-Sirois Commission?', ['The strain of the Great Depression', 'The end of World War II', 'The Klondike Gold Rush', 'The signing of Confederation in 1867'], 0),
   ('What did the Rowell-Sirois Commission recommend?', ['Giving the federal government a stronger role in economic and social policy', 'Eliminating the federal government entirely', 'Giving all economic authority exclusively to municipalities', 'Ending all federal funding to the provinces'], 0),
   ('Why was reexamining dominion-provincial financial relations considered urgent in the late 1930s?', ['Many provinces faced severe financial strain and needed a clearer, more sustainable funding structure', 'Provinces had unlimited funding and needed no support', 'The federal government had no role in provincial finances at any time', 'Financial relations between governments were never a concern in Canada'], 0)]),
]),
day(154, [
L('Writing: The Problem-Solution Essay',
  'Grade 8 Language strand: a problem-solution essay identifies a specific issue, explains its causes and effects, and proposes one or more realistic solutions supported by evidence and reasoning.',
  [('What does a problem-solution essay identify?', ['A specific issue along with its causes and effects', 'A random collection of unrelated topics', 'A single sentence with no supporting explanation', 'A list of characters from a novel'], 0),
   ('What must a proposed solution in this type of essay be supported by?', ['Evidence and reasoning', 'No supporting explanation whatsoever', 'A single unsupported opinion', 'A completely unrelated topic'], 0),
   ('Why might a writer include the effects of a problem before proposing a solution?', ['To help readers understand why the issue matters and needs to be addressed', 'Effects are never relevant to a problem-solution essay', 'Including effects always confuses the reader', 'A problem-solution essay never discusses effects'], 0),
   ('What distinguishes a problem-solution essay from a purely descriptive essay?', ['It moves beyond description to propose and justify a course of action', 'It never describes the problem in any detail', 'There is no meaningful difference between the two', 'A problem-solution essay is always shorter than any other essay type'], 0),
   ('Why is a problem-solution essay considered a persuasive form of writing?', ['It aims to convince readers that a particular solution is reasonable and effective', 'It never tries to convince a reader of anything', 'It only presents facts with no argument at all', 'Persuasion has no role in this type of essay'], 0)]),
M('Algebra: An Introduction to Function Composition',
  'Grade 8 Math strand: function composition combines two functions by applying one function to the result of another, so that the output of the first function becomes the input of the second, producing a new combined function.',
  [('What does function composition do?', ['Combines two functions by applying one to the result of another', 'Deletes one function entirely', 'Converts a function into a single number with no variables', 'Removes all variables from a function'], 0),
   ('In a composed function, what becomes the input of the second function?', ['The output of the first function', 'A randomly chosen number with no connection to either function', 'The name of the first function', 'The exponent of the second function'], 0),
   ('If f(x) and g(x) are functions, what does f(g(x)) represent?', ['Applying g first, then applying f to that result', 'Applying f and g at the exact same time with no order', 'Adding f and g together', 'Multiplying f and g without applying either function'], 0),
   ('Why is the order in which functions are composed generally important?', ['Composing functions in a different order can produce a different result', 'The order of composition never affects the result', 'Functions cannot be composed in more than one order', 'Order only matters when composing exactly three functions'], 0),
   ('Why is function composition a useful concept in mathematics?', ['It allows complex relationships to be built from simpler, more basic functions', 'It has no practical use in mathematics', 'It only applies to functions with no variables', 'Composed functions can never be graphed'], 0)]),
Sc('Biology: Decomposers and Nutrient Cycling in Ecosystems',
   'Grade 8 Science strand: decomposers such as fungi and bacteria break down dead organisms and waste material, releasing nutrients back into the soil so they can be reused by plants, making decomposers essential to nutrient cycling within an ecosystem.',
   [('What do decomposers such as fungi and bacteria break down?', ['Dead organisms and waste material', 'Only living, healthy plants', 'Rocks and minerals only', 'Water molecules exclusively'], 0),
    ('What do decomposers release back into the soil?', ['Nutrients that can be reused by plants', 'Only carbon dioxide gas', 'Radioactive particles', 'Pure oxygen with no other elements'], 0),
    ('Why are decomposers considered essential to nutrient cycling?', ['They return nutrients from dead matter to the ecosystem so they can be used again', 'Decomposers remove all nutrients permanently from an ecosystem', 'Decomposers have no role in an ecosystems nutrient supply', 'Nutrient cycling occurs with no involvement from decomposers'], 0),
    ('What might happen to an ecosystem if decomposers were removed?', ['Dead matter would accumulate and nutrients would not be returned to the soil', 'The ecosystem would function exactly the same with no changes', 'Nutrient levels in the soil would increase dramatically', 'Plants would grow more quickly with no decomposers present'], 0),
    ('Why are decomposers sometimes described as natures recyclers?', ['They convert waste and dead material into reusable nutrients for other living things', 'They destroy nutrients permanently with no benefit to an ecosystem', 'They produce waste rather than breaking it down', 'They have no connection to recycling of any kind'], 0)]),
H('The Padlock Law and Civil Liberties in Depression-Era Quebec',
  'Grade 8 History strand: passed by the Quebec government in 1937, the Padlock Law allowed authorities to close, or padlock, any premises suspected of spreading communist propaganda, raising lasting concerns about civil liberties and freedom of expression in Canada.',
  [('In what year was the Padlock Law passed in Quebec?', ['1937', '1867', '1921', '1949'], 0),
   ('What did the Padlock Law allow authorities to do?', ['Close, or padlock, premises suspected of spreading communist propaganda', 'Build new schools across the province', 'Lower taxes for all Quebec residents', 'Expand voting rights to more citizens'], 0),
   ('What broader concern did the Padlock Law raise?', ['Concerns about civil liberties and freedom of expression', 'Concerns about railway construction costs', 'Concerns about agricultural production', 'Concerns about international trade agreements'], 0),
   ('Which level of government passed the Padlock Law?', ['The Quebec provincial government', 'The federal government of Canada', 'The government of Ontario', 'A municipal city council'], 0),
   ('Why is the Padlock Law still studied as an important moment in Canadian civil liberties history?', ['It illustrates tension between government authority and individual freedom of expression during a period of political anxiety', 'It has no lasting significance for Canadian history', 'It expanded freedom of expression for every Canadian', 'It was never actually enforced by any authority'], 0)]),
]),
day(155, [
L('Media Literacy: Analyzing Photojournalism and Image Manipulation',
  'Grade 8 Language strand: photojournalism uses photographs to document real events, but choices such as cropping, framing, and digital editing can alter how a viewer interprets an image, making it important for media consumers to consider a photographs context and possible manipulation.',
  [('What is photojournalism?', ['The use of photographs to document real events', 'A style of writing used only in fiction', 'A method of editing video footage exclusively', 'A type of illustration used in cartoons'], 0),
   ('Which of these can influence how a viewer interprets a news photograph?', ['Cropping, framing, and digital editing', 'The photographs file size alone', 'The type of camera used with no other factor', 'The photographers height'], 0),
   ('Why is it important for media consumers to consider a photographs context?', ['An image removed from its context can create a misleading impression of an event', 'Context never affects how an image is understood', 'Photographs always tell the complete story with no need for context', 'Context only matters for written articles, never photographs'], 0),
   ('What might indicate that a photograph has been digitally manipulated?', ['Inconsistent lighting, shadows, or unnatural edges within the image', 'A photograph taken in bright daylight', 'A photograph printed on high-quality paper', 'A photograph that includes more than one person'], 0),
   ('Why should viewers evaluate news photographs critically rather than accepting them at face value?', ['Manipulated or selectively framed images can distort a viewers understanding of real events', 'All news photographs are always completely accurate with no exceptions', 'Critical evaluation of photographs serves no useful purpose', 'Photographs can never be altered or manipulated in any way'], 0)]),
M('Probability: An Introduction to Markov Chains',
  'Grade 8 Math strand: a Markov chain models a system that moves between a set of states, where the probability of moving to the next state depends only on the current state and not on the sequence of states that came before it.',
  [('What does a Markov chain model?', ['A system that moves between a set of states with defined probabilities', 'A single fixed number with no possible change', 'A shape with no defined boundaries', 'A list of unrelated historical dates'], 0),
   ('In a Markov chain, what does the probability of the next state depend on?', ['Only the current state', 'Every state that has ever occurred in the past', 'A state that has not yet been defined', 'Nothing at all, since the process is entirely undefined'], 0),
   ('What is this key property of Markov chains, where the future depends only on the present state, often called?', ['The Markov property', 'The Euclidean property', 'The Pythagorean property', 'The commutative property'], 0),
   ('Which of these could be modeled using a Markov chain?', ['The probability of tomorrows weather depending only on todays weather', 'The exact colour of a randomly chosen car', 'The alphabetical order of a list of names', 'The area of a randomly drawn triangle'], 0),
   ('Why are Markov chains useful for modeling real-world systems?', ['They provide a simplified but powerful way to predict how a system evolves over time', 'They cannot be applied to any real-world situation', 'They require knowing every past state in complete detail', 'They only apply to systems with a single possible state'], 0)]),
Sc('Space Science: The Structure of the Milky Way Galaxy',
   'Grade 8 Science strand: the Milky Way is a large spiral galaxy containing billions of stars, including the Sun, arranged in a flattened disc with curved spiral arms surrounding a dense central bulge.',
   [('What type of galaxy is the Milky Way?', ['A large spiral galaxy', 'A small, perfectly spherical galaxy', 'A galaxy with no defined shape', 'A galaxy made entirely of comets'], 0),
    ('Roughly how many stars does the Milky Way contain?', ['Billions of stars, including the Sun', 'Exactly one hundred stars', 'Fewer than ten stars', 'No stars at all, only planets'], 0),
    ('What shape does the Milky Way form?', ['A flattened disc with curved spiral arms', 'A perfect cube', 'A single straight line', 'A hollow, empty sphere'], 0),
    ('What lies at the centre of the Milky Way?', ['A dense central bulge', 'An empty region with no matter at all', 'A single small planet', 'A frozen ice cap'], 0),
    ('Why is it difficult for scientists on Earth to directly observe the overall shape of the Milky Way?', ['Earth is located within the galaxys disc, limiting an outside view of its full structure', 'The Milky Way has no shape at all to observe', 'Telescopes are physically incapable of viewing any part of the galaxy', 'Earth is located completely outside the Milky Way'], 0)]),
H('The National Housing Act and the Growth of Canadian Suburbs',
  'Grade 8 History strand: first passed in 1938 and expanded significantly after World War II, the National Housing Act helped make mortgages more accessible to Canadian families, fueling rapid suburban growth around major Canadian cities in the following decades.',
  [('In what year was the National Housing Act first passed?', ['1938', '1867', '1921', '1905'], 0),
   ('What did the National Housing Act help make more accessible to Canadian families?', ['Mortgages', 'International passports', 'University tuition', 'Farmland in the north'], 0),
   ('What growth did the National Housing Act help fuel in the decades that followed?', ['Rapid suburban growth around major Canadian cities', 'A sharp decline in Canadas overall population', 'The end of all urban development in Canada', 'A complete halt to residential construction'], 0),
   ('When was the National Housing Act significantly expanded?', ['After World War II', 'Before Confederation in 1867', 'During the Klondike Gold Rush', 'During the 1918 influenza pandemic'], 0),
   ('Why might increased access to mortgages lead to rapid suburban development?', ['More families were able to afford homeownership outside crowded city centres', 'Mortgages have no connection to where people choose to live', 'Increased mortgage access always reduces homeownership rates', 'Suburban development happened entirely independent of housing policy'], 0)]),
]),
day(156, [
L('Grammar: Split Infinitives and Verb Phrase Clarity',
  'Grade 8 Language strand: a split infinitive occurs when a word, usually an adverb, is placed between the word to and the base verb it introduces, and while some traditional style guides discourage the construction, modern usage often accepts it when it improves clarity.',
  [('What is a split infinitive?', ['A construction where a word is placed between to and the base verb it introduces', 'A sentence with no verb at all', 'A word split into two separate sentences', 'A punctuation mark placed inside a verb'], 0),
   ('Which sentence contains a split infinitive?', ['She decided to quickly finish her homework.', 'She decided to finish her homework quickly.', 'Quickly, she decided to finish her homework.', 'She quickly decided to finish her homework.'], 0),
   ('What word is most commonly placed inside a split infinitive?', ['An adverb', 'A proper noun', 'A conjunction', 'A preposition'], 0),
   ('How do many modern style guides view split infinitives?', ['They often accept the construction when it improves clarity or sounds natural', 'They always forbid the construction under every circumstance', 'They require every sentence to contain one', 'They consider the construction to be grammatically impossible'], 0),
   ('Why might a writer choose to avoid a split infinitive in very formal writing?', ['Some traditional style guides and readers still consider it less formal or correct', 'Split infinitives are always required in formal writing', 'Formal writing never contains any infinitives', 'Avoiding split infinitives always makes a sentence less clear'], 0)]),
M('Number Theory: An Introduction to Amicable Numbers',
  'Grade 8 Math strand: two numbers are called amicable if the sum of the proper divisors of each number equals the other number, forming a pair connected through their divisors rather than through any obvious numerical similarity.',
  [('What makes two numbers amicable?', ['The sum of the proper divisors of each number equals the other number', 'Both numbers are always exactly equal to each other', 'Both numbers must be prime', 'Neither number can have any divisors at all'], 0),
   ('What are proper divisors of a number?', ['All the positive divisors of a number except the number itself', 'Only the number one and the number itself', 'Every negative number smaller than the number', 'A single divisor chosen at random'], 0),
   ('How many numbers are typically involved in an amicable relationship?', ['Two numbers, forming a pair', 'Exactly one number', 'A minimum of ten numbers', 'An undefined and unlimited quantity'], 0),
   ('What is the smallest known pair of amicable numbers?', ['220 and 284', '6 and 28', '10 and 20', '100 and 200'], 0),
   ('Why do mathematicians find amicable numbers an interesting area of number theory?', ['They reveal unexpected numerical relationships that require careful calculation to discover', 'Amicable numbers have no interesting mathematical properties', 'Every pair of numbers is automatically amicable', 'Amicable numbers can only be whole numbers less than five'], 0)]),
Sc('Technology: How GPS Satellites Determine Location',
   'Grade 8 Science strand: the Global Positioning System uses a network of orbiting satellites that continuously transmit timed signals, allowing a receiver on Earth to calculate its exact location by measuring how long each signal took to arrive from multiple satellites.',
   [('What does the Global Positioning System rely on?', ['A network of orbiting satellites transmitting timed signals', 'A single satellite positioned above the North Pole', 'Underground cables connected to every city', 'Radio towers built only along coastlines'], 0),
    ('How does a GPS receiver calculate its location?', ['By measuring how long signals took to arrive from multiple satellites', 'By guessing based on the time of day', 'By measuring the temperature of the surrounding air', 'By counting the number of clouds overhead'], 0),
    ('Why must a GPS receiver use signals from several satellites rather than just one?', ['Multiple signals are needed to accurately pinpoint a precise location', 'A single satellite always provides a perfectly accurate location', 'Using more than one satellite makes the signal weaker', 'GPS receivers are physically unable to detect more than one satellite'], 0),
    ('What kind of information do GPS satellites continuously transmit?', ['Timed signals marking exactly when each signal was sent', 'Photographs of the Earths surface', 'Weather forecasts for the entire planet', 'Text messages intended for individual users'], 0),
    ('Why is extremely precise timing important for GPS accuracy?', ['Even tiny timing errors can translate into significant errors in calculated position', 'Timing has no effect on the accuracy of a GPS location', 'GPS satellites do not use timing information at all', 'Precise timing only matters for satellites, never for receivers'], 0)]),
H('The Old Age Pensions Act of 1927',
  'Grade 8 History strand: the Old Age Pensions Act of 1927 established a shared federal-provincial pension for Canadians over the age of seventy who met certain income requirements, marking an early step toward the modern Canadian social welfare system.',
  [('In what year was the Old Age Pensions Act passed?', ['1927', '1867', '1911', '1949'], 0),
   ('What did the Old Age Pensions Act establish?', ['A shared federal-provincial pension for eligible older Canadians', 'A new national railway system', 'A tax exclusively for young workers', 'A ban on all provincial pensions'], 0),
   ('What age did a Canadian generally need to reach to qualify for the original pension?', ['Seventy', 'Twenty-five', 'Forty', 'Fifty-five'], 0),
   ('What kind of requirement did applicants for the pension also need to meet?', ['An income requirement', 'A requirement to own a car', 'A requirement to live in a major city', 'A requirement to speak more than one language'], 0),
   ('Why is the Old Age Pensions Act of 1927 considered an important step in Canadian history?', ['It marked an early stage in the development of Canadas modern social welfare system', 'It eliminated all forms of government support for citizens', 'It had no lasting effect on Canadian social policy', 'It only applied to residents of a single city'], 0)]),
]),
day(157, [
L('Vocabulary: Clipped Words and Abbreviated Forms',
  'Grade 8 Language strand: a clipped word is formed by shortening a longer word while keeping the same basic meaning, such as gym from gymnasium or phone from telephone, and clipping is a common way that informal vocabulary enters everyday language.',
  [('What is a clipped word?', ['A word formed by shortening a longer word while keeping the same basic meaning', 'A word created by combining two unrelated words', 'A word with no defined meaning at all', 'A word borrowed directly from another language with no change'], 0),
   ('Which of these is an example of a clipped word?', ['Gym, shortened from gymnasium', 'Bookshelf, combining book and shelf', 'Sandwich, named after a person', 'Umbrella, borrowed from another language'], 0),
   ('Where do clipped words most commonly appear?', ['In informal, everyday spoken and written language', 'Only in formal legal documents', 'Only in ancient historical texts', 'Clipped words never appear in any form of language'], 0),
   ('Why might a clipped word eventually become as common as its original full form?', ['Frequent use in casual speech can make the shorter form widely accepted over time', 'Clipped words are always immediately rejected by speakers', 'Shortened words are grammatically forbidden in any context', 'Clipped words never gain acceptance in everyday use'], 0),
   ('Why is studying clipped words useful when analyzing how language changes?', ['It shows one common way that vocabulary evolves to become more efficient over time', 'Clipped words provide no insight into how language evolves', 'Vocabulary never changes or evolves over time', 'Clipping has no connection to the study of language change'], 0)]),
M('Statistics: An Introduction to Simpsons Paradox',
  'Grade 8 Math strand: Simpsons Paradox occurs when a trend appears in several separate groups of data but disappears or reverses when the groups are combined, showing why data must be examined carefully before drawing broad conclusions.',
  [('What is Simpsons Paradox?', ['A trend that appears in separate groups but disappears or reverses when combined', 'A rule that always guarantees accurate statistical conclusions', 'A method for rounding decimal numbers', 'A law describing how probabilities always increase over time'], 0),
   ('Why does Simpsons Paradox make data analysis challenging?', ['Combining groups can produce a misleading overall trend that hides what is happening within each group', 'It makes every statistical conclusion automatically correct', 'It only occurs with data sets containing a single value', 'It has no effect on how data should be interpreted'], 0),
   ('What does Simpsons Paradox demonstrate about drawing conclusions from data?', ['Data must be examined carefully, considering how groups are combined, before drawing broad conclusions', 'Conclusions can always be drawn instantly with no analysis required', 'Combining groups of data never affects the conclusions drawn', 'Data should never be separated into groups under any circumstance'], 0),
   ('In which field might Simpsons Paradox commonly arise?', ['Comparing outcomes across combined groups, such as in medical studies', 'Only in the study of ancient languages', 'Only in the design of video games', 'Only in the study of weather on other planets'], 0),
   ('Why is awareness of Simpsons Paradox important for interpreting statistics in the news?', ['It helps prevent readers from being misled by conclusions drawn from improperly combined data', 'It guarantees that news reports never contain any errors', 'It has no relevance to how statistics are reported', 'It only matters for statisticians, never for the general public'], 0)]),
Sc('Chemistry: Catalysts and Reaction Rates',
   'Grade 8 Science strand: a catalyst is a substance that increases the rate of a chemical reaction without being permanently consumed in the process, often by providing an alternative pathway that requires less energy to begin the reaction.',
   [('What does a catalyst do to a chemical reaction?', ['Increases its rate without being permanently consumed', 'Always stops the reaction from occurring', 'Permanently disappears after a single use', 'Has no measurable effect on the reaction'], 0),
    ('What happens to a catalyst after a reaction is complete?', ['It remains chemically unchanged and can be used again', 'It is permanently destroyed and cannot be reused', 'It transforms into an entirely different element', 'It becomes part of the final product permanently'], 0),
    ('How does a catalyst typically speed up a reaction?', ['By providing an alternative pathway that requires less energy to begin', 'By increasing the amount of energy required to begin the reaction', 'By removing all reactants from the reaction', 'By cooling the reaction to a very low temperature'], 0),
    ('Which of these is an example of a catalyst in everyday life?', ['An enzyme that speeds up digestion in the body', 'A rock sitting motionless on the ground', 'A shadow cast by a tree', 'A sound wave travelling through air'], 0),
    ('Why are catalysts important in industrial chemical processes?', ['They can make reactions faster and more energy-efficient on a large scale', 'They always make industrial processes slower and less efficient', 'Catalysts have no role in any industrial process', 'They permanently prevent any reaction from occurring'], 0)]),
H('The Formation of Trans-Canada Air Lines in 1937',
  'Grade 8 History strand: established by the federal government in 1937 as a Crown corporation, Trans-Canada Air Lines became the countrys first major national airline, connecting distant Canadian cities and later evolving into Air Canada.',
  [('In what year was Trans-Canada Air Lines established?', ['1937', '1867', '1905', '1949'], 0),
   ('What kind of organization was Trans-Canada Air Lines when it was created?', ['A federal Crown corporation', 'A privately owned foreign company', 'A provincial ministry with no airline operations', 'A charitable, not-for-profit organization'], 0),
   ('What was significant about Trans-Canada Air Lines when it began operating?', ['It became the countrys first major national airline', 'It was the first railway company in Canada', 'It was the last airline ever created in Canada', 'It operated exclusively outside of Canada'], 0),
   ('What did Trans-Canada Air Lines eventually become?', ['Air Canada', 'The Canadian National Railway', 'The Royal Canadian Air Force', 'The Canadian Coast Guard'], 0),
   ('Why might the federal government have wanted to establish a national airline in the 1930s?', ['To connect distant Canadian cities and support national transportation and communication', 'To eliminate all forms of transportation across Canada', 'To discourage travel between Canadian provinces', 'Air travel had no benefit to a country as large as Canada'], 0)]),
]),
day(158, [
L('Reading: Analyzing Parody and Pastiche in Literature',
  'Grade 8 Language strand: parody imitates the style of a work or genre to mock or comment on it humorously, while pastiche imitates a style out of admiration rather than mockery, and distinguishing between the two helps readers understand an authors purpose.',
  [('What is the main purpose of parody?', ['To imitate a work or genre in order to mock or comment on it humorously', 'To copy a work exactly with no changes at all', 'To translate a text into another language', 'To remove all humour from a piece of writing'], 0),
   ('How does pastiche differ from parody?', ['Pastiche imitates a style out of admiration rather than mockery', 'Pastiche always mocks the original work more harshly than parody', 'There is no difference between pastiche and parody', 'Pastiche never imitates another authors style'], 0),
   ('Which is an example of parody?', ['A humorous piece that exaggerates the style of a famous novel to poke fun at it', 'A serious biography with no humour', 'A dictionary definition of a common word', 'A weather report describing tomorrows forecast'], 0),
   ('Why might an author choose to write a pastiche instead of an original work?', ['To pay tribute to a style or author they admire', 'To completely destroy the reputation of another author', 'Pastiche is never used by authors for any reason', 'To avoid using any recognizable style at all'], 0),
   ('Why is distinguishing parody from pastiche useful when analyzing a text?', ['It helps readers understand whether an author intends to criticize or celebrate the work being imitated', 'This distinction has no effect on understanding a text', 'Parody and pastiche always have the exact same purpose', 'Only professional critics can ever notice this distinction'], 0)]),
M('Algebra: An Introduction to Vector Spaces',
  'Grade 8 Math strand: a vector space is a collection of objects called vectors that can be added together and multiplied by numbers called scalars, following a consistent set of rules that generalize the familiar properties of vectors in two and three dimensions.',
  [('What is a vector space?', ['A collection of vectors that can be added together and multiplied by scalars', 'A single fixed point with no other properties', 'A shape that has no defined dimensions', 'A list of unrelated numbers with no structure'], 0),
   ('What is a scalar in the context of a vector space?', ['A number used to multiply a vector', 'A type of vector with no numerical value', 'A shape with exactly four sides', 'A unit used only to measure temperature'], 0),
   ('What must a set of rules in a vector space consistently do?', ['Generalize the familiar properties of vectors in two and three dimensions', 'Apply only to numbers smaller than ten', 'Contradict the basic properties of vectors', 'Ignore all mathematical operations entirely'], 0),
   ('Which of these operations must be defined within a vector space?', ['Vector addition and scalar multiplication', 'Only division of vectors by other vectors', 'Only the square root of a vector', 'Only rounding a vector to the nearest whole number'], 0),
   ('Why do mathematicians study vector spaces beyond two or three dimensions?', ['The same structure can describe more abstract systems used across science and engineering', 'Vector spaces beyond three dimensions have no practical use', 'Higher-dimensional vector spaces are mathematically impossible', 'Only two- and three-dimensional vectors exist in mathematics'], 0)]),
Sc('Physics: The Electromagnetic Spectrum and Its Applications',
   'Grade 8 Science strand: the electromagnetic spectrum includes all types of electromagnetic radiation, ranging from long-wavelength radio waves to short-wavelength gamma rays, with visible light forming only a small portion used by the human eye.',
   [('What does the electromagnetic spectrum include?', ['All types of electromagnetic radiation', 'Only the light visible to the human eye', 'Only sound waves travelling through air', 'Only radio waves used for broadcasting'], 0),
    ('Which type of electromagnetic wave has the longest wavelength?', ['Radio waves', 'Gamma rays', 'X-rays', 'Ultraviolet light'], 0),
    ('Which type of electromagnetic wave has the shortest wavelength?', ['Gamma rays', 'Radio waves', 'Microwaves', 'Infrared light'], 0),
    ('What portion of the electromagnetic spectrum can the human eye detect?', ['Only a small portion, known as visible light', 'The entire electromagnetic spectrum', 'Only radio waves and microwaves', 'None of the electromagnetic spectrum at all'], 0),
    ('Why are different parts of the electromagnetic spectrum used for different technologies?', ['Each wavelength range has properties suited to specific practical applications, such as communication or medical imaging', 'Every part of the spectrum behaves in exactly the same way', 'Only visible light has any practical technological use', 'The electromagnetic spectrum has no connection to modern technology'], 0)]),
H('The Dust Bowl and Drought on the Canadian Prairies During the 1930s',
  'Grade 8 History strand: during the 1930s, prolonged drought and severe soil erosion turned large areas of the Canadian prairies into a dust bowl, devastating farm income and forcing many families to abandon their land during the depths of the Great Depression.',
  [('What environmental conditions caused the prairie dust bowl of the 1930s?', ['Prolonged drought and severe soil erosion', 'Excessive rainfall and flooding', 'A sudden drop in temperature across the entire country', 'A shortage of available farmland'], 0),
   ('What effect did the dust bowl have on prairie farm income?', ['It devastated farm income', 'It caused farm income to rise dramatically', 'It had no effect on farm income at all', 'It only affected income in coastal provinces'], 0),
   ('What did many prairie families do as a result of the dust bowl?', ['Abandon their land', 'Purchase additional farmland', 'Move to the prairies for the first time', 'Expand their farms significantly'], 0),
   ('During which broader economic crisis did the prairie dust bowl occur?', ['The Great Depression', 'World War II', 'The Cold War', 'The 1990s recession'], 0),
   ('Why did soil erosion worsen so severely on the prairies during this drought?', ['Years of farming practices combined with drought left topsoil exposed and vulnerable to wind', 'Soil erosion never occurs during a drought', 'The prairies received far too much rainfall during this period', 'Farming practices had no connection to the severity of soil erosion'], 0)]),
]),
day(159, [
L('Writing: The Character Sketch and Descriptive Writing',
  'Grade 8 Language strand: a character sketch is a short piece of descriptive writing that captures a persons physical appearance, personality, and mannerisms through vivid, specific detail rather than a simple list of traits.',
  [('What does a character sketch capture?', ['A persons physical appearance, personality, and mannerisms', 'Only the exact date a person was born', 'A list of unrelated historical events', 'A summary of an entirely different persons life'], 0),
   ('What kind of detail does effective descriptive writing rely on?', ['Vivid, specific detail rather than a simple list of traits', 'Vague, general statements with no specific detail', 'A single one-word description', 'No descriptive detail of any kind'], 0),
   ('Why might a writer include a characters mannerisms in a sketch?', ['Small habits and gestures can reveal personality more effectively than direct statements', 'Mannerisms have no connection to a characters personality', 'Including mannerisms always makes a sketch less effective', 'A character sketch is required to exclude all behavioural detail'], 0),
   ('What distinguishes a character sketch from a full narrative?', ['A character sketch focuses on describing a character rather than telling a complete story', 'A character sketch always contains a complete plot with a beginning, middle, and end', 'There is no meaningful difference between the two forms', 'A character sketch must always be longer than a full narrative'], 0),
   ('Why is descriptive precision important when writing a character sketch?', ['Specific, concrete details help a reader form a clear and vivid mental image of the character', 'Vague descriptions always create a clearer image than specific ones', 'Precision has no effect on how a reader imagines a character', 'A character sketch should avoid describing the character entirely'], 0)]),
M('Calculus Preview: An Introduction to Related Rates',
  'Grade 8 Math strand: related rates problems use derivatives to find how quickly one quantity changes in relation to another quantity it depends on, such as finding how fast the radius of a balloon grows as it is filled with air at a known rate.',
  [('What do related rates problems find?', ['How quickly one quantity changes in relation to another quantity it depends on', 'The exact area of a single fixed shape', 'A rule for rounding decimals to the nearest whole number', 'The colour of a graphed function'], 0),
   ('What calculus concept is central to solving a related rates problem?', ['The derivative', 'The greatest common divisor', 'A probability distribution', 'A geometric proof with no calculation'], 0),
   ('Which is an example of a related rates problem?', ['Finding how fast a balloons radius grows as air is added at a known rate', 'Finding the exact colour of a balloon', 'Counting the total number of balloons in a room', 'Measuring the weight of a balloon at rest'], 0),
   ('Why must two related quantities in this type of problem be connected by an equation?', ['The equation allows their rates of change to be linked through differentiation', 'An equation has no role in solving a related rates problem', 'The two quantities must always be completely unrelated', 'Equations can only describe quantities that never change'], 0),
   ('Why are related rates problems useful in real-world applications?', ['They model how interconnected quantities change together over time in physical situations', 'They have no real-world applications of any kind', 'They only apply to quantities that remain constant forever', 'Related rates problems cannot be solved using calculus'], 0)]),
Sc('Biology: Coevolution and Predator-Prey Adaptations',
   'Grade 8 Science strand: coevolution occurs when two species influence each others evolution over time, often seen in predator-prey relationships where predators evolve better hunting adaptations while prey simultaneously evolve improved defenses.',
   [('What is coevolution?', ['A process where two species influence each others evolution over time', 'A process where a single species evolves with no outside influence', 'A process that only occurs in plants, never animals', 'A process where evolution stops entirely for both species'], 0),
    ('In a predator-prey relationship, what might predators evolve?', ['Better hunting adaptations', 'A complete inability to move', 'Adaptations that make hunting impossible', 'No adaptations of any kind'], 0),
    ('In a predator-prey relationship, what might prey evolve in response?', ['Improved defenses against predators', 'A complete loss of all senses', 'Adaptations that attract more predators', 'No response of any kind'], 0),
    ('Why is this evolutionary relationship often described as an ongoing arms race?', ['Improvements in one species often drive further adaptations in the other over time', 'Neither species ever changes in response to the other', 'The relationship between predator and prey never involves any change', 'Only predators are capable of evolving new adaptations'], 0),
    ('Why is coevolution considered an important concept in ecology?', ['It helps explain how closely interacting species continue to shape each others survival strategies over time', 'It has no connection to how species interact with one another', 'Coevolution only applies to species that never interact', 'It proves that species never adapt to their environment'], 0)]),
H('The Bank of Canada Act and the Creation of Canadas Central Bank',
  'Grade 8 History strand: passed in 1934, the Bank of Canada Act created the Bank of Canada, the countrys central bank, giving the federal government a formal tool to manage the national currency and monetary policy for the first time.',
  [('In what year was the Bank of Canada Act passed?', ['1934', '1867', '1911', '1949'], 0),
   ('What institution did the Bank of Canada Act create?', ['The Bank of Canada, the countrys central bank', 'The Supreme Court of Canada', 'The Royal Canadian Mounted Police', 'The Canadian National Railway'], 0),
   ('What new formal tool did the federal government gain as a result of the Bank of Canada Act?', ['A means to manage the national currency and monetary policy', 'Control over all provincial school systems', 'Authority over international shipping routes', 'The power to appoint provincial premiers'], 0),
   ('Why might the Great Depression have encouraged the creation of a central bank?', ['Economic instability highlighted the need for more coordinated national monetary management', 'The Great Depression had no connection to Canadas banking system', 'Economic stability during the Depression removed any need for a central bank', 'A central bank was created decades before the Great Depression began'], 0),
   ('Why is the creation of the Bank of Canada considered a significant milestone in Canadian economic history?', ['It gave Canada its own institution to oversee monetary policy rather than relying on other mechanisms', 'It ended all banking activity in Canada permanently', 'It transferred control of Canadian currency to another country', 'It had no lasting impact on Canadas economy'], 0)]),
]),
day(160, [
L('Language Review: Grammar, Vocabulary, and Literary Analysis (Days 151-159)',
  'Grade 8 Language strand review: students revisit inverted sentence structure, slang and generational language, static and dynamic characters, the problem-solution essay, and parody and pastiche.',
  [('What does inverted sentence structure reverse?', ['The usual subject-verb order', 'The meaning of every word in a sentence', 'The spelling of a word', 'The tense of a verb only'], 0),
   ('What is slang?', ['Informal vocabulary that develops within a particular group or generation', 'A formal citation style used in academic writing', 'A grammatical rule about verb tense', 'A punctuation mark used to end a question'], 0),
   ('What defines a dynamic character?', ['A character who undergoes significant internal change during a story', 'A character who has no personality traits at all', 'A character who appears in only one sentence', 'A character who is identical to every other character'], 0),
   ('What does a problem-solution essay identify?', ['A specific issue along with its causes and effects', 'A random collection of unrelated topics', 'A single sentence with no supporting explanation', 'A list of characters from a novel'], 0),
   ('How does pastiche differ from parody?', ['Pastiche imitates a style out of admiration rather than mockery', 'Pastiche always mocks the original work more harshly than parody', 'There is no difference between pastiche and parody', 'Pastiche never imitates another authors style'], 0)]),
M('Math Review: Statistics, Algebra, and Number Theory (Days 151-159)',
  'Grade 8 Math strand review: students revisit the Central Limit Theorem, the Euclidean Algorithm, function composition, Markov chains, and Simpsons Paradox.',
  [('What does the Central Limit Theorem describe?', ['How the distribution of sample means tends toward a normal distribution as sample size grows', 'How to calculate the area of a triangle', 'A rule for rounding decimals', 'A method for factoring polynomials'], 0),
   ('What does the Euclidean Algorithm find?', ['The greatest common divisor of two integers', 'The least common multiple of two integers only', 'The square root of a number', 'The average of two integers'], 0),
   ('What does function composition do?', ['Combines two functions by applying one to the result of another', 'Deletes one function entirely', 'Converts a function into a single number with no variables', 'Removes all variables from a function'], 0),
   ('In a Markov chain, what does the probability of the next state depend on?', ['Only the current state', 'Every state that has ever occurred in the past', 'A state that has not yet been defined', 'Nothing at all, since the process is entirely undefined'], 0),
   ('What is Simpsons Paradox?', ['A trend that appears in separate groups but disappears or reverses when combined', 'A rule that always guarantees accurate statistical conclusions', 'A method for rounding decimal numbers', 'A law describing how probabilities always increase over time'], 0)]),
Sc('Science Review: Chemistry, Earth Science, and Space Science (Days 151-159)',
   'Grade 8 Science strand review: students revisit electrolysis and electroplating, static electricity, ocean currents and thermohaline circulation, the structure of the Milky Way, and catalysts and reaction rates.',
   [('What does electrolysis use to drive a chemical reaction?', ['An electric current', 'A magnetic field only', 'A change in air pressure', 'Sound waves'], 0),
    ('What is the transfer of electrons through rubbing known as?', ['The triboelectric effect', 'The photoelectric effect', 'Electromagnetic induction', 'Nuclear fission'], 0),
    ('What is thermohaline circulation?', ['A deep, slow-moving global conveyor of ocean water driven by temperature and salinity differences', 'A fast-moving surface current found only near the equator', 'A process that only occurs in freshwater lakes', 'A current caused entirely by tides alone'], 0),
    ('What type of galaxy is the Milky Way?', ['A large spiral galaxy', 'A small, perfectly spherical galaxy', 'A galaxy with no defined shape', 'A galaxy made entirely of comets'], 0),
    ('What does a catalyst do to a chemical reaction?', ['Increases its rate without being permanently consumed', 'Always stops the reaction from occurring', 'Permanently disappears after a single use', 'Has no measurable effect on the reaction'], 0)]),
H('History Review: Depression-Era Politics and Social Reform (Days 151-159)',
  'Grade 8 History strand review: students revisit Agnes Macphail, the 1918 Spanish Flu pandemic, the Rowell-Sirois Commission, the Old Age Pensions Act of 1927, and the Bank of Canada Act.',
  [('What distinction did Agnes Macphail hold as a member of Parliament?', ['She was the first woman elected to the Canadian House of Commons', 'She was the first prime minister of Canada', 'She was the first woman appointed to the Senate', 'She was the first woman to serve as a provincial premier'], 0),
   ('What is the 1918 influenza pandemic commonly known as?', ['The Spanish Flu', 'The Asian Flu', 'The Black Death', 'The Great Fever'], 0),
   ('What relationship did the Rowell-Sirois Commission examine?', ['The financial relationship between the federal and provincial governments', 'Canadas relationship with the United Nations', 'The relationship between Canada and France', 'The structure of Canadas court system'], 0),
   ('What did the Old Age Pensions Act establish?', ['A shared federal-provincial pension for eligible older Canadians', 'A new national railway system', 'A tax exclusively for young workers', 'A ban on all provincial pensions'], 0),
   ('What institution did the Bank of Canada Act create?', ['The Bank of Canada, the countrys central bank', 'The Supreme Court of Canada', 'The Royal Canadian Mounted Police', 'The Canadian National Railway'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_151_160)
    append_to(8, g8_151_160)
