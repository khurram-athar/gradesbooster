#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 31-40 -- first batch extending Grade 0 past
the original 30-day program. This is a self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to() helpers, since those do not
support a worksheet field) modeled on the Grade 3-12 Days 31-40/41-50
generators, but adapted to the ACTUAL current data/grade0.ts conventions:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-30 topics (see data/grade0.ts), including filling the pre-existing
Letter N / Letter O gap in Language. No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions are avoided entirely for kindergarten
readability and to keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260820):
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


# ─── DAY 31 ─────────────────────────────────────────────────────────────────
d31_lang = sub('Language', 'Letter N',
  'Explore uppercase and lowercase N. Students identify the letter, practise its sound, and find words beginning with N such as nest, nut, and net.',
  [('Write the missing letter: _est (a home for a bird)', ['n']),
   ('Write the missing letter: _ut (a small hard food from a tree)', ['n']),
   ('What letter comes right after M?', ['n'])],
  [('Which word starts with the same sound as nest?', ['Sun', 'Net', 'Cat', 'Dog'], 1),
   ('Which letter comes after M in the alphabet?', ['L', 'N', 'O', 'P'], 1),
   ('How many humps does lowercase n have?', ['0', '1', '2', '3'], 1),
   ('Which N word is a small hard food that grows on trees?', ['Nest', 'Net', 'Nut', 'Nose'], 2),
   ('In sun, nut, dog, cat, which word starts with N?', ['dog', 'cat', 'sun', 'nut'], 3)])

d31_math = sub('Math', 'Comparing Numbers: More, Less, or Equal',
  'Students compare two groups of objects and use the words more, less, and equal to describe which group has a greater, smaller, or the same amount.',
  [('Which is more: 3 or 8? Write the bigger number.', ['8', 'eight']),
   ('Which is less: 5 or 2? Write the smaller number.', ['2', 'two']),
   ('If both groups have 4 objects, are they equal or not equal?', ['equal'])],
  [('Which group has more: 3 apples or 5 apples?', ['3 apples', '5 apples', 'They are equal', 'Cannot tell'], 1),
   ('If you have 4 balls and your friend has 4 balls, the amounts are ___.', ['More', 'Less', 'Equal', 'Unknown'], 2),
   ('Which number is less: 2 or 7?', ['7', '2', 'They are equal', 'Cannot tell'], 1),
   ('Count: 6 stars or 4 stars, which group has less?', ['6 stars', '4 stars', 'Equal', 'Cannot tell'], 1),
   ('If two groups have the exact same amount, they are ___.', ['More than', 'Less than', 'Equal', 'Plus'], 2)])

d31_sci = sub('Science', 'Five Senses: Seeing and Hearing',
  'Students learn that eyes let us see and ears let us hear. They explore how these two senses help us learn about the world around us.',
  [('Which body part do you use to see a rainbow?', ['eyes', 'eye']),
   ('Which body part do you use to hear music?', ['ears', 'ear']),
   ('Name one sense that eyes give you.', ['sight', 'seeing', 'vision'])],
  [('Which body part do we use to see?', ['Ears', 'Eyes', 'Nose', 'Tongue'], 1),
   ('Which body part do we use to hear?', ['Eyes', 'Ears', 'Hands', 'Feet'], 1),
   ('A loud sound is heard with your ___.', ['Eyes', 'Nose', 'Ears', 'Tongue'], 2),
   ('Which sense tells you a ball is red?', ['Hearing', 'Seeing', 'Smelling', 'Tasting'], 1),
   ('We have how many eyes and how many ears?', ['One eye, one ear', 'Two eyes, two ears', 'Three eyes, three ears', 'Two eyes, one ear'], 1)])

d31_ss = sub('SocialStudies', 'Getting Around: Types of Transportation',
  'Students explore different ways people travel, including cars, buses, bikes, trains, and airplanes, and talk about how they get to school or around their community.',
  [('Which vehicle flies in the sky?', ['airplane', 'plane']),
   ('Which vehicle has two wheels and no motor, pedalled by a rider?', ['bicycle', 'bike']),
   ('Name one way you can travel to school.', ['bus', 'car', 'walk', 'walking', 'bike', 'bicycle', 'train'])],
  [('Which vehicle travels on train tracks?', ['Car', 'Airplane', 'Train', 'Bicycle'], 2),
   ('Which vehicle can fly in the sky?', ['Bus', 'Airplane', 'Bicycle', 'Boat'], 1),
   ('Which of these has two wheels and is pedalled?', ['Bicycle', 'Car', 'Bus', 'Train'], 0),
   ('A bus is used to carry ___.', ['Only one person', 'Many people at once', 'Only pets', 'Only food'], 1),
   ('Which vehicle travels on water?', ['Boat', 'Car', 'Bicycle', 'Bus'], 0)])

# ─── DAY 32 ─────────────────────────────────────────────────────────────────
d32_lang = sub('Language', 'Letter O',
  'Explore uppercase and lowercase O. Students identify the letter, practise its short /o/ sound, and find words beginning with O such as octopus, orange, and ostrich.',
  [('Write the missing letter: _range (an orange fruit)', ['o']),
   ('Write the missing letter: _ctopus (has eight arms)', ['o']),
   ('What letter comes right after N?', ['o'])],
  [('Which word starts with the same sound as octopus?', ['Cat', 'Orange', 'Sun', 'Dog'], 1),
   ('What shape does the letter O look like?', ['A square', 'A circle', 'A triangle', 'A line'], 1),
   ('Which O word is a fruit?', ['Owl', 'Orange', 'Ostrich', 'Otter'], 1),
   ('Which letter comes right after N?', ['M', 'P', 'O', 'Q'], 2),
   ('In dog, otter, cat, sun, which word starts with O?', ['dog', 'cat', 'sun', 'otter'], 3)])

