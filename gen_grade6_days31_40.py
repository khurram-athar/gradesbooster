#!/usr/bin/env python3
"""Phase 3: Grade 6, Days 31-40 (first Grade 6 batch, continuing the
10-day pattern used for Grades 3-5). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade6.json): tone/bias
analysis, thesis statements, two-step equations, surface area, cells and
microorganisms, natural disasters, and world-history topics not yet
covered (Vikings, the Silk Road, the Islamic Golden Age, feudal Japan,
the Cold War, the UN, and Canada's peacekeeping role).

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes use the curly
Unicode form (’) so they never collide with the single-quoted Python
string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science & Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


g6_31_40 = [
day(31, [
L('Reading: Analyzing Tone and Bias in Nonfiction',
  'Ontario Grade 6 Reading strand: tone is the author’s attitude toward a topic, and analyzing tone alongside word choice can reveal bias in a nonfiction text.',
  [('Tone in a text refers to ___.', ['The author’s attitude toward the topic', 'The page count of the text', 'The font style used', 'The publisher’s name'], 0),
   ('Which word choice might suggest a critical tone toward a decision?', ['Reckless', 'Careful', 'Thoughtful', 'Balanced'], 0),
   ('Bias in a nonfiction text can often be detected through ___.', ['Neutral, balanced language only', 'Word choice that favours one side of an issue', 'A complete absence of any opinion', 'The colour of the text'], 1),
   ('Why is it useful for readers to analyze tone when evaluating nonfiction?', ['It helps reveal the author’s perspective and potential bias', 'Tone has no connection to bias', 'Analyzing tone replaces the need to read the whole text', 'Tone only matters in fiction'], 0),
   ('Which is an example of biased language in a news headline?', ['Reckless politician pushes dangerous new policy', 'Politician proposes new policy', 'City council reviews proposed policy', 'New policy to be discussed next week'], 0)]),
M('Ratio Tables and Scaling',
  'Ontario Grade 6 Number strand: a ratio table shows equivalent ratios by scaling a ratio up or down, keeping the relationship between the two quantities consistent.',
  [('If a recipe uses a ratio of 2 cups flour to 1 cup sugar, how much sugar is needed for 6 cups of flour?', ['2 cups', '3 cups', '4 cups', '6 cups'], 1),
   ('A ratio table shows ___.', ['Unrelated random numbers', 'Equivalent ratios scaled up or down consistently', 'Only one single ratio with no scaling', 'Data with no numeric relationship'], 1),
   ('If the ratio of red to blue marbles is 3 to 5, and there are 15 blue marbles, how many red marbles are there?', ['6', '9', '10', '12'], 1),
   ('Scaling a ratio up means ___.', ['Multiplying both quantities by the same number', 'Multiplying only one quantity', 'Subtracting from both quantities', 'Ignoring the original ratio'], 0),
   ('If a ratio table shows 1:4, 2:8, 3:12, what is the next equivalent ratio?', ['4:15', '4:16', '5:16', '4:20'], 1)]),
Sc('The Water Cycle and Its Impact on Climate',
   'Ontario Grade 6 Science Earth and Space Systems strand: the water cycle, including evaporation, condensation, and precipitation, moves water through the atmosphere and land, playing a key role in shaping regional climate.',
   [('Evaporation in the water cycle refers to ___.', ['Water changing from a liquid into a gas', 'Water freezing into ice', 'Water falling as precipitation', 'Water flowing underground only'], 0),
    ('Condensation in the water cycle refers to ___.', ['Water vapour changing into liquid water droplets', 'Ice melting into liquid water', 'Water evaporating into the air', 'Water flowing into rivers'], 0),
    ('Precipitation refers to water ___.', ['Falling from the atmosphere as rain, snow, or hail', 'Evaporating into the atmosphere', 'Freezing permanently underground', 'Disappearing completely'], 0),
    ('How does the water cycle influence regional climate?', ['It affects moisture levels and precipitation patterns in different regions', 'The water cycle has no connection to climate', 'Climate is entirely unrelated to water movement', 'The water cycle only affects ocean temperature'], 0),
    ('Why is the water cycle considered a continuous process?', ['Water constantly moves between the atmosphere, land, and oceans', 'Water only moves once and then stops permanently', 'The water cycle occurs only once a year', 'Water disappears entirely after evaporating'], 0)]),
SS('The Vikings and Early Norse Exploration',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Vikings were Norse seafarers from Scandinavia who explored, traded, and settled across parts of Europe and even reached North America around 1000 CE.',
   [('The Vikings originated from which region?', ['Scandinavia', 'North Africa', 'South America', 'East Asia'], 0),
    ('Vikings were known for their skill in ___.', ['Seafaring and exploration', 'Building pyramids', 'Desert farming', 'Space travel'], 0),
    ('Around 1000 CE, Norse explorers are believed to have reached ___.', ['North America', 'Australia', 'Antarctica', 'The Moon'], 0),
    ('In addition to exploration, Vikings were also known for ___.', ['Trade across parts of Europe', 'Having no contact with other regions', 'Avoiding travel by sea entirely', 'Building only underground cities'], 0),
    ('Why is early Norse exploration significant to world history?', ['It represents some of the earliest known European contact with North America', 'It had no historical significance', 'It occurred after Columbus’s voyages', 'Vikings never actually travelled anywhere'], 0)])]),

day(32, [
L('Writing: Compare and Contrast Essay',
  'Ontario Grade 6 Writing strand: a compare and contrast essay examines the similarities and differences between two subjects, often organized point-by-point or subject-by-subject.',
  [('A compare and contrast essay focuses on ___.', ['Only the similarities between two subjects', 'The similarities and differences between two subjects', 'A single subject only', 'A completely unrelated topic'], 1),
   ('One way to organize a compare and contrast essay is ___.', ['Point-by-point or subject-by-subject', 'Randomly with no structure', 'Only using bullet points with no essay structure', 'By ignoring one of the two subjects'], 0),
   ('Which transition word signals a contrast between ideas?', ['However', 'Similarly', 'Also', 'In addition'], 0),
   ('Which transition word signals a similarity between ideas?', ['But', 'Similarly', 'On the other hand', 'In contrast'], 1),
   ('Why might a writer choose the point-by-point structure for a compare and contrast essay?', ['It allows direct comparison of specific features between the two subjects', 'It ignores one of the subjects entirely', 'It has no organizational benefit', 'It removes the need for any comparison'], 0)]),
M('Solving Two-Step Equations',
  'Ontario Grade 6 Algebra strand: a two-step equation requires two inverse operations to isolate the variable, typically undoing addition or subtraction first, then multiplication or division.',
  [('Solve for x: 2x + 3 = 11.', ['x = 4', 'x = 7', 'x = 3', 'x = 14'], 0),
   ('Solve for y: 3y minus 5 = 10.', ['y = 5', 'y = 15', 'y = 3', 'y = 45'], 0),
   ('When solving a two-step equation, which operation is typically undone first?', ['Multiplication or division', 'Addition or subtraction', 'It does not matter at all', 'Neither operation needs to be undone'], 1),
   ('Solve for n: 4n + 8 = 24.', ['n = 4', 'n = 8', 'n = 6', 'n = 16'], 0),
   ('Solve for m: 5m minus 2 = 18.', ['m = 4', 'm = 20', 'm = 16', 'm = 3.2'], 0)]),
Sc('Sustainable Technologies and Innovation',
   'Ontario Grade 6 Science and Technology strand: sustainable technologies are designed to meet human needs while minimizing environmental impact, such as energy-efficient appliances, electric vehicles, and green building design.',
   [('Sustainable technology is designed to ___.', ['Maximize environmental harm', 'Meet human needs while minimizing environmental impact', 'Ignore environmental concerns entirely', 'Use only non-renewable resources'], 1),
    ('Which is an example of a sustainable technology?', ['An energy-efficient appliance', 'A machine designed to waste as much energy as possible', 'A device with no consideration for resource use', 'A technology banned for excessive pollution'], 0),
    ('Green building design often focuses on ___.', ['Reducing energy use and environmental impact', 'Increasing pollution and waste', 'Ignoring energy efficiency entirely', 'Using only non-renewable materials'], 0),
    ('Why might engineers prioritize sustainable innovation?', ['To help address environmental challenges while still meeting human needs', 'Sustainability has no connection to engineering', 'Sustainable design always increases environmental harm', 'There is no benefit to sustainable technology'], 0),
    ('Which of these could be considered a sustainable transportation technology?', ['An electric vehicle', 'A technology with no consideration for emissions', 'A method that ignores fuel efficiency entirely', 'None of these examples relate to sustainability'], 0)]),
SS('The Silk Road: Trade and Cultural Exchange',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Silk Road was a network of trade routes connecting Asia, the Middle East, and Europe, enabling the exchange of goods, ideas, and culture for centuries.',
   [('The Silk Road primarily connected which regions?', ['Asia, the Middle East, and Europe', 'Only North America and South America', 'Only Australia and Antarctica', 'A single isolated region with no connections'], 0),
    ('The Silk Road gets its name from ___.', ['The trade of silk and other valuable goods', 'A specific road built entirely of silk fabric', 'A single city named Silk', 'A modern highway system'], 0),
    ('Besides goods, the Silk Road also enabled the exchange of ___.', ['Ideas and culture', 'Nothing beyond physical goods', 'Only military weapons', 'Only currency'], 0),
    ('Why is the Silk Road considered historically significant?', ['It connected distant civilizations and fostered widespread cultural and economic exchange', 'It had no lasting historical impact', 'It only connected two small villages', 'It prevented any contact between civilizations'], 0),
    ('Which of these might have been traded along the Silk Road?', ['Silk, spices, and other goods', 'Nothing of value', 'Only modern electronics', 'Only currency with no physical goods'], 0)])]),

day(33, [
L('Grammar: Parallel Structure in Writing',
  'Ontario Grade 6 Writing strand: parallel structure means using the same grammatical pattern for related items in a sentence, such as in a list, to create clarity and rhythm.',
  [('Parallel structure means ___.', ['Using different grammatical patterns for related items', 'Using the same grammatical pattern for related items', 'Avoiding lists in writing entirely', 'Using only single-word sentences'], 1),
   ('Which sentence uses correct parallel structure?', ['She likes running, swimming, and to bike.', 'She likes running, swimming, and biking.', 'She likes to run, swimming, and biking.', 'She likes running, to swim, and biking.'], 1),
   ('Why is parallel structure important in writing?', ['It creates clarity and a smoother rhythm in sentences', 'It makes sentences more confusing', 'Parallel structure has no effect on writing quality', 'It should always be avoided in lists'], 0),
   ('Which sentence lacks parallel structure?', ['He enjoys reading, writing, and painting.', 'He enjoys to read, writing, and painting.', 'He enjoys reading, writing, and painting each day.', 'Reading, writing, and painting are his hobbies.'], 1),
   ('Parallel structure is especially useful when writing ___.', ['A list of related items or actions', 'A single isolated word', 'Random unrelated ideas', 'A sentence with no verbs'], 0)]),
M('Surface Area of Rectangular Prisms',
  'Ontario Grade 6 Geometry strand: the surface area of a rectangular prism is found by calculating the area of all six faces and adding them together.',
  [('The surface area of a 3D shape refers to ___.', ['The total area of all its outer faces', 'The space inside the shape', 'Only the area of one face', 'The shape’s weight'], 0),
   ('A rectangular prism has how many faces?', ['4', '6', '8', '12'], 1),
   ('If a rectangular prism’s six faces have areas of 20, 20, 15, 15, 12, and 12 square units, what is its total surface area?', ['47 square units', '94 square units', '82 square units', '74 square units'], 1),
   ('Surface area is measured in ___ units.', ['Cubic', 'Linear', 'Square', 'Degree'], 2),
   ('Why might it be useful to calculate the surface area of a box, such as when wrapping a gift?', ['It helps determine how much wrapping material is needed to cover it', 'Surface area has no practical use', 'Surface area only matters for spheres', 'It tells you how much the box weighs'], 0)]),
Sc('Cells: The Building Blocks of Life',
   'Ontario Grade 6 Science Life Systems strand: cells are the basic structural and functional units of all living things, and organisms can be made of a single cell or trillions of cells working together.',
   [('Cells are considered the ___.', ['Basic structural and functional units of all living things', 'Largest structures in the universe', 'Only found in plants', 'Non-living materials'], 0),
    ('An organism made up of only one cell is called ___.', ['Multicellular', 'Unicellular', 'Non-living', 'Inorganic'], 1),
    ('Human beings are made up of ___.', ['A single cell only', 'Trillions of cells working together', 'No cells at all', 'Exactly one hundred cells'], 1),
    ('Why are cells considered essential to understanding living things?', ['All living organisms are built from and function through cells', 'Cells have no connection to living organisms', 'Only some living things are made of cells', 'Cells are found only in non-living matter'], 0),
    ('Which of these is an example of a unicellular organism?', ['Bacteria', 'A human being', 'An elephant', 'A tree'], 0)]),
SS('The Islamic Golden Age',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Islamic Golden Age was a period of significant advances in science, medicine, mathematics, and culture across the Islamic world, roughly from the 8th to 14th centuries.',
   [('The Islamic Golden Age is associated with major advances in fields such as ___.', ['Science, medicine, and mathematics', 'Nothing of lasting significance', 'Only military conquest', 'Only architecture with no other achievements'], 0),
    ('Roughly during which centuries did the Islamic Golden Age take place?', ['1st to 3rd centuries', '8th to 14th centuries', '18th to 20th centuries', 'It never took place'], 1),
    ('Scholars during the Islamic Golden Age made contributions that influenced ___.', ['Later scientific and mathematical developments worldwide', 'No other regions or time periods', 'Only local, isolated communities', 'Nothing related to science'], 0),
    ('Why is the Islamic Golden Age considered an important period in world history?', ['It produced lasting achievements in science, medicine, and scholarship', 'It had no lasting impact on world history', 'It involved no scholarly or scientific work', 'It occurred entirely in modern times'], 0),
    ('Centres of learning during the Islamic Golden Age often focused on preserving and expanding knowledge in ___.', ['Multiple fields, including mathematics and astronomy', 'No academic fields at all', 'Only entertainment', 'Only sports'], 0)])]),

day(34, [
L('Vocabulary: Word Origins and Etymology',
  'Ontario Grade 6 Language strand: many English words originate from Latin, Greek, French, or other languages, and understanding a word’s etymology can help clarify its meaning and spelling.',
  [('Etymology is the study of ___.', ['A word’s origin and history', 'A word’s length only', 'How to pronounce a word', 'A word’s font style'], 0),
   ('Many English words have roots in which languages?', ['Latin, Greek, and French', 'Only modern English', 'No other languages at all', 'Only invented, fictional languages'], 0),
   ('Understanding a word’s etymology can help readers ___.', ['Clarify its meaning and spelling', 'Ignore the word entirely', 'Make the word harder to understand', 'Change the word’s actual meaning randomly'], 0),
   ('The word aquarium comes from the Latin root aqua, meaning ___.', ['Fire', 'Water', 'Earth', 'Air'], 1),
   ('Why might studying etymology help build a stronger vocabulary?', ['Recognizing common roots helps decode the meaning of unfamiliar words', 'Etymology has no connection to vocabulary building', 'Word origins are unrelated to word meaning', 'Etymology only applies to very short words'], 0)]),
M('Circles: Circumference and Area',
  'Ontario Grade 6 Geometry strand: the circumference of a circle is found using pi times the diameter, while the area is found using pi times the radius squared.',
  [('The formula for the circumference of a circle is ___.', ['Pi times the diameter', 'Pi times the radius squared', 'Radius times height', 'Diameter divided by pi'], 0),
   ('The formula for the area of a circle is ___.', ['Pi times the diameter', 'Pi times the radius squared', 'Two times pi times radius', 'Radius times diameter'], 1),
   ('If a circle has a radius of 4 cm, which formula would you use to find its area?', ['Pi times 4 squared', 'Pi times 4', 'Pi times 8', '4 times 4'], 0),
   ('The value of pi is approximately ___.', ['1.14', '3.14', '4.13', '2.71'], 1),
   ('If a circle’s diameter is 10 cm, what expression represents its circumference?', ['Pi times 10', 'Pi times 5 squared', 'Pi times 20', '10 divided by pi'], 0)]),
Sc('Microorganisms: Bacteria, Viruses, and Fungi',
   'Ontario Grade 6 Science Life Systems strand: microorganisms, including bacteria, viruses, and fungi, are tiny living or non-living particles that can be helpful, such as in digestion, or harmful, such as causing illness.',
   [('Which of these is classified as a microorganism?', ['Bacteria', 'An elephant', 'A whale', 'A large tree'], 0),
    ('Some bacteria can be helpful to humans by ___.', ['Aiding in digestion', 'Always causing severe illness with no exceptions', 'Having no role in the human body', 'Destroying all food sources'], 0),
    ('Viruses differ from bacteria in that viruses ___.', ['Are generally not considered fully living on their own and need a host to reproduce', 'Are always larger than bacteria', 'Can never cause illness', 'Are visible without a microscope'], 0),
    ('Fungi, such as mushrooms and mould, can play a role in ___.', ['Breaking down dead organic material', 'Preventing all decomposition', 'Only causing harm with no other roles', 'Producing electricity'], 0),
    ('Why are microorganisms studied in science, despite being too small to see with the naked eye?', ['They play significant roles in health, ecosystems, and disease', 'Microorganisms have no impact on living things', 'They are not considered part of biology', 'Studying microorganisms serves no purpose'], 0)]),
SS('Feudal Japan: Samurai and Shogunate',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: feudal Japan was organized around a strict social hierarchy, with a shogun holding military power and samurai warriors serving as loyal, skilled fighters bound by a code of honour.',
   [('In feudal Japan, the shogun held ___.', ['No power at all', 'Significant military power', 'Only religious authority', 'No connection to government'], 1),
    ('Samurai were known as ___.', ['Skilled warriors bound by a code of honour', 'Farmers with no military role', 'Foreign traders', 'Government officials with no military training'], 0),
    ('Feudal Japan was organized around a ___.', ['Strict social hierarchy', 'Complete lack of social structure', 'A system with no leaders', 'A structure identical to modern Japan'], 0),
    ('The samurai code of honour emphasized values such as ___.', ['Loyalty and discipline', 'Dishonesty and disorder', 'Avoiding all responsibility', 'Ignoring any code of conduct'], 0),
    ('Why is feudal Japan studied as part of world history?', ['It offers insight into a distinct social and political system that shaped Japanese history', 'It has no historical significance', 'Feudal Japan never actually existed', 'It is identical to feudal systems everywhere else'], 0)])]),

day(35, [
L('Reading: Annotating and Active Reading Strategies',
  'Ontario Grade 6 Reading strand: active reading strategies, such as annotating a text with notes, questions, and highlights, help readers stay engaged and better understand and remember what they read.',
  [('Annotating a text involves ___.', ['Adding notes, questions, or highlights while reading', 'Ignoring the text completely', 'Reading without any interaction with the text', 'Skipping directly to the last page'], 0),
   ('Active reading strategies are designed to help readers ___.', ['Stay engaged and better understand the text', 'Read as quickly as possible with no comprehension', 'Avoid thinking about the text', 'Forget the content immediately after reading'], 0),
   ('Which is an example of an active reading strategy?', ['Underlining key ideas and writing questions in the margins', 'Reading with no attention to the content', 'Skipping the entire text', 'Reading only the cover of the book'], 0),
   ('Why might a reader pause to ask questions while reading a challenging text?', ['To check their understanding and clarify confusing parts', 'Questions have no value while reading', 'Pausing always disrupts understanding', 'Questions should only be asked after finishing the entire book'], 0),
   ('Annotating can help readers later ___.', ['Quickly locate important information when reviewing the text', 'Forget the content of what they read', 'Avoid returning to the text at all', 'Make the text impossible to understand'], 0)]),
M('Constructing Circle Graphs',
  'Ontario Grade 6 Data Management strand: constructing a circle graph involves calculating what percentage each category represents of the whole data set, then dividing the circle into matching proportional sections.',
  [('To construct a circle graph, you first need to calculate each category’s ___.', ['Percentage of the total data set', 'Exact colour', 'Alphabetical order', 'Distance from the centre'], 0),
   ('If a category makes up 25 percent of the data, its slice of the circle graph should represent ___.', ['25 percent of the full circle', '50 percent of the full circle', '100 percent of the full circle', '10 percent of the full circle'], 0),
   ('A full circle graph represents ___ percent of the total data.', ['50', '75', '100', '200'], 2),
   ('Why might a circle graph be a good choice for showing survey results?', ['It visually shows how each response compares to the whole', 'Circle graphs cannot represent percentages', 'Circle graphs are never useful for surveys', 'They only work with negative numbers'], 0),
   ('If two categories in a data set are equal in size, their slices on the circle graph should be ___.', ['Different sizes', 'The same size', 'Impossible to draw', 'One larger than 100 percent'], 1)]),
Sc('Natural Disasters: Earthquakes and Volcanoes',
   'Ontario Grade 6 Science Earth and Space Systems strand: earthquakes and volcanoes are natural events often caused by the movement of tectonic plates, and understanding their causes helps communities prepare and stay safe.',
   [('Earthquakes are often caused by ___.', ['The movement of tectonic plates', 'Changes in the weather only', 'Ocean tides', 'Nothing related to Earth’s structure'], 0),
    ('A volcano erupts when ___.', ['Magma and gases are released from beneath Earth’s surface', 'It only produces cold water', 'Tectonic plates disappear entirely', 'No pressure builds up inside Earth'], 0),
    ('Areas along tectonic plate boundaries often experience more ___.', ['Earthquake and volcanic activity', 'Stability with no natural events', 'No connection to geological activity', 'Only mild weather changes'], 0),
    ('Why is it important for communities in earthquake-prone areas to prepare in advance?', ['Preparation can help reduce risk to people and property when an earthquake occurs', 'Preparation has no benefit for earthquake safety', 'Earthquakes never cause any damage', 'Communities cannot take any useful precautions'], 0),
    ('Scientists who study earthquakes are called ___.', ['Seismologists', 'Meteorologists', 'Astronomers', 'Botanists'], 0)]),
SS('The Cold War: Origins and Key Events',
   'Ontario Grade 6 Social Studies Heritage and Identity strand: the Cold War was a long period of political tension after World War II, mainly between the United States and the Soviet Union, involving competition without direct large-scale warfare between the two powers.',
   [('The Cold War took place mainly after which major global conflict?', ['World War I', 'World War II', 'The War of 1812', 'The American Revolution'], 1),
    ('The Cold War was primarily a period of tension between the United States and ___.', ['The Soviet Union', 'Canada', 'France', 'Japan'], 0),
    ('Unlike many other wars, the Cold War did not involve ___.', ['Political tension', 'Direct large-scale warfare between the two main powers', 'Competition between countries', 'Any historical significance'], 1),
    ('Why is the Cold War considered an important period in 20th-century history?', ['It shaped global politics and international relationships for decades', 'It had no lasting effect on world history', 'It occurred before World War I', 'It involved no international tension at all'], 0),
    ('The term Cold War reflects the idea that the conflict was mostly ___.', ['Fought through direct military battles only', 'Political and indirect, rather than direct warfare between the major powers', 'Entirely unrelated to politics', 'A conflict that never actually happened'], 1)])]),

day(36, [
L('Writing: Crafting a Strong Thesis Statement',
  'Ontario Grade 6 Writing strand: a thesis statement clearly presents the main argument or focus of an essay, usually appearing near the end of the introduction, and guides the structure of the entire piece.',
  [('A thesis statement is best described as ___.', ['A statement that presents the main argument or focus of an essay', 'A random unrelated fact', 'The very last sentence of the conclusion only', 'A list of unrelated topics'], 0),
   ('A thesis statement typically appears ___.', ['At the very end of the essay only', 'Near the end of the introduction', 'In the middle of a random body paragraph', 'Nowhere in a well-organized essay'], 1),
   ('Why is a strong thesis statement important?', ['It guides the structure and focus of the entire essay', 'It has no connection to the rest of the essay', 'A thesis statement should always be vague and unclear', 'It replaces the need for any supporting evidence'], 0),
   ('Which is an example of a strong, specific thesis statement?', ['Recess should be extended because it improves student focus and physical health.', 'Recess is a thing that happens at school.', 'Some people like recess.', 'This essay is about school.'], 0),
   ('A weak thesis statement is often ___.', ['Too vague or broad to guide the essay effectively', 'Extremely specific and well-supported', 'Always placed in the conclusion', 'Unnecessary for any essay'], 0)]),
M('Financial Literacy: Budgets and Percent Discounts',
  'Ontario Grade 6 Financial Literacy strand: a budget tracks income and expenses, and percent discounts reduce an item’s price by a specific percentage, useful for comparing sale prices and managing spending.',
  [('A budget helps track ___.', ['Income and expenses', 'Only expenses, never income', 'Nothing related to money', 'Only savings with no other categories'], 0),
   ('If an item originally costs $80 and is 25 percent off, what is the discount amount?', ['$10', '$20', '$25', '$60'], 1),
   ('If an item originally costs $80 and is 25 percent off, what is the final sale price?', ['$20', '$55', '$60', '$65'], 2),
   ('Why is it useful to calculate percent discounts before making a purchase?', ['It helps determine the actual amount you will pay and compare deals', 'Percent discounts have no effect on the final price', 'Discounts are always irrelevant to shopping decisions', 'Calculating discounts wastes time with no benefit'], 0),
   ('If a $50 item is discounted by 10 percent, what is the new price?', ['$5', '$40', '$45', '$55'], 2)]),
Sc('Genetics and Heredity: Introduction',
   'Ontario Grade 6 Science Life Systems strand: heredity is the passing of traits from parents to offspring through genes, which are segments of DNA that carry instructions for an organism’s characteristics.',
   [('Heredity refers to ___.', ['The passing of traits from parents to offspring', 'A type of weather pattern', 'A type of rock formation', 'A process unrelated to living things'], 0),
    ('Genes are best described as ___.', ['Segments of DNA that carry instructions for traits', 'A type of cell found only in plants', 'A part of the digestive system', 'A type of chemical unrelated to biology'], 0),
    ('Offspring often inherit traits from ___.', ['Their parents', 'No one at all', 'A completely random, unrelated source', 'Only their environment, with no genetic influence'], 0),
    ('Which is an example of an inherited trait?', ['Eye colour', 'A learned skill like playing an instrument', 'A scar from an injury', 'A haircut style'], 0),
    ('Why is understanding heredity useful in science?', ['It helps explain how traits are passed between generations', 'Heredity has no connection to biology', 'Heredity only applies to plants, never animals', 'Understanding heredity serves no scientific purpose'], 0)]),
SS('The United Nations and International Cooperation',
   'Ontario Grade 6 Social Studies People and Environments strand: the United Nations is an international organization formed after World War II to promote peace, cooperation, and human rights among countries around the world.',
   [('The United Nations was formed after which major event?', ['World War I', 'World War II', 'The Cold War began', 'The Renaissance'], 1),
    ('One of the main goals of the United Nations is to promote ___.', ['Conflict between countries', 'Peace and cooperation among nations', 'Isolation of all countries from each other', 'The end of all international organizations'], 1),
    ('The United Nations includes member countries from ___.', ['Around the world', 'Only North America', 'Only Europe', 'No countries at all'], 0),
    ('Why might countries choose to work together through an organization like the United Nations?', ['To address global challenges more effectively through cooperation', 'Cooperation between countries serves no purpose', 'Countries are never able to work together', 'International organizations have no real function'], 0),
    ('Which is an example of an issue the United Nations might address?', ['International peace and human rights', 'Only issues within a single country', 'No global issues at all', 'Only issues unrelated to international relations'], 0)])]),

day(37, [
L('Media Literacy: Deconstructing Social Media Messages',
  'Ontario Grade 6 Media Literacy strand: deconstructing a social media message means identifying its purpose, intended audience, and the techniques used to grab attention or persuade, such as headlines or images.',
  [('Deconstructing a media message involves ___.', ['Ignoring the message entirely', 'Identifying its purpose, audience, and persuasive techniques', 'Accepting all information without question', 'Avoiding all analysis of the message'], 1),
   ('Which is a technique social media posts might use to grab attention?', ['A bold headline or striking image', 'Completely plain, unformatted text with no visuals', 'Avoiding any visual elements', 'Ignoring the audience entirely'], 0),
   ('Why is it useful to identify the purpose behind a social media message?', ['It helps viewers understand what the creator wants them to think, feel, or do', 'Purpose has no connection to how a message is created', 'All social media messages have no clear purpose', 'Identifying purpose is not a useful skill'], 0),
   ('Considering the intended audience of a message can help you understand ___.', ['Why certain content or language choices were used', 'Nothing useful about the message', 'Only the exact time it was posted', 'The message’s file size'], 0),
   ('Which question is useful when critically evaluating a social media post?', ['Who created this, and why?', 'What font is being used?', 'How many emojis are included?', 'What time zone was it posted in?'], 0)]),
M('Coordinate Geometry: Plotting and Interpreting Points',
  'Ontario Grade 6 Geometry strand: plotting and interpreting points on a coordinate grid involves using ordered pairs to locate positions and analyze relationships, such as distances between points on the same horizontal or vertical line.',
  [('To plot the point (5, 2), you move ___.', ['5 units up, 2 units across', '5 units across, 2 units up', '2 units across, 5 units down', '2 units up, 5 units left'], 1),
   ('Two points with the same y-coordinate lie on the same ___ line.', ['Vertical', 'Horizontal', 'Diagonal', 'Curved'], 1),
   ('What is the distance between the points (2, 3) and (7, 3)?', ['3 units', '5 units', '7 units', '10 units'], 1),
   ('Two points with the same x-coordinate lie on the same ___ line.', ['Horizontal', 'Vertical', 'Diagonal', 'Curved'], 1),
   ('An ordered pair like (4, 6) is written in the order ___.', ['(y, x)', '(x, y)', 'Alphabetical order', 'Random order'], 1)]),
Sc('Chemical Reactions in Everyday Life',
   'Ontario Grade 6 Science Matter and Energy strand: chemical reactions occur regularly in everyday life, such as cooking, digestion, and rusting, producing new substances with properties different from the original materials.',
   [('Which everyday activity involves a chemical reaction?', ['Cooking an egg', 'Folding a piece of paper', 'Cutting a piece of string', 'Stacking blocks'], 0),
    ('Rusting is an example of a chemical reaction between metal and ___.', ['Oxygen and moisture', 'Sunlight only', 'Sound waves', 'Cold temperatures alone'], 0),
    ('Digestion involves chemical reactions that help the body ___.', ['Break down food into usable nutrients', 'Prevent any nutrients from being absorbed', 'Avoid processing food entirely', 'Only physically chop food with no chemical process'], 0),
    ('A chemical reaction produces substances with properties that are ___ the original materials.', ['Identical to', 'Different from', 'Unrelated to any material properties', 'Impossible to observe'], 1),
    ('Why is it useful to recognize chemical reactions in daily life?', ['It helps explain many common processes we observe and rely on', 'Chemical reactions never occur in daily life', 'Recognizing reactions serves no practical purpose', 'Chemical reactions only happen in laboratories'], 0)]),
SS('Human Rights: The Universal Declaration',
   'Ontario Grade 6 Social Studies People and Environments strand: the Universal Declaration of Human Rights, adopted by the United Nations in 1948, outlines fundamental rights and freedoms believed to belong to all people.',
   [('The Universal Declaration of Human Rights was adopted in which year?', ['1918', '1948', '1982', '2000'], 1),
    ('The Universal Declaration of Human Rights was adopted by ___.', ['The United Nations', 'A single country acting alone', 'No formal organization', 'A private company'], 0),
    ('The document outlines rights and freedoms believed to belong to ___.', ['Only citizens of one country', 'All people', 'No one in particular', 'Only government officials'], 1),
    ('Why is the Universal Declaration of Human Rights considered historically significant?', ['It established a shared international standard for basic human rights', 'It has no connection to international law or standards', 'It was created before the United Nations existed', 'It applies to no countries at all'], 0),
    ('Which is an example of a right commonly recognized under human rights frameworks?', ['Freedom of expression', 'The right to ignore all laws', 'The right to harm others without consequence', 'No rights are recognized internationally'], 0)])]),

day(38, [
L('Grammar: Using Semicolons and Colons',
  'Ontario Grade 6 Writing strand: a semicolon can join two closely related independent clauses, while a colon introduces a list, explanation, or example following a complete sentence.',
  [('A semicolon can be used to ___.', ['End a sentence permanently', 'Join two closely related independent clauses', 'Replace all commas in a sentence', 'Begin every sentence'], 1),
   ('A colon is often used to ___.', ['Introduce a list or explanation after a complete sentence', 'Replace a period at random points', 'Separate unrelated ideas with no connection', 'Begin a sentence'], 0),
   ('Which sentence correctly uses a semicolon?', ['I love reading; it helps me relax.', 'I love reading, it helps me relax;', 'I love reading; it, helps me relax.', 'I love; reading it helps me relax.'], 0),
   ('Which sentence correctly uses a colon?', ['I need three things: pencils, paper, and erasers.', 'I need three things, pencils: paper, and erasers.', 'I need: three things pencils, paper, and erasers.', 'I need three things pencils, paper: and erasers.'], 0),
   ('Why might a writer choose a semicolon instead of starting a new sentence?', ['To show a close relationship between two related ideas', 'Semicolons have no specific grammatical purpose', 'Semicolons should always be avoided', 'To make two unrelated ideas seem connected'], 0)]),
M('Divisibility Rules and Prime Factorization',
  'Ontario Grade 6 Number strand: divisibility rules help quickly determine if a number can be evenly divided by another, and prime factorization breaks a number down into the prime numbers that multiply to form it.',
  [('Which divisibility rule correctly applies to the number 2?', ['A number is divisible by 2 if its last digit is even', 'A number is divisible by 2 if it ends in 5', 'A number is divisible by 2 only if it is odd', 'There is no rule for divisibility by 2'], 0),
   ('Which divisibility rule correctly applies to the number 5?', ['A number is divisible by 5 if it ends in 0 or 5', 'A number is divisible by 5 if it ends in 2 or 4', 'A number is divisible by 5 if it is even', 'There is no rule for divisibility by 5'], 0),
   ('What is the prime factorization of 12?', ['2 x 2 x 3', '2 x 6', '3 x 4', '1 x 12'], 0),
   ('A prime number is a number that ___.', ['Has exactly two factors: 1 and itself', 'Can be divided evenly by many numbers', 'Is always an even number', 'Has no factors at all'], 0),
   ('What is the prime factorization of 18?', ['2 x 3 x 3', '2 x 9', '3 x 6', '1 x 18'], 0)]),
Sc('Renewable Energy: Solar, Wind, and Hydro Technologies',
   'Ontario Grade 6 Science Matter and Energy strand: technologies like solar panels, wind turbines, and hydroelectric dams harness renewable natural energy sources to generate electricity with reduced environmental impact.',
   [('Solar panel technology captures energy from ___.', ['Sunlight', 'Wind', 'Underground heat only', 'Ocean tides only'], 0),
    ('Wind turbine technology captures energy from ___.', ['Sunlight', 'The motion of wind', 'Underground heat', 'Coal combustion'], 1),
    ('Hydroelectric technology generates electricity using the movement of ___.', ['Water', 'Wind', 'Sunlight', 'Coal'], 0),
    ('A key advantage of renewable energy technologies is that they ___.', ['Rely on sources that can be naturally replenished', 'Always run out permanently after one use', 'Have no environmental benefits at all', 'Cannot generate any usable electricity'], 0),
    ('Why might a community choose to invest in renewable energy technologies?', ['To reduce reliance on non-renewable resources and lower environmental impact', 'Renewable technologies provide no benefits', 'They always increase pollution significantly', 'There is no reason to consider renewable energy'], 0)]),
SS('Globalization and Its Effects on Canada',
   'Ontario Grade 6 Social Studies People and Environments strand: globalization is the increasing connection between countries through trade, technology, and culture, which affects Canada’s economy and daily life in various ways.',
   [('Globalization refers to ___.', ['The increasing connection between countries through trade and technology', 'Countries becoming completely isolated from each other', 'A decrease in international trade', 'Nothing related to international connections'], 0),
    ('Which is an example of globalization’s effect on Canada?', ['Access to products manufactured in other countries', 'Complete isolation from world markets', 'No connection to international trade', 'A total absence of foreign products'], 0),
    ('Globalization can affect Canada’s economy by ___.', ['Creating both opportunities and challenges through international trade', 'Having no effect on the economy at all', 'Eliminating all trade between countries', 'Preventing any international business activity'], 0),
    ('Technology has contributed to globalization by ___.', ['Making communication and trade between countries faster and easier', 'Making international communication impossible', 'Having no connection to global trade', 'Isolating countries from each other'], 0),
    ('Why is it useful for students to understand globalization?', ['It helps explain how interconnected the modern world has become', 'Globalization has no relevance to daily life', 'Countries no longer interact with each other', 'It has no connection to Canada’s economy'], 0)])]),

day(39, [
L('Writing: Effective Introductions and Conclusions',
  'Ontario Grade 6 Writing strand: a strong introduction grabs the reader’s attention and previews the main idea, while an effective conclusion summarizes key points and leaves a lasting impression.',
  [('A strong introduction should ___.', ['Grab the reader’s attention and preview the main idea', 'Contain no information about the topic', 'Always be the shortest part of the essay', 'Repeat the conclusion word for word'], 0),
   ('An effective conclusion typically ___.', ['Summarizes key points and leaves a lasting impression', 'Introduces a brand new, unrelated topic', 'Contains no connection to the rest of the essay', 'Simply repeats the introduction exactly'], 0),
   ('Which is a common technique used to grab attention in an introduction?', ['Starting with a compelling question or interesting fact', 'Beginning with unrelated information', 'Avoiding any connection to the topic', 'Starting with the exact same sentence as the conclusion'], 0),
   ('Why is it important for an introduction to preview the main idea?', ['It helps the reader understand what the piece of writing will be about', 'Previewing the main idea makes writing worse', 'Readers should never know the main idea in advance', 'It replaces the need for any body paragraphs'], 0),
   ('Why might an essay end with a strong final thought or call to action?', ['To leave a lasting, memorable impression on the reader', 'Endings have no effect on how a reader remembers an essay', 'A strong ending is never necessary', 'It should always contradict the essay’s main argument'], 0)]),
M('Converting Between Metric Units',
  'Ontario Grade 6 Measurement strand: converting between metric units, such as millimetres, centimetres, metres, and kilometres, involves multiplying or dividing by powers of ten based on the relationship between the units.',
  [('How many millimetres are in 1 centimetre?', ['1', '10', '100', '1,000'], 1),
   ('How many metres are in 1 kilometre?', ['10', '100', '1,000', '10,000'], 2),
   ('Convert 4,500 metres to kilometres.', ['0.45 km', '4.5 km', '45 km', '450 km'], 1),
   ('Convert 2 metres to centimetres.', ['20 cm', '200 cm', '2,000 cm', '2 cm'], 1),
   ('To convert from a smaller metric unit to a larger one, you typically ___.', ['Multiply', 'Divide', 'Always add 100', 'Always subtract 100'], 1)]),
Sc('The Carbon Cycle and Its Role in Climate',
   'Ontario Grade 6 Science Earth and Space Systems strand: the carbon cycle describes how carbon moves between the atmosphere, oceans, land, and living things, playing a key role in regulating Earth’s climate.',
   [('The carbon cycle describes how carbon moves between ___.', ['The atmosphere, oceans, land, and living things', 'Only outer space', 'Nowhere, since carbon never moves', 'Only underground rock layers'], 0),
    ('Plants absorb carbon dioxide from the atmosphere during ___.', ['Photosynthesis', 'Respiration only', 'Erosion', 'Evaporation'], 0),
    ('Burning fossil fuels releases stored carbon into the ___.', ['Atmosphere', 'Ocean floor only', 'Nowhere at all', 'Only underground reservoirs'], 0),
    ('Why is the carbon cycle closely connected to Earth’s climate?', ['Carbon dioxide levels in the atmosphere can affect global temperatures', 'Carbon has no connection to climate', 'The carbon cycle only affects ocean colour', 'Climate is entirely unrelated to atmospheric gases'], 0),
    ('Which human activity significantly affects the natural carbon cycle?', ['Burning fossil fuels', 'Reading books', 'Painting a picture', 'Playing a musical instrument'], 0)]),
SS('Indigenous Peoples’ Rights Movements in Canada',
   'Ontario Grade 6 Social Studies People and Environments strand: Indigenous peoples in Canada have organized rights movements over many decades to advocate for land rights, self-government, and recognition of treaty rights.',
   [('Indigenous rights movements in Canada have advocated for issues such as ___.', ['Land rights and self-government', 'Nothing of significance', 'The elimination of all Indigenous rights', 'Issues unrelated to Indigenous communities'], 0),
    ('Treaty rights refer to ___.', ['Rights established through historical agreements between Indigenous nations and governments', 'Rights that have no legal basis', 'Rights that apply only to non-Indigenous people', 'Agreements that were never actually made'], 0),
    ('Why have Indigenous rights movements been important in Canadian history?', ['They have brought attention to important issues of justice, land, and self-determination', 'These movements have had no impact on Canadian society', 'Indigenous rights have never been a topic of discussion', 'Rights movements have no connection to treaty agreements'], 0),
    ('Self-government, as discussed in Indigenous rights movements, refers to ___.', ['A community’s authority to govern its own affairs', 'Complete removal of any community authority', 'Government control with no Indigenous involvement', 'A concept unrelated to Indigenous communities'], 0),
    ('Learning about Indigenous rights movements helps students understand ___.', ['Ongoing efforts toward justice and reconciliation in Canada', 'That these issues have no relevance today', 'That Indigenous communities have no history of advocacy', 'That rights movements only occurred outside Canada'], 0)])]),

day(40, [
L('Reading: Evaluating an Author’s Credibility and Perspective',
  'Ontario Grade 6 Reading strand: evaluating an author’s credibility involves considering their expertise, potential motives, and perspective, which can shape how information in a text is presented.',
  [('Evaluating an author’s credibility involves considering ___.', ['Their expertise and potential motives', 'Only the length of their writing', 'The colour of the book cover', 'Nothing related to the author at all'], 0),
   ('An author’s perspective can shape ___.', ['How information in a text is presented', 'Nothing about how a text is written', 'Only the font used in the text', 'The exact number of pages in a book'], 0),
   ('Why might an author’s expertise on a topic matter to readers?', ['Expertise can affect how reliable and accurate their information is likely to be', 'Expertise never has any effect on reliability', 'All authors are equally credible on every topic', 'Readers should never consider an author’s background'], 0),
   ('Which might be a sign that an author has a strong personal bias on a topic?', ['Presenting only one extreme viewpoint with no acknowledgment of others', 'Citing multiple credible sources', 'Presenting balanced perspectives', 'Including relevant supporting evidence'], 0),
   ('Why is it valuable to compare texts written by authors with different perspectives?', ['It offers a more complete and balanced understanding of a topic', 'Comparing perspectives has no value for readers', 'Only one perspective should ever be considered', 'Different perspectives always contain no useful information'], 0)]),
M('Review: Ratios, Equations, Geometry, and Number Sense',
  'Ontario Grade 6 Number and Geometry strands review: this lesson revisits ratio tables, two-step equations, circle circumference and area, surface area, and divisibility and prime factorization from recent lessons.',
  [('If a ratio is 2 to 3 and scaled up to have 6 as the first term, what is the second term?', ['6', '9', '12', '3'], 1),
   ('Solve for x: 3x + 4 = 19.', ['x = 5', 'x = 15', 'x = 23', 'x = 3'], 0),
   ('What is the circumference formula for a circle?', ['Pi times diameter', 'Pi times radius squared', 'Length times width', 'Radius times height'], 0),
   ('What is the prime factorization of 20?', ['2 x 2 x 5', '2 x 10', '4 x 5', '1 x 20'], 0),
   ('Why is it useful to review ratios, equations, geometry, and number sense together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Cells, Microorganisms, Genetics, and Earth Systems',
   'Ontario Grade 6 Science review: this lesson revisits cells, microorganisms, genetics and heredity, natural disasters, and the water and carbon cycles covered across recent lessons.',
   [('Which are considered the basic building blocks of living things?', ['Cells', 'Rocks', 'Clouds', 'Rivers'], 0),
    ('Which type of microorganism generally needs a host to reproduce?', ['A virus', 'A plant', 'A large mammal', 'A rock'], 0),
    ('Heredity involves the passing of traits through ___.', ['Genes', 'Weather patterns', 'Rock formations', 'Ocean currents'], 0),
    ('Earthquakes are commonly linked to the movement of ___.', ['Tectonic plates', 'Ocean currents only', 'Clouds', 'Ratios'], 0),
    ('Why is it valuable to review cells, microorganisms, genetics, and Earth systems together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: World History and Global Cooperation',
   'Ontario Grade 6 Social Studies review: this lesson revisits the Vikings, the Silk Road, the Islamic Golden Age, feudal Japan, the Cold War, the United Nations, human rights, globalization, and Indigenous rights movements.',
   [('Which group of Norse seafarers explored and traded across parts of Europe and reached North America?', ['The Vikings', 'The Romans', 'The Aztecs', 'The Mongols'], 0),
    ('Which network of trade routes connected Asia, the Middle East, and Europe?', ['The Silk Road', 'The Cold War', 'The United Nations', 'A modern highway system'], 0),
    ('Which international organization was formed after World War II to promote peace and cooperation?', ['The United Nations', 'A single country’s government', 'A private business', 'A local municipal council'], 0),
    ('The Universal Declaration of Human Rights outlines rights believed to belong to ___.', ['All people', 'Only government leaders', 'No one in particular', 'Only citizens of one country'], 0),
    ('Why is it useful to review world history and global cooperation topics together?', ['It helps reinforce how historical events and international cooperation connect over time', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260715):
    """Same technique used for the earlier Phase 3 batches -- reassigns
    each question's correct-answer slot via a shuffled round-robin (even
    across 0-3) and shuffles the wrong options into the remaining slots.
    Question and option TEXT is never changed. Mutates `days` in place."""
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


if __name__ == '__main__':
    _rebalance_answer_positions(g6_31_40)
    append_to(6, g6_31_40)
