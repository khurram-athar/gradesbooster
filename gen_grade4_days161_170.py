#!/usr/bin/env python3
"""Grade 4, Days 161-170 -- extends Grade 4 from 160 to 170 days. Modeled
exactly on gen_grade4_days151_160.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-160
topics (verified against data/grade4.json, which already densely covers
nearly the entire grade 4 curriculum, including the immediately prior
Days 151-160 batch). New topics: interrogative pronouns, reflexive
pronouns, possessive pronouns, understanding motifs in literature,
identifying an unreliable narrator, writing an acrostic poem, writing a
fairy tale, writing a product review, and commonly confused words (their,
there, and theyre) for Language; points lines line segments and rays,
multiplying a 3-digit number by a 2-digit number, constructing and
interpreting line plots, using tree diagrams to list possible outcomes,
calculating simple profit and loss, divisibility rules for 4 and 8,
classifying triangles by angle type, multiplying decimals by 10 100 and
1,000, and ordering integers on a number line for Math; an introduction
to cells, elements compounds and mixtures, spiders and other arachnids,
the layers of a rainforest, tsunamis, hurricanes and tropical storms, how
batteries store and release energy, bioluminescence, and types of
volcanoes for Science; and the Mongol Empire, the Bay of Fundy, David
Thompson and the mapping of western Canada, the Bluenose, Point Pelee
National Park and bird migration, Canadas automotive industry, credit
unions and cooperative banking, the role of the ombudsman, and
traditional Indigenous housing (igloos, longhouses, and tipis) for Social
Studies -- none of those exact ideas appear in Days 1-160. Day 170 is a
review day across all four subjects, matching the end-of-batch pattern
used in every prior 10-day batch (one representative question drawn from
each of the first five lessons of the batch, per subject, exactly as Day
160 did for Days 151-155). The four Day 170 review titles (Language
Review: Pronouns, Motifs, and Narrators / Math Review: Geometry,
Multiplication, and Data / Science Review: Cells, Ecosystems, and Natural
Forces / Social Studies Review: World Empires, Canadian Landmarks, and
Explorers) were checked against every earlier review-day title in Days
1-160, including Day 140, Day 150, Day 160, and every "Review: ...
(Days X-Y)" day, and are textually distinct from all of them. No embedded
ASCII double-quote or apostrophe characters are used anywhere in title/
summary/question/option text, matching the convention used in
gen_grade4_days151_160.py (apostrophes dropped entirely, e.g. "Canadas"
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


def _rebalance_answer_positions(days, seed=20260824):
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


g4_161_170 = [
day(161, [
L('Grammar: Interrogative Pronouns — Who, Whom, Whose, Which, and What',
  'Grade 4 Language strand: interrogative pronouns, including who, whom, whose, which, and what, are used to ask questions and stand in for the noun being asked about.',
  [('Which interrogative pronoun asks about a person acting as the subject?', ['Who', 'Whom', 'Whose', 'Which'], 0),
   ('Which interrogative pronoun asks about a person as the object of a verb or preposition?', ['Whom', 'Who', 'Which', 'What'], 0),
   ('Which interrogative pronoun asks about ownership?', ['Whose', 'Who', 'What', 'Which'], 0),
   ('Which interrogative pronoun asks someone to choose among specific options?', ['Which', 'What', 'Who', 'Whose'], 0),
   ('Why do writers use interrogative pronouns?', ['To ask questions and identify unknown information', 'To state a fact with certainty', 'To give a command', 'To join two independent sentences'], 0)]),
M('Geometry: Points, Lines, Line Segments, and Rays',
  'Grade 4 Math strand: a point marks an exact location in space, a line extends infinitely in both directions, a line segment has two fixed endpoints, and a ray starts at one point and extends infinitely in a single direction.',
  [('What is a point in geometry?', ['An exact location in space with no size', 'A line that never ends', 'A shape with four sides', 'A measurement of an angle'], 0),
   ('How far does a line extend?', ['Infinitely in both directions', 'Only between two endpoints', 'Only in one direction', 'It does not extend at all'], 0),
   ('What makes a line segment different from a line?', ['A line segment has two fixed endpoints', 'A line segment extends forever', 'A line segment has no length', 'A line segment is always curved'], 0),
   ('What is a ray?', ['A part of a line that starts at one point and extends infinitely in one direction', 'A shape with three sides', 'A line with two endpoints', 'A single point with no direction'], 0),
   ('Why do mathematicians distinguish between lines, line segments, and rays?', ['Each has a different length and direction that affects how it is used', 'They are all exactly identical', 'Distinguishing between them has no mathematical use', 'Only rays are ever used in geometry'], 0)]),
Sc('Science: Introduction to Cells — The Basic Building Blocks of Living Things',
   'Grade 4 Science strand: all living things are made up of cells, the basic units of life, and cells can be so small that a microscope is needed to see them clearly.',
   [('What are cells?', ['The basic building blocks of living things', 'A type of rock', 'A type of weather pattern', 'A form of energy'], 0),
    ('What tool is often needed to see individual cells?', ['A microscope', 'A telescope', 'A thermometer', 'A compass'], 0),
    ('Do all living things have cells?', ['Yes, all living things are made of one or more cells', 'No, only animals have cells', 'No, only plants have cells', 'Only humans have cells'], 0),
    ('What might a single-celled organism have compared to a human?', ['Just one cell instead of trillions of cells', 'No cells at all', 'The exact same number of cells as a human', 'No connection to being a living thing'], 0),
    ('Why do scientists study cells?', ['To understand how living things grow, function, and stay alive', 'Cells have no connection to how living things work', 'Studying cells has no scientific value', 'Cells are not related to life at all'], 0)]),
SS('Social Studies: The Mongol Empire — Conquest and Trade Across Asia',
   'Grade 4 Social Studies strand: the Mongol Empire, led by Genghis Khan, became one of the largest empires in history, connecting distant regions of Asia and Europe through conquest and extensive trade routes.',
   [('Who founded the Mongol Empire?', ['Genghis Khan', 'Julius Caesar', 'Alexander the Great', 'Hammurabi'], 0),
    ('What made the Mongol Empire notable in size?', ['It became one of the largest empires in history', 'It never expanded beyond one small village', 'It had no connection to trade', 'It only existed for a single day'], 0),
    ('How did the Mongol Empire affect trade between distant regions?', ['It helped connect trade routes across Asia and Europe', 'It completely blocked all trade', 'It had no effect on trade at all', 'It only allowed trade within one city'], 0),
    ('What skill were Mongol warriors especially known for?', ['Skilled horseback riding and archery', 'Building pyramids', 'Deep sea navigation', 'Farming rice paddies'], 0),
    ('Why do historians still study the Mongol Empire today?', ['It reshaped trade, culture, and borders across a huge part of the world', 'It has no historical importance', 'It never interacted with other civilizations', 'It only affected a small unimportant area'], 0)]),
]),
day(162, [
L('Grammar: Reflexive Pronouns',
  'Grade 4 Language strand: reflexive pronouns, such as myself, yourself, himself, herself, itself, ourselves, yourselves, and themselves, are used when the subject and object of a sentence refer to the same person or thing.',
  [('What is a reflexive pronoun?', ['A pronoun used when the subject and object of a sentence are the same', 'A pronoun that only names an object', 'A word that joins two sentences', 'A type of punctuation mark'], 0),
   ('Which reflexive pronoun matches the subject I?', ['Myself', 'Yourself', 'Himself', 'Themselves'], 0),
   ('Which sentence correctly uses a reflexive pronoun?', ['She hurt herself while running.', 'She hurt she while running.', 'She hurt hers while running.', 'She hurt their while running.'], 0),
   ('Which reflexive pronoun matches the subject they?', ['Themselves', 'Himself', 'Itself', 'Myself'], 0),
   ('Why are reflexive pronouns useful in writing?', ['They show the subject and object of a sentence are the same person or thing', 'They always change the subject of a sentence', 'They remove the need for a verb', 'They are never used in complete sentences'], 0)]),
M('Number Sense: Multiplying a 3-Digit Number by a 2-Digit Number',
  'Grade 4 Math strand: multiplying a 3-digit number by a 2-digit number involves breaking the 2-digit number into tens and ones, multiplying each part separately, and adding the partial products together.',
  [('What is a common first step to multiply a 3-digit number by a 2-digit number?', ['Break the 2-digit number into tens and ones', 'Add the two numbers together', 'Divide the numbers first', 'Round both numbers to zero'], 0),
   ('What is 213 multiplied by 12?', ['2,556', '2,486', '2,600', '2,356'], 0),
   ('What is 145 multiplied by 21?', ['3,045', '2,945', '3,145', '3,245'], 0),
   ('After multiplying by the tens digit and the ones digit separately, what should you do next?', ['Add the two partial products together', 'Subtract the smaller product from the larger one', 'Divide both products by 10', 'Multiply the two partial products together'], 0),
   ('Why is breaking numbers into tens and ones helpful when multiplying larger numbers?', ['It makes the multiplication easier to manage in smaller steps', 'It always produces an incorrect answer', 'It removes the need for any calculation', 'It only works with 1-digit numbers'], 0)]),
Sc('Science: Elements, Compounds, and Mixtures — Classifying Matter',
   'Grade 4 Science strand: matter can be classified as an element, a pure substance made of only one type of atom, a compound, made of two or more elements chemically joined, or a mixture, made of substances that are combined but not chemically joined.',
   [('What is an element?', ['A pure substance made of only one type of atom', 'A mixture of many substances', 'A liquid that cannot be separated', 'A type of rock only'], 0),
    ('What is a compound?', ['Two or more elements chemically joined together', 'A single element with no other substances', 'A type of light wave', 'A form of energy'], 0),
    ('What is a mixture?', ['A combination of substances that are not chemically joined', 'A substance made of only one type of atom', 'A compound with exactly two elements', 'A type of rock'], 0),
    ('Which of these is an example of a mixture?', ['A salad with many separate ingredients', 'Pure oxygen gas', 'A single gold atom', 'Pure carbon'], 0),
    ('Why is it useful to classify matter as elements, compounds, or mixtures?', ['It helps scientists understand what a substance is made of and how it behaves', 'Classifying matter has no scientific value', 'All matter is exactly identical', 'Matter cannot be classified in any way'], 0)]),
SS('Social Studies: The Bay of Fundy — Home to the Worlds Highest Tides',
   'Grade 4 Social Studies strand: the Bay of Fundy, located between Nova Scotia and New Brunswick, is famous for having the highest tides in the world, caused by the unique shape of the bay funnelling huge volumes of water.',
   [('In which two provinces is the Bay of Fundy located?', ['Nova Scotia and New Brunswick', 'Ontario and Quebec', 'British Columbia and Alberta', 'Manitoba and Saskatchewan'], 0),
    ('What is the Bay of Fundy famous for?', ['Having the highest tides in the world', 'Having no tides at all', 'Being the largest lake in Canada', 'Being located in the Arctic'], 0),
    ('What causes the Bay of Fundy to have such extreme tides?', ['The unique shape of the bay funnels large volumes of water', 'The bay has no connection to the ocean', 'The tides are caused by wind alone', 'The bay never experiences changing water levels'], 0),
    ('How much can water levels change during a tide cycle in the Bay of Fundy?', ['By many metres between high and low tide', 'By less than one centimetre', 'Water levels never change there', 'Only during the winter season'], 0),
    ('Why might scientists and tourists be interested in the Bay of Fundy?', ['Its dramatic tides make it a unique natural and scientific attraction', 'It has no scientific or tourism value', 'It is identical to every other bay in Canada', 'It is located far from any coastline'], 0)]),
]),
day(163, [
L('Grammar: Possessive Pronouns',
  'Grade 4 Language strand: possessive pronouns, such as mine, yours, his, hers, its, ours, and theirs, show ownership and replace a noun instead of coming before one.',
  [('What do possessive pronouns show?', ['Ownership of something', 'A question being asked', 'An action taking place', 'A location in a sentence'], 0),
   ('Which is an example of a possessive pronoun?', ['Theirs', 'They', 'Them', 'These'], 0),
   ('Which sentence correctly uses a possessive pronoun?', ['That book is mine.', 'That book is my.', 'That book is I.', 'That book is me.'], 0),
   ('How is a possessive pronoun different from a possessive noun like Sarahs?', ['A possessive pronoun replaces the noun entirely instead of attaching to it', 'A possessive pronoun is always spelled with an apostrophe', 'A possessive pronoun never shows ownership', 'A possessive pronoun is only used in questions'], 0),
   ('Why are possessive pronouns useful in writing?', ['They show ownership without repeating the noun', 'They remove all meaning from a sentence', 'They can only be used with plural nouns', 'They replace verbs in a sentence'], 0)]),
M('Data Management: Constructing and Interpreting Line Plots',
  'Grade 4 Math strand: a line plot displays data along a number line using symbols such as Xs or dots to show how many times each value occurs, making it easy to see the shape and spread of a data set.',
  [('What does a line plot use to show how many times a value occurs?', ['Symbols such as Xs or dots stacked above a number line', 'Bars of different colours', 'Slices of a circle', 'Multiple separate graphs'], 0),
   ('What does a line plot help you quickly see about a data set?', ['The shape and spread of the data', 'The exact title of the survey', 'Nothing useful about the data', 'Only the largest value in the set'], 0),
   ('If three Xs are stacked above the number 5 on a line plot, what does that mean?', ['The value 5 occurred three times in the data', 'The value 5 occurred only once', 'The number 3 occurred five times', 'The data set has no values at all'], 0),
   ('What is one advantage of a line plot for a small data set?', ['It shows every individual data point clearly', 'It hides all individual data points', 'It only works with very large data sets', 'It cannot show repeated values'], 0),
   ('Why might a class use a line plot to record data like favourite pet or shoe size?', ['It gives a simple visual way to compare how often each value appears', 'Line plots cannot be used for that kind of data', 'It removes the need to collect any data', 'It only works with negative numbers'], 0)]),
Sc('Science: Spiders and Other Arachnids — Unique Adaptations',
   'Grade 4 Science strand: spiders and other arachnids, such as scorpions and ticks, have eight legs and two main body parts, and many spiders have special adaptations like silk-spinning glands used to build webs for catching prey.',
   [('How many legs do spiders and other arachnids typically have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
    ('How many main body parts does a typical spider have?', ['Two', 'Three', 'One', 'Four'], 0),
    ('What is one adaptation many spiders use to catch prey?', ['Spinning silk webs', 'Growing wings', 'Producing bright flowers', 'Breathing underwater only'], 0),
    ('Which of these is an example of an arachnid other than a spider?', ['A scorpion', 'A butterfly', 'A bee', 'A ladybug'], 0),
    ('How are arachnids different from insects?', ['Arachnids have eight legs while insects have six', 'Arachnids have wings while insects never do', 'Arachnids have no legs at all', 'Insects always have more body parts than arachnids'], 0)]),
SS('Social Studies: David Thompson — Mapping Western Canada',
   'Grade 4 Social Studies strand: David Thompson was an explorer and surveyor who mapped vast areas of western Canada in the early 1800s, creating detailed maps that helped guide later settlement and trade.',
   [('What was David Thompson known for?', ['Mapping vast areas of western Canada', 'Building the CN Tower', 'Founding the city of Toronto', 'Leading a naval fleet'], 0),
    ('What job did David Thompson do to create his maps?', ['He worked as an explorer and surveyor', 'He worked only as a farmer', 'He worked only as a baker', 'He never travelled anywhere'], 0),
    ('When did David Thompson complete much of his mapping work?', ['In the early 1800s', 'In the twenty-first century', 'In ancient times', 'During the Ice Age'], 0),
    ('How did David Thompsons maps help later Canadians?', ['They guided later settlement and trade routes', 'They had no use to anyone', 'They were immediately lost and never used', 'They only showed oceans with no land'], 0),
    ('Why is David Thompson remembered as an important figure in Canadian history?', ['His detailed maps greatly expanded knowledge of western Canadas geography', 'He has no connection to Canadian history', 'He never explored any part of Canada', 'His work was never recorded'], 0)]),
]),
day(164, [
L('Reading: Understanding Motifs in Literature',
  'Grade 4 Language strand: a motif is a recurring image, symbol, or idea that appears throughout a text and helps reinforce its theme or deeper meaning.',
  [('What is a motif in literature?', ['A recurring image, symbol, or idea throughout a text', 'A single event that happens only once', 'The title of a book', 'A type of punctuation mark'], 0),
   ('What does a motif help reinforce in a story?', ['The theme or deeper meaning of the text', 'The page numbers of the book', 'The authors name', 'The font used in printing'], 0),
   ('If the colour red appears repeatedly around moments of danger in a story, what might this be an example of?', ['A motif connected to danger or warning', 'A random unrelated detail', 'A type of punctuation', 'A grammar rule'], 0),
   ('How is a motif different from a symbol used only once?', ['A motif repeats throughout the text while a single symbol may appear only once', 'A motif and a single symbol are exactly the same thing', 'A motif never repeats', 'A motif has no connection to meaning'], 0),
   ('Why might authors use motifs in their writing?', ['To subtly reinforce important ideas throughout a story', 'To confuse readers with no purpose', 'Motifs are never used in literature', 'To remove meaning from a text'], 0)]),
M('Probability: Using Tree Diagrams to List Possible Outcomes',
  'Grade 4 Math strand: a tree diagram is a branching diagram used to list all possible outcomes of an event or combination of events, making it easier to count outcomes and calculate probability.',
  [('What is a tree diagram used for?', ['Listing all possible outcomes of an event', 'Measuring the length of an object', 'Showing the temperature over time', 'Comparing prices at a store'], 0),
   ('If you flip a coin and then roll a die, how would a tree diagram help?', ['It would show every possible combination of coin and die results', 'It would only show the coin results', 'It would only show the die results', 'It would show no useful information'], 0),
   ('How many outcomes are shown by a tree diagram for flipping two coins?', ['Four', 'Two', 'Six', 'Eight'], 0),
   ('What does each branch of a tree diagram usually represent?', ['One possible choice or outcome at that stage', 'An unrelated topic', 'A fixed number that never changes', 'A type of punctuation mark'], 0),
   ('Why are tree diagrams useful in probability?', ['They help organize and count all possible outcomes clearly', 'They make outcomes impossible to count', 'They only work with one outcome at a time', 'They have no connection to probability'], 0)]),
Sc('Science: The Layers of a Rainforest — Canopy, Understory, and Forest Floor',
   'Grade 4 Science strand: a tropical rainforest has distinct layers, including the emergent layer of tallest trees, the canopy that forms a dense leafy roof, the understory of smaller plants, and the forest floor, each supporting different plants and animals.',
   [('What is the canopy of a rainforest?', ['A dense leafy layer formed by the crowns of tall trees', 'The layer of soil beneath the forest', 'The tallest single tree in the forest', 'A type of river found only in rainforests'], 0),
    ('What is found at the very top of a rainforest, above the canopy?', ['The emergent layer of the tallest trees', 'The forest floor', 'The understory', 'The root layer'], 0),
    ('What is the understory of a rainforest?', ['A layer of smaller plants growing beneath the canopy', 'The tallest layer of trees', 'A layer made entirely of rock', 'A layer found only underwater'], 0),
    ('Why does very little sunlight reach the forest floor of a rainforest?', ['The dense canopy blocks most sunlight from passing through', 'The forest floor is located underground', 'Rainforests receive no sunlight at all', 'The canopy has no effect on sunlight'], 0),
    ('Why do rainforest layers support different types of plants and animals?', ['Each layer offers different amounts of light, temperature, and space', 'All layers are exactly identical', 'Only the forest floor supports any life', 'Rainforest layers have no effect on living things'], 0)]),
SS('Social Studies: The Bluenose — A Famous Canadian Sailing Ship',
   'Grade 4 Social Studies strand: the Bluenose was a famous Canadian racing schooner built in Nova Scotia in the 1920s, celebrated for its speed and skill, and its image now appears on the Canadian dime.',
   [('What type of ship was the Bluenose?', ['A racing schooner', 'A submarine', 'A cruise ship', 'A cargo tanker'], 0),
    ('In which province was the Bluenose built?', ['Nova Scotia', 'Alberta', 'Manitoba', 'British Columbia'], 0),
    ('What was the Bluenose especially celebrated for?', ['Its speed and sailing skill', 'Being the largest ship ever built', 'Being used only for fishing trips', 'Never winning any races'], 0),
    ('Where does the image of the Bluenose appear today?', ['On the Canadian dime', 'On the Canadian flag', 'On the back of the twenty dollar bill', 'On provincial licence plates'], 0),
    ('Why is the Bluenose considered an important Canadian symbol?', ['It represents Canadian maritime skill and pride from the early twentieth century', 'It has no connection to Canadian history', 'It was built in a different country', 'It never achieved any recognition'], 0)]),
]),
day(165, [
L('Reading: Identifying an Unreliable Narrator',
  'Grade 4 Language strand: an unreliable narrator is a storyteller whose account of events may be inaccurate, biased, or incomplete, requiring readers to question and look beyond what is being told.',
  [('What is an unreliable narrator?', ['A storyteller whose account may be inaccurate or biased', 'A narrator who always tells the complete truth', 'A character who never speaks in the story', 'The author of the book'], 0),
   ('Why might readers need to question an unreliable narrators account?', ['Because the narrators version of events may be incomplete or biased', 'Because unreliable narrators are always completely accurate', 'Because the narrator never appears in the story', 'Because unreliable narrators cannot tell a story'], 0),
   ('What might cause a narrator to be unreliable?', ['Limited knowledge, strong bias, or a reason to hide the truth', 'Being the main character of the story', 'Speaking in the first person', 'Describing the setting'], 0),
   ('How can readers detect that a narrator might be unreliable?', ['By noticing contradictions or gaps between the narrators claims and other details', 'By trusting every statement completely', 'By ignoring the narrator entirely', 'Unreliable narrators cannot be detected'], 0),
   ('Why might an author choose to use an unreliable narrator?', ['To create suspense or challenge readers to think critically about the story', 'To make the story impossible to understand', 'Unreliable narrators are never used in literature', 'To remove all meaning from a story'], 0)]),
M('Financial Literacy: Calculating Simple Profit and Loss',
  'Grade 4 Math strand: profit occurs when the money earned from selling something is greater than the cost to make or buy it, while a loss occurs when the cost is greater than the money earned.',
  [('What is profit?', ['The amount earned that is greater than the cost', 'The amount lost after a sale', 'The total cost of making an item', 'The price customers pay before tax'], 0),
   ('What is a loss?', ['When the cost of an item is greater than the money earned from selling it', 'When profit is very high', 'When an item is sold for exactly its cost', 'When no money is spent at all'], 0),
   ('If a lemonade stand spends 5 dollars on supplies and earns 12 dollars in sales, what is the profit?', ['7 dollars', '5 dollars', '12 dollars', '17 dollars'], 0),
   ('If a stand spends 10 dollars on supplies and only earns 6 dollars in sales, what happened?', ['The stand had a loss of 4 dollars', 'The stand had a profit of 4 dollars', 'The stand broke even exactly', 'The stand earned exactly 10 dollars'], 0),
   ('Why is it useful for a business to track profit and loss?', ['It helps determine whether the business is making or losing money', 'Tracking profit and loss has no real purpose', 'All businesses always make the same amount of profit', 'Loss has no effect on a business'], 0)]),
Sc('Science: Tsunamis — Powerful Waves Triggered Beneath the Ocean',
   'Grade 4 Science strand: a tsunami is a series of powerful ocean waves usually triggered by an underwater earthquake, volcanic eruption, or landslide, capable of causing major flooding when it reaches the shore.',
   [('What most commonly triggers a tsunami?', ['An underwater earthquake', 'A sunny day', 'A change in air temperature', 'A full moon'], 0),
    ('What is a tsunami?', ['A series of powerful ocean waves', 'A type of underground cave', 'A gentle ripple in a pond', 'A type of cloud formation'], 0),
    ('Besides earthquakes, what else can trigger a tsunami?', ['An underwater volcanic eruption or landslide', 'A sunny afternoon', 'A light breeze', 'A change in the tide alone'], 0),
    ('What can happen when a tsunami reaches the shore?', ['It can cause major flooding and damage', 'It always disappears before reaching land', 'It has no effect on coastal areas', 'It only affects deep ocean water'], 0),
    ('Why do scientists monitor the ocean floor for tsunami warning signs?', ['To warn coastal communities early and help keep people safe', 'Monitoring the ocean floor has no benefit', 'Tsunamis cannot be detected in any way', 'Warning systems have no effect on safety'], 0)]),
SS('Social Studies: Point Pelee National Park and Bird Migration',
   'Grade 4 Social Studies strand: Point Pelee National Park, located at the southern tip of mainland Canada, is an important resting point for millions of migrating birds each spring and fall due to its location along a major migration route.',
   [('Where is Point Pelee National Park located?', ['At the southern tip of mainland Canada', 'In the Canadian Arctic', 'On the west coast of British Columbia', 'In northern Quebec'], 0),
    ('Why is Point Pelee important for birds?', ['It serves as a resting point along a major migration route', 'Birds never travel through this area', 'It has no connection to bird migration', 'It is located far from any migration paths'], 0),
    ('During which seasons do large numbers of birds pass through Point Pelee?', ['Spring and fall', 'Only in winter', 'Only in summer', 'Birds never pass through in any season'], 0),
    ('Why might birds need resting points like Point Pelee during migration?', ['Long migrations require stops to rest and find food', 'Birds never need to rest during migration', 'Resting points make migration impossible', 'Migration routes never include stops'], 0),
    ('Why do many visitors travel to Point Pelee each year?', ['To observe the large variety of migrating birds', 'It has no attractions for visitors', 'It is closed to the public', 'It has no connection to nature'], 0)]),
]),
day(166, [
L('Writing: Writing an Acrostic Poem',
  'Grade 4 Language strand: an acrostic poem uses the letters of a word, spelled vertically down the page, as the starting letter for each line, often describing or relating to that word.',
  [('What is an acrostic poem?', ['A poem where each line starts with a letter from a word spelled vertically', 'A poem with no structure at all', 'A poem that must rhyme every line', 'A poem written only about animals'], 0),
   ('How are the letters of the key word arranged in an acrostic poem?', ['Vertically down the page', 'Scattered randomly', 'Written backwards only', 'Hidden inside other words'], 0),
   ('What might each line of an acrostic poem describe?', ['Something related to the meaning of the key word', 'A completely unrelated topic', 'Only numbers', 'Only punctuation marks'], 0),
   ('If the key word is DOG, how many lines would a basic acrostic poem about DOG likely have?', ['Three', 'One', 'Five', 'Ten'], 0),
   ('Why might a writer choose to write an acrostic poem?', ['It offers a fun, structured way to explore a word or topic creatively', 'Acrostic poems have no creative value', 'It removes the need for any words', 'It only works for very long words'], 0)]),
M('Number Sense: Divisibility Rules for 4 and 8',
  'Grade 4 Math strand: a number is divisible by 4 if its last two digits form a number divisible by 4, and a number is divisible by 8 if its last three digits form a number divisible by 8.',
  [('How can you tell if a number is divisible by 4?', ['Check if the last two digits form a number divisible by 4', 'Check if the number is even', 'Check if the digits add up to 4', 'Check only the first digit'], 0),
   ('Is the number 316 divisible by 4?', ['Yes, because 16 is divisible by 4', 'No, because 16 is not divisible by 4', 'Yes, because 3 is divisible by 4', 'No, 316 cannot be tested'], 0),
   ('How can you tell if a number is divisible by 8?', ['Check if the last three digits form a number divisible by 8', 'Check if the number is odd', 'Check if the first digit is 8', 'Check if the digits add up to 8'], 0),
   ('Is the number 1,240 divisible by 8?', ['Yes, because 240 is divisible by 8', 'No, because 240 is not divisible by 8', 'Yes, because 1 is divisible by 8', 'No, only even numbers can be divisible by 8'], 0),
   ('Why are divisibility rules useful in math?', ['They help quickly check if a number can be divided evenly without doing long division', 'They make division impossible', 'They only work for the number 10', 'They have no practical use'], 0)]),
Sc('Science: Hurricanes and Tropical Storms',
   'Grade 4 Science strand: a hurricane is a powerful rotating storm that forms over warm ocean water, bringing strong winds, heavy rain, and dangerous storm surges when it reaches land.',
   [('Where do hurricanes typically form?', ['Over warm ocean water', 'Over frozen tundra', 'Over mountain peaks', 'Underground'], 0),
    ('What is a key feature of a hurricane?', ['Strong rotating winds', 'No wind at all', 'Freezing temperatures', 'A complete lack of rain'], 0),
    ('What can a hurricane bring when it reaches land?', ['Strong winds, heavy rain, and storm surges', 'Only light breezes', 'Only clear skies', 'Only cold temperatures'], 0),
    ('What is a storm surge?', ['A rise in sea level pushed toward the coast by a storm', 'A type of desert wind', 'A calm ocean current', 'A gentle wave with no danger'], 0),
    ('Why do meteorologists closely track hurricanes?', ['To warn coastal communities and help people prepare for safety', 'Tracking hurricanes has no benefit', 'Hurricanes cannot be tracked in any way', 'Hurricanes never affect people on land'], 0)]),
SS('Social Studies: Canadas Automotive Industry',
   'Grade 4 Social Studies strand: Canadas automotive industry, centred largely in Ontario, manufactures vehicles and parts, providing many jobs and playing a significant role in the countrys economy and trade with other nations.',
   [('Which province is most closely associated with Canadas automotive industry?', ['Ontario', 'British Columbia', 'Nova Scotia', 'Manitoba'], 0),
    ('What does Canadas automotive industry primarily manufacture?', ['Vehicles and vehicle parts', 'Only farming equipment', 'Only clothing', 'Only furniture'], 0),
    ('What does the automotive industry provide for many Canadians?', ['Jobs', 'Free vehicles for everyone', 'Unlimited fuel', 'Free land'], 0),
    ('How does the automotive industry connect to Canadas trade with other countries?', ['Vehicles and parts are often exported and imported between countries', 'Canada never trades vehicles with other countries', 'The industry has no connection to trade', 'All vehicles are only used within one factory'], 0),
    ('Why is the automotive industry considered important to Canadas economy?', ['It creates jobs and generates significant economic activity', 'It has no impact on the economy', 'It only affects a single small town', 'It provides no products or services'], 0)]),
]),
day(167, [
L('Writing: Writing a Fairy Tale',
  'Grade 4 Language strand: a fairy tale is a traditional story that often includes magical elements, a clear conflict between good and evil, and a lesson or happy ending, such as tales featuring castles, enchanted creatures, or brave heroes.',
  [('What is a common feature of a fairy tale?', ['Magical elements and a conflict between good and evil', 'Only factual scientific information', 'A list of unrelated statistics', 'A formal business letter'], 0),
   ('What kind of ending do many fairy tales have?', ['A happy ending or resolved lesson', 'An ending with no resolution at all', 'An ending that is never written', 'A completely random ending with no connection to the story'], 0),
   ('Which of these might commonly appear as a setting in a fairy tale?', ['An enchanted forest or castle', 'A modern office building', 'A shopping mall', 'A subway station'], 0),
   ('What role might a fairy tale hero often play in the story?', ['Overcoming a challenge or defeating an evil force', 'Causing all the problems in the story', 'Never appearing in the story', 'Ending the story without any actions'], 0),
   ('Why do many fairy tales include a clear lesson or moral?', ['To teach readers something meaningful through the story', 'Fairy tales never include lessons', 'Morals have no place in fairy tales', 'Lessons are only found in nonfiction texts'], 0)]),
M('Geometry: Classifying Triangles by Angle Type — Acute, Right, and Obtuse',
  'Grade 4 Math strand: triangles can be classified by their angles as acute, where all angles are less than 90 degrees, right, with one angle equal to exactly 90 degrees, or obtuse, with one angle greater than 90 degrees.',
  [('What defines an acute triangle?', ['All three angles are less than 90 degrees', 'One angle is exactly 90 degrees', 'One angle is greater than 90 degrees', 'All three angles are equal to 180 degrees'], 0),
   ('What defines a right triangle?', ['One angle is exactly 90 degrees', 'All angles are greater than 90 degrees', 'All angles are less than 45 degrees', 'No angles are equal'], 0),
   ('What defines an obtuse triangle?', ['One angle is greater than 90 degrees', 'All angles are less than 90 degrees', 'One angle is exactly 90 degrees', 'All angles are exactly equal'], 0),
   ('Can a triangle have two right angles?', ['No, because the three angles must add up to 180 degrees total', 'Yes, every triangle has two right angles', 'Yes, but only in obtuse triangles', 'No triangle can ever have a right angle'], 0),
   ('Why is it useful to classify triangles by their angles?', ['It helps identify and describe the properties of different triangle shapes', 'Classifying triangles has no mathematical value', 'All triangles have identical angles', 'Angles have no connection to triangle shape'], 0)]),
Sc('Science: How Batteries Store and Release Energy',
   'Grade 4 Science strand: a battery stores chemical energy and converts it into electrical energy through a chemical reaction inside the battery, allowing it to power devices when connected in a circuit.',
   [('What type of energy does a battery store?', ['Chemical energy', 'Light energy', 'Sound energy', 'Wind energy'], 0),
    ('What does a battery convert its stored energy into?', ['Electrical energy', 'Heat energy only', 'Sound energy only', 'Nuclear energy'], 0),
    ('How does a battery release its stored energy?', ['Through a chemical reaction inside the battery', 'By absorbing sunlight', 'By spinning rapidly', 'By freezing'], 0),
    ('What is needed for a battery to power a device?', ['The battery must be connected in a complete circuit', 'The battery must be left disconnected', 'The device must have no wires', 'The battery must be exposed to sunlight'], 0),
    ('Why do batteries eventually stop working and need to be replaced or recharged?', ['Their stored chemical energy runs out over time', 'Batteries never run out of energy', 'Batteries create energy from nothing', 'Batteries only work for one second'], 0)]),
SS('Social Studies: Credit Unions and Cooperative Banking in Canada',
   'Grade 4 Social Studies strand: a credit union is a cooperative financial institution owned by its members, offering banking services such as savings accounts and loans, with profits often returned to members rather than outside shareholders.',
   [('What is a credit union?', ['A cooperative financial institution owned by its members', 'A government tax office', 'A type of grocery store', 'A national park'], 0),
    ('Who owns a credit union?', ['Its members', 'A single wealthy owner', 'A foreign government', 'No one owns a credit union'], 0),
    ('What services might a credit union offer?', ['Savings accounts and loans', 'Only postal services', 'Only grocery delivery', 'Only construction services'], 0),
    ('How are credit union profits often used?', ['They are often returned to members instead of outside shareholders', 'They are always given to a foreign government', 'They disappear completely', 'They are never distributed to anyone'], 0),
    ('Why might someone choose to bank with a credit union?', ['Because it is member-owned and may offer benefits back to its community of members', 'Credit unions offer no benefits at all', 'Credit unions are not allowed to offer banking services', 'Credit unions only serve large businesses'], 0)]),
]),
day(168, [
L('Writing: Writing a Product Review',
  'Grade 4 Language strand: a product review is a piece of writing that describes a product, evaluates its strengths and weaknesses, and offers an opinion to help other readers decide whether to use it.',
  [('What is the purpose of a product review?', ['To evaluate a product and help readers decide whether to use it', 'To tell an imaginary story', 'To describe a historical event', 'To list unrelated facts'], 0),
   ('What might a product review include?', ['The products strengths and weaknesses', 'Only the products price with no opinion', 'A completely unrelated topic', 'A private diary entry'], 0),
   ('Why might a reviewer include specific examples in a product review?', ['To support their opinion with clear evidence', 'Examples have no value in a review', 'Reviews are not allowed to include examples', 'Examples always confuse the reader'], 0),
   ('What tone might a balanced product review use?', ['A fair tone that considers both positives and negatives', 'A tone that only praises the product', 'A tone that only criticizes the product', 'A tone with no opinion expressed at all'], 0),
   ('Why do many readers look for product reviews before making a purchase?', ['Reviews help them understand a products quality before buying it', 'Reviews have no influence on purchases', 'Product reviews are never read by anyone', 'Reviews only describe unrelated products'], 0)]),
M('Number Sense: Multiplying Decimals by 10, 100, and 1,000',
  'Grade 4 Math strand: multiplying a decimal by 10, 100, or 1,000 moves the decimal point to the right by one, two, or three places, making the number larger.',
  [('What happens to a decimal number when it is multiplied by 10?', ['The decimal point moves one place to the right', 'The decimal point moves one place to the left', 'The number becomes smaller', 'The number stays exactly the same'], 0),
   ('What is 3.45 multiplied by 10?', ['34.5', '3.45', '345', '0.345'], 0),
   ('What is 2.6 multiplied by 100?', ['260', '26', '2.6', '0.26'], 0),
   ('What is 0.7 multiplied by 1,000?', ['700', '70', '7', '0.7'], 0),
   ('Why is it useful to understand how multiplying by 10, 100, and 1,000 affects decimals?', ['It helps with mental math and understanding place value shifts', 'It has no effect on any calculation', 'Decimals cannot be multiplied by whole numbers', 'Multiplying decimals always produces a smaller number'], 0)]),
Sc('Science: Bioluminescence — Living Things That Glow',
   'Grade 4 Science strand: bioluminescence is the ability of certain living things, such as fireflies, jellyfish, and deep-sea fish, to produce their own light through a chemical reaction inside their bodies.',
   [('What is bioluminescence?', ['The ability of living things to produce their own light', 'The ability of living things to fly', 'The ability of living things to breathe underwater', 'The ability of living things to change colour'], 0),
    ('Which of these is a well-known example of a bioluminescent animal?', ['A firefly', 'A robin', 'A squirrel', 'A deer'], 0),
    ('How do bioluminescent organisms produce light?', ['Through a chemical reaction inside their bodies', 'By absorbing sunlight during the day', 'By reflecting moonlight only', 'By using electricity from wires'], 0),
    ('Where might many bioluminescent creatures be found besides on land?', ['In the deep ocean', 'In the desert', 'On mountain peaks', 'In outer space'], 0),
    ('Why might bioluminescence be useful to an animal?', ['It can help attract mates, lure prey, or ward off predators', 'It has no useful purpose for animals', 'It always harms the animal that produces it', 'It prevents animals from being seen at all'], 0)]),
SS('Social Studies: The Role of the Ombudsman in Protecting Citizens Rights',
   'Grade 4 Social Studies strand: an ombudsman is an independent official who investigates complaints from citizens about unfair treatment by government services, helping ensure fairness and accountability.',
   [('What does an ombudsman do?', ['Investigates complaints from citizens about unfair treatment', 'Builds highways across the country', 'Manages a countrys military', 'Runs a private business'], 0),
    ('Why is an ombudsman considered independent?', ['They investigate fairly without taking sides between citizens and government', 'They always side with the government', 'They are controlled entirely by a single business', 'They have no connection to government services'], 0),
    ('Who might contact an ombudsman for help?', ['A citizen who feels they were treated unfairly by a government service', 'Only foreign governments', 'Only large corporations', 'No one is allowed to contact an ombudsman'], 0),
    ('What is one goal of having an ombudsman in government?', ['Ensuring fairness and accountability in public services', 'Removing all rules from government', 'Preventing citizens from ever complaining', 'Making government services less accountable'], 0),
    ('Why is the role of an ombudsman valuable to a community?', ['It gives citizens a way to seek fair treatment and hold services accountable', 'It has no value to citizens', 'It removes all citizen rights', 'It only benefits government workers'], 0)]),
]),
day(169, [
L('Vocabulary: Commonly Confused Words — Their, There, and Theyre',
  'Grade 4 Language strand: their, there, and theyre are commonly confused homophones, where their shows possession, there refers to a location, and theyre is a short form of they are.',
  [('Which word shows possession, meaning something belongs to a group?', ['Their', 'There', 'Theyre', 'None of these'], 0),
   ('Which word refers to a location or place?', ['There', 'Their', 'Theyre', 'None of these'], 0),
   ('Which word is a short form combining they and are?', ['Theyre', 'Their', 'There', 'None of these'], 0),
   ('Which sentence uses their correctly?', ['The students brought their books to class.', 'The students brought there books to class.', 'The students brought theyre books to class.', 'The students brought books their to class.'], 0),
   ('Why is it important to use their, there, and theyre correctly in writing?', ['Using the correct word helps the sentence make clear sense to readers', 'These words all mean exactly the same thing', 'Spelling never affects meaning', 'These words are never confused by writers'], 0)]),
M('Number Sense: Ordering Integers on a Number Line',
  'Grade 4 Math strand: integers can be ordered from least to greatest by plotting them on a number line, remembering that numbers further to the left are smaller and numbers further to the right are larger, even with negative numbers.',
  [('On a number line, which direction do numbers increase in value?', ['To the right', 'To the left', 'Upward only', 'Downward only'], 0),
   ('Which integer is greater, -2 or 3?', ['3', '-2', 'They are equal', 'Cannot be determined'], 0),
   ('Which integer is smaller, -7 or -1?', ['-7', '-1', 'They are equal', 'Cannot be determined'], 0),
   ('How would you order -4, 2, and -1 from least to greatest?', ['-4, -1, 2', '2, -1, -4', '-1, -4, 2', '2, -4, -1'], 0),
   ('Why is it useful to plot integers on a number line before ordering them?', ['It gives a clear visual way to compare their positions and values', 'It makes ordering integers impossible', 'Number lines cannot include negative numbers', 'It has no effect on comparing values'], 0)]),
Sc('Science: Types of Volcanoes — Shield, Cinder Cone, and Composite',
   'Grade 4 Science strand: volcanoes can be classified by shape and eruption style, including shield volcanoes with gently sloping sides, cinder cone volcanoes with steep sides built from erupted debris, and composite volcanoes formed from alternating layers of lava and ash.',
   [('What is a shield volcano known for?', ['Having gently sloping sides formed by runny lava', 'Having extremely steep sides', 'Never erupting at all', 'Being made entirely of ice'], 0),
    ('What is a cinder cone volcano built from?', ['Erupted debris that piles up into steep sides', 'Only flowing water', 'Only sand from a desert', 'Only solid rock with no eruptions'], 0),
    ('What forms a composite volcano?', ['Alternating layers of lava and ash', 'A single layer of ice', 'A single layer of sand', 'A layer of only water'], 0),
    ('Which type of volcano tends to have the steepest, most cone-shaped profile?', ['Composite or cinder cone volcanoes', 'Shield volcanoes only', 'Volcanoes have no shape', 'All volcanoes look identical'], 0),
    ('Why do scientists classify volcanoes into different types?', ['It helps predict eruption style and potential hazards', 'Classifying volcanoes has no scientific use', 'All volcanoes behave in exactly the same way', 'Volcanoes cannot be studied or classified'], 0)]),
SS('Social Studies: Igloos, Longhouses, and Tipis — Traditional Indigenous Housing Across Canada',
   'Grade 4 Social Studies strand: Indigenous peoples across Canada developed different types of traditional housing suited to their environment and way of life, including igloos built from snow in the Arctic, longhouses built by Iroquoian peoples, and tipis used by Plains peoples.',
   [('What material were traditional igloos built from?', ['Blocks of snow and ice', 'Wood logs', 'Woven grass', 'Stone bricks'], 0),
    ('Which group of Indigenous peoples traditionally built longhouses?', ['Iroquoian peoples', 'Only peoples living in the Arctic', 'Only peoples living on the Pacific coast', 'No Indigenous peoples used longhouses'], 0),
    ('What were tipis traditionally used for?', ['Portable housing used by Plains peoples', 'Permanent housing used only in cities', 'Storage buildings for grain', 'Structures used only for fishing'], 0),
    ('Why did traditional Indigenous housing styles vary across Canada?', ['Different environments and ways of life called for different housing designs', 'All Indigenous housing was built exactly the same way', 'Housing style had no connection to environment', 'Indigenous peoples never built any housing'], 0),
    ('Why is it valuable to learn about traditional Indigenous housing?', ['It shows how Indigenous peoples adapted skillfully to their environments', 'It has no educational value', 'Traditional housing has no connection to Indigenous cultures', 'These housing styles were never actually used'], 0)]),
]),
day(170, [
L('Language Review: Pronouns, Motifs, and Narrators',
  'Grade 4 Language strand review: students revisit interrogative pronouns, reflexive pronouns, possessive pronouns, motifs in literature, and unreliable narrators.',
  [('Which interrogative pronoun asks about a person acting as the subject?', ['Who', 'Whom', 'Whose', 'Which'], 0),
   ('What is a reflexive pronoun?', ['A pronoun used when the subject and object of a sentence are the same', 'A pronoun that only names an object', 'A word that joins two sentences', 'A type of punctuation mark'], 0),
   ('What do possessive pronouns show?', ['Ownership of something', 'A question being asked', 'An action taking place', 'A location in a sentence'], 0),
   ('What is a motif in literature?', ['A recurring image, symbol, or idea throughout a text', 'A single event that happens only once', 'The title of a book', 'A type of punctuation mark'], 0),
   ('What is an unreliable narrator?', ['A storyteller whose account may be inaccurate or biased', 'A narrator who always tells the complete truth', 'A character who never speaks in the story', 'The author of the book'], 0)]),
M('Math Review: Geometry, Multiplication, and Data',
  'Grade 4 Math strand review: students revisit points lines and rays, multiplying a 3-digit number by a 2-digit number, line plots, tree diagrams, and profit and loss.',
  [('What is a point in geometry?', ['An exact location in space with no size', 'A line that never ends', 'A shape with four sides', 'A measurement of an angle'], 0),
   ('What is a common first step to multiply a 3-digit number by a 2-digit number?', ['Break the 2-digit number into tens and ones', 'Add the two numbers together', 'Divide the numbers first', 'Round both numbers to zero'], 0),
   ('What does a line plot use to show how many times a value occurs?', ['Symbols such as Xs or dots stacked above a number line', 'Bars of different colours', 'Slices of a circle', 'Multiple separate graphs'], 0),
   ('What is a tree diagram used for?', ['Listing all possible outcomes of an event', 'Measuring the length of an object', 'Showing the temperature over time', 'Comparing prices at a store'], 0),
   ('What is profit?', ['The amount earned that is greater than the cost', 'The amount lost after a sale', 'The total cost of making an item', 'The price customers pay before tax'], 0)]),
Sc('Science Review: Cells, Ecosystems, and Natural Forces',
   'Grade 4 Science strand review: students revisit cells, elements compounds and mixtures, spiders and arachnids, rainforest layers, and tsunamis.',
   [('What are cells?', ['The basic building blocks of living things', 'A type of rock', 'A type of weather pattern', 'A form of energy'], 0),
    ('What is an element?', ['A pure substance made of only one type of atom', 'A mixture of many substances', 'A liquid that cannot be separated', 'A type of rock only'], 0),
    ('How many legs do spiders and other arachnids typically have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
    ('What is the canopy of a rainforest?', ['A dense leafy layer formed by the crowns of tall trees', 'The layer of soil beneath the forest', 'The tallest single tree in the forest', 'A type of river found only in rainforests'], 0),
    ('What most commonly triggers a tsunami?', ['An underwater earthquake', 'A sunny day', 'A change in air temperature', 'A full moon'], 0)]),
SS('Social Studies Review: World Empires, Canadian Landmarks, and Explorers',
   'Grade 4 Social Studies strand review: students revisit the Mongol Empire, the Bay of Fundy, David Thompson, the Bluenose, and Point Pelee National Park.',
   [('Who founded the Mongol Empire?', ['Genghis Khan', 'Julius Caesar', 'Alexander the Great', 'Hammurabi'], 0),
    ('In which two provinces is the Bay of Fundy located?', ['Nova Scotia and New Brunswick', 'Ontario and Quebec', 'British Columbia and Alberta', 'Manitoba and Saskatchewan'], 0),
    ('What was David Thompson known for?', ['Mapping vast areas of western Canada', 'Building the CN Tower', 'Founding the city of Toronto', 'Leading a naval fleet'], 0),
    ('What type of ship was the Bluenose?', ['A racing schooner', 'A submarine', 'A cruise ship', 'A cargo tanker'], 0),
    ('Where is Point Pelee National Park located?', ['At the southern tip of mainland Canada', 'In the Canadian Arctic', 'On the west coast of British Columbia', 'In northern Quebec'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_161_170)
    append_to(4, g4_161_170)
