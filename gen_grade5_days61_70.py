#!/usr/bin/env python3
"""Phase 3 extension: Grade 5, Days 61-70 (continuing past the Day 60
milestone toward the full 157-day year). Topics chosen to avoid any
overlap with the existing Day 1-60 set (see data/grade5.json):
magnetism, decimal addition/subtraction, prime factorization,
Confederation, and Canadian inventions, among others.

Subject keys for Grade 5 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 5 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science & Technology',
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


g5_61_70 = [
day(61, [
L('Reading: Identifying Bias in a Text',
  'Grade 5 Language strand: bias occurs when a text presents information in a one-sided way, favouring a particular opinion instead of presenting facts fairly.',
  [('Bias in a text means the writing ___.', ['Presents information in a one-sided, unfair way', 'Presents every side of an issue equally', 'A concept unrelated to reading', 'Contains only verified factual statements'], 0),
   ('Which is a clue that a text might be biased?', ['It uses emotional language to persuade rather than inform', 'It includes a balanced mix of evidence from multiple sources', 'A clue unrelated to identifying bias', 'It cites where each piece of information came from'], 0),
   ('Why is it useful for readers to notice bias in a text?', ['It helps readers judge how trustworthy or one-sided the information is', 'Noticing bias never changes how a reader understands a text', 'A reason unrelated to critical reading', 'Bias has no effect on how information is presented'], 0),
   ('Which of these is an example of biased language?', ['Describing an idea as “obviously the only sensible choice”', 'Describing an idea using only measured, neutral facts', 'A phrase unrelated to biased language', 'Listing evidence for and against an idea equally'], 0),
   ('How can a reader check whether a text is biased?', ['Comparing it with other sources to see if the information is one-sided', 'Assuming every text is completely fair with no need to check', 'A method unrelated to identifying bias', 'Reading only the title and nothing else'], 0)]),
M('Adding and Subtracting Decimals',
  'Grade 5 Math strand: adding and subtracting decimals requires lining up the decimal points and place values before combining or comparing the digits.',
  [('When adding decimals, it is important to first ___.', ['Line up the decimal points', 'Ignore the decimal points entirely', 'A step unrelated to adding decimals', 'Round every number to a whole number'], 0),
   ('What is 4.5 + 3.2?', ['7.7', '7.2', 'A value unrelated to the calculation', '4.8'], 0),
   ('What is 6.8 - 2.3?', ['4.5', '4.1', 'A value unrelated to the calculation', '9.1'], 0),
   ('What is 12.75 + 0.5?', ['13.25', '12.8', 'A value unrelated to the calculation', '17.75'], 0),
   ('Why might someone need to add decimals in real life?', ['To total up amounts of money that include cents', 'Adding decimals never applies to real-life situations', 'A reason unrelated to decimals', 'Decimals are only used in scientific formulas'], 0)]),
Sc('Magnetism and Magnetic Forces',
   'Grade 5 Science strand: magnets create an invisible force field that attracts certain metals and can either pull objects together or push them apart, depending on their poles.',
   [('A magnet has two poles, called the ___.', ['North pole and south pole', 'Positive pole and negative pole', 'A concept unrelated to magnetism', 'Hot pole and cold pole'], 0),
    ('Which of these materials is most strongly attracted to a magnet?', ['Iron', 'Wood', 'A material unrelated to magnetism', 'Plastic'], 0),
    ('What happens when two like poles of a magnet are brought together?', ['They repel, or push apart', 'They always attract, or pull together', 'A concept unrelated to magnetism', 'They have no effect on each other'], 0),
    ('What happens when opposite poles of two magnets are brought together?', ['They attract, or pull together', 'They repel, or push apart', 'A concept unrelated to magnetism', 'They have no effect on each other'], 0),
    ('Which of these is an everyday use of magnets?', ['Holding notes on a refrigerator door', 'Boiling water for tea', 'A use unrelated to magnetism', 'Measuring the temperature outside'], 0)]),
SS('Confederation: The Birth of Canada in 1867',
   'Grade 5 Social Studies strand: Confederation in 1867 united several British colonies into the Dominion of Canada, creating a new country with its own federal government.',
   [('Confederation in 1867 united several British colonies to form ___.', ['The Dominion of Canada', 'A colony still ruled directly by Britain', 'A concept unrelated to Canadian history', 'A country called New France'], 0),
    ('Which four provinces joined together at Confederation in 1867?', ['Ontario, Quebec, Nova Scotia, and New Brunswick', 'British Columbia, Alberta, Manitoba, and Yukon', 'A group unrelated to Confederation', 'Only Ontario and Quebec'], 0),
    ('Why did colonies consider joining together at Confederation?', ['To gain strength through unity and build a stronger shared economy and defence', 'Joining together offered no benefits to the colonies', 'A reason unrelated to Confederation', 'The colonies were forced to join by another country'], 0),
    ('What is the significance of July 1, 1867 in Canadian history?', ['It marks the day Canada became a country through Confederation', 'It has no connection to Canadian history', 'A date unrelated to Confederation', 'It marks the day Canada gained full independence from Britain'], 0),
    ('Why is Confederation an important milestone for students to study?', ['It marks the founding of Canada as a nation and shaped its government', 'Confederation had no lasting impact on Canada', 'A reason unrelated to Canadian history', 'It only affected one small region of the country'], 0)])]),
day(62, [
L('Grammar: Prepositional Phrases',
  'Grade 5 Language strand: a prepositional phrase begins with a preposition, such as “in,” “on,” or “under,” and ends with a noun or pronoun, adding detail about location, time, or direction.',
  [('A prepositional phrase begins with a ___.', ['Preposition', 'Verb', 'A part of speech unrelated to prepositional phrases', 'Noun only, with no preposition'], 0),
   ('Which of these is a prepositional phrase?', ['Under the table', 'Quickly ran', 'A phrase unrelated to prepositions', 'The happy dog'], 0),
   ('In the sentence “The cat slept on the couch,” what is the prepositional phrase?', ['On the couch', 'The cat slept', 'A phrase unrelated to this sentence', 'Slept on'], 0),
   ('Prepositional phrases often add detail about ___.', ['Location, time, or direction', 'Only the main verb of a sentence', 'A concept unrelated to prepositional phrases', 'The subject’s exact age'], 0),
   ('Which word is a common preposition?', ['Beside', 'Quickly', 'A word unrelated to prepositions', 'Happiness'], 0)]),
M('Prime Factorization',
  'Grade 5 Math strand: prime factorization breaks a number down into the prime numbers that multiply together to make it, often shown using a factor tree.',
  [('Prime factorization breaks a number down into ___.', ['The prime numbers that multiply together to make it', 'A list of all its factors, prime or not', 'A concept unrelated to factorization', 'Only its largest factor'], 0),
   ('What is the prime factorization of 12?', ['2 x 2 x 3', '2 x 6', 'A factorization unrelated to 12', '4 x 3'], 0),
   ('What is the prime factorization of 20?', ['2 x 2 x 5', '4 x 5', 'A factorization unrelated to 20', '2 x 10'], 0),
   ('A factor tree is a tool used to ___.', ['Break a number down into its prime factors visually', 'Add two numbers together', 'A tool unrelated to factorization', 'List multiples of a number'], 0),
   ('Why is prime factorization a useful math skill?', ['It helps with finding common factors and simplifying fractions', 'It has no connection to other math skills', 'A reason unrelated to factorization', 'It only applies to even numbers'], 0)]),
Sc('The Layers of the Earth',
   'Grade 5 Science strand: the Earth is made up of several layers -- the crust, mantle, outer core, and inner core -- each with different properties and depths.',
   [('The outermost layer of the Earth is called the ___.', ['Crust', 'Mantle', 'A layer unrelated to Earth’s structure', 'Inner core'], 0),
    ('Which layer of the Earth is closest to the centre?', ['Inner core', 'Crust', 'A layer unrelated to Earth’s structure', 'Mantle'], 0),
    ('The mantle is located ___.', ['Between the crust and the outer core', 'Above the crust', 'A location unrelated to Earth’s structure', 'Outside the Earth’s atmosphere'], 0),
    ('Which layer of the Earth is believed to be extremely hot and mostly solid metal?', ['Inner core', 'Crust', 'A layer unrelated to Earth’s structure', 'Mantle'], 0),
    ('Why do scientists study the layers of the Earth?', ['To better understand processes like earthquakes and volcanic activity', 'Studying Earth’s layers provides no useful information', 'A reason unrelated to Earth science', 'The layers of the Earth have no connection to natural events'], 0)]),
SS('Canadian Inventions and Innovators',
   'Grade 5 Social Studies strand: Canadians have contributed many important inventions and innovations, from basketball to insulin, that have had a lasting impact on the world.',
   [('Which of these was invented by a Canadian?', ['Basketball', 'The telephone book', 'A concept unrelated to Canadian inventions', 'The bicycle'], 0),
    ('Why is it important to study Canadian inventors and innovators?', ['It highlights the contributions Canadians have made to the world', 'Canadian inventors have made no notable contributions', 'A reason unrelated to Canadian history', 'Only inventions from other countries matter'], 0),
    ('Insulin, a treatment for diabetes, was discovered by a research team working in ___.', ['Canada', 'A country unrelated to this discovery', 'A country that has never contributed to medicine', 'Only outside of North America'], 0),
    ('Which of these best describes an innovator?', ['Someone who creates a new idea, product, or way of doing something', 'Someone who only repeats ideas that already exist', 'A concept unrelated to innovation', 'Someone with no interest in solving problems'], 0),
    ('Why might Canadian inventions be a source of national pride?', ['They show how Canadians have contributed valuable ideas that benefit others', 'Inventions have no connection to how a country sees itself', 'A reason unrelated to Canadian identity', 'National pride has no connection to accomplishments'], 0)])]),
day(63, [
L('Writing: Writing a Book Review',
  'Grade 5 Language strand: a book review summarizes a text and shares the writer’s opinion of it, supported by specific reasons and examples from the book.',
  [('A book review typically includes a summary and ___.', ['The writer’s opinion, supported by reasons and examples', 'Only a list of characters with no opinion at all', 'A concept unrelated to book reviews', 'A completely different story with no connection to the book'], 0),
   ('Why should a book review include specific examples from the text?', ['They support the writer’s opinion and make the review more convincing', 'Examples are never needed in a book review', 'A reason unrelated to writing a review', 'Examples make a review harder to understand'], 0),
   ('Which is an example of an opinion a writer might include in a book review?', ['The pacing of the story felt slow in the middle chapters', 'The book has exactly two hundred pages', 'A concept unrelated to book reviews', 'The book was published by a certain company'], 0),
   ('What is one purpose of writing a book review?', ['To help other readers decide whether they might enjoy the book', 'To retell the entire story without offering any opinion', 'A purpose unrelated to book reviews', 'To copy the book’s summary from its back cover'], 0),
   ('Why might two readers write very different reviews of the same book?', ['Readers can have different reactions and opinions about the same text', 'All readers are required to feel the same way about every book', 'A reason unrelated to book reviews', 'Book reviews never include a personal opinion'], 0)]),
M('Introduction to Exponents',
  'Grade 5 Math strand: an exponent shows how many times a number, called the base, is multiplied by itself, such as 2 cubed meaning 2 x 2 x 2.',
  [('An exponent tells you ___.', ['How many times a number is multiplied by itself', 'How many times a number is divided by itself', 'A concept unrelated to exponents', 'The sum of a number added to itself'], 0),
   ('What does 2 to the power of 3 (2 cubed) mean?', ['2 x 2 x 2', '2 x 3', 'A value unrelated to this expression', '2 + 2 + 2'], 0),
   ('What is the value of 2 to the power of 3?', ['8', '6', 'A value unrelated to the calculation', '9'], 0),
   ('What is the value of 5 to the power of 2 (5 squared)?', ['25', '10', 'A value unrelated to the calculation', '52'], 0),
   ('In the expression 4 to the power of 2, what is the base?', ['4', '2', 'A number unrelated to this expression', '8'], 0)]),
Sc('Volcanoes: Formation and Types',
   'Grade 5 Science strand: volcanoes form when molten rock, gas, and ash escape from beneath the Earth’s surface, and different volcano types are shaped by how they erupt.',
   [('A volcano forms when molten rock, called magma, escapes from ___.', ['Beneath the Earth’s surface', 'Only the ocean floor', 'A concept unrelated to volcanoes', 'The Earth’s atmosphere'], 0),
    ('Magma that reaches the Earth’s surface is called ___.', ['Lava', 'Sediment', 'A term unrelated to volcanoes', 'Groundwater'], 0),
    ('A shield volcano is typically shaped by ___.', ['Slow-flowing lava that spreads out widely', 'Only ash with no lava involved', 'A concept unrelated to volcano formation', 'Cold temperatures with no eruption at all'], 0),
    ('Why do some volcanoes erupt explosively?', ['Built-up pressure from trapped gas is released suddenly', 'Explosive eruptions never involve pressure of any kind', 'A reason unrelated to volcanic activity', 'Volcanoes only erupt when the weather is cold'], 0),
    ('Why do scientists monitor active volcanoes closely?', ['To help predict eruptions and protect nearby communities', 'Monitoring volcanoes provides no useful information', 'A reason unrelated to science', 'Volcanoes never pose any risk to nearby areas'], 0)]),
SS('Canada’s Economy: Primary, Secondary, and Tertiary Industries',
   'Grade 5 Social Studies strand: Canada’s economy includes primary industries that gather raw materials, secondary industries that manufacture goods, and tertiary industries that provide services.',
   [('A primary industry is one that ___.', ['Gathers raw materials, such as mining or farming', 'Only sells finished products in stores', 'A concept unrelated to industries', 'Provides services like teaching or banking'], 0),
    ('Which of these is an example of a secondary industry?', ['A factory that manufactures cars from raw materials', 'A farm that grows wheat', 'A concept unrelated to secondary industries', 'A bank that offers financial services'], 0),
    ('Which of these is an example of a tertiary industry?', ['A hospital that provides healthcare services', 'A mine that extracts minerals from the ground', 'A concept unrelated to tertiary industries', 'A forest where logging takes place'], 0),
    ('Why does Canada’s economy rely on all three types of industries?', ['Each type of industry plays a different role in producing goods and services', 'Only one type of industry is actually needed', 'A reason unrelated to Canada’s economy', 'The three types of industries have no connection to each other'], 0),
    ('Why is fishing considered a primary industry in Canada?', ['It involves gathering a natural resource directly from the environment', 'Fishing always involves manufacturing finished products', 'A reason unrelated to Canada’s economy', 'Fishing is classified only as a service industry'], 0)])]),
day(64, [
L('Vocabulary: Prefixes and Suffixes',
  'Grade 5 Language strand: a prefix is added to the beginning of a word to change its meaning, while a suffix is added to the end, and both help readers figure out unfamiliar words.',
  [('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'A position unrelated to prefixes', 'Middle'], 0),
   ('A suffix is added to the ___ of a word.', ['End', 'Beginning', 'A position unrelated to suffixes', 'Middle'], 0),
   ('What does the prefix “un-” usually mean, as in “unhappy”?', ['Not', 'Again', 'A meaning unrelated to this prefix', 'Before'], 0),
   ('What does the suffix “-ful” usually mean, as in “helpful”?', ['Full of', 'Without', 'A meaning unrelated to this suffix', 'Before'], 0),
   ('Why are prefixes and suffixes useful when reading unfamiliar words?', ['They can give clues about a word’s meaning', 'They never provide any clues about meaning', 'A reason unrelated to vocabulary', 'They only affect how a word is spelled, not its meaning'], 0)]),
M('Divisibility Rules',
  'Grade 5 Math strand: divisibility rules are quick tests that show whether a number can be divided evenly by another number, without doing long division.',
  [('A number is divisible by 2 if it ___.', ['Ends in an even digit', 'Ends in an odd digit', 'A rule unrelated to divisibility by 2', 'Is greater than 100'], 0),
   ('A number is divisible by 5 if it ___.', ['Ends in 0 or 5', 'Ends in an even digit', 'A rule unrelated to divisibility by 5', 'Is a prime number'], 0),
   ('A number is divisible by 3 if ___.', ['The sum of its digits is divisible by 3', 'It ends in the digit 3', 'A rule unrelated to divisibility by 3', 'It is an even number'], 0),
   ('Is 42 divisible by 3? Use the digit-sum rule to check.', ['Yes, because 4 + 2 = 6, which is divisible by 3', 'No, because 42 is an odd number', 'A conclusion unrelated to the digit-sum rule', 'Yes, because 42 ends in 2'], 0),
   ('Why are divisibility rules useful?', ['They help quickly check if a number can be divided evenly without long division', 'They make it impossible to check divisibility', 'A reason unrelated to divisibility rules', 'They only work for the number 10'], 0)]),
Sc('Types of Pollution and Their Impact',
   'Grade 5 Science strand: pollution includes air, water, and land pollution caused by human activity, and each type can harm living things and the environment.',
   [('Air pollution can be caused by ___.', ['Smoke and exhaust from vehicles and factories', 'Rainfall over a forest', 'A concept unrelated to air pollution', 'Sunlight reaching the Earth’s surface'], 0),
    ('Which of these is an example of water pollution?', ['Chemicals or waste being released into a river', 'Rain falling into a lake', 'A concept unrelated to water pollution', 'Fish swimming in clean water'], 0),
    ('Land pollution often occurs when ___.', ['Garbage or harmful substances are dumped onto the ground', 'Farmers plant new crops in a field', 'A concept unrelated to land pollution', 'Leaves fall naturally from trees'], 0),
    ('Why can pollution be harmful to living things?', ['It can damage habitats and make air, water, or soil unsafe', 'Pollution never has any effect on living things', 'A reason unrelated to pollution', 'Pollution only affects things that are not alive'], 0),
    ('Which of these actions could help reduce pollution?', ['Reducing waste and recycling materials', 'Dumping more garbage into rivers', 'A concept unrelated to reducing pollution', 'Burning more fuel unnecessarily'], 0)]),
SS('Taxes and Government Services',
   'Grade 5 Social Studies strand: taxes are payments collected by governments from citizens and businesses, used to fund public services such as schools, roads, and healthcare.',
   [('Taxes are payments collected by governments to fund ___.', ['Public services such as schools, roads, and healthcare', 'Only the personal expenses of government leaders', 'A concept unrelated to taxes', 'Nothing, since taxes serve no real purpose'], 0),
    ('Which of these is typically funded through taxes?', ['Public schools', 'A privately owned business', 'A concept unrelated to public services', 'A family’s personal savings account'], 0),
    ('Why might governments at different levels, such as municipal and federal, both collect taxes?', ['Each level of government funds different public services and responsibilities', 'Only one level of government is ever allowed to collect taxes', 'A reason unrelated to government funding', 'Taxes are collected with no connection to government services'], 0),
    ('Which of these is an example of a public service funded by taxes?', ['Public libraries', 'A private vacation for one family', 'A concept unrelated to tax-funded services', 'A personal savings account'], 0),
    ('Why is it useful for citizens to understand how taxes are used?', ['It helps them understand how public services are funded and maintained', 'Taxes have no connection to the services citizens use', 'A reason unrelated to citizenship', 'Understanding taxes provides no useful information'], 0)])]),
day(65, [
L('Reading: Understanding Flashback',
  'Grade 5 Language strand: a flashback is a writing technique where the story pauses to show an event that happened earlier, before returning to the present moment of the story.',
  [('A flashback shows an event that happened ___.', ['Earlier in time, before the present moment of the story', 'Later in time, after the story has ended', 'A concept unrelated to reading', 'At exactly the same moment as the current scene'], 0),
   ('Why might an author use a flashback?', ['To give readers important background information about a character or event', 'Flashbacks never provide any useful information to readers', 'A reason unrelated to storytelling', 'To confuse readers with no clear purpose'], 0),
   ('Which is an example of a flashback?', ['A character suddenly remembering a moment from their childhood', 'A character planning something that will happen tomorrow', 'A concept unrelated to flashback', 'A story with no reference to any past events'], 0),
   ('How is a flashback different from foreshadowing?', ['A flashback shows past events, while foreshadowing hints at future events', 'A flashback and foreshadowing mean exactly the same thing', 'A concept unrelated to these techniques', 'Foreshadowing always shows events from the past'], 0),
   ('What often signals to a reader that a flashback is beginning?', ['A phrase or clue indicating a shift to an earlier time', 'A story ending abruptly with no explanation', 'A reason unrelated to flashback', 'Flashbacks are never signalled in any way'], 0)]),
M('Square Numbers and Square Roots',
  'Grade 5 Math strand: a square number is the result of multiplying a whole number by itself, and its square root is the number that was multiplied to produce it.',
  [('A square number is the result of ___.', ['Multiplying a whole number by itself', 'Adding a whole number to itself', 'A concept unrelated to square numbers', 'Dividing a whole number by itself'], 0),
   ('What is 4 squared (4 x 4)?', ['16', '8', 'A value unrelated to the calculation', '12'], 0),
   ('What is the square root of 25?', ['5', '10', 'A value unrelated to the calculation', '25'], 0),
   ('What is the square root of 49?', ['7', '14', 'A value unrelated to the calculation', '9'], 0),
   ('Why are square numbers often shown using a grid or array?', ['Because a square number can form a perfectly square grid of dots', 'Grids have no connection to square numbers', 'A reason unrelated to square numbers', 'Square numbers can only be shown using a number line'], 0)]),
Sc('Animal Life Cycles and Metamorphosis',
   'Grade 5 Science strand: many animals go through distinct life cycle stages, and some, such as butterflies and frogs, undergo metamorphosis, a dramatic change in body form.',
   [('Metamorphosis is a process in which an animal ___.', ['Changes dramatically in body form as it grows', 'Stays exactly the same throughout its entire life', 'A concept unrelated to animal life cycles', 'Loses all of its offspring immediately after birth'], 0),
    ('Which of these animals undergoes complete metamorphosis?', ['A butterfly', 'A dog', 'A concept unrelated to metamorphosis', 'A human'], 0),
    ('What is the correct order of a butterfly’s life cycle?', ['Egg, larva, pupa, adult', 'Adult, egg, pupa, larva', 'An order unrelated to a butterfly’s life cycle', 'Pupa, adult, egg, larva'], 0),
    ('A tadpole changing into a frog is an example of ___.', ['Metamorphosis', 'A life cycle stage that never changes', 'A concept unrelated to amphibians', 'Hibernation'], 0),
    ('Why is metamorphosis an important adaptation for some animals?', ['It can allow the animal to live in different environments or eat different foods at each stage', 'Metamorphosis has no connection to how an animal survives', 'A reason unrelated to animal life cycles', 'Metamorphosis prevents an animal from ever changing'], 0)]),
SS('Agriculture and Farming Regions of Canada',
   'Grade 5 Social Studies strand: Canada’s different regions support different types of farming, shaped by climate, soil, and land, from prairie grain farms to Ontario’s fruit orchards.',
   [('The Prairie provinces are well known for growing ___.', ['Grain crops such as wheat', 'Only tropical fruit', 'A concept unrelated to Prairie agriculture', 'No crops at all'], 0),
    ('Why might southern Ontario be suitable for growing fruit such as peaches and grapes?', ['It has a milder climate and fertile soil suited to fruit growing', 'Climate and soil have no connection to farming', 'A reason unrelated to agriculture', 'Southern Ontario has no farmland at all'], 0),
    ('Which factor most affects what crops can be grown in a Canadian region?', ['Climate and soil conditions', 'The colour of the provincial flag', 'A factor unrelated to agriculture', 'The size of the region’s cities'], 0),
    ('Why is agriculture an important part of Canada’s economy?', ['It provides food and supports jobs across many regions', 'Agriculture has no connection to Canada’s economy', 'A reason unrelated to farming', 'Farming no longer takes place anywhere in Canada'], 0),
    ('Why might farming be more limited in Canada’s northern territories?', ['Colder climates and shorter growing seasons make large-scale farming difficult', 'The north has the best possible climate for farming', 'A reason unrelated to Canadian geography', 'Farming is equally easy in every region of Canada'], 0)])]),
day(66, [
L('Figurative Language: Personification and Metaphor',
  'Grade 5 Language strand: personification gives human qualities to something non-human, while a metaphor directly compares two unlike things without using “like” or “as.”',
  [('Personification gives ___.', ['Human qualities to something non-human', 'Animal qualities to a human being', 'A concept unrelated to figurative language', 'No special qualities to anything at all'], 0),
   ('A metaphor compares two unlike things ___.', ['Directly, without using “like” or “as”', 'Only by using the word “like”', 'A concept unrelated to metaphors', 'Only by using the word “as”'], 0),
   ('Which sentence is an example of personification?', ['The wind whispered through the trees.', 'The wind blew at ten kilometres per hour.', 'A sentence unrelated to personification', 'The tree has green leaves.'], 0),
   ('Which sentence is an example of a metaphor?', ['Her smile was sunshine on a cloudy day.', 'Her smile was as bright as sunshine.', 'A sentence unrelated to metaphors', 'Her smile appeared briefly.'], 0),
   ('Why might a writer use personification or metaphor in a story?', ['To create a vivid image or add deeper meaning to the writing', 'These techniques never affect how a reader pictures a scene', 'A reason unrelated to figurative language', 'To make the writing more difficult to understand for no reason'], 0)]),
M('Data Management: Pictographs',
  'Grade 5 Math strand: a pictograph displays data using pictures or symbols, where each symbol represents a set number of items, along with a key explaining its value.',
  [('A pictograph displays data using ___.', ['Pictures or symbols, along with a key', 'Only bars of different heights', 'A concept unrelated to pictographs', 'Slices of a circle'], 0),
   ('What is the purpose of the key in a pictograph?', ['It explains how many items each symbol represents', 'It has no useful purpose in a pictograph', 'A concept unrelated to pictographs', 'It shows the title of the graph only'], 0),
   ('If a key shows that one symbol equals 5 items, and a row has 3 symbols, how many items does that represent?', ['15', '8', 'A value unrelated to the calculation', '3'], 0),
   ('Why might a half symbol appear in a pictograph?', ['To represent an amount that is half of the symbol’s usual value', 'Half symbols are never used in pictographs', 'A reason unrelated to pictographs', 'To represent exactly double the symbol’s usual value'], 0),
   ('Why are pictographs useful for displaying data?', ['They present data in a simple, visual way that is easy to compare', 'Pictographs cannot be used to compare any data', 'A reason unrelated to pictographs', 'Pictographs only work with negative numbers'], 0)]),
Sc('Nutrition and the Food Groups',
   'Grade 5 Science strand: a balanced diet includes a variety of foods from different groups, such as vegetables and fruits, grains, and protein foods, each providing different nutrients the body needs.',
   [('A balanced diet includes foods from ___.', ['A variety of different food groups', 'Only a single food group', 'A concept unrelated to nutrition', 'No specific groups at all'], 0),
    ('Which of these is considered a protein food?', ['Fish', 'Bread', 'A concept unrelated to protein foods', 'Rice'], 0),
    ('Why does the body need nutrients from vegetables and fruits?', ['They provide important vitamins, minerals, and fibre', 'Vegetables and fruits provide no nutrients at all', 'A reason unrelated to nutrition', 'They are needed only for their colour'], 0),
    ('What is one benefit of eating a variety of foods rather than just one type?', ['It helps the body get all the different nutrients it needs', 'Eating a variety of foods provides no benefit', 'A reason unrelated to nutrition', 'Variety only affects how food tastes, not health'], 0),
    ('Why might drinking enough water be considered part of good nutrition?', ['Water helps the body function properly and stay hydrated', 'Water has no connection to how the body functions', 'A reason unrelated to nutrition', 'The body does not need water to stay healthy'], 0)]),
SS('Canada’s Role in International Alliances (NATO)',
   'Grade 5 Social Studies strand: Canada is a member of international alliances, such as NATO, that bring countries together to support mutual defence and cooperation.',
   [('NATO is an alliance that brings countries together to support ___.', ['Mutual defence and cooperation', 'Complete isolation from other countries', 'A concept unrelated to international alliances', 'Trade disputes between member countries'], 0),
    ('Why might Canada choose to join an international alliance like NATO?', ['To strengthen security and cooperation with other countries', 'Joining an alliance offers no benefits to a country', 'A reason unrelated to international relations', 'Canada is required to join with no choice involved'], 0),
    ('Which of these best describes how alliance members support one another?', ['They cooperate on shared defence and security goals', 'They refuse to communicate with one another', 'A concept unrelated to alliances', 'They compete against each other militarily'], 0),
    ('Why might belonging to an international alliance be considered part of Canada’s foreign policy?', ['It reflects how Canada works with other countries on global issues', 'Alliances have no connection to a country’s foreign policy', 'A reason unrelated to Canadian government', 'Canada has never taken part in any international alliance'], 0),
    ('Why is it useful for students to learn about international alliances?', ['It helps them understand how countries cooperate on global security and issues', 'International alliances have no relevance to students', 'A reason unrelated to social studies learning', 'Countries never work together on shared goals'], 0)])]),
day(67, [
L('Writing: Writing Effective Introductions',
  'Grade 5 Language strand: an effective introduction grabs the reader’s attention, introduces the topic, and often previews the main ideas that will follow.',
  [('An effective introduction should ___.', ['Grab the reader’s attention and introduce the topic', 'Summarize the entire piece of writing word for word', 'A concept unrelated to writing', 'Avoid mentioning the topic at all'], 0),
   ('Which is an example of a strong opening hook in an introduction?', ['An interesting question or surprising fact related to the topic', 'A list of every source used in the writing', 'A concept unrelated to introductions', 'A random sentence with no connection to the topic'], 0),
   ('Why might a writer preview the main ideas in an introduction?', ['It helps the reader know what to expect from the rest of the writing', 'Previewing ideas always confuses the reader', 'A reason unrelated to writing introductions', 'Introductions should never mention any main ideas'], 0),
   ('Which of these would likely make a weak introduction?', ['Starting with “This essay is about a topic.” and nothing else', 'Starting with an interesting question about the topic', 'A concept unrelated to introductions', 'Starting with a surprising, relevant fact'], 0),
   ('Why is the introduction often considered an important part of a piece of writing?', ['It creates the reader’s first impression and sets up the rest of the writing', 'The introduction has no effect on how a reader experiences the writing', 'A reason unrelated to writing structure', 'Introductions are an optional part of writing that can be skipped'], 0)]),
M('Estimating Sums and Differences',
  'Grade 5 Math strand: estimating sums and differences involves rounding numbers before adding or subtracting to quickly find an approximate answer.',
  [('Estimating a sum or difference involves ___.', ['Rounding numbers before adding or subtracting', 'Finding the exact answer using a calculator', 'A concept unrelated to estimation', 'Ignoring the numbers in the problem entirely'], 0),
   ('Estimate the sum of 48 + 31 by rounding to the nearest ten.', ['80', '79', 'A value unrelated to the estimation', '90'], 0),
   ('Estimate the difference of 92 - 47 by rounding to the nearest ten.', ['50', '45', 'A value unrelated to the estimation', '40'], 0),
   ('Why might someone estimate before solving a math problem?', ['To quickly check whether their exact answer seems reasonable', 'Estimating never helps with checking an answer', 'A reason unrelated to estimation', 'Estimating always gives the exact same result as the real answer'], 0),
   ('Which is a real-life situation where estimating a sum could be useful?', ['Quickly checking if you have enough money for groceries', 'Estimating never applies to real-life situations', 'A reason unrelated to estimation', 'Estimating is only used in advanced scientific research'], 0)]),
Sc('The Skin and Its Functions',
   'Grade 5 Science strand: the skin is the body’s largest organ, protecting internal tissues, helping regulate body temperature, and providing the sense of touch.',
   [('The skin is considered the body’s ___.', ['Largest organ', 'Smallest organ', 'A concept unrelated to the skin', 'Only a covering with no other function'], 0),
    ('Which of these is a function of the skin?', ['Protecting the body from germs and injury', 'Pumping blood throughout the body', 'A function unrelated to the skin', 'Digesting food for energy'], 0),
    ('How does the skin help regulate body temperature?', ['By sweating to cool the body down when it is hot', 'The skin has no connection to body temperature', 'A reason unrelated to the skin', 'By preventing the body from ever losing heat'], 0),
    ('Which sense is closely connected to the skin?', ['Touch', 'Taste', 'A sense unrelated to the skin', 'Hearing'], 0),
    ('Why is it important to protect skin from sun damage?', ['The skin can be harmed by too much exposure to ultraviolet light', 'Sun exposure has no effect on the skin', 'A reason unrelated to skin health', 'Skin cannot be damaged by sunlight'], 0)]),
SS('Canada’s Provincial and Territorial Capitals',
   'Grade 5 Social Studies strand: each of Canada’s provinces and territories has its own capital city, which is home to that region’s government.',
   [('The capital city of Ontario is ___.', ['Toronto', 'Ottawa', 'A city unrelated to Ontario', 'Hamilton'], 0),
    ('The capital city of British Columbia is ___.', ['Victoria', 'Vancouver', 'A city unrelated to British Columbia', 'Kelowna'], 0),
    ('What is typically located in a province’s or territory’s capital city?', ['That region’s government buildings and legislature', 'Only farmland with no government presence', 'A concept unrelated to capital cities', 'The capital of a different province entirely'], 0),
    ('Which of these is the capital of Canada as a whole country?', ['Ottawa', 'Toronto', 'A city unrelated to Canada’s federal capital', 'Montreal'], 0),
    ('Why is it useful to know the capital cities of Canada’s provinces and territories?', ['It helps build understanding of where regional governments are based', 'Capital cities have no connection to how a region is governed', 'A reason unrelated to Canadian geography', 'Every province and territory shares the exact same capital'], 0)])]),
day(68, [
L('Grammar: Direct and Indirect Speech',
  'Grade 5 Language strand: direct speech repeats a speaker’s exact words, often in quotation marks, while indirect speech reports what someone said without quoting them exactly.',
  [('Direct speech repeats a speaker’s ___.', ['Exact words, often in quotation marks', 'General idea, without quoting them exactly', 'A concept unrelated to grammar', 'Words translated into a different language'], 0),
   ('Indirect speech reports what someone said ___.', ['Without quoting them exactly', 'Using their exact words in quotation marks', 'A concept unrelated to grammar', 'Only in the form of a question'], 0),
   ('Which sentence uses direct speech?', ['Maya said, “I am going to the library.”', 'Maya said that she was going to the library.', 'A sentence unrelated to direct speech', 'Maya mentioned something about a library once.'], 0),
   ('Which sentence uses indirect speech?', ['Jordan said that he would arrive early.', 'Jordan said, “I will arrive early.”', 'A sentence unrelated to indirect speech', 'Jordan shouted, “I am here early!”'], 0),
   ('Why might a writer choose indirect speech instead of direct speech?', ['To summarize what someone said without quoting their exact words', 'Indirect speech always requires quotation marks', 'A reason unrelated to grammar', 'Indirect speech is never used in writing'], 0)]),
M('Congruent and Similar Shapes',
  'Grade 5 Math strand: congruent shapes are identical in size and shape, while similar shapes have the same shape but can differ in size, with matching angles and proportional sides.',
  [('Congruent shapes are ___.', ['Identical in both size and shape', 'The same shape but always different sizes', 'A concept unrelated to congruent shapes', 'Never the same in any way'], 0),
   ('Similar shapes have ___.', ['The same shape, with matching angles and proportional sides', 'No matching angles or sides at all', 'A concept unrelated to similar shapes', 'Completely different shapes and angles'], 0),
   ('If two triangles are congruent, their corresponding sides are ___.', ['Exactly equal in length', 'Always different in length', 'A description unrelated to congruent triangles', 'Only equal if the triangles are also similar'], 0),
   ('If two rectangles are similar, one rectangle is ___ the other.', ['A scaled-up or scaled-down version of', 'Always exactly the same size as', 'A description unrelated to similar shapes', 'Never related in shape to'], 0),
   ('Why might architects use similar shapes when designing a building?', ['To create a scaled model that keeps the same proportions as the final building', 'Similar shapes have no use in architecture', 'A reason unrelated to similar shapes', 'Architects never use scale models of any kind'], 0)]),
Sc('Gravity and Its Effects',
   'Grade 5 Science strand: gravity is a force that pulls objects toward each other, and on Earth it pulls objects toward the ground, giving them weight.',
   [('Gravity is a force that ___.', ['Pulls objects toward each other', 'Pushes objects away from each other', 'A concept unrelated to gravity', 'Has no effect on objects at all'], 0),
    ('On Earth, gravity pulls objects toward ___.', ['The ground', 'Outer space', 'A direction unrelated to gravity', 'The sky above'], 0),
    ('Why do objects fall when dropped?', ['Earth’s gravity pulls them downward', 'Objects fall with no connection to gravity', 'A reason unrelated to gravity', 'Objects only fall because of wind'], 0),
    ('An object’s weight is affected by ___.', ['The strength of the gravity pulling on it', 'The colour of the object', 'A factor unrelated to weight', 'The temperature of the object'], 0),
    ('Why would an astronaut weigh less on the Moon than on Earth?', ['The Moon has weaker gravity than Earth', 'The Moon has stronger gravity than Earth', 'A reason unrelated to gravity', 'Gravity is exactly the same on the Moon and Earth'], 0)]),
SS('Consumer Rights and Responsibilities',
   'Grade 5 Social Studies strand: consumers have rights, such as receiving accurate information about products, along with responsibilities, such as spending money wisely.',
   [('A consumer right includes receiving ___.', ['Accurate information about a product before buying it', 'No information about a product at all', 'A concept unrelated to consumer rights', 'False advertising with no consequences'], 0),
    ('Which of these is a consumer responsibility?', ['Comparing prices and making informed spending decisions', 'Spending money without any thought or planning', 'A concept unrelated to consumer responsibilities', 'Ignoring the cost of a product entirely'], 0),
    ('Why might it be important for advertisements to be truthful?', ['Consumers rely on accurate information to make good decisions', 'Advertisements have no effect on what consumers decide to buy', 'A reason unrelated to consumer rights', 'Truthfulness in advertising is never required'], 0),
    ('Which of these is an example of being a responsible consumer?', ['Saving money for something important instead of spending it right away', 'Buying items with no consideration of cost', 'A concept unrelated to consumer responsibility', 'Ignoring how much money is available before spending'], 0),
    ('Why is it useful for students to learn about consumer rights and responsibilities?', ['It helps prepare them to make informed decisions as future consumers', 'This knowledge has no connection to everyday life', 'A reason unrelated to social studies learning', 'Consumers have no rights or responsibilities of any kind'], 0)])]),
day(69, [
L('Reading: Drawing Conclusions',
  'Grade 5 Language strand: drawing a conclusion means combining evidence from the text with what you already know to form a logical judgment about something the author does not state directly.',
  [('Drawing a conclusion means combining text evidence with ___.', ['What you already know to form a logical judgment', 'Only information that is stated directly in the text', 'A concept unrelated to reading', 'A random guess with no evidence involved'], 0),
   ('Which is an example of drawing a conclusion?', ['Deciding a character is nervous because of how they are described acting', 'Copying a sentence directly from the text', 'A concept unrelated to drawing conclusions', 'Ignoring all details in the text'], 0),
   ('Why is it useful for readers to draw conclusions while reading?', ['It helps them understand ideas the author implies but does not state directly', 'Drawing conclusions never adds anything to understanding a text', 'A reason unrelated to reading comprehension', 'Conclusions can only be drawn after finishing an entire book'], 0),
   ('What should a reader use as support when drawing a conclusion?', ['Specific evidence and details found in the text', 'A conclusion with no connection to the text at all', 'A concept unrelated to drawing conclusions', 'Only the title of the text'], 0),
   ('How is drawing a conclusion different from simply summarizing a text?', ['Drawing a conclusion involves interpreting evidence, not just restating events', 'Drawing a conclusion and summarizing mean exactly the same thing', 'A concept unrelated to reading skills', 'Summarizing always requires forming a judgment about the text'], 0)]),
M('Elapsed Time and Time Zones',
  'Grade 5 Math strand: elapsed time is the amount of time that passes between a start time and an end time, and time zones account for differences in time across regions.',
  [('Elapsed time is the amount of time that ___.', ['Passes between a start time and an end time', 'Is shown on a single clock at one moment', 'A concept unrelated to elapsed time', 'Never changes no matter the situation'], 0),
   ('If a movie starts at 2:15 p.m. and ends at 4:00 p.m., how much time has elapsed?', ['1 hour 45 minutes', '2 hours 15 minutes', 'A duration unrelated to the calculation', '1 hour 15 minutes'], 0),
   ('A time zone is a region that ___.', ['Shares the same standard time', 'Never experiences any change in time', 'A concept unrelated to time zones', 'Has no connection to time at all'], 0),
   ('Why does Canada have more than one time zone?', ['The country spans a wide distance from east to west', 'Canada has only one time zone across the entire country', 'A reason unrelated to time zones', 'Time zones have no connection to a country’s size'], 0),
   ('If it is 3:00 p.m. in one time zone and a neighbouring zone is one hour behind, what time is it there?', ['2:00 p.m.', '4:00 p.m.', 'A time unrelated to the calculation', '3:00 p.m.'], 0)]),
Sc('The Human Eye and Vision',
   'Grade 5 Science strand: the human eye detects light and sends signals to the brain, which interprets them as images, allowing us to see the world around us.',
   [('The human eye allows us to see by detecting ___.', ['Light', 'Sound waves', 'A concept unrelated to vision', 'Air pressure'], 0),
    ('Which part of the eye controls how much light enters?', ['The pupil', 'The eyelash', 'A part unrelated to vision', 'The eyebrow'], 0),
    ('After light enters the eye, signals are sent to the ___ to be interpreted.', ['Brain', 'Stomach', 'A part unrelated to vision', 'Lungs'], 0),
    ('Why might the pupil become smaller in bright light?', ['To limit the amount of light entering the eye', 'Bright light has no effect on the pupil', 'A reason unrelated to vision', 'The pupil always stays exactly the same size'], 0),
    ('Why is protecting your eyes important?', ['The eyes are sensitive organs needed for the sense of sight', 'The eyes have no important function in the body', 'A reason unrelated to eye safety', 'Eyes cannot be damaged in any way'], 0)]),
SS('Canada’s National Symbols and Their History',
   'Grade 5 Social Studies strand: Canada’s national symbols, such as the flag, coat of arms, and national anthem, represent the country’s identity and history.',
   [('Canada’s current national flag, featuring a red maple leaf, was officially adopted in ___.', ['1965', 'A year unrelated to Canada’s flag history', '1867', '2000'], 0),
    ('What does the maple leaf on the Canadian flag commonly represent?', ['Canadian identity and natural heritage', 'A concept unrelated to Canadian symbols', 'Another country’s national identity', 'A symbol with no connection to Canada'], 0),
    ('Which of these is considered an official national symbol of Canada?', ['The coat of arms', 'A symbol unrelated to Canadian identity', 'A flag belonging to a different country', 'An object with no historical significance'], 0),
    ('Why do countries often adopt national symbols?', ['To represent shared identity, values, and history', 'National symbols serve no real purpose', 'A reason unrelated to national identity', 'Symbols are chosen with no meaning behind them'], 0),
    ('Why might learning about the history of national symbols be valuable?', ['It helps explain how a country’s identity has developed over time', 'National symbols have no connection to a country’s history', 'A reason unrelated to social studies learning', 'Symbols never change or have any background story'], 0)])]),
day(70, [
L('Review: Bias, Prepositions, Flashback, and Figurative Language',
  'Grade 5 Language strand: this review lesson revisits key ideas from Days 61-69, including identifying bias, prepositional phrases, flashback, and personification and metaphor.',
  [('Bias in a text means the writing ___.', ['Presents information in a one-sided, unfair way', 'Presents every side of an issue equally', 'A concept unrelated to reading', 'Contains only verified factual statements'], 0),
   ('A prepositional phrase begins with a ___.', ['Preposition', 'Verb', 'A part of speech unrelated to prepositional phrases', 'Noun only, with no preposition'], 0),
   ('A flashback shows an event that happened ___.', ['Earlier in time, before the present moment of the story', 'Later in time, after the story has ended', 'A concept unrelated to reading', 'At exactly the same moment as the current scene'], 0),
   ('Personification gives ___.', ['Human qualities to something non-human', 'Animal qualities to a human being', 'A concept unrelated to figurative language', 'No special qualities to anything at all'], 0),
   ('Why is it useful to review reading and grammar skills like these together?', ['It reinforces how different language skills support clear reading and writing', 'These skills have no connection to each other', 'A reason unrelated to reviewing language', 'Review never helps strengthen understanding of a subject'], 0)]),
M('Review: Decimals, Exponents, Factors, and Shapes',
  'Grade 5 Math strand: this review lesson revisits key ideas from Days 61-69, including adding and subtracting decimals, exponents, prime factorization, and congruent and similar shapes.',
  [('When adding decimals, it is important to first ___.', ['Line up the decimal points', 'Ignore the decimal points entirely', 'A step unrelated to adding decimals', 'Round every number to a whole number'], 0),
   ('What does 2 to the power of 3 (2 cubed) mean?', ['2 x 2 x 2', '2 x 3', 'A value unrelated to this expression', '2 + 2 + 2'], 0),
   ('Prime factorization breaks a number down into ___.', ['The prime numbers that multiply together to make it', 'A list of all its factors, prime or not', 'A concept unrelated to factorization', 'Only its largest factor'], 0),
   ('Congruent shapes are ___.', ['Identical in both size and shape', 'The same shape but always different sizes', 'A concept unrelated to congruent shapes', 'Never the same in any way'], 0),
   ('Why is it useful to review decimals, exponents, factors, and shapes together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Magnetism, Earth Layers, Volcanoes, and the Human Body',
   'Grade 5 Science strand: this review lesson revisits key ideas from Days 61-69, including magnetism, the layers of the Earth, volcanoes, and the skin and human eye.',
   [('A magnet has two poles, called the ___.', ['North pole and south pole', 'Positive pole and negative pole', 'A concept unrelated to magnetism', 'Hot pole and cold pole'], 0),
    ('The outermost layer of the Earth is called the ___.', ['Crust', 'Mantle', 'A layer unrelated to Earth’s structure', 'Inner core'], 0),
    ('Magma that reaches the Earth’s surface is called ___.', ['Lava', 'Sediment', 'A term unrelated to volcanoes', 'Groundwater'], 0),
    ('The skin is considered the body’s ___.', ['Largest organ', 'Smallest organ', 'A concept unrelated to the skin', 'Only a covering with no other function'], 0),
    ('Why is it useful to review magnetism, Earth science, and body systems together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Confederation, Economy, Capitals, and Canadian Identity',
   'Grade 5 Social Studies strand: this review lesson revisits key ideas from Days 61-69, including Confederation, Canada’s economy, provincial capitals, and national symbols.',
   [('Confederation in 1867 united several British colonies to form ___.', ['The Dominion of Canada', 'A colony still ruled directly by Britain', 'A concept unrelated to Canadian history', 'A country called New France'], 0),
    ('A primary industry is one that ___.', ['Gathers raw materials, such as mining or farming', 'Only sells finished products in stores', 'A concept unrelated to industries', 'Provides services like teaching or banking'], 0),
    ('The capital city of Ontario is ___.', ['Toronto', 'Ottawa', 'A city unrelated to Ontario', 'Hamilton'], 0),
    ('What does the maple leaf on the Canadian flag commonly represent?', ['Canadian identity and natural heritage', 'A concept unrelated to Canadian symbols', 'Another country’s national identity', 'A symbol with no connection to Canada'], 0),
    ('Why is it useful to review Confederation, the economy, capitals, and national identity together?', ['It reinforces how these Social Studies concepts connect to build understanding of Canada', 'These topics have no connection to each other', 'A reason unrelated to reviewing social studies', 'Review never helps strengthen understanding of a subject'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260812):
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
    _rebalance_answer_positions(g5_61_70)
    append_to(5, g5_61_70)
