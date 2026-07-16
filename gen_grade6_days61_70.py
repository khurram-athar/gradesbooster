#!/usr/bin/env python3
"""Phase 3 extension: Grade 6, Days 61-70 (continuing past the Day 60
milestone reached in gen_grade6_days51_60.py, toward the full 157-day
year). Topics chosen to avoid any overlap with the existing Day 1-60
set (see data/grade6.json): prepositional phrases and descriptive
writing through Canadian civics, decimal operations through
stem-and-leaf plots, animal adaptations through Earth's atmosphere,
and the Indus Valley Civilization through Canada's justice system.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science & Technology',
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


g6_61_70 = [
day(61, [
L('Grammar: Prepositional Phrases and Their Function',
  'Grade 6 Language strand: a prepositional phrase begins with a preposition and ends with a noun or pronoun, adding detail about location, time, or direction to a sentence.',
  [('A prepositional phrase begins with a preposition and ends with a ___.', ['Noun or pronoun', 'Verb only', 'A concept unrelated to prepositional phrases', 'Punctuation mark'], 0),
   ('Which of these is an example of a prepositional phrase?', ['Under the old bridge', 'Quickly ran away', 'A phrase unrelated to prepositional phrases', 'Happily singing'], 0),
   ('In the sentence “The cat slept on the warm windowsill,” which words form the prepositional phrase?', ['On the warm windowsill', 'The cat slept', 'A phrase unrelated to this sentence', 'Slept on the'], 0),
   ('Prepositional phrases often add detail about ___.', ['Location, time, or direction', 'The subject’s name only', 'A concept unrelated to prepositional phrases', 'Nothing at all, since they carry no meaning'], 0),
   ('Why might a writer use prepositional phrases in their sentences?', ['To add specific detail and make writing more descriptive', 'Prepositional phrases always make writing confusing', 'A reason unrelated to grammar', 'Prepositional phrases are never useful in writing'], 0)]),
M('Adding and Subtracting Decimals',
  'Grade 6 Math strand: adding and subtracting decimals uses the same place-value rules as whole numbers, so digits must be lined up by their decimal point before combining them.',
  [('To add or subtract decimals correctly, you must first ___.', ['Line up the decimal points so digits match by place value', 'Round every number to the nearest whole number first', 'A step unrelated to adding decimals', 'Ignore the decimal points completely'], 0),
   ('What is 4.25 + 3.6?', ['7.85', '7.61', 'A value unrelated to the calculation', '7.31'], 0),
   ('What is 9.7 - 2.35?', ['7.35', '7.45', 'A value unrelated to the calculation', '6.35'], 0),
   ('What is 12.08 + 5.9?', ['17.98', '17.08', 'A value unrelated to the calculation', '12.99'], 0),
   ('Why might a store use decimal addition and subtraction when handling money?', ['Prices and change are often expressed using decimals for dollars and cents', 'Money is never expressed using decimal numbers', 'A reason unrelated to decimals', 'Decimals are only used in scientific contexts, never in stores'], 0)]),
Sc('Animal Adaptations and Survival Strategies',
   'Grade 6 Science strand: an adaptation is a physical feature or behaviour that helps an organism survive and reproduce in its specific environment.',
   [('An adaptation is best described as ___.', ['A physical feature or behaviour that helps an organism survive in its environment', 'A random change with no effect on survival', 'A concept unrelated to adaptations', 'A feature that always harms an organism’s chances of survival'], 0),
    ('Which of these is an example of a physical adaptation?', ['A polar bear’s thick fur for insulation in cold climates', 'A behaviour with no connection to survival', 'A concept unrelated to physical adaptations', 'An animal’s name'], 0),
    ('Which of these is an example of a behavioural adaptation?', ['Birds migrating to a warmer climate for winter', 'A fixed physical feature like fur colour', 'A concept unrelated to behavioural adaptations', 'An adaptation with no connection to survival'], 0),
    ('Why might camouflage be considered a helpful adaptation for many animals?', ['It helps an animal avoid predators or sneak up on prey by blending into its surroundings', 'Camouflage has no effect on an animal’s survival', 'A reason unrelated to adaptations', 'Camouflage always makes an animal more visible to predators'], 0),
    ('Why do different environments often lead to different adaptations in similar species?', ['Each environment presents different challenges, so useful traits differ from place to place', 'All environments present exactly the same challenges', 'A reason unrelated to adaptations', 'Adaptations never relate to an organism’s environment'], 0)]),
SS('Ancient India: The Indus Valley Civilization',
   'Grade 6 Social Studies strand: the Indus Valley Civilization was one of the world’s earliest urban societies, known for its advanced city planning, trade networks, and still-undeciphered writing system.',
   [('The Indus Valley Civilization is known for its advanced ___.', ['City planning, including organized streets and drainage systems', 'Complete absence of any cities or towns', 'A concept unrelated to the Indus Valley Civilization', 'Reliance on hunting and gathering, with no settled towns'], 0),
    ('The Indus Valley Civilization developed along which river system?', ['The Indus River', 'The Nile River', 'A river unrelated to this civilization', 'The Amazon River'], 0),
    ('Which of these remains a mystery to historians studying the Indus Valley Civilization?', ['Its written script has not yet been fully deciphered', 'Historians know every detail about its writing system', 'A concept unrelated to the Indus Valley Civilization', 'The civilization left behind no archaeological evidence at all'], 0),
    ('Why is the Indus Valley Civilization often compared to Mesopotamia and Egypt?', ['All three were early civilizations that developed advanced societies along major rivers', 'These civilizations developed with no connection to rivers at all', 'A reason unrelated to ancient river civilizations', 'They existed on entirely different planets, with no shared characteristics'], 0),
    ('Why do historians consider the Indus Valley Civilization an important part of ancient world history?', ['It was one of the earliest large, organized urban societies, contributing to later civilizations', 'It had no influence on later societies', 'A reason unrelated to its historical significance', 'It existed for too short a time to be historically significant'], 0)])]),
day(62, [
L('Writing: Descriptive Writing — Using Sensory Detail and Imagery',
  'Grade 6 Language strand: descriptive writing uses sensory detail and imagery — appealing to sight, sound, smell, taste, and touch — to help readers vividly picture a scene.',
  [('Descriptive writing often appeals to the reader’s ___.', ['Five senses', 'Ability to solve math problems', 'A concept unrelated to descriptive writing', 'Knowledge of grammar rules only'], 0),
   ('Which sentence uses strong sensory detail?', ['The crisp autumn air smelled of woodsmoke and fallen leaves.', 'It was outside.', 'A sentence unrelated to sensory detail', 'The weather happened.'], 0),
   ('Imagery in writing is best described as ___.', ['Language that creates a vivid picture in the reader’s mind', 'A list of facts with no descriptive language', 'A concept unrelated to imagery', 'A type of punctuation mark'], 0),
   ('Why might a writer choose specific, descriptive words over vague, general ones?', ['Specific words help readers form a clearer, more vivid mental picture', 'Vague words always create a clearer picture than specific ones', 'A reason unrelated to descriptive writing', 'Specific words make writing harder to understand'], 0),
   ('Which of these appeals most directly to the sense of sound?', ['The thunder rumbled loudly across the valley.', 'The velvet fabric felt soft.', 'A sentence unrelated to the sense of sound', 'The lemon tasted sour.'], 0)]),
M('Nets of 3D Figures',
  'Grade 6 Math strand: a net is a two-dimensional pattern that can be folded to form a three-dimensional figure, helping visualize the faces that make up a solid.',
  [('A net is best described as ___.', ['A two-dimensional pattern that folds into a three-dimensional figure', 'A three-dimensional figure with no flat faces', 'A concept unrelated to nets', 'A type of graph used to display data'], 0),
   ('How many faces does the net of a cube have?', ['6', '4', 'A number unrelated to the net of a cube', '8'], 0),
   ('Which 3D figure is formed by a net made of one rectangle and two circles?', ['A cylinder', 'A cube', 'A figure unrelated to this net', 'A cone'], 0),
   ('The net of a triangular prism includes ___.', ['Two triangles and three rectangles', 'Six squares and no triangles', 'A description unrelated to this net', 'Only triangles, with no rectangles at all'], 0),
   ('Why are nets useful when studying 3D figures?', ['They help show how many faces a solid has and how those faces connect', 'Nets provide no useful information about a 3D figure', 'A reason unrelated to nets', 'Nets can only be used with cubes, never other solids'], 0)]),
Sc('The Moon: Phases, Eclipses, and Its Effect on Earth',
   'Grade 6 Science strand: the Moon’s phases result from its changing position relative to Earth and the Sun, and eclipses occur when the Sun, Earth, and Moon align in specific ways.',
   [('The Moon’s phases are caused by ___.', ['Its changing position relative to Earth and the Sun', 'The Moon changing shape physically each month', 'A concept unrelated to the Moon’s phases', 'The Moon disappearing and reforming every month'], 0),
    ('A solar eclipse occurs when ___.', ['The Moon passes between the Sun and Earth, blocking sunlight', 'Earth passes directly between the Sun and the Moon', 'A concept unrelated to eclipses', 'The Moon and Sun are on opposite sides of Earth'], 0),
    ('A lunar eclipse occurs when ___.', ['Earth passes between the Sun and the Moon, casting a shadow on the Moon', 'The Moon blocks sunlight from reaching Earth', 'A concept unrelated to eclipses', 'The Sun passes between Earth and the Moon'], 0),
    ('Which of these best describes a full moon?', ['The entire visible side of the Moon appears illuminated', 'No part of the Moon is visible at all', 'A concept unrelated to Moon phases', 'Only the Moon’s edge appears illuminated'], 0),
    ('Why does the Moon appear to change shape throughout the month, even though its own shape never changes?', ['We see different amounts of its sunlit side depending on its position in orbit', 'The Moon actually changes its physical shape each month', 'A reason unrelated to Moon phases', 'The Moon disappears completely between phases'], 0)]),
SS('West African Kingdoms: Mali, Ghana, and Songhai',
   'Grade 6 Social Studies strand: the West African kingdoms of Ghana, Mali, and Songhai grew wealthy and powerful through control of gold and salt trade routes across the Sahara.',
   [('The West African kingdoms of Ghana, Mali, and Songhai grew powerful largely through control of ___.', ['Gold and salt trade routes across the Sahara', 'Fishing rights along the Atlantic coast only', 'A concept unrelated to these kingdoms', 'Trade routes that had no connection to gold or salt'], 0),
    ('Which West African ruler is well known for a famous pilgrimage that showcased the kingdom’s vast wealth?', ['Mansa Musa of the Mali Empire', 'A ruler unrelated to West African history', 'A ruler of ancient Egypt', 'A ruler of the Byzantine Empire'], 0),
    ('Why were trans-Saharan trade routes important to these West African kingdoms?', ['They connected West Africa to North Africa and beyond, enabling valuable trade', 'These routes had no economic importance to West Africa', 'A reason unrelated to trade routes', 'The kingdoms refused to trade with any outside regions'], 0),
    ('The city of Timbuktu, part of the Mali Empire, became well known as a centre of ___.', ['Learning and trade', 'Isolation, with no connections to trade or scholarship', 'A concept unrelated to Timbuktu', 'Farming only, with no scholarly activity'], 0),
    ('Why is the history of these West African kingdoms an important part of world history?', ['It highlights sophisticated, wealthy societies that are often underrepresented in world history lessons', 'These kingdoms had no lasting historical significance', 'A reason unrelated to their historical importance', 'West Africa had no organized societies before European contact'], 0)])]),
day(63, [
L('Reading: Distinguishing Fact from Opinion',
  'Grade 6 Language strand: a fact can be proven true or false with evidence, while an opinion expresses a personal belief, feeling, or judgment that cannot be proven.',
  [('A fact is a statement that ___.', ['Can be proven true or false with evidence', 'Reflects only a personal belief or feeling', 'A concept unrelated to facts', 'Is always written in a persuasive tone'], 0),
   ('An opinion is a statement that ___.', ['Expresses a personal belief or judgment', 'Can always be proven true with evidence', 'A concept unrelated to opinions', 'Is identical in meaning to a fact'], 0),
   ('Which of these is a fact rather than an opinion?', ['Water freezes at zero degrees Celsius.', 'Winter is the best season of the year.', 'A statement unrelated to facts or opinions', 'Blue is the most beautiful colour.'], 0),
   ('Which of these is an opinion rather than a fact?', ['This is the most exciting movie ever made.', 'The movie is ninety minutes long.', 'A statement unrelated to facts or opinions', 'The movie was released in 2020.'], 0),
   ('Why is it important for readers to be able to distinguish fact from opinion?', ['It helps readers evaluate information critically and avoid being misled', 'Facts and opinions always carry exactly the same weight', 'A reason unrelated to reading comprehension', 'Distinguishing fact from opinion serves no useful purpose'], 0)]),
M('Classifying and Constructing Quadrilaterals',
  'Grade 6 Math strand: quadrilaterals are four-sided polygons classified by their side lengths, angles, and parallel sides, including squares, rectangles, rhombuses, trapezoids, and parallelograms.',
  [('A quadrilateral is a polygon with ___.', ['Exactly four sides', 'Exactly three sides', 'A concept unrelated to quadrilaterals', 'Exactly six sides'], 0),
   ('Which quadrilateral has exactly one pair of parallel sides?', ['A trapezoid', 'A square', 'A shape unrelated to quadrilaterals', 'A rhombus'], 0),
   ('A rhombus is a quadrilateral with ___.', ['Four equal sides', 'Only two equal sides', 'A description unrelated to a rhombus', 'No sides that are ever equal'], 0),
   ('Which of these is true of every rectangle?', ['It has four right angles', 'It always has four equal sides', 'A statement unrelated to rectangles', 'It never has any parallel sides'], 0),
   ('Why is it useful to classify quadrilaterals by their properties?', ['It helps identify shapes accurately and understand their relationships to one another', 'Classifying quadrilaterals provides no useful information', 'A reason unrelated to geometry', 'All quadrilaterals are identical, so classification is unnecessary'], 0)]),
Sc('Constellations and Navigating the Night Sky',
   'Grade 6 Science strand: a constellation is a recognizable pattern of stars that people have used for centuries to tell stories, mark seasons, and navigate.',
   [('A constellation is best described as ___.', ['A recognizable pattern of stars in the night sky', 'A single, extremely bright star', 'A concept unrelated to constellations', 'A type of planet found only in our solar system'], 0),
    ('Why have constellations historically been useful for navigation?', ['Their fixed patterns helped travellers determine direction, such as finding north', 'Constellations move randomly and provide no useful direction', 'A reason unrelated to constellations', 'Constellations are only visible during the daytime'], 0),
    ('Which constellation is well known for helping viewers locate the North Star?', ['The Big Dipper (part of Ursa Major)', 'A constellation unrelated to finding the North Star', 'The Southern Cross, visible mainly from the far Southern Hemisphere', 'A group of planets, not stars'], 0),
    ('Why do different constellations appear in the sky during different seasons?', ['Earth’s orbit around the Sun changes which part of the night sky faces away from the Sun', 'The stars themselves physically move to new locations each season', 'A reason unrelated to constellations', 'The same constellations are visible at exactly the same time every night of the year'], 0),
    ('Why might ancient civilizations have created stories about constellations?', ['To help explain, remember, and pass down knowledge about the patterns in the sky', 'Ancient civilizations had no interest in the night sky', 'A reason unrelated to constellations', 'Constellations were invented recently and have no historical stories attached'], 0)]),
SS('The Maya Civilization: Innovation and Society',
   'Grade 6 Social Studies strand: the Maya civilization, centred in present-day Mexico and Central America, developed advanced achievements in mathematics, astronomy, and writing.',
   [('The Maya civilization was centred in present-day ___.', ['Mexico and Central America', 'Northern Europe', 'A region unrelated to the Maya civilization', 'East Asia'], 0),
    ('Which of these was a notable achievement of the Maya civilization?', ['A sophisticated calendar system based on astronomical observation', 'A complete lack of any written language', 'A concept unrelated to Maya achievements', 'No knowledge of mathematics whatsoever'], 0),
    ('The Maya developed a mathematical system that notably included the concept of ___.', ['Zero', 'Negative decimals only', 'A concept unrelated to Maya mathematics', 'Fractions expressed only in Roman numerals'], 0),
    ('Maya cities often featured large stone structures such as ___.', ['Pyramids and temples', 'Skyscrapers made of steel', 'A structure unrelated to Maya architecture', 'Structures built entirely underground'], 0),
    ('Why do historians study the Maya civilization’s achievements in mathematics and astronomy?', ['They demonstrate a highly advanced understanding of science for their time', 'The Maya made no notable contributions to mathematics or astronomy', 'A reason unrelated to the Maya civilization', 'These achievements had no influence on how the Maya tracked time'], 0)])]),
day(64, [
L('Vocabulary: Prefixes, Suffixes, and Root Words',
  'Grade 6 Language strand: a root word carries a word’s core meaning, a prefix is added to the beginning to change that meaning, and a suffix is added to the end, often changing its part of speech.',
  [('A root word is best described as ___.', ['The part of a word that carries its core meaning', 'A word part added only to the end of a word', 'A concept unrelated to root words', 'A punctuation mark used in spelling'], 0),
   ('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'A position unrelated to prefixes', 'Middle, always splitting the word in half'], 0),
   ('A suffix is added to the ___ of a word.', ['End', 'Beginning', 'A position unrelated to suffixes', 'Middle, always splitting the word in half'], 0),
   ('In the word “unhappiness,” which part means “not”?', ['The prefix un-', 'The suffix -ness', 'A part unrelated to this word’s meaning', 'The root word happy'], 0),
   ('Why is it useful to recognize common prefixes and suffixes when reading?', ['It can help figure out the meaning of unfamiliar words', 'Prefixes and suffixes never affect a word’s meaning', 'A reason unrelated to vocabulary', 'Recognizing word parts makes reading more difficult'], 0)]),
M('Perimeter and Area of Composite 2D Shapes',
  'Grade 6 Math strand: a composite 2D shape is made of two or more simple shapes joined together, and finding its perimeter or area involves breaking it into familiar parts.',
  [('To find the area of a composite 2D shape, you generally ___.', ['Break it into simple shapes, find each area, and add them together', 'Multiply only the longest side by itself', 'A method unrelated to composite shapes', 'Ignore all but one part of the shape'], 0),
   ('If a composite shape is made of a rectangle with area 24 and a triangle with area 6, what is its total area?', ['30', '18', 'A value unrelated to the calculation', '144'], 0),
   ('The perimeter of a shape is the ___.', ['Total distance around its outer edge', 'Total space it covers inside its boundary', 'A concept unrelated to perimeter', 'Number of sides it has, regardless of length'], 0),
   ('A shape made of a square with side 5 and a rectangle attached has more sides than a simple square because ___.', ['Joining two shapes together adds additional edges to trace around', 'Joining shapes always removes edges from the total shape', 'A reason unrelated to composite shapes', 'Composite shapes always have exactly four sides'], 0),
   ('Why might an architect need to calculate the area of a composite-shaped room?', ['To know how much flooring or paint material will be needed to cover the space', 'Composite shapes have no real-world measurement applications', 'A reason unrelated to area', 'Area calculations are never needed for irregular shapes'], 0)]),
Sc('Gravity and Its Effects Throughout the Solar System',
   'Grade 6 Science strand: gravity is a force of attraction between objects with mass, and it is what keeps planets in orbit around the Sun and moons in orbit around planets.',
   [('Gravity is best described as ___.', ['A force of attraction between objects with mass', 'A force that pushes objects apart from one another', 'A concept unrelated to gravity', 'A type of light emitted by stars'], 0),
    ('What keeps the planets in orbit around the Sun?', ['The Sun’s gravitational pull', 'The complete absence of any force acting on the planets', 'A concept unrelated to orbits', 'Strong winds in space'], 0),
    ('Why do objects with more mass generally exert a stronger gravitational pull?', ['Gravity’s strength increases as the amount of mass increases', 'Gravity’s strength has no connection to an object’s mass', 'A reason unrelated to gravity', 'Objects with more mass always have weaker gravity'], 0),
    ('Why would an astronaut weigh less on the Moon than on Earth?', ['The Moon has less mass than Earth, so its gravitational pull is weaker', 'The Moon has a stronger gravitational pull than Earth', 'A reason unrelated to gravity', 'Gravity does not exist on the Moon at all'], 0),
    ('Why is gravity considered essential to the structure of the solar system?', ['It holds planets, moons, and other objects in consistent orbital paths', 'Gravity has no role in how the solar system is organized', 'A reason unrelated to gravity', 'Without gravity, orbits would remain exactly the same'], 0)]),
SS('The French Revolution: Causes and Impact',
   'Grade 6 Social Studies strand: the French Revolution began in 1789 as widespread inequality and financial crisis led citizens to overthrow the monarchy and reshape France’s government.',
   [('A major cause of the French Revolution was ___.', ['Widespread inequality and a financial crisis affecting the country', 'A period with no economic or social problems at all', 'A concept unrelated to the French Revolution', 'An agreement between all social classes with no conflict'], 0),
    ('The French Revolution began in the year ___.', ['1789', '1600', 'A year unrelated to the French Revolution', '1900'], 0),
    ('Which group faced the greatest hardship under France’s social and tax system before the revolution?', ['The common people, known as the Third Estate', 'The nobility, who paid the highest taxes', 'A group unrelated to French society at the time', 'The clergy, who faced the same burdens as commoners'], 0),
    ('One major outcome of the French Revolution was ___.', ['The overthrow of the monarchy and a reshaping of France’s government', 'The strengthening of the king’s absolute power', 'A concept unrelated to the French Revolution', 'No change to France’s system of government'], 0),
    ('Why is the French Revolution considered an important turning point in world history?', ['It challenged the idea of absolute monarchy and inspired ideas about rights and citizenship', 'It had no influence on political ideas beyond France', 'A reason unrelated to its historical significance', 'It only affected a small, isolated village with no wider impact'], 0)])]),
day(65, [
L('Writing: Structuring a Cause and Effect Essay',
  'Grade 6 Language strand: a cause and effect essay explains why something happened (the cause) and what resulted from it (the effect), often using clear transition words to show these relationships.',
  [('A cause and effect essay explains ___.', ['Why something happened and what resulted from it', 'Only a sequence of unrelated events', 'A concept unrelated to this essay type', 'A comparison between two unrelated topics'], 0),
   ('Which of these is an example of a transition word often used in cause and effect writing?', ['Therefore', 'Meanwhile', 'A word unrelated to cause and effect writing', 'Beside'], 0),
   ('In the sentence “Because the road was icy, the bus arrived late,” what is the effect?', ['The bus arrived late', 'The road was icy', 'A concept unrelated to this sentence', 'There is no effect described in this sentence'], 0),
   ('Why might a writer use a cause and effect structure when explaining a historical event?', ['It helps readers understand the reasons behind an event and its consequences', 'This structure makes historical events harder to understand', 'A reason unrelated to cause and effect writing', 'Cause and effect writing cannot be used to explain historical events'], 0),
   ('Which of these is a well-structured cause and effect statement?', ['Heavy rainfall caused the river to flood the nearby fields.', 'The river flooded and rain fell at the same random time.', 'A sentence unrelated to cause and effect writing', 'The fields were flooded, so heavy rainfall must be blue.'], 0)]),
M('Comparing and Ordering Rational Numbers',
  'Grade 6 Math strand: comparing and ordering rational numbers means placing integers, fractions, and decimals on a common number line to determine their relative size.',
  [('To compare a fraction and a decimal, it often helps to first ___.', ['Convert them to the same form, such as both as decimals', 'Ignore one of the two values completely', 'A step unrelated to comparing numbers', 'Round both numbers up to the nearest ten'], 0),
   ('Which of these is greater: -3 or -7?', ['-3', '-7', 'A value unrelated to the comparison', 'They are equal'], 0),
   ('Which is greater: 0.6 or 3/5?', ['They are equal', '0.6', 'A value unrelated to the comparison', '3/5'], 0),
   ('Which of these numbers is closest to zero on a number line?', ['-1', '-5', 'A value unrelated to the comparison', '5'], 0),
   ('Why is it useful to be able to order rational numbers that include fractions, decimals, and integers together?', ['It allows accurate comparisons in real situations that mix different number forms', 'Rational numbers can never be compared to one another', 'A reason unrelated to number sense', 'Only whole numbers can ever be placed on a number line'], 0)]),
Sc('Structures: Load, Force, and Stability in Design',
   'Grade 6 Science strand: engineers design structures to withstand different types of loads and forces, using shapes and materials that provide stability and strength.',
   [('In structural design, a load refers to ___.', ['A force or weight that a structure must support', 'A material used only for decoration', 'A concept unrelated to structures', 'The colour chosen for a structure’s exterior'], 0),
    ('Why do many strong structures, like bridges, use triangular shapes?', ['Triangles distribute force evenly and resist bending better than many other shapes', 'Triangles are only used for their appearance, with no structural benefit', 'A reason unrelated to structural design', 'Triangular shapes are always weaker than square shapes'], 0),
    ('A structure’s stability refers to its ability to ___.', ['Remain standing and resist tipping or collapsing under a load', 'Change shape constantly under the slightest force', 'A concept unrelated to stability', 'Move freely with no fixed base'], 0),
    ('Why might an engineer widen the base of a tall structure?', ['A wider base can improve stability and help prevent tipping', 'A wider base always makes a structure less stable', 'A reason unrelated to structural design', 'The width of a base has no effect on stability'], 0),
    ('Why is it important for engineers to consider both load and material strength when designing a structure?', ['A structure must support the forces acting on it without failing', 'Load and material strength have no connection to a structure’s safety', 'A reason unrelated to engineering', 'Structures never need to support any kind of force'], 0)]),
SS('The American Revolution and Its Impact on British North America',
   'Grade 6 Social Studies strand: the American Revolution (1775-1783) saw the Thirteen Colonies gain independence from Britain, an event that also shaped migration and politics in British North America, including present-day Canada.',
   [('The American Revolution resulted in the Thirteen Colonies gaining independence from ___.', ['Britain', 'France', 'A country unrelated to the American Revolution', 'Spain'], 0),
    ('Following the American Revolution, many Loyalists (colonists who remained loyal to Britain) moved to ___.', ['British North America, including present-day Canada', 'A region unrelated to Loyalist migration', 'The southern United States exclusively', 'Continental Europe'], 0),
    ('Why might the arrival of Loyalists have significantly shaped early Canadian communities?', ['They brought new populations, skills, and ideas that influenced how these communities developed', 'Loyalist migration had no effect on the communities they settled in', 'A reason unrelated to this migration', 'No Loyalists ever settled in British North America'], 0),
    ('The American Revolution took place between the years ___.', ['1775 and 1783', '1900 and 1910', 'A time period unrelated to the American Revolution', '1600 and 1610'], 0),
    ('Why is the American Revolution relevant to the study of Canadian history?', ['It influenced migration patterns and political developments in British North America', 'It had no connection to the history of British North America', 'A reason unrelated to Canadian history', 'Canada was entirely unaffected by events happening south of its border'], 0)])]),
day(66, [
L('Reading: Making and Confirming Predictions',
  'Grade 6 Language strand: making predictions means using text clues and prior knowledge to guess what might happen next, then confirming or revising those predictions as more of the text is read.',
  [('Making a prediction while reading means ___.', ['Using clues and prior knowledge to guess what might happen next', 'Ignoring the text completely and guessing randomly', 'A concept unrelated to reading strategies', 'Reading the ending of a story before the beginning'], 0),
   ('Which of these might a reader use to help make a prediction?', ['Clues from the title, illustrations, and events so far', 'A source with no connection to the text', 'A concept unrelated to making predictions', 'Information from a completely different book'], 0),
   ('What does it mean to “confirm” a prediction while reading?', ['Checking whether the prediction matched what actually happened in the text', 'Ignoring what actually happens in the text', 'A concept unrelated to predictions', 'Making a brand new, unrelated prediction with no connection to the first'], 0),
   ('Why might a reader need to revise a prediction while reading further?', ['New information in the text may show the original prediction was incorrect', 'Predictions can never be revised once they are made', 'A reason unrelated to reading strategies', 'Revising predictions is unnecessary once a story begins'], 0),
   ('Why is making predictions considered a useful reading strategy?', ['It encourages active engagement and deeper thinking about a text', 'Making predictions has no effect on reading comprehension', 'A reason unrelated to reading strategies', 'Predictions are only useful after finishing a text, never during'], 0)]),
M('Line Symmetry and Rotational Symmetry',
  'Grade 6 Math strand: a shape has line symmetry if it can be folded along a line so both halves match exactly, and rotational symmetry if it looks the same after being turned less than a full rotation.',
  [('A shape has line symmetry if ___.', ['It can be folded along a line so both halves match exactly', 'It looks completely different no matter how it is folded', 'A concept unrelated to line symmetry', 'It has no straight edges at all'], 0),
   ('A shape has rotational symmetry if it ___.', ['Looks the same after being turned less than a full rotation', 'Only looks the same after a full 360-degree turn', 'A concept unrelated to rotational symmetry', 'Never looks the same no matter how it is turned'], 0),
   ('How many lines of symmetry does a square have?', ['4', '1', 'A number unrelated to a square’s symmetry', '2'], 0),
   ('Which of these letters has line symmetry?', ['A', 'F', 'A letter unrelated to line symmetry', 'R'], 0),
   ('Why might artists and designers use symmetry in their work?', ['Symmetry can create a sense of balance and visual appeal', 'Symmetry has no effect on how a design looks', 'A reason unrelated to symmetry', 'Designs are required to avoid symmetry entirely'], 0)]),
Sc('Conductors and Insulators: Materials in Electrical Circuits',
   'Grade 6 Science strand: a conductor allows electric current to flow easily through it, while an insulator resists the flow of electric current, a property that shapes how circuits and everyday devices are designed.',
   [('A conductor is a material that ___.', ['Allows electric current to flow through it easily', 'Blocks electric current from flowing through it', 'A concept unrelated to conductors', 'Has no connection to electricity at all'], 0),
    ('An insulator is a material that ___.', ['Resists the flow of electric current', 'Allows electric current to flow through it easily', 'A concept unrelated to insulators', 'Always conducts electricity better than metal'], 0),
    ('Which of these materials is typically a good conductor of electricity?', ['Copper', 'Rubber', 'A material unrelated to conducting electricity', 'Plastic'], 0),
    ('Why is rubber often used to coat electrical wires?', ['It insulates the wire, helping prevent electric shock', 'It conducts electricity better than the metal wire inside', 'A reason unrelated to electrical safety', 'Rubber has no effect on how a wire functions'], 0),
    ('Why is it important to understand the difference between conductors and insulators when designing electrical devices?', ['It helps ensure electricity flows where intended and people stay safe from shock', 'This distinction has no effect on how devices are designed', 'A reason unrelated to electrical safety', 'All materials conduct electricity in exactly the same way'], 0)]),
SS('Levels of Government in Canada: Municipal, Provincial, Federal',
   'Grade 6 Social Studies strand: Canada’s government is organized into three levels — municipal, provincial, and federal — each with distinct responsibilities for serving citizens.',
   [('Canada’s government is organized into which three levels?', ['Municipal, provincial, and federal', 'Only a single level, with no other divisions', 'A concept unrelated to Canada’s government structure', 'Regional, continental, and global'], 0),
    ('Which level of government is typically responsible for services like local roads and garbage collection?', ['Municipal government', 'Federal government', 'A level unrelated to these responsibilities', 'A level of government that does not exist in Canada'], 0),
    ('Which level of government is responsible for national defence and issues like immigration policy?', ['Federal government', 'Municipal government', 'A level unrelated to these responsibilities', 'A level of government that does not exist in Canada'], 0),
    ('Which level of government typically oversees education and healthcare policy within a province?', ['Provincial government', 'Municipal government only', 'A level unrelated to these responsibilities', 'No level of government oversees these areas'], 0),
    ('Why does Canada divide responsibilities among three levels of government?', ['It allows different levels to focus on issues suited to local, regional, or national scale', 'Dividing responsibilities serves no practical purpose', 'A reason unrelated to Canada’s government structure', 'A single level of government could handle every responsibility identically well'], 0)])]),
day(67, [
L('Oral Communication: Active Listening and Note-Taking',
  'Grade 6 Language strand: active listening involves fully focusing on a speaker and responding thoughtfully, while effective note-taking captures key ideas concisely rather than every single word.',
  [('Active listening involves ___.', ['Fully focusing on a speaker and responding thoughtfully', 'Only hearing a speaker while thinking about something else', 'A concept unrelated to active listening', 'Interrupting a speaker as often as possible'], 0),
   ('Effective notes should generally capture ___.', ['Key ideas concisely, rather than every single word', 'Every single word a speaker says, with nothing left out', 'A concept unrelated to note-taking', 'Only the speaker’s name, with no other information'], 0),
   ('Which of these is a sign of active listening?', ['Making eye contact and nodding to show understanding', 'Looking away and checking a phone during a conversation', 'A behaviour unrelated to active listening', 'Talking over the speaker repeatedly'], 0),
   ('Why might using abbreviations and symbols be helpful while taking notes?', ['They can help a listener record information quickly without missing key points', 'Abbreviations always make notes harder to understand later', 'A reason unrelated to note-taking', 'Using symbols is never useful while taking notes'], 0),
   ('Why is active listening an important skill in both school and everyday life?', ['It helps build understanding, respect, and clear communication with others', 'Active listening has no real benefit in communication', 'A reason unrelated to oral communication', 'Listening skills are not connected to understanding a speaker'], 0)]),
M('Solving Equations Involving Decimals',
  'Grade 6 Math strand: solving equations involving decimals uses the same inverse-operation steps as whole-number equations, applied carefully to decimal values.',
  [('To solve an equation with a decimal, you generally ___.', ['Use inverse operations, just as with whole numbers', 'Round every decimal to zero before solving', 'A method unrelated to solving equations', 'Ignore the decimal point during the solving process'], 0),
   ('Solve for x: x + 2.5 = 7.8.', ['x = 5.3', 'x = 5.8', 'A solution unrelated to the equation', 'x = 10.3'], 0),
   ('Solve for x: x - 1.4 = 3.6.', ['x = 5.0', 'x = 2.2', 'A solution unrelated to the equation', 'x = 5.6'], 0),
   ('Solve for x: 2x = 9.4.', ['x = 4.7', 'x = 18.8', 'A solution unrelated to the equation', 'x = 7.4'], 0),
   ('Why is it important to keep decimal points aligned while solving these equations?', ['Misaligned decimals can make the answer’s place value incorrect', 'Decimal point placement never affects the accuracy of an answer', 'A reason unrelated to solving equations', 'Decimal points can be placed anywhere without changing the value'], 0)]),
Sc('Drones and Modern Flight Technology',
   'Grade 6 Science strand: drones are unpiloted aircraft controlled remotely or by onboard computers, using propellers and the same basic forces of flight as other aircraft.',
   [('A drone is best described as ___.', ['An unpiloted aircraft controlled remotely or by onboard computers', 'An aircraft that must always have a pilot inside it', 'A concept unrelated to drones', 'A type of boat used for water travel'], 0),
    ('Like other aircraft, drones rely on which force to overcome gravity?', ['Lift', 'Friction only', 'A force unrelated to flight', 'Density'], 0),
    ('Which of these is a common real-world use for drones today?', ['Aerial photography and package delivery', 'A use unrelated to drone technology', 'Underwater exploration only, never aerial tasks', 'Drones have no practical uses'], 0),
    ('How do most small drones typically generate lift?', ['Spinning propellers that push air downward', 'Large fixed wings alone, with no propellers', 'A method unrelated to how drones fly', 'Balloons filled with helium'], 0),
    ('Why might drones be useful for scientists studying hard-to-reach environments?', ['They can access and capture data from locations that are difficult or unsafe for people to reach', 'Drones have no useful application in scientific research', 'A reason unrelated to drone technology', 'Drones can only be used in easily accessible locations'], 0)]),
SS('How Canadians Vote: Elections and Political Parties',
   'Grade 6 Social Studies strand: Canadians participate in democracy by voting in elections for candidates who often represent political parties with differing platforms and ideas.',
   [('In a Canadian election, citizens generally vote for ___.', ['A candidate to represent their area, often as part of a political party', 'No one, since Canada does not hold elections', 'A concept unrelated to Canadian elections', 'Only the Prime Minister directly, with no other candidates involved'], 0),
    ('A political party is best described as ___.', ['A group of people with similar political ideas who run candidates for office', 'A celebration with no connection to government', 'A concept unrelated to elections', 'A single individual with no supporters'], 0),
    ('Why might citizens compare political party platforms before voting?', ['To choose the candidate or party whose ideas best match their own views', 'Platforms have no influence on how people decide to vote', 'A reason unrelated to elections', 'All political parties always have identical platforms'], 0),
    ('To be eligible to vote in a Canadian federal election, a citizen must generally be at least ___.', ['18 years old', '10 years old', 'An age unrelated to voting eligibility', '30 years old'], 0),
    ('Why is voting considered an important part of Canadian democracy?', ['It gives citizens a voice in choosing their government representatives', 'Voting has no effect on who represents citizens in government', 'A reason unrelated to democracy', 'Elections are decided with no input from citizens at all'], 0)])]),
day(68, [
L('Writing: Crafting Realistic Dialogue in Narrative',
  'Grade 6 Language strand: realistic dialogue reflects how people actually speak, reveals character personality, and follows proper punctuation conventions like quotation marks and new paragraphs for each speaker.',
  [('Realistic dialogue in a story should ___.', ['Reflect how people actually speak', 'Sound as formal as a textbook at all times', 'A concept unrelated to dialogue', 'Avoid revealing anything about a character’s personality'], 0),
   ('In written dialogue, a new paragraph is typically started ___.', ['Each time the speaker changes', 'Only once per entire conversation', 'A concept unrelated to dialogue formatting', 'After every single word that is spoken'], 0),
   ('Which of these correctly punctuates a line of dialogue?', ['“I am ready to go,” said Maya.', 'I am ready to go, said Maya.', 'A sentence unrelated to dialogue punctuation', '“I am ready to go said Maya.'], 0),
   ('Why might a writer use dialogue to reveal a character’s personality?', ['The way a character speaks can show their attitude, background, or emotions', 'Dialogue never reveals anything about a character', 'A reason unrelated to writing dialogue', 'Only narration, never dialogue, can reveal character traits'], 0),
   ('Why is it important for dialogue to sound natural rather than overly formal?', ['Natural dialogue helps make characters and scenes feel realistic and relatable', 'Formal dialogue always makes a story feel more realistic', 'A reason unrelated to writing dialogue', 'The way characters speak has no effect on how readers experience a story'], 0)]),
M('Time: Elapsed Time and the 24-Hour Clock',
  'Grade 6 Math strand: elapsed time is the amount of time that passes between a start and an end time, and the 24-hour clock expresses time using hours 00 to 23 without needing a.m. or p.m.',
  [('Elapsed time is best described as ___.', ['The amount of time that passes between a start time and an end time', 'The exact time an event begins, with no reference to when it ends', 'A concept unrelated to elapsed time', 'A measurement that has nothing to do with clocks'], 0),
   ('On the 24-hour clock, 3:00 p.m. is written as ___.', ['15:00', '13:00', 'A time unrelated to the conversion', '03:00'], 0),
   ('If a movie starts at 14:30 and lasts 2 hours, at what time does it end?', ['16:30', '12:30', 'A time unrelated to the calculation', '17:00'], 0),
   ('How much time passes between 9:15 a.m. and 11:45 a.m.?', ['2 hours 30 minutes', '2 hours', 'A duration unrelated to the calculation', '3 hours 15 minutes'], 0),
   ('Why might the 24-hour clock be useful for schedules like train or flight timetables?', ['It avoids confusion between morning and afternoon times', 'The 24-hour clock makes timetables more confusing to read', 'A reason unrelated to timekeeping', 'It can only display times before noon'], 0)]),
Sc('The Layers of Earth’s Atmosphere',
   'Grade 6 Science strand: Earth’s atmosphere is made up of distinct layers, including the troposphere and stratosphere, each with different characteristics that support weather, climate, and life.',
   [('The layer of the atmosphere closest to Earth’s surface, where most weather occurs, is the ___.', ['Troposphere', 'Stratosphere', 'A layer unrelated to Earth’s atmosphere', 'Mesosphere'], 0),
    ('The stratosphere contains a layer that protects life on Earth by absorbing ___.', ['Harmful ultraviolet radiation from the Sun', 'All visible light from the Sun', 'A concept unrelated to the stratosphere', 'Sound waves travelling through space'], 0),
    ('Why does temperature generally decrease as altitude increases within the troposphere?', ['The air becomes thinner and less able to trap heat near the surface', 'Temperature always increases the higher you travel through the troposphere', 'A reason unrelated to atmospheric layers', 'The troposphere has no connection to temperature at all'], 0),
    ('Which gas makes up the largest percentage of Earth’s atmosphere?', ['Nitrogen', 'Oxygen', 'A gas unrelated to Earth’s atmosphere', 'Carbon dioxide'], 0),
    ('Why is it useful for scientists to study the different layers of the atmosphere?', ['It helps explain weather patterns, climate, and how the atmosphere protects life on Earth', 'The atmosphere’s layers have no effect on weather or climate', 'A reason unrelated to Earth science', 'Earth’s atmosphere is a single uniform layer with no distinct sections'], 0)]),
SS('The Role of the Governor General and Constitutional Monarchy',
   'Grade 6 Social Studies strand: Canada is a constitutional monarchy, meaning the monarch is head of state, represented in Canada by the Governor General, while elected officials hold governing power.',
   [('Canada is best described politically as a ___.', ['Constitutional monarchy', 'Country with no head of state at all', 'A concept unrelated to Canada’s political structure', 'Absolute monarchy with no elected officials'], 0),
    ('In Canada, the monarch is represented domestically by the ___.', ['Governor General', 'Prime Minister', 'A role unrelated to representing the monarch', 'Provincial premier'], 0),
    ('In a constitutional monarchy like Canada, who holds the actual governing power?', ['Elected officials, such as the Prime Minister and Parliament', 'The monarch alone, with no elected input', 'A concept unrelated to constitutional monarchy', 'No one holds any governing power'], 0),
    ('Which of these is a duty commonly associated with the Governor General?', ['Formally giving royal assent to new laws passed by Parliament', 'Personally writing and voting on every new law', 'A duty unrelated to the Governor General’s role', 'Replacing the Prime Minister whenever they choose'], 0),
    ('Why might Canada’s system be described as balancing tradition with democratic government?', ['It keeps a ceremonial monarchy while giving real governing power to elected representatives', 'It gives the monarch complete control over all governing decisions', 'A reason unrelated to Canada’s political structure', 'It removes all connection between Canada and the monarchy'], 0)])]),
day(69, [
L('Reading: Identifying Text Structure Patterns',
  'Grade 6 Language strand: nonfiction texts are often organized using structure patterns such as sequence, cause and effect, compare and contrast, or problem and solution, and recognizing these patterns supports comprehension.',
  [('Recognizing a text’s structure pattern can help a reader ___.', ['Better understand how ideas in the text are organized and connected', 'Ignore the content of the text entirely', 'A concept unrelated to text structure', 'Only understand the title of a text'], 0),
   ('Which structure pattern presents events in the order they happened?', ['Sequence', 'Compare and contrast', 'A pattern unrelated to text structure', 'Problem and solution'], 0),
   ('A text organized using the compare and contrast pattern focuses on ___.', ['Similarities and differences between two or more things', 'Only the order in which events occurred', 'A concept unrelated to text structure', 'A single cause with no described effect'], 0),
   ('Which structure pattern would most likely be used in a text describing a challenge and how it was resolved?', ['Problem and solution', 'Sequence only, with no described challenge', 'A pattern unrelated to text structure', 'Compare and contrast'], 0),
   ('Why might recognizing a cause and effect structure help a reader understand a nonfiction article?', ['It helps clarify why something happened and what resulted from it', 'Cause and effect structures provide no useful information to readers', 'A reason unrelated to text structure', 'Recognizing structure patterns never improves comprehension'], 0)]),
M('Stem-and-Leaf Plots',
  'Grade 6 Math strand: a stem-and-leaf plot organizes numerical data by splitting each value into a stem (leading digit or digits) and a leaf (the final digit), keeping the original values visible.',
  [('In a stem-and-leaf plot, the stem usually represents ___.', ['The leading digit or digits of a value', 'The final digit of a value only', 'A concept unrelated to stem-and-leaf plots', 'The total number of data points collected'], 0),
   ('In a stem-and-leaf plot, the leaf usually represents ___.', ['The final digit of a value', 'The leading digit of a value', 'A concept unrelated to stem-and-leaf plots', 'The average of all the data'], 0),
   ('In the data value 47, which digit would typically be the leaf?', ['7', '4', 'A digit unrelated to this value', '47'], 0),
   ('What is one advantage of a stem-and-leaf plot compared to a simple list of numbers?', ['It organizes data by size while still showing every original value', 'It hides the original data values completely', 'A reason unrelated to stem-and-leaf plots', 'It can only be used with exactly two data points'], 0),
   ('Why might a teacher use a stem-and-leaf plot to display a class’s test scores?', ['It shows the spread and clustering of scores while keeping each score visible', 'Stem-and-leaf plots cannot be used to display test scores', 'A reason unrelated to data management', 'It removes all individual scores from the display'], 0)]),
Sc('Insects and Pollinators: Their Role in Ecosystems',
   'Grade 6 Science strand: insects, including many pollinators like bees and butterflies, play essential roles in ecosystems by helping plants reproduce and supporting food webs.',
   [('Pollinators help plants reproduce by ___.', ['Carrying pollen from one flower to another', 'Removing pollen from flowers with no further effect', 'A concept unrelated to pollination', 'Preventing flowers from producing seeds'], 0),
    ('Which of these is a well-known pollinator?', ['A bee', 'An organism unrelated to pollination', 'A rock', 'A cloud'], 0),
    ('Why are many fruits and vegetables dependent on pollinators?', ['Pollination is often necessary for these plants to produce fruit and seeds', 'Pollinators have no connection to fruit or vegetable production', 'A reason unrelated to pollinators', 'Fruits and vegetables never require pollination'], 0),
    ('Besides pollination, how else do insects support many ecosystems?', ['They serve as an important food source for birds, amphibians, and other animals', 'Insects provide no useful role to other organisms', 'A reason unrelated to ecosystems', 'Insects only exist outside of any food web'], 0),
    ('Why might a decline in pollinator populations concern scientists?', ['It could reduce plant reproduction and disrupt food webs that depend on those plants', 'A decline in pollinators would have no effect on ecosystems', 'A reason unrelated to insects and ecosystems', 'Pollinators have no connection to the plants around them'], 0)]),
SS('Canada’s Justice System: Courts and the Rule of Law',
   'Grade 6 Social Studies strand: the rule of law means everyone, including government leaders, must follow the law, and Canada’s court system interprets and applies laws fairly through an independent judiciary.',
   [('The rule of law means that ___.', ['Everyone, including government leaders, must follow the law', 'Only ordinary citizens must follow the law, not leaders', 'A concept unrelated to the rule of law', 'Laws apply differently depending on a person’s job'], 0),
    ('Why is it important for Canada’s judges to be independent from political influence?', ['It helps ensure fair and unbiased decisions in court cases', 'Judicial independence has no effect on the fairness of court decisions', 'A reason unrelated to Canada’s justice system', 'Judges are expected to always favour the government’s position'], 0),
    ('Which of these is a role of Canada’s court system?', ['Interpreting and applying laws to resolve disputes and legal cases', 'Writing new laws with no involvement from Parliament', 'A role unrelated to the court system', 'Collecting taxes from citizens'], 0),
    ('What is the highest court in Canada, with the final say on legal appeals?', ['The Supreme Court of Canada', 'A municipal court', 'A court unrelated to Canada’s justice system', 'A provincial legislature'], 0),
    ('Why is the rule of law considered essential to a fair and functioning democracy?', ['It ensures laws are applied consistently and that no one is above them', 'The rule of law has no connection to fairness in society', 'A reason unrelated to democracy', 'A fair society can function without any laws at all'], 0)])]),
day(70, [
L('Review: Language Days 61-69',
  'Grade 6 Language strand: this review lesson revisits key ideas from Days 61-69, including prepositional phrases, descriptive writing, fact versus opinion, prefixes and suffixes, and text structure patterns.',
  [('A prepositional phrase begins with a preposition and ends with a ___.', ['Noun or pronoun', 'Verb only', 'A concept unrelated to prepositional phrases', 'Punctuation mark'], 0),
   ('A fact is a statement that ___.', ['Can be proven true or false with evidence', 'Reflects only a personal belief or feeling', 'A concept unrelated to facts', 'Is always written in a persuasive tone'], 0),
   ('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'A position unrelated to prefixes', 'Middle, always splitting the word in half'], 0),
   ('Recognizing a text’s structure pattern can help a reader ___.', ['Better understand how ideas in the text are organized and connected', 'Ignore the content of the text entirely', 'A concept unrelated to text structure', 'Only understand the title of a text'], 0),
   ('Why is it useful to review grammar, writing, and reading strategies together?', ['It reinforces how these language skills connect and support one another', 'These skills have no connection to each other', 'A reason unrelated to reviewing language concepts', 'Review never helps strengthen understanding of language skills'], 0)]),
M('Review: Math Days 61-69',
  'Grade 6 Math strand: this review lesson revisits key ideas from Days 61-69, including adding and subtracting decimals, nets of 3D figures, quadrilaterals, symmetry, and stem-and-leaf plots.',
  [('To add or subtract decimals correctly, you must first ___.', ['Line up the decimal points so digits match by place value', 'Round every number to the nearest whole number first', 'A step unrelated to adding decimals', 'Ignore the decimal points completely'], 0),
   ('A net is best described as ___.', ['A two-dimensional pattern that folds into a three-dimensional figure', 'A three-dimensional figure with no flat faces', 'A concept unrelated to nets', 'A type of graph used to display data'], 0),
   ('A rhombus is a quadrilateral with ___.', ['Four equal sides', 'Only two equal sides', 'A description unrelated to a rhombus', 'No sides that are ever equal'], 0),
   ('A shape has rotational symmetry if it ___.', ['Looks the same after being turned less than a full rotation', 'Only looks the same after a full 360-degree turn', 'A concept unrelated to rotational symmetry', 'Never looks the same no matter how it is turned'], 0),
   ('Why is it useful to review number, geometry, and data concepts together?', ['It reinforces how these math skills connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Science Days 61-69',
   'Grade 6 Science strand: this review lesson revisits key ideas from Days 61-69, including animal adaptations, the Moon’s phases, gravity, conductors and insulators, and Earth’s atmosphere.',
   [('An adaptation is best described as ___.', ['A physical feature or behaviour that helps an organism survive in its environment', 'A random change with no effect on survival', 'A concept unrelated to adaptations', 'A feature that always harms an organism’s chances of survival'], 0),
    ('The Moon’s phases are caused by ___.', ['Its changing position relative to Earth and the Sun', 'The Moon changing shape physically each month', 'A concept unrelated to the Moon’s phases', 'The Moon disappearing and reforming every month'], 0),
    ('What keeps the planets in orbit around the Sun?', ['The Sun’s gravitational pull', 'The complete absence of any force acting on the planets', 'A concept unrelated to orbits', 'Strong winds in space'], 0),
    ('A conductor is a material that ___.', ['Allows electric current to flow through it easily', 'Blocks electric current from flowing through it', 'A concept unrelated to conductors', 'Has no connection to electricity at all'], 0),
    ('Why is it useful to review life systems, space, and physical science concepts together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Social Studies Days 61-69',
   'Grade 6 Social Studies strand: this review lesson revisits key ideas from Days 61-69, including the Indus Valley Civilization, West African kingdoms, the French and American Revolutions, and levels of Canadian government.',
   [('The Indus Valley Civilization developed along which river system?', ['The Indus River', 'The Nile River', 'A river unrelated to this civilization', 'The Amazon River'], 0),
    ('The West African kingdoms of Ghana, Mali, and Songhai grew powerful largely through control of ___.', ['Gold and salt trade routes across the Sahara', 'Fishing rights along the Atlantic coast only', 'A concept unrelated to these kingdoms', 'Trade routes that had no connection to gold or salt'], 0),
    ('A major cause of the French Revolution was ___.', ['Widespread inequality and a financial crisis affecting the country', 'A period with no economic or social problems at all', 'A concept unrelated to the French Revolution', 'An agreement between all social classes with no conflict'], 0),
    ('Canada’s government is organized into which three levels?', ['Municipal, provincial, and federal', 'Only a single level, with no other divisions', 'A concept unrelated to Canada’s government structure', 'Regional, continental, and global'], 0),
    ('Why is it useful to review ancient civilizations, revolutions, and Canadian government together?', ['It reinforces how historical developments connect to how societies and governments are structured today', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260813):
    """Same technique used for the earlier Phase 3 batches -- reassigns
    each question's correct-answer slot via a shuffled round-robin (even
    across 0-3) and shuffles the wrong options into the remaining slots.
    Question and option TEXT is never changed. Mutates `days` in place."""
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    n = sum(len(quiz) for quiz in all_quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in all_quizzes:
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


if __name__ == '__main__':
    _rebalance_answer_positions(g6_61_70)
    append_to(6, g6_61_70)
