#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 161-170 -- fourteenth batch, extending Grade 0
past Day 160. Self-contained script (does NOT use gen_curriculum.py's
sub()/day()/append_to(), since those do not support a worksheet field)
modeled exactly on gen_grade0_days151_160.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-160 (dumped
and checked against data/grade0.json before writing): word families -ad,
-ag, -am; vowel teams igh and ow/ou; r-controlled vowel ur; the suffix
-ly; the prefix dis-; commas in a list for Language. Skip counting by 7s
and 8s, counting by even numbers (pairing with the existing odd-number
day), comparing durations, fourths, counting coins to a dollar,
estimating capacity, addition and subtraction stories to 20, and
comparing two-digit numbers with place value for Math. Life cycle of a
dragonfly, jellyfish, octopus, elephants, tornadoes, fingernails and
hair, evergreen and deciduous trees, earthquakes, and hummingbirds for
Science. Plumbers, hairdressers and barbers, judges and courts, Canadian
geography, trading goods, interpreters, the Royal Canadian Mint,
community festivals, and building inspectors for Social Studies. Day 170
is a review day across all four subjects, matching the end-of-batch
pattern used in every prior batch, with review titles textually distinct
from every earlier review day's title for each subject. No embedded
ASCII double-quote or straight apostrophe characters are used anywhere
in title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely, matching this project's convention (e.g. "Canadas" not
"Canada's"), since this text gets embedded directly into TypeScript
string literals.
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


def _rebalance_answer_positions(days, seed=20260813):
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


