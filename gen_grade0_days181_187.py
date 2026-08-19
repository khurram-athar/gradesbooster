#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 181-187 -- sixteenth and FINAL batch for this
grade, completing the full 187-day Ontario curriculum target. Self-contained
script (does NOT use gen_curriculum.py's sub()/day()/append_to(), since those
do not support a worksheet field) modeled exactly on gen_grade0_days171_180.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

This batch is only 7 days (181-187), not the usual 10, because 180 + 7 = 187
is the full-year target: 6 new content days (181-186, one new topic per
subject per day) plus Day 187 as a final cross-subject review day.

Topics chosen to avoid overlap with existing Grade 0 Days 1-180 (dumped and
checked against data/grade0.json before writing):

Language: word families -est and -ump; vowel teams ue and ew; r-controlled
wor words; the suffix -en; the prefix mis-. Skip every previously used word
family (-at, -an, -ig, -ug, -ot, -et, -ap, -in, -ub, -og, -ip, -op, -ack,
-ock, -ick, -ell, -ill, -ut, -un, -ad, -ag, -am, -ay, -oy, -ink), every
previously used vowel team (ai, ee, oa, ea, igh, ow, ou, oo), every
previously used r-controlled pattern (ar, or, er, ir, ur, are), every
previously used suffix (-ing, -ed, -es, -er, -y, -ful, -less, -ly, -ness),
and every previously used prefix (un-, re-, pre-, dis-, non-).

Math: number bonds to 14; subtracting two-digit numbers without regrouping;
counting to 200; the octagon; counting loonies and toonies; understanding
AM and PM. Skip number bonds already made (4, 9, 11, 12, 13), addition
(already done for two-digit numbers), counting already reached (150),
shapes already introduced (pentagon, hexagon, trapezoid, rhombus, cone,
pyramid, sphere, cube, cylinder), money already covered (pennies, nickels,
dimes, quarters, coins to a dollar, making change), and time already
covered (day/night, digital clock, hour, half hour, five-minute intervals,
elapsed time).

Science: raccoons, skunks, whales, moose, eagles, and earthworms. Skip
every previously covered animal (sea turtles, crabs, polar bears, snakes,
dolphins, sea otters, fireflies, owls, penguins, foxes/deer/squirrels as a
group, sharks, octopus, jellyfish, elephants, hummingbirds, spiders, and
many more) and every previously covered non-animal topic (glaciers, caves,
seasons, weather, water cycle, etc.).

Social Studies: zookeepers, mechanics, park rangers, engineers, coaches,
and train conductors. Skip every previously covered community helper
(water treatment workers, meteorologists, beekeepers, tailors, border
officers, photographers, postal workers, dentists, veterinarians,
librarians, construction workers, crossing guards, pharmacists, school bus
drivers, police and firefighters, grocers, bakers, farmers, conservation
officers, and many more) and every previously covered place/topic (the
Great Lakes, provincial symbols, Canadas national parks, and many more).

Day 187 is the final cross-subject review day, quizzing topics from the
immediately preceding six days (181-186) in the same mechanical format used
by every prior batch's review day, with review titles textually distinct
from every earlier review day's title for each subject. Since this is the
very last day of the entire K-12 curriculum build for Grade 0, the review
titles and summaries acknowledge this is the capstone/end-of-program review
("Our Final ..."), while the quiz and worksheet content strictly follows
the standard review-day mechanics (testing material from days 181-186
only).

No embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely, matching this project's convention (e.g.
"raccoons eyes" not "raccoon's eyes"), since this text gets embedded
directly into TypeScript string literals.
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


