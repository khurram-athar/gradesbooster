#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 131-140 -- eleventh batch, extending Grade 0
past Day 130. Self-contained script (does NOT use gen_curriculum.py's
sub()/day()/append_to(), since those do not support a worksheet field)
modeled exactly on gen_grade0_days121_130.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-130 (dumped
and checked against data/grade0.json before writing): word families -ack,
-ock, -ick; adding -y; comparative adjectives; onomatopoeia; nonfiction
text features (table of contents/headings); categorizing words; author's
purpose for Language. Missing addends, measuring with a ruler in cm, skip
counting by 4s, fractions/thirds, making a target amount with coins,
perimeter, trapezoid/rhombus, estimating weight, skip counting backwards
by 10s for Math. Animal diets (herbivore/carnivore/omnivore), fish
gills/fins, butterflies vs moths, ocean tides, sense of balance,
constellations, losing baby teeth, where tap water comes from, animal
mimicry for Science. National anthem, provincial premier, school
custodian, National Indigenous Peoples Day, local newspaper, then-and-now
communication, conservation officers, voting, snow plow drivers for
Social Studies. Day 140 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior batch. No embedded
ASCII double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely, matching this project's convention (e.g. "Canadas" not
"Canada's"), since this text gets embedded directly into TypeScript
string literals.
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


def _rebalance_answer_positions(days, seed=20260802):
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


