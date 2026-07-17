#!/usr/bin/env python3
"""Grade 1, Days 71-80 -- FIFTH batch, extending Grade 1 through Day 80.
Self-contained script modeled exactly on gen_grade1_days61_70.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-70 topics (see data/grade1.ts). No embedded ASCII double-quote or
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


# ─── DAY 71 ─────────────────────────────────────────────────────────────────
d71_lang = sub('Language', 'Digraph Endings: -ng and -nk',
  'Students learn that the letters ng and nk work together at the end of a word to make one ending sound, as in sing and ring for ng, and sink and pink for nk.',
  [('Name one word that ends with the ng sound, like sing or ring.', ['sing', 'ring', 'king']),
   ('Name one word that ends with the nk sound, like sink or pink.', ['sink', 'pink', 'think']),
   ('What two letters make the ending sound in the word sing?', ['ng'])],
  [('Which word ends with the ng sound?', ['Sing', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word ends with the nk sound?', ['Sink', 'Cat', 'Dog', 'Sun'], 0),
   ('Which letters end the word ring?', ['ng', 'nk', 'ck', 'sh'], 0),
   ('Which letters end the word pink?', ['nk', 'ng', 'ck', 'sh'], 0),
   ('The ng and nk endings are examples of ___.', ['Letter combinations that make one ending sound', 'Silent letters', 'Vowel teams only', 'Prefixes'], 0)])

d71_math = sub('Math', 'Skip Counting by 7s',
  'Students practise skip counting by 7s, saying the numbers 7, 14, 21, 28, and so on, to build number sense and recognize patterns.',
  [('What number comes after 7 when skip counting by 7s?', ['14', 'fourteen']),
   ('What number comes after 21 when skip counting by 7s?', ['28', 'twenty-eight']),
   ('Start at 7 and skip count by 7s two times. What is the second number?', ['14', 'fourteen'])],
  [('When skip counting by 7s, what number comes after 7?', ['14', '13', '15', '21'], 0),
   ('When skip counting by 7s, what number comes after 14?', ['21', '20', '22', '28'], 0),
   ('Which list shows skip counting by 7s?', ['7, 14, 21, 28', '7, 9, 11, 13', '7, 10, 13, 16', '5, 10, 15, 20'], 0),
   ('When skip counting by 7s, what number comes after 21?', ['28', '27', '29', '35'], 0),
   ('Skip counting by 7s means we count ___.', ['Every seventh number', 'Every second number', 'Backward only', 'Only even numbers'], 0)])

d71_sci = sub('Science', 'Clouds in the Sky: Types of Clouds',
  'Students learn that clouds are made of tiny drops of water high in the sky, and that clouds can look fluffy, flat, or wispy, with grey clouds often meaning rain is coming.',
  [('What are clouds made of, mostly tiny drops of what?', ['water', 'tiny water droplets']),
   ('Name one shape a cloud can look like, such as fluffy or flat.', ['fluffy', 'flat', 'wispy']),
   ('What colour of cloud often means rain is coming?', ['grey', 'dark grey', 'gray'])],
  [('What are clouds mostly made of?', ['Tiny drops of water', 'Solid rock', 'Sand', 'Metal'], 0),
   ('Which colour of cloud often means rain is coming soon?', ['Grey', 'Bright blue', 'Pink', 'Orange only'], 0),
   ('Which of these describes a fluffy white cloud shape?', ['Cumulus, puffy like cotton', 'Always flat and thin', 'Always tiny and invisible', 'Always red'], 0),
   ('Clouds form high up in the ___.', ['Sky', 'Ocean', 'Ground', 'Trees'], 0),
   ('Watching clouds can help us guess ___.', ['What the weather might do next', 'The time of day only', 'The colour of grass', 'The name of a season only'], 0)])

d71_ss = sub('SocialStudies', 'Police Officers: Keeping Our Community Safe',
  'Students learn that police officers help keep people safe, follow and enforce community rules, help in emergencies, and assist people who need help, such as directing traffic.',
  [('What is one job of a police officer, like keeping people safe?', ['keeping people safe', 'helping people', 'directing traffic']),
   ('Who can you call for help in an emergency, like a police officer?', ['a police officer', 'police', '911']),
   ('Name one tool a police officer might use, like a radio.', ['a radio', 'a car', 'a whistle'])],
  [('What is the main job of a police officer?', ['Keeping people in the community safe', 'Cooking food for a restaurant', 'Teaching a classroom', 'Delivering mail'], 0),
   ('Who might help direct traffic to keep streets safe?', ['A police officer', 'A librarian', 'A chef', 'A farmer'], 0),
   ('Which of these is something a police officer might do?', ['Help someone who is lost find their way home', 'Grow vegetables', 'Fly an airplane', 'Paint a picture'], 0),
   ('Why is it helpful to know how to find a police officer in an emergency?', ['They can help keep you and others safe', 'They never help anyone', 'They only work at night', 'They are not part of the community'], 0),
   ('Police officers are an example of ___.', ['Community helpers who keep people safe', 'People who grow food', 'People who deliver newspapers', 'People who build houses only'], 0)])

# ─── DAY 72 ─────────────────────────────────────────────────────────────────
d72_lang = sub('Language', 'The Letter Y as a Vowel: sky, my, happy',
  'Students learn that the letter y can act as a vowel, making a long i sound at the end of short words like my and sky, and a long e sound at the end of longer words like happy and funny.',
  [('What sound does the letter y make at the end of the word sky?', ['long i', 'i sound']),
   ('What sound does the letter y make at the end of the word happy?', ['long e', 'e sound']),
   ('Name one word where y sounds like long i, like sky or my.', ['sky', 'my', 'fly', 'cry'])],
  [('What sound does y make at the end of the word my?', ['Long i', 'Long e', 'Short a', 'Short o'], 0),
   ('What sound does y make at the end of the word happy?', ['Long e', 'Long i', 'Short u', 'Short e'], 0),
   ('Which word has y making a long i sound?', ['Sky', 'Happy', 'Funny', 'Bunny'], 0),
   ('Which word has y making a long e sound?', ['Funny', 'Sky', 'Cry', 'Fly'], 0),
   ('The letter y can act as a ___ at the end of some words.', ['Vowel', 'Consonant blend', 'Silent letter', 'Punctuation mark'], 0)])

d72_math = sub('Math', 'Ordering Numbers from Least to Greatest',
  'Students practise putting a group of numbers in order starting with the smallest, called the least, and ending with the largest, called the greatest.',
  [('Put these numbers in order from least to greatest: 5, 2, 8.', ['2, 5, 8', '2 5 8']),
   ('Which number is the least: 12, 4, 9?', ['4']),
   ('Which number is the greatest: 15, 20, 10?', ['20'])],
  [('Which list shows the numbers in order from least to greatest: 3, 7, 1?', ['1, 3, 7', '7, 3, 1', '3, 1, 7', '7, 1, 3'], 0),
   ('Which number is the least: 12, 4, 9?', ['4', '12', '9', 'They are equal'], 0),
   ('Which number is the greatest: 15, 20, 10?', ['20', '15', '10', 'They are equal'], 0),
   ('To order numbers from least to greatest, we start with the ___.', ['Smallest number', 'Largest number', 'Middle number', 'Last number written'], 0),
   ('Which list is already in order from least to greatest?', ['2, 6, 9', '9, 6, 2', '6, 2, 9', '9, 2, 6'], 0)])

d72_sci = sub('Science', 'Plant Parts We Eat: Roots, Stems, and Leaves',
  'Students learn that people eat different parts of plants, such as roots like carrots, stems like celery, and leaves like lettuce.',
  [('Name one root vegetable that people eat, like a carrot.', ['a carrot', 'carrot', 'a potato']),
   ('Name one plant stem that people eat, like celery.', ['celery']),
   ('Name one plant leaf that people eat, like lettuce.', ['lettuce', 'spinach'])],
  [('Which of these is a root that people eat?', ['A carrot', 'Celery', 'Lettuce', 'An apple'], 0),
   ('Which of these is a stem that people eat?', ['Celery', 'A carrot', 'Lettuce', 'A cherry'], 0),
   ('Which of these is a leaf that people eat?', ['Lettuce', 'A carrot', 'Celery', 'A potato'], 0),
   ('A potato is an example of a plant ___ that people eat.', ['Root', 'Flower', 'Fruit', 'Seed only'], 0),
   ('Eating different parts of plants can give our bodies ___.', ['Healthy vitamins and energy', 'No nutrition at all', 'Only water', 'Only sugar'], 0)])

d72_ss = sub('SocialStudies', 'Hospitals and Doctors: Healthcare in Our Community',
  'Students learn that hospitals and doctors help people who are sick or hurt get better, and that healthcare workers are an important part of a community.',
  [('Name one place where doctors and nurses help sick people.', ['a hospital', 'hospital', 'a clinic']),
   ('Name one job of a doctor, like helping people who are sick.', ['helping people who are sick', 'checking up on patients']),
   ('Name one healthcare worker besides a doctor, like a nurse.', ['a nurse', 'nurse'])],
  [('What is a hospital?', ['A place where doctors and nurses help sick or hurt people', 'A place to buy food', 'A place to mail letters', 'A place to see movies'], 0),
   ('What is one job of a doctor?', ['Helping people who are sick or hurt get better', 'Delivering mail', 'Cooking meals for a restaurant', 'Driving a bus'], 0),
   ('Which of these is a healthcare worker?', ['A nurse', 'A librarian', 'A farmer', 'A pilot'], 0),
   ('Why are hospitals important to a community?', ['They help keep people healthy and safe', 'They are not important', 'They only sell toys', 'They have no workers'], 0),
   ('If someone gets hurt, who might help them feel better?', ['A doctor or nurse', 'A chef', 'A mail carrier', 'A librarian'], 0)])

# ─── DAY 73 ─────────────────────────────────────────────────────────────────
d73_lang = sub('Language', 'R-Controlled Vowels: er, ir, ur',
  'Students learn that when the letter r follows a vowel, it changes the vowel sound, as in er in fern, ir in bird, and ur in turn, which often sound alike.',
  [('Name one word with the er sound, like fern or her.', ['fern', 'her', 'term']),
   ('Name one word with the ir sound, like bird or girl.', ['bird', 'girl', 'shirt']),
   ('Name one word with the ur sound, like turn or fur.', ['turn', 'fur', 'burn'])],
  [('Which word has the er sound?', ['Fern', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ir sound?', ['Bird', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ur sound?', ['Turn', 'Cat', 'Dog', 'Sun'], 0),
   ('The letters er, ir, and ur often make the ___ sound.', ['Same r-controlled vowel sound', 'A silent sound', 'A long a sound', 'A short i sound'], 0),
   ('In the word bird, which letters control the vowel sound?', ['ir', 'ur', 'er', 'ar'], 0)])

d73_math = sub('Math', 'Missing Number Subtraction Sentences',
  'Students solve subtraction sentences with a missing number, such as 9 minus what number equals 4, using known facts and counting strategies.',
  [('What number is missing: 9 minus ___ equals 4?', ['5', 'five']),
   ('What number is missing: ___ minus 3 equals 7?', ['10', 'ten']),
   ('What number is missing: 8 minus ___ equals 8?', ['0', 'zero'])],
  [('What number is missing: 9 minus ___ equals 4?', ['5', '4', '6', '3'], 0),
   ('What number is missing: ___ minus 3 equals 7?', ['10', '9', '11', '8'], 0),
   ('What number is missing: 6 minus ___ equals 2?', ['4', '3', '5', '2'], 0),
   ('What number is missing: ___ minus 5 equals 0?', ['5', '0', '10', '1'], 0),
   ('To solve a missing number subtraction sentence, it helps to ___.', ['Think about what number completes the difference', 'Guess with no strategy', 'Skip the problem', 'Always answer zero'], 0)])

d73_sci = sub('Science', 'The Human Skeleton: Bones That Support Us',
  'Students learn that the human body has many bones that make up a skeleton, which supports the body, protects organs like the heart, and helps us move.',
  [('What do we call all the bones in the body together?', ['a skeleton', 'skeleton']),
   ('Name one job of the skeleton, like supporting the body.', ['supporting the body', 'protecting organs', 'helping us move']),
   ('Name one bone in your body, like your skull or a rib.', ['skull', 'rib', 'arm bone'])],
  [('What do we call all the bones in the body together?', ['A skeleton', 'A muscle', 'A vein', 'An organ'], 0),
   ('What is one job of the skeleton?', ['Supporting the body and helping it move', 'Making blood only', 'Growing hair', 'Producing sound'], 0),
   ('Which bone protects the brain?', ['The skull', 'The rib', 'The arm bone', 'The leg bone'], 0),
   ('Ribs are bones that help protect ___.', ['The heart and lungs', 'The hair', 'The skin only', 'The teeth only'], 0),
   ('Without a skeleton, a body would not be able to ___.', ['Stand up or move properly', 'Sleep', 'Breathe at all', 'See colours'], 0)])

d73_ss = sub('SocialStudies', 'Volunteers: Helping Without Pay',
  'Students learn that a volunteer is someone who helps others without being paid, such as helping clean a park or reading to younger children.',
  [('What do we call someone who helps others without being paid?', ['a volunteer', 'volunteer']),
   ('Name one way a volunteer might help a community, like cleaning a park.', ['cleaning a park', 'reading to children', 'helping at a food bank']),
   ('Do volunteers get paid money for their help?', ['no'])],
  [('What is a volunteer?', ['Someone who helps others without being paid', 'Someone who is always paid a lot of money', 'A kind of machine', 'A type of animal'], 0),
   ('Which of these is an example of volunteering?', ['Helping clean up a park for free', 'Being paid to drive a bus', 'Selling toys at a store', 'Working at a bank for a salary'], 0),
   ('Why might someone choose to volunteer?', ['To help others and make the community better', 'Because they must be paid to help', 'Volunteering is never helpful', 'It is against the rules'], 0),
   ('Which of these could a volunteer do at a school?', ['Read stories to younger students', 'Fly an airplane', 'Build a hospital alone', 'Print money'], 0),
   ('Volunteering shows that people in a community can ___.', ['Care for each other and help without expecting pay', 'Only help if paid', 'Ignore each other', 'Never help others'], 0)])

# ─── DAY 74 ─────────────────────────────────────────────────────────────────
d74_lang = sub('Language', 'Compound Sentences: Joining Two Ideas with And',
  'Students learn that two short sentences can be joined into one longer sentence using the word and, making writing smoother and connecting related ideas.',
  [('Join these two sentences with and: I like cats. I like dogs.', ['i like cats and i like dogs', 'i like cats and dogs']),
   ('What word can join two short sentences together, like and?', ['and']),
   ('Name one reason writers join sentences with and, like to connect ideas.', ['to connect ideas', 'to make writing smoother'])],
  [('Which word can join two short sentences into one longer sentence?', ['And', 'The', 'Is', 'Was'], 0),
   ('Which sentence correctly joins two ideas with and?', ['The sun is bright and the sky is blue.', 'The sun is bright the sky is blue.', 'And the sun is bright sky.', 'Sun bright and.'], 0),
   ('Why might a writer join two short sentences with and?', ['To connect related ideas smoothly', 'To make the sentence confusing', 'To remove all punctuation', 'To make two new paragraphs'], 0),
   ('Which of these is two short sentences joined by and?', ['I ran fast and I felt happy.', 'I ran fast. I felt happy.', 'Ran fast happy I.', 'I, ran, fast, happy.'], 0),
   ('A sentence that joins two ideas together is called a ___ sentence.', ['Compound', 'Silent', 'Broken', 'Backward'], 0)])

d74_math = sub('Math', 'Fractions: Equal and Unequal Parts',
  'Students learn to tell the difference between a whole shape cut into equal parts, where each piece is the same size, and a shape cut into unequal parts, where the pieces are different sizes.',
  [('If a shape is cut into two same-size pieces, are the parts equal or unequal?', ['equal']),
   ('If a shape is cut into pieces of different sizes, are the parts equal or unequal?', ['unequal']),
   ('Name one shape you could cut into two equal parts, like a circle or a square.', ['a circle', 'a square', 'a rectangle'])],
  [('If a pizza is cut into two same-size pieces, the parts are ___.', ['Equal', 'Unequal', 'Missing', 'Doubled'], 0),
   ('If a sandwich is cut into one big piece and one small piece, the parts are ___.', ['Unequal', 'Equal', 'The same', 'Fractions only'], 0),
   ('For a fraction like one half to be correct, the parts must be ___.', ['Equal in size', 'Different colours', 'Different shapes', 'Unequal in size'], 0),
   ('Which of these shows a shape cut into equal parts?', ['A circle cut into two same-size halves', 'A circle cut into one big and one tiny piece', 'A square with no cuts', 'A triangle with a corner missing'], 0),
   ('Why do equal parts matter when sharing food fairly?', ['So everyone gets the same amount', 'So one person gets more', 'Equal parts do not matter', 'So the food disappears'], 0)])

d74_sci = sub('Science', 'Rainbows: Sunlight and Colours',
  'Students learn that a rainbow appears when sunlight passes through raindrops and splits into many colours, and that rainbows always show the colours in the same order.',
  [('What do we call the colourful arc that appears in the sky after rain?', ['a rainbow', 'rainbow']),
   ('What two things are needed to make a rainbow, like sunlight and rain?', ['sunlight and rain', 'sun and rain', 'light and water']),
   ('Name one colour you might see in a rainbow, like red or blue.', ['red', 'blue', 'orange', 'yellow', 'green', 'purple'])],
  [('What is needed to make a rainbow?', ['Sunlight and raindrops', 'Only darkness', 'Only wind', 'Only snow'], 0),
   ('What happens to sunlight when it passes through a raindrop to make a rainbow?', ['It splits into many colours', 'It disappears completely', 'It turns into snow', 'It becomes invisible'], 0),
   ('When might you be most likely to see a rainbow?', ['After rain when the sun comes out', 'In the middle of the night', 'During a snowstorm only', 'Inside a closed room'], 0),
   ('Rainbows always show their colours in ___.', ['The same order', 'A different order each time', 'No particular order', 'Only one colour'], 0),
   ('A rainbow is an example of ___.', ['Light splitting into many colours', 'A solid object', 'A living thing', 'A sound wave'], 0)])

d74_ss = sub('SocialStudies', 'Newcomers to Canada: Welcoming New Families',
  'Students learn that many families move to Canada from other countries to start a new life, and that welcoming newcomers with kindness helps them feel at home in their new community.',
  [('What do we call a family that has just moved to a new country?', ['newcomers', 'a newcomer family']),
   ('Name one kind way to welcome a newcomer to your class, like saying hello.', ['saying hello', 'being their friend', 'helping them feel welcome']),
   ('Why might a family move to a new country, like Canada?', ['to start a new life', 'for a better life', 'for safety'])],
  [('What is a newcomer?', ['A person or family who has recently moved to a new country', 'A person born in the same town forever', 'A type of building', 'A kind of holiday'], 0),
   ('Which of these is a kind way to welcome a newcomer at school?', ['Saying hello and inviting them to play', 'Ignoring them completely', 'Refusing to be their friend', 'Making fun of how they speak'], 0),
   ('Why might a family choose to move to a new country?', ['To find a better or safer life', 'They never have a reason', 'They are forced to leave for no reason', 'Only for vacation'], 0),
   ('How can a community help newcomers feel at home?', ['By being kind, friendly, and helpful', 'By ignoring their needs', 'By excluding them from activities', 'By refusing to speak with them'], 0),
   ('Communities in Canada are often made up of ___.', ['People and families from many different places', 'Only one kind of family', 'People who never move', 'Only very old buildings'], 0)])

# ─── DAY 75 ─────────────────────────────────────────────────────────────────
d75_lang = sub('Language', 'Onomatopoeia: Sound Words in Stories',
  'Students learn that onomatopoeia is when a word sounds like the noise it describes, such as buzz, splash, or crash, and that authors use these words to make stories more exciting.',
  [('Name one sound word that sounds like the noise it describes, like buzz.', ['buzz', 'splash', 'crash', 'pop']),
   ('What sound word describes the noise a bee makes?', ['buzz']),
   ('What sound word describes something falling into water?', ['splash'])],
  [('What is onomatopoeia?', ['A word that sounds like the noise it describes', 'A word with no meaning', 'A type of punctuation', 'A silent letter'], 0),
   ('Which word is an example of onomatopoeia for a bee?', ['Buzz', 'Happy', 'Table', 'Green'], 0),
   ('Which word is an example of onomatopoeia for something falling in water?', ['Splash', 'Chair', 'Yellow', 'Quiet'], 0),
   ('Why do authors use sound words like crash and pop in stories?', ['To make the story more exciting and vivid', 'To confuse the reader', 'To make the story shorter', 'To remove all action'], 0),
   ('Which of these is a sound word for something popping?', ['Pop', 'Book', 'Chair', 'Window'], 0)])

d75_math = sub('Math', 'Money: Counting Up to One Dollar',
  'Students practise adding coins such as quarters, dimes, and nickels to see how close they can get to making one dollar, which equals 100 cents.',
  [('How many cents make one dollar?', ['100 cents', '100']),
   ('If you have 4 quarters, how many cents do you have?', ['100 cents', '100']),
   ('If you have 75 cents, how many more cents do you need to make one dollar?', ['25 cents', '25'])],
  [('How many cents make one dollar?', ['100 cents', '50 cents', '10 cents', '75 cents'], 0),
   ('If you have 4 quarters, how much money do you have?', ['100 cents (one dollar)', '50 cents', '75 cents', '25 cents'], 0),
   ('If you have 75 cents, how many more cents do you need to make one dollar?', ['25 cents', '50 cents', '10 cents', '15 cents'], 0),
   ('Which coin is worth 25 cents?', ['A quarter', 'A dime', 'A nickel', 'A penny'], 0),
   ('Counting coins to reach one dollar helps us practise ___.', ['Adding money amounts', 'Telling time', 'Measuring length', 'Reading a map'], 0)])

d75_sci = sub('Science', 'Deserts: Life in a Dry Habitat',
  'Students learn that a desert is a very dry habitat with little rain, and that plants and animals living there, like cactuses and camels, have special ways to survive with very little water.',
  [('What kind of habitat gets very little rain, like a desert?', ['a desert', 'desert']),
   ('Name one plant that can survive in a desert, like a cactus.', ['a cactus', 'cactus']),
   ('Name one animal that can survive in a desert, like a camel.', ['a camel', 'camel'])],
  [('What is a desert?', ['A dry habitat that gets very little rain', 'A habitat covered in ice', 'A habitat found only underwater', 'A habitat with constant rain'], 0),
   ('Which plant is well known for surviving in the desert?', ['A cactus', 'A water lily', 'A pine tree', 'A fern'], 0),
   ('Which animal is known for surviving in the desert with little water?', ['A camel', 'A polar bear', 'A whale', 'A penguin'], 0),
   ('How do desert plants like cactuses often survive with little water?', ['They store water inside their thick stems', 'They need rain every day', 'They grow only underwater', 'They cannot survive at all'], 0),
   ('Which of these best describes desert weather?', ['Very dry with little rainfall', 'Very wet with constant rain', 'Always covered in snow', 'Always foggy'], 0)])

d75_ss = sub('SocialStudies', 'Earning Money: Jobs and Working',
  'Students learn that people earn money by working at a job, and that the money they earn can be used to pay for things their family needs, like food and clothing.',
  [('What do we call the money a person gets for doing a job?', ['earnings', 'pay', 'wages']),
   ('Name one job a person could have to earn money, like a teacher.', ['a teacher', 'a doctor', 'a farmer']),
   ('What can families use the money they earn for, like food?', ['food', 'clothing', 'a home'])],
  [('How do most people earn money?', ['By working at a job', 'Money grows on trees', 'It appears for free', 'By doing nothing'], 0),
   ('What can a family use the money they earn for?', ['Buying food, clothing, and a home', 'Nothing important', 'Only toys', 'Throwing it away'], 0),
   ('Which of these is an example of a job where someone earns money?', ['Working as a teacher', 'Sleeping all day', 'Watching television', 'Playing video games all day'], 0),
   ('Why is it important for people to earn money?', ['To help pay for things their family needs', 'Money is never needed', 'To avoid working', 'It has no purpose'], 0),
   ('Working hard at a job to earn money is an example of being ___.', ['Responsible', 'Careless', 'Unhelpful', 'Lazy'], 0)])

# ─── DAY 76 ─────────────────────────────────────────────────────────────────
d76_lang = sub('Language', 'Similes: Comparing with Like and As',
  'Students learn that a simile compares two different things using the words like or as, such as saying someone is as fast as a cheetah, to help readers picture an idea more clearly.',
  [('What two words are often used in a simile, like like and as?', ['like and as', 'like, as']),
   ('Finish this simile: The snow was as white as ___.', ['snow', 'a cloud', 'milk']),
   ('Name one simile you know, like busy as a bee.', ['busy as a bee', 'as fast as a cheetah', 'as quiet as a mouse'])],
  [('What is a simile?', ['A comparison using the words like or as', 'A word that sounds like a noise', 'A type of punctuation', 'A silent letter'], 0),
   ('Which sentence is an example of a simile?', ['She was as brave as a lion.', 'She was brave.', 'The lion was big.', 'She ran quickly.'], 0),
   ('Which words are commonly used in a simile?', ['Like and as', 'And and but', 'Is and was', 'The and a'], 0),
   ('Why do writers use similes?', ['To help readers picture an idea more clearly', 'To confuse the reader', 'To remove description', 'To make writing shorter only'], 0),
   ('Which of these completes a simile: The baby was as quiet as a ___.', ['Mouse', 'Table', 'Chair', 'Rock band'], 0)])

d76_math = sub('Math', 'Solving Simple Addition and Subtraction Word Problems',
  'Students practise reading a short word problem, deciding whether to add or subtract, and solving it, such as figuring out how many apples are left after some are eaten.',
  [('Sam had 6 apples and ate 2. How many apples are left?', ['4', 'four']),
   ('Mia had 3 stickers and got 5 more. How many stickers does she have now?', ['8', 'eight']),
   ('Should you add or subtract to find how many are left after some are used?', ['subtract'])],
  [('Sam had 6 apples and ate 2. How many apples are left?', ['4', '3', '5', '8'], 0),
   ('Mia had 3 stickers and got 5 more. How many stickers does she have now?', ['8', '7', '9', '2'], 0),
   ('A word problem that asks how many are left usually means you should ___.', ['Subtract', 'Add', 'Multiply', 'Ignore the numbers'], 0),
   ('A word problem that asks how many in all usually means you should ___.', ['Add', 'Subtract', 'Skip count only', 'Ignore the numbers'], 0),
   ('Tom had 4 toy cars and got 3 more for his birthday. How many toy cars does he have now?', ['7', '6', '8', '1'], 0)])

d76_sci = sub('Science', 'Arctic Animals: Life in the Cold',
  'Students learn that Arctic animals, such as polar bears and penguins, have special features like thick fur or feathers and fat to help them survive in very cold, icy habitats.',
  [('Name one animal that lives in a cold Arctic habitat, like a polar bear.', ['a polar bear', 'polar bear', 'a penguin']),
   ('Name one thing that helps an Arctic animal stay warm, like thick fur.', ['thick fur', 'fat', 'feathers']),
   ('Is the Arctic a very cold or very hot place?', ['very cold', 'cold'])],
  [('Which animal is known for living in the cold Arctic?', ['A polar bear', 'A camel', 'A lion', 'A monkey'], 0),
   ('What helps many Arctic animals stay warm in the cold?', ['Thick fur or fat', 'Thin skin only', 'Bright colours', 'Large ears'], 0),
   ('What kind of weather does the Arctic usually have?', ['Very cold with snow and ice', 'Very hot and dry', 'Warm and rainy', 'Mild all year'], 0),
   ('Why might an Arctic animal have white fur?', ['To blend in with the snow and ice', 'To stay cool in the heat', 'To attract more sunlight', 'It has no purpose'], 0),
   ('Which of these is a feature that helps Arctic animals survive the cold?', ['A thick layer of fat called blubber', 'Very thin fur with no warmth', 'Living only in warm deserts', 'Having no protection from cold'], 0)])

d76_ss = sub('SocialStudies', 'Airports: Travelling by Airplane',
  'Students learn that an airport is a place where airplanes take off and land, helping people travel quickly to faraway places for work, visiting family, or vacations.',
  [('What do we call a place where airplanes take off and land?', ['an airport', 'airport']),
   ('Name one reason people might travel by airplane, like visiting family.', ['visiting family', 'going on vacation', 'for work']),
   ('Is travelling by airplane usually faster or slower than travelling by car for long trips?', ['faster'])],
  [('What is an airport?', ['A place where airplanes take off and land', 'A place to borrow books', 'A place to buy groceries', 'A place to see movies'], 0),
   ('Why might a family travel by airplane?', ['To visit family or go on vacation far away', 'Airplanes are never used for travel', 'To buy milk nearby', 'To walk to school'], 0),
   ('For very long trips, travelling by airplane is usually ___ than travelling by car.', ['Faster', 'Slower', 'The same speed', 'Impossible'], 0),
   ('Who helps fly the airplane at an airport?', ['A pilot', 'A librarian', 'A chef', 'A farmer'], 0),
   ('Airports help connect communities by allowing people to ___.', ['Travel quickly to faraway places', 'Never leave their town', 'Only travel by boat', 'Stay home always'], 0)])

# ─── DAY 77 ─────────────────────────────────────────────────────────────────
d77_lang = sub('Language', 'Making Connections: Text to Self',
  'Students learn that good readers make connections between a story and their own lives, thinking about times they felt or did something similar to a character.',
  [('What do we call it when a reader connects a story to their own life?', ['a text-to-self connection', 'making a connection']),
   ('If a character in a story feels nervous on the first day of school, name a time you may have felt the same way.', ['first day of school', 'a new place', 'starting something new']),
   ('Why do good readers make connections while reading?', ['it helps them understand the story', 'to understand characters better'])],
  [('What is a text-to-self connection?', ['Connecting a story to something in your own life', 'Ignoring the story completely', 'Skipping every page', 'Only reading the title'], 0),
   ('If a character feels excited about a birthday party, a reader might connect this to ___.', ['A time they felt excited about their own celebration', 'A math problem', 'A weather report', 'A grocery list'], 0),
   ('Why is making connections helpful for readers?', ['It helps them understand and remember the story better', 'It makes reading pointless', 'It confuses the reader', 'It replaces reading completely'], 0),
   ('Which of these is an example of a text-to-self connection?', ['I felt scared like the character when I was lost once too.', 'The book has ten pages.', 'The cover is blue.', 'The author lives far away.'], 0),
   ('Making connections while reading is a strategy used by ___.', ['Good readers to understand a story better', 'Only writers', 'Only teachers', 'No one'], 0)])

d77_math = sub('Math', 'Comparing Length: Longer, Shorter, and the Same',
  'Students compare the length of two or more objects directly, using words like longer, shorter, and the same to describe the difference.',
  [('If a pencil is longer than a crayon, which object is shorter?', ['the crayon', 'crayon']),
   ('Name one object in your home that is longer than a pencil.', ['a table', 'a broom', 'a book']),
   ('If two ribbons are exactly the same length, what word describes them?', ['the same', 'equal'])],
  [('If a pencil is longer than a crayon, the crayon is ___.', ['Shorter', 'Longer', 'The same length', 'Heavier'], 0),
   ('Which of these is likely the longest object?', ['A school bus', 'A pencil', 'A crayon', 'A paperclip'], 0),
   ('If two ribbons are exactly the same length, we say they are ___.', ['Equal in length', 'Different lengths', 'Both very short', 'Both very heavy'], 0),
   ('Which word describes an object that is not as long as another?', ['Shorter', 'Longer', 'Wider', 'Heavier'], 0),
   ('To compare the length of two objects, you can line them up and see which one is ___.', ['Longer or shorter', 'Louder', 'Heavier only', 'Colder'], 0)])

d77_sci = sub('Science', 'Composting: Turning Food Scraps into Soil',
  'Students learn that composting is a way to turn food scraps and plant waste, like banana peels and leaves, into rich soil that helps new plants grow.',
  [('What do we call turning food scraps into rich soil?', ['composting', 'compost']),
   ('Name one food scrap that can be composted, like a banana peel.', ['a banana peel', 'banana peel', 'apple core']),
   ('What can compost help new plants do, like grow?', ['grow', 'grow better'])],
  [('What is composting?', ['Turning food scraps and plant waste into rich soil', 'Throwing all garbage into the ocean', 'Burning old leaves', 'Freezing food waste forever'], 0),
   ('Which of these can be composted?', ['A banana peel', 'A plastic bottle', 'A glass jar', 'A metal can'], 0),
   ('What does compost help new plants do?', ['Grow better with rich soil', 'Stop growing completely', 'Turn into rocks', 'Disappear'], 0),
   ('Why is composting a helpful habit for the environment?', ['It reduces waste and creates healthy soil', 'It creates more garbage', 'It has no benefit', 'It harms plants'], 0),
   ('Which of these is an example of something that should NOT go in a compost bin?', ['A plastic toy', 'An apple core', 'Dried leaves', 'A banana peel'], 0)])

d77_ss = sub('SocialStudies', 'Weather Around the World: Hot and Cold Climates',
  'Students learn that different places around the world have very different climates, from very hot places near the equator to very cold places near the poles, which affects how people live and dress.',
  [('Name one place that is usually very hot, like a desert near the equator.', ['a desert', 'near the equator', 'a hot country']),
   ('Name one place that is usually very cold, like near the North Pole.', ['near the north pole', 'the arctic', 'a cold country']),
   ('Why might people in a hot climate dress differently than people in a cold climate?', ['to stay comfortable', 'because of the weather'])],
  [('What do we call the usual weather pattern of a place over a long time?', ['Climate', 'A season', 'A storm', 'A forecast'], 0),
   ('Which of these places is usually very hot?', ['A desert near the equator', 'The North Pole', 'A snowy mountain top', 'The Arctic Ocean'], 0),
   ('Which of these places is usually very cold?', ['Near the North Pole', 'A tropical rainforest', 'A hot desert', 'A sunny beach at the equator'], 0),
   ('Why might people who live in cold climates wear heavy coats and boots?', ['To stay warm in cold weather', 'They never feel cold', 'To stay cool', 'Coats are only for decoration'], 0),
   ('Different climates around the world affect how people ___.', ['Dress and live', 'Never change anything', 'Only eat one kind of food', 'Have no effect at all'], 0)])

# ─── DAY 78 ─────────────────────────────────────────────────────────────────
d78_lang = sub('Language', 'Descriptive Writing: Painting a Picture with Words',
  'Students learn that descriptive writing uses detailed words about how something looks, sounds, feels, smells, or tastes to help readers picture it clearly in their minds.',
  [('Name one describing word you could use for a lemon, like sour or yellow.', ['sour', 'yellow', 'bumpy']),
   ('What is descriptive writing used for, like helping readers picture something?', ['helping readers picture something', 'to describe things clearly']),
   ('Name one sense you can use in descriptive writing, like sight or smell.', ['sight', 'smell', 'sound', 'taste', 'touch'])],
  [('What is descriptive writing?', ['Writing that uses detailed words to help readers picture something', 'Writing with no details at all', 'A list of numbers', 'A type of math problem'], 0),
   ('Which sentence is the most descriptive?', ['The bright red apple was crisp and sweet.', 'The apple was there.', 'Apple.', 'It was a fruit.'], 0),
   ('Which of these senses might a writer use to describe a flower?', ['Smell, sight, and touch', 'Only numbers', 'Only math facts', 'None at all'], 0),
   ('Descriptive writing helps a reader ___.', ['Picture the story clearly in their mind', 'Skip the story entirely', 'Forget the details', 'Ignore the characters'], 0),
   ('Which word is a strong describing word for a stormy sky?', ['Dark and swirling', 'A sky', 'It', 'Thing'], 0)])

d78_math = sub('Math', 'Time: Morning, Afternoon, and Evening',
  'Students learn to sort daily activities into morning, afternoon, and evening, building an understanding of how a day is divided into different parts.',
  [('Name one activity you do in the morning, like eating breakfast.', ['eating breakfast', 'waking up', 'brushing teeth']),
   ('Name one activity you do in the evening, like eating dinner.', ['eating dinner', 'going to bed', 'taking a bath']),
   ('Is lunch usually eaten in the morning or the afternoon?', ['the afternoon', 'afternoon'])],
  [('Which activity usually happens in the morning?', ['Eating breakfast', 'Going to bed', 'Eating dinner', 'Watching the sunset'], 0),
   ('Which activity usually happens in the evening?', ['Eating dinner', 'Eating breakfast', 'Waking up', 'Going to school'], 0),
   ('Is lunch usually eaten in the morning or afternoon?', ['Afternoon', 'Morning', 'Evening', 'Night'], 0),
   ('Which part of the day comes right after morning?', ['Afternoon', 'Evening', 'Night', 'Midnight'], 0),
   ('Sorting activities into morning, afternoon, and evening helps us understand ___.', ['How a day is divided into different parts', 'How to add numbers', 'How to measure length', 'How to count coins'], 0)])

d78_sci = sub('Science', 'Ladybugs and Beetles: Helpful Insects',
  'Students learn that ladybugs and other beetles are helpful insects because they eat pests like aphids that can harm garden plants.',
  [('Name one insect that helps gardens by eating pests, like a ladybug.', ['a ladybug', 'ladybug']),
   ('What small pest do ladybugs like to eat, like aphids?', ['aphids', 'tiny bugs']),
   ('How many legs does a ladybug have, like an insect?', ['6', 'six'])],
  [('Which insect is known for helping gardens by eating small pests?', ['A ladybug', 'A housefly', 'A mosquito', 'A moth'], 0),
   ('What small pest do ladybugs often eat?', ['Aphids', 'Large birds', 'Fish', 'Worms only'], 0),
   ('How many legs does a ladybug have, like other insects?', ['Six', 'Eight', 'Four', 'Ten'], 0),
   ('Why are ladybugs considered helpful to gardeners?', ['They eat pests that harm plants', 'They destroy all the plants', 'They scare away helpful bees', 'They have no effect on gardens'], 0),
   ('A ladybug is an example of a type of insect called a ___.', ['Beetle', 'Mammal', 'Reptile', 'Amphibian'], 0)])

d78_ss = sub('SocialStudies', 'Knowing Your Address: Where You Live',
  'Students learn why it is helpful to know their home address, including street name and city, so they can find their way home and share it with a trusted adult in an emergency.',
  [('What do we call the street name and number where you live?', ['an address', 'address']),
   ('Why is it helpful to know your address, like for an emergency?', ['for an emergency', 'to find your way home', 'so a trusted adult can help you']),
   ('Who should you tell your address to if you need help, like a police officer?', ['a police officer', 'a trusted adult', 'a parent'])],
  [('What is an address?', ['The street name and number where a person lives', 'A type of food', 'A kind of game', 'A school subject'], 0),
   ('Why is it helpful for a child to know their home address?', ['So they can get help finding their way home in an emergency', 'It is never useful', 'Only adults need addresses', 'Addresses are secret from everyone'], 0),
   ('Who is a safe person to share your address with if you need help?', ['A trusted adult like a parent or police officer', 'A stranger you just met', 'No one, ever', 'Anyone who asks online'], 0),
   ('Which of these is part of a home address?', ['A street name and number', 'A favourite colour', 'A pet name', 'A birthday'], 0),
   ('Knowing your address can help keep you ___.', ['Safe if you ever get lost', 'Confused', 'Unable to get help', 'Unsafe'], 0)])

# ─── DAY 79 ─────────────────────────────────────────────────────────────────
d79_lang = sub('Language', 'Asking Questions Before, During, and After Reading',
  'Students learn that good readers ask questions before reading to predict what a book might be about, during reading to check understanding, and after reading to think about what they learned.',
  [('Name one question you could ask before reading a book, like what will this book be about.', ['what will this book be about', 'what is the title telling me']),
   ('Name one question you could ask during reading, like what just happened.', ['what just happened', 'why did the character do that']),
   ('Name one question you could ask after reading, like what did I learn.', ['what did i learn', 'what was the lesson'])],
  [('Why might a reader ask a question before starting a book?', ['To predict what the book might be about', 'To skip the book entirely', 'To ignore the title', 'To avoid reading'], 0),
   ('Why might a reader ask a question while reading a story?', ['To check their understanding of what is happening', 'To forget the story', 'To close the book', 'To stop thinking'], 0),
   ('Why might a reader ask a question after finishing a book?', ['To think about what they learned or enjoyed', 'To erase their memory of the book', 'To avoid discussing it', 'Questions are not useful after reading'], 0),
   ('Which of these is a good question to ask before reading, based on the cover?', ['What do I think this book will be about?', 'What did I eat for lunch?', 'What colour is the sky?', 'What time is it?'], 0),
   ('Asking questions while reading helps a reader ___.', ['Understand and remember the story better', 'Forget everything they read', 'Read more slowly with no purpose', 'Ignore the characters'], 0)])

d79_math = sub('Math', 'Data: Making a Simple Survey and Chart',
  'Students learn to ask classmates a simple survey question, such as their favourite fruit, collect the answers, and organize the results into a simple chart.',
  [('What do we call asking a group of people the same question to collect information?', ['a survey', 'survey']),
   ('Name one question you could use for a survey, like what is your favourite fruit.', ['what is your favourite fruit', 'what is your favourite colour']),
   ('After collecting survey answers, where can you organize them, like on a chart?', ['a chart', 'chart'])],
  [('What is a survey?', ['Asking a group of people the same question to collect information', 'A type of shape', 'A math symbol', 'A kind of clock'], 0),
   ('Which of these is a good survey question?', ['What is your favourite fruit?', 'What time is it right now?', 'How many legs does a spider have?', 'What colour is the sky?'], 0),
   ('After collecting survey answers, what can we use to organize the results?', ['A chart', 'A ruler', 'A clock', 'A map'], 0),
   ('If most classmates chose apples as their favourite fruit in a survey, apples would be the ___ answer.', ['Most popular', 'Least popular', 'Only', 'Wrong'], 0),
   ('A chart of survey results helps us ___.', ['See information clearly at a glance', 'Hide the information', 'Make the data harder to read', 'Erase the results'], 0)])

d79_sci = sub('Science', 'Animal Diets: Herbivores, Carnivores, and Omnivores',
  'Students learn that animals can be grouped by what they eat: herbivores eat only plants, carnivores eat only other animals, and omnivores eat both plants and animals.',
  [('What do we call an animal that eats only plants?', ['a herbivore', 'herbivore']),
   ('What do we call an animal that eats only other animals?', ['a carnivore', 'carnivore']),
   ('What do we call an animal that eats both plants and animals?', ['an omnivore', 'omnivore'])],
  [('What do we call an animal that eats only plants?', ['A herbivore', 'A carnivore', 'An omnivore', 'A predator only'], 0),
   ('What do we call an animal that eats only other animals?', ['A carnivore', 'A herbivore', 'An omnivore', 'A plant'], 0),
   ('What do we call an animal that eats both plants and animals?', ['An omnivore', 'A herbivore', 'A carnivore', 'A producer'], 0),
   ('Which of these animals is a herbivore that eats mostly plants?', ['A rabbit', 'A lion', 'A shark', 'A wolf'], 0),
   ('Which of these animals is an omnivore that eats both plants and animals?', ['A bear', 'A cow', 'A shark', 'A rabbit'], 0)])

d79_ss = sub('SocialStudies', 'Time Capsules: Saving Memories for the Future',
  'Students learn that a time capsule is a container filled with objects and messages from today that is saved and opened many years later, helping people in the future learn about the past.',
  [('What do we call a container of objects saved to be opened in the future?', ['a time capsule', 'time capsule']),
   ('Name one object you might put in a time capsule, like a photo or letter.', ['a photo', 'a letter', 'a drawing']),
   ('Why might people make a time capsule, like to share memories with the future?', ['to share memories with the future', 'so people in the future can learn about today'])],
  [('What is a time capsule?', ['A container of objects saved to be opened in the future', 'A kind of clock', 'A type of vehicle', 'A musical instrument'], 0),
   ('Which of these might someone put inside a time capsule?', ['A photo and a letter', 'A live animal', 'A running car', 'A full-grown tree'], 0),
   ('Why might people create a time capsule?', ['To share memories and objects with people in the future', 'To throw items away forever', 'To hide from other people', 'It has no purpose'], 0),
   ('A time capsule is usually opened ___ after it is buried or stored.', ['Many years later', 'The very next day', 'Never', 'Immediately'], 0),
   ('Time capsules help future people learn about ___.', ['What life was like in the past', 'Only the weather tomorrow', 'Nothing at all', 'Only numbers'], 0)])

# ─── DAY 80 (Review) ────────────────────────────────────────────────────────
d80_lang = sub('Language', 'Language Review: Y as a Vowel, R-Controlled Vowels, and Reading Strategies',
  'Students review recent Language skills: digraph endings, y as a vowel, r-controlled vowels, compound sentences, onomatopoeia, similes, text-to-self connections, descriptive writing, and questioning strategies.',
  [('Name one word where y sounds like long i, like sky or my.', ['sky', 'my', 'fly', 'cry']),
   ('Name one word with the er sound, like fern or her.', ['fern', 'her', 'term']),
   ('What word can join two short sentences together, like and?', ['and'])],
  [('Which word ends with the ng sound?', ['Sing', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has y making a long i sound?', ['Sky', 'Happy', 'Funny', 'Bunny'], 0),
   ('Which word has the er sound?', ['Fern', 'Cat', 'Dog', 'Sun'], 0),
   ('Which sentence correctly joins two ideas with and?', ['The sun is bright and the sky is blue.', 'The sun is bright the sky is blue.', 'And the sun is bright sky.', 'Sun bright and.'], 0),
   ('Which sentence is an example of a simile?', ['She was as brave as a lion.', 'She was brave.', 'The lion was big.', 'She ran quickly.'], 0)])

d80_math = sub('Math', 'Math Review: Counting, Fractions, Money, and Time',
  'Students review recent Math skills: skip counting by 7s, ordering numbers, missing number subtraction, equal and unequal fraction parts, counting money to one dollar, word problems, comparing length, and parts of a day.',
  [('What number comes after 7 when skip counting by 7s?', ['14', 'fourteen']),
   ('Which number is the greatest: 15, 20, 10?', ['20']),
   ('How many cents make one dollar?', ['100 cents', '100'])],
  [('When skip counting by 7s, what number comes after 7?', ['14', '13', '15', '21'], 0),
   ('Which list shows the numbers in order from least to greatest: 3, 7, 1?', ['1, 3, 7', '7, 3, 1', '3, 1, 7', '7, 1, 3'], 0),
   ('If a pizza is cut into two same-size pieces, the parts are ___.', ['Equal', 'Unequal', 'Missing', 'Doubled'], 0),
   ('How many cents make one dollar?', ['100 cents', '50 cents', '10 cents', '75 cents'], 0),
   ('Which activity usually happens in the morning?', ['Eating breakfast', 'Going to bed', 'Eating dinner', 'Watching the sunset'], 0)])

d80_sci = sub('Science', 'Science Review: Weather, Plants, Habitats, and Animals',
  'Students review recent Science topics: clouds, plant parts we eat, the human skeleton, rainbows, deserts, arctic animals, composting, ladybugs, and animal diets.',
  [('What are clouds made of, mostly tiny drops of what?', ['water', 'tiny water droplets']),
   ('Name one root vegetable that people eat, like a carrot.', ['a carrot', 'carrot', 'a potato']),
   ('What do we call all the bones in the body together?', ['a skeleton', 'skeleton'])],
  [('What are clouds mostly made of?', ['Tiny drops of water', 'Solid rock', 'Sand', 'Metal'], 0),
   ('What do we call all the bones in the body together?', ['A skeleton', 'A muscle', 'A vein', 'An organ'], 0),
   ('What is a desert?', ['A dry habitat that gets very little rain', 'A habitat covered in ice', 'A habitat found only underwater', 'A habitat with constant rain'], 0),
   ('Which animal is known for living in the cold Arctic?', ['A polar bear', 'A camel', 'A lion', 'A monkey'], 0),
   ('What do we call an animal that eats only plants?', ['A herbivore', 'A carnivore', 'An omnivore', 'A predator only'], 0)])

d80_ss = sub('SocialStudies', 'Social Studies Review: Helpers, Newcomers, and Travel',
  'Students review recent Social Studies topics: police officers, hospitals and doctors, volunteers, newcomers to Canada, earning money, airports, weather around the world, addresses, and time capsules.',
  [('What is one job of a police officer, like keeping people safe?', ['keeping people safe', 'helping people', 'directing traffic']),
   ('What do we call someone who helps others without being paid?', ['a volunteer', 'volunteer']),
   ('What do we call the street name and number where you live?', ['an address', 'address'])],
  [('What is the main job of a police officer?', ['Keeping people in the community safe', 'Cooking food for a restaurant', 'Teaching a classroom', 'Delivering mail'], 0),
   ('What is a hospital?', ['A place where doctors and nurses help sick or hurt people', 'A place to buy food', 'A place to mail letters', 'A place to see movies'], 0),
   ('What is a volunteer?', ['Someone who helps others without being paid', 'Someone who is always paid a lot of money', 'A kind of machine', 'A type of animal'], 0),
   ('What is an airport?', ['A place where airplanes take off and land', 'A place to borrow books', 'A place to buy groceries', 'A place to see movies'], 0),
   ('What is an address?', ['The street name and number where a person lives', 'A type of food', 'A kind of game', 'A school subject'], 0)])


g1_71_80 = [
    day(71, [d71_lang, d71_math, d71_sci, d71_ss]),
    day(72, [d72_lang, d72_math, d72_sci, d72_ss]),
    day(73, [d73_lang, d73_math, d73_sci, d73_ss]),
    day(74, [d74_lang, d74_math, d74_sci, d74_ss]),
    day(75, [d75_lang, d75_math, d75_sci, d75_ss]),
    day(76, [d76_lang, d76_math, d76_sci, d76_ss]),
    day(77, [d77_lang, d77_math, d77_sci, d77_ss]),
    day(78, [d78_lang, d78_math, d78_sci, d78_ss]),
    day(79, [d79_lang, d79_math, d79_sci, d79_ss]),
    day(80, [d80_lang, d80_math, d80_sci, d80_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_71_80, seed=20260912)
    append_worksheet_days(1, g1_71_80)
