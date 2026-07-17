#!/usr/bin/env python3
"""Grade 2, Days 61-70 -- FOURTH batch extending Grade 2 past Day 60.
This is the LAST Grade 2 batch: after this, Grade 2 has Days 1-70 complete.
Self-contained script modeled exactly on gen_grade2_days51_60.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-60 topics (see data/grade2.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely (or
rewritten without the apostrophe) to keep the generated .ts string
literals valid.
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
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} grade 2 educational')
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


def _rebalance_answer_positions(days, seed=20260831):
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
d61_lang = sub('Language', 'Irregular Past Tense Verbs',
  'Students learn that some verbs do not add -ed to show the past tense but change into a new word instead, such as go becoming went, run becoming ran, and see becoming saw.',
  [('What is the past tense of the verb go?', ['went']),
   ('What is the past tense of the verb run?', ['ran']),
   ('What is the past tense of the verb see?', ['saw'])],
  [('What is the past tense of the verb go?', ['Went', 'Goed', 'Going', 'Goes'], 0),
   ('What is the past tense of the verb run?', ['Ran', 'Runned', 'Running', 'Runs'], 0),
   ('What is the past tense of the verb see?', ['Saw', 'Seed', 'Seeing', 'Sees'], 0),
   ('Which sentence uses the correct irregular past tense of eat?', ['Yesterday I ate breakfast.', 'Yesterday I eated breakfast.', 'Yesterday I eat breakfast.', 'Yesterday I eating breakfast.'], 0),
   ('Irregular past tense verbs are different from regular past tense verbs because they ___.', ['Change into a whole new word instead of adding -ed', 'Always add -ed at the end', 'Never change at all', 'Always add -ing at the end'], 0)])

d61_math = sub('Math', 'Understanding Hundreds: Place Value to 1000',
  'Students learn that three-digit numbers are made up of hundreds, tens, and ones, and practice breaking numbers like 342 into 3 hundreds, 4 tens, and 2 ones.',
  [('How many hundreds are in the number 342?', ['3', 'three']),
   ('How many tens are in the number 342?', ['4', 'four']),
   ('How many ones are in the number 342?', ['2', 'two'])],
  [('How many hundreds are in the number 342?', ['3', '4', '2', '7'], 0),
   ('How many tens are in the number 156?', ['5', '1', '6', '7'], 0),
   ('What is the value of the 7 in the number 273?', ['70', '7', '700', '270'], 0),
   ('Which number has 5 hundreds, 2 tens, and 8 ones?', ['528', '258', '852', '285'], 0),
   ('Place value helps us understand ___.', ['What each digit in a number is worth', 'The colour of a number', 'The sound of a number', 'The shape of a number'], 0)])

d61_sci = sub('Science', 'Life Cycle of a Frog: From Tadpole to Frog',
  'Students learn the life cycle of a frog, which begins as an egg in water, hatches into a swimming tadpole, grows legs, and changes into an adult frog that can live on land and in water.',
  [('What is the first stage of a frog life cycle?', ['egg', 'an egg']),
   ('What do we call a young frog that swims and breathes with gills before it grows legs?', ['a tadpole', 'tadpole']),
   ('Where does a frog lay its eggs?', ['in water', 'water'])],
  [('What is the first stage of a frog life cycle?', ['Egg', 'Tadpole', 'Froglet', 'Adult frog'], 0),
   ('What do we call a young frog that swims using a tail before it grows legs?', ['A tadpole', 'A caterpillar', 'A cub', 'A chick'], 0),
   ('Where does a frog usually lay its eggs?', ['In water', 'In a nest in a tree', 'Underground', 'On a rock in the desert'], 0),
   ('Put the frog life cycle stages in the correct order.', ['Egg, tadpole, froglet, adult frog', 'Adult frog, egg, froglet, tadpole', 'Froglet, egg, tadpole, adult frog', 'Tadpole, adult frog, egg, froglet'], 0),
   ('As a tadpole grows into a frog, it ___.', ['Grows legs and loses its tail', 'Grows wings and flies away', 'Grows a shell and stops moving', 'Turns into a fish permanently'], 0)])

d61_ss = sub('SocialStudies', 'Local Businesses: Meeting Our Community Needs',
  'Students learn that local businesses, such as bakeries, grocery stores, and repair shops, provide goods and services that help meet the needs of people living in a community.',
  [('Name one local business found in many communities, like a bakery or a grocery store.', ['a bakery', 'bakery', 'a grocery store', 'grocery store']),
   ('What do we call the goods and services a business provides to help people?', ['goods and services', 'things people need']),
   ('Why are local businesses important to a community?', ['they provide goods and services', 'they help meet needs', 'they help people get what they need'])],
  [('Which of these is an example of a local business?', ['A bakery', 'A mountain', 'A river', 'A cloud'], 0),
   ('What do local businesses provide to the people in a community?', ['Goods and services people need', 'Only entertainment', 'Only weather reports', 'Only maps'], 0),
   ('Why might a family visit a local grocery store?', ['To buy food and other items they need', 'To watch a movie', 'To play a sport', 'To mail a letter'], 0),
   ('A shoe repair shop is an example of a business that provides a ___.', ['Service', 'Type of food', 'Type of weather', 'Type of animal'], 0),
   ('Local businesses help a community by ___.', ['Providing jobs and things people need nearby', 'Removing all jobs from a community', 'Making it harder to find food', 'Taking away community services'], 0)])

# ─── DAY 62 ─────────────────────────────────────────────────────────────────
d62_lang = sub('Language', 'Sentence Fragments vs Complete Sentences',
  'Students learn that a complete sentence has a subject and a verb and expresses a full thought, while a sentence fragment is missing a part and does not express a complete thought.',
  [('What two parts does a complete sentence need, like a subject and a verb?', ['a subject and a verb', 'subject and verb']),
   ('Is the group of words running fast a complete sentence or a fragment?', ['a fragment', 'fragment']),
   ('Is the sentence the dog ran fast a complete sentence or a fragment?', ['a complete sentence', 'complete sentence'])],
  [('What two parts does a complete sentence need?', ['A subject and a verb', 'Only a noun', 'Only a question mark', 'Only a capital letter'], 0),
   ('Which of these is a complete sentence?', ['The dog ran fast.', 'Running fast.', 'Fast dog the.', 'Ran fast dog'], 0),
   ('Which of these is a sentence fragment?', ['Under the table.', 'The cat slept.', 'She smiled.', 'Birds fly.'], 0),
   ('A sentence fragment is missing ___.', ['A part needed to express a complete thought', 'A period only', 'A capital letter only', 'A title'], 0),
   ('Why is it important to write in complete sentences?', ['So readers can understand a full thought clearly', 'So sentences look longer', 'So readers get confused', 'So writing has no meaning'], 0)])

d62_math = sub('Math', 'Adding Three One-Digit Numbers',
  'Students learn strategies for adding three one-digit numbers together, such as looking for a ten first or adding two numbers before adding the third.',
  [('What is 2 + 3 + 4?', ['9', 'nine']),
   ('What is 5 + 5 + 1?', ['11', 'eleven']),
   ('What is 3 + 3 + 3?', ['9', 'nine'])],
  [('What is 2 + 3 + 4?', ['9', '8', '10', '7'], 0),
   ('What is 5 + 5 + 1?', ['11', '10', '12', '9'], 0),
   ('What is 6 + 2 + 2?', ['10', '9', '11', '8'], 0),
   ('When adding three numbers, a helpful strategy is to ___.', ['Look for two numbers that make a ten first', 'Always add in a random order', 'Only add the first two numbers', 'Ignore the third number'], 0),
   ('What is 4 + 4 + 4?', ['12', '10', '14', '8'], 0)])

d62_sci = sub('Science', 'Fossils: Clues from the Past',
  'Students learn that fossils are the preserved remains or traces of ancient plants and animals found in rock, giving scientists clues about life on earth long ago.',
  [('What word describes the preserved remains or traces of ancient living things found in rock?', ['fossil', 'fossils']),
   ('Name one place fossils are often found, like in rock.', ['in rock', 'rock', 'in the ground']),
   ('What can scientists learn from studying fossils?', ['clues about life long ago', 'about ancient plants and animals', 'about the past'])],
  [('What word describes the preserved remains or traces of ancient living things?', ['A fossil', 'A crystal', 'A magnet', 'A shadow'], 0),
   ('Where are fossils most often found?', ['In layers of rock', 'Floating in the air', 'Inside a cloud', 'In a rainbow'], 0),
   ('What can scientists learn by studying fossils?', ['Clues about plants and animals from long ago', 'How to build a house', 'How to bake bread', 'How to tell time'], 0),
   ('Which of these could become a fossil over a very long time?', ['A dinosaur bone buried in mud', 'A soap bubble', 'A snowflake', 'A cloud'], 0),
   ('Studying fossils helps scientists understand ___.', ['What life on earth was like millions of years ago', 'What the weather will be tomorrow', 'How to count money', 'How to grow a garden'], 0)])

d62_ss = sub('SocialStudies', 'Schools Long Ago and Today',
  'Students compare what schools were like long ago, such as one-room schoolhouses with fewer supplies, to schools today, which often have computers, libraries, and many more resources.',
  [('Name one thing schools have today that schools long ago often did not have, like computers.', ['computers', 'a computer']),
   ('What did many schools look like long ago, with all grades in one place?', ['a one-room schoolhouse', 'one-room schoolhouse', 'one room']),
   ('Name one way schools have changed over time.', ['more technology', 'more resources', 'computers', 'bigger buildings'])],
  [('What did many schools look like long ago, especially in small communities?', ['A one-room schoolhouse with all grades together', 'A large building with computers in every room', 'An underwater classroom', 'A school with no students'], 0),
   ('Which of these is something many schools have today that schools long ago usually did not?', ['Computers', 'Chalkboards', 'Pencils', 'Desks'], 0),
   ('How did students long ago often travel to school compared to some students today?', ['They often walked long distances', 'They always took an airplane', 'They always took a rocket', 'They never went to school'], 0),
   ('Comparing schools long ago and today helps us understand ___.', ['How education has changed over time', 'How to build a computer', 'How to grow food', 'How to play a sport'], 0),
   ('Which of these might have been used for writing in schools long ago instead of paper and pencil?', ['A small chalkboard called a slate', 'A laptop computer', 'A tablet', 'A smartphone'], 0)])

# ─── DAY 63 ─────────────────────────────────────────────────────────────────
d63_lang = sub('Language', 'Using Quotation Marks in Dialogue',
  'Students learn that quotation marks are punctuation marks placed before and after the exact spoken words of a character in a story, helping readers know exactly what was said aloud.',
  [('What do we call the punctuation marks placed before and after the exact words a character speaks?', ['quotation marks']),
   ('What do we call the words that characters speak aloud in a story?', ['dialogue']),
   ('Why do writers use quotation marks in a story?', ['to show exactly what a character said', 'to show spoken words', 'so readers know what was said'])],
  [('What do we call the punctuation marks placed before and after the exact words a character speaks?', ['Quotation marks', 'A period', 'A comma', 'A question mark'], 0),
   ('What do we call the words that characters speak aloud in a story?', ['Dialogue', 'A caption', 'A heading', 'A summary'], 0),
   ('Why do writers use quotation marks around spoken words?', ['To show readers exactly what a character said', 'To make the story shorter', 'To hide what a character said', 'To end the story'], 0),
   ('Quotation marks are placed ___ the exact words a character speaks.', ['Before and after', 'Only before', 'Only after', 'In the middle of'], 0),
   ('Which part of a story would most likely use quotation marks?', ['A conversation between two characters', 'The title of the book', 'The page number', 'The table of contents'], 0)])

d63_math = sub('Math', 'Missing Number Addition and Subtraction Sentences',
  'Students solve equations with a missing number, such as 5 plus a missing number equals 9, by using their knowledge of addition and subtraction facts.',
  [('What number makes this true: 5 + ___ = 9?', ['4', 'four']),
   ('What number makes this true: ___ - 3 = 6?', ['9', 'nine']),
   ('What number makes this true: 10 - ___ = 4?', ['6', 'six'])],
  [('What number makes this true: 5 + ___ = 9?', ['4', '5', '9', '14'], 0),
   ('What number makes this true: ___ minus 3 equals 6?', ['9', '3', '6', '12'], 0),
   ('What number makes this true: 10 minus ___ equals 4?', ['6', '4', '10', '14'], 0),
   ('What number makes this true: 7 + ___ = 12?', ['5', '6', '7', '4'], 0),
   ('To find a missing number in an equation, it helps to ___.', ['Think about the opposite operation or count on', 'Guess without checking', 'Ignore the equal sign', 'Change all the numbers'], 0)])

d63_sci = sub('Science', 'Wheels and Axles: Making Work Easier',
  'Students learn that a wheel and axle is a simple machine made of a wheel attached to a rod called an axle, which turns together to help move objects with less effort.',
  [('What do we call the rod that a wheel turns around?', ['an axle', 'axle']),
   ('Name one object that uses wheels and axles, like a bicycle or a wagon.', ['a bicycle', 'bicycle', 'a wagon', 'wagon', 'a car', 'car']),
   ('Does a wheel and axle make moving objects easier or harder?', ['easier'])],
  [('What do we call the rod that a wheel turns around?', ['An axle', 'A lever', 'A pulley', 'A ramp'], 0),
   ('Which of these objects uses wheels and axles?', ['A bicycle', 'A seesaw', 'A doorstop', 'A magnet'], 0),
   ('A wheel and axle is a type of ___.', ['Simple machine', 'Living thing', 'Weather pattern', 'Food group'], 0),
   ('Using a wheel and axle to move a heavy object makes the task ___.', ['Easier', 'Impossible', 'Slower and harder', 'Dangerous'], 0),
   ('Which part of a wagon turns together as one unit?', ['The wheel and axle', 'The handle only', 'The box only', 'The paint on the wagon'], 0)])

d63_ss = sub('SocialStudies', 'Canadian Currency: The Loonie, Toonie, and Bills',
  'Students learn about Canadian money, including the one dollar coin called the loonie, the two dollar coin called the toonie, and paper bills used to pay for goods and services.',
  [('What is the name of the Canadian one dollar coin?', ['loonie', 'the loonie']),
   ('What is the name of the Canadian two dollar coin?', ['toonie', 'the toonie']),
   ('Name one way Canadian money is used, like paying for goods and services.', ['to pay for goods', 'to buy things', 'paying for goods and services'])],
  [('What is the name of the Canadian one dollar coin?', ['The loonie', 'The toonie', 'The nickel', 'The dime'], 0),
   ('What is the name of the Canadian two dollar coin?', ['The toonie', 'The loonie', 'The penny', 'The quarter'], 0),
   ('Why do people in Canada use money like coins and bills?', ['To pay for goods and services', 'To decorate their homes', 'To feed animals', 'To measure temperature'], 0),
   ('Which of these is Canadian paper money called?', ['A bill', 'A rock', 'A leaf', 'A ticket'], 0),
   ('The picture on the Canadian one dollar coin shows a ___.', ['Loon, a type of bird', 'Bear', 'Moose', 'Beaver'], 0)])

# ─── DAY 64 ─────────────────────────────────────────────────────────────────
d64_lang = sub('Language', 'Point of View: Whose Story Is It',
  'Students learn that point of view tells readers who is telling the story, such as first person, when a character uses words like I and me, or third person, when a narrator uses words like he, she, and they.',
  [('What do we call the perspective from which a story is told?', ['point of view']),
   ('If a character tells the story using the word I, what point of view is that?', ['first person']),
   ('If a narrator tells the story using words like he and she, what point of view is that?', ['third person'])],
  [('What do we call the perspective from which a story is told?', ['Point of view', 'A caption', 'A heading', 'A theme'], 0),
   ('If a character tells the story using the word I, what point of view is being used?', ['First person', 'Third person', 'Second person', 'No point of view'], 0),
   ('If a narrator tells the story using words like he and she, what point of view is being used?', ['Third person', 'First person', 'Second person', 'No point of view'], 0),
   ('Which sentence is told from a first person point of view?', ['I walked to the park with my dog.', 'She walked to the park with her dog.', 'He walked to the park with his dog.', 'They walked to the park with their dog.'], 0),
   ('Knowing the point of view of a story helps readers understand ___.', ['Whose thoughts and feelings are being shared', 'The page number of the story', 'The title of the book', 'The font used in the book'], 0)])

d64_math = sub('Math', 'Arrays: Rows and Columns',
  'Students learn that an array is a way of arranging objects into equal rows and columns, which helps show multiplication as repeated groups.',
  [('What do we call objects arranged into equal rows and columns?', ['an array', 'array']),
   ('If an array has 3 rows with 4 objects in each row, how many objects are there in total?', ['12', 'twelve']),
   ('Do all rows in an array have the same number of objects?', ['yes'])],
  [('What do we call objects arranged into equal rows and columns?', ['An array', 'A fraction', 'A pattern', 'A graph'], 0),
   ('If an array has 3 rows with 4 objects in each row, how many objects are there in total?', ['12', '7', '10', '9'], 0),
   ('If an array has 2 rows with 5 objects in each row, how many objects are there in total?', ['10', '7', '12', '5'], 0),
   ('In an array, each row must have ___.', ['The same number of objects as every other row', 'A different number of objects', 'Only one object', 'No objects at all'], 0),
   ('Arrays help us understand multiplication because they show ___.', ['Equal groups arranged in rows and columns', 'Only subtraction', 'Only measurement', 'Only time'], 0)])

d64_sci = sub('Science', 'Decomposers: Breaking Down Dead Plants and Animals',
  'Students learn that decomposers, such as worms, mushrooms, and some bacteria, break down dead plants and animals, returning nutrients to the soil.',
  [('What do we call living things that break down dead plants and animals?', ['decomposers', 'decomposer']),
   ('Name one example of a decomposer, like a worm or a mushroom.', ['a worm', 'worm', 'a mushroom', 'mushroom']),
   ('What do decomposers return to the soil after breaking down dead material?', ['nutrients'])],
  [('What do we call living things that break down dead plants and animals?', ['Decomposers', 'Predators', 'Producers', 'Pollinators'], 0),
   ('Which of these is an example of a decomposer?', ['A worm', 'A rose', 'A rock', 'A cloud'], 0),
   ('What do decomposers return to the soil after breaking down dead material?', ['Nutrients', 'Water only', 'Sand', 'Plastic'], 0),
   ('Why are decomposers important to nature?', ['They recycle nutrients so new plants can grow', 'They stop all plants from growing', 'They make soil disappear', 'They create pollution'], 0),
   ('Which of these is a job that mushrooms can do in nature?', ['Help break down dead material', 'Fly through the air', 'Swim in the ocean', 'Make electricity'], 0)])

d64_ss = sub('SocialStudies', 'Canadian National Parks: Protecting Wild Spaces',
  'Students learn that Canada has national parks, protected areas of land set aside to preserve nature, wildlife, and beautiful landscapes for everyone to enjoy.',
  [('What do we call an area of land protected to preserve nature and wildlife?', ['a national park', 'national park']),
   ('Name one reason national parks are important, like protecting wildlife.', ['to protect wildlife', 'protecting nature', 'protecting wildlife and nature']),
   ('Name one activity people might do in a national park, like hiking.', ['hiking', 'camping', 'exploring nature'])],
  [('What do we call an area of land protected to preserve nature and wildlife?', ['A national park', 'A shopping mall', 'A parking lot', 'A factory'], 0),
   ('Why are national parks important to Canada?', ['They protect nature, wildlife, and beautiful landscapes', 'They remove all trees', 'They stop animals from living freely', 'They are used only for building houses'], 0),
   ('Which activity might a family enjoy in a national park?', ['Hiking and camping', 'Shopping for clothes', 'Watching a movie indoors', 'Visiting a bank'], 0),
   ('National parks help protect animals by ___.', ['Preserving their natural habitats', 'Removing their food sources', 'Filling their homes with buildings', 'Taking away their water'], 0),
   ('Which of these is something visitors are usually asked to do in a national park?', ['Respect nature and leave no trace', 'Pick all the flowers', 'Feed wild animals junk food', 'Leave garbage behind'], 0)])

# ─── DAY 65 ─────────────────────────────────────────────────────────────────
d65_lang = sub('Language', 'Opinion Writing: Stating and Supporting an Opinion',
  'Students learn to write an opinion by clearly stating what they think and giving at least one reason that supports their opinion.',
  [('What do we call a sentence that shares what a person thinks or feels?', ['an opinion', 'opinion']),
   ('What should you give after stating your opinion to support it?', ['a reason', 'reason', 'reasons']),
   ('Name one word that often signals an opinion, like think or believe.', ['think', 'believe', 'i think', 'i believe'])],
  [('What do we call a sentence that shares what a person thinks or feels?', ['An opinion', 'A fact', 'A caption', 'A heading'], 0),
   ('What should a writer give after stating an opinion?', ['A reason that supports it', 'A random fact', 'Nothing at all', 'A different opinion'], 0),
   ('Which sentence is an opinion?', ['I think puppies are the best pets.', 'A puppy is a young dog.', 'Puppies have four legs.', 'Puppies are born with their eyes closed.'], 0),
   ('Which word often signals that a sentence is an opinion?', ['Think', 'Is', 'Has', 'Was'], 0),
   ('Good opinion writing includes ___.', ['A clear opinion and a reason to support it', 'Only facts and numbers', 'No opinion at all', 'A list of unrelated ideas'], 0)])

d65_math = sub('Math', 'Reading a Thermometer: Measuring Temperature',
  'Students learn to read a thermometer to measure temperature in degrees Celsius and understand that higher numbers mean warmer temperatures.',
  [('What tool do we use to measure temperature?', ['a thermometer', 'thermometer']),
   ('What unit do we use to measure temperature in Canada?', ['degrees celsius', 'celsius']),
   ('Does a higher number on a thermometer mean warmer or colder?', ['warmer'])],
  [('What tool do we use to measure temperature?', ['A thermometer', 'A ruler', 'A scale', 'A clock'], 0),
   ('What unit is commonly used to measure temperature in Canada?', ['Degrees Celsius', 'Litres', 'Kilograms', 'Metres'], 0),
   ('Does a higher number on a thermometer mean the temperature is warmer or colder?', ['Warmer', 'Colder', 'The same', 'Impossible to tell'], 0),
   ('Which temperature would most likely be recorded on a hot summer day?', ['30 degrees Celsius', 'Minus 20 degrees Celsius', '0 degrees Celsius', '5 degrees Celsius'], 0),
   ('A thermometer helps us know ___.', ['How hot or cold something is', 'How heavy something is', 'How long something is', 'How loud something is'], 0)])

d65_sci = sub('Science', 'Plant Adaptations: Surviving in Different Places',
  'Students learn that plants have special features, called adaptations, that help them survive in different environments, such as thick stems that store water in a desert or wide leaves that capture sunlight in a rainforest.',
  [('What word describes a special feature that helps a plant survive in its environment?', ['an adaptation', 'adaptation']),
   ('Name one plant adaptation that helps a cactus survive in a dry desert.', ['storing water', 'thick stem', 'spines', 'storing water in its stem']),
   ('Why do plants in a rainforest often have wide leaves?', ['to capture sunlight', 'to collect more sunlight', 'to catch sunlight'])],
  [('What word describes a special feature that helps a plant survive in its environment?', ['An adaptation', 'A migration', 'A habitat', 'A fossil'], 0),
   ('Which adaptation helps a cactus survive in a dry desert?', ['A thick stem that stores water', 'Wide leaves that need lots of rain', 'Roots that need constant flooding', 'A stem that never stores water'], 0),
   ('Why might a rainforest plant have very wide leaves?', ['To capture as much sunlight as possible', 'To store extra water like a cactus', 'To stay hidden underground', 'To avoid all sunlight'], 0),
   ('Which of these is an example of a plant adaptation?', ['Sharp spines that protect a cactus from animals', 'A plant that never needs sunlight', 'A plant that never needs water', 'A plant that grows only in space'], 0),
   ('Plant adaptations help a plant ___.', ['Survive better in its specific environment', 'Move around like an animal', 'Change into a different species instantly', 'Stop needing sunlight completely'], 0)])

d65_ss = sub('SocialStudies', 'Time Zones: Why Time Differs Across Canada',
  'Students learn that Canada is so wide that it is divided into different time zones, meaning the time of day can be different in places like British Columbia and Newfoundland at the same moment.',
  [('What do we call the different regions of time across a wide country like Canada?', ['time zones', 'time zone']),
   ('Why does Canada have more than one time zone?', ['because it is so wide', 'because the country is very wide', 'because it stretches across a large distance']),
   ('Can it be a different time of day in two provinces at the same moment?', ['yes'])],
  [('What do we call the different regions of time across a wide country like Canada?', ['Time zones', 'Provinces', 'Territories', 'Continents'], 0),
   ('Why does Canada have more than one time zone?', ['Because the country is very wide from coast to coast', 'Because Canada has no clocks', 'Because every province chooses a random time', 'Because Canada has only one season'], 0),
   ('If it is noon in one time zone, could it be a different time in another Canadian time zone at the same moment?', ['Yes, it could be earlier or later', 'No, it is always the same time everywhere', 'No, time zones do not exist', 'Yes, but only during winter'], 0),
   ('Why is it helpful to know about time zones when calling family in another province?', ['So you know what time it actually is for them', 'So you can change the weather', 'So you can change the date on a calendar', 'So you can skip a day of the week'], 0),
   ('Time zones exist because ___.', ['Different parts of the world see sunrise and sunset at different times', 'All places on earth have the exact same time', 'The sun never moves', 'Clocks are different colours in each province'], 0)])

# ─── DAY 66 ─────────────────────────────────────────────────────────────────
d66_lang = sub('Language', 'Idioms and Expressions',
  'Students learn that an idiom is a group of words with a meaning different from the literal meaning of the individual words, such as it is raining cats and dogs meaning it is raining very hard.',
  [('What do we call a group of words whose meaning is different from what the words literally say?', ['an idiom', 'idiom']),
   ('What does the idiom it is raining cats and dogs mean?', ['it is raining very hard', 'raining hard', 'heavy rain']),
   ('What does the idiom break a leg mean when said to a performer?', ['good luck', 'wishing someone good luck'])],
  [('What do we call a group of words whose meaning is different from what the words literally say?', ['An idiom', 'A fact', 'A caption', 'A heading'], 0),
   ('What does the idiom it is raining cats and dogs mean?', ['It is raining very hard', 'Animals are falling from the sky', 'It is very sunny', 'It is very cold'], 0),
   ('What does the idiom break a leg mean when said to a performer before a show?', ['Good luck', 'Be careful not to fall', 'Stay home today', 'Stop performing'], 0),
   ('What does it mean if someone says an idea costs an arm and a leg?', ['It is very expensive', 'It requires body parts', 'It is very cheap', 'It is impossible to buy'], 0),
   ('Understanding idioms helps readers because ___.', ['The literal words do not always explain the real meaning', 'Idioms always mean exactly what they say', 'Idioms are only used in math', 'Idioms have no meaning at all'], 0)])

d66_math = sub('Math', 'Near Doubles: Doubles Plus One and Doubles Minus One',
  'Students learn to use known doubles facts, like 5 plus 5 equals 10, to quickly solve near doubles, such as 5 plus 6, by thinking of it as double 5 plus one more.',
  [('What is 5 + 5?', ['10', 'ten']),
   ('Using the fact that 5 + 5 = 10, what is 5 + 6?', ['11', 'eleven']),
   ('Using the fact that 4 + 4 = 8, what is 4 + 5?', ['9', 'nine'])],
  [('What is 5 + 5?', ['10', '9', '11', '8'], 0),
   ('Using the fact that 5 + 5 = 10, what is 5 + 6?', ['11', '10', '12', '9'], 0),
   ('Using the fact that 4 + 4 = 8, what is 4 + 5?', ['9', '8', '10', '7'], 0),
   ('Using the fact that 6 + 6 = 12, what is 6 + 7?', ['13', '12', '14', '11'], 0),
   ('Near doubles are a helpful strategy because they let us ___.', ['Use a known double fact to solve a close addition problem quickly', 'Ignore addition facts completely', 'Only work with even numbers', 'Always subtract instead of add'], 0)])

d66_sci = sub('Science', 'Planets in Our Solar System',
  'Students learn that the solar system includes the sun and the planets that orbit it, such as Mercury, Venus, Earth, and Mars, each with its own size and distance from the sun.',
  [('What do we call the group of planets that orbit the sun?', ['the solar system', 'solar system']),
   ('Which planet do people live on?', ['earth']),
   ('Name one planet in our solar system besides earth, like Mars or Venus.', ['mars', 'venus', 'mercury', 'jupiter', 'saturn', 'uranus', 'neptune'])],
  [('What do we call the group of planets that orbit the sun?', ['The solar system', 'The water cycle', 'The food chain', 'The rock cycle'], 0),
   ('Which planet do people live on?', ['Earth', 'Mars', 'Venus', 'Jupiter'], 0),
   ('Which of these is a planet in our solar system?', ['Mars', 'The moon', 'A comet', 'A star'], 0),
   ('What do all the planets in our solar system orbit?', ['The sun', 'The moon', 'Earth', 'A comet'], 0),
   ('Which planet is often called the red planet?', ['Mars', 'Venus', 'Mercury', 'Earth'], 0)])

d66_ss = sub('SocialStudies', 'Food From Around the World: Exploring Cultures Through Food',
  'Students learn that families from different cultures often enjoy special foods and recipes that have been passed down for generations, helping to share and celebrate their culture.',
  [('Name one reason families might cook a special recipe passed down in their family.', ['to celebrate their culture', 'to share their culture', 'tradition']),
   ('What do we call food traditions passed down from one generation to the next?', ['a tradition', 'tradition', 'family tradition']),
   ('Why is it fun to try foods from different cultures?', ['to learn about other cultures', 'to experience different cultures', 'to learn about the world'])],
  [('Why might a family cook a special recipe that has been passed down for generations?', ['To celebrate and share their culture', 'To avoid eating anything at all', 'To copy a recipe from a stranger', 'To follow a rule with no meaning'], 0),
   ('What can trying foods from different cultures teach us?', ['About the traditions and history of different cultures', 'Nothing about other cultures', 'Only about one culture', 'Only about cooking tools'], 0),
   ('Which of these is an example of a food tradition?', ['A family recipe passed down through generations', 'A brand new food invented yesterday', 'A food nobody has ever eaten', 'A food with no ingredients'], 0),
   ('Learning about food from around the world helps students understand ___.', ['That different cultures have unique and special traditions', 'That all cultures eat the same food', 'That food has no connection to culture', 'That recipes never change'], 0),
   ('Sharing food from different cultures at a school event can help classmates ___.', ['Learn about and appreciate different cultures', 'Ignore other cultures', 'Avoid trying new things', 'Stop celebrating traditions'], 0)])

# ─── DAY 67 ─────────────────────────────────────────────────────────────────
d67_lang = sub('Language', 'Alliteration: Repeating Beginning Sounds',
  'Students learn that alliteration happens when two or more words close together begin with the same sound, such as silly snakes slither slowly, adding rhythm to writing.',
  [('What do we call it when two or more words close together begin with the same sound?', ['alliteration']),
   ('Which two words show alliteration: happy hippo or happy elephant?', ['happy hippo']),
   ('In the phrase silly snakes slither slowly, which sound repeats at the beginning of each word?', ['s', 'the s sound', 'silly s sound'])],
  [('What do we call it when two or more words close together begin with the same sound?', ['Alliteration', 'Onomatopoeia', 'Rhyme', 'Synonym'], 0),
   ('Which phrase is an example of alliteration?', ['Silly snakes slither slowly', 'The dog ran fast', 'I like pizza', 'She is happy'], 0),
   ('In the phrase silly snakes slither slowly, which sound repeats at the beginning of each word?', ['The s sound', 'The t sound', 'The l sound', 'The a sound'], 0),
   ('Which pair of words shows alliteration?', ['Big blue balloon', 'Big red balloon', 'Small blue balloon', 'Big blue kite'], 0),
   ('Writers use alliteration to ___.', ['Add rhythm and a fun sound to their writing', 'Remove all sounds from writing', 'Make writing harder to read', 'Make writing shorter'], 0)])

d67_math = sub('Math', 'Input and Output Number Patterns',
  'Students learn to find a rule that changes an input number into an output number, such as add 2, and use that rule to complete a number pattern.',
  [('If the rule is add 2 and the input is 3, what is the output?', ['5', 'five']),
   ('If the rule is add 3 and the input is 4, what is the output?', ['7', 'seven']),
   ('If an input of 5 gives an output of 8, what is the rule?', ['add 3', 'plus 3'])],
  [('If the rule is add 2 and the input is 3, what is the output?', ['5', '4', '6', '3'], 0),
   ('If the rule is add 3 and the input is 4, what is the output?', ['7', '6', '8', '5'], 0),
   ('If an input of 5 gives an output of 8, what is the rule?', ['Add 3', 'Add 2', 'Subtract 3', 'Add 5'], 0),
   ('If the rule is subtract 2 and the input is 9, what is the output?', ['7', '11', '9', '5'], 0),
   ('An input and output number pattern always follows ___.', ['The same rule for every number in the pattern', 'A different rule each time', 'No rule at all', 'Only subtraction'], 0)])

d67_sci = sub('Science', 'How We Breathe: The Lungs and Respiratory System',
  'Students learn that the lungs are organs inside the chest that help the body breathe in oxygen from the air and breathe out carbon dioxide.',
  [('What organs help us breathe air in and out?', ['lungs', 'the lungs']),
   ('What gas do we breathe in that our body needs?', ['oxygen']),
   ('What gas do we breathe out?', ['carbon dioxide'])],
  [('What organs help us breathe air in and out?', ['The lungs', 'The stomach', 'The bones', 'The skin'], 0),
   ('What gas does our body need that we breathe in from the air?', ['Oxygen', 'Carbon dioxide', 'Nitrogen only', 'Smoke'], 0),
   ('What gas do we breathe out of our lungs?', ['Carbon dioxide', 'Oxygen', 'Water only', 'Helium'], 0),
   ('Where are the lungs located in the body?', ['Inside the chest', 'Inside the leg', 'Inside the arm', 'Inside the foot'], 0),
   ('Why is breathing important for our body?', ['It brings oxygen that our body needs to work', 'It has no purpose', 'It only makes noise', 'It stops our heart from beating'], 0)])

d67_ss = sub('SocialStudies', 'Postal Codes and Addresses: Finding Your Way',
  'Students learn that an address, including a postal code, helps identify exactly where a person lives so that mail and packages can be delivered to the right place.',
  [('What do we call the group of letters and numbers that helps identify a specific area for mail delivery?', ['a postal code', 'postal code']),
   ('Name one part of an address, like a street name or a house number.', ['a street name', 'street name', 'a house number', 'house number']),
   ('Why is an address important for mail delivery?', ['so mail goes to the right place', 'so packages are delivered correctly', 'to find the right location'])],
  [('What do we call the group of letters and numbers that helps identify a specific area for mail delivery?', ['A postal code', 'A phone number', 'A birthday', 'A time zone'], 0),
   ('Which of these is part of a home address?', ['A street name and house number', 'A favourite colour', 'A shoe size', 'A birthday'], 0),
   ('Why is an address important?', ['It helps mail and packages reach the right place', 'It tells you what time it is', 'It tells you the weather', 'It tells you what to eat'], 0),
   ('Who might use your address to deliver a package?', ['A mail carrier', 'A dentist', 'A teacher', 'A chef'], 0),
   ('A complete address usually includes ___.', ['A house number, street name, city, and postal code', 'Only a first name', 'Only a favourite colour', 'Only a phone number'], 0)])

# ─── DAY 68 ─────────────────────────────────────────────────────────────────
d68_lang = sub('Language', 'Reading Fluency and Expression',
  'Students learn that reading fluently means reading smoothly and at a good pace, while reading with expression means using your voice to show feelings and match punctuation, like excitement for an exclamation mark.',
  [('What do we call reading smoothly and at a good pace?', ['fluency', 'reading fluency', 'fluent reading']),
   ('What should your voice show when you read a sentence that ends with an exclamation mark?', ['excitement', 'strong feeling', 'emotion']),
   ('Why is reading with expression helpful to listeners?', ['it helps the story come alive', 'it makes the story more interesting', 'it helps listeners understand feelings'])],
  [('What do we call reading smoothly and at a good pace?', ['Fluency', 'A caption', 'A theme', 'A summary'], 0),
   ('What should your voice show when reading a sentence that ends with an exclamation mark?', ['Excitement or strong feeling', 'No feeling at all', 'Confusion only', 'Silence'], 0),
   ('Reading with expression means ___.', ['Using your voice to show feelings while reading', 'Reading as fast as possible with no pauses', 'Reading in a whisper the whole time', 'Skipping all punctuation'], 0),
   ('Why is reading fluency important?', ['It helps readers understand and enjoy a story more easily', 'It makes reading impossible', 'It slows readers down on purpose', 'It removes all meaning from a story'], 0),
   ('If a sentence ends with a question mark, how should your voice sound at the end?', ['It should rise, like you are asking something', 'It should stay completely flat', 'It should get very loud', 'It should stop suddenly with no sound'], 0)])

d68_math = sub('Math', 'Line Plots: Organizing Data Points',
  'Students learn to organize data on a line plot, a simple graph that uses marks above a number line to show how many times each value occurs.',
  [('What do we call a graph that uses marks above a number line to show data?', ['a line plot', 'line plot']),
   ('On a line plot, what does each mark usually represent?', ['one item', 'one piece of data', 'one data point']),
   ('If a line plot shows 3 marks above the number 5, how many times did the value 5 occur?', ['3', 'three'])],
  [('What do we call a graph that uses marks above a number line to show data?', ['A line plot', 'A bar graph', 'A pictograph', 'A tally chart'], 0),
   ('On a line plot, what does each mark usually represent?', ['One piece of data', 'The total of all data', 'The average of all data', 'Nothing at all'], 0),
   ('If a line plot shows 3 marks above the number 5, how many times did the value 5 occur in the data?', ['3', '5', '8', '2'], 0),
   ('A line plot is a useful tool because it helps us ___.', ['See how often each value occurs in a set of data', 'Measure temperature', 'Tell time', 'Measure length'], 0),
   ('If the number 4 has more marks above it than any other number on a line plot, what does that tell us?', ['The value 4 occurs most often in the data', 'The value 4 occurs least often', 'The value 4 was never counted', 'The value 4 is the smallest number'], 0)])

d68_sci = sub('Science', 'Clouds and the Weather They Bring',
  'Students learn to identify different types of clouds, such as fluffy cumulus clouds, thin wispy cirrus clouds, and gray stratus clouds, and connect them to the weather they often bring.',
  [('What do we call fluffy, cotton-like clouds often seen on a sunny day?', ['cumulus clouds', 'cumulus']),
   ('What do we call thin, wispy clouds high in the sky?', ['cirrus clouds', 'cirrus']),
   ('What do we call gray clouds that often cover the whole sky and can bring rain?', ['stratus clouds', 'stratus'])],
  [('What do we call fluffy, cotton-like clouds often seen on a sunny day?', ['Cumulus clouds', 'Cirrus clouds', 'Stratus clouds', 'Storm clouds only'], 0),
   ('What do we call thin, wispy clouds found high in the sky?', ['Cirrus clouds', 'Cumulus clouds', 'Stratus clouds', 'Rain clouds only'], 0),
   ('What do we call gray clouds that often cover the whole sky and can bring rain?', ['Stratus clouds', 'Cirrus clouds', 'Cumulus clouds', 'Clear clouds'], 0),
   ('Which type of cloud is most closely connected to a chance of rain covering the whole sky?', ['Stratus clouds', 'Cirrus clouds', 'Cumulus clouds', 'No clouds at all'], 0),
   ('Observing clouds can help us ___.', ['Predict what kind of weather might be coming', 'Change the weather instantly', 'Measure how heavy an object is', 'Tell exact time'], 0)])

d68_ss = sub('SocialStudies', 'Preparing for Severe Weather: Staying Safe',
  'Students learn simple steps for staying safe during severe weather, such as a thunderstorm or blizzard, including listening to an adult, staying indoors, and having an emergency kit ready.',
  [('What should you do during a thunderstorm to stay safe?', ['stay indoors', 'go inside', 'stay inside']),
   ('Who should you listen to during severe weather to stay safe?', ['an adult', 'a trusted adult', 'adults']),
   ('Name one item that might be in a family emergency kit, like a flashlight.', ['a flashlight', 'flashlight', 'water', 'batteries'])],
  [('What should you do during a thunderstorm to stay safe?', ['Stay indoors away from windows', 'Stand under a tall tree outside', 'Go swimming outside', 'Ignore the storm completely'], 0),
   ('Who should children listen to for guidance during severe weather?', ['A trusted adult', 'A stranger', 'No one', 'A pet'], 0),
   ('Which of these might be found in a family emergency kit?', ['A flashlight and batteries', 'A television remote', 'A video game', 'A bicycle'], 0),
   ('Why is it helpful for a family to have an emergency plan for severe weather?', ['So everyone knows what to do and stays safe', 'So the storm becomes stronger', 'So no one prepares at all', 'So the weather changes instantly'], 0),
   ('During a blizzard, which of these is a safe choice?', ['Staying inside a warm home', 'Walking far from home alone', 'Ignoring warnings from adults', 'Staying outside for a long time'], 0)])

# ─── DAY 69 ─────────────────────────────────────────────────────────────────
d69_lang = sub('Language', 'Root Words and Word Families',
  'Students learn that a root word is the base part of a word that carries its main meaning, and that other words can be built from it, such as play, playful, and player, all coming from the root word play.',
  [('What do we call the base part of a word that carries its main meaning?', ['a root word', 'root word']),
   ('What is the root word in the word playful?', ['play']),
   ('Name one word that can be built from the root word teach, like teacher.', ['teacher', 'teaching', 'teaches'])],
  [('What do we call the base part of a word that carries its main meaning?', ['A root word', 'A synonym', 'An antonym', 'A caption'], 0),
   ('What is the root word in the word playful?', ['Play', 'Ful', 'Full', 'Fully'], 0),
   ('Which of these words comes from the root word teach?', ['Teacher', 'Doctor', 'Farmer', 'Painter'], 0),
   ('Which group of words are all part of the same word family built from the root word jump?', ['Jump, jumped, jumping, jumper', 'Run, ran, running, runner', 'Play, player, playful, played', 'Read, reader, reading, reread'], 0),
   ('Understanding root words helps readers ___.', ['Figure out the meaning of related unfamiliar words', 'Forget how to read', 'Only read short words', 'Avoid learning new words'], 0)])

d69_math = sub('Math', 'Multiplication Facts: 2s, 5s, and 10s',
  'Students learn and practice basic multiplication facts for the 2 times table, 5 times table, and 10 times table, such as 2 times 3 equals 6.',
  [('What is 2 times 3?', ['6', 'six']),
   ('What is 5 times 4?', ['20', 'twenty']),
   ('What is 10 times 2?', ['20', 'twenty'])],
  [('What is 2 times 3?', ['6', '5', '7', '8'], 0),
   ('What is 5 times 4?', ['20', '15', '25', '10'], 0),
   ('What is 10 times 2?', ['20', '10', '12', '22'], 0),
   ('What is 5 times 5?', ['25', '20', '30', '15'], 0),
   ('Multiplication facts for the 10 times table always end in what digit?', ['0', '5', '1', '2'], 0)])

d69_sci = sub('Science', 'Animal Diets: Herbivores, Carnivores, and Omnivores',
  'Students learn that animals can be grouped by what they eat, such as herbivores that eat only plants, carnivores that eat only meat, and omnivores that eat both plants and meat.',
  [('What do we call an animal that eats only plants?', ['a herbivore', 'herbivore']),
   ('What do we call an animal that eats only meat?', ['a carnivore', 'carnivore']),
   ('What do we call an animal that eats both plants and meat?', ['an omnivore', 'omnivore'])],
  [('What do we call an animal that eats only plants?', ['A herbivore', 'A carnivore', 'An omnivore', 'A decomposer'], 0),
   ('What do we call an animal that eats only meat?', ['A carnivore', 'A herbivore', 'An omnivore', 'A producer'], 0),
   ('What do we call an animal that eats both plants and meat?', ['An omnivore', 'A herbivore', 'A carnivore', 'A decomposer'], 0),
   ('Which of these animals is a herbivore that eats mostly grass and leaves?', ['A deer', 'A lion', 'A wolf', 'A shark'], 0),
   ('Bears are often considered omnivores because they eat ___.', ['Both plants like berries and meat like fish', 'Only rocks and soil', 'Only sunlight', 'Only water'], 0)])

d69_ss = sub('SocialStudies', 'Life in Northern Canada: Weather and Ways of Living',
  'Students learn that Northern Canada has a cold climate with long winters, and that communities there have adapted their ways of living, travel, and clothing to the environment.',
  [('What kind of climate does Northern Canada have, with long cold winters?', ['a cold climate', 'cold climate']),
   ('Name one way people in Northern Canada might adapt to the cold climate, like wearing warm clothing.', ['wearing warm clothing', 'warm clothing', 'special travel methods']),
   ('Why might traveling in Northern Canada look different than traveling in a city?', ['because of snow and ice', 'because of the cold climate', 'different terrain'])],
  [('What kind of climate does Northern Canada generally have?', ['A cold climate with long winters', 'A hot climate with no winter', 'A rainy climate with no snow', 'A desert climate with no water'], 0),
   ('Which of these is a way people in Northern Canada might adapt to a cold climate?', ['Wearing warm layered clothing', 'Wearing sandals year round', 'Avoiding all winter clothing', 'Ignoring the cold weather'], 0),
   ('Why might communities in Northern Canada use different methods of travel than a big city?', ['Because of snow, ice, and remote locations', 'Because they have no need to travel', 'Because cars are not allowed anywhere in Canada', 'Because there are no roads anywhere in Canada'], 0),
   ('Which of these might be true about daylight in parts of Northern Canada during winter?', ['There can be very few hours of daylight', 'There is always exactly 12 hours of daylight', 'There is no daylight ever, all year', 'There is always more daylight than in summer'], 0),
   ('Learning about life in Northern Canada helps us understand ___.', ['How people adapt their lives to a unique climate', 'That all parts of Canada have the same weather', 'That no one lives in Northern Canada', 'That climate has no effect on daily life'], 0)])

# ─── DAY 70 (Final Review) ──────────────────────────────────────────────────
d70_lang = sub('Language', 'Final Review: Language Skills (Days 61-69)',
  'Students review Language skills from Days 61 to 69: irregular past tense verbs, sentence fragments, quotation marks, point of view, opinion writing, idioms, alliteration, reading fluency, and root words.',
  [('What is the past tense of the verb go?', ['went']),
   ('What do we call a group of words whose meaning is different from what the words literally say?', ['an idiom', 'idiom']),
   ('What do we call the base part of a word that carries its main meaning?', ['a root word', 'root word'])],
  [('What is the past tense of the verb go?', ['Went', 'Goed', 'Going', 'Goes'], 0),
   ('What two parts does a complete sentence need?', ['A subject and a verb', 'Only a noun', 'Only a question mark', 'Only a capital letter'], 0),
   ('What do we call the punctuation marks placed before and after the exact words a character speaks?', ['Quotation marks', 'A period', 'A comma', 'A question mark'], 0),
   ('What do we call the perspective from which a story is told?', ['Point of view', 'A caption', 'A heading', 'A theme'], 0),
   ('What do we call a group of words whose meaning is different from what the words literally say?', ['An idiom', 'A fact', 'A caption', 'A heading'], 0)])

d70_math = sub('Math', 'Final Review: Math Skills (Days 61-69)',
  'Students review Math skills from Days 61 to 69: place value to 1000, adding three numbers, missing number equations, arrays, thermometers, near doubles, number patterns, line plots, and multiplication facts.',
  [('How many hundreds are in the number 342?', ['3', 'three']),
   ('What is 2 + 3 + 4?', ['9', 'nine']),
   ('What is 2 times 3?', ['6', 'six'])],
  [('How many hundreds are in the number 342?', ['3', '4', '2', '7'], 0),
   ('What is 2 + 3 + 4?', ['9', '8', '10', '7'], 0),
   ('What number makes this true: 5 + ___ = 9?', ['4', '5', '9', '14'], 0),
   ('If an array has 3 rows with 4 objects in each row, how many objects are there in total?', ['12', '7', '10', '9'], 0),
   ('What is 2 times 3?', ['6', '5', '7', '8'], 0)])

d70_sci = sub('Science', 'Final Review: Science Skills (Days 61-69)',
  'Students review Science topics from Days 61 to 69: frog life cycles, fossils, wheels and axles, decomposers, plant adaptations, planets, breathing and lungs, clouds and weather, and animal diets.',
  [('What is the first stage of a frog life cycle?', ['egg', 'an egg']),
   ('What word describes the preserved remains or traces of ancient living things found in rock?', ['fossil', 'fossils']),
   ('What do we call an animal that eats only plants?', ['a herbivore', 'herbivore'])],
  [('What is the first stage of a frog life cycle?', ['Egg', 'Tadpole', 'Froglet', 'Adult frog'], 0),
   ('What word describes the preserved remains or traces of ancient living things?', ['A fossil', 'A crystal', 'A magnet', 'A shadow'], 0),
   ('What do we call living things that break down dead plants and animals?', ['Decomposers', 'Predators', 'Producers', 'Pollinators'], 0),
   ('Which planet do people live on?', ['Earth', 'Mars', 'Venus', 'Jupiter'], 0),
   ('What do we call an animal that eats only meat?', ['A carnivore', 'A herbivore', 'An omnivore', 'A producer'], 0)])

d70_ss = sub('SocialStudies', 'Final Review: Social Studies Skills (Days 61-69)',
  'Students review Social Studies topics from Days 61 to 69: local businesses, schools long ago and today, Canadian currency, national parks, time zones, food from around the world, addresses, severe weather safety, and life in Northern Canada.',
  [('What do we call the goods and services a business provides to help people?', ['goods and services', 'things people need']),
   ('What is the name of the Canadian one dollar coin?', ['loonie', 'the loonie']),
   ('What do we call an area of land protected to preserve nature and wildlife?', ['a national park', 'national park'])],
  [('Which of these is an example of a local business?', ['A bakery', 'A mountain', 'A river', 'A cloud'], 0),
   ('What is the name of the Canadian one dollar coin?', ['The loonie', 'The toonie', 'The nickel', 'The dime'], 0),
   ('What do we call an area of land protected to preserve nature and wildlife?', ['A national park', 'A shopping mall', 'A parking lot', 'A factory'], 0),
   ('What do we call the different regions of time across a wide country like Canada?', ['Time zones', 'Provinces', 'Territories', 'Continents'], 0),
   ('What should you do during a thunderstorm to stay safe?', ['Stay indoors away from windows', 'Stand under a tall tree outside', 'Go swimming outside', 'Ignore the storm completely'], 0)])


g2_61_70 = [
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
    _rebalance_answer_positions(g2_61_70, seed=20260831)
    append_worksheet_days(2, g2_61_70)
