#!/usr/bin/env python3
"""Grade 4, Days 151-160 -- extends Grade 4 from 150 to 160 days. Modeled
exactly on gen_grade4_days141_150.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-150
topics (verified against data/grade4.json, which already densely covers
nearly the entire grade 4 curriculum, including the immediately prior
Days 141-150 batch). New topics: articles (a, an, the), understanding plot
structure (rising action, climax, falling action), writing a character
sketch, indirect objects, common suffixes and their meanings, identifying
the protagonist and antagonist, writing a travel brochure, demonstrative
pronouns, and writing a riddle or joke for Language; dividing by 10, 100,
and 1,000, the circumference of a circle, simplifying fractions to lowest
terms, converting between units of time, an introduction to scatter
plots, reading and writing numbers to 100,000, rounding to the nearest
hundred thousand, comparing theoretical and experimental probability, and
diameter and radius of a circle for Math; the life cycle of a butterfly,
deciduous and coniferous trees, the difference between weather and
climate, the layers of the atmosphere, herbivores carnivores and
omnivores, the human life cycle, glaciers, composting and decomposition,
and echoes for Science; and ancient Carthage and the Phoenician traders,
Niagara Falls, the Trans-Canada Highway, provincial and territorial
flags, the role of school boards in Ontario, the CN Tower, ancient
Babylon and the Code of Hammurabi, Canadas national historic sites, and
the role of Canadian embassies abroad for Social Studies -- none of those
exact ideas appear in Days 1-150. Day 160 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior 10-day
batch (one representative question drawn from each of the first five
lessons of the batch, per subject, exactly as Day 150 did for Days
141-145). The four Day 160 review titles (Language Review: Grammar
Basics, Story Structure, and Word Parts / Math Review: Circles,
Fractions, and Time / Science Review: Life Cycles, Trees, and Weather
Systems / Social Studies Review: Ancient Trade, Canadian Landmarks, and
Local Government) were checked against every earlier review-day title in
Days 1-150, including Day 140, Day 150, and every "Review: ... (Days
X-Y)" day, and are textually distinct from all of them. No embedded ASCII
double-quote or apostrophe characters are used anywhere in title/summary/
question/option text, matching the convention used in
gen_grade4_days141_150.py (apostrophes dropped entirely, e.g. "Canadas"
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


def _rebalance_answer_positions(days, seed=20260817):
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


g4_151_160 = [
day(151, [
L('Grammar: Articles — A, An, and The',
  'Grade 4 Language strand: articles are small words used before nouns, where a and an are indefinite articles used with nonspecific nouns, while the is a definite article used with a specific noun, and an is used before words that begin with a vowel sound.',
  [('What is the definite article in English?', ['The', 'A', 'An', 'But'], 0),
   ('Which article is indefinite and used before consonant sounds?', ['A', 'An', 'The', 'So'], 0),
   ('Which article is indefinite and used before vowel sounds?', ['An', 'A', 'The', 'Or'], 0),
   ('Which sentence uses the correct article?', ['She ate an apple for lunch.', 'She ate a apple for lunch.', 'She ate an the apple for lunch.', 'She eat an apple for lunch.'], 0),
   ('Why do writers use the article the before a noun?', ['To show the noun is specific and already known', 'To show the noun is one of many unknown things', 'Articles have no purpose in a sentence', 'To turn a noun into a verb'], 0)]),
M('Number Sense: Dividing by 10, 100, and 1,000',
  'Grade 4 Math strand: dividing a whole number by 10, 100, or 1,000 moves the digits to the right, shifting the decimal point left by one, two, or three places.',
  [('What happens to a number when it is divided by 10?', ['The decimal point moves one place to the left', 'The decimal point moves one place to the right', 'The number is multiplied by 10', 'The number stays exactly the same'], 0),
   ('What is 4,500 divided by 10?', ['450', '45', '4500', '40500'], 0),
   ('What is 4,500 divided by 100?', ['45', '450', '4.5', '45000'], 0),
   ('What is 6,000 divided by 1,000?', ['6', '60', '600', '0.6'], 0),
   ('Why is it useful to know how to divide by 10, 100, and 1,000 quickly?', ['It makes mental math with place value faster and easier', 'It has no real use in math', 'Division rules change for every number', 'It only works with negative numbers'], 0)]),
Sc('Science: The Life Cycle of a Butterfly — Complete Metamorphosis in Detail',
   'Grade 4 Science strand: a butterfly undergoes complete metamorphosis, changing from an egg to a larva called a caterpillar, then to a pupa inside a chrysalis, before emerging as an adult butterfly.',
   [('What is the first stage of a butterflys life cycle?', ['Egg', 'Caterpillar', 'Chrysalis', 'Adult butterfly'], 0),
    ('What is a caterpillar also known as in the butterfly life cycle?', ['A larva', 'A pupa', 'An egg', 'An adult'], 0),
    ('What is the chrysalis stage also called?', ['The pupa stage', 'The larva stage', 'The egg stage', 'The adult stage'], 0),
    ('What term describes the dramatic change from caterpillar to butterfly?', ['Complete metamorphosis', 'Photosynthesis', 'Hibernation', 'Pollination'], 0),
    ('What emerges from the chrysalis at the end of the life cycle?', ['An adult butterfly', 'A new caterpillar', 'A new egg', 'A moth only'], 0)]),
SS('Social Studies: Ancient Carthage and the Phoenician Traders',
   'Grade 4 Social Studies strand: ancient Carthage was a powerful trading city founded by the Phoenicians, known for its skilled sailors, extensive trade routes, and influence across the Mediterranean Sea.',
   [('Who founded the ancient city of Carthage?', ['The Phoenicians', 'The Romans', 'The Egyptians', 'The Greeks'], 0),
    ('What were the Phoenicians especially well known for?', ['Being skilled sailors and traders', 'Building pyramids', 'Farming rice', 'Mining coal'], 0),
    ('Where was ancient Carthage located?', ['On the coast of the Mediterranean Sea', 'In the middle of a large desert with no water access', 'On a small island in the Pacific Ocean', 'In the mountains far from any coastline'], 0),
    ('Why was trade important to the city of Carthage?', ['It helped Carthage grow wealthy and powerful through Mediterranean trade routes', 'Carthage refused to trade with any other cities', 'Trade had no effect on Carthages growth', 'Carthage only relied on farming for its economy'], 0),
    ('Why do historians still study ancient Carthage today?', ['It reveals how trade and seafaring shaped ancient Mediterranean societies', 'Carthage has no historical importance', 'Carthage was never involved in trade', 'Carthage was located far from any trade routes'], 0)]),
]),
day(152, [
L('Reading: Understanding Plot Structure — Rising Action, Climax, and Falling Action',
  'Grade 4 Language strand: plot structure includes rising action, where tension builds, the climax, the most exciting turning point, and falling action, where events lead toward the resolution.',
  [('What happens during the rising action of a story?', ['Tension and events build toward the most exciting moment', 'The story ends completely', 'Characters are introduced for the first time', 'Nothing happens in the plot'], 0),
   ('What is the climax of a story?', ['The most exciting turning point in the plot', 'The very first sentence of the story', 'The list of characters', 'The title of the book'], 0),
   ('What happens during the falling action?', ['Events move toward the resolution after the climax', 'The story is just beginning', 'The main problem is first introduced', 'Characters are named for the first time'], 0),
   ('Which part of the plot usually contains the biggest conflict?', ['The climax', 'The falling action', 'The resolution', 'The title'], 0),
   ('Why is understanding plot structure useful for readers?', ['It helps readers see how a story builds and resolves tension', 'Plot structure has no effect on understanding a story', 'Every story has the exact same events', 'Plot structure only applies to poems'], 0)]),
M('Geometry: Finding the Circumference of a Circle (Introduction)',
  'Grade 4 Math strand: the circumference of a circle is the distance around its outer edge, and students explore how it relates to the circles diameter as an introduction to measuring circles.',
  [('What is the circumference of a circle?', ['The distance around the outer edge of the circle', 'The distance across the middle of the circle', 'The area inside the circle', 'The number of sides a circle has'], 0),
   ('What part of a circle stretches from one side to the other through the centre?', ['The diameter', 'The circumference', 'The radius only', 'The arc'], 0),
   ('If you wrapped a string around a circular plate, what would you be measuring?', ['The circumference', 'The area', 'The radius', 'The diameter'], 0),
   ('Why might someone need to know the circumference of a circle?', ['To measure the distance around circular objects like wheels or plates', 'Circumference has no real world use', 'To find how much space is inside a square', 'To count the number of sides on a shape'], 0),
   ('Which shape has a circumference instead of a perimeter made of straight sides?', ['A circle', 'A square', 'A triangle', 'A rectangle'], 0)]),
Sc('Science: Deciduous and Coniferous Trees — Comparing Two Types of Forests',
   'Grade 4 Science strand: deciduous trees have broad leaves that change colour and drop in autumn, while coniferous trees have needle-like leaves and cones and generally stay green throughout the year.',
   [('What kind of leaves do deciduous trees typically have?', ['Broad leaves that change colour and drop in autumn', 'Needle-like leaves that never fall', 'No leaves at all', 'Only flowers instead of leaves'], 0),
    ('What kind of leaves do coniferous trees typically have?', ['Needle-like leaves', 'Broad flat leaves', 'No leaves at all', 'Only petals'], 0),
    ('What do coniferous trees produce to hold their seeds?', ['Cones', 'Flowers only', 'Fruit only', 'Bulbs'], 0),
    ('Which type of tree usually stays green throughout the year?', ['Coniferous trees', 'Deciduous trees', 'Neither type of tree', 'Both types lose all their leaves'], 0),
    ('Why do deciduous trees drop their leaves in autumn?', ['To conserve water and energy during colder months', 'To attract more sunlight in winter', 'Leaves fall only during summer', 'Trees never lose their leaves'], 0)]),
SS('Social Studies: Niagara Falls — Geography and Importance to Canada',
   'Grade 4 Social Studies strand: Niagara Falls is a group of powerful waterfalls on the border between Canada and the United States, important for tourism, hydroelectric power, and Ontarios geography.',
   [('Niagara Falls is located on the border between Canada and which country?', ['The United States', 'Mexico', 'France', 'Brazil'], 0),
    ('What is Niagara Falls an example of?', ['A powerful group of waterfalls', 'A tall mountain range', 'A large desert', 'A deep underground cave'], 0),
    ('What is one important use of the water power at Niagara Falls?', ['Generating hydroelectric power', 'Growing desert crops', 'Mining coal', 'Producing salt'], 0),
    ('Why do millions of visitors travel to see Niagara Falls each year?', ['It is a famous and powerful natural landmark', 'It has no scenic value', 'It is located far from any accessible roads', 'It is a small quiet stream'], 0),
    ('Which Canadian province is home to Niagara Falls?', ['Ontario', 'British Columbia', 'Manitoba', 'Nova Scotia'], 0)]),
]),
day(153, [
L('Writing: Writing a Character Sketch',
  'Grade 4 Language strand: a character sketch is a short piece of writing that describes a characters appearance, personality, and behaviour to help readers picture and understand them.',
  [('What is the purpose of a character sketch?', ['To describe a characters appearance, personality, and behaviour', 'To list random unrelated facts', 'To describe only a setting', 'To summarize an entire plot with no character details'], 0),
   ('Which detail would likely appear in a character sketch?', ['A description of the characters personality traits', 'A list of unrelated math problems', 'The publication date of a magazine', 'A recipe for a meal'], 0),
   ('Why might a writer include a characters actions in a character sketch?', ['Actions can reveal personality traits without stating them directly', 'Actions have no connection to personality', 'Character sketches never include actions', 'Actions are only used in poetry'], 0),
   ('What might a character sketch describe about physical appearance?', ['Details like hair colour, height, or clothing', 'Only the characters favourite food', 'Only the weather in the story', 'Only the title of the book'], 0),
   ('Why is a strong character sketch useful to readers?', ['It helps readers picture and understand a character more clearly', 'It confuses readers on purpose', 'It removes all detail from a story', 'It only describes the setting'], 0)]),
M('Fractions: Simplifying Fractions to Lowest Terms',
  'Grade 4 Math strand: simplifying a fraction to lowest terms means dividing the numerator and denominator by their greatest common factor so the fraction cannot be reduced any further.',
  [('What does it mean to simplify a fraction to lowest terms?', ['Dividing the numerator and denominator by their greatest common factor', 'Multiplying the numerator and denominator by two', 'Adding one to the numerator only', 'Changing the fraction into a whole number'], 0),
   ('What is 4/8 simplified to lowest terms?', ['1/2', '2/4', '4/8', '1/4'], 0),
   ('What is 6/9 simplified to lowest terms?', ['2/3', '3/6', '6/9', '1/3'], 0),
   ('What is 10/20 simplified to lowest terms?', ['1/2', '2/10', '5/10', '10/1'], 0),
   ('Why might it be useful to simplify a fraction?', ['It makes the fraction easier to read, compare, and work with', 'Simplifying always changes the fractions value', 'Fractions cannot be simplified', 'Simplifying makes a fraction larger'], 0)]),
Sc('Science: The Difference Between Weather and Climate',
   'Grade 4 Science strand: weather describes short-term conditions in the atmosphere on a given day, while climate describes the typical weather patterns of a region over many years.',
   [('What does weather describe?', ['Short-term atmospheric conditions on a given day', 'The average conditions of a region over many years', 'Only the temperature of the ocean', 'Only the phases of the moon'], 0),
    ('What does climate describe?', ['The typical weather patterns of a region over many years', 'The weather happening right now outside', 'A single days temperature only', 'The colour of the sky at sunset'], 0),
    ('Which is an example of weather rather than climate?', ['It is raining outside today', 'This region usually has cold winters and mild summers', 'This area is generally a desert climate', 'This region typically receives heavy snowfall each year'], 0),
    ('Which is an example of climate rather than weather?', ['This region typically has hot, dry summers every year', 'It is sunny outside right now', 'There was a thunderstorm this afternoon', 'Today feels colder than yesterday'], 0),
    ('Why is it useful to understand the difference between weather and climate?', ['It helps us describe short-term conditions versus long-term patterns accurately', 'Weather and climate always mean the exact same thing', 'Climate changes every single hour', 'Weather never changes from day to day'], 0)]),
SS('Social Studies: The Trans-Canada Highway — Connecting the Country by Road',
   'Grade 4 Social Studies strand: the Trans-Canada Highway is a major road system that stretches across the country, connecting communities in every province and supporting travel and trade.',
   [('What is the Trans-Canada Highway?', ['A major road system connecting communities across the country', 'A railway line used only for cargo', 'A walking trail through one city', 'A canal used for shipping goods'], 0),
    ('How many provinces does the Trans-Canada Highway pass through?', ['Every province in Canada', 'Only one province', 'Only two provinces', 'No provinces at all'], 0),
    ('What is one benefit of the Trans-Canada Highway for communities?', ['It supports travel and trade between distant communities', 'It prevents any travel between provinces', 'It only connects cities in the same province', 'It has no effect on trade'], 0),
    ('Why might the Trans-Canada Highway be considered an important piece of infrastructure?', ['It helps connect people, goods, and communities across a vast country', 'It has no importance to Canadian communities', 'It only exists in one small town', 'It replaces the need for any other roads'], 0),
    ('What might travellers use the Trans-Canada Highway for?', ['Driving long distances between provinces', 'Traveling only by boat', 'Flying between cities', 'Walking short distances within one neighbourhood'], 0)]),
]),
day(154, [
L('Grammar: Indirect Objects',
  'Grade 4 Language strand: an indirect object receives the direct object of a sentence, usually telling to whom or for whom an action is done, such as her in the sentence I gave her a gift.',
  [('What does an indirect object usually tell us?', ['To whom or for whom an action is done', 'The subject performing the action', 'The main verb in a sentence', 'The setting of a story'], 0),
   ('In the sentence I gave her a gift, what is the indirect object?', ['Her', 'Gift', 'Gave', 'I'], 0),
   ('In the sentence Mom baked us cookies, what is the indirect object?', ['Us', 'Cookies', 'Baked', 'Mom'], 0),
   ('Which sentence contains an indirect object?', ['She sent him a letter.', 'She sent a letter.', 'The letter was sent.', 'She wrote quickly.'], 0),
   ('Why is it useful to recognize indirect objects in a sentence?', ['It helps show who receives the action along with the direct object', 'Indirect objects have no function in a sentence', 'Every sentence must contain an indirect object', 'Indirect objects replace the subject of a sentence'], 0)]),
M('Measurement: Converting Between Units of Time',
  'Grade 4 Math strand: converting between units of time involves knowing that 60 seconds make a minute, 60 minutes make an hour, and 24 hours make a day, to move between smaller and larger units.',
  [('How many seconds are in one minute?', ['60', '100', '30', '24'], 0),
   ('How many minutes are in one hour?', ['60', '24', '100', '12'], 0),
   ('How many hours are in one day?', ['24', '60', '12', '100'], 0),
   ('How many minutes are in 2 hours?', ['120', '60', '100', '24'], 0),
   ('Why is it useful to convert between units of time?', ['It helps compare and calculate durations given in different units', 'Units of time can never be converted', 'Time only exists in seconds', 'Converting time has no real-life use'], 0)]),
Sc('Science: The Layers of the Atmosphere',
   'Grade 4 Science strand: Earths atmosphere is made up of layers, including the troposphere closest to the ground where weather occurs, and higher layers that protect the planet and thin out into space.',
   [('Which layer of the atmosphere is closest to the ground?', ['The troposphere', 'The exosphere', 'The thermosphere', 'The mesosphere'], 0),
    ('Where does most of Earths weather occur?', ['In the troposphere', 'In outer space', 'In the deepest ocean', 'Underground'], 0),
    ('What generally happens to air as you move through higher layers of the atmosphere?', ['It becomes thinner and less dense', 'It becomes thicker and heavier', 'It disappears completely at ground level', 'It turns into solid rock'], 0),
    ('Why is the atmosphere important for life on Earth?', ['It provides air to breathe and helps protect the planet', 'It has no effect on life on Earth', 'It blocks all sunlight completely', 'It removes all oxygen from the planet'], 0),
    ('What eventually happens to the atmosphere at its outer edge?', ['It gradually thins out into space', 'It suddenly stops with a solid wall', 'It turns into water', 'It becomes part of the ocean'], 0)]),
SS('Social Studies: Provincial and Territorial Flags of Canada',
   'Grade 4 Social Studies strand: each Canadian province and territory has its own flag, featuring unique colours, symbols, and designs that represent its history, geography, and identity.',
   [('What does each Canadian province and territory have of its own?', ['A unique flag', 'No flag at all', 'The exact same flag as every other province', 'Only a national flag'], 0),
    ('What might a provincial flag represent?', ['The regions history, geography, and identity', 'Nothing meaningful at all', 'Only the name of the capital city', 'A foreign countrys history'], 0),
    ('Why might provincial flags differ from one another?', ['Each region has its own unique symbols and history to represent', 'All provinces share identical histories', 'Flags are chosen randomly with no meaning', 'Provinces are not allowed to have their own flags'], 0),
    ('Where might you see a provincial or territorial flag displayed?', ['At government buildings within that province or territory', 'Only in other countries', 'Nowhere within Canada', 'Only inside private homes'], 0),
    ('Why is it valuable to learn about the symbols on provincial flags?', ['It helps us understand the unique identity of each region', 'Provincial flags have no connection to regional identity', 'All flags contain the exact same symbols', 'Learning about flags has no educational value'], 0)]),
]),
day(155, [
L('Vocabulary: Common Suffixes and Their Meanings',
  'Grade 4 Language strand: suffixes are word parts added to the end of a base word that change its meaning or part of speech, such as -tion, -ment, and -able.',
  [('What is a suffix?', ['A word part added to the end of a base word', 'A word part added to the beginning of a base word', 'A punctuation mark', 'A type of sentence'], 0),
   ('What does the suffix -able often mean?', ['Capable of or able to be', 'Never able to happen', 'Always in the past', 'A type of number'], 0),
   ('Adding -tion to a verb often changes it into what part of speech?', ['A noun', 'A verb', 'An adjective', 'A preposition'], 0),
   ('What does the word enjoyment mean, based on the suffix -ment?', ['The state or action of enjoying something', 'The opposite of enjoying something', 'A type of vegetable', 'A verb meaning to run'], 0),
   ('Why is it helpful to learn common suffixes?', ['It helps figure out the meaning of unfamiliar words', 'Suffixes never change a words meaning', 'Suffixes only appear in math vocabulary', 'Suffixes make words impossible to understand'], 0)]),
M('Data Management: Introduction to Scatter Plots',
  'Grade 4 Math strand: a scatter plot uses points on a grid to show the relationship between two sets of data, helping students see patterns or trends between the values.',
  [('What does a scatter plot use to display data?', ['Points plotted on a grid', 'Bars of different heights', 'Slices of a circle', 'Lines connecting single values only'], 0),
   ('What can a scatter plot help you see between two sets of data?', ['A pattern or trend between the values', 'The exact colour of each data point', 'The title of the graph only', 'Nothing meaningful about the data'], 0),
   ('If points on a scatter plot generally rise from left to right, what might this suggest?', ['A positive relationship between the two sets of data', 'No relationship at all', 'A relationship that cannot be shown visually', 'That the data must be incorrect'], 0),
   ('What are the two axes of a scatter plot used to represent?', ['Two different sets of data being compared', 'Only one type of data repeated twice', 'Nothing measurable', 'Only categories with no numbers'], 0),
   ('Why might scientists or researchers use scatter plots?', ['To visually explore relationships between two variables', 'Scatter plots have no practical use', 'To hide patterns in data', 'To avoid comparing information'], 0)]),
Sc('Science: Herbivores, Carnivores, and Omnivores — Animal Diets',
   'Grade 4 Science strand: animals can be classified by diet as herbivores, which eat only plants, carnivores, which eat only other animals, and omnivores, which eat both plants and animals.',
   [('What does a herbivore eat?', ['Only plants', 'Only other animals', 'Both plants and animals', 'Nothing at all'], 0),
    ('What does a carnivore eat?', ['Only other animals', 'Only plants', 'Both plants and animals', 'Only insects and nothing else'], 0),
    ('What does an omnivore eat?', ['Both plants and animals', 'Only plants', 'Only meat', 'Neither plants nor animals'], 0),
    ('Which of these animals is typically classified as a herbivore?', ['A deer', 'A lion', 'A wolf', 'A shark'], 0),
    ('Why do scientists classify animals by their diet?', ['It helps explain an animals role in its ecosystem', 'Diet has no connection to an animals role in nature', 'All animals eat exactly the same food', 'Classification by diet is not useful in science'], 0)]),
SS('Social Studies: The Role of School Boards in Ontario',
   'Grade 4 Social Studies strand: a school board is a local governing body responsible for managing public schools in a region, making decisions about programs, staffing, and resources for students.',
   [('What is a school board responsible for?', ['Managing public schools in a region', 'Running a countrys military', 'Managing national parks', 'Building highways across Canada'], 0),
    ('What might a school board make decisions about?', ['Programs, staffing, and resources for students', 'Only decisions about foreign trade', 'Only decisions about provincial parks', 'Only decisions about highways'], 0),
    ('What kind of area does an Ontario school board usually oversee?', ['A local region with several schools', 'The entire country', 'Every province in Canada', 'Only one classroom'], 0),
    ('Why might communities have their own local school boards?', ['To make decisions suited to the needs of local students and schools', 'School boards have no real purpose', 'Every school board makes identical decisions everywhere', 'Local input has no value for schools'], 0),
    ('Who might work with a school board to support students?', ['Teachers, principals, and school staff', 'Only foreign diplomats', 'Only airline pilots', 'Only professional athletes'], 0)]),
]),
day(156, [
L('Reading: Identifying the Protagonist and Antagonist',
  'Grade 4 Language strand: the protagonist is the main character a story follows, while the antagonist is the character or force that creates conflict and opposes the protagonist.',
  [('Who is the protagonist of a story?', ['The main character the story follows', 'The character who never appears', 'The setting of the story', 'The title of the book'], 0),
   ('Who or what is the antagonist of a story?', ['The character or force that opposes the protagonist', 'The narrator only', 'The author of the book', 'A minor unimportant character'], 0),
   ('Why might a story include an antagonist?', ['To create conflict that challenges the protagonist', 'To remove all tension from the plot', 'Antagonists are never included in stories', 'To confuse readers with no purpose'], 0),
   ('Can an antagonist be something other than a person?', ['Yes, it can be a force like nature or society', 'No, an antagonist must always be a person', 'No, an antagonist must always be an animal', 'No, a story cannot have an antagonist'], 0),
   ('Why is identifying the protagonist and antagonist useful when reading?', ['It helps readers understand the central conflict of the story', 'It has no effect on understanding a story', 'Every story has the exact same protagonist', 'Protagonists and antagonists are always the same character'], 0)]),
M('Number Sense: Reading and Writing Numbers to 100,000',
  'Grade 4 Math strand: reading and writing numbers to 100,000 involves understanding place value positions including ten thousands and hundred thousands, and expressing numbers in standard and word form.',
  [('What is the value of the digit 3 in the number 63,000?', ['3 thousands', '3 hundreds', '3 tens', '3 ones'], 0),
   ('How do you write the number 45,290 in words?', ['Forty-five thousand, two hundred ninety', 'Four thousand, five hundred twenty-nine', 'Forty-five hundred and twenty-nine', 'Four hundred fifty-two thousand ninety'], 0),
   ('What is one hundred thousand written as a numeral?', ['100,000', '10,000', '1,000,000', '1,000'], 0),
   ('Which number is greater, 78,450 or 78,045?', ['78,450', '78,045', 'They are equal', 'Cannot be compared'], 0),
   ('Why is understanding place value important when reading large numbers?', ['It helps determine the value of each digit based on its position', 'Place value has no effect on a numbers value', 'All digits always represent the same value', 'Large numbers cannot be broken down by place value'], 0)]),
Sc('Science: The Human Life Cycle — From Infancy to Adulthood',
   'Grade 4 Science strand: humans go through stages of a life cycle including infancy, childhood, adolescence, and adulthood, each marked by physical growth and development.',
   [('What is the first stage of the human life cycle?', ['Infancy', 'Childhood', 'Adolescence', 'Adulthood'], 0),
    ('What stage comes after childhood in the human life cycle?', ['Adolescence', 'Infancy', 'Old age only', 'Birth'], 0),
    ('What generally happens to the human body during each stage of the life cycle?', ['It grows and develops in different ways', 'It stays exactly the same at every stage', 'It shrinks continuously from birth', 'Growth only happens during infancy'], 0),
    ('Which stage of life is generally associated with becoming fully grown?', ['Adulthood', 'Infancy', 'Early childhood', 'Birth'], 0),
    ('Why do scientists study the stages of the human life cycle?', ['To understand how humans grow, develop, and change over time', 'Life cycle stages have no scientific value', 'Humans do not go through any stages of growth', 'Every stage of life looks exactly the same'], 0)]),
SS('Social Studies: The CN Tower — A Canadian Landmark',
   'Grade 4 Social Studies strand: the CN Tower is a tall communications and observation tower in Toronto, recognized as an important Canadian landmark and a symbol of the citys skyline.',
   [('In which city is the CN Tower located?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 0),
    ('What was the CN Tower originally built to support?', ['Communications and broadcasting', 'Farming operations', 'Shipping across the ocean', 'Mining operations'], 0),
    ('What is the CN Tower recognized as today?', ['An important Canadian landmark and tourist attraction', 'A structure with no significance', 'A small residential building', 'A type of bridge'], 0),
    ('What can visitors do at the CN Tower?', ['View the city from an observation deck', 'Go swimming in an underground pool', 'Visit a working farm', 'Ride a roller coaster only'], 0),
    ('Why might the CN Tower be considered a symbol of Toronto?', ['It is a recognizable and iconic structure on the citys skyline', 'It has no connection to Toronto', 'It is located outside of Canada', 'It is a symbol of a completely different city'], 0)]),
]),
day(157, [
L('Grammar: Demonstrative Pronouns — This, That, These, Those',
  'Grade 4 Language strand: demonstrative pronouns, including this, that, these, and those, point to specific people, places, or things, showing whether they are near or far and singular or plural.',
  [('Which word is a demonstrative pronoun used for something singular and nearby?', ['This', 'These', 'Those', 'Who'], 0),
   ('Which word is a demonstrative pronoun used for something plural and nearby?', ['These', 'This', 'That', 'Which'], 0),
   ('Which word is a demonstrative pronoun used for something singular and farther away?', ['That', 'This', 'These', 'Those'], 0),
   ('Which word is a demonstrative pronoun used for something plural and farther away?', ['Those', 'That', 'This', 'These'], 0),
   ('What do demonstrative pronouns generally show?', ['Whether something is near or far and singular or plural', 'The tense of a verb', 'The subject of a question', 'A type of punctuation'], 0)]),
M('Number Sense: Rounding to the Nearest Hundred Thousand',
  'Grade 4 Math strand: to round a number to the nearest hundred thousand, students look at the ten thousands digit to decide whether to round up or keep the hundred thousands digit the same.',
  [('What digit do you check when rounding to the nearest hundred thousand?', ['The ten thousands digit', 'The ones digit', 'The hundreds digit', 'The tenths digit'], 0),
   ('What is 340,000 rounded to the nearest hundred thousand?', ['300,000', '400,000', '340,000', '350,000'], 0),
   ('What is 762,000 rounded to the nearest hundred thousand?', ['800,000', '700,000', '762,000', '760,000'], 0),
   ('If the ten thousands digit is 5 or greater, what should you do when rounding to the nearest hundred thousand?', ['Round the hundred thousands digit up by one', 'Keep the hundred thousands digit the same', 'Round down to zero', 'Ignore the digit completely'], 0),
   ('Why might someone round a very large number to the nearest hundred thousand?', ['To make the number easier to estimate or compare', 'Rounding removes the need for all math', 'Rounding only works with small numbers', 'To make the number less useful'], 0)]),
Sc('Science: Glaciers — How Ice Shapes the Land',
   'Grade 4 Science strand: glaciers are massive slow-moving bodies of ice that shape the land over time by carving valleys, moving rocks and soil, and leaving distinct landforms behind as they melt or retreat.',
   [('What is a glacier?', ['A massive slow-moving body of ice', 'A fast-moving river of water', 'A type of ocean current', 'A small puddle of melted snow'], 0),
    ('How do glaciers generally move?', ['Slowly, over a long period of time', 'Instantly, in a single moment', 'Only sideways in a straight line', 'They never move at all'], 0),
    ('What can a glacier do to the land as it moves?', ['Carve valleys and move rocks and soil', 'Have no effect on the land at all', 'Only create new oceans', 'Instantly disappear without changing anything'], 0),
    ('What might be left behind after a glacier melts or retreats?', ['Distinct landforms shaped by the ice', 'No trace of any kind', 'Only new glaciers immediately forming', 'Lava flows'], 0),
    ('Why do scientists study glaciers today?', ['To understand how they shape landscapes and respond to climate change', 'Glaciers have no scientific importance', 'Glaciers do not exist anywhere on Earth', 'Glaciers never change over time'], 0)]),
SS('Social Studies: Ancient Babylon and the Code of Hammurabi',
   'Grade 4 Social Studies strand: ancient Babylon was a powerful city in Mesopotamia, known for the Code of Hammurabi, one of the earliest known sets of written laws that governed behaviour in society.',
   [('What ancient region was the city of Babylon located in?', ['Mesopotamia', 'Ancient Egypt', 'Ancient Greece', 'Ancient Rome'], 0),
    ('What is the Code of Hammurabi?', ['One of the earliest known sets of written laws', 'A type of ancient currency', 'A religious ceremony', 'A famous ancient painting'], 0),
    ('Why was the Code of Hammurabi important to Babylonian society?', ['It helped establish rules that governed behaviour in society', 'It had no effect on daily life', 'It banned all forms of trade', 'It only applied to farming activities'], 0),
    ('What material were early written laws like the Code of Hammurabi often carved into?', ['Stone', 'Paper', 'Plastic', 'Glass'], 0),
    ('Why do historians consider the Code of Hammurabi historically significant?', ['It is one of the earliest examples of a written legal system', 'It has no connection to the history of law', 'It was created in modern times', 'It was never actually used by anyone'], 0)]),
]),
day(158, [
L('Writing: Writing a Travel Brochure',
  'Grade 4 Language strand: a travel brochure is a persuasive informational text that describes a destination using engaging descriptions, facts, and images to encourage people to visit.',
  [('What is the purpose of a travel brochure?', ['To describe a destination and encourage people to visit', 'To share a private diary entry', 'To list unrelated math problems', 'To describe a fictional dragon'], 0),
   ('What might a travel brochure include to attract visitors?', ['Engaging descriptions and interesting facts about a place', 'Only blank pages with no text', 'Random unrelated numbers', 'A single word with no explanation'], 0),
   ('Why might a travel brochure include images?', ['To visually show visitors what the destination looks like', 'Images have no purpose in a brochure', 'Brochures are not allowed to include pictures', 'Images always confuse the reader'], 0),
   ('What tone would likely be used in a travel brochure?', ['Positive and inviting', 'Negative and discouraging', 'Angry and confusing', 'Completely neutral with no persuasive language'], 0),
   ('Which detail would likely appear in a travel brochure about a national park?', ['Popular trails and interesting wildlife to see', 'A list of unrelated math formulas', 'A private letter to a friend', 'An unrelated recipe'], 0)]),
M('Probability: Comparing Theoretical and Experimental Probability',
  'Grade 4 Math strand: theoretical probability predicts outcomes based on possible results, while experimental probability is based on the actual results of repeated trials, and the two can be compared.',
  [('What is theoretical probability based on?', ['The possible outcomes that could happen', 'The actual results of trials already conducted', 'Random guessing with no calculation', 'Only outcomes that have already occurred'], 0),
   ('What is experimental probability based on?', ['The actual results of trials that have been carried out', 'Only outcomes that could theoretically happen', 'A prediction made without any testing', 'Guessing without any data'], 0),
   ('If you flip a coin, what is the theoretical probability of landing on heads?', ['1/2', '1/4', '1', '0'], 0),
   ('If you flip a coin 10 times and get heads 7 times, what is the experimental probability of heads?', ['7/10', '1/2', '3/10', '10/7'], 0),
   ('Why might experimental probability differ from theoretical probability?', ['Real trials can vary due to chance even when outcomes are equally likely', 'They are always exactly identical in every situation', 'Experimental probability is always incorrect', 'Theoretical probability changes with every trial'], 0)]),
Sc('Science: Composting and Decomposition — Natures Recycling System',
   'Grade 4 Science strand: composting is a natural process where decomposers such as bacteria, fungi, and worms break down organic waste into nutrient-rich soil that can support new plant growth.',
   [('What is composting?', ['A natural process that breaks down organic waste into nutrient-rich soil', 'A process that creates plastic from waste', 'A process that removes all soil nutrients', 'A process that only happens underwater'], 0),
    ('Which of these might help break down organic material during composting?', ['Bacteria, fungi, and worms', 'Only rocks and sand', 'Only metal and glass', 'Only plastic materials'], 0),
    ('What can composted material be used for?', ['Supporting new plant growth as nutrient-rich soil', 'Powering electrical devices', 'Building bridges', 'Making glass'], 0),
    ('Why is composting considered good for the environment?', ['It reduces waste and recycles nutrients back into the soil', 'It increases the amount of waste sent to landfills', 'It has no environmental benefit', 'It destroys nutrients permanently'], 0),
    ('Which of these items would be appropriate to add to a compost pile?', ['Vegetable scraps and fruit peels', 'Plastic bottles', 'Metal cans', 'Glass jars'], 0)]),
SS('Social Studies: Canadas National Historic Sites',
   'Grade 4 Social Studies strand: national historic sites are locations across Canada recognized for their importance to the countrys history, preserving buildings, events, and stories for future generations.',
   [('What is a national historic site?', ['A location recognized for its importance to Canadas history', 'A brand new shopping centre', 'A location with no historical connection', 'A private business with no public access'], 0),
    ('Why are national historic sites preserved?', ['To protect important buildings, events, and stories for future generations', 'They are not preserved at all', 'They have no value to Canadian history', 'They are meant to be destroyed over time'], 0),
    ('Who might designate a location as a national historic site in Canada?', ['The Canadian government, through organizations like Parks Canada', 'A private individual with no authority', 'A foreign government', 'No one has this authority'], 0),
    ('What might visitors learn by exploring a national historic site?', ['Important stories and events from Canadas past', 'Nothing of educational value', 'Only modern technology', 'Unrelated foreign history'], 0),
    ('Why is it valuable for a country to preserve national historic sites?', ['It helps connect people with their shared history and heritage', 'Preserving history has no value', 'It prevents anyone from learning about the past', 'It focuses only on the future with no connection to history'], 0)]),
]),
day(159, [
L('Writing: Writing a Riddle or Joke',
  'Grade 4 Language strand: writing a riddle or joke uses wordplay, clever clues, and often a surprising twist or pun to entertain an audience and challenge them to guess an answer.',
  [('What is a common feature of a riddle?', ['Clever clues that lead to a surprising answer', 'A long list of unrelated facts', 'A formal letter format', 'A detailed scientific explanation'], 0),
   ('What technique do many jokes use to create humour?', ['Wordplay or a surprising twist', 'Long complicated sentences', 'Only serious factual statements', 'Random unrelated numbers'], 0),
   ('What is a pun?', ['A play on words that uses multiple meanings for humour', 'A formal apology', 'A type of punctuation mark', 'A scientific measurement'], 0),
   ('Why might a riddle challenge its audience?', ['It asks them to figure out a clever or tricky answer', 'It gives away the answer immediately', 'It has no question or challenge at all', 'It only contains true statements with no puzzle'], 0),
   ('What is the main goal of writing a joke?', ['To entertain an audience and make them laugh', 'To provide a serious history lesson', 'To describe a scientific process in detail', 'To give step by step cooking instructions'], 0)]),
M('Geometry: Diameter and Radius of a Circle',
  'Grade 4 Math strand: the diameter of a circle is the distance across the circle through its centre, while the radius is the distance from the centre to the edge, and the diameter is always twice the radius.',
  [('What is the radius of a circle?', ['The distance from the centre to the edge of the circle', 'The distance around the outside of the circle', 'The distance across the circle through the centre', 'The number of sides a circle has'], 0),
   ('What is the diameter of a circle?', ['The distance across the circle through the centre', 'The distance from the centre to the edge', 'The distance around the outside of the circle', 'The area inside the circle'], 0),
   ('If the radius of a circle is 5 centimetres, what is the diameter?', ['10 centimetres', '5 centimetres', '2.5 centimetres', '15 centimetres'], 0),
   ('If the diameter of a circle is 18 centimetres, what is the radius?', ['9 centimetres', '18 centimetres', '36 centimetres', '6 centimetres'], 0),
   ('How is the diameter of a circle related to its radius?', ['The diameter is always twice the radius', 'The diameter is always half the radius', 'The diameter and radius are always equal', 'The diameter has no relationship to the radius'], 0)]),
Sc('Science: Echoes — How Sound Waves Reflect',
   'Grade 4 Science strand: an echo is a reflection of a sound wave that bounces off a hard surface, such as a wall or a canyon, and returns to the listener a short time after the original sound.',
   [('What is an echo?', ['A reflection of a sound wave bouncing off a surface', 'A type of light wave', 'A magnetic force', 'A change in air pressure'], 0),
    ('What kind of surface is likely to produce a strong echo?', ['A hard, flat surface like a canyon wall', 'A soft surface like a pillow', 'An empty patch of grass', 'A cloud in the sky'], 0),
    ('Why does an echo reach a listener after a short delay?', ['Sound takes time to travel to a surface and bounce back', 'Sound travels instantly with no delay', 'Echoes happen before the original sound', 'Echoes are unrelated to the original sound'], 0),
    ('Where might you be especially likely to hear an echo?', ['Inside a large empty canyon or cave', 'In outer space with no air', 'Deep underground with no walls', 'In a completely open field with no surfaces'], 0),
    ('What does the presence of an echo tell us about sound?', ['Sound can reflect off surfaces like a wave', 'Sound cannot travel through air', 'Sound never interacts with surfaces', 'Sound only exists near water'], 0)]),
SS('Social Studies: The Role of Canadian Embassies Abroad',
   'Grade 4 Social Studies strand: a Canadian embassy is an official office located in another country that represents Canadas government, assists Canadian citizens abroad, and supports relationships between countries.',
   [('What is a Canadian embassy?', ['An official office in another country that represents Canadas government', 'A type of Canadian national park', 'A private Canadian business', 'A Canadian military base only'], 0),
    ('What might a Canadian embassy help with?', ['Assisting Canadian citizens who are traveling or living abroad', 'Managing Canadian school boards', 'Building highways in Canada', 'Running Canadian elections'], 0),
    ('Where is a Canadian embassy typically located?', ['In another country', 'In a Canadian province only', 'Underground', 'In outer space'], 0),
    ('Why are embassies important for relationships between countries?', ['They help support communication and cooperation between governments', 'They prevent any communication between countries', 'They have no diplomatic purpose', 'They only exist to sell goods'], 0),
    ('Who might work at a Canadian embassy?', ['Diplomats and government representatives', 'Only foreign tourists', 'Only private business owners', 'Only students on vacation'], 0)]),
]),
day(160, [
L('Language Review: Grammar Basics, Story Structure, and Word Parts',
  'Grade 4 Language strand review: students revisit articles, plot structure, character sketches, indirect objects, and suffixes.',
  [('What is the definite article in English?', ['The', 'A', 'An', 'But'], 0),
   ('What happens during the rising action of a story?', ['Tension and events build toward the most exciting moment', 'The story ends completely', 'Characters are introduced for the first time', 'Nothing happens in the plot'], 0),
   ('What is the purpose of a character sketch?', ['To describe a characters appearance, personality, and behaviour', 'To list random unrelated facts', 'To describe only a setting', 'To summarize an entire plot with no character details'], 0),
   ('What does an indirect object usually tell us?', ['To whom or for whom an action is done', 'The subject performing the action', 'The main verb in a sentence', 'The setting of a story'], 0),
   ('What is a suffix?', ['A word part added to the end of a base word', 'A word part added to the beginning of a base word', 'A punctuation mark', 'A type of sentence'], 0)]),
M('Math Review: Circles, Fractions, and Time',
  'Grade 4 Math strand review: students revisit dividing by 10, 100, and 1,000, the circumference of a circle, simplifying fractions, converting units of time, and scatter plots.',
  [('What happens to a number when it is divided by 10?', ['The decimal point moves one place to the left', 'The decimal point moves one place to the right', 'The number is multiplied by 10', 'The number stays exactly the same'], 0),
   ('What is the circumference of a circle?', ['The distance around the outer edge of the circle', 'The distance across the middle of the circle', 'The area inside the circle', 'The number of sides a circle has'], 0),
   ('What does it mean to simplify a fraction to lowest terms?', ['Dividing the numerator and denominator by their greatest common factor', 'Multiplying the numerator and denominator by two', 'Adding one to the numerator only', 'Changing the fraction into a whole number'], 0),
   ('How many seconds are in one minute?', ['60', '100', '30', '24'], 0),
   ('What does a scatter plot use to display data?', ['Points plotted on a grid', 'Bars of different heights', 'Slices of a circle', 'Lines connecting single values only'], 0)]),
Sc('Science Review: Life Cycles, Trees, and Weather Systems',
   'Grade 4 Science strand review: students revisit the butterfly life cycle, deciduous and coniferous trees, weather versus climate, the layers of the atmosphere, and animal diets.',
   [('What is the first stage of a butterflys life cycle?', ['Egg', 'Caterpillar', 'Chrysalis', 'Adult butterfly'], 0),
    ('What kind of leaves do deciduous trees typically have?', ['Broad leaves that change colour and drop in autumn', 'Needle-like leaves that never fall', 'No leaves at all', 'Only flowers instead of leaves'], 0),
    ('What does weather describe?', ['Short-term atmospheric conditions on a given day', 'The average conditions of a region over many years', 'Only the temperature of the ocean', 'Only the phases of the moon'], 0),
    ('Which layer of the atmosphere is closest to the ground?', ['The troposphere', 'The exosphere', 'The thermosphere', 'The mesosphere'], 0),
    ('What does a herbivore eat?', ['Only plants', 'Only other animals', 'Both plants and animals', 'Nothing at all'], 0)]),
SS('Social Studies Review: Ancient Trade, Canadian Landmarks, and Local Government',
   'Grade 4 Social Studies strand review: students revisit ancient Carthage, Niagara Falls, the Trans-Canada Highway, provincial flags, and school boards.',
   [('Who founded the ancient city of Carthage?', ['The Phoenicians', 'The Romans', 'The Egyptians', 'The Greeks'], 0),
    ('Niagara Falls is located on the border between Canada and which country?', ['The United States', 'Mexico', 'France', 'Brazil'], 0),
    ('What is the Trans-Canada Highway?', ['A major road system connecting communities across the country', 'A railway line used only for cargo', 'A walking trail through one city', 'A canal used for shipping goods'], 0),
    ('What does each Canadian province and territory have of its own?', ['A unique flag', 'No flag at all', 'The exact same flag as every other province', 'Only a national flag'], 0),
    ('What is a school board responsible for?', ['Managing public schools in a region', 'Running a countrys military', 'Managing national parks', 'Building highways across Canada'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_151_160)
    append_to(4, g4_151_160)
