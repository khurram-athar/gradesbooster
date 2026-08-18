#!/usr/bin/env python3
"""Grade 1, Days 171-180 -- fifteenth batch, extending Grade 1 past Day 170
toward the full ~187-day school year. Self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to(), since those do not support a
worksheet field) modeled exactly on gen_grade1_days161_170.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by the video-backfill task)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics chosen to avoid overlap with existing Grade 1 Days 1-170 (dumped and
checked against data/grade1.json before writing): silent e (the magic e
rule), three-letter blends thr/squ/spl, text features (bullet points and
lists), media literacy (how commercials try to persuade us), brainstorming,
story maps for planning writing, active listening, chunking big words, and
revising writing for Language. Numbers to 700, fractions sixths, area
(covering a shape with square units), rounding to the nearest hundred,
money up to twenty dollars, comparing analog and digital clocks, reading a
picture graph with a key, finding lines of symmetry, and adding three
two-digit numbers for Math. Foxes, squirrels, screws and wedges (completing
the simple-machines set alongside the pulleys/wheels-axles/levers days
already used), friction, growing up and how our bodies change, wolves,
skunks, black bears, and deer for Science (all new animals/topics, not
reusing moose, raccoons, snails, crabs, camels, polar bears, elephants,
giraffes, chameleons, beavers, or any other animal from earlier batches).
Labour Day, our dentist, the Rocky Mountains, Indigenous games, Victoria
Day, sanitation workers, our pharmacist, the Prairies, and Halloween
community safety for Social Studies (new holiday, helper, and geography
topics, distinct from the many community-helper, holiday, and landmark
days already used in Days 1-170). Day 180 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior batch, with
review titles worded distinctly from every earlier review day's title
(checked against every "Review" title already present in data/grade1.json).
No embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz/worksheet text -- contractions and
possessives are avoided entirely, matching this project's convention (e.g.
"Canadas" not "Canada's", "oclock" not "o'clock"), since this text gets
embedded directly into TypeScript string literals.
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


def _rebalance_answer_positions(days, seed=20260818):
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


g1_171_180 = [
day(171, [
L('Silent e: The Magic e Rule',
  'Grade 1 Language strand: adding a silent e to the end of a short word can change a short vowel sound into a long vowel sound, such as changing cap into cape or kit into kite.',
  [('What does adding a silent e to cap turn it into?', ['cape', 'the word cape']),
   ('What does adding a silent e to kit turn it into?', ['kite', 'the word kite']),
   ('Does the silent e itself make a sound when we read it?', ['no', 'no it is silent'])],
  [('What does adding a silent e to the word cap turn it into?', ['Cape', 'Capped', 'Capping', 'Cape only in plural'], 0),
   ('What does adding a silent e to the word kit turn it into?', ['Kite', 'Kitten', 'Kits', 'Kitted'], 0),
   ('What kind of vowel sound does a silent e usually create in the word before it?', ['A long vowel sound', 'A short vowel sound', 'No vowel sound', 'A silent vowel sound'], 0),
   ('Which word uses the silent e rule to make a long vowel sound?', ['Cake', 'Cat', 'Can', 'Cap'], 0),
   ('A silent e at the end of a word is a letter that is written but ___.', ['Not pronounced', 'Always pronounced loudly', 'The first letter said', 'Always a consonant sound'], 0)]),
M('Numbers to 700: Beyond 600',
  'Grade 1 Math strand: students read, write, and count numbers beyond 600, up to 700.',
  [('What number comes right after 699?', ['700', 'seven hundred']),
   ('What number comes right before 650?', ['649', 'six hundred forty nine']),
   ('Count by tens from 680 to 700.', ['680,690,700', '680 690 700'])],
  [('What number comes right after 699?', ['700', '699', '701', '698'], 0),
   ('Which number is between 620 and 640?', ['630', '610', '650', '660'], 0),
   ('What number comes right before 700?', ['699', '700', '698', '701'], 0),
   ('Which of these numbers is the largest?', ['699', '599', '499', '399'], 0),
   ('Counting beyond 600 helps us understand numbers up to ___.', ['700', '70', '7', '7000'], 0)]),
Sc('Foxes: Clever Hunters of the Forest',
   'Grade 1 Science strand: foxes are small, clever mammals with pointed ears and bushy tails that hunt small animals in forests and fields, often at dawn and dusk.',
   [('What kind of tail does a fox have?', ['a bushy tail', 'bushy tail']),
    ('When does a fox often hunt?', ['at dawn and dusk', 'dawn and dusk']),
    ('What kind of animal is a fox?', ['a mammal'])],
   [('What kind of tail does a fox have?', ['A bushy tail', 'A shell', 'No tail at all', 'A flat tail'], 0),
    ('When does a fox often hunt for food?', ['At dawn and dusk', 'Only at noon', 'Only underwater', 'Only in winter'], 0),
    ('What kind of animal is a fox?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Where do foxes usually hunt?', ['Forests and fields', 'The ocean floor', 'The desert only', 'Inside caves under the sea'], 0),
    ('Foxes are known for being very ___ hunters.', ['Clever', 'Slow', 'Clumsy', 'Loud'], 0)]),
SS('Labour Day: Celebrating Workers',
   'Grade 1 Social Studies strand: Labour Day is a September holiday that celebrates the hard work of people in all kinds of jobs and marks the end of summer before school begins.',
   [('What does Labour Day celebrate?', ['the hard work of people', 'workers and their jobs']),
    ('In what month is Labour Day celebrated?', ['September']),
    ('What does Labour Day mark the end of?', ['summer', 'the end of summer'])],
   [('What does Labour Day celebrate?', ['The hard work of people in many jobs', 'A famous hockey game', 'A new school building', 'A type of weather'], 0),
    ('In which month is Labour Day celebrated?', ['September', 'January', 'April', 'November'], 0),
    ('What does Labour Day mark the start of for most students?', ['A new school year', 'Summer vacation', 'A winter holiday', 'A sports season'], 0),
    ('Labour Day is meant to honour people who do what?', ['Work at many different jobs', 'Only play sports', 'Only go on vacation', 'Only stay home'], 0),
    ('Celebrating workers on Labour Day shows that jobs are ___ to our communities.', ['Important', 'Unimportant', 'Boring', 'Unnecessary'], 0)]),
]),
day(172, [
L('Three-Letter Blends: thr, squ, and spl',
  'Grade 1 Language strand: some words begin with three consonants blended together, such as thr in three, squ in square, and spl in splash.',
  [('Give a word that starts with the thr blend.', ['three', 'throw']),
   ('Give a word that starts with the squ blend.', ['square', 'squirrel']),
   ('Give a word that starts with the spl blend.', ['splash', 'split'])],
  [('Which word starts with the thr blend?', ['Three', 'Tree', 'Free', 'Bee'], 0),
   ('Which word starts with the squ blend?', ['Square', 'Care', 'Bare', 'Fair'], 0),
   ('Which word starts with the spl blend?', ['Splash', 'Sash', 'Flash', 'Cash'], 0),
   ('A three-letter blend has how many consonant sounds blended together?', ['3', '1', '2', '4'], 0),
   ('Which of these words has a three-letter blend at the start?', ['Splash', 'Wash', 'Cash', 'Dash'], 0)]),
M('Fractions: Sixths of a Whole',
  'Grade 1 Math strand: when a whole is divided into six equal parts, each part is called a sixth, written as one out of six equal pieces.',
  [('What is each equal part called when a whole is split into six pieces?', ['a sixth', 'one sixth']),
   ('How many equal parts make a whole when it is divided into sixths?', ['6', 'six']),
   ('If you eat one sixth of a pizza, how many equal pieces are left?', ['5', 'five'])],
  [('What is each equal part called when a whole is divided into six pieces?', ['A sixth', 'A half', 'A third', 'A fifth'], 0),
   ('How many equal parts make up a whole divided into sixths?', ['6', '5', '4', '3'], 0),
   ('If a pizza is cut into sixths, how many pieces does it have in total?', ['6', '5', '4', '3'], 0),
   ('Which fraction shows one out of six equal parts?', ['One sixth', 'One half', 'One third', 'One fifth'], 0),
   ('For parts to be called sixths, they must be ___.', ['Equal in size', 'Different sizes', 'Only two pieces', 'Not connected'], 0)]),
Sc('Squirrels: Gathering Food for Winter',
   'Grade 1 Science strand: squirrels are small mammals with bushy tails that climb trees and gather and bury nuts and seeds in the fall to eat during the winter.',
   [('What do squirrels gather in the fall?', ['nuts and seeds', 'nuts']),
    ('Why do squirrels bury food?', ['to eat it later in winter', 'to save it for winter']),
    ('What helps a squirrel climb and balance in trees?', ['its bushy tail', 'bushy tail'])],
   [('What do squirrels gather in the fall?', ['Nuts and seeds', 'Fish', 'Leaves only', 'Ice'], 0),
    ('Why do squirrels bury food in the ground?', ['To eat it later during winter', 'To hide it forever', 'To grow new trees only', 'To share with birds only'], 0),
    ('What helps a squirrel balance while climbing trees?', ['Its bushy tail', 'Its wings', 'Its fins', 'Its shell'], 0),
    ('What kind of animal is a squirrel?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Squirrels are well known for being excellent tree ___.', ['Climbers', 'Swimmers', 'Diggers only', 'Flyers'], 0)]),
SS('Our Dentist: Caring for Our Teeth',
   'Grade 1 Social Studies strand: a dentist is a community helper who checks, cleans, and cares for our teeth to help keep our smiles healthy.',
   [('What does a dentist help take care of?', ['our teeth', 'teeth']),
    ('Name one thing a dentist might do during a visit.', ['clean our teeth', 'check our teeth']),
    ('Why is visiting the dentist important?', ['helps keep our teeth healthy', 'keeps our smile healthy'])],
   [('What does a dentist help take care of?', ['Our teeth', 'Our eyes', 'Our hair', 'Our shoes'], 0),
    ('What might a dentist do during a checkup?', ['Check and clean our teeth', 'Cut our hair', 'Fix a car', 'Deliver mail'], 0),
    ('Why is it important to visit the dentist regularly?', ['It helps keep our teeth and smile healthy', 'It has no real purpose', 'It only happens once in a lifetime', 'It replaces brushing at home'], 0),
    ('A dentist is an example of what kind of community member?', ['A community helper', 'A farmer', 'A pilot', 'A firefighter'], 0),
    ('Taking care of our teeth is part of taking care of our overall ___.', ['Health', 'Toys', 'Homework', 'Weather'], 0)]),
]),
day(173, [
L('Text Features: Bullet Points and Lists',
  'Grade 1 Language strand: bullet points and lists organize information into short separate pieces, making facts easier for readers to find and understand.',
  [('What do bullet points help organize?', ['information', 'facts into a list']),
   ('Why are lists helpful for readers?', ['easier to find information', 'makes facts easy to find']),
   ('Give an example of something you might write as a list.', ['a list of steps', 'a grocery list'])],
  [('What do bullet points and lists help organize?', ['Information into short separate pieces', 'A story into chapters', 'A picture into colours', 'A song into verses'], 0),
   ('Why might an author use a list instead of a paragraph?', ['To make facts easier to find', 'To make the text longer', 'To confuse the reader', 'To hide information'], 0),
   ('Which of these is an example of information written as a list?', ['Steps to make a sandwich', 'A long story about a dragon', 'A poem about the moon', 'A letter to a friend'], 0),
   ('Bullet points usually appear before each ___ in a list.', ['Item', 'Chapter', 'Author', 'Title'], 0),
   ('Lists and bullet points are a kind of ___.', ['Text feature', 'Punctuation mark', 'Vowel team', 'Suffix'], 0)]),
M('Area: Covering a Shape with Square Units',
  'Grade 1 Math strand: area is the amount of space inside a flat shape, and students measure it by counting how many equal square units are needed to cover the shape.',
  [('What is area?', ['the space inside a shape', 'amount of space inside a flat shape']),
   ('What do we count to measure area?', ['square units', 'squares that cover the shape']),
   ('If a shape is covered by six squares, what is its area?', ['6 square units', 'six'])],
  [('What is area?', ['The amount of space inside a flat shape', 'The distance around a shape', 'The number of corners a shape has', 'The colour of a shape'], 0),
   ('What do we count to find the area of a shape?', ['Square units that cover the shape', 'The sides of the shape', 'The corners of the shape', 'The colours in the shape'], 0),
   ('If a rectangle is covered by eight equal squares, what is its area?', ['8 square units', '4 square units', '2 square units', '10 square units'], 0),
   ('Which tool could help you measure the area of a shape?', ['Small equal squares', 'A thermometer', 'A clock', 'A calendar'], 0),
   ('Area tells us how much ___ is inside a flat shape.', ['Space', 'Time', 'Weight', 'Sound'], 0)]),
Sc('Simple Machines: Screws and Wedges',
   'Grade 1 Science strand: a screw is a simple machine shaped like a spiral ramp that holds things together, and a wedge is a simple machine shaped like a triangle that helps split or lift things.',
   [('What shape is a screw?', ['a spiral ramp', 'spiral shape']),
    ('What does a wedge help do?', ['split or lift things', 'splits things apart']),
    ('Name a place you might see a screw used.', ['a jar lid', 'holding wood together'])],
   [('What shape is a screw?', ['A spiral ramp', 'A perfect circle', 'A flat square', 'A straight line'], 0),
    ('What does a wedge help people do?', ['Split or lift objects', 'Tell time', 'Cook food', 'Measure temperature'], 0),
    ('Which of these commonly uses a screw?', ['A jar lid', 'A thermometer', 'A calendar', 'A clock'], 0),
    ('Which tool is shaped like a triangle and used to split things apart?', ['A wedge', 'A wheel', 'A pulley', 'A lever'], 0),
    ('Screws and wedges are both examples of ___.', ['Simple machines', 'Living things', 'Weather tools', 'Musical instruments'], 0)]),
SS('The Rocky Mountains: A Famous Canadian Landmark',
   'Grade 1 Social Studies strand: the Rocky Mountains are a tall, snow-capped mountain range in western Canada, known for their beautiful scenery and home to many animals.',
   [('What are the Rocky Mountains?', ['a tall mountain range', 'a mountain range in western Canada']),
    ('In what part of Canada are the Rocky Mountains found?', ['western Canada', 'the west']),
    ('Name one thing the Rocky Mountains are known for.', ['beautiful scenery', 'being home to many animals'])],
   [('What are the Rocky Mountains?', ['A tall, snow-capped mountain range', 'A large flat desert', 'A group of small islands', 'A busy city'], 0),
    ('In which part of Canada are the Rocky Mountains located?', ['Western Canada', 'Eastern Canada', 'Northern Canada only', 'Southern Ontario'], 0),
    ('What are the Rocky Mountains known for?', ['Beautiful scenery and wildlife', 'Being completely flat', 'Having no animals at all', 'Being under the ocean'], 0),
    ('What often covers the tops of the Rocky Mountains?', ['Snow', 'Sand', 'Grass only', 'Water only'], 0),
    ('The Rocky Mountains are an example of a Canadian ___.', ['Landmark', 'Holiday', 'Government building', 'Coin'], 0)]),
]),
day(174, [
L('Media Literacy: How Commercials Try to Persuade Us',
  'Grade 1 Language strand: commercials are short messages that try to persuade people to buy something or believe an idea, often using bright colours, music, and exciting words.',
  [('What is a commercial trying to do?', ['persuade people', 'get people to buy something']),
   ('Name one way commercials try to grab our attention.', ['bright colours', 'music']),
   ('Should we always believe everything a commercial says?', ['no', 'no we should think about it'])],
  [('What is the main purpose of a commercial?', ['To persuade people to buy something or believe an idea', 'To teach a math lesson', 'To tell the weather forecast', 'To read a bedtime story'], 0),
   ('Which of these might a commercial use to grab attention?', ['Bright colours and music', 'Only silence', 'Only plain black and white text', 'Only whispering'], 0),
   ('Why is it important to think carefully about commercials?', ['They are trying to persuade us and may not tell the whole story', 'They are always completely true', 'They never try to sell anything', 'They are the same as the news'], 0),
   ('Which of these is an example of a commercial?', ['A short ad for a new toy', 'A chapter in a novel', 'A page in a dictionary', 'A weather map'], 0),
   ('Being a smart media viewer means asking ___ about what we see.', ['Questions', 'Nothing at all', 'Only the price', 'Only the colours'], 0)]),
M('Rounding to the Nearest Hundred',
  'Grade 1 Math strand: rounding a number to the nearest hundred means deciding which multiple of one hundred it is closest to, such as rounding 340 to 300.',
  [('Round 340 to the nearest hundred.', ['300', 'three hundred']),
   ('Round 470 to the nearest hundred.', ['500', 'five hundred']),
   ('Is 250 exactly halfway between 200 and 300?', ['yes', 'yes it is'])],
  [('Round 340 to the nearest hundred.', ['300', '400', '350', '300 and 400'], 0),
   ('Round 470 to the nearest hundred.', ['500', '400', '450', '470'], 0),
   ('Round 620 to the nearest hundred.', ['600', '700', '650', '620'], 0),
   ('When a number ends in 50 or more, we usually round it ___ to the next hundred.', ['Up', 'Down', 'Sideways', 'Never'], 0),
   ('Rounding to the nearest hundred helps us find a ___ number that is easier to work with.', ['Simpler', 'More complicated', 'Smaller than zero', 'Random'], 0)]),
Sc('Friction: A Force That Slows Things Down',
   'Grade 1 Science strand: friction is a force created when two surfaces rub together, and it slows down or stops moving objects, such as a ball rolling to a stop on grass.',
   [('What is friction?', ['a force from surfaces rubbing together', 'a force that slows things down']),
    ('What can friction do to a moving object?', ['slow it down or stop it', 'slows it down']),
    ('Give an example of friction in everyday life.', ['a ball stopping on grass', 'rubbing your hands together'])],
   [('What is friction?', ['A force created when two surfaces rub together', 'A force that only exists in space', 'A type of light', 'A kind of sound'], 0),
    ('What effect does friction usually have on a moving object?', ['It slows the object down or stops it', 'It always speeds the object up', 'It has no effect at all', 'It changes the objects colour'], 0),
    ('Which surface would likely create more friction for a rolling ball?', ['Grass', 'Smooth ice', 'Polished wood', 'A slide'], 0),
    ('What happens when you rub your hands together quickly?', ['Friction makes your hands feel warm', 'Your hands turn cold instantly', 'Nothing happens at all', 'Your hands disappear'], 0),
    ('Friction is an example of a ___ that affects moving objects.', ['Force', 'Colour', 'Sound', 'Smell'], 0)]),
SS('Indigenous Games: Traditional Sports and Play',
   'Grade 1 Social Studies strand: Indigenous peoples in Canada have long played traditional games that build strength, skill, and teamwork, and many of these games are still played and celebrated today.',
   [('What do traditional Indigenous games help build?', ['strength and skill', 'strength, skill, and teamwork']),
    ('Are Indigenous games still played today?', ['yes', 'yes many still are']),
    ('Why might communities celebrate traditional games?', ['they honour Indigenous culture', 'to share and celebrate culture'])],
   [('What do traditional Indigenous games help build?', ['Strength, skill, and teamwork', 'Only reading skills', 'Only counting skills', 'Only quiet time'], 0),
    ('Are traditional Indigenous games still played today?', ['Yes, many are still played and celebrated', 'No, they stopped long ago', 'Only in other countries', 'Only by adults'], 0),
    ('Why might a community hold an event to celebrate traditional games?', ['To honour and share Indigenous culture', 'To replace all other sports', 'To keep the games secret', 'To avoid teamwork'], 0),
    ('Traditional Indigenous games are an example of ___ passed down over time.', ['Culture', 'Weather', 'Currency', 'Government'], 0),
    ('Learning about traditional games helps students understand and respect ___.', ['Indigenous culture', 'Only modern sports', 'Only board games', 'Only video games'], 0)]),
]),
day(175, [
L('Brainstorming: Gathering Ideas Before We Write',
  'Grade 1 Language strand: brainstorming means thinking of many ideas quickly before writing, often by making a list or web of words, so a writer has plenty of ideas to choose from.',
  [('What is brainstorming?', ['thinking of many ideas quickly', 'gathering ideas before writing']),
   ('Why might a writer brainstorm before starting a story?', ['to gather ideas first', 'so they have ideas to choose from']),
   ('Name one way to brainstorm ideas.', ['making a list', 'making a word web'])],
  [('What is brainstorming?', ['Thinking of many ideas quickly before writing', 'Writing a final copy neatly', 'Reading a finished book', 'Erasing all our ideas'], 0),
   ('Why do writers brainstorm before they begin writing?', ['So they have plenty of ideas to choose from', 'So they can skip writing altogether', 'So they never have to plan', 'So their story is shorter'], 0),
   ('Which of these is a common way to brainstorm ideas?', ['Making a list or word web', 'Reading the dictionary silently', 'Copying another story exactly', 'Erasing all notes'], 0),
   ('Brainstorming usually happens ___ a writer starts the final draft.', ['Before', 'After', 'Never', 'During printing'], 0),
   ('A good brainstorming session should produce ___ ideas.', ['Many', 'Zero', 'Exactly one', 'No new'], 0)]),
M('Money: Making Amounts Up to Twenty Dollars',
  'Grade 1 Math strand: students combine coins and bills to make amounts of money up to twenty dollars.',
  [('How many ten dollar bills make twenty dollars?', ['2', 'two ten dollar bills']),
   ('Name a way to make twenty dollars using bills.', ['a twenty dollar bill', 'two ten dollar bills']),
   ('If you have one ten dollar bill and one five dollar bill and one toonie, how much money do you have?', ['17 dollars', 'seventeen dollars'])],
  [('How many ten dollar bills would you need to make twenty dollars?', ['2', '1', '3', '4'], 0),
   ('Which combination makes exactly twenty dollars?', ['Two ten dollar bills', 'One ten dollar bill', 'Two five dollar bills', 'Three toonies'], 0),
   ('If you have one ten dollar bill and two five dollar bills, how much money do you have?', ['20 dollars', '15 dollars', '10 dollars', '25 dollars'], 0),
   ('Which single bill is worth twenty dollars?', ['A twenty dollar bill', 'A ten dollar bill', 'A five dollar bill', 'A one dollar bill'], 0),
   ('Practising with amounts up to twenty dollars helps us understand ___.', ['Even larger amounts of money', 'Only shapes', 'Only colours', 'Nothing useful'], 0)]),
Sc('Growing Up: How Our Bodies Change Over Time',
   'Grade 1 Science strand: our bodies grow and change as we get older, becoming taller and stronger, and we learn new skills at each stage of growing up.',
   [('Name one way our bodies change as we grow older.', ['we get taller', 'we grow taller and stronger']),
    ('What do we learn as we get older?', ['new skills', 'new skills at each stage']),
    ('Do babies, children, and adults look the same?', ['no', 'no they look different'])],
   [('What is one way our bodies change as we grow older?', ['We get taller and stronger', 'We always stay exactly the same', 'We become smaller each year', 'We stop needing food'], 0),
    ('What do people usually learn as they grow from a baby to a child?', ['New skills, such as walking and talking', 'Nothing new at all', 'Only how to sleep', 'Only how to sit still'], 0),
    ('Which of these shows a stage of growing up?', ['Baby, child, teenager, adult', 'Egg, tadpole, frog', 'Seed, sprout, flower', 'Caterpillar, cocoon, butterfly'], 0),
    ('Growing and changing over time happens to which of these?', ['All living things, including people', 'Only rocks', 'Only water', 'Only the weather'], 0),
    ('Learning about how our bodies grow helps us understand our own ___.', ['Growth', 'Weather', 'Money', 'Government'], 0)]),
SS('Victoria Day: An Ontario Spring Holiday',
   'Grade 1 Social Studies strand: Victoria Day is a holiday celebrated in May with fireworks and outdoor gatherings, marking the unofficial start of summer for many Canadian families.',
   [('In what month is Victoria Day celebrated?', ['May']),
    ('What do many families do to celebrate Victoria Day?', ['watch fireworks', 'have outdoor gatherings']),
    ('What does Victoria Day mark the start of for many families?', ['summer', 'the start of summer'])],
   [('In which month is Victoria Day celebrated?', ['May', 'July', 'September', 'February'], 0),
    ('What do many families do to celebrate Victoria Day?', ['Watch fireworks and gather outdoors', 'Stay inside all day', 'Go to school', 'Rake autumn leaves'], 0),
    ('What does Victoria Day mark the unofficial start of for many Canadians?', ['Summer', 'Winter', 'The school year', 'The new year'], 0),
    ('Victoria Day happens during which season in Canada?', ['Spring', 'Winter', 'Autumn', 'Late summer'], 0),
    ('Holidays like Victoria Day give communities a chance to gather and ___.', ['Celebrate together', 'Avoid each other', 'Stay indoors alone', 'Ignore the season'], 0)]),
]),
day(176, [
L('Story Maps: Planning a Story Before Writing',
  'Grade 1 Language strand: a story map is a graphic organizer that helps writers plan the characters, setting, problem, and solution of a story before they begin writing it.',
  [('What is a story map used for?', ['planning a story', 'planning before writing']),
   ('Name one part of a story a story map helps plan.', ['characters', 'the setting']),
   ('Should a story map be made before or after writing a story?', ['before', 'before writing'])],
  [('What is a story map?', ['A graphic organizer for planning a story', 'A map of a real country', 'A list of spelling words', 'A drawing of a classroom'], 0),
   ('Which of these might a story map help a writer plan?', ['Characters, setting, problem, and solution', 'Only the title of the book', 'Only the page numbers', 'Only the price of the book'], 0),
   ('When should a writer usually fill out a story map?', ['Before writing the story', 'After the story is published', 'Only while reading someone elses story', 'Never'], 0),
   ('A story map is an example of what kind of tool?', ['A graphic organizer', 'A musical instrument', 'A measuring tool', 'A cooking tool'], 0),
   ('Using a story map can help make our writing more ___.', ['Organized', 'Confusing', 'Random', 'Empty'], 0)]),
M('Time: Comparing Analog and Digital Clocks',
  'Grade 1 Math strand: an analog clock shows time with moving hands on a round face, while a digital clock shows time using numbers, and both tell us the same time in different ways.',
  [('What kind of clock uses moving hands on a round face?', ['an analog clock', 'analog clock']),
   ('What kind of clock shows time using numbers only?', ['a digital clock', 'digital clock']),
   ('Do an analog clock and a digital clock showing the same time tell different times?', ['no', 'no they show the same time'])],
  [('What kind of clock uses moving hands to show time?', ['An analog clock', 'A digital clock', 'A calendar', 'A thermometer'], 0),
   ('What kind of clock shows time using only numbers?', ['A digital clock', 'An analog clock', 'A sundial', 'A calendar'], 0),
   ('If an analog clock shows 3:00 and a digital clock shows 3:00, what does this mean?', ['They are showing the same time', 'They are showing different times', 'One of them is broken', 'Only the digital clock is correct'], 0),
   ('Which part of an analog clock points to the hour?', ['The short hand', 'The long hand', 'The numbers only', 'The battery'], 0),
   ('Comparing analog and digital clocks helps us understand that time can be shown in ___ ways.', ['Different', 'Only one', 'No', 'Random'], 0)]),
Sc('Wolves: Animals That Live and Hunt in Packs',
   'Grade 1 Science strand: wolves are wild mammals related to dogs that live and hunt together in groups called packs, working as a team to find food.',
   [('What group do wolves live and hunt in?', ['a pack', 'packs']),
    ('What animal are wolves related to?', ['dogs']),
    ('Why do wolves work together as a team?', ['to find food', 'to hunt together'])],
   [('What is a group of wolves called?', ['A pack', 'A herd', 'A flock', 'A colony'], 0),
    ('What animal are wolves closely related to?', ['Dogs', 'Cats', 'Bears', 'Foxes only'], 0),
    ('Why do wolves hunt together in a pack?', ['To work as a team to find food', 'Because they cannot see', 'To avoid running at all', 'Because they live underwater'], 0),
    ('What kind of animal is a wolf?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Wolves are known for communicating with each other by ___.', ['Howling', 'Buzzing', 'Chirping only', 'Staying silent'], 0)]),
SS('Sanitation Workers: Keeping Our Community Clean',
   'Grade 1 Social Studies strand: sanitation workers collect garbage and recycling from homes and businesses, helping keep our streets and neighbourhoods clean and healthy.',
   [('What do sanitation workers collect?', ['garbage and recycling', 'garbage']),
    ('What does the work of sanitation workers help keep clean?', ['our streets and neighbourhoods', 'our community']),
    ('Why is the work of sanitation workers important for health?', ['keeps the community healthy', 'stops garbage from piling up'])],
   [('What do sanitation workers collect?', ['Garbage and recycling', 'Mail and packages', 'Books for the library', 'Money for the bank'], 0),
    ('What does the work of sanitation workers help keep clean?', ['Our streets and neighbourhoods', 'Only the school playground', 'Only farms', 'Only the ocean'], 0),
    ('Why is collecting garbage regularly important for a community?', ['It helps keep the community clean and healthy', 'It makes streets messier', 'It has no real benefit', 'It only helps one house'], 0),
    ('Sanitation workers are an example of what kind of community member?', ['A community helper', 'A pilot', 'A judge', 'A farmer'], 0),
    ('Keeping our neighbourhoods clean is a job that benefits ___.', ['The whole community', 'No one', 'Only one family', 'Only pets'], 0)]),
]),
day(177, [
L('Listening Actively: Being a Good Listener',
  'Grade 1 Language strand: active listening means paying close attention to a speaker, looking at them, and thinking about what they are saying instead of interrupting.',
  [('What does active listening mean?', ['paying close attention', 'paying close attention to a speaker']),
   ('Name one thing a good listener does while someone is talking.', ['looks at the speaker', 'thinks about what they are saying']),
   ('Should a good listener interrupt while someone else is talking?', ['no', 'no they should wait'])],
  [('What does active listening mean?', ['Paying close attention to a speaker', 'Talking the whole time', 'Looking away from the speaker', 'Interrupting often'], 0),
   ('Which of these is a sign of a good listener?', ['Looking at the speaker and staying quiet', 'Talking over the speaker', 'Playing with toys instead', 'Walking away mid-sentence'], 0),
   ('Why is active listening important during a class discussion?', ['It helps us understand what others are saying', 'It stops us from learning anything', 'It makes conversations impossible', 'It has no real purpose'], 0),
   ('What should a good listener do before speaking after someone else?', ['Wait until the speaker is finished', 'Interrupt right away', 'Ignore what was said', 'Leave the room'], 0),
   ('Active listening helps us show ___ for the person speaking.', ['Respect', 'Confusion', 'Boredom', 'Impatience'], 0)]),
M('Data: Reading a Picture Graph with a Key',
  'Grade 1 Math strand: a picture graph uses small pictures to show data, and a key tells us how many items each picture represents, helping us read the graph correctly.',
  [('What does a picture graph use to show data?', ['pictures', 'small pictures']),
   ('What does the key on a picture graph tell us?', ['how many items each picture stands for', 'what each picture means']),
   ('If the key shows one picture equals two items, and there are three pictures, how many items are there in total?', ['6', 'six'])],
  [('What does a picture graph use to display data?', ['Small pictures', 'Only numbers', 'Only words', 'Only colours with no pictures'], 0),
   ('What does the key on a picture graph explain?', ['How many items each picture represents', 'The title of the graph only', 'The name of the teacher', 'The colour of the paper'], 0),
   ('If the key shows one picture equals two items, and there are four pictures, how many items are shown in total?', ['8', '4', '6', '2'], 0),
   ('Why is a key important on a picture graph?', ['It helps us read the graph correctly', 'It makes the graph harder to understand', 'It replaces the need for pictures', 'It has no real purpose'], 0),
   ('Picture graphs help us compare data in a way that is easy to ___.', ['See', 'Hear', 'Smell', 'Taste'], 0)]),
Sc('Skunks: Animals with a Stinky Defence',
   'Grade 1 Science strand: skunks are small black and white mammals that spray a strong smelling liquid to defend themselves when they feel scared or threatened.',
   [('What colours is a skunks fur usually?', ['black and white']),
    ('What does a skunk spray to defend itself?', ['a strong smelling liquid', 'smelly spray']),
    ('When does a skunk usually spray its smelly liquid?', ['when it feels scared or threatened', 'when threatened'])],
   [('What colours is a skunks fur usually?', ['Black and white', 'Orange and green', 'All grey', 'All brown'], 0),
    ('What does a skunk spray when it feels threatened?', ['A strong smelling liquid', 'Water only', 'Ink', 'Nothing at all'], 0),
    ('Why does a skunk spray its strong smelling liquid?', ['To defend itself from danger', 'To attract other skunks only', 'To clean its fur', 'To find food'], 0),
    ('What kind of animal is a skunk?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('A skunks spray is an example of an animal ___.', ['Defence', 'Song', 'Nest', 'Shell'], 0)]),
SS('Our Pharmacist: Helping Us Stay Healthy',
   'Grade 1 Social Studies strand: a pharmacist is a community helper who prepares medicine and explains to people how to take it safely to help them feel better.',
   [('What does a pharmacist prepare?', ['medicine']),
    ('What does a pharmacist explain to people?', ['how to take medicine safely', 'how to take their medicine']),
    ('Where might you visit to see a pharmacist?', ['a pharmacy', 'a drugstore'])],
   [('What does a pharmacist prepare for people?', ['Medicine', 'Meals', 'Mail', 'Books'], 0),
    ('What does a pharmacist explain to help keep people safe?', ['How to take medicine safely', 'How to fix a car', 'How to bake bread', 'How to fly a plane'], 0),
    ('Where would you go to visit a pharmacist?', ['A pharmacy', 'A fire station', 'A library', 'An airport'], 0),
    ('A pharmacist is an example of what kind of community member?', ['A community helper', 'A farmer', 'A pilot', 'A judge'], 0),
    ('Pharmacists work closely with doctors to help people stay ___.', ['Healthy', 'Confused', 'Hungry', 'Cold'], 0)]),
]),
day(178, [
L('Chunking: Breaking Big Words into Smaller Parts',
  'Grade 1 Language strand: chunking means breaking a long word into smaller parts, or syllables, to make it easier to read and sound out.',
  [('What does chunking a word mean?', ['breaking it into smaller parts', 'breaking a word into parts']),
   ('Why might chunking help a reader?', ['makes long words easier to read', 'easier to sound out']),
   ('Give an example of a long word you could break into chunks.', ['rabbit', 'basketball'])],
  [('What does chunking a word mean?', ['Breaking it into smaller parts', 'Erasing part of the word', 'Making the word longer', 'Changing the word into a picture'], 0),
   ('Why is chunking a helpful reading strategy?', ['It makes long words easier to sound out', 'It makes words impossible to read', 'It removes all vowels', 'It only works with short words'], 0),
   ('Which of these words could be broken into two chunks, rab and bit?', ['Rabbit', 'Cat', 'Dog', 'Sun'], 0),
   ('The smaller parts we break words into while chunking are called ___.', ['Syllables', 'Suffixes only', 'Prefixes only', 'Punctuation marks'], 0),
   ('Chunking is most helpful when reading words that are ___.', ['Long', 'Very short', 'Already familiar', 'Silent'], 0)]),
M('Geometry: Finding Lines of Symmetry',
  'Grade 1 Math strand: a line of symmetry divides a shape into two matching halves, and some shapes have more than one line of symmetry.',
  [('What does a line of symmetry do to a shape?', ['divides it into two matching halves', 'splits a shape into equal halves']),
   ('Can a shape have more than one line of symmetry?', ['yes', 'yes some shapes do']),
   ('Name a shape that has a line of symmetry.', ['a square', 'a circle'])],
  [('What does a line of symmetry do to a shape?', ['Divides it into two matching halves', 'Makes the shape bigger', 'Removes one side', 'Changes the shapes colour'], 0),
   ('Can a shape have more than one line of symmetry?', ['Yes, some shapes have several', 'No, every shape has exactly one', 'No shape ever has symmetry', 'Only circles have symmetry'], 0),
   ('Which of these shapes clearly has at least one line of symmetry?', ['A square', 'A scribble', 'An uneven blob', 'A random squiggle'], 0),
   ('If you fold a shape along its line of symmetry, the two halves should ___.', ['Match exactly', 'Look completely different', 'Disappear', 'Change colour'], 0),
   ('Finding lines of symmetry helps us understand how shapes can be ___.', ['Balanced', 'Heavier', 'Louder', 'Colder'], 0)]),
Sc('Black Bears: Foragers of the Forest',
   'Grade 1 Science strand: black bears are large forest mammals with a strong sense of smell that forage for berries, plants, and insects, and sleep through much of the winter.',
   [('Where do black bears mostly live?', ['forests', 'the forest']),
    ('What do black bears forage for?', ['berries, plants, and insects', 'berries and plants']),
    ('What do black bears do for much of the winter?', ['sleep', 'they sleep through winter'])],
   [('Where do black bears mostly live?', ['Forests', 'The desert', 'The ocean', 'A city street'], 0),
    ('What do black bears often forage for?', ['Berries, plants, and insects', 'Only rocks', 'Only sand', 'Only ice'], 0),
    ('What do black bears do for much of the winter?', ['Sleep through much of the winter', 'Migrate to the ocean', 'Stay awake and swim all season', 'Fly south'], 0),
    ('What kind of animal is a black bear?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Black bears are known for having a very strong sense of ___.', ['Smell', 'Sight only', 'Hearing only', 'Taste only'], 0)]),
SS('The Prairies: Canadas Flat Farming Land',
   'Grade 1 Social Studies strand: the Prairies are a large, mostly flat region in western Canada known for its wide fields, big skies, and important role in growing wheat and other crops.',
   [('What kind of land do the Prairies have?', ['flat land', 'mostly flat land']),
    ('In what part of Canada are the Prairies found?', ['western Canada']),
    ('What crop are the Prairies well known for growing?', ['wheat', 'wheat and other crops'])],
   [('What kind of land do the Prairies mostly have?', ['Flat land', 'Steep mountains', 'Deep ocean', 'Icy glaciers'], 0),
    ('In which part of Canada are the Prairies located?', ['Western Canada', 'Eastern Canada', 'Northern Canada only', 'The Atlantic coast'], 0),
    ('What crop is strongly associated with the Prairies?', ['Wheat', 'Bananas', 'Coconuts', 'Rice'], 0),
    ('What is the Prairies known for having above the flat land?', ['Big open skies', 'Tall skyscrapers only', 'Thick jungle canopy', 'No sky at all'], 0),
    ('The Prairies play an important role in Canadas ___.', ['Farming', 'Fishing only', 'Mining only', 'Shipping only'], 0)]),
]),
day(179, [
L('Revising: Making Our Writing Even Better',
  'Grade 1 Language strand: revising means rereading our writing and making changes to add details, fix confusing parts, or use stronger words, so our writing is clearer for readers.',
  [('What does revising mean?', ['making changes to writing', 'rereading and improving writing']),
   ('Name one reason a writer might revise their work.', ['to add details', 'to fix confusing parts']),
   ('Should revising happen before or after we write a first draft?', ['after', 'after the first draft'])],
  [('What does revising mean?', ['Rereading writing and making changes to improve it', 'Throwing away the writing completely', 'Reading someone elses story instead', 'Copying a story word for word'], 0),
   ('Which of these is a reason a writer might revise their work?', ['To add details or fix confusing parts', 'To make the writing shorter for no reason', 'To remove all the words', 'To avoid reading it again'], 0),
   ('When does revising usually happen in the writing process?', ['After writing a first draft', 'Before choosing a topic', 'Before brainstorming', 'Never'], 0),
   ('Which change would be part of revising a story?', ['Using a stronger, more exciting word', 'Erasing the whole page blank', 'Changing the paper colour', 'Ignoring the story completely'], 0),
   ('Revising helps make our writing more ___ for readers.', ['Clear', 'Confusing', 'Empty', 'Shorter without reason'], 0)]),
M('Addition: Adding Three Two-Digit Numbers',
  'Grade 1 Math strand: students practise adding three two-digit numbers together by adding the ones first, then the tens, to find the total.',
  [('What is 12 plus 13 plus 10?', ['35', 'thirty five']),
   ('What is 20 plus 20 plus 20?', ['60', 'sixty']),
   ('When adding three two-digit numbers, which digits do you add first?', ['the ones', 'the ones digits'])],
  [('What is 12 plus 13 plus 10?', ['35', '34', '36', '33'], 0),
   ('What is 20 plus 20 plus 20?', ['60', '50', '70', '40'], 0),
   ('When adding three two-digit numbers, which digits should you add first?', ['The ones digits', 'The tens digits', 'Neither digit', 'Both at random'], 0),
   ('What is 11 plus 22 plus 15?', ['48', '47', '49', '46'], 0),
   ('Adding three two-digit numbers together gives us a ___.', ['Total sum', 'Difference', 'Fraction', 'Product only'], 0)]),
Sc('Deer: Graceful Animals of the Forest',
   'Grade 1 Science strand: deer are graceful mammals with slender legs that live in forests and fields, eating plants and grasses, and some males grow antlers each year.',
   [('Where do deer usually live?', ['forests and fields', 'forests']),
    ('What do deer mainly eat?', ['plants and grasses', 'plants']),
    ('What do some male deer grow each year?', ['antlers'])],
   [('Where do deer usually live?', ['Forests and fields', 'The ocean floor', 'The desert only', 'Under the ice'], 0),
    ('What do deer mainly eat?', ['Plants and grasses', 'Fish', 'Other animals', 'Insects only'], 0),
    ('What do some male deer grow each year?', ['Antlers', 'Wings', 'A shell', 'Feathers'], 0),
    ('What kind of animal is a deer?', ['A mammal', 'A reptile', 'A bird', 'A fish'], 0),
    ('Deer are often described as having very ___ legs, which help them run quickly.', ['Slender', 'Short and stubby', 'Missing entirely', 'Made of stone'], 0)]),
SS('Halloween: Community Safety and Fun',
   'Grade 1 Social Studies strand: Halloween is an October holiday when many families dress in costumes and visit neighbours for treats, while also following safety rules like staying with an adult and using flashlights.',
   [('In what month is Halloween celebrated?', ['October']),
    ('What do many families wear on Halloween?', ['costumes']),
    ('Name one safety rule people follow on Halloween.', ['stay with an adult', 'use flashlights'])],
   [('In which month is Halloween celebrated?', ['October', 'March', 'June', 'January'], 0),
    ('What do many people wear to celebrate Halloween?', ['Costumes', 'Winter coats only', 'Swimsuits', 'School uniforms'], 0),
    ('Which of these is a Halloween safety rule?', ['Staying with a trusted adult', 'Walking alone in the dark streets', 'Ignoring traffic lights', 'Entering strangers homes alone'], 0),
    ('Why might people use flashlights or reflective gear on Halloween?', ['To be seen more easily in the dark', 'To make it harder to be seen', 'To scare away neighbours', 'To avoid walking at all'], 0),
    ('Following safety rules on Halloween helps keep our community ___.', ['Safe', 'Confused', 'Dark', 'Unfriendly'], 0)]),
]),
day(180, [
L('Language Review: Word Study, Media Literacy, and Writing Process',
  'Grade 1 Language strand review: students revisit silent e, three-letter blends thr, squ, and spl, bullet point text features, media literacy with commercials, brainstorming, story maps, active listening, chunking, and revising.',
  [('What does adding a silent e to the word cap turn it into?', ['cape']),
   ('What is the main purpose of a commercial?', ['to persuade people']),
   ('What does revising mean?', ['rereading and improving writing'])],
  [('What does adding a silent e to the word kit turn it into?', ['Kite', 'Kitten', 'Kits', 'Kitted'], 0),
   ('Which word starts with the squ blend?', ['Square', 'Care', 'Bare', 'Fair'], 0),
   ('What do bullet points and lists help organize?', ['Information into short separate pieces', 'A story into chapters', 'A picture into colours', 'A song into verses'], 0),
   ('What is a story map?', ['A graphic organizer for planning a story', 'A map of a real country', 'A list of spelling words', 'A drawing of a classroom'], 0),
   ('What does chunking a word mean?', ['Breaking it into smaller parts', 'Erasing part of the word', 'Making the word longer', 'Changing the word into a picture'], 0)]),
M('Math Review: Numbers, Area, and Money',
  'Grade 1 Math strand review: students revisit numbers to 700, fractions as sixths, area with square units, rounding to the nearest hundred, money up to twenty dollars, comparing analog and digital clocks, picture graphs with a key, lines of symmetry, and adding three two-digit numbers.',
  [('What number comes right after 699?', ['700']),
   ('What is each equal part called when a whole is divided into six pieces?', ['a sixth']),
   ('What does a line of symmetry do to a shape?', ['divides it into two matching halves'])],
  [('What number comes right after 699?', ['700', '699', '701', '698'], 0),
   ('What is each equal part called when a whole is divided into six pieces?', ['A sixth', 'A half', 'A third', 'A fifth'], 0),
   ('Round 340 to the nearest hundred.', ['300', '400', '350', '300 and 400'], 0),
   ('What kind of clock shows time using only numbers?', ['A digital clock', 'An analog clock', 'A sundial', 'A calendar'], 0),
   ('What is 12 plus 13 plus 10?', ['35', '34', '36', '33'], 0)]),
Sc('Science Review: Forest Animals, Forces, and Growth',
   'Grade 1 Science strand review: students revisit foxes, squirrels, screws and wedges, friction, growing up and how our bodies change, wolves, skunks, black bears, and deer.',
   [('What kind of animal is a fox?', ['a mammal']),
    ('What is friction?', ['a force from surfaces rubbing together']),
    ('What is a group of wolves called?', ['a pack'])],
   [('When does a fox often hunt for food?', ['At dawn and dusk', 'Only at noon', 'Only underwater', 'Only in winter'], 0),
    ('What shape is a screw?', ['A spiral ramp', 'A perfect circle', 'A flat square', 'A straight line'], 0),
    ('What effect does friction usually have on a moving object?', ['It slows the object down or stops it', 'It always speeds the object up', 'It has no effect at all', 'It changes the objects colour'], 0),
    ('What do black bears do for much of the winter?', ['Sleep through much of the winter', 'Migrate to the ocean', 'Stay awake and swim all season', 'Fly south'], 0),
    ('What do some male deer grow each year?', ['Antlers', 'Wings', 'A shell', 'Feathers'], 0)]),
SS('Social Studies Review: Holidays, Community Helpers, and Landmarks',
   'Grade 1 Social Studies strand review: students revisit Labour Day, our dentist, the Rocky Mountains, Indigenous games, Victoria Day, sanitation workers, our pharmacist, the Prairies, and Halloween.',
   [('In what month is Labour Day celebrated?', ['September']),
    ('What does a dentist help take care of?', ['our teeth']),
    ('In what month is Halloween celebrated?', ['October'])],
   [('What does Labour Day celebrate?', ['The hard work of people in many jobs', 'A famous hockey game', 'A new school building', 'A type of weather'], 0),
    ('What are the Rocky Mountains known for?', ['Beautiful scenery and wildlife', 'Being completely flat', 'Having no animals at all', 'Being under the ocean'], 0),
    ('In which month is Victoria Day celebrated?', ['May', 'July', 'September', 'February'], 0),
    ('What do sanitation workers collect?', ['Garbage and recycling', 'Mail and packages', 'Books for the library', 'Money for the bank'], 0),
    ('What crop is strongly associated with the Prairies?', ['Wheat', 'Bananas', 'Coconuts', 'Rice'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g1_171_180)
    append_worksheet_days(1, g1_171_180)
