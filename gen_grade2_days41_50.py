#!/usr/bin/env python3
"""Grade 2, Days 41-50 -- SECOND batch extending Grade 2 past Day 40.
Self-contained script modeled exactly on gen_grade2_days31_40.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-40 topics (see data/grade2.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely (or
written without the apostrophe, e.g. "objects weight") to keep the
generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260829):
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
d41_lang = sub('Language', 'Silent Letters: kn, wr, mb, gh',
  'Students learn that some words contain silent letters, letters that are written but not pronounced, such as the k in knee, the w in write, the b in comb, and the gh in night.',
  [('What letter is silent at the beginning of the word knee?', ['k']),
   ('What letter is silent at the beginning of the word write?', ['w']),
   ('Name one word with a silent letter, like comb or night.', ['comb', 'night', 'knee', 'write'])],
  [('Which letter is silent in the word knee?', ['K', 'N', 'E', 'All letters are pronounced'], 0),
   ('Which letter is silent in the word write?', ['W', 'R', 'I', 'T'], 0),
   ('Which letter is silent in the word comb?', ['B', 'C', 'O', 'M'], 0),
   ('In the word night, which two letters together are silent?', ['GH', 'NI', 'HT', 'IG'], 0),
   ('A silent letter is a letter that is ___.', ['Written but not pronounced', 'Always pronounced loudly', 'Never written', 'Always capitalized'], 0)])

d41_math = sub('Math', 'Numbers to 1000: Counting and Comparing',
  'Students count, read, and compare numbers up to 1000, using place value to understand hundreds, tens, and ones.',
  [('What number comes right after 499?', ['500', 'five hundred']),
   ('Which is greater, 350 or 305?', ['350']),
   ('How many hundreds are in the number 400?', ['4', 'four'])],
  [('What number comes right after 499?', ['500', '499', '501', '450'], 0),
   ('Which number is greater, 620 or 602?', ['620', '602', 'They are equal', 'Cannot tell'], 0),
   ('How many hundreds are in the number 700?', ['7', '70', '700', '17'], 0),
   ('Which of these numbers is between 400 and 500?', ['450', '399', '501', '600'], 0),
   ('In the number 384, what digit is in the hundreds place?', ['3', '8', '4', '0'], 0)])

d41_sci = sub('Science', 'Life Cycle of a Plant: Seed to Flower',
  'Students learn the life cycle of a plant, from a seed that sprouts into a seedling, grows into a mature plant, and produces flowers that make new seeds.',
  [('What is the very first stage in a plant life cycle?', ['a seed', 'seed']),
   ('What do we call a young plant that has just sprouted?', ['a seedling', 'seedling']),
   ('What does a flower produce that can grow into a new plant?', ['seeds', 'new seeds'])],
  [('What is the very first stage of a plant life cycle?', ['A seed', 'A flower', 'A root', 'A leaf'], 0),
   ('What do we call a young plant that has just sprouted from a seed?', ['A seedling', 'A sapling', 'A bud', 'A stem'], 0),
   ('What does a mature plant produce that can grow into a new plant?', ['Seeds', 'Rocks', 'Soil', 'Water'], 0),
   ('Put these stages in order.', ['Seed, seedling, mature plant, flower', 'Flower, seed, seedling, mature plant', 'Mature plant, flower, seed, seedling', 'Seedling, flower, seed, mature plant'], 0),
   ('A plant life cycle describes how a plant ___.', ['Grows and changes from a seed to a new seed-producing plant', 'Never changes at all', 'Turns into an animal', 'Only lives for one day'], 0)])

d41_ss = sub('SocialStudies', 'Explorers and Early Settlers in Canada',
  'Students learn about explorers and early settlers who traveled to Canada long ago, discovering the land, meeting Indigenous peoples, and building the first small communities.',
  [('What do we call a person who travels to discover new lands?', ['an explorer', 'explorer']),
   ('What do we call the first people to build a community in a new place?', ['settlers', 'early settlers']),
   ('Did explorers meet Indigenous peoples already living on the land?', ['yes'])],
  [('What do we call a person who travels to discover new lands?', ['An explorer', 'A mayor', 'A farmer', 'A tourist'], 0),
   ('What do we call people who build the first communities in a new place?', ['Settlers', 'Tourists', 'Mayors', 'Astronauts'], 0),
   ('When explorers arrived in Canada long ago, who was already living on the land?', ['Indigenous peoples', 'No one at all', 'Only animals', 'Only settlers from Europe'], 0),
   ('Why did early explorers travel to new lands like Canada?', ['To discover new places and resources', 'To avoid meeting new people', 'To stay home instead', 'To build only underground homes'], 0),
   ('Early settlers often built their first communities near ___.', ['Rivers and lakes for water and travel', 'The middle of the desert', 'The top of tall mountains only', 'Places with no resources'], 0)])

# ─── DAY 42 ─────────────────────────────────────────────────────────────────
d42_lang = sub('Language', 'Homophones: Words That Sound the Same',
  'Students learn that homophones are words that sound the same but have different spellings and meanings, such as to, too, and two, or their and there.',
  [('Name one homophone pair, like to and too.', ['to and too', 'their and there', 'two and to']),
   ('Which word means the number after one, to, too, or two?', ['two']),
   ('Which word means also, to, too, or two?', ['too'])],
  [('What do we call words that sound the same but have different spellings and meanings?', ['Homophones', 'Synonyms', 'Antonyms', 'Compound words'], 0),
   ('Which word means also or as well?', ['Too', 'To', 'Two', 'Ten'], 0),
   ('Which word means the number 2?', ['Two', 'To', 'Too', 'Twelve'], 0),
   ('Which word means toward or in the direction of?', ['To', 'Too', 'Two', 'Ten'], 0),
   ('Their and there are examples of ___.', ['Homophones', 'Compound words', 'Contractions', 'Prefixes'], 0)])

d42_math = sub('Math', 'Fact Families: Addition and Subtraction',
  'Students learn that a fact family is a group of related addition and subtraction facts made from the same three numbers, such as 4 + 5 = 9, 5 + 4 = 9, 9 - 4 = 5, and 9 - 5 = 4.',
  [('If 4 + 5 = 9, what subtraction fact also belongs in this fact family?', ['9 - 5 = 4', '9 - 4 = 5']),
   ('Name the three numbers in the fact family for 3 + 6 = 9.', ['3, 6, and 9', '3 6 9']),
   ('If 7 + 2 = 9, what is 9 - 2?', ['7'])],
  [('What do we call a group of related addition and subtraction facts made from the same three numbers?', ['A fact family', 'A number line', 'A pattern', 'A fraction'], 0),
   ('If 4 + 5 = 9, which of these also belongs in the same fact family?', ['9 - 5 = 4', '9 + 5 = 14', '4 - 5 = 9', '5 - 9 = 4'], 0),
   ('Which three numbers make up the fact family that includes 3 + 6 = 9?', ['3, 6, and 9', '3, 6, and 18', '6, 9, and 15', '3, 9, and 12'], 0),
   ('If 8 + 2 = 10, what is 10 - 8?', ['2', '8', '10', '18'], 0),
   ('Knowing a fact family helps you ___.', ['Solve both addition and subtraction problems more quickly', 'Only solve addition problems', 'Forget subtraction', 'Multiply numbers'], 0)])

d42_sci = sub('Science', 'Floating and Sinking',
  'Students explore why some objects float on water while others sink, learning that this depends on an objects weight, shape, and the material it is made of.',
  [('What do we call it when an object stays on top of the water?', ['floating', 'float']),
   ('What do we call it when an object goes down under the water?', ['sinking', 'sink']),
   ('Name one object that usually floats in water, like a leaf or a piece of wood.', ['a leaf', 'leaf', 'a piece of wood', 'wood'])],
  [('What do we call it when an object stays on top of the water?', ['Floating', 'Sinking', 'Melting', 'Freezing'], 0),
   ('What do we call it when an object goes down under the water?', ['Sinking', 'Floating', 'Evaporating', 'Boiling'], 0),
   ('Which of these objects would most likely float in water?', ['A wooden block', 'A metal spoon', 'A large rock', 'A brick'], 0),
   ('Which of these objects would most likely sink in water?', ['A heavy rock', 'A rubber duck', 'An empty plastic bottle', 'A leaf'], 0),
   ('Whether an object floats or sinks depends on its ___.', ['Weight, shape, and material', 'Colour only', 'Smell only', 'Name only'], 0)])

d42_ss = sub('SocialStudies', 'Volunteering: Helping Our Community',
  'Students learn that volunteering means giving time and effort to help others without expecting payment, such as helping clean a park or collecting food for those in need.',
  [('What do we call giving your time to help others without expecting payment?', ['volunteering']),
   ('Name one way someone could volunteer, like cleaning a park.', ['cleaning a park', 'collecting food', 'helping others']),
   ('Does volunteering help make a community better?', ['yes'])],
  [('What do we call giving your time to help others without being paid?', ['Volunteering', 'Shopping', 'Working for money', 'Voting'], 0),
   ('Which of these is an example of volunteering?', ['Helping clean up a local park', 'Buying a new toy', 'Watching television', 'Sleeping in late'], 0),
   ('Why might someone choose to volunteer in their community?', ['To help others and make the community better', 'To earn a large paycheck', 'To avoid helping anyone', 'To stay away from other people'], 0),
   ('Which of these groups might collect food to help families in need?', ['A food bank', 'A toy store', 'A movie theatre', 'A car dealership'], 0),
   ('Volunteering can help a community by ___.', ['Bringing people together to solve problems and help others', 'Making the community worse', 'Taking resources away from people', 'Having no effect at all'], 0)])

# ─── DAY 43 ─────────────────────────────────────────────────────────────────
d43_lang = sub('Language', 'Adverbs: How, When, and Where',
  'Students learn that an adverb is a word that describes a verb, telling how, when, or where an action happens, such as quickly, today, or outside.',
  [('Name one adverb that tells how something happens, like quickly or slowly.', ['quickly', 'slowly', 'carefully']),
   ('Name one adverb that tells when something happens, like today or soon.', ['today', 'soon', 'yesterday']),
   ('Name one adverb that tells where something happens, like outside or here.', ['outside', 'here', 'there'])],
  [('An adverb is a word that describes a ___.', ['Verb', 'Noun', 'Pronoun', 'Article'], 0),
   ('Which word tells how someone runs in the sentence, She runs quickly?', ['Quickly', 'Runs', 'She', 'The'], 0),
   ('Which word is an adverb that tells when, as in We will go today?', ['Today', 'Go', 'We', 'Will'], 0),
   ('Which word is an adverb that tells where, as in The cat sat outside?', ['Outside', 'Cat', 'Sat', 'The'], 0),
   ('Which of these words is an adverb?', ['Carefully', 'Happy', 'Dog', 'Jump'], 0)])

d43_math = sub('Math', 'Telling Time: Elapsed Time and the Calendar',
  'Students learn to figure out how much time has passed between two events, called elapsed time, and to read a calendar to find days, weeks, and months.',
  [('How many days are in one week?', ['7', 'seven']),
   ('If a movie starts at 3:00 and ends at 4:00, how much time has passed?', ['1 hour', 'one hour']),
   ('How many months are in one year?', ['12', 'twelve'])],
  [('How many days are in one week?', ['7', '5', '10', '30'], 0),
   ('If a game starts at 2:00 and ends at 3:00, how much time has passed?', ['1 hour', '30 minutes', '2 hours', '15 minutes'], 0),
   ('How many months are in one year?', ['12', '10', '52', '365'], 0),
   ('What tool would you use to find out what day of the week a date falls on?', ['A calendar', 'A ruler', 'A thermometer', 'A scale'], 0),
   ('Elapsed time tells us ___.', ['How much time has passed between two events', 'The temperature outside', 'The day of the week only', 'The weight of an object'], 0)])

d43_sci = sub('Science', 'Forces: Gravity Pulls Things Down',
  'Students learn that gravity is a force that pulls objects toward the earth, which is why things fall down instead of floating away when dropped.',
  [('What do we call the force that pulls objects toward the earth?', ['gravity']),
   ('If you drop a ball, which direction does gravity pull it?', ['down', 'downward']),
   ('Does gravity pull objects toward the earth or away from it?', ['toward the earth', 'toward'])],
  [('What do we call the force that pulls objects toward the earth?', ['Gravity', 'Friction', 'Magnetism', 'Wind'], 0),
   ('If you drop a ball, which way does gravity pull it?', ['Down toward the ground', 'Up into the sky', 'Sideways only', 'Nowhere at all'], 0),
   ('Why does a dropped pencil fall to the floor instead of floating in the air?', ['Gravity pulls it toward the earth', 'Wind pushes it down', 'Magnetism pulls it down', 'It has no weight'], 0),
   ('Which of these is an example of gravity at work?', ['An apple falling from a tree', 'A magnet pulling a paperclip', 'Wind blowing leaves', 'Water evaporating'], 0),
   ('Without gravity, objects on earth would ___.', ['Float away instead of staying on the ground', 'Become heavier', 'Turn into gas', 'Melt instantly'], 0)])

d43_ss = sub('SocialStudies', 'Weather and Climate Across Canada',
  'Students learn that weather and climate can be very different across Canada, with some regions having cold snowy winters, others having milder weather, and coastlines with rain.',
  [('Name one type of weather common in many parts of Canada during winter.', ['snow', 'cold weather', 'snowy weather']),
   ('Do different regions of Canada have different climates?', ['yes']),
   ('Name one part of Canada known for rainy weather, like the coast.', ['the coast', 'coast', 'coastal areas'])],
  [('What do we call the usual weather pattern of a region over a long time?', ['Climate', 'A season', 'A map', 'A landmark'], 0),
   ('Which season in many parts of Canada is known for cold temperatures and snow?', ['Winter', 'Summer', 'Only spring', 'Only autumn'], 0),
   ('Why might the climate be different in different parts of Canada?', ['Location, such as being near mountains, coasts, or the north, affects climate', 'All of Canada always has the exact same weather', 'Climate never changes anywhere', 'Only cities have climate'], 0),
   ('Which part of Canada might experience a lot of rain because it is near the ocean?', ['A coastal region', 'The middle of a desert', 'The top of a dry plain', 'An underground cave'], 0),
   ('Understanding climate helps people ___.', ['Prepare for the kind of weather common in their region', 'Ignore the weather completely', 'Stop the weather from happening', 'Change the seasons'], 0)])

# ─── DAY 44 ─────────────────────────────────────────────────────────────────
d44_lang = sub('Language', 'Cause and Effect in Stories',
  'Students learn to identify cause and effect in stories, understanding that a cause is why something happens and an effect is what happens as a result.',
  [('What do we call the reason something happens in a story?', ['a cause', 'cause']),
   ('What do we call the result of what happens in a story?', ['an effect', 'effect']),
   ('If it rained and the ground got wet, name the effect.', ['the ground got wet', 'ground got wet'])],
  [('What do we call the reason something happens in a story?', ['A cause', 'An effect', 'A setting', 'A character'], 0),
   ('What do we call the result of an event in a story?', ['An effect', 'A cause', 'A title', 'A rhyme'], 0),
   ('If a boy forgot his umbrella and got wet in the rain, what is the cause?', ['He forgot his umbrella', 'He got wet', 'It stopped raining', 'He stayed dry'], 0),
   ('If a boy forgot his umbrella and got wet in the rain, what is the effect?', ['He got wet', 'He forgot his umbrella', 'He owns an umbrella', 'It was sunny'], 0),
   ('Understanding cause and effect helps readers ___.', ['Understand why events happen in a story', 'Ignore the story completely', 'Skip the ending', 'Change the characters names'], 0)])

d44_math = sub('Math', 'Tally Charts and Simple Data Collection',
  'Students learn to collect data by counting and recording it using tally marks, then use a tally chart to see totals for each category.',
  [('How many tally marks make up one group in a tally chart?', ['5', 'five']),
   ('What do we call marks used to keep count while collecting data?', ['tally marks']),
   ('If a tally chart shows one full group of 5 plus 2 more marks, how many is that in total?', ['7', 'seven'])],
  [('What do we call marks used to keep count while collecting data?', ['Tally marks', 'Number lines', 'Fractions', 'Graphs'], 0),
   ('How many tally marks are grouped together before starting a new group?', ['5', '4', '10', '3'], 0),
   ('If a tally chart shows one full group of five plus three more marks, what is the total?', ['8', '5', '3', '10'], 0),
   ('Why do we collect data using a tally chart?', ['To count and organize information clearly', 'To draw pictures only', 'To tell time', 'To measure length'], 0),
   ('After collecting data in a tally chart, the totals can be shown in a ___.', ['Bar graph or pictograph', 'Clock', 'Calendar', 'Thermometer'], 0)])

d44_sci = sub('Science', 'Food Chains: Who Eats What',
  'Students learn that a food chain shows how energy passes from one living thing to another, starting with a plant, moving to an animal that eats the plant, and then to an animal that eats that animal.',
  [('What do we call a chain that shows who eats what in nature?', ['a food chain', 'food chain']),
   ('What is usually the first link in a food chain, like a plant?', ['a plant', 'plant']),
   ('Name an animal that eats plants, like a rabbit or a deer.', ['a rabbit', 'rabbit', 'a deer', 'deer'])],
  [('What do we call a chain that shows how energy passes from one living thing to another through eating?', ['A food chain', 'A water cycle', 'A life cycle', 'A habitat'], 0),
   ('What is usually the first link in a food chain?', ['A plant', 'A lion', 'A fish', 'A bird'], 0),
   ('In a food chain with grass, a rabbit, and a fox, what does the rabbit eat?', ['Grass', 'The fox', 'Rocks', 'Water'], 0),
   ('In a food chain with grass, a rabbit, and a fox, what eats the rabbit?', ['The fox', 'The grass', 'Nothing eats the rabbit', 'The sun'], 0),
   ('Food chains show how ___.', ['Energy moves from plants to animals that eat them', 'Rocks turn into soil', 'Water evaporates into the air', 'Seasons change throughout the year'], 0)])

d44_ss = sub('SocialStudies', 'Public Safety Services: Police, Fire, and Ambulance',
  'Students learn about public safety services in a community, such as police officers who keep people safe, firefighters who put out fires, and paramedics who help people who are hurt or sick.',
  [('Name one public safety service that helps put out fires.', ['firefighters', 'fire department']),
   ('Name one public safety service that helps keep people safe from crime.', ['police', 'police officers']),
   ('Name one public safety service that helps people who are hurt or sick.', ['ambulance', 'paramedics'])],
  [('Which public safety service is trained to put out fires?', ['Firefighters', 'Teachers', 'Farmers', 'Mail carriers'], 0),
   ('Which public safety service helps keep a community safe from crime?', ['Police officers', 'Bakers', 'Librarians', 'Artists'], 0),
   ('Which public safety service helps people who are hurt or sick get to a hospital quickly?', ['Paramedics in an ambulance', 'A mail carrier', 'A shopkeeper', 'A librarian'], 0),
   ('What number do many communities use to call for help in an emergency?', ['911', '411', '511', '111'], 0),
   ('Public safety services are important because they ___.', ['Help keep people in a community safe and healthy', 'Have no purpose in a community', 'Only help during holidays', 'Are never needed'], 0)])

# ─── DAY 45 (Review) ────────────────────────────────────────────────────────
d45_lang = sub('Language', 'Review: Silent Letters, Homophones, Adverbs and Cause and Effect',
  'Students review recent Language skills: silent letters, homophones, adverbs, and cause and effect in stories.',
  [('What letter is silent at the beginning of the word knee?', ['k']),
   ('Name one homophone pair, like to and too.', ['to and too', 'their and there', 'two and to']),
   ('Name one adverb that tells how something happens, like quickly or slowly.', ['quickly', 'slowly', 'carefully'])],
  [('Which letter is silent in the word write?', ['W', 'R', 'I', 'T'], 0),
   ('Which word means also or as well?', ['Too', 'To', 'Two', 'Ten'], 0),
   ('Which word is an adverb that tells where, as in The cat sat outside?', ['Outside', 'Cat', 'Sat', 'The'], 0),
   ('What do we call the result of an event in a story?', ['An effect', 'A cause', 'A title', 'A rhyme'], 0),
   ('Their and there are examples of ___.', ['Homophones', 'Compound words', 'Contractions', 'Prefixes'], 0)])

d45_math = sub('Math', 'Review: Numbers to 1000, Fact Families, Elapsed Time and Data',
  'Students review recent Math skills: numbers to 1000, fact families, elapsed time and the calendar, and tally charts.',
  [('What number comes right after 499?', ['500', 'five hundred']),
   ('If 4 + 5 = 9, what subtraction fact also belongs in this fact family?', ['9 - 5 = 4', '9 - 4 = 5']),
   ('How many days are in one week?', ['7', 'seven'])],
  [('Which number is greater, 620 or 602?', ['620', '602', 'They are equal', 'Cannot tell'], 0),
   ('If 8 + 2 = 10, what is 10 - 8?', ['2', '8', '10', '18'], 0),
   ('How many months are in one year?', ['12', '10', '52', '365'], 0),
   ('Why do we collect data using a tally chart?', ['To count and organize information clearly', 'To draw pictures only', 'To tell time', 'To measure length'], 0),
   ('In the number 384, what digit is in the hundreds place?', ['3', '8', '4', '0'], 0)])

d45_sci = sub('Science', 'Review: Plant Life Cycle, Floating and Sinking, Gravity and Food Chains',
  'Students review recent Science topics: the life cycle of a plant, floating and sinking, gravity, and food chains.',
  [('What is the very first stage in a plant life cycle?', ['a seed', 'seed']),
   ('What do we call it when an object stays on top of the water?', ['floating', 'float']),
   ('What do we call the force that pulls objects toward the earth?', ['gravity'])],
  [('What does a mature plant produce that can grow into a new plant?', ['Seeds', 'Rocks', 'Soil', 'Water'], 0),
   ('Which of these objects would most likely sink in water?', ['A heavy rock', 'A rubber duck', 'An empty plastic bottle', 'A leaf'], 0),
   ('Why does a dropped pencil fall to the floor instead of floating in the air?', ['Gravity pulls it toward the earth', 'Wind pushes it down', 'Magnetism pulls it down', 'It has no weight'], 0),
   ('In a food chain with grass, a rabbit, and a fox, what eats the rabbit?', ['The fox', 'The grass', 'Nothing eats the rabbit', 'The sun'], 0),
   ('What do we call a chain that shows how energy passes from one living thing to another through eating?', ['A food chain', 'A water cycle', 'A life cycle', 'A habitat'], 0)])

d45_ss = sub('SocialStudies', 'Review: Explorers, Volunteering, Weather and Public Safety',
  'Students review recent Social Studies topics: explorers and early settlers, volunteering, weather and climate across Canada, and public safety services.',
  [('What do we call a person who travels to discover new lands?', ['an explorer', 'explorer']),
   ('What do we call giving your time to help others without expecting payment?', ['volunteering']),
   ('Name one public safety service that helps put out fires.', ['firefighters', 'fire department'])],
  [('Why did early explorers travel to new lands like Canada?', ['To discover new places and resources', 'To avoid meeting new people', 'To stay home instead', 'To build only underground homes'], 0),
   ('Which of these is an example of volunteering?', ['Helping clean up a local park', 'Buying a new toy', 'Watching television', 'Sleeping in late'], 0),
   ('Which season in many parts of Canada is known for cold temperatures and snow?', ['Winter', 'Summer', 'Only spring', 'Only autumn'], 0),
   ('What number do many communities use to call for help in an emergency?', ['911', '411', '511', '111'], 0),
   ('Why might the climate be different in different parts of Canada?', ['Location, such as being near mountains, coasts, or the north, affects climate', 'All of Canada always has the exact same weather', 'Climate never changes anywhere', 'Only cities have climate'], 0)])

# ─── DAY 46 ─────────────────────────────────────────────────────────────────
d46_lang = sub('Language', 'Combining Sentences with And, But, and Because',
  'Students learn to combine two short sentences into one longer sentence using the joining words and, but, and because.',
  [('Which joining word would you use to combine two similar ideas, like I like apples and I like pears?', ['and']),
   ('Which joining word shows a difference between two ideas, like It was cold but I was warm?', ['but']),
   ('Which joining word explains a reason, like I wore a coat because it was cold?', ['because'])],
  [('Which joining word combines two similar ideas?', ['And', 'But', 'Because', 'Or'], 0),
   ('Which joining word shows a contrast or difference between two ideas?', ['But', 'And', 'Because', 'So'], 0),
   ('Which joining word gives a reason for something?', ['Because', 'And', 'But', 'Or'], 0),
   ('Which sentence correctly combines two ideas with and?', ['I like dogs and I like cats.', 'I like dogs but I like cats.', 'I like dogs because cats.', 'I like dogs, cats.'], 0),
   ('Combining short sentences into one longer sentence can make writing ___.', ['Smoother and more interesting', 'Impossible to read', 'Shorter than one word', 'Always incorrect'], 0)])

d46_math = sub('Math', 'Rounding to the Nearest Ten',
  'Students learn to round two-digit numbers to the nearest ten, checking the ones digit to decide whether to round up or down.',
  [('What is 23 rounded to the nearest ten?', ['20', 'twenty']),
   ('What is 47 rounded to the nearest ten?', ['50', 'fifty']),
   ('If the ones digit is 5 or more, do we round up?', ['yes'])],
  [('What is 23 rounded to the nearest ten?', ['20', '30', '23', '10'], 0),
   ('What is 47 rounded to the nearest ten?', ['50', '40', '47', '45'], 0),
   ('When rounding, if the ones digit is 5 or more, we round ___.', ['Up to the next ten', 'Down to the previous ten', 'To zero', 'Nowhere'], 0),
   ('What is 62 rounded to the nearest ten?', ['60', '70', '62', '50'], 0),
   ('Rounding numbers helps us ___.', ['Estimate quickly using simpler numbers', 'Get the exact answer every time', 'Make numbers bigger only', 'Avoid using numbers'], 0)])

d46_sci = sub('Science', 'Animal Migration and Hibernation',
  'Students learn that some animals migrate, traveling long distances to find food or warmer weather, while other animals hibernate, going into a deep sleep through the cold winter months.',
  [('What do we call it when animals travel long distances to find food or warmer weather?', ['migration', 'migrate']),
   ('What do we call it when an animal goes into a deep sleep through winter?', ['hibernation', 'hibernate']),
   ('Name one animal that hibernates, like a bear.', ['a bear', 'bear'])],
  [('What do we call it when animals travel long distances to find food or warmer weather?', ['Migration', 'Hibernation', 'Pollination', 'Evaporation'], 0),
   ('What do we call it when an animal goes into a deep sleep through the cold winter months?', ['Hibernation', 'Migration', 'Camouflage', 'Metamorphosis'], 0),
   ('Which of these animals is known for migrating long distances?', ['A goose', 'A snail', 'A worm', 'A rock'], 0),
   ('Which of these animals is known for hibernating in winter?', ['A bear', 'A goose', 'A butterfly', 'A fish'], 0),
   ('Why might an animal migrate to a warmer place?', ['To find food and better living conditions', 'To avoid all other animals', 'To grow new feathers only', 'To change colour'], 0)])

d46_ss = sub('SocialStudies', 'Cultural Diversity: Celebrating Our Differences',
  'Students learn that communities in Canada are made up of people from many different cultures and backgrounds, and that learning about different traditions, languages, and foods helps everyone understand and respect each other.',
  [('What word describes a community made up of people from many different cultures?', ['diverse', 'diversity']),
   ('Name one thing that can be different between cultures, like food or language.', ['food', 'language', 'traditions', 'clothing']),
   ('Does learning about other cultures help people understand each other?', ['yes'])],
  [('What word describes a community made up of people from many different cultures and backgrounds?', ['Diverse', 'Empty', 'Silent', 'Identical'], 0),
   ('Which of these might be different between two cultures?', ['Food, language, and traditions', 'The number of days in a week', 'The colour of the sky', 'Gravity'], 0),
   ('Why is it helpful to learn about different cultures in your community?', ['It helps people understand and respect each other', 'It causes communities to fall apart', 'It has no benefit at all', 'It makes people forget their own culture'], 0),
   ('Which of these is a respectful way to learn about a friends culture?', ['Asking questions and listening with respect', 'Making fun of their traditions', 'Ignoring them completely', 'Refusing to learn anything new'], 0),
   ('Celebrating cultural diversity means ___.', ['Valuing and respecting many different backgrounds and traditions', 'Only valuing one culture', 'Ignoring all traditions', 'Avoiding people who are different'], 0)])

# ─── DAY 47 ─────────────────────────────────────────────────────────────────
d47_lang = sub('Language', 'Reading Comprehension: Fact vs Opinion',
  'Students learn the difference between a fact, a statement that can be proven true, and an opinion, a statement that shows what someone thinks or feels.',
  [('What do we call a statement that can be proven true?', ['a fact', 'fact']),
   ('What do we call a statement that shows what someone thinks or feels?', ['an opinion', 'opinion']),
   ('Is the statement dogs are the best pets a fact or an opinion?', ['an opinion', 'opinion'])],
  [('What do we call a statement that can be proven true?', ['A fact', 'An opinion', 'A rhyme', 'A question'], 0),
   ('What do we call a statement that shows what someone thinks or feels?', ['An opinion', 'A fact', 'A title', 'A setting'], 0),
   ('Which of these sentences is a fact?', ['A week has seven days.', 'Pizza is the tastiest food.', 'Summer is the best season.', 'Cats are better than dogs.'], 0),
   ('Which of these sentences is an opinion?', ['Chocolate ice cream tastes the best.', 'A triangle has three sides.', 'Fish live in water.', 'There are twelve months in a year.'], 0),
   ('Facts can be checked and proven, while opinions ___.', ['Show what a person thinks or feels', 'Can never be spoken aloud', 'Are always false', 'Are always the same as facts'], 0)])

d47_math = sub('Math', 'Area: Covering a Shape with Squares',
  'Students learn that area is the amount of space a flat shape covers, measured by counting how many equal squares fit inside the shape.',
  [('What do we call the amount of space a flat shape covers?', ['area']),
   ('If a rectangle is covered by 6 equal squares with no gaps, what is its area?', ['6 squares', '6']),
   ('Do all the squares used to measure area need to be the same size?', ['yes'])],
  [('What do we call the amount of space a flat shape covers?', ['Area', 'Perimeter', 'Length', 'Weight'], 0),
   ('If a rectangle is covered exactly by 8 equal squares, what is its area?', ['8 square units', '8 metres', '4 square units', '2 square units'], 0),
   ('To measure area, we count how many equal ___ fit inside a shape.', ['Squares', 'Circles', 'Lines', 'Dots'], 0),
   ('Which shape would likely have a larger area, one covered by 4 squares or one covered by 10 squares?', ['The one covered by 10 squares', 'The one covered by 4 squares', 'They are always equal', 'Cannot be measured'], 0),
   ('Area is measured in units such as ___.', ['Square units', 'Kilograms', 'Litres', 'Degrees'], 0)])

d47_sci = sub('Science', 'Pollination: How Bees Help Plants Grow',
  'Students learn that pollination happens when bees and other insects carry pollen from one flower to another, helping plants make seeds and grow new plants.',
  [('Name one insect that helps pollinate flowers, like a bee or a butterfly.', ['a bee', 'bee', 'a butterfly', 'butterfly']),
   ('What is the yellow powder inside a flower called that insects carry from flower to flower?', ['pollen']),
   ('Does pollination help plants make seeds?', ['yes'])],
  [('What do we call it when insects carry pollen from one flower to another?', ['Pollination', 'Migration', 'Hibernation', 'Evaporation'], 0),
   ('Which of these insects is well known for helping pollinate flowers?', ['A bee', 'A spider', 'A worm', 'An ant'], 0),
   ('What is the powder inside a flower called that bees carry from flower to flower?', ['Pollen', 'Soil', 'Sap', 'Bark'], 0),
   ('Why is pollination important for plants?', ['It helps plants make seeds and grow new plants', 'It helps plants stay small forever', 'It stops plants from growing', 'It has no effect on plants'], 0),
   ('Bees are attracted to flowers partly because flowers provide ___.', ['Nectar for the bees to collect', 'Rocks for the bees to eat', 'Water for the bees to drink only', 'Nothing at all'], 0)])

d47_ss = sub('SocialStudies', 'The Role of Schools and Libraries in a Community',
  'Students learn that schools help children learn and grow, while libraries offer books and resources for people of all ages to read, learn, and explore new ideas.',
  [('What do we call a place where children go to learn?', ['a school', 'school']),
   ('What do we call a place where people can borrow books for free?', ['a library', 'library']),
   ('Are libraries useful for people of all ages?', ['yes'])],
  [('What is the main purpose of a school in a community?', ['To help children learn and grow', 'To sell food', 'To fix cars', 'To grow crops'], 0),
   ('What can people typically borrow for free at a library?', ['Books', 'Cars', 'Houses', 'Food only'], 0),
   ('Who can usually use the resources at a public library?', ['People of all ages', 'Only children', 'Only teachers', 'Only adults'], 0),
   ('Which of these activities might happen at a school?', ['Students learning to read and do math', 'Firefighters putting out fires', 'Farmers growing crops', 'Doctors performing surgery'], 0),
   ('Schools and libraries both help communities by ___.', ['Supporting learning and sharing knowledge', 'Selling clothing', 'Building roads', 'Growing vegetables'], 0)])

# ─── DAY 48 ─────────────────────────────────────────────────────────────────
d48_lang = sub('Language', 'Using a Dictionary and Glossary',
  'Students learn how to use a dictionary or glossary to find the meaning of a word, using guide words and alphabetical order to locate entries quickly.',
  [('What book can you use to find the meaning of a word?', ['a dictionary', 'dictionary']),
   ('What do we call a list of words and meanings found at the back of a book?', ['a glossary', 'glossary']),
   ('Are the words in a dictionary listed in alphabetical order?', ['yes'])],
  [('What can you use to find the meaning of an unfamiliar word?', ['A dictionary', 'A calendar', 'A map', 'A recipe'], 0),
   ('What do we call a list of important words and their meanings at the back of a book?', ['A glossary', 'A title page', 'A table of contents', 'An index card'], 0),
   ('How are words usually organized in a dictionary?', ['In alphabetical order', 'By colour', 'By length', 'Randomly'], 0),
   ('What are the two words at the top of a dictionary page called, showing the first and last entries?', ['Guide words', 'Title words', 'Cover words', 'Page numbers'], 0),
   ('Using a dictionary helps readers ___.', ['Find the meaning and spelling of words', 'Draw pictures', 'Solve math problems', 'Tell time'], 0)])

d48_math = sub('Math', 'Perimeter: Measuring Around a Shape',
  'Students learn that perimeter is the total distance around the outside edge of a shape, found by adding the lengths of all its sides.',
  [('What do we call the distance around the outside edge of a shape?', ['perimeter']),
   ('If a square has sides of 4 centimetres each, what is its perimeter?', ['16 centimetres', '16']),
   ('To find perimeter, do we add the lengths of all the sides?', ['yes'])],
  [('What do we call the total distance around the outside edge of a shape?', ['Perimeter', 'Area', 'Volume', 'Mass'], 0),
   ('If a square has sides of 4 centimetres each, what is its perimeter?', ['16 centimetres', '4 centimetres', '8 centimetres', '12 centimetres'], 0),
   ('To find the perimeter of a shape, we ___.', ['Add the lengths of all its sides', 'Count the squares inside it', 'Multiply its width by its height', 'Measure only one side'], 0),
   ('What is the perimeter of a rectangle with sides of 3, 5, 3, and 5 centimetres?', ['16 centimetres', '15 centimetres', '8 centimetres', '20 centimetres'], 0),
   ('Perimeter is different from area because perimeter measures ___.', ['The distance around a shape, not the space inside it', 'The exact same thing as area', 'Only the width of a shape', 'Only weight'], 0)])

d48_sci = sub('Science', 'Simple Circuits and Electricity',
  'Students learn that a simple electric circuit is a complete loop that lets electricity flow from a battery through wires to power something like a light bulb.',
  [('What do we call a complete loop that lets electricity flow?', ['a circuit', 'circuit']),
   ('Name one part of a simple circuit, like a battery or a wire.', ['a battery', 'battery', 'a wire', 'wire', 'a bulb', 'bulb']),
   ('Does a circuit need to be a complete loop for electricity to flow?', ['yes'])],
  [('What do we call a complete loop that lets electricity flow through it?', ['A circuit', 'A magnet', 'A pattern', 'A pulley'], 0),
   ('Which of these provides the energy in a simple circuit?', ['A battery', 'A wooden block', 'A cotton ball', 'A leaf'], 0),
   ('What happens to a light bulb in a circuit if the loop is broken?', ['The light turns off', 'The light gets brighter', 'Nothing changes', 'The light changes colour'], 0),
   ('Which of these materials would work well as a wire in a circuit because it lets electricity flow through it?', ['Metal', 'Wood', 'Rubber', 'Paper'], 0),
   ('A simple circuit usually includes a battery, wires, and ___.', ['Something that uses electricity, like a light bulb', 'A cup of water', 'A pile of sand', 'A stack of books'], 0)])

d48_ss = sub('SocialStudies', 'Canadian Wildlife and Where Animals Live',
  'Students learn about wildlife found across Canada, such as moose in forests, polar bears in the Arctic, and beavers near rivers and lakes, and how each animal is suited to where it lives.',
  [('Name one animal found in Canadian forests, like a moose or a deer.', ['a moose', 'moose', 'a deer', 'deer']),
   ('Name one animal that lives in the cold Arctic region of Canada.', ['a polar bear', 'polar bear']),
   ('Name one animal often found living near rivers and lakes in Canada.', ['a beaver', 'beaver'])],
  [('Which large animal is commonly found in Canadian forests?', ['A moose', 'A camel', 'A kangaroo', 'A penguin'], 0),
   ('Which animal is well known for living in the cold Arctic region of Canada?', ['A polar bear', 'A monkey', 'A lion', 'A parrot'], 0),
   ('Which animal is often found building dams near rivers and lakes in Canada?', ['A beaver', 'A camel', 'A giraffe', 'An elephant'], 0),
   ('Why is a polar bear well suited to living in the Arctic?', ['It has thick fur and fat to stay warm in the cold', 'It has thin fur to stay cool', 'It cannot swim in cold water', 'It only eats plants'], 0),
   ('Learning about Canadian wildlife helps us understand ___.', ['How animals are suited to the places they live', 'How to build houses', 'How to bake bread', 'How to read a clock'], 0)])

# ─── DAY 49 ─────────────────────────────────────────────────────────────────
d49_lang = sub('Language', 'Writing Simple Instructions: How-To Writing',
  'Students learn to write simple step-by-step instructions, called how-to writing, using order words like first, next, and last to explain how to do something.',
  [('What do we call writing that explains the steps to do something?', ['how-to writing', 'instructions']),
   ('Name one order word used in how-to writing, like first or next.', ['first', 'next', 'last', 'then']),
   ('Should the steps in how-to writing be written in the correct order?', ['yes'])],
  [('What do we call writing that explains the steps to do something?', ['How-to writing', 'A poem', 'A letter', 'A song'], 0),
   ('Which of these is an order word used in how-to writing?', ['First', 'Happy', 'Blue', 'Quickly'], 0),
   ('Why is it important to write the steps of instructions in order?', ['So the reader can follow them correctly', 'So the reader gets confused', 'Order does not matter', 'To make the writing longer'], 0),
   ('Which sentence would most likely begin a set of how-to instructions?', ['First, gather all your materials.', 'The end.', 'Once upon a time.', 'Yesterday I went to the park.'], 0),
   ('How-to writing is most useful for ___.', ['Explaining how to complete a task step by step', 'Describing a characters feelings', 'Telling a make-believe story', 'Listing opinions about a topic'], 0)])

d49_math = sub('Math', 'Ordinal Numbers: First, Second, Third',
  'Students learn to use ordinal numbers, such as first, second, and third, to describe the position or order of objects and events in a sequence.',
  [('Which ordinal number describes the very first object in a line?', ['first']),
   ('Which ordinal number describes the object right after the first one?', ['second']),
   ('If a runner finishes the race in third place, what ordinal number describes their position?', ['third'])],
  [('Which ordinal number describes the object at the very start of a line?', ['First', 'Second', 'Third', 'Fourth'], 0),
   ('Which ordinal number comes right after first?', ['Second', 'Third', 'Fourth', 'Fifth'], 0),
   ('If a student is the third person in line, which two students came before them?', ['The first and second students', 'The fourth and fifth students', 'Only the first student', 'No one came before them'], 0),
   ('Ordinal numbers are used to describe ___.', ['The position or order of something in a sequence', 'The exact amount of something', 'The weight of an object', 'The temperature outside'], 0),
   ('Which of these is an ordinal number?', ['Fifth', 'Five', 'Fifty', 'Fives'], 0)])

d49_sci = sub('Science', 'Classifying Animals: Mammals, Birds, Fish, and More',
  'Students learn to classify animals into groups such as mammals, birds, fish, reptiles, and amphibians, based on shared features like fur, feathers, scales, or how they breathe.',
  [('Name one group that animals with fur and that feed their babies milk belong to.', ['mammals', 'mammal']),
   ('Name one feature that helps classify a bird, like feathers or wings.', ['feathers', 'wings']),
   ('Name one group of animals that live mostly in water and breathe with gills.', ['fish'])],
  [('Which animal group is covered in fur and feeds its babies milk?', ['Mammals', 'Birds', 'Fish', 'Reptiles'], 0),
   ('Which animal group is covered in feathers and can usually fly?', ['Birds', 'Mammals', 'Fish', 'Amphibians'], 0),
   ('Which animal group lives mostly in water and breathes using gills?', ['Fish', 'Birds', 'Mammals', 'Insects'], 0),
   ('Which of these is an example of a reptile?', ['A snake', 'A robin', 'A dog', 'A frog'], 0),
   ('Scientists classify animals into groups based on ___.', ['Shared features like fur, feathers, or scales', 'Their favourite colour', 'Their name only', 'Where they were born only'], 0)])

d49_ss = sub('SocialStudies', 'Communication Long Ago and Today',
  'Students compare how people communicated long ago, using letters and messengers, with how people communicate today, using telephones, computers, and the internet.',
  [('Name one way people communicated long ago, like writing a letter.', ['a letter', 'letter', 'writing a letter']),
   ('Name one way people communicate quickly today, like a telephone or computer.', ['a telephone', 'telephone', 'a computer', 'computer', 'the internet']),
   ('Is communicating with someone far away usually faster today than it was long ago?', ['yes'])],
  [('Which of these was a common way people communicated with each other long ago?', ['Writing a letter', 'Sending a text message', 'Video calling', 'Using the internet'], 0),
   ('Which of these tools helps people communicate quickly over long distances today?', ['A telephone', 'A quill pen only', 'A messenger on foot only', 'A carrier pigeon only'], 0),
   ('How has communication changed from long ago to today?', ['It has become much faster with new technology', 'It has become much slower', 'It has completely stopped', 'It has stayed exactly the same'], 0),
   ('Long ago, how might an important message have been delivered to a faraway town?', ['By a messenger traveling on foot or horseback', 'By a video call', 'By a text message', 'By email'], 0),
   ('Fast communication today, like the internet, allows people to ___.', ['Share information and messages almost instantly', 'Wait many weeks to send a simple message', 'Never talk to people far away', 'Only communicate in person'], 0)])

# ─── DAY 50 (Final Review) ──────────────────────────────────────────────────
d50_lang = sub('Language', 'Final Review: Sentence Combining, Fact and Opinion, Dictionaries and How-To Writing',
  'Students review recent Language skills: combining sentences with joining words, fact versus opinion, using a dictionary and glossary, and how-to writing.',
  [('Which joining word gives a reason for something?', ['because']),
   ('Is the statement dogs are the best pets a fact or an opinion?', ['an opinion', 'opinion']),
   ('Name one order word used in how-to writing, like first or next.', ['first', 'next', 'last', 'then'])],
  [('Which joining word shows a contrast or difference between two ideas?', ['But', 'And', 'Because', 'Or'], 0),
   ('Which of these sentences is a fact?', ['A week has seven days.', 'Pizza is the tastiest food.', 'Summer is the best season.', 'Cats are better than dogs.'], 0),
   ('What do we call a list of important words and their meanings at the back of a book?', ['A glossary', 'A title page', 'A table of contents', 'An index card'], 0),
   ('Which of these is an order word used in how-to writing?', ['First', 'Happy', 'Blue', 'Quickly'], 0),
   ('Combining short sentences into one longer sentence can make writing ___.', ['Smoother and more interesting', 'Impossible to read', 'Shorter than one word', 'Always incorrect'], 0)])

d50_math = sub('Math', 'Final Review: Rounding, Area, Perimeter and Ordinal Numbers',
  'Students review recent Math skills: rounding to the nearest ten, area, perimeter, and ordinal numbers.',
  [('What is 23 rounded to the nearest ten?', ['20', 'twenty']),
   ('What do we call the amount of space a flat shape covers?', ['area']),
   ('Which ordinal number comes right after first?', ['second'])],
  [('What is 47 rounded to the nearest ten?', ['50', '40', '47', '45'], 0),
   ('To measure area, we count how many equal ___ fit inside a shape.', ['Squares', 'Circles', 'Lines', 'Dots'], 0),
   ('To find the perimeter of a shape, we ___.', ['Add the lengths of all its sides', 'Count the squares inside it', 'Multiply its width by its height', 'Measure only one side'], 0),
   ('If a student is the third person in line, which two students came before them?', ['The first and second students', 'The fourth and fifth students', 'Only the first student', 'No one came before them'], 0),
   ('What is the perimeter of a rectangle with sides of 3, 5, 3, and 5 centimetres?', ['16 centimetres', '15 centimetres', '8 centimetres', '20 centimetres'], 0)])

d50_sci = sub('Science', 'Final Review: Migration, Pollination, Circuits and Animal Classification',
  'Students review recent Science topics: animal migration and hibernation, pollination, simple circuits and electricity, and classifying animals.',
  [('What do we call it when animals travel long distances to find food or warmer weather?', ['migration', 'migrate']),
   ('What is the powder inside a flower called that bees carry from flower to flower?', ['pollen']),
   ('What do we call a complete loop that lets electricity flow?', ['a circuit', 'circuit'])],
  [('Which of these animals is known for hibernating in winter?', ['A bear', 'A goose', 'A butterfly', 'A fish'], 0),
   ('Why is pollination important for plants?', ['It helps plants make seeds and grow new plants', 'It helps plants stay small forever', 'It stops plants from growing', 'It has no effect on plants'], 0),
   ('What happens to a light bulb in a circuit if the loop is broken?', ['The light turns off', 'The light gets brighter', 'Nothing changes', 'The light changes colour'], 0),
   ('Which animal group is covered in fur and feeds its babies milk?', ['Mammals', 'Birds', 'Fish', 'Reptiles'], 0),
   ('Which of these is an example of a reptile?', ['A snake', 'A robin', 'A dog', 'A frog'], 0)])

d50_ss = sub('SocialStudies', 'Final Review: Diversity, Schools and Libraries, Wildlife and Communication',
  'Students review recent Social Studies topics: cultural diversity, the role of schools and libraries, Canadian wildlife, and communication long ago and today.',
  [('What word describes a community made up of people from many different cultures?', ['diverse', 'diversity']),
   ('What do we call a place where people can borrow books for free?', ['a library', 'library']),
   ('Name one animal that lives in the cold Arctic region of Canada.', ['a polar bear', 'polar bear'])],
  [('Why is it helpful to learn about different cultures in your community?', ['It helps people understand and respect each other', 'It causes communities to fall apart', 'It has no benefit at all', 'It makes people forget their own culture'], 0),
   ('Who can usually use the resources at a public library?', ['People of all ages', 'Only children', 'Only teachers', 'Only adults'], 0),
   ('Which animal is often found building dams near rivers and lakes in Canada?', ['A beaver', 'A camel', 'A giraffe', 'An elephant'], 0),
   ('How has communication changed from long ago to today?', ['It has become much faster with new technology', 'It has become much slower', 'It has completely stopped', 'It has stayed exactly the same'], 0),
   ('Celebrating cultural diversity means ___.', ['Valuing and respecting many different backgrounds and traditions', 'Only valuing one culture', 'Ignoring all traditions', 'Avoiding people who are different'], 0)])


g2_41_50 = [
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
    _rebalance_answer_positions(g2_41_50, seed=20260829)
    append_worksheet_days(2, g2_41_50)