d32_math = sub('Math', 'Making 10: Number Bonds',
  'Students explore pairs of numbers that combine to make 10, such as 6 and 4 or 7 and 3, building a strong foundation for addition.',
  [('6 and ___ make 10. Write the missing number.', ['4', 'four']),
   ('8 and ___ make 10. Write the missing number.', ['2', 'two']),
   ('Write two numbers that add up to make 10.', ['5 and 5', '4 and 6', '3 and 7', '2 and 8', '1 and 9', '6 and 4', '7 and 3', '8 and 2', '9 and 1'])],
  [('6 and ___ make 10.', ['3', '4', '5', '6'], 1),
   ('Which pair of numbers makes 10?', ['2 and 5', '7 and 3', '4 and 4', '9 and 2'], 1),
   ('10 is made of 8 and ___.', ['1', '2', '3', '4'], 1),
   ('Which pair does NOT make 10?', ['5 and 5', '6 and 4', '9 and 1', '8 and 3'], 3),
   ('9 and 1 make ___.', ['9', '10', '11', '8'], 1)])

d32_sci = sub('Science', 'Five Senses: Smelling, Tasting, and Touching',
  'Students learn that the nose helps us smell, the tongue helps us taste, and skin helps us feel or touch. They explore how these senses give us information about our world.',
  [('Which body part helps you smell cookies baking?', ['nose']),
   ('Which body part helps you taste food?', ['tongue']),
   ('Which body part covers your whole body and helps you feel things?', ['skin'])],
  [('Which body part helps you smell a flower?', ['Ears', 'Nose', 'Eyes', 'Hands'], 1),
   ('Which body part helps you taste ice cream?', ['Tongue', 'Nose', 'Ears', 'Eyes'], 0),
   ('Which body part helps you feel if something is soft?', ['Skin', 'Nose', 'Tongue', 'Ears'], 0),
   ('A lemon tastes ___.', ['Sweet', 'Sour', 'Salty', 'Spicy'], 1),
   ('Which sense helps you know a blanket is warm?', ['Touch', 'Sight', 'Hearing', 'Smell'], 0)])

d32_ss = sub('SocialStudies', 'Reading Simple Maps',
  'Students look at simple picture maps of a classroom or park and learn that a map shows where things are located, using pictures and symbols.',
  [('What does a map help you find?', ['places', 'location', 'where things are', 'the way']),
   ('A small picture used on a map is called a ___.', ['symbol']),
   ('Name one place a map could show, like a park or a school.', ['park', 'school', 'playground', 'classroom', 'library', 'store'])],
  [('A map is a drawing that shows ___.', ['A made-up story', 'Where places and things are', 'A list of numbers', 'A song'], 1),
   ('On a simple classroom map, a picture of a desk shows where the ___ is.', ['Window', 'Desk', 'Door', 'Playground'], 1),
   ('Maps often use small pictures instead of words. These are called ___.', ['Symbols', 'Sentences', 'Songs', 'Colours'], 0),
   ('Why are maps useful?', ['They help us find our way to places', 'They are only for decoration', 'They tell jokes', 'They are only for adults'], 0),
   ('Which of these could be shown on a park map?', ['A playground and a pond', 'A math test', 'A birthday song', 'A telephone number'], 0)])

# ─── DAY 33 ─────────────────────────────────────────────────────────────────
d33_lang = sub('Language', 'Beginning Sounds: Listening for First Sounds',
  'Students listen carefully to the first sound in a word and match words that begin with the same sound, building phonemic awareness.',
  [('What is the first sound in the word map?', ['m', 'mmm']),
   ('Which word begins with the same sound as sun: bat or sock?', ['sock']),
   ('What is the first sound in the word run?', ['r'])],
  [('Which two words begin with the same sound: sun, sock, dog?', ['sun and dog', 'sock and dog', 'sun and sock', 'dog only'], 2),
   ('What is the first sound in ball?', ['/s/', '/b/', '/t/', '/m/'], 1),
   ('Which word begins with the same sound as fish?', ['Fan', 'Cat', 'Log', 'Sun'], 0),
   ('Which word does NOT begin with the same sound as top, tap, and ten?', ['Top', 'Tap', 'Ten', 'Ball'], 3),
   ('Listening for beginning sounds helps us with ___.', ['Cooking', 'Reading and spelling', 'Jumping', 'Swimming'], 1)])

d33_math = sub('Math', 'Position Words: Near, Far, Between, and Beside',
  'Students use positional language such as near, far, between, and beside to describe where objects are located in relation to each other.',
  [('If a toy is right next to you, is it near or far?', ['near']),
   ('If a book sits in the middle of two other books, where is it?', ['between', 'in between']),
   ('Write a word that means the opposite of near.', ['far'])],
  [('If the cat is next to the box, the cat is ___ the box.', ['Far from', 'Beside', 'Under', 'Inside'], 1),
   ('If the school is many kilometres away, it is ___ your house.', ['Near', 'Beside', 'Far from', 'On top of'], 2),
   ('If the ball sits in the middle of two chairs, it is ___ the chairs.', ['Beside', 'Between', 'Far from', 'Under'], 1),
   ('If your friend sits right next to you, they are ___ you.', ['Near or beside', 'Far from', 'Under', 'Above'], 0),
   ('Which word describes something that is close by?', ['Far', 'Near', 'Between', 'Above'], 1)])

