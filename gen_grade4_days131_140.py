#!/usr/bin/env python3
"""Grade 4, Days 131-140 -- extends Grade 4 from 130 to 140 days. Modeled
exactly on gen_grade4_days121_130.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-130
topics (see data/grade4.json), which already densely cover nearly the
entire grade 4 curriculum. New topics: semicolons and colons, types of
conflict in stories, writing a play script, understanding allusion,
summarizing versus paraphrasing, subject and predicate, regional
dialects, writing a letter to the editor, and analyzing illustrations in
non-fiction texts for Language; subtracting fractions with unlike
denominators, an introduction to exponents, surface area of rectangular
prisms, range as a measure of spread, Roman numerals, estimating sums and
differences, multiplying a fraction by a fraction, area of triangles
using a formula, and constructing a histogram for Math; heat transfer
(conduction/convection/radiation), seed dispersal, symbiosis, acids and
bases, cave formations, an introduction to Newtons laws of motion, food
groups and healthy eating, comparing the planets, and teeth/dental health
for Science; and the Byzantine Empire, the Rocky Mountains, the Canadian
Pacific Railway, Canadas fishing industry, the National Day for Truth and
Reconciliation, the Klondike Gold Rush, provincial legislatures, Canadian
sports and national games, and the role of the Lieutenant Governor for
Social Studies -- none of those exact ideas appear in Days 1-130. Day 140
is a review day across all four subjects, matching the end-of-batch
pattern used in every prior 10-day batch (one representative question
drawn from each of the first five lessons of the batch, per subject,
exactly as Day 130 did for Days 121-125). No embedded ASCII double-quote
or apostrophe characters are used anywhere in title/summary/question/
option text, matching the convention used in gen_grade4_days121_130.py
(apostrophes dropped entirely, e.g. "Canadas" not "Canada's").
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


g4_131_140 = [
day(131, [
L('Grammar: Semicolons and Colons',
  'Grade 4 Language strand: a semicolon can join two closely related independent clauses without a conjunction, while a colon introduces a list, explanation, or quotation.',
  [('What can a semicolon join without using a conjunction?', ['Two closely related independent clauses', 'A single word and a comma', 'Two unrelated topics', 'A title and a subtitle'], 0),
   ('Which sentence correctly uses a semicolon?', ['I like soccer; I also like basketball.', 'I like soccer; and basketball.', 'I like soccer, I also; like basketball.', 'I like; soccer and basketball.'], 0),
   ('What does a colon often introduce?', ['A list of items', 'A single silent letter', 'A question mark', 'A new paragraph title'], 0),
   ('Which sentence correctly uses a colon?', ['Bring these items: a map, a compass, and water.', 'Bring these items, a map: a compass, and water.', 'Bring: these items a map, a compass, and water.', 'Bring these items a map, a compass: and water.'], 0),
   ('Why might a writer choose a semicolon instead of starting a new sentence?', ['To show the two ideas are closely connected', 'To make the sentence shorter', 'Semicolons have no real purpose', 'To replace all commas'], 0)]),
M('Fractions: Subtracting Fractions with Unlike Denominators',
  'Grade 4 Math strand: to subtract fractions with unlike denominators, students find a common denominator, rewrite each fraction as an equivalent fraction, then subtract the numerators.',
  [('What must fractions have before they can be subtracted directly?', ['A common denominator', 'The same numerator', 'A common numerator', 'Different denominators'], 0),
   ('What is 1/2 - 1/4?', ['1/4', '1/2', '0', '3/4'], 0),
   ('What is 2/3 - 1/6?', ['1/2', '1/3', '1/6', '5/6'], 0),
   ('What is the first step in subtracting fractions with unlike denominators?', ['Find a common denominator', 'Subtract the denominators', 'Multiply the numerators', 'Add the fractions'], 0),
   ('Why cant we subtract fraction numerators directly when denominators differ?', ['Because the pieces are different sizes until denominators match', 'Subtraction is impossible with fractions', 'Numerators are always equal', 'Denominators do not matter'], 0)]),
Sc('Science: Heat Transfer — Conduction, Convection, and Radiation',
   'Grade 4 Science strand: heat moves from warmer objects to cooler ones through conduction (touching objects), convection (moving liquids or gases), and radiation (waves travelling through space).',
   [('What is conduction?', ['Heat transfer through direct contact between objects', 'Heat transfer through empty space', 'Heat transfer only in liquids', 'Heat that never moves'], 0),
    ('What is convection?', ['Heat transfer through the movement of liquids or gases', 'Heat transfer through solid metal only', 'Heat transfer through sound waves', 'Heat that disappears instantly'], 0),
    ('What is radiation in terms of heat transfer?', ['Heat transfer through waves that can travel through empty space', 'Heat transfer only through touching', 'Heat transfer only underwater', 'Heat that cannot reach the Earth'], 0),
    ('Which is an example of conduction?', ['A metal spoon heating up in hot soup', 'Sunlight warming your skin', 'Warm air rising in a room', 'Steam escaping a kettle'], 0),
    ('Why does the Sun warm the Earth even though there is empty space between them?', ['Heat travels from the Sun by radiation', 'Heat needs direct contact to travel', 'Heat can only travel through water', 'Heat cannot cross empty space at all'], 0)]),
SS('Social Studies: The Byzantine Empire — An Ancient Civilization',
   'Grade 4 Social Studies strand: the Byzantine Empire was the eastern continuation of the Roman Empire, centered on the city of Constantinople, known for its trade, architecture, and preservation of learning.',
   [('What was the Byzantine Empire a continuation of?', ['The eastern Roman Empire', 'A brand new empire with no history', 'The ancient Egyptian empire', 'The Greek city-states'], 0),
    ('What was the capital city of the Byzantine Empire?', ['Constantinople', 'Rome', 'Athens', 'Cairo'], 0),
    ('What was the Byzantine Empire known for preserving?', ['Ancient learning, art, and knowledge', 'Nothing of value', 'Only farming tools', 'Only weapons'], 0),
    ('What helped the Byzantine Empire grow wealthy?', ['Trade along important routes', 'Avoiding all contact with other regions', 'Having no cities', 'Ignoring all trade opportunities'], 0),
    ('Why is the Byzantine Empire important to study?', ['It shows how earlier civilizations influenced later ones', 'It had no lasting influence', 'It never existed', 'It only affected modern Italy'], 0)]),
]),
day(132, [
L('Reading: Types of Conflict in Stories',
  'Grade 4 Language strand: stories often contain a central conflict, such as character versus character, character versus self, character versus nature, or character versus society.',
  [('What is a literary conflict?', ['A problem or struggle a character faces', 'The setting of a story', 'The title of a book', 'A type of punctuation'], 0),
   ('What type of conflict is character versus character?', ['A struggle between two characters', 'A character struggling with their own feelings', 'A character struggling against weather', 'A character struggling against laws'], 0),
   ('What type of conflict is character versus nature?', ['A struggle between a character and natural forces', 'A struggle between two friends', 'A struggle between a character and society', 'A struggle with no cause'], 0),
   ('What type of conflict is character versus self?', ['A character struggling with their own thoughts or feelings', 'A struggle against a storm', 'A struggle against another character', 'A struggle against a government'], 0),
   ('Why is conflict important in a story?', ['It drives the plot forward and creates interest', 'Stories cannot have conflict', 'Conflict has no effect on plot', 'It only appears in nonfiction'], 0)]),
M('Number Sense: Introduction to Exponents',
  'Grade 4 Math strand: an exponent shows how many times a number, called the base, is multiplied by itself, such as 2 to the third power (2 cubed) meaning 2 x 2 x 2 = 8.',
  [('What does an exponent tell you?', ['How many times a number is multiplied by itself', 'How many times to add a number', 'How many digits a number has', 'How to divide a number'], 0),
   ('What is 2 to the third power (2 x 2 x 2)?', ['8', '6', '4', '9'], 0),
   ('What is 10 to the second power (10 x 10)?', ['100', '20', '10', '1000'], 0),
   ('In the expression 3 to the fourth power, what is the base?', ['3', '4', '12', '7'], 0),
   ('What is 4 to the second power (4 x 4)?', ['16', '8', '12', '20'], 0)]),
Sc('Science: Seed Dispersal — How Plants Spread Their Seeds',
   'Grade 4 Science strand: plants spread their seeds away from the parent plant through methods such as wind, water, animals, and seed pods that burst open, helping new plants grow in different locations.',
   [('Why do plants need to disperse their seeds?', ['So new plants have room and resources to grow away from the parent plant', 'So seeds never grow into plants', 'So plants can stay in one exact spot forever', 'Seeds do not need to move'], 0),
    ('Which method of seed dispersal uses moving air?', ['Wind dispersal', 'Water dispersal', 'Animal dispersal', 'Explosive dispersal'], 0),
    ('How do some seeds travel by animal?', ['They stick to fur or are eaten and carried elsewhere', 'Animals never carry seeds', 'Seeds repel all animals', 'Animals destroy every seed they touch'], 0),
    ('Which seeds are adapted for water dispersal?', ['Seeds that float, such as coconuts', 'Seeds that are heavier than any liquid', 'Seeds that dissolve in water', 'Seeds that sink immediately and cannot travel'], 0),
    ('What happens when some seed pods dry out?', ['They burst open and fling seeds away from the plant', 'They grow new roots instantly', 'They turn into flowers', 'They disappear completely'], 0)]),
SS('Social Studies: The Rocky Mountains and Canadas Mountain Ranges',
   'Grade 4 Social Studies strand: the Rocky Mountains stretch through western Canada, forming a dramatic mountain range that shapes climate, wildlife habitats, and the tourism industry in provinces such as Alberta and British Columbia.',
   [('In which part of Canada are the Rocky Mountains located?', ['Western Canada', 'Eastern Canada', 'Northern Canada only', 'Southern Ontario'], 0),
    ('Which two provinces are closely associated with the Rocky Mountains?', ['Alberta and British Columbia', 'Ontario and Quebec', 'Manitoba and Saskatchewan', 'Nova Scotia and New Brunswick'], 0),
    ('How do mountains like the Rockies affect climate?', ['They can block moisture and create different climates on each side', 'They have no effect on climate', 'They only exist in deserts', 'They make every region identical'], 0),
    ('What industry benefits from the scenery of the Rocky Mountains?', ['Tourism', 'Only farming', 'Only mining', 'Only fishing'], 0),
    ('What kind of wildlife habitat do the Rocky Mountains provide?', ['Habitat for animals adapted to mountain environments', 'No habitat at all', 'Ocean-only habitat', 'Desert-only habitat'], 0)]),
]),
day(133, [
L('Writing: Writing a Play Script',
  'Grade 4 Language strand: a play script tells a story through dialogue and stage directions, organized into scenes, and is meant to be performed by actors in front of an audience.',
  [('What is a play script mainly made up of?', ['Dialogue and stage directions', 'Only descriptive paragraphs', 'Only a list of characters', 'Only a summary of events'], 0),
   ('What are stage directions used for?', ['Telling actors how to move or what to do', 'Telling the audience the ending in advance', 'Replacing all dialogue', 'Naming the author'], 0),
   ('How is a play script usually organized?', ['Into scenes', 'Into stanzas', 'Into chapters only', 'Into paragraphs with no divisions'], 0),
   ('Who is a play script ultimately written to be performed by?', ['Actors in front of an audience', 'Only silent readers', 'Only the author', 'No one'], 0),
   ('Why is dialogue especially important in a play script?', ['It is the main way the story and characters are revealed', 'Plays never use dialogue', 'Dialogue is only used in poems', 'Dialogue replaces the need for actors'], 0)]),
M('Geometry: Surface Area of Rectangular Prisms',
  'Grade 4 Math strand: the surface area of a rectangular prism is the total area of all six of its faces, found by calculating the area of each face and adding them together.',
  [('What is surface area?', ['The total area of all the faces of a 3D shape', 'The space inside a shape', 'The distance around a shape', 'The height of a shape only'], 0),
   ('How many faces does a rectangular prism have?', ['Six', 'Four', 'Eight', 'Three'], 0),
   ('To find the surface area of a rectangular prism, you should ___.', ['Find the area of each face and add them together', 'Multiply only the length and width once', 'Add only two of the faces', 'Ignore the top and bottom faces'], 0),
   ('Why might builders need to know the surface area of a box?', ['To know how much material is needed to cover its outside', 'Surface area has no real use', 'To find out how heavy the box is', 'To find how loud the box is'], 0),
   ('If a cube has six identical square faces each with an area of 4 square units, what is its total surface area?', ['24 square units', '16 square units', '20 square units', '4 square units'], 0)]),
Sc('Science: Symbiosis — Mutualism, Commensalism, and Parasitism',
   'Grade 4 Science strand: symbiosis describes close relationships between different species, including mutualism where both benefit, commensalism where one benefits without harming the other, and parasitism where one benefits while harming the other.',
   [('What is symbiosis?', ['A close relationship between two different species', 'A type of rock formation', 'A single organism living alone', 'A weather pattern'], 0),
    ('In mutualism, how do the two species involved benefit?', ['Both species benefit from the relationship', 'Only one species benefits while harming the other', 'Neither species benefits', 'Both species are harmed'], 0),
    ('In parasitism, what happens to the host organism?', ['It is harmed while the parasite benefits', 'It always benefits equally', 'It benefits while the parasite is harmed', 'Nothing happens to either organism'], 0),
    ('What best describes commensalism?', ['One species benefits while the other is unaffected', 'Both species are harmed', 'Both species benefit equally', 'One species always dies'], 0),
    ('Which is an example of mutualism?', ['Bees pollinating flowers while gaining nectar', 'A tick feeding on a dog', 'A bird building a nest with no effect on trees', 'Two animals that never interact'], 0)]),
SS('Social Studies: The Canadian Pacific Railway — Connecting the Country',
   'Grade 4 Social Studies strand: the Canadian Pacific Railway, completed in 1885, linked the country from coast to coast, encouraging settlement and trade, and helping fulfill a promise made to British Columbia when it joined Confederation.',
   [('What did the Canadian Pacific Railway connect?', ['Communities from coast to coast across Canada', 'Only two neighbouring cities', 'Canada to another country by land', 'Nothing of importance'], 0),
    ('In what year was the Canadian Pacific Railway completed?', ['1885', '1867', '1900', '1812'], 0),
    ('Why was building the railway important for British Columbia joining Confederation?', ['Canada promised a railway to connect BC to the rest of the country', 'BC had no interest in railways', 'The railway was built before BC existed', 'BC refused any transportation link'], 0),
    ('What did the railway help encourage across Canada?', ['Settlement and trade', 'The end of all trade', 'Fewer communities', 'Isolation between regions'], 0),
    ('What kind of workers helped build the railway, including through dangerous mountain sections?', ['Labourers, including many Chinese workers', 'No workers were needed', 'Only government officials', 'Only farmers'], 0)]),
]),
day(134, [
L('Vocabulary: Understanding Allusion',
  'Grade 4 Language strand: an allusion is a brief reference to a well-known person, place, event, or story that a writer expects the reader to recognize and understand.',
  [('What is an allusion?', ['A brief reference to something well known, such as a story or event', 'A type of punctuation mark', 'A word with no meaning', 'A long detailed description'], 0),
   ('Why do writers use allusions?', ['To quickly connect an idea to something readers already know', 'To confuse readers on purpose', 'Allusions are never used by writers', 'To avoid using any description'], 0),
   ('If a story describes someone as strong as Hercules, what is this an allusion to?', ['A figure from Greek mythology', 'A modern celebrity', 'A scientific law', 'A grammar rule'], 0),
   ('What must a reader do to understand an allusion?', ['Recognize the reference being made', 'Ignore the sentence completely', 'Only read the title', 'Allusions do not need to be understood'], 0),
   ('Which of these could be the subject of an allusion?', ['A famous story or historical event', 'A random made-up word', 'A blank page', 'A single punctuation mark'], 0)]),
M('Data Management: Range as a Measure of Spread',
  'Grade 4 Math strand: the range of a data set is found by subtracting the smallest value from the largest value, showing how spread out the data is.',
  [('What is the range of a data set?', ['The difference between the largest and smallest values', 'The average of all values', 'The most common value', 'The middle value'], 0),
   ('What is the range of this data set: 4, 7, 9, 12, 15?', ['11', '15', '4', '9'], 0),
   ('How do you calculate the range?', ['Subtract the smallest value from the largest value', 'Add all the values together', 'Multiply the largest and smallest values', 'Count the number of values'], 0),
   ('What does a large range suggest about a data set?', ['The data values are spread far apart', 'All the data values are identical', 'The data set has no smallest value', 'The data set has no largest value'], 0),
   ('What does a small range suggest about a data set?', ['The data values are close together', 'The data values are spread very far apart', 'There is no data at all', 'The data cannot be measured'], 0)]),
Sc('Science: Acids and Bases — Everyday Chemistry',
   'Grade 4 Science strand: acids and bases are two types of substances with different properties, such as taste and reaction with litmus paper, found in many everyday items such as lemon juice and baking soda.',
   [('What is a common property of acids?', ['They often taste sour', 'They always taste sweet', 'They cannot be found in food', 'They never react with anything'], 0),
    ('What colour does litmus paper turn in the presence of an acid?', ['Red', 'Blue', 'Green', 'Black'], 0),
    ('What colour does litmus paper turn in the presence of a base?', ['Blue', 'Red', 'Yellow', 'Purple'], 0),
    ('Which of these is an example of an acid found in food?', ['Lemon juice', 'Baking soda', 'Soap', 'Chalk'], 0),
    ('Which of these is an example of a common base?', ['Baking soda', 'Lemon juice', 'Orange juice', 'Vinegar'], 0)]),
SS('Social Studies: Canadas Fishing Industry',
   'Grade 4 Social Studies strand: Canadas fishing industry harvests seafood such as salmon, lobster, and cod from coastal waters on the Atlantic and Pacific coasts, supporting coastal communities and export trade.',
   [('What does the fishing industry harvest from Canadas coastal waters?', ['Seafood such as fish and shellfish', 'Only fresh vegetables', 'Only minerals', 'Only lumber'], 0),
    ('Name one type of seafood commonly harvested in Canada.', ['Lobster', 'Corn', 'Wheat', 'Cotton'], 0),
    ('Which coasts support Canadas major fishing industries?', ['The Atlantic and Pacific coasts', 'Only landlocked lakes', 'Only the Arctic ice cap', 'No coasts at all'], 0),
    ('How does the fishing industry support coastal communities?', ['It provides jobs and income for people living there', 'It has no effect on communities', 'It only affects inland cities', 'It replaces all other industries'], 0),
    ('Why is sustainable fishing important?', ['To ensure fish populations remain healthy for the future', 'Sustainability does not matter for fishing', 'Overfishing has no consequences', 'Fish populations can never be affected'], 0)]),
]),
day(135, [
L('Reading: Summarizing versus Paraphrasing',
  'Grade 4 Language strand: summarizing condenses the main ideas of a text into a much shorter form, while paraphrasing restates specific information in different words without necessarily shortening it.',
  [('What does summarizing a text involve?', ['Condensing the main ideas into a much shorter form', 'Copying the text word for word', 'Making the text longer', 'Ignoring the main ideas'], 0),
   ('What does paraphrasing involve?', ['Restating information in your own words', 'Copying the exact original wording', 'Only using the first sentence', 'Removing all information'], 0),
   ('How is summarizing different from paraphrasing?', ['Summarizing shortens the overall content, while paraphrasing restates it without necessarily shortening it', 'They are exactly the same skill', 'Summarizing always makes text longer', 'Paraphrasing always copies the original words exactly'], 0),
   ('Why is it useful to summarize a long text?', ['It helps identify and remember the most important ideas', 'It removes the need to understand the text', 'It always confuses the reader', 'Summaries are never useful'], 0),
   ('When paraphrasing, why should you avoid copying the original wording?', ['To show understanding and avoid copying someone elses exact words', 'Copying the original wording is required', 'Paraphrasing means changing nothing', 'Original wording is always incorrect'], 0)]),
M('Number Sense: Roman Numerals',
  'Grade 4 Math strand: Roman numerals use letters such as I, V, X, L, and C to represent numbers, an ancient number system still seen today on clocks, in book chapters, and in movie credits.',
  [('What does the Roman numeral X represent?', ['10', '5', '1', '50'], 0),
   ('What does the Roman numeral V represent?', ['5', '10', '1', '100'], 0),
   ('How is the number 4 written in Roman numerals?', ['IV', 'IIII', 'VI', 'IX'], 0),
   ('Where might you still see Roman numerals used today?', ['On clocks and in movie credits', 'Only in ancient ruins', 'Nowhere in modern life', 'Only in outer space'], 0),
   ('What does the Roman numeral L represent?', ['50', '100', '500', '5'], 0)]),
Sc('Science: Caves and Cave Formations — Stalactites and Stalagmites',
   'Grade 4 Science strand: caves often form when water slowly dissolves rock such as limestone, and mineral deposits left behind create formations such as stalactites hanging from the ceiling and stalagmites rising from the floor.',
   [('What type of rock is commonly dissolved by water to form caves?', ['Limestone', 'Granite', 'Iron', 'Rubber'], 0),
    ('What is a stalactite?', ['A mineral formation hanging from a cave ceiling', 'A mineral formation rising from the cave floor', 'A type of cave animal', 'A type of underground river'], 0),
    ('What is a stalagmite?', ['A mineral formation rising from the cave floor', 'A mineral formation hanging from the ceiling', 'A type of rock that never forms in caves', 'A kind of cave entrance'], 0),
    ('How do stalactites and stalagmites typically form?', ['Mineral-rich water slowly deposits minerals over a long time', 'They form instantly overnight', 'They are carved by cave explorers', 'They are made of ice only'], 0),
    ('Why can caves take thousands of years to form these features?', ['Because mineral deposits build up very slowly over time', 'Because caves form in a single day', 'Because rock never dissolves', 'Because water has no effect on rock'], 0)]),
SS('Social Studies: National Day for Truth and Reconciliation',
   'Grade 4 Social Studies strand: the National Day for Truth and Reconciliation, observed on September 30, honours residential school survivors and their families, and encourages learning and reflection about the history and experiences of Indigenous peoples in Canada.',
   [('On what date is the National Day for Truth and Reconciliation observed?', ['September 30', 'July 1', 'November 11', 'October 31'], 0),
    ('What does the National Day for Truth and Reconciliation honour?', ['Residential school survivors, their families, and their communities', 'A sports championship', 'A harvest festival', 'A national election'], 0),
    ('What colour of shirt is commonly worn to mark this day?', ['Orange', 'Blue', 'Green', 'Purple'], 0),
    ('Why is learning about this history important for students?', ['It helps build understanding and respect for Indigenous experiences', 'It has no importance to Canadian history', 'It only concerns one small region', 'It is not part of Canadian history'], 0),
    ('What is one way schools mark this day?', ['Learning about Indigenous history and holding reflective activities', 'Ignoring the day completely', 'Cancelling all lessons with no discussion', 'Celebrating with fireworks'], 0)]),
]),
day(136, [
L('Grammar: Sentence Structure — Subject and Predicate',
  'Grade 4 Language strand: every complete sentence has a subject, who or what the sentence is about, and a predicate, which tells what the subject does or is.',
  [('What is the subject of a sentence?', ['Who or what the sentence is about', 'The action word only', 'The last word in the sentence', 'The punctuation mark'], 0),
   ('What is the predicate of a sentence?', ['The part that tells what the subject does or is', 'Only the first word', 'A type of punctuation', 'The title of the sentence'], 0),
   ('In the sentence The dog barked loudly, what is the subject?', ['The dog', 'Barked', 'Loudly', 'Barked loudly'], 0),
   ('In the sentence The dog barked loudly, what is the predicate?', ['Barked loudly', 'The dog', 'Loudly', 'Dog'], 0),
   ('Why does a sentence need both a subject and a predicate?', ['To express a complete thought', 'Only the subject is needed', 'Only the predicate is needed', 'Sentences do not need either'], 0)]),
M('Number Sense: Estimating Sums and Differences',
  'Grade 4 Math strand: estimating sums and differences involves rounding numbers before adding or subtracting to quickly check whether an exact answer is reasonable.',
  [('Why do we estimate sums and differences?', ['To quickly check whether an exact answer is reasonable', 'To always get the exact answer', 'To avoid using numbers', 'Estimating has no purpose'], 0),
   ('What is a quick estimate of 398 + 205 after rounding to the nearest hundred?', ['600', '500', '700', '800'], 0),
   ('What is a quick estimate of 812 - 397 after rounding to the nearest hundred?', ['400', '500', '300', '1200'], 0),
   ('What is the first step in estimating a sum or difference?', ['Round the numbers to a convenient place value', 'Multiply the numbers exactly', 'Add without rounding', 'Ignore the numbers'], 0),
   ('Why is estimating useful when shopping?', ['It helps quickly check if you have enough money', 'It always gives the exact total', 'It has no real-life use', 'It replaces the need for money'], 0)]),
Sc('Science: Newtons Laws of Motion — An Introduction',
   'Grade 4 Science strand: Isaac Newtons three laws of motion describe how objects move, including that objects at rest stay at rest unless a force acts on them, and every action has an equal and opposite reaction.',
   [('According to Newtons first law, what happens to an object at rest?', ['It stays at rest unless a force acts on it', 'It always starts moving on its own', 'It disappears', 'It only moves in circles'], 0),
    ('What does Newtons third law state?', ['For every action there is an equal and opposite reaction', 'Objects never interact with each other', 'Force has no effect on motion', 'Objects always slow down for no reason'], 0),
    ('Who is credited with developing these three laws of motion?', ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Charles Darwin'], 0),
    ('What is needed to change the motion of an object, according to Newtons first law?', ['A force', 'Nothing at all', 'Only sunlight', 'Only gravity'], 0),
    ('Which is a real-life example of Newtons third law?', ['A swimmer pushing water backward to move forward', 'A ball that never moves', 'A rock sitting still with no force', 'An object floating in a vacuum with no interactions'], 0)]),
SS('Social Studies: The Klondike Gold Rush',
   'Grade 4 Social Studies strand: the Klondike Gold Rush of the late 1890s drew thousands of prospectors to the Yukon in search of gold, shaping the growth of towns such as Dawson City and the history of northern Canada.',
   [('What resource drew thousands of prospectors to the Yukon during the Klondike Gold Rush?', ['Gold', 'Oil', 'Coal', 'Diamonds'], 0),
    ('In which decade did the Klondike Gold Rush mainly take place?', ['The 1890s', 'The 1700s', 'The 1950s', 'The 1600s'], 0),
    ('Which town grew rapidly because of the Klondike Gold Rush?', ['Dawson City', 'Toronto', 'Ottawa', 'Halifax'], 0),
    ('What challenges did prospectors often face traveling to the Klondike?', ['Harsh terrain and difficult northern conditions', 'No challenges at all', 'Warm tropical weather', 'Easy travel by highway'], 0),
    ('How did the Klondike Gold Rush affect northern Canada?', ['It brought rapid population growth and development to the region', 'It caused the region to become empty', 'It had no lasting effect', 'It only affected southern Canada'], 0)]),
]),
day(137, [
L('Vocabulary: Regional Dialects and Word Choice',
  'Grade 4 Language strand: a dialect is a way of speaking shared by people in a particular region or group, involving differences in word choice, pronunciation, and expressions, such as pop versus soda.',
  [('What is a dialect?', ['A way of speaking shared by people in a region or group', 'A type of punctuation', 'A single incorrect word', 'A grammar rule with no exceptions'], 0),
   ('What might differ between regional dialects?', ['Word choice, pronunciation, and expressions', 'Only spelling of numbers', 'Nothing at all', 'Only capitalization rules'], 0),
   ('Which is an example of regional word choice differences?', ['Some regions say pop while others say soda', 'All regions use identical words for everything', 'Dialects do not affect word choice', 'Only written language has dialects'], 0),
   ('Why is it useful to understand different dialects?', ['It helps us communicate and understand speakers from different regions', 'Dialects have no real purpose', 'Understanding dialects is never useful', 'Only one dialect is considered correct'], 0),
   ('Is a dialect considered incorrect language?', ['No, dialects are valid ways of speaking shared by a community', 'Yes, dialects are always wrong', 'Dialects do not exist', 'Dialects are only used in writing'], 0)]),
M('Fractions: Multiplying a Fraction by a Fraction',
  'Grade 4 Math strand: to multiply a fraction by a fraction, students multiply the numerators together and multiply the denominators together, then simplify if possible.',
  [('How do you multiply two fractions together?', ['Multiply the numerators together and the denominators together', 'Add the numerators and denominators', 'Only multiply the denominators', 'Only multiply the numerators'], 0),
   ('What is 1/2 x 1/3?', ['1/6', '1/5', '2/3', '1/3'], 0),
   ('What is 1/2 x 1/2?', ['1/4', '1/2', '3/4', '1/6'], 0),
   ('What is 2/3 x 1/2?', ['1/3', '3/5', '2/3', '1/2'], 0),
   ('Why does multiplying two fractions less than one usually create a smaller result?', ['Because you are finding a fractional part of a fractional part', 'Multiplication always makes numbers bigger', 'Fractions cannot be multiplied', 'The result is always equal to one'], 0)]),
Sc('Science: The Food Groups and Healthy Eating',
   'Grade 4 Science strand: a balanced diet includes foods from different groups, such as vegetables and fruits, grain products, protein foods, and dairy or alternatives, each providing nutrients the body needs to grow and stay healthy.',
   [('Why does the body need a variety of food groups?', ['Different foods provide different nutrients the body needs', 'The body only needs one type of food', 'Food groups have no effect on health', 'Eating a variety of foods is unnecessary'], 0),
    ('Which food group provides vitamins found in many colourful foods?', ['Vegetables and fruits', 'Only sugary snacks', 'Only fried foods', 'Only candy'], 0),
    ('Which food group provides energy through foods such as bread and rice?', ['Grain products', 'Only desserts', 'Only fats', 'Only spices'], 0),
    ('Why are protein foods important for the body?', ['They help build and repair muscles and tissues', 'They have no function in the body', 'They only provide flavour', 'They are harmful to the body'], 0),
    ('What is one benefit of eating a balanced variety of foods?', ['It helps the body grow, function, and stay healthy', 'It has no effect on health', 'It only helps with taste', 'Balanced eating is unnecessary for children'], 0)]),
SS('Social Studies: How Provinces Make Laws — Provincial Legislatures',
   'Grade 4 Social Studies strand: each Canadian province has its own legislature that debates and passes provincial laws on matters such as education and health care, led by a premier and elected members.',
   [('What is a provincial legislature responsible for?', ['Debating and passing provincial laws', 'Passing laws for other countries', 'Running local sports teams', 'Managing federal military forces'], 0),
    ('Who typically leads a provincial government?', ['The premier', 'The Prime Minister', 'The Governor General', 'The mayor'], 0),
    ('Name one area that provincial governments often oversee.', ['Education and health care', 'Foreign trade agreements', 'National defence', 'International treaties'], 0),
    ('How are members of a provincial legislature usually chosen?', ['Elected by voters in the province', 'Appointed by another country', 'Chosen at random', 'Inherited through family'], 0),
    ('Why does Canada have both federal and provincial governments?', ['To share responsibilities between national and regional levels', 'Because Canada has no federal government', 'Because provinces have no responsibilities', 'To eliminate all local decision-making'], 0)]),
]),
day(138, [
L('Writing: Writing a Letter to the Editor',
  'Grade 4 Language strand: a letter to the editor expresses an opinion about a current issue in a newspaper or publication, using clear reasons and evidence to persuade readers.',
  [('What is the purpose of a letter to the editor?', ['To express an opinion about a current issue and persuade readers', 'To tell a fictional story', 'To give step-by-step instructions', 'To summarize a sports score'], 0),
   ('What should a letter to the editor include to be convincing?', ['Clear reasons and evidence supporting the opinion', 'Random unrelated facts', 'No opinion at all', 'Only questions with no statements'], 0),
   ('Where is a letter to the editor typically published?', ['In a newspaper or similar publication', 'Only in a private diary', 'Only in a textbook', 'Nowhere at all'], 0),
   ('What tone is usually appropriate for a letter to the editor?', ['A respectful, clear, and persuasive tone', 'An angry, disrespectful tone', 'A silly, joking tone with no purpose', 'A completely neutral tone with no opinion'], 0),
   ('Why might someone write a letter to the editor about a local issue?', ['To raise awareness and encourage change or discussion', 'Letters to the editor cannot discuss local issues', 'To avoid sharing any opinion', 'To copy someone elses letter exactly'], 0)]),
M('Geometry: Area of Triangles Using a Formula',
  'Grade 4 Math strand: the area of a triangle is found using the formula base multiplied by height, divided by two, since a triangle is half of a parallelogram with the same base and height.',
  [('What is the formula for finding the area of a triangle?', ['Base multiplied by height, divided by two', 'Base multiplied by height', 'Base plus height', 'Base multiplied by height multiplied by two'], 0),
   ('What is the area of a triangle with a base of 6 and a height of 4?', ['12', '24', '10', '20'], 0),
   ('What is the area of a triangle with a base of 10 and a height of 5?', ['25', '50', '15', '45'], 0),
   ('Why is the area of a triangle half of base times height?', ['A triangle is half of a parallelogram with the same base and height', 'Triangles have no relationship to parallelograms', 'Area formulas are chosen randomly', 'A triangle always has zero area'], 0),
   ('Which measurement is needed along with the base to find a triangles area?', ['The height', 'The perimeter', 'The number of sides', 'The colour'], 0)]),
Sc('Science: Comparing the Planets — Size, Distance, and Composition',
   'Grade 4 Science strand: the eight planets in our solar system differ greatly in size, distance from the Sun, and composition, ranging from small rocky planets like Mercury to huge gas giants like Jupiter.',
   [('Which planet is the largest in our solar system?', ['Jupiter', 'Mercury', 'Earth', 'Mars'], 0),
    ('Which planet is closest to the Sun?', ['Mercury', 'Earth', 'Venus', 'Neptune'], 0),
    ('What are Mercury, Venus, Earth, and Mars often classified as?', ['Rocky planets', 'Gas giants', 'Ice planets', 'Moons'], 0),
    ('What are Jupiter and Saturn often classified as?', ['Gas giants', 'Rocky planets', 'Dwarf planets', 'Asteroids'], 0),
    ('Why do planets farther from the Sun generally take longer to orbit it?', ['They travel a much longer path around the Sun', 'They move faster than closer planets', 'Distance has no effect on orbit time', 'All planets take exactly the same time to orbit'], 0)]),
SS('Social Studies: Canadian Sports and National Games',
   'Grade 4 Social Studies strand: sports such as hockey and lacrosse hold special cultural significance in Canada, with lacrosse recognized as a summer national sport rooted in Indigenous tradition and hockey deeply woven into Canadian identity.',
   [('Which sport is widely considered central to Canadian culture and identity?', ['Hockey', 'Cricket', 'Rugby', 'Sumo wrestling'], 0),
    ('Which sport is recognized as Canadas official summer national sport?', ['Lacrosse', 'Basketball', 'Soccer', 'Golf'], 0),
    ('What is the origin of lacrosse?', ['It has roots in Indigenous tradition', 'It was invented in Europe', 'It has no historical origin', 'It was invented very recently'], 0),
    ('Why are national sports significant to a country?', ['They can reflect shared culture, history, and identity', 'National sports have no significance', 'They are only played by professionals', 'They have no connection to culture'], 0),
    ('What season is hockey traditionally associated with in Canada?', ['Winter', 'Summer', 'Spring only', 'Autumn only'], 0)]),
]),
day(139, [
L('Reading: Analyzing Illustrations and Visual Elements in Non-Fiction Texts',
  'Grade 4 Language strand: illustrations, diagrams, and photographs in non-fiction texts provide visual information that supports and extends the written words, helping readers better understand the topic.',
  [('What is the purpose of illustrations in a non-fiction text?', ['To provide visual information that supports the written words', 'To replace all written words', 'To confuse the reader', 'To take up empty space'], 0),
   ('What might a labelled diagram help a reader understand?', ['The parts of an object or process', 'Nothing useful', 'Only the title of the book', 'Only the authors name'], 0),
   ('Why might a photograph be included in a non-fiction text?', ['To show a real example related to the topic', 'Photographs are never used in non-fiction', 'To replace the entire text', 'To confuse readers on purpose'], 0),
   ('How should readers use illustrations alongside the text?', ['Use them together with the words to build understanding', 'Ignore illustrations completely', 'Only look at illustrations and skip the words', 'Illustrations have no connection to the text'], 0),
   ('What visual element often shows steps in a process?', ['A diagram with numbered steps', 'A single colour with no labels', 'An unrelated photograph', 'A blank page'], 0)]),
M('Data Management: Constructing a Histogram',
  'Grade 4 Math strand: a histogram is a type of bar graph that displays how data is distributed across ranges of numerical values, with bars touching to show continuous data.',
  [('What does a histogram display?', ['How data is distributed across ranges of numerical values', 'Only a single data point', 'Data with no numerical values', 'Only the mode of a data set'], 0),
   ('How is a histogram different from a regular bar graph?', ['Its bars touch to show continuous numerical ranges', 'Its bars are always separated by gaps', 'It never uses numbers', 'It only shows categories with no ranges'], 0),
   ('What might the x-axis of a histogram show?', ['Ranges of values, such as test score intervals', 'Only colours', 'Only names of students', 'Nothing numerical'], 0),
   ('What might the y-axis of a histogram show?', ['The frequency, or how many data points fall in each range', 'The exact value of a single point', 'The title of the graph', 'Nothing useful'], 0),
   ('Why are histograms useful for large data sets?', ['They show patterns and distribution at a glance', 'They hide all patterns in the data', 'They can only show two data points', 'They are never used with numerical data'], 0)]),
Sc('Science: Teeth and Dental Health',
   'Grade 4 Science strand: humans have different types of teeth, including incisors, canines, and molars, each shaped for a different job in biting and chewing food, and healthy habits help protect teeth from decay.',
   [('What job do incisors do?', ['Cutting food', 'Grinding food', 'Tearing food only', 'Digesting food'], 0),
    ('What job do molars do?', ['Grinding and chewing food', 'Cutting food only', 'Sensing taste', 'Producing saliva'], 0),
    ('What job do canine teeth do?', ['Tearing food', 'Grinding food', 'Digesting food', 'Producing enamel'], 0),
    ('What outer layer protects teeth from damage?', ['Enamel', 'Bone', 'Muscle', 'Cartilage'], 0),
    ('Which habit helps prevent tooth decay?', ['Brushing teeth regularly and reducing sugary foods', 'Eating sugary snacks constantly', 'Never brushing teeth', 'Avoiding all dental checkups'], 0)]),
SS('Social Studies: The Role of the Lieutenant Governor',
   'Grade 4 Social Studies strand: the Lieutenant Governor is the representative of the Crown at the provincial level, performing ceremonial duties and formally granting royal assent to provincial laws.',
   [('Who does the Lieutenant Governor represent at the provincial level?', ['The Crown', 'The Prime Minister', 'The United Nations', 'A foreign government'], 0),
    ('What must a provincial bill receive from the Lieutenant Governor to become law?', ['Royal assent', 'A public vote only', 'A court ruling', 'A newspaper announcement'], 0),
    ('What type of duties does the Lieutenant Governor often perform?', ['Ceremonial duties', 'Managing a citys police force', 'Coaching sports teams', 'Running a business'], 0),
    ('How does the role of Lieutenant Governor compare to the Governor General?', ['It is a similar role but at the provincial level instead of the federal level', 'They are exactly the same job with the same title', 'The Lieutenant Governor has no connection to the Crown', 'The Lieutenant Governor governs another country'], 0),
    ('Why does Canada have a Lieutenant Governor in each province?', ['To represent the Crown and perform formal duties provincially', 'Provinces have no need for this role', 'To replace the premier entirely', 'To manage international trade only'], 0)]),
]),
day(140, [
L('Language Review: Grammar, Reading, and Writing Forms',
  'Grade 4 Language strand review: students revisit semicolons and colons, types of conflict, play scripts, allusion, and summarizing versus paraphrasing.',
  [('What can a semicolon join without using a conjunction?', ['Two closely related independent clauses', 'A single word and a comma', 'Two unrelated topics', 'A title and a subtitle'], 0),
   ('What is a literary conflict?', ['A problem or struggle a character faces', 'The setting of a story', 'The title of a book', 'A type of punctuation'], 0),
   ('What is a play script mainly made up of?', ['Dialogue and stage directions', 'Only descriptive paragraphs', 'Only a list of characters', 'Only a summary of events'], 0),
   ('What is an allusion?', ['A brief reference to something well known, such as a story or event', 'A type of punctuation mark', 'A word with no meaning', 'A long detailed description'], 0),
   ('What does summarizing a text involve?', ['Condensing the main ideas into a much shorter form', 'Copying the text word for word', 'Making the text longer', 'Ignoring the main ideas'], 0)]),
M('Math Review: Fractions, Number Sense, and Geometry',
  'Grade 4 Math strand review: students revisit subtracting fractions with unlike denominators, exponents, surface area, range, and Roman numerals.',
  [('What must fractions have before they can be subtracted directly?', ['A common denominator', 'The same numerator', 'A common numerator', 'Different denominators'], 0),
   ('What does an exponent tell you?', ['How many times a number is multiplied by itself', 'How many times to add a number', 'How many digits a number has', 'How to divide a number'], 0),
   ('What is surface area?', ['The total area of all the faces of a 3D shape', 'The space inside a shape', 'The distance around a shape', 'The height of a shape only'], 0),
   ('What is the range of a data set?', ['The difference between the largest and smallest values', 'The average of all values', 'The most common value', 'The middle value'], 0),
   ('What does the Roman numeral X represent?', ['10', '5', '1', '50'], 0)]),
Sc('Science Review: Heat, Life Science, and Chemistry',
   'Grade 4 Science strand review: students revisit heat transfer, seed dispersal, symbiosis, acids and bases, and cave formations.',
   [('What is conduction?', ['Heat transfer through direct contact between objects', 'Heat transfer through empty space', 'Heat transfer only in liquids', 'Heat that never moves'], 0),
    ('Why do plants need to disperse their seeds?', ['So new plants have room and resources to grow away from the parent plant', 'So seeds never grow into plants', 'So plants can stay in one exact spot forever', 'Seeds do not need to move'], 0),
    ('What is symbiosis?', ['A close relationship between two different species', 'A type of rock formation', 'A single organism living alone', 'A weather pattern'], 0),
    ('What is a common property of acids?', ['They often taste sour', 'They always taste sweet', 'They cannot be found in food', 'They never react with anything'], 0),
    ('What type of rock is commonly dissolved by water to form caves?', ['Limestone', 'Granite', 'Iron', 'Rubber'], 0)]),
SS('Social Studies Review: Ancient Civilizations, Geography, and Canadian History',
   'Grade 4 Social Studies strand review: students revisit the Byzantine Empire, the Rocky Mountains, the Canadian Pacific Railway, Canadas fishing industry, and the National Day for Truth and Reconciliation.',
   [('What was the Byzantine Empire a continuation of?', ['The eastern Roman Empire', 'A brand new empire with no history', 'The ancient Egyptian empire', 'The Greek city-states'], 0),
    ('In which part of Canada are the Rocky Mountains located?', ['Western Canada', 'Eastern Canada', 'Northern Canada only', 'Southern Ontario'], 0),
    ('What did the Canadian Pacific Railway connect?', ['Communities from coast to coast across Canada', 'Only two neighbouring cities', 'Canada to another country by land', 'Nothing of importance'], 0),
    ('What does the fishing industry harvest from Canadas coastal waters?', ['Seafood such as fish and shellfish', 'Only fresh vegetables', 'Only minerals', 'Only lumber'], 0),
    ('On what date is the National Day for Truth and Reconciliation observed?', ['September 30', 'July 1', 'November 11', 'October 31'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_131_140)
    append_to(4, g4_131_140)
