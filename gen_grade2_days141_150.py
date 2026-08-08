#!/usr/bin/env python3
"""Grade 2, Days 141-150 -- twelfth batch, extending Grade 2 past Day 140
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by the video-backfill task)

Topics chosen to avoid overlap with existing Grade 2 Days 1-140 (dumped
and checked against data/grade2.json before writing, which already
densely covers nearly the full grade 2 ELA, math, science, and social
studies curriculum): three-letter blends thr/squ/spr, timelines,
invitations, persuasive techniques, setting a purpose before reading,
rising action and climax, vivid verbs, compound-complex sentences, and
graphic organizers for Language. Long division, adding fractions with
the same denominator, stem-and-leaf plots, classifying triangles,
elapsed time word problems, making change from five and ten dollar
bills, patterns in the multiplication table, converting grams to
kilograms, and coordinate grids for Math. Our sense of balance, density,
nuclear energy, animal tracks, vaccines, desert plants, ice ages,
beavers, and wetlands for Science. Our senate, the Order of Canada, our
school board, world currency, land acknowledgements, our provincial
legislature, our school yearbook, Canadian lighthouses, and our local
fire hall for Social Studies. Day 150 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior 10-day
batch. No embedded ASCII double-quote or straight apostrophe characters
are used anywhere in title/summary/quiz text -- contractions and
possessives are avoided entirely (or rewritten without the apostrophe)
to keep the generated .ts string literals valid.
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


g2_141_150 = [
day(141, [
L('Blends: thr, squ, and spr',
  'Grade 2 Language strand: three-letter consonant blends like thr, squ, and spr appear at the start of words such as three, squirrel, and spring.',
  [('Which word begins with the thr blend?', ['Three', 'Squirrel', 'Spring', 'Sun'], 0),
   ('Which word begins with the squ blend?', ['Three', 'Squirrel', 'Spring', 'Sit'], 1),
   ('Which word begins with the spr blend?', ['Three', 'Squirrel', 'Spring', 'Stop'], 2),
   ('How many letters are in a three-letter blend like spr?', ['Two', 'Three', 'Four', 'Five'], 1),
   ('Which of these words has a three-letter blend?', ['Throw', 'Cat', 'Sun', 'Dog'], 0)]),
M('Long Division: Dividing Two-Digit Numbers by One-Digit Numbers',
  'Grade 2 Math strand: students practise dividing a two-digit number by a one-digit number, sharing the total into equal groups.',
  [('What is 24 divided by 4?', ['4', '5', '6', '8'], 2),
   ('What is 36 divided by 6?', ['4', '5', '6', '7'], 2),
   ('What is 42 divided by 7?', ['5', '6', '7', '8'], 1),
   ('When we divide a two-digit number, we are sharing it into ___.', ['Equal groups', 'Random groups', 'One big group', 'No groups'], 0),
   ('What is 48 divided by 8?', ['5', '6', '7', '8'], 1)]),
Sc('Our Sense of Balance: The Inner Ear',
   'Grade 2 Science strand: our sense of balance is controlled by a part deep inside our ear, helping us stand, walk, and stay steady without falling.',
   [('What sense helps us stand and walk without falling?', ['Sense of balance', 'Sense of taste', 'Sense of smell', 'Sense of hearing'], 0),
    ('Where in our body is our sense of balance controlled?', ['Deep inside our ear', 'In our elbow', 'In our hair', 'In our teeth'], 0),
    ('Which activity relies heavily on our sense of balance?', ['Riding a bicycle', 'Tasting food', 'Smelling a flower', 'Listening to music'], 0),
    ('Our sense of balance helps prevent us from ___.', ['Falling over', 'Hearing sounds', 'Tasting food', 'Smelling things'], 0),
    ('Why might spinning in circles make us feel dizzy?', ['It confuses the balance system in our inner ear', 'It has no effect on our body', 'It makes our eyes change colour', 'It stops our heart from beating'], 0)]),
SS('Our Senate: Another Part of Canadas Government',
   'Grade 2 Social Studies strand: the Senate is part of Canadas government, made up of appointed senators who review and can suggest changes to new laws.',
   [('What is the Senate?', ['A part of Canadas government', 'A group that reviews new laws', 'A city council', 'A sports league'], 0),
    ('How do people usually become senators, unlike members of Parliament?', ['They are appointed, not elected', 'They are elected by the public', 'They are chosen by a lottery', 'They inherit the position'], 0),
    ('What is one job of the Senate?', ['Reviewing and suggesting changes to new laws', 'Coaching sports teams', 'Running local schools', 'Delivering mail'], 0),
    ('The Senate is part of which level of government?', ['The federal government', 'A single citys government', 'A school government', 'A private business'], 0),
    ('Why might it be helpful to have more than one group review a new law?', ['It helps catch mistakes and improve the law', 'It has no benefit at all', 'It slows down government for no reason', 'It removes the need for any laws'], 0)]),
]),
day(142, [
L('Text Features: Timelines',
  'Grade 2 Language strand: a timeline is a text feature that shows events in the order they happened, often with dates along a line.',
  [('What does a timeline show?', ['Events in the order they happened', 'A list of characters', 'A map of a place', 'A recipe'], 0),
   ('What is often included along a timeline?', ['Dates', 'Colours', 'Songs', 'Weather'], 0),
   ('Why might an author use a timeline in a nonfiction book?', ['To help readers understand the order of events', 'To confuse the reader', 'To remove all the facts', 'To make the book shorter with less detail'], 0),
   ('A timeline usually reads from ___.', ['Earliest to latest', 'Latest to earliest only', 'Random order', 'Top to bottom only'], 0),
   ('Which subject might use a timeline to show important events?', ['History', 'Colouring', 'Cooking only', 'Singing'], 0)]),
M('Fractions: Adding Fractions with the Same Denominator',
  'Grade 2 Math strand: to add fractions with the same denominator, we add the numerators together and keep the denominator the same.',
  [('What is 1/4 + 2/4?', ['2/4', '3/4', '4/4', '1/2'], 1),
   ('What is 2/5 + 1/5?', ['3/5', '3/10', '2/10', '1/5'], 0),
   ('When adding fractions with the same denominator, what stays the same?', ['The denominator', 'The numerator', 'Both numbers', 'Neither number'], 0),
   ('What is 3/8 + 2/8?', ['5/8', '5/16', '1/8', '6/8'], 0),
   ('What is 1/6 + 3/6?', ['4/6', '4/12', '3/6', '2/6'], 0)]),
Sc('Density: Why Some Things Float Higher Than Others',
   'Grade 2 Science strand: density describes how tightly packed the matter in an object is, and it helps explain why some objects float higher or sink faster than others.',
   [('What does density describe?', ['How tightly packed matter is in an object', 'The colour of an object', 'The taste of an object', 'The sound an object makes'], 0),
    ('Which object would likely have higher density, a rock or a feather of the same size?', ['A rock', 'A feather', 'They are always equal', 'Neither has density'], 0),
    ('Why might one object float higher in water than another?', ['It has a lower density', 'It has a higher density', 'It is a different colour', 'It makes more noise'], 0),
    ('What happens to an object with very high density when placed in water?', ['It is more likely to sink', 'It always floats on top', 'It disappears', 'It changes colour'], 0),
    ('Understanding density helps scientists explain why ships made of metal can still ___.', ['Float', 'Sink immediately', 'Disappear', 'Change shape'], 0)]),
SS('The Order of Canada: Honouring Outstanding Canadians',
   'Grade 2 Social Studies strand: the Order of Canada is a special honour given to Canadians who have made an outstanding contribution to their community or country.',
   [('What is the Order of Canada?', ['A special honour for outstanding Canadians', 'A type of holiday', 'A sports league', 'A kind of coin'], 0),
    ('Who might receive the Order of Canada?', ['Someone who made an outstanding contribution', 'Anyone chosen at random', 'Only professional athletes', 'Only politicians'], 0),
    ('Why does Canada give out this kind of honour?', ['To recognize people who have helped their community or country', 'It has no purpose', 'To give away free prizes', 'To replace elections'], 0),
    ('The Order of Canada could be given to someone who worked in ___.', ['Many different fields, like science or the arts', 'Only one specific job', 'No particular field', 'Only professional sports'], 0),
    ('Recognizing outstanding Canadians can help inspire others to ___.', ['Make a positive difference too', 'Stop trying to help others', 'Ignore their community', 'Avoid working hard'], 0)]),
]),
day(143, [
L('Writing an Invitation: Sharing Details Clearly',
  'Grade 2 Language strand: an invitation shares important details about an event, like the date, time, and place, so people know how to join.',
  [('What is the purpose of an invitation?', ['To share details about an event', 'To tell a made-up story', 'To list facts about animals', 'To give a weather report'], 0),
   ('Which detail should always be included in an invitation?', ['The date and time of the event', 'A random riddle', 'A grocery list', 'A weather forecast'], 0),
   ('Why is it important for an invitation to be clear?', ['So people know exactly how to join the event', 'Clarity does not matter for invitations', 'To confuse the reader on purpose', 'To make the event a surprise from everyone'], 0),
   ('Which of these might also appear on an invitation?', ['The location of the event', 'A math equation', 'A weather forecast for another country', 'A recipe for soup'], 0),
   ('An invitation is an example of writing that is meant to ___.', ['Inform people about an event', 'Entertain with a made-up story', 'Persuade someone to buy something', 'Describe a scientific process'], 0)]),
M('Data: Stem-and-Leaf Plots',
  'Grade 2 Math strand: a stem-and-leaf plot organizes numbers by splitting each one into a stem, the larger digits, and a leaf, the last digit.',
  [('What does a stem-and-leaf plot organize?', ['Numbers, split into stems and leaves', 'Colours', 'Shapes', 'Letters'], 0),
   ('In the number 23, what would the stem usually be?', ['2', '3', '23', '0'], 0),
   ('In the number 23, what would the leaf usually be?', ['2', '3', '23', '0'], 1),
   ('Why might we use a stem-and-leaf plot instead of a list of numbers?', ['It helps organize data so it is easier to read', 'It hides the numbers completely', 'It removes the need for numbers', 'It only works with letters'], 0),
   ('A stem-and-leaf plot is a way to organize and display ___.', ['Data', 'Colours', 'Story characters', 'Weather patterns'], 0)]),
Sc('Nuclear Energy: Power from Atoms',
   'Grade 2 Science strand: nuclear energy is a powerful form of energy that comes from splitting tiny particles called atoms, and it can be used to make electricity.',
   [('What does nuclear energy come from?', ['Splitting tiny particles called atoms', 'Burning wood', 'Wind blowing', 'Sunlight only'], 0),
    ('What can nuclear energy be used to make?', ['Electricity', 'Rain', 'Wind', 'Rocks'], 0),
    ('What are the tiny particles split to release nuclear energy called?', ['Atoms', 'Cells', 'Molecules of water only', 'Rocks'], 0),
    ('Nuclear energy is considered a powerful source of ___.', ['Energy', 'Food', 'Water', 'Sound'], 0),
    ('Why do scientists and engineers need to be very careful when working with nuclear energy?', ['Because it is a very powerful form of energy', 'Because it has no power at all', 'Because it is the same as solar energy', 'Because it only works on cloudy days'], 0)]),
SS('Our School Board: Supporting Many Schools',
   'Grade 2 Social Studies strand: a school board oversees many schools in an area, helping make decisions about education for a whole region.',
   [('What does a school board oversee?', ['Many schools in an area', 'Just one single classroom', 'Only sports teams', 'Only school buses'], 0),
    ('Does a school board oversee just one school or many schools?', ['Many schools', 'Just one school', 'No schools at all', 'Only private homes'], 0),
    ('Why is a school board an important part of education?', ['It helps make decisions that support many schools', 'It has no role in education', 'It only decides lunch menus', 'It replaces teachers completely'], 0),
    ('Which of these might a school board help decide?', ['How schools in the area are run', 'What every student eats for breakfast at home', 'The colour of every students shoes', 'Personal weekend plans for families'], 0),
    ('A school board works to support ___ across a region.', ['Education', 'Only sports', 'Only art class', 'Nothing important'], 0)]),
]),
day(144, [
L('Persuasive Techniques: Loaded Words and Bandwagon Appeals',
  'Grade 2 Language strand: persuasive writers sometimes use loaded words, which carry strong feelings, or bandwagon appeals, which suggest everyone else agrees, to convince readers.',
  [('What are loaded words?', ['Words that carry strong feelings', 'Words with no meaning', 'Words that rhyme', 'Words that are always true'], 0),
   ('What is a bandwagon appeal?', ['Suggesting everyone else agrees, so you should too', 'A type of vehicle', 'A type of song', 'A math strategy'], 0),
   ('Why might a writer use these persuasive techniques?', ['To try to convince readers to agree with them', 'To confuse the reader on purpose', 'To share only true facts with no opinion', 'To avoid persuading anyone'], 0),
   ('Which is an example of a bandwagon appeal?', ['Everyone is choosing this, so you should too', 'The sky is blue', 'Two plus two equals four', 'Water freezes at zero degrees'], 0),
   ('Recognizing persuasive techniques helps readers think ___ about what they read.', ['Carefully and critically', 'Without any thought', 'Only about the pictures', 'Only about the title'], 0)]),
M('Geometry: Classifying Triangles by Sides and Angles',
  'Grade 2 Math strand: triangles can be classified by their sides, like equilateral or scalene, or by their angles, like right or obtuse.',
  [('What is a triangle with three equal sides called?', ['Equilateral', 'Scalene', 'Isosceles', 'Obtuse'], 0),
   ('What is a triangle with no equal sides called?', ['Scalene', 'Equilateral', 'Isosceles', 'Right'], 0),
   ('What is a triangle with one 90 degree angle called?', ['A right triangle', 'An equilateral triangle', 'A scalene triangle', 'An obtuse triangle'], 0),
   ('How many sides does every triangle have?', ['2', '3', '4', '5'], 1),
   ('Classifying shapes by their sides and angles helps us understand their ___.', ['Properties', 'Colour', 'Weight', 'Smell'], 0)]),
Sc('Animal Tracks: Reading Footprints in Snow and Mud',
   'Grade 2 Science strand: many animals leave tracks, or footprints, in snow or mud, and scientists can study the shape and pattern of tracks to identify which animal made them.',
   [('What are animal tracks?', ['Footprints animals leave behind', 'A type of animal food', 'A kind of nest', 'A sound animals make'], 0),
    ('Where can animal tracks often be seen most clearly?', ['In snow or soft mud', 'On a sunny sidewalk', 'In the middle of the ocean', 'In the sky'], 0),
    ('How can scientists use the shape of a track?', ['To help identify which animal made it', 'To tell the animals favourite colour', 'To predict the weather', 'To calculate the animals age exactly'], 0),
    ('Which of these might leave visible tracks in snow?', ['A rabbit', 'A goldfish', 'A whale', 'A jellyfish'], 0),
    ('Studying animal tracks is one way scientists learn about animals without ___.', ['Seeing the animal directly', 'Any effort at all', 'Using their eyes', 'Leaving their home'], 0)]),
SS('World Currency: Comparing Money From Different Countries',
   'Grade 2 Social Studies strand: different countries use different kinds of money, called currency, and comparing currencies helps us understand how trade and travel work around the world.',
   [('What is the money used by a country called?', ['Currency', 'Language', 'Anthem', 'Symbol'], 0),
    ('Do all countries around the world use the exact same currency?', ['No, different countries use different currency', 'Yes, every country uses the same money', 'Money is not used anywhere', 'Only Canada uses money'], 0),
    ('Why might a traveller need to exchange money when visiting another country?', ['Because that country uses a different currency', 'Money never changes anywhere', 'All countries ban money', 'Currency is only used in stores'], 0),
    ('Comparing currencies from different countries can help us understand ___.', ['Trade and travel around the world', 'Nothing important', 'Only colours', 'Only shapes'], 0),
    ('Which of these is an example of a countrys currency?', ['The Canadian dollar', 'A national anthem', 'A national flag', 'A national bird'], 0)]),
]),
day(145, [
L('Reading Strategy: Setting a Purpose Before Reading',
  'Grade 2 Language strand: setting a purpose before reading means thinking about why we are reading something, such as to learn facts or to enjoy a story.',
  [('What does it mean to set a purpose before reading?', ['Thinking about why we are reading something', 'Skipping the whole book without reading', 'Reading with no thought at all', 'Ignoring the title and cover'], 0),
   ('Which is an example of a purpose for reading?', ['Reading to learn facts about animals', 'Reading with your eyes closed', 'Reading a book upside down', 'Reading without opening the book'], 0),
   ('Why is it helpful to set a purpose before reading?', ['It helps us focus on the most important parts', 'It makes reading pointless', 'It has no benefit at all', 'It prevents us from understanding the text'], 0),
   ('If your purpose is to learn facts, which kind of book would you likely choose?', ['A nonfiction book', 'A fictional fairy tale', 'A joke book', 'A blank notebook'], 0),
   ('Setting a purpose before reading is a strategy that helps improve our ___.', ['Understanding of the text', 'Ability to ignore the text', 'Handwriting', 'Drawing skills'], 0)]),
M('Time: Solving Elapsed Time Word Problems',
  'Grade 2 Math strand: elapsed time word problems ask us to figure out how much time has passed between a start time and an end time.',
  [('If a movie starts at 2:00 and ends at 4:00, how much time passed?', ['1 hour', '2 hours', '3 hours', '4 hours'], 1),
   ('If recess starts at 10:15 and ends at 10:30, how many minutes passed?', ['5 minutes', '10 minutes', '15 minutes', '20 minutes'], 2),
   ('What do we call the amount of time that passes between a start and end time?', ['Elapsed time', 'Start time', 'End time', 'No time'], 0),
   ('If school starts at 9:00 and ends at 3:00, how many hours is that?', ['4 hours', '5 hours', '6 hours', '7 hours'], 2),
   ('To solve an elapsed time problem, we need to know the ___.', ['Start time and end time', 'Only the start time', 'Only the end time', 'Neither time'], 0)]),
Sc('Vaccines: Helping Our Body Fight Disease',
   'Grade 2 Science strand: vaccines help our immune system learn to recognize and fight off certain diseases before we ever get sick from them.',
   [('What do vaccines help our body do?', ['Recognize and fight off certain diseases', 'Grow taller', 'See better', 'Hear better'], 0),
    ('Which body system do vaccines work with?', ['The immune system', 'The skeletal system', 'The digestive system', 'The circulatory system only'], 0),
    ('Why might someone get a vaccine before they are sick?', ['So their body can learn to fight the disease ahead of time', 'Vaccines only work after someone is already sick', 'Vaccines have no effect at all', 'To make someone sick on purpose'], 0),
    ('Vaccines are an example of how science helps us stay ___.', ['Healthy', 'Confused', 'Unwell', 'Unaware'], 0),
    ('Which of these best describes what a vaccine does over time?', ['Helps the immune system remember how to fight a disease', 'Removes the immune system completely', 'Has no connection to the immune system', 'Makes the body forget how to fight disease'], 0)]),
SS('Land Acknowledgements: Respecting Indigenous Territory',
   'Grade 2 Social Studies strand: a land acknowledgement is a respectful statement recognizing that a place was, and often still is, the traditional territory of Indigenous peoples.',
   [('What is a land acknowledgement?', ['A respectful statement about Indigenous territory', 'A type of map', 'A kind of song', 'A weather report'], 0),
    ('What does a land acknowledgement recognize?', ['That a place was, and still is, Indigenous territory', 'A random fact about weather', 'A sports team', 'A type of food'], 0),
    ('Where might you hear a land acknowledgement given?', ['At the start of a school assembly or event', 'Only in outer space', 'Never anywhere', 'Only in other countries'], 0),
    ('Why do communities share land acknowledgements?', ['To show respect for Indigenous peoples and their history', 'They have no meaning at all', 'To ignore Indigenous history', 'To replace all history lessons'], 0),
    ('A land acknowledgement is one way people can show ___.', ['Respect and awareness', 'Disrespect', 'Confusion', 'Carelessness'], 0)]),
]),
day(146, [
L('Story Structure: Rising Action and Climax',
  'Grade 2 Language strand: rising action is the part of a story where excitement builds, leading up to the climax, the most exciting or important moment of the story.',
  [('What is rising action?', ['The part of a story where excitement builds', 'The very beginning of a story', 'The title of a story', 'The back cover of a book'], 0),
   ('What is the climax of a story?', ['The most exciting or important moment', 'The first sentence', 'The list of characters', 'The books price'], 0),
   ('Does rising action happen before or after the climax?', ['Before', 'After', 'At the very end', 'It never happens'], 0),
   ('Why is rising action important in a story?', ['It builds excitement leading to the climax', 'It has no purpose in a story', 'It always comes after the ending', 'It removes the main problem'], 0),
   ('Which of these describes the climax of a story?', ['The most tense or exciting turning point', 'The very first page', 'The dedication page', 'The table of contents'], 0)]),
M('Money: Making Change from Five and Ten Dollar Bills',
  'Grade 2 Math strand: students practise figuring out how much change to give back when someone pays with a five or ten dollar bill.',
  [('If something costs 3 dollars and you pay with a 5 dollar bill, how much change do you get?', ['1 dollar', '2 dollars', '3 dollars', '4 dollars'], 1),
   ('If something costs 7 dollars and you pay with a 10 dollar bill, how much change do you get?', ['2 dollars', '3 dollars', '4 dollars', '5 dollars'], 1),
   ('If something costs 4 dollars and you pay with a 5 dollar bill, how much change do you get?', ['1 dollar', '2 dollars', '3 dollars', '4 dollars'], 0),
   ('Making change correctly is important because it makes sure a purchase is ___.', ['Fair and accurate', 'Confusing', 'Unfair', 'Impossible'], 0),
   ('If something costs 6 dollars and you pay with a 10 dollar bill, how much change do you get?', ['2 dollars', '3 dollars', '4 dollars', '5 dollars'], 2)]),
Sc('Desert Plants: Cacti and Succulents',
   'Grade 2 Science strand: desert plants like cacti and succulents store water in their thick stems and leaves so they can survive long periods without rain.',
   [('What do cacti and succulents store water in?', ['Their thick stems and leaves', 'The air around them', 'The wind', 'The clouds'], 0),
    ('Why do desert plants need to store water?', ['To survive long periods without rain', 'They never need water', 'To grow taller instantly', 'To change colour'], 0),
    ('What is a cactus an example of?', ['A desert plant', 'An ocean animal', 'A rainforest tree', 'A type of rock'], 0),
    ('Which feature helps some desert plants avoid losing too much water?', ['Thick, waxy skin', 'Thin, papery leaves', 'No leaves and no stem at all', 'Constant rainfall'], 0),
    ('Desert plants like cacti are well adapted to living in a place that is usually ___.', ['Hot and dry', 'Cold and wet', 'Underwater', 'Covered in snow'], 0)]),
SS('Our Provincial Legislature: Where Laws Are Made',
   'Grade 2 Social Studies strand: the provincial legislature is a building where elected leaders meet to discuss and create laws for the province.',
   [('What happens at a provincial legislature?', ['Elected leaders discuss and create laws', 'Students take a math test', 'Food is sold to the public', 'Movies are shown to visitors'], 0),
    ('Who works at a provincial legislature?', ['Elected leaders, including the premier', 'Only firefighters', 'Only doctors', 'Only bus drivers'], 0),
    ('Why is a provincial legislature an important building?', ['Important laws and decisions are made there', 'It has no real purpose', 'It is only used for sports games', 'It is closed at all times'], 0),
    ('Which of these might happen inside a provincial legislature?', ['A debate about a new provincial law', 'A birthday party for one family', 'A private vacation', 'Nothing important at all'], 0),
    ('A provincial legislature helps a province by creating ___.', ['Laws and important decisions', 'Only weather forecasts', 'Only sports schedules', 'Nothing useful'], 0)]),
]),
day(147, [
L('Word Choice: Vivid Verbs Instead of Said',
  'Grade 2 Language strand: writers can replace the word said with more vivid verbs, like whispered, shouted, or exclaimed, to show more about how a character speaks.',
  [('What is a vivid verb?', ['A specific, descriptive action word', 'A word with no meaning', 'A type of punctuation', 'A type of noun'], 0),
   ('Which of these is a vivid verb that could replace said?', ['Whispered', 'The', 'And', 'Very'], 0),
   ('Why might a writer choose whispered instead of said?', ['It shows more about how the character spoke', 'It has the exact same meaning with no extra detail', 'It confuses the reader on purpose', 'It removes all dialogue from the story'], 0),
   ('Which sentence uses a vivid verb?', ['She shouted with excitement', 'She said something', 'She talked', 'She spoke'], 0),
   ('Using vivid verbs instead of plain words helps make writing more ___.', ['Interesting and descriptive', 'Boring', 'Confusing', 'Short with no detail'], 0)]),
M('Number Patterns: Patterns in the Multiplication Table',
  'Grade 2 Math strand: students look for patterns in the multiplication table, such as how the 2s row is always even, or how rows and columns mirror each other.',
  [('Are the numbers in the 2 times table always even or always odd?', ['Always even', 'Always odd', 'Sometimes even and sometimes odd', 'Neither even nor odd'], 0),
   ('In a multiplication table, the 3 row and the 3 column contain ___.', ['The same set of numbers', 'Completely different numbers', 'Only odd numbers', 'Only the number 3'], 0),
   ('Why might noticing patterns in a multiplication table be helpful?', ['It helps us remember multiplication facts more easily', 'It makes multiplication impossible to learn', 'It has no use at all', 'It only works for addition'], 0),
   ('What pattern can you find in the 10 times table?', ['Every answer ends in a zero', 'Every answer is odd', 'Every answer is the same number', 'There is no pattern at all'], 0),
   ('Looking for patterns in math helps us become better at ___.', ['Solving problems', 'Drawing pictures', 'Spelling words', 'Singing songs'], 0)]),
Sc('Ice Ages: When Earth Was Covered in Ice',
   'Grade 2 Science strand: an ice age is a long period of time when much of the Earth was covered by thick sheets of ice called glaciers.',
   [('What is an ice age?', ['A long period when much of Earth was covered in ice', 'A single cold day', 'A type of animal', 'A kind of rock'], 0),
    ('What covered much of the Earth during an ice age?', ['Thick sheets of ice called glaciers', 'Warm ocean water', 'Sand and desert', 'Rainforest trees'], 0),
    ('How long did ice ages usually last?', ['A very long period of time', 'Just one single day', 'One hour', 'A few minutes'], 0),
    ('What can scientists study to learn about past ice ages?', ['Fossils and layers of ice or rock', 'Only todays weather', 'Only modern buildings', 'Nothing at all'], 0),
    ('Ice ages remind us that Earths climate has ___ over a very long time.', ['Changed', 'Never changed', 'Stayed exactly the same forever', 'Disappeared completely'], 0)]),
SS('Our School Yearbook: Remembering the School Year',
   'Grade 2 Social Studies strand: a school yearbook is a book filled with photos and memories that helps students remember their school year.',
   [('What is a school yearbook?', ['A book filled with photos and memories from the school year', 'A math textbook', 'A list of school rules only', 'A calendar with no pictures'], 0),
    ('Why might a school create a yearbook?', ['To help students remember the school year', 'To replace all textbooks', 'It has no real purpose', 'To confuse students'], 0),
    ('Which of these might appear in a school yearbook?', ['Class photos', 'A grocery list', 'A weather forecast', 'A car manual'], 0),
    ('A yearbook can help students look back on their year and remember ___.', ['Special moments and friends', 'Nothing important', 'Only test scores', 'Only homework assignments'], 0),
    ('Yearbooks are usually created ___ during the school year.', ['Once, near the end', 'Every single day', 'Never', 'Only in summer'], 0)]),
]),
day(148, [
L('Compound-Complex Sentences: Combining Three Ideas',
  'Grade 2 Language strand: a compound-complex sentence combines two complete ideas with a joining word, plus an extra dependent idea, all in one sentence.',
  [('What does a compound-complex sentence combine?', ['Two complete ideas and an extra dependent idea', 'Only a single word', 'No punctuation at all', 'Only a title'], 0),
   ('Why might a writer choose to use a compound-complex sentence?', ['To smoothly combine multiple related ideas', 'To make the sentence disappear', 'To remove all meaning from the sentence', 'To confuse the reader on purpose'], 0),
   ('Which of these is a feature of a compound-complex sentence?', ['It joins more than one complete idea together', 'It never has a verb', 'It is always exactly one word', 'It cannot have any punctuation'], 0),
   ('A compound-complex sentence is generally ___ than a simple sentence.', ['Longer and more detailed', 'Always shorter', 'Exactly the same length', 'Impossible to write'], 0),
   ('Combining ideas smoothly in a sentence can help make writing feel more ___.', ['Connected and clear', 'Confusing', 'Choppy and broken', 'Meaningless'], 0)]),
M('Measurement: Converting Grams to Kilograms',
  'Grade 2 Math strand: students learn that 1000 grams equal 1 kilogram, and practise converting between the two units.',
  [('How many grams are in one kilogram?', ['10', '100', '1000', '10000'], 2),
   ('If something weighs 2000 grams, how many kilograms is that?', ['1', '2', '3', '20'], 1),
   ('Which unit would we usually use to weigh a small paperclip?', ['Grams', 'Kilograms', 'Litres', 'Metres'], 0),
   ('Which unit would we usually use to weigh a large bag of rice?', ['Kilograms', 'Grams only', 'Millilitres', 'Centimetres'], 0),
   ('Knowing that 1000 grams equal 1 kilogram helps us ___ between units.', ['Convert', 'Confuse', 'Ignore', 'Erase'], 0)]),
Sc('Beavers: Natures Engineers',
   'Grade 2 Science strand: beavers are known as natures engineers because they build dams and lodges using trees, branches, and mud to change their habitat.',
   [('Why are beavers sometimes called natures engineers?', ['They build dams and lodges to change their habitat', 'They fly through the air', 'They live only in trees', 'They cannot swim'], 0),
    ('What materials do beavers use to build a dam?', ['Trees, branches, and mud', 'Rocks only', 'Ice only', 'Sand only'], 0),
    ('What does a beaver dam do to a habitat?', ['Changes the flow of water, often creating a pond', 'Has no effect on the habitat', 'Destroys all nearby plants instantly', 'Turns the area into a desert'], 0),
    ('What body part helps a beaver cut down trees?', ['Its strong front teeth', 'Its tail', 'Its claws only', 'Its nose'], 0),
    ('Beavers changing their habitat by building dams is an example of ___.', ['An animal shaping its environment', 'An animal with no effect on nature', 'A type of weather', 'A type of rock formation'], 0)]),
SS('Canadian Lighthouses: Guiding Ships Safely',
   'Grade 2 Social Studies strand: lighthouses along Canadas coasts use bright lights to help guide ships safely and warn them away from rocky shores.',
   [('What is the main purpose of a lighthouse?', ['To help guide ships safely', 'To provide housing for fish', 'To grow crops', 'To collect rainwater'], 0),
    ('What do lighthouses use to help guide ships?', ['A bright light', 'Loud music', 'Colourful flags only', 'Smoke signals only'], 0),
    ('Where are lighthouses usually built?', ['Along coasts, near rocky shores or harbours', 'In the middle of a city', 'On top of a mountain far from water', 'Inside a forest'], 0),
    ('Why might a lighthouse warn ships away from certain areas?', ['To help ships avoid dangerous rocky shores', 'Lighthouses have no real purpose', 'To confuse sailors on purpose', 'To stop all ships from ever sailing'], 0),
    ('Lighthouses are an important part of keeping people who travel by ___ safe.', ['Water', 'Air', 'Land only', 'Space'], 0)]),
]),
day(149, [
L('Graphic Organizers: Mapping Out Our Ideas',
  'Grade 2 Language strand: a graphic organizer is a visual tool, like a web or a chart, that helps writers plan and organize their ideas before writing.',
  [('What is a graphic organizer?', ['A visual tool for planning and organizing ideas', 'A type of made-up story', 'A punctuation mark', 'A math equation'], 0),
   ('Why might a writer use a graphic organizer before writing?', ['To plan and organize their ideas clearly', 'To skip planning entirely', 'To make writing more confusing', 'To remove all their ideas completely'], 0),
   ('Which of these is an example of a graphic organizer?', ['A web with connected ideas', 'A grocery list with no structure', 'A single random word', 'A blank page with nothing on it'], 0),
   ('A graphic organizer can help a writer see how their ideas ___.', ['Connect to each other', 'Disappear completely', 'Have no relationship at all', 'Cannot be organized'], 0),
   ('Using a graphic organizer before writing is a helpful step in the writing ___.', ['Process', 'Ending', 'Title', 'Font'], 0)]),
M('Coordinate Grids: Plotting Points on a Grid',
  'Grade 2 Math strand: students learn to plot points on a coordinate grid using two numbers, moving across and then up to find the exact spot.',
  [('What two numbers are used to plot a point on a coordinate grid?', ['A horizontal number and a vertical number', 'Only one number', 'Three numbers', 'No numbers at all'], 0),
   ('Which direction do we usually move first when plotting a point on a grid?', ['Across, then up', 'Up, then across', 'Diagonally only', 'We never move'], 0),
   ('Why are coordinate grids useful in math?', ['They help us find an exact location', 'They have no real use', 'They only work with letters', 'They remove the need for numbers'], 0),
   ('A coordinate grid is made up of a horizontal line and a ___ line.', ['Vertical', 'Diagonal', 'Curved', 'Dotted'], 0),
   ('Plotting points on a grid can help us create simple ___.', ['Maps or pictures', 'Songs', 'Stories with no numbers', 'Recipes'], 0)]),
Sc('Wetlands: A Habitat Between Land and Water',
   'Grade 2 Science strand: a wetland is a special habitat where the land is covered by shallow water for at least part of the year, supporting many plants and animals.',
   [('What is a wetland?', ['A habitat where land is covered by shallow water', 'A dry desert', 'A tall mountain', 'A frozen glacier'], 0),
    ('What kind of living things does a wetland often support?', ['Many plants and animals', 'No living things at all', 'Only rocks', 'Only sand'], 0),
    ('Why are wetlands considered an important type of habitat?', ['They support a wide variety of plants and animals', 'They have no living things in them', 'They are always completely dry', 'They cannot support any life'], 0),
    ('Which of these might you find living in a wetland?', ['Frogs and ducks', 'Camels', 'Polar bears', 'Cactus plants'], 0),
    ('A wetland is a habitat found between ___.', ['Land and water', 'Sky and space', 'Ice and fire', 'Rock and sand only'], 0)]),
SS('Our Local Fire Hall: Where Firefighters Prepare',
   'Grade 2 Social Studies strand: the local fire hall is where firefighters keep their trucks and equipment ready and train so they can respond quickly to emergencies.',
   [('What do firefighters keep ready at the fire hall?', ['Their trucks and equipment', 'Only food', 'Only books', 'Only toys'], 0),
    ('Why do firefighters train regularly at the fire hall?', ['So they can respond quickly to emergencies', 'Training has no purpose for firefighters', 'To avoid ever helping anyone', 'To make emergencies happen more often'], 0),
    ('What is the main purpose of a fire hall?', ['To be a base where firefighters prepare and respond from', 'To sell groceries', 'To teach math classes', 'To show movies to the public'], 0),
    ('Which of these might be found inside a fire hall?', ['A fire truck', 'A swimming pool', 'A movie theatre', 'A shopping mall'], 0),
    ('Having a well prepared fire hall helps keep a community ___.', ['Safer', 'More confused', 'Less prepared', 'Unaware of emergencies'], 0)]),
]),
day(150, [
L('Language Review: Text Features, Persuasion, and Sentence Craft',
  'Grade 2 Language strand review: students revisit three-letter blends, timelines, invitations, persuasive techniques, story structure, vivid verbs, compound-complex sentences, and graphic organizers.',
  [('Which word begins with the thr blend?', ['Three', 'Squirrel', 'Spring', 'Sun'], 0),
   ('What does a timeline show?', ['Events in the order they happened', 'A list of characters', 'A map of a place', 'A recipe'], 0),
   ('What is a bandwagon appeal?', ['Suggesting everyone else agrees, so you should too', 'A type of vehicle', 'A type of song', 'A math strategy'], 0),
   ('What is the climax of a story?', ['The most exciting or important moment', 'The first sentence', 'The list of characters', 'The books price'], 0),
   ('What is a graphic organizer?', ['A visual tool for planning and organizing ideas', 'A type of made-up story', 'A punctuation mark', 'A math equation'], 0)]),
M('Math Review: Division, Fractions, Data, and Measurement',
  'Grade 2 Math strand review: students revisit long division, adding fractions, stem-and-leaf plots, classifying triangles, elapsed time, making change, patterns, and measurement conversions.',
  [('What is 24 divided by 4?', ['4', '5', '6', '8'], 2),
   ('What is 1/4 + 2/4?', ['2/4', '3/4', '4/4', '1/2'], 1),
   ('What is a triangle with three equal sides called?', ['Equilateral', 'Scalene', 'Isosceles', 'Obtuse'], 0),
   ('If something costs 3 dollars and you pay with a 5 dollar bill, how much change do you get?', ['1 dollar', '2 dollars', '3 dollars', '4 dollars'], 1),
   ('How many grams are in one kilogram?', ['10', '100', '1000', '10000'], 2)]),
Sc('Science Review: Our Bodies, Earth, and Habitats',
   'Grade 2 Science strand review: students revisit our sense of balance, density, nuclear energy, animal tracks, vaccines, desert plants, ice ages, beavers, and wetlands.',
   [('What sense helps us stand and walk without falling?', ['Sense of balance', 'Sense of taste', 'Sense of smell', 'Sense of hearing'], 0),
    ('What does density describe?', ['How tightly packed matter is in an object', 'The colour of an object', 'The taste of an object', 'The sound an object makes'], 0),
    ('What do vaccines help our body do?', ['Recognize and fight off certain diseases', 'Grow taller', 'See better', 'Hear better'], 0),
    ('What is an ice age?', ['A long period when much of Earth was covered in ice', 'A single cold day', 'A type of animal', 'A kind of rock'], 0),
    ('What is a wetland?', ['A habitat where land is covered by shallow water', 'A dry desert', 'A tall mountain', 'A frozen glacier'], 0)]),
SS('Social Studies Review: Government, Money, and Our Communities',
   'Grade 2 Social Studies strand review: students revisit our senate, the Order of Canada, our school board, world currency, land acknowledgements, our legislature, our yearbook, lighthouses, and our fire hall.',
   [('What is the Senate?', ['A part of Canadas government', 'A group that reviews new laws', 'A city council', 'A sports league'], 0),
    ('What is the Order of Canada?', ['A special honour for outstanding Canadians', 'A type of holiday', 'A sports league', 'A kind of coin'], 0),
    ('What is a land acknowledgement?', ['A respectful statement about Indigenous territory', 'A type of map', 'A kind of song', 'A weather report'], 0),
    ('What happens at a provincial legislature?', ['Elected leaders discuss and create laws', 'Students take a math test', 'Food is sold to the public', 'Movies are shown to visitors'], 0),
    ('What is the main purpose of a lighthouse?', ['To help guide ships safely', 'To provide housing for fish', 'To grow crops', 'To collect rainwater'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_141_150)
    append_to(2, g2_141_150)