d33_sci = sub('Science', 'Life Cycle of a Butterfly',
  'Students learn the four stages of a butterfly life cycle: egg, caterpillar, chrysalis, and butterfly.',
  [('What comes first in a butterfly life cycle: egg or caterpillar?', ['egg']),
   ('What does a caterpillar turn into before becoming a butterfly?', ['chrysalis']),
   ('What is the last stage of the butterfly life cycle?', ['butterfly'])],
  [('What is the first stage of a butterfly life cycle?', ['Caterpillar', 'Egg', 'Chrysalis', 'Butterfly'], 1),
   ('What hatches from a butterfly egg?', ['Butterfly', 'Caterpillar', 'Chrysalis', 'Cocoon'], 1),
   ('During which stage does the caterpillar change inside a hard case?', ['Egg', 'Caterpillar', 'Chrysalis', 'Adult'], 2),
   ('What is the last stage of the butterfly life cycle?', ['Egg', 'Caterpillar', 'Chrysalis', 'Butterfly'], 3),
   ('A caterpillar spends most of its time ___.', ['Flying', 'Eating leaves', 'Sleeping underground', 'Swimming'], 1)])

d33_ss = sub('SocialStudies', 'Then and Now: How Things Change',
  'Students compare how things like toys, clothing, and transportation looked long ago and how they look today, building an early sense of time and change.',
  [('Name one way people travelled long ago before cars.', ['horse', 'walking', 'wagon', 'horse and wagon']),
   ('Is a wooden toy from long ago or from today more likely to be electronic?', ['today']),
   ('Write one thing that has changed over time, like transportation or toys.', ['transportation', 'toys', 'clothing', 'communication', 'technology'])],
  [('Long ago, people often travelled by horse and wagon. Today, many people travel by ___.', ['Horse only', 'Car', 'Walking only', 'Nothing changed'], 1),
   ('Which of these is an old way to send a message, before phones?', ['Texting', 'A letter carried by hand or mail', 'Video call', 'Email'], 1),
   ('Comparing then and now helps us understand ___.', ['That nothing ever changes', 'How life has changed over time', 'Only future events', 'Only today'], 1),
   ('Long ago, many people washed clothes ___.', ['With a washing machine', 'By hand', 'With a dryer only', 'They never washed clothes'], 1),
   ('Which is true about toys long ago compared to today?', ['They were exactly the same', 'Some were simpler, like wooden toys', 'There were no toys at all', 'They were all electronic'], 1)])

# ─── DAY 34 ─────────────────────────────────────────────────────────────────
d34_lang = sub('Language', 'Ending Sounds: Listening for Last Sounds',
  'Students listen carefully to the last sound in a word and identify words that end with the same sound, building phonemic awareness.',
  [('What is the last sound in the word bed?', ['d']),
   ('Which word ends with the same sound as sun: fun or cat?', ['fun']),
   ('What is the last sound in the word map?', ['p'])],
  [('What is the last sound in the word cat?', ['/c/', '/a/', '/t/', '/k/'], 2),
   ('Which word ends with the same sound as sun?', ['Sit', 'Run', 'Cap', 'Dog'], 1),
   ('Which word does NOT end with the same sound as hop, top, and mop?', ['Hop', 'Top', 'Mop', 'Sun'], 3),
   ('What is the last sound in the word dog?', ['/d/', '/o/', '/g/', '/n/'], 2),
   ('Listening for ending sounds helps us with ___.', ['Jumping rope', 'Spelling and reading', 'Painting', 'Counting'], 1)])

d34_math = sub('Math', 'Telling Time: Day and Night',
  'Students learn to tell the difference between day and night activities and begin to recognize a clock as a tool that shows time.',
  [('Do we usually sleep during the day or at night?', ['night']),
   ('What tool tells us the time?', ['clock']),
   ('Name one thing you do during the daytime, like going to school.', ['school', 'play', 'eat breakfast', 'learn', 'go to school'])],
  [('Which activity usually happens at night?', ['Eating breakfast', 'Sleeping in bed', 'Going to school', 'Playing at recess'], 1),
   ('The sun is in the sky during ___.', ['Night', 'Day', 'Neither', 'Both equally at all times'], 1),
   ('What tool do we use to tell the time?', ['A ruler', 'A clock', 'A scale', 'A map'], 1),
   ('Which of these happens during the day?', ['Stars come out', 'We go to school', 'We always sleep', 'The moon is brightest'], 1),
   ('At night, the sky is usually ___.', ['Bright and sunny', 'Dark, with the moon and stars', 'Rainy always', 'Always orange'], 1)])

d34_sci = sub('Science', 'Life Cycle of a Frog',
  'Students learn the stages of a frog life cycle: egg, tadpole, froglet, and adult frog.',
  [('What comes out of a frog egg?', ['tadpole']),
   ('Where does a tadpole live?', ['water', 'in water', 'pond']),
   ('What is the last stage of a frog life cycle?', ['adult frog', 'frog'])],
  [('What is the first stage of a frog life cycle?', ['Tadpole', 'Egg', 'Froglet', 'Adult frog'], 1),
   ('What hatches from a frog egg?', ['Adult frog', 'Tadpole', 'Froglet', 'Fish'], 1),
   ('A tadpole lives mostly ___.', ['On land', 'In water', 'In the air', 'Underground'], 1),
   ('As a tadpole grows legs and loses its tail, it becomes a ___.', ['Egg', 'Froglet', 'Fish', 'Bird'], 1),
   ('Where do adult frogs usually live?', ['Only underwater', 'Both in water and on land', 'Only in trees', 'Only in the desert'], 1)])

