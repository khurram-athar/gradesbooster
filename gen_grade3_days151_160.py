#!/usr/bin/env python3
"""Grade 3, Days 151-160 -- extends Grade 3 from 150 to 160 days. Modeled
exactly on gen_grade3_days141_150.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-150
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum many times over. New topics for this
batch: using colons before lists, loanwords, hyperbole, writing a fable,
paraphrasing what a speaker said, correcting double negatives,
palindromes, formal versus informal language, and writing an acrostic
poem for Language; composing and decomposing numbers, prisms and
pyramids, reading simple circle graphs, fractions that equal one whole,
using an array model for 2-digit multiplication, interpreting remainders
in word problems, comparing volume and capacity, patterns with two
attributes, and comparing costs to find the best deal for Math; the
order of the planets, octopuses, carnivorous plants, how mountains are
formed, rainbows, teeth and their jobs, beetles, the life cycle of a sea
turtle, and the importance of sleep for Science; and Canadas national
historic sites, the immigration points system, Canada Post, trade
agreements, the Canadian Coast Guard, Canadas national sports, access to
clean drinking water, self-government in the territories, and settlement
services for newcomers for Social Studies -- none of those exact ideas
appear in Days 1-150. Day 160 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch, with
review titles written to be textually distinct from every earlier review
days title (e.g. Day 140s and Day 150s). No embedded ASCII double-quote
or straight apostrophe characters are used anywhere in
title/summary/question/option text; apostrophes are dropped entirely
(e.g. Canadas instead of Canada with an apostrophe s), matching the
convention established in Days 111-150.

Invocation (matches the 141-150 script):
  cd ~/gradesbooster && python3 gen_grade3_days151_160.py
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


def _rebalance_answer_positions(days, seed=20260809):
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


g3_151_160 = [
day(151, [
L('Grammar: Using Colons Before Lists',
  'Grade 3 Language strand: a colon can introduce a list of items after a complete sentence, signalling to the reader that specific examples or details are about to follow.',
  [('What can a colon introduce after a complete sentence?', ['A list of items', 'A brand new paragraph', 'A single silent letter', 'A page number'], 0),
   ('Which sentence correctly uses a colon before a list?', ['Pack these items: a tent, a flashlight, and a map.', 'Pack these items, a tent, a flashlight, and a map.', 'Pack these: items a tent a flashlight and a map.', 'Pack, these items a tent a flashlight and a map.'], 0),
   ('A colon before a list should usually follow what kind of clause?', ['An independent clause that could stand alone as a sentence', 'A single lonely word', 'A question with no verb', 'A title with no punctuation'], 0),
   ('Why might a writer use a colon before a list?', ['To signal that specific examples or details will follow', 'To end the sentence early with no list', 'To remove all punctuation from a sentence', 'To hide the list from the reader'], 0),
   ('Which is NOT a common use of a colon in a sentence?', ['Ending a question', 'Introducing a list', 'Introducing an explanation', 'Introducing a quotation'], 0)]),
M('Number: Composing and Decomposing Numbers in Different Ways',
  'Grade 3 Math strand: a number can be composed and decomposed in more than one way, such as showing 47 as 40 plus 7 or as 30 plus 17, which builds flexible thinking about place value.',
  [('Which is one way to decompose the number 47?', ['40 + 7', '4 + 7', '470', '47 + 47'], 0),
   ('What does it mean to decompose a number?', ['To break it apart into smaller parts that add up to the whole', 'To multiply it by ten', 'To erase the number completely', 'To turn it into a fraction'], 0),
   ('Which is another way to show 53 besides 50 + 3?', ['40 + 13', '5 + 3', '530', '35 + 35'], 0),
   ('Why is it useful to decompose numbers in more than one way?', ['It builds flexible thinking about place value and helps with mental math', 'It makes numbers disappear', 'It removes the need for addition', 'It only works for even numbers'], 0),
   ('Composing a number means ___.', ['Putting parts together to form the whole number', 'Breaking the number into single digits only', 'Deleting the number entirely', 'Turning the number into a letter'], 0)]),
Sc('Science: The Order of the Planets from the Sun',
   'Grade 3 Science strand: the eight planets of our solar system orbit the Sun in a specific order, starting with Mercury, the closest planet, and ending with Neptune, the farthest planet.',
   [('Which planet is closest to the Sun?', ['Mercury', 'Venus', 'Earth', 'Mars'], 0),
    ('Which planet is known as the third planet from the Sun?', ['Earth', 'Mercury', 'Venus', 'Mars'], 0),
    ('Which planet is the farthest from the Sun?', ['Neptune', 'Saturn', 'Jupiter', 'Mars'], 0),
    ('How many planets orbit the Sun in our solar system?', ['Eight', 'Six', 'Ten', 'Five'], 0),
    ('What keeps the planets orbiting the Sun?', ['The pull of the Suns gravity', 'Strong winds in space', 'Ropes connecting the planets', 'Nothing holds them at all'], 0)]),
SS('Social Studies: Canadas National Historic Sites',
   'Grade 3 Social Studies strand: a national historic site is a place recognized for its importance to Canadas history, and these sites help Canadians learn about and remember significant people and events.',
   [('What is a national historic site?', ['A place recognized for its importance to Canadas history', 'A type of grocery store', 'A type of weather station', 'A brand new shopping mall'], 0),
    ('Why might a place be designated a national historic site?', ['It is important to understanding Canadas history', 'It has no connection to history at all', 'It was built within the last year', 'It has no visitors ever'], 0),
    ('What can visitors often do at a national historic site?', ['Learn about significant people and events from the past', 'Buy foreign currency only', 'Ignore all the exhibits', 'Avoid learning anything new'], 0),
    ('Who helps protect and maintain many of Canadas national historic sites?', ['Government agencies and heritage organizations', 'No one looks after them', 'Only private individuals with no support', 'Only tourists from other countries'], 0),
    ('Why is it valuable for students to learn about national historic sites?', ['They help connect students to important parts of Canadas past', 'They have no educational value', 'They only exist in one province', 'They replace the need for history books'], 0)]),
]),
day(152, [
L('Vocabulary: Loanwords — Words English Has Borrowed',
  'Grade 3 Language strand: a loanword is a word that English has borrowed from another language, such as balcony from Italian, kindergarten from German, and canoe from an Indigenous language.',
  [('What is a loanword?', ['A word that English has borrowed from another language', 'A word with no meaning at all', 'A word used only in math', 'A punctuation mark'], 0),
   ('The word kindergarten was borrowed from which language?', ['German', 'French only', 'Latin only', 'A made-up language'], 0),
   ('Why does English contain so many loanwords?', ['English has borrowed words through contact with many cultures and languages', 'English has never changed at all', 'Loanwords are always mistakes', 'English only uses invented words'], 0),
   ('Which is an example of a loanword in English?', ['Canoe', 'Jump', 'Happy', 'Quick'], 0),
   ('Learning about loanwords can help readers understand ___.', ['How languages influence and borrow from each other', 'That words never have interesting origins', 'That English has no history', 'That every word was invented in English'], 0)]),
M('Geometry: Prisms and Pyramids — Comparing 3D Shapes',
  'Grade 3 Math strand: a prism has two matching parallel bases connected by rectangular faces, while a pyramid has one base and triangular faces that meet at a single point called the apex.',
  [('How many bases does a prism have?', ['Two matching parallel bases', 'One base only', 'Three bases', 'No bases at all'], 0),
   ('How many bases does a pyramid have?', ['One base', 'Two bases', 'Three bases', 'No bases at all'], 0),
   ('What shape are the side faces of a prism usually?', ['Rectangles', 'Circles', 'Ovals', 'Stars'], 0),
   ('What do the triangular faces of a pyramid meet at?', ['A single point called the apex', 'Another base', 'A flat edge only', 'Nothing, they never meet'], 0),
   ('Which is an example of a prism?', ['A rectangular box', 'A cone', 'A sphere', 'A pyramid'], 0)]),
Sc('Science: Octopuses — Intelligent Ocean Creatures',
   'Grade 3 Science strand: an octopus is a soft-bodied ocean animal with eight arms, no internal skeleton, and a highly developed brain that allows it to solve problems and change colour to hide from predators.',
   [('How many arms does an octopus have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
    ('What is unusual about an octopuses body?', ['It has no internal skeleton', 'It has a hard shell like a turtle', 'It has fur covering its body', 'It has wings for flying'], 0),
    ('Why might an octopus change colour?', ['To hide from predators by blending into its surroundings', 'To attract airplanes', 'To become heavier', 'To stop breathing'], 0),
    ('What is notable about an octopuses brain?', ['It is highly developed, allowing the octopus to solve problems', 'It does not exist at all', 'It only controls one arm', 'It cannot process any information'], 0),
    ('Where do octopuses live?', ['In the ocean', 'In deserts', 'In treetops', 'In caves with no water'], 0)]),
SS('Social Studies: How Canadas Immigration Points System Works',
   'Grade 3 Social Studies strand: Canadas immigration points system evaluates factors such as education, work experience, and language skills to help decide who may be able to immigrate to Canada.',
   [('What does Canadas immigration points system evaluate?', ['Factors such as education, work experience, and language skills', 'Only a persons favourite colour', 'Only a persons height', 'Only a persons birthday'], 0),
    ('Why might a country use a points system for immigration?', ['To help make fair and consistent decisions about applicants', 'To avoid ever welcoming immigrants', 'To choose applicants randomly with no criteria', 'To remove all rules from immigration'], 0),
    ('Which is an example of a factor considered in a points system?', ['Language ability, such as English or French skills', 'Favourite sports team', 'Favourite type of weather', 'Shoe size'], 0),
    ('Why is language ability often an important factor for newcomers?', ['It can help newcomers communicate and find work in their new community', 'It has no effect on daily life', 'It is never considered important', 'It only matters for tourists'], 0),
    ('Learning about the immigration points system helps students understand ___.', ['How Canada decides who may immigrate to the country', 'That immigration decisions are made without any process', 'That Canada does not allow immigration', 'That points systems are used only for sports'], 0)]),
]),
day(153, [
L('Reading: Understanding Hyperbole',
  'Grade 3 Language strand: hyperbole is an extreme exaggeration used for effect, not meant to be taken literally, such as saying I am so hungry I could eat a horse.',
  [('What is hyperbole?', ['An extreme exaggeration used for effect', 'A statement that is always literally true', 'A type of punctuation mark', 'A silent letter in a word'], 0),
   ('Which sentence is an example of hyperbole?', ['I have told you a million times to clean your room.', 'I have told you three times to clean your room.', 'I asked you to clean your room.', 'Please clean your room today.'], 0),
   ('Is hyperbole meant to be taken literally?', ['No, it is meant to be understood as exaggeration', 'Yes, every word is exactly true', 'It has no meaning at all', 'It is always a factual measurement'], 0),
   ('Why might a writer use hyperbole?', ['To create a strong or humorous effect', 'To confuse the reader with facts', 'To remove all feeling from writing', 'To make writing perfectly literal'], 0),
   ('Which phrase uses hyperbole?', ['This bag weighs a ton.', 'This bag weighs five kilograms.', 'This bag is blue.', 'This bag is on the table.'], 0)]),
M('Data: Reading Simple Circle Graphs',
  'Grade 3 Math strand: a circle graph, also called a pie chart, shows how a whole set of data is divided into parts, with each slice representing a portion of the total.',
  [('What does a circle graph show?', ['How a whole set of data is divided into parts', 'Only a single number with no context', 'A list of names in alphabetical order', 'A single line moving up and down'], 0),
   ('What is another name for a circle graph?', ['A pie chart', 'A bar graph', 'A line plot', 'A tally chart'], 0),
   ('In a circle graph, a larger slice represents ___.', ['A larger portion of the total data', 'A smaller portion of the total data', 'No data at all', 'The exact same amount every time'], 0),
   ('If a circle graph shows favourite fruits and the apple slice is the biggest, what does that mean?', ['Apple was chosen by the most people', 'Apple was chosen by the fewest people', 'No one chose apple', 'Everyone chose a different fruit'], 0),
   ('Why might data be shown in a circle graph instead of a list of numbers?', ['To make it easy to compare parts of a whole visually', 'To hide the data completely', 'To remove all numbers from the data', 'To make the data impossible to read'], 0)]),
Sc('Science: Carnivorous Plants — Unusual Ways of Getting Nutrients',
   'Grade 3 Science strand: carnivorous plants, such as the Venus flytrap and pitcher plant, capture and digest insects to get nutrients that are often missing from the poor soil where they grow.',
   [('What do carnivorous plants capture and digest?', ['Insects', 'Only sunlight', 'Only rocks', 'Only rainwater'], 0),
    ('Which is an example of a carnivorous plant?', ['The Venus flytrap', 'A sunflower', 'An apple tree', 'A rose bush'], 0),
    ('Why do carnivorous plants often capture insects for nutrients?', ['They often grow in poor soil that lacks certain nutrients', 'They dislike sunlight completely', 'They cannot grow roots at all', 'They never need any nutrients'], 0),
    ('How does a Venus flytrap capture its prey?', ['Its leaves snap shut when an insect touches trigger hairs', 'It chases insects across the ground', 'It sprays water at insects', 'It waits underground for insects'], 0),
    ('What do carnivorous plants have in common with other plants?', ['They still use sunlight to make some of their own food', 'They never use sunlight at all', 'They have no leaves or roots', 'They cannot survive in soil'], 0)]),
SS('Social Studies: Canada Post and How Mail Is Delivered',
   'Grade 3 Social Studies strand: Canada Post is the national postal service that collects, sorts, and delivers letters and packages to homes and businesses across the country.',
   [('What is Canada Post?', ['The national postal service that delivers letters and packages', 'A type of national park', 'A type of grocery store', 'A private airline'], 0),
    ('What are some of the main jobs of a postal service?', ['Collecting, sorting, and delivering mail', 'Selling groceries', 'Repairing roads', 'Teaching students'], 0),
    ('Why might someone use the mail to send a letter or package?', ['To communicate or send items to people in other places', 'To avoid all communication', 'Because mail cannot travel far', 'Because mail is never delivered'], 0),
    ('What might a postal worker do to make sure mail reaches the right address?', ['Sort mail carefully by postal code and address', 'Deliver mail to random locations', 'Ignore the address on each item', 'Throw mail away instead of delivering it'], 0),
    ('Why is a reliable postal service important to a country?', ['It helps people and businesses stay connected across long distances', 'It has no importance to communities', 'It only matters in one city', 'It replaces the need for phones and computers'], 0)]),
]),
day(154, [
L('Writing: Writing a Fable with a Moral',
  'Grade 3 Language strand: a fable is a short story, often featuring animal characters, that ends with a moral, or lesson, meant to teach the reader something about life.',
  [('What is a fable?', ['A short story, often with animal characters, that teaches a lesson', 'A long chapter book with no lesson', 'A list of facts about animals', 'A poem with no characters'], 0),
   ('What is a moral in a fable?', ['The lesson the story is meant to teach', 'The title of the story', 'The name of the author', 'The setting of the story'], 0),
   ('Why do fables often use animal characters?', ['Animal characters can represent human behaviours in a simple, memorable way', 'Animals cannot be characters in stories', 'Fables never include characters', 'Animal characters make the story impossible to understand'], 0),
   ('Which is an example of a moral from a fable?', ['Slow and steady wins the race.', 'The weather was sunny today.', 'The characters name was Sam.', 'The story took place in a forest.'], 0),
   ('Why might a writer choose to write a fable instead of another kind of story?', ['To teach an important lesson in a short, engaging way', 'To avoid teaching anything at all', 'To make the story as long as possible', 'To remove any meaning from the story'], 0)]),
M('Fractions: Fractions That Equal One Whole',
  'Grade 3 Math strand: a fraction is equal to one whole when its numerator and denominator are the same number, such as 3/3 or 5/5, since all the equal parts of the whole have been counted.',
  [('Which fraction is equal to one whole?', ['4/4', '1/4', '3/4', '2/4'], 0),
   ('A fraction equals one whole when ___.', ['The numerator and denominator are the same number', 'The numerator is zero', 'The denominator is zero', 'The numerator is greater than the denominator'], 0),
   ('Which fraction is equal to one whole?', ['6/6', '5/6', '1/6', '4/6'], 0),
   ('If a pizza is cut into 8 equal slices and all 8 are eaten, what fraction of the pizza was eaten?', ['8/8', '1/8', '4/8', '7/8'], 0),
   ('Why does 3/3 represent one whole?', ['All three equal parts of the whole have been counted', 'Only one part of the whole has been counted', 'No parts of the whole have been counted', 'It represents more than one whole'], 0)]),
Sc('Science: How Mountains Are Formed',
   'Grade 3 Science strand: mountains often form when huge sections of Earths crust, called plates, push against each other over millions of years, slowly forcing the land upward.',
   [('What are the huge sections of Earths crust called?', ['Plates', 'Rivers', 'Clouds', 'Oceans'], 0),
    ('How do many mountains form?', ['Plates in Earths crust push against each other, forcing land upward', 'They appear suddenly overnight', 'They are built entirely by animals', 'They form only from melting ice'], 0),
    ('About how long can it take for a mountain range to form?', ['Millions of years', 'A single day', 'One week', 'A few hours'], 0),
    ('What might happen at the edge where two plates push together?', ['The land can slowly be forced upward, forming mountains', 'Nothing ever happens there', 'The land always sinks into the ocean', 'The plates instantly disappear'], 0),
    ('Why do scientists study how mountains form?', ['To better understand the forces that shape Earths surface', 'Because mountains have no scientific value', 'Because mountains never change', 'Because it explains ocean tides only'], 0)]),
SS('Social Studies: Trade Agreements and Why Countries Sign Them',
   'Grade 3 Social Studies strand: a trade agreement is a deal between countries that sets rules for buying and selling goods and services, often making trade easier and less costly between the countries involved.',
   [('What is a trade agreement?', ['A deal between countries that sets rules for buying and selling goods', 'A type of national holiday', 'A type of weather pattern', 'A single countrys law about sports'], 0),
    ('Why might countries sign a trade agreement?', ['To make trade easier and less costly between them', 'To stop all trade completely', 'To avoid working with any other country', 'To remove all rules about trade'], 0),
    ('What might a trade agreement help reduce between countries?', ['Costs or barriers involved in buying and selling goods', 'The number of people living in a country', 'The size of a countrys mountains', 'The length of a countrys coastline'], 0),
    ('Which is an example of something a trade agreement might cover?', ['Rules about which goods can be bought and sold between countries', 'Rules about a familys home decorations', 'Rules about a school playground', 'Rules about a single persons diet'], 0),
    ('Why might trade agreements matter to people in Canada?', ['They can affect the price and availability of goods people buy', 'They have no effect on daily life at all', 'They only affect people in one city', 'They only apply to a single store'], 0)]),
]),
day(155, [
L('Oral Communication: Paraphrasing What a Speaker Said',
  'Grade 3 Language strand: paraphrasing means restating what a speaker said in your own words, showing that you listened carefully and understood the main idea.',
  [('What does it mean to paraphrase what a speaker said?', ['To restate it in your own words', 'To repeat it word for word', 'To ignore what the speaker said', 'To interrupt the speaker'], 0),
   ('Why might paraphrasing show that you were listening?', ['It shows you understood and can express the main idea yourself', 'It shows you were not paying attention', 'It proves you memorized every single word', 'It has nothing to do with listening'], 0),
   ('Which is an example of paraphrasing?', ['Restating a friends idea using different words that mean the same thing', 'Copying a friends exact words with no changes', 'Ignoring a friends idea completely', 'Changing the topic entirely'], 0),
   ('When might paraphrasing be a useful skill during a discussion?', ['When checking that you understood another persons point correctly', 'When trying to avoid listening at all', 'When trying to confuse the speaker', 'When ending a conversation immediately'], 0),
   ('Paraphrasing is different from quoting because paraphrasing ___.', ['Uses your own words instead of the speakers exact words', 'Uses the exact same words as the speaker', 'Removes the meaning of the original statement', 'Requires no listening at all'], 0)]),
M('Multiplication: Using an Array Model for 2-Digit by 1-Digit Multiplication',
  'Grade 3 Math strand: an array model breaks a 2-digit by 1-digit multiplication problem into smaller, easier parts based on place value, such as splitting 23 x 4 into 20 x 4 and 3 x 4, then adding the results.',
  [('When using an array model for 23 x 4, how might the problem be split by place value?', ['Into 20 x 4 and 3 x 4', 'Into 2 x 4 and 3 x 4 only', 'Into 23 x 40', 'Into 23 x 2 and 23 x 3'], 0),
   ('What is 20 x 4?', ['80', '24', '84', '60'], 0),
   ('Using the array model, what is 23 x 4? (20 x 4 = 80, 3 x 4 = 12)', ['92', '82', '96', '88'], 0),
   ('Why might an array model help with multiplying larger numbers?', ['It breaks a hard problem into smaller, easier parts to add together', 'It removes the need for any calculation', 'It only works for numbers under five', 'It makes multiplication impossible to understand'], 0),
   ('An array model is based on breaking a number apart by ___.', ['Place value', 'Colour', 'Alphabetical order', 'Random guessing'], 0)]),
Sc('Science: Rainbows — How Light and Water Create Them',
   'Grade 3 Science strand: a rainbow forms when sunlight passes through tiny drops of water in the air, and the water bends and separates the light into the colours of the visible spectrum.',
   [('What two things are needed to form a rainbow?', ['Sunlight and tiny drops of water in the air', 'Only clouds and wind', 'Only darkness and snow', 'Only rocks and soil'], 0),
    ('What happens to sunlight as it passes through a raindrop?', ['It bends and separates into different colours', 'It disappears completely', 'It turns into a solid', 'It stops moving entirely'], 0),
    ('Which colour is often seen on the outer edge of a rainbow?', ['Red', 'Blue', 'Green', 'Purple'], 0),
    ('Why might a rainbow appear after a rain shower on a sunny day?', ['Sunlight can pass through the remaining water droplets in the air', 'Rain always blocks sunlight completely', 'Rainbows only appear at night', 'Water droplets remove all colour from light'], 0),
    ('A rainbow shows the colours of the ___.', ['Visible spectrum of light', 'Ocean floor', 'Night sky only', 'Underground rock layers'], 0)]),
SS('Social Studies: The Canadian Coast Guard — Safety on the Water',
   'Grade 3 Social Studies strand: the Canadian Coast Guard helps keep people safe on Canadas oceans, lakes, and rivers, responding to emergencies and supporting search and rescue operations.',
   [('What is a main job of the Canadian Coast Guard?', ['Helping keep people safe on the water', 'Delivering mail', 'Building schools', 'Selling groceries'], 0),
    ('Which is an example of a Coast Guard responsibility?', ['Responding to emergencies on the water', 'Teaching math classes', 'Repairing city streets', 'Running a restaurant'], 0),
    ('What kind of operations does the Coast Guard support?', ['Search and rescue operations', 'Only fashion shows', 'Only concerts', 'Only farming operations'], 0),
    ('Where might the Canadian Coast Guard operate?', ['Canadas oceans, lakes, and rivers', 'Only inside office buildings', 'Only on mountain trails', 'Only in deserts'], 0),
    ('Why is a Coast Guard important to a country with a lot of coastline and waterways?', ['It helps protect people and respond to emergencies on the water', 'It has no real purpose', 'It only matters to one small town', 'It replaces the need for any other safety service'], 0)]),
]),
day(156, [
L('Grammar: Correcting Double Negatives',
  'Grade 3 Language strand: a double negative happens when two negative words are used in the same sentence, which can confuse the meaning, so writers use only one negative word to express a negative idea.',
  [('What is a double negative?', ['Using two negative words in the same sentence', 'Using two positive words in a sentence', 'A sentence with no verb', 'A sentence with two subjects'], 0),
   ('Which sentence contains a double negative?', ['I do not have no pencils.', 'I do not have any pencils.', 'I have some pencils.', 'I have no pencils.'], 0),
   ('How can a double negative be corrected?', ['By using only one negative word in the sentence', 'By adding a third negative word', 'By removing all punctuation', 'By making the sentence a question'], 0),
   ('Which sentence correctly avoids a double negative?', ['I do not want anything.', 'I do not want nothing.', 'I want not nothing.', 'I never want nothing at all.'], 0),
   ('Why might double negatives confuse a reader?', ['Two negatives can unintentionally cancel each other out or confuse the meaning', 'They always make a sentence clearer', 'They are required in every sentence', 'They have no effect on meaning at all'], 0)]),
M('Division: Interpreting Remainders in Word Problems',
  'Grade 3 Math strand: when solving a division word problem with a remainder, students must decide what to do with the remainder based on the situation, such as rounding up, dropping it, or reporting it separately.',
  [('If 22 students are put into groups of 4, and 2 students are left over, what should you do with the leftover students in a real situation?', ['Consider adding them to an existing group or forming a smaller group', 'Ignore them completely', 'Send them home', 'Erase them from the problem'], 0),
   ('If you need 25 cookies and each box holds 6, how many boxes must you buy to have enough?', ['5 boxes', '4 boxes', '3 boxes', '6 boxes'], 0),
   ('In the cookie box example, why must you round the quotient up instead of down?', ['Because you need enough cookies, so a partial box is not enough', 'Because rounding up is always required in every division problem', 'Because remainders never matter', 'Because you should always round down'], 0),
   ('If 17 apples are shared equally among 5 baskets, how many apples are left over as a remainder?', ['2', '3', '5', '1'], 0),
   ('Why is it important to think about the situation when interpreting a remainder?', ['Different situations may call for rounding up, rounding down, or reporting the remainder separately', 'Remainders always mean the exact same thing in every situation', 'Remainders should always be ignored', 'Every division problem needs the remainder rounded up'], 0)]),
Sc('Science: Teeth and Their Different Jobs',
   'Grade 3 Science strand: humans have different types of teeth, including incisors for cutting, canines for tearing, and molars for grinding, each shaped to help break down food.',
   [('What job do incisors do?', ['Cutting food', 'Grinding food only', 'Tearing food only', 'Digesting food'], 0),
    ('What job do molars do?', ['Grinding food', 'Cutting food only', 'Tearing food only', 'Sensing taste'], 0),
    ('Which teeth are used mainly for tearing food?', ['Canines', 'Incisors', 'Molars only', 'Wisdom teeth only'], 0),
    ('Why do humans have different types of teeth?', ['Each type is shaped to help break down food in a different way', 'All teeth do the exact same job', 'Teeth have no real purpose', 'Different teeth only affect how a smile looks'], 0),
    ('Why is it important to take care of your teeth?', ['Healthy teeth help you chew food properly and stay healthy', 'Teeth never need any care', 'Teeth have no connection to eating', 'Caring for teeth has no benefit'], 0)]),
SS('Social Studies: Canadas National Sports — Hockey and Lacrosse',
   'Grade 3 Social Studies strand: Canada has two official national sports, ice hockey as the official winter sport and lacrosse as the official summer sport, both recognized in Canadian law.',
   [('Which sport is Canadas official winter national sport?', ['Ice hockey', 'Basketball', 'Soccer', 'Tennis'], 0),
    ('Which sport is Canadas official summer national sport?', ['Lacrosse', 'Baseball', 'Golf', 'Swimming'], 0),
    ('How many official national sports does Canada have?', ['Two', 'One', 'Five', 'Zero'], 0),
    ('Where does lacrosse have deep roots in Canadian history?', ['It has roots in games played by Indigenous peoples long before Confederation', 'It was invented in the last ten years', 'It has no connection to Canadian history', 'It began as a European royal sport'], 0),
    ('Why might a country officially recognize national sports?', ['To celebrate sports that are an important part of its culture and history', 'To discourage people from playing sports', 'Because national sports have no cultural meaning', 'To replace all other sports completely'], 0)]),
]),
day(157, [
L('Vocabulary: Palindromes — Words That Read the Same Backwards',
  'Grade 3 Language strand: a palindrome is a word or phrase that reads the same forwards and backwards, such as mom, pop, and level.',
  [('What is a palindrome?', ['A word or phrase that reads the same forwards and backwards', 'A word with no vowels', 'A word that rhymes with another word', 'A type of punctuation mark'], 0),
   ('Which of these words is a palindrome?', ['Level', 'Happy', 'Jumping', 'Yellow'], 0),
   ('Which of these words is a palindrome?', ['Mom', 'Dad only backwards spells something else', 'Family', 'Sister'], 0),
   ('How can you check if a word is a palindrome?', ['Read the letters backwards and see if they match the original word', 'Count the number of vowels only', 'Check if the word rhymes with another word', 'Check if the word has more than five letters'], 0),
   ('Why might palindromes be fun to explore in word study?', ['They reveal interesting patterns in how letters can be arranged', 'They have no patterns at all', 'They always contain silent letters', 'They are never real words'], 0)]),
M('Measurement: Comparing Volume and Capacity',
  'Grade 3 Math strand: volume is the amount of space an object takes up, while capacity is the amount a container can hold, and both are commonly measured using units such as litres and millilitres.',
  [('What does volume measure?', ['The amount of space an object takes up', 'The weight of an object', 'The temperature of an object', 'The colour of an object'], 0),
   ('What does capacity measure?', ['The amount a container can hold', 'The length of an object', 'The mass of an object', 'The speed of an object'], 0),
   ('Which unit is commonly used to measure capacity?', ['Litres', 'Metres', 'Grams', 'Degrees'], 0),
   ('If a jug can hold 2 litres of water, what is being described?', ['Its capacity', 'Its mass', 'Its length', 'Its temperature'], 0),
   ('How are volume and capacity related?', ['Capacity describes how much volume a container can hold', 'They are completely unrelated ideas', 'Capacity only applies to solids', 'Volume only applies to liquids'], 0)]),
Sc('Science: Beetles — The Largest Group of Insects',
   'Grade 3 Science strand: beetles make up the largest group of insects on Earth, and most beetles have a hard pair of outer wings that protect a second pair of wings used for flying.',
   [('What makes beetles unique among insect groups?', ['They make up the largest group of insects on Earth', 'They are the smallest group of insects', 'They have no wings at all', 'They only live underwater'], 0),
    ('What protects a beetles flying wings?', ['A hard pair of outer wings', 'A layer of fur', 'A shell made of ice', 'Nothing protects them'], 0),
    ('How many pairs of wings do most beetles have?', ['Two pairs', 'One pair', 'Three pairs', 'No wings at all'], 0),
    ('Which is an example of a beetle?', ['A ladybird beetle', 'A honeybee', 'A dragonfly', 'A butterfly'], 0),
    ('Why do scientists find beetles interesting to study?', ['There are more known beetle species than almost any other group of animals', 'Beetles do not actually exist', 'Beetles are identical to birds', 'Beetles have no scientific importance'], 0)]),
SS('Social Studies: Ensuring Access to Clean Drinking Water',
   'Grade 3 Social Studies strand: communities work to ensure everyone has access to clean, safe drinking water through infrastructure such as water treatment systems, pipes, and wells, though some communities still face challenges.',
   [('Why is access to clean drinking water important?', ['Clean water is essential for health and daily life', 'Clean water has no importance to communities', 'Only some people need water to survive', 'Water quality never affects health'], 0),
    ('Which is an example of infrastructure that helps provide clean water?', ['Water treatment systems and pipes', 'Movie theatres', 'Shopping malls', 'Sports stadiums'], 0),
    ('What challenge do some communities in Canada still face regarding water?', ['Some communities do not yet have consistent access to clean drinking water', 'Every community has always had perfect water access', 'Water access has never been a challenge anywhere', 'Only large cities need clean water'], 0),
    ('Why might governments invest in improving water infrastructure?', ['To help ensure all communities have access to safe, clean water', 'To make water more difficult to access', 'Because water infrastructure has no benefit', 'To remove water access from communities'], 0),
    ('Learning about access to clean water helps students understand ___.', ['That reliable infrastructure is important for community wellbeing', 'That water access is guaranteed everywhere with no effort', 'That clean water has no connection to health', 'That only wealthy countries need clean water'], 0)]),
]),
day(158, [
L('Reading: Distinguishing Formal and Informal Language',
  'Grade 3 Language strand: formal language is more polished and structured, often used in school work or professional writing, while informal language is casual and relaxed, often used with friends and family.',
  [('What is formal language often used for?', ['School work or professional writing', 'Talking casually with close friends', 'Texting family members only', 'Never used in any situation'], 0),
   ('What is informal language often used for?', ['Casual conversations with friends and family', 'Official government documents', 'A formal research report', 'A professional email to a stranger'], 0),
   ('Which sentence uses more formal language?', ['I would like to request additional information.', 'Hey, can you tell me more?', 'Whats up, tell me more!', 'Gimme more info please.'], 0),
   ('Why might a writer choose formal language for a school report?', ['To sound clear, polished, and appropriate for the audience', 'To confuse the reader on purpose', 'Because formal language has no purpose', 'To avoid being understood at all'], 0),
   ('Recognizing the difference between formal and informal language helps writers ___.', ['Choose language appropriate for their audience and purpose', 'Use the exact same style in every situation', 'Avoid writing to different audiences', 'Ignore who will be reading their writing'], 0)]),
M('Patterning: Patterns with Two Attributes — Shape and Colour',
  'Grade 3 Math strand: a pattern can be based on more than one attribute at the same time, such as shape and colour changing together in a repeating sequence.',
  [('What does it mean for a pattern to have two attributes?', ['Two features, such as shape and colour, change together in the pattern', 'Only one feature ever changes', 'The pattern has no repeating part', 'The pattern uses only numbers'], 0),
   ('In the pattern red circle, blue square, red circle, blue square, which two attributes are changing?', ['Colour and shape', 'Only colour', 'Only shape', 'Neither colour nor shape'], 0),
   ('What comes next in this pattern: red circle, blue square, red circle, blue square, ___?', ['Red circle', 'Green triangle', 'Blue square', 'Yellow star'], 0),
   ('Why might a pattern with two attributes be more challenging than a pattern with one?', ['You must track more than one changing feature at the same time', 'It only uses a single colour', 'It never repeats at all', 'It has no attributes to track'], 0),
   ('Identifying the core of a two-attribute pattern means finding ___.', ['The smallest repeating part that includes both attributes', 'Only the first shape in the pattern', 'A part of the pattern that never repeats', 'The largest shape in the pattern'], 0)]),
Sc('Science: The Life Cycle of a Sea Turtle',
   'Grade 3 Science strand: a sea turtle begins life as an egg buried in sand on a beach, hatches and crawls to the ocean, and grows over many years into an adult that eventually returns to lay its own eggs.',
   [('Where do sea turtle eggs begin their life cycle?', ['Buried in sand on a beach', 'Deep underwater in a cave', 'On top of a mountain', 'Inside a floating iceberg'], 0),
    ('What do baby sea turtles do after hatching?', ['Crawl from the sand to the ocean', 'Stay buried in the sand forever', 'Fly to a new location', 'Climb a tree'], 0),
    ('About how does a sea turtles life cycle end up completing?', ['An adult sea turtle eventually returns to a beach to lay its own eggs', 'A sea turtle never grows into an adult', 'A sea turtle never lays eggs', 'A sea turtle stays as an egg forever'], 0),
    ('Why is the journey from the sand to the ocean risky for baby sea turtles?', ['Predators and other dangers can threaten the hatchlings along the way', 'The journey is always completely safe', 'Baby sea turtles cannot move at all', 'The ocean is not connected to the beach'], 0),
    ('Why do scientists study sea turtle life cycles?', ['To help protect sea turtles and understand their needs', 'Because sea turtles have no scientific value', 'Because sea turtles never face any threats', 'Because sea turtles do not lay eggs'], 0)]),
SS('Social Studies: Self-Government and Territorial Governments in the North',
   'Grade 3 Social Studies strand: Canadas three territories, Yukon, the Northwest Territories, and Nunavut, each have their own territorial governments that make decisions about many local matters, with Nunavut created in part to support Inuit self-government.',
   [('How many territories does Canada have?', ['Three', 'One', 'Five', 'Ten'], 0),
    ('What can a territorial government make decisions about?', ['Many local matters affecting people in the territory', 'Only decisions made in another country', 'Nothing at all', 'Only decisions about other provinces'], 0),
    ('Which territory was created in part to support Inuit self-government?', ['Nunavut', 'Yukon', 'The Northwest Territories', 'Ontario'], 0),
    ('Why might self-government be important to a community?', ['It allows a community to make decisions that reflect its own needs and culture', 'It removes all decision-making from a community', 'It has no connection to a communitys needs', 'It only benefits people outside the community'], 0),
    ('Learning about territorial governments helps students understand ___.', ['How different regions of Canada are governed', 'That Canada has only one type of government everywhere', 'That territories have no government at all', 'That only provinces can make local decisions'], 0)]),
]),
day(159, [
L('Writing: Writing an Acrostic Poem',
  'Grade 3 Language strand: an acrostic poem uses the letters of a word, spelled out vertically, as the first letter of each line, with each line often describing or relating to that word.',
  [('What does an acrostic poem use as the first letter of each line?', ['The letters of a chosen word, spelled out vertically', 'A random letter each time', 'Only the letter A', 'No letters at all'], 0),
   ('What do the lines of an acrostic poem often describe?', ['Something related to the chosen word', 'A completely unrelated topic', 'Nothing at all', 'Only numbers'], 0),
   ('If the word SUN is used for an acrostic poem, how many lines would the poem likely have?', ['Three', 'One', 'Ten', 'Zero'], 0),
   ('Why might a writer choose to write an acrostic poem?', ['To creatively explore ideas connected to a specific word', 'To avoid using any letters', 'To write without any structure at all', 'To remove all meaning from a poem'], 0),
   ('An acrostic poem is a fun way to practise ___.', ['Word choice and creative writing', 'Long division', 'Map reading', 'Scientific measurement'], 0)]),
M('Financial Literacy: Comparing the Cost of Multiple Items to Find the Best Deal',
  'Grade 3 Math strand: students compare the total cost and quantity of similar items to determine which option offers the best value, such as comparing the price per item in different sized packages.',
  [('If a pack of 4 pencils costs 8 dollars, what is the cost per pencil?', ['2 dollars', '4 dollars', '8 dollars', '1 dollar'], 0),
   ('If pack A has 4 pencils for 8 dollars and pack B has 5 pencils for 15 dollars, which pack costs less per pencil?', ['Pack A', 'Pack B', 'They cost the same per pencil', 'Cannot be determined'], 0),
   ('Why is it useful to compare the cost per item when shopping?', ['It helps you find the better value between two options', 'It always makes items more expensive', 'It has no effect on spending decisions', 'It only works for buying one item at a time'], 0),
   ('If a large box of 10 markers costs 20 dollars, what is the cost per marker?', ['2 dollars', '10 dollars', '20 dollars', '5 dollars'], 0),
   ('What does it mean to find the best deal?', ['To find the option that offers the most value for the price paid', 'To always choose the most expensive item', 'To ignore the price of every item', 'To buy the largest quantity regardless of cost'], 0)]),
Sc('Science: Why Sleep Is Important for a Healthy Body',
   'Grade 3 Science strand: sleep gives the body time to rest, repair itself, and support growth, and getting enough sleep helps the brain and body function well during the day.',
   [('What does sleep give the body time to do?', ['Rest, repair itself, and support growth', 'Stop growing completely', 'Digest food only', 'Nothing important at all'], 0),
    ('Why might not getting enough sleep affect how someone feels during the day?', ['The brain and body need enough rest to function well', 'Sleep has no effect on how the body feels', 'Sleep only affects eyesight', 'Sleep only matters for adults'], 0),
    ('Which is a healthy habit that can support good sleep?', ['Having a regular bedtime routine', 'Staying awake as long as possible every night', 'Avoiding sleep completely', 'Sleeping only once a month'], 0),
    ('Why is sleep especially important for growing children?', ['Sleep supports healthy growth and development', 'Sleep has no connection to growth', 'Children do not need any sleep', 'Sleep only matters for the heart'], 0),
    ('What might happen if a person consistently does not get enough sleep?', ['They may feel tired and find it harder to focus', 'They will instantly become taller', 'Nothing at all would change', 'Their body would need no more rest ever'], 0)]),
SS('Social Studies: Settlement Services That Help Newcomers to Canada',
   'Grade 3 Social Studies strand: settlement services help newcomers adjust to life in Canada by offering support such as language classes, help finding housing, and information about the community.',
   [('What is one purpose of settlement services?', ['To help newcomers adjust to life in Canada', 'To prevent newcomers from settling anywhere', 'To remove newcomers from the community', 'To ignore the needs of newcomers'], 0),
    ('Which is an example of a settlement service?', ['Language classes to help newcomers learn English or French', 'A closed store with no services offered', 'A private club with no public access', 'A service that only helps long-time residents'], 0),
    ('How might settlement services help a newcomer family find a home?', ['By offering support and information about finding housing', 'By refusing to provide any housing information', 'By requiring families to find housing with no help', 'By removing housing options completely'], 0),
    ('Why might communities offer settlement services to newcomers?', ['To help newcomers feel welcome and successfully join the community', 'To make it harder for newcomers to adjust', 'Because newcomers need no support at all', 'To discourage immigration completely'], 0),
    ('Learning about settlement services helps students understand ___.', ['How communities support newcomers in building a new life', 'That newcomers receive no support at all', 'That settlement services do not exist in Canada', 'That only large cities welcome newcomers'], 0)]),
]),
day(160, [
L('Language Review: Colons, Fables, and Paraphrasing',
  'Grade 3 Language strand review: students revisit using colons before lists, loanwords, hyperbole, writing a fable with a moral, paraphrasing what a speaker said, correcting double negatives, palindromes, formal and informal language, and writing an acrostic poem.',
  [('What can a colon introduce after a complete sentence?', ['A list of items', 'A brand new paragraph', 'A single silent letter', 'A page number'], 0),
   ('What is a loanword?', ['A word that English has borrowed from another language', 'A word with no meaning at all', 'A word used only in math', 'A punctuation mark'], 0),
   ('What is a moral in a fable?', ['The lesson the story is meant to teach', 'The title of the story', 'The name of the author', 'The setting of the story'], 0),
   ('What is a double negative?', ['Using two negative words in the same sentence', 'Using two positive words in a sentence', 'A sentence with no verb', 'A sentence with two subjects'], 0),
   ('What is a palindrome?', ['A word or phrase that reads the same forwards and backwards', 'A word with no vowels', 'A word that rhymes with another word', 'A type of punctuation mark'], 0)]),
M('Math Review: Composing Numbers, Fractions, and Data',
  'Grade 3 Math strand review: students revisit composing and decomposing numbers, prisms and pyramids, reading circle graphs, fractions that equal one whole, the array model for multiplication, interpreting remainders, comparing volume and capacity, patterns with two attributes, and comparing costs to find the best deal.',
  [('What does it mean to decompose a number?', ['To break it apart into smaller parts that add up to the whole', 'To multiply it by ten', 'To erase the number completely', 'To turn it into a fraction'], 0),
   ('How many bases does a pyramid have?', ['One base', 'Two bases', 'Three bases', 'No bases at all'], 0),
   ('A fraction equals one whole when ___.', ['The numerator and denominator are the same number', 'The numerator is zero', 'The denominator is zero', 'The numerator is greater than the denominator'], 0),
   ('What does capacity measure?', ['The amount a container can hold', 'The length of an object', 'The mass of an object', 'The speed of an object'], 0),
   ('What does it mean to find the best deal?', ['To find the option that offers the most value for the price paid', 'To always choose the most expensive item', 'To ignore the price of every item', 'To buy the largest quantity regardless of cost'], 0)]),
Sc('Science Review: Space, Ocean Life, and the Human Body',
   'Grade 3 Science strand review: students revisit the order of the planets, octopuses, carnivorous plants, how mountains are formed, rainbows, teeth and their jobs, beetles, the life cycle of a sea turtle, and why sleep is important.',
   [('Which planet is closest to the Sun?', ['Mercury', 'Venus', 'Earth', 'Mars'], 0),
    ('What is unusual about an octopuses body?', ['It has no internal skeleton', 'It has a hard shell like a turtle', 'It has fur covering its body', 'It has wings for flying'], 0),
    ('What are the huge sections of Earths crust called?', ['Plates', 'Rivers', 'Clouds', 'Oceans'], 0),
    ('What job do molars do?', ['Grinding food', 'Cutting food only', 'Tearing food only', 'Sensing taste'], 0),
    ('What does sleep give the body time to do?', ['Rest, repair itself, and support growth', 'Stop growing completely', 'Digest food only', 'Nothing important at all'], 0)]),
SS('Social Studies Review: Immigration, Trade, and Public Services',
   'Grade 3 Social Studies strand review: students revisit national historic sites, the immigration points system, Canada Post, trade agreements, the Canadian Coast Guard, Canadas national sports, access to clean drinking water, self-government in the territories, and settlement services for newcomers.',
   [('What is a national historic site?', ['A place recognized for its importance to Canadas history', 'A type of grocery store', 'A type of weather station', 'A brand new shopping mall'], 0),
    ('What does Canadas immigration points system evaluate?', ['Factors such as education, work experience, and language skills', 'Only a persons favourite colour', 'Only a persons height', 'Only a persons birthday'], 0),
    ('What is a trade agreement?', ['A deal between countries that sets rules for buying and selling goods', 'A type of national holiday', 'A type of weather pattern', 'A single countrys law about sports'], 0),
    ('How many territories does Canada have?', ['Three', 'One', 'Five', 'Ten'], 0),
    ('What is one purpose of settlement services?', ['To help newcomers adjust to life in Canada', 'To prevent newcomers from settling anywhere', 'To remove newcomers from the community', 'To ignore the needs of newcomers'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_151_160, seed=20260809)
    append_to(3, g3_151_160)
