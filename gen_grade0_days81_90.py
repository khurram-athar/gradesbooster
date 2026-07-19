#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 81-90 -- sixth batch extending Grade 0 past
the Days 71-80 batch, completing Days 1-90. This is a self-contained script
(does NOT use gen_curriculum.py's sub()/day()/append_to() helpers, since
those do not support a worksheet field) modeled exactly on
gen_grade0_days71_80.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-80 topics (see data/grade0.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260919):
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


# ─── DAY 81 ─────────────────────────────────────────────────────────────────
d81_lang = sub('Language', 'Word Families: -ig Words',
  'Students explore the -ig word family, learning that changing the first letter of words like big, pig, and dig creates new rhyming words that share the same ending sound.',
  [('Change the b in big to p. What new word do you make?', ['pig']),
   ('Change the p in pig to d. What new word do you make?', ['dig']),
   ('Name one more word that rhymes with big, pig, and dig.', ['wig', 'fig', 'jig'])],
  [('Which word rhymes with big?', ['Pig', 'Dog', 'Sun', 'Cup'], 0),
   ('Change the b in big to d. What new word do you make?', ['Dig', 'Dog', 'Dad', 'Din'], 0),
   ('Which of these words is part of the -ig word family?', ['Wig', 'Wag', 'Wet', 'Win'], 0),
   ('Words in the -ig family all end with the same ___.', ['Sound', 'Colour', 'Picture', 'Number'], 0),
   ('Which word does not belong in the -ig word family?', ['Sun', 'Big', 'Pig', 'Dig'], 0)])

d81_math = sub('Math', 'Place Value: Grouping into Tens and Ones',
  'Students learn that a two-digit number can be broken into a group of ten and some extra ones, such as seeing 14 as one group of ten plus four more ones.',
  [('How many tens are in the number 14?', ['1', 'one']),
   ('How many extra ones are in the number 14?', ['4', 'four']),
   ('If you have 1 group of ten and 6 ones, what number do you have?', ['16', 'sixteen'])],
  [('How many tens are in the number 12?', ['1', '2', '0', '3'], 0),
   ('How many ones are left over in the number 12?', ['2', '1', '0', '3'], 0),
   ('If you have 1 group of ten and 8 ones, what number do you have?', ['18', '10', '8', '80'], 0),
   ('The number 20 is made of how many groups of ten?', ['2', '1', '20', '0'], 0),
   ('Breaking a number into tens and ones helps us ___.', ['Understand what the number means', 'Forget the number', 'Make the number smaller', 'Change the number completely'], 0)])

d81_sci = sub('Science', 'Our Skin: Protecting Our Body',
  'Students learn that skin covers our whole body and helps protect us from germs, dirt, and the sun, and that keeping skin clean helps us stay healthy.',
  [('What body part covers our whole body and protects us?', ['skin']),
   ('Name one thing our skin protects us from, like germs or dirt.', ['germs', 'dirt', 'the sun']),
   ('Does washing our skin help keep us healthy?', ['yes'])],
  [('What body part covers our whole body?', ['Skin', 'Hair', 'Teeth', 'Eyes'], 0),
   ('What does our skin help protect us from?', ['Germs and dirt', 'Nothing at all', 'Only loud noises', 'Only bright light'], 0),
   ('Why is it important to wash our skin?', ['It helps keep us clean and healthy', 'Washing skin has no benefit', 'Skin never gets dirty', 'Skin does not need care'], 0),
   ('Which of these helps protect our skin outside on a sunny day?', ['Wearing sunscreen or a hat', 'Staying dirty all day', 'Ignoring the sun completely', 'Removing all clothing'], 0),
   ('Our skin is best described as our bodys ___.', ['Protective covering', 'Only decoration', 'Least important part', 'Food source'], 0)])

d81_ss = sub('SocialStudies', 'Our Librarian: Helping Us Find and Borrow Books',
  'Students learn about the job of a librarian, a community helper who works at the library, helps people find books, and teaches us how to borrow and return them.',
  [('Who works at the library and helps people find books?', ['librarian']),
   ('Name one thing you can borrow from the library, like a book.', ['book', 'a book']),
   ('Should we return library books after we finish reading them?', ['yes'])],
  [('Who helps people find books at the library?', ['A librarian', 'A baker', 'A firefighter', 'A postal worker'], 0),
   ('What can you do with a library book after reading it?', ['Return it to the library', 'Keep it forever without asking', 'Throw it away', 'Give it to a stranger'], 0),
   ('Why is a librarian a helpful community member?', ['They help people find and borrow books', 'They deliver mail', 'They fix cars', 'They cook food'], 0),
   ('Which of these might a librarian teach you?', ['How to find a book you want to read', 'How to bake bread', 'How to fly a plane', 'How to fix a pipe'], 0),
   ('A library is a place where books are ___.', ['Shared with the whole community', 'Only for one family', 'Never allowed to be read', 'Always thrown away'], 0)])

# ─── DAY 82 ─────────────────────────────────────────────────────────────────
d82_lang = sub('Language', 'Word Families: -ug Words',
  'Students explore the -ug word family, learning that changing the first letter of words like bug, rug, and hug creates new rhyming words that share the same ending sound.',
  [('Change the b in bug to r. What new word do you make?', ['rug']),
   ('Change the r in rug to h. What new word do you make?', ['hug']),
   ('Name one more word that rhymes with bug, rug, and hug.', ['mug', 'jug', 'tug'])],
  [('Which word rhymes with bug?', ['Rug', 'Cat', 'Sun', 'Pen'], 0),
   ('Change the b in bug to h. What new word do you make?', ['Hug', 'Hop', 'Hat', 'Hit'], 0),
   ('Which of these words is part of the -ug word family?', ['Mug', 'Man', 'Mad', 'Map'], 0),
   ('Words in the same word family share the same ending ___.', ['Sound', 'Meaning', 'Colour', 'Author'], 0),
   ('Which word does not belong in the -ug word family?', ['Top', 'Bug', 'Rug', 'Hug'], 0)])

