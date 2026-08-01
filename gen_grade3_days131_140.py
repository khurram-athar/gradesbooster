#!/usr/bin/env python3
"""Grade 3, Days 131-140 -- extends Grade 3 from 130 to 140 days. Modeled
exactly on gen_grade3_days121_130.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-130
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum, including -- among many other things
-- all eight named physical regions of Canada, three body systems
(skeletal, respiratory, muscular), and most Canadian habitats (tundra,
grassland/savanna, desert, rainforest, coral reef, ocean, freshwater).
New topics for this batch: run-on sentences, etymology, identifying a
central argument, formal email writing, interview skills, collective
nouns, comparing a book to its film adaptation, transition words, and
eyewitness news reports for Language; comparing/ordering numbers to
100 000, composite figures, 3-digit by 1-digit multiplication, checking
division with multiplication, mean/average, converting mixed numbers and
improper fractions, the metric system's kilo/centi/milli prefixes,
setting a savings goal, and circumference for Math; the circulatory
system, the nervous system, the skin, the five senses, mountain/alpine
habitats, predator-prey relationships, earthworms and soil health,
weather versus climate, and the honeybee life cycle for Science; and the
Inuit, early European explorers, the Governor General, how a bill
becomes a law, the Senate and House of Commons, Canadian achievements in
space, land acknowledgements, the Coat of Arms, and Canadian
peacekeeping for Social Studies -- none of those exact ideas appear in
Days 1-130. Day 140 is a review day across all four subjects, matching
the end-of-batch pattern used in every prior 10-day batch. No embedded
ASCII double-quote or straight apostrophe characters are used anywhere
in title/summary/question/option text; apostrophes are dropped entirely
(e.g. "Canadas" not "Canada's"), matching the convention established in
Days 111-130.

Invocation (matches the 121-130 script):
  cd ~/gradesbooster && python3 gen_grade3_days131_140.py
followed by:
  cd ~/gradesbooster && python3 build_json.py --grade 3
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


def _rebalance_answer_positions(days, seed=20260801):
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


g3_131_140 = [
day(131, [
L('Grammar: Correcting Run-on Sentences',
  'Grade 3 Language strand: a run-on sentence joins two or more independent clauses without proper punctuation or a conjunction, and writers fix it by adding a period, a comma with a conjunction, or a semicolon.',
  [('What is a run-on sentence?', ['Two or more independent clauses joined without proper punctuation or a conjunction', 'A sentence that is too short', 'A sentence with no verb', 'A question with no answer'], 0),
   ('Which is one way to fix a run-on sentence?', ['Add a period to separate the clauses into two sentences', 'Remove all punctuation', 'Add more independent clauses', 'Delete the subject'], 0),
   ('Which sentence is a run-on?', ['I like dogs I like cats too', 'I like dogs, and I like cats too.', 'I like dogs.', 'I like cats.'], 0),
   ('Adding a comma and a conjunction like and can fix a run-on by ___.', ['Joining the clauses correctly', 'Removing one of the clauses', 'Making the sentence longer only', 'Deleting the verb'], 0),
   ('Why is it important to fix run-on sentences?', ['To make writing clear and easy to understand', 'To make writing harder to read', 'To remove all punctuation', 'To shorten every sentence'], 0)]),
M('Number: Comparing and Ordering Numbers to 100 000',
  'Grade 3 Math strand: students compare and order whole numbers up to 100 000 using place value, looking first at the digit with the greatest place value to decide which number is larger.',
  [('When comparing two large numbers, which digit should you look at first?', ['The digit with the greatest place value', 'The digit with the smallest place value', 'The last digit only', 'Any digit chosen at random'], 0),
   ('Which number is greater: 45 000 or 54 000?', ['54 000', '45 000', 'They are equal', 'Cannot be determined'], 0),
   ('Which number is smallest: 12 000, 21 000, or 1 200?', ['1 200', '12 000', '21 000', 'They are all equal'], 0),
   ('What symbol means greater than?', ['>', '<', '=', '%'], 0),
   ('Ordering numbers from least to greatest means arranging them ___.', ['Starting with the smallest and ending with the largest', 'Starting with the largest and ending with the smallest', 'In alphabetical order', 'Randomly'], 0)]),
Sc('Science: The Circulatory System — Heart and Blood Vessels',
   'Grade 3 Science strand: the circulatory system includes the heart, which pumps blood, and blood vessels, which carry blood carrying oxygen and nutrients throughout the body.',
   [('What is the main job of the heart?', ['To pump blood throughout the body', 'To digest food', 'To help us breathe', 'To help us think'], 0),
    ('What do blood vessels do?', ['Carry blood throughout the body', 'Digest food', 'Protect the brain', 'Filter air'], 0),
    ('What does blood carry to the bodys cells?', ['Oxygen and nutrients', 'Sound waves', 'Light', 'Electricity only'], 0),
    ('The heart, blood, and blood vessels together make up the ___.', ['Circulatory system', 'Digestive system', 'Respiratory system', 'Skeletal system'], 0),
    ('Why is the circulatory system important?', ['It delivers oxygen and nutrients cells need to survive', 'It has no real function', 'It only affects the skin', 'It controls hearing only'], 0)]),
SS('Social Studies: The Inuit — Culture and Life in the Arctic',
   'Grade 3 Social Studies strand: the Inuit are one of the three recognized groups of Indigenous peoples in Canada, traditionally living in the Arctic regions and developing skills and knowledge suited to a cold environment.',
   [('The Inuit are one of how many recognized groups of Indigenous peoples in Canada?', ['Three', 'One', 'Ten', 'Twenty'], 0),
    ('Where have the Inuit traditionally lived?', ['The Arctic regions of Canada', 'The Prairies', 'The Rocky Mountains', 'Southern Ontario only'], 0),
    ('Why did the Inuit develop specialized skills and knowledge?', ['To survive and thrive in a cold Arctic environment', 'To farm in a hot desert', 'To sail across the ocean only', 'To build cities quickly'], 0),
    ('Which region of Canada is closely associated with Inuit communities?', ['The Arctic', 'The St. Lawrence Lowlands', 'The Prairies', 'The Rocky Mountains'], 0),
    ('Learning about Inuit culture helps students understand ___.', ['The diversity of Indigenous peoples in Canada', 'That all Indigenous peoples are identical', 'That Canada has only one culture', 'That the Arctic is uninhabited'], 0)]),
]),
day(132, [
L('Vocabulary: Etymology — Where Words Come From',
  'Grade 3 Language strand: etymology is the study of where words come from and how their meanings have changed over time, and many English words have roots in other languages such as Latin, Greek, or French.',
  [('What is etymology?', ['The study of where words come from and how they have changed', 'The study of punctuation marks', 'The study of handwriting', 'The study of grammar rules only'], 0),
   ('Many English words have roots in which languages?', ['Latin, Greek, and French, among others', 'Only English itself', 'Only made-up languages', 'No other languages'], 0),
   ('Why might learning etymology help a reader?', ['It can help them understand the meaning of unfamiliar words', 'It makes reading impossible', 'It removes the need for a dictionary entirely', 'It only helps with spelling tests'], 0),
   ('The word telephone comes from Greek roots meaning far and sound. This shows that word origins can reveal ___.', ['A words meaning', 'A words punctuation', 'A words capitalization', 'A words font'], 0),
   ('Studying word origins is one strategy for ___.', ['Building vocabulary and understanding new words', 'Avoiding all reading', 'Ignoring word meanings', 'Removing words from a sentence'], 0)]),
M('Geometry: Combining Shapes to Make Composite Figures',
  'Grade 3 Math strand: a composite figure is made by combining two or more simple 2D shapes, such as a square and a triangle joined together to form a house shape.',
  [('What is a composite figure?', ['A shape made by combining two or more simple shapes', 'A shape with only one side', 'A shape that has no corners', 'A perfectly round shape'], 0),
   ('Which two shapes could combine to make a house shape?', ['A square and a triangle', 'A circle and a line', 'Two circles', 'A single triangle'], 0),
   ('Why might it help to break a composite figure into simple shapes?', ['To find its area or perimeter more easily', 'To make the shape disappear', 'To avoid using a ruler', 'To make it a 3D shape'], 0),
   ('A composite figure could be made from ___.', ['Two or more simple 2D shapes joined together', 'Only one point', 'A single straight line', 'Nothing at all'], 0),
   ('Which is an example of a composite figure?', ['A shape made of a rectangle and a semicircle joined together', 'A single dot', 'A straight line segment', 'A single point on a grid'], 0)]),
Sc('Science: The Nervous System — Brain, Spinal Cord, and Nerves',
   'Grade 3 Science strand: the nervous system includes the brain, spinal cord, and nerves, and it controls the body by sending and receiving messages throughout the body.',
   [('What organ controls most of the nervous system?', ['The brain', 'The stomach', 'The lungs', 'The skin'], 0),
    ('What connects the brain to nerves throughout the body?', ['The spinal cord', 'The stomach', 'The lungs', 'The bloodstream only'], 0),
    ('What is the main job of the nervous system?', ['To send and receive messages throughout the body', 'To digest food', 'To pump blood', 'To filter air only'], 0),
    ('What do nerves carry?', ['Messages, or signals, to and from the brain', 'Food to the stomach', 'Air to the lungs', 'Blood to the heart'], 0),
    ('The brain, spinal cord, and nerves together make up the ___.', ['Nervous system', 'Digestive system', 'Circulatory system', 'Skeletal system'], 0)]),
SS('Social Studies: Early European Explorers in Canada',
   'Grade 3 Social Studies strand: early European explorers travelled to what is now Canada searching for new trade routes and resources, meeting and interacting with Indigenous peoples who already lived on the land.',
   [('Why did early European explorers travel to what is now Canada?', ['Searching for new trade routes and resources', 'To avoid all contact with people', 'To build cities that already existed', 'By complete accident with no purpose'], 0),
    ('Who did early European explorers meet when they arrived in Canada?', ['Indigenous peoples who already lived on the land', 'No one at all', 'Only other explorers', 'Animals but no people'], 0),
    ('What might explorers have been searching for on their journeys?', ['New trade routes and resources', 'Nothing of value', 'A way to avoid the ocean', 'A way to avoid trade'], 0),
    ('Exploring new lands often led to ___.', ['Contact and trade between explorers and Indigenous peoples', 'No change at all', 'The disappearance of all maps', 'The end of travel'], 0),
    ('Why do we study early exploration in social studies?', ['To understand how early contact shaped Canadas history', 'Because it has no importance', 'To memorize ship names only', 'To avoid learning about Indigenous peoples'], 0)]),
]),
day(133, [
L('Reading: Identifying the Central Argument in Persuasive Text',
  'Grade 3 Language strand: the central argument of a persuasive text is the main claim the writer wants readers to believe or act on, supported by reasons and evidence throughout the text.',
  [('What is the central argument of a persuasive text?', ['The main claim the writer wants readers to believe or act on', 'A random fact with no purpose', 'The title of the text only', 'A list of unrelated ideas'], 0),
   ('What usually supports the central argument?', ['Reasons and evidence', 'Random pictures only', 'The page number', 'Nothing at all'], 0),
   ('Where might a writer often state their central argument?', ['Near the beginning of the text', 'Only in a footnote', 'Never in the text', 'Only in the title'], 0),
   ('Why do writers include evidence?', ['To convince readers that their argument is valid', 'To confuse readers on purpose', 'To make the text longer with no purpose', 'To avoid making a point'], 0),
   ('Identifying the central argument helps readers ___.', ['Understand the main point the writer is trying to make', 'Ignore the text completely', 'Skip every sentence', 'Avoid understanding the text'], 0)]),
M('Multiplication: Multiplying 3-Digit Numbers by 1-Digit Numbers',
  'Grade 3 Math strand: students multiply a 3-digit number by a 1-digit number using place value strategies or the standard algorithm, multiplying each place value and regrouping as needed.',
  [('What is 213 x 3?', ['639', '629', '613', '636'], 0),
   ('When multiplying a 3-digit number by a 1-digit number, you multiply ___.', ['Each place value, starting from the ones', 'Only the hundreds digit', 'Only the tens digit', 'The digits in a random order'], 0),
   ('What is 104 x 2?', ['208', '204', '206', '210'], 0),
   ('Why might you need to regroup when multiplying multi-digit numbers?', ['Because a product in one place value may be 10 or more', 'Because regrouping is never needed', 'Because the numbers are too small', 'Because subtraction is required instead'], 0),
   ('What is 312 x 3?', ['936', '926', '916', '933'], 0)]),
Sc('Science: The Skin — Protecting Our Bodies',
   'Grade 3 Science strand: the skin is the largest organ of the body, and it protects the body from germs and injury, helps control body temperature, and allows us to sense touch.',
   [('What is the largest organ of the human body?', ['The skin', 'The heart', 'The stomach', 'The brain'], 0),
    ('What is one job of the skin?', ['Protecting the body from germs and injury', 'Pumping blood', 'Digesting food', 'Producing sound'], 0),
    ('How does skin help control body temperature?', ['By sweating to cool the body down', 'By stopping the heart', 'By producing sound waves', 'By digesting food'], 0),
    ('What sense does skin allow us to experience?', ['Touch', 'Taste', 'Smell', 'Sight'], 0),
    ('Why is skin considered an important organ?', ['It protects the body and helps it sense the world', 'It has no real purpose', 'It only affects hair colour', 'It only affects eye colour'], 0)]),
SS('Social Studies: The Governor General — Representing the Crown in Canada',
   'Grade 3 Social Studies strand: the Governor General represents the King or Queen in Canada, performing ceremonial duties and formally approving laws passed by Parliament.',
   [('Who does the Governor General represent in Canada?', ['The King or Queen', 'The mayor of Toronto', 'The Prime Minister of another country', 'A local school board'], 0),
    ('What kind of duties does the Governor General often perform?', ['Ceremonial duties', 'Only sports coaching', 'Only cooking duties', 'Only construction duties'], 0),
    ('What does the Governor General formally do with laws passed by Parliament?', ['Approve them', 'Ignore them completely', 'Write all of them alone', 'Delete them'], 0),
    ('The role of Governor General is mostly ___.', ['Ceremonial and representative', 'Focused only on farming', 'Focused only on sports', 'Focused only on cooking'], 0),
    ('Why does Canada have a Governor General?', ['To represent the Crown within Canada', 'To replace the Prime Minister', 'To run local businesses', 'To coach national sports teams'], 0)]),
]),
day(134, [
L('Writing: Writing a Formal Email',
  'Grade 3 Language strand: a formal email includes a clear subject line, a polite greeting, organized body paragraphs, and a courteous closing, and it avoids slang or informal language.',
  [('What should a formal email include at the top?', ['A clear subject line', 'A random drawing', 'No information at all', 'A joke'], 0),
   ('How should a formal email begin?', ['With a polite greeting', 'With no greeting at all', 'With slang', 'With a random number'], 0),
   ('What should a formal email avoid?', ['Slang or informal language', 'Complete sentences', 'A subject line', 'A greeting'], 0),
   ('What should a formal email have at the end?', ['A courteous closing', 'No closing at all', 'A string of emojis only', 'An unrelated topic'], 0),
   ('Why might someone write a formal email instead of texting?', ['To communicate clearly and respectfully in a professional situation', 'To avoid using words', 'To make the message harder to read', 'To use only slang'], 0)]),
M('Division: Checking Answers Using Multiplication',
  'Grade 3 Math strand: division and multiplication are inverse operations, so a division answer can be checked by multiplying the quotient by the divisor to see if it equals the dividend.',
  [('What operation can be used to check a division answer?', ['Multiplication', 'Subtraction only', 'Addition only', 'No operation is needed'], 0),
   ('If 12 divided by 3 = 4, how can you check this answer?', ['Multiply 4 by 3 to see if it equals 12', 'Divide 4 by 3 again', 'Add 4 and 3', 'Subtract 3 from 4'], 0),
   ('Multiplication and division are called ___.', ['Inverse operations', 'Unrelated operations', 'The same operation', 'Impossible operations'], 0),
   ('If 20 divided by 5 = 4, what multiplication fact checks this?', ['4 x 5 = 20', '5 x 5 = 20', '4 x 4 = 20', '20 x 20 = 4'], 0),
   ('Why is it useful to check a division answer?', ['To make sure the answer is correct', 'To make the answer wrong on purpose', 'To avoid using multiplication ever', 'To skip the problem entirely'], 0)]),
Sc('Science: The Five Senses and Sensory Organs',
   'Grade 3 Science strand: humans experience the world through five senses, sight, hearing, smell, taste, and touch, each linked to a specific sensory organ such as the eyes, ears, nose, tongue, and skin.',
   [('Which organ is linked to the sense of sight?', ['The eyes', 'The ears', 'The nose', 'The tongue'], 0),
    ('Which organ is linked to the sense of hearing?', ['The ears', 'The eyes', 'The nose', 'The tongue'], 0),
    ('Which organ is linked to the sense of taste?', ['The tongue', 'The eyes', 'The ears', 'The nose'], 0),
    ('Which organ is linked to the sense of smell?', ['The nose', 'The eyes', 'The ears', 'The tongue'], 0),
    ('How many senses are commonly described in humans?', ['Five', 'Two', 'Three', 'Ten'], 0)]),
SS('Social Studies: How a Bill Becomes a Law in Canada',
   'Grade 3 Social Studies strand: a bill is a proposed law that must be debated and voted on by elected representatives before it can be approved and become an official law.',
   [('What is a bill?', ['A proposed law', 'A type of currency', 'A holiday celebration', 'A type of map'], 0),
    ('What must happen to a bill before it can become a law?', ['It must be debated and voted on by elected representatives', 'It must be ignored completely', 'It must be hidden from the public', 'It must be sold at a store'], 0),
    ('Who votes on whether a bill becomes a law?', ['Elected representatives', 'Only one person', 'No one votes', 'Only students'], 0),
    ('Why is a bill debated before becoming a law?', ['So representatives can discuss and consider its effects', 'To waste time with no purpose', 'To avoid making any decisions', 'To skip the voting process'], 0),
    ('What is the result if a bill is approved through the proper process?', ['It becomes an official law', 'It disappears completely', 'It becomes a coin', 'It becomes a map'], 0)]),
]),
day(135, [
L('Oral Communication: Interviewing Skills — Asking and Answering Questions',
  'Grade 3 Language strand: interviewing involves preparing clear questions in advance, listening carefully to answers, and asking follow-up questions to learn more about a topic.',
  [('What should an interviewer do before an interview?', ['Prepare clear questions in advance', 'Avoid thinking about the topic', 'Refuse to listen to answers', 'Skip planning entirely'], 0),
   ('What is a follow-up question?', ['A question that asks for more detail about a previous answer', 'A question with no connection to the topic', 'The very first question asked', 'A question that ends the interview'], 0),
   ('Why is listening carefully important during an interview?', ['It helps the interviewer understand and respond to the answers', 'It has no benefit at all', 'It only matters for the person being interviewed', 'It slows down the interview with no purpose'], 0),
   ('Which is an example of a good interview question?', ['An open-ended question that invites detail', 'A question with only a yes or no answer every time', 'A question unrelated to the topic', 'No question at all'], 0),
   ('Why do reporters and researchers use interviews?', ['To gather information directly from a person', 'To avoid learning anything new', 'To make up facts', 'To skip research entirely'], 0)]),
M('Data: Calculating the Mean (Average) of a Data Set',
  'Grade 3 Math strand: the mean, or average, of a data set is found by adding all the values together and dividing by the number of values.',
  [('How do you find the mean of a data set?', ['Add all the values and divide by the number of values', 'Multiply all the values together', 'Subtract the smallest value from the largest', 'Count the number of values only'], 0),
   ('What is another word for mean in math?', ['Average', 'Mode', 'Range', 'Median only'], 0),
   ('What is the mean of 2, 4, and 6?', ['4', '3', '5', '6'], 0),
   ('If you have 4 numbers that add up to 20, what is the mean?', ['5', '4', '6', '20'], 0),
   ('The mean helps describe ___.', ['A typical or central value in a data set', 'The exact largest value only', 'The exact smallest value only', 'Nothing useful about the data'], 0)]),
Sc('Science: Mountain and Alpine Habitats',
   'Grade 3 Science strand: mountain and alpine habitats are found at high elevations where temperatures are cold and winds are strong, and the plants and animals that live there have special adaptations to survive.',
   [('What are mountain and alpine habitats known for?', ['High elevations with cold temperatures and strong winds', 'Low elevations with hot, humid weather', 'Being underwater', 'Being completely flat'], 0),
    ('Why do animals in alpine habitats need special adaptations?', ['To survive cold temperatures and strong winds', 'To survive in warm rainforests', 'To survive underwater only', 'They do not need adaptations'], 0),
    ('Which might be an adaptation of an alpine animal?', ['Thick fur to stay warm', 'Gills for breathing underwater', 'Bright colours to attract predators', 'No fur or feathers at all'], 0),
    ('As elevation increases on a mountain, temperature generally ___.', ['Decreases', 'Increases', 'Stays exactly the same', 'Becomes impossible to measure'], 0),
    ('Plants in alpine habitats are often ___.', ['Low-growing to avoid strong winds', 'Extremely tall to catch more wind', 'Found only underwater', 'Unable to survive at all'], 0)]),
SS('Social Studies: The Canadian Senate and House of Commons',
   'Grade 3 Social Studies strand: the Parliament of Canada is made up of the House of Commons, whose members are elected, and the Senate, whose members are appointed, and both review proposed laws.',
   [('What are the two parts of the Parliament of Canada?', ['The House of Commons and the Senate', 'The Mayor and the Council', 'The Army and the Navy', 'The Courts and the Police'], 0),
    ('How do members of the House of Commons get their positions?', ['They are elected', 'They are born into the role', 'They buy their seats', 'They are chosen randomly'], 0),
    ('How do members of the Senate get their positions?', ['They are appointed', 'They are elected only', 'They inherit the role', 'They win a lottery'], 0),
    ('What is one role of both the House of Commons and the Senate?', ['To review proposed laws', 'To coach sports teams', 'To run local restaurants', 'To build roads directly'], 0),
    ('Why might a country have two parts to its parliament?', ['To allow proposed laws to be reviewed more carefully', 'To make government slower with no benefit', 'To avoid making any laws', 'To eliminate elections entirely'], 0)]),
]),
day(136, [
L('Vocabulary: Collective Nouns for Groups of Animals and People',
  'Grade 3 Language strand: a collective noun names a group of people, animals, or things treated as one unit, such as a flock of birds, a herd of cattle, or a team of players.',
  [('What is a collective noun?', ['A noun that names a group treated as one unit', 'A noun that names only one object', 'A verb that describes an action', 'An adjective that describes a noun'], 0),
   ('Which is an example of a collective noun for birds?', ['A flock', 'A herd', 'A pack', 'A school'], 0),
   ('Which is an example of a collective noun for cattle?', ['A herd', 'A flock', 'A pod', 'A swarm'], 0),
   ('Which is an example of a collective noun for players?', ['A team', 'A herd', 'A flock', 'A pack'], 0),
   ('Collective nouns help writers ___.', ['Describe groups with a single precise word', 'Avoid using nouns entirely', 'Confuse readers on purpose', 'Remove all verbs from a sentence'], 0)]),
M('Fractions: Converting Between Mixed Numbers and Improper Fractions',
  'Grade 3 Math strand: a mixed number combines a whole number and a fraction, and it can be converted into an improper fraction where the numerator is greater than or equal to the denominator.',
  [('What is a mixed number?', ['A number that combines a whole number and a fraction', 'A number with only a denominator', 'A number with no fraction at all', 'A number that is always negative'], 0),
   ('What is 1 and 1/2 written as an improper fraction?', ['3/2', '1/2', '2/1', '1/3'], 0),
   ('What is 5/2 written as a mixed number?', ['2 and 1/2', '1 and 1/2', '5 and 1/2', '2 and 2/5'], 0),
   ('In an improper fraction, the numerator is ___.', ['Greater than or equal to the denominator', 'Always zero', 'Always less than the denominator', 'Always negative'], 0),
   ('Why might it be useful to convert between mixed numbers and improper fractions?', ['To make certain calculations, like addition, easier', 'To make fractions disappear', 'To avoid using numbers', 'To make every fraction equal to one'], 0)]),
Sc('Science: Predator and Prey Relationships in Nature',
   'Grade 3 Science strand: a predator is an animal that hunts and eats other animals, while prey is the animal being hunted, and this relationship helps keep ecosystems balanced.',
   [('What is a predator?', ['An animal that hunts and eats other animals', 'An animal that only eats plants', 'A plant that grows in water', 'A rock formation'], 0),
    ('What is prey?', ['An animal that is hunted by a predator', 'An animal that only hunts plants', 'A type of plant', 'A type of rock'], 0),
    ('Which is an example of a predator-prey relationship?', ['A fox hunting a rabbit', 'Two rabbits playing together', 'A tree growing leaves', 'A rock sitting in a field'], 0),
    ('Why are predator-prey relationships important in an ecosystem?', ['They help keep populations of animals balanced', 'They have no effect on an ecosystem', 'They only affect plants', 'They cause all animals to disappear'], 0),
    ('What might happen if all the predators disappeared from an ecosystem?', ['Prey populations could grow too large', 'Nothing would change at all', 'Prey populations would disappear instantly', 'Plants would disappear immediately'], 0)]),
SS('Social Studies: Canadas Achievements in Space Exploration',
   'Grade 3 Social Studies strand: Canada has contributed to space exploration through achievements such as Canadian astronauts travelling to space and the Canadarm robotic arm used on space missions.',
   [('What is the Canadarm?', ['A robotic arm used on space missions', 'A type of Canadian coin', 'A national holiday', 'A style of building'], 0),
    ('What is one way Canada has contributed to space exploration?', ['Sending Canadian astronauts to space', 'Refusing to study space at all', 'Only observing space from the ground', 'Banning space research'], 0),
    ('Why might a country be proud of its contributions to space exploration?', ['It shows the countrys scientific achievements', 'It has no meaning at all', 'It only matters to astronauts', 'It shows a lack of progress'], 0),
    ('What skills might be important for a career as an astronaut?', ['Science, teamwork, and problem-solving skills', 'No skills are needed', 'Only artistic skills', 'Only cooking skills'], 0),
    ('Learning about Canadas role in space exploration shows that ___.', ['Canada has made notable contributions to science and technology', 'Canada has never studied space', 'Space exploration is impossible', 'Only other countries study space'], 0)]),
]),
day(137, [
L('Reading: Comparing a Book and Its Film Adaptation',
  'Grade 3 Language strand: when a book is made into a film, some details are often changed, added, or removed, and comparing the two versions helps readers think about how each medium tells a story differently.',
  [('What is a film adaptation?', ['A movie version of a book', 'A type of comic strip', 'A type of poem', 'A type of textbook'], 0),
   ('What often happens when a book becomes a film?', ['Some details are changed, added, or removed', 'The story is always identical to the book', 'The book disappears completely', 'Nothing about the story is used'], 0),
   ('Why might a filmmaker change details from the book?', ['To fit the story into the time and format of a film', 'To confuse the audience on purpose', 'Because books cannot be understood', 'To remove the story entirely'], 0),
   ('Comparing a book and its film adaptation can help readers ___.', ['Think about how each medium tells a story differently', 'Avoid thinking about the story', 'Forget the book completely', 'Ignore the film completely'], 0),
   ('Which is one way a book and its film adaptation might differ?', ['The ending or certain characters may be changed', 'The title is always exactly the same word for word', 'Every single detail matches perfectly', 'They are always released the same year'], 0)]),
M('Measurement: The Metric System — Kilo, Centi, and Milli Prefixes',
  'Grade 3 Math strand: the metric system uses prefixes like kilo- (1000), centi- (1/100), and milli- (1/1000) attached to base units such as metre, gram, and litre to describe different sizes of measurement.',
  [('What does the prefix kilo- mean?', ['1000', '100', '10', '1/1000'], 0),
   ('What does the prefix centi- mean?', ['1/100', '100', '1000', '1/1000'], 0),
   ('What does the prefix milli- mean?', ['1/1000', '1000', '1/100', '100'], 0),
   ('How many centimetres are in a metre?', ['100', '10', '1000', '1'], 0),
   ('How many grams are in a kilogram?', ['1000', '100', '10', '1'], 0)]),
Sc('Science: Earthworms and Their Role in Healthy Soil',
   'Grade 3 Science strand: earthworms burrow through soil, breaking it up and mixing in nutrients, which helps air and water reach plant roots and keeps soil healthy.',
   [('What do earthworms do as they move through soil?', ['Burrow through it, breaking it up and mixing in nutrients', 'Destroy all plant roots', 'Remove all water from soil', 'Turn soil into rock'], 0),
    ('How do earthworms help plants?', ['By helping air and water reach plant roots', 'By eating all the leaves', 'By blocking sunlight', 'By removing soil completely'], 0),
    ('Why are earthworms considered helpful to soil health?', ['They mix nutrients into the soil as they burrow', 'They remove all nutrients from soil', 'They make soil impossible to use', 'They have no effect on soil'], 0),
    ('What do earthworms eat as they move through soil?', ['Decaying organic matter in the soil', 'Rocks and metal', 'Only sunlight', 'Only water'], 0),
    ('Why might gardeners be happy to find earthworms in their soil?', ['Earthworms help keep the soil healthy for plants', 'Earthworms destroy every garden', 'Earthworms remove all plants', 'Earthworms have no benefit'], 0)]),
SS('Social Studies: Understanding Land Acknowledgements',
   'Grade 3 Social Studies strand: a land acknowledgement is a statement recognizing the Indigenous peoples who traditionally lived on and cared for the land where an event or gathering is taking place.',
   [('What is a land acknowledgement?', ['A statement recognizing the Indigenous peoples connected to a piece of land', 'A type of map legend', 'A type of government tax', 'A type of currency'], 0),
    ('Why might a school or event begin with a land acknowledgement?', ['To recognize and respect the Indigenous peoples connected to that land', 'To ignore the history of the land', 'To sell the land to visitors', 'To replace the national anthem'], 0),
    ('A land acknowledgement often mentions ___.', ['The Indigenous peoples who traditionally lived on the land', 'Only sports teams', 'Only weather patterns', 'Only local businesses'], 0),
    ('What can learning about land acknowledgements help students understand?', ['The history and presence of Indigenous peoples in Canada', 'That Indigenous peoples no longer exist', 'That land has no history', 'That acknowledgements are unnecessary'], 0),
    ('A land acknowledgement is one way communities show ___.', ['Respect for Indigenous peoples and their connection to the land', 'A disregard for history', 'A new way to sell land', 'A replacement for maps'], 0)]),
]),
day(138, [
L('Grammar: Using Transition Words to Link Ideas',
  'Grade 3 Language strand: transition words such as first, next, however, and finally help connect ideas within and between sentences, making writing easier to follow.',
  [('What do transition words help do?', ['Connect ideas within and between sentences', 'Remove all punctuation', 'Make writing harder to follow', 'Delete verbs from a sentence'], 0),
   ('Which is an example of a transition word?', ['However', 'Elephant', 'Purple', 'Jump'], 0),
   ('Which transition word could show a sequence of steps?', ['First', 'However', 'Although', 'But'], 0),
   ('Which transition word could show a contrast between ideas?', ['However', 'First', 'Next', 'Finally'], 0),
   ('Why might a writer use transition words?', ['To make writing clearer and easier to follow', 'To confuse the reader on purpose', 'To remove all ideas from a paragraph', 'To make sentences disconnected'], 0)]),
M('Financial Literacy: Setting and Reaching a Savings Goal',
  'Grade 3 Math strand: a savings goal is a target amount of money someone plans to save by a certain time, and reaching it often involves setting aside a portion of money regularly.',
  [('What is a savings goal?', ['A target amount of money someone plans to save', 'An amount of money that must be spent immediately', 'A type of tax', 'A type of loan'], 0),
   ('How might someone work toward a savings goal?', ['By setting aside a portion of money regularly', 'By spending all their money right away', 'By ignoring their savings completely', 'By borrowing money instead of saving'], 0),
   ('If you save 5 dollars each week, how much will you have after 4 weeks?', ['20 dollars', '9 dollars', '15 dollars', '25 dollars'], 0),
   ('Why might someone set a savings goal?', ['To plan and save for something they want to buy', 'To avoid ever having money', 'To spend more than they earn', 'To ignore their future needs'], 0),
   ('What could help track progress toward a savings goal?', ['Keeping a record of money saved so far', 'Ignoring how much has been saved', 'Spending the savings immediately', 'Forgetting the goal entirely'], 0)]),
Sc('Science: Weather vs Climate — What Is the Difference',
   'Grade 3 Science strand: weather describes the conditions in the atmosphere at a specific time and place, while climate describes the average weather patterns of a region over many years.',
   [('What does weather describe?', ['The conditions in the atmosphere at a specific time and place', 'The average pattern over many years', 'The colour of the sky only', 'The number of clouds forever'], 0),
    ('What does climate describe?', ['The average weather patterns of a region over many years', 'The temperature at one single moment', 'A single days conditions only', 'Nothing related to weather'], 0),
    ('Which is an example of weather?', ['It is raining outside today', 'A region typically has cold winters', 'A region typically has hot summers', 'A region has a dry climate overall'], 0),
    ('Which is an example of climate?', ['A region typically has cold, snowy winters', 'It is sunny right now', 'It is windy this afternoon', 'It rained one hour ago'], 0),
    ('How is climate different from weather?', ['Climate describes long-term patterns, while weather describes short-term conditions', 'They mean exactly the same thing', 'Climate only applies to oceans', 'Weather only applies to mountains'], 0)]),
SS('Social Studies: Canadas Coat of Arms',
   'Grade 3 Social Studies strand: the Coat of Arms is an official symbol of Canada that includes images such as lions, a unicorn, and maple leaves, representing the countrys history and values.',
   [('What is the Coat of Arms?', ['An official symbol of Canada', 'A type of currency', 'A type of holiday', 'A type of map'], 0),
    ('Which images might appear on Canadas Coat of Arms?', ['Lions, a unicorn, and maple leaves', 'Only a soccer ball', 'Only a bicycle', 'Only a computer'], 0),
    ('What does the Coat of Arms represent?', ['Canadas history and values', 'A single citys sports team', 'A private companys logo', 'A foreign countrys flag'], 0),
    ('Where might you see an official symbol like the Coat of Arms used?', ['On government documents and buildings', 'Only on birthday cards', 'Only on food packaging', 'Only on toys'], 0),
    ('Why do countries have official symbols like a coat of arms?', ['To represent their identity and history', 'To confuse visitors', 'To replace their currency', 'To avoid having a flag'], 0)]),
]),
day(139, [
L('Writing: Writing an Eyewitness News Report',
  'Grade 3 Language strand: an eyewitness news report describes an event using details the writer directly observed, answering questions like who, what, where, when, and why to inform readers.',
  [('What is an eyewitness news report?', ['A report that describes an event using details the writer directly observed', 'A made-up story with no facts', 'A poem about nature', 'A list of spelling words'], 0),
   ('Which questions does a news report typically answer?', ['Who, what, where, when, and why', 'Only how much something costs', 'Only what colour something is', 'Only the writers opinion'], 0),
   ('Why is it important for an eyewitness report to be accurate?', ['So readers get a true account of what happened', 'So readers are confused about the event', 'So the report can be ignored', 'So facts can be hidden'], 0),
   ('What might an eyewitness include in their report?', ['Details they personally saw or experienced', 'Details from a story they made up', 'Details about an unrelated event', 'No details at all'], 0),
   ('Why do news reports often start with the most important information?', ['To quickly inform readers of the key facts', 'To hide the key facts until the end', 'To confuse the reader from the start', 'To avoid informing readers at all'], 0)]),
M('Geometry: Circumference — The Distance Around a Circle',
  'Grade 3 Math strand: the circumference of a circle is the distance around its outer edge, similar to how perimeter measures the distance around a polygon.',
  [('What is the circumference of a circle?', ['The distance around its outer edge', 'The distance across the circle through the centre', 'The distance from the centre to the edge', 'The area inside the circle'], 0),
   ('Circumference is similar to which measurement for polygons?', ['Perimeter', 'Area', 'Volume', 'Angle'], 0),
   ('If you walked all the way around a circular track once, you would travel a distance equal to its ___.', ['Circumference', 'Radius', 'Diameter', 'Area'], 0),
   ('Which measurement tool could estimate the circumference of a circle?', ['A piece of string wrapped around the edge, then measured with a ruler', 'A thermometer', 'A scale', 'A clock'], 0),
   ('The circumference measures the distance ___.', ['Around the outside edge of a circle', 'Through the middle of a circle', 'Above a circle', 'Below a circle'], 0)]),
Sc('Science: The Life Cycle of a Honeybee',
   'Grade 3 Science strand: a honeybee begins life as an egg, hatches into a larva, develops into a pupa, and finally emerges as an adult bee, completing a full metamorphosis.',
   [('What is the first stage of a honeybees life cycle?', ['Egg', 'Larva', 'Pupa', 'Adult bee'], 0),
    ('What stage comes after the egg hatches?', ['Larva', 'Pupa', 'Adult bee', 'Egg again'], 0),
    ('What stage comes after the larva?', ['Pupa', 'Egg', 'Adult bee', 'Nothing, it stops growing'], 0),
    ('What is the final stage of a honeybees life cycle?', ['Adult bee', 'Egg', 'Larva', 'Pupa'], 0),
    ('A honeybees life cycle, with distinct egg, larva, pupa, and adult stages, is an example of ___.', ['Complete metamorphosis', 'No change at all', 'Hibernation', 'Migration'], 0)]),
SS('Social Studies: Canadas Role in International Peacekeeping',
   'Grade 3 Social Studies strand: peacekeeping involves sending trained personnel to help maintain peace in areas affected by conflict, and Canada has a long history of contributing to international peacekeeping missions.',
   [('What is peacekeeping?', ['Sending trained personnel to help maintain peace in areas affected by conflict', 'Starting new conflicts between countries', 'Refusing to help other countries', 'Selling weapons to all countries'], 0),
    ('What has Canada contributed to internationally over many years?', ['Peacekeeping missions', 'Nothing at all', 'Only trade disputes', 'Only sports competitions'], 0),
    ('Why might countries send peacekeepers to a region?', ['To help maintain peace after conflict', 'To start new wars', 'To remove all citizens', 'To ignore the region entirely'], 0),
    ('Peacekeeping missions are often organized through which international organization?', ['The United Nations', 'A single countrys army alone', 'A private company', 'No organization at all'], 0),
    ('Why might a country be proud of its peacekeeping history?', ['It shows a commitment to promoting peace around the world', 'It shows a wish to avoid all cooperation', 'It has no meaning at all', 'It shows a preference for conflict'], 0)]),
]),
day(140, [
L('Language Review: Run-on Sentences, Etymology, and Interview Skills',
  'Grade 3 Language strand review: students revisit correcting run-on sentences, etymology, identifying a central argument, writing a formal email, interviewing skills, collective nouns, comparing a book and its film adaptation, transition words, and writing an eyewitness news report.',
  [('What is a run-on sentence?', ['Two or more independent clauses joined without proper punctuation or a conjunction', 'A sentence that is too short', 'A sentence with no verb', 'A question with no answer'], 0),
   ('What is etymology?', ['The study of where words come from and how they have changed', 'The study of punctuation marks', 'The study of handwriting', 'The study of grammar rules only'], 0),
   ('What is the central argument of a persuasive text?', ['The main claim the writer wants readers to believe or act on', 'A random fact with no purpose', 'The title of the text only', 'A list of unrelated ideas'], 0),
   ('What is a collective noun?', ['A noun that names a group treated as one unit', 'A noun that names only one object', 'A verb that describes an action', 'An adjective that describes a noun'], 0),
   ('What do transition words help do?', ['Connect ideas within and between sentences', 'Remove all punctuation', 'Make writing harder to follow', 'Delete verbs from a sentence'], 0)]),
M('Math Review: Large Numbers, Multiplication, and Circumference',
  'Grade 3 Math strand review: students revisit comparing and ordering numbers to 100 000, composite figures, 3-digit by 1-digit multiplication, checking division with multiplication, mean, converting mixed numbers and improper fractions, the metric system, savings goals, and circumference.',
  [('When comparing two large numbers, which digit should you look at first?', ['The digit with the greatest place value', 'The digit with the smallest place value', 'The last digit only', 'Any digit chosen at random'], 0),
   ('What is a composite figure?', ['A shape made by combining two or more simple shapes', 'A shape with only one side', 'A shape that has no corners', 'A perfectly round shape'], 0),
   ('How do you find the mean of a data set?', ['Add all the values and divide by the number of values', 'Multiply all the values together', 'Subtract the smallest value from the largest', 'Count the number of values only'], 0),
   ('What does the prefix kilo- mean?', ['1000', '100', '10', '1/1000'], 0),
   ('What is the circumference of a circle?', ['The distance around its outer edge', 'The distance across the circle through the centre', 'The distance from the centre to the edge', 'The area inside the circle'], 0)]),
Sc('Science Review: Body Systems, Habitats, and Predators',
   'Grade 3 Science strand review: students revisit the circulatory system, the nervous system, the skin, the five senses, mountain and alpine habitats, predator-prey relationships, earthworms and soil health, weather versus climate, and the life cycle of a honeybee.',
   [('What is the main job of the heart?', ['To pump blood throughout the body', 'To digest food', 'To help us breathe', 'To help us think'], 0),
    ('What is the main job of the nervous system?', ['To send and receive messages throughout the body', 'To digest food', 'To pump blood', 'To filter air only'], 0),
    ('What is the largest organ of the human body?', ['The skin', 'The heart', 'The stomach', 'The brain'], 0),
    ('What is a predator?', ['An animal that hunts and eats other animals', 'An animal that only eats plants', 'A plant that grows in water', 'A rock formation'], 0),
    ('How is climate different from weather?', ['Climate describes long-term patterns, while weather describes short-term conditions', 'They mean exactly the same thing', 'Climate only applies to oceans', 'Weather only applies to mountains'], 0)]),
SS('Social Studies Review: Government, Explorers, and Canadian Symbols',
   'Grade 3 Social Studies strand review: students revisit the Inuit, early European explorers, the Governor General, how a bill becomes a law, the Senate and House of Commons, Canadian achievements in space, land acknowledgements, the Coat of Arms, and Canadian peacekeeping.',
   [('The Inuit are one of how many recognized groups of Indigenous peoples in Canada?', ['Three', 'One', 'Ten', 'Twenty'], 0),
    ('Who does the Governor General represent in Canada?', ['The King or Queen', 'The mayor of Toronto', 'The Prime Minister of another country', 'A local school board'], 0),
    ('What are the two parts of the Parliament of Canada?', ['The House of Commons and the Senate', 'The Mayor and the Council', 'The Army and the Navy', 'The Courts and the Police'], 0),
    ('What is the Coat of Arms?', ['An official symbol of Canada', 'A type of currency', 'A type of holiday', 'A type of map'], 0),
    ('What is peacekeeping?', ['Sending trained personnel to help maintain peace in areas affected by conflict', 'Starting new conflicts between countries', 'Refusing to help other countries', 'Selling weapons to all countries'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_131_140, seed=20260801)
    append_to(3, g3_131_140)
