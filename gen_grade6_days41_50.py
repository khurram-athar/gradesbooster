#!/usr/bin/env python3
"""Phase 3: Grade 6, Days 41-50 (second Grade 6 batch, continuing the
10-day pattern). Topics chosen to avoid any overlap with the existing Day
1-40 set (see data/grade6.json after the Days 31-40 batch): rhetorical
devices, the distributive property, proportional reasoning, photosynthesis,
the immune system, Newton's laws, and further world-history topics
(Byzantine Empire, Mongol Empire, Aztec/Inca civilizations, colonialism
and decolonization, the EU, and Canada's foreign policy).

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes use the curly
Unicode form (’) so they never collide with the single-quoted Python
string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
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


g6_41_50 = [
day(41, [
L('Reading: Analyzing Rhetorical Devices',
  'Ontario Grade 6 Reading strand: rhetorical devices, such as repetition, rhetorical questions, and appeals to emotion, are techniques writers and speakers use to persuade or emphasize a point.',
  [('A rhetorical question is a question ___.', ['Asked to genuinely request information', 'Asked for effect, without expecting a direct answer', 'Never used in persuasive writing', 'Always answered immediately by the writer'], 1),
   ('Repetition as a rhetorical device is used to ___.', ['Emphasize an important idea', 'Confuse the reader on purpose', 'Remove emphasis from a point', 'Avoid making any point at all'], 0),
   ('An appeal to emotion tries to persuade an audience by ___.', ['Triggering feelings related to the topic', 'Presenting only statistics with no emotional language', 'Avoiding any connection to the audience’s feelings', 'Ignoring the audience completely'], 0),
   ('Why might a speaker use rhetorical devices in a speech?', ['To make their argument more persuasive and memorable', 'Rhetorical devices weaken every argument', 'They have no effect on an audience', 'They should never be used in speeches'], 0),
   ('Which is an example of using repetition for rhetorical effect?', ['We will not give up. We will not back down. We will succeed.', 'We might try again later.', 'This is a plain, neutral statement.', 'The weather today is mild.'], 0)]),
M('The Distributive Property in Algebra',
  'Ontario Grade 6 Algebra strand: the distributive property states that multiplying a number by a sum is the same as multiplying it by each addend separately and then adding the results, such as 3(x + 4) equalling 3x + 12.',
  [('Using the distributive property, what is 3 times (x + 4)?', ['3x + 4', '3x + 12', 'x + 12', '3x + 7'], 1),
   ('Using the distributive property, what is 5 times (y + 2)?', ['5y + 2', '5y + 10', 'y + 10', '5y + 7'], 1),
   ('The distributive property allows you to ___.', ['Multiply a number by each term inside parentheses separately', 'Ignore the parentheses completely', 'Only add numbers, never multiply', 'Divide instead of multiply'], 0),
   ('Using the distributive property, what is 4 times (2x + 3)?', ['8x + 3', '8x + 12', '6x + 12', '2x + 12'], 1),
   ('Why is the distributive property useful in algebra?', ['It helps simplify expressions that involve parentheses', 'It has no practical use in algebra', 'It only applies to whole numbers with no variables', 'It eliminates the need for addition entirely'], 0)]),
Sc('Photosynthesis and Plant Energy',
   'Ontario Grade 6 Science Life Systems strand: photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce their own food (glucose) and release oxygen as a byproduct.',
   [('Photosynthesis allows plants to produce their own ___.', ['Food', 'Soil', 'Water only', 'Sunlight'], 0),
    ('Which three things do plants need for photosynthesis?', ['Sunlight, water, and carbon dioxide', 'Only soil and darkness', 'Only oxygen and darkness', 'Only sound and heat'], 0),
    ('A byproduct released by plants during photosynthesis is ___.', ['Oxygen', 'Carbon dioxide only', 'Nitrogen only', 'Nothing is released'], 0),
    ('Why is photosynthesis important not just for plants, but for many other living things?', ['It produces oxygen that many organisms need to survive', 'Photosynthesis has no effect beyond the plant itself', 'It removes all oxygen from the atmosphere', 'It has no connection to other living things'], 0),
    ('The sugar produced by plants during photosynthesis is called ___.', ['Glucose', 'Cellulose only', 'Chlorophyll', 'Carbon dioxide'], 0)]),
SS('The Fall of the Roman Empire',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the fall of the Roman Empire in the West, traditionally dated to 476 CE, resulted from a combination of factors including economic troubles, invasions, and political instability.',
   [('The fall of the Western Roman Empire is traditionally dated to which year?', ['476 CE', '1000 CE', '1492 CE', '1789 CE'], 0),
    ('Which is a commonly cited factor in the fall of the Roman Empire?', ['Economic troubles and political instability', 'A sudden, single unexplained event', 'No factors at all, since it never actually fell', 'Only good weather'], 0),
    ('Invasions by various groups contributed to ___.', ['The weakening of the Western Roman Empire', 'The strengthening of Rome with no negative effects', 'Nothing related to Rome’s decline', 'The founding of Rome'], 0),
    ('Why do historians study the fall of the Roman Empire?', ['To understand the causes behind the decline of a major historical civilization', 'This event has no historical significance', 'The Roman Empire never actually existed', 'It has no connection to later European history'], 0),
    ('After the fall of the Western Roman Empire, Europe entered a period often referred to as ___.', ['The Medieval or Middle Ages', 'Modern times immediately', 'A period with no historical name', 'The Renaissance immediately'], 0)])]),

day(42, [
L('Writing: Writing a Book Critique',
  'Ontario Grade 6 Writing strand: a book critique evaluates a book’s strengths and weaknesses, such as its plot, characters, and writing style, supported by specific examples from the text.',
  [('A book critique focuses on ___.', ['Evaluating a book’s strengths and weaknesses with examples', 'Only listing the book’s price', 'Ignoring the book’s content entirely', 'Copying the book word for word'], 0),
   ('Which element might a book critique evaluate?', ['Plot, characters, and writing style', 'Only the book’s cover colour', 'The publisher’s address', 'The number of chapters only'], 0),
   ('Why should a book critique include specific examples from the text?', ['To support the reviewer’s opinions with clear evidence', 'Examples are unnecessary in a critique', 'A critique should never reference the actual text', 'Examples make a critique less credible'], 0),
   ('A well-balanced book critique typically discusses ___.', ['Both strengths and weaknesses of the book', 'Only positive aspects, with no criticism', 'Only negative aspects, with no praise', 'Nothing specific about the book at all'], 0),
   ('Why might a critique differ from a simple book report?', ['A critique involves evaluating and analyzing quality, not just summarizing', 'A critique and a report are exactly the same', 'A critique never includes any analysis', 'A book report always includes more analysis than a critique'], 0)]),
M('Solving Equations with Fractions',
  'Ontario Grade 6 Algebra strand: solving equations that include fractions often involves using inverse operations, such as multiplying both sides by the denominator to eliminate the fraction.',
  [('Solve for x: x/3 = 6.', ['x = 2', 'x = 3', 'x = 9', 'x = 18'], 3),
   ('Solve for y: y/4 + 2 = 5.', ['y = 3', 'y = 8', 'y = 12', 'y = 20'], 2),
   ('To eliminate a fraction like x/5 in an equation, you can ___.', ['Multiply both sides by 5', 'Divide both sides by 5', 'Add 5 to both sides', 'Subtract 5 from both sides'], 0),
   ('Solve for n: n/2 minus 3 = 1.', ['n = 2', 'n = 4', 'n = 8', 'n = 6'], 2),
   ('Solve for m: 2m/3 = 8.', ['m = 4', 'm = 8', 'm = 12', 'm = 16'], 2)]),
Sc('Ecosystem Interdependence and Symbiosis',
   'Ontario Grade 6 Science Life Systems strand: symbiosis describes close relationships between different species in an ecosystem, including mutualism (both benefit), commensalism (one benefits, the other unaffected), and parasitism (one benefits, the other harmed).',
   [('Symbiosis refers to ___.', ['A close relationship between different species', 'A single species living completely alone', 'Only non-living interactions', 'The absence of any species interaction'], 0),
    ('In a mutualistic relationship, ___.', ['Both species benefit', 'Only one species benefits, while the other is harmed', 'Neither species benefits', 'One species disappears completely'], 0),
    ('In a parasitic relationship, ___.', ['Both species benefit equally', 'One species benefits while the other is harmed', 'Neither species is affected at all', 'Only the environment is affected, not the species'], 1),
    ('In a commensal relationship, ___.', ['One species benefits while the other is largely unaffected', 'Both species are always harmed', 'Both species always benefit equally', 'Neither species exists in the relationship'], 0),
    ('Why is understanding symbiotic relationships important in studying ecosystems?', ['It helps explain how different species depend on and affect one another', 'Symbiosis has no connection to ecosystems', 'Species in an ecosystem never interact', 'Symbiotic relationships only exist in a laboratory setting'], 0)]),
SS('The Byzantine Empire',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Byzantine Empire was the continuation of the Eastern Roman Empire, centred in Constantinople, known for preserving Roman and Greek traditions and developing its own rich culture for many centuries.',
   [('The Byzantine Empire was the continuation of the ___.', ['Western Roman Empire', 'Eastern Roman Empire', 'Ancient Egyptian Empire', 'Mongol Empire'], 1),
    ('The capital city of the Byzantine Empire was ___.', ['Rome', 'Constantinople', 'Athens', 'Cairo'], 1),
    ('The Byzantine Empire is known for preserving elements of ___.', ['Roman and Greek traditions', 'No historical traditions at all', 'Only traditions unrelated to Rome or Greece', 'A completely unrelated culture'], 0),
    ('The Byzantine Empire lasted for ___.', ['Only a single year', 'Many centuries', 'Less than a decade', 'It never actually existed'], 1),
    ('Why is the Byzantine Empire significant to world history?', ['It helped preserve and pass on classical knowledge and culture for centuries', 'It had no connection to Roman or Greek history', 'It contributed nothing to world history', 'It existed only in legend, not reality'], 0)])]),

day(43, [
L('Grammar: Verb Tense Consistency',
  'Ontario Grade 6 Writing strand: verb tense consistency means keeping the same tense (past, present, or future) throughout related sentences unless there is a clear reason to shift, to avoid confusing the reader.',
  [('Verb tense consistency means ___.', ['Randomly switching tenses throughout a piece of writing', 'Keeping the same tense throughout related sentences', 'Using only the future tense at all times', 'Avoiding verbs entirely'], 1),
   ('Which sentence has a tense consistency error?', ['Yesterday, I walked to school and eat breakfast.', 'Yesterday, I walked to school and ate breakfast.', 'I will walk to school tomorrow.', 'I walk to school every day.'], 0),
   ('Why is verb tense consistency important in writing?', ['It helps avoid confusing the reader about when events occur', 'Tense consistency has no effect on clarity', 'Writers should always mix tenses freely with no pattern', 'It replaces the need for correct spelling'], 0),
   ('Which sentence correctly maintains consistent past tense?', ['She opened the door and walked inside.', 'She opened the door and walks inside.', 'She opens the door and walked inside.', 'She will open the door and walked inside.'], 0),
   ('When might a shift in verb tense be appropriate within a piece of writing?', ['When clearly signaling a change in the time being described', 'Tense should never shift under any circumstances', 'Only when writing about the future', 'Shifting tense is always a grammar error with no exceptions'], 0)]),
M('Proportional Reasoning',
  'Ontario Grade 6 Number strand: proportional reasoning involves comparing two ratios to determine if they are equal, often used to solve problems involving scaling, recipes, or map distances.',
  [('If 2 pencils cost $1, how much would 8 pencils cost, using proportional reasoning?', ['$2', '$4', '$8', '$1'], 1),
   ('Two ratios are proportional if ___.', ['They are equal when simplified', 'They always have different values', 'They cannot be compared', 'One ratio must always be larger'], 0),
   ('If a map shows 1 cm representing 20 km, how many kilometres does 5 cm represent?', ['20 km', '25 km', '100 km', '5 km'], 2),
   ('Which situation would likely use proportional reasoning?', ['Scaling a recipe up to serve more people', 'Choosing a favourite colour', 'Selecting a book to read', 'Deciding what time to wake up'], 0),
   ('If 3 shirts cost $45, what would 5 shirts cost at the same rate?', ['$60', '$75', '$50', '$65'], 1)]),
Sc('The Immune System: How the Body Fights Illness',
   'Ontario Grade 6 Science Human Body Systems strand: the immune system defends the body against harmful microorganisms using white blood cells and other defenses that identify and destroy invading pathogens.',
   [('The immune system’s main role is to ___.', ['Defend the body against harmful microorganisms', 'Digest food', 'Pump blood throughout the body', 'Control body movement'], 0),
    ('Which cells play a key role in fighting off infections in the immune system?', ['White blood cells', 'Muscle cells only', 'Skin cells only', 'Bone cells only'], 0),
    ('A pathogen is best described as ___.', ['A microorganism capable of causing disease', 'A type of healthy cell', 'A part of the skeletal system', 'A vitamin found in food'], 0),
    ('Why might a fever occur when the body is fighting an infection?', ['It can be part of the immune system’s response to help fight off pathogens', 'Fevers have no connection to the immune system', 'Fevers always indicate a completely healthy body', 'The immune system has no role in body temperature'], 0),
    ('Vaccines work by helping the immune system ___.', ['Recognize and respond more quickly to specific pathogens', 'Ignore all future infections completely', 'Stop functioning altogether', 'Increase the risk of illness'], 0)]),
SS('The Mongol Empire',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Mongol Empire, founded by Genghis Khan in the 13th century, became the largest contiguous land empire in history, connecting trade and cultural exchange across Asia and into Europe.',
   [('The Mongol Empire was founded by ___.', ['Genghis Khan', 'A Roman emperor', 'A Byzantine ruler', 'An Egyptian pharaoh'], 0),
    ('The Mongol Empire is often noted for being ___.', ['The largest contiguous land empire in history', 'A very small, short-lived kingdom', 'Limited to a single small city', 'Entirely disconnected from trade routes'], 0),
    ('The Mongol Empire helped connect trade and cultural exchange across ___.', ['Asia and into Europe', 'Only one isolated village', 'No regions at all', 'Only modern countries'], 0),
    ('In which century was the Mongol Empire founded?', ['5th century', '13th century', '19th century', '21st century'], 1),
    ('Why is the Mongol Empire significant in world history?', ['It had a major impact on trade, culture, and political boundaries across a vast region', 'It had no lasting impact on history', 'It never actually controlled any territory', 'It was limited to religious activities only'], 0)])]),

day(44, [
L('Vocabulary: Idioms Across Cultures',
  'Ontario Grade 6 Language strand: idioms are expressions whose meaning cannot be understood literally, and different cultures and languages often have their own unique idioms that reflect their history and values.',
  [('An idiom is an expression whose meaning ___.', ['Can always be understood literally', 'Cannot be understood from its literal words alone', 'Is identical in every language', 'Has no meaning at all'], 1),
   ('Different cultures often have their own idioms because ___.', ['Language and expressions are shaped by a culture’s history and experiences', 'All cultures use identical idioms', 'Idioms have no connection to culture', 'Cultures never develop unique expressions'], 0),
   ('Why might idioms be challenging for someone learning a new language?', ['Their meaning often cannot be figured out by translating the words literally', 'Idioms are always easy to understand literally', 'Idioms never appear in everyday conversation', 'All languages share the exact same idioms'], 0),
   ('Which is an example of an English idiom?', ['Break the ice', 'The sky is blue', 'Two plus two equals four', 'The dog is brown'], 0),
   ('Comparing idioms across cultures can help students ___.', ['Appreciate different ways language reflects culture', 'Conclude that all cultures are identical', 'Avoid learning about other cultures', 'Ignore the connection between language and culture'], 0)]),
M('Volume of Triangular Prisms and Cylinders',
  'Ontario Grade 6 Geometry strand: the volume of a triangular prism is found using base area times length, while the volume of a cylinder is found using the area of its circular base times its height.',
  [('The formula for the volume of a cylinder is ___.', ['Base area (a circle) times height', 'Base area times width only', 'Radius times height only', 'Diameter times height'], 0),
   ('If a triangular prism’s base area is 10 square units and its length is 6 units, what is its volume?', ['16 cubic units', '60 cubic units', '10 cubic units', '600 cubic units'], 1),
   ('To find the volume of a cylinder, you first need to calculate the area of its ___.', ['Circular base', 'Rectangular side', 'Height only', 'Diameter only'], 0),
   ('Both triangular prisms and cylinders have volume formulas that involve ___.', ['Multiplying a base area by a height or length', 'Adding all the edges together', 'Ignoring the base entirely', 'Only measuring the outer surface'], 0),
   ('If a cylinder’s circular base area is 28 square units and its height is 5 units, what is its volume?', ['33 cubic units', '140 cubic units', '23 cubic units', '5.6 cubic units'], 1)]),
Sc('Newton’s Laws of Motion: An Introduction',
   'Ontario Grade 6 Science Structures and Mechanisms strand: Newton’s laws of motion describe how objects behave when forces act on them, including how objects at rest stay at rest unless acted on by an outside force.',
   [('According to Newton’s first law, an object at rest will ___.', ['Stay at rest unless acted on by an outside force', 'Always start moving on its own', 'Immediately disappear', 'Change its own mass spontaneously'], 0),
    ('Newton’s laws of motion describe how objects behave when ___.', ['Forces act on them', 'No forces exist anywhere', 'They have no mass at all', 'They are completely motionless with no exceptions'], 0),
    ('Which is an everyday example related to Newton’s first law?', ['A ball stays still until someone kicks it', 'A ball changes colour on its own', 'A ball disappears without any cause', 'A ball grows heavier while sitting still'], 0),
    ('Newton’s laws are considered foundational to the study of ___.', ['Motion and forces in physics', 'Only chemistry', 'Only biology', 'Only geography'], 0),
    ('Why are Newton’s laws still relevant in modern science and engineering?', ['They help explain and predict how objects move under different forces', 'These laws have been proven completely incorrect', 'They only applied in the past, not today', 'They have no connection to real-world motion'], 0)]),
SS('The Aztec and Inca Civilizations',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Aztec civilization in Mesoamerica and the Inca civilization in South America both developed advanced cities, agriculture, and governance systems before European contact.',
   [('The Aztec civilization was located mainly in ___.', ['Mesoamerica (present-day Mexico)', 'North Africa', 'Northern Europe', 'East Asia'], 0),
    ('The Inca civilization was located mainly in ___.', ['South America', 'North Africa', 'Southeast Asia', 'Northern Europe'], 0),
    ('Both the Aztec and Inca civilizations developed advanced ___.', ['Cities, agriculture, and governance systems', 'No cities or organized systems at all', 'Only small nomadic camps', 'Systems identical to modern countries'], 0),
    ('These civilizations existed ___ major European contact.', ['Before', 'Only after', 'At the exact same time as', 'They had no connection to European contact at all'], 0),
    ('Why do historians study the Aztec and Inca civilizations?', ['They represent significant, advanced societies with rich cultural achievements', 'These civilizations had no notable achievements', 'They never actually existed', 'They are identical to European civilizations of the same era'], 0)])]),

day(45, [
L('Reading: Analyzing Non-Linear Narrative Structure',
  'Ontario Grade 6 Reading strand: some stories use a non-linear structure, presenting events out of chronological order through techniques like flashbacks, to build suspense or reveal information strategically.',
  [('A non-linear narrative structure presents events ___.', ['In strict chronological order only', 'Out of chronological order', 'With no events at all', 'Only in the future tense'], 1),
   ('A flashback is a technique used to ___.', ['Show an event from earlier in the timeline', 'Predict a future event with certainty', 'Remove all context from a story', 'Skip the story’s ending entirely'], 0),
   ('Why might an author choose a non-linear structure for a story?', ['To build suspense or reveal information strategically', 'Non-linear structures always make stories worse', 'To confuse the reader with no purpose', 'It is required for every story'], 0),
   ('Which is a sign that a story might be using a non-linear structure?', ['The story jumps between past and present events', 'The story proceeds in perfect chronological order', 'The story has no characters', 'The story has no setting'], 0),
   ('Why might understanding narrative structure help readers follow a complex story?', ['It helps readers track how and why events are being presented in a particular order', 'Narrative structure has no effect on understanding', 'Readers never need to consider story structure', 'All stories use the exact same structure'], 0)]),
M('Multiplying and Dividing Integers',
  'Ontario Grade 6 Number strand: when multiplying or dividing integers, two numbers with the same sign produce a positive result, while two numbers with different signs produce a negative result.',
  [('What is the result of a negative integer multiplied by a negative integer?', ['Negative', 'Positive', 'Zero', 'Cannot be determined'], 1),
   ('What is the result of a positive integer multiplied by a negative integer?', ['Positive', 'Negative', 'Zero', 'Cannot be determined'], 1),
   ('What is -4 times -3?', ['-12', '12', '-7', '7'], 1),
   ('What is 15 divided by -3?', ['5', '-5', '-18', '18'], 1),
   ('What is -20 divided by -4?', ['5', '-5', '-24', '24'], 0)]),
Sc('The Periodic Table: An Introduction to Elements',
   'Ontario Grade 6 Science Matter and Energy strand: the periodic table organizes all known chemical elements based on their properties, with elements arranged by increasing atomic number.',
   [('The periodic table organizes elements based on their ___.', ['Properties and atomic number', 'Colour only', 'Random order with no pattern', 'Alphabetical order of their names'], 0),
    ('An element is best described as ___.', ['A pure substance made of only one type of atom', 'Always a mixture of multiple substances', 'A living organism', 'A type of energy, not matter'], 0),
    ('Which of these is an example of an element found on the periodic table?', ['Oxygen', 'Water', 'Air', 'Salt water'], 0),
    ('Elements on the periodic table are arranged by ___.', ['Increasing atomic number', 'Random placement with no order', 'Alphabetical order only', 'Colour only'], 0),
    ('Why is the periodic table a useful tool in science?', ['It organizes elements in a way that reveals patterns in their properties', 'It has no scientific usefulness', 'It only lists elements with no other information', 'It is used only in mathematics, not science'], 0)]),
SS('Colonialism in Africa',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: during the 19th and early 20th centuries, several European powers colonized much of Africa, significantly impacting local societies, economies, and political borders.',
   [('During the 19th and early 20th centuries, several European powers colonized much of ___.', ['Africa', 'Antarctica', 'The Moon', 'No territory at all'], 0),
    ('Colonialism in Africa significantly impacted local ___.', ['Societies, economies, and political borders', 'Nothing at all', 'Only weather patterns', 'Only wildlife populations'], 0),
    ('Colonial powers often drew political borders in Africa based on ___.', ['Their own interests, sometimes with little regard for existing communities', 'Careful, consistent consultation with every local community', 'Random chance with no lasting effect', 'Ancient borders that had never changed'], 0),
    ('Why do historians study the effects of colonialism in Africa?', ['To understand its long-lasting impact on the continent’s societies and politics', 'Colonialism had no lasting effects', 'Colonialism never occurred in Africa', 'It has no connection to modern African nations'], 0),
    ('Which is a lasting effect often associated with colonial-era borders in Africa?', ['Borders that sometimes divided or combined communities in ways that caused later challenges', 'Borders that perfectly matched every community with no issues', 'No effect on modern nations at all', 'Borders that were immediately erased after colonization'], 0)])]),

day(46, [
L('Writing: Persuasive Letter Writing',
  'Ontario Grade 6 Writing strand: a persuasive letter presents a clear request or opinion, supported by reasons and evidence, and is written with a tone and format appropriate for its intended reader.',
  [('A persuasive letter is written to ___.', ['Convince the reader of an opinion or request', 'Only describe the writer’s daily schedule', 'Avoid taking any clear position', 'Copy information with no persuasive purpose'], 0),
   ('A persuasive letter should be supported by ___.', ['Reasons and evidence', 'No supporting details at all', 'Only the writer’s name', 'Random, unrelated facts'], 0),
   ('Why is tone important when writing a persuasive letter?', ['An appropriate tone helps the message be taken seriously by the reader', 'Tone has no effect on how a letter is received', 'Persuasive letters should always sound rude', 'Tone only matters in fictional writing'], 0),
   ('Which is an example of a strong persuasive letter opening?', ['I am writing to request that our school extend library hours, because...', 'This letter is about something.', 'Hello, this is a letter.', 'Nothing important is being requested here.'], 0),
   ('Why might a persuasive letter end with a clear call to action?', ['It tells the reader exactly what the writer hopes will happen next', 'A call to action weakens a persuasive letter', 'Persuasive letters should never state what the writer wants', 'Endings have no effect on persuasive writing'], 0)]),
M('Statistics: Analyzing and Comparing Data Sets',
  'Ontario Grade 6 Data Management strand: analyzing and comparing data sets involves looking at measures like mean, median, mode, and range to understand and compare different sets of information.',
  [('The range of a data set is found by ___.', ['Subtracting the smallest value from the largest value', 'Adding all values together', 'Finding the middle value only', 'Finding the most frequent value only'], 0),
   ('What is the range of the data set 4, 9, 15, 22?', ['9', '15', '18', '22'], 2),
   ('Comparing the mean of two data sets can help determine ___.', ['Which set has a higher overall average', 'Nothing useful about the data', 'Which set has more individual values, regardless of size', 'Only the colour of the data'], 0),
   ('Why might range be a useful statistic to calculate alongside the mean?', ['It shows how spread out the data values are', 'Range has no connection to understanding data', 'Range always equals the mean', 'Range should never be calculated with the mean'], 0),
   ('If Data Set A has a mean of 50 and Data Set B has a mean of 65, which set has a higher average?', ['Data Set A', 'Data Set B', 'They are equal', 'Cannot be determined from the means alone'], 1)]),
Sc('Space Exploration Technologies and Robotics',
   'Ontario Grade 6 Science and Technology strand: space exploration relies on technologies such as rockets, satellites, and robotic rovers to study space and other planets without always requiring human astronauts.',
   [('Robotic rovers are used in space exploration to ___.', ['Study planets and gather data, often without a human on board', 'Replace all forms of space technology', 'Prevent any exploration of other planets', 'Only orbit Earth with no other function'], 0),
    ('Satellites in space exploration are commonly used for ___.', ['Communication and observation', 'Nothing useful', 'Only decoration', 'Preventing all forms of communication'], 0),
    ('One advantage of using robots instead of astronauts for some space missions is ___.', ['Robots can operate in environments too extreme or risky for humans', 'Robots have no advantages over astronauts', 'Robots cannot gather any useful information', 'Robots always cost significantly more than crewed missions'], 0),
    ('Rockets are primarily used in space exploration to ___.', ['Launch spacecraft beyond Earth’s atmosphere', 'Stay permanently on Earth’s surface', 'Replace the need for satellites', 'Only orbit underwater'], 0),
    ('Why has robotic technology become increasingly important in space exploration?', ['It allows for exploration of distant or hazardous locations more safely and often at lower cost', 'Robotic technology has no role in space exploration', 'Robots cannot function in space at all', 'Robotic exploration has replaced the need for any spacecraft'], 0)]),
SS('Decolonization Movements in the 20th Century',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: decolonization refers to the process by which colonized nations, especially in Africa and Asia, gained independence from colonial powers during the 20th century.',
   [('Decolonization refers to the process of ___.', ['Colonized nations gaining independence from colonial powers', 'Countries becoming newly colonized', 'A single country expanding its colonies', 'Nations losing all forms of self-governance'], 0),
    ('Decolonization movements were especially significant in which regions during the 20th century?', ['Africa and Asia', 'Only Antarctica', 'Only uninhabited regions', 'No regions experienced decolonization'], 0),
    ('Why did many colonized nations seek independence during the 20th century?', ['To gain self-governance and control over their own political and economic future', 'They had no interest in gaining independence', 'Independence provided no benefits to these nations', 'Colonized nations were already fully independent'], 0),
    ('Decolonization often involved ___.', ['Political movements and, at times, significant conflict', 'No political activity whatsoever', 'Immediate and effortless transitions with no challenges', 'A return to earlier colonial rule'], 0),
    ('Why is studying decolonization important to understanding the modern world?', ['Many current nations and borders were shaped by this 20th-century process', 'Decolonization has no connection to today’s world', 'This process only affected ancient history', 'It has no relevance to modern international relations'], 0)])]),

day(47, [
L('Media Literacy: Analyzing News Bias Across Outlets',
  'Ontario Grade 6 Media Literacy strand: comparing how different news outlets report on the same event can reveal differences in tone, word choice, and focus that may indicate bias.',
  [('Comparing multiple news outlets on the same event can reveal ___.', ['Differences in tone, word choice, and focus', 'Nothing useful about the coverage', 'That all outlets always report identically', 'Only irrelevant details'], 0),
   ('Why might two news outlets present the same event differently?', ['They may have different perspectives, priorities, or biases', 'News outlets are legally required to report identically', 'Differences in reporting never occur', 'Facts always change between outlets'], 0),
   ('Which is a useful strategy for spotting potential bias in news coverage?', ['Comparing word choice and framing across multiple sources', 'Reading only a single source and assuming it is fully accurate', 'Ignoring all news coverage entirely', 'Assuming every source has identical bias'], 0),
   ('Word choice in a news report, such as calling a group protesters versus rioters, can ___.', ['Influence how readers perceive the event', 'Have no effect on how readers understand a story', 'Always be completely neutral with no impact', 'Never appear in real news coverage'], 0),
   ('Why is media literacy considered an important skill for citizens?', ['It helps people critically evaluate information and form well-informed opinions', 'Media literacy has no real-world value', 'Citizens do not need to evaluate news critically', 'All news sources are always perfectly unbiased'], 0)]),
M('Classifying and Constructing Triangles',
  'Ontario Grade 6 Geometry strand: triangles can be classified by their side lengths (equilateral, isosceles, scalene) and angles (acute, right, obtuse), and can be constructed using a ruler and protractor.',
  [('A triangle with three equal sides is called ___.', ['Scalene', 'Isosceles', 'Equilateral', 'Obtuse'], 2),
   ('A triangle with exactly two equal sides is called ___.', ['Equilateral', 'Isosceles', 'Scalene', 'Right'], 1),
   ('A triangle with one angle greater than 90 degrees is called ___.', ['Acute', 'Right', 'Obtuse', 'Equilateral'], 2),
   ('A triangle with all angles less than 90 degrees is called ___.', ['Acute', 'Obtuse', 'Right', 'Scalene'], 0),
   ('Which tools are commonly used to construct an accurate triangle?', ['A ruler and protractor', 'Only a calculator', 'Only a paintbrush', 'No tools are needed'], 0)]),
Sc('Sound Waves and Frequency',
   'Ontario Grade 6 Science Matter and Energy strand: sound travels as vibrations in waves, and frequency, measured in hertz, determines pitch, with higher frequencies producing higher-pitched sounds.',
   [('Sound travels through the air as ___.', ['Vibrations in waves', 'A solid beam of light', 'A type of liquid', 'Nothing measurable'], 0),
    ('Frequency is measured in units called ___.', ['Decibels', 'Hertz', 'Metres', 'Litres'], 1),
    ('A higher frequency generally produces a ___ pitched sound.', ['Lower', 'Higher', 'Silent', 'Identical'], 1),
    ('Which is an example of a high-pitched sound?', ['A bird’s chirp', 'A deep drumbeat', 'Complete silence', 'A low rumble'], 0),
    ('Why might understanding frequency be useful when studying musical instruments?', ['It helps explain why different instruments or notes produce different pitches', 'Frequency has no connection to sound or pitch', 'All instruments produce identical frequencies', 'Frequency only applies to light, not sound'], 0)]),
SS('The European Union: Cooperation and Integration',
   'Ontario Grade 6 Social Studies People and Environments strand: the European Union is a political and economic partnership among many European countries that cooperate on trade, travel, and shared policies.',
   [('The European Union is best described as ___.', ['A political and economic partnership among European countries', 'A single country in Europe', 'An organization with no member countries', 'A military-only alliance with no economic role'], 0),
    ('Member countries of the European Union often cooperate on issues such as ___.', ['Trade and shared policies', 'Nothing of shared interest', 'Only isolated, unrelated local issues', 'Preventing any cooperation between countries'], 0),
    ('One benefit some European Union countries experience is ___.', ['Easier trade and travel between member countries', 'Complete isolation from neighbouring countries', 'The elimination of all international relationships', 'No connection between member economies'], 0),
    ('Why might countries choose to form an organization like the European Union?', ['To gain benefits from working together on shared economic and political goals', 'Cooperation between countries provides no benefits', 'Forming such an organization serves no purpose', 'Countries are always better off acting in complete isolation'], 0),
    ('Studying the European Union helps students understand ___.', ['One example of how countries can cooperate through international organizations', 'That international cooperation never occurs', 'That all countries operate in complete isolation', 'That trade partnerships have no real-world examples'], 0)])]),

day(48, [
L('Grammar: Commonly Confused Words',
  'Ontario Grade 6 Language strand: some words are easily confused because they sound alike but have different meanings and spellings, such as affect versus effect, or accept versus except.',
  [('Which sentence correctly uses affect and effect? The medicine will ___ my health, and the ___ should be positive.', ['effect, affect', 'affect, effect', 'affect, affect', 'effect, effect'], 1),
   ('Accept generally means ___.', ['To receive or agree to something', 'To exclude something', 'To measure distance', 'To multiply numbers'], 0),
   ('Except generally means ___.', ['To receive something willingly', 'Excluding or leaving out', 'To celebrate an event', 'To measure time'], 1),
   ('Which sentence uses accept and except correctly? I will ___ your invitation, but I cannot attend every event ___ the first one.', ['accept, except', 'except, accept', 'accept, accept', 'except, except'], 0),
   ('Why is it useful to learn commonly confused word pairs?', ['It helps writers choose the correct word and avoid unclear or incorrect sentences', 'These word pairs have no effect on writing clarity', 'Confused words never impact meaning', 'Only one of each pair is ever a real word'], 0)]),
M('Nonlinear Growing Patterns',
  'Ontario Grade 6 Algebra strand: a nonlinear growing pattern changes by a rate that is not constant, such as doubling each time, unlike a linear pattern which increases by the same amount each step.',
  [('In the pattern 2, 4, 8, 16, what is the next number?', ['18', '20', '24', '32'], 3),
   ('A nonlinear pattern is one where the amount of change ___.', ['Stays exactly the same each step', 'Is not constant between steps', 'Never occurs at all', 'Is always negative'], 1),
   ('Which of these is an example of a nonlinear growing pattern?', ['3, 6, 12, 24', '3, 6, 9, 12', '5, 10, 15, 20', '2, 4, 6, 8'], 0),
   ('In a doubling pattern starting at 5, what are the first four terms?', ['5, 10, 15, 20', '5, 10, 20, 40', '5, 7, 9, 11', '5, 6, 7, 8'], 1),
   ('How is a nonlinear pattern different from a linear pattern?', ['A nonlinear pattern’s rate of change is not constant, while a linear pattern’s is', 'They are exactly the same type of pattern', 'A linear pattern always decreases', 'A nonlinear pattern never changes at all'], 0)]),
Sc('Weather Systems and Forecasting',
   'Ontario Grade 6 Science Earth and Space Systems strand: weather systems, such as high and low pressure areas and fronts, influence daily weather, and meteorologists use data and technology to forecast upcoming conditions.',
   [('A low pressure system is often associated with ___.', ['Clear, sunny weather with no clouds', 'Cloudy, stormy weather', 'No effect on weather at all', 'Only warm temperatures with no variation'], 1),
    ('Meteorologists use data and technology to ___.', ['Forecast upcoming weather conditions', 'Control the weather directly', 'Prevent all storms from happening', 'Ignore current weather patterns'], 0),
    ('A weather front occurs where ___.', ['Two different air masses meet', 'No air masses exist', 'Only one type of weather ever occurs', 'Temperature never changes'], 0),
    ('Which technology might meteorologists use to help forecast weather?', ['Satellites and radar', 'Only guesswork with no tools', 'A compass only', 'A thermometer with no other tools'], 0),
    ('Why is understanding weather systems useful for communities?', ['It helps people prepare for changing or severe weather conditions', 'Weather forecasting provides no useful information', 'Weather systems have no connection to daily life', 'Communities never need to prepare for weather changes'], 0)]),
SS('Modern Canadian Immigration and Multicultural Policy',
   'Ontario Grade 6 Social Studies People and Environments strand: Canada’s modern immigration and multiculturalism policies aim to welcome newcomers from around the world while supporting the preservation of diverse cultural identities.',
   [('Canada’s modern immigration policies aim to ___.', ['Welcome newcomers from around the world', 'Prevent all immigration to Canada', 'Only allow immigration from one specific country', 'Ignore the needs of newcomers entirely'], 0),
    ('Canada’s multiculturalism policy supports ___.', ['The preservation of diverse cultural identities', 'The elimination of all cultural diversity', 'A single required culture for all citizens', 'No recognition of cultural differences'], 0),
    ('Why might Canada benefit from welcoming immigrants from many different countries?', ['Immigration can contribute diverse skills, perspectives, and economic growth', 'Immigration provides no benefits to Canada', 'Diversity has no connection to a country’s growth', 'Immigrants contribute nothing to Canadian society'], 0),
    ('Canada officially adopted multiculturalism as a policy to ___.', ['Recognize and support the value of cultural diversity', 'Discourage cultural diversity', 'Require all citizens to abandon their heritage', 'Limit interactions between different cultural groups'], 0),
    ('Studying Canada’s immigration and multicultural policies helps students understand ___.', ['How Canada has shaped its identity as a diverse nation', 'That Canada has always been a closed, single-culture nation', 'That immigration policy has no connection to Canadian identity', 'That multiculturalism has no historical or political significance'], 0)])]),

day(49, [
L('Writing: Personal Narrative with Reflection',
  'Ontario Grade 6 Writing strand: a personal narrative with reflection tells a true story from the writer’s life and includes thoughtful reflection on what the experience meant or taught them.',
  [('A personal narrative is a story that is ___.', ['Entirely fictional', 'True and based on the writer’s own experience', 'Written by someone else about a stranger', 'Always about historical events only'], 1),
   ('Reflection in a personal narrative involves ___.', ['Describing what the experience meant or taught the writer', 'Ignoring the meaning of the experience entirely', 'Only listing events with no deeper thought', 'Copying someone else’s story'], 0),
   ('Why is reflection an important part of a personal narrative?', ['It helps convey the significance or lesson behind the experience', 'Reflection has no value in personal writing', 'A narrative should never include the writer’s thoughts', 'Reflection replaces the need for describing events'], 0),
   ('Which is an example of reflective writing in a personal narrative?', ['That experience taught me the importance of asking for help.', 'I woke up. I ate breakfast. I went to school.', 'The weather was cold that day.', 'The story has no connection to real events.'], 0),
   ('A strong personal narrative often includes both ___.', ['Descriptive storytelling and meaningful reflection', 'Only a list of unrelated facts', 'No storytelling elements at all', 'Only reflection with no actual story'], 0)]),
M('Simple and Compound Interest',
  'Ontario Grade 6 Financial Literacy strand: simple interest is calculated only on the original amount, while compound interest is calculated on the original amount plus any interest already earned, causing savings to grow faster over time.',
  [('Simple interest is calculated based on ___.', ['Only the original amount', 'The original amount plus previously earned interest', 'A completely random amount', 'Nothing related to the amount saved'], 0),
   ('Compound interest is calculated based on ___.', ['Only the original amount, never changing', 'The original amount plus interest already earned', 'An amount unrelated to savings', 'Only amounts borrowed, never saved'], 1),
   ('Why does compound interest generally cause savings to grow faster than simple interest?', ['Interest is earned on both the original amount and previously earned interest', 'Compound interest is calculated exactly the same way as simple interest', 'Compound interest always results in less money over time', 'Interest rates are always higher with simple interest'], 0),
   ('If you save money using compound interest, your balance grows because interest is calculated ___.', ['On both your original savings and prior interest earned', 'Only once, at the very end', 'On money not related to your account', 'Only on the interest, ignoring the original savings'], 0),
   ('Which type of interest would likely result in a larger final amount after several years, assuming the same rate?', ['Compound interest', 'Simple interest', 'They would always be exactly equal', 'Neither type of interest ever changes the final amount'], 0)]),
Sc('Human Impact on Climate Change',
   'Ontario Grade 6 Science Earth and Space Systems strand: human activities, such as burning fossil fuels and deforestation, release greenhouse gases that contribute to changes in Earth’s climate over time.',
   [('Which human activity is commonly linked to increased greenhouse gas emissions?', ['Burning fossil fuels', 'Planting more trees', 'Reducing energy use', 'Recycling materials'], 0),
    ('Deforestation can contribute to climate change by ___.', ['Reducing the number of trees that absorb carbon dioxide', 'Increasing the number of trees absorbing carbon dioxide', 'Having no effect on the atmosphere', 'Removing all greenhouse gases immediately'], 0),
    ('Greenhouse gases contribute to climate change by ___.', ['Trapping heat in Earth’s atmosphere', 'Cooling the atmosphere with no other effects', 'Having no connection to temperature', 'Immediately disappearing from the atmosphere'], 0),
    ('Why might reducing fossil fuel use help address climate change?', ['It can help lower the amount of greenhouse gases released into the atmosphere', 'Fossil fuel use has no connection to greenhouse gases', 'Reducing fossil fuel use always increases emissions', 'Climate change is unrelated to human activity'], 0),
    ('Which is an example of an action that could help reduce human impact on climate change?', ['Increasing the use of renewable energy sources', 'Increasing the burning of fossil fuels', 'Cutting down more forests with no replanting', 'Ignoring energy use entirely'], 0)]),
SS('Climate Change as a Global Issue',
   'Ontario Grade 6 Social Studies People and Environments strand: climate change affects countries around the world, requiring international cooperation among nations to address its causes and impacts.',
   [('Climate change is considered a global issue because ___.', ['It affects countries and regions around the world', 'It only affects a single isolated location', 'It has no international impact whatsoever', 'It is limited strictly to one continent'], 0),
    ('International cooperation on climate change often involves ___.', ['Countries working together to address shared environmental challenges', 'Countries refusing to communicate about the issue', 'A single country solving the issue alone with no help', 'Ignoring the problem entirely'], 0),
    ('Why might addressing climate change require cooperation between many countries?', ['Its causes and effects cross national borders and require coordinated action', 'Climate change only affects one specific country', 'International cooperation has no role in environmental issues', 'Countries never need to work together on shared problems'], 0),
    ('Which is an example of international cooperation related to climate change?', ['Countries participating in a global climate agreement', 'A single country acting in complete isolation', 'Countries refusing to discuss the issue at all', 'No form of cooperation has ever existed on this topic'], 0),
    ('Why is climate change considered relevant to social studies as well as science?', ['It involves political, economic, and social decisions among countries and communities', 'Climate change has no connection to social or political issues', 'Social studies has no relevance to environmental topics', 'Only scientists need to consider climate change'], 0)])]),

day(50, [
L('Reading: Evaluating Theme Across a Novel',
  'Ontario Grade 6 Reading strand: evaluating theme across an entire novel involves tracing how a central idea develops and is reinforced through multiple events, characters, and details throughout the story.',
  [('Evaluating theme across a novel involves ___.', ['Looking at a single isolated sentence only', 'Tracing how a central idea develops throughout the story', 'Ignoring the plot and characters entirely', 'Focusing only on the book’s cover'], 1),
   ('A theme is often reinforced throughout a novel through ___.', ['Multiple events, characters, and details', 'A single unrelated detail with no connection to the rest of the story', 'The book’s price', 'The font used in printing'], 0),
   ('Why might tracing a theme across an entire novel be more complex than identifying it in a single passage?', ['A novel’s theme often develops gradually through many connected parts of the story', 'Themes never appear in longer works like novels', 'Themes are always stated directly in the first sentence', 'Longer texts never have identifiable themes'], 0),
   ('Which is a strategy for evaluating a novel’s theme?', ['Considering how different characters’ experiences relate to a central idea', 'Ignoring the characters completely', 'Only reading the very last page', 'Assuming every novel has the exact same theme'], 0),
   ('Why is evaluating theme considered a valuable skill for readers of longer texts?', ['It deepens understanding of the author’s message across the whole work', 'Theme evaluation has no benefit for understanding a novel', 'It replaces the need to understand the plot', 'Only short texts can have meaningful themes'], 0)]),
M('Review: Algebra, Proportional Reasoning, and Geometry',
  'Ontario Grade 6 Number and Geometry strands review: this lesson revisits the distributive property, solving equations with fractions, proportional reasoning, multiplying and dividing integers, and classifying triangles.',
  [('Using the distributive property, what is 2 times (x + 5)?', ['2x + 5', '2x + 10', 'x + 10', '2x + 7'], 1),
   ('Solve for x: x/4 = 5.', ['x = 1.25', 'x = 9', 'x = 20', 'x = 4'], 2),
   ('If 4 notebooks cost $8, how much would 10 notebooks cost at the same rate?', ['$16', '$20', '$18', '$22'], 1),
   ('What is -6 times 3?', ['18', '-18', '-9', '9'], 1),
   ('Why is it useful to review algebra, proportional reasoning, and geometry skills together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Photosynthesis, Body Systems, and Physical Science',
   'Ontario Grade 6 Science review: this lesson revisits photosynthesis, symbiosis, the immune system, Newton’s laws, the periodic table, sound waves, and human impact on climate covered across recent lessons.',
   [('Photosynthesis allows plants to produce their own ___.', ['Food', 'Bones', 'Blood', 'Fur'], 0),
    ('Which body system defends against harmful microorganisms?', ['The immune system', 'The skeletal system', 'The muscular system only', 'The excretory system only'], 0),
    ('Newton’s first law describes how objects behave when ___.', ['No force acts on them', 'They are always accelerating with no cause', 'They have no mass', 'Forces have no effect on motion'], 0),
    ('Higher frequency sound waves generally produce a ___ pitch.', ['Lower', 'Higher', 'Silent', 'Unchanged'], 1),
    ('Why is it valuable to review photosynthesis, body systems, and physical science together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: World Empires and Global Challenges',
   'Ontario Grade 6 Social Studies review: this lesson revisits the fall of Rome, the Byzantine Empire, the Mongol Empire, the Aztec and Inca civilizations, colonialism, decolonization, and climate change as a global issue.',
   [('Which empire was centred in Constantinople and continued Roman and Greek traditions?', ['The Byzantine Empire', 'The Aztec Empire', 'The Inca Empire', 'The Mongol Empire'], 0),
    ('Which empire, founded by Genghis Khan, became the largest contiguous land empire in history?', ['The Byzantine Empire', 'The Mongol Empire', 'The Roman Empire', 'The Aztec Empire'], 1),
    ('Decolonization refers to colonized nations gaining ___.', ['Independence from colonial powers', 'New colonial rulers', 'No political changes at all', 'Complete isolation from the rest of the world'], 0),
    ('Climate change is considered a global issue because it requires ___.', ['International cooperation to address its causes and effects', 'No cooperation between countries', 'Action from only a single country', 'No connection to international relations'], 0),
    ('Why is it useful to review world empires and global challenges together?', ['It helps reinforce how historical patterns of power and cooperation connect to challenges today', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260716):
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
    _rebalance_answer_positions(g6_41_50)
    append_to(6, g6_41_50)
