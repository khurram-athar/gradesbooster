#!/usr/bin/env python3
"""Grade 2, Days 51-60 -- THIRD batch extending Grade 2 past Day 50.
Self-contained script modeled exactly on gen_grade2_days41_50.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-50 topics (see data/grade2.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260830):
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


# ─── DAY 51 ─────────────────────────────────────────────────────────────────
d51_lang = sub('Language', 'Regular Past Tense Verbs: Adding -ed',
  'Students learn that many verbs show something already happened by adding the ending -ed, such as jump becoming jumped, walk becoming walked, and play becoming played.',
  [('What ending do we usually add to a verb to show it already happened?', ['-ed', 'ed']),
   ('What is the past tense of the verb jump?', ['jumped']),
   ('What is the past tense of the verb walk?', ['walked'])],
  [('What ending do we usually add to a verb to show something already happened?', ['-ed', '-ing', '-er', '-est'], 0),
   ('What is the past tense of the verb jump?', ['Jumped', 'Jumping', 'Jumps', 'Jumpy'], 0),
   ('What is the past tense of the verb walk?', ['Walked', 'Walking', 'Walks', 'Walker'], 0),
   ('Which sentence uses the correct past tense of play?', ['Yesterday I played outside.', 'Yesterday I play outside.', 'Yesterday I playing outside.', 'Yesterday I plays outside.'], 0),
   ('Adding -ed to a verb tells the reader that an action ___.', ['Already happened', 'Will happen soon', 'Is happening right now', 'Never happened'], 0)])

d51_math = sub('Math', 'Skip Counting by 3s and 4s',
  'Students practice skip counting by 3s and by 4s, extending patterns such as 3, 6, 9, 12 and 4, 8, 12, 16 to build number sense.',
  [('Skip count by 3s: 3, 6, 9, ___', ['12', 'twelve']),
   ('Skip count by 4s: 4, 8, 12, ___', ['16', 'sixteen']),
   ('What number comes next when skip counting by 3s: 9, 12, 15, ___?', ['18', 'eighteen'])],
  [('Skip count by 3s: 3, 6, 9, ___', ['12', '10', '11', '15'], 0),
   ('Skip count by 4s: 4, 8, 12, ___', ['16', '14', '15', '20'], 0),
   ('Which set of numbers shows skip counting by 3s?', ['3, 6, 9, 12', '2, 4, 6, 8', '5, 10, 15, 20', '4, 8, 12, 16'], 0),
   ('Which set of numbers shows skip counting by 4s?', ['4, 8, 12, 16', '3, 6, 9, 12', '2, 4, 6, 8', '5, 10, 15, 20'], 0),
   ('Skip counting by 3s and 4s helps us ___.', ['Count in equal groups more quickly', 'Measure length', 'Tell time', 'Read a clock'], 0)])

d51_sci = sub('Science', 'Animal Camouflage: Hiding in Plain Sight',
  'Students learn that camouflage happens when the color or pattern of an animal helps it blend into its surroundings, making it harder for predators or prey to see it.',
  [('What word describes an animal blending into its surroundings using color or pattern?', ['camouflage']),
   ('Name one reason an animal might use camouflage, like hiding from a predator.', ['hiding from a predator', 'to hide from predators', 'to hide from prey']),
   ('Name one animal that uses camouflage, like a frog or a stick insect.', ['a frog', 'frog', 'a stick insect', 'stick insect', 'a chameleon', 'chameleon'])],
  [('What word describes an animal blending into its surroundings using color or pattern?', ['Camouflage', 'Migration', 'Hibernation', 'Pollination'], 0),
   ('Why might an animal use camouflage?', ['To hide from predators or sneak up on prey', 'To fly faster', 'To make more noise', 'To change the weather'], 0),
   ('Which animal is well known for using camouflage to blend into leaves?', ['A stick insect', 'A penguin', 'A flamingo', 'A peacock'], 0),
   ('The white fur of a polar bear helps it camouflage in ___.', ['Snow and ice', 'A green forest', 'A sandy desert', 'A rocky cave'], 0),
   ('Camouflage helps animals survive by ___.', ['Making them harder to see in their habitat', 'Making them louder', 'Making them brighter colors always', 'Making them run faster'], 0)])

d51_ss = sub('SocialStudies', 'Notable Canadians and Their Achievements',
  'Students learn about notable Canadians from the past and present who made important contributions in fields such as science, sports, and the arts.',
  [('What word describes a person who is well known for an important contribution?', ['notable', 'famous']),
   ('Name one field where a notable Canadian might make a contribution, like science or sports.', ['science', 'sports', 'the arts', 'music']),
   ('Why do we learn about notable Canadians in social studies?', ['to learn about their achievements', 'to learn about important contributions', 'to learn about their achievements and history'])],
  [('What word describes a person who is well known for an important contribution?', ['Notable', 'Ordinary', 'Invisible', 'Silent'], 0),
   ('Which of these is a field where a notable Canadian might make a contribution?', ['Science, sports, or the arts', 'Only sleeping', 'Only eating', 'Only traveling'], 0),
   ('Why is it valuable to learn about notable Canadians?', ['It helps us understand important achievements and history', 'It has no value at all', 'It only teaches math', 'It teaches nothing about Canada'], 0),
   ('A notable Canadian scientist might be remembered for ___.', ['An important discovery or invention', 'Losing a game', 'Forgetting their homework', 'Staying home all day'], 0),
   ('Learning about people who made a difference can inspire us to ___.', ['Work hard and contribute to our community', 'Ignore our community', 'Avoid learning new things', 'Stop trying new things'], 0)])

# ─── DAY 52 ─────────────────────────────────────────────────────────────────
d52_lang = sub('Language', 'Capitalization Rules: Names, Places, and Titles',
  'Students learn that capital letters are used at the beginning of names of people, places, and titles, such as Sarah, Toronto, and the title of a book.',
  [('What kind of letter starts the name of a person?', ['a capital letter', 'capital letter']),
   ('Should the name of a city, like Toronto, start with a capital letter?', ['yes']),
   ('Name one type of word that always starts with a capital letter, like a name or a place.', ['a name', 'name', 'a place', 'place', 'a title', 'title'])],
  [('What kind of letter starts the name of a person, like Sarah?', ['A capital letter', 'A lowercase letter', 'A number', 'A silent letter'], 0),
   ('Which of these words should start with a capital letter?', ['Toronto', 'the', 'and', 'dog'], 0),
   ('Which sentence uses capitalization correctly?', ['My friend Sam lives in Ottawa.', 'my friend sam lives in ottawa.', 'My Friend sam Lives in ottawa.', 'my friend Sam lives in Ottawa.'], 0),
   ('The first word in the title of a book should begin with a ___.', ['Capital letter', 'Lowercase letter', 'Number', 'Question mark'], 0),
   ('Capitalization rules help readers know that a word is ___.', ['A special name for a person, place, or title', 'Always a verb', 'Always plural', 'Always short'], 0)])

d52_math = sub('Math', 'Introduction to Division: Sharing Equally into Groups',
  'Students learn that division means sharing a group of objects equally into smaller groups, such as sharing 12 apples equally among 3 friends so each friend gets 4.',
  [('If you share 12 apples equally among 3 friends, how many apples does each friend get?', ['4', 'four']),
   ('What do we call splitting a group of objects equally into smaller groups?', ['division', 'sharing equally']),
   ('If you share 10 stickers equally between 2 friends, how many stickers does each friend get?', ['5', 'five'])],
  [('What do we call splitting a group of objects equally into smaller groups?', ['Division', 'Addition', 'Multiplication', 'Rounding'], 0),
   ('If you share 12 apples equally among 3 friends, how many apples does each friend get?', ['4', '3', '6', '12'], 0),
   ('If you share 10 stickers equally between 2 friends, how many stickers does each friend get?', ['5', '2', '10', '4'], 0),
   ('If you share 8 cookies equally among 4 friends, how many cookies does each friend get?', ['2', '4', '8', '1'], 0),
   ('Sharing a group of objects equally means each group gets ___.', ['The same amount', 'A different amount each time', 'Nothing at all', 'Only one object total'], 0)])

d52_sci = sub('Science', 'Life Cycle of a Butterfly: Metamorphosis',
  'Students learn the life cycle of a butterfly, called metamorphosis, which includes the stages of egg, caterpillar, chrysalis, and adult butterfly.',
  [('What is the first stage of a butterfly life cycle?', ['egg', 'an egg']),
   ('What do we call a young butterfly that hatches from an egg and eats leaves?', ['a caterpillar', 'caterpillar']),
   ('What do we call the changing process a caterpillar goes through inside a chrysalis?', ['metamorphosis'])],
  [('What is the first stage of a butterfly life cycle?', ['Egg', 'Caterpillar', 'Chrysalis', 'Adult butterfly'], 0),
   ('What do we call a young butterfly that hatches from an egg and eats leaves?', ['A caterpillar', 'A tadpole', 'A cub', 'A chick'], 0),
   ('What do we call the stage where a caterpillar forms a hard case and changes shape?', ['Chrysalis', 'Nest', 'Burrow', 'Web'], 0),
   ('Put the butterfly life cycle stages in the correct order.', ['Egg, caterpillar, chrysalis, adult butterfly', 'Adult butterfly, egg, chrysalis, caterpillar', 'Chrysalis, egg, caterpillar, adult butterfly', 'Caterpillar, adult butterfly, egg, chrysalis'], 0),
   ('The complete change in body shape that a butterfly goes through is called ___.', ['Metamorphosis', 'Hibernation', 'Migration', 'Pollination'], 0)])

d52_ss = sub('SocialStudies', 'Canadian Inventions That Changed the World',
  'Students learn about inventions created in Canada that changed the way people live, work, and play, such as basketball and insulin.',
  [('Name one invention or discovery created in Canada, like basketball or insulin.', ['basketball', 'insulin']),
   ('What word describes something new that a person creates for the first time?', ['an invention', 'invention']),
   ('Why are inventions important to a community?', ['they solve problems', 'they make life easier', 'they help people'])],
  [('What word describes something new that a person creates for the first time?', ['An invention', 'A tradition', 'A landmark', 'A festival'], 0),
   ('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Baseball', 'Tennis'], 0),
   ('Why are inventions important to a community?', ['They can solve problems and make life easier', 'They always cause problems', 'They have no effect on daily life', 'They stop people from working'], 0),
   ('Insulin, an important medicine, was discovered by scientists working in which country?', ['Canada', 'Australia', 'Brazil', 'Egypt'], 0),
   ('Learning about inventions helps us understand ___.', ['How new ideas can improve daily life', 'How to bake bread', 'How to play music', 'How to grow plants'], 0)])

# ─── DAY 53 ─────────────────────────────────────────────────────────────────
d53_lang = sub('Language', 'Multiple-Meaning Words',
  'Students learn that some words have more than one meaning depending on how they are used in a sentence, such as bat, an animal or something used to hit a ball, and bark, the sound a dog makes or the covering of a tree.',
  [('Name one word that can mean two different things, like bat or bark.', ['bat', 'bark', 'ring', 'bank']),
   ('In the sentence, the dog began to bark, what does bark mean?', ['the sound a dog makes', 'dog sound', 'sound']),
   ('In the sentence, we saw a bat flying at night, what does bat mean?', ['an animal', 'animal', 'flying animal'])],
  [('What do we call a word that has more than one meaning?', ['A multiple-meaning word', 'A synonym', 'An antonym', 'A silent letter'], 0),
   ('In the sentence, the dog began to bark, what does bark mean?', ['The sound a dog makes', 'The covering of a tree', 'A baseball bat', 'A type of boat'], 0),
   ('In the sentence, the bark of the tree was rough, what does bark mean?', ['The covering of a tree', 'The sound a dog makes', 'A flying animal', 'A type of ball'], 0),
   ('Which word can mean both an animal and a piece of sports equipment?', ['Bat', 'Dog', 'Tree', 'Chair'], 0),
   ('To figure out which meaning of a word is being used, readers should ___.', ['Look at the other words in the sentence', 'Only look at the first letter', 'Ignore the sentence completely', 'Guess without reading'], 0)])

d53_math = sub('Math', 'Probability: Likely, Unlikely, Certain, and Impossible',
  'Students learn to describe the chance of an event happening using the words certain, likely, unlikely, and impossible.',
  [('What word describes an event that will definitely happen?', ['certain']),
   ('What word describes an event that will definitely not happen?', ['impossible']),
   ('Is it likely or unlikely that it will snow in July in Ontario?', ['unlikely'])],
  [('What word describes an event that will definitely happen?', ['Certain', 'Impossible', 'Unlikely', 'Random'], 0),
   ('What word describes an event that can never happen?', ['Impossible', 'Certain', 'Likely', 'Probable'], 0),
   ('Is it certain or unlikely that the sun will rise tomorrow?', ['Certain', 'Impossible', 'Unlikely', 'Random'], 0),
   ('Is it likely or unlikely that it will snow in Ontario in July?', ['Unlikely', 'Certain', 'Likely', 'Impossible'], 0),
   ('If a bag has only red marbles, picking a blue marble is ___.', ['Impossible', 'Certain', 'Likely', 'Unlikely but possible'], 0)])

d53_sci = sub('Science', 'Bones and Muscles: How Our Body Moves',
  'Students learn that bones form a skeleton that supports and protects the body, while muscles work with bones to help the body move.',
  [('What do we call the frame of bones inside our body?', ['a skeleton', 'skeleton']),
   ('What body part works with bones to help us move?', ['muscles', 'muscle']),
   ('Name one job that bones do for our body, like protecting organs.', ['protecting organs', 'support the body', 'protect the body'])],
  [('What do we call the frame of bones that supports our body?', ['A skeleton', 'A muscle', 'A joint', 'An organ'], 0),
   ('What body part works together with bones to help us move?', ['Muscles', 'Skin', 'Hair', 'Nails'], 0),
   ('Which of these is a job that bones do for the body?', ['Protecting organs like the heart and brain', 'Digesting food', 'Pumping blood', 'Seeing light'], 0),
   ('Where would you find the bones that protect your brain?', ['The skull', 'The arm', 'The leg', 'The hand'], 0),
   ('Muscles help the body move by ___.', ['Pulling on bones to create movement', 'Making bones disappear', 'Turning into skin', 'Stopping the heart'], 0)])

d53_ss = sub('SocialStudies', 'How We Get Our Water: From Source to Tap',
  'Students learn how water travels from lakes and rivers, through a treatment plant that makes it clean, and finally through pipes to homes and schools.',
  [('Name one place water might come from before it reaches our homes, like a lake or river.', ['a lake', 'lake', 'a river', 'river']),
   ('What do we call a place that cleans water before it reaches our homes?', ['a treatment plant', 'treatment plant', 'water treatment plant']),
   ('How does clean water travel from a treatment plant to our homes?', ['through pipes', 'pipes'])],
  [('Where might the water that reaches our homes first come from?', ['A lake or river', 'A cloud only', 'A grocery store', 'A library'], 0),
   ('What do we call a place that cleans water so it is safe to drink?', ['A water treatment plant', 'A fire station', 'A school', 'A farm'], 0),
   ('How does clean water usually travel from a treatment plant to our homes?', ['Through underground pipes', 'By truck only', 'By airplane', 'By boat only'], 0),
   ('Why is it important to clean water before people drink it?', ['To remove dirt and germs so it is safe', 'To make it taste like juice', 'To make it colder', 'To make it a different color'], 0),
   ('Communities build water systems so that people can ___.', ['Have safe, clean water for drinking and washing', 'Never use water at all', 'Only use rainwater', 'Avoid drinking water completely'], 0)])

# ─── DAY 54 ─────────────────────────────────────────────────────────────────
d54_lang = sub('Language', 'Using Context Clues to Find Word Meaning',
  'Students learn to use context clues, the words and sentences around an unfamiliar word, to figure out what that word probably means.',
  [('What do we call the words around an unfamiliar word that help us guess its meaning?', ['context clues']),
   ('If a sentence says, the enormous elephant was huge and heavy, what might enormous mean?', ['very big', 'huge', 'big']),
   ('Why are context clues useful when reading?', ['they help us understand new words', 'help figure out word meaning'])],
  [('What do we call the words and sentences around an unfamiliar word that help us understand its meaning?', ['Context clues', 'Rhyming words', 'Compound words', 'Silent letters'], 0),
   ('If a sentence says, the enormous elephant was huge and heavy, what does enormous most likely mean?', ['Very big', 'Very small', 'Very fast', 'Very quiet'], 0),
   ('Why should readers use context clues when they find an unfamiliar word?', ['To figure out its meaning without a dictionary', 'To skip the word completely', 'To stop reading the book', 'To change the word into a picture'], 0),
   ('If a sentence says, the frigid winter air made her shiver, what does frigid most likely mean?', ['Very cold', 'Very hot', 'Very bright', 'Very loud'], 0),
   ('Context clues can be found ___.', ['In the words and sentences near the unfamiliar word', 'Only in the dictionary', 'Only in the title of the book', 'Only in pictures'], 0)])

d54_math = sub('Math', 'Using a Number Line to Add and Subtract',
  'Students learn to use a number line as a tool to add by jumping forward and to subtract by jumping backward.',
  [('On a number line, which direction do you jump to add?', ['forward', 'to the right']),
   ('On a number line, which direction do you jump to subtract?', ['backward', 'to the left']),
   ('Starting at 5 on a number line and jumping forward 3, where do you land?', ['8', 'eight'])],
  [('On a number line, which direction do you jump to add numbers?', ['Forward', 'Backward', 'Sideways', 'You do not move'], 0),
   ('On a number line, which direction do you jump to subtract numbers?', ['Backward', 'Forward', 'Upward', 'Downward'], 0),
   ('Starting at 5 on a number line and jumping forward 3, where do you land?', ['8', '2', '6', '9'], 0),
   ('Starting at 10 on a number line and jumping backward 4, where do you land?', ['6', '14', '4', '8'], 0),
   ('A number line is a useful tool because it helps us ___.', ['See addition and subtraction as jumps forward or backward', 'Only measure weight', 'Only tell time', 'Only count coins'], 0)])

d54_sci = sub('Science', 'The Phases of the Moon',
  'Students learn that the moon appears to change shape in the sky over about a month, moving through phases such as new moon, crescent, half moon, and full moon.',
  [('What do we call the changing shapes of the moon we see in the sky?', ['phases of the moon', 'moon phases']),
   ('Name one phase of the moon, like full moon or new moon.', ['full moon', 'new moon', 'crescent', 'half moon']),
   ('About how long does it take the moon to go through all its phases?', ['about a month', 'one month', 'a month'])],
  [('What do we call the changing shapes of the moon that we see in the sky?', ['Phases of the moon', 'Seasons', 'Eclipses', 'Constellations'], 0),
   ('Which phase of the moon looks like a complete bright circle?', ['Full moon', 'New moon', 'Crescent moon', 'Half moon'], 0),
   ('During a new moon, how much of the moon can we usually see?', ['Very little or none', 'The whole moon', 'Exactly half', 'Three quarters'], 0),
   ('About how long does it take the moon to go through all of its phases?', ['About a month', 'About a day', 'About a year', 'About a week'], 0),
   ('The moon appears to change shape because ___.', ['We see different amounts of its sunlit side as it orbits earth', 'The moon changes size', 'The moon turns a different color', 'The moon disappears and reappears'], 0)])

d54_ss = sub('SocialStudies', 'Types of Homes Around the World',
  'Students learn that people around the world live in many different types of homes, such as apartments, houses, igloos, and huts, often built to suit the climate and resources of their region.',
  [('Name one type of home people might live in, like an apartment or a house.', ['an apartment', 'apartment', 'a house', 'house', 'an igloo', 'igloo']),
   ('Why might homes look different in different parts of the world?', ['different climates', 'different resources', 'climate and resources']),
   ('Name a type of home built to suit a cold, snowy climate.', ['an igloo', 'igloo'])],
  [('Which of these is a type of home people might live in?', ['An apartment', 'A river', 'A mountain', 'A cloud'], 0),
   ('Why might homes look different in different parts of the world?', ['Different climates and available resources', 'All homes are exactly the same everywhere', 'Homes never change', 'Weather does not affect homes'], 0),
   ('Which type of home was traditionally built to suit a very cold, snowy climate?', ['An igloo', 'A treehouse', 'A houseboat', 'A beach hut'], 0),
   ('In a crowded city, many people might choose to live in a ___.', ['An apartment building', 'A large farm', 'A desert tent', 'A floating village'], 0),
   ('Learning about homes around the world helps us understand ___.', ['How people adapt to their environment', 'How to build roads', 'How to grow crops', 'How to read a map only'], 0)])

# ─── DAY 55 ─────────────────────────────────────────────────────────────────
d55_lang = sub('Language', 'Onomatopoeia: Sound Words in Stories',
  'Students learn that onomatopoeia words imitate the sound they describe, such as buzz, crash, splash, and pop, adding excitement to writing.',
  [('What do we call a word that imitates the sound it describes, like buzz or splash?', ['onomatopoeia']),
   ('Name one onomatopoeia word that describes the sound a bee makes.', ['buzz']),
   ('Name one onomatopoeia word that describes the sound something makes when it falls into water.', ['splash'])],
  [('What do we call a word that imitates the sound it describes?', ['Onomatopoeia', 'A synonym', 'An antonym', 'A compound word'], 0),
   ('Which of these words is an example of onomatopoeia?', ['Buzz', 'Happy', 'Quickly', 'Elephant'], 0),
   ('Which onomatopoeia word describes the sound of something falling into water?', ['Splash', 'Buzz', 'Crash', 'Pop'], 0),
   ('Which onomatopoeia word describes the sound of two objects colliding loudly?', ['Crash', 'Splash', 'Whisper', 'Hum'], 0),
   ('Writers use onomatopoeia to ___.', ['Help readers imagine the sounds in a story', 'Make writing longer only', 'Confuse the reader', 'Remove all sounds from a story'], 0)])

d55_math = sub('Math', 'Measuring Mass with Grams and Kilograms',
  'Students learn that mass, or how heavy an object is, can be measured using grams for lighter objects and kilograms for heavier objects.',
  [('What unit would you use to measure the mass of a light object, like a pencil?', ['grams', 'gram']),
   ('What unit would you use to measure the mass of a heavy object, like a dog?', ['kilograms', 'kilogram']),
   ('Which is heavier, 1 kilogram or 1 gram?', ['1 kilogram', 'kilogram'])],
  [('What unit would you most likely use to measure the mass of a paperclip?', ['Grams', 'Kilograms', 'Litres', 'Centimetres'], 0),
   ('What unit would you most likely use to measure the mass of a large dog?', ['Kilograms', 'Grams', 'Millilitres', 'Metres'], 0),
   ('Which is heavier, 1 kilogram or 1 gram?', ['1 kilogram', '1 gram', 'They are equal', 'Cannot tell'], 0),
   ('What tool would you use to measure the mass of an object?', ['A scale', 'A ruler', 'A clock', 'A thermometer'], 0),
   ('Mass tells us ___.', ['How heavy an object is', 'How long an object is', 'How much liquid an object holds', 'How hot an object is'], 0)])

d55_sci = sub('Science', 'How Wind and Water Change the Land: Erosion',
  'Students learn that erosion happens when wind and water slowly wear away rock and soil, changing the shape of the land over time.',
  [('What do we call it when wind and water slowly wear away rock and soil?', ['erosion']),
   ('Name one force of nature that can cause erosion, like wind or water.', ['wind', 'water']),
   ('Does erosion happen quickly or slowly, over a long time?', ['slowly', 'over a long time'])],
  [('What do we call it when wind and water slowly wear away rock and soil?', ['Erosion', 'Pollination', 'Migration', 'Hibernation'], 0),
   ('Which of these can cause erosion?', ['Wind and water', 'Sunlight only', 'Silence', 'Colours'], 0),
   ('Erosion usually happens ___.', ['Slowly, over a long period of time', 'In one single second', 'Only during the night', 'Only in cities'], 0),
   ('Which of these landforms could be shaped by water erosion over time?', ['A river canyon', 'A parking lot', 'A classroom', 'A library'], 0),
   ('Planting trees and grass can help reduce erosion because roots ___.', ['Hold soil in place', 'Attract more wind', 'Make rocks heavier', 'Stop rain completely'], 0)])

d55_ss = sub('SocialStudies', 'Canadian Sports and Pastimes',
  'Students learn about sports and pastimes enjoyed across Canada, such as hockey, lacrosse, skating, and camping, and how they reflect Canadian culture and geography.',
  [('Name one sport that is popular in Canada, like hockey or lacrosse.', ['hockey', 'lacrosse']),
   ('Which Canadian sport is often played on ice?', ['hockey']),
   ('Name one outdoor pastime enjoyed in Canada, like camping or skating.', ['camping', 'skating'])],
  [('Which sport is widely played and watched across Canada, especially in winter?', ['Hockey', 'Surfing', 'Bullfighting', 'Sumo wrestling'], 0),
   ('Which sport, often called the national summer sport of Canada, uses a small rubber ball and a net on a long stick?', ['Lacrosse', 'Basketball', 'Cricket', 'Golf'], 0),
   ('Why might winter sports like hockey and skating be popular in many parts of Canada?', ['Because winters are cold with lots of snow and ice', 'Because it never snows in Canada', 'Because Canada has no winter season', 'Because ice never forms in Canada'], 0),
   ('Which of these is an outdoor pastime many Canadians enjoy in the summer?', ['Camping', 'Ice fishing', 'Building snow forts', 'Tobogganing'], 0),
   ('Sports and pastimes in a country can reflect its ___.', ['Culture, climate, and geography', 'Only its population size', 'Only its currency', 'Only its government'], 0)])

# ─── DAY 56 ─────────────────────────────────────────────────────────────────
d56_lang = sub('Language', 'Text Features: Titles, Headings, and Captions',
  'Students learn that text features such as titles, headings, and captions help readers find information and understand what a section of text is about.',
  [('What do we call the words at the top of a book or chapter that tell what it is about?', ['a title', 'title']),
   ('What do we call a short label under a picture that explains what it shows?', ['a caption', 'caption']),
   ('What do we call a word or phrase that introduces a new section of text?', ['a heading', 'heading'])],
  [('What do we call the words at the top of a book that tell what it is about?', ['A title', 'A caption', 'A footnote', 'A glossary'], 0),
   ('What do we call a short label under a picture that explains what it shows?', ['A caption', 'A heading', 'A title', 'A table of contents'], 0),
   ('What do we call a word or phrase that introduces a new section in a text?', ['A heading', 'A caption', 'A footnote', 'An index'], 0),
   ('Why are text features like titles and headings helpful to readers?', ['They help readers find information quickly', 'They make books heavier', 'They remove all pictures', 'They make reading impossible'], 0),
   ('Which of these is an example of a text feature?', ['A heading', 'A verb', 'A vowel', 'A syllable'], 0)])

d56_math = sub('Math', 'Measuring Capacity with Litres and Millilitres',
  'Students learn that capacity, or how much liquid a container can hold, can be measured using millilitres for small amounts and litres for larger amounts.',
  [('What unit would you use to measure a small amount of liquid, like in a spoon?', ['millilitres', 'millilitre']),
   ('What unit would you use to measure a large amount of liquid, like in a bathtub?', ['litres', 'litre']),
   ('Which holds more liquid, 1 litre or 1 millilitre?', ['1 litre', 'litre'])],
  [('What unit would you most likely use to measure a small spoonful of liquid?', ['Millilitres', 'Litres', 'Kilograms', 'Metres'], 0),
   ('What unit would you most likely use to measure the water in a bathtub?', ['Litres', 'Millilitres', 'Grams', 'Centimetres'], 0),
   ('Which holds more liquid, 1 litre or 1 millilitre?', ['1 litre', '1 millilitre', 'They are equal', 'Cannot tell'], 0),
   ('What do we call the amount of liquid a container can hold?', ['Capacity', 'Perimeter', 'Area', 'Mass'], 0),
   ('A large water bottle would most likely be measured in ___.', ['Litres', 'Kilograms', 'Metres', 'Degrees'], 0)])

d56_sci = sub('Science', 'Static Electricity: Why Balloons Stick to Walls',
  'Students learn that static electricity happens when tiny charges build up on an object, such as a balloon rubbed on hair, causing it to stick to a wall or attract small bits of paper.',
  [('What kind of electricity builds up when you rub a balloon on your hair?', ['static electricity', 'static']),
   ('What can a balloon with static electricity stick to, like a wall?', ['a wall', 'wall']),
   ('Name one small object that a balloon with static electricity might attract, like bits of paper.', ['bits of paper', 'paper', 'small pieces of paper'])],
  [('What kind of electricity builds up when you rub a balloon on your hair?', ['Static electricity', 'Circuit electricity', 'Solar electricity', 'Wind electricity'], 0),
   ('After rubbing a balloon on your hair, what might the balloon do?', ['Stick to a wall', 'Turn into a solid', 'Melt', 'Freeze'], 0),
   ('What can happen when you rub a balloon on hair and then hold it near small bits of paper?', ['The paper is attracted to the balloon', 'The paper turns into water', 'The paper disappears', 'Nothing happens at all'], 0),
   ('Static electricity is different from the electricity in a simple circuit because static electricity ___.', ['Builds up charges that are not flowing in a loop', 'Always needs a battery', 'Only comes from the sun', 'Never happens outdoors'], 0),
   ('Rubbing certain materials together can cause tiny charges to ___.', ['Build up on their surfaces', 'Disappear completely', 'Turn into heat only', 'Turn into light only'], 0)])

d56_ss = sub('SocialStudies', 'Why People Settle Near Water and Resources',
  'Students learn that communities often grow near lakes, rivers, and other resources because water and resources provide food, transportation, and materials people need.',
  [('Name one resource that might make people want to build a community nearby, like water.', ['water', 'fresh water', 'fertile land', 'trees']),
   ('Why might people build communities near rivers or lakes?', ['for water', 'for transportation', 'for water and transportation']),
   ('Name one thing water provides for a community, like transportation or drinking water.', ['transportation', 'drinking water', 'water for farming'])],
  [('Why do many communities grow near lakes and rivers?', ['Water and resources are easier to access there', 'Water is never useful to communities', 'Rivers make land colder', 'Lakes make travel impossible'], 0),
   ('Which of these is a reason people might settle near water?', ['Water for drinking, farming, and transportation', 'Water makes land disappear', 'Water stops all travel', 'Water removes all resources'], 0),
   ('Which of these resources might attract people to build a community nearby?', ['Fertile farmland and fresh water', 'Empty air only', 'A place with no resources', 'A place with no water'], 0),
   ('Rivers can help communities by providing a route for ___.', ['Transportation and trade', 'Only swimming', 'Only fishing tournaments', 'Only boating races'], 0),
   ('Studying why communities settle in certain places helps us understand ___.', ['How geography and resources shape where people live', 'How to build a car', 'How to bake bread', 'How to play music'], 0)])

# ─── DAY 57 ─────────────────────────────────────────────────────────────────
d57_lang = sub('Language', 'Purpose for Writing: Inform, Entertain, or Persuade',
  'Students learn that writers have a purpose for writing, such as to inform readers with facts, to entertain readers with a fun story, or to persuade readers to agree with an idea.',
  [('What is the purpose of writing when the goal is to give readers facts?', ['to inform', 'inform']),
   ('What is the purpose of writing when the goal is to make readers laugh or enjoy a story?', ['to entertain', 'entertain']),
   ('What is the purpose of writing when the goal is to convince readers to agree with an idea?', ['to persuade', 'persuade'])],
  [('What is the purpose of writing that gives readers facts and information?', ['To inform', 'To entertain', 'To persuade', 'To rhyme'], 0),
   ('What is the purpose of writing a funny story or an adventure tale?', ['To entertain', 'To inform', 'To persuade', 'To measure'], 0),
   ('What is the purpose of writing that tries to convince readers to agree with an idea?', ['To persuade', 'To inform', 'To entertain', 'To describe only colours'], 0),
   ('A weather report that shares facts about the weather tomorrow is meant to ___.', ['Inform', 'Entertain', 'Persuade', 'Confuse'], 0),
   ('A poster that says, recycle to help our planet, is trying to ___.', ['Persuade readers to take action', 'Only entertain readers', 'Only inform readers with numbers', 'Confuse the reader'], 0)])

d57_math = sub('Math', 'Comparing Money Amounts and Making Combinations',
  'Students learn to compare different amounts of money to see which is greater, and to find different combinations of coins that add up to the same amount.',
  [('Which is worth more, 3 quarters or 2 dimes?', ['3 quarters', 'three quarters']),
   ('Name two coins that could add up to 15 cents.', ['a dime and a nickel', 'dime and nickel']),
   ('If you have 1 quarter, how many cents do you have?', ['25', '25 cents'])],
  [('Which is worth more, 3 quarters or 2 dimes?', ['3 quarters', '2 dimes', 'They are equal', 'Cannot tell'], 0),
   ('Which combination of coins adds up to 15 cents?', ['A dime and a nickel', 'Two quarters', 'Three dimes', 'One nickel'], 0),
   ('How many cents is 1 quarter worth?', ['25 cents', '10 cents', '5 cents', '1 cent'], 0),
   ('Which amount of money is greater, 45 cents or 4 dimes?', ['45 cents', '4 dimes', 'They are equal', 'Cannot tell'], 0),
   ('Comparing money amounts helps us know ___.', ['Which amount is worth more or less', 'How to tell time', 'How to measure length', 'How to weigh objects'], 0)])

d57_sci = sub('Science', 'Protecting Endangered Animals',
  'Students learn that an endangered animal is one that is at risk of disappearing forever, and that people can help protect these animals by preserving habitats and reducing pollution.',
  [('What word describes an animal that is at risk of disappearing forever?', ['endangered']),
   ('Name one way people can help protect endangered animals, like preserving habitats.', ['preserving habitats', 'protecting habitats', 'reducing pollution']),
   ('Name one endangered animal, like a panda or a sea turtle.', ['a panda', 'panda', 'a sea turtle', 'sea turtle'])],
  [('What word describes an animal that is at risk of disappearing forever?', ['Endangered', 'Nocturnal', 'Migratory', 'Domestic'], 0),
   ('Which of these can help protect endangered animals?', ['Preserving their habitats', 'Cutting down more forests', 'Increasing pollution', 'Ignoring the problem'], 0),
   ('Which of these is an example of an endangered animal?', ['A giant panda', 'A house cat', 'A farm cow', 'A pet goldfish'], 0),
   ('Why might an animal become endangered?', ['Losing its habitat or being hunted too much', 'Having too many babies', 'Living too long', 'Eating too much food'], 0),
   ('Protecting endangered animals is important because ___.', ['It helps keep nature balanced and healthy for the future', 'It has no effect on nature', 'It makes habitats disappear faster', 'It only helps people, not animals'], 0)])

d57_ss = sub('SocialStudies', 'History of Money: From Trading to Coins',
  'Students learn that before coins and bills existed, people traded goods directly, called bartering, and over time societies developed coins and paper money to make trading easier.',
  [('What do we call it when people trade goods directly without using money?', ['bartering', 'trading goods']),
   ('What did people use before coins and paper money existed?', ['bartering', 'trading goods', 'trading']),
   ('Why did societies eventually start using coins instead of only bartering?', ['to make trading easier', 'easier trading'])],
  [('What do we call it when people trade goods directly without using money?', ['Bartering', 'Borrowing', 'Saving', 'Investing'], 0),
   ('Before coins and paper money existed, how did people usually get the things they needed?', ['By trading goods directly with each other', 'By using credit cards', 'By using the internet', 'By using cheques'], 0),
   ('Why did societies eventually begin using coins instead of only trading goods?', ['Coins made trading easier and fairer', 'Coins made trading impossible', 'Coins removed the need for goods', 'Coins were heavier than goods'], 0),
   ('What were some of the first types of money often made from?', ['Metal, shaped into coins', 'Plastic cards', 'Paper only', 'Wood only'], 0),
   ('Learning about the history of money helps us understand ___.', ['How trading and money have changed over time', 'How to grow crops', 'How to build houses', 'How to read a map'], 0)])

# ─── DAY 58 ─────────────────────────────────────────────────────────────────
d58_lang = sub('Language', 'Story Theme: The Lesson Behind a Story',
  'Students learn that a theme is the main lesson or message of a story, often about kindness, honesty, or working hard, that readers can apply to their own lives.',
  [('What do we call the main lesson or message of a story?', ['theme', 'the theme']),
   ('Name one common story theme, like kindness or honesty.', ['kindness', 'honesty', 'hard work', 'friendship']),
   ('How is a theme different from the plot of a story?', ['theme is the lesson', 'theme is the message, plot is what happens'])],
  [('What do we call the main lesson or message of a story?', ['Theme', 'Setting', 'Character', 'Caption'], 0),
   ('Which of these is a common theme found in stories?', ['Kindness matters', 'The exact page number', 'The book title only', 'The font used'], 0),
   ('How is theme different from plot?', ['Theme is the lesson, plot is the sequence of events', 'Theme and plot are the same thing', 'Theme is only a picture', 'Plot is the lesson, theme is the setting'], 0),
   ('In a story where a slow turtle wins a race by trying hard, a likely theme is ___.', ['Hard work and patience can lead to success', 'Fast animals always win', 'Racing is dangerous', 'Turtles cannot move'], 0),
   ('Finding the theme of a story helps readers ___.', ['Understand a lesson they can apply to their own lives', 'Skip the ending', 'Forget the story quickly', 'Avoid thinking about the story'], 0)])

d58_math = sub('Math', 'Sorting 3D Objects by Attributes',
  'Students learn to sort three-dimensional objects, such as cubes, spheres, cones, and cylinders, by attributes like the number of faces, edges, and whether they can roll.',
  [('Name one three-dimensional shape, like a cube or a sphere.', ['a cube', 'cube', 'a sphere', 'sphere', 'a cone', 'cone', 'a cylinder', 'cylinder']),
   ('Which 3D shape looks like a ball and can roll in any direction?', ['a sphere', 'sphere']),
   ('Which 3D shape has six flat square faces?', ['a cube', 'cube'])],
  [('Which 3D shape looks like a ball and can roll in any direction?', ['Sphere', 'Cube', 'Cone', 'Cylinder'], 0),
   ('Which 3D shape has six flat square faces?', ['Cube', 'Sphere', 'Cone', 'Cylinder'], 0),
   ('Which 3D shape has one flat circular face and one pointed tip?', ['Cone', 'Cube', 'Cylinder', 'Sphere'], 0),
   ('Which 3D shape has two flat circular faces and one curved surface, like a can?', ['Cylinder', 'Cube', 'Cone', 'Sphere'], 0),
   ('When sorting 3D shapes, we can group them by ___.', ['The number of faces, edges, and whether they roll', 'Their colour only', 'Their smell', 'Their name only'], 0)])

d58_sci = sub('Science', 'Taking Care of Your Teeth',
  'Students learn healthy habits for taking care of their teeth, such as brushing twice a day, flossing, and visiting the dentist for checkups.',
  [('How many times a day should you usually brush your teeth?', ['twice', 'two times', '2']),
   ('Name one tool used to clean between your teeth, like floss.', ['floss']),
   ('Who should you visit for regular teeth checkups?', ['a dentist', 'dentist'])],
  [('How many times a day should you usually brush your teeth?', ['Twice', 'Once a week', 'Ten times', 'Never'], 0),
   ('What tool is used to clean between your teeth?', ['Floss', 'A hammer', 'A ruler', 'A thermometer'], 0),
   ('Who should you visit for regular teeth checkups?', ['A dentist', 'A librarian', 'A firefighter', 'A farmer'], 0),
   ('Which of these foods can help keep teeth healthy?', ['Fruits and vegetables', 'Sugary candy', 'Sticky sweets', 'Sugary soda'], 0),
   ('Taking care of your teeth is important because it helps ___.', ['Prevent cavities and keep teeth healthy', 'Make teeth fall out faster', 'Make food taste worse', 'Stop you from smiling'], 0)])

d58_ss = sub('SocialStudies', 'Community Recreation: Parks, Rinks, and Playgrounds',
  'Students learn that communities build recreation spaces, such as parks, skating rinks, and playgrounds, so people can exercise, play, and spend time together.',
  [('Name one recreation space found in many communities, like a park or a playground.', ['a park', 'park', 'a playground', 'playground', 'a rink', 'rink']),
   ('Why do communities build recreation spaces like parks and playgrounds?', ['so people can play and exercise', 'for exercise and fun', 'so people can spend time together']),
   ('Name one activity people might do at a community park.', ['playing', 'exercising', 'picnicking', 'walking'])],
  [('Which of these is an example of a community recreation space?', ['A park', 'A hospital', 'A bank', 'A factory'], 0),
   ('Why do communities build recreation spaces like parks and playgrounds?', ['So people can exercise, play, and spend time together', 'So no one can go outside', 'To store extra food', 'To park cars only'], 0),
   ('Which recreation space would most likely have ice for skating in winter?', ['A skating rink', 'A library', 'A grocery store', 'A bakery'], 0),
   ('Which of these activities might happen at a community playground?', ['Children playing on swings and slides', 'Doctors performing surgery', 'Farmers growing crops', 'Firefighters putting out fires'], 0),
   ('Community recreation spaces help people by ___.', ['Giving them places to be active and connect with others', 'Keeping everyone indoors', 'Removing all green spaces', 'Making communities more crowded with buildings only'], 0)])

# ─── DAY 59 ─────────────────────────────────────────────────────────────────
d59_lang = sub('Language', 'Writing a Friendly Letter',
  'Students learn the parts of a friendly letter, including the greeting, body, closing, and signature, used to write a personal message to someone.',
  [('What part of a friendly letter greets the person you are writing to, like Dear Sam?', ['the greeting', 'greeting']),
   ('What part of a friendly letter contains the main message?', ['the body', 'body']),
   ('What part of a friendly letter comes at the end, like Your friend, before your name?', ['the closing', 'closing'])],
  [('What part of a friendly letter greets the person you are writing to?', ['The greeting', 'The body', 'The closing', 'The signature only'], 0),
   ('What part of a friendly letter contains the main message?', ['The body', 'The greeting', 'The closing', 'The date only'], 0),
   ('Which of these is an example of a greeting in a friendly letter?', ['Dear Sam,', 'Your friend,', 'The end.', 'Once upon a time.'], 0),
   ('Which of these is an example of a closing in a friendly letter?', ['Your friend,', 'Dear Sam,', 'Chapter One', 'The Title'], 0),
   ('A friendly letter is most often written to ___.', ['Share a personal message with someone you know', 'Give a weather report', 'List math problems', 'Explain science facts only'], 0)])

d59_math = sub('Math', 'Finding the Mode in a Data Set',
  'Students learn that the mode of a data set is the number or item that appears most often, helping to summarize information collected in a survey or chart.',
  [('What do we call the number or item that appears most often in a data set?', ['mode', 'the mode']),
   ('In the data set 2, 3, 3, 5, 3, what number appears most often?', ['3', 'three']),
   ('If most classmates picked red as their favourite colour, what is the mode of that survey?', ['red'])],
  [('What do we call the number or item that appears most often in a data set?', ['Mode', 'Perimeter', 'Area', 'Fraction'], 0),
   ('In the data set 2, 3, 3, 5, 3, what number appears most often?', ['3', '2', '5', '4'], 0),
   ('If most classmates in a survey picked red as their favourite colour, what is the mode?', ['Red', 'Blue', 'Green', 'Yellow'], 0),
   ('In the data set 7, 7, 8, 9, 9, 9, what is the mode?', ['9', '7', '8', 'There is no mode'], 0),
   ('Finding the mode of a data set helps us know ___.', ['Which item or number appears most often', 'How much something weighs', 'How long something is', 'What time it is'], 0)])

d59_sci = sub('Science', 'Where Energy Comes From: Sun, Wind, and Water',
  'Students learn that energy can come from natural sources such as the sun, wind, and moving water, which can be used to create electricity and power homes.',
  [('Name one natural source of energy, like the sun or wind.', ['the sun', 'sun', 'wind', 'water']),
   ('What do we call panels that capture energy from the sun?', ['solar panels']),
   ('Name one machine that uses wind to create energy, like a wind turbine.', ['a wind turbine', 'wind turbine'])],
  [('Which of these is a natural source of energy?', ['The sun', 'A plastic bag', 'A cardboard box', 'A rubber ball'], 0),
   ('What do we call panels that capture energy from sunlight?', ['Solar panels', 'Wind turbines', 'Water wheels', 'Batteries only'], 0),
   ('Which machine uses wind to create energy?', ['A wind turbine', 'A solar panel', 'A dam', 'A battery'], 0),
   ('Moving water, like a river through a dam, can be used to create ___.', ['Electricity', 'Sunlight', 'Wind', 'Soil'], 0),
   ('Using natural sources like sun, wind, and water for energy is helpful because they ___.', ['Can be used again and again without running out', 'Always cause pollution', 'Disappear after one use', 'Cannot power anything'], 0)])

d59_ss = sub('SocialStudies', 'Museums and Historical Sites: Learning About the Past',
  'Students learn that museums and historical sites help people learn about the past by displaying old objects, artifacts, and stories from earlier times.',
  [('What do we call a place that displays old objects and artifacts for people to learn from?', ['a museum', 'museum']),
   ('What do we call an old object that helps us learn about the past, like an old tool?', ['an artifact', 'artifact']),
   ('Name one reason people visit museums, like to learn about history.', ['to learn about history', 'to learn about the past'])],
  [('What do we call a place that displays old objects and artifacts for people to learn from?', ['A museum', 'A farm', 'A bank', 'A factory'], 0),
   ('What do we call an old object that helps us learn about people from the past?', ['An artifact', 'A calendar', 'A recipe', 'A map only'], 0),
   ('Why might a class visit a historical site on a field trip?', ['To learn about important events from the past', 'To buy groceries', 'To play sports', 'To watch a movie'], 0),
   ('Which of these might you find displayed inside a museum?', ['Old tools and artifacts', 'Fresh vegetables', 'New cars for sale', 'Restaurant menus'], 0),
   ('Museums and historical sites help communities by ___.', ['Preserving and sharing stories from the past', 'Erasing history completely', 'Hiding artifacts from everyone', 'Selling old objects only'], 0)])

# ─── DAY 60 (Final Review) ──────────────────────────────────────────────────
d60_lang = sub('Language', 'Final Review: Language Skills (Days 51-59)',
  'Students review Language skills from Days 51 to 59: past tense verbs, capitalization, multiple-meaning words, context clues, onomatopoeia, text features, purpose for writing, story theme, and friendly letters.',
  [('What is the past tense of the verb jump?', ['jumped']),
   ('What do we call a word that has more than one meaning?', ['a multiple-meaning word', 'multiple-meaning word']),
   ('What do we call the main lesson or message of a story?', ['theme', 'the theme'])],
  [('What ending do we usually add to a verb to show something already happened?', ['-ed', '-ing', '-er', '-est'], 0),
   ('What kind of letter starts the name of a person, like Sarah?', ['A capital letter', 'A lowercase letter', 'A number', 'A silent letter'], 0),
   ('What do we call the words and sentences around an unfamiliar word that help us understand its meaning?', ['Context clues', 'Rhyming words', 'Compound words', 'Silent letters'], 0),
   ('What is the purpose of writing that gives readers facts and information?', ['To inform', 'To entertain', 'To persuade', 'To rhyme'], 0),
   ('What part of a friendly letter contains the main message?', ['The body', 'The greeting', 'The closing', 'The date only'], 0)])

d60_math = sub('Math', 'Final Review: Math Skills (Days 51-59)',
  'Students review Math skills from Days 51 to 59: skip counting by 3s and 4s, division, probability, number lines, measuring mass and capacity, comparing money, sorting 3D objects, and finding the mode.',
  [('Skip count by 3s: 3, 6, 9, ___', ['12', 'twelve']),
   ('What do we call splitting a group of objects equally into smaller groups?', ['division', 'sharing equally']),
   ('What do we call the number or item that appears most often in a data set?', ['mode', 'the mode'])],
  [('Skip count by 4s: 4, 8, 12, ___', ['16', '14', '15', '20'], 0),
   ('If you share 12 apples equally among 3 friends, how many apples does each friend get?', ['4', '3', '6', '12'], 0),
   ('Is it likely or unlikely that it will snow in Ontario in July?', ['Unlikely', 'Certain', 'Likely', 'Impossible'], 0),
   ('What unit would you most likely use to measure the water in a bathtub?', ['Litres', 'Millilitres', 'Grams', 'Centimetres'], 0),
   ('Which 3D shape has six flat square faces?', ['Cube', 'Sphere', 'Cone', 'Cylinder'], 0)])

d60_sci = sub('Science', 'Final Review: Science Skills (Days 51-59)',
  'Students review Science topics from Days 51 to 59: animal camouflage, butterfly metamorphosis, bones and muscles, moon phases, erosion, static electricity, endangered animals, dental care, and energy sources.',
  [('What word describes an animal blending into its surroundings using color or pattern?', ['camouflage']),
   ('What do we call the changing shapes of the moon that we see in the sky?', ['phases of the moon', 'moon phases']),
   ('What word describes an animal that is at risk of disappearing forever?', ['endangered'])],
  [('Why might an animal use camouflage?', ['To hide from predators or sneak up on prey', 'To fly faster', 'To make more noise', 'To change the weather'], 0),
   ('What do we call the stage where a caterpillar forms a hard case and changes shape?', ['Chrysalis', 'Nest', 'Burrow', 'Web'], 0),
   ('What do we call it when wind and water slowly wear away rock and soil?', ['Erosion', 'Pollination', 'Migration', 'Hibernation'], 0),
   ('What kind of electricity builds up when you rub a balloon on your hair?', ['Static electricity', 'Circuit electricity', 'Solar electricity', 'Wind electricity'], 0),
   ('Which of these is a natural source of energy?', ['The sun', 'A plastic bag', 'A cardboard box', 'A rubber ball'], 0)])

d60_ss = sub('SocialStudies', 'Final Review: Social Studies Skills (Days 51-59)',
  'Students review Social Studies topics from Days 51 to 59: notable Canadians, Canadian inventions, water systems, homes around the world, Canadian sports, settlement patterns, the history of money, community recreation, and museums.',
  [('What word describes a person who is well known for an important contribution?', ['notable', 'famous']),
   ('What do we call a place that cleans water before it reaches our homes?', ['a treatment plant', 'treatment plant', 'water treatment plant']),
   ('What do we call a place that displays old objects and artifacts for people to learn from?', ['a museum', 'museum'])],
  [('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Baseball', 'Tennis'], 0),
   ('How does clean water usually travel from a treatment plant to our homes?', ['Through underground pipes', 'By truck only', 'By airplane', 'By boat only'], 0),
   ('Which sport is widely played and watched across Canada, especially in winter?', ['Hockey', 'Surfing', 'Bullfighting', 'Sumo wrestling'], 0),
   ('Why did societies eventually begin using coins instead of only trading goods?', ['Coins made trading easier and fairer', 'Coins made trading impossible', 'Coins removed the need for goods', 'Coins were heavier than goods'], 0),
   ('Why might a class visit a historical site on a field trip?', ['To learn about important events from the past', 'To buy groceries', 'To play sports', 'To watch a movie'], 0)])


g2_51_60 = [
    day(51, [d51_lang, d51_math, d51_sci, d51_ss]),
    day(52, [d52_lang, d52_math, d52_sci, d52_ss]),
    day(53, [d53_lang, d53_math, d53_sci, d53_ss]),
    day(54, [d54_lang, d54_math, d54_sci, d54_ss]),
    day(55, [d55_lang, d55_math, d55_sci, d55_ss]),
    day(56, [d56_lang, d56_math, d56_sci, d56_ss]),
    day(57, [d57_lang, d57_math, d57_sci, d57_ss]),
    day(58, [d58_lang, d58_math, d58_sci, d58_ss]),
    day(59, [d59_lang, d59_math, d59_sci, d59_ss]),
    day(60, [d60_lang, d60_math, d60_sci, d60_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_51_60, seed=20260830)
    append_worksheet_days(2, g2_51_60)
