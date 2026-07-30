#!/usr/bin/env python3
"""Grade 1, Days 111-120 -- ninth batch, extending Grade 1 past Day 110
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days101_110.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by fetch_video_ids.py)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-110 (see
data/grade1.ts / data/grade1.json, which already densely covers phonics,
grammar, number sense, and most elementary science/social-studies
subtopics): adverbs, new word families (-ell, -ick), dialogue and
quotation marks, table of contents/index, run-on sentences, summarizing,
journal writing, sensory words, and story grammar for Language; two-digit
regrouping, congruent shapes, shrinking patterns, estimating elapsed time,
metres, perimeter, number-line operations, and repeated addition for
Math; eyes, the digestive system, the solar system, mixing materials,
animal shelters, baby/adult teeth, wheels and axles, erosion, and plant
adaptations to dry/cold climates for Science; and the three Indigenous
groups, the coast guard, Canada's neighbour the United States, playground
safety, zoos, the Terry Fox Run, interprovincial trade, famous Canadians,
and global connections for Social Studies -- none of those exact ideas
appear in Days 1-110. Day 120 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch. No
embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely to keep the generated .ts string
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


g1_111_120 = [
day(111, [
L('Adverbs: Words That Describe Verbs',
  'Grade 1 Language strand: an adverb describes a verb and often tells how something is done, such as quickly, slowly, loudly, or quietly.',
  [('Give an example of an adverb.', ['quickly', 'slowly', 'loudly']),
   ('What does an adverb describe?', ['a verb', 'how an action happens']),
   ('In the sentence She sings loudly, which word is the adverb?', ['loudly', 'loudly is the adverb'])],
  [('Which word is an adverb?', ['Happy', 'Dog', 'Quickly', 'Table'], 2),
   ('An adverb usually describes a ___.', ['Noun', 'Verb', 'Colour', 'Number'], 1),
   ('In the sentence He runs fast, which word is the adverb?', ['He', 'Runs', 'Fast', 'The'], 2),
   ('Which sentence uses an adverb?', ['The cat is black.', 'The cat sleeps quietly.', 'The cat is a pet.', 'The cat has fur.'], 1),
   ('Which word tells how someone walked?', ['Slowly', 'Shoe', 'Path', 'Street'], 0)]),
M('Two-Digit Addition With Regrouping',
  'Grade 1 Math strand: when adding two two-digit numbers, if the ones digits add to 10 or more, students regroup by carrying a ten to the tens place.',
  [('When ones add to 10 or more, what do you do?', ['regroup', 'carry a ten']),
   ('What is 28 + 5?', ['33', '33']),
   ('What is 17 + 6?', ['23', '23'])],
  [('What is 26 + 7?', ['32', '33', '34', '35'], 1),
   ('When the ones digits add to 10 or more, we ___.', ['Ignore the extra', 'Carry a ten to the tens place', 'Stop adding', 'Subtract instead'], 1),
   ('What is 19 + 4?', ['22', '23', '24', '21'], 1),
   ('What is 35 + 8?', ['41', '42', '43', '44'], 2),
   ('What is 47 + 6?', ['52', '53', '54', '51'], 1)]),
Sc('Our Eyes: How We See Colours and Shapes',
   'Grade 1 Science strand: eyes are the body part we use to see colours, shapes, and light around us, and they send messages to our brain.',
   [('What body part do we use to see?', ['eyes', 'our eyes']),
    ('What do our eyes send messages to?', ['the brain', 'our brain']),
    ('Name one thing our eyes help us see.', ['colours', 'shapes', 'light'])],
   [('What body part helps us see?', ['Ears', 'Eyes', 'Nose', 'Skin'], 1),
    ('Our eyes send messages to the ___.', ['Heart', 'Brain', 'Lungs', 'Stomach'], 1),
    ('Which of these can our eyes help us notice?', ['Colours and shapes', 'Loud sounds', 'Sweet tastes', 'Soft textures'], 0),
    ('What do we need to be able to see things?', ['Light', 'Darkness only', 'Silence', 'Cold air'], 0),
    ('Which sense organ is used for seeing?', ['Tongue', 'Eyes', 'Ears', 'Skin'], 1)]),
SS('First Nations, Metis, and Inuit: Three Indigenous Groups in Canada',
   'Grade 1 Social Studies strand: Canada recognizes three distinct groups of Indigenous peoples -- First Nations, Metis, and Inuit -- each with their own history, languages, and traditions.',
   [('Name one of the three Indigenous groups in Canada.', ['First Nations', 'Metis', 'Inuit']),
    ('Do the three groups have their own languages and traditions?', ['yes', 'yes they do']),
    ('Why is it important to learn about all three groups?', ['they each have unique cultures', 'they are all part of Canadas history'])],
   [('What are the three recognized Indigenous groups in Canada?', ['First Nations, Metis, and Inuit', 'Settlers, Explorers, and Traders', 'Farmers, Fishers, and Hunters only', 'North, South, and East'], 0),
    ('Do First Nations, Metis, and Inuit peoples share the exact same culture?', ['Yes, they are identical', 'No, each has its own history and traditions', 'They have no traditions', 'Only one group has culture'], 1),
    ('The Inuit have traditionally lived mostly in which part of Canada?', ['The far north', 'The far south', 'Only cities', 'Outside Canada'], 0),
    ('Why do we learn about First Nations, Metis, and Inuit peoples?', ['They are an important part of Canadas history and present', 'They are not important', 'Only for one day a year', 'It is not required'], 0),
    ('What might make each Indigenous group unique?', ['Their own languages and traditions', 'They all speak one language', 'They have no history', 'They are all the same age'], 0)]),
]),
day(112, [
L('Word Families: -ell and -ick',
  'Grade 1 Language strand: the -ell word family includes bell, sell, and shell, while the -ick word family includes kick, lick, and stick.',
  [('Name a word in the -ell family.', ['bell', 'sell', 'shell']),
   ('Name a word in the -ick family.', ['kick', 'lick', 'stick']),
   ('What sound do bell and shell share?', ['ell', 'the ell sound'])],
  [('Which word belongs to the -ell family?', ['Bell', 'Bell', 'Bit', 'Bat'], 0),
   ('Which word belongs to the -ick family?', ['Kick', 'Kit', 'Cat', 'Cot'], 0),
   ('Which word rhymes with shell?', ['Shed', 'Bell', 'Ship', 'Shop'], 1),
   ('Which word rhymes with stick?', ['Stack', 'Stock', 'Kick', 'Stove'], 2),
   ('Word families help readers ___.', ['Recognize spelling patterns', 'Draw pictures', 'Count numbers', 'Sing loudly'], 0)]),
M('Two-Digit Subtraction With Regrouping',
  'Grade 1 Math strand: when subtracting and the ones digit of the top number is smaller, students regroup by borrowing a ten from the tens place.',
  [('What do you do when the top ones digit is too small to subtract?', ['borrow a ten', 'regroup']),
   ('What is 32 - 5?', ['27', '27']),
   ('What is 41 - 6?', ['35', '35'])],
  [('What is 43 - 8?', ['33', '34', '35', '36'], 2),
   ('When the top ones digit is smaller than the bottom, we ___.', ['Add instead', 'Borrow a ten from the tens place', 'Stop subtracting', 'Ignore the tens'], 1),
   ('What is 51 - 7?', ['42', '43', '44', '45'], 2),
   ('What is 62 - 9?', ['52', '53', '54', '55'], 1),
   ('What is 70 - 4?', ['64', '65', '66', '67'], 2)]),
Sc('The Digestive System: Where Food Goes',
   'Grade 1 Science strand: after we eat, food travels through our body from the mouth to the stomach, where our body breaks it down for energy.',
   [('Where does food first enter your body?', ['your mouth', 'the mouth']),
    ('What body part helps break down food after the mouth?', ['stomach', 'the stomach']),
    ('Why does our body break down food?', ['for energy', 'to get energy'])],
   [('Where does food first enter the digestive system?', ['The mouth', 'The stomach', 'The heart', 'The lungs'], 0),
    ('After the mouth, food travels down a tube toward the ___.', ['Brain', 'Stomach', 'Ears', 'Skin'], 1),
    ('Why does the body digest food?', ['To get energy from it', 'To make it disappear', 'To make it heavier', 'For no reason'], 0),
    ('The stomach helps to ___ food.', ['Freeze', 'Break down', 'Ignore', 'Colour'], 1),
    ('Which body system is used to process the food we eat?', ['The digestive system', 'The skeletal system', 'The respiratory system', 'The nervous system'], 0)]),
SS('Our Coast Guard: Keeping People Safe on the Water',
   'Grade 1 Social Studies strand: the coast guard is a group of community helpers who keep people safe on lakes, rivers, and oceans, including helping boats in trouble.',
   [('What does the coast guard help keep people safe on?', ['water', 'the water']),
    ('Name one thing the coast guard might do.', ['rescue a boat', 'help people in trouble']),
    ('Why is water safety important in Canada?', ['Canada has many lakes and coasts', 'to protect people near water'])],
   [('Where does the coast guard mainly help keep people safe?', ['On the water', 'In the sky', 'Underground', 'In classrooms'], 0),
    ('What might the coast guard do if a boat is in trouble?', ['Ignore it', 'Rescue the people aboard', 'Sell the boat', 'Paint the boat'], 1),
    ('Why does Canada need a coast guard?', ['Canada has many lakes, rivers, and coastlines', 'Canada has no water', 'Only for fun', 'It is not needed'], 0),
    ('Which of these is a coast guard responsibility?', ['Teaching math', 'Helping boats and swimmers stay safe', 'Delivering mail', 'Building houses'], 1),
    ('The coast guard is an example of a ___.', ['Community helper', 'Type of weather', 'Kind of animal', 'Type of food'], 0)]),
]),
day(113, [
L('Dialogue: Using Quotation Marks in Conversation',
  'Grade 1 Language strand: quotation marks show exactly what a character says out loud in a story, placed at the start and end of the spoken words.',
  [('What punctuation marks show a character is speaking?', ['quotation marks', 'quote marks']),
   ('Where are quotation marks placed?', ['around the spoken words', 'at the start and end of what is said']),
   ('In the sentence Sam said, I am happy, which words go inside quotation marks?', ['I am happy', 'I am happy is spoken'])],
  [('What punctuation shows exactly what a character says?', ['A period', 'Quotation marks', 'A comma', 'An exclamation mark'], 1),
   ('Where do quotation marks go around spoken words?', ['Only at the beginning', 'Only at the end', 'At the start and end of the spoken words', 'They are not used'], 2),
   ('In Mia said, Let us go, which part is inside quotation marks?', ['Mia said', 'Let us go', 'The whole sentence', 'Nothing'], 1),
   ('Dialogue in a story means ___.', ['The setting', 'Characters speaking to each other', 'The title', 'The ending only'], 1),
   ('Which sentence correctly shows dialogue?', ['Tom said hello.', 'Tom said, Hello there!', 'Tom, said hello.', 'Tom hello said.'], 1)]),
M('Congruent Shapes: Same Size and Shape',
  'Grade 1 Math strand: two shapes are congruent when they are exactly the same size and the same shape, like two identical squares.',
  [('What does congruent mean?', ['exactly the same size and shape', 'the same shape and size']),
   ('If two triangles are the same size and shape, are they congruent?', ['yes', 'yes they are']),
   ('Name two shapes that could be congruent.', ['two squares', 'two circles the same size'])],
  [('What does it mean for two shapes to be congruent?', ['They are the same colour', 'They are the same size and shape', 'They have different sizes', 'They are both triangles'], 1),
   ('Which pair of shapes could be congruent?', ['A big circle and a small circle', 'Two identical squares', 'A triangle and a rectangle', 'A circle and a square'], 1),
   ('If two shapes are congruent, one can fit exactly over the ___.', ['Table', 'Other one', 'Floor', 'Wall'], 1),
   ('Are a large square and a small square congruent?', ['Yes, always', 'No, they are different sizes', 'Only if red', 'Only on Mondays'], 1),
   ('Congruent shapes must match in ___.', ['Colour only', 'Size and shape', 'Weight only', 'Name only'], 1)]),
Sc('The Solar System: Planets Around the Sun',
   'Grade 1 Science strand: our solar system is made up of the sun and the planets, including Earth, that travel around it in paths called orbits.',
   [('What is at the centre of our solar system?', ['the sun', 'the sun is the centre']),
    ('What do planets do around the sun?', ['orbit it', 'travel around it']),
    ('Name one planet in our solar system.', ['Earth', 'Mars'])],
   [('What is at the centre of our solar system?', ['The Moon', 'The Sun', 'Earth', 'A star cluster'], 1),
    ('What do we call the path a planet takes around the sun?', ['A road', 'An orbit', 'A trail', 'A line'], 1),
    ('Which planet do we live on?', ['Mars', 'Earth', 'Venus', 'Jupiter'], 1),
    ('The word solar refers to the ___.', ['Moon', 'Sun', 'Stars', 'Sky'], 1),
    ('How many planets are commonly taught as part of our solar system?', ['Eight', 'Two', 'Twenty', 'One hundred'], 0)]),
SS('Canadas Neighbours: The United States',
   'Grade 1 Social Studies strand: the United States is the country that shares a long border with Canada to the south, and the two countries trade and travel between each other.',
   [('Which country is south of Canada?', ['The United States', 'the USA']),
    ('What do neighbouring countries often do with each other?', ['trade', 'travel between them']),
    ('Name one thing Canada and the United States share.', ['a border', 'a long border'])],
   [('Which country shares a long border with Canada?', ['Mexico', 'The United States', 'France', 'Japan'], 1),
    ('Where is the United States located compared to Canada?', ['North of Canada', 'South of Canada', 'East of Canada', 'Inside Canada'], 1),
    ('What might neighbouring countries do together?', ['Ignore each other', 'Trade goods and travel between them', 'Never communicate', 'Share no history'], 1),
    ('A border is ___.', ['A line that separates two countries', 'A type of food', 'A kind of animal', 'A holiday'], 0),
    ('Why is it useful to know about Canadas neighbours?', ['It helps us understand our place in the world', 'It is not useful', 'Neighbours do not matter', 'Only oceans matter'], 0)]),
]),
day(114, [
L('Text Features: Table of Contents and Index',
  'Grade 1 Language strand: a table of contents at the front of a book lists chapter titles and page numbers, while an index at the back helps readers find specific topics.',
  [('Where is a table of contents usually found?', ['at the front of the book', 'the front']),
   ('Where is an index usually found?', ['at the back of the book', 'the back']),
   ('What does a table of contents list?', ['chapter titles and page numbers', 'the chapters and pages'])],
  [('Where would you find a table of contents?', ['At the back of the book', 'At the front of the book', 'On the cover only', 'It does not exist'], 1),
   ('What does a table of contents usually show?', ['Chapter titles and page numbers', 'The authors life story', 'A glossary of words', 'Pictures only'], 0),
   ('Where would you usually find an index?', ['At the front', 'In the middle', 'At the back of the book', 'On the cover'], 2),
   ('An index helps readers ___.', ['Find specific topics quickly', 'Colour the pages', 'Skip the whole book', 'Write a new story'], 0),
   ('Which text feature would help you find page 42 for chapter 3?', ['A table of contents', 'A glossary', 'A caption', 'A title'], 0)]),
M('Patterns: Shrinking Patterns',
  'Grade 1 Math strand: a shrinking pattern is a sequence that gets smaller or decreases each time, such as 20, 15, 10, 5.',
  [('In the pattern 20, 15, 10, ___, what comes next?', ['5', 'five']),
   ('Does a shrinking pattern get bigger or smaller?', ['smaller', 'it gets smaller']),
   ('Give an example of a shrinking pattern.', ['20, 15, 10, 5', '10, 8, 6, 4'])],
  [('In the pattern 18, 14, 10, ___, what comes next?', ['4', '5', '6', '8'], 2),
   ('A shrinking pattern is a sequence that ___.', ['Stays the same', 'Gets smaller each time', 'Gets bigger each time', 'Has no order'], 1),
   ('Which sequence is a shrinking pattern?', ['2, 4, 6, 8', '20, 16, 12, 8', '1, 1, 1, 1', '5, 10, 15, 20'], 1),
   ('In the pattern 30, 25, 20, ___, what comes next?', ['10', '15', '18', '22'], 1),
   ('What is the opposite of a shrinking pattern?', ['A repeating pattern', 'A growing pattern', 'No pattern', 'A colour pattern'], 1)]),
Sc('Mixing Materials: Combining Solids and Liquids',
   'Grade 1 Science strand: when we mix materials, such as stirring sand into water or sugar into juice, some materials dissolve and others do not.',
   [('What happens when sugar is stirred into warm water?', ['it dissolves', 'it disappears into the water']),
    ('Does sand dissolve in water?', ['no', 'no it does not']),
    ('What word means a solid seems to disappear into a liquid?', ['dissolve', 'dissolving'])],
   [('What happens when you stir sugar into warm water?', ['It sinks and stays solid', 'It dissolves into the water', 'It turns into a gas', 'Nothing happens'], 1),
    ('Does sand dissolve when mixed into water?', ['Yes, completely', 'No, it stays as solid grains', 'It disappears forever', 'It turns into sugar'], 1),
    ('What word describes a solid seeming to disappear into a liquid?', ['Freezing', 'Dissolving', 'Melting', 'Evaporating'], 1),
    ('Which of these would dissolve in warm water?', ['Salt', 'A rock', 'A marble', 'A spoon'], 0),
    ('Mixing materials together is a way scientists ___.', ['Ignore matter', 'Investigate how materials behave', 'Avoid learning', 'Waste time'], 1)]),
SS('Playground Safety: Rules for Playing Together',
   'Grade 1 Social Studies strand: playground rules, such as taking turns and using equipment properly, help keep everyone safe while having fun together.',
   [('Name one playground safety rule.', ['take turns', 'use equipment properly']),
    ('Why do playgrounds have rules?', ['to keep everyone safe', 'so no one gets hurt']),
    ('What should you do if you see someone get hurt at the playground?', ['tell an adult', 'get help'])],
   [('Why do playgrounds have safety rules?', ['To keep everyone safe while having fun', 'To make playing boring', 'Rules are not needed', 'To stop all games'], 0),
    ('Which is an example of a playground safety rule?', ['Pushing to go first', 'Taking turns on the slide', 'Climbing where it is not allowed', 'Ignoring others'], 1),
    ('What should you do if a friend gets hurt on the playground?', ['Walk away', 'Tell an adult for help', 'Laugh', 'Ignore it'], 1),
    ('Using playground equipment properly means ___.', ['Following the rules for how to use it', 'Using it however you want', 'Breaking it', 'Avoiding it always'], 0),
    ('Playground rules help build a community that is ___.', ['Unsafe', 'Safe and fair for everyone', 'Confusing', 'Unfriendly'], 1)]),
]),
day(115, [
L('Run-on Sentences: Too Many Ideas at Once',
  'Grade 1 Language strand: a run-on sentence happens when two or more complete ideas are joined without correct punctuation, making the sentence confusing.',
  [('What is a run-on sentence?', ['too many ideas joined without punctuation', 'ideas joined incorrectly']),
   ('Why are run-on sentences confusing?', ['too many ideas at once', 'there is no clear break']),
   ('How can we fix a run-on sentence?', ['add a period or split it', 'split it into two sentences'])],
  [('What is a run-on sentence?', ['A very short sentence', 'Too many ideas joined without proper punctuation', 'A sentence with no words', 'A question'], 1),
   ('Why can run-on sentences be hard to read?', ['They have too many ideas joined together', 'They are too short', 'They have no letters', 'They are always questions'], 0),
   ('How can you fix a run-on sentence?', ['Add more ideas', 'Split it into two clear sentences', 'Remove all punctuation', 'Make it longer'], 1),
   ('Which is a run-on sentence?', ['I like dogs. I like cats.', 'I like dogs I like cats they are fun', 'I like dogs.', 'Do you like dogs?'], 1),
   ('A complete sentence needs a clear ___.', ['Beginning and end', 'Colour', 'Rhyme', 'Number'], 0)]),
M('Time: Estimating How Long an Activity Takes',
  'Grade 1 Math strand: students estimate whether an activity, like brushing teeth or eating dinner, takes seconds, minutes, or hours.',
  [('Would brushing your teeth take seconds, minutes, or hours?', ['minutes', 'a few minutes']),
   ('Would sleeping overnight take minutes or hours?', ['hours', 'many hours']),
   ('Would clapping your hands once take seconds or hours?', ['seconds', 'a second'])],
  [('About how long does it take to brush your teeth?', ['A few seconds', 'A few minutes', 'A few hours', 'A whole day'], 1),
   ('About how long does a full night of sleep take?', ['A few minutes', 'A few seconds', 'About eight or more hours', 'One second'], 2),
   ('About how long does it take to snap your fingers?', ['A second', 'An hour', 'A day', 'A week'], 0),
   ('Which activity would likely take hours, not minutes?', ['Blinking your eyes', 'A school day', 'Clapping once', 'Saying hello'], 1),
   ('Estimating time helps us guess ___.', ['The colour of an object', 'About how long something takes', 'The weight of an object', 'The taste of food'], 1)]),
Sc('Animal Shelters: Nests, Burrows, and Shells',
   'Grade 1 Science strand: animals build or use different kinds of shelters to stay safe, including nests for birds, burrows for rabbits, and shells for turtles.',
   [('What kind of shelter does a bird often build?', ['a nest', 'nest']),
    ('What kind of shelter does a rabbit often dig?', ['a burrow', 'burrow']),
    ('What shelter does a turtle carry with it?', ['a shell', 'its shell'])],
   [('What shelter do many birds build?', ['A burrow', 'A nest', 'A shell', 'A den'], 1),
    ('What do we call an underground home dug by an animal like a rabbit?', ['A nest', 'A burrow', 'A hive', 'A web'], 1),
    ('What shelter does a turtle always carry with it?', ['A nest', 'A burrow', 'A shell', 'A web'], 2),
    ('Why do animals need shelters?', ['To stay safe from weather and predators', 'For decoration', 'They do not need shelters', 'Only to sleep'], 0),
    ('Which animal is known for spinning a web as part of its home?', ['A spider', 'A rabbit', 'A turtle', 'A bird'], 0)]),
SS('Zoos and Wildlife Parks: Caring for Animals in Human Care',
   'Grade 1 Social Studies strand: zoos and wildlife parks care for animals, teach visitors about wildlife, and sometimes help protect endangered species.',
   [('Name one thing a zoo does for animals.', ['cares for them', 'protects them']),
    ('What can visitors learn at a zoo?', ['about wildlife', 'about different animals']),
    ('Why might zoos help endangered animals?', ['to protect them', 'so they do not disappear'])],
   [('What is one job of a zoo?', ['Caring for and studying animals', 'Selling toys only', 'Ignoring animals', 'Farming crops'], 0),
    ('What can people learn by visiting a zoo?', ['About different kinds of wildlife', 'Nothing new', 'Only about pets', 'About cars'], 0),
    ('Why might a zoo help care for an endangered animal?', ['To help protect the species', 'Endangered animals do not need help', 'For no reason', 'To sell them'], 0),
    ('Who usually works at a zoo caring for the animals?', ['Zookeepers', 'Firefighters', 'Pilots', 'Bakers'], 0),
    ('A wildlife park is similar to a zoo because it also ___.', ['Ignores wildlife', 'Cares for and protects animals', 'Sells cars', 'Has no animals'], 1)]),
]),
day(116, [
L('Summarizing: Retelling a Story in Fewer Words',
  'Grade 1 Language strand: summarizing means retelling the most important parts of a story using fewer words than the original text.',
  [('What does summarizing mean?', ['retelling with fewer words', 'telling the important parts briefly']),
   ('Why do we summarize a story?', ['to share the main parts quickly', 'so it is shorter']),
   ('Should a summary include every small detail?', ['no', 'no just the important parts'])],
  [('What does it mean to summarize a story?', ['Retell it word for word', 'Retell only the most important parts in fewer words', 'Ignore the story', 'Add many new details'], 1),
   ('Why is summarizing a useful skill?', ['It helps us share the main idea quickly', 'It makes stories longer', 'It removes the main idea', 'It is not useful'], 0),
   ('Should a summary include small, unimportant details?', ['Yes, all details', 'No, only the most important parts', 'Only the title', 'Only the pictures'], 1),
   ('A good summary is usually ___ than the original story.', ['Longer', 'Shorter', 'The same length', 'Twice as long'], 1),
   ('Which is an example of summarizing?', ['Copying the whole book', 'Telling the main events in a few sentences', 'Reading it out loud', 'Ignoring the story'], 1)]),
M('Measuring Length in Metres: Longer Distances',
  'Grade 1 Math strand: while centimetres measure small objects, metres are used to measure longer distances, such as the length of a classroom.',
  [('What unit measures longer distances than a centimetre?', ['a metre', 'metres']),
   ('Would you measure a classroom in centimetres or metres?', ['metres', 'metres because it is long']),
   ('Would you measure a pencil in centimetres or metres?', ['centimetres', 'centimetres because it is short'])],
  [('Which unit is used to measure longer distances?', ['Centimetres', 'Metres', 'Grams', 'Litres'], 1),
   ('Which object would you most likely measure in metres?', ['A pencil', 'A classroom', 'A paperclip', 'A crayon'], 1),
   ('Which object would you most likely measure in centimetres?', ['A hallway', 'A pencil', 'A soccer field', 'A classroom'], 1),
   ('A metre is ___ than a centimetre.', ['Shorter', 'Longer', 'The same', 'Heavier'], 1),
   ('Why do we use different measurement units?', ['To match the size of what we measure', 'Units do not matter', 'To confuse people', 'Only metres are used'], 0)]),
Sc('Baby Teeth and Adult Teeth: How Our Teeth Change',
   'Grade 1 Science strand: children have a set of baby teeth that eventually fall out and are replaced by permanent adult teeth as they grow.',
   [('What do we call the first set of teeth children have?', ['baby teeth', 'baby teeth or milk teeth']),
    ('What happens to baby teeth as we grow?', ['they fall out', 'fall out and are replaced']),
    ('What replaces baby teeth?', ['adult teeth', 'permanent teeth'])],
   [('What are a childs first set of teeth called?', ['Adult teeth', 'Baby teeth', 'Wisdom teeth', 'Fake teeth'], 1),
    ('What eventually happens to baby teeth?', ['They stay forever', 'They fall out and are replaced', 'They turn into bones', 'They disappear with no replacement'], 1),
    ('What teeth replace baby teeth?', ['Permanent adult teeth', 'More baby teeth', 'No teeth at all', 'Wooden teeth'], 0),
    ('Why is it important to take care of both baby and adult teeth?', ['Healthy teeth help us eat and stay healthy', 'Teeth do not matter', 'Only adult teeth need care', 'Teeth care is unnecessary'], 0),
    ('Roughly when do most children begin losing baby teeth?', ['Around age five or six', 'At birth', 'At age eighteen', 'They never lose them'], 0)]),
SS('The Terry Fox Run: A Canadian Tradition of Giving',
   'Grade 1 Social Studies strand: the Terry Fox Run is an annual Canadian event where people walk or run together to raise money for cancer research, honouring a brave young Canadian.',
   [('What does the Terry Fox Run raise money for?', ['cancer research', 'to help fight cancer']),
    ('Is the Terry Fox Run a Canadian tradition?', ['yes', 'yes it is']),
    ('What do people do during the Terry Fox Run?', ['walk or run together', 'run or walk to raise money'])],
   [('What does the Terry Fox Run help raise money for?', ['Cancer research', 'New toys', 'Building roads', 'Buying food'], 0),
    ('The Terry Fox Run happens ___.', ['Only once, long ago', 'Every year across Canada', 'Never', 'Only in one city'], 1),
    ('What do participants usually do at the Terry Fox Run?', ['Walk or run together', 'Sit and watch', 'Sleep all day', 'Play video games'], 0),
    ('Why do schools across Canada take part in the Terry Fox Run?', ['To honour Terry Fox and support a cause', 'It has no meaning', 'It is required with no purpose', 'To skip school'], 0),
    ('The Terry Fox Run is an example of Canadians ___.', ['Ignoring important causes', 'Coming together to give and help others', 'Competing for money', 'Avoiding community events'], 1)]),
]),
day(117, [
L('Journal Writing: Writing About My Day',
  'Grade 1 Language strand: journal writing lets students write about their own experiences, thoughts, and feelings, often using the word I and describing real events.',
  [('What do we write about in a journal?', ['our own experiences', 'our thoughts and feelings']),
   ('What pronoun do journal entries often use?', ['I', 'the word I']),
   ('Give an example of something you could write in a journal.', ['what I did today', 'how I felt'])],
  [('What is journal writing mainly about?', ['A made-up fantasy world', 'Our own experiences, thoughts, and feelings', 'Only math facts', 'Someone elses life'], 1),
   ('Which pronoun is commonly used in journal writing?', ['They', 'I', 'It', 'We only'], 1),
   ('Which sentence sounds like a journal entry?', ['The dog ran fast.', 'Today I played outside with my friend.', 'Dogs are mammals.', 'The sky is blue.'], 1),
   ('Why might someone keep a journal?', ['To remember and reflect on their day', 'To hide their thoughts forever', 'It has no purpose', 'To copy a textbook'], 0),
   ('A journal entry usually describes ___.', ['Real events from the writers life', 'Only fictional dragons', 'Math equations', 'Weather reports only'], 0)]),
M('Perimeter: Measuring Around a Shape',
  'Grade 1 Math strand: the perimeter of a shape is the total distance around its outside edge, found by adding the length of all its sides.',
  [('What is perimeter?', ['the distance around a shape', 'the total distance around the edge']),
   ('How do you find the perimeter of a shape?', ['add all the sides', 'add up the side lengths']),
   ('What is the perimeter of a square with sides of 3?', ['12', '12 because 3+3+3+3']),
  ],
  [('What does perimeter measure?', ['The space inside a shape', 'The distance around a shape', 'The weight of a shape', 'The colour of a shape'], 1),
   ('How do you find the perimeter of a shape?', ['Multiply the sides', 'Add up the lengths of all the sides', 'Count the corners', 'Measure only one side'], 1),
   ('What is the perimeter of a square with each side equal to 4?', ['8', '12', '16', '20'], 2),
   ('A rectangle has sides of 5, 3, 5, and 3. What is its perimeter?', ['15', '16', '18', '13'], 2),
   ('Perimeter is measured using units such as ___.', ['Litres', 'Centimetres or metres', 'Grams', 'Degrees'], 1)]),
Sc('Simple Machines: Wheels and Axles',
   'Grade 1 Science strand: a wheel and axle is a simple machine made of a wheel attached to a rod, which makes it easier to move heavy things, like on a wagon or bicycle.',
   [('What simple machine is found on a wagon?', ['a wheel and axle', 'wheel and axle']),
    ('What does a wheel and axle make easier?', ['moving heavy things', 'moving objects']),
    ('Name one object that uses wheels and axles.', ['a bicycle', 'a wagon', 'a car'])],
   [('What simple machine helps a wagon move easily?', ['A lever', 'A wheel and axle', 'A pulley', 'A screw'], 1),
    ('A wheel and axle is made of a wheel attached to a ___.', ['Rope', 'Rod', 'Ramp', 'Wedge'], 1),
    ('Which object uses a wheel and axle?', ['A bicycle', 'A seesaw', 'A doorstop', 'A spoon'], 0),
    ('Why are wheels useful simple machines?', ['They make moving heavy things easier', 'They make objects heavier', 'They stop motion', 'They are only decorative'], 0),
    ('Which of these also uses wheels and axles to move?', ['A car', 'A book', 'A chair', 'A pillow'], 0)]),
SS('Trade Between Provinces: Sharing Resources Across Canada',
   'Grade 1 Social Studies strand: different provinces in Canada have different resources, so they trade goods like fish, lumber, and grain with one another.',
   [('Why do provinces trade with each other?', ['they have different resources', 'to share what they have']),
    ('Name one resource a province might trade.', ['fish', 'lumber', 'grain']),
    ('What is it called when provinces exchange goods?', ['trade', 'trading'])],
   [('Why do Canadian provinces trade goods with each other?', ['They each have different resources', 'They all have identical resources', 'Trade is not allowed', 'They never need anything'], 0),
    ('Which is an example of a resource a province might trade?', ['Fish', 'Sunshine', 'Air', 'Silence'], 0),
    ('What word describes provinces exchanging goods with each other?', ['Trade', 'Ignoring', 'Hiding', 'Wasting'], 0),
    ('How does trading resources help Canadians?', ['It lets people get things their own province may not have', 'It hurts communities', 'It stops all sharing', 'It has no benefit'], 0),
    ('A province known for forests might trade ___.', ['Lumber', 'Only sand', 'Nothing at all', 'Only ice'], 0)]),
]),
day(118, [
L('Sensory Words: Describing with Our Five Senses',
  'Grade 1 Language strand: sensory words help writers describe what something looks, sounds, smells, tastes, or feels like, making writing more vivid.',
  [('Name a sensory word that describes a sound.', ['loud', 'quiet']),
   ('Name a sensory word that describes a taste.', ['sweet', 'sour']),
   ('Why do writers use sensory words?', ['to make writing vivid', 'to help readers imagine it'])],
  [('What do sensory words help describe?', ['Only numbers', 'What something looks, sounds, smells, tastes, or feels like', 'Only colours', 'Only shapes'], 1),
   ('Which word is a sensory word describing taste?', ['Bright', 'Sweet', 'Loud', 'Tall'], 1),
   ('Which word describes how something feels to touch?', ['Soft', 'Sour', 'Bright', 'Loud'], 0),
   ('Why do authors use sensory words in their writing?', ['To make the writing dull', 'To help readers imagine the scene vividly', 'To confuse readers', 'To remove all description'], 1),
   ('Which sentence uses a sensory word?', ['The dog ran.', 'The soft, furry dog ran.', 'The dog is a pet.', 'A dog is an animal.'], 1)]),
M('Using a Number Line to Add and Subtract',
  'Grade 1 Math strand: a number line can help solve addition and subtraction problems by jumping forward to add or jumping backward to subtract.',
  [('On a number line, which direction do you jump to add?', ['forward', 'to the right']),
   ('On a number line, which direction do you jump to subtract?', ['backward', 'to the left']),
   ('Using a number line, what is 4 + 3?', ['7', '7'])],
  [('On a number line, which direction shows addition?', ['Backward', 'Forward', 'Sideways', 'It does not matter'], 1),
   ('On a number line, which direction shows subtraction?', ['Forward', 'Backward', 'Upward', 'Downward'], 1),
   ('Using a number line, what is 6 + 4?', ['9', '10', '11', '8'], 1),
   ('Using a number line, what is 9 - 3?', ['5', '6', '7', '8'], 1),
   ('A number line is a useful tool because it shows numbers ___.', ['In random order', 'In order, making jumps easy to see', 'Only as pictures', 'Without any order'], 1)]),
Sc('Erosion: How Wind and Water Change the Land',
   'Grade 1 Science strand: erosion happens when wind or water slowly wears away soil and rock, changing the shape of the land over time.',
   [('What can wear away soil and rock over time?', ['wind and water', 'wind or water']),
    ('What do we call this slow wearing away of land?', ['erosion', 'erosion is the word']),
    ('Does erosion happen quickly or slowly?', ['slowly', 'usually slowly'])],
   [('What is erosion?', ['Land suddenly appearing', 'Wind or water slowly wearing away soil and rock', 'Rain falling from clouds', 'Plants growing quickly'], 1),
    ('Which of these can cause erosion?', ['Wind and water', 'Silence', 'Darkness', 'Cold air alone'], 0),
    ('Erosion usually happens ___.', ['Instantly', 'Slowly over time', 'Only in winter', 'Never'], 1),
    ('What might erosion change over a long time?', ['The shape of the land', 'The colour of the sky', 'The taste of water', 'The sound of wind'], 0),
    ('Which landform might be shaped by water erosion over many years?', ['A canyon', 'A cloud', 'A rainbow', 'A shadow'], 0)]),
SS('Famous Canadians: People Who Made a Difference',
   'Grade 1 Social Studies strand: many Canadians throughout history have made important contributions in science, sports, the arts, and their communities.',
   [('What does it mean to make a difference?', ['to help or improve something', 'to have a positive impact']),
    ('Name a way a person could make a difference in Canada.', ['through science', 'through sports', 'through art']),
    ('Why do we learn about famous Canadians?', ['to be inspired by them', 'to learn from their contributions'])],
   [('What does it mean when someone makes a difference?', ['They help or improve something for others', 'They do nothing at all', 'They cause problems', 'They ignore their community'], 0),
    ('In which area might a famous Canadian have made a contribution?', ['Science, sports, or the arts', 'Only sleeping', 'Only eating', 'Nothing at all'], 0),
    ('Why do students learn about people who made a difference?', ['To be inspired and learn from their example', 'It has no purpose', 'To memorize random facts', 'To ignore history'], 0),
    ('A person who works hard to help their community is being a good ___.', ['Stranger', 'Citizen', 'Visitor', 'Bystander'], 1),
    ('Learning about important Canadians helps us understand ___.', ['Our shared history and values', 'Nothing useful', 'Only foreign countries', 'Random unrelated facts'], 0)]),
]),
day(119, [
L('Story Grammar: Characters, Setting, Problem, and Solution Together',
  'Grade 1 Language strand: story grammar combines the key parts of a story -- characters, setting, problem, and solution -- to help readers understand how a story fits together.',
  [('Name the four main parts of story grammar.', ['characters, setting, problem, solution', 'characters, setting, problem, and solution']),
   ('What is the problem in a story?', ['the challenge the characters face', 'a challenge that needs solving']),
   ('What is the solution in a story?', ['how the problem is solved', 'the way the problem gets solved'])],
  [('Which four parts make up story grammar?', ['Title, author, cover, pages', 'Characters, setting, problem, and solution', 'Loud, quiet, fast, slow', 'Beginning, ending only'], 1),
   ('What is the setting of a story?', ['The characters feelings', 'Where and when the story happens', 'The books cover', 'The last sentence'], 1),
   ('What is the problem in a story?', ['The challenge the characters must solve', 'The title of the book', 'The authors name', 'The illustration'], 0),
   ('What is the solution in a story?', ['The way the problem gets solved', 'The beginning of the story', 'The setting', 'The characters names'], 0),
   ('Why is it helpful to know all four parts of story grammar?', ['It helps readers understand how a story fits together', 'It makes stories longer', 'It has no benefit', 'It replaces reading the story'], 0)]),
M('Repeated Addition: Adding Equal Groups',
  'Grade 1 Math strand: when equal groups of objects are combined, students can find the total using repeated addition, such as 3 + 3 + 3 for three groups of three.',
  [('If you have 3 groups of 3, what repeated addition shows this?', ['3+3+3', '3 plus 3 plus 3']),
   ('What is 3+3+3?', ['9', '9']),
   ('If you have 4 groups of 2, what is the total?', ['8', '8'])],
  [('Which repeated addition shows 4 groups of 2?', ['2+2+2+2', '4+4', '2+4', '4+2+2'], 0),
   ('What is 2+2+2+2?', ['6', '7', '8', '9'], 2),
   ('If you have 5 groups of 2 apples, how many apples in all?', ['8', '9', '10', '12'], 2),
   ('What is 4+4+4?', ['8', '10', '12', '14'], 2),
   ('Repeated addition is useful when groups are ___.', ['Different sizes', 'Equal in size', 'Empty', 'Unknown'], 1)]),
Sc('Plant Adaptations: Surviving in Dry and Cold Places',
   'Grade 1 Science strand: plants have special features called adaptations that help them survive in tough environments, like thick leaves in the desert or short stems in the cold.',
   [('What do we call special features that help plants survive?', ['adaptations', 'plant adaptations']),
    ('Name one way a desert plant might survive with little water.', ['thick leaves', 'storing water']),
    ('Why might a plant in a cold place grow low to the ground?', ['to stay protected from wind and cold', 'to survive the cold'])],
   [('What word describes special features that help plants survive their environment?', ['Habitats', 'Adaptations', 'Migrations', 'Predators'], 1),
    ('How might a desert plant, like a cactus, survive with little rain?', ['By storing water in thick stems or leaves', 'By needing lots of daily rain', 'By growing very tall only', 'By living underwater'], 0),
    ('Why might plants in cold places grow low to the ground?', ['To stay protected from cold wind', 'To reach more sunlight only', 'To attract more animals', 'For no reason'], 0),
    ('Plant adaptations help plants ___.', ['Survive in their environment', 'Move to new places', 'Talk to animals', 'Change colour instantly'], 0),
    ('Which environment would likely require water-saving adaptations?', ['A desert', 'A rainforest', 'A swamp', 'A lake'], 0)]),
SS('The Global Village: How We Are Connected to Other Countries',
   'Grade 1 Social Studies strand: the idea of a global village means that people, goods, and information can connect quickly with other countries around the world.',
   [('What does global village mean?', ['the world feels connected', 'countries are connected to each other']),
    ('Name one way people connect with other countries.', ['travel', 'communication', 'trade']),
    ('Why is our world considered connected today?', ['information and goods travel quickly', 'we can communicate easily'])],
   [('What does the term global village describe?', ['A single small town', 'How the world feels connected through travel and communication', 'A type of farm', 'A kind of forest'], 1),
    ('Which of these helps connect countries around the world?', ['Trade and communication', 'Ignoring each other', 'Building walls only', 'Avoiding travel'], 0),
    ('Why might a toy in your home be made in another country?', ['Countries trade goods with each other', 'Toys can only be made locally', 'Trade does not exist', 'It is impossible'], 0),
    ('Which is an example of global connection?', ['A video call with someone in another country', 'Never leaving your street', 'Ignoring the news', 'Avoiding maps'], 0),
    ('Understanding the global village helps us see that ___.', ['Countries are isolated from each other', 'Countries are connected in many ways', 'Only one country matters', 'The world has no connections'], 1)]),
]),
day(120, [
L('Language Review: Adverbs, Dialogue, and Story Grammar',
  'Grade 1 Language strand review: students revisit adverbs, the word families -ell and -ick, dialogue and quotation marks, summarizing, and the four parts of story grammar.',
  [('Give an example of an adverb.', ['quickly', 'slowly']),
   ('What punctuation shows a character is speaking?', ['quotation marks', 'quote marks']),
   ('Name the four parts of story grammar.', ['characters, setting, problem, solution', 'characters, setting, problem, and solution'])],
  [('Which word is an adverb?', ['Happy', 'Dog', 'Quickly', 'Table'], 2),
   ('What punctuation shows exactly what a character says?', ['A period', 'Quotation marks', 'A comma', 'An exclamation mark'], 1),
   ('What does it mean to summarize a story?', ['Retell it word for word', 'Retell only the most important parts in fewer words', 'Ignore the story', 'Add many new details'], 1),
   ('Which four parts make up story grammar?', ['Title, author, cover, pages', 'Characters, setting, problem, and solution', 'Loud, quiet, fast, slow', 'Beginning, ending only'], 1),
   ('Which word belongs to the -ick family?', ['Kick', 'Kit', 'Cat', 'Cot'], 0)]),
M('Math Review: Regrouping, Shapes, and Patterns',
  'Grade 1 Math strand review: students revisit two-digit addition and subtraction with regrouping, congruent shapes, shrinking patterns, perimeter, and repeated addition.',
  [('What is 26 + 7?', ['33', '33']),
   ('What does congruent mean?', ['same size and shape', 'exactly the same size and shape']),
   ('How do you find the perimeter of a shape?', ['add all the sides', 'add up the side lengths'])],
  [('What is 43 - 8?', ['33', '34', '35', '36'], 2),
   ('What does it mean for two shapes to be congruent?', ['They are the same colour', 'They are the same size and shape', 'They have different sizes', 'They are both triangles'], 1),
   ('In the pattern 18, 14, 10, ___, what comes next?', ['4', '5', '6', '8'], 2),
   ('What is the perimeter of a square with each side equal to 4?', ['8', '12', '16', '20'], 2),
   ('Which repeated addition shows 4 groups of 2?', ['2+2+2+2', '4+4', '2+4', '4+2+2'], 0)]),
Sc('Science Review: Our Bodies, Space, and the Land',
   'Grade 1 Science strand review: students revisit our eyes, the digestive system, the solar system, mixing materials, animal shelters, and plant adaptations.',
   [('What body part helps us see?', ['eyes', 'our eyes']),
    ('What is at the centre of our solar system?', ['the sun', 'the sun is']),
    ('What word describes wind or water wearing away land?', ['erosion', 'erosion is the word'])],
   [('What body part helps us see?', ['Ears', 'Eyes', 'Nose', 'Skin'], 1),
    ('Where does food first enter the digestive system?', ['The mouth', 'The stomach', 'The heart', 'The lungs'], 0),
    ('What is at the centre of our solar system?', ['The Moon', 'The Sun', 'Earth', 'A star cluster'], 1),
    ('What do we call an underground home dug by an animal like a rabbit?', ['A nest', 'A burrow', 'A hive', 'A web'], 1),
    ('What is erosion?', ['Land suddenly appearing', 'Wind or water slowly wearing away soil and rock', 'Rain falling from clouds', 'Plants growing quickly'], 1)]),
SS('Social Studies Review: Indigenous Peoples, Helpers, and Our World',
   'Grade 1 Social Studies strand review: students revisit the three Indigenous groups in Canada, the coast guard, Canadas neighbours, playground safety, the Terry Fox Run, and the global village.',
   [('Name one of the three Indigenous groups in Canada.', ['First Nations', 'Metis', 'Inuit']),
    ('Where does the coast guard mainly help keep people safe?', ['on the water', 'the water']),
    ('What does the Terry Fox Run raise money for?', ['cancer research', 'to help fight cancer'])],
   [('What are the three recognized Indigenous groups in Canada?', ['First Nations, Metis, and Inuit', 'Settlers, Explorers, and Traders', 'Farmers, Fishers, and Hunters only', 'North, South, and East'], 0),
    ('Where does the coast guard mainly help keep people safe?', ['On the water', 'In the sky', 'Underground', 'In classrooms'], 0),
    ('Which country shares a long border with Canada?', ['Mexico', 'The United States', 'France', 'Japan'], 1),
    ('What does the Terry Fox Run help raise money for?', ['Cancer research', 'New toys', 'Building roads', 'Buying food'], 0),
    ('What does the term global village describe?', ['A single small town', 'How the world feels connected through travel and communication', 'A type of farm', 'A kind of forest'], 1)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_111_120)
    append_worksheet_days(1, g1_111_120)
