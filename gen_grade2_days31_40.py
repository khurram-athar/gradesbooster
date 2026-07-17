#!/usr/bin/env python3
"""Grade 2, Days 31-40 -- FIRST batch extending Grade 2 past Day 30.
Self-contained script modeled exactly on gen_grade1_days61_70.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-30 topics (see data/grade2.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely (or
written without the apostrophe, e.g. "Canadas") to keep the generated
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


# ─── DAY 31 ─────────────────────────────────────────────────────────────────
d31_lang = sub('Language', 'Consonant Blends: bl, cl, fl, gl',
  'Students learn beginning consonant blends where two consonants join and both sounds are heard, such as bl in black, cl in clap, fl in flag, and gl in glow.',
  [('Name one word that begins with the bl blend, like black or blue.', ['black', 'blue', 'blow', 'blob']),
   ('What two letters begin the word clap?', ['cl']),
   ('Name one word that begins with the gl blend, like glow or glue.', ['glow', 'glue', 'glass'])],
  [('Which word begins with the bl blend?', ['Black', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the cl blend?', ['Clap', 'Cat', 'Bed', 'Sun'], 0),
   ('Which word begins with the fl blend?', ['Flag', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the gl blend?', ['Glow', 'Cat', 'Dog', 'Sun'], 0),
   ('A consonant blend is two consonants that ___.', ['Blend together with both sounds heard', 'Never appear together', 'Always make one new sound like a digraph', 'Are always silent'], 0)])

d31_math = sub('Math', 'Addition Within 100 (With Regrouping)',
  'Students add two-digit numbers within 100 that require regrouping a ten when the ones digits add to 10 or more.',
  [('What is 27 + 15?', ['42', 'forty-two', 'forty two']),
   ('When adding 38 + 26, do the ones digits add up to 10 or more?', ['yes']),
   ('What is 46 + 19?', ['65', 'sixty-five', 'sixty five'])],
  [('What is 27 + 15?', ['42', '41', '43', '32'], 0),
   ('What is 38 + 26?', ['64', '63', '65', '54'], 0),
   ('What is 46 + 19?', ['65', '64', '66', '55'], 0),
   ('When the ones digits add to 10 or more, we ___.', ['Regroup a ten into the tens column', 'Ignore the extra', 'Subtract instead', 'Stop the problem'], 0),
   ('What is 55 + 27?', ['82', '81', '83', '72'], 0)])

d31_sci = sub('Science', 'Nocturnal Animals: Creatures of the Night',
  'Students learn that nocturnal animals, such as owls and bats, are awake and active at night and sleep during the day, often having special senses like keen hearing or eyesight to help them in the dark.',
  [('What do we call an animal that is awake mostly at night?', ['a nocturnal animal', 'nocturnal']),
   ('Name one nocturnal animal, like an owl or a bat.', ['an owl', 'owl', 'a bat', 'bat']),
   ('Do nocturnal animals usually sleep during the day?', ['yes'])],
  [('What do we call an animal that is active mainly at night?', ['A nocturnal animal', 'A diurnal animal', 'A hibernating animal', 'A migrating animal'], 0),
   ('Which of these animals is known for being nocturnal?', ['An owl', 'A robin', 'A squirrel', 'A butterfly'], 0),
   ('Nocturnal animals usually sleep during ___.', ['The day', 'The night', 'Every other hour', 'Only in winter'], 0),
   ('Why might keen hearing help a nocturnal animal?', ['It helps them find food and avoid danger in the dark', 'It helps them fly to warmer places', 'It helps them change colour', 'It helps them build nests only'], 0),
   ('Which sense often helps owls hunt at night?', ['Hearing and sight', 'Taste only', 'Smell only', 'Touch only'], 0)])

d31_ss = sub('SocialStudies', 'Farms and Where Our Food Comes From',
  'Students learn that much of our food is grown or raised on farms, where farmers grow crops like wheat and vegetables and raise animals like cows and chickens, before the food travels to stores.',
  [('Name one place where much of our food is grown or raised.', ['a farm', 'farm']),
   ('Name one crop a farmer might grow, like wheat or corn.', ['wheat', 'corn', 'vegetables']),
   ('Does food usually travel from a farm to a store before we buy it?', ['yes'])],
  [('Where does much of our food come from before it reaches a store?', ['A farm', 'A library', 'A hospital', 'A school'], 0),
   ('Which of these is a crop a farmer might grow?', ['Wheat', 'A car', 'A shoe', 'A television'], 0),
   ('Which of these animals might a farmer raise for food?', ['A cow', 'A lion', 'A whale', 'A tiger'], 0),
   ('After food is grown or raised on a farm, it usually ___.', ['Travels to stores for people to buy', 'Stays on the farm forever', 'Disappears completely', 'Is never eaten'], 0),
   ('Why are farms important to communities?', ['They grow and raise much of the food we eat', 'They build houses', 'They print newspapers', 'They teach students'], 0)])

# ─── DAY 32 ─────────────────────────────────────────────────────────────────
d32_lang = sub('Language', 'Consonant Digraphs: sh, ch, th, wh',
  'Students learn that a consonant digraph is two consonants that combine to make one new sound, such as sh in ship, ch in chip, th in thin, and wh in whale.',
  [('What two letters make the beginning sound in the word ship?', ['sh']),
   ('Name one word that begins with the ch digraph, like chip or chair.', ['chip', 'chair', 'chin']),
   ('What two letters make the beginning sound in the word whale?', ['wh'])],
  [('Which word begins with the sh digraph?', ['Ship', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the ch digraph?', ['Chip', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the th digraph?', ['Thin', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the wh digraph?', ['Whale', 'Cat', 'Dog', 'Sun'], 0),
   ('A consonant digraph is two consonants that ___.', ['Combine to make one new sound', 'Always keep both sounds separate', 'Are always silent', 'Never appear together'], 0)])

d32_math = sub('Math', 'Subtraction Within 100 (With Regrouping)',
  'Students subtract two-digit numbers within 100 that require regrouping a ten when the ones digit of the first number is smaller than the ones digit being subtracted.',
  [('What is 52 - 27?', ['25', 'twenty-five', 'twenty five']),
   ('When subtracting 43 - 18, is the ones digit 3 smaller than 8?', ['yes']),
   ('What is 71 - 36?', ['35', 'thirty-five', 'thirty five'])],
  [('What is 52 - 27?', ['25', '24', '26', '35'], 0),
   ('What is 43 - 18?', ['25', '24', '26', '35'], 0),
   ('What is 71 - 36?', ['35', '34', '36', '45'], 0),
   ('We regroup (borrow) a ten when ___.', ['The ones digit we are subtracting from is too small', 'The numbers are both even', 'We are adding not subtracting', 'The tens digits are equal'], 0),
   ('What is 80 - 45?', ['35', '34', '36', '45'], 0)])

d32_sci = sub('Science', 'Insects and Their Body Parts',
  'Students learn that insects are small animals with six legs and three main body parts, head, thorax, and abdomen, and that many insects also have wings and antennae.',
  [('How many legs does an insect have?', ['6', 'six']),
   ('Name the three main body parts of an insect: head, thorax, and ___.', ['abdomen']),
   ('Name one body part many insects use to sense their surroundings, like antennae.', ['antennae', 'wings'])],
  [('How many legs does an insect have?', ['Six', 'Eight', 'Four', 'Ten'], 0),
   ('What are the three main body parts of an insect?', ['Head, thorax, and abdomen', 'Head, tail, and wings', 'Legs, eyes, and fur', 'Shell, fin, and gills'], 0),
   ('Which body part do many insects use to sense their surroundings?', ['Antennae', 'Fur', 'Gills', 'Fins'], 0),
   ('Which of these is an example of an insect?', ['A ladybug', 'A spider', 'A worm', 'A snail'], 0),
   ('How is a spider different from an insect?', ['A spider has eight legs, not six', 'A spider has six legs, not eight', 'A spider has wings', 'An insect has eight legs'], 0)])

d32_ss = sub('SocialStudies', 'Community Types: City, Suburb, and Countryside',
  'Students compare different types of communities, such as a busy city with tall buildings, a quieter suburb with houses close together, and the countryside with farms and open land.',
  [('Name one type of community with tall buildings and many people, like a city.', ['a city', 'city']),
   ('Name one type of community with farms and open land, like the countryside.', ['the countryside', 'countryside', 'rural area']),
   ('Are suburbs usually busier than the countryside but quieter than a city?', ['yes'])],
  [('Which type of community usually has tall buildings and many people?', ['A city', 'The countryside', 'A forest', 'An ocean'], 0),
   ('Which type of community usually has farms and open land?', ['The countryside', 'A city', 'A subway', 'A skyscraper'], 0),
   ('A suburb is usually ___.', ['Between a city and the countryside in size and busyness', 'Busier than any city', 'The same as a farm', 'Found only underwater'], 0),
   ('Which of these might you find in a city but not usually in the countryside?', ['Many tall buildings close together', 'Wide open fields', 'Large farms', 'Quiet forests only'], 0),
   ('Why do different communities look different from each other?', ['They are built to fit the land and the needs of the people there', 'All communities look exactly the same', 'Communities never change', 'Only cities have people'], 0)])

# ─── DAY 33 ─────────────────────────────────────────────────────────────────
d33_lang = sub('Language', 'Common and Proper Nouns',
  'Students learn that a common noun names a general person, place, or thing, like city or dog, while a proper noun names a specific one and begins with a capital letter, like Toronto or Rex.',
  [('Is the word dog a common noun or a proper noun?', ['common noun', 'common']),
   ('Is the word Toronto a common noun or a proper noun?', ['proper noun', 'proper']),
   ('Should a proper noun begin with a capital letter?', ['yes'])],
  [('Which of these is a common noun?', ['Dog', 'Toronto', 'Canada', 'Monday'], 0),
   ('Which of these is a proper noun?', ['Toronto', 'city', 'dog', 'boy'], 0),
   ('A proper noun always begins with a ___.', ['Capital letter', 'Lowercase letter', 'Number', 'Question mark'], 0),
   ('Which sentence uses a proper noun correctly?', ['My friend lives in Toronto.', 'My friend lives in toronto.', 'my friend lives in Toronto.', 'My Friend lives in toronto.'], 0),
   ('Which of these is a common noun, not a proper noun?', ['City', 'Canada', 'Monday', 'Toronto'], 0)])

d33_math = sub('Math', 'Telling Time to Five-Minute Intervals',
  'Students learn to read an analog clock to the nearest five minutes, counting by 5s around the clock face starting from the 12.',
  [('If the minute hand points to the 3, how many minutes past the hour is it?', ['15']),
   ('If the minute hand points to the 6, how many minutes past the hour is it?', ['30']),
   ('Counting by 5s around a clock face, what number comes after 20?', ['25'])],
  [('If the minute hand points to the 3, what time is it past the hour?', ['15 minutes', '5 minutes', '20 minutes', '30 minutes'], 0),
   ('If the minute hand points to the 6, what time is it past the hour?', ['30 minutes', '15 minutes', '45 minutes', '6 minutes'], 0),
   ('If the minute hand points to the 9, what time is it past the hour?', ['45 minutes', '9 minutes', '30 minutes', '15 minutes'], 0),
   ('When reading a clock, each number represents ___ minutes.', ['5', '1', '10', '15'], 0),
   ('If the hour hand is between 2 and 3, and the minute hand points to the 6, what time is it?', ['2:30', '3:30', '2:15', '6:02'], 0)])

d33_sci = sub('Science', 'Recycling and Reducing Waste',
  'Students learn that recycling turns used materials like paper, plastic, and glass into new products, and that reducing and reusing waste helps protect the environment.',
  [('Name one material that can be recycled, like paper or plastic.', ['paper', 'plastic', 'glass']),
   ('What do we call turning used materials into new products?', ['recycling']),
   ('Name one way to reduce waste, like reusing a bag.', ['reusing a bag', 'reusing', 'using less'])],
  [('What is recycling?', ['Turning used materials into new products', 'Throwing everything away', 'Burning all garbage', 'Burying all waste'], 0),
   ('Which of these materials can often be recycled?', ['Paper', 'Food scraps only', 'Water', 'Air'], 0),
   ('Which action helps reduce waste?', ['Reusing a shopping bag', 'Throwing away items that still work', 'Buying more than you need', 'Wasting paper'], 0),
   ('Why is recycling helpful for the environment?', ['It saves materials and reduces garbage', 'It creates more garbage', 'It uses up more resources', 'It has no effect'], 0),
   ('Which of these bins would glass bottles most likely go into?', ['A recycling bin', 'A garden', 'A pond', 'A closet'], 0)])

d33_ss = sub('SocialStudies', 'Provinces and Territories of Canada',
  'Students learn that Canada is divided into ten provinces and three territories, each with its own capital city, and that Ontario is the province where they live.',
  [('What do we call the large regions Canada is divided into, like Ontario?', ['provinces']),
   ('How many provinces does Canada have?', ['10', 'ten']),
   ('Name the province where Ontario students live.', ['Ontario'])],
  [('What do we call the large regions Canada is divided into, such as Ontario and Quebec?', ['Provinces', 'Countries', 'Continents', 'Oceans'], 0),
   ('How many provinces does Canada have?', ['10', '5', '13', '3'], 0),
   ('Besides provinces, Canada also has three ___.', ['Territories', 'Oceans', 'Continents', 'Capitals'], 0),
   ('Which of these is a province in Canada?', ['Ontario', 'Texas', 'London', 'France'], 0),
   ('Each province and territory in Canada has its own ___.', ['Capital city', 'Ocean', 'Continent', 'Language spoken by everyone'], 0)])

# ─── DAY 34 ─────────────────────────────────────────────────────────────────
d34_lang = sub('Language', 'Pronouns: He, She, It, They',
  'Students learn that a pronoun is a word that can take the place of a noun, such as using he for a boy, she for a girl, it for a thing, and they for more than one person or thing.',
  [('Which pronoun could replace the word boy?', ['he']),
   ('Which pronoun could replace the word girl?', ['she']),
   ('Which pronoun could replace the words the dogs?', ['they'])],
  [('Which pronoun could replace the noun Sam if Sam is a boy?', ['He', 'She', 'It', 'They'], 0),
   ('Which pronoun could replace the noun Maria if Maria is a girl?', ['She', 'He', 'It', 'They'], 0),
   ('Which pronoun could replace the words the two cats?', ['They', 'He', 'She', 'It'], 0),
   ('Which pronoun could replace the word ball?', ['It', 'He', 'She', 'They'], 0),
   ('A pronoun is a word that ___.', ['Takes the place of a noun', 'Describes a noun', 'Shows an action', 'Joins two sentences'], 0)])

d34_math = sub('Math', 'Measuring Length with Centimetres and Metres',
  'Students learn to measure the length of objects using standard units, choosing centimetres for shorter objects like a pencil and metres for longer distances like a hallway.',
  [('Would you use centimetres or metres to measure a pencil?', ['centimetres']),
   ('Would you use centimetres or metres to measure the length of a hallway?', ['metres']),
   ('Which is longer, 1 metre or 1 centimetre?', ['1 metre', 'metre'])],
  [('Which unit would you use to measure the length of a pencil?', ['Centimetres', 'Metres', 'Kilograms', 'Litres'], 0),
   ('Which unit would you use to measure the length of a hallway?', ['Metres', 'Centimetres', 'Millilitres', 'Degrees'], 0),
   ('Which is longer, 1 metre or 1 centimetre?', ['1 metre', '1 centimetre', 'They are equal', 'Cannot tell'], 0),
   ('About how many centimetres long is a small paperclip?', ['About 3 centimetres', 'About 3 metres', 'About 30 metres', 'About 300 centimetres'], 0),
   ('Choosing the right unit helps us measure length ___.', ['Accurately', 'Randomly', 'Incorrectly', 'Loudly'], 0)])

d34_sci = sub('Science', 'States of Matter: Gases',
  'Students learn that a gas is a state of matter that has no definite shape or volume and spreads out to fill its container, such as the air we breathe.',
  [('Name one example of a gas, like air.', ['air']),
   ('Does a gas have a definite shape?', ['no']),
   ('What state of matter fills up all the space in its container?', ['a gas', 'gas'])],
  [('Which of these is an example of a gas?', ['Air', 'A rock', 'Ice', 'Juice'], 0),
   ('Does a gas have a definite shape of its own?', ['No, it takes the shape of its container', 'Yes, it always keeps one shape', 'Only sometimes', 'Only when frozen'], 0),
   ('What happens to a gas inside a balloon?', ['It spreads out to fill the whole balloon', 'It stays in one corner', 'It turns into a solid', 'It disappears completely'], 0),
   ('Which of the three states of matter usually cannot be seen?', ['Gas', 'Solid', 'Liquid', 'None of them'], 0),
   ('Water can become a gas called water vapour when it ___.', ['Evaporates and turns into a gas', 'Freezes solid', 'Turns into a rock', 'Becomes colder'], 0)])

d34_ss = sub('SocialStudies', 'Municipal Government: Mayors and Councils',
  'Students learn that a municipal government, led by a mayor and council, makes decisions for a city or town, such as caring for parks, roads, and local services.',
  [('What do we call the leader of a city or town government?', ['a mayor', 'mayor']),
   ('Name one thing a municipal government might take care of, like roads or parks.', ['roads', 'parks', 'local services']),
   ('Do people in a community vote to choose their mayor and council?', ['yes'])],
  [('Who usually leads a city or town government?', ['A mayor', 'A king', 'A principal', 'A farmer'], 0),
   ('Which of these is something a municipal government might take care of?', ['Local roads and parks', 'Ocean currents', 'Outer space', 'The weather'], 0),
   ('How do people in a community usually choose their mayor?', ['By voting in an election', 'By flipping a coin', 'By age only', 'It is never chosen'], 0),
   ('A group of elected people who help run a city along with the mayor is called the ___.', ['City council', 'School board', 'Sports team', 'Farmers market'], 0),
   ('Why is local government important to a community?', ['It makes decisions that affect daily life, like roads and parks', 'It has no effect on daily life', 'It only affects other countries', 'It never makes decisions'], 0)])

# ─── DAY 35 (Review) ────────────────────────────────────────────────────────
d35_lang = sub('Language', 'Review: Blends, Digraphs, Nouns and Pronouns',
  'Students review recent Language skills: consonant blends, consonant digraphs, common and proper nouns, and pronouns.',
  [('Name one word that begins with the bl blend, like black or blue.', ['black', 'blue', 'blow']),
   ('What two letters make the beginning sound in the word ship?', ['sh']),
   ('Which pronoun could replace the word boy?', ['he'])],
  [('Which word begins with the bl blend?', ['Black', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with the sh digraph?', ['Ship', 'Cat', 'Dog', 'Sun'], 0),
   ('Which of these is a proper noun?', ['Toronto', 'city', 'dog', 'boy'], 0),
   ('Which pronoun could replace the words the two cats?', ['They', 'He', 'She', 'It'], 0),
   ('A consonant digraph is two consonants that ___.', ['Combine to make one new sound', 'Always keep both sounds separate', 'Are always silent', 'Never appear together'], 0)])

d35_math = sub('Math', 'Review: Regrouping, Time and Measuring',
  'Students review recent Math skills: addition and subtraction within 100 with regrouping, telling time to five-minute intervals, and measuring length with centimetres and metres.',
  [('What is 27 + 15?', ['42', 'forty-two', 'forty two']),
   ('If the minute hand points to the 6, how many minutes past the hour is it?', ['30']),
   ('Would you use centimetres or metres to measure a pencil?', ['centimetres'])],
  [('What is 27 + 15?', ['42', '41', '43', '32'], 0),
   ('What is 52 - 27?', ['25', '24', '26', '35'], 0),
   ('If the minute hand points to the 3, what time is it past the hour?', ['15 minutes', '5 minutes', '20 minutes', '30 minutes'], 0),
   ('Which unit would you use to measure the length of a hallway?', ['Metres', 'Centimetres', 'Millilitres', 'Degrees'], 0),
   ('What is 46 + 19?', ['65', '64', '66', '55'], 0)])

d35_sci = sub('Science', 'Review: Nocturnal Animals, Insects, Recycling and Gases',
  'Students review recent Science topics: nocturnal animals, insects and their body parts, recycling and reducing waste, and the gas state of matter.',
  [('Name one nocturnal animal, like an owl or a bat.', ['an owl', 'owl', 'a bat', 'bat']),
   ('How many legs does an insect have?', ['6', 'six']),
   ('Name one material that can be recycled, like paper or plastic.', ['paper', 'plastic', 'glass'])],
  [('Which of these animals is known for being nocturnal?', ['An owl', 'A robin', 'A squirrel', 'A butterfly'], 0),
   ('What are the three main body parts of an insect?', ['Head, thorax, and abdomen', 'Head, tail, and wings', 'Legs, eyes, and fur', 'Shell, fin, and gills'], 0),
   ('Which of these materials can often be recycled?', ['Paper', 'Food scraps only', 'Water', 'Air'], 0),
   ('Which of these is an example of a gas?', ['Air', 'A rock', 'Ice', 'Juice'], 0),
   ('Why are nocturnal animals often good at hearing or seeing in the dark?', ['It helps them find food and avoid danger at night', 'It helps them fly to warmer places', 'It helps them change colour', 'It helps them build nests only'], 0)])

d35_ss = sub('SocialStudies', 'Review: Food Sources, Community Types, Provinces and Local Government',
  'Students review recent Social Studies topics: where food comes from, types of communities, the provinces and territories of Canada, and municipal government.',
  [('Name one place where much of our food is grown or raised.', ['a farm', 'farm']),
   ('Name one type of community with tall buildings and many people, like a city.', ['a city', 'city']),
   ('How many provinces does Canada have?', ['10', 'ten'])],
  [('Where does much of our food come from before it reaches a store?', ['A farm', 'A library', 'A hospital', 'A school'], 0),
   ('Which type of community usually has farms and open land?', ['The countryside', 'A city', 'A subway', 'A skyscraper'], 0),
   ('How many provinces does Canada have?', ['10', '5', '13', '3'], 0),
   ('Who usually leads a city or town government?', ['A mayor', 'A king', 'A principal', 'A farmer'], 0),
   ('Why are farms important to communities?', ['They grow and raise much of the food we eat', 'They build houses', 'They print newspapers', 'They teach students'], 0)])

# ─── DAY 36 ─────────────────────────────────────────────────────────────────
d36_lang = sub('Language', 'Prefixes: un- and re-',
  'Students learn that the prefixes un- and re- can be added to the beginning of a word to change its meaning, with un- often meaning not, and re- often meaning again.',
  [('What does the prefix un- usually mean, as in unhappy?', ['not']),
   ('What does the prefix re- usually mean, as in redo?', ['again']),
   ('Name one word that begins with the prefix un-, like unhappy or unsafe.', ['unhappy', 'unsafe', 'unfair'])],
  [('What does the prefix un- usually mean?', ['Not', 'Again', 'Before', 'Always'], 0),
   ('What does the prefix re- usually mean?', ['Again', 'Not', 'Never', 'Before'], 0),
   ('Which word means to do something again by using the prefix re-?', ['Redo', 'Undo', 'Predo', 'Disdo'], 0),
   ('Which word means not happy by using the prefix un-?', ['Unhappy', 'Rehappy', 'Prehappy', 'Dishappy'], 0),
   ('A prefix is added to the ___ of a word to change its meaning.', ['Beginning', 'End', 'Middle', 'Nowhere'], 0)])

d36_math = sub('Math', 'Fractions: Thirds and Eighths',
  'Students explore fractions with thirds and eighths, understanding that a whole can be split into 3 or 8 equal parts, each called one third or one eighth.',
  [('If a pizza is cut into 3 equal parts, what is each part called?', ['one third', 'a third']),
   ('If a chocolate bar is cut into 8 equal parts, what is each part called?', ['one eighth', 'an eighth']),
   ('Which is bigger, one third or one eighth of the same whole?', ['one third', 'a third'])],
  [('If a whole is split into 3 equal parts, each part is called ___.', ['One third', 'One eighth', 'One half', 'One quarter'], 0),
   ('If a whole is split into 8 equal parts, each part is called ___.', ['One eighth', 'One third', 'One half', 'One whole'], 0),
   ('Which is bigger, one third or one eighth of the same pizza?', ['One third', 'One eighth', 'They are equal', 'Cannot tell'], 0),
   ('Three friends sharing a pizza equally would each get ___ of the pizza.', ['One third', 'One eighth', 'One half', 'The whole pizza'], 0),
   ('Splitting a whole into more equal parts makes each part ___.', ['Smaller', 'Bigger', 'Stay the same size', 'Disappear'], 0)])

d36_sci = sub('Science', 'Magnets: Push and Pull Without Touching',
  'Students learn that a magnet can push or pull certain metal objects without touching them, and that magnets have two ends called poles that can attract or repel each other.',
  [('What do we call the force a magnet uses to attract or push away objects?', ['magnetism', 'magnetic force']),
   ('Name one material that a magnet can attract, like iron or steel.', ['iron', 'steel']),
   ('Do magnets have two ends called poles?', ['yes'])],
  [('What can a magnet do to certain metal objects without touching them?', ['Push or pull them', 'Change their colour', 'Make them disappear', 'Melt them'], 0),
   ('Which of these materials would a magnet most likely attract?', ['An iron nail', 'A wooden block', 'A plastic cup', 'A paper towel'], 0),
   ('What do we call the two ends of a magnet?', ['Poles', 'Corners', 'Tips', 'Wheels'], 0),
   ('What happens when two magnets with the same pole are brought close together?', ['They push each other away', 'They always stick together', 'They disappear', 'They melt'], 0),
   ('What happens when two magnets with opposite poles are brought close together?', ['They attract and pull together', 'They always push apart', 'They disappear', 'They melt'], 0)])

d36_ss = sub('SocialStudies', 'Immigration: New Families Joining Canada',
  'Students learn that immigration is when people move from one country to make a new home in another country, and that many families have come to Canada from around the world, adding to its cultures and traditions.',
  [('What do we call it when people move from one country to live in another?', ['immigration']),
   ('What do we call a person who moves to a new country to live?', ['an immigrant', 'immigrant']),
   ('Do families who immigrate to Canada bring their own traditions and cultures?', ['yes'])],
  [('What is immigration?', ['When people move from one country to live in another', 'When people travel on vacation', 'When animals migrate with the seasons', 'When a family moves within the same city'], 0),
   ('What do we call a person who has moved to a new country to live?', ['An immigrant', 'A tourist', 'A citizen only', 'A visitor only'], 0),
   ('Why might a family choose to immigrate to Canada?', ['To find new opportunities, safety, or to be with family', 'Canada has no reasons to immigrate to', 'Only for a short vacation', 'To avoid all other countries'], 0),
   ('How do immigrant families often help Canadian communities?', ['By sharing their cultures, languages, and traditions', 'By keeping to themselves only', 'They do not help communities', 'By changing nothing about the community'], 0),
   ('Canada is often described as a country made up of ___.', ['People from many different cultures and backgrounds', 'Only one culture', 'No immigrants at all', 'Only people born in Canada'], 0)])

# ─── DAY 37 ─────────────────────────────────────────────────────────────────
d37_lang = sub('Language', 'Suffixes: -ful and -less',
  'Students learn that the suffixes -ful and -less can be added to the end of a word, with -ful often meaning full of, and -less often meaning without.',
  [('What does the suffix -ful usually mean, as in joyful?', ['full of']),
   ('What does the suffix -less usually mean, as in helpless?', ['without']),
   ('Name one word that ends in -ful, like joyful or careful.', ['joyful', 'careful', 'colourful'])],
  [('What does the suffix -ful usually mean?', ['Full of', 'Without', 'Before', 'Again'], 0),
   ('What does the suffix -less usually mean?', ['Without', 'Full of', 'Always', 'Never before'], 0),
   ('Which word means without help by using the suffix -less?', ['Helpless', 'Helpful', 'Prehelp', 'Rehelp'], 0),
   ('Which word means full of joy by using the suffix -ful?', ['Joyful', 'Joyless', 'Rejoy', 'Prejoy'], 0),
   ('A suffix is added to the ___ of a word to change its meaning.', ['End', 'Beginning', 'Middle', 'Nowhere'], 0)])

d37_math = sub('Math', 'Odd and Even Numbers',
  'Students learn to identify odd and even numbers, understanding that even numbers can be split into two equal groups and odd numbers cannot.',
  [('Is the number 8 odd or even?', ['even']),
   ('Is the number 7 odd or even?', ['odd']),
   ('Can an even number always be split into two equal groups?', ['yes'])],
  [('Is the number 8 odd or even?', ['Even', 'Odd', 'Neither', 'Both'], 0),
   ('Is the number 7 odd or even?', ['Odd', 'Even', 'Neither', 'Both'], 0),
   ('Which of these numbers is even?', ['10', '11', '13', '15'], 0),
   ('Which of these numbers is odd?', ['9', '8', '6', '4'], 0),
   ('An even number can always be split into ___.', ['Two equal groups', 'Three equal groups', 'No equal groups', 'Odd groups only'], 0)])

d37_sci = sub('Science', 'The Water Cycle',
  'Students learn about the water cycle, the process where water evaporates into the air, forms clouds through condensation, and falls back to the earth as precipitation like rain or snow.',
  [('What do we call water turning into vapour and rising into the air?', ['evaporation']),
   ('What do we call rain or snow falling from clouds?', ['precipitation']),
   ('Name one form precipitation can take, like rain or snow.', ['rain', 'snow'])],
  [('What do we call water turning into vapour and rising into the air?', ['Evaporation', 'Condensation', 'Precipitation', 'Freezing'], 0),
   ('What do we call water vapour forming into clouds?', ['Condensation', 'Evaporation', 'Precipitation', 'Melting'], 0),
   ('What do we call rain or snow falling from clouds to the ground?', ['Precipitation', 'Evaporation', 'Condensation', 'Freezing'], 0),
   ('Where does most of the water that evaporates come from?', ['Oceans, lakes, and rivers', 'Only swimming pools', 'Only clouds', 'Only underground caves'], 0),
   ('The water cycle describes how water ___.', ['Moves between the earth, air, and clouds again and again', 'Disappears forever after it rains', 'Never moves at all', 'Only exists in oceans'], 0)])

d37_ss = sub('SocialStudies', 'My Body Belongs to Me: Personal Safety',
  'Students learn that their body belongs to them, that they can say no to touches that make them uncomfortable, and that they should tell a trusted adult if something makes them feel unsafe.',
  [('Whose body belongs to you?', ['my body', 'mine', 'yours']),
   ('What should you do if a touch makes you feel unsafe or uncomfortable?', ['say no', 'tell a trusted adult']),
   ('Name one person who could be a trusted adult, like a parent or teacher.', ['a parent', 'parent', 'a teacher', 'teacher'])],
  [('Whose body belongs to a child?', ['Their own body belongs to them', 'Only their parents decide everything about it', 'Only their teacher', 'No one, it belongs to strangers'], 0),
   ('What can a child do if a touch makes them feel uncomfortable or unsafe?', ['Say no and tell a trusted adult', 'Stay quiet and never tell anyone', 'Ignore the feeling completely', 'Do whatever they are told'], 0),
   ('Who could be a trusted adult a child talks to about feeling unsafe?', ['A parent or teacher', 'A stranger', 'No one at all', 'Only another child'], 0),
   ('Why is it important for children to know their body belongs to them?', ['It helps them stay safe and speak up if something feels wrong', 'It has no importance', 'It only matters for adults', 'Children should never speak up'], 0),
   ('If something makes a child feel unsafe, a helpful first step is to ___.', ['Tell a trusted adult right away', 'Keep it a secret forever', 'Ignore it and hope it stops', 'Blame themselves'], 0)])

# ─── DAY 38 ─────────────────────────────────────────────────────────────────
d38_lang = sub('Language', 'Comparing with -er and -est',
  'Students learn that the suffixes -er and -est can be added to describing words to compare things, with -er comparing two things, as in taller, and -est comparing three or more, as in tallest.',
  [('If comparing two children heights, which word would you use, taller or tallest?', ['taller']),
   ('If comparing the heights of a whole class, which word would you use, taller or tallest?', ['tallest']),
   ('Add -er to the word fast to compare two runners.', ['faster'])],
  [('Which suffix compares exactly two things?', ['-er', '-est', '-ful', '-less'], 0),
   ('Which suffix compares three or more things?', ['-est', '-er', '-ful', '-less'], 0),
   ('Which word correctly compares two runners?', ['Faster', 'Fastest', 'Fast', 'Fasting'], 0),
   ('Which word correctly compares the tallest person in a whole class?', ['Tallest', 'Taller', 'Tall', 'Talling'], 0),
   ('If Sam is tall, Mia is taller, and Leo is the ___, Leo is the tallest of all three.', ['Tallest', 'Taller', 'Tall', 'Tallness'], 0)])

d38_math = sub('Math', 'Repeating Patterns with Shapes and Numbers',
  'Students identify and extend repeating patterns made from shapes, colours, or numbers, recognizing the core unit that repeats over and over.',
  [('In the pattern circle, square, circle, square, what shape comes next?', ['circle']),
   ('In the pattern 2, 4, 2, 4, 2, what number comes next?', ['4', 'four']),
   ('What do we call the smallest part of a pattern that repeats?', ['the core', 'core'])],
  [('In the pattern circle, square, circle, square, ___, what comes next?', ['Circle', 'Square', 'Triangle', 'Star'], 0),
   ('In the pattern 3, 6, 3, 6, 3, ___, what comes next?', ['6', '3', '9', '12'], 0),
   ('In the pattern red, blue, blue, red, blue, blue, ___, what comes next?', ['Red', 'Blue', 'Green', 'Yellow'], 0),
   ('What do we call the smallest part of a pattern that repeats over and over?', ['The core', 'The end', 'The middle', 'The total'], 0),
   ('A repeating pattern is one where the core ___.', ['Repeats again and again', 'Never repeats', 'Only appears once', 'Gets bigger each time'], 0)])

d38_sci = sub('Science', 'Rocks and Soil: What the Earth is Made Of',
  'Students learn that rocks come in many shapes, sizes, and colours, and that soil is made up of tiny broken bits of rock mixed with decayed plants and animals, which helps plants grow.',
  [('Name one thing soil is made of, like broken rock or decayed plants.', ['broken rock', 'decayed plants', 'tiny rock pieces']),
   ('Do rocks come in different shapes, sizes, and colours?', ['yes']),
   ('Does soil help plants grow?', ['yes'])],
  [('What is soil made up of?', ['Tiny broken bits of rock mixed with decayed plants and animals', 'Only water', 'Only metal', 'Only glass'], 0),
   ('Which of these is true about rocks?', ['They come in many shapes, sizes, and colours', 'They are all exactly the same', 'They are all soft', 'They are always tiny'], 0),
   ('Why is soil important for plants?', ['It provides nutrients and support for roots to grow', 'It stops plants from growing', 'It has no use for plants', 'It only harms plants'], 0),
   ('Over a very long time, rocks can slowly break down into ___.', ['Tiny pieces that become part of soil', 'Water', 'Gas', 'Metal'], 0),
   ('Which of these is an example of a rock?', ['Granite', 'Water', 'Air', 'Wood'], 0)])

d38_ss = sub('SocialStudies', 'Saving and Spending Money Wisely',
  'Students learn the difference between saving money for later and spending money now, and that making thoughtful choices about money helps people reach their goals.',
  [('What do we call putting money aside instead of spending it right away?', ['saving']),
   ('What do we call using money to buy something now?', ['spending']),
   ('Can saving money help you buy something bigger later?', ['yes'])],
  [('What does it mean to save money?', ['Putting money aside instead of spending it right away', 'Spending all your money right away', 'Losing your money', 'Giving all your money away'], 0),
   ('What does it mean to spend money?', ['Using money to buy something', 'Putting money away for later', 'Hiding money', 'Throwing money away'], 0),
   ('Why might someone choose to save money instead of spending it right away?', ['To buy something bigger or more important later', 'Saving money is never useful', 'To lose track of it', 'Money should never be saved'], 0),
   ('Which of these is an example of making a wise choice about money?', ['Thinking before spending and saving some for later', 'Spending every coin the moment you get it', 'Never thinking about money at all', 'Losing money on purpose'], 0),
   ('Making thoughtful choices about money can help someone ___.', ['Reach a savings goal', 'Waste all their money', 'Avoid ever having money', 'Never buy anything they want'], 0)])

# ─── DAY 39 ─────────────────────────────────────────────────────────────────
d39_lang = sub('Language', 'Writing a Simple Paragraph',
  'Students learn that a simple paragraph has a topic sentence that introduces the main idea, a few detail sentences that add information, and stays focused on one idea.',
  [('What do we call the sentence that introduces the main idea of a paragraph?', ['the topic sentence', 'topic sentence']),
   ('Should the sentences in a paragraph stay focused on one idea?', ['yes']),
   ('Name one thing a detail sentence does in a paragraph, like adding information.', ['adds information', 'gives more details'])],
  [('What is a topic sentence?', ['The sentence that introduces the main idea of a paragraph', 'The last sentence in a story', 'A sentence with no meaning', 'A question only'], 0),
   ('What do detail sentences in a paragraph do?', ['Add more information about the main idea', 'Change the topic completely', 'Ask random questions', 'End the paragraph immediately'], 0),
   ('A good paragraph usually stays focused on ___.', ['One main idea', 'Many unrelated ideas', 'No idea at all', 'Only questions'], 0),
   ('Which of these would make the best topic sentence for a paragraph about dogs?', ['Dogs make wonderful pets for many families.', 'The sky is blue today.', 'I like pizza for lunch.', 'Cars can be fast or slow.'], 0),
   ('Why is it important to stay on topic when writing a paragraph?', ['It helps the reader understand the main idea clearly', 'It confuses the reader on purpose', 'Paragraphs do not need a topic', 'Readers prefer unrelated ideas'], 0)])

d39_math = sub('Math', 'Symmetry in Shapes',
  'Students learn that a shape has symmetry if it can be folded along a line so that both halves match exactly, and that this line is called a line of symmetry.',
  [('What do we call a shape that can be folded so both halves match exactly?', ['a symmetrical shape', 'symmetrical']),
   ('What do we call the line where a symmetrical shape can be folded so both halves match?', ['a line of symmetry', 'line of symmetry']),
   ('Does a circle have a line of symmetry?', ['yes'])],
  [('A shape has symmetry if it can be folded so that ___.', ['Both halves match exactly', 'One half disappears', 'Both halves are different sizes', 'It cannot be folded at all'], 0),
   ('What do we call the line where a symmetrical shape can be folded so both halves match?', ['A line of symmetry', 'A number line', 'A border line', 'A curved line'], 0),
   ('Which of these shapes has a line of symmetry?', ['A square', 'A scribble', 'A random blob', 'An uneven shape'], 0),
   ('How many lines of symmetry does a circle have?', ['Many', 'None', 'Exactly one', 'Exactly two'], 0),
   ('Which of these letters has a line of symmetry?', ['A', 'F', 'G', 'R'], 0)])

d39_sci = sub('Science', 'Healthy Eating and the Food Groups',
  'Students learn that eating a balance of different food groups, such as fruits, vegetables, grains, and proteins, helps their bodies grow strong and stay healthy.',
  [('Name one food group, like fruits or vegetables.', ['fruits', 'vegetables', 'grains', 'proteins']),
   ('Does eating a balance of different food groups help your body stay healthy?', ['yes']),
   ('Name one fruit or vegetable you could eat for a healthy snack.', ['an apple', 'apple', 'carrot', 'banana'])],
  [('Why is it important to eat a balance of different food groups?', ['It helps the body grow strong and stay healthy', 'It makes food taste worse', 'It has no effect on health', 'It only matters for adults'], 0),
   ('Which of these is an example of a fruit or vegetable?', ['An apple', 'A candy bar', 'A soda', 'A cookie'], 0),
   ('Which food group gives the body energy from foods like bread and rice?', ['Grains', 'Only sweets', 'Only fats', 'Only sugar'], 0),
   ('Which of these is a healthy snack choice?', ['Carrot sticks', 'A bag of candy', 'A can of soda', 'A bag of chips'], 0),
   ('Eating too much of only one food group and ignoring the others can ___.', ['Make it harder for the body to stay balanced and healthy', 'Always make you healthier', 'Have no effect at all', 'Make you grow taller instantly'], 0)])

d39_ss = sub('SocialStudies', 'Landmarks and Famous Places in Canada',
  'Students learn about well-known Canadian landmarks, such as the CN Tower, Niagara Falls, and the Parliament Buildings, and why these places are important to the country.',
  [('Name one famous Canadian landmark, like the CN Tower or Niagara Falls.', ['the CN Tower', 'CN Tower', 'Niagara Falls']),
   ('In which city is the CN Tower located?', ['Toronto']),
   ('Name one reason people visit famous landmarks, like to learn about history.', ['to learn about history', 'to see something special', 'to visit'])],
  [('Which of these is a famous Canadian landmark?', ['The CN Tower', 'The Eiffel Tower', 'The Great Wall', 'The Pyramids'], 0),
   ('In which city would you find the CN Tower?', ['Toronto', 'Vancouver', 'Montreal', 'Ottawa'], 0),
   ('Which famous Canadian landmark is a large and powerful waterfall?', ['Niagara Falls', 'The CN Tower', 'Parliament Hill', 'The Rocky Mountains'], 0),
   ('Where do Canadas government leaders meet, at a famous landmark in Ottawa?', ['The Parliament Buildings', 'The CN Tower', 'Niagara Falls', 'A shopping mall'], 0),
   ('Why are landmarks important to a country?', ['They represent history, culture, or natural beauty', 'They have no importance at all', 'They are only found in other countries', 'They are never visited'], 0)])

# ─── DAY 40 (Final Review) ──────────────────────────────────────────────────
d40_lang = sub('Language', 'Final Review: Prefixes, Suffixes, Comparing Words and Paragraphs',
  'Students review recent Language skills: prefixes un- and re-, suffixes -ful and -less, comparing with -er and -est, and writing a simple paragraph.',
  [('What does the prefix re- usually mean, as in redo?', ['again']),
   ('What does the suffix -less usually mean, as in helpless?', ['without']),
   ('What do we call the sentence that introduces the main idea of a paragraph?', ['the topic sentence', 'topic sentence'])],
  [('What does the prefix un- usually mean?', ['Not', 'Again', 'Before', 'Always'], 0),
   ('Which word means full of joy by using the suffix -ful?', ['Joyful', 'Joyless', 'Rejoy', 'Prejoy'], 0),
   ('Which suffix compares three or more things?', ['-est', '-er', '-ful', '-less'], 0),
   ('What is a topic sentence?', ['The sentence that introduces the main idea of a paragraph', 'The last sentence in a story', 'A sentence with no meaning', 'A question only'], 0),
   ('Which word means without help by using the suffix -less?', ['Helpless', 'Helpful', 'Prehelp', 'Rehelp'], 0)])

d40_math = sub('Math', 'Final Review: Fractions, Odd/Even, Patterns and Symmetry',
  'Students review recent Math skills: thirds and eighths, odd and even numbers, repeating patterns, and symmetry in shapes.',
  [('If a whole is split into 3 equal parts, what is each part called?', ['one third', 'a third']),
   ('Is the number 8 odd or even?', ['even']),
   ('What do we call the line where a symmetrical shape can be folded so both halves match?', ['a line of symmetry', 'line of symmetry'])],
  [('If a whole is split into 8 equal parts, each part is called ___.', ['One eighth', 'One third', 'One half', 'One whole'], 0),
   ('Which of these numbers is odd?', ['9', '8', '6', '4'], 0),
   ('In the pattern circle, square, circle, square, ___, what comes next?', ['Circle', 'Square', 'Triangle', 'Star'], 0),
   ('A shape has symmetry if it can be folded so that ___.', ['Both halves match exactly', 'One half disappears', 'Both halves are different sizes', 'It cannot be folded at all'], 0),
   ('Splitting a whole into more equal parts makes each part ___.', ['Smaller', 'Bigger', 'Stay the same size', 'Disappear'], 0)])

d40_sci = sub('Science', 'Final Review: Magnets, Water Cycle, Rocks/Soil and Healthy Eating',
  'Students review recent Science topics: magnets, the water cycle, rocks and soil, and healthy eating and food groups.',
  [('What do we call the force a magnet uses to attract or push away objects?', ['magnetism', 'magnetic force']),
   ('What do we call water turning into vapour and rising into the air?', ['evaporation']),
   ('What is soil made up of?', ['broken rock and decayed plants', 'tiny broken bits of rock and decayed matter'])],
  [('Which of these materials would a magnet most likely attract?', ['An iron nail', 'A wooden block', 'A plastic cup', 'A paper towel'], 0),
   ('What do we call rain or snow falling from clouds to the ground?', ['Precipitation', 'Evaporation', 'Condensation', 'Freezing'], 0),
   ('What is soil made up of?', ['Tiny broken bits of rock mixed with decayed plants and animals', 'Only water', 'Only metal', 'Only glass'], 0),
   ('Why is it important to eat a balance of different food groups?', ['It helps the body grow strong and stay healthy', 'It makes food taste worse', 'It has no effect on health', 'It only matters for adults'], 0),
   ('What happens when two magnets with opposite poles are brought close together?', ['They attract and pull together', 'They always push apart', 'They disappear', 'They melt'], 0)])

d40_ss = sub('SocialStudies', 'Final Review: Immigration, Personal Safety, Money and Landmarks',
  'Students review recent Social Studies topics: immigration, personal safety, saving and spending money wisely, and Canadian landmarks.',
  [('What do we call it when people move from one country to live in another?', ['immigration']),
   ('What should you do if a touch makes you feel unsafe or uncomfortable?', ['say no', 'tell a trusted adult']),
   ('What do we call putting money aside instead of spending it right away?', ['saving'])],
  [('What is immigration?', ['When people move from one country to live in another', 'When people travel on vacation', 'When animals migrate with the seasons', 'When a family moves within the same city'], 0),
   ('Who could be a trusted adult a child talks to about feeling unsafe?', ['A parent or teacher', 'A stranger', 'No one at all', 'Only another child'], 0),
   ('What does it mean to save money?', ['Putting money aside instead of spending it right away', 'Spending all your money right away', 'Losing your money', 'Giving all your money away'], 0),
   ('In which city would you find the CN Tower?', ['Toronto', 'Vancouver', 'Montreal', 'Ottawa'], 0),
   ('Why might a family choose to immigrate to Canada?', ['To find new opportunities, safety, or to be with family', 'Canada has no reasons to immigrate to', 'Only for a short vacation', 'To avoid all other countries'], 0)])


g2_31_40 = [
    day(31, [d31_lang, d31_math, d31_sci, d31_ss]),
    day(32, [d32_lang, d32_math, d32_sci, d32_ss]),
    day(33, [d33_lang, d33_math, d33_sci, d33_ss]),
    day(34, [d34_lang, d34_math, d34_sci, d34_ss]),
    day(35, [d35_lang, d35_math, d35_sci, d35_ss]),
    day(36, [d36_lang, d36_math, d36_sci, d36_ss]),
    day(37, [d37_lang, d37_math, d37_sci, d37_ss]),
    day(38, [d38_lang, d38_math, d38_sci, d38_ss]),
    day(39, [d39_lang, d39_math, d39_sci, d39_ss]),
    day(40, [d40_lang, d40_math, d40_sci, d40_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_31_40, seed=20260828)
    append_worksheet_days(2, g2_31_40)
