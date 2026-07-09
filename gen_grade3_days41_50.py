#!/usr/bin/env python3
"""Phase 3: Grade 3, Days 41-50 (second batch of the full-year expansion).
Topics chosen to avoid any overlap with the existing Day 1-40 set (see
data/grade3.json) and to draw on Ontario Grade 3 curriculum strands not
yet covered or only partially covered: the Solar System and constellations
(Earth and Space Systems), materials/forces on structures (Structures and
Mechanisms), classification of living things (Life Systems), the fur trade
and relations with Indigenous peoples (Heritage and Identity), and two more
physical regions of Canada (St. Lawrence Lowlands, Arctic).

As with Days 31-40: videoUrl is intentionally left unset for every
subject -- fetch_video_ids.py fills these in automatically on its next
daily run. No embedded double-quote characters are used anywhere in
question/summary/option text (gen_curriculum.py's serializer doesn't
escape them, so a literal " inside a string breaks the generated .ts --
learned the hard way on the Days 31-40 batch).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L3 = 'https://tvolearn.com/pages/grade-3-language'
M3 = 'https://tvolearn.com/pages/grade-3-mathematics'
S3 = 'https://tvolearn.com/pages/grade-3-science-and-technology'
SS3 = 'https://tvolearn.com/pages/grade-3-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 3 Language',
    'TVO Learn: Grade 3 Mathematics',
    'TVO Learn: Grade 3 Science & Technology',
    'TVO Learn: Grade 3 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L3, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M3, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S3, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS3, q)


g3_41_50 = [
day(41, [
L('Reading: Author\'s Purpose',
  'Ontario Grade 3 Reading strand: authors write for different purposes -- to persuade, to inform, or to entertain -- and identifying the purpose helps readers understand a text more deeply.',
  [('An author who writes to share facts about volcanoes is writing to ___.', ['Persuade', 'Inform', 'Entertain', 'Confuse'], 1),
   ('An author who writes a funny made-up story is mainly writing to ___.', ['Inform', 'Persuade', 'Entertain', 'Instruct'], 2),
   ('An author who writes an ad convincing you to buy a toy is writing to ___.', ['Entertain', 'Persuade', 'Inform only', 'Describe weather'], 1),
   ('A recipe is usually written to ___.', ['Entertain', 'Instruct or inform', 'Persuade', 'Confuse the reader'], 1),
   ('Why is it useful to know an author\'s purpose?', ['It helps you understand how to read and think about the text', 'It has no effect on reading', 'It only matters for pictures', 'It changes the page numbers'], 0)]),
M('Odd and Even Numbers',
  'Ontario Grade 3 Number strand: even numbers can be divided into two equal groups with nothing left over (2, 4, 6...), while odd numbers always have one left over (1, 3, 5...).',
  [('Which of these is an even number?', ['7', '10', '13', '9'], 1),
   ('Which of these is an odd number?', ['8', '12', '15', '20'], 2),
   ('A number is even if it can be divided into two equal groups with ___.', ['One left over', 'Nothing left over', 'Three left over', 'It cannot be divided'], 1),
   ('Which pattern shows only even numbers?', ['1, 3, 5, 7', '2, 4, 6, 8', '1, 2, 3, 4', '3, 6, 9, 12'], 1),
   ('Is 0 considered an even number?', ['No, it is odd', 'Yes, it is even', '0 is neither', 'Only sometimes'], 1)]),
Sc('Space: The Solar System',
   'Ontario Grade 3 Science Earth and Space Systems strand: the solar system includes the Sun and everything that orbits it, including eight planets, moons, and other objects like asteroids and comets.',
   [('The solar system is centred around the ___.', ['Moon', 'Sun', 'Earth', 'North Star'], 1),
    ('How many planets are in our solar system?', ['Six', 'Seven', 'Eight', 'Ten'], 2),
    ('Which planet is closest to the Sun?', ['Earth', 'Mercury', 'Mars', 'Venus'], 1),
    ('Which planet do humans live on?', ['Mars', 'Venus', 'Earth', 'Jupiter'], 2),
    ('Objects that orbit the Sun besides planets include ___.', ['Only clouds', 'Asteroids and comets', 'Only oceans', 'Nothing else'], 1)]),
SS('The Fur Trade in Early Canada',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: the fur trade was a major early economic activity in Canada, connecting European traders and Indigenous peoples who traded furs, especially beaver pelts, for goods.',
   [('The fur trade mainly involved trading ___.', ['Grain for money', 'Furs, especially beaver pelts, for goods', 'Fish for gold', 'Land for cattle'], 1),
    ('Who were the two main groups involved in the early Canadian fur trade?', ['Only European settlers', 'European traders and Indigenous peoples', 'Only sailors', 'Only farmers'], 1),
    ('Why was beaver fur especially valuable in the fur trade?', ['It was used to make popular hats in Europe', 'It was used as money directly', 'It could not be traded', 'It had no value'], 0),
    ('Indigenous peoples contributed important skills to the fur trade, such as ___.', ['Building airplanes', 'Trapping, guiding, and knowledge of the land', 'Mining coal', 'Operating factories'], 1),
    ('The fur trade helped shape early Canada by ___.', ['Creating trade routes and economic connections across the land', 'Stopping all travel completely', 'Having no lasting effect', 'Isolating all communities from each other'], 0)])]),

day(42, [
L('Grammar: Conjunctions',
  'Ontario Grade 3 Writing strand: conjunctions are joining words such as and, but, or, and because that connect words, phrases, or sentences together.',
  [('Which word is a conjunction?', ['Quickly', 'And', 'Purple', 'Jump'], 1),
   ('Choose the best conjunction: I wanted to play outside, ___ it started to rain.', ['and', 'but', 'because', 'quickly'], 1),
   ('Choose the best conjunction: I was tired ___ I went to bed early.', ['but', 'or', 'because', 'and'], 2),
   ('Conjunctions are used to ___.', ['End a sentence', 'Join words, phrases, or sentences together', 'Replace nouns', 'Show ownership'], 1),
   ('Which sentence correctly uses a conjunction?', ['I like apples and oranges.', 'I like apples, oranges.', 'I like, apples and oranges', 'I and like apples oranges'], 0)]),
M('Multiples and Skip Counting Review',
  'Ontario Grade 3 Number strand: a multiple of a number is what you get by multiplying it by a whole number, and skip counting is a quick way to list multiples in order.',
  [('Which of these is a multiple of 4?', ['6', '9', '12', '14'], 2),
   ('Which of these is a multiple of 3?', ['4', '7', '9', '10'], 2),
   ('Skip counting by 5s produces which list of numbers?', ['1, 2, 3, 4, 5', '5, 10, 15, 20', '2, 4, 6, 8', '5, 6, 7, 8'], 1),
   ('The first four multiples of 6 are ___.', ['6, 12, 18, 24', '6, 7, 8, 9', '1, 2, 3, 6', '6, 16, 26, 36'], 0),
   ('Multiples of 10 always end in the digit ___.', ['5', '1', '0', '2'], 2)]),
Sc('Space: Stars and Constellations',
   'Ontario Grade 3 Science Earth and Space Systems strand: stars are giant balls of hot gas that give off their own light, and a constellation is a recognizable pattern of stars that people have named, such as the Big Dipper.',
   [('A star is best described as a ___.', ['Cold rock', 'Giant ball of hot gas that gives off light', 'Piece of ice', 'Type of planet'], 1),
    ('A constellation is ___.', ['A single planet', 'A recognizable pattern of stars', 'A type of moon', 'A weather event'], 1),
    ('Which is a well-known constellation?', ['The Big Dipper', 'The Great Lake', 'The Rocky Mountains', 'The Grand Canyon'], 0),
    ('Stars appear to twinkle mainly because of ___.', ['Their own movement', 'Earth\'s atmosphere bending their light', 'They are actually blinking', 'They are very close to Earth'], 1),
    ('Why can we usually only see stars at night?', ['Stars turn off during the day', 'The Sun\'s brightness outshines them during the day', 'Stars move away during the day', 'Stars are only made at night'], 1)]),
SS('Communities in Canada, 1780-1850: Relations with Indigenous Peoples',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: early relationships between settlers and Indigenous peoples included both cooperation, such as trading and sharing knowledge, and conflict, especially over land and resources.',
   [('Indigenous peoples often helped early settlers by sharing ___.', ['Nothing at all', 'Knowledge of the land, farming, and survival skills', 'Only money', 'Modern technology'], 1),
    ('Relationships between settlers and Indigenous peoples in this period included ___.', ['Only conflict, never cooperation', 'Both cooperation, such as trade, and conflict', 'Only cooperation, never conflict', 'No contact at all'], 1),
    ('A major source of conflict between settlers and Indigenous peoples was often ___.', ['Weather patterns', 'Land and resources', 'Language lessons', 'Farming tools only'], 1),
    ('Trade between settlers and Indigenous peoples often involved exchanging ___.', ['Furs and goods', 'Nothing of value', 'Only stories', 'Modern currency'], 0),
    ('Learning about this history helps students understand ___.', ['That Canada\'s early history involved complex relationships between different peoples', 'That history is unimportant', 'That only one group shaped early Canada', 'That nothing from this era matters today'], 0)])]),

day(43, [
L('Writing: Compare and Contrast Essay',
  'Ontario Grade 3 Writing strand: a compare and contrast piece explains how two things are similar and different, often using words like both, similarly, however, and unlike.',
  [('A compare and contrast essay explains ___.', ['Only how two things are the same', 'How two things are similar and different', 'Only how two things are different', 'A single made-up story'], 1),
   ('Which word signals a similarity between two things?', ['However', 'Unlike', 'Similarly', 'But'], 2),
   ('Which word signals a difference between two things?', ['Both', 'Similarly', 'Also', 'However'], 3),
   ('Comparing dogs and cats, a similarity might be that both ___.', ['Bark loudly', 'Are common pets', 'Live only in water', 'Cannot be trained'], 1),
   ('Why do writers use compare and contrast writing?', ['To help readers understand relationships between two topics', 'To confuse the reader on purpose', 'To avoid describing anything', 'It serves no purpose'], 0)]),
M('Measurement: Temperature',
  'Ontario Grade 3 Measurement strand: temperature is measured in degrees Celsius (°C) in Canada using a thermometer, with 0°C being the freezing point of water and 100°C being the boiling point.',
  [('Temperature in Canada is commonly measured in ___.', ['Kilograms', 'Degrees Celsius', 'Litres', 'Metres'], 1),
   ('Water freezes at ___ degrees Celsius.', ['0', '50', '100', '32'], 0),
   ('Water boils at ___ degrees Celsius.', ['0', '50', '100', '212'], 2),
   ('Which tool is used to measure temperature?', ['Ruler', 'Thermometer', 'Scale', 'Clock'], 1),
   ('Which temperature would feel like a cold winter day in Ontario?', ['30 degrees Celsius', '-10 degrees Celsius', '100 degrees Celsius', '50 degrees Celsius'], 1)]),
Sc('Structures: Materials and Their Properties',
   'Ontario Grade 3 Science Structures and Mechanisms strand: builders choose materials for structures based on properties like strength, flexibility, and waterproofing, since different materials suit different jobs.',
   [('Which property describes how well a material resists breaking?', ['Strength', 'Colour', 'Smell', 'Taste'], 0),
    ('A material that bends easily without breaking is described as ___.', ['Rigid', 'Flexible', 'Waterproof', 'Transparent'], 1),
    ('Why might a builder choose a waterproof material for a roof?', ['To keep rain from getting inside the structure', 'To make the roof heavier for no reason', 'Waterproofing has no purpose', 'To make the structure invisible'], 0),
    ('Which material would likely be a poor choice for a building\'s foundation?', ['Concrete', 'Steel', 'Tissue paper', 'Solid rock'], 2),
    ('Choosing the right material for a structure\'s job is important because ___.', ['Different materials have different strengths and weaknesses suited to different tasks', 'All materials work equally well for every job', 'Material choice does not matter at all', 'Only colour matters when choosing materials'], 0)]),
SS('Physical Regions of Canada: The St. Lawrence Lowlands',
   'Ontario Grade 3 Social Studies People and Environments strand: the St. Lawrence Lowlands is a fertile, flat region along the St. Lawrence River and Great Lakes, home to some of Canada\'s largest cities and richest farmland.',
   [('The St. Lawrence Lowlands region is known for ___.', ['Fertile farmland and major cities', 'Being mostly frozen year-round', 'Having no rivers nearby', 'Being entirely desert'], 0),
    ('Which body of water is closely connected to the St. Lawrence Lowlands?', ['The Pacific Ocean', 'The St. Lawrence River and Great Lakes', 'The Arctic Ocean', 'Hudson Bay only'], 1),
    ('Many of Canada\'s largest cities are located in or near ___.', ['The Arctic tundra', 'The St. Lawrence Lowlands', 'The open ocean', 'Remote mountain peaks'], 1),
    ('Farming thrives in the St. Lawrence Lowlands mainly because of its ___.', ['Rocky, infertile soil', 'Fertile soil and flat land', 'Constant snow cover', 'Lack of water'], 1),
    ('Compared to the Canadian Shield, the St. Lawrence Lowlands are generally ___.', ['Flatter and more fertile for farming', 'Made of the same ancient rock', 'Colder and less populated', 'Entirely mountainous'], 0)])]),

day(44, [
L('Vocabulary: Compound Words',
  'Ontario Grade 3 Language strand: a compound word is formed by joining two smaller words together to make a new word with its own meaning, such as sun + flower = sunflower.',
  [('A compound word is formed by joining ___.', ['A word and a number', 'Two smaller words together', 'A letter and a symbol', 'Two punctuation marks'], 1),
   ('Which of these is a compound word?', ['Happy', 'Butterfly', 'Quickly', 'Jump'], 1),
   ('Sun + flower makes the compound word ___.', ['Sunny', 'Sunflower', 'Flowery', 'Sunlight'], 1),
   ('Which pair of words could combine to form a compound word?', ['Cat and dog', 'Rain and bow', 'Blue and fast', 'Run and happy'], 1),
   ('Understanding compound words can help readers ___.', ['Figure out the meaning of a new word from its parts', 'Ignore new words completely', 'Only memorize spelling', 'Avoid reading longer words'], 0)]),
M('Geometry: Transformations (Slides, Flips, and Turns)',
  'Ontario Grade 3 Geometry strand: shapes can move through transformations -- a slide (translation) moves a shape without turning it, a flip (reflection) creates a mirror image, and a turn (rotation) spins a shape around a point.',
  [('A slide moves a shape ___.', ['By flipping it into a mirror image', 'In a straight direction without turning it', 'By spinning it in a circle', 'By making it disappear'], 1),
   ('A flip creates a shape that is a ___ of the original.', ['Mirror image', 'Exact copy in the same spot', 'Smaller version', 'Larger version'], 0),
   ('A turn moves a shape by ___.', ['Sliding it sideways only', 'Rotating it around a point', 'Making a mirror image', 'Erasing part of it'], 1),
   ('Which transformation is also called a translation?', ['Turn', 'Flip', 'Slide', 'Rotation'], 2),
   ('Which transformation is also called a reflection?', ['Slide', 'Flip', 'Turn', 'Translation'], 1)]),
Sc('Structures: Forces Acting on Structures',
   'Ontario Grade 3 Science Structures and Mechanisms strand: structures experience forces such as compression (pushing/squeezing) and tension (pulling/stretching), and good designs handle these forces without breaking.',
   [('Compression is a force that ___.', ['Pulls or stretches a material', 'Pushes or squeezes a material', 'Has no effect on structures', 'Only affects liquids'], 1),
    ('Tension is a force that ___.', ['Pushes or squeezes a material', 'Pulls or stretches a material', 'Never occurs in structures', 'Only affects gases'], 1),
    ('A stretched rope experiences mainly ___.', ['Compression', 'Tension', 'No force at all', 'Only gravity'], 1),
    ('The legs of a table experience mainly ___ from the weight above them.', ['Tension', 'Compression', 'No force', 'Magnetism'], 1),
    ('Why do engineers study forces like compression and tension?', ['To design structures that can safely handle the forces acting on them', 'Forces are not important in design', 'To make structures weaker on purpose', 'Only for decoration purposes'], 0)]),
SS('Physical Regions of Canada: The Arctic',
   'Ontario Grade 3 Social Studies People and Environments strand: the Arctic is Canada\'s northernmost region, with a very cold climate, tundra landscape, and communities that have adapted their ways of life to the environment.',
   [('The Arctic region of Canada is best described as ___.', ['Warm and tropical', 'Very cold with a tundra landscape', 'Covered in dense rainforest', 'Mostly farmland'], 1),
    ('Tundra is a landscape with ___.', ['Tall dense forests', 'Low-growing plants and no trees, due to the cold climate', 'Tropical fruit trees', 'Sandy deserts'], 1),
    ('Communities in the Arctic have adapted their ways of life to ___.', ['A hot, humid climate', 'A cold climate and unique landscape', 'A rainy, mild climate', 'An environment identical to southern Canada'], 1),
    ('Which best describes daylight in parts of the Arctic during winter?', ['Extremely long periods of darkness', 'Exactly 12 hours of daylight every day', 'No difference from summer', 'Constant bright daylight'], 0),
    ('The Arctic is located in Canada\'s ___.', ['Far south', 'Far north', 'Central plains', 'Eastern coast only'], 1)])]),

day(45, [
L('Reading: Identifying Theme',
  'Ontario Grade 3 Reading strand: the theme of a story is the deeper message or lesson the author wants readers to take away, different from the plot, which is simply what happens.',
  [('The theme of a story is ___.', ['The exact list of events', 'The deeper message or lesson of the story', 'The name of the author', 'The number of chapters'], 1),
   ('Which is an example of a common story theme?', ['The main character has brown hair', 'Friendship and kindness matter', 'The story has five chapters', 'The book has a blue cover'], 1),
   ('Theme is different from plot because plot is ___.', ['The lesson of the story', 'What actually happens in the story', 'The author\'s name', 'The book\'s price'], 1),
   ('A story about a character learning to be honest likely has the theme of ___.', ['Honesty', 'Cooking', 'Weather', 'Sports scores'], 0),
   ('Why do authors include a theme in their stories?', ['To share a meaningful message or lesson with readers', 'Themes are never included in stories', 'To make books longer with no purpose', 'To confuse young readers'], 0)]),
M('Fractions: Adding Fractions with the Same Denominator',
  'Ontario Grade 3 Number strand: to add fractions with the same denominator, add the numerators and keep the denominator the same, such as 1/4 + 2/4 = 3/4.',
  [('1/5 + 2/5 = ?', ['3/5', '3/10', '2/5', '1/10'], 0),
   ('2/6 + 3/6 = ?', ['5/12', '5/6', '6/6', '1/6'], 1),
   ('When adding fractions with the same denominator, you ___.', ['Add both the numerators and denominators', 'Add the numerators and keep the denominator the same', 'Multiply the numerators', 'Only add the denominators'], 1),
   ('1/8 + 4/8 = ?', ['5/8', '5/16', '4/8', '1/8'], 0),
   ('3/10 + 3/10 = ?', ['6/20', '6/10', '3/10', '9/10'], 1)]),
Sc('Classifying Plants and Animals',
   'Ontario Grade 3 Science Life Systems strand: scientists classify (sort) living things into groups based on shared characteristics, such as sorting animals into mammals, birds, fish, reptiles, and amphibians.',
   [('Classifying living things means ___.', ['Sorting them into groups based on shared characteristics', 'Giving every living thing the same name', 'Ignoring their differences', 'Counting how many exist'], 0),
    ('Which group is classified as mammals?', ['Animals with feathers that lay eggs', 'Animals that typically have fur and feed milk to their young', 'Animals that only live underwater', 'Animals with no bones at all'], 1),
    ('Which is a characteristic of birds?', ['Fur and whiskers', 'Feathers and typically laying eggs', 'Living only underwater', 'Cold-blooded and scaly always'], 1),
    ('Fish are classified partly by their ability to ___.', ['Fly long distances', 'Breathe underwater using gills', 'Live only on land', 'Grow fur'], 1),
    ('Why do scientists classify living things into groups?', ['It helps organize and understand the natural world more clearly', 'It has no real purpose', 'To make studying life more confusing', 'Classification is random with no reason'], 0)]),
SS('Map Skills: Legends, Symbols, and the Compass Rose',
   'Ontario Grade 3 Social Studies People and Environments strand: maps use a legend (key) to explain symbols, and a compass rose to show direction, helping readers interpret the information a map presents.',
   [('A map legend (or key) is used to ___.', ['Explain what the symbols on a map mean', 'Show the map\'s price', 'List the mapmaker\'s name only', 'Replace the need for a title'], 0),
    ('A compass rose on a map shows ___.', ['Temperature', 'Direction (north, south, east, west)', 'Population size', 'The map\'s age'], 1),
    ('If a map symbol of a tent means campground, that information comes from the ___.', ['Compass rose', 'Legend', 'Scale bar', 'Title only'], 1),
    ('On a standard map with a compass rose, north is usually ___.', ['At the bottom', 'At the top', 'On the left', 'On the right'], 1),
    ('Why are legends and compass roses important map features?', ['They help readers understand and navigate the information shown on a map', 'They are just decorations with no purpose', 'They replace the need for any map details', 'Maps cannot include them together'], 0)])]),

day(46, [
L('Writing: Journal and Diary Entries',
  'Ontario Grade 3 Writing strand: a journal or diary entry is a personal piece of writing, usually dated, where the writer reflects on their day, thoughts, or feelings in their own voice.',
  [('A journal entry is typically written in ___.', ['A formal business tone', 'The writer\'s own personal voice and reflections', 'Only a list format', 'A stranger\'s voice'], 1),
   ('Journal entries are usually organized by ___.', ['Random topics with no order', 'Date', 'Alphabetical order', 'Length only'], 1),
   ('Which is most likely to appear in a diary entry?', ['A weather forecast for next year', 'The writer\'s personal thoughts and feelings about their day', 'A recipe for soup', 'A math worksheet'], 1),
   ('Why might someone keep a journal?', ['To reflect on experiences and remember them later', 'It serves no purpose', 'Only teachers are allowed to write journals', 'To avoid thinking about anything'], 0),
   ('A journal entry is generally written in ___ person.', ['Third', 'First', 'Second', 'No particular'], 1)]),
M('Number: Expanded Form',
  'Ontario Grade 3 Number strand: expanded form breaks a number into the value of each digit, such as 347 = 300 + 40 + 7, showing what each place value represents.',
  [('What is 452 in expanded form?', ['400 + 50 + 2', '4 + 5 + 2', '450 + 2', '400 + 52'], 0),
   ('What is 700 + 20 + 6 in standard form?', ['726', '7206', '76', '7026'], 0),
   ('What is 813 in expanded form?', ['80 + 13', '800 + 10 + 3', '8 + 1 + 3', '810 + 3'], 1),
   ('Expanded form shows ___.', ['The value of each digit based on its place', 'Only the ones digit', 'A number multiplied by itself', 'A completely different number'], 0),
   ('What is 900 + 5 in standard form?', ['95', '905', '950', '90'], 1)]),
Sc('Energy: Heat and Temperature',
   'Ontario Grade 3 Science Matter and Energy strand: heat is a form of energy that flows from warmer objects to cooler ones, and temperature is a measurement of how hot or cold something is.',
   [('Heat energy flows from ___.', ['Cooler objects to warmer objects', 'Warmer objects to cooler objects', 'It does not flow at all', 'Only from the Sun to space'], 1),
    ('Temperature measures ___.', ['How much a material weighs', 'How hot or cold something is', 'The size of an object', 'The colour of an object'], 1),
    ('If you hold an ice cube, heat flows from ___.', ['The ice cube to your hand', 'Your hand to the ice cube', 'Nowhere, heat does not move', 'The air only'], 1),
    ('Which is a good conductor that transfers heat quickly?', ['Wood', 'Metal', 'Rubber', 'Foam'], 1),
    ('Why does a hot drink eventually cool down at room temperature?', ['Heat flows from the drink into the cooler surrounding air', 'The drink creates more heat over time', 'Temperature never changes', 'Cold flows into the drink'], 0)]),
SS('Comparing Government: Then and Now',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: government in early Canadian communities (1780-1850) was more local and limited, while today Canada has federal, provincial, and municipal governments with defined roles.',
   [('Government in early Canadian settlements was often more ___ than today.', ['Complex and centralized', 'Local and limited', 'Identical to today\'s system', 'Nonexistent'], 1),
    ('Today, Canada has how many main levels of government?', ['One', 'Two', 'Three', 'Five'], 2),
    ('Which is a level of government in Canada today?', ['Municipal', 'Only royal', 'Only village elders', 'None exist'], 0),
    ('Compared to today, early settler communities had ___ formal laws and services.', ['More', 'Fewer', 'The exact same number of', 'No difference in'], 1),
    ('Why is it useful to compare government then and now?', ['It helps us understand how communities and their needs have changed over time', 'It has no educational value', 'Government has never changed', 'It only matters for adults'], 0)])]),

day(47, [
L('Oral Communication: Active Listening',
  'Ontario Grade 3 Oral Communication strand: active listening means fully focusing on the speaker, showing attention through eye contact and body language, and asking questions to understand better.',
  [('Active listening means ___.', ['Thinking about something else while someone talks', 'Fully focusing on and understanding the speaker', 'Interrupting constantly', 'Ignoring the speaker'], 1),
   ('Which is a sign of active listening?', ['Looking at your phone', 'Making eye contact with the speaker', 'Talking over the speaker', 'Walking away'], 1),
   ('Asking a question after someone speaks can show that you ___.', ['Were not listening at all', 'Were engaged and want to understand more', 'Want to change the subject', 'Are bored'], 1),
   ('Why is active listening an important skill?', ['It helps you understand others and communicate effectively', 'It is not useful in daily life', 'It only matters in school', 'It means never speaking at all'], 0),
   ('Which body language shows you are NOT actively listening?', ['Nodding along', 'Looking away and playing with objects', 'Eye contact', 'Leaning in slightly'], 1)]),
M('Choosing the Best Graph for Data',
  'Ontario Grade 3 Data strand: different graphs suit different data -- bar graphs compare categories, line graphs show change over time, and pictographs use pictures to represent quantities.',
  [('Which graph is best for comparing how many students like each fruit?', ['Line graph', 'Bar graph', 'Neither works', 'A blank page'], 1),
   ('Which graph is best for showing temperature changes over a week?', ['Pictograph', 'Line graph', 'No graph needed', 'A single number'], 1),
   ('A pictograph represents data using ___.', ['Only numbers', 'Pictures or symbols', 'Colours with no meaning', 'Random shapes with no key'], 1),
   ('Why is choosing the right graph type important?', ['It helps clearly show and communicate the data', 'All graphs are exactly the same', 'It does not matter which graph is used', 'Graphs are never useful'], 0),
   ('Which type of graph connects data points with a line?', ['Bar graph', 'Pictograph', 'Line graph', 'Tally chart'], 2)]),
Sc('Matter: Properties of Materials',
   'Ontario Grade 3 Science Matter and Energy strand: materials have measurable properties such as mass (how much matter they contain) and volume (how much space they take up).',
   [('Mass measures ___.', ['How much space an object takes up', 'How much matter an object contains', 'The colour of an object', 'The temperature of an object'], 1),
    ('Volume measures ___.', ['How much matter something contains', 'How much space an object takes up', 'How heavy something feels only', 'The material\'s smell'], 1),
    ('Which tool could help measure the volume of a liquid?', ['A measuring cup', 'A thermometer', 'A ruler only', 'A clock'], 0),
    ('Two objects can have the same volume but different ___.', ['Names', 'Mass', 'Existence', 'Location only'], 1),
    ('Why do scientists measure properties like mass and volume?', ['To describe and compare materials accurately', 'These properties cannot be measured', 'It has no scientific use', 'Only artists need this information'], 0)]),
SS('Canada\'s Multicultural Identity',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: Canada is home to people from many different cultural backgrounds, and this diversity shapes communities through shared traditions, languages, and celebrations.',
   [('Multicultural means a place is home to ___.', ['Only one culture', 'People from many different cultural backgrounds', 'No cultural traditions at all', 'Only recent immigrants'], 1),
    ('Which is an example of cultural diversity in a community?', ['Everyone speaking only one language', 'Different languages, foods, and celebrations', 'No festivals of any kind', 'Identical traditions for everyone'], 1),
    ('Why might a community host a multicultural festival?', ['To celebrate and share different cultural traditions', 'To discourage diversity', 'It has no purpose', 'To separate cultural groups'], 0),
    ('Canada\'s multicultural identity has grown partly through ___.', ['Complete isolation from other countries', 'Immigration from many countries around the world', 'Banning new cultures', 'Staying exactly the same since 1867'], 1),
    ('Respecting cultural diversity helps communities by ___.', ['Building understanding and inclusion among different groups', 'Creating unnecessary conflict', 'It has no community benefit', 'Making communities less connected'], 0)])]),

day(48, [
L('Grammar: Capitalization Rules',
  'Ontario Grade 3 Writing strand: capital letters are used at the start of a sentence, for proper nouns (names of specific people, places, and things), and for the pronoun I.',
  [('A sentence should always begin with a ___.', ['Lowercase letter', 'Capital letter', 'Number', 'Question mark'], 1),
   ('Which word should be capitalized?', ['dog', 'toronto', 'happy', 'the'], 1),
   ('Proper nouns, like specific names of people or places, should be ___.', ['Never capitalized', 'Always capitalized', 'Capitalized only sometimes randomly', 'Written in numbers'], 1),
   ('Which sentence uses capitalization correctly?', ['my friend sam lives in ottawa.', 'My friend Sam lives in Ottawa.', 'My Friend sam Lives in ottawa.', 'my Friend Sam lives In ottawa'], 1),
   ('The pronoun referring to yourself, I, should ___.', ['Never be capitalized', 'Always be capitalized', 'Only be capitalized at the start of a sentence', 'Be written as a lowercase i always'], 1)]),
M('Patterning: Growing Patterns with Shapes',
  'Ontario Grade 3 Algebra strand: a growing pattern increases by a consistent rule at each step, such as adding one more shape each time, and can be shown with objects, pictures, or numbers.',
  [('If a pattern of squares goes 1, 3, 5, 7, what is the rule?', ['Add 1', 'Add 2', 'Add 3', 'Subtract 2'], 1),
   ('A growing pattern of triangles has 2, 4, 6 triangles in the first three steps. How many in the fourth step?', ['7', '8', '9', '10'], 1),
   ('In a growing pattern, each step usually ___ compared to the one before.', ['Stays exactly the same', 'Increases by a consistent rule', 'Decreases randomly', 'Has no relationship'], 1),
   ('If a pattern starts at 3 and grows by 3 each time, what are the first four terms?', ['3, 6, 9, 12', '3, 4, 5, 6', '3, 9, 27, 81', '3, 5, 7, 9'], 0),
   ('Growing patterns can be represented using ___.', ['Only spoken words', 'Objects, pictures, or numbers', 'Nothing visual', 'Only colours with no structure'], 1)]),
Sc('Endangered Species and Conservation',
   'Ontario Grade 3 Science Life Systems strand: an endangered species is a type of plant or animal at risk of disappearing, often due to habitat loss, and conservation efforts help protect them.',
   [('An endangered species is one that is ___.', ['Extremely common', 'At risk of disappearing entirely', 'Found only in zoos', 'Not affected by habitat changes'], 1),
    ('A common cause of species becoming endangered is ___.', ['Too much habitat available', 'Loss of habitat', 'Too many protections', 'Nothing affects species survival'], 1),
    ('Conservation efforts aim to ___.', ['Speed up habitat destruction', 'Protect species and their habitats', 'Ignore endangered species', 'Remove all wildlife protections'], 1),
    ('Which is an example of a conservation action?', ['Cutting down protected forests', 'Creating protected parks and reserves', 'Ignoring pollution', 'Removing all environmental rules'], 1),
    ('Why is protecting endangered species considered important?', ['To help maintain balance and biodiversity in ecosystems', 'It has no ecological importance', 'Endangered species have no role in nature', 'It only matters for pets'], 0)]),
SS('Protecting Natural Resources for the Future',
   'Ontario Grade 3 Social Studies People and Environments strand: natural resources like forests, water, and minerals must be used responsibly so they remain available for future generations, a practice known as sustainability.',
   [('Sustainability means using resources in a way that ___.', ['Uses them all up as fast as possible', 'Keeps them available for future generations', 'Ignores future needs completely', 'Has no long-term plan'], 1),
    ('Which is an example of a natural resource?', ['A shopping mall', 'Forests', 'A video game', 'A highway sign'], 1),
    ('Why might a community limit how much of a forest is logged each year?', ['To ensure the forest can regrow and remain a resource long-term', 'Logging has no effect on forests', 'To use up all the trees quickly', 'Forests do not need protection'], 0),
    ('Which action supports sustainable use of water resources?', ['Wasting water freely', 'Conserving water and preventing pollution', 'Polluting rivers without limits', 'Ignoring water resources entirely'], 1),
    ('Protecting natural resources today mainly benefits ___.', ['No one', 'Future generations as well as people today', 'Only people living right now', 'Only businesses'], 1)])]),

day(49, [
L('Reading: Using Graphic Organizers',
  'Ontario Grade 3 Reading strand: graphic organizers such as webs, charts, and Venn diagrams help readers visually organize information and ideas from a text to better understand and remember it.',
  [('A graphic organizer helps readers ___.', ['Ignore the text completely', 'Visually organize information and ideas', 'Skip important details', 'Avoid taking notes'], 1),
   ('A Venn diagram is especially useful for ___.', ['Listing events in order only', 'Comparing similarities and differences between two things', 'Measuring length', 'Drawing maps'], 1),
   ('A web (or mind map) graphic organizer is useful for ___.', ['Organizing ideas around a central topic', 'Only listing numbers', 'Showing only differences', 'Replacing reading entirely'], 0),
   ('Why might a student use a graphic organizer before writing a report?', ['To plan and organize their ideas clearly first', 'It has no benefit before writing', 'To avoid researching the topic', 'To make writing more confusing'], 0),
   ('Which is an example of a graphic organizer?', ['A Venn diagram', 'A calculator', 'A dictionary only', 'A pencil'], 0)]),
M('Multi-Step Word Problems',
  'Ontario Grade 3 Number strand: multi-step word problems require more than one operation (like addition and then subtraction) to solve, so students must carefully identify each step needed.',
  [('Sam has 24 stickers, gives away 6, then gets 10 more. How many does Sam have now?', ['18', '28', '34', '20'], 1),
   ('A shop had 50 apples, sold 20, then received 15 more. How many apples now?', ['30', '45', '35', '65'], 2),
   ('Solving a multi-step word problem requires ___.', ['Using only one operation always', 'Carefully identifying and completing each step needed', 'Guessing the answer randomly', 'Ignoring some of the information given'], 1),
   ('Mia read 12 pages Monday and 15 pages Tuesday. She wants to read 40 pages total. How many pages are left?', ['13', '27', '15', '40'], 0),
   ('Why is it helpful to underline key numbers in a word problem?', ['To keep track of important information needed to solve each step', 'It has no benefit', 'To make the problem harder', 'To skip reading the problem'], 0)]),
Sc('Simple Machines Review: Mechanical Advantage',
   'Ontario Grade 3 Science Structures and Mechanisms strand: mechanical advantage means a simple machine makes a task easier by reducing the force needed or changing the direction of the force applied.',
   [('Mechanical advantage means a simple machine ___.', ['Makes a task harder to complete', 'Makes a task easier by reducing needed force or changing its direction', 'Has no effect on force', 'Always requires electricity'], 1),
    ('Which simple machine helps lift heavy objects with less effort by using a sloped surface?', ['Pulley', 'Inclined plane', 'Screw', 'Lever'], 1),
    ('A lever provides mechanical advantage by ___.', ['Requiring more force to lift objects', 'Helping lift or move objects with less force using a pivot point', 'Only working underwater', 'Eliminating the need for any force'], 1),
    ('A pulley system can make lifting easier by ___.', ['Changing the direction of the force and sometimes reducing effort', 'Making objects heavier', 'Removing gravity entirely', 'Only working on flat ground'], 0),
    ('Why do humans use simple machines?', ['To make physical tasks easier and more efficient', 'Simple machines make tasks harder on purpose', 'They have no practical use', 'They only work in factories'], 0)]),
SS('Canadian Landmarks and Symbols',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: Canada has many recognizable landmarks and symbols, such as the CN Tower, Parliament Hill, the maple leaf, and the beaver, that represent its identity and heritage.',
   [('The CN Tower is a famous landmark located in ___.', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 1),
    ('Parliament Hill, where Canada\'s federal government meets, is located in ___.', ['Toronto', 'Ottawa', 'Calgary', 'Halifax'], 1),
    ('Which animal is a well-known symbol of Canada?', ['Lion', 'Beaver', 'Elephant', 'Kangaroo'], 1),
    ('Landmarks and symbols help represent a country\'s ___.', ['Weather patterns only', 'Identity and heritage', 'Population count', 'Currency value'], 1),
    ('Which of these is a Canadian landmark?', ['The Eiffel Tower', 'The CN Tower', 'The Great Wall', 'The Statue of Liberty'], 1)])]),

day(50, [
L('Media Literacy: Recognizing Bias',
  'Ontario Grade 3 Media Literacy strand: bias means a text or media source favours one side or opinion over another, so readers should notice whose viewpoint is being shown and whether other viewpoints are missing.',
  [('Bias in a text means ___.', ['The text is completely balanced', 'The text favours one side or opinion over another', 'The text contains no opinions at all', 'The text is always false'], 1),
   ('A smart reader who notices bias should ask ___.', ['Nothing, bias does not matter', 'Whose viewpoint is being shown and what might be missing', 'Only who wrote the title', 'How many pages the text has'], 1),
   ('Which is a sign that a text might be biased?', ['It only presents one side of an issue positively', 'It presents multiple balanced viewpoints', 'It lists only facts with sources', 'It has no opinions at all'], 0),
   ('Why is it useful to recognize bias in media?', ['To think critically and understand different perspectives', 'It is not useful to notice bias', 'To automatically believe everything read', 'To stop reading entirely'], 0),
   ('Comparing multiple sources on a topic can help readers ___.', ['Get a more balanced understanding', 'Become more confused for no reason', 'Only see one viewpoint', 'Avoid learning anything new'], 0)]),
M('Problem Solving: Choosing the Right Operation',
  'Ontario Grade 3 Number strand: solving a word problem well starts with deciding which operation -- addition, subtraction, multiplication, or division -- fits what the problem is asking.',
  [('A problem asks how many total cookies are in 4 bags of 6. Which operation fits best?', ['Addition', 'Multiplication', 'Subtraction', 'Division'], 1),
   ('A problem asks how many are left after giving some away. Which operation fits best?', ['Multiplication', 'Subtraction', 'Division', 'None of these'], 1),
   ('A problem asks how to split 20 candies evenly among 5 friends. Which operation fits best?', ['Addition', 'Subtraction', 'Division', 'Multiplication'], 2),
   ('A problem asks for the total of two separate groups combined. Which operation fits best?', ['Division', 'Multiplication', 'Addition', 'Subtraction'], 2),
   ('Why is it important to choose the correct operation before solving?', ['Using the wrong operation will likely lead to an incorrect answer', 'The operation chosen never matters', 'All operations give the same result', 'It only matters for large numbers'], 0)]),
Sc('Science Inquiry: The Scientific Method',
   'Ontario Grade 3 Science strand across all topics: the scientific method is a process scientists use -- asking a question, making a prediction, testing it, and drawing a conclusion -- to investigate the world.',
   [('The first step of the scientific method is usually ___.', ['Drawing a conclusion', 'Asking a question', 'Publishing a report', 'Building a final product'], 1),
    ('A prediction made before testing is called a ___.', ['Conclusion', 'Hypothesis', 'Observation only', 'Random guess with no reasoning'], 1),
    ('Testing a hypothesis usually involves ___.', ['Skipping any investigation', 'Conducting an experiment or investigation', 'Ignoring the question entirely', 'Guessing the final answer only'], 1),
    ('A conclusion in the scientific method is based on ___.', ['Random opinions with no evidence', 'The results and evidence gathered during testing', 'What someone assumed before starting', 'Nothing measurable'], 1),
    ('Why do scientists follow a consistent method for investigations?', ['To ensure results are reliable and can be checked or repeated', 'The method has no real benefit', 'To make discoveries less trustworthy', 'To avoid asking questions'], 0)]),
SS('Planning for My Community\'s Future',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: thinking about a community\'s future involves considering how population growth, the environment, and technology might shape decisions communities make together.',
   [('Community planning for the future often considers ___.', ['Only decisions from the distant past', 'Population growth, environment, and technology', 'Nothing about the environment', 'Random unrelated topics'], 1),
    ('Why might a growing community need to plan for more schools or services?', ['To meet the needs of a larger population over time', 'Growth never affects community needs', 'Planning is unnecessary for communities', 'Only large cities ever grow'], 0),
    ('Considering the environment in community planning helps ___.', ['Protect natural resources for the future', 'Ignore environmental impacts entirely', 'Make decisions with no lasting effect', 'Remove the need for parks and green spaces'], 0),
    ('New technology can shape a community\'s future by ___.', ['Changing how people work, travel, and communicate', 'Having no impact on daily life', 'Only affecting large cities', 'Making community planning unnecessary'], 0),
    ('Why is it valuable for students to think about their community\'s future?', ['It builds awareness of how choices today shape tomorrow', 'It has no connection to real life', 'Only adults can think about the future', 'The future is completely unpredictable and not worth considering'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260710):
    """Same technique as gen_grade3_days31_40.py's version -- see that file
    for the full rationale. Reassigns each question's correct-answer slot
    via a shuffled round-robin (even across 0-3) and shuffles the wrong
    options into the remaining slots. Question/option TEXT is never
    changed. Mutates `days` in place."""
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
    _rebalance_answer_positions(g3_41_50)
    append_to(3, g3_41_50)
