#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 61-70 -- fourth and FINAL batch extending
Grade 0 past the Days 51-60 batch, completing Days 1-70. This is a
self-contained script (does NOT use gen_curriculum.py's sub()/day()/
append_to() helpers, since those do not support a worksheet field) modeled
exactly on gen_grade0_days51_60.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-60 topics (see data/grade0.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260823):
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


# ─── DAY 61 ─────────────────────────────────────────────────────────────────
d61_lang = sub('Language', 'Letter Sounds Review: Consonant Blends',
  'Students learn that two consonants can blend together at the start of a word, such as bl in black or st in stop, and practise hearing both sounds.',
  [('What two letters blend together at the start of the word stop?', ['st']),
   ('What two letters blend together at the start of the word black?', ['bl']),
   ('Say the word flag. What two letters blend at the start?', ['fl'])],
  [('Which word begins with the blend st?', ['Cat', 'Stop', 'Dog', 'Run'], 1),
   ('Which word begins with the blend bl?', ['Black', 'Sun', 'Pig', 'Hat'], 0),
   ('In the word flag, which two letters blend together?', ['Ag', 'La', 'Fl', 'Gl'], 2),
   ('A consonant blend is when two consonant letters ___.', ['Are silent', 'Blend their sounds together', 'Turn into vowels', 'Are never used'], 1),
   ('Which word begins with the blend gr?', ['Green', 'Top', 'Man', 'Sit'], 0)])

d61_math = sub('Math', 'Number Words 11 to 20',
  'Students learn to read and match the written number words for eleven through twenty, such as eleven, fifteen, and twenty, to their matching numerals.',
  [('Write the number word for 11.', ['eleven']),
   ('Write the number word for 15.', ['fifteen']),
   ('Write the number word for 20.', ['twenty'])],
  [('Which number word matches the numeral 12?', ['Twelve', 'Two', 'Twenty', 'Ten'], 0),
   ('Which number word matches the numeral 16?', ['Six', 'Sixty', 'Sixteen', 'Ten'], 2),
   ('Which numeral matches the word nineteen?', ['9', '90', '19', '91'], 2),
   ('Which number word matches the numeral 20?', ['Twelve', 'Two', 'Twenty', 'Ten'], 2),
   ('Which numeral matches the word eleven?', ['1', '11', '10', '111'], 1)])

d61_sci = sub('Science', 'Our Eyes: Seeing Colours and Shapes',
  'Students learn that eyes help us see colours, shapes, and light, and explore how our two eyes work together to help us see the world around us.',
  [('What body part do we use to see?', ['eyes']),
   ('How many eyes do most people have?', ['2', 'two']),
   ('Name one colour your eyes can help you see, like red or blue.', ['red', 'blue', 'green', 'yellow'])],
  [('What body part helps us see colours and shapes?', ['Ears', 'Eyes', 'Nose', 'Elbow'], 1),
   ('How many eyes does a person usually have?', ['1', '2', '3', '4'], 1),
   ('Which of these can our eyes help us notice?', ['Colours and shapes', 'Sounds only', 'Smells only', 'Tastes only'], 0),
   ('Why do we have two eyes instead of one?', ['They work together to help us see well', 'Two eyes are not useful', 'Eyes do not help us see', 'Only one eye is ever used'], 0),
   ('Which of these would you use your eyes to notice?', ['A bright red ball', 'A loud drum', 'A sweet smell', 'A soft touch'], 0)])

d61_ss = sub('SocialStudies', 'Our Postal Worker: Delivering Mail',
  'Students learn about the job of a postal worker, who delivers letters and packages to homes and businesses in the community every day.',
  [('What does a postal worker deliver to our homes?', ['mail', 'letters', 'packages']),
   ('Name one thing a postal worker might carry, like a letter or package.', ['letter', 'package', 'mail']),
   ('Does a postal worker help our community by delivering mail?', ['yes'])],
  [('What does a postal worker deliver?', ['Mail and packages', 'Food only', 'Water only', 'Toys only'], 0),
   ('Where might a postal worker deliver mail?', ['To homes and businesses', 'Only to the moon', 'Nowhere at all', 'Only to farms'], 0),
   ('Why is the job of a postal worker helpful to a community?', ['It helps people send and receive mail', 'It is not helpful', 'Mail is never needed', 'Only businesses need mail'], 0),
   ('Which of these is something a postal worker might wear or use?', ['A mail bag', 'A stethoscope', 'A chef hat', 'A fire hose'], 0),
   ('A postal worker is an example of a ___.', ['Wild animal', 'Community helper', 'Story character', 'Weather tool'], 1)])

# ─── DAY 62 ─────────────────────────────────────────────────────────────────
d62_lang = sub('Language', 'Ending Blends: Two Sounds at the End',
  'Students learn that two consonants can blend together at the end of a word, such as nd in hand or st in fast, and practise hearing both ending sounds.',
  [('What two letters blend together at the end of the word hand?', ['nd']),
   ('What two letters blend together at the end of the word fast?', ['st']),
   ('Say the word jump. What two letters blend at the end?', ['mp'])],
  [('Which word ends with the blend nd?', ['Hand', 'Cat', 'Sun', 'Pig'], 0),
   ('Which word ends with the blend st?', ['Fast', 'Top', 'Run', 'Sit'], 0),
   ('In the word jump, which two letters blend together at the end?', ['Ju', 'Mp', 'Um', 'Pj'], 1),
   ('An ending blend is when two consonant letters ___.', ['Are always silent', 'Blend their sounds together at the end of a word', 'Turn into numbers', 'Are never used'], 1),
   ('Which word ends with the blend lt?', ['Belt', 'Sun', 'Man', 'Top'], 0)])

