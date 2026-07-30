#!/usr/bin/env python3
"""Grade 3, Days 121-130 -- extends Grade 3 from 120 to 130 days. Modeled
exactly on gen_grade3_days111_120.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-120
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum: complex sentences, personification,
comparing story versions, biography writing, group discussions,
connotation/denotation, sequence text structure, thesaurus use, and
research reports for Language; classifying triangles by angle, 2-digit by
2-digit multiplication, three-digit division, place value beyond 10 000,
frequency tables, improper fractions, protractor use, discounts, and
circles for Math; reptiles, the skeletal system, the respiratory system,
food groups, the muscular system, grasslands/savannas, bees and
pollinators, glaciers/icebergs, and the salmon life cycle for Science; and
the Hudson Bay Lowlands, national symbols, the Prime Minister, the Metis
Nation, statutory holidays, Canadian inventions, the United Nations, the
Royal Canadian Mint, and trading partners for Social Studies -- none of
those exact ideas appear in Days 1-120. Day 130 is a review day across
all four subjects, matching the end-of-batch pattern used in every prior
10-day batch. No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/question/option text;
apostrophes are dropped entirely (e.g. "Canadas" not "Canada's"),
matching the convention established in Days 111-120.
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


g3_121_130 = [
day(121, [
L('Grammar: Complex Sentences and Subordinate Clauses',
  'Grade 3 Language strand: a complex sentence combines an independent clause, which can stand alone, with a subordinate clause, which cannot stand alone and often begins with a word like because, although, or when.',
  [('What is an independent clause?', ['A clause that can stand alone as a complete sentence', 'A clause that always begins with because', 'A single word only', 'A clause with no verb'], 0),
   ('What is a subordinate clause?', ['A clause that cannot stand alone and depends on another clause', 'A clause that is always the shortest part of a sentence', 'A type of punctuation mark', 'A word that rhymes with the subject'], 0),
   ('Which word could begin a subordinate clause?', ['Because', 'Dog', 'Quickly', 'Purple'], 0),
   ('Which sentence is a complex sentence?', ['Because it was raining, we stayed inside.', 'We stayed inside.', 'It was raining.', 'We stayed inside and it rained.'], 0),
   ('A complex sentence combines ___.', ['An independent clause and a subordinate clause', 'Two subordinate clauses only', 'Two nouns', 'A question and an exclamation'], 0)]),
M('Geometry: Classifying Triangles by Angle — Acute, Right, and Obtuse',
  'Grade 3 Math strand: triangles can be classified by their angles as acute (all angles less than 90 degrees), right (one angle exactly 90 degrees), or obtuse (one angle greater than 90 degrees).',
  [('A right triangle has one angle that measures ___.', ['Exactly 90 degrees', 'Less than 90 degrees', 'More than 90 degrees', 'Exactly 180 degrees'], 0),
   ('In an acute triangle, all angles are ___.', ['Less than 90 degrees', 'Exactly 90 degrees', 'Greater than 90 degrees', 'Equal to 180 degrees'], 0),
   ('An obtuse triangle has one angle that is ___.', ['Greater than 90 degrees', 'Less than 90 degrees', 'Exactly 90 degrees', 'Equal to 0 degrees'], 0),
   ('How many right angles can a triangle have at most?', ['1', '2', '3', '0'], 0),
   ('If a triangle has angles of 60, 60, and 60 degrees, it is classified as ___.', ['Acute', 'Right', 'Obtuse', 'Straight'], 0)]),
Sc('Science: Reptiles — Scales, Cold-Blooded Bodies, and Survival',
   'Grade 3 Science strand: reptiles are cold-blooded animals covered in scales that rely on their environment to regulate body temperature, including snakes, turtles, and lizards.',
   [('What covers the body of a reptile?', ['Scales', 'Feathers', 'Fur', 'Smooth wet skin'], 0),
    ('What does it mean that reptiles are cold-blooded?', ['Their body temperature depends on their environment', 'Their blood is always freezing', 'They cannot survive at all', 'They have no blood'], 0),
    ('Which of these is an example of a reptile?', ['A turtle', 'A robin', 'A frog', 'A bat'], 0),
    ('How might a reptile warm up its body on a cool day?', ['By basking in the sun', 'By shivering constantly', 'By swimming in cold water', 'By staying in the shade all day'], 0),
    ('Reptiles are different from amphibians because reptiles ___.', ['Have dry, scaly skin rather than moist skin', 'Always live underwater', 'Have feathers', 'Cannot lay eggs'], 0)]),
SS('Social Studies: Physical Regions of Canada — The Hudson Bay Lowlands',
   'Grade 3 Social Studies strand: the Hudson Bay Lowlands is a flat, marshy physical region of Canada surrounding Hudson Bay, known for wetlands, permafrost, and unique wildlife such as polar bears.',
   [('What physical region surrounds Hudson Bay?', ['The Hudson Bay Lowlands', 'The Rocky Mountains', 'The Canadian Shield', 'The Prairies'], 0),
    ('What kind of landscape is typical of the Hudson Bay Lowlands?', ['Flat and marshy', 'Tall and mountainous', 'Sandy desert', 'Tropical rainforest'], 0),
    ('Which animal is closely associated with the Hudson Bay Lowlands region?', ['The polar bear', 'The camel', 'The kangaroo', 'The parrot'], 0),
    ('What is permafrost, which is common in this region?', ['Permanently frozen ground', 'A type of ocean current', 'A warm wind pattern', 'A type of rock only found in mountains'], 0),
    ('The Hudson Bay Lowlands is one of Canadas ___.', ['Physical regions', 'Provinces', 'Territories only', 'Official languages'], 0)]),
]),
day(122, [
L('Vocabulary: Personification',
  'Grade 3 Language strand: personification is a figure of speech that gives human qualities, such as feelings or actions, to an animal, object, or idea, such as saying the wind whispered through the trees.',
  [('What is personification?', ['Giving human qualities to something that is not human', 'A rhyme scheme in poetry', 'A type of punctuation', 'A synonym for a noun'], 0),
   ('Which sentence uses personification?', ['The sun smiled down on the park.', 'The sun is a star.', 'The sun rose at six oclock.', 'The sun is very hot.'], 0),
   ('Personification often gives objects or animals the ability to ___.', ['Think, feel, or act like a person', 'Change colour instantly', 'Disappear completely', 'Multiply on their own'], 0),
   ('Why do authors use personification?', ['To make writing more vivid and imaginative', 'To make sentences shorter', 'To avoid using adjectives', 'To confuse the reader on purpose'], 0),
   ('Which phrase is an example of personification?', ['The old car groaned as it climbed the hill.', 'The old car is blue.', 'The old car has four wheels.', 'The old car was parked outside.'], 0)]),
M('Multiplication: Introducing 2-Digit by 2-Digit Multiplication',
  'Grade 3 Math strand: multiplying two 2-digit numbers can be done by breaking each number into tens and ones and multiplying the parts before adding the results together.',
  [('To multiply 23 x 12, one strategy is to break 12 into ___.', ['10 and 2', '20 and 1', '6 and 6', '11 and 1'], 0),
   ('What is 23 x 10?', ['230', '233', '23', '2300'], 0),
   ('What is 23 x 2?', ['46', '44', '43', '48'], 0),
   ('Using the break-apart strategy, 23 x 12 equals 23 x 10 plus 23 x 2, which is 230 plus 46, or ___.', ['276', '266', '286', '256'], 0),
   ('Breaking a multiplication problem into smaller, friendlier parts is called the ___.', ['Distributive strategy', 'Rounding strategy', 'Estimating strategy', 'Grouping strategy only for division'], 0)]),
Sc('Science: The Skeletal System — Bones for Support and Protection',
   'Grade 3 Science strand: the skeletal system is made up of bones that give the body structure and support, protect internal organs, and work with muscles to allow movement.',
   [('What is the main job of the skeletal system?', ['To support the body and protect organs', 'To digest food', 'To pump blood', 'To help us breathe'], 0),
    ('Which organ does the skull protect?', ['The brain', 'The stomach', 'The lungs', 'The muscles'], 0),
    ('What protects the heart and lungs inside the chest?', ['The rib cage', 'The skull', 'The spine alone', 'The skin'], 0),
    ('What do bones work together with to allow the body to move?', ['Muscles', 'The digestive system', 'The skin', 'The lungs alone'], 0),
    ('The skeletal system is made up mainly of ___.', ['Bones', 'Blood vessels', 'Nerves', 'Muscles only'], 0)]),
SS('Social Studies: Canadas National Symbols — The Flag and Anthem',
   'Grade 3 Social Studies strand: national symbols like the maple leaf flag and the national anthem O Canada represent shared Canadian identity and are used at ceremonies and celebrations across the country.',
   [('What image appears on the Canadian flag?', ['A maple leaf', 'A star', 'A crown', 'An eagle'], 0),
    ('What is the name of Canadas national anthem?', ['O Canada', 'God Save the King', 'The Maple Song', 'True North'], 0),
    ('Why do countries have national symbols like flags and anthems?', ['To represent shared identity and unity', 'To confuse other countries', 'To replace all laws', 'To decorate buildings only'], 0),
    ('Where might you commonly hear the Canadian national anthem performed?', ['At school assemblies and sporting events', 'Only inside private homes', 'Never in public', 'Only in other countries'], 0),
    ('What colours appear on the Canadian flag?', ['Red and white', 'Blue and green', 'Yellow and black', 'Purple and orange'], 0)]),
]),
day(123, [
L('Reading: Comparing Multiple Versions of the Same Story',
  'Grade 3 Language strand: readers can compare different versions of the same story, such as a book and its film adaptation, by noting similarities and differences in characters, setting, and events.',
  [('When comparing two versions of the same story, what might a reader look for?', ['Similarities and differences in characters, setting, and events', 'Only the page numbers', 'The colour of the cover', 'The name of the printer'], 0),
   ('Which is an example of comparing two versions of a story?', ['Comparing a book to its movie adaptation', 'Reading the same page twice', 'Counting the words in a chapter', 'Looking only at the title'], 0),
   ('A detail that appears in the book but not in the movie is an example of a ___.', ['Difference between the two versions', 'Similarity between the two versions', 'Grammar rule', 'Punctuation mark'], 0),
   ('Why might a movie version of a story leave out some events from the book?', ['To fit the story into a shorter amount of time', 'Movies must always be identical to books', 'Movies cannot show characters speaking', 'It is never allowed to change anything'], 0),
   ('Comparing versions of a story can help readers understand ___.', ['How different choices affect storytelling', 'Only the price of the book', 'The authors home address', 'The exact publication date'], 0)]),
M('Division: Three-Digit by One-Digit Division',
  'Grade 3 Math strand: dividing a three-digit number by a one-digit number can be done by breaking the number into hundreds, tens, and ones and dividing each part, such as 936 divided by 3.',
  [('What is 936 divided by 3?', ['312', '313', '302', '321'], 0),
   ('What is 848 divided by 4?', ['212', '202', '221', '210'], 0),
   ('What is 555 divided by 5?', ['111', '101', '115', '110'], 0),
   ('What is 728 divided by 7?', ['104', '114', '140', '102'], 0),
   ('One strategy for dividing a large number is to break it into ___.', ['Hundreds, tens, and ones', 'Random digits', 'Only even parts', 'Fractions'], 0)]),
Sc('Science: The Respiratory System — How We Breathe',
   'Grade 3 Science strand: the respiratory system brings oxygen into the body and removes carbon dioxide, using the lungs to exchange gases each time we breathe in and out.',
   [('What is the main job of the respiratory system?', ['To bring in oxygen and remove carbon dioxide', 'To digest food', 'To move the body', 'To pump blood'], 0),
    ('Which organs are the main part of the respiratory system?', ['The lungs', 'The stomach', 'The bones', 'The muscles'], 0),
    ('What gas does the body take in when breathing?', ['Oxygen', 'Carbon dioxide only', 'Nitrogen only', 'Helium'], 0),
    ('What gas does the body release when breathing out?', ['Carbon dioxide', 'Oxygen only', 'Hydrogen', 'Water only'], 0),
    ('Air usually enters the body through the ___.', ['Nose or mouth', 'Ears', 'Skin', 'Eyes'], 0)]),
SS('Social Studies: The Role of the Prime Minister',
   'Grade 3 Social Studies strand: the Prime Minister is the leader of the federal government in Canada, responsible for guiding national policy and representing Canada at home and abroad.',
   [('What is the Prime Minister the leader of?', ['The federal government of Canada', 'A single city', 'A school board', 'A sports league'], 0),
    ('What is one responsibility of the Prime Minister?', ['Guiding national policy and decisions', 'Coaching a hockey team', 'Running a local business', 'Teaching in a classroom'], 0),
    ('At which level of government does the Prime Minister serve?', ['Federal', 'Municipal only', 'Provincial only', 'None of these'], 0),
    ('How does the Prime Minister typically represent Canada?', ['By meeting with leaders of other countries', 'By ignoring international events', 'By only working within one city', 'By avoiding all public appearances'], 0),
    ('The Prime Minister works alongside elected representatives to ___.', ['Make decisions for the whole country', 'Make decisions for a single street', 'Run a private company', 'Coach youth sports'], 0)]),
]),
day(124, [
L('Writing: Writing a Biography',
  'Grade 3 Language strand: a biography is a true account of a real persons life written by someone else, organized around key events, achievements, and their importance.',
  [('What is a biography?', ['A true account of a real persons life written by someone else', 'A made-up story about an animal', 'A list of spelling words', 'A type of poem'], 0),
   ('A biography is different from an autobiography because ___.', ['A biography is written by someone other than the subject', 'A biography is always fiction', 'A biography has no facts', 'A biography is written only by children'], 0),
   ('Which detail would likely appear in a biography?', ['Important events and achievements in the persons life', 'A recipe for cookies', 'A weather forecast', 'A made-up dialogue between dragons'], 0),
   ('Why do writers often organize a biography in time order?', ['To show how events in the persons life unfolded', 'To make it harder to understand', 'To avoid mentioning any dates', 'To copy a diary exactly'], 0),
   ('Which of these people could be the subject of a biography?', ['A real scientist who made an important discovery', 'A talking cartoon rabbit', 'A fictional wizard', 'An imaginary planet'], 0)]),
M('Number: Place Value Beyond 10 000',
  'Grade 3 Math strand: numbers greater than 10 000 can be understood using place value, where each digit represents ones, tens, hundreds, thousands, or ten-thousands depending on its position.',
  [('In the number 34 521, what digit is in the ten-thousands place?', ['3', '4', '5', '2'], 0),
   ('In the number 34 521, what digit is in the thousands place?', ['4', '3', '5', '2'], 0),
   ('What is the value of the digit 5 in the number 34 521?', ['500', '5000', '50', '5'], 0),
   ('Which number is greater, 45 678 or 45 687?', ['45 687', '45 678', 'They are equal', 'Cannot be determined'], 0),
   ('How many digits does a number with a ten-thousands place have at minimum?', ['5', '4', '3', '6'], 0)]),
Sc('Science: Food Groups and a Balanced Diet',
   'Grade 3 Science strand: a balanced diet includes a variety of foods from different groups, such as vegetables and fruits, grain products, protein foods, and dairy or alternatives, to keep the body healthy.',
   [('What is a balanced diet?', ['Eating a variety of foods from different food groups', 'Eating only one type of food', 'Eating as much sugar as possible', 'Skipping meals entirely'], 0),
    ('Which of these is an example of a vegetable or fruit?', ['An apple', 'A slice of bread', 'A glass of milk', 'A piece of chicken'], 0),
    ('Why is it important to eat a variety of food groups?', ['Different foods provide different nutrients the body needs', 'All foods provide the exact same nutrients', 'Variety makes food taste worse', 'The body only needs one nutrient'], 0),
    ('Which food group provides calcium for strong bones?', ['Dairy or alternatives', 'Grain products only', 'Sugary snacks', 'Only vegetables'], 0),
    ('A healthy meal often includes foods from ___.', ['Several different food groups', 'Only the dessert group', 'A single food group', 'No food groups at all'], 0)]),
SS('Social Studies: The Metis Nation and Their History',
   'Grade 3 Social Studies strand: the Metis Nation is one of the three recognized Indigenous peoples of Canada, with a distinct culture that developed from the intermarriage of First Nations and European fur traders.',
   [('The Metis Nation is one of how many recognized Indigenous peoples of Canada?', ['Three', 'One', 'Ten', 'Twenty'], 0),
    ('The distinct Metis culture developed historically from the intermarriage of which two groups?', ['First Nations and European fur traders', 'Only European settlers', 'Only Inuit peoples', 'Only recent immigrants'], 0),
    ('What is one way the Metis Nation has a distinct identity?', ['Its own culture, language, and traditions', 'No traditions of any kind', 'An identical culture to all other groups', 'No historical connection to Canada'], 0),
    ('Which of the following is one of Canadas three recognized Indigenous peoples alongside the Metis?', ['First Nations', 'Settlers', 'Immigrants', 'Explorers'], 0),
    ('Learning about the Metis Nation helps students understand ___.', ['An important part of Canadian history and identity', 'A topic unrelated to Canada', 'A fictional story only', 'A single unrelated event'], 0)]),
]),
day(125, [
L('Oral Communication: Participating in a Group Discussion',
  'Grade 3 Language strand: participating effectively in a group discussion involves taking turns speaking, listening to others ideas, and building on what classmates say in a respectful way.',
  [('What is an important skill for participating in a group discussion?', ['Taking turns speaking and listening to others', 'Talking constantly without stopping', 'Ignoring what classmates say', 'Leaving the group before it starts'], 0),
   ('What does it mean to build on someone elses idea in a discussion?', ['Adding a related thought that connects to what was said', 'Repeating the exact same sentence', 'Changing the subject completely', 'Refusing to respond'], 0),
   ('Why is respectful listening important during a group discussion?', ['It helps everyone understand different viewpoints', 'It slows the discussion down for no reason', 'It is not actually necessary', 'It only matters for the teacher'], 0),
   ('Which behaviour shows good discussion skills?', ['Waiting for a turn to speak and staying on topic', 'Interrupting others frequently', 'Talking over classmates', 'Refusing to share any ideas'], 0),
   ('A group discussion works best when everyone ___.', ['Contributes ideas and listens to others', 'Speaks at the same time', 'Stays silent the whole time', 'Only talks about themselves'], 0)]),
M('Data: Creating and Reading a Frequency Table',
  'Grade 3 Math strand: a frequency table organizes data by showing how many times each value or category occurs, making patterns in the data easier to see.',
  [('What does a frequency table show?', ['How many times each value or category occurs', 'Only the largest value', 'Only the smallest value', 'The colour of each item'], 0),
   ('If 5 students chose blue as their favourite colour, what number would appear next to blue in the frequency table?', ['5', '1', '10', '0'], 0),
   ('A frequency table is useful for organizing data because it ___.', ['Makes patterns and totals easier to see', 'Hides the data completely', 'Removes all numbers', 'Only works with one item'], 0),
   ('What is usually listed in the first column of a frequency table?', ['The categories or values being counted', 'Random numbers', 'The date only', 'The teachers name'], 0),
   ('After collecting data, what is often the next step before making a frequency table?', ['Tallying or counting the results', 'Throwing away the data', 'Guessing the results', 'Skipping the count'], 0)]),
Sc('Science: The Muscular System — Muscles That Move Our Bodies',
   'Grade 3 Science strand: the muscular system is made up of muscles that contract and relax to move the bones of the skeleton, allowing the body to walk, run, and perform other movements.',
   [('What does the muscular system help the body do?', ['Move', 'Digest food', 'Breathe only', 'See'], 0),
    ('How do muscles create movement?', ['By contracting and relaxing', 'By growing new bones', 'By producing blood', 'By changing colour'], 0),
    ('What do muscles pull on to move the body?', ['Bones', 'Skin only', 'Blood vessels', 'Nerves alone'], 0),
    ('Which activity relies heavily on the muscular system?', ['Running', 'Sleeping', 'Thinking silently', 'Sitting still with eyes closed'], 0),
    ('The muscular system works closely with which other body system to create movement?', ['The skeletal system', 'The digestive system', 'The respiratory system alone', 'The circulatory system alone'], 0)]),
SS('Social Studies: Statutory Holidays Across Canada',
   'Grade 3 Social Studies strand: statutory holidays are official days off recognized by law, such as Victoria Day and Thanksgiving, and some holidays vary between provinces and territories.',
   [('What is a statutory holiday?', ['An official day off recognized by law', 'A holiday only celebrated by one family', 'A day with no meaning', 'A regular school day'], 0),
    ('Which of these is an example of a Canadian statutory holiday?', ['Thanksgiving', 'A random Tuesday', 'A birthday party', 'A weekend errand'], 0),
    ('Do all provinces and territories in Canada share the exact same statutory holidays?', ['No, some holidays vary by province or territory', 'Yes, every holiday is identical everywhere', 'Canada has no statutory holidays', 'Only one province has holidays'], 0),
    ('Why might a country establish statutory holidays?', ['To recognize important events or give workers time to rest and celebrate', 'To remove all days off', 'To confuse the calendar', 'To replace weekends entirely'], 0),
    ('Which holiday celebrates the arrival of spring and Queen Victorias birthday in Canada?', ['Victoria Day', 'Canada Day', 'Remembrance Day', 'Labour Day'], 0)]),
]),
day(126, [
L('Vocabulary: Connotation and Denotation',
  'Grade 3 Language strand: denotation is the literal, dictionary definition of a word, while connotation is the feeling or association the word carries, such as the difference between the words skinny and slender.',
  [('What is denotation?', ['The literal, dictionary definition of a word', 'The feeling a word gives the reader', 'A type of punctuation', 'A rhyme within a poem'], 0),
   ('What is connotation?', ['The feeling or association a word carries beyond its literal meaning', 'The exact number of letters in a word', 'The part of speech of a word', 'The opposite of a word'], 0),
   ('Which word has a more positive connotation than skinny even though both describe a similar body type?', ['Slender', 'Bony', 'Scrawny', 'Underfed'], 0),
   ('Why might a writer choose a word with a certain connotation?', ['To create a specific feeling or impression in the reader', 'To make the sentence longer', 'To avoid describing anything', 'To confuse the meaning entirely'], 0),
   ('The words house and home have similar denotations, but home often has a connotation of ___.', ['Warmth and comfort', 'Danger', 'Confusion', 'Emptiness'], 0)]),
M('Fractions: Fractions Greater Than One (Improper Fractions)',
  'Grade 3 Math strand: an improper fraction has a numerator greater than or equal to its denominator, representing an amount greater than or equal to one whole, such as 5/4.',
  [('What is an improper fraction?', ['A fraction with a numerator greater than or equal to its denominator', 'A fraction that is always less than one', 'A fraction with a denominator of zero', 'A fraction with no numerator'], 0),
   ('Which of these is an improper fraction?', ['5/4', '1/4', '3/8', '2/5'], 0),
   ('Does 5/4 represent more or less than one whole?', ['More than one whole', 'Less than one whole', 'Exactly zero', 'Exactly one half'], 0),
   ('Which fraction is equal to exactly one whole?', ['4/4', '1/4', '2/4', '3/4'], 0),
   ('An improper fraction can be rewritten as ___.', ['A mixed number', 'A decimal only', 'A negative number', 'An even number'], 0)]),
Sc('Science: Grasslands and Savanna Habitats',
   'Grade 3 Science strand: grasslands and savannas are habitats dominated by grasses with few trees, supporting animals adapted to open spaces such as grazing herds and fast-running predators.',
   [('What is the main type of plant found in a grassland habitat?', ['Grasses', 'Cacti', 'Coral', 'Moss only'], 0),
    ('Why do grassland habitats have few trees?', ['Conditions like rainfall and fires favour grasses over trees', 'Trees are not allowed to grow anywhere on Earth', 'It is always too cold for any plants', 'The soil contains no nutrients at all'], 0),
    ('Which adaptation might help an animal survive on an open grassland?', ['Speed to escape predators in open spaces', 'Gills for breathing underwater', 'Thick fur for arctic cold only', 'Wings for flying underwater'], 0),
    ('A savanna is best described as a ___.', ['Grassy habitat with scattered trees', 'Dense underwater forest', 'Frozen tundra', 'Deep ocean trench'], 0),
    ('Which animal is commonly associated with grassland or savanna habitats?', ['A zebra', 'A polar bear', 'A shark', 'A penguin'], 0)]),
SS('Social Studies: Canadian Inventions That Changed the World',
   'Grade 3 Social Studies strand: Canadians have contributed many important inventions, such as the telephone, insulin, and basketball, that have had a lasting impact on daily life around the world.',
   [('Which of these inventions is credited to a Canadian context?', ['The telephone', 'The wheel', 'The printing press', 'The compass'], 0),
    ('What important medical treatment was discovered by Canadian researchers?', ['Insulin', 'Penicillin', 'Vaccines in general', 'X-rays'], 0),
    ('Which popular sport was invented by a Canadian?', ['Basketball', 'Soccer', 'Tennis', 'Cricket'], 0),
    ('Why is it valuable to learn about Canadian inventions?', ['They show how Canadians have contributed to the world', 'They have no importance', 'They only matter in one city', 'They prove inventions are impossible'], 0),
    ('An invention that changed the world usually ___.', ['Has a lasting impact on how people live', 'Disappears within a day', 'Affects nobody at all', 'Cannot be used more than once'], 0)]),
]),
day(127, [
L('Reading: Text Structure — Sequence and Chronological Order',
  'Grade 3 Language strand: sequence, or chronological order, is a text structure that presents events or steps in the order they happen, often signalled by words like first, next, then, and finally.',
  [('What does sequence text structure show?', ['Events or steps in the order they happen', 'A comparison between two topics', 'A single opinion', 'A list of definitions only'], 0),
   ('Which words often signal sequence in a text?', ['First, next, then, finally', 'Although, however, but', 'Same as, different from', 'Because, therefore, so'], 0),
   ('Which type of text is most likely to use sequence structure?', ['A set of instructions for building a birdhouse', 'A poem about the moon', 'A persuasive letter', 'A dictionary entry'], 0),
   ('Chronological order arranges events based on ___.', ['The order in which they occurred in time', 'Their length', 'Their importance only', 'Their spelling'], 0),
   ('Why is sequence structure useful in a how-to text?', ['It helps readers follow steps in the correct order', 'It hides important steps', 'It makes steps optional', 'It removes the need for steps'], 0)]),
M('Measurement: Measuring Angles with a Protractor',
  'Grade 3 Math strand: a protractor is a tool used to measure the size of an angle in degrees, with the flat edge lined up along one side of the angle and zero on the scale.',
  [('What tool is used to measure the size of an angle?', ['A protractor', 'A ruler', 'A thermometer', 'A scale'], 0),
   ('Angles are measured in units called ___.', ['Degrees', 'Metres', 'Litres', 'Grams'], 0),
   ('When using a protractor, what should line up with zero on the scale?', ['One side of the angle', 'The tip of the pencil', 'The middle of the page', 'The bottom of the ruler'], 0),
   ('A right angle measures exactly ___ degrees.', ['90', '45', '180', '360'], 0),
   ('Why is it useful to know how to measure angles precisely?', ['It helps accurately compare and classify shapes', 'It has no real use', 'It only matters for circles', 'It replaces the need for rulers'], 0)]),
Sc('Science: Bees and Pollinators — Hive Life and Pollination',
   'Grade 3 Science strand: bees are important pollinators that live in organized hives, and as they collect nectar from flowers, they transfer pollen that helps many plants reproduce.',
   [('What is a pollinator?', ['An animal that helps move pollen between flowers', 'An animal that eats only meat', 'A plant that grows underwater', 'A rock formation'], 0),
    ('What do bees collect from flowers?', ['Nectar', 'Sand', 'Water only', 'Bark'], 0),
    ('How do bees help plants reproduce?', ['By transferring pollen from flower to flower', 'By eating the flowers entirely', 'By digging up plant roots', 'By blocking sunlight from plants'], 0),
    ('Where do many bees live together in an organized group?', ['A hive', 'A den', 'A burrow', 'A nest made of sticks only'], 0),
    ('Why are pollinators like bees important to ecosystems?', ['Many plants depend on them to produce seeds and fruit', 'They have no effect on plants', 'They only harm gardens', 'They prevent all plants from growing'], 0)]),
SS('Social Studies: Canada and the United Nations',
   'Grade 3 Social Studies strand: the United Nations is an international organization that countries, including Canada, join to cooperate on issues like peace, human rights, and helping people around the world.',
   [('What is the United Nations?', ['An international organization that countries join to cooperate', 'A single country', 'A type of currency', 'A sports league'], 0),
    ('Is Canada a member of the United Nations?', ['Yes', 'No', 'Canada left long ago', 'Canada has never been invited'], 0),
    ('What is one goal of the United Nations?', ['Promoting peace and human rights around the world', 'Starting conflicts between countries', 'Removing all cooperation between nations', 'Ending international trade'], 0),
    ('Why might countries choose to work together through an organization like the United Nations?', ['To solve problems that affect many countries together', 'It is required with no benefit', 'To avoid helping anyone', 'To compete secretly'], 0),
    ('The United Nations includes members from ___.', ['Many countries around the world', 'Only North America', 'Only Canada', 'Only one continent'], 0)]),
]),
day(128, [
L('Grammar: Using a Thesaurus to Improve Word Choice',
  'Grade 3 Language strand: a thesaurus is a reference tool that lists synonyms for a word, helping writers choose more precise or varied vocabulary in their writing.',
  [('What is a thesaurus?', ['A reference tool that lists synonyms for words', 'A tool for checking spelling only', 'A type of calculator', 'A book of maps'], 0),
   ('Why might a writer use a thesaurus?', ['To find a more precise or interesting word', 'To make their writing shorter', 'To remove all adjectives', 'To find the definition of a word only'], 0),
   ('If a writer looks up the word happy in a thesaurus, what might they find?', ['Synonyms like joyful or delighted', 'The opposite of happy only', 'The spelling of the word', 'A list of rhyming words'], 0),
   ('A thesaurus is different from a dictionary because a thesaurus ___.', ['Focuses on synonyms rather than definitions', 'Only has pictures', 'Has no words at all', 'Only lists numbers'], 0),
   ('Using varied vocabulary from a thesaurus can help writing become ___.', ['More interesting and precise', 'Harder to read on purpose', 'Completely nonsensical', 'Shorter than one sentence'], 0)]),
M('Financial Literacy: Calculating Discounts and Sale Prices',
  'Grade 3 Math strand: a discount lowers the original price of an item, and the sale price can be found by subtracting the discount amount from the original price.',
  [('What does a discount do to the price of an item?', ['Lowers it', 'Raises it', 'Keeps it the same', 'Doubles it'], 0),
   ('If a toy originally costs 20 dollars and has a 5 dollar discount, what is the sale price?', ['15 dollars', '25 dollars', '5 dollars', '20 dollars'], 0),
   ('How do you find the sale price of an item?', ['Subtract the discount from the original price', 'Add the discount to the original price', 'Multiply the price by zero', 'Ignore the discount'], 0),
   ('A store sign that says 3 dollars off means the item costs ___.', ['3 dollars less than the original price', '3 dollars more than the original price', 'Exactly 3 dollars', 'Free'], 0),
   ('Why might a store offer a discount on an item?', ['To encourage customers to buy it', 'To make the item impossible to buy', 'To raise its price permanently', 'To remove it from shelves without selling it'], 0)]),
Sc('Science: How Glaciers and Icebergs Form',
   'Grade 3 Science strand: glaciers are massive, slow-moving bodies of ice formed from compacted snow over many years, and icebergs are large chunks of ice that break off, or calve, from glaciers into the ocean.',
   [('What is a glacier?', ['A massive, slow-moving body of ice', 'A type of cloud', 'A warm ocean current', 'A desert landform'], 0),
    ('How do glaciers form?', ['From snow compacting into ice over many years', 'From lava cooling quickly', 'From sand piling up', 'From rivers freezing overnight only'], 0),
    ('What is an iceberg?', ['A large chunk of ice that has broken off a glacier', 'A type of fish', 'A warm-water current', 'A kind of cloud'], 0),
    ('What is it called when a piece of ice breaks off a glacier?', ['Calving', 'Melting completely', 'Erupting', 'Evaporating'], 0),
    ('Where might you expect to find glaciers on Earth?', ['Cold regions such as near the poles or high mountains', 'Tropical rainforests', 'Deserts', 'Grasslands'], 0)]),
SS('Social Studies: The Royal Canadian Mint — How Coins Are Made',
   'Grade 3 Social Studies strand: the Royal Canadian Mint is the government facility that designs and produces Canadas coins, using metal, machinery, and careful quality checks.',
   [('What does the Royal Canadian Mint produce?', ['Canadas coins', 'Paper money only', 'Postage stamps', 'Passports'], 0),
    ('What material are most coins made from?', ['Metal', 'Wood', 'Plastic only', 'Paper'], 0),
    ('Why might coins go through quality checks at the mint?', ['To make sure they are made correctly and consistently', 'Quality does not matter for coins', 'To make each coin different from the rest', 'To make coins impossible to spend'], 0),
    ('Who typically produces the official currency of a country?', ['A government-run mint', 'A random individual citizen', 'A private toy company', 'No one produces currency'], 0),
    ('Learning how coins are made helps students understand ___.', ['How currency is produced and used in the economy', 'How to grow crops', 'How weather forecasts work', 'How elections are held'], 0)]),
]),
day(129, [
L('Writing: Writing a Research Report',
  'Grade 3 Language strand: a research report presents organized facts about a topic gathered from multiple sources, typically arranged with an introduction, body paragraphs, and a conclusion.',
  [('What is a research report?', ['An organized presentation of facts about a topic', 'A made-up story with characters', 'A single opinion with no facts', 'A list of random words'], 0),
   ('Where do the facts in a research report usually come from?', ['Multiple reliable sources', 'The writers imagination alone', 'A single unreliable rumour', 'Nowhere; facts are optional'], 0),
   ('Which part of a research report usually introduces the topic?', ['The introduction', 'The conclusion', 'The middle of the second paragraph', 'The bibliography only'], 0),
   ('Why is it important to organize a research report into paragraphs?', ['To group related facts and make the report easier to follow', 'To make the report harder to read', 'To hide the main topic', 'To avoid using facts'], 0),
   ('What might a research report include at the end?', ['A conclusion that summarizes the main points', 'A brand new unrelated topic', 'Only a single question', 'A blank page'], 0)]),
M('Geometry: Introducing Circles — Radius and Diameter',
  'Grade 3 Math strand: a circle has a centre point, a radius that measures from the centre to the edge, and a diameter that measures across the circle through the centre and is twice the length of the radius.',
  [('What is the radius of a circle?', ['The distance from the centre to the edge', 'The distance all the way around the circle', 'The distance across the circle through the centre', 'The number of sides a circle has'], 0),
   ('What is the diameter of a circle?', ['The distance across the circle through the centre', 'The distance from the centre to the edge', 'The area inside the circle', 'The number of corners'], 0),
   ('If a circle has a radius of 4 cm, what is its diameter?', ['8 cm', '4 cm', '2 cm', '16 cm'], 0),
   ('The diameter of a circle is always ___ the radius.', ['Twice', 'Half', 'Equal to', 'Three times'], 0),
   ('Every point on the edge of a circle is the same distance from the ___.', ['Centre', 'Diameter', 'Radius line', 'Edge only'], 0)]),
Sc('Science: The Life Cycle of a Salmon',
   'Grade 3 Science strand: a salmon begins life as an egg in freshwater, grows into a young fish, migrates to the ocean to mature, and eventually returns to its home stream to spawn and complete its life cycle.',
   [('Where does a salmons life cycle typically begin?', ['As an egg in freshwater', 'As an adult in the ocean', 'Inside a cocoon', 'On dry land'], 0),
    ('What does a salmon do after growing older, before returning to spawn?', ['Migrates to the ocean to mature', 'Stays in the same spot its entire life', 'Turns into a bird', 'Buries itself in soil'], 0),
    ('What does it mean for a salmon to spawn?', ['To lay or fertilize eggs to reproduce', 'To grow wings', 'To hibernate for winter', 'To change into a different species'], 0),
    ('Where do adult salmon typically return to spawn?', ['Their home freshwater stream', 'A random ocean location', 'A desert', 'A mountain peak'], 0),
    ('The journey of a salmon between freshwater and the ocean over its life is an example of ___.', ['Migration', 'Hibernation', 'Metamorphosis into an insect', 'Photosynthesis'], 0)]),
SS('Social Studies: Canadas Major Trading Partners',
   'Grade 3 Social Studies strand: Canada trades goods and services with countries around the world, and some of its largest trading partners include the United States, China, and countries in Europe.',
   [('What does it mean for two countries to be trading partners?', ['They regularly buy and sell goods and services with each other', 'They never communicate', 'They share the exact same government', 'They compete in the same sports league'], 0),
    ('Which country is one of Canadas largest trading partners?', ['The United States', 'Antarctica', 'A country that does not exist', 'No countries trade with Canada'], 0),
    ('Why is trade important for Canadas economy?', ['It allows Canada to sell its goods and buy products it needs', 'Trade has no effect on the economy', 'It only benefits other countries', 'It prevents any economic growth'], 0),
    ('Which of these might Canada export to other countries?', ['Natural resources like lumber and oil', 'Nothing at all', 'Only used items', 'Only borrowed goods'], 0),
    ('Trading with many different countries helps Canada ___.', ['Access a wider variety of goods and markets', 'Isolate itself completely', 'Avoid all economic activity', 'Stop producing its own goods'], 0)]),
]),
day(130, [
L('Language Review: Complex Sentences, Personification, and Discussion Skills',
  'Grade 3 Language strand review: students revisit complex sentences and subordinate clauses, personification, comparing story versions, writing a biography, group discussion skills, connotation and denotation, sequence text structure, using a thesaurus, and writing a research report.',
  [('What is a subordinate clause?', ['A clause that cannot stand alone and depends on another clause', 'A clause that is always the shortest part of a sentence', 'A type of punctuation mark', 'A word that rhymes with the subject'], 0),
   ('What is personification?', ['Giving human qualities to something that is not human', 'A rhyme scheme in poetry', 'A type of punctuation', 'A synonym for a noun'], 0),
   ('What is a biography?', ['A true account of a real persons life written by someone else', 'A made-up story about an animal', 'A list of spelling words', 'A type of poem'], 0),
   ('What is connotation?', ['The feeling or association a word carries beyond its literal meaning', 'The exact number of letters in a word', 'The part of speech of a word', 'The opposite of a word'], 0),
   ('What is a research report?', ['An organized presentation of facts about a topic', 'A made-up story with characters', 'A single opinion with no facts', 'A list of random words'], 0)]),
M('Math Review: Triangles, Place Value, and Circles',
  'Grade 3 Math strand review: students revisit classifying triangles by angle, 2-digit by 2-digit multiplication, three-digit division, place value beyond 10 000, frequency tables, improper fractions, measuring angles, discounts, and circles.',
  [('A right triangle has one angle that measures ___.', ['Exactly 90 degrees', 'Less than 90 degrees', 'More than 90 degrees', 'Exactly 180 degrees'], 0),
   ('What is an improper fraction?', ['A fraction with a numerator greater than or equal to its denominator', 'A fraction that is always less than one', 'A fraction with a denominator of zero', 'A fraction with no numerator'], 0),
   ('What tool is used to measure the size of an angle?', ['A protractor', 'A ruler', 'A thermometer', 'A scale'], 0),
   ('What does a discount do to the price of an item?', ['Lowers it', 'Raises it', 'Keeps it the same', 'Doubles it'], 0),
   ('What is the diameter of a circle?', ['The distance across the circle through the centre', 'The distance from the centre to the edge', 'The area inside the circle', 'The number of corners'], 0)]),
Sc('Science Review: Body Systems, Reptiles, and Habitats',
   'Grade 3 Science strand review: students revisit reptiles, the skeletal system, the respiratory system, food groups, the muscular system, grassland and savanna habitats, bees and pollination, glaciers and icebergs, and the life cycle of a salmon.',
   [('What covers the body of a reptile?', ['Scales', 'Feathers', 'Fur', 'Smooth wet skin'], 0),
    ('What is the main job of the skeletal system?', ['To support the body and protect organs', 'To digest food', 'To pump blood', 'To help us breathe'], 0),
    ('What is the main job of the respiratory system?', ['To bring in oxygen and remove carbon dioxide', 'To digest food', 'To move the body', 'To pump blood'], 0),
    ('What is a balanced diet?', ['Eating a variety of foods from different food groups', 'Eating only one type of food', 'Eating as much sugar as possible', 'Skipping meals entirely'], 0),
    ('What is a pollinator?', ['An animal that helps move pollen between flowers', 'An animal that eats only meat', 'A plant that grows underwater', 'A rock formation'], 0)]),
SS('Social Studies Review: Regions, Symbols, and Government',
   'Grade 3 Social Studies strand review: students revisit the Hudson Bay Lowlands, national symbols, the role of the Prime Minister, the Metis Nation, statutory holidays, Canadian inventions, the United Nations, the Royal Canadian Mint, and Canadas trading partners.',
   [('What physical region surrounds Hudson Bay?', ['The Hudson Bay Lowlands', 'The Rocky Mountains', 'The Canadian Shield', 'The Prairies'], 0),
    ('What image appears on the Canadian flag?', ['A maple leaf', 'A star', 'A crown', 'An eagle'], 0),
    ('What is the Prime Minister the leader of?', ['The federal government of Canada', 'A single city', 'A school board', 'A sports league'], 0),
    ('The Metis Nation is one of how many recognized Indigenous peoples of Canada?', ['Three', 'One', 'Ten', 'Twenty'], 0),
    ('What is a statutory holiday?', ['An official day off recognized by law', 'A holiday only celebrated by one family', 'A day with no meaning', 'A regular school day'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_121_130, seed=20260730)
    append_to(3, g3_121_130)