d34_ss = sub('SocialStudies', 'Rules Keep Us Safe: Traffic Safety',
  'Students learn simple traffic safety rules, such as looking both ways before crossing, holding an adult hand, and stopping at a red light.',
  [('What colour traffic light means stop?', ['red']),
   ('What should you do before crossing the street?', ['look both ways', 'look both ways first']),
   ('What colour traffic light means go?', ['green'])],
  [('Before crossing the street, you should ___.', ['Run across quickly', 'Look both ways', 'Close your eyes', 'Ignore traffic lights'], 1),
   ('A red traffic light means ___.', ['Go', 'Stop', 'Slow down only', 'Turn only'], 1),
   ('A green traffic light means ___.', ['Stop', 'Go', 'Wait', 'Turn around'], 1),
   ('When crossing the street, young children should ___.', ['Cross alone', 'Hold an adult hand', 'Run ahead', 'Look at their shoes'], 1),
   ('Why do we follow traffic safety rules?', ['To have fun only', 'To stay safe near cars and streets', 'Rules do not matter', 'To slow down cars for no reason'], 1)])

# ─── DAY 35 ─────────────────────────────────────────────────────────────────
d35_lang = sub('Language', 'Syllables: Clapping Words Apart',
  'Students clap out the syllables, or beats, in words to build awareness that words are made of smaller sound parts.',
  [('How many syllables (claps) are in the word sun?', ['1', 'one']),
   ('How many syllables are in the word rabbit?', ['2', 'two']),
   ('How many syllables are in the word banana?', ['3', 'three'])],
  [('How many syllables (claps) are in the word cat?', ['1', '2', '3', '4'], 0),
   ('How many syllables are in the word apple?', ['1', '2', '3', '4'], 1),
   ('How many syllables are in the word butterfly?', ['1', '2', '3', '4'], 2),
   ('Clapping out a word into parts helps us ___.', ['Sing songs', 'Break words into smaller sound parts', 'Draw pictures', 'Count numbers'], 1),
   ('How many syllables are in the word dog?', ['1', '2', '3', '4'], 0)])

d35_math = sub('Math', 'Tally Marks: Counting in Groups of Five',
  'Students learn to make and read tally marks, grouping marks into fives with a diagonal line, to count and organize information.',
  [('How many single tally marks make one group before you draw the diagonal line?', ['5', 'five']),
   ('If you have one full group of tally marks, how many does that show?', ['5', 'five']),
   ('Tally marks are used to help us do what to objects?', ['count'])],
  [('A group of 5 tally marks is usually shown with ___.', ['Four straight lines and one diagonal line across them', 'Five separate dots', 'One long line', 'Five circles'], 0),
   ('How many tally marks make one full group?', ['3', '4', '5', '6'], 2),
   ('If you have 2 full groups of tally marks, how many is that?', ['5', '8', '10', '12'], 2),
   ('Tally marks help us ___ things easily.', ['Draw', 'Count', 'Colour', 'Sing about'], 1),
   ('Four lines plus one diagonal line across them shows how many tally marks?', ['4', '5', '6', '10'], 1)])

d35_sci = sub('Science', 'Healthy Habits: Food and Exercise',
  'Students learn that eating healthy foods, drinking water, staying active, and getting enough sleep help keep our bodies healthy and strong.',
  [('Name one healthy food, like a fruit or vegetable.', ['apple', 'banana', 'carrot', 'fruit', 'vegetable', 'broccoli']),
   ('What should we drink to stay healthy?', ['water']),
   ('Name one way to exercise, like running or jumping.', ['running', 'jumping', 'playing', 'walking', 'dancing'])],
  [('Which food is a healthy choice?', ['Candy only', 'An apple', 'Chips only', 'Soda'], 1),
   ('Why is exercise good for our bodies?', ['It makes us tired forever', 'It keeps our bodies strong and healthy', 'It has no benefit', 'It only helps our hair'], 1),
   ('What should we drink most often to stay healthy?', ['Soda', 'Water', 'Juice only', 'Nothing'], 1),
   ('Why do our bodies need sleep?', ['Sleep is not needed', 'To rest and grow', 'To make us hungry', 'To make us sick'], 1),
   ('Which is an example of exercise?', ['Watching television all day', 'Running and jumping', 'Sitting quietly all day', 'Sleeping all day'], 1)])

d35_ss = sub('SocialStudies', 'Where Our Food Comes From',
  'Students learn that much of our food comes from farms, where farmers grow plants and raise animals, before it reaches grocery stores and our tables.',
  [('Who grows the fruits and vegetables we eat?', ['farmer', 'farmers']),
   ('Name one place food travels to after leaving a farm.', ['grocery store', 'store', 'market']),
   ('Name one food that comes from an animal, like milk or eggs.', ['milk', 'eggs', 'cheese', 'meat'])],
  [('Where do many fruits and vegetables come from?', ['A toy store', 'A farm', 'A library', 'A pool'], 1),
   ('Who grows crops and raises animals for food?', ['A teacher', 'A farmer', 'A doctor', 'A pilot'], 1),
   ('Before food reaches our table, it often travels from a farm to a ___.', ['Grocery store', 'Movie theatre', 'Playground', 'Museum'], 0),
   ('Which of these comes from an animal?', ['An apple', 'Milk', 'A carrot', 'Bread from wheat only'], 1),
   ('Why is it important to know where food comes from?', ['It is not important', 'It helps us understand and appreciate our food', 'Only farmers need to know', 'It has no purpose'], 1)])

# ─── DAY 36 ─────────────────────────────────────────────────────────────────
d36_lang = sub('Language', 'Opposites: Words That Mean the Opposite',
  'Students explore opposite word pairs such as big and small, hot and cold, and up and down to build vocabulary and understanding of contrast.',
  [('What is the opposite of day?', ['night']),
   ('What is the opposite of open?', ['closed', 'shut']),
   ('What is the opposite of full?', ['empty'])],
  [('What is the opposite of big?', ['Tall', 'Small', 'Round', 'Fast'], 1),
   ('What is the opposite of hot?', ['Warm', 'Cold', 'Sunny', 'Wet'], 1),
   ('What is the opposite of up?', ['Down', 'Sideways', 'Over', 'Near'], 0),
   ('What is the opposite of happy?', ['Glad', 'Sad', 'Excited', 'Silly'], 1),
   ('What is the opposite of fast?', ['Quick', 'Slow', 'Loud', 'Bright'], 1)])