d62_math = sub('Math', 'Number Bonds to 20',
  'Students explore pairs of numbers that combine to make 20, such as 10 and 10 or 15 and 5, building on earlier number bond work within 10.',
  [('What number added to 10 makes 20?', ['10', 'ten']),
   ('What number added to 15 makes 20?', ['5', 'five']),
   ('What number added to 18 makes 20?', ['2', 'two'])],
  [('What number added to 10 makes 20?', ['5', '10', '15', '20'], 1),
   ('What number added to 15 makes 20?', ['3', '4', '5', '6'], 2),
   ('What number added to 12 makes 20?', ['6', '7', '8', '9'], 2),
   ('A number bond shows how two numbers ___.', ['Combine to make a total', 'Cancel each other out', 'Are always equal', 'Are never related'], 0),
   ('What number added to 19 makes 20?', ['0', '1', '2', '3'], 1)])

d62_sci = sub('Science', 'Animal Coverings: Fur, Feathers, and Scales',
  'Students sort animals by the type of covering on their body, such as fur on a dog, feathers on a bird, or scales on a fish, and learn each covering helps the animal in different ways.',
  [('What covers most of a dog body?', ['fur']),
   ('What covers most of a bird body?', ['feathers']),
   ('What covers most of a fish body?', ['scales'])],
  [('What covering does a dog usually have?', ['Scales', 'Fur', 'Feathers', 'Shell'], 1),
   ('What covering does a bird usually have?', ['Fur', 'Feathers', 'Scales', 'Shell'], 1),
   ('What covering does a fish usually have?', ['Feathers', 'Fur', 'Scales', 'Shell'], 2),
   ('Which animal covering helps keep a dog warm?', ['Fur', 'Scales', 'A shell', 'Feathers'], 0),
   ('Why do different animals have different coverings?', ['Coverings help each animal survive in its own way', 'Coverings do not matter', 'All animals have the same covering', 'Coverings are only for decoration'], 0)])

d62_ss = sub('SocialStudies', 'Our Firehall: Where Firefighters Work',
  'Students learn about the firehall as a special building in the community where firefighters work, sleep, and keep their fire trucks ready to help.',
  [('What is the name of the building where firefighters work?', ['firehall', 'fire hall', 'fire station']),
   ('What big vehicle do firefighters keep ready at the firehall?', ['fire truck']),
   ('Do firefighters live and sleep at the firehall while on duty?', ['yes'])],
  [('What is the building called where firefighters work?', ['Firehall', 'Library', 'Bakery', 'Farm'], 0),
   ('What vehicle is kept ready at the firehall?', ['A fire truck', 'A school bus', 'A boat', 'A bicycle'], 0),
   ('Why do firefighters keep their truck and gear ready at all times?', ['So they can respond quickly to emergencies', 'They never need to respond quickly', 'The truck is just for show', 'Firefighters do not use trucks'], 0),
   ('Which of these might you see at a firehall?', ['A fire truck and hoses', 'A cash register', 'A blackboard', 'A garden hose reel only'], 0),
   ('A firehall is an important part of our ___.', ['Ocean', 'Community', 'Forest', 'Desert'], 1)])

# ─── DAY 63 ─────────────────────────────────────────────────────────────────
d63_lang = sub('Language', 'Making New Words: Adding an S',
  'Students learn that adding the letter s to the end of many words makes them mean more than one, such as changing cat to cats or dog to dogs.',
  [('Add an s to the word cat. What new word do you make?', ['cats']),
   ('Add an s to the word dog. What new word do you make?', ['dogs']),
   ('Does the word cats mean one cat or more than one cat?', ['more than one'])],
  [('Add an s to the word hat. What new word do you make?', ['Hats', 'Hate', 'Has', 'Hate'], 0),
   ('Which word means more than one book?', ['Book', 'Books', 'Booked', 'Booking'], 1),
   ('Adding an s to the end of a word usually shows that there is ___.', ['Only one', 'More than one', 'None at all', 'A colour'], 1),
   ('Which of these words already means more than one?', ['Toys', 'Toy', 'Toying', 'Toyed'], 0),
   ('Add an s to the word bird. What new word do you make?', ['Birds', 'Bird', 'Birde', 'Birdy'], 0)])

d63_math = sub('Math', 'Counting to 50',
  'Students practise counting aloud from 1 to 50 by ones, and recognize written numerals up to 50, extending their counting range beyond 30.',
  [('What number comes right after 29?', ['30', 'thirty']),
   ('What number comes right after 39?', ['40', 'forty']),
   ('What number comes right after 49?', ['50', 'fifty'])],
  [('What number comes right after 29?', ['28', '29', '30', '31'], 2),
   ('What number comes right after 39?', ['38', '39', '40', '41'], 2),
   ('Which number is greater, 42 or 24?', ['24', '42', 'They are equal', 'Cannot tell'], 1),
   ('What number comes right before 50?', ['48', '49', '50', '51'], 1),
   ('Counting from 1 to 50 means we say each number ___.', ['In order, one at a time', 'Backward only', 'Twice each', 'In random order'], 0)])

d63_sci = sub('Science', 'Fruits and Vegetables: Eating the Rainbow',
  'Students sort common fruits and vegetables by colour, such as red apples, orange carrots, and green broccoli, and learn that eating many colours helps keep our bodies healthy.',
  [('Name one fruit that is red, like an apple.', ['apple']),
   ('Name one vegetable that is orange, like a carrot.', ['carrot']),
   ('Is broccoli usually green or purple?', ['green'])],
  [('Which of these fruits is usually red?', ['Apple', 'Banana', 'Broccoli', 'Carrot'], 0),
   ('Which of these vegetables is usually orange?', ['Broccoli', 'Carrot', 'Grape', 'Spinach'], 1),
   ('What colour is broccoli usually?', ['Purple', 'Green', 'Orange', 'Red'], 1),
   ('Why is it healthy to eat fruits and vegetables of many colours?', ['Different colours give our bodies different helpful nutrients', 'Colour does not matter for health', 'Only one colour of food is healthy', 'Fruits and vegetables are not healthy'], 0),
   ('Which of these is a fruit?', ['Banana', 'Carrot', 'Potato', 'Broccoli'], 0)])

