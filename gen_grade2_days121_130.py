#!/usr/bin/env python3
"""Grade 2, Days 121-130 -- tenth batch, extending Grade 2 past Day 120
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by fetch_video_ids.py)

Topics chosen to avoid overlap with existing Grade 2 Days 1-120 (see
data/grade2.ts / data/grade2.json, which already densely covers nearly the
full grade 2 ELA, math, science, and social studies curriculum): adjective
order, using a thesaurus, foreshadowing, visualizing, free verse poetry,
informal writing, story pacing, asking questions while reading, and
repetition for emphasis for Language; fractions on a number line, number
bonds to 100, median, AM/PM, multiplying three numbers, perimeter and
area together, skip counting backwards by 10s/100s, choosing measurement
units, and tessellations for Math; bats and echolocation, reptiles and
amphibians, photosynthesis, rainforest layers, polar animals, animal
groups (herds/flocks/schools), bioluminescence, camel desert adaptations,
and spiders for Science; and classroom jobs, how goods travel, community
recycling programs, the history of the Canadian flag, bridges and
tunnels, statues and monuments, emergency 911, fair trade, and peer
mediation for Social Studies -- none of those exact ideas appear in Days
1-120. Day 130 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch. No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz text -- contractions and possessives are avoided
entirely (or rewritten without the apostrophe) to keep the generated .ts
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


def _rebalance_answer_positions(days, seed=20260730):
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


g2_121_130 = [
day(121, [
L('Adjective Order: Which Word Comes First?',
  'Grade 2 Language strand: when using more than one adjective before a noun, there is often a natural order, such as saying a big red ball rather than a red big ball.',
  [('Which phrase uses correct adjective order?', ['A red big ball', 'A big red ball', 'A ball big red', 'Big a red ball'], 1),
   ('Which of these follows natural English adjective order?', ['A wooden small box', 'A small wooden box', 'Box small wooden', 'Wooden box a small'], 1),
   ('Why does adjective order matter in English?', ['It makes sentences sound natural', 'It has no effect at all', 'It changes the spelling', 'It is never important'], 0),
   ('Which sentence sounds correct?', ['She wore a blue lovely dress.', 'She wore a lovely blue dress.', 'She wore dress a lovely blue.', 'She wore blue dress a lovely.'], 1),
   ('Adjective order is a pattern that ___.', ['Native speakers often follow naturally', 'Has no pattern at all', 'Only applies to colours', 'Never applies to size'], 0)]),
M('Fractions on a Number Line',
  'Grade 2 Math strand: fractions can be placed on a number line between 0 and 1, showing their value relative to whole numbers.',
  [('Where would the fraction 1/2 be placed on a number line from 0 to 1?', ['At the very start', 'Exactly in the middle', 'At the very end', 'Past the number 1'], 1),
   ('Where would the fraction 1/4 be placed on a number line from 0 to 1?', ['Closer to 0', 'Exactly in the middle', 'Closer to 1', 'Past the number 1'], 0),
   ('On a number line, which fraction is closer to 1: 3/4 or 1/4?', ['3/4', '1/4', 'They are equal', 'Neither is close to 1'], 0),
   ('A number line showing fractions between 0 and 1 helps us see ___.', ['The size of fractions compared to whole numbers', 'Only whole numbers', 'Colours', 'Shapes'], 0),
   ('Where is the fraction 0/4 located on a number line from 0 to 1?', ['At 0', 'At 1', 'In the middle', 'Past 1'], 0)]),
Sc('Bats: Nocturnal Mammals That Use Echolocation',
   'Grade 2 Science strand: bats are nocturnal mammals that use echolocation, bouncing sound off objects, to find food and navigate in the dark.',
   [('Are bats active mostly during the day or at night?', ['Day', 'Night', 'Neither', 'Only at noon'], 1),
    ('What is echolocation?', ['Using sound to find objects in the dark', 'Using light to see', 'Using smell only', 'Using taste only'], 0),
    ('Are bats classified as birds or mammals?', ['Birds', 'Mammals', 'Reptiles', 'Fish'], 1),
    ('How does echolocation help a bat?', ['It helps the bat find food and avoid obstacles in the dark', 'It helps the bat see colours', 'It helps the bat breathe underwater', 'It has no purpose'], 0),
    ('Bats are the only mammals that can ___.', ['Truly fly', 'Swim', 'Run fast', 'Change colour'], 0)]),
SS('Classroom Jobs: Sharing Responsibility Together',
   'Grade 2 Social Studies strand: classroom jobs, such as line leader or paper passer, give students a chance to share responsibility and help their classroom run smoothly.',
   [('What is the purpose of classroom jobs?', ['To share responsibility and help the classroom run smoothly', 'To keep students from learning', 'They have no purpose', 'Only the teacher should do all the work'], 0),
    ('Which of these could be a classroom job?', ['Line leader', 'Mayor', 'Judge', 'Pilot'], 0),
    ('Why might students take turns with classroom jobs?', ['So everyone gets a chance to contribute', 'Only one student should ever help', 'Turns are not important', 'Jobs should never rotate'], 0),
    ('Having classroom jobs helps build a sense of ___.', ['Community and responsibility', 'Confusion', 'Unfairness', 'Boredom'], 0),
    ('Which is an example of a helpful classroom job?', ['Passing out papers', 'Ignoring the teacher', 'Refusing to help', 'Leaving early'], 0)]),
]),
day(122, [
L('Using a Thesaurus to Find Synonyms',
  'Grade 2 Language strand: a thesaurus is a reference book that lists synonyms, or words with similar meanings, to help writers choose stronger words.',
  [('What is a thesaurus used for?', ['Finding synonyms for a word', 'Finding the weather forecast', 'Finding a recipe', 'Finding a map'], 0),
   ('If you look up happy in a thesaurus, what might you find?', ['Glad or joyful', 'The definition only', 'A picture', 'A math equation'], 0),
   ('How is a thesaurus different from a dictionary?', ['A thesaurus gives synonyms, a dictionary gives definitions', 'They are exactly the same', 'A thesaurus has no words', 'A dictionary only has pictures'], 0),
   ('Why might a writer use a thesaurus?', ['To find a stronger or more interesting word', 'To find a phone number', 'To check the weather', 'To draw a picture'], 0),
   ('Which of these could you find in a thesaurus entry for big?', ['Large, huge, enormous', 'A recipe for cookies', 'A math problem', 'A weather report'], 0)]),
M('Number Bonds to 100: Finding Missing Addends',
  'Grade 2 Math strand: students find missing addends that combine with a given number to make 100, such as finding that 35 needs 65 more to reach 100.',
  [('35 + ? = 100', ['55', '60', '65', '70'], 2),
   ('What number is needed to make 100 when added to 40?', ['50', '60', '65', '70'], 1),
   ('80 + ? = 100', ['10', '15', '20', '25'], 2),
   ('Finding a number bond to 100 means finding ___.', ['The missing addend that reaches 100', 'A number greater than 100', 'A fraction of 100', 'Half of 100 only'], 0),
   ('25 + ? = 100', ['65', '70', '75', '80'], 2)]),
Sc('Reptiles and Amphibians: Cold-Blooded Animals',
   'Grade 2 Science strand: reptiles like snakes and turtles, and amphibians like frogs, are cold-blooded animals whose body temperature changes with their surroundings.',
   [('What does it mean for an animal to be cold-blooded?', ['Its body temperature changes with its surroundings', 'It has cold blood at all times', 'It never moves', 'It cannot survive at all'], 0),
    ('Which of these is a reptile?', ['Snake', 'Frog', 'Dog', 'Robin'], 0),
    ('Which of these is an amphibian?', ['Frog', 'Snake', 'Turtle', 'Lizard'], 0),
    ('Why might a reptile bask in the sun?', ['To warm up its body temperature', 'To cool down completely', 'To hide from all light', 'For no reason'], 0),
    ('Amphibians typically begin life in ___.', ['Water', 'The desert', 'Outer space', 'Deep snow'], 0)]),
SS('How Goods Travel: From Producer to Consumer',
   'Grade 2 Social Studies strand: goods travel a long path from the producer who makes them to the consumer who buys them, often through factories, trucks, and stores.',
   [('Who is a producer?', ['A person or company that makes goods', 'A person who only buys goods', 'A type of animal', 'A kind of weather'], 0),
    ('Who is a consumer?', ['A person who buys and uses goods', 'A person who only makes goods', 'A type of vehicle', 'A kind of building'], 0),
    ('Which of these might help transport goods from a factory to a store?', ['A truck', 'A dictionary', 'A calendar', 'A thermometer'], 0),
    ('Why is it useful to understand how goods travel?', ['It helps us see how products reach us', 'It has no value', 'Goods appear instantly with no process', 'Only farmers need to know this'], 0),
    ('The journey of a good from producer to consumer often passes through ___.', ['Factories, trucks, and stores', 'Only one single step', 'Nothing at all', 'Only the consumers home'], 0)]),
]),
day(123, [
L('Foreshadowing: Hints About What Will Happen',
  'Grade 2 Language strand: foreshadowing is when an author gives readers small clues or hints early in a story about events that will happen later.',
  [('What is foreshadowing?', ['Hints about what will happen later in a story', 'The ending of a story', 'A characters name', 'The title of a book'], 0),
   ('Why do authors use foreshadowing?', ['To build suspense and hint at future events', 'To confuse readers on purpose with no meaning', 'To end the story early', 'To skip the middle of the story'], 0),
   ('If a story mentions dark storm clouds early on, this might foreshadow ___.', ['A storm or trouble coming later', 'A sunny happy ending only', 'Nothing at all', 'The title of the book'], 0),
   ('Foreshadowing usually appears ___ in a story.', ['Only at the very end', 'Early on, before the event happens', 'Never', 'Only in the title'], 1),
   ('Noticing foreshadowing can help readers ___.', ['Predict what might happen next', 'Forget the story completely', 'Skip the ending', 'Ignore the plot'], 0)]),
M('Data: Finding the Median of a Data Set',
  'Grade 2 Math strand: the median of a data set is the middle number when the values are arranged in order from least to greatest.',
  [('What is the median of the data set 2, 4, 6?', ['2', '4', '6', '12'], 1),
   ('How do you find the median of a data set?', ['Add all the numbers together', 'Order the numbers and find the middle value', 'Multiply the numbers', 'Find the largest number only'], 1),
   ('What is the median of the data set 1, 3, 5, 7, 9?', ['1', '3', '5', '9'], 2),
   ('Before finding the median, the data should be ___.', ['Ordered from least to greatest', 'Left in random order', 'Multiplied together', 'Ignored'], 0),
   ('The median tells us about the ___ of a data set.', ['Middle value', 'Total sum', 'Largest value only', 'Number of items only'], 0)]),
Sc('How Plants Make Food: An Introduction to Photosynthesis',
   'Grade 2 Science strand: plants make their own food through a process called photosynthesis, using sunlight, water, and air to grow.',
   [('What is photosynthesis?', ['The process plants use to make their own food', 'A type of animal behaviour', 'A kind of rock formation', 'A weather pattern'], 0),
    ('What do plants need for photosynthesis?', ['Sunlight, water, and air', 'Only darkness', 'Only soil', 'Only sound'], 0),
    ('Where in the plant does most photosynthesis happen?', ['The leaves', 'The roots', 'The flower petals only', 'The seeds only'], 0),
    ('Why is photosynthesis important for plants?', ['It lets plants make the food they need to grow', 'It has no purpose', 'It stops plants from growing', 'It only happens at night'], 0),
    ('Photosynthesis mainly requires energy from ___.', ['Sunlight', 'The moon', 'Wind alone', 'Rocks'], 0)]),
SS('Community Recycling Programs: Where Our Blue Bin Goes',
   'Grade 2 Social Studies strand: communities run recycling programs, collecting materials in blue bins and sending them to facilities where they are sorted and turned into new products.',
   [('What colour bin is often used for recycling in many communities?', ['Blue', 'Black', 'Yellow', 'Pink'], 0),
    ('Where do recycled materials go after being collected?', ['A recycling facility to be sorted and processed', 'Straight to a landfill', 'Nowhere, they disappear', 'Back to the same store'], 0),
    ('Why do communities run recycling programs?', ['To reduce waste and reuse materials', 'To create more garbage', 'Recycling has no benefit', 'To waste more resources'], 0),
    ('Which of these is commonly recycled?', ['Paper and cardboard', 'Food scraps only', 'Rocks', 'Sunlight'], 0),
    ('A community recycling program helps ___.', ['Protect the environment', 'Harm the environment', 'Increase pollution', 'Waste more resources'], 0)]),
]),
day(124, [
L('Visualizing: Making Pictures in Your Mind While Reading',
  'Grade 2 Language strand: visualizing means using descriptive details in a text to create a picture in your mind of what is happening in the story.',
  [('What does it mean to visualize while reading?', ['Creating a picture in your mind of the story', 'Ignoring the words', 'Only looking at illustrations', 'Skipping descriptive parts'], 0),
   ('What kind of details help readers visualize a scene?', ['Descriptive details about sights, sounds, and feelings', 'Only the page number', 'Only the title', 'Only the authors name'], 0),
   ('Why is visualizing a helpful reading strategy?', ['It helps readers understand and enjoy the story more', 'It has no benefit', 'It replaces reading completely', 'It only works with pictures already in the book'], 0),
   ('If a story describes a crunchy, golden autumn leaf, what does this help readers do?', ['Picture the leaf in their mind', 'Ignore the sentence', 'Skip to the next page', 'Forget the story'], 0),
   ('Visualizing is a strategy used mainly during ___.', ['Reading', 'Recess', 'Lunch', 'Gym class'], 0)]),
M('Time: Understanding AM and PM',
  'Grade 2 Math strand: AM refers to the time from midnight to noon, and PM refers to the time from noon to midnight, helping us describe when events happen.',
  [('Does AM refer to morning or evening hours?', ['Morning, from midnight to noon', 'Evening, from noon to midnight', 'Only midnight exactly', 'Only noon exactly'], 0),
   ('Does PM refer to morning or evening hours?', ['Morning hours', 'Noon to midnight hours', 'Only midnight', 'Only sunrise'], 1),
   ('If you wake up at 7:00 in the morning, is that AM or PM?', ['AM', 'PM', 'Neither', 'Both'], 0),
   ('If you eat dinner at 6:00 in the evening, is that AM or PM?', ['AM', 'PM', 'Neither', 'Both'], 1),
   ('AM and PM help us know ___.', ['Whether a time is in the morning or evening/night', 'The day of the week', 'The month of the year', 'The temperature outside'], 0)]),
Sc('Layers of the Rainforest: Canopy to Forest Floor',
   'Grade 2 Science strand: a rainforest has different layers, including the tall emergent layer, the leafy canopy, the understory, and the shaded forest floor.',
   [('What is the very top layer of a rainforest called?', ['The emergent layer', 'The forest floor', 'The understory', 'The basement'], 0),
    ('What is the leafy, tree-top layer of a rainforest called?', ['The canopy', 'The forest floor', 'The emergent layer only', 'The roots'], 0),
    ('Which rainforest layer receives the least sunlight?', ['The forest floor', 'The emergent layer', 'The canopy', 'The very top'], 0),
    ('Why do rainforests have different layers?', ['Different plants and animals live at different heights', 'All rainforest layers are identical', 'Layers do not exist in rainforests', 'Only the ground layer matters'], 0),
    ('The layer just below the canopy is called the ___.', ['Understory', 'Overstory', 'Basement', 'Attic'], 0)]),
SS('The History of the Canadian Flag: Before and After 1965',
   'Grade 2 Social Studies strand: before 1965, Canada used a different flag, and the current red and white maple leaf flag was officially adopted that year.',
   [('In what year was the current Canadian maple leaf flag adopted?', ['1965', '1867', '1812', '2000'], 0),
    ('What are the main colours of the Canadian flag?', ['Red and white', 'Blue and yellow', 'Green and orange', 'Purple and black'], 0),
    ('What symbol is in the centre of the Canadian flag?', ['A maple leaf', 'A star', 'A crown', 'A bird'], 0),
    ('Did Canada always use the same flag as it does today?', ['No, the flag changed in 1965', 'Yes, it has never changed', 'Canada has never had a flag', 'The flag changes every year'], 0),
    ('Learning about the history of the flag helps us understand ___.', ['How national symbols can change over time', 'Nothing important', 'Only recent history', 'A fictional story'], 0)]),
]),
day(125, [
L('Free Verse Poetry: Poems Without Rhyme or Rules',
  'Grade 2 Language strand: free verse poetry does not follow a set rhyme scheme or rhythm, allowing writers to express ideas freely in whatever lines feel right.',
  [('Does free verse poetry need to rhyme?', ['No', 'Yes, always', 'Only sometimes required', 'Rhyme is the only rule'], 0),
   ('What makes free verse different from rhyming poetry?', ['It does not follow a set rhyme or rhythm pattern', 'It must rhyme perfectly', 'It has strict rules about length', 'It cannot use descriptive words'], 0),
   ('Why might a poet choose to write in free verse?', ['To express ideas freely without following strict rules', 'Because it is the only kind of poem that exists', 'Because rhyming is required', 'Because it has to be exactly ten lines'], 0),
   ('Which is a feature of free verse poetry?', ['Flexible line lengths and no required rhyme', 'Every line must rhyme with the next', 'It must be written in one sentence', 'It cannot use imagery'], 0),
   ('Free verse poetry is a type of ___.', ['Poetry', 'Math problem', 'Science report', 'Map'], 0)]),
M('Multiplying Three Numbers Together',
  'Grade 2 Math strand: to multiply three numbers together, students multiply two of the numbers first, then multiply that answer by the third number.',
  [('What is 2 x 3 x 2?', ['10', '12', '14', '16'], 1),
   ('To solve 2 x 2 x 5, which two numbers might you multiply first?', ['2 and 2', 'Any two of the numbers, then multiply by the third', 'Only the largest number', 'None of them'], 1),
   ('What is 1 x 4 x 3?', ['8', '10', '12', '14'], 2),
   ('What is 3 x 2 x 2?', ['10', '12', '14', '16'], 1),
   ('When multiplying three numbers, the order you multiply them in ___.', ['Does not change the final answer', 'Always changes the final answer', 'Must always start with the largest', 'Must always start with the smallest'], 0)]),
Sc('Polar Animals: Surviving the Arctic Cold',
   'Grade 2 Science strand: polar animals, such as polar bears and arctic foxes, have thick fur and fat to help them survive extremely cold temperatures.',
   [('Name one adaptation that helps polar animals stay warm.', ['Thick fur or fat', 'Thin skin only', 'No fur at all', 'Bright feathers only'], 0),
    ('Which of these is a polar animal?', ['Polar bear', 'Camel', 'Toucan', 'Kangaroo'], 0),
    ('Why do polar animals often have white fur?', ['To camouflage in the snow', 'To attract more predators', 'It has no purpose', 'To stay cooler in heat'], 0),
    ('What body feature helps seals and whales survive cold arctic water?', ['A thick layer of fat called blubber', 'Feathers', 'Dry scaly skin', 'No body fat at all'], 0),
    ('Polar regions are known for being ___.', ['Extremely cold', 'Extremely hot', 'Always rainy', 'Always dry and sandy'], 0)]),
SS('Canadian Bridges and Tunnels: Engineering Our Connections',
   'Grade 2 Social Studies strand: bridges and tunnels are built across Canada to connect communities separated by rivers, valleys, or mountains, making travel easier.',
   [('Why are bridges built?', ['To connect places separated by water, valleys, or gaps', 'To block travel', 'They serve no purpose', 'To make travel harder'], 0),
    ('Why might a tunnel be built through a mountain?', ['To make travel through the mountain easier and faster', 'To make travel impossible', 'Tunnels are never useful', 'To hide the mountain'], 0),
    ('What do bridges and tunnels both help improve?', ['Transportation and connection between places', 'Nothing important', 'Only decoration', 'Weather patterns'], 0),
    ('Which of these might a bridge cross over?', ['A river', 'A classroom', 'A single house', 'A pencil'], 0),
    ('Engineers who design bridges and tunnels need to consider ___.', ['Safety and strong construction', 'Nothing at all', 'Only the colour', 'Only the price of paint'], 0)]),
]),
day(126, [
L('Informal Writing: Notes and Messages',
  'Grade 2 Language strand: informal writing, like a quick note or message to a friend, uses a casual, friendly tone that is different from formal writing.',
  [('What is informal writing?', ['Casual writing like a note or message', 'A formal report only', 'A legal document', 'A dictionary entry'], 0),
   ('Which of these is an example of informal writing?', ['A quick note to a friend', 'A formal essay for a teacher', 'A legal contract', 'A scientific report'], 0),
   ('How is informal writing different from formal writing?', ['It uses a casual, friendly tone', 'It is always longer', 'It must always rhyme', 'It has no purpose'], 0),
   ('Which sentence sounds informal?', ['Hey, want to play at recess?', 'It is hereby requested that you attend.', 'The following report outlines the findings.', 'This document shall be reviewed.'], 0),
   ('Informal writing is often used when writing to ___.', ['Friends or family', 'A judge in court', 'A government office', 'A formal business only'], 0)]),
M('Perimeter and Area Together: Comparing Two Measurements',
  'Grade 2 Math strand: perimeter measures the distance around a shape, while area measures the space inside it, and students compare both for the same shape.',
  [('What does perimeter measure?', ['The distance around a shape', 'The space inside a shape', 'The weight of a shape', 'The colour of a shape'], 0),
   ('What does area measure?', ['The distance around a shape', 'The space inside a shape', 'The height only', 'The number of corners'], 1),
   ('A rectangle has a perimeter of 14 and sides of 5 and 2. Does the math check out, since 5+5+2+2 equals 14?', ['Yes, 14', 'No, it should be 10', 'No, it should be 20', 'No, it should be 7'], 0),
   ('Can two different shapes have the same perimeter but different areas?', ['Yes', 'No, never', 'Only if they are squares', 'Only if they are circles'], 0),
   ('Perimeter and area are both examples of ___.', ['Measurements of a shape', 'Colours', 'Types of graphs', 'Fractions'], 0)]),
Sc('Animal Groups: Herds, Flocks, and Schools',
   'Grade 2 Science strand: many animals live and move together in groups with special names, such as a herd of deer, a flock of birds, or a school of fish.',
   [('What do we call a group of deer?', ['A herd', 'A flock', 'A school', 'A pack'], 0),
    ('What do we call a group of birds flying together?', ['A flock', 'A herd', 'A school', 'A den'], 0),
    ('What do we call a group of fish swimming together?', ['A school', 'A herd', 'A flock', 'A pod'], 0),
    ('Why might animals travel together in groups?', ['For safety and to find food more easily', 'Groups provide no benefit', 'To get lost more easily', 'It is always dangerous'], 0),
    ('A group of wolves is called a ___.', ['Pack', 'Flock', 'School', 'Herd'], 0)]),
SS('Statues and Monuments: Remembering Our History',
   'Grade 2 Social Studies strand: statues and monuments are built in public places to help communities remember important people or events from history.',
   [('What is the purpose of a statue or monument?', ['To help communities remember important people or events', 'To block traffic', 'They have no purpose', 'To confuse visitors'], 0),
    ('Where are statues and monuments often found?', ['In public places like parks or squares', 'Hidden underground with no access', 'Only inside private homes', 'Nowhere, they do not exist'], 0),
    ('Why might a community build a monument for a historical event?', ['To remember and honour what happened', 'To forget the event completely', 'It has no meaning', 'To hide the event from everyone'], 0),
    ('Which of these could a monument represent?', ['A historical figure or event', 'A random shape with no meaning', 'A type of food', 'A weather pattern'], 0),
    ('Learning about statues and monuments helps us understand ___.', ['Parts of our shared history', 'Nothing about the past', 'Only fictional stories', 'Modern technology only'], 0)]),
]),
day(127, [
L('Story Pacing: Fast and Slow Moments in a Story',
  'Grade 2 Language strand: story pacing describes how quickly or slowly events unfold, with exciting parts often moving fast and quiet parts moving slower.',
  [('What does story pacing describe?', ['How quickly or slowly events happen', 'The characters names', 'The title of the book', 'The cover colour'], 0),
   ('During an exciting chase scene, the pacing is usually ___.', ['Fast', 'Slow', 'Nonexistent', 'The same as a quiet scene'], 0),
   ('During a calm, quiet moment in a story, the pacing is usually ___.', ['Slow', 'Fast', 'Random', 'Not important'], 0),
   ('Why do authors vary the pacing of a story?', ['To create excitement or calm at the right moments', 'Pacing never changes in stories', 'It has no purpose', 'To confuse readers on purpose'], 0),
   ('Which word suggests fast pacing in a scene?', ['Suddenly', 'Slowly', 'Quietly', 'Eventually, over many years'], 0)]),
M('Skip Counting Backwards by 10s and 100s',
  'Grade 2 Math strand: students skip count backwards by 10s and 100s, such as counting 100, 90, 80 or 500, 400, 300.',
  [('What comes next: 100, 90, 80, ___?', ['75', '70', '65', '60'], 1),
   ('What comes next: 500, 400, 300, ___?', ['250', '200', '150', '100'], 1),
   ('Skip counting backwards by 10s from 50 gives what number next?', ['45', '40', '35', '30'], 1),
   ('What comes next: 900, 800, 700, ___?', ['650', '600', '550', '500'], 1),
   ('Skip counting backwards by 100s means we subtract ___ each time.', ['10', '50', '100', '1000'], 2)]),
Sc('Bioluminescence: Animals That Glow in the Dark',
   'Grade 2 Science strand: bioluminescence is when living things, such as fireflies and some deep-sea fish, produce their own light using a chemical reaction.',
   [('What is bioluminescence?', ['When living things produce their own light', 'When animals sleep all winter', 'When plants change colour', 'When rocks glow from heat'], 0),
    ('Name one animal known for bioluminescence.', ['A firefly', 'A cow', 'A rabbit', 'A sheep'], 0),
    ('Where do many bioluminescent sea creatures live?', ['Deep in the dark ocean', 'On mountain tops', 'In deserts', 'In dry grasslands'], 0),
    ('Why might an animal use bioluminescence?', ['To attract food, find mates, or scare predators', 'It has no purpose at all', 'To stay warm', 'To breathe underwater'], 0),
    ('Bioluminescent light is created through a ___.', ['Chemical reaction inside the animals body', 'Reflection of moonlight only', 'Burning fire', 'Electric wire'], 0)]),
SS('Emergency 911: How to Call for Help',
   'Grade 2 Social Studies strand: in Canada, 911 is the emergency phone number people call to reach police, firefighters, or ambulance workers quickly during an emergency.',
   [('What phone number do people call in an emergency in Canada?', ['911', '411', '611', '211'], 0),
    ('Who might answer a 911 call?', ['An emergency dispatcher who sends help', 'A random stranger', 'No one answers', 'A store clerk'], 0),
    ('Which of these is an example of a real emergency to call 911 for?', ['A house fire', 'Wanting a snack', 'Losing a toy', 'Being bored'], 0),
    ('Why is it important to know how to call 911?', ['It can help get fast help during a real emergency', 'It has no importance', 'It should never be used', 'It is only for adults to know'], 0),
    ('When calling 911, it is important to ___.', ['Stay calm and give clear information', 'Hang up right away', 'Say nothing at all', 'Call as a joke'], 0)]),
]),
day(128, [
L('Reading Strategy: Asking Questions Before and During Reading',
  'Grade 2 Language strand: strong readers ask themselves questions before and during reading, such as wondering what will happen next, to stay engaged and understand the text.',
  [('What is one benefit of asking questions while reading?', ['It helps readers stay engaged and understand more', 'It has no benefit', 'It replaces reading completely', 'It confuses readers on purpose'], 0),
   ('Which is an example of a question a reader might ask before starting a book?', ['What do I think this book will be about?', 'What is for lunch today?', 'What time is recess?', 'What is the weather like?'], 0),
   ('When might a reader ask questions during reading?', ['Whenever something seems confusing or interesting', 'Only after finishing the whole book', 'Never', 'Only during math class'], 0),
   ('Asking questions while reading is an example of a ___.', ['Reading strategy', 'Math strategy', 'Art project', 'Recess game'], 0),
   ('Which question shows deep thinking about a story?', ['Why did the character make that choice?', 'What colour is the cover?', 'How many pages does it have?', 'What font is used?'], 0)]),
M('Estimating Measurement: Choosing the Best Unit',
  'Grade 2 Math strand: students choose the most reasonable unit to estimate a measurement, such as using metres for a hallway and centimetres for a pencil.',
  [('Which unit would best measure the length of a pencil?', ['Metres', 'Centimetres', 'Kilometres', 'Litres'], 1),
   ('Which unit would best measure the length of a hallway?', ['Centimetres', 'Metres', 'Grams', 'Millilitres'], 1),
   ('Which unit would best measure the mass of an apple?', ['Kilograms', 'Grams', 'Litres', 'Metres'], 1),
   ('Which unit would best measure the capacity of a bathtub?', ['Millilitres', 'Litres', 'Centimetres', 'Grams'], 1),
   ('Choosing the best unit depends on the ___ of the object being measured.', ['Size', 'Colour', 'Name', 'Price'], 0)]),
Sc('Camels and Desert Adaptations: Storing Water and Fat',
   'Grade 2 Science strand: camels have special adaptations for desert life, such as humps that store fat and the ability to go a long time without drinking water.',
   [('What do camel humps mainly store?', ['Fat', 'Water only', 'Sand', 'Air'], 0),
    ('Why can camels survive a long time without water?', ['Their bodies are adapted to conserve water', 'They never need water at all', 'They drink constantly', 'They live only in wet places'], 0),
    ('Camels are well adapted to living in ___.', ['Deserts', 'Oceans', 'Rainforests', 'The Arctic'], 0),
    ('Which of these is a camel adaptation for hot, sandy environments?', ['Long eyelashes to protect from sand', 'Thick blubber like a whale', 'Wings for flying', 'Gills for breathing underwater'], 0),
    ('Desert adaptations help animals like camels survive with ___.', ['Very little water', 'Constant rain', 'Extreme cold only', 'No sunlight at all'], 0)]),
SS('Fair Trade: Buying Products That Help Others',
   'Grade 2 Social Studies strand: fair trade means buying products, like coffee or chocolate, that are made in ways that pay workers fairly and protect the environment.',
   [('What does fair trade mean?', ['Buying products made in ways that pay workers fairly', 'Buying the cheapest product always', 'Ignoring how products are made', 'Only buying products from one country'], 0),
    ('Which of these might have a fair trade label?', ['Coffee or chocolate', 'A rock', 'A cloud', 'A shadow'], 0),
    ('Why might someone choose to buy fair trade products?', ['To support fair pay and good conditions for workers', 'It has no purpose', 'To harm workers on purpose', 'Fair trade does not exist'], 0),
    ('Fair trade often also considers ___.', ['Protecting the environment', 'Ignoring nature completely', 'Making products more wasteful', 'Increasing pollution'], 0),
    ('Choosing fair trade products is one way to be a ___.', ['Responsible consumer', 'Careless shopper', 'Wasteful buyer', 'Unfair trader'], 0)]),
]),
day(129, [
L('Authors Craft: Repetition for Emphasis',
  'Grade 2 Language strand: authors sometimes repeat words or phrases on purpose to emphasize an idea or create a rhythm, such as repeating never give up, never give up.',
  [('Why might an author repeat a word or phrase in a story?', ['To emphasize an important idea', 'By accident every time', 'To confuse the reader', 'To make the story shorter'], 0),
   ('Which of these shows repetition for emphasis?', ['Run, run, run as fast as you can!', 'The dog ran quickly.', 'She walked to school.', 'It was a sunny day.'], 0),
   ('What effect can repetition have on a reader?', ['It can create rhythm and emphasize meaning', 'It always makes writing boring', 'It has no effect', 'It removes all meaning'], 0),
   ('Repetition is a tool used mainly in ___.', ['Writing and poetry', 'Math equations only', 'Weather reports only', 'Phone numbers'], 0),
   ('Which phrase uses repetition to build excitement?', ['Faster, faster, faster we go!', 'The car moved.', 'It was quiet.', 'The room was empty.'], 0)]),
M('Tessellations: Shapes That Tile Without Gaps',
  'Grade 2 Math strand: a tessellation is a pattern of shapes, like squares or triangles, that fit together perfectly with no gaps or overlaps.',
  [('What is a tessellation?', ['Shapes that fit together with no gaps or overlaps', 'A single shape alone', 'A type of graph', 'A kind of number'], 0),
   ('Which shape can tessellate easily to cover a floor with no gaps?', ['Square', 'A random blob', 'A shape with curves only', 'None of these can tessellate'], 0),
   ('Why might tessellations be used in floor tiles?', ['They fit together perfectly with no wasted space', 'They always leave big gaps', 'They cannot be repeated', 'They are only used once'], 0),
   ('Which of these shapes tessellates well?', ['A triangle', 'A random curved blob', 'An oval', 'A single point'], 0),
   ('A pattern with no gaps or overlaps between repeating shapes is called a ___.', ['Tessellation', 'Fraction', 'Median', 'Perimeter'], 0)]),
Sc('Spiders: Eight-Legged Predators',
   'Grade 2 Science strand: spiders are eight-legged animals, unlike six-legged insects, that often build webs to catch prey for food.',
   [('How many legs does a spider have?', ['Six', 'Eight', 'Ten', 'Four'], 1),
    ('How is a spider different from an insect?', ['A spider has eight legs, an insect has six', 'They are exactly the same', 'Spiders have wings, insects do not', 'Insects have eight legs, spiders have six'], 0),
    ('What do many spiders build to catch food?', ['A web', 'A nest', 'A burrow', 'A hive'], 0),
    ('What do spiders mainly eat?', ['Insects and other small creatures', 'Only leaves', 'Only fruit', 'Only rocks'], 0),
    ('Spiders are classified as ___.', ['Predators that catch prey', 'Plants', 'Birds', 'Fish'], 0)]),
SS('Peer Mediation: Helping Classmates Solve Disagreements',
   'Grade 2 Social Studies strand: peer mediation is when trained students help classmates talk through a disagreement calmly and find a fair solution together.',
   [('What is peer mediation?', ['Trained students helping classmates solve disagreements', 'Ignoring a disagreement completely', 'A teacher solving every problem alone', 'A type of game'], 0),
    ('What is the goal of peer mediation?', ['To help both sides find a fair solution', 'To pick one side and ignore the other', 'To make the disagreement worse', 'To avoid talking about the problem'], 0),
    ('Which skill is important for a peer mediator?', ['Listening carefully to both sides', 'Yelling the loudest', 'Ignoring both students', 'Choosing a side immediately'], 0),
    ('Why might schools use peer mediation programs?', ['To help students solve conflicts peacefully', 'Conflicts should never be discussed', 'It has no benefit', 'Only adults can solve problems'], 0),
    ('A successful peer mediation usually ends with ___.', ['A fair solution both sides agree on', 'One side losing completely', 'More arguing', 'No resolution at all'], 0)]),
]),
day(130, [
L('Language Review: Word Choice, Poetry, and Reading Strategies',
  'Grade 2 Language strand review: students revisit adjective order, using a thesaurus, foreshadowing, visualizing, free verse poetry, and asking questions while reading.',
  [('Which phrase uses correct adjective order?', ['A red big ball', 'A big red ball', 'A ball big red', 'Big a red ball'], 1),
   ('What is a thesaurus used for?', ['Finding synonyms for a word', 'Finding the weather forecast', 'Finding a recipe', 'Finding a map'], 0),
   ('What is foreshadowing?', ['Hints about what will happen later in a story', 'The ending of a story', 'A characters name', 'The title of a book'], 0),
   ('What does it mean to visualize while reading?', ['Creating a picture in your mind of the story', 'Ignoring the words', 'Only looking at illustrations', 'Skipping descriptive parts'], 0),
   ('Does free verse poetry need to rhyme?', ['No', 'Yes, always', 'Only sometimes required', 'Rhyme is the only rule'], 0)]),
M('Math Review: Fractions, Time, and Measurement',
  'Grade 2 Math strand review: students revisit fractions on a number line, number bonds to 100, finding the median, AM and PM, multiplying three numbers, and tessellations.',
  [('Where would the fraction 1/2 be placed on a number line from 0 to 1?', ['At the very start', 'Exactly in the middle', 'At the very end', 'Past the number 1'], 1),
   ('35 + ? = 100', ['55', '60', '65', '70'], 2),
   ('What is the median of the data set 2, 4, 6?', ['2', '4', '6', '12'], 1),
   ('If you wake up at 7:00 in the morning, is that AM or PM?', ['AM', 'PM', 'Neither', 'Both'], 0),
   ('What is 2 x 3 x 2?', ['10', '12', '14', '16'], 1)]),
Sc('Science Review: Animals, Plants, and Habitats',
   'Grade 2 Science strand review: students revisit bats, reptiles and amphibians, photosynthesis, rainforest layers, polar animals, animal groups, and bioluminescence.',
   [('Are bats active mostly during the day or at night?', ['Day', 'Night', 'Neither', 'Only at noon'], 1),
    ('Which of these is a reptile?', ['Snake', 'Frog', 'Dog', 'Robin'], 0),
    ('What is photosynthesis?', ['The process plants use to make their own food', 'A type of animal behaviour', 'A kind of rock formation', 'A weather pattern'], 0),
    ('What is the very top layer of a rainforest called?', ['The emergent layer', 'The forest floor', 'The understory', 'The basement'], 0),
    ('What do we call a group of fish swimming together?', ['A school', 'A herd', 'A flock', 'A pod'], 0)]),
SS('Social Studies Review: Community, Symbols, and Responsibility',
   'Grade 2 Social Studies strand review: students revisit classroom jobs, how goods travel, recycling programs, the Canadian flags history, bridges and tunnels, and peer mediation.',
   [('What is the purpose of classroom jobs?', ['To share responsibility and help the classroom run smoothly', 'To keep students from learning', 'They have no purpose', 'Only the teacher should do all the work'], 0),
    ('Who is a producer?', ['A person or company that makes goods', 'A person who only buys goods', 'A type of animal', 'A kind of weather'], 0),
    ('In what year was the current Canadian maple leaf flag adopted?', ['1965', '1867', '1812', '2000'], 0),
    ('What phone number do people call in an emergency in Canada?', ['911', '411', '611', '211'], 0),
    ('What is peer mediation?', ['Trained students helping classmates solve disagreements', 'Ignoring a disagreement completely', 'A teacher solving every problem alone', 'A type of game'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_121_130)
    append_to(2, g2_121_130)
