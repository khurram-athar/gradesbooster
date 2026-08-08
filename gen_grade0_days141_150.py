#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 141-150 -- twelfth batch, extending Grade 0
past Day 140. Self-contained script (does NOT use gen_curriculum.py's
sub()/day()/append_to(), since those do not support a worksheet field)
modeled exactly on gen_grade0_days131_140.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-140 (dumped
and checked against data/grade0.json before writing): word families -ell,
-ill; prefixes re-; suffixes -ful; homophones; contractions; dialogue;
sequencing events with pictures; question words why and how for Language.
Near doubles, number bonds to 11, digital clocks, comparing volume,
dimes and quarters, composing pictures with shapes, skip counting by twos
on a number line, estimating quantities, tens and ones blocks for Math.
Ladybug life cycle, beavers, bread making, recycling symbols, immune
system, simple circuits, animal tracks, camels, icebergs for Science.
Lifeguards, electricians, world currency, town hall, welcoming new
students, Canadian inventions, recycling truck drivers, provincial and
territorial flags, world landmarks for Social Studies. Day 150 is a
review day across all four subjects, matching the end-of-batch pattern
used in every prior batch. No embedded ASCII double-quote or straight
apostrophe characters are used anywhere in title/summary/quiz/worksheet
text -- contractions and possessives are avoided entirely, matching this
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


def _rebalance_answer_positions(days, seed=20260807):
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