d63_ss = sub('SocialStudies', 'Our Grocery Store: Where Food Comes From',
  'Students learn about the grocery store as a community place where families go to buy food and other everyday items they need.',
  [('Where do many families go to buy food?', ['grocery store', 'the grocery store']),
   ('Name one item you might buy at a grocery store, like milk or bread.', ['milk', 'bread', 'apples', 'fruit']),
   ('Do people usually pay for the items they take home from a grocery store?', ['yes'])],
  [('Where do many families buy food?', ['A grocery store', 'A firehall', 'A library', 'A park'], 0),
   ('Which of these might you buy at a grocery store?', ['Milk', 'A fire truck', 'A library book', 'A mailbox'], 0),
   ('What do people usually do before taking items home from a store?', ['Pay for them', 'Leave without paying', 'Break them', 'Hide them'], 0),
   ('Why is a grocery store helpful to a community?', ['It gives people a place to buy the food they need', 'It is not helpful', 'Food is never needed', 'Grocery stores sell no food'], 0),
   ('Who works at a grocery store to help customers?', ['Cashiers and store workers', 'Firefighters only', 'Pilots only', 'Doctors only'], 0)])

# ─── DAY 64 ─────────────────────────────────────────────────────────────────
d64_lang = sub('Language', 'Story Titles: What a Book Is Called',
  'Students learn that the title of a book is its name, usually found on the cover, and practise identifying and talking about story titles.',
  [('What word describes the name of a book?', ['title']),
   ('Where on a book do you usually find the title?', ['cover', 'the cover', 'front cover']),
   ('Can two different books ever have the same title?', ['yes'])],
  [('What is the title of a book?', ['The last page', 'The name of the book', 'A character', 'The setting'], 1),
   ('Where is the title of a book usually found?', ['On the cover', 'On the very last page', 'Nowhere', 'Inside a drawer'], 0),
   ('Why is a title helpful when choosing a book?', ['It tells us the name of the book', 'It tells us the weather', 'It tells us a phone number', 'Titles are not helpful'], 0),
   ('Which of these could be a book title?', ['The Little Red Hen', 'A page number', 'A blank space', 'A staple'], 0),
   ('The title of a book is usually written in ___ letters.', ['Invisible', 'Large or bold', 'No letters at all', 'Backward'], 1)])

d64_math = sub('Math', 'Shapes with Many Sides: Pentagon and Hexagon',
  'Students learn to recognize and name shapes with more than four sides, such as a pentagon with five sides and a hexagon with six sides.',
  [('How many sides does a pentagon have?', ['5', 'five']),
   ('How many sides does a hexagon have?', ['6', 'six']),
   ('Which shape has more sides, a pentagon or a hexagon?', ['hexagon'])],
  [('How many sides does a pentagon have?', ['4', '5', '6', '7'], 1),
   ('How many sides does a hexagon have?', ['4', '5', '6', '7'], 2),
   ('Which shape has more sides, a pentagon or a hexagon?', ['Pentagon', 'Hexagon', 'They are equal', 'Cannot tell'], 1),
   ('A shape with five straight sides is called a ___.', ['Hexagon', 'Pentagon', 'Triangle', 'Circle'], 1),
   ('Which of these has six sides?', ['Triangle', 'Square', 'Hexagon', 'Circle'], 2)])

d64_sci = sub('Science', 'Migration: Animals on the Move',
  'Students learn that some animals, such as geese and monarch butterflies, travel long distances called migration to find warmer weather or food during the year.',
  [('What word describes animals travelling long distances to find warmer weather?', ['migration']),
   ('Name one animal that migrates, like a goose or a butterfly.', ['goose', 'geese', 'butterfly', 'monarch butterfly']),
   ('Do migrating animals often move to find warmer weather or food?', ['yes'])],
  [('What is migration?', ['Animals sleeping all winter', 'Animals travelling long distances to find warmer weather or food', 'Animals building nests', 'Animals eating leaves'], 1),
   ('Which of these animals is known for migrating long distances?', ['Monarch butterfly', 'A pet goldfish', 'A house cat', 'A garden worm'], 0),
   ('Why might an animal migrate?', ['To find warmer weather or more food', 'To get lost on purpose', 'Migration has no reason', 'To avoid all food'], 0),
   ('Geese often fly together in a group shape during migration called a ___.', ['Square', 'V shape', 'Circle', 'Straight line only'], 1),
   ('Migration usually happens as the ___ change.', ['Colours of paint', 'Seasons', 'Names of animals', 'Shapes of clouds'], 1)])

d64_ss = sub('SocialStudies', 'Our Bakery: Where Bread Is Made',
  'Students learn about the bakery as a community place where bakers make bread, cakes, and other baked goods for people to buy and enjoy.',
  [('What does a baker make at a bakery, like bread or cake?', ['bread', 'cake', 'baked goods']),
   ('Name one job a baker does, like baking bread.', ['baking bread', 'baking', 'making bread']),
   ('Do people buy baked goods like bread from a bakery?', ['yes'])],
  [('What does a baker make?', ['Bread and baked goods', 'Fire trucks', 'Mail', 'Library books'], 0),
   ('Where might you go to buy fresh bread?', ['A bakery', 'A firehall', 'A library', 'A pond'], 0),
   ('Why is a bakery helpful to a community?', ['It gives people fresh baked food to buy', 'It is not helpful', 'Bread is never needed', 'Bakeries make no food'], 0),
   ('Which of these is something a baker might make?', ['A loaf of bread', 'A fire hose', 'A library card', 'A mailbox'], 0),
   ('A baker is an example of a ___.', ['Wild animal', 'Community helper', 'Weather tool', 'Story setting'], 1)])