g0_131_140 = [
day(131, [
L('Word Families: -ack Words',
  'Kindergarten Language strand: the -ack word family shares the same ending sound, as in back, pack, sack, and track.',
  [('Name a word that rhymes with back.', ['pack', 'sack', 'track']),
   ('What ending sound do pack and sack share?', ['ack', 'the ack sound']),
   ('Is snack part of the -ack family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ack family?', ['Sun', 'Pack', 'Bed', 'Cup'], 0),
   ('Which word rhymes with sack?', ['Sit', 'Back', 'Sad', 'Sob'], 1),
   ('Which word does NOT belong to the -ack family?', ['Back', 'Sack', 'Track', 'Truck'], 3),
   ('Complete the rhyme: I carry books in my back___.', ['pack', 'pick', 'peck', 'poke'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Missing Addends: Finding the Missing Number',
  'Kindergarten Math strand: students find the missing number in an addition sentence, such as figuring out that 3 plus what number makes 5.',
  [('What number is missing in 3 + ? = 5?', ['2', 'two']),
   ('What number is missing in 4 + ? = 6?', ['2', 'two']),
   ('How can you find a missing addend?', ['count up from the first number', 'count up to the total'])],
  [('3 + ? = 5', ['1', '2', '3', '4'], 1),
   ('2 + ? = 6', ['2', '3', '4', '5'], 2),
   ('? + 4 = 7', ['2', '3', '4', '5'], 1),
   ('To find a missing addend, we can ___.', ['Guess with no thinking', 'Count up from the first number to the total', 'Ignore the total', 'Subtract two totals'], 1),
   ('5 + ? = 9', ['3', '4', '5', '6'], 1)]),
Sc('Animal Diets: Herbivores, Carnivores, and Omnivores',
   'Kindergarten Science strand: animals eat different things — herbivores eat only plants, carnivores eat only meat, and omnivores eat both plants and meat.',
   [('What does a herbivore eat?', ['only plants', 'plants']),
    ('What does a carnivore eat?', ['only meat', 'meat']),
    ('What does an omnivore eat?', ['plants and meat', 'both plants and meat'])],
   [('An animal that eats only plants is called a ___.', ['Carnivore', 'Herbivore', 'Omnivore', 'Predator'], 1),
    ('An animal that eats only meat is called a ___.', ['Herbivore', 'Carnivore', 'Omnivore', 'Grazer'], 1),
    ('An animal that eats both plants and meat is called a ___.', ['Herbivore', 'Carnivore', 'Omnivore', 'Vegetarian'], 2),
    ('Which of these is usually a herbivore?', ['Lion', 'Rabbit', 'Wolf', 'Shark'], 1),
    ('A bear that eats berries and fish is an example of a(n) ___.', ['Herbivore', 'Carnivore', 'Omnivore', 'Insect'], 2)]),
SS('Our National Anthem: O Canada',
   'Kindergarten Social Studies strand: O Canada is our national anthem, a special song we sing to show pride in and respect for our country.',
   [('What is the name of our national anthem?', ['O Canada', 'O Canada song']),
    ('Why do we sing our national anthem?', ['to show pride in our country', 'show respect for Canada']),
    ('Name a place where you might hear O Canada sung.', ['school', 'a hockey game'])],
   [('What is the name of Canadas national anthem?', ['O Canada', 'God Save the King', 'This Land Is Your Land', 'True North'], 0),
    ('Why do people stand and sing the national anthem?', ['To show pride and respect for their country', 'It is required by law with no meaning', 'To warm up before recess', 'It has no reason'], 0),
    ('Where might you hear O Canada being sung?', ['At a school assembly or hockey game', 'Only in outer space', 'Never anywhere', 'Only in other countries'], 0),
    ('A national anthem is a special ___ for a country.', ['Song', 'Food', 'Building', 'Animal'], 0),
    ('Singing O Canada is one way people show they ___ their country.', ['Care about', 'Ignore', 'Dislike', 'Forget'], 0)]),
]),
day(132, [
L('Word Families: -ock Words',
  'Kindergarten Language strand: the -ock word family shares the same ending sound, as in rock, sock, lock, and clock.',
  [('Name a word that rhymes with rock.', ['sock', 'lock', 'clock']),
   ('What ending sound do sock and lock share?', ['ock', 'the ock sound']),
   ('Is block part of the -ock family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ock family?', ['Run', 'Sock', 'Sun', 'Pen'], 1),
   ('Which word rhymes with clock?', ['Cat', 'Rock', 'Cup', 'Can'], 1),
   ('Which word does NOT belong to the -ock family?', ['Rock', 'Sock', 'Lock', 'Lick'], 3),
   ('Complete the rhyme: I wear a shoe and a ___.', ['sock', 'sack', 'sick', 'sink'], 0),
   ('The ending sound of a word family stays the ___ in every word.', ['Same', 'Different', 'Silent', 'Missing'], 0)]),
M('Length: Measuring with a Ruler in Centimetres',
  'Kindergarten Math strand: students use a ruler to measure how long an object is in centimetres, lining up the end of the object with the zero mark.',
  [('What tool do we use to measure length in centimetres?', ['a ruler', 'ruler']),
   ('Where do we line up the object when measuring with a ruler?', ['the zero mark', 'at zero']),
   ('What unit do we use when measuring with a ruler?', ['centimetres', 'cm'])],
  [('What tool is used to measure length in centimetres?', ['A scale', 'A ruler', 'A clock', 'A cup'], 1),
   ('When measuring with a ruler, where should the object start?', ['At the zero mark', 'At the number 5', 'Anywhere at all', 'Off the ruler'], 0),
   ('Which unit does a ruler usually show for short objects?', ['Kilometres', 'Centimetres', 'Litres', 'Hours'], 1),
   ('If a crayon lines up with the number 8 on a ruler starting at 0, it is about ___ long.', ['8 centimetres', '8 hours', '8 litres', '8 kilograms'], 0),
   ('A ruler helps us measure length more ___ than just guessing.', ['Loudly', 'Accurately', 'Slowly only', 'Colourfully'], 1)]),
Sc('Fish: Gills and Fins',
   'Kindergarten Science strand: fish live in water and breathe using gills, and they swim using their fins.',
   [('Where do fish live?', ['in water', 'water']),
    ('What body part do fish use to breathe?', ['gills', 'their gills']),
    ('What body part do fish use to swim?', ['fins', 'their fins'])],
   [('Where do fish live?', ['In trees', 'In water', 'Underground', 'In the sky'], 1),
    ('What do fish use to breathe underwater?', ['Lungs', 'Gills', 'A nose', 'Skin only'], 1),
    ('What do fish use to swim through the water?', ['Legs', 'Wings', 'Fins', 'Claws'], 2),
    ('Which of these is a fish?', ['Salmon', 'Frog', 'Duck', 'Whale'], 0),
    ('Gills help a fish take in ___ from the water.', ['Oxygen', 'Sunlight', 'Sand', 'Salt only'], 0)]),
SS('Our Provincial Premier: Leading Our Province',
   'Kindergarten Social Studies strand: the premier is the leader of a province, working with other elected people to make decisions for everyone who lives there.',
   [('What do we call the leader of a province?', ['the premier', 'premier']),
    ('Does a premier lead a whole country or a province?', ['a province', 'just the province']),
    ('Why is a premier important?', ['makes decisions for the province', 'helps lead the province'])],
   [('What do we call the leader of a province?', ['The mayor', 'The premier', 'The principal', 'The prime minister'], 1),
    ('A premier leads ___.', ['A whole country', 'One province', 'A single school', 'A single street'], 1),
    ('How is a premier different from a mayor?', ['A premier leads a province, a mayor leads a town or city', 'They are the exact same job', 'A premier only leads schools', 'A mayor leads the whole country'], 0),
    ('A premier works with other elected people to make decisions for ___.', ['No one', 'Everyone in the province', 'Only one street', 'Only their own family'], 1),
    ('Which level of leader is a premier?', ['Provincial', 'International', 'Household', 'Classroom'], 0)]),
]),
day(133, [
L('Making New Words: Adding -y',
  'Kindergarten Language strand: adding -y to the end of a word can create a new word, such as changing rain into rainy or sun into sunny.',
  [('What does adding -y to rain make?', ['rainy', 'it makes rainy']),
   ('What does adding -y to sun make?', ['sunny', 'it makes sunny']),
   ('What does the word sleepy mean?', ['feeling like sleeping', 'wanting to sleep'])],
  [('What word do we get by adding -y to rain?', ['Rained', 'Rainy', 'Raining', 'Rainly'], 1),
   ('What word do we get by adding -y to sun?', ['Sunned', 'Sunny', 'Suns', 'Sunday'], 1),
   ('What does the word windy describe?', ['A day with a lot of wind', 'A day with no weather', 'A colour', 'A shape'], 0),
   ('Adding -y to a word often describes ___.', ['A colour', 'What something is like', 'A number', 'A place only'], 1),
   ('Which word is formed correctly by adding -y?', ['Cloud plus y equals cloudy', 'Cloud plus y equals clouding', 'Cloud plus y equals clouded', 'Cloud plus y equals cloudly'], 0)]),
M('Skip Counting by 4s to 40',
  'Kindergarten Math strand: students skip count by 4s, saying 4, 8, 12, 16, and continuing on up to 40.',
  [('What number comes after 4, 8, 12?', ['16', 'sixteen']),
   ('Skip count by 4s from 4 to 20.', ['4,8,12,16,20', '4 8 12 16 20']),
   ('What number comes right before 40 when skip counting by 4s?', ['36', 'thirty six'])],
  [('What comes next: 4, 8, 12, ___?', ['13', '14', '15', '16'], 3),
   ('What comes next: 16, 20, 24, ___?', ['25', '26', '27', '28'], 3),
   ('When skip counting by 4s, what number comes after 28?', ['29', '30', '31', '32'], 3),
   ('Skip counting by 4s means we add ___ each time.', ['1', '2', '4', '5'], 2),
   ('Which list correctly skip counts by 4s?', ['4, 8, 12, 16', '4, 6, 8, 10', '4, 8, 11, 16', '4, 5, 6, 7'], 0)]),
Sc('Butterflies and Moths: Comparing Two Insects',
   'Kindergarten Science strand: butterflies and moths are both insects with wings, but butterflies usually fly in the day and moths usually fly at night.',
   [('When do butterflies usually fly?', ['during the day', 'daytime']),
    ('When do moths usually fly?', ['at night', 'nighttime']),
    ('Are butterflies and moths both insects?', ['yes', 'yes they are'])],
   [('When are butterflies usually active?', ['At night', 'During the day', 'Only in winter', 'Never'], 1),
    ('When are moths usually active?', ['During the day', 'At night', 'Only underwater', 'Only in the rain'], 1),
    ('What do butterflies and moths have in common?', ['They are both insects with wings', 'They are both mammals', 'They both live underwater', 'They have no wings'], 0),
    ('Which is a way to tell some moths apart from butterflies?', ['Moths are often active at night', 'Moths never have wings', 'Moths live only in water', 'Moths are not insects'], 0),
    ('Butterflies and moths both begin life as a ___.', ['Caterpillar', 'Tadpole', 'Chick', 'Kitten'], 0)]),
SS('Our School Custodian: Keeping Our School Clean',
   'Kindergarten Social Studies strand: the school custodian works hard every day to keep our school clean, safe, and running smoothly.',
   [('What does a school custodian do?', ['keeps the school clean', 'cleans and fixes things']),
    ('Why is a custodians job important?', ['keeps the school clean and safe', 'helps everyone stay healthy']),
    ('How can students help the custodian?', ['clean up after themselves', 'put things away'])],
   [('What is a main job of the school custodian?', ['Teaching math', 'Keeping the school clean and in good repair', 'Driving the bus', 'Cooking lunch'], 1),
    ('Why is the custodians work important for the whole school?', ['It keeps the school clean and safe for everyone', 'It has no effect on the school', 'It only matters on weekends', 'It is not important'], 0),
    ('How can students help make the custodians job easier?', ['Cleaning up after themselves', 'Making extra messes on purpose', 'Ignoring spills', 'Hiding trash'], 0),
    ('Which task might a school custodian do?', ['Sweeping the hallway', 'Grading tests', 'Teaching art class', 'Driving to other cities'], 0),
    ('A clean and safe school helps students ___.', ['Learn better', 'Get sick more often', 'Feel unsafe', 'Avoid school'], 0)]),
]),
day(134, [
L('Comparing Adjectives: Big, Bigger, Biggest',
  'Kindergarten Language strand: students learn how adjectives change to compare things, such as big, bigger, and biggest.',
  [('What word describes one big thing?', ['big']),
   ('What word compares two things that are big?', ['bigger']),
   ('What word describes the biggest of three or more things?', ['biggest'])],
  [('Which word compares two big things?', ['Big', 'Bigger', 'Biggest', 'Bigly'], 1),
   ('Which word describes the biggest out of a whole group?', ['Big', 'Bigger', 'Biggest', 'Bigger than'], 2),
   ('An elephant is ___ than a mouse.', ['Big', 'Bigger', 'Biggest', 'Small'], 1),
   ('Out of a mouse, a dog, and an elephant, the elephant is the ___.', ['Big', 'Bigger', 'Biggest', 'Smallest'], 2),
   ('Adding -er to an adjective usually compares ___ things.', ['One', 'Two', 'No', 'Every colour of'], 1)]),
M('Fractions: Introducing Thirds',
  'Kindergarten Math strand: students learn that cutting a shape into three equal parts makes thirds, with each part called one third.',
  [('If a shape is cut into three equal parts, what is each part called?', ['a third', 'one third']),
   ('How many equal parts make up thirds?', ['3', 'three']),
   ('Are the three parts in thirds the same size?', ['yes', 'yes they are equal'])],
  [('If a shape is cut into three equal parts, each part is called ___.', ['A half', 'A third', 'A quarter', 'A whole'], 1),
   ('How many equal parts are in thirds?', ['2', '3', '4', '6'], 1),
   ('For parts to be called thirds, they must be ___.', ['Different sizes', 'Equal in size', 'Only two parts', 'Uncounted'], 1),
   ('Which shows a shape divided into thirds?', ['A circle cut into 3 equal slices', 'A circle cut into 2 equal slices', 'A whole uncut circle', 'A circle cut into 5 pieces'], 0),
   ('Thirds have ___ equal parts, while halves have 2.', ['3', '4', '5', '6'], 0)]),
Sc('Ocean Tides: The Rise and Fall of the Sea',
   'Kindergarten Science strand: ocean tides are the rise and fall of the sea, which happens twice a day and can be seen on the beach.',
   [('What are ocean tides?', ['the rise and fall of the sea', 'the sea going up and down']),
    ('Where can you often see tides?', ['at the beach', 'the beach']),
    ('How many times a day does the tide usually rise and fall?', ['twice', 'two times'])],
   [('What are ocean tides?', ['The rise and fall of the sea', 'A kind of fish', 'A type of storm', 'A colour of water'], 0),
    ('Where can people often observe the tide changing?', ['In the desert', 'At the beach', 'In a forest', 'On a mountain'], 1),
    ('About how many times a day does the tide usually rise and fall?', ['Once', 'Twice', 'Ten times', 'Never'], 1),
    ('At low tide, the water usually moves ___ the shore.', ['Away from', 'Straight up into the sky above', 'Underground beneath', 'Nowhere near'], 0),
    ('Tides are an example of how the ocean is always ___.', ['Frozen solid', 'Moving and changing', 'Completely still', 'Made of ice'], 1)]),
SS('National Indigenous Peoples Day',
   'Kindergarten Social Studies strand: National Indigenous Peoples Day is a special day in June when Canadians celebrate the cultures and achievements of First Nations, Metis, and Inuit peoples.',
   [('What is celebrated on National Indigenous Peoples Day?', ['Indigenous cultures and achievements', 'First Nations, Metis, and Inuit peoples']),
    ('In what month is National Indigenous Peoples Day?', ['June']),
    ('Why do we celebrate this day?', ['to honour Indigenous cultures', 'show respect and learn'])],
   [('What does National Indigenous Peoples Day celebrate?', ['The cultures and achievements of First Nations, Metis, and Inuit peoples', 'A type of weather', 'A new school building', 'A sports team'], 0),
    ('In which month is National Indigenous Peoples Day celebrated?', ['December', 'June', 'February', 'August'], 1),
    ('Why is it important to celebrate National Indigenous Peoples Day?', ['To honour and learn about Indigenous cultures', 'It is not important', 'To ignore Canadian history', 'Only adults need to know about it'], 0),
    ('Which groups are celebrated on this day?', ['First Nations, Metis, and Inuit peoples', 'Only visitors from other countries', 'Only teachers', 'Only students'], 0),
    ('Learning about National Indigenous Peoples Day helps students show ___.', ['Confusion', 'Respect and understanding', 'Carelessness', 'No interest'], 1)]),
]),
day(135, [
L('Onomatopoeia: Sound Words in Stories',
  'Kindergarten Language strand: onomatopoeia words sound like the noise they describe, such as buzz, splash, and crash.',
  [('Give an example of a sound word.', ['buzz', 'splash', 'crash']),
   ('What sound word describes a bee?', ['buzz']),
   ('What sound word describes something falling into water?', ['splash'])],
  [('Which word sounds like the noise it describes?', ['Happy', 'Buzz', 'Table', 'Green'], 1),
   ('Which sound word could describe a bee flying by?', ['Splash', 'Buzz', 'Crash', 'Whisper'], 1),
   ('Which sound word could describe something falling into water?', ['Buzz', 'Splash', 'Tick', 'Meow'], 1),
   ('Sound words that copy the noise they describe are called ___.', ['Synonyms', 'Onomatopoeia', 'Prefixes', 'Rhymes'], 1),
   ('Which word is an example of onomatopoeia?', ['Crash', 'Chair', 'Blue', 'Walk'], 0)]),
M('Money: Making a Target Amount with Different Coins',
  'Kindergarten Math strand: students find different ways to make the same amount of money, such as making 10 cents with two nickels or ten pennies.',
  [('Name one way to make 10 cents.', ['two nickels', 'ten pennies']),
   ('Name another way to make 10 cents.', ['one nickel and five pennies', 'ten pennies']),
   ('Can there be more than one way to make the same amount?', ['yes', 'yes there can'])],
  [('Which is one way to make 10 cents?', ['Two nickels', 'One penny', 'Three pennies', 'One dime and one nickel'], 0),
   ('Which coins could also make 10 cents?', ['Ten pennies', 'Two dimes', 'One nickel alone', 'Five nickels'], 0),
   ('Is there only one way to make the same amount of money?', ['Yes, only one way', 'No, there can be many ways', 'Money cannot be made with coins', 'Coins have no value'], 1),
   ('Which combination makes 6 cents?', ['One nickel and one penny', 'Two nickels', 'Six dimes', 'One dime'], 0),
   ('Finding different coin combinations for the same amount helps us understand ___.', ['Coin values', 'Animal habitats', 'Story characters', 'The alphabet'], 0)]),
Sc('Our Sense of Balance: How We Stay Upright',
   'Kindergarten Science strand: our body has a sense of balance, helped by a part inside our ear, that lets us stand, walk, and stay upright without falling.',
   [('What helps our body stay upright?', ['our sense of balance', 'balance']),
    ('What body part helps us with balance?', ['inside our ear', 'our ear']),
    ('Name an activity that uses balance.', ['walking', 'standing on one foot'])],
   [('What sense helps us stand and walk without falling?', ['Sense of taste', 'Sense of balance', 'Sense of smell', 'Sense of hearing only'], 1),
    ('Which body part helps control our sense of balance?', ['Our elbow', 'A part inside our ear', 'Our hair', 'Our teeth'], 1),
    ('Which activity uses our sense of balance the most?', ['Standing on one foot', 'Smelling a flower', 'Tasting food', 'Listening to music'], 0),
    ('Our sense of balance helps prevent us from ___.', ['Hearing sounds', 'Falling over', 'Tasting food', 'Smelling things'], 1),
    ('Riding a bicycle is a good example of using ___.', ['Balance', 'Taste', 'Smell only', 'Nothing at all'], 0)]),
SS('Our Local Newspaper: Sharing the News',
   'Kindergarten Social Studies strand: a local newspaper shares stories and information about what is happening in our community.',
   [('What does a newspaper share with people?', ['news and information', 'stories about the community']),
    ('Who writes stories for a newspaper?', ['reporters', 'a journalist']),
    ('Name one thing you might read about in a local newspaper.', ['community events', 'local news'])],
   [('What does a local newspaper share with the community?', ['News and information', 'Only pictures with no words', 'Nothing at all', 'Only weather from other planets'], 0),
    ('Who writes the stories in a newspaper?', ['Reporters', 'Firefighters', 'Doctors', 'Pilots'], 0),
    ('Which is something you might read about in a local newspaper?', ['A community event', 'A made-up fairy tale only', 'Nothing about your town', 'Only ads for toys'], 0),
    ('A newspaper helps people in a community stay ___.', ['Confused', 'Informed', 'Unaware', 'Bored only'], 1),
    ('Besides paper newspapers, where else might people read local news today?', ['Online or on a website', 'Nowhere else', 'Only in outer space', 'Only by asking a stranger'], 0)]),
]),
day(136, [
L('Nonfiction Text Features: Table of Contents and Headings',
  'Kindergarten Language strand: nonfiction books often have a table of contents and headings that help readers find information quickly.',
  [('What does a table of contents show?', ['where to find each part of a book', 'a list of the parts of a book']),
   ('What is a heading?', ['a title for a section', 'a small title above some text']),
   ('Why are these features helpful?', ['help readers find information', 'make it easier to find things'])],
  [('What does a table of contents usually show?', ['A list of story characters', 'A list of the parts of a book and their pages', 'A list of ingredients', 'A list of weather facts'], 1),
   ('What is a heading in a nonfiction book?', ['A small title above a section of text', 'The last page of the book', 'A picture with no words', 'The books cover colour'], 0),
   ('Why do nonfiction books use headings and a table of contents?', ['To help readers find information quickly', 'To make the book longer for no reason', 'To confuse the reader', 'They have no purpose'], 0),
   ('Where would you usually find a table of contents in a book?', ['Near the beginning', 'Only on the back cover', 'In the middle of a chapter', 'Nowhere in the book'], 0),
   ('A heading tells the reader what a section is mostly ___.', ['About', 'Coloured', 'Weighing', 'Smelling like'], 0)]),
M('Perimeter: Walking Around the Edge of a Shape',
  'Kindergarten Math strand: perimeter is the distance all the way around the outside edge of a shape, like walking around the edge of a garden.',
  [('What is perimeter?', ['the distance around a shape', 'the distance around the outside edge']),
   ('If you walk around the edge of a square garden, what are you measuring?', ['its perimeter', 'perimeter']),
   ('Does perimeter measure the inside or the outside edge of a shape?', ['the outside edge', 'outside'])],
  [('What is the perimeter of a shape?', ['The space inside it', 'The distance all the way around its outside edge', 'Its colour', 'Its weight'], 1),
   ('If you walk all the way around a playground, you are walking its ___.', ['Area', 'Perimeter', 'Volume', 'Height'], 1),
   ('Which shape has a longer perimeter, a big square or a tiny square?', ['The big square', 'The tiny square', 'They are always equal', 'Neither has a perimeter'], 0),
   ('To find perimeter, we add up the length of each ___ of the shape.', ['Corner', 'Side', 'Colour', 'Centre'], 1),
   ('Perimeter measures the ___ of a shape, not the space inside it.', ['Outside edge', 'Middle', 'Weight', 'Smell'], 0)]),
Sc('The Night Sky: Constellations',
   'Kindergarten Science strand: a constellation is a group of stars that forms a pattern in the night sky, such as the Big Dipper.',
   [('What is a constellation?', ['a group of stars that forms a pattern', 'a pattern of stars']),
    ('Name a well-known constellation.', ['the Big Dipper']),
    ('When can we see constellations?', ['at night', 'nighttime'])],
   [('What is a constellation?', ['A group of stars forming a pattern', 'A type of planet', 'A kind of cloud', 'A single bright star'], 0),
    ('What is a well-known constellation people often learn first?', ['The Big Dipper', 'The Sahara', 'The Rocky Mountains', 'The Great Lakes'], 0),
    ('When can we usually see constellations in the sky?', ['During the day', 'At night', 'Only underwater', 'Never'], 1),
    ('People have used constellations for a long time to help with ___.', ['Finding direction', 'Cooking food', 'Growing plants', 'Building houses'], 0),
    ('A constellation is made up of many ___ that form a shape.', ['Stars', 'Planets', 'Moons', 'Clouds'], 0)]),
SS('Comparing Then and Now: How We Communicate',
   'Kindergarten Social Studies strand: the way people communicate has changed over time, from writing letters long ago to using phones and video calls today.',
   [('Name a way people communicated long ago.', ['writing letters', 'sending a letter']),
    ('Name a way people communicate today.', ['phone call', 'video call']),
    ('How has communication changed over time?', ['it became faster', 'new technology like phones'])],
   [('How did many people communicate over long distances long ago?', ['By writing letters', 'By video call', 'By text message', 'By email only'], 0),
    ('Which is a modern way people communicate today?', ['Sending a video call', 'Only sending letters by horse', 'Using smoke signals only', 'Not communicating at all'], 0),
    ('How has communication changed from long ago to today?', ['It has become faster with new technology', 'It has not changed at all', 'People stopped talking to each other', 'It became slower'], 0),
    ('Comparing then and now helps us understand ___.', ['That things can change over time', 'That nothing ever changes', 'Nothing important', 'Only todays technology'], 0),
    ('Which is an example of an older way to send a message?', ['A handwritten letter', 'A smartphone video call', 'A text message', 'An email'], 0)]),
]),
day(137, [
L('Categorizing Words: Sorting Words into Groups',
  'Kindergarten Language strand: students sort words into categories, such as grouping animals, foods, and colours into separate groups.',
  [('Name a word that belongs in the category animals.', ['dog', 'cat', 'bird']),
   ('Name a word that belongs in the category foods.', ['apple', 'bread']),
   ('Why do we sort words into categories?', ['to organize them by meaning', 'group similar things'])],
  [('Which word belongs in the category animals?', ['Apple', 'Dog', 'Chair', 'Red'], 1),
   ('Which word belongs in the category foods?', ['Bread', 'Lion', 'Table', 'Green'], 0),
   ('Which word does NOT belong with cat, dog, and bird?', ['Fish', 'Banana', 'Rabbit', 'Horse'], 1),
   ('Sorting words into categories helps us understand how words are ___.', ['Coloured', 'Related in meaning', 'Spelled backwards', 'Counted'], 1),
   ('Which group are all colours?', ['Red, blue, yellow', 'Dog, cat, bird', 'Apple, banana, grape', 'One, two, three'], 0)]),
M('Shapes: Introducing the Trapezoid and Rhombus',
  'Kindergarten Math strand: students learn two new shape names, the trapezoid, which has one pair of parallel sides, and the rhombus, a slanted shape with four equal sides.',
  [('How many sides does a trapezoid have?', ['4', 'four']),
   ('How many equal sides does a rhombus have?', ['4', 'four']),
   ('Name something shaped like a trapezoid.', ['a table top', 'a kite has a similar shape'])],
  [('How many sides does a trapezoid have?', ['3', '4', '5', '6'], 1),
   ('A rhombus has how many equal sides?', ['2', '3', '4', '5'], 2),
   ('Which shape looks like a slanted square?', ['Circle', 'Rhombus', 'Cone', 'Sphere'], 1),
   ('A trapezoid has one pair of sides that are ___.', ['Parallel', 'Curved', 'Missing', 'Coloured'], 0),
   ('Which of these shapes has four equal sides that are slanted?', ['Rhombus', 'Triangle', 'Circle', 'Trapezoid'], 0)]),
Sc('Losing Teeth: Baby Teeth and Adult Teeth',
   'Kindergarten Science strand: children have baby teeth that fall out over time and are replaced by bigger, stronger adult teeth.',
   [('What do we call the first teeth children have?', ['baby teeth', 'baby teeth or milk teeth']),
    ('What happens to baby teeth over time?', ['they fall out', 'fall out and are replaced']),
    ('What replaces baby teeth?', ['adult teeth', 'bigger adult teeth'])],
   [('What are a childs first teeth called?', ['Adult teeth', 'Baby teeth', 'Wisdom teeth', 'Silver teeth'], 1),
    ('What eventually happens to baby teeth?', ['They fall out and are replaced', 'They stay forever', 'They turn into hair', 'They disappear with no replacement'], 0),
    ('What kind of teeth replace baby teeth?', ['Adult teeth', 'No new teeth at all', 'Plastic teeth', 'Baby teeth again'], 0),
    ('Why is it healthy to take care of baby teeth even though they fall out?', ['They help with eating and speaking until adult teeth arrive', 'They do not matter at all', 'Only adult teeth need care', 'Baby teeth cause no problems ever'], 0),
    ('Adult teeth are usually ___ than baby teeth.', ['Smaller', 'Bigger and stronger', 'The exact same size', 'Softer'], 1)]),
SS('Our Conservation Officers: Protecting Parks and Wildlife',
   'Kindergarten Social Studies strand: conservation officers work to protect parks, forests, and wild animals, making sure people follow rules that keep nature safe.',
   [('What do conservation officers protect?', ['parks and wildlife', 'nature and animals']),
    ('Why are rules important in parks?', ['to keep nature and people safe', 'protect animals and plants']),
    ('Name one place a conservation officer might work.', ['a park', 'a forest'])],
   [('What is the main job of a conservation officer?', ['Protecting parks, forests, and wildlife', 'Delivering mail', 'Teaching math', 'Building houses'], 0),
    ('Why do parks have rules that conservation officers help enforce?', ['To keep nature and visitors safe', 'Rules are not needed in parks', 'To make parks boring', 'To stop people from ever visiting'], 0),
    ('Where might a conservation officer work?', ['In a forest or park', 'Only inside an office building', 'Only in a classroom', 'Only in a hospital'], 0),
    ('Conservation officers help protect wild animals from ___.', ['Being cared for', 'Harm and unsafe treatment', 'Nothing at all', 'Only sunshine'], 1),
    ('Following park rules helps keep both people and ___ safe.', ['Wildlife', 'Nothing', 'Cars', 'Buildings'], 0)]),
]),
day(138, [
L('Story Purpose: To Entertain or To Inform',
  'Kindergarten Language strand: stories can be written to entertain us with fun and adventure, or to inform us with facts and true information.',
  [('What does a story written to entertain do?', ['makes us have fun', 'tells a fun or exciting story']),
   ('What does a story written to inform do?', ['teaches us facts', 'gives true information']),
   ('Give an example of a book that mostly informs.', ['a book about animals', 'a fact book'])],
  [('A story written mainly to make us laugh or feel excited is meant to ___.', ['Inform', 'Entertain', 'Confuse', 'Erase'], 1),
   ('A book that gives true facts about animals is meant to ___.', ['Entertain only', 'Inform', 'Trick the reader', 'Do nothing'], 1),
   ('Which is an example of a book written mostly to inform?', ['A book of true facts about the ocean', 'A made-up fairy tale', 'A silly poem about a dragon', 'A joke book'], 0),
   ('Which is an example of a book written mostly to entertain?', ['An adventure story about a pirate', 'A book of weather facts', 'An encyclopedia', 'A recipe book'], 0),
   ('Knowing a storys purpose helps readers understand ___.', ['Why the author wrote it', 'Nothing useful', 'Only the page numbers', 'The books colour'], 0)]),
M('Estimating Weight: About How Heavy Is It?',
  'Kindergarten Math strand: students make a reasonable guess, or estimate, about how heavy an object is before checking with a scale.',
  [('What does it mean to estimate weight?', ['make a careful guess about how heavy something is', 'guess how heavy']),
   ('Which is heavier, a feather or a rock?', ['a rock', 'the rock']),
   ('How can you check if your estimate was close?', ['weigh it on a scale', 'use a scale'])],
  [('What does it mean to estimate the weight of something?', ['Make a careful guess before checking', 'Know the exact weight with no guessing', 'Ignore the object completely', 'Measure its colour'], 0),
   ('Which object is likely heavier?', ['A feather', 'A large rock', 'A single leaf', 'A cotton ball'], 1),
   ('How can we check if a weight estimate was close?', ['Weigh the object on a scale', 'Guess again with no tool', 'Ask a random question', 'Ignore it forever'], 0),
   ('A good estimate is a guess that is ___.', ['Completely random', 'Reasonable and thoughtful', 'Always exactly right', 'Impossible to make'], 1),
   ('Which of these would likely feel the lightest?', ['A feather', 'A brick', 'A bowling ball', 'A large book'], 0)]),
Sc('Where Our Tap Water Comes From',
   'Kindergarten Science strand: the water that comes from our tap travels through pipes from a treatment plant that cleans water from rivers, lakes, or underground.',
   [('Where does tap water come from before it reaches our home?', ['a water treatment plant', 'treatment plant']),
    ('What does a water treatment plant do?', ['cleans the water', 'makes water safe to drink']),
    ('How does water get to our home?', ['through pipes', 'pipes']),],
   [('What cleans water before it reaches our tap?', ['A water treatment plant', 'A toy factory', 'A bakery', 'A library'], 0),
    ('How does clean water usually travel to our homes?', ['Through underground pipes', 'By airplane', 'By hand delivery', 'It does not travel at all'], 0),
    ('Where might a treatment plant get water from originally?', ['Rivers, lakes, or underground sources', 'Only from clouds directly', 'Only from the ocean', 'From nowhere at all'], 0),
    ('Why is it important for water to be treated before we drink it?', ['To make sure it is clean and safe', 'Treatment makes no difference', 'It tastes better dirty', 'It is not important'], 0),
    ('Which best describes the journey of tap water?', ['Source water is cleaned, then piped to homes', 'Water appears instantly with no process', 'Water is delivered by truck only', 'Water never needs cleaning'], 0)]),
SS('Voting: How We Choose Our Leaders',
   'Kindergarten Social Studies strand: voting is how people choose their leaders, with each person getting to pick who they think will do the best job.',
   [('What is voting?', ['choosing a leader by picking a choice', 'how people choose leaders']),
    ('Why do people vote?', ['to choose their leaders', 'help decide who leads']),
    ('Is voting a way for many people to have a say?', ['yes', 'yes it lets everyone choose'])],
   [('What is voting?', ['A way people choose their leaders', 'A type of game with no purpose', 'A way to clean a classroom', 'A kind of food'], 0),
    ('Why is voting important in choosing leaders like a mayor or premier?', ['It lets many people have a say in who leads', 'It has no importance', 'Only one person should decide alone', 'It makes decisions harder for no reason'], 0),
    ('When people vote, they are usually choosing between ___.', ['Different foods', 'Different candidates or choices', 'Different colours only', 'Nothing at all'], 1),
    ('A classroom could use voting to decide ___.', ['Which book to read together', 'What the weather will be', 'What day it is', 'Nothing useful'], 0),
    ('Voting gives people a chance to ___ who leads them.', ['Have no opinion about', 'Help choose', 'Ignore', 'Avoid learning about'], 1)]),
]),
day(139, [
L('Word Families: -ick Words',
  'Kindergarten Language strand: the -ick word family shares the same ending sound, as in kick, pick, lick, and stick.',
  [('Name a word that rhymes with kick.', ['pick', 'lick', 'stick']),
   ('What ending sound do pick and lick share?', ['ick', 'the ick sound']),
   ('Is quick part of the -ick family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ick family?', ['Cat', 'Pick', 'Dog', 'Sun'], 1),
   ('Which word rhymes with stick?', ['Stop', 'Kick', 'Star', 'Stay'], 1),
   ('Which word does NOT belong to the -ick family?', ['Kick', 'Lick', 'Pick', 'Pack'], 3),
   ('Complete the rhyme: My favourite treat is a lollipop I like to ___.', ['lick', 'lack', 'lock', 'luck'], 0),
   ('Recognizing word families helps us read new words that share the same ___.', ['Colour', 'Ending sound', 'Meaning', 'Number of letters'], 1)]),
M('Skip Counting Backwards by 10s from 100',
  'Kindergarten Math strand: students skip count backwards by 10s, saying 100, 90, 80, and continuing down to 0.',
  [('What number comes right after 100 when counting backwards by 10s?', ['90', 'ninety']),
   ('Skip count backwards by 10s from 50 to 0.', ['50,40,30,20,10,0', '50 40 30 20 10 0']),
   ('What number comes right before 0 when counting backwards by 10s?', ['10', 'ten'])],
  [('Counting backwards by 10s from 100, what comes next: 100, 90, ___?', ['85', '80', '75', '70'], 1),
   ('Counting backwards by 10s, what comes after 50?', ['45', '40', '35', '30'], 1),
   ('Counting backwards by 10s from 30, what comes right before 0?', ['5', '10', '15', '20'], 1),
   ('Skip counting backwards by 10s means we subtract ___ each time.', ['1', '5', '10', '100'], 2),
   ('Which list correctly skip counts backwards by 10s?', ['100, 90, 80, 70', '100, 95, 90, 85', '100, 90, 70, 60', '100, 80, 60, 50'], 0)]),
Sc('Animal Mimicry: Looking Like Something Else',
   'Kindergarten Science strand: some animals use mimicry, looking or acting like a different, often more dangerous animal, to help keep themselves safe.',
   [('What is animal mimicry?', ['looking like a different animal', 'copying how another animal looks']),
    ('Why might an animal use mimicry?', ['to stay safe from predators', 'to look dangerous']),
    ('Is mimicry the same as camouflage?', ['no', 'no it is different, it copies another animal'])],
   [('What is animal mimicry?', ['An animal looking or acting like a different animal', 'An animal that never moves', 'A type of weather', 'An animal that only eats plants'], 0),
    ('Why might a harmless animal use mimicry?', ['To look dangerous and scare away predators', 'To become invisible completely', 'To fly higher', 'To grow bigger permanently'], 0),
    ('How is mimicry different from camouflage?', ['Mimicry copies another animals look, camouflage blends into surroundings', 'They are the exact same thing', 'Mimicry only happens underwater', 'Camouflage only happens in mimicry'], 0),
    ('Which is an example of mimicry?', ['A harmless insect looking like a stinging wasp', 'A brown moth blending into tree bark', 'A polar bear being white like snow', 'A fish swimming in a school'], 0),
    ('Animal mimicry mainly helps an animal ___.', ['Stay safer from danger', 'Fly faster', 'Grow taller', 'Change colour permanently'], 0)]),
SS('Snow Plow Drivers: Keeping Roads Safe in Winter',
   'Kindergarten Social Studies strand: snow plow drivers clear snow and ice from roads in winter so that cars, buses, and people can travel safely.',
   [('What does a snow plow driver clear from roads?', ['snow and ice', 'snow']),
    ('Why is it important to clear snow from roads?', ['so people can travel safely', 'keeps roads safe for driving']),
    ('When do snow plow drivers usually work the most?', ['winter', 'during snowstorms'])],
   [('What is the main job of a snow plow driver?', ['Clearing snow and ice from roads', 'Delivering mail', 'Teaching school', 'Growing vegetables'], 0),
    ('Why is it important for roads to be cleared of snow?', ['So cars, buses, and people can travel safely', 'Snow on roads is not a problem', 'It has no effect on safety', 'Roads should always be covered'], 0),
    ('When are snow plow drivers usually busiest?', ['During summer', 'During winter snowstorms', 'During the spring only', 'They are never busy'], 1),
    ('Snow plow drivers help keep school buses running by ___.', ['Clearing the roads they drive on', 'Driving the buses themselves', 'Teaching the bus drivers', 'Painting the buses'], 0),
    ('Which of these might a snow plow driver use to clear a road?', ['A large plow blade on a truck', 'A paintbrush', 'A telescope', 'A cooking pot'], 0)]),
]),
day(140, [
L('Language Review: New Word Families, Adjectives, and Text Features',
  'Kindergarten Language strand review: students revisit the -ack, -ock, and -ick word families, adding -y, comparing adjectives, onomatopoeia, and nonfiction text features.',
  [('Name a word from the -ack, -ock, or -ick family.', ['back', 'sock', 'kick']),
   ('What word do we get by adding -y to sun?', ['sunny']),
   ('Give an example of a sound word.', ['buzz', 'splash'])],
  [('Which word belongs to the -ack family?', ['Sun', 'Pack', 'Bed', 'Cup'], 1),
   ('What word do we get by adding -y to rain?', ['Rained', 'Rainy', 'Raining', 'Rainly'], 1),
   ('Which word compares two big things?', ['Big', 'Bigger', 'Biggest', 'Bigly'], 1),
   ('Which word sounds like the noise it describes?', ['Happy', 'Buzz', 'Table', 'Green'], 1),
   ('What does a table of contents usually show?', ['A list of story characters', 'A list of the parts of a book and their pages', 'A list of ingredients', 'A list of weather facts'], 1)]),
M('Math Review: Missing Addends, Fractions, and Shapes',
  'Kindergarten Math strand review: students revisit missing addends, measuring with a ruler, skip counting by 4s, thirds, money combinations, perimeter, and new shapes.',
  [('What number is missing in 3 + ? = 5?', ['2']),
   ('If a shape is cut into three equal parts, what is each part called?', ['a third']),
   ('How many sides does a trapezoid have?', ['4'])],
  [('3 + ? = 5', ['1', '2', '3', '4'], 1),
   ('What tool is used to measure length in centimetres?', ['A scale', 'A ruler', 'A clock', 'A cup'], 1),
   ('If a shape is cut into three equal parts, each part is called ___.', ['A half', 'A third', 'A quarter', 'A whole'], 1),
   ('What is the perimeter of a shape?', ['The space inside it', 'The distance all the way around its outside edge', 'Its colour', 'Its weight'], 1),
   ('A rhombus has how many equal sides?', ['2', '3', '4', '5'], 2)]),
Sc('Science Review: Animals, Space, and Our Bodies',
   'Kindergarten Science strand review: students revisit animal diets, fish, butterflies and moths, ocean tides, our sense of balance, constellations, losing teeth, tap water, and mimicry.',
   [('An animal that eats only plants is called what?', ['a herbivore']),
    ('What is a constellation?', ['a group of stars that forms a pattern']),
    ('What replaces baby teeth?', ['adult teeth'])],
   [('An animal that eats only plants is called a ___.', ['Carnivore', 'Herbivore', 'Omnivore', 'Predator'], 1),
    ('What do fish use to breathe underwater?', ['Lungs', 'Gills', 'A nose', 'Skin only'], 1),
    ('What is a constellation?', ['A group of stars forming a pattern', 'A type of planet', 'A kind of cloud', 'A single bright star'], 0),
    ('What kind of teeth replace baby teeth?', ['Adult teeth', 'No new teeth at all', 'Plastic teeth', 'Baby teeth again'], 0),
    ('What is animal mimicry?', ['An animal looking or acting like a different animal', 'An animal that never moves', 'A type of weather', 'An animal that only eats plants'], 0)]),
SS('Social Studies Review: Leaders, Helpers, and Our Community',
   'Kindergarten Social Studies strand review: students revisit O Canada, the premier, our school custodian, National Indigenous Peoples Day, the newspaper, communication, conservation officers, voting, and snow plow drivers.',
   [('What is the name of Canadas national anthem?', ['O Canada']),
    ('What do we call the leader of a province?', ['the premier']),
    ('What is voting?', ['choosing a leader by picking a choice'])],
   [('What is the name of Canadas national anthem?', ['O Canada', 'God Save the King', 'This Land Is Your Land', 'True North'], 0),
    ('What do we call the leader of a province?', ['The mayor', 'The premier', 'The principal', 'The prime minister'], 1),
    ('What is the main job of the school custodian?', ['Teaching math', 'Keeping the school clean and in good repair', 'Driving the bus', 'Cooking lunch'], 1),
    ('What is the main job of a conservation officer?', ['Protecting parks, forests, and wildlife', 'Delivering mail', 'Teaching math', 'Building houses'], 0),
    ('What is voting?', ['A way people choose their leaders', 'A type of game with no purpose', 'A way to clean a classroom', 'A kind of food'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_131_140)
    append_worksheet_days(0, g0_131_140)
