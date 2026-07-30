#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 111-120 -- ninth batch, extending Grade 0
past Day 110 toward the full ~187-day school year. Self-contained script
(does NOT use gen_curriculum.py's sub()/day()/append_to(), since those do
not support a worksheet field) modeled exactly on gen_grade0_days101_110.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by fetch_video_ids.py)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-110 (see
data/grade0.ts / data/grade0.json): new word families (-ub, -og), vowel
teams (ai/ee), r-controlled vowels (ar/or), plural -s, pronouns, position
words in stories, and nursery rhyme patterns for Language; number bonds to
7 and 8, comparing sets, string measurement, oval/diamond shapes, a
yesterday/today/tomorrow calendar, addition/subtraction joining-and-taking
stories, and AAB/ABB patterns for Math; muscles, woodland animals,
puddles/evaporation, owls, penguins, volcanoes, ice as solid water, coral
reefs, and wind power for Science; and airport workers, the coast guard,
seasons around the world, sharing chores, being a leader, the school bus
driver, land acknowledgement, Canada's territories, and kindness to
animals for Social Studies -- none of those exact ideas appear in Days
1-110. Day 120 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch. No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely for kindergarten readability and to keep the generated
.ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260726):
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


g0_111_120 = [
day(111, [
L('Word Families: -ub Words',
  'Kindergarten Language strand: the -ub word family shares the same ending sound, as in cub, rub, tub, and sub.',
  [('Name a word that rhymes with tub.', ['cub', 'rub', 'sub', 'club']),
   ('What ending sound do cub, rub, and tub share?', ['ub', 'the ub sound']),
   ('Is hub part of the -ub family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ub family?', ['Hat', 'Cub', 'Bag', 'Pen'], 1),
   ('Which word rhymes with rub?', ['Rob', 'Rib', 'Tub', 'Rap'], 2),
   ('Which word does NOT belong to the -ub family?', ['Sub', 'Cub', 'Tub', 'Cap'], 3),
   ('Complete the rhyme: The pig sat in the ___.', ['tub', 'top', 'ten', 'toe'], 0),
   ('Word families share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Number Bonds: Ways to Make 7',
  'Kindergarten Math strand: students find different pairs of numbers that combine to make 7, such as 3 and 4, or 5 and 2.',
  [('What two numbers make 7 with 1?', ['6', '1 and 6']),
   ('What two numbers make 7 with 5?', ['2', '5 and 2']),
   ('Show one way to make 7.', ['3 and 4', '0 and 7'])],
  [('3 + ? = 7', ['3', '4', '5', '6'], 1),
   ('Which pair makes 7?', ['2 and 4', '5 and 2', '6 and 2', '1 and 4'], 1),
   ('6 + ? = 7', ['0', '1', '2', '3'], 1),
   ('Which pair does NOT make 7?', ['1 and 6', '3 and 4', '2 and 5', '2 and 6'], 3),
   ('0 + ? = 7', ['6', '7', '8', '5'], 1)]),
Sc('Our Muscles: Helping Us Move',
   'Kindergarten Science strand: muscles are body parts that help us move, such as when we run, jump, wave, and smile.',
   [('Name one thing your muscles help you do.', ['run', 'jump', 'wave', 'smile']),
    ('Where are muscles found in your body?', ['all over', 'everywhere in the body']),
    ('What happens to muscles when you exercise?', ['they get stronger', 'grow stronger'])],
   [('What do muscles help us do?', ['See colours', 'Move our body', 'Hear sounds', 'Smell food'], 1),
    ('Which activity uses your leg muscles?', ['Reading', 'Running', 'Listening', 'Smelling'], 1),
    ('What can make muscles stronger?', ['Sleeping all day', 'Exercise', 'Watching television', 'Sitting still'], 1),
    ('Do your arm muscles help you wave?', ['Yes', 'No', 'Only at night', 'Only in winter'], 0),
    ('Muscles are found ___ your body.', ['Only in your feet', 'All over', 'Only in your face', 'Only in your hands'], 1)]),
SS('Our Airport Workers: Helping People Travel',
   'Kindergarten Social Studies strand: airport workers such as pilots, flight attendants, and baggage handlers help people travel safely by air.',
   [('Name one worker who helps people at an airport.', ['pilot', 'flight attendant', 'baggage handler']),
    ('What does a pilot do?', ['flies the plane', 'flies the airplane']),
    ('Why do airports need many workers?', ['to help people travel safely', 'to keep travel safe'])],
   [('Who flies the airplane?', ['A pilot', 'A chef', 'A teacher', 'A farmer'], 0),
    ('Who helps passengers on the airplane?', ['A flight attendant', 'A doctor', 'A librarian', 'A mail carrier'], 0),
    ('Who carries and loads the suitcases?', ['A baggage handler', 'A dentist', 'A crossing guard', 'A vet'], 0),
    ('An airport is a place where people go to ___.', ['Swim', 'Catch an airplane', 'Buy groceries', 'Play sports'], 1),
    ('Why do we need many different airport workers?', ['To make travel safe and smooth', 'They do not help anyone', 'Only one worker is needed', 'Airports have no workers'], 0)]),
]),
day(112, [
L('Word Families: -og Words',
  'Kindergarten Language strand: the -og word family shares the same ending sound, as in dog, log, fog, and jog.',
  [('Name a word that rhymes with dog.', ['log', 'fog', 'jog']),
   ('What ending sound do dog and log share?', ['og', 'the og sound']),
   ('Is hog part of the -og family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -og family?', ['Dig', 'Log', 'Cat', 'Sun'], 1),
   ('Which word rhymes with fog?', ['Fig', 'Fun', 'Jog', 'Far'], 2),
   ('Which word does NOT belong to the -og family?', ['Dog', 'Fog', 'Jog', 'Jug'], 3),
   ('Complete the rhyme: The frog sat on a ___.', ['log', 'lap', 'lid', 'let'], 0),
   ('Word families help us read new words because they ___.', ['Look the same colour', 'Share a spelling pattern', 'Are always short', 'Have no vowels'], 1)]),
M('Number Bonds: Ways to Make 8',
  'Kindergarten Math strand: students find different pairs of numbers that combine to make 8, such as 3 and 5, or 6 and 2.',
  [('What two numbers make 8 with 1?', ['7', '1 and 7']),
   ('What two numbers make 8 with 4?', ['4', '4 and 4']),
   ('Show one way to make 8.', ['5 and 3', '2 and 6'])],
  [('5 + ? = 8', ['2', '3', '4', '5'], 1),
   ('Which pair makes 8?', ['3 and 4', '6 and 2', '5 and 4', '7 and 2'], 1),
   ('4 + ? = 8', ['2', '3', '4', '5'], 2),
   ('Which pair does NOT make 8?', ['1 and 7', '2 and 6', '3 and 5', '2 and 5'], 3),
   ('0 + ? = 8', ['7', '8', '9', '6'], 1)]),
Sc('Woodland Animals: Squirrels, Deer, and Foxes',
   'Kindergarten Science strand: woodland animals such as squirrels, deer, and foxes live in forests and have features that help them survive there.',
   [('Name one animal that lives in the woods.', ['squirrel', 'deer', 'fox']),
    ('What do squirrels often collect and store?', ['nuts', 'acorns']),
    ('Why do woodland animals have fur?', ['to stay warm', 'keeps them warm'])],
   [('Which animal lives in the forest?', ['Squirrel', 'Shark', 'Camel', 'Whale'], 0),
    ('What do squirrels gather and store for winter?', ['Fish', 'Nuts', 'Seaweed', 'Sand'], 1),
    ('What helps a fox move quietly through the woods?', ['Its soft paws', 'Its loud voice', 'Its bright colour', 'Its size'], 0),
    ('Deer often live in groups called ___.', ['Packs', 'Herds', 'Flocks', 'Schools'], 1),
    ('Why do woodland animals have fur coats?', ['To swim faster', 'To stay warm', 'To fly higher', 'To glow at night'], 1)]),
SS('Our Coast Guard: Helping on the Water',
   'Kindergarten Social Studies strand: the coast guard helps keep people safe on lakes, rivers, and oceans, including rescuing boats in trouble.',
   [('What does the coast guard help with?', ['keeping people safe on water', 'water safety']),
    ('Where does the coast guard work?', ['on the water', 'lakes and oceans']),
    ('Why is water safety important?', ['to keep people safe', 'so no one gets hurt'])],
   [('Where does the coast guard mostly work?', ['In the sky', 'On the water', 'Underground', 'In a classroom'], 1),
    ('What might the coast guard do for a boat in trouble?', ['Ignore it', 'Rescue it', 'Paint it', 'Sell it'], 1),
    ('The coast guard helps keep people safe on ___.', ['Roads', 'Water', 'Playgrounds', 'Farms'], 1),
    ('Which is a job of the coast guard?', ['Teaching school', 'Watching for boats in danger', 'Baking bread', 'Fixing cars'], 1),
    ('Why do communities near water need a coast guard?', ['To help keep people safe there', 'Water needs no safety helpers', 'Only for fun', 'To sell fish'], 0)]),
]),
day(113, [
L('Vowel Teams: ai and ee',
  'Kindergarten Language strand: some long vowel sounds are spelled with two vowels together, called a vowel team, such as ai in rain and ee in bee.',
  [('Name a word with the ai vowel team.', ['rain', 'sail', 'pail']),
   ('Name a word with the ee vowel team.', ['bee', 'see', 'tree']),
   ('What sound does ai usually make?', ['long a', 'the long a sound'])],
  [('Which word has the ai vowel team?', ['Rain', 'Run', 'Red', 'Rib'], 0),
   ('Which word has the ee vowel team?', ['Bed', 'Bee', 'Big', 'Bag'], 1),
   ('What sound does ai make in rain?', ['Short a', 'Long a', 'Long e', 'Short e'], 1),
   ('What sound does ee make in tree?', ['Long e', 'Short e', 'Long a', 'Short i'], 0),
   ('A vowel team is ___.', ['One consonant alone', 'Two vowels working together', 'A silent letter', 'A number'], 1)]),
M('Comparing Sets: Same Number or Different',
  'Kindergarten Math strand: students compare two small groups of objects to decide whether they have the same number or a different number.',
  [('If one group has 4 dots and another has 4 dots, are they the same?', ['yes', 'yes the same']),
   ('If one group has 3 dots and another has 5 dots, are they different?', ['yes', 'yes different']),
   ('How can you check if two groups have the same number?', ['count each group', 'count both']),],
  [('A group of 5 apples and a group of 5 oranges have ___.', ['Different numbers', 'The same number', 'No fruit', 'Too many'], 1),
   ('A group of 3 and a group of 6 have ___.', ['The same number', 'Different numbers', 'Zero', 'One'], 1),
   ('How do we compare two groups?', ['Guess', 'Count each group', 'Ignore them', 'Colour them'], 1),
   ('Which pair has the same number?', ['2 and 5', '4 and 4', '1 and 3', '6 and 2'], 1),
   ('If both groups have 6 objects, they are ___.', ['Equal', 'Unequal', 'Empty', 'Missing'], 0)]),
Sc('Puddles: Where Does Rainwater Go?',
   'Kindergarten Science strand: after it rains, water collects in puddles, then slowly soaks into the ground or evaporates into the air.',
   [('Where does rainwater collect after a storm?', ['in puddles', 'puddles']),
    ('What happens to a puddle after a sunny day?', ['it dries up', 'evaporates']),
    ('Name one place puddle water can go.', ['into the ground', 'into the air'])],
   [('Where does rain often collect on the ground?', ['In puddles', 'In the sky', 'In trees', 'In clouds'], 0),
    ('What can happen to a puddle on a warm sunny day?', ['It grows bigger forever', 'It evaporates and dries up', 'It turns to ice', 'It turns into a river'], 1),
    ('Some puddle water soaks into the ___.', ['Sky', 'Ground', 'Sun', 'Wind'], 1),
    ('What word means water turning into vapour in the air?', ['Evaporation', 'Freezing', 'Melting', 'Sinking'], 0),
    ('Puddles usually form after ___.', ['Rain', 'Sunshine only', 'Wind only', 'Snowmen'], 0)]),
SS('Seasons Around the World: Not Everywhere Has Snow',
   'Kindergarten Social Studies strand: different places around the world have different weather and seasons; some places are always warm and never see snow.',
   [('Do all places in the world get snow?', ['no', 'not all places']),
    ('Name a kind of place that is always warm.', ['a hot country', 'near the equator']),
    ('Why might people dress differently in different countries?', ['different weather', 'the weather is different there'])],
   [('Do all countries have snowy winters?', ['Yes, every country', 'No, some places stay warm', 'Only Canada has weather', 'Snow falls everywhere equally'], 1),
    ('Why might someone in a warm country never see snow?', ['Their weather stays warm all year', 'They do not like snow', 'Snow is not real', 'They have no seasons at all'], 0),
    ('People dress differently around the world mostly because of ___.', ['Their favourite colour', 'Different weather and climates', 'Random choices', 'School rules'], 1),
    ('Which clothing suits a very warm place?', ['A heavy winter coat', 'Light, cool clothing', 'Snow boots', 'Mittens'], 1),
    ('Learning about weather around the world helps us understand ___.', ['That everyone lives the same way', 'That places can be very different', 'That snow falls everywhere', 'Nothing important'], 1)]),
]),
day(114, [
L('R-Controlled Vowels: ar and or',
  'Kindergarten Language strand: when a vowel is followed by the letter r, the vowel sound changes, as in car (ar) and for (or).',
  [('Name a word with the ar sound, like in car.', ['car', 'star', 'far']),
   ('Name a word with the or sound, like in for.', ['for', 'corn', 'fort']),
   ('What letter changes the vowel sound in car?', ['r', 'the letter r'])],
  [('Which word has the ar sound?', ['Car', 'Cat', 'Cap', 'Can'], 0),
   ('Which word has the or sound?', ['For', 'Fun', 'Fin', 'Fan'], 0),
   ('What letter after a vowel often changes its sound?', ['s', 'r', 't', 'm'], 1),
   ('Which word does NOT have the ar sound?', ['Star', 'Far', 'Car', 'Cot'], 3),
   ('In the word corn, which two letters make the or sound?', ['co', 'or', 'rn', 'cn'], 1)]),
M('Measurement: Comparing Length with a String',
  'Kindergarten Math strand: students use a piece of string to measure and compare the length of different objects, such as a book or a table.',
  [('What tool can you use to measure length in this lesson?', ['string', 'a piece of string']),
   ('If a string wraps around the book two times, what does that tell you?', ['the book is that long', 'about its length']),
   ('Name something in your home you could measure with string.', ['a table', 'a book'])],
  [('What can a piece of string help us measure?', ['Sound', 'Length', 'Colour', 'Taste'], 1),
   ('To compare two objects with string, we check which one is ___.', ['Louder', 'Longer or shorter', 'Colder', 'Heavier'], 1),
   ('If a table needs a longer string than a book, the table is ___.', ['Shorter', 'Longer', 'The same size', 'Lighter'], 1),
   ('Why is string a useful measuring tool for young learners?', ['It can bend around objects', 'It tells the time', 'It can weigh things', 'It never breaks'], 0),
   ('Comparing length means finding out which object is ___.', ['Louder', 'Bigger or smaller in size', 'Tastier', 'A different colour'], 1)]),
Sc('Owls: Hunters of the Night',
   'Kindergarten Science strand: owls are birds that are awake at night, have excellent hearing, and can turn their heads to look around.',
   [('When are owls usually awake?', ['at night', 'nighttime']),
    ('What sense helps owls hunt in the dark?', ['hearing', 'good hearing']),
    ('Name one thing owls eat.', ['mice', 'small animals'])],
   [('Owls are mostly active ___.', ['During the day', 'At night', 'Underwater', 'Never'], 1),
    ('What helps owls hunt well in the dark?', ['Bright colours', 'Excellent hearing', 'Loud singing', 'Long tails'], 1),
    ('An animal that is awake mostly at night is called ___.', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0),
    ('Owls can turn their heads to ___.', ['Fly faster', 'Look around without moving their body', 'Change colour', 'Breathe underwater'], 1),
    ('What might an owl eat?', ['Only leaves', 'Small animals like mice', 'Only fruit', 'Rocks'], 1)]),
SS('Sharing Chores: Helping as a Family Team',
   'Kindergarten Social Studies strand: family members share chores, such as cleaning up or setting the table, working together as a team at home.',
   [('Name one chore you can do at home.', ['clean up', 'set the table']),
    ('Why do families share chores?', ['to help each other', 'work as a team']),
    ('How do you feel when you help at home?', ['happy', 'proud'])],
   [('What is a chore?', ['A game', 'A job or task to help at home', 'A snack', 'A holiday'], 1),
    ('Why do families share chores?', ['To make more mess', 'To help each other and work as a team', 'Chores are not helpful', 'Only grown-ups should help'], 1),
    ('Which is an example of a chore?', ['Watching television', 'Setting the table', 'Sleeping', 'Playing outside'], 1),
    ('How might a family feel when everyone helps with chores?', ['Angry', 'Proud and happy', 'Confused', 'Bored'], 1),
    ('Doing chores can teach children to be ___.', ['Lazy', 'Responsible', 'Unkind', 'Careless'], 1)]),
]),
day(115, [
L('Plural Nouns: Adding -s to Show More Than One',
  'Kindergarten Language strand: adding -s to the end of most nouns shows that there is more than one, such as changing cat to cats.',
  [('What do we add to cat to show more than one?', ['s', 'add an s']),
   ('What is the plural of dog?', ['dogs', 'dogs, adding s']),
   ('What is the plural of book?', ['books', 'books with an s'])],
  [('What do we add to most nouns to show more than one?', ['ing', 's', 'ed', 'er'], 1),
   ('What is the plural of cup?', ['Cup', 'Cups', 'Cupp', 'Cupes'], 1),
   ('Which word means more than one bird?', ['Bird', 'Birds', 'Birdy', 'Birding'], 1),
   ('A plural noun means ___.', ['Only one thing', 'More than one thing', 'A colour', 'An action'], 1),
   ('What is the plural of hat?', ['Hates', 'Hat', 'Hats', 'Hatting'], 2)]),
M('2D Shapes: Oval and Diamond',
  'Kindergarten Math strand: students identify and describe two new flat shapes, the oval, which looks like a stretched circle, and the diamond, which has four pointed sides.',
  [('Name a shape that looks like a stretched circle.', ['oval', 'an oval']),
   ('How many points does a diamond have?', ['4', 'four']),
   ('Name something shaped like an oval.', ['an egg', 'a football'])],
  [('Which shape looks like a stretched circle?', ['Square', 'Oval', 'Triangle', 'Rectangle'], 1),
   ('How many points does a diamond shape have?', ['2', '3', '4', '5'], 2),
   ('Which real object is shaped like an oval?', ['A brick', 'An egg', 'A ball', 'A book'], 1),
   ('A diamond shape has four ___.', ['Circles', 'Pointed sides', 'Wheels', 'Colours'], 1),
   ('Which shape has no straight sides?', ['Diamond', 'Square', 'Oval', 'Triangle'], 2)]),
Sc('Penguins: Birds That Cannot Fly',
   'Kindergarten Science strand: penguins are birds with wings shaped like flippers that help them swim, though they cannot fly through the air.',
   [('Can penguins fly?', ['no', 'no they cannot']),
    ('What do penguins use their wings for instead of flying?', ['swimming', 'to swim']),
    ('Where do many penguins live?', ['cold places', 'near icy water'])],
   [('Can penguins fly like most other birds?', ['Yes', 'No', 'Only in summer', 'Only babies fly'], 1),
    ('What are penguin wings shaped like?', ['Flippers', 'Fans', 'Umbrellas', 'Leaves'], 0),
    ('What do penguins use their flipper wings for?', ['Swimming', 'Flying high', 'Digging tunnels', 'Climbing trees'], 0),
    ('Penguins are still classified as ___ even though they cannot fly.', ['Fish', 'Birds', 'Mammals', 'Reptiles'], 1),
    ('Many penguins live in ___ places.', ['Very hot', 'Cold, icy', 'Sandy desert', 'Rainforest'], 1)]),
SS('Being a Leader: Taking Turns to Lead',
   'Kindergarten Social Studies strand: leaders help guide a group, and everyone can practise being a leader by taking turns leading a line or a game.',
   [('What is a leader?', ['someone who guides others', 'a person who leads']),
    ('Name a time you might be a leader at school.', ['leading a line', 'leading a game']),
    ('Why is it good to take turns leading?', ['everyone gets a chance', 'fair for everyone'])],
   [('What does a leader do for a group?', ['Ignores them', 'Guides and helps them', 'Confuses them', 'Leaves them alone'], 1),
    ('Which is an example of leading at school?', ['Leading the line to the gym', 'Ignoring the teacher', 'Sitting alone', 'Refusing to share'], 0),
    ('Why should everyone get a turn to be leader?', ['It is fair and everyone learns', 'Only some people should lead', 'It does not matter', 'Leaders are always the same person'], 0),
    ('A good leader treats classmates with ___.', ['Unkindness', 'Respect', 'Silence', 'Confusion'], 1),
    ('Taking turns leading helps children practise ___.', ['Ignoring others', 'Responsibility', 'Being unfair', 'Hiding'], 1)]),
]),
day(116, [
L('Pronouns: I, You, He, and She',
  'Kindergarten Language strand: pronouns like I, you, he, and she take the place of a persons name in a sentence, such as saying she instead of Maria.',
  [('What pronoun could replace the name Sam if Sam is a boy?', ['he', 'he can']),
   ('What pronoun do you use to talk about yourself?', ['I', 'I do']),
   ('What pronoun could replace Maria if Maria is a girl?', ['she', 'she is'])],
  [('Which word could replace a boys name in a sentence?', ['He', 'She', 'It', 'They'], 0),
   ('Which word could replace a girls name in a sentence?', ['He', 'It', 'She', 'We'], 2),
   ('Which pronoun do you use to talk about yourself?', ['You', 'I', 'He', 'She'], 1),
   ('A pronoun takes the place of a ___.', ['Verb', 'Persons name', 'Number', 'Colour'], 1),
   ('Which sentence uses a pronoun?', ['Maria runs fast.', 'She runs fast.', 'The dog barks.', 'Run fast now.'], 1)]),
M('Time: Yesterday, Today, and Tomorrow',
  'Kindergarten Math strand: students use a simple calendar to talk about yesterday, today, and tomorrow, building an understanding of the passing of time.',
  [('What day comes right before today?', ['yesterday', 'yesterday does']),
   ('What day comes right after today?', ['tomorrow', 'tomorrow does']),
   ('What is the word for the day we are in right now?', ['today', 'today is now'])],
  [('The day right before today is called ___.', ['Tomorrow', 'Yesterday', 'Today', 'Next week'], 1),
   ('The day right after today is called ___.', ['Yesterday', 'Last week', 'Tomorrow', 'Today'], 2),
   ('What word means the current day?', ['Yesterday', 'Today', 'Tomorrow', 'Never'], 1),
   ('If today is Tuesday, what was yesterday?', ['Wednesday', 'Monday', 'Thursday', 'Sunday'], 1),
   ('If today is Tuesday, what is tomorrow?', ['Monday', 'Sunday', 'Wednesday', 'Friday'], 2)]),
Sc('Volcanoes: Mountains That Erupt',
   'Kindergarten Science strand: a volcano is a mountain that can erupt, sending hot melted rock called lava out from deep inside the Earth.',
   [('What comes out of a volcano when it erupts?', ['lava', 'hot melted rock']),
    ('Is a volcano a type of mountain?', ['yes', 'yes it is']),
    ('Where does lava come from?', ['inside the Earth', 'deep underground'])],
   [('What is a volcano?', ['A type of cloud', 'A mountain that can erupt', 'A kind of animal', 'An ocean current'], 1),
    ('What hot melted rock can come out of an erupting volcano?', ['Lava', 'Ice', 'Sand', 'Snow'], 0),
    ('Where does lava come from?', ['Deep inside the Earth', 'The clouds', 'The ocean surface', 'Outer space'], 0),
    ('When a volcano sends out lava, ash, and gas, we say it is ___.', ['Sleeping', 'Erupting', 'Melting', 'Floating'], 1),
    ('A volcano is best described as a kind of ___.', ['River', 'Mountain', 'Lake', 'Cloud'], 1)]),
SS('Our School Bus Driver: Getting Us There Safely',
   'Kindergarten Social Studies strand: the school bus driver is a community helper who drives students safely to and from school every day.',
   [('Who drives the school bus?', ['the bus driver', 'a bus driver']),
    ('What is the bus drivers job?', ['drive us safely', 'take students to school']),
    ('Name one rule for riding the bus safely.', ['stay seated', 'listen to the driver'])],
   [('Who is responsible for driving the school bus?', ['The principal', 'The bus driver', 'A student', 'A parent only'], 1),
    ('What is the main job of a bus driver?', ['Teach lessons', 'Drive students safely', 'Cook lunch', 'Clean classrooms'], 1),
    ('Which is a good bus safety rule?', ['Standing up while the bus moves', 'Staying seated and quiet', 'Yelling loudly', 'Sticking arms out the window'], 1),
    ('Why should students listen to the bus driver?', ['To stay safe on the ride', 'It does not matter', 'Drivers give no instructions', 'Only for fun'], 0),
    ('A bus driver helps the school community by ___.', ['Getting students there safely', 'Grading homework', 'Selling snacks', 'Fixing computers'], 0)]),
]),
day(117, [
L('Position Words in Stories: In, On, and Under',
  'Kindergarten Language strand: authors use position words like in, on, and under to help readers picture exactly where something is happening.',
  [('Give an example of a position word.', ['in', 'on', 'under']),
   ('If a cat is under the table, where is it?', ['under the table', 'below the table']),
   ('Why do stories use position words?', ['to show where things are', 'help us picture the scene'])],
  [('Which of these is a position word?', ['Happy', 'Under', 'Quickly', 'Blue'], 1),
   ('If a ball is on the chair, where is the ball?', ['Inside the chair', 'On top of the chair', 'Under the chair', 'Behind the chair'], 1),
   ('If a shoe is under the bed, where is it?', ['On the bed', 'Beside the bed', 'Below the bed', 'Inside the closet'], 2),
   ('Position words help readers ___.', ['Picture where things are', 'Learn colours', 'Count objects', 'Sing songs'], 0),
   ('Which sentence uses a position word?', ['The dog is happy.', 'The dog is in the box.', 'The dog barks loudly.', 'The dog is brown.'], 1)]),
M('Addition Stories to 10: Joining Two Groups',
  'Kindergarten Math strand: students act out and solve simple addition stories to 10, such as joining a group of 3 toys with a group of 4 toys.',
  [('If you have 3 toys and get 2 more, how many toys do you have?', ['5', 'five']),
   ('If you join a group of 4 and a group of 4, how many is that?', ['8', 'eight']),
   ('What action word tells you to add in a story?', ['join', 'more', 'altogether'])],
  [('You have 4 apples and get 3 more. How many apples now?', ['6', '7', '8', '5'], 1),
   ('A story says 2 birds join 5 birds. How many birds altogether?', ['6', '7', '8', '9'], 1),
   ('Which word in a story often means to add?', ['Take away', 'Altogether', 'Fewer', 'Less'], 1),
   ('You have 5 blocks and get 5 more. How many blocks now?', ['9', '10', '11', '8'], 1),
   ('3 fish join 4 fish in a pond. How many fish are there now?', ['6', '7', '8', '5'], 1)]),
Sc('Ice and Snow: Water Becomes Solid',
   'Kindergarten Science strand: when water gets very cold, it freezes and changes into a solid called ice or snow.',
   [('What does water become when it freezes?', ['ice', 'ice or snow']),
    ('What causes water to freeze?', ['getting very cold', 'cold temperature']),
    ('What happens to ice when it warms up?', ['it melts', 'it turns back to water'])],
   [('What happens to water when it gets very cold?', ['It boils', 'It freezes into ice', 'It disappears', 'It turns green'], 1),
    ('Ice and snow are both examples of water in what state?', ['Liquid', 'Gas', 'Solid', 'Steam'], 2),
    ('What causes liquid water to turn into ice?', ['Very cold temperatures', 'Very hot temperatures', 'Wind', 'Sunlight only'], 0),
    ('What happens when ice warms up?', ['It stays the same', 'It melts back into water', 'It turns into rock', 'It disappears forever'], 1),
    ('Snowflakes are a form of frozen ___.', ['Sand', 'Water', 'Air', 'Soil'], 1)]),
SS('Land Acknowledgement: Honouring Indigenous Land',
   'Kindergarten Social Studies strand: a land acknowledgement is a respectful way of recognizing that Indigenous peoples have cared for the land for a very long time.',
   [('What does a land acknowledgement recognize?', ['Indigenous peoples and the land', 'that Indigenous peoples cared for the land']),
    ('Who has lived on and cared for the land for a very long time?', ['Indigenous peoples', 'First Peoples']),
    ('Why do communities share a land acknowledgement?', ['to show respect', 'to be respectful'])],
   [('What is a land acknowledgement?', ['A song', 'A respectful way to recognize Indigenous peoples and land', 'A type of map', 'A holiday'], 1),
    ('Who has cared for the land for a very long time?', ['Indigenous peoples', 'Only recent visitors', 'No one', 'Only animals'], 0),
    ('Why might a school share a land acknowledgement?', ['To show respect and remembrance', 'It has no meaning', 'To confuse students', 'Just for fun'], 0),
    ('A land acknowledgement is often shared ___.', ['Never', 'At the start of an event or gathering', 'Only in winter', 'Only by animals'], 1),
    ('Learning about Indigenous peoples helps us understand ___.', ['Nothing important', 'Canadas history and the first peoples of the land', 'Only modern cities', 'Only other countries'], 1)]),
]),
day(118, [
L('Story Retelling with a Beginning, Middle, and End Picture',
  'Kindergarten Language strand: students retell a story by drawing or describing what happened at the beginning, the middle, and the end.',
  [('What are the three parts of a story we retell?', ['beginning, middle, end', 'beginning, middle, and end']),
   ('What happens in the beginning of a story?', ['characters and setting are introduced', 'we meet the characters']),
   ('What happens at the end of a story?', ['the problem is solved', 'the ending happens'])],
  [('What are the three parts used to retell a story?', ['Title, author, cover', 'Beginning, middle, end', 'Loud, quiet, silent', 'Big, medium, small'], 1),
   ('What usually happens at the beginning of a story?', ['The problem is solved', 'We meet the characters and setting', 'The story ends', 'Nothing happens'], 1),
   ('What usually happens in the middle of a story?', ['The characters are introduced', 'Something happens or a problem appears', 'The book closes', 'The title is shown'], 1),
   ('What usually happens at the end of a story?', ['The problem is solved', 'The characters are introduced', 'The setting is shown', 'The book begins'], 0),
   ('Retelling a story in order helps us ___.', ['Forget the story', 'Understand and remember it', 'Change the ending', 'Draw a random picture'], 1)]),
M('Subtraction Stories to 10: Taking Away',
  'Kindergarten Math strand: students act out and solve simple subtraction stories to 10, such as taking 2 away from a group of 6.',
  [('If you have 6 cookies and eat 2, how many are left?', ['4', 'four']),
   ('If you have 8 balloons and 3 pop, how many are left?', ['5', 'five']),
   ('What word in a story often means subtract?', ['left', 'take away'])],
  [('You have 7 grapes and eat 3. How many are left?', ['3', '4', '5', '6'], 1),
   ('A story says 9 ducks swim away, leaving 4. How many ducks were there before?', ['12', '13', '14', '11'], 1),
   ('Which word often signals subtraction in a story?', ['Altogether', 'Left', 'More', 'Join'], 1),
   ('You have 10 stickers and give away 4. How many do you have now?', ['5', '6', '7', '8'], 1),
   ('8 birds are on a branch, then 5 fly away. How many birds are left?', ['2', '3', '4', '5'], 1)]),
Sc('Coral Reefs: A Colourful Ocean Home',
   'Kindergarten Science strand: coral reefs are colourful underwater habitats built by tiny living creatures called coral, home to many fish and sea animals.',
   [('What builds a coral reef?', ['coral', 'tiny living creatures']),
    ('What lives in a coral reef?', ['fish and sea animals', 'many sea creatures']),
    ('Are coral reefs found in the ocean?', ['yes', 'yes in the ocean'])],
   [('What builds a coral reef?', ['Fish', 'Tiny living creatures called coral', 'Rocks alone', 'Plants alone'], 1),
    ('Coral reefs are found ___.', ['In deserts', 'Underwater in the ocean', 'In forests', 'On mountains'], 1),
    ('What lives among the colourful coral in a reef?', ['Many fish and sea animals', 'Only birds', 'Only insects', 'Nothing lives there'], 0),
    ('What word describes the many bright colours of a coral reef?', ['Colourful', 'Colourless', 'Grey', 'Dull'], 0),
    ('Why are coral reefs important habitats?', ['They give a home to many sea creatures', 'They are not important', 'They stay empty', 'They only exist on land'], 0)]),
SS('Canadas Territories: The Far North',
   'Kindergarten Social Studies strand: in addition to provinces, Canada has three territories in the far north, which have cold weather and unique communities.',
   [('Does Canada have territories in the far north?', ['yes', 'yes it does']),
    ('Is the far north usually cold?', ['yes', 'yes very cold']),
    ('Name one thing that makes the north unique.', ['very cold weather', 'unique communities'])],
   [('Besides provinces, Canada also has three ___.', ['Oceans', 'Territories', 'Islands only', 'Capitals'], 1),
    ('Canadas territories are located in the ___.', ['Far south', 'Far north', 'Middle of the ocean', 'Far east only'], 1),
    ('What kind of weather is common in Canadas far north?', ['Very hot', 'Very cold', 'Always rainy', 'Always dry desert'], 1),
    ('Why might communities in the north look different from southern cities?', ['The cold climate shapes how people live', 'They are exactly the same', 'The north has no people', 'Weather does not matter'], 0),
    ('Learning about Canadas territories helps us understand ___.', ['Only one part of Canada', 'That Canada is large and varied', 'Nothing new', 'That Canada has no north'], 1)]),
]),
day(119, [
L('Nursery Rhymes: Listening for Rhyme Patterns',
  'Kindergarten Language strand: nursery rhymes like Jack and Jill use repeating rhyme patterns that help young children hear and predict sounds in language.',
  [('Name a nursery rhyme you know.', ['Jack and Jill', 'Humpty Dumpty']),
   ('What do the last words of rhyming lines usually share?', ['the same ending sound', 'similar sounds']),
   ('Why are nursery rhymes good for learning language?', ['they have patterns', 'help us hear sounds'])],
  [('What do rhyming lines in a nursery rhyme usually share?', ['The same first letter', 'The same ending sound', 'The same number of words', 'No pattern at all'], 1),
   ('Which pair of words rhymes, like in a nursery rhyme?', ['Hill and Jill', 'Hill and Hat', 'Hill and Sun', 'Hill and Dog'], 0),
   ('Why are nursery rhymes helpful for young learners?', ['They help children hear and predict sounds', 'They have no purpose', 'They confuse children', 'They teach only numbers'], 0),
   ('A rhyme pattern is when words ___.', ['End with the same sound', 'Start with different letters', 'Have no meaning', 'Are always long'], 0),
   ('Which is an example of a nursery rhyme?', ['A grocery list', 'Jack and Jill', 'A weather report', 'A phone number'], 1)]),
M('Patterns: AAB and ABB Patterns',
  'Kindergarten Math strand: students extend more complex repeating patterns beyond ABAB, including AAB (clap, clap, stomp) and ABB (red, blue, blue).',
  [('In the pattern clap, clap, stomp, clap, clap, stomp, what comes next after another clap, clap?', ['stomp', 'stomp again']),
   ('What pattern name describes red, blue, blue, red, blue, blue?', ['ABB', 'an ABB pattern']),
   ('What pattern name describes clap, clap, stomp?', ['AAB', 'an AAB pattern'])],
  [('In the pattern square, square, circle, square, square, ___, what comes next?', ['Square', 'Circle', 'Triangle', 'Star'], 1),
   ('What do we call the pattern red, red, blue, red, red, blue?', ['ABAB', 'AAB', 'ABB', 'AABB'], 1),
   ('What do we call the pattern yellow, green, green, yellow, green, green?', ['AAB', 'ABAB', 'ABB', 'AABB'], 2),
   ('In an AAB pattern, how many times does the first item repeat before the second?', ['Once', 'Twice', 'Three times', 'Never'], 1),
   ('Which sequence follows an ABB pattern?', ['Cat, dog, dog, cat, dog, dog', 'Cat, dog, cat, dog', 'Cat, cat, dog, cat, cat, dog', 'Cat, dog, bird, cat'], 0)]),
Sc('Wind Power: Using Moving Air',
   'Kindergarten Science strand: moving air, or wind, can be used to do work, such as spinning a pinwheel, sailing a boat, or turning a wind turbine.',
   [('What is wind?', ['moving air', 'air that moves']),
    ('Name one thing wind can spin or move.', ['a pinwheel', 'a kite', 'a sailboat']),
    ('Can wind be used to make electricity?', ['yes', 'yes with turbines'])],
   [('What is wind?', ['Still air', 'Moving air', 'Water', 'Sunlight'], 1),
    ('Which toy can be spun by wind?', ['A pinwheel', 'A book', 'A ball', 'A block'], 0),
    ('What tall machine can use wind to make electricity?', ['A wind turbine', 'A refrigerator', 'A television', 'A bicycle'], 0),
    ('Which of these is powered by wind?', ['A sailboat', 'A submarine', 'A subway train', 'An elevator'], 0),
    ('Wind power is considered a form of ___ energy.', ['Clean, renewable', 'Dangerous', 'Fake', 'Underground'], 0)]),
SS('Kindness to Animals: Caring for Pets and Wildlife',
   'Kindergarten Social Studies strand: showing kindness to animals means treating pets and wild animals gently, giving them food, water, and space to be safe.',
   [('Name one way to be kind to a pet.', ['give it food and water', 'be gentle with it']),
    ('Should we be gentle with wild animals too?', ['yes', 'yes we should']),
    ('Why is kindness to animals important?', ['animals have feelings and needs', 'to keep them safe and happy'])],
   [('Which is a kind way to treat a pet?', ['Ignoring its needs', 'Giving it food, water, and gentle care', 'Yelling at it', 'Leaving it outside all the time'], 1),
    ('How should we act around wild animals?', ['Chase and scare them', 'Give them space and be gentle', 'Try to catch them', 'Throw things at them'], 1),
    ('Why is it important to care for animals kindly?', ['Animals have needs and feelings too', 'Animals do not matter', 'It is not important', 'Only people matter'], 0),
    ('Which is an example of caring for a pet?', ['Forgetting to feed it', 'Giving it fresh water every day', 'Leaving it alone for days', 'Being rough with it'], 1),
    ('Being kind to animals shows that we are ___.', ['Careless', 'Caring and responsible', 'Unkind', 'Confused'], 1)]),
]),
day(120, [
L('Language Review: Vowel Teams, Plurals, and Story Retelling',
  'Kindergarten Language strand review: students revisit word families -ub and -og, vowel teams ai and ee, plural -s, pronouns, and retelling a story with a beginning, middle, and end.',
  [('Give a word from the -ub or -og word family.', ['cub', 'dog', 'log']),
   ('What do we add to a word to show more than one?', ['s', 'add an s']),
   ('What are the three parts we use to retell a story?', ['beginning, middle, end', 'beginning, middle, and end'])],
  [('Which word has the ai vowel team?', ['Rain', 'Run', 'Red', 'Rib'], 0),
   ('What do we add to most nouns to show more than one?', ['ing', 's', 'ed', 'er'], 1),
   ('Which pronoun could replace a boys name?', ['She', 'He', 'It', 'They'], 1),
   ('What are the three parts of retelling a story?', ['Title, author, cover', 'Beginning, middle, end', 'Loud, quiet, silent', 'Big, medium, small'], 1),
   ('Which word belongs to the -ub family?', ['Hat', 'Cub', 'Bag', 'Pen'], 1)]),
M('Math Review: Number Bonds, Shapes, and Patterns',
  'Kindergarten Math strand review: students revisit number bonds to 7 and 8, comparing sets, oval and diamond shapes, addition and subtraction stories, and AAB/ABB patterns.',
  [('Show one way to make 7.', ['3 and 4', '5 and 2']),
   ('How many points does a diamond have?', ['4', 'four']),
   ('What do we call the pattern clap, clap, stomp?', ['AAB', 'an AAB pattern'])],
  [('Which pair makes 8?', ['3 and 4', '6 and 2', '5 and 4', '7 and 2'], 1),
   ('Which shape looks like a stretched circle?', ['Square', 'Oval', 'Triangle', 'Rectangle'], 1),
   ('A group of 5 apples and a group of 5 oranges have ___.', ['Different numbers', 'The same number', 'No fruit', 'Too many'], 1),
   ('You have 6 cookies and eat 2. How many are left?', ['3', '4', '5', '6'], 1),
   ('What do we call the pattern red, blue, blue, red, blue, blue?', ['ABAB', 'AAB', 'ABB', 'AABB'], 2)]),
Sc('Science Review: Bodies, Animals, and Earth',
   'Kindergarten Science strand review: students revisit muscles, woodland animals, puddles and evaporation, owls, penguins, volcanoes, ice, coral reefs, and wind power.',
   [('What do muscles help us do?', ['move', 'help us move']),
    ('What comes out of an erupting volcano?', ['lava', 'hot melted rock']),
    ('Can penguins fly?', ['no', 'no they cannot'])],
   [('What do muscles help us do?', ['See colours', 'Move our body', 'Hear sounds', 'Smell food'], 1),
    ('What happens to water when it gets very cold?', ['It boils', 'It freezes into ice', 'It disappears', 'It turns green'], 1),
    ('What builds a coral reef?', ['Fish', 'Tiny living creatures called coral', 'Rocks alone', 'Plants alone'], 1),
    ('Owls are mostly active ___.', ['During the day', 'At night', 'Underwater', 'Never'], 1),
    ('What is wind?', ['Still air', 'Moving air', 'Water', 'Sunlight'], 1)]),
SS('Social Studies Review: Helpers, Kindness, and Our Country',
   'Kindergarten Social Studies strand review: students revisit airport workers, the coast guard, sharing chores, being a leader, the bus driver, land acknowledgement, Canadas territories, and kindness to animals.',
   [('Name one worker who helps at an airport.', ['pilot', 'flight attendant']),
    ('Why do families share chores?', ['to help each other', 'work as a team']),
    ('Why should we be kind to animals?', ['they have needs and feelings', 'to keep them safe'])],
   [('Who flies the airplane?', ['A pilot', 'A chef', 'A teacher', 'A farmer'], 0),
    ('What is the main job of a bus driver?', ['Teach lessons', 'Drive students safely', 'Cook lunch', 'Clean classrooms'], 1),
    ('Besides provinces, Canada also has three ___.', ['Oceans', 'Territories', 'Islands only', 'Capitals'], 1),
    ('Why do families share chores?', ['To make more mess', 'To help each other and work as a team', 'Chores are not helpful', 'Only grown-ups should help'], 1),
    ('Which is a kind way to treat a pet?', ['Ignoring its needs', 'Giving it food, water, and gentle care', 'Yelling at it', 'Leaving it outside all the time'], 1)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_111_120)
    append_worksheet_days(0, g0_111_120)