# ─── DAY 65 ─────────────────────────────────────────────────────────────────
d65_lang = sub('Language', 'Sentence Types: Telling and Asking',
  'Students learn that some sentences tell us something and end with a period, while other sentences ask a question and end with a question mark.',
  [('Does a telling sentence end with a period or a question mark?', ['period']),
   ('Does an asking sentence end with a period or a question mark?', ['question mark']),
   ('Is the sentence Where is the ball? a telling sentence or an asking sentence?', ['asking sentence', 'asking'])],
  [('What punctuation mark ends a telling sentence?', ['Question mark', 'Period', 'Exclamation mark', 'Comma'], 1),
   ('What punctuation mark ends an asking sentence?', ['Period', 'Question mark', 'Comma', 'Exclamation mark'], 1),
   ('Which of these is an asking sentence?', ['I like dogs.', 'What is your name?', 'The sun is bright.', 'She runs fast.'], 1),
   ('Which of these is a telling sentence?', ['Where is my hat?', 'The cat is sleeping.', 'Do you like cake?', 'Can we go outside?'], 1),
   ('A question mark tells us that a sentence is ___.', ['Asking something', 'Telling something', 'Shouting', 'Singing'], 0)])

d65_math = sub('Math', 'Addition and Subtraction Stories to 10',
  'Students solve simple word problems within 10 by acting them out or drawing pictures, connecting real situations to addition and subtraction.',
  [('You have 3 apples and get 2 more. How many apples do you have now?', ['5', 'five']),
   ('You have 7 crayons and give away 3. How many crayons do you have left?', ['4', 'four']),
   ('You have 4 balloons and get 1 more. How many balloons do you have now?', ['5', 'five'])],
  [('You have 5 stickers and get 3 more. How many stickers do you have now?', ['6', '7', '8', '9'], 2),
   ('You have 9 grapes and eat 4 of them. How many grapes are left?', ['3', '4', '5', '6'], 2),
   ('You have 2 blocks and get 6 more. How many blocks do you have now?', ['6', '7', '8', '9'], 2),
   ('You have 10 marbles and give away 5. How many marbles are left?', ['3', '4', '5', '6'], 2),
   ('A story problem that uses the word altogether usually means you should ___.', ['Subtract', 'Add', 'Multiply', 'Ignore the numbers'], 1)])

d65_sci = sub('Science', 'Bees and Pollination: Helping Flowers Grow',
  'Students learn that bees visit flowers to collect nectar and, in doing so, carry pollen that helps new flowers and fruits grow, a process called pollination.',
  [('What insect helps carry pollen between flowers?', ['bee', 'bees']),
   ('What do bees collect from flowers to make honey?', ['nectar']),
   ('Does pollination help new flowers and fruits grow?', ['yes'])],
  [('Which insect is well known for helping pollinate flowers?', ['Bee', 'Spider', 'Ant', 'Worm'], 0),
   ('What do bees collect from flowers?', ['Nectar', 'Rocks', 'Water only', 'Sand'], 0),
   ('What is pollination?', ['Bees carrying pollen that helps flowers and fruits grow', 'Bees sleeping in winter', 'Bees building fire trucks', 'Bees eating leaves'], 0),
   ('Why are bees important to plants?', ['They help pollinate flowers so fruits can grow', 'Bees do not help plants at all', 'Bees eat all the flowers', 'Bees are not connected to plants'], 0),
   ('What sweet food do bees make using nectar?', ['Honey', 'Bread', 'Juice', 'Jam'], 0)])

d65_ss = sub('SocialStudies', 'Fair Sharing: Splitting Things Equally',
  'Students learn what it means to share fairly, such as splitting a snack or toys equally so that everyone gets a turn or an equal amount.',
  [('If two friends split a snack equally, does each friend get the same amount?', ['yes']),
   ('What word describes giving everyone the same amount or a fair turn?', ['fair', 'fairly', 'sharing fairly']),
   ('Is it fair for one friend to keep everything and give nothing to another?', ['no'])],
  [('If two friends split a snack fairly, what happens?', ['One friend gets everything', 'Each friend gets an equal amount', 'No one gets any snack', 'They fight over it'], 1),
   ('What does it mean to share fairly?', ['Giving everyone an equal or fair amount', 'Keeping everything for yourself', 'Ignoring others', 'Hiding your toys'], 0),
   ('Is it fair for one person to take all the toys and share none?', ['Yes', 'No', 'Sometimes', 'It does not matter'], 1),
   ('Which of these shows fair sharing?', ['Splitting crackers evenly between two friends', 'Taking all the crackers for yourself', 'Throwing the crackers away', 'Hiding the crackers'], 0),
   ('Fair sharing helps friends feel ___.', ['Left out', 'Happy and included', 'Angry', 'Ignored'], 1)])

# ─── DAY 66 ─────────────────────────────────────────────────────────────────
d66_lang = sub('Language', 'Making New Words: Adding -ing',
  'Students learn that adding -ing to the end of an action word shows that the action is happening right now, such as changing jump to jumping.',
  [('Add -ing to the word jump. What new word do you make?', ['jumping']),
   ('Add -ing to the word run. What new word do you make?', ['running']),
   ('Does the word jumping show an action happening right now or an action from long ago?', ['right now', 'now'])],
  [('Add -ing to the word walk. What new word do you make?', ['Walked', 'Walking', 'Walks', 'Walker'], 1),
   ('Which word shows an action happening right now?', ['Played', 'Playing', 'Plays', 'Play'], 1),
   ('Adding -ing to an action word usually shows that the action is ___.', ['Finished long ago', 'Happening right now', 'Never going to happen', 'A noun'], 1),
   ('Add -ing to the word sing. What new word do you make?', ['Singing', 'Sings', 'Sang', 'Singer'], 0),
   ('Which of these words already ends in -ing?', ['Reading', 'Read', 'Reads', 'Reader'], 0)])

