#!/usr/bin/env python3
"""Phase 3: Grade 3, Days 31-40 (first batch of the full-year expansion
beyond the original 30-day summer program). Topics chosen to avoid any
overlap with the existing Day 1-30 set (see data/grade3.json for that
list) and to draw on Ontario Grade 3 curriculum strands not yet covered:
Growth and Changes in Plants (Science Life Systems), Physical Regions of
Canada and Communities in Canada 1780-1850 (Social Studies), Mass/Capacity/
Angles (Math Measurement/Geometry), and Media Literacy (Language).

videoUrl is intentionally left unset for every subject here -- per the
Phase 3 video-sourcing decision, fetch_video_ids.py (now day-range-aware,
see its docstring) fills these in automatically on its next daily run
rather than each one being manually searched during authoring.
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


g3_31_40 = [
day(31, [
L('Media Literacy: Advertising and Persuasion',
  'Ontario Grade 3 Media Literacy strand: advertisements are created to persuade people to buy or believe something, often using bright colours, catchy slogans, and famous people or characters.',
  [('An advertisement is mainly created to ___.', ['Inform without any goal', 'Persuade people to buy or believe something', 'Tell a fictional story only', 'Report the weather'], 1),
   ('Which is a common technique used in ads?', ['Long boring paragraphs', 'Catchy slogans and bright colours', 'No pictures at all', 'Only black and white text'], 1),
   ('Why might a cereal box show a cartoon character?', ['To make the cereal taste different', 'To catch children\'s attention and make it appealing', 'It is required by law', 'To explain the ingredients'], 1),
   ('A slogan is ___.', ['A long instruction manual', 'A short, catchy phrase that sticks in your memory', 'A type of food', 'A weather report'], 1),
   ('Being a smart media viewer means ___.', ['Believing every ad completely', 'Thinking critically about what an ad wants you to do', 'Ignoring all pictures', 'Never watching TV'], 1)]),
M('Rounding to the Nearest 10 and 100',
  'Ontario Grade 3 Number strand: rounding means changing a number to the nearest ten or hundred to make it easier to work with, based on whether the next digit is 5 or more.',
  [('Round 47 to the nearest 10.', ['40', '45', '50', '47'], 2),
   ('Round 82 to the nearest 10.', ['80', '85', '90', '82'], 0),
   ('Round 350 to the nearest 100.', ['300', '350', '400', '450'], 2),
   ('Round 124 to the nearest 100.', ['100', '120', '150', '200'], 0),
   ('When rounding, if the next digit is 5 or more, you round ___.', ['Down', 'Up', 'To zero', 'Not at all'], 1)]),
Sc('Growth and Changes in Plants: The Life Cycle',
   'Ontario Grade 3 Science Life Systems strand: plants grow through a life cycle -- seed, germination, seedling, mature plant, flower, and new seeds -- repeating the pattern.',
   [('What is the first stage of a plant\'s life cycle?', ['Flower', 'Seed', 'Mature plant', 'Fruit'], 1),
    ('Germination means ___.', ['A plant dying', 'A seed beginning to sprout and grow', 'A flower blooming', 'Leaves falling off'], 1),
    ('After a seedling grows, it becomes a ___.', ['Seed again', 'Mature plant', 'Rock', 'Root only'], 1),
    ('What does a mature plant produce to continue its life cycle?', ['More soil', 'Flowers and new seeds', 'Only leaves', 'Only roots'], 1),
    ('A plant\'s life cycle is best described as ___.', ['A straight line that never repeats', 'A repeating pattern from seed to seed', 'Random and unpredictable', 'The same as an animal\'s life cycle'], 1)]),
SS('Physical Regions of Canada: The Canadian Shield',
   'Ontario Grade 3 Social Studies People and Environments strand: the Canadian Shield is a huge region of ancient rock, forests, and lakes that covers much of central and northern Canada, including most of Ontario.',
   [('The Canadian Shield is mostly made of ___.', ['Sand dunes', 'Ancient rock', 'Ocean water', 'Ice sheets only'], 1),
    ('Which is a common feature of the Canadian Shield?', ['Deserts', 'Forests and lakes', 'Coral reefs', 'Tropical rainforests'], 1),
    ('Much of which province lies on the Canadian Shield?', ['British Columbia', 'Ontario', 'Prince Edward Island', 'Nova Scotia only'], 1),
    ('The Canadian Shield is one of Earth\'s ___.', ['Newest rock formations', 'Oldest rock formations', 'Youngest mountain ranges', 'Smallest islands'], 1),
    ('Why are there so many lakes in the Canadian Shield?', ['The rock holds water well, and ancient glaciers carved out basins', 'It never rains there', 'People dug them all by hand', 'It is a desert region'], 1)])]),

day(32, [
L('Reading: Making Connections',
  'Ontario Grade 3 Reading strand: strong readers make connections between a text and themselves (text-to-self), other texts (text-to-text), or the wider world (text-to-world) to deepen understanding.',
  [('A text-to-self connection means the reader ___.', ['Compares the text to another book', 'Relates the text to their own life or experiences', 'Ignores the text completely', 'Compares the text to a news event'], 1),
   ('A text-to-world connection means relating a text to ___.', ['Only the reader\'s pet', 'Events or issues happening in the wider world', 'A completely unrelated topic', 'Nothing at all'], 1),
   ('Why do readers make connections while reading?', ['To skip pages faster', 'To better understand and remember the text', 'To make the book longer', 'It is not useful'], 1),
   ('A text-to-text connection compares ___.', ['Two different books or stories', 'A book and the reader\'s shoes', 'Nothing in particular', 'Only pictures'], 0),
   ('If a story about moving to a new school reminds you of your own first day, that is a ___ connection.', ['Text-to-text', 'Text-to-self', 'Text-to-world', 'No connection'], 1)]),
M('Comparing and Ordering 3-Digit Numbers',
  'Ontario Grade 3 Number strand: students compare 3-digit numbers by looking at the hundreds digit first, then tens, then ones, and order sets of numbers from least to greatest.',
  [('Which is greater: 452 or 425?', ['452', '425', 'They are equal', 'Cannot tell'], 0),
   ('Order from least to greatest: 318, 138, 381.', ['138, 318, 381', '318, 138, 381', '381, 318, 138', '138, 381, 318'], 0),
   ('When comparing 3-digit numbers, which digit do you check first?', ['Ones', 'Tens', 'Hundreds', 'None of them'], 2),
   ('Which symbol means greater than?', ['<', '=', '>', '+'], 2),
   ('Which is smallest: 205, 250, or 502?', ['205', '250', '502', 'They are equal'], 0)]),
Sc('Growth and Changes in Plants: Pollination and Seed Dispersal',
   'Ontario Grade 3 Science Life Systems strand: pollination moves pollen from flower to flower (often by insects like bees), and seed dispersal spreads seeds by wind, animals, or water so new plants can grow in new places.',
   [('Which insect commonly helps pollinate flowers?', ['Ants', 'Bees', 'Ladybugs only', 'Spiders'], 1),
    ('Pollination is the process of ___.', ['Moving pollen between flowers to help make seeds', 'Watering plants', 'Cutting down trees', 'Removing leaves'], 0),
    ('Which is a way seeds can be dispersed?', ['They never move from the flower', 'Carried by wind, animals, or water', 'Only by human hands', 'They dissolve in soil'], 1),
    ('Why is seed dispersal important?', ['It lets new plants grow in new areas instead of competing with the parent plant', 'It stops plants from growing at all', 'It only helps animals eat', 'It has no purpose'], 0),
    ('A dandelion seed with a fluffy parachute is adapted for dispersal by ___.', ['Water', 'Wind', 'Fire', 'Digging'], 1)]),
SS('Physical Regions of Canada: The Prairies',
   'Ontario Grade 3 Social Studies People and Environments strand: the Prairies are a large, flat region in central Canada known for rich farmland, wheat and canola fields, and wide-open grasslands.',
   [('The Prairie region is known for being ___.', ['Mountainous and rocky', 'Flat, with rich farmland', 'Covered in rainforest', 'Made mostly of islands'], 1),
    ('Which crops are commonly grown on the Prairies?', ['Coconuts and bananas', 'Wheat and canola', 'Pineapples', 'Coffee beans'], 1),
    ('Which provinces are mainly part of the Canadian Prairies?', ['British Columbia and Ontario', 'Alberta, Saskatchewan, and Manitoba', 'Nova Scotia and PEI', 'Yukon and Nunavut'], 1),
    ('The Prairies are important to Canada mainly because of ___.', ['Fishing industries only', 'Farming and agriculture', 'Coral reefs', 'Volcanic activity'], 1),
    ('Before farming, the Prairies were mostly covered in ___.', ['Dense jungle', 'Natural grasslands', 'Glaciers year-round', 'Desert sand dunes'], 1)])]),

day(33, [
L('Grammar: Subject-Verb Agreement',
  'Ontario Grade 3 Writing strand: the subject and verb in a sentence must agree in number -- singular subjects take singular verbs (the dog runs) and plural subjects take plural verbs (the dogs run).',
  [('Which sentence has correct subject-verb agreement?', ['The dogs runs fast.', 'The dog run fast.', 'The dog runs fast.', 'The dogs is running fast.'], 2),
   ('Choose the correct verb: The cats ___ in the yard.', ['plays', 'play', 'playing', 'played playing'], 1),
   ('Choose the correct verb: She ___ to school every day.', ['walk', 'walks', 'walking', 'walked walk'], 1),
   ('A singular subject (one person or thing) usually takes a verb ending in ___.', ['-s', '-ing only', '-ed always', 'no ending ever'], 0),
   ('Which is correct: The children ___ happy.', ['is', 'was', 'are', 'am'], 2)]),
M('Measurement: Mass (Grams and Kilograms)',
  'Ontario Grade 3 Measurement strand: mass is measured in grams (g) for lighter objects and kilograms (kg) for heavier objects, using a balance scale to compare.',
  [('Which unit would best measure the mass of an apple?', ['Kilograms', 'Grams', 'Litres', 'Metres'], 1),
   ('Which unit would best measure the mass of a large dog?', ['Grams', 'Kilograms', 'Centimetres', 'Millilitres'], 1),
   ('1 kilogram equals how many grams?', ['10', '100', '1000', '10000'], 2),
   ('A balance scale is used to compare ___.', ['Length', 'Mass', 'Temperature', 'Time'], 1),
   ('Which is likely heavier?', ['A feather (grams)', 'A bicycle (kilograms)', 'They are the same', 'Cannot compare mass'], 1)]),
Sc('Structures: Strength and Stability',
   'Ontario Grade 3 Science Structures and Mechanisms strand: a strong structure resists breaking under a load, while a stable structure resists tipping over; shape (like triangles) and a wide base help both.',
   [('A structure that resists breaking under a load is considered ___.', ['Stable', 'Strong', 'Colourful', 'Small'], 1),
    ('A structure that resists tipping over is considered ___.', ['Strong', 'Stable', 'Fragile', 'Tall only'], 1),
    ('Which shape is known for adding strength to structures?', ['Circle', 'Triangle', 'Oval', 'Line'], 1),
    ('A wide base generally makes a structure more ___.', ['Weak', 'Stable', 'Invisible', 'Heavier only, with no benefit'], 1),
    ('Why do many bridges use triangle shapes in their design?', ['Triangles look nicer only', 'Triangles distribute weight evenly and resist bending', 'Triangles are cheaper to build always', 'Triangles are required by law'], 1)]),
SS('Physical Regions of Canada: The Rocky Mountains',
   'Ontario Grade 3 Social Studies People and Environments strand: the Rocky Mountains are a tall, rugged mountain range in western Canada, home to diverse wildlife and important for tourism.',
   [('The Rocky Mountains are located mainly in ___.', ['Eastern Canada', 'Western Canada', 'Northern Ontario', 'The Atlantic provinces'], 1),
    ('Which best describes the Rocky Mountains?', ['Flat and grassy', 'Tall and rugged', 'Covered entirely in sand', 'Underwater'], 1),
    ('Which province contains most of the Canadian Rockies?', ['British Columbia and Alberta', 'Ontario', 'Quebec', 'Manitoba'], 0),
    ('Why do many tourists visit the Rocky Mountains?', ['For scenic beauty, hiking, and wildlife viewing', 'There is nothing to see there', 'For deep-sea diving', 'For desert camping'], 0),
    ('Which animal might you expect to see in the Rocky Mountains?', ['Camel', 'Mountain goat', 'Penguin', 'Kangaroo'], 1)])]),

day(34, [
L('Writing: Descriptive Writing (Show, Don\'t Tell)',
  'Ontario Grade 3 Writing strand: descriptive writing uses sensory details -- sight, sound, smell, touch, taste -- to help readers picture a scene, showing an experience rather than just stating it plainly.',
  [('The phrase show, don\'t tell means writers should ___.', ['State facts plainly with no detail', 'Use vivid sensory details to help readers picture the scene', 'Avoid describing anything', 'Only use dialogue'], 1),
   ('Which sentence uses more descriptive, showing language?', ['The dog was happy.', 'The dog\'s tail wagged wildly as it barked with joy.', 'The dog was a dog.', 'It was a dog, and it was there.'], 1),
   ('Sensory details appeal to ___.', ['Only sight', 'The five senses: sight, sound, smell, touch, taste', 'Only sound', 'Nothing in particular'], 1),
   ('Which word is a strong, descriptive verb instead of a plain one?', ['Went', 'Sprinted', 'Was', 'Did'], 1),
   ('Why do writers use descriptive details?', ['To confuse the reader', 'To help the reader imagine the scene vividly', 'To make the writing shorter', 'It is not important'], 1)]),
M('Measurement: Capacity (Litres and Millilitres)',
  'Ontario Grade 3 Measurement strand: capacity is how much a container can hold, measured in millilitres (mL) for small amounts and litres (L) for larger amounts.',
  [('Which unit would best measure the capacity of a small juice box?', ['Litres', 'Millilitres', 'Kilograms', 'Metres'], 1),
   ('Which unit would best measure the capacity of a bathtub?', ['Millilitres', 'Litres', 'Grams', 'Centimetres'], 1),
   ('1 litre equals how many millilitres?', ['10', '100', '1000', '10000'], 2),
   ('Capacity measures ___.', ['How heavy something is', 'How much a container can hold', 'How long something is', 'How hot something is'], 1),
   ('Which container likely holds more?', ['A teaspoon', 'A bucket', 'They hold the same', 'Cannot compare'], 1)]),
Sc('Structures: Testing and Improving Designs',
   'Ontario Grade 3 Science Structures and Mechanisms strand: engineers test structures, identify weaknesses, and improve their designs through a repeated process of building, testing, and revising.',
   [('Why do engineers test structures before using them?', ['Testing is not necessary', 'To find weaknesses and make the design safer and stronger', 'To make the structure look different', 'To use more materials for no reason'], 1),
    ('The design process typically involves ___.', ['Building once and never changing it', 'Planning, building, testing, and improving', 'Guessing with no plan', 'Only drawing pictures'], 1),
    ('If a model bridge collapses during testing, what should happen next?', ['Give up on the project', 'Identify the weak point and redesign that part', 'Build the exact same bridge again unchanged', 'Ignore the failure'], 1),
    ('Which is an example of improving a structure\'s design?', ['Adding random unrelated decorations', 'Adding extra support where it was weak', 'Removing all support beams', 'Making it taller with no other changes'], 1),
    ('Testing and improving designs helps engineers ___.', ['Waste materials', 'Build safer, stronger structures', 'Avoid all planning', 'Make structures weaker on purpose'], 1)]),
SS('Physical Regions of Canada: Coastal Regions',
   'Ontario Grade 3 Social Studies People and Environments strand: Canada has coastal regions on the Atlantic (east), Pacific (west), and Arctic (north) oceans, each with unique climates, industries like fishing, and ways of life.',
   [('Canada has coastlines on which oceans?', ['Only the Pacific', 'The Atlantic, Pacific, and Arctic Oceans', 'Only the Indian Ocean', 'No oceans'], 1),
    ('Which industry is common in many Canadian coastal regions?', ['Desert farming', 'Fishing', 'Coal mining only', 'Space exploration'], 1),
    ('The Atlantic coast of Canada includes provinces such as ___.', ['Alberta and Saskatchewan', 'Nova Scotia and Newfoundland and Labrador', 'Ontario and Manitoba', 'Yukon only'], 1),
    ('The Pacific coast of Canada is found in which province?', ['British Columbia', 'Quebec', 'Prince Edward Island', 'Ontario'], 0),
    ('Why might people in coastal communities rely on the ocean?', ['For fishing, transportation, and trade', 'The ocean has no importance to them', 'Only for scenery, never for work', 'They avoid the ocean entirely'], 0)])]),

day(35, [
L('Reading: Sequencing Events',
  'Ontario Grade 3 Reading strand: sequencing means identifying the order in which events happen in a text, often signalled by words like first, next, then, and finally.',
  [('Which words often signal the order of events?', ['Red, blue, green', 'First, next, then, finally', 'Big, small, medium', 'Happy, sad, angry'], 1),
   ('Sequencing a story means identifying ___.', ['The characters\' names only', 'The order in which events happen', 'The title of the book', 'The author\'s name'], 1),
   ('If a recipe says to first mix the eggs, then add flour, which happens first?', ['Adding flour', 'Mixing the eggs', 'Both at the same time', 'Neither'], 1),
   ('Why is understanding sequence important when reading instructions?', ['It is not important', 'So you complete steps in the correct order', 'To make reading take longer', 'To skip steps'], 1),
   ('Which word usually signals the last event in a sequence?', ['First', 'Next', 'Finally', 'Then'], 2)]),
M('Geometry: Introducing Angles',
  'Ontario Grade 3 Geometry strand: an angle is formed where two lines meet; a right angle looks like the corner of a square, while angles smaller than a right angle are acute and larger ones are obtuse.',
  [('A right angle looks like the corner of a ___.', ['Circle', 'Square', 'Triangle only', 'Line'], 1),
   ('An angle smaller than a right angle is called ___.', ['Obtuse', 'Acute', 'Straight', 'Reflex'], 1),
   ('An angle larger than a right angle (but less than a straight line) is called ___.', ['Acute', 'Right', 'Obtuse', 'Zero'], 2),
   ('An angle is formed where ___ meet.', ['Two colours', 'Two lines or line segments', 'Two numbers', 'Two shapes only'], 1),
   ('Which everyday object has a right angle?', ['A ball', 'The corner of a book', 'A circle', 'A curved road'], 1)]),
Sc('Energy: Renewable vs Non-Renewable Sources',
   'Ontario Grade 3 Science Matter and Energy strand: renewable energy sources (like sun, wind, and water) can be replenished naturally, while non-renewable sources (like coal and oil) take millions of years to form and can run out.',
   [('Which is an example of a renewable energy source?', ['Coal', 'Sunlight', 'Oil', 'Natural gas'], 1),
    ('Which is an example of a non-renewable energy source?', ['Wind', 'Solar power', 'Coal', 'Water (hydro)'], 2),
    ('Renewable energy sources are considered renewable because they ___.', ['Never run out and can be naturally replenished', 'Take millions of years to form', 'Are always more expensive', 'Cannot be used for electricity'], 0),
    ('Wind turbines convert ___ into electricity.', ['Sunlight', 'Wind energy', 'Coal', 'Oil'], 1),
    ('Why do many people want to use more renewable energy?', ['It causes more pollution', 'It is generally cleaner and does not run out', 'It cannot be used for electricity', 'It is illegal'], 1)]),
SS('Communities in Canada, 1780-1850: Daily Life',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: early settler communities in Canada (1780-1850) grew much of their own food, made their own clothing and tools, and relied on family and neighbours for support.',
   [('In early Canadian settler communities (1780-1850), most families ___.', ['Bought all their food from large supermarkets', 'Grew much of their own food and made their own goods', 'Ordered everything online', 'Never worked'], 1),
    ('Why did early settlers rely heavily on neighbours?', ['Farming and building tasks were difficult to do alone', 'Neighbours were not needed at all', 'It was against the rules to be alone', 'They had modern machines to help'], 0),
    ('Which was a common daily task in early settler life?', ['Watching television', 'Chopping wood and tending crops', 'Driving to town', 'Video calling relatives'], 1),
    ('Clothing in early settler communities was often ___.', ['Bought from distant factories overnight', 'Made by hand at home from cloth or animal hides', 'Printed with a machine instantly', '3D printed'], 1),
    ('Compared to today, daily life in 1780-1850 required ___.', ['Much more manual labour for basic needs', 'Much less effort for basic needs', 'The exact same technology as today', 'No farming at all'], 0)])]),

day(36, [
L('Vocabulary: Synonyms and Antonyms',
  'Ontario Grade 3 Language strand: synonyms are words with similar meanings (happy/glad), and antonyms are words with opposite meanings (happy/sad); knowing both helps build stronger, more varied writing.',
  [('A synonym for happy is ___.', ['Sad', 'Glad', 'Angry', 'Tired'], 1),
   ('An antonym for happy is ___.', ['Glad', 'Joyful', 'Sad', 'Cheerful'], 2),
   ('Synonyms are words that have ___ meanings.', ['Opposite', 'Similar', 'No', 'Unrelated'], 1),
   ('Which pair are antonyms?', ['Big / large', 'Hot / cold', 'Small / tiny', 'Fast / quick'], 1),
   ('Why do writers use synonyms?', ['To repeat the exact same word every time', 'To add variety and avoid repeating the same word', 'To confuse readers', 'It has no purpose'], 1)]),
M('Data: Line Graphs',
  'Ontario Grade 3 Data strand: a line graph shows how data changes over time by connecting points with a line, useful for tracking things like temperature or growth.',
  [('A line graph is most useful for showing ___.', ['A single number with no comparison', 'How data changes over time', 'Only colours', 'Random unrelated facts'], 1),
   ('On a line graph, points are connected by a ___.', ['Bar', 'Line', 'Circle only', 'Nothing'], 1),
   ('Which would be a good use for a line graph?', ['Tracking daily temperature over a week', 'Listing students\' names', 'Showing a single favourite colour', 'A single yes/no answer'], 0),
   ('On a line graph, the horizontal line (x-axis) often shows ___.', ['Time', 'Colour', 'Taste', 'Smell'], 0),
   ('If a line graph line goes upward, the data is generally ___.', ['Decreasing', 'Increasing', 'Staying exactly the same always', 'Impossible to tell'], 1)]),
Sc('Space: The Sun, Earth, and Moon',
   'Ontario Grade 3 Science Earth and Space Systems strand: the Sun is a star that gives light and heat, Earth orbits the Sun, and the Moon orbits Earth, reflecting the Sun\'s light.',
   [('The Sun is best described as a ___.', ['Planet', 'Star', 'Moon', 'Comet'], 1),
    ('Earth orbits (travels around) the ___.', ['Moon', 'Sun', 'Another planet', 'Nothing'], 1),
    ('The Moon orbits ___.', ['The Sun directly', 'Earth', 'Mars', 'Nothing'], 1),
    ('The Moon appears to shine because it ___.', ['Makes its own light like the Sun', 'Reflects light from the Sun', 'Is on fire', 'Glows in the dark naturally'], 1),
    ('The Sun provides Earth with ___.', ['Light and heat', 'Only darkness', 'Only wind', 'Nothing important'], 0)]),
SS('Communities in Canada, 1780-1850: Transportation and Travel',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: before modern roads and vehicles, early Canadian settlers travelled by foot, horse, canoe, and boat, and waterways were especially important for trade and transportation.',
   [('Before cars, how did most early settlers travel long distances?', ['By airplane', 'By foot, horse, canoe, or boat', 'By subway', 'By bicycle only'], 1),
    ('Why were waterways so important to early settlers?', ['They were used for trade and transportation', 'They had no use at all', 'Only for drinking water', 'They were avoided completely'], 0),
    ('Which vehicle would NOT have existed in 1780-1850?', ['Canoe', 'Horse-drawn wagon', 'Automobile', 'Sailboat'], 2),
    ('Roads in early Canadian settlements were often ___.', ['Paved highways with streetlights', 'Rough dirt paths or trails', 'Underground tunnels', 'Made of glass'], 1),
    ('Travelling in 1780-1850 compared to today was generally ___.', ['Much slower', 'Much faster', 'Exactly the same speed', 'Instant'], 0)])]),

day(37, [
L('Writing: Persuasive Writing',
  'Ontario Grade 3 Writing strand: persuasive writing tries to convince the reader to agree with an opinion or take an action, using reasons and evidence to support the writer\'s point of view.',
  [('The goal of persuasive writing is to ___.', ['Simply list random facts', 'Convince the reader to agree with an opinion or take action', 'Tell a made-up story only', 'Confuse the reader'], 1),
   ('A strong persuasive piece includes ___.', ['No reasons at all', 'Clear reasons and evidence supporting the opinion', 'Only questions', 'Random unrelated topics'], 1),
   ('Which sentence is persuasive?', ['The sky is blue.', 'Everyone should recycle because it protects our planet.', 'The dog is brown.', 'It is Tuesday.'], 1),
   ('Persuasive writing often ends with a ___.', ['Random new topic', 'Call to action or strong closing statement', 'List of unrelated facts', 'A joke unrelated to the topic'], 1),
   ('Why might a writer use persuasive writing?', ['To convince others to support a cause or idea', 'To avoid sharing any opinion', 'To only describe scenery', 'It serves no purpose'], 0)]),
M('Estimating Sums and Differences',
  'Ontario Grade 3 Number strand: estimating means using rounded numbers to quickly find an approximate answer to an addition or subtraction problem, useful for checking if an exact answer makes sense.',
  [('Estimate: 198 + 302 is approximately ___.', ['200', '500', '600', '100'], 1),
   ('Estimating is useful because it helps you ___.', ['Get the exact answer with a calculator', 'Quickly check if an exact answer is reasonable', 'Avoid math completely', 'Make numbers disappear'], 1),
   ('To estimate 47 + 53, you might round to ___.', ['50 + 50 = 100', '40 + 50 = 90', '45 + 55 = 100 exactly with no rounding', '0 + 0'], 0),
   ('Estimate the difference: 401 - 199 is approximately ___.', ['400 - 200 = 200', '100', '600', '0'], 0),
   ('An estimated answer is ___.', ['Always exact', 'An approximate, reasonable answer', 'Always wrong', 'Never useful'], 1)]),
Sc('Space: Day and Night, and the Seasons',
   'Ontario Grade 3 Science Earth and Space Systems strand: day and night happen because Earth rotates (spins) on its axis, while the seasons change because Earth is tilted as it orbits the Sun.',
   [('Day and night happen because Earth ___.', ['Stops moving completely', 'Rotates (spins) on its axis', 'Changes shape', 'Moves closer to the Moon'], 1),
    ('One full rotation of Earth takes about ___.', ['One hour', 'One day (24 hours)', 'One year', 'One week'], 1),
    ('The seasons change mainly because ___.', ['Earth is tilted as it orbits the Sun', 'The Sun moves around Earth', 'The Moon controls temperature', 'Earth stops spinning in winter'], 0),
    ('One full orbit of Earth around the Sun takes about ___.', ['One day', 'One month', 'One year', 'Ten years'], 2),
    ('It is daytime on the side of Earth that ___.', ['Faces away from the Sun', 'Faces toward the Sun', 'Is closest to the Moon', 'Is spinning fastest'], 1)]),
SS('Communities in Canada, 1780-1850: Roles in the Community',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: early Canadian communities depended on workers with specific roles, such as blacksmiths, millers, farmers, and merchants, each contributing skills the community needed.',
   [('A blacksmith in an early settler community mainly worked with ___.', ['Metal, making tools and horseshoes', 'Only paperwork', 'Computers', 'Space travel'], 0),
    ('A miller\'s job was to ___.', ['Grind grain into flour', 'Repair shoes', 'Teach school', 'Deliver mail by airplane'], 0),
    ('Why did early communities need workers with many different roles?', ['Different skills met different needs the whole community relied on', 'One person could do every job alone', 'Roles were not important', 'Communities needed only farmers'], 0),
    ('A merchant in an early settlement mainly ___.', ['Bought and sold goods', 'Only farmed land', 'Repaired roads exclusively', 'Taught music only'], 0),
    ('Compared to today, early settlement jobs were ___.', ['Focused on directly meeting basic community needs', 'Identical to modern office jobs', 'Entirely done by machines', 'Nonexistent'], 0)])]),

day(38, [
L('Reading: Fact vs Opinion',
  'Ontario Grade 3 Reading strand: a fact is a statement that can be proven true or false, while an opinion is a personal belief or feeling that cannot be proven.',
  [('A fact is a statement that ___.', ['Can be proven true or false', 'Is always someone\'s feeling', 'Cannot be checked at all', 'Is always false'], 0),
   ('An opinion is ___.', ['A statement that can be measured exactly', 'A personal belief or feeling', 'Always agreed upon by everyone', 'The same as a fact'], 1),
   ('Which is a fact?', ['Pizza is the best food.', 'Water freezes at 0 degrees Celsius.', 'Summer is more fun than winter.', 'Blue is the prettiest colour.'], 1),
   ('Which is an opinion?', ['Dogs are better pets than cats.', 'A triangle has three sides.', 'Canada is a country.', 'Ice is frozen water.'], 0),
   ('Why is it important to tell facts and opinions apart?', ['It is not important', 'To understand what is proven versus what is someone\'s personal view', 'To only believe opinions', 'To ignore all facts'], 1)]),
M('Patterning: Number Patterns and Rules',
  'Ontario Grade 3 Algebra strand: a number pattern follows a rule, such as adding 3 each time, and identifying the rule lets you predict what number comes next.',
  [('What is the rule for the pattern 2, 5, 8, 11, ___?', ['Add 2', 'Add 3', 'Subtract 3', 'Multiply by 2'], 1),
   ('What comes next in the pattern 3, 6, 9, 12, ___?', ['13', '14', '15', '16'], 2),
   ('What is the rule for the pattern 20, 17, 14, 11, ___?', ['Add 3', 'Subtract 3', 'Add 4', 'Subtract 4'], 1),
   ('In the pattern 5, 10, 20, 40, the rule is ___.', ['Add 5', 'Multiply by 2', 'Subtract 5', 'Add 10 only once'], 1),
   ('Finding the rule in a pattern helps you ___.', ['Predict what number comes next', 'Make the pattern random', 'Remove all numbers', 'Nothing useful'], 0)]),
Sc('Matter: Changes of State',
   'Ontario Grade 3 Science Matter and Energy strand: matter can change state -- melting (solid to liquid), freezing (liquid to solid), evaporation (liquid to gas), and condensation (gas to liquid) -- usually caused by heating or cooling.',
   [('Melting is when a ___ changes to a liquid.', ['Gas', 'Solid', 'Liquid stays a liquid', 'Nothing'], 1),
    ('Freezing is when a liquid changes to a ___.', ['Gas', 'Solid', 'Different liquid', 'Nothing'], 1),
    ('Evaporation is when a liquid changes into a ___.', ['Solid', 'Gas', 'Rock', 'Different liquid'], 1),
    ('Condensation is when a gas changes into a ___.', ['Solid', 'Liquid', 'Nothing', 'Nothing changes'], 1),
    ('What usually causes ice to melt into water?', ['Cooling', 'Heating', 'Nothing changes it', 'Freezing further'], 1)]),
SS('Then and Now: Technology and Tools',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: comparing tools and technology from 1780-1850 to today shows how communication, farming, and travel have changed dramatically over time.',
   [('How did people mostly communicate over long distances in 1780-1850?', ['Text messages', 'Handwritten letters, which could take weeks to arrive', 'Video calls', 'Email'], 1),
    ('Farming in 1780-1850 mainly relied on ___.', ['Large automated machines', 'Hand tools and animal power', 'Robots', 'Drones'], 1),
    ('Compared to today, sending a message in 1780-1850 was ___.', ['Instant', 'Much slower', 'Exactly the same speed', 'Not possible at all'], 1),
    ('Which is an example of how technology has changed since 1780-1850?', ['We now have cars and the internet instead of horses and letters', 'Nothing has changed at all', 'People still travel by canoe only', 'Farming methods are identical'], 0),
    ('Comparing then and now helps us understand ___.', ['That change happens over time due to new inventions', 'That nothing ever changes', 'That old tools are always better', 'That technology never affects daily life'], 0)])]),

day(39, [
L('Grammar: Pronouns',
  'Ontario Grade 3 Writing strand: pronouns are words that take the place of nouns (he, she, it, they, we) to avoid repeating the same noun over and over.',
  [('A pronoun is a word that ___.', ['Describes an action', 'Takes the place of a noun', 'Is always a number', 'Connects two sentences only'], 1),
   ('Which word is a pronoun?', ['Table', 'Run', 'She', 'Blue'], 2),
   ('In the sentence Maria ate her lunch, the word her is a ___.', ['Noun', 'Pronoun', 'Verb', 'Adjective'], 1),
   ('Why do writers use pronouns?', ['To repeat the same noun many times', 'To avoid repeating the same noun and make writing smoother', 'To confuse readers', 'They serve no purpose'], 1),
   ('Which sentence correctly uses a pronoun?', ['Tom took Tom\'s book to Tom\'s class.', 'Tom took his book to his class.', 'Tom took a book to a class only.', 'Book took Tom to class.'], 1)]),
M('Fractions of a Set',
  'Ontario Grade 3 Number strand: a fraction can describe part of a group (a set), such as 2 out of 5 apples being red, written as 2/5.',
  [('If 3 out of 6 marbles are blue, what fraction of the marbles are blue?', ['3/6', '6/3', '3/3', '1/6'], 0),
   ('If 2 out of 4 pencils are sharpened, what fraction is that?', ['4/2', '2/4', '1/4', '4/4'], 1),
   ('A fraction of a set describes ___.', ['The whole set only', 'Part of a group of objects', 'A single object cut into pieces only', 'Nothing about groups'], 1),
   ('If 5 out of 10 stickers are stars, what fraction is NOT stars?', ['5/10', '10/10', '0/10', '10/5'], 0),
   ('If all 8 crayons in a box are red, what fraction of the set is red?', ['8/8', '0/8', '1/8', '4/8'], 0)]),
Sc('Habitats: Adaptations of Plants and Animals',
   'Ontario Grade 3 Science Life Systems strand: adaptations are special features or behaviours that help plants and animals survive in their specific habitat, such as thick fur in cold climates or sharp claws for digging.',
   [('An adaptation is a feature that helps a living thing ___.', ['Survive in its habitat', 'Move to a new planet', 'Avoid growing', 'Stop reproducing'], 0),
    ('Thick fur is an adaptation that helps animals survive in ___ climates.', ['Hot', 'Cold', 'Any climate equally', 'No particular climate'], 1),
    ('Sharp claws might be an adaptation that helps an animal ___.', ['Fly higher', 'Dig or catch food', 'Breathe underwater', 'Change colour'], 1),
    ('A cactus storing water in its stem is an adaptation to survive in a ___ habitat.', ['Rainforest', 'Desert', 'Ocean', 'Arctic'], 1),
    ('Why do different habitats lead to different adaptations?', ['Habitats have different challenges and resources that shape survival needs', 'All habitats are exactly the same', 'Adaptations happen completely randomly with no cause', 'Only animals adapt, never plants'], 0)]),
SS('Canada\'s Territories and the North',
   'Ontario Grade 3 Social Studies People and Environments strand: Canada\'s three territories -- Yukon, Northwest Territories, and Nunavut -- make up the northern part of the country, with cold climates and significant Indigenous populations.',
   [('How many territories does Canada have?', ['One', 'Two', 'Three', 'Five'], 2),
    ('Which of these is one of Canada\'s territories?', ['Nunavut', 'Ontario', 'Alberta', 'Quebec'], 0),
    ('Canada\'s territories are located mainly in the ___.', ['South', 'North', 'East coast only', 'Centre'], 1),
    ('The climate in Canada\'s northern territories is generally ___.', ['Tropical', 'Cold', 'Desert-like and hot', 'Mild year-round'], 1),
    ('Many communities in Canada\'s territories have significant ___ populations.', ['Indigenous', 'No permanent', 'Entirely non-Canadian', 'Underwater'], 0)])]),

day(40, [
L('Media Literacy: Comparing Print and Digital Texts',
  'Ontario Grade 3 Media Literacy strand: print texts (books, newspapers) and digital texts (websites, apps) both share information, but differ in how they are accessed, updated, and interacted with.',
  [('Which is an example of a print text?', ['A website', 'A newspaper', 'A mobile app', 'A video game'], 1),
   ('Which is an example of a digital text?', ['A printed book', 'A paper letter', 'A website', 'A newspaper'], 2),
   ('One advantage of digital texts is that they can often be ___.', ['Never updated', 'Updated quickly with new information', 'Only read once', 'Read only on paper'], 1),
   ('One advantage of print texts is that they ___.', ['Require electricity and a screen to read', 'Do not need a device or battery to read', 'Update themselves automatically', 'Are always digital'], 1),
   ('Both print and digital texts are created to ___.', ['Share information or stories with readers', 'Never be read by anyone', 'Confuse the audience', 'Replace all pictures'], 0)]),
M('Financial Literacy: Earning and Budgeting Basics',
  'Ontario Grade 3 Financial Literacy strand: people earn money through work or allowance, and a simple budget helps plan how much to spend and how much to save.',
  [('Earning money often comes from ___.', ['Doing work or chores', 'Wishing for it', 'Finding it randomly every day', 'It is never earned'], 0),
   ('A budget is a plan for ___.', ['Ignoring your money completely', 'How much money to spend and save', 'Spending all your money immediately', 'Never saving any money'], 1),
   ('If you earn $10 and save $4, how much do you have left to spend?', ['$4', '$6', '$10', '$14'], 1),
   ('Saving money means ___.', ['Spending it all right away', 'Setting some money aside for later', 'Giving it all away', 'Losing it'], 1),
   ('Why is budgeting a useful skill?', ['It helps you plan spending and saving wisely', 'It has no real purpose', 'It means spending without any plan', 'It only applies to adults'], 0)]),
Sc('Environment: Conservation and Recycling',
   'Ontario Grade 3 Science strand connecting to Structures and Matter: conservation means using resources wisely to protect the environment, and recycling turns used materials into new products instead of sending them to landfill.',
   [('Conservation means ___.', ['Wasting resources freely', 'Using resources wisely to protect the environment', 'Using as much as possible with no limits', 'Ignoring the environment'], 1),
    ('Recycling helps the environment by ___.', ['Sending more waste to landfill', 'Turning used materials into new products instead of waste', 'Creating more pollution', 'Destroying natural resources faster'], 1),
    ('Which is an example of recycling?', ['Throwing a plastic bottle in the garbage', 'Turning old paper into new paper products', 'Burning all waste', 'Burying everything permanently'], 1),
    ('Which of these is commonly recyclable?', ['Glass bottles', 'Food scraps mixed with garbage', 'Broken electronics thrown in a lake', 'Nothing is recyclable'], 0),
    ('Why is conservation important for the future?', ['It helps protect resources so they last for future generations', 'It has no benefit to anyone', 'It uses up resources faster', 'It only matters for one day'], 0)]),
SS('Ontario\'s Role in Confederation',
   'Ontario Grade 3 Social Studies Heritage and Identity strand: Ontario (formerly Canada West) was one of the four original provinces that joined together in 1867 to form the Dominion of Canada through Confederation.',
   [('In what year did Confederation create the Dominion of Canada?', ['1776', '1812', '1867', '1900'], 2),
    ('Ontario was one of how many original provinces at Confederation?', ['Two', 'Three', 'Four', 'Ten'], 2),
    ('Before Confederation, Ontario was known as ___.', ['Canada West', 'New France', 'Nunavut', 'British Columbia'], 0),
    ('Confederation joined the original provinces together to form ___.', ['A single city', 'The Dominion of Canada', 'A new ocean territory', 'A temporary alliance only'], 1),
    ('Why was Confederation an important event for Ontario and Canada?', ['It formally created Canada as a self-governing country', 'It had no lasting impact', 'It separated Ontario from Canada', 'It only affected one small town'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260709):
    """An audit (matching the pattern fix_answer_bias.py was originally
    written to catch in days 1-30) found this batch's first draft had 131
    of 200 correct answers on option B and zero on option D -- a kid could
    score ~65% just by always picking B. This reassigns each question's
    correct-answer slot via a shuffled round-robin (even across 0-3) and
    shuffles the wrong options into the remaining slots. Question and
    option TEXT are never touched, only which slot holds which option.
    Mutates `days` (and therefore the quiz tuples inside it) in place."""
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
    _rebalance_answer_positions(g3_31_40)
    append_to(3, g3_31_40)
