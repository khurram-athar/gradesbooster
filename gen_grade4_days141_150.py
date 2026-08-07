#!/usr/bin/env python3
"""Grade 4, Days 141-150 -- extends Grade 4 from 140 to 150 days. Modeled
exactly on gen_grade4_days131_140.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-140
topics (see data/grade4.json), which already densely cover nearly the
entire grade 4 curriculum. New topics: parallel structure, analyzing
character foils, writing a public service announcement, understanding
jargon and technical vocabulary, comparing two texts on the same topic,
verb moods, writing a persuasive advertisement script, identifying bias in
historical accounts, and understanding euphemisms for Language; dividing a
fraction by a whole number, volume of triangular prisms, an introduction
to integers, interpreting stacked bar graphs, rounding to the nearest ten
thousand, calculating change with multiple bills and coins, finding
missing angles in a triangle, comparing fractions decimals and percents,
and perimeter of composite shapes for Math; photosynthesis, vertebrates
and invertebrates, plant parts and their functions, magnetic fields and
compasses, the life cycle of a frog, static electricity and lightning,
an introduction to galaxies and the Milky Way, nocturnal animals, and
air pressure and wind for Science; and the Hudson Bay Company and the fur
trade economy, how taxes support Canadian communities, Canadas national
symbols (the beaver and the maple leaf), the Supreme Court of Canada,
ancient Israel and the Fertile Crescent, the Royal Canadian Mint, the
Canadian Armed Forces, public libraries, and World Heritage Sites in
Canada for Social Studies -- none of those exact ideas appear in Days
1-140. Day 150 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch (one representative
question drawn from each of the first five lessons of the batch, per
subject, exactly as Day 140 did for Days 131-135). No embedded ASCII
double-quote or apostrophe characters are used anywhere in title/summary/
question/option text, matching the convention used in
gen_grade4_days131_140.py (apostrophes dropped entirely, e.g. "Canadas"
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


def _rebalance_answer_positions(days, seed=20260810):
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


g4_141_150 = [
day(141, [
L('Grammar: Parallel Structure in Sentences',
  'Grade 4 Language strand: parallel structure means using the same grammatical pattern for items in a list or series, such as making sure all items are the same part of speech or verb form.',
  [('What is parallel structure in a sentence?', ['Using the same grammatical pattern for items in a series', 'Using a different verb tense for each item', 'Never using lists in a sentence', 'Using only nouns and no verbs'], 0),
   ('Which sentence uses parallel structure correctly?', ['She likes running, swimming, and biking.', 'She likes running, to swim, and biking.', 'She likes to run, swimming, and bike.', 'She likes runs, swims, and biking.'], 0),
   ('Why is parallel structure important in writing?', ['It makes sentences clearer and easier to read', 'It makes sentences confusing on purpose', 'It removes all verbs from a sentence', 'It has no effect on writing'], 0),
   ('What is wrong with the sentence He enjoys hiking, to fish, and camping?', ['It mixes a gerund and an infinitive instead of using the same form', 'It is already correct', 'It has too many commas', 'It uses no verbs at all'], 0),
   ('What should all items in a parallel list share?', ['The same grammatical form', 'Completely different meanings', 'Different punctuation each time', 'No connection to each other'], 0)]),
M('Fractions: Dividing a Fraction by a Whole Number',
  'Grade 4 Math strand: to divide a fraction by a whole number, students can think of splitting the fraction into that many equal groups, which multiplies the denominator by the whole number.',
  [('What happens to the denominator when dividing a fraction by a whole number?', ['The denominator is multiplied by the whole number', 'The denominator is divided by the whole number', 'The denominator stays exactly the same', 'The numerator disappears'], 0),
   ('What is 1/2 divided by 2?', ['1/4', '1/2', '1', '2/2'], 0),
   ('What is 1/3 divided by 2?', ['1/6', '1/3', '2/3', '1/2'], 0),
   ('What is 2/5 divided by 2?', ['1/5', '2/5', '4/5', '1/10'], 0),
   ('Why does dividing a fraction by a whole number usually make it smaller?', ['Because the fraction is being split into more equal parts', 'Division always makes numbers larger', 'The numerator always becomes zero', 'Fractions cannot be divided'], 0)]),
Sc('Science: Photosynthesis — How Plants Make Their Own Food',
   'Grade 4 Science strand: photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to make their own food and release oxygen as a byproduct.',
   [('What is photosynthesis?', ['The process by which plants make their own food using sunlight', 'A process where plants absorb food from soil only', 'A process where plants produce no oxygen', 'A process that only happens at night'], 0),
    ('What three things do plants need for photosynthesis?', ['Sunlight, water, and carbon dioxide', 'Only soil and rocks', 'Only darkness and water', 'Only oxygen and sugar'], 0),
    ('What gas do plants release during photosynthesis?', ['Oxygen', 'Carbon dioxide only', 'Nitrogen', 'Hydrogen'], 0),
    ('Where in a plant does most photosynthesis take place?', ['In the leaves', 'In the roots only', 'In the flowers only', 'In the bark only'], 0),
    ('Why is photosynthesis important for other living things?', ['It produces oxygen and food that many organisms depend on', 'It removes all oxygen from the air', 'It has no effect on other living things', 'It only matters to plants and no one else'], 0)]),
SS('Social Studies: Hudson Bay Company and the Fur Trade Economy',
   'Grade 4 Social Studies strand: the Hudson Bay Company was a major fur trading company that played a significant role in the exploration, economy, and early history of what is now Canada.',
   [('What kind of company was the Hudson Bay Company?', ['A major fur trading company', 'A modern technology company', 'An airline company', 'A film production company'], 0),
    ('What role did the Hudson Bay Company play in early Canadian history?', ['It played a major role in exploration and the fur trade economy', 'It had no role in Canadian history', 'It only operated outside of North America', 'It focused only on farming'], 0),
    ('What resource was central to the Hudson Bay Companys trade?', ['Animal furs, such as beaver pelts', 'Gold and silver only', 'Grain and wheat', 'Oil and gas'], 0),
    ('How did the fur trade affect relationships between European traders and Indigenous peoples?', ['It led to trading partnerships and exchanges of goods', 'It caused no interaction between the two groups', 'It only involved European traders', 'It had no effect on either group'], 0),
    ('Why is the Hudson Bay Company still studied in Canadian history today?', ['It significantly shaped early exploration, trade, and settlement patterns', 'It has no lasting historical importance', 'It was active for only one single day', 'It only affected countries outside North America'], 0)]),
]),
day(142, [
L('Reading: Analyzing Character Foils',
  'Grade 4 Language strand: a character foil is a character whose traits contrast with another character, highlighting specific qualities of the main character through the difference.',
  [('What is a character foil?', ['A character whose traits contrast with another character to highlight qualities', 'A character who looks exactly like the main character', 'A character who never appears in the story', 'A type of punctuation mark'], 0),
   ('What does a foil help readers notice about the main character?', ['Specific traits or qualities through contrast', 'Nothing useful about the story', 'Only the setting of the story', 'The authors name'], 0),
   ('If a brave character is paired with a timid character, what literary device might this show?', ['A character foil emphasizing bravery through contrast', 'A simile comparing two objects', 'An example of alliteration', 'A type of onomatopoeia'], 0),
   ('Where might a character foil appear in a story?', ['As a friend, sibling, or rival with opposite traits', 'Only in the title of the book', 'Only in the table of contents', 'Never in fiction'], 0),
   ('Why do authors use character foils?', ['To make certain traits of a character stand out more clearly', 'To confuse readers with no purpose', 'To remove conflict from a story', 'To avoid describing any characters'], 0)]),
M('Geometry: Volume of Triangular Prisms',
  'Grade 4 Math strand: the volume of a triangular prism is found by multiplying the area of its triangular base by the length of the prism.',
  [('What shape is the base of a triangular prism?', ['A triangle', 'A square', 'A circle', 'A pentagon'], 0),
   ('How do you find the volume of a triangular prism?', ['Multiply the area of the triangular base by the length of the prism', 'Multiply only the two shortest sides', 'Add all the edges together', 'Multiply the perimeter by the height'], 0),
   ('If a triangular base has an area of 6 square units and the prism is 5 units long, what is the volume?', ['30 cubic units', '11 cubic units', '25 cubic units', '6 cubic units'], 0),
   ('What units are used to measure the volume of a prism?', ['Cubic units', 'Square units', 'Linear units', 'No units are needed'], 0),
   ('Why is finding the area of the triangular base an important first step?', ['Because volume depends on the area of the base multiplied by length', 'The base has no effect on volume', 'Volume can be found without knowing the base', 'Triangular prisms never have a measurable base'], 0)]),
Sc('Science: Vertebrates and Invertebrates — Classifying Animals',
   'Grade 4 Science strand: animals can be classified as vertebrates, which have a backbone, or invertebrates, which do not, helping scientists organize and study the animal kingdom.',
   [('What is a vertebrate?', ['An animal that has a backbone', 'An animal that has no backbone', 'A type of plant', 'A type of rock'], 0),
    ('What is an invertebrate?', ['An animal that does not have a backbone', 'An animal that always has a backbone', 'A type of mineral', 'A type of weather pattern'], 0),
    ('Which of these is an example of a vertebrate?', ['A fish', 'A jellyfish', 'An insect', 'A worm'], 0),
    ('Which of these is an example of an invertebrate?', ['A snail', 'A bird', 'A mammal', 'A reptile'], 0),
    ('Why do scientists classify animals into groups like vertebrates and invertebrates?', ['It helps organize and study the wide variety of animals', 'Classification has no scientific purpose', 'All animals are exactly the same', 'Classification only applies to plants'], 0)]),
SS('Social Studies: How Taxes Support Canadian Communities',
   'Grade 4 Social Studies strand: taxes are money collected by governments from individuals and businesses, used to fund public services such as schools, roads, hospitals, and emergency services in Canadian communities.',
   [('What are taxes?', ['Money collected by governments to fund public services', 'Money given only to private businesses', 'A type of currency used only in stores', 'A voluntary gift with no purpose'], 0),
    ('Which of these is commonly funded by tax money?', ['Public schools and hospitals', 'Only private vacations', 'Only individual savings accounts', 'Only foreign purchases'], 0),
    ('Who is generally responsible for paying taxes?', ['Individuals and businesses', 'Only visitors from other countries', 'Only children', 'No one is responsible for taxes'], 0),
    ('Why are taxes important for a community?', ['They help pay for shared services everyone can use', 'They have no benefit to the community', 'Taxes only benefit the government itself', 'Taxes remove all public services'], 0),
    ('Which level of government might collect taxes in Canada?', ['Federal, provincial, and municipal governments', 'Only foreign governments', 'Only private companies', 'No government collects taxes'], 0)]),
]),
day(143, [
L('Writing: Writing a Public Service Announcement',
  'Grade 4 Language strand: a public service announcement is a short persuasive message that informs the public about an important issue and encourages a specific action, often used on radio, television, or posters.',
  [('What is the purpose of a public service announcement?', ['To inform the public about an issue and encourage action', 'To tell a made-up bedtime story', 'To sell a specific brand of toy', 'To share a private diary entry'], 0),
   ('Where might a public service announcement be shared?', ['On radio, television, or posters', 'Only in a private letter', 'Only in a math textbook', 'Nowhere at all'], 0),
   ('What should a strong public service announcement include?', ['A clear message and a call to action', 'Random unrelated facts', 'No message at all', 'Only decorative pictures'], 0),
   ('Which topic would be appropriate for a public service announcement?', ['Encouraging people to recycle', 'Describing a fictional dragon', 'Listing random numbers', 'Sharing a private joke'], 0),
   ('Why do public service announcements use short, clear language?', ['So the audience quickly understands and remembers the message', 'To make the message harder to understand', 'Because rules require no words at all', 'Short language has no benefit'], 0)]),
M('Number Sense: Introduction to Integers (Positive and Negative Numbers)',
  'Grade 4 Math strand: integers include positive numbers, negative numbers, and zero, and can be used to represent values such as temperatures below zero or money owed.',
  [('What are integers?', ['Positive numbers, negative numbers, and zero', 'Only positive numbers', 'Only fractions', 'Only decimals'], 0),
   ('What might a negative integer represent in real life?', ['A temperature below zero', 'A number of apples in a basket', 'The number of days in a week', 'The number of sides on a square'], 0),
   ('Which of these is a negative integer?', ['-5', '5', '0.5', '1/2'], 0),
   ('On a number line, where are negative integers located compared to zero?', ['To the left of zero', 'To the right of zero', 'Exactly at zero', 'Negative integers do not exist on a number line'], 0),
   ('Which integer is greater, -3 or -8?', ['-3', '-8', 'They are equal', 'Neither can be compared'], 0)]),
Sc('Science: Plant Parts and Their Functions — Roots, Stems, Leaves, and Flowers',
   'Grade 4 Science strand: each part of a plant has a specific function, with roots absorbing water and nutrients, stems supporting the plant and transporting materials, leaves capturing sunlight, and flowers producing seeds.',
   [('What is the main job of a plants roots?', ['Absorbing water and nutrients from the soil', 'Capturing sunlight for energy', 'Producing seeds', 'Releasing pollen only'], 0),
    ('What is the main job of a plants stem?', ['Supporting the plant and transporting water and nutrients', 'Absorbing sunlight directly', 'Producing fruit only', 'Anchoring the plant underground'], 0),
    ('What is the main job of a plants leaves?', ['Capturing sunlight to make food through photosynthesis', 'Absorbing water from the soil', 'Producing seeds for reproduction', 'Anchoring the plant in place'], 0),
    ('What is the main job of a plants flowers?', ['Producing seeds for reproduction', 'Absorbing water and nutrients', 'Supporting the entire plant structure', 'Releasing oxygen only at night'], 0),
    ('Why does a plant need all of these parts working together?', ['Each part performs a different function needed for the plant to survive and grow', 'Only one part is ever needed for survival', 'Plant parts have no connection to each other', 'Plants do not need roots or stems'], 0)]),
SS('Social Studies: Canadas National Symbols — The Beaver and the Maple Leaf',
   'Grade 4 Social Studies strand: Canada has several national symbols, including the beaver, recognized for its role in the fur trade and industriousness, and the maple leaf, featured on the national flag and representing Canadian identity.',
   [('Which animal is a well-known national symbol of Canada?', ['The beaver', 'The lion', 'The eagle', 'The kangaroo'], 0),
    ('What historical industry is the beaver closely associated with in Canada?', ['The fur trade', 'The mining industry', 'The fishing industry', 'The film industry'], 0),
    ('What plant symbol appears on the Canadian flag?', ['The maple leaf', 'The oak leaf', 'The palm leaf', 'The rose'], 0),
    ('Why are national symbols like the beaver and maple leaf important to Canadian identity?', ['They represent shared history and help people feel connected to their country', 'They have no connection to Canadian history', 'They are only used outside of Canada', 'They represent a completely different country'], 0),
    ('Where might you see the maple leaf symbol displayed?', ['On the Canadian flag and various official items', 'Only on private property', 'Only in other countries', 'Nowhere in Canada'], 0)]),
]),
day(144, [
L('Vocabulary: Understanding Jargon and Technical Vocabulary',
  'Grade 4 Language strand: jargon is special vocabulary used by people in a particular field or group, such as doctors or athletes, that may be unfamiliar to general readers.',
  [('What is jargon?', ['Special vocabulary used by people in a particular field or group', 'A type of punctuation mark', 'A word with no meaning at all', 'A grammar rule for verbs'], 0),
   ('Who might use medical jargon?', ['Doctors and nurses', 'Only young children', 'Only fictional characters', 'No one uses jargon'], 0),
   ('Why might jargon be confusing to general readers?', ['It uses specialized terms unfamiliar outside that field', 'It always uses the simplest words possible', 'Jargon is identical in every field', 'Jargon never appears in real language'], 0),
   ('What should a writer do when using jargon for a general audience?', ['Explain or define the specialized terms', 'Use only jargon with no explanation', 'Avoid all vocabulary completely', 'Assume everyone already knows it'], 0),
   ('Which is an example of sports jargon?', ['A term like slam dunk used among basketball players', 'A common word like table', 'A punctuation mark', 'A silent letter'], 0)]),
M('Data Management: Interpreting Stacked Bar Graphs',
  'Grade 4 Math strand: a stacked bar graph shows multiple categories within a single bar, with each section representing a different part of the total for that bar.',
  [('What does a stacked bar graph show within a single bar?', ['Multiple categories stacked to show parts of a total', 'Only one category with no divisions', 'A single number with no comparison', 'Nothing measurable'], 0),
   ('How can you find the total value represented by a stacked bar?', ['Add up all the sections stacked within that bar', 'Only look at the top section', 'Multiply the number of sections', 'Subtract each section from the others'], 0),
   ('Why might a stacked bar graph be useful for comparing data?', ['It shows both individual parts and the overall total at once', 'It only shows a single value with no detail', 'It cannot be used to compare anything', 'It hides all the data'], 0),
   ('What might different colours within a stacked bar represent?', ['Different categories or subgroups of data', 'Nothing at all', 'Only decoration', 'The title of the graph'], 0),
   ('If one bar shows red for 3 units and blue for 2 units stacked together, what is the total height of that bar?', ['5 units', '3 units', '2 units', '6 units'], 0)]),
Sc('Science: Magnetic Fields and Compasses',
   'Grade 4 Science strand: a magnet creates an invisible magnetic field around it, and a compass uses a small magnetized needle that aligns with Earths magnetic field to point toward magnetic north.',
   [('What is a magnetic field?', ['An invisible area of force surrounding a magnet', 'A visible line drawn around a magnet', 'A type of electrical current', 'A type of sound wave'], 0),
    ('What does a compass needle align with?', ['Earths magnetic field', 'The nearest light source', 'The direction of the wind', 'The temperature of the air'], 0),
    ('Which direction does a compass needle typically point?', ['Toward magnetic north', 'Toward the ground', 'Toward the nearest building', 'In a random direction each time'], 0),
    ('Why is a compass a useful navigation tool?', ['It helps travellers determine direction using Earths magnetic field', 'It has no practical use for navigation', 'It only works underwater', 'It measures temperature instead of direction'], 0),
    ('What happens to a compass needle near a strong magnet?', ['It can be pulled away from pointing to magnetic north', 'It always points south instead', 'It stops working permanently', 'It has no reaction at all'], 0)]),
SS('Social Studies: The Role of the Supreme Court of Canada',
   'Grade 4 Social Studies strand: the Supreme Court of Canada is the highest court in the country, making final decisions on important legal cases and ensuring laws follow the Canadian Constitution.',
   [('What is the Supreme Court of Canada?', ['The highest court in the country', 'A local municipal office', 'A branch of the police force', 'A private business court'], 0),
    ('What kind of decisions does the Supreme Court of Canada make?', ['Final decisions on important legal cases', 'Decisions about school lunch menus', 'Decisions about sports team rules', 'Decisions about weather forecasts'], 0),
    ('What document must Canadian laws align with, according to the Supreme Court?', ['The Canadian Constitution', 'A private companys rules', 'A foreign countrys constitution', 'A local city bylaw only'], 0),
    ('Why is having a highest court important for a country?', ['It provides a final, consistent decision on major legal questions', 'It has no real purpose in government', 'It replaces the need for any other courts', 'It only handles minor disputes'], 0),
    ('Who might bring a case to the Supreme Court of Canada?', ['People or groups involved in significant legal disputes', 'Only foreign governments', 'Only young children', 'No one is allowed to bring cases'], 0)]),
]),
day(145, [
L('Reading: Comparing Two Texts on the Same Topic',
  'Grade 4 Language strand: comparing two texts on the same topic involves identifying similarities and differences in the information, perspective, or purpose each author presents.',
  [('What does comparing two texts on the same topic involve?', ['Identifying similarities and differences between the texts', 'Reading only one of the texts', 'Ignoring the topic entirely', 'Copying one text exactly'], 0),
   ('Why might two texts about the same topic present different information?', ['Authors can have different purposes, perspectives, or sources', 'All texts on a topic are always identical', 'Topics never have more than one source', 'Texts about the same topic are not allowed to differ'], 0),
   ('What is one way authors perspectives might differ on the same topic?', ['One author might focus on benefits while another focuses on risks', 'All authors always agree completely', 'Perspective has no effect on writing', 'Only fictional texts can differ'], 0),
   ('Why is it useful to read multiple texts about the same topic?', ['It gives a fuller and more balanced understanding', 'It always causes more confusion', 'One text is always enough', 'Comparing texts is never useful'], 0),
   ('What might readers look for when comparing texts?', ['Facts, opinions, and evidence presented differently', 'Only the page numbers', 'Only the font used', 'Only the length of each text'], 0)]),
M('Number Sense: Rounding to the Nearest Ten Thousand',
  'Grade 4 Math strand: to round a number to the nearest ten thousand, students look at the thousands digit to decide whether to round up or keep the ten thousands digit the same.',
  [('What digit do you check when rounding to the nearest ten thousand?', ['The thousands digit', 'The ones digit', 'The hundred thousands digit', 'The tenths digit'], 0),
   ('What is 43,700 rounded to the nearest ten thousand?', ['40,000', '50,000', '43,000', '44,000'], 0),
   ('What is 76,200 rounded to the nearest ten thousand?', ['80,000', '70,000', '76,000', '77,000'], 0),
   ('If the thousands digit is 5 or greater, what should you do when rounding to the nearest ten thousand?', ['Round the ten thousands digit up by one', 'Keep the ten thousands digit the same', 'Round down to zero', 'Ignore the digit completely'], 0),
   ('Why might someone round a large number to the nearest ten thousand?', ['To make the number easier to work with or estimate', 'To make the number less accurate for no reason', 'Rounding removes the need for all math', 'Rounding only works with small numbers'], 0)]),
Sc('Science: The Life Cycle of a Frog — Amphibian Metamorphosis',
   'Grade 4 Science strand: a frog undergoes complete metamorphosis, changing from an egg to a tadpole living in water, then developing legs and lungs to become an adult frog that can live on land and in water.',
   [('What is the first stage of a frogs life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'Froglet'], 0),
    ('Where do tadpoles typically live and breathe?', ['In water, using gills', 'On dry land, using lungs', 'In trees, using skin only', 'Underground, using no breathing organs'], 0),
    ('What major changes happen as a tadpole becomes a frog?', ['It grows legs and develops lungs for breathing air', 'It loses all its organs', 'It turns into a completely different animal species', 'It stops growing entirely'], 0),
    ('What term describes the frogs dramatic change in body form?', ['Metamorphosis', 'Photosynthesis', 'Migration', 'Hibernation'], 0),
    ('Where can adult frogs typically live?', ['Both in water and on land', 'Only deep underground', 'Only in the desert', 'Only high in the mountains'], 0)]),
SS('Social Studies: Ancient Israel and the Fertile Crescent',
   'Grade 4 Social Studies strand: ancient Israel developed within the Fertile Crescent, a region with rich soil and access to water that supported early farming, trade, and the growth of significant historical societies.',
   [('What is the Fertile Crescent known for?', ['Rich soil and water access that supported early farming', 'Being a completely dry desert with no water', 'Having no history of early civilizations', 'Being located entirely underwater'], 0),
    ('Why did early societies often settle near rivers in the Fertile Crescent?', ['Rivers provided water for farming and daily life', 'Rivers made travel and farming impossible', 'Early societies avoided rivers completely', 'Rivers had no value to ancient peoples'], 0),
    ('What activity was strongly supported by the fertile land in this region?', ['Farming', 'Deep sea fishing only', 'Mountain climbing', 'Ice fishing'], 0),
    ('What is ancient Israel an example of in this region?', ['A significant historical society that developed in the Fertile Crescent', 'A modern country with no ancient history', 'A civilization located in Antarctica', 'A society with no connection to farming'], 0),
    ('Why do historians study the Fertile Crescent today?', ['It helps explain the origins of early farming and civilization', 'It has no historical significance', 'It is important only for its modern buildings', 'It was never inhabited by ancient peoples'], 0)]),
]),
day(146, [
L('Grammar: Understanding Verb Moods — Indicative, Imperative, and Interrogative',
  'Grade 4 Language strand: verb mood shows the purpose of a sentence, with the indicative mood stating facts, the imperative mood giving commands, and the interrogative mood asking questions.',
  [('What does the indicative mood do?', ['States a fact or opinion', 'Gives a command', 'Asks a question', 'Expresses a wish'], 0),
   ('What does the imperative mood do?', ['Gives a command or request', 'States a fact', 'Asks a question', 'Describes a feeling only'], 0),
   ('Which sentence is in the interrogative mood?', ['Did you finish your homework?', 'Close the door.', 'The sky is blue.', 'Please sit down.'], 0),
   ('Which sentence is in the imperative mood?', ['Please close the window.', 'The window is open.', 'Is the window open?', 'The window was closed yesterday.'], 0),
   ('Why is it useful to recognize verb mood?', ['It helps understand the purpose of a sentence', 'Verb mood has no real use', 'It only matters in poetry', 'It replaces the need for punctuation'], 0)]),
M('Financial Literacy: Calculating Change with Multiple Bills and Coins',
  'Grade 4 Math strand: calculating change involves subtracting the cost of an item from the amount paid, then determining which combination of bills and coins makes up that amount.',
  [('How do you calculate the change owed after a purchase?', ['Subtract the cost of the item from the amount paid', 'Add the cost of the item to the amount paid', 'Multiply the cost by the amount paid', 'Divide the amount paid by the cost'], 0),
   ('If an item costs 6 dollars and 25 cents and you pay with a 10 dollar bill, how much change should you receive?', ['3 dollars and 75 cents', '4 dollars and 25 cents', '3 dollars and 25 cents', '4 dollars and 75 cents'], 0),
   ('Why might a cashier give change using the fewest bills and coins possible?', ['It is a simpler and more efficient way to make change', 'It always uses more coins than necessary', 'Fewer bills and coins is against store rules', 'It has no effect on the transaction'], 0),
   ('Which combination of coins equals exactly 2 dollars?', ['Two 1 dollar coins', 'One 1 dollar coin and one quarter', 'Three quarters', 'Five dimes'], 0),
   ('Why is it useful to practice calculating change?', ['It helps ensure you receive the correct amount of money back', 'It has no real-life application', 'Change is never given in stores', 'Calculating change is only used in math class'], 0)]),
Sc('Science: Static Electricity and Lightning',
   'Grade 4 Science strand: static electricity builds up when electric charges collect on the surface of an object, and lightning is a dramatic natural example of static electricity discharging between clouds or between a cloud and the ground.',
   [('What is static electricity?', ['A buildup of electric charge on the surface of an object', 'A steady flow of electricity through a wire', 'A type of sound wave', 'A type of magnetic field'], 0),
    ('What natural event is a large-scale example of static electricity discharging?', ['Lightning', 'Rainfall', 'Wind', 'Fog'], 0),
    ('What can cause static electricity to build up between two objects?', ['Rubbing two objects together', 'Placing objects in water', 'Freezing an object', 'Heating an object slowly'], 0),
    ('Why might your hair stand up after rubbing a balloon on it?', ['Static charge causes strands of hair to repel each other', 'The balloon removes all electricity from your hair', 'Hair always stands up in cold weather', 'Rubbing an object has no electrical effect'], 0),
    ('Why is it dangerous to be outside during a lightning storm?', ['Lightning carries a powerful electric discharge that can strike people', 'Lightning has no real danger', 'Lightning only strikes underwater', 'Lightning never travels toward the ground'], 0)]),
SS('Social Studies: The Royal Canadian Mint and How Coins Are Made',
   'Grade 4 Social Studies strand: the Royal Canadian Mint is the government organization responsible for designing and producing Canadas coins, using metal, precise measurements, and detailed designs.',
   [('What is the Royal Canadian Mint responsible for?', ['Designing and producing Canadas coins', 'Printing paper money only', 'Managing Canadas highways', 'Running Canadas schools'], 0),
    ('What material is commonly used to produce coins?', ['Metal', 'Wood', 'Paper', 'Glass'], 0),
    ('Why must coins be made with precise measurements?', ['So they are consistent in size, weight, and value', 'Precision has no importance for coins', 'Coins are never measured during production', 'Every coin is meant to be a different size'], 0),
    ('What might appear on the design of a Canadian coin?', ['Important symbols or figures representing Canada', 'Random unrelated images with no meaning', 'Foreign national symbols only', 'Nothing at all'], 0),
    ('Why is it useful to learn how coins are made?', ['It helps us understand the process behind everyday currency', 'Coins are not used in Canada', 'Learning about currency has no value', 'Coins appear naturally with no production process'], 0)]),
]),
day(147, [
L('Writing: Writing a Persuasive Advertisement Script',
  'Grade 4 Language strand: a persuasive advertisement script uses catchy language, strong reasons, and a clear call to action to convince an audience to buy a product or support an idea.',
  [('What is the goal of a persuasive advertisement script?', ['To convince an audience to buy a product or support an idea', 'To share a private diary entry', 'To describe a historical event only', 'To list random facts with no purpose'], 0),
   ('What is a call to action in an advertisement?', ['A clear statement telling the audience what to do next', 'A random unrelated sentence', 'A type of punctuation mark', 'The title of the product only'], 0),
   ('Why might an advertisement use catchy language?', ['To grab attention and make the message memorable', 'To confuse the audience on purpose', 'Catchy language has no effect on advertising', 'To make the ad longer with no purpose'], 0),
   ('What might a persuasive advertisement include to support its claims?', ['Strong reasons or benefits of the product', 'Only random numbers', 'No reasons at all', 'Unrelated jokes only'], 0),
   ('Where might an advertisement script be performed?', ['On television, radio, or in a video', 'Only in a private notebook', 'Nowhere at all', 'Only inside a math class'], 0)]),
M('Geometry: Finding Missing Angles in a Triangle',
  'Grade 4 Math strand: the three interior angles of a triangle always add up to 180 degrees, so a missing angle can be found by subtracting the sum of the two known angles from 180.',
  [('What do the three interior angles of a triangle always add up to?', ['180 degrees', '360 degrees', '90 degrees', '270 degrees'], 0),
   ('If two angles in a triangle are 50 degrees and 60 degrees, what is the third angle?', ['70 degrees', '60 degrees', '80 degrees', '110 degrees'], 0),
   ('If two angles in a triangle are both 45 degrees, what is the third angle?', ['90 degrees', '45 degrees', '180 degrees', '60 degrees'], 0),
   ('How do you find a missing angle when you know the other two angles of a triangle?', ['Subtract the sum of the two known angles from 180 degrees', 'Add the two known angles together for the answer', 'Multiply the two known angles', 'Divide 180 by the two known angles'], 0),
   ('What is the missing angle if a triangle has angles of 90 degrees and 30 degrees?', ['60 degrees', '90 degrees', '30 degrees', '120 degrees'], 0)]),
Sc('Science: Space — An Introduction to Galaxies and the Milky Way',
   'Grade 4 Science strand: a galaxy is a massive collection of stars, planets, gas, and dust held together by gravity, and our solar system is located within a galaxy called the Milky Way.',
   [('What is a galaxy?', ['A massive collection of stars, planets, gas, and dust held together by gravity', 'A single star with no planets', 'A small cloud found only on Earth', 'A type of moon'], 0),
    ('What is the name of the galaxy that contains our solar system?', ['The Milky Way', 'The Andromeda Galaxy', 'The Solar Galaxy', 'The Orion Galaxy'], 0),
    ('What force holds a galaxy together?', ['Gravity', 'Wind', 'Magnetism only', 'Heat alone'], 0),
    ('What might a galaxy contain besides stars?', ['Planets, gas, and dust', 'Only empty space with nothing else', 'Only water', 'Only oxygen'], 0),
    ('Why can we see a band of light in the night sky called the Milky Way?', ['We are viewing part of our own galaxy from within it', 'It is a reflection from the Moon', 'It is caused by clouds on Earth', 'It is an illusion with no real explanation'], 0)]),
SS('Social Studies: The Canadian Armed Forces — Serving at Home and Abroad',
   'Grade 4 Social Studies strand: the Canadian Armed Forces protect Canada and its citizens, respond to emergencies at home, and take part in international missions such as peacekeeping alongside other countries.',
   [('What is a key responsibility of the Canadian Armed Forces?', ['Protecting Canada and its citizens', 'Managing local libraries', 'Running provincial elections', 'Building highways only'], 0),
    ('What might the Canadian Armed Forces do during a natural disaster at home?', ['Help respond to emergencies and assist affected communities', 'Ignore the emergency completely', 'Only respond to disasters in other countries', 'Cancel all emergency services'], 0),
    ('What international role do Canadian Armed Forces members sometimes take part in?', ['Peacekeeping missions', 'Running foreign businesses', 'Coaching sports teams abroad', 'Teaching foreign languages only'], 0),
    ('Why might Canada take part in international peacekeeping missions?', ['To help maintain peace and stability alongside other countries', 'Canada never takes part in international missions', 'To avoid working with other countries', 'Peacekeeping has no connection to the military'], 0),
    ('Why is the Canadian Armed Forces an important part of Canadian society?', ['It helps protect citizens and supports missions both at home and abroad', 'It has no connection to protecting Canadians', 'It only exists during wartime', 'It focuses solely on foreign trade'], 0)]),
]),
day(148, [
L('Reading: Identifying Bias in Historical Accounts',
  'Grade 4 Language strand: bias in a historical account occurs when a writer presents information in a way that favours one perspective, often leaving out other viewpoints or important facts.',
  [('What is bias in a historical account?', ['Presenting information in a way that favours one perspective', 'Presenting every perspective completely equally', 'A type of punctuation mark', 'A summary with no opinions at all'], 0),
   ('Why might a biased historical account leave out certain facts?', ['To support one particular viewpoint over others', 'To always present a fully balanced view', 'Bias never affects which facts are included', 'All historical accounts are automatically unbiased'], 0),
   ('How can readers identify possible bias in a text?', ['By checking whether other viewpoints or facts are missing', 'By trusting every single text completely', 'By ignoring the source of the text', 'Bias cannot ever be identified'], 0),
   ('Why is it useful to compare multiple historical sources?', ['It helps reveal different perspectives and possible bias', 'Comparing sources is never useful', 'One source is always enough', 'Multiple sources always say the exact same thing'], 0),
   ('What might indicate a source has strong bias?', ['Only describing one groups viewpoint as entirely correct', 'Presenting balanced evidence from multiple sides', 'Including dates and verified facts', 'Citing multiple credible sources'], 0)]),
M('Number Sense: Comparing Fractions Decimals and Percents',
  'Grade 4 Math strand: fractions, decimals, and percents are different ways of representing the same value, and converting between them helps students compare and order numbers.',
  [('What do fractions, decimals, and percents all represent?', ['Different ways of showing the same value', 'Only whole numbers', 'Only negative numbers', 'Completely unrelated concepts'], 0),
   ('What is 1/2 written as a decimal?', ['0.5', '0.2', '0.25', '1.5'], 0),
   ('What is 0.5 written as a percent?', ['50%', '5%', '500%', '0.5%'], 0),
   ('Which is greater, 1/4 or 0.4?', ['0.4', '1/4', 'They are equal', 'They cannot be compared'], 0),
   ('Why is it useful to convert between fractions, decimals, and percents?', ['It makes it easier to compare and order different values', 'Conversion is never useful in math', 'Fractions and decimals can never be compared', 'Percents cannot represent fractions'], 0)]),
Sc('Science: Nocturnal Animals and Their Adaptations',
   'Grade 4 Science strand: nocturnal animals are active mainly at night and have special adaptations, such as large eyes, strong hearing, or a keen sense of smell, that help them survive in the dark.',
   [('What does it mean for an animal to be nocturnal?', ['It is mainly active at night', 'It is mainly active during the day', 'It never sleeps at all', 'It lives only underwater'], 0),
    ('What adaptation helps many nocturnal animals see in low light?', ['Large eyes that gather more light', 'Extremely small eyes', 'No eyes at all', 'Bright colouring'], 0),
    ('Which of these is an example of a nocturnal animal?', ['An owl', 'A robin', 'A butterfly', 'A squirrel'], 0),
    ('Why might being active at night help some animals avoid predators?', ['Fewer daytime predators are hunting during the night', 'Nighttime has no predators anywhere', 'Predators are more active exclusively at night', 'Darkness has no effect on predator activity'], 0),
    ('Besides eyesight, what other sense might help nocturnal animals navigate in the dark?', ['A strong sense of hearing or smell', 'A sense of taste only', 'No senses are needed at night', 'Only their sense of sight'], 0)]),
SS('Social Studies: Public Libraries and Their Role in Canadian Communities',
   'Grade 4 Social Studies strand: public libraries are community institutions that provide free access to books, information, and programs, supporting learning and connection for people of all ages.',
   [('What do public libraries provide free access to?', ['Books, information, and community programs', 'Only expensive rare items', 'Only private business services', 'Nothing of value'], 0),
    ('Who can typically use a public library?', ['People of all ages in the community', 'Only government officials', 'Only students in university', 'Only wealthy citizens'], 0),
    ('What is one benefit public libraries offer to a community?', ['Supporting learning and access to information for everyone', 'Restricting access to information', 'Charging high fees for every book', 'Providing no community services'], 0),
    ('What kind of programs might a public library offer besides lending books?', ['Reading clubs and educational workshops', 'Only paid entertainment events', 'Only private business meetings', 'No programs at all'], 0),
    ('Why are public libraries considered an important public institution?', ['They provide equal access to knowledge and resources for the community', 'They serve no real purpose in society', 'They only benefit one small group of people', 'They charge for every service they offer'], 0)]),
]),
day(149, [
L('Vocabulary: Understanding Euphemisms',
  'Grade 4 Language strand: a euphemism is a mild or indirect word or phrase used in place of one that might be considered harsh, unpleasant, or too direct.',
  [('What is a euphemism?', ['A mild or indirect word used in place of a harsher one', 'A type of punctuation mark', 'A word that means the exact same as its opposite', 'A grammar rule for verbs'], 0),
   ('Why might a writer use a euphemism?', ['To soften language about a sensitive or unpleasant topic', 'To make language more harsh and direct', 'Euphemisms are never used in writing', 'To confuse the reader on purpose'], 0),
   ('Which is an example of a euphemism for passed away?', ['Passed on', 'Died suddenly', 'Was killed instantly', 'Stopped breathing forever'], 0),
   ('What might using a euphemism accomplish in conversation?', ['Making a difficult topic feel gentler to discuss', 'Making a topic feel more harsh', 'Removing all meaning from a sentence', 'Confusing the listener with random words'], 0),
   ('In which situation might someone use a euphemism?', ['When discussing a sensitive topic politely', 'When writing a shopping list', 'When stating a simple math fact', 'When labelling a diagram'], 0)]),
M('Measurement: Perimeter of Composite Shapes',
  'Grade 4 Math strand: the perimeter of a composite shape, made up of two or more simple shapes joined together, is found by adding the lengths of all the outer sides.',
  [('What is a composite shape?', ['A shape made up of two or more simple shapes joined together', 'A shape with only one side', 'A shape that has no area', 'A shape found only in circles'], 0),
   ('How do you find the perimeter of a composite shape?', ['Add the lengths of all the outer sides', 'Multiply the length by the width only', 'Add only two of the sides', 'Find the area instead of the perimeter'], 0),
   ('If a composite shape has outer sides of 4, 3, 4, 2, 2, and 1 units, what is its perimeter?', ['16 units', '14 units', '12 units', '18 units'], 0),
   ('Why might you need to find a missing side length before calculating perimeter?', ['Some outer side lengths might not be labelled directly on the shape', 'All side lengths are always labelled', 'Perimeter never requires knowing every side', 'Missing sides do not affect perimeter'], 0),
   ('What is the difference between area and perimeter?', ['Perimeter measures the distance around a shape while area measures the space inside it', 'They both measure the exact same thing', 'Area measures only around a shape', 'Perimeter measures the space inside a shape'], 0)]),
Sc('Science: Weather — Air Pressure and Wind',
   'Grade 4 Science strand: differences in air pressure between areas cause wind, as air moves from areas of higher pressure to areas of lower pressure, and this movement plays a major role in weather patterns.',
   [('What causes wind to form?', ['Air moving from areas of higher pressure to lower pressure', 'Air staying perfectly still at all times', 'The Moon pulling air directly', 'Water evaporating instantly'], 0),
    ('What is air pressure?', ['The weight of air pressing down on the Earths surface', 'The temperature of the air only', 'The colour of the sky', 'The speed of falling rain'], 0),
    ('What tool is commonly used to measure air pressure?', ['A barometer', 'A thermometer', 'A rain gauge', 'A compass'], 0),
    ('How are wind and air pressure related to weather patterns?', ['Changes in air pressure and wind often signal changing weather', 'They have no connection to weather at all', 'Wind only occurs in outer space', 'Air pressure never changes on Earth'], 0),
    ('What generally happens to air as it moves from high pressure to low pressure areas?', ['It creates wind as it flows toward the lower pressure area', 'It disappears completely', 'It always creates snow', 'It stops moving immediately'], 0)]),
SS('Social Studies: World Heritage Sites in Canada',
   'Grade 4 Social Studies strand: World Heritage Sites are locations recognized by UNESCO for their cultural or natural significance, and Canada is home to several such sites, including national parks and historic landmarks.',
   [('What organization designates World Heritage Sites?', ['UNESCO', 'The United Nations Security Council', 'The Canadian Senate', 'The World Trade Organization'], 0),
    ('Why are World Heritage Sites recognized?', ['For their outstanding cultural or natural significance', 'For having no significance at all', 'For being the newest buildings in a country', 'For being entirely man-made shopping centres'], 0),
    ('What type of location in Canada might be designated a World Heritage Site?', ['A national park or historic landmark', 'A private shopping mall', 'A random empty field', 'A brand new parking lot'], 0),
    ('Why is it valuable for a country to have World Heritage Sites?', ['It highlights important natural or cultural treasures worth protecting', 'It has no value to a country', 'It means the site must be destroyed', 'It only benefits foreign visitors'], 0),
    ('What might visitors learn from exploring a World Heritage Site?', ['About important natural or cultural history', 'Nothing of educational value', 'Only about modern technology', 'Only about unrelated topics'], 0)]),
]),
day(150, [
L('Language Review: Sentence Craft, Character, and Media Texts',
  'Grade 4 Language strand review: students revisit parallel structure, character foils, public service announcements, jargon, and comparing texts on the same topic.',
  [('What is parallel structure in a sentence?', ['Using the same grammatical pattern for items in a series', 'Using a different verb tense for each item', 'Two unrelated topics', 'A title and a subtitle'], 0),
   ('What is a character foil?', ['A character whose traits contrast with another character to highlight qualities', 'A character who looks exactly like the main character', 'A character who never appears in the story', 'A type of punctuation mark'], 0),
   ('What is the purpose of a public service announcement?', ['To inform the public about an issue and encourage action', 'To tell a made-up bedtime story', 'To sell a specific brand of toy', 'To share a private diary entry'], 0),
   ('What is jargon?', ['Special vocabulary used by people in a particular field or group', 'A type of punctuation mark', 'A word with no meaning at all', 'A grammar rule for verbs'], 0),
   ('What does comparing two texts on the same topic involve?', ['Identifying similarities and differences between the texts', 'Reading only one of the texts', 'Ignoring the topic entirely', 'Copying one text exactly'], 0)]),
M('Math Review: Operations, Measurement, and Data',
  'Grade 4 Math strand review: students revisit dividing a fraction by a whole number, volume of triangular prisms, integers, stacked bar graphs, and rounding to the nearest ten thousand.',
  [('What happens to the denominator when dividing a fraction by a whole number?', ['The denominator is multiplied by the whole number', 'The denominator is divided by the whole number', 'The denominator stays exactly the same', 'The numerator disappears'], 0),
   ('What shape is the base of a triangular prism?', ['A triangle', 'A square', 'A circle', 'A pentagon'], 0),
   ('What are integers?', ['Positive numbers, negative numbers, and zero', 'Only positive numbers', 'Only fractions', 'Only decimals'], 0),
   ('What does a stacked bar graph show within a single bar?', ['Multiple categories stacked to show parts of a total', 'Only one category with no divisions', 'A single number with no comparison', 'Nothing measurable'], 0),
   ('What digit do you check when rounding to the nearest ten thousand?', ['The thousands digit', 'The ones digit', 'The hundred thousands digit', 'The tenths digit'], 0)]),
Sc('Science Review: Life Science, Earth and Space, and Physical Science',
   'Grade 4 Science strand review: students revisit photosynthesis, vertebrates and invertebrates, plant parts, magnetic fields, and the life cycle of a frog.',
   [('What is photosynthesis?', ['The process by which plants make their own food using sunlight', 'A process where plants absorb food from soil only', 'A process where plants produce no oxygen', 'A process that only happens at night'], 0),
    ('What is a vertebrate?', ['An animal that has a backbone', 'An animal that has no backbone', 'A type of plant', 'A type of rock'], 0),
    ('What is the main job of a plants roots?', ['Absorbing water and nutrients from the soil', 'Capturing sunlight for energy', 'Producing seeds', 'Releasing pollen only'], 0),
    ('What is a magnetic field?', ['An invisible area of force surrounding a magnet', 'A visible line drawn around a magnet', 'A type of electrical current', 'A type of sound wave'], 0),
    ('What is the first stage of a frogs life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'Froglet'], 0)]),
SS('Social Studies Review: Canadian History, Government, and World Geography',
   'Grade 4 Social Studies strand review: students revisit the Hudson Bay Company, taxes, Canadas national symbols, the Supreme Court of Canada, and the Fertile Crescent.',
   [('What kind of company was the Hudson Bay Company?', ['A major fur trading company', 'A modern technology company', 'An airline company', 'A film production company'], 0),
    ('What are taxes?', ['Money collected by governments to fund public services', 'Money given only to private businesses', 'A type of currency used only in stores', 'A voluntary gift with no purpose'], 0),
    ('Which animal is a well-known national symbol of Canada?', ['The beaver', 'The lion', 'The eagle', 'The kangaroo'], 0),
    ('What is the Supreme Court of Canada?', ['The highest court in the country', 'A local municipal office', 'A branch of the police force', 'A private business court'], 0),
    ('What is the Fertile Crescent known for?', ['Rich soil and water access that supported early farming', 'Being a completely dry desert with no water', 'Having no history of early civilizations', 'Being located entirely underwater'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_141_150)
    append_to(4, g4_141_150)