d36_math = sub('Math', 'Symmetry: Matching Halves',
  'Students explore symmetry by folding shapes and pictures in half to see when both sides match exactly, like a butterfly or a heart.',
  [('If you fold a symmetrical shape in half, do both sides match or not match?', ['match']),
   ('Name one object that looks symmetrical, like a butterfly or a heart.', ['butterfly', 'heart']),
   ('What do we call the line where you fold a shape to check for symmetry?', ['line of symmetry', 'fold line'])],
  [('A shape is symmetrical when ___.', ['It has no shape', 'Both halves match exactly when folded', 'It is always red', 'It has many corners'], 1),
   ('Which of these shapes is symmetrical?', ['A heart', 'A random splash of paint', 'A scribble', 'An uneven blob'], 0),
   ('If you fold a symmetrical picture in half, both sides ___.', ['Look completely different', 'Match exactly', 'Disappear', 'Turn a new colour'], 1),
   ('Which everyday object often looks symmetrical?', ['A butterfly', 'A messy scribble', 'A cloud', 'A puddle'], 0),
   ('The line where you fold a shape to check symmetry is called the ___.', ['Line of symmetry', 'Number line', 'Finish line', 'Colour line'], 0)])

d36_sci = sub('Science', 'Reduce, Reuse, Recycle',
  'Students learn three simple ways to help the environment: reduce how much we use, reuse items instead of throwing them away, and recycle materials like paper and plastic.',
  [('What word means to use an item again instead of throwing it away?', ['reuse']),
   ('What word means turning used materials into new items?', ['recycle']),
   ('Name one material that can often be recycled.', ['paper', 'plastic', 'glass', 'cardboard'])],
  [('What does it mean to reduce?', ['Use more than you need', 'Use less of something', 'Throw everything away', 'Never use anything'], 1),
   ('What does it mean to reuse an item?', ['Throw it away right away', 'Use it again instead of throwing it out', 'Recycle it immediately', 'Never touch it again'], 1),
   ('What does it mean to recycle?', ['Turn used materials into new items', 'Throw everything in the garbage', 'Burn all materials', 'Bury everything in the ground'], 0),
   ('Which of these can often be recycled?', ['Paper and plastic bottles', 'Food waste only', 'Nothing can be recycled', 'Only glass'], 0),
   ('Why is it helpful to reduce, reuse, and recycle?', ['It helps protect our environment and reduces waste', 'It has no benefit', 'It makes more garbage', 'It hurts the environment'], 0)])

d36_ss = sub('SocialStudies', 'Taking Care of Our Belongings',
  'Students learn the importance of taking care of their toys, books, and clothing by keeping them clean, putting them away, and treating them gently.',
  [('What should you do with toys after you finish playing?', ['put them away', 'clean up']),
   ('Name one way to take care of a book.', ['turn pages gently', 'keep it clean', 'do not rip it']),
   ('Taking care of your things shows that you are being ___.', ['responsible'])],
  [('Why should we take care of our belongings?', ['So they last longer and stay useful', 'It does not matter', 'So we can throw them away sooner', 'Only adults need to care for things'], 0),
   ('Which is a good way to take care of a book?', ['Rip the pages', 'Turn pages gently and keep it clean', 'Throw it in mud', 'Leave it outside in the rain'], 1),
   ('After playing with toys, what should you do?', ['Leave them everywhere', 'Put them away neatly', 'Break them', 'Give them away without asking'], 1),
   ('Taking care of your belongings shows ___.', ['Carelessness', 'Responsibility', 'Laziness', 'Nothing important'], 1),
   ('Which is an example of NOT taking care of belongings?', ['Putting clothes away neatly', 'Throwing toys and stepping on them', 'Washing your hands', 'Cleaning your desk'], 1)])

# ─── DAY 37 ─────────────────────────────────────────────────────────────────
d37_lang = sub('Language', 'Story Elements: Beginning, Middle, End',
  'Students learn that stories have a beginning that introduces characters, a middle with a problem or event, and an end that solves the problem.',
  [('What part of the story introduces the characters?', ['beginning']),
   ('What part of the story has the problem?', ['middle']),
   ('What part of the story solves the problem?', ['end'])],
  [('What happens at the beginning of a story?', ['The story ends', 'Characters and setting are introduced', 'Nothing happens', 'The problem is solved'], 1),
   ('What usually happens in the middle of a story?', ['The story starts', 'A problem or event happens', 'The book closes', 'Credits roll'], 1),
   ('What happens at the end of a story?', ['Characters are introduced', 'The problem is solved', 'The story just starts', 'Nothing at all'], 1),
   ('Characters in a story are ___.', ['The people or animals in the story', 'The title only', 'The pictures only', 'The page numbers'], 0),
   ('Why do stories have a beginning, middle, and end?', ['To confuse readers', 'To help the story make sense in order', 'It is not necessary', 'Only for long books'], 1)])

d37_math = sub('Math', 'Numbers to 30',
  'Students count, read, and recognize numbers from 20 to 30, extending their counting skills beyond 20.',
  [('What number comes right after 27?', ['28']),
   ('What number comes right before 30?', ['29']),
   ('Write the number that comes between 24 and 26.', ['25'])],
  [('What number comes after 24?', ['23', '25', '26', '20'], 1),
   ('What number comes before 30?', ['31', '28', '29', '27'], 2),
   ('Count: 26, 27, 28, ___.', ['29', '30', '25', '31'], 0),
   ('Which number is between 21 and 23?', ['20', '22', '24', '25'], 1),
   ('What number comes right after 29?', ['28', '30', '31', '20'], 1)])

