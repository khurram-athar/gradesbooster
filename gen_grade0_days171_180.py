#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 171-180 -- fifteenth batch, extending Grade 0
past Day 170. Self-contained script (does NOT use gen_curriculum.py's
sub()/day()/append_to(), since those do not support a worksheet field)
modeled exactly on gen_grade0_days161_170.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-170 (dumped and
checked against data/grade0.json before writing): word families -ay, -oy,
and -ink; vowel team oo; r-controlled vowel are; the suffix -ness; the
prefix non-; quotation marks for speech for Language. Skip counting by 9s,
number bonds to 13, counting to 150, adding two-digit numbers without
regrouping, elapsed time, comparing halves/thirds/fourths, making change
from a dollar, estimating and measuring with non-standard units, and
ordinal numbers 6th to 10th for Math. Life cycle of a sea turtle, crabs,
polar bears, snakes, glaciers, dolphins, sea otters, caves, and fireflies
for Science. Water treatment workers, meteorologists, beekeepers, the
Great Lakes, tailors and seamstresses, border officers, provincial
symbols, photographers, and Canadas national parks for Social Studies.
Day 180 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior batch, with review titles
textually distinct from every earlier review day's title for each
subject. No embedded ASCII double-quote or straight apostrophe characters
are used anywhere in title/summary/quiz/worksheet text -- contractions
and possessives are avoided entirely, matching this project's convention
(e.g. "Canadas" not "Canada's"), since this text gets embedded directly
into TypeScript string literals.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import lbl

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def sub(subject_key, title, summary, worksheet, quiz):
    return [subject_key, title, summary, worksheet, quiz]


def day(n, subs):
    return [n, subs]


def append_worksheet_days(grade, days):
    p = f'{DIR}/grade{grade}.ts'
    content = open(p).read().rstrip()
    if content.endswith('export default curriculum;'):
        content = content[:-len('export default curriculum;')].rstrip()
    if content.endswith('];'):
        content = content[:-len('];')].rstrip()
    if content.endswith(']}'):
        content += ','
    extra = []
    for d in days:
        n, subs = d
        extra.append(f'{{day:{n}, label:"{lbl(n)}", subjects:[')
        for s in subs:
            sk, ti, su, ws, quiz = s
            rl = f'YouTube: {ti}'
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} kindergarten educational')
            extra.append(f'  {{subject:"{sk}", title:"{ti}", summary:"{su}",')
            extra.append(f'   resourceLabel:"{rl}", resourceUrl:"{ru}",')
            extra.append('   quiz:[')
            for i, (q, opts, a) in enumerate(quiz):
                sep = ',' if i < len(quiz) - 1 else ''
                os2 = ','.join(f'"{o}"' for o in opts)
                extra.append(f'     {{q:"{q}", options:[{os2}], answer:{a}}}{sep}')
            extra.append('   ],')
            extra.append('   worksheet:[')
            for i, (prompt, answers) in enumerate(ws):
                sep = ',' if i < len(ws) - 1 else ''
                ans2 = ','.join(f'"{a}"' for a in answers)
                extra.append(f'     {{prompt:"{prompt}", answers:[{ans2}]}}{sep}')
            extra.append('   ]},')
        extra.append(']},')
    extra += ['];', '', 'export default curriculum;']
    open(p, 'w').write(content + '\n' + '\n'.join(extra))
    print(f'grade{grade}.ts appended {len(days)} days (with worksheets)')


def _rebalance_answer_positions(days, seed=20260818):
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
    return days


def L(t, s, ws, q):
    return sub('Language', t, s, ws, q)


def M(t, s, ws, q):
    return sub('Math', t, s, ws, q)


def Sc(t, s, ws, q):
    return sub('Science', t, s, ws, q)


def SS(t, s, ws, q):
    return sub('SocialStudies', t, s, ws, q)


