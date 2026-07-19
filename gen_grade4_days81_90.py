#!/usr/bin/env python3
"""Grade 4, Days 81-90 -- extends Grade 4 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade4.json):
portmanteau words, active/passive voice, symbolism, speech writing,
oxymorons, correlative conjunctions, author credibility, etymology,
persuasive letters to leaders; multiplying/dividing decimals, classifying
quadrilaterals, stem-and-leaf plots, adding mixed numbers, converting
metric mass, simple probability as a fraction, algebraic expressions,
simple interest; food webs vs food chains, comets and asteroids, weather
fronts and air masses, air pollution, desert adaptations, chemical
reactions, eclipses, invasive species, generators; the Aztec civilization,
museums, Canadian peacekeeping, comparing government systems, the United
Nations, immigration policy, land acknowledgements, Canadian currency
history, and global trade organizations.

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


def _rebalance_answer_positions(days, seed=20260923):
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


g4_81_90 = [
day(81, [
L('Vocabulary: Portmanteau Words and Blends',
  'Grade 4 Language strand: a portmanteau word blends the sounds and meanings of two words into one new word, such as combining breakfast and lunch to make brunch.',
  [('A portmanteau word blends the sounds and meanings of how many words?', ['Two', 'Three', 'Zero', 'A concept unrelated to vocabulary'], 0),
   ('Which word is a portmanteau made from breakfast and lunch?', ['Brunch', 'Dinner', 'Snack', 'Meal'], 0),
   ('Which word is a portmanteau made from smoke and fog?', ['Smog', 'Fogsmoke', 'Cloud', 'Mist'], 0),
   ('Why might people create portmanteau words instead of using two separate words?', ['They can quickly describe something new by combining familiar ideas', 'Portmanteau words never have any real meaning', 'This concept has no connection to vocabulary', 'Portmanteau words are always longer than using two words'], 0),
   ('Which of these is an example of a portmanteau word?', ['Motel, from motor and hotel', 'Sunlight, a compound word', 'Happiness, a word with a suffix', 'Rewrite, a word with a prefix'], 0)]),
M('Multiplying Decimals by Whole Numbers',
  'Grade 4 Math strand: students learn to multiply a decimal number by a whole number, such as finding 0.4 times 3, by thinking of the decimal as tenths or hundredths.',
  [('What is 0.4 times 3?', ['1.2', '1.4', '0.7', '12'], 0),
   ('What is 0.2 times 5?', ['1.0', '0.7', '10', '2.5'], 0),
   ('What is 1.5 times 2?', ['3.0', '2.5', '15', '1.7'], 0),
   ('When multiplying a decimal by a whole number, why is it helpful to think of the decimal as tenths?', ['It helps keep track of the correct place value in the answer', 'Decimals have no connection to place value', 'This concept has no connection to multiplication', 'Tenths always make multiplication impossible'], 0),
   ('What is 0.6 times 4?', ['2.4', '2.0', '24', '0.24'], 0)]),
Sc('Science: Ecosystems: Food Webs vs Food Chains',
   'Grade 4 Science strand: a food chain shows a single path of energy from one living thing to the next, while a food web shows many connected food chains, illustrating an ecosystem’s more complex feeding relationships.',
   [('Does a food chain show a single path of energy, or many connected paths?', ['A single path', 'Many connected paths', 'A concept unrelated to ecosystems', 'No path at all'], 0),
    ('Does a food web show a single path of energy, or many connected food chains?', ['Many connected food chains', 'A single path only', 'A concept unrelated to ecosystems', 'No connections at all'], 0),
    ('Which shows a more complete picture of an ecosystem’s feeding relationships, a food chain or a food web?', ['A food web', 'A food chain', 'Neither shows any feeding relationships', 'They are exactly the same thing'], 0),
    ('Why might scientists prefer using a food web instead of a single food chain to study an ecosystem?', ['A food web shows how many different species are connected through feeding relationships', 'Food webs have no connection to ecosystems', 'A single food chain always shows more information than a food web', 'This concept has no relevance to science'], 0),
    ('What might happen to a food web if one species disappeared from the ecosystem?', ['Other species connected to it could also be affected', 'Removing one species would never affect any other species', 'Food webs never change no matter what happens', 'This concept has no connection to ecosystems'], 0)]),
SS('Social Studies: Ancient Aztec Civilization',
   'Grade 4 Social Studies strand: the Aztec civilization built a powerful empire in what is now Mexico, known for its capital city Tenochtitlan, advanced farming methods, and detailed calendar system.',
   [('In what area did the Aztec civilization build its empire?', ['What is now Mexico', 'What is now Canada', 'A concept unrelated to ancient civilizations', 'What is now Australia'], 0),
    ('What was the name of the Aztec capital city?', ['Tenochtitlan', 'Rome', 'Athens', 'A concept unrelated to the Aztecs'], 0),
    ('Were the Aztecs known for advanced farming methods?', ['Yes', 'No, they had no farming methods at all', 'A concept unrelated to the Aztecs', 'They never grew any food'], 0),
    ('Why might the Aztecs’ detailed calendar system have been important to their society?', ['It likely helped them plan farming, festivals, and other important events', 'Calendars have no connection to ancient societies', 'The Aztecs never used any kind of calendar', 'This concept has no relevance to social studies'], 0),
    ('Why do historians study ancient civilizations like the Aztecs?', ['To understand how past societies lived, built cities, and organized their communities', 'Ancient civilizations have no connection to history', 'Studying past societies has no value at all', 'This concept has no relevance to social studies'], 0)]),
]),

day(82, [
L('Grammar: Active and Passive Voice',
  'Grade 4 Language strand: in the active voice, the subject performs the action, such as The dog chased the ball, while in the passive voice, the subject receives the action, such as The ball was chased by the dog.',
  [('In the active voice, does the subject perform the action or receive it?', ['Perform it', 'Receive it', 'A concept unrelated to grammar', 'Neither perform nor receive it'], 0),
   ('In the passive voice, does the subject perform the action or receive it?', ['Receive it', 'Perform it', 'A concept unrelated to grammar', 'Neither perform nor receive it'], 0),
   ('Which sentence is written in the active voice?', ['The dog chased the ball.', 'The ball was chased by the dog.', 'The ball chased itself.', 'A concept unrelated to grammar'], 0),
   ('Which sentence is written in the passive voice?', ['The ball was chased by the dog.', 'The dog chased the ball.', 'The dog is fast.', 'A concept unrelated to grammar'], 0),
   ('Why might a writer choose the active voice over the passive voice?', ['Active voice often sounds clearer and more direct', 'The active voice is never used by writers', 'This concept has no connection to writing style', 'Passive voice always sounds clearer than active voice'], 0)]),
M('Dividing Decimals by Whole Numbers',
  'Grade 4 Math strand: students learn to divide a decimal number by a whole number, such as finding 6.4 divided by 2, keeping careful track of the decimal point in the answer.',
  [('What is 6.4 divided by 2?', ['3.2', '3.4', '32', '2.2'], 0),
   ('What is 8.4 divided by 4?', ['2.1', '2.4', '84', '4.2'], 0),
   ('What is 9.0 divided by 3?', ['3.0', '3.9', '90', '2.7'], 0),
   ('When dividing a decimal by a whole number, what should you carefully keep track of?', ['The position of the decimal point', 'Only the size of the whole number', 'A concept unrelated to division', 'Only the colour of the numbers'], 0),
   ('What is 5.5 divided by 5?', ['1.1', '1.5', '5.5', '11'], 0)]),
Sc('Science: Comets and Asteroids',
   'Grade 4 Science strand: a comet is a ball of ice and dust that develops a glowing tail as it nears the Sun, while an asteroid is a rocky object that orbits the Sun, often found in a belt between Mars and Jupiter.',
   [('What is a comet mostly made of?', ['Ice and dust', 'Only solid rock', 'A concept unrelated to space', 'Only metal'], 0),
    ('What is an asteroid mostly made of?', ['Rock', 'Only ice', 'A concept unrelated to space', 'Only gas'], 0),
    ('Does a comet develop a glowing tail as it nears the Sun?', ['Yes', 'No, comets never develop a tail', 'A concept unrelated to comets', 'Only asteroids develop tails'], 0),
    ('Where is a well-known belt of asteroids located in our solar system?', ['Between Mars and Jupiter', 'Between Earth and the Moon', 'A concept unrelated to the solar system', 'Beyond Pluto only'], 0),
    ('Why might scientists study comets and asteroids?', ['They can teach us about the early materials that formed our solar system', 'Comets and asteroids have no connection to the solar system', 'Studying comets and asteroids has no scientific value', 'This concept has no relevance to space science'], 0)]),
SS('Social Studies: The Role of Museums in Preserving History',
   'Grade 4 Social Studies strand: museums collect, preserve, and display historical artifacts and stories, helping communities learn about and remember important parts of their past.',
   [('What do museums do with historical artifacts, besides displaying them?', ['Collect and preserve them', 'Throw them away', 'A concept unrelated to museums', 'Ignore them completely'], 0),
    ('Do museums help communities learn about and remember their past?', ['Yes', 'No, museums have no connection to the past', 'A concept unrelated to history', 'Museums only display modern objects'], 0),
    ('Name one thing you might find preserved in a museum, such as an old artifact.', ['An old artifact', 'A concept unrelated to museums', 'A fresh loaf of bread', 'A brand new smartphone'], 0),
    ('Why is it important for museums to carefully preserve historical artifacts?', ['So future generations can learn about and understand the past', 'Preserving artifacts has no value to a community', 'Historical artifacts never need any care at all', 'This concept has no relevance to social studies'], 0),
    ('How might visiting a museum help a student understand a historical event better than just reading about it?', ['Seeing real artifacts and exhibits can make history feel more real and memorable', 'Museums never help anyone understand history', 'This concept has no connection to learning about the past', 'Reading and visiting a museum are always exactly the same experience'], 0)]),
]),

day(83, [
L('Reading: Analyzing Symbolism in Stories',
  'Grade 4 Language strand: symbolism is when an author uses an object, colour, or image to represent a deeper idea, such as a dove often symbolizing peace.',
  [('What do we call it when an author uses an object to represent a deeper idea?', ['Symbolism', 'A concept unrelated to reading', 'A grammar rule', 'A math pattern'], 0),
   ('What does a dove often symbolize in stories?', ['Peace', 'War', 'A concept unrelated to symbolism', 'Anger'], 0),
   ('Can a colour, like the colour black, be used as a symbol in a story?', ['Yes', 'No, colours are never used as symbols', 'A concept unrelated to reading', 'Only objects can be symbols, never colours'], 0),
   ('Why might an author use symbolism instead of directly stating an idea?', ['It can add deeper meaning and invite readers to think more carefully', 'Symbolism never adds meaning to a story', 'This concept has no connection to storytelling', 'Authors should always state ideas directly and never use symbols'], 0),
   ('If a story repeatedly shows a wilting flower as a character grows sadder, what might the flower symbolize?', ['The character’s fading hope or happiness', 'A concept unrelated to the character’s feelings', 'Nothing at all connected to the story', 'The flower has no symbolic meaning'], 0)]),
M('Geometry: Classifying Quadrilaterals by Properties',
  'Grade 4 Math strand: quadrilaterals can be classified by their properties, such as a parallelogram having two pairs of parallel sides, and a rhombus having four equal sides.',
  [('How many pairs of parallel sides does a parallelogram have?', ['Two', 'One', 'Zero', 'Four'], 0),
   ('How many equal sides does a rhombus have?', ['Four', 'Two', 'Three', 'Zero'], 0),
   ('Is a square a special type of rhombus with four right angles?', ['Yes', 'No, a square is never a rhombus', 'A concept unrelated to quadrilaterals', 'A square has no right angles'], 0),
   ('What property must a shape have to be classified as a quadrilateral?', ['Four sides', 'Three sides', 'Five sides', 'No sides at all'], 0),
   ('Which of these shapes always has four equal sides?', ['A rhombus', 'A rectangle that is not a square', 'A trapezoid', 'A triangle'], 0)]),
Sc('Science: Weather Fronts and Air Masses',
   'Grade 4 Science strand: an air mass is a large body of air with a similar temperature and moisture, and a front is where two different air masses meet, often causing changes in the weather.',
   [('What do we call a large body of air with a similar temperature and moisture?', ['An air mass', 'A concept unrelated to weather', 'A rock formation', 'A type of soil'], 0),
    ('What do we call the place where two different air masses meet?', ['A front', 'A concept unrelated to weather', 'A tide', 'A rock cycle'], 0),
    ('Can a front cause changes in the weather?', ['Yes', 'No, fronts never affect the weather', 'A concept unrelated to weather', 'Fronts only occur in the ocean'], 0),
    ('Why might meteorologists track air masses and fronts to predict weather?', ['Where air masses meet can signal upcoming changes, like rain or temperature shifts', 'Air masses and fronts have no connection to weather prediction', 'This concept has no relevance to science', 'Weather never actually changes because of fronts'], 0),
    ('What might happen when a cold air mass meets a warm air mass?', ['Weather changes can occur, such as clouds or precipitation forming', 'Nothing at all happens when air masses meet', 'This concept has no connection to weather patterns', 'The two air masses always instantly become identical'], 0)]),
SS('Social Studies: Canada’s Peacekeeping Role Internationally',
   'Grade 4 Social Studies strand: Canada has a history of contributing peacekeepers, often through the United Nations, to help maintain peace and stability in regions experiencing conflict.',
   [('What do we call soldiers sent to help maintain peace in a conflict region?', ['Peacekeepers', 'A concept unrelated to international relations', 'Firefighters', 'Postal workers'], 0),
    ('Has Canada historically contributed peacekeepers to international efforts?', ['Yes', 'No, Canada has never contributed peacekeepers', 'A concept unrelated to Canada', 'Only other countries send peacekeepers'], 0),
    ('Through what international organization has Canada often sent peacekeepers?', ['The United Nations', 'A concept unrelated to peacekeeping', 'A single private company', 'A local town council'], 0),
    ('Why might a country choose to send peacekeepers to a conflict region?', ['To help maintain peace and stability where conflict is occurring', 'Peacekeepers never help with maintaining peace', 'This concept has no connection to international relations', 'Sending peacekeepers always increases conflict'], 0),
    ('Why might Canada’s peacekeeping role be an important part of its national identity?', ['It reflects Canada’s values of cooperation and supporting global peace', 'Peacekeeping has no connection to national identity', 'This concept has no relevance to Canadian history', 'Canada has no international role at all'], 0)]),
]),

day(84, [
L('Writing: Writing a Speech',
  'Grade 4 Language strand: a speech is a piece of writing meant to be spoken aloud to an audience, often including a strong opening, clear main points, and a memorable closing.',
  [('What kind of writing is meant to be spoken aloud to an audience?', ['A speech', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Should a speech include a strong opening to capture the audience’s attention?', ['Yes', 'No, openings are never important in a speech', 'A concept unrelated to writing', 'Only the closing matters in a speech'], 0),
   ('Should a speech include clear main points for the audience to follow?', ['Yes', 'No, speeches should never have any main points', 'A concept unrelated to writing', 'Main points are only needed in essays, never speeches'], 0),
   ('Why might a speech benefit from a memorable closing?', ['It helps the message stick with the audience after the speech ends', 'Closings never affect how an audience remembers a speech', 'This concept has no connection to writing a speech', 'A speech should never have any kind of ending'], 0),
   ('Which of these is most likely the opening line of a speech about kindness?', ['Have you ever wondered how one small act of kindness can change someone’s whole day?', 'The chemical symbol for water is H2O.', 'Add 3 and 4 to get 7.', 'A triangle has three sides.'], 0)]),
M('Data: Stem-and-Leaf Plots',
  'Grade 4 Math strand: a stem-and-leaf plot organizes numerical data by splitting each number into a stem, its leading digit or digits, and a leaf, its final digit, making patterns in the data easier to see.',
  [('In a stem-and-leaf plot, what does the stem usually represent?', ['The leading digit or digits of a number', 'The final digit of a number', 'A concept unrelated to data', 'The colour of the data'], 0),
   ('In a stem-and-leaf plot, what does the leaf usually represent?', ['The final digit of a number', 'The leading digit of a number', 'A concept unrelated to data', 'The average of the data'], 0),
   ('In the number 42, if 4 is the stem, what is the leaf?', ['2', '4', '42', '24'], 0),
   ('Why might a stem-and-leaf plot be useful for organizing a set of test scores?', ['It can show patterns in the data, like where most scores cluster', 'Stem-and-leaf plots never show any patterns', 'This concept has no connection to organizing data', 'Test scores can never be organized in a plot'], 0),
   ('What is a key benefit of a stem-and-leaf plot compared to just a list of numbers?', ['It keeps the exact values while also showing the data’s overall shape', 'A stem-and-leaf plot always hides the exact values', 'This concept has no benefit at all', 'Lists of numbers are always clearer than a stem-and-leaf plot'], 0)]),
Sc('Science: Air Pollution and Clean Air Initiatives',
   'Grade 4 Science strand: air pollution happens when harmful substances, such as smoke or chemicals, enter the air, and clean air initiatives, like reducing car emissions, help protect air quality.',
   [('What happens when harmful substances like smoke enter the air?', ['Air pollution', 'Clean air', 'A concept unrelated to air quality', 'Photosynthesis'], 0),
    ('Name one example of a clean air initiative, such as reducing car emissions.', ['Reducing car emissions', 'A concept unrelated to air quality', 'Increasing pollution on purpose', 'Ignoring air quality completely'], 0),
    ('Can air pollution be harmful to people and the environment?', ['Yes', 'No, air pollution is never harmful', 'A concept unrelated to air quality', 'Air pollution only affects plants, never people'], 0),
    ('Why might a city encourage people to use public transportation instead of cars?', ['It can help reduce air pollution from car emissions', 'Public transportation has no connection to air quality', 'Using cars always improves air quality', 'This concept has no relevance to science'], 0),
    ('Why is monitoring air quality important for a community’s health?', ['Poor air quality can affect breathing and overall health', 'Air quality has no connection to health', 'This concept has no relevance to science', 'Air pollution never actually affects anyone’s health'], 0)]),
SS('Social Studies: Comparing Monarchy, Democracy, and Dictatorship',
   'Grade 4 Social Studies strand: countries can be governed in different ways, including a monarchy led by a king or queen, a democracy where citizens vote for leaders, and a dictatorship led by one person with total control.',
   [('In a monarchy, who typically leads the country?', ['A king or queen', 'Citizens who vote', 'A concept unrelated to government', 'No one leads at all'], 0),
    ('In a democracy, how are leaders typically chosen?', ['Citizens vote for them', 'A single king or queen decides', 'A concept unrelated to government', 'Leaders are chosen at random'], 0),
    ('In a dictatorship, how much control does typically one single leader have?', ['Total control', 'No control at all', 'A concept unrelated to government', 'Equal control shared among all citizens'], 0),
    ('Why might citizens in a democracy have more say in their government compared to a dictatorship?', ['Citizens in a democracy can vote for their leaders and influence decisions', 'Citizens never have any say in a democracy', 'Democracies and dictatorships work in exactly the same way', 'This concept has no relevance to government systems'], 0),
    ('Why is it useful to compare different systems of government, like monarchy, democracy, and dictatorship?', ['It helps us understand how power and decisions are organized differently around the world', 'Comparing government systems has no educational value', 'All systems of government are always identical', 'This concept has no relevance to social studies'], 0)]),
]),

day(85, [
L('Figurative Language: Oxymorons',
  'Grade 4 Language strand: an oxymoron combines two contradictory words for effect, such as jumbo shrimp or deafening silence, creating an interesting or thought-provoking phrase.',
  [('What do we call a phrase that combines two contradictory words, like jumbo shrimp?', ['An oxymoron', 'A concept unrelated to figurative language', 'A synonym', 'A homophone'], 0),
   ('Which of these is an example of an oxymoron?', ['Deafening silence', 'A quiet library', 'A loud concert', 'A silent night'], 0),
   ('Why do the two words in an oxymoron seem to contradict each other?', ['They have opposite or conflicting meanings', 'The two words always mean the exact same thing', 'This concept has no connection to figurative language', 'Oxymorons never actually combine two words'], 0),
   ('Why might a writer use an oxymoron like bittersweet in their writing?', ['It can capture a complex feeling that a single word cannot fully express', 'Oxymorons never add any meaning to writing', 'This concept has no connection to figurative language', 'A bittersweet feeling can always be described with just one simple word'], 0),
   ('Which of these phrases is an oxymoron?', ['Original copy', 'Bright sunshine', 'Tall building', 'Fast car'], 0)]),
M('Fractions: Adding Mixed Numbers',
  'Grade 4 Math strand: students learn to add two mixed numbers, such as 2 and 1 fourth plus 1 and 2 fourths, by adding the whole numbers and the fractions separately, then combining the results.',
  [('What is 2 and 1 fourth plus 1 and 2 fourths?', ['3 and 3 fourths', '3 and 1 fourth', '4 and 3 fourths', '3 and 2 fourths'], 0),
   ('What is 1 and 1 third plus 1 and 1 third?', ['2 and 2 thirds', '2 and 1 third', '3 and 2 thirds', '1 and 2 thirds'], 0),
   ('What is 3 and 1 fifth plus 2 and 2 fifths?', ['5 and 3 fifths', '5 and 2 fifths', '6 and 3 fifths', '5 and 1 fifth'], 0),
   ('When adding mixed numbers, what should you add first?', ['The whole numbers and the fractions can each be added separately', 'Only the whole numbers, ignoring the fractions completely', 'Only the fractions, ignoring the whole numbers completely', 'Neither part should ever be added'], 0),
   ('What is 4 and 2 sixths plus 1 and 3 sixths?', ['5 and 5 sixths', '5 and 6 sixths', '6 and 5 sixths', '5 and 2 sixths'], 0)]),
Sc('Science: Desert Survival Strategies',
   'Grade 4 Science strand: desert plants and animals have special adaptations for survival, such as storing water, being active at night to avoid heat, and having features that reduce water loss.',
   [('Name one adaptation of a desert plant, such as storing water.', ['Storing water', 'A concept unrelated to desert survival', 'Growing in deep snow', 'Living underwater'], 0),
    ('Do some desert animals stay active at night to avoid daytime heat?', ['Yes', 'No, all desert animals are active only during the hottest part of the day', 'A concept unrelated to adaptations', 'Desert animals are never affected by heat'], 0),
    ('Why might a desert animal have features that reduce water loss?', ['Water is scarce in the desert, so conserving it helps the animal survive', 'Water loss has no connection to desert survival', 'Deserts always have plenty of available water', 'This concept has no relevance to adaptations'], 0),
    ('Why do many desert animals rest during the hottest part of the day?', ['To avoid losing too much water and overheating', 'Resting has no connection to surviving desert heat', 'Desert animals never need to avoid the heat', 'This concept has no relevance to science'], 0),
    ('Why might a cactus’s thick, waxy skin help it survive in the desert?', ['It helps the plant hold onto its stored water longer', 'Thick skin has no connection to water loss', 'Cacti never need to store any water', 'This concept has no relevance to desert adaptations'], 0)]),
SS('Social Studies: The Role of the United Nations',
   'Grade 4 Social Studies strand: the United Nations is an international organization where countries work together on issues like peace, human rights, and humanitarian aid.',
   [('What do we call the international organization where countries work together on global issues?', ['The United Nations', 'A concept unrelated to international relations', 'A single country’s government', 'A local town council'], 0),
    ('Name one issue the United Nations works on, such as peace or human rights.', ['Peace', 'A concept unrelated to the United Nations', 'A local school rule', 'A backyard garden'], 0),
    ('Do many different countries work together as part of the United Nations?', ['Yes', 'No, only one single country is involved', 'A concept unrelated to the United Nations', 'The United Nations has no members at all'], 0),
    ('Why might countries choose to work together through an organization like the United Nations?', ['Cooperating can help solve problems that affect many countries at once', 'Countries never benefit from working together', 'This concept has no connection to international relations', 'Global issues never require cooperation between countries'], 0),
    ('Why might humanitarian aid be an important part of the United Nations’ work?', ['It can help people affected by disasters or conflict around the world', 'Humanitarian aid has no connection to the United Nations', 'This concept has no relevance to social studies', 'People affected by disasters never need any help'], 0)]),
]),

day(86, [
L('Grammar: Correlative Conjunctions',
  'Grade 4 Language strand: correlative conjunctions are pairs of words that work together to join related ideas, such as either/or, neither/nor, and both/and.',
  [('Correlative conjunctions are pairs of words that work together to do what?', ['Join related ideas', 'A concept unrelated to grammar', 'Replace all nouns in a sentence', 'End every sentence'], 0),
   ('Which of these is a pair of correlative conjunctions?', ['Either/or', 'Cat/dog', 'Run/jump', 'Blue/red'], 0),
   ('Which of these is a pair of correlative conjunctions?', ['Neither/nor', 'Happy/sad', 'Fast/slow', 'Up/down'], 0),
   ('Which sentence correctly uses correlative conjunctions?', ['Either you can walk, or you can bike.', 'Either walk you can, bike or you can.', 'You either can walk bike or you can.', 'Bike or you can either walk you can.'], 0),
   ('Why might a writer use both/and to join two ideas?', ['To show that both ideas are true or included together', 'Both/and always shows a choice between two ideas', 'This concept has no connection to grammar', 'Both/and can never be used to join ideas'], 0)]),
M('Measurement: Converting Between Metric Units of Mass',
  'Grade 4 Math strand: students learn to convert between metric units of mass, knowing that 1 kilogram equals 1000 grams, to solve problems involving weight.',
  [('How many grams are in 1 kilogram?', ['1000', '100', '10', '10000'], 0),
   ('How many grams are in 2 kilograms?', ['2000', '200', '20', '20000'], 0),
   ('If an object has a mass of 500 grams, is that more or less than half a kilogram?', ['Exactly half a kilogram', 'More than half a kilogram', 'Less than half a kilogram', 'Cannot tell'], 0),
   ('Converting 3000 grams into kilograms gives you how many kilograms?', ['3', '30', '300', '3000'], 0),
   ('Why is it useful to convert between grams and kilograms?', ['It helps compare or combine measurements given in different units', 'Converting units never has any real use', 'This concept has no connection to measurement', 'Grams and kilograms can never be compared'], 0)]),
Sc('Science: Chemical Reactions: Signs That a New Substance Formed',
   'Grade 4 Science strand: signs that a chemical reaction has occurred include a colour change, bubbles forming, a new smell, or heat being given off, showing that a new substance was created.',
   [('Name one sign that a chemical reaction may have occurred, such as bubbles forming.', ['Bubbles forming', 'A concept unrelated to chemical reactions', 'The object staying exactly the same', 'Nothing happening at all'], 0),
    ('Can a colour change be a sign that a chemical reaction has occurred?', ['Yes', 'No, colour changes never indicate a reaction', 'A concept unrelated to chemistry', 'Colour changes only happen during physical changes'], 0),
    ('Can heat being given off be a sign of a chemical reaction?', ['Yes', 'No, heat is never connected to chemical reactions', 'A concept unrelated to chemistry', 'Heat only occurs during freezing'], 0),
    ('Why do scientists look for signs like bubbles or colour changes when studying a reaction?', ['These signs can indicate that a new substance has formed', 'These signs have no connection to chemical reactions', 'This concept has no relevance to science', 'A new substance never actually forms during a reaction'], 0),
    ('Why might baking a cake be considered an example of a chemical reaction?', ['The ingredients combine and change to form a completely new substance', 'Baking a cake never actually changes the ingredients at all', 'This concept has no connection to chemical reactions', 'A cake is exactly the same as its raw ingredients'], 0)]),
SS('Social Studies: Canada’s Immigration Policies Today',
   'Grade 4 Social Studies strand: Canada has immigration policies today that determine how people from other countries can come to live, work, or study in Canada, contributing to the country’s diversity.',
   [('What do we call the rules that determine how people can come to live in Canada?', ['Immigration policies', 'A concept unrelated to government', 'Traffic laws', 'School rules'], 0),
    ('Can people come to Canada to work or study through immigration policies?', ['Yes', 'No, immigration policies only apply to tourists', 'A concept unrelated to immigration', 'No one is ever allowed to come to Canada'], 0),
    ('Do immigrants contribute to Canada’s diversity?', ['Yes', 'No, immigrants have no effect on Canada’s diversity', 'A concept unrelated to immigration', 'Diversity has no connection to immigration'], 0),
    ('Why might Canada have specific policies for immigration rather than no rules at all?', ['Policies help organize and manage how people come to live, work, or study in the country', 'Immigration policies serve no real purpose', 'This concept has no connection to government', 'Countries never need any immigration policies'], 0),
    ('How might immigration contribute to Canada’s economy and culture?', ['Immigrants can bring new skills, ideas, and traditions that enrich communities', 'Immigration never affects a country’s economy or culture', 'This concept has no relevance to social studies', 'Immigrants never contribute anything to a country'], 0)]),
]),

day(87, [
L('Reading: Evaluating an Author’s Credibility',
  'Grade 4 Language strand: evaluating an author’s credibility means considering whether the author is a trustworthy source, such as checking their expertise or whether their information can be verified.',
  [('What does it mean to evaluate an author’s credibility?', ['Considering whether the author is a trustworthy source', 'Ignoring the author completely', 'A concept unrelated to reading', 'Assuming every author is always correct with no evidence'], 0),
   ('Name one way to check an author’s credibility, such as checking their expertise.', ['Checking their expertise', 'A concept unrelated to credibility', 'Ignoring the topic entirely', 'Guessing without any evidence'], 0),
   ('Should readers consider whether information can be verified when evaluating credibility?', ['Yes', 'No, verification is never important', 'A concept unrelated to reading', 'Only the length of a text matters for credibility'], 0),
   ('Why is it important to evaluate an author’s credibility before trusting their claims?', ['It helps readers judge whether information is accurate and reliable', 'Credibility never affects how reliable information is', 'This concept has no connection to reading comprehension', 'All authors are always completely trustworthy no matter what'], 0),
   ('Which of these might suggest an author is credible on a science topic?', ['The author has expertise or training in that scientific field', 'The author has never studied the topic at all', 'The author’s book has a colourful cover', 'The author wrote the book very quickly'], 0)]),
M('Probability: Calculating Simple Probability as a Fraction',
  'Grade 4 Math strand: students learn to express the probability of an event as a fraction, such as the chance of rolling a 4 on a 6-sided die being 1 out of 6.',
  [('What is the probability, as a fraction, of rolling a 4 on a 6-sided die?', ['1 sixth', '1 fourth', '4 sixths', '1 half'], 0),
   ('What is the probability, as a fraction, of flipping heads on a coin?', ['1 half', '1 fourth', '1 sixth', '1 third'], 0),
   ('If a bag has 3 red marbles and 2 blue marbles, what is the probability of picking a red marble?', ['3 fifths', '2 fifths', '3 halves', '1 fifth'], 0),
   ('To express probability as a fraction, what goes in the denominator?', ['The total number of possible outcomes', 'The number of favourable outcomes only', 'A concept unrelated to probability', 'Always the number 100'], 0),
   ('If a spinner has 4 equal sections and only 1 is red, what is the probability of landing on red?', ['1 fourth', '1 half', '4 fourths', '1 third'], 0)]),
Sc('Science: Eclipses — Solar and Lunar',
   'Grade 4 Science strand: a solar eclipse happens when the Moon passes between the Sun and Earth, blocking sunlight, while a lunar eclipse happens when Earth passes between the Sun and Moon.',
   [('What happens during a solar eclipse?', ['The Moon passes between the Sun and Earth', 'Earth passes between the Sun and Moon', 'A concept unrelated to eclipses', 'Nothing happens in the sky at all'], 0),
    ('What happens during a lunar eclipse?', ['Earth passes between the Sun and Moon', 'The Moon passes between the Sun and Earth', 'A concept unrelated to eclipses', 'The Sun disappears completely'], 0),
    ('During a solar eclipse, what does the Moon block?', ['Sunlight', 'Moonlight', 'A concept unrelated to eclipses', 'Nothing at all'], 0),
    ('Why do solar and lunar eclipses not happen every single month?', ['The Sun, Earth, and Moon must align in a very specific way, which does not happen every month', 'Eclipses actually happen every single day', 'This concept has no connection to the Sun, Earth, and Moon', 'The Moon never moves in any predictable pattern'], 0),
    ('Why should people avoid looking directly at a solar eclipse without proper eye protection?', ['Looking directly at the Sun, even during an eclipse, can damage the eyes', 'Solar eclipses are never harmful to look at directly', 'This concept has no connection to eye safety', 'Eclipses always make the Sun completely safe to view directly'], 0)]),
SS('Social Studies: Indigenous Land Acknowledgements: Why They Matter',
   'Grade 4 Social Studies strand: a land acknowledgement recognizes the Indigenous Peoples who have traditionally lived on and cared for the land, showing respect for their history and ongoing connection to it.',
   [('What do we call a statement recognizing the Indigenous Peoples connected to a piece of land?', ['A land acknowledgement', 'A concept unrelated to Indigenous history', 'A grocery list', 'A weather report'], 0),
    ('Does a land acknowledgement show respect for Indigenous history and connection to the land?', ['Yes', 'No, it shows no respect at all', 'A concept unrelated to Indigenous Peoples', 'It has no connection to history'], 0),
    ('Might a land acknowledgement be shared at the start of a school event or meeting?', ['Yes', 'No, land acknowledgements are never shared publicly', 'A concept unrelated to Indigenous Peoples', 'They are only shared in private'], 0),
    ('Why might communities choose to share a land acknowledgement?', ['To honour and recognize Indigenous Peoples’ long history and connection to the land', 'Land acknowledgements have no real purpose', 'This concept has no connection to Indigenous history', 'Communities never need to recognize any history at all'], 0),
    ('Why is understanding the meaning behind a land acknowledgement more valuable than simply reading it aloud?', ['Understanding its meaning helps build genuine respect and awareness, not just repetition', 'The meaning behind a land acknowledgement never matters at all', 'This concept has no relevance to social studies', 'Reading it aloud without understanding has the exact same value as understanding it'], 0)]),
]),

day(88, [
L('Vocabulary: Etymology — Where Words Come From',
  'Grade 4 Language strand: etymology is the study of where words come from and how their meanings have changed over time, often tracing English words back to Latin, Greek, or other languages.',
  [('What do we call the study of where words come from?', ['Etymology', 'A concept unrelated to vocabulary', 'Geometry', 'Geography'], 0),
   ('Do word meanings sometimes change over time?', ['Yes', 'No, word meanings never change', 'A concept unrelated to etymology', 'Words are never studied by anyone'], 0),
   ('Name one language that many English words can be traced back to, such as Latin.', ['Latin', 'A concept unrelated to etymology', 'A made-up language with no real speakers', 'A computer programming language'], 0),
   ('Why might learning about a word’s etymology help with understanding its meaning?', ['Knowing a word’s origin can reveal clues about its meaning', 'Etymology never provides any useful information about words', 'This concept has no connection to vocabulary', 'A word’s origin always has the opposite meaning of the word itself'], 0),
   ('Why might studying etymology help someone learn new vocabulary more easily?', ['Recognizing common word origins can help predict the meaning of unfamiliar words', 'Etymology never helps with learning new words', 'This concept has no relevance to vocabulary study', 'Every word has a completely unrelated, random origin'], 0)]),
M('Patterning: Algebraic Expressions with a Variable',
  'Grade 4 Math strand: students learn to write simple algebraic expressions using a variable, such as letting n represent an unknown number in the expression n plus 5.',
  [('In the expression n plus 5, what does the letter n represent?', ['An unknown number', 'Always the number 5', 'A concept unrelated to algebra', 'The answer to the expression'], 0),
   ('If n equals 3, what is the value of n plus 5?', ['8', '5', '3', '15'], 0),
   ('If n equals 10, what is the value of n minus 4?', ['6', '10', '4', '14'], 0),
   ('What do we call a letter used to represent an unknown number in an expression?', ['A variable', 'A constant', 'A concept unrelated to algebra', 'An operation'], 0),
   ('If a expression is written as 2 times n, and n equals 4, what is the value?', ['8', '2', '4', '6'], 0)]),
Sc('Science: Invasive Species and Their Effects',
   'Grade 4 Science strand: an invasive species is a plant or animal introduced to a new environment where it can spread quickly and harm native species by competing for food or space.',
   [('What do we call a plant or animal that spreads quickly in a new environment and can cause harm?', ['An invasive species', 'A native species', 'A concept unrelated to ecosystems', 'A domesticated species'], 0),
    ('Can an invasive species compete with native species for food or space?', ['Yes', 'No, invasive species never affect native species', 'A concept unrelated to ecosystems', 'Invasive species always help native species'], 0),
    ('Is an invasive species originally from the environment it is found in, or introduced from elsewhere?', ['Introduced from elsewhere', 'Originally from that environment', 'A concept unrelated to invasive species', 'Neither, it appears from nowhere'], 0),
    ('Why can invasive species be harmful to an ecosystem?', ['They can outcompete native species for resources, disrupting the balance of the ecosystem', 'Invasive species never have any effect on an ecosystem', 'This concept has no connection to ecosystems', 'Invasive species always help balance an ecosystem perfectly'], 0),
    ('Why might people be asked not to release aquarium fish into local lakes or rivers?', ['The fish could become an invasive species and harm the local ecosystem', 'Releasing aquarium fish never has any effect on an ecosystem', 'This concept has no relevance to science', 'Aquarium fish can never survive outside a tank'], 0)]),
SS('Social Studies: The History of Canadian Currency',
   'Grade 4 Social Studies strand: Canadian currency has changed over time, from early trade using items like fur pelts, to coins and paper bills, to today’s polymer bank notes.',
   [('Name one early form of trade used before coins existed, such as fur pelts.', ['Fur pelts', 'A concept unrelated to currency', 'Modern credit cards', 'Digital currency'], 0),
    ('Has Canadian currency changed over time?', ['Yes', 'No, currency has always been exactly the same', 'A concept unrelated to Canadian history', 'Currency never changes in any country'], 0),
    ('What material are today’s Canadian bank notes often made from?', ['Polymer', 'Only paper', 'Only cotton', 'A concept unrelated to currency'], 0),
    ('Why might a country update its currency over time, such as moving to polymer bank notes?', ['New materials or designs can improve durability and security', 'Currency changes have no real purpose', 'This concept has no connection to Canadian history', 'Countries never update their currency for any reason'], 0),
    ('Why is understanding the history of currency helpful for understanding a country’s economy?', ['It shows how trade and money have evolved to meet the needs of a growing society', 'The history of currency has no connection to the economy', 'This concept has no relevance to social studies', 'Currency has never changed in any meaningful way'], 0)]),
]),

day(89, [
L('Writing: Writing a Persuasive Letter to a Local Leader',
  'Grade 4 Language strand: a persuasive letter to a local leader states a clear opinion about a community issue, supported by reasons and evidence, aiming to convince the leader to take action.',
  [('What kind of writing states a clear opinion to convince a local leader to take action?', ['A persuasive letter', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Should a persuasive letter include reasons and evidence to support its opinion?', ['Yes', 'No, reasons and evidence are never needed', 'A concept unrelated to writing', 'Only the opinion matters, with no support at all'], 0),
   ('What is the goal of a persuasive letter to a local leader?', ['To convince the leader to take action on an issue', 'To simply describe a random unrelated topic', 'A concept unrelated to persuasive writing', 'To confuse the reader with no clear point'], 0),
   ('Why might a student write a persuasive letter about adding a crosswalk near their school?', ['To convince a local leader that the crosswalk would improve safety', 'Persuasive letters are never used for community issues', 'This concept has no connection to writing', 'A crosswalk has no connection to community safety'], 0),
   ('Which of these would strengthen a persuasive letter about protecting a local park?', ['Evidence showing how the park benefits the community', 'A random fact about a different country entirely', 'A drawing with no connection to the topic', 'A completely unrelated math equation'], 0)]),
M('Financial Literacy: Simple Interest Basics',
  'Grade 4 Math strand: simple interest is extra money earned or owed based on a percentage of an original amount, such as earning interest on money kept in a savings account.',
  [('What do we call extra money earned based on a percentage of an original amount?', ['Simple interest', 'A concept unrelated to money', 'A discount', 'A tax'], 0),
   ('Might a savings account earn simple interest over time?', ['Yes', 'No, savings accounts never earn any interest', 'A concept unrelated to finance', 'Interest is only ever owed, never earned'], 0),
   ('If you have 100 dollars in an account earning 5 dollars in interest, how much money do you have in total?', ['105 dollars', '100 dollars', '95 dollars', '5 dollars'], 0),
   ('Why might someone want to save money in an account that earns interest?', ['Their money can grow over time without any extra effort', 'Interest never actually adds any money to an account', 'This concept has no connection to saving money', 'Savings accounts always lose money over time'], 0),
   ('Simple interest is usually calculated as a percentage of the ___.', ['Original amount', 'Weather forecast', 'Time of day', 'Number of coins in a piggy bank'], 0)]),
Sc('Science: How a Generator Makes Electricity',
   'Grade 4 Science strand: a generator produces electricity by using motion, such as spinning magnets near coils of wire, to convert mechanical energy into electrical energy.',
   [('What does a generator produce?', ['Electricity', 'Sunlight', 'A concept unrelated to energy', 'Fresh water'], 0),
    ('Does a generator use motion, such as spinning magnets, to produce electricity?', ['Yes', 'No, generators never use any motion', 'A concept unrelated to generators', 'Generators only use sunlight'], 0),
    ('What type of energy does a generator convert into electrical energy?', ['Mechanical energy', 'Only sound energy', 'A concept unrelated to energy', 'Only light energy'], 0),
    ('Why might a generator be useful during a power outage?', ['It can produce electricity when the regular power supply is unavailable', 'Generators are never useful during a power outage', 'This concept has no connection to electricity', 'Generators can only be used when regular power is already working'], 0),
    ('Why is understanding how a generator works helpful for understanding renewable energy, like wind power?', ['Many renewable energy sources, like wind turbines, also use motion to generate electricity', 'Generators have no connection to renewable energy', 'This concept has no relevance to science', 'Wind power never actually produces any electricity'], 0)]),
SS('Social Studies: Global Trade Organizations and Agreements',
   'Grade 4 Social Studies strand: countries often join trade organizations or sign agreements to set shared rules for buying and selling goods internationally, helping trade run smoothly.',
   [('What do countries often join to set shared rules for international trade?', ['Trade organizations or agreements', 'A concept unrelated to global trade', 'A local sports league', 'A single school club'], 0),
    ('Do trade agreements help set rules for buying and selling goods between countries?', ['Yes', 'No, trade agreements have no connection to buying and selling goods', 'A concept unrelated to trade', 'Trade agreements only apply within one single country'], 0),
    ('Can trade organizations help trade run more smoothly between countries?', ['Yes', 'No, trade organizations always make trade more difficult', 'A concept unrelated to international relations', 'Trade organizations have no connection to trade at all'], 0),
    ('Why might countries want shared rules for international trade instead of each having completely different rules?', ['Shared rules can make trading goods more predictable and fair for everyone involved', 'Shared trade rules never actually help anyone', 'This concept has no connection to global trade', 'Countries never actually trade goods with each other'], 0),
    ('Why might joining a trade organization benefit a country’s economy?', ['It can open up new markets and opportunities to sell and buy goods', 'Joining a trade organization never benefits a country’s economy', 'This concept has no relevance to social studies', 'Trade organizations only exist to limit a country’s economy'], 0)]),
]),

day(90, [
L('Review: Vocabulary, Grammar, and Reading Skills (Days 81-89)',
  'Grade 4 Language strand review: students revisit portmanteau words, active and passive voice, symbolism, speech writing, oxymorons, correlative conjunctions, author credibility, etymology, and persuasive letters.',
  [('A portmanteau word blends the sounds and meanings of how many words?', ['Two', 'Three', 'Zero', 'A concept unrelated to vocabulary'], 0),
   ('In the active voice, does the subject perform the action or receive it?', ['Perform it', 'Receive it', 'A concept unrelated to grammar', 'Neither perform nor receive it'], 0),
   ('What do we call it when an author uses an object to represent a deeper idea?', ['Symbolism', 'A concept unrelated to reading', 'A grammar rule', 'A math pattern'], 0),
   ('What do we call a phrase that combines two contradictory words, like jumbo shrimp?', ['An oxymoron', 'A concept unrelated to figurative language', 'A synonym', 'A homophone'], 0),
   ('What do we call the study of where words come from?', ['Etymology', 'A concept unrelated to vocabulary', 'Geometry', 'Geography'], 0)]),
M('Review: Decimals, Fractions, and Data (Days 81-89)',
  'Grade 4 Math strand review: students revisit multiplying and dividing decimals, classifying quadrilaterals, stem-and-leaf plots, adding mixed numbers, converting mass, probability as a fraction, algebraic expressions, and simple interest.',
  [('What is 0.4 times 3?', ['1.2', '1.4', '0.7', '12'], 0),
   ('What is 6.4 divided by 2?', ['3.2', '3.4', '32', '2.2'], 0),
   ('How many equal sides does a rhombus have?', ['Four', 'Two', 'Three', 'Zero'], 0),
   ('What is 2 and 1 fourth plus 1 and 2 fourths?', ['3 and 3 fourths', '3 and 1 fourth', '4 and 3 fourths', '3 and 2 fourths'], 0),
   ('What is the probability, as a fraction, of flipping heads on a coin?', ['1 half', '1 fourth', '1 sixth', '1 third'], 0)]),
Sc('Review: Ecosystems, Earth and Space, and Physical Science (Days 81-89)',
   'Grade 4 Science strand review: students revisit food webs, comets and asteroids, weather fronts, air pollution, desert adaptations, chemical reactions, eclipses, invasive species, and generators.',
   [('Does a food web show a single path of energy, or many connected food chains?', ['Many connected food chains', 'A single path only', 'A concept unrelated to ecosystems', 'No connections at all'], 0),
    ('What is a comet mostly made of?', ['Ice and dust', 'Only solid rock', 'A concept unrelated to space', 'Only metal'], 0),
    ('What do we call the place where two different air masses meet?', ['A front', 'A concept unrelated to weather', 'A tide', 'A rock cycle'], 0),
    ('What happens during a solar eclipse?', ['The Moon passes between the Sun and Earth', 'Earth passes between the Sun and Moon', 'A concept unrelated to eclipses', 'Nothing happens in the sky at all'], 0),
    ('What does a generator produce?', ['Electricity', 'Sunlight', 'A concept unrelated to energy', 'Fresh water'], 0)]),
SS('Review: Ancient Societies, Government, and Global Connections (Days 81-89)',
   'Grade 4 Social Studies strand review: students revisit the Aztec civilization, museums, Canadian peacekeeping, comparing government systems, the United Nations, immigration policy, land acknowledgements, currency history, and global trade.',
   [('What was the name of the Aztec capital city?', ['Tenochtitlan', 'Rome', 'Athens', 'A concept unrelated to the Aztecs'], 0),
    ('What do we call soldiers sent to help maintain peace in a conflict region?', ['Peacekeepers', 'A concept unrelated to international relations', 'Firefighters', 'Postal workers'], 0),
    ('In a democracy, how are leaders typically chosen?', ['Citizens vote for them', 'A single king or queen decides', 'A concept unrelated to government', 'Leaders are chosen at random'], 0),
    ('What do we call a statement recognizing the Indigenous Peoples connected to a piece of land?', ['A land acknowledgement', 'A concept unrelated to Indigenous history', 'A grocery list', 'A weather report'], 0),
    ('What do countries often join to set shared rules for international trade?', ['Trade organizations or agreements', 'A concept unrelated to global trade', 'A local sports league', 'A single school club'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_81_90)
    append_to(4, g4_81_90)