g0_141_150 = [
day(141, [
L('Word Families: -ell Words',
  'Kindergarten Language strand: the -ell word family shares the same ending sound, as in bell, sell, tell, and shell.',
  [('Name a word that rhymes with bell.', ['sell', 'tell', 'shell']),
   ('What ending sound do sell and tell share?', ['ell', 'the ell sound']),
   ('Is smell part of the -ell family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ell family?', ['Cat', 'Bell', 'Sun', 'Top'], 1),
   ('Which word rhymes with shell?', ['Sit', 'Bell', 'Sock', 'Sad'], 1),
   ('Which word does NOT belong to the -ell family?', ['Bell', 'Sell', 'Tell', 'Ball'], 3),
   ('Complete the rhyme: I found a pretty seashell by the ___.', ['well', 'wall', 'wool', 'will'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('Doubles Minus One: Near Doubles',
  'Kindergarten Math strand: students learn that a near double, like 5 plus 4, is close to a double fact, like 5 plus 5, but one less.',
  [('What is 5 plus 5?', ['10', 'ten']),
   ('What is 5 plus 4?', ['9', 'nine']),
   ('How does knowing a double help with a near double?', ['it is one less than the double', 'take one away from the double']),
   ],
  [('If 6 + 6 = 12, what is 6 + 5?', ['10', '11', '12', '13'], 1),
   ('If 4 + 4 = 8, what is 4 + 3?', ['5', '6', '7', '8'], 2),
   ('A near double is a fact that is close to a ___.', ['Subtraction fact', 'Double fact', 'Number word', 'Shape'], 1),
   ('What is 7 + 6 if you know 7 + 7 = 14?', ['12', '13', '14', '15'], 1),
   ('Knowing doubles can help us solve ___ faster.', ['Near doubles', 'Shapes', 'Colours', 'Letters'], 0)]),
Sc('Life Cycle of a Ladybug',
   'Kindergarten Science strand: a ladybug begins life as a tiny egg, hatches into a larva, forms a pupa, and becomes an adult ladybug with spotted wings.',
   [('What is the first stage of a ladybugs life?', ['egg', 'an egg']),
    ('What comes after the egg stage?', ['larva', 'a larva']),
    ('What does an adult ladybug look like?', ['it has spotted wings', 'small with spots'])],
   [('What is the first stage of a ladybugs life cycle?', ['Egg', 'Larva', 'Pupa', 'Adult'], 0),
    ('What stage comes right after the egg?', ['Adult', 'Larva', 'Pupa', 'Cocoon'], 1),
    ('What is special about an adult ladybugs wings?', ['They often have spots', 'They are always plain white', 'They cannot fly', 'They have no colour'], 0),
    ('Which stage comes right before an adult ladybug?', ['Egg', 'Larva', 'Pupa', 'Nothing'], 2),
    ('A ladybug life cycle has how many main stages?', ['2', '3', '4', '5'], 2)]),
SS('Our Lifeguards: Keeping Us Safe at the Pool',
   'Kindergarten Social Studies strand: lifeguards watch over swimmers at pools and beaches, ready to help keep everyone safe in the water.',
   [('What does a lifeguard do?', ['keeps swimmers safe', 'watches over the water']),
    ('Where might you see a lifeguard working?', ['a pool', 'a beach']),
    ('Why is it important to listen to a lifeguard?', ['they help keep us safe', 'they watch for danger'])],
   [('What is the main job of a lifeguard?', ['Keeping swimmers safe in the water', 'Teaching math', 'Cooking food', 'Driving a bus'], 0),
    ('Where might a lifeguard work?', ['At a pool or beach', 'In a library', 'In a classroom', 'In outer space'], 0),
    ('Why should swimmers listen to a lifeguards instructions?', ['To stay safe in and around the water', 'Lifeguards have no important job', 'It does not matter what they say', 'Only to be polite'], 0),
    ('A lifeguard watches the water closely to ___.', ['Spot anyone who needs help', 'Count the waves', 'Sell tickets', 'Clean the pool deck only'], 0),
    ('Which tool might a lifeguard use to help a swimmer?', ['A rescue float or buoy', 'A cooking pot', 'A paintbrush', 'A telescope'], 0)]),
]),
day(142, [
L('Word Families: -ill Words',
  'Kindergarten Language strand: the -ill word family shares the same ending sound, as in hill, fill, will, and spill.',
  [('Name a word that rhymes with hill.', ['fill', 'will', 'spill']),
   ('What ending sound do fill and will share?', ['ill', 'the ill sound']),
   ('Is drill part of the -ill family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ill family?', ['Dog', 'Hill', 'Cup', 'Bed'], 1),
   ('Which word rhymes with spill?', ['Fill', 'Sit', 'Sun', 'Cap'], 0),
   ('Which word does NOT belong to the -ill family?', ['Hill', 'Fill', 'Will', 'Wall'], 3),
   ('Complete the rhyme: I like to run up and down the ___.', ['hill', 'hall', 'hull', 'hell'], 0),
   ('Recognizing word families helps us read new words that share the same ___.', ['Meaning', 'Ending sound', 'Colour', 'Number of letters'], 1)]),
M('Number Bonds: Ways to Make 11',
  'Kindergarten Math strand: students find different pairs of numbers that add together to make 11, such as 6 and 5, or 8 and 3.',
  [('Name two numbers that add up to 11.', ['6 and 5', '8 and 3']),
   ('What is 9 plus 2?', ['11', 'eleven']),
   ('How many ways can you make 11 with two numbers?', ['many ways', 'several ways'])],
  [('Which pair of numbers makes 11?', ['4 and 5', '6 and 5', '3 and 3', '2 and 2'], 1),
   ('What is 9 + 2?', ['9', '10', '11', '12'], 2),
   ('What is 7 + 4?', ['9', '10', '11', '12'], 2),
   ('If one part of 11 is 8, the other part is ___.', ['2', '3', '4', '5'], 1),
   ('Number bonds show us different ways to make the same ___.', ['Colour', 'Total', 'Shape', 'Letter'], 1)]),
Sc('Beavers: Canadas National Animal',
   'Kindergarten Science strand: the beaver is Canadas national animal, known for its flat tail and strong teeth that it uses to cut down trees and build dams.',
   [('What is Canadas national animal?', ['the beaver', 'beaver']),
    ('What body part helps a beaver cut down trees?', ['its teeth', 'strong teeth']),
    ('What does a beaver build with the trees it cuts?', ['a dam', 'dams and lodges'])],
   [('What animal is the national animal of Canada?', ['The beaver', 'The moose', 'The polar bear', 'The loon'], 0),
    ('What does a beaver use to cut down trees?', ['Its strong front teeth', 'Its tail', 'Its claws only', 'Its nose'], 0),
    ('What does a beaver build using cut trees and branches?', ['A dam', 'A nest in a tree', 'A web', 'A burrow underground only'], 0),
    ('What is special about a beavers tail?', ['It is flat and helps it swim', 'It is very long and thin', 'It has feathers', 'It glows in the dark'], 0),
    ('Beavers are known for changing their environment by building ___.', ['Dams', 'Roads', 'Bridges made of metal', 'Cities'], 0)]),
SS('Our Electricians: Keeping the Lights On',
   'Kindergarten Social Studies strand: electricians install and fix the wires and lights that bring electricity to our homes and schools.',
   [('What does an electrician work with?', ['electricity and wires', 'wires and lights']),
    ('Why is an electricians job important?', ['keeps our lights and power working', 'helps keep us safe with electricity']),
    ('Name one place an electrician might work.', ['a house', 'a school'])],
   [('What does an electrician mainly work with?', ['Electrical wires and lights', 'Food and cooking', 'Books and pencils', 'Cars and roads'], 0),
    ('Why is it important to have skilled electricians?', ['They keep our power safe and working', 'Electricity does not need care', 'They have no important job', 'Only for decoration'], 0),
    ('Where might an electrician be called to work?', ['A house or school with an electrical problem', 'Only in outer space', 'Only underwater', 'Nowhere at all'], 0),
    ('Which of these might an electrician fix?', ['A broken light switch', 'A flat tire', 'A torn book page', 'A leaky faucet'], 0),
    ('Working with electricity safely is important because it can be ___ if handled carelessly.', ['Dangerous', 'Completely harmless', 'Invisible with no effect', 'Only a game'], 0)]),
]),
day(143, [
L('Prefixes: Adding Re- to Change Meaning',
  'Kindergarten Language strand: adding the prefix re- to the start of a word can mean to do something again, such as changing do into redo.',
  [('What does redo mean?', ['to do something again', 'do again']),
   ('What does the prefix re- usually mean?', ['again', 'to do again']),
   ('Give an example of a word with the prefix re-.', ['redo', 'refill'])],
  [('What does the word redo mean?', ['To do something again', 'To never do something', 'To stop doing something', 'To do something badly'], 0),
   ('What does the prefix re- usually add to a word?', ['The meaning of again', 'The meaning of not', 'A number', 'A colour'], 0),
   ('Which word means to fill something again?', ['Unfill', 'Refill', 'Filling', 'Filled'], 1),
   ('Adding re- to the word read makes the word ___.', ['Reread, meaning to read again', 'Unread', 'Reading only', 'Readless'], 0),
   ('A prefix is added to the ___ of a word.', ['End', 'Beginning', 'Middle', 'Nowhere'], 1)]),
M('Time: Reading a Digital Clock',
  'Kindergarten Math strand: students learn to read the hour and minutes shown on a digital clock, like a clock that shows 3:00.',
  [('What does a digital clock show?', ['numbers for the time', 'the hour and minutes']),
   ('What does 3:00 mean on a digital clock?', ['3 oclock', 'three oclock']),
   ('Which number comes first on a digital clock, the hour or the minutes?', ['the hour', 'hour comes first'])],
  [('What does a digital clock use to show the time?', ['Numbers', 'Hands', 'Pictures only', 'Colours'], 0),
   ('What time is shown by 3:00 on a digital clock?', ['Three oclock', 'Thirty oclock', 'Three minutes', 'Thirteen oclock'], 0),
   ('On a digital clock, which number usually comes first?', ['The minutes', 'The hour', 'The seconds', 'Neither'], 1),
   ('If a digital clock shows 7:00, what time is it?', ['Seven oclock', 'Seventeen oclock', 'Seven minutes', 'Seventy oclock'], 0),
   ('A digital clock is different from a clock with hands because it shows ___.', ['Numbers directly', 'No time at all', 'Only colours', 'Only shapes'], 0)]),
Sc('How Bread Is Made: From Wheat to Loaf',
   'Kindergarten Science strand: bread starts as wheat grown on a farm, which is ground into flour, mixed into dough, and baked in an oven.',
   [('What plant is bread usually made from?', ['wheat', 'wheat grain']),
    ('What is wheat ground into?', ['flour', 'flour for baking']),
    ('Where is bread dough baked?', ['an oven', 'in an oven'])],
   [('What crop is most bread made from?', ['Wheat', 'Rice', 'Cotton', 'Grass'], 0),
    ('What is wheat ground into to make bread?', ['Flour', 'Sugar', 'Salt', 'Juice'], 0),
    ('What do bakers mix flour with to make dough?', ['Water and other ingredients', 'Sand', 'Rocks', 'Nothing at all'], 0),
    ('Where is bread dough cooked?', ['In an oven', 'In a freezer', 'Underground', 'In a river'], 0),
    ('Bread making is an example of how food changes from a ___ to something we eat.', ['Plant', 'Rock', 'Animal', 'Machine'], 0)]),
SS('Money From Around the World: Comparing Currency',
   'Kindergarten Social Studies strand: different countries use different kinds of money, called currency, such as the Canadian dollar or the American dollar.',
   [('What is money from a country called?', ['currency', 'a countrys currency']),
    ('Name the currency used in Canada.', ['the Canadian dollar', 'dollar']),
    ('Do all countries use the same money?', ['no', 'no they use different currency'])],
   [('What word describes the money used by a country?', ['Currency', 'Language', 'Anthem', 'Symbol'], 0),
    ('What is the name of the currency used in Canada?', ['The Canadian dollar', 'The euro', 'The yen', 'The pound'], 0),
    ('Do all countries around the world use the exact same money?', ['No, different countries use different currency', 'Yes, every country uses the same money', 'Money is not used anywhere', 'Only Canada uses money'], 0),
    ('Why might a traveller need to exchange money when visiting another country?', ['Because that country uses a different currency', 'Money never changes anywhere', 'All countries ban money', 'Currency is only used in stores'], 0),
    ('Comparing currencies from different countries helps us learn about ___.', ['The world around us', 'Nothing important', 'Only colours', 'Only shapes'], 0)]),
]),
day(144, [
L('Suffixes: Adding -ful to Change Meaning',
  'Kindergarten Language strand: adding the suffix -ful to the end of a word can mean full of something, such as changing help into helpful.',
  [('What does helpful mean?', ['full of help', 'ready to help']),
   ('What does the suffix -ful usually mean?', ['full of', 'full of something']),
   ('Give an example of a word with the suffix -ful.', ['helpful', 'joyful'])],
  [('What does the word helpful mean?', ['Full of help, ready to help', 'Not helpful at all', 'Angry', 'Sleepy'], 0),
   ('What does the suffix -ful usually add to the meaning of a word?', ['Full of something', 'Not having something', 'A number', 'A colour'], 0),
   ('Which word means full of joy?', ['Joyless', 'Joyful', 'Joying', 'Unjoy'], 1),
   ('Adding -ful to the word care makes the word ___.', ['Careful, meaning full of care', 'Careless', 'Caring only', 'Uncared'], 0),
   ('A suffix is added to the ___ of a word.', ['Beginning', 'End', 'Middle', 'Nowhere'], 1)]),
M('Measurement: Comparing Volume with Containers',
  'Kindergarten Math strand: students compare how much different containers can hold, learning that some containers hold more than others.',
  [('What does volume tell us about a container?', ['how much it can hold', 'how much fits inside']),
   ('Which usually holds more, a big bucket or a small cup?', ['a big bucket', 'the bucket']),
   ('How can we check which container holds more?', ['fill them and compare', 'pour water and see'])],
  [('What does the volume of a container measure?', ['How much it can hold', 'How heavy it is', 'Its colour', 'Its shape only'], 0),
   ('Which container usually holds more water?', ['A large bucket', 'A small cup', 'A spoon', 'A thimble'], 0),
   ('How can you test which of two containers holds more?', ['Fill one with water and pour it into the other', 'Guess with no testing', 'Look at the colour only', 'Weigh them with a ruler'], 0),
   ('A container that holds less than another has a ___ volume.', ['Smaller', 'Bigger', 'Equal', 'Unknown'], 0),
   ('Comparing volume helps us understand how much something can ___.', ['Hold', 'Weigh', 'Cost', 'Smell'], 0)]),
Sc('Recycling Symbols: What the Arrows Mean',
   'Kindergarten Science strand: the recycling symbol has three arrows chasing each other, showing that materials can be turned into something new instead of thrown away.',
   [('How many arrows are in the recycling symbol?', ['3', 'three']),
    ('What does the recycling symbol mean?', ['materials can be reused', 'items can be turned into something new']),
    ('Why do we recycle?', ['to help take care of the earth', 'reduce waste'])],
   [('How many arrows make up the recycling symbol?', ['2', '3', '4', '5'], 1),
    ('What does the recycling symbol tell us about a material?', ['It can be turned into something new', 'It must be thrown in the garbage', 'It is dangerous', 'It is made of gold'], 0),
    ('Why is recycling helpful for the environment?', ['It reduces waste and reuses materials', 'It creates more garbage', 'It has no effect at all', 'It uses more resources for no reason'], 0),
    ('Which of these is often recyclable?', ['A clean plastic bottle', 'A banana peel', 'Wet paper towels', 'Broken glass shards mixed with trash'], 0),
    ('The recycling symbol reminds us to think before we ___ something.', ['Throw it away', 'Wear it', 'Eat it', 'Paint it'], 0)]),
SS('Our Town Hall: Where Decisions Are Made',
   'Kindergarten Social Studies strand: the town hall is a building where local leaders meet to make decisions and provide services for the community.',
   [('What is a town hall?', ['a building where leaders meet', 'where community decisions are made']),
    ('Who might work at a town hall?', ['a mayor', 'local leaders']),
    ('Why is a town hall important?', ['it helps run the community', 'decisions are made there'])],
   [('What is a town hall?', ['A building where local leaders make decisions', 'A place to buy groceries', 'A type of park', 'A kind of school'], 0),
    ('Who is one person who might work at a town hall?', ['The mayor', 'A pilot', 'A farmer', 'A doctor'], 0),
    ('Why is the town hall important to a community?', ['It is where decisions about the community are made', 'It has no purpose', 'It is only used for sports', 'It is closed at all times'], 0),
    ('Which of these might happen at a town hall?', ['A meeting about a new park', 'A birthday party for one family', 'A private vacation', 'Nothing at all'], 0),
    ('A town hall helps a community by providing ___.', ['Services and leadership', 'Only food', 'Only toys', 'Nothing useful'], 0)]),
]),
day(145, [
L('Homophones: Words That Sound the Same',
  'Kindergarten Language strand: homophones are words that sound exactly the same but have different meanings and spellings, like to, too, and two.',
  [('Give an example of two homophones.', ['to and too', 'sea and see']),
   ('Do homophones sound the same or different?', ['the same', 'they sound the same']),
   ('Do homophones always have the same spelling?', ['no', 'no they can be spelled differently'])],
  [('What are homophones?', ['Words that sound the same but have different meanings', 'Words that look the same', 'Words with no meaning', 'Words that rhyme but sound different'], 0),
   ('Which pair is an example of homophones?', ['Sea and see', 'Cat and dog', 'Big and small', 'Run and walk'], 0),
   ('Do homophones always have the same spelling?', ['Yes, always', 'No, they can be spelled differently', 'They have no spelling', 'Only sometimes the same sound'], 1),
   ('Which word is a homophone of the number two?', ['Too', 'Ten', 'Three', 'Twelve'], 0),
   ('Homophones can sometimes make writing tricky because they ___.', ['Sound alike but mean different things', 'Always look the same', 'Never sound alike', 'Have no use'], 0)]),
M('Money: Counting Dimes and Quarters',
  'Kindergarten Math strand: students learn that a dime is worth 10 cents and a quarter is worth 25 cents, and practice adding them together.',
  [('How much is a dime worth?', ['10 cents', 'ten cents']),
   ('How much is a quarter worth?', ['25 cents', 'twenty five cents']),
   ('What is the total of one dime and one quarter?', ['35 cents', '35']),
   ],
  [('How much is one dime worth?', ['1 cent', '5 cents', '10 cents', '25 cents'], 2),
   ('How much is one quarter worth?', ['10 cents', '15 cents', '20 cents', '25 cents'], 3),
   ('What is the total value of two dimes?', ['10 cents', '15 cents', '20 cents', '25 cents'], 2),
   ('What is the total value of one quarter and one dime?', ['15 cents', '25 cents', '30 cents', '35 cents'], 3),
   ('Which coin is worth more, a dime or a quarter?', ['A dime', 'A quarter', 'They are equal', 'Neither has value'], 1)]),
Sc('Our Immune System: Fighting Germs',
   'Kindergarten Science strand: our immune system is the bodys way of fighting off germs to help keep us healthy.',
   [('What does our immune system do?', ['fights off germs', 'helps keep us healthy']),
    ('Why is washing our hands helpful for our immune system?', ['it removes germs before they can make us sick', 'stops germs from spreading']),
    ('Name one way to help keep our immune system strong.', ['eating healthy food', 'getting enough sleep'])],
   [('What is the main job of our immune system?', ['Fighting off germs to keep us healthy', 'Helping us see', 'Helping us hear', 'Helping us taste food'], 0),
    ('How does handwashing help our immune system?', ['It removes germs before they can make us sick', 'It makes germs stronger', 'It has no effect', 'It only cleans our clothes'], 0),
    ('Which of these can help keep our immune system strong?', ['Eating healthy food and sleeping enough', 'Never washing our hands', 'Staying up very late every night', 'Avoiding all fruits and vegetables'], 0),
    ('What might happen if germs get past our immune system?', ['We might get sick', 'We instantly grow taller', 'Nothing changes at all', 'We become stronger instantly'], 0),
    ('Our immune system helps protect our body like a ___.', ['Defense team against germs', 'Type of food', 'Kind of toy', 'Colour'], 0)]),
SS('Helping New Students Feel Welcome',
   'Kindergarten Social Studies strand: when a new student joins our class, we can help them feel welcome by being friendly and showing them around.',
   [('How can you help a new student feel welcome?', ['be friendly to them', 'show them around']),
    ('Why might a new student feel nervous?', ['everything is unfamiliar', 'they do not know anyone yet']),
    ('Name one kind thing you could say to a new student.', ['welcome to our class', 'do you want to play'])],
   [('What is one way to help a new student feel welcome?', ['Being friendly and including them', 'Ignoring them completely', 'Being unkind to them', 'Avoiding them on purpose'], 0),
    ('Why might starting at a new school feel hard for someone?', ['Everything and everyone is unfamiliar at first', 'New schools are never hard', 'They already know everyone', 'It is never a big change'], 0),
    ('Which is a kind thing to say to a new student?', ['Welcome to our class, would you like to play', 'Go away, we do not want you here', 'Nothing at all', 'You do not belong here'], 0),
    ('Helping others feel welcome is an example of being ___.', ['Kind and inclusive', 'Unfriendly', 'Careless', 'Rude'], 0),
    ('How might you help a new student learn classroom rules?', ['Explain the rules kindly', 'Let them guess with no help', 'Get upset if they make a mistake', 'Ignore their questions'], 0)]),
]),
day(146, [
L('Contractions: Joining Two Words Together',
  'Kindergarten Language strand: a contraction joins two words together into one shorter word, using an apostrophe to show missing letters, such as do not becoming a shorter word.',
  [('What does a contraction do?', ['joins two words into one', 'makes two words shorter']),
   ('What mark shows letters are missing in a contraction?', ['an apostrophe', 'apostrophe']),
   ('Give an example of two words that can be joined into a contraction.', ['do not', 'I am'])],
  [('What is a contraction?', ['Two words joined into one shorter word', 'A very long word', 'A type of punctuation mark alone', 'A word with no meaning'], 0),
   ('What mark is used in a contraction to show missing letters?', ['A period', 'An apostrophe', 'A comma', 'A question mark'], 1),
   ('Which two words can combine to form a contraction?', ['Do and not', 'Cat and dog', 'Big and small', 'Red and blue'], 0),
   ('Contractions make writing and speaking ___.', ['Shorter and quicker', 'Longer', 'Impossible to understand', 'Silent'], 0),
   ('Why do contractions use an apostrophe?', ['To show that some letters were left out', 'To make the word longer', 'To change the meaning completely', 'For no reason at all'], 0)]),
M('Shapes: Composing Pictures with 2D Shapes',
  'Kindergarten Math strand: students combine different 2D shapes, like triangles, squares, and circles, to build pictures such as a house or a boat.',
  [('Name a shape you could use to make the roof of a house.', ['a triangle', 'triangle']),
   ('Name a shape you could use for the body of a boat.', ['a rectangle', 'trapezoid']),
   ('Why do we combine shapes to make pictures?', ['to build new pictures', 'shapes fit together to form pictures'])],
  [('Which shape is often used for the roof of a house picture?', ['Circle', 'Triangle', 'Oval', 'Rhombus'], 1),
   ('Which shape could be combined with a triangle to build a simple house?', ['A square', 'A single dot', 'Nothing else', 'A line'], 0),
   ('Combining shapes to make a picture is called ___ shapes.', ['Composing', 'Erasing', 'Hiding', 'Melting'], 0),
   ('Which shapes could you combine to build a simple boat?', ['A trapezoid and a triangle', 'Only circles', 'No shapes at all', 'Only lines'], 0),
   ('Why is it useful to combine shapes to build pictures?', ['It helps us see how shapes fit together', 'It has no purpose', 'It makes shapes disappear', 'It only works with one shape'], 0)]),
Sc('Simple Circuits: Making a Light Bulb Glow',
   'Kindergarten Science strand: a simple circuit connects a battery, wires, and a light bulb in a complete loop so that electricity can flow and make the bulb light up.',
   [('What powers a simple circuit?', ['a battery', 'the battery']),
    ('What happens when a circuit is complete?', ['the light bulb glows', 'electricity flows and the bulb lights up']),
    ('What connects the battery to the light bulb?', ['wires', 'a wire'])],
   [('What provides the power in a simple circuit?', ['A battery', 'A cup of water', 'A rock', 'Sunlight only'], 0),
    ('What happens when a circuit is complete and connected properly?', ['The light bulb glows', 'Nothing happens at all', 'The battery disappears', 'The wire melts instantly'], 0),
    ('What connects the parts of a simple circuit together?', ['Wires', 'String', 'Glue', 'Tape only'], 0),
    ('What do we call a circuit that is broken and not connected all the way around?', ['An open circuit', 'A closed circuit', 'A full circuit', 'A perfect circuit'], 0),
    ('A simple circuit needs a battery, wires, and a ___ to work.', ['Light bulb', 'Balloon', 'Book', 'Toy car'], 0)]),
SS('Canadian Inventions: Things Made in Canada',
   'Kindergarten Social Studies strand: Canadians have invented many useful things, such as basketball and insulin, that people around the world still use today.',
   [('Name something invented by a Canadian.', ['basketball', 'insulin']),
    ('Why are Canadian inventions important?', ['they help people around the world', 'they are used by many people']),
    ('Who invented basketball?', ['a Canadian named James Naismith', 'James Naismith'])],
   [('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Tennis', 'Golf'], 0),
    ('Why are Canadian inventions important to the world?', ['They help and are used by people everywhere', 'They are only used in Canada', 'They have no impact on anyone', 'They were never used at all'], 0),
    ('Which of these is an example of a Canadian invention?', ['Insulin', 'Pizza', 'The airplane wing alone', 'Chocolate'], 0),
    ('Inventions from Canada show that Canadians are ___.', ['Creative and helpful to the world', 'Not important', 'Unable to invent things', 'Only good at sports'], 0),
    ('Learning about Canadian inventions helps us understand ___.', ['How Canada has contributed to the world', 'Nothing important', 'Only Canadian weather', 'Only Canadian food'], 0)]),
]),
day(147, [
L('Dialogue: When Characters Speak',
  'Kindergarten Language strand: dialogue is when characters in a story talk, and it is often shown using quotation marks around the words they say.',
  [('What is dialogue?', ['when characters talk in a story', 'characters speaking']),
   ('What marks show that a character is speaking?', ['quotation marks', 'talking marks']),
   ('Why do authors use dialogue?', ['to show what characters say', 'make the story feel real'])],
  [('What is dialogue in a story?', ['When characters speak', 'The title of the book', 'The pictures in the book', 'The back cover'], 0),
   ('What marks are usually used to show a character is speaking?', ['Quotation marks', 'Question marks only', 'Exclamation marks only', 'Periods only'], 0),
   ('Why might an author include dialogue in a story?', ['To show what the characters say and feel', 'To make the book longer for no reason', 'To confuse the reader', 'To remove the characters'], 0),
   ('Which of these is an example of dialogue?', ['The character said hello to her friend', 'The sun was shining brightly', 'The story took place in a forest', 'The book had ten pages'], 0),
   ('Dialogue helps readers understand a characters ___.', ['Thoughts and feelings', 'Height', 'Weight', 'Age only'], 0)]),
M('Number Lines: Skip Counting by Twos',
  'Kindergarten Math strand: students use a number line to skip count by twos, jumping from 2 to 4 to 6 and beyond.',
  [('What number comes after 2, 4, 6 on a number line?', ['8', 'eight']),
   ('What is a number line used for when skip counting?', ['to jump between numbers', 'to see the pattern of jumps']),
   ('Skip count by 2s from 0 to 10.', ['0,2,4,6,8,10', '0 2 4 6 8 10'])],
  [('What comes next on a number line: 2, 4, 6, ___?', ['7', '8', '9', '10'], 1),
   ('Skip counting by 2s on a number line, what comes after 10?', ['11', '12', '13', '14'], 1),
   ('Each jump when skip counting by 2s on a number line covers ___ numbers.', ['1', '2', '3', '4'], 1),
   ('Which sequence shows skip counting by 2s?', ['2, 4, 6, 8', '2, 3, 4, 5', '2, 5, 8, 11', '2, 4, 8, 16'], 0),
   ('A number line helps us see the ___ between numbers when we skip count.', ['Jumps or pattern', 'Colours', 'Shapes', 'Letters'], 0)]),
Sc('Animal Tracks: Footprints in the Snow',
   'Kindergarten Science strand: many animals leave tracks, or footprints, in snow or mud, and we can use the shape of the tracks to guess which animal made them.',
   [('What are animal tracks?', ['footprints animals leave behind', 'footprints in snow or mud']),
    ('Where might you easily see animal tracks?', ['in snow', 'in mud or snow']),
    ('How can tracks help us learn about an animal?', ['the shape can show which animal made them', 'they show the animal was there'])],
   [('What are animal tracks?', ['Footprints animals leave behind', 'A type of animal food', 'A kind of nest', 'A sound animals make'], 0),
    ('Where can animal tracks often be seen clearly?', ['In snow or soft mud', 'On a sunny sidewalk', 'In the middle of the ocean', 'In the sky'], 0),
    ('How can the shape of a track help us?', ['It can help us guess which animal made it', 'It tells us the animals favourite colour', 'It has no useful information', 'It tells us the animals age exactly'], 0),
    ('Which of these might leave visible tracks in snow?', ['A rabbit', 'A goldfish', 'A whale', 'A jellyfish'], 0),
    ('Studying animal tracks is a way scientists learn about animals without ___.', ['Seeing the animal directly', 'Any effort at all', 'Using their eyes', 'Leaving their home'], 0)]),
SS('Our Recycling Truck Drivers: Collecting Bottles and Cans',
   'Kindergarten Social Studies strand: recycling truck drivers collect bottles, cans, and paper from our homes so they can be turned into new things instead of going to waste.',
   [('What do recycling truck drivers collect?', ['bottles, cans, and paper', 'recyclable materials']),
    ('Why is their job helpful for the environment?', ['recycled materials do not go to waste', 'they help reduce waste']),
    ('What happens to the materials after they are collected?', ['they are turned into new things', 'they get recycled into new products'])],
   [('What do recycling truck drivers mainly collect?', ['Bottles, cans, and paper', 'Wild animals', 'Books from the library', 'Fresh food'], 0),
    ('Why is the work of recycling truck drivers helpful for the environment?', ['It helps materials get reused instead of wasted', 'It creates more pollution on purpose', 'It has no benefit at all', 'It only helps one family'], 0),
    ('What often happens to materials after a recycling truck collects them?', ['They are processed and turned into new products', 'They are thrown into the ocean', 'They disappear completely', 'Nothing happens to them'], 0),
    ('How can families help recycling truck drivers do their job well?', ['Sorting recyclables correctly before pickup', 'Mixing all garbage together', 'Hiding the bins', 'Ignoring recycling completely'], 0),
    ('Recycling helps our community by ___.', ['Reducing waste and reusing materials', 'Increasing pollution', 'Wasting more resources', 'Doing nothing useful'], 0)]),
]),
day(148, [
L('Sequencing Events: Story Order with Pictures',
  'Kindergarten Language strand: students look at pictures from a story and put them in order to show what happened first, next, and last.',
  [('What does sequencing events mean?', ['putting events in order', 'showing what happened first, next, and last']),
   ('What word describes the event that happens first?', ['first', 'beginning']),
   ('What word describes the event that happens last?', ['last', 'end'])],
  [('What does it mean to sequence events in a story?', ['Putting events in the order they happened', 'Drawing new pictures', 'Changing the characters', 'Removing the ending'], 0),
   ('Which word tells us an event happens at the very beginning?', ['First', 'Last', 'Never', 'Sometimes'], 0),
   ('Which word tells us an event happens at the very end?', ['First', 'Next', 'Last', 'Before'], 2),
   ('Why do we use pictures to help sequence a story?', ['They help show the order of events clearly', 'Pictures have no use in stories', 'They only show the ending', 'They confuse the order'], 0),
   ('Putting story pictures in the correct order helps readers understand the ___.', ['Plot', 'Cover colour', 'Page count', 'Font size'], 0)]),
M('Estimating Quantities: About How Many in a Jar',
  'Kindergarten Math strand: students make a reasonable guess about how many objects are in a jar before counting to check.',
  [('What does it mean to estimate a quantity?', ['make a careful guess about how many', 'guess about how many there are']),
   ('How can you check if your estimate was close?', ['count the objects', 'count to check']),
   ('Why might we estimate before counting?', ['to practise making a good guess', 'counting takes time'])],
  [('What does it mean to estimate how many objects are in a jar?', ['Make a careful guess before counting', 'Know the exact number with no guessing', 'Ignore the jar completely', 'Measure the jars height only'], 0),
   ('How can we find out if our estimate was close to the real amount?', ['Count the objects carefully', 'Guess again with no counting', 'Shake the jar and stop', 'Ignore it forever'], 0),
   ('A good estimate is a guess that is ___.', ['Wildly random', 'Reasonable and thoughtful', 'Always exactly correct', 'Impossible to make'], 1),
   ('Which jar would likely hold more small objects, a tall thin jar or a tiny jar?', ['A tall thin jar', 'A tiny jar', 'They always hold the same amount', 'Neither can hold objects'], 0),
   ('Estimating before counting helps us practise thinking about ___.', ['Numbers and amounts', 'Colours only', 'Shapes only', 'Nothing useful'], 0)]),
Sc('Camels: Animals of the Desert',
   'Kindergarten Science strand: camels are animals well suited to life in the desert, with humps that store fat and the ability to go a long time without water.',
   [('What kind of environment do camels live in?', ['the desert', 'a desert'])
    , ('What is stored in a camels hump?', ['fat', 'fat, not water']),
    ('How long can a camel go without drinking water?', ['a long time', 'many days'])],
   [('What kind of habitat are camels well suited for?', ['The desert', 'The ocean', 'The rainforest', 'The Arctic'], 0),
    ('What is actually stored inside a camels hump?', ['Fat', 'Water', 'Sand', 'Air'], 0),
    ('What is a camel able to do that helps it survive the desert?', ['Go a long time without drinking water', 'Fly over sand dunes', 'Breathe underwater', 'Live only in snow'], 0),
    ('Which body feature helps protect a camels eyes from blowing sand?', ['Long eyelashes', 'Big ears', 'A long tail', 'Sharp claws'], 0),
    ('Camels are well adapted to living in a habitat that is usually ___.', ['Hot and dry', 'Cold and wet', 'Underwater', 'Covered in snow'], 0)]),
SS('Provincial and Territorial Flags: Symbols of Canada',
   'Kindergarten Social Studies strand: each province and territory in Canada has its own flag, with special colours and pictures that represent that place.',
   [('What does a provincial flag represent?', ['a province', 'that province or territory']),
    ('Do all provinces have the same flag?', ['no', 'no, each one is different']),
    ('Name one thing a flag might show.', ['a symbol or picture', 'special colours'])],
   [('What does each provincial or territorial flag represent?', ['That specific province or territory', 'The whole world', 'Only cities', 'Nothing at all'], 0),
    ('Do all of Canadas provinces and territories share one identical flag?', ['No, each has its own unique flag', 'Yes, they are all the same', 'Only two provinces have flags', 'Flags are not allowed in Canada'], 0),
    ('What might a provincial flag include?', ['Special colours and symbols', 'Only plain white', 'Nothing visible', 'Random scribbles'], 0),
    ('Why might people be proud of their provinces flag?', ['It represents their home and identity', 'Flags have no meaning', 'It represents another country', 'It is only used once a year'], 0),
    ('Learning about provincial flags helps us understand more about ___.', ['Canadas different provinces and territories', 'Nothing important', 'Only the capital city', 'Only sports teams'], 0)]),
]),
day(149, [
L('Question Words: Why and How',
  'Kindergarten Language strand: the question words why and how help us ask about reasons and the way something happens.',
  [('What does the question word why ask about?', ['a reason', 'the reason for something']),
   ('What does the question word how ask about?', ['the way something happens', 'the way or method']),
   ('Give an example of a question using why.', ['why is the sky blue', 'why do birds fly'])],
  [('What does the question word why usually ask about?', ['A reason', 'A place', 'A time', 'A person'], 0),
   ('What does the question word how usually ask about?', ['The way something is done', 'A colour', 'A number only', 'A shape only'], 0),
   ('Which question uses the word why?', ['Why is the sky blue?', 'Where is the park?', 'Who is that?', 'What time is it?'], 0),
   ('Which question uses the word how?', ['How do birds fly?', 'Who made this?', 'When is it?', 'Where do we go?'], 0),
   ('Asking why and how helps us understand ___ about the world.', ['Reasons and processes', 'Only colours', 'Only names', 'Nothing new'], 0)]),
M('Building Numbers with Tens and Ones Blocks',
  'Kindergarten Math strand: students use blocks that represent tens and ones to build two-digit numbers, such as using 2 tens blocks and 3 ones blocks to make 23.',
  [('How many tens blocks and ones blocks make 23?', ['2 tens and 3 ones', '2 tens blocks and 3 ones blocks']),
   ('What number is made with 3 tens blocks and 0 ones blocks?', ['30', 'thirty']),
   ('Why do we use tens and ones blocks?', ['to help build and see numbers', 'to understand place value'])],
  [('How many tens blocks and ones blocks make the number 23?', ['2 tens and 3 ones', '3 tens and 2 ones', '2 tens and 2 ones', '3 tens and 3 ones'], 0),
   ('What number is shown by 4 tens blocks and 0 ones blocks?', ['4', '14', '40', '400'], 2),
   ('What number is shown by 1 ten block and 5 ones blocks?', ['5', '10', '15', '51'], 2),
   ('Using tens and ones blocks helps us understand ___.', ['Place value', 'Colours', 'Shapes', 'Letters'], 0),
   ('Which is bigger, a tens block or a ones block?', ['A tens block', 'A ones block', 'They are the same size', 'Neither has size'], 0)]),
Sc('Icebergs: Giant Pieces of Floating Ice',
   'Kindergarten Science strand: an iceberg is a huge piece of ice that has broken off a glacier and floats in the ocean, with most of it hidden underwater.',
   [('What is an iceberg?', ['a huge piece of floating ice', 'a giant piece of ice in the ocean']),
    ('Where does an iceberg come from?', ['it breaks off a glacier', 'a glacier']),
    ('Is most of an iceberg above or below the water?', ['below the water', 'below']),
    ],
   [('What is an iceberg?', ['A huge piece of floating ice', 'A type of fish', 'A warm ocean current', 'A kind of boat'], 0),
    ('Where does an iceberg usually come from?', ['It breaks off a glacier', 'It is made in a factory', 'It falls from the sky as one piece', 'It grows from the ocean floor'], 0),
    ('Which part of an iceberg is usually hidden underwater?', ['Most of it', 'None of it', 'A tiny bit', 'All of it floats on top'], 0),
    ('Why can icebergs be dangerous for ships?', ['A large hidden part is underwater and hard to see', 'They are always painted bright colours', 'They make loud warning sounds', 'They never move'], 0),
    ('Icebergs are found in very ___ parts of the ocean.', ['Cold', 'Hot', 'Sandy', 'Dry'], 0)]),
SS('World Landmarks: Famous Places Around the World',
   'Kindergarten Social Studies strand: world landmarks are famous and special places found in different countries, like a tall tower or an ancient pyramid, that many people like to visit and learn about.',
   [('What is a world landmark?', ['a famous special place', 'a well known place in the world']),
    ('Name a world landmark.', ['a pyramid', 'a famous tower']),
    ('Why do people visit world landmarks?', ['to see something special', 'to learn about the place'])],
   [('What is a world landmark?', ['A famous and special place people like to visit', 'A type of food', 'A kind of animal', 'A weather pattern'], 0),
    ('Which of these is an example of a world landmark?', ['A famous ancient pyramid', 'A regular kitchen chair', 'A plain sidewalk', 'A common street sign'], 0),
    ('Why might people travel to see a world landmark?', ['To see something special and learn about it', 'Landmarks have no interest to anyone', 'To avoid learning anything new', 'Landmarks cannot be visited'], 0),
    ('Learning about landmarks in other countries helps us understand ___.', ['Different places and cultures around the world', 'Nothing outside our own street', 'Only our own country', 'Only our own school'], 0),
    ('Which best describes why landmarks are considered special?', ['They represent something important about a place or its history', 'They are chosen completely at random', 'They have no history at all', 'They are the same everywhere'], 0)]),
]),
day(150, [
L('Language Review: New Word Families, Word Parts, and Story Skills',
  'Kindergarten Language strand review: students revisit the -ell and -ill word families, prefixes and suffixes, homophones, contractions, dialogue, sequencing, and question words.',
  [('Name a word from the -ell or -ill family.', ['bell', 'hill']),
   ('What does the prefix re- usually mean?', ['again']),
   ('What is dialogue in a story?', ['when characters speak'])],
  [('Which word belongs to the -ell family?', ['Cat', 'Bell', 'Sun', 'Top'], 1),
   ('What does the word helpful mean?', ['Full of help, ready to help', 'Not helpful at all', 'Angry', 'Sleepy'], 0),
   ('What are homophones?', ['Words that sound the same but have different meanings', 'Words that look the same', 'Words with no meaning', 'Words that rhyme but sound different'], 0),
   ('What is a contraction?', ['Two words joined into one shorter word', 'A very long word', 'A type of punctuation mark alone', 'A word with no meaning'], 0),
   ('What does the question word why usually ask about?', ['A reason', 'A place', 'A time', 'A person'], 0)]),
M('Math Review: Near Doubles, Time, Money, and Place Value',
  'Kindergarten Math strand review: students revisit near doubles, number bonds to 11, digital clocks, comparing volume, dimes and quarters, shapes, number lines, estimating, and tens and ones blocks.',
  [('If 6 + 6 = 12, what is 6 + 5?', ['11']),
   ('How much is one quarter worth?', ['25 cents']),
   ('How many tens blocks and ones blocks make 23?', ['2 tens and 3 ones'])],
  [('If 6 + 6 = 12, what is 6 + 5?', ['10', '11', '12', '13'], 1),
   ('What time is shown by 3:00 on a digital clock?', ['Three oclock', 'Thirty oclock', 'Three minutes', 'Thirteen oclock'], 0),
   ('How much is one quarter worth?', ['10 cents', '15 cents', '20 cents', '25 cents'], 3),
   ('What comes next on a number line: 2, 4, 6, ___?', ['7', '8', '9', '10'], 1),
   ('What number is shown by 4 tens blocks and 0 ones blocks?', ['4', '14', '40', '400'], 2)]),
Sc('Science Review: Ladybugs, Animals, and Our Bodies',
   'Kindergarten Science strand review: students revisit the ladybug life cycle, beavers, bread making, recycling symbols, our immune system, simple circuits, animal tracks, camels, and icebergs.',
   [('What is the first stage of a ladybugs life cycle?', ['egg']),
    ('What animal is Canadas national animal?', ['the beaver']),
    ('What is the main job of our immune system?', ['fighting off germs'])],
   [('What is the first stage of a ladybugs life cycle?', ['Egg', 'Larva', 'Pupa', 'Adult'], 0),
    ('What animal is the national animal of Canada?', ['The beaver', 'The moose', 'The polar bear', 'The loon'], 0),
    ('What is the main job of our immune system?', ['Fighting off germs to keep us healthy', 'Helping us see', 'Helping us hear', 'Helping us taste food'], 0),
    ('What provides the power in a simple circuit?', ['A battery', 'A cup of water', 'A rock', 'Sunlight only'], 0),
    ('What kind of habitat are camels well suited for?', ['The desert', 'The ocean', 'The rainforest', 'The Arctic'], 0)]),
SS('Social Studies Review: Helpers, Money, and Our World',
   'Kindergarten Social Studies strand review: students revisit lifeguards, electricians, world currency, the town hall, welcoming new students, Canadian inventions, recycling truck drivers, provincial flags, and world landmarks.',
   [('What is the main job of a lifeguard?', ['keeping swimmers safe']),
    ('What word describes the money used by a country?', ['currency']),
    ('What is a world landmark?', ['a famous special place'])],
   [('What is the main job of a lifeguard?', ['Keeping swimmers safe in the water', 'Teaching math', 'Cooking food', 'Driving a bus'], 0),
    ('What word describes the money used by a country?', ['Currency', 'Language', 'Anthem', 'Symbol'], 0),
    ('What is a town hall?', ['A building where local leaders make decisions', 'A place to buy groceries', 'A type of park', 'A kind of school'], 0),
    ('Which sport was invented by a Canadian named James Naismith?', ['Basketball', 'Soccer', 'Tennis', 'Golf'], 0),
    ('What is a world landmark?', ['A famous and special place people like to visit', 'A type of food', 'A kind of animal', 'A weather pattern'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_141_150)
    append_worksheet_days(0, g0_141_150)
