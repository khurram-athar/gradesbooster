#!/usr/bin/env python3
"""Grade 1, Days 131-140 -- eleventh batch, extending Grade 1 past Day 130
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days121_130.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-130 (dumped
and checked against data/grade1.json before writing): vowel teams au/aw,
prefixes mis-/non-, adding -ly, text features maps/charts,
personification, sentence fragments, syllables, fact vs opinion, silent
letters mb/gh for Language. Skip counting by 20s, numbers to 300, time to
the nearest five minutes, doubling two-digit numbers, skip counting
backwards by 5s, comparing metres and centimetres, choosing the right
measuring tool, estimating groups of ten, patterns on a hundred chart for
Math. Octopuses and squid, desert animals, layers of the earth, weather
instruments, our joints, beavers, layers of the atmosphere, sense of
balance, turtles and tortoises for Science. Our school principal, the
Canadian Shield, Sir John A Macdonald, Canadian explorers, the fur
trade, Orange Shirt Day, our senate, our court system, the Underground
Railroad for Social Studies. Day 140 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior batch.
No embedded ASCII double-quote or straight apostrophe characters are
used anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely, matching this project's convention
(e.g. "Canadas" not "Canada's"), since this text gets embedded directly
into TypeScript string literals. Sensitive historical topics (Orange
Shirt Day, the Underground Railroad) are handled with age-appropriate,
respectful, factual framing suitable for a Grade 1 audience.
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


def _rebalance_answer_positions(days, seed=20260802):
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


g1_131_140 = [
day(131, [
L('Vowel Teams: au and aw',
  'Grade 1 Language strand: the vowel teams au and aw both make the same sound, heard in words like sauce, haul, saw, and claw.',
  [('Give a word with the au vowel team.', ['sauce', 'haul']),
   ('Give a word with the aw vowel team.', ['saw', 'claw']),
   ('Do au and aw make the same sound?', ['yes', 'yes they do'])],
  [('Which word has the au vowel team?', ['Cat', 'Sauce', 'Fun', 'Bike'], 1),
   ('Which word has the aw vowel team?', ['Claw', 'Cup', 'Dog', 'Run'], 0),
   ('Do au and aw usually make the same sound?', ['Yes', 'No', 'Only sometimes', 'Never'], 0),
   ('Which word does NOT contain the au or aw sound?', ['Haul', 'Saw', 'Claw', 'Cat'], 3),
   ('Complete the sentence: I like to draw with chalk on the side___.', ['walk', 'wilk', 'wolk', 'wuke'], 0)]),
M('Skip Counting by 20s',
  'Grade 1 Math strand: students skip count by 20s, saying 20, 40, 60, 80, and continuing on toward 200.',
  [('What comes after 20, 40, 60?', ['80', 'eighty']),
   ('Skip count by 20s from 20 to 100.', ['20,40,60,80,100', '20 40 60 80 100']),
   ('What number comes right before 200 when skip counting by 20s?', ['180', 'one hundred eighty'])],
  [('What comes next: 20, 40, 60, ___?', ['70', '75', '80', '90'], 2),
   ('What comes next: 80, 100, 120, ___?', ['130', '135', '140', '150'], 2),
   ('Skip counting by 20s means we add ___ each time.', ['2', '10', '20', '25'], 2),
   ('Which list correctly skip counts by 20s?', ['20, 40, 60, 80', '20, 30, 40, 50', '20, 40, 50, 80', '20, 25, 30, 35'], 0),
   ('What number comes right before 200 when skip counting by 20s?', ['170', '180', '190', '195'], 1)]),
Sc('Octopuses and Squid: Ocean Creatures Without Bones',
   'Grade 1 Science strand: octopuses and squid are ocean animals with soft bodies and no bones, and they use their arms and tentacles to swim and catch food.',
   [('Do octopuses have bones?', ['no', 'no they do not']),
    ('What body part do octopuses use to catch food?', ['their arms', 'arms and tentacles']),
    ('Where do octopuses and squid live?', ['the ocean', 'in the ocean'])],
   [('Do octopuses have bones inside their bodies?', ['Yes', 'No', 'Only in their arms', 'Only when young'], 1),
    ('What do octopuses use to swim and catch food?', ['Wings', 'Arms and tentacles', 'Fins only', 'Claws'], 1),
    ('Where do octopuses and squid live?', ['In the desert', 'In the ocean', 'In trees', 'Underground'], 1),
    ('Which of these is true about squid?', ['They have soft bodies and no bones', 'They are mammals', 'They live only on land', 'They have hard shells like turtles'], 0),
    ('Animals with no bones inside their body are called ___.', ['Invertebrates', 'Mammals', 'Reptiles', 'Amphibians'], 0)]),
SS('Our School Principal: Leading Our School',
   'Grade 1 Social Studies strand: the school principal leads the school, helping teachers, students, and families, and making sure the school runs smoothly and safely.',
   [('What does a school principal do?', ['leads the school', 'helps run the school']),
    ('Who does a principal work with?', ['teachers, students, and families', 'the whole school community']),
    ('Why is a principal important?', ['helps the school run smoothly and safely', 'leads and supports the school'])],
   [('What is the main role of a school principal?', ['Leading and supporting the whole school', 'Driving the school bus', 'Cooking lunch', 'Cleaning the hallways'], 0),
    ('Who might a principal work closely with?', ['Teachers, students, and families', 'Only the mayor', 'Only firefighters', 'No one at all'], 0),
    ('Why is the principals job important to a school?', ['It helps the school run smoothly and safely', 'It has no effect on the school', 'Only classrooms matter', 'Principals do not help students'], 0),
    ('Which is something a principal might do?', ['Welcome new students to the school', 'Deliver mail across town', 'Fly an airplane', 'Grow crops on a farm'], 0),
    ('A school principal is an example of a ___.', ['Community helper', 'Type of weather', 'Kind of animal', 'Type of vehicle'], 0)]),
]),
day(132, [
L('Prefixes: mis- and non-',
  'Grade 1 Language strand: the prefixes mis- and non- change the meaning of a word, as in misspell meaning to spell wrong and nonstop meaning without stopping.',
  [('What does the prefix mis- usually mean?', ['wrong or badly', 'incorrectly']),
   ('What does the prefix non- usually mean?', ['not or without', 'the opposite of having']),
   ('What does the word misspell mean?', ['to spell a word wrong', 'spell incorrectly'])],
  [('What does the prefix mis- usually mean?', ['Again', 'Wrong or badly', 'Before', 'Not needed'], 1),
   ('What does the prefix non- usually mean?', ['Not or without', 'Very much', 'Again and again', 'Before something'], 0),
   ('What does the word misspell mean?', ['To spell a word correctly', 'To spell a word wrong', 'To read a word', 'To write neatly'], 1),
   ('What does the word nonstop mean?', ['Stopping often', 'Without stopping', 'Stopping once', 'Never starting'], 1),
   ('Which word means without sense?', ['Misread', 'Nonsense', 'Rewrite', 'Preview'], 1)]),
M('Numbers to 300: Beyond 200',
  'Grade 1 Math strand: students extend their counting and number recognition beyond 200, reading and writing numbers up to 300.',
  [('What number comes after 200?', ['201', 'two hundred one']),
   ('Read the number 250.', ['two hundred fifty', 'two fifty']),
   ('What number comes right before 300?', ['299', 'two hundred ninety nine'])],
  [('What number comes right after 249?', ['248', '250', '251', '260'], 1),
   ('Which number is between 200 and 300?', ['150', '199', '260', '350'], 2),
   ('How do we read the number 275?', ['Two hundred seventy five', 'Two seventy five hundred', 'Twenty seven five', 'Two hundred seven'], 0),
   ('What number comes right before 300?', ['290', '295', '298', '299'], 3),
   ('Counting past 200 helps us understand numbers up to ___.', ['100', '200', '300', '1000'], 2)]),
Sc('Animals of the Desert: Staying Cool and Finding Water',
   'Grade 1 Science strand: desert animals like camels and desert foxes have special ways to stay cool in the heat and find water in a dry habitat.',
   [('Name an animal that lives in the desert.', ['a camel', 'a desert fox']),
    ('Why do desert animals need special ways to stay cool?', ['it is very hot in the desert', 'the desert has extreme heat']),
    ('What is one challenge desert animals face?', ['finding water', 'staying cool in the heat'])],
   [('Which of these is a desert animal?', ['Camel', 'Polar bear', 'Penguin', 'Salmon'], 0),
    ('Why do desert animals need ways to stay cool?', ['The desert is very hot', 'The desert is always cold', 'Deserts have no sun', 'Deserts are underwater'], 0),
    ('What is a major challenge for animals living in the desert?', ['Finding water', 'Finding snow', 'Finding ice', 'Finding rain daily'], 0),
    ('A camel can survive a long time in the desert because it can ___.', ['Store fat and water in its body', 'Breathe underwater', 'Fly to find water', 'Live without eating forever'], 0),
    ('Desert animals are adapted to survive in a habitat that is ___.', ['Hot and dry', 'Cold and wet', 'Icy and frozen', 'Deep underwater'], 0)]),
SS('The Canadian Shield: A Special Land Region',
   'Grade 1 Social Studies strand: the Canadian Shield is a huge, rocky land region that covers much of Canada, filled with lakes, forests, and ancient rock.',
   [('What is the Canadian Shield?', ['a huge rocky land region', 'a large area of ancient rock']),
    ('What can be found across the Canadian Shield?', ['lakes and forests', 'many lakes, forests, and rocks']),
    ('Is the Canadian Shield a small or large area?', ['large', 'a huge area'])],
   [('What is the Canadian Shield?', ['A huge rocky land region in Canada', 'A type of building', 'A small city park', 'A kind of vehicle'], 0),
    ('Which of these can be found across the Canadian Shield?', ['Lakes, forests, and ancient rock', 'Only sand dunes', 'Only ocean water', 'Only tall skyscrapers'], 0),
    ('Is the Canadian Shield a small or large land region?', ['Very small', 'Huge, covering much of Canada', 'It does not exist', 'Smaller than one city'], 1),
    ('The rock found in the Canadian Shield is often described as ___.', ['Ancient and very old', 'Brand new', 'Made of ice', 'Made of glass'], 0),
    ('Learning about the Canadian Shield helps us understand ___.', ['Canadas land and geography', 'Only other countries', 'Nothing about Canada', 'A made-up place'], 0)]),
]),
day(133, [
L('Adding -ly to Make Adverbs',
  'Grade 1 Language strand: adding -ly to a describing word can make an adverb, a word that tells how someone did something, such as quick becoming quickly.',
  [('What does adding -ly to quick make?', ['quickly', 'it makes quickly']),
   ('What does adding -ly to slow make?', ['slowly', 'it makes slowly']),
   ('What does an adverb like quickly tell us?', ['how someone did something', 'how an action happened'])],
  [('What word do we get by adding -ly to quick?', ['Quicker', 'Quickly', 'Quickest', 'Quickable'], 1),
   ('What word do we get by adding -ly to slow?', ['Slower', 'Slowly', 'Slowest', 'Slowness'], 1),
   ('In the sentence She ran quickly, which word is the adverb?', ['She', 'Ran', 'Quickly', 'The'], 2),
   ('An adverb ending in -ly usually tells us ___.', ['What colour something is', 'How an action was done', 'Who did something', 'When something starts'], 1),
   ('Which word is an adverb?', ['Happy', 'Happily', 'Happiness', 'Happier'], 1)]),
M('Time to the Nearest Five Minutes',
  'Grade 1 Math strand: students read a clock to the nearest five minutes, counting by 5s around the clock face to name times like 3:05 or 3:35.',
  [('If the minute hand points to the 1, what minute is it?', ['5', 'five minutes']),
   ('If the minute hand points to the 6, what minute is it?', ['30', 'thirty minutes']),
   ('How do we count around a clock face to find the minutes?', ['count by 5s', 'skip count by 5']),],
  [('If the minute hand points to the 2, how many minutes past the hour is it?', ['2', '5', '10', '20'], 2),
   ('If the minute hand points to the 9, how many minutes past the hour is it?', ['9', '35', '45', '50'], 2),
   ('To read minutes on a clock face, we count around by ___.', ['1s', '5s', '10s', '20s'], 1),
   ('If the hour hand is near the 4 and the minute hand points to the 3, the time is about ___.', ['4:03', '4:15', '4:30', '4:45'], 1),
   ('Reading a clock to the nearest five minutes uses which math skill?', ['Subtracting', 'Skip counting by 5s', 'Multiplying', 'Rounding'], 1)]),
Sc('The Layers of the Earth: Crust, Mantle, and Core',
   'Grade 1 Science strand: the Earth is made of layers, with a rocky crust on the outside, a hot mantle in the middle, and a very hot core at the centre.',
   [('What is the outer layer of the Earth called?', ['the crust', 'crust']),
    ('What is the middle layer of the Earth called?', ['the mantle', 'mantle']),
    ('What is the layer at the very centre of the Earth called?', ['the core', 'core'])],
   [('What is the outer, rocky layer of the Earth called?', ['The core', 'The crust', 'The mantle', 'The surface only'], 1),
    ('What is the layer beneath the crust called?', ['The mantle', 'The crust', 'The sky', 'The ocean'], 0),
    ('What is the layer at the very centre of the Earth called?', ['The crust', 'The mantle', 'The core', 'The atmosphere'], 2),
    ('Which layer of the Earth is closest to the surface where we live?', ['The core', 'The crust', 'The mantle', 'The deep ocean'], 1),
    ('The centre of the Earth is described as very ___.', ['Cold', 'Hot', 'Empty', 'Made of water'], 1)]),
SS('Sir John A Macdonald: Canadas First Prime Minister',
   'Grade 1 Social Studies strand: Sir John A Macdonald was Canadas first prime minister, leading the country after Confederation brought the colonies together.',
   [('Who was Canadas first prime minister?', ['Sir John A Macdonald', 'John A Macdonald']),
    ('What event happened before he became prime minister?', ['Confederation', 'Canada became a country']),
    ('What does a prime minister do?', ['leads the country', 'leads Canada'])],
   [('Who was Canadas first prime minister?', ['Sir John A Macdonald', 'Terry Fox', 'A mayor', 'A premier'], 0),
    ('What major event happened around the time Sir John A Macdonald became prime minister?', ['Confederation', 'A hockey game', 'A school opening', 'A snowstorm'], 0),
    ('What is the main job of a prime minister?', ['Leading the whole country', 'Leading one school', 'Leading one town', 'Leading one street'], 0),
    ('Why do students learn about Canadas first prime minister?', ['To understand how Canada was led as a new country', 'It has no importance', 'It is a made-up story', 'It only matters in other countries'], 0),
    ('Sir John A Macdonald became prime minister after Canada became a country through ___.', ['Confederation', 'A vote at school', 'A treaty with another planet', 'A sports competition'], 0)]),
]),
day(134, [
L('Text Features: Maps and Charts',
  'Grade 1 Language strand: nonfiction books sometimes use maps and charts to show information visually, helping readers understand places or data quickly.',
  [('What does a map show in a nonfiction book?', ['a place or location', 'where things are']),
   ('What does a chart help show?', ['information or data', 'organized information']),
   ('Why are maps and charts helpful text features?', ['show information quickly', 'help readers understand faster'])],
  [('What does a map in a nonfiction book usually show?', ['A place or location', 'A made-up story', 'A list of characters', 'A poem'], 0),
   ('What does a chart in a nonfiction book usually show?', ['Organized information or data', 'A fictional character', 'A rhyme', 'A joke'], 0),
   ('Why might an author include a map in a book about animal habitats?', ['To show where the animals live', 'To confuse the reader', 'It has no purpose', 'To make the book longer only'], 0),
   ('Which text feature would best show how many students like each fruit?', ['A chart', 'A title', 'A caption', 'A glossary'], 0),
   ('Maps and charts help readers understand information more ___.', ['Slowly', 'Quickly and clearly', 'Incorrectly', 'Confusingly'], 1)]),
M('Doubling Two-Digit Numbers',
  'Grade 1 Math strand: students double two-digit numbers by adding the number to itself, such as doubling 14 to get 28.',
  [('What is double 14?', ['28', 'twenty eight']),
   ('What is double 20?', ['40', 'forty']),
   ('What does it mean to double a number?', ['add it to itself', 'add the same number twice'])],
  [('What is double 14?', ['24', '26', '28', '30'], 2),
   ('What is double 25?', ['40', '45', '50', '55'], 2),
   ('To double a number means to ___.', ['Add it to itself', 'Subtract it from itself', 'Divide it in half', 'Multiply it by zero'], 0),
   ('What is double 30?', ['50', '55', '60', '65'], 2),
   ('If half of a number is 18, what is double 18?', ['18', '26', '36', '40'], 2)]),
Sc('Weather Instruments: Wind Vanes and Measuring Wind',
   'Grade 1 Science strand: a wind vane is a tool that shows which direction the wind is blowing, helping people understand and predict the weather.',
   [('What tool shows which direction the wind is blowing?', ['a wind vane', 'wind vane']),
    ('Why do people use wind vanes?', ['to know wind direction', 'to help understand weather']),
    ('Name one other tool used to study weather.', ['a thermometer', 'a rain gauge'])],
   [('What tool shows the direction the wind is blowing?', ['A thermometer', 'A wind vane', 'A rain gauge', 'A clock'], 1),
    ('Why is knowing wind direction useful?', ['It helps people understand and predict weather', 'It has no use at all', 'It tells us the time', 'It tells us the temperature'], 0),
    ('Which of these is also used to study weather?', ['A thermometer', 'A ruler', 'A calculator', 'A paintbrush'], 0),
    ('A wind vane usually points ___.', ['In the direction the wind is blowing from', 'Straight up always', 'Straight down always', 'Nowhere in particular'], 0),
    ('Weather instruments help scientists ___.', ['Understand and predict weather', 'Change the weather', 'Stop the wind', 'Make it rain on command'], 0)]),
SS('Canadian Explorers: Discovering New Places',
   'Grade 1 Social Studies strand: early Canadian explorers travelled by canoe, ship, and on foot to map rivers, lakes, and coastlines across the land.',
   [('How did early explorers often travel across Canada?', ['by canoe', 'canoe, ship, or on foot']),
    ('What did explorers often do as they travelled?', ['map rivers and lakes', 'explore and map new places']),
    ('Why is it important to learn about explorers?', ['helps us understand Canadas history', 'they helped map our land'])],
   [('How did many early Canadian explorers often travel?', ['By canoe', 'By airplane', 'By car', 'By subway'], 0),
    ('What did explorers often do as they traveled through new areas?', ['Mapped rivers, lakes, and coastlines', 'Built shopping malls', 'Played video games', 'Watched television'], 0),
    ('Why do students learn about Canadian explorers?', ['To understand part of Canadas history', 'It has no importance', 'They never existed', 'Only for fun with no purpose'], 0),
    ('Which of these might an explorer have used to travel on water?', ['A canoe', 'A bicycle', 'A skateboard', 'A wheelchair'], 0),
    ('Exploring new places long ago helped people learn more about ___.', ['The land and its geography', 'Nothing useful', 'Only cities', 'Only mountains'], 0)]),
]),
day(135, [
L('Personification: Giving Human Qualities to Objects',
  'Grade 1 Language strand: personification gives human qualities to things that are not human, such as saying the wind whispered or the sun smiled.',
  [('Give an example of personification.', ['the wind whispered', 'the sun smiled']),
   ('What does personification do?', ['gives human qualities to objects', 'makes things act like people']),
   ('Can the wind actually whisper?', ['no', 'no, that is personification'])],
  [('What is personification?', ['Giving human qualities to something that is not human', 'A comparison using like or as', 'A type of punctuation', 'A rhyming word'], 0),
   ('Which sentence uses personification?', ['The wind blew hard.', 'The wind whispered through the trees.', 'The wind is cold.', 'Is the wind strong?'], 1),
   ('Can the sun really smile?', ['Yes, literally', 'No, that is personification', 'Only in winter', 'Only at night'], 1),
   ('Which of these is an example of personification?', ['The flowers danced in the breeze.', 'The flowers are pink.', 'I picked the flowers.', 'The flowers grew tall.'], 0),
   ('Writers use personification to make their writing more ___.', ['Boring', 'Imaginative and vivid', 'Confusing', 'Short'], 1)]),
M('Skip Counting Backwards by 5s',
  'Grade 1 Math strand: students skip count backwards by 5s, saying 100, 95, 90, and continuing down toward 0.',
  [('What number comes right after 100 when counting backwards by 5s?', ['95', 'ninety five']),
   ('Skip count backwards by 5s from 50 to 30.', ['50,45,40,35,30', '50 45 40 35 30']),
   ('What number comes right before 0 when counting backwards by 5s?', ['5', 'five'])],
  [('Counting backwards by 5s from 50, what comes next: 50, 45, ___?', ['35', '40', '42', '44'], 1),
   ('Counting backwards by 5s, what comes after 30?', ['20', '25', '26', '28'], 1),
   ('Counting backwards by 5s from 20, what comes right before 0?', ['1', '3', '5', '10'], 2),
   ('Skip counting backwards by 5s means we subtract ___ each time.', ['1', '2', '5', '10'], 2),
   ('Which list correctly skip counts backwards by 5s?', ['50, 45, 40, 35', '50, 40, 35, 25', '50, 45, 35, 30', '50, 48, 46, 44'], 0)]),
Sc('Our Joints: Bending and Moving',
   'Grade 1 Science strand: joints are the parts of our body, like our elbows and knees, where two bones meet and let us bend and move.',
   [('What are joints?', ['places where two bones meet', 'where bones meet and bend']),
    ('Name one joint in your body.', ['elbow', 'knee']),
    ('What do joints let our body do?', ['bend and move', 'move different ways'])],
   [('What is a joint in our body?', ['A place where two bones meet and can bend', 'A type of muscle', 'A part of our skin', 'A part of our hair'], 0),
    ('Which of these is an example of a joint?', ['Elbow', 'Fingernail', 'Eyebrow', 'Earlobe'], 0),
    ('What do joints allow our body to do?', ['Bend and move', 'Taste food', 'Smell flowers', 'Hear sounds'], 0),
    ('Which activity uses your knee joints the most?', ['Bending your legs to sit down', 'Smelling a flower', 'Tasting food', 'Listening to music'], 0),
    ('Without joints, our bodies would have a much harder time ___.', ['Bending and moving', 'Breathing', 'Hearing', 'Seeing'], 0)]),
SS('The Fur Trade: Trading in Early Canada',
   'Grade 1 Social Studies strand: the fur trade was an early Canadian business where Indigenous peoples and settlers traded furs, like beaver pelts, for tools and other goods.',
   [('What was traded in the fur trade?', ['furs', 'beaver pelts and other furs']),
    ('Who took part in the fur trade?', ['Indigenous peoples and settlers', 'both Indigenous peoples and settlers']),
    ('What did people receive in exchange for furs?', ['tools and goods', 'other goods'])],
   [('What was mainly traded during the fur trade?', ['Furs, like beaver pelts', 'Cars', 'Computers', 'Ice cream'], 0),
    ('Who took part in the early Canadian fur trade?', ['Indigenous peoples and settlers', 'Only animals', 'Only astronauts', 'No one at all'], 0),
    ('What might people receive in exchange for furs during the fur trade?', ['Tools and other goods', 'Nothing at all', 'Only gold coins', 'Only food from overseas'], 0),
    ('Why is the fur trade an important part of early Canadian history?', ['It shaped trade and relationships between groups', 'It has no importance', 'It happened only recently', 'It only involved one person'], 0),
    ('The fur trade often relied on animals such as the ___.', ['Beaver', 'Penguin', 'Camel', 'Kangaroo'], 0)]),
]),
day(136, [
L('Sentence Fragments: Complete vs Incomplete Thoughts',
  'Grade 1 Language strand: a sentence fragment is an incomplete thought that is missing a subject, a verb, or both, unlike a complete sentence.',
  [('What is a sentence fragment?', ['an incomplete thought', 'a sentence missing something']),
   ('What might a fragment be missing?', ['a subject or a verb', 'a subject, verb, or both']),
   ('Give an example of a complete sentence.', ['The dog barked.', 'She read a book.'])],
  [('What is a sentence fragment?', ['A complete thought with a subject and verb', 'An incomplete thought missing a subject or verb', 'A question only', 'A very long sentence'], 1),
   ('Which of these is a sentence fragment?', ['Ran to the park.', 'The boy ran to the park.', 'The boy ran.', 'Did the boy run?'], 0),
   ('Which of these is a complete sentence?', ['Under the table.', 'The cat slept under the table.', 'Sleeping quietly.', 'Very tired today.'], 1),
   ('A complete sentence must have ___.', ['A subject and a verb', 'Only a subject', 'Only a verb', 'Neither a subject nor a verb'], 0),
   ('Why should writers avoid using sentence fragments in most writing?', ['Fragments do not express a complete thought', 'Fragments are always correct', 'Fragments are the same as questions', 'Fragments make writing clearer'], 0)]),
M('Length: Comparing Metres and Centimetres',
  'Grade 1 Math strand: students compare metres and centimetres, learning that a metre is a much longer unit made up of 100 centimetres.',
  [('Which is longer, a metre or a centimetre?', ['a metre', 'a metre is longer']),
   ('How many centimetres are in one metre?', ['100', 'one hundred']),
   ('Would you measure a pencil in metres or centimetres?', ['centimetres', 'centimetres because it is short'])],
  [('Which unit is longer, a metre or a centimetre?', ['A centimetre', 'A metre', 'They are the same', 'Neither is a unit of length'], 1),
   ('How many centimetres make up one metre?', ['10', '50', '100', '1000'], 2),
   ('Which would you most likely measure in centimetres?', ['A pencil', 'A hallway', 'A football field', 'A road'], 0),
   ('Which would you most likely measure in metres?', ['A crayon', 'A paperclip', 'A classroom', 'A fingernail'], 2),
   ('Choosing the right unit depends mostly on the ___ of the object.', ['Colour', 'Size', 'Smell', 'Weight'], 1)]),
Sc('Beavers: Canadas National Animal',
   'Grade 1 Science strand: the beaver is a large rodent and Canadas national animal, known for building dams and lodges out of sticks and mud.',
   [('What is Canadas national animal?', ['the beaver', 'a beaver']),
    ('What does a beaver build using sticks and mud?', ['a dam or lodge', 'dams and lodges']),
    ('What kind of animal is a beaver?', ['a rodent', 'a large rodent'])],
   [('Which animal is known as Canadas national animal?', ['The moose', 'The beaver', 'The polar bear', 'The loon'], 1),
    ('What does a beaver build using sticks and mud?', ['A dam or lodge', 'A nest in a tree', 'A web', 'A burrow underground only'], 0),
    ('What type of animal is a beaver?', ['A bird', 'A rodent', 'A reptile', 'A fish'], 1),
    ('Why might a beaver build a dam?', ['To create a pond that protects its home', 'To block roads for no reason', 'To fly higher', 'To make a nest in a tree'], 0),
    ('The beaver is a strong swimmer thanks to its ___.', ['Flat, paddle-like tail', 'Wings', 'Gills', 'Long legs'], 0)]),
SS('Orange Shirt Day: Every Child Matters',
   'Grade 1 Social Studies strand: Orange Shirt Day, on September 30, is a special day when Canadians wear orange to remember Indigenous children and show that every child matters.',
   [('What colour do people wear on Orange Shirt Day?', ['orange']),
    ('What is the message of Orange Shirt Day?', ['every child matters', 'that all children matter']),
    ('When is Orange Shirt Day?', ['September 30'])],
   [('What colour do people wear to take part in Orange Shirt Day?', ['Orange', 'Blue', 'Green', 'Purple'], 0),
    ('What is the main message of Orange Shirt Day?', ['Every child matters', 'Everyone should wear the same colour for fun', 'Only some children matter', 'Nothing important'], 0),
    ('When is Orange Shirt Day observed in Canada?', ['September 30', 'December 25', 'July 1', 'February 14'], 0),
    ('Orange Shirt Day helps Canadians remember and honour ___.', ['Indigenous children and their experiences', 'A sports team', 'A type of food', 'A weather event'], 0),
    ('Why is it important for schools to talk about Orange Shirt Day?', ['To show respect and help every child feel valued', 'It is not important', 'To ignore Canadian history', 'Only adults need to know about it'], 0)]),
]),
day(137, [
L('Syllables: Clapping the Beats in Words',
  'Grade 1 Language strand: students clap the beats, or syllables, in a word to help them read and spell longer words, such as clapping twice for the word rabbit.',
  [('How many syllables are in the word rabbit?', ['2', 'two']),
   ('How can we find syllables in a word?', ['clap each beat', 'clap the parts of the word']),
   ('How many syllables are in the word dinosaur?', ['3', 'three'])],
  [('How many syllables does the word rabbit have?', ['1', '2', '3', '4'], 1),
   ('What is a helpful way to find syllables in a word?', ['Clap for each beat you hear', 'Guess without listening', 'Count the letters only', 'Look at the pictures'], 0),
   ('How many syllables does the word sun have?', ['1', '2', '3', '4'], 0),
   ('How many syllables does the word dinosaur have?', ['1', '2', '3', '4'], 2),
   ('Knowing how to break a word into syllables can help with ___.', ['Reading and spelling', 'Drawing pictures', 'Counting money', 'Telling time'], 0)]),
M('Choosing the Right Measuring Tool',
  'Grade 1 Math strand: students choose the best tool for a measuring task, such as a ruler for a short object or a scale for weight.',
  [('What tool would you use to measure a pencils length?', ['a ruler', 'ruler']),
   ('What tool would you use to measure how heavy something is?', ['a scale', 'a balance scale']),
   ('Why is it important to choose the right measuring tool?', ['to get an accurate measurement', 'gives more accurate results'])],
  [('Which tool would best measure the length of a pencil?', ['A ruler', 'A scale', 'A clock', 'A thermometer'], 0),
   ('Which tool would best measure how heavy an object is?', ['A ruler', 'A scale', 'A calendar', 'A measuring cup'], 1),
   ('Which tool would best measure how much juice fills a cup?', ['A ruler', 'A scale', 'A measuring cup', 'A clock'], 2),
   ('Choosing the correct measuring tool helps us get results that are more ___.', ['Random', 'Accurate', 'Colourful', 'Confusing'], 1),
   ('Which tool would best measure the temperature outside?', ['A thermometer', 'A ruler', 'A scale', 'A measuring cup'], 0)]),
Sc('The Layers of the Atmosphere: Air Above Us',
   'Grade 1 Science strand: the atmosphere is made of layers of air that surround the Earth, protecting us and giving us air to breathe.',
   [('What is the atmosphere?', ['the layers of air around the Earth', 'air that surrounds the Earth']),
    ('What does the atmosphere give us to breathe?', ['air', 'oxygen']),
    ('Does the atmosphere help protect the Earth?', ['yes', 'yes it does'])],
   [('What is the atmosphere?', ['Layers of air that surround the Earth', 'A type of ocean', 'A layer of rock', 'A kind of cloud only'], 0),
    ('What does the atmosphere give living things to breathe?', ['Air', 'Water', 'Sunlight only', 'Sand'], 0),
    ('Does the atmosphere help protect Earth from some things in space?', ['Yes', 'No', 'Only at night', 'Only in winter'], 0),
    ('Which of these is part of the atmosphere?', ['The air we breathe', 'The rocky crust', 'The ocean floor', 'The core of the Earth'], 0),
    ('Without the atmosphere, Earth would not have ___ for living things to breathe.', ['Air', 'Sound', 'Colour', 'Gravity'], 0)]),
SS('Our Senate: Another Part of Canadas Government',
   'Grade 1 Social Studies strand: the Senate is a part of Canadas government that reviews new laws to help make sure they are fair before they are approved.',
   [('What is the Senate?', ['a part of Canadas government', 'a group that reviews laws']),
    ('What does the Senate help do with new laws?', ['review them', 'make sure they are fair']),
    ('Is the Senate part of how Canada is governed?', ['yes', 'yes it is'])],
   [('What is the Senate?', ['A part of Canadas government that reviews laws', 'A type of school', 'A sports team', 'A kind of store'], 0),
    ('What does the Senate help do before a new law is approved?', ['Review it to help make sure it is fair', 'Ignore it completely', 'Delete it right away', 'Sell it'], 0),
    ('Is the Senate part of how Canada is governed?', ['Yes', 'No', 'Only in one province', 'Only during elections'], 0),
    ('Learning about the Senate helps students understand ___.', ['How laws are made and reviewed in Canada', 'Nothing about government', 'Only foreign governments', 'A make-believe story'], 0),
    ('The Senate works alongside other parts of government, such as the ___.', ['Prime Minister and Parliament', 'School principal', 'Local bakery', 'Grocery store'], 0)]),
]),
day(138, [
L('Fact and Opinion: Two Kinds of Statements',
  'Grade 1 Language strand: a fact is a statement that can be proven true, while an opinion is what someone thinks or feels, and readers learn to tell them apart.',
  [('What is a fact?', ['a statement that can be proven true', 'something that is true']),
   ('What is an opinion?', ['what someone thinks or feels', 'a personal belief']),
   ('Give an example of an opinion.', ['ice cream is the best treat', 'summer is the best season'])],
  [('What is a fact?', ['Something that can be proven true', 'What someone thinks or feels', 'A made-up story', 'A rhyme'], 0),
   ('What is an opinion?', ['A statement that can be proven true', 'What someone thinks or feels', 'A math equation', 'A punctuation mark'], 1),
   ('Which of these is a fact?', ['Dogs are the best pets.', 'Dogs are mammals.', 'Dogs are cuter than cats.', 'Dogs should live inside.'], 1),
   ('Which of these is an opinion?', ['Water freezes at a low temperature.', 'Chocolate ice cream is the best flavour.', 'The sun rises in the east.', 'A triangle has three sides.'], 1),
   ('Learning to tell facts from opinions helps readers ___.', ['Understand what is proven versus what someone believes', 'Ignore all information', 'Confuse true and false randomly', 'Avoid reading altogether'], 0)]),
M('Estimating Groups of Ten',
  'Grade 1 Math strand: students estimate how many objects are in a large group by comparing it to a group of ten they can already count.',
  [('How can comparing to a group of ten help you estimate a larger group?', ['it gives a size reference', 'helps guess a reasonable amount']),
   ('If a group looks about twice the size of ten, about how many is it?', ['about 20', 'around 20']),
   ('Is an estimate the same as an exact count?', ['no', 'no it is a reasonable guess'])],
  [('Why is it helpful to compare a large group to a group of ten?', ['It gives a helpful reference for estimating', 'It has no use', 'It replaces exact counting always', 'It only works with pennies'], 0),
   ('If a group of objects looks about three times the size of ten, about how many objects are there?', ['About 13', 'About 20', 'About 30', 'About 40'], 2),
   ('An estimate based on a group of ten is meant to be ___.', ['The exact count with no guessing', 'A reasonable guess, not exact', 'Always wrong', 'Impossible to make'], 1),
   ('If a group looks smaller than ten, a good estimate might be ___.', ['20', '15', '5', '30'], 2),
   ('Estimating with groups of ten is a useful skill because it helps us ___.', ['Make a quick, reasonable guess', 'Avoid counting forever', 'Confuse numbers', 'Skip math entirely'], 0)]),
Sc('Turtles and Tortoises: Reptiles with Shells',
   'Grade 1 Science strand: turtles and tortoises are reptiles with hard shells that protect their bodies, and turtles usually live near water while tortoises live on land.',
   [('What protects the body of a turtle or tortoise?', ['a hard shell', 'their shell']),
    ('What kind of animal is a turtle or tortoise?', ['a reptile', 'they are reptiles']),
    ('Where do tortoises usually live?', ['on land', 'mostly on land'])],
   [('What protects a turtle or tortoises body?', ['A hard shell', 'Feathers', 'Fur', 'Scales only'], 0),
    ('What kind of animal are turtles and tortoises?', ['Mammals', 'Reptiles', 'Amphibians', 'Birds'], 1),
    ('Where do tortoises usually live?', ['Mostly on land', 'Only deep in the ocean', 'Only in trees', 'Only in the sky'], 0),
    ('Where do many turtles spend a lot of their time?', ['Near or in water', 'In the desert only', 'In snow only', 'In caves only'], 0),
    ('A turtles shell is an example of a body part that helps it ___.', ['Stay protected from danger', 'Fly higher', 'Breathe underwater like a fish', 'Change colour instantly'], 0)]),
SS('Our Court System: Judges and Fair Decisions',
   'Grade 1 Social Studies strand: courts are places where judges listen carefully and help make fair decisions when people disagree or when someone breaks a rule.',
   [('Who helps make fair decisions in a court?', ['a judge', 'judges']),
    ('When might people go to court?', ['when they disagree', 'when someone breaks a rule']),
    ('Why is fairness important in a court?', ['so decisions are fair for everyone', 'helps everyone be treated fairly'])],
   [('Who listens and helps make fair decisions in a court?', ['A judge', 'A firefighter', 'A pilot', 'A chef'], 0),
    ('When might people go to a court?', ['When they disagree or someone breaks a rule', 'To buy groceries', 'To watch a movie', 'To play a game'], 0),
    ('Why is it important for courts to be fair?', ['So everyone is treated fairly under the rules', 'Fairness does not matter', 'Only some people deserve fairness', 'Courts do not need to be fair'], 0),
    ('A judges main job is to help ___.', ['Make fair decisions', 'Cook meals', 'Deliver mail', 'Drive buses'], 0),
    ('Courts are an important part of how a community ___.', ['Solves disagreements fairly', 'Ignores all rules', 'Avoids helping people', 'Plans parties'], 0)]),
]),
day(139, [
L('Silent Letters: mb and gh',
  'Grade 1 Language strand: some letters in words are silent and not pronounced, such as the b in comb and the gh in night.',
  [('Is the b in comb pronounced?', ['no', 'no it is silent']),
   ('Is the gh in night pronounced?', ['no', 'no it is silent']),
   ('Give another word with a silent letter.', ['lamb', 'light'])],
  [('In the word comb, which letter is silent?', ['C', 'O', 'M', 'B'], 3),
   ('In the word night, which letters are silent?', ['N and I', 'G and H', 'T', 'None of them'], 1),
   ('Which word has a silent b?', ['Lamb', 'Bed', 'Ball', 'Big'], 0),
   ('Which word has a silent gh?', ['Light', 'Go', 'Home', 'Green'], 0),
   ('Silent letters in a word are letters that are written but ___.', ['Always capitalized', 'Not pronounced', 'The loudest sound', 'Removed from spelling'], 1)]),
M('Patterns on a Hundred Chart',
  'Grade 1 Math strand: students explore number patterns on a hundred chart, noticing how numbers going down a column increase by ten each time.',
  [('On a hundred chart, what happens to a number when you move down one row?', ['it increases by 10', 'goes up by ten']),
   ('What number is directly below 24 on a hundred chart?', ['34', 'thirty four']),
   ('What number is directly above 57 on a hundred chart?', ['47', 'forty seven'])],
  [('On a hundred chart, moving down one row changes the number by ___.', ['1', '5', '10', '100'], 2),
   ('What number is directly below 24 on a hundred chart?', ['25', '14', '34', '44'], 2),
   ('What number is directly above 57 on a hundred chart?', ['47', '56', '58', '67'], 0),
   ('On a hundred chart, moving one space to the right changes the number by ___.', ['1', '5', '10', '100'], 0),
   ('Patterns on a hundred chart help students understand ___.', ['Place value and counting patterns', 'Colours', 'Story characters', 'Weather'], 0)]),
Sc('Our Sense of Balance: How We Stay Upright',
   'Grade 1 Science strand: our body has a sense of balance, controlled by a part inside our ear, that helps us stand, walk, and ride a bike without falling.',
   [('What sense helps us stay upright?', ['our sense of balance', 'balance']),
    ('What body part helps control balance?', ['a part inside our ear', 'our inner ear']),
    ('Name an activity that requires good balance.', ['riding a bike', 'walking on a balance beam'])],
   [('What sense helps our body stay upright and steady?', ['Sense of taste', 'Sense of balance', 'Sense of smell', 'Sense of touch only'], 1),
    ('Which body part helps control our sense of balance?', ['Our elbow', 'A part inside our ear', 'Our knee', 'Our hair'], 1),
    ('Which activity relies heavily on good balance?', ['Riding a bicycle', 'Smelling a flower', 'Tasting food', 'Listening to a song'], 0),
    ('Our sense of balance helps prevent us from ___.', ['Hearing sounds', 'Falling over', 'Tasting food', 'Seeing colours'], 1),
    ('Walking along a narrow balance beam is a good test of our sense of ___.', ['Smell', 'Balance', 'Taste', 'Hearing'], 1)]),
SS('The Underground Railroad: A Journey to Freedom',
   'Grade 1 Social Studies strand: the Underground Railroad was a secret network of routes and helpers that guided people escaping slavery in the United States toward freedom, with many finding safety in Canada.',
   [('What was the Underground Railroad?', ['a secret network of routes to freedom', 'a path to freedom']),
    ('Where did many people travel to for safety and freedom?', ['Canada', 'freedom in Canada']),
    ('Why is the Underground Railroad an important story?', ['it shows courage and the search for freedom', 'people worked together to help others'])],
   [('What was the Underground Railroad?', ['A secret network of routes and helpers guiding people to freedom', 'An actual underground train', 'A modern subway system', 'A type of game'], 0),
    ('Many people who used the Underground Railroad were trying to reach ___.', ['Freedom, often in Canada', 'The moon', 'A different planet', 'A school'], 0),
    ('Why is the story of the Underground Railroad important to learn about?', ['It shows courage and the importance of freedom', 'It is not important', 'It was not a real event', 'It only matters in one country'], 0),
    ('People who helped others along the Underground Railroad were showing ___.', ['Bravery and kindness', 'Carelessness', 'Indifference', 'Unfairness'], 0),
    ('Learning about the Underground Railroad helps students understand ___.', ['An important part of history about freedom', 'A make-believe story', 'A modern invention', 'Something unrelated to history'], 0)]),
]),
day(140, [
L('Language Review: Vowel Teams, Prefixes, and Figurative Language',
  'Grade 1 Language strand review: students revisit the au and aw vowel teams, prefixes mis- and non-, adding -ly, personification, and fact versus opinion.',
  [('Give a word with the au or aw vowel team.', ['sauce', 'claw']),
   ('What does the prefix non- usually mean?', ['not or without']),
   ('What is a fact?', ['a statement that can be proven true'])],
  [('Which word has the aw vowel team?', ['Claw', 'Cup', 'Dog', 'Run'], 0),
   ('What does the word nonstop mean?', ['Stopping often', 'Without stopping', 'Stopping once', 'Never starting'], 1),
   ('What word do we get by adding -ly to quick?', ['Quicker', 'Quickly', 'Quickest', 'Quickable'], 1),
   ('Which sentence uses personification?', ['The wind blew hard.', 'The wind whispered through the trees.', 'The wind is cold.', 'Is the wind strong?'], 1),
   ('Which of these is a fact?', ['Dogs are the best pets.', 'Dogs are mammals.', 'Dogs are cuter than cats.', 'Dogs should live inside.'], 1)]),
M('Math Review: Skip Counting, Time, and Number Patterns',
  'Grade 1 Math strand review: students revisit skip counting by 20s, numbers to 300, time to the nearest five minutes, doubling, and hundred chart patterns.',
  [('What comes after 20, 40, 60?', ['80']),
   ('What number comes right before 300?', ['299']),
   ('What is double 14?', ['28'])],
  [('What comes next: 20, 40, 60, ___?', ['70', '75', '80', '90'], 2),
   ('What number comes right before 300?', ['290', '295', '298', '299'], 3),
   ('If the minute hand points to the 2, how many minutes past the hour is it?', ['2', '5', '10', '20'], 2),
   ('What is double 25?', ['40', '45', '50', '55'], 2),
   ('On a hundred chart, moving down one row changes the number by ___.', ['1', '5', '10', '100'], 2)]),
Sc('Science Review: Ocean Life, Earth, and Our Bodies',
   'Grade 1 Science strand review: students revisit octopuses and squid, desert animals, layers of the earth, our joints, beavers, the atmosphere, and our sense of balance.',
   [('Do octopuses have bones inside their bodies?', ['no']),
    ('What is the layer at the very centre of the Earth called?', ['the core']),
    ('What sense helps us stay upright?', ['our sense of balance'])],
   [('Do octopuses have bones inside their bodies?', ['Yes', 'No', 'Only in their arms', 'Only when young'], 1),
    ('Which of these is a desert animal?', ['Camel', 'Polar bear', 'Penguin', 'Salmon'], 0),
    ('What is the layer at the very centre of the Earth called?', ['The crust', 'The mantle', 'The core', 'The atmosphere'], 2),
    ('Which animal is known as Canadas national animal?', ['The moose', 'The beaver', 'The polar bear', 'The loon'], 1),
    ('What sense helps our body stay upright and steady?', ['Sense of taste', 'Sense of balance', 'Sense of smell', 'Sense of touch only'], 1)]),
SS('Social Studies Review: Leaders, Land, and Our History',
   'Grade 1 Social Studies strand review: students revisit our school principal, the Canadian Shield, Sir John A Macdonald, the fur trade, Orange Shirt Day, and the Underground Railroad.',
   [('What is the main role of a school principal?', ['leading and supporting the whole school']),
    ('What colour do people wear on Orange Shirt Day?', ['orange']),
    ('What was the Underground Railroad?', ['a secret network of routes to freedom'])],
   [('What is the main role of a school principal?', ['Leading and supporting the whole school', 'Driving the school bus', 'Cooking lunch', 'Cleaning the hallways'], 0),
    ('What is the Canadian Shield?', ['A huge rocky land region in Canada', 'A type of building', 'A small city park', 'A kind of vehicle'], 0),
    ('Who was Canadas first prime minister?', ['Sir John A Macdonald', 'Terry Fox', 'A mayor', 'A premier'], 0),
    ('What colour do people wear to take part in Orange Shirt Day?', ['Orange', 'Blue', 'Green', 'Purple'], 0),
    ('What was the Underground Railroad?', ['A secret network of routes and helpers guiding people to freedom', 'An actual underground train', 'A modern subway system', 'A type of game'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_131_140)
    append_worksheet_days(1, g1_131_140)
