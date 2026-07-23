#!/usr/bin/env python3
"""Grade 1, Days 101-110 -- EIGHTH batch, extending Grade 1 through Day 110.
Self-contained script modeled exactly on gen_grade1_days91_100.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-100 topics (see data/grade1.ts / data/grade1.json). No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely to keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260723):
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
d101_lang = sub('Language', 'Possessive Nouns: Showing Ownership with s',
  'Students learn that adding an apostrophe and s to a noun shows that something belongs to someone, as in the dogs bone or Sams hat.',
  [('What do we add to a name to show it owns something, like Sam s hat?', ['apostrophe s', 's']),
   ('In the dogs bone, who owns the bone?', ['the dog']),
   ('Say a short phrase that shows something belongs to your friend.', ['my friends toy', 'my friends book', 'my friends pencil', 'my friends bag'])],
  [('Which phrase shows that the ball belongs to Mia?', ['Mias ball', 'Mia ball', 'Ball Mia', 'The ball Mia'], 0),
   ('What does adding an apostrophe and s to a name usually show?', ['That something belongs to that person', 'That the word is a question', 'That the word is plural only', 'Nothing at all'], 0),
   ('Which phrase correctly shows the cats toy?', ['cats toy', 'cat toy s', 'toy cats', 'cats toys toy'], 0),
   ('In the teachers desk, who owns the desk?', ['The teacher', 'The student', 'The principal', 'No one'], 0),
   ('Why is it useful to know how to show ownership in writing?', ['It helps readers understand who something belongs to', 'It makes words longer for no reason', 'It changes the meaning of every sentence', 'It has no real use'], 0)])

d101_math = sub('Math', 'Place Value: Hundreds, Tens, and Ones to 200',
  'Students build on their understanding of tens and ones to include hundreds, learning that numbers past 100 have one hundred plus some tens and ones.',
  [('In the number 156, how many hundreds are there?', ['1', 'one']),
   ('In the number 156, how many tens are there?', ['5', 'five']),
   ('In the number 156, how many ones are there?', ['6', 'six'])],
  [('In the number 174, how many hundreds are there?', ['1', '7', '4', '0'], 0),
   ('In the number 138, how many tens are there?', ['3', '1', '8', '0'], 0),
   ('In the number 192, how many ones are there?', ['2', '9', '1', '0'], 0),
   ('What is 100 plus 40 plus 5?', ['145', '140', '154', '105'], 0),
   ('Why do we group numbers into hundreds, tens, and ones?', ['It makes larger numbers easier to read and understand', 'It makes numbers harder to understand', 'It only works for small numbers', 'It has no real purpose'], 0)])

d101_sci = sub('Science', 'Our Skin: Protecting Our Body',
  'Students learn that skin is the largest organ of our body, and it protects us from germs, helps us feel touch, and helps control our body temperature.',
  [('What is the largest organ of our body?', ['skin']),
   ('Does our skin help protect us from germs?', ['yes']),
   ('Name one thing our skin helps us feel, like touch.', ['touch', 'heat', 'cold', 'pain'])],
  [('What is the largest organ of our body?', ['Skin', 'Heart', 'Brain', 'Lungs'], 0),
   ('What does our skin help protect us from?', ['Germs', 'Loud sounds only', 'Bright light only', 'Nothing at all'], 0),
   ('What can our skin help us feel?', ['Touch, heat, and cold', 'Only sound', 'Only taste', 'Only smell'], 0),
   ('Why is it important to keep our skin clean?', ['To help stop germs from making us sick', 'It has no real reason', 'To make our skin a different colour', 'To make us taller'], 0),
   ('What covers almost our entire body and protects what is inside?', ['Our skin', 'Our hair only', 'Our clothes only', 'Our bones only'], 0)])

d101_ss = sub('SocialStudies', 'Our Municipal Services: Water, Garbage, and Roads',
  'Students learn that local governments provide municipal services like clean water, garbage pickup, and road repairs that help keep a community running smoothly.',
  [('Name one municipal service, like garbage pickup.', ['garbage pickup', 'clean water', 'road repairs']),
   ('Who usually provides municipal services like garbage pickup?', ['the local government', 'the town', 'the city']),
   ('Why do communities need clean water?', ['to stay healthy', 'to drink safely', 'for health'])],
  [('What is a municipal service?', ['A service a local government provides, like garbage pickup', 'A toy sold in stores', 'A type of food', 'A kind of weather'], 0),
   ('Who usually provides services like road repairs in a town?', ['The local government', 'A single family', 'A visiting tourist', 'No one at all'], 0),
   ('Why is clean water an important municipal service?', ['People need clean water to stay healthy', 'It has no real importance', 'It is only used for washing cars', 'It is never actually needed'], 0),
   ('What might happen without regular garbage pickup?', ['Garbage would build up in the community', 'Nothing would change at all', 'Streets would become cleaner', 'Water would become dirtier only'], 0),
   ('Why do communities rely on many different municipal services together?', ['Each service helps keep the community safe, clean, and running smoothly', 'Communities never actually need any services', 'One single service can meet every need', 'Municipal services are optional and unimportant'], 0)])

# ─── DAY 102 ────────────────────────────────────────────────────────────────
d102_lang = sub('Language', 'Reading Comprehension: Sequencing in Nonfiction',
  'Students learn to identify the order of steps or events in a nonfiction text, using clue words like first, next, then, and last.',
  [('Name one clue word that shows order in a nonfiction text, like first.', ['first', 'next', 'then', 'last']),
   ('Why do nonfiction texts often use words like first and next?', ['to show the order of steps', 'to show sequence']),
   ('What comes right after first in a sequence?', ['next', 'then'])],
  [('Which word is a clue that something happens first?', ['First', 'Cat', 'Blue', 'Jump'], 0),
   ('Why do writers use words like first, next, and last in a nonfiction text?', ['To show the order in which things happen', 'To make the text longer for no reason', 'To confuse the reader', 'To add extra pictures'], 0),
   ('In a recipe, which step usually comes before mixing the ingredients?', ['Gathering the ingredients', 'Eating the food', 'Washing the dishes', 'Serving the food'], 0),
   ('If a text says last, we know the step or event described is ___.', ['At the end of the sequence', 'At the very beginning', 'In the middle only', 'Not part of any order'], 0),
   ('Why is understanding sequence helpful when following instructions?', ['It helps us complete steps in the correct order', 'It makes instructions harder to follow', 'It has no real use', 'It only matters for stories, not instructions'], 0)])

d102_math = sub('Math', 'Two-Digit Addition Without Regrouping',
  'Students learn to add two two-digit numbers by adding the ones together and the tens together, without needing to regroup.',
  [('What is 23 plus 15?', ['38', 'thirty-eight']),
   ('What is 42 plus 31?', ['73', 'seventy-three']),
   ('When adding two-digit numbers, which digits do we add together first?', ['the ones', 'ones digits'])],
  [('What is 12 plus 24?', ['36', '35', '38', '34'], 0),
   ('What is 41 plus 27?', ['68', '67', '69', '66'], 0),
   ('When adding 34 plus 15, what do we add first?', ['The ones digits, 4 and 5', 'The tens digits only', 'Nothing at all', 'The whole numbers randomly'], 0),
   ('What is 53 plus 26?', ['79', '78', '80', '77'], 0),
   ('Why is it helpful to add the ones and tens separately?', ['It breaks the problem into smaller, easier steps', 'It makes the problem impossible to solve', 'It only works for one-digit numbers', 'It has no real benefit'], 0)])

d102_sci = sub('Science', 'Owls: Nocturnal Birds of Prey',
  'Students learn that owls are birds that hunt at night, using sharp eyesight, quiet flight, and strong hearing to find small animals to eat.',
  [('Do owls usually hunt during the day or at night?', ['at night']),
   ('Name one thing that helps an owl hunt, like sharp eyesight.', ['sharp eyesight', 'quiet flight', 'strong hearing']),
   ('What do we call an animal that hunts other animals for food?', ['predator'])],
  [('When do owls usually hunt for food?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
   ('What helps an owl fly quietly to sneak up on prey?', ['Special soft feathers', 'Loud wings', 'Bright colours', 'A long tail only'], 0),
   ('What sense helps an owl find small animals in the dark?', ['Strong hearing', 'Taste only', 'Smell only', 'No senses at all'], 0),
   ('What do we call an animal, like an owl, that hunts other animals for food?', ['A predator', 'A prey animal only', 'A plant', 'A pet'], 0),
   ('Why are an owls adaptations, like quiet flight and sharp eyesight, useful for night hunting?', ['They help the owl find and catch food in the dark', 'They have no real purpose', 'They only help the owl during the day', 'They make the owl slower'], 0)])

d102_ss = sub('SocialStudies', 'Canadas Territories: The North',
  'Students learn that Canada has three territories in the north - Yukon, Northwest Territories, and Nunavut - with cold climates and unique communities.',
  [('Name one of Canadas three territories.', ['Yukon', 'Northwest Territories', 'Nunavut']),
   ('How many territories does Canada have?', ['3', 'three']),
   ('Are Canadas territories generally located in the north or south?', ['the north'])],
  [('How many territories does Canada have?', ['Three', 'One', 'Ten', 'Thirteen'], 0),
   ('Which of these is one of Canadas three territories?', ['Nunavut', 'Alberta', 'Quebec', 'Manitoba'], 0),
   ('Where in Canada are the three territories located?', ['In the north', 'In the far south', 'On the west coast only', 'In the middle of the country only'], 0),
   ('What is often true about the climate in Canadas territories?', ['It is generally cold, especially in winter', 'It is always hot and dry', 'It never changes throughout the year', 'It has no connection to the seasons'], 0),
   ('Why might communities in the territories have unique ways of life compared to southern Canada?', ['Their cold climate and remote location shape how people live, travel, and get food', 'The climate and location have no effect on daily life', 'Every part of Canada has the exact same way of life', 'Communities in the territories never adapt to their environment'], 0)])

# ─── DAY 103 ────────────────────────────────────────────────────────────────
d103_lang = sub('Language', 'Exclamatory Sentences: Showing Strong Feeling',
  'Students learn that an exclamatory sentence shows strong feeling, like excitement or surprise, and ends with an exclamation mark.',
  [('What punctuation mark ends an exclamatory sentence?', ['exclamation mark', '!']),
   ('What kind of feeling does an exclamatory sentence often show?', ['strong feeling', 'excitement']),
   ('Say a short exclamatory sentence about something fun.', ['That was so fun!', 'We won the game!', 'I love this!'])],
  [('Which sentence is an exclamatory sentence?', ['We won the game!', 'We won the game.', 'Did we win the game?', 'We might win the game'], 0),
   ('What does an exclamatory sentence usually show?', ['Strong feeling, like excitement or surprise', 'A calm, quiet fact only', 'A question with no answer', 'Nothing at all'], 0),
   ('Which punctuation mark ends an exclamatory sentence?', ['An exclamation mark', 'A period', 'A question mark', 'A comma'], 0),
   ('Which sentence shows surprise using an exclamation mark?', ['Wow, look at that rainbow!', 'The rainbow has colours.', 'Is that a rainbow?', 'Rainbows form after rain'], 0),
   ('Why might a writer use an exclamatory sentence in a story?', ['To show a character feels excited or surprised', 'To make the sentence longer for no reason', 'To ask the reader a question', 'To end the story'], 0)])

d103_math = sub('Math', 'Two-Digit Subtraction Without Regrouping',
  'Students learn to subtract two-digit numbers by subtracting the ones and the tens separately, without needing to regroup.',
  [('What is 48 minus 15?', ['33', 'thirty-three']),
   ('What is 67 minus 24?', ['43', 'forty-three']),
   ('When subtracting two-digit numbers, which digits do we subtract first?', ['the ones', 'ones digits'])],
  [('What is 39 minus 16?', ['23', '22', '24', '25'], 0),
   ('What is 58 minus 27?', ['31', '30', '32', '29'], 0),
   ('When subtracting 45 minus 12, what do we subtract first?', ['The ones digits, 5 minus 2', 'The tens digits only', 'Nothing at all', 'The whole numbers randomly'], 0),
   ('What is 76 minus 34?', ['42', '41', '43', '40'], 0),
   ('Why is it helpful to subtract the ones and tens separately?', ['It breaks the problem into smaller, easier steps', 'It makes the problem impossible to solve', 'It only works for one-digit numbers', 'It has no real benefit'], 0)])

d103_sci = sub('Science', 'Bats: Flying Mammals of the Night',
  'Students learn that bats are mammals that can fly, are active at night, and many kinds use echolocation, or sound bouncing back, to find food in the dark.',
  [('Are bats mammals or insects?', ['mammals']),
   ('Are bats usually active during the day or at night?', ['at night']),
   ('What do we call the way some bats use sound to find food in the dark?', ['echolocation'])],
  [('What kind of animal is a bat?', ['A mammal', 'An insect', 'A reptile', 'A fish'], 0),
   ('When are bats usually most active?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
   ('What is echolocation?', ['Using sound that bounces back to find things in the dark', 'A type of bright light', 'A kind of food bats eat', 'A place where bats sleep'], 0),
   ('Where do many bats rest during the day?', ['In caves or hanging upside down in trees', 'Underwater', 'In the middle of a busy road', 'Floating in the sky'], 0),
   ('Why is echolocation useful for a bat flying at night?', ['It helps the bat find food and avoid obstacles in the dark', 'It has no real use for a bat', 'It only helps a bat see colours', 'It stops a bat from flying at all'], 0)])

d103_ss = sub('SocialStudies', 'Trading and Bartering Long Ago',
  'Students learn that before money was commonly used, people often traded goods directly with each other, a practice called bartering.',
  [('What do we call trading goods directly, without using money?', ['bartering']),
   ('Did people use bartering before money was common?', ['yes']),
   ('Give an example of a barter, like trading eggs for bread.', ['trading eggs for bread', 'trading vegetables for milk', 'trading wood for food'])],
  [('What is bartering?', ['Trading goods directly without using money', 'Buying goods only with coins', 'Giving goods away for free', 'A type of modern online shopping'], 0),
   ('Did people use bartering before money became common?', ['Yes', 'No, money has always been used', 'A concept unrelated to trading', 'Bartering was never used by anyone'], 0),
   ('Which is an example of bartering?', ['Trading eggs for a loaf of bread', 'Paying with a credit card', 'Withdrawing money from a bank', 'Ordering something online'], 0),
   ('Why might bartering have been useful before money was widely used?', ['It let people exchange goods they needed without using coins or bills', 'It made trading goods impossible', 'It required people to use only money', 'It had no real purpose'], 0),
   ('Why might money have eventually become more common than bartering?', ['Money made it easier to trade without needing to find someone who wanted exactly what you had', 'Money made trading much harder than bartering', 'Bartering was always more convenient than money', 'People stopped needing to trade at all'], 0)])

# ─── DAY 104 ────────────────────────────────────────────────────────────────
d104_lang = sub('Language', 'Word Families: -ock and -uck',
  'Students learn to read and build words in the -ock and -uck word families, such as rock, clock, duck, and truck.',
  [('Name a word in the -ock family, like rock.', ['rock', 'clock', 'sock', 'lock']),
   ('Name a word in the -uck family, like duck.', ['duck', 'truck', 'luck', 'stuck']),
   ('What sound do rock and clock share at the end?', ['ock', '-ock'])],
  [('Which word belongs to the -ock word family?', ['Clock', 'Truck', 'Duck', 'Luck'], 0),
   ('Which word belongs to the -uck word family?', ['Truck', 'Rock', 'Sock', 'Lock'], 0),
   ('Which word rhymes with sock?', ['Rock', 'Duck', 'Truck', 'Luck'], 0),
   ('Which word rhymes with stuck?', ['Truck', 'Rock', 'Sock', 'Lock'], 0),
   ('Why is it helpful to learn word families like -ock and -uck?', ['Knowing one word helps us read and spell other words with the same pattern', 'Word families never help with reading', 'They only work for one single word', 'They make reading more confusing'], 0)])

d104_math = sub('Math', 'Data: Line Plots with Simple Objects',
  'Students learn to organize simple data using a line plot, placing an X above a number or category for each object counted.',
  [('On a line plot, what do we place above a number to show a count?', ['an X', 'a mark']),
   ('What kind of information can a line plot show?', ['data', 'counts of things']),
   ('If three children have 2 pets, how many Xs go above the number 2?', ['3', 'three'])],
  [('On a line plot, what symbol is often used to show one item?', ['An X', 'A circle only', 'A triangle only', 'A word only'], 0),
   ('If four students chose apples as their favourite fruit, how many Xs would appear above apples on a line plot?', ['Four', 'One', 'Two', 'Ten'], 0),
   ('What does a line plot help us do with data?', ['Organize and count information visually', 'Hide information from view', 'Make numbers disappear', 'Replace numbers with pictures only'], 0),
   ('If a line plot shows 5 Xs above the number 3, what does that tell us?', ['Five items or people are linked to the number 3', 'Nothing at all', 'The number 3 was never counted', 'Only one item was counted'], 0),
   ('Why might we use a line plot instead of just listing numbers?', ['It makes patterns in the data easier to see at a glance', 'It hides all the information', 'It makes counting harder', 'It has no real purpose'], 0)])

d104_sci = sub('Science', 'The Life Cycle of a Frog',
  'Students learn that a frog begins life as an egg, hatches into a tadpole that lives in water, and slowly grows legs and lungs to become an adult frog.',
  [('What is the first stage of a frogs life cycle?', ['egg']),
   ('What do we call a young frog that lives in water and has a tail?', ['tadpole']),
   ('Does a tadpole slowly grow legs as it changes into a frog?', ['yes'])],
  [('What is the first stage of a frogs life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'Froglet'], 0),
   ('What do we call a young frog that lives in water and has a tail?', ['A tadpole', 'An egg', 'A froglet only', 'A pollywog only, with no other name'], 0),
   ('Does a tadpole breathe using gills or lungs at first?', ['Gills', 'Lungs only', 'Neither gills nor lungs', 'Both equally from the very start'], 0),
   ('What changes happen as a tadpole grows into an adult frog?', ['It grows legs and develops lungs for breathing air', 'It grows a longer tail only', 'It shrinks smaller and smaller', 'Nothing changes at all'], 0),
   ('Why do frogs usually lay their eggs in water?', ['Tadpoles need to live in water until they develop lungs and legs', 'Frog eggs can only survive on dry land', 'Water has no connection to a frogs life cycle', 'Frogs never actually lay eggs'], 0)])

d104_ss = sub('SocialStudies', 'Community Centres: Places to Play and Learn',
  'Students learn that community centres are public buildings where people can take part in sports, classes, and activities together.',
  [('What is a community centre?', ['a public building for activities', 'a place to play and learn']),
   ('Name one activity you might do at a community centre.', ['sports', 'take a class', 'play games']),
   ('Are community centres open to everyone in the community?', ['yes'])],
  [('What is a community centre?', ['A public building where people take part in activities together', 'A private home', 'A type of grocery store', 'A kind of vehicle'], 0),
   ('Which activity might happen at a community centre?', ['A sports class', 'Landing an airplane', 'Growing crops on a large farm', 'Building a skyscraper'], 0),
   ('Who is usually welcome to use a community centre?', ['People in the community', 'Only one single family', 'Only government leaders', 'No one at all'], 0),
   ('Why might a community centre be an important place for a neighbourhood?', ['It gives people a shared space to connect, learn, and stay active', 'It has no real benefit to a community', 'It is only used once a year', 'It keeps people from meeting each other'], 0),
   ('Why might community centres offer many different kinds of classes and activities?', ['To meet the different interests and needs of everyone in the community', 'Because only one activity is ever allowed', 'Community centres never offer any activities', 'To make sure no one can use the building'], 0)])

# ─── DAY 105 ────────────────────────────────────────────────────────────────
d105_lang = sub('Language', 'Setting the Scene: Describing Where a Story Happens',
  'Students learn that the setting of a story tells us where and when a story takes place, and authors use describing words to help readers picture it.',
  [('What does the setting of a story tell us?', ['where and when it happens', 'where a story takes place']),
   ('Name a word that could describe a story setting, like sunny or snowy.', ['sunny', 'snowy', 'dark', 'busy']),
   ('Why do authors describe the setting of a story?', ['to help readers picture it', 'to help us imagine the place'])],
  [('What does the setting of a story describe?', ['Where and when the story takes place', 'Only the main character', 'Only the ending of the story', 'Nothing important'], 0),
   ('Which sentence describes a setting?', ['The forest was dark and quiet at night.', 'She ran quickly to the door.', 'He felt very happy.', 'They laughed together.'], 0),
   ('Why might an author use describing words when writing about a setting?', ['To help readers picture the place in their minds', 'To make the story shorter', 'To confuse the reader', 'To remove all characters from the story'], 0),
   ('Which of these is an example of a story setting?', ['A snowy mountain in winter', 'A character named Sam', 'A feeling of excitement', 'An action like jumping'], 0),
   ('Why is understanding the setting helpful when reading a story?', ['It helps readers understand where and when events are happening', 'It has no connection to understanding a story', 'It only matters for the title of a book', 'Settings are never described in stories'], 0)])

d105_math = sub('Math', 'Comparing 2D and 3D Shapes',
  'Students compare flat 2D shapes, like circles and squares, with solid 3D shapes, like spheres and cubes, noticing how 3D shapes take up space.',
  [('Is a circle a 2D shape or a 3D shape?', ['2D shape', '2D']),
   ('Is a sphere a 2D shape or a 3D shape?', ['3D shape', '3D']),
   ('Name one 3D shape, like a cube.', ['cube', 'sphere', 'cone', 'cylinder'])],
  [('Which of these is a 2D shape?', ['A square', 'A cube', 'A sphere', 'A cone'], 0),
   ('Which of these is a 3D shape?', ['A sphere', 'A circle', 'A triangle', 'A rectangle'], 0),
   ('What is one difference between a 2D shape and a 3D shape?', ['A 3D shape takes up space, while a 2D shape is flat', 'There is no real difference at all', 'A 2D shape always has more sides', 'A 3D shape is always smaller'], 0),
   ('Which 3D shape looks like a ball?', ['A sphere', 'A cube', 'A cone', 'A cylinder'], 0),
   ('Why might we compare 2D and 3D shapes when learning geometry?', ['It helps us notice how flat shapes and solid shapes are different', 'It has no real purpose', 'It only matters for very old students', 'Shapes are never compared in math'], 0)])

d105_sci = sub('Science', 'Penguins: Birds That Cannot Fly',
  'Students learn that penguins are birds that cannot fly, but instead use their wings like flippers to swim well in cold ocean water.',
  [('Can penguins fly?', ['no']),
   ('What do penguins use their wings for instead of flying?', ['swimming', 'to swim']),
   ('Do penguins usually live in cold or warm places?', ['cold places', 'cold'])],
  [('Can penguins fly through the air?', ['No', 'Yes, very high', 'Only at night', 'Only in summer'], 0),
   ('What do penguins use their wings for?', ['Swimming, like flippers', 'Flying very high', 'Digging underground', 'Nothing at all'], 0),
   ('What kind of climate do most penguins live in?', ['Cold climates', 'Hot deserts', 'Tropical rainforests', 'Underground caves only'], 0),
   ('Why are penguins good swimmers even though they cannot fly?', ['Their wings act like flippers, helping them move well through water', 'Penguins never actually enter water', 'Their wings are too small to help them at all', 'Penguins use their beaks to swim instead of wings'], 0),
   ('Why might being unable to fly not be a problem for a penguin?', ['Penguins get the food and safety they need by swimming instead', 'Not flying always makes an animal unable to survive', 'Penguins need to fly to find any food', 'Flying is the only way any bird can survive'], 0)])

d105_ss = sub('SocialStudies', 'Winter Celebrations Around the World',
  'Students learn that people around the world celebrate different winter holidays and traditions, such as lighting candles or sharing special meals.',
  [('Name one thing people might do during a winter celebration, like light candles.', ['light candles', 'share a meal', 'sing songs']),
   ('Do different cultures celebrate different winter holidays?', ['yes']),
   ('Why do families gather during winter celebrations?', ['to be together', 'to celebrate together'])],
  [('What might families do during a winter celebration?', ['Light candles or share a special meal', 'Ignore each other completely', 'Avoid any traditions', 'Stay apart from family'], 0),
   ('Do different cultures around the world celebrate different winter holidays?', ['Yes', 'No, every culture celebrates in the exact same way', 'A concept unrelated to winter celebrations', 'Winter holidays do not exist anywhere'], 0),
   ('Why might learning about other cultures winter celebrations be interesting?', ['It helps us understand and appreciate different traditions around the world', 'It has no real value at all', 'Every culture celebrates in an identical way', 'Winter celebrations are only found in one single country'], 0),
   ('Which of these is an example of a winter tradition?', ['Lighting candles together as a family', 'Planting a garden in July', 'Swimming at an outdoor beach', 'Harvesting summer crops'], 0),
   ('Why do many winter celebrations include gathering with family or community?', ['Coming together helps people feel connected and share warmth during the cold season', 'Gathering with others has no connection to winter celebrations', 'Winter celebrations always keep people apart', 'Families never gather during winter'], 0)])

# ─── DAY 106 ────────────────────────────────────────────────────────────────
d106_lang = sub('Language', 'Blends: fr, tr, pr',
  'Students learn to read and spell words that begin with the consonant blends fr, tr, and pr, hearing each consonant sound in the blend.',
  [('Name a word that starts with the fr blend, like frog.', ['frog', 'fry', 'free', 'friend']),
   ('Name a word that starts with the tr blend, like tree.', ['tree', 'train', 'truck', 'trip']),
   ('Name a word that starts with the pr blend, like present.', ['present', 'pretty', 'print', 'prize'])],
  [('Which word starts with the fr blend?', ['Frog', 'Tree', 'Prize', 'Snail'], 0),
   ('Which word starts with the tr blend?', ['Train', 'Frog', 'Print', 'Snail'], 0),
   ('Which word starts with the pr blend?', ['Prize', 'Frog', 'Train', 'Snail'], 0),
   ('In the word tree, which two letters make the beginning blend?', ['tr', 'ee', 'tt', 're'], 0),
   ('Why is it helpful to practise blends like fr, tr, and pr?', ['It helps us read and spell many new words that start the same way', 'Blends never appear in real words', 'It makes reading more difficult', 'It only matters for one single word'], 0)])

d106_math = sub('Math', 'Estimating Before Measuring',
  'Students practise making a reasonable guess, or estimate, about a length or amount before measuring it exactly, then compare their estimate to the real measurement.',
  [('What do we call a reasonable guess made before measuring?', ['an estimate', 'estimate']),
   ('Why might we estimate before measuring something exactly?', ['to make a smart guess first', 'to practise guessing']),
   ('If you guess a pencil is about 10 cubes long, what is that guess called?', ['an estimate', 'estimate'])],
  [('What is an estimate?', ['A reasonable guess made before measuring exactly', 'An exact measurement with no guessing', 'A type of shape', 'A kind of number pattern'], 0),
   ('Why might someone estimate the length of a table before measuring it with a ruler?', ['It gives a reasonable idea of the length before checking the exact size', 'Estimating has no real purpose', 'Estimating always gives the exact same number as measuring', 'It replaces the need to ever measure at all'], 0),
   ('If you estimate a book is about 20 cubes long, what should you do next to check?', ['Measure the book with the cubes to see how close the estimate was', 'Never measure the book at all', 'Change the size of the book', 'Ignore the estimate completely'], 0),
   ('Is an estimate expected to be the exact same as a real measurement every time?', ['No, but it should be reasonably close', 'Yes, it must be exactly the same every time', 'An estimate has no connection to a real measurement', 'Estimates are always wildly different from real measurements'], 0),
   ('Why is practising estimation a useful math skill in everyday life?', ['It helps us make quick, reasonable guesses about size or amount', 'It has no use in everyday life', 'It replaces the need for exact measurements forever', 'Estimating is only useful for very large numbers'], 0)])

d106_sci = sub('Science', 'Simple Circuits: How a Light Bulb Turns On',
  'Students learn that a simple circuit needs a battery, a wire, and a light bulb connected in a loop for electricity to flow and make the bulb light up.',
  [('Name one part needed to make a simple circuit, like a battery.', ['battery', 'wire', 'light bulb']),
   ('Does electricity need to flow in a complete loop to light a bulb?', ['yes']),
   ('What happens to a light bulb when a circuit is complete?', ['it lights up', 'it turns on'])],
  [('What is needed to make a simple circuit light up a bulb?', ['A battery, a wire, and a light bulb connected in a loop', 'Only a light bulb by itself', 'Only water', 'Nothing at all'], 0),
   ('What happens when a circuit is broken, or not connected in a full loop?', ['The light bulb does not light up', 'The light bulb always stays lit', 'The battery disappears', 'Nothing changes at all'], 0),
   ('What provides the electricity in a simple circuit like this?', ['The battery', 'The light bulb', 'The wire alone', 'The air around it'], 0),
   ('Why must the wire, battery, and bulb be connected in a complete loop?', ['Electricity needs an unbroken path to flow all the way around and light the bulb', 'A complete loop has no effect on whether the bulb lights up', 'Electricity can flow even without a complete loop', 'The bulb lights up only when the loop is broken'], 0),
   ('Why is learning about simple circuits useful for understanding everyday electronics?', ['Many devices use circuits made of a power source, wires, and a part like a bulb', 'Circuits have no connection to everyday electronics', 'Electronics never use anything like a circuit', 'This concept only applies to one single light bulb'], 0)])

d106_ss = sub('SocialStudies', 'How Goods Travel: From Factory to Store',
  'Students learn that many goods travel a long journey, from being made in a factory, to being shipped by truck, train, or boat, before arriving at a store.',
  [('Where are many goods first made?', ['a factory', 'in a factory']),
   ('Name one way goods might travel to a store, like by truck.', ['by truck', 'by train', 'by boat']),
   ('Where do goods usually end up after their journey?', ['a store', 'at the store'])],
  [('Where are many goods first made?', ['In a factory', 'On the moon', 'Inside a store only', 'Underground caves only'], 0),
   ('Name one way that goods might travel from a factory to a store.', ['By truck', 'By walking alone', 'By floating in the air', 'By teleporting instantly'], 0),
   ('Why might a good travel a long distance before reaching a store shelf?', ['It may be made far away and needs to be shipped to where people will buy it', 'Goods are always made right inside the store', 'Goods never actually need to travel anywhere', 'Stores make every good themselves'], 0),
   ('What might slow down or speed up how quickly goods travel to a store?', ['The distance travelled and the type of transportation used', 'The colour of the goods', 'The weather has no effect on transportation at all', 'Nothing ever affects how goods travel'], 0),
   ('Why is understanding how goods travel helpful for understanding what we buy?', ['It helps us see the journey and effort behind everyday items in a store', 'It has no connection to the items we buy', 'Goods appear in stores with no journey at all', 'This concept only applies to food items'], 0)])

# ─── DAY 107 ────────────────────────────────────────────────────────────────
d107_lang = sub('Language', 'Common and Proper Nouns',
  'Students learn that a common noun names a general person, place, or thing, while a proper noun names a specific one and begins with a capital letter.',
  [('Does a proper noun begin with a capital letter?', ['yes']),
   ('Is dog a common noun or a proper noun?', ['common noun', 'common']),
   ('Is Toronto a common noun or a proper noun?', ['proper noun', 'proper'])],
  [('Which of these is a proper noun?', ['Toronto', 'city', 'school', 'dog'], 0),
   ('Which of these is a common noun?', ['Dog', 'Canada', 'Toronto', 'Monday'], 0),
   ('What is true about proper nouns?', ['They name a specific person, place, or thing and start with a capital letter', 'They are always lowercase', 'They only name animals', 'They never appear in sentences'], 0),
   ('Which sentence uses a proper noun correctly?', ['We visited Toronto last summer.', 'We visited toronto last summer.', 'We visited a City last summer.', 'We visited the CITY last summer.'], 0),
   ('Why is it important to capitalize proper nouns in writing?', ['It shows the reader that the word names something specific', 'Capital letters have no real purpose', 'It makes every sentence a question', 'It changes the meaning of a common noun'], 0)])

d107_math = sub('Math', 'Counting Forward and Backward Within 200',
  'Students practise counting forward and backward by ones within 200, strengthening their understanding of how numbers increase and decrease in order.',
  [('What number comes right before 150?', ['149', 'one hundred forty-nine']),
   ('What number comes right after 199?', ['200', 'two hundred']),
   ('Count backward from 103 by ones: 103, 102, ___.', ['101', 'one hundred one'])],
  [('What number comes right before 120?', ['119', '121', '118', '110'], 0),
   ('What number comes right after 168?', ['169', '170', '167', '178'], 0),
   ('Counting backward from 175, what comes next: 175, 174, ___?', ['173', '176', '172', '180'], 0),
   ('Counting forward from 196, what comes next: 196, 197, ___?', ['198', '199', '200', '195'], 0),
   ('Why is practising counting forward and backward a useful math skill?', ['It builds a strong understanding of how numbers relate and increase or decrease', 'It has no connection to understanding numbers', 'Counting backward is never actually useful', 'It only matters for very large numbers'], 0)])

d107_sci = sub('Science', 'Wind: Moving Air We Cannot See',
  'Students learn that wind is moving air, which we cannot see but can feel, and observe through moving leaves, flags, and clouds.',
  [('Can we see wind directly?', ['no']),
   ('What is wind?', ['moving air', 'air that moves']),
   ('Name one thing that shows us wind is blowing, like moving leaves.', ['moving leaves', 'a flag waving', 'moving clouds'])],
  [('What is wind?', ['Moving air', 'A type of cloud', 'Frozen water', 'A kind of light'], 0),
   ('Can we see wind directly with our eyes?', ['No, but we can feel it and see its effects', 'Yes, wind is always clearly visible', 'Wind has no effect on anything around us', 'Wind can only be heard, never felt'], 0),
   ('Which of these shows us that wind is blowing?', ['Leaves moving on a tree', 'A rock sitting still', 'A closed door with no movement', 'A book resting on a table'], 0),
   ('Why can we feel wind even though we cannot see it?', ['Moving air pushes against our skin, even though air itself is invisible', 'Wind is not actually real', 'We can always see wind clearly, just like water', 'Wind only exists indoors'], 0),
   ('Why might a flag be a good way to notice wind outside?', ['A flag moves and waves when air pushes against it, showing the wind is blowing', 'Flags never move because of wind', 'Flags only move when there is no wind at all', 'Wind has no effect on flags'], 0)])

d107_ss = sub('SocialStudies', 'Canadas Two Official Languages: English and French',
  'Students learn that Canada has two official languages, English and French, and that both languages are used in government documents and services.',
  [('Name one of Canadas two official languages.', ['English', 'French']),
   ('How many official languages does Canada have?', ['2', 'two']),
   ('Are both English and French used in Canadian government services?', ['yes'])],
  [('How many official languages does Canada have?', ['Two', 'One', 'Five', 'Ten'], 0),
   ('Which two languages are Canadas official languages?', ['English and French', 'English and Spanish', 'French and German', 'English only'], 0),
   ('Where might you see both English and French used together in Canada?', ['On government documents and signs', 'Only on private restaurant menus', 'Nowhere at all', 'Only in one single province'], 0),
   ('Why does Canada have two official languages?', ['It reflects Canadas history with both English and French-speaking communities', 'It has no historical reason at all', 'Only one language has ever been used in Canada', 'Every country in the world has exactly two official languages'], 0),
   ('Why might learning about Canadas official languages help us understand the country better?', ['It shows part of the history and diversity of communities across Canada', 'It has no connection to understanding Canada', 'Official languages have no real importance', 'Canada has never had any official languages'], 0)])

# ─── DAY 108 ────────────────────────────────────────────────────────────────
d108_lang = sub('Language', 'Story Problem and Solution',
  'Students learn to identify the problem a character faces in a story and the solution, or how the character solves it, by the end.',
  [('What do we call the trouble a character faces in a story?', ['the problem', 'a problem']),
   ('What do we call how a character fixes the trouble in a story?', ['the solution', 'a solution']),
   ('Why do most stories include a problem and a solution?', ['to make the story interesting', 'so the story has a plot'])],
  [('What is the problem in a story?', ['The trouble or challenge a character faces', 'The very last word in the story', 'The name of the author', 'The cover picture of the book'], 0),
   ('What is the solution in a story?', ['How the character solves the problem', 'The title of the book', 'A list of characters', 'The setting of the story'], 0),
   ('Why do most stories include both a problem and a solution?', ['It gives the story a clear plot that keeps readers interested', 'Stories never actually need a problem', 'A solution never matters in a story', 'It makes the story less interesting'], 0),
   ('If a character loses their dog and then finds it, what is the solution?', ['Finding the dog', 'Losing the dog', 'The characters name', 'The title of the story'], 0),
   ('Why is identifying the problem and solution helpful when retelling a story?', ['It helps summarize the most important parts of what happened', 'It leaves out the most important parts of the story', 'It has no connection to understanding a story', 'Problems and solutions never appear in stories'], 0)])

d108_math = sub('Math', 'Fact Families to 20',
  'Students explore fact families, sets of related addition and subtraction facts that use the same three numbers, extending their work to numbers within 20.',
  [('If 8 plus 9 equals 17, what subtraction fact is in the same fact family?', ['17 minus 9 equals 8', '17 minus 8 equals 9']),
   ('Do fact families use the same three numbers in different addition and subtraction facts?', ['yes']),
   ('If 6 plus 7 equals 13, name one more fact in that fact family.', ['7 plus 6 equals 13', '13 minus 6 equals 7', '13 minus 7 equals 6'])],
  [('If 9 plus 6 equals 15, which subtraction fact belongs to the same fact family?', ['15 minus 6 equals 9', '15 minus 9 equals 15', '9 minus 6 equals 3', '6 minus 9 equals 3'], 0),
   ('Which three numbers make up the fact family with 7, 8, and 15?', ['7 plus 8 equals 15, 15 minus 7 equals 8, 15 minus 8 equals 7', '7 plus 15 equals 22', '8 minus 7 equals 1', '15 plus 15 equals 30'], 0),
   ('What do all the facts in one fact family have in common?', ['They use the same three numbers', 'They always use completely different numbers', 'They are never related to each other', 'They only include addition facts'], 0),
   ('If 5 plus 12 equals 17, what is 17 minus 12?', ['5', '12', '17', '29'], 0),
   ('Why are fact families a helpful way to learn addition and subtraction together?', ['They show how addition and subtraction facts are connected using the same numbers', 'They make addition and subtraction completely unrelated', 'They only work for numbers larger than 100', 'They have no real use in math'], 0)])

d108_sci = sub('Science', 'Animal Tracks: Footprints in the Snow',
  'Students learn that many animals leave tracks, or footprints, in snow or mud, and that the shape and size of tracks can help us identify which animal made them.',
  [('What do we call the footprints an animal leaves behind?', ['tracks', 'animal tracks']),
   ('Can the shape of a track help us know which animal made it?', ['yes']),
   ('Name one place animal tracks are easy to see, like in snow.', ['snow', 'mud'])],
  [('What are animal tracks?', ['Footprints an animal leaves behind', 'A type of animal food', 'A kind of animal home', 'A sound an animal makes'], 0),
   ('Where might animal tracks be easiest to see?', ['In snow or soft mud', 'In the middle of a lake', 'Inside a closed box', 'On a cloudy sky'], 0),
   ('How can the shape and size of a track help scientists?', ['It can help identify which animal made the track', 'It never gives any useful information', 'It only shows the weather', 'It tells us the animals favourite food'], 0),
   ('Why might a rabbit track look different from a deer track?', ['Different animals have differently shaped and sized feet', 'All animal feet are exactly the same shape', 'Tracks never show any differences between animals', 'Rabbits and deer never leave any tracks'], 0),
   ('Why do scientists sometimes study animal tracks instead of the animals themselves?', ['Tracks can show which animals visited an area even if the animal itself is not seen', 'Tracks give no useful information at all', 'Animals never leave any tracks behind', 'Studying tracks is always less useful than seeing the animal'], 0)])

d108_ss = sub('SocialStudies', 'Helping New Students Feel Welcome at School',
  'Students learn simple ways to help new students feel welcome at school, such as introducing themselves, sharing information, and including others in games.',
  [('Name one way to help a new student feel welcome, like introducing yourself.', ['introducing yourself', 'saying hello', 'including them in a game']),
   ('Why might a new student feel nervous on their first day?', ['everything is new to them', 'they do not know anyone yet']),
   ('How can including someone in a game help them feel welcome?', ['it helps them feel included', 'it makes them feel part of the group'])],
  [('What is one way to help a new student feel welcome?', ['Introducing yourself and saying hello', 'Ignoring them completely', 'Avoiding eye contact', 'Excluding them from games'], 0),
   ('Why might a new student feel nervous on their first day at a school?', ['Everything, like the building and the people, is new to them', 'New students never feel nervous at all', 'They already know everyone at the school', 'Being new never has any effect on how someone feels'], 0),
   ('How can inviting a new student to play a game help them?', ['It helps them feel included and make new friends', 'It has no effect on how they feel', 'It always makes them feel more left out', 'Games have no connection to feeling welcome'], 0),
   ('Why is being kind to new students an important part of being a good classmate?', ['It helps everyone feel safe, included, and ready to learn together', 'Kindness has no real effect on a classroom', 'Only teachers need to be kind to new students', 'New students never need any extra kindness'], 0),
   ('Why might sharing simple information, like where the library is, help a new student?', ['It helps them feel more comfortable and confident finding their way around', 'Sharing information never helps anyone feel comfortable', 'New students already know where everything is', 'This kind of help has no real value'], 0)])

# ─── DAY 109 ────────────────────────────────────────────────────────────────
d109_lang = sub('Language', 'Author Message: What Is the Story Teaching Us',
  'Students learn to think about the message or lesson an author wants readers to take away from a story, sometimes called the moral or big idea.',
  [('What do we call the lesson or big idea an author wants us to learn?', ['the message', 'the moral']),
   ('Why might an author write a story with a message?', ['to teach the reader something', 'to share a lesson']),
   ('Name a possible message a story about sharing might teach.', ['sharing is kind', 'it is good to share'])],
  [('What is an author message in a story?', ['The lesson or big idea the author wants readers to take away', 'The name of the main character', 'The colour of the book cover', 'The number of pages in the book'], 0),
   ('Why might an author write a story about a character who learns to be kind?', ['To teach readers a lesson about kindness', 'To make the story longer for no reason', 'Authors never include any lessons in stories', 'To confuse the reader on purpose'], 0),
   ('Which of these is most likely a story message?', ['Being honest is important, even when it is hard.', 'The sky is blue.', 'The book has one hundred pages.', 'The story was published last year.'], 0),
   ('Why is thinking about an author message helpful when reading a story?', ['It helps readers understand a deeper meaning, not just the events', 'It has no connection to understanding a story', 'Stories never actually have any message', 'It only matters for very short stories'], 0),
   ('How might two readers find slightly different messages in the same story?', ['Readers can connect a story to their own experiences in different ways', 'Every reader must always find the exact same message', 'Stories never have more than one possible meaning', 'Messages are printed directly on the last page of every book'], 0)])

d109_math = sub('Math', 'Combining Coins and Bills to Make an Amount',
  'Students practise combining different coins, like nickels and dimes, along with a one-dollar bill, to make a specific total amount of money.',
  [('How many cents is one dime worth?', ['10', 'ten cents']),
   ('How many cents is one nickel worth?', ['5', 'five cents']),
   ('If you have one dollar bill and one dime, how much money do you have in total?', ['1 dollar and 10 cents', '$1.10'])],
  [('How much is one dime worth?', ['10 cents', '5 cents', '25 cents', '1 cent'], 0),
   ('If you have 2 dimes and 1 nickel, how much money do you have?', ['25 cents', '20 cents', '30 cents', '15 cents'], 0),
   ('If you have a one-dollar bill and 3 dimes, how much money do you have in total?', ['1 dollar and 30 cents', '1 dollar and 3 cents', '3 dollars and 10 cents', '30 cents only'], 0),
   ('Which combination of coins makes exactly 15 cents?', ['One dime and one nickel', 'Two dimes', 'Three nickels and a dime', 'One dime alone'], 0),
   ('Why is it useful to practise combining coins and bills to make an amount?', ['It helps us understand how to pay for things in everyday life', 'Coins and bills are never actually combined in real life', 'It has no connection to using money', 'This skill is only useful for very large amounts of money'], 0)])

d109_sci = sub('Science', 'Ants: Tiny but Mighty Workers',
  'Students learn that ants are insects that live and work together in large colonies, sharing jobs like gathering food, building tunnels, and caring for young ants.',
  [('Are ants insects or mammals?', ['insects']),
   ('Do ants usually live alone or in large groups called colonies?', ['in large groups', 'colonies']),
   ('Name one job an ant might do, like gathering food.', ['gathering food', 'building tunnels', 'caring for young ants'])],
  [('What kind of animal is an ant?', ['An insect', 'A mammal', 'A reptile', 'A bird'], 0),
   ('Do ants usually live alone or in large groups?', ['In large groups called colonies', 'Always completely alone', 'Only in pairs of two', 'Ants never live anywhere at all'], 0),
   ('Name one job that ants might share within their colony.', ['Gathering food', 'Flying airplanes', 'Driving cars', 'Building houses out of bricks'], 0),
   ('Why might ants be able to carry objects much heavier than their own body?', ['Ants have strong muscles compared to their small size', 'Ants are never able to carry anything at all', 'Ants only carry things lighter than a single grain of sand', 'This has no connection to how ants are built'], 0),
   ('Why is working together in a colony helpful for ants?', ['Sharing jobs helps the whole colony survive and find enough food', 'Working together never helps any animal survive', 'Ants always work completely alone with no cooperation', 'Colonies have no real purpose for ants'], 0)])

d109_ss = sub('SocialStudies', 'Taking Care of Shared Spaces: Parks and Playgrounds',
  'Students learn that parks and playgrounds are shared spaces that everyone in a community can enjoy, and that taking care of them helps keep them nice for everyone.',
  [('Name one shared space in a community, like a park.', ['a park', 'a playground']),
   ('Why should we take care of shared spaces like parks?', ['so everyone can enjoy them', 'to keep them nice for everyone']),
   ('Name one way to take care of a park, like picking up litter.', ['picking up litter', 'not littering', 'being gentle with equipment'])],
  [('What is a shared space, like a park or playground?', ['A place everyone in the community can use and enjoy', 'A space only one family is allowed to use', 'A private backyard', 'A space no one is allowed to enter'], 0),
   ('Why is it important to take care of shared spaces like parks?', ['So they stay clean and enjoyable for everyone in the community', 'Shared spaces never need any care at all', 'Only one person is responsible for a whole park', 'Taking care of shared spaces has no real benefit'], 0),
   ('Which of these is a way to help take care of a playground?', ['Picking up litter and putting it in the bin', 'Leaving garbage on the ground', 'Breaking playground equipment on purpose', 'Ignoring any mess that is made'], 0),
   ('Why might a park feel less enjoyable if people do not take care of it?', ['Litter or damage can make the space unpleasant or unsafe to use', 'A messy park always feels exactly the same as a clean one', 'Taking care of a park never changes how it feels to visit', 'Parks are never affected by how people treat them'], 0),
   ('Why is caring for shared spaces considered a responsibility of the whole community?', ['Everyone uses and benefits from these spaces, so everyone can help keep them nice', 'Only city workers are ever responsible for shared spaces', 'Shared spaces have no connection to the community', 'Community members have no role in caring for shared spaces'], 0)])

# ─── DAY 110 (REVIEW) ───────────────────────────────────────────────────────
d110_lang = sub('Language', 'Language Review: Nouns, Sentences, and Story Elements',
  'Students review recent Language topics: possessive nouns, sequencing in nonfiction, exclamatory sentences, word families, setting, blends, common and proper nouns, story problem and solution, and author message.',
  [('What do we add to a name to show ownership, like Sams hat?', ['apostrophe s', 's']),
   ('What punctuation mark ends an exclamatory sentence?', ['exclamation mark', '!']),
   ('What does the setting of a story tell us?', ['where and when it happens', 'where a story takes place'])],
  [('Which phrase correctly shows ownership?', ['Mias ball', 'Mia ball', 'Ball Mia', 'The ball Mia'], 0),
   ('Which sentence is exclamatory?', ['We won the game!', 'We won the game.', 'Did we win?', 'We might win'], 0),
   ('Which word is a proper noun?', ['Toronto', 'city', 'school', 'dog'], 0),
   ('What do we call the trouble a character faces in a story?', ['The problem', 'The title', 'The cover', 'The author'], 0),
   ('What do we call the lesson an author wants readers to learn?', ['The message', 'The page number', 'The setting only', 'The cover colour'], 0)])

d110_math = sub('Math', 'Math Review: Place Value, Operations, and Data',
  'Students review recent Math topics: place value to 200, two-digit addition and subtraction, line plots, comparing 2D and 3D shapes, estimating, counting to 200, fact families, and combining coins.',
  [('In the number 156, how many hundreds are there?', ['1', 'one']),
   ('What is 23 plus 15?', ['38', 'thirty-eight']),
   ('How many cents is one dime worth?', ['10', 'ten cents'])],
  [('In the number 174, how many hundreds are there?', ['1', '7', '4', '0'], 0),
   ('What is 12 plus 24?', ['36', '35', '38', '34'], 0),
   ('Which of these is a 3D shape?', ['A sphere', 'A circle', 'A triangle', 'A rectangle'], 0),
   ('What is an estimate?', ['A reasonable guess made before measuring exactly', 'An exact measurement', 'A type of shape', 'A number pattern'], 0),
   ('If 8 plus 9 equals 17, what subtraction fact is in the same fact family?', ['17 minus 9 equals 8', '17 minus 8 equals 9 only', '9 minus 8 equals 1', '8 minus 9 equals negative 1'], 0)])

d110_sci = sub('Science', 'Science Review: Our Bodies, Animals, and Energy',
  'Students review recent Science topics: skin, owls, bats, frog life cycles, penguins, simple circuits, wind, animal tracks, and ants.',
  [('What is the largest organ of our body?', ['skin']),
   ('Do bats use echolocation to find food in the dark?', ['yes']),
   ('What is wind?', ['moving air', 'air that moves'])],
  [('What is the largest organ of our body?', ['Skin', 'Heart', 'Brain', 'Lungs'], 0),
   ('When do owls usually hunt for food?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
   ('What is the first stage of a frogs life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'Froglet'], 0),
   ('Can penguins fly through the air?', ['No', 'Yes, very high', 'Only at night', 'Only in summer'], 0),
   ('What kind of animal is an ant?', ['An insect', 'A mammal', 'A reptile', 'A bird'], 0)])

d110_ss = sub('SocialStudies', 'Social Studies Review: Community, Money, and Culture',
  'Students review recent Social Studies topics: municipal services, Canadas territories, bartering, community centres, winter celebrations, official languages, and shared spaces.',
  [('Name one municipal service, like garbage pickup.', ['garbage pickup', 'clean water', 'road repairs']),
   ('How many official languages does Canada have?', ['2', 'two']),
   ('Name one shared space in a community, like a park.', ['a park', 'a playground'])],
  [('What is a municipal service?', ['A service a local government provides, like garbage pickup', 'A toy sold in stores', 'A type of food', 'A kind of weather'], 0),
   ('How many territories does Canada have?', ['Three', 'One', 'Ten', 'Thirteen'], 0),
   ('What is bartering?', ['Trading goods directly without using money', 'Buying goods only with coins', 'Giving goods away for free', 'A type of modern online shopping'], 0),
   ('Which two languages are Canadas official languages?', ['English and French', 'English and Spanish', 'French and German', 'English only'], 0),
   ('Why is it important to take care of shared spaces like parks?', ['So they stay clean and enjoyable for everyone in the community', 'Shared spaces never need any care at all', 'Only one person is responsible for a whole park', 'Taking care of shared spaces has no real benefit'], 0)])

g1_101_110 = [
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
    _rebalance_answer_positions(g1_101_110)
    append_worksheet_days(1, g1_101_110)