d82_math = sub('Math', 'Fact Families: Related Addition and Subtraction',
  'Students learn that three numbers, such as 3, 4, and 7, can form a fact family, showing how the same numbers connect two addition facts and two subtraction facts.',
  [('If 3 plus 4 equals 7, what does 7 minus 4 equal?', ['3', 'three']),
   ('If 3 plus 4 equals 7, what does 7 minus 3 equal?', ['4', 'four']),
   ('Name the three numbers in the fact family with 3, 4, and 7.', ['3, 4, 7', '3 4 7'])],
  [('If 2 plus 5 equals 7, what does 7 minus 5 equal?', ['2', '5', '7', '0'], 0),
   ('If 6 plus 2 equals 8, what does 8 minus 6 equal?', ['2', '6', '8', '0'], 0),
   ('Which numbers form a fact family with 4, 5, and 9?', ['4 plus 5 equals 9', '4 plus 9 equals 5', '5 minus 9 equals 4', '9 plus 5 equals 4'], 0),
   ('A fact family uses the same ___ numbers in different addition and subtraction sentences.', ['Three', 'Two', 'Five', 'Ten'], 0),
   ('Knowing a fact family helps us see how addition and subtraction are ___.', ['Connected to each other', 'Never related', 'Always the same number', 'Impossible to compare'], 0)])

d82_sci = sub('Science', 'Animal Babies: Born Live or Hatched from Eggs',
  'Students learn that some animal babies, like puppies and kittens, are born live, while other animal babies, like chicks and turtles, hatch from eggs.',
  [('Name one animal baby that is born live, like a puppy.', ['puppy', 'kitten']),
   ('Name one animal baby that hatches from an egg, like a chick.', ['chick', 'turtle', 'a chick']),
   ('Does a chick hatch from an egg or get born live?', ['hatch from an egg', 'from an egg'])],
  [('Which animal baby is born live?', ['Puppy', 'Chick', 'Turtle', 'Snake'], 0),
   ('Which animal baby hatches from an egg?', ['Chick', 'Puppy', 'Kitten', 'Cow'], 0),
   ('A baby bird grows and hatches from ___.', ['An egg', 'Its mothers fur', 'A nest of leaves only', 'Nothing at all'], 0),
   ('Which of these animals hatches from an egg?', ['A turtle', 'A dog', 'A cat', 'A cow'], 0),
   ('Comparing how animal babies are born helps us learn that animals ___.', ['Grow and are born in different ways', 'All grow in the exact same way', 'Never grow at all', 'Are not connected to their parents'], 0)])

d82_ss = sub('SocialStudies', 'Our Mayor: Leading Our Town or City',
  'Students learn about the job of a mayor, a person chosen to help lead a town or city and make decisions that help the whole community.',
  [('What do we call the person chosen to help lead a town or city?', ['mayor']),
   ('Does a mayor help make decisions for a whole community?', ['yes']),
   ('Name one thing a mayor might help decide, like building a new park.', ['a new park', 'building a park', 'community decisions'])],
  [('What do we call the person chosen to help lead a town or city?', ['Mayor', 'Librarian', 'Dentist', 'Baker'], 0),
   ('What kind of decisions might a mayor help make?', ['Decisions that help the whole community', 'Decisions about only one persons house', 'No decisions at all', 'Decisions about outer space'], 0),
   ('Why is a mayor an important community leader?', ['They help lead and make decisions for the town or city', 'They deliver mail every day', 'They only bake bread', 'They fix broken pipes'], 0),
   ('Which of these might a mayor help with?', ['Deciding to build a new park', 'Fixing a leaky faucet', 'Baking a birthday cake', 'Delivering a package'], 0),
   ('A mayor leads a community similar to how a principal leads a ___.', ['School', 'Forest', 'Ocean', 'Desert'], 0)])

# ─── DAY 83 ─────────────────────────────────────────────────────────────────
d83_lang = sub('Language', 'Beginning Blends: Two Sounds Together at the Start',
  'Students learn that some words begin with two consonant sounds blended together, such as bl in black, st in stop, and gr in green, with both sounds heard clearly.',
  [('What two letters blend together at the start of the word black?', ['bl']),
   ('What two letters blend together at the start of the word stop?', ['st']),
   ('Say the word green. What two letters blend together at the start?', ['gr'])],
  [('Which word begins with the blend bl?', ['Black', 'Cat', 'Sun', 'Top'], 0),
   ('Which word begins with the blend st?', ['Stop', 'Man', 'Pig', 'Dog'], 0),
   ('In the word green, which two letters blend together at the start?', ['Gr', 'Ee', 'En', 'Re'], 0),
   ('A beginning blend is when two letters ___.', ['Are both heard together at the start of a word', 'Make one totally silent sound', 'Never appear together', 'Are always at the end of a word'], 0),
   ('Which word begins with the blend gr?', ['Green', 'Red', 'Big', 'Wet'], 0)])

d83_math = sub('Math', 'Composing Shapes: Making Bigger Shapes from Smaller Ones',
  'Students explore how smaller shapes, like two triangles, can be put together to make a new, bigger shape, such as combining two triangles to form a square.',
  [('If you put two triangles together, what new shape can you make?', ['square', 'a square']),
   ('What do we call it when we put small shapes together to make a bigger shape?', ['composing shapes', 'composing']),
   ('Can two smaller shapes ever combine to make one bigger shape?', ['yes'])],
  [('If you put two triangles together carefully, what shape can you make?', ['A square', 'A circle', 'A single dot', 'Nothing at all'], 0),
   ('What is it called when we combine smaller shapes to build a bigger shape?', ['Composing shapes', 'Erasing shapes', 'Hiding shapes', 'Ignoring shapes'], 0),
   ('Which two shapes could combine to make a rectangle?', ['Two squares', 'Two circles', 'Two dots', 'One triangle'], 0),
   ('Building a new shape out of smaller shapes helps us understand that shapes can be ___.', ['Put together in different ways', 'Never combined', 'Only taken apart', 'Impossible to build'], 0),
   ('Composing shapes is a skill that helps us later understand ___.', ['How bigger shapes are built from smaller parts', 'How to bake bread', 'How to spell words', 'How to sing songs'], 0)])