g0_161_170 = [
day(161, [
L('Word Families: -ad Words',
  'Kindergarten Language strand: the -ad word family shares the same ending sound, as in bad, dad, mad, and sad.',
  [('Name a word that rhymes with bad.', ['dad', 'mad', 'sad']),
   ('What ending sound do dad and sad share?', ['ad', 'the ad sound']),
   ('Is glad part of the -ad family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ad family?', ['Sun', 'Sad', 'Bed', 'Top'], 1),
   ('Which word rhymes with mad?', ['Sit', 'Bad', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -ad family?', ['Bad', 'Dad', 'Sad', 'Sun'], 3),
   ('Complete the rhyme: My cat is very ___ when it rains.', ['sad', 'sat', 'sit', 'set'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Skip Counting by 7s to 70',
  'Kindergarten Math strand: students skip count by 7s, saying 7, 14, 21, 28, and continuing on up to 70.',
  [('What number comes after 7, 14, 21?', ['28', 'twenty eight']),
   ('Skip count by 7s from 7 to 35.', ['7,14,21,28,35', '7 14 21 28 35']),
   ('What number comes right before 70 when skip counting by 7s?', ['63', 'sixty three'])],
  [('What comes next: 7, 14, 21, ___?', ['22', '27', '28', '29'], 2),
   ('What comes next: 28, 35, 42, ___?', ['43', '45', '48', '49'], 3),
   ('When skip counting by 7s, what number comes after 49?', ['50', '54', '56', '58'], 2),
   ('Skip counting by 7s means we add ___ each time.', ['5', '6', '7', '8'], 2),
   ('Which list correctly skip counts by 7s?', ['7, 14, 21, 28', '7, 10, 14, 18', '7, 14, 20, 28', '7, 12, 17, 28'], 0)]),
Sc('Life Cycle of a Dragonfly',
   'Kindergarten Science strand: a dragonfly begins life as an egg laid in water, grows underwater as a nymph, and later becomes a flying adult with two pairs of wings.',
   [('Where does a dragonfly begin its life?', ['as an egg in water', 'in water']),
    ('What is a young dragonfly called before it can fly?', ['a nymph', 'nymph']),
    ('How many pairs of wings does an adult dragonfly have?', ['two pairs', 'two'])],
   [('Where does a dragonfly life cycle begin?', ['As an egg in water', 'As an egg in the desert', 'As an adult in the sky', 'As an egg in a tree'], 0),
    ('What is a young dragonfly called before it grows wings?', ['A nymph', 'A caterpillar', 'A tadpole', 'A cub'], 0),
    ('Where does a young dragonfly nymph live?', ['Underwater', 'In a tree', 'In the sand', 'In the sky'], 0),
    ('How many pairs of wings does an adult dragonfly have?', ['One pair', 'Two pairs', 'Three pairs', 'No wings'], 1),
    ('A dragonfly changing from a nymph into a flying adult is an example of a ___.', ['Life cycle', 'Food chain', 'Habitat', 'Season'], 0)]),
SS('Our Plumbers: Fixing Pipes and Water Leaks',
   'Kindergarten Social Studies strand: plumbers are trained workers who fix pipes, taps, and water leaks so that clean water can flow safely into our homes.',
   [('What do plumbers fix?', ['pipes and water leaks', 'pipes']),
    ('Why is a plumbers job important?', ['they help keep our water clean and flowing', 'so water works safely in our homes']),
    ('Name one tool a plumber might use.', ['a wrench', 'wrench'])],
   [('What is the main job of a plumber?', ['Fixing pipes and water leaks', 'Teaching school', 'Flying airplanes', 'Growing food'], 0),
    ('Why do homes need plumbers?', ['To keep water flowing safely through pipes', 'Plumbers are not needed', 'To cook food', 'To deliver mail'], 0),
    ('Which tool might a plumber use to fix a pipe?', ['A wrench', 'A paintbrush', 'A stethoscope', 'A fishing rod'], 0),
    ('What might happen if a leaking pipe is not fixed?', ['Water could leak and cause damage', 'Nothing would happen at all', 'The house would get warmer', 'The pipe would fix itself'], 0),
    ('Plumbers help make sure our homes have clean ___.', ['Water', 'Air only', 'Food', 'Light only'], 0)]),
]),
day(162, [
L('Word Families: -ag Words',
  'Kindergarten Language strand: the -ag word family shares the same ending sound, as in bag, tag, rag, and wag.',
  [('Name a word that rhymes with bag.', ['tag', 'rag', 'wag']),
   ('What ending sound do tag and rag share?', ['ag', 'the ag sound']),
   ('Is flag part of the -ag family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ag family?', ['Sun', 'Tag', 'Bed', 'Top'], 1),
   ('Which word rhymes with rag?', ['Sit', 'Bag', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -ag family?', ['Bag', 'Tag', 'Rag', 'Run'], 3),
   ('Complete the rhyme: On Canada Day we wave a red and white ___.', ['flag', 'flat', 'flap', 'flab'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Skip Counting by 8s to 80',
  'Kindergarten Math strand: students skip count by 8s, saying 8, 16, 24, 32, and continuing on up to 80.',
  [('What number comes after 8, 16, 24?', ['32', 'thirty two']),
   ('Skip count by 8s from 8 to 40.', ['8,16,24,32,40', '8 16 24 32 40']),
   ('What number comes right before 80 when skip counting by 8s?', ['72', 'seventy two'])],
  [('What comes next: 8, 16, 24, ___?', ['25', '30', '32', '34'], 2),
   ('What comes next: 32, 40, 48, ___?', ['49', '52', '56', '58'], 2),
   ('When skip counting by 8s, what number comes after 56?', ['57', '60', '64', '66'], 2),
   ('Skip counting by 8s means we add ___ each time.', ['6', '7', '8', '9'], 2),
   ('Which list correctly skip counts by 8s?', ['8, 16, 24, 32', '8, 10, 18, 24', '8, 16, 20, 32', '8, 14, 22, 32'], 0)]),
Sc('Jellyfish: Ocean Animals Without Bones',
   'Kindergarten Science strand: a jellyfish is a soft ocean animal with no bones and no brain, that uses its tentacles to catch food and can sting to protect itself.',
   [('Does a jellyfish have bones?', ['no', 'no it does not']),
    ('What does a jellyfish use to catch food?', ['its tentacles', 'tentacles']),
    ('What can a jellyfish do to protect itself?', ['sting', 'it can sting'])],
   [('Does a jellyfish have bones inside its body?', ['Yes', 'No', 'Only in its head', 'Only in its tentacles'], 1),
    ('What does a jellyfish use to catch food?', ['Its tentacles', 'Its legs', 'Its wings', 'Its fins'], 0),
    ('How can a jellyfish protect itself?', ['By stinging', 'By running away fast', 'By flying', 'By barking'], 0),
    ('Where does a jellyfish live?', ['In the ocean', 'In a desert', 'In a tree', 'Underground'], 0),
    ('A jellyfish moves through water mostly by ___.', ['Floating and drifting with gentle pulses', 'Walking on legs', 'Flying', 'Digging'], 0)]),
SS('Our Hairdressers and Barbers: Cutting and Styling Hair',
   'Kindergarten Social Studies strand: hairdressers and barbers are workers who cut, wash, and style hair to help people look and feel their best.',
   [('What do hairdressers and barbers do?', ['cut and style hair', 'cut hair']),
    ('Name one tool a hairdresser might use.', ['scissors', 'a comb']),
    ('Why might someone visit a hairdresser or barber?', ['to get a haircut', 'to have their hair styled'])],
   [('What is the main job of a hairdresser or barber?', ['Cutting and styling hair', 'Fixing pipes', 'Flying airplanes', 'Cooking food'], 0),
    ('Which tool might a hairdresser use?', ['Scissors', 'A stethoscope', 'A wrench', 'A shovel'], 0),
    ('Why might a person visit a barber shop?', ['To get a haircut', 'To buy groceries', 'To mail a letter', 'To see a doctor'], 0),
    ('Which of these best describes the work of a hairdresser?', ['Helping people look and feel their best with their hair', 'Teaching math', 'Delivering mail', 'Building houses'], 0),
    ('Hairdressers and barbers work in a place often called a ___.', ['Salon or barber shop', 'Fire station', 'Library', 'Farm'], 0)]),
]),
day(163, [
L('Word Families: -am Words',
  'Kindergarten Language strand: the -am word family shares the same ending sound, as in ham, jam, ram, and yam.',
  [('Name a word that rhymes with ham.', ['jam', 'ram', 'yam']),
   ('What ending sound do jam and ram share?', ['am', 'the am sound']),
   ('Is clam part of the -am family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -am family?', ['Sun', 'Ham', 'Bed', 'Top'], 1),
   ('Which word rhymes with jam?', ['Sit', 'Ram', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -am family?', ['Ham', 'Jam', 'Ram', 'Run'], 3),
   ('Complete the rhyme: I like toast with butter and ___.', ['jam', 'jog', 'jug', 'jet'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Number Patterns: Counting by Even Numbers',
  'Kindergarten Math strand: even numbers like 2, 4, 6, 8, and 10 follow a pattern where each number is two more than the last, and can be split into two equal groups.',
  [('Name the first three even numbers.', ['2, 4, 6', 'two four six']),
   ('What number comes after 6 when counting by even numbers?', ['8', 'eight']),
   ('Can an even number be split into two equal groups?', ['yes', 'yes it can'])],
  [('Which set of numbers shows counting by even numbers?', ['2, 4, 6, 8', '1, 3, 5, 7', '1, 2, 3, 4', '5, 10, 15, 20'], 0),
   ('What number comes next: 4, 6, 8, ___?', ['9', '10', '11', '12'], 1),
   ('Which of these numbers is even?', ['3', '5', '6', '9'], 2),
   ('An even number of objects can be split into ___ equal groups.', ['Two', 'Three', 'One', 'Five'], 0),
   ('When counting by even numbers, each number is how much more than the last?', ['1', '2', '3', '5'], 1)]),
Sc('Octopus: Eight Arms in the Ocean',
   'Kindergarten Science strand: an octopus is a soft-bodied ocean animal with eight arms covered in suckers, and it can change colour to hide from other animals.',
   [('How many arms does an octopus have?', ['eight', '8']),
    ('What covers the arms of an octopus?', ['suckers', 'suckers']),
    ('What can an octopus do to hide from other animals?', ['change colour', 'it can change colour'])],
   [('How many arms does an octopus have?', ['Four', 'Six', 'Eight', 'Ten'], 2),
    ('What covers the arms of an octopus?', ['Suckers', 'Feathers', 'Scales', 'Fur'], 0),
    ('How does an octopus hide from other animals?', ['By changing colour', 'By flying away', 'By barking loudly', 'By growing wings'], 0),
    ('Where does an octopus live?', ['In the ocean', 'In a desert', 'In a tree', 'Underground'], 0),
    ('An octopus has a body that is mostly ___.', ['Soft, with no bones', 'Covered in a hard shell', 'Covered in fur', 'Covered in feathers'], 0)]),
SS('Our Judges and Courts: Making Things Fair',
   'Kindergarten Social Studies strand: judges work in courts and help make fair decisions when people disagree or when someone needs help understanding if a rule was followed.',
   [('Where does a judge work?', ['in a court', 'a courthouse']),
    ('What does a judge help make?', ['fair decisions', 'fair choices']),
    ('Why are judges and courts important in a community?', ['they help keep things fair', 'to help solve problems fairly'])],
   [('Where does a judge usually work?', ['In a court', 'In a kitchen', 'On a farm', 'In an airplane'], 0),
    ('What is the main job of a judge?', ['Helping make fair decisions', 'Cooking food', 'Flying planes', 'Fixing pipes'], 0),
    ('Why might people go to a court?', ['To help solve a disagreement fairly', 'To buy groceries', 'To get a haircut', 'To mail a letter'], 0),
    ('A courtroom helps a community by making sure decisions are ___.', ['Fair', 'Random', 'Unfair', 'Secret'], 0),
    ('Judges listen carefully before making a decision because it helps them be ___.', ['Fair and thoughtful', 'Fast and careless', 'Loud and rude', 'Silent forever'], 0)]),
]),
day(164, [
L('Vowel Teams: igh Words',
  'Kindergarten Language strand: the letters igh together make the long i sound, as in night, light, and high.',
  [('What sound do the letters igh make in the word night?', ['long i sound', 'the long i sound']),
   ('Give another word with the igh vowel team.', ['light', 'high']),
   ('Is bright a word with the igh vowel team?', ['yes', 'yes it is'])],
  [('Which word has the igh vowel team?', ['Night', 'Net', 'Nit', 'Not'], 0),
   ('What sound do the letters igh usually make together?', ['A long i sound', 'A short a sound', 'A silent sound', 'A long e sound'], 0),
   ('Which of these words has the igh vowel team?', ['Light', 'Lit', 'Let', 'Lot'], 0),
   ('Complete the rhyme: The stars twinkle in the sky at ___.', ['night', 'net', 'nut', 'not'], 0),
   ('When three letters team up to make one sound, it is called a ___.', ['Vowel team', 'Consonant blend', 'Suffix', 'Prefix'], 0)]),
M('Time: Comparing Durations - Which Takes Longer',
  'Kindergarten Math strand: students compare two activities to decide which one takes a longer amount of time, such as brushing your teeth compared to baking a cake.',
  [('Which usually takes longer, brushing your teeth or baking a cake?', ['baking a cake', 'baking a cake takes longer']),
   ('Which usually takes a shorter time, blinking your eyes or reading a book?', ['blinking your eyes', 'blinking is shorter']),
   ('Why is it useful to compare how long activities take?', ['it helps us plan our day', 'to know what to expect'])],
  [('Which activity usually takes longer?', ['Baking a cake', 'Clapping your hands once', 'Blinking your eyes', 'Sneezing'], 0),
   ('Which activity usually takes a shorter amount of time?', ['Snapping your fingers', 'Growing a garden', 'Building a house', 'Taking a long trip'], 0),
   ('Comparing how long two activities take helps us understand ___.', ['Duration', 'Colour', 'Weight', 'Shape'], 0),
   ('Which would likely take longer, washing one dish or washing a whole sink of dishes?', ['Washing a whole sink of dishes', 'Washing one dish', 'They take the same time', 'Neither takes any time'], 0),
   ('An activity that takes a very short time might be measured in ___.', ['Seconds', 'Months', 'Years', 'Decades'], 0)]),
Sc('Elephants: The Largest Land Animals',
   'Kindergarten Science strand: elephants are the largest animals that live on land, using their long trunks to eat, drink, and greet other elephants.',
   [('What do elephants use their trunk for?', ['eating and drinking', 'to eat and drink and greet other elephants']),
    ('Are elephants the largest land animals or the largest ocean animals?', ['largest land animals', 'land animals']),
    ('Name one thing an elephant might use its trunk to do.', ['drink water', 'pick up food'])],
   [('What are elephants known for being?', ['The largest land animals', 'The smallest land animals', 'The fastest ocean animals', 'The smallest insects'], 0),
    ('What body part do elephants use to eat, drink, and greet each other?', ['Their trunk', 'Their tail', 'Their ears', 'Their feet'], 0),
    ('Where do elephants live?', ['On land', 'Only in the ocean', 'Only underground', 'Only in trees'], 0),
    ('Elephants often live together in a group called a ___.', ['Herd', 'Flock', 'Pack', 'School'], 0),
    ('Large ears help elephants stay cool by ___.', ['Fanning away heat', 'Making them fly', 'Helping them swim', 'Making them invisible'], 0)]),
SS('Canadian Geography: Mountains, Prairies, and Coastlines',
   'Kindergarten Social Studies strand: Canada has many different kinds of land, including tall mountains, flat prairies, and long coastlines next to the ocean.',
   [('Name one kind of land found in Canada.', ['mountains', 'prairies']),
    ('What is a coastline?', ['land next to the ocean', 'where land meets the ocean']),
    ('Are prairies flat or mountainous?', ['flat', 'they are flat'])],
   [('Which of these is a kind of land found in Canada?', ['Mountains', 'Only deserts', 'Only islands', 'Only ice'], 0),
    ('What is a prairie?', ['A large area of flat land', 'A tall mountain', 'A deep ocean', 'A small pond'], 0),
    ('What is a coastline?', ['Land next to the ocean', 'The middle of a mountain', 'A type of building', 'A kind of animal'], 0),
    ('Canada has land that includes mountains, prairies, and ___.', ['Coastlines', 'Nothing else', 'Only sand', 'Only snow'], 0),
    ('Learning about different kinds of land helps us understand our ___.', ['Country geography', 'Favourite foods', 'Favourite games', 'School subjects only'], 0)]),
]),
day(165, [
L('Vowel Teams: ow and ou',
  'Kindergarten Language strand: the letters ow and ou can team up to make the same sound, as in cow and out.',
  [('What sound do the letters ow make in the word cow?', ['ow sound', 'the ow sound']),
   ('What sound do the letters ou make in the word out?', ['ow sound', 'sounds like ow']),
   ('Give another word that has the ow sound.', ['how', 'now'])],
  [('Which word has the ow vowel team?', ['Cow', 'Cot', 'Cat', 'Cup'], 0),
   ('Which word has the ou vowel team?', ['Out', 'Oat', 'Ot', 'Ol'], 0),
   ('What sound do the letters ow often make together?', ['The ow sound, like in cow', 'A silent sound', 'A long e sound', 'A long a sound'], 0),
   ('Which of these words has the ou vowel team?', ['Shout', 'Shot', 'Shut', 'Shirt'], 0),
   ('The ow and ou teams often make the ___ sound.', ['Same', 'Different', 'Silent', 'Opposite'], 0)]),
M('Fractions: Introducing Fourths',
  'Kindergarten Math strand: when a whole shape is cut into four equal parts, each part is called a fourth, or a quarter.',
  [('If a shape is cut into four equal parts, what is each part called?', ['a fourth', 'a quarter']),
   ('How many fourths make one whole?', ['4', 'four']),
   ('Do all fourths need to be equal in size?', ['yes', 'yes they do'])],
  [('If a shape is cut into four equal parts, what is each part called?', ['A fourth', 'A half', 'A third', 'A whole'], 0),
   ('How many fourths make one whole shape?', ['2', '3', '4', '5'], 2),
   ('For a shape to be cut into fourths, the parts must be ___.', ['Equal in size', 'Different sizes', 'Any shape at all', 'Only two parts'], 0),
   ('Which shows a shape divided into fourths?', ['A circle cut into four equal slices', 'A circle with no cuts', 'A circle cut into two pieces', 'A square cut into three pieces'], 0),
   ('A fourth is also sometimes called a ___.', ['Quarter', 'Half', 'Whole', 'Double'], 0)]),
Sc('Tornadoes: Powerful Spinning Storms',
   'Kindergarten Science strand: a tornado is a powerful, spinning column of air that can move quickly across the ground during a strong storm.',
   [('What does a tornado look like?', ['a spinning column of air', 'a spinning funnel']),
    ('When do tornadoes usually happen?', ['during a strong storm', 'during storms']),
    ('Why is it important to stay safe during a tornado?', ['tornadoes can be very dangerous', 'because they are powerful and fast'])],
   [('What is a tornado?', ['A powerful, spinning column of air', 'A gentle breeze', 'A type of cloud with no wind', 'A calm sunny day'], 0),
    ('When do tornadoes usually form?', ['During a strong storm', 'On a calm clear day', 'Only at night', 'Only in winter'], 0),
    ('Why should people go somewhere safe during a tornado?', ['Tornadoes can be very dangerous', 'Tornadoes never cause harm', 'Tornadoes are slow moving', 'Tornadoes only happen in the ocean'], 0),
    ('A tornado moving across the ground can pick up and move ___.', ['Objects and debris', 'Nothing at all', 'Only water', 'Only leaves'], 0),
    ('Tornadoes are studied by scientists so people can stay ___.', ['Safe', 'Confused', 'In danger', 'Unaware'], 0)]),
SS('Trading Goods: How Communities Share What They Make',
   'Kindergarten Social Studies strand: communities trade goods, giving things they make or grow to other communities in exchange for things they need.',
   [('What does it mean to trade goods?', ['giving something for something else you need', 'exchanging things']),
    ('Why might one community trade with another?', ['to get things they do not have', 'to share what they make']),
    ('Name one good a community might trade.', ['food', 'fruit'])],
   [('What does it mean to trade goods?', ['Exchanging things for other things you need', 'Throwing things away', 'Keeping everything forever', 'Hiding goods from others'], 0),
    ('Why might communities trade with each other?', ['To get things they do not have themselves', 'Trading has no purpose', 'To waste resources', 'To avoid helping anyone'], 0),
    ('Which is an example of trading goods?', ['A farmer trading vegetables for fruit from another town', 'Burying vegetables in the yard', 'Throwing away extra fruit', 'Never sharing anything'], 0),
    ('Trading goods helps communities get things they ___.', ['Need but cannot make themselves', 'Never need at all', 'Already have too much of', 'Refuse to use'], 0),
    ('Long ago and today, trading goods helps connect ___.', ['Different communities', 'Nothing at all', 'Only one family', 'Only one person'], 0)]),
]),
day(166, [
L('R-Controlled Vowels: ur Words',
  'Kindergarten Language strand: when the letter r follows the letter u, it makes the ur sound, as in fur, turn, and burn.',
  [('What sound do the letters ur make in the word fur?', ['ur sound', 'the ur sound']),
   ('Give another word that has the ur sound.', ['turn', 'burn']),
   ('Does the ur sound in turn sound similar to the er sound in fern?', ['yes', 'yes it does'])],
  [('Which word has the ur sound?', ['Fur', 'Fan', 'Fin', 'Fun'], 0),
   ('Which of these words has an r-controlled ur sound?', ['Turn', 'Ten', 'Tan', 'Ton'], 0),
   ('The ur sound often sounds similar to which other r-controlled sound?', ['The er sound', 'A short a sound', 'A silent sound', 'A long o sound'], 0),
   ('Complete the rhyme: A cat has soft ___.', ['fur', 'fan', 'fun', 'fin'], 0),
   ('R-controlled vowels change how a vowel ___.', ['Sounds', 'Looks on the page', 'Is spelled only', 'Is coloured'], 0)]),
M('Money: Counting Coins to a Dollar',
  'Kindergarten Math strand: students add up the value of different coins, like quarters, dimes, and nickels, to see how many are needed to make one dollar, or 100 cents.',
  [('How many cents make one dollar?', ['100', 'one hundred']),
   ('How many quarters make one dollar?', ['4', 'four']),
   ('If you have 75 cents, how many more cents do you need to make a dollar?', ['25', 'twenty five'])],
  [('How many cents make one dollar?', ['50', '75', '100', '200'], 2),
   ('How many quarters are needed to make one dollar?', ['2', '3', '4', '5'], 2),
   ('If you have 90 cents, how many more cents do you need to make a dollar?', ['5', '10', '15', '20'], 1),
   ('Which combination of coins could make one dollar?', ['Four quarters', 'Two dimes', 'One nickel', 'One penny'], 0),
   ('Counting coins to reach one dollar helps us practice ___.', ['Adding money amounts', 'Subtracting shapes', 'Telling time', 'Measuring length'], 0)]),
Sc('Our Fingernails and Hair: Growing Parts of Our Body',
   'Kindergarten Science strand: our fingernails and hair are parts of our body that keep growing throughout our lives and need regular care, like trimming and washing.',
   [('Name one body part that keeps growing throughout our lives.', ['fingernails', 'hair']),
    ('Why do we trim our fingernails?', ['so they do not get too long', 'to keep them neat']),
    ('What can we use to keep our hair clean?', ['shampoo', 'water and shampoo'])],
   [('Which of these body parts keeps growing throughout our lives?', ['Fingernails and hair', 'Our eyes', 'Our ears', 'Our teeth'], 0),
    ('Why is it important to trim our fingernails?', ['So they stay neat and do not get too long', 'Trimming is never needed', 'To make them fall out', 'To stop them from growing forever'], 0),
    ('What helps keep our hair clean and healthy?', ['Washing it with shampoo', 'Never washing it', 'Cutting it every day', 'Ignoring it completely'], 0),
    ('Fingernails help protect the tips of our ___.', ['Fingers', 'Toes only', 'Ears', 'Nose'], 0),
    ('Taking care of our hair and nails is part of staying ___.', ['Clean and healthy', 'Sick', 'Cold', 'Tired'], 0)]),
SS('Our Interpreters: Helping People Understand Each Other',
   'Kindergarten Social Studies strand: interpreters are workers who help people who speak different languages understand each other by translating what is being said.',
   [('What do interpreters help people do?', ['understand each other', 'communicate']),
    ('Why might an interpreter be needed?', ['when people speak different languages', 'to help translate words']),
    ('Name a place where an interpreter might help.', ['a hospital', 'a school'])],
   [('What is the main job of an interpreter?', ['Helping people who speak different languages understand each other', 'Fixing pipes', 'Flying planes', 'Cooking food'], 0),
    ('When might an interpreter be needed?', ['When people speak different languages', 'When everyone speaks the same language', 'Never', 'Only during a storm'], 0),
    ('Where might an interpreter help someone?', ['At a hospital or school', 'Underwater', 'In outer space', 'Nowhere at all'], 0),
    ('Interpreters help make communities more ___.', ['Welcoming and easy to understand', 'Confusing', 'Unfriendly', 'Silent'], 0),
    ('An interpreter changes spoken words from one language into ___.', ['Another language', 'A picture', 'A number', 'A colour'], 0)]),
]),
day(167, [
L('Suffixes: Adding -ly to Change Meaning',
  'Kindergarten Language strand: adding the suffix -ly to the end of a word can describe how something is done, such as changing quick into quickly, meaning done in a quick way.',
  [('What does quickly mean?', ['done in a quick way', 'fast']),
   ('What does the suffix -ly usually do to a word?', ['describes how something is done', 'changes it to describe an action']),
   ('Give an example of a word with the suffix -ly.', ['quickly', 'slowly'])],
  [('What does the word quickly mean?', ['Done in a fast way', 'Done very slowly', 'Not moving at all', 'Done loudly only'], 0),
   ('What does the suffix -ly usually add to a word?', ['A description of how something is done', 'A number', 'A colour', 'A place'], 0),
   ('Which word means done in a slow way?', ['Slowly', 'Slowest', 'Slower', 'Slow only'], 0),
   ('Adding -ly to the word soft makes the word ___.', ['Softly, meaning done in a soft way', 'Softest', 'Softness only', 'Unsoft'], 0),
   ('A suffix that tells us how something is done is often added to a describing word to form an ___.', ['Adverb', 'Noun', 'Prefix', 'Number'], 0)]),
M('Estimating Capacity: About How Much Does It Hold?',
  'Kindergarten Math strand: students estimate about how much a container can hold before checking by filling it, comparing containers like a cup, a bowl, and a bucket.',
  [('Which usually holds more, a cup or a bucket?', ['a bucket', 'bucket']),
   ('What does it mean to estimate capacity?', ['to guess about how much something holds', 'make a careful guess before checking']),
   ('Why do we check our estimate after guessing?', ['to see how close our guess was', 'to compare our guess to the real amount'])],
  [('Which of these likely holds more?', ['A bucket', 'A teaspoon', 'A small cup', 'A thimble'], 0),
   ('What does it mean to estimate the capacity of a container?', ['To make a careful guess about how much it holds', 'To measure its exact weight', 'To count its sides', 'To paint it a colour'], 0),
   ('Why might we check our estimate after guessing a containers capacity?', ['To see how close our guess was to the real amount', 'Checking is never useful', 'To make the container disappear', 'To change the container shape'], 0),
   ('Which activity helps us estimate capacity?', ['Guessing then pouring water to check', 'Measuring with a ruler', 'Counting sides of a shape', 'Weighing on a scale'], 0),
   ('A large bucket most likely holds ___ water than a small cup.', ['More', 'Less', 'The same amount of', 'No'], 0)]),
Sc('Types of Trees: Evergreen and Deciduous',
   'Kindergarten Science strand: evergreen trees keep their green needles all year, while deciduous trees lose their leaves in autumn and grow new ones in spring.',
   [('Does an evergreen tree lose its needles in winter?', ['no', 'no it does not']),
    ('What happens to the leaves of a deciduous tree in autumn?', ['they fall off', 'they fall to the ground']),
    ('Name one example of an evergreen tree.', ['a pine tree', 'a spruce tree'])],
   [('What is true about an evergreen tree?', ['It keeps its green needles all year', 'It loses all its leaves every autumn', 'It never has any leaves or needles', 'It only grows in the desert'], 0),
    ('What happens to a deciduous tree in autumn?', ['Its leaves change colour and fall off', 'Its leaves stay green forever', 'It grows underwater', 'It disappears completely'], 0),
    ('Which of these is an example of an evergreen tree?', ['A pine tree', 'An oak tree that loses its leaves', 'A maple tree that loses its leaves', 'A tree with no needles or leaves'], 0),
    ('Deciduous trees grow new leaves again in which season?', ['Spring', 'Only winter', 'Never again', 'Only at night'], 0),
    ('Comparing evergreen and deciduous trees helps us understand how trees can be ___.', ['Different from each other', 'Exactly the same', 'Not really trees', 'Always the same colour'], 0)]),
SS('The Royal Canadian Mint: Where Our Coins Are Made',
   'Kindergarten Social Studies strand: the Royal Canadian Mint is a special place where Canadian coins are designed and made before they are used in stores across the country.',
   [('What is the Royal Canadian Mint?', ['a place where coins are made', 'where Canadian coins are made']),
    ('What happens to coins after they are made at the mint?', ['they are used in stores', 'sent out to be used as money']),
    ('Why is the mint an important place in Canada?', ['it makes the coins we use every day', 'it creates our money'])],
   [('What is the Royal Canadian Mint?', ['A place where Canadian coins are made', 'A type of coin', 'A grocery store', 'A school'], 0),
    ('What happens at the Royal Canadian Mint?', ['Coins are designed and made', 'Coins are destroyed', 'Coins are grown like plants', 'Coins are painted only'], 0),
    ('After coins are made, where do they usually go?', ['Out into stores and banks to be used as money', 'Back into the ground', 'Nowhere, they stay in one place forever', 'Into outer space'], 0),
    ('Why is the mint an important part of Canada?', ['It creates the coins Canadians use every day', 'It has no importance', 'It only makes toys', 'It only makes paper'], 0),
    ('The word mint, when talking about money, refers to a place that ___.', ['Makes coins', 'Sells food', 'Teaches school', 'Fixes cars'], 0)]),
]),
day(168, [
L('Prefixes: Adding Dis- to Change Meaning',
  'Kindergarten Language strand: adding the prefix dis- to the start of a word can mean not or the opposite of, such as changing like into dislike, meaning to not like something.',
  [('What does dislike mean?', ['to not like something', 'not liking something']),
   ('What does the prefix dis- usually mean?', ['not', 'the opposite of']),
   ('Give an example of a word with the prefix dis-.', ['dislike', 'disagree'])],
  [('What does the word dislike mean?', ['To not like something', 'To really enjoy something', 'To agree with something', 'To forget something'], 0),
   ('What does the prefix dis- usually add to a word?', ['The meaning of not or the opposite', 'The meaning of again', 'A number', 'A colour'], 0),
   ('Which word means to not agree?', ['Disagree', 'Agreeable', 'Agreement', 'Reagree'], 0),
   ('Adding dis- to the word appear makes the word ___.', ['Disappear, meaning to go away', 'Reappear', 'Appearing only', 'Unappear'], 0),
   ('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'Middle', 'Nowhere'], 0)]),
M('Addition and Subtraction Stories to 20',
  'Kindergarten Math strand: students solve addition and subtraction word stories using numbers up to 20, such as combining two groups or taking objects away.',
  [('If you have 12 apples and get 5 more, how many apples do you have?', ['17', 'seventeen']),
   ('If you have 18 stickers and give away 6, how many are left?', ['12', 'twelve']),
   ('What operation do we use when we combine two groups together?', ['addition', 'adding'])],
  [('If you have 12 apples and get 5 more, how many apples do you have in total?', ['15', '16', '17', '18'], 2),
   ('If you have 18 stickers and give away 6, how many stickers are left?', ['10', '11', '12', '13'], 2),
   ('Which operation do we use to find a total when combining two groups?', ['Addition', 'Subtraction', 'Multiplication', 'Division'], 0),
   ('If a story says objects are being taken away, which operation should you use?', ['Addition', 'Subtraction', 'Sorting', 'Estimating'], 1),
   ('If you have 9 crayons and find 8 more, how many crayons do you have?', ['15', '16', '17', '18'], 2)]),
Sc('Earthquakes: When the Ground Shakes',
   'Kindergarten Science strand: an earthquake happens when the ground shakes suddenly because of movement deep under the surface of the earth.',
   [('What happens to the ground during an earthquake?', ['it shakes', 'the ground shakes']),
    ('Where does the movement that causes an earthquake happen?', ['deep under the ground', 'under the surface of the earth']),
    ('Why is it important to know what to do during an earthquake?', ['to stay safe', 'so we know how to stay safe'])],
   [('What happens to the ground during an earthquake?', ['It shakes suddenly', 'It turns to water', 'It disappears', 'It grows taller'], 0),
    ('Where does the movement that causes an earthquake happen?', ['Deep under the surface of the earth', 'In the clouds', 'In the ocean only', 'In outer space'], 0),
    ('Why do schools sometimes practice earthquake drills?', ['To help people know how to stay safe', 'Drills are never useful', 'To make people scared', 'To waste time'], 0),
    ('During an earthquake, it is often recommended to ___.', ['Drop, cover, and hold on', 'Run outside immediately', 'Stand near a window', 'Ignore it completely'], 0),
    ('An earthquake is an example of a natural event that comes from inside our ___.', ['Planet', 'Refrigerator', 'Classroom', 'Backpack'], 0)]),
SS('Community Events: Fairs and Festivals',
   'Kindergarten Social Studies strand: communities often hold fairs and festivals where neighbours gather to enjoy music, food, games, and activities together.',
   [('What is a community fair or festival?', ['a gathering for neighbours to enjoy together', 'an event where people gather']),
    ('Name one thing you might find at a community festival.', ['music', 'food']),
    ('Why are community festivals a good way to bring people together?', ['everyone can enjoy activities together', 'they help neighbours get to know each other'])],
   [('What is a community festival?', ['A gathering where neighbours enjoy activities together', 'A type of school test', 'A private event for one family', 'A kind of weather'], 0),
    ('Which of these might you find at a community fair?', ['Music and games', 'A courtroom', 'A hospital bed', 'A car repair shop'], 0),
    ('Why are community festivals helpful for neighbourhoods?', ['They help bring neighbours together', 'They keep neighbours apart', 'They have no purpose', 'They only help one person'], 0),
    ('Community festivals often celebrate things like ___.', ['Local traditions and culture', 'Nothing important', 'Only sports scores', 'Only weather reports'], 0),
    ('Attending a local fair or festival is one way to feel part of a ___.', ['Community', 'Desert', 'Ocean', 'Forest'], 0)]),
]),
day(169, [
L('Punctuation: Commas in a List',
  'Kindergarten Language strand: a comma is used to separate items in a list, such as in the sentence I have a cat, a dog, and a bird.',
  [('What punctuation mark is used to separate items in a list?', ['a comma', 'comma']),
   ('Where do we put a comma in a list of three items?', ['between each item', 'after the first two items']),
   ('Give an example of a sentence with a list that uses commas.', ['I have a cat, a dog, and a bird', 'I like apples, bananas, and grapes'])],
  [('What punctuation mark separates items in a list?', ['A comma', 'A period', 'A question mark', 'An exclamation mark'], 0),
   ('In the sentence I have a cat, a dog, and a bird, how many commas are used?', ['1', '2', '3', '4'], 1),
   ('Which sentence correctly uses commas in a list?', ['I like red, blue, and green', 'I like red blue and green', 'I like red. blue. and green.', 'I like red; blue; and green'], 0),
   ('A comma helps readers know where one item in a list ___.', ['Ends and the next begins', 'Is the loudest', 'Is the most important', 'Is coloured'], 0),
   ('Which of these is an example of a list that needs commas?', ['Apples, oranges, and pears', 'One single apple', 'A short question', 'A single exclamation'], 0)]),
M('Place Value: Comparing Two-Digit Numbers',
  'Kindergarten Math strand: students use their understanding of tens and ones to compare two-digit numbers and decide which number is greater or less.',
  [('Which number is greater, 42 or 24?', ['42', 'forty two']),
   ('How many tens are in the number 35?', ['3', 'three']),
   ('Why does knowing the tens digit help us compare two numbers?', ['the number with more tens is usually greater', 'it tells us which number is bigger'])],
  [('Which number is greater, 53 or 35?', ['53', '35', 'they are equal', 'neither'], 0),
   ('How many tens are in the number 47?', ['3', '4', '5', '7'], 1),
   ('When comparing two two-digit numbers, which digit should you look at first?', ['The tens digit', 'The ones digit', 'Neither digit', 'Only the colour'], 0),
   ('Which number is less, 61 or 16?', ['61', '16', 'they are equal', 'neither'], 1),
   ('If two numbers have the same tens digit, which digit do you compare next?', ['The ones digit', 'The tens digit again', 'Neither', 'The colour'], 0)]),
Sc('Hummingbirds: Tiny Fast-Flying Birds',
   'Kindergarten Science strand: hummingbirds are tiny birds that flap their wings very fast, letting them hover in the air while they drink nectar from flowers.',
   [('What do hummingbirds drink from flowers?', ['nectar', 'flower nectar']),
    ('What can a hummingbird do while it flaps its wings very fast?', ['hover in the air', 'stay in one spot in the air']),
    ('Are hummingbirds large or small birds?', ['small', 'tiny'])],
   [('What do hummingbirds drink from flowers?', ['Nectar', 'Water only', 'Milk', 'Juice'], 0),
    ('What special thing can hummingbirds do because they flap their wings so fast?', ['Hover in one spot in the air', 'Swim underwater', 'Dig tunnels', 'Change colour'], 0),
    ('Are hummingbirds large or small birds?', ['Small and tiny', 'Very large', 'The largest birds in the world', 'The size of an eagle'], 0),
    ('A hummingbird flaps its wings so fast that they can be hard to ___.', ['See clearly', 'Hear loudly', 'Find quickly', 'Feed slowly'], 0),
    ('Hummingbirds are known for being one of the ___ birds.', ['Smallest', 'Largest', 'Loudest', 'Slowest'], 0)]),
SS('Our Building Inspectors: Keeping Buildings Safe',
   'Kindergarten Social Studies strand: building inspectors check that new buildings are built safely and follow the rules before people are allowed to live or work inside them.',
   [('What do building inspectors check?', ['that buildings are safe', 'if buildings follow the rules']),
    ('Why is it important for a building to be inspected before people move in?', ['to make sure it is safe', 'so everyone inside stays safe']),
    ('Name one thing a building inspector might look at.', ['the walls', 'the wiring'])],
   [('What is the main job of a building inspector?', ['Checking that buildings are built safely', 'Cooking food', 'Flying planes', 'Cutting hair'], 0),
    ('Why do buildings need to be inspected before people move in?', ['To make sure the building is safe', 'Inspections are never needed', 'To make the building louder', 'To paint the walls'], 0),
    ('Which of these might a building inspector check?', ['The wiring and walls', 'The weather forecast', 'A grocery list', 'A bus schedule'], 0),
    ('Building inspectors help protect the safety of people who will ___.', ['Live or work in the building', 'Never enter the building', 'Fly over the building', 'Avoid the building forever'], 0),
    ('A building that passes inspection is considered ___.', ['Safe to use', 'Dangerous', 'Incomplete forever', 'Invisible'], 0)]),
]),
day(170, [
L('Language Review: New Word Families, Vowel Teams, and Punctuation',
  'Kindergarten Language strand review: students revisit the -ad, -ag, and -am word families, vowel teams igh and ow/ou, r-controlled ur, the suffix -ly, the prefix dis-, and commas in a list.',
  [('Name a word from the -ad, -ag, or -am family.', ['bad', 'tag']),
   ('What does the prefix dis- usually mean?', ['not']),
   ('What punctuation mark separates items in a list?', ['a comma'])],
  [('Which word belongs to the -ad family?', ['Sun', 'Sad', 'Bed', 'Top'], 1),
   ('Which word has the igh vowel team?', ['Night', 'Net', 'Nit', 'Not'], 0),
   ('What does the word dislike mean?', ['To not like something', 'To really enjoy something', 'To agree with something', 'To forget something'], 0),
   ('What punctuation mark separates items in a list?', ['A comma', 'A period', 'A question mark', 'An exclamation mark'], 0),
   ('What does the word quickly mean?', ['Done in a fast way', 'Done very slowly', 'Not moving at all', 'Done loudly only'], 0)]),
M('Math Review: Skip Counting, Fractions, and Money',
  'Kindergarten Math strand review: students revisit skip counting by 7s and 8s, even numbers, comparing durations, fourths, counting coins to a dollar, estimating capacity, addition and subtraction stories to 20, and comparing two-digit numbers.',
  [('What comes next: 7, 14, 21, ___?', ['28']),
   ('How many fourths make one whole?', ['4']),
   ('How many cents make one dollar?', ['100'])],
  [('What comes next: 7, 14, 21, ___?', ['22', '27', '28', '29'], 2),
   ('Which set of numbers shows counting by even numbers?', ['2, 4, 6, 8', '1, 3, 5, 7', '1, 2, 3, 4', '5, 10, 15, 20'], 0),
   ('If a shape is cut into four equal parts, what is each part called?', ['A fourth', 'A half', 'A third', 'A whole'], 0),
   ('How many cents make one dollar?', ['50', '75', '100', '200'], 2),
   ('Which number is greater, 53 or 35?', ['53', '35', 'they are equal', 'neither'], 0)]),
Sc('Science Review: Life Cycles, Ocean Animals, and Weather',
   'Kindergarten Science strand review: students revisit the life cycle of a dragonfly, jellyfish, octopus, elephants, tornadoes, fingernails and hair, evergreen and deciduous trees, earthquakes, and hummingbirds.',
   [('Where does a dragonfly life cycle begin?', ['as an egg in water']),
    ('How many arms does an octopus have?', ['eight']),
    ('What do hummingbirds drink from flowers?', ['nectar'])],
   [('Where does a dragonfly life cycle begin?', ['As an egg in water', 'As an egg in the desert', 'As an adult in the sky', 'As an egg in a tree'], 0),
    ('Does a jellyfish have bones inside its body?', ['Yes', 'No', 'Only in its head', 'Only in its tentacles'], 1),
    ('What are elephants known for being?', ['The largest land animals', 'The smallest land animals', 'The fastest ocean animals', 'The smallest insects'], 0),
    ('What happens to the ground during an earthquake?', ['It shakes suddenly', 'It turns to water', 'It disappears', 'It grows taller'], 0),
    ('What do hummingbirds drink from flowers?', ['Nectar', 'Water only', 'Milk', 'Juice'], 0)]),
SS('Social Studies Review: Helpers, Geography, and Trade',
   'Kindergarten Social Studies strand review: students revisit plumbers, hairdressers and barbers, judges and courts, Canadian geography, trading goods, interpreters, the Royal Canadian Mint, community festivals, and building inspectors.',
   [('What is the main job of a plumber?', ['fixing pipes and water leaks']),
    ('What is a prairie?', ['a large area of flat land']),
    ('What is the main job of a building inspector?', ['checking that buildings are built safely'])],
   [('What is the main job of a plumber?', ['Fixing pipes and water leaks', 'Teaching school', 'Flying airplanes', 'Growing food'], 0),
    ('Where does a judge usually work?', ['In a court', 'In a kitchen', 'On a farm', 'In an airplane'], 0),
    ('What is a prairie?', ['A large area of flat land', 'A tall mountain', 'A deep ocean', 'A small pond'], 0),
    ('What is the Royal Canadian Mint?', ['A place where Canadian coins are made', 'A type of coin', 'A grocery store', 'A school'], 0),
    ('What is the main job of a building inspector?', ['Checking that buildings are built safely', 'Cooking food', 'Flying planes', 'Cutting hair'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_161_170)
    append_worksheet_days(0, g0_161_170)
