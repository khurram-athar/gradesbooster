#!/usr/bin/env python3
"""Grade 2, Days 151-160 -- thirteenth batch, extending Grade 2 past Day 150
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field --
Grade 2's sub() signature is exactly (subject_key, title, summary,
resourceLabel, resourceUrl, quiz), confirmed by reading gen_curriculum.py
directly rather than assuming; there is no worksheet argument anywhere
in Grade 2's own generator scripts or in gen_curriculum.build()/append_to()):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by the video-backfill task)

Topics chosen to avoid overlap with existing Grade 2 Days 1-150 (dumped
and checked against data/grade2.json before writing, which already
densely covers nearly the full grade 2 ELA, math, science, and social
studies curriculum -- including, notably, nearly every multiplication
fact family 0-12, most fraction/graph/measurement topics, and dozens of
specific animals, habitats, and Canadian civics topics):

Language: conjunctions, homographs, character traits, journal writing,
text features (bold print and italics), assonance and consonance,
hyperbole, acrostic poems, and writing a fictional story (distinct from
the existing personal narrative/true story lesson).

Math: line graphs, parallel and perpendicular lines, telling time on
digital versus analog clocks, fraction of a group, finding the total
cost of multiple items, naming polygons by number of sides, comparing
numbers with greater-than/less-than/equal signs, comparing fractions
with different denominators using models, and choosing the best type of
graph for a data set. (Multiplication facts 0-12 are already exhaustively
covered across Days 1-150, so no new multiplication-facts day was added;
similarly "estimating products" and "line plots" already exist and were
avoided.)

Science: the digestive system, sharks, penguins, invasive species,
biodiversity, grasslands and prairies, keystone species, scavengers, and
deciduous versus coniferous trees -- none of which appear in the very
dense existing Days 1-150 science coverage (which already includes the
heart, lungs, immune system, bones/muscles, vertebrates/invertebrates,
food chains/webs, camouflage, symbiosis, ecosystems, and dozens of named
animals and habitats).

Social Studies: the Royal Canadian Mounted Police, multiculturalism,
hockey, municipal taxes, the Trans-Canada Highway, public libraries, the
lieutenant governor, Canadian citizenship, and the Canadian Armed Forces
-- distinct from the existing Governor General, premier/prime minister,
immigration, currency, and public-safety-services lessons already in
Days 1-150.

Day 160 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch (Day 140, Day 150,
etc). Its four review titles are textually distinct from every earlier
review title in Days 1-150. No embedded ASCII double-quote or straight
apostrophe characters are used anywhere in title/summary/quiz text --
contractions and possessives are avoided entirely (or rewritten without
the apostrophe, e.g. "Canadas" not "Canada's") to keep the generated .ts
string literals valid.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to


def mk(subject_key, title, summary, quiz):
    rl = f'YouTube: {title}'
    ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{title} grade 2 educational')
    return sub(subject_key, title, summary, rl, ru, quiz)


def L(t, s, q):
    return mk('Language', t, s, q)


def M(t, s, q):
    return mk('Math', t, s, q)


def Sc(t, s, q):
    return mk('Science', t, s, q)


def SS(t, s, q):
    return mk('SocialStudies', t, s, q)


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


g2_151_160 = [
day(151, [
L('Conjunctions: Joining Words Like And, But, and Or',
  'Grade 2 Language strand: a conjunction is a joining word, such as and, but, or or, that connects two words or two parts of a sentence.',
  [('What is a conjunction?', ['A joining word that connects ideas', 'A punctuation mark', 'A type of noun', 'A vowel sound'], 0),
   ('Which word is a conjunction?', ['And', 'Jump', 'Blue', 'Quickly'], 0),
   ('Which sentence uses a conjunction correctly?', ['I like apples and oranges', 'I like apples the oranges', 'I like apples run oranges', 'I like apples big oranges'], 0),
   ('The word but is often used to show ___.', ['A contrast or difference', 'Addition only', 'A question', 'A command'], 0),
   ('Why do writers use conjunctions?', ['To connect ideas smoothly in a sentence', 'To end a sentence', 'To remove all meaning', 'To make a word plural'], 0)]),
M('Data: Line Graphs Showing Change Over Time',
  'Grade 2 Math strand: a line graph uses points connected by lines to show how something changes over time, such as temperature over a week.',
  [('What does a line graph show?', ['How something changes over time', 'A single number only', 'A list of names', 'A shape'], 0),
   ('What connects the points on a line graph?', ['Lines', 'Bars', 'Circles', 'Squares'], 0),
   ('Which of these would a line graph be good for showing?', ['Temperature changing each day of the week', 'The colour of a shirt', 'A single students name', 'The title of a book'], 0),
   ('If a line graph slopes upward, what does that usually mean?', ['The value is increasing', 'The value is staying the same', 'The value is unknown', 'There is no data'], 0),
   ('A line graph is especially useful for showing data over ___.', ['Time', 'A single moment', 'No particular order', 'Colours'], 0)]),
Sc('The Digestive System: How Our Body Uses Food',
   'Grade 2 Science strand: the digestive system breaks down the food we eat so our body can use it for energy and growth.',
   [('What does the digestive system do?', ['Breaks down food so the body can use it', 'Pumps blood through the body', 'Helps us see', 'Helps us hear'], 0),
    ('Why does our body need to break down food?', ['To get energy and nutrients for growth', 'Food has no purpose in the body', 'To make the food disappear completely', 'To change the food into water only'], 0),
    ('Where does digestion begin?', ['In the mouth, with chewing', 'In the feet', 'In the ears', 'In the hair'], 0),
    ('Which of these is part of the digestive system?', ['The stomach', 'The eye', 'The ear', 'The skin only'], 0),
    ('After food is digested, the body uses the nutrients to ___.', ['Grow and have energy', 'Stop growing completely', 'Lose all its energy', 'Change colour'], 0)]),
SS('The Royal Canadian Mounted Police: A National Police Force',
   'Grade 2 Social Studies strand: the Royal Canadian Mounted Police, or RCMP, is a police force that works to keep people safe across many parts of Canada.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Music Program', 'Regional Canadian Map Project', 'Rural Canadian Mail Post'], 0),
    ('What is the main job of the RCMP?', ['To help keep people safe', 'To deliver mail', 'To teach in schools', 'To build roads'], 0),
    ('The RCMP is known for its distinctive uniform, which is often ___.', ['Red', 'Blue', 'Green', 'Purple'], 0),
    ('Does the RCMP work in only one small area or across much of Canada?', ['Across much of Canada', 'Only in one single city', 'Only outside Canada', 'Only on farms'], 0),
    ('Why might a country have a national police force like the RCMP?', ['To help keep communities safe across a large area', 'It has no real purpose', 'To replace all local governments', 'To stop people from travelling'], 0)]),
]),
day(152, [
L('Homographs: Same Spelling, Different Meanings',
  'Grade 2 Language strand: homographs are words spelled the same way but with different meanings, like bat, the flying animal, and bat, used to hit a ball.',
  [('What is a homograph?', ['A word spelled the same with different meanings', 'A word that sounds different but is spelled the same always', 'A punctuation mark', 'A type of sentence'], 0),
   ('Which word can be a homograph?', ['Bat', 'Elephant', 'Umbrella', 'Rainbow'], 0),
   ('The word bat can mean a flying animal or ___.', ['A tool used to hit a ball', 'A type of tree', 'A colour', 'A season'], 0),
   ('Why can homographs sometimes be tricky for readers?', ['The same word can have more than one meaning', 'They are always spelled differently', 'They never appear in sentences', 'They have no meaning at all'], 0),
   ('How can a reader figure out which meaning of a homograph is being used?', ['By looking at the context of the sentence', 'By ignoring the sentence completely', 'By guessing randomly with no clues', 'By counting the letters only'], 0)]),
M('Geometry: Parallel and Perpendicular Lines',
  'Grade 2 Math strand: parallel lines run side by side and never meet, while perpendicular lines cross each other to form a right angle.',
  [('What do parallel lines never do?', ['Meet or cross', 'Stay straight', 'Bend', 'Touch a point'], 0),
   ('What do perpendicular lines form where they cross?', ['A right angle', 'A curve', 'A circle', 'No angle at all'], 0),
   ('Which of these is an example of parallel lines?', ['The two rails of a train track', 'The hands of a clock at three oclock', 'A single straight line', 'A circle'], 0),
   ('Perpendicular lines cross at an angle of how many degrees?', ['90 degrees', '45 degrees', '180 degrees', '0 degrees'], 0),
   ('Why might builders use parallel and perpendicular lines when constructing a building?', ['To make sure walls and floors line up correctly', 'They have no use in construction', 'To make the building crooked on purpose', 'To remove the need for measurement'], 0)]),
Sc('Sharks: Ocean Predators',
   'Grade 2 Science strand: sharks are fish with skeletons made of cartilage instead of bone, and many species are skilled ocean predators.',
   [('What are shark skeletons mostly made of?', ['Cartilage', 'Bone', 'Wood', 'Metal'], 0),
    ('What is a shark classified as?', ['A fish', 'A mammal', 'A bird', 'A reptile'], 0),
    ('What helps many sharks detect prey in the water?', ['A strong sense of smell', 'Bright colours', 'Loud sounds they make', 'Fur on their skin'], 0),
    ('Which of these describes most sharks?', ['Skilled ocean predators', 'Land animals', 'Insects', 'Birds that fly'], 0),
    ('Why are sharks an important part of ocean ecosystems?', ['They help keep other populations balanced', 'They have no role in the ocean', 'They only live on land', 'They eat only plants'], 0)]),
SS('Multiculturalism: Many Cultures Living Together',
   'Grade 2 Social Studies strand: multiculturalism means people from many different cultures, languages, and traditions live together and share their communities.',
   [('What does multiculturalism mean?', ['People from many cultures living together', 'Only one culture is allowed', 'No cultures exist', 'Everyone must look the same'], 0),
    ('Which of these might be shared in a multicultural community?', ['Different foods, languages, and traditions', 'Only one single food', 'No traditions at all', 'Only one language'], 0),
    ('Why is multiculturalism considered a strength in Canada?', ['It brings many ideas, traditions, and perspectives together', 'It has no benefit at all', 'It forces everyone to be the same', 'It removes all traditions'], 0),
    ('How can students show respect in a multicultural classroom?', ['By learning about and respecting differences', 'By ignoring classmates who are different', 'By making fun of other cultures', 'By refusing to share'], 0),
    ('A community that welcomes many cultures is often described as ___.', ['Multicultural', 'Empty', 'Silent', 'Unchanging'], 0)]),
]),
day(153, [
L('Character Traits: Describing Who Someone Is',
  'Grade 2 Language strand: a character trait describes what a character is like on the inside, such as brave, honest, or kind, shown through their words and actions.',
  [('What is a character trait?', ['A description of what a character is like inside', 'The name of a character', 'The setting of a story', 'The title of a book'], 0),
   ('Which word describes a character trait?', ['Brave', 'Table', 'Jump', 'Blue'], 0),
   ('How can a reader figure out a character trait?', ['By looking at the characters words and actions', 'By counting the pages in the book', 'By reading only the title', 'By ignoring the character completely'], 0),
   ('If a character always helps others, which trait might describe them?', ['Kind', 'Selfish', 'Lazy', 'Rude'], 0),
   ('Character traits help readers understand a character ___.', ['More deeply', 'Less clearly', 'Not at all', 'Only by their name'], 0)]),
M('Telling Time: Digital and Analog Clocks',
  'Grade 2 Math strand: an analog clock shows time with moving hands on a round face, while a digital clock shows time using numbers only.',
  [('Which clock shows time using hands on a round face?', ['An analog clock', 'A digital clock', 'A calendar', 'A ruler'], 0),
   ('Which clock shows time using numbers only?', ['A digital clock', 'An analog clock', 'A thermometer', 'A scale'], 0),
   ('On an analog clock, which hand moves faster, the hour hand or the minute hand?', ['The minute hand', 'The hour hand', 'They move at the same speed', 'Neither hand moves'], 0),
   ('If a digital clock reads 3:30, what would an analog clock show at the same time?', ['The hour hand between 3 and 4, minute hand at 6', 'The hour hand at 12', 'Both hands at 12', 'The minute hand at 3 only'], 0),
   ('Why is it useful to be able to read both kinds of clocks?', ['Both types of clocks are used in everyday life', 'Only one type of clock exists', 'Clocks are never used', 'Digital clocks are never accurate'], 0)]),
Sc('Penguins: Birds That Cannot Fly',
   'Grade 2 Science strand: penguins are birds with wings shaped like flippers that help them swim instead of fly, and many species live in cold climates.',
   [('Can most penguins fly?', ['No, they cannot fly', 'Yes, they fly very high', 'Yes, but only short distances', 'Only baby penguins can fly'], 0),
    ('What are penguin wings shaped like?', ['Flippers, for swimming', 'Large sails', 'Long straws', 'Umbrellas'], 0),
    ('What helps penguins move quickly through water?', ['Their flipper-shaped wings', 'Their beaks alone', 'Their eyes', 'Their tails alone'], 0),
    ('Where do many penguin species live?', ['Cold climates', 'Hot deserts', 'Rainforests', 'Underground caves only'], 0),
    ('Penguins are classified as ___.', ['Birds', 'Fish', 'Mammals', 'Reptiles'], 0)]),
SS('Hockey: Canadas Popular Winter Sport',
   'Grade 2 Social Studies strand: hockey is a fast winter sport played on ice that is closely connected to Canadian culture and community life.',
   [('What kind of sport is hockey?', ['A fast winter sport played on ice', 'A summer sport played in water', 'A sport played only indoors on grass', 'A sport with no equipment'], 0),
    ('What surface is hockey typically played on?', ['Ice', 'Sand', 'Grass', 'Water'], 0),
    ('Why is hockey often connected to Canadian culture?', ['It is a widely popular and celebrated sport across the country', 'No one in Canada plays hockey', 'It is only played in one small town', 'It has no connection to community life'], 0),
    ('Which of these is equipment commonly used in hockey?', ['A stick and skates', 'A racket and net only', 'A bat and glove', 'A bow and arrow'], 0),
    ('Community hockey rinks can help bring people together by ___.', ['Giving neighbours a place to play and watch together', 'Keeping everyone apart', 'Closing all winter activities', 'Removing community events'], 0)]),
]),
day(154, [
L('Journal Writing: Recording Your Day',
  'Grade 2 Language strand: journal writing means recording thoughts, feelings, and events from your day, often written regularly like a personal diary.',
  [('What is journal writing?', ['Recording thoughts and events from your day', 'Writing a made-up fairy tale only', 'Writing a science report only', 'Copying words from a dictionary'], 0),
   ('How often might someone write in a journal?', ['Regularly, such as every day', 'Only once in a lifetime', 'Never', 'Only during a test'], 0),
   ('What might a journal entry include?', ['Thoughts, feelings, and events from the day', 'Only numbers', 'Only a list of colours', 'Only other peoples names'], 0),
   ('Why might writing in a journal be helpful?', ['It helps you reflect on and remember your day', 'It has no purpose at all', 'It removes your memories', 'It replaces reading completely'], 0),
   ('Journal writing is usually written from whose point of view?', ['The writers own point of view', 'A strangers point of view only', 'No point of view at all', 'A made-up characters point of view only'], 0)]),
M('Fractions: Finding a Fraction of a Group',
  'Grade 2 Math strand: finding a fraction of a group means splitting a set of objects into equal parts and counting how many are in one or more of those parts.',
  [('What does it mean to find a fraction of a group?', ['Splitting a set into equal parts', 'Adding two whole numbers', 'Measuring length', 'Telling time'], 0),
   ('What is 1/2 of a group of 8 objects?', ['2', '4', '6', '8'], 1),
   ('What is 1/4 of a group of 12 objects?', ['2', '3', '4', '6'], 1),
   ('To find a fraction of a group, we first split the group into ___.', ['Equal parts', 'Random piles', 'One large pile', 'Two unequal piles'], 0),
   ('What is 1/3 of a group of 9 objects?', ['2', '3', '4', '5'], 1)]),
Sc('Invasive Species: When Plants or Animals Do Not Belong',
   'Grade 2 Science strand: an invasive species is a plant or animal that moves into a new area where it does not naturally belong and can crowd out native species.',
   [('What is an invasive species?', ['A plant or animal that does not naturally belong in an area', 'Any animal that lives in a zoo', 'A type of pet only', 'A plant grown in a garden on purpose'], 0),
    ('What can invasive species do to native plants and animals?', ['Crowd them out and compete for resources', 'Always help them grow faster', 'Have no effect on them at all', 'Protect them from every danger'], 0),
    ('How might an invasive species arrive in a new area?', ['It can be carried there accidentally by people or transport', 'It always evolves there naturally', 'It has always lived there', 'It can only appear by magic'], 0),
    ('Why do scientists study invasive species carefully?', ['To understand and reduce the harm they might cause', 'Invasive species cause no harm at all', 'To help them spread faster', 'To remove all native species instead'], 0),
    ('A species that belongs naturally in an area is called a ___ species.', ['Native', 'Invasive', 'Imaginary', 'Extinct'], 0)]),
SS('Municipal Taxes: How Cities Pay for Services',
   'Grade 2 Social Studies strand: municipal taxes are money collected by a city or town from residents to help pay for services like roads, parks, and libraries.',
   [('What are municipal taxes?', ['Money collected by a city to pay for services', 'A type of holiday', 'A type of sport', 'A kind of weather'], 0),
    ('Which of these might municipal taxes help pay for?', ['Roads, parks, and libraries', 'Only one persons house', 'Only private businesses', 'Nothing at all'], 0),
    ('Who usually pays municipal taxes?', ['Residents of a city or town', 'Only visitors passing through', 'No one', 'Only children'], 0),
    ('Why does a city need money from taxes?', ['To provide services that benefit the whole community', 'Cities need no money at all', 'To keep the money hidden away', 'To pay for things in other countries only'], 0),
    ('Municipal taxes are an example of how a community works together to ___.', ['Fund shared services', 'Avoid helping each other', 'Remove all public services', 'Ignore community needs'], 0)]),
]),
day(155, [
L('Text Features: Bold Print and Italics',
  'Grade 2 Language strand: bold print makes words stand out as darker and thicker, while italics slant words sideways, and both features signal important words to readers.',
  [('What does bold print look like?', ['Darker and thicker than regular text', 'Slanted sideways', 'Underlined only', 'Invisible'], 0),
   ('What does italic text look like?', ['Slanted sideways', 'Darker and thicker', 'Underlined only', 'Invisible'], 0),
   ('Why might an author use bold print for a word?', ['To show that the word is especially important', 'To hide the word from readers', 'To remove the word from the sentence', 'To make the word disappear'], 0),
   ('Which of these is a common use for italics?', ['Showing the title of a book', 'Making a word invisible', 'Removing punctuation', 'Ending a sentence'], 0),
   ('Bold print and italics are both examples of ___.', ['Text features', 'Punctuation marks', 'Vowel sounds', 'Consonant blends'], 0)]),
M('Money: Finding the Total Cost of Multiple Items',
  'Grade 2 Math strand: students add the prices of several items together to find the total cost of a purchase.',
  [('If a pencil costs 1 dollar and an eraser costs 2 dollars, what is the total cost?', ['2 dollars', '3 dollars', '4 dollars', '5 dollars'], 1),
   ('If three toys each cost 2 dollars, what is the total cost?', ['4 dollars', '5 dollars', '6 dollars', '8 dollars'], 2),
   ('To find the total cost of several items, we ___ their prices.', ['Add', 'Subtract', 'Ignore', 'Divide only'], 0),
   ('If a book costs 5 dollars and a bookmark costs 1 dollar, what is the total cost?', ['4 dollars', '5 dollars', '6 dollars', '7 dollars'], 2),
   ('Why is it useful to know how to find a total cost before shopping?', ['It helps make sure you have enough money', 'It has no real use', 'It only matters for adults', 'It removes the need for money'], 0)]),
Sc('Biodiversity: Many Kinds of Living Things in One Place',
   'Grade 2 Science strand: biodiversity means having many different kinds of living things, like plants, animals, and insects, living together in one area.',
   [('What does biodiversity mean?', ['Having many different kinds of living things in one area', 'Having only one kind of animal', 'Having no living things at all', 'Having only rocks and sand'], 0),
    ('Which of these describes a place with high biodiversity?', ['A rainforest with many different species', 'An empty parking lot', 'A room with no plants or animals', 'A single house with one pet'], 0),
    ('Why is biodiversity important for an ecosystem?', ['It helps the ecosystem stay healthy and balanced', 'It has no importance at all', 'It always causes harm', 'It removes the need for any species'], 0),
    ('Which of these could reduce biodiversity in an area?', ['Destroying habitats', 'Protecting many species', 'Planting more variety of plants', 'Creating nature reserves'], 0),
    ('A healthy ecosystem usually has ___ different kinds of living things.', ['Many', 'Zero', 'Exactly one', 'No particular number of'], 0)]),
SS('The Trans-Canada Highway: Connecting the Country',
   'Grade 2 Social Studies strand: the Trans-Canada Highway is a very long road that connects communities across the country, from coast to coast.',
   [('What does the Trans-Canada Highway connect?', ['Communities across the country, coast to coast', 'Only two small towns', 'Only cities outside Canada', 'Nothing at all'], 0),
    ('What kind of route is the Trans-Canada Highway?', ['A very long road', 'A short walking path', 'A river route', 'A railway only'], 0),
    ('Why might a road like this be important for a large country?', ['It helps people and goods travel long distances', 'It has no real purpose', 'It only connects two houses', 'It prevents any travel at all'], 0),
    ('Which of these might travel along the Trans-Canada Highway?', ['Cars, trucks, and travellers', 'Only bicycles', 'Only boats', 'Only airplanes'], 0),
    ('A highway that spans an entire country helps support ___.', ['Trade and travel between communities', 'Isolation between communities', 'The end of all transportation', 'Nothing important'], 0)]),
]),
day(156, [
L('Assonance and Consonance: Sound Patterns in Poetry',
  'Grade 2 Language strand: assonance repeats vowel sounds within nearby words, while consonance repeats consonant sounds, and both create musical patterns in poetry.',
  [('What does assonance repeat?', ['Vowel sounds within nearby words', 'Only the first letter of a word', 'Punctuation marks', 'Whole sentences'], 0),
   ('What does consonance repeat?', ['Consonant sounds within nearby words', 'Only vowel letters', 'Whole paragraphs', 'Titles of poems'], 0),
   ('Which is an example of assonance?', ['The rain in Spain falls mainly', 'A quiet cat sat', 'A loud dog ran', 'The sky is blue'], 0),
   ('Why might a poet use assonance or consonance?', ['To create a musical, pleasing sound pattern', 'To remove all sound from the poem', 'To confuse the reader on purpose', 'To make the poem impossible to read'], 0),
   ('Assonance and consonance are both examples of ___ in poetry.', ['Sound patterns', 'Story elements', 'Grammar rules', 'Punctuation marks'], 0)]),
M('Geometry: Naming Polygons by Number of Sides',
  'Grade 2 Math strand: polygons are named by how many sides and angles they have, such as a triangle with three sides or a pentagon with five sides.',
  [('How many sides does a triangle have?', ['3', '4', '5', '6'], 0),
   ('How many sides does a pentagon have?', ['4', '5', '6', '7'], 1),
   ('How many sides does a hexagon have?', ['5', '6', '7', '8'], 1),
   ('How many sides does an octagon have?', ['6', '7', '8', '9'], 2),
   ('A polygon is named based on its number of ___.', ['Sides', 'Colours', 'Corners only, never sides', 'Textures'], 0)]),
Sc('Grasslands and Prairies: Open Habitats',
   'Grade 2 Science strand: grasslands and prairies are wide open habitats covered mostly in grasses, with few trees, and are home to animals adapted to open spaces.',
   [('What covers most of a grassland or prairie?', ['Grasses', 'Tall trees', 'Ice', 'Ocean water'], 0),
    ('Do grasslands usually have many trees or few trees?', ['Few trees', 'Many tall trees', 'Trees only, no grass', 'No plants at all'], 0),
    ('Which animal might be adapted to living on an open prairie?', ['An animal built for running long distances', 'A fish that only lives in the deep ocean', 'An animal that only lives in caves', 'A creature that only lives underwater'], 0),
    ('Why might grassland animals need to be fast runners?', ['There are few places to hide from predators', 'There is too much water to swim in', 'There are too many trees to climb', 'They never need to move at all'], 0),
    ('A prairie is an example of a ___.', ['Habitat', 'Weather pattern', 'Type of rock', 'Kind of ocean'], 0)]),
SS('Public Libraries: Free Access to Books for Everyone',
   'Grade 2 Social Studies strand: a public library is a community place where anyone can borrow books and other resources for free.',
   [('What can people usually do at a public library?', ['Borrow books for free', 'Buy expensive furniture', 'Watch a sports game', 'Get a haircut'], 0),
    ('Who is usually allowed to use a public library?', ['Anyone in the community', 'Only certain wealthy people', 'Only teachers', 'Only one single family'], 0),
    ('Why are public libraries an important community resource?', ['They give everyone free access to books and information', 'They charge very high prices for everything', 'They are only open one day per year', 'They have no useful resources'], 0),
    ('Besides books, what else might a public library offer?', ['Computers or community programs', 'Only empty rooms', 'Nothing besides books', 'Only outdoor sports equipment'], 0),
    ('A public library helps support learning by making resources ___.', ['Accessible to everyone', 'Available to no one', 'Extremely expensive', 'Hidden away'], 0)]),
]),
day(157, [
L('Hyperbole: Exaggerating for Effect',
  'Grade 2 Language strand: hyperbole is an extreme exaggeration used to make a strong point or add humour, like saying I am so hungry I could eat a horse.',
  [('What is hyperbole?', ['An extreme exaggeration', 'A true, exact statement', 'A type of punctuation', 'A silent letter'], 0),
   ('Which sentence is an example of hyperbole?', ['I am so tired I could sleep for a year', 'I slept for eight hours', 'I woke up at seven', 'I feel a little tired'], 0),
   ('Why might a writer use hyperbole?', ['To make a strong point or add humour', 'To state only exact facts', 'To confuse the reader with true numbers', 'To remove all feeling from writing'], 0),
   ('Is hyperbole meant to be taken literally?', ['No, it is an exaggeration, not literal', 'Yes, it is always exactly true', 'It has no meaning at all', 'It is a math equation'], 0),
   ('Which of these is the best example of hyperbole?', ['This bag weighs a million pounds', 'This bag weighs five pounds', 'This bag is blue', 'This bag has a zipper'], 0)]),
M('Number Sense: Comparing Numbers Using Greater Than, Less Than, and Equal Signs',
  'Grade 2 Math strand: students compare two numbers using the greater than sign, the less than sign, or the equal sign to show their relationship.',
  [('Which symbol means greater than?', ['>', '<', '=', '+'], 0),
   ('Which symbol means less than?', ['<', '>', '=', '-'], 0),
   ('Which symbol means equal to?', ['=', '>', '<', '/'], 0),
   ('Which comparison is correct for 8 and 5?', ['8 is greater than 5', '8 is less than 5', '8 is equal to 5', '8 cannot be compared to 5'], 0),
   ('Which comparison is correct for 6 and 6?', ['6 is equal to 6', '6 is greater than 6', '6 is less than 6', '6 cannot be compared to itself'], 0)]),
Sc('Keystone Species: Animals That Hold Ecosystems Together',
   'Grade 2 Science strand: a keystone species is an animal that has a very large effect on its ecosystem, helping keep many other plants and animals in balance.',
   [('What is a keystone species?', ['An animal with a very large effect on its ecosystem', 'Any animal with no effect on nature', 'A type of rock', 'A kind of plant that never grows'], 0),
    ('What might happen if a keystone species disappeared from its ecosystem?', ['The ecosystem could become unbalanced', 'Nothing would change at all', 'The ecosystem would instantly improve', 'Every other species would disappear too, with no cause'], 0),
    ('Why do scientists pay close attention to keystone species?', ['Because they help keep an ecosystem healthy and balanced', 'They have no importance in an ecosystem', 'They only exist in stories', 'They cause every ecosystem to fail'], 0),
    ('A keystone species can be thought of as important because it ___.', ['Supports many other living things around it', 'Lives completely alone with no effect', 'Only eats rocks', 'Has no connection to its habitat'], 0),
    ('Keystone species help scientists understand how living things are ___.', ['Connected to each other', 'Completely separate from each other', 'Unimportant to nature', 'Impossible to study'], 0)]),
SS('The Lieutenant Governor: A Provincial Representative of the Crown',
   'Grade 2 Social Studies strand: the lieutenant governor is a ceremonial representative of the Crown in each province, similar to the Governor General at the national level.',
   [('What role does a lieutenant governor represent?', ['A ceremonial representative of the Crown in a province', 'The mayor of a city', 'A school principal', 'A local shop owner'], 0),
    ('Is the lieutenant governor role found at the provincial or federal level?', ['The provincial level', 'The federal level only', 'The municipal level only', 'It does not exist in Canada'], 0),
    ('Which national role is similar to a provincial lieutenant governor?', ['The Governor General', 'The Prime Minister', 'A mayor', 'A school teacher'], 0),
    ('What kind of duties does a lieutenant governor often perform?', ['Ceremonial duties, such as opening a legislature session', 'Cooking meals for the province', 'Driving school buses', 'Coaching sports teams'], 0),
    ('Each Canadian province has its own ___.', ['Lieutenant governor', 'Ocean', 'National anthem', 'Country'], 0)]),
]),
day(158, [
L('Acrostic Poems: Writing With Hidden Words',
  'Grade 2 Language strand: an acrostic poem uses the first letter of each line to spell out a word, often the topic of the poem, reading down the page.',
  [('What does an acrostic poem spell using the first letter of each line?', ['A hidden word, often the topic', 'A random number', 'A punctuation mark', 'A silent letter'], 0),
   ('In an acrostic poem, how do the first letters usually read?', ['Down the page', 'Backwards only', 'In a circle', 'Sideways only'], 0),
   ('Why might a writer choose to write an acrostic poem?', ['To creatively connect a word to descriptive lines', 'To remove all words from the poem', 'To make the poem impossible to read', 'To avoid choosing a topic'], 0),
   ('If the word SUN is used in an acrostic poem, how many lines would it likely have?', ['3', '5', '10', '1'], 0),
   ('An acrostic poem is a fun way to explore a topic through ___.', ['Creative, connected lines', 'Random unrelated facts', 'Silence', 'Numbers only'], 0)]),
M('Fractions: Comparing Fractions with Different Denominators Using Models',
  'Grade 2 Math strand: students use visual models, like fraction bars or circles, to compare fractions that have different denominators.',
  [('Why are visual models helpful when comparing fractions with different denominators?', ['They help us see which fraction is larger', 'They make fractions disappear', 'They remove the need for numbers', 'They only work with whole numbers'], 0),
   ('Using a model, which is larger, 1/2 or 1/4?', ['1/2', '1/4', 'They are equal', 'Cannot be compared'], 0),
   ('Using a model, which is larger, 1/3 or 1/6?', ['1/3', '1/6', 'They are equal', 'Cannot be compared'], 0),
   ('When the numerator is the same, a fraction with a smaller denominator is usually ___.', ['Larger', 'Smaller', 'Equal to zero', 'Impossible to compare'], 0),
   ('A fraction bar model divided into more equal parts shows ___ pieces.', ['Smaller', 'Larger', 'The same size', 'No'], 0)]),
Sc('Scavengers: Natures Cleanup Crew',
   'Grade 2 Science strand: scavengers are animals that eat dead plants and animals they find, helping clean up the environment and recycle nutrients.',
   [('What do scavengers typically eat?', ['Dead plants and animals they find', 'Only live prey they hunt', 'Only rocks', 'Nothing at all'], 0),
    ('How do scavengers help the environment?', ['They help clean up dead material and recycle nutrients', 'They make the environment messier', 'They have no effect on the environment', 'They destroy every habitat'], 0),
    ('Which of these best describes a scavenger?', ['An animal that eats what it finds rather than hunts', 'An animal that only eats plants it grows itself', 'An animal that never eats anything', 'An animal that lives only underwater'], 0),
    ('Why are scavengers considered an important part of an ecosystem?', ['They help recycle nutrients back into the environment', 'They have no important role', 'They remove all other animals', 'They stop plants from growing'], 0),
    ('Scavengers are different from predators because scavengers usually ___.', ['Eat animals that are already dead', 'Only eat plants', 'Never eat anything', 'Hunt only live prey'], 0)]),
SS('Canadian Citizenship: Becoming a Canadian',
   'Grade 2 Social Studies strand: Canadian citizenship is the process by which a person officially becomes a member of Canada, often including learning about the countrys history and values.',
   [('What is Canadian citizenship?', ['Officially becoming a member of Canada', 'A type of holiday', 'A type of food', 'A kind of weather'], 0),
    ('What might someone learn about before becoming a Canadian citizen?', ['Canadas history and values', 'Only sports scores', 'Only recipes', 'Only weather patterns'], 0),
    ('Why might a person choose to become a Canadian citizen?', ['To fully participate in Canadian society, including voting', 'It has no benefit at all', 'To stop living in Canada', 'To avoid all responsibilities'], 0),
    ('Which of these could be part of becoming a citizen?', ['Taking a citizenship test and ceremony', 'Ignoring all Canadian laws', 'Never learning about Canada', 'Ending all connections to Canada'], 0),
    ('New citizens joining Canada can add to the countrys ___.', ['Diversity and community', 'Emptiness', 'Isolation', 'Silence'], 0)]),
]),
day(159, [
L('Writing a Fictional Story: Beginning, Middle, and End',
  'Grade 2 Language strand: a fictional story is a made-up tale with a clear beginning that introduces characters, a middle with a problem, and an end with a solution.',
  [('What is a fictional story?', ['A made-up tale', 'A true report of real events', 'A list of facts', 'A dictionary entry'], 0),
   ('What usually happens in the beginning of a fictional story?', ['Characters and setting are introduced', 'The problem is solved', 'The story ends', 'Nothing happens at all'], 0),
   ('What usually happens in the middle of a fictional story?', ['A problem or challenge appears', 'The story has not started yet', 'The characters are introduced for the first time', 'The book cover is shown'], 0),
   ('What usually happens at the end of a fictional story?', ['The problem is solved', 'The characters are introduced', 'The title is chosen', 'Nothing happens at all'], 0),
   ('Why is planning a beginning, middle, and end helpful before writing a story?', ['It helps organize the story clearly', 'It makes the story impossible to write', 'It removes the need for characters', 'It has no benefit at all'], 0)]),
M('Data: Choosing the Best Type of Graph',
  'Grade 2 Math strand: different graphs, like bar graphs, line graphs, and pictographs, are useful for showing different kinds of data.',
  [('Which type of graph is best for showing change over time?', ['A line graph', 'A bar graph only', 'A pictograph only', 'No graph is useful for this'], 0),
   ('Which type of graph uses pictures to represent data?', ['A pictograph', 'A line graph', 'A number line', 'A ruler'], 0),
   ('Which type of graph uses bars to compare amounts?', ['A bar graph', 'A line graph', 'A pictograph', 'A clock'], 0),
   ('Why is it important to choose the right type of graph?', ['It makes the data easier to understand', 'It has no effect on understanding', 'It always makes data more confusing', 'Graphs are never useful'], 0),
   ('If you wanted to compare the heights of five plants, which graph might work best?', ['A bar graph', 'A line graph only', 'No graph at all', 'A pictograph is never useful'], 0)]),
Sc('Deciduous vs Coniferous Trees: Two Kinds of Forests',
   'Grade 2 Science strand: deciduous trees lose their leaves each fall, while coniferous trees have needles and cones and usually stay green all year.',
   [('What do deciduous trees do each fall?', ['Lose their leaves', 'Grow needles instead of leaves', 'Turn into a different plant', 'Disappear completely'], 0),
    ('What do coniferous trees usually have instead of broad leaves?', ['Needles and cones', 'No leaves of any kind', 'Flowers only', 'Fruit only'], 0),
    ('Do coniferous trees usually stay green all year or lose their needles each fall?', ['Stay green all year', 'Lose all their needles every fall', 'Turn a different colour each season', 'Disappear in winter'], 0),
    ('Which of these is an example of a deciduous tree?', ['A maple tree', 'A pine tree', 'A spruce tree', 'A fir tree'], 0),
    ('A forest made mostly of coniferous trees is sometimes called a ___ forest.', ['Evergreen', 'Leafless', 'Underwater', 'Desert'], 0)]),
SS('The Canadian Armed Forces: Protecting Our Country',
   'Grade 2 Social Studies strand: the Canadian Armed Forces are the men and women who serve to protect Canada and help during emergencies at home and abroad.',
   [('What is the main role of the Canadian Armed Forces?', ['To protect Canada and help during emergencies', 'To deliver mail', 'To teach in schools', 'To run grocery stores'], 0),
    ('Where might members of the Canadian Armed Forces help during an emergency?', ['At home in Canada or in other countries', 'Only in outer space', 'Only in one single building', 'Nowhere at all'], 0),
    ('Which of these might the Canadian Armed Forces help with?', ['Natural disasters, like floods', 'Grocery shopping for a family', 'Painting houses', 'Coaching a soccer team'], 0),
    ('The people who serve in the Canadian Armed Forces are often called ___.', ['Members of the military', 'Farmers', 'Librarians', 'Bus drivers'], 0),
    ('Why might communities honour the service of the Canadian Armed Forces?', ['To show respect for their sacrifice and service', 'They have no reason to be honoured', 'The Armed Forces have never helped anyone', 'It has no meaning at all'], 0)]),
]),
day(160, [
L('Language Review: Word Relationships, Poetry Devices, and Story Writing',
  'Grade 2 Language strand review: students revisit conjunctions, homographs, character traits, journal writing, bold and italic text features, assonance and consonance, hyperbole, acrostic poems, and writing a fictional story.',
  [('What is a conjunction?', ['A joining word that connects ideas', 'A punctuation mark', 'A type of noun', 'A vowel sound'], 0),
   ('What is a homograph?', ['A word spelled the same with different meanings', 'A word that sounds different but is spelled the same always', 'A punctuation mark', 'A type of sentence'], 0),
   ('What is a character trait?', ['A description of what a character is like inside', 'The name of a character', 'The setting of a story', 'The title of a book'], 0),
   ('What is hyperbole?', ['An extreme exaggeration', 'A true, exact statement', 'A type of punctuation', 'A silent letter'], 0),
   ('What does an acrostic poem spell using the first letter of each line?', ['A hidden word, often the topic', 'A random number', 'A punctuation mark', 'A silent letter'], 0)]),
M('Math Review: Graphs, Geometry, Time, Fractions, and Comparing Numbers',
  'Grade 2 Math strand review: students revisit line graphs, parallel and perpendicular lines, digital and analog clocks, fraction of a group, total cost, polygons, comparing numbers, comparing fractions, and choosing the best graph.',
  [('What does a line graph show?', ['How something changes over time', 'A single number only', 'A list of names', 'A shape'], 0),
   ('What do perpendicular lines form where they cross?', ['A right angle', 'A curve', 'A circle', 'No angle at all'], 0),
   ('What is 1/2 of a group of 8 objects?', ['2', '4', '6', '8'], 1),
   ('How many sides does a pentagon have?', ['4', '5', '6', '7'], 1),
   ('Which symbol means greater than?', ['>', '<', '=', '+'], 0)]),
Sc('Science Review: Our Bodies, Animals, and Ecosystems',
   'Grade 2 Science strand review: students revisit the digestive system, sharks, penguins, invasive species, biodiversity, grasslands and prairies, keystone species, scavengers, and deciduous versus coniferous trees.',
   [('What does the digestive system do?', ['Breaks down food so the body can use it', 'Pumps blood through the body', 'Helps us see', 'Helps us hear'], 0),
    ('What are shark skeletons mostly made of?', ['Cartilage', 'Bone', 'Wood', 'Metal'], 0),
    ('What is an invasive species?', ['A plant or animal that does not naturally belong in an area', 'Any animal that lives in a zoo', 'A type of pet only', 'A plant grown in a garden on purpose'], 0),
    ('What is a keystone species?', ['An animal with a very large effect on its ecosystem', 'Any animal with no effect on nature', 'A type of rock', 'A kind of plant that never grows'], 0),
    ('What do deciduous trees do each fall?', ['Lose their leaves', 'Grow needles instead of leaves', 'Turn into a different plant', 'Disappear completely'], 0)]),
SS('Social Studies Review: Services, Culture, and Our Country',
   'Grade 2 Social Studies strand review: students revisit the RCMP, multiculturalism, hockey, municipal taxes, the Trans-Canada Highway, public libraries, the lieutenant governor, Canadian citizenship, and the Canadian Armed Forces.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Music Program', 'Regional Canadian Map Project', 'Rural Canadian Mail Post'], 0),
    ('What does multiculturalism mean?', ['People from many cultures living together', 'Only one culture is allowed', 'No cultures exist', 'Everyone must look the same'], 0),
    ('What are municipal taxes?', ['Money collected by a city to pay for services', 'A type of holiday', 'A type of sport', 'A kind of weather'], 0),
    ('What role does a lieutenant governor represent?', ['A ceremonial representative of the Crown in a province', 'The mayor of a city', 'A school principal', 'A local shop owner'], 0),
    ('What is the main role of the Canadian Armed Forces?', ['To protect Canada and help during emergencies', 'To deliver mail', 'To teach in schools', 'To run grocery stores'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_151_160)
    append_to(2, g2_151_160)