d83_sci = sub('Science', 'Inside a Seed: How a Plant Begins',
  'Students learn that a tiny seed holds everything a new plant needs to begin growing, and that with soil, water, and sunlight, a seed can sprout into a plant.',
  [('What tiny object holds everything a new plant needs to begin growing?', ['seed', 'a seed']),
   ('Name one thing a seed needs to sprout, like water or sunlight.', ['water', 'sunlight', 'soil']),
   ('Can a seed grow into a plant if it gets soil, water, and sunlight?', ['yes'])],
  [('What tiny object holds everything a new plant needs to grow?', ['A seed', 'A rock', 'A cloud', 'A shell'], 0),
   ('Which of these does a seed need to sprout?', ['Water', 'Sand only', 'Loud noise', 'Darkness only'], 0),
   ('What happens to a seed when it gets soil, water, and sunlight?', ['It sprouts and grows into a plant', 'It disappears completely', 'It turns into a rock', 'Nothing happens at all'], 0),
   ('Why is a seed an important part of a plants life cycle?', ['It is where a brand new plant begins to grow', 'Seeds have no connection to plants', 'Plants never start from seeds', 'Seeds only exist after a plant dies'], 0),
   ('A seed is best described as the ___ of a plant.', ['Beginning', 'Ending', 'Middle only', 'Shadow'], 0)])

d83_ss = sub('SocialStudies', 'Community Gardens: Growing Food Together',
  'Students learn that a community garden is a shared space where neighbours can plant, grow, and take care of vegetables and flowers together.',
  [('What do we call a shared space where neighbours grow food together?', ['community garden']),
   ('Name one thing that might grow in a community garden, like a vegetable.', ['vegetable', 'flower', 'tomato']),
   ('Do neighbours work together to take care of a community garden?', ['yes'])],
  [('What is a community garden?', ['A shared space where neighbours grow food together', 'A garden owned by only one family', 'A store that sells toys', 'A place with no plants at all'], 0),
   ('Which of these might you find in a community garden?', ['Vegetables and flowers', 'Books and pencils', 'Cars and trucks', 'Televisions'], 0),
   ('Why might neighbours enjoy working in a community garden together?', ['It lets them share the work and enjoy fresh food together', 'Gardens are never shared with anyone', 'Working together is never helpful', 'Community gardens have no benefit'], 0),
   ('A community garden helps teach us that neighbours can ___.', ['Work together to grow something helpful', 'Never help each other', 'Only work completely alone', 'Ignore their shared spaces'], 0),
   ('Taking care of a community garden together is an example of ___.', ['Teamwork and cooperation', 'Arguing and disagreement', 'Ignoring the community', 'Wasting food on purpose'], 0)])

# ─── DAY 84 ─────────────────────────────────────────────────────────────────
d84_lang = sub('Language', 'Rhyming or Not: Does It Rhyme?',
  'Students practise listening to pairs of words and deciding whether the words rhyme, meaning they end with the same sound, like cat and hat, or do not rhyme, like cat and dog.',
  [('Do the words cat and hat rhyme?', ['yes']),
   ('Do the words cat and dog rhyme?', ['no']),
   ('Name a word that rhymes with the word sun.', ['fun', 'run', 'bun'])],
  [('Do the words sun and fun rhyme?', ['Yes', 'No', 'Cannot tell', 'Only sometimes'], 0),
   ('Do the words sun and cup rhyme?', ['No', 'Yes', 'Cannot tell', 'Always'], 0),
   ('Two words rhyme when they ___.', ['End with the same sound', 'Start with the same letter', 'Have the same number of letters', 'Mean the exact same thing'], 0),
   ('Which word rhymes with tree?', ['Bee', 'Sun', 'Dog', 'Cup'], 0),
   ('Which pair of words does NOT rhyme?', ['Dog and star', 'Cat and hat', 'Sun and fun', 'Tree and bee'], 0)])

d84_math = sub('Math', 'Data: Sorting Objects into a Chart',
  'Students learn to sort a group of objects, such as toys or shapes, into a simple chart based on one shared feature, like colour or type, and then count each group.',
  [('If you sort toys by colour, do red toys go with other red toys?', ['yes']),
   ('What do we call it when we group objects that share a feature?', ['sorting']),
   ('After sorting toys into a chart, what can we do to see which group has more?', ['count them', 'counting'])],
  [('If you sort blocks by colour, where would a blue block go?', ['With the other blue blocks', 'With the red blocks', 'Nowhere at all', 'With every colour at once'], 0),
   ('What do we call grouping objects that share the same feature?', ['Sorting', 'Erasing', 'Hiding', 'Ignoring'], 0),
   ('After sorting toys into a chart, how can we tell which group has the most?', ['Count each group and compare', 'Guess without counting', 'Throw the toys away', 'Ignore the chart completely'], 0),
   ('If a chart shows 5 red toys and 3 blue toys, which colour has more?', ['Red', 'Blue', 'They are equal', 'Cannot tell'], 0),
   ('Sorting objects into a chart helps us ___ information easily.', ['Organize and compare', 'Forget', 'Hide', 'Waste'], 0)])

d84_sci = sub('Science', 'Simple Machines: Levers and Pulleys',
  'Students learn that a lever is a simple machine that helps lift heavy things using a bar and a support point, and a pulley uses a wheel and rope to help lift objects up.',
  [('What simple machine uses a bar to help lift heavy things?', ['lever', 'a lever']),
   ('What simple machine uses a wheel and rope to lift objects?', ['pulley', 'a pulley']),
   ('Do levers and pulleys make lifting heavy things easier?', ['yes'])],
  [('What simple machine uses a bar and a support point to lift things?', ['A lever', 'A pulley', 'A wheel only', 'A ramp'], 0),
   ('What simple machine uses a wheel and rope?', ['A pulley', 'A lever', 'A ramp', 'A wedge'], 0),
   ('Why might someone use a lever or pulley?', ['To make lifting heavy things easier', 'To make objects heavier', 'To make lifting harder', 'They have no real purpose'], 0),
   ('Which of these is an example of a pulley in real life?', ['Raising a flag on a flagpole', 'Reading a book', 'Eating lunch', 'Drawing a picture'], 0),
   ('Simple machines like levers and pulleys help people ___.', ['Do work more easily', 'Make work harder', 'Avoid all work forever', 'Create more mess'], 0)])

