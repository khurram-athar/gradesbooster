#!/usr/bin/env python3
"""Grade 2, Days 181-187 -- sixteenth and FINAL batch for Grade 2, completing
the full 187-day Ontario curriculum target for this grade.

Structural note (checked directly before writing this file, per the
required process): this batch is modeled closely on the immediately prior
batch, gen_grade2_days171_180.py, which was read in full first. That file
itself documents (in its own docstring) that an earlier task brief
inaccurately described Grade 2 as using a "worksheet-required" format with
an append_worksheet_days() helper and a 3-item worksheet field on every
subject -- and that this does NOT match Grade 2's real, current generator
scripts. Grepping every gen_grade2_days*.py file in the repo for the
literal word "worksheet" confirms every hit is inside a docstring
explaining why it is NOT used, never in actual code past roughly Day 100.
So, exactly like gen_grade2_days171_180.py, this file uses the
sub()/day()/append_to() helpers imported directly from gen_curriculum.py,
with Grade 2's exact signature (subject_key, title, summary, resourceLabel,
resourceUrl, quiz) and no worksheet field of any kind:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate video-backfill task)

This is only a 7-day batch (Days 181-187), not the usual 10, because
180 + 7 = 187, the full-year Ontario curriculum target for this grade.
It is structured as 6 new content days (181-186, one new topic per subject
per day) plus Day 187 as a final cross-subject review day.

Topics chosen to avoid overlap with existing Grade 2 Days 1-180 (dumped
from data/grade2.json and checked in full before writing -- Days 1-180
already densely cover nearly the entire Grade 2 ELA, math, science, and
social studies curriculum, including the topics newly added in the
immediately-prior Days 171-180 batch: limericks, reflexive pronouns, tall
tales, onset/rime, kennings, thank-you notes, fables, diamante poems,
tch/dge trigraphs, subtracting fractions, circle graphs, Canadian paper
bills, minutes-to-seconds, balance scales, points/lines/rays, reading a
schedule, skip counting 6s-9s, Carroll diagrams, chameleons, kangaroos,
jellyfish, hummingbirds, savanna habitats, solar eclipses, pulleys, frogs
and toads, wedges/screws, House of Commons, Canadian passport, National
Indigenous Peoples Day, search and rescue, northern lights, Hudson Bay,
Rocky Mountains, border crossings, and the Royal Canadian Mint):

Language: collective nouns, silent e (magic e), r-controlled vowels
(ar/or/er), diphthongs (oi/oy/ou/ow), cinquain poems, and readers theatre
scripts -- none of which appear in the existing Days 1-180 Language
coverage (which already includes limericks, haiku, shape poems, list
poems, free verse, acrostic poems, diamante poems, kennings, possessive
nouns, reflexive pronouns, personal pronouns, several consonant blend,
digraph, and trigraph families, silent letters kn/wr/mb/gh, long and short
vowel sounds, and dozens of other topics).

Math: the 24-hour clock, volume with unit cubes, benchmark fractions
(comparing to zero, one-half, and one), prisms and pyramids, estimating
total cost by rounding, and calculating age in years and months -- new
angles distinct from the extensive existing coverage of telling time,
capacity and mass, fractions (halves/quarters/thirds/eighths, unit
fractions, equivalent fractions, adding and subtracting fractions with the
same denominator, comparing fractions with different denominators), 3D
shape faces/edges/vertices and nets, money coins and bills, and rounding
to the nearest ten and hundred.

Science: sloths, wolves, elephants, kelp forests, ladybugs, and tsunamis
-- none of which appear in the very dense existing Days 1-180 science
coverage (which already includes sharks, penguins, bats, octopuses,
turtles, whales and dolphins, spiders, beavers, ants, bees, birds of prey,
camels, polar animals, nocturnal animals, savanna habitats, tundra,
deserts, rainforests, wetlands, coral reefs, ocean zones, earthquakes,
volcanoes, glaciers, and dozens of other animals, habitats, and
earth-science topics).

Social Studies: the Canadian Shield, the Arctic Ocean, traditional
Indigenous homes (longhouses, tipis, and igloos), Victoria Day, the
Olympic Games in Canada, and curling -- distinct from the existing House
of Commons, Senate, Governor General, Truth and Reconciliation Day,
National Indigenous Peoples Day, Great Lakes, Niagara Falls, Rocky
Mountains, Hudson Bay, Canada Day and Remembrance Day, hockey, and
lacrosse lessons already in Days 1-180.

Day 187 is the final cross-subject review day of the ENTIRE 187-day
Grade 2 curriculum -- the capstone day completing the full-year Ontario
build for this grade. Its four review titles keep the same mechanical
"Subject Review: A, B, and C" format used in every prior batch (Day 150,
Day 160, Day 170, Day 180, etc.), each with an added closing clause
acknowledging this milestone, and are textually distinct from every
earlier review title in Days 1-180. No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz
text -- contractions and possessives are avoided entirely (or rewritten
without the apostrophe, e.g. "Canadas" not "Canada's") to keep the
generated .ts string literals valid.
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


g2_181_187 = [
day(181, [
L('Collective Nouns: A Herd, a Flock, a Pack',
  'Grade 2 Language strand: a collective noun names a group of people, animals, or things acting as one unit, such as a herd of cows, a flock of birds, or a pack of wolves.',
  [('What does a collective noun name?', ['A group of people, animals, or things acting as one unit', 'A single object only', 'A type of punctuation', 'A silent letter'], 0),
   ('Which of these is a collective noun for a group of birds?', ['Flock', 'Slice', 'Puddle', 'Corner'], 0),
   ('Which collective noun describes a group of wolves?', ['Pack', 'Herd', 'Team', 'Choir'], 0),
   ('Which sentence uses a collective noun correctly?', ['A herd of cows grazed in the field', 'A herd of cow grazed in the field', 'A cow of herds grazed in the field', 'Herd a of cows grazed'], 0),
   ('Why are collective nouns useful in writing?', ['They let a writer name a whole group with one word', 'They remove all nouns from a sentence', 'They only work with numbers', 'They cannot describe animals'], 0)]),
M('Time: Introducing the 24-Hour Clock',
  'Grade 2 Math strand: the 24-hour clock numbers the hours from 0 to 23 across a full day, so afternoon and evening times continue counting past 12 instead of starting over.',
  [('How many hours does the 24-hour clock count across a full day?', ['24', '12', '60', '100'], 0),
   ('On a 24-hour clock, what hour comes right after 12?', ['13', '1', '0', '24'], 0),
   ('What time on a 12-hour clock matches 15:00 on a 24-hour clock?', ['3:00 PM', '3:00 AM', '5:00 PM', '1:00 PM'], 0),
   ('Why might schedules like train timetables use the 24-hour clock?', ['It avoids confusing morning and afternoon times', 'It only works for counting minutes', 'It removes the need for numbers', 'It only shows the date, not the time'], 0),
   ('On the 24-hour clock, midnight is usually shown as ___.', ['00:00', '12:00', '24:24', '6:00'], 0)]),
Sc('Sloths: Slow-Moving Rainforest Mammals',
   'Grade 2 Science strand: sloths are mammals that live in rainforest trees, move very slowly to save energy, and often have algae growing in their fur for extra camouflage.',
   [('Where do sloths mainly live?', ['In rainforest trees', 'In deep ocean water', 'In frozen arctic ice', 'In dry desert sand'], 0),
    ('Why do sloths move so slowly?', ['To save energy', 'Because they cannot see', 'Because they have no legs', 'Because they are always asleep'], 0),
    ('What can often be found growing in a sloths fur?', ['Algae', 'Coral', 'Moss made of glass', 'Feathers'], 0),
    ('What type of animal is a sloth?', ['A mammal', 'A reptile', 'A fish', 'An insect'], 0),
    ('How might growing algae help a sloth?', ['It adds extra camouflage in the trees', 'It helps the sloth fly', 'It makes the sloth move faster', 'It has no effect at all'], 0)]),
SS('The Canadian Shield: Ancient Rock Beneath Our Feet',
   'Grade 2 Social Studies strand: the Canadian Shield is a huge area of very old, hard rock that covers much of central and eastern Canada and is rich in minerals.',
   [('What is the Canadian Shield mostly made of?', ['Very old, hard rock', 'Soft sand only', 'Ice that never melts', 'Ocean water'], 0),
    ('Which parts of Canada does the Canadian Shield mostly cover?', ['Much of central and eastern Canada', 'Only a small island', 'Only the ocean floor', 'Another country entirely'], 0),
    ('What natural resource is the Canadian Shield known for containing?', ['Minerals', 'Tropical fruit', 'Coral', 'Sand dunes only'], 0),
    ('How old is the rock of the Canadian Shield generally considered to be?', ['Very old, among the oldest rock on Earth', 'Formed yesterday', 'Formed only last year', 'Newer than most rock on Earth'], 0),
    ('The Canadian Shield is an example of a ___.', ['Geographic landform', 'Type of government', 'National holiday', 'Kind of currency'], 0)]),
]),
day(182, [
L('Silent e: How Adding e Changes a Vowel Sound',
  'Grade 2 Language strand: adding a silent e to the end of a word often changes a short vowel sound into a long vowel sound, such as turning cap into cape or kit into kite.',
  [('What does a silent e at the end of a word often do?', ['Changes a short vowel sound into a long vowel sound', 'Makes the word disappear', 'Adds a new syllable you can hear', 'Removes all vowels from the word'], 0),
   ('Adding a silent e to cap changes it into which word?', ['Cape', 'Cup', 'Cop', 'Cap'], 0),
   ('Adding a silent e to kit changes it into which word?', ['Kite', 'Kit', 'Knot', 'Kite is wrong'], 0),
   ('Is the final e in words like cape or kite pronounced out loud?', ['No, it is silent', 'Yes, it is always loud', 'It is pronounced as a long e sound', 'It is pronounced as a short a sound'], 0),
   ('Which word shows the silent e pattern changing a short vowel to a long vowel?', ['Cube', 'Cub', 'Run', 'Sit'], 0)]),
M('Measurement: Introduction to Volume with Unit Cubes',
  'Grade 2 Math strand: volume measures how much space a solid shape takes up, and one way to measure it is by counting how many small unit cubes fit exactly inside the shape.',
  [('What does volume measure?', ['How much space a solid shape takes up', 'How heavy an object is', 'How long an object is', 'How loud a sound is'], 0),
   ('What is one way to measure the volume of a box?', ['Counting how many unit cubes fit inside it', 'Measuring only its colour', 'Weighing it on a scale', 'Timing how fast it falls'], 0),
   ('If a box is filled exactly with 12 unit cubes, what is its volume?', ['12 cubic units', '12 metres', '12 grams', '12 minutes'], 0),
   ('Which of these could you find the volume of?', ['A cardboard box', 'A shadow', 'A sound', 'A colour'], 0),
   ('Why are unit cubes useful for measuring volume?', ['They are a consistent size that can be counted', 'They melt when placed in a box', 'They change size every time', 'They cannot be counted at all'], 0)]),
Sc('Wolves: Pack Hunters of the Forest',
   'Grade 2 Science strand: wolves are wild relatives of dogs that live and hunt together in groups called packs, working as a team to find food and protect their territory.',
   [('What is a group of wolves called?', ['A pack', 'A herd', 'A flock', 'A school'], 0),
    ('How do wolves usually hunt?', ['Together as a team in a pack', 'Completely alone with no help', 'By staying underwater', 'By flying above their prey'], 0),
    ('What animal are wolves closely related to?', ['Dogs', 'Cats', 'Birds', 'Fish'], 0),
    ('Why might hunting in a pack help wolves?', ['It helps them find and catch food more successfully', 'It makes hunting impossible', 'It has no effect on hunting', 'It only helps them sleep'], 0),
    ('Besides hunting, what else might a wolf pack work together to do?', ['Protect their territory', 'Build underwater nests', 'Grow plants', 'Fly south for winter'], 0)]),
SS('The Arctic Ocean: Canadas Northern Coastline',
   'Grade 2 Social Studies strand: the Arctic Ocean is the icy ocean that borders northern Canada, home to sea ice, unique wildlife, and northern communities.',
   [('Which part of Canada does the Arctic Ocean border?', ['Northern Canada', 'Southern Canada only', 'No part of Canada', 'Only inland lakes'], 0),
    ('What often covers large parts of the Arctic Ocean?', ['Sea ice', 'Tropical coral', 'Sand dunes', 'Rainforest canopy'], 0),
    ('What kind of ocean is the Arctic Ocean generally?', ['Cold and icy', 'Warm and tropical', 'Made entirely of fresh water', 'Located underground'], 0),
    ('Which of these might be found in or near the Arctic Ocean?', ['Northern communities and unique wildlife', 'Desert cactus plants', 'Coral reef fish only', 'Rainforest monkeys'], 0),
    ('The Arctic Ocean is an example of a Canadian ___.', ['Geographic feature', 'Type of government', 'Kind of currency', 'National holiday'], 0)]),
]),
day(183, [
L('R-Controlled Vowels: ar, or, and er',
  'Grade 2 Language strand: when a vowel is followed by the letter r, the r changes how the vowel sounds, as in the ar of car, the or of for, and the er of her.',
  [('What does an r-controlled vowel mean?', ['The letter r changes how the vowel sounds', 'The vowel is always silent', 'The r is never pronounced', 'The vowel becomes a consonant'], 0),
   ('Which r-controlled pattern is found in the word car?', ['Ar', 'Or', 'Er', 'Ir'], 0),
   ('Which r-controlled pattern is found in the word for?', ['Or', 'Ar', 'Er', 'Ur'], 0),
   ('Which word contains the er r-controlled sound?', ['Her', 'Car', 'For', 'Cat'], 0),
   ('Why might r-controlled vowels be tricky for young readers?', ['The r changes the vowel sound in a way that is not obvious from spelling alone', 'They are always completely silent', 'They never appear in real words', 'They only appear at the start of a sentence'], 0)]),
M('Fractions: Benchmark Fractions — Zero, One-Half, and One',
  'Grade 2 Math strand: benchmark fractions like zero, one-half, and one are useful reference points that help estimate whether another fraction is close to none, half, or a whole.',
  [('What are benchmark fractions used for?', ['Helping estimate how close another fraction is to a reference point', 'Multiplying whole numbers only', 'Measuring temperature', 'Telling time'], 0),
   ('Which three benchmark fractions are commonly used?', ['Zero, one-half, and one', 'Two, four, and six', 'Ten, twenty, and thirty', 'One-third, two-thirds, and one'], 0),
   ('Is three-eighths closer to zero or one-half?', ['Zero', 'One-half', 'One', 'It cannot be estimated'], 0),
   ('Is five-sixths closer to one-half or one whole?', ['One whole', 'One-half', 'Zero', 'It cannot be estimated'], 0),
   ('Why are benchmark fractions helpful before doing exact calculations?', ['They give a quick way to estimate the size of a fraction', 'They make fractions impossible to compare', 'They only work with whole numbers', 'They remove the need for numerators'], 0)]),
Sc('Elephants: The Largest Land Animals',
   'Grade 2 Science strand: elephants are the largest land animals on Earth, known for their long trunks, large ears, and strong family bonds within their herds.',
   [('What are elephants known for being?', ['The largest land animals on Earth', 'The smallest land animals on Earth', 'Animals that live only underwater', 'Animals with no legs'], 0),
    ('What body part do elephants use to grab food and drink water?', ['Their trunk', 'Their tail', 'Their ears', 'Their tusks only'], 0),
    ('What might an elephants large ears help it do?', ['Help release heat and cool down', 'Help it fly', 'Help it breathe underwater', 'Help it change colour'], 0),
    ('Elephants are known for living together in groups called ___.', ['Herds', 'Packs', 'Flocks', 'Schools'], 0),
    ('What does it mean that elephants have strong family bonds?', ['Elephant families stay close and care for one another', 'Elephants never interact with other elephants', 'Elephants live completely alone', 'Elephants forget their families quickly'], 0)]),
SS('Traditional Indigenous Homes: Longhouses, Tipis, and Igloos',
   'Grade 2 Social Studies strand: Indigenous peoples across Canada traditionally built different kinds of homes suited to their environment, including longhouses, tipis, and igloos.',
   [('What is a longhouse?', ['A long traditional home shared by several families', 'A type of boat', 'A modern apartment building', 'A kind of bridge'], 0),
    ('What is a tipi traditionally made from?', ['Poles covered with animal hides', 'Solid brick walls', 'Glass panels', 'Steel beams'], 0),
    ('What is an igloo traditionally built from?', ['Blocks of packed snow or ice', 'Wood planks', 'Woven grass', 'Clay bricks'], 0),
    ('Why did different Indigenous groups build different kinds of homes?', ['Homes were suited to their local environment and resources', 'All Indigenous groups built identical homes', 'Home styles had no connection to environment', 'Homes were chosen randomly with no reason'], 0),
    ('Longhouses, tipis, and igloos are all examples of ___.', ['Traditional Indigenous homes', 'Types of vehicles', 'Kinds of food', 'Forms of government'], 0)]),
]),
day(184, [
L('Diphthongs: The Sounds of oi, oy, ou, and ow',
  'Grade 2 Language strand: a diphthong is a vowel sound made by gliding from one vowel sound to another within the same syllable, as in the oi of coin, the oy of boy, the ou of cloud, and the ow of cow.',
  [('What is a diphthong?', ['A vowel sound made by gliding between two vowel sounds', 'A silent consonant', 'A punctuation mark', 'A type of sentence'], 0),
   ('Which diphthong is found in the word coin?', ['Oi', 'Ee', 'Ay', 'Oo'], 0),
   ('Which diphthong is found in the word boy?', ['Oy', 'Ar', 'Er', 'Ea'], 0),
   ('Which diphthong is found in the word cloud?', ['Ou', 'Oi', 'Igh', 'Ee'], 0),
   ('Which word contains the ow diphthong sound heard in cow?', ['Now', 'Snow', 'Low', 'Grow'], 0)]),
M('Geometry: Prisms and Pyramids — Comparing 3D Shapes',
  'Grade 2 Math strand: a prism has two matching flat ends connected by rectangular sides, while a pyramid has one flat base and triangular sides that meet at a single point.',
  [('What shape do the two matching ends of a prism usually have?', ['They match each other', 'They are always circles only', 'They are always triangles only', 'A prism has no ends'], 0),
   ('What connects the two ends of a prism?', ['Rectangular sides', 'Curved lines only', 'Nothing connects them', 'A single point'], 0),
   ('How many flat bases does a pyramid have?', ['One', 'Two', 'Zero', 'Six'], 0),
   ('What shape are the sides of a pyramid, and where do they meet?', ['Triangles that meet at a single point', 'Rectangles that never meet', 'Circles that meet at two points', 'Ovals with no point'], 0),
   ('Which of these is an example of a pyramid shape?', ['A shape with a square base and four triangle sides meeting at a point', 'A can-shaped object with two circle ends', 'A flat rectangle with no height', 'A shape with no faces at all'], 0)]),
Sc('Kelp Forests: Underwater Forests of the Sea',
   'Grade 2 Science strand: kelp forests are underwater habitats made of tall seaweed called kelp that grows from the ocean floor toward the surface, providing shelter and food for many sea animals.',
   [('What is kelp?', ['A tall seaweed that grows in the ocean', 'A type of coral', 'A land plant', 'A kind of rock'], 0),
    ('Where does kelp typically grow?', ['From the ocean floor toward the surface', 'On top of mountains', 'In the desert sand', 'Inside caves with no water'], 0),
    ('What can a kelp forest provide for sea animals?', ['Shelter and food', 'Nothing useful at all', 'Only a place to freeze', 'Only sunlight with no shelter'], 0),
    ('A kelp forest is best described as an underwater ___.', ['Habitat', 'Desert', 'Volcano', 'City street'], 0),
    ('Which of these animals might you expect to find living in a kelp forest?', ['Fish and sea otters', 'Camels', 'Penguins living only on ice', 'Desert lizards'], 0)]),
SS('Victoria Day: Celebrating in Late May',
   'Grade 2 Social Studies strand: Victoria Day is a Canadian holiday celebrated on a Monday in late May, marking the unofficial start of summer with community events and fireworks.',
   [('In which month is Victoria Day celebrated?', ['May', 'July', 'December', 'October'], 0),
    ('On what day of the week does Victoria Day usually fall?', ['A Monday', 'A Sunday', 'A Wednesday', 'A Saturday'], 0),
    ('What does Victoria Day mark the unofficial start of?', ['Summer', 'Winter', 'The school year', 'Autumn'], 0),
    ('Which of these might communities hold to celebrate Victoria Day?', ['Fireworks and community events', 'A snow sculpture contest only', 'A silent day with no activities', 'A day with no celebrations at all'], 0),
    ('Victoria Day is an example of a Canadian ___.', ['Holiday', 'Sport', 'Type of currency', 'Landform'], 0)]),
]),
day(185, [
L('Cinquain Poems: Five Lines Building an Idea',
  'Grade 2 Language strand: a cinquain is a five-line poem that often follows a pattern of word counts or types on each line, building a clear picture of one topic.',
  [('How many lines does a cinquain poem have?', ['Five', 'Two', 'Ten', 'One'], 0),
   ('What does a cinquain poem often build a picture of?', ['One clear topic', 'Ten unrelated topics', 'No topic at all', 'A list of random numbers'], 0),
   ('What might a cinquain poem follow to organize its lines?', ['A pattern of word counts or types', 'No pattern of any kind', 'A pattern of only punctuation', 'A pattern based on colours only'], 0),
   ('Which of these could be a good topic for a cinquain poem?', ['A favourite animal', 'A math equation', 'A blank page', 'A silent letter'], 0),
   ('Why might a poet choose the short cinquain form?', ['To describe a single idea clearly and concisely', 'To write as many unrelated ideas as possible', 'To avoid describing anything', 'Cinquains must always be very long'], 0)]),
M('Money: Estimating Total Cost by Rounding to the Nearest Dollar',
  'Grade 2 Math strand: rounding each item price to the nearest dollar before adding them together gives a quick estimate of the total cost of several items.',
  [('What does rounding prices to the nearest dollar help you find quickly?', ['An estimate of the total cost', 'The exact colour of an item', 'The weight of an item', 'The shape of an item'], 0),
   ('If an item costs 2.85 dollars, what is that rounded to the nearest dollar?', ['3 dollars', '2 dollars', '5 dollars', '10 dollars'], 0),
   ('If an item costs 4.10 dollars, what is that rounded to the nearest dollar?', ['4 dollars', '5 dollars', '3 dollars', '10 dollars'], 0),
   ('Why might someone estimate a total cost before checking out at a store?', ['To make sure they have enough money', 'Estimating costs has no real use', 'To avoid ever paying for anything', 'To make the prices disappear'], 0),
   ('If two items are estimated at about 3 dollars each, about how much would both items cost together?', ['About 6 dollars', 'About 1 dollar', 'About 20 dollars', 'About 0 dollars'], 0)]),
Sc('Ladybugs: Helpful Garden Insects',
   'Grade 2 Science strand: ladybugs are small, round insects with spotted wing covers that help gardens by eating plant pests such as aphids.',
   [('What type of animal is a ladybug?', ['An insect', 'A mammal', 'A reptile', 'A bird'], 0),
    ('What do ladybug wing covers usually look like?', ['Round and spotted', 'Long and striped', 'Square and plain', 'Covered in fur'], 0),
    ('How do ladybugs help gardens?', ['By eating plant pests such as aphids', 'By destroying every plant', 'By making soil disappear', 'By blocking sunlight'], 0),
    ('Ladybugs are an example of an insect that is considered ___ by gardeners.', ['Helpful', 'Dangerous to touch', 'Useless', 'Poisonous to plants'], 0),
    ('Besides its wing covers, what other insect body parts might a ladybug have?', ['Legs and antennae', 'Fur and hooves', 'Gills and fins', 'Feathers and a beak'], 0)]),
SS('Canada at the Olympics: Winter and Summer Games',
   'Grade 2 Social Studies strand: Canadian athletes compete at both the Winter and Summer Olympic Games, representing Canada in sports from hockey and skating to swimming and track.',
   [('In which two kinds of Olympic Games do Canadian athletes compete?', ['Winter and Summer Games', 'Only Spring Games', 'Only Autumn Games', 'Neither kind of Games'], 0),
    ('What might a Canadian athlete wear or carry to show which country they represent?', ['The Canadian flag or team uniform', 'A random flag with no meaning', 'Nothing that shows their country', 'A blank sign'], 0),
    ('Which of these is a Winter Olympic sport Canada is known for?', ['Hockey', 'Surfing', 'Desert racing', 'Beach volleyball only'], 0),
    ('Why might people watch the Olympics to support their countrys athletes?', ['To cheer on athletes representing their country', 'Olympics have no connection to countries', 'People never watch the Olympics', 'Only athletes are allowed to watch'], 0),
    ('The Olympics is best described as an international ___.', ['Sporting event', 'Type of government', 'Kind of currency', 'National holiday'], 0)]),
]),
day(186, [
L('Readers Theatre: Reading Scripts Aloud Together',
  'Grade 2 Language strand: readers theatre is a way of reading a script aloud with expression as a group, with each person reading a different character part instead of acting it out with costumes or props.',
  [('What is readers theatre?', ['Reading a script aloud with expression as a group', 'A silent activity with no talking', 'A type of math worksheet', 'A way of drawing pictures only'], 0),
   ('In readers theatre, what does each person usually read?', ['A different character part', 'The exact same line as everyone else', 'Only stage directions', 'Nothing at all'], 0),
   ('Do readers theatre performers usually need costumes and props?', ['No, they read with expression instead', 'Yes, elaborate costumes are required', 'Only shoes are required', 'Only masks are required'], 0),
   ('Why might readers theatre help build reading skills?', ['It gives practice reading aloud with fluency and expression', 'It removes the need to read any words', 'It only involves silent reading', 'It has no connection to reading'], 0),
   ('Which of these is a script written for a readers theatre performance?', ['A short play with lines for different characters', 'A single math equation', 'A blank page with no words', 'A grocery list'], 0)]),
M('Time: Calculating Age in Years and Months',
  'Grade 2 Math strand: to find someones age in years and months, compare their birth date to todays date, counting full years first and then the remaining months.',
  [('What two dates do you compare to calculate someones age?', ['Their birth date and todays date', 'Two random unrelated dates', 'Only the current year', 'Only the current month'], 0),
   ('If a child was born in March and it is now June of the same year, how many months old are they?', ['3 months', '6 months', '9 months', '1 month'], 0),
   ('What should you count first when calculating age in years and months?', ['Full years', 'Only days', 'Only seconds', 'Only the current month'], 0),
   ('If someone turned 8 years old two months ago, how would you describe their age?', ['8 years and 2 months old', '8 years and 12 months old', '6 years old', '10 years old'], 0),
   ('Why might knowing someones exact age in years and months be useful?', ['It gives a more precise picture of how old someone is', 'Age never needs to be precise', 'Months have no connection to age', 'It replaces the need for a birth date'], 0)]),
Sc('Tsunamis: Giant Waves Caused by Earth Movement',
   'Grade 2 Science strand: a tsunami is a series of giant ocean waves usually caused by an earthquake or other sudden movement under the sea, capable of causing major flooding when it reaches land.',
   [('What is a tsunami?', ['A series of giant ocean waves', 'A gentle ripple in a pond', 'A type of cloud', 'A kind of desert wind'], 0),
    ('What often causes a tsunami?', ['An earthquake or sudden movement under the sea', 'A light breeze', 'A change in leaf colour', 'A single raindrop'], 0),
    ('What can a tsunami cause when it reaches land?', ['Major flooding', 'No effect at all', 'A drought', 'A snowstorm'], 0),
    ('Where do tsunamis begin?', ['Under the sea', 'On top of a mountain', 'Inside a cave', 'In the desert'], 0),
    ('Tsunamis are an example of a natural ___.', ['Hazard connected to ocean movement', 'Type of government', 'Kind of currency', 'National holiday'], 0)]),
SS('Curling: A Canadian Winter Tradition',
   'Grade 2 Social Studies strand: curling is a winter sport played on ice where teams slide heavy stones toward a target, using brooms to help guide the stones path, and is a popular Canadian pastime.',
   [('What surface is curling played on?', ['Ice', 'Sand', 'Grass', 'Water'], 0),
    ('What do curling players slide toward a target?', ['Heavy stones', 'Small balls', 'Wooden blocks', 'Balloons'], 0),
    ('What tool do curling players use to help guide the stones path?', ['A broom', 'A hockey stick', 'A paddle', 'A racket'], 0),
    ('Curling is best described as a popular Canadian ___.', ['Winter sport', 'Summer sport only', 'Type of government', 'Kind of currency'], 0),
    ('Why might sweeping the ice with a broom affect how a curling stone moves?', ['It can change the speed and path of the sliding stone', 'Sweeping has no effect on the stone', 'It stops the stone completely every time', 'It changes the colour of the stone'], 0)]),
]),
day(187, [
L('Language Review: Grammar, Poetry, and Word Study — A Final Grade Two Celebration',
  'Grade 2 Language strand review, and the final Language lesson of the full 187-day Grade 2 curriculum: students revisit collective nouns, silent e, r-controlled vowels, diphthongs, cinquain poems, and readers theatre.',
  [('What does a collective noun name?', ['A group of people, animals, or things acting as one unit', 'A single object only', 'A type of punctuation', 'A silent letter'], 0),
   ('What does a silent e at the end of a word often do?', ['Changes a short vowel sound into a long vowel sound', 'Makes the word disappear', 'Adds a new syllable you can hear', 'Removes all vowels from the word'], 0),
   ('What does an r-controlled vowel mean?', ['The letter r changes how the vowel sounds', 'The vowel is always silent', 'The r is never pronounced', 'The vowel becomes a consonant'], 0),
   ('What is a diphthong?', ['A vowel sound made by gliding between two vowel sounds', 'A silent consonant', 'A punctuation mark', 'A type of sentence'], 0),
   ('What is readers theatre?', ['Reading a script aloud with expression as a group', 'A silent activity with no talking', 'A type of math worksheet', 'A way of drawing pictures only'], 0)]),
M('Math Review: Time, Measurement, Fractions, and Geometry — A Final Grade Two Celebration',
  'Grade 2 Math strand review, and the final Math lesson of the full 187-day Grade 2 curriculum: students revisit the 24-hour clock, volume with unit cubes, benchmark fractions, prisms and pyramids, estimating cost by rounding, and calculating age in years and months.',
  [('How many hours does the 24-hour clock count across a full day?', ['24', '12', '60', '100'], 0),
   ('What does volume measure?', ['How much space a solid shape takes up', 'How heavy an object is', 'How long an object is', 'How loud a sound is'], 0),
   ('Which three benchmark fractions are commonly used?', ['Zero, one-half, and one', 'Two, four, and six', 'Ten, twenty, and thirty', 'One-third, two-thirds, and one'], 0),
   ('How many flat bases does a pyramid have?', ['One', 'Two', 'Zero', 'Six'], 0),
   ('What two dates do you compare to calculate someones age?', ['Their birth date and todays date', 'Two random unrelated dates', 'Only the current year', 'Only the current month'], 0)]),
Sc('Science Review: Animals, Habitats, and Earth Events — A Final Grade Two Celebration',
   'Grade 2 Science strand review, and the final Science lesson of the full 187-day Grade 2 curriculum: students revisit sloths, wolves, elephants, kelp forests, ladybugs, and tsunamis.',
   [('Where do sloths mainly live?', ['In rainforest trees', 'In deep ocean water', 'In frozen arctic ice', 'In dry desert sand'], 0),
    ('What is a group of wolves called?', ['A pack', 'A herd', 'A flock', 'A school'], 0),
    ('What are elephants known for being?', ['The largest land animals on Earth', 'The smallest land animals on Earth', 'Animals that live only underwater', 'Animals with no legs'], 0),
    ('Where does kelp typically grow?', ['From the ocean floor toward the surface', 'On top of mountains', 'In the desert sand', 'Inside caves with no water'], 0),
    ('What often causes a tsunami?', ['An earthquake or sudden movement under the sea', 'A light breeze', 'A change in leaf colour', 'A single raindrop'], 0)]),
SS('Social Studies Review: Geography, Culture, and Canadian Life — A Final Grade Two Celebration',
   'Grade 2 Social Studies strand review, and the final Social Studies lesson of the full 187-day Grade 2 curriculum: students revisit the Canadian Shield, the Arctic Ocean, traditional Indigenous homes, Victoria Day, the Olympics in Canada, and curling.',
   [('What is the Canadian Shield mostly made of?', ['Very old, hard rock', 'Soft sand only', 'Ice that never melts', 'Ocean water'], 0),
    ('Which part of Canada does the Arctic Ocean border?', ['Northern Canada', 'Southern Canada only', 'No part of Canada', 'Only inland lakes'], 0),
    ('What is a longhouse?', ['A long traditional home shared by several families', 'A type of boat', 'A modern apartment building', 'A kind of bridge'], 0),
    ('In which month is Victoria Day celebrated?', ['May', 'July', 'December', 'October'], 0),
    ('What surface is curling played on?', ['Ice', 'Sand', 'Grass', 'Water'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_181_187)
    append_to(2, g2_181_187)
