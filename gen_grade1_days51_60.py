#!/usr/bin/env python3
"""Grade 1, Days 51-60 -- THIRD batch extending Grade 1 past Day 50.
Self-contained script modeled exactly on gen_grade1_days41_50.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-50 topics (see data/grade1.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260826):
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
d51_lang = sub('Language', 'Consonant Digraphs: ph and ck',
  'Students learn that two letters can join to make one new sound called a digraph, such as ph making the f sound in phone, and ck making the k sound in duck.',
  [('What two letters make the f sound in the word phone?', ['ph']),
   ('What two letters make the k sound at the end of the word duck?', ['ck']),
   ('Name one word that has the ph digraph, like phone or dolphin.', ['phone', 'dolphin', 'elephant'])],
  [('Which word has the ph digraph making the f sound?', ['Phone', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word ends with the ck digraph?', ['Duck', 'Cat', 'Bed', 'Sun'], 0),
   ('In the word dolphin, which letters make the f sound?', ['ph', 'ck', 'sh', 'th'], 0),
   ('Which word ends with the k sound spelled ck?', ['Rock', 'Frog', 'Bird', 'Fish'], 0),
   ('A digraph is two letters that ___.', ['Work together to make one sound', 'Always make two sounds', 'Are always vowels', 'Are never used together'], 0)])

d51_math = sub('Math', 'Numbers to 120',
  'Students extend counting and number recognition beyond 100, learning to count, read, and write numbers up to 120.',
  [('What number comes right after 100?', ['101', 'one hundred one']),
   ('What number comes right after 109?', ['110', 'one hundred ten']),
   ('Count from 115 to 120. What is the last number?', ['120', 'one hundred twenty'])],
  [('What number comes right after 100?', ['99', '101', '110', '200'], 1),
   ('Which number is between 105 and 107?', ['104', '106', '108', '110'], 1),
   ('What number comes right before 120?', ['118', '119', '121', '100'], 1),
   ('Which of these numbers is greater than 100?', ['95', '99', '100', '115'], 3),
   ('Counting past 100 helps us because ___.', ['We can count and compare even larger numbers', 'Numbers stop at 100', 'We never need numbers past 100', 'All numbers past 100 are the same'], 0)])

d51_sci = sub('Science', 'Reptiles and Their Body Parts',
  'Students learn about the body parts of reptiles, such as dry scaly skin and four legs on many reptiles, and how these parts help reptiles such as turtles and lizards survive.',
  [('What covers the skin of most reptiles?', ['scales']),
   ('Name one animal that is a reptile, like a turtle or lizard.', ['turtle', 'lizard', 'snake']),
   ('Is a reptile skin usually wet or dry?', ['dry'])],
  [('What covers the skin of most reptiles?', ['Feathers', 'Scales', 'Fur', 'Fins'], 1),
   ('Which of these animals is a reptile?', ['A turtle', 'A robin', 'A frog', 'A fish'], 0),
   ('Is the skin of most reptiles usually wet or dry?', ['Wet', 'Dry', 'Sticky', 'Frozen'], 1),
   ('Which of these reptiles has no legs at all?', ['A snake', 'A turtle', 'A lizard', 'A crocodile'], 0),
   ('Why might a hard shell help a turtle?', ['It protects the turtle body from danger', 'It helps the turtle fly', 'It helps the turtle breathe underwater only', 'It has no purpose'], 0)])

d51_ss = sub('SocialStudies', 'Rural and Urban Communities: City and Country Life',
  'Students compare rural communities, quiet areas with farms and open land, to urban communities, busy cities with many buildings and people, and learn that Canada has both types.',
  [('What do we call a busy community with many tall buildings?', ['city', 'urban community', 'urban']),
   ('What do we call a quiet community with farms and open land?', ['countryside', 'rural community', 'rural']),
   ('Name one thing you might see more of in a city, like tall buildings.', ['tall buildings', 'many people', 'traffic'])],
  [('What do we call a busy community with many tall buildings and people?', ['An urban community', 'A rural community', 'An ocean', 'A desert'], 0),
   ('What do we call a quiet community with farms and open fields?', ['An urban community', 'A rural community', 'A city', 'A mountain'], 1),
   ('Which of these is more likely found in a rural community?', ['A large farm field', 'A tall office tower', 'A subway train', 'A crowded sidewalk'], 0),
   ('Which of these is more likely found in an urban community?', ['Many tall buildings close together', 'A single farmhouse', 'An empty field', 'A quiet forest trail'], 0),
   ('Canada has ___ communities.', ['Both rural and urban', 'Only rural', 'Only urban', 'No'], 0)])

# ─── DAY 52 ─────────────────────────────────────────────────────────────────
d52_lang = sub('Language', 'Silent Letters: kn and wr',
  'Students learn that some words have silent letters, letters that are not pronounced, such as the silent k in knee and the silent w in write.',
  [('In the word knee, which letter is silent?', ['k']),
   ('In the word write, which letter is silent?', ['w']),
   ('Name one word that begins with a silent k, like knee or knife.', ['knee', 'knife', 'know'])],
  [('In the word knee, which letter makes no sound?', ['k', 'n', 'e', 'all letters are heard'], 0),
   ('In the word write, which letter makes no sound?', ['w', 'r', 'i', 't'], 0),
   ('Which word begins with a silent letter?', ['Knife', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word begins with a silent w?', ['Wrist', 'Cat', 'Bed', 'Sun'], 0),
   ('A silent letter is a letter that ___.', ['Is written but not pronounced', 'Is always pronounced loudly', 'Never appears in words', 'Makes a new sound every time'], 0)])

d52_math = sub('Math', 'Skip Counting by 4s',
  'Students practise skip counting by 4s, saying the numbers 4, 8, 12, 16, and so on, to build number sense and prepare for multiplication.',
  [('What number comes after 4 when skip counting by 4s?', ['8', 'eight']),
   ('What number comes after 12 when skip counting by 4s?', ['16', 'sixteen']),
   ('Start at 4 and skip count by 4s three times. What is the third number?', ['12', 'twelve'])],
  [('When skip counting by 4s, what number comes after 8?', ['9', '10', '11', '12'], 3),
   ('When skip counting by 4s, what number comes after 16?', ['17', '18', '19', '20'], 3),
   ('Which of these lists shows skip counting by 4s?', ['4, 8, 12, 16', '4, 6, 8, 10', '4, 7, 10, 13', '3, 6, 9, 12'], 0),
   ('When skip counting by 4s, what number comes after 20?', ['21', '22', '23', '24'], 3),
   ('Skip counting by 4s means we count ___.', ['Every fourth number', 'Every second number', 'Backward only', 'Only odd numbers'], 0)])

d52_sci = sub('Science', 'Amphibians and Their Life Cycle',
  'Students learn that amphibians, such as frogs, begin life in water as eggs and tadpoles, then change into adults that can live both in water and on land.',
  [('Name one animal that is an amphibian, like a frog.', ['frog', 'toad', 'salamander']),
   ('What is a baby frog called before it grows legs?', ['tadpole']),
   ('Can adult frogs live both in water and on land?', ['yes'])],
  [('Which of these animals is an amphibian?', ['A frog', 'A robin', 'A turtle', 'A shark'], 0),
   ('What is a young frog called before it grows legs?', ['A tadpole', 'A calf', 'A cub', 'A chick'], 0),
   ('Where do frog eggs usually hatch?', ['In water', 'In a nest in a tree', 'Underground', 'In the sky'], 0),
   ('As a tadpole grows into a frog, what happens to its body?', ['It grows legs and can breathe air', 'It grows feathers', 'It grows fur', 'It stays exactly the same'], 0),
   ('Where can most adult frogs live?', ['Both in water and on land', 'Only deep in the ocean', 'Only in the sky', 'Only underground'], 0)])

d52_ss = sub('SocialStudies', 'Canadian Inventions and Inventors',
  'Students learn about a few simple inventions created by people in Canada, such as basketball, and that inventors are people who create new and useful things.',
  [('What do we call a person who creates a new and useful thing?', ['inventor']),
   ('What sport was invented by a Canadian named James Naismith?', ['basketball']),
   ('Do inventions help solve problems or make life easier?', ['yes'])],
  [('What do we call a person who creates something new and useful?', ['An inventor', 'A farmer', 'A pilot', 'A dentist'], 0),
   ('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Cricket', 'Tennis'], 0),
   ('Why are inventions helpful to people?', ['They can solve problems or make life easier', 'Inventions never help anyone', 'They only cause problems', 'They have no purpose'], 0),
   ('Which of these best describes an invention?', ['A new and useful thing that someone creates', 'A mountain', 'A cloud', 'A river'], 0),
   ('Canadians have created inventions in fields such as ___.', ['Sports and technology', 'Nothing at all', 'Only cooking', 'Only music'], 0)])

# ─── DAY 53 ─────────────────────────────────────────────────────────────────
d53_lang = sub('Language', 'Word Families: -op and -og',
  'Students learn word families -op and -og, groups of words that share the same ending sound and spelling pattern, such as hop and top, or dog and log.',
  [('Name one word in the -op word family, like hop or top.', ['hop', 'top', 'mop', 'pop']),
   ('Name one word in the -og word family, like dog or log.', ['dog', 'log', 'fog', 'jog']),
   ('What ending sound do the words hop and top share?', ['op'])],
  [('Which word belongs to the -op word family?', ['Hop', 'Cat', 'Sun', 'Bed'], 0),
   ('Which word belongs to the -og word family?', ['Dog', 'Cat', 'Sun', 'Bed'], 0),
   ('Which word rhymes with top?', ['Hop', 'Cat', 'Sun', 'Bed'], 0),
   ('Which word rhymes with log?', ['Fog', 'Cat', 'Sun', 'Bed'], 0),
   ('A word family is a group of words that share the same ___.', ['Ending sound and spelling pattern', 'Beginning letter only', 'Meaning', 'Number of letters'], 0)])

d53_math = sub('Math', 'Fractions: Thirds',
  'Students learn that a whole can be split into three equal parts called thirds, and that each part is called one third of the whole.',
  [('If a pizza is cut into three equal parts, what is each part called?', ['a third', 'one third']),
   ('How many equal parts make up a whole cut into thirds?', ['3', 'three']),
   ('If you eat one of three equal parts of a sandwich, how much did you eat?', ['one third', 'a third'])],
  [('If a shape is split into three equal parts, each part is called ___.', ['A half', 'A third', 'A quarter', 'A whole'], 1),
   ('How many equal parts make up thirds?', ['2', '3', '4', '5'], 1),
   ('Which picture would show thirds?', ['A circle split into 3 equal parts', 'A circle split into 2 equal parts', 'A circle with no parts', 'A square split into 5 parts'], 0),
   ('If you have 3 equal slices of an apple, each slice is ___ of the apple.', ['One third', 'One half', 'One quarter', 'The whole'], 0),
   ('For a fraction to be a true third, the parts must be ___.', ['Equal in size', 'Different sizes', 'Different colours', 'Different shapes'], 0)])

d53_sci = sub('Science', 'Mammals and Their Body Parts',
  'Students learn about the body parts of mammals, such as fur covering their skin and the way most mammal babies drink milk from their mother, and how these features help mammals survive.',
  [('What usually covers the skin of a mammal?', ['fur']),
   ('Name one animal that is a mammal, like a dog or a cat.', ['dog', 'cat', 'cow', 'human']),
   ('How do most baby mammals get food from their mother at first?', ['drink milk', 'milk'])],
  [('What usually covers the skin of a mammal?', ['Fur', 'Scales', 'Feathers', 'Fins'], 0),
   ('Which of these animals is a mammal?', ['A dog', 'A snake', 'A fish', 'A frog'], 0),
   ('How do most baby mammals get their food at first?', ['They drink milk from their mother', 'They make their own food', 'They eat only rocks', 'They do not eat'], 0),
   ('Which of these is true about most mammals?', ['They breathe air using lungs', 'They breathe only underwater using gills', 'They have no bones', 'They are always cold to the touch'], 0),
   ('Which of these animals is not a mammal?', ['A fish', 'A dog', 'A cat', 'A cow'], 0)])

d53_ss = sub('SocialStudies', 'Visiting the Library: Borrowing and Sharing Books',
  'Students learn that a library is a community place where people can borrow books and other materials for free, and that a library card and returning books on time help everyone share.',
  [('What is a community place where people can borrow books for free?', ['library', 'the library']),
   ('What card do you need to borrow books from a library?', ['a library card', 'library card']),
   ('Why should borrowed books be returned on time?', ['so others can borrow them', 'to share with others'])],
  [('What is a library?', ['A place where people can borrow books for free', 'A place that sells only toys', 'A place with no books', 'A place to buy food'], 0),
   ('What do you usually need to borrow books from a library?', ['A library card', 'A hammer', 'A map', 'A ticket'], 0),
   ('Why is it important to return library books on time?', ['So other people can also borrow them', 'Books do not need to be returned', 'Returning books is not important', 'Only librarians can read books'], 0),
   ('Who helps people find books at a library?', ['A librarian', 'A farmer', 'A firefighter', 'A pilot'], 0),
   ('Sharing library books with the whole community is an example of ___.', ['Being a good citizen', 'Being unkind', 'Ignoring others', 'Wasting resources'], 0)])

# ─── DAY 54 ─────────────────────────────────────────────────────────────────
d54_lang = sub('Language', 'Vowel Teams: ee and ea',
  'Students learn that the letters ee and ea can work together as a vowel team to make the long e sound, as in tree and leaf.',
  [('What two letters make the long e sound in the word tree?', ['ee']),
   ('What two letters make the long e sound in the word leaf?', ['ea']),
   ('Name one word that has the ee vowel team, like tree or bee.', ['tree', 'bee', 'see', 'feet'])],
  [('Which letters make the long e sound in the word tree?', ['ee', 'ea', 'ai', 'oa'], 0),
   ('Which letters make the long e sound in the word leaf?', ['ee', 'ea', 'ay', 'oo'], 1),
   ('Which word has the ee vowel team?', ['Bee', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ea vowel team?', ['Leaf', 'Cat', 'Dog', 'Sun'], 0),
   ('The ee and ea vowel teams both usually make the ___ sound.', ['Long e', 'Short a', 'Long o', 'Short i'], 0)])

d54_math = sub('Math', 'Adding and Subtracting Tens',
  'Students learn to add and subtract multiples of ten, such as 30 add 20, by thinking about groups of ten instead of counting one at a time.',
  [('What is 30 add 20?', ['50', 'fifty']),
   ('What is 60 minus 20?', ['40', 'forty']),
   ('What is 10 add 40?', ['50', 'fifty'])],
  [('What is 20 add 30?', ['40', '50', '60', '70'], 1),
   ('What is 70 minus 30?', ['30', '40', '50', '60'], 1),
   ('What is 10 add 10 add 10?', ['20', '30', '40', '50'], 1),
   ('What is 90 minus 40?', ['40', '50', '60', '70'], 1),
   ('When adding tens, such as 40 add 30, it helps to think about ___.', ['Groups of ten', 'Groups of one hundred', 'Only single digits', 'Only shapes'], 0)])

d54_sci = sub('Science', 'The Water Cycle',
  'Students learn about the water cycle, the way water moves from Earth into the sky as it evaporates, forms clouds, and falls back down again as rain or snow.',
  [('What do we call water rising into the air and turning into vapour?', ['evaporation']),
   ('What falls from clouds back down to Earth, like rain or snow?', ['rain', 'snow', 'precipitation']),
   ('What forms in the sky when water vapour cools and gathers together?', ['clouds', 'a cloud'])],
  [('What do we call water turning into vapour and rising into the air?', ['Evaporation', 'Freezing', 'Sinking', 'Camouflage'], 0),
   ('What forms in the sky when water vapour cools and gathers together?', ['Clouds', 'Rocks', 'Soil', 'Sand'], 0),
   ('Which of these falls from clouds back down to Earth?', ['Rain', 'Sunlight', 'Wind only', 'Soil'], 0),
   ('Put these water cycle steps in order: water evaporates, clouds form, rain falls.', ['Evaporate then clouds then rain', 'Rain then clouds then evaporate', 'Clouds then rain then evaporate', 'All happen at the same time'], 0),
   ('The water cycle describes how water ___.', ['Moves between Earth and the sky again and again', 'Disappears forever', 'Never moves at all', 'Only exists in oceans'], 0)])

d54_ss = sub('SocialStudies', 'How Mail Gets Delivered: Post Office Helpers',
  'Students learn that letters and packages travel through a post office and are delivered by mail carriers, who sort and bring mail to homes and businesses.',
  [('What do we call the person who delivers mail to homes?', ['mail carrier', 'mail person', 'postal worker']),
   ('Name one place mail might travel through before reaching your home, like a post office.', ['post office', 'a mail truck']),
   ('Name one thing that can be delivered by mail, like a letter or a package.', ['a letter', 'a package', 'letters', 'packages'])],
  [('What do we call a person whose job is to deliver mail?', ['A mail carrier', 'A farmer', 'A dentist', 'A pilot'], 0),
   ('What building sorts letters and packages before they are delivered?', ['A post office', 'A library', 'A hospital', 'A school'], 0),
   ('Which of these is something that can be sent through the mail?', ['A letter', 'A mountain', 'A river', 'The sky'], 0),
   ('Why is a mail carrier an important community helper?', ['They help letters and packages reach the right homes', 'They grow food for the community', 'They put out fires', 'They teach students'], 0),
   ('Before mail trucks, how might people have sent letters long ago?', ['By horse and rider or by ship', 'By video call', 'By the internet', 'By airplane text message'], 0)])

# ─── DAY 55 ─────────────────────────────────────────────────────────────────
d55_lang = sub('Language', 'R-Controlled Vowels: ar and or',
  'Students learn that when a vowel is followed by the letter r, its sound changes, such as ar in car and or in corn, forming an r-controlled vowel sound.',
  [('What two letters make the sound in the word car?', ['ar']),
   ('What two letters make the sound in the word corn?', ['or']),
   ('Name one word that has the ar sound, like car or star.', ['car', 'star', 'farm', 'park'])],
  [('Which letters make the sound in the word car?', ['ar', 'or', 'ai', 'ee'], 0),
   ('Which letters make the sound in the word corn?', ['ar', 'or', 'ay', 'oo'], 1),
   ('Which word has the ar sound?', ['Star', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the or sound?', ['Fork', 'Cat', 'Dog', 'Sun'], 0),
   ('An r-controlled vowel happens when a vowel is followed by the letter ___.', ['r', 's', 't', 'm'], 0)])

d55_math = sub('Math', 'Comparing Numbers on a Number Line',
  'Students use a number line, a line marked with numbers in order, to compare numbers and see which number is greater or less than another.',
  [('On a number line, is the number 8 to the left or right of the number 5?', ['right']),
   ('On a number line, which number is farther to the left, 3 or 9?', ['3', 'three']),
   ('On a number line, numbers get larger as you move in which direction?', ['right', 'to the right'])],
  [('On a number line, numbers get larger as you move ___.', ['To the right', 'To the left', 'Upward only', 'Downward only'], 0),
   ('On a number line, which number is farther to the left, 4 or 10?', ['4', '10', 'They are the same', 'Cannot tell'], 0),
   ('If 6 is to the left of 9 on a number line, which number is greater?', ['6', '9', 'They are equal', 'Cannot tell'], 1),
   ('A number line helps us compare numbers by showing ___.', ['Their order and position', 'Their colour', 'Their shape', 'Their weight'], 0),
   ('On a number line from 0 to 20, which number would be closest to 0?', ['1', '15', '19', '20'], 0)])

d55_sci = sub('Science', 'Day and Night',
  'Students learn that Earth slowly spinning causes day and night, with daytime happening when a place faces the sun and nighttime happening when it faces away from the sun.',
  [('What do we see in the sky mostly during the day?', ['the sun', 'sun']),
   ('What do we often see in the sky at night?', ['the moon', 'moon', 'stars']),
   ('Does the Earth slowly spin to cause day and night?', ['yes'])],
  [('What causes day and night on Earth?', ['Earth slowly spinning around', 'Earth changing colour', 'The sun moving very fast', 'The moon disappearing'], 0),
   ('During the day, a place on Earth is usually facing ___.', ['Toward the sun', 'Away from the sun', 'Toward the moon only', 'Nowhere at all'], 0),
   ('During the night, a place on Earth is usually facing ___.', ['Toward the sun', 'Away from the sun', 'Toward a rainbow', 'Nowhere at all'], 1),
   ('Which of these do we often see in the night sky?', ['The moon and stars', 'Only rainbows', 'Only clouds', 'Only the sun'], 0),
   ('About how long does it take for Earth to spin around once, giving us one day and one night?', ['About one hour', 'About one day', 'About one week', 'About one year'], 1)])

d55_ss = sub('SocialStudies', 'National Parks: Protecting Nature in Canada',
  'Students learn that national parks are special protected areas of land in Canada set aside to keep nature, plants, and animals safe for everyone to enjoy.',
  [('What do we call a protected area of land set aside to keep nature safe?', ['a national park', 'national park']),
   ('Name one thing a national park helps protect, like plants or animals.', ['plants', 'animals', 'nature', 'wildlife']),
   ('Should visitors to a national park take care not to harm nature?', ['yes'])],
  [('What is a national park?', ['A protected area of land set aside to keep nature safe', 'A tall office building', 'A shopping mall', 'A parking lot'], 0),
   ('Why does Canada have national parks?', ['To protect plants, animals, and natural land', 'To build more houses', 'To sell more toys', 'National parks have no purpose'], 0),
   ('Which of these might you find in a national park?', ['Wild animals and forests', 'Video game arcades', 'Grocery stores', 'Office buildings'], 0),
   ('How should visitors treat a national park?', ['With care, so nature stays protected', 'By littering everywhere', 'By picking all the flowers', 'By ignoring the rules'], 0),
   ('National parks help make sure that nature is enjoyed by ___.', ['Everyone, now and in the future', 'Only a few people', 'No one', 'Only animals'], 0)])

# ─── DAY 56 ─────────────────────────────────────────────────────────────────
d56_lang = sub('Language', 'Homophones: to, too, and two',
  'Students learn about homophones, words that sound the same but have different spellings and meanings, such as to, too, and two.',
  [('Which word means the number 2?', ['two']),
   ('Which word means also, or more than enough?', ['too']),
   ('Which word is used to show direction, like going to the park?', ['to'])],
  [('Which word means the number 2?', ['To', 'Too', 'Two', 'Threw'], 2),
   ('Which word means also or as well?', ['To', 'Too', 'Two', 'Ate'], 1),
   ('Which word would complete the sentence: I am going ___ the park?', ['To', 'Too', 'Two', 'Ate'], 0),
   ('Which word would complete the sentence: I want ___ apples?', ['To', 'Too', 'Two', 'Ate'], 2),
   ('Homophones are words that ___.', ['Sound the same but have different spellings and meanings', 'Are always spelled the same', 'Never sound alike', 'Are always the same word'], 0)])

d56_math = sub('Math', 'Data: Bar Graphs',
  'Students learn to read and create simple bar graphs, charts that use bars of different heights to show and compare amounts of data.',
  [('On a bar graph, does a taller bar show more or fewer items?', ['more']),
   ('What do we call a chart that uses bars of different heights to compare amounts?', ['a bar graph', 'bar graph']),
   ('If a bar graph shows 3 red bars and 5 blue bars, which colour has more?', ['blue'])],
  [('What does a bar graph use to show data?', ['Bars of different heights', 'Only numbers', 'Only words', 'Only colours'], 0),
   ('On a bar graph, a taller bar usually shows ___.', ['A larger amount', 'A smaller amount', 'No amount at all', 'The same amount always'], 0),
   ('If a bar graph shows 4 bars for apples and 2 bars for bananas, which fruit has more?', ['Apples', 'Bananas', 'They are equal', 'Cannot tell'], 0),
   ('Why are bar graphs useful?', ['They help us compare amounts easily', 'They are never useful', 'They only show colours', 'They hide information'], 0),
   ('What do we call the information shown on a bar graph?', ['Data', 'Weather', 'Feelings', 'Sounds'], 0)])

d56_sci = sub('Science', 'Forces: Gravity Pulls Things Down',
  'Students learn that gravity is a force that pulls objects down toward the ground, which is why a dropped ball falls instead of floating away.',
  [('What is the name of the force that pulls objects down toward the ground?', ['gravity']),
   ('If you drop a ball, does gravity pull it up or down?', ['down']),
   ('Name one object that gravity pulls down when you drop it, like a ball or a book.', ['a ball', 'a book', 'a toy'])],
  [('What is the name of the force that pulls objects down toward the ground?', ['Gravity', 'Magnetism', 'Sound', 'Light'], 0),
   ('If you drop an apple, what happens because of gravity?', ['It falls down to the ground', 'It floats up into the sky', 'It disappears', 'It turns into water'], 0),
   ('Which of these shows gravity at work?', ['A ball rolling down a hill', 'A ball floating in the air on its own', 'A ball turning into a cloud', 'A ball changing colour'], 0),
   ('Without gravity, objects on Earth would likely ___.', ['Float away instead of staying on the ground', 'Become heavier', 'Turn into rocks', 'Disappear completely'], 0),
   ('Gravity is an example of a ___.', ['Force', 'Colour', 'Sound', 'Season'], 0)])

d56_ss = sub('SocialStudies', 'Community Activities Through the Seasons',
  'Students learn that communities offer different activities depending on the season, such as skating in winter and swimming in summer, and that people plan events around the weather.',
  [('Name one activity people might do in a community during winter, like skating.', ['skating', 'sledding', 'playing in the snow']),
   ('Name one activity people might do in a community during summer, like swimming.', ['swimming', 'playing outside', 'having a picnic']),
   ('Do communities plan different activities depending on the season?', ['yes'])],
  [('Which activity would a community more likely plan for winter?', ['Skating on an outdoor rink', 'Swimming at an outdoor pool', 'A beach picnic', 'Planting a garden'], 0),
   ('Which activity would a community more likely plan for summer?', ['A snowman building contest', 'A splash pad or pool day', 'Ice skating', 'Sledding'], 1),
   ('Why do communities plan different activities for different seasons?', ['Weather changes what activities are safe and fun', 'The season never changes anything', 'Activities are always the same all year', 'Communities do not plan activities'], 0),
   ('Which season might a community host an outdoor harvest festival?', ['Fall', 'Only winter', 'Only summer', 'No season'], 0),
   ('Planning community events around the seasons helps people ___.', ['Enjoy activities that fit the weather', 'Ignore the weather completely', 'Stay indoors all year', 'Avoid all activities'], 0)])

# ─── DAY 57 ─────────────────────────────────────────────────────────────────
d57_lang = sub('Language', 'Types of Sentences: Statements and Commands',
  'Students learn that a statement is a sentence that tells something and usually ends with a period, while a command tells someone to do something, such as Close the door.',
  [('What kind of sentence tells something, like The sky is blue?', ['a statement', 'statement']),
   ('What kind of sentence tells someone to do something, like Close the door?', ['a command', 'command']),
   ('What punctuation mark usually ends a statement?', ['a period', 'period'])],
  [('Which sentence is a statement?', ['The sky is blue.', 'Close the door.', 'Please sit down.', 'Pick it up.'], 0),
   ('Which sentence is a command?', ['The sky is blue.', 'Close the door.', 'The dog is brown.', 'I like apples.'], 1),
   ('A statement is a sentence that ___.', ['Tells something', 'Always asks a question', 'Always shouts', 'Never ends with a period'], 0),
   ('A command is a sentence that ___.', ['Tells someone to do something', 'Only tells a fact', 'Always ends with a question mark', 'Is never useful'], 0),
   ('Which punctuation mark usually ends a statement?', ['A period', 'A question mark only', 'No punctuation', 'A comma only'], 0)])

d57_math = sub('Math', 'Repeating Patterns: AB and ABC',
  'Students learn to recognize and continue repeating patterns, such as an AB pattern like red, blue, red, blue, or an ABC pattern like circle, square, triangle, circle, square, triangle.',
  [('In the pattern red, blue, red, blue, what colour comes next?', ['red']),
   ('In the pattern circle, square, triangle, circle, square, triangle, what shape comes next?', ['circle']),
   ('What do we call a pattern that repeats two items over and over, like red, blue, red, blue?', ['an AB pattern', 'AB pattern'])],
  [('In the pattern red, blue, red, blue, red, what comes next?', ['Red', 'Blue', 'Green', 'Yellow'], 1),
   ('In the pattern circle, square, triangle, circle, square, what comes next?', ['Circle', 'Square', 'Triangle', 'Star'], 2),
   ('What do we call a pattern that repeats two items, like clap, stomp, clap, stomp?', ['An AB pattern', 'An ABC pattern', 'No pattern', 'A number pattern'], 0),
   ('What do we call a pattern that repeats three items, like red, yellow, blue, red, yellow, blue?', ['An AB pattern', 'An ABC pattern', 'No pattern', 'A shape only'], 1),
   ('To continue a repeating pattern, we should ___.', ['Look at what repeats and keep the order going', 'Guess randomly', 'Always pick the same item', 'Change the pattern completely'], 0)])

d57_sci = sub('Science', 'Life Cycle of a Butterfly',
  'Students learn the life cycle of a butterfly, which changes from an egg to a caterpillar, then to a chrysalis, and finally into an adult butterfly.',
  [('What is the crawling stage of a butterfly life cycle called?', ['caterpillar']),
   ('What do we call the stage when a caterpillar rests inside a hard case before becoming a butterfly?', ['chrysalis', 'pupa']),
   ('What is the first stage of a butterfly life cycle?', ['egg'])],
  [('What is the first stage of a butterfly life cycle?', ['Egg', 'Caterpillar', 'Chrysalis', 'Adult butterfly'], 0),
   ('What do we call the crawling stage that hatches from a butterfly egg?', ['A caterpillar', 'A tadpole', 'A cub', 'A chick'], 0),
   ('What do we call the resting stage inside a hard case before a caterpillar becomes a butterfly?', ['A chrysalis', 'A nest', 'A den', 'A shell only'], 0),
   ('What is the last stage of the butterfly life cycle?', ['Adult butterfly', 'Egg', 'Caterpillar', 'Chrysalis'], 0),
   ('Put these butterfly life cycle stages in the correct order.', ['Egg, caterpillar, chrysalis, butterfly', 'Butterfly, egg, caterpillar, chrysalis', 'Chrysalis, egg, butterfly, caterpillar', 'Caterpillar, butterfly, egg, chrysalis'], 0)])

d57_ss = sub('SocialStudies', 'Making Fair Choices in a Group',
  'Students learn simple ways a group can make fair choices together, such as taking turns, listening to every idea, and choosing an option that works well for everyone.',
  [('Name one way a group can make a fair choice, like taking turns.', ['taking turns', 'listening to ideas', 'sharing']),
   ('Why is it important to listen to everyone ideas in a group?', ['so everyone feels heard', 'to be fair']),
   ('Is it fair for one person to always choose without asking others?', ['no'])],
  [('Which of these is a fair way for a group to make a choice?', ['Taking turns and listening to everyone', 'Only one person deciding every time', 'Ignoring what others want', 'Arguing without listening'], 0),
   ('Why is it helpful to listen to every idea in a group?', ['It helps everyone feel heard and included', 'Listening wastes time', 'Ideas from others do not matter', 'Only the loudest idea should count'], 0),
   ('If two friends want different games, what is a fair solution?', ['Take turns playing each game', 'Only one friend ever gets to choose', 'Refuse to play any game', 'Argue until someone gives up'], 0),
   ('Making fair choices in a group helps everyone feel ___.', ['Included and respected', 'Left out', 'Ignored', 'Unimportant'], 0),
   ('Which of these shows a group working together fairly?', ['Everyone gets a chance to share their idea', 'Only the leader ever speaks', 'No one is allowed to share ideas', 'Ideas are chosen without listening'], 0)])

# ─── DAY 58 ─────────────────────────────────────────────────────────────────
d58_lang = sub('Language', 'Making Inferences While Reading',
  'Students learn to make inferences, using clues from a story along with what they already know, to figure out something the author does not say directly.',
  [('What do we call using story clues and what we already know to figure something out?', ['an inference', 'inference', 'making an inference']),
   ('If a character in a story is shivering and wearing a coat, what might you infer about the weather?', ['it is cold', 'cold']),
   ('Do good readers use clues from the story to make inferences?', ['yes'])],
  [('What is an inference?', ['Using clues and what we already know to figure something out', 'A made-up word', 'A type of punctuation', 'A kind of picture'], 0),
   ('If a character is holding an umbrella and wearing boots, what might you infer?', ['It is raining', 'It is sunny and hot', 'It is nighttime', 'It is snowing indoors'], 0),
   ('If a story says a dog is wagging its tail and barking happily, what might you infer about the dog feelings?', ['The dog is happy', 'The dog is sad', 'The dog is asleep', 'The dog is scared'], 0),
   ('Making inferences while reading helps readers ___.', ['Understand more about the story than what is written', 'Ignore the story completely', 'Skip important details', 'Read more slowly with no benefit'], 0),
   ('Which clue would help you infer that a character is tired?', ['The character is yawning and rubbing their eyes', 'The character is laughing loudly', 'The character is running fast', 'The character is eating lunch'], 0)])

d58_math = sub('Math', 'Estimating: More, Fewer, and About How Many',
  'Students practise estimating, making a sensible guess about how many objects there are without counting each one exactly.',
  [('What do we call making a sensible guess about how many objects there are?', ['an estimate', 'estimating', 'a guess']),
   ('If a jar clearly has more items than another jar, does it have more or fewer?', ['more']),
   ('Is an estimate always the exact count?', ['no'])],
  [('What does it mean to estimate?', ['Make a sensible guess without counting exactly', 'Count every single item slowly', 'Measure with a ruler', 'Draw a picture'], 0),
   ('If one jar looks like it has many more candies than another jar, the first jar likely has ___ candies.', ['More', 'Fewer', 'The exact same amount', 'Zero'], 0),
   ('Estimating is a useful skill because it helps us ___.', ['Make quick, sensible guesses about amounts', 'Always get the exact count', 'Avoid thinking about numbers', 'Replace counting completely'], 0),
   ('About how many apples might fit in a small basket that looks about half full of a dozen apples?', ['About 6', 'Exactly 1000', 'Exactly 0', 'About 500'], 0),
   ('Which of these is an example of estimating?', ['Guessing about how many beans are in a jar', 'Counting each bean one by one out loud', 'Measuring the jar with a ruler', 'Weighing the jar on a scale'], 0)])

d58_sci = sub('Science', 'Animal Coverings: Fur, Feathers, and Scales',
  'Students compare different animal body coverings, such as fur on mammals, feathers on birds, and scales on fish and reptiles, and how each covering helps the animal.',
  [('What body covering do most mammals have?', ['fur']),
   ('What body covering do most birds have?', ['feathers']),
   ('What body covering do fish and reptiles usually have?', ['scales'])],
  [('Which animal covering helps keep many mammals warm?', ['Fur', 'Feathers', 'Scales', 'Shells'], 0),
   ('Which body covering helps many birds fly and stay warm?', ['Fur', 'Feathers', 'Scales', 'Fins'], 1),
   ('Which body covering do fish usually have that helps protect their skin?', ['Fur', 'Feathers', 'Scales', 'Leaves'], 2),
   ('Which of these animals is covered in feathers?', ['A robin', 'A dog', 'A snake', 'A fish'], 0),
   ('Comparing animal coverings helps scientists ___.', ['Group animals and understand how their bodies help them survive', 'Change the weather', 'Grow plants faster', 'Build machines'], 0)])

d58_ss = sub('SocialStudies', 'Museums: Learning About the Past',
  'Students learn that a museum is a community place where people can see and learn about objects from the past, such as old tools, artwork, and artifacts.',
  [('What is a community place where people can see and learn about objects from the past?', ['a museum', 'museum']),
   ('Name one type of object you might see at a museum, like old tools or artwork.', ['old tools', 'artwork', 'artifacts']),
   ('Do museums help us learn about the past?', ['yes'])],
  [('What is a museum?', ['A place where people can see and learn about objects from the past', 'A place to buy groceries', 'A place to mail letters', 'A place to swim'], 0),
   ('Which of these might you see displayed at a museum?', ['Old tools and artwork', 'Fresh vegetables for sale', 'Mail being sorted', 'Swimming pools'], 0),
   ('Why do people visit museums?', ['To learn about history and the past', 'To buy new clothes', 'To mail packages', 'To play sports'], 0),
   ('What do we call an old object kept and shown at a museum because it teaches us about the past?', ['An artifact', 'A recipe', 'A weather report', 'A shopping list'], 0),
   ('Museums help communities by ___.', ['Helping people learn about history together', 'Selling food to families', 'Delivering mail to homes', 'Building new roads'], 0)])

# ─── DAY 59 ─────────────────────────────────────────────────────────────────
d59_lang = sub('Language', 'Sorting Words into Categories',
  'Students practise sorting words into categories, groups that share something in common, such as sorting animal words separately from food words.',
  [('Name one word that would belong in the category of animals, like dog or cat.', ['dog', 'cat', 'bird', 'fish']),
   ('Name one word that would belong in the category of foods, like apple or bread.', ['apple', 'bread', 'milk']),
   ('What do we call a group of words that share something in common?', ['a category', 'category'])],
  [('Which word belongs in the category of animals?', ['Dog', 'Apple', 'Chair', 'Bread'], 0),
   ('Which word belongs in the category of foods?', ['Bread', 'Dog', 'Chair', 'Cat'], 0),
   ('Which word does not belong with the others: apple, banana, grape, dog?', ['Apple', 'Banana', 'Grape', 'Dog'], 3),
   ('Which word does not belong with the others: cat, dog, bird, chair?', ['Cat', 'Dog', 'Bird', 'Chair'], 3),
   ('Sorting words into categories helps us ___.', ['See how words are related to each other', 'Forget what words mean', 'Make words longer', 'Remove vowels from words'], 0)])

d59_math = sub('Math', 'Digital Time: Reading Digital Clocks',
  'Students learn to read a digital clock, which shows the hour and minutes using numbers, such as 3:00 for three o clock.',
  [('On a digital clock showing 3:00, what hour is it?', ['3', 'three']),
   ('On a digital clock, which number comes first, the hour or the minutes?', ['the hour', 'hour']),
   ('If a digital clock shows 7:00, is it seven o clock?', ['yes'])],
  [('On a digital clock, which numbers come first?', ['The hour', 'The minutes', 'The seconds', 'The day'], 0),
   ('What time does a digital clock showing 5:00 tell us?', ['Five o clock', 'Five minutes past', 'Fifty o clock', 'Fifteen o clock'], 0),
   ('On a digital clock, the numbers after the colon show the ___.', ['Minutes', 'Hour', 'Day', 'Month'], 0),
   ('If a digital clock shows 9:00, what time is it?', ['Nine o clock', 'Nineteen o clock', 'Ninety o clock', 'Nine minutes'], 0),
   ('Which of these is different from a digital clock?', ['A clock with two moving hands and numbers around it', 'A clock showing 4:00', 'A clock showing 8:00', 'A clock showing 12:00'], 0)])

d59_sci = sub('Science', 'Ocean Animals: Creatures of the Sea',
  'Students learn about animals that live in the ocean, such as fish, whales, and octopuses, and how the deep salty water of the ocean is their home.',
  [('Name one animal that lives in the ocean, like a fish or a whale.', ['fish', 'whale', 'octopus', 'shark']),
   ('Is ocean water salty or fresh?', ['salty']),
   ('Do whales live in the ocean?', ['yes'])],
  [('Which of these animals lives in the ocean?', ['A whale', 'A robin', 'A rabbit', 'A cow'], 0),
   ('Is ocean water salty or fresh?', ['Salty', 'Fresh', 'Frozen always', 'Colourless only'], 0),
   ('Which of these ocean animals has eight arms?', ['An octopus', 'A whale', 'A shark', 'A crab'], 0),
   ('Why are oceans important homes for many animals?', ['They provide food, water, and space for ocean creatures to live', 'Oceans have no animals living in them', 'Oceans are always frozen', 'Oceans have no water'], 0),
   ('Which of these is the largest ocean animal mentioned, known for its huge size?', ['A whale', 'A crab', 'A starfish', 'A shrimp'], 0)])

d59_ss = sub('SocialStudies', 'Grocery Stores and Where We Buy Our Food',
  'Students learn that grocery stores are community places where people buy food grown on farms or made in factories, and that workers stock shelves and help customers.',
  [('What is a community place where people go to buy food?', ['a grocery store', 'grocery store']),
   ('Name one job a worker might do at a grocery store, like stocking shelves.', ['stocking shelves', 'helping customers', 'cashier']),
   ('Does food at a grocery store often come from farms?', ['yes'])],
  [('What is a grocery store?', ['A place where people buy food', 'A place to mail letters', 'A place to borrow books', 'A place to see art'], 0),
   ('Which of these might a grocery store worker do?', ['Stock shelves with food', 'Deliver mail', 'Put out fires', 'Teach a class'], 0),
   ('Where does much of the food sold at a grocery store come from?', ['Farms and factories', 'Outer space', 'The library', 'The post office'], 0),
   ('Why are grocery stores important to a community?', ['They give people a place to buy the food they need', 'They have no purpose', 'They only sell toys', 'They only sell furniture'], 0),
   ('Which of these is something you would likely buy at a grocery store?', ['Bread and vegetables', 'A library book', 'A stamp for mail', 'A museum ticket'], 0)])

# ─── DAY 60 (Review) ────────────────────────────────────────────────────────
d60_lang = sub('Language', 'Language Review: Digraphs, Vowel Teams, and Sentence Types',
  'Students review recent Language skills: consonant and silent-letter digraphs, word families, vowel teams, r-controlled vowels, homophones, sentence types, inferences, and sorting words into categories.',
  [('What two letters make the f sound in the word phone?', ['ph']),
   ('What two letters make the long e sound in the word tree?', ['ee']),
   ('What kind of sentence tells something, like The sky is blue?', ['a statement', 'statement'])],
  [('Which word has the ph digraph making the f sound?', ['Phone', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ee vowel team?', ['Bee', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ar sound?', ['Star', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word means the number 2?', ['To', 'Too', 'Two', 'Threw'], 2),
   ('Which sentence is a command?', ['The sky is blue.', 'Close the door.', 'The dog is brown.', 'I like apples.'], 1)])

d60_math = sub('Math', 'Math Review: Numbers, Patterns, and Time',
  'Students review recent Math skills: numbers to 120, skip counting by 4s, fractions of thirds, adding and subtracting tens, number lines, bar graphs, repeating patterns, estimating, and digital time.',
  [('What number comes right after 100?', ['101', 'one hundred one']),
   ('What is 30 add 20?', ['50', 'fifty']),
   ('On a digital clock showing 3:00, what hour is it?', ['3', 'three'])],
  [('What number comes right after 100?', ['99', '101', '110', '200'], 1),
   ('When skip counting by 4s, what number comes after 8?', ['9', '10', '11', '12'], 3),
   ('If a shape is split into three equal parts, each part is called ___.', ['A half', 'A third', 'A quarter', 'A whole'], 1),
   ('What is 20 add 30?', ['40', '50', '60', '70'], 1),
   ('In the pattern red, blue, red, blue, red, what comes next?', ['Red', 'Blue', 'Green', 'Yellow'], 1)])

d60_sci = sub('Science', 'Science Review: Animals, Water, and Sky',
  'Students review recent Science topics: reptiles, amphibians, mammals, the water cycle, day and night, gravity, the butterfly life cycle, animal coverings, and ocean animals.',
  [('What covers the skin of most reptiles?', ['scales']),
   ('What is a baby frog called before it grows legs?', ['tadpole']),
   ('What is the name of the force that pulls objects down toward the ground?', ['gravity'])],
  [('What covers the skin of most reptiles?', ['Feathers', 'Scales', 'Fur', 'Fins'], 1),
   ('Which of these animals is an amphibian?', ['A frog', 'A robin', 'A turtle', 'A shark'], 0),
   ('What causes day and night on Earth?', ['Earth slowly spinning around', 'Earth changing colour', 'The sun moving very fast', 'The moon disappearing'], 0),
   ('What do we call the resting stage inside a hard case before a caterpillar becomes a butterfly?', ['A chrysalis', 'A nest', 'A den', 'A shell only'], 0),
   ('Is ocean water salty or fresh?', ['Salty', 'Fresh', 'Frozen always', 'Colourless only'], 0)])

d60_ss = sub('SocialStudies', 'Social Studies Review: Places, Inventions, and Fair Choices',
  'Students review recent Social Studies topics: rural and urban communities, Canadian inventions, libraries, mail delivery, national parks, seasonal activities, fair group choices, museums, and grocery stores.',
  [('What do we call a busy community with many tall buildings?', ['city', 'urban community', 'urban']),
   ('What sport was invented by a Canadian named James Naismith?', ['basketball']),
   ('What is a community place where people go to buy food?', ['a grocery store', 'grocery store'])],
  [('What do we call a busy community with many tall buildings and people?', ['An urban community', 'A rural community', 'An ocean', 'A desert'], 0),
   ('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Cricket', 'Tennis'], 0),
   ('What is a national park?', ['A protected area of land set aside to keep nature safe', 'A tall office building', 'A shopping mall', 'A parking lot'], 0),
   ('Which of these is a fair way for a group to make a choice?', ['Taking turns and listening to everyone', 'Only one person deciding every time', 'Ignoring what others want', 'Arguing without listening'], 0),
   ('What is a museum?', ['A place where people can see and learn about objects from the past', 'A place to buy groceries', 'A place to mail letters', 'A place to swim'], 0)])


g1_51_60 = [
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
    _rebalance_answer_positions(g1_51_60)
    append_worksheet_days(1, g1_51_60)