d84_ss = sub('SocialStudies', 'Riding the Bus: Being Safe and Polite',
  'Students learn safe and polite behaviour when riding a school bus or public bus, such as staying seated, using a quiet voice, and waiting for a turn to get on and off.',
  [('Should we stay seated while riding on a bus?', ['yes']),
   ('Name one polite behaviour to show on a bus, like using a quiet voice.', ['quiet voice', 'waiting your turn']),
   ('Is it safe to walk around while the bus is moving?', ['no'])],
  [('Why should riders stay seated on a moving bus?', ['To stay safe while the bus is moving', 'Sitting down is never important', 'Standing is always safer', 'Buses never move'], 0),
   ('Which of these shows polite behaviour on a bus?', ['Using a quiet voice', 'Yelling loudly the whole ride', 'Pushing other riders', 'Ignoring the bus driver completely'], 0),
   ('Why do bus riders wait for their turn to get on and off?', ['So everyone can board and exit safely', 'Waiting is never necessary', 'Only the first rider matters', 'Turns are not important on a bus'], 0),
   ('What should you do if the bus driver gives an instruction?', ['Listen and follow it', 'Ignore it completely', 'Argue with the driver', 'Cover your ears'], 0),
   ('Being safe and polite on a bus helps keep everyone ___.', ['Comfortable and safe', 'Confused', 'In danger', 'Upset with each other'], 0)])

# ─── DAY 85 ─────────────────────────────────────────────────────────────────
d85_lang = sub('Language', 'Punctuation: Question Marks for Asking',
  'Students learn that a question mark is used at the end of a sentence that asks something, such as What is your name?, instead of a calm period.',
  [('What punctuation mark is used at the end of a sentence that asks something?', ['question mark']),
   ('Does the sentence What is your name? ask a question or tell a fact?', ['ask a question', 'asks a question']),
   ('Which punctuation mark ends a sentence that tells a fact instead of asking?', ['period'])],
  [('What punctuation mark ends a sentence that asks something?', ['Question mark', 'Period', 'Exclamation mark', 'Comma'], 0),
   ('Which of these sentences would end with a question mark?', ['Where is my hat?', 'The sky is blue.', 'Watch out!', 'I like apples.'], 0),
   ('A sentence that asks something is called a ___.', ['Question', 'Command', 'Statement', 'Exclamation'], 0),
   ('Which punctuation mark would best end the sentence Do you like pizza', ['Question mark', 'Period', 'Nothing at all', 'Exclamation mark only'], 0),
   ('Question marks help readers know a sentence is ___.', ['Asking something', 'Shouting loudly', 'Giving a command', 'Telling a plain fact'], 0)])

d85_math = sub('Math', 'Skip Counting by 5s to 100',
  'Students practise counting forward by 5s, such as 5, 10, 15, 20, all the way up to 100, building on earlier skip-counting skills.',
  [('If you skip count by 5s, what comes after 5?', ['10', 'ten']),
   ('If you skip count by 5s, what comes after 20?', ['25', 'twenty-five']),
   ('What number comes right before 100 when skip counting by 5s?', ['95', 'ninety-five'])],
  [('If you skip count by 5s starting at 5, what comes after 15?', ['20', '16', '25', '10'], 0),
   ('If you skip count by 5s, what comes after 45?', ['50', '46', '55', '40'], 0),
   ('What number comes right before 100 when skip counting by 5s?', ['95', '90', '99', '85'], 0),
   ('Skip counting by 5s means counting forward by adding ___ each time.', ['5', '1', '10', '2'], 0),
   ('Which of these numbers would you say while skip counting by 5s?', ['30', '32', '28', '33'], 0)])

d85_sci = sub('Science', 'States of Matter: Solid, Liquid, and Gas',
  'Students learn that matter can be a solid, like a rock, a liquid, like water, or a gas, like the air we breathe, and that each state looks and behaves differently.',
  [('Name one example of a solid, like a rock or a block.', ['rock', 'block', 'a rock']),
   ('Name one example of a liquid, like water or juice.', ['water', 'juice', 'a liquid']),
   ('Is the air we breathe a solid, liquid, or gas?', ['gas'])],
  [('Which of these is an example of a solid?', ['A rock', 'Water', 'Air', 'Steam'], 0),
   ('Which of these is an example of a liquid?', ['Water', 'A rock', 'A block', 'A toy'], 0),
   ('Is the air we breathe a solid, liquid, or gas?', ['Gas', 'Solid', 'Liquid', 'None of these'], 0),
   ('How is a solid different from a liquid?', ['A solid keeps its shape, while a liquid can flow and change shape', 'A solid can flow like water', 'A liquid always stays completely still', 'There is no difference at all'], 0),
   ('Matter can exist in these three states: solid, liquid, and ___.', ['Gas', 'Colour', 'Sound', 'Shadow'], 0)])

d85_ss = sub('SocialStudies', 'Grandparents: Learning from Our Elders',
  'Students learn that grandparents and other elders in a family often share stories, wisdom, and traditions that help younger family members learn about the past.',
  [('Name a family member who is often older, like a grandparent.', ['grandparent', 'grandma', 'grandpa']),
   ('Can grandparents share stories about the past with us?', ['yes']),
   ('What word describes learning from someone older and wiser, like a grandparent?', ['learning from elders', 'wisdom'])],
  [('Who are grandparents?', ['Older family members who can share stories and wisdom', 'Strangers we never know', 'Only characters in books', 'People with no connection to our family'], 0),
   ('What might a grandparent share with a younger family member?', ['Stories and family traditions', 'Nothing at all', 'Only silence', 'Random facts about strangers'], 0),
   ('Why is it valuable to listen to our elders, like grandparents?', ['They can teach us about the past and share helpful wisdom', 'Elders never have anything useful to share', 'Listening to elders is not important', 'Grandparents know nothing about our family'], 0),
   ('Which of these shows respect for a grandparent?', ['Listening carefully to their stories', 'Ignoring them completely', 'Interrupting them constantly', 'Walking away while they speak'], 0),
   ('Learning from our elders helps us understand our familys ___.', ['History and traditions', 'Future only', 'Nothing important', 'Least important details'], 0)])

# ─── DAY 86 ─────────────────────────────────────────────────────────────────
d86_lang = sub('Language', 'Print Concepts: Spaces Between Words',
  'Students learn that in written sentences, small spaces separate one word from the next, helping readers know where one word ends and another begins.',
  [('What do we call the small gaps that separate one written word from the next?', ['spaces']),
   ('Do spaces help readers know where one word ends and another begins?', ['yes']),
   ('If there were no spaces between words, would reading be easier or harder?', ['harder'])],
  [('What separates one written word from the next?', ['A space', 'A picture', 'A number', 'A colour'], 0),
   ('Why are spaces between words important for readers?', ['They show where one word ends and the next begins', 'Spaces make reading harder', 'Spaces have no purpose at all', 'Spaces are only used in pictures'], 0),
   ('If a sentence had no spaces between its words, what would happen?', ['It would be much harder to read', 'It would be exactly the same to read', 'It would be easier to read', 'Nothing would change at all'], 0),
   ('Which of these correctly shows spaces between words?', ['I see a cat', 'Iseeacat', 'I  see    a cat', 'Isee acat'], 0),
   ('Print concepts, like spaces between words, help beginning readers ___.', ['Understand how written language works', 'Forget how to read', 'Avoid reading altogether', 'Only look at pictures'], 0)])

