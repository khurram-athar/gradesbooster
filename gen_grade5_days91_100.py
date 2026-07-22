#!/usr/bin/env python3
"""Grade 5, Days 91-100 -- extends Grade 5 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade5.json):
similes, coordinating and subordinating conjunctions, plot structure,
elements of poetry, writing a myth or legend, synonyms and antonyms,
protagonist and antagonist, capitalization rules, note-taking and
paraphrasing; classifying triangles, area of triangles and
parallelograms, multiplying and dividing whole numbers by powers of ten,
tree diagrams and sample space, classifying quadrilaterals, surface area
of triangular prisms, integers in real-life contexts, budgeting for a
savings goal, volume of composite rectangular figures; the endocrine
system, plate tectonics, kinetic and potential energy, the human ear,
decomposers and nutrient cycling, why triangles are the strongest shape,
camouflage and animal defense mechanisms, coral reefs, microorganisms;
Canada's music and film industry, how provinces and territories joined
Confederation, the RCMP, federal and provincial division of powers, the
Bank of Canada, universal health care, criminal versus civil law, the
Group of Seven, and Canadian national holidays.

Subject keys for Grade 5 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 5 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science and Technology',
    'TVO Learn: Grade 5 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L5, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M5, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S5, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS5, q)


def _rebalance_answer_positions(days, seed=20260924):
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


g5_91_100 = [
day(91, [
L('Figurative Language: Similes',
  'Grade 5 Language strand: a simile is a figure of speech that compares two unlike things using the words like or as, such as brave as a lion or fast like the wind.',
  [('What do we call a comparison between two unlike things that uses the word like or as?', ['A simile', 'A concept unrelated to figurative language', 'A homophone', 'A prefix'], 0),
   ('Which sentence contains a simile?', ['Her smile was as bright as the sun.', 'Her smile lit up the room.', 'The sun rose over the hill.', 'She smiled at her friend.'], 0),
   ('Does a simile always use the word like or as to make its comparison?', ['Yes', 'No, a simile never compares anything', 'A concept unrelated to similes', 'Similes only ever use the word than'], 0),
   ('Why might a writer use a simile instead of stating a plain description?', ['It creates a vivid picture by connecting an idea to something familiar', 'Similes never add any meaning to writing', 'This concept has no connection to figurative language', 'Similes always make a description less clear'], 0),
   ('Which of these is an example of a simile?', ['The wind howled like a wolf.', 'The wind is a wolf.', 'The wind howled loudly.', 'The wolf howled at the wind.'], 0)]),
M('Geometry: Classifying Triangles by Angles and Sides',
  'Grade 5 Math strand: triangles can be classified by their sides, such as equilateral, isosceles, and scalene, and by their angles, such as acute, right, and obtuse.',
  [('What do we call a triangle with all three sides equal in length?', ['An equilateral triangle', 'A scalene triangle', 'An obtuse triangle', 'A right triangle'], 0),
   ('What do we call a triangle with exactly two equal sides?', ['An isosceles triangle', 'An equilateral triangle', 'A scalene triangle', 'A concept unrelated to triangles'], 0),
   ('What do we call a triangle with no equal sides at all?', ['A scalene triangle', 'An equilateral triangle', 'An isosceles triangle', 'A right triangle'], 0),
   ('What do we call a triangle that contains one 90-degree angle?', ['A right triangle', 'An acute triangle', 'An obtuse triangle', 'An equilateral triangle'], 0),
   ('Why might it be useful to classify triangles by both their sides and their angles?', ['It gives a more complete and precise description of a triangle’s shape', 'Classifying triangles never gives any useful information', 'This concept has no connection to geometry', 'A triangle can only ever be described one single way'], 0)]),
Sc('The Endocrine System and Hormones',
   'Grade 5 Science strand: the endocrine system is a network of glands, such as the thyroid and pituitary gland, that release hormones into the bloodstream to regulate processes like growth and metabolism.',
   [('What do we call the body system made up of glands that release hormones into the bloodstream?', ['The endocrine system', 'A concept unrelated to the body', 'The digestive system', 'The skeletal system'], 0),
    ('What are the chemical messengers released by glands in the endocrine system called?', ['Hormones', 'Enzymes', 'A concept unrelated to the endocrine system', 'Antibodies'], 0),
    ('Name one gland that is part of the endocrine system, such as the thyroid.', ['The thyroid gland', 'A concept unrelated to the endocrine system', 'The stomach', 'The lungs'], 0),
    ('Why is it important for hormones to travel through the bloodstream to reach different parts of the body?', ['It allows glands to send signals that regulate processes throughout the whole body', 'Hormones never travel anywhere in the body', 'This concept has no connection to the endocrine system', 'The bloodstream has no connection to hormones at all'], 0),
    ('Why might a problem with the endocrine system affect a person’s growth or energy levels?', ['Hormones help control processes like growth and metabolism, so imbalances can cause noticeable effects', 'The endocrine system has no effect on growth or energy at all', 'This concept has no relevance to science', 'Growth and metabolism are never controlled by hormones'], 0)]),
SS('Canada’s Music and Film Industry and National Culture',
   'Grade 5 Social Studies strand: Canada has a thriving music and film industry, with Canadian content rules helping ensure Canadian stories, music, and voices are shared with audiences at home and abroad.',
   [('What do we call rules that help ensure Canadian stories and music are shared with audiences, sometimes known as Canadian content rules?', ['Canadian content rules', 'A concept unrelated to Canadian culture', 'International trade tariffs', 'A concept with no real name'], 0),
    ('Does Canada have its own music and film industry?', ['Yes', 'No, Canada has never produced any music or films', 'A concept unrelated to Canadian culture', 'Only other countries make music and films'], 0),
    ('Can Canadian musicians and filmmakers find success both in Canada and internationally?', ['Yes', 'No, Canadian artists never find success anywhere', 'A concept unrelated to Canada', 'Success is only possible outside of Canada'], 0),
    ('Why might Canadian content rules be important for supporting Canadian culture?', ['They help ensure Canadian creators and stories get a chance to be seen and heard', 'These rules have no connection to supporting culture', 'This concept has no relevance to social studies', 'Canadian content rules always block Canadian stories from being shared'], 0),
    ('Why might a strong music and film industry help build a sense of national identity?', ['Shared stories, songs, and films can reflect and connect people’s experiences across the country', 'Music and film have no connection to national identity', 'This concept has no connection to Canadian culture', 'National identity is never influenced by art or culture'], 0)]),
]),

day(92, [
L('Grammar: Coordinating and Subordinating Conjunctions',
  'Grade 5 Language strand: a coordinating conjunction, such as and, but, or, joins two equal ideas, while a subordinating conjunction, such as because, although, or when, joins a dependent clause to an independent clause.',
  [('Which of these is a coordinating conjunction?', ['But', 'Because', 'Although', 'Since'], 0),
   ('Which of these is a subordinating conjunction?', ['Because', 'And', 'But', 'Or'], 0),
   ('Does a coordinating conjunction join two equal, independent ideas?', ['Yes', 'No, it always joins a dependent clause only', 'A concept unrelated to grammar', 'Coordinating conjunctions never join anything'], 0),
   ('In the sentence Although it was raining, we went outside, what type of conjunction is although?', ['A subordinating conjunction', 'A coordinating conjunction', 'A concept unrelated to grammar', 'A preposition'], 0),
   ('Why might a writer use a subordinating conjunction like because in a sentence?', ['It can show a reason or cause-and-effect relationship between two ideas', 'Subordinating conjunctions never connect any ideas', 'This concept has no connection to grammar', 'Subordinating conjunctions only ever join two equal independent ideas'], 0)]),
M('Measurement: Area of Triangles and Parallelograms',
  'Grade 5 Math strand: students learn that the area of a triangle equals one half of its base times its height, and the area of a parallelogram equals its base times its height.',
  [('What is the formula for the area of a parallelogram?', ['Base times height', 'Base plus height', 'Half of base times height', 'Base divided by height'], 0),
   ('What is the formula for the area of a triangle?', ['One half of base times height', 'Base times height', 'Base plus height', 'Base divided by height'], 0),
   ('If a triangle has a base of 8 cm and a height of 5 cm, what is its area?', ['20 square cm', '40 square cm', '13 square cm', '10 square cm'], 0),
   ('If a parallelogram has a base of 6 cm and a height of 4 cm, what is its area?', ['24 square cm', '10 square cm', '12 square cm', '20 square cm'], 0),
   ('Why does the area of a triangle formula include multiplying by one half?', ['A triangle is exactly half of a parallelogram with the same base and height', 'Multiplying by one half never has any connection to a triangle’s area', 'This concept has no connection to geometry', 'A triangle and a parallelogram always have the exact same area formula'], 0)]),
Sc('Plate Tectonics and Continental Drift',
   'Grade 5 Science strand: Earth’s crust is broken into large plates that move very slowly over time, a process that can cause earthquakes, form mountains, and create volcanoes at plate boundaries.',
   [('What do we call the large sections of Earth’s crust that move very slowly over time?', ['Tectonic plates', 'A concept unrelated to Earth science', 'Ocean currents', 'Weather systems'], 0),
    ('Can the movement of tectonic plates cause earthquakes?', ['Yes', 'No, tectonic plates have no connection to earthquakes', 'A concept unrelated to plate tectonics', 'Earthquakes only ever happen underwater'], 0),
    ('Can mountains form where tectonic plates push against each other?', ['Yes', 'No, mountains never form because of tectonic plates', 'A concept unrelated to plate tectonics', 'Mountains only form from volcanoes, never from plate movement'], 0),
    ('Why might volcanoes often be found near the edges of tectonic plates?', ['Plate boundaries can create openings where melted rock from inside Earth reaches the surface', 'Volcanoes have no connection to tectonic plates at all', 'This concept has no relevance to science', 'Volcanoes are found only in the exact centre of a tectonic plate'], 0),
    ('Why do scientists say plate movement happens very slowly, often just centimetres per year?', ['The plates are extremely large and heavy, so they shift gradually over a very long time', 'Tectonic plates actually move at extremely fast speeds', 'This concept has no connection to plate tectonics', 'Plate movement happens instantly with no gradual process'], 0)]),
SS('How Provinces and Territories Joined Confederation Over Time',
   'Grade 5 Social Studies strand: Canada began in 1867 with four provinces and grew over time as other provinces and territories, such as British Columbia in 1871 and Newfoundland in 1949, joined Confederation.',
   [('How many provinces originally joined together to form Canada in 1867?', ['Four', 'Ten', 'Two', 'Six'], 0),
    ('Which province was the last to join Confederation, in 1949?', ['Newfoundland', 'British Columbia', 'Manitoba', 'Prince Edward Island'], 0),
    ('Did Canada grow by adding new provinces and territories after 1867?', ['Yes', 'No, Canada has always had the exact same provinces since 1867', 'A concept unrelated to Confederation', 'No new provinces have ever joined Canada'], 0),
    ('Why might a province have chosen to join Confederation years after 1867 rather than right away?', ['Each province had its own reasons and negotiations before deciding to join Canada', 'Every province was forced to join in the exact same year', 'This concept has no connection to Canadian history', 'Joining Confederation was never an actual choice for any province'], 0),
    ('Why is it useful to know the order in which provinces and territories joined Confederation?', ['It helps explain how Canada grew and changed shape over time', 'The order provinces joined has no connection to Canadian history', 'This concept has no relevance to social studies', 'All provinces and territories joined in the exact same instant'], 0)]),
]),

day(93, [
L('Reading: Understanding Plot Structure',
  'Grade 5 Language strand: plot structure describes the shape of a story, including the exposition, rising action, climax, falling action, and resolution.',
  [('What is the term for the part of a story where the main conflict reaches its most intense point?', ['The climax', 'The exposition', 'The falling action', 'The resolution'], 0),
   ('What is the term for the part of a story that introduces the characters and setting?', ['The exposition', 'The climax', 'The rising action', 'The resolution'], 0),
   ('What is the term for the part of a story where the conflict is finally solved?', ['The resolution', 'The exposition', 'The climax', 'The rising action'], 0),
   ('Does the rising action happen before or after the climax of a story?', ['Before', 'After', 'A concept unrelated to plot structure', 'Rising action never happens in a story'], 0),
   ('Why might understanding plot structure help a reader predict what will happen next in a story?', ['Recognizing the stages of a plot can signal whether tension is building or being resolved', 'Plot structure never gives any clues about a story', 'This concept has no connection to reading comprehension', 'Every story follows a completely random, unpredictable structure'], 0)]),
M('Number Sense: Multiplying and Dividing Whole Numbers by Powers of Ten',
  'Grade 5 Math strand: multiplying a whole number by a power of ten, such as 10, 100, or 1000, shifts its digits to the left, while dividing shifts its digits to the right.',
  [('What is 45 multiplied by 10?', ['450', '45', '4500', '4.5'], 0),
   ('What is 45 multiplied by 100?', ['4500', '450', '45000', '4.5'], 0),
   ('What is 4500 divided by 100?', ['45', '450', '4.5', '45000'], 0),
   ('When you multiply a whole number by a power of ten, what happens to its digits?', ['They shift to the left', 'They shift to the right', 'A concept unrelated to place value', 'Nothing happens to the digits at all'], 0),
   ('Why is it useful to recognize the pattern of multiplying and dividing by powers of ten?', ['It allows you to solve these problems quickly using place value, without long multiplication', 'This pattern never applies to whole numbers', 'This concept has no connection to number sense', 'Powers of ten never affect how digits are arranged'], 0)]),
Sc('Energy: Kinetic and Potential Energy',
   'Grade 5 Science strand: kinetic energy is the energy of motion, such as a rolling ball, while potential energy is stored energy based on position, such as a ball held at the top of a hill.',
   [('What do we call the energy of motion, such as a rolling ball has?', ['Kinetic energy', 'Potential energy', 'A concept unrelated to energy', 'Chemical energy'], 0),
    ('What do we call stored energy based on an object’s position, such as a ball held at the top of a hill?', ['Potential energy', 'Kinetic energy', 'A concept unrelated to energy', 'Sound energy'], 0),
    ('When a ball rolls down a hill, does its potential energy change into kinetic energy?', ['Yes', 'No, potential energy never changes into kinetic energy', 'A concept unrelated to energy', 'The ball loses all of its energy instantly'], 0),
    ('Why does an object held high above the ground have more potential energy than one on the ground?', ['Its higher position gives it more stored energy that could be released if it falls', 'Height has no connection to potential energy', 'This concept has no relevance to science', 'Objects on the ground always have more potential energy'], 0),
    ('Why might a roller coaster at the top of a hill be a good example of potential energy changing into kinetic energy?', ['As the coaster drops, its stored potential energy converts into the energy of motion', 'Roller coasters never involve any changes in energy', 'This concept has no connection to kinetic and potential energy', 'A roller coaster has the same amount of energy at every point on the track'], 0)]),
SS('The Royal Canadian Mounted Police and Its History',
   'Grade 5 Social Studies strand: the Royal Canadian Mounted Police, or RCMP, began in 1873 as the North-West Mounted Police and has grown into Canada’s national police force, recognized worldwide by its red uniform.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Regional Canadian Municipal Patrol', 'A concept unrelated to Canadian history', 'Royal Canadian Marine Patrol'], 0),
    ('What was the RCMP originally called when it was founded in 1873?', ['The North-West Mounted Police', 'The Canadian Border Patrol', 'A concept unrelated to the RCMP', 'The Royal Guard'], 0),
    ('Is the RCMP recognized around the world by its red uniform?', ['Yes', 'No, the RCMP has never had a distinctive uniform', 'A concept unrelated to the RCMP', 'The RCMP wears the exact same uniform as every other police force'], 0),
    ('Why might the RCMP be considered an important symbol of Canada, in addition to being a police force?', ['Its uniform and history are widely recognized as part of Canadian identity', 'The RCMP has no connection to Canadian identity at all', 'This concept has no relevance to social studies', 'Police forces are never associated with a country’s identity'], 0),
    ('Why might a national police force like the RCMP have different responsibilities than a local police department?', ['A national force may handle matters that cross provincial or territorial boundaries', 'National and local police forces always have identical responsibilities', 'This concept has no connection to Canadian government', 'A national police force never has any responsibilities at all'], 0)]),
]),

day(94, [
L('Poetry: Elements of Poetry (Rhyme, Rhythm, and Stanza)',
  'Grade 5 Language strand: poems often use rhyme, the repetition of similar ending sounds, rhythm, a pattern of beats, and stanzas, groups of lines organized like paragraphs.',
  [('What do we call the repetition of similar ending sounds in a poem?', ['Rhyme', 'Rhythm', 'A stanza', 'A concept unrelated to poetry'], 0),
   ('What do we call a group of lines in a poem, organized like a paragraph?', ['A stanza', 'A rhyme', 'A concept unrelated to poetry', 'A syllable'], 0),
   ('What do we call the pattern of beats or stresses in a poem?', ['Rhythm', 'A stanza', 'A concept unrelated to poetry', 'A metaphor'], 0),
   ('In the lines The cat sat on the mat, which words rhyme?', ['Cat and mat', 'Cat and sat', 'The and on', 'Sat and the'], 0),
   ('Why might a poet use rhythm to help create a certain feeling in a poem?', ['A steady or changing pattern of beats can affect the mood or pace of the poem', 'Rhythm never affects how a poem feels to read', 'This concept has no connection to poetry', 'Every poem has the exact same rhythm'], 0)]),
M('Data Management: Tree Diagrams and Sample Space',
  'Grade 5 Math strand: a tree diagram lists all possible outcomes of an event, called the sample space, such as showing all combinations when flipping a coin and rolling a die.',
  [('What do we call the list of all possible outcomes of an event?', ['The sample space', 'The mean', 'A concept unrelated to probability', 'The median'], 0),
   ('What is a diagram called that branches out to show all possible outcomes of an event?', ['A tree diagram', 'A bar graph', 'A concept unrelated to probability', 'A pictograph'], 0),
   ('How many total outcomes are there when flipping a coin (2 outcomes) and rolling a six-sided die (6 outcomes)?', ['12', '8', '6', '2'], 0),
   ('If you flip a coin twice, how many total outcomes are in the sample space?', ['4', '2', '8', '6'], 0),
   ('Why might a tree diagram be helpful for solving a probability problem with two events?', ['It organizes every possible combination clearly, making outcomes easier to count', 'Tree diagrams never help with organizing outcomes', 'This concept has no connection to data management', 'A sample space can never actually be shown in a diagram'], 0)]),
Sc('The Human Ear and How We Hear',
   'Grade 5 Science strand: the ear collects sound waves in the outer ear, vibrates the eardrum in the middle ear, and converts those vibrations into nerve signals in the inner ear, which the brain interprets as sound.',
   [('What part of the ear vibrates when sound waves reach it?', ['The eardrum', 'The outer ear only', 'A concept unrelated to hearing', 'The nose'], 0),
    ('Where are sound waves first collected before travelling further into the ear?', ['The outer ear', 'The inner ear', 'A concept unrelated to the ear', 'The brain'], 0),
    ('What part of the ear converts vibrations into nerve signals that the brain can interpret?', ['The inner ear', 'The outer ear', 'A concept unrelated to hearing', 'The eyebrow'], 0),
    ('Why is it important for the eardrum to vibrate when sound waves reach it?', ['The vibrations are the first step in turning sound waves into signals the brain can understand', 'The eardrum has no connection to how we hear sound', 'This concept has no relevance to science', 'Sound can be heard without any vibration occurring at all'], 0),
    ('Why might loud noises over a long period of time damage a person’s hearing?', ['Strong vibrations can harm the delicate structures inside the ear that detect sound', 'Loud noises never have any effect on hearing', 'This concept has no connection to the human ear', 'The ear is completely unaffected by any sound, no matter how loud'], 0)]),
SS('Federal and Provincial Division of Powers in Canada',
   'Grade 5 Social Studies strand: Canada’s Constitution divides responsibilities between the federal government, which handles matters like national defence and currency, and provincial governments, which handle matters like education and health care.',
   [('Which level of government is typically responsible for national defence and currency?', ['The federal government', 'The provincial government', 'A concept unrelated to Canadian government', 'The municipal government'], 0),
    ('Which level of government is typically responsible for education and health care?', ['The provincial government', 'The federal government', 'A concept unrelated to Canadian government', 'No level of government handles these areas'], 0),
    ('Does Canada’s Constitution divide responsibilities between federal and provincial governments?', ['Yes', 'No, only one level of government exists in Canada', 'A concept unrelated to Canadian government', 'Responsibilities are never divided in Canada'], 0),
    ('Why might it make sense for education to be handled at the provincial level rather than the federal level?', ['Provinces can design education systems suited to their own populations and needs', 'Education has no connection to any level of government', 'This concept has no relevance to social studies', 'Every province in Canada must have an identical education system by law'], 0),
    ('Why is it useful for a country like Canada to divide responsibilities between different levels of government?', ['It allows different levels of government to focus on issues at the right scale, from national to local', 'Dividing responsibilities never has any benefit', 'This concept has no connection to Canadian government', 'A single level of government could handle every responsibility equally well'], 0)]),
]),

day(95, [
L('Writing: Writing a Myth or Legend',
  'Grade 5 Language strand: a myth is a traditional story that often explains natural events or features gods and heroes, while a legend is a traditional story often based loosely on real people or events.',
  [('What do we call a traditional story that often explains a natural event and features gods or heroes?', ['A myth', 'A concept unrelated to writing', 'A recipe', 'A grocery list'], 0),
   ('What do we call a traditional story often based loosely on real people or events?', ['A legend', 'A myth', 'A concept unrelated to writing', 'A weather report'], 0),
   ('Might a myth be used to explain something in nature, such as why the seasons change?', ['Yes', 'No, myths never explain anything about nature', 'A concept unrelated to myths', 'Myths only ever describe modern technology'], 0),
   ('Why might ancient cultures have created myths to explain natural events, like thunderstorms?', ['Storytelling offered an understandable explanation before scientific knowledge was available', 'Myths were never created to explain anything', 'This concept has no connection to writing', 'Ancient cultures always had complete scientific explanations already'], 0),
   ('Which of these is most likely the beginning of a legend?', ['Long ago, a brave warrior was said to have defended the village.', 'Add two cups of flour to the bowl.', 'The weather today will be sunny with a light breeze.', 'Multiply 6 by 7 to find the answer.'], 0)]),
M('Geometry: Classifying Quadrilaterals',
  'Grade 5 Math strand: quadrilaterals can be classified by their properties, such as a square with four equal sides and four right angles, or a trapezoid with only one pair of parallel sides.',
  [('What do we call a quadrilateral with four equal sides and four right angles?', ['A square', 'A trapezoid', 'A rhombus', 'A concept unrelated to quadrilaterals'], 0),
   ('What do we call a quadrilateral with only one pair of parallel sides?', ['A trapezoid', 'A square', 'A rectangle', 'A rhombus'], 0),
   ('Does a rectangle always have four right angles?', ['Yes', 'No, a rectangle never has any right angles', 'A concept unrelated to quadrilaterals', 'A rectangle has exactly two right angles only'], 0),
   ('What do we call a quadrilateral with four equal sides, but not necessarily four right angles?', ['A rhombus', 'A square', 'A trapezoid', 'A concept unrelated to quadrilaterals'], 0),
   ('Why might a square be considered a special type of rectangle?', ['A square has all the properties of a rectangle, plus four equal sides', 'A square and a rectangle share no properties at all', 'This concept has no connection to geometry', 'A square never has four right angles'], 0)]),
Sc('Decomposers and Nutrient Cycling in Ecosystems',
   'Grade 5 Science strand: decomposers, such as fungi, bacteria, and worms, break down dead plants and animals, returning nutrients to the soil so they can be used again by living things.',
   [('What do we call organisms, such as fungi and bacteria, that break down dead plants and animals?', ['Decomposers', 'Producers', 'A concept unrelated to ecosystems', 'Predators'], 0),
    ('Name one example of a decomposer, such as fungi or worms.', ['Fungi', 'A concept unrelated to decomposers', 'A lion', 'A hawk'], 0),
    ('What do decomposers return to the soil as they break down dead organisms?', ['Nutrients', 'Only water', 'A concept unrelated to decomposers', 'Nothing at all'], 0),
    ('Why are decomposers an essential part of an ecosystem’s nutrient cycle?', ['They recycle nutrients from dead organisms so living things can use them again', 'Decomposers have no connection to nutrient cycles', 'This concept has no relevance to science', 'Nutrients never need to be recycled in an ecosystem'], 0),
    ('Why might an ecosystem struggle if it suddenly had no decomposers at all?', ['Dead plants and animals would not break down, and nutrients would not return to the soil', 'An ecosystem would function exactly the same without any decomposers', 'This concept has no connection to decomposers', 'Decomposers have no effect on how an ecosystem functions'], 0)]),
SS('The Bank of Canada and Canada’s Monetary System',
   'Grade 5 Social Studies strand: the Bank of Canada is the country’s central bank, responsible for issuing currency and setting policies that help keep prices and the economy stable.',
   [('What is the name of Canada’s central bank?', ['The Bank of Canada', 'A concept unrelated to Canadian government', 'A private company only', 'A bank from a different country'], 0),
    ('Is the Bank of Canada responsible for issuing Canada’s currency?', ['Yes', 'No, the Bank of Canada has no connection to currency', 'A concept unrelated to the Bank of Canada', 'Only individual citizens issue currency'], 0),
    ('Does the Bank of Canada help set policies to keep prices and the economy stable?', ['Yes', 'No, the Bank of Canada has no role in the economy', 'A concept unrelated to Canada’s monetary system', 'Prices are never affected by any government policy'], 0),
    ('Why might a country need a central bank like the Bank of Canada?', ['It helps manage the money supply and keep the economy stable for everyone', 'A central bank has no useful purpose', 'This concept has no relevance to social studies', 'Every country manages its economy without any central bank'], 0),
    ('Why might rising prices across the country be a concern that the Bank of Canada tries to manage?', ['Rapidly rising prices can make it harder for people to afford everyday goods and services', 'Rising prices never have any effect on people’s daily lives', 'This concept has no connection to the Bank of Canada', 'The Bank of Canada has no responsibility for the cost of goods'], 0)]),
]),

day(96, [
L('Vocabulary: Synonyms and Antonyms',
  'Grade 5 Language strand: a synonym is a word that means the same, or nearly the same, as another word, while an antonym is a word that means the opposite of another word.',
  [('What do we call a word that means the same, or nearly the same, as another word?', ['A synonym', 'An antonym', 'A concept unrelated to vocabulary', 'A homophone'], 0),
   ('What do we call a word that means the opposite of another word?', ['An antonym', 'A synonym', 'A concept unrelated to vocabulary', 'A prefix'], 0),
   ('Which word is a synonym for happy?', ['Joyful', 'Sad', 'Angry', 'Tired'], 0),
   ('Which word is an antonym for large?', ['Small', 'Huge', 'Big', 'Giant'], 0),
   ('Why might a thesaurus be a useful tool when looking for synonyms while writing?', ['It lists words with similar meanings, helping a writer choose more precise or varied language', 'A thesaurus never lists any synonyms', 'This concept has no connection to vocabulary', 'A thesaurus only ever lists antonyms, never synonyms'], 0)]),
M('Measurement: Surface Area of Triangular Prisms',
  'Grade 5 Math strand: the surface area of a triangular prism is found by adding the areas of its two triangular bases and its three rectangular sides.',
  [('How many triangular faces does a triangular prism have?', ['2', '1', '3', '4'], 0),
   ('How many rectangular faces does a triangular prism typically have?', ['3', '2', '1', '4'], 0),
   ('To find the surface area of a triangular prism, what should you do with the areas of all its faces?', ['Add them together', 'Multiply them together', 'A concept unrelated to surface area', 'Subtract them from each other'], 0),
   ('If the two triangular faces of a prism each have an area of 6 square cm, and the three rectangular faces have areas of 10, 10, and 8 square cm, what is the total surface area?', ['40 square cm', '34 square cm', '28 square cm', '22 square cm'], 0),
   ('Why is it useful to know how to calculate the surface area of a triangular prism?', ['It helps determine how much material is needed to cover or build an object shaped like the prism', 'Surface area calculations never apply to any real objects', 'This concept has no connection to measurement', 'A triangular prism never actually has any measurable surface area'], 0)]),
Sc('Structures: Why Triangles Are the Strongest Shape',
   'Grade 5 Science strand: triangles are considered the strongest basic shape used in structures because their fixed angles resist bending and distribute force evenly, unlike squares, which can collapse into a slanted shape under pressure.',
   [('Which basic shape is considered the strongest for use in structures like bridges?', ['A triangle', 'A square', 'A circle', 'A concept unrelated to structures'], 0),
    ('Can a square shape collapse into a slanted shape more easily than a triangle under pressure?', ['Yes', 'No, a square is always stronger than a triangle', 'A concept unrelated to structures', 'Squares and triangles are always equally strong'], 0),
    ('Do the fixed angles of a triangle help it resist bending?', ['Yes', 'No, a triangle’s angles have no effect on its strength', 'A concept unrelated to structures', 'Triangles have no fixed angles at all'], 0),
    ('Why might engineers use triangle shapes, like trusses, when designing bridges?', ['Triangles distribute force evenly and hold their shape well under pressure', 'Triangles have no benefit in structural design', 'This concept has no relevance to science', 'Bridges are never built using triangle shapes'], 0),
    ('Why might a structure built only with square shapes need extra bracing for stability?', ['Squares can shift and lean under force unless something, like a diagonal brace, holds their shape', 'Square shapes never need any extra support', 'This concept has no connection to structures', 'Square shapes are always stronger than triangle shapes'], 0)]),
SS('Canada’s Universal Health Care System',
   'Grade 5 Social Studies strand: Canada has a publicly funded health care system, guided by the Canada Health Act, which provides medically necessary care to residents regardless of their ability to pay.',
   [('What do we call a health care system that is publicly funded and available to all residents?', ['A universal health care system', 'A concept unrelated to Canadian government', 'A privately owned system only', 'A system available only to wealthy citizens'], 0),
    ('What is the name of the federal law that guides Canada’s health care system?', ['The Canada Health Act', 'A concept unrelated to health care', 'The Canadian Constitution only', 'A provincial law with no federal connection'], 0),
    ('Does Canada’s health care system aim to provide care regardless of a person’s ability to pay?', ['Yes', 'No, only wealthy people can access health care in Canada', 'A concept unrelated to health care', 'Health care in Canada is never provided to anyone'], 0),
    ('Why might a universal health care system be considered important for a country’s population?', ['It can help ensure that people receive necessary medical care regardless of their income', 'Universal health care has no connection to people’s well-being', 'This concept has no relevance to social studies', 'A universal health care system never actually provides any care'], 0),
    ('Why is health care in Canada mainly delivered by provincial governments, even though it follows a federal law?', ['Health care is a provincial responsibility, so each province manages its own delivery system', 'Health care is never actually managed by any level of government', 'This concept has no connection to Canadian government', 'The federal government directly runs every hospital in Canada'], 0)]),
]),

day(97, [
L('Reading: Identifying Protagonist and Antagonist',
  'Grade 5 Language strand: the protagonist is the main character a story follows, while the antagonist is the character or force that opposes the protagonist and creates conflict.',
  [('What do we call the main character a story follows?', ['The protagonist', 'The antagonist', 'A concept unrelated to reading', 'The setting'], 0),
   ('What do we call the character or force that opposes the main character?', ['The antagonist', 'The protagonist', 'A concept unrelated to reading', 'The narrator'], 0),
   ('Does the antagonist typically create conflict for the protagonist?', ['Yes', 'No, the antagonist never creates any conflict', 'A concept unrelated to reading comprehension', 'The antagonist always helps the protagonist'], 0),
   ('Why might a story feel less interesting without a clear antagonist or obstacle for the protagonist?', ['Conflict often drives the plot and keeps readers engaged in what happens next', 'A story never needs any conflict to be interesting', 'This concept has no connection to reading comprehension', 'Antagonists never have any effect on a story’s plot'], 0),
   ('Can an antagonist sometimes be a force, such as a storm, rather than a person?', ['Yes', 'No, an antagonist must always be a person', 'A concept unrelated to reading', 'A story can never have a non-human antagonist'], 0)]),
M('Number Sense: Integers in Real-Life Contexts',
  'Grade 5 Math strand: integers can represent real-life situations, such as temperatures below zero shown as negative numbers or elevations below sea level shown as negative numbers.',
  [('If the temperature is 5 degrees below zero, how would this be written as an integer?', ['-5', '5', '0', '-10'], 0),
   ('If a location is 100 metres below sea level, how would this elevation be written as an integer?', ['-100', '100', '0', '-1'], 0),
   ('Which temperature is colder: -8 degrees or -3 degrees?', ['-8 degrees', '-3 degrees', 'They are the same temperature', 'A concept unrelated to integers'], 0),
   ('If the temperature rises from -6 degrees to -2 degrees, by how many degrees did it increase?', ['4 degrees', '8 degrees', '2 degrees', '6 degrees'], 0),
   ('Why are negative integers useful for describing real-world measurements like temperature or elevation?', ['They allow values below a starting point, like zero or sea level, to be represented clearly', 'Negative integers have no real-world use at all', 'This concept has no connection to number sense', 'Temperatures and elevations can never go below zero'], 0)]),
Sc('Camouflage and Animal Defense Mechanisms',
   'Grade 5 Science strand: many animals rely on defense mechanisms, such as camouflage that blends them into their surroundings, warning colours, or physical features like spines, to avoid predators.',
   [('What do we call it when an animal’s colouring or pattern helps it blend into its surroundings?', ['Camouflage', 'A concept unrelated to adaptations', 'Migration', 'Hibernation'], 0),
    ('Name one physical feature an animal might use to defend itself, such as spines.', ['Spines', 'A concept unrelated to animal defenses', 'A pleasant smell', 'A soft texture'], 0),
    ('Can bright warning colours on an animal signal to predators that it may be dangerous or unpleasant to eat?', ['Yes', 'No, warning colours never signal anything to predators', 'A concept unrelated to animal defenses', 'Bright colours always attract predators intentionally'], 0),
    ('Why might camouflage be especially useful for an animal trying to avoid a predator?', ['Blending into the environment can make the animal harder for a predator to notice', 'Camouflage never helps an animal avoid being seen', 'This concept has no relevance to science', 'Predators can always see camouflaged animals with no difficulty'], 0),
    ('Why might different animals in the same habitat have developed very different defense mechanisms?', ['Different body types and behaviours can lead to different effective strategies for survival', 'All animals in the same habitat always use the exact same defense mechanism', 'This concept has no connection to animal defenses', 'Defense mechanisms never vary between different animal species'], 0)]),
SS('Criminal Law vs Civil Law in the Canadian Justice System',
   'Grade 5 Social Studies strand: criminal law deals with actions considered offences against society, such as theft, prosecuted by the government, while civil law deals with disputes between individuals or groups, such as contract disagreements.',
   [('What type of law deals with actions considered offences against society, such as theft?', ['Criminal law', 'Civil law', 'A concept unrelated to the justice system', 'International law'], 0),
    ('What type of law deals with disputes between individuals or groups, such as contract disagreements?', ['Civil law', 'Criminal law', 'A concept unrelated to the justice system', 'Constitutional law'], 0),
    ('In a criminal law case, who typically prosecutes the accused person?', ['The government', 'Only the victim personally', 'A concept unrelated to criminal law', 'No one prosecutes in a criminal case'], 0),
    ('Why might a disagreement over a broken contract between two businesses be handled as a civil law matter?', ['It is a dispute between parties rather than an offence against society as a whole', 'Contract disagreements are never handled through any legal process', 'This concept has no connection to the justice system', 'All disagreements between businesses are automatically criminal matters'], 0),
    ('Why is it useful for a justice system to separate criminal law from civil law?', ['It allows different types of legal issues to be handled with rules suited to their purpose', 'Separating criminal and civil law never has any benefit', 'This concept has no relevance to social studies', 'Criminal law and civil law are always handled in the exact same way'], 0)]),
]),

day(98, [
L('Grammar: Capitalization Rules',
  'Grade 5 Language strand: capitalization rules include capitalizing the first word of a sentence, proper nouns, titles, the pronoun I, and the days of the week and months of the year.',
  [('Which of these should always be capitalized, no matter where it appears in a sentence?', ['The pronoun I', 'A common noun like dog', 'A verb like run', 'An adjective like happy'], 0),
   ('Should the first word of a sentence always be capitalized?', ['Yes', 'No, the first word is never capitalized', 'A concept unrelated to grammar', 'Only questions require capitalization'], 0),
   ('Which of these is an example of a proper noun that should be capitalized?', ['Toronto', 'city', 'building', 'street'], 0),
   ('Should the days of the week, such as Monday, be capitalized?', ['Yes', 'No, days of the week are never capitalized', 'A concept unrelated to capitalization', 'Only some days of the week are capitalized'], 0),
   ('Why is it important to capitalize proper nouns, like the names of specific people or places?', ['It helps distinguish specific, named things from general, common nouns', 'Capitalization never provides any useful information to a reader', 'This concept has no connection to grammar', 'Proper nouns and common nouns are always treated exactly the same way'], 0)]),
M('Financial Literacy: Simple Budgeting for a Savings Goal',
  'Grade 5 Math strand: students learn to create a simple budget by tracking income and expenses to figure out how much money can be saved toward a specific goal over time.',
  [('What do we call a plan that tracks income and expenses to help manage money?', ['A budget', 'A concept unrelated to financial literacy', 'A recipe', 'A map'], 0),
   ('If you earn 20 dollars a week in allowance and spend 12 dollars, how much can you save each week?', ['8 dollars', '20 dollars', '12 dollars', '32 dollars'], 0),
   ('If you save 5 dollars a week, how many weeks will it take to save 30 dollars?', ['6 weeks', '5 weeks', '30 weeks', '10 weeks'], 0),
   ('What is the term for money you receive, such as allowance or gifts?', ['Income', 'An expense', 'A concept unrelated to budgeting', 'A loan'], 0),
   ('Why is it helpful to set a savings goal before you start budgeting your money?', ['A clear goal can help you decide how much to save and how long it might take', 'Savings goals never help with budgeting money', 'This concept has no connection to financial literacy', 'A budget is never affected by having a specific goal'], 0)]),
Sc('Coral Reefs and Marine Ecosystems',
   'Grade 5 Science strand: coral reefs are built by tiny living organisms called coral polyps and support a huge variety of marine life, but they are sensitive to changes in ocean temperature.',
   [('What tiny living organisms build coral reefs?', ['Coral polyps', 'Fish', 'A concept unrelated to marine ecosystems', 'Whales'], 0),
    ('Do coral reefs support a large variety of marine life?', ['Yes', 'No, coral reefs support no marine life at all', 'A concept unrelated to coral reefs', 'Only one single species lives in coral reefs'], 0),
    ('Are coral reefs sensitive to changes in ocean temperature?', ['Yes', 'No, coral reefs are never affected by temperature', 'A concept unrelated to coral reefs', 'Ocean temperature has no connection to marine ecosystems'], 0),
    ('Why might rising ocean temperatures be harmful to coral reefs?', ['Warmer water can stress coral polyps, sometimes causing coral bleaching and reef damage', 'Rising temperatures never have any effect on coral reefs', 'This concept has no relevance to science', 'Coral reefs always grow faster in warmer ocean water'], 0),
    ('Why are coral reefs sometimes described as important habitats for ocean life?', ['They provide shelter, food, and breeding grounds for many different marine species', 'Coral reefs provide no habitat value for any marine species', 'This concept has no connection to marine ecosystems', 'Marine life never depends on coral reefs in any way'], 0)]),
SS('The Group of Seven and Canadian Landscape Art',
   'Grade 5 Social Studies strand: the Group of Seven was a collection of Canadian painters in the early 1900s known for their bold depictions of Canada’s wilderness, helping shape a distinct Canadian artistic identity.',
   [('What was the name of the group of Canadian painters known for depicting Canada’s wilderness in the early 1900s?', ['The Group of Seven', 'A concept unrelated to Canadian art', 'A modern film studio', 'A sports league'], 0),
    ('Did the Group of Seven often paint scenes of Canada’s natural landscapes?', ['Yes', 'No, the Group of Seven never painted landscapes', 'A concept unrelated to Canadian art', 'They painted only city skylines from other countries'], 0),
    ('Around what time period was the Group of Seven active?', ['The early 1900s', 'The 1600s', 'A concept unrelated to Canadian art history', 'The present day only'], 0),
    ('Why might the Group of Seven’s paintings have helped shape a distinct Canadian artistic identity?', ['Their bold depictions of Canadian wilderness offered a new way of representing the country through art', 'Their paintings had no connection to Canadian identity at all', 'This concept has no relevance to social studies', 'The Group of Seven never painted anything related to Canada'], 0),
    ('Why might studying historical art movements, like the Group of Seven, help students understand a country’s culture?', ['Art can reflect how people at a certain time viewed and valued their surroundings', 'Art has no connection to understanding a country’s culture', 'This concept has no connection to social studies', 'Historical art movements never reveal anything about a culture'], 0)]),
]),

day(99, [
L('Writing: Note-Taking and Paraphrasing',
  'Grade 5 Language strand: note-taking involves recording key words and ideas rather than full sentences, while paraphrasing means restating information in your own words without copying the original text.',
  [('What does it mean to paraphrase information from a text?', ['Restating it in your own words', 'Copying it word for word', 'A concept unrelated to writing', 'Ignoring the information completely'], 0),
   ('When taking notes, should you usually write full sentences or key words and ideas?', ['Key words and ideas', 'Full sentences only', 'A concept unrelated to note-taking', 'Nothing at all should be written'], 0),
   ('Why is it important to paraphrase rather than copy text directly when researching a topic?', ['It shows understanding of the material and avoids copying someone else’s exact words', 'Paraphrasing is never useful when researching a topic', 'This concept has no connection to writing', 'Copying text directly is always the preferred method for research'], 0),
   ('Which of these is an example of good note-taking?', ['Writing short phrases like frogs: cold-blooded, live in water and land', 'Copying every single word from the textbook', 'Drawing only a picture with no words', 'Writing nothing down at all'], 0),
   ('Why might organized notes be especially helpful when writing a research report later?', ['They make it easier to find and organize key information without searching the entire original source again', 'Notes never help when writing a report', 'This concept has no connection to writing', 'A research report can only ever be written without using any notes'], 0)]),
M('Geometry: Volume of Composite Rectangular Figures',
  'Grade 5 Math strand: to find the volume of a composite figure made of rectangular prisms, students break the shape into smaller rectangular prisms, find each volume, and add them together.',
  [('To find the volume of a composite figure, what should you do first?', ['Break it into smaller rectangular prisms', 'Multiply every measurement by ten', 'A concept unrelated to volume', 'Ignore part of the shape entirely'], 0),
   ('After finding the volume of each smaller prism in a composite figure, what should you do next?', ['Add the volumes together', 'Subtract the volumes from each other', 'A concept unrelated to volume', 'Multiply the volumes together'], 0),
   ('If a composite figure is made of two rectangular prisms with volumes of 24 cubic cm and 18 cubic cm, what is the total volume?', ['42 cubic cm', '24 cubic cm', '18 cubic cm', '432 cubic cm'], 0),
   ('If a composite figure is made of three prisms with volumes of 10, 15, and 5 cubic cm, what is the total volume?', ['30 cubic cm', '25 cubic cm', '20 cubic cm', '15 cubic cm'], 0),
   ('Why is it helpful to break a composite figure into smaller, simpler shapes before finding its volume?', ['It is easier to calculate the volume of simple shapes and then combine the results', 'Breaking a shape apart never helps with finding its volume', 'This concept has no connection to geometry', 'Composite figures can never actually be separated into smaller shapes'], 0)]),
Sc('Microorganisms: Bacteria, Viruses, and Fungi',
   'Grade 5 Science strand: microorganisms, including bacteria, viruses, and fungi, are tiny living or non-living things, some of which can cause illness while others help with processes like decomposition and fermentation.',
   [('What do we call tiny organisms, such as bacteria and fungi, that are often too small to see without a microscope?', ['Microorganisms', 'A concept unrelated to biology', 'Mammals', 'Reptiles'], 0),
    ('Name one type of microorganism, such as bacteria.', ['Bacteria', 'A concept unrelated to microorganisms', 'A dog', 'A bird'], 0),
    ('Can some microorganisms be helpful, such as by aiding in decomposition or fermentation?', ['Yes', 'No, all microorganisms are always harmful', 'A concept unrelated to microorganisms', 'Microorganisms never have any function at all'], 0),
    ('Why might some microorganisms, like certain bacteria and viruses, cause illness in humans?', ['They can multiply inside the body and disrupt normal bodily functions', 'Microorganisms never cause any illness', 'This concept has no relevance to science', 'Illness is never connected to microorganisms in any way'], 0),
    ('Why is it useful to understand that not all microorganisms are harmful?', ['It helps recognize that many microorganisms play beneficial roles, like helping break down waste', 'Understanding microorganisms never has any usefulness', 'This concept has no connection to science', 'All microorganisms behave in exactly the same harmful way'], 0)]),
SS('Canadian National Holidays and Celebrations',
   'Grade 5 Social Studies strand: Canada observes national holidays, such as Canada Day on July 1 and Remembrance Day on November 11, which mark important events and values in the country’s history.',
   [('On what date is Canada Day celebrated?', ['July 1', 'January 1', 'November 11', 'December 25'], 0),
    ('On what date is Remembrance Day observed in Canada?', ['November 11', 'July 1', 'October 31', 'September 1'], 0),
    ('Does Canada Day mark an important event in the country’s history?', ['Yes', 'No, Canada Day has no historical significance', 'A concept unrelated to Canadian holidays', 'Canada Day is not an actual holiday'], 0),
    ('Why might Remembrance Day be an important day for many Canadians to observe?', ['It honours the sacrifices of those who served in wars and conflicts', 'Remembrance Day has no meaning or purpose', 'This concept has no relevance to social studies', 'Remembrance Day only celebrates a sports event'], 0),
    ('Why might national holidays help bring people across a country together?', ['They give communities a shared occasion to reflect on or celebrate common history and values', 'National holidays never bring communities together in any way', 'This concept has no connection to Canadian identity', 'Every Canadian celebrates each holiday in a completely different, unrelated way'], 0)]),
]),

day(100, [
L('Review: Figurative Language, Grammar, and Reading (Days 91-99)',
  'Grade 5 Language strand review: students revisit similes, conjunctions, plot structure, elements of poetry, writing a myth or legend, synonyms and antonyms, protagonist and antagonist, capitalization rules, and note-taking and paraphrasing.',
  [('What do we call a comparison between two unlike things that uses the word like or as?', ['A simile', 'A concept unrelated to figurative language', 'A homophone', 'A prefix'], 0),
   ('Which of these is a subordinating conjunction?', ['Because', 'And', 'But', 'Or'], 0),
   ('What is the term for the part of a story where the main conflict reaches its most intense point?', ['The climax', 'The exposition', 'The falling action', 'The resolution'], 0),
   ('What do we call a word that means the opposite of another word?', ['An antonym', 'A synonym', 'A concept unrelated to vocabulary', 'A prefix'], 0),
   ('What do we call the main character a story follows?', ['The protagonist', 'The antagonist', 'A concept unrelated to reading', 'The setting'], 0)]),
M('Review: Geometry, Number Sense, and Financial Literacy (Days 91-99)',
  'Grade 5 Math strand review: students revisit classifying triangles and quadrilaterals, area of triangles and parallelograms, powers of ten, tree diagrams, surface area of triangular prisms, integers in real life, budgeting, and composite volume.',
  [('What do we call a triangle with all three sides equal in length?', ['An equilateral triangle', 'A scalene triangle', 'An obtuse triangle', 'A right triangle'], 0),
   ('What is the formula for the area of a triangle?', ['One half of base times height', 'Base times height', 'Base plus height', 'Base divided by height'], 0),
   ('What is 45 multiplied by 100?', ['4500', '450', '45000', '4.5'], 0),
   ('If the temperature is 5 degrees below zero, how would this be written as an integer?', ['-5', '5', '0', '-10'], 0),
   ('To find the volume of a composite figure, what should you do first?', ['Break it into smaller rectangular prisms', 'Multiply every measurement by ten', 'A concept unrelated to volume', 'Ignore part of the shape entirely'], 0)]),
Sc('Review: Body Systems, Earth Science, and Life Science (Days 91-99)',
   'Grade 5 Science strand review: students revisit the endocrine system, plate tectonics, kinetic and potential energy, the human ear, decomposers, why triangles are the strongest shape, camouflage, coral reefs, and microorganisms.',
   [('What do we call the body system made up of glands that release hormones into the bloodstream?', ['The endocrine system', 'A concept unrelated to the body', 'The digestive system', 'The skeletal system'], 0),
    ('What do we call the large sections of Earth’s crust that move very slowly over time?', ['Tectonic plates', 'A concept unrelated to Earth science', 'Ocean currents', 'Weather systems'], 0),
    ('What do we call the energy of motion, such as a rolling ball has?', ['Kinetic energy', 'Potential energy', 'A concept unrelated to energy', 'Chemical energy'], 0),
    ('What do we call organisms, such as fungi and bacteria, that break down dead plants and animals?', ['Decomposers', 'Producers', 'A concept unrelated to ecosystems', 'Predators'], 0),
    ('What tiny living organisms build coral reefs?', ['Coral polyps', 'Fish', 'A concept unrelated to marine ecosystems', 'Whales'], 0)]),
SS('Review: Canadian Institutions, History, and Culture (Days 91-99)',
   'Grade 5 Social Studies strand review: students revisit Canada’s music and film industry, provinces joining Confederation, the RCMP, division of powers, the Bank of Canada, universal health care, criminal versus civil law, the Group of Seven, and national holidays.',
   [('Which province was the last to join Confederation, in 1949?', ['Newfoundland', 'British Columbia', 'Manitoba', 'Prince Edward Island'], 0),
    ('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Regional Canadian Municipal Patrol', 'A concept unrelated to Canadian history', 'Royal Canadian Marine Patrol'], 0),
    ('What is the name of Canada’s central bank?', ['The Bank of Canada', 'A concept unrelated to Canadian government', 'A private company only', 'A bank from a different country'], 0),
    ('What type of law deals with actions considered offences against society, such as theft?', ['Criminal law', 'Civil law', 'A concept unrelated to the justice system', 'International law'], 0),
    ('On what date is Canada Day celebrated?', ['July 1', 'January 1', 'November 11', 'December 25'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_91_100)
    append_to(5, g5_91_100)