g0_171_180 = [
day(171, [
L('Word Families: -ay Words',
  'Kindergarten Language strand: the -ay word family shares the same ending sound, as in day, play, way, and say.',
  [('Name a word that rhymes with day.', ['play', 'way', 'say']),
   ('What ending sound do play and way share?', ['ay', 'the ay sound']),
   ('Is stay part of the -ay family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ay family?', ['Sun', 'Play', 'Bed', 'Top'], 1),
   ('Which word rhymes with way?', ['Sit', 'Day', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -ay family?', ['Day', 'Play', 'Say', 'Sun'], 3),
   ('Complete the rhyme: We go outside every ___ to play.', ['day', 'dot', 'dip', 'den'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Skip Counting by 9s to 90',
  'Kindergarten Math strand: students skip count by 9s, saying 9, 18, 27, 36, and continuing on up to 90.',
  [('What number comes after 9, 18, 27?', ['36', 'thirty six']),
   ('Skip count by 9s from 9 to 45.', ['9,18,27,36,45', '9 18 27 36 45']),
   ('What number comes right before 90 when skip counting by 9s?', ['81', 'eighty one'])],
  [('What comes next: 9, 18, 27, ___?', ['28', '35', '36', '37'], 2),
   ('What comes next: 36, 45, 54, ___?', ['55', '60', '63', '64'], 2),
   ('When skip counting by 9s, what number comes after 63?', ['64', '68', '72', '74'], 2),
   ('Skip counting by 9s means we add ___ each time.', ['7', '8', '9', '10'], 2),
   ('Which list correctly skip counts by 9s?', ['9, 18, 27, 36', '9, 16, 27, 36', '9, 18, 24, 36', '9, 19, 27, 36'], 0)]),
Sc('Life Cycle of a Sea Turtle',
   'Kindergarten Science strand: a sea turtle hatches from an egg buried in warm sand, crawls to the ocean as a hatchling, and grows into a large swimming adult over many years.',
   [('Where does a sea turtle egg hatch?', ['in warm sand', 'buried sand on a beach']),
    ('What is a newly hatched sea turtle called?', ['a hatchling', 'hatchling']),
    ('Where does a sea turtle swim once it reaches the ocean?', ['in the ocean', 'the sea'])],
   [('Where does a sea turtle begin its life?', ['As an egg buried in warm sand', 'As an egg in a tree', 'As an adult in the ocean', 'As an egg in the snow'], 0),
    ('What is a newly hatched sea turtle called?', ['A hatchling', 'A tadpole', 'A cub', 'A nymph'], 0),
    ('Where does a hatchling sea turtle crawl toward after hatching?', ['The ocean', 'A mountain', 'A forest', 'A desert'], 0),
    ('How long does it take a sea turtle to grow into a large adult?', ['Many years', 'One day', 'One hour', 'One week'], 0),
    ('A sea turtle growing from an egg into a swimming adult is an example of a ___.', ['Life cycle', 'Food chain', 'Habitat', 'Season'], 0)]),
SS('Our Water Treatment Workers: Making Water Safe to Drink',
   'Kindergarten Social Studies strand: water treatment workers clean and test water so that it is safe for our community to drink, cook with, and use every day.',
   [('What do water treatment workers do to water?', ['clean and test it', 'make it safe to drink']),
    ('Why is testing water important?', ['so it is safe to drink', 'to make sure it is clean']),
    ('Name one thing we use clean water for.', ['drinking', 'cooking'])],
   [('What is the main job of a water treatment worker?', ['Cleaning and testing water', 'Cutting hair', 'Flying planes', 'Teaching school'], 0),
    ('Why do communities need clean water?', ['To drink, cook, and stay healthy', 'Clean water is not needed', 'To paint houses', 'To fly airplanes'], 0),
    ('What might happen if water is not tested and cleaned?', ['It could make people sick', 'Nothing would happen', 'It would turn into ice', 'It would disappear'], 0),
    ('Water treatment workers help keep our water ___.', ['Safe and clean', 'Dirty', 'Frozen', 'Invisible'], 0),
    ('Which of these is a job done by a water treatment worker?', ['Testing water for safety', 'Delivering mail', 'Building roads', 'Selling food'], 0)]),
]),
day(172, [
L('Word Families: -oy Words',
  'Kindergarten Language strand: the -oy word family shares the same ending sound, as in boy, toy, joy, and Roy.',
  [('Name a word that rhymes with toy.', ['boy', 'joy']),
   ('What ending sound do boy and joy share?', ['oy', 'the oy sound']),
   ('Is enjoy part of the -oy family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -oy family?', ['Sun', 'Toy', 'Bed', 'Top'], 1),
   ('Which word rhymes with boy?', ['Sit', 'Toy', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -oy family?', ['Toy', 'Boy', 'Joy', 'Sun'], 3),
   ('Complete the rhyme: My favourite thing to play with is a ___.', ['toy', 'top', 'tip', 'tap'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Number Bonds: Ways to Make 13',
  'Kindergarten Math strand: students explore the different pairs of numbers that add together to make 13, such as 6 and 7, or 9 and 4.',
  [('Name two numbers that add together to make 13.', ['6 and 7', '9 and 4']),
   ('If one part of 13 is 8, what is the other part?', ['5', 'five']),
   ('Is 13 an even or odd number?', ['odd', 'odd number'])],
  [('Which pair of numbers makes 13?', ['6 and 7', '5 and 9', '4 and 10', '3 and 8'], 0),
   ('If one part of 13 is 8, what is the other part?', ['3', '4', '5', '6'], 2),
   ('Which pair does NOT make 13?', ['9 and 4', '7 and 6', '10 and 3', '8 and 8'], 3),
   ('13 is one more than which number?', ['11', '12', '14', '15'], 1),
   ('Finding different ways to make the same number is called ___.', ['Number bonds', 'Skip counting', 'Estimating', 'Sorting'], 0)]),
Sc('Crabs: Ocean Animals with Claws',
   'Kindergarten Science strand: a crab is an ocean animal with a hard shell, ten legs, and two strong claws that it uses to grab food and defend itself.',
   [('How many legs does a crab have?', ['ten', '10']),
    ('What does a crab use its claws for?', ['to grab food', 'to defend itself']),
    ('What covers and protects a crabs body?', ['a hard shell', 'shell'])],
   [('How many legs does a crab have?', ['Six', 'Eight', 'Ten', 'Twelve'], 2),
    ('What does a crab use its claws for?', ['Grabbing food and defending itself', 'Flying', 'Digging tunnels only', 'Singing'], 0),
    ('What protects the soft body of a crab?', ['A hard shell', 'Feathers', 'Fur', 'Scales like a fish'], 0),
    ('Where does a crab usually live?', ['Near the ocean or on the beach', 'In a tree', 'In the desert', 'In the sky'], 0),
    ('A crab moving sideways along the sand shows how it likes to ___.', ['Move', 'Fly', 'Swim upward', 'Hide in trees'], 0)]),
SS('Our Meteorologists: Forecasting the Weather',
   'Kindergarten Social Studies strand: meteorologists study clouds, wind, and temperature to forecast the weather so that our community knows what to expect each day.',
   [('What do meteorologists study?', ['the weather', 'clouds and wind and temperature']),
    ('Why is a weather forecast helpful?', ['it tells us what to expect', 'so we can plan our day']),
    ('Name one tool a meteorologist might use.', ['a thermometer', 'a weather map'])],
   [('What is the main job of a meteorologist?', ['Forecasting the weather', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('Why do people find weather forecasts helpful?', ['They help us plan what to wear and do', 'Forecasts are never useful', 'They tell us what to eat', 'They tell us where to shop'], 0),
    ('Which of these might a meteorologist study?', ['Clouds, wind, and temperature', 'Only paintings', 'Only books', 'Only music'], 0),
    ('A meteorologist might warn a community about an approaching ___.', ['Storm', 'Birthday party', 'Parade', 'Bake sale'], 0),
    ('Meteorologists help communities stay ___.', ['Prepared and safe', 'Confused', 'Hungry', 'Lost'], 0)]),
]),
day(173, [
L('Word Families: -ink Words',
  'Kindergarten Language strand: the -ink word family shares the same ending sound, as in pink, sink, think, and wink.',
  [('Name a word that rhymes with pink.', ['sink', 'wink']),
   ('What ending sound do sink and think share?', ['ink', 'the ink sound']),
   ('Is drink part of the -ink family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ink family?', ['Sun', 'Pink', 'Bed', 'Top'], 1),
   ('Which word rhymes with sink?', ['Sit', 'Pink', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -ink family?', ['Pink', 'Sink', 'Wink', 'Sun'], 3),
   ('Complete the rhyme: Take a moment to stop and ___.', ['think', 'that', 'than', 'then'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Numbers to 150: Counting Beyond 120',
  'Kindergarten Math strand: students continue counting past 120, saying number names in order all the way up to 150.',
  [('What number comes after 120?', ['121', 'one hundred twenty one']),
   ('Count from 128 to 132.', ['128,129,130,131,132', '128 129 130 131 132']),
   ('What number comes right before 150?', ['149', 'one hundred forty nine'])],
  [('What number comes right after 129?', ['128', '130', '131', '140'], 1),
   ('Which number comes between 135 and 137?', ['134', '136', '138', '139'], 1),
   ('What number comes right before 150?', ['148', '149', '151', '152'], 1),
   ('Counting past 120 all the way to 150 means we say numbers in ___.', ['Order', 'Reverse only', 'Random order', 'Groups of five only'], 0),
   ('Which of these numbers is greater than 130?', ['142', '125', '118', '99'], 0)]),
Sc('Polar Bears: Giants of the Arctic Ice',
   'Kindergarten Science strand: a polar bear is a huge white-furred mammal that lives on Arctic ice and hunts seals to survive in the cold.',
   [('What colour is a polar bears fur?', ['white', 'white fur']),
    ('Where does a polar bear live?', ['on Arctic ice', 'the Arctic']),
    ('What does a polar bear hunt to survive?', ['seals', 'it hunts seals'])],
   [('What colour is a polar bears thick fur?', ['White', 'Black', 'Green', 'Orange'], 0),
    ('Where does a polar bear mostly live?', ['On Arctic ice', 'In a rainforest', 'In a desert', 'In the ocean depths'], 0),
    ('What does a polar bear often hunt for food?', ['Seals', 'Insects', 'Fruit', 'Grass'], 0),
    ('A polar bears thick fur and fat help it stay ___ in cold weather.', ['Warm', 'Cool', 'Wet', 'Dry'], 0),
    ('Polar bears are one of the largest ___ on Earth.', ['Land mammals', 'Insects', 'Fish', 'Birds'], 0)]),
SS('Our Beekeepers: Caring for Bees and Making Honey',
   'Kindergarten Social Studies strand: beekeepers care for hives of bees, helping them stay healthy so the bees can make honey and help pollinate flowers and crops.',
   [('What do beekeepers care for?', ['bees', 'hives of bees']),
    ('What do bees make that beekeepers collect?', ['honey', 'they collect honey']),
    ('Why are bees important to farms and gardens?', ['they pollinate flowers and crops', 'pollination'])],
   [('What is the main job of a beekeeper?', ['Caring for bees and hives', 'Fixing pipes', 'Cutting hair', 'Flying planes'], 0),
    ('What do bees make that beekeepers collect?', ['Honey', 'Milk', 'Bread', 'Juice'], 0),
    ('Why are bees important to farms and gardens?', ['They help pollinate flowers and crops', 'Bees are not helpful', 'They only make noise', 'They eat all the plants'], 0),
    ('A beekeeper wears special clothing mainly to ___.', ['Stay safe from stings', 'Stay warm in winter', 'Look fancy', 'Fly faster'], 0),
    ('Beekeepers help their community by providing ___.', ['Honey and healthy pollinated crops', 'Nothing useful', 'Only wax candles', 'Loud noise'], 0)]),
]),
day(174, [
L('Vowel Teams: oo Words',
  'Kindergarten Language strand: the letters oo together can make a long sound, as in moon and food, or a short sound, as in book and look.',
  [('What sound do the letters oo make in the word moon?', ['a long oo sound', 'long oo']),
   ('Give another word with the oo vowel team.', ['food', 'look']),
   ('Is book a word with the oo vowel team?', ['yes', 'yes it is'])],
  [('Which word has the oo vowel team?', ['Moon', 'Man', 'Mat', 'Mud'], 0),
   ('What sound do the letters oo make in the word food?', ['A long oo sound', 'A short a sound', 'A silent sound', 'A long e sound'], 0),
   ('Which of these words has the oo vowel team?', ['Book', 'Bake', 'Bike', 'Back'], 0),
   ('Complete the rhyme: At night we can see a bright round ___.', ['moon', 'man', 'map', 'mud'], 0),
   ('When two letters team up to make one sound, it is called a ___.', ['Vowel team', 'Consonant blend', 'Suffix', 'Prefix'], 0)]),
M('Addition: Adding Two-Digit Numbers Without Regrouping',
  'Kindergarten Math strand: students add two two-digit numbers by adding the ones together and the tens together, without needing to regroup.',
  [('What is 23 plus 15?', ['38', 'thirty eight']),
   ('When adding 34 and 22, what do you add first?', ['the ones', 'ones digits']),
   ('What is 41 plus 26?', ['67', 'sixty seven'])],
  [('What is 23 plus 15?', ['35', '36', '37', '38'], 3),
   ('What is 41 plus 26?', ['65', '66', '67', '68'], 2),
   ('When adding two two-digit numbers, which digits do we usually add first?', ['The ones digits', 'The tens digits', 'Neither digit', 'Only the first number'], 0),
   ('What is 32 plus 44?', ['74', '75', '76', '77'], 2),
   ('What is 50 plus 27?', ['76', '77', '78', '79'], 1)]),
Sc('Snakes: Legless Reptiles That Slither',
   'Kindergarten Science strand: a snake is a reptile with no legs that moves by slithering along the ground and uses its tongue to smell the air around it.',
   [('How many legs does a snake have?', ['none', 'zero']),
    ('How does a snake move?', ['it slithers', 'slithering']),
    ('What does a snake use its tongue for?', ['to smell the air', 'smelling'])],
   [('How many legs does a snake have?', ['Zero', 'Two', 'Four', 'Six'], 0),
    ('How does a snake move along the ground?', ['By slithering', 'By hopping', 'By flying', 'By rolling'], 0),
    ('What does a snake use its tongue to do?', ['Smell the air around it', 'Taste colours', 'Fly', 'Dig tunnels'], 0),
    ('A snake is what type of animal?', ['A reptile', 'A mammal', 'An insect', 'A bird'], 0),
    ('Some snakes shed their old ___ as they grow.', ['Skin', 'Legs', 'Wings', 'Fur'], 0)]),
SS('The Great Lakes: Freshwater Seas of Canada',
   'Kindergarten Social Studies strand: the Great Lakes are five enormous freshwater lakes along part of Canadas border, so large that they are sometimes called freshwater seas.',
   [('How many Great Lakes are there?', ['five', '5']),
    ('What kind of water is in the Great Lakes?', ['freshwater', 'fresh water']),
    ('Why are the Great Lakes sometimes called freshwater seas?', ['because they are so large', 'they are very big'])],
   [('How many Great Lakes are there?', ['Three', 'Four', 'Five', 'Six'], 2),
    ('What kind of water fills the Great Lakes?', ['Freshwater', 'Salt water', 'Rain only', 'Ice only'], 0),
    ('Why are the Great Lakes sometimes called freshwater seas?', ['Because they are so large', 'Because they taste salty', 'Because they are very small', 'Because they are frozen year round'], 0),
    ('The Great Lakes are located along part of Canadas border with which country?', ['The United States', 'Mexico', 'France', 'Brazil'], 0),
    ('Learning about the Great Lakes helps us understand Canadian ___.', ['Geography', 'Sports', 'Music', 'Cooking'], 0)]),
]),
day(175, [
L('R-Controlled Vowels: are Words',
  'Kindergarten Language strand: when the letters are appear together, they often make one sound, as in care, share, and bare.',
  [('What sound do the letters are make in the word care?', ['the are sound', 'air sound']),
   ('Give another word that has the are sound.', ['share', 'bare']),
   ('Does the are sound in share rhyme with care?', ['yes', 'yes it does'])],
  [('Which word has the are sound?', ['Care', 'Cat', 'Cup', 'Cot'], 0),
   ('Which of these words has the r-controlled are sound?', ['Share', 'Ship', 'Shop', 'Shut'], 0),
   ('Complete the rhyme: It is kind to ___ your toys with a friend.', ['share', 'shop', 'ship', 'shut'], 0),
   ('Which word rhymes with bare?', ['Bat', 'Bit', 'Care', 'But'], 2),
   ('R-controlled vowels change how a vowel ___.', ['Sounds', 'Looks on the page', 'Is spelled only', 'Is coloured'], 0)]),
M('Time: Elapsed Time - What Happens Next',
  'Kindergarten Math strand: students think about the order of events and how much time passes between one activity and the next, such as what happens after breakfast and before school.',
  [('What usually happens right after breakfast?', ['getting ready for school', 'brushing teeth']),
   ('Which happens first, lunch or dinner?', ['lunch', 'lunch happens first']),
   ('Why is it helpful to think about the order of our day?', ['it helps us know what comes next', 'it helps us plan'])],
  [('What usually happens right after waking up in the morning?', ['Getting dressed', 'Going to sleep', 'Eating dinner', 'Watching the sunset'], 0),
   ('Which meal usually happens first in the day?', ['Breakfast', 'Dinner', 'A midnight snack', 'Dessert'], 0),
   ('Thinking about what happens between two events is called thinking about ___.', ['Elapsed time', 'Weight', 'Colour', 'Shape'], 0),
   ('Which of these happens last in a typical school day?', ['Going home', 'Waking up', 'Eating breakfast', 'Getting dressed'], 0),
   ('Understanding the order of events helps us know what to do ___.', ['Next', 'Never', 'Randomly', 'Backwards only'], 0)]),
Sc('Glaciers: Rivers of Ice',
   'Kindergarten Science strand: a glacier is a giant, slow-moving river of ice formed from packed snow over many years in very cold places.',
   [('What is a glacier made of?', ['packed snow and ice', 'ice']),
    ('How does a glacier move?', ['slowly', 'very slowly']),
    ('Where are glaciers usually found?', ['in very cold places', 'cold places'])],
   [('What is a glacier?', ['A giant, slow-moving river of ice', 'A warm ocean current', 'A type of cloud', 'A desert sand dune'], 0),
    ('What is a glacier made of?', ['Packed snow and ice', 'Melted rock', 'Sand', 'Wood'], 0),
    ('Where are glaciers usually found?', ['In very cold places', 'In hot deserts', 'In rainforests', 'In grasslands'], 0),
    ('How fast does a glacier usually move?', ['Very slowly', 'Very quickly', 'Instantly', 'Never'], 0),
    ('Glaciers form over many ___ from packed snow.', ['Years', 'Minutes', 'Seconds', 'Hours'], 0)]),
SS('Our Tailors and Seamstresses: Making and Fixing Clothes',
   'Kindergarten Social Studies strand: tailors and seamstresses are workers who sew, make, and repair clothing so that people have clothes that fit well and last a long time.',
   [('What do tailors and seamstresses do?', ['sew and repair clothing', 'make and fix clothes']),
    ('Name one tool a tailor might use.', ['a needle', 'scissors']),
    ('Why might someone visit a tailor?', ['to fix or make clothing fit', 'to get clothes fixed'])],
   [('What is the main job of a tailor or seamstress?', ['Making and fixing clothes', 'Fixing pipes', 'Flying planes', 'Cooking food'], 0),
    ('Which tool might a tailor use?', ['A needle and thread', 'A stethoscope', 'A wrench', 'A shovel'], 0),
    ('Why might a person visit a tailor?', ['To have clothing fixed or made to fit', 'To buy groceries', 'To mail a letter', 'To see a doctor'], 0),
    ('Tailors help make sure our clothes ___.', ['Fit well and last a long time', 'Fall apart quickly', 'Disappear', 'Change colour'], 0),
    ('A seamstress uses a sewing machine mainly to ___.', ['Sew pieces of fabric together', 'Cook food', 'Deliver mail', 'Fly planes'], 0)]),
]),
day(176, [
L('Suffixes: Adding -ness to Change Meaning',
  'Kindergarten Language strand: adding the suffix -ness to the end of a word can turn it into a naming word, such as changing happy into happiness, meaning the state of being happy.',
  [('What does happiness mean?', ['the state of being happy', 'being happy']),
   ('What does the suffix -ness usually do to a word?', ['turns it into a naming word', 'changes it to describe a state']),
   ('Give an example of a word with the suffix -ness.', ['happiness', 'kindness'])],
  [('What does the word happiness mean?', ['The state of being happy', 'The state of being sad', 'A type of food', 'A colour'], 0),
   ('What does the suffix -ness usually add to a word?', ['The meaning of a state or quality', 'A number', 'A place', 'An action'], 0),
   ('Which word means the quality of being kind?', ['Kindness', 'Kindly', 'Kinder', 'Unkind'], 0),
   ('Adding -ness to the word soft makes the word ___.', ['Softness, meaning the quality of being soft', 'Softly', 'Softer', 'Unsoft'], 0),
   ('A suffix that turns a describing word into a naming word is often added to the ___ of a word.', ['End', 'Beginning', 'Middle', 'Nowhere'], 0)]),
M('Fractions: Comparing Halves, Thirds, and Fourths',
  'Kindergarten Math strand: students compare halves, thirds, and fourths to notice that as a whole is cut into more equal parts, each part becomes smaller.',
  [('Which is bigger, a half or a fourth of the same shape?', ['a half', 'half is bigger']),
   ('How many parts are in a whole cut into thirds?', ['3', 'three']),
   ('As a shape is cut into more equal parts, what happens to each part?', ['it gets smaller', 'each part becomes smaller'])],
  [('Which is larger, one half or one fourth of the same whole?', ['One half', 'One fourth', 'They are equal', 'Neither'], 0),
   ('How many equal parts are in a whole cut into thirds?', ['Two', 'Three', 'Four', 'Five'], 1),
   ('As a whole is cut into more equal parts, each part becomes ___.', ['Smaller', 'Larger', 'The same size', 'Invisible'], 0),
   ('Which fraction shows a whole cut into two equal parts?', ['A half', 'A third', 'A fourth', 'A whole'], 0),
   ('Comparing halves, thirds, and fourths helps us understand that fractions name ___.', ['Equal parts of a whole', 'Only whole numbers', 'Only large numbers', 'Colours'], 0)]),
Sc('Dolphins: Smart Swimmers of the Sea',
   'Kindergarten Science strand: a dolphin is a smart ocean mammal that breathes air through a blowhole and uses clicking sounds to find food and talk to other dolphins.',
   [('How does a dolphin breathe?', ['through a blowhole', 'it breathes air']),
    ('What does a dolphin use clicking sounds for?', ['to find food', 'to talk to other dolphins']),
    ('Is a dolphin a fish or a mammal?', ['a mammal', 'mammal'])],
   [('How does a dolphin breathe?', ['Through a blowhole', 'Through gills', 'Through its skin', 'It does not breathe'], 0),
    ('What does a dolphin use clicking sounds for?', ['Finding food and communicating', 'Seeing in the dark only', 'Swimming faster', 'Changing colour'], 0),
    ('Is a dolphin a fish or a mammal?', ['A mammal', 'A fish', 'An insect', 'A reptile'], 0),
    ('Dolphins often swim together in a group called a ___.', ['Pod', 'Herd', 'Flock', 'Pack'], 0),
    ('Dolphins are known for being very ___ animals.', ['Smart', 'Slow', 'Silent', 'Sleepy'], 0)]),
SS('Our Border Officers: Keeping Our Country Safe',
   'Kindergarten Social Studies strand: border officers check people and goods entering the country to help keep our communities safe and make sure rules are followed.',
   [('What do border officers check?', ['people and goods entering the country', 'travellers and goods']),
    ('Why is the work of border officers important?', ['it helps keep our country safe', 'to help follow the rules']),
    ('Name one place where a border officer might work.', ['an airport', 'a border crossing'])],
   [('What is the main job of a border officer?', ['Checking people and goods entering the country', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('Why is the work of a border officer important?', ['It helps keep our country safe', 'It is not important', 'It only sells tickets', 'It teaches school'], 0),
    ('Where might a border officer work?', ['At an airport or border crossing', 'Underwater', 'In outer space', 'In a kitchen'], 0),
    ('Border officers help make sure travellers follow the ___.', ['Rules', 'Weather', 'Recipes', 'Songs'], 0),
    ('Which of these might a border officer check?', ['Passports and bags', 'Grocery lists', 'Bus schedules', 'Library books'], 0)]),
]),
day(177, [
L('Prefixes: Adding Non- to Change Meaning',
  'Kindergarten Language strand: adding the prefix non- to the start of a word can mean not, such as changing fiction into nonfiction, meaning writing that is not made up.',
  [('What does nonfiction mean?', ['writing that is not made up', 'true writing']),
   ('What does the prefix non- usually mean?', ['not', 'the opposite of']),
   ('Give an example of a word with the prefix non-.', ['nonfiction', 'nonstop'])],
  [('What does the word nonfiction mean?', ['Writing that is true and not made up', 'A made-up story', 'A type of poem', 'A silent word'], 0),
   ('What does the prefix non- usually add to a word?', ['The meaning of not', 'The meaning of again', 'A number', 'A colour'], 0),
   ('Which word means without stopping?', ['Nonstop', 'Stopping', 'Stopped', 'Restop'], 0),
   ('Adding non- to the word sense makes the word ___.', ['Nonsense, meaning without sense', 'Sensible', 'Sensing only', 'Resense'], 0),
   ('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'Middle', 'Nowhere'], 0)]),
M('Money: Making Change from a Dollar',
  'Kindergarten Math strand: students figure out how much change should be given back when something costing less than a dollar is paid for with a dollar.',
  [('If something costs 60 cents and you pay with a dollar, how much change do you get back?', ['40 cents', '40']),
   ('How many cents are in one dollar?', ['100', 'one hundred']),
   ('If something costs 25 cents and you pay with a dollar, how much change do you get back?', ['75 cents', '75'])],
  [('If something costs 60 cents and you pay with a dollar, how much change should you get back?', ['30 cents', '35 cents', '40 cents', '45 cents'], 2),
   ('If something costs 25 cents and you pay with a dollar, how much change should you get back?', ['65 cents', '70 cents', '75 cents', '80 cents'], 2),
   ('How many cents are in one dollar?', ['50', '75', '100', '150'], 2),
   ('If something costs 90 cents and you pay with a dollar, how much change should you get back?', ['5 cents', '10 cents', '15 cents', '20 cents'], 1),
   ('Making change means figuring out how much money should be ___.', ['Given back', 'Kept forever', 'Thrown away', 'Hidden'], 0)]),
Sc('Sea Otters: Ocean Animals That Use Tools',
   'Kindergarten Science strand: a sea otter is a furry ocean mammal that floats on its back and uses rocks as tools to crack open shellfish for food.',
   [('What does a sea otter use to crack open shellfish?', ['a rock', 'rocks as tools']),
    ('How does a sea otter often rest or eat?', ['floating on its back', 'it floats']),
    ('What keeps a sea otter warm in cold water?', ['its thick fur', 'thick fur'])],
   [('What does a sea otter often use as a tool?', ['A rock', 'A stick', 'A shell only', 'A leaf'], 0),
    ('How does a sea otter often float and eat?', ['On its back', 'Upside down underwater', 'Buried in sand', 'Standing on land'], 0),
    ('What keeps a sea otter warm in cold ocean water?', ['Its thick fur', 'A shell', 'Blubber only', 'Feathers'], 0),
    ('Sea otters mainly eat ___.', ['Shellfish', 'Leaves', 'Grass', 'Fruit'], 0),
    ('Using a rock to crack open a shell shows that sea otters can use ___.', ['Tools', 'Fire', 'Wheels', 'Machines'], 0)]),
SS('Provincial Symbols: Flowers, Birds, and Trees of Our Province',
   'Kindergarten Social Studies strand: each Canadian province and territory has its own special symbols, such as an official flower, bird, or tree, that represent its identity.',
   [('Name one kind of symbol a province might have.', ['a flower', 'a bird']),
    ('What does an official provincial symbol represent?', ['the identity of the province', 'the province']),
    ('Why do provinces choose special symbols?', ['to represent their identity', 'to show what makes them special'])],
   [('Which of these can be an official symbol of a province?', ['A flower, bird, or tree', 'Only a number', 'Only a food', 'Only a colour'], 0),
    ('What does a provincial symbol usually represent?', ['The identity of the province', 'Nothing important', 'A type of weather', 'A single family'], 0),
    ('Why might a province choose an official flower or bird?', ['To represent what makes it special', 'Flowers have no meaning', 'To confuse people', 'To copy another province'], 0),
    ('Learning about provincial symbols helps us understand Canadian ___.', ['Diversity', 'Math', 'Cooking', 'Sports scores'], 0),
    ('Every Canadian province and territory has its own set of official ___.', ['Symbols', 'Languages only', 'Foods only', 'Songs only'], 0)]),
]),
day(178, [
L('Punctuation: Quotation Marks for Speech',
  'Kindergarten Language strand: quotation marks are used to show the exact words a character says out loud in a story.',
  [('What punctuation mark shows the exact words someone says?', ['quotation marks', 'quote marks']),
   ('Where do quotation marks go in a sentence with speech?', ['around the spoken words', 'before and after the words']),
   ('Give an example of a sentence that uses quotation marks.', ['She said, I am happy', 'He said, Look at that'])],
  [('What punctuation mark shows the exact words a character says?', ['Quotation marks', 'A period', 'A comma', 'A question mark'], 0),
   ('Where are quotation marks placed around spoken words?', ['Before and after the spoken words', 'Only at the end of the sentence', 'Only at the start of the sentence', 'Nowhere near the words'], 0),
   ('Which sentence correctly uses quotation marks?', ['She said, I am happy', 'She said I am happy', 'She said. I am happy.', 'She said; I am happy'], 0),
   ('Quotation marks help readers know that someone is ___.', ['Speaking', 'Sleeping', 'Running', 'Painting'], 0),
   ('Which of these would most likely use quotation marks?', ['A characters spoken words in a story', 'A list of numbers', 'A math equation', 'A single letter'], 0)]),
M('Measurement: Estimating and Measuring with Non-Standard Units',
  'Kindergarten Math strand: students estimate then measure the length of objects using non-standard units like paper clips or cubes, then check how close their estimate was.',
  [('Name a non-standard unit that could be used to measure length.', ['a paper clip', 'a cube']),
   ('What does it mean to estimate a length before measuring?', ['to guess about how long it is', 'to make a careful guess']),
   ('Why do we check our estimate after measuring?', ['to see how close our guess was', 'to compare it to the real length'])],
  [('Which of these could be used as a non-standard measuring unit?', ['A paper clip', 'A ruler with numbers', 'A thermometer', 'A clock'], 0),
   ('What does it mean to estimate a length?', ['To make a careful guess before measuring', 'To measure with a ruler exactly', 'To weigh an object', 'To count its sides'], 0),
   ('Why do we check our estimate after measuring an object?', ['To see how close our guess was', 'Checking is never useful', 'To make the object longer', 'To change its colour'], 0),
   ('If a pencil is about 8 paper clips long, this tells us its ___ using a non-standard unit.', ['Length', 'Weight', 'Temperature', 'Colour'], 0),
   ('Using non-standard units like cubes to measure helps us practice ___.', ['Measuring length', 'Telling time', 'Counting money', 'Sorting shapes'], 0)]),
Sc('Caves: Underground Homes for Bats and Bugs',
   'Kindergarten Science strand: a cave is a large, dark, hollow space underground or inside a mountain that provides shelter for animals like bats and insects.',
   [('Where are caves usually found?', ['underground or inside a mountain', 'underground']),
    ('Name one animal that might live in a cave.', ['a bat', 'a bug']),
    ('What is a cave usually like inside?', ['dark', 'large and dark'])],
   [('Where are caves usually found?', ['Underground or inside a mountain', 'Floating in the sky', 'On top of the ocean', 'Inside a cloud'], 0),
    ('Which animal often makes its home inside a cave?', ['A bat', 'A polar bear', 'A dolphin', 'A hummingbird'], 0),
    ('What is the inside of a cave usually like?', ['Dark and hollow', 'Bright and sunny', 'Full of water only', 'Covered in snow'], 0),
    ('Caves provide animals like bats with ___.', ['Shelter', 'Food only', 'Sunlight', 'Nothing useful'], 0),
    ('A cave habitat is mostly known for being ___.', ['Dark and sheltered', 'Bright and open', 'Underwater always', 'Covered in sand'], 0)]),
SS('Our Photographers: Capturing Special Moments',
   'Kindergarten Social Studies strand: photographers use cameras to capture special moments, such as celebrations and events, so that communities can remember them.',
   [('What tool does a photographer use?', ['a camera', 'camera']),
    ('What do photographers capture?', ['special moments', 'pictures of events']),
    ('Why might a community want photographs of an event?', ['to remember it', 'to look back on it later'])],
   [('What is the main job of a photographer?', ['Capturing special moments with a camera', 'Fixing pipes', 'Cutting hair', 'Flying planes'], 0),
    ('What tool does a photographer mainly use?', ['A camera', 'A stethoscope', 'A wrench', 'A shovel'], 0),
    ('Why might a community hire a photographer for an event?', ['To remember the special moment', 'Photographs are never useful', 'To make the event louder', 'To clean the venue'], 0),
    ('Photographs help people look back on ___.', ['Special memories', 'Nothing important', 'Only the weather', 'Only math problems'], 0),
    ('Which of these might a photographer take pictures of?', ['A community festival', 'A math test', 'A grocery list', 'A bus schedule'], 0)]),
]),
day(179, [
L('Text Connections: Relating Stories to Our Own Lives',
  'Kindergarten Language strand: readers make text connections by thinking about how a story relates to something that has happened in their own lives.',
  [('What is a text connection?', ['relating a story to your own life', 'connecting a story to something you know']),
   ('Why do readers make text connections?', ['to understand the story better', 'it helps understanding']),
   ('Give an example of a text connection you could make with a story about pets.', ['thinking about your own pet', 'remembering a pet you have'])],
  [('What is a text connection?', ['Relating a story to your own life', 'Reading the title only', 'Counting the pages', 'Looking at the cover only'], 0),
   ('Why might a reader make a text connection while reading?', ['It helps them understand the story better', 'Connections are never helpful', 'It makes the book longer', 'It changes the ending'], 0),
   ('Which is an example of making a text connection?', ['Thinking about your own pet while reading about a pet', 'Ignoring the story completely', 'Skipping every page', 'Closing the book immediately'], 0),
   ('Text connections can help readers feel more ___ to a story.', ['Connected', 'Confused', 'Bored', 'Distant'], 0),
   ('Making connections between a story and our own lives is a skill used by good ___.', ['Readers', 'Painters', 'Builders', 'Drivers'], 0)]),
M('Ordinal Numbers: 6th to 10th',
  'Kindergarten Math strand: students extend their understanding of ordinal numbers, naming positions from sixth to tenth in a line or sequence.',
  [('What ordinal number comes after fifth?', ['sixth', '6th']),
   ('What position is tenth in a line of ten people?', ['last', 'the last position']),
   ('What ordinal number comes between eighth and tenth?', ['ninth', '9th'])],
  [('What ordinal number comes right after fifth?', ['Sixth', 'Seventh', 'Fourth', 'Eighth'], 0),
   ('Which ordinal number describes the last position in a line of ten?', ['Tenth', 'Ninth', 'Fifth', 'First'], 0),
   ('What ordinal number comes between eighth and tenth?', ['Ninth', 'Seventh', 'Sixth', 'Fifth'], 0),
   ('If a child is seventh in line, how many children are in front of them?', ['5', '6', '7', '8'], 1),
   ('Ordinal numbers are used to describe ___ in a sequence.', ['Position', 'Weight', 'Colour', 'Temperature'], 0)]),
Sc('Fireflies: Bugs That Glow in the Dark',
   'Kindergarten Science strand: a firefly is a small flying insect that makes its own light using a special part of its body, glowing to attract other fireflies at night.',
   [('What does a firefly do at night?', ['it glows', 'makes light']),
    ('What part of a firefly makes light?', ['a special part of its body', 'its lower body']),
    ('Why does a firefly glow?', ['to attract other fireflies', 'to signal to other fireflies'])],
   [('What is special about a firefly?', ['It can make its own light', 'It can breathe underwater', 'It has no wings', 'It cannot fly'], 0),
    ('When do fireflies usually glow?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
    ('Why do fireflies glow?', ['To attract other fireflies', 'To scare away the sun', 'To stay cool', 'To dig tunnels'], 0),
    ('A firefly is what type of animal?', ['An insect', 'A mammal', 'A reptile', 'A fish'], 0),
    ('Fireflies making their own light is an example of something called ___.', ['Bioluminescence', 'Camouflage', 'Hibernation', 'Migration'], 0)]),
SS('Canadas National Parks: Protecting Special Places',
   'Kindergarten Social Studies strand: Canada has many national parks that protect forests, mountains, and wildlife so that special natural places can be enjoyed for years to come.',
   [('What do national parks protect?', ['forests, mountains, and wildlife', 'nature']),
    ('Why are national parks important?', ['they protect special places', 'so nature can be enjoyed for years to come']),
    ('Name one thing you might see in a national park.', ['wildlife', 'mountains'])],
   [('What do national parks help protect?', ['Forests, mountains, and wildlife', 'Only buildings', 'Only roads', 'Only stores'], 0),
    ('Why are national parks important to Canada?', ['They protect special natural places', 'They have no purpose', 'They are only for one family', 'They stop all animals from living there'], 0),
    ('Which of these might you see while visiting a national park?', ['Wildlife and mountains', 'A shopping mall', 'A hospital', 'A factory'], 0),
    ('National parks help make sure natural places can be enjoyed ___.', ['For years to come', 'Only once', 'Never again', 'Only by rangers'], 0),
    ('Protecting national parks is an example of caring for our ___.', ['Environment', 'Homework', 'Toys', 'Furniture'], 0)]),
]),
day(180, [
L('Language Review: New Sounds, Word Endings, and Punctuation',
  'Kindergarten Language strand review: students revisit the -ay, -oy, and -ink word families, vowel team oo, r-controlled are, the suffix -ness, the prefix non-, quotation marks, and making text connections.',
  [('Name a word from the -ay, -oy, or -ink family.', ['day', 'toy']),
   ('What does the prefix non- usually mean?', ['not']),
   ('What punctuation mark shows the exact words someone says?', ['quotation marks'])],
  [('Which word belongs to the -ay family?', ['Sun', 'Play', 'Bed', 'Top'], 1),
   ('Which word has the oo vowel team?', ['Moon', 'Man', 'Mat', 'Mud'], 0),
   ('What does the word nonfiction mean?', ['Writing that is true and not made up', 'A made-up story', 'A type of poem', 'A silent word'], 0),
   ('What punctuation mark shows the exact words a character says?', ['Quotation marks', 'A period', 'A comma', 'A question mark'], 0),
   ('What is a text connection?', ['Relating a story to your own life', 'Reading the title only', 'Counting the pages', 'Looking at the cover only'], 0)]),
M('Math Review: Number Bonds, Big Numbers, and Elapsed Time',
  'Kindergarten Math strand review: students revisit skip counting by 9s, number bonds to 13, counting to 150, adding two-digit numbers, elapsed time, comparing fractions, making change, non-standard measurement, and ordinal numbers to tenth.',
  [('What comes next: 9, 18, 27, ___?', ['36']),
   ('Which pair of numbers makes 13?', ['6 and 7']),
   ('What number comes right before 150?', ['149'])],
  [('What comes next: 9, 18, 27, ___?', ['28', '35', '36', '37'], 2),
   ('Which pair of numbers makes 13?', ['6 and 7', '5 and 9', '4 and 10', '3 and 8'], 0),
   ('What is 23 plus 15?', ['35', '36', '37', '38'], 3),
   ('If something costs 60 cents and you pay with a dollar, how much change should you get back?', ['30 cents', '35 cents', '40 cents', '45 cents'], 2),
   ('Which ordinal number describes the last position in a line of ten?', ['Tenth', 'Ninth', 'Fifth', 'First'], 0)]),
Sc('Science Review: New Animals, Ice, and Underground Life',
   'Kindergarten Science strand review: students revisit the life cycle of a sea turtle, crabs, polar bears, snakes, glaciers, dolphins, sea otters, caves, and fireflies.',
   [('Where does a sea turtle begin its life?', ['as an egg buried in warm sand']),
    ('What colour is a polar bears fur?', ['white']),
    ('Why do fireflies glow?', ['to attract other fireflies'])],
   [('Where does a sea turtle begin its life?', ['As an egg buried in warm sand', 'As an egg in a tree', 'As an adult in the ocean', 'As an egg in the snow'], 0),
    ('How many legs does a crab have?', ['Six', 'Eight', 'Ten', 'Twelve'], 2),
    ('What colour is a polar bears thick fur?', ['White', 'Black', 'Green', 'Orange'], 0),
    ('What is a glacier?', ['A giant, slow-moving river of ice', 'A warm ocean current', 'A type of cloud', 'A desert sand dune'], 0),
    ('Why do fireflies glow?', ['To attract other fireflies', 'To scare away the sun', 'To stay cool', 'To dig tunnels'], 0)]),
SS('Social Studies Review: Workers, Lakes, and Canadian Symbols',
   'Kindergarten Social Studies strand review: students revisit water treatment workers, meteorologists, beekeepers, the Great Lakes, tailors and seamstresses, border officers, provincial symbols, photographers, and Canadas national parks.',
   [('What is the main job of a water treatment worker?', ['cleaning and testing water']),
    ('How many Great Lakes are there?', ['five']),
    ('What is the main job of a photographer?', ['capturing special moments with a camera'])],
   [('What is the main job of a water treatment worker?', ['Cleaning and testing water', 'Cutting hair', 'Flying planes', 'Teaching school'], 0),
    ('What is the main job of a meteorologist?', ['Forecasting the weather', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('How many Great Lakes are there?', ['Three', 'Four', 'Five', 'Six'], 2),
    ('What is the main job of a border officer?', ['Checking people and goods entering the country', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('What is the main job of a photographer?', ['Capturing special moments with a camera', 'Fixing pipes', 'Cutting hair', 'Flying planes'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_171_180)
    append_worksheet_days(0, g0_171_180)