d86_math = sub('Math', 'Time: Morning, Afternoon, and Night',
  'Students learn to describe parts of the day as morning, afternoon, or night, and connect daily activities, like eating breakfast or going to sleep, to the correct part of the day.',
  [('Do we usually eat breakfast in the morning or at night?', ['morning']),
   ('Do we usually go to sleep in the afternoon or at night?', ['night']),
   ('Is lunchtime usually part of the morning or the afternoon?', ['afternoon'])],
  [('When do we usually eat breakfast?', ['In the morning', 'At night', 'Never', 'Only on weekends'], 0),
   ('When do we usually go to sleep?', ['At night', 'In the morning', 'At lunchtime', 'Never'], 0),
   ('Which activity usually happens in the afternoon?', ['Eating lunch', 'Sleeping all night', 'Waking up for the first time', 'Eating breakfast'], 0),
   ('Putting the day in order, which comes first: morning, afternoon, or night?', ['Morning', 'Night', 'Afternoon', 'They happen at the same time'], 0),
   ('Describing the parts of a day helps us understand ___.', ['The order that daily events happen in', 'Only what happens on weekends', 'Nothing useful about our day', 'Only nighttime activities'], 0)])

d86_sci = sub('Science', 'Our Brain: The Body Control Centre',
  'Students learn that the brain is inside our head and acts like a control centre, helping us think, move, feel, and remember things.',
  [('What body part acts like a control centre inside our head?', ['brain', 'the brain']),
   ('Name one thing our brain helps us do, like think or move.', ['think', 'move', 'remember']),
   ('Is our brain located inside our head or inside our foot?', ['inside our head', 'our head'])],
  [('What body part is like a control centre inside our head?', ['Brain', 'Elbow', 'Toe', 'Hair'], 0),
   ('Which of these does our brain help us do?', ['Think and remember', 'Only grow taller', 'Only make loud sounds', 'Nothing at all'], 0),
   ('Where is our brain located?', ['Inside our head', 'Inside our foot', 'Outside our body', 'Inside our hand'], 0),
   ('Why is the brain an important body part?', ['It helps control thinking, moving, and feeling', 'It has no real job', 'It only helps us taste food', 'It only helps us hear sounds'], 0),
   ('Our brain is best described as our bodys ___.', ['Control centre', 'Least useful part', 'Only decoration', 'Food storage'], 0)])

d86_ss = sub('SocialStudies', 'Cultural Celebrations Around the World',
  'Students learn that families around the world celebrate different cultural festivals, such as Lunar New Year and Diwali, often with special foods, clothing, and traditions.',
  [('Name one cultural celebration families might enjoy, like Lunar New Year.', ['Lunar New Year', 'Diwali']),
   ('Do different cultures often celebrate with special foods and clothing?', ['yes']),
   ('Is it kind to be curious and respectful about a friends cultural celebration?', ['yes'])],
  [('What is a cultural celebration?', ['A special festival that a group of people celebrates together', 'A random day with no meaning', 'A day when nothing happens', 'A rule about traffic safety'], 0),
   ('Which of these is an example of a cultural celebration?', ['Lunar New Year', 'A regular Tuesday', 'A trip to the store', 'A nap time'], 0),
   ('Why might families wear special clothing during a cultural celebration?', ['It is part of honouring their traditions', 'Special clothing has no meaning', 'Celebrations never involve clothing', 'It is only for random reasons'], 0),
   ('How should we respond when a friend shares about their cultural celebration?', ['With curiosity and respect', 'By ignoring them', 'By laughing unkindly', 'By refusing to listen'], 0),
   ('Learning about different cultural celebrations helps us ___.', ['Understand and respect our differences', 'Judge people unfairly', 'Ignore other cultures completely', 'Avoid learning anything new'], 0)])

# ─── DAY 87 ─────────────────────────────────────────────────────────────────
d87_lang = sub('Language', 'Time Order Words: Yesterday, Today, and Tomorrow',
  'Students learn that yesterday describes a day that already happened, today describes the day happening right now, and tomorrow describes the day that is coming next.',
  [('Does the word yesterday describe a day that already happened or one that is coming?', ['already happened', 'a day that already happened']),
   ('Does the word today describe the day happening right now?', ['yes']),
   ('Does the word tomorrow describe a day that already happened or one that is coming?', ['one that is coming', 'coming next'])],
  [('What word describes a day that already happened?', ['Yesterday', 'Today', 'Tomorrow', 'Never'], 0),
   ('What word describes the day happening right now?', ['Today', 'Yesterday', 'Tomorrow', 'Always'], 0),
   ('What word describes the day that is coming next?', ['Tomorrow', 'Yesterday', 'Today', 'Never'], 0),
   ('Putting these in order, which comes first: yesterday, today, or tomorrow?', ['Yesterday', 'Tomorrow', 'Today', 'They all happen at once'], 0),
   ('Time order words like yesterday and tomorrow help us understand ___.', ['When events happen in relation to today', 'Only how tall something is', 'Only what colour something is', 'Nothing useful at all'], 0)])

d87_math = sub('Math', 'Addition: Adding Three Numbers Together',
  'Students practise adding three small numbers together, such as 2 plus 3 plus 1, by combining any two numbers first and then adding the third.',
  [('What is 2 plus 3 plus 1?', ['6', 'six']),
   ('What is 1 plus 1 plus 1?', ['3', 'three']),
   ('What is 4 plus 2 plus 2?', ['8', 'eight'])],
  [('What is 2 plus 2 plus 2?', ['6', '4', '8', '5'], 0),
   ('What is 1 plus 3 plus 2?', ['6', '5', '7', '4'], 0),
   ('What is 5 plus 1 plus 1?', ['7', '6', '8', '5'], 0),
   ('When adding three numbers, you can add any two first and then add the ___.', ['Third number', 'Same number twice', 'Largest number only', 'Answer again'], 0),
   ('What is 3 plus 3 plus 1?', ['7', '6', '8', '9'], 0)])

