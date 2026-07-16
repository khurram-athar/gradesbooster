#!/usr/bin/env python3
"""Grade 1, Days 41-50 -- SECOND batch extending Grade 1 past Day 40.
Self-contained script modeled exactly on gen_grade1_days31_40.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-40 topics (see data/grade1.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260825):
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
d41_lang = sub('Language', 'Consonant Blends: br, cr, dr, gr',
  'Students learn that two consonants can blend together at the start of a word, such as br in brush, cr in crab, dr in drum, and gr in grape.',
  [('What two letters blend together at the start of the word brush?', ['br']),
   ('What two letters blend together at the start of the word crab?', ['cr']),
   ('Say the word drum. What two letters blend at the start?', ['dr'])],
  [('Which word begins with the blend br?', ['Brush', 'Cat', 'Dog', 'Run'], 0),
   ('Which word begins with the blend cr?', ['Crab', 'Sun', 'Pig', 'Hat'], 0),
   ('Which word begins with the blend dr?', ['Drum', 'Top', 'Man', 'Sit'], 0),
   ('Which word begins with the blend gr?', ['Grape', 'Cat', 'Bed', 'Sun'], 0),
   ('A beginning blend is when two consonant letters ___.', ['Are silent', 'Blend their sounds together at the start of a word', 'Turn into vowels', 'Are never used'], 1)])

d41_math = sub('Math', 'Addition and Subtraction Fact Families',
  'Students learn that a fact family is a group of related addition and subtraction facts that use the same three numbers, such as 3 add 4 equals 7, 4 add 3 equals 7, 7 minus 3 equals 4, and 7 minus 4 equals 3.',
  [('If 3 add 4 equals 7, what is 7 minus 4?', ['3', 'three']),
   ('Name the three numbers in the fact family 2, 5, and 7.', ['2, 5, 7', '2 5 7', 'two five seven']),
   ('If 6 add 2 equals 8, what is 8 minus 2?', ['6', 'six'])],
  [('Which subtraction fact belongs to the same fact family as 3 add 4 equals 7?', ['7 minus 3 equals 4', '8 minus 1 equals 7', '5 minus 2 equals 3', '9 minus 4 equals 5'], 0),
   ('A fact family uses how many different numbers?', ['2', '3', '4', '5'], 1),
   ('Which addition fact belongs to the same fact family as 8 minus 5 equals 3?', ['5 add 3 equals 8', '4 add 4 equals 8', '6 add 2 equals 8', '7 add 1 equals 8'], 0),
   ('If 6 add 3 equals 9, which subtraction fact is in the same family?', ['9 minus 6 equals 3', '9 minus 2 equals 7', '8 minus 3 equals 5', '7 minus 3 equals 4'], 0),
   ('Knowing a fact family helps us because ___.', ['Related addition and subtraction facts share the same numbers', 'All numbers are the same anyway', 'Subtraction and addition are never related', 'Fact families only work for even numbers'], 0)])

d41_sci = sub('Science', 'Taking Care of Our Bodies: Exercise and Rest',
  'Students learn that staying healthy means being active with exercise, such as running or playing, and also getting enough rest and sleep each night.',
  [('Name one way to exercise, like running or jumping.', ['running', 'jumping', 'playing', 'walking']),
   ('About how many hours of sleep should a child get each night?', ['10', 'ten', 'about 10 hours', '10 hours']),
   ('Why does our body need rest?', ['to grow and stay healthy', 'to rest and grow', 'to feel better'])],
  [('Which of these is a way to exercise your body?', ['Running', 'Sleeping all day', 'Watching only', 'Sitting still all day'], 0),
   ('Why is exercise good for your body?', ['It helps keep your body strong and healthy', 'It makes your body weaker', 'It has no effect on your body', 'It only helps your hair grow'], 0),
   ('Why do people need to sleep at night?', ['To help the body rest and grow', 'To make the body tired forever', 'Sleep is not needed', 'To stop the body from growing'], 0),
   ('About how many hours of sleep does a young child usually need each night?', ['2 hours', '5 hours', '10 hours', '20 hours'], 2),
   ('Which of these is a healthy balance for a growing body?', ['Exercise and rest', 'Only exercise, no rest', 'Only rest, no exercise', 'Neither exercise nor rest'], 0)])

d41_ss = sub('SocialStudies', 'Farms and Where Our Food Comes From',
  'Students learn that many foods, such as fruits, vegetables, milk, and eggs, come from farms, and that farmers grow crops and raise animals to help feed communities.',
  [('Name one food that comes from a farm, like an egg or an apple.', ['egg', 'apple', 'milk', 'vegetables']),
   ('What do we call a person who grows crops and raises animals for food?', ['farmer']),
   ('Name one animal that might live on a farm, like a cow or chicken.', ['cow', 'chicken', 'pig', 'sheep'])],
  [('Which of these foods usually comes from a farm?', ['Milk', 'A plastic toy', 'A rock', 'A cloud'], 0),
   ('What do we call a person whose job is to grow crops and raise animals?', ['A farmer', 'A pilot', 'A dentist', 'A librarian'], 0),
   ('Which of these animals is commonly raised on a farm?', ['A cow', 'A shark', 'A polar bear', 'A penguin'], 0),
   ('Why are farms important to communities?', ['They grow and raise much of the food people eat', 'Farms do not help communities', 'Farms only grow flowers', 'Farms have no purpose'], 0),
   ('Which of these is something a farmer might grow in a field?', ['Wheat', 'A car', 'A computer', 'A television'], 0)])

# ─── DAY 42 ─────────────────────────────────────────────────────────────────
d42_lang = sub('Language', 'Ending Blends: st, nd, nt, mp',
  'Students learn that two consonants can blend together at the end of a word, such as st in nest, nd in hand, nt in tent, and mp in lamp.',
  [('What two letters blend together at the end of the word nest?', ['st']),
   ('What two letters blend together at the end of the word hand?', ['nd']),
   ('Say the word lamp. What two letters blend at the end?', ['mp'])],
  [('Which word ends with the blend st?', ['Nest', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word ends with the blend nd?', ['Top', 'Hand', 'Pig', 'Bed'], 1),
   ('Which word ends with the blend nt?', ['Tent', 'Man', 'Sit', 'Run'], 0),
   ('Which word ends with the blend mp?', ['Lamp', 'Cat', 'Sun', 'Bed'], 0),
   ('An ending blend is when two consonant letters ___.', ['Blend their sounds together at the end of a word', 'Are always silent', 'Turn into vowels', 'Never appear together'], 0)])

d42_math = sub('Math', 'Doubles Facts in Addition',
  'Students learn doubles facts, addition facts where both addends are the same number, such as 2 add 2 equals 4 and 5 add 5 equals 10, as a quick way to add.',
  [('What is 3 add 3?', ['6', 'six']),
   ('What is 5 add 5?', ['10', 'ten']),
   ('What is 4 add 4?', ['8', 'eight'])],
  [('What is 2 add 2?', ['2', '3', '4', '5'], 2),
   ('What is 6 add 6?', ['10', '11', '12', '13'], 2),
   ('A doubles fact is when ___.', ['Both numbers being added are the same', 'The two numbers are always different', 'One number is zero', 'The sum is always ten'], 0),
   ('What is 7 add 7?', ['12', '13', '14', '15'], 2),
   ('Which of these is a doubles fact?', ['4 add 4', '3 add 5', '2 add 6', '1 add 7'], 0)])

d42_sci = sub('Science', 'Healthy Eating and Food Groups',
  'Students learn that healthy eating means choosing foods from different groups, such as fruits, vegetables, grains, and protein foods, to help the body grow strong.',
  [('Name one fruit that is healthy to eat, like an apple or banana.', ['apple', 'banana', 'orange', 'grapes']),
   ('Name one vegetable that is healthy to eat, like a carrot.', ['carrot', 'broccoli', 'peas']),
   ('Why is it important to eat a variety of healthy foods?', ['to help the body grow strong', 'to stay healthy', 'to grow strong'])],
  [('Which of these is a healthy fruit?', ['An apple', 'A candy bar', 'A soda', 'A lollipop'], 0),
   ('Which of these is a healthy vegetable?', ['Broccoli', 'Chips', 'Cookies', 'Candy'], 0),
   ('Why do we eat foods from different food groups?', ['To help our bodies grow strong and stay healthy', 'Food groups do not matter', 'To make us feel sick', 'Eating only one food is best'], 0),
   ('Which of these is an example of a grain food?', ['Bread', 'A rock', 'A balloon', 'A toy car'], 0),
   ('Eating a variety of healthy foods each day is called eating a ___.', ['Balanced diet', 'Broken diet', 'Empty plate', 'Single food'], 0)])

d42_ss = sub('SocialStudies', 'Local Government: Our Town Leaders',
  'Students learn that towns and cities have leaders, such as a mayor and council, who help make decisions and take care of the community.',
  [('What do we call the elected leader of a city or town?', ['mayor']),
   ('Name one thing a town leader might help decide, like building a park.', ['building a park', 'fixing roads', 'building a school']),
   ('Do town leaders help take care of the community?', ['yes'])],
  [('What is the title of an elected leader of a city or town?', ['Mayor', 'Farmer', 'Dentist', 'Pilot'], 0),
   ('What does a town or city government help do?', ['Take care of the community and make decisions', 'Nothing at all', 'Only sell food', 'Only build houses'], 0),
   ('Which of these is something a local government might take care of?', ['Roads and parks', 'Outer space', 'The ocean floor', 'The weather'], 0),
   ('Why do towns and cities need leaders?', ['To help make decisions and take care of the community', 'Leaders are not needed', 'To confuse people', 'To build spaceships'], 0),
   ('A group of people who help a mayor make decisions is called a ___.', ['Council', 'Herd', 'Flock', 'Choir'], 0)])

# ─── DAY 43 ─────────────────────────────────────────────────────────────────
d43_lang = sub('Language', 'Vowel Teams: ai and ay',
  'Students learn that the letters ai and ay can work together as a vowel team to make the long a sound, as in rain and day.',
  [('What two letters make the long a sound in the word rain?', ['ai']),
   ('What two letters make the long a sound in the word day?', ['ay']),
   ('Name one word that has the ai vowel team, like rain or train.', ['rain', 'train', 'paint', 'mail'])],
  [('Which letters make the long a sound in the word rain?', ['ai', 'ay', 'ee', 'oa'], 0),
   ('Which letters make the long a sound in the word day?', ['ai', 'ay', 'oa', 'ee'], 1),
   ('Which word has the ai vowel team?', ['Train', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ay vowel team?', ['Play', 'Cat', 'Dog', 'Sun'], 0),
   ('A vowel team is two vowel letters that work together to make ___.', ['One sound', 'Two separate sounds', 'No sound at all', 'A consonant sound'], 0)])

d43_math = sub('Math', 'Skip Counting by 3s',
  'Students practise skip counting by 3s, saying the numbers 3, 6, 9, 12, and so on, to build number sense and prepare for multiplication.',
  [('What number comes after 6 when skip counting by 3s?', ['9', 'nine']),
   ('What number comes after 12 when skip counting by 3s?', ['15', 'fifteen']),
   ('Start at 3 and skip count by 3s three times. What is the third number?', ['9', 'nine'])],
  [('When skip counting by 3s, what number comes after 3?', ['4', '5', '6', '7'], 2),
   ('When skip counting by 3s, what number comes after 9?', ['10', '11', '12', '13'], 2),
   ('Which of these lists shows skip counting by 3s?', ['3, 6, 9, 12', '3, 5, 7, 9', '3, 6, 8, 10', '2, 4, 6, 8'], 0),
   ('When skip counting by 3s, what number comes after 15?', ['16', '17', '18', '19'], 2),
   ('Skip counting by 3s means we count ___.', ['Every third number', 'Every second number', 'Backward only', 'Only even numbers'], 0)])

d43_sci = sub('Science', 'Germs and Staying Healthy',
  'Students learn that germs are tiny living things that can make people sick, and that washing hands and covering coughs are simple ways to stay healthy.',
  [('What do we call tiny living things that can make people sick?', ['germs']),
   ('Name one way to stop germs from spreading, like washing hands.', ['washing hands', 'covering a cough', 'covering a sneeze']),
   ('Should you wash your hands before eating?', ['yes'])],
  [('What are germs?', ['Tiny living things that can make people sick', 'Large rocks', 'A type of weather', 'A kind of plant'], 0),
   ('Which of these helps stop germs from spreading?', ['Washing your hands', 'Never washing your hands', 'Sharing food with someone who is sick', 'Touching your face often'], 0),
   ('What should you do when you cough or sneeze?', ['Cover your mouth', 'Cough on someone else', 'Do nothing', 'Cough into your open hand and touch things'], 0),
   ('Why is it important to wash your hands before eating?', ['It helps remove germs that could make you sick', 'Washing hands has no effect', 'It makes food taste better', 'It is not important'], 0),
   ('Which of these is a healthy habit that fights germs?', ['Washing hands with soap and water', 'Never washing hands', 'Sharing a toothbrush', 'Touching everything at the store'], 0)])

d43_ss = sub('SocialStudies', 'Canadian Currency: Our Coins and Bills',
  'Students learn that Canada has its own money, called currency, including coins such as the loonie and toonie and paper bills of different colours and values.',
  [('What is the name of the Canadian one dollar coin?', ['loonie']),
   ('What is the name of the Canadian two dollar coin?', ['toonie']),
   ('Name one form Canadian money can take, like a coin or a bill.', ['coin', 'bill', 'coins', 'bills'])],
  [('What is the name of the Canadian one dollar coin?', ['Loonie', 'Toonie', 'Nickel', 'Dime'], 0),
   ('What is the name of the Canadian two dollar coin?', ['Loonie', 'Toonie', 'Penny', 'Quarter'], 1),
   ('What do we call the money used in a country?', ['Currency', 'Weather', 'Language', 'Landmark'], 0),
   ('Besides coins, what other form does Canadian money take?', ['Paper bills', 'Rocks', 'Leaves', 'Shells'], 0),
   ('Why does Canada have its own currency?', ['So people can buy and sell goods and services', 'Currency is not needed', 'To decorate homes', 'To use as toys only'], 0)])

# ─── DAY 44 ─────────────────────────────────────────────────────────────────
d44_lang = sub('Language', 'Vowel Teams: oa and ow',
  'Students learn that the letters oa and ow can work together as a vowel team to make the long o sound, as in boat and snow.',
  [('What two letters make the long o sound in the word boat?', ['oa']),
   ('What two letters make the long o sound in the word snow?', ['ow']),
   ('Name one word that has the oa vowel team, like boat or coat.', ['boat', 'coat', 'road', 'goat'])],
  [('Which letters make the long o sound in the word boat?', ['oa', 'ow', 'ai', 'ee'], 0),
   ('Which letters make the long o sound in the word snow?', ['oa', 'ow', 'ay', 'oo'], 1),
   ('Which word has the oa vowel team?', ['Coat', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ow vowel team?', ['Grow', 'Cat', 'Dog', 'Sun'], 0),
   ('The oa and ow vowel teams both make the ___ sound.', ['Long o', 'Short a', 'Long e', 'Short i'], 0)])

d44_math = sub('Math', 'Number Bonds to 10',
  'Students explore number bonds to 10, learning the pairs of numbers that add together to make 10, such as 6 and 4, or 8 and 2.',
  [('What number pairs with 6 to make a number bond of 10?', ['4', 'four']),
   ('What number pairs with 8 to make a number bond of 10?', ['2', 'two']),
   ('What number pairs with 5 to make a number bond of 10?', ['5', 'five'])],
  [('Which number pairs with 7 to make 10?', ['1', '2', '3', '4'], 1),
   ('Which number pairs with 9 to make 10?', ['1', '2', '3', '4'], 0),
   ('Which pair of numbers makes a number bond of 10?', ['6 and 4', '5 and 4', '7 and 2', '3 and 5'], 0),
   ('Which number pairs with 5 to make 10?', ['4', '5', '6', '7'], 1),
   ('A number bond shows two numbers that combine to make ___.', ['A smaller number', 'A larger total', 'No total at all', 'A different shape'], 1)])

d44_sci = sub('Science', 'Air All Around Us',
  'Students learn that air is all around us even though we cannot see it, and that moving air, called wind, can push objects like leaves and kites.',
  [('Can you see the air around you?', ['no']),
   ('What do we call air that is moving?', ['wind']),
   ('Name one object that wind can move, like a kite or leaves.', ['kite', 'leaves', 'leaf'])],
  [('Can we usually see the air around us?', ['Yes, always', 'No, we cannot see it', 'Only at night', 'Only in winter'], 1),
   ('What do we call moving air?', ['Wind', 'Water', 'Soil', 'Sunlight'], 0),
   ('Which of these can wind move?', ['A kite', 'A mountain', 'The ocean floor', 'A building'], 0),
   ('How do we know air is really there even though we cannot see it?', ['We can feel it and see it move things like leaves', 'Air does not really exist', 'Air can be seen clearly', 'Air never moves'], 0),
   ('Which of these is a sign that wind is blowing?', ['Leaves moving on a tree', 'A rock sitting still', 'A closed door', 'A quiet, empty room'], 0)])

d44_ss = sub('SocialStudies', 'Saving and Spending Money Wisely',
  'Students learn the difference between saving money, keeping it for later, and spending money, using it to buy something now, and why both choices can be helpful.',
  [('What word describes keeping money to use later?', ['saving']),
   ('What word describes using money to buy something now?', ['spending']),
   ('Name one reason someone might save money, like buying something big later.', ['to buy something big later', 'to buy a toy later', 'for later'])],
  [('What does it mean to save money?', ['Keeping money to use later', 'Spending all money right away', 'Throwing money away', 'Losing money'], 0),
   ('What does it mean to spend money?', ['Keeping it forever', 'Using it to buy something now', 'Hiding it', 'Losing it'], 1),
   ('Why might someone choose to save money instead of spending it right away?', ['To buy something bigger later', 'Saving is never helpful', 'To lose it', 'Saving has no purpose'], 0),
   ('Where might someone keep money they are saving, like in a small container with a slot?', ['A piggy bank', 'A garden', 'A closet floor', 'A backpack pocket only'], 0),
   ('Making thoughtful choices about saving and spending money is called being ___ with money.', ['Wise', 'Careless', 'Wasteful', 'Confused'], 0)])

# ─── DAY 45 ─────────────────────────────────────────────────────────────────
d45_lang = sub('Language', 'Plural Nouns: Adding -s and -es',
  'Students learn that most nouns become plural, meaning more than one, by adding -s, as in cats, while some nouns need -es, as in boxes.',
  [('How do you make the word cat plural?', ['add s', 'cats', 'add -s']),
   ('How do you make the word box plural?', ['add es', 'boxes', 'add -es']),
   ('What does the word plural mean?', ['more than one'])],
  [('What does the word plural mean?', ['More than one', 'Only one', 'No amount at all', 'A colour'], 0),
   ('How do you usually make a noun plural?', ['Add -s or -es', 'Add -ing', 'Add -er', 'Remove a letter'], 0),
   ('What is the plural of the word dog?', ['Dogs', 'Doges', 'Dogies', 'Dogx'], 0),
   ('Which words need -es instead of just -s to become plural, like box?', ['Words ending in x, like box', 'All words', 'No words', 'Only short words'], 0),
   ('What is the plural of the word bus?', ['Bus', 'Buss', 'Buses', 'Busies'], 2)])

d45_math = sub('Math', 'Odd and Even Numbers',
  'Students learn to tell odd numbers, which cannot be split into two equal groups, from even numbers, which can be split into two equal groups, such as 4 being even and 5 being odd.',
  [('Is the number 4 odd or even?', ['even']),
   ('Is the number 7 odd or even?', ['odd']),
   ('Name one even number less than 10.', ['2', '4', '6', '8'])],
  [('Which of these numbers is even?', ['3', '4', '5', '7'], 1),
   ('Which of these numbers is odd?', ['2', '4', '6', '9'], 3),
   ('A number is even if it can be split into ___.', ['Two equal groups', 'Three equal groups', 'No groups at all', 'One large group'], 0),
   ('Which of these numbers is odd?', ['10', '11', '12', '14'], 1),
   ('Is 0 usually counted as an even or odd number?', ['Even', 'Odd', 'Neither', 'Both'], 0)])

d45_sci = sub('Science', 'Floating and Sinking',
  'Students explore why some objects float on water while others sink, testing objects such as a wooden block, a rock, and a rubber duck.',
  [('Does a rock usually float or sink in water?', ['sink']),
   ('Name one object that usually floats in water, like a rubber duck.', ['rubber duck', 'wood', 'a leaf']),
   ('Does a wooden block usually float or sink?', ['float'])],
  [('What happens when you drop a heavy rock into water?', ['It sinks', 'It floats', 'It disappears', 'It turns to ice'], 0),
   ('Which of these objects usually floats on water?', ['A rubber duck', 'A large rock', 'A metal spoon', 'A brick'], 0),
   ('What word describes an object that stays on top of the water?', ['Sinking', 'Floating', 'Melting', 'Freezing'], 1),
   ('What word describes an object that goes down to the bottom of the water?', ['Floating', 'Sinking', 'Growing', 'Melting'], 1),
   ('Why might a heavy metal spoon sink while a light rubber duck floats?', ['Heavy, dense objects tend to sink while light objects tend to float', 'All objects always float', 'All objects always sink', 'Weight has no effect on floating'], 0)])

d45_ss = sub('SocialStudies', 'Emergency Workers and Calling for Help',
  'Students learn about emergency workers, such as firefighters, paramedics, and police officers, and that calling for help right away can keep people safe during an emergency.',
  [('Name one type of emergency worker, like a firefighter or paramedic.', ['firefighter', 'paramedic', 'police officer']),
   ('What should you do if there is an emergency, like a fire?', ['call for help', 'tell an adult', 'call an emergency number']),
   ('Do emergency workers help keep people safe?', ['yes'])],
  [('Which of these is an emergency worker?', ['A firefighter', 'A baker', 'A farmer', 'An artist'], 0),
   ('What should you do first if you see an emergency, like a fire?', ['Tell a trusted adult right away', 'Ignore it', 'Hide and tell no one', 'Wait a long time'], 0),
   ('What job do paramedics do during an emergency?', ['Help people who are hurt or sick', 'Bake bread', 'Deliver mail', 'Teach school'], 0),
   ('Why is it important to know about emergency workers?', ['They can help keep people safe during emergencies', 'They are not helpful', 'Emergencies never happen', 'Only adults need to know this'], 0),
   ('Which of these is a good reason to know how to get help in an emergency?', ['It can keep you and others safe', 'It is not useful', 'Emergencies are not serious', 'Only firefighters need this information'], 0)])

# ─── DAY 46 ─────────────────────────────────────────────────────────────────
d46_lang = sub('Language', 'Alphabetical Order',
  'Students learn to put words in alphabetical order by comparing the first letter of each word, using their knowledge of the alphabet from A to Z.',
  [('Which comes first in alphabetical order, apple or banana?', ['apple']),
   ('Which comes first in alphabetical order, cat or bat?', ['bat']),
   ('What is the very first letter of the alphabet?', ['a'])],
  [('Which word would come first in alphabetical order, dog or cat?', ['Dog', 'Cat', 'They are the same', 'Cannot tell'], 1),
   ('What does it mean to put words in alphabetical order?', ['Arranging them by size', 'Arranging them by the order of the alphabet', 'Arranging them by colour', 'Arranging them randomly'], 1),
   ('Which word would come first in alphabetical order, sun or moon?', ['Sun', 'Moon', 'They are the same', 'Cannot tell'], 1),
   ('Which letter comes first in the alphabet, B or M?', ['B', 'M', 'They are the same', 'Cannot tell'], 0),
   ('Alphabetical order is useful for finding words in a ___.', ['Dictionary', 'Puddle', 'Cloud', 'Shadow'], 0)])

d46_math = sub('Math', 'Time: Quarter Past and Quarter To',
  'Students learn to read an analog clock showing quarter past and quarter to the hour, recognizing that the long hand points to the 3 for quarter past and the 9 for quarter to.',
  [('When the long hand points to the 3, what part of the hour is it?', ['quarter past']),
   ('When the long hand points to the 9, what part of the hour is it?', ['quarter to']),
   ('At quarter past the hour, how many minutes have passed since the start of the hour?', ['15', 'fifteen', '15 minutes'])],
  [('At quarter past the hour, where does the long hand point?', ['The 12', 'The 3', 'The 6', 'The 9'], 1),
   ('At quarter to the hour, where does the long hand point?', ['The 3', 'The 6', 'The 9', 'The 12'], 2),
   ('Quarter past the hour means how many minutes have passed?', ['10 minutes', '15 minutes', '30 minutes', '45 minutes'], 1),
   ('Quarter to the hour means the clock is how many minutes before the next hour?', ['5 minutes', '10 minutes', '15 minutes', '20 minutes'], 2),
   ('If the long hand points to the 3, what part of the hour is shown?', ['Quarter past', 'Quarter to', 'Half past', 'On the hour'], 0)])

d46_sci = sub('Science', 'Fish and Their Body Parts',
  'Students learn about the body parts of fish, such as fins for swimming and gills for breathing underwater, and how these parts help fish live in water.',
  [('What body part helps a fish swim?', ['fins', 'a fin']),
   ('What body part helps a fish breathe underwater?', ['gills']),
   ('Do fish live in water?', ['yes'])],
  [('What body part helps a fish swim through water?', ['Fins', 'Wings', 'Legs', 'Ears'], 0),
   ('What body part helps a fish breathe underwater?', ['Lungs', 'Gills', 'A nose', 'Fur'], 1),
   ('Where do most fish live?', ['In water', 'In trees', 'Underground', 'In the sky'], 0),
   ('Which of these covers the body of many fish?', ['Scales', 'Feathers', 'Fur', 'Leaves'], 0),
   ('Why are gills important to a fish?', ['They let the fish breathe oxygen from water', 'They help the fish fly', 'They help the fish walk', 'They have no purpose'], 0)])

d46_ss = sub('SocialStudies', 'Fire Safety at Home and School',
  'Students learn simple fire safety rules, such as knowing an escape plan, never playing with matches, and what to do if they hear a smoke alarm.',
  [('What should you do if you hear a smoke alarm?', ['leave the building', 'get out', 'exit the building']),
   ('Should children ever play with matches or lighters?', ['no']),
   ('What do we call a plan for how to safely leave a building during a fire?', ['an escape plan', 'escape plan', 'a fire drill'])],
  [('What should you do if you hear a smoke alarm?', ['Leave the building right away', 'Hide under the bed', 'Ignore it', 'Go find your toys first'], 0),
   ('Should children ever play with matches or lighters?', ['Yes, if an adult is not looking', 'No, never', 'Only outside', 'Only at school'], 1),
   ('What do we call a practice for safely leaving a building during a fire?', ['A fire drill', 'A birthday party', 'A field trip', 'A spelling test'], 0),
   ('Why is it helpful to know a fire escape plan?', ['It helps everyone leave safely and quickly', 'It is not helpful', 'Fires never happen', 'Only firefighters need a plan'], 0),
   ('Who should you tell if you notice something that could start a fire?', ['A trusted adult', 'No one', 'A friend far away', 'Nobody, just ignore it'], 0)])

# ─── DAY 47 ─────────────────────────────────────────────────────────────────
d47_lang = sub('Language', 'Comparing Adjectives: -er and -est',
  'Students learn that adjectives can compare things by adding -er to compare two things, as in taller, or -est to compare more than two things, as in tallest.',
  [('How would you compare two things using the word tall, like comparing two friends?', ['taller']),
   ('How would you compare three or more things using the word tall?', ['tallest']),
   ('What does the ending -est usually mean when comparing things?', ['the most', 'the most of all'])],
  [('Which word compares two things?', ['Tall', 'Taller', 'Tallest', 'Tallness'], 1),
   ('Which word compares three or more things and means the most?', ['Tall', 'Taller', 'Tallest', 'Talling'], 2),
   ('What ending do we add to compare two things, as in bigger?', ['-er', '-est', '-ing', '-ed'], 0),
   ('What ending do we add to compare more than two things, as in biggest?', ['-er', '-est', '-ing', '-ly'], 1),
   ('Which sentence correctly compares more than two friends?', ['She is the tallest of the three friends.', 'She is tall of the three friends.', 'She is taller of the three friends.', 'She is tall-er of the three friends.'], 0)])

d47_math = sub('Math', 'Money: Comparing Amounts',
  'Students compare small amounts of money made from coins, learning to tell which group of coins has a greater value and which has a lesser value.',
  [('Which has more value, a dime or a penny?', ['a dime', 'dime']),
   ('Which has more value, a quarter or a nickel?', ['a quarter', 'quarter']),
   ('If you have two dimes, how much money do you have?', ['20 cents', '20'])],
  [('Which coin has a greater value, a nickel or a dime?', ['Nickel', 'Dime', 'They are equal', 'Cannot tell'], 1),
   ('Which amount of money is greater, 3 pennies or 1 dime?', ['3 pennies', '1 dime', 'They are equal', 'Cannot tell'], 1),
   ('If you have one quarter, how many cents do you have?', ['10 cents', '15 cents', '25 cents', '50 cents'], 2),
   ('Which group of coins has more value, two dimes or one quarter?', ['Two dimes', 'One quarter', 'They are equal', 'Cannot tell'], 1),
   ('Comparing money amounts helps us know ___.', ['Which amount is worth more', 'The colour of a coin', 'The shape of a coin', 'Nothing useful'], 0)])

d47_sci = sub('Science', 'Birds and Their Body Parts',
  'Students learn about the body parts of birds, such as feathers, wings, and beaks, and how these parts help many birds fly and find food.',
  [('What body part covers most of a bird body?', ['feathers']),
   ('What body part helps most birds fly?', ['wings', 'a wing']),
   ('What body part does a bird use to eat, like pecking seeds?', ['beak'])],
  [('What covers most of a bird body?', ['Fur', 'Feathers', 'Scales', 'Skin only'], 1),
   ('What body part helps most birds fly through the air?', ['Wings', 'Fins', 'Legs', 'Gills'], 0),
   ('What body part does a bird use to eat food?', ['A beak', 'Teeth', 'A tongue only', 'Hands'], 0),
   ('Which of these animals is a bird?', ['A robin', 'A fish', 'A frog', 'A spider'], 0),
   ('Why are feathers helpful to a bird?', ['They help with flying and keeping warm', 'Feathers have no purpose', 'They help the bird swim only', 'They make the bird heavier and unable to move'], 0)])

d47_ss = sub('SocialStudies', 'Caring for Pets and Animals',
  'Students learn about the responsibility of caring for a pet, such as giving it food, water, and a safe home, and treating animals with kindness.',
  [('Name one thing a pet needs, like food or water.', ['food', 'water', 'a safe home', 'shelter']),
   ('Should we treat animals with kindness?', ['yes']),
   ('Name one pet that people might take care of, like a dog or cat.', ['dog', 'cat', 'fish', 'bird'])],
  [('Which of these is something a pet needs from its owner?', ['Food and water', 'Nothing at all', 'Only a name', 'A birthday cake'], 0),
   ('How should people treat animals?', ['With kindness and care', 'With unkindness', 'It does not matter', 'Animals do not need care'], 0),
   ('Why is caring for a pet a big responsibility?', ['A pet depends on its owner for food, water, and care', 'Pets need nothing from people', 'Pets can care for themselves completely', 'It is not a responsibility'], 0),
   ('Which of these shows responsible pet care?', ['Giving a pet fresh water every day', 'Never feeding a pet', 'Leaving a pet outside in bad weather', 'Ignoring a pet completely'], 0),
   ('Which of these animals is commonly kept as a pet?', ['A dog', 'A shark', 'A tiger', 'An eagle'], 0)])

# ─── DAY 48 ─────────────────────────────────────────────────────────────────
d48_lang = sub('Language', 'Following Written Instructions',
  'Students practise reading and following short written instructions, such as steps in a simple recipe or a set of directions for an activity, in the correct order.',
  [('Why is it important to follow instructions in order?', ['so the steps work correctly', 'to do the activity correctly', 'so it makes sense']),
   ('Name one place you might find written instructions, like a recipe.', ['a recipe', 'a game', 'a craft']),
   ('Should you read all the steps before starting an activity?', ['yes'])],
  [('Why is it important to read instructions carefully?', ['So you know what steps to follow and in what order', 'Instructions do not matter', 'You should skip reading them', 'Order never matters'], 0),
   ('Which of these is an example of written instructions?', ['The steps in a simple recipe', 'A made-up story', 'A birthday card', 'A weather report'], 0),
   ('What might happen if you follow instructions out of order?', ['The activity might not turn out correctly', 'Nothing would change', 'It always works out fine', 'Order never matters'], 0),
   ('What should you do if you do not understand a written instruction?', ['Ask a trusted adult or read it again', 'Guess and hope for the best', 'Give up completely', 'Ignore the instruction'], 0),
   ('Following instructions helps us ___.', ['Complete a task correctly', 'Make more mistakes', 'Skip important steps', 'Confuse ourselves'], 0)])

d48_math = sub('Math', 'Positional Language: Above, Below, Beside, Between',
  'Students learn positional words that describe where objects are located, such as above, below, beside, and between, to describe the position of one object compared to another.',
  [('If a bird is flying over a tree, is it above or below the tree?', ['above']),
   ('If a ball is under a table, is it above or below the table?', ['below']),
   ('If a cup is between two plates, how many plates are around it?', ['2', 'two'])],
  [('If a cloud is high in the sky over a house, the cloud is ___ the house.', ['Above', 'Below', 'Beside', 'Inside'], 0),
   ('If a shoe is under a bed, the shoe is ___ the bed.', ['Above', 'Below', 'Beside', 'On top of'], 1),
   ('If a chair is right next to a table, the chair is ___ the table.', ['Above', 'Below', 'Beside', 'Under'], 2),
   ('If a book is placed between two other books, how many books are on either side of it?', ['1 on each side', '2 on each side', '0 books', '3 on each side'], 0),
   ('Positional words like above and below describe ___.', ['Where an object is located', 'The colour of an object', 'The weight of an object', 'The sound an object makes'], 0)])

d48_sci = sub('Science', 'Camouflage: Hiding in Nature',
  'Students learn that camouflage is when an animal color or pattern helps it blend in with its surroundings, making it harder for predators or prey to see it.',
  [('What do we call it when an animal color helps it blend in with its surroundings?', ['camouflage']),
   ('Name one animal that uses camouflage, like a chameleon or a frog.', ['chameleon', 'frog', 'stick insect']),
   ('Does camouflage help an animal stay hidden?', ['yes'])],
  [('What is camouflage?', ['When an animal color or pattern helps it blend into its surroundings', 'A type of weather', 'A kind of food', 'A loud animal sound'], 0),
   ('Why might camouflage help an animal survive?', ['It helps the animal hide from predators or sneak up on prey', 'Camouflage has no benefit', 'It makes the animal easier to see', 'It only changes the animal sound'], 0),
   ('Which of these is an example of an animal using camouflage?', ['A frog that is green like the leaves around it', 'A bright pink flamingo in a field of snow', 'A loud animal call', 'An animal running very fast'], 0),
   ('Which environment might a snowy white animal blend into using camouflage?', ['A snowy, icy place', 'A hot desert', 'A green forest', 'A sandy beach'], 0),
   ('Camouflage mainly helps an animal by ___.', ['Making it harder to see against its surroundings', 'Making it louder', 'Making it faster', 'Making it a brighter color'], 0)])

d48_ss = sub('SocialStudies', 'Toys and Games: Then and Now',
  'Students compare toys and games children played with long ago, such as simple wooden toys and marbles, to toys and games children play with today, such as video games.',
  [('Name one toy children might have played with long ago, like a wooden toy.', ['a wooden toy', 'marbles', 'a doll']),
   ('Name one toy or game children play with today, like a video game.', ['a video game', 'a tablet game', 'a board game']),
   ('Have toys and games changed over time?', ['yes'])],
  [('Which of these is an example of a toy children may have played with long ago?', ['A simple wooden toy', 'A video game console', 'A tablet', 'A smartphone app'], 0),
   ('Which of these is a toy or game children commonly play with today?', ['A video game', 'A stone tool', 'A horse and wagon', 'A quill pen'], 0),
   ('How have toys and games changed over time?', ['New technology has created many new kinds of toys and games', 'Toys and games have never changed', 'Only old toys exist today', 'Children no longer play with toys'], 0),
   ('Which of these toys likely existed long before video games?', ['Marbles', 'A tablet', 'A video game console', 'A smartphone'], 0),
   ('Why is it interesting to compare toys and games then and now?', ['It shows us how childhood and technology have changed', 'Toys have never changed', 'It is not interesting', 'Old and new toys are identical'], 0)])

# ─── DAY 49 ─────────────────────────────────────────────────────────────────
d49_lang = sub('Language', 'Capital Letters: Names and Sentence Beginnings',
  'Students learn that capital letters are used at the beginning of a sentence and for the names of people, places, and days of the week.',
  [('Should the first word of a sentence begin with a capital letter?', ['yes']),
   ('Should the name of a person, like Maya, begin with a capital letter?', ['yes']),
   ('Name one day of the week that should begin with a capital letter, like Monday.', ['monday', 'tuesday', 'friday'])],
  [('What kind of letter should begin the first word of a sentence?', ['A capital letter', 'A lowercase letter', 'No letter at all', 'A number'], 0),
   ('Which of these should always begin with a capital letter?', ['The name of a person', 'Every word in a sentence', 'No words at all', 'Only short words'], 0),
   ('Which sentence uses capital letters correctly?', ['My friend Maya lives on Elm Street.', 'my friend maya lives on elm street.', 'MY FRIEND MAYA lives ON elm STREET.', 'my Friend maya Lives on elm street.'], 0),
   ('Which of these words should begin with a capital letter?', ['Monday', 'chair', 'apple', 'run'], 0),
   ('Why do we use capital letters for names and the start of sentences?', ['It helps readers notice important words and where sentences begin', 'Capital letters have no purpose', 'Capital letters are only for shouting', 'Capital letters are never needed'], 0)])

d49_math = sub('Math', 'Adding Three Numbers Together',
  'Students learn to add three one-digit numbers together, such as 2 add 3 add 4, by adding two numbers first and then adding the third number to that sum.',
  [('What is 2 add 3 add 4?', ['9', 'nine']),
   ('What is 1 add 1 add 1?', ['3', 'three']),
   ('What is 5 add 2 add 1?', ['8', 'eight'])],
  [('What is 3 add 2 add 1?', ['5', '6', '7', '8'], 1),
   ('What is 4 add 4 add 1?', ['8', '9', '10', '11'], 1),
   ('When adding three numbers, a good first step is to ___.', ['Add two of the numbers first, then add the third', 'Add nothing at all', 'Only add the largest number', 'Ignore the smallest number'], 0),
   ('What is 2 add 2 add 2?', ['4', '5', '6', '7'], 2),
   ('What is 6 add 1 add 2?', ['7', '8', '9', '10'], 2)])

d49_sci = sub('Science', 'Temperature: Hot and Cold',
  'Students learn to compare temperature, how hot or cold something is, and that a thermometer is a tool used to measure temperature.',
  [('What tool is used to measure temperature?', ['a thermometer', 'thermometer']),
   ('Name one thing that feels hot, like the sun or a stove.', ['the sun', 'a stove', 'fire']),
   ('Name one thing that feels cold, like ice or snow.', ['ice', 'snow', 'a fridge'])],
  [('What tool do we use to measure temperature?', ['A thermometer', 'A ruler', 'A scale', 'A clock'], 0),
   ('Which of these usually feels hot?', ['A campfire', 'An ice cube', 'Snow', 'A cold drink'], 0),
   ('Which of these usually feels cold?', ['Ice', 'A campfire', 'The sun', 'A stove'], 0),
   ('Temperature tells us ___.', ['How hot or cold something is', 'How heavy something is', 'How long something is', 'What colour something is'], 0),
   ('Which season usually has colder temperatures?', ['Winter', 'Summer', 'Both are the same', 'Temperature never changes'], 0)])

d49_ss = sub('SocialStudies', 'Road and Bicycle Safety Rules',
  'Students learn simple road and bicycle safety rules, such as looking both ways before crossing the street, wearing a helmet, and obeying traffic signals.',
  [('What should you look for before crossing a street?', ['cars', 'traffic', 'both ways']),
   ('What should you wear on your head when riding a bicycle?', ['a helmet', 'helmet']),
   ('What colour on a traffic light means stop?', ['red'])],
  [('What should you do before crossing the street?', ['Look both ways for traffic', 'Run across quickly without looking', 'Close your eyes', 'Ignore traffic'], 0),
   ('What should you wear on your head when riding a bicycle?', ['A helmet', 'A hat only', 'Nothing', 'Sunglasses only'], 0),
   ('What does a red traffic light mean?', ['Stop', 'Go', 'Slow down only', 'Turn only'], 0),
   ('What does a green traffic light mean?', ['Stop', 'Go', 'Wait', 'Turn around'], 1),
   ('Why is it important to follow road and bicycle safety rules?', ['They help keep people safe near traffic', 'They are not important', 'Rules only apply to adults', 'Traffic is never dangerous'], 0)])

# ─── DAY 50 (Review) ────────────────────────────────────────────────────────
d50_lang = sub('Language', 'Language Review: Blends, Vowel Teams, and Sentences',
  'Students review recent Language skills: beginning and ending blends, vowel teams, plural nouns, alphabetical order, comparing adjectives, following instructions, and capital letters.',
  [('What two letters blend together at the start of the word brush?', ['br']),
   ('What two letters make the long a sound in the word rain?', ['ai']),
   ('Should the first word of a sentence begin with a capital letter?', ['yes'])],
  [('Which word begins with the blend br?', ['Brush', 'Cat', 'Dog', 'Run'], 0),
   ('Which word ends with the blend st?', ['Nest', 'Cat', 'Dog', 'Sun'], 0),
   ('Which word has the ai vowel team?', ['Train', 'Cat', 'Dog', 'Sun'], 0),
   ('What is the plural of the word dog?', ['Dogs', 'Doges', 'Dogies', 'Dogx'], 0),
   ('What kind of letter should begin the first word of a sentence?', ['A capital letter', 'A lowercase letter', 'No letter at all', 'A number'], 0)])

d50_math = sub('Math', 'Math Review: Facts, Patterns, and Time',
  'Students review recent Math skills: fact families, doubles facts, skip counting by 3s, number bonds, odd and even numbers, telling time, comparing money, positional language, and adding three numbers.',
  [('If 3 add 4 equals 7, what is 7 minus 4?', ['3', 'three']),
   ('What is 5 add 5?', ['10', 'ten']),
   ('Is the number 4 odd or even?', ['even'])],
  [('Which subtraction fact belongs to the same fact family as 3 add 4 equals 7?', ['7 minus 3 equals 4', '8 minus 1 equals 7', '5 minus 2 equals 3', '9 minus 4 equals 5'], 0),
   ('Which of these numbers is even?', ['3', '4', '5', '7'], 1),
   ('At quarter past the hour, where does the long hand point?', ['The 12', 'The 3', 'The 6', 'The 9'], 1),
   ('Which coin has a greater value, a nickel or a dime?', ['Nickel', 'Dime', 'They are equal', 'Cannot tell'], 1),
   ('What is 3 add 2 add 1?', ['5', '6', '7', '8'], 1)])

d50_sci = sub('Science', 'Science Review: Bodies, Air, and Animals',
  'Students review recent Science topics: exercise and rest, healthy eating, germs, air and wind, floating and sinking, fish and birds, camouflage, and temperature.',
  [('Name one way to exercise, like running or jumping.', ['running', 'jumping', 'playing', 'walking']),
   ('What do we call tiny living things that can make people sick?', ['germs']),
   ('What tool is used to measure temperature?', ['a thermometer', 'thermometer'])],
  [('Which of these is a way to exercise your body?', ['Running', 'Sleeping all day', 'Watching only', 'Sitting still all day'], 0),
   ('What do we call moving air?', ['Wind', 'Water', 'Soil', 'Sunlight'], 0),
   ('What word describes an object that stays on top of the water?', ['Sinking', 'Floating', 'Melting', 'Freezing'], 1),
   ('What body part helps a fish breathe underwater?', ['Lungs', 'Gills', 'A nose', 'Fur'], 1),
   ('What is camouflage?', ['When an animal color or pattern helps it blend into its surroundings', 'A type of weather', 'A kind of food', 'A loud animal sound'], 0)])

d50_ss = sub('SocialStudies', 'Social Studies Review: Safety, Money, and Community Helpers',
  'Students review recent Social Studies topics: farms, local government, Canadian currency, saving and spending, emergency workers, fire safety, pet care, toys then and now, and road safety.',
  [('What do we call a person who grows crops and raises animals for food?', ['farmer']),
   ('What is the name of the Canadian one dollar coin?', ['loonie']),
   ('What should you wear on your head when riding a bicycle?', ['a helmet', 'helmet'])],
  [('What is the title of an elected leader of a city or town?', ['Mayor', 'Farmer', 'Dentist', 'Pilot'], 0),
   ('What does it mean to save money?', ['Keeping money to use later', 'Spending all money right away', 'Throwing money away', 'Losing money'], 0),
   ('Which of these is an emergency worker?', ['A firefighter', 'A baker', 'A farmer', 'An artist'], 0),
   ('What should you do if you hear a smoke alarm?', ['Leave the building right away', 'Hide under the bed', 'Ignore it', 'Go find your toys first'], 0),
   ('What does a red traffic light mean?', ['Stop', 'Go', 'Slow down only', 'Turn only'], 0)])


g1_41_50 = [
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
    _rebalance_answer_positions(g1_41_50)
    append_worksheet_days(1, g1_41_50)
