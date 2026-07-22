#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 91-100 -- seventh batch extending Grade 0
past the Days 81-90 batch, completing Days 1-100. This is a self-contained
script (does NOT use gen_curriculum.py's sub()/day()/append_to() helpers,
since those do not support a worksheet field) modeled exactly on
gen_grade0_days81_90.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-90 topics (see data/grade0.ts / data/grade0.json). New word families
(-ot, -et), new punctuation/comprehension skills (capital letters, cause
and effect, story mood, compare and contrast, environmental print,
sentence building, adding -es), new math concepts (subitizing, one-to-one
correspondence, new position words, 3D shape attributes, covering space
with tiles, ways to make 5, comparing height, loonies/toonies, triangle
and rectangle), new science topics (chicken life cycle, pond and mountain
habitats, gravity, static electricity, moon phases, germs, fossils,
erosion), and new social studies topics (farmers, construction workers,
Remembrance Day, laws, emergency vehicles, city vs country life, Ottawa,
weather safety, global citizenship) were all selected specifically
because none of those exact ideas appear in Days 1-90. No embedded ASCII
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


# ─── DAY 91 ─────────────────────────────────────────────────────────────────
d91_lang = sub('Language', 'Word Families: -ot Words',
  'Students explore the -ot word family, learning that changing the first letter of words like hot, pot, and dot creates new rhyming words that share the same ending sound.',
  [('Change the h in hot to p. What new word do you make?', ['pot']),
   ('Change the p in pot to d. What new word do you make?', ['dot']),
   ('Name one more word that rhymes with hot, pot, and dot.', ['not', 'cot', 'lot', 'jot'])],
  [('Which word rhymes with hot?', ['Pot', 'Dog', 'Sun', 'Cup'], 0),
   ('Change the h in hot to d. What new word do you make?', ['Dot', 'Dog', 'Dad', 'Din'], 0),
   ('Which of these words is part of the -ot word family?', ['Cot', 'Cat', 'Cut', 'Cop'], 0),
   ('Words in the -ot family all end with the same ___.', ['Sound', 'Colour', 'Picture', 'Number'], 0),
   ('Which word does not belong in the -ot word family?', ['Sun', 'Hot', 'Pot', 'Dot'], 0)])

d91_math = sub('Math', 'Subitizing: Knowing Amounts Without Counting',
  'Students practise subitizing, which means looking at a small group of dots or objects and knowing how many there are right away without counting one by one.',
  [('What do we call knowing how many objects are in a small group without counting?', ['subitizing']),
   ('If you see a group of 3 dots arranged like a triangle, can you know it is 3 without counting?', ['yes']),
   ('Name one way subitizing can help us in math, like being faster at counting.', ['being faster', 'quick counting', 'saving time'])],
  [('What do we call knowing how many objects are in a group without counting one by one?', ['Subitizing', 'Sorting', 'Measuring', 'Erasing'], 0),
   ('If you instantly know a group of 2 dots has 2 without counting, what skill are you using?', ['Subitizing', 'Estimating length', 'Skip counting', 'Sorting'], 0),
   ('Why is subitizing a helpful math skill?', ['It helps us know an amount quickly', 'It makes numbers disappear', 'It replaces counting forever', 'It only works with big numbers'], 0),
   ('Which group size is easiest to subitize without counting?', ['A small group like 3', 'A huge group like 100', 'An invisible group', 'A group with no objects'], 0),
   ('Subitizing works best with ___ groups of objects.', ['Small', 'Enormous', 'Invisible', 'Moving'], 0)])

d91_sci = sub('Science', 'Life Cycle of a Chicken: Egg to Hen',
  'Students learn that a chicken begins life inside an egg, hatches into a fluffy chick, and grows through several stages into a fully grown hen or rooster.',
  [('What does a baby chick hatch out of?', ['egg', 'an egg']),
   ('What is a baby chicken called right after it hatches?', ['chick', 'a chick']),
   ('Name one stage in the life cycle of a chicken, like egg or chick.', ['egg', 'chick', 'hen', 'rooster'])],
  [('What does a baby chick hatch out of?', ['An egg', 'A shell of sand', 'A flower', 'A rock'], 0),
   ('What is a baby chicken called right after it hatches?', ['A chick', 'A calf', 'A cub', 'A kit'], 0),
   ('Put these in order: egg, chick, ___.', ['A grown hen or rooster', 'Nothing at all', 'Only more eggs', 'A fish'], 0),
   ('A life cycle shows how a living thing ___.', ['Grows and changes over time', 'Never changes at all', 'Turns into a rock', 'Disappears completely'], 0),
   ('Which of these is part of a chicken life cycle?', ['Egg', 'Sandcastle', 'Cloud', 'Rainbow'], 0)])

d91_ss = sub('SocialStudies', 'Our Farmers: Growing the Food We Eat',
  'Students learn about the job of a farmer, a community helper who grows crops and raises animals so families can have food to eat.',
  [('What do we call a person who grows crops and raises animals for food?', ['farmer']),
   ('Name one thing a farmer might grow, like corn or wheat.', ['corn', 'wheat', 'vegetables', 'fruit']),
   ('Does the food we eat often start on a farm?', ['yes'])],
  [('What do we call a person who grows crops and raises animals for food?', ['A farmer', 'A librarian', 'A dentist', 'A mayor'], 0),
   ('Which of these might a farmer grow?', ['Corn', 'Cars', 'Books', 'Shoes'], 0),
   ('Why is a farmer an important community helper?', ['They grow the food that many people eat', 'They fix broken pipes', 'They deliver mail', 'They teach at school'], 0),
   ('Where does a farmer usually work?', ['On a farm', 'In a library', 'In a hospital', 'In a bank'], 0),
   ('Food on our table often begins its journey at a ___.', ['Farm', 'Museum', 'Bank', 'School'], 0)])

# ─── DAY 92 ─────────────────────────────────────────────────────────────────
d92_lang = sub('Language', 'Word Families: -et Words',
  'Students explore the -et word family, learning that changing the first letter of words like wet, pet, and net creates new rhyming words that share the same ending sound.',
  [('Change the w in wet to p. What new word do you make?', ['pet']),
   ('Change the p in pet to n. What new word do you make?', ['net']),
   ('Name one more word that rhymes with wet, pet, and net.', ['jet', 'met', 'set', 'get'])],
  [('Which word rhymes with wet?', ['Pet', 'Dog', 'Sun', 'Cup'], 0),
   ('Change the w in wet to n. What new word do you make?', ['Net', 'Nap', 'Nut', 'Nod'], 0),
   ('Which of these words is part of the -et word family?', ['Jet', 'Jam', 'Jog', 'Jab'], 0),
   ('Words in the -et family all end with the same ___.', ['Sound', 'Colour', 'Picture', 'Number'], 0),
   ('Which word does not belong in the -et word family?', ['Sun', 'Wet', 'Pet', 'Net'], 0)])

