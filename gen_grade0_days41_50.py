#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 41-50 -- second batch extending Grade 0 past
the Days 31-40 batch. This is a self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to() helpers, since those do not
support a worksheet field) modeled exactly on gen_grade0_days31_40.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-40 topics (see data/grade0.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely for
kindergarten readability and to keep the generated .ts string literals
valid.
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


def _rebalance_answer_positions(days, seed=20260821):
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


# ─── DAY 41 ─────────────────────────────────────────────────────────────────
d41_lang = sub('Language', 'Blending Sounds: Putting Sounds Together',
  'Students practise blending separate sounds together to form a whole word, such as combining the sounds s, u, n to say sun, building an important pre-reading skill.',
  [('Blend the sounds s, u, n together. What word do they make?', ['sun']),
   ('Blend the sounds h, a, t together. What word do they make?', ['hat']),
   ('Blend the sounds d, o, g together. What word do they make?', ['dog'])],
  [('When you blend the sounds c, a, t, what word do you make?', ['Cap', 'Cat', 'Can', 'Cot'], 1),
   ('Blending sounds means to ___.', ['Take a word apart', 'Put sounds together to make a word', 'Draw a picture', 'Sing a song'], 1),
   ('What word do the sounds r, u, n blend to make?', ['Run', 'Rat', 'Rug', 'Ran'], 0),
   ('Blending sounds helps us ___.', ['Learn to read words', 'Learn to swim', 'Learn to paint', 'Learn to count'], 0),
   ('What word do the sounds p, i, g blend to make?', ['Pit', 'Pig', 'Pin', 'Peg'], 1)])

d41_math = sub('Math', 'Addition to 20',
  'Students extend their addition skills to sums within 20, using objects, fingers, or pictures to add two numbers together.',
  [('12 + 3 = ?', ['15', 'fifteen']),
   ('9 + 8 = ?', ['17', 'seventeen']),
   ('10 + 10 = ?', ['20', 'twenty'])],
  [('11 + 4 = ?', ['14', '15', '16', '13'], 1),
   ('7 + 9 = ?', ['15', '16', '17', '18'], 2),
   ('10 + 6 = ?', ['15', '16', '17', '14'], 1),
   ('13 + 5 = ?', ['17', '18', '19', '16'], 1),
   ('8 + 8 = ?', ['14', '15', '16', '17'], 2)])

d41_sci = sub('Science', 'Life Cycle of a Plant: Seed to Flower',
  'Students learn the stages a plant goes through, starting as a small seed, sprouting into a seedling, and growing into a full plant that may bloom with flowers.',
  [('What is the first stage of a plant life cycle, before it sprouts?', ['seed']),
   ('What does a seed need to grow, like water and sunlight?', ['water', 'sunlight', 'sun', 'soil']),
   ('What grows on some plants at the end of their life cycle, like a rose?', ['flower', 'flowers'])],
  [('What is the first stage of a plant life cycle?', ['Flower', 'Seed', 'Sprout', 'Root'], 1),
   ('What does a seed need to grow into a plant?', ['Only darkness', 'Water and sunlight', 'Only cold air', 'Nothing at all'], 1),
   ('After a seed sprouts, a tiny young plant with leaves is called a ___.', ['Seedling', 'Flower', 'Root', 'Petal'], 0),
   ('What often grows at the top of a fully grown plant?', ['Roots', 'Flowers', 'Seeds only', 'Soil'], 1),
   ('Where do plant roots usually grow?', ['In the air', 'Under the soil', 'On leaves', 'On flowers'], 1)])

d41_ss = sub('SocialStudies', 'Jobs People Do: Different Kinds of Work',
  'Students explore different jobs people do in their community, such as chef, farmer, artist, and pilot, and talk about the work each job involves.',
  [('Who cooks food at a restaurant?', ['chef', 'cook']),
   ('Who flies an airplane?', ['pilot']),
   ('Name one job a person can do, like teacher or farmer.', ['teacher', 'farmer', 'doctor', 'chef', 'pilot', 'artist', 'nurse'])],
  [('Who cooks meals at a restaurant?', ['Pilot', 'Chef', 'Farmer', 'Artist'], 1),
   ('Who flies an airplane?', ['Chef', 'Pilot', 'Teacher', 'Farmer'], 1),
   ('A farmer job includes ___.', ['Flying planes', 'Growing crops and raising animals', 'Painting pictures', 'Teaching math'], 1),
   ('What does an artist do?', ['Creates paintings or drawings', 'Flies planes', 'Cooks food', 'Grows crops'], 0),
   ('Why do people have different jobs?', ['So our community works well with many different tasks done', 'Jobs are not important', 'Everyone does the same job', 'Only adults need jobs'], 0)])

# ─── DAY 42 ─────────────────────────────────────────────────────────────────
d42_lang = sub('Language', 'Compound Words: Two Words Become One',
  'Students learn that some words are made by joining two smaller words together, such as sun and flower joining to make sunflower.',
  [('Sun plus flower makes which word?', ['sunflower']),
   ('Rain plus bow makes which word?', ['rainbow']),
   ('Butter plus fly makes which word?', ['butterfly'])],
  [('Which two words join to make sunflower?', ['Sun and flower', 'Moon and flower', 'Sun and star', 'Rain and flower'], 0),
   ('What do rain and bow join to make?', ['Rainbow', 'Raincoat', 'Bowtie', 'Rainfall'], 0),
   ('A compound word is made of ___.', ['One long letter', 'Two smaller words joined together', 'A picture', 'A number'], 1),
   ('Which two words join to make butterfly?', ['Bird and fly', 'Butter and fly', 'Bug and fly', 'Bee and fly'], 1),
   ('What do bed and room join to make?', ['Bedroom', 'Bedtime', 'Bedsheet', 'Bunkbed'], 0)])

d42_math = sub('Math', 'Subtraction to 20',
  'Students extend their subtraction skills to numbers within 20, taking one number away from another using objects or pictures.',
  [('18 - 5 = ?', ['13', 'thirteen']),
   ('20 - 10 = ?', ['10', 'ten']),
   ('15 - 6 = ?', ['9', 'nine'])],
  [('16 - 4 = ?', ['11', '12', '13', '10'], 1),
   ('20 - 8 = ?', ['11', '12', '13', '14'], 1),
   ('14 - 7 = ?', ['6', '7', '8', '9'], 1),
   ('19 - 9 = ?', ['8', '9', '10', '11'], 2),
   ('12 - 5 = ?', ['6', '7', '8', '9'], 1)])

d42_sci = sub('Science', 'Animal Habitats: Where Animals Live',
  'Students learn that a habitat is the place where an animal lives, and explore different habitats such as forests, oceans, and deserts.',
  [('What word means the place where an animal lives?', ['habitat']),
   ('Name a habitat where a fish lives.', ['ocean', 'water', 'pond', 'lake', 'sea']),
   ('Name a habitat where a bear might live.', ['forest', 'woods'])],
  [('What is a habitat?', ['A type of food', 'The place where an animal lives', 'A type of toy', 'A season'], 1),
   ('Where do fish usually live?', ['In a forest', 'In water', 'In a desert', 'In the sky'], 1),
   ('Which animal is most likely to live in a forest?', ['A bear', 'A fish', 'A camel', 'A whale'], 0),
   ('Which habitat is very hot and dry with little water?', ['Ocean', 'Forest', 'Desert', 'Pond'], 2),
   ('Why do different animals live in different habitats?', ['Each habitat gives the food and shelter that animal needs', 'Animals do not need homes', 'All animals live in the same place', 'Habitats do not matter to animals'], 0)])

d42_ss = sub('SocialStudies', 'Indigenous Peoples: The First Peoples of Canada',
  'Students learn that Indigenous Peoples were the first people to live in what is now Canada, and explore some of their traditions, such as storytelling and caring for the land.',
  [('Who were the first people to live in Canada?', ['indigenous peoples', 'indigenous people', 'first nations']),
   ('Name one way Indigenous Peoples traditionally shared knowledge, like through stories.', ['stories', 'storytelling']),
   ('Indigenous Peoples traditionally cared deeply for the ___.', ['land', 'earth', 'nature'])],
  [('Who were the first people to live in what is now Canada?', ['European settlers', 'Indigenous Peoples', 'Astronauts', 'Pilots'], 1),
   ('Indigenous Peoples have traditionally shared their history and lessons through ___.', ['Storytelling', 'Television', 'Video games', 'Newspapers only'], 0),
   ('Many Indigenous traditions show great respect and care for ___.', ['Cars', 'The land and nature', 'Money', 'Buildings'], 1),
   ('Learning about Indigenous Peoples helps us understand ___.', ['Nothing important', 'The history and cultures of the first peoples of Canada', 'Only modern cities', 'Only farming'], 1),
   ('Which is an example of an Indigenous tradition mentioned in this lesson?', ['Storytelling', 'Flying airplanes', 'Building skyscrapers', 'Playing video games'], 0)])

# ─── DAY 43 ─────────────────────────────────────────────────────────────────
d43_lang = sub('Language', 'Question Words: Who, What, and Where',
  'Students learn common question words, including who, what, and where, and practise using them to ask about people, things, and places.',
  [('Which question word asks about a person?', ['who']),
   ('Which question word asks about a place?', ['where']),
   ('Which question word asks about a thing?', ['what'])],
  [('Which question word would you use to ask about a person, like your teacher?', ['What', 'Who', 'Where', 'When'], 1),
   ('Which question word would you use to ask about a place, like the park?', ['Who', 'What', 'Where', 'Why'], 2),
   ('Which question word would you use to ask about a thing, like a toy?', ['Who', 'What', 'Where', 'When'], 1),
   ('Where is my hat is an example of a question asking about a ___.', ['Person', 'Place', 'Colour', 'Sound'], 1),
   ('Who is your friend is an example of a question asking about a ___.', ['Place', 'Person', 'Thing', 'Time'], 1)])

d43_math = sub('Math', 'Skip Counting by 10s to 100',
  'Students practise skip counting by tens, saying 10, 20, 30, and so on up to 100, to build number sense for larger numbers.',
  [('Skip count by tens: 10, 20, 30, then what number?', ['40', 'forty']),
   ('Skip count by tens: 60, 70, then what number?', ['80', 'eighty']),
   ('What number comes right before 100 when counting by tens?', ['90', 'ninety'])],
  [('Skip count by tens: 10, 20, then what number?', ['25', '30', '40', '21'], 1),
   ('Skip count by tens: 50, 60, 70, then what number?', ['71', '75', '80', '90'], 2),
   ('What number comes after 90 when counting by tens?', ['91', '95', '100', '110'], 2),
   ('Counting by tens to 100 uses how many number words?', ['5', '10', '20', '100'], 1),
   ('Skip count by tens: 30, 40, then what number?', ['41', '45', '50', '60'], 2)])

d43_sci = sub('Science', 'Nocturnal Animals: Awake at Night',
  'Students learn that some animals, called nocturnal animals, sleep during the day and are awake at night, such as owls and bats.',
  [('What word describes animals that are awake at night and sleep during the day?', ['nocturnal']),
   ('Name one nocturnal animal, like an owl or bat.', ['owl', 'bat', 'raccoon']),
   ('Are nocturnal animals awake during the day or at night?', ['night', 'at night'])],
  [('What does nocturnal mean?', ['Awake during the day', 'Awake at night and asleep during the day', 'Never sleeping', 'Only found in water'], 1),
   ('Which of these is a nocturnal animal?', ['Owl', 'Chicken', 'Cow', 'Rooster'], 0),
   ('Bats are nocturnal, which means they are most active ___.', ['In the morning', 'At night', 'At noon', 'Underwater'], 1),
   ('Why might nocturnal animals have very good hearing or eyesight in the dark?', ['To help them find food and stay safe at night', 'It does not help them at all', 'They never need to see or hear', 'Only daytime animals need senses'], 0),
   ('Which of these animals is usually awake during the day instead of at night?', ['Owl', 'Bat', 'Rooster', 'Raccoon'], 2)])

d43_ss = sub('SocialStudies', 'Landmarks: Special Places in Our Community',
  'Students learn about landmarks, special and well known places in a community such as a library, a park, or a city hall.',
  [('What word means a special, well known place in a community?', ['landmark']),
   ('Name one landmark you might visit, like a library or park.', ['library', 'park', 'city hall', 'museum']),
   ('Why are landmarks important to a community?', ['they are special places', 'people gather there', 'important places'])],
  [('What is a landmark?', ['A type of food', 'A special, well known place in a community', 'A kind of weather', 'A math tool'], 1),
   ('Which of these is an example of a landmark?', ['A library', 'A sock', 'A pencil', 'A cloud'], 0),
   ('Why might a community build a park as a landmark?', ['So people have a special place to play and gather', 'Parks are not useful', 'To block traffic', 'To grow only weeds'], 0),
   ('A city hall is a landmark where ___.', ['Community leaders work', 'Only animals live', 'Food is grown', 'Cars are repaired'], 0),
   ('Landmarks help people in a community ___.', ['Get lost more easily', 'Recognize and gather in special shared places', 'Avoid each other', 'Forget their town'], 1)])

# ─── DAY 44 ─────────────────────────────────────────────────────────────────
d44_lang = sub('Language', 'Sequencing Words: First, Next, and Last',
  'Students learn to use sequencing words such as first, next, and last to describe the order in which things happen.',
  [('Which sequencing word describes what happens at the very beginning?', ['first']),
   ('Which sequencing word describes what happens at the very end?', ['last']),
   ('Which sequencing word can describe something that happens after first?', ['next'])],
  [('Which word describes what happens at the very beginning of an event?', ['Last', 'Next', 'First', 'Then'], 2),
   ('Which word describes what happens at the very end of an event?', ['First', 'Last', 'Next', 'Before'], 1),
   ('If you brush your teeth, then eat breakfast, then go to school, what happens right after brushing your teeth?', ['Go to school', 'Eat breakfast', 'Brush teeth again', 'Sleep'], 1),
   ('Sequencing words help us understand ___.', ['The order that things happen in', 'Colours', 'Shapes', 'Weather'], 0),
   ('Which word could describe something happening in the middle of an order of events?', ['First', 'Next', 'Last', 'Before all'], 1)])

d44_math = sub('Math', 'Money: Recognizing Coins',
  'Students explore Canadian coins, including the penny, nickel, dime, and quarter, and practise recognizing them by their size and appearance.',
  [('Name the smallest value Canadian coin, worth one cent.', ['penny']),
   ('Name the coin worth five cents.', ['nickel']),
   ('Name the coin worth twenty five cents.', ['quarter'])],
  [('Which coin is worth five cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 1),
   ('Which coin is worth ten cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 2),
   ('Which coin is worth twenty five cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 3),
   ('A penny is worth ___ cent.', ['One', 'Five', 'Ten', 'Twenty five'], 0),
   ('Which coin has the smallest value?', ['Quarter', 'Dime', 'Nickel', 'Penny'], 3)])

d44_sci = sub('Science', 'Our Body: Bones and Muscles',
  'Students learn that bones give our body its shape and support, while muscles help our body move.',
  [('What body part gives our body its shape and support?', ['bones', 'bone']),
   ('What body part helps our body move?', ['muscles', 'muscle']),
   ('Name one bone in your body, like in your arm or leg.', ['arm bone', 'leg bone', 'skull', 'rib', 'bone'])],
  [('What gives our body its shape and support?', ['Muscles', 'Bones', 'Skin', 'Hair'], 1),
   ('What helps our body move, like when we run or jump?', ['Bones', 'Muscles', 'Nails', 'Hair'], 1),
   ('Where are bones found in your body?', ['Only in your head', 'All throughout your body', 'Only in your feet', 'They are not in the body'], 1),
   ('Why is it important to keep our bones and muscles healthy?', ['It is not important', 'So our body can grow strong and move well', 'Only athletes need healthy bones', 'Bones do not need care'], 1),
   ('Which activity helps keep muscles strong?', ['Sitting all day', 'Exercise like running and jumping', 'Sleeping all day', 'Watching television only'], 1)])

d44_ss = sub('SocialStudies', 'Money: Trading and Buying',
  'Students learn that people use money to buy things they need or want, and that trading means exchanging one thing for another.',
  [('What do people use to buy things at a store?', ['money']),
   ('What word means exchanging one thing for another?', ['trading', 'trade']),
   ('Name one place where people use money to buy things.', ['store', 'market', 'shop'])],
  [('What do people use to buy food and toys at a store?', ['Leaves', 'Money', 'Rocks', 'Water'], 1),
   ('What does trading mean?', ['Throwing things away', 'Exchanging one thing for another', 'Hiding your things', 'Painting pictures'], 1),
   ('Where might a family use money to buy groceries?', ['At a store', 'At the playground', 'At the library only', 'In the sky'], 0),
   ('Long ago, before money, some people traded items directly. This is called ___.', ['Bartering', 'Painting', 'Singing', 'Reading'], 0),
   ('Why do people need money or trading?', ['To get things they need or want', 'It is not needed', 'Only adults care about it', 'To make noise'], 0)])

# ─── DAY 45 ─────────────────────────────────────────────────────────────────
d45_lang = sub('Language', 'Writing: Labels for Pictures',
  'Students practise writing simple labels, like one word or a short phrase, to describe a picture they have drawn.',
  [('If you draw a picture of a cat, what simple label could you write under it?', ['cat']),
   ('If you draw a picture of the sun, what simple label could you write?', ['sun']),
   ('Why do we add labels to pictures?', ['to describe them', 'to tell what it is', 'to explain the picture'])],
  [('A label under a picture usually tells us ___.', ['What the picture shows', 'A math problem', 'A song', 'Nothing at all'], 0),
   ('If you draw a dog, a good label would be ___.', ['Cat', 'Dog', 'Sun', 'Tree'], 1),
   ('Why do writers add labels to their pictures?', ['To help explain what the picture shows', 'To make the picture messy', 'Labels are not helpful', 'Only for adults'], 0),
   ('A label is usually ___.', ['A very long story', 'A short word or phrase', 'A whole book', 'A song'], 1),
   ('If you draw the sun, a good label would be ___.', ['Moon', 'Star', 'Sun', 'Cloud'], 2)])

d45_math = sub('Math', 'Growing Patterns: Patterns That Change',
  'Students explore growing patterns, where the pattern increases by a set amount each time, such as one block, two blocks, three blocks.',
  [('If a growing pattern goes 1, 2, 3, what comes next?', ['4', 'four']),
   ('In a growing pattern of shapes with 1 circle, then 2 circles, then 3 circles, how many circles come next?', ['4', 'four']),
   ('Does a growing pattern get bigger or stay the same each time?', ['bigger', 'gets bigger'])],
  [('In a growing pattern, the amount ___ each time.', ['Stays the same', 'Increases', 'Decreases', 'Disappears'], 1),
   ('If a growing pattern shows 1 block, 2 blocks, 3 blocks, how many blocks come next?', ['3', '4', '5', '1'], 1),
   ('Which is an example of a growing pattern?', ['1 star every time with no change', 'Sets that grow: 2 stars, then 3 stars, then 4 stars', 'Red, blue, red, blue repeating', 'The same shape every time'], 1),
   ('A growing pattern of 2, 4, 6 continues with ___.', ['7', '8', '9', '10'], 1),
   ('In a growing pattern that adds one more shape each time, if it starts with 2 shapes, the next step has ___.', ['1 shape', '2 shapes', '3 shapes', '5 shapes'], 2)])

d45_sci = sub('Science', 'Weather Tools: Measuring Rain and Temperature',
  'Students learn about simple weather tools, such as a rain gauge to measure rainfall and a thermometer to measure temperature.',
  [('What tool measures how hot or cold it is outside?', ['thermometer']),
   ('What tool measures how much rain has fallen?', ['rain gauge']),
   ('Would we use a thermometer to check temperature or to check the time?', ['temperature'])],
  [('What tool measures temperature?', ['Rain gauge', 'Thermometer', 'Ruler', 'Scale'], 1),
   ('What tool measures how much rain has fallen?', ['Thermometer', 'Rain gauge', 'Clock', 'Compass'], 1),
   ('If the thermometer shows a high number, the weather is likely ___.', ['Cold', 'Hot', 'Snowy', 'Foggy'], 1),
   ('Why do people use weather tools?', ['To measure and understand the weather', 'They are only toys', 'Weather cannot be measured', 'To make noise'], 0),
   ('A rain gauge is usually shaped like a ___.', ['Cube', 'Tall narrow container', 'Flat circle', 'Triangle'], 1)])

d45_ss = sub('SocialStudies', 'Sharing and Taking Turns',
  'Students learn the importance of sharing toys and materials, and taking turns, when playing and working with others.',
  [('What word means letting someone else use something you have?', ['sharing', 'share']),
   ('What word means waiting for your chance to do something?', ['taking turns', 'turn']),
   ('Why is sharing important when playing with friends?', ['it is kind', 'everyone gets a turn', 'it is fair'])],
  [('What does it mean to share?', ['Keeping everything for yourself', 'Letting others use or have some of what you have', 'Hiding your toys', 'Ignoring friends'], 1),
   ('What does taking turns mean?', ['Always going first', 'Waiting for your chance after someone else', 'Never playing', 'Playing alone forever'], 1),
   ('Why is sharing a kind thing to do?', ['It helps everyone feel included and happy', 'It is not kind', 'It makes others sad', 'It has no effect'], 0),
   ('If two children want the same toy, a good solution is to ___.', ['Fight over it', 'Take turns using it', 'Break it', 'Hide it from the other child'], 1),
   ('Sharing and taking turns help us ___.', ['Be good friends and get along with others', 'Avoid all friends', 'Never play together', 'Make others upset'], 0)])

# ─── DAY 46 ─────────────────────────────────────────────────────────────────
d46_lang = sub('Language', 'Nouns: Naming People, Places, and Things',
  'Students learn that a noun is a word that names a person, place, or thing, such as teacher, school, or ball.',
  [('Is the word teacher a noun that names a person, place, or thing?', ['person']),
   ('Is the word school a noun that names a person, place, or thing?', ['place']),
   ('Is the word ball a noun that names a person, place, or thing?', ['thing'])],
  [('What is a noun?', ['A word that names a person, place, or thing', 'A colour', 'A number', 'A feeling only'], 0),
   ('Which word is a noun that names a person?', ['Run', 'Teacher', 'Fast', 'Blue'], 1),
   ('Which word is a noun that names a place?', ['Jump', 'School', 'Happy', 'Sing'], 1),
   ('Which word is a noun that names a thing?', ['Ball', 'Quickly', 'Sad', 'Sing'], 0),
   ('Which of these is NOT a noun?', ['Dog', 'Park', 'Book', 'Jump'], 3)])

d46_math = sub('Math', 'Measurement: Weight, Heavier and Lighter',
  'Students compare objects by weight, using the words heavier and lighter to describe which object weighs more or less.',
  [('Between a feather and a rock, which is heavier?', ['rock']),
   ('Between a feather and a rock, which is lighter?', ['feather']),
   ('What tool can help us check which object weighs more?', ['scale'])],
  [('Which is heavier: a feather or a rock?', ['Feather', 'Rock', 'They weigh the same', 'Cannot tell'], 1),
   ('Which is lighter: a book or a pencil?', ['Book', 'Pencil', 'They weigh the same', 'Cannot tell'], 1),
   ('A scale can help us find out which object is ___.', ['Colourful', 'Heavier or lighter', 'Louder', 'Faster'], 1),
   ('If two objects weigh the exact same amount, they are ___.', ['Heavier', 'Lighter', 'Equal in weight', 'Not comparable'], 2),
   ('Which word describes an object that weighs a lot?', ['Light', 'Heavy', 'Small', 'Fast'], 1)])

d46_sci = sub('Science', 'Solids and Liquids: Sorting by State',
  'Students explore two states of matter, solids and liquids, and sort everyday materials such as ice, water, wood, and juice into each group.',
  [('Is a rock a solid or a liquid?', ['solid']),
   ('Is water a solid or a liquid?', ['liquid']),
   ('Name one solid object, like a block or a rock.', ['block', 'rock', 'book', 'toy'])],
  [('Which of these is a solid?', ['Water', 'Juice', 'A rock', 'Milk'], 2),
   ('Which of these is a liquid?', ['A block', 'A book', 'Juice', 'A rock'], 2),
   ('A solid usually ___.', ['Keeps its own shape', 'Always flows and spreads out', 'Has no shape at all', 'Is always a gas'], 0),
   ('A liquid usually ___.', ['Keeps a fixed shape like a block', 'Flows and takes the shape of its container', 'Cannot be poured', 'Is always frozen'], 1),
   ('Which of these could change from a solid to a liquid, like when it melts?', ['Ice', 'A rock', 'A wooden block', 'A book'], 0)])

d46_ss = sub('SocialStudies', 'Solving Problems: Working Out Disagreements',
  'Students learn simple strategies to solve small disagreements with friends, such as talking calmly, listening, and finding a fair solution.',
  [('What should you do first when you disagree with a friend?', ['talk calmly', 'talk about it']),
   ('Why is it important to listen during a disagreement?', ['to understand each other', 'to be fair']),
   ('Name one fair way to solve a disagreement, like taking turns.', ['taking turns', 'talking it out', 'compromise'])],
  [('What is a good first step when you disagree with a friend?', ['Yelling', 'Talking calmly about the problem', 'Walking away angrily', 'Hitting'], 1),
   ('Why is listening important during a disagreement?', ['It is not important', 'It helps you understand how the other person feels', 'It makes the problem worse', 'It wastes time'], 1),
   ('Which is a fair way to solve a disagreement over a toy?', ['One person keeps it forever', 'Taking turns using it', 'Breaking the toy', 'Ignoring the other person'], 1),
   ('If you cannot solve a problem with a friend, who could help?', ['No one can help', 'A teacher or trusted adult', 'A stranger', 'Nobody, just ignore it'], 1),
   ('Solving disagreements calmly helps friends ___.', ['Stop being friends', 'Stay friends and understand each other', 'Fight more', 'Avoid talking forever'], 1)])

# ─── DAY 47 ─────────────────────────────────────────────────────────────────
d47_lang = sub('Language', 'Verbs: Action Words',
  'Students learn that a verb is a word that shows action, such as run, jump, or sing, and practise identifying verbs in simple sentences.',
  [('Is the word jump an action word or a naming word?', ['action word', 'action']),
   ('Name one verb, or action word, like run or sing.', ['run', 'jump', 'sing', 'walk', 'eat', 'play']),
   ('In the sentence The dog runs, which word is the verb?', ['runs'])],
  [('What is a verb?', ['A word that names a person', 'A word that shows action', 'A colour word', 'A number word'], 1),
   ('Which word is a verb?', ['Dog', 'Jump', 'Happy', 'Blue'], 1),
   ('In the sentence She sings a song, which word is the verb?', ['She', 'Sings', 'A', 'Song'], 1),
   ('Which of these is NOT a verb?', ['Run', 'Jump', 'Table', 'Swim'], 2),
   ('Which word could complete the sentence The bird can ___?', ['Table', 'Fly', 'Happy', 'Blue'], 1)])

d47_math = sub('Math', 'Fractions: Sharing Equally in Halves',
  'Students explore the idea of a half, learning that cutting something into two equal parts means sharing it fairly and equally.',
  [('If you cut a cookie into two equal parts, what is each part called?', ['half', 'a half']),
   ('How many halves make one whole cookie?', ['2', 'two']),
   ('If you share one apple equally with a friend, does each person get more or less than the whole apple?', ['less'])],
  [('If you cut a sandwich into two equal parts, each part is called a ___.', ['Whole', 'Half', 'Quarter', 'Double'], 1),
   ('How many halves make one whole?', ['1', '2', '3', '4'], 1),
   ('To share a cookie fairly between two friends, you should cut it into ___.', ['Two equal parts', 'Three unequal parts', 'One big piece', 'Four different sizes'], 0),
   ('If a pizza is cut into two equal halves, is each half bigger or smaller than the whole pizza?', ['Bigger', 'Smaller', 'The exact same size', 'Cannot tell'], 1),
   ('Which of these describes a shape cut into two equal halves?', ['A shape split into two same size parts', 'A shape split into four different size parts', 'A whole uncut shape', 'A shape with no parts'], 0)])

d47_sci = sub('Science', 'Shadows: Light and Dark',
  'Students explore how shadows are formed when an object blocks light, and observe how their own shadow can change size and shape.',
  [('What is needed to make a shadow, besides an object?', ['light']),
   ('What happens when an object blocks light?', ['a shadow forms', 'it makes a shadow']),
   ('Can your shadow change size during the day?', ['yes'])],
  [('What is needed to make a shadow?', ['Only darkness', 'Light and an object blocking it', 'Water', 'Wind'], 1),
   ('A shadow forms when an object ___.', ['Blocks light', 'Makes a sound', 'Floats in water', 'Melts'], 0),
   ('On a sunny day, where does your shadow usually appear?', ['On the ground near you', 'In the sky', 'Underground', 'Nowhere'], 0),
   ('Can a shadow shape and size change during the day?', ['No, it never changes', 'Yes, it can change as the sun moves', 'Shadows do not exist', 'Only at night'], 1),
   ('Which of these would create a shadow outside on a sunny day?', ['A tree blocking the sunlight', 'The wind blowing', 'Rain falling', 'A cloud passing at night'], 0)])

d47_ss = sub('SocialStudies', 'Safety Helpers: Calling for Emergency Help',
  'Students learn what an emergency is and that they can call a special number to reach safety helpers like police, firefighters, or paramedics if there is a serious emergency.',
  [('What number can you call in Canada for a serious emergency?', ['911']),
   ('Name one safety helper who might respond to an emergency call, like a firefighter.', ['firefighter', 'police officer', 'paramedic']),
   ('Should you call for emergency help if someone is badly hurt or in danger?', ['yes'])],
  [('What number can you call in an emergency in Canada?', ['411', '911', '611', '111'], 1),
   ('Which of these is an example of a serious emergency?', ['A fire in a house', 'Wanting a snack', 'Being bored', 'Losing a toy'], 0),
   ('Which safety helper might come if you call for emergency help?', ['A pilot', 'A firefighter', 'An artist', 'A chef'], 1),
   ('Why is it important to only call for emergency help during a real emergency?', ['So helpers can quickly reach people who truly need help', 'It does not matter', 'Emergency numbers are just for fun', 'Helpers are never busy'], 0),
   ('If someone is badly hurt, what is a safe first step?', ['Ignore them', 'Tell a trusted adult or call for emergency help', 'Run away', 'Do nothing'], 1)])

# ─── DAY 48 ─────────────────────────────────────────────────────────────────
d48_lang = sub('Language', 'Predicting: What Happens Next',
  'Students practise predicting, or making a smart guess, about what might happen next in a story based on clues from the pictures and words.',
  [('What does it mean to predict what happens next in a story?', ['make a guess', 'guess what happens']),
   ('What can help you predict what happens next, like pictures or clues?', ['pictures', 'clues']),
   ('If dark clouds appear in a story picture, what might you predict will happen next?', ['rain', 'it will rain'])],
  [('What does it mean to predict?', ['To make a smart guess about what might happen', 'To read the last page first', 'To ignore the story', 'To draw a picture'], 0),
   ('What can help you make a good prediction about a story?', ['Clues from pictures and words', 'Closing your eyes', 'Ignoring the book', 'Skipping pages'], 0),
   ('If a story shows a character packing a suitcase, what might you predict happens next?', ['The character is going on a trip', 'The character is going to sleep', 'The character is cooking', 'The character is swimming'], 0),
   ('Predicting what happens next helps readers ___.', ['Understand and enjoy the story more', 'Forget the story', 'Stop reading', 'Avoid thinking'], 0),
   ('If dark clouds appear in a picture, a good prediction might be that ___.', ['It will rain', 'It will snow candy', 'Nothing will happen', 'The sun will disappear forever'], 0)])

d48_math = sub('Math', 'Shapes in Our World: 2D and 3D Together',
  'Students look for 2D shapes, like circles and squares, and 3D shapes, like spheres and cubes, in everyday objects around their classroom and home.',
  [('Is a book shaped like a rectangular box a 2D or 3D shape example?', ['3d', '3D']),
   ('Name one object shaped like a sphere, like a ball.', ['ball']),
   ('Name one flat shape you might see drawn on paper, like a circle or square.', ['circle', 'square', 'triangle', 'rectangle'])],
  [('Which of these is an example of a 3D shape in real life?', ['A drawn circle', 'A ball', 'A flat square drawing', 'A triangle drawn on paper'], 1),
   ('Which of these is an example of a 2D shape?', ['A cube', 'A sphere', 'A circle drawn on paper', 'A cylinder'], 2),
   ('A book is closest in shape to which 3D shape?', ['Sphere', 'Cube or rectangular prism', 'Cone', 'Cylinder'], 1),
   ('A clock face is closest in shape to which 2D shape?', ['Square', 'Circle', 'Triangle', 'Rectangle'], 1),
   ('Why do we look for shapes in our world?', ['Shapes are only in math books', 'To notice that shapes are all around us in everyday objects', 'Shapes do not exist in real life', 'Only artists need shapes'], 1)])

d48_sci = sub('Science', 'Camouflage: Hiding in Plain Sight',
  'Students learn that camouflage is when an animal blends into its surroundings, using colours or patterns to hide from other animals.',
  [('What word describes when an animal blends into its surroundings to hide?', ['camouflage']),
   ('Why might an animal use camouflage?', ['to hide', 'to stay safe', 'to avoid predators']),
   ('Name one animal that uses camouflage, like a chameleon or a frog.', ['chameleon', 'frog', 'polar bear', 'stick insect'])],
  [('What is camouflage?', ['When an animal blends into its surroundings to hide', 'When an animal makes loud noises', 'When an animal flies very high', 'When an animal sleeps all day'], 0),
   ('Why do some animals use camouflage?', ['To attract attention', 'To hide from predators or prey', 'To grow bigger', 'To make friends'], 1),
   ('White fur on a polar bear helps it blend into ___.', ['Sand', 'Snow and ice', 'Grass', 'Mud'], 1),
   ('Which animal is known for changing colour to blend into its surroundings?', ['Chameleon', 'Elephant', 'Lion', 'Whale'], 0),
   ('Camouflage helps animals ___.', ['Stay hidden and safe', 'Become louder', 'Fly faster', 'Grow larger'], 0)])

d48_ss = sub('SocialStudies', 'Land and Water: Exploring Our Earth',
  'Students learn that the Earth is made up of land, such as mountains and forests, and water, such as lakes, rivers, and oceans.',
  [('Name one type of land feature, like a mountain or forest.', ['mountain', 'forest', 'hill']),
   ('Name one type of water feature, like a lake or ocean.', ['lake', 'ocean', 'river', 'pond']),
   ('Is a mountain a land feature or a water feature?', ['land'])],
  [('Which of these is a land feature?', ['Ocean', 'Mountain', 'River', 'Lake'], 1),
   ('Which of these is a water feature?', ['Mountain', 'Forest', 'Ocean', 'Hill'], 2),
   ('Our Earth is covered mostly by ___.', ['Only land', 'Only ice', 'A mix of land and water', 'Only sand'], 2),
   ('Which of these is an example of a body of water?', ['A river', 'A mountain', 'A forest', 'A hill'], 0),
   ('Why is it helpful to learn about land and water on Earth?', ['It helps us understand and appreciate our planet', 'It is not useful', 'Only sailors need to know', 'Land and water do not matter'], 0)])

# ─── DAY 49 ─────────────────────────────────────────────────────────────────
d49_lang = sub('Language', 'Retelling a Story in My Own Words',
  'Students practise retelling a story they have heard, using their own words to describe the characters, setting, and events in order.',
  [('When you retell a story, whose words do you use?', ['your own', 'my own']),
   ('What should you include when retelling a story, like the characters and what happened?', ['characters', 'events', 'what happened']),
   ('Should you retell the events of a story in order or out of order?', ['in order'])],
  [('What does it mean to retell a story?', ['To read the story silently', 'To tell the story again in your own words', 'To draw the story', 'To ignore the story'], 1),
   ('When retelling a story, what should you include?', ['Only the title', 'The characters, setting, and important events', 'Nothing at all', 'Only the last page'], 1),
   ('Why is it helpful to retell a story in order?', ['So the story makes sense to the listener', 'Order does not matter', 'It is not helpful', 'To make the story shorter always'], 0),
   ('If you retell a story, whose words should you mostly use?', ['The exact words from the original book', 'Your own words', 'No words at all', 'Only pictures'], 1),
   ('Retelling a story helps us practise ___.', ['Listening and speaking skills', 'Only drawing', 'Only counting', 'Only singing'], 0)])

d49_math = sub('Math', 'Number Lines: Counting Forward and Back',
  'Students use a number line to practise counting forward and backward, and to find numbers that come before, after, or between other numbers.',
  [('On a number line, if you count forward from 5, what number comes next?', ['6', 'six']),
   ('On a number line, if you count backward from 5, what number comes next?', ['4', 'four']),
   ('On a number line, which number is between 7 and 9?', ['8', 'eight'])],
  [('On a number line, counting forward from 3 gives you ___ next.', ['2', '4', '5', '1'], 1),
   ('On a number line, counting backward from 8 gives you ___ next.', ['9', '7', '10', '6'], 1),
   ('Which number sits between 10 and 12 on a number line?', ['9', '11', '13', '14'], 1),
   ('A number line helps us see numbers in ___.', ['Random order', 'Order from smallest to largest', 'Backwards colours', 'Shapes only'], 1),
   ('On a number line, moving to the right usually means the numbers ___.', ['Get smaller', 'Get bigger', 'Stay the same', 'Disappear'], 1)])

d49_sci = sub('Science', 'Taking Care of Our Teeth',
  'Students learn simple habits for keeping their teeth healthy, such as brushing twice a day, flossing, and visiting the dentist.',
  [('How many times a day should you brush your teeth?', ['2', 'two', 'twice']),
   ('Who helps check and take care of our teeth at a special office?', ['dentist']),
   ('Name one food that can be unhealthy for teeth if eaten too much, like candy.', ['candy', 'sugar', 'sweets'])],
  [('How many times a day should you brush your teeth?', ['Never', 'Once a week', 'Twice a day', 'Ten times a day'], 2),
   ('Who helps take care of our teeth at a special office?', ['A dentist', 'A pilot', 'A chef', 'An artist'], 0),
   ('Which food can be unhealthy for teeth if eaten too much?', ['An apple', 'Candy', 'Water', 'Broccoli'], 1),
   ('What tool do we use to clean between our teeth?', ['A hairbrush', 'Floss', 'A paintbrush', 'A pencil'], 1),
   ('Why is it important to take care of our teeth?', ['To keep them healthy and strong', 'Teeth do not need care', 'Only adults have teeth', 'It does not matter'], 0)])

d49_ss = sub('SocialStudies', 'Our Classroom Jobs: Helping Out',
  'Students learn about simple classroom jobs, such as line leader, helper, or paper passer, and how doing a job helps the whole class run smoothly.',
  [('Name one classroom job, like line leader or helper.', ['line leader', 'helper', 'paper passer']),
   ('Why do classrooms have jobs for students to do?', ['to help the class', 'to share responsibility']),
   ('Who leads the line when walking to another room?', ['line leader'])],
  [('Which of these is an example of a classroom job?', ['Line leader', 'Sleeping', 'Watching television', 'Nothing'], 0),
   ('Why do classrooms often give students jobs to do?', ['To help the classroom run smoothly and share responsibility', 'Jobs are not helpful', 'Only the teacher should do everything', 'To keep students bored'], 0),
   ('What does a line leader do?', ['Leads the class in a line', 'Cleans the whole school', 'Cooks lunch', 'Drives the bus'], 0),
   ('Doing a classroom job well shows that you are being ___.', ['Careless', 'Responsible', 'Unkind', 'Lazy'], 1),
   ('Which is a benefit of having classroom jobs?', ['It helps everyone contribute and feel part of the class', 'It causes more mess', 'It is unfair to have jobs', 'Nobody benefits'], 0)])

# ─── DAY 50 (Review) ────────────────────────────────────────────────────────
d50_lang = sub('Language', 'Language Review: Nouns, Verbs, and Stories',
  'Students review recent Language skills: blending sounds, compound words, question words, sequencing words, writing labels, nouns, verbs, predicting, and retelling stories.',
  [('What word do the sounds c, a, t blend to make?', ['cat']),
   ('What is a word that names a person, place, or thing called?', ['noun']),
   ('What is a word that shows action called?', ['verb'])],
  [('Sun and flower blend to make which compound word?', ['Sunflower', 'Sunshine', 'Sundial', 'Sunset'], 0),
   ('Which question word asks about a person?', ['What', 'Who', 'Where', 'When'], 1),
   ('Which word is a noun?', ['Run', 'School', 'Happy', 'Quickly'], 1),
   ('Which word is a verb?', ['Dog', 'Jump', 'Blue', 'Table'], 1),
   ('What does it mean to predict what happens next in a story?', ['To make a smart guess based on clues', 'To skip the story', 'To close the book', 'To ignore pictures'], 0)])

d50_math = sub('Math', 'Math Review: Addition, Money, and Shapes',
  'Students review recent Math skills: addition and subtraction to 20, skip counting by tens, money, growing patterns, weight, fractions, shapes, and number lines.',
  [('12 + 3 = ?', ['15', 'fifteen']),
   ('Which coin is worth ten cents?', ['dime']),
   ('If you cut a cookie into two equal parts, what is each part called?', ['half', 'a half'])],
  [('11 + 4 = ?', ['14', '15', '16', '13'], 1),
   ('18 - 5 = ?', ['12', '13', '14', '11'], 1),
   ('Skip count by tens: 10, 20, 30, then what number?', ['35', '40', '45', '50'], 1),
   ('Which coin is worth twenty five cents?', ['Penny', 'Nickel', 'Dime', 'Quarter'], 3),
   ('Which is heavier: a feather or a rock?', ['Feather', 'Rock', 'They weigh the same', 'Cannot tell'], 1)])

d50_sci = sub('Science', 'Science Review: Life Cycles, Habitats, and Our Bodies',
  'Students review recent Science topics: plant life cycles, animal habitats, nocturnal animals, bones and muscles, weather tools, solids and liquids, shadows, camouflage, and taking care of our teeth.',
  [('What is the first stage of a plant life cycle?', ['seed']),
   ('What word means the place where an animal lives?', ['habitat']),
   ('What tool measures temperature?', ['thermometer'])],
  [('What is the first stage of a plant life cycle?', ['Flower', 'Seed', 'Root', 'Sprout'], 1),
   ('What does nocturnal mean?', ['Awake during the day', 'Awake at night and asleep during the day', 'Always asleep', 'Living only in water'], 1),
   ('What gives our body its shape and support?', ['Muscles', 'Bones', 'Skin', 'Hair'], 1),
   ('What is needed to make a shadow?', ['Only darkness', 'Light and an object blocking it', 'Water', 'Wind'], 1),
   ('What is camouflage?', ['When an animal blends into its surroundings to hide', 'When an animal makes loud noises', 'When an animal flies high', 'When an animal sleeps all day'], 0)])

d50_ss = sub('SocialStudies', 'Social Studies Review: Jobs, Community, and Our Earth',
  'Students review recent Social Studies topics: jobs people do, Indigenous Peoples, landmarks, money, sharing, solving problems, safety helpers, land and water, and classroom jobs.',
  [('Who cooks meals at a restaurant?', ['chef', 'cook']),
   ('What number can you call in an emergency in Canada?', ['911']),
   ('Name one classroom job, like line leader or helper.', ['line leader', 'helper', 'paper passer'])],
  [('Who flies an airplane?', ['Chef', 'Pilot', 'Teacher', 'Farmer'], 1),
   ('Who were the first people to live in what is now Canada?', ['European settlers', 'Indigenous Peoples', 'Astronauts', 'Pilots'], 1),
   ('What is a landmark?', ['A type of food', 'A special, well known place in a community', 'A kind of weather', 'A math tool'], 1),
   ('What does taking turns mean?', ['Always going first', 'Waiting for your chance after someone else', 'Never playing', 'Playing alone forever'], 1),
   ('Which of these is a land feature?', ['Ocean', 'Mountain', 'River', 'Lake'], 1)])


g0_41_50 = [
    day(41, [d41_lang, d41_math, d41_sci, d41_ss]),
    day(42, [d42_lang, d42_math, d42_sci, d42_ss]),
    day(43, [d43_lang, d43_math, d43_sci, d43_ss]),
    day(44, [d44_lang, d44_math, d44_sci, d44_ss]),
    day(45, [d45_lang, d45_math, d45_sci, d45_ss]),
    day(46, [d46_lang, d46_math, d46_sci, d46_ss]),
    day(47, [d47_lang, d47_math, d47_sci, d47_ss]),
    day(48, [d48_lang, d48_math, d48_sci, d48_ss]),
    day(49, [d49_lang, d49_math, d49_sci, d49_ss]),
    day(50, [d50_lang, d50_math, d50_sci, d50_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_41_50)
    append_worksheet_days(0, g0_41_50)