d37_sci = sub('Science', 'Simple Machines: Ramps and Wheels',
  'Students explore two simple machines, ramps and wheels, and how they make moving objects easier.',
  [('Name one object that uses wheels to move, like a car or bike.', ['car', 'bike', 'bicycle', 'wagon']),
   ('What simple machine is shaped like a slide and helps move things up or down?', ['ramp']),
   ('Do wheels make it easier or harder to move objects?', ['easier'])],
  [('What does a ramp help us do?', ['Move things up or down more easily', 'Make loud noises', 'Cook food', 'Grow plants'], 0),
   ('What do wheels help with?', ['Making objects move more easily', 'Making objects heavier', 'Making objects colourful', 'Stopping all movement'], 0),
   ('Which of these is an example of a ramp?', ['A slide', 'A ball', 'A blanket', 'A spoon'], 0),
   ('Why do cars and bikes have wheels?', ['To look nice', 'To help them move smoothly', 'To make them heavier', 'To make noise'], 1),
   ('A ramp is a simple machine shaped like a ___.', ['Circle', 'Slanted surface', 'Cube', 'Star'], 1)])

d37_ss = sub('SocialStudies', 'Keeping Our Community Clean',
  'Students learn simple ways to help keep their community clean, such as putting garbage in the bin, picking up litter, and taking care of parks.',
  [('Where should you put your garbage?', ['garbage bin', 'bin', 'trash can']),
   ('What word means garbage left on the ground instead of in a bin?', ['litter']),
   ('Name one way to help keep a park clean.', ['pick up litter', 'use the garbage bin', 'do not litter'])],
  [('Where should garbage go?', ['On the ground', 'In a garbage bin', 'In the park grass', 'Anywhere'], 1),
   ('Litter is ___.', ['Garbage left on the ground instead of in a bin', 'A type of flower', 'A community helper', 'A type of food'], 0),
   ('Why is it important to keep our community clean?', ['It does not matter', 'It keeps places healthy, safe, and nice for everyone', 'It makes more work for no reason', 'Only workers should care'], 1),
   ('Which is a good way to help keep a park clean?', ['Leaving trash behind', 'Picking up litter and using bins', 'Breaking plants', 'Ignoring the mess'], 1),
   ('Everyone in a community can help keep it clean by ___.', ['Doing nothing', 'Throwing garbage properly and picking up litter', 'Only blaming others', 'Leaving it to one person'], 1)])

# ─── DAY 38 ─────────────────────────────────────────────────────────────────
d38_lang = sub('Language', 'Writing: My Name',
  'Students practise writing their own first name correctly, starting with a capital letter, as an important early writing and identity skill.',
  [('Should your name start with a capital letter or a lowercase letter?', ['capital letter', 'capital']),
   ('Write your first name using a capital letter at the start.', ['name', 'yes']),
   ('Name one place at school where you might write your name.', ['worksheet', 'cubby', 'paper', 'desk'])],
  [('A name should always start with a ___.', ['Lowercase letter', 'Capital letter', 'Number', 'Symbol'], 1),
   ('Why is it important to learn to write your own name?', ['It is not important', 'It helps you recognize and label your own things', 'Only teachers need names', 'Names are only spoken, never written'], 1),
   ('If your name is Sam, how should you write the first letter?', ['lowercase s', 'Capital S', 'No letter at all', 'A number'], 1),
   ('Where might you write your name at school?', ['On your worksheet or cubby', 'Nowhere at school', 'Only on the wall', 'Only in a book you do not own'], 0),
   ('Practising writing your name helps you build ___.', ['Cooking skills', 'Fine motor and writing skills', 'Swimming skills', 'Singing skills'], 1)])

d38_math = sub('Math', 'Estimation: About How Many?',
  'Students practise estimating, or making a smart guess, about how many objects are in a group before counting to check.',
  [('What does it mean to estimate?', ['make a smart guess', 'guess']),
   ('After you estimate how many objects there are, what should you do next?', ['count them', 'count']),
   ('Which is a more reasonable estimate for apples in a small basket: 5 or 5000?', ['5', 'five'])],
  [('Estimating means ___.', ['Counting very slowly', 'Making a smart guess about an amount', 'Ignoring numbers', 'Always guessing zero'], 1),
   ('If a jar looks like it has about 10 candies, a good estimate might be ___.', ['1000', '10', '0', '1'], 1),
   ('After estimating how many objects are in a group, what should you do to check?', ['Nothing', 'Count them', 'Throw them away', 'Draw them'], 1),
   ('Which is a more reasonable estimate for the number of students in one classroom?', ['2', '20', '2000', '0'], 1),
   ('Estimating is a useful skill because it helps us ___.', ['Make quick, reasonable guesses before counting exactly', 'Avoid counting forever', 'Make numbers disappear', 'Never need math'], 0)])

d38_sci = sub('Science', 'Magnets: Attract and Repel',
  'Students explore magnets and discover that they can pull, or attract, certain metal objects, and can also push away, or repel, other magnets.',
  [('What word means a magnet pulling an object toward it?', ['attract', 'attracting']),
   ('What word means two magnets pushing away from each other?', ['repel', 'repelling']),
   ('Name one object a magnet could pick up, like a paper clip.', ['paper clip', 'nail', 'metal object'])],
  [('What can a magnet pull toward it?', ['Wooden blocks', 'Certain metal objects', 'Paper only', 'Water'], 1),
   ('When a magnet pulls an object toward it, this is called ___.', ['Repelling', 'Attracting', 'Floating', 'Sinking'], 1),
   ('When two magnets push away from each other, this is called ___.', ['Attracting', 'Repelling', 'Melting', 'Freezing'], 1),
   ('Which object would a magnet most likely attract?', ['A plastic cup', 'A paper clip', 'A wooden spoon', 'A cotton ball'], 1),
   ('Magnets are useful for ___.', ['Picking up certain metal objects', 'Making food taste better', 'Growing plants', 'Changing the weather'], 0)])

