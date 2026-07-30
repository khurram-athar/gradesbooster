#!/usr/bin/env python3
"""Grade 3, Days 111-120 -- extends Grade 3 from 110 to 120 days. Modeled
exactly on gen_grade3_days101_110.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-110
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum: pronoun-antecedent agreement, genre
identification, analogies, dialogue writing, summarizing nonfiction,
symbolism, speech-giving, abbreviations/acronyms, and shades of meaning
for Language; equivalent fractions, two-digit division and multiplication,
line plots, simple interest, perimeter vs area, rounding to the nearest
100, multiplication-chart patterns, and probability language for Math;
owls, bats, comets/asteroids, fish, hibernation, tundra habitats,
lightning, fossil fuels, and the digestive system for Science; and the
Interior Plains region, the monarchy, the RCMP, the justice system, the
census, Terry Fox, Canada Day, sister cities, and the Commonwealth for
Social Studies -- none of those exact ideas appear in Days 1-110. Day 120
is a review day across all four subjects, matching the end-of-batch
pattern used in every prior 10-day batch. No embedded ASCII double-quote
or straight apostrophe characters are used anywhere in question/summary/
option text; apostrophes and quotation marks use the curly Unicode form
(u2019 u201c u201d), matching the rest of Grade 3.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L3 = 'https://tvolearn.com/pages/grade-3-language'
M3 = 'https://tvolearn.com/pages/grade-3-mathematics'
S3 = 'https://tvolearn.com/pages/grade-3-science-and-technology'
SS3 = 'https://tvolearn.com/pages/grade-3-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 3 Language',
    'TVO Learn: Grade 3 Mathematics',
    'TVO Learn: Grade 3 Science and Technology',
    'TVO Learn: Grade 3 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L3, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M3, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S3, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS3, q)


def _rebalance_answer_positions(days, seed=20260730):
    import random
    rng = random.Random(seed)
    quizzes = [sub_entry[5] for _, subs in days for sub_entry in subs]
    n = sum(len(q) for q in quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in quizzes:
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


g3_111_120 = [
day(111, [
L('Grammar: Pronoun-Antecedent Agreement',
  'Grade 3 Language strand: a pronoun must match its antecedent (the noun it replaces) in number, using a singular pronoun for a singular noun and a plural pronoun for a plural noun.',
  [('In the sentence Maria lost her book, what is the antecedent of her?', ['Maria', 'lost', 'book', 'her'], 0),
   ('Which pronoun correctly replaces the plural noun in The dogs ate ___ food?', ['its', 'his', 'their', 'her'], 2),
   ('Which pronoun correctly replaces the singular noun in Sam packed ___ lunch?', ['their', 'his', 'they', 'our'], 1),
   ('What does it mean for a pronoun to agree with its antecedent?', ['They match in number (singular or plural)', 'They must rhyme', 'They must be the same length', 'They must start with the same letter'], 0),
   ('Which sentence has correct pronoun-antecedent agreement?', ['The students opened his book.', 'The girl opened their book.', 'The boys opened their books.', 'The team opened its books wrongly matched.'], 2)]),
M('Fractions: Equivalent Fractions',
  'Grade 3 Math strand: equivalent fractions are different fractions that name the same amount, such as 1/2 and 2/4, found by multiplying or dividing the numerator and denominator by the same number.',
  [('Which fraction is equivalent to 1/2?', ['2/4', '1/4', '3/8', '2/3'], 0),
   ('Which fraction is equivalent to 2/3?', ['3/4', '4/6', '2/6', '1/3'], 1),
   ('To find an equivalent fraction, you multiply the numerator and denominator by ___.', ['Different numbers', 'The same number', 'Zero', 'A fraction'], 1),
   ('Which fraction is NOT equivalent to 1/3?', ['2/6', '3/9', '4/12', '1/2'], 3),
   ('Why are 2/4 and 1/2 considered equivalent?', ['They represent the same amount', 'They have the same numerator', 'They have the same denominator', 'They look identical when written'], 0)]),
Sc('Science: Owls — Nocturnal Hunters with Special Adaptations',
   'Grade 3 Science strand: owls are birds adapted for nighttime hunting, with excellent hearing, silent flight feathers, and the ability to turn their heads far around.',
   [('When are owls typically active?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
    ('What adaptation helps owls fly without being heard by prey?', ['Silent flight feathers', 'Bright colours', 'Loud wingbeats', 'Long tails'], 0),
    ('Why is excellent hearing important for an owl?', ['It helps locate prey in the dark', 'It helps the owl swim', 'It helps the owl change colour', 'It has no purpose'], 0),
    ('How far can many owls turn their heads?', ['Nearly all the way around', 'Not at all', 'Only slightly to one side', 'Upside down only'], 0),
    ('What word describes an animal that is mainly active at night?', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0)]),
SS('Social Studies: Physical Regions of Canada — The Interior Plains',
   'Grade 3 Social Studies strand: the Interior Plains is a large, flat region of Canada known for fertile farmland, grasslands, and oil and gas resources.',
   [('What is the Interior Plains region known for?', ['Fertile farmland and grasslands', 'Tall mountains only', 'Tropical rainforest', 'Coral reefs'], 0),
    ('Which natural resources are commonly found in the Interior Plains?', ['Oil and gas', 'Coral', 'Volcanic rock only', 'Icebergs'], 0),
    ('How would you describe the landscape of the Interior Plains?', ['Mostly flat', 'Mostly mountainous', 'Mostly underwater', 'Mostly desert dunes'], 0),
    ('Why is the Interior Plains important for farming?', ['Its flat, fertile land suits growing crops', 'It never receives any rain', 'It is covered in ice year-round', 'It has no soil'], 0),
    ('The Interior Plains is one of several physical regions that make up ___.', ['Canada', 'The United States only', 'Europe', 'A single city'], 0)]),
]),
day(112, [
L('Reading: Identifying Genre — Fiction, Nonfiction, and Poetry',
  'Grade 3 Language strand: readers identify a texts genre, or category, such as fiction, nonfiction, or poetry, using clues like structure, purpose, and content.',
  [('What is genre?', ['A category or type of text', 'The title of a book', 'The last page of a book', 'A punctuation mark'], 0),
   ('Which genre tells a made-up story?', ['Fiction', 'Nonfiction', 'A dictionary entry', 'A recipe'], 0),
   ('Which genre presents true facts and information?', ['Nonfiction', 'Fiction', 'A fairy tale', 'A fable'], 0),
   ('Which clue might help identify a poem?', ['Lines that do not fill the whole page and may rhyme', 'A table of contents', 'A glossary', 'Chapter numbers'], 0),
   ('Why is it useful to identify a texts genre before reading?', ['It helps set expectations for content and structure', 'It has no effect on reading', 'It changes the words in the book', 'It tells you the price of the book'], 0)]),
M('Division: Two-Digit by One-Digit Division',
  'Grade 3 Math strand: students divide a two-digit number by a one-digit number, such as 48 divided by 4, using place value strategies or repeated subtraction.',
  [('What is 48 divided by 4?', ['10', '11', '12', '13'], 2),
   ('What is 63 divided by 7?', ['8', '9', '10', '11'], 1),
   ('What is 84 divided by 6?', ['12', '13', '14', '15'], 2),
   ('What is 72 divided by 8?', ['8', '9', '10', '11'], 1),
   ('One strategy for dividing a two-digit number is to break it into ___.', ['Friendlier smaller parts', 'Random digits', 'Only even numbers', 'Fractions only'], 0)]),
Sc('Science: Bats — Nocturnal Mammals That Use Echolocation',
   'Grade 3 Science strand: bats are the only flying mammals, and many species use echolocation, bouncing sound off objects, to navigate and find food in the dark.',
   [('What makes bats unique among mammals?', ['They are the only mammals that truly fly', 'They live underwater', 'They have no fur', 'They lay eggs'], 0),
    ('What is echolocation?', ['Using sound to locate objects', 'Using light to see', 'Using smell to hunt', 'Using taste to navigate'], 0),
    ('When are most bats active?', ['At night', 'At noon', 'Only in winter', 'Only underwater'], 0),
    ('How do bats use echolocation to find food?', ['They listen for sound bouncing back off insects', 'They smell insects from far away', 'They see insects glow in the dark', 'They taste the air'], 0),
    ('Bats are classified as ___.', ['Mammals', 'Birds', 'Insects', 'Reptiles'], 0)]),
SS('Social Studies: Canadas Head of State — The Role of the Monarchy',
   'Grade 3 Social Studies strand: Canada is a constitutional monarchy, meaning the reigning monarch is Canadas ceremonial head of state, represented locally by the Governor General.',
   [('What type of government does Canada have regarding its head of state?', ['A constitutional monarchy', 'A dictatorship', 'No government at all', 'A monarchy with total power'], 0),
    ('Who represents the monarch in Canada?', ['The Governor General', 'The Prime Minister only', 'A mayor', 'A judge'], 0),
    ('Is the monarchs role in Canada mostly ceremonial today?', ['Yes', 'No, the monarch runs daily government', 'The monarch has no role at all', 'The monarch controls all laws directly'], 0),
    ('Who actually runs the day-to-day government of Canada?', ['Elected officials like the Prime Minister', 'The monarch alone', 'No one', 'A random citizen'], 0),
    ('A constitutional monarchy combines a monarch with ___.', ['A democratic, elected government', 'No laws at all', 'Only military rule', 'Complete royal control'], 0)]),
]),
day(113, [
L('Vocabulary: Analogies',
  'Grade 3 Language strand: an analogy compares two pairs of words that share a similar relationship, such as hot is to cold as day is to night.',
  [('What is an analogy?', ['A comparison between two pairs of words with a similar relationship', 'A type of punctuation', 'A rhyming poem', 'A single word'], 0),
   ('Complete the analogy: Puppy is to dog as kitten is to ___.', ['Cat', 'Bird', 'Fish', 'Mouse'], 0),
   ('Complete the analogy: Hot is to cold as day is to ___.', ['Night', 'Sun', 'Morning', 'Bright'], 0),
   ('What relationship does the analogy big is to small as fast is to slow show?', ['Opposites', 'Synonyms', 'Categories', 'Rhymes'], 0),
   ('Complete the analogy: Author is to book as painter is to ___.', ['Painting', 'Pencil', 'Museum', 'Colour'], 0)]),
M('Multiplication: Two-Digit by One-Digit Using the Standard Algorithm',
  'Grade 3 Math strand: students use the standard algorithm to multiply a two-digit number by a one-digit number, regrouping when needed, such as 34 x 3.',
  [('What is 34 x 3?', ['92', '102', '99', '96'], 1),
   ('What is 27 x 4?', ['98', '108', '104', '112'], 2),
   ('What is 46 x 2?', ['82', '88', '92', '96'], 2),
   ('What is 53 x 3?', ['153', '159', '163', '149'], 1),
   ('When multiplying with the standard algorithm, regrouping happens when a product is ___.', ['10 or more', 'Less than 5', 'An odd number', 'Exactly 0'], 0)]),
Sc('Science: Comets and Asteroids — Visitors from Space',
   'Grade 3 Science strand: comets are icy space objects that develop a glowing tail near the sun, while asteroids are rocky objects, and both orbit the sun like planets.',
   [('What is a comet mostly made of?', ['Ice and dust', 'Solid metal only', 'Water alone', 'Living organisms'], 0),
    ('What forms a comets glowing tail?', ['Ice and dust heated by the sun', 'Reflected moonlight only', 'Fire from the comets core', 'Nothing, comets have no tail'], 0),
    ('What is an asteroid mostly made of?', ['Rock and metal', 'Ice only', 'Gas only', 'Water only'], 0),
    ('Do comets and asteroids orbit the sun?', ['Yes', 'No, they float randomly', 'Only comets do', 'Only asteroids do'], 0),
    ('Where are many asteroids found in our solar system?', ['In a belt between Mars and Jupiter', 'Inside the sun', 'On Earths surface', 'Inside the Moon'], 0)]),
SS('Social Studies: The RCMP — Canadas National Police Force',
   'Grade 3 Social Studies strand: the Royal Canadian Mounted Police, or RCMP, is Canadas national police force, known for its red serge uniform and role in federal law enforcement.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is the RCMP known for wearing?', ['A red serge uniform', 'A blue business suit', 'A firefighter helmet', 'A chefs apron'], 0),
    ('What kind of police force is the RCMP?', ['A national police force', 'A single citys local force only', 'A private security company', 'A volunteer club'], 0),
    ('What is one role of the RCMP?', ['Enforcing federal laws', 'Teaching in schools', 'Running restaurants', 'Building bridges'], 0),
    ('Why might a country have a national police force in addition to local police?', ['To handle law enforcement across the whole country', 'National police are not needed', 'Only cities need police', 'It replaces all other laws'], 0)]),
]),
day(114, [
L('Writing: Writing Dialogue Between Characters',
  'Grade 3 Language strand: writing dialogue means creating realistic conversation between characters, using quotation marks and giving each character a distinct voice.',
  [('What punctuation is used to show a character speaking?', ['Quotation marks', 'A colon', 'A semicolon', 'An ellipsis'], 0),
   ('What does it mean to give a character a distinct voice in dialogue?', ['Making their speech sound unique to them', 'Making every character sound the same', 'Removing all punctuation', 'Writing in all capital letters'], 0),
   ('Why do writers use dialogue in a story?', ['To show characters interacting and reveal personality', 'To avoid describing the setting', 'To make the story shorter', 'To remove all characters'], 0),
   ('Which is an example of well-written dialogue?', ['Sam said, I do not want to go.', 'Sam said I do not want to go', 'Sam, said I do not want to go.', 'sam said i do not want to go'], 0),
   ('When a new character starts speaking in dialogue, writers usually ___.', ['Start a new paragraph', 'Use the exact same paragraph', 'Remove punctuation', 'Switch to all capitals'], 0)]),
M('Data: Line Plots',
  'Grade 3 Math strand: a line plot displays data along a number line, using X marks or dots to show how many times each value occurs.',
  [('What does a line plot use to show data?', ['Marks like Xs or dots above a number line', 'Only bars', 'Only pie slices', 'Only colours'], 0),
   ('On a line plot, what does a taller stack of marks above a number mean?', ['That value occurs more often', 'That value occurs less often', 'That value is incorrect', 'That value is the smallest'], 0),
   ('A line plot is especially useful for showing ___.', ['How often each value appears in a data set', 'The exact time of day', 'The colour of an object', 'A map location'], 0),
   ('If three students scored 8 on a quiz, how many marks would appear above 8 on the line plot?', ['2', '3', '4', '8'], 1),
   ('What is the first step in making a line plot?', ['Drawing a number line covering the data range', 'Drawing a pie chart', 'Choosing random colours', 'Skipping the data'], 0)]),
Sc('Science: Fish — Gills, Fins, and Life Underwater',
   'Grade 3 Science strand: fish are adapted for life underwater, using gills to breathe oxygen from water and fins to swim and steer.',
   [('What body part do fish use to breathe underwater?', ['Gills', 'Lungs', 'Nostrils', 'Skin only'], 0),
    ('What do fish use to swim and steer through water?', ['Fins', 'Wings', 'Legs', 'Antennae'], 0),
    ('How do gills help a fish breathe?', ['They take oxygen from the water', 'They take oxygen from the air', 'They filter sunlight', 'They store food'], 0),
    ('Which of these is an adaptation for underwater life?', ['Gills for breathing water', 'Wings for flying', 'Fur for warmth on land', 'Lungs for breathing air only'], 0),
    ('Fish are classified as ___.', ['Aquatic animals', 'Land mammals', 'Insects', 'Birds'], 0)]),
SS('Social Studies: Canadas Justice System — Courts and Judges',
   'Grade 3 Social Studies strand: Canadas justice system uses courts and judges to settle disagreements and decide cases fairly when laws may have been broken.',
   [('Who makes decisions in a courtroom?', ['A judge', 'A mayor', 'A teacher', 'A shopkeeper'], 0),
    ('What is the purpose of Canadas justice system?', ['To settle disagreements and apply laws fairly', 'To sell goods', 'To build roads', 'To teach students'], 0),
    ('Where do court cases usually take place?', ['In a courtroom', 'In a classroom', 'In a grocery store', 'In a park'], 0),
    ('Why is fairness important in a justice system?', ['So everyone is treated equally under the law', 'Fairness does not matter', 'Only some people deserve fairness', 'Judges should favour one side'], 0),
    ('What might a court decide in a case?', ['Whether a law was broken and what happens next', 'What is for lunch', 'The weather forecast', 'A sports score'], 0)]),
]),
day(115, [
L('Reading: Summarizing a Nonfiction Article',
  'Grade 3 Language strand: summarizing a nonfiction article means identifying the main topic and key facts, then retelling them briefly in your own words.',
  [('What is the first step in summarizing a nonfiction article?', ['Identifying the main topic', 'Copying the whole article', 'Ignoring the article', 'Drawing a picture'], 0),
   ('A good summary includes ___.', ['Only the most important facts', 'Every single detail', 'Only the title', 'No information at all'], 0),
   ('Why do we summarize nonfiction articles?', ['To understand and remember the key information quickly', 'To make the article longer', 'To confuse the reader', 'To remove all facts'], 0),
   ('A summary should be written ___.', ['In your own words', 'Word for word from the article', 'Only as a question', 'In a foreign language'], 0),
   ('Which is an example of a nonfiction article topic?', ['How volcanoes form', 'A made-up dragon story', 'A fairy tale', 'A poem about a unicorn'], 0)]),
M('Financial Literacy: Understanding Interest — How Savings Grow',
  'Grade 3 Math strand: interest is extra money a bank may add to savings over time, meaning money left in a savings account can grow larger.',
  [('What is interest?', ['Extra money a bank may add to savings over time', 'Money taken away from your savings', 'A type of coin', 'A punishment for saving'], 0),
   ('If you leave money in a savings account, what might happen to it over time with interest?', ['It can grow larger', 'It always shrinks', 'It disappears', 'It turns into a different currency'], 0),
   ('Why might someone choose to save money in a bank account?', ['To keep it safe and potentially earn interest', 'Banks never help money grow', 'To lose money', 'It has no benefit'], 0),
   ('Interest is usually calculated based on ___.', ['How much money is saved and for how long', 'The colour of the piggy bank', 'The day of the week', 'The customers age'], 0),
   ('Which best describes the idea of savings growing with interest?', ['Small amounts added over time can add up', 'Savings never change', 'Interest removes all your money', 'Interest is the same as a tax'], 0)]),
Sc('Science: Hibernation — How Some Animals Sleep Through Winter',
   'Grade 3 Science strand: hibernation is a deep, long sleep some animals use to survive winter, slowing their heart rate and body functions to save energy when food is scarce.',
   [('What is hibernation?', ['A deep, long sleep some animals use to survive winter', 'A type of summer activity', 'A way animals find food quickly', 'A kind of migration'], 0),
    ('Why do some animals hibernate?', ['To save energy when food is scarce in winter', 'To find more food in winter', 'To grow taller', 'To change colour'], 0),
    ('What happens to an animals heart rate during hibernation?', ['It slows down', 'It speeds up', 'It stops completely', 'It stays exactly the same'], 0),
    ('Name an animal known for hibernating.', ['A bear', 'A robin', 'A shark', 'A butterfly'], 0),
    ('Hibernation mainly helps animals survive a season with ___.', ['Cold weather and little food', 'Warm weather and lots of food', 'No weather changes', 'Constant sunshine'], 0)]),
SS('Social Studies: The Census — Counting Everyone in Canada',
   'Grade 3 Social Studies strand: a census is an official count of everyone living in Canada, helping the government plan services like schools, hospitals, and roads.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('Why does the government conduct a census?', ['To help plan services like schools and hospitals', 'To sell products', 'To have no reason', 'To confuse citizens'], 0),
    ('How often is a census usually taken in Canada?', ['At regular intervals, such as every few years', 'Every single day', 'Only once ever', 'Never'], 0),
    ('Which service might benefit from census information?', ['Planning new schools', 'Painting a fence', 'Selling candy', 'Playing a game'], 0),
    ('A census helps a government understand ___.', ['How many people live in different areas', 'The weather forecast', 'Sports scores', 'Movie ratings'], 0)]),
]),
day(116, [
L('Reading: Symbolism — When an Object Means More Than Itself',
  'Grade 3 Language strand: symbolism is when an author uses an object, colour, or image to represent a deeper idea, such as a dove symbolizing peace.',
  [('What is symbolism?', ['Using an object to represent a deeper idea', 'A type of punctuation', 'A grammar rule', 'A math symbol'], 0),
   ('What does a dove commonly symbolize?', ['Peace', 'Danger', 'Anger', 'Confusion'], 0),
   ('What might a storm symbolize in a story?', ['Trouble or conflict', 'Always literal weather only', 'Happiness', 'Nothing at all'], 0),
   ('Why do authors use symbolism?', ['To add deeper meaning beyond the literal object', 'To confuse readers on purpose', 'To make the story shorter', 'To avoid using words'], 0),
   ('Which is an example of symbolism?', ['A broken mirror representing bad luck', 'A character eating breakfast', 'A character walking to school', 'A character opening a door'], 0)]),
M('Measurement: Perimeter vs Area — What Is the Difference',
  'Grade 3 Math strand: perimeter measures the distance around the outside of a shape, while area measures the amount of space inside it, and the two are calculated differently.',
  [('What does perimeter measure?', ['The distance around a shape', 'The space inside a shape', 'The weight of a shape', 'The colour of a shape'], 0),
   ('What does area measure?', ['The space inside a shape', 'The distance around a shape', 'The height of a shape only', 'The number of corners'], 0),
   ('How do you find the perimeter of a rectangle?', ['Add the lengths of all four sides', 'Multiply length by width', 'Count the corners', 'Measure only one side'], 0),
   ('How do you find the area of a rectangle?', ['Multiply length by width', 'Add all four sides', 'Count the corners', 'Measure the diagonal'], 0),
   ('A rectangle is 4 units by 3 units. What is its area?', ['7', '12', '14', '10'], 1)]),
Sc('Science: Tundra Habitats — Life in the Cold',
   'Grade 3 Science strand: the tundra is a cold, treeless habitat with permanently frozen ground called permafrost, home to hardy plants and animals adapted to the cold.',
   [('What is the tundra?', ['A cold, treeless habitat', 'A hot desert', 'A tropical rainforest', 'An underwater habitat'], 0),
    ('What is permafrost?', ['Permanently frozen ground', 'A type of flower', 'A warm ocean current', 'A kind of cloud'], 0),
    ('Why does the tundra have few or no trees?', ['The cold climate and frozen ground make it hard for trees to grow', 'Trees are not allowed there', 'It is always too hot for trees', 'There is too much rain'], 0),
    ('Which animal might be adapted to live in the tundra?', ['An arctic fox', 'A parrot', 'A crocodile', 'A monkey'], 0),
    ('Tundra animals often have adaptations to help them ___.', ['Stay warm in extreme cold', 'Stay cool in extreme heat', 'Swim in warm oceans', 'Climb tall rainforest trees'], 0)]),
SS('Social Studies: Terry Fox — A Canadian Hero and His Marathon of Hope',
   'Grade 3 Social Studies strand: Terry Fox was a young Canadian who ran partway across Canada to raise money for cancer research, inspiring an annual tradition that continues today.',
   [('What did Terry Fox do to raise money for cancer research?', ['He ran across much of Canada', 'He wrote a book', 'He built a hospital himself', 'He painted a mural'], 0),
    ('What is the name of Terry Foxs journey called?', ['The Marathon of Hope', 'The Race for Life', 'The Cross-Canada Walk', 'The Great Run'], 0),
    ('What continues today in honour of Terry Fox?', ['An annual run raising money for cancer research', 'A national holiday with no purpose', 'A yearly parade with no cause', 'Nothing continues'], 0),
    ('Why is Terry Fox considered a Canadian hero?', ['He showed great courage and inspired others to help a cause', 'He was a famous actor', 'He was a hockey champion', 'He was a prime minister'], 0),
    ('The Terry Fox Run happening in schools across Canada shows ___.', ['Canadians coming together to support a cause', 'A random unrelated tradition', 'A rule with no meaning', 'A one-time-only event'], 0)]),
]),
day(117, [
L('Oral Communication: Preparing and Giving a Short Speech',
  'Grade 3 Language strand: giving a short speech involves choosing a clear topic, organizing ideas with a beginning, middle, and end, and speaking clearly to an audience.',
  [('What is the first step in preparing a speech?', ['Choosing a clear topic', 'Speaking without any plan', 'Skipping practice', 'Reading someone elses speech word for word'], 0),
   ('A well-organized speech usually has ___.', ['A beginning, middle, and end', 'No structure at all', 'Only one sentence', 'Random unrelated facts'], 0),
   ('Why is it important to speak clearly during a speech?', ['So the audience can understand you', 'It does not matter how you speak', 'To confuse the audience', 'To speak as quietly as possible'], 0),
   ('What can help a speaker feel more confident?', ['Practicing the speech beforehand', 'Never practicing at all', 'Reading it for the first time out loud to the audience', 'Ignoring the topic'], 0),
   ('Making eye contact with the audience during a speech helps ___.', ['Engage listeners and show confidence', 'Confuse the audience', 'Make the speech longer', 'Replace the need for words'], 0)]),
M('Number: Rounding to the Nearest 100',
  'Grade 3 Math strand: to round a number to the nearest hundred, look at the tens digit -- if it is 5 or more, round up; if it is less than 5, round down.',
  [('Which digit do you check to round to the nearest hundred?', ['The tens digit', 'The ones digit', 'The hundreds digit', 'The thousands digit'], 0),
   ('Round 348 to the nearest hundred.', ['300', '340', '400', '350'], 2),
   ('Round 152 to the nearest hundred.', ['100', '150', '200', '160'], 2),
   ('Round 275 to the nearest hundred.', ['200', '270', '280', '300'], 3),
   ('If the tens digit is exactly 5, what do you do?', ['Round up', 'Round down', 'Ignore the number', 'Round to zero'], 0)]),
Sc('Science: Lightning and Thunder — Electricity in the Sky',
   'Grade 3 Science strand: lightning is a giant spark of electricity in the sky during a storm, and thunder is the sound caused by the rapid heating of air around the lightning.',
   [('What is lightning?', ['A giant spark of electricity in the sky', 'A type of cloud', 'A kind of wind', 'A form of rain'], 0),
    ('What causes thunder?', ['Rapid heating of air around a lightning bolt', 'Wind blowing through trees', 'Rain hitting the ground', 'Clouds moving quickly'], 0),
    ('During which kind of weather is lightning most common?', ['Thunderstorms', 'Clear sunny days', 'Light snow', 'Calm, windless days'], 0),
    ('Why do we often hear thunder after seeing lightning?', ['Light travels faster than sound', 'Sound travels faster than light', 'They happen at the exact same instant we notice them', 'Thunder happens before lightning'], 0),
    ('What safety advice is often given during a lightning storm?', ['Stay indoors and avoid open areas', 'Stand under a tall tree', 'Go swimming', 'Fly a kite'], 0)]),
SS('Social Studies: Canada Day — Celebrating Our Country',
   'Grade 3 Social Studies strand: Canada Day, celebrated every July 1st, marks the anniversary of Confederation and is celebrated across the country with fireworks, festivals, and community events.',
   [('On what date is Canada Day celebrated?', ['July 1st', 'January 1st', 'December 25th', 'October 31st'], 0),
    ('What does Canada Day commemorate?', ['The anniversary of Confederation', 'A hockey championship', 'A famous explorer landing', 'A harvest festival'], 0),
    ('How do many Canadians celebrate Canada Day?', ['Fireworks, festivals, and community events', 'By staying indoors all day', 'By closing all parks', 'By ignoring the holiday'], 0),
    ('Why might communities host events on Canada Day?', ['To celebrate and build a sense of national pride and unity', 'Events are not allowed on this day', 'To avoid celebrating', 'It has no significance'], 0),
    ('Canada Day is an example of a ___.', ['National holiday', 'Type of currency', 'Kind of landform', 'Sports team'], 0)]),
]),
day(118, [
L('Grammar: Abbreviations and Acronyms',
  'Grade 3 Language strand: an abbreviation is a shortened form of a word, like Dr for Doctor, while an acronym is a word formed from the first letters of a phrase, like NASA.',
  [('What is an abbreviation?', ['A shortened form of a word', 'A full sentence', 'A type of poem', 'A punctuation mark'], 0),
   ('Which of these is an abbreviation?', ['Dr.', 'Doctor', 'Doctoral', 'Doctorate'], 0),
   ('What is an acronym?', ['A word formed from the first letters of a phrase', 'A synonym for a word', 'A type of rhyme', 'A long sentence'], 0),
   ('Which of these is an example of an acronym?', ['NASA', 'Doctor', 'Running', 'Happiness'], 0),
   ('Why do people use abbreviations and acronyms?', ['To save space and time when writing or speaking', 'To make words longer', 'To confuse readers', 'To remove all meaning from words'], 0)]),
M('Patterning: Patterns in a Multiplication Chart',
  'Grade 3 Math strand: a multiplication chart reveals number patterns, such as columns increasing by the same amount and symmetry across the diagonal.',
  [('In a multiplication chart, the numbers in the 2s column increase by ___ each row.', ['2', '3', '4', '5'], 0),
   ('What pattern can you find in the 5s column of a multiplication chart?', ['It increases by 5 each time', 'It stays the same', 'It decreases by 5 each time', 'It has no pattern'], 0),
   ('In a multiplication chart, is 6 x 4 the same as 4 x 6?', ['Yes', 'No', 'Only sometimes', 'Never'], 0),
   ('What do we call the property showing 6 x 4 equals 4 x 6?', ['The commutative property', 'The distributive property', 'The associative property', 'The identity property'], 0),
   ('A multiplication chart can help students ___.', ['Spot patterns and memorize facts', 'Learn to read', 'Measure length', 'Tell time'], 0)]),
Sc('Science: Fossil Fuels — Coal, Oil, and Natural Gas',
   'Grade 3 Science strand: fossil fuels like coal, oil, and natural gas formed underground over millions of years from ancient plants and animals, and are burned for energy.',
   [('Name one type of fossil fuel.', ['Coal', 'Solar power', 'Wind power', 'Water'], 0),
    ('How did fossil fuels form?', ['From ancient plants and animals over millions of years', 'They were made yesterday', 'From plastic', 'From metal'], 0),
    ('What are fossil fuels commonly used for?', ['Producing energy', 'Growing food', 'Making rain', 'Cooling the ocean'], 0),
    ('Where are fossil fuels typically found?', ['Underground', 'Floating in the air', 'On top of clouds', 'In outer space'], 0),
    ('Fossil fuels are different from renewable energy sources like solar and wind because they ___.', ['Take millions of years to form and can run out', 'Never run out', 'Come from the sun directly', 'Are always clean to burn'], 0)]),
SS('Social Studies: Sister Cities — Twin Communities Around the World',
   'Grade 3 Social Studies strand: sister cities are communities in different countries that form a special partnership to share culture, ideas, and friendship.',
   [('What is a sister city?', ['A partner community in another country', 'A city with no people', 'A type of building', 'A kind of holiday'], 0),
    ('Why might two cities become sister cities?', ['To share culture, ideas, and friendship', 'To compete against each other', 'To ignore one another', 'To close their borders'], 0),
    ('What might sister cities share with each other?', ['Cultural events and ideas', 'Nothing at all', 'Only complaints', 'Weather patterns only'], 0),
    ('Is a sister city partnership an example of global friendship?', ['Yes', 'No', 'Only if in the same country', 'It has no purpose'], 0),
    ('Sister city partnerships can help people learn about ___.', ['Other cultures and communities', 'Only their own city', 'Nothing new', 'Weather forecasting'], 0)]),
]),
day(119, [
L('Vocabulary: Shades of Meaning',
  'Grade 3 Language strand: many words have similar meanings but different shades, or intensities, such as the difference between happy, glad, and thrilled.',
  [('What does shades of meaning refer to?', ['Small differences in the intensity of similar words', 'The colour of a word on a page', 'A type of punctuation', 'A grammar rule'], 0),
   ('Which word shows the strongest degree of happiness?', ['Thrilled', 'Content', 'Fine', 'Okay'], 0),
   ('Which word is a milder version of angry?', ['Annoyed', 'Furious', 'Enraged', 'Livid'], 0),
   ('Why do writers choose words with precise shades of meaning?', ['To express ideas more accurately', 'To confuse the reader', 'To make sentences longer without reason', 'To avoid using adjectives'], 0),
   ('Which set of words goes from mildest to strongest?', ['Warm, hot, scorching', 'Scorching, hot, warm', 'Hot, scorching, warm', 'Warm, scorching, hot'], 0)]),
M('Probability: Certain, Likely, Unlikely, and Impossible',
  'Grade 3 Math strand: students describe the chance of an event happening using probability language: certain, likely, unlikely, or impossible.',
  [('If an event will definitely happen, it is described as ___.', ['Certain', 'Impossible', 'Unlikely', 'Random'], 0),
   ('If an event cannot happen at all, it is described as ___.', ['Impossible', 'Certain', 'Likely', 'Guaranteed'], 0),
   ('Rolling a number less than 7 on a standard six-sided die is ___.', ['Certain', 'Impossible', 'Unlikely', 'Random only'], 0),
   ('Rolling a 7 on a standard six-sided die (numbered 1-6) is ___.', ['Impossible', 'Certain', 'Likely', 'Guaranteed'], 0),
   ('If an event has a small chance of happening, it is described as ___.', ['Unlikely', 'Certain', 'Impossible', 'Guaranteed'], 0)]),
Sc('Science: The Human Digestive System — How Our Bodies Use Food',
   'Grade 3 Science strand: the digestive system breaks down the food we eat into nutrients our body can use for energy, starting in the mouth and continuing through the stomach and intestines.',
   [('Where does digestion begin?', ['In the mouth', 'In the stomach', 'In the lungs', 'In the brain'], 0),
    ('What does the digestive system break food down into?', ['Nutrients the body can use', 'Bones', 'Blood cells', 'Muscles'], 0),
    ('After the mouth, where does food travel next in digestion?', ['Toward the stomach', 'Toward the lungs', 'Toward the brain', 'Toward the skin'], 0),
    ('Why does our body need to digest food?', ['To get energy and nutrients from it', 'To make the food disappear', 'To make it heavier', 'For no reason'], 0),
    ('Which body system processes the food we eat?', ['The digestive system', 'The skeletal system', 'The respiratory system', 'The nervous system'], 0)]),
SS('Social Studies: The Commonwealth — Canadas International Connections',
   'Grade 3 Social Studies strand: the Commonwealth is a voluntary association of countries, including Canada, that share historical ties and cooperate on shared goals.',
   [('What is the Commonwealth?', ['A voluntary association of countries with shared historical ties', 'A single country', 'A type of currency', 'A sports league'], 0),
    ('Is Canada a member of the Commonwealth?', ['Yes', 'No', 'Canada left long ago', 'Canada has never joined'], 0),
    ('Why might countries choose to be part of the Commonwealth?', ['To cooperate on shared goals and maintain historical ties', 'They are forced to join', 'It has no purpose', 'To compete militarily'], 0),
    ('What might Commonwealth countries do together?', ['Share ideas and cooperate on common interests', 'Ignore each other completely', 'Refuse to communicate', 'Compete only in secret'], 0),
    ('Being part of an international group like the Commonwealth helps a country ___.', ['Build global connections and cooperation', 'Isolate itself from the world', 'Lose all its own identity', 'Avoid all foreign relationships'], 0)]),
]),
day(120, [
L('Language Review: Pronouns, Genre, and Speaking Skills',
  'Grade 3 Language strand review: students revisit pronoun-antecedent agreement, identifying genre, analogies, writing dialogue, summarizing nonfiction, symbolism, and giving a short speech.',
  [('What does it mean for a pronoun to agree with its antecedent?', ['They match in number (singular or plural)', 'They must rhyme', 'They must be the same length', 'They must start with the same letter'], 0),
   ('What is genre?', ['A category or type of text', 'The title of a book', 'The last page of a book', 'A punctuation mark'], 0),
   ('What punctuation is used to show a character speaking?', ['Quotation marks', 'A colon', 'A semicolon', 'An ellipsis'], 0),
   ('What is symbolism?', ['Using an object to represent a deeper idea', 'A type of punctuation', 'A grammar rule', 'A math symbol'], 0),
   ('A well-organized speech usually has ___.', ['A beginning, middle, and end', 'No structure at all', 'Only one sentence', 'Random unrelated facts'], 0)]),
M('Math Review: Fractions, Division, and Measurement',
  'Grade 3 Math strand review: students revisit equivalent fractions, two-digit division and multiplication, line plots, perimeter vs area, rounding to the nearest 100, and probability language.',
  [('Which fraction is equivalent to 1/2?', ['2/4', '1/4', '3/8', '2/3'], 0),
   ('What is 48 divided by 4?', ['10', '11', '12', '13'], 2),
   ('What does perimeter measure?', ['The distance around a shape', 'The space inside a shape', 'The weight of a shape', 'The colour of a shape'], 0),
   ('Round 348 to the nearest hundred.', ['300', '340', '400', '350'], 2),
   ('If an event will definitely happen, it is described as ___.', ['Certain', 'Impossible', 'Unlikely', 'Random'], 0)]),
Sc('Science Review: Nocturnal Animals, Habitats, and Earth Science',
   'Grade 3 Science strand review: students revisit owls, bats, comets and asteroids, fish adaptations, hibernation, tundra habitats, lightning, fossil fuels, and the digestive system.',
   [('What adaptation helps owls fly without being heard by prey?', ['Silent flight feathers', 'Bright colours', 'Loud wingbeats', 'Long tails'], 0),
    ('What is echolocation?', ['Using sound to locate objects', 'Using light to see', 'Using smell to hunt', 'Using taste to navigate'], 0),
    ('What is permafrost?', ['Permanently frozen ground', 'A type of flower', 'A warm ocean current', 'A kind of cloud'], 0),
    ('What causes thunder?', ['Rapid heating of air around a lightning bolt', 'Wind blowing through trees', 'Rain hitting the ground', 'Clouds moving quickly'], 0),
    ('Where does digestion begin?', ['In the mouth', 'In the stomach', 'In the lungs', 'In the brain'], 0)]),
SS('Social Studies Review: Government, Geography, and Canadian Identity',
   'Grade 3 Social Studies strand review: students revisit the Interior Plains, the monarchy, the RCMP, the justice system, the census, Terry Fox, Canada Day, sister cities, and the Commonwealth.',
   [('What is the Interior Plains region known for?', ['Fertile farmland and grasslands', 'Tall mountains only', 'Tropical rainforest', 'Coral reefs'], 0),
    ('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('What is the name of Terry Foxs journey called?', ['The Marathon of Hope', 'The Race for Life', 'The Cross-Canada Walk', 'The Great Run'], 0),
    ('On what date is Canada Day celebrated?', ['July 1st', 'January 1st', 'December 25th', 'October 31st'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_111_120)
    append_to(3, g3_111_120)