d66_math = sub('Math', 'Measurement: Comparing Weight with a Balance',
  'Students use a simple balance scale to compare the weight of two objects, learning that the heavier object makes its side of the balance go down.',
  [('On a balance scale, does the heavier object go up or down?', ['down']),
   ('On a balance scale, does the lighter object go up or down?', ['up']),
   ('If a rock and a feather are on a balance scale, which side goes down?', ['rock', 'the rock side'])],
  [('On a balance scale, which way does the heavier side move?', ['Up', 'Down', 'Sideways', 'It stays still'], 1),
   ('On a balance scale, which way does the lighter side move?', ['Down', 'Up', 'Sideways', 'It stays still'], 1),
   ('If a book and a crayon are on a balance scale, which side likely goes down?', ['The crayon side', 'The book side', 'Neither side moves', 'Both sides go down'], 1),
   ('A balance scale helps us compare two objects by their ___.', ['Colour', 'Weight', 'Smell', 'Sound'], 1),
   ('If both sides of a balance scale are level, the objects are ___.', ['The same weight', 'Different weights', 'Not real', 'Invisible'], 0)])

d66_sci = sub('Science', 'Our Lungs: Breathing In and Out',
  'Students learn that lungs help our body breathe in fresh air and breathe out air we do not need, and practise taking slow, calm breaths.',
  [('What body part helps us breathe?', ['lungs']),
   ('Do we breathe in fresh air using our lungs?', ['yes']),
   ('Name one time you might take slow, calm breaths, like when resting.', ['resting', 'sleeping', 'relaxing', 'calming down'])],
  [('What body part helps us breathe air in and out?', ['Lungs', 'Elbow', 'Knee', 'Hair'], 0),
   ('What do our lungs help us breathe in?', ['Fresh air', 'Water', 'Sand', 'Rocks'], 0),
   ('Taking slow, calm breaths can help our body feel ___.', ['More upset', 'Calm and relaxed', 'Hungry', 'Sleepy only'], 1),
   ('Where are our lungs located in our body?', ['Inside our chest', 'In our feet', 'In our hair', 'Outside our body'], 0),
   ('Why is breathing important for our bodies?', ['It brings fresh air that our body needs', 'Breathing is not important', 'Our body never needs air', 'Only animals need to breathe'], 0)])

d66_ss = sub('SocialStudies', 'Getting to School: Different Ways We Travel',
  'Students compare different ways children get to school, such as walking, riding the bus, biking, or being driven, and discuss safe habits for each.',
  [('Name one way you might get to school, like walking or riding the bus.', ['walking', 'bus', 'biking', 'car']),
   ('Should you wear a helmet if you ride a bike to school?', ['yes']),
   ('Is it safe to look both ways before crossing the street on the way to school?', ['yes'])],
  [('Which of these is a way children might get to school?', ['Riding the bus', 'Flying a plane alone', 'Sailing a boat', 'Riding a horse alone'], 0),
   ('What should you wear if you ride a bike to school?', ['Nothing extra', 'A helmet', 'Sunglasses only', 'Mittens only'], 1),
   ('What should you do before crossing the street on the way to school?', ['Run across quickly', 'Look both ways', 'Close your eyes', 'Ignore traffic'], 1),
   ('Why do different families choose different ways to get to school?', ['Different families have different needs and distances', 'There is only one way to get to school', 'Travel choices never differ', 'Only buses are allowed'], 0),
   ('Which is a safe habit no matter how you travel to school?', ['Following safety rules', 'Ignoring adults', 'Running into traffic', 'Not paying attention'], 0)])

# ─── DAY 67 ─────────────────────────────────────────────────────────────────
d67_lang = sub('Language', 'Story Author and Illustrator',
  'Students learn that the author is the person who writes the words of a book and the illustrator is the person who draws the pictures, and that sometimes one person does both jobs.',
  [('What word describes the person who writes the words of a book?', ['author']),
   ('What word describes the person who draws the pictures in a book?', ['illustrator']),
   ('Can the same person be both the author and the illustrator of a book?', ['yes'])],
  [('What does an author do?', ['Draws the pictures', 'Writes the words of a book', 'Prints the book', 'Sells the book'], 1),
   ('What does an illustrator do?', ['Writes the words', 'Draws the pictures in a book', 'Reads the book aloud', 'Sells the book'], 1),
   ('Can one person be both the author and illustrator of a book?', ['No, never', 'Yes, sometimes', 'Only in some countries', 'Books need no author'], 1),
   ('Where might you find the name of a book author?', ['On the cover', 'Nowhere', 'Only on the last page', 'Books have no author names'], 0),
   ('Why are illustrations helpful in a story?', ['They help show the story with pictures', 'Pictures are never helpful', 'Illustrations replace all the words', 'Only adults need pictures'], 0)])

