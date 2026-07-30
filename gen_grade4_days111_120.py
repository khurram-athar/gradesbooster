#!/usr/bin/env python3
"""Grade 4, Days 111-120 -- extends Grade 4 from 110 to 120 days. Modeled
exactly on gen_grade4_days101_110.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-110
topics (see data/grade4.json), which already densely cover nearly the
entire grade 4 curriculum -- essentially all core grammar, figurative
language, vocabulary, reading strategies, and writing forms for Language;
essentially every number-sense/fraction/decimal/geometry/data/financial-
literacy strand plus algebra basics for Math; the full ecosystems/rocks-
and-minerals/light/sound/electricity/forces/simple-machines/structures/
matter/weather/space/energy strand list for Science (notably NOT yet
touching human body systems); and an extensive ancient-civilizations plus
Canadian-geography/government/history list for Social Studies. New
topics: coordinating/subordinating conjunctions, gerunds and infinitives,
appositives, primary/secondary sources, satire, Greek/Latin roots,
website credibility, debate basics, and song lyric writing for Language;
percent, order of operations, LCM/GCF, prime factorization, outliers,
composite-shape area, scale drawings, dividing by a unit fraction, and
composite-prism volume for Math; volcanoes/earthquakes, the skeletal and
muscular systems, the circulatory system, the respiratory system, the
nervous system, density, groundwater/aquifers, owls, and bats for
Science; and the RCMP, the Senate, how a bill becomes a law, NATO,
Canadian inventions, the Official Languages Act, the Franklin Expedition,
Terry Fox, and the census for Social Studies -- none of those exact ideas
appear in Days 1-110. Day 120 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch. No
embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form, matching the rest of Grade 4.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L4 = 'https://tvolearn.com/pages/grade-4-language'
M4 = 'https://tvolearn.com/pages/grade-4-mathematics'
S4 = 'https://tvolearn.com/pages/grade-4-science-and-technology'
SS4 = 'https://tvolearn.com/pages/grade-4-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 4 Language',
    'TVO Learn: Grade 4 Mathematics',
    'TVO Learn: Grade 4 Science and Technology',
    'TVO Learn: Grade 4 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L4, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M4, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S4, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS4, q)


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


g4_111_120 = [
day(111, [
L('Grammar: Coordinating and Subordinating Conjunctions',
  'Grade 4 Language strand: coordinating conjunctions (and, but, or) join equal ideas, while subordinating conjunctions (because, although, since) join a main idea to a dependent one.',
  [('Which is a coordinating conjunction?', ['And', 'Because', 'Although', 'Since'], 0),
   ('Which is a subordinating conjunction?', ['Because', 'And', 'But', 'Or'], 0),
   ('What do coordinating conjunctions join?', ['Two equal ideas', 'Only single words', 'Only questions', 'Nothing at all'], 0),
   ('In the sentence I stayed home because it rained, which word is the subordinating conjunction?', ['Because', 'Stayed', 'Home', 'It'], 0),
   ('Which sentence uses a coordinating conjunction correctly?', ['I like tea and coffee.', 'I like tea because coffee.', 'I like tea although coffee.', 'I like tea since coffee.'], 0)]),
M('Number Sense: Introduction to Percent',
  'Grade 4 Math strand: percent means out of one hundred, and students learn to represent simple percentages such as 50% (half) and 25% (a quarter) using models and fractions.',
  [('What does percent mean?', ['Out of one hundred', 'Out of ten', 'Out of one', 'Out of one thousand'], 0),
   ('What fraction is equal to 50%?', ['1/2', '1/4', '1/10', '1/5'], 0),
   ('What fraction is equal to 25%?', ['1/4', '1/2', '1/5', '3/4'], 0),
   ('If a shape is 100% shaded, how much of it is shaded?', ['All of it', 'None of it', 'Half of it', 'A quarter of it'], 0),
   ('The percent symbol is written as ___.', ['%', '&', '#', '@'], 0)]),
Sc('Science: Volcanoes and Earthquakes — Forces Beneath Earths Surface',
   'Grade 4 Science strand: volcanoes and earthquakes are caused by movement and pressure within the Earth, releasing molten rock or causing the ground to shake.',
   [('What can cause a volcano to erupt?', ['Pressure and molten rock beneath the surface', 'Rain falling from clouds', 'Wind blowing across land', 'Ocean tides'], 0),
    ('What is an earthquake?', ['A shaking of the ground caused by movement beneath the surface', 'A type of storm', 'A kind of flood', 'A slow-moving glacier'], 0),
    ('What is the molten rock that comes out of a volcano called?', ['Lava', 'Ice', 'Sand', 'Steam only'], 0),
    ('Where do many earthquakes and volcanoes occur?', ['Near the edges of tectonic plates', 'Only in the ocean', 'Only in deserts', 'Nowhere on Earth'], 0),
    ('Why do scientists study volcanoes and earthquakes?', ['To understand and help predict these natural events', 'They have no scientific value', 'To cause more of them', 'To ignore the risks'], 0)]),
SS('Social Studies: The RCMP — Canadas National Police Force',
   'Grade 4 Social Studies strand: the Royal Canadian Mounted Police, or RCMP, is Canadas national police force, responsible for enforcing federal laws across the country.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is the RCMPs main responsibility?', ['Enforcing federal laws across Canada', 'Teaching in schools', 'Running restaurants', 'Building bridges'], 0),
    ('What is the RCMP known for wearing?', ['A red serge uniform', 'A blue business suit', 'A firefighter helmet', 'A chefs apron'], 0),
    ('Why does Canada need both local police and a national police force?', ['Different levels of law enforcement handle different responsibilities', 'National police are unnecessary', 'Only cities need police', 'It replaces all city police'], 0),
    ('The RCMP is an example of a service provided at the ___ level of government.', ['Federal', 'Only municipal', 'Only provincial', 'International'], 0)]),
]),
day(112, [
L('Grammar: Gerunds and Infinitives',
  'Grade 4 Language strand: a gerund is a verb form ending in -ing used as a noun (Swimming is fun), and an infinitive is to plus the base verb used as a noun (To swim is fun).',
  [('What is a gerund?', ['A verb form ending in -ing used as a noun', 'A type of adjective', 'A punctuation mark', 'A prefix'], 0),
   ('Which word is a gerund in the sentence Running is great exercise?', ['Running', 'Is', 'Great', 'Exercise'], 0),
   ('What is an infinitive?', ['To plus the base verb used as a noun', 'A verb ending in -ed', 'A type of pronoun', 'A comma rule'], 0),
   ('Which phrase is an infinitive?', ['To swim', 'Swimming', 'Swam', 'Swims'], 0),
   ('Which sentence uses a gerund correctly as the subject?', ['Reading is my favourite hobby.', 'Read is my favourite hobby.', 'To reads is my favourite hobby.', 'Reads is my favourite hobby.'], 0)]),
M('Number Sense: Order of Operations',
  'Grade 4 Math strand: the order of operations tells us the sequence to solve a math expression -- brackets, exponents, multiplication and division, then addition and subtraction.',
  [('What do we solve first in the order of operations?', ['Brackets', 'Addition', 'Subtraction', 'Whatever comes first left to right, always'], 0),
   ('In the order of operations, which comes before addition and subtraction?', ['Multiplication and division', 'Nothing, addition is always first', 'Brackets are solved last', 'Exponents are ignored'], 0),
   ('What is 3 + 4 x 2 using the order of operations?', ['11', '14', '10', '9'], 0),
   ('What is (3 + 4) x 2 using the order of operations?', ['14', '11', '9', '10'], 0),
   ('Why do we follow a consistent order of operations?', ['So everyone gets the same answer to the same expression', 'It does not matter what order we use', 'To make math harder on purpose', 'Order never affects the answer'], 0)]),
Sc('Science: The Human Skeletal and Muscular Systems',
   'Grade 4 Science strand: the skeletal system gives our body structure and protection using bones, while the muscular system works with bones to allow movement.',
   [('What does the skeletal system give our body?', ['Structure and protection', 'Only colour', 'Only taste', 'Only smell'], 0),
    ('What do muscles work with to allow movement?', ['Bones', 'Blood cells only', 'Hair', 'Skin colour'], 0),
    ('Why are bones important for protection?', ['They shield organs like the brain and heart', 'They have no protective role', 'They only help us taste food', 'They stop us from breathing'], 0),
    ('What happens when a muscle contracts?', ['It shortens and can move a bone', 'It disappears', 'It turns into bone', 'It stops working permanently'], 0),
    ('The skeletal and muscular systems work together to allow the body to ___.', ['Move and stay supported', 'Taste food', 'See colours', 'Hear sounds'], 0)]),
SS('Social Studies: The Canadian Senate — The Other House of Parliament',
   'Grade 4 Social Studies strand: the Senate is the second chamber of Canadas Parliament, where appointed senators review and can suggest changes to proposed laws.',
   [('What is the Senate?', ['The second chamber of Canadas Parliament', 'A type of court', 'A city government', 'A sports league'], 0),
    ('How do people typically become senators in Canada?', ['They are appointed', 'They are elected by the public', 'They inherit the position', 'They are chosen by lottery'], 0),
    ('What is one role of the Senate?', ['Reviewing and suggesting changes to proposed laws', 'Running local schools', 'Managing hospitals', 'Selling products'], 0),
    ('Parliament in Canada is made up of the House of Commons and the ___.', ['Senate', 'Supreme Court', 'City Council', 'Cabinet only'], 0),
    ('Why might a country have two chambers reviewing proposed laws?', ['To provide additional review and balance', 'Two chambers serve no purpose', 'To slow down all government forever', 'Only one chamber is ever needed'], 0)]),
]),
day(113, [
L('Grammar: Appositives — Adding Extra Information',
  'Grade 4 Language strand: an appositive is a noun or phrase placed next to another noun to rename or explain it, often set off by commas, such as my dog, a golden retriever, loves to run.',
  [('What is an appositive?', ['A noun or phrase that renames or explains another noun', 'A type of verb', 'A punctuation mark', 'A prefix'], 0),
   ('In my dog, a golden retriever, loves to run, what is the appositive?', ['A golden retriever', 'My dog', 'Loves to run', 'To run'], 0),
   ('How are appositives usually set off in a sentence?', ['With commas', 'With exclamation marks', 'With no punctuation at all', 'With question marks'], 0),
   ('Why do writers use appositives?', ['To add extra detail or explanation about a noun', 'To remove information from a sentence', 'To make sentences shorter', 'To avoid using nouns'], 0),
   ('Which sentence contains an appositive?', ['My teacher, Mrs. Lee, is kind.', 'My teacher is kind.', 'Is my teacher kind?', 'My kind teacher.'], 0)]),
M('Number Sense: Least Common Multiple and Greatest Common Factor',
  'Grade 4 Math strand: the least common multiple (LCM) is the smallest number that is a multiple of two numbers, while the greatest common factor (GCF) is the largest number that divides evenly into both.',
  [('What does LCM stand for?', ['Least common multiple', 'Largest common measure', 'Least counted multiple', 'Longest common multiple'], 0),
   ('What is the LCM of 4 and 6?', ['12', '10', '24', '6'], 0),
   ('What does GCF stand for?', ['Greatest common factor', 'Greatest counted fraction', 'Grouped common factor', 'General common fraction'], 0),
   ('What is the GCF of 8 and 12?', ['4', '2', '8', '24'], 0),
   ('Finding the GCF can help when ___.', ['Simplifying fractions', 'Multiplying decimals', 'Measuring angles', 'Reading a clock'], 0)]),
Sc('Science: The Circulatory System — How Blood Moves Through Our Body',
   'Grade 4 Science strand: the circulatory system uses the heart to pump blood through blood vessels, delivering oxygen and nutrients throughout the body.',
   [('What organ pumps blood through the body?', ['The heart', 'The lungs', 'The stomach', 'The brain'], 0),
    ('What does blood deliver to the body?', ['Oxygen and nutrients', 'Only water', 'Only sound', 'Only light'], 0),
    ('What are the tubes that carry blood through the body called?', ['Blood vessels', 'Bones', 'Muscles', 'Nerves'], 0),
    ('Why is the circulatory system important?', ['It carries oxygen and nutrients to every part of the body', 'It has no important function', 'It only affects the fingers', 'It stops blood from moving'], 0),
    ('The circulatory system works closely with which other system to deliver oxygen?', ['The respiratory system', 'The skeletal system only', 'The digestive system only', 'No other system'], 0)]),
SS('Social Studies: How a Bill Becomes a Law in Canada',
   'Grade 4 Social Studies strand: a proposed law, called a bill, must be debated and approved by the House of Commons and the Senate before receiving royal assent to become law.',
   [('What is a bill?', ['A proposed law', 'A type of currency', 'A court decision', 'A type of tax'], 0),
    ('Which groups must approve a bill before it becomes law?', ['The House of Commons and the Senate', 'Only the mayor', 'Only the public directly', 'No one needs to approve it'], 0),
    ('What is the final step for a bill to become law?', ['Receiving royal assent', 'Being ignored', 'Being erased', 'Being renamed'], 0),
    ('Why does a bill go through multiple steps of review?', ['To ensure it is carefully considered before becoming law', 'Review is not necessary', 'To make the process instant', 'To skip debate entirely'], 0),
    ('A bill is debated in Parliament to ___.', ['Discuss its strengths and weaknesses', 'Immediately reject all bills', 'Avoid making decisions', 'Ignore public interest'], 0)]),
]),
day(114, [
L('Reading: Distinguishing Primary and Secondary Sources',
  'Grade 4 Language strand: a primary source is a firsthand account or original document, like a diary or photograph, while a secondary source, like a textbook, interprets or describes primary sources.',
  [('What is a primary source?', ['A firsthand account or original document', 'A summary written by someone else', 'A textbook only', 'A type of punctuation'], 0),
   ('Which is an example of a primary source?', ['A diary entry written at the time of an event', 'A textbook chapter written later', 'An encyclopedia article', 'A documentary made years later'], 0),
   ('What is a secondary source?', ['A source that interprets or describes primary sources', 'The original document itself', 'A photograph taken during an event', 'A firsthand letter'], 0),
   ('Which is an example of a secondary source?', ['A history textbook', 'An original letter from the 1800s', 'A photograph from the event', 'A diary from that time'], 0),
   ('Why is it useful to know the difference between primary and secondary sources?', ['It helps evaluate the reliability and origin of information', 'It has no research value', 'Sources are always the same', 'It only matters for fiction'], 0)]),
M('Number Sense: Prime Factorization',
  'Grade 4 Math strand: prime factorization means breaking a number down into the prime numbers that multiply together to make it, such as 12 = 2 x 2 x 3.',
  [('What is prime factorization?', ['Breaking a number into the prime numbers that multiply to make it', 'Adding all factors together', 'Rounding a number', 'Dividing by zero'], 0),
   ('What is the prime factorization of 12?', ['2 x 2 x 3', '2 x 6', '3 x 4', '1 x 12'], 0),
   ('What is the prime factorization of 20?', ['2 x 2 x 5', '4 x 5', '2 x 10', '1 x 20'], 0),
   ('A prime number has exactly ___ factors.', ['Two (1 and itself)', 'Three', 'Zero', 'Ten'], 0),
   ('Why might prime factorization be useful?', ['It helps find LCM and GCF of numbers', 'It changes a number into a fraction', 'It rounds numbers automatically', 'It has no mathematical use'], 0)]),
Sc('Science: The Respiratory System — How We Breathe',
   'Grade 4 Science strand: the respiratory system, including the lungs, allows us to breathe in oxygen and breathe out carbon dioxide.',
   [('What organs are central to the respiratory system?', ['The lungs', 'The stomach', 'The bones', 'The skin'], 0),
    ('What gas do we breathe in?', ['Oxygen', 'Carbon dioxide only', 'Nitrogen only', 'Helium'], 0),
    ('What gas do we breathe out?', ['Carbon dioxide', 'Only oxygen', 'Only water', 'Only helium'], 0),
    ('Why do our bodies need oxygen?', ['To help cells produce energy', 'Oxygen has no use in the body', 'To make bones stronger only', 'To help us taste food'], 0),
    ('The respiratory system works with the ___ system to deliver oxygen throughout the body.', ['Circulatory', 'Skeletal', 'Digestive', 'Muscular'], 0)]),
SS('Social Studies: Canadas Role in NATO',
   'Grade 4 Social Studies strand: NATO is an international alliance of countries, including Canada, that agree to support and defend one another for collective security.',
   [('What does NATO stand for?', ['North Atlantic Treaty Organization', 'National Association of Trade Organizations', 'North American Trade Office', 'National Alliance for Territorial Order'], 0),
    ('Is Canada a member of NATO?', ['Yes', 'No', 'Canada withdrew long ago', 'Canada has never joined'], 0),
    ('What is the main purpose of NATO?', ['Collective security and mutual defence among member countries', 'Selling goods internationally', 'Organizing sports competitions', 'Managing world weather'], 0),
    ('What does collective security mean in the context of NATO?', ['Members agree to support each other if one is threatened', 'Each country defends only itself', 'No countries cooperate at all', 'Only one country makes decisions'], 0),
    ('Being part of an international alliance like NATO helps Canada ___.', ['Build cooperative relationships with other countries', 'Isolate itself from the world', 'Avoid all international relationships', 'Lose its own identity'], 0)]),
]),
day(115, [
L('Reading: Understanding Satire',
  'Grade 4 Language strand: satire uses humour, irony, or exaggeration to criticize or poke fun at ideas, people, or society, often to make a point.',
  [('What is satire?', ['Using humour or exaggeration to criticize something', 'A type of punctuation', 'A grammar rule', 'A math term'], 0),
   ('What might a satirical story use to make its point?', ['Humour, irony, or exaggeration', 'Only serious facts', 'Only numbers', 'Complete silence'], 0),
   ('Why do writers use satire?', ['To criticize or comment on society in an entertaining way', 'To avoid making any point', 'To confuse readers with no purpose', 'To remove all humour from writing'], 0),
   ('Which is an example of a satirical idea?', ['A story exaggerating a rule to show how silly it is', 'A textbook definition', 'A weather report', 'A grocery list'], 0),
   ('Satire is closely related to which other literary technique?', ['Irony', 'Rhyme', 'Alliteration', 'Onomatopoeia'], 0)]),
M('Data Management: Identifying Outliers in a Data Set',
  'Grade 4 Math strand: an outlier is a data value that is much higher or lower than the rest of the data, and it can affect measures like the mean.',
  [('What is an outlier?', ['A data value much higher or lower than the rest', 'The most common value', 'The middle value', 'The total of all values'], 0),
   ('In the data set 4, 5, 6, 5, 40, which value is the outlier?', ['40', '4', '5', '6'], 0),
   ('How can an outlier affect the mean of a data set?', ['It can pull the mean higher or lower than expected', 'It has no effect on the mean', 'It always makes the mean exactly zero', 'It removes all other data'], 0),
   ('Why is it important to notice outliers in data?', ['They may indicate an error or something unusual worth investigating', 'Outliers should always be ignored completely', 'Outliers are never meaningful', 'They automatically fix the data'], 0),
   ('Which of these data sets has an obvious outlier?', ['2, 3, 3, 4, 50', '2, 3, 4, 5, 6', '10, 11, 12, 13, 14', '5, 5, 5, 5, 5'], 0)]),
Sc('Science: The Nervous System — How Our Brain Sends Messages',
   'Grade 4 Science strand: the nervous system, controlled by the brain, sends and receives messages throughout the body using nerves, allowing us to think, feel, and react.',
   [('What organ controls the nervous system?', ['The brain', 'The stomach', 'The lungs', 'The skin'], 0),
    ('What do nerves do?', ['Send and receive messages throughout the body', 'Pump blood', 'Digest food', 'Filter air'], 0),
    ('What allows us to react quickly to touching something hot?', ['The nervous system sending fast signals', 'The digestive system', 'The skeletal system alone', 'Nothing, reactions are random'], 0),
    ('The nervous system helps us to ___.', ['Think, feel, and react', 'Only see colours', 'Only taste food', 'Only grow taller'], 0),
    ('Nerves carry messages between the brain and ___.', ['The rest of the body', 'Only the eyes', 'Only the stomach', 'Nowhere else'], 0)]),
SS('Social Studies: Canadian Inventions and Inventors',
   'Grade 4 Social Studies strand: Canadians have contributed many important inventions, including basketball, insulin therapy, and the telephone, shaping science and daily life around the world.',
   [('Which sport was invented by a Canadian?', ['Basketball', 'Soccer', 'Cricket', 'Rugby'], 0),
    ('What is one area where Canadian inventors have made important contributions?', ['Medicine, sports, and technology', 'Nothing significant', 'Only cooking', 'Only fashion'], 0),
    ('Why is it valuable to learn about Canadian inventions?', ['It highlights Canadian contributions to the world', 'Inventions do not matter', 'Only foreign inventions count', 'It has no educational value'], 0),
    ('Canadian inventors have contributed to fields including ___.', ['Medicine and technology', 'Only farming', 'Only weather forecasting', 'Nothing at all'], 0),
    ('Learning about inventors can inspire students to ___.', ['Value creativity and problem-solving', 'Avoid trying new ideas', 'Ignore science and technology', 'Dislike innovation'], 0)]),
]),
day(116, [
L('Vocabulary: Words with Greek and Latin Roots',
  'Grade 4 Language strand: many English words come from Greek and Latin roots, such as tele- (far) in telephone, or aqua (water) in aquarium, helping readers decode unfamiliar words.',
  [('What does the root tele- mean?', ['Far', 'Water', 'Light', 'Sound'], 0),
   ('What does the root aqua mean?', ['Water', 'Fire', 'Earth', 'Air'], 0),
   ('Which word contains the root tele- meaning far?', ['Telephone', 'Table', 'Tent', 'Ten'], 0),
   ('Which word contains the root aqua meaning water?', ['Aquarium', 'Aardvark', 'Apple', 'Airplane'], 0),
   ('Why is learning Greek and Latin roots helpful?', ['It helps decode the meaning of unfamiliar words', 'It makes words impossible to understand', 'It has no effect on vocabulary', 'It only applies to math'], 0)]),
M('Geometry: Area of Composite Shapes',
  'Grade 4 Math strand: a composite shape is made of two or more simple shapes, and its area is found by breaking it into parts, finding each area, then adding them together.',
  [('What is a composite shape?', ['A shape made of two or more simple shapes', 'A shape with no sides', 'A single circle', 'A single triangle only'], 0),
   ('How do you find the area of a composite shape?', ['Break it into simple shapes, find each area, and add them', 'Multiply all the side lengths together', 'Guess the area', 'Measure only one side'], 0),
   ('A composite shape made of a rectangle (area 20) and a triangle (area 6) has a total area of ___.', ['26', '20', '6', '14'], 0),
   ('Why might builders and designers need to calculate composite areas?', ['Real objects are often made of combined shapes', 'Composite areas are never needed', 'All shapes are simple in real life', 'It only applies to circles'], 0),
   ('The first step in solving a composite area problem is to ___.', ['Divide the shape into simpler parts', 'Skip measuring anything', 'Guess the final answer', 'Ignore the shape entirely'], 0)]),
Sc('Science: Density — Why Some Objects Sink While Others Float',
   'Grade 4 Science strand: density describes how much mass is packed into a given volume, and objects denser than water sink while less dense objects float.',
   [('What is density?', ['How much mass is packed into a given volume', 'The colour of an object', 'The temperature of an object', 'The shape of an object'], 0),
    ('What happens to an object that is denser than water?', ['It sinks', 'It floats', 'It disappears', 'It changes colour'], 0),
    ('What happens to an object that is less dense than water?', ['It floats', 'It sinks', 'It disappears', 'It explodes'], 0),
    ('Why does a large ship made of metal float, even though metal is dense?', ['Its overall shape displaces enough water to float', 'Metal always sinks with no exceptions', 'Ships are not made of dense materials', 'Water has no effect on ships'], 0),
    ('Density compares an objects mass to its ___.', ['Volume', 'Colour', 'Temperature', 'Age'], 0)]),
SS('Social Studies: Canadas Official Languages Act — Bilingualism in Canada',
   'Grade 4 Social Studies strand: the Official Languages Act recognizes English and French as Canadas two official languages, guaranteeing services in both languages at the federal level.',
   [('What are Canadas two official languages?', ['English and French', 'English and Spanish', 'French and German', 'English only'], 0),
    ('What does the Official Languages Act guarantee?', ['Federal services in both English and French', 'Services in only one language', 'No language rights at all', 'Services only in provinces'], 0),
    ('Why might a country recognize more than one official language?', ['To reflect the diverse linguistic heritage of its population', 'Languages do not matter to government', 'To confuse citizens on purpose', 'Only one language should ever be used'], 0),
    ('Which province in Canada has a large French-speaking population historically tied to this policy?', ['Quebec', 'British Columbia', 'Alberta', 'Manitoba only'], 0),
    ('Bilingualism in Canada reflects the countrys ___.', ['English and French heritage', 'Single-language history', 'Lack of cultural diversity', 'Rejection of French language rights'], 0)]),
]),
day(117, [
L('Media Literacy: Evaluating Website Credibility',
  'Grade 4 Language strand: evaluating a websites credibility means checking who wrote it, when it was published, and whether the information is supported by evidence before trusting it.',
  [('What should you check to evaluate a websites credibility?', ['Who wrote it and when it was published', 'Only the background colour', 'Only the font style', 'Nothing, all websites are equally reliable'], 0),
   ('Why is it important to check who wrote a website?', ['To judge whether the author is a reliable source', 'The author never matters', 'Authors are always experts', 'It has no effect on trust'], 0),
   ('What is a sign that a website might be less credible?', ['It provides no evidence or sources for its claims', 'It cites clear sources', 'It has a recent publish date', 'It is written by an expert'], 0),
   ('Why might the publish date of a website matter?', ['Information can become outdated over time', 'Dates never matter online', 'Older websites are always more accurate', 'Publish dates are always fake'], 0),
   ('Which is a good habit when researching online?', ['Comparing information across multiple credible sources', 'Trusting the very first result blindly', 'Ignoring all sources', 'Believing everything without checking'], 0)]),
M('Geometry: Scale Drawings and Scale Factor',
  'Grade 4 Math strand: a scale drawing represents a real object at a different size using a scale factor, such as 1 cm representing 1 metre in real life.',
  [('What is a scale drawing?', ['A drawing that represents a real object at a different size', 'A drawing with no measurements', 'A random sketch', 'A drawing without shapes'], 0),
   ('What does a scale factor tell you?', ['The relationship between the drawing size and the real size', 'The colour of the drawing', 'The artists name', 'The type of paper used'], 0),
   ('If a scale is 1 cm = 1 m, what does 5 cm on the drawing represent in real life?', ['5 m', '5 cm', '50 m', '1 m'], 0),
   ('Why do architects use scale drawings?', ['To accurately represent large structures on paper', 'Scale drawings are never used in real life', 'To make buildings smaller in real life', 'To avoid using any measurements'], 0),
   ('A map is an example of a ___.', ['Scale drawing', 'Composite shape', 'Prime number', 'Data table'], 0)]),
Sc('Science: Groundwater and Aquifers',
   'Grade 4 Science strand: groundwater is water that soaks into the ground and collects in layers of rock and soil called aquifers, an important source of fresh water.',
   [('What is groundwater?', ['Water that soaks into the ground and collects underground', 'Water in the ocean only', 'Water in the clouds', 'Water in a swimming pool'], 0),
    ('What is an aquifer?', ['An underground layer of rock or soil that holds water', 'A type of cloud', 'A kind of river', 'A weather instrument'], 0),
    ('Why is groundwater important?', ['It is a major source of fresh water for people', 'It has no importance', 'It only exists in oceans', 'It cannot be used by people'], 0),
    ('How does water typically get into an aquifer?', ['It soaks down through soil and rock', 'It falls directly from space', 'It is pumped in by machines only', 'It never enters an aquifer'], 0),
    ('Protecting groundwater from pollution is important because ___.', ['Many communities rely on it for drinking water', 'Groundwater is never used by people', 'Pollution never affects groundwater', 'Aquifers cannot be polluted'], 0)]),
SS('Social Studies: The Franklin Expedition — Arctic Exploration History',
   'Grade 4 Social Studies strand: the Franklin Expedition was a 19th-century voyage that attempted to navigate the Arctic and became a famous mystery when the ships were lost.',
   [('What was the Franklin Expedition trying to do?', ['Navigate a route through the Arctic', 'Explore the desert', 'Sail across the Pacific', 'Climb a mountain range'], 0),
    ('What happened to the Franklin Expeditions ships?', ['They became lost, creating a historical mystery', 'They arrived successfully with no issues', 'They never left port', 'They were never real ships'], 0),
    ('When did the Franklin Expedition take place?', ['In the 1800s', 'Last year', 'In ancient times', 'It has not happened yet'], 0),
    ('Why do historians and scientists remain interested in the Franklin Expedition?', ['It reveals details about Arctic exploration and history', 'It has no historical significance', 'It is a modern event', 'No evidence of it has ever been found'], 0),
    ('The Franklin Expedition is an example of ___.', ['Historical Arctic exploration', 'A modern space mission', 'A type of Canadian currency', 'A sport played in Canada'], 0)]),
]),
day(118, [
L('Oral Communication: Debate Basics — Presenting and Countering Arguments',
  'Grade 4 Language strand: a debate involves presenting a clear argument with supporting reasons, then respectfully listening and responding to the other sides points.',
  [('What is a key part of presenting an argument in a debate?', ['Supporting it with clear reasons', 'Yelling louder than the other side', 'Ignoring the topic', 'Refusing to speak'], 0),
   ('Why is listening important during a debate?', ['It helps you understand and respond to the other sides points', 'Listening is not necessary', 'You should never consider other viewpoints', 'It has no effect on the debate'], 0),
   ('What does it mean to counter an argument?', ['To respond to it with your own reasoning or evidence', 'To ignore it completely', 'To repeat it exactly', 'To agree immediately with no thought'], 0),
   ('A respectful debate involves ___.', ['Listening and responding calmly', 'Interrupting constantly', 'Insulting the other side', 'Refusing to speak at all'], 0),
   ('Why do students practice debating in school?', ['To build skills in reasoning, listening, and public speaking', 'Debating has no educational value', 'To avoid learning to communicate', 'It only teaches memorization'], 0)]),
M('Fractions: Dividing a Whole Number by a Unit Fraction',
  'Grade 4 Math strand: dividing a whole number by a unit fraction, like 3 divided by 1/2, tells us how many of that fraction fit into the whole number.',
  [('What does 3 divided by 1/2 ask?', ['How many halves fit into 3', 'How many thirds fit into a half', 'How many wholes fit into a half', 'The sum of 3 and 1/2'], 0),
   ('What is 3 divided by 1/2?', ['6', '3', '1.5', '2'], 0),
   ('What is 4 divided by 1/4?', ['16', '4', '1', '8'], 0),
   ('Dividing a whole number by a unit fraction usually gives an answer ___ the original whole number.', ['Larger than', 'Smaller than', 'Equal to', 'Negative compared to'], 0),
   ('Why does dividing by a fraction less than 1 make the number larger?', ['Because you are finding how many smaller pieces fit into the whole', 'Division always makes numbers smaller', 'It is a coincidence with no reason', 'Fractions cannot be divided'], 0)]),
Sc('Science: Owls and Other Birds of Prey — Adaptations for Hunting',
   'Grade 4 Science strand: birds of prey like owls, hawks, and eagles have adaptations such as sharp talons, hooked beaks, and keen eyesight that help them hunt effectively.',
   [('What are birds of prey adapted to do?', ['Hunt effectively', 'Swim underwater only', 'Live only in water', 'Avoid all movement'], 0),
    ('What body part helps birds of prey grab their food?', ['Sharp talons', 'Webbed feet', 'Long tails only', 'Soft fur'], 0),
    ('What kind of beak do birds of prey typically have?', ['A hooked beak for tearing food', 'A flat beak for filtering water', 'No beak at all', 'A beak made of fur'], 0),
    ('Which sense is especially sharp in birds of prey like owls?', ['Eyesight or hearing', 'Taste', 'Smell', 'Touch'], 0),
    ('Adaptations in birds of prey help them ___.', ['Survive by hunting successfully', 'Avoid eating altogether', 'Live only underwater', 'Lose their ability to fly'], 0)]),
SS('Social Studies: Terry Fox — A Canadian Hero and His Marathon of Hope',
   'Grade 4 Social Studies strand: Terry Fox was a young Canadian who ran partway across Canada to raise money for cancer research, inspiring an annual tradition that continues today.',
   [('What did Terry Fox do to raise money for cancer research?', ['He ran across much of Canada', 'He wrote a book', 'He built a hospital himself', 'He painted a mural'], 0),
    ('What is the name of Terry Foxs journey called?', ['The Marathon of Hope', 'The Race for Life', 'The Cross-Canada Walk', 'The Great Run'], 0),
    ('What continues today in honour of Terry Fox?', ['An annual run raising money for cancer research', 'A national holiday with no purpose', 'A yearly parade with no cause', 'Nothing continues'], 0),
    ('Why is Terry Fox considered a Canadian hero?', ['He showed great courage and inspired others to help a cause', 'He was a famous actor', 'He was a hockey champion', 'He was a prime minister'], 0),
    ('The Terry Fox Run happening in schools across Canada shows ___.', ['Canadians coming together to support a cause', 'A random unrelated tradition', 'A rule with no meaning', 'A one-time-only event'], 0)]),
]),
day(119, [
L('Writing: Writing Song Lyrics or a Rap',
  'Grade 4 Language strand: writing song lyrics or a rap involves choosing a topic, using rhythm and rhyme, and organizing ideas into verses and a repeating chorus.',
  [('What are the two repeating structural parts often found in songs?', ['Verses and a chorus', 'Only a title', 'Only a footnote', 'A table of contents'], 0),
   ('What poetic elements are commonly used in song lyrics?', ['Rhythm and rhyme', 'Only silence', 'Only numbers', 'Only punctuation marks'], 0),
   ('What usually stays the same each time it repeats in a song?', ['The chorus', 'The verse', 'The title only', 'The authors name'], 0),
   ('Why might a songwriter choose words carefully for rhythm?', ['To match the beat and flow of the music', 'Rhythm does not matter in songwriting', 'Words are chosen randomly', 'To avoid using any rhyme'], 0),
   ('Which is a first step in writing song lyrics?', ['Choosing a clear topic or feeling to express', 'Skipping all planning', 'Copying another song exactly', 'Avoiding any structure'], 0)]),
M('Measurement: Volume of Composite Rectangular Prisms',
  'Grade 4 Math strand: the volume of a composite shape made of rectangular prisms is found by breaking it into simple prisms, finding each volume, then adding them together.',
  [('How do you find the volume of a composite shape made of rectangular prisms?', ['Break it into prisms, find each volume, and add them', 'Multiply all side lengths of the whole shape at once', 'Guess the volume', 'Measure only the height'], 0),
   ('If two rectangular prisms have volumes of 24 and 10, what is the total composite volume?', ['34', '24', '10', '14'], 0),
   ('What formula finds the volume of a single rectangular prism?', ['Length x width x height', 'Length + width + height', 'Length x width only', 'Height only'], 0),
   ('Why might real objects require composite volume calculations?', ['Many real objects are combinations of simple 3D shapes', 'Real objects are always simple cubes', 'Composite volume is never used practically', 'Volume only applies to 2D shapes'], 0),
   ('The units for volume are typically expressed in ___.', ['Cubic units', 'Square units', 'Linear units only', 'No units at all'], 0)]),
Sc('Science: Bats and Echolocation',
   'Grade 4 Science strand: bats are the only flying mammals, and many species use echolocation, bouncing sound waves off objects, to navigate and find food in the dark.',
   [('What makes bats unique among mammals?', ['They are the only mammals that truly fly', 'They live underwater', 'They have no fur', 'They lay eggs'], 0),
    ('What is echolocation?', ['Using sound waves to locate objects', 'Using light to see', 'Using smell to hunt', 'Using taste to navigate'], 0),
    ('When are most bats active?', ['At night', 'At noon', 'Only in winter', 'Only underwater'], 0),
    ('How do bats use echolocation to find food?', ['They listen for sound bouncing back off insects', 'They smell insects from far away', 'They see insects glow in the dark', 'They taste the air'], 0),
    ('Bats are classified as ___.', ['Mammals', 'Birds', 'Insects', 'Reptiles'], 0)]),
SS('Social Studies: The Census — Counting Everyone in Canada',
   'Grade 4 Social Studies strand: a census is an official count of everyone living in Canada, helping the government plan services like schools, hospitals, and roads.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('Why does the government conduct a census?', ['To help plan services like schools and hospitals', 'To sell products', 'To have no reason', 'To confuse citizens'], 0),
    ('How often is a census usually taken in Canada?', ['At regular intervals, such as every few years', 'Every single day', 'Only once ever', 'Never'], 0),
    ('Which service might benefit from census information?', ['Planning new schools', 'Painting a fence', 'Selling candy', 'Playing a game'], 0),
    ('A census helps a government understand ___.', ['How many people live in different areas', 'The weather forecast', 'Sports scores', 'Movie ratings'], 0)]),
]),
day(120, [
L('Language Review: Grammar, Sources, and Media Literacy',
  'Grade 4 Language strand review: students revisit coordinating and subordinating conjunctions, gerunds and infinitives, appositives, primary and secondary sources, satire, and evaluating website credibility.',
  [('Which is a coordinating conjunction?', ['And', 'Because', 'Although', 'Since'], 0),
   ('What is a gerund?', ['A verb form ending in -ing used as a noun', 'A type of adjective', 'A punctuation mark', 'A prefix'], 0),
   ('What is an appositive?', ['A noun or phrase that renames or explains another noun', 'A type of verb', 'A punctuation mark', 'A prefix'], 0),
   ('What is a primary source?', ['A firsthand account or original document', 'A summary written by someone else', 'A textbook only', 'A type of punctuation'], 0),
   ('What is satire?', ['Using humour or exaggeration to criticize something', 'A type of punctuation', 'A grammar rule', 'A math term'], 0)]),
M('Math Review: Number Sense, Geometry, and Measurement',
  'Grade 4 Math strand review: students revisit percent, order of operations, LCM/GCF, prime factorization, outliers, composite area, scale drawings, and composite volume.',
  [('What does percent mean?', ['Out of one hundred', 'Out of ten', 'Out of one', 'Out of one thousand'], 0),
   ('What is 3 + 4 x 2 using the order of operations?', ['11', '14', '10', '9'], 0),
   ('What is the LCM of 4 and 6?', ['12', '10', '24', '6'], 0),
   ('What is the prime factorization of 12?', ['2 x 2 x 3', '2 x 6', '3 x 4', '1 x 12'], 0),
   ('What is an outlier?', ['A data value much higher or lower than the rest', 'The most common value', 'The middle value', 'The total of all values'], 0)]),
Sc('Science Review: Human Body Systems and Earth Science',
   'Grade 4 Science strand review: students revisit volcanoes and earthquakes, the skeletal and muscular systems, the circulatory system, the respiratory system, the nervous system, and density.',
   [('What organ pumps blood through the body?', ['The heart', 'The lungs', 'The stomach', 'The brain'], 0),
    ('What organs are central to the respiratory system?', ['The lungs', 'The stomach', 'The bones', 'The skin'], 0),
    ('What organ controls the nervous system?', ['The brain', 'The stomach', 'The lungs', 'The skin'], 0),
    ('What is density?', ['How much mass is packed into a given volume', 'The colour of an object', 'The temperature of an object', 'The shape of an object'], 0),
    ('What is an earthquake?', ['A shaking of the ground caused by movement beneath the surface', 'A type of storm', 'A kind of flood', 'A slow-moving glacier'], 0)]),
SS('Social Studies Review: Government, History, and Canadian Identity',
   'Grade 4 Social Studies strand review: students revisit the RCMP, the Senate, how a bill becomes a law, NATO, Canadian inventions, bilingualism, the Franklin Expedition, Terry Fox, and the census.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is the Senate?', ['The second chamber of Canadas Parliament', 'A type of court', 'A city government', 'A sports league'], 0),
    ('What does NATO stand for?', ['North Atlantic Treaty Organization', 'National Association of Trade Organizations', 'North American Trade Office', 'National Alliance for Territorial Order'], 0),
    ('What are Canadas two official languages?', ['English and French', 'English and Spanish', 'French and German', 'English only'], 0),
    ('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_111_120)
    append_to(4, g4_111_120)
