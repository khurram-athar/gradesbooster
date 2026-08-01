#!/usr/bin/env python3
"""Grade 5, Days 131-140 -- extends Grade 5 from 130 to 140 days. Modeled
exactly on gen_grade5_days121_130.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-130
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: correlative
conjunctions, proverbs and adages, writing a fable with a moral, conditional
(if-then) sentences, understanding allegory, portmanteau words, double
negatives, writing a folktale, and prologues/epilogues for Language;
histograms, profit and loss, graphing number patterns on a coordinate grid,
vertical and adjacent angles, probability of two independent events,
surface area of square-based pyramids, estimating area of irregular shapes
with a grid, expanded form for large numbers, and cube numbers/cube roots
for Math; Newtons second and third laws of motion, series and parallel
circuits, types of rocks (igneous/sedimentary/metamorphic), layers of the
atmosphere, the greenhouse effect and climate change, meteor showers,
bioluminescence, echolocation, and sublimation for Science; and Canadas
immigration points system, political cartoons as historical sources, the
War Measures Act, Crown corporations, the Indian Act, public opinion polls
in elections, Remembrance Day and war memorials, interprovincial trade, and
the Metis sash and Metis cultural symbols for Social Studies -- none of
those exact ideas appear in Days 1-130. Day 140 is a review day across all
four subjects, matching the end-of-batch pattern used in every prior
10-day batch (drawing one representative quiz question per subject from
each of the first five days of the batch, Days 131-135, exactly as Day 130
drew from Days 121-125). No embedded ASCII double-quote characters are
used anywhere in question/summary/option text; apostrophes are dropped
entirely, matching the rest of Grade 5 Days 111-130 (e.g. "Canadas" not
"Canada's", "governments" not "government's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science and Technology',
    'TVO Learn: Grade 5 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L5, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M5, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S5, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS5, q)


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


g5_131_140 = [
day(131, [
L('Grammar: Correlative Conjunctions',
  'Grade 5 Language strand: correlative conjunctions work in pairs, such as either/or, neither/nor, and both/and, to connect balanced words, phrases, or clauses in a sentence.',
  [('What is a correlative conjunction?', ['A pair of words that work together to connect balanced parts of a sentence', 'A single word that ends a sentence', 'A word that shows possession', 'A type of punctuation mark'], 0),
   ('Which pair of words is a correlative conjunction?', ['Either...or', 'Quickly...slowly', 'Dog...cat', 'Run...jump'], 0),
   ('Which sentence correctly uses a correlative conjunction?', ['Neither the cat nor the dog was hungry.', 'The cat neither dog was hungry.', 'The cat, the dog, was hungry.', 'Neither cat the dog hungry.'], 0),
   ('Which correlative conjunction pair would best complete: ___ Sam ___ his sister finished the race?', ['Both...and', 'Either...nor', 'Neither...or', 'Not only...but'], 0),
   ('Why might a writer use correlative conjunctions?', ['To clearly show a balanced relationship between two connected ideas', 'Correlative conjunctions never connect ideas', 'This concept has no connection to grammar', 'To separate every sentence into fragments'], 0)]),
M('Data Management: Constructing and Interpreting Histograms',
  'Grade 5 Math strand: a histogram displays numerical data grouped into equal intervals called bins, using bars with no gaps to show how many data points fall into each range.',
  [('What does a histogram show?', ['How many data points fall into each of several equal-sized intervals', 'A single data point only', 'The names of categories with no numbers', 'A list of unrelated facts'], 0),
   ('How are the bars in a histogram usually arranged?', ['With no gaps between them', 'With wide gaps between every bar', 'Stacked on top of one another', 'In a circle'], 0),
   ('What do we call the equal-sized groups used in a histogram?', ['Bins or intervals', 'Categories only', 'Outliers', 'Axes'], 0),
   ('If a histogram bin for heights 140 to 150 centimetres has a bar reaching 8, what does that mean?', ['8 data points fall between 140 and 150 centimetres', 'The tallest person is 8 centimetres', 'There are 8 different bins in total', '8 people are exactly 140 centimetres tall'], 0),
   ('How is a histogram different from a bar graph of categories?', ['A histogram groups continuous numerical data into ranges, while a bar graph often compares separate categories', 'A histogram never uses bars', 'A bar graph always shows numerical ranges', 'There is no difference between the two graphs'], 0)]),
Sc('Newtons Second and Third Laws of Motion',
   'Grade 5 Science strand: Newtons second law explains that a greater force is needed to accelerate a heavier object, while Newtons third law states that every action has an equal and opposite reaction.',
   [('What does Newtons second law describe?', ['How force, mass, and acceleration are related', 'How objects change colour', 'How sound travels through air', 'How plants grow toward light'], 0),
    ('According to Newtons second law, what happens if you push a heavier object with the same force as a lighter one?', ['The heavier object accelerates more slowly', 'The heavier object accelerates faster', 'Both objects stay perfectly still', 'Only the lighter object can move at all'], 0),
    ('What does Newtons third law state?', ['For every action there is an equal and opposite reaction', 'Objects always stay at rest forever', 'Force has no effect on motion', 'Heavier objects always move faster'], 0),
    ('Which example demonstrates Newtons third law?', ['A swimmer pushes water backward and moves forward', 'A ball rolls downhill without any force', 'A book sits still on a shelf', 'A car engine turns off by itself'], 0),
    ('Why are Newtons laws useful for understanding everyday movement?', ['They explain how forces cause and change the motion of objects around us', 'They only apply to objects in outer space', 'This concept has no relevance to physical science', 'Forces never actually affect how objects move'], 0)]),
SS('Canadas Immigration Points System',
   'Grade 5 Social Studies strand: Canadas immigration points system evaluates applicants for factors such as education, work experience, age, and language ability to help decide who may immigrate through certain programs.',
   [('What is the purpose of Canadas immigration points system?', ['To evaluate applicants based on factors like education and work experience', 'To randomly select applicants with no criteria', 'To collect taxes from new immigrants', 'To limit travel between provinces'], 0),
    ('Which of these might be considered under the points system?', ['Language ability', 'Favourite colour', 'Height', 'Shoe size'], 0),
    ('Why might language ability be an important factor in the points system?', ['Strong language skills can help newcomers find work and integrate into their community', 'Language ability never affects daily life', 'This concept has no connection to immigration', 'The points system ignores every practical skill'], 0),
    ('Is the points system the only way someone can immigrate to Canada?', ['No, there are other programs such as family sponsorship and refugee protection', 'Yes, it is the only possible pathway', 'Immigration to Canada is never possible', 'Only points-based applicants may enter Canada at all'], 0),
    ('Why might a country use a points system for immigration instead of choosing applicants randomly?', ['It allows the country to consider specific skills and needs when welcoming newcomers', 'Random selection is always required by law', 'This concept has no relevance to social studies', 'Points systems ignore a countrys economic needs'], 0)]),
]),
day(132, [
L('Vocabulary: Proverbs and Adages',
  'Grade 5 Language strand: a proverb, or adage, is a short traditional saying that expresses a piece of wisdom or advice, such as Look before you leap.',
  [('What is a proverb?', ['A short traditional saying that expresses wisdom or advice', 'A long chapter in a novel', 'A type of punctuation mark', 'A formal citation of a source'], 0),
   ('What is another word for proverb used in this lesson?', ['Adage', 'Metaphor', 'Simile', 'Prefix'], 0),
   ('What lesson does the proverb Look before you leap teach?', ['Think carefully before acting', 'Always run as fast as possible', 'Leaping is never a good idea', 'Looking is unnecessary before any action'], 0),
   ('Why might proverbs be passed down for many generations?', ['They capture useful lessons or advice in a memorable way', 'Proverbs are always forgotten quickly', 'This concept has no connection to vocabulary', 'Proverbs never contain any useful meaning'], 0),
   ('Which of these is most likely an example of a proverb?', ['Better late than never.', 'The sky is blue today.', 'She walked to the store.', 'Seven plus two equals nine.'], 0)]),
M('Financial Literacy: Understanding Profit and Loss in a Simple Business',
  'Grade 5 Math strand: profit occurs when a businesss revenue is greater than its costs, while a loss occurs when costs are greater than revenue, and calculating both helps track how well a business is doing.',
  [('What is profit?', ['The amount left over when revenue is greater than costs', 'The total amount spent on supplies', 'A type of bank loan', 'The number of customers a business has'], 0),
   ('What is a loss in a business?', ['When costs are greater than revenue', 'When revenue is greater than costs', 'When a business has no customers at all', 'A type of savings account'], 0),
   ('If a lemonade stand earns 40 dollars in sales and spent 25 dollars on supplies, what is the profit?', ['15 dollars', '25 dollars', '40 dollars', '65 dollars'], 0),
   ('If a business spends 60 dollars but only earns 45 dollars in sales, what happened?', ['The business had a loss of 15 dollars', 'The business had a profit of 15 dollars', 'The business broke even exactly', 'The business earned 60 dollars in profit'], 0),
   ('Why is it useful for a business owner to track profit and loss?', ['It helps them understand whether the business is making or losing money over time', 'Profit and loss have no connection to a business', 'This concept has no relevance to financial literacy', 'Tracking money never helps a business owner'], 0)]),
Sc('Simple Circuits: Series and Parallel Connections',
   'Grade 5 Science strand: in a series circuit, components are connected along a single path so current flows through each one in turn, while in a parallel circuit, components are connected along separate branches so current can take multiple paths.',
   [('In a series circuit, how are components connected?', ['Along a single path, one after another', 'Along many completely separate paths', 'They are not connected at all', 'Only to a single battery with no wires'], 0),
    ('In a parallel circuit, how are components connected?', ['Along separate branches', 'Along a single unbroken path only', 'They cannot be connected to each other', 'Only outside of the circuit'], 0),
    ('What happens to the other bulbs in a series circuit if one bulb burns out?', ['They all stop working because the single path is broken', 'They continue to shine as brightly as before', 'They automatically get brighter', 'Nothing changes in the circuit at all'], 0),
    ('What happens to the other bulbs in a parallel circuit if one bulb burns out?', ['The other bulbs usually continue working through their own branch', 'All the bulbs immediately stop working', 'The circuit disappears completely', 'The remaining bulbs turn a different colour'], 0),
    ('Why might household wiring commonly use parallel circuits instead of series circuits?', ['So that one broken device or switch does not stop electricity from reaching everything else', 'Parallel circuits never allow electricity to flow', 'This concept has no relevance to science', 'Series circuits are always safer for a house'], 0)]),
SS('The Role of Political Cartoons in Recording History',
   'Grade 5 Social Studies strand: political cartoons use humour, symbols, and exaggeration to comment on events, leaders, or issues, offering historians a visual record of public opinion at a given time.',
   [('What is a political cartoon?', ['A drawing that uses humour and symbols to comment on events or issues', 'A formal government document', 'A type of national law', 'A photograph with no artistic elements'], 0),
    ('Why might political cartoons use exaggeration?', ['To emphasize a point or opinion in a memorable way', 'Exaggeration is never used in cartoons', 'This concept has no connection to social studies', 'Cartoons always avoid expressing any opinion'], 0),
    ('What can political cartoons tell historians about the past?', ['How people viewed events or leaders at the time', 'The exact temperature on a historic day', 'Nothing useful about historical opinions', 'Only information about weather patterns'], 0),
    ('Why might a cartoonist use a symbol, such as an animal, to represent a country?', ['Symbols can quickly communicate an idea without lengthy explanation', 'Symbols never represent any larger idea', 'This concept has no relevance to history', 'Cartoonists are required to avoid all symbolism'], 0),
    ('Why is it useful to consider a cartoonists point of view when studying a political cartoon?', ['Cartoons often express a particular opinion rather than a neutral fact', 'Cartoons are always completely neutral and factual', 'A cartoonists point of view never matters', 'This concept has no connection to social studies'], 0)]),
]),
day(133, [
L('Writing: Writing a Fable with a Moral',
  'Grade 5 Language strand: a fable is a short story, often featuring animal characters, that teaches a lesson called a moral, usually stated directly at the end of the story.',
  [('What is a fable?', ['A short story, often with animal characters, that teaches a lesson', 'A long biography of a real person', 'A type of grammar rule', 'A formal research report'], 0),
   ('What is the moral of a fable?', ['The lesson the story teaches', 'The title of the story', 'The name of the author', 'A list of characters'], 0),
   ('Where is the moral of a fable often stated?', ['At the end of the story', 'Only in the title', 'Never stated anywhere', 'At the very beginning before any events'], 0),
   ('Why might a fable use animal characters instead of human characters?', ['Animals with human traits can make a lesson memorable and entertaining', 'Animal characters never teach any lesson', 'This concept has no connection to writing', 'Fables are required to avoid all characters'], 0),
   ('Which is most likely the moral of a fable about a slow but steady turtle winning a race?', ['Slow and steady wins the race.', 'Fast animals always win every race.', 'Races are never worth entering.', 'Turtles cannot move at all.'], 0)]),
M('Algebra: Graphing Number Patterns on a Coordinate Grid',
  'Grade 5 Math strand: the outputs of a number pattern can be plotted as ordered pairs on a coordinate grid, revealing whether the pattern grows steadily and forms a straight line.',
  [('What can be plotted on a coordinate grid to show a number pattern?', ['Ordered pairs made from the pattern inputs and outputs', 'Only the colour of each term', 'A single unrelated point', 'The name of the pattern only'], 0),
   ('If a pattern rule is add 3 starting at 2, what are the first three terms?', ['2, 5, 8', '2, 3, 4', '3, 6, 9', '2, 6, 10'], 0),
   ('What might it mean if the plotted points of a pattern form a straight line?', ['The pattern grows or shrinks at a steady, constant rate', 'The pattern has no rule at all', 'The points were plotted incorrectly every time', 'The pattern only has one single term'], 0),
   ('In an ordered pair (x, y) on a graph, what does the x-value usually represent for a pattern?', ['The input, such as the term number', 'The colour of the point', 'A random unrelated number', 'The total of every term added together'], 0),
   ('Why is graphing a number pattern useful?', ['It gives a visual way to see how the pattern changes and predict future terms', 'Graphing a pattern never shows anything useful', 'This concept has no connection to algebra', 'Patterns cannot be represented visually in any way'], 0)]),
Sc('Types of Rocks: Igneous, Sedimentary, and Metamorphic',
   'Grade 5 Science strand: rocks are classified as igneous, sedimentary, or metamorphic based on how they form, whether from cooled magma, compressed layers of sediment, or existing rock changed by heat and pressure.',
   [('How does an igneous rock form?', ['From cooled and hardened magma or lava', 'From layers of sand compressed together', 'From rock heated and pressured underground', 'From dissolved minerals in rivers only'], 0),
    ('How does a sedimentary rock form?', ['From layers of sediment compressed together over time', 'From cooled magma erupting from a volcano', 'From rock instantly turning to gas', 'From lightning striking the ground'], 0),
    ('How does a metamorphic rock form?', ['From existing rock changed by heat and pressure', 'From cooled lava only', 'From sediment that never compresses', 'From rock dissolving completely into water'], 0),
    ('Which type of rock might contain visible layers of sand or mud pressed together?', ['Sedimentary rock', 'Igneous rock', 'Metamorphic rock', 'Molten rock'], 0),
    ('Why might a metamorphic rock look very different from the rock it originally was?', ['Intense heat and pressure can change its mineral structure and appearance', 'Metamorphic rocks never change in any way', 'This concept has no relevance to Earth science', 'Heat and pressure have no effect on rocks'], 0)]),
SS('The War Measures Act and Civil Liberties in Canadian History',
   'Grade 5 Social Studies strand: the War Measures Act was a federal law that allowed the government to take special emergency powers during wartime or crises, at times limiting the civil liberties of Canadians.',
   [('What was the War Measures Act?', ['A federal law allowing special emergency powers during wartime or crises', 'A provincial tax law', 'A treaty with another country', 'A type of municipal bylaw'], 0),
    ('What could the War Measures Act allow the government to limit?', ['The civil liberties of Canadians', 'The size of a province', 'The number of national holidays', 'The colours of the Canadian flag'], 0),
    ('During what kind of situation might the War Measures Act have been used?', ['A national emergency, such as a world war', 'A minor local disagreement', 'A routine municipal election', 'A weekly town meeting'], 0),
    ('Why might historians view the use of the War Measures Act as controversial at times?', ['It sometimes restricted the rights and freedoms of certain groups of Canadians', 'It never had any effect on Canadians', 'This concept has no connection to Canadian history', 'The Act was never actually used by the government'], 0),
    ('Why is it important for students to study laws like the War Measures Act?', ['It helps them understand the balance between government power and individual rights', 'It has no relevance to understanding government', 'This concept has no connection to social studies', 'Laws from the past never affect how we think today'], 0)]),
]),
day(134, [
L('Grammar: Conditional Sentences (If-Then Statements)',
  'Grade 5 Language strand: a conditional sentence uses an if clause to describe a condition and a main clause to describe the result, such as If it rains, we will stay inside.',
  [('What does a conditional sentence describe?', ['A condition and its result', 'A list of nouns only', 'A single interjection', 'A type of rhyme scheme'], 0),
   ('Which part of a conditional sentence usually begins with the word if?', ['The condition clause', 'The result clause only', 'The title of the sentence', 'A footnote'], 0),
   ('Which sentence is a correctly formed conditional sentence?', ['If it rains, we will stay inside.', 'Rains if it we will stay inside.', 'We stay inside it rains if.', 'Inside stay we will if it rains'], 0),
   ('In the sentence If you study, you will pass the test, what is the result clause?', ['You will pass the test', 'If you study', 'The word if', 'A comma only'], 0),
   ('Why might writers use conditional sentences?', ['To show a cause-and-effect relationship between a condition and its outcome', 'Conditional sentences never show any relationship between ideas', 'This concept has no connection to grammar', 'Conditional sentences always describe two unrelated events'], 0)]),
M('Geometry: Vertical and Adjacent Angles',
  'Grade 5 Math strand: when two lines cross, they form vertical angles, which are opposite each other and always equal, and adjacent angles, which share a vertex and a side.',
  [('What are vertical angles?', ['A pair of opposite angles formed when two lines cross, which are always equal', 'Angles that never touch each other', 'Angles that always add up to 90 degrees', 'A single angle with no pair'], 0),
   ('What are adjacent angles?', ['Angles that share a vertex and a side', 'Angles that are always exactly equal', 'Angles found only in circles', 'Angles that never share any point'], 0),
   ('If two lines cross and one angle measures 50 degrees, what does its vertical angle measure?', ['50 degrees', '40 degrees', '90 degrees', '130 degrees'], 0),
   ('Do adjacent angles always add up to 90 degrees?', ['No, only certain adjacent angles add up to 90 degrees', 'Yes, every pair of adjacent angles equals 90 degrees', 'Adjacent angles always equal 360 degrees', 'Adjacent angles are never measured in degrees'], 0),
   ('Why is knowing that vertical angles are equal useful in geometry?', ['It helps you find a missing angle measure without measuring it directly', 'Vertical angles are never useful in geometry', 'This concept has no connection to angles', 'Vertical angles always have different measures'], 0)]),
Sc('The Layers of Earths Atmosphere',
   'Grade 5 Science strand: Earths atmosphere is made up of several layers, including the troposphere closest to the surface and the higher stratosphere, each with different roles such as containing weather or the ozone layer.',
   [('Which layer of the atmosphere is closest to Earths surface?', ['The troposphere', 'The stratosphere', 'The mesosphere', 'The exosphere'], 0),
    ('What happens in the troposphere?', ['Most weather occurs there', 'It contains no gases at all', 'It is completely empty of air', 'It is located far beyond the Moon'], 0),
    ('Which layer contains the ozone layer that filters harmful sunlight?', ['The stratosphere', 'The troposphere', 'The core of the Earth', 'The ocean floor'], 0),
    ('Why might air become thinner at higher layers of the atmosphere?', ['There are fewer gas molecules as altitude increases', 'Air always becomes thicker with altitude', 'The atmosphere has no layers at all', 'Gravity has no effect on the atmosphere'], 0),
    ('Why is it useful for scientists to study the different layers of the atmosphere?', ['It helps them understand weather, climate, and the protection the atmosphere provides', 'The atmosphere has no effect on Earth', 'This concept has no relevance to science', 'Studying the atmosphere provides no useful information'], 0)]),
SS('Crown Corporations in Canada — CBC, Canada Post, and More',
   'Grade 5 Social Studies strand: a Crown corporation is a business owned by the government that provides services such as broadcasting or mail delivery, operating with public goals rather than only seeking profit.',
   [('What is a Crown corporation?', ['A business owned by the government', 'A private company with no government connection', 'A type of foreign embassy', 'A club run entirely by volunteers'], 0),
    ('Which of these is an example of a Canadian Crown corporation?', ['Canada Post', 'A local bakery', 'A private grocery chain', 'A family-owned farm'], 0),
    ('What does the CBC provide as a Crown corporation?', ['Public broadcasting services', 'National defence', 'Provincial voting districts', 'Municipal water supply'], 0),
    ('Why might a government choose to run certain services through Crown corporations?', ['To ensure important services are available to the public, not only for profit', 'Crown corporations are never connected to public services', 'This concept has no relevance to government', 'Governments never operate any businesses'], 0),
    ('How is a Crown corporation different from a typical private business?', ['It is owned by the government and often focuses on public service goals', 'It has no owners of any kind', 'It is identical in every way to a private business', 'It cannot provide any services to the public'], 0)]),
]),
day(135, [
L('Reading: Understanding Allegory',
  'Grade 5 Language strand: an allegory is a story in which characters, settings, or events represent broader ideas or messages, often about morality or society, beyond the literal plot.',
  [('What is an allegory?', ['A story in which characters or events represent broader ideas or messages', 'A story with no characters at all', 'A list of vocabulary definitions', 'A type of punctuation mark'], 0),
   ('What might an allegory be about, beyond its literal plot?', ['Morality or society', 'The exact date it was written', 'The authors favourite colour', 'A random unrelated topic'], 0),
   ('Why might an author choose to write an allegory instead of stating a message directly?', ['It allows readers to discover a deeper meaning through the story itself', 'Allegories never contain any deeper meaning', 'This concept has no connection to reading', 'Authors never intend allegories to have any message'], 0),
   ('Which is most likely a feature of an allegory?', ['Characters that symbolize larger ideas, such as greed or justice', 'A story with absolutely no symbolism', 'A text with only factual, literal information', 'A story that avoids any characters entirely'], 0),
   ('Why might understanding allegory help a reader analyze a text more deeply?', ['It reveals a layer of meaning beyond the surface-level events of the story', 'Allegory never adds any meaning to a story', 'This concept has no relevance to reading comprehension', 'Allegories are always identical to nonfiction texts'], 0)]),
M('Data Management: Probability of Two Independent Events',
  'Grade 5 Math strand: when two events are independent, meaning one does not affect the other, the probability of both happening can be found by multiplying their individual probabilities.',
  [('What does it mean for two events to be independent?', ['The outcome of one event does not affect the outcome of the other', 'The two events always happen at the exact same time', 'One event always causes the other to happen', 'Independent events can never both occur'], 0),
   ('How do you find the probability of two independent events both happening?', ['Multiply their individual probabilities', 'Add their individual probabilities', 'Subtract one probability from the other', 'Divide the two probabilities by ten'], 0),
   ('If the probability of flipping heads is 1/2 and rolling a 6 is 1/6, what is the probability of both happening?', ['1/12', '1/8', '1/2', '2/3'], 0),
   ('Which situation describes two independent events?', ['Flipping a coin and rolling a die', 'Drawing two cards from a deck without replacing the first', 'Picking a marble and then picking another without putting the first back', 'Choosing a captain, then a co-captain from the remaining players'], 0),
   ('Why is multiplying probabilities useful for independent events?', ['It shows how much less likely it is for two separate events to both occur together', 'Multiplying probabilities is never useful in data management', 'This concept has no connection to probability', 'Independent events always have a probability of exactly 1'], 0)]),
Sc('The Greenhouse Effect and Climate Change',
   'Grade 5 Science strand: the greenhouse effect occurs when gases in the atmosphere trap heat from the sun, and an increase in these gases from human activity is linked to long-term changes in Earths climate.',
   [('What does the greenhouse effect describe?', ['Gases in the atmosphere trapping heat from the sun', 'Plants growing inside a glass building', 'The Moon reflecting light onto Earth', 'Ocean currents cooling the atmosphere'], 0),
    ('Which of these is considered a greenhouse gas?', ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'], 0),
    ('What human activity is often linked to increasing greenhouse gases?', ['Burning fossil fuels', 'Planting more forests', 'Recycling paper', 'Drinking more water'], 0),
    ('Why is the greenhouse effect sometimes described as necessary for life on Earth in normal amounts?', ['It helps keep the planet warm enough to support living things', 'It removes all heat from the planet', 'It has no connection to temperature at all', 'It prevents any sunlight from reaching Earth'], 0),
    ('Why are scientists concerned about rising levels of greenhouse gases?', ['Extra trapped heat is linked to long-term changes in Earths climate', 'Greenhouse gases have no effect on climate at all', 'This concept has no relevance to science', 'Rising greenhouse gases always cool the planet down'], 0)]),
SS('The Indian Act and Its Legacy',
   'Grade 5 Social Studies strand: the Indian Act is a federal law first passed in 1876 that has governed many aspects of life for First Nations peoples, and its ongoing legacy remains an important part of understanding reconciliation in Canada.',
   [('What is the Indian Act?', ['A federal law that has governed many aspects of life for First Nations peoples', 'A treaty between Canada and another country', 'A provincial tax code', 'A modern trade agreement'], 0),
    ('Roughly when was the Indian Act first passed?', ['1876', '1967', '2000', '1600'], 0),
    ('Why is the Indian Act considered significant in Canadian history?', ['It has had a lasting impact on the rights and daily lives of First Nations peoples', 'It never affected anyone in Canada', 'This concept has no relevance to social studies', 'It was cancelled the year after it was passed'], 0),
    ('Why do many people today discuss reforming or replacing parts of the Indian Act?', ['Its historic restrictions and effects are seen as harmful to Indigenous self-determination', 'The Act has always been viewed as entirely beneficial', 'No one has ever discussed changing the Act', 'The Act has no connection to Indigenous peoples'], 0),
    ('Why is learning about the Indian Act important for understanding reconciliation in Canada?', ['It helps explain the historical roots of challenges First Nations communities continue to address', 'It has no connection to reconciliation efforts', 'This concept has no relevance to Canadian history', 'Reconciliation has nothing to do with past laws'], 0)]),
]),
day(136, [
L('Vocabulary: Portmanteau Words (Blended Words)',
  'Grade 5 Language strand: a portmanteau word blends the sounds and meanings of two other words into one new word, such as brunch from breakfast and lunch.',
  [('What is a portmanteau word?', ['A word that blends the sounds and meanings of two other words', 'A word with no meaning at all', 'A type of punctuation mark', 'A word borrowed directly from a persons name'], 0),
   ('The word brunch is a portmanteau of which two words?', ['Breakfast and lunch', 'Bread and lunch', 'Brunch and dinner', 'Break and munch only'], 0),
   ('What two words combine to form the portmanteau smog?', ['Smoke and fog', 'Small and dog', 'Smooth and log', 'Snow and frog'], 0),
   ('Why might people create portmanteau words?', ['To describe a new idea by combining two familiar words', 'Portmanteau words are always accidental mistakes', 'This concept has no connection to vocabulary', 'Portmanteau words never combine any existing words'], 0),
   ('Which of these is an example of a portmanteau word?', ['Motel', 'Table', 'Window', 'Pencil'], 0)]),
M('Geometry: Surface Area of Square-Based Pyramids',
  'Grade 5 Math strand: the surface area of a square-based pyramid is found by adding the area of its square base to the areas of its four triangular faces.',
  [('What shape is the base of a square-based pyramid?', ['A square', 'A circle', 'A triangle', 'A pentagon'], 0),
   ('How many triangular faces does a square-based pyramid have?', ['Four', 'Two', 'Six', 'One'], 0),
   ('What is added to the area of the base to find the total surface area of a square-based pyramid?', ['The areas of the four triangular faces', 'The volume of the pyramid', 'The perimeter of the base only', 'The height of the pyramid'], 0),
   ('Why might you calculate the area of each triangular face separately before adding them together?', ['Each face may need its own measurements to calculate area accurately', 'All faces are always exactly the same regardless of measurements', 'Triangular faces never need to be measured', 'Surface area never involves triangular faces'], 0),
   ('Why is understanding surface area useful for a real object, like a tent shaped like a pyramid?', ['It helps determine how much material is needed to cover the entire shape', 'Surface area has no connection to real objects', 'This concept has no relevance to geometry', 'Surface area only applies to two-dimensional shapes'], 0)]),
Sc('Meteor Showers and Shooting Stars',
   'Grade 5 Science strand: a meteor shower occurs when Earth passes through a trail of debris left by a comet, causing many small particles to burn up in the atmosphere and appear as shooting stars.',
   [('What causes a meteor shower?', ['Earth passing through a trail of debris left by a comet', 'The Moon exploding into small pieces', 'Sunlight reflecting off ocean water', 'Wind currents high in the atmosphere'], 0),
    ('What is commonly called a shooting star?', ['A small particle burning up as it enters Earths atmosphere', 'A star that physically falls out of the sky', 'A planet moving closer to Earth', 'A cloud lit up by the Moon'], 0),
    ('Why do meteors glow brightly as they fall?', ['Friction with the atmosphere heats them until they burn up', 'They reflect light from distant galaxies', 'They are struck by lightning', 'They absorb heat from the ocean'], 0),
    ('Are meteor showers generally predictable events?', ['Yes, they often occur at similar times each year', 'No, they have never been observed before', 'They only happen once per century', 'They can only be seen from outer space'], 0),
    ('Why might scientists study meteor showers?', ['To learn more about comets and the debris left behind in space', 'Meteor showers provide no useful scientific information', 'This concept has no relevance to Earth and space science', 'Meteor showers have no connection to comets'], 0)]),
SS('Public Opinion Polls and Their Role in Canadian Elections',
   'Grade 5 Social Studies strand: public opinion polls survey a sample of people to estimate how a larger population feels about candidates or issues, often shaping media coverage during elections.',
   [('What is the purpose of a public opinion poll?', ['To estimate how a larger population feels about candidates or issues', 'To officially declare the winner of an election', 'To collect taxes from voters', 'To replace the need for an election entirely'], 0),
    ('How do pollsters usually gather information for a poll?', ['By surveying a sample of people', 'By asking every single citizen in the country', 'By guessing without asking anyone', 'By reading only newspaper headlines'], 0),
    ('Why might polls sometimes be inaccurate?', ['The sample surveyed may not perfectly represent the whole population', 'Polls are always exactly accurate with no exceptions', 'Polls never involve any sampling of people', 'This concept has no relevance to elections'], 0),
    ('How might public opinion polls influence media coverage during an election?', ['Media may focus more attention on candidates shown to be leading in the polls', 'Polls have no effect on media coverage at all', 'Media coverage always ignores every poll result', 'Polls are only used after an election ends'], 0),
    ('Why is it important for citizens to think critically about poll results?', ['Polls are estimates, not guarantees, of how an election will turn out', 'Poll results are always a perfect prediction of the outcome', 'This concept has no relevance to social studies', 'Citizens should always ignore all poll information'], 0)]),
]),
day(137, [
L('Grammar: Double Negatives and How to Correct Them',
  'Grade 5 Language strand: a double negative occurs when two negative words are used in the same clause, which is considered incorrect in standard English and can be fixed by removing one negative word.',
  [('What is a double negative?', ['Using two negative words in the same clause', 'Using two positive words in a sentence', 'Repeating the same noun twice', 'A sentence with no verb at all'], 0),
   ('Which sentence contains a double negative?', ['I do not have no pencils.', 'I do not have any pencils.', 'I have some pencils.', 'I have several pencils.'], 0),
   ('How can the double negative in I do not have no pencils be corrected?', ['I do not have any pencils.', 'I do not have no pencils still.', 'I have no pencils not.', 'I not have no pencils.'], 0),
   ('Why are double negatives considered incorrect in standard English?', ['They can create confusing or contradictory meaning', 'Double negatives always make a sentence clearer', 'This concept has no connection to grammar', 'Double negatives are required in every sentence'], 0),
   ('Which sentence correctly avoids a double negative?', ['She does not want any help.', 'She does not want no help.', 'She not want no help never.', 'She never wants no help at all.'], 0)]),
M('Measurement: Estimating Area of Irregular Shapes Using a Grid',
  'Grade 5 Math strand: the area of an irregular shape can be estimated by placing it on a grid and counting the number of whole and partial squares it covers.',
  [('How can you estimate the area of an irregular shape using a grid?', ['By counting the whole and partial squares it covers', 'By measuring only its longest side', 'By ignoring the shape completely', 'By counting only the whole squares outside the shape'], 0),
   ('If a shape covers 10 whole squares and 4 half squares, what is a reasonable area estimate?', ['12 square units', '10 square units', '14 square units', '4 square units'], 0),
   ('Why is this method called an estimate rather than an exact measurement?', ['Partial squares must be judged and combined, which is not perfectly precise', 'Grids always give a perfectly exact measurement', 'Estimation is never involved in this method', 'This concept has no connection to measurement'], 0),
   ('Why might placing a shape on a grid help when it has curved or uneven edges?', ['It breaks the shape into small, countable square units for easier estimation', 'Grids cannot be used with curved shapes at all', 'Curved shapes have no area to measure', 'This concept has no relevance to geometry'], 0),
   ('Why is estimating area with a grid a useful skill in real life?', ['It helps approximate the size of oddly shaped spaces, such as a garden or lake', 'This skill is never useful outside of a classroom', 'Irregular shapes never appear in real life', 'This concept has no connection to measurement'], 0)]),
Sc('Bioluminescence — Living Things That Make Their Own Light',
   'Grade 5 Science strand: bioluminescence is the ability of certain living things, such as fireflies and some deep-sea creatures, to produce their own light through a chemical reaction inside their bodies.',
   [('What is bioluminescence?', ['The ability of a living thing to produce its own light', 'The ability to survive without water', 'The ability to change colour like a chameleon', 'The ability to fly at high speeds'], 0),
    ('Which of these animals is known for bioluminescence?', ['Fireflies', 'Elephants', 'Wolves', 'Sparrows'], 0),
    ('How do bioluminescent organisms typically produce light?', ['Through a chemical reaction inside their bodies', 'By absorbing sunlight during the day', 'By reflecting moonlight off their skin', 'By using electricity from wires'], 0),
    ('Why might bioluminescence be especially useful for creatures living in the deep ocean?', ['It provides a source of light in an environment with little or no sunlight', 'The deep ocean already has abundant sunlight', 'Bioluminescence has no use in the ocean', 'Deep-sea creatures never need any light at all'], 0),
    ('Why might an organism use bioluminescence to attract prey or a mate?', ['Light can signal or lure other organisms in dark environments', 'Light never attracts other living things', 'This concept has no relevance to science', 'Bioluminescence always repels every nearby creature'], 0)]),
SS('Remembrance Day and Canadas War Memorials',
   'Grade 5 Social Studies strand: Remembrance Day, observed on November 11, honours Canadians who served and died in wartime, and war memorials across the country help preserve the memory of their sacrifice.',
   [('What does Remembrance Day honour?', ['Canadians who served and died in wartime', 'The founding of a new political party', 'The signing of a trade agreement', 'The opening of a new national park'], 0),
    ('On what date is Remembrance Day observed?', ['November 11', 'July 1', 'January 1', 'October 31'], 0),
    ('What symbol is commonly worn in Canada leading up to Remembrance Day?', ['A poppy', 'A maple leaf pin', 'A small flag', 'A red ribbon'], 0),
    ('What is the purpose of a war memorial?', ['To help preserve the memory of those who served and sacrificed', 'To celebrate a sports championship', 'To mark the location of a new building', 'To advertise a local business'], 0),
    ('Why might communities hold ceremonies at war memorials on Remembrance Day?', ['To publicly honour and remember those who served their country', 'Ceremonies at war memorials never take place', 'This concept has no connection to Canadian history', 'War memorials have no connection to Remembrance Day'], 0)]),
]),
day(138, [
L('Writing: Writing a Folktale',
  'Grade 5 Language strand: a folktale is a traditional story passed down through generations, often explaining customs or beliefs of a culture and featuring simple, memorable characters.',
  [('What is a folktale?', ['A traditional story passed down through generations', 'A modern news article', 'A type of formal essay', 'A scientific research report'], 0),
   ('What might a folktale help explain about a culture?', ['Its customs or beliefs', 'The exact population of a country', 'A modern stock market trend', 'A list of scientific formulas'], 0),
   ('How are folktales traditionally passed down?', ['Through spoken storytelling across generations', 'Only through official government documents', 'Through scientific journals', 'Through modern television broadcasts only'], 0),
   ('Why might folktale characters often be simple and memorable?', ['This makes the story easier to remember and retell', 'Simple characters make a story impossible to remember', 'This concept has no connection to writing', 'Folktales are required to avoid all characters'], 0),
   ('Which of these best describes a folktale?', ['A traditional tale reflecting the values of a community', 'A factual news report with no story elements', 'A formal legal document', 'A scientific diagram with labels'], 0)]),
M('Number Sense: Expanded Form and Place Value for Large Numbers',
  'Grade 5 Math strand: expanded form breaks a large number into the sum of the values of each digit based on place value, such as writing 4,532 as 4000 + 500 + 30 + 2.',
  [('What does expanded form show about a number?', ['The value of each digit based on its place value', 'The colour associated with a number', 'The number rounded to the nearest ten', 'A number written in Roman numerals'], 0),
   ('How would 4,532 be written in expanded form?', ['4000 + 500 + 30 + 2', '4000 + 500 + 3 + 2', '400 + 50 + 3 + 2', '4532 + 0'], 0),
   ('In the number 7,215, what is the value of the digit 2?', ['200', '2', '20', '2000'], 0),
   ('Why is expanded form useful when working with large numbers?', ['It shows the value contributed by each digit, making place value clearer', 'Expanded form removes all meaning from a number', 'This concept has no connection to number sense', 'Expanded form only works for numbers under ten'], 0),
   ('Which expanded form correctly represents 9,043?', ['9000 + 40 + 3', '9000 + 400 + 3', '900 + 40 + 3', '9000 + 43'], 0)]),
Sc('Echolocation — How Bats Navigate in the Dark',
   'Grade 5 Science strand: echolocation is a method some animals, such as bats, use to navigate and find prey by emitting sounds and listening for the echoes that bounce back off nearby objects.',
   [('What is echolocation?', ['A method of navigating by emitting sounds and listening for echoes', 'A method of seeing in bright daylight only', 'A way of communicating using only colour', 'A process plants use to absorb sunlight'], 0),
    ('Which animal is well known for using echolocation?', ['Bats', 'Butterflies', 'Squirrels', 'Robins'], 0),
    ('How does echolocation help a bat find prey in the dark?', ['The returning echoes reveal the location and distance of nearby objects', 'Bats rely only on bright moonlight to see', 'Bats use their sense of taste to locate prey', 'Bats cannot find prey in the dark at all'], 0),
    ('Why might echolocation be especially useful for an animal that is active at night?', ['It allows the animal to navigate without relying on sight', 'Echolocation only works during the day', 'Nocturnal animals never need to navigate', 'This concept has no relevance to science'], 0),
    ('Why do echoes bounce back differently depending on what they hit?', ['Different objects reflect sound waves differently based on their size, shape, and material', 'All objects reflect every sound wave in exactly the same way', 'Echoes never depend on the object they hit', 'Sound waves never bounce off any surface'], 0)]),
SS('Interprovincial Trade — Buying and Selling Within Canada',
   'Grade 5 Social Studies strand: interprovincial trade refers to the buying and selling of goods and services between provinces and territories within Canada, an important part of the countrys overall economy.',
   [('What is interprovincial trade?', ['The buying and selling of goods and services between provinces and territories', 'Trade that only happens with other countries', 'A tax charged on all imported goods', 'A type of municipal election'], 0),
    ('How is interprovincial trade different from international trade?', ['It takes place within Canada rather than between Canada and other countries', 'It only involves goods from outside North America', 'There is no difference between the two types of trade', 'International trade only happens within one province'], 0),
    ('Why might interprovincial trade be important to Canadas economy?', ['It allows provinces to share resources and products they may not produce themselves', 'Interprovincial trade has no effect on the economy', 'This concept has no relevance to social studies', 'Provinces are never allowed to trade with each other'], 0),
    ('What might be an example of interprovincial trade?', ['Alberta selling oil products to Ontario', 'Canada selling wheat to another country', 'A country importing goods from overseas', 'A city collecting property taxes'], 0),
    ('Why might differing provincial regulations sometimes create a barrier to interprovincial trade?', ['Different rules between provinces can make it harder to move goods and services smoothly', 'Provincial regulations never affect trade in any way', 'This concept has no connection to Canadas economy', 'All provinces are required to have identical laws'], 0)]),
]),
day(139, [
L('Reading: Understanding Prologues and Epilogues',
  'Grade 5 Language strand: a prologue is an introductory section that appears before the main story to provide background information, while an epilogue appears after the main story to show what happens afterward.',
  [('What is a prologue?', ['An introductory section that appears before the main story', 'The final chapter of a novel', 'A list of characters only', 'A type of punctuation mark'], 0),
   ('What is an epilogue?', ['A section that appears after the main story to show what happens afterward', 'A section that always appears before the title page', 'A summary written by a different author', 'A dictionary of difficult words'], 0),
   ('What kind of information might a prologue provide?', ['Background information that helps set up the story', 'The exact ending of the story', 'A list of unrelated grammar rules', 'A recipe for a meal'], 0),
   ('Why might an author include an epilogue?', ['To show readers the outcome or future of the characters after the main plot ends', 'Epilogues never provide any information about characters', 'This concept has no connection to reading', 'An epilogue always appears before the story begins'], 0),
   ('Why might a prologue be useful for a reader before starting the main story?', ['It can provide context that helps the reader understand events to come', 'A prologue always confuses readers on purpose', 'This concept has no relevance to reading comprehension', 'Prologues never relate to the main story in any way'], 0)]),
M('Number Sense: Cube Numbers and Cube Roots',
  'Grade 5 Math strand: a cube number is the result of multiplying a whole number by itself three times, such as 2 cubed equals 8, and a cube root works backward to find that original number.',
  [('What does it mean to cube a number?', ['To multiply it by itself three times', 'To multiply it by itself two times', 'To divide it by three', 'To add three to it'], 0),
   ('What is 2 cubed (2 x 2 x 2)?', ['8', '6', '4', '9'], 0),
   ('What is the cube root of 27?', ['3', '9', '6', '27'], 0),
   ('How is finding a cube root different from finding a cube number?', ['A cube root works backward to find the original number that was cubed', 'A cube root and a cube number mean exactly the same thing', 'Cube roots always produce a larger number than the original', 'Cube roots have no connection to cube numbers'], 0),
   ('Why might understanding cube numbers be useful when studying volume?', ['The volume of a cube with equal side lengths involves multiplying that length by itself three times', 'Cube numbers have no connection to volume at all', 'This concept has no relevance to number sense', 'Volume is never calculated using multiplication'], 0)]),
Sc('Sublimation — When a Solid Turns Directly Into a Gas',
   'Grade 5 Science strand: sublimation is the process by which a solid changes directly into a gas without passing through a liquid state, as seen when dry ice releases a fog-like vapour.',
   [('What is sublimation?', ['The process of a solid changing directly into a gas', 'The process of a liquid changing into a solid', 'The process of a gas changing into a liquid', 'The process of a solid melting into a liquid'], 0),
    ('During sublimation, does a substance pass through a liquid state?', ['No, it skips the liquid state entirely', 'Yes, it always becomes a liquid first', 'It becomes a liquid and then a solid again', 'Sublimation only happens to liquids'], 0),
    ('Which substance is commonly used to demonstrate sublimation?', ['Dry ice', 'Liquid water', 'Table salt', 'Cooking oil'], 0),
    ('What is the opposite process of sublimation, in which a gas changes directly into a solid?', ['Deposition', 'Evaporation', 'Condensation', 'Melting'], 0),
    ('Why might sublimation be considered a change in state rather than a chemical change?', ['The substance is still made of the same particles, just arranged differently', 'Sublimation always creates a completely new substance', 'This concept has no connection to matter', 'Sublimation destroys all the original particles'], 0)]),
SS('The Métis Sash and Symbols of Métis Culture',
   'Grade 5 Social Studies strand: the Métis sash is a colourful, woven garment worn as a symbol of Métis identity and pride, historically used for practical purposes as well as to represent community and heritage.',
   [('What is the Métis sash?', ['A colourful, woven garment that symbolizes Métis identity and pride', 'A type of government document', 'A style of traditional footwear', 'A musical instrument'], 0),
    ('Besides being a symbol, what was the Métis sash historically used for?', ['Practical purposes, such as carrying items or providing warmth', 'Collecting taxes from traders', 'Marking provincial borders', 'Measuring distances on a map'], 0),
    ('What might wearing a Métis sash represent today?', ['Pride in Métis community and heritage', 'A random fashion choice with no meaning', 'A type of school uniform', 'A rule required by federal law'], 0),
    ('Why are cultural symbols like the Métis sash important to a community?', ['They help preserve and express a groups identity and history', 'Cultural symbols have no meaning to any community', 'This concept has no relevance to social studies', 'Symbols always replace a communitys traditions entirely'], 0),
    ('Why might students learn about symbols like the Métis sash in social studies?', ['It helps build understanding and respect for Métis culture and heritage', 'Learning about cultural symbols has no educational value', 'This concept has no connection to Canadian history', 'Métis culture has no symbols worth studying'], 0)]),
]),
day(140, [
L('Language Review: Grammar, Vocabulary, and Storytelling Forms',
  'Grade 5 Language strand review: students revisit correlative conjunctions, proverbs and adages, writing a fable with a moral, conditional sentences, and allegory.',
  [('What is a correlative conjunction?', ['A pair of words that work together to connect balanced parts of a sentence', 'A single word that ends a sentence', 'A word that shows possession', 'A type of punctuation mark'], 0),
   ('What is a proverb?', ['A short traditional saying that expresses wisdom or advice', 'A long chapter in a novel', 'A type of punctuation mark', 'A formal citation of a source'], 0),
   ('What is a fable?', ['A short story, often with animal characters, that teaches a lesson', 'A long biography of a real person', 'A type of grammar rule', 'A formal research report'], 0),
   ('What does a conditional sentence describe?', ['A condition and its result', 'A list of nouns only', 'A single interjection', 'A type of rhyme scheme'], 0),
   ('What is an allegory?', ['A story in which characters or events represent broader ideas or messages', 'A story with no characters at all', 'A list of vocabulary definitions', 'A type of punctuation mark'], 0)]),
M('Math Review: Data, Algebra, and Probability',
  'Grade 5 Math strand review: students revisit histograms, profit and loss, graphing number patterns, vertical and adjacent angles, and probability of independent events.',
  [('What does a histogram show?', ['How many data points fall into each of several equal-sized intervals', 'A single data point only', 'The names of categories with no numbers', 'A list of unrelated facts'], 0),
   ('What is profit?', ['The amount left over when revenue is greater than costs', 'The total amount spent on supplies', 'A type of bank loan', 'The number of customers a business has'], 0),
   ('What can be plotted on a coordinate grid to show a number pattern?', ['Ordered pairs made from the pattern inputs and outputs', 'Only the colour of each term', 'A single unrelated point', 'The name of the pattern only'], 0),
   ('What are vertical angles?', ['A pair of opposite angles formed when two lines cross, which are always equal', 'Angles that never touch each other', 'Angles that always add up to 90 degrees', 'A single angle with no pair'], 0),
   ('What does it mean for two events to be independent?', ['The outcome of one event does not affect the outcome of the other', 'The two events always happen at the exact same time', 'One event always causes the other to happen', 'Independent events can never both occur'], 0)]),
Sc('Science Review: Forces, Matter, and Earth Systems',
   'Grade 5 Science strand review: students revisit Newtons second and third laws, series and parallel circuits, types of rocks, layers of the atmosphere, and the greenhouse effect.',
   [('What does Newtons second law describe?', ['How force, mass, and acceleration are related', 'How objects change colour', 'How sound travels through air', 'How plants grow toward light'], 0),
    ('In a series circuit, how are components connected?', ['Along a single path, one after another', 'Along many completely separate paths', 'They are not connected at all', 'Only to a single battery with no wires'], 0),
    ('How does an igneous rock form?', ['From cooled and hardened magma or lava', 'From layers of sand compressed together', 'From rock heated and pressured underground', 'From dissolved minerals in rivers only'], 0),
    ('Which layer of the atmosphere is closest to Earths surface?', ['The troposphere', 'The stratosphere', 'The mesosphere', 'The exosphere'], 0),
    ('What does the greenhouse effect describe?', ['Gases in the atmosphere trapping heat from the sun', 'Plants growing inside a glass building', 'The Moon reflecting light onto Earth', 'Ocean currents cooling the atmosphere'], 0)]),
SS('Social Studies Review: Immigration, Government, and Canadian History',
   'Grade 5 Social Studies strand review: students revisit the immigration points system, political cartoons, the War Measures Act, Crown corporations, and the Indian Act.',
   [('What is the purpose of Canadas immigration points system?', ['To evaluate applicants based on factors like education and work experience', 'To randomly select applicants with no criteria', 'To collect taxes from new immigrants', 'To limit travel between provinces'], 0),
    ('What is a political cartoon?', ['A drawing that uses humour and symbols to comment on events or issues', 'A formal government document', 'A type of national law', 'A photograph with no artistic elements'], 0),
    ('What was the War Measures Act?', ['A federal law allowing special emergency powers during wartime or crises', 'A provincial tax law', 'A treaty with another country', 'A type of municipal bylaw'], 0),
    ('What is a Crown corporation?', ['A business owned by the government', 'A private company with no government connection', 'A type of foreign embassy', 'A club run entirely by volunteers'], 0),
    ('What is the Indian Act?', ['A federal law that has governed many aspects of life for First Nations peoples', 'A treaty between Canada and another country', 'A provincial tax code', 'A modern trade agreement'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_131_140)
    append_to(5, g5_131_140)