d67_math = sub('Math', 'Repeating Patterns with Three Elements',
  'Students identify and extend repeating patterns that use three different elements, such as an ABC pattern of circle, square, triangle, circle, square, triangle.',
  [('In the pattern circle, square, triangle, circle, square, ___, what comes next?', ['triangle']),
   ('How many different shapes repeat in an ABC pattern?', ['3', 'three']),
   ('In the pattern red, blue, green, red, blue, ___, what colour comes next?', ['green'])],
  [('In the pattern star, moon, sun, star, moon, ___, what comes next?', ['Star', 'Moon', 'Sun', 'Cloud'], 2),
   ('How many different elements repeat in an ABC pattern?', ['2', '3', '4', '5'], 1),
   ('In the pattern red, blue, green, red, blue, ___, what comes next?', ['Red', 'Blue', 'Green', 'Yellow'], 2),
   ('An ABC pattern repeats in groups of ___.', ['Two', 'Three', 'Four', 'Five'], 1),
   ('In the pattern dog, cat, bird, dog, cat, ___, what comes next?', ['Dog', 'Cat', 'Bird', 'Fish'], 2)])

d67_sci = sub('Science', 'Our Skeleton: Bones That Hold Us Up',
  'Students learn that bones inside our body form a skeleton that helps us stand up, move, and protect important parts like the brain and heart.',
  [('What word describes all the bones inside our body together?', ['skeleton']),
   ('Do bones help our body stand up and move?', ['yes']),
   ('Name one bone-protected body part, like the brain or heart.', ['brain', 'heart'])],
  [('What is a skeleton?', ['A type of food', 'All the bones inside our body', 'A kind of weather', 'A story character'], 1),
   ('What do our bones help us do?', ['Stand up and move', 'Taste food', 'Smell flowers', 'Hear sounds'], 0),
   ('Which body part do our skull bones help protect?', ['Our brain', 'Our toes', 'Our elbow', 'Our hair'], 0),
   ('Without bones, would our body be able to stand up easily?', ['Yes, easily', 'No, it would be much harder', 'Bones do not matter', 'Standing needs no bones'], 1),
   ('Why is it important to take care of our bones?', ['Healthy bones help our body work well', 'Bones do not need care', 'Bones are not important', 'Only adults have bones'], 0)])

d67_ss = sub('SocialStudies', 'Working Together to Solve a Problem',
  'Students learn that a team can often solve a problem better than one person alone, and practise working together on a small classroom task.',
  [('Is it sometimes easier to solve a problem with a team or completely alone?', ['team', 'with a team']),
   ('What word describes people working together toward the same goal?', ['teamwork']),
   ('Should team members listen to each other ideas when solving a problem?', ['yes'])],
  [('Why might a problem be easier to solve with a team?', ['Team members can share ideas and help each other', 'Teams never help', 'One person is always better alone', 'Teams make problems harder'], 0),
   ('What word describes people working together toward a shared goal?', ['Teamwork', 'Selfishness', 'Ignoring', 'Arguing'], 0),
   ('When working in a team, what should members do with each other ideas?', ['Ignore all ideas', 'Listen and consider them', 'Yell over each other', 'Refuse to share'], 1),
   ('Which of these shows good teamwork?', ['Sharing jobs and helping each other', 'Doing everything alone', 'Refusing to help', 'Arguing without listening'], 0),
   ('A team that works well together can often ___.', ['Solve problems more easily', 'Never solve anything', 'Make problems worse', 'Avoid all tasks'], 0)])

# ─── DAY 68 ─────────────────────────────────────────────────────────────────
d68_lang = sub('Language', 'Long Vowel Sounds: Saying the Letter Name',
  'Students learn that a long vowel sound says the letter name, such as the long a in cake or the long o in boat, compared to a short vowel sound.',
  [('Does the word cake have a long a sound or a short a sound?', ['long a', 'long']),
   ('Does the word boat have a long o sound or a short o sound?', ['long o', 'long']),
   ('A long vowel sound says the letter ___.', ['name'])],
  [('Which word has a long a sound?', ['Cat', 'Cake', 'Cap', 'Can'], 1),
   ('Which word has a long o sound?', ['Boat', 'Hot', 'Dog', 'Top'], 0),
   ('A long vowel sound usually says the ___ of the letter.', ['Colour', 'Name', 'Number', 'Shape'], 1),
   ('Which word has a long e sound?', ['Bed', 'Bee', 'Ten', 'Pen'], 1),
   ('Which word has a short vowel sound instead of a long one?', ['Cat', 'Cake', 'Bee', 'Boat'], 0)])

d68_math = sub('Math', 'Position on a Grid: Rows and Columns',
  'Students explore simple grids made of rows and columns, learning to find and describe the position of an object using words like row and column.',
  [('What word describes a line of boxes going across a grid?', ['row']),
   ('What word describes a line of boxes going up and down a grid?', ['column']),
   ('On a grid, do rows go across or up and down?', ['across'])],
  [('What word describes a line of boxes going across a grid?', ['Column', 'Row', 'Circle', 'Corner'], 1),
   ('What word describes a line of boxes going up and down a grid?', ['Row', 'Column', 'Triangle', 'Corner'], 1),
   ('On a grid, do columns go across or up and down?', ['Across', 'Up and down', 'Diagonally', 'Nowhere'], 1),
   ('A grid is made up of ___.', ['Rows and columns', 'Only circles', 'Only triangles', 'Only one line'], 0),
   ('Finding an object on a grid can help us describe its ___.', ['Colour', 'Position', 'Smell', 'Sound'], 1)])