d92_math = sub('Math', 'One-to-One Correspondence: Touching and Counting Carefully',
  'Students practise one-to-one correspondence, touching each object exactly once while saying one number word, so the last number said tells how many objects there are in total.',
  [('When counting objects, should you touch each one only one time?', ['yes']),
   ('If you count 5 blocks by touching each one once, what number do you say last?', ['5', 'five']),
   ('What might happen if you touch one block two times while counting?', ['you get the wrong count', 'wrong answer', 'miscount'])],
  [('What does it mean to use one-to-one correspondence while counting?', ['Touching each object exactly once as you count', 'Touching every object many times', 'Never touching the objects', 'Counting only the biggest object'], 0),
   ('If you touch 4 toys once each while counting, what is the last number you say?', ['4', '3', '5', '1'], 0),
   ('Why is touching each object only once important while counting?', ['It helps you count accurately without mistakes', 'It makes counting take longer for no reason', 'It changes how many objects there are', 'It has no effect on counting'], 0),
   ('If you skip touching one object while counting a group, what might happen?', ['You might count one too few', 'You will always get the right answer', 'The objects will disappear', 'Nothing changes at all'], 0),
   ('The last number word you say while counting objects one by one tells you ___.', ['How many objects there are in all', 'The colour of the objects', 'The shape of the objects', 'Nothing useful'], 0)])

