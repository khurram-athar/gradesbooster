#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 121-130 -- tenth batch, extending Grade 0
past Day 120 toward the full ~187-day school year. Self-contained script
(does NOT use gen_curriculum.py's sub()/day()/append_to(), since those do
not support a worksheet field) modeled exactly on gen_grade0_days111_120.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by fetch_video_ids.py)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 0 Days 1-120 (see
data/grade0.ts / data/grade0.json): new word families (-ip, -op), synonyms,
the un- prefix, comparing stories, reading comprehension, letter formation,
command sentences, and rhyming families for Language; cone and pyramid
solids, counting to 120, quarter-hour time, skip counting by 3s, equal and
unequal fraction parts, comparing area, counting groups of coins, real
graphs, and number bonds to 4 for Math; the solar system, stars, reptiles,
amphibians, bats, underground animals, blood, extreme weather, and solar
energy for Science; and Terry Fox, Canada Day, First Nations/Metis/Inuit
peoples, the school principal, farmers markets, public transit, fire
drills, fair play, and comparing toys then and now for Social Studies --
none of those exact ideas appear in Days 1-120. Day 130 is a review day
across all four subjects, matching the end-of-batch pattern used in every
prior 10-day batch. No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/quiz/worksheet text --
contractions and possessives are avoided entirely for kindergarten
readability and to keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260730):
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


