#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 151-160 -- thirteenth batch, extending Grade 0
past Day 150. Self-contained script (does NOT use gen_curriculum.py's
sub()/day()/append_to(), since those do not support a worksheet field)
modeled exactly on gen_grade0_days141_150.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-150 (dumped
and checked against data/grade0.json before writing): word families -ut,
-un; suffixes -less; prefixes pre-; vowel teams oa and ea; r-controlled
vowels er and ir; story genre (fairy tales and fables); main idea;
alliteration for Language. Number bonds to 12, skip counting by 6s, ten
frames, numbers before and after, halving, comparing temperature with a
thermometer, sorting and counting a data collection, counting by odd
numbers, reading a clock to five-minute intervals for Math. Summer season
(the only individual season not yet covered -- autumn, winter, spring,
and a seasons review already exist), life cycle of a salmon, ants,
kangaroos, sharks, our stomach, desert habitats, hibernation, meteors for
Science. Paramedics, optometrists, chefs and cooks, saving and spending
money, Earth Day, Canadian currency symbols, our local council, ferry
workers, pilots for Social Studies. Day 160 is a review day across all
four subjects, matching the end-of-batch pattern used in every prior
batch, with review titles textually distinct from every earlier review
day's title for each subject. No embedded ASCII double-quote or straight
apostrophe characters are used anywhere in title/summary/quiz/worksheet
text -- contractions and possessives are avoided entirely, matching this
project's convention (e.g. "Canadas" not "Canada's"), since this text
gets embedded directly into TypeScript string literals.
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


def _rebalance_answer_positions(days, seed=20260809):
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


