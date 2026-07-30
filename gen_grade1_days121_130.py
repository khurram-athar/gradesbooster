#!/usr/bin/env python3
"""Grade 1, Days 121-130 -- tenth batch, extending Grade 1 past Day 120
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days111_120.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by fetch_video_ids.py)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-120 (see
data/grade1.ts / data/grade1.json, which already densely covers phonics,
grammar, number sense, and most elementary science/social-studies
subtopics): metaphors, possessive pronouns, word choice, editing,
procedural writing, glossary/labels, counting syllables, but/or compound
sentences, and retelling nonfiction for Language; arrays, expanded form,
rounding to the nearest ten, comparison subtraction, balance scales,
calendar math, skip counting by 25s, estimating cost, and comparing bar
graphs for Math; our ears, levers and inclined planes, precipitation,
whales and dolphins, animal communication, ocean tides, the rock cycle,
honeybees, and wind turbines for Science; and the crossing guard, the
veterinarian, the school custodian, the school bus driver, Canada's coat
of arms, the Governor General, treaties, Confederation, and the military
for Social Studies -- none of those exact ideas appear in Days 1-120. Day
130 is a review day across all four subjects, matching the end-of-batch
pattern used in every prior 10-day batch. No embedded ASCII double-quote
or straight apostrophe characters are used anywhere in
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


def _rebalance_answer_positions(days, seed=20260730):
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


g1_121_130 = [
day(121, [
L('Metaphors: Describing One Thing as Another',
  'Grade 1 Language strand: a metaphor describes one thing by calling it something else, without using like or as, such as saying the classroom was a zoo.',
  [('Give an example of a metaphor.', ['the classroom was a zoo', 'her smile was sunshine']),
   ('Does a metaphor use the words like or as?', ['no', 'no it does not']),
   ('What does a metaphor do?', ['describes one thing as another', 'compares without like or as'])],
  [('What is a metaphor?', ['A comparison using like or as', 'A comparison that calls one thing another without like or as', 'A type of question', 'A punctuation mark'], 1),
   ('Which sentence is a metaphor?', ['The moon is like a ball.', 'The moon is a silver coin in the sky.', 'The moon is round.', 'Is the moon bright?'], 1),
   ('A metaphor is different from a simile because it does NOT use ___.', ['Nouns', 'Like or as', 'Verbs', 'Capital letters'], 1),
   ('Which of these could be a metaphor for a very fast runner?', ['He is a cheetah.', 'He runs fast.', 'He is tired.', 'He likes running.'], 0),
   ('Writers use metaphors to make their writing ___.', ['More boring', 'More vivid and imaginative', 'Shorter', 'Harder to read'], 1)]),
M('Arrays: Rows and Columns of Objects',
  'Grade 1 Math strand: an array arranges objects in equal rows and columns, helping students see multiplication and addition in an organized way.',
  [('What is an array?', ['objects arranged in rows and columns', 'equal rows and columns of objects']),
   ('If an array has 3 rows of 2, how many objects in all?', ['6', 'six']),
   ('Describe an array with 2 rows of 4.', ['2 rows of 4 objects', '8 objects in 2 rows'])],
  [('What is an array?', ['A random pile of objects', 'Objects arranged in equal rows and columns', 'A single line of objects', 'A type of graph only'], 1),
   ('An array with 3 rows of 4 has how many objects in total?', ['7', '10', '12', '14'], 2),
   ('Which of these describes an array?', ['4 rows of 2 apples', 'A messy pile of apples', 'One apple alone', 'A drawing of an apple'], 0),
   ('Arrays help us understand ___.', ['Colours', 'Equal groups and repeated addition', 'Only subtraction', 'Only shapes'], 1),
   ('An array with 2 rows of 5 equals ___.', ['7', '8', '9', '10'], 3)]),
Sc('Our Ears: How We Hear Sounds',
   'Grade 1 Science strand: our ears are the body part that lets us hear sounds, catching vibrations in the air and sending signals to our brain.',
   [('What body part do we use to hear?', ['ears', 'our ears']),
    ('What do sounds travel through the air as?', ['vibrations', 'sound vibrations']),
    ('Where do our ears send signals about sound?', ['the brain', 'our brain'])],
   [('What body part lets us hear sounds?', ['Eyes', 'Ears', 'Nose', 'Skin'], 1),
    ('Sounds travel through the air as ___.', ['Light', 'Vibrations', 'Water', 'Wind only'], 1),
    ('After catching a sound, our ears send a signal to the ___.', ['Stomach', 'Brain', 'Lungs', 'Skin'], 1),
    ('Which of these is a loud sound?', ['A whisper', 'A thunderclap', 'A ticking clock softly', 'A falling leaf'], 1),
    ('Why are our ears important?', ['They let us hear and understand sounds', 'They help us see', 'They help us taste', 'They help us smell'], 0)]),
SS('Our Crossing Guard: Helping Us Cross the Street Safely',
   'Grade 1 Social Studies strand: a crossing guard helps students cross busy streets safely near schools, using signs and signals to stop traffic.',
   [('What does a crossing guard help us do?', ['cross the street safely', 'cross safely']),
    ('Where do crossing guards often work?', ['near schools', 'busy streets near schools']),
    ('What might a crossing guard use to stop traffic?', ['a sign', 'a stop sign'])],
   [('What is the main job of a crossing guard?', ['Teaching class', 'Helping people cross the street safely', 'Driving a bus', 'Selling snacks'], 1),
    ('Where do crossing guards usually work?', ['Inside classrooms', 'Near busy streets, often by schools', 'On farms', 'In hospitals'], 1),
    ('What tool might a crossing guard use to stop traffic?', ['A stop sign', 'A paintbrush', 'A shovel', 'A camera only'], 0),
    ('Why is a crossing guards job important?', ['It helps keep pedestrians safe from traffic', 'It has no purpose', 'It slows down students for no reason', 'Only cars matter'], 0),
    ('A crossing guard is an example of a ___.', ['Community helper', 'Type of vehicle', 'Kind of animal', 'Type of weather'], 0)]),
]),
day(122, [
L('Possessive Pronouns: My, Your, His, and Her',
  'Grade 1 Language strand: possessive pronouns like my, your, his, and her show who owns something without adding an apostrophe s.',
  [('Give an example of a possessive pronoun.', ['my', 'your', 'his', 'her']),
   ('In the sentence That is her book, which word shows ownership?', ['her', 'her shows ownership']),
   ('What does a possessive pronoun show?', ['who owns something', 'ownership'])],
  [('Which word is a possessive pronoun?', ['Run', 'Her', 'Quickly', 'Happy'], 1),
   ('In the sentence This is my hat, which word shows ownership?', ['This', 'Is', 'My', 'Hat'], 2),
   ('Which sentence uses a possessive pronoun correctly?', ['Is your coat blue?', 'Is you coat blue?', 'Is coat your blue?', 'Blue is coat your?'], 0),
   ('Which possessive pronoun would replace Toms in Toms book?', ['He', 'His', 'Him', 'He is'], 1),
   ('Possessive pronouns tell us ___.', ['Who owns something', 'How fast something moves', 'What colour something is', 'When something happened'], 0)]),
M('Place Value: Writing Numbers in Expanded Form',
  'Grade 1 Math strand: expanded form breaks a number into the value of each digit, such as writing 34 as 30 + 4.',
  [('Write 34 in expanded form.', ['30+4', '30 plus 4']),
   ('Write 52 in expanded form.', ['50+2', '50 plus 2']),
   ('What does expanded form show?', ['the value of each digit', 'tens and ones added together'])],
  [('What is 47 written in expanded form?', ['4+7', '40+7', '470', '40+70'], 1),
   ('What is 65 written in expanded form?', ['6+5', '60+5', '650', '65+0'], 1),
   ('Expanded form shows the value of each ___.', ['Word', 'Digit', 'Colour', 'Shape'], 1),
   ('Which expanded form matches 82?', ['80+2', '8+2', '820', '8+20'], 0),
   ('Writing a number in expanded form helps us understand ___.', ['Place value', 'Colours', 'Time', 'Shapes'], 0)]),
Sc('Simple Machines: Levers and Inclined Planes',
   'Grade 1 Science strand: a lever helps lift heavy things by pushing down on one end, and an inclined plane, or ramp, makes it easier to move things up or down.',
   [('What simple machine helps lift heavy things by pushing on one end?', ['a lever', 'lever']),
    ('What do we call a ramp used to move things up or down easily?', ['an inclined plane', 'a ramp']),
    ('Name something that uses a lever.', ['a seesaw', 'a wheelbarrow'])],
   [('What simple machine helps lift a heavy object by pushing down on one end?', ['A wheel', 'A lever', 'A screw', 'A wedge'], 1),
    ('What is another name for a ramp?', ['A lever', 'An inclined plane', 'A pulley', 'A wheel'], 1),
    ('Which of these uses a lever?', ['A seesaw', 'A doorknob', 'A rope', 'A ball'], 0),
    ('Why do people use ramps instead of steps sometimes?', ['They make moving things up or down easier', 'They make things heavier', 'They are decorative only', 'They stop movement'], 0),
    ('A lever usually has a fixed point called a ___.', ['Pulley', 'Fulcrum', 'Wedge', 'Axle'], 1)]),
SS('Our Veterinarian: Caring for Sick and Injured Animals',
   'Grade 1 Social Studies strand: a veterinarian, or vet, is a community helper who examines, treats, and cares for sick or injured animals.',
   [('What do we call a doctor for animals?', ['a veterinarian', 'a vet']),
    ('What does a vet do?', ['cares for sick or injured animals', 'treats animals']),
    ('Name one animal a vet might help.', ['a dog', 'a cat', 'a bird'])],
   [('What do we call a doctor who cares for animals?', ['A teacher', 'A veterinarian', 'A pilot', 'A librarian'], 1),
    ('What might a veterinarian do for a sick pet?', ['Examine and treat it', 'Ignore it', 'Sell it', 'Paint it'], 0),
    ('Where might you take a sick pet for help?', ['A veterinary clinic', 'A bakery', 'A library', 'An airport'], 0),
    ('Why is a veterinarians job important to a community?', ['It helps keep animals healthy', 'It has no purpose', 'Animals do not need care', 'Only wild animals need help'], 0),
    ('A veterinarian is an example of a ___.', ['Community helper', 'Type of weather', 'Kind of food', 'Type of vehicle'], 0)]),
]),
day(123, [
L('Word Choice: Choosing Strong, Precise Words',
  'Grade 1 Language strand: strong writers choose precise words, such as sprinted instead of ran, to help readers picture exactly what is happening.',
  [('Give a strong word that could replace ran.', ['sprinted', 'dashed']),
   ('Why do writers choose precise words?', ['to help readers picture it clearly', 'stronger images']),
   ('Which word is more precise, big or enormous?', ['enormous', 'enormous is more precise'])],
  [('Which word is a more precise choice than said?', ['Whispered', 'Word', 'Talk', 'Speak'], 0),
   ('Why do writers choose strong, precise words?', ['To help readers picture things clearly', 'To make writing shorter only', 'Word choice does not matter', 'To confuse readers'], 0),
   ('Which sentence uses the most precise word?', ['She walked to the store.', 'She strolled to the store.', 'She went to the store.', 'She did to the store.'], 1),
   ('Which word is more precise than happy?', ['Glad', 'Feeling', 'Thrilled', 'Nice'], 2),
   ('Choosing strong verbs instead of weak ones makes writing ___.', ['More vivid', 'Harder to read', 'Less clear', 'Shorter only'], 0)]),
M('Rounding to the Nearest Ten',
  'Grade 1 Math strand: rounding a number to the nearest ten means finding the closest multiple of ten, such as rounding 23 to 20.',
  [('Round 23 to the nearest ten.', ['20', 'twenty']),
   ('Round 47 to the nearest ten.', ['50', 'fifty']),
   ('Round 15 to the nearest ten.', ['20', 'twenty'])],
  [('What is 23 rounded to the nearest ten?', ['20', '25', '30', '10'], 0),
   ('What is 68 rounded to the nearest ten?', ['60', '65', '70', '80'], 2),
   ('What is 42 rounded to the nearest ten?', ['30', '40', '45', '50'], 1),
   ('Rounding a number means finding the closest ___.', ['Colour', 'Multiple of ten', 'Shape', 'Letter'], 1),
   ('What is 35 rounded to the nearest ten?', ['30', '35', '40', '50'], 2)]),
Sc('Precipitation: Rain, Snow, Sleet, and Hail',
   'Grade 1 Science strand: precipitation is water that falls from clouds, and it can fall as rain, snow, sleet, or hail depending on the temperature.',
   [('What is precipitation?', ['water falling from clouds', 'rain, snow, sleet, or hail']),
    ('Name one type of precipitation.', ['rain', 'snow', 'sleet', 'hail']),
    ('What decides whether precipitation is rain or snow?', ['temperature', 'how cold or warm it is'])],
   [('What is precipitation?', ['Wind blowing across the land', 'Water falling from clouds', 'Sunlight warming the earth', 'A type of rock'], 1),
    ('Which of these is a form of precipitation?', ['Snow', 'Wind', 'Sunshine', 'Fog only'], 0),
    ('What mainly determines whether precipitation falls as rain or snow?', ['The colour of the clouds', 'The temperature of the air', 'The time of day', 'The season name'], 1),
    ('Hail is best described as ___.', ['Balls of ice that fall from storm clouds', 'Warm rain', 'A type of wind', 'A rainbow'], 0),
    ('Sleet is a mix of ___.', ['Rain and ice', 'Sand and water', 'Dust and wind', 'Fire and smoke'], 0)]),
SS('Our School Custodian: Keeping Our School Clean',
   'Grade 1 Social Studies strand: the school custodian is a helper who keeps the school clean, safe, and in good repair for students and staff every day.',
   [('What does a school custodian do?', ['keeps the school clean', 'cleans and maintains the school']),
    ('Why is a clean school important?', ['keeps everyone healthy and safe', 'healthy environment']),
    ('Name one job a custodian might do.', ['cleaning classrooms', 'fixing things'])],
   [('What is the main job of a school custodian?', ['Teaching lessons', 'Keeping the school clean and in good repair', 'Driving students home', 'Selling books'], 1),
    ('Why is it important for a school to have a custodian?', ['A clean, safe school helps everyone learn well', 'It is not important', 'Schools do not need cleaning', 'Only classrooms matter'], 0),
    ('Which is an example of a custodians job?', ['Mopping the floors', 'Grading tests', 'Driving the school bus', 'Cooking lunch'], 0),
    ('A school custodian helps keep the building ___.', ['Messy', 'Clean and safe', 'Locked forever', 'Empty'], 1),
    ('The school custodian is an example of a ___.', ['Community helper', 'Type of animal', 'Kind of weather', 'Type of food'], 0)]),
]),
day(124, [
L('Editing Our Writing: Checking for Mistakes',
  'Grade 1 Language strand: editing means rereading our writing to check for mistakes in spelling, punctuation, and capital letters before sharing it.',
  [('What does editing mean?', ['checking writing for mistakes', 'fixing mistakes']),
   ('Name one thing we check for when editing.', ['spelling', 'punctuation', 'capital letters']),
   ('Why do we edit our writing?', ['to fix mistakes before sharing', 'make it clearer'])],
  [('What does it mean to edit your writing?', ['Throw it away', 'Check it for mistakes and fix them', 'Write it once and never look again', 'Copy someone elses writing'], 1),
   ('Which is something you check for while editing?', ['Spelling', 'Favourite colour', 'Lunch menu', 'Weather'], 0),
   ('Why is editing an important step in writing?', ['It helps make writing clear and correct', 'It makes writing longer', 'It is not important', 'It removes all the words'], 0),
   ('Which sentence needs editing?', ['I like dogs.', 'i like dogs', 'I like dogs?', 'I like dogs!'], 1),
   ('Editing usually happens ___ writing a first draft.', ['Before', 'After', 'Instead of', 'Never'], 1)]),
M('Comparison Subtraction: How Many More?',
  'Grade 1 Math strand: comparison subtraction finds how many more one group has than another, such as comparing 8 apples to 5 oranges.',
  [('If there are 8 apples and 5 oranges, how many more apples are there?', ['3', 'three']),
   ('What operation do we use to find how many more?', ['subtraction', 'subtract']),
   ('If one group has 10 and another has 6, how many more does the first group have?', ['4', 'four'])],
  [('There are 9 dogs and 4 cats. How many more dogs are there than cats?', ['3', '4', '5', '6'], 2),
   ('To find how many more one group has than another, we use ___.', ['Addition', 'Subtraction', 'Multiplication', 'Counting only'], 1),
   ('There are 12 birds and 7 squirrels. How many more birds are there?', ['3', '4', '5', '6'], 2),
   ('If group A has 6 and group B has 6, how many more does group A have?', ['0', '1', '6', '12'], 0),
   ('Comparison subtraction helps us find the ___ between two groups.', ['Sum', 'Difference', 'Product', 'Average'], 1)]),
Sc('Whales and Dolphins: Ocean Mammals',
   'Grade 1 Science strand: whales and dolphins are mammals that live in the ocean, breathe air through blowholes, and give birth to live young.',
   [('Are whales and dolphins mammals or fish?', ['mammals', 'they are mammals']),
    ('How do whales and dolphins breathe?', ['through a blowhole', 'they breathe air']),
    ('Do whales give birth to live young or lay eggs?', ['live young', 'they give birth to live young'])],
   [('Are whales and dolphins classified as mammals or fish?', ['Fish', 'Mammals', 'Reptiles', 'Amphibians'], 1),
    ('How do whales and dolphins breathe air?', ['Through gills', 'Through a blowhole', 'Through their skin', 'They do not breathe'], 1),
    ('Do whales lay eggs or give birth to live young?', ['Lay eggs', 'Give birth to live young', 'Neither', 'Both equally'], 1),
    ('Why are whales and dolphins considered mammals and not fish?', ['They breathe air and give birth to live young', 'They live in water', 'They are large', 'They swim fast'], 0),
    ('Which of these is an ocean mammal?', ['Dolphin', 'Shark', 'Starfish', 'Jellyfish'], 0)]),
SS('Our School Bus Driver: Getting Us to School Safely',
   'Grade 1 Social Studies strand: the school bus driver is a community helper who drives students safely to and from school each day, following traffic rules.',
   [('Who drives the school bus?', ['the bus driver', 'a bus driver']),
    ('What is the bus drivers main job?', ['drive students safely', 'get students to school safely']),
    ('Name one rule for riding the bus safely.', ['stay seated', 'listen to the driver'])],
   [('Who is responsible for driving the school bus?', ['The principal', 'The bus driver', 'A student', 'A parent only'], 1),
    ('What is the main job of a school bus driver?', ['Teach lessons', 'Drive students safely to and from school', 'Cook lunch', 'Clean classrooms'], 1),
    ('Which is a good bus safety rule?', ['Standing up while the bus moves', 'Staying seated and quiet', 'Yelling loudly', 'Sticking arms out the window'], 1),
    ('Why should students follow the bus drivers instructions?', ['To stay safe during the ride', 'It does not matter', 'Drivers give no instructions', 'Only for fun'], 0),
    ('A bus driver helps the school community by ___.', ['Getting students there safely', 'Grading homework', 'Selling snacks', 'Fixing computers'], 0)]),
]),
day(125, [
L('Procedural Writing: Writing Steps in Order',
  'Grade 1 Language strand: procedural writing gives step-by-step directions for how to do something, such as a recipe or instructions for a game.',
  [('What is procedural writing?', ['step by step instructions', 'directions for how to do something']),
   ('Give an example of something written as steps.', ['a recipe', 'instructions for a game']),
   ('Why is order important in procedural writing?', ['steps must be followed in order', 'so it works correctly'])],
  [('What is procedural writing used for?', ['Telling a made-up story', 'Giving step-by-step instructions', 'Describing feelings only', 'Writing a poem'], 1),
   ('Which is an example of procedural writing?', ['A recipe for cookies', 'A fairy tale', 'A diary entry', 'A poem about the moon'], 0),
   ('Why does the order of steps matter in procedural writing?', ['The steps must be followed correctly to work', 'Order never matters', 'Steps can be random', 'Only the first step matters'], 0),
   ('Which words are often used in procedural writing to show order?', ['First, next, then, finally', 'Happy, sad, angry', 'Loud, quiet, soft', 'Red, blue, green'], 0),
   ('Procedural writing helps readers ___.', ['Complete a task correctly', 'Feel an emotion', 'Learn a fictional story', 'Draw a random picture'], 0)]),
M('Balancing Objects: Heavier and Lighter',
  'Grade 1 Math strand: students use a balance scale to compare two objects and determine which one is heavier and which one is lighter.',
  [('What tool can compare which object is heavier?', ['a balance scale', 'a scale']),
   ('If a book makes the scale go down, is it heavier or lighter than the other object?', ['heavier', 'heavier than the other object']),
   ('Name two objects you could compare on a balance scale.', ['a book and a pencil', 'an apple and a feather'])],
  [('What tool helps us compare the weight of two objects?', ['A ruler', 'A balance scale', 'A clock', 'A thermometer'], 1),
   ('On a balance scale, the heavier object goes ___.', ['Up', 'Down', 'Sideways', 'Nowhere'], 1),
   ('If a feather and a rock are compared, which is likely heavier?', ['The feather', 'The rock', 'They weigh the same', 'Neither has weight'], 1),
   ('A balance scale helps us compare which object is ___.', ['Louder', 'Heavier or lighter', 'Taller', 'Older'], 1),
   ('If both sides of a balance scale are level, the objects are ___.', ['Unequal in weight', 'Equal in weight', 'Both very light', 'Both very heavy'], 1)]),
Sc('Animal Communication: How Animals Talk to Each Other',
   'Grade 1 Science strand: animals communicate with each other using sounds, movements, and colours, such as a bees dance or a birds song.',
   [('Name one way animals communicate.', ['sounds', 'movements', 'colours']),
    ('What does a bee do to tell other bees where food is?', ['a dance', 'a waggle dance']),
    ('Why do birds sing?', ['to communicate', 'to send messages to other birds'])],
   [('Which of these is a way animals communicate?', ['Sounds and movements', 'Doing nothing at all', 'Only sleeping', 'Only eating'], 0),
    ('What does a bee do to show other bees where flowers are?', ['A special dance', 'It writes a note', 'It sings a song', 'It draws a map'], 0),
    ('Why might a bird sing loudly?', ['To communicate with other birds', 'It has no reason', 'To scare away the sun', 'To make itself invisible'], 0),
    ('Which animal uses colour to communicate warning signals?', ['A poison dart frog', 'A grey rock', 'A brown stick', 'A clear window'], 0),
    ('Animal communication helps animals ___.', ['Ignore each other', 'Share information with each other', 'Stay confused', 'Avoid all other animals'], 1)]),
SS('Canadas Coat of Arms: A Symbol of Our Country',
   'Grade 1 Social Studies strand: Canadas coat of arms is an official symbol that includes images like lions, a unicorn, and maple leaves, representing our countrys history.',
   [('What is a coat of arms?', ['an official symbol of a country', 'a symbol representing history']),
    ('Name one image found on Canadas coat of arms.', ['a lion', 'a unicorn', 'a maple leaf']),
    ('What does Canadas coat of arms represent?', ['our countrys history', 'Canadas history and values'])],
   [('What is a coat of arms?', ['A type of clothing', 'An official symbol representing a country', 'A kind of food', 'A musical instrument'], 1),
    ('Which image can be found on Canadas coat of arms?', ['A maple leaf', 'A cactus', 'A palm tree', 'A volcano'], 0),
    ('What does Canadas coat of arms represent?', ['Our countrys history and values', 'A single city only', 'Nothing important', 'A foreign country'], 0),
    ('Besides the coat of arms, what other symbols represent Canada?', ['The flag and the national anthem', 'Only the weather', 'Only sports teams', 'Nothing else'], 0),
    ('Official symbols like a coat of arms help people feel a sense of ___.', ['Confusion', 'National pride and identity', 'Boredom', 'Fear'], 1)]),
]),
day(126, [
L('Text Features: Glossary and Labels',
  'Grade 1 Language strand: a glossary explains the meaning of tricky words used in a book, and labels name the parts of a picture or diagram.',
  [('What does a glossary help readers do?', ['understand tricky words', 'find word meanings']),
   ('What do labels do on a picture?', ['name the parts', 'show what things are called']),
   ('Where is a glossary usually found in a book?', ['at the back', 'the back of the book'])],
  [('What is a glossary used for?', ['Showing pictures only', 'Explaining the meaning of tricky words', 'Listing chapter titles', 'Showing the authors name'], 1),
   ('Where would you typically find a glossary?', ['At the front of the book', 'At the back of the book', 'On the cover', 'In the middle of a sentence'], 1),
   ('What do labels on a diagram usually show?', ['The names of the parts', 'The colour of the page', 'The price of the book', 'The authors age'], 0),
   ('Which text feature would help you find the meaning of the word habitat?', ['A glossary', 'A caption', 'A title', 'A heading'], 0),
   ('Labels are especially useful on ___.', ['Diagrams and pictures', 'The back cover only', 'Blank pages', 'The title page'], 0)]),
M('Calendar Math: Counting Days Until an Event',
  'Grade 1 Math strand: students use a calendar to count how many days are left until a special event, such as a birthday or holiday.',
  [('What tool can help you count days until an event?', ['a calendar', 'the calendar']),
   ('If today is the 3rd and your birthday is the 10th, how many days away is it?', ['7', 'seven']),
   ('Name a special event you might count down to.', ['a birthday', 'a holiday'])],
  [('What tool is used to count days until an event?', ['A ruler', 'A calendar', 'A scale', 'A thermometer'], 1),
   ('If today is day 5 and an event is on day 12, how many days away is the event?', ['5', '6', '7', '8'], 2),
   ('If today is day 1 and an event is on day 8, how many days until the event?', ['6', '7', '8', '9'], 1),
   ('A calendar is organized into ___.', ['Weeks and months', 'Only hours', 'Only minutes', 'Colours'], 0),
   ('Counting days until an event uses which math skill?', ['Multiplication', 'Counting or subtraction', 'Measuring length', 'Comparing weight'], 1)]),
Sc('Ocean Tides: The Rise and Fall of the Sea',
   'Grade 1 Science strand: ocean tides are the regular rising and falling of sea water along the shore, happening a few times each day.',
   [('What are ocean tides?', ['the rise and fall of sea water', 'rising and falling water']),
    ('How often do tides usually happen in a day?', ['a few times', 'a couple of times a day']),
    ('Where can we observe tides?', ['at the beach or shore', 'along the coast'])],
   [('What are ocean tides?', ['The regular rising and falling of sea water', 'A type of ocean animal', 'A kind of storm', 'A colour of the ocean'], 0),
    ('About how often do tides usually rise and fall each day?', ['Once a year', 'A few times a day', 'Once a month', 'Never'], 1),
    ('Where would you observe the effects of tides most easily?', ['In the desert', 'Along the coast or shore', 'In a forest', 'On a mountain'], 1),
    ('At low tide, the water level along the shore is ___.', ['Higher than usual', 'Lower than usual', 'Frozen', 'Boiling'], 1),
    ('Tides are an example of how the ocean ___.', ['Never changes', 'Changes in a regular pattern', 'Disappears completely', 'Turns to ice daily'], 1)]),
SS('Canadas Governor General: A Ceremonial Role',
   'Grade 1 Social Studies strand: the Governor General represents the King or Queen in Canada and performs ceremonial duties, such as welcoming important visitors.',
   [('Who does the Governor General represent in Canada?', ['the King or Queen', 'the monarch']),
    ('Name one duty of the Governor General.', ['welcoming visitors', 'ceremonial duties']),
    ('Is the Governor Generals role mostly ceremonial?', ['yes', 'yes it is mostly ceremonial'])],
   [('Who does Canadas Governor General represent?', ['The mayor', 'The King or Queen', 'A foreign president', 'A local business'], 1),
    ('Which of these might be a duty of the Governor General?', ['Welcoming important visitors', 'Driving a school bus', 'Teaching a classroom', 'Selling groceries'], 0),
    ('The role of the Governor General is mostly ___.', ['Ceremonial', 'Related to farming', 'About sports', 'About cooking'], 0),
    ('Is the Governor General the same as the Prime Minister?', ['Yes, exactly the same', 'No, they have different roles', 'They never exist at the same time', 'Canada has neither'], 1),
    ('Learning about the Governor General helps us understand ___.', ['Part of how Canada is organized', 'Nothing useful', 'Only foreign countries', 'A made-up story'], 0)]),
]),
day(127, [
L('Counting Syllables in Longer Words',
  'Grade 1 Language strand: students count syllables in longer words by clapping each beat, such as clapping three times for the word elephant.',
  [('How many syllables are in the word elephant?', ['3', 'three']),
   ('How can we count syllables in a word?', ['clap each beat', 'clap the parts']),
   ('How many syllables are in the word banana?', ['3', 'three'])],
  [('How many syllables does the word elephant have?', ['1', '2', '3', '4'], 2),
   ('What is a good way to count syllables in a word?', ['Clap for each beat you hear', 'Count the letters only', 'Guess randomly', 'Count the vowels written'], 0),
   ('How many syllables does the word cat have?', ['1', '2', '3', '4'], 0),
   ('How many syllables does the word butterfly have?', ['1', '2', '3', '4'], 2),
   ('Counting syllables helps readers understand a words ___.', ['Colour', 'Number of beats or parts', 'Spelling only', 'Meaning only'], 1)]),
M('Skip Counting by 25s: Counting Quarters',
  'Grade 1 Math strand: students skip count by 25s to find the value of quarters, such as 25, 50, 75, and 100 cents for four quarters.',
  [('Skip count by 25s starting from 25 to 100.', ['25,50,75,100', '25 50 75 100']),
   ('What is the value of one quarter?', ['25 cents', '25 cents each']),
   ('What is the value of two quarters together?', ['50 cents', 'fifty cents'])],
  [('What comes next: 25, 50, 75, ___?', ['85', '90', '100', '110'], 2),
   ('What is the value of one quarter?', ['10 cents', '25 cents', '50 cents', '5 cents'], 1),
   ('Three quarters together are worth ___.', ['50 cents', '65 cents', '75 cents', '100 cents'], 2),
   ('Skip counting by 25s helps us count ___ quickly.', ['Pennies', 'Quarters', 'Nickels', 'Dimes'], 1),
   ('Four quarters together equal ___.', ['75 cents', '90 cents', '100 cents', '125 cents'], 2)]),
Sc('The Rock Cycle: How Rocks Slowly Change',
   'Grade 1 Science strand: rocks slowly change over a very long time, breaking down, moving, and sometimes forming new kinds of rock in the rock cycle.',
   [('Do rocks stay exactly the same forever?', ['no', 'no they can change']),
    ('What can cause rocks to slowly break down?', ['wind and water', 'erosion']),
    ('Does rock change happen quickly or slowly?', ['slowly', 'very slowly, over a long time'])],
   [('Do rocks change over time?', ['No, never', 'Yes, very slowly over a long time', 'Yes, instantly', 'Only in winter'], 1),
    ('What can cause rocks to slowly break down?', ['Wind and water', 'Silence', 'Darkness', 'Nothing at all'], 0),
    ('The rock cycle describes how rocks ___.', ['Stay exactly the same forever', 'Slowly change and sometimes form new rocks', 'Disappear completely with no trace', 'Turn into water'], 1),
    ('Rock changes usually happen over ___.', ['A single day', 'A very long time', 'One hour', 'A few minutes'], 1),
    ('Which of these could slowly wear down a rock over time?', ['Flowing water', 'A single raindrop once', 'A shadow', 'A quiet room'], 0)]),
SS('Treaties: Promises Between Canada and Indigenous Peoples',
   'Grade 1 Social Studies strand: treaties are formal agreements made long ago between the government and Indigenous peoples about sharing land and resources.',
   [('What is a treaty?', ['a formal agreement', 'a promise or agreement between groups']),
    ('Who were treaties made between in Canada?', ['the government and Indigenous peoples', 'Canada and Indigenous peoples']),
    ('Why are treaties still important today?', ['they are still honoured and remembered', 'they affect how we share the land'])],
   [('What is a treaty?', ['A type of food', 'A formal agreement between groups', 'A kind of holiday', 'A piece of clothing'], 1),
    ('In Canada, treaties were often made between the government and ___.', ['Indigenous peoples', 'Other countries only', 'Animals', 'No one'], 0),
    ('Why are treaties important to learn about today?', ['They are still honoured and shape relationships today', 'They have no meaning today', 'They were quickly forgotten', 'They are not real'], 0),
    ('Treaties often involved agreements about ___.', ['Sharing land and resources', 'Sports rules', 'School subjects', 'Weather patterns'], 0),
    ('Learning about treaties helps students understand ___.', ['An important part of Canadian history', 'Nothing important', 'Only modern events', 'A fictional story'], 0)]),
]),
day(128, [
L('Compound Sentences: Joining Ideas with But and Or',
  'Grade 1 Language strand: compound sentences can join two ideas using the words but or or, in addition to and, to show contrast or choice.',
  [('Give an example of a compound sentence using but.', ['I like cats but I like dogs more', 'I wanted to play but it rained']),
   ('Give an example of a compound sentence using or.', ['We can walk or we can ride bikes', 'You can have juice or milk']),
   ('What does the word but usually show?', ['contrast', 'a difference'])],
  [('Which word can join two ideas to show contrast?', ['And', 'But', 'The', 'A'], 1),
   ('Which word can join two ideas to show a choice?', ['Or', 'And', 'The', 'Is'], 0),
   ('Which sentence correctly uses but to join two ideas?', ['I wanted to play but it started raining.', 'I wanted to play, it started raining.', 'I wanted to play it started raining.', 'I wanted play but raining.'], 0),
   ('Which sentence uses or to show a choice?', ['You can have apples or oranges.', 'You can have apples and oranges.', 'You can have apples but oranges.', 'You have apples oranges.'], 0),
   ('Compound sentences join two complete ideas using words such as ___.', ['And, but, or', 'The, a, an', 'Run, jump, skip', 'Red, blue, green'], 0)]),
M('Estimating Cost: About How Much Does It Cost?',
  'Grade 1 Math strand: students estimate the total cost of a few items by rounding prices to make a quick, reasonable guess before adding exactly.',
  [('If an apple costs about 1 dollar and a juice costs about 2 dollars, about how much do both cost?', ['about 3 dollars', 'around 3 dollars']),
   ('Why do we estimate cost before adding exactly?', ['to make a quick guess', 'to check if our answer is reasonable']),
   ('Is an estimate the exact answer?', ['no', 'no it is a guess'])],
  [('What does it mean to estimate a cost?', ['Find the exact price to the penny', 'Make a quick, reasonable guess about the total', 'Ignore the prices', 'Guess with no reason at all'], 1),
   ('If two toys each cost about 5 dollars, about how much do both cost together?', ['5 dollars', '10 dollars', '15 dollars', '20 dollars'], 1),
   ('Why is estimating cost a useful skill?', ['It helps us check if we have enough money', 'It replaces exact counting always', 'It is never useful', 'It only works with pennies'], 0),
   ('An estimate is ___ an exact answer.', ['The same as', 'Close to but not exactly', 'Always higher than', 'Always lower than'], 1),
   ('If items cost about 3 dollars and about 4 dollars, a good estimate for the total is about ___.', ['2 dollars', '5 dollars', '7 dollars', '10 dollars'], 2)]),
Sc('Honeybees: Life Inside a Hive',
   'Grade 1 Science strand: honeybees live and work together in a hive, where different bees have different jobs, such as making honey or caring for young bees.',
   [('Where do honeybees live and work together?', ['a hive', 'in a hive']),
    ('Name one job a bee might have in the hive.', ['making honey', 'caring for young bees']),
    ('Do honeybees work alone or together?', ['together', 'they work together'])],
   [('Where do honeybees live and work together?', ['A nest', 'A hive', 'A burrow', 'A web'], 1),
    ('Which of these is a job some bees do in the hive?', ['Making honey', 'Reading books', 'Cooking meals', 'Driving cars'], 0),
    ('Do honeybees work alone or as a group?', ['Alone', 'As a group', 'They do not work', 'Only at night'], 1),
    ('Why is it important for bees to work together in a hive?', ['So the whole colony can survive and thrive', 'It is not important', 'Bees prefer to be alone', 'Hives do not need teamwork'], 0),
    ('What do bees make and store in the hive?', ['Honey', 'Milk', 'Bread', 'Ice'], 0)]),
SS('Confederation: How Canada Became a Country',
   'Grade 1 Social Studies strand: Confederation was when several colonies joined together long ago to form the country of Canada, an event we now celebrate on Canada Day.',
   [('What is Confederation?', ['when colonies joined to form Canada', 'the joining of colonies into Canada']),
    ('What day do we celebrate to remember Confederation?', ['Canada Day', 'July 1st']),
    ('Did Canada always exist as one country?', ['no', 'no it was formed over time'])],
   [('What does the word Confederation describe?', ['A type of animal', 'Colonies joining together to form Canada', 'A single citys history', 'A type of weather'], 1),
    ('What holiday celebrates the anniversary of Confederation?', ['Thanksgiving', 'Canada Day', 'Remembrance Day', 'Victoria Day'], 1),
    ('Before Confederation, Canada was made up of ___.', ['Separate colonies', 'One giant city', 'No people at all', 'Only forests'], 0),
    ('Why is Confederation an important event in Canadian history?', ['It marks the beginning of Canada as a country', 'It has no importance', 'It happened yesterday', 'It only affected one town'], 0),
    ('Learning about Confederation helps us understand ___.', ['How Canada began as a country', 'Nothing about Canada', 'Only recent events', 'A fictional tale'], 0)]),
]),
day(129, [
L('Retelling Nonfiction: Using Key Facts',
  'Grade 1 Language strand: retelling a nonfiction text means sharing the most important facts learned, rather than retelling a story with characters.',
  [('What do we retell when reading nonfiction?', ['the important facts', 'key facts we learned']),
   ('Is nonfiction retelling about characters or facts?', ['facts', 'it is about facts']),
   ('Give an example of a fact you might retell after reading about penguins.', ['penguins cannot fly', 'penguins live in cold places'])],
  [('When retelling nonfiction, what should we focus on?', ['Made-up characters', 'The most important facts learned', 'The illustrations only', 'The books colour'], 1),
   ('Which is an example of retelling nonfiction correctly?', ['Once upon a time there was a penguin.', 'Penguins cannot fly but they can swim well.', 'The penguin felt happy and sad.', 'The end.'], 1),
   ('Nonfiction retelling is different from fiction retelling because nonfiction ___.', ['Has no facts', 'Focuses on true facts, not made-up characters', 'Is always a poem', 'Has no title'], 1),
   ('Why is it useful to retell nonfiction facts?', ['To show we understood and remembered what we learned', 'It has no purpose', 'To make up a new story', 'To ignore the text'], 0),
   ('Which of these would likely appear in a nonfiction retelling about bears?', ['Bears hibernate in winter.', 'The bear lived happily ever after.', 'Once there was a magic bear.', 'The bear wished upon a star.'], 0)]),
M('Data: Comparing Two Bar Graphs',
  'Grade 1 Math strand: students compare two bar graphs to see which one shows a taller bar, meaning a greater amount for that category.',
  [('On a bar graph, what does a taller bar usually mean?', ['a greater amount', 'more of something']),
   ('How can we compare two bar graphs?', ['look at the bar heights', 'compare the heights']),
   ('If one bar graph has a taller bar for apples, what does that tell us?', ['there are more apples', 'apples are more'])],
  [('On a bar graph, a taller bar usually means ___.', ['A smaller amount', 'A greater amount', 'No amount', 'An equal amount'], 1),
   ('When comparing two bar graphs, we look at ___.', ['The colours only', 'The heights of the bars', 'The titles only', 'The paper size'], 1),
   ('If one graph shows 8 apples and another shows 5 apples, which has more?', ['The graph showing 5', 'The graph showing 8', 'They are equal', 'Neither shows more'], 1),
   ('Bar graphs help us ___ different amounts.', ['Ignore', 'Compare', 'Hide', 'Forget'], 1),
   ('Comparing two bar graphs can help us decide which category has the ___.', ['Least or most', 'Best colour', 'Nicest shape', 'Loudest sound'], 0)]),
Sc('Wind Turbines: Catching the Wind for Power',
   'Grade 1 Science strand: a wind turbine has large spinning blades that catch the wind and turn its movement into electricity.',
   [('What does a wind turbine catch to make power?', ['wind', 'moving air']),
    ('What part of a wind turbine spins in the wind?', ['the blades', 'large blades']),
    ('What does a wind turbine turn wind movement into?', ['electricity', 'power'])],
   [('What does a wind turbine capture to make electricity?', ['Sunlight', 'Wind', 'Water', 'Fire'], 1),
    ('What part of a wind turbine spins to catch the wind?', ['The tower', 'The blades', 'The base', 'The wires'], 1),
    ('A wind turbine turns moving air into ___.', ['Sunlight', 'Electricity', 'Water', 'Sound only'], 1),
    ('Wind power is considered a ___ source of energy.', ['Dirty and limited', 'Clean and renewable', 'Fake', 'Dangerous only'], 1),
    ('Which location would likely be good for wind turbines?', ['A windy, open area', 'A sealed underground cave', 'A perfectly still room', 'A closet'], 0)]),
SS('Our Military: Protecting Our Country',
   'Grade 1 Social Studies strand: the Canadian military includes the army, navy, and air force, who work to protect Canada and help during emergencies.',
   [('Name one part of the Canadian military.', ['the army', 'the navy', 'the air force']),
    ('What is one job of the military?', ['protect the country', 'help during emergencies']),
    ('Why do we honour military members on Remembrance Day?', ['to remember their service and sacrifice', 'to thank them for their service'])],
   [('Which of these is part of the Canadian military?', ['The army', 'The library', 'The post office', 'The grocery store'], 0),
    ('What is one job of the Canadian military?', ['Protecting the country', 'Teaching school', 'Selling food', 'Delivering mail'], 0),
    ('Besides protecting the country, the military sometimes helps during ___.', ['Emergencies like floods', 'Birthday parties', 'Grocery shopping', 'School recess'], 0),
    ('On which day do Canadians especially honour military members?', ['Canada Day', 'Remembrance Day', 'Thanksgiving', 'Halloween'], 1),
    ('The Canadian military includes the army, navy, and ___.', ['Air force', 'Fire department', 'Police force', 'Coast guard only'], 0)]),
]),
day(130, [
L('Language Review: Word Choice, Metaphors, and Nonfiction Retelling',
  'Grade 1 Language strand review: students revisit metaphors, possessive pronouns, strong word choice, editing, procedural writing, and retelling nonfiction facts.',
  [('Give an example of a metaphor.', ['the classroom was a zoo', 'her smile was sunshine']),
   ('Give an example of a possessive pronoun.', ['my', 'your', 'his', 'her']),
   ('What does editing mean?', ['checking writing for mistakes', 'fixing mistakes'])],
  [('What is a metaphor?', ['A comparison using like or as', 'A comparison that calls one thing another without like or as', 'A type of question', 'A punctuation mark'], 1),
   ('In the sentence This is my hat, which word shows ownership?', ['This', 'Is', 'My', 'Hat'], 2),
   ('What does it mean to edit your writing?', ['Throw it away', 'Check it for mistakes and fix them', 'Write it once and never look again', 'Copy someone elses writing'], 1),
   ('Which is an example of procedural writing?', ['A recipe for cookies', 'A fairy tale', 'A diary entry', 'A poem about the moon'], 0),
   ('When retelling nonfiction, what should we focus on?', ['Made-up characters', 'The most important facts learned', 'The illustrations only', 'The books colour'], 1)]),
M('Math Review: Arrays, Rounding, and Comparing Data',
  'Grade 1 Math strand review: students revisit arrays, expanded form, rounding to the nearest ten, comparison subtraction, quarters, and comparing bar graphs.',
  [('What is an array?', ['objects arranged in rows and columns', 'equal rows and columns of objects']),
   ('Round 23 to the nearest ten.', ['20', 'twenty']),
   ('What is the value of one quarter?', ['25 cents', '25 cents each'])],
  [('An array with 3 rows of 4 has how many objects in total?', ['7', '10', '12', '14'], 2),
   ('What is 65 written in expanded form?', ['6+5', '60+5', '650', '65+0'], 1),
   ('What is 23 rounded to the nearest ten?', ['20', '25', '30', '10'], 0),
   ('There are 9 dogs and 4 cats. How many more dogs are there than cats?', ['3', '4', '5', '6'], 2),
   ('On a bar graph, a taller bar usually means ___.', ['A smaller amount', 'A greater amount', 'No amount', 'An equal amount'], 1)]),
Sc('Science Review: Senses, Machines, and Earths Water',
   'Grade 1 Science strand review: students revisit our ears, levers and inclined planes, precipitation, whales and dolphins, ocean tides, and wind turbines.',
   [('What body part do we use to hear?', ['ears', 'our ears']),
    ('What is precipitation?', ['water falling from clouds', 'rain, snow, sleet, or hail']),
    ('What does a wind turbine catch to make power?', ['wind', 'moving air'])],
   [('What body part lets us hear sounds?', ['Eyes', 'Ears', 'Nose', 'Skin'], 1),
    ('What is another name for a ramp?', ['A lever', 'An inclined plane', 'A pulley', 'A wheel'], 1),
    ('Which of these is a form of precipitation?', ['Snow', 'Wind', 'Sunshine', 'Fog only'], 0),
    ('Are whales and dolphins classified as mammals or fish?', ['Fish', 'Mammals', 'Reptiles', 'Amphibians'], 1),
    ('What does a wind turbine capture to make electricity?', ['Sunlight', 'Wind', 'Water', 'Fire'], 1)]),
SS('Social Studies Review: Helpers, Symbols, and Our History',
   'Grade 1 Social Studies strand review: students revisit the crossing guard, veterinarian, school custodian, Canadas coat of arms, treaties, Confederation, and the military.',
   [('What does a crossing guard help us do?', ['cross the street safely', 'cross safely']),
    ('What is a treaty?', ['a formal agreement', 'a promise or agreement between groups']),
    ('What is Confederation?', ['when colonies joined to form Canada', 'the joining of colonies into Canada'])],
   [('What is the main job of a crossing guard?', ['Teaching class', 'Helping people cross the street safely', 'Driving a bus', 'Selling snacks'], 1),
    ('What do we call a doctor who cares for animals?', ['A teacher', 'A veterinarian', 'A pilot', 'A librarian'], 1),
    ('Which image can be found on Canadas coat of arms?', ['A maple leaf', 'A cactus', 'A palm tree', 'A volcano'], 0),
    ('What holiday celebrates the anniversary of Confederation?', ['Thanksgiving', 'Canada Day', 'Remembrance Day', 'Victoria Day'], 1),
    ('What is one job of the Canadian military?', ['Protecting the country', 'Teaching school', 'Selling food', 'Delivering mail'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_121_130)
    append_worksheet_days(1, g1_121_130)
