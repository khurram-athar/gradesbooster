#!/usr/bin/env python3
"""Grade 1, Days 181-187 -- sixteenth and FINAL batch for Grade 1, completing the
full 187-day Ontario curriculum target (180 + 7 = 187). Self-contained script
(does NOT use gen_curriculum.py's sub()/day()/append_to() helpers, since those
do not support a worksheet field) modeled exactly on gen_grade1_days171_180.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

This batch is only 6 new content days (181-186, one new topic per subject per
day) plus Day 187 as a final cross-subject review day, since 180 + 7 = 187 is
the full-year target (instead of the usual 9-new-day + 1-review-day pattern).

Topics chosen to avoid overlap with existing Grade 1 Days 1-180 (every
existing (subject, title) pair was dumped from data/grade1.json and checked
against the topics below before writing): the vowel team oe (long o in toe
and hoe), speech bubbles as a text feature in comics, understanding character
feelings, acrostic poems, book talks, and expanding sentences with more
detail for Language. Numbers to 800, fractions as eighths, composite shapes
(combining simple shapes to make new ones), money up to fifty dollars,
comparing durations (which activity takes longer), and sorting data by two
attributes at once for Math. Rabbits, groundhogs, animal mimicry (as
distinct from the camouflage day already used), chickens (egg to hen life
cycle), decomposers, and constellations for Science (all new animals/topics,
not reusing any fox, squirrel, wolf, skunk, black bear, deer, moose, raccoon,
snail, crab, camel, polar bear, elephant, giraffe, chameleon, beaver, whale,
shark, turtle, frog, penguin, owl, bat, or other animal/space topic from
earlier batches). The CN Tower, Groundhog Day, bakers, ferries and ships,
foods from around the world, and powwows for Social Studies (new landmark,
holiday, helper, transportation, culture, and Indigenous-culture topics,
distinct from the many landmark, holiday, helper, and Indigenous days
already used in Days 1-180).

Day 187 is the final review day across all four subjects, matching the
mechanical end-of-batch review pattern used in every prior batch (dump
selected facts from the batch into a short worksheet and quiz per subject),
but since this is the very last day of the entire 187-day Grade 1 curriculum
build, its four review titles ("A Year of Words, Stories, and Poems", "A
Year of Numbers, Shapes, and Problem Solving", "A Year of Discovering Our
World", "A Year of Community, Culture, and Canada") lean into a capstone,
end-of-program tone while still following the exact mechanical review-day
format used in every prior batch. All four Day 187 review titles were
checked against every "Review" title already present in data/grade1.json
and are textually distinct from all of them.

No embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely, matching this project's convention (e.g.
"Canadas" not "Canada's", "Natures" not "Nature's", "Its" needs no
apostrophe since it is already the correct possessive pronoun), since this
text gets embedded directly into TypeScript string literals.

After this script runs and build_json.py is run, data/grade1.json will have
exactly 187 days, completing Grade 1's full-year Ontario curriculum target.
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


def _rebalance_answer_positions(days, seed=20260818):
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


g1_181_187 = [
day(181, [
L('Vowel Team oe: The Long O Sound in Toe and Hoe',
  'Grade 1 Language strand: the vowel team oe can make the long o sound in words such as toe, hoe, and foe, helping readers recognize this less common way to spell long o.',
  [('What sound does the vowel team oe usually make?', ['the long o sound', 'long o']),
   ('Give an example of a word that has the oe vowel team.', ['toe', 'hoe', 'foe']),
   ('How many letters are in the vowel team oe?', ['2', 'two'])],
  [('What sound does the vowel team oe make in the word toe?', ['The long o sound', 'The short o sound', 'The long e sound', 'The long a sound'], 0),
   ('Which word contains the oe vowel team?', ['Hoe', 'Hot', 'Hop', 'Ham'], 0),
   ('How many letters make up the vowel team oe?', ['2', '1', '3', '4'], 0),
   ('Which of these words rhymes with toe using the oe vowel team?', ['Foe', 'Fun', 'Fit', 'Fat'], 0),
   ('The oe vowel team is a less common way to spell which sound?', ['Long o', 'Short o', 'Long i', 'Short a'], 0)]),
M('Numbers to 800: Beyond 700',
  'Grade 1 Math strand: students read, write, and count numbers beyond 700, up to 800.',
  [('What number comes right after 799?', ['800', 'eight hundred']),
   ('What number comes right before 750?', ['749', 'seven hundred forty nine']),
   ('Count by tens from 780 to 800.', ['780,790,800', '780 790 800'])],
  [('What number comes right after 799?', ['800', '799', '801', '798'], 0),
   ('Which number is between 720 and 740?', ['730', '710', '750', '760'], 0),
   ('What number comes right before 800?', ['799', '800', '798', '801'], 0),
   ('Which of these numbers is the largest?', ['799', '699', '599', '499'], 0),
   ('Counting beyond 700 helps us understand numbers up to ___.', ['800', '80', '8', '8000'], 0)]),
Sc('Rabbits: Hopping Mammals of Meadows and Gardens',
   'Grade 1 Science strand: rabbits are small mammals with long ears and strong back legs that let them hop quickly, and they eat plants such as grass, clover, and garden vegetables.',
   [('What body part helps a rabbit hop quickly?', ['its back legs', 'strong back legs']),
    ('What do rabbits mainly eat?', ['plants', 'grass and vegetables']),
    ('What kind of animal is a rabbit?', ['a mammal'])],
   [('What helps a rabbit hop quickly?', ['Its strong back legs', 'Its tail only', 'Its ears only', 'Its whiskers only'], 0),
    ('What do rabbits mainly eat?', ['Plants such as grass and clover', 'Fish', 'Other animals', 'Insects only'], 0),
    ('What kind of animal is a rabbit?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('What body part do rabbits have that is especially long?', ['Their ears', 'Their tail', 'Their nose', 'Their whiskers'], 0),
    ('Rabbits are often found living in which kind of place?', ['Meadows and gardens', 'The ocean floor', 'Deep caves underwater', 'The desert only'], 0)]),
SS('The CN Tower: A Famous Toronto Landmark',
   'Grade 1 Social Studies strand: the CN Tower is a very tall tower in Toronto, Ontario, that people can visit to see far across the city and learn about Canadian engineering.',
   [('In which city is the CN Tower located?', ['Toronto', 'Toronto, Ontario']),
    ('What can people do at the top of the CN Tower?', ['see far across the city', 'look out over the city']),
    ('What province is Toronto in?', ['Ontario'])],
   [('In which city is the CN Tower located?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 0),
    ('What can visitors do at the top of the CN Tower?', ['See far across the city', 'Go swimming', 'Ride a horse', 'Plant a garden'], 0),
    ('In which province is the CN Tower located?', ['Ontario', 'Quebec', 'Alberta', 'Manitoba'], 0),
    ('What is the CN Tower an example of?', ['A famous Canadian landmark', 'A type of food', 'A kind of animal', 'A weather pattern'], 0),
    ('The CN Tower shows off Canadian skill in what area?', ['Engineering', 'Farming', 'Fishing', 'Mining'], 0)]),
]),
day(182, [
L('Text Features: Speech Bubbles in Comics and Graphic Novels',
  'Grade 1 Language strand: speech bubbles are a text feature used in comics and graphic novels to show what a character is saying, helping readers follow the conversation.',
  [('What do speech bubbles show?', ['what a character is saying', 'what characters say']),
   ('In what kind of books do we often see speech bubbles?', ['comics', 'comics and graphic novels']),
   ('Why are speech bubbles helpful to readers?', ['help us follow the conversation', 'easier to follow what characters say'])],
  [('What do speech bubbles usually show in a comic?', ['What a character is saying', 'The title of the book', 'The page number', 'The authors name'], 0),
   ('In which kind of text would you most likely see speech bubbles?', ['A graphic novel', 'A dictionary', 'A weather report', 'A math worksheet'], 0),
   ('Why do authors use speech bubbles?', ['To help readers follow what characters say', 'To make the pages blank', 'To hide the story', 'To replace all pictures'], 0),
   ('A speech bubble is an example of what kind of feature?', ['A text feature', 'A punctuation mark', 'A vowel team', 'A suffix'], 0),
   ('Speech bubbles usually point toward which part of a picture?', ['The character who is speaking', 'The background only', 'The page number', 'The title'], 0)]),
M('Fractions: Eighths of a Whole',
  'Grade 1 Math strand: when a whole is divided into eight equal parts, each part is called an eighth, written as one out of eight equal pieces.',
  [('What is each equal part called when a whole is split into eight pieces?', ['an eighth', 'one eighth']),
   ('How many equal parts make a whole when it is divided into eighths?', ['8', 'eight']),
   ('If you eat one eighth of a pizza, how many equal pieces are left?', ['7', 'seven'])],
  [('What is each equal part called when a whole is divided into eight pieces?', ['An eighth', 'A half', 'A third', 'A fourth'], 0),
   ('How many equal parts make up a whole divided into eighths?', ['8', '6', '4', '2'], 0),
   ('If a pizza is cut into eighths, how many pieces does it have in total?', ['8', '6', '4', '2'], 0),
   ('Which fraction shows one out of eight equal parts?', ['One eighth', 'One half', 'One third', 'One fourth'], 0),
   ('For parts to be called eighths, they must be ___.', ['Equal in size', 'Different sizes', 'Only two pieces', 'Not connected'], 0)]),
Sc('Groundhogs: Diggers That Sleep All Winter',
   'Grade 1 Science strand: groundhogs are burrowing mammals that dig underground homes and hibernate, sleeping through most of the winter until warmer weather returns.',
   [('What do groundhogs dig?', ['underground homes', 'burrows']),
    ('What do groundhogs do during winter?', ['hibernate', 'sleep through winter']),
    ('What kind of animal is a groundhog?', ['a mammal'])],
   [('What do groundhogs dig underground?', ['Burrows to live in', 'Tunnels to the ocean', 'Nests in trees', 'Ponds for swimming'], 0),
    ('What do groundhogs do for most of the winter?', ['Hibernate', 'Migrate south', 'Stay awake and play', 'Build igloos'], 0),
    ('What kind of animal is a groundhog?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Where do groundhogs usually make their homes?', ['Underground burrows', 'Tall trees', 'Rivers', 'Caves under the sea'], 0),
    ('Groundhogs are known for being skilled ___.', ['Diggers', 'Swimmers', 'Flyers', 'Climbers only'], 0)]),
SS('Groundhog Day: A Late-Winter Tradition',
   'Grade 1 Social Studies strand: Groundhog Day is a late-winter tradition celebrated in February when people watch to see whether a groundhog sees its shadow, a fun custom said to predict more winter weather or an early spring.',
   [('In what month is Groundhog Day celebrated?', ['February']),
    ('What do people watch for on Groundhog Day?', ['whether a groundhog sees its shadow', 'a groundhogs shadow']),
    ('What season does Groundhog Day happen near the end of?', ['winter', 'late winter'])],
   [('In which month is Groundhog Day celebrated?', ['February', 'May', 'August', 'November'], 0),
    ('What do people watch for on Groundhog Day?', ['Whether a groundhog sees its shadow', 'A parade of animals', 'A fireworks show', 'A snowstorm forecast only'], 0),
    ('Groundhog Day is a tradition that is said to predict what?', ['More winter weather or an early spring', 'The next holiday', 'The weather for the whole year', 'A new school year'], 0),
    ('During which season does Groundhog Day take place?', ['Late winter', 'Summer', 'Early autumn', 'Mid spring'], 0),
    ('Groundhog Day is an example of a fun community ___.', ['Tradition', 'Law', 'Election', 'Invention'], 0)]),
]),
day(183, [
L('Character Feelings: Understanding How a Character Feels',
  'Grade 1 Language strand: readers can understand how a character feels by paying attention to their words, actions, and facial expressions described in the story.',
  [('Name one clue that shows how a character feels.', ['their words', 'their actions', 'their facial expressions']),
   ('Why is it helpful to understand a characters feelings?', ['helps us understand the story better', 'understand why they act that way']),
   ('Give an example of a feeling a character might have in a story.', ['happy', 'sad', 'scared', 'excited'])],
  [('Which of these can show how a character feels?', ['Their words and actions', 'The page number', 'The book cover colour', 'The font size'], 0),
   ('Why do readers try to understand a characters feelings?', ['It helps us understand the story better', 'It has no real purpose', 'It replaces reading the words', 'It only matters for pictures'], 0),
   ('If a character is smiling and laughing, how might they feel?', ['Happy', 'Angry', 'Scared', 'Bored'], 0),
   ('If a character is crying, how might they feel?', ['Sad', 'Excited', 'Proud', 'Calm'], 0),
   ('Understanding character feelings helps readers make a stronger ___ with the story.', ['Connection', 'Wall', 'Distance', 'Silence'], 0)]),
M('Composite Shapes: Combining Simple Shapes to Make New Ones',
  'Grade 1 Math strand: a composite shape is made by combining two or more simple shapes, such as putting a triangle on top of a square to make a shape like a house.',
  [('What is a composite shape?', ['a shape made of two or more simple shapes', 'a shape made by combining shapes']),
   ('Name two shapes you could combine to make a house shape.', ['a triangle and a square', 'triangle and square']),
   ('Can a composite shape be made from more than two simple shapes?', ['yes'])],
  [('What is a composite shape?', ['A shape made by combining two or more simple shapes', 'A shape with only one side', 'A shape that has no corners', 'A shape that cannot be drawn'], 0),
   ('Which two shapes could combine to make a shape like a house?', ['A triangle and a square', 'Two circles', 'Two triangles only', 'A circle and a line'], 0),
   ('Can a composite shape be made from more than two simple shapes?', ['Yes, it can combine several shapes', 'No, only exactly two shapes', 'No, composite shapes are impossible', 'Only circles can be combined'], 0),
   ('Which of these is an example of a composite shape?', ['A rocket made of a triangle and a rectangle', 'A single circle', 'A single square', 'A single triangle'], 0),
   ('Combining simple shapes to build new ones helps us understand ___.', ['Geometry', 'Weather', 'Money', 'Time'], 0)]),
Sc('Animal Mimicry: Looking Like Something Else for Safety',
   'Grade 1 Science strand: mimicry is when an animal looks like a different, often dangerous animal or object to trick predators and stay safe, which is different from camouflage, where an animal blends into its surroundings.',
   [('What is mimicry?', ['when an animal looks like something else for safety', 'looking like a different animal to stay safe']),
    ('How is mimicry different from camouflage?', ['mimicry looks like something else, camouflage blends in', 'camouflage blends in, mimicry copies another animal']),
    ('Why might an animal use mimicry?', ['to trick predators', 'to stay safe'])],
   [('What is mimicry?', ['When an animal looks like something else to stay safe', 'When an animal changes colour to blend in', 'When an animal hides underground', 'When an animal migrates south'], 0),
    ('How is mimicry different from camouflage?', ['Mimicry copies another animal or object, camouflage blends into surroundings', 'They are exactly the same thing', 'Mimicry only happens underwater', 'Camouflage only happens in winter'], 0),
    ('Why might an animal use mimicry?', ['To trick predators and stay safe', 'To find more food only', 'To grow bigger', 'To make more noise'], 0),
    ('Which of these is an example of mimicry?', ['A harmless insect looking like a stinging wasp', 'A polar bear having white fur in snow', 'A chameleon changing colour', 'A bird migrating south for winter'], 0),
    ('Mimicry is a way that animals ___ to survive.', ['Adapt', 'Sleep', 'Grow taller', 'Change diet'], 0)]),
SS('Bakers: Baking Bread and Treats for Our Community',
   'Grade 1 Social Studies strand: a baker is a community helper who bakes bread, cakes, and other treats for people in our community to enjoy and share.',
   [('What does a baker make?', ['bread and treats', 'bread, cakes, and other treats']),
    ('Where might you go to buy something a baker made?', ['a bakery']),
    ('Why are bakers important to our community?', ['they make food for people to enjoy', 'provide bread and treats'])],
   [('What does a baker make?', ['Bread, cakes, and other treats', 'Mail and packages', 'Medicine', 'Furniture'], 0),
    ('Where would you go to buy food made by a baker?', ['A bakery', 'A fire station', 'A library', 'An airport'], 0),
    ('Why are bakers important to a community?', ['They make food for people to enjoy and share', 'They have no real job', 'They only work one day a year', 'They fix cars'], 0),
    ('A baker is an example of what kind of community member?', ['A community helper', 'A farmer only', 'A pilot', 'A judge'], 0),
    ('Bakers often start their work very ___ in the morning to have fresh food ready.', ['Early', 'Late', 'Never', 'Once a year'], 0)]),
]),
day(184, [
L('Acrostic Poems: Writing a Poem Using a Word',
  'Grade 1 Language strand: an acrostic poem uses each letter of a chosen word, written down the page, as the first letter of a new line describing that word.',
  [('What does an acrostic poem use to start each line?', ['a letter from the chosen word', 'each letter of a word']),
   ('Where is the chosen word written in an acrostic poem?', ['down the page', 'down the side']),
   ('Write one line that could start an acrostic poem for the word SUN.', ['Shining bright', 'Sunny and warm'])],
  [('What does an acrostic poem use to begin each line?', ['A letter from the chosen word', 'A random number', 'A drawing', 'A question mark'], 0),
   ('How is the chosen word arranged in an acrostic poem?', ['Written down the page, one letter per line', 'Written backwards only', 'Hidden at the very end', 'Never written at all'], 0),
   ('Which of these could be the first line of an acrostic poem for the word CAT?', ['Cuddly and soft', 'A big loud truck', 'Zooming down the street', 'Playing in the rain'], 0),
   ('An acrostic poem is an example of what kind of writing?', ['Poetry', 'A letter', 'A recipe', 'A newspaper article'], 0),
   ('Writing an acrostic poem helps students practise thinking of words that ___.', ['Match a chosen letter', 'Rhyme only', 'Are always long', 'Have no meaning'], 0)]),
M('Money: Making Amounts Up to Fifty Dollars',
  'Grade 1 Math strand: students combine coins and bills to make amounts of money up to fifty dollars.',
  [('How many ten dollar bills make fifty dollars?', ['5', 'five ten dollar bills']),
   ('Name a way to make fifty dollars using bills.', ['a fifty dollar bill', 'five ten dollar bills']),
   ('If you have two twenty dollar bills and one ten dollar bill, how much money do you have?', ['50 dollars', 'fifty dollars'])],
  [('How many ten dollar bills would you need to make fifty dollars?', ['5', '4', '3', '6'], 0),
   ('Which combination makes exactly fifty dollars?', ['Five ten dollar bills', 'Two ten dollar bills', 'Three five dollar bills', 'One twenty dollar bill'], 0),
   ('If you have two twenty dollar bills and one ten dollar bill, how much money do you have?', ['50 dollars', '40 dollars', '30 dollars', '60 dollars'], 0),
   ('Which single bill is worth fifty dollars?', ['A fifty dollar bill', 'A twenty dollar bill', 'A ten dollar bill', 'A five dollar bill'], 0),
   ('Practising with amounts up to fifty dollars helps us understand ___.', ['Even larger amounts of money', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('Chickens: From Egg to Hen',
   'Grade 1 Science strand: chickens hatch from eggs, grow into fluffy baby chicks, and then grow into adult hens or roosters, part of the life cycle of this common farm bird.',
   [('What do baby chickens hatch from?', ['eggs', 'an egg']),
    ('What is a baby chicken called?', ['a chick']),
    ('What is an adult female chicken called?', ['a hen'])],
   [('What do baby chickens hatch from?', ['Eggs', 'Cocoons', 'Seeds', 'Nests only'], 0),
    ('What is a baby chicken called?', ['A chick', 'A calf', 'A kit', 'A joey'], 0),
    ('What is an adult female chicken called?', ['A hen', 'A rooster', 'A chick', 'A duckling'], 0),
    ('What kind of animal is a chicken?', ['A bird', 'A mammal', 'A reptile', 'A fish'], 0),
    ('The stages a chicken goes through as it grows are called its ___.', ['Life cycle', 'Habitat', 'Food chain', 'Migration'], 0)]),
SS('Ferries and Ships: Travelling on the Water',
   'Grade 1 Social Studies strand: ferries and ships are large boats that carry people, cars, and goods across lakes, rivers, and oceans, an important way to travel and transport items where there are no roads or bridges.',
   [('What do ferries and ships carry?', ['people, cars, and goods', 'people and goods']),
    ('Where do ferries and ships travel?', ['across lakes, rivers, and oceans', 'on water']),
    ('Why are ferries useful where there are no roads or bridges?', ['they help people and goods cross the water', 'provide a way to travel across water'])],
   [('What do ferries and ships often carry?', ['People, cars, and goods', 'Only mail', 'Only animals', 'Only ice'], 0),
    ('Where do ferries and ships travel?', ['Across lakes, rivers, and oceans', 'Only on roads', 'Only in the sky', 'Only underground'], 0),
    ('Why are ferries especially useful in some places?', ['They help people cross water where there are no roads or bridges', 'They fly over mountains', 'They dig tunnels', 'They deliver mail only'], 0),
    ('Which of these is an example of a large boat that carries cars and people?', ['A ferry', 'A bicycle', 'An airplane', 'A train'], 0),
    ('Ferries and ships are an important way to ___ across water.', ['Travel and transport goods', 'Stay in one place', 'Avoid other communities', 'Grow food'], 0)]),
]),
day(185, [
L('Book Talk: Sharing Our Favourite Books With Others',
  'Grade 1 Language strand: a book talk is a short spoken description of a book that shares what it is about and why we like it, helping other readers decide if they want to read it too.',
  [('What is a book talk?', ['a short spoken description of a book', 'talking about a book we like']),
   ('Name one thing you might share during a book talk.', ['what the book is about', 'why we like it']),
   ('Why might a book talk help other readers?', ['helps them decide if they want to read it', 'gives them an idea about the book'])],
  [('What is a book talk?', ['A short spoken description of a book', 'A written test about a book', 'A picture drawn from a book', 'A silent reading period'], 0),
   ('What might someone share during a book talk?', ['What the book is about and why they like it', 'Only the page count', 'Only the price of the book', 'Only the authors birthday'], 0),
   ('Why might a book talk be helpful to other readers?', ['It helps them decide if they want to read the book', 'It tells them the ending only', 'It replaces reading altogether', 'It has no real purpose'], 0),
   ('A book talk is an example of what kind of communication?', ['Spoken communication', 'Written communication only', 'Silent communication', 'No communication at all'], 0),
   ('Sharing our favourite books with others can help build a love of ___.', ['Reading', 'Silence', 'Homework', 'Weather'], 0)]),
M('Comparing Durations: Which Activity Takes Longer',
  'Grade 1 Math strand: comparing durations means deciding which of two activities takes more time, such as figuring out that brushing your teeth takes less time than eating dinner.',
  [('Which usually takes longer, brushing your teeth or eating dinner?', ['eating dinner']),
   ('Which usually takes longer, a school day or recess?', ['a school day']),
   ('Name two activities and tell which one takes longer.', ['answers vary'])],
  [('Which activity usually takes longer, brushing your teeth or eating dinner?', ['Eating dinner', 'Brushing your teeth', 'They take the same amount of time', 'Neither takes any time'], 0),
   ('Which activity usually takes longer, a school day or recess?', ['A school day', 'Recess', 'They are exactly the same length', 'Neither has a length'], 0),
   ('Which of these activities would likely take the least amount of time?', ['Blinking your eyes', 'Watching a movie', 'Sleeping at night', 'Going on a car trip'], 0),
   ('Comparing durations means deciding which activity takes ___ time.', ['More or less', 'The same amount of', 'No', 'An unknown amount of'], 0),
   ('Which activity would likely take longer, reading one page or reading a whole book?', ['Reading a whole book', 'Reading one page', 'They take the same time', 'Neither takes time'], 0)]),
Sc('Decomposers: Natures Recyclers',
   'Grade 1 Science strand: decomposers, such as earthworms and fungi, break down dead plants and animals into simple materials that enrich the soil and help new plants grow.',
   [('What do decomposers break down?', ['dead plants and animals', 'dead plants and animals into simple materials']),
    ('Name one example of a decomposer.', ['earthworms', 'fungi']),
    ('How do decomposers help the soil?', ['they enrich the soil', 'help new plants grow'])],
   [('What do decomposers break down?', ['Dead plants and animals', 'Rocks only', 'Water only', 'Sunlight only'], 0),
    ('Which of these is an example of a decomposer?', ['An earthworm', 'A rabbit', 'A hawk', 'A deer'], 0),
    ('How do decomposers help the soil?', ['They enrich it so new plants can grow', 'They remove all nutrients', 'They make the soil disappear', 'They have no effect on soil'], 0),
    ('Why are decomposers sometimes called natures recyclers?', ['They turn dead material into materials that help new life grow', 'They collect garbage from homes', 'They build new roads', 'They make electricity'], 0),
    ('Decomposers are an important part of a healthy ___.', ['Ecosystem', 'Classroom', 'Vehicle', 'Building'], 0)]),
SS('Foods from Around the World: Sharing Culture Through Food',
   'Grade 1 Social Studies strand: families from different cultures often enjoy special foods that are part of their traditions, and sharing these foods with others helps us learn about and appreciate different cultures.',
   [('Why do families from different cultures often have special foods?', ['the foods are part of their traditions', 'part of their culture']),
    ('What can sharing foods from other cultures help us do?', ['learn about different cultures', 'appreciate different cultures']),
    ('Name a food from a culture different from your own.', ['answers vary'])],
   [('Why do families from different cultures often eat special foods?', ['The foods are part of their traditions', 'They have no other choice', 'It is required by law', 'They dislike other foods'], 0),
    ('What can trying foods from other cultures help us do?', ['Learn about and appreciate different cultures', 'Forget our own culture', 'Avoid making new friends', 'Stop celebrating traditions'], 0),
    ('Sharing food from our own culture with others is a way of ___.', ['Sharing our traditions', 'Hiding our traditions', 'Ignoring others', 'Avoiding celebrations'], 0),
    ('Which of these is an example of learning about culture through food?', ['Trying a dish from a friends family tradition', 'Reading only about weather', 'Studying only shapes', 'Watching only sports'], 0),
    ('Canada is home to people from many cultures, which means our communities enjoy a variety of ___.', ['Foods and traditions', 'Weather patterns only', 'Shapes only', 'Colours only'], 0)]),
]),
day(186, [
L('Expanding Sentences: Adding More Detail to Our Writing',
  'Grade 1 Language strand: expanding a sentence means adding more detail, such as describing words or information about where and when, to make a simple sentence more interesting.',
  [('What does expanding a sentence mean?', ['adding more detail', 'adding more detail to a sentence']),
   ('Name one kind of detail we can add to expand a sentence.', ['a describing word', 'where or when something happened']),
   ('Expand this sentence with one detail: The dog ran.', ['The big dog ran quickly', 'The dog ran in the park'])],
  [('What does expanding a sentence mean?', ['Adding more detail to make it more interesting', 'Making the sentence shorter', 'Removing all the words', 'Changing the sentence into a question'], 0),
   ('Which of these is an expanded version of The dog ran?', ['The big brown dog ran quickly across the yard', 'Dog ran', 'Ran', 'The'], 0),
   ('Which kind of word can help expand a sentence with more detail?', ['A describing word', 'A silent letter', 'A blank space', 'A number only'], 0),
   ('Adding where or when something happened is one way to ___.', ['Expand a sentence', 'Shorten a sentence', 'End a sentence early', 'Remove punctuation'], 0),
   ('Expanding our sentences helps our writing become more ___.', ['Detailed and interesting', 'Confusing', 'Empty', 'Repetitive without meaning'], 0)]),
M('Data: Sorting Information by Two Attributes',
  'Grade 1 Math strand: objects can be sorted using two attributes at the same time, such as sorting shapes by both colour and size, to organize information in more detailed ways.',
  [('What does sorting by two attributes mean?', ['sorting using two features at once', 'sorting by two things at the same time']),
   ('Name two attributes you could use to sort shapes.', ['colour and size', 'colour and shape']),
   ('If you sort buttons by colour and shape, how many things are you thinking about at once?', ['2', 'two'])],
  [('What does sorting by two attributes mean?', ['Sorting using two features at the same time', 'Sorting using no features at all', 'Sorting only by colour', 'Sorting only by size'], 0),
   ('Which of these shows sorting by two attributes?', ['Grouping big red shapes together and small blue shapes together', 'Grouping everything into one pile', 'Ignoring all features', 'Sorting only by weight'], 0),
   ('Which two attributes could you use to sort a group of toy cars?', ['Colour and size', 'Only sound', 'Only smell', 'Only taste'], 0),
   ('Sorting by two attributes helps us organize information in a more ___ way.', ['Detailed', 'Confusing', 'Random', 'Incomplete'], 0),
   ('If shapes are sorted by colour and shape, how many attributes are being used?', ['2', '1', '3', '0'], 0)]),
Sc('Constellations: Patterns of Stars in the Night Sky',
   'Grade 1 Science strand: a constellation is a group of stars that forms a pattern in the night sky, and people have used constellations for a long time to tell stories and find their way.',
   [('What is a constellation?', ['a group of stars that forms a pattern', 'a pattern of stars in the sky']),
    ('When can we usually see constellations?', ['at night', 'in the night sky']),
    ('Name one thing people have used constellations for.', ['telling stories', 'finding their way'])],
   [('What is a constellation?', ['A group of stars that forms a pattern', 'A single bright planet', 'A type of cloud', 'A kind of moon phase'], 0),
    ('When can we usually see constellations in the sky?', ['At night', 'Only at noon', 'Only during a storm', 'Only underwater'], 0),
    ('What have people used constellations for in the past?', ['Telling stories and finding their way', 'Growing plants', 'Cooking food', 'Building houses'], 0),
    ('Constellations are made up of what?', ['Stars', 'Clouds', 'Planets only', 'Raindrops'], 0),
    ('Looking at patterns of stars in the sky is part of studying ___.', ['Space', 'The ocean', 'The soil', 'Plants'], 0)]),
SS('Powwows: Celebrating Indigenous Culture Through Dance and Music',
   'Grade 1 Social Studies strand: a powwow is a gathering where Indigenous peoples celebrate their culture through traditional dancing, drumming, singing, and regalia, welcoming others to learn and take part.',
   [('What is a powwow?', ['a gathering to celebrate Indigenous culture', 'a gathering with dancing, drumming, and singing']),
    ('Name one activity that happens at a powwow.', ['dancing', 'drumming', 'singing']),
    ('What can visitors do at a powwow?', ['learn about Indigenous culture', 'take part and learn'])],
   [('What is a powwow?', ['A gathering to celebrate Indigenous culture through dance and music', 'A type of weather event', 'A kind of building', 'A sports competition only'], 0),
    ('Which of these activities happens at a powwow?', ['Traditional dancing and drumming', 'Only silent reading', 'Only swimming', 'Only shopping'], 0),
    ('What is regalia at a powwow?', ['Special traditional clothing worn for dancing', 'A type of food', 'A musical instrument only', 'A kind of drum only'], 0),
    ('What can visitors do when they attend a powwow?', ['Learn about and take part in Indigenous culture', 'Ignore the event completely', 'Only watch from far away with no learning', 'Avoid all traditions'], 0),
    ('Powwows help communities celebrate and share ___.', ['Indigenous culture and traditions', 'Only modern inventions', 'Only sports scores', 'Only weather patterns'], 0)]),
]),
day(187, [
L('Language Review: A Year of Words, Stories, and Poems',
  'Grade 1 Language strand review, and a capstone review closing out the full year of Grade 1 Language: students revisit the vowel team oe, speech bubbles as a text feature, character feelings, acrostic poems, book talks, and expanding sentences.',
  [('What sound does the vowel team oe make in the word toe?', ['the long o sound']),
   ('What is a book talk?', ['a short spoken description of a book']),
   ('What does expanding a sentence mean?', ['adding more detail'])],
  [('What sound does the vowel team oe make?', ['The long o sound', 'The short o sound', 'The long e sound', 'The long a sound'], 0),
   ('What do speech bubbles usually show in a comic?', ['What a character is saying', 'The title of the book', 'The page number', 'The authors name'], 0),
   ('Which of these can show how a character feels?', ['Their words and actions', 'The page number', 'The book cover colour', 'The font size'], 0),
   ('What does an acrostic poem use to begin each line?', ['A letter from the chosen word', 'A random number', 'A drawing', 'A question mark'], 0),
   ('What does expanding a sentence mean?', ['Adding more detail to make it more interesting', 'Making the sentence shorter', 'Removing all the words', 'Changing the sentence into a question'], 0)]),
M('Math Review: A Year of Numbers, Shapes, and Problem Solving',
  'Grade 1 Math strand review, and a capstone review closing out the full year of Grade 1 Math: students revisit numbers to 800, fractions as eighths, composite shapes, money up to fifty dollars, comparing durations, and sorting data by two attributes.',
  [('What number comes right after 799?', ['800']),
   ('What is each equal part called when a whole is divided into eight pieces?', ['an eighth']),
   ('How many ten dollar bills make fifty dollars?', ['5', 'five'])],
  [('What number comes right after 799?', ['800', '799', '801', '798'], 0),
   ('What is each equal part called when a whole is divided into eight pieces?', ['An eighth', 'A half', 'A third', 'A fourth'], 0),
   ('What is a composite shape?', ['A shape made by combining two or more simple shapes', 'A shape with only one side', 'A shape that has no corners', 'A shape that cannot be drawn'], 0),
   ('Which combination makes exactly fifty dollars?', ['Five ten dollar bills', 'Two ten dollar bills', 'Three five dollar bills', 'One twenty dollar bill'], 0),
   ('Which activity usually takes longer, brushing your teeth or eating dinner?', ['Eating dinner', 'Brushing your teeth', 'They take the same amount of time', 'Neither takes any time'], 0)]),
Sc('Science Review: A Year of Discovering Our World',
   'Grade 1 Science strand review, and a capstone review closing out the full year of Grade 1 Science: students revisit rabbits, groundhogs, animal mimicry, chickens, decomposers, and constellations.',
   [('What helps a rabbit hop quickly?', ['its strong back legs']),
    ('What do decomposers break down?', ['dead plants and animals']),
    ('What is a constellation?', ['a group of stars that forms a pattern'])],
   [('What helps a rabbit hop quickly?', ['Its strong back legs', 'Its tail only', 'Its ears only', 'Its whiskers only'], 0),
    ('What do groundhogs do for most of the winter?', ['Hibernate', 'Migrate south', 'Stay awake and play', 'Build igloos'], 0),
    ('What is mimicry?', ['When an animal looks like something else to stay safe', 'When an animal changes colour to blend in', 'When an animal hides underground', 'When an animal migrates south'], 0),
    ('What is a baby chicken called?', ['A chick', 'A calf', 'A kit', 'A joey'], 0),
    ('What is a constellation?', ['A group of stars that forms a pattern', 'A single bright planet', 'A type of cloud', 'A kind of moon phase'], 0)]),
SS('Social Studies Review: A Year of Community, Culture, and Canada',
   'Grade 1 Social Studies strand review, and a capstone review closing out the full year of Grade 1 Social Studies: students revisit the CN Tower, Groundhog Day, bakers, ferries and ships, foods from around the world, and powwows.',
   [('In which city is the CN Tower located?', ['Toronto']),
    ('In what month is Groundhog Day celebrated?', ['February']),
    ('What is a powwow?', ['a gathering to celebrate Indigenous culture'])],
   [('In which city is the CN Tower located?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 0),
    ('In which month is Groundhog Day celebrated?', ['February', 'May', 'August', 'November'], 0),
    ('What does a baker make?', ['Bread, cakes, and other treats', 'Mail and packages', 'Medicine', 'Furniture'], 0),
    ('Where do ferries and ships travel?', ['Across lakes, rivers, and oceans', 'Only on roads', 'Only in the sky', 'Only underground'], 0),
    ('What is a powwow?', ['A gathering to celebrate Indigenous culture through dance and music', 'A type of weather event', 'A kind of building', 'A sports competition only'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_181_187)
    append_worksheet_days(1, g1_181_187)