g0_151_160 = [
day(151, [
L('Word Families: -ut Words',
  'Kindergarten Language strand: the -ut word family shares the same ending sound, as in but, cut, hut, and nut.',
  [('Name a word that rhymes with cut.', ['but', 'hut', 'nut']),
   ('What ending sound do hut and nut share?', ['ut', 'the ut sound']),
   ('Is shut part of the -ut family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ut family?', ['Sun', 'Nut', 'Bed', 'Top'], 1),
   ('Which word rhymes with hut?', ['Sit', 'Nut', 'Sock', 'Sad'], 1),
   ('Which word does NOT belong to the -ut family?', ['Cut', 'Hut', 'Nut', 'Net'], 3),
   ('Complete the rhyme: A squirrel likes to eat a ___.', ['nut', 'net', 'nap', 'nod'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Number Bonds: Ways to Make 12',
  'Kindergarten Math strand: students find different pairs of numbers that add together to make 12, such as 7 and 5, or 9 and 3.',
  [('Name two numbers that add up to 12.', ['7 and 5', '9 and 3']),
   ('What is 10 plus 2?', ['12', 'twelve']),
   ('How many ways can you make 12 with two numbers?', ['many ways', 'several ways'])],
  [('Which pair of numbers makes 12?', ['5 and 5', '7 and 5', '4 and 4', '3 and 3'], 1),
   ('What is 10 + 2?', ['10', '11', '12', '13'], 2),
   ('What is 8 + 4?', ['10', '11', '12', '13'], 2),
   ('If one part of 12 is 9, the other part is ___.', ['2', '3', '4', '5'], 1),
   ('Number bonds show us different ways to make the same ___.', ['Colour', 'Total', 'Shape', 'Letter'], 1)]),
Sc('Summer Season',
   'Kindergarten Science strand: summer is a warm season with long sunny days, when many plants grow, flowers bloom, and children can play outside for a long time.',
   [('What is the weather usually like in summer?', ['warm', 'warm and sunny']),
    ('Name one thing you might do outside in summer.', ['swim', 'play outside']),
    ('What happens to many plants in summer?', ['they grow', 'they grow and bloom'])],
   [('What is summer weather usually like?', ['Cold and snowy', 'Warm and sunny', 'Very windy only', 'Always rainy'], 1),
    ('Which activity is common in summer?', ['Swimming outside', 'Building a snowman', 'Raking fallen leaves', 'Wearing a heavy winter coat'], 0),
    ('What happens to many plants during the summer?', ['They grow and bloom', 'They stop growing completely', 'They turn to ice', 'They disappear'], 0),
    ('Which season usually comes right before summer?', ['Spring', 'Winter', 'Autumn', 'There is no season before summer'], 0),
    ('Summer days are often ___ than winter days.', ['Longer and sunnier', 'Shorter and darker', 'Exactly the same', 'Always rainy'], 0)]),
SS('Our Paramedics: Helping in an Emergency',
   'Kindergarten Social Studies strand: paramedics are trained helpers who quickly come to give medical care when someone is hurt or very sick.',
   [('What do paramedics help with?', ['medical emergencies', 'helping people who are hurt or sick']),
    ('What vehicle do paramedics often drive?', ['an ambulance', 'ambulance']),
    ('Why is it important to call for help quickly in an emergency?', ['so paramedics can help fast', 'to get help right away'])],
   [('What is the main job of a paramedic?', ['Giving medical help in an emergency', 'Teaching math', 'Cooking food', 'Building houses'], 0),
    ('What vehicle do paramedics usually use to reach people quickly?', ['An ambulance', 'A bicycle', 'A sailboat', 'A school bus'], 0),
    ('Why do paramedics need to arrive quickly in an emergency?', ['To give medical help as soon as possible', 'Speed does not matter at all', 'To avoid helping anyone', 'Because they are always late'], 0),
    ('Which number can be called to ask for a paramedic in Canada?', ['911', '123', '555', '000'], 0),
    ('Paramedics are trained to help people who are ___.', ['Hurt or very sick', 'Playing a game', 'Reading a book', 'Cooking dinner'], 0)]),
]),
day(152, [
L('Word Families: -un Words',
  'Kindergarten Language strand: the -un word family shares the same ending sound, as in run, fun, sun, and bun.',
  [('Name a word that rhymes with run.', ['fun', 'sun', 'bun']),
   ('What ending sound do fun and sun share?', ['un', 'the un sound']),
   ('Is spun part of the -un family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -un family?', ['Cat', 'Sun', 'Bed', 'Top'], 1),
   ('Which word rhymes with fun?', ['Sit', 'Run', 'Sock', 'Sad'], 1),
   ('Which word does NOT belong to the -un family?', ['Run', 'Sun', 'Fun', 'Fin'], 3),
   ('Complete the rhyme: We like to play out in the ___.', ['sun', 'sat', 'sit', 'set'], 0),
   ('Recognizing word families helps us read new words that share the same ___.', ['Meaning', 'Ending sound', 'Colour', 'Number of letters'], 1)]),
M('Skip Counting by 6s to 60',
  'Kindergarten Math strand: students skip count by 6s, saying 6, 12, 18, 24, and continuing on up to 60.',
  [('What number comes after 6, 12, 18?', ['24', 'twenty four']),
   ('Skip count by 6s from 6 to 30.', ['6,12,18,24,30', '6 12 18 24 30']),
   ('What number comes right before 60 when skip counting by 6s?', ['54', 'fifty four'])],
  [('What comes next: 6, 12, 18, ___?', ['19', '20', '22', '24'], 3),
   ('What comes next: 24, 30, 36, ___?', ['37', '40', '42', '48'], 2),
   ('When skip counting by 6s, what number comes after 42?', ['43', '44', '46', '48'], 3),
   ('Skip counting by 6s means we add ___ each time.', ['2', '4', '6', '8'], 2),
   ('Which list correctly skip counts by 6s?', ['6, 12, 18, 24', '6, 8, 10, 12', '6, 12, 20, 24', '6, 10, 16, 24'], 0)]),
Sc('Life Cycle of a Salmon: Egg to Adult',
   'Kindergarten Science strand: a salmon begins life as an egg in a river, hatches and grows in fresh water, swims out to the ocean, and later returns to the river to lay its own eggs.',
   [('Where does a salmon begin its life?', ['as an egg in a river', 'in a river']),
    ('Where does a salmon travel to grow bigger?', ['the ocean', 'out to the ocean']),
    ('Where does an adult salmon return to lay eggs?', ['the river', 'back to the river'])],
   [('Where does a salmon life cycle begin?', ['As an egg in a river', 'As an egg in the desert', 'As an adult in the ocean', 'As an egg on a mountain'], 0),
    ('Where does a young salmon swim to as it grows?', ['The ocean', 'A dry field', 'A cave', 'The sky'], 0),
    ('Where does an adult salmon return to lay its eggs?', ['Back to the river where it hatched', 'To a desert', 'To a forest', 'Nowhere, it stays in the ocean'], 0),
    ('A salmon spends part of its life in fresh water and part in ___.', ['Salt water in the ocean', 'The sky', 'A tree', 'A cave'], 0),
    ('The salmon life cycle is an example of an animal that ___.', ['Travels between two kinds of homes', 'Never moves at all', 'Lives only in the desert', 'Lives only on land'], 0)]),
SS('Our Optometrist: Checking Our Eyes',
   'Kindergarten Social Studies strand: an optometrist is a doctor who checks our eyes to make sure we can see clearly and helps us get glasses if we need them.',
   [('What does an optometrist check?', ['our eyes', 'how well we see']),
    ('What might an optometrist give us if we need help seeing?', ['glasses', 'a pair of glasses']),
    ('Why is it helpful to visit an optometrist?', ['to make sure our eyes are healthy', 'to check if we see clearly'])],
   [('What does an optometrist mainly check?', ['Our eyes and vision', 'Our teeth', 'Our hearing', 'Our height'], 0),
    ('What might an optometrist give a person who has trouble seeing clearly?', ['Glasses', 'A cast', 'A bandage', 'A toothbrush'], 0),
    ('Why is it important to have our eyes checked?', ['To make sure we can see clearly and our eyes are healthy', 'Eyes never need to be checked', 'It has no benefit at all', 'Only adults have eyes'], 0),
    ('Where might you visit to see an optometrist?', ['An eye clinic or office', 'A bakery', 'A fire station', 'A grocery store'], 0),
    ('An optometrist helps people by testing how well they can ___.', ['See', 'Hear', 'Taste', 'Smell'], 0)]),
]),
day(153, [
L('Suffixes: Adding -less to Change Meaning',
  'Kindergarten Language strand: adding the suffix -less to the end of a word can mean without something, such as changing care into careless, meaning without care.',
  [('What does careless mean?', ['without care', 'not being careful']),
   ('What does the suffix -less usually mean?', ['without', 'without something']),
   ('Give an example of a word with the suffix -less.', ['careless', 'colourless'])],
  [('What does the word careless mean?', ['Without care, not careful', 'Full of care', 'Very happy', 'Very sleepy'], 0),
   ('What does the suffix -less usually add to the meaning of a word?', ['Without something', 'Full of something', 'A number', 'A colour'], 0),
   ('Which word means without a home?', ['Homeful', 'Homeless', 'Homing', 'Unhome'], 1),
   ('Adding -less to the word hope makes the word ___.', ['Hopeless, meaning without hope', 'Hopeful', 'Hoping only', 'Rehope'], 0),
   ('A suffix meaning without something is the opposite of a suffix meaning ___.', ['Full of something', 'A number', 'A place', 'A shape'], 0)]),
M('Ten Frames: Filling to Make Ten',
  'Kindergarten Math strand: a ten frame is a simple grid of ten boxes that helps students see how many more counters are needed to make a full group of ten.',
  [('How many boxes are in a ten frame?', ['10', 'ten']),
   ('If a ten frame has 7 counters, how many more are needed to fill it?', ['3', 'three']),
   ('Why is a ten frame a helpful tool?', ['it helps us see numbers up to ten', 'it shows how close a number is to ten'])],
  [('How many boxes make up a full ten frame?', ['5', '8', '10', '12'], 2),
   ('If a ten frame shows 6 filled boxes, how many empty boxes are left?', ['2', '3', '4', '5'], 2),
   ('If a ten frame shows 9 filled boxes, how many more are needed to make 10?', ['1', '2', '3', '4'], 0),
   ('A ten frame helps students see numbers in relation to ___.', ['Ten', 'One hundred', 'One thousand', 'Zero only'], 0),
   ('Which ten frame shows the number 10?', ['A ten frame with all boxes filled', 'A ten frame with no boxes filled', 'A ten frame with half the boxes filled', 'An empty page with no frame'], 0)]),
Sc('Ants: Small but Strong Workers',
   'Kindergarten Science strand: ants are small insects that live and work together in large groups, called colonies, and can carry things much heavier than their own body.',
   [('What do we call a large group of ants living together?', ['a colony', 'an ant colony']),
    ('How strong are ants compared to their size?', ['very strong', 'they can carry things heavier than themselves']),
    ('Do ants usually work alone or together?', ['together', 'they work together'])],
   [('What is a large group of ants living together called?', ['A colony', 'A herd', 'A flock', 'A pack'], 0),
    ('How does the strength of an ant compare to its own body size?', ['An ant can carry much more than its own weight', 'An ant cannot carry anything at all', 'An ant is the weakest insect', 'An ant can only carry things smaller than a crumb'], 0),
    ('Do ants usually work alone or as a group?', ['As a group', 'Always alone', 'Only in pairs of two', 'They never move'], 0),
    ('Which of these is true about ants?', ['They are insects that live in colonies', 'They are mammals that live alone', 'They cannot walk on the ground', 'They only live underwater'], 0),
    ('Ants working together to build a home shows they are good at ___.', ['Teamwork', 'Flying', 'Swimming', 'Singing'], 0)]),
SS('Our Chefs and Cooks: Making the Food We Eat',
   'Kindergarten Social Studies strand: chefs and cooks prepare and cook food for people to eat at restaurants, cafeterias, and other places in our community.',
   [('What do chefs and cooks make?', ['food', 'meals for people to eat']),
    ('Name one place a chef might work.', ['a restaurant', 'a cafeteria']),
    ('Why is a chefs job important?', ['they make food for people to eat', 'they help feed our community'])],
   [('What is the main job of a chef or cook?', ['Preparing and cooking food', 'Teaching school', 'Driving a bus', 'Fixing wires'], 0),
    ('Where might a chef work?', ['A restaurant or cafeteria', 'A library only', 'A fire station', 'An airplane cockpit'], 0),
    ('Why is the work of chefs and cooks important to a community?', ['They prepare food that people need to eat', 'Food never needs to be cooked', 'Cooking is not important', 'Only families can make food'], 0),
    ('Which of these might a chef use to prepare food?', ['A pot and a stove', 'A stethoscope', 'A fire hose', 'A microscope'], 0),
    ('Chefs and cooks help make sure people in a community have ___.', ['Meals to eat', 'Clean water only', 'A place to sleep', 'Safe roads'], 0)]),
]),
day(154, [
L('Prefixes: Adding Pre- to Change Meaning',
  'Kindergarten Language strand: adding the prefix pre- to the start of a word can mean before, such as changing view into preview, meaning to see before.',
  [('What does preview mean?', ['to see before', 'look at something before']),
   ('What does the prefix pre- usually mean?', ['before', 'to come before']),
   ('Give an example of a word with the prefix pre-.', ['preview', 'preheat'])],
  [('What does the word preview mean?', ['To see something before it happens', 'To never see something', 'To see something after it happens', 'To hear something loudly'], 0),
   ('What does the prefix pre- usually add to a word?', ['The meaning of before', 'The meaning of again', 'A number', 'A colour'], 0),
   ('Which word means to heat something before cooking?', ['Postheat', 'Preheat', 'Unheat', 'Heating only'], 1),
   ('Adding pre- to the word school makes the word ___.', ['Preschool, meaning before school', 'Postschool', 'Schooling only', 'Unschool'], 0),
   ('A prefix is added to the ___ of a word.', ['End', 'Beginning', 'Middle', 'Nowhere'], 1)]),
M('Numbers Before and After: What Comes Next',
  'Kindergarten Math strand: students identify the number that comes right before or right after a given number, such as knowing that 8 comes right before 9 and 10 comes right after 9.',
  [('What number comes right after 9?', ['10', 'ten']),
   ('What number comes right before 9?', ['8', 'eight']),
   ('Why is it helpful to know what comes before and after a number?', ['it helps us count and order numbers', 'it helps with counting'])],
  [('What number comes right after 9?', ['8', '9', '10', '11'], 2),
   ('What number comes right before 15?', ['13', '14', '16', '17'], 1),
   ('What number comes right after 19?', ['18', '20', '21', '29'], 1),
   ('Knowing what comes before and after a number helps us with ___.', ['Counting and number order', 'Colours', 'Shapes', 'Letters'], 0),
   ('What number comes right before 1?', ['0', '2', '10', 'There is none'], 0)]),
Sc('Kangaroos: Animals with Pouches',
   'Kindergarten Science strand: a kangaroo is an animal from Australia that carries its baby, called a joey, in a special pouch on its belly.',
   [('What is a baby kangaroo called?', ['a joey', 'joey']),
    ('Where does a mother kangaroo carry her baby?', ['in her pouch', 'a pouch on her belly']),
    ('What country are kangaroos mostly found in?', ['Australia', 'in Australia'])],
   [('What is a baby kangaroo called?', ['A cub', 'A joey', 'A calf', 'A kit'], 1),
    ('Where does a mother kangaroo keep her baby?', ['In a pouch on her belly', 'On her back', 'In a nest', 'Under a rock'], 0),
    ('Where are kangaroos mostly found living in the wild?', ['Australia', 'Canada', 'The Arctic', 'The ocean'], 0),
    ('How do kangaroos usually move around?', ['By hopping on strong back legs', 'By flying', 'By swimming only', 'By crawling on their bellies'], 0),
    ('An animal that carries its baby in a pouch is called a ___.', ['Marsupial', 'Reptile', 'Amphibian', 'Insect'], 0)]),
SS('Saving and Spending: Making Choices with Money',
   'Kindergarten Social Studies strand: people make choices about money, deciding whether to spend it on something they want now or save it for something later.',
   [('What does it mean to save money?', ['keep it for later', 'not spend it right away']),
    ('What does it mean to spend money?', ['use it to buy something', 'trade it for something you want']),
    ('Why might someone choose to save money instead of spending it?', ['to buy something bigger later', 'for something they want in the future'])],
   [('What does it mean to save money?', ['Keep it instead of spending it right away', 'Give it away for free', 'Throw it away', 'Hide it forever with no plan'], 0),
    ('What does it mean to spend money?', ['Use it to buy something', 'Bury it in the ground', 'Never use it', 'Give it back automatically'], 0),
    ('Why might a person choose to save money?', ['To buy something bigger later', 'Money can never be saved', 'Saving has no purpose', 'To make it disappear'], 0),
    ('Which is an example of saving money?', ['Putting coins into a piggy bank', 'Spending every coin right away', 'Losing money on purpose', 'Giving all money away'], 0),
    ('Making choices about money helps people plan for ___.', ['The future', 'Nothing at all', 'Only today', 'Only their friends'], 0)]),
]),
day(155, [
L('Vowel Teams: oa and ea',
  'Kindergarten Language strand: the letters oa and ea can team up to make one vowel sound, as in boat and read.',
  [('What sound do the letters oa make in the word boat?', ['long o sound', 'the long o sound']),
   ('What sound do the letters ea make in the word read?', ['long e sound', 'the long e sound']),
   ('Give another word that has the oa vowel team.', ['coat', 'road'])],
  [('Which word has the oa vowel team?', ['Boat', 'Bat', 'Bit', 'But'], 0),
   ('Which word has the ea vowel team?', ['Read', 'Red', 'Rid', 'Rod'], 0),
   ('What sound do the letters oa usually make together?', ['A long o sound', 'A short a sound', 'A silent sound', 'A long i sound'], 0),
   ('Which of these words has the ea vowel team?', ['Team', 'Ten', 'Tin', 'Ton'], 0),
   ('When two vowels team up, they often make ___.', ['Two separate sounds', 'One vowel sound', 'No sound at all', 'A consonant sound'], 1)]),
M('Halving: Splitting a Group into Two Equal Parts',
  'Kindergarten Math strand: halving means splitting a group of objects into two equal parts, such as splitting 8 counters into two groups of 4.',
  [('If you halve 8 counters, how many are in each group?', ['4', 'four']),
   ('If you halve 10 counters, how many are in each group?', ['5', 'five']),
   ('Why must the two groups be equal when halving?', ['so each part is fair', 'both parts should be the same size'])],
  [('If you halve 8 objects, how many are in each equal group?', ['2', '3', '4', '5'], 2),
   ('If you halve 6 objects, how many are in each equal group?', ['2', '3', '4', '5'], 1),
   ('Halving a group means splitting it into ___ equal parts.', ['One', 'Two', 'Three', 'Four'], 1),
   ('If you halve 12 objects, how many are in each equal group?', ['4', '5', '6', '7'], 2),
   ('For halving to be fair, each of the two groups must be ___.', ['The same size', 'Different sizes', 'Empty', 'Twice as big'], 0)]),
Sc('Sharks: Fish of the Deep Ocean',
   'Kindergarten Science strand: sharks are a kind of fish with many sharp teeth, and they use their gills to breathe underwater like other fish.',
   [('What kind of animal is a shark?', ['a fish', 'a type of fish']),
    ('What do sharks have many of in their mouths?', ['sharp teeth', 'teeth']),
    ('What do sharks use to breathe underwater?', ['gills', 'their gills'])],
   [('What kind of animal is a shark?', ['A fish', 'A mammal', 'A reptile', 'An amphibian'], 0),
    ('What are sharks well known for having many of?', ['Sharp teeth', 'Feathers', 'Legs', 'Fur'], 0),
    ('How do sharks breathe underwater?', ['Using gills', 'Using lungs', 'Holding their breath', 'Using a nose only'], 0),
    ('Where do sharks live?', ['In the ocean', 'In trees', 'In the desert', 'Underground'], 0),
    ('Sharks help keep the ocean healthy by eating ___.', ['Weaker or sick fish', 'Only plants', 'Rocks', 'Nothing at all'], 0)]),
SS('Earth Day: Caring for Our Planet',
   'Kindergarten Social Studies strand: Earth Day is a special day when people around the world do things like pick up litter and plant trees to help take care of our planet.',
   [('What is Earth Day about?', ['taking care of our planet', 'helping the earth']),
    ('Name one thing people might do on Earth Day.', ['pick up litter', 'plant a tree']),
    ('Why is it important to take care of the earth?', ['so it stays healthy for everyone', 'to keep nature clean and safe'])],
   [('What is the main purpose of Earth Day?', ['To help take care of our planet', 'To celebrate a sports team', 'To eat special food only', 'To stay home from school'], 0),
    ('Which is something people might do to celebrate Earth Day?', ['Plant a tree or pick up litter', 'Litter more than usual', 'Cut down every tree', 'Waste as much water as possible'], 0),
    ('Why is taking care of the earth important?', ['So it stays healthy for people, animals, and plants', 'The earth does not need any care', 'Only one country needs to help', 'It has no effect on anyone'], 0),
    ('Earth Day reminds us to think about how we treat ___.', ['Our planet', 'Only our own house', 'Nothing at all', 'Only toys'], 0),
    ('Which of these actions helps the earth?', ['Recycling bottles and cans', 'Leaving trash on the ground', 'Wasting water', 'Cutting down trees for no reason'], 0)]),
]),
day(156, [
L('R-Controlled Vowels: er and ir',
  'Kindergarten Language strand: when the letter r follows a vowel, it changes the vowel sound, as in the er sound in fern and the ir sound in bird.',
  [('What sound do the letters er make in the word fern?', ['er sound', 'the er sound']),
   ('What sound do the letters ir make in the word bird?', ['er sound', 'sounds like er']),
   ('Give another word that has the ir sound.', ['girl', 'shirt'])],
  [('Which word has the er sound?', ['Fern', 'Fan', 'Fin', 'Fun'], 0),
   ('Which word has the ir sound?', ['Bird', 'Bad', 'Bed', 'Bud'], 0),
   ('What happens to a vowel sound when it is followed by the letter r?', ['The vowel sound changes', 'The vowel disappears completely', 'Nothing changes at all', 'The vowel becomes silent'], 0),
   ('Which of these words has an r-controlled vowel sound?', ['Girl', 'Cat', 'Dog', 'Sun'], 0),
   ('The er sound and the ir sound often sound ___ to each other.', ['Very similar', 'Completely different', 'Silent', 'Backwards'], 0)]),
M('Measurement: Comparing Temperature with a Thermometer',
  'Kindergarten Math strand: a thermometer is a tool that measures how hot or cold something is, and students compare readings to see which is warmer or cooler.',
  [('What tool measures how hot or cold something is?', ['a thermometer', 'thermometer']),
   ('If one reading is higher than another, which is warmer?', ['the higher reading', 'the one with the higher number']),
   ('Name one place you might use a thermometer.', ['outside', 'to check if you are sick'])],
  [('What tool is used to measure temperature?', ['A ruler', 'A thermometer', 'A scale', 'A clock'], 1),
   ('If one thermometer reading is higher than another, which is warmer?', ['The higher reading', 'The lower reading', 'They are always the same', 'Neither is warmer'], 0),
   ('Which of these would likely have a higher temperature reading?', ['A cup of hot soup', 'A bowl of ice', 'A snowbank', 'A freezer'], 0),
   ('A thermometer helps us compare how ___ different things are.', ['Hot or cold', 'Heavy or light', 'Long or short', 'Loud or quiet'], 0),
   ('On a very cold winter day, a thermometer reading would likely be ___.', ['Low', 'High', 'The same as summer', 'Impossible to read'], 0)]),
Sc('Our Stomach: Digesting the Food We Eat',
   'Kindergarten Science strand: our stomach is a body part that mixes and breaks down the food we eat so our body can use it for energy.',
   [('What does our stomach do to the food we eat?', ['mixes and breaks it down', 'digests it']),
    ('Why does our body need to digest food?', ['to get energy from it', 'so our body can use it']),
    ('Where is the stomach located in our body?', ['inside our belly', 'in our belly'])],
   [('What is the main job of our stomach?', ['Mixing and breaking down food we eat', 'Pumping blood', 'Helping us breathe', 'Helping us see'], 0),
    ('Why does our body need to digest food?', ['To get energy and nutrients from it', 'Digesting food has no purpose', 'To make food disappear with no use', 'To make us feel sleepy only'], 0),
    ('Where is the stomach located in the human body?', ['Inside the belly', 'In the head', 'In the foot', 'In the ear'], 0),
    ('After food leaves the stomach, where does it go next in our body?', ['Into the intestines', 'Back out of the mouth', 'Into the lungs', 'Into the brain'], 0),
    ('Taking care of what we eat helps our stomach and body stay ___.', ['Healthy', 'Weak', 'Confused', 'Cold'], 0)]),
SS('Canadian Currency: Symbols on Our Coins and Bills',
   'Kindergarten Social Studies strand: Canadian coins and bills have special pictures and symbols on them, like a loon on the dollar coin and a portrait on many bills.',
   [('What is another name for Canadian money?', ['currency', 'Canadian currency']),
    ('What animal appears on the Canadian dollar coin?', ['a loon', 'loon']),
    ('Why do coins and bills have pictures on them?', ['to show something important about Canada', 'special symbols and pictures'])],
   [('What word describes Canadian money like coins and bills?', ['Currency', 'Language', 'Anthem', 'Symbol only'], 0),
    ('What bird appears on the Canadian one dollar coin?', ['A loon', 'An eagle', 'A robin', 'A penguin'], 0),
    ('Why do Canadian coins and bills often have special pictures?', ['To show symbols important to Canada', 'Pictures are never used on money', 'To confuse people', 'Only for decoration with no meaning'], 0),
    ('Which of these is found on Canadian currency?', ['A portrait and national symbols', 'Random scribbles with no meaning', 'Pictures from other countries only', 'Nothing at all'], 0),
    ('Looking closely at coins and bills can teach us about ___.', ['Canadian symbols and history', 'Nothing important', 'Only numbers', 'Only colours'], 0)]),
]),
day(157, [
L('Story Genre: Fairy Tales and Fables',
  'Kindergarten Language strand: fairy tales are make-believe stories that often include magic, while fables are short stories with animal characters that teach a lesson.',
  [('What might a fairy tale include?', ['magic', 'make-believe magic']),
   ('What do fables usually teach?', ['a lesson', 'a moral or lesson']),
   ('What kind of characters are often found in fables?', ['animals', 'talking animals'])],
  [('What might a fairy tale often include?', ['Magic and make-believe events', 'Only true facts', 'Only real people from history', 'No characters at all'], 0),
   ('What do fables usually teach the reader?', ['A lesson or moral', 'Nothing at all', 'Only weather facts', 'Only math facts'], 0),
   ('What kind of characters are common in fables?', ['Talking animals', 'Only doctors', 'Only robots', 'Only weather'], 0),
   ('Which is an example of a fairy tale element?', ['A magic spell', 'A weather report', 'A recipe', 'A math equation'], 0),
   ('Knowing a storys genre helps readers understand ___.', ['What kind of story to expect', 'Nothing useful', 'Only the page count', 'Only the cover colour'], 0)]),
M('Data: Sorting and Counting a Collection',
  'Kindergarten Math strand: students sort a collection of objects into groups by a shared attribute, like colour or shape, and count how many are in each group.',
  [('Name one way you could sort a collection of buttons.', ['by colour', 'by shape']),
   ('If you sort buttons by colour, what do you do next?', ['count how many are in each group', 'count each group']),
   ('Why do we sort a collection before counting it?', ['it makes counting easier', 'to organize it first'])],
  [('Which of these is a way to sort a collection of objects?', ['By colour', 'By nothing at all', 'By randomly mixing them', 'By hiding them'], 0),
   ('After sorting a collection into groups, what should you do next?', ['Count how many are in each group', 'Throw the groups away', 'Mix them back together with no count', 'Ignore the groups'], 0),
   ('If you sort a bag of blocks by shape, how many groups might you end up with?', ['One group for each different shape', 'Only one group no matter what', 'Zero groups', 'A random unrelated number'], 0),
   ('Sorting a collection before counting helps make counting ___.', ['Easier and more organized', 'Impossible', 'Slower for no reason', 'Less accurate'], 0),
   ('Which attribute could you use to sort a pile of toy cars?', ['Colour', 'Sound they make when silent', 'Their smell', 'Their taste'], 0)]),
Sc('Desert Habitats: Surviving the Heat',
   'Kindergarten Science strand: a desert is a very dry habitat that gets little rain, and the plants and animals that live there have special ways to survive the heat and lack of water.',
   [('What is a desert habitat like?', ['dry', 'very dry with little rain']),
    ('Name one animal that lives in a desert.', ['a camel', 'a lizard']),
    ('How do desert animals survive without much water?', ['they have special adaptations', 'they can go a long time without water'])],
   [('What kind of habitat is a desert?', ['Very dry with little rain', 'Very wet with lots of rain', 'Covered in ice and snow', 'Underwater'], 0),
    ('Which of these animals is well suited to live in a desert?', ['A camel', 'A polar bear', 'A whale', 'A penguin'], 0),
    ('How do many desert plants survive with little water?', ['They store water inside themselves', 'They need water every hour', 'They cannot survive at all', 'They grow only underwater'], 0),
    ('Desert days can be very hot, while desert nights can be quite ___.', ['Cold', 'Wet', 'Snowy', 'The exact same temperature'], 0),
    ('Animals and plants that survive well in a habitat like the desert are said to be well ___.', ['Adapted', 'Lost', 'Confused', 'Unprepared'], 0)]),
SS('Our Local Council: Making Decisions for Our City',
   'Kindergarten Social Studies strand: a local council is a group of elected people who work together to make decisions and rules for a city or town.',
   [('What is a local council?', ['a group that makes decisions for a city', 'a group of elected leaders']),
    ('What do council members do together?', ['make decisions and rules', 'work together to decide things']),
    ('Why does a city need a council?', ['to help make good decisions for everyone', 'to lead and organize the city'])],
   [('What is a local council?', ['A group of elected people who make decisions for a city', 'A single person who owns the city', 'A type of building only', 'A sports team'], 0),
    ('What do council members work together to do?', ['Make decisions and rules for the community', 'Play games all day', 'Avoid helping the community', 'Ignore what people need'], 0),
    ('Why might a city need a council instead of just one leader deciding everything?', ['Many people working together can make better decisions', 'One person always knows best with no help', 'Councils have no purpose', 'Cities do not need any leaders'], 0),
    ('Where might a local council hold its meetings?', ['At the town hall', 'On the moon', 'In outer space', 'Nowhere at all'], 0),
    ('A local council helps make sure a city has fair ___.', ['Decisions and rules', 'Weather', 'Food only', 'Games'], 0)]),
]),
day(158, [
L('Main Idea: What Is the Story Mostly About',
  'Kindergarten Language strand: the main idea of a story is what the story is mostly about, even though the story might include many small details.',
  [('What does the main idea of a story tell us?', ['what the story is mostly about', 'the big idea of the story']),
   ('Why is finding the main idea helpful?', ['it helps us understand the story', 'summarize what happened']),
   ('Give an example of a main idea for a story about a dog finding a bone.', ['a dog finds a bone', 'a dog looking for a bone'])],
  [('What does the main idea of a story tell readers?', ['What the story is mostly about', 'The exact number of pages', 'The colour of the cover', 'The name of the author only'], 0),
   ('Why is it useful to find the main idea of a story?', ['It helps readers understand and summarize the story', 'It has no use for readers', 'It tells us nothing important', 'It only matters for pictures'], 0),
   ('Which best shows understanding of a storys main idea?', ['Being able to explain what the story is mostly about', 'Counting the number of words', 'Naming the printer of the book', 'Guessing the cover colour'], 0),
   ('A story can have many small details but usually only one ___.', ['Main idea', 'Cover', 'Title page', 'Price'], 0),
   ('If a story is mostly about a girl planting a garden, the main idea is ___.', ['A girl plants a garden', 'The colour of the sky', 'The name of the printer', 'The page numbers'], 0)]),
M('Number Patterns: Counting by Odd Numbers',
  'Kindergarten Math strand: odd numbers like 1, 3, 5, 7, and 9 follow a pattern where each number is two more than the last, and cannot be split into two equal groups.',
  [('Name the first three odd numbers.', ['1, 3, 5', 'one three five']),
   ('What number comes after 5 when counting by odd numbers?', ['7', 'seven']),
   ('Can an odd number be split into two equal groups?', ['no', 'no it cannot'])],
  [('Which set of numbers shows counting by odd numbers?', ['1, 3, 5, 7', '2, 4, 6, 8', '1, 2, 3, 4', '5, 10, 15, 20'], 0),
   ('What number comes next: 3, 5, 7, ___?', ['8', '9', '10', '11'], 1),
   ('Which of these numbers is odd?', ['4', '6', '7', '8'], 2),
   ('An odd number of objects cannot be split into ___ equal groups.', ['Two', 'Three', 'One', 'Four'], 0),
   ('When counting by odd numbers, each number is how much more than the last?', ['1', '2', '3', '5'], 1)]),
Sc('Hibernation: Sleeping Through Winter',
   'Kindergarten Science strand: some animals, like bears, go into a deep sleep called hibernation during winter to save energy when food is hard to find.',
   [('What is hibernation?', ['a deep winter sleep', 'a long sleep animals take in winter']),
    ('Name an animal that hibernates.', ['a bear', 'bears']),
    ('Why do some animals hibernate in winter?', ['to save energy', 'because food is hard to find'])],
   [('What is hibernation?', ['A deep sleep some animals take during winter', 'A dance animals do in summer', 'A type of food', 'A kind of nest'], 0),
    ('Which animal is well known for hibernating in winter?', ['A bear', 'A shark', 'A parrot', 'A frog that stays awake all year'], 0),
    ('Why might an animal hibernate during winter?', ['To save energy when food is hard to find', 'To grow taller quickly', 'To learn new sounds', 'To find more sunlight'], 0),
    ('During hibernation, an animal is usually ___.', ['In a very deep, long sleep', 'Wide awake and very active', 'Swimming in the ocean', 'Flying south'], 0),
    ('Hibernation mostly happens during which season?', ['Winter', 'Summer', 'Spring only', 'It happens every season equally'], 0)]),
SS('Our Ferry Workers: Traveling Across the Water',
   'Kindergarten Social Studies strand: ferry workers operate boats called ferries that carry people, cars, and goods safely across rivers, lakes, or the ocean.',
   [('What does a ferry carry across the water?', ['people and cars', 'people, cars, and goods']),
    ('What is a ferry?', ['a boat that carries people and vehicles', 'a type of boat']),
    ('Why are ferry workers important?', ['they help people travel safely', 'keep everyone safe on the water'])],
   [('What is a ferry?', ['A boat that carries people and vehicles across water', 'A type of airplane', 'A kind of car', 'A bicycle'], 0),
    ('What is the main job of a ferry worker?', ['Operating the ferry and keeping passengers safe', 'Teaching school', 'Delivering mail on foot', 'Growing food'], 0),
    ('Where might a ferry travel across?', ['A river, lake, or the ocean', 'A desert', 'A mountain', 'A forest with no water'], 0),
    ('Why might someone choose to take a ferry instead of driving around a large body of water?', ['It can be a faster and easier way to cross', 'Ferries never carry people', 'Ferries only carry animals', 'It is against the rules'], 0),
    ('Ferry workers help keep passengers ___ during the trip.', ['Safe', 'Confused', 'Unaware', 'In danger'], 0)]),
]),
day(159, [
L('Alliteration: Words That Start with the Same Sound',
  'Kindergarten Language strand: alliteration is when several words in a row start with the same beginning sound, such as in silly snakes slither slowly.',
  [('What is alliteration?', ['words that start with the same sound', 'repeating a beginning sound']),
   ('Give an example of an alliteration sentence.', ['silly snakes slither slowly', 'big brown bears bounce']),
   ('What beginning sound is repeated in Peter Piper picked?', ['the p sound', 'p'])],
  [('What is alliteration?', ['Several words in a row starting with the same sound', 'Words that rhyme at the end', 'A story with no characters', 'A silent letter'], 0),
   ('Which sentence is an example of alliteration?', ['Big brown bears bounce', 'The cat sat on a mat', 'I like to read books', 'The sun is bright today'], 0),
   ('What beginning sound is repeated in silly snakes slither?', ['The s sound', 'The b sound', 'The t sound', 'The m sound'], 0),
   ('Authors sometimes use alliteration to make writing sound more ___.', ['Fun and playful', 'Boring', 'Confusing', 'Silent'], 0),
   ('Which pair of words shares the same beginning sound?', ['Happy and hopeful', 'Cat and dog', 'Big and small', 'Sun and moon'], 0)]),
M('Time: Reading a Clock to Five-Minute Intervals',
  'Kindergarten Math strand: students learn to read a clock to the nearest five minutes, counting by fives around the clock face starting from the twelve.',
  [('If the minute hand points to the 1, how many minutes past the hour is it?', ['5 minutes', 'five minutes']),
   ('If the minute hand points to the 2, how many minutes past the hour is it?', ['10 minutes', 'ten minutes']),
   ('Why do we count by fives when reading the minute hand?', ['each number stands for five minutes', 'it matches the five minute marks'])],
  [('If the minute hand points to the 3, how many minutes past the hour is it?', ['5 minutes', '10 minutes', '15 minutes', '20 minutes'], 2),
   ('If the minute hand points to the 6, how many minutes past the hour is it?', ['20 minutes', '25 minutes', '30 minutes', '35 minutes'], 2),
   ('When reading the minute hand on a clock, each number represents ___ minutes.', ['1', '2', '5', '10'], 2),
   ('If the minute hand points to the 9, how many minutes past the hour is it?', ['35 minutes', '40 minutes', '45 minutes', '50 minutes'], 2),
   ('Counting by fives around a clock face helps us read the ___.', ['Minutes', 'Seconds only', 'Day of the week', 'Month'], 0)]),
Sc('Meteors: Shooting Stars in the Sky',
   'Kindergarten Science strand: a meteor, sometimes called a shooting star, is a small piece of space rock that burns up in a bright streak as it enters our atmosphere.',
   [('What is another name for a meteor?', ['a shooting star', 'shooting star']),
    ('What happens to a meteor as it enters our atmosphere?', ['it burns up', 'it burns and makes a bright streak']),
    ('When are meteors easiest to see?', ['at night', 'on a clear night'])],
   [('What is another common name for a meteor?', ['A shooting star', 'A moon rock', 'A cloud', 'A rainbow'], 0),
    ('What happens to a meteor as it enters our atmosphere?', ['It burns up in a bright streak', 'It grows much larger', 'It turns into water', 'It stays completely cold'], 0),
    ('When is the best time to try to see a meteor?', ['On a clear night', 'During a rainstorm', 'At noon on a sunny day', 'Only in a classroom'], 0),
    ('A meteor is best described as a small piece of ___.', ['Space rock', 'Ocean water', 'Cotton candy', 'Paper'], 0),
    ('Meteors travel through the sky very ___.', ['Quickly', 'Slowly', 'Never moving', 'Only sideways'], 0)]),
SS('Our Pilots: Flying Us to New Places',
   'Kindergarten Social Studies strand: pilots are trained to safely fly airplanes, taking passengers and goods to cities and countries around the world.',
   [('What does a pilot do?', ['flies an airplane', 'flies planes safely']),
    ('What might a pilot carry on an airplane?', ['passengers', 'passengers and goods']),
    ('Why do pilots need special training?', ['to fly safely', 'to keep everyone on the plane safe'])],
   [('What is the main job of a pilot?', ['Flying an airplane safely', 'Cooking meals', 'Teaching school', 'Fixing wires'], 0),
    ('What might a pilot carry on a flight?', ['Passengers and goods', 'Only empty seats', 'Nothing at all', 'Only animals'], 0),
    ('Why do pilots need a lot of special training?', ['To fly safely and handle the airplane well', 'Flying needs no training at all', 'Training is not important', 'Anyone can fly without learning'], 0),
    ('Where might a pilot fly passengers to?', ['Cities and countries around the world', 'Only next door', 'Nowhere at all', 'Only underwater'], 0),
    ('Pilots work together with other airport workers to keep flights ___.', ['Safe', 'Confusing', 'Unplanned', 'Dangerous'], 0)]),
]),
day(160, [
L('Language Review: Word Families, Prefixes and Suffixes, and Story Genres',
  'Kindergarten Language strand review: students revisit the -ut and -un word families, the suffix -less, the prefix pre-, vowel teams, r-controlled vowels, fairy tales and fables, main idea, and alliteration.',
  [('Name a word from the -ut or -un family.', ['nut', 'sun']),
   ('What does the prefix pre- usually mean?', ['before']),
   ('What is alliteration?', ['words that start with the same sound'])],
  [('Which word belongs to the -ut family?', ['Sun', 'Nut', 'Bed', 'Top'], 1),
   ('What does the word careless mean?', ['Without care, not careful', 'Full of care', 'Very happy', 'Very sleepy'], 0),
   ('Which word has the oa vowel team?', ['Boat', 'Bat', 'Bit', 'But'], 0),
   ('What might a fairy tale often include?', ['Magic and make-believe events', 'Only true facts', 'Only real people from history', 'No characters at all'], 0),
   ('What is alliteration?', ['Several words in a row starting with the same sound', 'Words that rhyme at the end', 'A story with no characters', 'A silent letter'], 0)]),
M('Math Review: Number Bonds, Skip Counting, and Time',
  'Kindergarten Math strand review: students revisit number bonds to 12, skip counting by 6s, ten frames, numbers before and after, halving, comparing temperature, sorting data, odd numbers, and reading a clock to five-minute intervals.',
  [('What is 10 plus 2?', ['12']),
   ('How many boxes make up a full ten frame?', ['10']),
   ('If the minute hand points to the 1, how many minutes past the hour is it?', ['5 minutes'])],
  [('Which pair of numbers makes 12?', ['5 and 5', '7 and 5', '4 and 4', '3 and 3'], 1),
   ('What comes next: 6, 12, 18, ___?', ['19', '20', '22', '24'], 3),
   ('If a ten frame shows 9 filled boxes, how many more are needed to make 10?', ['1', '2', '3', '4'], 0),
   ('Which set of numbers shows counting by odd numbers?', ['1, 3, 5, 7', '2, 4, 6, 8', '1, 2, 3, 4', '5, 10, 15, 20'], 0),
   ('If the minute hand points to the 6, how many minutes past the hour is it?', ['20 minutes', '25 minutes', '30 minutes', '35 minutes'], 2)]),
Sc('Science Review: Seasons, Life Cycles, and Habitats',
   'Kindergarten Science strand review: students revisit the summer season, the life cycle of a salmon, ants, kangaroos, sharks, our stomach, desert habitats, hibernation, and meteors.',
   [('What is summer weather usually like?', ['warm and sunny']),
    ('What is a baby kangaroo called?', ['a joey']),
    ('What is hibernation?', ['a deep winter sleep'])],
   [('What is summer weather usually like?', ['Cold and snowy', 'Warm and sunny', 'Very windy only', 'Always rainy'], 1),
    ('Where does a salmon life cycle begin?', ['As an egg in a river', 'As an egg in the desert', 'As an adult in the ocean', 'As an egg on a mountain'], 0),
    ('What is a large group of ants living together called?', ['A colony', 'A herd', 'A flock', 'A pack'], 0),
    ('What kind of animal is a shark?', ['A fish', 'A mammal', 'A reptile', 'An amphibian'], 0),
    ('What is hibernation?', ['A deep sleep some animals take during winter', 'A dance animals do in summer', 'A type of food', 'A kind of nest'], 0)]),
SS('Social Studies Review: New Helpers, Money, and Celebrations',
   'Kindergarten Social Studies strand review: students revisit paramedics, optometrists, chefs and cooks, saving and spending, Earth Day, Canadian currency, our local council, ferry workers, and pilots.',
   [('What is the main job of a paramedic?', ['giving medical help in an emergency']),
    ('What does it mean to save money?', ['keep it instead of spending it right away']),
    ('What is the main job of a pilot?', ['flying an airplane safely'])],
   [('What is the main job of a paramedic?', ['Giving medical help in an emergency', 'Teaching math', 'Cooking food', 'Building houses'], 0),
    ('What does an optometrist mainly check?', ['Our eyes and vision', 'Our teeth', 'Our hearing', 'Our height'], 0),
    ('What does it mean to save money?', ['Keep it instead of spending it right away', 'Give it away for free', 'Throw it away', 'Hide it forever with no plan'], 0),
    ('What is a local council?', ['A group of elected people who make decisions for a city', 'A single person who owns the city', 'A type of building only', 'A sports team'], 0),
    ('What is the main job of a pilot?', ['Flying an airplane safely', 'Cooking meals', 'Teaching school', 'Fixing wires'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_151_160)
    append_worksheet_days(0, g0_151_160)