d87_sci = sub('Science', 'Grassland Habitats: Wide Open Spaces',
  'Students learn that a grassland is a habitat with wide open spaces covered mostly in grass and few trees, home to animals such as zebras, lions, and prairie dogs.',
  [('Is a grassland habitat covered mostly in grass or covered mostly in ice?', ['grass', 'mostly in grass']),
   ('Name one animal that can live in a grassland, like a zebra.', ['zebra', 'lion', 'prairie dog']),
   ('Does a grassland usually have wide open spaces?', ['yes'])],
  [('What covers most of a grassland habitat?', ['Grass', 'Ice', 'Sand dunes only', 'Deep water'], 0),
   ('Which animal is well known for living in a grassland?', ['Zebra', 'Polar bear', 'Whale', 'Penguin'], 0),
   ('What is one feature of a grassland habitat?', ['Wide open spaces with few trees', 'Thick snow all year', 'Deep ocean water', 'Tall dense rainforest trees'], 0),
   ('Why can large animals like zebras roam easily in a grassland?', ['The wide open space gives them plenty of room to move', 'Grasslands have no open space at all', 'Zebras never move around', 'Grasslands are covered in solid ice'], 0),
   ('A grassland is an example of a ___.', ['Habitat', 'Story character', 'Number', 'Colour'], 0)])

d87_ss = sub('SocialStudies', 'Our Provinces and Territories: Parts of Canada',
  'Students learn that Canada is made up of different provinces and territories, each with its own name, and that all of them together make up our whole country.',
  [('What do we call the different parts that make up the country of Canada?', ['provinces and territories', 'provinces', 'territories']),
   ('Do all the provinces and territories together make up our whole country?', ['yes']),
   ('Name one province or territory in Canada, if you know one.', ['Ontario', 'Quebec', 'Alberta', 'British Columbia']),
  ],
  [('What do we call the different parts that make up Canada?', ['Provinces and territories', 'Countries', 'Continents', 'Oceans'], 0),
   ('What happens when all the provinces and territories are put together?', ['They make up our whole country', 'They make a different country', 'They disappear completely', 'They make up only one city'], 0),
   ('Which of these is a province in Canada?', ['Ontario', 'France', 'Japan', 'Egypt'], 0),
   ('Why is it helpful to learn about our provinces and territories?', ['It helps us understand how our country is organized', 'It has no connection to our country', 'Provinces have nothing to do with Canada', 'This concept is only about other countries'], 0),
   ('Canada is best described as a country made up of many ___.', ['Provinces and territories', 'Oceans only', 'Single cities only', 'Random unrelated places'], 0)])

# ─── DAY 88 ─────────────────────────────────────────────────────────────────
d88_lang = sub('Language', 'Character Traits: How a Character Acts',
  'Students learn that a character trait describes how a character usually behaves, such as being kind, brave, or silly, which is different from how a character feels at one moment.',
  [('Name one character trait, like kind, brave, or silly.', ['kind', 'brave', 'silly']),
   ('If a character always helps others, what trait might describe them?', ['kind', 'helpful']),
   ('Is a character trait about how they usually act, or about one moment only?', ['how they usually act', 'usually act'])],
  [('What is a character trait?', ['How a character usually behaves', 'The colour of a characters clothes', 'The title of the book', 'The name of the author'], 0),
   ('If a character always shares and helps friends, which trait describes them?', ['Kind', 'Mean', 'Lazy', 'Rude'], 0),
   ('Which of these is an example of a character trait?', ['Brave', 'Purple', 'Tuesday', 'Twelve'], 0),
   ('How is a character trait different from a characters feeling in one moment?', ['A trait describes how they usually act, not just one moment', 'A trait and a feeling are exactly the same thing', 'Traits only describe feelings, never actions', 'Character traits have no connection to how someone acts'], 0),
   ('Recognizing character traits helps readers understand ___.', ['What a character is usually like', 'Only the pictures in a book', 'Nothing about the story', 'Only the books title'], 0)])

d88_math = sub('Math', 'Estimating Length: About How Long Is It?',
  'Students practise estimating, or making a careful guess, about how long an object is before measuring it, such as guessing how many blocks long a book might be.',
  [('What word describes making a careful guess about how long something is?', ['estimating', 'estimate']),
   ('If you estimate a book is about 5 blocks long, is that a careful guess or an exact answer?', ['a careful guess', 'guess']),
   ('Should we estimate before or after we measure something exactly?', ['before'])],
  [('What does it mean to estimate the length of an object?', ['To make a careful guess before measuring exactly', 'To measure something perfectly every time', 'To ignore the object completely', 'To guess without any thought at all'], 0),
   ('If you estimate a pencil is about 3 blocks long, what have you done?', ['Made a careful guess about its length', 'Measured it perfectly', 'Ignored the pencil', 'Changed the pencils real length'], 0),
   ('Why might estimating length be a useful skill?', ['It helps us make a reasonable guess quickly before measuring exactly', 'Estimating is never useful', 'Estimating always gives the exact same answer as measuring', 'This concept has no connection to measurement'], 0),
   ('Which is more likely to be a good estimate for the length of a crayon?', ['About 2 blocks', 'About 200 blocks', 'About 2000 blocks', 'About 0 blocks'], 0),
   ('After estimating an objects length, what can we do to check how close our guess was?', ['Measure the object exactly', 'Ignore the object forever', 'Throw the object away', 'Guess again without measuring'], 0)])

d88_sci = sub('Science', 'Rainbows: Colours After the Rain',
  'Students learn that a rainbow can appear in the sky when sunlight shines through raindrops, spreading the light into many colours like red, orange, yellow, green, blue, and purple.',
  [('What natural event often happens right before we might see a rainbow?', ['rain']),
   ('Name one colour we might see in a rainbow, like red or blue.', ['red', 'blue', 'yellow', 'green', 'orange', 'purple']),
   ('Does sunlight shining through raindrops help create a rainbow?', ['yes'])],
  [('What weather event often happens before we see a rainbow?', ['Rain', 'Snow', 'Wind only', 'A clear night'], 0),
   ('What causes sunlight to spread into a rainbows many colours?', ['Sunlight shining through raindrops', 'Sunlight shining through rocks', 'The sound of thunder', 'Darkness at night'], 0),
   ('Which of these colours might you see in a rainbow?', ['Red', 'Black', 'Brown', 'Grey'], 0),
   ('Why do rainbows often appear after it rains?', ['Sunlight can shine through the raindrops still in the air', 'Rainbows have no connection to rain at all', 'Rainbows only appear on cloudy nights', 'Rain removes all light from the sky'], 0),
   ('A rainbow is best described as sunlight being spread into many ___.', ['Colours', 'Shapes', 'Sounds', 'Smells'], 0)])