d68_sci = sub('Science', 'Deserts: A Very Dry Habitat',
  'Students learn that a desert is a very dry habitat with little rain, and that some plants and animals, such as cactuses and camels, are specially suited to live there.',
  [('Is a desert a very wet place or a very dry place?', ['dry']),
   ('Name one plant that can live in the desert, like a cactus.', ['cactus']),
   ('Name one animal that can live in the desert, like a camel.', ['camel'])],
  [('Is a desert usually a wet place or a dry place?', ['Wet', 'Dry', 'Neither', 'Both'], 1),
   ('Which plant is specially suited to live in the desert?', ['Cactus', 'Water lily', 'Seaweed', 'Moss'], 0),
   ('Which animal is well known for living in the desert?', ['Camel', 'Polar bear', 'Penguin', 'Whale'], 0),
   ('Why do desert plants like cactuses need less water than other plants?', ['They are specially suited to store water and survive dry conditions', 'They need more water than other plants', 'Deserts have lots of rain', 'Cactuses do not need water at all'], 0),
   ('A desert is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d68_ss = sub('SocialStudies', 'Rules at the Playground: Playing Safely',
  'Students learn simple playground rules that help everyone play safely and fairly, such as taking turns on the slide and not pushing others.',
  [('Should you push other children while playing on the playground?', ['no']),
   ('What should you do while waiting for a turn on the slide?', ['wait', 'take turns', 'wait patiently']),
   ('Do playground rules help keep everyone safe?', ['yes'])],
  [('Should you push other children on the playground?', ['Yes', 'No', 'Only sometimes', 'It does not matter'], 1),
   ('What should you do while waiting for a turn on the slide?', ['Push ahead', 'Wait patiently', 'Yell loudly', 'Climb over others'], 1),
   ('Why do playgrounds have rules?', ['To help keep everyone safe and having fun', 'Rules are not needed on a playground', 'To make playing boring', 'Only adults need rules'], 0),
   ('Which of these is a safe playground behaviour?', ['Taking turns on the slide', 'Pushing others off the swing', 'Running with sticks', 'Climbing the wrong way up the slide'], 0),
   ('Following playground rules helps everyone ___.', ['Get hurt', 'Play safely and have fun', 'Feel left out', 'Argue more'], 1)])

# ─── DAY 69 ─────────────────────────────────────────────────────────────────
d69_lang = sub('Language', 'Story Lessons: What We Learn from a Story',
  'Students learn that many stories teach a lesson or message, such as being kind or telling the truth, and practise thinking about what a story teaches.',
  [('What word describes a message or teaching found in a story?', ['lesson']),
   ('Name one lesson a story might teach, like being kind or honest.', ['being kind', 'honesty', 'kindness', 'telling the truth']),
   ('Do many stories try to teach us something?', ['yes'])],
  [('What is a lesson in a story?', ['The title of the book', 'A message or teaching found in the story', 'The name of a character', 'The number of pages'], 1),
   ('Which of these could be a lesson from a story?', ['Being kind to others', 'The colour of the cover', 'The size of the book', 'The page numbers'], 0),
   ('Why do authors often include a lesson in a story?', ['To help readers learn something important', 'Lessons are never included', 'To confuse readers', 'Stories never teach anything'], 0),
   ('If a story is about sharing and being kind, what might the lesson be?', ['Sharing and kindness are important', 'Numbers are important', 'Colours are important', 'Nothing can be learned'], 0),
   ('Thinking about a story lesson helps us ___.', ['Understand the message of the story', 'Forget the story', 'Ignore the characters', 'Skip the ending'], 0)])

d69_math = sub('Math', 'Time: Reading a Clock to the Hour',
  'Students learn to read a simple analog clock to the hour, recognizing that the short hand points to the hour and the long hand points to the 12 at the top.',
  [('On a clock, which hand is shorter, the hour hand or the minute hand?', ['hour hand']),
   ('When it is exactly 3 oclock, where does the long hand point?', ['12', 'the 12']),
   ('When it is exactly 3 oclock, where does the short hand point?', ['3', 'the 3'])],
  [('On a clock, which hand shows the hour?', ['The long hand', 'The short hand', 'Both hands', 'Neither hand'], 1),
   ('When it is exactly 6 oclock, where does the long hand point?', ['The 6', 'The 12', 'The 3', 'The 9'], 1),
   ('When it is exactly 8 oclock, where does the short hand point?', ['The 12', 'The 6', 'The 8', 'The 3'], 2),
   ('A clock with a short hand and a long hand is called an ___ clock.', ['Digital', 'Analog', 'Broken', 'Empty'], 1),
   ('Reading a clock to the hour helps us know ___.', ['What time it is', 'What day it is', 'What season it is', 'What colour it is'], 0)])

d69_sci = sub('Science', 'Oceans: A Home for Sea Animals',
  'Students learn that oceans are large bodies of salt water that are home to many animals, such as fish, whales, and sea turtles.',
  [('Is ocean water salty or fresh?', ['salty']),
   ('Name one animal that lives in the ocean, like a fish or whale.', ['fish', 'whale', 'sea turtle']),
   ('Are oceans large bodies of water?', ['yes'])],
  [('Is ocean water salty or fresh?', ['Fresh', 'Salty', 'Neither', 'Both the same'], 1),
   ('Which of these animals lives in the ocean?', ['Whale', 'Cow', 'Camel', 'Chicken'], 0),
   ('An ocean is an example of a ___.', ['Desert', 'Large body of salt water', 'Mountain', 'Forest'], 1),
   ('Which of these is also an ocean animal?', ['Sea turtle', 'Farm pig', 'Barn owl', 'Garden worm'], 0),
   ('Why do many different animals live in the ocean?', ['The ocean provides food and a home for sea life', 'The ocean has no water', 'Animals cannot live in oceans', 'Oceans are always frozen'], 0)])

d69_ss = sub('SocialStudies', 'Our Doctor Office: Staying Healthy',
  'Students learn about visiting the doctor office for checkups and when feeling unwell, and that doctors and nurses work together to help keep people healthy.',
  [('Who helps check if you are healthy at a doctor office?', ['doctor']),
   ('What word describes a regular visit to make sure you are healthy?', ['checkup']),
   ('Do doctors and nurses work together to help people?', ['yes'])],
  [('Who helps check if you are healthy at a doctor office?', ['A doctor', 'A firefighter', 'A baker', 'A postal worker'], 0),
   ('What is a checkup?', ['A regular visit to make sure you are healthy', 'A type of food', 'A kind of toy', 'A weather event'], 0),
   ('Who often works alongside doctors to help patients?', ['Nurses', 'Bakers', 'Firefighters', 'Postal workers'], 0),
   ('Why is it helpful to visit the doctor for regular checkups?', ['It helps make sure we stay healthy', 'Checkups are not helpful', 'Doctors never help', 'Health does not matter'], 0),
   ('A doctor office is a place in our community that helps people stay ___.', ['Healthy', 'Confused', 'Hungry', 'Lost'], 0)])

# ─── DAY 70 (Review) ────────────────────────────────────────────────────────
d70_lang = sub('Language', 'Language Review: Blends, Words, and Stories',
  'Students review recent Language skills: consonant blends, number of s and -ing endings, sentence types, book authors, and story lessons.',
  [('What two letters blend together at the start of the word stop?', ['st']),
   ('Add an s to the word cat. What new word do you make?', ['cats']),
   ('What word describes the person who writes the words of a book?', ['author'])],
  [('Which word begins with the blend bl?', ['Black', 'Sun', 'Pig', 'Hat'], 0),
   ('Which word means more than one book?', ['Book', 'Books', 'Booked', 'Booking'], 1),
   ('What punctuation mark ends an asking sentence?', ['Period', 'Question mark', 'Comma', 'Exclamation mark'], 1),
   ('What does an author do?', ['Draws the pictures', 'Writes the words of a book', 'Prints the book', 'Sells the book'], 1),
   ('What is a lesson in a story?', ['The title of the book', 'A message or teaching found in the story', 'The name of a character', 'The number of pages'], 1)])

d70_math = sub('Math', 'Math Review: Numbers, Patterns, and Time',
  'Students review recent Math skills: number words, counting to 50, number bonds to 20, shapes with many sides, patterns, grids, and telling time to the hour.',
  [('Write the number word for 15.', ['fifteen']),
   ('What number added to 15 makes 20?', ['5', 'five']),
   ('How many sides does a hexagon have?', ['6', 'six'])],
  [('Which number word matches the numeral 12?', ['Twelve', 'Two', 'Twenty', 'Ten'], 0),
   ('What number comes right after 39?', ['38', '39', '40', '41'], 2),
   ('How many sides does a pentagon have?', ['4', '5', '6', '7'], 1),
   ('In the pattern star, moon, sun, star, moon, ___, what comes next?', ['Star', 'Moon', 'Sun', 'Cloud'], 2),
   ('When it is exactly 6 oclock, where does the long hand point?', ['The 6', 'The 12', 'The 3', 'The 9'], 1)])

d70_sci = sub('Science', 'Science Review: Bodies, Habitats, and Animals',
  'Students review recent Science topics: our eyes, animal coverings, migration, bees and pollination, our skeleton, deserts, and oceans.',
  [('What body part do we use to see?', ['eyes']),
   ('What covers most of a dog body?', ['fur']),
   ('What word describes animals travelling long distances to find warmer weather?', ['migration'])],
  [('How many eyes does a person usually have?', ['1', '2', '3', '4'], 1),
   ('What covering does a bird usually have?', ['Fur', 'Feathers', 'Scales', 'Shell'], 1),
   ('What do bees collect from flowers?', ['Nectar', 'Rocks', 'Water only', 'Sand'], 0),
   ('Is a desert usually a wet place or a dry place?', ['Wet', 'Dry', 'Neither', 'Both'], 1),
   ('Is ocean water salty or fresh?', ['Fresh', 'Salty', 'Neither', 'Both the same'], 1)])

d70_ss = sub('SocialStudies', 'Social Studies Review: Community Helpers and Habits',
  'Students review recent Social Studies topics: postal workers, firefighters, grocery stores, bakeries, getting to school, teamwork, playground rules, and doctor offices.',
  [('What does a postal worker deliver to our homes?', ['mail', 'letters', 'packages']),
   ('What is the name of the building where firefighters work?', ['firehall', 'fire hall', 'fire station']),
   ('Where do many families go to buy food?', ['grocery store', 'the grocery store'])],
  [('What does a postal worker deliver?', ['Mail and packages', 'Food only', 'Water only', 'Toys only'], 0),
   ('What vehicle is kept ready at the firehall?', ['A fire truck', 'A school bus', 'A boat', 'A bicycle'], 0),
   ('What should you wear if you ride a bike to school?', ['Nothing extra', 'A helmet', 'Sunglasses only', 'Mittens only'], 1),
   ('Which of these shows good teamwork?', ['Sharing jobs and helping each other', 'Doing everything alone', 'Refusing to help', 'Arguing without listening'], 0),
   ('Who helps check if you are healthy at a doctor office?', ['A doctor', 'A firefighter', 'A baker', 'A postal worker'], 0)])


g0_61_70 = [
    day(61, [d61_lang, d61_math, d61_sci, d61_ss]),
    day(62, [d62_lang, d62_math, d62_sci, d62_ss]),
    day(63, [d63_lang, d63_math, d63_sci, d63_ss]),
    day(64, [d64_lang, d64_math, d64_sci, d64_ss]),
    day(65, [d65_lang, d65_math, d65_sci, d65_ss]),
    day(66, [d66_lang, d66_math, d66_sci, d66_ss]),
    day(67, [d67_lang, d67_math, d67_sci, d67_ss]),
    day(68, [d68_lang, d68_math, d68_sci, d68_ss]),
    day(69, [d69_lang, d69_math, d69_sci, d69_ss]),
    day(70, [d70_lang, d70_math, d70_sci, d70_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_61_70)
    append_worksheet_days(0, g0_61_70)