g0_181_187 = [
day(181, [
L('Word Families: -est Words',
  'Kindergarten Language strand: the -est word family shares the same ending sound, as in best, nest, rest, and test.',
  [('Name a word that rhymes with nest.', ['best', 'test']),
   ('What ending sound do best and rest share?', ['est', 'the est sound']),
   ('Is west part of the -est family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -est family?', ['Sun', 'Nest', 'Bed', 'Top'], 1),
   ('Which word rhymes with best?', ['Sit', 'Nest', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -est family?', ['Nest', 'Best', 'Rest', 'Sun'], 3),
   ('Complete the rhyme: A little bird built a ___ in the tree.', ['nest', 'not', 'nap', 'net'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Number Bonds: Ways to Make 14',
  'Kindergarten Math strand: students explore the different pairs of numbers that add together to make 14, such as 7 and 7, or 9 and 5.',
  [('Name two numbers that add together to make 14.', ['7 and 7', '9 and 5']),
   ('If one part of 14 is 8, what is the other part?', ['6', 'six']),
   ('Is 14 an even or odd number?', ['even', 'even number'])],
  [('Which pair of numbers makes 14?', ['7 and 7', '6 and 9', '5 and 10', '4 and 8'], 0),
   ('If one part of 14 is 8, what is the other part?', ['4', '5', '6', '7'], 2),
   ('Which pair does NOT make 14?', ['9 and 5', '8 and 6', '10 and 4', '7 and 8'], 3),
   ('14 is one more than which number?', ['12', '13', '15', '16'], 1),
   ('Finding different ways to make the same number is called ___.', ['Number bonds', 'Skip counting', 'Estimating', 'Sorting'], 0)]),
Sc('Raccoons: Clever Nighttime Visitors',
   'Kindergarten Science strand: a raccoon is a nocturnal mammal with a striped tail and a black mask of fur around its eyes that uses its clever paws to open containers and find food.',
   [('What covers a raccoons eyes like a mask?', ['black fur', 'a black mask of fur']),
    ('When is a raccoon usually active?', ['at night', 'nighttime']),
    ('What does a raccoon use its paws for?', ['to open containers and find food', 'finding food'])],
   [('What covers a raccoons eyes like a mask?', ['Black fur', 'White feathers', 'Green scales', 'Orange fur'], 0),
    ('When is a raccoon usually most active?', ['At night', 'At noon', 'Underwater', 'In winter only'], 0),
    ('What does a raccoon use its clever paws for?', ['Opening containers and finding food', 'Flying', 'Digging tunnels only', 'Swimming great distances'], 0),
    ('A raccoon is what type of animal?', ['A mammal', 'A reptile', 'An insect', 'A bird'], 0),
    ('An animal that is mostly active at night is called ___.', ['Nocturnal', 'Diurnal', 'Hibernating', 'Migrating'], 0)]),
SS('Our Zookeepers: Caring for Animals at the Zoo',
   'Kindergarten Social Studies strand: zookeepers feed, clean up after, and care for the health of animals living at the zoo, helping visitors learn about animals from around the world.',
   [('What do zookeepers do for zoo animals?', ['feed and care for them', 'clean up after them']),
    ('Why do zookeepers check on animal health?', ['to keep animals healthy', 'so animals stay healthy']),
    ('What can visitors learn at a zoo?', ['about animals from around the world', 'about different animals'])],
   [('What is the main job of a zookeeper?', ['Feeding and caring for zoo animals', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('Why do zookeepers check on the health of animals?', ['To keep the animals healthy', 'Health is not important', 'To make animals louder', 'To sell the animals'], 0),
    ('What can people learn by visiting a zoo?', ['About animals from around the world', 'Nothing at all', 'Only about plants', 'Only about the weather'], 0),
    ('Zookeepers help make sure zoo animals have ___.', ['Food, water, and care', 'No food at all', 'Only toys', 'Only noise'], 0),
    ('Which of these is a task a zookeeper might do?', ['Cleaning animal habitats', 'Delivering mail', 'Building roads', 'Selling groceries'], 0)]),
]),
day(182, [
L('Word Families: -ump Words',
  'Kindergarten Language strand: the -ump word family shares the same ending sound, as in jump, bump, lump, and pump.',
  [('Name a word that rhymes with jump.', ['bump', 'pump']),
   ('What ending sound do bump and lump share?', ['ump', 'the ump sound']),
   ('Is pump part of the -ump family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ump family?', ['Sun', 'Jump', 'Bed', 'Top'], 1),
   ('Which word rhymes with bump?', ['Sit', 'Jump', 'Sock', 'Sun'], 1),
   ('Which word does NOT belong to the -ump family?', ['Jump', 'Bump', 'Pump', 'Sun'], 3),
   ('Complete the rhyme: I like to run and ___ over the puddle.', ['jump', 'jam', 'jog', 'jet'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Subtraction: Two-Digit Numbers Without Regrouping',
  'Kindergarten Math strand: students subtract two two-digit numbers by subtracting the ones and the tens separately, without needing to regroup.',
  [('What is 38 minus 15?', ['23', 'twenty three']),
   ('When subtracting 46 minus 22, what do you subtract first?', ['the ones', 'ones digits']),
   ('What is 59 minus 27?', ['32', 'thirty two'])],
  [('What is 38 minus 15?', ['21', '22', '23', '24'], 2),
   ('What is 59 minus 27?', ['30', '31', '32', '33'], 2),
   ('When subtracting two two-digit numbers, which digits do we usually subtract first?', ['The ones digits', 'The tens digits', 'Neither digit', 'Only the first number'], 0),
   ('What is 47 minus 24?', ['21', '22', '23', '24'], 2),
   ('What is 68 minus 35?', ['31', '32', '33', '34'], 2)]),
Sc('Skunks: Animals with a Smelly Defence',
   'Kindergarten Science strand: a skunk is a small black-and-white mammal that sprays a strong-smelling liquid to defend itself when it feels scared or threatened.',
   [('What colours is a skunks fur?', ['black and white', 'black-and-white']),
    ('What does a skunk spray to defend itself?', ['a strong-smelling liquid', 'smelly spray']),
    ('When does a skunk spray its smelly liquid?', ['when it feels scared or threatened', 'when threatened'])],
   [('What colours is a skunks fur?', ['Black and white', 'Brown and orange', 'Green and yellow', 'All white'], 0),
    ('How does a skunk defend itself?', ['By spraying a strong-smelling liquid', 'By flying away', 'By biting only', 'By hiding underwater'], 0),
    ('When does a skunk usually spray its smelly liquid?', ['When it feels scared or threatened', 'Every morning', 'Only while sleeping', 'Never'], 0),
    ('A skunk is what type of animal?', ['A mammal', 'A reptile', 'An insect', 'A fish'], 0),
    ('A skunks smelly spray is an example of an animal ___.', ['Defence', 'Habitat', 'Life cycle', 'Migration'], 0)]),
SS('Our Mechanics: Fixing Cars and Trucks',
   'Kindergarten Social Studies strand: mechanics repair and maintain cars and trucks so that vehicles run safely and community members can travel where they need to go.',
   [('What do mechanics fix?', ['cars and trucks', 'vehicles']),
    ('Why is it important for vehicles to be fixed properly?', ['so they run safely', 'to keep people safe']),
    ('Name one tool a mechanic might use.', ['a wrench', 'a jack'])],
   [('What is the main job of a mechanic?', ['Fixing and maintaining cars and trucks', 'Cutting hair', 'Teaching school', 'Flying planes'], 0),
    ('Why is it important for a mechanic to fix vehicles properly?', ['So vehicles run safely', 'Safety does not matter', 'To make vehicles louder', 'To make vehicles disappear'], 0),
    ('Which tool might a mechanic use?', ['A wrench', 'A stethoscope', 'A paintbrush', 'A microphone'], 0),
    ('Mechanics help our community by keeping vehicles ___.', ['Running safely', 'Broken', 'Loud', 'Dirty'], 0),
    ('Which of these might a mechanic repair?', ['A cars engine', 'A broken tooth', 'A torn shirt', 'A leaking pipe'], 0)]),
]),
day(183, [
L('Vowel Teams: ue and ew Words',
  'Kindergarten Language strand: the letters ue and ew together can make a long u sound, as in blue and few.',
  [('What sound do the letters ue make in the word blue?', ['a long u sound', 'long u']),
   ('Give another word with the ew vowel team.', ['few', 'new']),
   ('Is glue a word with the ue vowel team?', ['yes', 'yes it is'])],
  [('Which word has the ue vowel team?', ['Blue', 'Ball', 'Bat', 'Bed'], 0),
   ('What sound do the letters ew make in the word new?', ['A long u sound', 'A short a sound', 'A silent sound', 'A long e sound'], 0),
   ('Which of these words has the ew vowel team?', ['Few', 'Fun', 'Fit', 'Fat'], 0),
   ('Complete the rhyme: The sky above us is coloured ___.', ['blue', 'black', 'brown', 'big'], 0),
   ('When two letters team up to make one sound, it is called a ___.', ['Vowel team', 'Consonant blend', 'Suffix', 'Prefix'], 0)]),
M('Numbers to 200: Counting Beyond 150',
  'Kindergarten Math strand: students continue counting past 150, saying number names in order all the way up to 200.',
  [('What number comes after 150?', ['151', 'one hundred fifty one']),
   ('Count from 168 to 172.', ['168,169,170,171,172', '168 169 170 171 172']),
   ('What number comes right before 200?', ['199', 'one hundred ninety nine'])],
  [('What number comes right after 159?', ['158', '160', '161', '170'], 1),
   ('Which number comes between 175 and 177?', ['174', '176', '178', '179'], 1),
   ('What number comes right before 200?', ['198', '199', '201', '202'], 1),
   ('Counting past 150 all the way to 200 means we say numbers in ___.', ['Order', 'Reverse only', 'Random order', 'Groups of five only'], 0),
   ('Which of these numbers is greater than 180?', ['192', '165', '148', '99'], 0)]),
Sc('Whales: Enormous Mammals of the Ocean',
   'Kindergarten Science strand: a whale is a huge ocean mammal that breathes air through a blowhole and can be one of the largest animals ever to live on Earth.',
   [('How does a whale breathe?', ['through a blowhole', 'it breathes air']),
    ('Is a whale a fish or a mammal?', ['a mammal', 'mammal']),
    ('What makes some whales record-setting animals?', ['they can be the largest animals on Earth', 'their huge size'])],
   [('How does a whale breathe?', ['Through a blowhole', 'Through gills', 'Through its skin', 'It does not breathe'], 0),
    ('Is a whale a fish or a mammal?', ['A mammal', 'A fish', 'An insect', 'A reptile'], 0),
    ('Some whales can be among the ___ animals ever to live on Earth.', ['Largest', 'Smallest', 'Fastest flying', 'Loudest buzzing'], 0),
    ('Where do whales live?', ['In the ocean', 'In deserts', 'In forests', 'In caves'], 0),
    ('Whales are known for making loud sounds to ___ with each other.', ['Communicate', 'Cook', 'Build', 'Draw'], 0)]),
SS('Our Park Rangers: Guiding Visitors and Caring for Trails',
   'Kindergarten Social Studies strand: park rangers welcome visitors, share information about nature, and take care of trails and green spaces so that parks stay safe and enjoyable for everyone.',
   [('What do park rangers share with visitors?', ['information about nature', 'nature facts']),
    ('What do park rangers take care of?', ['trails and green spaces', 'trails']),
    ('Why is it important for parks to stay safe?', ['so everyone can enjoy them', 'for visitors safety'])],
   [('What is the main job of a park ranger?', ['Guiding visitors and caring for trails', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('What might a park ranger share with visitors?', ['Information about nature and safety', 'Recipes for dinner', 'Bus schedules', 'Math homework'], 0),
    ('What do park rangers help take care of?', ['Trails and green spaces', 'Shopping malls', 'Hospitals', 'Factories'], 0),
    ('Why is it important for parks to be well cared for?', ['So they stay safe and enjoyable for everyone', 'Parks do not need care', 'So no one can visit', 'So plants stop growing'], 0),
    ('Which of these might a park ranger do?', ['Lead a nature walk', 'Deliver mail', 'Sell groceries', 'Repair a car'], 0)]),
]),
day(184, [
L('R-Controlled Vowels: wor Words',
  'Kindergarten Language strand: when the letters or follow the letter w, they often make an er sound, as in work, word, and world.',
  [('What sound do the letters or make in the word work?', ['the er sound', 'ur sound']),
   ('Give another word that has the wor pattern.', ['word', 'world']),
   ('Does worm start with the wor pattern?', ['yes', 'yes it does'])],
  [('Which word has the wor pattern making an er sound?', ['Work', 'Wet', 'Win', 'Wag'], 0),
   ('Which of these words has the r-controlled wor pattern?', ['World', 'Wag', 'Win', 'Wet'], 0),
   ('Complete the sentence: A small creature that lives in soil is called a ___.', ['worm', 'wag', 'win', 'wig'], 0),
   ('Which word rhymes with word?', ['Bird', 'Bad', 'Bed', 'Bud'], 0),
   ('R-controlled vowels change how a vowel ___.', ['Sounds', 'Looks on the page', 'Is spelled only', 'Is coloured'], 0)]),
M('Shapes: Introducing the Octagon',
  'Kindergarten Math strand: an octagon is a shape with eight straight sides and eight corners, like the shape of a stop sign.',
  [('How many sides does an octagon have?', ['8', 'eight']),
   ('How many corners does an octagon have?', ['8', 'eight']),
   ('Name a real object shaped like an octagon.', ['a stop sign', 'stop sign'])],
  [('How many sides does an octagon have?', ['Five', 'Six', 'Seven', 'Eight'], 3),
   ('How many corners does an octagon have?', ['Five', 'Six', 'Seven', 'Eight'], 3),
   ('Which real object is shaped like an octagon?', ['A stop sign', 'A wheel', 'A door', 'A ball'], 0),
   ('An octagon has more sides than a ___.', ['Hexagon', 'Nonagon', 'Decagon', 'None of these'], 0),
   ('A shape with eight straight sides is called a ___.', ['Octagon', 'Pentagon', 'Hexagon', 'Trapezoid'], 0)]),
Sc('Moose: Giants of the Canadian Forest',
   'Kindergarten Science strand: a moose is a huge Canadian forest animal with long legs, a large nose, and wide antlers that only male moose grow.',
   [('Where does a moose usually live?', ['in the Canadian forest', 'in forests']),
    ('What do male moose grow that female moose do not?', ['antlers', 'wide antlers']),
    ('What is unusual about a moose nose?', ['it is large', 'a large nose'])],
   [('Where does a moose usually live?', ['In the Canadian forest', 'In the desert', 'In the ocean', 'Underground'], 0),
    ('Which moose grow wide antlers?', ['Male moose', 'Female moose', 'Baby moose only', 'No moose grow antlers'], 0),
    ('What is a noticeable feature of a moose face?', ['A large nose', 'A short beak', 'A tiny mouth', 'No nose at all'], 0),
    ('A moose has what kind of legs?', ['Long legs', 'Very short legs', 'No legs', 'Wings instead of legs'], 0),
    ('The moose is an animal often associated with ___.', ['Canadian forests', 'Ocean reefs', 'Sandy deserts', 'Tropical rainforests'], 0)]),
SS('Our Engineers: Designing and Building for Our Community',
   'Kindergarten Social Studies strand: engineers plan and design things our community needs, such as bridges, roads, and buildings, making sure they are safe and built to last.',
   [('What do engineers design?', ['bridges, roads, and buildings', 'things our community needs']),
    ('Why do engineers make sure their designs are safe?', ['so structures do not fail', 'for community safety']),
    ('Name one thing an engineer might help build.', ['a bridge', 'a road'])],
   [('What is the main job of an engineer?', ['Designing and building things our community needs', 'Cutting hair', 'Teaching school', 'Flying planes'], 0),
    ('Why do engineers make sure their designs are safe?', ['So structures do not fail and people stay safe', 'Safety does not matter', 'To make buildings fall down', 'To waste materials'], 0),
    ('Which of these might an engineer help design?', ['A bridge', 'A haircut', 'A grocery list', 'A song'], 0),
    ('Engineers help make sure buildings and roads are built to ___.', ['Last and be safe', 'Fall apart quickly', 'Disappear', 'Change colour'], 0),
    ('Which of these is an example of something an engineer might plan?', ['A new road', 'A birthday cake', 'A haircut', 'A bedtime story'], 0)]),
]),
day(185, [
L('Suffixes: Adding -en to Change Meaning',
  'Kindergarten Language strand: adding the suffix -en to the end of a word can turn it into a describing word, such as changing wood into wooden, meaning made of wood.',
  [('What does wooden mean?', ['made of wood', 'made from wood']),
   ('What does the suffix -en usually do to a word?', ['turns it into a describing word', 'shows what something is made of']),
   ('Give an example of a word with the suffix -en.', ['wooden', 'golden'])],
  [('What does the word wooden mean?', ['Made of wood', 'Made of metal', 'A type of food', 'A colour'], 0),
   ('What does the suffix -en usually add to a word?', ['The meaning of being made of something', 'A number', 'A place', 'An action'], 0),
   ('Which word means made of gold?', ['Golden', 'Goldly', 'Golder', 'Ungold'], 0),
   ('Adding -en to the word wool could make the word ___.', ['Woolen, meaning made of wool', 'Woolly only', 'Wooler', 'Unwool'], 0),
   ('A suffix that changes a naming word into a describing word is often added to the ___ of a word.', ['End', 'Beginning', 'Middle', 'Nowhere'], 0)]),
M('Money: Counting Loonies and Toonies',
  'Kindergarten Math strand: a loonie is a Canadian one-dollar coin and a toonie is a Canadian two-dollar coin, and students count groups of loonies and toonies to find a total.',
  [('How much is one loonie worth?', ['1 dollar', 'one dollar']),
   ('How much is one toonie worth?', ['2 dollars', 'two dollars']),
   ('How much are two loonies worth together?', ['2 dollars', 'two dollars'])],
  [('How much is one loonie worth?', ['50 cents', '1 dollar', '2 dollars', '5 dollars'], 1),
   ('How much is one toonie worth?', ['1 dollar', '2 dollars', '5 dollars', '10 dollars'], 1),
   ('How much are three loonies worth together?', ['1 dollar', '2 dollars', '3 dollars', '4 dollars'], 2),
   ('How much are two toonies worth together?', ['2 dollars', '3 dollars', '4 dollars', '5 dollars'], 2),
   ('Which Canadian coin is worth more, a loonie or a toonie?', ['A toonie', 'A loonie', 'They are equal', 'Neither has value'], 0)]),
Sc('Eagles: Powerful Birds of Prey',
   'Kindergarten Science strand: an eagle is a powerful bird with sharp eyesight, strong talons, and a hooked beak that it uses to hunt other animals for food.',
   [('What does an eagle use its talons for?', ['to hunt', 'to catch food']),
    ('What kind of eyesight does an eagle have?', ['sharp eyesight', 'very sharp eyesight']),
    ('What shape is an eagles beak?', ['hooked', 'a hooked shape'])],
   [('What does an eagle use its sharp talons for?', ['Catching and holding prey', 'Swimming', 'Digging tunnels', 'Building nests only'], 0),
    ('What kind of eyesight does an eagle have?', ['Very sharp eyesight', 'Very poor eyesight', 'No eyesight at all', 'Blurry eyesight'], 0),
    ('What shape is an eagles beak?', ['Hooked', 'Flat', 'Straight and thin', 'Round like a ball'], 0),
    ('An eagle is what type of animal?', ['A bird', 'A mammal', 'A reptile', 'An insect'], 0),
    ('A bird that hunts other animals for food is called a bird of ___.', ['Prey', 'Paradise', 'Migration', 'Habitat'], 0)]),
SS('Our Coaches: Teaching Us to Play and Work Together',
   'Kindergarten Social Studies strand: coaches teach skills, rules, and teamwork for sports and activities, helping children learn to work together and try their best.',
   [('What do coaches teach?', ['skills, rules, and teamwork', 'how to play a sport']),
    ('Why is teamwork important in sports?', ['it helps everyone work together', 'so the team can succeed together']),
    ('Name one thing a coach might help you learn.', ['a new skill', 'the rules of a game'])],
   [('What is the main job of a coach?', ['Teaching skills, rules, and teamwork', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('Why do coaches teach teamwork?', ['To help players work together and succeed', 'Teamwork is not important', 'To make players argue', 'To slow the game down'], 0),
    ('Which of these might a coach help a child learn?', ['A new sports skill', 'A math equation', 'A recipe', 'A song lyric'], 0),
    ('Coaches help players learn to try their ___.', ['Best', 'Worst', 'Slowest', 'Least'], 0),
    ('Which of these is something a coach might do?', ['Lead a team practice', 'Deliver mail', 'Sell groceries', 'Fix a car'], 0)]),
]),
day(186, [
L('Prefixes: Adding Mis- to Change Meaning',
  'Kindergarten Language strand: adding the prefix mis- to the start of a word can mean wrongly or badly, such as changing spell into misspell, meaning to spell wrongly.',
  [('What does misspell mean?', ['to spell wrongly', 'to spell incorrectly']),
   ('What does the prefix mis- usually mean?', ['wrongly', 'badly']),
   ('Give an example of a word with the prefix mis-.', ['misspell', 'misplace'])],
  [('What does the word misspell mean?', ['To spell a word wrongly', 'To spell a word correctly', 'To read quickly', 'To write neatly'], 0),
   ('What does the prefix mis- usually add to a word?', ['The meaning of wrongly or badly', 'The meaning of again', 'A number', 'A colour'], 0),
   ('Which word means to place something in the wrong spot?', ['Misplace', 'Replace', 'Placement', 'Placer'], 0),
   ('Adding mis- to the word understand makes the word ___.', ['Misunderstand, meaning to understand wrongly', 'Understandable', 'Understanding only', 'Reunderstand'], 0),
   ('A prefix is added to the ___ of a word.', ['Beginning', 'End', 'Middle', 'Nowhere'], 0)]),
M('Time: Understanding AM and PM',
  'Kindergarten Math strand: students learn that AM refers to the morning hours before noon, and PM refers to the afternoon and evening hours after noon.',
  [('Does AM mean morning or afternoon?', ['morning', 'the morning hours']),
   ('Does PM mean afternoon and evening or morning?', ['afternoon and evening', 'the afternoon and evening hours']),
   ('Is eating breakfast usually an AM or PM activity?', ['AM', 'morning'])],
  [('What does AM refer to?', ['The morning hours before noon', 'The afternoon hours', 'The evening hours', 'Midnight only'], 0),
   ('What does PM refer to?', ['The afternoon and evening hours after noon', 'The morning hours', 'Only midnight', 'Only noon'], 0),
   ('Eating breakfast usually happens during ___.', ['AM', 'PM', 'Neither', 'Both at once'], 0),
   ('Going to bed at night usually happens during ___.', ['PM', 'AM', 'Neither', 'Both at once'], 0),
   ('AM and PM help us know whether it is ___.', ['Morning or afternoon and evening', 'Hot or cold', 'Sunny or rainy', 'A weekday or weekend'], 0)]),
Sc('Earthworms: Helpers Beneath the Soil',
   'Kindergarten Science strand: an earthworm is a small, legless creature that lives in soil, eating and burrowing through dirt in ways that help plants grow.',
   [('Where does an earthworm usually live?', ['in soil', 'underground']),
    ('How many legs does an earthworm have?', ['none', 'zero']),
    ('How does an earthworm help plants grow?', ['by burrowing through and mixing the soil', 'by helping the soil'])],
   [('Where does an earthworm usually live?', ['In soil', 'In trees', 'In the ocean', 'In the sky'], 0),
    ('How many legs does an earthworm have?', ['Zero', 'Two', 'Four', 'Six'], 0),
    ('How does an earthworm help plants grow?', ['By burrowing through and mixing the soil', 'By eating the plants leaves', 'By blocking sunlight', 'By drying out the soil'], 0),
    ('An earthworm moves by ___.', ['Wiggling and stretching its body', 'Flying', 'Hopping on legs', 'Rolling like a ball'], 0),
    ('Earthworms are considered helpful because they improve the ___.', ['Soil', 'Weather', 'Ocean', 'Sky'], 0)]),
SS('Our Train Conductors: Keeping Passengers Safe on the Rails',
   'Kindergarten Social Studies strand: train conductors check tickets, announce stops, and watch over passengers to help trains run safely and on schedule.',
   [('What does a train conductor check?', ['tickets', 'passenger tickets']),
    ('What does a train conductor announce?', ['stops', 'the stops']),
    ('Why is it important for trains to run on schedule?', ['so passengers arrive on time', 'to keep things organized'])],
   [('What is the main job of a train conductor?', ['Keeping passengers safe and trains on schedule', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('What might a train conductor check as passengers board?', ['Tickets', 'Groceries', 'Homework', 'Recipes'], 0),
    ('Why does a train conductor announce upcoming stops?', ['So passengers know when to get off', 'To confuse passengers', 'To make the trip longer', 'To play music'], 0),
    ('Train conductors help make sure trains run ___.', ['Safely and on schedule', 'Randomly', 'Only at night', 'Backwards'], 0),
    ('Which of these is a task a train conductor might do?', ['Watching over passengers', 'Delivering mail', 'Selling groceries', 'Repairing a car'], 0)]),
]),
day(187, [
L('Language Review: Our Final Words, Sounds, and Stories',
  'Kindergarten Language strand review, and the final Language lesson of the kindergarten curriculum: students revisit the -est and -ump word families, vowel teams ue and ew, r-controlled wor words, the suffix -en, and the prefix mis-.',
  [('Name a word from the -est or -ump family.', ['nest', 'jump']),
   ('What does the prefix mis- usually mean?', ['wrongly']),
   ('What does the suffix -en usually do to a word?', ['turns it into a describing word'])],
  [('Which word belongs to the -est family?', ['Sun', 'Nest', 'Bed', 'Top'], 1),
   ('Which word has the ue vowel team?', ['Blue', 'Ball', 'Bat', 'Bed'], 0),
   ('Which word has the wor pattern making an er sound?', ['Work', 'Wet', 'Win', 'Wag'], 0),
   ('What does the word wooden mean?', ['Made of wood', 'Made of metal', 'A type of food', 'A colour'], 0),
   ('What does the word misspell mean?', ['To spell a word wrongly', 'To spell a word correctly', 'To read quickly', 'To write neatly'], 0)]),
M('Math Review: Our Final Numbers, Shapes, and Time',
  'Kindergarten Math strand review, and the final Math lesson of the kindergarten curriculum: students revisit number bonds to 14, subtracting two-digit numbers, counting to 200, the octagon, counting loonies and toonies, and understanding AM and PM.',
  [('Name two numbers that add together to make 14.', ['7 and 7']),
   ('How many sides does an octagon have?', ['8']),
   ('How much is one toonie worth?', ['2 dollars'])],
  [('Which pair of numbers makes 14?', ['7 and 7', '6 and 9', '5 and 10', '4 and 8'], 0),
   ('What is 38 minus 15?', ['21', '22', '23', '24'], 2),
   ('What number comes right before 200?', ['198', '199', '201', '202'], 1),
   ('How many sides does an octagon have?', ['Five', 'Six', 'Seven', 'Eight'], 3),
   ('What does AM refer to?', ['The morning hours before noon', 'The afternoon hours', 'The evening hours', 'Midnight only'], 0)]),
Sc('Science Review: Our Final Animals and Discoveries',
   'Kindergarten Science strand review, and the final Science lesson of the kindergarten curriculum: students revisit raccoons, skunks, whales, moose, eagles, and earthworms.',
   [('What covers a raccoons eyes like a mask?', ['black fur']),
    ('How does a whale breathe?', ['through a blowhole']),
    ('Where does an earthworm usually live?', ['in soil'])],
   [('What covers a raccoons eyes like a mask?', ['Black fur', 'White feathers', 'Green scales', 'Orange fur'], 0),
    ('How does a skunk defend itself?', ['By spraying a strong-smelling liquid', 'By flying away', 'By biting only', 'By hiding underwater'], 0),
    ('Is a whale a fish or a mammal?', ['A mammal', 'A fish', 'An insect', 'A reptile'], 0),
    ('What shape is an eagles beak?', ['Hooked', 'Flat', 'Straight and thin', 'Round like a ball'], 0),
    ('How many legs does an earthworm have?', ['Zero', 'Two', 'Four', 'Six'], 0)]),
SS('Social Studies Review: Our Final Helpers and Community Learning',
   'Kindergarten Social Studies strand review, and the final Social Studies lesson of the kindergarten curriculum, marking the completion of the full kindergarten program: students revisit zookeepers, mechanics, park rangers, engineers, coaches, and train conductors.',
   [('What is the main job of a zookeeper?', ['feeding and caring for zoo animals']),
    ('What is the main job of an engineer?', ['designing and building things our community needs']),
    ('What is the main job of a train conductor?', ['keeping passengers safe and trains on schedule'])],
   [('What is the main job of a zookeeper?', ['Feeding and caring for zoo animals', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('What is the main job of a mechanic?', ['Fixing and maintaining cars and trucks', 'Cutting hair', 'Teaching school', 'Flying planes'], 0),
    ('What is the main job of a park ranger?', ['Guiding visitors and caring for trails', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0),
    ('What is the main job of an engineer?', ['Designing and building things our community needs', 'Cutting hair', 'Teaching school', 'Flying planes'], 0),
    ('What is the main job of a train conductor?', ['Keeping passengers safe and trains on schedule', 'Cutting hair', 'Fixing pipes', 'Flying planes'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_181_187)
    append_worksheet_days(0, g0_181_187)