d88_ss = sub('SocialStudies', 'Welcoming New Neighbours: Being Kind to Newcomers',
  'Students learn that when a new family moves into the neighbourhood, being welcoming and kind, such as saying hello or offering to help, makes newcomers feel included.',
  [('What should we do to make a new neighbour feel included, like saying hello?', ['say hello', 'be kind']),
   ('Is it kind or unkind to ignore a new family who just moved in?', ['unkind']),
   ('Can offering to help a new neighbour make them feel welcome?', ['yes'])],
  [('What is a good way to make a new neighbour feel welcome?', ['Saying hello and offering to help', 'Ignoring them completely', 'Being unkind to them', 'Refusing to speak with them'], 0),
   ('Why might a new family feel nervous when they first move to a neighbourhood?', ['Everything and everyone around them is unfamiliar at first', 'New families never feel nervous', 'Moving to a new place has no effect on feelings', 'This concept has no connection to being new'], 0),
   ('Which of these shows kindness to a newcomer?', ['Introducing yourself and offering to help', 'Whispering unkindly about them', 'Refusing to include them in games', 'Walking away without saying anything'], 0),
   ('How might welcoming a new neighbour help the whole community?', ['It can help the newcomer feel included and build a stronger community', 'Welcoming newcomers never helps a community', 'New neighbours should always be avoided', 'This concept has no connection to community life'], 0),
   ('Being kind to newcomers helps build a community that feels ___.', ['Welcoming and included', 'Cold and unfriendly', 'Confusing', 'Unsafe'], 0)])

# ─── DAY 89 ─────────────────────────────────────────────────────────────────
d89_lang = sub('Language', 'Poetry: Simple Rhymes and Rhythm',
  'Students learn that a poem often uses rhyming words and a steady rhythm, or beat, to make the words sound musical and fun to say aloud.',
  [('Do poems often use words that rhyme with each other?', ['yes']),
   ('What word describes the steady beat we hear in a poem?', ['rhythm']),
   ('Is reading a poem aloud often fun because of its rhythm and rhyme?', ['yes'])],
  [('What do many poems use to sound musical?', ['Rhyming words and rhythm', 'Only silence', 'Only numbers', 'Only pictures'], 0),
   ('What word describes the steady beat felt in a poem?', ['Rhythm', 'Chapter', 'Cover', 'Index'], 0),
   ('Which of these lines shows rhyming words?', ['The cat sat on a mat', 'The cat sat on a chair', 'The dog ran in the yard', 'The bird flew over the house'], 0),
   ('Why might reading a poem aloud feel different from reading a plain sentence?', ['A poems rhythm and rhyme can make it sound musical and fun', 'Poems are always silent when read aloud', 'Poems never use any rhythm at all', 'Poems and plain sentences always sound identical'], 0),
   ('Poetry often uses rhyme and rhythm to make words feel ___.', ['Musical and fun to say', 'Boring and flat', 'Impossible to read', 'Completely silent'], 0)])

d89_math = sub('Math', 'Repeating Patterns: Predicting What Comes Next',
  'Students practise looking at a repeating pattern, such as circle, square, circle, square, and predicting which shape or colour should come next in the sequence.',
  [('In the pattern circle, square, circle, square, what comes next?', ['circle', 'a circle']),
   ('In the pattern red, blue, red, blue, red, what comes next?', ['blue', 'a blue']),
   ('What do we call guessing what comes next in a pattern?', ['predicting', 'prediction'])],
  [('In the pattern star, moon, star, moon, what comes next?', ['Star', 'Moon', 'Sun', 'Cloud'], 0),
   ('In the pattern 1, 2, 1, 2, 1, what comes next?', ['2', '1', '3', '0'], 0),
   ('What do we call guessing what comes next in a repeating pattern?', ['Predicting', 'Forgetting', 'Erasing', 'Ignoring'], 0),
   ('In the pattern green, green, yellow, green, green, yellow, what comes next?', ['Green', 'Yellow', 'Blue', 'Red'], 0),
   ('Predicting what comes next in a pattern helps us understand that patterns ___.', ['Repeat in a predictable way', 'Never repeat at all', 'Are always random', 'Have no order at all'], 0)])

d89_sci = sub('Science', 'Sound: Loud, Quiet, High, and Low',
  'Students learn that sounds can be loud or quiet, and also high or low, and that different objects, like a drum or a whistle, make different kinds of sounds.',
  [('Name one word that describes a very soft sound, like a whisper.', ['quiet', 'soft']),
   ('Name one word that describes a very noisy sound, like a shout.', ['loud']),
   ('Does a whistle usually make a high sound or a low sound?', ['high'])],
  [('Which word describes a very soft sound?', ['Quiet', 'Loud', 'Bright', 'Heavy'], 0),
   ('Which word describes a very noisy sound?', ['Loud', 'Quiet', 'Dim', 'Soft'], 0),
   ('Does a whistle usually make a high sound or a low sound?', ['High', 'Low', 'No sound at all', 'Cannot tell'], 0),
   ('Which of these is likely to make a loud sound?', ['A drum being banged', 'A feather falling', 'A leaf resting on grass', 'A whisper'], 0),
   ('Sounds can be described using these two pairs of words: loud and quiet, high and ___.', ['Low', 'Colourful', 'Heavy', 'Bright'], 0)])

