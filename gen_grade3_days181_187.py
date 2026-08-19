#!/usr/bin/env python3
"""Grade 3, Days 181-187 -- FINAL batch, completing the 187-day Ontario
Grade 3 curriculum target. Extends Grade 3 from 180 to 187 days: 6 new
content days (181-186, one new topic per subject per day) plus Day 187 as
a final cross-subject review day that closes out the entire K-12
curriculum build for this grade.

Modeled exactly on gen_grade3_days171_180.py: same L/M/Sc/SS helpers over
gen_curriculum sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-180
topics (see data/grade3.json). Every (subject, title) pair below was
checked against a full dump of Days 1-180 (all subject/title pairs
printed and reviewed) and confirmed to be new. New topics for this
batch: using dashes to add emphasis or extra information, neologisms
(new words), how setting shapes a story mood, writing a fan letter to a
favourite author, giving constructive feedback to a partner, and words
Canadian English has borrowed from French, for Language; introducing
Roman numerals, multiplying by skip counting on a hundred chart, finding
lines of symmetry in everyday objects, fractions of a whole using area
models, creating a pictograph with a scale of two, and calculating a tip
at a restaurant, for Math; raccoons and their nighttime foraging habits,
Canada geese and their V-formation migration, sea otters and how they
use tools, porcupines and their quills, orcas as apex ocean predators,
and how snowflakes form unique crystal shapes, for Science; and the CN
Tower, Canadian Thanksgiving traditions, the Stanley Cup and Canadas
hockey tradition, volunteer firefighters in rural communities, the role
of food banks in communities, and search and rescue teams in Canada, for
Social Studies -- none of those exact ideas appear in Days 1-180. Day
187 is the final cross-subject review day across all four subjects,
matching the end-of-batch pattern used in every prior batch, with review
titles written to be textually distinct from every earlier review days
title, and its tone gently acknowledges this is the capstone review that
closes out the full 187-day Grade 3 program while still following the
exact mechanical review-day format used in every prior batch (one
review entry per subject, five quiz questions drawn from the batchs own
new topics). No embedded ASCII double-quote or straight/curly apostrophe
characters are used anywhere in title/summary/question/option text;
apostrophes are dropped entirely (e.g. Canadas instead of Canada with an
apostrophe s) or the phrasing is rewritten to avoid needing one (e.g. do
not instead of dont), matching the convention established in Days
111-180.

This is the final batch for Grade 3: 180 + 7 = 187, the full-year
Ontario curriculum day target.

Invocation (matches the 171-180 script):
  cd ~/gradesbooster && python3 gen_grade3_days181_187.py
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


def _rebalance_answer_positions(days, seed=20260818):
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


g3_181_187 = [
day(181, [
L('Grammar: Using Dashes to Add Emphasis or Extra Information',
  'Grade 3 Language strand: a dash can interrupt a sentence to add emphasis, an aside, or extra information without changing the main idea of the sentence.',
  [('What can a dash add to a sentence?', ['Emphasis or extra information', 'A completely new topic unrelated to the sentence', 'A silent letter', 'A math symbol'], 0),
   ('Which sentence correctly uses a dash to add extra information?', ['The dog — a small brown terrier — barked loudly.', 'The dog a small — brown, terrier — barked.', 'The, dog small brown terrier — barked loudly', 'The dog small, brown terrier: barked loudly —'], 0),
   ('Where can a dash be placed in a sentence?', ['In the middle or at the end to set off extra information', 'Only at the very beginning of a word', 'Only inside a number', 'Dashes can never be placed in a sentence'], 0),
   ('Why might a writer choose a dash instead of a comma?', ['To create a stronger pause and draw attention to the added information', 'Dashes and commas are always identical', 'To remove the extra information entirely', 'Dashes are never used in writing'], 0),
   ('What happens to the main idea of a sentence when extra information is set off by dashes?', ['The main idea stays clear even with the extra detail added', 'The main idea disappears completely', 'The sentence becomes a question', 'The sentence loses all punctuation'], 0)]),
M('Number: Introducing Roman Numerals to 20',
  'Grade 3 Math strand: Roman numerals use letters such as I, V, and X to represent numbers, and were used by the ancient Romans as their number system.',
  [('Which Roman numeral represents the number 1?', ['I', 'V', 'X', 'L'], 0),
   ('Which Roman numeral represents the number 5?', ['V', 'I', 'X', 'C'], 0),
   ('Which Roman numeral represents the number 10?', ['X', 'I', 'V', 'L'], 0),
   ('What number does the Roman numeral XII represent?', ['12', '7', '15', '21'], 0),
   ('Why might Roman numerals still be used today, such as on clock faces?', ['They are a traditional way to display numbers using letters', 'Because Roman numerals are easier to add', 'Because Roman numerals replace all other numbers', 'Because clocks cannot use regular numbers'], 0)]),
Sc('Science: Raccoons and Their Nighttime Foraging Habits',
   'Grade 3 Science strand: raccoons are nocturnal mammals with dexterous front paws and a habit of searching for food at night in forests, parks, and even cities.',
   [('When are raccoons most active?', ['At night', 'At noon', 'Only in winter', 'Only underwater'], 0),
    ('What helps a raccoon search for and grab food?', ['Its dexterous front paws', 'Its wings', 'Its gills', 'Its long neck'], 0),
    ('Where might raccoons search for food?', ['Forests, parks, and even cities', 'Only deep in the ocean', 'Only in the desert', 'Only in underground caves'], 0),
    ('What word describes an animal that is mostly active at night?', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0),
    ('Why might raccoons be able to live successfully in cities?', ['They can adapt and find food in many different environments', 'Cities have no food sources at all', 'Raccoons never adapt to new environments', 'Raccoons can only survive in one type of habitat'], 0)]),
SS('Social Studies: The CN Tower — An Iconic Canadian Landmark',
   'Grade 3 Social Studies strand: the CN Tower in Toronto is a tall communications and observation tower that has long stood as one of Canadas most recognized landmarks.',
   [('In which city is the CN Tower located?', ['Toronto', 'Ottawa', 'Vancouver', 'Winnipeg'], 0),
    ('What was the CN Tower originally built to support?', ['Communications, such as broadcasting signals', 'Farming equipment', 'Ocean shipping', 'Underground mining'], 0),
    ('What can visitors do at the CN Tower?', ['View the city from an observation deck', 'Go swimming in an ocean', 'Ride a farm tractor', 'Visit an underground mine'], 0),
    ('Why is the CN Tower considered an iconic landmark?', ['It is a tall, recognizable structure closely associated with Toronto and Canada', 'It has no connection to any city', 'It was built outside of Canada', 'It is rarely seen in photographs of Toronto'], 0),
    ('What kind of structure is the CN Tower?', ['A tall tower', 'A short bridge', 'An underground tunnel', 'A small house'], 0)]),
]),
day(182, [
L('Vocabulary: Neologisms — New Words in the English Language',
  'Grade 3 Language strand: a neologism is a newly created word or phrase that enters a language, often to describe a new invention, idea, or trend.',
  [('What is a neologism?', ['A newly created word or phrase', 'A word that has existed for thousands of years', 'A punctuation mark', 'A silent letter'], 0),
   ('Why might a neologism be created?', ['To describe a new invention, idea, or trend', 'To replace every word already in the dictionary', 'Neologisms are never created for a reason', 'To remove words from a language'], 0),
   ('Which is an example of how a neologism might enter a language?', ['A new word is created to describe a new type of technology', 'An old word is removed and never used again', 'A neologism only appears in ancient texts', 'Neologisms only describe animals'], 0),
   ('Over time, what might happen to a popular neologism?', ['It may be added to the dictionary as an accepted word', 'It always disappears within a day', 'It becomes a silent letter', 'It turns into a number'], 0),
   ('Why do languages continue to create neologisms?', ['Language changes over time as new ideas and inventions appear', 'Languages never change', 'Neologisms are not allowed in a language', 'Only ancient languages have neologisms'], 0)]),
M('Multiplication: Multiplying by Skip Counting on a Hundred Chart',
  'Grade 3 Math strand: a hundred chart can be used to multiply by skip counting, moving through the chart in equal jumps that match the multiplication facts being practised.',
  [('What does skip counting on a hundred chart involve?', ['Counting forward in equal jumps', 'Counting backward only by ones', 'Randomly choosing numbers', 'Counting only to ten'], 0),
   ('To find 3 times 5 using skip counting by 5s, how many jumps of 5 would you make?', ['3 jumps', '5 jumps', '15 jumps', '8 jumps'], 0),
   ('If you skip count by 4s starting at zero, which number comes third?', ['12', '8', '16', '4'], 0),
   ('Why might a hundred chart help with multiplication?', ['It shows a visual pattern of equal jumps that match a multiplication fact', 'It removes the need to know any multiplication facts', 'It only works for subtraction', 'It hides the numbers being counted'], 0),
   ('What pattern do you notice when skip counting by 10s on a hundred chart?', ['The numbers land in the same column every time', 'The numbers are always odd', 'The numbers never repeat a pattern', 'The numbers decrease each time'], 0)]),
Sc('Science: Canada Geese and Their V-Formation Migration',
   'Grade 3 Science strand: Canada geese migrate long distances in a V-shaped formation, which helps the birds save energy and communicate during flight.',
   [('What shape do Canada geese often form while migrating?', ['A V-shape', 'A circle', 'A straight line only', 'A square'], 0),
    ('Why might flying in a V-formation help migrating geese?', ['It helps them save energy and communicate during flight', 'It has no benefit to the geese', 'It makes the geese fly slower on purpose', 'It prevents the geese from ever resting'], 0),
    ('What is migration?', ['Travelling long distances, often on a seasonal basis', 'Staying in the exact same spot all year', 'Growing new feathers', 'Building a nest underground'], 0),
    ('What sound do Canada geese often make while flying together?', ['Honking calls', 'Complete silence at all times', 'A buzzing sound like a bee', 'A roar like a lion'], 0),
    ('Why might geese take turns leading the V-formation?', ['Leading the front takes more energy, so sharing the role helps the group', 'Geese never take turns leading', 'Only one goose is ever allowed to fly', 'Leading the formation takes no energy at all'], 0)]),
SS('Social Studies: Canadian Thanksgiving and Its Traditions',
   'Grade 3 Social Studies strand: Canadian Thanksgiving is a holiday in October when families gather to share a meal and give thanks for the harvest and other good things in their lives.',
   [('In which month is Canadian Thanksgiving celebrated?', ['October', 'July', 'December', 'March'], 0),
    ('What do families traditionally do on Thanksgiving?', ['Gather to share a meal and give thanks', 'Avoid seeing family members', 'Go to school all day', 'Stay silent the entire day'], 0),
    ('What idea does Thanksgiving traditionally celebrate?', ['Being thankful for the harvest and other good things', 'Being upset about the changing seasons', 'Ignoring family and friends', 'Competing in a sports tournament'], 0),
    ('What type of holiday is Thanksgiving?', ['A holiday centred on gratitude and gathering', 'A holiday with no traditions at all', 'A holiday celebrated by only one family in Canada', 'A holiday that has no connection to food'], 0),
    ('Why might sharing a meal be an important part of Thanksgiving traditions?', ['It brings family and friends together to connect and give thanks', 'Meals have no connection to the holiday', 'Thanksgiving meals are always eaten alone', 'Sharing a meal is discouraged on Thanksgiving'], 0)]),
]),
day(183, [
L('Reading: How Setting Shapes a Storys Mood',
  'Grade 3 Language strand: the setting of a story, including the time, place, and weather, can shape the mood or feeling that a reader experiences while reading.',
  [('What is the setting of a story?', ['The time, place, and weather in which the story happens', 'The list of characters only', 'The title of the book', 'The name of the author'], 0),
   ('How can setting affect a storys mood?', ['A dark, stormy setting might create a scary or tense mood', 'Setting never affects mood', 'Mood is only created by character names', 'Setting only affects the length of a story'], 0),
   ('Which setting might create a peaceful mood?', ['A sunny meadow on a calm afternoon', 'A dark cave during a thunderstorm', 'A crowded, noisy battlefield', 'A haunted house at midnight'], 0),
   ('Why might an author carefully choose a storys setting?', ['To help create a particular feeling or atmosphere for the reader', 'Setting has no effect on how a story feels', 'Authors never think about setting', 'Setting only matters in nonfiction books'], 0),
   ('Which setting might help create a mysterious mood?', ['A foggy forest at night', 'A bright, sunny playground at noon', 'A cheerful birthday party', 'A calm, quiet library in the afternoon'], 0)]),
M('Geometry: Finding Lines of Symmetry in Everyday Objects',
  'Grade 3 Math strand: a line of symmetry divides a shape or object into two matching halves that are mirror images of each other, and many everyday objects show this kind of symmetry.',
  [('What does a line of symmetry do?', ['Divides a shape into two matching mirror-image halves', 'Divides a shape into two unequal parts', 'Removes the shape completely', 'Adds a new side to the shape'], 0),
   ('Which everyday object often shows a line of symmetry?', ['A butterfly with matching wings', 'A random scribble', 'A torn piece of paper', 'A pile of sand'], 0),
   ('How many lines of symmetry does a square have?', ['4', '1', '2', '0'], 0),
   ('If you fold a shape along its line of symmetry, what should happen?', ['The two halves should match up exactly', 'The two halves should look completely different', 'The shape should disappear', 'The fold should tear the shape'], 0),
   ('Why might finding lines of symmetry be a useful geometry skill?', ['It helps identify balance and matching patterns in shapes and objects', 'It has no real use in geometry', 'It only works with numbers', 'Lines of symmetry never appear in real objects'], 0)]),
Sc('Science: Sea Otters and How They Use Tools',
   'Grade 3 Science strand: sea otters are marine mammals that float on their backs and sometimes use rocks as tools to crack open the shells of clams and other food.',
   [('What do sea otters sometimes use as a tool?', ['A rock', 'A pair of scissors', 'A wooden hammer', 'A metal spoon'], 0),
    ('Why might a sea otter use a rock while eating?', ['To crack open the shells of clams and other food', 'To build a nest', 'To dig a tunnel', 'To signal other otters'], 0),
    ('How do sea otters often rest and eat on the water?', ['By floating on their backs', 'By standing on the ocean floor', 'By flying above the waves', 'By burrowing into sand'], 0),
    ('What type of animal is a sea otter?', ['A marine mammal', 'A fish', 'An insect', 'A reptile'], 0),
    ('Why is it notable that sea otters use tools?', ['Using tools shows a high level of problem-solving among animals', 'Using tools is common among all ocean animals', 'Tool use has no connection to problem-solving', 'Sea otters never interact with objects around them'], 0)]),
SS('Social Studies: The Stanley Cup and Canadas Hockey Tradition',
   'Grade 3 Social Studies strand: the Stanley Cup is one of the oldest trophies in professional sports and is closely connected to Canadas long tradition of playing and watching hockey.',
   [('What is the Stanley Cup?', ['A trophy connected to professional hockey', 'A type of Canadian currency', 'A famous Canadian mountain', 'A style of Canadian cooking'], 0),
    ('What sport is closely associated with the Stanley Cup?', ['Hockey', 'Soccer', 'Basketball', 'Tennis'], 0),
    ('Why is the Stanley Cup considered historically significant?', ['It is one of the oldest trophies in professional sports', 'It was created only last year', 'It has no connection to any sport', 'It is the newest trophy in the world'], 0),
    ('Why might hockey be considered an important part of Canadian culture?', ['It has a long tradition of being played and watched across the country', 'Hockey has no connection to Canada', 'Hockey is not played in Canada', 'Hockey was invented outside of North America'], 0),
    ('What might communities across Canada do to celebrate hockey?', ['Build local rinks and cheer for hockey teams', 'Avoid playing any winter sports', 'Ban hockey from being played', 'Ignore hockey completely'], 0)]),
]),
day(184, [
L('Writing: Writing a Fan Letter to a Favourite Author',
  'Grade 3 Language strand: a fan letter to a favourite author expresses appreciation for their work and often includes specific details about what the reader enjoyed and questions they might have.',
  [('What is the purpose of a fan letter to an author?', ['To express appreciation for the authors work', 'To criticize the author unfairly', 'To ask the author to stop writing', 'To describe an unrelated topic'], 0),
   ('What might a strong fan letter include?', ['Specific details about what the reader enjoyed in the book', 'No mention of the book at all', 'Only the readers home address', 'A list of unrelated numbers'], 0),
   ('Why might a reader ask questions in a fan letter?', ['To learn more about the authors ideas or writing process', 'Questions are never included in fan letters', 'To confuse the author', 'To avoid mentioning the book'], 0),
   ('What tone would be most appropriate in a fan letter?', ['Polite and appreciative', 'Rude and demanding', 'Angry and threatening', 'Completely blank with no tone'], 0),
   ('Why might mentioning a specific character or scene make a fan letter stronger?', ['It shows the author that the reader engaged closely with their work', 'It makes the letter harder to understand', 'Specific details are never helpful in a letter', 'It has no effect on the letters quality'], 0)]),
M('Fractions: Fractions of a Whole Using Area Models',
  'Grade 3 Math strand: an area model divides a shape, such as a rectangle or circle, into equal parts to show what fraction of the whole shape is shaded or used.',
  [('What does an area model use to represent a fraction?', ['A shape divided into equal parts', 'A single unshaded shape', 'A list of unrelated numbers', 'A shape with unequal parts'], 0),
   ('If a rectangle is divided into 4 equal parts and 1 part is shaded, what fraction is shaded?', ['One fourth', 'One half', 'One third', 'Two fourths'], 0),
   ('Why must the parts of an area model be equal?', ['So each part represents the same size fraction of the whole', 'Equal parts are not required for area models', 'Unequal parts always make fractions larger', 'Area models never use equal parts'], 0),
   ('If a circle is divided into 8 equal slices and 3 are shaded, what fraction is shaded?', ['Three eighths', 'Three fourths', 'Eight thirds', 'One eighth'], 0),
   ('Why might an area model help someone understand fractions?', ['It visually shows how a whole can be divided into equal parts', 'It removes the need to understand fractions', 'It only works with whole numbers', 'It hides the size of each part'], 0)]),
Sc('Science: Porcupines and Their Quills',
   'Grade 3 Science strand: porcupines are rodents covered in sharp quills that they raise as a defense when threatened by predators.',
   [('What covers a porcupines body?', ['Sharp quills', 'Smooth scales', 'Soft feathers', 'A hard shell'], 0),
    ('What do porcupines do with their quills when threatened?', ['Raise them as a defense', 'Hide them completely', 'Throw them at predators from far away', 'Quills have no defensive use'], 0),
    ('What type of animal is a porcupine?', ['A rodent', 'A reptile', 'A bird', 'An amphibian'], 0),
    ('Why might a predator avoid attacking a porcupine?', ['The sharp quills can cause a painful injury', 'Porcupines are always invisible', 'Porcupines can fly away instantly', 'Predators are unaffected by quills'], 0),
    ('How might a porcupines quills help it survive in its habitat?', ['They provide a strong defense against predators', 'Quills provide no benefit to survival', 'Quills prevent the porcupine from ever moving', 'Quills attract predators on purpose'], 0)]),
SS('Social Studies: Volunteer Firefighters in Rural Communities',
   'Grade 3 Social Studies strand: in many small and rural communities across Canada, volunteer firefighters respond to emergencies alongside their regular jobs to help keep their community safe.',
   [('What is a volunteer firefighter?', ['A person who responds to emergencies without it being their full-time paid job', 'A firefighter who never responds to emergencies', 'A person who only fights fires in a city', 'A firefighter who is paid more than anyone else'], 0),
    ('Where are volunteer fire departments especially common?', ['In small and rural communities', 'Only in the largest cities', 'Only outside of Canada', 'Only in communities with no emergencies'], 0),
    ('Why might a rural community rely on volunteer firefighters?', ['The community may be too small to support a large full-time fire department', 'Rural communities never experience emergencies', 'Volunteers are required in every community regardless of size', 'Rural communities have no need for firefighters'], 0),
    ('What might a volunteer firefighter do in addition to firefighting duties?', ['Hold a separate regular job', 'Only work as a firefighter and nothing else', 'Refuse to help their community', 'Live outside of the community they serve'], 0),
    ('Why are volunteer firefighters valuable to their communities?', ['They provide an important safety service that keeps the community protected', 'They provide no real service to their community', 'Volunteer firefighters are never trained', 'They have no connection to community safety'], 0)]),
]),
day(185, [
L('Oral Communication: Giving Constructive Feedback to a Partner',
  'Grade 3 Language strand: constructive feedback focuses on specific, helpful suggestions that encourage a partner to improve their work while also recognizing what they did well.',
  [('What is constructive feedback?', ['Specific, helpful suggestions that encourage improvement', 'Feedback that is only negative', 'Feedback with no details at all', 'Ignoring a partners work completely'], 0),
   ('Why is it helpful to recognize what a partner did well before giving suggestions?', ['It encourages the partner and shows the feedback is balanced', 'It makes the feedback less honest', 'Positive comments are never included in feedback', 'It confuses the partner on purpose'], 0),
   ('Which is an example of specific, constructive feedback?', ['Your introduction clearly explains the topic, and one more detail could make it even stronger.', 'Your work is bad.', 'This makes no sense at all.', 'I have nothing to say.'], 0),
   ('Why might a partner want to hear feedback on their work?', ['To learn how to improve and grow as a learner', 'Feedback has no purpose for a partner', 'To be discouraged from ever trying again', 'Feedback is never useful in a group setting'], 0),
   ('What tone should be used when giving feedback to a partner?', ['A respectful and encouraging tone', 'A harsh and mocking tone', 'A tone with no words at all', 'An angry and dismissive tone'], 0)]),
M('Data: Creating a Pictograph with a Scale of Two',
  'Grade 3 Math strand: a pictograph uses pictures or symbols to represent data, and when a scale of two is used, each picture stands for two items instead of one.',
  [('What does a pictograph use to represent data?', ['Pictures or symbols', 'Only numbers with no pictures', 'Only colours with no symbols', 'Blank spaces'], 0),
   ('If a pictograph uses a scale of two, how many items does each picture represent?', ['2 items', '1 item', '4 items', '10 items'], 0),
   ('If a row has 3 symbols and the scale is two, how many total items does that row represent?', ['6 items', '3 items', '9 items', '12 items'], 0),
   ('Why might a scale of two be used instead of a scale of one?', ['It allows a pictograph to represent larger amounts of data using fewer symbols', 'A scale of two makes data impossible to read', 'Scales are never used in pictographs', 'A scale of two removes the need for a key'], 0),
   ('What part of a pictograph tells you what scale is being used?', ['The key', 'The title only', 'The background colour', 'The border of the graph'], 0)]),
Sc('Science: Orcas — Apex Predators of the Ocean',
   'Grade 3 Science strand: orcas, also called killer whales, are powerful ocean predators that hunt in family groups called pods and communicate using clicks and calls.',
   [('What is another name for an orca?', ['A killer whale', 'A dolphin fish', 'A sea lion', 'A manatee'], 0),
    ('What do orcas hunt in?', ['Family groups called pods', 'Complete isolation at all times', 'Large herds of one hundred', 'Pairs of unrelated orcas only'], 0),
    ('How do orcas communicate with each other?', ['Using clicks and calls', 'Using written symbols', 'Using bright flashing colours', 'Orcas never communicate'], 0),
    ('Why are orcas considered apex predators?', ['They are at the top of the ocean food chain with few natural predators', 'They are hunted by every other ocean animal', 'Apex predators have no role in an ecosystem', 'Orcas are the smallest animals in the ocean'], 0),
    ('What helps orca pods hunt successfully together?', ['Working together and communicating as a group', 'Never working together', 'Avoiding all communication while hunting', 'Hunting alone at all times'], 0)]),
SS('Social Studies: The Role of Food Banks in Communities',
   'Grade 3 Social Studies strand: food banks are community organizations that collect and distribute food to people who need extra support, helping ensure everyone has access to meals.',
   [('What is the main purpose of a food bank?', ['Collecting and distributing food to people who need support', 'Selling food for the highest possible price', 'Growing all of a communitys food', 'Replacing grocery stores completely'], 0),
    ('Where might a food bank get the food it distributes?', ['Donations from community members and organizations', 'Food banks never accept donations', 'Only from one single farm', 'Food appears with no source at all'], 0),
    ('Who might a food bank help in a community?', ['People who need extra support getting enough food', 'Only people who already have plenty of food', 'No one in the community', 'Only businesses looking for a profit'], 0),
    ('Why might volunteers be important to how a food bank runs?', ['They help collect, sort, and distribute food to those in need', 'Volunteers have no role at a food bank', 'Food banks operate with no helpers at all', 'Volunteers only work at grocery stores'], 0),
    ('Why is having access to a food bank valuable for a community?', ['It helps make sure more people have access to the food they need', 'It has no benefit to a community', 'Food banks make it harder to get food', 'It only benefits one single person'], 0)]),
]),
day(186, [
L('Vocabulary: Words Borrowed from French in Canadian English',
  'Grade 3 Language strand: many English words used in Canada come from French, reflecting the countrys history as home to both English and French speaking communities.',
  [('What language have many Canadian English words been borrowed from?', ['French', 'Mandarin', 'Arabic', 'Russian'], 0),
   ('Why might Canadian English include words borrowed from French?', ['Canada has a long history of both English and French speaking communities', 'Canada has no history connected to French', 'Borrowed words are never used in Canadian English', 'French has no connection to Canada'], 0),
   ('What is it called when a language adopts a word from another language?', ['A loanword or borrowed word', 'A silent letter', 'A homophone', 'A contraction'], 0),
   ('Where in Canada might French words be especially common in everyday language?', ['Areas with strong French speaking communities, such as Quebec', 'Nowhere in Canada', 'Only outside of Canada', 'Only in areas with no French speakers'], 0),
   ('Why is it useful to recognize borrowed words in a language?', ['It helps show how cultures and languages influence each other over time', 'Borrowed words have no connection to culture', 'Recognizing borrowed words serves no purpose', 'Languages never influence each other'], 0)]),
M('Financial Literacy: Calculating a Tip at a Restaurant',
  'Grade 3 Math strand: a tip is an extra amount of money added to a bill to thank someone for good service, and it can be estimated using simple mental math.',
  [('What is a tip?', ['An extra amount of money added to a bill for good service', 'A discount taken off a bill', 'A type of tax collected by the government', 'A fee charged for being late'], 0),
   ('If a meal costs 10 dollars and a customer wants to leave a tip of about 2 dollars, roughly what fraction of the bill is the tip?', ['About one fifth', 'About one half', 'About double the bill', 'About one hundredth'], 0),
   ('Why might a customer choose to leave a tip?', ['To thank someone for providing good service', 'Tips are never given for any reason', 'To pay for the cost of the building', 'To replace the price of the meal'], 0),
   ('If a bill is 20 dollars and a tip of 4 dollars is added, what is the new total?', ['24 dollars', '20 dollars', '16 dollars', '28 dollars'], 0),
   ('Why is estimating useful when calculating a tip?', ['It gives a quick, reasonable amount without needing an exact calculation', 'Estimating always gives the wrong answer', 'Tips can never be estimated', 'Estimating removes the need for any math at all'], 0)]),
Sc('Science: How Snowflakes Form Unique Crystal Shapes',
   'Grade 3 Science strand: a snowflake forms when water vapour in a cold cloud freezes directly into a tiny ice crystal, and the exact conditions it passes through give each snowflake a unique six-sided shape.',
   [('What does a snowflake form from?', ['Water vapour freezing directly into an ice crystal', 'Melted rain falling to the ground', 'Dust mixing with warm air', 'Sand carried by the wind'], 0),
    ('How many main sides does a typical snowflake crystal have?', ['Six', 'Three', 'Four', 'Eight'], 0),
    ('Why might no two snowflakes look exactly alike?', ['Each one passes through slightly different temperature and moisture conditions as it falls', 'All snowflakes are actually identical', 'Snowflakes never form in different shapes', 'Snowflakes are shaped by hand'], 0),
    ('Where do snowflakes begin to form?', ['Inside a cold cloud', 'At the bottom of a lake', 'Underground in soil', 'Inside a warm greenhouse'], 0),
    ('Why is studying snowflakes an example of science in nature?', ['It shows how water and temperature can create complex natural patterns', 'Snowflakes have no connection to science', 'Snowflakes are created without any natural process', 'Weather has no effect on how snowflakes form'], 0)]),
SS('Social Studies: Search and Rescue Teams in Canada',
   'Grade 3 Social Studies strand: search and rescue teams are trained volunteers and professionals who look for and help people who are lost or in danger in the wilderness, water, or after a disaster.',
   [('What is the main job of a search and rescue team?', ['Finding and helping people who are lost or in danger', 'Selling maps to hikers', 'Building new hiking trails', 'Repairing broken bridges'], 0),
    ('In what kinds of places might search and rescue teams be needed?', ['The wilderness, on the water, or after a disaster', 'Only inside a shopping mall', 'Only inside a classroom', 'Nowhere, they are never needed'], 0),
    ('Who might be part of a search and rescue team?', ['Trained volunteers and professionals', 'Only people with no training at all', 'Only children under the age of ten', 'Only people who have never left their home'], 0),
    ('Why might search and rescue teams need special training?', ['To safely find and help people in difficult or dangerous conditions', 'Training has no connection to search and rescue', 'Search and rescue work requires no skill at all', 'Special training is never provided to these teams'], 0),
    ('Why are search and rescue teams valuable to a community?', ['They help keep people safe during emergencies in remote or dangerous areas', 'They have no benefit to a community', 'They prevent people from ever going outdoors', 'They only work during the summer months'], 0)]),
]),
day(187, [
L('Language Review: Dashes, Neologisms, and a Grade 3 Farewell',
  'Grade 3 Language strand review, and the final Language day of the Grade 3 program: students revisit using dashes for emphasis, neologisms, how setting shapes a storys mood, writing a fan letter to a favourite author, and giving constructive feedback to a partner.',
  [('What can a dash add to a sentence?', ['Emphasis or extra information', 'A completely new topic unrelated to the sentence', 'A silent letter', 'A math symbol'], 0),
   ('What is a neologism?', ['A newly created word or phrase', 'A word that has existed for thousands of years', 'A punctuation mark', 'A silent letter'], 0),
   ('How can setting affect a storys mood?', ['A dark, stormy setting might create a scary or tense mood', 'Setting never affects mood', 'Mood is only created by character names', 'Setting only affects the length of a story'], 0),
   ('What is the purpose of a fan letter to an author?', ['To express appreciation for the authors work', 'To criticize the author unfairly', 'To ask the author to stop writing', 'To describe an unrelated topic'], 0),
   ('What is constructive feedback?', ['Specific, helpful suggestions that encourage improvement', 'Feedback that is only negative', 'Feedback with no details at all', 'Ignoring a partners work completely'], 0)]),
M('Math Review: Roman Numerals, Symmetry, and a Grade 3 Send-Off',
  'Grade 3 Math strand review, and the final Math day of the Grade 3 program: students revisit Roman numerals, multiplying by skip counting on a hundred chart, lines of symmetry, fractions of a whole using area models, and creating a pictograph with a scale of two.',
  [('Which Roman numeral represents the number 10?', ['X', 'I', 'V', 'L'], 0),
   ('What does skip counting on a hundred chart involve?', ['Counting forward in equal jumps', 'Counting backward only by ones', 'Randomly choosing numbers', 'Counting only to ten'], 0),
   ('What does a line of symmetry do?', ['Divides a shape into two matching mirror-image halves', 'Divides a shape into two unequal parts', 'Removes the shape completely', 'Adds a new side to the shape'], 0),
   ('If a rectangle is divided into 4 equal parts and 1 part is shaded, what fraction is shaded?', ['One fourth', 'One half', 'One third', 'Two fourths'], 0),
   ('If a pictograph uses a scale of two, how many items does each picture represent?', ['2 items', '1 item', '4 items', '10 items'], 0)]),
Sc('Science Review: Wild Canada and a Final Look at Grade 3 Science',
   'Grade 3 Science strand review, and the final Science day of the Grade 3 program: students revisit raccoons, Canada geese migration, sea otters using tools, porcupine quills, and orcas as apex predators.',
   [('When are raccoons most active?', ['At night', 'At noon', 'Only in winter', 'Only underwater'], 0),
    ('What shape do Canada geese often form while migrating?', ['A V-shape', 'A circle', 'A straight line only', 'A square'], 0),
    ('What do sea otters sometimes use as a tool?', ['A rock', 'A pair of scissors', 'A wooden hammer', 'A metal spoon'], 0),
    ('What covers a porcupines body?', ['Sharp quills', 'Smooth scales', 'Soft feathers', 'A hard shell'], 0),
    ('Why are orcas considered apex predators?', ['They are at the top of the ocean food chain with few natural predators', 'They are hunted by every other ocean animal', 'Apex predators have no role in an ecosystem', 'Orcas are the smallest animals in the ocean'], 0)]),
SS('Social Studies Review: Landmarks, Traditions, and Our Community — A Grade 3 Send-Off',
   'Grade 3 Social Studies strand review, and the final Social Studies day of the Grade 3 program: students revisit the CN Tower, Canadian Thanksgiving, the Stanley Cup and hockey tradition, volunteer firefighters, and food banks, closing out the full Grade 3 year.',
   [('In which city is the CN Tower located?', ['Toronto', 'Ottawa', 'Vancouver', 'Winnipeg'], 0),
    ('In which month is Canadian Thanksgiving celebrated?', ['October', 'July', 'December', 'March'], 0),
    ('What is the Stanley Cup?', ['A trophy connected to professional hockey', 'A type of Canadian currency', 'A famous Canadian mountain', 'A style of Canadian cooking'], 0),
    ('Where are volunteer fire departments especially common?', ['In small and rural communities', 'Only in the largest cities', 'Only outside of Canada', 'Only in communities with no emergencies'], 0),
    ('What is the main purpose of a food bank?', ['Collecting and distributing food to people who need support', 'Selling food for the highest possible price', 'Growing all of a communitys food', 'Replacing grocery stores completely'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_181_187, seed=20260818)
    append_to(3, g3_181_187)
