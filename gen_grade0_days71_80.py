#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 71-80 -- fifth batch extending Grade 0 past
the Days 61-70 batch, completing Days 1-80. This is a self-contained script
(does NOT use gen_curriculum.py's sub()/day()/append_to() helpers, since
those do not support a worksheet field) modeled exactly on
gen_grade0_days61_70.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-70 topics (see data/grade0.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely for
kindergarten readability and to keep the generated .ts string literals
valid.
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


def _rebalance_answer_positions(days, seed=20260911):
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


# ─── DAY 71 ─────────────────────────────────────────────────────────────────
d71_lang = sub('Language', 'Digraphs: sh, ch, and th',
  'Students learn that certain pairs of letters, such as sh, ch, and th, blend together to make one brand new sound instead of two separate sounds, as in ship, chip, and think.',
  [('What two letters make one new sound at the start of the word ship?', ['sh']),
   ('What two letters make one new sound at the start of the word chip?', ['ch']),
   ('Say the word think. What two letters make one new sound at the start?', ['th'])],
  [('Which word begins with the digraph sh?', ['Ship', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the digraph ch?', ['Chip', 'Man', 'Top', 'Sit'], 0),
   ('In the word think, which two letters make one new sound?', ['Th', 'In', 'Nk', 'Ti'], 0),
   ('A digraph is when two letters ___.', ['Blend to keep both sounds', 'Make one brand new sound together', 'Are always silent', 'Are never used together'], 1),
   ('Which word begins with the digraph th?', ['Think', 'Red', 'Big', 'Wet'], 0)])

d71_math = sub('Math', 'Counting to 100 by Ones',
  'Students practise counting aloud from 1 to 100 by ones, and recognize written numerals up to 100, extending their counting range beyond 50.',
  [('What number comes right after 59?', ['60', 'sixty']),
   ('What number comes right after 89?', ['90', 'ninety']),
   ('What number comes right after 99?', ['100', 'one hundred'])],
  [('What number comes right after 59?', ['60', '59', '61', '58'], 0),
   ('What number comes right after 89?', ['90', '88', '91', '80'], 0),
   ('What number comes right before 100?', ['99', '100', '98', '101'], 0),
   ('Which number is greater, 75 or 57?', ['75', '57', 'They are equal', 'Cannot tell'], 0),
   ('Counting from 1 to 100 means we say each number ___.', ['In order, one at a time', 'Backward only', 'Twice each', 'In random order'], 0)])

d71_sci = sub('Science', 'Our Heart: Beating and Pumping Blood',
  'Students learn that the heart is a strong muscle inside our chest that beats and pumps blood all through our body, and that exercise can make our heart beat faster.',
  [('What body part beats and pumps blood through our body?', ['heart']),
   ('Where in our body is our heart located?', ['chest', 'inside our chest']),
   ('Can exercise make our heart beat faster?', ['yes'])],
  [('What body part pumps blood through our body?', ['Heart', 'Elbow', 'Ear', 'Hair'], 0),
   ('Where is our heart located?', ['Inside our chest', 'In our foot', 'In our hair', 'Outside our body'], 0),
   ('What happens to our heart rate when we exercise?', ['It beats faster', 'It stops beating', 'It beats slower', 'Nothing changes'], 0),
   ('Why is our heart important?', ['It pumps blood that our body needs to work', 'It has no important job', 'It only helps us see', 'It only helps us hear'], 0),
   ('Our heart is best described as a strong ___.', ['Muscle', 'Bone', 'Feather', 'Rock'], 0)])

d71_ss = sub('SocialStudies', 'Our Dentist: Keeping Our Teeth Healthy',
  'Students learn about the job of a dentist, a community helper who checks our teeth, helps keep them clean and healthy, and teaches us how to brush properly.',
  [('Who checks and helps keep our teeth healthy?', ['dentist']),
   ('Name one tool a dentist might use, like a small mirror or brush.', ['mirror', 'brush', 'toothbrush']),
   ('Should we visit the dentist to keep our teeth healthy?', ['yes'])],
  [('Who checks and helps keep our teeth healthy?', ['A dentist', 'A baker', 'A postal worker', 'A firefighter'], 0),
   ('Why is it helpful to visit the dentist regularly?', ['It helps keep our teeth clean and healthy', 'It is not helpful', 'Teeth never need care', 'Dentists do not help with teeth'], 0),
   ('Which of these might a dentist teach you?', ['How to brush your teeth properly', 'How to bake bread', 'How to deliver mail', 'How to fly a plane'], 0),
   ('A dentist office is a place in our community that helps people stay ___.', ['Healthy', 'Lost', 'Hungry', 'Confused'], 0),
   ('A dentist is an example of a ___.', ['Wild animal', 'Community helper', 'Story character', 'Weather tool'], 1)])

# ─── DAY 72 ─────────────────────────────────────────────────────────────────
d72_lang = sub('Language', 'Silent E: The Magic E at the End',
  'Students learn that adding a silent e to the end of a short word can change the vowel sound, such as changing cap to cape or kit to kite, a pattern often called magic e.',
  [('Add a silent e to the word cap. What new word do you make?', ['cape']),
   ('Add a silent e to the word kit. What new word do you make?', ['kite']),
   ('Does adding a silent e to cap change the short a sound to a long a sound?', ['yes'])],
  [('Add a silent e to the word cap. What new word do you make?', ['Cape', 'Cup', 'Cop', 'Cab'], 0),
   ('Add a silent e to the word kit. What new word do you make?', ['Kite', 'Bit', 'Sit', 'Hit'], 0),
   ('What does a silent e at the end of a word often do to the vowel sound?', ['Makes it long', 'Makes it disappear', 'Makes it short', 'Does nothing at all'], 0),
   ('Which word has a silent e at the end?', ['Cake', 'Cat', 'Cap', 'Can'], 0),
   ('Add a silent e to the word tap. What new word do you make?', ['Tape', 'Top', 'Tip', 'Tag'], 0)])

d72_math = sub('Math', 'Doubles Plus One: Near Doubles',
  'Students learn a mental math strategy for adding two numbers that are almost the same, such as 5 plus 6, by first thinking of the double 5 plus 5 and then adding one more.',
  [('What is double 5 (5 plus 5)?', ['10', 'ten']),
   ('If double 5 is 10, what is 5 plus 6?', ['11', 'eleven']),
   ('What is double 4 plus 1 more, or 4 plus 5?', ['9', 'nine'])],
  [('What is double 5 (5 plus 5)?', ['10', '9', '11', '8'], 0),
   ('If double 5 is 10, what is 5 plus 6?', ['11', '10', '12', '9'], 0),
   ('What is double 3 (3 plus 3)?', ['6', '5', '7', '8'], 0),
   ('Using double 3 plus 3 equals 6, what is 3 plus 4?', ['7', '6', '8', '5'], 0),
   ('A near doubles strategy helps us add two numbers that are ___.', ['Almost the same', 'Always equal to 10', 'Never related', 'Always odd'], 0)])

d72_sci = sub('Science', 'Rainforests: A Warm, Wet Habitat',
  'Students learn that a rainforest is a warm, wet habitat with lots of rain and tall trees, home to many colourful animals such as parrots, monkeys, and frogs.',
  [('Is a rainforest usually a warm, wet place or a cold, dry place?', ['warm, wet', 'warm and wet']),
   ('Name one animal that can live in the rainforest, like a parrot or monkey.', ['parrot', 'monkey', 'frog']),
   ('Does a rainforest get a lot of rain?', ['yes'])],
  [('Is a rainforest usually warm and wet or cold and dry?', ['Warm and wet', 'Cold and dry', 'Cold and wet', 'Warm and dry'], 0),
   ('Which animal is well known for living in the rainforest?', ['Monkey', 'Polar bear', 'Camel', 'Penguin'], 0),
   ('What do rainforests have a lot of, that gives them their name?', ['Rain', 'Snow', 'Sand', 'Ice'], 0),
   ('Why do so many different animals live in the rainforest?', ['It is warm and wet with lots of trees and food', 'It has no trees or food', 'It is always frozen', 'Animals cannot live there'], 0),
   ('A rainforest is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d72_ss = sub('SocialStudies', 'Our Bank: Saving Our Money',
  'Students learn about the bank as a community place where people can keep their money safe and save it for things they want to buy later.',
  [('What is a place called where people can keep their money safe?', ['bank']),
   ('What word describes keeping money instead of spending it right away?', ['saving']),
   ('Can people save money at a bank for something they want later?', ['yes'])],
  [('What is a place called where people can keep their money safe?', ['A bank', 'A bakery', 'A firehall', 'A library'], 0),
   ('What does it mean to save money?', ['Keeping money instead of spending it right away', 'Throwing money away', 'Spending all money at once', 'Losing money on purpose'], 0),
   ('Why might a family save money at a bank?', ['To buy something they want later', 'Saving money is never useful', 'Banks do not help with money', 'Money cannot be saved'], 0),
   ('Which of these is something you might do at a bank?', ['Save your money', 'Buy bread', 'Borrow a library book', 'Mail a letter'], 0),
   ('A bank helps people in a community by ___.', ['Keeping their money safe', 'Delivering mail', 'Baking bread', 'Fighting fires'], 0)])

# ─── DAY 73 ─────────────────────────────────────────────────────────────────
d73_lang = sub('Language', 'Adding -ed: Talking About the Past',
  'Students learn that adding -ed to the end of many action words shows that something already happened, such as changing jump to jumped or walk to walked.',
  [('Add -ed to the word jump. What new word do you make?', ['jumped']),
   ('Add -ed to the word walk. What new word do you make?', ['walked']),
   ('Does the word jumped show something happening now or something that already happened?', ['already happened', 'happened already', 'the past'])],
  [('Add -ed to the word walk. What new word do you make?', ['Walked', 'Walking', 'Walks', 'Walker'], 0),
   ('Which word shows an action that already happened?', ['Played', 'Playing', 'Plays', 'Play'], 0),
   ('Adding -ed to an action word usually shows the action ___.', ['Already happened', 'Is happening right now', 'Will happen tomorrow', 'Never happened'], 0),
   ('Add -ed to the word help. What new word do you make?', ['Helped', 'Helping', 'Helps', 'Helper'], 0),
   ('Which of these words already ends in -ed?', ['Cooked', 'Cook', 'Cooks', 'Cooking'], 0)])

d73_math = sub('Math', 'Money: Adding Pennies and Nickels Together',
  'Students practise finding the total value of a small group of coins, learning that a penny is worth 1 cent and a nickel is worth 5 cents, and adding their values together.',
  [('How many cents is one penny worth?', ['1', 'one']),
   ('How many cents is one nickel worth?', ['5', 'five']),
   ('If you have 1 nickel and 1 penny, how many cents do you have in total?', ['6', 'six'])],
  [('How many cents is one penny worth?', ['1', '5', '10', '2'], 0),
   ('How many cents is one nickel worth?', ['5', '1', '10', '50'], 0),
   ('If you have 2 pennies, how many cents do you have?', ['2', '1', '5', '10'], 0),
   ('If you have 1 nickel and 2 pennies, how many cents do you have in total?', ['7', '5', '6', '2'], 0),
   ('Which coin is worth more, a nickel or a penny?', ['Nickel', 'Penny', 'They are equal', 'Cannot tell'], 0)])

d73_sci = sub('Science', 'Arctic Animals: Living in the Cold',
  'Students learn that the Arctic is a very cold habitat, and that animals such as polar bears, seals, and arctic foxes have thick fur or fat to help them stay warm.',
  [('Is the Arctic usually a very cold place or a very hot place?', ['cold', 'very cold']),
   ('Name one animal that lives in the Arctic, like a polar bear or seal.', ['polar bear', 'seal', 'arctic fox']),
   ('Does thick fur help an Arctic animal stay warm?', ['yes'])],
  [('Is the Arctic usually a very cold place or a very hot place?', ['Very cold', 'Very hot', 'Warm', 'Rainy'], 0),
   ('Which animal is well known for living in the Arctic?', ['Polar bear', 'Camel', 'Monkey', 'Parrot'], 0),
   ('What helps many Arctic animals stay warm?', ['Thick fur or fat', 'Thin feathers', 'Wet skin', 'Nothing at all'], 0),
   ('Which of these is also an Arctic animal?', ['Seal', 'Desert cactus', 'Rainforest parrot', 'Farm cow'], 0),
   ('Why are Arctic animals specially suited to their habitat?', ['Their bodies help them survive the cold', 'They do not need to survive the cold', 'The Arctic is always warm', 'Arctic animals prefer heat'], 0)])

d73_ss = sub('SocialStudies', 'Our Recycling Centre: Where Bottles and Cans Go',
  'Students learn about the recycling centre, a place in the community where bottles, cans, and paper are collected and turned into new materials instead of becoming trash.',
  [('Name one item that might go to a recycling centre, like a bottle or can.', ['bottle', 'can', 'paper']),
   ('What happens to items at a recycling centre instead of becoming trash?', ['turned into new materials', 'recycled', 'made into new things']),
   ('Is recycling bottles and cans helpful for our earth?', ['yes'])],
  [('What is a recycling centre?', ['A place where items like bottles and cans are collected to be reused', 'A place that sells bread', 'A place that delivers mail', 'A place that fights fires'], 0),
   ('Which of these items might go to a recycling centre?', ['A glass bottle', 'A banana peel', 'A fallen leaf', 'A puddle of water'], 0),
   ('What happens to materials sent to a recycling centre?', ['They are turned into new materials', 'They disappear forever', 'They are always thrown away', 'Nothing happens to them'], 0),
   ('Why is recycling helpful to our community and earth?', ['It reduces waste and reuses materials', 'It creates more trash', 'It harms the earth', 'It has no effect at all'], 0),
   ('Sorting bottles, cans, and paper for recycling is an example of ___.', ['Caring for our environment', 'Ignoring our environment', 'Wasting resources', 'Harming nature'], 0)])

# ─── DAY 74 ─────────────────────────────────────────────────────────────────
d74_lang = sub('Language', 'Word Families: -at Words',
  'Students explore the -at word family, learning that changing the first letter of words like cat, hat, and mat creates new rhyming words that share the same ending sound.',
  [('Change the c in cat to h. What new word do you make?', ['hat']),
   ('Change the h in hat to m. What new word do you make?', ['mat']),
   ('Name one more word that rhymes with cat, hat, and mat.', ['bat', 'sat', 'rat', 'fat', 'pat'])],
  [('Which word rhymes with cat?', ['Hat', 'Dog', 'Sun', 'Pig'], 0),
   ('Change the c in cat to m. What new word do you make?', ['Mat', 'Cap', 'Man', 'Mad'], 0),
   ('Which of these words is part of the -at word family?', ['Sat', 'Sun', 'Six', 'Sit'], 0),
   ('A word family is a group of words that share the same ___.', ['Ending sound', 'Colour', 'Number of letters', 'Meaning'], 0),
   ('Which word does not belong in the -at word family?', ['Dog', 'Bat', 'Hat', 'Rat'], 0)])

d74_math = sub('Math', 'Capacity: Full, Empty, and Half Full',
  'Students compare containers by how much they hold, learning to describe them as full, empty, or half full, and explore which containers hold more or less.',
  [('What word describes a cup with no water in it at all?', ['empty']),
   ('What word describes a cup filled all the way to the top?', ['full']),
   ('What word describes a cup filled only partway, about to the middle?', ['half full'])],
  [('What word describes a cup with no water in it?', ['Empty', 'Full', 'Half full', 'Heavy'], 0),
   ('What word describes a cup filled all the way to the top?', ['Full', 'Empty', 'Light', 'Half full'], 0),
   ('What word describes a cup filled only partway, about to the middle?', ['Half full', 'Full', 'Empty', 'Tiny'], 0),
   ('Which container likely holds more water, a small cup or a large bucket?', ['A large bucket', 'A small cup', 'They hold the same', 'Neither holds water'], 0),
   ('Capacity describes how much a container can ___.', ['Hold', 'Weigh', 'Cost', 'Smell'], 0)])

d74_sci = sub('Science', 'Spiders: Eight Legs and Webs',
  'Students learn that spiders have eight legs, unlike insects which have six, and that many spiders spin silky webs to catch food.',
  [('How many legs does a spider have?', ['8', 'eight']),
   ('How many legs does an insect have?', ['6', 'six']),
   ('What do many spiders spin to catch food?', ['web', 'a web'])],
  [('How many legs does a spider have?', ['8', '6', '4', '2'], 0),
   ('How many legs does an insect have?', ['6', '8', '4', '2'], 0),
   ('What do many spiders spin to catch food?', ['A web', 'A nest', 'A shell', 'A cocoon'], 0),
   ('Is a spider an insect?', ['No, it has more legs than an insect', 'Yes, it is exactly the same as an insect', 'Spiders have no legs', 'Insects have more legs than spiders'], 0),
   ('Why do spiders spin webs?', ['To catch food', 'To fly', 'To swim', 'To make honey'], 0)])

d74_ss = sub('SocialStudies', 'Our Local Park: Where Neighbours Gather',
  'Students learn about the local park as a shared community space where neighbours can play, relax, and gather together outdoors.',
  [('Name one thing you might do at a local park, like play or relax.', ['play', 'relax', 'gather']),
   ('Is a park a place shared by many neighbours, or owned by just one family?', ['shared by many neighbours', 'shared']),
   ('Should we take care of our local park so everyone can enjoy it?', ['yes'])],
  [('What is a local park?', ['A shared outdoor space where neighbours can gather', 'A place that only one family may use', 'A kind of store', 'A place with no outdoor space'], 0),
   ('Which of these might you do at a local park?', ['Play and relax with neighbours', 'Buy groceries', 'Mail a letter', 'Visit the dentist'], 0),
   ('Why is it important to take care of a local park?', ['So everyone in the community can enjoy it', 'Parks do not need care', 'Only one person uses a park', 'Parks are never shared'], 0),
   ('A local park is an example of a space shared by the ___.', ['Community', 'Ocean', 'Desert', 'Moon'], 0),
   ('Which of these shows good behaviour at a local park?', ['Cleaning up after yourself and sharing space', 'Littering on the grass', 'Ignoring other visitors rudely', 'Damaging the playground equipment'], 0)])

# ─── DAY 75 ─────────────────────────────────────────────────────────────────
d75_lang = sub('Language', 'Word Families: -an Words',
  'Students explore the -an word family, learning that changing the first letter of words like can, man, and fan creates new rhyming words that share the same ending sound.',
  [('Change the c in can to m. What new word do you make?', ['man']),
   ('Change the m in man to f. What new word do you make?', ['fan']),
   ('Name one more word that rhymes with can, man, and fan.', ['pan', 'ran', 'tan', 'van'])],
  [('Which word rhymes with can?', ['Man', 'Dog', 'Cup', 'Pig'], 0),
   ('Change the m in man to f. What new word do you make?', ['Fan', 'Fat', 'Fun', 'Fin'], 0),
   ('Which of these words is part of the -an word family?', ['Ran', 'Run', 'Red', 'Rid'], 0),
   ('Words in the same word family share the same ___.', ['Ending sound', 'Author', 'Cover colour', 'Page number'], 0),
   ('Which word does not belong in the -an word family?', ['Cup', 'Can', 'Man', 'Pan'], 0)])

d75_math = sub('Math', 'Data: Picture Graphs',
  'Students learn to read a simple picture graph, where each picture or symbol represents one item, and use it to count and compare groups of objects.',
  [('On a picture graph, does each picture usually stand for one item?', ['yes']),
   ('If a row has 4 apple pictures, how many apples does that row show?', ['4', 'four']),
   ('What do we call a graph that uses pictures to show information?', ['picture graph'])],
  [('On a picture graph, what does each picture usually represent?', ['One item', 'Ten items', 'Nothing', 'A colour'], 0),
   ('If a row on a picture graph has 5 star pictures, how many stars does it show?', ['5', '4', '6', '1'], 0),
   ('What is a picture graph used for?', ['Showing and comparing information with pictures', 'Telling time', 'Measuring weight', 'Naming shapes'], 0),
   ('On a picture graph, which row shows more items, one with 3 pictures or one with 6 pictures?', ['The row with 6 pictures', 'The row with 3 pictures', 'They are equal', 'Cannot tell'], 0),
   ('A picture graph helps us ___ groups of objects.', ['Compare and count', 'Cook', 'Paint', 'Sing about'], 0)])

d75_sci = sub('Science', 'The Water Cycle: Rain, Clouds, and Evaporation',
  'Students learn the simple steps of the water cycle, where the sun warms water and turns it into vapour that rises to form clouds, which later fall back down as rain.',
  [('What warms water and turns it into vapour that rises up?', ['sun', 'the sun']),
   ('What forms in the sky when water vapour rises up?', ['clouds']),
   ('What falls from clouds back down to the ground?', ['rain'])],
  [('What warms water and turns it into vapour that rises up?', ['The sun', 'The moon', 'The wind', 'The snow'], 0),
   ('What forms in the sky when water vapour rises up?', ['Clouds', 'Rocks', 'Sand', 'Ice cream'], 0),
   ('What falls from clouds back down to the ground?', ['Rain', 'Fire', 'Sand', 'Leaves'], 0),
   ('What do we call these repeating steps of water moving between the ground, air, and clouds?', ['The water cycle', 'The rock cycle', 'The food chain', 'The seasons'], 0),
   ('Why is the water cycle important?', ['It brings fresh water back to the earth again and again', 'It removes all water from the earth', 'It never repeats', 'It has nothing to do with rain'], 0)])

d75_ss = sub('SocialStudies', 'Being a Good Sport: Winning and Losing Kindly',
  'Students learn what it means to be a good sport, such as congratulating others after a game, staying calm when losing, and celebrating kindly when winning.',
  [('What word describes someone who plays fair and is kind whether they win or lose?', ['good sport']),
   ('Should you say well done to a friend who won a game?', ['yes']),
   ('Is it kind or unkind to brag loudly after winning a game?', ['unkind'])],
  [('What does it mean to be a good sport?', ['Being kind and fair whether you win or lose', 'Only being kind when you win', 'Yelling at others when you lose', 'Never playing games'], 0),
   ('What should you say to a friend who won a game?', ['Well done or congratulations', 'Nothing at all', 'Something unkind', 'You are not a winner'], 0),
   ('Is it kind or unkind to brag loudly after winning a game?', ['Unkind', 'Kind', 'Neither kind nor unkind', 'Always required'], 0),
   ('How should a good sport act after losing a game?', ['Stay calm and congratulate the winner', 'Cry and refuse to play again', 'Yell at the winner', 'Break the game pieces'], 0),
   ('Being a good sport helps friends feel ___ during games.', ['Respected and included', 'Ignored', 'Embarrassed', 'Left out'], 0)])

# ─── DAY 76 ─────────────────────────────────────────────────────────────────
d76_lang = sub('Language', 'Punctuation: Exclamation Marks for Excitement',
  'Students learn that an exclamation mark is used at the end of a sentence to show strong feeling or excitement, such as Wow! or Look out!, instead of a calm period.',
  [('What punctuation mark shows excitement at the end of a sentence?', ['exclamation mark']),
   ('Does the sentence Wow, look at that! sound calm or excited?', ['excited']),
   ('Which is more calm: a period or an exclamation mark?', ['period'])],
  [('What punctuation mark shows strong feeling or excitement?', ['Exclamation mark', 'Period', 'Comma', 'Question mark'], 0),
   ('Which of these sentences would likely end with an exclamation mark?', ['Watch out for that ball!', 'I like apples.', 'She is reading.', 'The sky is blue.'], 0),
   ('A period usually ends a sentence that sounds ___.', ['Calm and telling', 'Excited and shouting', 'Confused', 'Musical'], 0),
   ('Which punctuation mark would best end an excited sentence like We won the game?', ['Exclamation mark', 'Comma', 'Nothing at all', 'Semicolon'], 0),
   ('Exclamation marks help readers know a sentence should sound ___.', ['Excited', 'Sleepy', 'Silent', 'Confusing'], 0)])

d76_math = sub('Math', 'Missing Numbers: Filling in the Gaps to 20',
  'Students practise finding a missing number in a short counting sequence up to 20, such as figuring out the number that belongs between 7 and 9.',
  [('What number is missing between 7 and 9?', ['8', 'eight']),
   ('What number is missing between 14 and 16?', ['15', 'fifteen']),
   ('What number is missing between 18 and 20?', ['19', 'nineteen'])],
  [('What number is missing between 7 and 9?', ['8', '7', '9', '10'], 0),
   ('What number is missing between 14 and 16?', ['15', '14', '16', '13'], 0),
   ('What number is missing between 3 and 5?', ['4', '3', '5', '6'], 0),
   ('What number is missing between 18 and 20?', ['19', '18', '20', '17'], 0),
   ('Finding a missing number in a sequence means figuring out the number that fits ___.', ['In order between the other numbers', 'At the very end only', 'Nowhere at all', 'Before the sequence starts'], 0)])

d76_sci = sub('Science', 'Magnifying Glasses: Looking Closely at Small Things',
  'Students learn that a magnifying glass is a tool with a curved piece of glass that makes small objects look bigger, helping scientists observe tiny details.',
  [('What tool makes small objects look bigger?', ['magnifying glass']),
   ('Would a magnifying glass help you see the tiny hairs on a leaf?', ['yes']),
   ('What word describes looking closely at something to learn about it?', ['observing', 'observation'])],
  [('What tool makes small objects look bigger?', ['A magnifying glass', 'A hammer', 'A paintbrush', 'A spoon'], 0),
   ('Why might a scientist use a magnifying glass?', ['To see small details more clearly', 'To make things smaller', 'To make loud sounds', 'To measure weight'], 0),
   ('Which of these might you look at closely with a magnifying glass?', ['A tiny insect', 'A whole mountain', 'The entire sky', 'A large lake'], 0),
   ('What word describes looking closely and carefully to learn about something?', ['Observing', 'Sleeping', 'Forgetting', 'Guessing without looking'], 0),
   ('A magnifying glass uses curved glass to make things appear ___.', ['Bigger', 'Smaller', 'Invisible', 'Colder'], 0)])

d76_ss = sub('SocialStudies', 'Community Helpers: Veterinarians Caring for Animals',
  'Students learn about the job of a veterinarian, a community helper who checks on pets and other animals to keep them healthy when they are sick or hurt.',
  [('Who checks on pets and animals to keep them healthy?', ['veterinarian', 'vet']),
   ('Name one animal a veterinarian might help, like a dog or cat.', ['dog', 'cat', 'pet']),
   ('Does a veterinarian help animals when they are sick or hurt?', ['yes'])],
  [('Who checks on pets and animals to keep them healthy?', ['A veterinarian', 'A baker', 'A postal worker', 'A librarian'], 0),
   ('Which of these might a veterinarian help?', ['A sick dog', 'A broken chair', 'A leaking pipe', 'A burnt cake'], 0),
   ('Why is a veterinarian an important community helper?', ['They help keep animals healthy', 'They deliver mail', 'They bake bread', 'They fight fires'], 0),
   ('Where might you take a sick pet for help?', ['A veterinarian office', 'A bakery', 'A firehall', 'A post office'], 0),
   ('A veterinarian is similar to a doctor, but they help ___.', ['Animals', 'Only plants', 'Only buildings', 'Only cars'], 0)])

# ─── DAY 77 ─────────────────────────────────────────────────────────────────
d77_lang = sub('Language', 'Fiction and Nonfiction: Real or Make-Believe',
  'Students learn that fiction stories are make-believe, with events and characters that are not real, while nonfiction books give true facts about real people, places, or things.',
  [('Does a fiction story tell about real events or make-believe events?', ['make-believe', 'make believe']),
   ('Does a nonfiction book give true facts or make-believe stories?', ['true facts', 'facts']),
   ('Is a book about talking animals wearing hats fiction or nonfiction?', ['fiction'])],
  [('What kind of story is fiction?', ['A make-believe story', 'A book of true facts', 'A phone book', 'A recipe'], 0),
   ('What kind of book is nonfiction?', ['A make-believe story', 'A book that gives true facts', 'A fairy tale', 'A story about dragons'], 1),
   ('Which of these is most likely a fiction story?', ['A talking dragon who flies to the moon', 'A book about how bees make honey', 'A book about real weather', 'A book about real animals in the ocean'], 0),
   ('Which of these is most likely a nonfiction book?', ['A true book about how plants grow', 'A story about a talking teapot', 'A tale about a flying carpet', 'A story about a dragon and a wizard'], 0),
   ('Knowing if a book is fiction or nonfiction helps readers know if the story is ___.', ['Real or make-believe', 'Long or short', 'Loud or quiet', 'Old or new'], 0)])

d77_math = sub('Math', 'Sorting 2D Shapes by Number of Sides',
  'Students sort a mixed group of 2D shapes, such as triangles, squares, and hexagons, into groups based on how many straight sides each shape has.',
  [('How many sides does a triangle have?', ['3', 'three']),
   ('How many sides does a square have?', ['4', 'four']),
   ('If you sort shapes by number of sides, would a triangle and a hexagon go in the same group?', ['no'])],
  [('How many sides does a triangle have?', ['3', '4', '5', '6'], 0),
   ('How many sides does a square have?', ['4', '3', '5', '6'], 0),
   ('Which shape has the most sides: triangle, square, or hexagon?', ['Hexagon', 'Triangle', 'Square', 'They are equal'], 0),
   ('When sorting shapes by number of sides, which two shapes would go together?', ['Two squares', 'A triangle and a hexagon', 'A circle and a square', 'A square and a hexagon'], 0),
   ('Sorting shapes by number of sides means grouping shapes that ___.', ['Have the same number of straight sides', 'Are the same colour', 'Are the same size', 'Have no sides at all'], 0)])

d77_sci = sub('Science', 'Compost: Turning Food Scraps into Soil',
  'Students learn that compost is made when food scraps, such as fruit peels and vegetable bits, break down over time and turn into rich soil that helps plants grow.',
  [('Name one food scrap that could go into a compost bin, like a fruit peel.', ['fruit peel', 'vegetable bits', 'banana peel']),
   ('What does compost eventually turn into?', ['soil', 'rich soil']),
   ('Does compost help plants grow?', ['yes'])],
  [('What is compost?', ['Food scraps that break down into rich soil', 'A kind of rock', 'A type of animal', 'A weather event'], 0),
   ('Which of these could go into a compost bin?', ['A fruit peel', 'A plastic toy', 'A metal spoon', 'A glass bottle'], 0),
   ('What does compost eventually turn into?', ['Rich soil', 'Water', 'Sand', 'Ice'], 0),
   ('How does compost help plants?', ['It adds helpful nutrients to the soil', 'It removes all nutrients from soil', 'It stops plants from growing', 'It has no effect on plants'], 0),
   ('Making compost instead of throwing food scraps away helps ___.', ['Reduce waste and help the earth', 'Increase waste', 'Harm plants', 'Make more garbage'], 0)])

d77_ss = sub('SocialStudies', 'Our Local Museum: Learning About the Past',
  'Students learn about the museum as a community place that displays old objects and stories, helping visitors learn about history and how things used to be.',
  [('What kind of place displays old objects and stories about history?', ['museum']),
   ('Can a museum help us learn about how things used to be long ago?', ['yes']),
   ('Name one thing you might see at a museum, like an old object.', ['old object', 'artifact', 'old tool'])],
  [('What is a museum?', ['A place that displays old objects and stories about history', 'A place that sells bread', 'A place that delivers mail', 'A place that fights fires'], 0),
   ('Why might a family visit a museum?', ['To learn about history and the past', 'To buy groceries', 'To mail a letter', 'To see a doctor'], 0),
   ('Which of these might you find in a museum?', ['An old object from long ago', 'A fresh loaf of bread', 'A fire truck ready to respond', 'A mailbox'], 0),
   ('A museum helps a community by ___.', ['Teaching people about history', 'Delivering mail', 'Baking bread', 'Fighting fires'], 0),
   ('Learning about the past at a museum helps us understand ___.', ['How things used to be', 'Only the weather today', 'Only future events', 'Nothing useful'], 0)])

# ─── DAY 78 ─────────────────────────────────────────────────────────────────
d78_lang = sub('Language', 'Book Parts: Front Cover, Back Cover, and Pages',
  'Students learn to identify the parts of a book, including the front cover, back cover, and pages in between, and practise handling books carefully.',
  [('What part of a book usually shows the title and a picture?', ['front cover', 'the front cover']),
   ('What part of a book is at the very end?', ['back cover', 'the back cover']),
   ('What do we call the parts of a book that we turn to read the words?', ['pages'])],
  [('What is the front cover of a book?', ['The part that shows the title and a picture', 'The very last page', 'A blank page', 'The spine only'], 0),
   ('What is the back cover of a book?', ['The part at the very end of the book', 'The first page', 'The title only', 'A picture only'], 0),
   ('What do we call the parts inside a book that we turn to read?', ['Pages', 'Covers', 'Titles', 'Spines'], 0),
   ('Why should we handle a book carefully?', ['So the pages and covers do not get damaged', 'Books cannot be damaged', 'Handling does not matter', 'Only new books need care'], 0),
   ('Which part of the book would you look at first to guess what a story is about?', ['The front cover', 'The back cover', 'A random page', 'The spine only'], 0)])

d78_math = sub('Math', 'Time: Reading a Clock to the Half Hour',
  'Students learn to read a simple analog clock to the half hour, recognizing that when the long hand points to the 6, it means thirty minutes past the hour.',
  [('When the long hand points to the 6, how many minutes past the hour is it?', ['30', 'thirty']),
   ('At half past 3, does the short hand point exactly at the 3 or partway between 3 and 4?', ['partway between 3 and 4', 'between 3 and 4']),
   ('What do we call the time when the long hand points to the 6?', ['half past', 'half hour', 'half past the hour'])],
  [('When the long hand points to the 6, how many minutes past the hour is it?', ['30', '15', '45', '60'], 0),
   ('At half past 3, where does the short hand usually point?', ['Partway between 3 and 4', 'Exactly at the 12', 'Exactly at the 6', 'Exactly at the 9'], 0),
   ('What do we call it when the long hand points to the 6?', ['Half past the hour', 'The top of the hour', 'Midnight only', 'Noon only'], 0),
   ('If it is half past 8, which numbers might you see the clock hands near?', ['The 8 and the 6', 'The 12 and the 12', 'The 3 and the 9', 'The 1 and the 1'], 0),
   ('Reading a clock to the half hour helps us know time in steps of ___ minutes.', ['30', '5', '1', '60'], 0)])

d78_sci = sub('Science', 'Nests and Homes: How Animals Build Shelter',
  'Students learn that many animals build or find shelters to live in, such as birds building nests from twigs, beavers building dams, and rabbits digging burrows.',
  [('What do many birds build out of twigs to live in?', ['nest', 'a nest']),
   ('What do beavers build using sticks and mud?', ['dam', 'a dam']),
   ('What do rabbits often dig to make a home?', ['burrow', 'a burrow', 'hole'])],
  [('What do many birds build to live in?', ['A nest', 'A dam', 'A burrow', 'A hive'], 0),
   ('What do beavers build using sticks and mud?', ['A dam', 'A nest', 'A web', 'A shell'], 0),
   ('What do rabbits often dig to make a home?', ['A burrow', 'A nest', 'A dam', 'A web'], 0),
   ('Why do animals build or find shelters?', ['To stay safe and protected from weather and danger', 'Shelters are not useful to animals', 'Animals never need a home', 'To make more noise'], 0),
   ('Which animal is known for building a home from twigs?', ['A bird', 'A fish', 'A snake', 'A worm'], 0)])

d78_ss = sub('SocialStudies', 'Choosing Together: How Groups Decide',
  'Students learn that when a group needs to make a choice, such as picking a class activity, everyone can share their opinion and the group can decide together in a fair way.',
  [('What word describes a group deciding something together fairly?', ['choosing together', 'group decision', 'deciding together']),
   ('Should everyone in a group have a chance to share their opinion before deciding?', ['yes']),
   ('Is it fair for one person to decide everything without asking the group?', ['no'])],
  [('What does it mean for a group to choose together?', ['Everyone shares an opinion and the group decides fairly', 'One person decides for everyone without asking', 'No one is allowed to share ideas', 'The group never makes a choice'], 0),
   ('Why is it helpful to let everyone share their opinion before a group decision?', ['It helps the group make a fair choice everyone can accept', 'Opinions are not helpful', 'Only one opinion should ever be heard', 'Sharing opinions wastes time'], 0),
   ('Which of these shows a fair way for a group to decide?', ['Listening to everyone and choosing together', 'Ignoring everyone but one person', 'Refusing to make a choice at all', 'Arguing without listening'], 0),
   ('If a class wants to pick a game to play together, what is a fair way to decide?', ['Letting everyone share ideas and choosing together', 'Letting only one student choose every time', 'Not playing any games', 'Fighting over the choice'], 0),
   ('Choosing together as a group helps everyone feel ___.', ['Included and heard', 'Left out', 'Ignored', 'Unimportant'], 0)])

# ─── DAY 79 ─────────────────────────────────────────────────────────────────
d79_lang = sub('Language', 'Sight Words: Reading Words We Know by Heart',
  'Students learn that some common words, such as the, and, and see, appear so often in books that readers practise recognizing them instantly, without sounding them out each time.',
  [('Name one common sight word that appears often in books, like the or and.', ['the', 'and', 'see', 'is']),
   ('Do sight words need to be sounded out every single time, or recognized instantly?', ['recognized instantly', 'instantly']),
   ('Why do readers practise sight words often?', ['so they can read them quickly', 'to read faster', 'to recognize them instantly'])],
  [('What is a sight word?', ['A common word readers recognize instantly', 'A word that is never used', 'A word found in only one book', 'A number word'], 0),
   ('Which of these is a common sight word?', ['The', 'Dinosaur', 'Kaleidoscope', 'Hexagon'], 0),
   ('Why do readers practise sight words?', ['So they can read them quickly without sounding them out', 'So they never have to read again', 'Sight words are not useful', 'To make reading slower'], 0),
   ('Which of these words would likely be a sight word because it appears so often?', ['And', 'Rhinoceros', 'Xylophone', 'Astronaut'], 0),
   ('Recognizing sight words instantly helps readers ___.', ['Read more smoothly', 'Forget the story', 'Skip every page', 'Avoid reading altogether'], 0)])

d79_math = sub('Math', 'Ordering Three Numbers: Least to Greatest',
  'Students practise putting a group of three numbers in order from least to greatest, using their knowledge of counting and comparing numbers.',
  [('Put these numbers in order from least to greatest: 5, 2, 8.', ['2, 5, 8', '2 5 8']),
   ('Which number is the least: 10, 3, 7?', ['3', 'three']),
   ('Which number is the greatest: 12, 20, 6?', ['20', 'twenty'])],
  [('Put these numbers in order from least to greatest: 4, 1, 7.', ['1, 4, 7', '7, 4, 1', '4, 1, 7', '1, 7, 4'], 0),
   ('Which number is the least: 9, 2, 6?', ['2', '9', '6', 'They are equal'], 0),
   ('Which number is the greatest: 15, 8, 20?', ['20', '15', '8', 'They are equal'], 0),
   ('Put these numbers in order from least to greatest: 10, 3, 6.', ['3, 6, 10', '10, 6, 3', '6, 3, 10', '3, 10, 6'], 0),
   ('Ordering numbers from least to greatest means starting with the ___ number.', ['Smallest', 'Largest', 'Roundest', 'Loudest'], 0)])

d79_sci = sub('Science', 'Our Tongue: Tasting Sweet, Sour, and Salty',
  'Students learn that the tongue helps us taste different flavours, such as sweet, sour, and salty, and that our sense of taste helps us enjoy and notice our food.',
  [('What body part helps us taste our food?', ['tongue']),
   ('Name one taste our tongue can notice, like sweet or salty.', ['sweet', 'sour', 'salty']),
   ('Is a lemon usually described as tasting sweet or sour?', ['sour'])],
  [('What body part helps us taste food?', ['Tongue', 'Elbow', 'Ear', 'Hair'], 0),
   ('Which of these is a taste our tongue can notice?', ['Sweet', 'Loud', 'Bright', 'Soft'], 0),
   ('Is a lemon usually described as tasting sweet or sour?', ['Sour', 'Sweet', 'Salty', 'Spicy only'], 0),
   ('Is sugar usually described as tasting sweet or sour?', ['Sweet', 'Sour', 'Salty', 'Bitter only'], 0),
   ('Why is our sense of taste helpful?', ['It helps us enjoy and notice different foods', 'Taste is not helpful at all', 'We cannot taste anything', 'Taste only works on rainy days'], 0)])

d79_ss = sub('SocialStudies', 'Being Honest: Telling the Truth',
  'Students learn what it means to be honest, such as telling the truth even when it is hard, and why honesty helps people trust one another.',
  [('What word describes telling the truth?', ['honest', 'honesty']),
   ('If you accidentally break something, should you tell the truth about what happened?', ['yes']),
   ('Does honesty help people trust one another?', ['yes'])],
  [('What does it mean to be honest?', ['Telling the truth', 'Telling made-up stories', 'Hiding what happened', 'Never speaking at all'], 0),
   ('If you accidentally break a toy, what is the honest thing to do?', ['Tell an adult what happened', 'Hide the toy and say nothing', 'Blame someone else', 'Pretend it never happened'], 0),
   ('Why is honesty important between friends?', ['It helps friends trust one another', 'Honesty makes friends distrust each other', 'Honesty is not important', 'Friends should never be honest'], 0),
   ('Which of these shows honesty?', ['Telling the truth even when it is hard', 'Making up a story to avoid trouble', 'Hiding a mistake from everyone', 'Blaming a friend for your mistake'], 0),
   ('Being honest helps build ___ between people.', ['Trust', 'Confusion', 'Distrust', 'Fear'], 0)])

# ─── DAY 80 (Review) ────────────────────────────────────────────────────────
d80_lang = sub('Language', 'Language Review: Digraphs, Word Families, and Books',
  'Students review recent Language skills: digraphs, silent e, adding -ed, word families, exclamation marks, fiction and nonfiction, book parts, and sight words.',
  [('What two letters make one new sound at the start of the word ship?', ['sh']),
   ('Change the c in cat to h. What new word do you make?', ['hat']),
   ('Is a book about talking animals wearing hats fiction or nonfiction?', ['fiction'])],
  [('Which word begins with the digraph sh?', ['Ship', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word rhymes with cat?', ['Hat', 'Dog', 'Sun', 'Pig'], 0),
   ('What punctuation mark shows strong feeling or excitement?', ['Exclamation mark', 'Period', 'Comma', 'Question mark'], 0),
   ('What kind of book is nonfiction?', ['A make-believe story', 'A book that gives true facts', 'A fairy tale', 'A story about dragons'], 1),
   ('What is a sight word?', ['A common word readers recognize instantly', 'A word that is never used', 'A word found in only one book', 'A number word'], 0)])

d80_math = sub('Math', 'Math Review: Counting, Money, and Time',
  'Students review recent Math skills: counting to 100, near doubles, coin values, capacity, picture graphs, missing numbers, sorting shapes, and telling time to the half hour.',
  [('What number comes right after 89?', ['90', 'ninety']),
   ('How many cents is one nickel worth?', ['5', 'five']),
   ('What number is missing between 7 and 9?', ['8', 'eight'])],
  [('What number comes right after 59?', ['60', '59', '61', '58'], 0),
   ('If double 5 is 10, what is 5 plus 6?', ['11', '10', '12', '9'], 0),
   ('What word describes a cup filled all the way to the top?', ['Full', 'Empty', 'Light', 'Half full'], 0),
   ('On a picture graph, what does each picture usually represent?', ['One item', 'Ten items', 'Nothing', 'A colour'], 0),
   ('When the long hand points to the 6, how many minutes past the hour is it?', ['30', '15', '45', '60'], 0)])

d80_sci = sub('Science', 'Science Review: Our Bodies, Habitats, and Nature',
  'Students review recent Science topics: our heart, rainforests, Arctic animals, spiders, the water cycle, magnifying glasses, compost, animal shelters, and our tongue.',
  [('What body part pumps blood through our body?', ['heart']),
   ('How many legs does a spider have?', ['8', 'eight']),
   ('What falls from clouds back down to the ground?', ['rain'])],
  [('Which animal is well known for living in the rainforest?', ['Monkey', 'Polar bear', 'Camel', 'Penguin'], 0),
   ('Which animal is well known for living in the Arctic?', ['Polar bear', 'Camel', 'Monkey', 'Parrot'], 0),
   ('What do many spiders spin to catch food?', ['A web', 'A nest', 'A shell', 'A cocoon'], 0),
   ('What tool makes small objects look bigger?', ['A magnifying glass', 'A hammer', 'A paintbrush', 'A spoon'], 0),
   ('What body part helps us taste food?', ['Tongue', 'Elbow', 'Ear', 'Hair'], 0)])

d80_ss = sub('SocialStudies', 'Social Studies Review: Helpers, Places, and Kindness',
  'Students review recent Social Studies topics: dentists, banks, recycling centres, local parks, good sportsmanship, veterinarians, museums, group choices, and honesty.',
  [('Who checks and helps keep our teeth healthy?', ['dentist']),
   ('Who checks on pets and animals to keep them healthy?', ['veterinarian', 'vet']),
   ('What word describes telling the truth?', ['honest', 'honesty'])],
  [('What is a place called where people can keep their money safe?', ['A bank', 'A bakery', 'A firehall', 'A library'], 0),
   ('What happens to materials sent to a recycling centre?', ['They are turned into new materials', 'They disappear forever', 'They are always thrown away', 'Nothing happens to them'], 0),
   ('What does it mean to be a good sport?', ['Being kind and fair whether you win or lose', 'Only being kind when you win', 'Yelling at others when you lose', 'Never playing games'], 0),
   ('What is a museum?', ['A place that displays old objects and stories about history', 'A place that sells bread', 'A place that delivers mail', 'A place that fights fires'], 0),
   ('What does it mean to be honest?', ['Telling the truth', 'Telling made-up stories', 'Hiding what happened', 'Never speaking at all'], 0)])


g0_71_80 = [
    day(71, [d71_lang, d71_math, d71_sci, d71_ss]),
    day(72, [d72_lang, d72_math, d72_sci, d72_ss]),
    day(73, [d73_lang, d73_math, d73_sci, d73_ss]),
    day(74, [d74_lang, d74_math, d74_sci, d74_ss]),
    day(75, [d75_lang, d75_math, d75_sci, d75_ss]),
    day(76, [d76_lang, d76_math, d76_sci, d76_ss]),
    day(77, [d77_lang, d77_math, d77_sci, d77_ss]),
    day(78, [d78_lang, d78_math, d78_sci, d78_ss]),
    day(79, [d79_lang, d79_math, d79_sci, d79_ss]),
    day(80, [d80_lang, d80_math, d80_sci, d80_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_71_80)
    append_worksheet_days(0, g0_71_80)
