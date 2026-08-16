#!/usr/bin/env python3
"""Grade 1, Days 161-170 -- fourteenth batch, extending Grade 1 past Day 160
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days151_160.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-160 (dumped and
checked against data/grade1.json before writing): articles (a/an/the),
vowel teams ey and eigh, three-letter blends str/spr/scr, interjections,
silent letters gn and st, the suffix -able, note-taking, story climax,
word sorts for Language. Numbers to 600, skip counting by 100s, fractions
fifths, money up to ten dollars, sorting 3D shapes by number of faces,
two-digit plus one-digit addition, two-digit minus one-digit subtraction,
three-group Venn diagrams, and before/after/between number sense to 500
for Math. Moose, raccoons, snails, crabs, pulleys, comets and meteors,
minerals, camels, and fireflies for Science (all new animals/topics, not
reusing polar bears, elephants, giraffes, chameleons, jellyfish, or
earthworms from Days 151-160, and not reusing owls, bats, sharks, octopus,
turtles, whales, dolphins, penguins, ants, spiders, ladybugs, or honeybees
from earlier batches). The Great Lakes, the loon as a currency symbol, the
House of Commons, citizenship ceremonies, translators and interpreters,
National Flag of Canada Day, Canadian Olympians, food banks, and winter
road crews for Social Studies (new geography, government, helper, and
holiday topics, distinct from the many community-helper, government, and
holiday days already used in Days 1-160). Day 170 is a review day across
all four subjects, matching the end-of-batch pattern used in every prior
batch, with review titles worded distinctly from every earlier review
day's title. No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/quiz/worksheet text --
contractions and possessives are avoided entirely, matching this
project's convention (e.g. "Canadas" not "Canada's"), since this text
gets embedded directly into TypeScript string literals.
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


def _rebalance_answer_positions(days, seed=20260813):
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


g1_161_170 = [
day(161, [
L('Articles: Using A, An, and The',
  'Grade 1 Language strand: articles like a, an, and the come before nouns, with a used before consonant sounds, an before vowel sounds, and the used to point out a specific thing.',
  [('Which article goes before a word that starts with a vowel sound, a or an?', ['an', 'the word an']),
   ('Give an example of a sentence using the article the.', ['I see the dog', 'The sun is bright']),
   ('Why do we use articles before nouns?', ['to show we mean a noun', 'to introduce a noun'])],
  [('Which article goes before a word starting with a vowel sound, such as apple?', ['An', 'A', 'The', 'No article'], 0),
   ('Which article is used to point out one specific thing?', ['The', 'A', 'An', 'Some'], 0),
   ('Which sentence uses an article correctly?', ['I saw a cat', 'I saw cat', 'I saw the a cat', 'I saw an cat'], 0),
   ('Which article would come before the word egg?', ['An', 'A', 'The only', 'No article needed'], 0),
   ('Articles are small words that come right before a ___.', ['Noun', 'Verb', 'Adjective only', 'Punctuation mark'], 0)]),
M('Numbers to 600: Counting Beyond 500',
  'Grade 1 Math strand: students read, write, and count numbers beyond 500, up to 600.',
  [('What number comes right after 599?', ['600', 'six hundred']),
   ('What number comes right before 550?', ['549', 'five hundred forty nine']),
   ('Count by tens from 580 to 600.', ['580,590,600', '580 590 600'])],
  [('What number comes right after 599?', ['600', '599', '601', '598'], 0),
   ('Which number is between 520 and 540?', ['530', '510', '550', '560'], 0),
   ('What number comes right before 600?', ['599', '600', '598', '601'], 0),
   ('Which of these numbers is the largest?', ['599', '499', '399', '299'], 0),
   ('Counting beyond 500 helps us understand numbers up to ___.', ['600', '60', '6', '6000'], 0)]),
Sc('Moose: Canadas Large Forest Animal',
   'Grade 1 Science strand: the moose is a large mammal with wide antlers that lives in Canadian forests and near lakes, eating leaves, twigs, and water plants.',
   [('Where does a moose usually live?', ['forests near lakes', 'in the forest']),
    ('What does a moose have on its head?', ['antlers', 'wide antlers']),
    ('What does a moose eat?', ['leaves and twigs', 'water plants'])],
   [('Where does a moose usually live?', ['Forests near lakes', 'The desert', 'The ocean', 'A city street'], 0),
    ('What does a moose have on its head?', ['Wide antlers', 'A shell', 'Feathers', 'A long trunk'], 0),
    ('What does a moose mainly eat?', ['Leaves, twigs, and water plants', 'Fish', 'Other animals', 'Insects only'], 0),
    ('What kind of animal is a moose?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Moose are known for being one of the ___ animals in the forest.', ['Largest', 'Smallest', 'Fastest flying', 'Only underwater'], 0)]),
SS('The Great Lakes: Canadas Freshwater Giants',
   'Grade 1 Social Studies strand: the Great Lakes are a group of huge freshwater lakes on the border between Canada and the United States, important for drinking water, travel, and wildlife.',
   [('What are the Great Lakes?', ['huge freshwater lakes', 'a group of big lakes']),
    ('Between which two countries are the Great Lakes located?', ['Canada and the United States']),
    ('Name one reason the Great Lakes are important.', ['drinking water', 'travel and wildlife'])],
   [('What are the Great Lakes?', ['A group of huge freshwater lakes', 'A chain of mountains', 'A desert region', 'A set of small ponds'], 0),
    ('The Great Lakes lie on the border between Canada and which country?', ['The United States', 'Mexico', 'France', 'Australia'], 0),
    ('Why are the Great Lakes important to people?', ['They provide drinking water and travel routes', 'They have no importance', 'They are always frozen', 'They are used only for parking'], 0),
    ('What kind of water do the Great Lakes contain?', ['Freshwater', 'Salt water', 'No water', 'Ice only'], 0),
    ('The Great Lakes are home to many kinds of ___.', ['Fish and wildlife', 'Cars', 'Buildings', 'Airplanes'], 0)]),
]),
day(162, [
L('Vowel Teams: ey and eigh (Long A Sound)',
  'Grade 1 Language strand: the vowel teams ey and eigh can both make the long a sound, as in the words they and eight.',
  [('What sound do ey and eigh often make?', ['long a', 'the long a sound']),
   ('Give a word that uses ey to make the long a sound.', ['they', 'grey']),
   ('Give a word that uses eigh to make the long a sound.', ['eight', 'weigh'])],
  [('What sound do the vowel teams ey and eigh often make?', ['Long a', 'Short a', 'Long e', 'Short i'], 0),
   ('Which word uses ey to make the long a sound?', ['They', 'Tree', 'Toy', 'Cat'], 0),
   ('Which word uses eigh to make the long a sound?', ['Eight', 'Egg', 'Ear', 'End'], 0),
   ('Which of these words rhymes with eight?', ['Weight', 'Eat', 'Ant', 'Ink'], 0),
   ('Vowel teams like ey and eigh are made up of ___ letters working together.', ['Two or more', 'Only one', 'Five', 'Zero'], 0)]),
M('Skip Counting by 100s',
  'Grade 1 Math strand: students practise skip counting by 100s, counting 100, 200, 300, and so on, to build number sense with much larger numbers.',
  [('Count by 100s from 100 to 600.', ['100,200,300,400,500,600', '100 200 300 400 500 600']),
   ('What number comes after 400 when counting by 100s?', ['500', 'five hundred']),
   ('Is 350 a number you would say when counting by 100s starting at 100?', ['no', 'no it is not'])],
  [('What number comes right after 300 when counting by 100s?', ['400', '350', '310', '500'], 0),
   ('What number comes right after 500 when counting by 100s?', ['600', '550', '510', '700'], 0),
   ('Which of these numbers would you say when counting by 100s starting at 100?', ['500', '450', '150', '250'], 0),
   ('Skip counting by 100s means adding ___ each time.', ['100', '10', '50', '1'], 0),
   ('Which of these numbers would NOT be said when counting by 100s starting at 100?', ['250', '200', '300', '400'], 0)]),
Sc('Raccoons: Clever Nighttime Visitors',
   'Grade 1 Science strand: raccoons are clever nocturnal mammals with masked faces and ringed tails that use their paws to explore and find food at night.',
   [('When are raccoons usually active, day or night?', ['night', 'at night']),
    ('What does a raccoon use to explore and find food?', ['its paws', 'clever paws']),
    ('Describe what a raccoons face looks like.', ['it has a mask-like pattern', 'dark fur around the eyes'])],
   [('When are raccoons usually active?', ['At night', 'Only at noon', 'Only in the morning', 'Never'], 0),
    ('What do raccoons use to explore and grab food?', ['Their clever paws', 'Their wings', 'Their gills', 'Their tails only'], 0),
    ('What does a raccoons face often look like?', ['It has a dark mask-like pattern', 'It has feathers', 'It has no fur at all', 'It has a long beak'], 0),
    ('What kind of animal is a raccoon?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Animals that are mostly active at night are called ___.', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0)]),
SS('The Loon: A Canadian Symbol on Our Coins',
   'Grade 1 Social Studies strand: the loon is a Canadian bird known for its call on northern lakes, and its picture appears on the Canadian one dollar coin, often called the loonie.',
   [('What kind of animal is a loon?', ['a bird', 'a water bird']),
    ('On what Canadian coin does the loon appear?', ['the one dollar coin', 'the loonie']),
    ('Where does a loon usually live?', ['on northern lakes', 'on lakes'])],
   [('What kind of animal is a loon?', ['A bird', 'A fish', 'A mammal', 'An insect'], 0),
    ('On which Canadian coin does the loon appear?', ['The one dollar coin', 'The five cent coin', 'The ten cent coin', 'The twenty five cent coin'], 0),
    ('What is the one dollar coin often nicknamed because of the loon?', ['The loonie', 'The toonie', 'The nickel', 'The dime'], 0),
    ('Where does a loon usually live?', ['On northern lakes', 'In the desert', 'In the mountains', 'In the ocean only'], 0),
    ('The loon is an example of a Canadian animal used as a ___.', ['Symbol', 'Vehicle', 'Tool', 'Building material'], 0)]),
]),
day(163, [
L('Three-Letter Blends: str, spr, and scr',
  'Grade 1 Language strand: some words begin with three consonants blended together, such as str in string, spr in spring, and scr in scratch.',
  [('Give a word that starts with the str blend.', ['string', 'street']),
   ('Give a word that starts with the spr blend.', ['spring', 'sprout']),
   ('Give a word that starts with the scr blend.', ['scratch', 'scream'])],
  [('Which word starts with the str blend?', ['String', 'Sing', 'Ring', 'Tring'], 0),
   ('Which word starts with the spr blend?', ['Spring', 'Ping', 'Sing', 'Ring'], 0),
   ('Which word starts with the scr blend?', ['Scratch', 'Catch', 'Match', 'Latch'], 0),
   ('A three-letter blend has how many consonant sounds blended together?', ['3', '1', '2', '4'], 0),
   ('Which of these words has a three-letter blend at the start?', ['Spray', 'Play', 'Say', 'Day'], 0)]),
M('Fractions: Fifths of a Whole',
  'Grade 1 Math strand: when a whole is divided into five equal parts, each part is called a fifth, written as one out of five equal pieces.',
  [('What is each equal part called when a whole is split into five pieces?', ['a fifth', 'one fifth']),
   ('How many equal parts make a whole when it is divided into fifths?', ['5', 'five']),
   ('If you eat one fifth of a pizza, how many equal pieces are left?', ['4', 'four'])],
  [('What is each equal part called when a whole is divided into five pieces?', ['A fifth', 'A half', 'A third', 'A quarter'], 0),
   ('How many equal parts make up a whole divided into fifths?', ['5', '4', '3', '2'], 0),
   ('If a pizza is cut into fifths, how many pieces does it have in total?', ['5', '4', '3', '2'], 0),
   ('Which fraction shows one out of five equal parts?', ['One fifth', 'One half', 'One third', 'One quarter'], 0),
   ('For parts to be called fifths, they must be ___.', ['Equal in size', 'Different sizes', 'Only two pieces', 'Not connected'], 0)]),
Sc('Snails: Slow Movers with Shells',
   'Grade 1 Science strand: snails are small animals with soft bodies and hard shells on their backs that move slowly using a single muscular foot.',
   [('What does a snail carry on its back?', ['a shell', 'a hard shell']),
    ('How does a snail move?', ['using its foot', 'slowly using a muscular foot']),
    ('Why is a snails shell helpful?', ['it protects its soft body', 'keeps it safe'])],
   [('What does a snail carry on its back?', ['A hard shell', 'A pair of wings', 'A set of feathers', 'A long tail'], 0),
    ('How does a snail move from place to place?', ['By using a single muscular foot', 'By flying', 'By running on four legs', 'By swimming with fins'], 0),
    ('Why is a snails shell important?', ['It protects its soft body', 'It helps it fly', 'It helps it breathe underwater only', 'It has no real purpose'], 0),
    ('What kind of body does a snail have under its shell?', ['A soft body', 'A hard body', 'A furry body', 'A feathered body'], 0),
    ('Snails are known for moving very ___.', ['Slowly', 'Quickly', 'Loudly', 'Underground only'], 0)]),
SS('The House of Commons: Where Our Laws Are Debated',
   'Grade 1 Social Studies strand: the House of Commons is a part of the Canadian government where elected members meet in Ottawa to discuss and vote on new laws.',
   [('What is the House of Commons?', ['a place where laws are discussed', 'part of Canadas government']),
    ('In what city is the House of Commons located?', ['Ottawa']),
    ('What do the elected members do in the House of Commons?', ['discuss and vote on laws', 'debate new laws'])],
   [('What is the House of Commons?', ['A place where elected members discuss and vote on laws', 'A shopping mall', 'A hospital', 'A school'], 0),
    ('In which city is the House of Commons located?', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 0),
    ('What do members of the House of Commons do?', ['Discuss and vote on new laws', 'Sell groceries', 'Build houses', 'Teach classes'], 0),
    ('The House of Commons is part of what larger system?', ['The Canadian government', 'A sports league', 'A school board', 'A private company'], 0),
    ('People who are elected to the House of Commons are called Members of ___.', ['Parliament', 'The Public', 'The Community', 'The Committee'], 0)]),
]),
day(164, [
L('Interjections: Showing Strong Feelings with Wow and Hooray',
  'Grade 1 Language strand: an interjection is a short word or phrase, like Wow or Hooray, that shows a burst of strong feeling and is often followed by an exclamation mark.',
  [('What is an interjection used for?', ['to show strong feeling', 'to express excitement']),
   ('Give an example of an interjection.', ['Wow', 'Hooray']),
   ('What punctuation mark often follows an interjection?', ['an exclamation mark', '!'])],
  [('What does an interjection usually show?', ['A burst of strong feeling', 'A calm fact', 'A question', 'A list of items'], 0),
   ('Which of these words is an interjection?', ['Hooray', 'Table', 'Walking', 'Blue'], 0),
   ('Which punctuation mark often follows an interjection?', ['An exclamation mark', 'A comma', 'A question mark', 'A period only'], 0),
   ('Which sentence uses an interjection correctly?', ['Wow, that is amazing!', 'That wow is amazing', 'Amazing wow that is', 'Is wow that amazing'], 0),
   ('Interjections are usually ___ words placed at the start of a sentence.', ['Short, feeling-filled', 'Long and boring', 'Silent', 'Numeric'], 0)]),
M('Money: Making Amounts Up to Ten Dollars',
  'Grade 1 Math strand: students combine coins and bills to make amounts of money up to ten dollars.',
  [('How many toonies make ten dollars?', ['5', 'five toonies']),
   ('Name a way to make ten dollars using bills.', ['a ten dollar bill', 'two five dollar bills']),
   ('If you have one five dollar bill and one toonie and one loonie, how much money do you have?', ['8 dollars', 'eight dollars'])],
  [('How many toonies would you need to make ten dollars?', ['5', '4', '3', '2'], 0),
   ('Which combination makes exactly ten dollars?', ['Two five dollar bills', 'One five dollar bill', 'Two loonies', 'Three toonies'], 0),
   ('If you have one five dollar bill and two toonies, how much money do you have?', ['9 dollars', '8 dollars', '7 dollars', '10 dollars'], 0),
   ('Which single bill is worth ten dollars?', ['A ten dollar bill', 'A five dollar bill', 'A one dollar bill', 'A twenty dollar bill'], 0),
   ('Practising with coins and bills up to ten dollars helps us understand ___.', ['Even larger amounts of money', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('Crabs: Sideways Walkers of the Shore',
   'Grade 1 Science strand: crabs are small sea animals with hard shells and pincers that usually walk sideways along beaches and ocean floors.',
   [('How do crabs usually walk?', ['sideways', 'they walk sideways']),
    ('What do crabs use to grab food or defend themselves?', ['pincers', 'claws']),
    ('Where might you find a crab?', ['on a beach', 'the ocean floor'])],
   [('How do crabs usually walk?', ['Sideways', 'Backwards only', 'Straight forward only', 'They do not walk'], 0),
    ('What do crabs use to grab food or defend themselves?', ['Pincers', 'Wings', 'Fins only', 'A trunk'], 0),
    ('Where might you commonly find a crab?', ['On a beach or ocean floor', 'In a desert', 'In a treetop', 'In the sky'], 0),
    ('What covers a crabs body to protect it?', ['A hard shell', 'Soft fur', 'Feathers', 'Scales like a fish'], 0),
    ('Crabs belong to a group of animals with hard outer shells called ___.', ['Crustaceans', 'Mammals', 'Birds', 'Amphibians'], 0)]),
SS('Citizenship Ceremony: Becoming a Canadian Citizen',
   'Grade 1 Social Studies strand: a citizenship ceremony is a special event where newcomers promise to follow Canadian laws and officially become Canadian citizens.',
   [('What happens at a citizenship ceremony?', ['newcomers become citizens', 'people officially become Canadian citizens']),
    ('What do new citizens promise to do at the ceremony?', ['follow Canadian laws', 'follow the rules of Canada']),
    ('Why might a citizenship ceremony be an exciting day for a family?', ['it is a special new beginning', 'they officially belong to Canada'])],
   [('What happens at a citizenship ceremony?', ['Newcomers officially become Canadian citizens', 'People go grocery shopping', 'Students take a math test', 'Workers build a road'], 0),
    ('What do new citizens promise at a citizenship ceremony?', ['To follow Canadian laws', 'To never leave their house', 'To stop speaking their first language', 'To move to another country'], 0),
    ('Why might a citizenship ceremony be an important day for a family?', ['It marks officially belonging to Canada', 'It has no meaning at all', 'It only happens to visitors', 'It is the same as a birthday party'], 0),
    ('Who usually attends a citizenship ceremony to become a citizen?', ['Newcomers to Canada', 'Only babies born in Canada', 'Only tourists', 'Only government workers'], 0),
    ('Becoming a citizen is one way people show they are part of the Canadian ___.', ['Community', 'Weather', 'Geography', 'Alphabet'], 0)]),
]),
day(165, [
L('Silent Letters: gn and st',
  'Grade 1 Language strand: some words have silent letters that are not pronounced, such as the silent g in sign and the silent t in listen.',
  [('What letter is silent in the word sign?', ['g', 'the g']),
   ('What letter is silent in the word listen?', ['t', 'the t']),
   ('Give another word with a silent letter.', ['gnome', 'castle'])],
  [('Which letter is silent in the word sign?', ['G', 'S', 'I', 'N'], 0),
   ('Which letter is silent in the word listen?', ['T', 'L', 'I', 'S'], 0),
   ('Which of these words has a silent letter?', ['Gnome', 'Game', 'Goat', 'Gum'], 0),
   ('A silent letter is a letter that ___.', ['Is written but not pronounced', 'Is always the first letter', 'Is always a vowel', 'Makes a loud sound'], 0),
   ('Which of these words has a silent t?', ['Castle', 'Cat', 'Tent', 'Table'], 0)]),
M('Geometry: Sorting 3D Shapes by Number of Faces',
  'Grade 1 Math strand: 3D shapes can be sorted by how many flat faces they have, such as a cube with six faces or a cone with one flat face.',
  [('How many faces does a cube have?', ['6', 'six']),
   ('How many flat faces does a cone have?', ['1', 'one']),
   ('Name a 3D shape with no flat faces.', ['sphere', 'ball'])],
  [('How many faces does a cube have?', ['6', '4', '5', '8'], 0),
   ('How many flat faces does a cone have?', ['1', '0', '2', '3'], 0),
   ('Which 3D shape has no flat faces at all?', ['A sphere', 'A cube', 'A cone', 'A cylinder'], 0),
   ('Sorting 3D shapes by faces is an example of ___.', ['Classifying shapes', 'Measuring length', 'Telling time', 'Counting money'], 0),
   ('Which of these shapes has two flat circular faces?', ['A cylinder', 'A cube', 'A sphere', 'A cone'], 0)]),
Sc('Simple Machines: Pulleys and Lifting Loads',
   'Grade 1 Science strand: a pulley is a simple machine with a wheel and a rope that helps people lift heavy loads more easily by pulling down instead of straight up.',
   [('What is a pulley?', ['a simple machine with a wheel and rope', 'a machine that helps lift loads']),
    ('What does a pulley help people do?', ['lift heavy loads', 'move things up more easily']),
    ('Name a place you might see a pulley used.', ['a flagpole', 'a crane'])],
   [('What is a pulley?', ['A simple machine with a wheel and rope', 'A type of clock', 'A kind of shape', 'A musical instrument'], 0),
    ('What does a pulley help people do?', ['Lift heavy loads more easily', 'Tell time', 'Cook food', 'Measure temperature'], 0),
    ('Which of these commonly uses a pulley?', ['A flagpole', 'A thermometer', 'A calendar', 'A clock'], 0),
    ('A pulley is an example of what kind of machine?', ['A simple machine', 'A computer', 'An engine', 'A robot'], 0),
    ('Using a pulley can make lifting a heavy object feel ___.', ['Easier', 'Impossible', 'Much heavier', 'Slower and harder'], 0)]),
SS('Translators and Interpreters: Helping People Communicate',
   'Grade 1 Social Studies strand: translators and interpreters help people who speak different languages understand each other by changing words from one language into another.',
   [('What do translators and interpreters help people do?', ['understand each other', 'communicate across languages']),
    ('Why might a translator be helpful for a newcomer family?', ['helps them understand a new language', 'helps them communicate']),
    ('Give an example of a place a translator might help.', ['a hospital', 'a school'])],
   [('What do translators and interpreters help people do?', ['Communicate across different languages', 'Cook meals', 'Fix cars', 'Deliver mail'], 0),
    ('Why might a translator be helpful for a newcomer family?', ['It helps them understand a new language', 'It has no real purpose', 'It replaces the need for school', 'It only helps with math'], 0),
    ('Where might a translator help people communicate?', ['At a hospital or school', 'Only in outer space', 'Only underwater', 'Nowhere at all'], 0),
    ('A translator changes words from one ___ into another.', ['Language', 'Colour', 'Shape', 'Season'], 0),
    ('Translators help make communities more ___.', ['Welcoming and connected', 'Confusing', 'Divided', 'Silent'], 0)]),
]),
day(166, [
L('Suffixes: Adding -able to Describe What Can Be Done',
  'Grade 1 Language strand: adding the suffix -able to a word can create an adjective meaning able to be done, such as changing wash into washable or read into readable.',
  [('What does adding -able to wash make?', ['washable', 'able to be washed']),
   ('What does adding -able to read make?', ['readable', 'able to be read']),
   ('What does the suffix -able usually mean?', ['able to be done', 'capable of'])],
  [('What does adding -able to wash make?', ['Washable', 'Washed', 'Washing', 'Washer'], 0),
   ('What does the suffix -able usually mean?', ['Able to be done', 'Not able to be done', 'Done many times', 'Never done'], 0),
   ('Which word means able to be read?', ['Readable', 'Reader', 'Reading', 'Read only'], 0),
   ('Which word is formed by adding -able to enjoy?', ['Enjoyable', 'Enjoyed', 'Enjoying', 'Enjoyer'], 0),
   ('Adding -able to a word usually turns it into an ___.', ['Adjective', 'Verb', 'Pronoun', 'Preposition'], 0)]),
M('Addition: Adding a Two-Digit Number and a One-Digit Number',
  'Grade 1 Math strand: students practise adding a two-digit number and a one-digit number by combining the ones first and then adding the tens.',
  [('What is 23 plus 4?', ['27', 'twenty seven']),
   ('What is 15 plus 3?', ['18', 'eighteen']),
   ('When adding a two-digit and a one-digit number, which digits do you add first?', ['the ones', 'the ones digits'])],
  [('What is 23 plus 4?', ['27', '26', '28', '25'], 0),
   ('What is 15 plus 3?', ['18', '17', '19', '16'], 0),
   ('When adding a two-digit number and a one-digit number, which digits should you add first?', ['The ones digits', 'The tens digits', 'Neither digit', 'Both at random'], 0),
   ('What is 42 plus 6?', ['48', '47', '49', '46'], 0),
   ('Adding a two-digit number and a one-digit number usually changes the ___ digit.', ['Ones', 'Tens only', 'Hundreds', 'No digit'], 0)]),
Sc('Comets and Meteors: Visitors From Space',
   'Grade 1 Science strand: comets are balls of ice and dust that travel through space, while meteors are small pieces of rock that burn up as bright streaks when they enter Earths atmosphere.',
   [('What is a comet made of?', ['ice and dust', 'ice and dust travelling through space']),
    ('What is a meteor?', ['a small piece of rock burning up', 'a streak of light in the sky']),
    ('Where do meteors burn up?', ['Earths atmosphere', 'the sky'])],
   [('What is a comet mostly made of?', ['Ice and dust', 'Only metal', 'Only water', 'Only sand'], 0),
    ('What is a meteor?', ['A small piece of rock that burns up in the sky', 'A type of planet', 'A kind of moon', 'A large star'], 0),
    ('Where does a meteor burn up as a bright streak?', ['In Earths atmosphere', 'On the ocean floor', 'Underground', 'Inside a volcano'], 0),
    ('Comets travel through what part of space?', ['Outer space near the sun', 'Inside the ocean', 'Under the ground', 'Inside a cloud'], 0),
    ('A meteor that we see burning up in the night sky is sometimes called a ___.', ['Shooting star', 'Black hole', 'Galaxy', 'Nebula'], 0)]),
SS('National Flag of Canada Day: Celebrating Our Flag',
   'Grade 1 Social Studies strand: National Flag of Canada Day is celebrated every February to honour the day Canada adopted its red and white maple leaf flag.',
   [('What month is National Flag of Canada Day celebrated?', ['February']),
    ('What does National Flag of Canada Day honour?', ['the day Canada adopted its flag', 'the Canadian flag']),
    ('What is on the Canadian flag?', ['a maple leaf', 'a red maple leaf'])],
   [('In what month is National Flag of Canada Day celebrated?', ['February', 'June', 'October', 'December'], 0),
    ('What does National Flag of Canada Day honour?', ['The day Canada adopted its flag', 'A famous hockey game', 'A new school opening', 'A weather event'], 0),
    ('What symbol is at the centre of the Canadian flag?', ['A maple leaf', 'A beaver', 'A loon', 'A star'], 0),
    ('What colours are on the Canadian flag?', ['Red and white', 'Blue and yellow', 'Green and black', 'Purple and orange'], 0),
    ('Celebrating a flag day helps people feel proud of their ___.', ['Country', 'School only', 'Neighbourhood only', 'Family only'], 0)]),
]),
day(167, [
L('Note-Taking: Jotting Down Important Ideas',
  'Grade 1 Language strand: note-taking means writing down short important words or ideas while listening or reading, to help remember key information later.',
  [('What is note-taking?', ['writing down important ideas', 'jotting down key words']),
   ('Why might a student take notes during a lesson?', ['to remember important ideas', 'helps them remember later']),
   ('Should notes be written in full long sentences or short important words?', ['short important words', 'short words'])],
  [('What is note-taking?', ['Writing down short important ideas', 'Drawing a picture only', 'Singing a song', 'Erasing information'], 0),
   ('Why might a student take notes while listening to a story?', ['To remember important ideas later', 'To make the story longer', 'To avoid listening', 'To confuse themselves'], 0),
   ('Notes are usually written using ___.', ['Short important words', 'Long complete paragraphs', 'Only pictures', 'Only numbers'], 0),
   ('Which of these is a good example of a note?', ['Bear eats fish', 'Once upon a time there was a bear who loved to eat many different kinds of fish', 'A poem about bears', 'A song about fish'], 0),
   ('Taking notes can help us stay ___ during a lesson.', ['Organized and focused', 'Distracted', 'Confused', 'Bored'], 0)]),
M('Subtraction: Subtracting a One-Digit Number from a Two-Digit Number',
  'Grade 1 Math strand: students practise subtracting a one-digit number from a two-digit number by taking away from the ones place first.',
  [('What is 27 minus 4?', ['23', 'twenty three']),
   ('What is 18 minus 5?', ['13', 'thirteen']),
   ('When subtracting a one-digit number from a two-digit number, which digits do you subtract first?', ['the ones', 'the ones digits'])],
  [('What is 27 minus 4?', ['23', '22', '24', '21'], 0),
   ('What is 18 minus 5?', ['13', '12', '14', '11'], 0),
   ('When subtracting a one-digit number from a two-digit number, which digits should you subtract first?', ['The ones digits', 'The tens digits', 'Neither digit', 'Both at random'], 0),
   ('What is 39 minus 6?', ['33', '32', '34', '35'], 0),
   ('Subtracting a one-digit number from a two-digit number usually changes the ___ digit.', ['Ones', 'Tens only', 'Hundreds', 'No digit'], 0)]),
Sc('Minerals: What Rocks Are Made Of',
   'Grade 1 Science strand: minerals are natural solid materials found in the earth that combine together to form rocks, each with its own colour, hardness, and shine.',
   [('What are minerals?', ['natural solid materials', 'materials that form rocks']),
    ('What do minerals combine together to form?', ['rocks']),
    ('Name one way minerals can be different from each other.', ['colour', 'hardness'])],
   [('What are minerals?', ['Natural solid materials found in the earth', 'A type of liquid', 'A kind of gas', 'A man-made plastic'], 0),
    ('What do minerals combine together to form?', ['Rocks', 'Clouds', 'Rivers', 'Trees'], 0),
    ('Which of these is a way minerals can differ from each other?', ['Their colour and hardness', 'Their favourite food', 'Their age in years', 'Their sound'], 0),
    ('Where are minerals naturally found?', ['In the earth', 'In the clouds', 'In outer space only', 'In the wind'], 0),
    ('Studying minerals helps scientists understand what rocks are made of and how they ___.', ['Form', 'Sing', 'Fly', 'Swim'], 0)]),
SS('Canadian Olympians: Representing Canada in Sports',
   'Grade 1 Social Studies strand: Canadian Olympians are athletes who train hard and compete for Canada at the Olympic Games, representing their country in sports from around the world.',
   [('What is a Canadian Olympian?', ['an athlete who competes for Canada', 'a Canadian athlete at the Olympics']),
    ('What do Olympians do before competing?', ['train hard']),
    ('Why is it exciting when a Canadian wins at the Olympics?', ['represents Canada', 'shows what Canadians can achieve'])],
   [('What is a Canadian Olympian?', ['An athlete who competes for Canada at the Olympics', 'A type of coin', 'A government leader', 'A school subject'], 0),
    ('What do Olympians usually do before competing?', ['Train hard for many years', 'Skip practising', 'Only watch television', 'Avoid exercise'], 0),
    ('Why might it be exciting when a Canadian wins an Olympic medal?', ['They represent Canada on the world stage', 'It has no meaning at all', 'Only Canadians can watch the Olympics', 'The Olympics happen every day'], 0),
    ('The Olympic Games bring together athletes from ___.', ['Around the world', 'Only Canada', 'Only one city', 'Only one school'], 0),
    ('Canadian Olympians help make other Canadians feel ___ of their country.', ['Proud', 'Ashamed', 'Bored', 'Confused'], 0)]),
]),
day(168, [
L('Story Climax: The Most Exciting Part of a Story',
  'Grade 1 Language strand: the climax of a story is the most exciting or important moment, often where the main problem reaches its highest point before being solved.',
  [('What is the climax of a story?', ['the most exciting part', 'the most important moment']),
   ('What often happens right after the climax?', ['the problem gets solved', 'the story starts to end']),
   ('Why is the climax an important part of a story?', ['it is the most exciting moment', 'it grabs the readers attention'])],
  [('What is the climax of a story?', ['The most exciting or important moment', 'The very first sentence', 'The title of the book', 'The name of the author'], 0),
   ('What often happens right after the climax of a story?', ['The problem begins to be solved', 'The story just begins', 'Nothing happens at all', 'A new book starts'], 0),
   ('Why is the climax an important part of a story?', ['It is the most exciting moment for readers', 'It is always the shortest part', 'It has no purpose', 'It happens before the story starts'], 0),
   ('Which of these might happen at the climax of an adventure story?', ['The hero faces the biggest challenge', 'The book cover is designed', 'The author is born', 'The library opens'], 0),
   ('The climax usually comes ___ in a story.', ['Near the highest point of excitement', 'At the very beginning only', 'Before the story starts', 'On the back cover'], 0)]),
M('Data: Sorting Objects into a Venn Diagram with Three Groups',
  'Grade 1 Math strand: a Venn diagram can use three overlapping circles to sort objects that might belong to one, two, or all three groups at once.',
  [('How many circles does a three-group Venn diagram have?', ['3', 'three']),
   ('What does it mean if an object is placed where two circles overlap?', ['it belongs to both groups', 'fits both categories']),
   ('Why might we use three circles instead of two?', ['to sort into more groups', 'compare more categories at once'])],
  [('How many circles are used in a three-group Venn diagram?', ['3', '1', '2', '4'], 0),
   ('What does it mean when an object is placed where two circles overlap?', ['It belongs to both groups', 'It belongs to no group', 'It is not allowed in the diagram', 'It must be removed'], 0),
   ('Why might someone use a three-circle Venn diagram instead of a two-circle one?', ['To sort objects into more groups at once', 'To make the diagram harder to read', 'To remove information', 'To avoid comparing anything'], 0),
   ('An object placed in the very middle of three overlapping circles belongs to ___.', ['All three groups', 'No groups', 'Only one group', 'A group outside the diagram'], 0),
   ('Venn diagrams help us visually compare and ___ objects or ideas.', ['Sort', 'Hide', 'Erase', 'Ignore'], 0)]),
Sc('Camels: Animals Built for the Desert',
   'Grade 1 Science strand: camels are large mammals with humps that store fat, helping them survive for long periods without food or water in hot, dry desert habitats.',
   [('What do camels have on their backs?', ['humps', 'one or two humps']),
    ('What is stored inside a camels hump?', ['fat']),
    ('Why are camels well suited to desert life?', ['can survive without food or water for a long time', 'store fat for energy'])],
   [('What do camels have on their backs?', ['Humps', 'Wings', 'Shells', 'Fins'], 0),
    ('What is stored inside a camels hump?', ['Fat', 'Water only', 'Sand', 'Bones'], 0),
    ('Why are camels well suited to desert life?', ['They can survive long periods without food or water', 'They need water every hour', 'They cannot handle heat at all', 'They live only underwater'], 0),
    ('What kind of animal is a camel?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Camels are often called ships of the desert because they help people ___ across sandy land.', ['Travel', 'Swim', 'Fly', 'Dig tunnels'], 0)]),
SS('Our Local Food Bank: Helping Neighbours in Need',
   'Grade 1 Social Studies strand: a food bank is a place in our community that collects and gives out food to families who need extra help getting enough to eat.',
   [('What is a food bank?', ['a place that gives out food', 'a place that helps families get food']),
    ('Who might a food bank help?', ['families who need extra help', 'neighbours in need']),
    ('How can people support a food bank?', ['donate food', 'give food or volunteer'])],
   [('What is a food bank?', ['A place that collects and gives out food to families in need', 'A place to keep money safe', 'A store that only sells toys', 'A place to watch movies'], 0),
    ('Who does a food bank help?', ['Families who need extra help getting food', 'Only wealthy families', 'Only pets', 'Only tourists'], 0),
    ('How can community members support a food bank?', ['By donating food or volunteering', 'By ignoring it completely', 'By taking food without giving any back', 'By closing it down'], 0),
    ('A food bank is an example of a place that shows ___ in a community.', ['Kindness and caring', 'Unfairness', 'Carelessness', 'Competition'], 0),
    ('Food banks help make sure that ___ have enough to eat.', ['More families', 'No families', 'Only one family', 'Only animals'], 0)]),
]),
day(169, [
L('Word Sorts: Grouping Words by Sound or Spelling',
  'Grade 1 Language strand: a word sort is an activity where students group words into categories based on shared sounds or spelling patterns, helping them notice patterns in language.',
  [('What is a word sort?', ['grouping words by sound or spelling', 'an activity to group words']),
   ('Give an example of two words that could be sorted into the same group.', ['cat and hat', 'run and fun']),
   ('Why are word sorts a helpful activity?', ['helps notice spelling patterns', 'helps us see patterns in words'])],
  [('What is a word sort?', ['An activity that groups words by sound or spelling', 'A way to erase words', 'A type of math problem', 'A drawing activity'], 0),
   ('Which pair of words could be sorted into the same rhyming group?', ['Cat and hat', 'Cat and dog', 'Cat and sun', 'Cat and pen'], 0),
   ('Why might a teacher use word sorts in class?', ['To help students notice spelling patterns', 'To make spelling harder', 'To remove all patterns', 'To replace reading time'], 0),
   ('Which of these words could be grouped with the -ing family?', ['Running', 'Cat', 'Sun', 'Blue'], 0),
   ('Word sorts help students become more aware of ___ in words.', ['Patterns', 'Colours', 'Numbers', 'Shapes'], 0)]),
M('Number Sense: Before, After, and Between to 500',
  'Grade 1 Math strand: students practise identifying which numbers come before, after, or between other numbers up to 500.',
  [('What number comes right before 300?', ['299', 'two hundred ninety nine']),
   ('What number comes right after 249?', ['250', 'two hundred fifty']),
   ('What number comes between 399 and 401?', ['400', 'four hundred'])],
  [('What number comes right before 300?', ['299', '301', '298', '310'], 0),
   ('What number comes right after 249?', ['250', '248', '251', '260'], 0),
   ('What number comes between 399 and 401?', ['400', '398', '402', '410'], 0),
   ('Which number comes right before 500?', ['499', '501', '498', '510'], 0),
   ('Knowing which numbers come before and after helps us understand ___.', ['Number order', 'Colours', 'Shapes', 'Weather'], 0)]),
Sc('Fireflies: Insects That Glow in the Dark',
   'Grade 1 Science strand: fireflies are small flying insects that make their own light using a special part of their body, glowing on warm summer nights to attract other fireflies.',
   [('What special thing can fireflies do?', ['make their own light', 'glow in the dark']),
    ('When do fireflies usually glow?', ['on warm summer nights', 'at night']),
    ('Why do fireflies glow?', ['to attract other fireflies', 'to communicate with each other'])],
   [('What special ability do fireflies have?', ['Making their own light', 'Breathing underwater', 'Growing very tall', 'Changing colour like a chameleon'], 0),
    ('When do fireflies usually glow?', ['On warm summer nights', 'Only during winter mornings', 'Only underwater', 'Only in the desert at noon'], 0),
    ('Why do fireflies glow?', ['To attract other fireflies', 'To scare away the sun', 'To stay warm', 'To breathe better'], 0),
    ('What kind of animal is a firefly?', ['An insect', 'A mammal', 'A reptile', 'A fish'], 0),
    ('A fireflies glow is created by a special part of its ___.', ['Body', 'Wing colour only', 'Shell', 'Fur'], 0)]),
SS('Snow Removal and Winter Road Crews: Keeping Us Safe in Winter',
   'Grade 1 Social Studies strand: winter road crews use plows and salt to clear snow and ice from roads and sidewalks, helping people travel safely during the cold months.',
   [('What do winter road crews use to clear roads?', ['plows and salt', 'plows']),
    ('Why is it important to clear snow and ice from roads?', ['to keep people safe when travelling', 'helps people travel safely']),
    ('When do we mostly see winter road crews working?', ['during the cold months', 'in winter'])],
   [('What do winter road crews use to clear roads?', ['Plows and salt', 'Paint and brushes', 'Shovels only for sidewalks', 'Nothing at all'], 0),
    ('Why is it important to clear snow and ice from roads?', ['To help people travel safely', 'To make roads more slippery', 'To block traffic completely', 'To grow more snow'], 0),
    ('When do winter road crews do most of their work?', ['During the cold winter months', 'Only in summer', 'Only in spring', 'Only in autumn'], 0),
    ('What might happen if roads were never cleared of snow and ice?', ['Travel would become unsafe', 'Nothing would change', 'Roads would become warmer', 'Cars would travel faster'], 0),
    ('Winter road crews are an example of community workers who help keep us ___.', ['Safe', 'Confused', 'Cold', 'Lost'], 0)]),
]),
day(170, [
L('Language Review: Word Parts, Sentence Craft, and Story Elements',
  'Grade 1 Language strand review: students revisit articles, the vowel teams ey and eigh, three-letter blends, interjections, silent letters gn and st, the suffix -able, note-taking, story climax, and word sorts.',
  [('Which article goes before a word starting with a vowel sound, such as apple?', ['an']),
   ('What sound do ey and eigh often make?', ['long a']),
   ('What is the climax of a story?', ['the most exciting part'])],
  [('Which article goes before a word starting with a vowel sound, such as apple?', ['An', 'A', 'The', 'No article'], 0),
   ('Which word starts with the str blend?', ['String', 'Sing', 'Ring', 'Tring'], 0),
   ('What does an interjection usually show?', ['A burst of strong feeling', 'A calm fact', 'A question', 'A list of items'], 0),
   ('Which letter is silent in the word sign?', ['G', 'S', 'I', 'N'], 0),
   ('What is note-taking?', ['Writing down short important ideas', 'Drawing a picture only', 'Singing a song', 'Erasing information'], 0)]),
M('Math Review: Larger Numbers, Shapes, and Operations',
  'Grade 1 Math strand review: students revisit numbers to 600, skip counting by 100s, fifths, money up to ten dollars, sorting 3D shapes by faces, two-digit plus one-digit addition and subtraction, three-group Venn diagrams, and number order to 500.',
  [('What number comes right after 599?', ['600']),
   ('How many faces does a cube have?', ['6']),
   ('What is 23 plus 4?', ['27'])],
  [('What number comes right after 599?', ['600', '599', '601', '598'], 0),
   ('What number comes right after 300 when counting by 100s?', ['400', '350', '310', '500'], 0),
   ('What is each equal part called when a whole is divided into five pieces?', ['A fifth', 'A half', 'A third', 'A quarter'], 0),
   ('How many faces does a cube have?', ['6', '4', '5', '8'], 0),
   ('What is 27 minus 4?', ['23', '22', '24', '21'], 0)]),
Sc('Science Review: New Animals, Earth Materials, and Simple Machines',
   'Grade 1 Science strand review: students revisit moose, raccoons, snails, crabs, pulleys, comets and meteors, minerals, camels, and fireflies.',
   [('Where does a moose usually live?', ['forests near lakes']),
    ('What is a pulley?', ['a simple machine with a wheel and rope']),
    ('Why do fireflies glow?', ['to attract other fireflies'])],
   [('Where does a moose usually live?', ['Forests near lakes', 'The desert', 'The ocean', 'A city street'], 0),
    ('What do raccoons use to explore and grab food?', ['Their clever paws', 'Their wings', 'Their gills', 'Their tails only'], 0),
    ('What is a pulley?', ['A simple machine with a wheel and rope', 'A type of clock', 'A kind of shape', 'A musical instrument'], 0),
    ('What is a meteor?', ['A small piece of rock that burns up in the sky', 'A type of planet', 'A kind of moon', 'A large star'], 0),
    ('Why are camels well suited to desert life?', ['They can survive long periods without food or water', 'They need water every hour', 'They cannot handle heat at all', 'They live only underwater'], 0)]),
SS('Social Studies Review: Symbols, Leaders, and Newcomers',
   'Grade 1 Social Studies strand review: students revisit the Great Lakes, the loon, the House of Commons, citizenship ceremonies, translators, National Flag of Canada Day, Canadian Olympians, food banks, and winter road crews.',
   [('What are the Great Lakes?', ['huge freshwater lakes']),
    ('On which Canadian coin does the loon appear?', ['the one dollar coin']),
    ('What happens at a citizenship ceremony?', ['newcomers become citizens'])],
   [('What are the Great Lakes?', ['A group of huge freshwater lakes', 'A chain of mountains', 'A desert region', 'A set of small ponds'], 0),
    ('On which Canadian coin does the loon appear?', ['The one dollar coin', 'The five cent coin', 'The ten cent coin', 'The twenty five cent coin'], 0),
    ('What happens at a citizenship ceremony?', ['Newcomers officially become Canadian citizens', 'People go grocery shopping', 'Students take a math test', 'Workers build a road'], 0),
    ('In what month is National Flag of Canada Day celebrated?', ['February', 'June', 'October', 'December'], 0),
    ('What is a food bank?', ['A place that collects and gives out food to families in need', 'A place to keep money safe', 'A store that only sells toys', 'A place to watch movies'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_161_170)
    append_worksheet_days(1, g1_161_170)
