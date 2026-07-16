#!/usr/bin/env python3
"""Grade 1, Days 31-40 -- FIRST batch extending Grade 1 past Day 30.
Self-contained script (does NOT use gen_curriculum.py's sub()/day()/
append_to() helpers, since those do not support a worksheet field) modeled
exactly on gen_grade0_days61_70.py, but for Grade 1 (ages 6-7) instead of
Kindergarten:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-30 topics (see data/grade1.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely to
keep the generated .ts string literals valid.
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
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} grade 1 educational')
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


def _rebalance_answer_positions(days, seed=20260824):
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
d31_lang = sub('Language', 'Consonant Digraphs: sh, ch, th, wh',
  'Students learn that two consonants can combine to make one new sound called a digraph, such as sh in ship, ch in chip, th in thin, and wh in whale.',
  [('What two letters make the sh sound at the start of the word ship?', ['sh']),
   ('What two letters make the ch sound at the start of the word chip?', ['ch']),
   ('Say the word whale. What two letters make the wh sound at the start?', ['wh'])],
  [('Which word begins with the digraph sh?', ['Ship', 'Cat', 'Dog', 'Run'], 0),
   ('Which word begins with the digraph ch?', ['Chip', 'Sun', 'Pig', 'Hat'], 0),
   ('Which word begins with the digraph th?', ['Top', 'Thin', 'Man', 'Sit'], 1),
   ('A digraph is two consonant letters that make ___.', ['Two separate sounds', 'One new sound together', 'No sound at all', 'A vowel sound'], 1),
   ('Which word begins with the digraph wh?', ['Whale', 'Cat', 'Bed', 'Sun'], 0)])

d31_math = sub('Math', 'Counting to 100',
  'Students practise counting aloud from 1 to 100 by ones, and recognize written numerals up to 100, extending counting skills learned earlier in the year.',
  [('What number comes right after 59?', ['60', 'sixty']),
   ('What number comes right after 89?', ['90', 'ninety']),
   ('What number comes right before 100?', ['99', 'ninety-nine', 'ninety nine'])],
  [('What number comes right after 69?', ['68', '69', '70', '71'], 2),
   ('What number comes right after 99?', ['98', '99', '100', '101'], 2),
   ('Which number is greater, 76 or 67?', ['67', '76', 'They are equal', 'Cannot tell'], 1),
   ('What number comes right before 80?', ['78', '79', '80', '81'], 1),
   ('Counting from 1 to 100 means we say each number ___.', ['In order, one at a time', 'Backward only', 'Twice each', 'In random order'], 0)])

d31_sci = sub('Science', 'Seasonal Changes: Spring',
  'Students learn that spring is a season when the weather warms up, snow melts, plants begin to grow, and many animals become active again after winter.',
  [('Name one thing that happens to snow in spring.', ['it melts', 'melts', 'melting']),
   ('Name one thing that begins to grow in spring, like a flower or plant.', ['flowers', 'plants', 'flower', 'plant']),
   ('Does the weather usually get warmer or colder in spring?', ['warmer'])],
  [('What usually happens to the weather in spring?', ['It gets warmer', 'It gets colder', 'It stays exactly the same', 'It disappears'], 0),
   ('What happens to snow as spring arrives?', ['It grows bigger', 'It melts', 'It turns to sand', 'It turns purple'], 1),
   ('Which of these often happens to plants in spring?', ['They begin to grow', 'They disappear forever', 'They turn to stone', 'They freeze completely'], 0),
   ('Which season comes right before spring?', ['Summer', 'Fall', 'Winter', 'Spring again'], 2),
   ('Why do many animals become more active in spring?', ['The warmer weather brings more food and better conditions', 'Animals never move in spring', 'Spring has no effect on animals', 'Animals sleep more in spring'], 0)])

d31_ss = sub('SocialStudies', 'Our Neighbourhood: Places We Visit',
  'Students learn about familiar places in their neighbourhood, such as a park, library, or store, and discuss how each place helps the community.',
  [('Name one place you might visit in your neighbourhood, like a park or library.', ['park', 'library', 'store']),
   ('What can you borrow at a library?', ['books', 'a book']),
   ('Do neighbourhoods have many different places that help people?', ['yes'])],
  [('Which of these is a place you might find in a neighbourhood?', ['A park', 'The ocean floor', 'Outer space', 'A volcano'], 0),
   ('What can you do at a library?', ['Borrow books', 'Buy groceries', 'Fight fires', 'Deliver mail'], 0),
   ('Why are neighbourhood places like parks and libraries helpful?', ['They give people places to play, learn, and gather', 'They are not helpful', 'People never use them', 'They cost nothing and do nothing'], 0),
   ('A neighbourhood is a part of a larger ___.', ['Ocean', 'Community', 'Desert', 'Galaxy'], 1),
   ('Which of these might you visit to buy food in your neighbourhood?', ['A grocery store', 'A fire truck', 'A cloud', 'A mountain'], 0)])

# ─── DAY 32 ─────────────────────────────────────────────────────────────────
d32_lang = sub('Language', 'Word Families: -it and -in',
  'Students explore the -it and -in word families, learning that changing the first letter of sit or pin can create new rhyming words such as bit, hit, win, and fin.',
  [('Change the first letter of sit to make a new word that rhymes.', ['bit', 'hit', 'fit', 'kit']),
   ('Change the first letter of pin to make a new word that rhymes.', ['win', 'fin', 'din', 'tin']),
   ('Do sit and hit belong to the same word family?', ['yes'])],
  [('Which word belongs to the -it word family?', ['Sit', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word belongs to the -in word family?', ['Top', 'Win', 'Man', 'Bed'], 1),
   ('Which word rhymes with pin?', ['Fin', 'Cat', 'Dog', 'Sun'], 0),
   ('A word family is a group of words that share the same ___.', ['Colour', 'Ending sound', 'Meaning', 'Author'], 1),
   ('Which word does not belong to the -it family?', ['Bit', 'Hit', 'Sit', 'Dog'], 3)])

d32_math = sub('Math', 'Numbers to 100: Tens and Ones',
  'Students learn to break apart two-digit numbers into tens and ones, such as recognizing that 47 is made of 4 tens and 7 ones.',
  [('How many tens are in the number 47?', ['4', 'four']),
   ('How many ones are in the number 47?', ['7', 'seven']),
   ('Write the number that has 6 tens and 3 ones.', ['63'])],
  [('How many tens are in the number 52?', ['2', '5', '7', '50'], 1),
   ('How many ones are in the number 38?', ['3', '8', '30', '38'], 1),
   ('Which number has 7 tens and 2 ones?', ['27', '72', '79', '70'], 1),
   ('What number is made of 9 tens and 0 ones?', ['9', '19', '90', '99'], 2),
   ('Breaking a number into tens and ones helps us understand its ___.', ['Colour', 'Value', 'Smell', 'Sound'], 1)])

d32_sci = sub('Science', 'Seasonal Changes: Summer',
  'Students learn that summer is the warmest season of the year, with long sunny days, and that many plants and animals are very active during this time.',
  [('Is summer usually the warmest or the coldest season?', ['warmest']),
   ('Are the days in summer usually long or short?', ['long']),
   ('Name one activity people often do in summer, like swimming.', ['swimming', 'swim', 'play outside', 'picnic'])],
  [('Which season is usually the warmest of the year?', ['Winter', 'Fall', 'Summer', 'Spring'], 2),
   ('In summer, are the days usually longer or shorter?', ['Longer', 'Shorter', 'Exactly the same', 'There is no daylight'], 0),
   ('Which season comes right after summer?', ['Winter', 'Spring', 'Fall', 'Summer again'], 2),
   ('Why are plants often very healthy and green in summer?', ['They get plenty of sunlight and warmth', 'Summer has no sunlight', 'Plants stop growing in summer', 'Summer is the coldest season'], 0),
   ('Which of these is a common summer activity?', ['Swimming outdoors', 'Building a snowman', 'Raking fallen leaves', 'Sledding downhill'], 0)])

d32_ss = sub('SocialStudies', 'Jobs People Do: Goods and Services',
  'Students learn that some jobs make or sell goods, like toys or bread, while other jobs provide services, like teaching or fixing things, and both kinds of jobs help a community.',
  [('Name one job that makes or sells a good, like a baker.', ['baker', 'toy maker', 'farmer']),
   ('Name one job that provides a service, like a teacher.', ['teacher', 'doctor', 'dentist']),
   ('Do both goods and services help people in a community?', ['yes'])],
  [('What word describes an item that is made or sold, like a toy?', ['A service', 'A good', 'A rule', 'A season'], 1),
   ('What word describes a helpful job like teaching or fixing something?', ['A good', 'A service', 'A holiday', 'A season'], 1),
   ('Which of these jobs mainly provides a service?', ['Teacher', 'Toy maker', 'Baker', 'Farmer'], 0),
   ('Which of these jobs mainly makes a good?', ['Doctor', 'Dentist', 'Baker', 'Teacher'], 2),
   ('Why does a community need both goods and services?', ['People need things to buy and helpful jobs done', 'Goods and services are not needed', 'Communities need only goods', 'Communities need only services'], 0)])

# ─── DAY 33 ─────────────────────────────────────────────────────────────────
d33_lang = sub('Language', 'Word Families: -ug and -ub',
  'Students explore the -ug and -ub word families, learning that changing the first letter of bug or cub can create new rhyming words such as hug, rug, tub, and cub.',
  [('Change the first letter of bug to make a new word that rhymes.', ['hug', 'rug', 'mug', 'jug', 'tug']),
   ('Change the first letter of cub to make a new word that rhymes.', ['tub', 'rub', 'sub', 'hub']),
   ('Do bug and hug belong to the same word family?', ['yes'])],
  [('Which word belongs to the -ug word family?', ['Bug', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word belongs to the -ub word family?', ['Top', 'Cub', 'Man', 'Bed'], 1),
   ('Which word rhymes with rug?', ['Hug', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word does not belong to the -ub family?', ['Cub', 'Tub', 'Rub', 'Cat'], 3),
   ('Word families help us read new words by noticing ___.', ['Colours', 'Similar endings', 'Page numbers', 'Pictures only'], 1)])

d33_math = sub('Math', 'Comparing Numbers: Greater Than and Less Than',
  'Students learn to compare two numbers up to 100 and use the words greater than, less than, and equal to describe which number is bigger or smaller.',
  [('Which number is greater, 45 or 54?', ['54']),
   ('Which number is less, 68 or 39?', ['39']),
   ('Are 20 and 20 equal or different?', ['equal', 'the same'])],
  [('Which number is greater, 62 or 26?', ['26', '62', 'They are equal', 'Cannot tell'], 1),
   ('Which number is less, 81 or 18?', ['81', '18', 'They are equal', 'Cannot tell'], 1),
   ('What word describes two numbers that have the same value?', ['Greater', 'Less', 'Equal', 'Odd'], 2),
   ('Which word means a number is bigger than another?', ['Less than', 'Greater than', 'Equal to', 'Odd'], 1),
   ('Which of these is true?', ['30 is less than 20', '50 is greater than 40', '15 is greater than 25', '10 is equal to 20'], 1)])

d33_sci = sub('Science', 'Insects and Their Body Parts',
  'Students learn that insects, such as ants and butterflies, have three main body parts and six legs, and explore how insects are different from other animals.',
  [('How many legs does an insect have?', ['6', 'six']),
   ('Name one insect, like an ant or butterfly.', ['ant', 'butterfly', 'bee', 'ladybug']),
   ('How many main body parts does an insect have?', ['3', 'three'])],
  [('How many legs does an insect have?', ['4', '6', '8', '10'], 1),
   ('How many main body parts does an insect have?', ['2', '3', '4', '5'], 1),
   ('Which of these is an insect?', ['Butterfly', 'Dog', 'Fish', 'Bird'], 0),
   ('Which of these is not an insect?', ['Ant', 'Bee', 'Spider', 'Ladybug'], 2),
   ('What covers the outside of many insect bodies?', ['Fur', 'A hard outer shell', 'Feathers', 'Scales like a fish'], 1)])

d33_ss = sub('SocialStudies', 'Needs and Wants: What We Really Need',
  'Students learn to tell the difference between needs, things we must have to live such as food and shelter, and wants, things that are nice to have but not necessary such as toys.',
  [('Name one thing that is a need, like food or water.', ['food', 'water', 'shelter', 'clothing']),
   ('Name one thing that is a want, like a toy.', ['toy', 'candy', 'video game']),
   ('Do people need food to live?', ['yes'])],
  [('Which of these is a need?', ['A toy', 'Water', 'A video game', 'Candy'], 1),
   ('Which of these is a want?', ['Shelter', 'Food', 'A new toy', 'Water'], 2),
   ('What is the difference between a need and a want?', ['Needs are necessary to live, wants are not', 'There is no difference', 'Wants are more important', 'Needs are only for adults'], 0),
   ('Which of these is something every person needs to survive?', ['A bicycle', 'Shelter', 'A game console', 'A birthday gift'], 1),
   ('Why is it helpful to understand needs and wants?', ['It helps us make good choices about what is most important', 'Needs and wants are the same thing', 'It does not matter', 'Wants are always more important than needs'], 0)])

# ─── DAY 34 ─────────────────────────────────────────────────────────────────
d34_lang = sub('Language', 'Beginning Blends: sp, sm, sn, sw',
  'Students learn that two consonants can blend together at the start of a word, such as sp in spin, sm in smile, sn in snail, and sw in swim.',
  [('What two letters blend together at the start of the word spin?', ['sp']),
   ('What two letters blend together at the start of the word smile?', ['sm']),
   ('Say the word swim. What two letters blend at the start?', ['sw'])],
  [('Which word begins with the blend sp?', ['Spin', 'Cat', 'Dog', 'Run'], 0),
   ('Which word begins with the blend sm?', ['Smile', 'Sun', 'Pig', 'Hat'], 0),
   ('Which word begins with the blend sn?', ['Snail', 'Top', 'Man', 'Sit'], 0),
   ('Which word begins with the blend sw?', ['Swim', 'Cat', 'Bed', 'Sun'], 0),
   ('A beginning blend is when two consonant letters ___.', ['Are silent', 'Blend their sounds together at the start of a word', 'Turn into vowels', 'Are never used'], 1)])

d34_math = sub('Math', 'Fractions: Quarters',
  'Students learn that dividing a whole into four equal parts creates quarters, and that one of the four parts is called one-quarter or one-fourth.',
  [('If a pizza is cut into 4 equal parts, what is each part called?', ['a quarter', 'quarter', 'one-quarter', 'one fourth', 'a fourth']),
   ('How many quarters make one whole?', ['4', 'four']),
   ('Is one-quarter bigger or smaller than one-half?', ['smaller'])],
  [('If a shape is cut into 4 equal parts, each part is called ___.', ['One-half', 'One-quarter', 'One-third', 'One whole'], 1),
   ('How many quarters make one whole?', ['2', '3', '4', '5'], 2),
   ('Which is smaller, one-quarter or one-half?', ['One-quarter', 'One-half', 'They are equal', 'Cannot tell'], 0),
   ('A whole cut into four equal parts shows ___.', ['Halves', 'Thirds', 'Quarters', 'Wholes'], 2),
   ('If you eat one-quarter of a sandwich, how many quarters are left?', ['1', '2', '3', '4'], 2)])

d34_sci = sub('Science', 'Nocturnal Animals: Creatures of the Night',
  'Students learn that nocturnal animals, such as owls and bats, are awake and active mostly at night and sleep during the day.',
  [('What word describes animals that are awake mostly at night?', ['nocturnal']),
   ('Name one nocturnal animal, like an owl or bat.', ['owl', 'bat', 'raccoon']),
   ('Do nocturnal animals usually sleep during the day?', ['yes'])],
  [('What does the word nocturnal mean?', ['Awake mostly during the day', 'Awake mostly at night', 'Never awake', 'Always asleep'], 1),
   ('Which of these animals is known for being nocturnal?', ['Owl', 'Chicken', 'Robin', 'Squirrel'], 0),
   ('What do most nocturnal animals do during the day?', ['Play loudly', 'Sleep or rest', 'Fly to school', 'Go swimming'], 1),
   ('Why might large eyes help a nocturnal animal like an owl?', ['They help the animal see well in the dark', 'Large eyes are not helpful at night', 'Nocturnal animals cannot see at all', 'Large eyes help in bright sunlight only'], 0),
   ('Which of these is also a nocturnal animal?', ['Bat', 'Rooster', 'Duck', 'Robin'], 0)])

d34_ss = sub('SocialStudies', 'Transportation Then and Now',
  'Students compare how people travelled long ago, such as by horse and wagon, to how people travel today, such as by car, bus, and airplane.',
  [('Name one way people travelled long ago, like by horse.', ['horse', 'wagon', 'horse and wagon']),
   ('Name one way people travel today, like by car.', ['car', 'bus', 'airplane', 'train']),
   ('Is travel today usually faster than travel long ago?', ['yes'])],
  [('How did many people travel long ago before cars were invented?', ['By airplane', 'By horse and wagon', 'By rocket', 'By submarine'], 1),
   ('Which of these is a common way people travel today?', ['Horse and wagon only', 'Car', 'Ox cart only', 'Sailboat only'], 1),
   ('How has transportation changed over time?', ['It has become faster and easier', 'It has not changed at all', 'It has become slower', 'People no longer travel'], 0),
   ('Which of these did NOT exist long ago the way it does today?', ['Airplanes', 'Walking', 'Rivers', 'The sun'], 0),
   ('Why is it useful to learn about transportation then and now?', ['It helps us understand how travel has changed and improved', 'Transportation never changes', 'Old and new transportation are identical', 'It is not useful'], 0)])

# ─── DAY 35 ─────────────────────────────────────────────────────────────────
d35_lang = sub('Language', 'Rhyming Words',
  'Students practise identifying rhyming words, pairs of words that end with the same sound, such as cat and hat or sun and fun.',
  [('Name a word that rhymes with cat.', ['hat', 'bat', 'mat', 'sat', 'rat', 'fat']),
   ('Name a word that rhymes with sun.', ['fun', 'run', 'bun', 'one']),
   ('Do hat and cat rhyme?', ['yes'])],
  [('Which word rhymes with cat?', ['Hat', 'Dog', 'Sun', 'Pig'], 0),
   ('Which word rhymes with sun?', ['Cat', 'Fun', 'Dog', 'Bed'], 1),
   ('Two words rhyme when they ___.', ['Start with the same letter', 'End with the same sound', 'Have the same meaning', 'Are the same length'], 1),
   ('Which word rhymes with hop?', ['Top', 'Cat', 'Sun', 'Pig'], 0),
   ('Which pair of words does NOT rhyme?', ['Cat and hat', 'Sun and fun', 'Dog and log', 'Cat and dog'], 3)])

d35_math = sub('Math', 'Measuring Capacity: More and Less',
  'Students compare the capacity of different containers, learning which container holds more or less using non-standard units, such as pouring water between cups.',
  [('If a big jug and a small cup are filled with water, which one holds more?', ['the jug', 'jug', 'big jug']),
   ('What word describes how much a container can hold?', ['capacity']),
   ('Which usually holds less water, a bathtub or a teacup?', ['teacup', 'the teacup'])],
  [('Which container usually holds more water, a bucket or a teacup?', ['Teacup', 'Bucket', 'They hold the same', 'Cannot tell'], 1),
   ('What word describes how much liquid a container can hold?', ['Length', 'Capacity', 'Weight', 'Colour'], 1),
   ('If you pour water from a full cup into a bigger empty bowl, what happens?', ['The water disappears', 'The water fits with room to spare', 'The bowl overflows immediately', 'Nothing happens'], 1),
   ('Which of these containers likely holds the least amount of water?', ['A bathtub', 'A swimming pool', 'A teaspoon', 'A bucket'], 2),
   ('Comparing capacity helps us understand ___.', ['How much a container can hold', 'How heavy an object is', 'How long an object is', 'What colour something is'], 0)])

d35_sci = sub('Science', 'The Moon and Its Phases',
  'Students learn that the Moon appears to change shape in the sky over about a month, moving through phases such as a full moon and a crescent moon.',
  [('What do we call it when the whole round Moon is visible in the sky?', ['full moon']),
   ('What do we call the thin curved shape of the Moon?', ['crescent moon', 'crescent']),
   ('Does the Moon appear to change shape over time?', ['yes'])],
  [('What do we call it when the Moon looks like a complete circle in the sky?', ['New moon', 'Full moon', 'Crescent moon', 'Half moon'], 1),
   ('What do we call the thin curved shape of the Moon?', ['Full moon', 'Crescent moon', 'Square moon', 'Star'], 1),
   ('About how long does it take the Moon to go through all of its phases?', ['One day', 'About a month', 'One year', 'Ten years'], 1),
   ('Why does the Moon appear to change shape in the sky?', ['Different amounts of sunlit Moon are visible from Earth over time', 'The Moon actually changes size', 'The Moon disappears and grows back', 'Clouds change the Moon shape'], 0),
   ('The changing shapes of the Moon are called Moon ___.', ['Phases', 'Seasons', 'Colours', 'Rings'], 0)])

d35_ss = sub('SocialStudies', 'My Body Belongs to Me: Personal Safety',
  'Students learn simple personal safety rules, such as it is okay to say no to unwanted touches and to tell a trusted adult if something makes them feel unsafe.',
  [('What should you do if something makes you feel unsafe?', ['tell a trusted adult', 'tell an adult']),
   ('Is it okay to say no if someone tries to touch you in a way you do not like?', ['yes']),
   ('Name one trusted adult you could talk to, like a parent or teacher.', ['parent', 'teacher', 'mom', 'dad'])],
  [('What should you do if someone makes you feel unsafe?', ['Stay quiet forever', 'Tell a trusted adult', 'Run away and hide alone', 'Ignore the feeling'], 1),
   ('Is it okay to say no to a touch that makes you feel uncomfortable?', ['No, never', 'Yes, it is okay', 'Only if an adult says so', 'Only at school'], 1),
   ('Which of these is a trusted adult you might talk to about a safety concern?', ['A parent or teacher', 'A stranger online', 'Nobody', 'A cartoon character'], 0),
   ('Why is it important to talk about feelings of being unsafe?', ['Trusted adults can help keep you safe', 'Feelings are never important', 'It is better to stay silent', 'Only adults have feelings'], 0),
   ('Whose body is it, and who gets to decide about unwanted touches?', ['Only an adult decides', 'My body belongs to me', 'No one decides', 'Only a teacher decides'], 1)])

# ─── DAY 36 ─────────────────────────────────────────────────────────────────
d36_lang = sub('Language', 'Sequencing Events: First, Next, Last',
  'Students learn to put events from a story in order using the words first, next, and last, helping them understand and retell what happened.',
  [('What word tells us an event that happens at the very beginning?', ['first']),
   ('What word tells us an event that happens at the very end?', ['last']),
   ('Put these words in order to describe a sequence: first, next, ___.', ['last'])],
  [('Which word describes the event that happens at the beginning of a story?', ['Last', 'First', 'Middle only', 'Never'], 1),
   ('Which word describes the event that happens at the end of a story?', ['First', 'Next', 'Last', 'Before'], 2),
   ('Which sentence uses sequencing words correctly?', ['First we ate lunch then we woke up', 'First we woke up, next we ate breakfast, last we went to school', 'Last we start the day', 'None of these show order'], 1),
   ('Why is putting events in order important when retelling a story?', ['It helps the story make sense', 'Order does not matter', 'Stories have no order', 'Only the ending matters'], 0),
   ('Which word would you use to describe an event that happens in the middle?', ['First', 'Next', 'Last', 'Before'], 1)])

d36_math = sub('Math', 'Symmetry: Matching Halves',
  'Students explore symmetry by folding shapes and pictures in half to see if both sides match exactly, learning that a symmetrical shape has two matching halves.',
  [('What word describes a shape whose two halves match exactly?', ['symmetrical', 'symmetry']),
   ('Name one shape that is symmetrical, like a circle or square.', ['circle', 'square', 'heart']),
   ('If you fold a symmetrical shape in half, do both sides match?', ['yes'])],
  [('What does it mean for a shape to be symmetrical?', ['Both halves match exactly', 'The shape has no sides', 'The shape is always a circle', 'The shape is coloured red'], 0),
   ('Which of these shapes is symmetrical?', ['A heart', 'A scribble', 'A random blob', 'An uneven splash'], 0),
   ('If you fold a symmetrical picture exactly in half, what happens?', ['Both sides match', 'The sides look completely different', 'The picture disappears', 'Nothing can be compared'], 0),
   ('A line that divides a shape into two matching halves is called a line of ___.', ['Colour', 'Symmetry', 'Length', 'Weight'], 1),
   ('Which of these letters is symmetrical when folded top to bottom?', ['B', 'F', 'G', 'J'], 0)])

d36_sci = sub('Science', 'Recycling and Reducing Waste',
  'Students learn simple ways to care for the environment by reducing waste, reusing items, and recycling materials such as paper, plastic, and cans.',
  [('Name one material that can be recycled, like paper or plastic.', ['paper', 'plastic', 'cans', 'glass']),
   ('What word describes using something again instead of throwing it away?', ['reuse', 'reusing']),
   ('Is it good for the environment to recycle instead of throwing everything away?', ['yes'])],
  [('Which of these materials can often be recycled?', ['Paper', 'Sunlight', 'Air', 'Rainbows'], 0),
   ('What does it mean to reuse an item?', ['Throwing it away right away', 'Using it again instead of throwing it away', 'Burying it in the yard', 'Ignoring it'], 1),
   ('Why is recycling helpful for the environment?', ['It reduces waste and saves resources', 'It creates more garbage', 'It harms the environment', 'It has no effect'], 0),
   ('Which of these actions helps reduce waste?', ['Using a reusable water bottle', 'Throwing away recyclable cans', 'Wasting paper', 'Littering outside'], 0),
   ('The three words often used together to describe caring for the environment are reduce, reuse, and ___.', ['Recycle', 'Repeat', 'Remove', 'Replace'], 0)])

d36_ss = sub('SocialStudies', 'Communication Then and Now',
  'Students compare how people communicated long ago, such as sending letters, to how people communicate today, such as using phones and computers.',
  [('Name one way people communicated long ago, like writing a letter.', ['letter', 'writing letters', 'sending letters']),
   ('Name one way people communicate today, like using a phone.', ['phone', 'telephone', 'computer', 'email']),
   ('Is communication today usually faster than communication long ago?', ['yes'])],
  [('How did many people send messages long ago before phones were common?', ['By writing letters', 'By video call', 'By text message', 'By email'], 0),
   ('Which of these is a common way people communicate today?', ['Only smoke signals', 'Telephone', 'Only carrier pigeons', 'Only letters carried by horse'], 1),
   ('How has communication changed over time?', ['It has become faster and easier', 'It has not changed at all', 'It has become slower', 'People no longer communicate'], 0),
   ('Which of these did people use to communicate long before phones existed?', ['Written letters', 'Video calls', 'The internet', 'Text messages'], 0),
   ('Why is it useful to compare communication then and now?', ['It helps us understand how technology has changed our lives', 'Communication never changes', 'Old and new communication are identical', 'It is not useful'], 0)])

# ─── DAY 37 ─────────────────────────────────────────────────────────────────
d37_lang = sub('Language', 'Fiction and Non-Fiction: Comparing Texts',
  'Students learn to compare fiction texts, which tell made-up stories, with non-fiction texts, which give true facts and information.',
  [('Does a fiction book tell a true story or a made-up story?', ['made-up story', 'made up story', 'made-up']),
   ('Does a non-fiction book give true facts or made-up stories?', ['true facts', 'facts']),
   ('Name one example of a non-fiction topic, like animals or weather.', ['animals', 'weather', 'space'])],
  [('What kind of story does a fiction book tell?', ['A true story', 'A made-up story', 'No story at all', 'Only facts'], 1),
   ('What kind of information does a non-fiction book give?', ['Made-up stories', 'True facts and information', 'Only pictures', 'Nothing at all'], 1),
   ('Which of these is an example of a fiction book?', ['A book about talking animals having an adventure', 'A book about real ocean animals', 'A book about the water cycle', 'A book about the solar system'], 0),
   ('Which of these is an example of a non-fiction book?', ['A book of true facts about dinosaurs', 'A story about a dragon', 'A tale about a magic castle', 'A story about a talking teddy bear'], 0),
   ('Why is it useful to know if a book is fiction or non-fiction?', ['It helps us know if a book is telling a true story or made-up story', 'It does not matter', 'All books are the same', 'Fiction and non-fiction are identical'], 0)])

d37_math = sub('Math', 'Sorting and Classifying Objects',
  'Students practise sorting a group of objects into categories based on shared attributes, such as colour, size, or shape, and explain the rule used to sort them.',
  [('Name one way you could sort a group of buttons, like by colour or size.', ['colour', 'size', 'shape']),
   ('If you sort toys by colour, what group would a red ball and a red block go in?', ['red', 'red group']),
   ('Can objects be sorted in more than one way?', ['yes'])],
  [('Which of these is a way you could sort a group of objects?', ['By colour', 'By nothing', 'Randomly with no rule', 'Objects cannot be sorted'], 0),
   ('If you sort shapes by number of sides, where would a triangle and a different triangle go?', ['In different groups', 'In the same group', 'No group at all', 'Shapes cannot be sorted this way'], 1),
   ('Why do we sort objects into groups?', ['It helps us see patterns and organize information', 'Sorting is never useful', 'It makes objects disappear', 'It has no purpose'], 0),
   ('Which of these objects would NOT belong in a group of red objects?', ['A red apple', 'A red ball', 'A blue car', 'A red block'], 2),
   ('A sorting rule tells us ___.', ['How objects are grouped together', 'Nothing useful', 'The colour of the sky', 'The weather'], 0)])

d37_sci = sub('Science', 'Taking Care of Our Teeth',
  'Students learn simple habits for keeping teeth healthy, such as brushing twice a day, flossing, eating healthy foods, and visiting the dentist.',
  [('How many times a day should you usually brush your teeth?', ['2', 'two', 'twice']),
   ('Who helps check that your teeth are healthy?', ['dentist']),
   ('Name one healthy food that is good for your teeth, like an apple.', ['apple', 'vegetables', 'cheese'])],
  [('How many times a day should you usually brush your teeth?', ['Once', 'Twice', 'Never', 'Only on weekends'], 1),
   ('Who is a helper that checks and cares for our teeth?', ['A dentist', 'A baker', 'A firefighter', 'A postal worker'], 0),
   ('Which of these habits helps keep our teeth healthy?', ['Brushing and flossing', 'Eating candy all day', 'Never brushing', 'Ignoring toothaches'], 0),
   ('Why is it important to take care of our teeth?', ['Healthy teeth help us eat and stay healthy', 'Teeth do not need care', 'Teeth care is not important', 'Only adults have teeth'], 0),
   ('Which of these foods is better for healthy teeth?', ['An apple', 'A sugary candy', 'A sugary soda', 'A lollipop'], 0)])

d37_ss = sub('SocialStudies', 'Cooperation and Teamwork in a Group',
  'Students learn what it means to cooperate with others in a group, such as sharing materials, taking turns, and listening to different ideas to reach a shared goal.',
  [('What word describes people working together toward a shared goal?', ['cooperation', 'teamwork']),
   ('Name one way to cooperate in a group, like sharing or taking turns.', ['sharing', 'taking turns', 'listening']),
   ('Should group members listen to each other ideas?', ['yes'])],
  [('What does it mean to cooperate with a group?', ['Working together toward a shared goal', 'Ignoring everyone else', 'Doing everything alone', 'Refusing to share'], 0),
   ('Which of these shows good cooperation in a group?', ['Sharing materials and taking turns', 'Grabbing everything for yourself', 'Yelling over others', 'Refusing to listen'], 0),
   ('Why is cooperation important when working in a group?', ['It helps the group reach its goal more smoothly', 'Cooperation is not helpful', 'Groups work better without cooperation', 'It slows everything down'], 0),
   ('What should you do if a group member has a different idea than you?', ['Ignore them completely', 'Listen and discuss the idea', 'Yell at them', 'Leave the group'], 1),
   ('A group that cooperates well can often ___.', ['Finish tasks more successfully', 'Never finish anything', 'Make tasks harder', 'Avoid working together'], 0)])

# ─── DAY 38 ─────────────────────────────────────────────────────────────────
d38_lang = sub('Language', 'Asking and Answering Questions About a Text',
  'Students practise asking and answering simple questions about a story or text they have read or heard, to check their understanding of what happened.',
  [('What is one question you could ask about a story you just read?', ['who is in the story', 'what happened', 'where did it happen']),
   ('Why do we ask questions about a text?', ['to understand it', 'to check understanding']),
   ('Can asking questions help you understand a story better?', ['yes'])],
  [('Why do readers ask questions about a text?', ['To help them understand what they read', 'Questions are never helpful', 'To confuse themselves', 'To skip reading'], 0),
   ('Which of these is a good question to ask after reading a story?', ['What happened in the story?', 'What is your favourite colour?', 'What is the weather today?', 'None of these'], 0),
   ('Answering questions about a text helps us ___.', ['Understand and remember what we read', 'Forget the story', 'Ignore the story', 'Skip the ending'], 0),
   ('Which question word would you use to ask about a character in a story?', ['Who', 'Never', 'Nothing', 'Colour'], 0),
   ('If you cannot answer a question about a story, what might help?', ['Reading the story again', 'Giving up completely', 'Ignoring the question', 'Changing the story'], 0)])

d38_math = sub('Math', 'Money: Making Small Amounts',
  'Students practise combining coins, such as nickels, dimes, and pennies, to make small amounts of money, such as making 15 cents using a dime and a nickel.',
  [('Which two coins could you use to make 15 cents?', ['dime and nickel', 'a dime and a nickel']),
   ('How many pennies make 5 cents?', ['5', 'five']),
   ('What coin is worth 10 cents?', ['dime'])],
  [('Which coin is worth 10 cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 2),
   ('Which coin is worth 5 cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 1),
   ('Which combination of coins makes 15 cents?', ['A dime and a nickel', 'Two pennies', 'A quarter', 'One nickel'], 0),
   ('How many nickels make 10 cents?', ['1', '2', '3', '4'], 1),
   ('If you have a dime and two pennies, how much money do you have?', ['10 cents', '11 cents', '12 cents', '13 cents'], 2)])

d38_sci = sub('Science', 'The Five Senses',
  'Students review the five senses, sight, hearing, smell, taste, and touch, and the body part used for each, such as eyes for sight and ears for hearing.',
  [('What body part do we use to smell?', ['nose']),
   ('What body part do we use to taste?', ['tongue']),
   ('Name one sense that uses our skin to feel things.', ['touch'])],
  [('Which body part do we use to smell?', ['Eyes', 'Ears', 'Nose', 'Tongue'], 2),
   ('Which body part do we use to taste?', ['Nose', 'Tongue', 'Ears', 'Skin'], 1),
   ('Which sense do we use to hear sounds?', ['Sight', 'Hearing', 'Smell', 'Taste'], 1),
   ('Which body part helps us feel if something is soft or rough?', ['Skin', 'Nose', 'Tongue', 'Ears'], 0),
   ('How many senses do people have?', ['3', '4', '5', '6'], 2)])

d38_ss = sub('SocialStudies', 'Our Capital City: Ottawa',
  'Students learn that Ottawa is the capital city of Canada, where important government buildings, such as the Parliament Buildings, are located.',
  [('What is the capital city of Canada?', ['ottawa']),
   ('What are the important government buildings in Ottawa called?', ['parliament buildings', 'parliament']),
   ('Is Ottawa an important city for the government of Canada?', ['yes'])],
  [('What is the capital city of Canada?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 1),
   ('What important buildings are located in Ottawa?', ['The Parliament Buildings', 'A large farm', 'A ski resort', 'A fishing dock'], 0),
   ('Why is Ottawa an important city in Canada?', ['It is where important government decisions are made', 'It is not important', 'It has no government buildings', 'It is the smallest town in Canada'], 0),
   ('In which province is Ottawa located?', ['Ontario', 'Quebec', 'Alberta', 'Manitoba'], 0),
   ('What is usually located in a capital city?', ['The government of a country', 'A large desert', 'A small pond', 'Nothing important'], 0)])

# ─── DAY 39 ─────────────────────────────────────────────────────────────────
d39_lang = sub('Language', 'Letter Writing: A Note to a Friend',
  'Students learn the basic parts of a friendly letter, including a greeting, a short message, and a closing, and practise writing a simple note to a friend.',
  [('What word often starts a friendly letter, like Dear?', ['dear']),
   ('What is one thing you might write in the closing of a letter, like Love or From?', ['love', 'from', 'your friend']),
   ('Does a friendly letter usually have a greeting at the start?', ['yes'])],
  [('What word often begins a friendly letter?', ['The End', 'Dear', 'Chapter One', 'Once'], 1),
   ('What is the greeting of a letter used for?', ['To end the letter', 'To greet the person you are writing to', 'To draw a picture', 'To add a date only'], 1),
   ('Which of these could be a closing for a friendly letter?', ['From', 'Once upon a time', 'Chapter Two', 'The middle'], 0),
   ('Why might you write a letter to a friend?', ['To share news or say something kind', 'Letters are never useful', 'To confuse your friend', 'To avoid talking'], 0),
   ('A friendly letter usually has a greeting, a message, and a ___.', ['Table of contents', 'Closing', 'Index', 'Glossary'], 1)])

d39_math = sub('Math', 'Time: Half Past the Hour',
  'Students learn to read an analog clock showing half past the hour, recognizing that the long hand points to the 6 and the short hand is halfway between two numbers.',
  [('When the long hand points to the 6, what part of the hour is it?', ['half past', 'half past the hour']),
   ('At half past 3, is the short hand pointing exactly at the 3 or between the 3 and 4?', ['between the 3 and 4', 'between 3 and 4']),
   ('What number does the long hand point to at half past any hour?', ['6', 'the 6'])],
  [('At half past the hour, where does the long hand point?', ['The 12', 'The 3', 'The 6', 'The 9'], 2),
   ('At half past 4, where is the short hand pointing?', ['Exactly at the 4', 'Between the 4 and 5', 'Exactly at the 5', 'Exactly at the 12'], 1),
   ('Half past the hour means how many minutes have passed since the hour started?', ['15 minutes', '30 minutes', '45 minutes', '60 minutes'], 1),
   ('If the long hand points to the 6 and the short hand is between the 7 and 8, what time is it?', ['Half past 6', 'Half past 7', 'Half past 8', 'Half past 12'], 1),
   ('Reading a clock to the half hour helps us know ___.', ['What time it is', 'What day it is', 'What season it is', 'What colour it is'], 0)])

d39_sci = sub('Science', 'Changing Materials: Heating and Cooling',
  'Students learn that heating and cooling can change materials, such as ice melting into water when warmed or water freezing into ice when cooled.',
  [('What happens to ice when it is heated?', ['it melts', 'melts']),
   ('What happens to water when it is cooled a lot?', ['it freezes', 'freezes']),
   ('Name one material that changes when you heat it, like ice or chocolate.', ['ice', 'chocolate', 'butter'])],
  [('What happens to ice when it is heated?', ['It melts into water', 'It turns to stone', 'It disappears completely', 'It gets colder'], 0),
   ('What happens to water when it is cooled to a very low temperature?', ['It boils', 'It freezes into ice', 'It turns to gas', 'Nothing happens'], 1),
   ('Heating and cooling can change a material from one ___ to another.', ['Colour', 'State', 'Name', 'Owner'], 1),
   ('Which of these is an example of heating changing a material?', ['Butter melting in the sun', 'A rock staying the same', 'A book being read', 'A shoe being tied'], 0),
   ('Why is it useful to know how heating and cooling change materials?', ['It helps us understand how the world around us works', 'It is not useful', 'Materials never change', 'Heat and cold do nothing'], 0)])

d39_ss = sub('SocialStudies', 'Landmarks and Special Places in Canada',
  'Students learn about well-known Canadian landmarks, such as Niagara Falls and the Rocky Mountains, and discuss why these special places are important.',
  [('Name one famous Canadian landmark, like Niagara Falls.', ['niagara falls', 'the rocky mountains', 'cn tower']),
   ('Are the Rocky Mountains located in Canada?', ['yes']),
   ('What is Niagara Falls an example of, a waterfall or a desert?', ['waterfall'])],
  [('What is Niagara Falls?', ['A famous waterfall', 'A desert', 'A small pond', 'A city hall'], 0),
   ('Which of these is a famous Canadian mountain range?', ['The Rocky Mountains', 'The Sahara Desert', 'The Amazon River', 'The Great Wall'], 0),
   ('Why are landmarks like Niagara Falls important to Canada?', ['They are special natural places many people visit', 'They are not important', 'No one visits them', 'They are found in every country'], 0),
   ('Which of these is a tall tower landmark found in Toronto?', ['The CN Tower', 'The Eiffel Tower', 'The Great Wall', 'The Rocky Mountains'], 0),
   ('What is a landmark?', ['A well-known and special place', 'A type of food', 'A kind of weather', 'A school subject'], 0)])

# ─── DAY 40 (Review) ────────────────────────────────────────────────────────
d40_lang = sub('Language', 'Language Review: Sounds, Words, and Stories',
  'Students review recent Language skills: digraphs, word families, blends, rhyming, sequencing, and comparing fiction and non-fiction texts.',
  [('What two letters make the sh sound at the start of the word ship?', ['sh']),
   ('Name a word that rhymes with cat.', ['hat', 'bat', 'mat', 'sat', 'rat', 'fat']),
   ('Does a fiction book tell a true story or a made-up story?', ['made-up story', 'made up story', 'made-up'])],
  [('Which word begins with the digraph sh?', ['Ship', 'Cat', 'Dog', 'Run'], 0),
   ('Which word rhymes with cat?', ['Hat', 'Dog', 'Sun', 'Pig'], 0),
   ('Which word belongs to the -it word family?', ['Sit', 'Cat', 'Dog', 'Sun'], 0),
   ('What kind of story does a fiction book tell?', ['A true story', 'A made-up story', 'No story at all', 'Only facts'], 1),
   ('Which word begins with the blend sp?', ['Spin', 'Cat', 'Dog', 'Run'], 0)])

d40_math = sub('Math', 'Math Review: Numbers, Shapes, and Time',
  'Students review recent Math skills: counting to 100, place value, comparing numbers, fractions, capacity, symmetry, sorting, money, and telling time to the half hour.',
  [('What number comes right after 89?', ['90', 'ninety']),
   ('How many tens are in the number 47?', ['4', 'four']),
   ('How many quarters make one whole?', ['4', 'four'])],
  [('What number comes right after 99?', ['98', '99', '100', '101'], 2),
   ('Which number is greater, 62 or 26?', ['26', '62', 'They are equal', 'Cannot tell'], 1),
   ('If a shape is cut into 4 equal parts, each part is called ___.', ['One-half', 'One-quarter', 'One-third', 'One whole'], 1),
   ('Which coin is worth 10 cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 2),
   ('At half past the hour, where does the long hand point?', ['The 12', 'The 3', 'The 6', 'The 9'], 2)])

d40_sci = sub('Science', 'Science Review: Seasons, Senses, and Earth',
  'Students review recent Science topics: seasonal changes, insects, nocturnal animals, the Moon, recycling, dental health, the five senses, and changing materials.',
  [('Is summer usually the warmest or the coldest season?', ['warmest']),
   ('How many legs does an insect have?', ['6', 'six']),
   ('What happens to ice when it is heated?', ['it melts', 'melts'])],
  [('Which season is usually the warmest of the year?', ['Winter', 'Fall', 'Summer', 'Spring'], 2),
   ('How many legs does an insect have?', ['4', '6', '8', '10'], 1),
   ('Which of these animals is known for being nocturnal?', ['Owl', 'Chicken', 'Robin', 'Squirrel'], 0),
   ('Which body part do we use to smell?', ['Eyes', 'Ears', 'Nose', 'Tongue'], 2),
   ('What happens to water when it is cooled to a very low temperature?', ['It boils', 'It freezes into ice', 'It turns to gas', 'Nothing happens'], 1)])

d40_ss = sub('SocialStudies', 'Social Studies Review: Community, Canada, and Cooperation',
  'Students review recent Social Studies topics: neighbourhoods, jobs, needs and wants, transportation, personal safety, communication, cooperation, and Canadian landmarks.',
  [('Name one place you might visit in your neighbourhood, like a park or library.', ['park', 'library', 'store']),
   ('What is the capital city of Canada?', ['ottawa']),
   ('What should you do if someone makes you feel unsafe?', ['tell a trusted adult', 'tell an adult'])],
  [('Which of these is a place you might find in a neighbourhood?', ['A park', 'The ocean floor', 'Outer space', 'A volcano'], 0),
   ('Which of these is a need?', ['A toy', 'Water', 'A video game', 'Candy'], 1),
   ('What should you do if someone makes you feel unsafe?', ['Stay quiet forever', 'Tell a trusted adult', 'Run away and hide alone', 'Ignore the feeling'], 1),
   ('What is the capital city of Canada?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 1),
   ('What does it mean to cooperate with a group?', ['Working together toward a shared goal', 'Ignoring everyone else', 'Doing everything alone', 'Refusing to share'], 0)])


g1_31_40 = [
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
    _rebalance_answer_positions(g1_31_40)
    append_worksheet_days(1, g1_31_40)
