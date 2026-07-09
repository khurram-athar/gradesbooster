#!/usr/bin/env python3
"""Phase 3: Grade 5, Days 41-50 (second Grade 5 batch, continuing the
10-day pattern). Topics chosen to avoid any overlap with the existing Day
1-40 set (see data/grade5.json after the Days 31-40 batch): setting/mood,
symbolism, unit rates, circles, the skeletal/muscular/excretory systems,
compound machines, and 20th-century Canadian constitutional history (the
Statute of Westminster, the 1982 Constitution Act and Charter, the Great
Depression, and the Truth and Reconciliation Commission).

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

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science & Technology',
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


g5_41_50 = [
day(41, [
L('Reading: Analyzing Setting and Mood',
  'Ontario Grade 5 Reading strand: setting is the time and place of a story, and mood is the feeling or atmosphere the setting and word choice create for the reader.',
  [('Setting refers to ___.', ['The time and place of a story', 'The main character’s name', 'The book’s title', 'The number of chapters'], 0),
   ('Mood refers to ___.', ['The feeling or atmosphere created for the reader', 'The exact page count', 'The author’s home address', 'The font used in the book'], 0),
   ('A dark, stormy setting with creaking floors would likely create a ___ mood.', ['Cheerful', 'Tense or eerie', 'Silly', 'Relaxed'], 1),
   ('Which technique might an author use to build a peaceful mood?', ['Describing a quiet meadow with soft sunlight', 'Describing a loud, chaotic battle', 'Using only dialogue with no description', 'Listing random unrelated facts'], 0),
   ('Why is setting closely connected to mood?', ['Details about time and place often shape the emotional atmosphere of a scene', 'Setting and mood are always unrelated', 'Mood only comes from character names', 'Setting has no effect on how a reader feels'], 0)]),
M('Unit Rates',
  'Ontario Grade 5 Number strand: a unit rate compares a quantity to one unit of another quantity, such as kilometres per hour or price per item, making it easier to compare different options.',
  [('If a car travels 300 kilometres in 5 hours, what is its unit rate in kilometres per hour?', ['50 km/h', '60 km/h', '1,500 km/h', '5 km/h'], 1),
   ('A unit rate compares a quantity to ___.', ['One unit of another quantity', 'Ten units of another quantity', 'A completely unrelated quantity', 'Nothing at all'], 0),
   ('If 4 apples cost $2, what is the unit rate (price per apple)?', ['$0.50', '$2.00', '$8.00', '$4.00'], 0),
   ('Unit rates are useful for ___.', ['Comparing which option offers better value', 'Making comparisons impossible', 'Ignoring price differences', 'Only measuring time'], 0),
   ('If a runner covers 100 metres in 20 seconds, what is their unit rate in metres per second?', ['5 m/s', '20 m/s', '80 m/s', '2,000 m/s'], 0)]),
Sc('The Skeletal and Muscular Systems',
   'Ontario Grade 5 Science Human Body Systems strand: the skeletal system (bones) provides structure and protection for the body, while the muscular system works with bones to allow movement.',
   [('The main role of the skeletal system is to ___.', ['Provide structure and protect internal organs', 'Digest food', 'Pump blood', 'Filter air'], 0),
    ('The muscular system works with the skeletal system to ___.', ['Allow the body to move', 'Digest food only', 'Filter blood', 'Control emotions directly'], 0),
    ('Which body part is protected by the ribcage, part of the skeletal system?', ['Heart and lungs', 'Fingernails', 'Hair', 'Skin only'], 0),
    ('Muscles typically move the body by ___.', ['Contracting and relaxing', 'Dissolving completely', 'Producing digestive enzymes', 'Filtering waste'], 0),
    ('Why do the skeletal and muscular systems need to work together?', ['Muscles pull on bones to create movement at the joints', 'They function completely independently with no connection', 'Bones move entirely on their own without muscles', 'Muscles have no connection to bones'], 0)]),
SS('The Great Depression in Canada',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: the Great Depression of the 1930s caused widespread unemployment and hardship across Canada, leading to significant changes in government support programs.',
   [('The Great Depression took place mainly during which decade?', ['1890s', '1930s', '1960s', '1990s'], 1),
    ('The Great Depression caused widespread ___.', ['Economic prosperity', 'Unemployment and hardship', 'Population growth with no problems', 'Immediate improvement in living conditions'], 1),
    ('The hardships of the Great Depression contributed to changes in ___.', ['Government support programs', 'Nothing related to government policy', 'Only sports rules', 'Foreign languages spoken in Canada'], 0),
    ('Why is the Great Depression significant to Canadian history?', ['It caused major economic and social hardship that shaped later government policy', 'It had no lasting impact on Canada', 'It only affected other countries, not Canada', 'It happened in modern times'], 0),
    ('Which is an example of hardship many Canadians faced during the Great Depression?', ['Widespread job loss and poverty', 'Unlimited access to jobs and wealth', 'No economic changes at all', 'A booming economy with no challenges'], 0)])]),

day(42, [
L('Grammar: Modifiers and Clarity',
  'Ontario Grade 5 Writing strand: a modifier is a word or phrase that describes another word, and misplaced modifiers can make a sentence unclear or confusing if placed too far from the word they describe.',
  [('A modifier is a word or phrase that ___.', ['Describes another word in the sentence', 'Replaces punctuation', 'Is always the subject of a sentence', 'Has no grammatical function'], 0),
   ('A misplaced modifier can cause a sentence to ___.', ['Become clearer', 'Become confusing or unclear', 'Have no effect on meaning', 'Automatically fix itself'], 1),
   ('Which sentence has a misplaced modifier? Running quickly, the finish line was reached by Sam.', ['This sentence', 'Sam ran quickly to the finish line.', 'Sam reached the finish line.', 'The finish line was near Sam.'], 0),
   ('Why is it important to place modifiers close to the word they describe?', ['To avoid confusing or unintended meanings in a sentence', 'Placement of modifiers never matters', 'Modifiers should always be at the very end of a paragraph', 'Clarity is not a goal of good writing'], 0),
   ('Which is a corrected, clear version of a modifier issue? Wearing a red hat, I saw my friend.', ['I saw my friend wearing a red hat.', 'Wearing a red hat, my friend I saw.', 'Both sentences mean the exact same thing with no ambiguity.', 'Neither sentence uses a modifier.'], 0)]),
M('Multiplying Fractions by Fractions',
  'Ontario Grade 5 Number strand: to multiply two fractions, multiply the numerators together and the denominators together, then simplify the result if possible.',
  [('What is 1/2 times 1/3?', ['1/6', '2/5', '1/5', '2/6'], 0),
   ('What is 2/3 times 3/4?', ['6/12, which simplifies to 1/2', '5/7', '6/7', '2/12'], 0),
   ('To multiply two fractions, you ___.', ['Multiply the numerators and multiply the denominators', 'Add the numerators and denominators', 'Only multiply the denominators', 'Only multiply the numerators'], 0),
   ('What is 3/5 times 1/2?', ['3/10', '4/7', '3/7', '4/10'], 0),
   ('What is 2/4 times 2/4?', ['4/16, which simplifies to 1/4', '4/8', '2/4', '8/4'], 0)]),
Sc('The Excretory System',
   'Ontario Grade 5 Science Human Body Systems strand: the excretory system, including the kidneys and bladder, removes waste products and excess water from the blood to keep the body’s internal environment balanced.',
   [('The main organs of the excretory system include the ___.', ['Kidneys and bladder', 'Heart and lungs', 'Brain and spinal cord', 'Stomach and intestines only'], 0),
    ('The main role of the excretory system is to ___.', ['Remove waste products and excess water from the blood', 'Digest food completely', 'Pump oxygen throughout the body', 'Control body temperature only'], 0),
    ('The kidneys filter waste out of the ___.', ['Blood', 'Bones', 'Muscles', 'Skin'], 0),
    ('Why is the excretory system important for overall health?', ['It helps maintain a balanced internal environment by removing waste', 'It has no real role in the body', 'It only affects hair growth', 'It produces energy for muscles'], 0),
    ('Urine, produced by the kidneys, is eventually stored in the ___ before being removed from the body.', ['Bladder', 'Stomach', 'Lungs', 'Heart'], 0)]),
SS('Canada’s Path to Full Independence: The Statute of Westminster',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: the Statute of Westminster, passed in 1931, gave Canada and other Commonwealth countries greater legal independence from Britain in making their own laws.',
   [('The Statute of Westminster was passed in which year?', ['1867', '1931', '1982', '1945'], 1),
    ('The Statute of Westminster gave Canada greater ___.', ['Legal independence in making its own laws', 'Control over other countries', 'Dependence on Britain', 'Isolation from the Commonwealth'], 0),
    ('Before the Statute of Westminster, Canada’s laws were more closely tied to ___.', ['The United States', 'Britain', 'France', 'No other country'], 1),
    ('Why is the Statute of Westminster considered an important step in Canadian history?', ['It marked significant progress toward Canada governing itself independently', 'It had no effect on Canada’s legal status', 'It made Canada less independent', 'It ended Canada’s relationship with the Commonwealth entirely'], 0),
    ('The Statute of Westminster applied to Canada and other ___ countries.', ['Commonwealth', 'European Union', 'Unrelated', 'South American'], 0)])]),

day(43, [
L('Writing: Writing a News Report',
  'Ontario Grade 5 Writing strand: a news report presents factual information about a recent event, typically answering who, what, when, where, why, and how, often starting with the most important details.',
  [('A news report typically answers questions including ___.', ['Who, what, when, where, why, and how', 'Only the writer’s opinion', 'Only the weather', 'Nothing specific at all'], 0),
   ('News reports usually begin with ___.', ['The least important details', 'The most important details', 'A long unrelated introduction', 'A poem'], 1),
   ('Why should a news report focus on factual information?', ['To accurately inform readers about what happened', 'Facts are not important in news reports', 'News reports should always be fictional', 'Opinions should replace facts entirely'], 0),
   ('Which is an example of a strong news report opening?', ['A fire broke out at a downtown building early this morning, displacing twelve residents.', 'Once upon a time, in a faraway land...', 'Fires are sometimes hot.', 'This report has no clear topic.'], 0),
   ('Why is it useful for a news report to include where an event happened?', ['It helps readers understand the specific context and location of the event', 'Location is never relevant to news', 'News reports should never mention places', 'Where something happened has no value to readers'], 0)]),
M('Volume of Triangular Prisms',
  'Ontario Grade 5 Geometry strand: the volume of a triangular prism can be found by multiplying the area of its triangular base by the length (height) of the prism.',
  [('The formula for the volume of a triangular prism is ___.', ['Base area times length of the prism', 'Base area divided by length', 'Perimeter times height', 'Length times width only'], 0),
   ('If a triangular prism’s base area is 12 square units and its length is 5 units, what is its volume?', ['60 cubic units', '17 cubic units', '30 cubic units', '12 cubic units'], 0),
   ('To find a triangular prism’s volume, you first need to know its ___.', ['Base area and length', 'Colour and weight', 'Number of edges only', 'Surface temperature'], 0),
   ('If a triangular prism’s base area is 8 square units and its length is 10 units, what is its volume?', ['18 cubic units', '80 cubic units', '8 cubic units', '800 cubic units'], 1),
   ('Volume is measured in ___ units.', ['Square', 'Cubic', 'Linear', 'Degree'], 1)]),
Sc('Compound Machines: Combining Simple Machines',
   'Ontario Grade 5 Science Structures and Mechanisms strand: a compound machine combines two or more simple machines, such as a wheelbarrow (lever and wheel-and-axle) or scissors (two levers), to make tasks easier.',
   [('A compound machine is made up of ___.', ['Only one simple machine', 'Two or more simple machines working together', 'No simple machines at all', 'Only electrical parts'], 1),
    ('A wheelbarrow combines which two simple machines?', ['A lever and a wheel-and-axle', 'A pulley and a screw', 'Two inclined planes', 'Two screws'], 0),
    ('Scissors are an example of a compound machine made from ___.', ['Two levers', 'A pulley and a wheel', 'A single inclined plane', 'Two screws'], 0),
    ('Why might a compound machine be more useful than a single simple machine?', ['Combining simple machines can accomplish more complex tasks efficiently', 'Compound machines are always less useful than simple ones', 'Compound machines cannot perform any task', 'Simple machines can never be combined'], 0),
    ('Which everyday tool is an example of a compound machine?', ['A pair of scissors', 'A flat ramp with nothing else', 'A single nail', 'A plain rope'], 0)]),
SS('The 1982 Constitution Act and the Charter of Rights and Freedoms',
   'Ontario Grade 5 Social Studies People and Environments strand: the 1982 Constitution Act patriated Canada’s constitution from Britain and included the Canadian Charter of Rights and Freedoms, which protects fundamental rights of Canadians.',
   [('The Constitution Act was passed in which year?', ['1867', '1931', '1982', '1867 and 1931 only'], 2),
    ('Patriating the constitution meant Canada could ___.', ['No longer amend its own constitution', 'Amend its own constitution without approval from Britain', 'Give up its constitution entirely', 'Only follow British law forever'], 1),
    ('The Canadian Charter of Rights and Freedoms is included within the ___.', ['1867 British North America Act', '1982 Constitution Act', 'Statute of Westminster', 'A separate, unrelated document'], 1),
    ('The Charter of Rights and Freedoms is meant to protect ___.', ['No one’s rights', 'Fundamental rights of people in Canada', 'Only the rights of elected officials', 'Only property rights'], 1),
    ('Why is 1982 considered an important year in Canadian constitutional history?', ['Canada gained full control over its constitution and adopted the Charter', 'Nothing significant happened that year', 'Canada lost its independence that year', 'Canada joined a new country that year'], 0)])]),

day(44, [
L('Figurative Language: Symbolism',
  'Ontario Grade 5 Reading strand: symbolism is when an object, character, or colour represents a deeper idea or meaning beyond its literal sense, such as a dove symbolizing peace.',
  [('Symbolism is when something represents ___.', ['Only its literal, surface meaning', 'A deeper idea or meaning beyond its literal sense', 'Nothing at all', 'A random unrelated word'], 1),
   ('A dove is commonly used as a symbol of ___.', ['War', 'Peace', 'Anger', 'Confusion'], 1),
   ('Why do authors use symbolism in their writing?', ['To add deeper meaning and layers of interpretation to a story', 'To make stories completely literal with no deeper meaning', 'Symbolism has no purpose in writing', 'To confuse readers with no intended meaning'], 0),
   ('Which could serve as a symbol of new beginnings in a story?', ['A sunrise', 'A broken clock with no context', 'A random number', 'An empty page with nothing described'], 0),
   ('Symbolism is different from a literal description because it ___.', ['Suggests meaning beyond the object’s surface appearance', 'Only describes exactly what something looks like', 'Never appears in stories', 'Is the same as describing a character’s height'], 0)]),
M('Circles: Radius, Diameter, and Circumference',
  'Ontario Grade 5 Geometry strand: a circle’s radius is the distance from the centre to the edge, its diameter is twice the radius, and its circumference is the distance around the circle.',
  [('The radius of a circle is the distance from ___.', ['The centre to the edge', 'One edge to the opposite edge', 'The circumference to the diameter', 'Nowhere in particular'], 0),
   ('The diameter of a circle is ___ the radius.', ['Half of', 'Equal to', 'Twice', 'Four times'], 2),
   ('If a circle’s radius is 5 cm, what is its diameter?', ['2.5 cm', '5 cm', '10 cm', '15 cm'], 2),
   ('The circumference of a circle refers to ___.', ['The distance around the circle', 'The area inside the circle', 'The radius only', 'The centre point'], 0),
   ('If a circle’s diameter is 8 cm, what is its radius?', ['4 cm', '8 cm', '16 cm', '2 cm'], 0)]),
Sc('Properties of Air and Atmosphere',
   'Ontario Grade 5 Science Matter and Energy strand: air is a mixture of gases that makes up Earth’s atmosphere, has mass and takes up space, and plays a key role in weather and supporting life.',
   [('Air is best described as ___.', ['A single pure element', 'A mixture of gases', 'A solid material', 'Empty space with nothing in it'], 1),
    ('Which of these is true about air?', ['It has no mass and takes up no space', 'It has mass and takes up space', 'It cannot move at all', 'It has no connection to weather'], 1),
    ('Earth’s atmosphere plays an important role in ___.', ['Supporting life and influencing weather', 'Nothing important', 'Preventing all forms of weather', 'Blocking all forms of life'], 0),
    ('Which gas makes up the largest portion of Earth’s atmosphere?', ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Hydrogen'], 1),
    ('Why is it important to study the properties of air and atmosphere?', ['It helps us understand weather patterns and the conditions that support life', 'Air has no scientific importance', 'The atmosphere has no connection to weather', 'Air properties never change'], 0)]),
SS('Regional Economic Differences Across Canada',
   'Ontario Grade 5 Social Studies People and Environments strand: different regions of Canada have distinct economies based on their available resources and industries, such as fishing in Atlantic Canada or oil production in Alberta.',
   [('Atlantic Canada’s economy has historically relied heavily on ___.', ['Oil production', 'Fishing', 'Desert farming', 'Coral reef tourism only'], 1),
    ('Alberta’s economy has historically relied heavily on ___.', ['Oil production', 'Deep-sea fishing', 'Rainforest logging', 'Nothing at all'], 0),
    ('Regional economic differences across Canada are often shaped by ___.', ['Available natural resources and local industries', 'Nothing related to geography', 'Random chance with no connection to resources', 'Identical factors everywhere in Canada'], 0),
    ('Why might different provinces specialize in different economic activities?', ['They make use of the resources and conditions unique to their region', 'All provinces have exactly the same resources', 'Specialization has no connection to available resources', 'Economic activity is unrelated to geography'], 0),
    ('Which is an example of a resource-based industry in a specific Canadian region?', ['Forestry in British Columbia', 'Desert farming in the Arctic', 'Coral reef diving in Ontario', 'Volcano tourism in the Prairies'], 0)])]),

day(45, [
L('Reading: Distinguishing Facts from Inferences',
  'Ontario Grade 5 Reading strand: a fact is directly stated in a text, while an inference is a logical conclusion a reader draws by combining text clues with their own knowledge.',
  [('A fact in a text is ___.', ['Directly stated information', 'Always a guess with no evidence', 'Never found in nonfiction', 'The same thing as an inference'], 0),
   ('An inference is ___.', ['Directly stated in the text word for word', 'A logical conclusion drawn from text clues and prior knowledge', 'Always incorrect', 'Impossible to support with evidence'], 1),
   ('If a text says a character’s hands were shaking as they opened a letter, a reasonable inference might be that the character felt ___.', ['Nervous or anxious', 'Nothing at all', 'Extremely relaxed', 'Bored'], 0),
   ('Why is it useful for readers to make inferences?', ['It helps readers understand ideas that are implied but not directly stated', 'Inferences are never useful in reading', 'Only facts matter when reading a text', 'Inferences should always be avoided'], 0),
   ('An inference is considered reasonable when it is ___.', ['Based on clues from the text and logical thinking', 'A completely random guess', 'Unrelated to anything in the text', 'Always identical to a stated fact'], 0)]),
M('Constructing and Interpreting Circle Graphs',
  'Ontario Grade 5 Data Management strand: a circle graph (pie chart) shows data as slices of a circle, where each slice’s size represents its proportion of the whole set of data.',
  [('In a circle graph, the size of each slice represents ___.', ['Its proportion of the whole data set', 'A random unrelated value', 'The colour used', 'Nothing measurable'], 0),
   ('A circle graph is also commonly known as a ___.', ['Bar graph', 'Pie chart', 'Line graph', 'Pictograph'], 1),
   ('If half of a circle graph is shaded for one category, that category represents ___ of the total data.', ['10 percent', '25 percent', '50 percent', '100 percent'], 2),
   ('Circle graphs are especially useful for showing ___.', ['How parts relate to a whole', 'Data with no relationship to a total', 'Only exact numerical values with no proportions', 'Data over time only'], 0),
   ('If a circle graph has four equal slices, each slice represents ___ of the total.', ['10 percent', '20 percent', '25 percent', '50 percent'], 2)]),
Sc('Stars and Constellations',
   'Ontario Grade 5 Science Earth and Space Systems strand: stars are massive, glowing balls of gas that produce their own light and heat, and patterns of stars form constellations that have been used historically for navigation.',
   [('A star is best described as ___.', ['A massive, glowing ball of gas that produces its own light and heat', 'A small rocky planet', 'A moon orbiting a planet', 'A type of comet'], 0),
    ('A constellation is ___.', ['A single very bright star', 'A recognized pattern formed by a group of stars', 'A type of planet', 'A type of galaxy'], 1),
    ('Historically, constellations have been used for ___.', ['Navigation and storytelling', 'Cooking recipes', 'Building houses', 'Farming schedules only'], 0),
    ('Why do stars appear as small points of light from Earth?', ['They are extremely far away, despite being enormous in size', 'Stars are actually very small in real life', 'Stars produce no light at all', 'Stars are the same size as planets'], 0),
    ('Which of these is an example of a well-known constellation?', ['The Big Dipper', 'The Great Lakes', 'The Rocky Mountains', 'The Sahara Desert'], 0)]),
SS('Urbanization and Its Effects on Canadian Cities',
   'Ontario Grade 5 Social Studies People and Environments strand: urbanization is the growth of cities as more people move from rural areas to urban centres, which can affect housing, transportation, and the environment.',
   [('Urbanization refers to ___.', ['The growth of cities as populations shift toward urban centres', 'The disappearance of all cities', 'A decrease in city populations', 'Nothing related to population movement'], 0),
    ('Which challenge is commonly associated with rapid urbanization?', ['Increased demand for housing and transportation', 'A complete lack of any challenges', 'Fewer people needing services', 'No effect on infrastructure at all'], 0),
    ('Urbanization can affect the environment by ___.', ['Increasing land development and resource use in cities', 'Having no environmental impact whatsoever', 'Automatically improving air quality with no effort', 'Reducing the need for any resources'], 0),
    ('Why might people move from rural areas to cities?', ['For access to jobs, services, and opportunities often concentrated in urban areas', 'Cities never offer any advantages', 'Rural areas always have more job opportunities', 'People never choose to move for economic reasons'], 0),
    ('City planners must consider urbanization’s effects on ___.', ['Housing, transportation, and environmental sustainability', 'Nothing related to daily life', 'Only the colour of buildings', 'Weather patterns exclusively'], 0)])]),

day(46, [
L('Vocabulary: Connotation and Denotation',
  'Ontario Grade 5 Language strand: denotation is a word’s literal dictionary definition, while connotation is the feeling or association a word carries beyond its literal meaning, such as childish versus youthful.',
  [('Denotation refers to ___.', ['A word’s literal dictionary definition', 'The feeling a word suggests', 'A word’s spelling only', 'A word’s pronunciation only'], 0),
   ('Connotation refers to ___.', ['A word’s literal definition only', 'The feeling or association a word carries beyond its literal meaning', 'A word’s part of speech', 'A word’s syllable count'], 1),
   ('The words childish and youthful have similar denotations but different ___.', ['Spellings', 'Connotations', 'Pronunciations', 'Definitions in the dictionary'], 1),
   ('Which word likely has a more positive connotation than stubborn, despite a similar meaning?', ['Determined', 'Careless', 'Lazy', 'Rude'], 0),
   ('Why is understanding connotation useful for writers?', ['It helps them choose words that create the intended tone or feeling', 'Connotation has no effect on writing', 'Writers should always ignore how words feel to readers', 'Connotation only applies to poetry'], 0)]),
M('Geometric Nets and 3D Shape Construction',
  'Ontario Grade 5 Geometry strand: a net is a 2D pattern that can be folded to form a 3D shape, showing all of the shape’s faces laid out flat.',
  [('A net is best described as ___.', ['A 2D pattern that folds into a 3D shape', 'A type of graph', 'A type of fraction', 'A measurement of angles only'], 0),
   ('The net of a cube is made up of how many square faces?', ['4', '6', '8', '12'], 1),
   ('Nets help us understand 3D shapes by ___.', ['Showing all of a shape’s faces laid out flat', 'Hiding all of a shape’s faces', 'Removing the need for any faces', 'Turning a 3D shape into a single point'], 0),
   ('The net of a triangular prism includes ___.', ['Two triangles and three rectangles', 'Six squares', 'Only circles', 'One single triangle only'], 0),
   ('Why might builders or designers use nets when creating 3D objects?', ['Nets help plan how flat material can be folded into a finished 3D shape', 'Nets have no practical use', 'Nets are only used in fiction writing', 'Nets eliminate the need for any measurements'], 0)]),
Sc('Conservation of Biodiversity',
   'Ontario Grade 5 Science Life Systems strand: biodiversity is the variety of living things in an ecosystem, and conservation efforts aim to protect that variety from threats like habitat loss and pollution.',
   [('Biodiversity refers to ___.', ['The variety of living things in an ecosystem', 'A single species living alone', 'The absence of all living things', 'Only the number of trees in a forest'], 0),
    ('Which is a common threat to biodiversity?', ['Habitat loss', 'Too much protected land', 'Too many conservation programs', 'Nothing threatens biodiversity'], 0),
    ('Why is biodiversity important to a healthy ecosystem?', ['A variety of species helps maintain balance and resilience in the ecosystem', 'Biodiversity has no effect on ecosystems', 'Ecosystems function better with only one species present', 'Biodiversity always harms ecosystems'], 0),
    ('Which is an example of a conservation effort to protect biodiversity?', ['Establishing protected wildlife habitats', 'Removing all environmental protections', 'Encouraging unlimited habitat destruction', 'Ignoring threats to species'], 0),
    ('Why might scientists monitor biodiversity levels over time?', ['To detect changes that might signal environmental problems', 'Monitoring biodiversity serves no purpose', 'Biodiversity never changes over time', 'Only non-living things are worth monitoring'], 0)]),
SS('Canada’s Relationship with the Commonwealth',
   'Ontario Grade 5 Social Studies People and Environments strand: the Commonwealth is a voluntary association of countries, many once part of the British Empire, that cooperate on shared goals like trade, education, and democracy.',
   [('The Commonwealth is best described as ___.', ['A voluntary association of countries cooperating on shared goals', 'A single country', 'An organization with no members', 'A military alliance only'], 0),
    ('Many Commonwealth countries were historically connected through ___.', ['The British Empire', 'The Roman Empire', 'No historical connection at all', 'Ancient trade routes only'], 0),
    ('Commonwealth countries often cooperate on issues such as ___.', ['Trade, education, and democracy', 'Nothing of shared interest', 'Only military conflict', 'Isolating each other completely'], 0),
    ('Is membership in the Commonwealth mandatory for its member countries?', ['Yes, countries are forced to join', 'No, membership is voluntary', 'Only some countries are allowed to leave', 'Membership has never been optional'], 1),
    ('Why might Canada value its relationship with the Commonwealth?', ['It offers opportunities for cooperation and shared connections with other nations', 'The Commonwealth provides no benefit to Canada', 'Canada has no historical ties to Commonwealth countries', 'Commonwealth membership isolates Canada from the world'], 0)])]),

day(47, [
L('Writing: Formal Speech Writing',
  'Ontario Grade 5 Writing strand: a formal speech is organized with a clear introduction, body, and conclusion, uses persuasive or informative language suited to the audience, and is written to be spoken aloud.',
  [('A formal speech is typically organized with ___.', ['No clear structure at all', 'A clear introduction, body, and conclusion', 'Only random unrelated points', 'A single sentence'], 1),
   ('Why should a speech writer consider their audience?', ['To choose language and content the audience will understand and connect with', 'The audience never matters when writing a speech', 'All speeches should be written the exact same way regardless of audience', 'Considering the audience makes a speech less effective'], 0),
   ('A strong speech introduction often ___.', ['Captures the audience’s attention and introduces the topic', 'Immediately ends the speech', 'Ignores the topic entirely', 'Contains no information at all'], 0),
   ('Since a speech is meant to be spoken aloud, writers should consider ___.', ['How the words will sound and flow when read aloud', 'Only how the words look on paper', 'Nothing related to pacing or tone', 'Making every sentence as long as possible'], 0),
   ('A speech’s conclusion should typically ___.', ['Reinforce the main message and leave a lasting impression', 'Introduce a brand new unrelated topic', 'Repeat random unrelated facts', 'Contain no connection to the rest of the speech'], 0)]),
M('Patterns with Two Variables',
  'Ontario Grade 5 Algebra strand: a pattern with two variables shows how one value changes in relation to another, often organized in a table, where identifying the rule connecting them helps predict future values.',
  [('If the rule is y equals x plus 3, what is y when x is 5?', ['5', '8', '3', '15'], 1),
   ('In a table showing two related variables, identifying the rule helps you ___.', ['Predict future values', 'Ignore the pattern entirely', 'Avoid understanding the relationship', 'Only look at one variable'], 0),
   ('If the rule is y equals x times 2, what is y when x is 7?', ['9', '14', '5', '72'], 1),
   ('If x is 1, 2, 3 and the matching y values are 4, 8, 12, what is the rule connecting x and y?', ['y equals x plus 4', 'y equals x times 4', 'y equals x minus 4', 'y equals x divided by 4'], 1),
   ('Why are tables useful for exploring patterns with two variables?', ['They organize the data clearly, making the relationship between variables easier to see', 'Tables make patterns impossible to identify', 'Tables are never used for patterns', 'Tables only work with a single variable'], 0)]),
Sc('Chemical Changes and Reactions',
   'Ontario Grade 5 Science Matter and Energy strand: a chemical change occurs when substances react to form new substances with different properties, often shown by signs like colour change, gas bubbles, or heat being released.',
   [('A chemical change occurs when ___.', ['Substances react to form new substances with different properties', 'A substance only changes shape', 'Nothing about the substance changes at all', 'A substance simply melts'], 0),
    ('Which is a common sign that a chemical reaction has occurred?', ['Gas bubbles forming', 'The object staying exactly the same', 'No observable change at all', 'The object becoming a different shape only'], 0),
    ('Rusting metal is an example of a ___.', ['Physical change only', 'Chemical change', 'Change that never actually occurs', 'Change with no cause'], 1),
    ('Chemical reactions can release or absorb ___.', ['Heat energy', 'Nothing at all', 'Only sound', 'Only light with no other effect'], 0),
    ('Why is it useful to be able to identify signs of a chemical reaction?', ['It helps distinguish a chemical change from a simple physical change', 'Chemical reactions have no observable signs', 'All changes in matter are identical', 'Identifying reactions serves no scientific purpose'], 0)]),
SS('The Role of the Media in a Democracy',
   'Ontario Grade 5 Social Studies People and Environments strand: media, including news outlets and journalists, plays a role in informing citizens about government actions and current events, which supports an informed and engaged democracy.',
   [('One key role of the media in a democracy is to ___.', ['Inform citizens about government actions and current events', 'Prevent citizens from learning anything', 'Replace the need for elections', 'Control what citizens are allowed to think'], 0),
    ('An informed citizen is better able to ___.', ['Participate thoughtfully in democratic decisions like voting', 'Avoid all civic responsibilities', 'Ignore important issues entirely', 'Make decisions with no available information'], 0),
    ('Why is it important for media to report accurately?', ['Accurate reporting helps citizens make informed decisions', 'Accuracy has no effect on democracy', 'Citizens do not need accurate information', 'Inaccurate reporting always benefits democracy'], 0),
    ('Journalists in a democracy often play a role in ___.', ['Investigating and reporting on issues that affect the public', 'Avoiding any coverage of government actions', 'Making all government decisions themselves', 'Replacing elected officials'], 0),
    ('Why might citizens compare multiple media sources when following an issue?', ['To get a fuller, more balanced understanding of the topic', 'Comparing sources has no value', 'One source always tells the complete story', 'Citizens should avoid all media sources'], 0)])]),

day(48, [
L('Media Literacy: Comparing Media Formats',
  'Ontario Grade 5 Media Literacy strand: different media formats, such as print articles, videos, podcasts, and social media posts, present information differently and can shape how audiences understand a topic.',
  [('Which is an example of a media format?', ['A podcast', 'A math equation', 'A single letter of the alphabet', 'A blank page'], 0),
   ('Different media formats can ___.', ['Present the same topic in different ways', 'Always present information identically', 'Have no effect on understanding', 'Never be compared to each other'], 0),
   ('A video format might convey information differently from print by using ___.', ['Visuals, sound, and movement', 'Only plain text with no other elements', 'Nothing beyond written words', 'No sound or visuals at all'], 0),
   ('Why might comparing how different formats cover the same topic be useful?', ['It reveals how the choice of format can shape understanding of a topic', 'Comparing formats has no value', 'All formats always present identical information', 'Only one media format can ever be trusted'], 0),
   ('Social media posts often present information ___.', ['In a longer, more detailed form than any other format', 'In short, quickly consumed pieces', 'Exactly the same way as an academic textbook', 'With no possibility of bias'], 1)]),
M('Estimating and Measuring Angles with a Protractor',
  'Ontario Grade 5 Geometry strand: a protractor is a tool used to measure the size of an angle in degrees, and estimating an angle’s size before measuring helps check whether the measurement is reasonable.',
  [('A protractor is used to measure ___.', ['The length of a line', 'The size of an angle in degrees', 'The weight of an object', 'The volume of a shape'], 1),
   ('Before measuring an angle exactly, estimating its size helps you ___.', ['Guess randomly with no purpose', 'Check whether your final measurement is reasonable', 'Avoid using a protractor altogether', 'Skip measuring entirely'], 1),
   ('An angle that looks close to a right angle is likely close to ___ degrees.', ['45', '90', '180', '360'], 1),
   ('A straight angle measures ___ degrees.', ['90', '180', '360', '45'], 1),
   ('When using a protractor, the vertex of the angle should be lined up with ___.', ['The centre point of the protractor', 'The edge of the paper', 'A random point', 'The 90-degree mark only'], 0)]),
Sc('Forces: Friction and Air Resistance',
   'Ontario Grade 5 Science Structures and Mechanisms strand: friction is a force that resists motion between two surfaces in contact, and air resistance is a similar force that slows objects moving through air.',
   [('Friction is a force that ___.', ['Speeds up motion between surfaces', 'Resists motion between two surfaces in contact', 'Only exists in outer space', 'Has no effect on moving objects'], 1),
    ('Air resistance is a force that ___.', ['Slows down objects moving through air', 'Speeds up objects moving through air with no limit', 'Only affects objects underwater', 'Has no connection to motion'], 0),
    ('Which surface would likely create more friction?', ['A rough, bumpy surface', 'A perfectly smooth, oiled surface', 'A surface with no contact at all', 'Friction is unaffected by surface texture'], 0),
    ('Why might a parachute use air resistance to its advantage?', ['It slows a falling object down for a safer landing', 'Air resistance has no effect on falling objects', 'Parachutes eliminate air resistance completely', 'Air resistance only affects solid objects, not fabric'], 0),
    ('Which situation involves a large amount of friction?', ['Sliding a heavy box across rough pavement', 'An object floating freely in space', 'A ball rolling on a frictionless surface', 'An object at complete rest with no forces acting on it'], 0)]),
SS('Comparing Government Systems: Canada and Other Countries',
   'Ontario Grade 5 Social Studies People and Environments strand: comparing Canada’s parliamentary democracy to other government systems, such as a republic or a monarchy without elected representatives, helps highlight different ways countries are governed.',
   [('Canada’s system of government is best described as a ___.', ['Parliamentary democracy', 'Government with no elected officials', 'System with no laws at all', 'Government led entirely by a single unelected ruler'], 0),
    ('Comparing government systems across countries can help students understand ___.', ['Different ways nations organize decision-making and representation', 'That all countries are governed identically', 'That government systems have no real differences', 'That comparing systems serves no purpose'], 0),
    ('A republic is generally a system where ___.', ['The head of state is typically elected, not a hereditary monarch', 'There is no government at all', 'Only a king or queen can ever lead', 'Citizens have no role in choosing leaders'], 0),
    ('Why might different countries choose different systems of government?', ['Government systems often reflect a country’s unique history, values, and needs', 'All countries are required to use the same system', 'Government systems have no connection to history or culture', 'Choice of government system is always random'], 0),
    ('Studying different government systems helps citizens ___.', ['Better understand how their own government compares to others', 'Avoid learning about their own government', 'Understand that comparison is unnecessary', 'Conclude that only one system has ever existed'], 0)])]),

day(49, [
L('Grammar: Correcting Run-on Sentences and Fragments',
  'Ontario Grade 5 Writing strand: a run-on sentence incorrectly joins two or more complete sentences without proper punctuation, while a sentence fragment is an incomplete sentence missing a subject, verb, or complete thought.',
  [('A run-on sentence is one that ___.', ['Incorrectly joins two or more complete sentences without proper punctuation', 'Is always too short', 'Has perfect punctuation throughout', 'Contains no subject or verb at all'], 0),
   ('A sentence fragment is ___.', ['A complete sentence with excess punctuation', 'An incomplete sentence missing a subject, verb, or complete thought', 'Always longer than a run-on sentence', 'A sentence with no possible errors'], 1),
   ('Which of these is a sentence fragment?', ['Running down the street.', 'The dog ran down the street.', 'The dog ran down the street, and it barked loudly.', 'She smiled.'], 0),
   ('Which of these is a run-on sentence?', ['I like pizza I also like pasta.', 'I like pizza, and I also like pasta.', 'I like pizza.', 'Pizza is my favourite food.'], 0),
   ('How can a run-on sentence often be corrected?', ['By adding proper punctuation or splitting it into separate sentences', 'By removing all punctuation entirely', 'Run-on sentences cannot be corrected', 'By making the sentence even longer'], 0)]),
M('Comparing Costs and Value for Money',
  'Ontario Grade 5 Financial Literacy strand: comparing costs and value for money involves looking beyond price alone to consider quality, quantity, and unit rates when deciding which option offers the best value.',
  [('Value for money means considering ___.', ['Only the lowest price, regardless of quality', 'Price along with quality and quantity', 'Nothing beyond the item’s colour', 'Only the brand name'], 1),
   ('If a 500 mL bottle costs $2 and a 1 L bottle costs $3.50, which offers better value per litre?', ['The 500 mL bottle', 'The 1 L bottle', 'They offer identical value', 'Value cannot be compared here'], 1),
   ('Why might a shopper compare unit rates when choosing between products?', ['To determine which option provides more value for the price', 'Unit rates have no connection to value', 'Comparing unit rates always wastes time', 'Price should never be considered when shopping'], 0),
   ('Which factor, beyond price, might affect a product’s overall value?', ['Its quality and how long it lasts', 'Nothing beyond the sticker price', 'The store’s wall colour', 'The day of the week it was purchased'], 0),
   ('A shopper choosing the cheapest option without considering quality might end up with ___.', ['Guaranteed excellent value every time', 'A product that does not meet their needs despite the lower price', 'No possible downsides', 'The best possible value automatically'], 1)]),
Sc('Fossils and What They Tell Us About Earth’s History',
   'Ontario Grade 5 Science Earth and Space Systems strand: fossils are the preserved remains or traces of ancient organisms, and studying them helps scientists understand how life and environments on Earth have changed over time.',
   [('A fossil is best described as ___.', ['A living organism found today', 'The preserved remains or traces of an ancient organism', 'A type of modern rock with no history', 'A man-made object'], 1),
    ('Studying fossils helps scientists understand ___.', ['How life and environments on Earth have changed over time', 'Nothing about Earth’s history', 'Only current weather patterns', 'Only modern technology'], 0),
    ('Fossils are often found preserved within ___.', ['Layers of sedimentary rock', 'Only living trees', 'Modern plastic materials', 'Clouds'], 0),
    ('Why might finding a fossil of a sea creature high in the mountains be significant?', ['It could suggest that area was once covered by water long ago', 'It has no scientific significance at all', 'It proves mountains never change over time', 'It means sea creatures currently live in the mountains'], 0),
    ('Scientists who study fossils are called ___.', ['Astronomers', 'Paleontologists', 'Meteorologists', 'Chemists'], 1)]),
SS('The Truth and Reconciliation Commission',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: the Truth and Reconciliation Commission of Canada was established to document the history and impact of the residential school system and to make recommendations toward healing and reconciliation.',
   [('The Truth and Reconciliation Commission was established to document the history of ___.', ['The residential school system', 'The War of 1812', 'The Great Depression', 'The building of the railway'], 0),
    ('One purpose of the Truth and Reconciliation Commission was to ___.', ['Make recommendations toward healing and reconciliation', 'Erase historical records completely', 'Ignore the experiences of residential school survivors', 'Prevent any future discussion of this history'], 0),
    ('The Truth and Reconciliation Commission gathered information partly by ___.', ['Listening to the experiences of residential school survivors', 'Refusing to speak with anyone affected', 'Only using fictional accounts', 'Ignoring all historical evidence'], 0),
    ('Why is learning about the Truth and Reconciliation Commission important for students today?', ['It helps build understanding of this history and supports ongoing reconciliation efforts', 'This history has no relevance today', 'It should be avoided in schools entirely', 'It has no connection to Canadian identity'], 0),
    ('Reconciliation, in this context, refers to ___.', ['Working to repair relationships and address historical harms', 'Ignoring the effects of past policies', 'A type of sporting event', 'A type of geography lesson only'], 0)])]),

day(50, [
L('Reading: Synthesizing Information from Multiple Texts',
  'Ontario Grade 5 Reading strand: synthesizing means combining information from multiple texts or sources to form a more complete understanding of a topic than any single source could provide alone.',
  [('Synthesizing information means ___.', ['Reading only a single source and ignoring all others', 'Combining information from multiple sources into a fuller understanding', 'Copying one text exactly', 'Ignoring all sources completely'], 1),
   ('Why might a reader consult multiple texts on the same topic?', ['To build a more complete and well-rounded understanding', 'One source always provides complete information', 'Consulting multiple texts is a waste of time', 'Additional sources never add useful information'], 0),
   ('When synthesizing, a reader should look for ___.', ['Connections, similarities, and differences across sources', 'Only the exact same information repeated in every source', 'Nothing related to the sources’ content', 'Random unrelated facts with no connections'], 0),
   ('Which is an example of synthesizing information?', ['Combining facts from two articles to write a well-rounded report', 'Reading only the title of one article', 'Ignoring every source except one', 'Copying a single paragraph exactly'], 0),
   ('Why is synthesizing considered an advanced reading skill?', ['It requires understanding, comparing, and combining ideas from multiple sources', 'It requires no understanding of any text', 'It only involves reading a single sentence', 'It has no connection to comprehension'], 0)]),
M('Review: Fractions, Percent, Integers, and Geometry',
  'Ontario Grade 5 Number and Geometry strands review: this lesson revisits fraction operations, percent, integers, and geometry concepts like circles and volume covered across recent lessons.',
  [('What is 1/4 plus 1/4?', ['1/4', '1/2', '2/8', '1'], 1),
   ('What is 20 percent of 50?', ['5', '10', '20', '100'], 1),
   ('Which is colder: -10 degrees or -2 degrees?', ['-10 degrees', '-2 degrees', 'They are equal', 'Cannot be determined'], 0),
   ('What is the diameter of a circle with a radius of 6 cm?', ['3 cm', '6 cm', '12 cm', '18 cm'], 2),
   ('Why is it useful to review fraction, percent, integer, and geometry skills together?', ['These related number and spatial concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Human Body Systems and Forces',
   'Ontario Grade 5 Science review: this lesson revisits the nervous, circulatory, respiratory, skeletal, muscular, and excretory systems alongside forces like friction, air resistance, and mechanical advantage covered recently.',
   [('Which system is responsible for sending electrical signals throughout the body?', ['The nervous system', 'The excretory system', 'The muscular system', 'The skeletal system'], 0),
    ('Which system transports oxygen and nutrients through the body?', ['The circulatory system', 'The excretory system', 'The skeletal system', 'The respiratory system'], 0),
    ('Which force resists motion between two surfaces in contact?', ['Air resistance', 'Friction', 'Buoyancy', 'Magnetism'], 1),
    ('Which body system removes waste products from the blood?', ['The excretory system', 'The muscular system', 'The nervous system', 'The respiratory system'], 0),
    ('Why is it valuable to review body systems and forces together at this point?', ['It helps connect and reinforce related concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each system must always be studied in isolation'], 0)]),
SS('Review: Canadian Government, Rights, and Recent History',
   'Ontario Grade 5 Social Studies review: this lesson revisits Canada’s path to independence, the Charter of Rights and Freedoms, the courts, political parties, and reconciliation efforts covered across recent lessons.',
   [('Which document, adopted in 1982, includes the Canadian Charter of Rights and Freedoms?', ['The Statute of Westminster', 'The Constitution Act', 'The Treaty of Paris', 'The British North America Act only'], 1),
    ('Which body in Canada is responsible for interpreting and applying the law?', ['The courts', 'Only municipal councils', 'Only the media', 'No formal body exists for this'], 0),
    ('The Truth and Reconciliation Commission focused on documenting the history and impact of ___.', ['The residential school system', 'The War of 1812', 'The building of the railway', 'The Great Depression'], 0),
    ('Political parties in Canada generally represent ___.', ['Different ideas about how the country should be governed', 'Identical positions with no real differences', 'No connection to government at all', 'Only local municipal issues'], 0),
    ('Why is reviewing recent Canadian government and history topics together useful?', ['It helps reinforce how these related civic and historical concepts connect', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260714):
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
    _rebalance_answer_positions(g5_41_50)
    append_to(5, g5_41_50)
