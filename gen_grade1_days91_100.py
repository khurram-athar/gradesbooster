#!/usr/bin/env python3
"""Grade 1, Days 91-100 -- SEVENTH batch, extending Grade 1 through Day 100.
Self-contained script modeled exactly on gen_grade1_days81_90.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-90 topics (see data/grade1.ts / data/grade1.json). No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely to keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260920):
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


# ─── DAY 91 ─────────────────────────────────────────────────────────────────
d91_lang = sub('Language', 'Vowel Teams: ie and igh (Long I Sound)',
  'Students learn that the letters ie and igh can each spell the long i sound, as in pie and tie, and in night and light.',
  [('Does the ie in pie make the long i sound or the short i sound?', ['long i sound', 'long i']),
   ('Does the igh in night make the long i sound or the short i sound?', ['long i sound', 'long i']),
   ('Name one more word with the igh spelling for long i, like night or light.', ['night', 'light', 'might', 'right', 'sight', 'bright'])],
  [('Which word has the long i sound spelled ie?', ['Pie', 'Pit', 'Pin', 'Sit'], 0),
   ('Which word has the long i sound spelled igh?', ['Sit', 'Light', 'Pig', 'Fin'], 1),
   ('The letters ie in a word like pie usually make what sound?', ['The long i sound', 'The short i sound', 'The short e sound', 'The long o sound'], 0),
   ('Which word has the same igh spelling as night?', ['Bright', 'Bit', 'Bin', 'Big'], 0),
   ('Knowing that ie and igh can both spell long i helps readers ___.', ['Try the long i sound when they see these spellings', 'Never try any new sound', 'Skip every word with these letters', 'Only ever guess the short i sound'], 0)])

d91_math = sub('Math', 'Numbers to 200: Counting Beyond 150',
  'Students extend their number sense from 150 to 200, learning to read, write, and count numbers in this range using their understanding of tens and ones.',
  [('What number comes right after 169?', ['170', 'one hundred seventy']),
   ('What number comes right after 199?', ['200', 'two hundred']),
   ('Is 182 greater than or less than 178?', ['greater than', 'greater'])],
  [('What number comes right after 159?', ['160', '161', '150', '169'], 0),
   ('What number comes right after 189?', ['190', '191', '180', '199'], 0),
   ('Which number is greater, 175 or 157?', ['175', '157', 'They are equal', 'Cannot tell'], 0),
   ('The number 200 has how many hundreds?', ['2', '20', '200', '1'], 0),
   ('Counting to 200 builds on our understanding of ___.', ['Tens and ones', 'Only colours', 'Only shapes', 'Only time'], 0)])

d91_sci = sub('Science', 'Our Heart: A Muscle That Pumps Blood',
  'Students learn that the heart is a strong muscle inside our chest that pumps blood through our body, delivering the oxygen and nutrients our body needs.',
  [('What body part pumps blood through our body?', ['heart']),
   ('Is the heart a muscle?', ['yes']),
   ('Does blood carry oxygen to the rest of our body?', ['yes'])],
  [('What is the heart?', ['A strong muscle that pumps blood', 'A bone in our leg', 'A part of our ear', 'A type of food'], 0),
   ('Where is the heart located?', ['Inside our chest', 'Inside our foot', 'Outside our body', 'Inside our ear'], 0),
   ('What does blood carry to the rest of our body?', ['Oxygen and nutrients', 'Only water', 'Only air', 'Nothing at all'], 0),
   ('Why is the heart an important muscle?', ['It pumps blood that our whole body needs', 'It has no real job', 'It only helps us hear', 'It only helps us see'], 0),
   ('The heart is best described as a muscle that ___.', ['Pumps blood through our body', 'Helps us smell', 'Helps us taste', 'Helps us think'], 0)])

d91_ss = sub('SocialStudies', 'Land Acknowledgements: Respecting Indigenous Territory',
  'Students learn that a land acknowledgement is a statement recognizing the Indigenous Peoples who have cared for the land now called Canada since long before settlers arrived.',
  [('What do we call a statement that recognizes the Indigenous Peoples connected to a land?', ['land acknowledgement']),
   ('Have Indigenous Peoples cared for the land now called Canada for a very long time?', ['yes']),
   ('Why might a school say a land acknowledgement at an assembly?', ['to show respect', 'to honour Indigenous Peoples', 'respect'])],
  [('What is a land acknowledgement?', ['A statement that recognizes Indigenous Peoples connected to the land', 'A rule about traffic safety', 'A kind of food', 'A type of building'], 0),
   ('Why do schools and communities share land acknowledgements?', ['To show respect for Indigenous Peoples and their long connection to the land', 'Land acknowledgements have no meaning at all', 'To ignore the history of the land', 'To replace Indigenous history'], 0),
   ('Have Indigenous Peoples lived on and cared for this land for a short time or a long time?', ['A very long time', 'A single year', 'One week', 'They have never lived here'], 0),
   ('Listening to a land acknowledgement helps us ___.', ['Remember and respect Indigenous history', 'Forget about Indigenous Peoples', 'Ignore the past completely', 'Learn nothing new'], 0),
   ('A land acknowledgement is one way communities show ___.', ['Respect', 'Carelessness', 'Disrespect', 'Confusion'], 0)])

# ─── DAY 92 ─────────────────────────────────────────────────────────────────
d92_lang = sub('Language', 'Contractions: Joining Two Words Into One',
  'Students learn that a contraction joins two words together into a shorter word, using an apostrophe in place of missing letters, such as do not becoming dont and I am becoming Im.',
  [('What do we call a shorter word made by joining two words together, like dont?', ['contraction']),
   ('Join the words do and not together. What contraction do you make?', ['dont']),
   ('Join the words I and am together. What contraction do you make?', ['Im'])],
  [('What is a contraction?', ['A shorter word made by joining two words together', 'A word with no vowels', 'A type of punctuation mark', 'A word that means the opposite'], 0),
   ('Which word is the contraction for do not?', ['Dont', 'Does', 'Doing', 'Did'], 0),
   ('Which word is the contraction for I am?', ['Im', 'Am', 'Are', 'Was'], 0),
   ('Which word is the contraction for cannot?', ['Cant', 'Cane', 'Cans', 'Canned'], 0),
   ('A contraction uses an apostrophe to show that ___.', ['Some letters have been left out', 'Extra letters have been added', 'The word is a question', 'The word is very long'], 0)])

d92_math = sub('Math', 'Doubles Plus One: A Mental Math Strategy',
  'Students learn the doubles plus one strategy, using a known doubles fact like 5 plus 5 to quickly solve a nearby fact like 5 plus 6 by adding one more.',
  [('What is 5 plus 5?', ['10', 'ten']),
   ('Using doubles plus one, what is 5 plus 6?', ['11', 'eleven']),
   ('What double fact helps you solve 6 plus 7?', ['6 plus 6', '6+6'])],
  [('What is 4 plus 4?', ['8', '7', '9', '6'], 0),
   ('Using doubles plus one, what is 4 plus 5?', ['9', '8', '10', '7'], 0),
   ('Which doubles fact helps solve 7 plus 8?', ['7 plus 7', '8 plus 8', '7 plus 6', '9 plus 9'], 0),
   ('The doubles plus one strategy works when two numbers are ___.', ['Right next to each other, like 6 and 7', 'Very far apart', 'Both equal to zero', 'Both equal to ten'], 0),
   ('Using doubles plus one, what is 8 plus 9?', ['17', '16', '18', '15'], 0)])

d92_sci = sub('Science', 'Our Brain: The Bodys Control Centre',
  'Students learn that the brain is the control centre of our body, located inside our head, helping us think, learn, move, and feel.',
  [('What body part is the control centre of our body?', ['brain']),
   ('Where is our brain located?', ['inside our head', 'head']),
   ('Does our brain help us think and learn?', ['yes'])],
  [('What is the brain?', ['The control centre of our body', 'A bone in our arm', 'A part of our foot', 'A type of muscle only'], 0),
   ('Where is the brain located?', ['Inside our head', 'Inside our chest', 'Inside our foot', 'Outside our body'], 0),
   ('Which of these does our brain help us do?', ['Think, learn, and move', 'Only breathe', 'Only digest food', 'Only grow hair'], 0),
   ('Why is the brain an important body part?', ['It controls how our whole body works', 'It has no real job', 'It only helps us smell', 'It only helps us taste'], 0),
   ('Our brain is best described as the bodys ___.', ['Control centre', 'Source of food', 'Source of water', 'Storage for clothes'], 0)])

d92_ss = sub('SocialStudies', 'Levels of Leadership: Mayor, Premier, and Prime Minister',
  'Students learn that Canada has different levels of leadership, with a mayor leading a city or town, a premier leading a province, and a prime minister leading the whole country.',
  [('Who leads a city or town?', ['mayor']),
   ('Who leads a province, like Ontario?', ['premier']),
   ('Who leads the whole country of Canada?', ['prime minister'])],
  [('Who is the leader of a city or town?', ['A mayor', 'A premier', 'A prime minister', 'A principal'], 0),
   ('Who is the leader of a province, like Ontario?', ['A premier', 'A mayor', 'A prime minister', 'A teacher'], 0),
   ('Who is the leader of the whole country of Canada?', ['A prime minister', 'A mayor', 'A premier', 'A librarian'], 0),
   ('Why does Canada have different levels of leadership?', ['To help make decisions for cities, provinces, and the whole country', 'Leaders never make any decisions', 'Only one leader is needed for everything', 'Levels of leadership have no purpose'], 0),
   ('A mayor is most similar to a premier because both ___.', ['Lead and make decisions for the place they represent', 'Have no responsibilities at all', 'Only work at city hall', 'Only work outside Canada'], 0)])

# ─── DAY 93 ─────────────────────────────────────────────────────────────────
d93_lang = sub('Language', 'Root Words: Finding the Base Word Inside',
  'Students learn that a root word, or base word, is the simplest form of a word before prefixes or suffixes are added, such as play inside playing or replay.',
  [('What do we call the simplest form of a word before endings are added?', ['root word', 'base word']),
   ('What is the root word inside the word playing?', ['play']),
   ('What is the root word inside the word jumped?', ['jump'])],
  [('What is a root word?', ['The simplest form of a word before endings are added', 'A word with no meaning', 'A punctuation mark', 'A number word'], 0),
   ('What is the root word inside jumping?', ['Jump', 'Jumping', 'Ing', 'Jum'], 0),
   ('What is the root word inside replay?', ['Play', 'Re', 'Replay', 'Ply'], 0),
   ('What is the root word inside careless?', ['Care', 'Less', 'Careless', 'Car'], 0),
   ('Finding the root word inside a longer word can help readers ___.', ['Understand the meaning of the whole word', 'Forget the meaning of the word', 'Never read the word again', 'Make the word longer'], 0)])

d93_math = sub('Math', 'Data Management: Probability Language - Likely, Unlikely, Certain, and Impossible',
  'Students learn probability words such as likely, unlikely, certain, and impossible to describe how probable it is that something will happen.',
  [('What word describes something that will definitely happen?', ['certain']),
   ('What word describes something that will never happen?', ['impossible']),
   ('Is it likely or unlikely that it will snow in July in Ontario?', ['unlikely'])],
  [('What word describes something that will definitely happen?', ['Certain', 'Impossible', 'Unlikely', 'Maybe'], 0),
   ('What word describes something that can never happen?', ['Impossible', 'Certain', 'Likely', 'Probable'], 0),
   ('Is it likely or unlikely that the sun will rise tomorrow?', ['Likely', 'Unlikely', 'Impossible', 'Certain never'], 0),
   ('Is it likely or unlikely that a cat will fly like a bird?', ['Unlikely', 'Likely', 'Certain', 'It happens every day'], 0),
   ('Probability words help us describe ___.', ['How probable it is that something will happen', 'Only the weather', 'Only the time of day', 'Only numbers to 10'], 0)])

d93_sci = sub('Science', 'Icebergs and Glaciers: Frozen Water',
  'Students learn that glaciers are huge, slow-moving masses of ice, and that icebergs are large chunks of ice that break off glaciers and float in the ocean.',
  [('What do we call a huge, slow-moving mass of ice?', ['glacier']),
   ('What do we call a large chunk of ice floating in the ocean?', ['iceberg']),
   ('Do icebergs break off from glaciers?', ['yes'])],
  [('What is a glacier?', ['A huge, slow-moving mass of ice', 'A type of cloud', 'A kind of desert', 'A warm ocean current'], 0),
   ('What is an iceberg?', ['A large chunk of ice floating in the ocean', 'A type of fish', 'A kind of mountain made of sand', 'A cloud formation'], 0),
   ('Where do icebergs come from?', ['They break off from glaciers', 'They grow from seeds', 'They form from sand', 'They fall from the sun'], 0),
   ('Where would you most likely find glaciers and icebergs?', ['Very cold places on Earth', 'Very hot deserts', 'Inside a volcano', 'In a rainforest'], 0),
   ('Icebergs and glaciers are both made of ___.', ['Frozen water', 'Melted rock', 'Sand and soil', 'Liquid water only'], 0)])

d93_ss = sub('SocialStudies', 'Voting: How Communities Make Decisions Together',
  'Students learn that voting is a way for people in a community to share their opinion and help choose leaders or make decisions together.',
  [('What do we call sharing your choice to help make a decision, like choosing a leader?', ['voting', 'vote']),
   ('Can voting help a community choose its leaders?', ['yes']),
   ('Name one thing a class might vote on, like a class pet or a game.', ['class pet', 'a game', 'a book'])],
  [('What is voting?', ['A way for people to share their choice and help make a decision', 'A way to ignore other peoples opinions', 'A rule about traffic safety', 'A type of food'], 0),
   ('What might a community use voting to help choose?', ['Their leaders', 'The weather', 'The season', 'The time of day'], 0),
   ('Why is voting a fair way to make decisions?', ['It lets everyone share their opinion and be heard', 'Only one person ever gets to decide', 'Voting ignores what most people want', 'Voting has no real purpose'], 0),
   ('Which of these is an example of a class voting together?', ['Choosing a class pet by counting votes', 'One student deciding alone for everyone', 'Ignoring everyones opinion', 'Flipping a coin without asking anyone'], 0),
   ('Voting helps a community make decisions ___.', ['Together, in a fair way', 'Without anyone participating', 'In a way that ignores most people', 'Randomly, with no input'], 0)])

# ─── DAY 94 ─────────────────────────────────────────────────────────────────
d94_lang = sub('Language', 'Alliteration: Repeating Beginning Sounds',
  'Students learn that alliteration is when several words close together start with the same sound, such as in silly snakes slither, which authors use to make writing fun to read.',
  [('What do we call it when several words close together start with the same sound?', ['alliteration']),
   ('In the phrase silly snakes slither, what sound repeats at the beginning of each word?', ['s sound', 's']),
   ('Make up your own short alliteration phrase using words that start with the same sound.', ['big brown bear', 'happy hopping hare', 'tall tiger tiptoes'])],
  [('What is alliteration?', ['When words close together start with the same sound', 'A word that means the opposite of another word', 'A type of punctuation mark', 'A word with no vowels'], 0),
   ('Which phrase is an example of alliteration?', ['Big blue balloons', 'The dog ran fast', 'She likes apples', 'It is a sunny day'], 0),
   ('In the phrase five funny frogs, what sound repeats?', ['The f sound', 'The s sound', 'The b sound', 'The t sound'], 0),
   ('Why might an author use alliteration in a poem?', ['To make the writing fun and interesting to read', 'Alliteration makes writing boring', 'Alliteration is never used in poems', 'It has no effect on how writing sounds'], 0),
   ('Which of these words could join silly snake to make alliteration?', ['Slither', 'Jump', 'Run', 'Hop'], 0)])

d94_math = sub('Math', 'Growing Patterns: Patterns That Get Bigger',
  'Students learn to recognize and extend growing patterns, where each step adds more objects or a larger number than the step before, such as 2, 4, 6, 8.',
  [('In the growing pattern 2, 4, 6, 8, what number comes next?', ['10', 'ten']),
   ('In a growing pattern, does each step usually get bigger or stay the same?', ['bigger']),
   ('Make your own growing pattern starting at 1 and adding 2 each time.', ['1, 3, 5, 7', '1,3,5,7'])],
  [('What is a growing pattern?', ['A pattern where each step gets bigger', 'A pattern that always stays the same', 'A pattern that only uses colours', 'A pattern with no numbers'], 0),
   ('In the growing pattern 1, 2, 3, 4, what comes next?', ['5', '6', '3', '1'], 0),
   ('In the growing pattern 5, 10, 15, 20, what comes next?', ['25', '21', '30', '24'], 0),
   ('Which of these is an example of a growing pattern?', ['3, 6, 9, 12', '5, 5, 5, 5', 'Red, blue, red, blue', '2, 2, 2, 2'], 0),
   ('A growing pattern is different from a repeating pattern because a growing pattern ___.', ['Changes and gets bigger each step', 'Always repeats the exact same steps', 'Never changes at all', 'Only uses shapes'], 0)])

d94_sci = sub('Science', 'Adaptation: How Animals Survive in Their Habitat',
  'Students learn that an adaptation is a special feature or behaviour that helps an animal survive in its habitat, such as thick fur for warmth or sharp claws for digging.',
  [('What do we call a special feature that helps an animal survive?', ['adaptation']),
   ('Name one adaptation that helps an animal stay warm, like thick fur.', ['thick fur', 'fur']),
   ('Do adaptations help animals survive in their habitat?', ['yes'])],
  [('What is an adaptation?', ['A special feature or behaviour that helps an animal survive', 'A type of food animals eat only once', 'A rule animals must follow', 'A place where animals shop'], 0),
   ('Which of these is an example of an adaptation?', ['Thick fur that keeps a polar bear warm', 'A rock sitting still', 'A cloud in the sky', 'A toy in a store'], 0),
   ('Why might a desert animal have large ears?', ['Large ears can help release heat and keep the animal cool', 'Large ears have no purpose at all', 'Large ears only help animals hear music', 'Large ears make animals heavier'], 0),
   ('An adaptation helps an animal do what in its habitat?', ['Survive', 'Disappear completely', 'Become a plant', 'Stop needing food'], 0),
   ('Sharp claws that help an animal dig are an example of a ___.', ['Adaptation', 'Season', 'Weather pattern', 'Rock formation'], 0)])

d94_ss = sub('SocialStudies', 'Classroom Jobs: Helping Our Classroom Run Smoothly',
  'Students learn that classroom jobs, such as line leader or paper passer, give students a responsibility that helps their classroom community run smoothly each day.',
  [('What do we call a job in the classroom, like line leader?', ['classroom job']),
   ('Name one classroom job, like line leader or paper passer.', ['line leader', 'paper passer', 'helper']),
   ('Do classroom jobs help the classroom run smoothly?', ['yes'])],
  [('What is a classroom job?', ['A responsibility that helps the classroom run smoothly', 'A job that pays money', 'A rule about traffic safety', 'A job only adults can do'], 0),
   ('Which of these is an example of a classroom job?', ['Line leader', 'Firefighter', 'Mayor', 'Doctor'], 0),
   ('Why do teachers give students classroom jobs?', ['To help everyone share responsibility for the classroom', 'Classroom jobs have no purpose', 'Only the teacher should ever help', 'Jobs make the classroom messier'], 0),
   ('How is a classroom job similar to a job in the wider community?', ['Both involve a responsibility that helps others', 'They have no similarities at all', 'Classroom jobs pay a salary just like community jobs', 'Community jobs are never real responsibilities'], 0),
   ('Taking turns with classroom jobs teaches students about ___.', ['Responsibility and teamwork', 'Ignoring others', 'Working alone always', 'Avoiding chores'], 0)])

# ─── DAY 95 ─────────────────────────────────────────────────────────────────
d95_lang = sub('Language', 'Text Features: Captions and Diagrams',
  'Students learn that non-fiction books often use captions, short sentences under a picture, and diagrams, labeled drawings, to give readers extra information about a topic.',
  [('What do we call a short sentence written under a picture?', ['caption']),
   ('What do we call a labeled drawing that explains something?', ['diagram']),
   ('Can captions and diagrams give readers extra information about a topic?', ['yes'])],
  [('What is a caption?', ['A short sentence written under a picture', 'A title at the top of a book', 'A number on a page', 'A kind of punctuation mark'], 0),
   ('What is a diagram?', ['A labeled drawing that explains something', 'A made-up story', 'A type of chapter title', 'A book cover'], 0),
   ('Why might a non-fiction book include a diagram of a plant?', ['To show and label the parts of a plant clearly', 'Diagrams never help explain a topic', 'Diagrams are only used in fiction books', 'To confuse the reader on purpose'], 0),
   ('Which of these is an example of a text feature that gives extra information about a picture?', ['A caption', 'A talking dragon', 'A made-up character', 'A fairy godmother'], 0),
   ('Captions and diagrams help readers ___.', ['Understand a topic more clearly', 'Get more confused about a topic', 'Avoid reading the book entirely', 'Skip all of the pictures'], 0)])

d95_math = sub('Math', '3D Shapes: Faces, Edges, and Vertices',
  'Students build on earlier learning about 3D shapes by identifying and counting their faces, edges, and vertices, such as a cube having 6 faces, 12 edges, and 8 vertices.',
  [('What do we call the flat surfaces on a 3D shape?', ['faces']),
   ('What do we call the corners on a 3D shape?', ['vertices', 'corners']),
   ('How many faces does a cube have?', ['6', 'six'])],
  [('What do we call the flat surfaces of a 3D shape?', ['Faces', 'Edges', 'Vertices', 'Corners only'], 0),
   ('What do we call the line where two faces of a 3D shape meet?', ['An edge', 'A vertex', 'A face', 'A curve'], 0),
   ('How many faces does a cube have?', ['6', '4', '8', '12'], 0),
   ('How many vertices does a cube have?', ['8', '6', '12', '4'], 0),
   ('Counting faces, edges, and vertices helps us describe a 3D shapes ___.', ['Attributes', 'Colour only', 'Weight', 'Smell'], 0)])

d95_sci = sub('Science', 'Dinosaurs: Animals from Long Ago',
  'Students learn that dinosaurs were animals that lived on Earth a very long time ago, and that scientists learn about them by studying fossils found in rock.',
  [('What word describes animals that lived on Earth a very long time ago, like dinosaurs?', ['dinosaurs']),
   ('What do scientists study to learn about dinosaurs?', ['fossils']),
   ('Are dinosaurs alive on Earth today?', ['no'])],
  [('What were dinosaurs?', ['Animals that lived on Earth a very long time ago', 'Animals that live in cities today', 'A type of plant', 'A kind of cloud'], 0),
   ('How do scientists learn about dinosaurs?', ['By studying fossils found in rock', 'By asking dinosaurs directly', 'Dinosaurs are impossible to study', 'By watching dinosaurs on farms'], 0),
   ('Are dinosaurs alive on Earth today?', ['No, they lived long ago', 'Yes, they live in oceans', 'Yes, they live in deserts', 'Yes, they live in cities'], 0),
   ('What is a fossil?', ['A trace or remains of a living thing from long ago, preserved in rock', 'A type of modern toy', 'A kind of cloud', 'A living dinosaur'], 0),
   ('Learning about dinosaurs helps scientists understand ___.', ['What life on Earth was like long ago', 'What the weather will be tomorrow', 'How to build houses', 'How to cook food'], 0)])

d95_ss = sub('SocialStudies', 'Public Signs and Symbols: Understanding Signs Around Us',
  'Students learn that public signs and symbols, such as a stop sign or a washroom symbol, use shapes, colours, and pictures to share important information quickly.',
  [('What shape is a stop sign?', ['octagon', 'eight-sided shape']),
   ('What colour is a stop sign?', ['red']),
   ('Why do public signs often use pictures instead of only words?', ['so everyone can understand quickly', 'pictures are easy to understand'])],
  [('What is a public sign?', ['A sign that shares important information using shapes, colours, or pictures', 'A private note between friends', 'A type of story', 'A kind of song'], 0),
   ('What shape is a stop sign?', ['An octagon, with eight sides', 'A circle', 'A square', 'A triangle'], 0),
   ('What colour is a stop sign?', ['Red', 'Blue', 'Green', 'Yellow'], 0),
   ('Why do many signs use pictures instead of only words?', ['So people who speak different languages can understand them quickly', 'Pictures make signs harder to understand', 'Words are always better than pictures', 'Signs never need to be understood quickly'], 0),
   ('Public signs and symbols help keep communities ___.', ['Safe and informed', 'Confused', 'Unsafe', 'Uninformed'], 0)])

# ─── DAY 96 ─────────────────────────────────────────────────────────────────
d96_lang = sub('Language', 'Persuasive Writing: Convincing Someone With Words',
  'Students learn that persuasive writing tries to convince a reader to agree with an idea or take an action, using reasons that support the writers opinion.',
  [('What kind of writing tries to convince a reader to agree with an idea?', ['persuasive writing', 'persuasive']),
   ('Name one reason you might give to persuade someone to get a class pet.', ['it teaches responsibility', 'pets are fun', 'it teaches caring']),
   ('Should persuasive writing include reasons that support the writers opinion?', ['yes'])],
  [('What is persuasive writing?', ['Writing that tries to convince a reader to agree with an idea', 'Writing that only tells a made-up story', 'Writing with no opinions at all', 'Writing that only lists facts with no reasons'], 0),
   ('Which sentence is an example of persuasive writing?', ['Our class should get a pet because it teaches responsibility', 'The sky is blue', 'A dog has four legs', 'Water is wet'], 0),
   ('Why do writers include reasons in persuasive writing?', ['To support their opinion and convince the reader', 'Reasons are never needed in persuasive writing', 'Reasons make an argument weaker', 'Persuasive writing never has an opinion'], 0),
   ('Which of these might you find in a persuasive letter asking for a class trip to the zoo?', ['Reasons why the trip would be fun and educational', 'A made-up fairy tale', 'A list of random numbers', 'A drawing with no words'], 0),
   ('Persuasive writing is meant to ___.', ['Convince the reader to agree with an idea', 'Confuse the reader completely', 'Only entertain with silly jokes', 'Share facts with no opinions at all'], 0)])

d96_math = sub('Math', 'Fractions: Sharing a Group of Objects Equally',
  'Students learn to find halves and quarters of a group of objects, such as sharing 8 counters equally between 2 people so that each person gets an equal share.',
  [('If you share 8 counters equally between 2 people, how many does each person get?', ['4', 'four']),
   ('If you share 12 counters equally between 2 people, how many does each person get?', ['6', 'six']),
   ('Why must each share be equal when finding half of a group?', ['so it is fair', 'so each person gets the same amount'])],
  [('If you share 6 counters equally between 2 people, how many does each person get?', ['3', '2', '4', '6'], 0),
   ('If you share 10 counters equally between 2 people, how many does each person get?', ['5', '4', '6', '10'], 0),
   ('If you share 8 counters equally among 4 people, how many does each person get?', ['2', '4', '8', '1'], 0),
   ('When sharing a group of objects to find half, each share must be ___.', ['Equal', 'Different sizes', 'As big as possible for one person', 'Ignored'], 0),
   ('Sharing 12 apples equally between 2 friends is the same as finding ___ of 12.', ['Half', 'A quarter', 'A third', 'Double'], 0)])

d96_sci = sub('Science', 'Static Electricity: Why Balloons Stick to Walls',
  'Students learn that rubbing certain objects together, like a balloon on hair, can create static electricity, a tiny electric charge that can make objects stick together or attract.',
  [('What do we call the tiny electric charge made when you rub a balloon on your hair?', ['static electricity']),
   ('Can static electricity make a balloon stick to a wall?', ['yes']),
   ('What did you rub the balloon on to create static electricity, like hair?', ['hair'])],
  [('What is static electricity?', ['A tiny electric charge made by rubbing certain objects together', 'A type of weather', 'A kind of plant', 'A sound animals make'], 0),
   ('What might happen if you rub a balloon on your hair and hold it near a wall?', ['The balloon might stick to the wall', 'The balloon will disappear', 'The wall will change colour', 'Nothing can ever happen'], 0),
   ('Static electricity is created by ___.', ['Rubbing certain objects together', 'Freezing water', 'Boiling water', 'Planting seeds'], 0),
   ('Which of these might you notice because of static electricity?', ['Your hair standing up after rubbing a balloon on it', 'A plant growing taller', 'A rock changing colour', 'Water freezing into ice'], 0),
   ('Static electricity is an example of a topic scientists study called ___.', ['Energy', 'Weather', 'Animal habitats', 'Plant growth'], 0)])

d96_ss = sub('SocialStudies', 'Thanksgiving in Canada: A Time to Give Thanks',
  'Students learn that Thanksgiving is a Canadian holiday in October when families gather to give thanks for the harvest and for the good things in their lives.',
  [('What Canadian holiday in October is a time to give thanks?', ['Thanksgiving']),
   ('Do families often gather together on Thanksgiving?', ['yes']),
   ('Name one thing you might feel thankful for.', ['family', 'food', 'friends', 'home'])],
  [('What is Thanksgiving?', ['A Canadian holiday when people give thanks for the harvest and good things in life', 'A holiday only celebrated in the summer', 'A rule about traffic safety', 'A type of school subject'], 0),
   ('In what month is Thanksgiving celebrated in Canada?', ['October', 'December', 'July', 'February'], 0),
   ('What do many families do together on Thanksgiving?', ['Gather and share a meal together', 'Ignore each other completely', 'Go to school', 'Stay apart from each other'], 0),
   ('Why might people give thanks on Thanksgiving?', ['To appreciate the good things in their lives, like family and food', 'Giving thanks has no meaning at all', 'Thanksgiving has nothing to do with gratitude', 'People never give thanks on this holiday'], 0),
   ('Thanksgiving is an example of a Canadian ___.', ['Holiday and tradition', 'Rule about safety', 'Type of currency', 'Kind of building'], 0)])

# ─── DAY 97 ─────────────────────────────────────────────────────────────────
d97_lang = sub('Language', 'Story Endings: Writing a New Ending for a Tale',
  'Students practise writing a new ending for a familiar story, using their imagination to change what happens after the storys problem while keeping the characters and setting the same.',
  [('What part of a story can you change when you write a new ending?', ['what happens after the problem', 'the ending']),
   ('Should the characters usually stay the same when you write a new ending?', ['yes']),
   ('Write one new ending idea for a story about a lost puppy finding its way home.', ['the puppy finds a new friend', 'the puppy is rescued by a kind stranger', 'the puppy finds its way home a different way'])],
  [('What does it mean to write a new ending for a story?', ['To imagine and write a different way the story could finish', 'To copy the original ending exactly', 'To change the beginning of the story only', 'To remove the characters completely'], 0),
   ('When writing a new ending, what usually stays the same?', ['The characters and setting', 'The entire plot from the beginning', 'Nothing at all', 'The title of a different book'], 0),
   ('Which of these is an example of writing a new ending?', ['Imagining the lost puppy finds a new friend instead of going home', 'Copying the story word for word', 'Reading the story silently', 'Drawing the book cover'], 0),
   ('Why is writing a new ending a useful creative writing skill?', ['It lets writers use their imagination and understand story structure', 'New endings are never useful to practise', 'Writers should never imagine different outcomes', 'This concept has no connection to writing'], 0),
   ('Writing a new story ending is an example of ___ writing.', ['Creative', 'Persuasive only', 'Instructional', 'Factual only'], 0)])

d97_math = sub('Math', 'Money: Trading Coins for Equal Value',
  'Students learn that coins of different values can be traded for an equal amount, such as trading 5 pennies for 1 nickel or 2 nickels for 1 dime.',
  [('How many pennies can be traded for 1 nickel?', ['5', 'five']),
   ('How many nickels can be traded for 1 dime?', ['2', 'two']),
   ('If you trade 10 pennies, how many dimes worth of value do you have?', ['1', 'one'])],
  [('How many pennies equal the value of 1 nickel?', ['5', '10', '2', '1'], 0),
   ('How many nickels equal the value of 1 dime?', ['2', '5', '10', '1'], 0),
   ('How many pennies equal the value of 1 dime?', ['10', '5', '2', '1'], 0),
   ('Trading coins for equal value means the coins ___.', ['Are worth the same amount even though they look different', 'Always look exactly the same', 'Have no value at all', 'Cannot ever be exchanged'], 0),
   ('Why is it useful to know that coins can be traded for equal value?', ['It helps us understand different ways to make the same amount of money', 'Trading coins never helps with money skills', 'Coins can never equal the same value', 'This concept has no connection to money'], 0)])

d97_sci = sub('Science', 'Our Muscles: Helping Us Move and Stay Strong',
  'Students learn that muscles are body parts that stretch and squeeze to help us move, working together with our bones to let us run, jump, and lift things.',
  [('What body parts stretch and squeeze to help us move?', ['muscles']),
   ('Do muscles work together with our bones to help us move?', ['yes']),
   ('Name one activity that uses your muscles, like running or jumping.', ['running', 'jumping', 'lifting'])],
  [('What are muscles?', ['Body parts that stretch and squeeze to help us move', 'Bones that support our body', 'Parts of our brain', 'A type of food'], 0),
   ('What do muscles work together with to help us move?', ['Our bones', 'Our hair', 'Our nails', 'Our teeth'], 0),
   ('Which of these activities uses your muscles?', ['Running and jumping', 'Sleeping only', 'Sitting completely still', 'Thinking quietly'], 0),
   ('Why is it important to exercise our muscles?', ['It helps keep our muscles strong and healthy', 'Exercise weakens our muscles', 'Muscles never need exercise', 'This concept has no connection to health'], 0),
   ('Our muscles are best described as body parts that help us ___.', ['Move and stay strong', 'Taste food', 'Hear sounds', 'See colours'], 0)])

d97_ss = sub('SocialStudies', 'Remembrance Day: Honouring Those Who Served',
  'Students learn that Remembrance Day, on November 11, is a day when Canadians wear a poppy and take a moment of silence to honour those who served in the military.',
  [('On what date is Remembrance Day observed in Canada?', ['November 11', 'Nov 11']),
   ('What flower do people often wear to honour Remembrance Day?', ['poppy']),
   ('Do Canadians take a moment of silence on Remembrance Day?', ['yes'])],
  [('What is Remembrance Day?', ['A day to honour those who served in the military', 'A day to celebrate a birthday', 'A rule about traffic safety', 'A type of school subject'], 0),
   ('On what date is Remembrance Day observed?', ['November 11', 'July 1', 'October 12', 'December 25'], 0),
   ('What flower do people often wear on Remembrance Day?', ['A poppy', 'A rose', 'A tulip', 'A sunflower'], 0),
   ('What do many Canadians do at 11 oclock on Remembrance Day?', ['Take a moment of silence', 'Have a large parade with loud music', 'Go to school as usual with no changes', 'Ignore the day completely'], 0),
   ('Remembrance Day helps Canadians ___.', ['Honour and remember those who served', 'Forget about the past', 'Ignore Canadian history', 'Celebrate a harvest'], 0)])

# ─── DAY 98 ─────────────────────────────────────────────────────────────────
d98_lang = sub('Language', 'Nonsense Words: Practising Phonics Skills',
  'Students practise decoding nonsense words, made-up words that follow real spelling patterns, such as zin or plob, to strengthen their phonics skills without relying on word memory.',
  [('What do we call a made-up word that follows real spelling patterns, like zin?', ['nonsense word']),
   ('Can sounding out a nonsense word help you practise phonics skills?', ['yes']),
   ('Make up your own nonsense word using the -at family pattern.', ['zat', 'plat', 'frat'])],
  [('What is a nonsense word?', ['A made-up word that follows real spelling patterns', 'A real word with a meaning', 'A punctuation mark', 'A type of sentence'], 0),
   ('Why do readers practise sounding out nonsense words?', ['To strengthen phonics skills without relying on memory', 'Nonsense words are never useful to practise', 'Nonsense words have real meanings to memorize', 'This concept has no connection to reading'], 0),
   ('Which of these is an example of a nonsense word?', ['Zop', 'Cat', 'Dog', 'Sun'], 0),
   ('When sounding out the nonsense word plim, which sound comes first?', ['The pl sound', 'The m sound', 'The i sound', 'The silent e sound'], 0),
   ('Practising nonsense words helps readers focus on ___.', ['Sounding out letters and patterns, not memorized meaning', 'Only memorizing whole words', 'Ignoring letter sounds completely', 'Skipping every unfamiliar word'], 0)])

d98_math = sub('Math', 'Measuring Mass: Heavier, Lighter, and Balancing',
  'Students use a balance scale to compare the mass of two objects, learning that the side that tips down holds the object with greater mass, or is heavier.',
  [('What tool can help you compare the mass of two objects?', ['balance scale', 'scale']),
   ('On a balance scale, does the heavier object tip down or up?', ['down']),
   ('If two objects balance evenly, are they the same mass or different mass?', ['same mass', 'the same'])],
  [('What tool can be used to compare the mass of two objects?', ['A balance scale', 'A ruler', 'A clock', 'A thermometer'], 0),
   ('On a balance scale, what happens to the side with the heavier object?', ['It tips down', 'It tips up', 'It stays perfectly still', 'It disappears'], 0),
   ('If a balance scale is level with an object on each side, what does that tell us?', ['Both objects have the same mass', 'One object is much heavier', 'One object is much lighter', 'The scale is broken'], 0),
   ('Which of these words describes an object with more mass than another?', ['Heavier', 'Lighter', 'Shorter', 'Longer'], 0),
   ('Using a balance scale helps us compare ___.', ['Mass', 'Colour', 'Sound', 'Time'], 0)])

d98_sci = sub('Science', 'Water Conservation: Saving Our Water',
  'Students learn simple ways to conserve water, such as turning off the tap while brushing teeth, to help protect this important resource for people, plants, and animals.',
  [('What word describes using less water and protecting it, like turning off a tap?', ['water conservation', 'conservation']),
   ('Name one way to save water, like turning off the tap while brushing teeth.', ['turning off the tap', 'turn off the tap']),
   ('Do people, plants, and animals all need water?', ['yes'])],
  [('What is water conservation?', ['Using water carefully and saving it for the future', 'Wasting as much water as possible', 'A type of ocean animal', 'A kind of weather'], 0),
   ('Which of these is a way to save water?', ['Turning off the tap while brushing your teeth', 'Leaving the tap running all day', 'Filling a pool every single day', 'Watering a garden during a rainstorm'], 0),
   ('Why is it important to save water?', ['Water is an important resource that people, plants, and animals need', 'Water is not important at all', 'We will never run out of water anywhere', 'Saving water has no benefit'], 0),
   ('Which of these living things need water to survive?', ['People, plants, and animals', 'Only people', 'Only plants', 'Nothing needs water'], 0),
   ('Turning off the tap while brushing your teeth is an example of ___.', ['Water conservation', 'Wasting water', 'Water pollution', 'Ignoring the environment'], 0)])

d98_ss = sub('SocialStudies', 'Money From Around the World: Comparing Currencies',
  'Students learn that different countries use different money, called currency, such as the Canadian dollar in Canada and the US dollar in the United States.',
  [('What word describes the money used in a country?', ['currency']),
   ('What is the name of the currency used in Canada?', ['Canadian dollar', 'dollar']),
   ('Do different countries often use different currencies?', ['yes'])],
  [('What is currency?', ['The money used in a country', 'A type of food', 'A rule about traffic safety', 'A kind of building'], 0),
   ('What is the name of the currency used in Canada?', ['The Canadian dollar', 'The euro', 'The yen', 'The peso'], 0),
   ('Do all countries use the exact same currency?', ['No, different countries often use different currencies', 'Yes, every country uses the same money', 'Only Canada has currency', 'Money is the same everywhere'], 0),
   ('Why might a traveller need to exchange their money when visiting another country?', ['Because different countries use different currencies', 'Money never needs to be exchanged', 'All countries accept only Canadian dollars', 'Currency has no connection to travel'], 0),
   ('Comparing currencies from different countries helps us understand that the world has ___.', ['Many different countries with their own money', 'Only one type of money everywhere', 'No connection between countries', 'No difference between countries at all'], 0)])

# ─── DAY 99 ─────────────────────────────────────────────────────────────────
d99_lang = sub('Language', 'Point of View: Whose Story Is It?',
  'Students learn that point of view describes who is telling a story, and that a story can be told from a characters point of view using words like I and me.',
  [('What word describes who is telling a story?', ['point of view']),
   ('If a story uses the words I and me, whose point of view is it likely told from?', ['a characters', 'the characters']),
   ('Can two characters in the same story have different points of view?', ['yes'])],
  [('What is point of view?', ['Who is telling a story', 'The title of a book', 'The setting of a story', 'The number of pages in a book'], 0),
   ('If a story uses the words I and me, it is likely told from ___.', ['A characters point of view', 'No point of view at all', 'The readers point of view only', 'A random strangers point of view'], 0),
   ('Why might two characters in the same story see events differently?', ['Each character has their own point of view and feelings', 'All characters always think exactly the same way', 'Point of view never changes how a story feels', 'Characters never have their own feelings'], 0),
   ('Thinking about point of view helps readers understand ___.', ['How a character feels about the story events', 'Only the page numbers', 'Only the cover of the book', 'Nothing about the story'], 0),
   ('Which of these might change depending on a storys point of view?', ['How events in the story are described', 'The title of the book only', 'The colour of the cover', 'The number of chapters'], 0)])

d99_math = sub('Math', 'Addition and Subtraction: Choosing the Best Strategy',
  'Students review addition and subtraction strategies, such as counting on, making ten, doubles, and counting back, and practise choosing the strategy that works best for a given problem.',
  [('Name one addition strategy you have learned, like making ten or doubles.', ['making ten', 'doubles', 'counting on']),
   ('Name one subtraction strategy you have learned, like counting back.', ['counting back']),
   ('Which strategy would work well for solving 9 plus 9?', ['doubles'])],
  [('Which strategy works well for solving 8 plus 8?', ['Doubles', 'Counting back', 'Skip counting by 10s', 'None of these'], 0),
   ('Which strategy works well for solving 9 plus 4?', ['Making ten', 'Doubling only', 'Counting by 5s', 'Measuring'], 0),
   ('Which strategy works well for solving 10 minus 3?', ['Counting back', 'Making ten', 'Doubles', 'Skip counting by 10s'], 0),
   ('Why is it helpful to know more than one addition or subtraction strategy?', ['Different problems can be solved more easily with different strategies', 'Only one strategy ever works for every problem', 'Strategies never help solve problems', 'Knowing strategies has no benefit'], 0),
   ('Choosing the best strategy for a problem means picking the one that ___.', ['Makes the problem easiest to solve', 'Takes the longest amount of time', 'Is always the same no matter the problem', 'Has nothing to do with the numbers involved'], 0)])

d99_sci = sub('Science', 'Sound Vibrations: How Sound Travels',
  'Students build on earlier learning about sound by exploring how sound is made by vibrations, tiny fast back and forth movements, that travel through air to our ears.',
  [('What do we call the tiny fast back and forth movements that make sound?', ['vibrations']),
   ('Do vibrations travel through air to reach our ears?', ['yes']),
   ('If you pluck a guitar string, can you sometimes feel it vibrate?', ['yes'])],
  [('What makes sound?', ['Vibrations', 'Sunlight', 'Cold air only', 'Water freezing'], 0),
   ('What are vibrations?', ['Tiny fast back and forth movements', 'A type of cloud', 'A kind of rock', 'A colour of light'], 0),
   ('How does sound travel to our ears?', ['It travels through the air as vibrations', 'It travels through solid rock only', 'Sound cannot travel at all', 'It travels through sunlight'], 0),
   ('If you pluck a guitar string, what might you feel?', ['The string vibrating', 'The string turning into liquid', 'The string disappearing', 'Nothing at all'], 0),
   ('Understanding vibrations helps us understand how ___.', ['Sound is made and how it travels', 'Plants grow', 'Rocks form', 'Water freezes'], 0)])

d99_ss = sub('SocialStudies', 'Recycling, Reusing, and Reducing: The Three Rs',
  'Students learn the three Rs, reduce, reuse, and recycle, as three ways people in a community can help take care of the environment and produce less waste.',
  [('Name the three Rs that help take care of the environment.', ['reduce, reuse, recycle', 'reduce reuse recycle']),
   ('What does it mean to reuse something?', ['use it again', 'use again']),
   ('Do the three Rs help produce less waste?', ['yes'])],
  [('What are the three Rs?', ['Reduce, reuse, and recycle', 'Read, write, and run', 'Rest, relax, and repeat', 'Run, ride, and roll'], 0),
   ('What does it mean to reduce?', ['To use less of something', 'To throw everything away', 'To use something one time only', 'To ignore the environment'], 0),
   ('What does it mean to reuse something?', ['To use it again instead of throwing it away', 'To throw it away immediately', 'To buy a brand new one every time', 'To ignore it completely'], 0),
   ('Which of these is an example of recycling?', ['Putting a used paper in a recycling bin to be made into new paper', 'Throwing a can into the garbage', 'Leaving litter on the ground', 'Wasting water'], 0),
   ('Practising the three Rs helps a community ___.', ['Produce less waste and care for the environment', 'Produce more waste', 'Harm the environment', 'Ignore environmental care'], 0)])

# ─── DAY 100 (Review) ───────────────────────────────────────────────────────
d100_lang = sub('Language', 'Language Review: Vowel Teams, Word Parts, and Story Craft',
  'Students review recent Language skills: the ie and igh vowel teams, contractions, root words, alliteration, text features, persuasive writing, story endings, nonsense words, and point of view.',
  [('Does the igh in night make the long i sound or the short i sound?', ['long i sound', 'long i']),
   ('What do we call a shorter word made by joining two words together, like dont?', ['contraction']),
   ('What do we call the simplest form of a word before endings are added?', ['root word', 'base word'])],
  [('Which word has the long i sound spelled ie?', ['Pie', 'Pit', 'Pin', 'Sit'], 0),
   ('What is a contraction?', ['A shorter word made by joining two words together', 'A word with no vowels', 'A type of punctuation mark', 'A word that means the opposite'], 0),
   ('What is alliteration?', ['When words close together start with the same sound', 'A word that means the opposite of another word', 'A type of punctuation mark', 'A word with no vowels'], 0),
   ('What is persuasive writing?', ['Writing that tries to convince a reader to agree with an idea', 'Writing that only tells a made-up story', 'Writing with no opinions at all', 'Writing that only lists facts with no reasons'], 0),
   ('What is point of view?', ['Who is telling a story', 'The title of a book', 'The setting of a story', 'The number of pages in a book'], 0)])

d100_math = sub('Math', 'Math Review: Numbers, Patterns, and Strategies',
  'Students review recent Math skills: numbers to 200, doubles plus one, probability language, growing patterns, 3D shape attributes, fractions of a group, trading coins, measuring mass, and choosing addition and subtraction strategies.',
  [('What number comes right after 169?', ['170', 'one hundred seventy']),
   ('What is 5 plus 5?', ['10', 'ten']),
   ('What word describes something that will definitely happen?', ['certain'])],
  [('What number comes right after 159?', ['160', '161', '150', '169'], 0),
   ('What word describes something that will definitely happen?', ['Certain', 'Impossible', 'Unlikely', 'Maybe'], 0),
   ('How many faces does a cube have?', ['6', '4', '8', '12'], 0),
   ('How many pennies equal the value of 1 nickel?', ['5', '10', '2', '1'], 0),
   ('Which strategy works well for solving 8 plus 8?', ['Doubles', 'Counting back', 'Skip counting by 10s', 'None of these'], 0)])

d100_sci = sub('Science', 'Science Review: Our Bodies, Earth, and Energy',
  'Students review recent Science topics: our heart, our brain, icebergs and glaciers, animal adaptation, dinosaurs, static electricity, our muscles, water conservation, and sound vibrations.',
  [('What body part pumps blood through our body?', ['heart']),
   ('What body part is the control centre of our body?', ['brain']),
   ('What do we call a special feature that helps an animal survive?', ['adaptation'])],
  [('What is the heart?', ['A strong muscle that pumps blood', 'A bone in our leg', 'A part of our ear', 'A type of food'], 0),
   ('What is a glacier?', ['A huge, slow-moving mass of ice', 'A type of cloud', 'A kind of desert', 'A warm ocean current'], 0),
   ('What were dinosaurs?', ['Animals that lived on Earth a very long time ago', 'Animals that live in cities today', 'A type of plant', 'A kind of cloud'], 0),
   ('What are muscles?', ['Body parts that stretch and squeeze to help us move', 'Bones that support our body', 'Parts of our brain', 'A type of food'], 0),
   ('What makes sound?', ['Vibrations', 'Sunlight', 'Cold air only', 'Water freezing'], 0)])

d100_ss = sub('SocialStudies', 'Social Studies Review: Leadership, Traditions, and Caring for Our World',
  'Students review recent Social Studies topics: land acknowledgements, levels of leadership, voting, classroom jobs, public signs, Thanksgiving, Remembrance Day, currencies around the world, and the three Rs.',
  [('What do we call a statement that recognizes the Indigenous Peoples connected to a land?', ['land acknowledgement']),
   ('Who leads a city or town?', ['mayor']),
   ('What are the three Rs that help take care of the environment?', ['reduce, reuse, recycle', 'reduce reuse recycle'])],
  [('What is a land acknowledgement?', ['A statement that recognizes Indigenous Peoples connected to the land', 'A rule about traffic safety', 'A kind of food', 'A type of building'], 0),
   ('Who is the leader of a city or town?', ['A mayor', 'A premier', 'A prime minister', 'A principal'], 0),
   ('What is voting?', ['A way for people to share their choice and help make a decision', 'A way to ignore other peoples opinions', 'A rule about traffic safety', 'A type of food'], 0),
   ('What is Thanksgiving?', ['A Canadian holiday when people give thanks for the harvest and good things in life', 'A holiday only celebrated in the summer', 'A rule about traffic safety', 'A type of school subject'], 0),
   ('What are the three Rs?', ['Reduce, reuse, and recycle', 'Read, write, and run', 'Rest, relax, and repeat', 'Run, ride, and roll'], 0)])


g1_91_100 = [
    day(91, [d91_lang, d91_math, d91_sci, d91_ss]),
    day(92, [d92_lang, d92_math, d92_sci, d92_ss]),
    day(93, [d93_lang, d93_math, d93_sci, d93_ss]),
    day(94, [d94_lang, d94_math, d94_sci, d94_ss]),
    day(95, [d95_lang, d95_math, d95_sci, d95_ss]),
    day(96, [d96_lang, d96_math, d96_sci, d96_ss]),
    day(97, [d97_lang, d97_math, d97_sci, d97_ss]),
    day(98, [d98_lang, d98_math, d98_sci, d98_ss]),
    day(99, [d99_lang, d99_math, d99_sci, d99_ss]),
    day(100, [d100_lang, d100_math, d100_sci, d100_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_91_100)
    append_worksheet_days(1, g1_91_100)