d38_ss = sub('SocialStudies', 'Working Together: Teamwork and Cooperation',
  'Students explore how working together, sharing jobs, and helping each other lets a group accomplish more than one person alone, both at school and at home.',
  [('What do we call people working together toward the same goal?', ['teamwork', 'team']),
   ('Name one place you can practise teamwork, like at school or at home.', ['school', 'home', 'classroom']),
   ('When everyone helps clean up together, is that good teamwork or bad teamwork?', ['good teamwork', 'good'])],
  [('What does it mean to work as a team?', ['Working alone always', 'People working together toward a shared goal', 'Ignoring others', 'Competing to be the only winner'], 1),
   ('Which is an example of good teamwork?', ['Sharing jobs and helping each other clean up', 'Refusing to help classmates', 'Taking all the toys for yourself', 'Ignoring group instructions'], 0),
   ('Why is teamwork helpful?', ['It makes tasks harder', 'Groups can often accomplish more together than one person alone', 'It never helps anyone', 'Only adults can work as a team'], 1),
   ('When cleaning up a classroom together, everyone should ___.', ['Wait for one person to do it all', 'Help with a part of the job', 'Leave the room', 'Make more mess'], 1),
   ('Cooperation means ___.', ['Working well together with others', 'Working alone only', 'Ignoring group needs', 'Arguing constantly'], 0)])

# ─── DAY 39 ─────────────────────────────────────────────────────────────────
d39_lang = sub('Language', 'Listening and Following Directions',
  'Students practise listening carefully to simple two-step directions and following them in order, an important early literacy and classroom skill.',
  [('If told to clap then jump, what should you do first?', ['clap']),
   ('What should you do if you do not understand a direction?', ['ask a question', 'ask']),
   ('Following directions in the correct order is called ___.', ['sequencing'])],
  [('Why is it important to listen carefully to directions?', ['So you can follow them correctly', 'It is not important', 'Only teachers need to listen', 'Directions are always the same'], 0),
   ('If someone says stand up then clap your hands, what should you do first?', ['Clap your hands', 'Stand up', 'Sit down', 'Nothing'], 1),
   ('Following directions in the correct order is called ___.', ['Sequencing', 'Singing', 'Painting', 'Sleeping'], 0),
   ('Which is a good listening habit?', ['Looking at the speaker and staying quiet', 'Talking while others speak', 'Ignoring instructions', 'Playing with toys during directions'], 0),
   ('If you are unsure about a direction, what should you do?', ['Guess and never ask', 'Ask a question to make sure you understand', 'Ignore it', 'Do something else instead'], 1)])

d39_math = sub('Math', 'Doubles: Adding a Number to Itself',
  'Students explore doubles facts, where a number is added to itself, such as 2 plus 2 or 3 plus 3, to build quick addition fluency.',
  [('2 + 2 = ?', ['4', 'four']),
   ('3 + 3 = ?', ['6', 'six']),
   ('5 + 5 = ?', ['10', 'ten'])],
  [('2 + 2 = ?', ['3', '4', '5', '6'], 1),
   ('3 + 3 = ?', ['5', '6', '7', '8'], 1),
   ('A doubles fact means ___.', ['Adding two different numbers', 'Adding a number to itself', 'Subtracting a number', 'Multiplying by zero'], 1),
   ('4 + 4 = ?', ['6', '7', '8', '9'], 2),
   ('5 + 5 = ?', ['9', '10', '11', '8'], 1)])

d39_sci = sub('Science', 'Rocks and Soil',
  'Students explore rocks and soil, learning that rocks can be different sizes, colours, and textures, and that soil is made partly of tiny broken pieces of rock along with other materials.',
  [('What is soil partly made of, along with other materials?', ['broken rock', 'tiny rock pieces', 'rock']),
   ('Name one place plants often grow in outside.', ['soil', 'dirt', 'ground']),
   ('What do we call a very small rock, smaller than a stone?', ['pebble'])],
  [('Which of these best describes soil?', ['Only water', 'A mix of tiny broken rock pieces and other materials', 'A type of metal', 'A liquid'], 1),
   ('Rocks can be different ___.', ['Sizes, colours, and textures', 'Only one size', 'Only one colour', 'Only round'], 0),
   ('Which of these is an example of a rock?', ['A pebble', 'A cloud', 'A raindrop', 'A leaf only'], 0),
   ('Plants often grow in ___.', ['Only water', 'Soil', 'Only air', 'Only rocks'], 1),
   ('A very small rock, smaller than a stone, is often called a ___.', ['Boulder', 'Pebble', 'Mountain', 'Cliff'], 1)])