g0_121_130 = [
day(121, [
L('Word Families: -ip Words',
  'Kindergarten Language strand: the -ip word family shares the same ending sound, as in dip, hip, rip, and zip.',
  [('Name a word that rhymes with hip.', ['dip', 'rip', 'zip', 'lip']),
   ('What ending sound do dip and rip share?', ['ip', 'the ip sound']),
   ('Is tip part of the -ip family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -ip family?', ['Cat', 'Zip', 'Bag', 'Sun'], 1),
   ('Which word rhymes with lip?', ['Lap', 'Lot', 'Rip', 'Log'], 2),
   ('Which word does NOT belong to the -ip family?', ['Dip', 'Hip', 'Rip', 'Run'], 3),
   ('Complete the rhyme: The boat began to ___.', ['tip', 'tap', 'top', 'ten'], 0),
   ('Words in the same word family share the same ___.', ['Colour', 'Ending sound', 'First letter', 'Meaning'], 1)]),
M('3D Shapes: Cone and Pyramid',
  'Kindergarten Math strand: students identify two new solid shapes, the cone, which has a round base and a point, and the pyramid, which has flat triangular sides meeting at a point.',
  [('Name something shaped like a cone.', ['an ice cream cone', 'a party hat']),
   ('How many points does a cone have?', ['1', 'one']),
   ('Name something shaped like a pyramid.', ['a pyramid in Egypt', 'a tent'])],
  [('Which real object is shaped like a cone?', ['A ball', 'An ice cream cone', 'A box', 'A can'], 1),
   ('A cone has a round base and comes to a ___.', ['Flat top', 'Point', 'Square edge', 'Curve only'], 1),
   ('Which shape has flat triangular sides that meet at a point?', ['Sphere', 'Cylinder', 'Pyramid', 'Cube'], 2),
   ('Which object looks like a pyramid?', ['A soccer ball', 'An Egyptian pyramid', 'A soup can', 'A shoebox'], 1),
   ('How many points does a cone have?', ['0', '1', '2', '4'], 1)]),
Sc('The Solar System: The Sun and Planets',
   'Kindergarten Science strand: the solar system is made up of the Sun at the centre and planets, including Earth, that travel around it.',
   [('What is at the centre of our solar system?', ['the Sun', 'Sun']),
    ('Name the planet we live on.', ['Earth']),
    ('Do planets move around the Sun?', ['yes', 'yes they orbit it'])],
   [('What is at the centre of our solar system?', ['The Moon', 'The Sun', 'Earth', 'A star far away'], 1),
    ('What is the name of the planet we live on?', ['Mars', 'Earth', 'Venus', 'Jupiter'], 1),
    ('Planets travel around the Sun in a path called an ___.', ['Orbit', 'Ocean', 'Island', 'Eclipse'], 0),
    ('The solar system includes the Sun and ___.', ['Only clouds', 'Planets that travel around it', 'Only oceans', 'Only the Moon'], 1),
    ('Which of these is part of our solar system?', ['Earth', 'A river', 'A forest', 'A city'], 0)]),
SS('Terry Fox: A Canadian Hero',
   'Kindergarten Social Studies strand: Terry Fox was a brave Canadian who ran across much of Canada to raise money for cancer research, inspiring people every year.',
   [('What did Terry Fox do to raise money?', ['ran across Canada', 'ran a marathon']),
    ('What was Terry Fox trying to help find a cure for?', ['cancer', 'cancer research']),
    ('Why do people remember Terry Fox every year?', ['he was brave and inspiring', 'his courage'])],
   [('What is Terry Fox best known for?', ['Building bridges', 'Running across Canada to raise money for cancer research', 'Leading the government', 'Flying airplanes'], 1),
    ('Why did Terry Fox run across Canada?', ['For fun only', 'To raise money for cancer research', 'To visit family', 'To sell food'], 1),
    ('What do many schools do every year in honour of Terry Fox?', ['Hold a Terry Fox run or walk', 'Ignore the day', 'Close for a month', 'Nothing at all'], 0),
    ('Terry Fox is remembered as a Canadian ___.', ['Villain', 'Hero', 'Stranger', 'Athlete only for fun'], 1),
    ('What quality did Terry Fox show by running despite being unwell?', ['Bravery', 'Carelessness', 'Laziness', 'Unkindness'], 0)]),
]),
day(122, [
L('Word Families: -op Words',
  'Kindergarten Language strand: the -op word family shares the same ending sound, as in hop, mop, pop, and top.',
  [('Name a word that rhymes with hop.', ['mop', 'pop', 'top', 'stop']),
   ('What ending sound do mop and top share?', ['op', 'the op sound']),
   ('Is chop part of the -op family?', ['yes', 'yes it is'])],
  [('Which word belongs to the -op family?', ['Sit', 'Top', 'Bed', 'Run'], 1),
   ('Which word rhymes with pop?', ['Pin', 'Hop', 'Pen', 'Pig'], 1),
   ('Which word does NOT belong to the -op family?', ['Hop', 'Mop', 'Pop', 'Pig'], 3),
   ('Complete the rhyme: The bunny likes to ___.', ['hop', 'hat', 'hen', 'hid'], 0),
   ('Learning word families helps us read new words by ___.', ['Guessing randomly', 'Spotting the shared pattern', 'Skipping them', 'Ignoring letters'], 1)]),
M('Counting to 120: Beyond 100',
  'Kindergarten Math strand: students extend counting past 100, learning that after 100 comes 101, 102, and continuing up to 120.',
  [('What number comes right after 100?', ['101', 'one hundred one']),
   ('What number comes right after 109?', ['110', 'one hundred ten']),
   ('Count from 117 to 120.', ['117,118,119,120', '117 118 119 120'])],
  [('What number comes right after 100?', ['99', '100', '101', '110'], 2),
   ('What number comes right after 119?', ['118', '120', '121', '100'], 1),
   ('Which number is greater than 100?', ['99', '95', '105', '80'], 2),
   ('What number comes right before 110?', ['109', '111', '100', '108'], 0),
   ('Counting past 100 continues in the same way as ___.', ['Counting past 10', 'A totally new pattern', 'Backwards counting', 'Skip counting only'], 0)]),
Sc('Stars: Twinkling Lights in the Night Sky',
   'Kindergarten Science strand: stars are giant balls of hot glowing gas that we see twinkling as tiny points of light in the night sky.',
   [('When can we usually see stars?', ['at night', 'nighttime']),
    ('What are stars made of?', ['hot glowing gas', 'burning gas']),
    ('Do stars look big or small from Earth?', ['small', 'tiny points of light'])],
   [('When do we usually see stars in the sky?', ['During the day', 'At night', 'Only in winter', 'Never'], 1),
    ('Stars are giant balls of hot glowing ___.', ['Rock', 'Gas', 'Water', 'Ice'], 1),
    ('Why do stars look tiny from Earth?', ['They are very far away', 'They are actually tiny', 'They are hiding', 'They are not real'], 0),
    ('What is the closest star to Earth?', ['The Moon', 'The Sun', 'A planet', 'A comet'], 1),
    ('Stars appear to ___ in the night sky.', ['Twinkle', 'Melt', 'Bounce', 'Sing'], 0)]),
SS('Canada Day: Celebrating Our Country',
   'Kindergarten Social Studies strand: Canada Day is a special holiday on July 1st when people celebrate our country with parades, fireworks, and the colours red and white.',
   [('What date is Canada Day celebrated on?', ['July 1st', 'July 1']),
    ('Name one way people celebrate Canada Day.', ['fireworks', 'parades']),
    ('What colours are often seen on Canada Day?', ['red and white', 'red and white like the flag'])],
   [('On what date is Canada Day celebrated?', ['July 1st', 'December 25th', 'October 31st', 'January 1st'], 0),
    ('What does Canada Day celebrate?', ['Our country, Canada', 'A different country', 'A single city', 'Nothing special'], 0),
    ('Which colours are often worn on Canada Day?', ['Blue and yellow', 'Red and white', 'Green and orange', 'Purple and black'], 1),
    ('Which is a common way to celebrate Canada Day?', ['Watching fireworks', 'Raking leaves', 'Shovelling snow', 'Staying inside all day'], 0),
    ('Canada Day helps people show ___ for their country.', ['Pride and celebration', 'Anger', 'Fear', 'Boredom'], 0)]),
]),
day(123, [
L('Synonyms: Words That Mean the Same',
  'Kindergarten Language strand: synonyms are different words that mean almost the same thing, such as happy and glad, or big and large.',
  [('Give a word that means the same as happy.', ['glad', 'joyful']),
   ('Give a word that means the same as big.', ['large', 'huge']),
   ('What do we call words that mean almost the same thing?', ['synonyms', 'synonym'])],
  [('Which word means the same as happy?', ['Sad', 'Glad', 'Angry', 'Tired'], 1),
   ('Which word means the same as big?', ['Tiny', 'Large', 'Short', 'Thin'], 1),
   ('Words that mean almost the same thing are called ___.', ['Opposites', 'Synonyms', 'Nouns', 'Verbs'], 1),
   ('Which pair of words are synonyms?', ['Hot and cold', 'Fast and quick', 'Up and down', 'Day and night'], 1),
   ('Which word means the same as small?', ['Little', 'Giant', 'Wide', 'Tall'], 0)]),
M('Time: Reading a Clock to the Quarter Hour',
  'Kindergarten Math strand: students read a clock to the quarter hour, recognizing when the minute hand points to the 3 for quarter past.',
  [('When the minute hand points to the 3, how many minutes past the hour is it?', ['15', 'fifteen']),
   ('What do we call 15 minutes past the hour?', ['quarter past', 'a quarter past']),
   ('If it is quarter past 2, what time is that?', ['2:15', 'two fifteen'])],
  [('When the minute hand points to the 3, it is ___ minutes past the hour.', ['5', '10', '15', '30'], 2),
   ('What do we call 15 minutes past the hour?', ['Half past', 'Quarter past', 'Quarter to', 'A full hour'], 1),
   ('If it is quarter past 4, what time does the clock show?', ['4:00', '4:15', '4:30', '4:45'], 1),
   ('The minute hand pointing at the 3 means the clock shows a ___.', ['Half hour', 'Quarter hour', 'Full hour', 'Second'], 1),
   ('Quarter past an hour is how many minutes after that hour?', ['10 minutes', '15 minutes', '20 minutes', '30 minutes'], 1)]),
Sc('Reptiles: Scaly Animals That Bask in the Sun',
   'Kindergarten Science strand: reptiles, such as snakes, lizards, and turtles, have dry scaly skin and often bask in the sun to stay warm.',
   [('Name one kind of reptile.', ['snake', 'lizard', 'turtle']),
    ('What covers a reptiles skin?', ['scales', 'dry scales']),
    ('Why do reptiles bask in the sun?', ['to stay warm', 'to warm up'])],
   [('Which of these is a reptile?', ['Frog', 'Snake', 'Fish', 'Bird'], 1),
    ('What covers the skin of a reptile?', ['Feathers', 'Fur', 'Scales', 'Slime'], 2),
    ('Why do reptiles often bask in the sun?', ['To cool down', 'To stay warm', 'To hide', 'To sleep forever'], 1),
    ('Which animal is NOT a reptile?', ['Turtle', 'Lizard', 'Rabbit', 'Snake'], 2),
    ('Reptile skin is usually ___.', ['Wet and slimy', 'Dry and scaly', 'Covered in fur', 'Covered in feathers'], 1)]),
SS('First Nations, Metis, and Inuit: Peoples of Canada',
   'Kindergarten Social Studies strand: First Nations, Metis, and Inuit peoples are the Indigenous peoples of Canada, each with their own rich histories and traditions.',
   [('Name one Indigenous group in Canada.', ['First Nations', 'Metis', 'Inuit']),
    ('Have Indigenous peoples lived in Canada for a long time?', ['yes', 'yes a very long time']),
    ('Why is it important to learn about Indigenous peoples?', ['to respect their history and cultures', 'learn about Canada'])],
   [('Which are the three main groups of Indigenous peoples in Canada?', ['First Nations, Metis, and Inuit', 'Farmers, teachers, and doctors', 'North, South, and East', 'Kings, queens, and princes'], 0),
    ('How long have Indigenous peoples lived on this land?', ['A few years', 'A very long time', 'Since last year', 'They have not lived here'], 1),
    ('Why is it important to learn about First Nations, Metis, and Inuit peoples?', ['To respect their histories and cultures', 'It is not important', 'Only for one day a year', 'To ignore their stories'], 0),
    ('Each Indigenous group in Canada has its own ___.', ['Identical culture', 'Unique traditions and history', 'No traditions at all', 'The same language everywhere'], 1),
    ('Learning about Indigenous peoples helps students understand ___.', ['Nothing new', 'An important part of Canadas story', 'Only modern Canada', 'A made-up story'], 1)]),
]),
day(124, [
L('Prefixes: Adding Un- to Change Meaning',
  'Kindergarten Language strand: adding the prefix un- to the start of a word can change its meaning to the opposite, such as changing happy to unhappy.',
  [('What does adding un- to happy make?', ['unhappy', 'it makes unhappy']),
   ('What does unhappy mean?', ['not happy', 'the opposite of happy']),
   ('What is a prefix?', ['letters added to the start of a word', 'word part at the beginning'])],
  [('What do we call letters added to the beginning of a word?', ['A suffix', 'A prefix', 'A vowel team', 'A pronoun'], 1),
   ('What does adding un- to the word happy create?', ['Happier', 'Unhappy', 'Happily', 'Happiness'], 1),
   ('What does the word unfair mean?', ['Very fair', 'Not fair', 'More fair', 'A kind of game'], 1),
   ('Adding un- to a word usually gives it the ___ meaning.', ['Same', 'Opposite', 'Longer', 'Louder'], 1),
   ('Which word means the opposite of kind, using un-?', ['Kindly', 'Unkind', 'Kindness', 'Kinder'], 1)]),
M('Skip Counting by 3s to 30',
  'Kindergarten Math strand: students skip count by 3s, saying 3, 6, 9, 12, and continuing on up to 30.',
  [('What number comes after 3, 6, 9?', ['12', 'twelve']),
   ('Skip count by 3s from 3 to 15.', ['3,6,9,12,15', '3 6 9 12 15']),
   ('What number comes right before 30 when skip counting by 3s?', ['27', 'twenty seven'])],
  [('What comes next: 3, 6, 9, ___?', ['10', '11', '12', '13'], 2),
   ('What comes next: 12, 15, 18, ___?', ['19', '20', '21', '22'], 2),
   ('When skip counting by 3s, what number comes after 21?', ['22', '23', '24', '25'], 2),
   ('Skip counting by 3s means we add ___ each time.', ['1', '2', '3', '5'], 2),
   ('Which list correctly skip counts by 3s?', ['3, 6, 9, 12', '3, 5, 7, 9', '3, 6, 10, 13', '3, 4, 5, 6'], 0)]),
Sc('Amphibians: Living on Land and in Water',
   'Kindergarten Science strand: amphibians, such as frogs and salamanders, can live both on land and in water and often start life swimming.',
   [('Name one kind of amphibian.', ['frog', 'salamander', 'toad']),
    ('Where can amphibians live?', ['land and water', 'both land and water']),
    ('What do many baby amphibians do first?', ['swim', 'live in water'])],
   [('Which of these is an amphibian?', ['Frog', 'Snake', 'Eagle', 'Cow'], 0),
    ('Amphibians can live in ___.', ['Only water', 'Only land', 'Both land and water', 'Only air'], 2),
    ('What do many baby amphibians do before becoming adults?', ['Fly', 'Swim in water', 'Live in trees', 'Hibernate immediately'], 1),
    ('Which is an example of an amphibian besides a frog?', ['Salamander', 'Turtle', 'Lizard', 'Snake'], 0),
    ('Amphibians usually have skin that is ___.', ['Dry and scaly', 'Moist', 'Covered in feathers', 'Covered in fur'], 1)]),
SS('Our School Principal: Leading Our School',
   'Kindergarten Social Studies strand: the school principal is a leader who helps keep the whole school safe, organized, and running smoothly every day.',
   [('Who is the leader of a school?', ['the principal', 'school principal']),
    ('Name one job of a principal.', ['keep the school safe', 'help teachers and students']),
    ('Why is a principal important to a school community?', ['helps everything run smoothly', 'leads the school'])],
   [('Who is the leader of a school?', ['The bus driver', 'The principal', 'A student', 'A visitor'], 1),
    ('Which is a job of the school principal?', ['Keeping the school safe and organized', 'Driving the bus', 'Delivering mail', 'Selling groceries'], 0),
    ('Why might a student visit the principals office?', ['For help with a problem or an announcement', 'To buy food', 'To catch a bus', 'To swim'], 0),
    ('The principal helps the whole ___ run smoothly.', ['Grocery store', 'School', 'Airport', 'Hospital'], 1),
    ('A good school leader treats everyone with ___.', ['Unkindness', 'Respect and fairness', 'Silence', 'Confusion'], 1)]),
]),
day(125, [
L('Story Comparison: How Two Stories Are Alike and Different',
  'Kindergarten Language strand: students compare two stories to notice ways the characters, settings, or events are alike and ways they are different.',
  [('Name two stories you know well.', ['any two familiar stories']),
   ('Give one way two stories can be alike.', ['same kind of character', 'similar setting']),
   ('Give one way two stories can be different.', ['different ending', 'different setting'])],
  [('When we compare two stories, we look for ways they are ___.', ['Alike and different', 'Loud and quiet', 'Long and short only', 'Colourful'], 0),
   ('Which is something we could compare between two stories?', ['The characters', 'The weather outside', 'The classroom colour', 'Todays date'], 0),
   ('If both stories have a brave character, that is an example of a ___.', ['Difference', 'Similarity', 'Setting', 'Title'], 1),
   ('If one story happens in a forest and another in a city, that is a ___.', ['Similarity', 'Difference', 'Rhyme', 'Prefix'], 1),
   ('Comparing two stories helps readers ___.', ['Forget both stories', 'Think more deeply about each one', 'Avoid reading', 'Skip the pictures'], 1)]),
M('Fractions: Equal and Unequal Parts',
  'Kindergarten Math strand: students look at shapes cut into pieces to decide whether the parts are equal in size or unequal in size.',
  [('If a circle is cut into two same-size pieces, are the parts equal?', ['yes', 'yes equal']),
   ('If a square is cut into one big piece and one small piece, are the parts equal?', ['no', 'no unequal']),
   ('Why does it matter if parts are equal when sharing?', ['so everyone gets a fair share', 'fairness'])],
  [('If a shape is cut into two same-size pieces, the parts are ___.', ['Unequal', 'Equal', 'Missing', 'Too many'], 1),
   ('If one piece is much bigger than the other, the parts are ___.', ['Equal', 'Unequal', 'The same', 'Whole'], 1),
   ('Why is it important for shared pieces to be equal?', ['So everyone gets a fair amount', 'So one person gets more', 'It does not matter', 'So pieces disappear'], 0),
   ('Which shows equal parts?', ['A circle cut into two same-size halves', 'A circle cut into one tiny and one huge piece', 'A whole uncut circle', 'A square with no cuts'], 0),
   ('Cutting a sandwich into two matching halves gives ___ parts.', ['Unequal', 'Equal', 'Extra', 'Zero'], 1)]),
Sc('Bats: Mammals That Fly at Night',
   'Kindergarten Science strand: bats are the only mammals that can truly fly, and most are nocturnal, coming out to hunt insects at night.',
   [('When are most bats active?', ['at night', 'nighttime']),
    ('Are bats mammals or birds?', ['mammals', 'they are mammals']),
    ('What do many bats eat?', ['insects', 'bugs'])],
   [('Bats are the only ___ that can truly fly.', ['Birds', 'Mammals', 'Reptiles', 'Fish'], 1),
    ('Most bats are active ___.', ['During the day', 'At night', 'Underwater', 'Never'], 1),
    ('What do many bats eat?', ['Insects', 'Only leaves', 'Rocks', 'Metal'], 0),
    ('Is a bat a bird?', ['Yes', 'No, it is a mammal', 'Only baby bats are birds', 'Bats are fish'], 1),
    ('An animal that is mostly active at night is called ___.', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0)]),
SS('Our Farmers Market: Buying Fresh Food',
   'Kindergarten Social Studies strand: a farmers market is a place where local farmers sell fresh fruits, vegetables, and other foods directly to the community.',
   [('Who sells food at a farmers market?', ['local farmers', 'farmers']),
    ('Name one thing you might buy at a farmers market.', ['fruit', 'vegetables']),
    ('Why do people like shopping at a farmers market?', ['fresh local food', 'support local farmers'])],
   [('Who sells food directly at a farmers market?', ['Local farmers', 'Doctors', 'Firefighters', 'Teachers'], 0),
    ('What kinds of food can you often buy at a farmers market?', ['Fresh fruits and vegetables', 'Only candy', 'Only toys', 'Only clothing'], 0),
    ('Why might a community enjoy having a farmers market?', ['It supports local farmers and offers fresh food', 'It has no benefit', 'It only sells old food', 'It closes the town'], 0),
    ('A farmers market is different from a grocery store because ___.', ['It sells food directly from local farmers', 'It never sells food', 'It only sells books', 'It is the same as a hospital'], 0),
    ('Buying food from a farmers market helps support ___.', ['People in other countries only', 'Local farmers in our community', 'No one at all', 'Only large companies'], 1)]),
]),
day(126, [
L('Reading Comprehension: Answering Questions About What We Read',
  'Kindergarten Language strand: after listening to a story, students answer simple questions to show they understood who, what, and where.',
  [('After a story, what question word asks about a character?', ['who', 'who is it about']),
   ('What question word asks about the place in a story?', ['where', 'where does it happen']),
   ('Why do we answer questions after a story?', ['to show we understood it', 'check understanding'])],
  [('The question word who asks about a story ___.', ['Character', 'Colour', 'Number', 'Sound'], 0),
   ('The question word where asks about a story ___.', ['Setting or place', 'Character', 'Ending only', 'Title'], 0),
   ('Answering questions after a story helps show ___.', ['We fell asleep', 'We understood the story', 'We changed the story', 'Nothing at all'], 1),
   ('Which question could you ask about a story?', ['What happened first?', 'What is your address?', 'What time is it?', 'What did you eat?'], 0),
   ('A good listener can answer questions about ___.', ['A story they heard', 'A song they never heard', 'A place they never visited', 'Nothing in particular'], 0)]),
M('Measurement: Comparing Area, Which Covers More',
  'Kindergarten Math strand: students compare two flat shapes to see which one covers more space on a table.',
  [('If one piece of paper covers more of the table, is it bigger or smaller?', ['bigger', 'it is bigger']),
   ('What can you use to compare how much space two shapes cover?', ['lay them side by side', 'place them next to each other']),
   ('Name something in your room that covers a lot of space.', ['a rug', 'a table'])],
  [('Which shape covers more of a table, a large blanket or a small napkin?', ['The napkin', 'The blanket', 'They are the same', 'Neither covers space'], 1),
   ('To compare how much space two shapes cover, we can ___.', ['Guess without looking', 'Lay them next to each other', 'Ignore them', 'Count their colours'], 1),
   ('A bigger piece of paper covers ___ space than a smaller one.', ['Less', 'More', 'The same', 'No'], 1),
   ('Comparing which shape covers more space is comparing their ___.', ['Weight', 'Area', 'Sound', 'Smell'], 1),
   ('Which object likely covers the most area on the floor?', ['A coin', 'A rug', 'A pencil', 'A button'], 1)]),
Sc('Underground Animals: Burrows and Tunnels',
   'Kindergarten Science strand: some animals, like rabbits, moles, and ants, dig burrows and tunnels underground to live and stay safe.',
   [('Name one animal that digs underground.', ['rabbit', 'mole', 'ant']),
    ('What do we call the underground home an animal digs?', ['a burrow', 'burrow or tunnel']),
    ('Why might an animal live underground?', ['to stay safe', 'protection and shelter'])],
   [('Which animal is known for digging underground burrows?', ['Rabbit', 'Eagle', 'Whale', 'Penguin'], 0),
    ('What do we call an underground home dug by an animal?', ['A nest', 'A burrow', 'A hive', 'A web'], 1),
    ('Why do many animals live underground?', ['To stay safe from danger', 'To fly higher', 'To swim faster', 'For no reason'], 0),
    ('Which tiny insect is known for digging tunnels?', ['Bee', 'Ant', 'Butterfly', 'Ladybug'], 1),
    ('Underground burrows can help protect animals from ___.', ['Predators and bad weather', 'Sunshine only', 'Water only', 'Nothing at all'], 0)]),
SS('Public Transit: Riding the Subway or Train',
   'Kindergarten Social Studies strand: public transit, such as subways and trains, helps many people travel around a city together instead of using separate cars.',
   [('Name one type of public transit.', ['subway', 'train']),
    ('Why do many people use public transit?', ['to travel together', 'share transportation']),
    ('Name one rule for riding public transit safely.', ['stay seated', 'hold on'])],
   [('Which of these is a form of public transit?', ['A bicycle', 'A subway train', 'A private car', 'A skateboard'], 1),
    ('Why do cities have public transit like subways and trains?', ['To help many people travel together', 'To keep people at home', 'They have no purpose', 'Only for one person to use'], 0),
    ('Which is a good safety rule when riding a subway or train?', ['Standing near the edge of the platform', 'Holding on and staying seated', 'Running through the doors', 'Yelling loudly'], 1),
    ('Public transit can help reduce the number of ___ on the road.', ['Trees', 'Cars', 'Buildings', 'Sidewalks'], 1),
    ('A subway usually travels ___.', ['Underground', 'In the sky', 'On the ocean', 'Underwater only'], 0)]),
]),
day(127, [
L('Letter Formation: Writing Neatly on the Line',
  'Kindergarten Language strand: students practise forming letters carefully, starting at the top and keeping letters sitting neatly on the writing line.',
  [('Where should most letters start when writing?', ['at the top', 'from the top']),
   ('Where should letters sit when we write them?', ['on the line', 'on the writing line']),
   ('Why is it important to write neatly?', ['so others can read it', 'easy to read'])],
  [('Most letters should start at the ___ when we write them.', ['Bottom', 'Top', 'Middle', 'Side'], 1),
   ('Where should letters sit on the page?', ['Above the line', 'Below the line', 'On the writing line', 'Off the page'], 2),
   ('Why do we practise neat letter formation?', ['So our writing is easy to read', 'So writing takes longer', 'It does not matter', 'To make letters bigger only'], 0),
   ('Which is a good habit when forming letters?', ['Starting in a random spot', 'Starting at the top and following the line', 'Writing very fast without care', 'Skipping some letters'], 1),
   ('Writing neatly on the line helps other people ___.', ['Ignore our writing', 'Read our writing clearly', 'Guess our writing', 'Erase our writing'], 1)]),
M('Money: Counting Groups of Coins Together',
  'Kindergarten Math strand: students count small groups of coins together, such as adding two pennies and one nickel to find the total value.',
  [('What is the value of 2 pennies together?', ['2 cents', 'two cents']),
   ('What is the value of 1 nickel and 1 penny together?', ['6 cents', 'six cents']),
   ('Which coin is worth more, a nickel or a penny?', ['a nickel', 'nickel'])],
  [('2 pennies and 1 nickel together are worth ___.', ['5 cents', '6 cents', '7 cents', '10 cents'], 2),
   ('Which group of coins is worth more?', ['3 pennies', '1 nickel', '2 pennies', '1 penny'], 1),
   ('1 nickel and 1 nickel together equal ___.', ['5 cents', '10 cents', '15 cents', '1 cent'], 1),
   ('To find the total value of a group of coins, we ___.', ['Guess', 'Add their values together', 'Ignore them', 'Count the coins only, not value'], 1),
   ('3 pennies together are worth ___.', ['1 cent', '2 cents', '3 cents', '5 cents'], 2)]),
Sc('Our Blood: Carrying What Our Body Needs',
   'Kindergarten Science strand: blood travels through our body carrying oxygen and nutrients that our body needs to stay healthy and strong.',
   [('What does blood carry around our body?', ['oxygen and nutrients', 'things our body needs']),
    ('What body part pumps blood around?', ['the heart', 'heart']),
    ('Why is blood important?', ['it carries what our body needs', 'keeps us healthy'])],
   [('What does blood carry to different parts of our body?', ['Only water', 'Oxygen and nutrients', 'Only air', 'Nothing'], 1),
    ('What body part pumps blood through our body?', ['The lungs', 'The heart', 'The brain', 'The stomach'], 1),
    ('Why does our body need blood?', ['To carry what our body needs to stay healthy', 'It has no purpose', 'Only to make us cold', 'Blood is not needed'], 0),
    ('Blood travels through tiny paths in our body called ___.', ['Bones', 'Blood vessels', 'Muscles', 'Nerves'], 1),
    ('Which of these does blood carry to our cells?', ['Oxygen', 'Sunlight', 'Sound', 'Colour'], 0)]),
SS('Fire Drills: Practising to Stay Safe',
   'Kindergarten Social Studies strand: a fire drill is a practice where the whole school calmly walks outside so everyone knows what to do in a real emergency.',
   [('What is a fire drill?', ['a practice for emergencies', 'practising what to do']),
    ('What should you do when the fire alarm rings during a drill?', ['walk calmly outside', 'line up and go outside']),
    ('Why do schools practise fire drills?', ['to be ready for a real emergency', 'so everyone knows what to do'])],
   [('What is the purpose of a fire drill?', ['To practise leaving the building safely', 'To have extra recess', 'To scare students', 'To skip class forever'], 0),
    ('What should students do when a fire drill begins?', ['Run wildly', 'Walk calmly and follow the teacher', 'Hide under a desk', 'Ignore it'], 1),
    ('Why do schools practise fire drills regularly?', ['So everyone knows what to do in a real emergency', 'They are not helpful', 'Only teachers need to know', 'For fun only'], 0),
    ('During a fire drill, where do students usually go?', ['Outside to a meeting spot', 'To the cafeteria for lunch', 'Home', 'Nowhere at all'], 0),
    ('Practising a fire drill helps keep everyone ___.', ['Confused', 'Safe and prepared', 'Unsafe', 'Late for class'], 1)]),
]),
day(128, [
L('Command Sentences: Telling Someone What to Do',
  'Kindergarten Language strand: a command sentence tells someone what to do, such as Sit down or Please close the door.',
  [('Give an example of a command sentence.', ['Sit down', 'Close the door']),
   ('What does a command sentence do?', ['tells someone what to do', 'gives an instruction']),
   ('How does a command sentence often end?', ['with a period', 'a period or exclamation mark'])],
  [('What is the purpose of a command sentence?', ['To ask a question', 'To tell someone what to do', 'To show excitement only', 'To name a person'], 1),
   ('Which sentence is a command?', ['Are you hungry?', 'Please sit down.', 'What a big dog!', 'The sky is blue.'], 1),
   ('Which sentence is NOT a command?', ['Close the door.', 'Wash your hands.', 'It is raining today.', 'Sit down.'], 2),
   ('Command sentences often begin with a(n) ___.', ['Action word', 'Question word', 'Exclamation only', 'Number'], 0),
   ('Which is a command a teacher might give?', ['Line up quietly.', 'Is it lunchtime?', 'What a fun day!', 'The sun is shining.'], 0)]),
M('Data: Real Graphs Using Real Objects',
  'Kindergarten Math strand: students sort real objects, such as shoes or leaves, into rows to make a real graph and compare the groups.',
  [('Name two kinds of real objects you could sort into a graph.', ['shoes', 'leaves', 'buttons']),
   ('In a real graph, how are objects arranged?', ['in rows or lines', 'lined up']),
   ('How can you tell which group has more in a real graph?', ['the longer row has more', 'compare the lengths'])],
  [('A real graph is made using ___.', ['Only drawings', 'Actual real objects', 'Numbers only', 'Nothing at all'], 1),
   ('In a real graph, objects are usually arranged in ___.', ['A pile', 'Rows or lines', 'A circle', 'A random scatter'], 1),
   ('How can we tell which row has more objects in a real graph?', ['Guess', 'Compare the length of the rows', 'Count the colours', 'Smell the objects'], 1),
   ('Which is a good example of objects to sort into a real graph?', ['Shoes by colour', 'The weather', 'A song', 'A story'], 0),
   ('Making a real graph helps us ___.', ['Compare groups of objects', 'Forget the objects', 'Hide the objects', 'Mix up the objects'], 0)]),
Sc('Extreme Weather: Storms and Lightning',
   'Kindergarten Science strand: extreme weather, such as thunderstorms with lightning and loud thunder, can happen quickly and requires staying safe indoors.',
   [('Name one type of extreme weather.', ['thunderstorm', 'lightning']),
    ('What should you do during a thunderstorm to stay safe?', ['stay indoors', 'go inside']),
    ('What comes after we see lightning in a storm?', ['thunder', 'the sound of thunder'])],
   [('Which is an example of extreme weather?', ['A gentle breeze', 'A thunderstorm', 'A sunny sky', 'A light cloud'], 1),
    ('What should people do to stay safe during a thunderstorm?', ['Stay outside', 'Stay indoors', 'Stand under a tree', 'Swim in a lake'], 1),
    ('What loud sound often follows a flash of lightning?', ['Thunder', 'Wind', 'Rain', 'Silence'], 0),
    ('Lightning is a flash of ___ during a storm.', ['Sound', 'Electricity', 'Water', 'Wind'], 1),
    ('Extreme weather can happen ___.', ['Never', 'Quickly and without much warning', 'Only in summer', 'Only at night'], 1)]),
SS('Fair Play: Sharing Toys and Taking Turns',
   'Kindergarten Social Studies strand: fair play means sharing toys, taking turns, and following the same rules so that everyone can enjoy playing together.',
   [('What does fair play mean?', ['sharing and taking turns', 'playing fairly']),
    ('Name one way to show fair play.', ['sharing toys', 'taking turns']),
    ('Why is fair play important when playing with friends?', ['everyone gets to enjoy playing', 'keeps play fun for everyone'])],
   [('What does fair play mean?', ['Keeping all the toys for yourself', 'Sharing and taking turns', 'Ignoring the rules', 'Never playing with others'], 1),
    ('Which is an example of fair play?', ['Taking turns on the swing', 'Grabbing all the toys', 'Refusing to share', 'Breaking the rules'], 0),
    ('Why is fair play important when playing games?', ['It keeps play fun and kind for everyone', 'It makes games boring', 'It is not important', 'Only one person should have fun'], 0),
    ('If two children want the same toy, fair play means they should ___.', ['Fight over it', 'Take turns using it', 'Hide it', 'Break it'], 1),
    ('Following the same rules for everyone is an example of ___.', ['Unfairness', 'Fairness', 'Cheating', 'Confusion'], 1)]),
]),
day(129, [
L('Rhyming Families: Grouping Words That Rhyme',
  'Kindergarten Language strand: students sort words into groups by their rhyme, gathering words like cat, hat, and bat into one rhyming family.',
  [('Name three words that rhyme with cat.', ['hat, bat, mat', 'hat and bat and mat']),
   ('How do we know two words rhyme?', ['they end with the same sound', 'same ending sound']),
   ('Sort hop and top. Do they rhyme?', ['yes', 'yes they do'])],
  [('Which group of words all rhyme together?', ['Cat, hat, bat', 'Cat, dog, sun', 'Cat, cup, cot', 'Cat, car, can'], 0),
   ('How can we tell if words belong in the same rhyming family?', ['They look the same colour', 'They end with the same sound', 'They start with the same letter', 'They have the same number of letters'], 1),
   ('Which word would join the family hop, top, mop?', ['Pop', 'Pig', 'Pen', 'Pan'], 0),
   ('Sorting words by rhyme helps us notice ___.', ['Sound patterns', 'Random colours', 'Story characters', 'Math facts'], 0),
   ('Which word does NOT rhyme with sun?', ['Fun', 'Run', 'Bun', 'Bug'], 3)]),
M('Number Bonds: Ways to Make 4',
  'Kindergarten Math strand: students find different pairs of numbers that combine to make 4, such as 1 and 3, or 2 and 2.',
  [('What two numbers make 4 with 1?', ['3', '1 and 3']),
   ('What two numbers make 4 with 2?', ['2', '2 and 2']),
   ('Show one way to make 4.', ['1 and 3', '0 and 4'])],
  [('1 + ? = 4', ['1', '2', '3', '4'], 2),
   ('Which pair makes 4?', ['1 and 1', '2 and 2', '3 and 3', '0 and 1'], 1),
   ('2 + ? = 4', ['0', '1', '2', '3'], 2),
   ('Which pair does NOT make 4?', ['1 and 3', '2 and 2', '0 and 4', '1 and 4'], 3),
   ('0 + ? = 4', ['3', '4', '5', '2'], 1)]),
Sc('Solar Energy: Power from the Sun',
   'Kindergarten Science strand: solar energy is power that comes from sunlight, which can be captured by solar panels to make electricity.',
   [('Where does solar energy come from?', ['the Sun', 'sunlight']),
    ('What tool can capture sunlight to make electricity?', ['a solar panel', 'solar panels']),
    ('Is solar energy a clean form of energy?', ['yes', 'yes it is clean'])],
   [('Where does solar energy come from?', ['The wind', 'The Sun', 'The ocean', 'Underground rocks'], 1),
    ('What can capture sunlight and turn it into electricity?', ['A solar panel', 'A fan', 'A candle', 'A blanket'], 0),
    ('Solar energy is considered a ___ source of power.', ['Dirty', 'Clean, renewable', 'Fake', 'Dangerous'], 1),
    ('Which of these uses solar energy?', ['A solar-powered calculator', 'A candle', 'A campfire', 'A gasoline car'], 0),
    ('Solar energy is powered by ___.', ['Moonlight', 'Sunlight', 'Rain', 'Snow'], 1)]),
SS('Comparing Toys: Then and Now',
   'Kindergarten Social Studies strand: toys have changed over time, from simple wooden toys long ago to the electronic toys and games many children play with now.',
   [('Name a toy children might have played with long ago.', ['a wooden toy', 'a doll']),
    ('Name a toy children often play with now.', ['a tablet game', 'an electronic toy']),
    ('How have toys changed over time?', ['they became more electronic', 'new materials and technology'])],
   [('What kind of toys did many children play with long ago?', ['Electronic toys', 'Simple wooden or cloth toys', 'Video games', 'Tablets'], 1),
    ('What kind of toys do many children play with today?', ['Only wooden blocks', 'Electronic toys and games', 'Nothing at all', 'Only rocks'], 1),
    ('How have toys changed from long ago to now?', ['They have not changed at all', 'They have become more electronic and modern', 'They have disappeared', 'They became simpler'], 1),
    ('Comparing old and new toys helps us understand ___.', ['That things can change over time', 'That toys never change', 'Nothing important', 'Only todays toys'], 0),
    ('Which is an example of an older, simple toy?', ['A wooden top', 'A tablet', 'A video game console', 'A smartphone'], 0)]),
]),
day(130, [
L('Language Review: Synonyms, Prefixes, and Story Comparison',
  'Kindergarten Language strand review: students revisit word families -ip and -op, synonyms, the prefix un-, comparing stories, and command sentences.',
  [('Give a word from the -ip or -op word family.', ['dip', 'hop', 'top']),
   ('Give a synonym for happy.', ['glad', 'joyful']),
   ('Give an example of a command sentence.', ['Sit down', 'Close the door'])],
  [('Which word belongs to the -ip family?', ['Cat', 'Zip', 'Bag', 'Sun'], 1),
   ('Which word means the same as happy?', ['Sad', 'Glad', 'Angry', 'Tired'], 1),
   ('What does adding un- to the word happy create?', ['Happier', 'Unhappy', 'Happily', 'Happiness'], 1),
   ('When we compare two stories, we look for ways they are ___.', ['Alike and different', 'Loud and quiet', 'Long and short only', 'Colourful'], 0),
   ('Which sentence is a command?', ['Are you hungry?', 'Please sit down.', 'What a big dog!', 'The sky is blue.'], 1)]),
M('Math Review: 3D Shapes, Fractions, and Number Bonds',
  'Kindergarten Math strand review: students revisit cones and pyramids, counting beyond 100, quarter-hour time, fractions of equal parts, and number bonds to 4.',
  [('Name something shaped like a cone.', ['an ice cream cone', 'a party hat']),
   ('What number comes right after 100?', ['101', 'one hundred one']),
   ('Show one way to make 4.', ['1 and 3', '0 and 4'])],
  [('Which real object is shaped like a cone?', ['A ball', 'An ice cream cone', 'A box', 'A can'], 1),
   ('What number comes right after 119?', ['118', '120', '121', '100'], 1),
   ('What do we call 15 minutes past the hour?', ['Half past', 'Quarter past', 'Quarter to', 'A full hour'], 1),
   ('If a shape is cut into two same-size pieces, the parts are ___.', ['Unequal', 'Equal', 'Missing', 'Too many'], 1),
   ('Which pair makes 4?', ['1 and 1', '2 and 2', '3 and 3', '0 and 1'], 1)]),
Sc('Science Review: Space, Animals, and Energy',
   'Kindergarten Science strand review: students revisit the solar system, stars, reptiles, amphibians, bats, underground animals, blood, extreme weather, and solar energy.',
   [('What is at the centre of our solar system?', ['the Sun', 'Sun']),
    ('What covers a reptiles skin?', ['scales', 'dry scales']),
    ('Where does solar energy come from?', ['the Sun', 'sunlight'])],
   [('What is at the centre of our solar system?', ['The Moon', 'The Sun', 'Earth', 'A star far away'], 1),
    ('Which of these is a reptile?', ['Frog', 'Snake', 'Fish', 'Bird'], 1),
    ('Bats are the only ___ that can truly fly.', ['Birds', 'Mammals', 'Reptiles', 'Fish'], 1),
    ('What body part pumps blood through our body?', ['The lungs', 'The heart', 'The brain', 'The stomach'], 1),
    ('What can capture sunlight and turn it into electricity?', ['A solar panel', 'A fan', 'A candle', 'A blanket'], 0)]),
SS('Social Studies Review: Heroes, Community, and Fair Play',
   'Kindergarten Social Studies strand review: students revisit Terry Fox, Canada Day, Indigenous peoples of Canada, the school principal, public transit, fire drills, and fair play.',
   [('What did Terry Fox do to raise money?', ['ran across Canada', 'ran a marathon']),
    ('What date is Canada Day celebrated on?', ['July 1st', 'July 1']),
    ('What does fair play mean?', ['sharing and taking turns', 'playing fairly'])],
   [('What is Terry Fox best known for?', ['Building bridges', 'Running across Canada to raise money for cancer research', 'Leading the government', 'Flying airplanes'], 1),
    ('On what date is Canada Day celebrated?', ['July 1st', 'December 25th', 'October 31st', 'January 1st'], 0),
    ('Who is the leader of a school?', ['The bus driver', 'The principal', 'A student', 'A visitor'], 1),
    ('Which of these is a form of public transit?', ['A bicycle', 'A subway train', 'A private car', 'A skateboard'], 1),
    ('What is the purpose of a fire drill?', ['To practise leaving the building safely', 'To have extra recess', 'To scare students', 'To skip class forever'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_121_130)
    append_worksheet_days(0, g0_121_130)
