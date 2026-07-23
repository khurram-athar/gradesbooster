#!/usr/bin/env python3
"""Grade 4, Days 101-110 -- extends Grade 4 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade4.json): types of nouns, drawing conclusions, relative pronouns,
irony, writing a research report, number prefixes, direct and indirect
speech, identifying text structure, writing a diary entry from a historical
perspective; even and odd numbers, negative numbers, solving equations with
an unknown, area of rectangles using a formula, rotational symmetry,
collecting data through surveys, ways to pay for goods and services, skip
counting by 25s/50s/100s, classifying prisms and pyramids; tension and
compression in structures, layers of the Earth, opaque/translucent/
transparent materials, fixed and movable pulleys, testing rock and mineral
properties, ocean and coastal ecosystems, pitch and volume, natural and
artificial light sources, types of soil; the Indus Valley civilization,
West African kingdoms (Ghana, Mali, Songhai), United Empire Loyalists, the
War of 1812, the Underground Railroad, Canada's justice system, the Metis
Nation and the Red River Resistance, the history of the Canadian flag, and
Canada's contributions to space exploration.

Subject keys for Grade 4 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 4 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L4 = 'https://tvolearn.com/pages/grade-4-language'
M4 = 'https://tvolearn.com/pages/grade-4-mathematics'
S4 = 'https://tvolearn.com/pages/grade-4-science-and-technology'
SS4 = 'https://tvolearn.com/pages/grade-4-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 4 Language',
    'TVO Learn: Grade 4 Mathematics',
    'TVO Learn: Grade 4 Science and Technology',
    'TVO Learn: Grade 4 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L4, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M4, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S4, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS4, q)


def _rebalance_answer_positions(days, seed=20260722):
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


g4_101_110 = [
day(101, [
L('Grammar: Types of Nouns — Common, Proper, Collective, and Abstract',
  'Grade 4 Language strand: nouns can be common (a general name like city), proper (a specific name like Toronto, always capitalized), collective (a name for a group like team or flock), or abstract (a name for an idea or feeling like happiness).',
  [('What do we call a noun that names a specific person, place, or thing and starts with a capital letter?', ['A proper noun', 'A common noun', 'A collective noun', 'A concept unrelated to grammar'], 0),
   ('What do we call a noun that names a group of people or things, such as team or flock?', ['A collective noun', 'A proper noun', 'An abstract noun', 'A concept unrelated to grammar'], 0),
   ('What do we call a noun that names an idea or feeling, such as happiness or courage?', ['An abstract noun', 'A common noun', 'A proper noun', 'A concept unrelated to grammar'], 0),
   ('Why is dog considered a common noun while Rex is a proper noun?', ['Rex names one specific dog, while dog names any dog in general', 'Common nouns and proper nouns always mean exactly the same thing', 'This concept has no connection to grammar', 'Proper nouns are never capitalized'], 0),
   ('Which sentence correctly uses a collective noun?', ['The herd of cows walked across the field.', 'The herds of cow walked across field cows.', 'A concept unrelated to grammar', 'Herd cow the field walked across.'], 0)]),
M('Number Sense: Even and Odd Numbers and Their Properties',
  'Grade 4 Math strand: even numbers can be split into two equal groups and end in 0, 2, 4, 6, or 8, while odd numbers cannot be split evenly and end in 1, 3, 5, 7, or 9.',
  [('Which digit endings always make a number even?', ['0, 2, 4, 6, or 8', '1, 3, 5, 7, or 9', 'A concept unrelated to number sense', 'Only 0'], 0),
   ('Is the number 47 even or odd?', ['Odd', 'Even', 'A concept unrelated to number sense', 'Neither even nor odd'], 0),
   ('When you add two even numbers, such as 4 plus 6, is the sum always even?', ['Yes', 'No, the sum is always odd', 'A concept unrelated to number sense', 'The sum is never a whole number'], 0),
   ('Why is 8 considered an even number?', ['It can be split into two equal groups with none left over', 'It can never be divided evenly', 'This concept has no connection to number sense', '8 has no relationship to grouping at all'], 0),
   ('Which of these numbers is odd?', ['53', '54', '60', '72'], 0)]),
Sc('Science: Structures: Forces Acting on Structures — Tension and Compression',
   'Grade 4 Science strand: structures experience tension, a pulling or stretching force, and compression, a pushing or squeezing force, and engineers design structures to withstand both.',
   [('What do we call a pulling or stretching force on a structure?', ['Tension', 'Compression', 'A concept unrelated to structures', 'Friction'], 0),
    ('What do we call a pushing or squeezing force on a structure?', ['Compression', 'Tension', 'A concept unrelated to structures', 'Gravity'], 0),
    ('Is a rope holding up a swing under tension as it stretches?', ['Yes', 'No, ropes are never under tension', 'A concept unrelated to structures', 'Ropes only experience compression'], 0),
    ('Why must engineers design bridges to withstand both tension and compression?', ['Different parts of a bridge experience different forces as weight moves across it', 'Bridges never experience any forces at all', 'This concept has no connection to structures', 'Tension and compression never occur in real structures'], 0),
    ('Which example shows compression?', ['A stack of books pressing down on a table', 'A rope being stretched by a swing', 'A concept unrelated to structures', 'A kite string blowing loosely in the wind'], 0)]),
SS('Social Studies: The Indus Valley Civilization',
   'Grade 4 Social Studies strand: the Indus Valley civilization developed along the Indus River in present-day Pakistan and India, known for well-planned cities such as Mohenjo-daro that had organized streets and drainage systems.',
   [('Along which river did the Indus Valley civilization develop?', ['The Indus River', 'The Nile River', 'A concept unrelated to ancient civilizations', 'The Amazon River'], 0),
    ('Name a well-planned city built by the Indus Valley civilization.', ['Mohenjo-daro', 'A concept unrelated to the Indus Valley', 'Rome', 'Athens'], 0),
    ('Was the Indus Valley civilization known for organized city planning, including drainage systems?', ['Yes', 'No, its cities had no planning at all', 'A concept unrelated to the Indus Valley', 'Its cities had no streets or buildings'], 0),
    ('Why do historians consider the Indus Valley’s drainage systems impressive?', ['They show advanced engineering skill for such an early civilization', 'Drainage systems have no connection to ancient engineering', 'This concept has no relevance to social studies', 'The Indus Valley civilization never built anything at all'], 0),
    ('In which present-day countries was the Indus Valley civilization located?', ['Pakistan and India', 'Mexico and Peru', 'A concept unrelated to the Indus Valley', 'Canada and the United States'], 0)]),
]),

day(102, [
L('Reading: Drawing Conclusions',
  'Grade 4 Language strand: drawing conclusions means using clues from the text along with what you already know to figure out something the author does not state directly.',
  [('What do we call using text clues and prior knowledge to figure out something an author does not state directly?', ['Drawing a conclusion', 'A concept unrelated to reading', 'A summary', 'A prediction about the weather'], 0),
   ('If a character grabs an umbrella and puts on rain boots before leaving, what conclusion can you draw?', ['It is probably raining or about to rain', 'It is a sunny, dry day', 'A concept unrelated to the story', 'Nothing at all can be concluded'], 0),
   ('Do readers usually need clues from the text to draw an accurate conclusion?', ['Yes', 'No, conclusions never need any evidence', 'A concept unrelated to reading', 'Conclusions are always stated directly by the author'], 0),
   ('Why might drawing conclusions make reading more enjoyable?', ['It lets readers think more deeply and make connections beyond the words on the page', 'Drawing conclusions never adds anything to reading', 'This concept has no connection to reading', 'Conclusions always ruin the ending of a story'], 0),
   ('If a character’s hands are shaking and their face is pale before a test, what conclusion can you draw?', ['They are probably nervous or scared', 'They are probably very relaxed', 'A concept unrelated to the story', 'They feel nothing at all'], 0)]),
M('Number Sense: Negative Numbers in Everyday Contexts',
  'Grade 4 Math strand: negative numbers are numbers less than zero, often used to describe situations such as temperatures below freezing or an elevation below sea level.',
  [('What do we call a number less than zero?', ['A negative number', 'A positive number', 'A concept unrelated to number sense', 'A fraction'], 0),
   ('Which temperature is colder: -5 degrees or 2 degrees?', ['-5 degrees', '2 degrees', 'They are equally cold', 'Cannot be compared'], 0),
   ('On a number line, negative numbers are found in which direction from zero?', ['To the left', 'To the right', 'A concept unrelated to number sense', 'Straight up'], 0),
   ('Why is it useful to represent temperatures below freezing with negative numbers?', ['It gives an accurate way to show values that are less than zero', 'Negative numbers never represent real values', 'This concept has no connection to number sense', 'Temperatures can never actually go below zero'], 0),
   ('Which of these numbers is the coldest?', ['-10', '-2', '0', '5'], 0)]),
Sc('Science: Earth and Space: Layers of the Earth',
   'Grade 4 Science strand: Earth is made of layers, including the crust we live on, the mantle beneath it, and the core at the very centre, which has an outer and an inner part.',
   [('What is the name of Earth’s outermost layer, where we live?', ['The crust', 'The mantle', 'A concept unrelated to Earth’s layers', 'The core'], 0),
    ('Which layer lies directly beneath the crust?', ['The mantle', 'The crust', 'A concept unrelated to Earth’s layers', 'The atmosphere'], 0),
    ('What is the name of the layer at the very centre of the Earth?', ['The core', 'The crust', 'A concept unrelated to Earth’s layers', 'The mantle'], 0),
    ('Why is the crust often compared to the thin skin of an apple?', ['It is a very thin layer compared to the much thicker layers beneath it', 'The crust is actually the thickest layer of the Earth', 'This concept has no connection to Earth’s layers', 'The crust and the core are exactly the same thickness'], 0),
    ('Does Earth’s core have both an outer and an inner part?', ['Yes', 'No, the core has only one part', 'A concept unrelated to Earth’s layers', 'The core has no connection to Earth’s structure'], 0)]),
SS('Social Studies: Ancient Kingdoms of West Africa — Ghana, Mali, and Songhai',
   'Grade 4 Social Studies strand: the West African kingdoms of Ghana, Mali, and Songhai grew wealthy and powerful through trade in gold and salt across the Sahara Desert.',
   [('Name one ancient kingdom of West Africa.', ['Mali', 'A concept unrelated to West Africa', 'Rome', 'Athens'], 0),
    ('What resources helped these West African kingdoms grow wealthy?', ['Gold and salt', 'Oil and coal', 'A concept unrelated to trade', 'Rice and tea'], 0),
    ('Across which desert did much of this trade take place?', ['The Sahara Desert', 'The Gobi Desert', 'A concept unrelated to West Africa', 'The Arctic tundra'], 0),
    ('Why might control of trade routes have helped these kingdoms grow powerful?', ['It let them profit from and manage the flow of valuable goods like gold and salt', 'Trade routes never affected how powerful a kingdom became', 'This concept has no connection to West African history', 'These kingdoms had no connection to trade at all'], 0),
    ('Were Ghana, Mali, and Songhai all located in the same general region of Africa?', ['Yes', 'No, they were located on different continents', 'A concept unrelated to West Africa', 'They were located only in modern-day Canada'], 0)]),
]),

day(103, [
L('Grammar: Relative Pronouns — Who, Which, and That',
  'Grade 4 Language strand: relative pronouns such as who, which, and that connect a describing clause to a noun, with who used for people and which or that often used for things.',
  [('Which relative pronoun is typically used to describe people?', ['Who', 'Which', 'It', 'A concept unrelated to grammar'], 0),
   ('Which sentence correctly uses a relative pronoun?', ['The book that I borrowed was excellent.', 'The book who I borrowed was excellent.', 'Borrowed I book that excellent was.', 'A concept unrelated to grammar'], 0),
   ('Which relative pronoun would best complete: The scientist ___ discovered the cure was famous.', ['who', 'which', 'A concept unrelated to grammar', 'it'], 0),
   ('Why do writers use relative pronouns like who and which?', ['They connect extra descriptive information to a noun in the same sentence', 'Relative pronouns never add any information to a sentence', 'This concept has no connection to grammar', 'Relative pronouns always begin a brand new sentence'], 0),
   ('Which relative pronoun usually describes a thing rather than a person?', ['Which', 'Who', 'A concept unrelated to grammar', 'Whom is only used for animals'], 0)]),
M('Algebra: Solving Equations with an Unknown Value',
  'Grade 4 Math strand: students learn to find the value of an unknown, often shown as a letter or symbol, in a simple equation, such as solving n plus 5 equals 12 for n.',
  [('What is the value of n in n plus 5 equals 12?', ['7', '17', '5', '12'], 0),
   ('What is the value of x in x minus 3 equals 9?', ['12', '6', '3', '9'], 0),
   ('What is the value of y in y times 4 equals 20?', ['5', '16', '24', '80'], 0),
   ('Why is it helpful to check your answer by substituting it back into the equation?', ['It confirms whether the value makes the equation true', 'Checking an answer never actually proves anything', 'This concept has no connection to algebra', 'Substituting a value always makes an equation false'], 0),
   ('What is the value of a in 6 plus a equals 14?', ['8', '20', '6', '14'], 0)]),
Sc('Science: Light: Opaque, Translucent, and Transparent Materials',
   'Grade 4 Science strand: materials can be transparent, letting light pass through clearly like glass; translucent, letting some light through like wax paper; or opaque, blocking light completely like wood.',
   [('What do we call a material that lets light pass through clearly, like glass?', ['Transparent', 'Opaque', 'Translucent', 'A concept unrelated to light'], 0),
    ('What do we call a material that blocks light completely?', ['Opaque', 'Transparent', 'Translucent', 'A concept unrelated to light'], 0),
    ('What do we call a material that lets some light through but blurs what is on the other side, like wax paper?', ['Translucent', 'Opaque', 'Transparent', 'A concept unrelated to light'], 0),
    ('Why are windows usually made from a transparent material?', ['It allows light and a clear view to pass through easily', 'Transparent materials always block all light', 'This concept has no connection to light', 'Windows are never made from transparent materials'], 0),
    ('Which of these is a good example of an opaque material?', ['Wood', 'Clear glass', 'Wax paper', 'A concept unrelated to light'], 0)]),
SS('Social Studies: United Empire Loyalists',
   'Grade 4 Social Studies strand: United Empire Loyalists were colonists who remained loyal to Britain during the American Revolution and moved north to settle in what is now Canada.',
   [('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain and moved to Canada', 'Colonists who fought against Britain', 'A concept unrelated to Canadian history', 'Explorers from Spain'], 0),
    ('During which conflict did many Loyalists move north to Canada?', ['The American Revolution', 'The War of the Roses', 'A concept unrelated to Loyalists', 'World War One'], 0),
    ('Did the arrival of Loyalists help shape early settlement in what is now Canada?', ['Yes', 'No, Loyalists had no effect on early Canada', 'A concept unrelated to Loyalists', 'Loyalists never actually settled anywhere'], 0),
    ('Why is the resettlement of Loyalists in areas like present-day Ontario significant?', ['It contributed to population growth and the development of new communities', 'Loyalists never settled in what is now Ontario', 'This concept has no connection to Canadian history', 'Population growth has no connection to settlement'], 0),
    ('Where did most Loyalists live before moving north?', ['The thirteen American colonies', 'Western Europe', 'A concept unrelated to Loyalists', 'South America'], 0)]),
]),

day(104, [
L('Reading: Understanding Irony',
  'Grade 4 Language strand: irony occurs when what actually happens is different from what a reader or character expects, often creating humour or surprise.',
  [('What do we call it when what happens is different from what is expected?', ['Irony', 'A concept unrelated to reading', 'A metaphor', 'A summary'], 0),
   ('If a fire station burns down, what makes this situation ironic?', ['A place meant to fight fires was destroyed by one', 'The fire station is very old', 'A concept unrelated to the story', 'Fire stations always catch fire eventually'], 0),
   ('Can irony create humour or surprise for a reader?', ['Yes', 'No, irony never creates any reaction', 'A concept unrelated to irony', 'Irony always makes a story boring'], 0),
   ('Why might an author use irony in a story?', ['It can add surprise or humour by showing an unexpected outcome', 'Irony never affects how a reader feels', 'This concept has no connection to storytelling', 'Authors should never include unexpected outcomes'], 0),
   ('Which situation is an example of irony?', ['A traffic officer gets a parking ticket.', 'A student studies hard and passes a test.', 'A concept unrelated to the story', 'A baker bakes bread every day.'], 0)]),
M('Measurement: Area of Rectangles Using a Formula',
  'Grade 4 Math strand: students learn to find the area of a rectangle by multiplying its length by its width, with the result measured in square units.',
  [('What formula finds the area of a rectangle?', ['Length times width', 'Length plus width', 'A concept unrelated to measurement', 'Length minus width'], 0),
   ('What is the area of a rectangle with a length of 6 cm and a width of 4 cm?', ['24 square cm', '20 square cm', '10 square cm', '28 square cm'], 0),
   ('What is the area of a rectangle with a length of 9 cm and a width of 3 cm?', ['27 square cm', '24 square cm', '12 square cm', '30 square cm'], 0),
   ('Why is area measured in square units, such as square centimetres?', ['It describes how much flat, two-dimensional surface a shape covers', 'Square units never actually describe any surface', 'This concept has no connection to measurement', 'Area is always measured using only whole numbers with no units'], 0),
   ('What is the area of a square with sides of 5 cm?', ['25 square cm', '20 square cm', '10 square cm', '15 square cm'], 0)]),
Sc('Science: Simple Machines: Fixed and Movable Pulleys',
   'Grade 4 Science strand: a fixed pulley is attached in one place and changes the direction of a force, while a movable pulley moves with the load and helps reduce the force needed to lift it.',
   [('What type of pulley stays attached in one place and changes the direction of a force?', ['A fixed pulley', 'A movable pulley', 'A concept unrelated to simple machines', 'A lever'], 0),
    ('What type of pulley moves with the load and helps reduce the force needed to lift it?', ['A movable pulley', 'A fixed pulley', 'A concept unrelated to simple machines', 'A wedge'], 0),
    ('Does a flag pole typically use a fixed pulley to raise the flag?', ['Yes', 'No, flag poles never use pulleys', 'A concept unrelated to pulleys', 'Flag poles only use movable pulleys'], 0),
    ('Why might a movable pulley make it easier to lift a heavy load?', ['It can reduce the amount of force needed compared to lifting the load directly', 'A movable pulley always makes an object heavier', 'This concept has no connection to simple machines', 'Movable pulleys never actually help lift anything'], 0),
    ('Which of these is an example of a fixed pulley in use?', ['The rope and pulley on a flag pole', 'A wheelbarrow being pushed', 'A concept unrelated to pulleys', 'A wedge splitting wood'], 0)]),
SS('Social Studies: The War of 1812',
   'Grade 4 Social Studies strand: the War of 1812 was fought between the United States and Britain, with many battles taking place in Canada, helping shape a shared sense of identity among settlers, Indigenous allies, and British soldiers.',
   [('Which two sides fought in the War of 1812, with Canada as a major battleground?', ['The United States and Britain', 'France and Spain', 'A concept unrelated to the War of 1812', 'Canada and Mexico'], 0),
    ('Where did many battles of the War of 1812 take place?', ['In what is now Canada', 'In South America', 'A concept unrelated to the War of 1812', 'In Australia'], 0),
    ('Did Indigenous allies play an important role in the War of 1812?', ['Yes', 'No, Indigenous peoples had no role in the war', 'A concept unrelated to the War of 1812', 'The war involved no allies of any kind'], 0),
    ('Why is the War of 1812 seen as important to the growth of a shared identity among people in Canada?', ['Settlers, Indigenous allies, and British soldiers worked together to defend the same territory', 'The war had no connection to identity in Canada', 'This concept has no relevance to social studies', 'No one living in Canada was affected by the war'], 0),
    ('In approximately what time period did the War of 1812 take place?', ['The early 1800s', 'The early 1900s', 'A concept unrelated to the War of 1812', 'The late 1700s'], 0)]),
]),

day(105, [
L('Writing: Writing a Research Report',
  'Grade 4 Language strand: writing a research report involves choosing a topic, gathering facts from reliable sources, organizing information under headings, and citing where the information came from.',
  [('What is usually the first step in writing a research report?', ['Choosing a topic', 'Writing the conclusion first', 'A concept unrelated to writing', 'Skipping straight to citing sources'], 0),
   ('Why should a research report use reliable sources of information?', ['To make sure the information shared is accurate and trustworthy', 'Reliable sources never actually matter in research', 'This concept has no connection to writing', 'Any source, reliable or not, works equally well'], 0),
   ('What can help organize the information in a research report?', ['Headings', 'Random order with no structure', 'A concept unrelated to writing', 'Rhyming lines'], 0),
   ('Why is it important to cite where information came from in a research report?', ['It gives credit to the original source and shows the information is trustworthy', 'Citing sources never matters in a research report', 'This concept has no connection to writing', 'Citations always confuse a reader'], 0),
   ('Which of these would most likely appear in a research report about volcanoes?', ['Facts about how volcanoes form and erupt', 'A made-up story about a dragon', 'A grocery list', 'A poem about the ocean'], 0)]),
M('Geometry: Rotational Symmetry',
  'Grade 4 Math strand: a shape has rotational symmetry if it looks the same after being turned less than a full circle around its centre point, such as a square looking the same after a quarter turn.',
  [('What do we call a shape that looks the same after being turned less than a full circle around its centre?', ['A shape with rotational symmetry', 'A shape with no symmetry at all', 'A concept unrelated to geometry', 'An irregular polygon'], 0),
   ('Does a square have rotational symmetry?', ['Yes', 'No, squares never have any symmetry', 'A concept unrelated to geometry', 'Only circles can have symmetry'], 0),
   ('How many times does a square look the same during one full turn?', ['4 times', '2 times', '1 time', '8 times'], 0),
   ('Why might a pinwheel design be a good example of rotational symmetry?', ['Its repeating pattern looks the same after each partial turn around the centre', 'A pinwheel has no connection to rotational symmetry', 'This concept has no relevance to geometry', 'Pinwheels never actually spin or turn'], 0),
   ('Which shape most likely has rotational symmetry?', ['A regular hexagon', 'A scalene triangle with three different side lengths', 'A concept unrelated to geometry', 'A random, irregular blob shape'], 0)]),
Sc('Science: Rocks and Minerals: Testing Properties — Hardness, Lustre, and Streak',
   'Grade 4 Science strand: scientists identify minerals by testing physical properties such as hardness (resistance to scratching), lustre (how the surface reflects light), and streak (the colour left behind when scratched on a tile).',
   [('What test measures a mineral’s resistance to scratching?', ['A hardness test', 'A streak test', 'A concept unrelated to minerals', 'A taste test'], 0),
    ('What test describes how a mineral’s surface reflects light?', ['A lustre test', 'A hardness test', 'A concept unrelated to minerals', 'A smell test'], 0),
    ('What test looks at the colour a mineral leaves behind when scratched on a tile?', ['A streak test', 'A hardness test', 'A concept unrelated to minerals', 'A taste test'], 0),
    ('Why can a harder mineral scratch a softer one during a hardness test?', ['Its particles resist being worn away more than the softer mineral’s do', 'Hardness never affects whether one mineral can scratch another', 'This concept has no connection to minerals', 'Softer minerals always scratch harder ones instead'], 0),
    ('Which word describes a mineral with a shiny, metal-like lustre?', ['Metallic', 'Dull', 'A concept unrelated to minerals', 'Transparent'], 0)]),
SS('Social Studies: The Underground Railroad and Canada',
   'Grade 4 Social Studies strand: the Underground Railroad was a secret network of routes and safe houses that helped enslaved people from the United States escape to freedom, with many settling in Canada.',
   [('What was the Underground Railroad?', ['A secret network of routes and safe houses', 'An actual underground train system', 'A concept unrelated to Canadian history', 'A government building in Ottawa'], 0),
    ('Who used the Underground Railroad to seek freedom?', ['Enslaved people escaping to freedom', 'Tourists visiting Canada', 'A concept unrelated to the Underground Railroad', 'Soldiers travelling to battle'], 0),
    ('Did many freedom seekers who used the Underground Railroad settle in Canada?', ['Yes', 'No, no one who used it ever reached Canada', 'A concept unrelated to the Underground Railroad', 'They only settled in Mexico'], 0),
    ('Why was Canada seen as a safe destination for freedom seekers?', ['Slavery had been abolished there, offering safety and freedom', 'Canada had no connection to the Underground Railroad', 'This concept has no relevance to social studies', 'Canada was the only place slavery still existed'], 0),
    ('Was the Underground Railroad an actual railroad with tracks and trains?', ['No, it was a network of secret routes, not literal train tracks', 'Yes, it had real trains running underground', 'A concept unrelated to the Underground Railroad', 'It was a railroad built entirely in Canada'], 0)]),
]),

day(106, [
L('Vocabulary: Number Prefixes — Uni-, Bi-, Tri-, and Quad-',
  'Grade 4 Language strand: number prefixes such as uni-, bi-, tri-, and quad- attach to the beginning of words to show how many, as in unicycle, bicycle, triangle, and quadrilateral.',
  [('Which prefix means one, as in unicycle?', ['Uni-', 'Bi-', 'Tri-', 'Quad-'], 0),
   ('Which prefix means two, as in bicycle?', ['Bi-', 'Uni-', 'Tri-', 'Quad-'], 0),
   ('Which prefix means three, as in triangle?', ['Tri-', 'Uni-', 'Bi-', 'Quad-'], 0),
   ('Why does the word quadrilateral describe a shape with four sides?', ['The prefix quad- means four, matching the number of sides', 'The prefix quad- means one hundred', 'This concept has no connection to vocabulary', 'Quadrilateral has no connection to number prefixes'], 0),
   ('Which word uses a prefix meaning two?', ['Bicycle', 'Unicycle', 'Triangle', 'Quadrilateral'], 0)]),
M('Data Management: Collecting Data Through Surveys',
  'Grade 4 Math strand: students learn to design a simple survey question, collect responses from classmates, and organize the results into a table or graph.',
  [('What is a survey used to do?', ['Collect information or opinions from a group of people', 'Predict the weather', 'A concept unrelated to data management', 'Measure the length of an object'], 0),
   ('Why should a good survey question be clear and easy to understand?', ['It helps people answer accurately, which leads to more useful results', 'Clear questions never affect the quality of survey results', 'This concept has no connection to data management', 'Confusing questions always produce the most useful data'], 0),
   ('What should you do with survey responses after collecting them?', ['Organize them into a table or graph', 'Throw them away immediately', 'A concept unrelated to data management', 'Ignore them completely'], 0),
   ('Why is organizing survey data into a graph helpful?', ['It makes it easier to see patterns and compare results at a glance', 'Organizing data never makes results easier to understand', 'This concept has no connection to surveys', 'Graphs always hide the true results of a survey'], 0),
   ('Which of these is an example of a good survey question?', ['What is your favourite fruit?', 'A concept unrelated to surveys', 'A random string of unrelated numbers', 'A statement with no question at all'], 0)]),
Sc('Science: Ocean and Coastal Ecosystems',
   'Grade 4 Science strand: ocean and coastal ecosystems include tide pools, coral reefs, and open water habitats that support a wide variety of plants and animals adapted to salty water.',
   [('What do we call a shoreline habitat that fills and empties with the rise and fall of tides?', ['A tide pool', 'A desert', 'A concept unrelated to ecosystems', 'A tundra'], 0),
    ('What colourful underwater ecosystem is built by tiny ocean animals?', ['A coral reef', 'A prairie', 'A concept unrelated to ecosystems', 'A rainforest canopy'], 0),
    ('Are ocean organisms usually adapted to survive in salty water?', ['Yes', 'No, ocean organisms cannot survive in salt water', 'A concept unrelated to ecosystems', 'Only freshwater organisms live in oceans'], 0),
    ('Why might a tide pool be considered a challenging habitat for the organisms living there?', ['Conditions like water level and temperature change constantly as tides rise and fall', 'Tide pool conditions never change at all', 'This concept has no relevance to science', 'Tide pools are always exactly the same as the open ocean'], 0),
    ('Which of these is an example of an ocean or coastal ecosystem?', ['A coral reef', 'A mountain forest', 'A concept unrelated to ecosystems', 'A desert dune'], 0)]),
SS('Social Studies: Canada’s Justice System and Courts',
   'Grade 4 Social Studies strand: Canada’s justice system includes courts that interpret and apply laws, with judges making rulings and everyone having the right to a fair trial.',
   [('What is the main role of courts in Canada’s justice system?', ['To interpret and apply the law', 'To build roads and bridges', 'A concept unrelated to government', 'To collect garbage in a community'], 0),
    ('Who typically makes rulings in a courtroom?', ['A judge', 'A mayor', 'A concept unrelated to the justice system', 'A store manager'], 0),
    ('Does everyone in Canada have the right to a fair trial?', ['Yes', 'No, only some people have this right', 'A concept unrelated to the justice system', 'Fair trials are never guaranteed to anyone'], 0),
    ('Why are fair trials an important part of Canada’s justice system?', ['They help protect people’s basic rights and ensure justice is applied fairly', 'Fair trials have no connection to protecting anyone’s rights', 'This concept has no relevance to social studies', 'Trials in Canada are never actually fair'], 0),
    ('Which of these is part of Canada’s justice system?', ['A courtroom', 'A grocery store', 'A concept unrelated to government', 'A movie theatre'], 0)]),
]),

day(107, [
L('Grammar: Direct and Indirect Speech',
  'Grade 4 Language strand: direct speech repeats a person’s exact words, while indirect (reported) speech tells what someone said without quoting their exact words.',
  [('What do we call speech that repeats a person’s exact words?', ['Direct speech', 'Indirect speech', 'A concept unrelated to grammar', 'A run-on sentence'], 0),
   ('What do we call speech that reports what someone said without quoting their exact words?', ['Indirect speech', 'Direct speech', 'A concept unrelated to grammar', 'A sentence fragment'], 0),
   ('Which sentence is written in direct speech, repeating the speaker’s exact words?', ['Maria said, I am hungry.', 'Maria said she was hungry.', 'A concept unrelated to grammar', 'Hungry, said Maria, was I.'], 0),
   ('Why do quotation marks matter when writing direct speech?', ['They show exactly which words were spoken by the person', 'Quotation marks never affect how a sentence is understood', 'This concept has no connection to grammar', 'Quotation marks are only used for titles of books'], 0),
   ('Which sentence correctly rewrites I will go, said Tom, as indirect speech?', ['Tom said he would go.', 'Tom said, I will go.', 'A concept unrelated to grammar', 'Go will I said Tom.'], 0)]),
M('Financial Literacy: Ways to Pay for Goods and Services',
  'Grade 4 Math strand: people can pay for goods and services using cash, debit cards, or credit cards, and each method has its own advantages and things to keep track of.',
  [('Name one way people can pay for goods besides cash.', ['A debit card', 'A concept unrelated to money', 'Nothing else exists', 'Only barter is possible'], 0),
   ('What is cash?', ['Physical money, such as coins and bills', 'A type of bank account only', 'A concept unrelated to money', 'A digital password'], 0),
   ('Why should people keep track of their spending when using a debit or credit card?', ['To avoid spending more money than they have', 'Keeping track of spending never matters with cards', 'This concept has no connection to financial literacy', 'Cards always show your exact balance with no effort'], 0),
   ('Why might a business accept multiple ways to pay, such as cash and debit?', ['It makes shopping more convenient for different customers', 'Businesses never accept more than one payment method', 'This concept has no relevance to financial literacy', 'Accepting multiple payment methods is never useful'], 0),
   ('Which of these is an example of paying with cash?', ['Handing the cashier coins and bills', 'Tapping a card on a machine', 'A concept unrelated to money', 'Entering a password online'], 0)]),
Sc('Science: Sound: Pitch and Volume',
   'Grade 4 Science strand: pitch describes how high or low a sound is and depends on how fast an object vibrates, while volume describes how loud or soft a sound is and depends on the size of the vibration.',
   [('What do we call the description of how high or low a sound is?', ['Pitch', 'Volume', 'A concept unrelated to sound', 'Echo'], 0),
    ('What do we call the description of how loud or soft a sound is?', ['Volume', 'Pitch', 'A concept unrelated to sound', 'Frequency alone'], 0),
    ('Does a faster vibration usually produce a higher or lower pitch?', ['A higher pitch', 'A lower pitch', 'A concept unrelated to sound', 'Vibration speed never affects pitch'], 0),
    ('Why does plucking a guitar string harder mainly change its volume rather than its pitch?', ['A harder pluck creates a bigger vibration, which makes the sound louder', 'Plucking harder always changes the pitch instead of the volume', 'This concept has no connection to sound', 'Volume and pitch are always exactly the same thing'], 0),
    ('Which is more likely to have a higher pitch: a small bell or a big drum?', ['A small bell', 'A big drum', 'They always sound exactly the same', 'A concept unrelated to sound'], 0)]),
SS('Social Studies: The Metis Nation and the Red River Resistance',
   'Grade 4 Social Studies strand: the Metis are a distinct Indigenous people with mixed First Nations and European ancestry, and the Red River Resistance, led by Louis Riel, was a stand to protect Metis land and rights in present-day Manitoba.',
   [('Who are the Metis?', ['A distinct Indigenous people with mixed First Nations and European ancestry', 'A group of European settlers only', 'A concept unrelated to Canadian history', 'A group with no connection to Canada'], 0),
    ('Who led the Red River Resistance?', ['Louis Riel', 'John A. Macdonald', 'A concept unrelated to the Red River Resistance', 'Queen Victoria'], 0),
    ('What were the Metis trying to protect during the Red River Resistance?', ['Their land and rights', 'A foreign country’s border', 'A concept unrelated to the Red River Resistance', 'A sports championship'], 0),
    ('Why is the Red River Resistance considered an important event in Canadian history?', ['It involved Indigenous peoples standing up for their rights and way of life', 'It had no connection to Indigenous rights in Canada', 'This concept has no relevance to social studies', 'It was an event that took place outside of Canada'], 0),
    ('In which present-day province did the Red River Resistance mostly take place?', ['Manitoba', 'British Columbia', 'A concept unrelated to the Red River Resistance', 'Nova Scotia'], 0)]),
]),

day(108, [
L('Reading: Identifying Text Structure — Sequence, Cause-Effect, and Problem-Solution',
  'Grade 4 Language strand: nonfiction authors organize ideas using text structures such as sequence (order of events), cause-and-effect (why something happens), and problem-solution (a challenge and how it is solved).',
  [('What text structure organizes events in the order they happened?', ['Sequence', 'Cause-and-effect', 'A concept unrelated to reading', 'Problem-solution'], 0),
   ('What text structure explains why something happens and what results from it?', ['Cause-and-effect', 'Sequence', 'A concept unrelated to reading', 'Problem-solution'], 0),
   ('What text structure describes a challenge and how it was solved?', ['Problem-solution', 'Sequence', 'A concept unrelated to reading', 'Cause-and-effect'], 0),
   ('Why might recognizing text structure help a reader understand a nonfiction article?', ['It shows how the ideas in the article are organized and connected', 'Text structure never affects how clear an article is', 'This concept has no connection to reading', 'All nonfiction articles are organized in exactly the same way'], 0),
   ('Which text structure would a recipe most likely use?', ['Sequence', 'Cause-and-effect', 'A concept unrelated to reading', 'Problem-solution'], 0)]),
M('Number Sense: Skip Counting by 25s, 50s, and 100s',
  'Grade 4 Math strand: skip counting by 25s, 50s, and 100s helps students count large groups of objects or amounts of money quickly, recognizing patterns such as 25, 50, 75, 100.',
  [('Skip count by 25s: 25, 50, 75, ___', ['100', '85', '90', '125'], 0),
   ('Skip count by 50s: 50, 100, 150, ___', ['200', '175', '160', '225'], 0),
   ('Skip count by 100s: 300, 400, 500, ___', ['600', '550', '510', '650'], 0),
   ('Why is skip counting by 25s especially helpful when counting quarters?', ['Each quarter is worth 25 cents, so skip counting by 25 matches their value', 'Skip counting by 25 never relates to money in any way', 'This concept has no connection to number sense', 'Quarters are always worth exactly 100 cents each'], 0),
   ('Which sequence correctly skip counts by 50s?', ['100, 150, 200, 250', '100, 125, 150, 175', '100, 200, 400, 800', '100, 110, 120, 130'], 0)]),
Sc('Science: Light: Natural and Artificial Light Sources',
   'Grade 4 Science strand: natural light sources, such as the Sun and fire, produce light without human-made technology, while artificial light sources, such as light bulbs and flashlights, are created by people.',
   [('Name a natural source of light.', ['The Sun', 'A light bulb', 'A concept unrelated to light', 'A flashlight'], 0),
    ('Name an artificial source of light.', ['A light bulb', 'The Sun', 'A concept unrelated to light', 'A campfire made by lightning'], 0),
    ('Is the Sun a natural or artificial light source?', ['Natural', 'Artificial', 'A concept unrelated to light', 'Neither natural nor artificial'], 0),
    ('Why did humans create artificial light sources such as light bulbs?', ['To see and work in places or times without natural light', 'Artificial light sources have no real purpose', 'This concept has no connection to light', 'Humans never actually created any light sources'], 0),
    ('Which of these is an example of artificial light?', ['A flashlight', 'The Sun', 'A concept unrelated to light', 'A bolt of lightning'], 0)]),
SS('Social Studies: The History of the Canadian Flag',
   'Grade 4 Social Studies strand: Canada adopted its current red and white maple leaf flag in 1965, replacing earlier flags and becoming a distinct national symbol chosen after public debate.',
   [('In what year was Canada’s current maple leaf flag officially adopted?', ['1965', '1867', '1812', '2000'], 0),
    ('What symbol appears on the Canadian flag?', ['A maple leaf', 'An eagle', 'A concept unrelated to Canadian symbols', 'A lion'], 0),
    ('What two colours appear on the Canadian flag?', ['Red and white', 'Blue and gold', 'A concept unrelated to Canadian symbols', 'Green and yellow'], 0),
    ('Why might having a distinct national flag help strengthen a country’s identity?', ['It gives citizens a shared symbol to recognize and take pride in', 'A flag never has any connection to national identity', 'This concept has no relevance to social studies', 'Flags are never associated with any country'], 0),
    ('Did choosing Canada’s current flag involve public debate before it was adopted?', ['Yes', 'No, the flag was chosen with no discussion at all', 'A concept unrelated to Canadian history', 'The flag has never actually changed since Confederation'], 0)]),
]),

day(109, [
L('Writing: Writing a Diary Entry from a Historical Perspective',
  'Grade 4 Language strand: writing a diary entry from a historical perspective means imagining you are a person from the past and describing daily events, thoughts, and feelings in the first person, based on accurate historical details.',
  [('Whose point of view does a historical diary entry usually use?', ['First person, as if you are the historical person', 'Third person, describing someone else entirely', 'A concept unrelated to writing', 'No point of view at all'], 0),
   ('Why might a writer research real historical details before writing a diary entry from the past?', ['It helps make the entry accurate and believable', 'Historical accuracy never matters in this kind of writing', 'This concept has no connection to writing', 'Diary entries should always ignore real facts'], 0),
   ('Does a historical diary entry usually use the word I to describe thoughts and feelings?', ['Yes', 'No, diary entries never use the word I', 'A concept unrelated to writing', 'Diary entries only describe other people’s feelings'], 0),
   ('Why is it important to include accurate historical details in this kind of diary entry?', ['It helps readers understand what daily life was really like in that time period', 'Historical details never help a reader understand the past', 'This concept has no connection to writing', 'Made-up details are always more accurate than real ones'], 0),
   ('Which of these would most likely appear in a diary entry written from the perspective of a Loyalist settler?', ['A description of the long journey north and building a new home', 'A description of riding in a car to school', 'A concept unrelated to the topic', 'A summary of a video game'], 0)]),
M('Geometry: Classifying Prisms and Pyramids',
  'Grade 4 Math strand: prisms have two matching parallel bases connected by rectangular faces, while pyramids have one base and triangular faces that meet at a single point called the apex.',
  [('What shape do the side faces of a pyramid meet at?', ['A single point, called the apex', 'Two separate points', 'A concept unrelated to geometry', 'They never meet at all'], 0),
   ('How many matching parallel bases does a prism have?', ['Two', 'One', 'Three', 'Four'], 0),
   ('What shape are the side faces of most prisms?', ['Rectangles', 'Circles', 'A concept unrelated to geometry', 'Triangles only'], 0),
   ('How can you tell a triangular prism apart from a triangular pyramid?', ['A prism has two triangular bases connected by rectangles, while a pyramid has one base and triangular sides meeting at a point', 'Prisms and pyramids are always exactly the same shape', 'This concept has no connection to geometry', 'A pyramid always has two identical bases like a prism'], 0),
   ('Which of these is an example of a pyramid?', ['A shape with a square base and four triangular faces meeting at a point', 'A shape with two rectangular bases and four rectangular sides', 'A concept unrelated to geometry', 'A perfect sphere'], 0)]),
Sc('Science: Soil: Types of Soil — Sand, Silt, Clay, and Loam',
   'Grade 4 Science strand: soil types include sandy soil with large particles that drain quickly, clay soil with tiny particles that hold water, silt with medium-sized particles, and loam, a balanced mixture good for growing plants.',
   [('Which soil type has the largest particles and drains water quickly?', ['Sandy soil', 'Clay soil', 'A concept unrelated to soil', 'Loam'], 0),
    ('Which soil type holds water well because of its tiny particles?', ['Clay soil', 'Sandy soil', 'A concept unrelated to soil', 'Silt'], 0),
    ('Which soil type is a balanced mixture often considered best for growing plants?', ['Loam', 'Sandy soil', 'A concept unrelated to soil', 'Pure clay'], 0),
    ('Why might farmers often prefer loam soil for growing crops?', ['It balances good drainage with the ability to hold enough water and nutrients', 'Loam soil never actually helps plants grow', 'This concept has no connection to soil', 'Loam is the only soil type that exists'], 0),
    ('Which soil type has particles that are between the size of sand and clay particles?', ['Silt', 'Loam', 'A concept unrelated to soil', 'Sandy soil'], 0)]),
SS('Social Studies: Canada’s Contributions to Space Exploration',
   'Grade 4 Social Studies strand: Canada has contributed to space exploration through the Canadarm robotic arm and Canadian astronauts who have travelled to space, including on the International Space Station.',
   [('What is the name of the famous robotic arm Canada contributed to space missions?', ['Canadarm', 'Spacebot', 'A concept unrelated to space exploration', 'Starlink'], 0),
    ('Name a place Canadian astronauts have travelled to in space.', ['The International Space Station', 'The surface of Mars', 'A concept unrelated to space exploration', 'The Moon’s surface'], 0),
    ('Has Canada made significant contributions to space technology?', ['Yes', 'No, Canada has never contributed to space technology', 'A concept unrelated to space exploration', 'Canada has no space program at all'], 0),
    ('Why is the Canadarm considered an important Canadian contribution to space exploration?', ['It helped with tasks like satellite repair, showing Canada’s role in space engineering', 'The Canadarm has no connection to space missions', 'This concept has no relevance to social studies', 'The Canadarm was never actually used in space'], 0),
    ('What do we call a Canadian who travels to space as part of a mission?', ['An astronaut', 'A pilot only', 'A concept unrelated to space exploration', 'A tourist'], 0)]),
]),

day(110, [
L('Review: Vocabulary, Grammar, and Reading Skills (Days 101-109)',
  'Grade 4 Language strand review: students revisit types of nouns, drawing conclusions, relative pronouns, irony, writing a research report, number prefixes, direct and indirect speech, identifying text structure, and writing a diary entry from a historical perspective.',
  [('What do we call a noun that names a specific person, place, or thing and starts with a capital letter?', ['A proper noun', 'A common noun', 'A collective noun', 'A concept unrelated to grammar'], 0),
   ('What do we call using text clues and prior knowledge to figure out something an author does not state directly?', ['Drawing a conclusion', 'A concept unrelated to reading', 'A summary', 'A prediction about the weather'], 0),
   ('What do we call it when what happens is different from what is expected?', ['Irony', 'A concept unrelated to reading', 'A metaphor', 'A summary'], 0),
   ('What do we call speech that repeats a person’s exact words?', ['Direct speech', 'Indirect speech', 'A concept unrelated to grammar', 'A run-on sentence'], 0),
   ('What text structure organizes events in the order they happened?', ['Sequence', 'Cause-and-effect', 'A concept unrelated to reading', 'Problem-solution'], 0)]),
M('Review: Number Sense, Algebra, and Measurement (Days 101-109)',
  'Grade 4 Math strand review: students revisit even and odd numbers, negative numbers, solving equations with an unknown, area of rectangles using a formula, rotational symmetry, collecting data through surveys, ways to pay for goods and services, skip counting by 25s/50s/100s, and classifying prisms and pyramids.',
  [('Is the number 47 even or odd?', ['Odd', 'Even', 'A concept unrelated to number sense', 'Neither even nor odd'], 0),
   ('What is the value of n in n plus 5 equals 12?', ['7', '17', '5', '12'], 0),
   ('What formula finds the area of a rectangle?', ['Length times width', 'Length plus width', 'A concept unrelated to measurement', 'Length minus width'], 0),
   ('What do we call a shape that looks the same after being turned less than a full circle around its centre?', ['A shape with rotational symmetry', 'A shape with no symmetry at all', 'A concept unrelated to geometry', 'An irregular polygon'], 0),
   ('How many matching parallel bases does a prism have?', ['Two', 'One', 'Three', 'Four'], 0)]),
Sc('Review: Structures, Earth and Space, Light, and Soil (Days 101-109)',
   'Grade 4 Science strand review: students revisit tension and compression, layers of the Earth, opaque/translucent/transparent materials, fixed and movable pulleys, testing rock and mineral properties, ocean and coastal ecosystems, pitch and volume, natural and artificial light sources, and types of soil.',
   [('What do we call a pulling or stretching force on a structure?', ['Tension', 'Compression', 'A concept unrelated to structures', 'Friction'], 0),
    ('What is the name of Earth’s outermost layer, where we live?', ['The crust', 'The mantle', 'A concept unrelated to Earth’s layers', 'The core'], 0),
    ('What do we call a material that blocks light completely?', ['Opaque', 'Transparent', 'Translucent', 'A concept unrelated to light'], 0),
    ('What do we call the description of how high or low a sound is?', ['Pitch', 'Volume', 'A concept unrelated to sound', 'Echo'], 0),
    ('Which soil type is a balanced mixture often considered best for growing plants?', ['Loam', 'Sandy soil', 'A concept unrelated to soil', 'Pure clay'], 0)]),
SS('Review: Ancient Civilizations and Canadian History (Days 101-109)',
   'Grade 4 Social Studies strand review: students revisit the Indus Valley civilization, West African kingdoms, United Empire Loyalists, the War of 1812, the Underground Railroad, Canada’s justice system, the Metis Nation and the Red River Resistance, the history of the Canadian flag, and Canada’s contributions to space exploration.',
   [('Along which river did the Indus Valley civilization develop?', ['The Indus River', 'The Nile River', 'A concept unrelated to ancient civilizations', 'The Amazon River'], 0),
    ('What resources helped the West African kingdoms of Ghana, Mali, and Songhai grow wealthy?', ['Gold and salt', 'Oil and coal', 'A concept unrelated to trade', 'Rice and tea'], 0),
    ('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain and moved to Canada', 'Colonists who fought against Britain', 'A concept unrelated to Canadian history', 'Explorers from Spain'], 0),
    ('Who led the Red River Resistance?', ['Louis Riel', 'John A. Macdonald', 'A concept unrelated to the Red River Resistance', 'Queen Victoria'], 0),
    ('In what year was Canada’s current maple leaf flag officially adopted?', ['1965', '1867', '1812', '2000'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_101_110)
    append_to(4, g4_101_110)
