#!/usr/bin/env python3
"""Grade 1, Days 61-70 -- FOURTH batch, completing Grade 1 through Day 70.
Self-contained script modeled exactly on gen_grade1_days51_60.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-60 topics (see data/grade1.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely to
keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260827):
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
d61_lang = sub('Language', 'Consonant Blends: sc, sk, sl, tw',
  'Students learn beginning consonant blends where two consonants join and both sounds are heard, such as sc in scarf, sk in skate, sl in slide, and tw in twin.',
  [('Name one word that begins with the sc blend, like scarf or scale.', ['scarf', 'scale', 'scoop', 'scan']),
   ('Name one word that begins with the sk blend, like skate or skip.', ['skate', 'skip', 'skunk', 'sky']),
   ('What two letters begin the word twin?', ['tw'])],
  [('Which word begins with the sc blend?', ['Scarf', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the sk blend?', ['Skate', 'Cat', 'Bed', 'Sun'], 0),
   ('Which word begins with the sl blend?', ['Slide', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the tw blend?', ['Twin', 'Cat', 'Dog', 'Sun'], 0),
   ('A consonant blend is two consonants that ___.', ['Blend together with both sounds heard', 'Never appear together', 'Always make one new sound like a digraph', 'Are always silent'], 0)])

d61_math = sub('Math', 'Time: Days of the Week and Months of the Year',
  'Students learn the names and order of the seven days of the week and the twelve months of the year, building an understanding of how a calendar is organized.',
  [('Name the day of the week that comes right after Monday.', ['tuesday']),
   ('How many days are in one week?', ['7', 'seven']),
   ('Name the month that comes right after January.', ['february'])],
  [('Which day comes right after Monday?', ['Tuesday', 'Sunday', 'Friday', 'Wednesday'], 0),
   ('How many days are in one week?', ['7', '5', '6', '10'], 0),
   ('Which month comes right after January?', ['February', 'March', 'December', 'June'], 0),
   ('How many months are in one year?', ['12', '10', '7', '24'], 0),
   ('A calendar helps us keep track of ___.', ['Days, weeks, and months', 'Only colours', 'Only shapes', 'Only weather'], 0)])

d61_sci = sub('Science', 'Spiders and Other Small Creatures',
  'Students learn that spiders are small creatures with eight legs that are not insects, and that many small creatures like spiders help control the number of other bugs.',
  [('How many legs does a spider have?', ['8', 'eight']),
   ('Is a spider an insect or not an insect?', ['not an insect', 'no']),
   ('Name one thing a spider can build to catch food, like a web.', ['a web', 'web'])],
  [('How many legs does a spider have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
   ('Is a spider an insect?', ['No, spiders are not insects', 'Yes, all spiders are insects', 'Spiders are birds', 'Spiders are fish'], 0),
   ('What can a spider build to catch food?', ['A web', 'A nest of sticks', 'A shell', 'A den'], 0),
   ('How many legs does an insect usually have?', ['Six', 'Eight', 'Four', 'Ten'], 0),
   ('Why are spiders helpful to have around?', ['They catch and eat many small bugs', 'They make loud noises', 'They grow flowers', 'They make honey'], 0)])

d61_ss = sub('SocialStudies', 'Weather and Clothing: Dressing for the Season',
  'Students learn that people choose different clothing depending on the weather and season, such as wearing a warm coat in winter and light clothing in summer.',
  [('Name one piece of clothing you might wear on a cold winter day, like a coat.', ['a coat', 'mittens', 'a hat', 'boots']),
   ('Name one piece of clothing you might wear on a hot summer day, like shorts.', ['shorts', 'a t-shirt', 'sandals']),
   ('Why do people change their clothing with the seasons?', ['to stay comfortable', 'to stay warm or cool'])],
  [('Which clothing would be best on a cold winter day?', ['A warm coat and mittens', 'Shorts and sandals', 'A swimsuit', 'A sun hat only'], 0),
   ('Which clothing would be best on a hot summer day?', ['Shorts and a t-shirt', 'A heavy winter coat', 'Snow boots', 'Mittens'], 0),
   ('Why do people wear different clothing in different seasons?', ['To stay comfortable in the weather', 'Clothing never needs to change', 'To match the colour of the sky', 'Because stores only sell one kind'], 0),
   ('What might you wear on a rainy day?', ['A raincoat and boots', 'A swimsuit', 'Shorts only', 'Mittens only'], 0),
   ('Choosing the right clothing for the weather helps people stay ___.', ['Safe and comfortable', 'Cold in summer', 'Hot in winter', 'Confused'], 0)])

# ─── DAY 62 ─────────────────────────────────────────────────────────────────
d62_lang = sub('Language', 'Vowel Teams: oi and oy',
  'Students learn that the letters oi and oy work together as a vowel team to make the same sound, as in coin and toy, with oi usually used in the middle of a word and oy at the end.',
  [('What two letters make the vowel sound in the middle of the word coin?', ['oi']),
   ('What two letters make the vowel sound at the end of the word toy?', ['oy']),
   ('Name one word that has the oy vowel team, like toy or boy.', ['toy', 'boy', 'joy'])],
  [('Which letters make the vowel sound in the word coin?', ['oi', 'oy', 'ee', 'ea'], 0),
   ('Which letters make the vowel sound in the word toy?', ['oy', 'oi', 'ai', 'ay'], 0),
   ('Which word has the oi vowel team?', ['Coin', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the oy vowel team?', ['Boy', 'Cat', 'Dog', 'Sun'], 0),
   ('The oi vowel team is usually found ___ a word, while oy is usually found at the end.', ['In the middle of', 'Never in', 'Only before', 'Only after the end of'], 0)])

d62_math = sub('Math', 'Money: Adding Coins to Make a Total',
  'Students practise adding the values of different coins, such as a nickel and a dime, to find the total amount of money.',
  [('If you have a nickel worth 5 cents and a dime worth 10 cents, what is the total?', ['15 cents', '15']),
   ('How many cents is one dime worth?', ['10 cents', '10']),
   ('If you have two dimes, how many cents do you have in total?', ['20 cents', '20'])],
  [('A nickel plus a dime equals how many cents?', ['15 cents', '10 cents', '20 cents', '5 cents'], 0),
   ('Two dimes together equal how many cents?', ['20 cents', '10 cents', '15 cents', '25 cents'], 0),
   ('A dime plus a penny equals how many cents?', ['11 cents', '10 cents', '12 cents', '15 cents'], 0),
   ('Which coin is worth the most: a penny, a nickel, or a dime?', ['A dime', 'A penny', 'A nickel', 'They are equal'], 0),
   ('When adding coins together, we find the ___ amount of money.', ['Total', 'Smallest', 'Heaviest', 'Oldest'], 0)])

d62_sci = sub('Science', 'Migration: Animals That Travel with the Seasons',
  'Students learn that migration is when animals, such as some birds, travel long distances to a different place as the seasons change, often to find food or warmer weather.',
  [('What do we call it when animals travel to a new place as seasons change?', ['migration']),
   ('Name one reason animals migrate, like finding food or warmth.', ['to find food', 'to find warmth', 'warmer weather']),
   ('Name one kind of animal that can migrate, like a bird.', ['a bird', 'birds', 'geese'])],
  [('What do we call animals travelling to a new place as the seasons change?', ['Migration', 'Hibernation', 'Camouflage', 'Pollination'], 0),
   ('Why do many animals migrate?', ['To find food or warmer weather', 'To grow new fur', 'To change colour', 'To build a nest only'], 0),
   ('Which of these animals is known for migrating long distances?', ['Geese', 'A pet dog', 'A goldfish in a bowl', 'A house cat'], 0),
   ('Migrating animals often travel toward warmer places during ___.', ['Winter', 'The middle of summer', 'Never', 'Only on sunny days'], 0),
   ('Migration is different from hibernation because migrating animals ___.', ['Travel to a new place instead of sleeping through winter', 'Always sleep all winter', 'Never move at all', 'Change colour instead'], 0)])

d62_ss = sub('SocialStudies', 'Public Transportation: Getting Around Our Community',
  'Students learn that public transportation, such as buses, trains, and subways, helps many people travel around their community together.',
  [('Name one kind of public transportation, like a bus or a train.', ['a bus', 'a train', 'a subway']),
   ('What is public transportation used for?', ['to help people travel', 'getting around the community']),
   ('Can many people ride on a bus at the same time?', ['yes'])],
  [('Which of these is a kind of public transportation?', ['A city bus', 'A single bicycle', 'A backpack', 'A skateboard'], 0),
   ('What is the main purpose of public transportation?', ['To help many people travel around the community', 'To deliver mail', 'To grow food', 'To put out fires'], 0),
   ('Which of these is true about a bus?', ['Many people can ride on it at once', 'Only one person can ever ride it', 'It cannot move', 'It only travels at night'], 0),
   ('Why might a family choose to ride a bus instead of driving a car?', ['It can save money and help the environment', 'Buses never go anywhere useful', 'Cars are always better', 'Buses cannot carry people'], 0),
   ('Which of these is an example of public transportation found in some cities?', ['A subway train', 'A private airplane', 'A rowboat', 'A garden'], 0)])

# ─── DAY 63 ─────────────────────────────────────────────────────────────────
d63_lang = sub('Language', 'Vowel Teams: ue and ew',
  'Students learn that the letters ue and ew can work together as a vowel team to make the long u sound, as in blue and new.',
  [('What two letters make the long u sound in the word blue?', ['ue']),
   ('What two letters make the long u sound in the word new?', ['ew']),
   ('Name one word that has the ew vowel team, like new or grew.', ['new', 'grew', 'few'])],
  [('Which letters make the long u sound in the word blue?', ['ue', 'ew', 'oa', 'ea'], 0),
   ('Which letters make the long u sound in the word new?', ['ew', 'ue', 'ai', 'oy'], 0),
   ('Which word has the ue vowel team?', ['Blue', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ew vowel team?', ['New', 'Cat', 'Dog', 'Sun'], 0),
   ('The ue and ew vowel teams both usually make the ___ sound.', ['Long u', 'Short a', 'Long o', 'Short i'], 0)])

d63_math = sub('Math', 'Fractions: Comparing Halves, Thirds, and Quarters',
  'Students compare fractions such as halves, thirds, and quarters to understand that when a whole is split into more equal parts, each part becomes smaller.',
  [('Which is bigger, one half of a pizza or one quarter of the same pizza?', ['one half', 'half']),
   ('If a shape is cut into more equal parts, do the parts get bigger or smaller?', ['smaller']),
   ('Which fraction shows a whole split into two equal parts?', ['one half', 'a half'])],
  [('Which is bigger, one half of a cake or one quarter of the same cake?', ['One half', 'One quarter', 'They are the same', 'Cannot tell'], 0),
   ('Which is smaller, one third of a sandwich or one half of the same sandwich?', ['One third', 'One half', 'They are the same', 'Cannot tell'], 0),
   ('As a whole is cut into more equal parts, each part gets ___.', ['Smaller', 'Bigger', 'The same size always', 'Heavier'], 0),
   ('Which fraction names a whole split into four equal parts?', ['One quarter', 'One half', 'One third', 'One whole'], 0),
   ('If you and one friend split a sandwich equally, how much does each person get?', ['One half', 'One third', 'One quarter', 'The whole sandwich'], 0)])

d63_sci = sub('Science', 'Trees: Evergreen and Deciduous',
  'Students compare two kinds of trees, evergreen trees that keep their green needles all year, and deciduous trees that lose their leaves in fall.',
  [('What do we call a tree that keeps its green needles all year, like a pine tree?', ['an evergreen tree', 'evergreen']),
   ('What do we call a tree that loses its leaves in fall, like a maple tree?', ['a deciduous tree', 'deciduous']),
   ('Name one kind of evergreen tree, like a pine or spruce.', ['pine', 'spruce', 'fir'])],
  [('What do we call a tree that keeps its green needles all year?', ['An evergreen tree', 'A deciduous tree', 'A flower', 'A vine'], 0),
   ('What do we call a tree that loses its leaves every fall?', ['A deciduous tree', 'An evergreen tree', 'A moss', 'A seed'], 0),
   ('Which of these is an example of an evergreen tree?', ['A pine tree', 'A maple tree', 'An oak tree', 'A birch tree'], 0),
   ('In winter, an evergreen tree usually ___.', ['Stays green with its needles', 'Loses all its needles', 'Turns bright orange', 'Disappears completely'], 0),
   ('A deciduous tree in fall usually ___.', ['Changes colour and drops its leaves', 'Grows new flowers', 'Stays exactly the same', 'Loses its roots'], 0)])

d63_ss = sub('SocialStudies', 'Fair Play and Good Sportsmanship in Games',
  'Students learn that good sportsmanship means following the rules, playing fairly, and being kind to others whether a game is won or lost.',
  [('What do we call playing fairly and being kind during a game?', ['good sportsmanship', 'sportsmanship']),
   ('Should players follow the rules of a game?', ['yes']),
   ('Name one kind thing a player can say after losing a game, like well played.', ['well played', 'good game', 'nice try'])],
  [('What is good sportsmanship?', ['Playing fairly and being kind to others', 'Breaking the rules to win', 'Being unkind to the other team', 'Refusing to share turns'], 0),
   ('What should a player do if their team loses a game?', ['Congratulate the other team and stay kind', 'Yell at teammates', 'Refuse to play again ever', 'Break the game equipment'], 0),
   ('Why is following the rules of a game important?', ['It keeps the game fair for everyone', 'Rules do not matter in games', 'Only the winner needs rules', 'Rules make games boring'], 0),
   ('Which of these shows good sportsmanship?', ['Shaking hands after a game', 'Cheating to win', 'Making fun of the other team', 'Refusing to take turns'], 0),
   ('Good sportsmanship helps a group ___.', ['Have fun and stay friendly during games', 'Argue more often', 'Ignore the rules', 'Play alone always'], 0)])

# ─── DAY 64 ─────────────────────────────────────────────────────────────────
d64_lang = sub('Language', 'Suffixes: -ed and -es',
  'Students learn that the suffixes -ed and -es can be added to the end of a word, with -ed often showing something happened in the past, and -es often showing more than one.',
  [('What suffix can be added to walk to show it happened in the past, like walked?', ['-ed', 'ed']),
   ('What suffix can be added to box to show more than one, like boxes?', ['-es', 'es']),
   ('Name one word that shows the past by ending in -ed, like jumped or played.', ['jumped', 'played', 'walked'])],
  [('Which word shows something happened in the past?', ['Jumped', 'Jump', 'Jumping', 'Jumps'], 0),
   ('Which suffix usually shows more than one, as in foxes or boxes?', ['-es', '-ed', '-ing', '-er'], 0),
   ('Which word correctly adds -ed to show the past tense of walk?', ['Walked', 'Walking', 'Walks', 'Walker'], 0),
   ('Which word correctly adds -es to show more than one bus?', ['Buses', 'Bused', 'Busing', 'Buser'], 0),
   ('A suffix is added to the ___ of a word to change its meaning.', ['End', 'Beginning', 'Middle', 'Nowhere'], 0)])

d64_math = sub('Math', 'Number Bonds to 20',
  'Students practise number bonds to 20, pairs of numbers that add together to make 20, such as 12 and 8, to build strong addition and subtraction skills.',
  [('What number, added to 12, makes 20?', ['8', 'eight']),
   ('What number, added to 15, makes 20?', ['5', 'five']),
   ('What two equal numbers add together to make 20?', ['10 and 10', '10'])],
  [('What number added to 12 makes 20?', ['8', '7', '9', '6'], 0),
   ('What number added to 15 makes 20?', ['5', '4', '6', '3'], 0),
   ('Which pair of numbers adds up to 20?', ['10 and 10', '10 and 5', '9 and 9', '8 and 8'], 0),
   ('What number added to 18 makes 20?', ['2', '1', '3', '4'], 0),
   ('Knowing number bonds to 20 helps us ___.', ['Add and subtract more quickly', 'Forget how to count', 'Only count to 10', 'Draw shapes'], 0)])

d64_sci = sub('Science', 'Fossils: Clues from the Past',
  'Students learn that fossils are the preserved remains or traces of ancient plants and animals, and that scientists study fossils to learn what life was like long ago.',
  [('What do we call the preserved remains or traces of an ancient plant or animal?', ['a fossil', 'fossil']),
   ('Name one place fossils can be found, like in rocks.', ['rocks', 'in the ground', 'in rock layers']),
   ('Do fossils help scientists learn about life long ago?', ['yes'])],
  [('What is a fossil?', ['The preserved remains or traces of an ancient living thing', 'A living animal today', 'A kind of weather', 'A new toy'], 0),
   ('Where are fossils often found?', ['In layers of rock', 'Floating in the sky', 'Inside a refrigerator', 'In a swimming pool'], 0),
   ('Why do scientists study fossils?', ['To learn what life was like long ago', 'To predict tomorrow weather', 'To build new houses', 'To cook food'], 0),
   ('Which of these could become a fossil over a very long time?', ['An ancient dinosaur bone', 'A cloud', 'The sunshine today', 'A rainbow'], 0),
   ('Fossils can show scientists the shape of ___.', ['Ancient plants and animals', 'Modern cars', 'The weather today', 'New buildings'], 0)])

d64_ss = sub('SocialStudies', 'Helping at Home: Chores and Family Responsibilities',
  'Students learn that family members can help at home by doing chores, such as tidying toys or setting the table, and that sharing tasks helps the whole family.',
  [('Name one chore you can do at home, like tidying toys.', ['tidying toys', 'setting the table', 'making the bed']),
   ('Why is it helpful for family members to share chores?', ['it helps the whole family', 'so no one does all the work']),
   ('Is doing a chore an example of a family responsibility?', ['yes'])],
  [('Which of these is an example of a chore at home?', ['Tidying up toys', 'Watching television all day', 'Ignoring a mess', 'Ignoring family members'], 0),
   ('Why is it helpful for everyone in a family to share chores?', ['It helps the whole family and is fair', 'Chores should only be done by one person', 'Sharing chores is never helpful', 'Chores are not important'], 0),
   ('Which of these is a responsibility a child might have at home?', ['Putting away their own toys', 'Driving a car', 'Paying bills', 'Cooking every meal alone'], 0),
   ('Doing chores at home helps children learn to be ___.', ['Responsible and helpful', 'Lazy', 'Unhelpful', 'Careless'], 0),
   ('Which of these shows a family working together at home?', ['Everyone helping to clean up after dinner', 'Only one person ever helping', 'Leaving all messes for someone else', 'Ignoring each other'], 0)])

# ─── DAY 65 ─────────────────────────────────────────────────────────────────
d65_lang = sub('Language', 'Prefixes: pre- and dis-',
  'Students learn that the prefixes pre- and dis- can be added to the beginning of a word to change its meaning, with pre- meaning before and dis- often meaning not or opposite.',
  [('What does the prefix pre- usually mean, as in preview?', ['before']),
   ('What does the prefix dis- usually mean, as in disagree?', ['not', 'opposite', 'not agree']),
   ('Name one word that begins with the prefix pre-, like preview or preheat.', ['preview', 'preheat', 'precut'])],
  [('What does the prefix pre- usually mean?', ['Before', 'After', 'Never', 'Always'], 0),
   ('What does the prefix dis- usually mean?', ['Not or opposite', 'Always', 'More', 'Before'], 0),
   ('Which word means the opposite of agree by using the prefix dis-?', ['Disagree', 'Preagree', 'Agreeing', 'Agreeful'], 0),
   ('Which word means to heat something before using it?', ['Preheat', 'Disheat', 'Reheat only', 'Unheat'], 0),
   ('A prefix is added to the ___ of a word to change its meaning.', ['Beginning', 'End', 'Middle', 'Nowhere'], 0)])

d65_math = sub('Math', 'Skip Counting by 6s',
  'Students practise skip counting by 6s, saying the numbers 6, 12, 18, 24, and so on, to build number sense and recognize patterns.',
  [('What number comes after 6 when skip counting by 6s?', ['12', 'twelve']),
   ('What number comes after 18 when skip counting by 6s?', ['24', 'twenty-four']),
   ('Start at 6 and skip count by 6s two times. What is the second number?', ['12', 'twelve'])],
  [('When skip counting by 6s, what number comes after 6?', ['12', '11', '13', '18'], 0),
   ('When skip counting by 6s, what number comes after 12?', ['18', '17', '19', '24'], 0),
   ('Which of these lists shows skip counting by 6s?', ['6, 12, 18, 24', '6, 8, 10, 12', '6, 9, 12, 15', '5, 10, 15, 20'], 0),
   ('When skip counting by 6s, what number comes after 18?', ['24', '23', '25', '30'], 0),
   ('Skip counting by 6s means we count ___.', ['Every sixth number', 'Every second number', 'Backward only', 'Only odd numbers'], 0)])

d65_sci = sub('Science', 'Shadows: Light and Dark',
  'Students learn that a shadow forms when an object blocks light, and that shadows can change in size and shape depending on where the light comes from.',
  [('What forms when an object blocks light?', ['a shadow', 'shadow']),
   ('Do you need light to make a shadow?', ['yes']),
   ('Name one time of day when your shadow might be very long, like early morning.', ['early morning', 'evening'])],
  [('What is a shadow?', ['A dark shape formed when an object blocks light', 'A bright light', 'A kind of cloud', 'A colour'], 0),
   ('What do you need to make a shadow?', ['Light and an object blocking it', 'Only darkness', 'Only water', 'Only wind'], 0),
   ('Which of these could make a shadow outside?', ['A tree blocking sunlight', 'A cloud with no sun out', 'Complete darkness at night', 'A closed box with no light'], 0),
   ('Shadows can change in size depending on ___.', ['Where the light is coming from', 'The colour of the object', 'The weight of the object', 'The smell of the object'], 0),
   ('At noon when the sun is high overhead, shadows are usually ___.', ['Shorter', 'Longer', 'The same size always', 'Invisible only'], 0)])

d65_ss = sub('SocialStudies', 'Schools Then and Now',
  'Students compare how schools looked and worked long ago with how schools look and work today, noticing changes in buildings, tools, and technology.',
  [('Name one tool students use in school today that was not common long ago, like a computer.', ['a computer', 'computers', 'tablets']),
   ('Long ago, did many students write with a chalkboard and slate instead of computers?', ['yes']),
   ('Name one thing about school that has stayed the same over time, like learning to read.', ['learning to read', 'students', 'teachers'])],
  [('Which tool is commonly used in schools today that was not common long ago?', ['A computer', 'A stone tablet only', 'A quill pen only', 'A chalk slate only'], 0),
   ('Long ago, many students wrote on ___.', ['Small chalkboards called slates', 'Laptops', 'Tablets with screens', 'Smartphones'], 0),
   ('Which of these has likely stayed the same about school over a long time?', ['Students learning to read and write', 'Everyone using computers', 'Everyone wearing the same uniform colour', 'No teachers being needed'], 0),
   ('Comparing schools then and now helps us understand ___.', ['How education has changed over time', 'That schools never change', 'That old schools had computers', 'That reading was invented recently'], 0),
   ('Which of these is an example of a change in schools over time?', ['Using computers instead of only chalkboards', 'Students no longer learning math', 'Teachers no longer teaching', 'Schools closing forever'], 0)])

# ─── DAY 66 ─────────────────────────────────────────────────────────────────
d66_lang = sub('Language', 'Multiple-Meaning Words',
  'Students learn that some words, called multiple-meaning words, have more than one meaning, such as bat, which can be a flying animal or something used to hit a ball.',
  [('Name two different meanings of the word bat.', ['a flying animal and something used to hit a ball', 'animal and sports equipment']),
   ('The word bark can mean the sound a dog makes or the outside of a tree. Name one meaning of bark.', ['a dog sound', 'the outside of a tree', 'tree covering']),
   ('What do we call a word that has more than one meaning?', ['a multiple-meaning word', 'multiple-meaning word'])],
  [('Which word can mean both a flying animal and something used to hit a ball?', ['Bat', 'Cat', 'Sun', 'Cup'], 0),
   ('The word bark can mean the sound a dog makes or ___.', ['The outside covering of a tree', 'A kind of fruit', 'A type of weather', 'A musical instrument'], 0),
   ('The word ring can mean a piece of jewelry or ___.', ['The sound a bell makes', 'A type of animal', 'A kind of food', 'A colour'], 0),
   ('A multiple-meaning word is a word that has ___.', ['More than one meaning', 'Only one meaning', 'No meaning', 'The same spelling as every other word'], 0),
   ('In the sentence, She will watch the clock, the word watch means ___.', ['To look at something', 'A device worn on the wrist only', 'A kind of animal', 'A colour'], 0)])

d66_math = sub('Math', 'Making Equal Groups: Sharing Fairly',
  'Students practise sharing a set of objects into equal groups, learning that dividing items fairly means each group gets the same amount.',
  [('If you share 6 apples equally between 2 friends, how many apples does each friend get?', ['3', 'three']),
   ('If you share 8 stickers equally between 4 friends, how many stickers does each friend get?', ['2', 'two']),
   ('What does it mean to share items fairly into equal groups?', ['each group gets the same amount'])],
  [('If you share 6 apples equally between 2 friends, how many does each friend get?', ['3', '2', '4', '6'], 0),
   ('If you share 8 stickers equally between 4 friends, how many does each friend get?', ['2', '4', '1', '8'], 0),
   ('If you share 10 crayons equally between 5 friends, how many does each friend get?', ['2', '5', '1', '10'], 0),
   ('Sharing items into equal groups means each group has ___.', ['The same amount', 'A different amount', 'No items at all', 'Extra items only'], 0),
   ('If 4 cookies are shared equally between 2 people, each person gets ___ cookies.', ['2', '4', '1', '3'], 0)])

d66_sci = sub('Science', 'Pollination: How Bees Help Flowers Grow',
  'Students learn that bees and other insects help pollinate flowers by carrying pollen from one flower to another, which helps plants make seeds and fruit.',
  [('What do we call the yellow powder that bees carry between flowers?', ['pollen']),
   ('Name one insect that helps pollinate flowers, like a bee.', ['a bee', 'bees', 'a butterfly']),
   ('Does pollination help plants make seeds and fruit?', ['yes'])],
  [('What is pollen?', ['A powder that helps plants make seeds', 'A kind of rock', 'A kind of water', 'A type of animal fur'], 0),
   ('Which insect is well known for helping pollinate flowers?', ['A bee', 'A spider', 'A snail', 'A worm'], 0),
   ('What happens when a bee carries pollen from one flower to another?', ['It helps the plant make seeds and fruit', 'It hurts the flower', 'It stops the flower from growing', 'Nothing happens at all'], 0),
   ('Why are bees important to gardens and farms?', ['They help pollinate many flowers and crops', 'They eat all the plants', 'They only make loud noises', 'They have no role in nature'], 0),
   ('Pollination is an example of how ___.', ['Animals and plants can help each other', 'Animals always harm plants', 'Plants never need animals', 'Bees never visit flowers'], 0)])

d66_ss = sub('SocialStudies', 'Newspapers and News: Learning About Our Community',
  'Students learn that newspapers and news reports share information and stories about events happening in a community, helping people stay informed.',
  [('What do we call a printed paper that shares news and stories about the community?', ['a newspaper', 'newspaper']),
   ('Name one way people can learn news about their community, like reading a newspaper.', ['reading a newspaper', 'watching the news', 'listening to the radio']),
   ('Does news help people stay informed about their community?', ['yes'])],
  [('What is a newspaper?', ['A printed paper that shares news and stories', 'A kind of food', 'A musical instrument', 'A type of clothing'], 0),
   ('Which of these is a way people can learn news about their community?', ['Reading a newspaper', 'Eating breakfast', 'Playing a board game', 'Taking a nap'], 0),
   ('Why is it helpful for people to read or watch the news?', ['It helps them stay informed about their community', 'News is never useful', 'It only shares made-up stories', 'It has no purpose'], 0),
   ('Which of these might a community newspaper report on?', ['A new park opening nearby', 'A story from long ago in another country only', 'Nothing at all', 'Only advertisements'], 0),
   ('Sharing news helps a community by ___.', ['Keeping people informed about important events', 'Keeping everyone confused', 'Hiding information from people', 'Replacing schools'], 0)])

# ─── DAY 67 ─────────────────────────────────────────────────────────────────
d67_lang = sub('Language', 'Author Purpose: To Tell, To Teach, To Entertain',
  'Students learn that authors write for a purpose, such as to tell a story, to teach facts, or to entertain readers, and that noticing the purpose helps readers understand a text.',
  [('If a book teaches you facts about animals, what is the author purpose?', ['to teach', 'to inform']),
   ('If a book makes you laugh with a funny story, what is the author purpose?', ['to entertain']),
   ('Name one reason an author might write a book, like to tell a story.', ['to tell a story', 'to teach', 'to entertain'])],
  [('If a book gives facts about how plants grow, the author purpose is likely to ___.', ['Teach', 'Only entertain with jokes', 'Confuse the reader', 'Sell toys'], 0),
   ('If a book tells a funny made-up story, the author purpose is likely to ___.', ['Entertain', 'Only teach facts', 'Give directions', 'Report weather'], 0),
   ('A recipe book is written mostly to ___.', ['Teach how to make food', 'Entertain with jokes', 'Tell a scary story', 'Share songs'], 0),
   ('Noticing an author purpose helps readers ___.', ['Understand why a text was written', 'Ignore the text completely', 'Skip every page', 'Forget the story'], 0),
   ('Which of these texts is written mostly to entertain?', ['A funny made-up story', 'A set of cooking instructions', 'A weather report', 'A phone book'], 0)])

d67_math = sub('Math', 'Missing Number Addition Sentences',
  'Students solve addition sentences with a missing number, such as 4 add what number equals 9, using known facts and counting strategies.',
  [('What number is missing: 4 add ___ equals 9?', ['5', 'five']),
   ('What number is missing: ___ add 3 equals 10?', ['7', 'seven']),
   ('What number is missing: 6 add ___ equals 6?', ['0', 'zero'])],
  [('What number is missing: 4 add ___ equals 9?', ['5', '4', '6', '3'], 0),
   ('What number is missing: ___ add 3 equals 10?', ['7', '6', '8', '5'], 0),
   ('What number is missing: 2 add ___ equals 8?', ['6', '5', '7', '4'], 0),
   ('What number is missing: ___ add 5 equals 5?', ['0', '1', '5', '10'], 0),
   ('To solve a missing number addition sentence, it helps to ___.', ['Think about what number completes the total', 'Guess with no strategy', 'Skip the problem', 'Always answer zero'], 0)])

d67_sci = sub('Science', 'Farm Animals and How They Help Us',
  'Students learn about common farm animals, such as cows, chickens, and sheep, and how each one provides something useful, such as milk, eggs, or wool.',
  [('Name one farm animal that gives us milk, like a cow.', ['a cow', 'cow']),
   ('Name one farm animal that lays eggs, like a chicken.', ['a chicken', 'chicken']),
   ('Name one farm animal that gives us wool, like a sheep.', ['a sheep', 'sheep'])],
  [('Which farm animal gives us milk?', ['A cow', 'A chicken', 'A sheep', 'A pig'], 0),
   ('Which farm animal lays eggs that people eat?', ['A chicken', 'A cow', 'A sheep', 'A horse'], 0),
   ('Which farm animal gives us wool to make clothing?', ['A sheep', 'A cow', 'A chicken', 'A duck'], 0),
   ('Why are farm animals important to people?', ['They provide foods and materials people use', 'They never help people', 'They only make noise', 'They have no purpose'], 0),
   ('Which of these is a product that comes from a farm animal?', ['Wool from a sheep', 'Sand from a beach', 'Wood from a factory', 'Rain from a cloud'], 0)])

d67_ss = sub('SocialStudies', 'Farmers Markets: Buying Local Food',
  'Students learn that a farmers market is a place where local farmers sell fruits, vegetables, and other foods directly to people in the community.',
  [('What do we call a place where local farmers sell food directly to people?', ['a farmers market', 'farmers market']),
   ('Name one kind of food you might buy at a farmers market, like vegetables.', ['vegetables', 'fruit', 'eggs']),
   ('Do farmers grow the food that is sold at a farmers market?', ['yes'])],
  [('What is a farmers market?', ['A place where local farmers sell food directly to people', 'A place to borrow books', 'A place to mail letters', 'A place to see art'], 0),
   ('Which of these might you buy at a farmers market?', ['Fresh vegetables', 'A library book', 'A postage stamp', 'A museum ticket'], 0),
   ('Why might someone choose to buy food at a farmers market?', ['To support local farmers and get fresh food', 'Farmers markets never sell food', 'To avoid buying any food', 'Farmers markets only sell toys'], 0),
   ('Who usually sells the food at a farmers market?', ['Local farmers', 'Only large factories', 'Only mail carriers', 'Only librarians'], 0),
   ('A farmers market helps connect a community to ___.', ['The local farmers who grow their food', 'The post office', 'The library', 'The museum'], 0)])

# ─── DAY 68 ─────────────────────────────────────────────────────────────────
d68_lang = sub('Language', 'Story Theme: The Lesson of a Story',
  'Students learn that a theme is the underlying lesson or message of a story, something readers can learn or take away after reading.',
  [('What do we call the lesson or message of a story?', ['the theme', 'theme']),
   ('If a story teaches that sharing makes friends happy, what is the theme?', ['sharing is good', 'sharing makes friends happy']),
   ('Do many fables and stories have a theme or lesson?', ['yes'])],
  [('What is the theme of a story?', ['The underlying lesson or message', 'The name of the main character', 'The title of the book', 'The number of pages'], 0),
   ('If a story shows a character learning to be kind, the theme might be about ___.', ['Kindness', 'Counting numbers', 'Weather patterns', 'Cooking'], 0),
   ('Which of these is an example of a story theme?', ['Hard work leads to success', 'The name of a character', 'The colour of the cover', 'The number of chapters'], 0),
   ('Finding the theme of a story helps readers ___.', ['Understand the lesson the author wants to share', 'Forget the story', 'Ignore the characters', 'Skip the ending'], 0),
   ('A fable about a slow but steady turtle winning a race often teaches the theme that ___.', ['Being steady and patient can lead to success', 'Speed always wins', 'Turtles cannot race', 'Rabbits always win'], 0)])

d68_math = sub('Math', 'Measuring Length with a Ruler: Centimetres',
  'Students learn to use a ruler to measure the length of objects in centimetres, lining up the end of the object with the zero mark.',
  [('What tool do we use to measure length in centimetres?', ['a ruler', 'ruler']),
   ('Where should you line up an object when measuring with a ruler?', ['the zero mark', 'zero']),
   ('What unit do we often use with a ruler to measure short objects?', ['centimetres', 'centimetre'])],
  [('What tool is used to measure the length of an object in centimetres?', ['A ruler', 'A clock', 'A scale', 'A thermometer'], 0),
   ('When measuring with a ruler, where should the object line up?', ['The zero mark', 'The middle of the ruler', 'The very end of the ruler', 'Anywhere at all'], 0),
   ('Which unit is commonly used with a ruler to measure a pencil?', ['Centimetres', 'Kilograms', 'Litres', 'Hours'], 0),
   ('If a crayon measures 8 centimetres and a marker measures 12 centimetres, which is longer?', ['The marker', 'The crayon', 'They are the same length', 'Cannot tell'], 0),
   ('Using a ruler helps us find the exact ___ of an object.', ['Length', 'Colour', 'Weight', 'Sound'], 0)])

d68_sci = sub('Science', 'Endangered Animals: Protecting Wildlife',
  'Students learn that some animals are endangered, meaning very few of them are left, and that people can help protect these animals by caring for their habitats.',
  [('What do we call an animal that has very few left in the wild?', ['an endangered animal', 'endangered']),
   ('Name one way people can help protect endangered animals, like caring for their habitat.', ['caring for their habitat', 'protecting their homes', 'not littering']),
   ('Should people try to protect animals that are endangered?', ['yes'])],
  [('What does it mean when an animal is endangered?', ['Very few of that animal are left in the wild', 'There are too many of that animal', 'The animal is very common', 'The animal lives only in zoos'], 0),
   ('Which of these can help protect endangered animals?', ['Taking care of their natural habitats', 'Littering in their homes', 'Ignoring their needs', 'Cutting down all their trees'], 0),
   ('Why is it important to protect endangered animals?', ['So they do not disappear forever', 'They are not important', 'So there are more of them to catch', 'It does not matter at all'], 0),
   ('Which of these might cause an animal to become endangered?', ['Losing its natural habitat', 'Having plenty of food and space', 'Living somewhere safe', 'Having many babies safely'], 0),
   ('People who work to protect endangered animals and their homes are helping ___.', ['Wildlife survive for the future', 'Nothing important', 'Only themselves', 'No one'], 0)])

d68_ss = sub('SocialStudies', 'Community Gardens: Growing Food Together',
  'Students learn that a community garden is a shared space where neighbours can grow vegetables, fruits, and flowers together.',
  [('What do we call a shared space where neighbours grow food together?', ['a community garden', 'community garden']),
   ('Name one thing people might grow in a community garden, like vegetables.', ['vegetables', 'fruit', 'flowers']),
   ('Do community gardens help neighbours work together?', ['yes'])],
  [('What is a community garden?', ['A shared space where neighbours grow food together', 'A place to buy toys', 'A place to mail letters', 'A place to see movies'], 0),
   ('Which of these might be grown in a community garden?', ['Vegetables and flowers', 'Cars', 'Books only', 'Furniture'], 0),
   ('How does a community garden help neighbours?', ['It brings people together to grow food and share work', 'It keeps neighbours apart', 'It has no benefit', 'It only helps one person'], 0),
   ('Which of these is a benefit of growing your own vegetables in a garden?', ['Fresh food and learning how plants grow', 'No benefit at all', 'Less fresh food', 'More pollution'], 0),
   ('Working together in a community garden is an example of ___.', ['Cooperation and teamwork', 'Ignoring others', 'Working alone always', 'Wasting time'], 0)])

# ─── DAY 69 ─────────────────────────────────────────────────────────────────
d69_lang = sub('Language', 'Using Context Clues to Find Word Meaning',
  'Students learn to use context clues, hints from the words and sentences around an unknown word, to figure out what that word means.',
  [('What do we call hints from nearby words that help us understand an unknown word?', ['context clues', 'context clue']),
   ('If a sentence says the huge elephant was bigger than a car, what does huge likely mean?', ['very big', 'big']),
   ('Do good readers use context clues to figure out new words?', ['yes'])],
  [('What are context clues?', ['Hints from nearby words that help explain an unknown word', 'A type of punctuation', 'A kind of picture only', 'A math symbol'], 0),
   ('If a sentence says the frigid winter wind made everyone shiver and wear coats, what does frigid likely mean?', ['Very cold', 'Very warm', 'Very loud', 'Very colourful'], 0),
   ('If a story says the puppy was famished and gobbled up its food quickly, what does famished likely mean?', ['Very hungry', 'Very tired', 'Very happy', 'Very cold'], 0),
   ('Using context clues helps readers ___.', ['Understand new words without a dictionary', 'Ignore new words completely', 'Skip every sentence', 'Forget the story'], 0),
   ('If a sentence says the tiny ant was much smaller than the beetle, what does tiny likely mean?', ['Very small', 'Very large', 'Very loud', 'Very fast'], 0)])

d69_math = sub('Math', 'Position and Movement: Turns and Slides',
  'Students learn simple ways shapes and objects can move, such as a slide, which moves an object in a straight direction, and a turn, which rotates an object around a point.',
  [('What do we call moving a shape in a straight direction without turning it?', ['a slide', 'slide']),
   ('What do we call rotating a shape around a point?', ['a turn', 'turn']),
   ('If you slide a toy car across a table, does it turn or move straight?', ['it moves straight', 'straight'])],
  [('What do we call moving a shape in a straight direction without turning it?', ['A slide', 'A turn', 'A flip', 'A stop'], 0),
   ('What do we call rotating a shape around a point?', ['A turn', 'A slide', 'A stack', 'A stretch'], 0),
   ('Which movement describes spinning a pinwheel around its centre?', ['A turn', 'A slide', 'A grow', 'A shrink'], 0),
   ('Which movement describes pushing a book straight across a desk?', ['A slide', 'A turn', 'A spin', 'A bounce'], 0),
   ('Learning about slides and turns helps us describe how shapes ___.', ['Move in space', 'Change colour', 'Change size only', 'Disappear'], 0)])

d69_sci = sub('Science', 'Simple Weather Tools: Thermometers and Rain Gauges',
  'Students learn about simple tools used to measure weather, such as a thermometer that measures temperature and a rain gauge that measures how much rain has fallen.',
  [('What tool measures how hot or cold it is outside?', ['a thermometer', 'thermometer']),
   ('What tool measures how much rain has fallen?', ['a rain gauge', 'rain gauge']),
   ('Do weather tools help us understand and record the weather?', ['yes'])],
  [('What tool measures how hot or cold it is outside?', ['A thermometer', 'A rain gauge', 'A ruler', 'A clock'], 0),
   ('What tool measures how much rain has fallen?', ['A rain gauge', 'A thermometer', 'A compass', 'A scale'], 0),
   ('Why do people use weather tools like thermometers?', ['To measure and record the weather accurately', 'To measure the length of objects', 'To tell time', 'To weigh objects'], 0),
   ('If a thermometer shows a high number, the weather is likely ___.', ['Hot', 'Cold', 'Snowy', 'Foggy'], 0),
   ('A rain gauge would be most useful for measuring weather during ___.', ['A rainy day', 'A sunny day with no rain', 'A clear night', 'A windy day with no rain'], 0)])

d69_ss = sub('SocialStudies', 'Banks: A Safe Place to Save Money',
  'Students learn that a bank is a safe place where people can keep and save their money, and that saving money can help people pay for things later.',
  [('What do we call a safe place where people can keep and save money?', ['a bank', 'bank']),
   ('Why might someone save money at a bank?', ['to keep it safe', 'to use it later']),
   ('Can saving money help you buy something later?', ['yes'])],
  [('What is a bank?', ['A safe place where people can keep and save money', 'A place to buy groceries', 'A place to mail letters', 'A place to borrow books'], 0),
   ('Why might a person choose to save money at a bank?', ['To keep it safe and use it later', 'Banks never keep money safe', 'To lose their money', 'Banks only sell food'], 0),
   ('Which of these is an example of saving money?', ['Putting some money aside instead of spending it all', 'Spending every coin right away', 'Throwing money away', 'Losing money on purpose'], 0),
   ('Saving money at a bank can help someone ___.', ['Pay for something they want later', 'Never buy anything again', 'Lose track of their money', 'Avoid ever using money'], 0),
   ('Which of these might someone save money for?', ['A special toy or trip in the future', 'Nothing at all', 'Throwing it away', 'Losing it'], 0)])

# ─── DAY 70 (Review) ────────────────────────────────────────────────────────
d70_lang = sub('Language', 'Language Review: Blends, Vowel Teams, and Word Meaning',
  'Students review recent Language skills: consonant blends, vowel teams, suffixes, prefixes, multiple-meaning words, author purpose, story theme, and context clues.',
  [('What two letters begin the word twin?', ['tw']),
   ('What two letters make the vowel sound in the middle of the word coin?', ['oi']),
   ('What do we call the lesson or message of a story?', ['the theme', 'theme'])],
  [('Which word begins with the sc blend?', ['Scarf', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the oi vowel team?', ['Coin', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word correctly adds -ed to show the past tense of walk?', ['Walked', 'Walking', 'Walks', 'Walker'], 0),
   ('Which word can mean both a flying animal and something used to hit a ball?', ['Bat', 'Cat', 'Sun', 'Cup'], 0),
   ('What is the theme of a story?', ['The underlying lesson or message', 'The name of the main character', 'The title of the book', 'The number of pages'], 0)])

d70_math = sub('Math', 'Math Review: Time, Money, Fractions, and Measurement',
  'Students review recent Math skills: days and months, adding coins, comparing fractions, number bonds to 20, skip counting by 6s, equal groups, missing number sentences, measuring length, and turns and slides.',
  [('How many days are in one week?', ['7', 'seven']),
   ('What number, added to 12, makes 20?', ['8', 'eight']),
   ('What tool do we use to measure length in centimetres?', ['a ruler', 'ruler'])],
  [('How many days are in one week?', ['7', '5', '6', '10'], 0),
   ('A nickel plus a dime equals how many cents?', ['15 cents', '10 cents', '20 cents', '5 cents'], 0),
   ('Which is bigger, one half of a cake or one quarter of the same cake?', ['One half', 'One quarter', 'They are the same', 'Cannot tell'], 0),
   ('When skip counting by 6s, what number comes after 6?', ['12', '11', '13', '18'], 0),
   ('What tool is used to measure the length of an object in centimetres?', ['A ruler', 'A clock', 'A scale', 'A thermometer'], 0)])

d70_sci = sub('Science', 'Science Review: Creatures, Plants, and Weather',
  'Students review recent Science topics: spiders, migration, evergreen and deciduous trees, fossils, shadows, pollination, farm animals, endangered animals, and weather tools.',
  [('How many legs does a spider have?', ['8', 'eight']),
   ('What do we call it when animals travel to a new place as seasons change?', ['migration']),
   ('What tool measures how hot or cold it is outside?', ['a thermometer', 'thermometer'])],
  [('How many legs does a spider have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
   ('What do we call animals travelling to a new place as the seasons change?', ['Migration', 'Hibernation', 'Camouflage', 'Pollination'], 0),
   ('What do we call a tree that keeps its green needles all year?', ['An evergreen tree', 'A deciduous tree', 'A flower', 'A vine'], 0),
   ('What is pollen?', ['A powder that helps plants make seeds', 'A kind of rock', 'A kind of water', 'A type of animal fur'], 0),
   ('What does it mean when an animal is endangered?', ['Very few of that animal are left in the wild', 'There are too many of that animal', 'The animal is very common', 'The animal lives only in zoos'], 0)])

d70_ss = sub('SocialStudies', 'Social Studies Review: Community, Money, and Cooperation',
  'Students review recent Social Studies topics: weather and clothing, public transportation, sportsmanship, chores at home, schools then and now, newspapers, farmers markets, community gardens, and banks.',
  [('Name one piece of clothing you might wear on a cold winter day, like a coat.', ['a coat', 'mittens', 'a hat', 'boots']),
   ('What do we call a place where local farmers sell food directly to people?', ['a farmers market', 'farmers market']),
   ('What do we call a safe place where people can keep and save money?', ['a bank', 'bank'])],
  [('Which clothing would be best on a cold winter day?', ['A warm coat and mittens', 'Shorts and sandals', 'A swimsuit', 'A sun hat only'], 0),
   ('What is the main purpose of public transportation?', ['To help many people travel around the community', 'To deliver mail', 'To grow food', 'To put out fires'], 0),
   ('What is good sportsmanship?', ['Playing fairly and being kind to others', 'Breaking the rules to win', 'Being unkind to the other team', 'Refusing to share turns'], 0),
   ('What is a farmers market?', ['A place where local farmers sell food directly to people', 'A place to borrow books', 'A place to mail letters', 'A place to see art'], 0),
   ('What is a bank?', ['A safe place where people can keep and save money', 'A place to buy groceries', 'A place to mail letters', 'A place to borrow books'], 0)])


g1_61_70 = [
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
    _rebalance_answer_positions(g1_61_70)
    append_worksheet_days(1, g1_61_70)
