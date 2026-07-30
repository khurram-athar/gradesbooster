#!/usr/bin/env python3
"""Grade 6, Days 121-130 -- extends Grade 6 from 120 to 130 days. Modeled
exactly on gen_grade6_days111_120.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-120
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: subject-
verb agreement, comparative and superlative adjectives, writing a
limerick, writing a eulogy or tribute, portmanteau words and blends,
evaluating online product reviews, impromptu speaking, understanding
analogies, and text-to-self/text/world reading connections for Language;
scientific notation, sum of interior angles in polygons, angles formed by
a transversal, volume of a sphere, repeating and terminating decimals,
translating word problems into algebraic expressions, weighted averages,
cumulative frequency tables, and reading/writing large numbers in the
millions and billions for Math; kinetic and potential energy, comets
asteroids and meteors, air pressure and weather, keystone species,
pulleys, insect and amphibian metamorphosis, bioaccumulation in food
chains, geothermal energy, and watersheds/drainage basins for Science;
and Canadian national symbols, the Persons Case, Canada's points-based
immigration system, the St. Lawrence Seaway, the Komagata Maru incident,
the Avro Arrow, the Halifax Explosion, Canada's national sports, and the
Canadian Pacific Railway for Social Studies -- none of those exact ideas
appear in Days 1-120. Day 130 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch. No
embedded ASCII apostrophe or double-quote characters are used anywhere in
title/summary/question/option text -- apostrophes are dropped entirely
(e.g. "Canadas" not "Canada's"), matching the rest of Grade 6.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science and Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


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


g6_121_130 = [
day(121, [
L('Grammar: Subject-Verb Agreement',
  'Grade 6 Language strand: subject-verb agreement requires a verb to match its subject in number, so singular subjects take singular verbs and plural subjects take plural verbs.',
  [('What does subject-verb agreement require?', ['A verb that matches its subject in number', 'A verb that always ends in s', 'A subject placed after the verb', 'A sentence with no verb at all'], 0),
   ('Which sentence shows correct subject-verb agreement?', ['The students are working quietly in the library.', 'The students is working quietly in the library.', 'The student are working quietly in the library.', 'The students working quietly in the library.'], 0),
   ('Which verb correctly completes this sentence: The team ___ practicing every afternoon this week.', ['is', 'are', 'were', 'have'], 0),
   ('Why can a long phrase between the subject and verb make agreement tricky?', ['It can make a writer mistakenly match the verb to a nearby word instead of the true subject', 'Long phrases always require plural verbs', 'Agreement rules only apply to short sentences', 'Verbs never need to match their subject in a long sentence'], 0),
   ('Which sentence is grammatically correct?', ['Neither of the answers was correct.', 'Neither of the answers were correct.', 'Neither of the answers is were correct.', 'Neither of the answer was correct.'], 0)]),
M('Number Sense: Introduction to Scientific Notation',
  'Grade 6 Math strand: scientific notation expresses very large or very small numbers as a number between 1 and 10 multiplied by a power of ten, making such numbers easier to read and compare.',
  [('What does scientific notation help express?', ['Very large or very small numbers in a compact form', 'Only numbers between 0 and 1', 'Fractions with large denominators only', 'Numbers that have no decimal point'], 0),
   ('In scientific notation, the first factor is a number between which two values?', ['1 and 10', '10 and 100', '0 and 1', '100 and 1000'], 0),
   ('Which of these is 4,500 written in scientific notation?', ['4.5 x 10^3', '45 x 10^2', '4.5 x 10^2', '0.45 x 10^4'], 0),
   ('Why is scientific notation useful for scientists working with numbers like the distance to a star?', ['It allows extremely large numbers to be written and compared more easily', 'It makes large numbers harder to read', 'Scientific notation can only be used for small numbers', 'It removes the need for any numbers at all'], 0),
   ('What does the exponent in scientific notation tell you?', ['How many places to move the decimal point', 'The exact value of the number with no further calculation', 'The number of digits in the answer only', 'Nothing useful about the number'], 0)]),
Sc('Kinetic and Potential Energy',
   'Grade 6 Science strand: kinetic energy is the energy of motion, while potential energy is stored energy based on an objects position or condition, and energy can transform between these two forms.',
   [('What is kinetic energy?', ['The energy of motion', 'Stored energy based on position', 'Energy that never changes form', 'A type of chemical reaction'], 0),
    ('What is potential energy?', ['Stored energy based on an objects position or condition', 'The energy of motion only', 'Energy found only in electrical circuits', 'Energy that cannot be transformed into anything else'], 0),
    ('A ball held at the top of a hill has mostly what type of energy?', ['Potential energy', 'Kinetic energy', 'Sound energy', 'No energy at all'], 0),
    ('As the ball rolls down the hill, what happens to its potential energy?', ['It converts into kinetic energy as the ball speeds up', 'It disappears completely with no transformation', 'It stays exactly the same the whole way down', 'It converts into potential energy at the bottom'], 0),
    ('Why is understanding kinetic and potential energy useful for explaining how a roller coaster works?', ['The energy continuously transforms between potential and kinetic as the coaster rises and falls', 'Roller coasters have no connection to energy transformation', 'Roller coasters use only kinetic energy at all times', 'Energy never changes form on a roller coaster'], 0)]),
SS('Social Studies: Canadian National Symbols — Flag, Anthem, and Coat of Arms',
   'Grade 6 Social Studies strand: Canada has several official national symbols, including the maple leaf flag, the national anthem O Canada, and the coat of arms, each representing aspects of the countrys identity and history.',
   [('What image appears on the Canadian flag?', ['A red maple leaf', 'A golden eagle', 'A blue star', 'A green shamrock'], 0),
    ('What is the name of Canadas national anthem?', ['O Canada', 'God Save the King', 'The Maple Leaf Forever', 'True North Strong'], 0),
    ('What is a coat of arms?', ['An official symbol representing a country, family, or organization', 'A type of winter clothing', 'A style of Canadian currency', 'A national holiday'], 0),
    ('Why do countries often adopt official symbols like flags and anthems?', ['They help represent a shared national identity and history', 'Symbols have no connection to national identity', 'Flags and anthems are chosen randomly with no meaning', 'National symbols are only used in other countries, not Canada'], 0),
    ('When was the current Canadian maple leaf flag officially adopted?', ['In 1965', 'In 1867', 'In 2000', 'In 1812'], 0)]),
]),
day(122, [
L('Grammar: Comparative and Superlative Adjectives',
  'Grade 6 Language strand: comparative adjectives compare two things, usually adding er or using more, while superlative adjectives compare three or more things, usually adding est or using most.',
  [('What does a comparative adjective do?', ['Compares two things', 'Compares three or more things', 'Describes only one thing with no comparison', 'Replaces a noun entirely'], 0),
   ('What does a superlative adjective do?', ['Compares three or more things', 'Compares exactly two things', 'Describes an action instead of a thing', 'Has no comparative function at all'], 0),
   ('Which is the correct superlative form of tall?', ['tallest', 'taller', 'more tall', 'most taller'], 0),
   ('Which sentence uses a comparative adjective correctly?', ['This backpack is heavier than that one.', 'This backpack is heaviest than that one.', 'This backpack is more heavier than that one.', 'This backpack is heavy than that one.'], 0),
   ('Why do longer adjectives, like beautiful, usually use more or most instead of adding er or est?', ['Adding er or est to longer words would be awkward to pronounce, so English speakers use more or most instead', 'Longer adjectives can never be compared', 'All adjectives use the exact same comparison rule regardless of length', 'Long adjectives are never used in comparisons'], 0)]),
M('Geometry: Sum of Interior Angles in Polygons',
  'Grade 6 Math strand: the sum of the interior angles of a polygon can be found using the formula (n minus 2) times 180 degrees, where n is the number of sides, extending the idea that a triangles angles sum to 180 degrees.',
  [('What formula finds the sum of the interior angles of a polygon with n sides?', ['(n minus 2) times 180 degrees', 'n times 90 degrees', 'n times 180 degrees', '(n plus 2) times 180 degrees'], 0),
   ('What is the sum of the interior angles of a quadrilateral (4 sides)?', ['360 degrees', '180 degrees', '540 degrees', '720 degrees'], 0),
   ('What is the sum of the interior angles of a pentagon (5 sides)?', ['540 degrees', '360 degrees', '450 degrees', '900 degrees'], 0),
   ('Why does the interior angle sum formula start by subtracting 2 from the number of sides?', ['Any polygon can be divided into (n minus 2) triangles, each contributing 180 degrees', 'Subtracting 2 has no mathematical meaning in this formula', 'Every polygon has exactly 2 fewer angles than sides', 'The formula ignores the number of sides entirely'], 0),
   ('As the number of sides in a regular polygon increases, what happens to the sum of its interior angles?', ['It increases', 'It stays exactly the same', 'It decreases', 'It always equals 180 degrees'], 0)]),
Sc('Comets, Asteroids, and Meteors',
   'Grade 6 Science strand: comets are icy bodies that develop glowing tails near the sun, asteroids are rocky bodies mostly found in the asteroid belt, and meteors are streaks of light produced when small space debris burns up in Earths atmosphere.',
   [('What is a comet mostly made of?', ['Ice and dust', 'Solid metal only', 'Liquid water only', 'Pure rock with no ice'], 0),
    ('Where are most asteroids in our solar system found?', ['In the asteroid belt between Mars and Jupiter', 'Inside the sun', 'On the surface of Earth', 'Beyond the edge of the solar system only'], 0),
    ('What causes a comets glowing tail to appear?', ['Heat from the sun causes ice and dust to release gas and particles', 'The tail is caused by the comet spinning rapidly', 'Comets never develop tails', 'The tail forms only when a comet is far from the sun'], 0),
    ('What is a meteor?', ['A streak of light caused by small space debris burning up in the atmosphere', 'A large planet outside our solar system', 'A permanent ring of ice around a planet', 'A type of star that never moves'], 0),
    ('What is the difference between a meteor and a meteorite?', ['A meteorite is the debris that survives and lands on Earths surface, while a meteor is the streak of light seen burning up', 'There is no difference between the two terms', 'A meteorite is always larger than a planet', 'A meteor is a type of comet with no tail'], 0)]),
SS('Social Studies: The Persons Case — Winning Legal Recognition for Women in Canada',
   'Grade 6 Social Studies strand: the Persons Case was a 1929 legal ruling that recognized women as persons under Canadian law, allowing them to be appointed to the Senate, a milestone achieved through the efforts of activists known as the Famous Five.',
   [('What did the Persons Case establish?', ['That women are legally recognized as persons under Canadian law', 'That only men could serve in government', 'A new set of provincial boundaries', 'A change to Canadas national currency'], 0),
    ('In what year was the Persons Case decided?', ['1929', '1867', '1982', '1945'], 0),
    ('What government position did the Persons Case allow women to be appointed to?', ['The Senate', 'The Supreme Court judge role exclusively', 'The office of Governor General only', 'No new positions were affected'], 0),
    ('Who were the group of activists known as the Famous Five who led the Persons Case?', ['A group of women who campaigned for womens legal rights in Canada', 'A group of male senators opposed to womens rights', 'A sports team from the 1920s', 'A group with no connection to Canadian history'], 0),
    ('Why is the Persons Case considered an important milestone in Canadian history?', ['It expanded legal rights and recognition for women in Canadian society', 'It had no lasting impact on Canadian law', 'It reduced the rights of women in Canada', 'It only affected a single province'], 0)]),
]),
day(123, [
L('Writing: Writing a Limerick',
  'Grade 6 Language strand: a limerick is a humorous five-line poem with an AABBA rhyme scheme, where the first, second, and fifth lines rhyme and are longer than the shorter third and fourth lines, which also rhyme with each other.',
  [('How many lines does a limerick have?', ['Five', 'Three', 'Seven', 'Ten'], 0),
   ('What is the rhyme scheme of a limerick?', ['AABBA', 'ABAB', 'AAAA', 'ABCD'], 0),
   ('What tone do limericks typically have?', ['Humorous or playful', 'Extremely formal', 'Purely factual', 'Always tragic'], 0),
   ('In a limerick, which lines are usually shorter than the others?', ['The third and fourth lines', 'The first and second lines', 'Only the last line', 'All five lines are the same length'], 0),
   ('Why might a limericks strict rhyme and rhythm pattern be challenging for a writer?', ['Every line must fit the pattern while still making sense and staying funny', 'Limericks have no rules to follow at all', 'Limericks are always written in free verse', 'Rhyme never matters in a limerick'], 0)]),
M('Geometry: Classifying Angles Formed by a Transversal',
  'Grade 6 Math strand: when a transversal line crosses two parallel lines, it creates pairs of angles, such as corresponding angles and alternate interior angles, that have special equal or supplementary relationships.',
  [('What is a transversal?', ['A line that crosses two or more other lines', 'A line that never crosses any other line', 'A single point where two lines meet', 'A curved line with no straight sections'], 0),
   ('When a transversal crosses two parallel lines, what is true about corresponding angles?', ['They are equal in measure', 'They always add up to 90 degrees', 'They are never related to each other', 'They are always different in measure'], 0),
   ('What are alternate interior angles?', ['Angles on opposite sides of the transversal, between the two parallel lines', 'Angles that are always outside the parallel lines', 'Angles that are always equal to 90 degrees', 'Angles that never appear when a transversal crosses parallel lines'], 0),
   ('If two lines crossed by a transversal are parallel, what is true about alternate interior angles?', ['They are equal in measure', 'They always add up to 360 degrees', 'They are always supplementary', 'They have no relationship to each other'], 0),
   ('Why is understanding transversal angle relationships useful in geometry?', ['It helps determine unknown angle measures when parallel lines are involved', 'It has no practical use in solving geometry problems', 'It only applies to lines that are not parallel', 'It replaces the need to know about triangles'], 0)]),
Sc('Air Pressure and How It Affects Weather',
   'Grade 6 Science strand: air pressure is the force exerted by the weight of air in the atmosphere, and areas of high and low pressure influence weather patterns, with low pressure often associated with clouds and precipitation.',
   [('What is air pressure?', ['The force exerted by the weight of air in the atmosphere', 'The temperature of the air only', 'The speed at which wind blows', 'A measurement of humidity only'], 0),
    ('What weather is often associated with low air pressure?', ['Clouds and precipitation', 'Always clear, sunny skies', 'No weather changes at all', 'Only extremely cold temperatures'], 0),
    ('What weather is often associated with high air pressure?', ['Generally clear and calmer conditions', 'Heavy storms and precipitation', 'Constant snowfall', 'No connection to weather conditions'], 0),
    ('What instrument is commonly used to measure air pressure?', ['A barometer', 'A thermometer', 'A compass', 'A rain gauge'], 0),
    ('Why do meteorologists monitor changes in air pressure to help forecast weather?', ['Shifts in air pressure often signal upcoming changes in weather conditions', 'Air pressure has no connection to weather forecasting', 'Air pressure never changes over time', 'Weather can be predicted only by measuring temperature'], 0)]),
SS('Social Studies: Canadas Points-Based Immigration System',
   'Grade 6 Social Studies strand: Canadas points-based immigration system evaluates prospective immigrants using factors such as education, work experience, language ability, and age, awarding points that determine eligibility for permanent residency.',
   [('What does Canadas points-based immigration system evaluate?', ['Factors such as education, work experience, language ability, and age', 'Only a persons country of origin', 'Only a persons age', 'Nothing related to a persons skills or background'], 0),
    ('What can a high point total in this system help a prospective immigrant achieve?', ['Eligibility for permanent residency in Canada', 'Automatic Canadian citizenship with no application', 'A guaranteed job placement', 'Exemption from all immigration rules'], 0),
    ('Why might strong language ability in English or French increase an applicants points?', ['Language skills can support successful integration into Canadian workplaces and communities', 'Language ability has no connection to immigration decisions', 'Only fluency in a third language is considered', 'Language points are never part of the system'], 0),
    ('Why might a country use a points-based system instead of other immigration approaches?', ['It provides a structured way to assess how well applicants may contribute to the economy and society', 'Points-based systems ignore an applicants skills and background entirely', 'This approach removes any need for immigration policy', 'A points-based system guarantees entry to everyone who applies'], 0),
    ('Which factor listed is commonly considered in Canadas points-based immigration system?', ['Work experience', 'Favourite hobby', 'Height', 'Eye colour'], 0)]),
]),
day(124, [
L('Writing: Writing a Eulogy or Tribute',
  'Grade 6 Language strand: a eulogy or tribute is a speech or piece of writing that honours a persons life and achievements, often shared at a memorial or celebration, using warm, respectful, and personal language.',
  [('What is the main purpose of a eulogy or tribute?', ['To honour a persons life and achievements', 'To criticize someone publicly', 'To report breaking news', 'To argue a persuasive position'], 0),
   ('What tone does a eulogy or tribute usually have?', ['Warm, respectful, and personal', 'Harsh and critical', 'Purely technical', 'Comedic and mocking'], 0),
   ('Where is a eulogy or tribute most often shared?', ['At a memorial or celebration', 'In a science textbook', 'In a weather report', 'In an instruction manual'], 0),
   ('Why might a eulogy include specific stories or memories about a person?', ['Specific details help capture what made the person unique and meaningful to others', 'Details are never included in a eulogy', 'A eulogy should avoid mentioning the person at all', 'Specific memories make a tribute less personal'], 0),
   ('Why is choosing respectful, thoughtful language especially important when writing a tribute?', ['The writing honours someone and is often shared with people who cared about that person', 'Word choice never matters in this type of writing', 'A tribute is meant to entertain with jokes only', 'Tributes are never read aloud to an audience'], 0)]),
M('Geometry: Volume of a Sphere',
  'Grade 6 Math strand: the volume of a sphere is found using the formula four-thirds times pi times the radius cubed, describing how much space is enclosed inside a perfectly round three-dimensional shape.',
  [('What formula is used to find the volume of a sphere?', ['Four-thirds times pi times the radius cubed', 'Four times pi times the radius squared', 'Pi times the radius squared times the height', 'Two-thirds times pi times the radius cubed'], 0),
   ('What measurement is needed to calculate the volume of a sphere?', ['The radius', 'Only the diameter with no other calculation', 'The surface area alone', 'The circumference alone'], 0),
   ('A basketball is an example of what three-dimensional shape?', ['A sphere', 'A cone', 'A cylinder', 'A pyramid'], 0),
   ('If a spheres radius is doubled, what happens to its volume?', ['It increases significantly, by a factor of eight', 'It stays exactly the same', 'It decreases', 'It doubles exactly'], 0),
   ('Volume of a sphere, like all volume measurements, is expressed in what type of units?', ['Cubic units', 'Square units', 'Linear units only', 'No units at all'], 0)]),
Sc('Keystone Species and Their Role in Ecosystems',
   'Grade 6 Science strand: a keystone species is an organism that has an unusually large effect on its ecosystem relative to its population size, and removing it can cause significant changes throughout the food web.',
   [('What is a keystone species?', ['An organism that has an unusually large effect on its ecosystem relative to its population size', 'The most numerous species in an ecosystem', 'A species that has no effect on its ecosystem', 'A species found only in captivity'], 0),
    ('What might happen to an ecosystem if a keystone species is removed?', ['Significant changes could occur throughout the food web', 'Nothing in the ecosystem would change at all', 'The ecosystem would automatically become more stable', 'Other species would be completely unaffected'], 0),
    ('Sea otters are often cited as a keystone species because they help control the population of which organism?', ['Sea urchins', 'Sharks', 'Whales', 'Seabirds'], 0),
    ('Why is population size not always a good indicator of a species importance to an ecosystem?', ['A species with a small population, like a keystone species, can still have a major impact on the ecosystem', 'Population size always determines a species importance', 'Every species has an identical effect on its ecosystem', 'Ecosystems never depend on any single species'], 0),
    ('Why do conservationists pay special attention to protecting keystone species?', ['Protecting them can help maintain the balance and health of an entire ecosystem', 'Keystone species have no real impact on conservation efforts', 'Protecting a keystone species only affects that one species', 'Keystone species are always the largest animals in an ecosystem'], 0)]),
SS('Social Studies: The St. Lawrence Seaway — A Vital Trade Route',
   'Grade 6 Social Studies strand: the St. Lawrence Seaway is a system of canals and locks that allows large ships to travel between the Atlantic Ocean and the Great Lakes, supporting trade and transportation for Canada and the United States.',
   [('What does the St. Lawrence Seaway allow large ships to do?', ['Travel between the Atlantic Ocean and the Great Lakes', 'Travel underground through tunnels', 'Cross the Pacific Ocean directly', 'Fly between two countries'], 0),
    ('What structures help ships navigate changes in water level along the Seaway?', ['Locks', 'Bridges only', 'Tunnels', 'Dams built only for flood control'], 0),
    ('Which two countries share and jointly manage the St. Lawrence Seaway?', ['Canada and the United States', 'Canada and Mexico', 'Canada and the United Kingdom', 'The United States and Mexico'], 0),
    ('Why is the St. Lawrence Seaway considered important for trade?', ['It allows goods to be shipped efficiently between inland regions and international markets', 'It has no connection to trade or shipping', 'It only allows small recreational boats to pass through', 'It blocks all shipping between the two countries'], 0),
    ('Why might a system of locks be necessary along a waterway like the St. Lawrence Seaway?', ['Locks raise or lower ships to match different water levels along the route', 'Locks have no function related to water levels', 'Locks are used only to collect tolls from ships', 'Locks prevent any ships from passing through at all'], 0)]),
]),
day(125, [
L('Vocabulary: Portmanteau Words and Blends',
  'Grade 6 Language strand: a portmanteau, or blend, is a word formed by combining parts of two other words into one, such as brunch from breakfast and lunch, to create a new meaning.',
  [('What is a portmanteau word?', ['A word formed by combining parts of two other words', 'A word with only one syllable', 'A word borrowed directly from another language with no change', 'A word with no meaning at all'], 0),
   ('Which word is an example of a portmanteau?', ['Brunch', 'Table', 'Quickly', 'Happy'], 0),
   ('What two words combine to form the portmanteau brunch?', ['Breakfast and lunch', 'Bread and lunch', 'Break and munch', 'Brew and lunch'], 0),
   ('What two words combine to form the portmanteau smog?', ['Smoke and fog', 'Small and dog', 'Smooth and log', 'Smile and jog'], 0),
   ('Why do new portmanteau words sometimes appear as technology and culture change?', ['Speakers often blend existing words to quickly name new ideas or inventions', 'Portmanteau words are never created for new ideas', 'Language never changes to reflect new inventions', 'New words can only be created by combining entire sentences'], 0)]),
M('Number Sense: Converting Fractions to Repeating and Terminating Decimals',
  'Grade 6 Math strand: when a fraction is converted to a decimal by dividing the numerator by the denominator, the result either terminates, ending after a certain number of digits, or repeats a digit pattern forever.',
  [('What is a terminating decimal?', ['A decimal that ends after a certain number of digits', 'A decimal that repeats forever', 'A decimal with no digits after the decimal point', 'A decimal that is always a whole number'], 0),
   ('What is a repeating decimal?', ['A decimal in which one or more digits repeat forever', 'A decimal that always ends after two digits', 'A decimal with no fractional part', 'A decimal that can never be written as a fraction'], 0),
   ('What is 1/4 written as a decimal?', ['0.25', '0.4', '0.14', '0.33'], 0),
   ('What is 1/3 written as a decimal?', ['0.333... (repeating)', '0.3 (terminating)', '0.13', '0.03'], 0),
   ('How can you convert any fraction into a decimal?', ['Divide the numerator by the denominator', 'Multiply the numerator by the denominator', 'Add the numerator and denominator together', 'Subtract the denominator from the numerator'], 0)]),
Sc('Pulleys — A Simple Machine for Lifting',
   'Grade 6 Science strand: a pulley is a simple machine made of a wheel and a rope or cable, used to change the direction of a force or to make lifting heavy objects easier, especially when combined into a system of multiple pulleys.',
   [('What is a pulley?', ['A simple machine made of a wheel and a rope or cable', 'A machine made entirely of gears', 'A tool used only for cutting materials', 'A device with no moving parts'], 0),
    ('What is one common use of a pulley?', ['Making it easier to lift heavy objects', 'Measuring temperature', 'Generating electricity from sunlight', 'Cutting through solid rock'], 0),
    ('How can a pulley system change the direction of a force?', ['Pulling down on one end of the rope can lift an object upward on the other end', 'A pulley can never change the direction of a force', 'Pulleys only work if the force pushes upward', 'Pulleys eliminate the need for any force at all'], 0),
    ('What happens when multiple pulleys are combined into a system?', ['The effort needed to lift a heavy load can be reduced', 'The load always becomes impossible to lift', 'Extra pulleys always increase the effort required', 'Combining pulleys has no effect on lifting objects'], 0),
    ('Which everyday object commonly uses a pulley system?', ['A flagpole', 'A wooden ramp', 'A pair of scissors', 'A doorknob'], 0)]),
SS('Social Studies: The Komagata Maru Incident',
   'Grade 6 Social Studies strand: in 1914, the ship Komagata Maru arrived in Vancouver carrying passengers from India who were denied entry to Canada under discriminatory immigration laws of the time, an event now recognized as an injustice in Canadian history.',
   [('What was the Komagata Maru?', ['A ship carrying passengers from India that arrived in Vancouver in 1914', 'A Canadian warship built in the 1800s', 'A modern cruise ship', 'A type of Canadian currency'], 0),
    ('What happened to most of the passengers aboard the Komagata Maru?', ['They were denied entry to Canada under discriminatory immigration laws', 'They were welcomed immediately with no restrictions', 'They were granted full Canadian citizenship on arrival', 'They never actually reached Canada by ship'], 0),
    ('In what year did the Komagata Maru incident take place?', ['1914', '1867', '1970', '1945'], 0),
    ('Why is the Komagata Maru incident now studied as an example of historical injustice?', ['It reflects discriminatory immigration policies that unfairly excluded people based on their origin', 'It has no connection to immigration history', 'The event demonstrates fair and equal treatment of all passengers', 'The incident was entirely fictional and never occurred'], 0),
    ('Why might learning about events like the Komagata Maru incident be valuable for understanding Canadian history today?', ['It helps Canadians understand past injustices and how immigration policy has changed over time', 'This event has no relevance to modern Canadian society', 'Immigration policy in Canada has never changed since 1914', 'Historical injustices have no connection to present-day understanding'], 0)]),
]),
day(126, [
L('Media Literacy: Evaluating Online Product Reviews and Testimonials',
  'Grade 6 Language strand: online product reviews and testimonials can be genuine or misleading, so readers should consider the reviewers credibility, look for detailed and specific feedback, and watch for signs of fake or paid reviews.',
  [('What should readers consider when evaluating an online product review?', ['The reviewers credibility and how detailed the feedback is', 'Only the star rating and nothing else', 'Whether the review uses capital letters', 'The colour of the product shown in the review'], 0),
   ('What is a warning sign that a review might be fake?', ['Vague praise with no specific details about the product', 'A review that describes both strengths and weaknesses', 'A review written by someone who used the product', 'A review with a moderate, balanced rating'], 0),
   ('Why might a company pay for positive reviews?', ['To make their product appear more trustworthy or popular than it really is', 'Paid reviews are always required by law', 'Companies never have any influence over online reviews', 'Positive reviews have no effect on sales'], 0),
   ('Why is it useful to read several reviews instead of just one before making a decision?', ['Reading multiple reviews gives a more balanced and reliable picture of a product', 'A single review always tells the whole truth', 'Reading more reviews never changes ones understanding of a product', 'Reviews are never useful when making decisions'], 0),
   ('Which detail in a review would most likely indicate it is genuine?', ['A specific description of how the product performed over time', 'A generic comment with no details, such as great product', 'An unusually large number of identical five-star reviews posted the same day', 'A review posted before the product was ever released'], 0)]),
M('Algebra: Translating Word Problems into Algebraic Expressions',
  'Grade 6 Math strand: translating a word problem into an algebraic expression means identifying an unknown quantity, assigning it a variable, and using mathematical operations to represent the relationships described in words.',
  [('What is the first step in translating a word problem into an algebraic expression?', ['Identifying the unknown quantity and assigning it a variable', 'Immediately solving for a numerical answer', 'Ignoring any numbers mentioned in the problem', 'Rewriting the problem without any numbers'], 0),
   ('Which expression represents five more than a number n?', ['n + 5', '5n', 'n - 5', '5/n'], 0),
   ('Which expression represents three times a number x, decreased by two?', ['3x - 2', '3x + 2', '2x - 3', 'x - 3 x 2'], 0),
   ('If a word problem says a number divided by four equals twelve, which equation represents this?', ['n / 4 = 12', '4n = 12', 'n + 4 = 12', 'n - 4 = 12'], 0),
   ('Why is translating word problems into algebraic expressions a useful skill?', ['It allows real-world situations to be represented and solved using mathematical tools', 'It removes the need to understand the original word problem', 'Word problems can never be represented using variables', 'This skill has no connection to solving real problems'], 0)]),
Sc('Metamorphosis — Life Cycles of Insects and Amphibians',
   'Grade 6 Science strand: metamorphosis is a process in which an animal undergoes dramatic physical changes as it develops, seen in insects like butterflies, which pass through egg, larva, pupa, and adult stages, and in amphibians like frogs.',
   [('What is metamorphosis?', ['A process in which an animal undergoes dramatic physical changes as it develops', 'A process in which an animal never changes throughout its life', 'A type of hibernation', 'A process found only in plants'], 0),
    ('What are the four stages of complete metamorphosis in a butterfly?', ['Egg, larva, pupa, adult', 'Egg, adult, larva, pupa', 'Larva, egg, adult, pupa', 'Pupa, larva, adult, egg'], 0),
    ('What is a caterpillar an example of in a butterflys life cycle?', ['The larva stage', 'The pupa stage', 'The adult stage', 'The egg stage'], 0),
    ('How does a tadpole change as it undergoes metamorphosis into an adult frog?', ['It develops legs and lungs while losing its tail and gills', 'It stays exactly the same throughout its entire life', 'It develops wings and flies away', 'It shrinks back into an egg'], 0),
    ('Why might metamorphosis be an advantage for a species survival?', ['Different life stages can use different food sources and habitats, reducing competition', 'Metamorphosis has no benefit for a species', 'All life stages of a species always compete for the same resources', 'Species that undergo metamorphosis cannot adapt to their environment'], 0)]),
SS('Social Studies: The Avro Arrow — A Canadian Aviation Story',
   'Grade 6 Social Studies strand: the Avro Arrow was an advanced Canadian-designed fighter jet developed in the 1950s, celebrated for its innovative engineering, but the program was cancelled in 1959, a decision that remains a debated moment in Canadian history.',
   [('What was the Avro Arrow?', ['An advanced Canadian-designed fighter jet', 'A type of Canadian passenger train', 'A famous Canadian ship', 'A Canadian currency design'], 0),
    ('In what decade was the Avro Arrow developed?', ['The 1950s', 'The 1800s', 'The 1990s', 'The 1700s'], 0),
    ('What happened to the Avro Arrow program in 1959?', ['It was cancelled', 'It was expanded into a worldwide fleet', 'It won an international design award and continued for decades', 'It was renamed but never changed'], 0),
    ('Why is the cancellation of the Avro Arrow still debated by historians today?', ['People disagree about whether the decision was the right economic and strategic choice', 'No one has ever discussed the cancellation since it happened', 'The cancellation had no effect on the Canadian aviation industry', 'The program was never actually cancelled'], 0),
    ('Why was the Avro Arrow considered an impressive engineering achievement for its time?', ['It featured advanced design and technology that was innovative for the era', 'It was built using outdated technology with no innovation', 'It had no unique design features compared to other aircraft', 'It was the slowest aircraft ever built in Canada'], 0)]),
]),
day(127, [
L('Oral Communication: Impromptu Speaking',
  'Grade 6 Language strand: impromptu speaking means speaking on a topic with little or no advance preparation, requiring a speaker to quickly organize their thoughts into a clear beginning, middle, and end.',
  [('What is impromptu speaking?', ['Speaking on a topic with little or no advance preparation', 'Reading a fully written speech word for word', 'Speaking only after weeks of preparation', 'A type of written essay'], 0),
   ('What is a helpful strategy for organizing thoughts quickly during an impromptu speech?', ['Mentally outlining a beginning, middle, and end before speaking', 'Speaking as fast as possible with no structure', 'Avoiding eye contact with the audience', 'Refusing to speak until fully prepared'], 0),
   ('Why might impromptu speaking feel more challenging than a prepared speech?', ['There is little time to plan exactly what to say', 'Impromptu speeches are always written down first', 'Impromptu speaking requires no thinking at all', 'Prepared speeches are always shorter than impromptu ones'], 0),
   ('Which situation is an example of impromptu speaking?', ['Answering an unexpected question from a classmate during a group discussion', 'Reading a memorized poem after months of practice', 'Presenting a slideshow prepared over several weeks', 'Reciting a speech from a printed script'], 0),
   ('Why is practising impromptu speaking a useful skill in everyday life?', ['People often need to respond thoughtfully to unexpected questions or situations', 'Unexpected situations never require clear communication', 'This skill has no real-world application', 'Impromptu speaking is only useful in formal debates'], 0)]),
M('Data Management: Calculating Weighted Averages',
  'Grade 6 Math strand: a weighted average gives different values different levels of importance before averaging, multiplying each value by its weight, adding the results, and dividing by the total of the weights.',
  [('What does a weighted average take into account that a simple average does not?', ['The different levels of importance, or weight, given to each value', 'Only the largest value in a data set', 'Only the smallest value in a data set', 'Nothing different from a simple average'], 0),
   ('How is a weighted average calculated?', ['Multiply each value by its weight, add the results, then divide by the total weight', 'Add all values together and divide by the number of values only', 'Subtract the smallest value from the largest value', 'Multiply all the values together'], 0),
   ('If a test is worth twice as much as a quiz, how is the test treated when calculating a weighted average grade?', ['It counts twice as much as the quiz toward the final average', 'It counts exactly the same as the quiz', 'It is not included in the average at all', 'It always lowers the final average'], 0),
   ('Why might a teacher use weighted averages to calculate a students final grade?', ['Some assignments, like exams, may be more significant than others, like small quizzes', 'All assignments must always count exactly the same amount', 'Weighted averages are never used in real grading systems', 'Weighted averages remove the need to grade individual assignments'], 0),
   ('In a weighted average, what happens to a value with a very high weight?', ['It has a greater influence on the overall average', 'It has no influence on the overall average', 'It is automatically excluded from the calculation', 'It always lowers the final result'], 0)]),
Sc('Bioaccumulation in Food Chains',
   'Grade 6 Science strand: bioaccumulation occurs when harmful substances, such as certain pollutants, build up in an organisms body over time and become more concentrated at each higher level of a food chain, a process called biomagnification.',
   [('What is bioaccumulation?', ['The buildup of harmful substances in an organisms body over time', 'The rapid removal of pollutants from an ecosystem', 'A process that only affects plants', 'A process with no connection to food chains'], 0),
    ('What is biomagnification?', ['The increasing concentration of harmful substances at each higher level of a food chain', 'A decrease in pollutant levels as they move up a food chain', 'A process unrelated to bioaccumulation', 'The process of removing toxins from water'], 0),
    ('Why do top predators in a food chain often have the highest concentrations of accumulated toxins?', ['They consume many organisms that have each already accumulated some of the toxin', 'Top predators never consume other organisms', 'Toxins disappear completely as they move up a food chain', 'Top predators are immune to all toxins'], 0),
    ('Which of these is an example of a substance that can bioaccumulate in ecosystems?', ['Certain industrial pollutants and pesticides', 'Pure oxygen', 'Rainwater with no contaminants', 'Ordinary table salt in tiny amounts'], 0),
    ('Why is understanding bioaccumulation important for protecting both wildlife and human health?', ['Substances that build up in animals can eventually affect the humans who eat them', 'Bioaccumulation has no connection to human health', 'Toxins never move between different species', 'Only the smallest organisms in a food chain are affected by toxins'], 0)]),
SS('Social Studies: The Halifax Explosion',
   'Grade 6 Social Studies strand: the Halifax Explosion of 1917 occurred when two ships collided in Halifax Harbour, one carrying wartime explosives, causing a massive blast that devastated the city and remains one of the largest human-made explosions in history before nuclear weapons.',
   [('What caused the Halifax Explosion?', ['A collision between two ships, one carrying wartime explosives', 'A volcanic eruption near the city', 'A severe earthquake', 'An accidental fire in a forest'], 0),
    ('In what year did the Halifax Explosion occur?', ['1917', '1867', '1945', '1929'], 0),
    ('What effect did the explosion have on the city of Halifax?', ['It caused massive destruction and loss of life throughout the city', 'It had no impact on the city at all', 'It only affected ships far out at sea', 'It improved the citys infrastructure immediately'], 0),
    ('Why is the Halifax Explosion historically significant beyond Nova Scotia?', ['It was one of the largest human-made explosions in history before nuclear weapons', 'It had no significance beyond the local area', 'It was a minor and quickly forgotten event', 'It only affected a small number of buildings'], 0),
    ('Why might studying disasters like the Halifax Explosion help communities today?', ['Understanding past disasters can inform better safety practices and emergency planning', 'Past disasters have no connection to modern safety planning', 'Studying history never helps with emergency preparedness', 'The event has no lessons relevant to todays communities'], 0)]),
]),
day(128, [
L('Reading: Understanding Analogies',
  'Grade 6 Language strand: an analogy compares the relationship between one pair of words to the relationship between another pair, helping readers recognize patterns such as cause and effect, part to whole, or synonym relationships.',
  [('What does an analogy compare?', ['The relationship between one pair of words and the relationship between another pair', 'Only the spelling of two words', 'The length of two sentences', 'The punctuation used in two different texts'], 0),
   ('In the analogy bird is to nest as bee is to ___, which word best completes it?', ['hive', 'honey', 'flower', 'sting'], 0),
   ('What type of relationship does the analogy happy is to sad as fast is to slow show?', ['Opposite, or antonym, relationship', 'Synonym relationship', 'Part to whole relationship', 'Cause and effect relationship'], 0),
   ('Why are analogies useful for building vocabulary?', ['They help readers see how word meanings and relationships connect to one another', 'Analogies never involve word meanings', 'Analogies are only used in mathematics', 'Analogies replace the need to learn new words'], 0),
   ('In the analogy finger is to hand as toe is to ___, which word best completes it?', ['foot', 'shoe', 'leg', 'nail'], 0)]),
M('Data Management: Cumulative Frequency Tables and Graphs',
  'Grade 6 Math strand: a cumulative frequency table shows the running total of frequencies as data values increase, and this running total can be graphed to show how data accumulates across a range of values.',
  [('What does a cumulative frequency table show?', ['The running total of frequencies as data values increase', 'Only the single most common data value', 'The average of all data values', 'A list of data values with no totals'], 0),
   ('If 5 students scored below 60 and 8 more scored between 60 and 70, what is the cumulative frequency up to 70?', ['13', '8', '5', '3'], 0),
   ('As you move down a cumulative frequency table, what happens to the running total?', ['It stays the same or increases, but never decreases', 'It always decreases', 'It resets to zero at each row', 'It has no consistent pattern'], 0),
   ('What shape does a cumulative frequency graph typically have?', ['A curve or line that steadily rises from left to right', 'A straight horizontal line', 'A line that always decreases', 'A series of unconnected points with no pattern'], 0),
   ('Why might a cumulative frequency graph be useful for finding the median of a data set?', ['It can show the point where half the total data has accumulated', 'It has no connection to finding the median', 'It only shows the smallest value in the data', 'Median values cannot be estimated using graphs'], 0)]),
Sc('Geothermal Energy — Heat from the Earth',
   'Grade 6 Science strand: geothermal energy is a renewable energy source that harnesses heat from deep within the Earth, often used to generate electricity or heat buildings directly in regions with accessible underground heat.',
   [('What is geothermal energy?', ['A renewable energy source that harnesses heat from within the Earth', 'Energy generated by burning fossil fuels', 'Energy captured only from sunlight', 'A type of energy that cannot be renewed'], 0),
    ('Where does the heat used in geothermal energy come from?', ['Deep within the Earth', 'The surface of the ocean', 'Wind currents high in the atmosphere', 'Burning coal underground'], 0),
    ('How can geothermal energy be used to generate electricity?', ['Heat from underground can produce steam that turns turbines connected to generators', 'Geothermal energy cannot be converted into electricity', 'It requires burning fuel to create electricity', 'It only works when the sun is shining'], 0),
    ('Why is geothermal energy considered a renewable energy source?', ['The heat from the Earths interior is continuously produced and does not run out on a human timescale', 'Geothermal energy is a finite resource that will run out very soon', 'Renewable energy sources always come from the sun only', 'Geothermal energy is created entirely by human activity'], 0),
    ('Why might geothermal energy be more practical in some regions of the world than others?', ['Accessible underground heat is more available in certain geologically active areas', 'Geothermal energy is equally available everywhere on Earth', 'Geothermal energy has no connection to geography', 'Every region of the world has identical access to underground heat'], 0)]),
SS('Social Studies: Canadas National Sport — Lacrosse and Hockey',
   'Grade 6 Social Studies strand: lacrosse, originally developed by Indigenous peoples, is legally recognized as Canadas national summer sport, while ice hockey, deeply woven into Canadian culture, is recognized as the national winter sport.',
   [('Which sport was originally developed by Indigenous peoples in North America?', ['Lacrosse', 'Ice hockey', 'Basketball', 'Soccer'], 0),
    ('What is Canadas legally recognized national summer sport?', ['Lacrosse', 'Ice hockey', 'Baseball', 'Tennis'], 0),
    ('What is Canadas legally recognized national winter sport?', ['Ice hockey', 'Lacrosse', 'Skiing', 'Curling'], 0),
    ('Why is lacrosse considered an important part of Indigenous culture and history?', ['It originated among Indigenous peoples and holds deep cultural and spiritual significance', 'Lacrosse has no connection to Indigenous history', 'It was invented entirely in modern times with no historical roots', 'Lacrosse has never been played by Indigenous peoples'], 0),
    ('Why might having two officially recognized national sports reflect aspects of Canadian identity and geography?', ['Canadas seasonal climate and diverse history are reflected in a summer and a winter national sport', 'National sports have no connection to a countrys climate or history', 'Every country has exactly two national sports for the same reasons', 'The choice of national sports was made with no consideration of Canadian culture'], 0)]),
]),
day(129, [
L('Reading: Making Text-to-Self, Text-to-Text, and Text-to-World Connections',
  'Grade 6 Language strand: readers deepen comprehension by making connections, relating a text to their own experiences (text-to-self), to other texts they have read (text-to-text), or to events and issues beyond the text (text-to-world).',
  [('What is a text-to-self connection?', ['Relating a text to ones own experiences', 'Comparing two different books', 'Connecting a text to a historical event', 'Ignoring personal experience while reading'], 0),
   ('What is a text-to-text connection?', ['Relating a text to another text a reader has read', 'Relating a text only to personal memories', 'Relating a text to a current news event', 'Reading a text without making any comparisons'], 0),
   ('What is a text-to-world connection?', ['Relating a text to events or issues beyond the text, such as in the wider world', 'Relating a text only to the readers own life', 'Relating a text only to a single other book', 'Ignoring the broader context of a text entirely'], 0),
   ('If a reader remembers a similar personal experience while reading a story about moving to a new school, what type of connection is this?', ['Text-to-self', 'Text-to-text', 'Text-to-world', 'Not a connection at all'], 0),
   ('Why do these types of connections help deepen reading comprehension?', ['They help readers relate new information to what they already know, making the text more meaningful', 'Connections always distract readers from the main text', 'Making connections has no effect on understanding', 'Only text-to-text connections are useful for comprehension'], 0)]),
M('Number Sense: Reading and Writing Large Numbers in the Millions and Billions',
  'Grade 6 Math strand: large numbers in the millions and billions are read and written using place value groups separated by commas, helping students make sense of quantities like populations, distances, and budgets.',
  [('In the number 3,254,000, what place value does the digit 3 represent?', ['Millions', 'Thousands', 'Hundreds', 'Tens'], 0),
   ('How many zeros follow the 1 in one billion when written as a numeral?', ['Nine', 'Six', 'Three', 'Twelve'], 0),
   ('Which number is written correctly using commas to separate place value groups?', ['4,500,000', '4500,000', '45,00,000', '4500000,'], 0),
   ('Why might understanding large numbers like millions and billions be useful when reading news about population or government budgets?', ['It helps readers make sense of the true scale of these quantities', 'Large numbers never appear in real-world contexts', 'Millions and billions are always treated as the same value', 'Understanding place value has no connection to real-world numbers'], 0),
   ('Which number is greater: 750 million or 1.2 billion?', ['1.2 billion', '750 million', 'They are equal', 'It cannot be determined'], 0)]),
Sc('Watersheds and Drainage Basins',
   'Grade 6 Science strand: a watershed, or drainage basin, is an area of land where all the surface water, from rain and melting snow, drains into a common river, lake, or other body of water.',
   [('What is a watershed?', ['An area of land where all surface water drains into a common body of water', 'A device used to measure rainfall', 'A type of underground cave system', 'A body of water with no connection to surrounding land'], 0),
    ('What are the two main sources of water that flow into a watershed?', ['Rain and melting snow', 'Ocean currents and tides', 'Underground mining and drilling', 'Industrial waste and sewage only'], 0),
    ('Where does water within a watershed eventually drain to?', ['A common river, lake, or other body of water', 'Directly into outer space', 'It never moves anywhere', 'Only into the soil, with no further movement'], 0),
    ('Why might pollution entering a watershed in one location affect communities far downstream?', ['Water carries pollutants as it flows through the watershed toward a common body of water', 'Pollution never spreads beyond its original location', 'Watersheds have no connection between different locations', 'Downstream communities are never affected by upstream events'], 0),
    ('Why is protecting a watershed considered important for both ecosystems and human communities?', ['Many people and wildlife depend on the same water sources within a watershed', 'Watersheds have no impact on either ecosystems or communities', 'Protecting a watershed only benefits a single organism', 'Watersheds are unrelated to drinking water supplies'], 0)]),
SS('Social Studies: The Canadian Pacific Railway and Nation-Building',
   'Grade 6 Social Studies strand: the Canadian Pacific Railway, completed in 1885, connected the country from coast to coast, fulfilling a promise made to British Columbia and playing a major role in Canadian settlement, trade, and national unity.',
   [('What did the completion of the Canadian Pacific Railway achieve?', ['It connected the country from coast to coast', 'It connected Canada to another continent by land', 'It replaced all water-based transportation in Canada', 'It had no effect on transportation in Canada'], 0),
    ('In what year was the Canadian Pacific Railway completed?', ['1885', '1867', '1929', '1945'], 0),
    ('What promise to a Canadian province motivated the building of the railway?', ['A promise made to British Columbia to join Confederation', 'A promise made to Newfoundland before it joined Canada', 'A promise involving Quebec sovereignty', 'No promise was involved in building the railway'], 0),
    ('Why is the Canadian Pacific Railway often described as playing a major role in nation-building?', ['It helped unify the country by enabling trade, settlement, and transportation across vast distances', 'It had no effect on how the country developed', 'It only connected two neighbouring cities', 'It discouraged settlement and trade across Canada'], 0),
    ('Why might building a railway across Canadas varied landscape, including the Rocky Mountains, have been a significant challenge?', ['Workers had to overcome difficult and diverse terrain across a vast distance', 'Canadas landscape is completely flat from coast to coast', 'Railways never need to account for geography', 'The railway was built entirely underground to avoid geography'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Poetic Forms, and Reading Strategies',
  'Grade 6 Language strand review: students revisit subject-verb agreement, comparative and superlative adjectives, limericks, eulogies, portmanteau words, online reviews, impromptu speaking, analogies, and reading connections.',
  [('What does subject-verb agreement require?', ['A verb that matches its subject in number', 'A verb that always ends in s', 'A subject placed after the verb', 'A sentence with no verb at all'], 0),
   ('How many lines does a limerick have?', ['Five', 'Three', 'Seven', 'Ten'], 0),
   ('What is a portmanteau word?', ['A word formed by combining parts of two other words', 'A word with only one syllable', 'A word borrowed directly from another language with no change', 'A word with no meaning at all'], 0),
   ('What does an analogy compare?', ['The relationship between one pair of words and the relationship between another pair', 'Only the spelling of two words', 'The length of two sentences', 'The punctuation used in two different texts'], 0),
   ('What is a text-to-self connection?', ['Relating a text to ones own experiences', 'Comparing two different books', 'Connecting a text to a historical event', 'Ignoring personal experience while reading'], 0)]),
M('Math Review: Number Sense, Geometry, and Data Management',
  'Grade 6 Math strand review: students revisit scientific notation, the sum of interior angles in polygons, the volume of a sphere, translating word problems into expressions, and weighted averages.',
  [('What does scientific notation help express?', ['Very large or very small numbers in a compact form', 'Only numbers between 0 and 1', 'Fractions with large denominators only', 'Numbers that have no decimal point'], 0),
   ('What formula finds the sum of the interior angles of a polygon with n sides?', ['(n minus 2) times 180 degrees', 'n times 90 degrees', 'n times 180 degrees', '(n plus 2) times 180 degrees'], 0),
   ('What formula is used to find the volume of a sphere?', ['Four-thirds times pi times the radius cubed', 'Four times pi times the radius squared', 'Pi times the radius squared times the height', 'Two-thirds times pi times the radius cubed'], 0),
   ('Which expression represents five more than a number n?', ['n + 5', '5n', 'n - 5', '5/n'], 0),
   ('What does a weighted average take into account that a simple average does not?', ['The different levels of importance, or weight, given to each value', 'Only the largest value in a data set', 'Only the smallest value in a data set', 'Nothing different from a simple average'], 0)]),
Sc('Science Review: Energy, Space, and Ecosystems',
   'Grade 6 Science strand review: students revisit kinetic and potential energy, comets, asteroids, and meteors, keystone species, insect and amphibian metamorphosis, and watersheds.',
   [('What is kinetic energy?', ['The energy of motion', 'Stored energy based on position', 'Energy that never changes form', 'A type of chemical reaction'], 0),
    ('What is a comet mostly made of?', ['Ice and dust', 'Solid metal only', 'Liquid water only', 'Pure rock with no ice'], 0),
    ('What is a keystone species?', ['An organism that has an unusually large effect on its ecosystem relative to its population size', 'The most numerous species in an ecosystem', 'A species that has no effect on its ecosystem', 'A species found only in captivity'], 0),
    ('What is metamorphosis?', ['A process in which an animal undergoes dramatic physical changes as it develops', 'A process in which an animal never changes throughout its life', 'A type of hibernation', 'A process found only in plants'], 0),
    ('What is a watershed?', ['An area of land where all surface water drains into a common body of water', 'A device used to measure rainfall', 'A type of underground cave system', 'A body of water with no connection to surrounding land'], 0)]),
SS('Social Studies Review: Canadian History, Identity, and Institutions',
   'Grade 6 Social Studies strand review: students revisit Canadian national symbols, the Persons Case, the St. Lawrence Seaway, the Avro Arrow, and the Canadian Pacific Railway.',
   [('What image appears on the Canadian flag?', ['A red maple leaf', 'A golden eagle', 'A blue star', 'A green shamrock'], 0),
    ('What did the Persons Case establish?', ['That women are legally recognized as persons under Canadian law', 'That only men could serve in government', 'A new set of provincial boundaries', 'A change to Canadas national currency'], 0),
    ('What does the St. Lawrence Seaway allow large ships to do?', ['Travel between the Atlantic Ocean and the Great Lakes', 'Travel underground through tunnels', 'Cross the Pacific Ocean directly', 'Fly between two countries'], 0),
    ('What was the Avro Arrow?', ['An advanced Canadian-designed fighter jet', 'A type of Canadian passenger train', 'A famous Canadian ship', 'A Canadian currency design'], 0),
    ('What did the completion of the Canadian Pacific Railway achieve?', ['It connected the country from coast to coast', 'It connected Canada to another continent by land', 'It replaced all water-based transportation in Canada', 'It had no effect on transportation in Canada'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_121_130)
    append_to(6, g6_121_130)