d39_ss = sub('SocialStudies', 'Children Around the World',
  'Students learn that children around the world go to school, play, and live in families, though homes, clothing, food, and languages may look different from place to place.',
  [('Name one thing that might be different for children in another country, like food or clothing.', ['food', 'clothing', 'language', 'homes']),
   ('Name one thing children around the world often have in common.', ['family', 'play', 'school', 'friends']),
   ('Learning about other cultures helps us build ___ for others.', ['respect', 'understanding'])],
  [('Which is true about children all around the world?', ['They are all exactly the same', 'They share things in common, like family and play, even though some things differ', 'None of them go to school', 'They never have families'], 1),
   ('Why might children in different countries speak different languages?', ['They come from different countries and cultures', 'Language never changes', 'It is random with no reason', 'Only some children speak languages'], 0),
   ('Which of these might be different for children in different parts of the world?', ['Clothing, food, and homes', 'Whether they are children at all', 'Whether they have families', 'Nothing is ever different'], 0),
   ('Learning about children in other countries helps us ___.', ['Understand and respect different cultures', 'Ignore other cultures', 'Believe only our own way is correct', 'Avoid learning anything new'], 0),
   ('Which activity do most children around the world enjoy, no matter where they live?', ['Playing', 'Nothing in common exists', 'Working only', 'Sleeping all day'], 0)])

# ─── DAY 40 (Review) ────────────────────────────────────────────────────────
d40_lang = sub('Language', 'Language Review: Sounds, Syllables, and Stories',
  'Students review key Language skills from recent weeks: the letters N and O, beginning and ending sounds, syllables, opposites, story elements, writing names, and listening to directions.',
  [('What letter comes right after M?', ['n']),
   ('What letter comes right after N?', ['o']),
   ('What part of a story usually solves the problem: the beginning or the end?', ['end', 'the end'])],
  [('Which letter makes the sound heard at the start of nest?', ['M', 'N', 'O', 'P'], 1),
   ('Which letter makes the round shape like the one in orange?', ['N', 'O', 'M', 'P'], 1),
   ('How many syllables (claps) are in the word banana?', ['1', '2', '3', '4'], 2),
   ('What is the opposite of hot?', ['Warm', 'Cold', 'Sunny', 'Dry'], 1),
   ('What part of a story tells us who the characters are?', ['The end', 'The middle', 'The beginning', 'The cover only'], 2)])

d40_math = sub('Math', 'Math Review: Numbers, Time, and Shapes',
  'Students review recent Math skills: comparing numbers, making 10, position words, telling time, tally marks, symmetry, numbers to 30, estimation, and doubles facts.',
  [('Which is less: 3 or 8?', ['3', 'three']),
   ('8 and ___ make 10.', ['2', 'two']),
   ('4 + 4 = ?', ['8', 'eight'])],
  [('Which is more: 4 or 9?', ['4', '9', 'They are equal', 'Cannot tell'], 1),
   ('6 and ___ make 10.', ['3', '4', '5', '2'], 1),
   ('What number comes right after 27?', ['26', '28', '29', '30'], 1),
   ('3 + 3 = ?', ['5', '6', '7', '8'], 1),
   ('A shape where both halves match when folded is called ___.', ['Symmetrical', 'Uneven', 'Random', 'Broken'], 0)])

d40_sci = sub('Science', 'Science Review: Senses, Life Cycles, and Our Earth',
  'Students review recent Science topics: the five senses, the life cycles of butterflies and frogs, healthy habits, reducing waste, simple machines, magnets, and rocks and soil.',
  [('Which body part helps you taste food?', ['tongue']),
   ('What is the last stage of a butterfly life cycle?', ['butterfly']),
   ('What word means two magnets pushing away from each other?', ['repel', 'repelling'])],
  [('Which body part do we use to hear?', ['Eyes', 'Ears', 'Nose', 'Tongue'], 1),
   ('What is the first stage of a butterfly life cycle?', ['Caterpillar', 'Egg', 'Chrysalis', 'Adult'], 1),
   ('What comes out of a frog egg?', ['Adult frog', 'Tadpole', 'Chrysalis', 'Caterpillar'], 1),
   ('What word means a magnet pulling an object toward it?', ['Repelling', 'Attracting', 'Floating', 'Melting'], 1),
   ('What is soil partly made of?', ['Only water', 'Tiny broken rock pieces', 'Only air', 'Only metal'], 1)])

d40_ss = sub('SocialStudies', 'Social Studies Review: Community and Change',
  'Students review recent Social Studies topics: transportation, maps, changes over time, traffic safety, where food comes from, caring for belongings, teamwork, keeping our community clean, and children around the world.',
  [('What colour traffic light means go?', ['green']),
   ('Where should garbage go?', ['garbage bin', 'bin', 'trash can']),
   ('Name one way children around the world are similar, like going to school or playing.', ['school', 'play', 'family'])],
  [('Which vehicle travels on train tracks?', ['Car', 'Train', 'Bicycle', 'Boat'], 1),
   ('What colour traffic light means stop?', ['Green', 'Yellow', 'Red', 'Blue'], 2),
   ('Who grows the fruits and vegetables we eat?', ['Teachers', 'Farmers', 'Doctors', 'Pilots'], 1),
   ('What do we call garbage left on the ground instead of in a bin?', ['Recycling', 'Litter', 'Soil', 'Compost'], 1),
   ('Working together toward a shared goal is called ___.', ['Teamwork', 'Arguing', 'Ignoring', 'Competing alone'], 0)])


g0_31_40 = [
    day(31, [d31_lang, d31_math, d31_sci, d31_ss]),
    day(32, [d32_lang, d32_math, d32_sci, d32_ss]),
    day(33, [d33_lang, d33_math, d33_sci, d33_ss]),
    day(34, [d34_lang, d34_math, d34_sci, d34_ss]),
    day(35, [d35_lang, d35_math, d35_sci, d35_ss]),
    day(36, [d36_lang, d36_math, d36_sci, d36_ss]),
    day(37, [d37_lang, d37_math, d37_sci, d37_ss]),
    day(38, [d38_lang, d38_math, d38_sci, d38_ss]),
    day(39, [d39_lang, d39_math, d39_sci, d39_ss]),
    day(40, [d40_lang, d40_math, d40_sci, d40_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_31_40)
    append_worksheet_days(0, g0_31_40)
