#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 101-110 -- eighth batch extending Grade 0
past the Days 91-100 batch. This is a self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to() helpers, since those do not
support a worksheet field) modeled exactly on gen_grade0_days91_100.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-100 topics (see data/grade0.ts / data/grade0.json). New punctuation
(periods), new word families (-ap, -in), a new suffix (-er), uppercase and
lowercase letter matching, story solutions, nonfiction text clues, asking
questions about a story, and the return sweep print concept were all
selected for Language; Venn diagrams, rolling/stacking/sliding 3D shapes,
the calendar and months of the year, counting backwards, comparing coin
values, comparing capacity, number bonds to 6, left/right position words,
and writing numerals were selected for Math; the sense of smell, forest
habitats, precipitation, seed dispersal, animal groups (herds/flocks/
packs), screws and wedges, the human life cycle, food groups, and
endangered animals were selected for Science; and crossing guards,
Thanksgiving, the Prime Minister, goods and services, pharmacists, garbage
collectors, personal safety information, the local zoo, and fire safety
were selected for Social Studies -- none of those exact ideas appear in
Days 1-100. No
embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely for kindergarten readability and to keep
the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260722):
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


# ─── DAY 101 ────────────────────────────────────────────────────────────────
d101_lang = sub('Language', 'Punctuation: Periods at the End of a Sentence',
  'Students learn that a sentence usually ends with a small dot called a period, which tells a reader to stop and pause before starting the next sentence.',
  [('What small dot do we put at the end of a telling sentence?', ['period', 'a period']),
   ('Look at the sentence I see a cat. What mark comes right after the word cat?', ['period', '.', 'a period']),
   ('Does a period tell a reader to stop and pause?', ['yes'])],
  [('What small dot do we put at the end of a telling sentence?', ['A period', 'A question mark', 'An exclamation mark', 'A comma'], 0),
   ('Which sentence correctly ends with a period?', ['I like dogs.', 'I like dogs', 'I like dogs!', 'I like dogs?'], 0),
   ('What does a period tell a reader to do?', ['Stop and pause before the next sentence', 'Read louder', 'Skip the sentence', 'Start singing'], 0),
   ('Which of these sentences is missing an ending mark?', ['The sun is hot', 'The sun is hot.', 'The sun is hot!', 'Is the sun hot?'], 0),
   ('A period is used at the end of a ___.', ['Telling sentence', 'Story title', 'Character name', 'Book cover'], 0)])

d101_math = sub('Math', 'Venn Diagrams: Sorting into Two Groups',
  'Students learn to use a Venn diagram, two overlapping circles, to sort objects into groups based on whether they share a certain attribute, like colour or shape.',
  [('If a Venn diagram has two circles, how many groups can objects be sorted into using them?', ['two', '2']),
   ('Name one way you could sort toys into two circles, like by colour or shape.', ['colour', 'shape', 'size']),
   ('If an object fits in both circles, where might it go in a Venn diagram?', ['in the middle', 'overlapping part', 'where the circles overlap'])],
  [('What shape do we usually use to sort objects into two groups on a Venn diagram?', ['Two overlapping circles', 'One square', 'A triangle', 'A straight line'], 0),
   ('If you sort toys by colour using a Venn diagram, what are you grouping toys by?', ['Their colour', 'Their weight', 'Their sound', 'Their smell'], 0),
   ('Where would an object go if it belongs in both circles of a Venn diagram?', ['In the middle part where the circles overlap', 'Outside both circles', 'Only in the left circle', 'Only in the right circle'], 0),
   ('A Venn diagram helps us ___.', ['Sort and compare objects into groups', 'Measure how loud something is', 'Tell time', 'Count to 100'], 0),
   ('Which of these could you sort using a Venn diagram?', ['Toys sorted by colour and shape', 'A single number', 'A song', 'A shadow'], 0)])

d101_sci = sub('Science', 'Our Nose: Smelling Good and Bad Smells',
  'Students learn that the nose is the body part used for smelling, helping us notice good smells like flowers and warning smells like smoke.',
  [('What body part do we use to smell things?', ['nose']),
   ('Name one smell that might be pleasant, like flowers or fresh bread.', ['flowers', 'fresh bread', 'cookies']),
   ('Can a smell, like smoke, warn us that something might be unsafe?', ['yes'])],
  [('What body part do we use to smell things?', ['Nose', 'Ears', 'Eyes', 'Elbow'], 0),
   ('Which of these is an example of a pleasant smell?', ['Fresh flowers', 'Burning smoke', 'Rotten food', 'Skunk spray'], 0),
   ('Why might the smell of smoke be an important warning smell?', ['It can warn us that there might be a fire', 'It always smells nice', 'It has no meaning at all', 'It tells us to eat lunch'], 0),
   ('Which of these smells might warn us that food has gone bad?', ['A sour, rotten smell', 'A sweet flower smell', 'A fresh bread smell', 'No smell change at all'], 0),
   ('Our nose is one of our five ___.', ['Senses', 'Bones', 'Colours', 'Shapes'], 0)])

d101_ss = sub('SocialStudies', 'Our Crossing Guard: Helping Us Cross Safely',
  'Students learn about the job of a crossing guard, a community helper who stands at busy streets to help children and families cross safely on their way to and from school.',
  [('What do we call a helper who stops traffic so we can cross the street safely?', ['crossing guard']),
   ('Where does a crossing guard often stand to help people cross safely?', ['at a busy street', 'near school', 'at a crosswalk']),
   ('Should we listen to and follow a crossing guard signal before crossing?', ['yes'])],
  [('What do we call a helper who stops traffic so people can cross the street safely?', ['A crossing guard', 'A librarian', 'A farmer', 'A mayor'], 0),
   ('Where does a crossing guard usually stand to help people?', ['At a busy street or crosswalk', 'Inside a library', 'Inside a bakery', 'On a mountain'], 0),
   ('What should you do when a crossing guard signals it is safe to cross?', ['Cross carefully while watching for cars', 'Run without looking', 'Ignore the signal', 'Stay in the middle of the street'], 0),
   ('Why is a crossing guard an important community helper?', ['They help keep people safe while crossing busy streets', 'They deliver mail', 'They grow food', 'They fix broken pipes'], 0),
   ('A crossing guard often helps children get to and from ___ safely.', ['School', 'The moon', 'A boat', 'A cave'], 0)])

