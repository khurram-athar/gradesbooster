#!/usr/bin/env python3
"""Grade 1, Days 141-150 -- twelfth batch, extending Grade 1 past Day 140
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days131_140.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-140 (dumped
and checked against data/grade1.json before writing): vowel teams ow/ou,
prefixes over-/under-, suffix -ness, bold print and italics, personal
narrative, compare and contrast characters, word families -est/-end,
reading nonfiction, transition words for Language. Numbers to 400,
counting up subtraction, fourths of a group, time to the nearest minute,
money to two dollars, comparing three-digit numbers, converting metres
and centimetres, estimating sums, increasing/decreasing patterns for
Math. Kidneys, symbiosis, food webs, plant life cycle, extreme weather,
sharks, frogs and toads, rainforest, bridges and structures for Science.
School librarian, local radio and TV, Canadian peacekeepers, school
board, water systems, world landmarks, provincial legislature, fair
trade, school yearbook for Social Studies. Day 150 is a review day
across all four subjects, matching the end-of-batch pattern used in
every prior batch. No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/quiz/worksheet text --
contractions and possessives are avoided entirely, matching this
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


g1_141_150 = [
day(141, [
L('Vowel Teams: ow and ou',
  'Grade 1 Language strand: the vowel teams ow and ou can make the same sound, as in cow and out, or as in owl and cloud.',
  [('Give a word with the ow vowel team.', ['cow', 'owl']),
   ('Give a word with the ou vowel team.', ['out', 'cloud']),
   ('Do ow and ou sometimes make the same sound?', ['yes', 'yes they can'])],
  [('Which word has the ow vowel team making the same sound as in cow?', ['Cow', 'Snow', 'Grow', 'Row'], 0),
   ('Which word has the ou vowel team making the same sound as in out?', ['Out', 'Soup', 'Group', 'Tour'], 0),
   ('Which two letters can make the same sound in cow and cloud?', ['ow and ou', 'ee and ea', 'ai and ay', 'oi and oy'], 0),
   ('Which word does NOT belong with cow, how, and now?', ['Cow', 'Snow', 'How', 'Now'], 1),
   ('Vowel teams are two vowels that work together to make ___.', ['One sound', 'No sound', 'Two separate sounds always', 'A silent letter'], 0)]),
M('Numbers to 400: Beyond 300',
  'Grade 1 Math strand: students read, write, and count numbers beyond 300, up to 400.',
  [('What number comes right after 399?', ['400', 'four hundred']),
   ('What number comes right before 350?', ['349', 'three hundred forty nine']),
   ('Count by tens from 380 to 400.', ['380,390,400', '380 390 400'])],
  [('What number comes right after 399?', ['398', '399', '400', '401'], 2),
   ('Which number is between 320 and 340?', ['310', '330', '350', '360'], 1),
   ('What number comes right before 400?', ['398', '399', '400', '401'], 1),
   ('Which of these numbers is the largest?', ['299', '349', '399', '298'], 2),
   ('Counting beyond 300 helps us understand numbers up to ___.', ['400', '40', '4', '4000'], 0)]),
Sc('Our Kidneys: Filtering Our Blood',
   'Grade 1 Science strand: our kidneys are two bean-shaped organs that filter waste out of our blood and help make urine.',
   [('What do our kidneys do?', ['filter waste from our blood', 'clean our blood']),
    ('What shape are our kidneys?', ['bean shaped', 'like a bean']),
    ('How many kidneys does a person usually have?', ['2', 'two'])],
   [('What is the main job of our kidneys?', ['Filtering waste out of our blood', 'Pumping blood around the body', 'Helping us breathe', 'Helping us see'], 0),
    ('What shape are our kidneys?', ['Bean shaped', 'Square shaped', 'Round like a ball', 'Long and flat'], 0),
    ('How many kidneys does a person usually have?', ['1', '2', '3', '4'], 1),
    ('What does our body make after the kidneys filter waste?', ['Urine', 'Bones', 'Hair', 'Skin'], 0),
    ('Our kidneys are an important part of keeping our blood ___.', ['Clean', 'Cold', 'Colourful', 'Loud'], 0)]),
SS('Our School Librarian: Helping Us Find Books',
   'Grade 1 Social Studies strand: the school librarian helps students find, borrow, and take care of books in the school library.',
   [('What does a school librarian help students do?', ['find and borrow books', 'find books they will like']),
    ('Where does a school librarian usually work?', ['the library', 'the school library']),
    ('Why is it important to take care of library books?', ['so other students can use them too', 'keeps books in good shape'])],
   [('What is the main job of a school librarian?', ['Helping students find and borrow books', 'Teaching math class', 'Driving the school bus', 'Cooking school lunches'], 0),
    ('Where does a school librarian usually work?', ['In the school library', 'On the playground', 'In the gym', 'In the parking lot'], 0),
    ('Why should students take good care of library books?', ['So other students can enjoy them too', 'Books do not need to be cared for', 'It does not matter at all', 'Books are meant to be thrown away'], 0),
    ('Which of these might a librarian help you do?', ['Find a book about a topic you like', 'Fix a bicycle', 'Bake a cake', 'Paint a fence'], 0),
    ('A well organized library helps students ___.', ['Find books more easily', 'Get lost more often', 'Avoid reading', 'Feel confused'], 0)]),
]),
day(142, [
L('Prefixes: over- and under-',
  'Grade 1 Language strand: the prefixes over- and under- change a words meaning to show too much or not enough, as in overfilled and underfed.',
  [('What does the prefix over- usually mean?', ['too much', 'more than enough']),
   ('What does the prefix under- usually mean?', ['not enough', 'too little']),
   ('Give an example of a word with over- or under-.', ['overfilled', 'underfed'])],
  [('What does the prefix over- usually add to a word?', ['The meaning of too much', 'The meaning of colour', 'The meaning of a number', 'The meaning of sound'], 0),
   ('What does the prefix under- usually add to a word?', ['The meaning of not enough', 'The meaning of too much', 'A shape', 'A feeling only'], 0),
   ('Which word means to cook something for too long?', ['Undercook', 'Overcook', 'Recook', 'Precook'], 1),
   ('Which word means something did not get enough food?', ['Overfed', 'Underfed', 'Refed', 'Prefed'], 1),
   ('Prefixes are added to the ___ of a word to change its meaning.', ['End', 'Beginning', 'Middle', 'Nowhere'], 1)]),
M('Subtraction: Counting Up Strategy',
  'Grade 1 Math strand: students learn the counting up strategy for subtraction, counting from the smaller number up to the larger number to find the difference.',
  [('What is the counting up strategy used for?', ['subtraction', 'finding the difference between numbers']),
   ('If you count up from 7 to 10, how many steps is that?', ['3', 'three']),
   ('Why might counting up be a helpful subtraction strategy?', ['it can be faster for numbers close together', 'easier for close numbers'])],
  [('What does the counting up strategy help us do?', ['Solve subtraction problems', 'Solve addition only', 'Tell time', 'Measure length'], 0),
   ('If you count up from 8 to 12, how many steps is that?', ['2', '3', '4', '5'], 2),
   ('Counting up is a helpful strategy when the two numbers are ___.', ['Close together', 'Very far apart', 'Always equal', 'Both zero'], 0),
   ('What is 15 minus 12 using the counting up strategy?', ['1', '2', '3', '4'], 2),
   ('Counting up from the smaller number to the larger number helps find the ___.', ['Difference', 'Sum', 'Product', 'Total groups'], 0)]),
Sc('Symbiosis: Living Things Helping Each Other',
   'Grade 1 Science strand: symbiosis happens when two different living things live closely together and help each other survive.',
   [('What is symbiosis?', ['when two living things help each other', 'living things working together']),
    ('Give an example of symbiosis.', ['bees and flowers', 'clownfish and sea anemones']),
    ('Why is symbiosis helpful?', ['both living things benefit', 'they help each other survive'])],
   [('What is symbiosis?', ['When two different living things help each other', 'When one animal eats another', 'A type of weather', 'A kind of rock'], 0),
    ('Which is an example of symbiosis?', ['A bee collecting nectar and pollinating a flower', 'A rock sitting in a field', 'A cloud floating in the sky', 'A river flowing downhill'], 0),
    ('Why is symbiosis helpful for living things?', ['Both living things can benefit from the relationship', 'It only helps one side and hurts the other always', 'It has no effect on either living thing', 'It only happens between plants'], 0),
    ('Clownfish and sea anemones are often used as an example of ___.', ['Symbiosis', 'A food chain only', 'A rock cycle', 'A weather pattern'], 0),
    ('Symbiosis shows us that living things in nature are often ___.', ['Connected and helpful to each other', 'Completely separate from each other', 'Never affected by other living things', 'Unable to survive together'], 0)]),
SS('Our Local Radio and TV: Sharing News and Weather',
   'Grade 1 Social Studies strand: local radio and television stations share news, weather, and important information with people in our community.',
   [('What do local radio and TV stations share?', ['news and weather', 'important community information']),
    ('Name one thing you might learn from watching the local news.', ['the weather', 'community events']),
    ('Why is local news helpful?', ['keeps people informed', 'tells us what is happening nearby'])],
   [('What is one thing local radio and TV stations share with the community?', ['News and weather updates', 'Only cartoons', 'Nothing useful', 'Only music from other countries'], 0),
    ('Why might people watch or listen to local news?', ['To stay informed about their community', 'It has no value at all', 'To avoid learning anything', 'Only for entertainment with no facts'], 0),
    ('Which of these might be shared on the local news?', ['Todays weather forecast', 'A private family photo album', 'A made-up fairy tale', 'A recipe with no real purpose'], 0),
    ('Local radio and TV help connect people in a community by sharing ___.', ['Important information', 'Nothing at all', 'Only advertisements', 'Only silence'], 0),
    ('Besides TV and radio, where else might people get local news today?', ['Online news websites', 'Nowhere else', 'Only word of mouth', 'It is impossible to find local news'], 0)]),
]),
day(143, [
L('Suffixes: Adding -ness to Make Nouns',
  'Grade 1 Language strand: adding the suffix -ness to an adjective creates a noun that names a quality, such as changing happy into happiness.',
  [('What does happiness mean?', ['the quality of being happy', 'being happy']),
   ('What does the suffix -ness usually do to a word?', ['turns it into a noun', 'names a quality']),
   ('Give an example of a word with the suffix -ness.', ['happiness', 'kindness'])],
  [('What does the word happiness mean?', ['The quality of being happy', 'Being sad', 'A type of food', 'A colour'], 0),
   ('What does the suffix -ness usually do to an adjective?', ['Turns it into a noun naming a quality', 'Turns it into a verb', 'Makes it a number', 'Makes it a question'], 0),
   ('Which word is formed by adding -ness to kind?', ['Kindful', 'Kindness', 'Kindly', 'Kinded'], 1),
   ('Adding -ness to the word sad makes the word ___.', ['Sadness', 'Sadful', 'Sadly', 'Sadable'], 0),
   ('A suffix like -ness is added to the ___ of a word.', ['Beginning', 'End', 'Middle', 'Nowhere'], 1)]),
M('Fractions: Fourths of a Group',
  'Grade 1 Math strand: students learn to find a fourth of a group of objects by sharing the group equally into four smaller groups.',
  [('What does finding a fourth of a group mean?', ['sharing a group into 4 equal parts', 'splitting into four equal groups']),
   ('If you split 8 apples into fourths, how many apples are in each group?', ['2', 'two']),
   ('Are the four groups the same size when you make fourths?', ['yes', 'yes they are equal'])],
  [('What does it mean to find a fourth of a group of objects?', ['Sharing the group into 4 equal parts', 'Sharing the group into 2 equal parts', 'Doubling the group', 'Ignoring the group'], 0),
   ('If 12 cookies are split into fourths, how many cookies are in each group?', ['2', '3', '4', '6'], 1),
   ('If 16 marbles are split into fourths, how many marbles are in each group?', ['2', '4', '6', '8'], 1),
   ('For groups to be called fourths, each group must be ___.', ['A different size', 'The same size', 'Missing objects', 'Uncounted'], 1),
   ('Fourths divide a group into ___ equal parts.', ['2', '3', '4', '5'], 2)]),
Sc('Food Webs: Connecting Many Food Chains',
   'Grade 1 Science strand: a food web shows how many different food chains connect together, showing all the ways animals in a habitat eat and are eaten.',
   [('What is a food web?', ['many food chains connected together', 'a way many animals connect through eating']),
    ('How is a food web different from a single food chain?', ['it shows many connections, not just one', 'it connects many chains']),
    ('Why are food webs important to understand?', ['show how living things depend on each other', 'help us see how nature is connected'])],
   [('What is a food web?', ['Many food chains connected together', 'A single line of animals eating one thing', 'A spider building a web', 'A map of a forest'], 0),
    ('How does a food web differ from a single food chain?', ['A food web shows many connected feeding relationships', 'They are exactly the same thing', 'A food web has no animals in it', 'A food chain shows more connections than a web'], 0),
    ('Why is it useful for scientists to study food webs?', ['To understand how living things depend on each other', 'Food webs have no real purpose', 'To avoid learning about animals', 'To count only plants'], 0),
    ('If one animal disappears from a food web, what might happen?', ['It can affect other living things connected to it', 'Nothing changes at all for anyone', 'The whole web disappears instantly', 'Only plants are affected'], 0),
    ('A food web helps us see that living things in a habitat are ___.', ['Connected to each other', 'Completely separate', 'Unrelated to their environment', 'Never affected by other animals'], 0)]),
SS('Canadian Peacekeepers: Helping Around the World',
   'Grade 1 Social Studies strand: Canadian peacekeepers travel to other countries to help keep peace and support people during difficult times.',
   [('What do Canadian peacekeepers do?', ['help keep peace in other countries', 'support people during hard times']),
    ('Where do peacekeepers often travel to help?', ['other countries', 'places facing conflict']),
    ('Why is peacekeeping an important job?', ['helps protect people and keep peace', 'supports countries in need'])],
   [('What is the main job of a Canadian peacekeeper?', ['Helping keep peace in other countries', 'Teaching school in Canada', 'Driving a school bus', 'Cooking meals at home'], 0),
    ('Where do peacekeepers often travel to do their work?', ['To other countries facing conflict or hardship', 'Only within their own backyard', 'Nowhere, they stay home always', 'Only to grocery stores'], 0),
    ('Why is peacekeeping considered an important job?', ['It helps protect people and support peace', 'It has no real purpose', 'It only helps one single person', 'It causes more conflict on purpose'], 0),
    ('Which best describes what peacekeepers try to achieve?', ['Helping communities stay safe and peaceful', 'Starting new conflicts', 'Ignoring people in need', 'Avoiding all countries in need'], 0),
    ('Canada sending peacekeepers to help other countries shows that Canada cares about ___.', ['Global peace and cooperation', 'Nothing beyond its own borders', 'Only its own citizens', 'Causing problems elsewhere'], 0)]),
]),
day(144, [
L('Text Features: Bold Print and Italics',
  'Grade 1 Language strand: bold print and italics are special kinds of text that help important words or ideas stand out on a page.',
  [('What does bold print look like?', ['darker and thicker letters', 'thick dark letters']),
   ('What does italics look like?', ['slanted letters', 'letters that lean']),
   ('Why do authors use bold print or italics?', ['to make words stand out', 'show importance']),
   ],
  [('What does bold print usually look like?', ['Darker, thicker letters', 'Slanted letters', 'Tiny letters', 'Underlined letters only'], 0),
   ('What does italic text usually look like?', ['Slanted letters', 'Very dark letters', 'Extra large letters', 'Coloured letters only'], 0),
   ('Why might an author use bold print for a word?', ['To make it stand out as important', 'To hide it from the reader', 'To make the page shorter', 'For no reason at all'], 0),
   ('Which of these is an example of using a text feature to highlight a word?', ['Writing a word in bold letters', 'Writing every word the same way', 'Erasing a word completely', 'Writing in invisible ink'], 0),
   ('Bold print and italics are examples of ___.', ['Text features', 'Punctuation marks', 'Vowel teams', 'Story characters'], 0)]),
M('Telling Time to the Nearest Minute',
  'Grade 1 Math strand: students practise reading a clock to tell time to the nearest minute, counting each small mark around the clock as one minute.',
  [('How many minutes are in one hour?', ['60', 'sixty']),
   ('If the minute hand points to the 1, how many minutes past the hour is it?', ['5', 'five']),
   ('How do we count the small marks around a clock?', ['each one is a minute', 'count by ones for minutes'])],
  [('How many minutes are in one full hour?', ['30', '45', '60', '100'], 2),
   ('If the minute hand points to the 3, how many minutes past the hour is it?', ['3', '10', '15', '30'], 2),
   ('If the minute hand points to the 6, how many minutes past the hour is it?', ['15', '30', '45', '50'], 1),
   ('Reading a clock to the nearest minute means counting each small mark as ___.', ['One minute', 'One hour', 'Ten minutes', 'One second'], 0),
   ('If a clock shows 4:07, how many minutes past 4 oclock is it?', ['5', '6', '7', '8'], 2)]),
Sc('The Life Cycle of a Plant: Seed to Flower',
   'Grade 1 Science strand: a plants life cycle begins as a seed, which grows roots and a stem, sprouts leaves, and eventually grows a flower.',
   [('What is the first stage of a plants life cycle?', ['seed', 'a seed']),
    ('What grows first from a seed underground?', ['roots', 'a root']),
    ('What does a plant often grow at the end of its life cycle?', ['a flower', 'flowers'])],
   [('What is the first stage of a plants life cycle?', ['Seed', 'Flower', 'Root', 'Leaf'], 0),
    ('What usually grows first from a planted seed, underground?', ['Roots', 'Flowers', 'Fruit', 'Bark'], 0),
    ('What often grows at the end of a plants life cycle?', ['A flower', 'A brand new seed packet', 'Nothing at all', 'A different kind of plant'], 0),
    ('Which of these is part of a plants life cycle in order?', ['Seed, roots, stem, leaves, flower', 'Flower, seed, roots, stem', 'Leaves, seed, flower, roots', 'Stem, flower, seed, roots'], 0),
    ('After a flower is pollinated, what can it eventually produce?', ['New seeds', 'Rocks', 'Water', 'Sunlight'], 0)]),
SS('Our School Board: Supporting Many Schools',
   'Grade 1 Social Studies strand: a school board oversees many schools in an area, helping make decisions about education for a whole region.',
   [('What does a school board do?', ['oversees many schools', 'makes decisions about education']),
    ('Does a school board oversee just one school or many schools?', ['many schools', 'many schools in an area']),
    ('Why is a school board important?', ['helps schools run well', 'supports education for many students'])],
   [('What does a school board oversee?', ['Many schools in an area', 'Just one single classroom', 'Only sports teams', 'Only school buses'], 0),
    ('Does a school board oversee just one school or many schools?', ['Many schools', 'Just one school', 'No schools at all', 'Only private homes'], 0),
    ('Why is a school board an important part of education?', ['It helps make decisions that support many schools', 'It has no role in education', 'It only decides lunch menus', 'It replaces teachers completely'], 0),
    ('Which of these might a school board help decide?', ['How schools in the area are run', 'What every student eats for breakfast at home', 'The colour of every students shoes', 'Personal weekend plans for families'], 0),
    ('A school board works to support ___ across a region.', ['Education', 'Only sports', 'Only art class', 'Nothing important'], 0)]),
]),
day(145, [
L('Personal Narrative: Writing About a Real Event',
  'Grade 1 Language strand: a personal narrative is a true story about something that happened to the writer, told in their own words.',
  [('What is a personal narrative?', ['a true story about the writer', 'a real event the writer experienced']),
   ('Is a personal narrative made up or true?', ['true', 'it is a real event']),
   ('Give an example of a topic for a personal narrative.', ['a trip to the park', 'my birthday'])],
  [('What is a personal narrative?', ['A true story about something that happened to the writer', 'A made-up fairy tale', 'A list of facts with no story', 'A poem with no meaning'], 0),
   ('Is a personal narrative fiction or true?', ['True', 'Completely made up', 'Neither true nor false', 'A type of poem only'], 0),
   ('Which of these is a good topic for a personal narrative?', ['A time you visited a special place', 'A story about a talking dragon', 'A list of math facts', 'A recipe for cookies'], 0),
   ('A personal narrative is usually written from whose point of view?', ['The writers own point of view', 'A made-up characters point of view only', 'No one at all', 'A random strangers point of view'], 0),
   ('Writing about a real event in your own words is an example of a ___.', ['Personal narrative', 'Nonfiction textbook', 'Dictionary entry', 'Recipe'], 0)]),
M('Money: Making Amounts Up to Two Dollars',
  'Grade 1 Math strand: students combine coins and bills to make amounts of money up to two dollars.',
  [('Name coins or bills that could make one dollar.', ['a loonie', 'four quarters']),
   ('How could you make two dollars using two coins?', ['two loonies', 'two dollar coins']),
   ('Why is it useful to practise making different money amounts?', ['helps us understand money better', 'useful for buying things'])],
  [('Which combination makes exactly one dollar?', ['Four quarters', 'Two dimes', 'One nickel', 'Three pennies'], 0),
   ('Which combination makes exactly two dollars?', ['Two loonies', 'One dime', 'One nickel', 'One penny'], 0),
   ('How many quarters are needed to make one dollar?', ['2', '3', '4', '5'], 2),
   ('If you have one loonie and one quarter, how much money do you have?', ['1 dollar and 10 cents', '1 dollar and 25 cents', '2 dollars', '25 cents'], 1),
   ('Practising with coins and bills helps us understand ___.', ['The value of money', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('Extreme Weather: Storms and Lightning',
   'Grade 1 Science strand: extreme weather like thunderstorms brings strong winds, heavy rain, and lightning, and it is important to stay safe indoors when it happens.',
   [('What is extreme weather?', ['very strong or unusual weather', 'weather like thunderstorms']),
    ('What does a thunderstorm often bring?', ['strong winds and lightning', 'heavy rain and lightning']),
    ('Where should you go during a thunderstorm to stay safe?', ['indoors', 'inside a building'])],
   [('What is extreme weather?', ['Very strong or unusual weather', 'A calm sunny day', 'A light breeze', 'A quiet cloudy day'], 0),
    ('What does a thunderstorm often bring?', ['Strong winds, heavy rain, and lightning', 'Only gentle sunshine', 'Only snow', 'Nothing unusual at all'], 0),
    ('Where is the safest place to be during a thunderstorm?', ['Indoors, away from windows', 'Standing under a tall tree outside', 'Swimming in a lake', 'On top of a hill'], 0),
    ('Why is lightning dangerous?', ['It carries a powerful and sudden electric charge', 'It is completely harmless', 'It only happens indoors', 'It never happens near people'], 0),
    ('Learning about extreme weather helps us know how to stay ___.', ['Safe', 'Careless', 'Unaware', 'Bored'], 0)]),
SS('Water Systems: How Clean Water Reaches Our Homes',
   'Grade 1 Social Studies strand: water systems clean and carry water through pipes from lakes, rivers, or wells to our homes so we have safe water to use.',
   [('Where does the water in our homes often come from?', ['lakes, rivers, or wells', 'a water source like a lake']),
    ('What happens to water before it reaches our homes?', ['it gets cleaned', 'treated to make it safe']),
    ('How does clean water travel to our homes?', ['through pipes', 'underground pipes'])],
   [('Where does the water used in our homes often come from originally?', ['Lakes, rivers, or wells', 'Only from bottled water trucks', 'Nowhere, it appears instantly', 'Only from the clouds directly'], 0),
    ('What usually happens to water before it reaches our homes?', ['It is cleaned and treated', 'It is left completely untreated', 'It disappears', 'It is frozen solid first'], 0),
    ('How does clean water usually travel to our homes?', ['Through underground pipes', 'By airplane delivery', 'By hand carried buckets only', 'It does not travel at all'], 0),
    ('Why is a water system important for a community?', ['It provides safe water for people to use', 'It has no importance', 'It only helps one house', 'It wastes water on purpose'], 0),
    ('Water systems help make sure the water we use is ___.', ['Clean and safe', 'Always dirty', 'Never available', 'Only for animals'], 0)]),
]),
day(146, [
L('Compare and Contrast: Two Characters in a Story',
  'Grade 1 Language strand: comparing and contrasting two characters means looking at how they are alike and how they are different.',
  [('What does it mean to compare two characters?', ['find how they are alike', 'see their similarities']),
   ('What does it mean to contrast two characters?', ['find how they are different', 'see their differences']),
   ('Why is comparing and contrasting characters useful?', ['helps us understand a story better', 'shows us what makes each character special'])],
  [('What does it mean to compare two characters?', ['Find how they are alike', 'Find how they are different', 'Ignore both characters', 'Erase one character'], 0),
   ('What does it mean to contrast two characters?', ['Find how they are different', 'Find how they are alike', 'Draw a picture of them', 'Skip reading about them'], 0),
   ('Why might a reader compare and contrast two characters in a story?', ['To understand the story and characters better', 'It has no purpose', 'To confuse the reader', 'To remove the characters from the story'], 0),
   ('If two characters both like to help others, that is an example of ___.', ['A similarity', 'A difference', 'A setting', 'A title'], 0),
   ('If one character is brave and another is shy, that is an example of ___.', ['A difference', 'A similarity', 'A setting', 'A summary'], 0)]),
M('Comparing Three-Digit Numbers',
  'Grade 1 Math strand: students compare two three-digit numbers to decide which is greater or less using place value.',
  [('Which is greater, 245 or 254?', ['254']),
   ('Which is smaller, 187 or 178?', ['178']),
   ('What place value do we check first when comparing three-digit numbers?', ['the hundreds place', 'hundreds digit'])],
  [('Which number is greater, 312 or 321?', ['312', '321', 'They are equal', 'Neither has a value'], 1),
   ('Which number is smaller, 456 or 465?', ['456', '465', 'They are equal', 'Cannot be compared'], 0),
   ('When comparing 3-digit numbers, which place do we check first?', ['The hundreds place', 'The ones place', 'The tens place only', 'The name of the number'], 0),
   ('Which symbol means greater than?', ['>', '<', '=', '+'], 0),
   ('If two numbers have the same hundreds digit, what do we check next?', ['The tens digit', 'The hundreds digit again', 'Nothing else', 'The colour of the numbers'], 0)]),
Sc('Sharks: Ocean Predators',
   'Grade 1 Science strand: sharks are ocean fish with rows of sharp teeth, and most sharks are important predators that help keep ocean ecosystems healthy.',
   [('What kind of animal is a shark?', ['a fish', 'an ocean fish']),
    ('What do sharks have rows of in their mouths?', ['sharp teeth', 'teeth']),
    ('Why are sharks important in the ocean?', ['they help keep ecosystems healthy', 'they are important predators'])],
   [('What kind of animal is a shark?', ['A fish', 'A mammal', 'A reptile', 'A bird'], 0),
    ('What do sharks have many rows of in their mouths?', ['Sharp teeth', 'Feathers', 'Fur', 'Scales only, no teeth'], 0),
    ('Why are sharks important to ocean ecosystems?', ['They help keep the ocean food chain balanced as predators', 'They have no role in the ocean', 'They only eat plants', 'They live only on land'], 0),
    ('How do sharks usually breathe underwater?', ['Using gills', 'Using lungs like a human', 'They do not need to breathe', 'Using their tail'], 0),
    ('Most sharks play the role of a ___ in the ocean food chain.', ['Predator', 'Producer only', 'Decomposer only', 'Non-living object'], 0)]),
SS('World Landmarks: Famous Places Around the World',
   'Grade 1 Social Studies strand: world landmarks are famous and special places found in different countries that many people like to visit and learn about.',
   [('What is a world landmark?', ['a famous special place', 'a well known place in the world']),
    ('Name a world landmark.', ['a pyramid', 'a famous tower']),
    ('Why do people visit world landmarks?', ['to see something special', 'to learn about the place'])],
   [('What is a world landmark?', ['A famous and special place people like to visit', 'A type of food', 'A kind of animal', 'A weather pattern'], 0),
    ('Which of these is an example of a world landmark?', ['A famous ancient pyramid', 'A regular kitchen chair', 'A plain sidewalk', 'A common street sign'], 0),
    ('Why might people travel to see a world landmark?', ['To see something special and learn about it', 'Landmarks have no interest to anyone', 'To avoid learning anything new', 'Landmarks cannot be visited'], 0),
    ('Learning about landmarks in other countries helps us understand ___.', ['Different places and cultures around the world', 'Nothing outside our own street', 'Only our own country', 'Only our own school'], 0),
    ('Which best describes why landmarks are considered special?', ['They represent something important about a place or its history', 'They are chosen completely at random', 'They have no history at all', 'They are the same everywhere'], 0)]),
]),
day(147, [
L('Word Families: -est and -end',
  'Grade 1 Language strand: the -est word family and the -end word family share ending sounds, as in best, nest, and rest, or bend, send, and spend.',
  [('Name a word that rhymes with best.', ['nest', 'rest']),
   ('Name a word that rhymes with bend.', ['send', 'spend']),
   ('What ending sound do best and nest share?', ['est', 'the est sound'])],
  [('Which word belongs to the -est family?', ['Cat', 'Nest', 'Sun', 'Dog'], 1),
   ('Which word belongs to the -end family?', ['Send', 'Sit', 'Sat', 'Six'], 0),
   ('Which word rhymes with rest?', ['Best', 'Run', 'Cup', 'Pen'], 0),
   ('Which word rhymes with spend?', ['Send', 'Sun', 'Sit', 'Sap'], 0),
   ('Recognizing word families helps us read new words that share the same ___.', ['Ending sound', 'Meaning', 'Colour', 'Number of letters'], 0)]),
M('Converting Between Metres and Centimetres',
  'Grade 1 Math strand: students learn that one metre is equal to 100 centimetres, and practise converting between the two units.',
  [('How many centimetres are in one metre?', ['100', 'one hundred']),
   ('If something is 2 metres long, how many centimetres is that?', ['200', 'two hundred']),
   ('Why do we sometimes use centimetres and sometimes metres?', ['centimetres for small things, metres for longer things', 'depends on the size'])],
  [('How many centimetres are in one metre?', ['10', '50', '100', '1000'], 2),
   ('If a rope is 2 metres long, how many centimetres is that?', ['20', '100', '200', '2000'], 2),
   ('Which unit would we usually use to measure the length of a pencil?', ['Centimetres', 'Metres', 'Kilometres', 'Litres'], 0),
   ('Which unit would we usually use to measure the length of a hallway?', ['Centimetres', 'Metres', 'Millilitres', 'Grams'], 1),
   ('Knowing that 100 centimetres equal 1 metre helps us ___ between units.', ['Convert', 'Confuse', 'Ignore', 'Ban'], 0)]),
Sc('Frogs and Toads: Comparing Two Amphibians',
   'Grade 1 Science strand: frogs and toads are both amphibians, but frogs usually have smooth, wet skin while toads usually have bumpy, dry skin.',
   [('What kind of animal are frogs and toads?', ['amphibians', 'both amphibians']),
    ('What kind of skin do frogs usually have?', ['smooth and wet', 'smooth skin']),
    ('What kind of skin do toads usually have?', ['bumpy and dry', 'bumpy skin'])],
   [('What kind of animals are both frogs and toads?', ['Amphibians', 'Reptiles', 'Mammals', 'Birds'], 0),
    ('What kind of skin do frogs usually have?', ['Smooth and wet', 'Bumpy and dry', 'Covered in fur', 'Covered in feathers'], 0),
    ('What kind of skin do toads usually have?', ['Bumpy and dry', 'Smooth and wet', 'Covered in scales like a fish', 'Covered in fur'], 0),
    ('Which is a similarity between frogs and toads?', ['They are both amphibians', 'They both have fur', 'They both fly', 'They both live only in trees'], 0),
    ('Comparing frogs and toads helps us see that similar animals can still have ___.', ['Some differences', 'No differences at all', 'The exact same features', 'No similarities at all'], 0)]),
SS('Our Provincial Legislature: Where Laws Are Made',
   'Grade 1 Social Studies strand: the provincial legislature is a building where elected leaders meet to discuss and create laws for the province.',
   [('What is a provincial legislature?', ['a place where laws are made', 'where elected leaders meet']),
    ('Who works at a provincial legislature?', ['elected leaders', 'the premier and other elected members']),
    ('Why is the legislature important?', ['it is where important decisions are made', 'laws for the province are created there'])],
   [('What happens at a provincial legislature?', ['Elected leaders discuss and create laws', 'Students take a math test', 'Food is sold to the public', 'Movies are shown to visitors'], 0),
    ('Who works at a provincial legislature?', ['Elected leaders, including the premier', 'Only firefighters', 'Only doctors', 'Only bus drivers'], 0),
    ('Why is a provincial legislature an important building?', ['Important laws and decisions are made there', 'It has no real purpose', 'It is only used for sports games', 'It is closed at all times'], 0),
    ('Which of these might happen inside a provincial legislature?', ['A debate about a new provincial law', 'A birthday party for one family', 'A private vacation', 'Nothing important at all'], 0),
    ('A provincial legislature helps a province by creating ___.', ['Laws and important decisions', 'Only weather forecasts', 'Only sports schedules', 'Nothing useful'], 0)]),
]),
day(148, [
L('Reading Nonfiction for Information',
  'Grade 1 Language strand: reading nonfiction helps us learn true facts and information about real topics, like animals, places, or how things work.',
  [('What kind of information do we learn from nonfiction?', ['true facts', 'real information']),
   ('Give an example of a nonfiction topic.', ['animals', 'how things work']),
   ('How is nonfiction different from fiction?', ['nonfiction is true, fiction is made up', 'nonfiction is real'])],
  [('What kind of information do we learn from a nonfiction book?', ['True facts about real topics', 'Made-up stories about dragons', 'Nothing real at all', 'Only pictures with no facts'], 0),
   ('Which of these is a nonfiction topic?', ['How volcanoes work', 'A talking teddy bear', 'A magical flying carpet', 'A dragon who grants wishes'], 0),
   ('How is nonfiction different from fiction?', ['Nonfiction is true, fiction is made up', 'They are exactly the same', 'Fiction is always true', 'Nonfiction has no facts at all'], 0),
   ('Why might someone read a nonfiction book about animals?', ['To learn true facts about animals', 'To read a made-up story', 'To avoid learning anything', 'Nonfiction books have no purpose'], 0),
   ('Reading nonfiction helps build our ___ about the real world.', ['Knowledge', 'Imagination only', 'Confusion', 'Silence'], 0)]),
M('Estimating Sums: About How Many Altogether',
  'Grade 1 Math strand: students make a reasonable guess, or estimate, about how many objects there will be altogether before adding them exactly.',
  [('What does it mean to estimate a sum?', ['make a careful guess before adding', 'guess the total before checking']),
   ('Why might we estimate before adding exactly?', ['it helps us check if our answer makes sense', 'gives us a quick idea of the total']),
   ('If you have about 10 apples and about 10 more, about how many altogether?', ['about 20', 'around 20'])],
  [('What does it mean to estimate a sum?', ['Make a careful guess about the total before adding exactly', 'Know the exact answer with no guessing', 'Ignore the numbers completely', 'Draw a picture instead of adding'], 0),
   ('Why is estimating a sum before adding exactly useful?', ['It helps us check if our exact answer makes sense', 'It replaces the need to ever add exactly', 'It has no real purpose', 'It only works with subtraction'], 0),
   ('About how many are 19 and 21 altogether?', ['About 20', 'About 40', 'About 4', 'About 100'], 1),
   ('A good estimate is a guess that is ___.', ['Reasonable and thoughtful', 'Completely random', 'Always exactly right', 'Impossible to make'], 0),
   ('Estimating sums helps students practise thinking about ___.', ['Numbers and totals', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('The Rainforest: A Warm Wet Habitat',
   'Grade 1 Science strand: a rainforest is a warm, wet habitat that gets a lot of rain and is home to many different kinds of plants and animals.',
   [('What kind of weather does a rainforest have?', ['warm and wet', 'lots of rain']),
    ('Why do so many animals live in the rainforest?', ['it has lots of food and shelter', 'the warm wet climate supports many living things']),
    ('Name an animal that might live in a rainforest.', ['a monkey', 'a parrot'])],
   [('What kind of climate does a rainforest have?', ['Warm and wet', 'Cold and dry', 'Hot and dry like a desert', 'Frozen year round'], 0),
    ('Why is the rainforest home to so many different living things?', ['Its warm wet climate supports lots of plants and animals', 'It has almost no plants or animals', 'It is too cold for most living things', 'It never rains there'], 0),
    ('Which of these animals might you find living in a rainforest?', ['A parrot', 'A polar bear', 'A camel', 'A penguin'], 0),
    ('What is a rainforest known for receiving a lot of?', ['Rain', 'Snow', 'Sand', 'Ice'], 0),
    ('Rainforests are considered important because they are home to a huge variety of ___.', ['Plants and animals', 'Rocks only', 'Ice and snow', 'Buildings'], 0)]),
SS('Fair Trade: Buying Goods That Help Others',
   'Grade 1 Social Studies strand: fair trade means buying goods, like chocolate or coffee, in a way that makes sure the workers who made them are paid fairly.',
   [('What does fair trade mean?', ['buying goods in a way that pays workers fairly', 'making sure workers are treated fairly']),
    ('Name a product that might have a fair trade label.', ['chocolate', 'coffee']),
    ('Why is fair trade important?', ['it helps workers get paid fairly', 'supports fair treatment of workers'])],
   [('What does fair trade mean?', ['Buying goods in a way that pays workers fairly', 'Buying the cheapest goods with no other thought', 'A type of holiday', 'A type of weather'], 0),
    ('Which of these products might carry a fair trade label?', ['Chocolate', 'A toy car with no label', 'A rock', 'A cloud'], 0),
    ('Why do some shoppers choose fair trade products?', ['To help make sure workers are paid fairly', 'It has no benefit to anyone', 'To make products more expensive for no reason', 'To avoid helping any workers'], 0),
    ('Fair trade helps protect the rights of ___.', ['Workers who grow or make products', 'No one at all', 'Only large companies', 'Only shoppers'], 0),
    ('Learning about fair trade helps us understand how our choices can ___.', ['Affect people around the world', 'Have no effect on anyone', 'Only affect our own family', 'Change nothing at all'], 0)]),
]),
day(149, [
L('Transition Words: First, Then, Finally',
  'Grade 1 Language strand: transition words like first, then, and finally help readers understand the order that events happen in a story or set of directions.',
  [('What does the transition word first tell us?', ['what happens at the beginning', 'the earliest step']),
   ('What does the transition word finally tell us?', ['what happens at the end', 'the last step']),
   ('Give a sentence using the word then.', ['then I ate breakfast', 'then we went outside'])],
  [('What does the transition word first usually tell us?', ['What happens at the beginning', 'What happens at the end', 'Nothing about order', 'A characters name'], 0),
   ('What does the transition word finally usually tell us?', ['What happens at the end', 'What happens first', 'The title of the story', 'The setting of the story'], 0),
   ('Which word could describe the middle step in a set of directions?', ['Then', 'First', 'Finally', 'Never'], 0),
   ('Why are transition words helpful in writing?', ['They show the order that events happen', 'They make writing confusing', 'They remove the need for sentences', 'They have no purpose'], 0),
   ('Which sentence uses a transition word correctly?', ['First, we got dressed, then we ate breakfast', 'We got dressed we ate breakfast', 'Breakfast dressed we got then', 'Then dressed breakfast we'], 0)]),
M('Patterns: Increasing and Decreasing Number Patterns',
  'Grade 1 Math strand: students identify number patterns that increase, growing larger each time, or decrease, growing smaller each time.',
  [('What does an increasing pattern do?', ['gets bigger each time', 'numbers grow larger']),
   ('What does a decreasing pattern do?', ['gets smaller each time', 'numbers grow smaller']),
   ('Is 2, 4, 6, 8 an increasing or decreasing pattern?', ['increasing', 'it increases'])],
  [('What happens to the numbers in an increasing pattern?', ['They get bigger each time', 'They get smaller each time', 'They stay the same', 'They disappear'], 0),
   ('What happens to the numbers in a decreasing pattern?', ['They get smaller each time', 'They get bigger each time', 'They stay exactly the same', 'They become letters'], 0),
   ('Is the pattern 20, 15, 10, 5 increasing or decreasing?', ['Increasing', 'Decreasing', 'Neither', 'Both at once'], 1),
   ('Is the pattern 3, 6, 9, 12 increasing or decreasing?', ['Increasing', 'Decreasing', 'Neither', 'Both at once'], 0),
   ('What comes next in the increasing pattern 5, 10, 15, ___?', ['18', '20', '25', '30'], 1)]),
Sc('Bridges and Structures: Simple Engineering',
   'Grade 1 Science strand: bridges are structures built to help people and vehicles cross rivers, roads, or valleys safely.',
   [('What is a bridge used for?', ['helping people cross something', 'crossing rivers or roads safely']),
    ('What might a bridge cross over?', ['a river', 'a road or valley']),
    ('Why do bridges need to be built strongly?', ['so they can safely hold weight', 'to be safe for people and vehicles'])],
   [('What is the main purpose of a bridge?', ['To help people and vehicles cross safely', 'To block a river completely', 'To create more traffic', 'To decorate a city'], 0),
    ('Which of these might a bridge be built to cross?', ['A river', 'A single small puddle', 'A backyard', 'A classroom'], 0),
    ('Why is it important for a bridge to be built strongly?', ['So it can safely hold the weight of people and vehicles', 'Strength does not matter for bridges', 'So it can float away easily', 'So it can bend in half'], 0),
    ('What might engineers think about carefully when designing a bridge?', ['How much weight it needs to hold safely', 'What colour to paint it only', 'Nothing important at all', 'How to make it disappear'], 0),
    ('Bridges are an example of how people use ___ to solve problems.', ['Simple engineering', 'Magic', 'Guesswork with no planning', 'Random chance'], 0)]),
SS('Our School Yearbook: Remembering the School Year',
   'Grade 1 Social Studies strand: a school yearbook is a book filled with photos and memories that helps students remember their school year.',
   [('What is a school yearbook?', ['a book of photos and memories', 'a book that remembers the school year']),
    ('Why do schools make yearbooks?', ['to help students remember the year', 'keep special memories']),
    ('Name something you might see in a yearbook.', ['class photos', 'pictures of school events'])],
   [('What is a school yearbook?', ['A book filled with photos and memories from the school year', 'A math textbook', 'A list of school rules only', 'A calendar with no pictures'], 0),
    ('Why might a school create a yearbook?', ['To help students remember the school year', 'To replace all textbooks', 'It has no real purpose', 'To confuse students'], 0),
    ('Which of these might appear in a school yearbook?', ['Class photos', 'A grocery list', 'A weather forecast', 'A car manual'], 0),
    ('A yearbook can help students look back on their year and remember ___.', ['Special moments and friends', 'Nothing important', 'Only test scores', 'Only homework assignments'], 0),
    ('Yearbooks are usually created ___ during the school year.', ['Once, near the end', 'Every single day', 'Never', 'Only in summer'], 0)]),
]),
day(150, [
L('Language Review: New Vowel Teams, Word Parts, and Writing Skills',
  'Grade 1 Language strand review: students revisit the ow and ou vowel teams, prefixes and suffixes, text features, personal narrative writing, and transition words.',
  [('Give a word with the ow or ou vowel team.', ['cow', 'out']),
   ('What does the prefix over- usually mean?', ['too much']),
   ('What is a personal narrative?', ['a true story about the writer'])],
  [('Which word has the ow vowel team making the same sound as in cow?', ['Cow', 'Snow', 'Grow', 'Row'], 0),
   ('What does the prefix over- usually add to a word?', ['The meaning of too much', 'The meaning of colour', 'The meaning of a number', 'The meaning of sound'], 0),
   ('What does the word happiness mean?', ['The quality of being happy', 'Being sad', 'A type of food', 'A colour'], 0),
   ('What does bold print usually look like?', ['Darker, thicker letters', 'Slanted letters', 'Tiny letters', 'Underlined letters only'], 0),
   ('What does the transition word first usually tell us?', ['What happens at the beginning', 'What happens at the end', 'Nothing about order', 'A characters name'], 0)]),
M('Math Review: Numbers, Fractions, Time, and Patterns',
  'Grade 1 Math strand review: students revisit numbers to 400, counting up subtraction, fourths of a group, time to the minute, money, comparing numbers, measurement, and patterns.',
  [('What number comes right after 399?', ['400']),
   ('If 12 cookies are split into fourths, how many are in each group?', ['3']),
   ('How many centimetres are in one metre?', ['100'])],
  [('What number comes right after 399?', ['398', '399', '400', '401'], 2),
   ('If 12 cookies are split into fourths, how many cookies are in each group?', ['2', '3', '4', '6'], 1),
   ('If the minute hand points to the 3, how many minutes past the hour is it?', ['3', '10', '15', '30'], 2),
   ('Which number is greater, 312 or 321?', ['312', '321', 'They are equal', 'Neither has a value'], 1),
   ('How many centimetres are in one metre?', ['10', '50', '100', '1000'], 2)]),
Sc('Science Review: Our Bodies, Animals, and Habitats',
   'Grade 1 Science strand review: students revisit our kidneys, symbiosis, food webs, plant life cycles, extreme weather, sharks, frogs and toads, the rainforest, and bridges.',
   [('What is the main job of our kidneys?', ['filtering waste from our blood']),
    ('What is symbiosis?', ['when two living things help each other']),
    ('What kind of animals are frogs and toads?', ['amphibians'])],
   [('What is the main job of our kidneys?', ['Filtering waste out of our blood', 'Pumping blood around the body', 'Helping us breathe', 'Helping us see'], 0),
    ('What is symbiosis?', ['When two different living things help each other', 'When one animal eats another', 'A type of weather', 'A kind of rock'], 0),
    ('What is the first stage of a plants life cycle?', ['Seed', 'Flower', 'Root', 'Leaf'], 0),
    ('What kind of animal is a shark?', ['A fish', 'A mammal', 'A reptile', 'A bird'], 0),
    ('What kind of climate does a rainforest have?', ['Warm and wet', 'Cold and dry', 'Hot and dry like a desert', 'Frozen year round'], 0)]),
SS('Social Studies Review: Helpers, Government, and Our World',
   'Grade 1 Social Studies strand review: students revisit the school librarian, local news, peacekeepers, the school board, water systems, world landmarks, the legislature, fair trade, and yearbooks.',
   [('What is the main job of a school librarian?', ['helping students find and borrow books']),
    ('What do local radio and TV stations share?', ['news and weather']),
    ('What is fair trade?', ['buying goods in a way that pays workers fairly'])],
   [('What is the main job of a school librarian?', ['Helping students find and borrow books', 'Teaching math class', 'Driving the school bus', 'Cooking school lunches'], 0),
    ('What is the main job of a Canadian peacekeeper?', ['Helping keep peace in other countries', 'Teaching school in Canada', 'Driving a school bus', 'Cooking meals at home'], 0),
    ('What happens at a provincial legislature?', ['Elected leaders discuss and create laws', 'Students take a math test', 'Food is sold to the public', 'Movies are shown to visitors'], 0),
    ('What does fair trade mean?', ['Buying goods in a way that pays workers fairly', 'Buying the cheapest goods with no other thought', 'A type of holiday', 'A type of weather'], 0),
    ('What is a school yearbook?', ['A book filled with photos and memories from the school year', 'A math textbook', 'A list of school rules only', 'A calendar with no pictures'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_141_150)
    append_worksheet_days(1, g1_141_150)