d89_ss = sub('SocialStudies', 'Weather Around the World: Hot and Cold Places',
  'Students learn that different places around the world have very different weather, with some places, like deserts, being very hot, and others, like the Arctic, being very cold.',
  [('Name one place in the world that is usually very hot, like a desert.', ['desert']),
   ('Name one place in the world that is usually very cold, like the Arctic.', ['Arctic', 'the Arctic']),
   ('Do different places around the world have different weather?', ['yes'])],
  [('Which of these places is usually very hot?', ['A desert', 'The Arctic', 'The North Pole', 'A snowy mountain'], 0),
   ('Which of these places is usually very cold?', ['The Arctic', 'A desert', 'A tropical beach', 'A rainforest'], 0),
   ('Why might people in hot places dress differently than people in cold places?', ['They need clothing suited to their own local weather', 'Clothing has no connection to weather', 'Everyone in the world wears the exact same clothing', 'Weather never changes what people wear'], 0),
   ('Learning about weather around the world helps us understand that ___.', ['Different places can have very different climates', 'Every place has the exact same weather', 'Weather never changes anywhere', 'Only one kind of weather exists on Earth'], 0),
   ('Comparing hot and cold places around the world is an example of learning about ___.', ['Our world and its different climates', 'Only our own neighbourhood', 'A make-believe story', 'Numbers and counting'], 0)])

# ─── DAY 90 (Review) ────────────────────────────────────────────────────────
d90_lang = sub('Language', 'Language Review: Word Families, Blends, and Poetry',
  'Students review recent Language skills: the -ig and -ug word families, beginning blends, rhyming, question marks, spaces between words, time order words, character traits, and poetry.',
  [('Change the b in big to p. What new word do you make?', ['pig']),
   ('What two letters blend together at the start of the word black?', ['bl']),
   ('What punctuation mark is used at the end of a sentence that asks something?', ['question mark'])],
  [('Which word rhymes with big?', ['Pig', 'Dog', 'Sun', 'Cup'], 0),
   ('Which word begins with the blend st?', ['Stop', 'Man', 'Pig', 'Dog'], 0),
   ('What punctuation mark ends a sentence that asks something?', ['Question mark', 'Period', 'Exclamation mark', 'Comma'], 0),
   ('What is a character trait?', ['How a character usually behaves', 'The colour of a characters clothes', 'The title of the book', 'The name of the author'], 0),
   ('What do many poems use to sound musical?', ['Rhyming words and rhythm', 'Only silence', 'Only numbers', 'Only pictures'], 0)])

d90_math = sub('Math', 'Math Review: Place Value, Facts, and Patterns',
  'Students review recent Math skills: tens and ones, fact families, composing shapes, sorting data, skip counting by 5s, adding three numbers, estimating length, and repeating patterns.',
  [('How many tens are in the number 14?', ['1', 'one']),
   ('If 3 plus 4 equals 7, what does 7 minus 4 equal?', ['3', 'three']),
   ('What is 2 plus 3 plus 1?', ['6', 'six'])],
  [('How many tens are in the number 12?', ['1', '2', '0', '3'], 0),
   ('If 2 plus 5 equals 7, what does 7 minus 5 equal?', ['2', '5', '7', '0'], 0),
   ('If you skip count by 5s starting at 5, what comes after 15?', ['20', '16', '25', '10'], 0),
   ('What is 2 plus 2 plus 2?', ['6', '4', '8', '5'], 0),
   ('In the pattern star, moon, star, moon, what comes next?', ['Star', 'Moon', 'Sun', 'Cloud'], 0)])

d90_sci = sub('Science', 'Science Review: Bodies, Habitats, and States of Matter',
  'Students review recent Science topics: our skin, animal babies, seeds, simple machines, states of matter, our brain, grasslands, rainbows, and sound.',
  [('What body part covers our whole body?', ['skin']),
   ('What tiny object holds everything a new plant needs to grow?', ['seed', 'a seed']),
   ('What body part is like a control centre inside our head?', ['brain', 'the brain'])],
  [('Which animal baby is born live?', ['Puppy', 'Chick', 'Turtle', 'Snake'], 0),
   ('What simple machine uses a bar and a support point to lift things?', ['A lever', 'A pulley', 'A wheel only', 'A ramp'], 0),
   ('Which of these is an example of a solid?', ['A rock', 'Water', 'Air', 'Steam'], 0),
   ('Which animal is well known for living in a grassland?', ['Zebra', 'Polar bear', 'Whale', 'Penguin'], 0),
   ('Which word describes a very soft sound?', ['Quiet', 'Loud', 'Bright', 'Heavy'], 0)])

d90_ss = sub('SocialStudies', 'Social Studies Review: Helpers, Leaders, and Our World',
  'Students review recent Social Studies topics: librarians, mayors, community gardens, bus safety, grandparents, cultural celebrations, provinces and territories, welcoming newcomers, and world weather.',
  [('Who helps people find books at the library?', ['librarian']),
   ('What do we call the person chosen to help lead a town or city?', ['mayor']),
   ('What do we call the different parts that make up Canada?', ['provinces and territories', 'provinces', 'territories'])],
  [('What is a community garden?', ['A shared space where neighbours grow food together', 'A garden owned by only one family', 'A store that sells toys', 'A place with no plants at all'], 0),
   ('Why should riders stay seated on a moving bus?', ['To stay safe while the bus is moving', 'Sitting down is never important', 'Standing is always safer', 'Buses never move'], 0),
   ('Which of these is an example of a cultural celebration?', ['Lunar New Year', 'A regular Tuesday', 'A trip to the store', 'A nap time'], 0),
   ('What is a good way to make a new neighbour feel welcome?', ['Saying hello and offering to help', 'Ignoring them completely', 'Being unkind to them', 'Refusing to speak with them'], 0),
   ('Which of these places is usually very hot?', ['A desert', 'The Arctic', 'The North Pole', 'A snowy mountain'], 0)])


g0_81_90 = [
    day(81, [d81_lang, d81_math, d81_sci, d81_ss]),
    day(82, [d82_lang, d82_math, d82_sci, d82_ss]),
    day(83, [d83_lang, d83_math, d83_sci, d83_ss]),
    day(84, [d84_lang, d84_math, d84_sci, d84_ss]),
    day(85, [d85_lang, d85_math, d85_sci, d85_ss]),
    day(86, [d86_lang, d86_math, d86_sci, d86_ss]),
    day(87, [d87_lang, d87_math, d87_sci, d87_ss]),
    day(88, [d88_lang, d88_math, d88_sci, d88_ss]),
    day(89, [d89_lang, d89_math, d89_sci, d89_ss]),
    day(90, [d90_lang, d90_math, d90_sci, d90_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_81_90)
    append_worksheet_days(0, g0_81_90)
