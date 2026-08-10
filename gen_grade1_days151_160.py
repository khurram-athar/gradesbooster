#!/usr/bin/env python3
"""Grade 1, Days 151-160 -- thirteenth batch, extending Grade 1 past Day 150
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days141_150.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-150 (dumped
and checked against data/grade1.json before writing): suffix -y, prefixes
in-/im-, hyperbole, book genres (fantasy, realistic fiction, fairy
tales), irregular plural nouns, conjunctions with because, list writing,
text boxes and sidebars, shape poems for Language. Numbers to 500, skip
counting by 50s, AM and PM, money up to five dollars, weight in
kilograms and grams, capacity in litres, sorting data into a table,
repeating patterns with shape/colour/size, sorting 2D shapes by number
of sides for Math. Our blood, tornadoes, polar bears, the ocean floor,
chameleons, jellyfish, earthworms, elephants, giraffes for Science.
Family Day, postal codes, Canadas national sports (hockey and
lacrosse), our school nurse, Canadas three oceans, time zones,
Canadian astronauts, our local conservation area, grandparents and
elders for Social Studies. Day 160 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior batch,
with review titles worded distinctly from the Day 140 and Day 150
review titles. No embedded ASCII double-quote or straight apostrophe
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


def _rebalance_answer_positions(days, seed=20260809):
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


g1_151_160 = [
day(151, [
L('Suffixes: Adding -y to Make Adjectives',
  'Grade 1 Language strand: adding the suffix -y to a noun can create an adjective describing something, such as changing rain into rainy or sun into sunny.',
  [('What does adding -y to rain make?', ['rainy', 'rainy weather']),
   ('What does adding -y to sun make?', ['sunny', 'sunny weather']),
   ('Give another example of a word with -y added.', ['windy', 'cloudy'])],
  [('Which word is formed by adding -y to rain?', ['Rainy', 'Rained', 'Raining', 'Rainer'], 0),
   ('Which word is formed by adding -y to sun?', ['Sunny', 'Sunned', 'Sunning', 'Suns'], 0),
   ('The suffix -y often turns a noun into a kind of ___.', ['Adjective', 'Verb', 'Pronoun', 'Preposition'], 0),
   ('Which word describes a day with lots of wind?', ['Windy', 'Wind', 'Winded', 'Winds'], 0),
   ('Adding -y to a word can help describe what the ___ is like.', ['Weather', 'Alphabet', 'Punctuation', 'Grammar'], 0)]),
M('Numbers to 500: Beyond 400',
  'Grade 1 Math strand: students read, write, and count numbers beyond 400, up to 500.',
  [('What number comes right after 499?', ['500', 'five hundred']),
   ('What number comes right before 450?', ['449', 'four hundred forty nine']),
   ('Count by tens from 480 to 500.', ['480,490,500', '480 490 500'])],
  [('What number comes right after 499?', ['500', '499', '501', '498'], 0),
   ('Which number is between 420 and 440?', ['430', '410', '450', '460'], 0),
   ('What number comes right before 500?', ['499', '500', '498', '501'], 0),
   ('Which of these numbers is the largest?', ['499', '399', '299', '199'], 0),
   ('Counting beyond 400 helps us understand numbers up to ___.', ['500', '50', '5', '5000'], 0)]),
Sc('Our Blood: Carrying Oxygen Through Our Body',
   'Grade 1 Science strand: our blood travels through our body carrying oxygen and nutrients to help keep every part of us working.',
   [('What does our blood carry to the rest of our body?', ['oxygen and nutrients', 'oxygen']),
    ('What organ pumps blood around our body?', ['the heart', 'heart']),
    ('Why is blood important for our body?', ['it keeps our body parts working', 'carries what we need to live'])],
   [('What does our blood mainly carry through our body?', ['Oxygen and nutrients', 'Only water', 'Only air', 'Nothing important'], 0),
    ('What organ pumps blood around our body?', ['The heart', 'The lungs', 'The stomach', 'The brain'], 0),
    ('Why do our body parts need blood?', ['To get oxygen and nutrients to keep working', 'Blood has no real job', 'To make us feel cold', 'To make us grow taller only'], 0),
    ('Which of these travels through our blood to our muscles?', ['Oxygen', 'Sound', 'Light', 'Electricity'], 0),
    ('Blood moves through our body inside tube-like pathways called ___.', ['Blood vessels', 'Bones', 'Muscles', 'Nerves'], 0)]),
SS('Family Day: A Special Ontario Holiday',
   'Grade 1 Social Studies strand: Family Day is a holiday in Ontario every February when families and friends can spend time together and rest.',
   [('What month is Family Day celebrated in Ontario?', ['February', 'in February']),
    ('Why do people celebrate Family Day?', ['to spend time with family', 'rest and be with family']),
    ('Name something a family might do together on Family Day.', ['go skating', 'play games together'])],
   [('In what month is Family Day celebrated in Ontario?', ['February', 'July', 'December', 'April'], 0),
    ('What is the main purpose of Family Day?', ['To spend time with family and friends', 'To go to school', 'To do extra homework', 'To clean the house only'], 0),
    ('Which of these might a family do together on Family Day?', ['Go skating together', 'Work at separate jobs all day', 'Stay apart from each other', 'Ignore each other'], 0),
    ('Family Day is an example of a ___ in Ontario.', ['Statutory holiday', 'School subject', 'Type of weather', 'Sports team'], 0),
    ('Family Day reminds us that spending time with family is ___.', ['Important', 'Unnecessary', 'Boring', 'A waste of time'], 0)]),
]),
day(152, [
L('Prefixes: in- and im-',
  'Grade 1 Language strand: the prefixes in- and im- can mean not, changing a word like active into inactive or possible into impossible.',
  [('What does the prefix in- often mean?', ['not', 'the opposite']),
   ('Give an example word using in- or im-.', ['inactive', 'impossible']),
   ('What does impossible mean?', ['not possible', 'cannot be done'])],
  [('What does the prefix in- often mean when added to a word?', ['Not', 'Very', 'Again', 'Before'], 0),
   ('Which word means not possible?', ['Impossible', 'Possible', 'Repossible', 'Prepossible'], 0),
   ('Which word means not active?', ['Inactive', 'Reactive', 'Preactive', 'Overactive'], 0),
   ('Adding in- or im- to a word usually changes its meaning to ___.', ['The opposite meaning', 'The same meaning', 'A colour', 'A number'], 0),
   ('Which word means not correct?', ['Incorrect', 'Precorrect', 'Overcorrect', 'Uncorrect'], 0)]),
M('Skip Counting by 50s',
  'Grade 1 Math strand: students practise skip counting by 50s, counting 50, 100, 150, and so on, to build number sense with larger numbers.',
  [('Count by 50s from 50 to 250.', ['50,100,150,200,250', '50 100 150 200 250']),
   ('What number comes after 200 when counting by 50s?', ['250', 'two hundred fifty']),
   ('Is 175 a number you would say when counting by 50s?', ['no', 'no it is not'])],
  [('What number comes right after 150 when counting by 50s?', ['200', '175', '160', '250'], 0),
   ('What number comes right after 300 when counting by 50s?', ['350', '325', '400', '375'], 0),
   ('Which of these numbers would you say when counting by 50s?', ['400', '410', '420', '430'], 0),
   ('Skip counting by 50s means adding ___ each time.', ['50', '5', '15', '100'], 0),
   ('Which of these numbers would NOT be said when counting by 50s starting at 50?', ['125', '100', '150', '200'], 0)]),
Sc('Tornadoes: Spinning Storms',
   'Grade 1 Science strand: a tornado is a spinning column of fast moving air that can form during a strong storm and cause damage.',
   [('What is a tornado?', ['a spinning column of air', 'a spinning storm']),
    ('What can happen when a tornado touches the ground?', ['it can cause damage', 'it can knock things down']),
    ('Where should you go to stay safe during a tornado?', ['a safe indoor space', 'a basement or interior room'])],
   [('What is a tornado?', ['A spinning column of fast moving air', 'A calm sunny breeze', 'A gentle rain shower', 'A quiet snowy day'], 0),
    ('What can a tornado do when it touches the ground?', ['Cause damage', 'Make flowers grow', 'Create rainbows', 'Cool the weather gently'], 0),
    ('Where is a safe place to go during a tornado?', ['A basement or interior room away from windows', 'Standing outside watching', 'Near a window for a better view', 'On a rooftop'], 0),
    ('Tornadoes often form during what kind of weather?', ['Strong thunderstorms', 'Calm sunny days', 'Light snowfall', 'Foggy mornings'], 0),
    ('Learning about tornadoes helps us know how to stay ___.', ['Safe', 'Careless', 'Unaware', 'Bored'], 0)]),
SS('Our Postal Code: A Special Set of Letters and Numbers',
   'Grade 1 Social Studies strand: a postal code is a special set of letters and numbers that helps mail carriers deliver mail to the right address.',
   [('What is a postal code made of?', ['letters and numbers', 'a mix of letters and numbers']),
    ('What does a postal code help with?', ['delivering mail', 'finding the right address']),
    ('Why is knowing your postal code useful?', ['helps mail reach you', 'helps others find your address'])],
   [('What is a postal code made up of?', ['Letters and numbers', 'Only pictures', 'Only colours', 'Only shapes'], 0),
    ('What does a postal code help mail carriers do?', ['Deliver mail to the right address', 'Bake bread', 'Drive a school bus', 'Water plants'], 0),
    ('Why might it be useful to know your own postal code?', ['It helps mail and packages reach your home', 'It has no real use', 'It changes every day', 'It is only used for games'], 0),
    ('A postal code is part of what larger piece of information?', ['Your home address', 'Your favourite colour', 'Your birthday', 'Your shoe size'], 0),
    ('Postal codes help make sure mail is delivered ___.', ['Accurately', 'Randomly', 'Never', 'Only on weekends'], 0)]),
]),
day(153, [
L('Hyperbole: Exaggerating for Effect',
  'Grade 1 Language strand: hyperbole is a big exaggeration used in stories to make a feeling or idea seem much bigger than it really is, like saying I could eat a horse.',
  [('What is hyperbole?', ['a big exaggeration', 'saying something is much bigger than true']),
   ('Give an example of hyperbole.', ['I could eat a horse', 'I have a million toys']),
   ('Why do writers use hyperbole?', ['to make a feeling seem bigger', 'for effect'])],
  [('What is hyperbole?', ['A big exaggeration used for effect', 'A true fact', 'A type of punctuation', 'A silent letter'], 0),
   ('Which sentence is an example of hyperbole?', ['I have a million toys', 'I have three toys', 'I have some toys', 'I have one toy'], 0),
   ('Why might an author use hyperbole in a story?', ['To make a feeling or idea seem bigger', 'To make the story shorter', 'To confuse the reader', 'To remove all feeling from a story'], 0),
   ('Which of these is an exaggeration?', ['This bag weighs a ton', 'This bag weighs two kilograms', 'This bag is empty', 'This bag is small'], 0),
   ('Hyperbole is a type of ___.', ['Figurative language', 'Punctuation mark', 'Silent letter', 'Vowel team'], 0)]),
M('Time: Understanding AM and PM',
  'Grade 1 Math strand: AM refers to the time from midnight to noon, while PM refers to the time from noon to midnight, helping us know if it is morning or evening.',
  [('Does AM mean morning or evening time?', ['morning', 'the morning part of the day']),
   ('Does PM mean morning or evening time?', ['evening', 'afternoon and evening']),
   ('Is 8 oclock in the morning AM or PM?', ['AM', 'it is AM'])],
  [('What part of the day does AM usually refer to?', ['Midnight to noon', 'Noon to midnight', 'Only nighttime', 'Only lunchtime'], 0),
   ('What part of the day does PM usually refer to?', ['Noon to midnight', 'Midnight to noon', 'Only breakfast time', 'Only bedtime'], 0),
   ('Is 7 oclock in the morning AM or PM?', ['AM', 'PM', 'Neither', 'Both'], 0),
   ('Is 7 oclock in the evening AM or PM?', ['PM', 'AM', 'Neither', 'Both'], 0),
   ('Knowing AM and PM helps us understand ___ of the day.', ['What time', 'What colour', 'What season', 'What weather'], 0)]),
Sc('Polar Bears: Giants of the Arctic',
   'Grade 1 Science strand: polar bears are large mammals with thick white fur that live in the Arctic and are strong swimmers who hunt seals.',
   [('Where do polar bears live?', ['the Arctic', 'in the Arctic']),
    ('What colour is a polar bears fur?', ['white', 'thick white fur']),
    ('What do polar bears often hunt?', ['seals', 'they hunt seals'])],
   [('Where do polar bears live?', ['The Arctic', 'The desert', 'The rainforest', 'The ocean floor'], 0),
    ('What colour is polar bear fur?', ['White', 'Black', 'Green', 'Orange'], 0),
    ('What do polar bears often hunt for food?', ['Seals', 'Zebras', 'Fish only in rivers', 'Insects'], 0),
    ('What kind of animal is a polar bear?', ['A mammal', 'A fish', 'A reptile', 'A bird'], 0),
    ('Polar bears are known to be strong ___.', ['Swimmers', 'Flyers', 'Diggers only', 'Climbers only'], 0)]),
SS('Canadas National Sports: Hockey and Lacrosse',
   'Grade 1 Social Studies strand: hockey is Canadas official winter sport and lacrosse is Canadas official summer sport, both loved by many Canadians.',
   [('What is Canadas official winter sport?', ['hockey', 'ice hockey']),
    ('What is Canadas official summer sport?', ['lacrosse']),
    ('Why do many Canadians enjoy hockey?', ['it is fun to play and watch', 'it is a fast exciting sport'])],
   [('What is Canadas official winter sport?', ['Hockey', 'Soccer', 'Basketball', 'Tennis'], 0),
    ('What is Canadas official summer sport?', ['Lacrosse', 'Baseball', 'Golf', 'Swimming'], 0),
    ('What season is hockey usually associated with?', ['Winter', 'Summer', 'Spring', 'Fall'], 0),
    ('Lacrosse is a sport that was first played by whom?', ['Indigenous peoples', 'Only recent settlers', 'Only astronauts', 'Only sailors'], 0),
    ('National sports like hockey and lacrosse are an important part of Canadas ___.', ['Culture', 'Weather', 'Government', 'Geography'], 0)]),
]),
day(154, [
L('Book Genres: Fantasy, Realistic Fiction, and Fairy Tales',
  'Grade 1 Language strand: books can belong to different genres, such as fantasy with magic, realistic fiction that could really happen, and fairy tales with classic story patterns.',
  [('What might you find in a fantasy story?', ['magic', 'dragons or magic']),
   ('What is realistic fiction?', ['a story that could really happen', 'made up but realistic']),
   ('Give an example of a fairy tale you know.', ['Cinderella', 'Snow White'])],
  [('What might you find in a fantasy story?', ['Magic and made-up creatures', 'Only true facts', 'Only real people', 'Only numbers'], 0),
   ('What makes a story realistic fiction?', ['It could really happen even though it is made up', 'It always includes dragons', 'It is always true', 'It has no characters'], 0),
   ('Which of these is a common feature of fairy tales?', ['A classic story pattern like a hero and a problem', 'Only diagrams and charts', 'Only real historical dates', 'Only recipes'], 0),
   ('Which of these is an example of a fairy tale?', ['Cinderella', 'A newspaper article', 'A math textbook', 'A weather report'], 0),
   ('Knowing about genres helps readers ___.', ['Choose books they will enjoy', 'Avoid reading altogether', 'Ignore the story', 'Skip every book'], 0)]),
M('Money: Counting Up to Five Dollars',
  'Grade 1 Math strand: students combine coins and bills to make amounts of money up to five dollars.',
  [('How many loonies make five dollars?', ['5', 'five loonies']),
   ('Name a way to make five dollars using bills or coins.', ['a five dollar bill', 'five loonies']),
   ('If you have three loonies and one toonie, how much money do you have?', ['5 dollars', 'five dollars'])],
  [('How many loonies would you need to make five dollars?', ['5', '4', '3', '2'], 0),
   ('Which combination makes exactly five dollars?', ['Five loonies', 'Two loonies', 'One toonie', 'Three quarters'], 0),
   ('If you have two toonies and one loonie, how much money do you have?', ['5 dollars', '4 dollars', '3 dollars', '2 dollars'], 0),
   ('Which single bill is worth five dollars?', ['A five dollar bill', 'A one dollar bill', 'A ten dollar bill', 'A twenty dollar bill'], 0),
   ('Practising with coins and bills up to five dollars helps us understand ___.', ['Larger amounts of money', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('The Ocean Floor: Exploring Under the Sea',
   'Grade 1 Science strand: the ocean floor is the ground under the sea, with features like mountains, valleys, and flat plains, home to many sea creatures.',
   [('What is the ocean floor?', ['the ground under the sea', 'the bottom of the ocean']),
    ('Name one feature found on the ocean floor.', ['mountains', 'valleys']),
    ('Why is the ocean floor important to sea creatures?', ['it gives them a home', 'provides shelter and food'])],
   [('What is the ocean floor?', ['The ground under the sea', 'The top of the water', 'A type of cloud', 'A kind of fish'], 0),
    ('Which of these might be found on the ocean floor?', ['Underwater mountains', 'Trees', 'Buildings', 'Roads'], 0),
    ('Why is the ocean floor important for sea creatures?', ['It provides a home and shelter', 'It has no importance', 'It is always empty', 'It only holds sand'], 0),
    ('Which of these lives on or near the ocean floor?', ['A crab', 'An eagle', 'A rabbit', 'A butterfly'], 0),
    ('The deepest parts of the ocean floor form deep ___.', ['Valleys', 'Deserts', 'Mountains only', 'Clouds'], 0)]),
SS('Our School Nurse: Keeping Us Healthy at School',
   'Grade 1 Social Studies strand: a school nurse helps take care of students who feel sick or hurt and teaches ways to stay healthy at school.',
   [('What does a school nurse help with?', ['taking care of sick or hurt students', 'helping students stay healthy']),
    ('Where does a school nurse usually work?', ['at school', 'in the school health room']),
    ('Why is having a school nurse helpful?', ['helps students feel better', 'keeps students safe and healthy'])],
   [('What is the main job of a school nurse?', ['Helping students who feel sick or hurt', 'Teaching math class', 'Driving the school bus', 'Cooking school lunches'], 0),
    ('Where does a school nurse usually work?', ['At school', 'In a grocery store', 'In a factory', 'At an airport'], 0),
    ('Why is it helpful for a school to have a nurse?', ['It helps keep students safe and healthy', 'It has no real purpose', 'It only helps teachers', 'It replaces doctors completely'], 0),
    ('Which of these might a school nurse help with?', ['A student with a scraped knee', 'Fixing a broken window', 'Planning a field trip', 'Painting a mural'], 0),
    ('A school nurse is an example of a helper who supports our ___.', ['Health', 'Homework', 'Transportation', 'Lunch menu'], 0)]),
]),
day(155, [
L('Plural Nouns: Irregular Plurals',
  'Grade 1 Language strand: some plural nouns do not simply add -s or -es, but change in special ways, such as mouse becoming mice or foot becoming feet.',
  [('What is the plural of mouse?', ['mice']),
   ('What is the plural of foot?', ['feet']),
   ('What is the plural of child?', ['children'])],
  [('What is the plural of mouse?', ['Mice', 'Mouses', 'Mices', 'Mousees'], 0),
   ('What is the plural of foot?', ['Feet', 'Foots', 'Feets', 'Footes'], 0),
   ('What is the plural of child?', ['Children', 'Childs', 'Childes', 'Childrens'], 0),
   ('What is the plural of tooth?', ['Teeth', 'Tooths', 'Teeths', 'Toothes'], 0),
   ('Irregular plurals are words that ___ when they become plural.', ['Change in a special way', 'Always add -s', 'Never change', 'Become shorter only'], 0)]),
M('Measurement: Weight in Kilograms and Grams',
  'Grade 1 Math strand: kilograms and grams are standard units used to measure how heavy something is, with grams used for lighter objects and kilograms for heavier ones.',
  [('Which unit would you use to weigh a feather, grams or kilograms?', ['grams']),
   ('Which unit would you use to weigh a dog, grams or kilograms?', ['kilograms']),
   ('Why do we use different units for weight?', ['some things are lighter or heavier', 'depends on the size of the object'])],
  [('Which unit would you use to weigh a small paperclip?', ['Grams', 'Kilograms', 'Metres', 'Litres'], 0),
   ('Which unit would you use to weigh a large dog?', ['Kilograms', 'Grams', 'Centimetres', 'Millilitres'], 0),
   ('Which is heavier, one kilogram or one gram?', ['One kilogram', 'One gram', 'They are the same', 'Neither has weight'], 0),
   ('Which tool do we use to measure weight?', ['A scale', 'A ruler', 'A clock', 'A thermometer'], 0),
   ('Grams are usually used to measure things that are ___.', ['Light', 'Very heavy', 'Tall', 'Long'], 0)]),
Sc('Chameleons: Colour-Changing Lizards',
   'Grade 1 Science strand: chameleons are lizards that can change the colour of their skin to blend in with their surroundings or show their feelings.',
   [('What kind of animal is a chameleon?', ['a lizard']),
    ('What special thing can a chameleon do?', ['change colour', 'change the colour of its skin']),
    ('Why might a chameleon change colour?', ['to blend in', 'to hide or show feelings'])],
   [('What kind of animal is a chameleon?', ['A lizard', 'A bird', 'A fish', 'A mammal'], 0),
    ('What special ability do chameleons have?', ['Changing the colour of their skin', 'Flying through the air', 'Breathing underwater only', 'Growing feathers'], 0),
    ('Why might a chameleon change its colour?', ['To blend in with its surroundings', 'To fly faster', 'To swim better', 'To grow bigger'], 0),
    ('Chameleons are an example of an animal with ___.', ['Camouflage abilities', 'Wings', 'Gills only', 'Fur'], 0),
    ('What kind of habitat might a chameleon live in?', ['A forest or jungle', 'The deep ocean', 'The Arctic ice', 'Outer space'], 0)]),
SS('Canadas Three Oceans: Atlantic, Pacific, and Arctic',
   'Grade 1 Social Studies strand: Canada is bordered by three oceans, the Atlantic Ocean in the east, the Pacific Ocean in the west, and the Arctic Ocean in the north.',
   [('Name one ocean that borders Canada.', ['Atlantic Ocean', 'Pacific Ocean']),
    ('Which ocean borders the west coast of Canada?', ['Pacific Ocean', 'the Pacific']),
    ('Which ocean borders the north of Canada?', ['Arctic Ocean', 'the Arctic'])],
   [('Which ocean borders the east coast of Canada?', ['The Atlantic Ocean', 'The Pacific Ocean', 'The Indian Ocean', 'The Southern Ocean'], 0),
    ('Which ocean borders the west coast of Canada?', ['The Pacific Ocean', 'The Atlantic Ocean', 'The Arctic Ocean', 'The Indian Ocean'], 0),
    ('Which ocean borders the north of Canada?', ['The Arctic Ocean', 'The Atlantic Ocean', 'The Pacific Ocean', 'The Indian Ocean'], 0),
    ('How many oceans border Canada?', ['3', '1', '2', '4'], 0),
    ('Being bordered by three oceans gives Canada a very long ___.', ['Coastline', 'Border with only one country', 'Desert region', 'Mountain range only'], 0)]),
]),
day(156, [
L('Conjunctions: Joining Ideas with Because',
  'Grade 1 Language strand: the word because is a conjunction that joins two ideas together to explain why something happens.',
  [('What does the word because help explain?', ['why something happens', 'a reason']),
   ('Give a sentence using the word because.', ['I was tired because I woke up early', 'I stayed inside because it was raining']),
   ('What kind of word is because?', ['a conjunction', 'a joining word'])],
  [('What does the word because usually explain?', ['Why something happens', 'When something happens', 'Where something happens', 'Who did something'], 0),
   ('Which sentence uses because correctly?', ['I stayed inside because it was raining', 'Because inside I stayed raining', 'Raining because it was I stayed inside', 'I stayed raining because inside'], 0),
   ('A conjunction is a word that ___.', ['Joins two ideas together', 'Ends a sentence', 'Starts every question', 'Replaces a noun'], 0),
   ('Which of these words is also a conjunction like because?', ['Since', 'Purple', 'Quickly', 'Running'], 0),
   ('Using because in a sentence helps the reader understand a ___.', ['Reason', 'Colour', 'Shape', 'Sound'], 0)]),
M('Measurement: Capacity in Litres',
  'Grade 1 Math strand: a litre is a standard unit used to measure capacity, or how much liquid a container can hold.',
  [('What does a litre measure?', ['capacity', 'how much liquid a container holds']),
   ('Name something that might hold about one litre of liquid.', ['a water bottle', 'a jug']),
   ('Would a bathtub hold more or less than one litre?', ['more', 'a lot more'])],
  [('What does a litre measure?', ['Capacity, or how much liquid something holds', 'Length', 'Weight', 'Time'], 0),
   ('Which of these might hold about one litre of water?', ['A large water bottle', 'A teaspoon', 'A swimming pool', 'A raindrop'], 0),
   ('Would a bathtub hold more or less than one litre of water?', ['More', 'Less', 'Exactly one litre', 'No water at all'], 0),
   ('Which tool might have litre markings on the side?', ['A measuring jug', 'A ruler', 'A clock', 'A thermometer'], 0),
   ('Litres help us measure the ___ of a container.', ['Capacity', 'Length', 'Weight', 'Temperature'], 0)]),
Sc('Jellyfish: Ocean Animals Without Bones',
   'Grade 1 Science strand: jellyfish are soft ocean animals without bones that float in the water and use stinging tentacles to catch food.',
   [('What kind of animal is a jellyfish?', ['an ocean animal without bones']),
    ('What do jellyfish use to catch food?', ['tentacles', 'stinging tentacles']),
    ('Where do jellyfish live?', ['the ocean'])],
   [('What is special about a jellyfish body?', ['It has no bones', 'It has many bones', 'It has a shell', 'It has fur'], 0),
    ('What do jellyfish use to catch food?', ['Stinging tentacles', 'Sharp teeth', 'Claws', 'Wings'], 0),
    ('Where do jellyfish live?', ['The ocean', 'The desert', 'The forest', 'The Arctic ice only'], 0),
    ('How do jellyfish usually move through the water?', ['By floating and gently pulsing', 'By walking on the ocean floor', 'By flying above the water', 'By digging tunnels'], 0),
    ('Jellyfish are an example of an animal that lives without a ___.', ['Skeleton of bones', 'Body', 'Home', 'Way to eat'], 0)]),
SS('Time Zones: Why Canada Has Different Times',
   'Grade 1 Social Studies strand: Canada is so wide that it has several time zones, meaning it can be a different time of day in different parts of the country at once.',
   [('Why does Canada have different time zones?', ['it is very wide', 'the country stretches across many hours']),
    ('If it is noon in one part of Canada, could it be a different time in another part?', ['yes', 'yes it could be different']),
    ('Why is it useful to know about time zones?', ['helps us know the time in other places', 'helps us call or visit at the right time'])],
   [('Why does Canada have several time zones?', ['Because the country is very wide', 'Because Canada is very small', 'Because Canada has no clocks', 'Because time zones are random'], 0),
    ('If it is noon in one part of Canada, could it be a different time in another part?', ['Yes, it could be different', 'No, it is always the same', 'Only on weekends', 'Only in winter'], 0),
    ('Why is it helpful to understand time zones?', ['It helps us know the time in other places', 'It has no real use', 'It only matters for math class', 'It changes the weather'], 0),
    ('How many time zones does Canada have?', ['Several', 'Only one', 'None', 'One hundred'], 0),
    ('Time zones exist because Earth is ___ shaped and turns as the sun shines on different parts.', ['Round', 'Flat', 'Square', 'Triangular'], 0)]),
]),
day(157, [
L('List Writing: Making a List for a Purpose',
  'Grade 1 Language strand: a list is a simple way of writing down items or steps in order, such as a grocery list or a list of things to pack.',
  [('What is a list used for?', ['writing down items in order', 'organizing information']),
   ('Give an example of a list you might write.', ['a grocery list', 'a list of toys']),
   ('Why is making a list helpful?', ['helps us remember things', 'keeps us organized'])],
  [('What is a list used for?', ['Writing down items or steps in order', 'Telling a made-up story', 'Drawing a picture', 'Singing a song'], 0),
   ('Which of these is an example of a list?', ['A grocery list', 'A fairy tale', 'A poem about the ocean', 'A letter to a friend'], 0),
   ('Why might someone write a list before going shopping?', ['To remember what they need to buy', 'To avoid buying anything', 'To write a story instead', 'To learn a new song'], 0),
   ('Lists are usually written in what kind of order?', ['One item after another', 'Backwards only', 'In a circle', 'Upside down'], 0),
   ('Making a list can help us stay ___.', ['Organized', 'Confused', 'Forgetful', 'Bored'], 0)]),
M('Data: Sorting Information into a Table',
  'Grade 1 Math strand: a table organizes information into rows and columns, making it easier to sort, compare, and read data.',
  [('What does a table help us do with information?', ['sort and organize it', 'compare data easily']),
   ('What are the two parts of a table called?', ['rows and columns']),
   ('Why might we use a table instead of just writing a list?', ['it is easier to compare', 'organizes information clearly'])],
  [('What does a table help us do with information?', ['Sort and organize it', 'Hide it', 'Erase it', 'Make it confusing'], 0),
   ('A table is made up of rows and what else?', ['Columns', 'Circles', 'Triangles', 'Lines only'], 0),
   ('Why might a table be easier to read than a plain list?', ['It organizes information clearly for comparing', 'It has no real benefit', 'It hides the information', 'It removes all the numbers'], 0),
   ('Which of these might be shown in a table?', ['The number of pets each classmate has', 'A made-up story', 'A drawing of a dragon', 'A song'], 0),
   ('Reading and making tables is a skill used in ___.', ['Data management', 'Only art class', 'Only gym class', 'Only music class'], 0)]),
Sc('Earthworms: Helpers in the Soil',
   'Grade 1 Science strand: earthworms live underground and help the soil by digging tunnels that let air and water reach plant roots.',
   [('Where do earthworms usually live?', ['underground', 'in the soil']),
    ('What do earthworms dig in the ground?', ['tunnels']),
    ('Why are earthworms helpful for plants?', ['let air and water reach roots', 'help the soil'])],
   [('Where do earthworms usually live?', ['Underground in the soil', 'In trees', 'In the ocean', 'In the sky'], 0),
    ('What do earthworms create as they move through soil?', ['Tunnels', 'Rivers', 'Roads', 'Bridges'], 0),
    ('How do earthworm tunnels help plants?', ['They let air and water reach plant roots', 'They block water from reaching roots', 'They harm plant roots', 'They have no effect on plants'], 0),
    ('Earthworms do not have which body part?', ['Legs', 'A body', 'Skin', 'A mouth'], 0),
    ('Earthworms are considered helpful because they improve the health of the ___.', ['Soil', 'Sky', 'Ocean', 'Clouds'], 0)]),
SS('Canadian Astronauts: Exploring Space for Canada',
   'Grade 1 Social Studies strand: Canadian astronauts travel to space to do research and represent Canada as part of international space missions.',
   [('What do Canadian astronauts travel to?', ['space']),
    ('What do astronauts do in space?', ['research', 'scientific research']),
    ('Why is it exciting when a Canadian goes to space?', ['represents Canada', 'shows what Canadians can achieve'])],
   [('Where do Canadian astronauts travel for their work?', ['Space', 'The ocean floor', 'The desert', 'The rainforest'], 0),
    ('What do astronauts often do while in space?', ['Scientific research', 'Play sports', 'Go shopping', 'Watch movies all day'], 0),
    ('Why is it special when a Canadian becomes an astronaut?', ['They represent Canada on international missions', 'It has no special meaning', 'Only Canadians can go to space', 'Astronauts never leave Earth'], 0),
    ('What might an astronaut wear outside a spacecraft?', ['A special space suit', 'Regular winter clothes', 'A raincoat', 'Nothing at all'], 0),
    ('Canadian astronauts often work as part of ___ space missions.', ['International', 'Only Canadian', 'Only American', 'Underwater'], 0)]),
]),
day(158, [
L('Text Features: Text Boxes and Sidebars',
  'Grade 1 Language strand: text boxes and sidebars are small sections on a page that give extra facts or interesting information related to the main text.',
  [('What is a text box used for?', ['extra information', 'giving extra facts']),
   ('Where is a sidebar usually found on a page?', ['on the side of the page']),
   ('Why do authors add text boxes?', ['to share interesting extra facts'])],
  [('What is a text box used for on a page?', ['Giving extra facts or information', 'Hiding the main text', 'Ending the book', 'Replacing all pictures'], 0),
   ('Where is a sidebar usually located on a page?', ['On the side of the page', 'In the middle of a sentence', 'On the back cover', 'Nowhere on the page'], 0),
   ('Why might an author include a text box in a nonfiction book?', ['To share interesting extra facts', 'To confuse the reader', 'To make the book shorter', 'To remove information'], 0),
   ('Which of these is an example of using a text feature?', ['A small box with a fun fact', 'Erasing a paragraph', 'Writing in invisible ink', 'Skipping a whole page'], 0),
   ('Text boxes and sidebars are examples of ___.', ['Text features', 'Punctuation marks', 'Vowel teams', 'Story characters'], 0)]),
M('Patterns: Repeating Patterns with Shape, Colour, and Size',
  'Grade 1 Math strand: repeating patterns can use more than one attribute at once, such as shape, colour, and size, to make the pattern more complex.',
  [('Name three attributes a pattern could use.', ['shape, colour, and size']),
   ('If a pattern goes big circle, small circle, big circle, small circle, what attribute is changing?', ['size']),
   ('Why might a pattern use more than one attribute?', ['makes the pattern more interesting', 'adds more detail'])],
  [('Which of these is an attribute a pattern could be based on?', ['Colour', 'A story', 'A season', 'A feeling'], 0),
   ('In the pattern big circle, small circle, big circle, small circle, what is changing?', ['Size', 'Colour only', 'Shape only', 'Nothing'], 0),
   ('A pattern using red square, blue square, red square, blue square is repeating based on ___.', ['Colour', 'Size', 'Sound', 'Weight'], 0),
   ('What comes next in the pattern big star, small star, big star, small star, ___?', ['Big star', 'Medium star', 'No star', 'A different shape'], 0),
   ('Patterns that use more than one attribute, like shape and colour together, are considered ___.', ['More complex', 'Impossible to make', 'Always the same', 'Only used in music'], 0)]),
Sc('Elephants: The Largest Land Animals',
   'Grade 1 Science strand: elephants are the largest land animals, known for their long trunks, big ears, and strong memories.',
   [('What is special about an elephants size?', ['they are the largest land animals']),
    ('What body part does an elephant use like a hand?', ['its trunk']),
    ('Name another feature elephants are known for.', ['big ears', 'strong memory'])],
   [('What is special about the size of an elephant?', ['It is the largest land animal', 'It is the smallest land animal', 'It is the fastest land animal', 'It is the tallest tree'], 0),
    ('What body part does an elephant use to grab food and water?', ['Its trunk', 'Its tail', 'Its ears', 'Its feet'], 0),
    ('What are elephants known for having, besides a trunk?', ['Big ears', 'Wings', 'Feathers', 'Gills'], 0),
    ('What kind of animal is an elephant?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Elephants are often described as having a strong ___.', ['Memory', 'Sense of smell only', 'Ability to fly', 'Ability to swim only'], 0)]),
SS('Our Local Conservation Area: Protecting Nature Nearby',
   'Grade 1 Social Studies strand: a conservation area is a piece of land near our community that is protected to keep plants, animals, and natural spaces safe.',
   [('What is a conservation area?', ['a protected piece of land']),
    ('Why are conservation areas protected?', ['to keep plants and animals safe']),
    ('Name something you might do at a conservation area.', ['go for a hike', 'look at nature'])],
   [('What is a conservation area?', ['A protected piece of land that keeps nature safe', 'A shopping mall', 'A parking lot', 'A factory'], 0),
    ('Why are conservation areas protected?', ['To keep plants, animals, and natural spaces safe', 'To build more houses', 'To create more roads', 'To store garbage'], 0),
    ('Which of these might you do at a conservation area?', ['Go for a nature walk', 'Watch a movie', 'Go grocery shopping', 'Attend a hockey game'], 0),
    ('Conservation areas help protect which of these?', ['Wildlife habitats', 'Shopping centres', 'Parking lots', 'Office buildings'], 0),
    ('Visiting a conservation area can help us appreciate ___.', ['Nature close to home', 'Only faraway places', 'Only cities', 'Only oceans'], 0)]),
]),
day(159, [
L('Shape Poems: Poetry You Can See',
  'Grade 1 Language strand: a shape poem is a poem written so that the words form the outline of the object the poem is about, combining writing and art.',
  [('What makes a shape poem special?', ['the words form a shape']),
   ('Give an example of a shape a poem could form.', ['a star', 'a tree']),
   ('Why might someone enjoy writing a shape poem?', ['it combines writing and art', 'it is fun and creative'])],
  [('What makes a shape poem different from a regular poem?', ['The words are arranged to form a shape', 'It has no words at all', 'It must rhyme perfectly', 'It cannot be about anything real'], 0),
   ('Which of these could be the shape of a shape poem?', ['A tree', 'Nothing at all', 'A blank page', 'A single letter'], 0),
   ('What two things does a shape poem combine?', ['Writing and art', 'Math and science', 'Music and dance', 'Cooking and gardening'], 0),
   ('Why might a student enjoy writing a shape poem?', ['It is a fun and creative way to write', 'It has strict boring rules', 'It cannot use any words', 'It must be written in one colour'], 0),
   ('A shape poem is a type of ___.', ['Poetry', 'Nonfiction report', 'Grocery list', 'Instruction manual'], 0)]),
M('Geometry: Sorting 2D Shapes by Number of Sides',
  'Grade 1 Math strand: 2D shapes can be sorted by how many sides they have, such as triangles with three sides or hexagons with six sides.',
  [('How many sides does a triangle have?', ['3', 'three']),
   ('How many sides does a hexagon have?', ['6', 'six']),
   ('Name a shape with four sides.', ['square', 'rectangle'])],
  [('How many sides does a triangle have?', ['3', '4', '5', '6'], 0),
   ('How many sides does a hexagon have?', ['6', '3', '4', '5'], 0),
   ('Which shape has four sides?', ['A square', 'A triangle', 'A hexagon', 'A circle'], 0),
   ('Sorting shapes by the number of sides is an example of ___.', ['Classifying shapes', 'Measuring length', 'Telling time', 'Counting money'], 0),
   ('Which of these shapes has no straight sides?', ['A circle', 'A square', 'A triangle', 'A hexagon'], 0)]),
Sc('Giraffes: The Tallest Land Animals',
   'Grade 1 Science strand: giraffes are the tallest land animals, with long necks that help them reach leaves high in trees.',
   [('What is special about a giraffes height?', ['they are the tallest land animals']),
    ('What body part helps a giraffe reach high leaves?', ['its long neck']),
    ('What do giraffes mainly eat?', ['leaves'])],
   [('What is special about the height of a giraffe?', ['It is the tallest land animal', 'It is the shortest land animal', 'It cannot stand up', 'It has no height at all'], 0),
    ('What body part helps a giraffe reach leaves high in trees?', ['Its long neck', 'Its short legs', 'Its small ears', 'Its tail'], 0),
    ('What do giraffes mainly eat?', ['Leaves', 'Meat', 'Fish', 'Insects only'], 0),
    ('What kind of animal is a giraffe?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Giraffes are often found living in which type of habitat?', ['The savanna', 'The Arctic', 'The deep ocean', 'The rainforest floor only'], 0)]),
SS('Grandparents and Elders: Learning from Our Elders',
   'Grade 1 Social Studies strand: grandparents and elders share wisdom, stories, and traditions with younger generations, helping communities remember their history.',
   [('What can grandparents and elders share with younger people?', ['stories and wisdom']),
    ('Why is it important to listen to elders?', ['they help us learn from the past']),
    ('Name something an elder might teach you.', ['a family story', 'a tradition'])],
   [('What can grandparents and elders often share with younger generations?', ['Stories and wisdom', 'Only chores', 'Only rules', 'Nothing important'], 0),
    ('Why is it valuable to listen to elders in a community?', ['They help us learn from the past', 'Their ideas are never useful', 'They have nothing to teach', 'They should be ignored'], 0),
    ('Which of these might an elder teach a child?', ['A family story or tradition', 'A new video game', 'A foreign language only', 'A math formula only'], 0),
    ('Many communities, including Indigenous communities, show elders great ___.', ['Respect', 'Disrespect', 'Indifference', 'Fear'], 0),
    ('Learning from elders helps younger generations understand their ___.', ['History and traditions', 'Homework only', 'Favourite foods only', 'Weather patterns'], 0)]),
]),
day(160, [
L('Language Review: Genres, Figurative Language, and Word Parts',
  'Grade 1 Language strand review: students revisit the suffix -y, prefixes in- and im-, hyperbole, book genres, irregular plural nouns, conjunctions, list writing, text boxes and sidebars, and shape poems.',
  [('What does adding -y to rain make?', ['rainy']),
   ('What does hyperbole mean?', ['a big exaggeration']),
   ('What is a conjunction?', ['a joining word'])],
  [('Which word is formed by adding -y to rain?', ['Rainy', 'Rained', 'Raining', 'Rainer'], 0),
   ('Which word means not possible?', ['Impossible', 'Possible', 'Repossible', 'Prepossible'], 0),
   ('What is hyperbole?', ['A big exaggeration used for effect', 'A true fact', 'A type of punctuation', 'A silent letter'], 0),
   ('Which of these is an example of a fairy tale?', ['Cinderella', 'A newspaper article', 'A math textbook', 'A weather report'], 0),
   ('What is the plural of mouse?', ['Mice', 'Mouses', 'Mices', 'Mousees'], 0)]),
M('Math Review: Numbers, Measurement, and Data',
  'Grade 1 Math strand review: students revisit numbers to 500, skip counting by 50s, AM and PM, money up to five dollars, kilograms and grams, litres, sorting data into tables, repeating patterns, and sorting 2D shapes.',
  [('What number comes right after 499?', ['500']),
   ('Which unit would you use to weigh a small paperclip?', ['grams']),
   ('How many sides does a triangle have?', ['3'])],
  [('What number comes right after 499?', ['500', '499', '501', '498'], 0),
   ('What number comes right after 150 when counting by 50s?', ['200', '175', '160', '250'], 0),
   ('Is 7 oclock in the morning AM or PM?', ['AM', 'PM', 'Neither', 'Both'], 0),
   ('Which unit would you use to weigh a large dog?', ['Kilograms', 'Grams', 'Centimetres', 'Millilitres'], 0),
   ('How many sides does a hexagon have?', ['6', '3', '4', '5'], 0)]),
Sc('Science Review: Weather, Animals, and the Human Body',
   'Grade 1 Science strand review: students revisit our blood, tornadoes, polar bears, the ocean floor, chameleons, jellyfish, earthworms, elephants, and giraffes.',
   [('What does our blood mainly carry through our body?', ['oxygen and nutrients']),
    ('What is a tornado?', ['a spinning column of air']),
    ('What is special about a giraffes height?', ['tallest land animal'])],
   [('What does our blood mainly carry through our body?', ['Oxygen and nutrients', 'Only water', 'Only air', 'Nothing important'], 0),
    ('What is a tornado?', ['A spinning column of fast moving air', 'A calm sunny breeze', 'A gentle rain shower', 'A quiet snowy day'], 0),
    ('Where do polar bears live?', ['The Arctic', 'The desert', 'The rainforest', 'The ocean floor'], 0),
    ('What kind of animal is a chameleon?', ['A lizard', 'A bird', 'A fish', 'A mammal'], 0),
    ('What is special about the height of a giraffe?', ['It is the tallest land animal', 'It is the shortest land animal', 'It cannot stand up', 'It has no height at all'], 0)]),
SS('Social Studies Review: Holidays, Helpers, and Geography',
   'Grade 1 Social Studies strand review: students revisit Family Day, postal codes, Canadas national sports, the school nurse, Canadas three oceans, time zones, Canadian astronauts, conservation areas, and learning from elders.',
   [('In what month is Family Day celebrated in Ontario?', ['February']),
    ('What is Canadas official winter sport?', ['hockey']),
    ('Why is it valuable to listen to elders in a community?', ['they help us learn from the past'])],
   [('In what month is Family Day celebrated in Ontario?', ['February', 'July', 'December', 'April'], 0),
    ('What is the main job of a school nurse?', ['Helping students who feel sick or hurt', 'Teaching math class', 'Driving the school bus', 'Cooking school lunches'], 0),
    ('Which ocean borders the west coast of Canada?', ['The Pacific Ocean', 'The Atlantic Ocean', 'The Arctic Ocean', 'The Indian Ocean'], 0),
    ('Where do Canadian astronauts travel for their work?', ['Space', 'The ocean floor', 'The desert', 'The rainforest'], 0),
    ('What is a conservation area?', ['A protected piece of land that keeps nature safe', 'A shopping mall', 'A parking lot', 'A factory'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_151_160)
    append_worksheet_days(1, g1_151_160)