d92_sci = sub('Science', 'Pond Habitats: Life In and Around the Water',
  'Students learn that a pond is a small habitat of still water where animals such as frogs, ducks, and fish live in or near the water together.',
  [('What do we call a small habitat of still water where frogs and ducks might live?', ['pond', 'a pond']),
   ('Name one animal that can live in or near a pond, like a frog or duck.', ['frog', 'duck', 'fish']),
   ('Is a pond usually made of moving ocean waves or still water?', ['still water'])],
  [('What is a pond?', ['A small habitat of still water', 'A huge ocean', 'A dry desert', 'A snowy mountain'], 0),
   ('Which animal is commonly found living in or near a pond?', ['A frog', 'A camel', 'A polar bear', 'A lion'], 0),
   ('What kind of water does a pond usually have?', ['Still, calm water', 'Giant crashing waves', 'No water at all', 'Boiling hot water'], 0),
   ('Why might ducks like living near a pond?', ['They can swim, find food, and rest near the water', 'Ducks never go near water', 'Ponds have no water for ducks', 'Ducks only live in deserts'], 0),
   ('A pond is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d92_ss = sub('SocialStudies', 'Our Construction Workers: Building Our Community',
  'Students learn about the job of a construction worker, a community helper who builds and repairs houses, schools, and other important buildings.',
  [('What do we call a worker who builds and repairs buildings?', ['construction worker']),
   ('Name one thing a construction worker might build, like a house or school.', ['house', 'school', 'building']),
   ('Do construction workers often wear a hard hat to stay safe?', ['yes'])],
  [('What do we call a worker who builds and repairs buildings?', ['A construction worker', 'A librarian', 'A mayor', 'A farmer'], 0),
   ('Which of these might a construction worker build?', ['A house', 'A poem', 'A song', 'A recipe'], 0),
   ('Why do construction workers often wear hard hats?', ['To keep their heads safe while they work', 'Hats are only for decoration', 'Hats make buildings taller', 'Construction workers never wear hats'], 0),
   ('Which tool might a construction worker use?', ['A hammer', 'A stethoscope', 'A cash register', 'A library card'], 0),
   ('Construction workers help our community by ___.', ['Building and repairing important places', 'Delivering mail', 'Teaching at school', 'Growing food'], 0)])

# ─── DAY 93 ─────────────────────────────────────────────────────────────────
d93_lang = sub('Language', 'Making New Words: Adding -es',
  'Students learn that adding -es to some words, such as changing box to boxes or wish to wishes, shows there is more than one.',
  [('Add -es to the word box. What new word do you make?', ['boxes']),
   ('Add -es to the word wish. What new word do you make?', ['wishes']),
   ('Does adding -es to a word usually mean there is only one, or more than one?', ['more than one'])],
  [('Add -es to the word box. What new word do you make?', ['Boxes', 'Boxs', 'Boxies', 'Boxen'], 0),
   ('Add -es to the word wish. What new word do you make?', ['Wishes', 'Wishs', 'Wishies', 'Wish'], 0),
   ('Adding -es to a word usually shows there is ___.', ['More than one', 'Only one', 'No amount', 'A colour'], 0),
   ('Which word correctly shows more than one dish?', ['Dishes', 'Dishs', 'Dish', 'Dishies'], 0),
   ('Which word correctly shows more than one bus?', ['Buses', 'Bus', 'Buss', 'Busies'], 0)])

d93_math = sub('Math', 'Position Words: Above, Below, Inside, and Outside',
  'Students learn positional language, describing where an object is located using words such as above, below, inside, and outside.',
  [('If a bird is flying over a tree, is the bird above or below the tree?', ['above']),
   ('If a toy is in a box, is the toy inside or outside the box?', ['inside']),
   ('Name one positional word that describes where something is, like above or below.', ['above', 'below', 'inside', 'outside'])],
  [('If a cloud is floating over a house, where is the cloud?', ['Above the house', 'Below the house', 'Inside the house', 'Under the ground'], 0),
   ('If a ball is sitting under a table, where is the ball?', ['Below the table', 'Above the table', 'Inside the table', 'Outside the room'], 0),
   ('If a book is inside a backpack, where is the book?', ['Inside the backpack', 'Outside the backpack', 'Above the backpack', 'Below the backpack'], 0),
   ('If a dog is standing outside a doghouse, where is the dog?', ['Outside the doghouse', 'Inside the doghouse', 'Above the doghouse', 'Below the doghouse'], 0),
   ('Position words like above and below help us describe ___.', ['Where something is located', 'What colour something is', 'How heavy something is', 'What sound something makes'], 0)])

d93_sci = sub('Science', 'Mountain Habitats: Life High Up',
  'Students learn that a mountain is a tall landform habitat where the air is cooler near the top, and animals such as mountain goats and eagles are suited to living there.',
  [('What do we call a very tall landform where some animals live?', ['mountain', 'a mountain']),
   ('Name one animal that can live on a mountain, like a mountain goat or eagle.', ['mountain goat', 'eagle']),
   ('Is the air near the top of a mountain usually cooler or warmer than at the bottom?', ['cooler'])],
  [('What is a mountain?', ['A very tall landform habitat', 'A small pond', 'A flat desert', 'A deep ocean'], 0),
   ('Which animal is well suited to living on a mountain?', ['A mountain goat', 'A fish', 'A whale', 'A camel'], 0),
   ('How is the air near the top of a mountain usually different from the bottom?', ['It is cooler near the top', 'It is always hotter near the top', 'It never changes at all', 'It disappears near the top'], 0),
   ('Why might a mountain goat be good at climbing steep rocky slopes?', ['Its body and feet are suited for climbing safely', 'Mountain goats cannot climb at all', 'Mountain goats only live in oceans', 'Mountain goats avoid rocky places'], 0),
   ('A mountain is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d93_ss = sub('SocialStudies', 'Remembrance Day: Honouring Those Who Served',
  'Students learn that Remembrance Day is a special day in Canada when people wear poppies and take a moment of silence to honour and remember soldiers who served the country.',
  [('What red flower do people often wear on Remembrance Day?', ['poppy', 'a poppy']),
   ('What day of the year is Remembrance Day, if you know it?', ['November 11', 'November 11th']),
   ('Do people take a quiet moment of silence on Remembrance Day to remember soldiers?', ['yes'])],
  [('What red flower do people often wear on Remembrance Day?', ['A poppy', 'A rose', 'A tulip', 'A daisy'], 0),
   ('What do people do during a moment of silence on Remembrance Day?', ['Stay quiet and think about soldiers who served', 'Sing loudly', 'Play games', 'Ignore the day completely'], 0),
   ('Why is Remembrance Day an important day in Canada?', ['It honours and remembers soldiers who served the country', 'It celebrates a birthday', 'It is only for adults', 'It has no meaning at all'], 0),
   ('When is Remembrance Day observed each year in Canada?', ['November 11', 'January 1', 'July 1', 'October 31'], 0),
   ('Wearing a poppy on Remembrance Day is a way to show ___.', ['Respect and remembrance', 'Anger', 'Confusion', 'Excitement about a party'], 0)])

# ─── DAY 94 ─────────────────────────────────────────────────────────────────
d94_lang = sub('Language', 'Compare and Contrast: How Two Things Are Different',
  'Students practise comparing and contrasting two things, such as two animals or two characters, by describing how they are alike and how they are different.',
  [('If you compare a cat and a dog, name one way they are alike.', ['both animals', 'both have fur', 'both are pets']),
   ('If you compare a cat and a dog, name one way they are different.', ['different sounds', 'different size', 'cat meows dog barks']),
   ('What word describes looking at how two things are alike?', ['compare', 'comparing'])],
  [('What does it mean to compare two things?', ['To look at how they are alike', 'To ignore them completely', 'To throw them away', 'To make them disappear'], 0),
   ('What does it mean to contrast two things?', ['To look at how they are different', 'To make them exactly the same', 'To ignore them completely', 'To hide them'], 0),
   ('Which of these is a way a cat and a dog might be alike?', ['Both are animals', 'Both can fly', 'Both live in water', 'Both are plants'], 0),
   ('Which of these is a way a cat and a dog might be different?', ['The sounds they make', 'They are both pets', 'They are both animals', 'They both have fur'], 0),
   ('Comparing and contrasting two characters in a story helps readers understand ___.', ['How the characters are alike and different', 'Only the title of the book', 'Only the colour of the cover', 'Nothing about the story'], 0)])

d94_math = sub('Math', '3D Shapes: Faces, Edges, and Corners',
  'Students explore three-dimensional shapes such as cubes and spheres, learning to describe them using the words faces, edges, and corners.',
  [('What do we call the flat sides of a 3D shape, like the sides of a cube?', ['faces']),
   ('What do we call the pointy corners of a 3D shape, like the corners of a cube?', ['corners', 'vertices']),
   ('Does a sphere, like a ball, have any flat faces?', ['no'])],
  [('What do we call the flat sides of a 3D shape?', ['Faces', 'Corners', 'Edges', 'Colours'], 0),
   ('What do we call the pointy points on a 3D shape, like on a cube?', ['Corners', 'Faces', 'Circles', 'Lines'], 0),
   ('How many flat faces does a cube have?', ['6', '2', '4', '8'], 0),
   ('Does a sphere, like a ball, have any flat faces?', ['No, it is completely round', 'Yes, it has 6 faces', 'Yes, it has 4 faces', 'Yes, it has 2 faces'], 0),
   ('An edge on a 3D shape is best described as ___.', ['The line where two faces meet', 'A pointy corner', 'A flat side', 'A round curve only'], 0)])

d94_sci = sub('Science', 'Gravity: Why Things Fall Down',
  'Students learn that gravity is an invisible force that pulls objects down toward the ground, which is why a dropped ball falls instead of floating up.',
  [('What do we call the invisible force that pulls objects down toward the ground?', ['gravity']),
   ('If you drop a ball, does it fall down or float up?', ['falls down', 'down']),
   ('Name one object that would fall down if you dropped it, like a ball or a book.', ['ball', 'book', 'toy'])],
  [('What do we call the invisible force that pulls objects down?', ['Gravity', 'Sound', 'Light', 'Wind'], 0),
   ('If you drop a toy, what happens because of gravity?', ['It falls down to the ground', 'It floats up into the sky', 'It disappears completely', 'It turns into a different toy'], 0),
   ('Which of these would gravity pull down if dropped?', ['A ball', 'A cloud', 'Sunlight', 'A shadow'], 0),
   ('Why do objects on Earth usually stay on the ground instead of floating away?', ['Gravity pulls them down', 'Gravity pushes them up', 'There is no gravity on Earth', 'Objects choose to stay down'], 0),
   ('Gravity is best described as a force that pulls objects ___.', ['Down toward the ground', 'Up into the sky', 'Sideways only', 'Nowhere at all'], 0)])

d94_ss = sub('SocialStudies', 'Laws and Rules: Why Communities Need Them',
  'Students learn that communities create laws and rules, bigger than classroom rules, to help keep everyone safe and to help people treat each other fairly.',
  [('What do we call the rules a whole community or country follows?', ['laws']),
   ('Name one reason communities have laws, like keeping people safe.', ['keeping people safe', 'fairness']),
   ('Should everyone in a community follow the same laws?', ['yes'])],
  [('What do we call the rules that a whole community or country follows?', ['Laws', 'Songs', 'Stories', 'Colours'], 0),
   ('Why do communities create laws?', ['To help keep everyone safe and treated fairly', 'To make life more confusing', 'Laws have no real purpose', 'To stop people from having fun'], 0),
   ('Which of these is an example of a law that keeps people safe?', ['Stopping at a red traffic light', 'Ignoring traffic signals', 'Running across a busy street', 'Littering in the park'], 0),
   ('Who is expected to follow the laws in a community?', ['Everyone in the community', 'Only children', 'Only adults', 'No one has to follow laws'], 0),
   ('Laws help a community stay ___.', ['Safe and fair for everyone', 'Confusing and unsafe', 'Unfair to some people', 'Impossible to live in'], 0)])

# ─── DAY 95 ─────────────────────────────────────────────────────────────────
d95_lang = sub('Language', 'Punctuation: Capital Letters at the Start of a Sentence',
  'Students learn that every written sentence begins with a capital letter, which signals to a reader that a new sentence is starting.',
  [('Should the first word of a sentence start with a capital letter or a lowercase letter?', ['capital letter']),
   ('Which of these correctly starts a sentence: the dog runs, or The dog runs?', ['The dog runs']),
   ('What does a capital letter at the start of a sentence tell a reader?', ['a new sentence is starting', 'new sentence'])],
  [('What kind of letter should begin every written sentence?', ['A capital letter', 'A lowercase letter', 'A number', 'A picture'], 0),
   ('Which of these correctly starts a sentence?', ['The sun is bright.', 'the sun is bright.', 'THE sun is bright', 'sun is bright the'], 0),
   ('Why do sentences begin with a capital letter?', ['It signals to the reader that a new sentence is starting', 'It has no purpose at all', 'It makes words harder to read', 'It is only used at the end of a sentence'], 0),
   ('Which of these sentences correctly begins with a capital letter?', ['Birds can fly.', 'birds can fly.', 'BIRDS can fly', 'birds Can Fly'], 0),
   ('A capital letter at the beginning of a sentence is a print concept that helps readers know ___.', ['Where a new sentence begins', 'Where a sentence ends', 'What colour to use', 'How loud to read'], 0)])

d95_math = sub('Math', 'Covering Space: Filling a Shape with Tiles',
  'Students explore early measurement of area by covering a flat shape, like a rectangle, with small tiles or squares and counting how many tiles it takes to fill the space completely.',
  [('What do we call small shapes, like squares, used to fill up a flat space?', ['tiles']),
   ('If it takes 6 small tiles to fill a shape completely, how many tiles cover the shape?', ['6', 'six']),
   ('Would a bigger shape usually need more tiles or fewer tiles to fill it completely?', ['more tiles', 'more'])],
  [('What are we doing when we fill a flat shape completely with small tiles?', ['Covering the space', 'Erasing the shape', 'Measuring the weight', 'Measuring the temperature'], 0),
   ('If it takes 8 small tiles to completely cover a rectangle, how many tiles were used?', ['8', '4', '2', '10'], 0),
   ('Would a bigger shape need more tiles or fewer tiles to cover it completely?', ['More tiles', 'Fewer tiles', 'No tiles at all', 'The exact same number always'], 0),
   ('Why might we count how many tiles cover a shape?', ['To measure and compare how much space the shape takes up', 'To measure how loud the shape is', 'To measure the shapes colour', 'Tiles have no connection to measurement'], 0),
   ('Covering a shape with tiles and counting them is an early way to measure ___.', ['Area, or how much space a shape covers', 'Sound', 'Weight', 'Temperature'], 0)])

d95_sci = sub('Science', 'Static Electricity: Making Things Stick',
  'Students explore static electricity by rubbing objects, such as a balloon on hair, to discover how this invisible force can make light objects stick together or attract to each other.',
  [('What invisible force can make a rubbed balloon stick to a wall?', ['static electricity']),
   ('If you rub a balloon on your hair, what might happen to your hair?', ['it sticks up', 'stands up', 'sticks to the balloon']),
   ('Name one object you might rub to create static electricity, like a balloon.', ['balloon', 'a balloon'])],
  [('What invisible force can make a rubbed balloon stick to a wall?', ['Static electricity', 'Gravity', 'Sound', 'Magnetism only'], 0),
   ('What might happen if you rub a balloon on your hair?', ['Your hair might stick up toward the balloon', 'Your hair turns a new colour', 'Your hair disappears', 'Nothing happens at all'], 0),
   ('Which of these could you rub to help create static electricity?', ['A balloon', 'A rock', 'Water', 'A shadow'], 0),
   ('Static electricity is an example of an invisible ___.', ['Force', 'Colour', 'Sound', 'Smell'], 0),
   ('Why does a rubbed balloon sometimes stick to a wall for a little while?', ['Static electricity pulls it toward the wall', 'The balloon becomes glue', 'Gravity pushes it sideways', 'The wall is magnetic'], 0)])

d95_ss = sub('SocialStudies', 'Emergency Vehicles: Sirens and Flashing Lights',
  'Students learn to identify emergency vehicles, such as ambulances, fire trucks, and police cars, and understand that their sirens and flashing lights warn others to make way quickly.',
  [('Name one type of emergency vehicle, like an ambulance or fire truck.', ['ambulance', 'fire truck', 'police car']),
   ('What do emergency vehicles use to warn people to make way, like a loud sound?', ['sirens', 'flashing lights']),
   ('Should cars pull over and make way when they hear an emergency vehicle siren?', ['yes'])],
  [('Which of these is an emergency vehicle?', ['An ambulance', 'A school bus', 'A taxi', 'A delivery truck'], 0),
   ('What do emergency vehicles use to warn others they are coming?', ['Sirens and flashing lights', 'Silence', 'Music', 'Nothing at all'], 0),
   ('What should drivers do when they hear an emergency vehicle siren?', ['Make way and let it pass safely', 'Speed up to race it', 'Ignore the siren completely', 'Stop and block the road'], 0),
   ('Which emergency vehicle helps put out fires?', ['A fire truck', 'An ambulance', 'A police car', 'A school bus'], 0),
   ('Why is it important for emergency vehicles to move quickly through traffic?', ['They may be rushing to help someone in danger', 'They are just driving for fun', 'They never need to hurry', 'Emergency vehicles are not important'], 0)])

# ─── DAY 96 ─────────────────────────────────────────────────────────────────
d96_lang = sub('Language', 'Cause and Effect: Why Things Happen in a Story',
  'Students learn to identify cause and effect in stories, understanding that a cause is why something happens and an effect is what happens as a result.',
  [('If a character forgets an umbrella and gets wet in the rain, what is the cause?', ['forgetting the umbrella']),
   ('If a character forgets an umbrella and gets wet in the rain, what is the effect?', ['getting wet']),
   ('What word describes why something happens in a story?', ['cause'])],
  [('What do we call the reason why something happens in a story?', ['The cause', 'The effect', 'The title', 'The cover'], 0),
   ('What do we call what happens as a result of an event in a story?', ['The effect', 'The cause', 'The author', 'The setting'], 0),
   ('If a character waters a plant and it grows, what is the cause?', ['Watering the plant', 'The plant growing', 'The characters name', 'The title of the story'], 0),
   ('If a character waters a plant and it grows, what is the effect?', ['The plant growing', 'Watering the plant', 'The characters name', 'The title of the story'], 0),
   ('Understanding cause and effect helps readers see how events in a story are ___.', ['Connected to each other', 'Never related at all', 'Always random', 'Impossible to understand'], 0)])

d96_math = sub('Math', 'Ways to Make 5: Number Combinations',
  'Students explore different combinations of two numbers that add together to make 5, such as 1 and 4, or 2 and 3, building an early understanding of number composition.',
  [('What two numbers can you add together to make 5, using 2 and another number?', ['2 and 3', '3']),
   ('What two numbers can you add together to make 5, using 1 and another number?', ['1 and 4', '4']),
   ('Can 5 and 0 also add together to make 5?', ['yes'])],
  [('Which two numbers add together to make 5?', ['2 and 3', '2 and 4', '3 and 3', '1 and 1'], 0),
   ('Which two numbers add together to make 5?', ['1 and 4', '1 and 5', '2 and 2', '4 and 4'], 0),
   ('Does 0 plus 5 also equal 5?', ['Yes', 'No', 'Only sometimes', 'Cannot tell'], 0),
   ('Which pair of numbers does NOT add together to make 5?', ['2 and 4', '1 and 4', '2 and 3', '0 and 5'], 0),
   ('Learning different ways to make 5 helps us understand that a number can be made of ___.', ['Different smaller number combinations', 'Only one possible combination', 'No smaller numbers at all', 'Only itself and zero'], 0)])

d96_sci = sub('Science', 'The Moon: Watching It Change Shape',
  'Students learn that the moon appears to change shape over about a month, moving through phases such as a full circle, a half circle, and a thin crescent.',
  [('What object in the night sky appears to change shape over about a month?', ['the moon', 'moon']),
   ('Name one shape the moon might look like, such as a full circle or a crescent.', ['full circle', 'full moon', 'crescent', 'half circle']),
   ('Does the moon appear to change shape slowly over many days?', ['yes'])],
  [('What object in the night sky appears to change shape over about a month?', ['The moon', 'The sun', 'A star', 'A cloud'], 0),
   ('Which of these is a shape the moon can appear to be?', ['A crescent', 'A square', 'A triangle', 'A rectangle'], 0),
   ('Does the moon change shape quickly in one night, or slowly over many days?', ['Slowly over many days', 'Quickly in one night', 'It never changes', 'It changes every second'], 0),
   ('What do we call the different shapes the moon appears to take, like full or crescent?', ['Phases of the moon', 'Seasons', 'Habitats', 'Life cycles'], 0),
   ('Watching the moon change shape over time is an example of studying ___.', ['Earth and space', 'Living things only', 'Community helpers', 'Story characters'], 0)])

d96_ss = sub('SocialStudies', 'City Life and Country Life: Comparing Communities',
  'Students compare city life and country life, learning that a city has many tall buildings and busy streets, while the country has more open land, farms, and fewer buildings.',
  [('Would you expect to see many tall buildings in a city or in the country?', ['city']),
   ('Would you expect to see wide open farmland in a city or in the country?', ['country']),
   ('Name one difference between city life and country life.', ['more buildings in the city', 'more open land in the country', 'busier streets in the city'])],
  [('Where would you expect to see many tall buildings close together?', ['In a city', 'In the country', 'Only at the beach', 'Only in the mountains'], 0),
   ('Where would you expect to see wide open farmland with fewer buildings?', ['In the country', 'In a city', 'Only underwater', 'Only in space'], 0),
   ('Which of these is more common in the country than in a busy city?', ['Wide open farmland', 'Tall skyscrapers', 'Very busy streets', 'Crowded subways'], 0),
   ('Why might a family choose to live in the country instead of a city?', ['They may enjoy more open space and quiet', 'Country living has no differences from the city', 'Cities have no buildings at all', 'The country has no benefits at all'], 0),
   ('Comparing city life and country life helps us understand that communities can be ___.', ['Different from each other in many ways', 'Exactly the same everywhere', 'Impossible to compare', 'Only found in one place'], 0)])

# ─── DAY 97 ─────────────────────────────────────────────────────────────────
d97_lang = sub('Language', 'Story Mood: How a Story Makes Us Feel',
  'Students learn that a story can have a mood, or overall feeling, such as happy, spooky, or exciting, often created through the words and pictures an author chooses.',
  [('What word describes the overall feeling a story gives us, like happy or spooky?', ['mood']),
   ('If a story has dark pictures and quiet words, might its mood feel spooky or cheerful?', ['spooky']),
   ('Name one mood a story could have, like happy or exciting.', ['happy', 'spooky', 'exciting', 'calm'])],
  [('What do we call the overall feeling a story gives its reader?', ['The mood', 'The title', 'The cover', 'The author'], 0),
   ('If a story uses bright pictures and cheerful words, what mood might it have?', ['A happy mood', 'A spooky mood', 'A sad mood', 'An angry mood'], 0),
   ('If a story uses dark pictures and quiet, mysterious words, what mood might it have?', ['A spooky mood', 'A happy mood', 'A silly mood', 'A calm sunny mood'], 0),
   ('What helps create the mood of a story?', ['The words and pictures an author chooses', 'Only the page numbers', 'Only the title', 'Nothing at all'], 0),
   ('Noticing the mood of a story helps readers understand ___.', ['How the story makes them feel', 'Only the name of the author', 'Only how many pages are in the book', 'Nothing about the story'], 0)])

d97_math = sub('Math', 'Comparing Height: Taller and Shorter',
  'Students compare the height of objects and people, using the words taller and shorter to describe which one measures more or less from bottom to top.',
  [('If one tree is bigger from bottom to top than another tree, is it taller or shorter?', ['taller']),
   ('If you are smaller from bottom to top than a grown-up, are you taller or shorter than them?', ['shorter']),
   ('Name one word we use to compare how tall two things are, like taller or shorter.', ['taller', 'shorter'])],
  [('If one building measures more from bottom to top than another, it is ___.', ['Taller', 'Shorter', 'Wider', 'Heavier'], 0),
   ('If a plant measures less from bottom to top than a tree, the plant is ___.', ['Shorter', 'Taller', 'Wider', 'Heavier'], 0),
   ('Which of these words compares how tall two things are?', ['Taller', 'Louder', 'Colder', 'Sweeter'], 0),
   ('If a giraffe is taller than a dog, what does that tell us?', ['The giraffe measures more from bottom to top', 'The giraffe is quieter', 'The dog is louder', 'The giraffe weighs less'], 0),
   ('Comparing height means comparing how ___ two things are.', ['Tall', 'Loud', 'Salty', 'Colourful'], 0)])

d97_sci = sub('Science', 'Germs: Staying Healthy and Washing Our Hands',
  'Students learn that germs are tiny living things too small to see that can make us sick, and that washing our hands with soap and water helps remove germs and keep us healthy.',
  [('What tiny living things, too small to see, can sometimes make us sick?', ['germs']),
   ('Name one way to help remove germs from our hands, like washing with soap.', ['washing hands', 'soap and water']),
   ('Can washing our hands help us stay healthy?', ['yes'])],
  [('What are germs?', ['Tiny living things too small to see that can make us sick', 'Large visible bugs', 'Colourful rocks', 'Types of clouds'], 0),
   ('What can help remove germs from our hands?', ['Washing with soap and water', 'Ignoring dirty hands', 'Never washing at all', 'Wiping hands on clothing only'], 0),
   ('Why is it important to wash our hands before eating?', ['It helps remove germs and keep us healthy', 'Washing hands has no benefit', 'Germs are never found on hands', 'Washing hands makes us sick'], 0),
   ('Which of these is a good time to wash our hands?', ['After using the washroom', 'Only once a year', 'Never at all', 'Only when hands look shiny'], 0),
   ('Washing our hands with soap and water helps us ___.', ['Stay healthy by removing germs', 'Grow taller', 'Change colour', 'Hear better'], 0)])

d97_ss = sub('SocialStudies', 'Ottawa: The Capital City of Canada',
  'Students learn that Ottawa is the capital city of Canada, the special city where important decisions for the whole country are made.',
  [('What is the capital city of Canada?', ['Ottawa']),
   ('Is Ottawa a small village or a capital city?', ['capital city']),
   ('Do important decisions for the whole country get made in the capital city?', ['yes'])],
  [('What is the capital city of Canada?', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 0),
   ('What is special about a capital city like Ottawa?', ['Important decisions for the whole country are made there', 'It is the smallest town in the country', 'No one lives there', 'It has no buildings at all'], 0),
   ('Ottawa is the capital city of which country?', ['Canada', 'The United States', 'France', 'Mexico'], 0),
   ('Which of these best describes Ottawa?', ['The capital city of Canada', 'A tiny island', 'A mountain range', 'A type of animal'], 0),
   ('Learning about a capital city like Ottawa helps us understand more about our ___.', ['Country', 'Weather', 'Favourite foods', 'Favourite games'], 0)])

# ─── DAY 98 ─────────────────────────────────────────────────────────────────
d98_lang = sub('Language', 'Environmental Print: Reading Signs and Labels',
  'Students learn to recognize environmental print, the words and symbols found on everyday signs and labels, such as a stop sign or a cereal box, that help us understand our surroundings.',
  [('What do we call the words and symbols on everyday signs, like a stop sign?', ['environmental print']),
   ('Name one place you might see environmental print, like a cereal box or street sign.', ['cereal box', 'street sign', 'stop sign']),
   ('Can reading signs and labels help us understand what is around us?', ['yes'])],
  [('What do we call the words and symbols found on everyday signs and labels?', ['Environmental print', 'Poetry', 'Fiction', 'A story problem'], 0),
   ('Which of these is an example of environmental print?', ['A stop sign', 'A bedtime story', 'A poem', 'A song'], 0),
   ('Why is it helpful to recognize environmental print?', ['It helps us understand our surroundings, like safety signs', 'It has no real use', 'It only appears in books', 'It is only found at school'], 0),
   ('Where might you see environmental print?', ['On a cereal box', 'Only inside a library book', 'Only in a poem', 'Only in a song'], 0),
   ('Environmental print often uses ___ to give people quick information.', ['Words and symbols', 'Only pictures with no words', 'Only numbers', 'Only colours'], 0)])

d98_math = sub('Math', 'Money: Loonies and Toonies (Dollar Coins)',
  'Students learn to identify the loonie, a coin worth one dollar, and the toonie, a coin worth two dollars, two important Canadian coins used for buying things.',
  [('What is the name of the Canadian coin worth one dollar?', ['loonie']),
   ('What is the name of the Canadian coin worth two dollars?', ['toonie']),
   ('Is a toonie worth more than a loonie?', ['yes'])],
  [('What is the name of the Canadian coin worth one dollar?', ['A loonie', 'A toonie', 'A penny', 'A dime'], 0),
   ('What is the name of the Canadian coin worth two dollars?', ['A toonie', 'A loonie', 'A nickel', 'A quarter'], 0),
   ('Which coin is worth more, a loonie or a toonie?', ['A toonie', 'A loonie', 'They are equal', 'Cannot tell'], 0),
   ('If you have 1 loonie and 1 toonie, how many dollars do you have in total?', ['3', '2', '1', '4'], 0),
   ('Loonies and toonies are both examples of Canadian ___.', ['Dollar coins', 'Paper bills', 'Stamps', 'Stickers'], 0)])

d98_sci = sub('Science', 'Fossils: Clues from Long Ago',
  'Students learn that a fossil is the preserved trace or remains of a plant or animal that lived a very long time ago, giving us clues about life on Earth in the past.',
  [('What do we call the preserved trace of a plant or animal that lived long ago?', ['fossil', 'a fossil']),
   ('Can fossils give us clues about animals that lived a very long time ago, like dinosaurs?', ['yes']),
   ('Name one place scientists might search to find fossils, like in rocks.', ['rocks', 'the ground', 'in the earth'])],
  [('What is a fossil?', ['The preserved trace of a plant or animal from long ago', 'A new type of rock candy', 'A living animal today', 'A type of cloud'], 0),
   ('What can fossils teach scientists?', ['Clues about life on Earth in the past', 'Todays weather forecast', 'How to bake bread', 'Todays traffic patterns'], 0),
   ('Which animal is commonly known from fossils found in rocks?', ['A dinosaur', 'A modern house cat', 'A pet goldfish', 'A classroom hamster'], 0),
   ('Where might scientists search to find fossils?', ['In rocks and the ground', 'In the clouds', 'In the ocean waves only', 'In a rainbow'], 0),
   ('A fossil is best described as a clue about ___.', ['Life long ago', 'Todays weather', 'Tomorrow only', 'Nothing important'], 0)])

d98_ss = sub('SocialStudies', 'Weather Safety: Being Prepared for Storms',
  'Students learn simple ways to stay safe during storms, such as going indoors when thunder is heard and listening to a trusted adult for instructions.',
  [('If you hear thunder outside, should you go indoors or stay outside?', ['go indoors', 'indoors']),
   ('Who should you listen to for instructions to stay safe during a storm?', ['trusted adult', 'an adult']),
   ('Name one way to stay safe during a storm, like going indoors.', ['going indoors', 'staying inside', 'listening to an adult'])],
  [('What should you do if you hear thunder while playing outside?', ['Go indoors right away', 'Keep playing outside', 'Stand under a tall tree', 'Ignore the thunder completely'], 0),
   ('Who should you listen to for instructions during a storm?', ['A trusted adult', 'A stranger', 'No one at all', 'Another child'], 0),
   ('Why is it important to go indoors during a thunderstorm?', ['To stay safe from lightning and heavy rain', 'Storms are never dangerous', 'Staying outside is always safer', 'Storms have no effect on safety'], 0),
   ('Which of these shows good weather safety?', ['Going inside when a storm starts', 'Standing outside during lightning', 'Ignoring storm warnings', 'Playing in flooded streets'], 0),
   ('Being prepared for storms helps keep our community ___.', ['Safe', 'In danger', 'Confused', 'Unprepared'], 0)])

# ─── DAY 99 ─────────────────────────────────────────────────────────────────
d99_lang = sub('Language', 'Sentence Building: Putting Words in Order',
  'Students practise sentence building, learning that words must be arranged in a sensible order for a sentence to make sense and be understood by a reader.',
  [('Put these words in order to make a sentence: dog, the, runs.', ['The dog runs', 'the dog runs']),
   ('Does word order matter for a sentence to make sense?', ['yes']),
   ('Name one word that could start a simple sentence about a cat, like The.', ['The', 'the'])],
  [('Why does word order matter in a sentence?', ['It helps the sentence make sense to a reader', 'Word order never matters', 'Sentences do not need any order', 'Only the last word matters'], 0),
   ('Which of these word groups is in the correct order to make sense?', ['The cat sleeps', 'Sleeps cat the', 'Cat the sleeps', 'The sleeps cat'], 0),
   ('Which of these word groups is NOT in a sensible order?', ['Runs dog the', 'The dog runs', 'The dog is happy', 'She likes apples'], 0),
   ('Putting words in a sensible order helps a reader ___.', ['Understand what the sentence means', 'Become confused on purpose', 'Ignore the sentence', 'Change the meaning randomly'], 0),
   ('Which sentence is correctly ordered?', ['I like ice cream', 'Ice I cream like', 'Cream ice like I', 'Like I cream ice'], 0)])

d99_math = sub('Math', '2D Shapes: Triangle and Rectangle',
  'Students explore two flat shapes, the triangle, with three straight sides, and the rectangle, with four straight sides and four corners, describing their attributes.',
  [('How many straight sides does a triangle have?', ['3', 'three']),
   ('How many straight sides does a rectangle have?', ['4', 'four']),
   ('Does a rectangle have four corners?', ['yes'])],
  [('How many straight sides does a triangle have?', ['3', '4', '2', '5'], 0),
   ('How many straight sides does a rectangle have?', ['4', '3', '2', '5'], 0),
   ('How many corners does a rectangle have?', ['4', '3', '2', '5'], 0),
   ('Which of these shapes has exactly three sides?', ['A triangle', 'A rectangle', 'A circle', 'A square only'], 0),
   ('A rectangle is best described as a shape with four sides and ___.', ['Four corners', 'No corners', 'One corner', 'Three corners'], 0)])

d99_sci = sub('Science', 'Erosion: How Wind and Water Change the Land',
  'Students learn that erosion happens when wind or water slowly wears away and moves bits of soil or rock, gradually changing the shape of the land over time.',
  [('What do we call it when wind or water slowly wears away soil or rock?', ['erosion']),
   ('Name one thing that can cause erosion, like wind or water.', ['wind', 'water']),
   ('Does erosion happen quickly in one second, or slowly over time?', ['slowly over time'])],
  [('What do we call it when wind or water slowly wears away soil or rock?', ['Erosion', 'Migration', 'Germination', 'Camouflage'], 0),
   ('Which of these can cause erosion?', ['Flowing water', 'A quiet room', 'A sleeping cat', 'A book'], 0),
   ('Does erosion usually happen quickly or slowly?', ['Slowly, over a long time', 'Instantly, in one second', 'It never happens', 'Only during winter'], 0),
   ('What can happen to land over a long time because of erosion?', ['Its shape can slowly change', 'It always stays exactly the same', 'It disappears in one second', 'It turns into water'], 0),
   ('Erosion is caused by natural forces such as wind and ___.', ['Water', 'Sound', 'Colour', 'Light'], 0)])

d99_ss = sub('SocialStudies', 'Being a Global Citizen: Caring About the Whole World',
  'Students learn that being a global citizen means caring not only about our own community but also about people, animals, and places all around the whole world.',
  [('What do we call someone who cares about people and places all around the world?', ['global citizen']),
   ('Name one way to show care for the whole world, like helping the environment.', ['helping the environment', 'being kind to others', 'recycling']),
   ('Do global citizens care about places beyond just their own community?', ['yes'])],
  [('What does it mean to be a global citizen?', ['To care about people and places all around the world', 'To only care about your own street', 'To ignore other countries', 'To never help anyone'], 0),
   ('Which of these shows being a good global citizen?', ['Caring for the environment we all share', 'Littering on purpose', 'Ignoring people in other countries', 'Wasting resources carelessly'], 0),
   ('Why might it be important to care about the whole world, not just our own community?', ['Our actions can affect people and places everywhere', 'Other places have no connection to us', 'Caring about the world is not important', 'Only our own street matters'], 0),
   ('Which of these is an example of global citizenship?', ['Learning about and respecting other cultures', 'Refusing to learn about other places', 'Being unkind to people who are different', 'Ignoring problems in other countries'], 0),
   ('Being a global citizen means thinking about how our choices affect ___.', ['People and places everywhere', 'Only ourselves', 'Nothing at all', 'Only our closest friends'], 0)])

# ─── DAY 100 (Review) ───────────────────────────────────────────────────────
d100_lang = sub('Language', 'Language Review: Word Families, Punctuation, and Comprehension',
  'Students review recent Language skills: the -ot and -et word families, adding -es, comparing and contrasting, capital letters, cause and effect, story mood, environmental print, and sentence building.',
  [('Change the h in hot to p. What new word do you make?', ['pot']),
   ('Add -es to the word box. What new word do you make?', ['boxes']),
   ('What kind of letter should begin every written sentence?', ['capital letter'])],
  [('Which word rhymes with hot?', ['Pot', 'Dog', 'Sun', 'Cup'], 0),
   ('Add -es to the word wish. What new word do you make?', ['Wishes', 'Wishs', 'Wishies', 'Wish'], 0),
   ('What do we call the reason why something happens in a story?', ['The cause', 'The effect', 'The title', 'The cover'], 0),
   ('What do we call the overall feeling a story gives its reader?', ['The mood', 'The title', 'The cover', 'The author'], 0),
   ('What do we call the words and symbols found on everyday signs and labels?', ['Environmental print', 'Poetry', 'Fiction', 'A story problem'], 0)])

d100_math = sub('Math', 'Math Review: Subitizing, Shapes, and Number Sense',
  'Students review recent Math skills: subitizing, one-to-one correspondence, position words, 3D shapes, covering space with tiles, ways to make 5, comparing height, money, and 2D shapes.',
  [('What do we call knowing how many objects are in a small group without counting?', ['subitizing']),
   ('What do we call the flat sides of a 3D shape?', ['faces']),
   ('Which two numbers add together to make 5, using 2 and another number?', ['2 and 3', '3'])],
  [('What do we call knowing how many objects are in a group without counting one by one?', ['Subitizing', 'Sorting', 'Measuring', 'Erasing'], 0),
   ('How many flat faces does a cube have?', ['6', '2', '4', '8'], 0),
   ('Which two numbers add together to make 5?', ['2 and 3', '2 and 4', '3 and 3', '1 and 1'], 0),
   ('What is the name of the Canadian coin worth one dollar?', ['A loonie', 'A toonie', 'A penny', 'A dime'], 0),
   ('How many straight sides does a triangle have?', ['3', '4', '2', '5'], 0)])

d100_sci = sub('Science', 'Science Review: Habitats, Earth, and Staying Healthy',
  'Students review recent Science topics: the chicken life cycle, pond and mountain habitats, gravity, static electricity, the moon, germs, fossils, and erosion.',
  [('What does a baby chick hatch out of?', ['egg', 'an egg']),
   ('What do we call the invisible force that pulls objects down?', ['gravity']),
   ('What are germs?', ['tiny living things', 'tiny things that make us sick'])],
  [('What does a baby chick hatch out of?', ['An egg', 'A shell of sand', 'A flower', 'A rock'], 0),
   ('What is a pond?', ['A small habitat of still water', 'A huge ocean', 'A dry desert', 'A snowy mountain'], 0),
   ('What do we call the invisible force that pulls objects down?', ['Gravity', 'Sound', 'Light', 'Wind'], 0),
   ('What can help remove germs from our hands?', ['Washing with soap and water', 'Ignoring dirty hands', 'Never washing at all', 'Wiping hands on clothing only'], 0),
   ('What do we call it when wind or water slowly wears away soil or rock?', ['Erosion', 'Migration', 'Germination', 'Camouflage'], 0)])

d100_ss = sub('SocialStudies', 'Social Studies Review: Helpers, Laws, and Our Country',
  'Students review recent Social Studies topics: farmers, construction workers, Remembrance Day, laws and rules, emergency vehicles, city and country life, Ottawa, weather safety, and global citizenship.',
  [('What do we call a person who grows crops and raises animals for food?', ['farmer']),
   ('What red flower do people often wear on Remembrance Day?', ['poppy', 'a poppy']),
   ('What is the capital city of Canada?', ['Ottawa'])],
  [('What do we call a person who grows crops and raises animals for food?', ['A farmer', 'A librarian', 'A dentist', 'A mayor'], 0),
   ('Why do communities create laws?', ['To help keep everyone safe and treated fairly', 'To make life more confusing', 'Laws have no real purpose', 'To stop people from having fun'], 0),
   ('What should drivers do when they hear an emergency vehicle siren?', ['Make way and let it pass safely', 'Speed up to race it', 'Ignore the siren completely', 'Stop and block the road'], 0),
   ('What is the capital city of Canada?', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 0),
   ('What does it mean to be a global citizen?', ['To care about people and places all around the world', 'To only care about your own street', 'To ignore other countries', 'To never help anyone'], 0)])


g0_91_100 = [
    day(91, [d91_lang, d91_math, d91_sci, d91_ss]),
    day(92, [d92_lang, d92_math, d92_sci, d92_ss]),
    day(93, [d93_lang, d93_math, d93_sci, d93_ss]),
    day(94, [d94_lang, d94_math, d94_sci, d94_ss]),
    day(95, [d95_lang, d95_math, d95_sci, d95_ss]),
    day(96, [d96_lang, d96_math, d96_sci, d96_ss]),
    day(97, [d97_lang, d97_math, d97_sci, d97_ss]),
    day(98, [d98_lang, d98_math, d98_sci, d98_ss]),
    day(99, [d99_lang, d99_math, d99_sci, d99_ss]),
    day(100, [d100_lang, d100_math, d100_sci, d100_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_91_100)
    append_worksheet_days(0, g0_91_100)
