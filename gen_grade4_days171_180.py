#!/usr/bin/env python3
"""Grade 4, Days 171-180 -- extends Grade 4 from 170 to 180 days. Modeled
exactly on gen_grade4_days161_170.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-170
topics (verified against data/grade4.json, which already densely covers
nearly the entire grade 4 curriculum, including the immediately prior
Days 161-170 batch). New topics: relative adverbs, subjunctive mood,
writing a folk tale, analyzing a plays structure, writing a limerick,
distinguishing denotation from connotation in poetry, writing a
persuasive speech, understanding allegory, and commonly confused words
(its and its) for Language; classifying quadrilaterals by parallel sides,
dividing a 4-digit number by a 1-digit divisor, calculating the mean of a
data set, using Venn diagrams for factors and multiples, converting
between fractions and decimals, calculating perimeter using algebraic
expressions, probability of independent events, estimating square roots,
and reading and interpreting a budget for Math; the water table and
aquifer recharge, the rock-paper-scissors of predator-prey cycles, the
digestive system of ruminant animals, the northern lights (aurora
borealis), how vaccines work, wetlands and marshes as ecosystems, the
process of fermentation, and the structure of the human eye for Science;
and the Underground Railroad conductors, the Hudson Strait and Arctic
shipping routes, the role of the Auditor General, the history of
residential schools and the path to reconciliation, Canadas peacekeeping
in the Suez Crisis, the Rideau Canal, municipal bylaws, and the role of
the Canadian Radio-television and Telecommunications Commission (CRTC)
for Social Studies -- none of those exact ideas appear in Days 1-170
(note: Days 1-170 already cover the Underground Railroad and Canada,
National Day for Truth and Reconciliation, and Canadas peacekeeping role
internationally in general terms, so this batchs Social Studies topics
narrow to a specific, previously-untouched angle for each: Underground
Railroad conductors specifically, rather than the Underground Railroad
overall; the history of residential schools and the path toward
reconciliation specifically, distinct from the National Day for Truth and
Reconciliation itself; and the Suez Crisis specifically, distinct from
Canadas peacekeeping role internationally in general). Day 180 is a
review day across all four subjects, matching the end-of-batch pattern
used in every prior 10-day batch (one representative question drawn from
each of the first five lessons of the batch, per subject, exactly as Day
170 did for Days 161-165). The four Day 180 review titles (Language
Review: Adverbs, Mood, and Storytelling Forms / Math Review: Quadrilaterals,
Division, and Data / Science Review: Water, Ecosystems, and the Human Body
/ Social Studies Review: Freedom Seekers, Arctic Geography, and Government
Oversight) were checked against every earlier review-day title in Days
1-170, including Day 140, Day 150, Day 160, Day 170, and every "Review:
... (Days X-Y)" day, and are textually distinct from all of them. No
embedded ASCII double-quote or apostrophe characters are used anywhere in
title/summary/question/option text, matching the convention used in
gen_grade4_days161_170.py (apostrophes dropped entirely, e.g. "Canadas"
not "Canada's").
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


def _rebalance_answer_positions(days, seed=20260825):
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


g4_171_180 = [
day(171, [
L('Grammar: Relative Adverbs — Where, When, and Why',
  'Grade 4 Language strand: relative adverbs, including where, when, and why, introduce a clause that describes a noun by giving information about a place, time, or reason.',
  [('Which relative adverb describes a place?', ['Where', 'When', 'Why', 'Who'], 0),
   ('Which relative adverb describes a time?', ['When', 'Where', 'Why', 'Which'], 0),
   ('Which relative adverb describes a reason?', ['Why', 'When', 'Where', 'What'], 0),
   ('Which sentence correctly uses a relative adverb?', ['This is the park where we played soccer.', 'This is the park who we played soccer.', 'This is the park which we played soccer.', 'This is the park whom we played soccer.'], 0),
   ('Why are relative adverbs useful in writing?', ['They add detail about place, time, or reason to a noun being described', 'They always change a sentence into a question', 'They remove the need for a verb', 'They only appear at the very start of a sentence'], 0)]),
M('Geometry: Classifying Quadrilaterals by Parallel Sides',
  'Grade 4 Math strand: quadrilaterals can be classified by their parallel sides, including parallelograms with two pairs of parallel sides, trapezoids with exactly one pair of parallel sides, and quadrilaterals with no parallel sides at all.',
  [('What defines a parallelogram?', ['It has two pairs of parallel sides', 'It has exactly one pair of parallel sides', 'It has no parallel sides', 'It has five sides'], 0),
   ('What defines a trapezoid?', ['It has exactly one pair of parallel sides', 'It has two pairs of parallel sides', 'It has no straight sides', 'It always has four equal angles'], 0),
   ('Can a quadrilateral have zero pairs of parallel sides?', ['Yes, some quadrilaterals have no parallel sides at all', 'No, every quadrilateral must have parallel sides', 'No, all four-sided shapes are parallelograms', 'Yes, but only if it has five sides'], 0),
   ('Is a square considered a type of parallelogram?', ['Yes, because it has two pairs of parallel sides', 'No, squares never have parallel sides', 'No, squares are a completely separate category', 'Yes, but only when rotated'], 0),
   ('Why is it useful to classify quadrilaterals by their parallel sides?', ['It helps identify and compare the properties of different four-sided shapes', 'Classifying quadrilaterals has no mathematical value', 'All quadrilaterals are exactly identical', 'Parallel sides have no connection to shape properties'], 0)]),
Sc('Science: The Water Table and Aquifer Recharge',
   'Grade 4 Science strand: the water table is the upper level of groundwater stored underground in an aquifer, and it rises or falls as rain and melting snow soak into the ground to recharge the supply.',
   [('What is the water table?', ['The upper level of groundwater stored underground', 'A table used to measure rainfall', 'A type of river on the surface', 'A machine used to pump ocean water'], 0),
    ('What is an aquifer?', ['An underground layer of rock or soil that stores groundwater', 'A type of cloud formation', 'A machine that purifies water', 'A surface lake found only in deserts'], 0),
    ('What can cause the water table to rise?', ['Rain and melting snow soaking into the ground', 'A long period with no precipitation at all', 'Paving over natural land with concrete', 'Removing water without any replacement'], 0),
    ('What does it mean for an aquifer to be recharged?', ['Water is added back into it from rain or snowmelt seeping down', 'The aquifer is permanently emptied', 'The aquifer turns into solid rock', 'The aquifer stops storing water forever'], 0),
    ('Why is it important for communities to manage groundwater use carefully?', ['Overusing groundwater faster than it recharges can lower the water table', 'Groundwater can never be used up', 'Aquifers refill instantly no matter how much is used', 'Groundwater has no connection to drinking water supplies'], 0)]),
SS('Social Studies: Conductors of the Underground Railroad',
   'Grade 4 Social Studies strand: conductors of the Underground Railroad were brave individuals, such as Harriet Tubman, who guided freedom seekers along secret routes and through safe houses toward freedom in Canada.',
   [('What was the role of a conductor on the Underground Railroad?', ['Guiding freedom seekers along secret routes toward freedom', 'Building railway tracks across Canada', 'Collecting taxes from travellers', 'Repairing roads between towns'], 0),
    ('Who is one of the most famous conductors of the Underground Railroad?', ['Harriet Tubman', 'John A. Macdonald', 'Laura Secord', 'Terry Fox'], 0),
    ('What made the work of a conductor dangerous?', ['Helping freedom seekers escape was illegal and risked severe punishment', 'Conductors were paid too much money', 'Conductors only worked during safe, sunny weather', 'There was no risk involved at all'], 0),
    ('What were the hidden stopping points along the Underground Railroad often called?', ['Safe houses', 'Train stations', 'Town halls', 'Marketplaces'], 0),
    ('Why are Underground Railroad conductors remembered as important historical figures?', ['They risked their own safety to help others reach freedom', 'They have no connection to Canadian history', 'They worked only to build literal railroads', 'They discouraged people from seeking freedom'], 0)]),
]),
day(172, [
L('Grammar: The Subjunctive Mood',
  'Grade 4 Language strand: the subjunctive mood is used to express a wish, a suggestion, or a situation that is not currently true, often appearing after words like if or wish and pairing with were instead of was.',
  [('What does the subjunctive mood often express?', ['A wish or a situation that is not currently true', 'A simple fact that is happening right now', 'A direct command', 'A question about a location'], 0),
   ('Which sentence correctly uses the subjunctive mood?', ['If I were taller, I could reach the shelf.', 'If I was taller, I could reach the shelf.', 'If I am taller, I could reach the shelf.', 'If I be taller, I could reach the shelf.'], 0),
   ('Which word often introduces a subjunctive statement?', ['If', 'And', 'But', 'So'], 0),
   ('In the subjunctive mood, which verb form is often used instead of was?', ['Were', 'Is', 'Being', 'Been'], 0),
   ('Why might a writer use the subjunctive mood?', ['To describe a wish or hypothetical situation that is not real', 'To describe something that is definitely true right now', 'To give a simple command', 'To ask a direct question'], 0)]),
M('Number Sense: Dividing a 4-Digit Number by a 1-Digit Divisor',
  'Grade 4 Math strand: dividing a 4-digit number by a 1-digit divisor involves working through the digits from left to right, dividing, multiplying, subtracting, and bringing down the next digit at each step.',
  [('What is a common first step when dividing a 4-digit number by a 1-digit divisor?', ['Start by dividing the leftmost digit or digits by the divisor', 'Start by dividing the rightmost digit by the divisor', 'Add the divisor to the 4-digit number', 'Multiply the two numbers together'], 0),
   ('What is 4,236 divided by 2?', ['2,118', '2,108', '2,218', '2,128'], 0),
   ('What is 5,145 divided by 5?', ['1,029', '1,030', '1,019', '1,039'], 0),
   ('After dividing and multiplying at each step, what should you do next?', ['Subtract, then bring down the next digit', 'Multiply again by the same digit', 'Skip the next digit entirely', 'Add the divisor to the quotient'], 0),
   ('Why is it helpful to work through long division one digit at a time?', ['It breaks a large problem into smaller, more manageable steps', 'It always produces an incorrect answer', 'It removes the need for any subtraction', 'It only works with 1-digit dividends'], 0)]),
Sc('Science: Predator-Prey Cycles in Ecosystems',
   'Grade 4 Science strand: predator and prey populations rise and fall in connected cycles, since more prey allows predator populations to grow, while more predators can then cause prey populations to shrink.',
   [('What happens to a predator population when prey becomes more plentiful?', ['The predator population tends to grow', 'The predator population disappears completely', 'The predator population has no reaction at all', 'The predator population instantly doubles overnight'], 0),
    ('What can happen to a prey population when predators become too numerous?', ['The prey population tends to shrink', 'The prey population always grows larger', 'The prey population is unaffected', 'The prey population becomes extinct instantly'], 0),
    ('Why are predator and prey populations described as being in a cycle?', ['Their population sizes rise and fall in a connected, repeating pattern', 'Their populations never change over time', 'Predators and prey have no effect on each other', 'Only prey populations ever change in an ecosystem'], 0),
    ('What might happen if a predator species were removed from an ecosystem entirely?', ['The prey population could grow rapidly without natural control', 'Nothing in the ecosystem would change at all', 'The prey population would disappear immediately', 'Other predators would automatically disappear too'], 0),
    ('Why do scientists study predator-prey cycles?', ['To understand how ecosystems stay balanced over time', 'Predator-prey cycles have no scientific importance', 'Ecosystems never change based on predators or prey', 'Studying these cycles has no real-world use'], 0)]),
SS('Social Studies: The Hudson Strait and Arctic Shipping Routes',
   'Grade 4 Social Studies strand: the Hudson Strait is a waterway connecting Hudson Bay to the Atlantic Ocean, forming part of an important Arctic shipping route used to transport goods to and from northern communities.',
   [('What does the Hudson Strait connect?', ['Hudson Bay to the Atlantic Ocean', 'The Pacific Ocean to the Great Lakes', 'Lake Ontario to Lake Erie', 'The Rocky Mountains to the prairies'], 0),
    ('Why is the Hudson Strait considered important for shipping?', ['It forms part of a route used to transport goods to northern communities', 'It has never been used for transportation', 'It is located entirely on dry land', 'It only connects two small lakes'], 0),
    ('What challenge do ships often face when using Arctic shipping routes?', ['Sea ice can block or limit travel during parts of the year', 'The water is always too warm to sail through', 'There is never any ice in the Arctic', 'Arctic routes are always completely open year-round'], 0),
    ('Why might goods need to be shipped to northern communities by water?', ['Many northern communities are not connected by road', 'All northern communities have major highways', 'Ships are the only form of transportation ever used in Canada', 'Northern communities do not need any supplies delivered'], 0),
    ('Why is understanding Arctic geography important for Canada?', ['It helps Canada manage transportation, trade, and northern communities', 'Arctic geography has no connection to Canada', 'The Arctic has no communities living there', 'Shipping routes never affect daily life'], 0)]),
]),
day(173, [
L('Writing: Writing a Folk Tale',
  'Grade 4 Language strand: a folk tale is a traditional story passed down through generations, often explaining customs or beliefs of a culture and featuring ordinary characters who face a challenge.',
  [('What is a folk tale?', ['A traditional story passed down through generations', 'A scientific report on nature', 'A formal business letter', 'A list of historical dates'], 0),
   ('What might a folk tale often explain?', ['Customs or beliefs of a culture', 'The exact temperature of a region', 'A mathematical formula', 'A companys yearly budget'], 0),
   ('What kind of characters commonly appear in folk tales?', ['Ordinary characters who face a challenge', 'Only scientists conducting experiments', 'Only government officials', 'Only fictional robots'], 0),
   ('How are folk tales traditionally shared between generations?', ['Often through spoken storytelling before being written down', 'Only through official government documents', 'Only through scientific journals', 'They are never shared at all'], 0),
   ('Why might folk tales be valuable to a culture?', ['They preserve traditions, values, and history through storytelling', 'Folk tales have no cultural value', 'Folk tales are always factually accurate reports', 'Folk tales are never passed down to others'], 0)]),
M('Data Management: Calculating the Mean of a Data Set',
  'Grade 4 Math strand: the mean, or average, of a data set is found by adding all the values together and dividing the sum by the number of values in the set.',
  [('How do you calculate the mean of a data set?', ['Add all the values and divide by the number of values', 'Find the largest value only', 'Find the smallest value only', 'Multiply all the values together'], 0),
   ('What is the mean of the data set 4, 6, 8?', ['6', '4', '8', '18'], 0),
   ('What is the mean of the data set 10, 20, 30, 40?', ['25', '20', '30', '100'], 0),
   ('If a data set has five values summing to 50, what is the mean?', ['10', '5', '50', '25'], 0),
   ('Why is the mean a useful way to describe a data set?', ['It gives a single value representing the typical or central amount', 'It only shows the largest value in the set', 'It always equals the smallest value in the set', 'It has no connection to the data set at all'], 0)]),
Sc('Science: Ruminant Animals — How Cows and Other Grazers Digest Grass',
   'Grade 4 Science strand: ruminant animals, such as cows, sheep, and deer, have a specialized four-chambered stomach that allows them to break down tough plant fibres by chewing their food more than once.',
   [('What is a ruminant animal?', ['An animal with a specialized four-chambered stomach for digesting plants', 'An animal that only eats meat', 'An animal that never eats at all', 'An animal that lives only underwater'], 0),
    ('Which of these is an example of a ruminant animal?', ['A cow', 'A lion', 'A shark', 'An eagle'], 0),
    ('What is unique about how ruminant animals digest their food?', ['They chew their food more than once to help break down tough fibres', 'They never chew their food at all', 'They swallow food whole and never digest it', 'They only eat food that has already been digested by another animal'], 0),
    ('What term describes food that a ruminant animal brings back up to chew again?', ['Cud', 'Compost', 'Sap', 'Pollen'], 0),
    ('Why is a multi-chambered stomach helpful for animals that eat grass?', ['It allows tough plant fibres to be broken down more completely for energy', 'It prevents the animal from digesting any food at all', 'It has no effect on digestion', 'It only works for animals that eat meat'], 0)]),
SS('Social Studies: The Role of the Auditor General of Canada',
   'Grade 4 Social Studies strand: the Auditor General is an independent official who examines how the federal government spends public money, reporting to Parliament on whether spending was managed responsibly.',
   [('What does the Auditor General of Canada examine?', ['How the federal government spends public money', 'The weather across Canada', 'The design of new highways', 'The scores of national sports teams'], 0),
    ('Who does the Auditor General report to?', ['Parliament', 'A private company', 'A foreign government', 'No one at all'], 0),
    ('Why is the Auditor General considered independent?', ['They examine government spending without taking political sides', 'They always agree with whatever the government wants', 'They are controlled by a single business', 'They have no connection to government spending'], 0),
    ('What is one goal of having an Auditor General?', ['Ensuring public money is spent responsibly and transparently', 'Preventing the government from ever spending any money', 'Removing accountability from government spending', 'Hiding government spending from the public'], 0),
    ('Why is the role of the Auditor General valuable to Canadian citizens?', ['It helps hold government spending accountable to the public', 'It has no value to citizens', 'It gives citizens no information about government spending', 'It only benefits government workers'], 0)]),
]),
day(174, [
L('Reading: Analyzing a Plays Structure — Acts and Scenes',
  'Grade 4 Language strand: a play is organized into acts and scenes, with acts marking major divisions of the story and scenes marking smaller sections within an act, often set in a single time and place.',
  [('What is an act in a play?', ['A major division of the story', 'A single line of dialogue', 'The name of a character', 'A type of stage prop'], 0),
   ('What is a scene in a play?', ['A smaller section within an act, often in one time and place', 'The entire play from start to finish', 'A list of actors names', 'A type of costume'], 0),
   ('How are acts and scenes usually organized in relation to each other?', ['A play is divided into acts, and acts are divided into scenes', 'Scenes are divided into acts', 'Acts and scenes are exactly the same thing', 'A play can only have one scene total'], 0),
   ('What might change between one scene and the next?', ['The time or place of the action', 'The title of the play', 'The name of the playwright', 'The type of paper the play is printed on'], 0),
   ('Why is understanding a plays structure of acts and scenes helpful to readers?', ['It helps track how the story is organized and how it progresses', 'Structure has no connection to understanding a play', 'Acts and scenes only exist in novels, not plays', 'It makes a play impossible to follow'], 0)]),
M('Number Sense: Using Venn Diagrams for Factors and Multiples',
  'Grade 4 Math strand: a Venn diagram can be used to compare the factors or multiples of two numbers, showing shared values in the overlapping section and unique values in the separate sections.',
  [('What can a Venn diagram show when comparing two numbers?', ['Their shared and unique factors or multiples', 'Only their sum', 'Only their difference', 'Only their product'], 0),
   ('In a Venn diagram comparing factors, where do shared factors appear?', ['In the overlapping section of the circles', 'Only in the left circle', 'Only in the right circle', 'Outside both circles'], 0),
   ('What are the common factors of 12 and 18 shown in the overlap?', ['1, 2, 3, and 6', '1 and 2 only', '4 and 9 only', '12 and 18 only'], 0),
   ('If comparing multiples of 4 and 6, which number would appear in the overlapping section?', ['12', '4', '6', '10'], 0),
   ('Why is a Venn diagram a useful tool for comparing factors or multiples?', ['It visually organizes shared and unique values for easy comparison', 'It removes the need to know any factors or multiples', 'It only works with a single number', 'It cannot show any shared values'], 0)]),
Sc('Science: The Northern Lights — Aurora Borealis',
   'Grade 4 Science strand: the aurora borealis, or northern lights, is a natural light display caused by charged particles from the sun interacting with gases in Earths atmosphere, most visible near the North Pole.',
   [('What causes the aurora borealis?', ['Charged particles from the sun interacting with Earths atmosphere', 'Reflections of city lights bouncing off clouds', 'A type of volcanic eruption', 'Sunlight passing through raindrops'], 0),
    ('Where is the aurora borealis most commonly visible?', ['Near the North Pole', 'Near the equator', 'In deserts only', 'Underwater'], 0),
    ('What is another common name for the aurora borealis?', ['The northern lights', 'The southern cross', 'The midnight sun', 'The polar vortex'], 0),
    ('What gives the aurora borealis its glowing colours?', ['Charged particles interacting with different gases in the atmosphere', 'Reflections from the ocean surface', 'Light bouncing off mountain snow', 'Fireworks launched from the ground'], 0),
    ('Why do scientists study the aurora borealis?', ['To better understand solar activity and its effects on Earths atmosphere', 'The aurora borealis has no scientific value', 'It never changes and cannot be studied', 'It has no connection to the sun'], 0)]),
SS('Social Studies: Residential Schools and the Path to Reconciliation',
   'Grade 4 Social Studies strand: residential schools were institutions that separated Indigenous children from their families and cultures for over a century, and Canada is now working toward reconciliation by acknowledging this history and rebuilding trust with Indigenous peoples.',
   [('What were residential schools designed to do?', ['Separate Indigenous children from their families and cultures', 'Teach all students about Indigenous traditions', 'Provide extra holidays for students', 'Build new roads across Canada'], 0),
    ('Roughly how long did the residential school system operate in Canada?', ['Over a century', 'Only a single year', 'Less than a month', 'It never actually operated'], 0),
    ('What does reconciliation mean in this context?', ['Acknowledging past harms and working to rebuild trust with Indigenous peoples', 'Ignoring history completely', 'Preventing any further learning about the past', 'Erasing all records of what happened'], 0),
    ('Why is learning about residential schools considered important today?', ['It helps Canadians understand history and support reconciliation efforts', 'This history has no relevance today', 'It is not connected to reconciliation at all', 'It should never be discussed'], 0),
    ('What is one way Canada has worked toward reconciliation?', ['Formal acknowledgements, apologies, and commemorative actions', 'Refusing to discuss the topic at all', 'Removing the history from all records', 'Ignoring requests from Indigenous communities'], 0)]),
]),
day(175, [
L('Writing: Writing a Limerick',
  'Grade 4 Language strand: a limerick is a humorous five-line poem with a distinct AABBA rhyme scheme, where the first, second, and fifth lines rhyme with each other and the third and fourth lines rhyme with each other.',
  [('How many lines does a limerick typically have?', ['Five', 'Three', 'Seven', 'Ten'], 0),
   ('What rhyme scheme does a limerick usually follow?', ['AABBA', 'ABAB', 'AAAA', 'ABCD'], 0),
   ('Which lines of a limerick rhyme with each other in the AABBA pattern?', ['Lines one, two, and five', 'Lines one and three', 'Lines two and four', 'All five lines rhyme differently'], 0),
   ('What tone do limericks usually have?', ['Humorous or playful', 'Extremely serious', 'Formal and businesslike', 'Purely scientific'], 0),
   ('Why might a writer enjoy writing a limerick?', ['It offers a fun, playful way to experiment with rhyme and rhythm', 'Limericks have no rhyme or structure at all', 'Limericks are always exactly one line long', 'It removes any creative choices from writing'], 0)]),
M('Number Sense: Converting Between Fractions and Decimals',
  'Grade 4 Math strand: a fraction can be converted to a decimal by dividing the numerator by the denominator, and a decimal can be converted to a fraction using its place value, such as tenths or hundredths.',
  [('How can you convert a fraction to a decimal?', ['Divide the numerator by the denominator', 'Multiply the numerator by the denominator', 'Add the numerator and denominator', 'Subtract the denominator from the numerator'], 0),
   ('What is the decimal form of 1/4?', ['0.25', '0.4', '0.14', '4.0'], 0),
   ('What is the decimal form of 3/10?', ['0.3', '0.03', '3.10', '0.31'], 0),
   ('What is the fraction form of 0.75?', ['75/100', '7/5', '0.75/1', '75/10'], 0),
   ('Why is it useful to be able to convert between fractions and decimals?', ['It allows numbers to be compared and used more flexibly in different situations', 'Fractions and decimals can never represent the same value', 'Converting between them is never useful in math', 'It only works with whole numbers'], 0)]),
Sc('Science: Wetlands and Marshes as Ecosystems',
   'Grade 4 Science strand: wetlands, including marshes, are ecosystems where land is regularly covered or saturated with water, supporting unique plants and animals while also filtering pollutants and reducing flooding.',
   [('What defines a wetland?', ['Land that is regularly covered or saturated with water', 'Land that never has any water at all', 'A dry desert region', 'A frozen area with no plant life'], 0),
    ('What is a marsh?', ['A type of wetland ecosystem', 'A type of mountain', 'A type of desert', 'A type of glacier'], 0),
    ('What is one important function wetlands provide for the environment?', ['Filtering pollutants and reducing flooding', 'Increasing air pollution', 'Removing all water from the surrounding land', 'Preventing any plants from growing'], 0),
    ('Why do wetlands support such a wide variety of plants and animals?', ['The combination of water and land creates diverse habitats', 'Wetlands have no water and cannot support life', 'Wetlands are identical to deserts', 'No living things can survive in wetlands'], 0),
    ('Why is protecting wetlands considered important?', ['They provide valuable ecological benefits like flood control and habitat', 'Wetlands provide no benefits to the environment', 'Wetlands have no connection to flooding', 'Protecting wetlands has no effect on wildlife'], 0)]),
SS('Social Studies: Canadas Peacekeeping Role in the Suez Crisis',
   'Grade 4 Social Studies strand: during the Suez Crisis of 1956, Canadian diplomat Lester B. Pearson proposed the creation of a United Nations peacekeeping force, an idea that helped resolve the conflict and later earned him the Nobel Peace Prize.',
   [('What was the Suez Crisis?', ['A 1956 international conflict involving Egypt and other nations', 'A natural disaster in northern Canada', 'A Canadian provincial election', 'A trade agreement between Canada and the United States'], 0),
    ('Who proposed the idea of a United Nations peacekeeping force during the Suez Crisis?', ['Lester B. Pearson', 'John A. Macdonald', 'Terry Fox', 'David Thompson'], 0),
    ('What recognition did Lester B. Pearson later receive for his role in the crisis?', ['The Nobel Peace Prize', 'The Stanley Cup', 'The Governor General Award for literature', 'An Olympic gold medal'], 0),
    ('What is the purpose of a United Nations peacekeeping force?', ['To help maintain peace and stability during or after conflicts', 'To start new wars between countries', 'To replace the governments of other countries', 'To prevent all countries from communicating'], 0),
    ('Why is the Suez Crisis significant in Canadian history?', ['It highlighted Canadas role in developing international peacekeeping', 'It has no connection to Canadian history', 'Canada played no part in resolving the crisis', 'It only involved countries outside of the United Nations'], 0)]),
]),
day(176, [
L('Vocabulary: Denotation and Connotation in Poetry',
  'Grade 4 Language strand: denotation is the literal dictionary meaning of a word, while connotation is the feeling or association a word carries, and poets often choose words carefully for their connotations.',
  [('What is denotation?', ['The literal dictionary meaning of a word', 'The feeling a word suggests', 'A type of punctuation mark', 'The sound a word makes when spoken'], 0),
   ('What is connotation?', ['The feeling or association a word carries beyond its literal meaning', 'The exact number of letters in a word', 'The literal dictionary definition of a word', 'A rule about capitalization'], 0),
   ('Why might a poet choose the word slender instead of skinny?', ['Slender often carries a more positive connotation than skinny', 'The two words have completely different denotations', 'Skinny is always considered a formal word', 'Connotation has no effect on word choice'], 0),
   ('Which of these words has a generally negative connotation, even though it can share a denotation with a neutral word?', ['Stubborn', 'Firm', 'Steady', 'Determined'], 0),
   ('Why is understanding connotation important when reading poetry?', ['It helps readers notice the deeper feelings and tone behind word choices', 'Connotation has no effect on how a poem feels', 'All words have identical connotations', 'Poets never consider connotation when choosing words'], 0)]),
M('Measurement: Calculating Perimeter Using Algebraic Expressions',
  'Grade 4 Math strand: the perimeter of a shape with unknown side lengths can be represented using an algebraic expression, where each side is written as a variable or expression and then combined.',
  [('If a square has a side length of s, what algebraic expression represents its perimeter?', ['4s', '2s', 's squared', 's plus 4'], 0),
   ('If a rectangle has length L and width W, what expression represents its perimeter?', ['2L plus 2W', 'L times W', 'L plus W', 'L minus W'], 0),
   ('If a triangle has sides represented by a, b, and c, what expression represents its perimeter?', ['a plus b plus c', 'a times b times c', 'a minus b minus c', 'a divided by b'], 0),
   ('If a square has a side length of x equal to 6, what is its perimeter using the expression 4x?', ['24', '20', '18', '30'], 0),
   ('Why is it useful to write perimeter as an algebraic expression?', ['It allows the perimeter to be calculated for any value of the unknown side length', 'Algebraic expressions can never represent a real measurement', 'It removes the need to know the shape of the figure', 'It only works for shapes with exactly one side'], 0)]),
Sc('Science: How Vaccines Help the Body Fight Disease',
   'Grade 4 Science strand: a vaccine trains the bodys immune system to recognize and fight a specific germ by introducing a safe, weakened, or inactive version of it, helping prevent future illness.',
   [('What does a vaccine help the body do?', ['Recognize and fight a specific germ', 'Grow taller more quickly', 'Digest food more efficiently', 'See in the dark'], 0),
    ('What might a vaccine contain to train the immune system?', ['A safe, weakened, or inactive version of a germ', 'A large amount of sugar', 'A type of metal', 'Pure water only'], 0),
    ('What part of the body responds to a vaccine?', ['The immune system', 'The digestive system', 'The skeletal system', 'The respiratory system alone'], 0),
    ('Why might a person who is vaccinated be less likely to get seriously ill from a disease?', ['Their immune system already learned how to recognize and fight the germ', 'Vaccines have no effect on the immune system', 'Vaccines remove the immune system entirely', 'Vaccinated people can no longer get sick from anything'], 0),
    ('Why are vaccines considered an important tool in public health?', ['They help prevent the spread of serious diseases in communities', 'Vaccines have no effect on disease prevention', 'Vaccines only affect a single person and no one else', 'Vaccines have never been used to prevent illness'], 0)]),
SS('Social Studies: The Rideau Canal — A Historic Waterway',
   'Grade 4 Social Studies strand: the Rideau Canal, connecting Ottawa to Kingston, was built in the early 1800s for military and transportation purposes and is now a UNESCO World Heritage Site known for boating in summer and skating in winter.',
   [('Which two cities does the Rideau Canal connect?', ['Ottawa and Kingston', 'Toronto and Montreal', 'Vancouver and Calgary', 'Halifax and Quebec City'], 0),
    ('Why was the Rideau Canal originally built?', ['For military and transportation purposes', 'As a place for growing crops', 'As a location for a shopping mall', 'As a site for an airport'], 0),
    ('In approximately what era was the Rideau Canal built?', ['The early 1800s', 'The late 1900s', 'Ancient times', 'The far future'], 0),
    ('What international recognition has the Rideau Canal received?', ['It is a UNESCO World Heritage Site', 'It has never received any recognition', 'It was declared a natural wonder of the world', 'It was renamed a national park'], 0),
    ('What activities is the Rideau Canal known for today?', ['Boating in summer and skating in winter', 'Only air travel year-round', 'Only agriculture and farming', 'Only underground mining'], 0)]),
]),
day(177, [
L('Writing: Writing a Persuasive Speech',
  'Grade 4 Language strand: a persuasive speech presents a clear opinion supported by reasons and evidence, uses persuasive language, and is organized to convince an audience through spoken delivery.',
  [('What is the main purpose of a persuasive speech?', ['To convince an audience to agree with an opinion', 'To simply describe a place in detail', 'To retell a fictional story', 'To list unrelated facts with no argument'], 0),
   ('What should support the opinion in a persuasive speech?', ['Clear reasons and evidence', 'Random unrelated details', 'A list of characters', 'A single unrelated fact'], 0),
   ('Why might a speaker use persuasive language such as strong or urgent words?', ['To make the argument feel more convincing and impactful', 'Persuasive language has no effect on an audience', 'It removes the speakers opinion from the speech', 'It makes the speech confusing on purpose'], 0),
   ('What is one difference between a persuasive speech and a persuasive essay?', ['A speech is delivered aloud to a live audience', 'A speech is never allowed to state an opinion', 'A speech cannot use evidence to support claims', 'A speech and an essay are always identical'], 0),
   ('Why might a strong conclusion be important in a persuasive speech?', ['It leaves the audience with a clear, memorable final impression', 'The conclusion has no effect on the audience', 'Conclusions are never included in speeches', 'A weak conclusion always makes a speech more persuasive'], 0)]),
M('Probability: Probability of Independent Events',
  'Grade 4 Math strand: two events are independent when the outcome of one does not affect the outcome of the other, and the probability of both independent events occurring is found by multiplying their individual probabilities.',
  [('What does it mean for two events to be independent?', ['The outcome of one event does not affect the other', 'The two events always happen at the exact same time', 'One event always causes the other to happen', 'Independent events can never both occur'], 0),
   ('How do you find the probability of two independent events both occurring?', ['Multiply their individual probabilities together', 'Add their individual probabilities together', 'Subtract one probability from the other', 'Divide one probability by the other'], 0),
   ('If the probability of flipping heads is 1/2 and rolling a 6 is 1/6, what is the probability of both happening?', ['1/12', '1/2', '1/6', '7/12'], 0),
   ('Is drawing a card and then flipping a coin an example of independent events?', ['Yes, because the card drawn does not affect the coin flip', 'No, because the two events are always connected', 'No, because a coin flip always affects a card draw', 'Yes, but only if the same object is used twice'], 0),
   ('Why is it useful to understand independent events in probability?', ['It helps accurately calculate the chances of multiple events happening together', 'Independent events can never be calculated', 'It has no real use in probability', 'It only applies to events that always happen'], 0)]),
Sc('Science: The Structure of the Human Eye',
   'Grade 4 Science strand: the human eye contains structures such as the cornea, pupil, lens, and retina that work together to focus light and allow the brain to interpret images.',
   [('What is the cornea of the eye?', ['A clear, curved outer layer that helps focus light entering the eye', 'A muscle that controls breathing', 'A bone that protects the skull', 'A type of blood vessel'], 0),
    ('What is the pupil?', ['The opening that allows light to enter the eye', 'A muscle used for walking', 'A bone in the inner ear', 'A part of the digestive system'], 0),
    ('What does the lens of the eye do?', ['Focuses light onto the retina', 'Pumps blood through the body', 'Produces sound waves', 'Filters air before breathing'], 0),
    ('What is the retina?', ['The layer at the back of the eye that senses light and sends signals to the brain', 'A muscle that moves the arms', 'A bone connected to the spine', 'A gland that produces saliva'], 0),
    ('Why do the different parts of the eye need to work together?', ['Each part plays a role in focusing light and forming a clear image for the brain', 'The parts of the eye have no connection to each other', 'Only one part of the eye is ever used at a time', 'The eye has no role in how we see'], 0)]),
SS('Social Studies: Municipal Bylaws — Local Rules for Communities',
   'Grade 4 Social Studies strand: a municipal bylaw is a local law made by a city or town council that regulates matters such as noise, parking, property standards, and animal control within that community.',
   [('What is a municipal bylaw?', ['A local law made by a city or town council', 'A national law passed by Parliament', 'An international treaty between countries', 'A rule that only applies inside a single school'], 0),
    ('Who creates municipal bylaws?', ['A city or town council', 'The Prime Minister', 'The Supreme Court of Canada', 'A foreign government'], 0),
    ('Which of these might be regulated by a municipal bylaw?', ['Noise levels and parking rules', 'International trade agreements', 'National defence policy', 'Federal income tax rates'], 0),
    ('Why might a community need bylaws about noise or property standards?', ['To help maintain order, safety, and quality of life locally', 'Bylaws have no effect on a community', 'Bylaws only apply to other countries', 'Local rules are never needed in communities'], 0),
    ('Why do bylaws vary from one municipality to another?', ['Each community may have different needs and local priorities', 'All municipalities are required to have identical rules', 'Bylaws are set only by the federal government', 'Municipalities are not allowed to make their own rules'], 0)]),
]),
day(178, [
L('Reading: Understanding Allegory',
  'Grade 4 Language strand: an allegory is a story in which characters, events, or settings represent a deeper meaning or message beyond the literal plot, often related to a moral, political, or spiritual idea.',
  [('What is an allegory?', ['A story where characters or events represent a deeper meaning', 'A story that has no meaning beyond the literal plot', 'A list of unrelated facts', 'A type of punctuation mark'], 0),
   ('What might the characters in an allegory represent?', ['Ideas, values, or real-world concepts beyond themselves', 'Nothing beyond their literal actions', 'Only random unrelated objects', 'Only the authors personal diary entries'], 0),
   ('Why might an author choose to write an allegory instead of stating an idea directly?', ['To explore a deeper message in an engaging, indirect way', 'Allegories cannot convey any meaning at all', 'Allegories always confuse readers on purpose', 'Direct statements are always more effective than allegories'], 0),
   ('What kind of message might an allegory often explore?', ['A moral, political, or spiritual idea', 'Only the weather forecast', 'Only a list of numbers', 'Only a recipe for cooking'], 0),
   ('How can readers identify that a story might be an allegory?', ['By noticing that characters or events seem to symbolize larger ideas', 'By checking the total number of pages', 'By ignoring the plot entirely', 'Allegories cannot be identified in any way'], 0)]),
M('Number Sense: Estimating Square Roots',
  'Grade 4 Math strand: the square root of a number that is not a perfect square can be estimated by identifying the two perfect squares it falls between and judging which one it is closer to.',
  [('What are the two perfect squares that 20 falls between?', ['16 and 25', '9 and 16', '25 and 36', '1 and 9'], 0),
   ('Since 20 falls between 16 and 25, is the square root of 20 closer to 4 or 5?', ['Closer to 5', 'Closer to 4', 'Exactly halfway', 'Closer to 6'], 0),
   ('What are the two perfect squares that 40 falls between?', ['36 and 49', '25 and 36', '49 and 64', '16 and 25'], 0),
   ('What is a reasonable estimate for the square root of 40?', ['About 6.3', 'About 4', 'About 10', 'About 20'], 0),
   ('Why is estimating square roots a useful skill?', ['It helps approximate values for numbers that are not perfect squares', 'Square roots can only be calculated for perfect squares', 'Estimating has no mathematical value', 'Square roots never need to be estimated'], 0)]),
Sc('Science: Fermentation — How Microorganisms Transform Food',
   'Grade 4 Science strand: fermentation is a process in which microorganisms such as yeast or bacteria break down sugars, producing gases or acids that change food, as seen in bread rising or yogurt forming.',
   [('What is fermentation?', ['A process where microorganisms break down sugars in food', 'A process where food is frozen solid', 'A process where food is boiled at high heat', 'A process that removes all microorganisms from food'], 0),
    ('Which microorganism is commonly used to help bread rise?', ['Yeast', 'A type of fish', 'A type of insect', 'A type of bird'], 0),
    ('What does fermentation produce that can cause bread dough to rise?', ['Gases, such as carbon dioxide', 'Pure water only', 'Solid metal', 'Sunlight'], 0),
    ('Which food is commonly made using fermentation?', ['Yogurt', 'Fresh raw carrots', 'Plain uncooked rice', 'Ice cubes'], 0),
    ('Why is fermentation useful in food preparation?', ['It can change food texture, flavour, and help with preservation', 'Fermentation has no effect on food at all', 'Fermentation destroys all nutrients instantly', 'Fermentation only works on liquids, never solids'], 0)]),
SS('Social Studies: The Role of the CRTC — Regulating Broadcasting and Telecommunications',
   'Grade 4 Social Studies strand: the Canadian Radio-television and Telecommunications Commission, or CRTC, is a federal agency that regulates radio, television, and telecommunications services to serve the public interest across Canada.',
   [('What does the CRTC stand for?', ['Canadian Radio-television and Telecommunications Commission', 'Canadian Road Transportation and Trade Council', 'Central Recreation and Tourism Commission', 'Canadian Retail and Trade Corporation'], 0),
    ('What kinds of services does the CRTC regulate?', ['Radio, television, and telecommunications services', 'Farming and agriculture', 'National parks and forests', 'Postal delivery services'], 0),
    ('Is the CRTC a federal or municipal agency?', ['Federal', 'Municipal', 'Provincial only', 'International only'], 0),
    ('Why might the CRTC set rules for Canadian broadcasting content?', ['To help ensure Canadian content and public interest are represented', 'To prevent any radio or television broadcasting from existing', 'To give complete control to foreign broadcasters only', 'Broadcasting has no connection to public interest'], 0),
    ('Why is it useful for a country to regulate broadcasting and telecommunications?', ['It helps ensure fair access, quality standards, and public interest protections', 'Regulation has no benefit to the public', 'Broadcasting never needs any oversight', 'Telecommunications services require no rules at all'], 0)]),
]),
day(179, [
L('Vocabulary: Commonly Confused Words — Its and Its',
  'Grade 4 Language strand: its and its are commonly confused homophones, where its shows possession and its is a short form of it is or it has.',
  [('Which word shows possession, meaning belonging to it?', ['Its', 'Its with an apostrophe', 'Neither word', 'Both words equally'], 0),
   ('Which word is a short form combining it and is?', ['Its with an apostrophe', 'Its without an apostrophe', 'Neither word', 'Both words equally'], 0),
   ('Which sentence correctly uses the possessive form?', ['The dog wagged its tail.', 'The dog wagged it is tail.', 'The dog wagged the tail of it is.', 'The dog wagged its is tail.'], 0),
   ('Which sentence correctly uses the short form for it is?', ['Its raining outside today, meaning it is raining.', 'The cat licked its raining paw.', 'Its is raining outside today.', 'The dog chased raining its tail.'], 0),
   ('Why is it important to use the possessive and short forms correctly in writing?', ['Using the correct form helps the sentence make clear sense to readers', 'The two forms always mean exactly the same thing', 'Spelling never affects meaning in a sentence', 'These forms are never confused by writers'], 0)]),
M('Financial Literacy: Reading and Interpreting a Budget',
  'Grade 4 Math strand: a budget is a plan that organizes expected income and expenses over a period of time, helping individuals or families track money coming in and money going out.',
  [('What is a budget?', ['A plan that organizes expected income and expenses', 'A type of bank building', 'A list of favourite foods', 'A schedule of sports games'], 0),
   ('What does income refer to in a budget?', ['Money coming in, such as from a job or allowance', 'Money spent on groceries', 'Money that has been lost', 'A type of tax only'], 0),
   ('What does an expense refer to in a budget?', ['Money going out, such as for bills or purchases', 'Money saved in a bank account', 'Money earned from a job', 'A type of income only'], 0),
   ('If a family budget shows 500 dollars in income and 350 dollars in expenses, how much money is left over?', ['150 dollars', '850 dollars', '350 dollars', '500 dollars'], 0),
   ('Why is creating a budget a helpful financial habit?', ['It helps track and plan how money is earned and spent', 'Budgets have no effect on managing money', 'Budgets only apply to large businesses', 'Tracking income and expenses has no real purpose'], 0)]),
Sc('Science: Wetlands and Marshes as Ecosystems — Case Study of a Local Marsh',
   'Grade 4 Science strand: examining a specific local marsh in detail builds on the general concept of wetlands, showing how plants such as cattails and animals such as herons rely on the shallow water and rich soil found there.',
   [('What kind of plant commonly grows in a marsh?', ['Cattails', 'Cactus', 'Pine trees', 'Desert shrubs'], 0),
    ('What kind of animal is often seen wading in a marsh looking for fish?', ['A heron', 'A polar bear', 'A camel', 'A kangaroo'], 0),
    ('Why do marshes typically have shallow water rather than deep water?', ['Shallow water allows sunlight to reach plants and supports diverse life', 'Marshes never contain any water at all', 'Deep water always forms in every marsh', 'Shallow water prevents any life from surviving there'], 0),
    ('What role does rich soil play in a marsh ecosystem?', ['It supports the growth of many types of marsh plants', 'It prevents any plants from growing', 'It has no connection to plant growth', 'It only supports growth in deserts'], 0),
    ('Why might scientists study a specific local marsh closely?', ['To understand how local plants and animals interact within that ecosystem', 'Local marshes have no scientific value', 'Marshes cannot support any wildlife', 'Studying one marsh applies to no other location'], 0)]),
SS('Social Studies: Comparing Federal, Provincial, and Municipal Bylaws and Laws',
   'Grade 4 Social Studies strand: laws in Canada exist at the federal, provincial, and municipal levels, with each level of government responsible for different areas, from national laws down to local community bylaws.',
   [('Which level of government creates laws for the entire country?', ['Federal', 'Municipal', 'Only provincial', 'None of these levels'], 0),
    ('Which level of government creates local bylaws, such as parking rules?', ['Municipal', 'Federal', 'Only provincial', 'None of these levels'], 0),
    ('Which level of government is responsible for areas such as healthcare and education in a province?', ['Provincial', 'Only municipal', 'Only federal', 'None of these levels'], 0),
    ('Why does Canada have laws made at three different levels of government?', ['Different levels handle national, regional, and local responsibilities effectively', 'Only one level of government is allowed to make laws', 'All laws in Canada are made by cities only', 'Having multiple levels of government serves no purpose'], 0),
    ('Why is it useful for students to understand how laws are made at different levels?', ['It helps them understand how decisions that affect their daily lives are made', 'Laws have no connection to daily life', 'Only adults are affected by any laws', 'Understanding government levels has no value'], 0)]),
]),
day(180, [
L('Language Review: Adverbs, Mood, and Storytelling Forms',
  'Grade 4 Language strand review: students revisit relative adverbs, the subjunctive mood, writing a folk tale, a plays structure, and writing a limerick.',
  [('Which relative adverb describes a place?', ['Where', 'When', 'Why', 'Who'], 0),
   ('What does the subjunctive mood often express?', ['A wish or a situation that is not currently true', 'A simple fact that is happening right now', 'A direct command', 'A question about a location'], 0),
   ('What is a folk tale?', ['A traditional story passed down through generations', 'A scientific report on nature', 'A formal business letter', 'A list of historical dates'], 0),
   ('What is an act in a play?', ['A major division of the story', 'A single line of dialogue', 'The name of a character', 'A type of stage prop'], 0),
   ('How many lines does a limerick typically have?', ['Five', 'Three', 'Seven', 'Ten'], 0)]),
M('Math Review: Quadrilaterals, Division, and Data',
  'Grade 4 Math strand review: students revisit classifying quadrilaterals by parallel sides, dividing a 4-digit number by a 1-digit divisor, calculating the mean, Venn diagrams for factors, and converting fractions to decimals.',
  [('What defines a parallelogram?', ['It has two pairs of parallel sides', 'It has exactly one pair of parallel sides', 'It has no parallel sides', 'It has five sides'], 0),
   ('What is a common first step when dividing a 4-digit number by a 1-digit divisor?', ['Start by dividing the leftmost digit or digits by the divisor', 'Start by dividing the rightmost digit by the divisor', 'Add the divisor to the 4-digit number', 'Multiply the two numbers together'], 0),
   ('How do you calculate the mean of a data set?', ['Add all the values and divide by the number of values', 'Find the largest value only', 'Find the smallest value only', 'Multiply all the values together'], 0),
   ('What can a Venn diagram show when comparing two numbers?', ['Their shared and unique factors or multiples', 'Only their sum', 'Only their difference', 'Only their product'], 0),
   ('How can you convert a fraction to a decimal?', ['Divide the numerator by the denominator', 'Multiply the numerator by the denominator', 'Add the numerator and denominator', 'Subtract the denominator from the numerator'], 0)]),
Sc('Science Review: Water, Ecosystems, and the Human Body',
   'Grade 4 Science strand review: students revisit the water table, predator-prey cycles, ruminant digestion, the northern lights, and how vaccines work.',
   [('What is the water table?', ['The upper level of groundwater stored underground', 'A table used to measure rainfall', 'A type of river on the surface', 'A machine used to pump ocean water'], 0),
    ('What happens to a predator population when prey becomes more plentiful?', ['The predator population tends to grow', 'The predator population disappears completely', 'The predator population has no reaction at all', 'The predator population instantly doubles overnight'], 0),
    ('What is a ruminant animal?', ['An animal with a specialized four-chambered stomach for digesting plants', 'An animal that only eats meat', 'An animal that never eats at all', 'An animal that lives only underwater'], 0),
    ('What causes the aurora borealis?', ['Charged particles from the sun interacting with Earths atmosphere', 'Reflections of city lights bouncing off clouds', 'A type of volcanic eruption', 'Sunlight passing through raindrops'], 0),
    ('What does a vaccine help the body do?', ['Recognize and fight a specific germ', 'Grow taller more quickly', 'Digest food more efficiently', 'See in the dark'], 0)]),
SS('Social Studies Review: Freedom Seekers, Arctic Geography, and Government Oversight',
   'Grade 4 Social Studies strand review: students revisit Underground Railroad conductors, the Hudson Strait, the Auditor General, residential schools and reconciliation, and the Suez Crisis.',
   [('What was the role of a conductor on the Underground Railroad?', ['Guiding freedom seekers along secret routes toward freedom', 'Building railway tracks across Canada', 'Collecting taxes from travellers', 'Repairing roads between towns'], 0),
    ('What does the Hudson Strait connect?', ['Hudson Bay to the Atlantic Ocean', 'The Pacific Ocean to the Great Lakes', 'Lake Ontario to Lake Erie', 'The Rocky Mountains to the prairies'], 0),
    ('What does the Auditor General of Canada examine?', ['How the federal government spends public money', 'The weather across Canada', 'The design of new highways', 'The scores of national sports teams'], 0),
    ('What were residential schools designed to do?', ['Separate Indigenous children from their families and cultures', 'Teach all students about Indigenous traditions', 'Provide extra holidays for students', 'Build new roads across Canada'], 0),
    ('Who proposed the idea of a United Nations peacekeeping force during the Suez Crisis?', ['Lester B. Pearson', 'John A. Macdonald', 'Terry Fox', 'David Thompson'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_171_180)
    append_to(4, g4_171_180)