# ─── DAY 102 ────────────────────────────────────────────────────────────────
d102_lang = sub('Language', 'Word Families: -ap Words',
  'Students explore the -ap word family, learning that changing the first letter of words like cap, map, and tap creates new rhyming words that share the same ending sound.',
  [('Change the c in cap to m. What new word do you make?', ['map']),
   ('Change the m in map to t. What new word do you make?', ['tap']),
   ('Name one more word that rhymes with cap, map, and tap.', ['nap', 'lap', 'sap', 'clap'])],
  [('Which word rhymes with cap?', ['Map', 'Dog', 'Sun', 'Cup'], 0),
   ('Change the c in cap to n. What new word do you make?', ['Nap', 'Nut', 'Net', 'Nod'], 0),
   ('Which of these words is part of the -ap word family?', ['Tap', 'Top', 'Tip', 'Tub'], 0),
   ('Words in the -ap family all end with the same ___.', ['Sound', 'Colour', 'Picture', 'Number'], 0),
   ('Which word does not belong in the -ap word family?', ['Sun', 'Cap', 'Map', 'Tap'], 0)])

d102_math = sub('Math', '3D Shapes: Which Ones Roll, Stack, or Slide',
  'Students explore 3D shapes by testing whether each one rolls, like a sphere, stacks, like a cube, or slides, like the flat face of a cylinder.',
  [('Would a round sphere, like a ball, roll or stay still?', ['roll']),
   ('Would a cube, with flat faces, be easy to stack on top of another cube?', ['yes']),
   ('Name one 3D shape that can roll, like a sphere or cylinder.', ['sphere', 'cylinder', 'ball'])],
  [('Which 3D shape rolls easily because it is round all over?', ['Sphere', 'Cube', 'Cone standing up', 'Rectangular prism'], 0),
   ('Why can a cube stack easily on top of another cube?', ['It has flat faces', 'It is round', 'It has no faces', 'It rolls away'], 0),
   ('Which 3D shape can both roll and stack, depending on how it is placed?', ['A cylinder', 'A sphere only', 'A cube only', 'None of these'], 0),
   ('Which shape would NOT roll well because it has flat faces and corners?', ['A cube', 'A sphere', 'A ball', 'A round marble'], 0),
   ('Testing whether shapes roll, stack, or slide helps us learn about their ___.', ['Attributes', 'Colours', 'Smells', 'Sounds'], 0)])

