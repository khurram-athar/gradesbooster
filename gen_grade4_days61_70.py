#!/usr/bin/env python3
"""Phase 3 extension: Grade 4, Days 61-70 (second batch past the Day 60
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-60 set (see data/grade4.json
and gen_grade4_days51_60.py): analogies, alliteration, interjections,
theme, place value, 2-digit by 2-digit multiplication, rounding
decimals, polygon classification, Canadian biomes, camouflage, Earth's
rotation, buoyancy, ancient Maya and Nubia, early-society leadership,
and the Canadian Shield. Day 70 of every subject is a review lesson
synthesizing that subject's Days 61-69 topics.

Subject keys for Grade 4 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 4 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
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


g4_61_70 = [
day(61, [
L('Vocabulary: Analogies',
  'Grade 4 Language strand: an analogy compares two pairs of words that share the same kind of relationship, such as hot is to cold as up is to down.',
  [('An analogy compares two pairs of words that share the same ___.', ['Type of relationship', 'Number of letters', 'X unrelated to analogies', 'Spelling pattern'], 0),
   ('Which word completes the analogy: Bird is to nest as bee is to ___?', ['Hive', 'Web', 'X unrelated to the analogy', 'Burrow'], 0),
   ('Which word completes the analogy: Puppy is to dog as kitten is to ___?', ['Cat', 'Cow', 'X unrelated to the analogy', 'Foal'], 0),
   ('Hot is to cold as up is to ___?', ['Down', 'Sideways', 'X unrelated to the analogy', 'Around'], 0),
   ('Why are analogies useful for building vocabulary?', ['They help readers see how word meanings and relationships connect', 'Analogies have no connection to word meaning', 'X unrelated to vocabulary building', 'Analogies only test spelling, not meaning'], 0)]),
M('Place Value to 10,000',
  'Grade 4 Math strand: place value to 10,000 describes the value of each digit in a number based on its position -- ones, tens, hundreds, and thousands.',
  [('In the number 6,482, the digit 4 represents ___.', ['4 hundreds', '4 tens', 'X unrelated to place value', '4 thousands'], 0),
   ('What is the value of the 7 in 7,315?', ['7,000', '700', 'X unrelated to place value', '70'], 0),
   ('Which number has a 5 in the thousands place?', ['5,214', '2,514', 'X unrelated to place value', '1,254'], 0),
   ('What is 3,000 + 400 + 20 + 6 written as a standard number?', ['3,426', '3,246', 'X unrelated to place value', '3,624'], 0),
   ('Why is it useful to understand place value in large numbers?', ['It helps read, write, and compare numbers accurately', 'Place value has no effect on the meaning of a number', 'X unrelated to place value', 'Every digit in a number always has the same value'], 0)]),
Sc('Canadian Biomes: Forests, Wetlands, and Tundra',
   'Grade 4 Science strand: Canada contains several distinct biomes, including forests, wetlands, and tundra, each with its own climate, plants, and animals.',
   [('A biome is best described as a large region with a distinct ___.', ['Climate, plants, and animals', 'Type of rock only', 'X unrelated to biomes', 'Style of building'], 0),
    ('Which biome is found in Canada’s far north, with very cold temperatures and few trees?', ['Tundra', 'Wetland', 'X unrelated to biomes', 'Rainforest'], 0),
    ('A wetland is an area that is ___.', ['Covered by water for at least part of the year', 'Always completely dry', 'X unrelated to biomes', 'Located only underground'], 0),
    ('Which biome covers much of central and northern Ontario, with many coniferous and deciduous trees?', ['Forest', 'Tundra', 'X unrelated to biomes', 'Desert'], 0),
    ('Why do scientists study different biomes?', ['To understand how climate shapes the plants and animals living there', 'Biomes provide no useful scientific information', 'X unrelated to biomes', 'Every biome on Earth is exactly the same'], 0)]),
SS('Ancient Maya Civilization',
   'Grade 4 Social Studies strand: the ancient Maya built cities in Central America between about 2000 BCE and 1500 CE, known for their pyramids, writing system, and knowledge of astronomy.',
   [('The ancient Maya civilization was located in ___.', ['Central America', 'Northern Europe', 'X unrelated to the Maya', 'Southern Africa'], 0),
    ('The Maya built large stone structures known as ___.', ['Pyramids', 'Igloos', 'X unrelated to Maya architecture', 'Log cabins'], 0),
    ('The Maya developed a system of ___ to record dates and events.', ['Writing (hieroglyphs)', 'Money made only of paper', 'X unrelated to Maya achievements', 'Modern printing presses'], 0),
    ('The Maya were skilled observers of ___.', ['The stars and sky (astronomy)', 'Only underwater life', 'X unrelated to Maya knowledge', 'Modern machinery'], 0),
    ('Why do historians study the ruins of Maya cities today?', ['They reveal how the Maya lived, built, and organized their society', 'Maya ruins provide no historical information', 'X unrelated to studying history', 'The Maya left behind no evidence of their civilization'], 0)])]),
day(62, [
L('Figurative Language: Alliteration',
  'Grade 4 Language strand: alliteration is the repetition of the same beginning consonant sound in a series of nearby words, such as slippery snakes slither silently.',
  [('Alliteration is the repetition of the same ___ in nearby words.', ['Beginning consonant sound', 'Ending vowel sound', 'X unrelated to alliteration', 'Number of syllables'], 0),
   ('Which phrase is an example of alliteration?', ['Busy bees buzzed by', 'The sun was very hot', 'X unrelated to alliteration', 'The dog ran quickly'], 0),
   ('Which phrase is an example of alliteration?', ['Peter Piper picked peppers', 'The cat sat on the mat', 'X unrelated to alliteration', 'She walked to the store'], 0),
   ('Why might a poet use alliteration?', ['To create rhythm and make language more memorable', 'Alliteration has no effect on how a poem sounds', 'X unrelated to figurative language', 'To make a poem harder to read aloud'], 0),
   ('Which word best continues this alliteration pattern: Silly snakes slid ___?', ['Slowly', 'Away', 'X unrelated to alliteration', 'Loudly'], 0)]),
M('Multiplying 2-Digit by 2-Digit Numbers',
  'Grade 4 Math strand: multiplying a 2-digit number by another 2-digit number involves breaking each factor into tens and ones, then adding the partial products together.',
  [('When multiplying 2-digit numbers, each factor can be broken into ___.', ['Tens and ones', 'Only hundreds', 'X unrelated to multiplication', 'Only fractions'], 0),
   ('What is 12 × 13?', ['156', '146', 'X unrelated to the calculation', '136'], 0),
   ('What is 21 × 14?', ['294', '284', 'X unrelated to the calculation', '304'], 0),
   ('What is 15 × 15?', ['225', '215', 'X unrelated to the calculation', '235'], 0),
   ('Why is it helpful to break numbers into tens and ones before multiplying?', ['It makes multiplying large numbers more manageable in smaller steps', 'Breaking numbers apart makes multiplication impossible', 'X unrelated to multiplication strategies', 'It changes the value of the original numbers'], 0)]),
Sc('Animal Camouflage and Mimicry',
   'Grade 4 Science strand: camouflage helps an animal blend into its surroundings, while mimicry occurs when one species evolves to resemble another species, both as strategies for survival.',
   [('Camouflage helps an animal ___.', ['Blend into its surroundings to avoid predators', 'Attract as much attention as possible', 'X unrelated to camouflage', 'Grow larger than other animals'], 0),
    ('Mimicry occurs when one species ___.', ['Resembles another species for protection or advantage', 'Has no connection to any other species', 'X unrelated to mimicry', 'Changes location every single day'], 0),
    ('Which is an example of camouflage?', ['A polar bear’s white fur blending into snow', 'A peacock’s bright, colourful tail feathers', 'X unrelated to camouflage', 'A lion’s loud roar'], 0),
    ('Why might a harmless insect evolve to look like a stinging wasp?', ['To trick predators into avoiding it, an example of mimicry', 'Looking similar to another species provides no benefit', 'X unrelated to mimicry', 'Insects never resemble other species'], 0),
    ('How do camouflage and mimicry both help animals survive?', ['They help animals avoid predators or better catch prey', 'They make animals more visible to predators', 'X unrelated to animal survival strategies', 'They have no effect on an animal’s chances of survival'], 0)]),
SS('Ancient Nubia (Kingdom of Kush)',
   'Grade 4 Social Studies strand: ancient Nubia, home to the Kingdom of Kush, was located along the Nile River south of Egypt and became known for its skilled ironworkers, pyramids, and trade in gold.',
   [('The ancient Kingdom of Kush was located ___.', ['Along the Nile River, south of Egypt', 'In Central America', 'X unrelated to Nubia', 'In Northern Europe'], 0),
    ('Nubia became especially well known for its skill in working with ___.', ['Iron', 'Plastic', 'X unrelated to Nubian achievements', 'Rubber'], 0),
    ('Like ancient Egypt, the Kingdom of Kush built ___.', ['Pyramids', 'Skyscrapers', 'X unrelated to Nubian architecture', 'Log cabins'], 0),
    ('Nubia traded valuable resources such as ___ with neighbouring regions.', ['Gold', 'Modern currency', 'X unrelated to Nubian trade', 'Plastic goods'], 0),
    ('Why is it important to learn about ancient Nubia alongside ancient Egypt?', ['It shows another powerful African civilization with its own rich history', 'Nubia had no history worth studying', 'X unrelated to ancient African civilizations', 'Only Egypt existed in ancient Africa'], 0)])]),
day(63, [
L('Grammar: Interjections',
  'Grade 4 Language strand: an interjection is a word or phrase that expresses strong emotion, such as Wow! or Ouch!, and is often followed by an exclamation mark.',
  [('An interjection is a word that expresses ___.', ['Strong emotion', 'A complete action', 'X unrelated to interjections', 'A location in a sentence'], 0),
   ('Which word is an interjection?', ['Wow', 'Jump', 'X unrelated to interjections', 'Table'], 0),
   ('An interjection is often followed by ___.', ['An exclamation mark', 'A semicolon', 'X unrelated to punctuation', 'Quotation marks only'], 0),
   ('Which sentence contains an interjection?', ['Ouch! That really hurt.', 'The dog ran across the yard.', 'X unrelated to interjections', 'She read the book quietly.'], 0),
   ('Why might a writer use an interjection in dialogue?', ['To show a character’s strong feeling or reaction', 'Interjections never appear in dialogue', 'X unrelated to interjections', 'To replace the need for any punctuation'], 0)]),
M('Rounding Decimals',
  'Grade 4 Math strand: rounding decimals means adjusting a decimal number to a nearby, simpler value, such as rounding to the nearest whole number or nearest tenth.',
  [('Rounding a decimal means adjusting it to a nearby, simpler ___.', ['Value', 'Shape', 'X unrelated to rounding', 'Colour'], 0),
   ('What is 4.7 rounded to the nearest whole number?', ['5', '4', 'X unrelated to the calculation', '6'], 0),
   ('What is 2.3 rounded to the nearest whole number?', ['2', '3', 'X unrelated to the calculation', '1'], 0),
   ('What is 6.85 rounded to the nearest tenth?', ['6.9', '6.8', 'X unrelated to the calculation', '7.0'], 0),
   ('Why might someone round a decimal number in everyday life?', ['To make an estimate or simplify a number quickly', 'Rounding decimals serves no practical purpose', 'X unrelated to rounding', 'Rounding always makes a number less accurate for every purpose'], 0)]),
Sc('Space: Earth’s Rotation and the Day/Night Cycle',
   'Grade 4 Science strand: Earth rotates on its axis once approximately every 24 hours, and this rotation causes the cycle of day and night.',
   [('Earth’s rotation on its axis takes approximately ___.', ['24 hours', '24 minutes', 'X unrelated to Earth’s rotation', 'One year'], 0),
    ('Day and night occur because Earth ___.', ['Rotates on its axis', 'Stops moving completely', 'X unrelated to day and night', 'Changes shape every day'], 0),
    ('When your part of Earth is facing the Sun, it is ___.', ['Daytime', 'Nighttime', 'X unrelated to Earth’s rotation', 'Always winter'], 0),
    ('Which term describes Earth spinning on its axis?', ['Rotation', 'Revolution around the Sun', 'X unrelated to Earth’s movement', 'Reflection'], 0),
    ('Why do different places on Earth experience day and night at different times?', ['Only half of the rotating Earth faces the Sun at any moment', 'The entire Earth always faces the Sun at once', 'X unrelated to Earth’s rotation', 'The Sun turns on and off each day'], 0)]),
SS('Early Societies: Tools and Technology',
   'Grade 4 Social Studies strand: early societies developed tools and technology, such as farming implements, pottery, and metalworking, to meet their daily needs and improve their way of life.',
   [('Early societies developed tools mainly to ___.', ['Meet daily needs, such as farming and building', 'Avoid doing any work at all', 'X unrelated to early technology', 'Compete in modern sporting events'], 0),
    ('Which material did many early societies learn to shape into tools and weapons?', ['Metal, such as bronze or iron', 'Plastic', 'X unrelated to early tools', 'Glass fibre'], 0),
    ('Pottery was an important early technology used mainly for ___.', ['Storing and carrying food and water', 'Building modern skyscrapers', 'X unrelated to pottery', 'Powering machines'], 0),
    ('How did farming tools, such as the plow, change early societies?', ['They allowed people to grow more food and support larger communities', 'Farming tools had no effect on early societies', 'X unrelated to early technology', 'They made growing food impossible'], 0),
    ('Why do historians study the tools used by early societies?', ['Tools reveal how people lived, worked, and solved problems', 'Studying tools provides no historical information', 'X unrelated to studying history', 'Early societies never used any tools'], 0)])]),
day(64, [
L('Reading: Identifying Theme',
  'Grade 4 Language strand: the theme of a story is its central message or lesson about life, which is different from the plot, or the events that happen.',
  [('The theme of a story is its ___.', ['Central message or lesson about life', 'List of characters only', 'X unrelated to theme', 'Number of chapters'], 0),
   ('How is theme different from plot?', ['Theme is the underlying message, while plot is the sequence of events', 'Theme and plot always mean exactly the same thing', 'X unrelated to theme', 'Plot is the message and theme is the setting'], 0),
   ('A story about a character who learns to be honest after telling a lie likely has a theme about ___.', ['Honesty', 'Cooking', 'X unrelated to the story’s theme', 'Travel'], 0),
   ('Why might two different stories share the same theme, such as courage?', ['Different plots and characters can still teach a similar life lesson', 'Themes can never repeat across different stories', 'X unrelated to identifying theme', 'Every story must have a completely unique theme'], 0),
   ('Which question would best help a reader identify a story’s theme?', ['What lesson does this story teach about life?', 'How many pages does this story have?', 'X unrelated to identifying theme', 'What colour is the book’s cover?'], 0)]),
M('Estimating Products and Quotients',
  'Grade 4 Math strand: estimating products and quotients involves rounding numbers before multiplying or dividing to quickly predict a reasonable answer.',
  [('Estimating a product or quotient means ___.', ['Rounding numbers first to quickly predict a reasonable answer', 'Calculating the exact answer with no rounding', 'X unrelated to estimation', 'Ignoring the numbers completely'], 0),
   ('Which is the best estimate for 29 × 4?', ['120', '90', 'X unrelated to the estimate', '200'], 0),
   ('Which is the best estimate for 58 ÷ 6?', ['10', '5', 'X unrelated to the estimate', '20'], 0),
   ('To estimate 19 × 21, you might round to ___.', ['20 × 20', '10 × 10', 'X unrelated to estimating this product', '19 × 30'], 0),
   ('Why is estimating useful before solving a multiplication or division problem?', ['It helps check whether the exact answer is reasonable', 'Estimating never helps with checking an answer', 'X unrelated to estimation', 'Estimating always gives the exact same result as calculating'], 0)]),
Sc('Matter: Why Objects Float or Sink (Buoyancy Basics)',
   'Grade 4 Science strand: whether an object floats or sinks in water depends on its buoyancy, which compares the object’s weight to the weight of the water it displaces.',
   [('Buoyancy refers to the ability of an object to ___.', ['Float in a liquid such as water', 'Change colour underwater', 'X unrelated to buoyancy', 'Dissolve completely in water'], 0),
    ('An object generally sinks in water when it is ___.', ['Denser (heavier for its size) than water', 'Lighter for its size than water', 'X unrelated to sinking', 'Exactly the same temperature as water'], 0),
    ('Which of these would most likely float in water?', ['A small wooden block', 'A solid metal ball', 'X unrelated to floating', 'A heavy rock'], 0),
    ('Why can a large steel ship float, even though steel is denser than water?', ['Its hollow shape displaces enough water to support its weight', 'Steel always sinks with no exceptions', 'X unrelated to buoyancy', 'Ships are not actually made of steel'], 0),
    ('Why is understanding buoyancy useful in everyday life?', ['It helps explain how boats, life jackets, and other objects behave in water', 'Buoyancy has no real-world application', 'X unrelated to buoyancy', 'All objects behave identically in water'], 0)]),
SS('Early Societies: Leadership and Government Structures',
   'Grade 4 Social Studies strand: early societies organized leadership in different ways, from kings and pharaohs to councils of elders, to make decisions and maintain order.',
   [('Many early societies were led by a single powerful ruler, such as a ___.', ['King or pharaoh', 'Modern prime minister', 'X unrelated to early leadership', 'Elected mayor'], 0),
    ('Some early societies made decisions through a ___.', ['Council of elders or respected leaders', 'Coin toss with no discussion at all', 'X unrelated to early government', 'Group of strangers chosen at random'], 0),
    ('Why did early societies need some form of leadership or government?', ['To make decisions, resolve conflicts, and maintain order', 'Leadership served no purpose in early societies', 'X unrelated to early government structures', 'Early societies never needed any organization'], 0),
    ('In ancient Egypt, the pharaoh was believed to be ___.', ['A god-like ruler with great authority', 'An ordinary citizen with no power', 'X unrelated to Egyptian leadership', 'Chosen by a public vote every year'], 0),
    ('How did leadership structures in early societies differ from one another?', ['Some had a single ruler, while others relied on councils or shared leadership', 'Every early society used the exact same system of leadership', 'X unrelated to comparing early societies', 'Early societies had no leaders at all'], 0)])]),
day(65, [
L('Writing: Newspaper Report Writing',
  'Grade 4 Language strand: a newspaper report presents factual information about a recent event, answering the questions who, what, where, when, why, and how in a clear headline and opening paragraph.',
  [('A newspaper report is mainly meant to ___.', ['Present factual information about a recent event', 'Share a completely fictional made-up story', 'X unrelated to newspaper reports', 'Persuade readers to buy a product'], 0),
   ('A strong newspaper report usually answers ___.', ['Who, what, where, when, why, and how', 'Only the writer’s personal opinion', 'X unrelated to newspaper reports', 'A single random question'], 0),
   ('The headline of a newspaper report should ___.', ['Summarize the story in a short, attention-grabbing way', 'Never relate to the story’s content', 'X unrelated to headlines', 'Be longer than the entire article'], 0),
   ('Where is the most important information usually placed in a newspaper report?', ['Near the beginning, in the opening paragraph', 'Only at the very end of the article', 'X unrelated to newspaper structure', 'Hidden within the middle paragraphs'], 0),
   ('Why should a newspaper report stick to facts rather than opinions?', ['So readers can trust the information as accurate and unbiased', 'Facts are never important in a newspaper report', 'X unrelated to newspaper writing', 'Opinions are always more important than facts'], 0)]),
M('Classifying Polygons by Sides and Angles',
  'Grade 4 Math strand: polygons are classified by their number of sides and angles, and can be described as regular (equal sides and angles) or irregular (unequal sides and angles).',
  [('A polygon is classified based on its number of ___.', ['Sides and angles', 'Colours', 'X unrelated to classifying polygons', 'Curved edges'], 0),
   ('A polygon with five sides is called a ___.', ['Pentagon', 'Hexagon', 'X unrelated to polygon names', 'Octagon'], 0),
   ('A polygon with six sides is called a ___.', ['Hexagon', 'Pentagon', 'X unrelated to polygon names', 'Heptagon'], 0),
   ('A regular polygon has ___.', ['All sides and angles equal', 'No straight sides at all', 'X unrelated to regular polygons', 'A different number of sides each time'], 0),
   ('Which best describes an irregular polygon?', ['Its sides and angles are not all equal', 'It has no sides or angles at all', 'X unrelated to irregular polygons', 'It must always be a circle'], 0)]),
Sc('Weather: Cloud Types and What They Predict',
   'Grade 4 Science strand: clouds form in different shapes and heights, and identifying cloud types, such as cumulus, stratus, and cirrus, can help predict upcoming weather.',
   [('Clouds form when water vapour in the air ___.', ['Cools and condenses into tiny droplets', 'Instantly disappears', 'X unrelated to cloud formation', 'Freezes into solid rock'], 0),
    ('Fluffy, puffy clouds with flat bottoms are called ___ clouds.', ['Cumulus', 'Cirrus', 'X unrelated to cloud types', 'Nimbus only'], 0),
    ('Thin, wispy clouds high in the sky are called ___ clouds.', ['Cirrus', 'Cumulus', 'X unrelated to cloud types', 'Stratus only'], 0),
    ('Flat, grey clouds that cover the sky like a blanket are called ___ clouds.', ['Stratus', 'Cirrus', 'X unrelated to cloud types', 'Cumulus only'], 0),
    ('Why might meteorologists study cloud types?', ['Cloud shapes and heights can help predict upcoming weather', 'Cloud types provide no useful weather information', 'X unrelated to studying weather', 'All clouds always predict the exact same weather'], 0)]),
SS('The Canadian Shield: Formation and Landscape',
   'Grade 4 Social Studies strand: the Canadian Shield is a vast region of ancient rock covering much of central and northern Canada, shaped by glaciers and known for its lakes, forests, and mineral deposits.',
   [('The Canadian Shield is best described as a vast region of ___.', ['Ancient rock covering much of central and northern Canada', 'Flat farmland found only in southern Ontario', 'X unrelated to the Canadian Shield', 'Desert sand dunes'], 0),
    ('The landscape of the Canadian Shield was heavily shaped by ___.', ['Glaciers moving across the land long ago', 'Ocean waves along a tropical coastline', 'X unrelated to the Canadian Shield’s formation', 'Volcanic eruptions happening every year'], 0),
    ('The Canadian Shield is known for having many ___.', ['Lakes and forests', 'Sandy beaches only', 'X unrelated to the Canadian Shield', 'Skyscrapers'], 0),
    ('Why is the rock of the Canadian Shield considered especially old?', ['It formed billions of years ago, making it some of the oldest rock on Earth', 'It formed only a few years ago', 'X unrelated to the Canadian Shield', 'The rock is not actually old at all'], 0),
    ('Which of these regions of Canada would you find part of the Canadian Shield?', ['Much of Ontario and Quebec', 'Only Vancouver Island', 'X unrelated to the Canadian Shield’s location', 'Only Prince Edward Island'], 0)])]),
day(66, [
L('Spelling: Silent Letters',
  'Grade 4 Language strand: some English words contain silent letters that are written but not pronounced, such as the k in knee or the b in comb.',
  [('A silent letter is a letter that is ___.', ['Written but not pronounced', 'Always pronounced loudly', 'X unrelated to silent letters', 'Never written in a word'], 0),
   ('Which letter is silent in the word knee?', ['K', 'N', 'X unrelated to silent letters', 'E'], 0),
   ('Which letter is silent in the word comb?', ['B', 'C', 'X unrelated to silent letters', 'M'], 0),
   ('Which letter is silent in the word write?', ['W', 'R', 'X unrelated to silent letters', 'T'], 0),
   ('Why can silent letters make spelling tricky for readers?', ['A letter appears in the word but is not heard when the word is spoken', 'Silent letters are always pronounced exactly as written', 'X unrelated to spelling challenges', 'Silent letters never appear in the English language'], 0)]),
M('Measuring Capacity: Litres and Millilitres',
  'Grade 4 Math strand: capacity describes how much liquid a container can hold, and is measured in millilitres (mL) for small amounts and litres (L) for larger amounts.',
  [('Capacity describes how much ___ a container can hold.', ['Liquid', 'Weight', 'X unrelated to capacity', 'Length'], 0),
   ('Which unit would best measure the capacity of a large water bottle?', ['Litres', 'Kilometres', 'X unrelated to measuring capacity', 'Grams'], 0),
   ('Which unit would best measure a small spoonful of liquid medicine?', ['Millilitres', 'Litres', 'X unrelated to measuring capacity', 'Metres'], 0),
   ('How many millilitres are in 1 litre?', ['1,000 millilitres', '100 millilitres', 'X unrelated to this conversion', '10 millilitres'], 0),
   ('Why is it useful to know both litres and millilitres?', ['Litres suit larger amounts, while millilitres suit smaller, more precise amounts', 'Litres and millilitres always measure the exact same amount', 'X unrelated to measuring capacity', 'Only one of these units is ever used in real life'], 0)]),
Sc('Forces: Air Resistance and Motion',
   'Grade 4 Science strand: air resistance is a force that pushes against objects as they move through the air, slowing them down depending on their shape and speed.',
   [('Air resistance is a force that ___.', ['Pushes against an object moving through the air', 'Pulls every object straight down to the ground', 'X unrelated to air resistance', 'Only affects objects underwater'], 0),
    ('Which object would experience more air resistance while falling?', ['An open parachute', 'A small pebble', 'X unrelated to air resistance', 'A tightly folded piece of paper'], 0),
    ('Why does a flat sheet of paper fall more slowly than a crumpled ball of the same paper?', ['Its larger surface area creates more air resistance', 'Flat paper weighs much more than crumpled paper', 'X unrelated to air resistance', 'Air resistance has no effect on falling paper'], 0),
    ('How does air resistance affect a moving bicycle?', ['It pushes against the rider, making it harder to pedal quickly', 'It has no effect on how a bicycle moves', 'X unrelated to air resistance', 'It always speeds up the bicycle'], 0),
    ('Why might race car designers shape cars to reduce air resistance?', ['A streamlined shape lets the car move faster with less resistance', 'Reducing air resistance has no benefit for a moving car', 'X unrelated to air resistance', 'Race cars are designed to increase air resistance as much as possible'], 0)]),
SS('Canada’s National Parks and Protected Areas',
   'Grade 4 Social Studies strand: Canada has established national parks and other protected areas to preserve natural landscapes, wildlife, and ecosystems for future generations.',
   [('A national park is an area of land that is ___.', ['Protected to preserve its natural landscape and wildlife', 'Open for unlimited building and development', 'X unrelated to national parks', 'Used only for large-scale farming'], 0),
    ('Why does Canada create protected areas such as national parks?', ['To conserve natural environments and wildlife for future generations', 'Protected areas serve no environmental purpose', 'X unrelated to conservation', 'To ensure land is developed as quickly as possible'], 0),
    ('Which of these activities is commonly allowed in many Canadian national parks?', ['Hiking and camping', 'Large-scale industrial mining', 'X unrelated to national park activities', 'Building shopping malls'], 0),
    ('Banff National Park, one of Canada’s oldest national parks, is located in ___.', ['Alberta', 'Nova Scotia', 'X unrelated to Banff’s location', 'Prince Edward Island'], 0),
    ('How do national parks help protect biodiversity?', ['They preserve habitats where many plants and animals can continue to live', 'National parks have no connection to biodiversity', 'X unrelated to protecting the environment', 'National parks remove all wildlife from an area'], 0)])]),
day(67, [
L('Grammar: Direct Objects',
  'Grade 4 Language strand: a direct object is the noun or pronoun that receives the action of a verb in a sentence, answering the question what or whom.',
  [('A direct object is the part of a sentence that ___.', ['Receives the action of the verb', 'Performs the action of the verb', 'X unrelated to direct objects', 'Describes the setting of a sentence'], 0),
   ('In the sentence Maya kicked the ball, what is the direct object?', ['Ball', 'Maya', 'X unrelated to the direct object', 'Kicked'], 0),
   ('In the sentence The chef baked a cake, what is the direct object?', ['Cake', 'Chef', 'X unrelated to the direct object', 'Baked'], 0),
   ('A direct object answers which question about the verb?', ['What or whom', 'Where or when', 'X unrelated to direct objects', 'How often'], 0),
   ('In the sentence The dog chased the squirrel, what is the direct object?', ['Squirrel', 'Dog', 'X unrelated to the direct object', 'Chased'], 0)]),
M('Comparing Prices: Unit Rate and Best Value',
  'Grade 4 Math strand: comparing prices using unit rate means finding the cost of a single item or unit, which helps shoppers decide which option offers the best value.',
  [('A unit rate compares the cost of ___.', ['A single item or unit', 'An entire store’s total sales', 'X unrelated to unit rate', 'Only the tax on a purchase'], 0),
   ('If 4 apples cost 2 dollars, what is the unit rate per apple?', ['0.50 dollars per apple', '2 dollars per apple', 'X unrelated to this unit rate', '4 dollars per apple'], 0),
   ('A pack of 5 pencils costs 5 dollars, and a pack of 10 pencils costs 8 dollars. Which has the better unit rate?', ['The pack of 10 pencils', 'The pack of 5 pencils', 'X unrelated to comparing unit rates', 'Both packs have the exact same unit rate'], 0),
   ('Why is finding the unit rate helpful when shopping?', ['It helps shoppers compare prices fairly to find the best value', 'Unit rate makes it impossible to compare prices', 'X unrelated to comparing prices', 'The total price is always more useful than the unit rate'], 0),
   ('If 3 juice boxes cost 6 dollars, what is the cost per juice box?', ['2 dollars', '3 dollars', 'X unrelated to this unit rate', '6 dollars'], 0)]),
Sc('Structures: Why Shape Affects Strength (Triangles vs Squares)',
   'Grade 4 Science strand: the shape of a structure affects its strength, and triangles are especially strong because their fixed angles resist bending and twisting better than squares.',
   [('Triangles are considered a strong shape in structures because their angles ___.', ['Resist bending and twisting under pressure', 'Change shape very easily under pressure', 'X unrelated to triangle strength', 'Have no effect on a structure’s strength'], 0),
    ('Compared to a triangle, a square shape is more likely to ___.', ['Collapse or change shape under pressure', 'Remain perfectly rigid under any pressure', 'X unrelated to comparing shapes', 'Support far more weight than a triangle'], 0),
    ('Why do builders often use triangular supports in bridges and towers?', ['Triangles distribute force evenly and resist bending', 'Triangles make a structure weaker and less stable', 'X unrelated to structural design', 'Triangular supports have no effect on strength'], 0),
    ('If you push on one corner of a square frame, what is likely to happen?', ['The square can shift into a different shape, such as a parallelogram', 'The square remains rigid and never changes shape', 'X unrelated to testing shape strength', 'The square becomes a triangle automatically'], 0),
    ('Why might engineers test different shapes before building a structure?', ['To find the shape that provides the most strength and stability', 'Testing shapes provides no useful information for engineers', 'X unrelated to engineering design', 'All shapes provide exactly the same strength'], 0)]),
SS('Time Zones Across Canada',
   'Grade 4 Social Studies strand: because Canada spans such a wide area from east to west, it is divided into six time zones, meaning it can be a different time of day in different parts of the country at once.',
   [('Canada is divided into time zones because it ___.', ['Spans a very wide area from east to west', 'Is a very small country', 'X unrelated to Canada’s time zones', 'Has only one region with people living in it'], 0),
    ('How many time zones does Canada have?', ['Six', 'One', 'X unrelated to Canada’s time zones', 'Twelve'], 0),
    ('If it is 3:00 p.m. in Ontario (Eastern time), it is generally earlier in the day in ___.', ['British Columbia (Pacific time)', 'Newfoundland (Newfoundland time)', 'X unrelated to comparing time zones', 'A place in exactly the same time zone'], 0),
    ('Why might someone need to consider time zones when calling a friend in another province?', ['The time of day may be different in each province', 'Every province in Canada shares the exact same time', 'X unrelated to time zones', 'Time zones only matter for international travel'], 0),
    ('Time zones are generally organized based on a location’s ___.', ['Longitude (east-west position)', 'Latitude (north-south position) only', 'X unrelated to time zones', 'Population size'], 0)])]),
day(68, [
L('Reading: Skimming and Scanning for Information',
  'Grade 4 Language strand: skimming means quickly reading a text to get its general idea, while scanning means searching a text quickly for specific facts, such as a date or name.',
  [('Skimming a text means reading quickly to ___.', ['Get the general idea of the text', 'Memorize every single word', 'X unrelated to skimming', 'Find one exact fact only'], 0),
   ('Scanning a text means searching quickly for ___.', ['A specific piece of information', 'The entire meaning of the text', 'X unrelated to scanning', 'The author’s complete biography'], 0),
   ('Which strategy would be best for quickly finding a specific date in a long article?', ['Scanning', 'Skimming', 'X unrelated to finding a specific fact', 'Reading every single word carefully'], 0),
   ('Which strategy would be best for getting a quick overview of what a chapter is about?', ['Skimming', 'Scanning', 'X unrelated to getting an overview', 'Memorizing the chapter word for word'], 0),
   ('Why are skimming and scanning useful reading strategies?', ['They help readers find information efficiently without reading every word', 'These strategies always take longer than reading word for word', 'X unrelated to reading strategies', 'They prevent readers from understanding a text at all'], 0)]),
M('Tally Charts and Frequency Tables',
  'Grade 4 Math strand: a tally chart uses marks to record how often something occurs, and this data can be organized into a frequency table showing the total count for each category.',
  [('A tally chart uses marks to record ___.', ['How often something occurs', 'The exact size of an object', 'X unrelated to tally charts', 'The colour of an object'], 0),
   ('In tally marks, a group of five is usually shown as ___.', ['Four vertical lines with a line crossed through them', 'Five separate dots', 'X unrelated to tally marks', 'A single curved line'], 0),
   ('A frequency table organizes data by showing the ___ for each category.', ['Total count', 'Colour', 'X unrelated to frequency tables', 'Alphabetical order only'], 0),
   ('If a tally chart shows a group of 5, then a group of 5, then 2 more marks for a category, how many are recorded?', ['12', '10', 'X unrelated to this tally count', '14'], 0),
   ('Why might a survey use a tally chart while collecting data?', ['It makes it quick and easy to record and count responses', 'Tally charts make it impossible to count responses', 'X unrelated to collecting data', 'Tally charts can only be used for numbers larger than 100'], 0)]),
Sc('Electricity: Reading Simple Circuit Diagrams',
   'Grade 4 Science strand: a circuit diagram uses standard symbols to represent parts of an electric circuit, such as a battery, switch, and light bulb, showing how they are connected.',
   [('A circuit diagram uses symbols to represent ___.', ['The parts of an electric circuit and how they connect', 'The colours of the wires only', 'X unrelated to circuit diagrams', 'The weather conditions outside'], 0),
    ('Which symbol typically represents a battery in a circuit diagram?', ['A pair of parallel lines, one longer than the other', 'A perfect circle with no lines', 'X unrelated to circuit diagrams', 'A wavy line'], 0),
    ('In a circuit diagram, a switch symbol shows where the circuit can be ___.', ['Opened or closed to control the flow of electricity', 'Permanently broken with no way to reconnect it', 'X unrelated to switches', 'Filled with water'], 0),
    ('Why are standard symbols used in circuit diagrams instead of drawings of real objects?', ['They allow anyone to read and understand a circuit clearly and quickly', 'Standard symbols make circuits impossible to understand', 'X unrelated to circuit diagrams', 'Every country uses completely different, unrelated symbols'], 0),
    ('If a circuit diagram shows a break in the line connecting the parts, what does this likely mean?', ['The circuit is open and electricity cannot flow', 'The circuit is complete and functioning normally', 'X unrelated to reading circuit diagrams', 'The diagram contains no useful information'], 0)]),
SS('Natural Hazards in Canada (Floods, Forest Fires, Earthquakes)',
   'Grade 4 Social Studies strand: different regions of Canada face different natural hazards, such as floods near rivers, forest fires in dry forested areas, and earthquakes along the west coast.',
   [('A natural hazard is an event caused by nature that can ___.', ['Threaten people, property, or the environment', 'Never affect people in any way', 'X unrelated to natural hazards', 'Only occur in outer space'], 0),
    ('Areas near rivers are especially at risk of ___.', ['Flooding', 'Volcanic eruptions', 'X unrelated to river hazards', 'Earthquakes only'], 0),
    ('Dry, forested regions of Canada are especially at risk of ___.', ['Forest fires', 'Flooding from the ocean', 'X unrelated to forest hazards', 'Blizzards only'], 0),
    ('Which region of Canada is more likely to experience earthquakes?', ['The west coast, such as British Columbia', 'The flat Prairies', 'X unrelated to earthquake risk', 'The Atlantic coast only'], 0),
    ('Why is it useful for communities to understand the natural hazards in their region?', ['It helps them prepare and respond safely to potential emergencies', 'Understanding natural hazards provides no benefit to a community', 'X unrelated to natural hazards', 'Natural hazards never affect any Canadian community'], 0)])]),
day(69, [
L('Vocabulary: Connotation and Denotation',
  'Grade 4 Language strand: denotation is the exact dictionary meaning of a word, while connotation is the feeling or association a word carries beyond its literal meaning.',
  [('Denotation refers to a word’s ___.', ['Exact dictionary meaning', 'Emotional feeling only', 'X unrelated to denotation', 'Number of syllables'], 0),
   ('Connotation refers to the ___ a word carries beyond its literal meaning.', ['Feeling or association', 'Exact spelling', 'X unrelated to connotation', 'Number of letters'], 0),
   ('The words skinny and slim have similar denotations but different ___.', ['Connotations', 'Spellings', 'X unrelated to comparing these words', 'Pronunciations'], 0),
   ('Which word has a more positive connotation than stubborn?', ['Determined', 'Careless', 'X unrelated to comparing connotations', 'Messy'], 0),
   ('Why might a writer carefully choose words based on their connotation?', ['To create a specific feeling or impression for the reader', 'Connotation has no effect on how a reader feels', 'X unrelated to word choice', 'Every word carries exactly the same feeling'], 0)]),
M('Number Lines: Plotting Fractions and Decimals',
  'Grade 4 Math strand: fractions and decimals can be plotted on a number line to compare their values and see how they relate to whole numbers.',
  [('A number line can be used to ___.', ['Compare the values of fractions and decimals', 'Only show whole numbers greater than 100', 'X unrelated to number lines', 'Measure the weight of an object'], 0),
   ('On a number line from 0 to 1, where would 1/2 be plotted?', ['Exactly halfway between 0 and 1', 'Right next to 0', 'X unrelated to plotting fractions', 'Right next to 1'], 0),
   ('On a number line, which is closer to 1: 0.75 or 0.25?', ['0.75', '0.25', 'X unrelated to comparing these decimals', 'They are equally close to 1'], 0),
   ('Where would the fraction 3/4 be plotted on a number line between 0 and 1?', ['Closer to 1 than to 0', 'Closer to 0 than to 1', 'X unrelated to plotting this fraction', 'Exactly at 0'], 0),
   ('Why is it useful to plot fractions and decimals on the same number line?', ['It helps show how fractions and decimals relate to and compare with each other', 'Fractions and decimals can never be compared to one another', 'X unrelated to number lines', 'A number line can only show whole numbers'], 0)]),
Sc('Compound Machines: Combining Simple Machines',
   'Grade 4 Science strand: a compound machine is made by combining two or more simple machines, such as a wheelbarrow (lever and wheel and axle) or scissors (two levers), to make work easier.',
   [('A compound machine is made by combining ___.', ['Two or more simple machines', 'Only electrical parts', 'X unrelated to compound machines', 'A single simple machine used alone'], 0),
    ('A wheelbarrow is an example of a compound machine because it combines a ___.', ['Lever and a wheel and axle', 'Pulley and a screw', 'X unrelated to how a wheelbarrow works', 'Wedge and an inclined plane only'], 0),
    ('Scissors are considered a compound machine because they are made of ___.', ['Two levers joined together', 'A single pulley', 'X unrelated to how scissors work', 'A wheel and axle only'], 0),
    ('Why might combining simple machines create a more useful tool?', ['Combined machines can make certain tasks even easier than a single simple machine', 'Combining simple machines always makes tasks harder to complete', 'X unrelated to compound machines', 'Simple machines cannot be combined with one another'], 0),
    ('Which of these is an example of a compound machine?', ['A bicycle, which combines wheels, levers, and gears', 'A single ramp with nothing else attached', 'X unrelated to compound machines', 'A single lever with no other parts'], 0)]),
SS('Canada’s Population Distribution: Where People Live',
   'Grade 4 Social Studies strand: most of Canada’s population lives in a narrow band near the southern border, close to resources, transportation, and warmer climates, while northern regions remain sparsely populated.',
   [('Most of Canada’s population lives ___.', ['In a narrow band near the southern border', 'Spread evenly across the entire country', 'X unrelated to Canada’s population', 'Mostly in the far north'], 0),
    ('Why do fewer people live in Canada’s northern regions?', ['The climate is harsher and there are fewer transportation routes and services', 'The north has no land at all', 'X unrelated to population distribution', 'Everyone in Canada is required to live in the south'], 0),
    ('Which factor most influences where Canadians choose to settle?', ['Access to resources, jobs, and transportation', 'The colour of the provincial flag', 'X unrelated to population distribution', 'The number of letters in a city’s name'], 0),
    ('Which of these Canadian cities would likely have one of the largest populations?', ['Toronto', 'A small hamlet in Nunavut', 'X unrelated to comparing population size', 'A remote research station'], 0),
    ('Why do geographers study population distribution?', ['It helps explain how and why people are spread across a country', 'Population distribution provides no useful information', 'X unrelated to studying geography', 'Every region of Canada has an identical population'], 0)])]),
day(70, [
L('Review: Vocabulary, Grammar, and Reading Skills (Days 61-69)',
  'Grade 4 Language strand: this review lesson revisits key ideas from Days 61-69, including analogies, alliteration, interjections, theme, and skimming and scanning.',
  [('An analogy compares two pairs of words that share the same ___.', ['Type of relationship', 'Number of letters', 'X unrelated to analogies', 'Spelling pattern'], 0),
   ('Alliteration is the repetition of the same ___ in nearby words.', ['Beginning consonant sound', 'Ending vowel sound', 'X unrelated to alliteration', 'Number of syllables'], 0),
   ('An interjection is a word that expresses ___.', ['Strong emotion', 'A complete action', 'X unrelated to interjections', 'A location in a sentence'], 0),
   ('The theme of a story is its ___.', ['Central message or lesson about life', 'List of characters only', 'X unrelated to theme', 'Number of chapters'], 0),
   ('Why is it useful to review vocabulary, grammar, and reading strategies together?', ['It reinforces how these language skills support clear reading and writing', 'These skills have no connection to each other', 'X unrelated to reviewing language arts', 'Reviewing past learning never helps strengthen understanding'], 0)]),
M('Review: Number Sense, Geometry, and Data (Days 61-69)',
  'Grade 4 Math strand: this review lesson revisits key ideas from Days 61-69, including place value, multiplying 2-digit numbers, rounding decimals, classifying polygons, and tally charts.',
  [('In the number 6,482, the digit 4 represents ___.', ['4 hundreds', '4 tens', 'X unrelated to place value', '4 thousands'], 0),
   ('What is 12 × 13?', ['156', '146', 'X unrelated to the calculation', '136'], 0),
   ('What is 4.7 rounded to the nearest whole number?', ['5', '4', 'X unrelated to the calculation', '6'], 0),
   ('A polygon with five sides is called a ___.', ['Pentagon', 'Hexagon', 'X unrelated to polygon names', 'Octagon'], 0),
   ('Why is it useful to review place value, multiplication, and geometry together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'X unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Ecosystems, Earth and Space, and Structures (Days 61-69)',
   'Grade 4 Science strand: this review lesson revisits key ideas from Days 61-69, including Canadian biomes, camouflage, Earth’s rotation, buoyancy, air resistance, and structural strength.',
   [('A biome is best described as a large region with a distinct ___.', ['Climate, plants, and animals', 'Type of rock only', 'X unrelated to biomes', 'Style of building'], 0),
    ('Camouflage helps an animal ___.', ['Blend into its surroundings to avoid predators', 'Attract as much attention as possible', 'X unrelated to camouflage', 'Grow larger than other animals'], 0),
    ('Day and night occur because Earth ___.', ['Rotates on its axis', 'Stops moving completely', 'X unrelated to day and night', 'Changes shape every day'], 0),
    ('Triangles are considered a strong shape in structures because their angles ___.', ['Resist bending and twisting under pressure', 'Change shape very easily under pressure', 'X unrelated to triangle strength', 'Have no effect on a structure’s strength'], 0),
    ('Why is it useful to review ecosystems, space, and structures together?', ['It reinforces how these science concepts each explain different parts of the natural world', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Early Societies and Canadian Geography (Days 61-69)',
   'Grade 4 Social Studies strand: this review lesson revisits key ideas from Days 61-69, including the Maya, Nubia, early leadership, the Canadian Shield, time zones, and population distribution.',
   [('The ancient Maya civilization was located in ___.', ['Central America', 'Northern Europe', 'X unrelated to the Maya', 'Southern Africa'], 0),
    ('Nubia became especially well known for its skill in working with ___.', ['Iron', 'Plastic', 'X unrelated to Nubian achievements', 'Rubber'], 0),
    ('The Canadian Shield is best described as a vast region of ___.', ['Ancient rock covering much of central and northern Canada', 'Flat farmland found only in southern Ontario', 'X unrelated to the Canadian Shield', 'Desert sand dunes'], 0),
    ('How many time zones does Canada have?', ['Six', 'One', 'X unrelated to Canada’s time zones', 'Twelve'], 0),
    ('Why is it useful to review early societies alongside Canadian geography?', ['It helps compare how different societies and regions have developed over time', 'These topics have no connection to social studies', 'X unrelated to reviewing social studies', 'Early societies and Canadian geography are exactly the same topic'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260910):
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
    _rebalance_answer_positions(g4_61_70)
    append_to(4, g4_61_70)
