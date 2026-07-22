#!/usr/bin/env python3
"""Grade 8, Days 91-100 -- extends Grade 8 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade8.json):
frame narratives, elegy and tribute writing, appositives, neologisms,
epistolary novels, sponsored content and native advertising, worldbuilding
in speculative fiction, subordinate clauses, motif and recurring imagery;
logarithms, polynomial long division, function notation/domain/range, the
Fibonacci sequence and golden ratio, probability trees, piecewise
functions, coordinate proofs, rational expressions, the unit circle;
volcanoes, radioactivity and nuclear decay, biomechanics, aerodynamics
and flight, data encryption, the digestive system, symbiosis, weather
fronts and air masses, circadian rhythms; the Halibut Treaty of 1923, the
Chanak Affair, the Balfour Declaration, Clifford Sifton and Prairie
settlement, the Group of Seven, the Progressive Party, the founding of
the United Church of Canada, the Bluenose, and the King-Byng Affair.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260927):
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


g8_91_100 = [
day(91, [
L('Reading: Analyzing Frame Narratives',
  'Grade 8 Language strand: a frame narrative is a story that contains another story within it, using an outer frame, such as a narrator recounting a tale, to introduce and enclose the inner story.',
  [('What is a frame narrative?', ['A story that contains another story within it', 'A story with only one single event and no characters', 'A concept unrelated to reading', 'A poem written in a fixed rhyme scheme'], 0),
   ('Does a frame narrative use an outer story to introduce an inner story?', ['Yes', 'No, a frame narrative never contains more than one story', 'A concept unrelated to frame narratives', 'The inner story always comes before the outer frame'], 0),
   ('Which of these best describes the outer part of a frame narrative?', ['The frame, which introduces and encloses the inner story', 'The climax of the inner story only', 'A concept unrelated to frame narratives', 'A glossary of unfamiliar words'], 0),
   ('Why might an author use a frame narrative to tell a story?', ['It can add context, perspective, or a reason for why the inner story is being told', 'A frame narrative never adds any context to a story', 'This concept has no connection to literature', 'Frame narratives always confuse readers with no added meaning'], 0),
   ('Why might a frame narrative change how readers interpret the inner story?', ['The outer narrator’s perspective can shape how trustworthy or meaningful the inner story feels', 'The outer narrator never has any effect on how a story is understood', 'This concept has no relevance to reading comprehension', 'Inner stories are always understood exactly the same regardless of framing'], 0)]),
M('Introduction to Logarithms',
  'Grade 8 Math strand: a logarithm is the inverse operation of exponentiation, answering the question of what exponent a given base must be raised to in order to produce a certain number.',
  [('What is a logarithm the inverse operation of?', ['Exponentiation', 'Addition', 'A concept unrelated to math', 'Division only'], 0),
   ('Does a logarithm answer what exponent a base must be raised to in order to reach a certain number?', ['Yes', 'No, logarithms have no connection to exponents', 'A concept unrelated to logarithms', 'Logarithms only ever apply to subtraction'], 0),
   ('What is the logarithm base 10 of 100?', ['2', '10', '100', '20'], 0),
   ('Why might logarithms be useful for solving an equation where the unknown value is an exponent?', ['They allow you to isolate and solve directly for the exponent', 'Logarithms never help with solving any type of equation', 'This concept has no connection to algebra', 'Exponents can never be solved for using any mathematical method'], 0),
   ('Why are logarithms used to measure things like earthquake magnitude on the Richter scale?', ['They can compress an enormous range of values into a more manageable scale', 'Logarithms have no connection to measuring real-world phenomena', 'This concept has no relevance to math', 'Earthquake magnitude is never measured using any mathematical scale'], 0)]),
Sc('Science: Volcanoes and Types of Volcanic Eruptions',
   'Grade 8 Science strand: a volcano is an opening in Earth’s crust where molten rock, gas, and ash can escape, with eruptions ranging from slow-flowing effusive events to violent, explosive ones.',
   [('What is a volcano?', ['An opening in Earth’s crust where molten rock, gas, and ash can escape', 'A large flat area with no geological activity', 'A concept unrelated to earth science', 'A type of cloud formation'], 0),
    ('Does magma become known as lava once it reaches Earth’s surface?', ['Yes', 'No, magma and lava are never related terms', 'A concept unrelated to volcanoes', 'Lava only exists underground, never on the surface'], 0),
    ('Name one type of volcanic eruption, such as effusive or explosive.', ['Explosive', 'A concept unrelated to volcanoes', 'Evaporative', 'Photosynthetic'], 0),
    ('Why might a volcano with thick, sticky magma tend to erupt more explosively than one with thin, runny magma?', ['Thick magma traps gases more easily, building pressure until it is released suddenly', 'Magma thickness never has any effect on how a volcano erupts', 'This concept has no connection to earth science', 'Thin magma always causes the most violent eruptions'], 0),
    ('Why do scientists monitor volcanoes for signs like gas emissions and small earthquakes?', ['These signs can help predict when an eruption may be about to occur', 'Monitoring volcanoes never provides any useful information', 'This concept has no relevance to science', 'Volcanic eruptions always happen with absolutely no warning signs'], 0)]),
H('The Halibut Treaty of 1923 and Canada’s Growing Independence',
  'Grade 8 History strand: the Halibut Treaty of 1923 was the first international treaty negotiated and signed independently by Canada, without direct British involvement, marking a step toward full Canadian autonomy in foreign affairs.',
  [('In what year was the Halibut Treaty signed?', ['1923', '1867', '1945', '1867'], 0),
   ('Was the Halibut Treaty the first international treaty negotiated and signed independently by Canada?', ['Yes', 'No, Canada had already signed many treaties fully on its own before this', 'A concept unrelated to the Halibut Treaty', 'This treaty was actually signed entirely by Britain, not Canada'], 0),
   ('Did the Halibut Treaty involve direct British involvement in the negotiations?', ['No', 'Yes, Britain led every part of the negotiations', 'A concept unrelated to the Halibut Treaty', 'Britain and Canada negotiated the treaty together equally'], 0),
   ('Why might the Halibut Treaty be considered an important step toward Canadian autonomy?', ['It showed Canada could conduct its own foreign relations without depending on Britain to negotiate on its behalf', 'The treaty had no real significance for Canadian independence', 'This concept has no connection to Canadian history', 'Canada’s foreign policy never changed as a result of this treaty'], 0),
   ('Why is it valuable for students to study early steps toward Canadian independence, like the Halibut Treaty?', ['It helps show how Canada gradually gained control over its own foreign policy and international relationships', 'Early steps toward independence have no relevance to understanding Canada today', 'This concept has no relevance to History', 'Canada’s foreign policy has never changed throughout its history'], 0)]),
]),

day(92, [
L('Writing: The Elegy and Tribute Writing',
  'Grade 8 Language strand: an elegy is a reflective piece of writing, often a poem, that mourns or honours someone who has died, expressing both grief and appreciation for their life.',
  [('What does an elegy typically do?', ['Mourns or honours someone who has died', 'Describes the steps of a science experiment', 'A concept unrelated to writing', 'Advertises a product for sale'], 0),
   ('Is an elegy often written in poem form?', ['Yes', 'No, elegies are never written as poems', 'A concept unrelated to elegies', 'Elegies are always written as recipes'], 0),
   ('Does an elegy typically express both grief and appreciation for a person’s life?', ['Yes', 'No, an elegy never expresses any emotion', 'A concept unrelated to elegies', 'An elegy only ever expresses anger'], 0),
   ('Why might a writer include specific memories or qualities of a person in an elegy?', ['It personalizes the tribute and helps readers understand what made that person special', 'Specific memories never add anything meaningful to a tribute', 'This concept has no connection to writing', 'Elegies should never mention any specific details about a person'], 0),
   ('Why might reading elegies help students understand how writers process loss?', ['It shows how emotion and reflection can be shaped into meaningful, structured writing', 'Elegies never reveal anything about how writers process emotion', 'This concept has no relevance to writing', 'Loss and grief are never explored through written work'], 0)]),
M('Polynomial Long Division',
  'Grade 8 Math strand: polynomial long division is a method for dividing a polynomial by another polynomial of equal or lesser degree, following a process similar to long division with numbers.',
  [('What does polynomial long division do?', ['Divides a polynomial by another polynomial', 'Multiplies two polynomials together', 'A concept unrelated to algebra', 'Adds a list of polynomials together'], 0),
   ('Is polynomial long division similar in process to long division with numbers?', ['Yes', 'No, the two processes share no similarities at all', 'A concept unrelated to polynomial long division', 'Polynomial long division never involves any division at all'], 0),
   ('What do you call the polynomial left over after a division that does not divide evenly?', ['The remainder', 'The product', 'A concept unrelated to polynomial division', 'The coefficient'], 0),
   ('Why might polynomial long division be useful when factoring a polynomial?', ['It can help confirm whether a given expression is a factor and simplify the polynomial', 'Polynomial long division never helps with factoring in any way', 'This concept has no connection to algebra', 'Factoring and division are always completely unrelated processes'], 0),
   ('Why is it important to arrange terms in order of degree before starting polynomial long division?', ['Working in order of degree keeps the process organized and prevents errors when combining terms', 'The order of terms never has any effect on the division process', 'This concept has no connection to polynomial long division', 'Terms should always be arranged in a completely random order'], 0)]),
Sc('Science: The Physics of Radioactivity and Nuclear Decay',
   'Grade 8 Science strand: radioactivity occurs when unstable atomic nuclei release energy and particles over time, a process called nuclear decay, which can be used to help determine the age of ancient materials.',
   [('What occurs when unstable atomic nuclei release energy and particles?', ['Radioactivity', 'Photosynthesis', 'A concept unrelated to physics', 'Evaporation'], 0),
    ('Is the process of an unstable nucleus gradually releasing energy called nuclear decay?', ['Yes', 'No, this process has no specific scientific name', 'A concept unrelated to radioactivity', 'This process is only ever called condensation'], 0),
    ('Can nuclear decay be used to help determine the age of ancient materials?', ['Yes', 'No, nuclear decay has no connection to dating materials', 'A concept unrelated to nuclear decay', 'Nuclear decay only ever applies to living organisms'], 0),
    ('Why might scientists use a radioactive isotope’s half-life to estimate the age of a fossil?', ['The predictable decay rate allows scientists to calculate how much time has passed', 'Half-life has no connection to estimating the age of any material', 'This concept has no connection to radioactivity', 'Fossils never contain any radioactive material to measure'], 0),
    ('Why is radioactive material considered potentially hazardous to living things?', ['The energy and particles released can damage cells and biological tissue', 'Radioactive material never has any effect on living cells', 'This concept has no relevance to science', 'Radioactivity only ever affects non-living objects like rocks'], 0)]),
H('The Chanak Affair of 1922',
  'Grade 8 History strand: the Chanak Affair of 1922 occurred when Britain asked Canada for military support in a conflict with Turkey, and Canada’s decision to consult Parliament rather than automatically agreeing signalled a new independence in foreign policy.',
  [('In what year did the Chanak Affair take place?', ['1922', '1867', '1945', '1970'], 0),
   ('Did Britain ask Canada for military support during the Chanak Affair?', ['Yes', 'No, Britain never asked Canada for any support', 'A concept unrelated to the Chanak Affair', 'Canada asked Britain for support instead'], 0),
   ('Did Canada automatically agree to send troops without consulting Parliament?', ['No', 'Yes, Canada agreed immediately with no discussion at all', 'A concept unrelated to the Chanak Affair', 'Parliament was never involved in Canadian decisions at this time'], 0),
   ('Why might Canada’s decision to consult Parliament during the Chanak Affair be seen as a shift in its relationship with Britain?', ['It showed Canada was beginning to make its own foreign policy decisions rather than automatically following Britain’s requests', 'This decision had no effect on Canada’s relationship with Britain', 'This concept has no connection to Canadian history', 'Canada had always made every foreign policy decision independently before this event'], 0),
   ('Why is the Chanak Affair considered an important early example of Canadian foreign policy independence?', ['It set a precedent that Canada would decide for itself whether to become involved in international conflicts', 'The Chanak Affair had no lasting significance in Canadian history', 'This concept has no relevance to History', 'Canada’s foreign policy decisions were never influenced by this event'], 0)]),
]),

day(93, [
L('Grammar: Appositives and Nonrestrictive Elements',
  'Grade 8 Language strand: an appositive is a noun or noun phrase that renames or explains another noun beside it, and nonrestrictive appositives are set off with commas because they add extra, non-essential information.',
  [('What does an appositive do?', ['Renames or explains a noun beside it', 'Replaces a verb in a sentence', 'A concept unrelated to grammar', 'Introduces a new paragraph'], 0),
   ('Are nonrestrictive appositives typically set off with commas?', ['Yes', 'No, nonrestrictive appositives never use commas', 'A concept unrelated to appositives', 'Nonrestrictive appositives always use quotation marks instead'], 0),
   ('Which sentence correctly uses a nonrestrictive appositive?', ['My teacher, Ms. Lee, is very kind.', 'My teacher Ms. Lee is very kind is helpful.', 'Kind my teacher Ms. Lee is very.', 'Very kind, is my teacher Ms. Lee.'], 0),
   ('Why is a nonrestrictive appositive considered non-essential information?', ['The sentence would still make sense and keep its core meaning without it', 'Nonrestrictive appositives always change the entire meaning of a sentence', 'This concept has no connection to grammar', 'Removing a nonrestrictive appositive always makes a sentence incomplete'], 0),
   ('Why might removing the commas around an appositive change how a sentence reads?', ['Commas signal that the appositive is extra information rather than essential to identifying the noun', 'Commas never have any effect on how a sentence is read', 'This concept has no connection to grammar', 'Appositives are never affected by punctuation in any way'], 0)]),
M('Introduction to Function Notation, Domain, and Range',
  'Grade 8 Math strand: function notation, such as f(x), represents the output of a function for a given input, while the domain is the set of possible inputs and the range is the set of possible outputs.',
  [('What does function notation like f(x) represent?', ['The output of a function for a given input', 'A random number with no connection to the function', 'A concept unrelated to algebra', 'The name of a variable with no other meaning'], 0),
   ('What is the domain of a function?', ['The set of possible inputs', 'The set of possible outputs', 'A concept unrelated to functions', 'A single fixed number only'], 0),
   ('What is the range of a function?', ['The set of possible outputs', 'The set of possible inputs', 'A concept unrelated to functions', 'A single fixed number only'], 0),
   ('If f(x) = x + 2, what is f(3)?', ['5', '6', '3', '2'], 0),
   ('Why is function notation useful for describing a relationship between two variables?', ['It clearly shows how an output value depends on a specific input value', 'Function notation never shows any relationship between variables', 'This concept has no connection to algebra', 'Inputs and outputs are always completely unrelated to each other'], 0)]),
Sc('Science: Biomechanics: How Muscles and Bones Work Together',
   'Grade 8 Science strand: biomechanics studies how muscles, bones, and joints work together as levers to produce movement, with muscles contracting to pull on bones across a joint.',
   [('What does biomechanics study?', ['How muscles, bones, and joints work together to produce movement', 'How rocks form deep underground', 'A concept unrelated to science', 'How plants absorb sunlight'], 0),
    ('Do muscles contract to pull on bones across a joint?', ['Yes', 'No, muscles never connect to bones in any way', 'A concept unrelated to biomechanics', 'Muscles only ever push bones, never pull them'], 0),
    ('What connects muscle to bone, allowing force to be transferred?', ['A tendon', 'A concept unrelated to biomechanics', 'A vein', 'A nerve ending only'], 0),
    ('Why might the arrangement of muscles and bones in the body be compared to a system of levers?', ['Because they work together to produce and amplify force and movement around a joint', 'Muscles and bones never work together in any coordinated way', 'This concept has no connection to biomechanics', 'Levers have no similarities to how the human body moves'], 0),
    ('Why is understanding biomechanics useful for designing prosthetic limbs?', ['It helps engineers replicate how natural muscles and joints move to create functional, effective devices', 'Biomechanics has no connection to designing prosthetic limbs', 'This concept has no relevance to science', 'Prosthetic limbs are designed with no consideration of how the body moves'], 0)]),
H('The Balfour Declaration of 1926',
  'Grade 8 History strand: the Balfour Declaration of 1926 formally recognized Canada and other British dominions as autonomous communities equal in status to Britain, laying the groundwork for the later Statute of Westminster.',
  [('In what year was the Balfour Declaration issued?', ['1926', '1867', '1945', '1970'], 0),
   ('Did the Balfour Declaration recognize dominions like Canada as equal in status to Britain?', ['Yes', 'No, it declared dominions to be entirely subordinate to Britain', 'A concept unrelated to the Balfour Declaration', 'The declaration had no connection to Canada at all'], 0),
   ('Did the Balfour Declaration lay groundwork for the later Statute of Westminster?', ['Yes', 'No, the two events had no connection to each other', 'A concept unrelated to the Balfour Declaration', 'The Statute of Westminster came many centuries before this declaration'], 0),
   ('Why might the Balfour Declaration be considered a major milestone in Canada’s path to independence?', ['It formally recognized Canada’s equal status, paving the way for full legal autonomy', 'The declaration had no real effect on Canada’s independence', 'This concept has no connection to Canadian history', 'Canada’s status within the British Empire never changed after this declaration'], 0),
   ('Why is it useful for students to understand the connection between the Balfour Declaration and later Canadian autonomy?', ['It shows how Canadian independence developed gradually through a series of connected historical milestones', 'The Balfour Declaration has no relevance to understanding Canadian independence', 'This concept has no relevance to History', 'Canadian autonomy developed instantly with no connection to earlier events'], 0)]),
]),

day(94, [
L('Vocabulary: Neologisms and Language Change',
  'Grade 8 Language strand: a neologism is a newly coined word or expression that enters a language, often created to describe new technology, culture, or ideas.',
  [('What is a neologism?', ['A newly coined word or expression', 'A word that has existed unchanged for centuries', 'A concept unrelated to vocabulary', 'A grammatical rule with no connection to words'], 0),
   ('Are neologisms often created to describe new technology or ideas?', ['Yes', 'No, neologisms are never connected to new ideas or technology', 'A concept unrelated to neologisms', 'Neologisms only ever describe ancient historical events'], 0),
   ('Which of these is an example of a modern neologism?', ['Selfie', 'Table', 'Run', 'Tree'], 0),
   ('Why might a neologism become widely used in everyday language?', ['It fills a need in the language for describing something new', 'Neologisms are never actually adopted into common usage', 'This concept has no connection to vocabulary', 'New words are always immediately rejected by every speaker'], 0),
   ('Why does language change over time as new neologisms are adopted?', ['Language evolves to reflect the changing needs, culture, and technology of its speakers', 'Language never changes for any reason over time', 'This concept has no relevance to vocabulary', 'New words have no effect on how a language develops'], 0)]),
M('The Fibonacci Sequence and the Golden Ratio',
  'Grade 8 Math strand: the Fibonacci sequence is a pattern where each number is the sum of the two numbers before it, and as the sequence grows, the ratio between consecutive terms approaches the golden ratio.',
  [('In the Fibonacci sequence, how is each new number formed?', ['By adding the two numbers before it', 'By multiplying the previous number by 2', 'A concept unrelated to the Fibonacci sequence', 'By subtracting the previous two numbers'], 0),
   ('What comes next in the sequence 0, 1, 1, 2, 3, 5, 8?', ['13', '10', '11', '15'], 0),
   ('Does the ratio between consecutive Fibonacci terms approach the golden ratio as the sequence grows?', ['Yes', 'No, the ratio never approaches any particular value', 'A concept unrelated to the Fibonacci sequence', 'The ratio becomes completely random as the sequence grows'], 0),
   ('Why is the Fibonacci sequence considered a recursive pattern?', ['Each term depends on the values of previous terms', 'Recursive patterns never depend on any previous values', 'This concept has no connection to math', 'Every term in the sequence is chosen at random'], 0),
   ('Why might the golden ratio and Fibonacci-like patterns appear in nature, such as in spiral shells or flower petals?', ['These patterns often emerge from efficient natural growth processes', 'The golden ratio never actually appears anywhere in nature', 'This concept has no relevance to math', 'Flower petals and shells never follow any mathematical pattern'], 0)]),
Sc('Science: The Physics of Flight and Aerodynamics',
   'Grade 8 Science strand: aerodynamics studies how air moves around objects, and flight depends on four forces, lift, weight, thrust, and drag, working together to allow an aircraft to rise and move forward.',
   [('What does aerodynamics study?', ['How air moves around objects', 'How rocks form over time', 'A concept unrelated to physics', 'How plants grow toward sunlight'], 0),
    ('Name one of the four forces involved in flight, such as lift or drag.', ['Lift', 'A concept unrelated to flight', 'Friction only, with no other force involved', 'Magnetism'], 0),
    ('Does lift need to be greater than weight for an aircraft to rise into the air?', ['Yes', 'No, weight always needs to be greater than lift to rise', 'A concept unrelated to aerodynamics', 'Lift and weight have no connection to whether a plane rises'], 0),
    ('Why is the shape of an airplane wing, called an airfoil, important for generating lift?', ['Its curved shape helps create a pressure difference between the air above and below the wing', 'The shape of a wing never has any effect on generating lift', 'This concept has no connection to aerodynamics', 'Airplane wings are always shaped as perfectly flat rectangles'], 0),
    ('Why must thrust overcome drag for an aircraft to increase its speed?', ['Drag is a resisting force that opposes an aircraft’s forward motion', 'Drag never has any effect on how fast an aircraft can travel', 'This concept has no relevance to science', 'Thrust and drag always work in exactly the same direction'], 0)]),
H('Clifford Sifton and the Settlement of the Canadian Prairies',
  'Grade 8 History strand: as Minister of the Interior in the early 1900s, Clifford Sifton launched an aggressive immigration campaign to attract settlers to the Canadian Prairies, significantly shaping the region’s development.',
  [('What government position did Clifford Sifton hold?', ['Minister of the Interior', 'Prime Minister', 'A concept unrelated to Canadian history', 'Governor General'], 0),
   ('Did Clifford Sifton launch a campaign to attract settlers to the Canadian Prairies?', ['Yes', 'No, Sifton discouraged all settlement of the Prairies', 'A concept unrelated to Clifford Sifton', 'Sifton had no connection to immigration policy at all'], 0),
   ('Around what time period was Clifford Sifton active in this role?', ['The early 1900s', 'The 1700s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
   ('Why might Sifton’s immigration campaign have specifically targeted farmers from certain regions, like Eastern Europe?', ['He believed farmers experienced with harsh climates would be well-suited to settling and working the Prairies', 'Sifton’s campaign never targeted any specific group of people', 'This concept has no connection to Canadian history', 'Farmers from Eastern Europe were never welcomed into Canada during this period'], 0),
   ('Why is Sifton’s immigration policy considered significant to the development of Western Canada?', ['It brought a large wave of settlers whose farming and communities shaped the region’s growth', 'Sifton’s policy had no lasting effect on Western Canada', 'This concept has no relevance to History', 'The Prairies remained completely unsettled throughout this entire period'], 0)]),
]),

day(95, [
L('Reading: Analyzing Epistolary Novels',
  'Grade 8 Language strand: an epistolary novel tells its story through a series of documents, such as letters, diary entries, or emails, rather than through traditional third-person narration.',
  [('What format does an epistolary novel use to tell its story?', ['A series of documents such as letters or diary entries', 'A single uninterrupted narration with no documents at all', 'A concept unrelated to reading', 'A collection of unrelated recipes'], 0),
   ('Does an epistolary novel typically use traditional third-person narration?', ['No', 'Yes, epistolary novels always use traditional third-person narration', 'A concept unrelated to epistolary novels', 'Epistolary novels never include any narration of any kind'], 0),
   ('Name one type of document that might appear in an epistolary novel.', ['Letters', 'A concept unrelated to epistolary novels', 'A grocery list with no story content', 'A math worksheet'], 0),
   ('Why might an epistolary novel feel more personal or intimate to readers?', ['Readers experience events directly through a character’s own written words and perspective', 'Epistolary novels never feel personal or intimate to readers', 'This concept has no connection to literature', 'Letters and diary entries never reveal anything about a character’s feelings'], 0),
   ('Why might using multiple letter-writers in an epistolary novel add complexity to the story?', ['It can present multiple perspectives on the same events, revealing different viewpoints and biases', 'Multiple letter-writers never add any complexity to a story', 'This concept has no connection to reading comprehension', 'An epistolary novel can only ever include a single letter-writer'], 0)]),
M('Probability Trees and Multi-Stage Events',
  'Grade 8 Math strand: a probability tree diagram maps out all possible outcomes of a multi-stage event, with branches showing each possible result and the probabilities multiplied along each path.',
  [('What does a probability tree diagram map out?', ['All possible outcomes of a multi-stage event', 'Only a single outcome with no branches', 'A concept unrelated to probability', 'The average of a set of numbers'], 0),
   ('In a probability tree, are probabilities multiplied along each path to find a combined outcome?', ['Yes', 'No, probabilities are always added along each path instead', 'A concept unrelated to probability trees', 'Probabilities have no connection to how a tree diagram works'], 0),
   ('What does each branch in a probability tree represent?', ['A possible outcome at that stage', 'A concept unrelated to probability trees', 'A fixed, unchanging number', 'The total sample size only'], 0),
   ('Why might a probability tree be useful for solving a problem involving two coin flips in a row?', ['It visually organizes every possible combination of outcomes across both flips', 'A probability tree never helps organize outcomes of multiple events', 'This concept has no connection to probability', 'Coin flips can never be represented using a tree diagram'], 0),
   ('Why is multiplying probabilities along a branch path a valid way to find the probability of a sequence of events?', ['It reflects the combined likelihood of independent events happening one after another', 'Multiplying probabilities never gives any meaningful result', 'This concept has no relevance to probability', 'Sequences of events never have any combined probability at all'], 0)]),
Sc('Science: Cybersecurity: The Science of Data Encryption',
   'Grade 8 Science strand: encryption is a process that uses mathematical algorithms to convert readable data into a coded format, helping protect information as it is transmitted or stored electronically.',
   [('What does encryption use to convert readable data into a coded format?', ['Mathematical algorithms', 'A concept unrelated to encryption', 'Random guessing with no formula', 'Physical locks and keys only'], 0),
    ('Does encryption help protect information as it is transmitted or stored?', ['Yes', 'No, encryption has no effect on protecting information', 'A concept unrelated to encryption', 'Encryption only ever makes information easier to access'], 0),
    ('What is the term for encrypted data before it is decoded back into a readable format?', ['Ciphertext', 'A concept unrelated to encryption', 'Plaintext', 'Metadata'], 0),
    ('Why might a website use encryption when a user enters personal information, like a password?', ['It helps prevent unauthorized parties from reading the information if it is intercepted', 'Encryption never has any effect on protecting personal information', 'This concept has no connection to cybersecurity', 'Websites never need to protect any information entered by users'], 0),
    ('Why is a decryption key necessary to reverse the encryption process?', ['Without the correct key, encrypted data cannot be converted back into its original, readable form', 'A decryption key never has any effect on reversing encryption', 'This concept has no relevance to science', 'Encrypted data can always be read without any special key'], 0)]),
H('The Group of Seven and Canadian National Identity',
  'Grade 8 History strand: the Group of Seven was a collective of Canadian landscape painters formed in the 1920s whose distinct artistic style helped shape a sense of Canadian national identity through depictions of the country’s wilderness.',
  [('What type of artists made up the Group of Seven?', ['Landscape painters', 'Portrait photographers', 'A concept unrelated to Canadian history', 'Classical musicians'], 0),
   ('Was the Group of Seven formed in the 1920s?', ['Yes', 'No, the Group of Seven was formed in the 1700s', 'A concept unrelated to the Group of Seven', 'The Group of Seven has never actually existed'], 0),
   ('Did the Group of Seven often depict Canada’s wilderness in their paintings?', ['Yes', 'No, they only painted scenes from other countries', 'A concept unrelated to the Group of Seven', 'Their paintings never depicted any natural landscapes'], 0),
   ('Why might the Group of Seven’s paintings have helped shape a distinct sense of Canadian identity?', ['Their artwork celebrated Canada’s unique landscapes in a style separate from European artistic traditions', 'Their paintings had no connection to Canadian identity at all', 'This concept has no connection to Canadian history', 'The Group of Seven copied European painting styles exactly'], 0),
   ('Why is art, like that of the Group of Seven, considered an important part of studying a country’s history?', ['Art can reflect and shape how a nation sees itself and its culture during a particular era', 'Art has no connection to how a country understands its own history', 'This concept has no relevance to History', 'Studying art never reveals anything about a country’s culture'], 0)]),
]),

day(96, [
L('Media Literacy: Evaluating Sponsored Content and Native Advertising',
  'Grade 8 Language strand: sponsored content, or native advertising, is paid promotional material designed to look like regular articles or posts, making it important for readers to identify when content is actually an advertisement.',
  [('What is sponsored content designed to resemble?', ['Regular articles or posts', 'A dictionary entry', 'A concept unrelated to media literacy', 'A blank page with no content'], 0),
   ('Is sponsored content a form of paid advertising?', ['Yes', 'No, sponsored content is never connected to advertising', 'A concept unrelated to sponsored content', 'Sponsored content is always completely unpaid'], 0),
   ('Why is it important for readers to identify sponsored content?', ['It may present a biased or promotional viewpoint disguised as neutral information', 'Sponsored content never has any bias or promotional intent', 'This concept has no connection to media literacy', 'Readers never need to consider who paid for a piece of content'], 0),
   ('Why might companies choose native advertising instead of a traditional, clearly labeled ad?', ['It can feel more trustworthy or engaging to readers who might not realize it is an advertisement', 'Native advertising is never used by any company', 'This concept has no connection to media literacy', 'Traditional ads and native advertising are always identical in every way'], 0),
   ('Why should readers look for disclosure labels, like sponsored, before trusting online content?', ['These labels help readers judge whether they are viewing an unbiased source', 'Disclosure labels never provide any useful information to readers', 'This concept has no relevance to media literacy', 'All online content is always completely free of any bias'], 0)]),
M('Introduction to Piecewise Functions',
  'Grade 8 Math strand: a piecewise function is defined by different expressions or rules depending on which interval the input value falls into, allowing a single function to model changing behaviour.',
  [('What defines a piecewise function?', ['Different expressions or rules depending on the interval of the input', 'A single rule that applies to every possible input', 'A concept unrelated to functions', 'A function with no defined output at all'], 0),
   ('Can a piecewise function use more than one rule depending on the input value?', ['Yes', 'No, a piecewise function can only ever use one single rule', 'A concept unrelated to piecewise functions', 'Piecewise functions never actually have any defined rules'], 0),
   ('Why might a piecewise function be useful for modeling a phone plan with different rates for different amounts of data usage?', ['It can represent different pricing rules that apply depending on the specific value of usage', 'Piecewise functions never help model real-world pricing situations', 'This concept has no connection to math', 'Phone plans always charge the exact same rate no matter how much data is used'], 0),
   ('If a piecewise function uses one rule for x less than 0 and another for x greater than or equal to 0, which rule applies when x equals 5?', ['The rule for x greater than or equal to 0', 'The rule for x less than 0', 'A concept unrelated to piecewise functions', 'Neither rule applies when x equals 5'], 0),
   ('Why might real-world situations, like tax brackets, be modeled using piecewise functions?', ['The rate or rule applied changes depending on which range a value falls into', 'Tax brackets are never modeled using any type of mathematical function', 'This concept has no relevance to math', 'Every tax bracket always applies the exact same fixed rate'], 0)]),
Sc('Science: The Human Digestive System and Nutrient Absorption',
   'Grade 8 Science strand: the digestive system breaks down food into smaller molecules through mechanical and chemical processes, allowing nutrients to be absorbed into the bloodstream, primarily in the small intestine.',
   [('What does the digestive system break food down into?', ['Smaller molecules', 'Only water and gas', 'A concept unrelated to biology', 'Larger, more complex molecules'], 0),
    ('Does nutrient absorption primarily occur in the small intestine?', ['Yes', 'No, nutrient absorption never occurs anywhere in the digestive system', 'A concept unrelated to digestion', 'Absorption only ever occurs in the mouth'], 0),
    ('Name one process, mechanical or chemical, involved in digestion.', ['Chemical digestion using enzymes', 'A concept unrelated to digestion', 'Photosynthesis', 'Evaporation'], 0),
    ('Why does food need to be broken down into smaller molecules before it can be absorbed into the bloodstream?', ['Only sufficiently small molecules can pass through the intestinal lining into the blood', 'The size of food molecules never has any effect on absorption', 'This concept has no connection to biology', 'Large, unbroken food particles are always absorbed directly into the blood'], 0),
    ('Why are enzymes important for the chemical digestion of food?', ['Enzymes speed up the breakdown of large food molecules into smaller, absorbable ones', 'Enzymes never play any role in the digestive process', 'This concept has no relevance to science', 'Chemical digestion happens with no help from enzymes at all'], 0)]),
H('The Progressive Party and Farmer Political Movements of the 1920s',
  'Grade 8 History strand: the Progressive Party emerged in the 1920s as farmers across Canada organized politically to address concerns such as high freight rates and tariffs that they felt unfairly favoured Eastern industry.',
  [('In what decade did the Progressive Party emerge in Canada?', ['The 1920s', 'The 1800s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
   ('Did farmers form the Progressive Party to address concerns like tariffs and freight rates?', ['Yes', 'No, the Progressive Party had no connection to farmers at all', 'A concept unrelated to the Progressive Party', 'The Progressive Party was formed entirely by factory owners'], 0),
   ('Did the Progressive Party believe existing policies unfairly favoured Eastern industry?', ['Yes', 'No, the Progressive Party believed policies were completely fair to everyone', 'A concept unrelated to the Progressive Party', 'The Progressive Party had no opinion on federal economic policy'], 0),
   ('Why might farmers in Western Canada have felt that federal policies unfairly benefited industries in the East?', ['Tariffs raised the cost of goods farmers needed, while freight rates made shipping their crops more expensive', 'Federal policies never had any effect on farmers in Western Canada', 'This concept has no connection to Canadian history', 'Tariffs and freight rates had no connection to the cost of farming'], 0),
   ('Why is the rise of the Progressive Party significant for understanding Canadian political history in the 1920s?', ['It reflected growing regional and economic tensions that shaped new political movements outside the traditional parties', 'The Progressive Party had no lasting significance in Canadian political history', 'This concept has no relevance to History', 'Political movements in Canada were never shaped by regional economic tensions'], 0)]),
]),

day(97, [
L('Writing: Worldbuilding in Speculative Fiction',
  'Grade 8 Language strand: worldbuilding is the process of creating a fictional setting with consistent rules, geography, history, or technology, giving speculative fiction stories a believable foundation.',
  [('What is worldbuilding?', ['Creating a fictional setting with consistent rules and details', 'Writing a story with absolutely no setting at all', 'A concept unrelated to writing', 'Copying an existing real-world city exactly'], 0),
   ('Does worldbuilding often include details like geography, history, or technology?', ['Yes', 'No, worldbuilding never includes any details about a setting', 'A concept unrelated to worldbuilding', 'Worldbuilding only ever focuses on character names'], 0),
   ('Why is consistency important in worldbuilding?', ['Inconsistent rules can confuse readers and break their trust in the story', 'Consistency never matters when building a fictional world', 'This concept has no connection to writing', 'Fictional worlds are always more interesting when their rules keep changing randomly'], 0),
   ('Why might a speculative fiction writer create detailed rules for how magic or technology works in their world?', ['It helps make the fictional world feel believable and logical, even though it does not exist in reality', 'Detailed rules never make a fictional world feel more believable', 'This concept has no connection to writing', 'Magic and technology never need any explanation in fiction'], 0),
   ('Why might readers become more immersed in a story with strong worldbuilding?', ['A well-developed setting can make a fictional world feel real and easier to imagine', 'Strong worldbuilding never has any effect on how immersed a reader feels', 'This concept has no relevance to writing', 'Readers are always equally immersed no matter how a setting is described'], 0)]),
M('Coordinate Proofs in Geometry',
  'Grade 8 Math strand: a coordinate proof uses algebra and points on a coordinate plane, along with formulas like distance and slope, to prove geometric properties, such as whether a shape is a parallelogram.',
  [('What tools does a coordinate proof use to prove geometric properties?', ['Algebra and points on a coordinate plane', 'Only a protractor and no calculations', 'A concept unrelated to geometry', 'Guesswork with no formulas involved'], 0),
   ('Can the distance formula be used in a coordinate proof to compare side lengths?', ['Yes', 'No, the distance formula has no connection to coordinate proofs', 'A concept unrelated to coordinate proofs', 'Side lengths can never be calculated using coordinates'], 0),
   ('Which formula could help prove that two sides of a shape are parallel in a coordinate proof?', ['The slope formula', 'The area formula', 'A concept unrelated to coordinate proofs', 'The volume formula'], 0),
   ('Why might a coordinate proof be useful for showing that a quadrilateral is a rectangle?', ['It can confirm properties like equal diagonals or right angles using calculated values', 'Coordinate proofs never help confirm any properties of a shape', 'This concept has no connection to geometry', 'Rectangles can never be proven using algebra or coordinates'], 0),
   ('Why is combining algebra with geometry useful for proving properties that might be hard to see visually?', ['Calculations provide precise, provable evidence rather than relying only on appearance', 'Combining algebra and geometry never provides any useful evidence', 'This concept has no relevance to math', 'Visual appearance is always sufficient proof of a geometric property'], 0)]),
Sc('Science: Symbiosis: Mutualism, Commensalism, and Parasitism',
   'Grade 8 Science strand: symbiosis describes close, long-term relationships between two different species, which can be classified as mutualism, commensalism, or parasitism depending on how each species is affected.',
   [('What does symbiosis describe?', ['Close, long-term relationships between two different species', 'A single species living completely alone', 'A concept unrelated to biology', 'The process of a species becoming extinct'], 0),
    ('In mutualism, do both species benefit from the relationship?', ['Yes', 'No, in mutualism only one species ever benefits', 'A concept unrelated to symbiosis', 'Mutualism always harms both species involved'], 0),
    ('In parasitism, is one species harmed while the other benefits?', ['Yes', 'No, in parasitism both species always benefit equally', 'A concept unrelated to symbiosis', 'Parasitism never involves any harm to either species'], 0),
    ('Why might a clownfish and sea anemone relationship be classified as mutualism?', ['The clownfish gains protection while the anemone benefits from the clownfish’s presence, such as cleaning or defense', 'This relationship provides no benefit to either the clownfish or the anemone', 'This concept has no connection to symbiosis', 'The clownfish and anemone have no relationship with each other at all'], 0),
    ('Why is understanding symbiotic relationships important for studying ecosystems?', ['These relationships can affect the survival and behaviour of species throughout a food web', 'Symbiotic relationships never have any effect on an ecosystem', 'This concept has no relevance to science', 'Species in an ecosystem never interact with each other in any way'], 0)]),
H('The Formation of the United Church of Canada',
  'Grade 8 History strand: the United Church of Canada was formed in 1925 through the merger of the Methodist, Congregationalist, and most Presbyterian churches, becoming one of the largest Protestant denominations in the country.',
  [('In what year was the United Church of Canada formed?', ['1925', '1867', '1945', '1970'], 0),
   ('Was the United Church of Canada formed through a merger of multiple existing churches?', ['Yes', 'No, it was formed as a completely new religion with no prior connections', 'A concept unrelated to the United Church of Canada', 'It was formed by splitting one large church into smaller pieces'], 0),
   ('Name one church that merged to form the United Church of Canada.', ['Methodist', 'A concept unrelated to the United Church of Canada', 'Buddhist', 'Islamic'], 0),
   ('Why might church leaders in the 1920s have chosen to merge into a single, unified church?', ['Combining resources and congregations could strengthen their ability to serve communities across the country', 'Merging churches never provides any practical benefit', 'This concept has no connection to Canadian history', 'Church leaders in the 1920s had no interest in working together'], 0),
   ('Why is the formation of the United Church of Canada considered a significant event in Canadian religious and social history?', ['It created one of the largest religious institutions in Canada, reflecting a major shift in the country’s religious landscape', 'This event had no lasting significance in Canadian history', 'This concept has no relevance to History', 'Religious institutions in Canada have never changed or merged throughout history'], 0)]),
]),

day(98, [
L('Grammar: Subordinate Clauses and Complex Sentences',
  'Grade 8 Language strand: a subordinate clause has a subject and verb but cannot stand alone as a complete sentence, and combining it with an independent clause creates a complex sentence.',
  [('Can a subordinate clause stand alone as a complete sentence?', ['No', 'Yes, a subordinate clause is always a complete sentence on its own', 'A concept unrelated to grammar', 'Subordinate clauses never contain a subject or verb'], 0),
   ('Does a subordinate clause have both a subject and a verb?', ['Yes', 'No, a subordinate clause never contains a subject or verb', 'A concept unrelated to subordinate clauses', 'A subordinate clause only ever contains a single noun'], 0),
   ('What type of sentence is formed by combining a subordinate clause with an independent clause?', ['A complex sentence', 'A concept unrelated to grammar', 'A sentence fragment with no meaning', 'A list with no connected ideas'], 0),
   ('Which sentence contains a subordinate clause?', ['Although it was raining, we went outside.', 'It was raining outside today.', 'We went outside today.', 'Raining, outside, we, today.'], 0),
   ('Why might using subordinate clauses help a writer show relationships between ideas, like cause and effect?', ['Subordinate clauses can signal how one idea depends on, contrasts with, or leads to another', 'Subordinate clauses never show any relationship between ideas', 'This concept has no connection to grammar', 'Cause and effect can never be expressed using clauses of any kind'], 0)]),
M('Simplifying and Multiplying Rational Expressions',
  'Grade 8 Math strand: a rational expression is a fraction containing polynomials, and simplifying or multiplying these expressions involves factoring and cancelling common factors, similar to working with numerical fractions.',
  [('What is a rational expression?', ['A fraction containing polynomials', 'A whole number with no fraction involved', 'A concept unrelated to algebra', 'A geometric shape with straight sides'], 0),
   ('Does simplifying a rational expression often involve factoring?', ['Yes', 'No, factoring is never used when simplifying a rational expression', 'A concept unrelated to rational expressions', 'Simplifying a rational expression never changes its form in any way'], 0),
   ('When multiplying two rational expressions, what can you do with common factors?', ['Cancel them out', 'Always leave them completely unchanged', 'A concept unrelated to rational expressions', 'Multiply them by zero'], 0),
   ('Why is factoring an important first step before simplifying a rational expression?', ['It reveals common factors in the numerator and denominator that can be cancelled', 'Factoring never reveals any useful information about a rational expression', 'This concept has no connection to algebra', 'Rational expressions can never actually be simplified in any way'], 0),
   ('Why must you be careful about values that make a rational expression’s denominator equal to zero?', ['Division by zero is undefined, so those values must be excluded from the domain', 'A denominator of zero never causes any problem in a rational expression', 'This concept has no connection to rational expressions', 'Every possible value can always be safely substituted into a rational expression'], 0)]),
Sc('Science: Weather Fronts and Air Masses',
   'Grade 8 Science strand: an air mass is a large body of air with a fairly uniform temperature and humidity, and a front forms where two different air masses meet, often causing changes in weather.',
   [('What is an air mass?', ['A large body of air with fairly uniform temperature and humidity', 'A single small cloud with no size at all', 'A concept unrelated to earth science', 'A type of ocean current'], 0),
    ('Does a front form where two different air masses meet?', ['Yes', 'No, fronts have no connection to air masses at all', 'A concept unrelated to weather fronts', 'Fronts only ever form over open ocean water'], 0),
    ('Name one type of front, such as a cold front or warm front.', ['Cold front', 'A concept unrelated to weather fronts', 'Solid front', 'Electric front'], 0),
    ('Why might a cold front moving into a region cause sudden, intense weather changes?', ['A dense, fast-moving cold air mass can quickly push under and displace a warmer air mass, causing rapid changes', 'Cold fronts never cause any noticeable change in the weather', 'This concept has no connection to earth science', 'Air masses never actually move or interact with each other'], 0),
    ('Why do meteorologists track the movement of air masses and fronts to help forecast weather?', ['Understanding how these systems move can help predict upcoming changes in temperature and precipitation', 'Tracking air masses never provides any useful weather information', 'This concept has no relevance to science', 'Weather forecasting has no connection to air masses or fronts'], 0)]),
H('The Bluenose and Maritime Canadian Identity',
  'Grade 8 History strand: the Bluenose was a Canadian racing schooner built in Nova Scotia in 1921 that became a symbol of Maritime pride and skill, later depicted on the Canadian dime.',
  [('In what year was the Bluenose built?', ['1921', '1867', '1945', '1970'], 0),
   ('Was the Bluenose built in Nova Scotia?', ['Yes', 'No, the Bluenose was built in British Columbia', 'A concept unrelated to the Bluenose', 'The Bluenose was built in a country outside Canada'], 0),
   ('Is the Bluenose depicted on a Canadian coin?', ['Yes', 'No, the Bluenose has never appeared on any Canadian currency', 'A concept unrelated to the Bluenose', 'Only paper currency has ever featured the Bluenose'], 0),
   ('Why might the Bluenose have become a symbol of pride for Maritime Canadians?', ['Its racing success showcased the shipbuilding and sailing skill associated with the Maritime provinces', 'The Bluenose had no connection to Maritime pride or identity', 'This concept has no connection to Canadian history', 'The Bluenose was never actually a successful racing ship'], 0),
   ('Why is it meaningful that an image of the Bluenose still appears on Canadian currency today?', ['It reflects how a piece of regional history can become a lasting part of national identity and symbolism', 'The Bluenose’s image has no connection to Canadian identity today', 'This concept has no relevance to History', 'Canadian currency has never featured any historical ships or symbols'], 0)]),
]),

day(99, [
L('Reading: Analyzing Motif and Recurring Imagery',
  'Grade 8 Language strand: a motif is a recurring image, symbol, or idea that appears throughout a text, reinforcing its central themes each time it reappears.',
  [('What is a motif?', ['A recurring image, symbol, or idea in a text', 'A single event that happens only once in a story', 'A concept unrelated to reading', 'The title of a book with no deeper meaning'], 0),
   ('Does a motif appear only once in a text?', ['No', 'Yes, a motif can only ever appear a single time', 'A concept unrelated to motifs', 'Motifs never actually appear anywhere within a text'], 0),
   ('Why might a motif reinforce a text’s central themes?', ['Its repeated appearance draws attention to a meaningful pattern', 'A motif never has any connection to a text’s themes', 'This concept has no connection to reading comprehension', 'Repeated images or ideas never carry any deeper meaning'], 0),
   ('Why might an author repeat a specific image, like light or darkness, throughout a story?', ['To reinforce meaning or connect it to a broader theme each time it appears', 'Repeating an image never adds any meaning to a story', 'This concept has no connection to literature', 'Authors never intentionally repeat images or symbols in their writing'], 0),
   ('Why is recognizing motifs useful when analyzing a longer novel?', ['It can reveal patterns that connect separate parts of the story into a unified theme', 'Recognizing motifs never helps with understanding a longer novel', 'This concept has no relevance to reading comprehension', 'Motifs never connect to any other part of a story'], 0)]),
M('Introduction to the Unit Circle',
  'Grade 8 Math strand: the unit circle is a circle with a radius of one centred at the origin, used to define sine and cosine values for different angles based on the coordinates of points on the circle.',
  [('What is the radius of the unit circle?', ['1', '10', '0', '100'], 0),
   ('Is the unit circle centred at the origin?', ['Yes', 'No, the unit circle is never centred at the origin', 'A concept unrelated to the unit circle', 'The unit circle has no fixed centre point at all'], 0),
   ('What do the coordinates of a point on the unit circle represent?', ['The cosine and sine values of the angle', 'The radius of a completely different circle', 'A concept unrelated to the unit circle', 'The area enclosed by the circle'], 0),
   ('Why is the unit circle a useful tool for understanding sine and cosine values beyond right triangles?', ['It allows angles greater than 90 degrees to still have defined sine and cosine values', 'The unit circle never helps define sine or cosine for any angle', 'This concept has no connection to math', 'Sine and cosine only ever apply to angles inside a right triangle'], 0),
   ('Why does the unit circle have a radius of exactly one?', ['A radius of one simplifies calculations, since the coordinates directly equal the cosine and sine values', 'The radius of the unit circle has no effect on any calculations', 'This concept has no relevance to math', 'A radius of one was chosen completely at random with no mathematical reason'], 0)]),
Sc('Science: The Science of Sleep and Circadian Rhythms',
   'Grade 8 Science strand: a circadian rhythm is an internal, roughly 24-hour biological clock that regulates sleep and wake cycles, influenced by external cues such as light and darkness.',
   [('What is a circadian rhythm?', ['An internal, roughly 24-hour biological clock', 'A type of external weather pattern', 'A concept unrelated to biology', 'A device used to measure temperature'], 0),
    ('Does a circadian rhythm regulate sleep and wake cycles?', ['Yes', 'No, circadian rhythms have no connection to sleep at all', 'A concept unrelated to circadian rhythms', 'Circadian rhythms only ever regulate digestion'], 0),
    ('Name one external cue that can influence circadian rhythms.', ['Light', 'A concept unrelated to circadian rhythms', 'A favourite colour', 'A type of food with no biological effect'], 0),
    ('Why might exposure to bright screens before bed disrupt a person’s circadian rhythm?', ['Light exposure can signal to the brain that it is still daytime, delaying the release of sleep-related hormones', 'Bright screens never have any effect on a person’s circadian rhythm', 'This concept has no connection to biology', 'Sleep-related hormones are never affected by any external light source'], 0),
    ('Why is maintaining a consistent circadian rhythm considered important for overall health?', ['Disruptions to this internal clock have been linked to problems with sleep quality, mood, and other body functions', 'A person’s circadian rhythm has no connection to their overall health', 'This concept has no relevance to science', 'Circadian rhythms never actually affect any part of the human body'], 0)]),
H('The King-Byng Affair of 1926',
  'Grade 8 History strand: the King-Byng Affair of 1926 was a constitutional crisis in which Governor General Lord Byng refused Prime Minister Mackenzie King’s request to dissolve Parliament, raising questions about the limits of the Governor General’s power.',
  [('In what year did the King-Byng Affair take place?', ['1926', '1867', '1945', '1970'], 0),
   ('Did Governor General Lord Byng refuse a request from Prime Minister Mackenzie King?', ['Yes', 'No, Lord Byng agreed immediately to every request King made', 'A concept unrelated to the King-Byng Affair', 'Lord Byng had no interactions with Mackenzie King at all'], 0),
   ('Was the request King made to dissolve Parliament?', ['Yes', 'No, King never made any request involving Parliament', 'A concept unrelated to the King-Byng Affair', 'King requested that Byng resign from his position instead'], 0),
   ('Why might the King-Byng Affair have raised questions about the limits of the Governor General’s power?', ['It was unclear whether the Governor General should have the authority to override the elected prime minister’s request', 'The King-Byng Affair never raised any questions about government power', 'This concept has no connection to Canadian history', 'The Governor General’s powers were never a topic of discussion in Canada'], 0),
   ('Why is the King-Byng Affair considered an important event in the development of Canadian constitutional convention?', ['It helped clarify expectations about the relationship between the Governor General and an elected government going forward', 'The King-Byng Affair had no lasting effect on Canadian government or convention', 'This concept has no relevance to History', 'The roles of the Governor General and prime minister were never affected by this event'], 0)]),
]),

day(100, [
L('Review: Language Arts and Grammar (Days 91-99)',
  'Grade 8 Language strand review: students revisit frame narratives, elegy and tribute writing, appositives, neologisms, epistolary novels, sponsored content, worldbuilding, subordinate clauses, and motif.',
  [('What is a frame narrative?', ['A story that contains another story within it', 'A story with only one single event and no characters', 'A concept unrelated to reading', 'A poem written in a fixed rhyme scheme'], 0),
   ('What does an elegy typically do?', ['Mourns or honours someone who has died', 'Describes the steps of a science experiment', 'A concept unrelated to writing', 'Advertises a product for sale'], 0),
   ('What is a neologism?', ['A newly coined word or expression', 'A word that has existed unchanged for centuries', 'A concept unrelated to vocabulary', 'A grammatical rule with no connection to words'], 0),
   ('What format does an epistolary novel use to tell its story?', ['A series of documents such as letters or diary entries', 'A single uninterrupted narration with no documents at all', 'A concept unrelated to reading', 'A collection of unrelated recipes'], 0),
   ('What is a motif?', ['A recurring image, symbol, or idea in a text', 'A single event that happens only once in a story', 'A concept unrelated to reading', 'The title of a book with no deeper meaning'], 0)]),
M('Review: Advanced Algebra, Functions, and Geometry (Days 91-99)',
  'Grade 8 Math strand review: students revisit logarithms, polynomial long division, function notation, the Fibonacci sequence, probability trees, piecewise functions, coordinate proofs, rational expressions, and the unit circle.',
  [('What is a logarithm the inverse operation of?', ['Exponentiation', 'Addition', 'A concept unrelated to math', 'Division only'], 0),
   ('What does function notation like f(x) represent?', ['The output of a function for a given input', 'A random number with no connection to the function', 'A concept unrelated to algebra', 'The name of a variable with no other meaning'], 0),
   ('In the Fibonacci sequence, how is each new number formed?', ['By adding the two numbers before it', 'By multiplying the previous number by 2', 'A concept unrelated to the Fibonacci sequence', 'By subtracting the previous two numbers'], 0),
   ('What defines a piecewise function?', ['Different expressions or rules depending on the interval of the input', 'A single rule that applies to every possible input', 'A concept unrelated to functions', 'A function with no defined output at all'], 0),
   ('What is the radius of the unit circle?', ['1', '10', '0', '100'], 0)]),
Sc('Review: Earth Science, Human Biology, and Technology (Days 91-99)',
   'Grade 8 Science strand review: students revisit volcanoes, radioactivity, biomechanics, aerodynamics, data encryption, the digestive system, symbiosis, weather fronts, and circadian rhythms.',
   [('What is a volcano?', ['An opening in Earth’s crust where molten rock, gas, and ash can escape', 'A large flat area with no geological activity', 'A concept unrelated to earth science', 'A type of cloud formation'], 0),
    ('What occurs when unstable atomic nuclei release energy and particles?', ['Radioactivity', 'Photosynthesis', 'A concept unrelated to physics', 'Evaporation'], 0),
    ('What does biomechanics study?', ['How muscles, bones, and joints work together to produce movement', 'How rocks form deep underground', 'A concept unrelated to science', 'How plants absorb sunlight'], 0),
    ('What does symbiosis describe?', ['Close, long-term relationships between two different species', 'A single species living completely alone', 'A concept unrelated to biology', 'The process of a species becoming extinct'], 0),
    ('What is a circadian rhythm?', ['An internal, roughly 24-hour biological clock', 'A type of external weather pattern', 'A concept unrelated to biology', 'A device used to measure temperature'], 0)]),
H('Review: Canadian Autonomy and Identity in the 1920s (Days 91-99)',
  'Grade 8 History strand review: students revisit the Halibut Treaty, the Chanak Affair, the Balfour Declaration, Clifford Sifton, the Group of Seven, the Progressive Party, the United Church of Canada, the Bluenose, and the King-Byng Affair.',
  [('In what year was the Halibut Treaty signed?', ['1923', '1867', '1945', '1867'], 0),
   ('In what year did the Chanak Affair take place?', ['1922', '1867', '1945', '1970'], 0),
   ('In what year was the Balfour Declaration issued?', ['1926', '1867', '1945', '1970'], 0),
   ('What type of artists made up the Group of Seven?', ['Landscape painters', 'Portrait photographers', 'A concept unrelated to Canadian history', 'Classical musicians'], 0),
   ('In what year did the King-Byng Affair take place?', ['1926', '1867', '1945', '1970'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_91_100)
    append_to(8, g8_91_100)