d102_sci = sub('Science', 'Forest Habitats: Trees and Wildlife',
  'Students learn that a forest is a habitat full of many trees, where animals such as squirrels, deer, and owls find food and shelter among the branches and leaves.',
  [('What do we call a habitat that is full of many trees?', ['forest', 'a forest']),
   ('Name one animal that might live in a forest, like a squirrel or owl.', ['squirrel', 'owl', 'deer']),
   ('Do forest animals often use trees for food and shelter?', ['yes'])],
  [('What is a forest?', ['A habitat full of many trees', 'A dry desert', 'A small pond', 'A deep ocean'], 0),
   ('Which animal is commonly found living in a forest?', ['A squirrel', 'A camel', 'A shark', 'A polar bear'], 0),
   ('Why might a forest be a good habitat for many animals?', ['It offers trees for food and shelter', 'It has no trees at all', 'It is always underwater', 'It never has any plants'], 0),
   ('What do forest animals like owls use trees for?', ['Finding food and shelter', 'Swimming', 'Making sand', 'Building roads'], 0),
   ('A forest is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d102_ss = sub('SocialStudies', 'Thanksgiving: A Time to Give Thanks',
  'Students learn that Thanksgiving is a Canadian holiday in the fall when families gather together to share a meal and give thanks for the good things in their lives.',
  [('What season does Canadian Thanksgiving happen in?', ['fall', 'autumn']),
   ('Name one thing families might do together on Thanksgiving, like sharing a meal.', ['share a meal', 'eat together', 'give thanks']),
   ('Is Thanksgiving a time to give thanks for good things in our lives?', ['yes'])],
  [('In what season does Canadian Thanksgiving take place?', ['Fall', 'Winter', 'Spring', 'Summer'], 0),
   ('What do families often do together on Thanksgiving?', ['Share a meal and give thanks', 'Go ice skating', 'Plant a garden', 'Build snowmen'], 0),
   ('What is the main idea of Thanksgiving?', ['Giving thanks for good things in our lives', 'Buying new toys', 'Sleeping all day', 'Cleaning the whole house'], 0),
   ('Which of these is often part of a Thanksgiving celebration?', ['A family gathering with a special meal', 'Wearing costumes to trick or treat', 'Giving out valentines', 'Watching fireworks at midnight'], 0),
   ('Thanksgiving reminds us to feel ___ for the good things we have.', ['Thankful', 'Angry', 'Bored', 'Afraid'], 0)])

# ─── DAY 103 ────────────────────────────────────────────────────────────────
d103_lang = sub('Language', 'Word Families: -in Words',
  'Students explore the -in word family, learning that changing the first letter of words like pin, win, and fin creates new rhyming words that share the same ending sound.',
  [('Change the p in pin to w. What new word do you make?', ['win']),
   ('Change the w in win to f. What new word do you make?', ['fin']),
   ('Name one more word that rhymes with pin, win, and fin.', ['bin', 'chin', 'tin', 'din'])],
  [('Which word rhymes with pin?', ['Win', 'Dog', 'Sun', 'Cup'], 0),
   ('Change the p in pin to f. What new word do you make?', ['Fin', 'Fan', 'Fun', 'Fig'], 0),
   ('Which of these words is part of the -in word family?', ['Bin', 'Bat', 'But', 'Bit'], 0),
   ('Words in the -in family all end with the same ___.', ['Sound', 'Colour', 'Picture', 'Number'], 0),
   ('Which word does not belong in the -in word family?', ['Sun', 'Pin', 'Win', 'Fin'], 0)])

d103_math = sub('Math', 'Calendar: Months of the Year',
  'Students learn that a year is divided into twelve months, such as January and July, and that a calendar helps us keep track of days, weeks, and months.',
  [('How many months are there in a year?', ['12', 'twelve']),
   ('Name one month of the year, like January or July.', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
   ('Does a calendar help us keep track of days and months?', ['yes'])],
  [('How many months are there in one year?', ['12', '7', '4', '52'], 0),
   ('Which of these is a month of the year?', ['July', 'Monday', 'Summer', 'Morning'], 0),
   ('What tool helps us keep track of days, weeks, and months?', ['A calendar', 'A ruler', 'A thermometer', 'A scale'], 0),
   ('Which month often comes right after December, starting a new year?', ['January', 'June', 'October', 'March'], 0),
   ('A year is made up of twelve ___.', ['Months', 'Days only', 'Hours only', 'Minutes only'], 0)])

d103_sci = sub('Science', 'Types of Precipitation: Rain, Snow, and Hail',
  'Students learn that precipitation is water that falls from clouds in different forms, such as rain, snow, and hail, depending on the temperature outside.',
  [('What word describes water falling from clouds, like rain or snow?', ['precipitation']),
   ('Name one type of precipitation that falls when it is very cold, like snow.', ['snow']),
   ('Does rain usually fall when the weather is warm rather than freezing?', ['yes'])],
  [('What word describes water falling from clouds, such as rain or snow?', ['Precipitation', 'Erosion', 'Gravity', 'Camouflage'], 0),
   ('Which type of precipitation usually falls when the weather is very cold?', ['Snow', 'Warm rain', 'Sunshine', 'Fog only'], 0),
   ('Which type of precipitation falls as small balls of ice?', ['Hail', 'Warm rain', 'Snowflakes only', 'Fog'], 0),
   ('What usually causes precipitation to fall as snow instead of rain?', ['Cold temperatures', 'Very hot temperatures', 'No clouds at all', 'Bright sunshine'], 0),
   ('Rain, snow, and hail are all types of ___.', ['Precipitation', 'Habitats', 'Life cycles', 'Forces'], 0)])

d103_ss = sub('SocialStudies', 'Our Prime Minister: Leading Our Country',
  'Students learn that the Prime Minister is the leader chosen to help make important decisions for the whole country of Canada.',
  [('What do we call the leader who helps make important decisions for all of Canada?', ['Prime Minister', 'the Prime Minister']),
   ('Is a mayor the leader of a town, or the leader of the whole country?', ['a town', 'town']),
   ('Does the Prime Minister help make decisions for the whole country?', ['yes'])],
  [('What do we call the leader who helps make important decisions for all of Canada?', ['The Prime Minister', 'The Mayor', 'The Librarian', 'The Farmer'], 0),
   ('How is the Prime Minister different from a mayor?', ['The Prime Minister leads the whole country while a mayor leads a town or city', 'They have the exact same job', 'A mayor leads the whole country', 'Neither one leads anything'], 0),
   ('Which of these best describes the job of the Prime Minister?', ['Helping make important decisions for Canada', 'Delivering mail across town', 'Growing food on a farm', 'Teaching kindergarten class'], 0),
   ('Where does the Prime Minister help make decisions for our country?', ['In Canada', 'In another country only', 'Nowhere at all', 'Only in one small town'], 0),
   ('Learning about the Prime Minister helps us understand more about our ___.', ['Country', 'Favourite foods', 'Favourite games', 'Weather'], 0)])

# ─── DAY 104 ────────────────────────────────────────────────────────────────
d104_lang = sub('Language', 'Making New Words: Adding -er',
  'Students learn that adding -er to some words, such as changing tall to taller or small to smaller, helps compare two things.',
  [('Add -er to the word tall. What new word do you make?', ['taller']),
   ('Add -er to the word small. What new word do you make?', ['smaller']),
   ('Does adding -er to a word often help us compare two things, like which is bigger?', ['yes'])],
  [('Add -er to the word tall. What new word do you make?', ['Taller', 'Tallier', 'Tall', 'Tallen'], 0),
   ('Add -er to the word small. What new word do you make?', ['Smaller', 'Smallier', 'Small', 'Smallen'], 0),
   ('Adding -er to a word like fast usually helps us ___.', ['Compare two things', 'Name a colour', 'Count objects', 'Tell time'], 0),
   ('Which word correctly compares two things using -er?', ['Faster', 'Fastier', 'Fasting', 'Fasten'], 0),
   ('Which sentence correctly uses a word with -er to compare two dogs?', ['The big dog is bigger than the small dog', 'The big dog is big than the small dog', 'The big dog is bigly the small dog', 'The big dog is bigness the small dog'], 0)])

d104_math = sub('Math', 'Counting Backwards from 10 to 1',
  'Students practise counting backwards, starting at 10 and saying each number in order down to 1, a skill often used during a countdown.',
  [('If you count backwards starting at 10, what number comes right after 10?', ['9', 'nine']),
   ('If you count backwards from 5, what number comes right after 5?', ['4', 'four']),
   ('What is the last number you say when counting backwards all the way down to 1?', ['1', 'one'])],
  [('If you count backwards starting at 10, what number comes next?', ['9', '11', '8', '7'], 0),
   ('If you count backwards from 5, what number comes right after 5?', ['4', '6', '3', '10'], 0),
   ('What is the last number you say when counting backwards down to 1?', ['1', '0', '2', '10'], 0),
   ('Counting backwards from 10 to 1 is often used during a ___.', ['Countdown', 'Song', 'Recipe', 'Story'], 0),
   ('Which list correctly shows numbers counting backwards from 5?', ['5, 4, 3, 2, 1', '1, 2, 3, 4, 5', '5, 3, 1, 2, 4', '1, 3, 5, 2, 4'], 0)])

d104_sci = sub('Science', 'Seed Dispersal: How Seeds Travel',
  'Students learn that seed dispersal happens when seeds travel away from the parent plant by wind, water, or animals, helping new plants grow in new places.',
  [('What word describes seeds travelling away from the parent plant?', ['seed dispersal', 'dispersal']),
   ('Name one way a seed might travel to a new place, like by wind or by an animal.', ['wind', 'water', 'animal']),
   ('Can seeds travelling to new places help new plants grow there?', ['yes'])],
  [('What do we call seeds travelling away from the parent plant?', ['Seed dispersal', 'Erosion', 'Gravity', 'Migration'], 0),
   ('Which of these can carry a seed to a new place?', ['Wind', 'A shadow', 'A number', 'A sound'], 0),
   ('How might an animal help disperse a seed?', ['By carrying the seed to a new spot', 'By eating the whole plant only', 'By ignoring the seed completely', 'By freezing the seed forever'], 0),
   ('Why is seed dispersal helpful for plants?', ['It helps new plants grow in new places', 'It stops plants from ever growing', 'It destroys all seeds', 'It has no purpose at all'], 0),
   ('Seeds can travel by wind, water, or ___.', ['Animals', 'Sound waves', 'Shadows', 'Colours'], 0)])

d104_ss = sub('SocialStudies', 'Goods and Services: What People Make and Do',
  'Students learn the difference between goods, which are things people make or grow, and services, which are helpful jobs people do for others.',
  [('What word describes things that people make or grow, like bread or toys?', ['goods']),
   ('What word describes helpful jobs people do for others, like cutting hair?', ['services']),
   ('Is a loaf of bread an example of a good or a service?', ['good', 'a good'])],
  [('What do we call things that people make or grow, like bread or toys?', ['Goods', 'Services', 'Laws', 'Habitats'], 0),
   ('What do we call helpful jobs people do for others, like fixing a car?', ['Services', 'Goods', 'Habitats', 'Fossils'], 0),
   ('Which of these is an example of a good?', ['A loaf of bread', 'A haircut', 'A doctor visit', 'A bus ride'], 0),
   ('Which of these is an example of a service?', ['A haircut from a hairdresser', 'A toy car', 'A bag of apples', 'A book'], 0),
   ('Farmers who grow food and hairdressers who cut hair both help our community by providing ___.', ['Goods and services', 'Laws only', 'Only games', 'Only stories'], 0)])

# ─── DAY 105 ────────────────────────────────────────────────────────────────
d105_lang = sub('Language', 'Uppercase and Lowercase Letters: Matching Big and Small',
  'Students learn to match uppercase, or capital, letters with their lowercase partners, such as matching a big B with a small b.',
  [('What do we call a big letter, like B, at the start of a name?', ['uppercase', 'capital letter']),
   ('What do we call a small letter, like b, used in the middle of a word?', ['lowercase']),
   ('Does the uppercase letter A match with the lowercase letter a?', ['yes'])],
  [('What do we call a big letter, like B?', ['Uppercase', 'Lowercase', 'Punctuation', 'Numeral'], 0),
   ('What do we call a small letter, like b?', ['Lowercase', 'Uppercase', 'Punctuation', 'Numeral'], 0),
   ('Which of these is the lowercase match for the uppercase letter M?', ['m', 'N', 'W', 'B'], 0),
   ('Which of these is the uppercase match for the lowercase letter t?', ['T', 'F', 'L', 'J'], 0),
   ('Uppercase letters are often used at the ___ of a sentence or name.', ['Beginning', 'End only', 'Middle only', 'Never used'], 0)])

d105_math = sub('Math', 'Money: Comparing Values of Coins',
  'Students compare the values of Canadian coins, learning that some coins, like a quarter, are worth more than others, like a nickel, even if they look similar in size.',
  [('Is a quarter worth more or less than a nickel?', ['more']),
   ('Name one Canadian coin, like a penny, nickel, dime, or quarter.', ['penny', 'nickel', 'dime', 'quarter']),
   ('Does a bigger looking coin always have a bigger value?', ['no'])],
  [('Which coin is worth more, a quarter or a nickel?', ['A quarter', 'A nickel', 'They are equal', 'Cannot tell'], 0),
   ('Which of these is a Canadian coin?', ['A dime', 'A leaf', 'A button', 'A rock'], 0),
   ('Does a coin size always tell us its value?', ['No, some small coins are worth more than bigger ones', 'Yes, bigger coins are always worth more', 'Coins have no value at all', 'Only paper money has value'], 0),
   ('Which coin is worth the least amount of money?', ['A penny', 'A dime', 'A quarter', 'A loonie'], 0),
   ('Comparing coin values helps us understand ___.', ['How much money we have', 'How tall we are', 'What day it is', 'What the weather is'], 0)])

d105_sci = sub('Science', 'Animal Groups: Herds, Flocks, and Packs',
  'Students learn that many animals live and travel together in groups, such as a herd of deer, a flock of birds, or a pack of wolves, which can help keep them safe.',
  [('What do we call a group of birds flying together?', ['flock']),
   ('What do we call a group of wolves living together?', ['pack']),
   ('Can living in a group help keep animals safer?', ['yes'])],
  [('What do we call a group of birds flying together?', ['A flock', 'A herd', 'A pack', 'A pod'], 0),
   ('What do we call a group of wolves living together?', ['A pack', 'A flock', 'A herd', 'A school'], 0),
   ('What do we call a group of deer moving together?', ['A herd', 'A flock', 'A pack', 'A pod'], 0),
   ('Why might animals live together in groups?', ['It can help keep them safer', 'It always makes them louder', 'Groups have no benefit', 'It makes them slower'], 0),
   ('Herds, flocks, and packs are all examples of animal ___.', ['Groups', 'Habitats', 'Fossils', 'Life cycles'], 0)])

d105_ss = sub('SocialStudies', 'Our Pharmacist: Helping Us Stay Healthy',
  'Students learn about the job of a pharmacist, a community helper who works at a pharmacy and helps prepare the medicine that doctors say people need.',
  [('What do we call a helper who prepares medicine at a pharmacy?', ['pharmacist']),
   ('Where does a pharmacist usually work?', ['pharmacy', 'a pharmacy']),
   ('Does a pharmacist help people stay healthy?', ['yes'])],
  [('What do we call a helper who prepares medicine at a pharmacy?', ['A pharmacist', 'A librarian', 'A farmer', 'A mayor'], 0),
   ('Where does a pharmacist usually work?', ['At a pharmacy', 'In a library', 'On a farm', 'At a museum'], 0),
   ('Why is a pharmacist an important community helper?', ['They help prepare medicine that keeps people healthy', 'They deliver mail', 'They grow food', 'They build houses'], 0),
   ('Who usually tells a pharmacist what medicine a person needs?', ['A doctor', 'A librarian', 'A farmer', 'A crossing guard'], 0),
   ('A pharmacist helps our community stay ___.', ['Healthy', 'Confused', 'Unsafe', 'Hungry'], 0)])

# ─── DAY 106 ────────────────────────────────────────────────────────────────
d106_lang = sub('Language', 'Story Solutions: How Problems Get Solved',
  'Students learn that many stories have a problem faced by a character and a solution, which is how the character solves or fixes that problem by the end.',
  [('What word describes how a character fixes a problem in a story?', ['solution']),
   ('If a character loses a toy and then finds it again, what is the solution?', ['finding the toy', 'finding it']),
   ('Do most stories show a problem and then a solution?', ['yes'])],
  [('What do we call how a character fixes a problem in a story?', ['The solution', 'The problem', 'The title', 'The cover'], 0),
   ('If a character is lost and then finds their way home, what is the solution?', ['Finding the way home', 'Getting lost', 'The characters name', 'The title of the book'], 0),
   ('Why do authors often include a solution at the end of a story?', ['To show how the characters problem gets fixed', 'To make the story longer for no reason', 'Solutions are never included in stories', 'To confuse the reader'], 0),
   ('Which of these is an example of a story solution?', ['A character asks a friend for help and solves the problem', 'A character never notices any problem', 'A story with no characters', 'A story with no problem at all'], 0),
   ('Understanding story solutions helps readers see how a problem gets ___.', ['Solved', 'Ignored', 'Hidden', 'Forgotten'], 0)])

d106_math = sub('Math', 'Measurement: Comparing Capacity (Holds More or Less)',
  'Students compare the capacity of different containers, learning to describe which container holds more and which holds less using water or sand.',
  [('If one cup holds more water than another cup, which one has a bigger capacity?', ['the cup that holds more', 'the bigger cup']),
   ('Name one word used to compare how much two containers can hold, like more or less.', ['more', 'less']),
   ('Could you use sand or water to test which container holds more?', ['yes'])],
  [('What word describes how much a container can hold?', ['Capacity', 'Weight', 'Length', 'Colour'], 0),
   ('If a bucket holds more water than a cup, the bucket has a ___ capacity.', ['Bigger', 'Smaller', 'Equal', 'No'], 0),
   ('How could you test which of two containers holds more water?', ['Fill each one and compare', 'Weigh them on a scale only', 'Measure their colour', 'Count their corners'], 0),
   ('If two containers hold the exact same amount of water, their capacities are ___.', ['Equal', 'Very different', 'Impossible to compare', 'Unknown forever'], 0),
   ('Comparing capacity helps us understand how much a container can ___.', ['Hold', 'Weigh', 'Cost', 'Sound like'], 0)])

d106_sci = sub('Science', 'Simple Machines: Screws and Wedges',
  'Students learn about two more simple machines, a screw, which is a spiral ramp that holds things together, and a wedge, which is a shape used to split or cut things apart.',
  [('What simple machine has a spiral shape and helps hold things together, like in wood?', ['screw']),
   ('What simple machine is shaped like a triangle and helps cut or split things, like an axe?', ['wedge']),
   ('Name one place you might see a screw being used.', ['furniture', 'wood', 'toys'])],
  [('What simple machine has a spiral shape and helps hold things together?', ['A screw', 'A wheel', 'A lever', 'A pulley'], 0),
   ('What simple machine is shaped like a triangle and helps cut or split things apart?', ['A wedge', 'A screw', 'A wheel', 'A ramp'], 0),
   ('Which of these tools uses a wedge shape to cut?', ['An axe', 'A screwdriver', 'A pulley rope', 'A wheel'], 0),
   ('Where might you find a screw being used?', ['Holding pieces of furniture together', 'Floating in the sky', 'Growing in a garden', 'Swimming in the ocean'], 0),
   ('Screws and wedges are both examples of ___.', ['Simple machines', 'Habitats', 'Life cycles', 'Weather tools'], 0)])

d106_ss = sub('SocialStudies', 'Our Garbage Collectors: Keeping Streets Tidy',
  'Students learn about the job of a garbage collector, a community helper who picks up garbage and recycling from homes so streets and neighbourhoods stay clean.',
  [('What do we call a helper who picks up garbage from homes?', ['garbage collector']),
   ('Why is it helpful for garbage collectors to pick up trash regularly?', ['keeps streets clean', 'stays tidy']),
   ('Do garbage collectors help keep our neighbourhood clean?', ['yes'])],
  [('What do we call a helper who picks up garbage from homes?', ['A garbage collector', 'A librarian', 'A farmer', 'A pharmacist'], 0),
   ('Why is the job of a garbage collector important for a community?', ['It helps keep streets and neighbourhoods clean', 'It has no real purpose', 'It makes streets messier', 'It only happens once a year'], 0),
   ('What might a garbage collector pick up from homes, besides garbage?', ['Recycling', 'Books', 'Medicine', 'Mail'], 0),
   ('What might a neighbourhood look like without garbage collectors?', ['Messy and full of trash', 'Perfectly clean forever', 'Exactly the same as always', 'Full of flowers only'], 0),
   ('Garbage collectors help keep our community ___.', ['Clean and tidy', 'Loud', 'Confusing', 'Unsafe'], 0)])

# ─── DAY 107 ────────────────────────────────────────────────────────────────
d107_lang = sub('Language', 'Nonfiction Clues: Labels and Photographs in Books',
  'Students learn that nonfiction books often use labels and photographs to give readers true information and help explain real people, places, or things.',
  [('What kind of pictures do nonfiction books often use to show real things?', ['photographs', 'photos']),
   ('What do we call words that name parts of a picture, like labelling parts of a flower?', ['labels']),
   ('Do nonfiction books give readers true information?', ['yes'])],
  [('What kind of book gives readers true information about real people, places, or things?', ['A nonfiction book', 'A fiction book', 'A poem only', 'A song only'], 0),
   ('What kind of pictures do nonfiction books often use to show real things clearly?', ['Photographs', 'Made-up cartoon drawings only', 'No pictures at all', 'Only maps'], 0),
   ('What do we call words that name parts of a picture, like the parts of a flower?', ['Labels', 'Titles', 'Rhymes', 'Punctuation'], 0),
   ('Why might a nonfiction book about animals use photographs?', ['To show readers what the real animal looks like', 'To make the book longer for no reason', 'Photographs are never used in nonfiction books', 'To confuse the reader'], 0),
   ('Labels and photographs are examples of clues found in ___ books.', ['Nonfiction', 'Fiction', 'Poetry', 'Fairy tale'], 0)])

d107_math = sub('Math', 'Number Bonds: Ways to Make 6',
  'Students explore different combinations of two numbers that add together to make 6, such as 1 and 5, or 2 and 4, building an understanding of number composition.',
  [('What two numbers can you add together to make 6, using 2 and another number?', ['2 and 4', '4']),
   ('What two numbers can you add together to make 6, using 1 and another number?', ['1 and 5', '5']),
   ('Can 3 and 3 also add together to make 6?', ['yes'])],
  [('Which two numbers add together to make 6?', ['2 and 4', '2 and 5', '3 and 4', '1 and 1'], 0),
   ('Which two numbers add together to make 6?', ['1 and 5', '1 and 6', '2 and 2', '5 and 5'], 0),
   ('Does 3 plus 3 also equal 6?', ['Yes', 'No', 'Only sometimes', 'Cannot tell'], 0),
   ('Which pair of numbers does NOT add together to make 6?', ['2 and 5', '1 and 5', '2 and 4', '3 and 3'], 0),
   ('Learning different ways to make 6 helps us understand that a number can be made of ___.', ['Different smaller number combinations', 'Only one possible combination', 'No smaller numbers at all', 'Only itself and zero'], 0)])

d107_sci = sub('Science', 'Life Cycle of a Human: Baby to Adult',
  'Students learn that humans grow and change through stages of life, starting as a baby, growing into a child, then a teenager, and eventually a grown adult.',
  [('What do we call a very young human right after being born?', ['baby']),
   ('Name one stage a human grows through, like baby, child, or adult.', ['baby', 'child', 'teenager', 'adult']),
   ('Do humans grow and change as they get older?', ['yes'])],
  [('What do we call a very young human right after being born?', ['A baby', 'A cub', 'A chick', 'A calf'], 0),
   ('Put these life stages in order: baby, child, ___.', ['Teenager and then adult', 'Only more babies', 'Nothing at all', 'Egg'], 0),
   ('What happens to humans as they move through the stages of life?', ['They grow and change over time', 'They never change at all', 'They turn into a different animal', 'They disappear completely'], 0),
   ('Which of these is a stage in the human life cycle?', ['Child', 'Fossil', 'Habitat', 'Erosion'], 0),
   ('Learning about human life stages helps us understand how people ___.', ['Grow and change over time', 'Stay exactly the same forever', 'Never grow at all', 'Live only underwater'], 0)])

d107_ss = sub('SocialStudies', 'Knowing My Information: Name, Address, and Phone Number',
  'Students learn why it is helpful and safe to know important personal information, such as their full name, home address, and a family phone number.',
  [('Name one important piece of information you should know about yourself, like your full name.', ['full name', 'name', 'address', 'phone number']),
   ('Why might it help to know your home address?', ['to find home', 'if you get lost', 'for safety']),
   ('Should you know a family phone number in case you need help?', ['yes'])],
  [('Which of these is important personal information to know for safety?', ['Your home address', 'Your favourite colour', 'Your favourite song', 'Your favourite toy'], 0),
   ('Why is it helpful to know a family phone number?', ['It can help a trusted adult contact your family if you need help', 'It has no real purpose', 'It is only useful for playing games', 'It should always be kept secret from everyone'], 0),
   ('Who should you share your important personal information with if you need help?', ['A trusted adult, like a parent, teacher, or police officer', 'Anyone who asks', 'A stranger', 'No one at all'], 0),
   ('Which of these is an example of personal information?', ['Your full name', 'The weather today', 'A story you read', 'A song you like'], 0),
   ('Knowing your name, address, and phone number can help keep you ___.', ['Safe', 'Confused', 'Bored', 'Hungry'], 0)])

# ─── DAY 108 ────────────────────────────────────────────────────────────────
d108_lang = sub('Language', 'Asking Questions: Wondering About a Story',
  'Students practise asking questions before, during, and after reading a story, wondering about characters, events, and what might happen next.',
  [('Name one question you might ask before reading a story, like what will happen.', ['what will happen', 'who is in it']),
   ('Name one question you might ask about a character in a story.', ['what does the character like', 'why did the character do that']),
   ('Can asking questions help us understand a story better?', ['yes'])],
  [('Why might a reader ask questions before starting a story?', ['To wonder what the story might be about', 'Questions are never helpful', 'To ignore the story', 'To skip the whole book'], 0),
   ('Which of these is a good question to ask while reading a story?', ['Why did the character do that', 'What is your favourite colour', 'What did you eat for breakfast', 'How tall are you'], 0),
   ('Asking questions while reading can help a reader ___.', ['Understand the story better', 'Forget the story completely', 'Make the story disappear', 'Read more slowly for no reason'], 0),
   ('Which of these is a question you might ask after finishing a story?', ['What happened at the end', 'What is your shoe size', 'What day is it today', 'What is the weather'], 0),
   ('Wondering about characters, events, and what happens next is part of ___.', ['Asking questions about a story', 'Ignoring a story', 'Writing your name', 'Counting pages only'], 0)])

d108_math = sub('Math', 'Position Words: Left and Right',
  'Students learn positional language, using the words left and right to describe the direction or side that an object or person is on.',
  [('If you raise the hand you write with, is that usually your left or right hand for most people?', ['right']),
   ('If a ball is sitting on the left side of a table, is it on the left side or the right side?', ['left']),
   ('Name one position word that tells direction, like left or right.', ['left', 'right'])],
  [('If a cup is sitting on the left side of a table, where is the cup?', ['On the left side', 'On the right side', 'Above the table', 'Below the table'], 0),
   ('If you point to the right, which direction are you pointing?', ['To the right side', 'To the left side', 'Straight up', 'Straight down'], 0),
   ('Which of these words describes a side or direction?', ['Left', 'Loud', 'Sweet', 'Cold'], 0),
   ('If a book is on your right side, where would you reach to find it?', ['To your right', 'To your left', 'Above your head', 'Below your feet'], 0),
   ('Position words like left and right help us describe ___.', ['Where something is located', 'What colour something is', 'How heavy something is', 'What sound something makes'], 0)])

d108_sci = sub('Science', 'Food Groups: Eating a Balanced Diet',
  'Students learn that healthy eating includes different food groups, such as fruits, vegetables, grains, and proteins, and that eating a variety of foods helps our bodies stay strong.',
  [('Name one food group, like fruits or vegetables.', ['fruits', 'vegetables', 'grains', 'proteins']),
   ('Does eating a variety of different foods help our bodies stay strong?', ['yes']),
   ('Name one healthy food you could eat from the fruit group.', ['apple', 'banana', 'orange'])],
  [('Which of these is a food group?', ['Vegetables', 'Toys', 'Colours', 'Shapes'], 0),
   ('Why is it healthy to eat foods from different food groups?', ['It helps our bodies get what they need to stay strong', 'It makes food taste worse', 'It has no effect on our bodies', 'Eating only one food group is always healthier'], 0),
   ('Which of these is an example of a fruit?', ['An apple', 'A carrot', 'A slice of bread', 'A piece of chicken'], 0),
   ('Which of these is an example of a vegetable?', ['A carrot', 'An apple', 'A banana', 'A grape'], 0),
   ('Eating a balanced diet means eating ___.', ['A variety of foods from different food groups', 'Only one kind of food', 'No food at all', 'Only sweet treats'], 0)])

d108_ss = sub('SocialStudies', 'Our Local Zoo: Learning About Animals',
  'Students learn that a zoo is a community place where people can visit and learn about animals from around the world while zookeepers care for their needs.',
  [('What do we call a place where people can visit and learn about animals?', ['zoo', 'a zoo']),
   ('Who takes care of the animals at a zoo?', ['zookeeper', 'zookeepers']),
   ('Can visiting a zoo help us learn about animals from around the world?', ['yes'])],
  [('What do we call a place where people can visit and learn about animals?', ['A zoo', 'A library', 'A bakery', 'A bank'], 0),
   ('Who takes care of the animals living at a zoo?', ['A zookeeper', 'A librarian', 'A pharmacist', 'A mayor'], 0),
   ('Why might families enjoy visiting a zoo?', ['They can see and learn about animals from around the world', 'Zoos have no animals at all', 'Zoos are only for adults', 'Zoos are always closed'], 0),
   ('What is one job a zookeeper might do?', ['Feeding and caring for the animals', 'Delivering mail', 'Growing crops', 'Fixing cars'], 0),
   ('A zoo helps our community by ___.', ['Teaching people about animals', 'Selling bread', 'Delivering packages', 'Growing vegetables'], 0)])

# ─── DAY 109 ────────────────────────────────────────────────────────────────
d109_lang = sub('Language', 'Print Concepts: Return Sweep (Reading Top to Bottom)',
  'Students learn about the return sweep, the way a reader eyes move from the end of one line of text back to the start of the next line below it.',
  [('After reading to the end of a line of text, where do our eyes move next?', ['down to the next line', 'next line']),
   ('Do we read a page from top to bottom, one line after another?', ['yes']),
   ('What do we call the eye movement from the end of one line back to the start of the next line?', ['return sweep'])],
  [('What do we call the eye movement from the end of one line of text back to the start of the next line?', ['The return sweep', 'The title', 'The cover', 'The author'], 0),
   ('After finishing a line of text, where should a readers eyes move next?', ['Down to the start of the next line', 'Back to the very first word of the book', 'Off the page completely', 'Up to the top of the page only'], 0),
   ('Do we usually read a page from top to bottom?', ['Yes', 'No', 'Only sometimes', 'Never'], 0),
   ('Why is the return sweep an important print concept for new readers?', ['It helps readers know where to continue reading next', 'It has no real purpose', 'It only matters for pictures', 'It tells us the title of the book'], 0),
   ('Understanding the return sweep helps readers follow the text in the correct ___.', ['Order', 'Colour', 'Volume', 'Smell'], 0)])

d109_math = sub('Math', 'Writing Numerals: Forming Numbers 0 to 10',
  'Students practise writing numerals from 0 to 10, learning to form each number shape correctly with a pencil or crayon.',
  [('Write the numeral that comes right after 4.', ['5']),
   ('Write the numeral that shows zero, meaning none at all.', ['0']),
   ('Name one numeral between 0 and 10 that you can practise writing.', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])],
  [('Which numeral comes right after 4?', ['5', '6', '3', '7'], 0),
   ('Which numeral shows zero, meaning none at all?', ['0', '1', '10', '9'], 0),
   ('When writing numerals, it is helpful to practise forming each ___ correctly.', ['Number shape', 'Colour', 'Sound', 'Song'], 0),
   ('Which numeral comes right before 10?', ['9', '8', '11', '7'], 0),
   ('Writing numerals from 0 to 10 helps us practise ___.', ['Forming numbers correctly', 'Singing a song', 'Drawing animals', 'Naming colours'], 0)])

d109_sci = sub('Science', 'Endangered Animals: Protecting Wildlife',
  'Students learn that an endangered animal is one with very few left in the wild, and that people can help protect these animals by caring for their habitats.',
  [('What word describes an animal with very few left in the wild?', ['endangered']),
   ('Name one way people can help protect endangered animals, like caring for habitats.', ['caring for habitats', 'protecting habitats']),
   ('Is it important to help protect animals that are endangered?', ['yes'])],
  [('What word describes an animal with very few left in the wild?', ['Endangered', 'Nocturnal', 'Migrating', 'Camouflaged'], 0),
   ('Which of these could help protect an endangered animal?', ['Taking care of its natural habitat', 'Destroying its habitat', 'Ignoring the animal completely', 'Hunting the animal for fun'], 0),
   ('Why might people want to protect endangered animals?', ['So the animals do not disappear forever', 'Endangered animals are not important', 'Protecting animals has no purpose', 'Endangered animals are not real'], 0),
   ('Which of these is a reason an animal might become endangered?', ['Losing its natural habitat', 'Having too many babies', 'Eating too much food', 'Living too long'], 0),
   ('Learning about endangered animals helps us understand how to ___.', ['Care for and protect wildlife', 'Ignore all animals', 'Destroy habitats', 'Hunt more animals'], 0)])

d109_ss = sub('SocialStudies', 'Fire Safety: What to Do If There Is a Fire',
  'Students learn simple fire safety steps, such as staying low to avoid smoke, using stop drop and roll if clothing catches fire, and getting to a safe meeting spot outside.',
  [('What three steps should you do if your clothing catches fire?', ['stop drop and roll', 'stop, drop, and roll']),
   ('Should you stay low to the ground to avoid breathing in smoke during a fire?', ['yes']),
   ('Where should your family meet if you ever need to leave your home during a fire?', ['a safe meeting spot', 'meeting spot outside'])],
  [('What three steps should you do if your clothing catches fire?', ['Stop, drop, and roll', 'Run as fast as you can', 'Hide under a bed', 'Shout and wave your arms'], 0),
   ('Why should you stay low to the ground during a fire?', ['To avoid breathing in smoke', 'To find toys faster', 'To hide from friends', 'It has no purpose'], 0),
   ('Why does a family practise a fire safety plan with a meeting spot outside?', ['So everyone knows where to gather safely if there is a fire', 'To play a fun game', 'Meeting spots are not important', 'To confuse family members'], 0),
   ('Which of these shows good fire safety?', ['Practising stop, drop, and roll', 'Hiding in a closet during a fire', 'Ignoring a smoke alarm', 'Playing with matches'], 0),
   ('Learning fire safety steps helps keep our family ___.', ['Safe', 'Confused', 'Unprepared', 'In danger'], 0)])

# ─── DAY 110 (Review) ───────────────────────────────────────────────────────
d110_lang = sub('Language', 'Language Review: Punctuation, Word Families, and Story Skills',
  'Students review recent Language skills: periods, the -ap and -in word families, adding -er, uppercase and lowercase letters, story solutions, nonfiction clues, asking questions, and the return sweep.',
  [('What small dot do we put at the end of a telling sentence?', ['period', 'a period']),
   ('Change the c in cap to m. What new word do you make?', ['map']),
   ('What do we call a big letter, like B?', ['uppercase', 'capital letter'])],
  [('What small dot do we put at the end of a telling sentence?', ['A period', 'A question mark', 'An exclamation mark', 'A comma'], 0),
   ('Which word rhymes with pin?', ['Win', 'Dog', 'Sun', 'Cup'], 0),
   ('Add -er to the word tall. What new word do you make?', ['Taller', 'Tallier', 'Tall', 'Tallen'], 0),
   ('What do we call how a character fixes a problem in a story?', ['The solution', 'The problem', 'The title', 'The cover'], 0),
   ('What do we call the eye movement from the end of one line of text back to the start of the next line?', ['The return sweep', 'The title', 'The cover', 'The author'], 0)])

d110_math = sub('Math', 'Math Review: Sorting, Shapes, and Number Sense',
  'Students review recent Math skills: Venn diagrams, 3D shapes that roll or stack, the calendar, counting backwards, comparing coin values, capacity, number bonds to 6, position words, and writing numerals.',
  [('What shape do we usually use to sort objects into two groups on a Venn diagram?', ['two overlapping circles', 'circles']),
   ('How many months are there in a year?', ['12', 'twelve']),
   ('Which two numbers add together to make 6, using 2 and another number?', ['2 and 4', '4'])],
  [('What shape do we usually use to sort objects into two groups on a Venn diagram?', ['Two overlapping circles', 'One square', 'A triangle', 'A straight line'], 0),
   ('Which 3D shape rolls easily because it is round all over?', ['Sphere', 'Cube', 'Cone standing up', 'Rectangular prism'], 0),
   ('How many months are there in one year?', ['12', '7', '4', '52'], 0),
   ('Which coin is worth more, a quarter or a nickel?', ['A quarter', 'A nickel', 'They are equal', 'Cannot tell'], 0),
   ('Which numeral comes right after 4?', ['5', '6', '3', '7'], 0)])

d110_sci = sub('Science', 'Science Review: Bodies, Habitats, and Nature',
  'Students review recent Science topics: our nose, forest habitats, precipitation, seed dispersal, animal groups, screws and wedges, the human life cycle, food groups, and endangered animals.',
  [('What body part do we use to smell things?', ['nose']),
   ('What is a forest?', ['a habitat full of trees', 'habitat with trees']),
   ('What word describes an animal with very few left in the wild?', ['endangered'])],
  [('What body part do we use to smell things?', ['Nose', 'Ears', 'Eyes', 'Elbow'], 0),
   ('What is a forest?', ['A habitat full of many trees', 'A dry desert', 'A small pond', 'A deep ocean'], 0),
   ('What do we call a group of wolves living together?', ['A pack', 'A flock', 'A herd', 'A school'], 0),
   ('Which of these is a food group?', ['Vegetables', 'Toys', 'Colours', 'Shapes'], 0),
   ('What word describes an animal with very few left in the wild?', ['Endangered', 'Nocturnal', 'Migrating', 'Camouflaged'], 0)])

d110_ss = sub('SocialStudies', 'Social Studies Review: Helpers, Holidays, and Our Country',
  'Students review recent Social Studies topics: crossing guards, Thanksgiving, the Prime Minister, goods and services, pharmacists, garbage collectors, personal information safety, the local zoo, and fire safety.',
  [('What do we call a helper who stops traffic so we can cross the street safely?', ['crossing guard']),
   ('What do we call the leader who helps make important decisions for all of Canada?', ['Prime Minister', 'the Prime Minister']),
   ('What do we call things that people make or grow, like bread or toys?', ['goods'])],
  [('What do we call a helper who stops traffic so people can cross the street safely?', ['A crossing guard', 'A librarian', 'A farmer', 'A mayor'], 0),
   ('In what season does Canadian Thanksgiving take place?', ['Fall', 'Winter', 'Spring', 'Summer'], 0),
   ('What do we call the leader who helps make important decisions for all of Canada?', ['The Prime Minister', 'The Mayor', 'The Librarian', 'The Farmer'], 0),
   ('What do we call a helper who prepares medicine at a pharmacy?', ['A pharmacist', 'A librarian', 'A farmer', 'A mayor'], 0),
   ('What do we call a place where people can visit and learn about animals?', ['A zoo', 'A library', 'A bakery', 'A bank'], 0)])


g0_101_110 = [
    day(101, [d101_lang, d101_math, d101_sci, d101_ss]),
    day(102, [d102_lang, d102_math, d102_sci, d102_ss]),
    day(103, [d103_lang, d103_math, d103_sci, d103_ss]),
    day(104, [d104_lang, d104_math, d104_sci, d104_ss]),
    day(105, [d105_lang, d105_math, d105_sci, d105_ss]),
    day(106, [d106_lang, d106_math, d106_sci, d106_ss]),
    day(107, [d107_lang, d107_math, d107_sci, d107_ss]),
    day(108, [d108_lang, d108_math, d108_sci, d108_ss]),
    day(109, [d109_lang, d109_math, d109_sci, d109_ss]),
    day(110, [d110_lang, d110_math, d110_sci, d110_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_101_110)
    append_worksheet_days(0, g0_101_110)
