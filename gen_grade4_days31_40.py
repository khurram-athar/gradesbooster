#!/usr/bin/env python3
"""Phase 3: Grade 4, Days 31-40 (first batch of the full-year expansion
beyond the original 30-day summer program). Topics chosen to avoid any
overlap with the existing Day 1-30 set (see data/grade4.json) and to draw
on Ontario Grade 4 curriculum strands not yet covered: more Early
Societies (Mesopotamia, China, daily life, belief systems -- alongside the
existing Egypt/Greece/Rome), simple machines beyond pulleys/gears, changes
of state, and physical/political regions of Canada beyond Ontario.

As with the Grade 3 batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded double-quote characters are used anywhere in
question/summary/option text (gen_curriculum.py's serializer doesn't
escape them).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L4 = 'https://tvolearn.com/pages/grade-4-language'
M4 = 'https://tvolearn.com/pages/grade-4-mathematics'
S4 = 'https://tvolearn.com/pages/grade-4-science-and-technology'
SS4 = 'https://tvolearn.com/pages/grade-4-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 4 Language',
    'TVO Learn: Grade 4 Mathematics',
    'TVO Learn: Grade 4 Science & Technology',
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


g4_31_40 = [
day(31, [
L('Reading: Fact and Opinion',
  'Ontario Grade 4 Reading strand: a fact can be proven true or false with evidence, while an opinion expresses a personal belief or judgement that cannot be proven.',
  [('Which of these is a fact?', ['Hockey is the most exciting sport.', 'Canada has ten provinces.', 'Winter is the best season.', 'Blue is the nicest colour.'], 1),
   ('Which of these is an opinion?', ['Water boils at 100 degrees Celsius.', 'Chocolate ice cream is the best flavour.', 'A triangle has three sides.', 'Toronto is in Ontario.'], 1),
   ('A fact can be described as a statement that ___.', ['Reflects a personal feeling', 'Can be proven true or false', 'Everyone must agree with', 'Is always negative'], 1),
   ('Why might two people disagree about an opinion but not a fact?', ['Opinions are based on personal judgement, while facts can be verified', 'Facts and opinions are exactly the same', 'Facts change depending on who says them', 'Opinions can always be proven true'], 0),
   ('Which phrase often signals an opinion?', ['According to the data', 'I believe that', 'Research shows', 'It was measured that'], 1)]),
M('Rounding and Estimating',
  'Ontario Grade 4 Number strand: rounding numbers to the nearest ten, hundred, or thousand makes estimating sums, differences, and totals faster and easier to check for reasonableness.',
  [('Round 3,482 to the nearest thousand.', ['3,000', '3,500', '4,000', '3,482'], 2),
   ('Round 6,251 to the nearest hundred.', ['6,200', '6,250', '6,300', '6,000'], 2),
   ('Estimate the sum: 2,890 + 3,150 is approximately ___.', ['3,000 + 3,000 = 6,000', '2,000 + 3,000 = 5,000', '2,800 + 3,100 = 5,900 exactly, no rounding', '10,000'], 0),
   ('Why is estimating useful before solving a problem exactly?', ['It helps you check whether your final answer is reasonable', 'It replaces the need to solve the problem', 'It always gives the exact answer', 'It has no real use in math'], 0),
   ('Round 749 to the nearest hundred.', ['700', '750', '800', '749'], 2)]),
Sc('Species at Risk in Canadian Ecosystems',
   'Ontario Grade 4 Science Life Systems strand: species at risk are plants or animals in Canada facing possible extinction, often due to habitat loss, pollution, or climate change, and conservation programs work to protect them.',
   [('A species at risk is one that is ___.', ['Extremely abundant everywhere', 'Facing possible extinction', 'No longer affected by its environment', 'Found only in aquariums'], 1),
    ('Which is a common cause of species becoming at risk?', ['Habitat loss', 'Too much protected land', 'Too many predators being removed by nature naturally', 'Nothing affects species survival'], 0),
    ('Which Canadian animal has historically been considered at risk?', ['House sparrow', 'Woodland caribou', 'Common squirrel', 'Raccoon'], 1),
    ('Conservation programs for species at risk often involve ___.', ['Destroying more natural habitat', 'Protecting habitat and monitoring populations', 'Ignoring the issue completely', 'Removing all environmental laws'], 1),
    ('Why do scientists track species at risk closely?', ['To take action before a species disappears entirely', 'Tracking has no scientific value', 'To speed up extinction', 'Only endangered plants are ever tracked'], 0)]),
SS('Ancient Mesopotamia',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient Mesopotamia, located between the Tigris and Euphrates rivers, is considered one of the earliest civilizations, known for early writing, cities, and irrigation systems.',
   [('Ancient Mesopotamia developed between which two rivers?', ['The Nile and Congo', 'The Tigris and Euphrates', 'The Amazon and Mississippi', 'The Ganges and Indus'], 1),
    ('Mesopotamia is often called one of the earliest ___.', ['Deserts', 'Civilizations', 'Oceans', 'Mountain ranges'], 1),
    ('Which early writing system developed in Mesopotamia?', ['Hieroglyphics', 'Cuneiform', 'The Latin alphabet', 'Braille'], 1),
    ('Irrigation systems in Mesopotamia were used mainly to ___.', ['Build pyramids', 'Bring river water to farmland for growing crops', 'Create early roads', 'Power early machines'], 1),
    ('Why did early civilizations like Mesopotamia often develop near rivers?', ['Rivers provided water for farming, drinking, and transportation', 'Rivers were avoided by early people', 'Rivers had no practical benefit', 'Rivers made travel impossible'], 0)])]),

day(32, [
L('Grammar: Comparative and Superlative Adjectives',
  'Ontario Grade 4 Writing strand: comparative adjectives (bigger, faster) compare two things, while superlative adjectives (biggest, fastest) compare three or more things, often adding -er or -est.',
  [('Which is the comparative form of tall?', ['Tall', 'Taller', 'Tallest', 'Tallness'], 1),
   ('Which is the superlative form of fast?', ['Faster', 'Fast', 'Fastest', 'Fastly'], 2),
   ('Comparative adjectives are used to compare ___.', ['Three or more things', 'Two things', 'One thing only', 'Nothing at all'], 1),
   ('Superlative adjectives are used to compare ___.', ['Two things only', 'Three or more things', 'Only colours', 'Only numbers'], 1),
   ('Choose the correct sentence: This is the ___ mountain in the range.', ['tall', 'taller', 'tallest', 'more tall'], 2)]),
M('Multiplying by 10, 100, and 1,000',
  'Ontario Grade 4 Number strand: multiplying a whole number by 10, 100, or 1,000 shifts its digits left, adding that many zeros, such as 25 times 100 equals 2,500.',
  [('What is 34 multiplied by 10?', ['34', '340', '3,400', '34,000'], 1),
   ('What is 56 multiplied by 100?', ['560', '5,600', '56,000', '56'], 1),
   ('What is 7 multiplied by 1,000?', ['70', '700', '7,000', '70,000'], 2),
   ('Multiplying by 100 is the same as adding how many zeros?', ['One', 'Two', 'Three', 'Four'], 1),
   ('What is 120 multiplied by 10?', ['120', '1,200', '12,000', '12'], 1)]),
Sc('Changes of State: Melting, Freezing, and Evaporating',
   'Ontario Grade 4 Science Matter and Energy strand: matter changes state through processes like melting (solid to liquid), freezing (liquid to solid), and evaporating (liquid to gas), usually caused by adding or removing heat.',
   [('Melting occurs when a solid changes into a ___ after gaining heat.', ['Gas', 'Liquid', 'Different solid', 'Nothing changes'], 1),
    ('Freezing occurs when a liquid changes into a solid after ___ heat.', ['Gaining', 'Losing', 'Creating', 'Ignoring'], 1),
    ('Evaporation occurs when a liquid changes into a ___.', ['Solid', 'Gas', 'Different liquid', 'Rock'], 1),
    ('Which is an everyday example of melting?', ['Water freezing into ice cubes', 'An ice cube turning into water on a warm day', 'Steam rising from a lake', 'Rain falling from clouds'], 1),
    ('What generally causes a substance to change state?', ['Adding or removing heat energy', 'Changing its colour', 'Changing its name', 'Nothing can cause a change of state'], 0)]),
SS('Ancient China',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient China developed along the Yellow and Yangtze rivers, and is known for early inventions such as paper, silk production, and the Great Wall.',
   [('Ancient China developed along which rivers?', ['The Nile and Congo', 'The Yellow and Yangtze', 'The Amazon and Mississippi', 'The Tigris and Euphrates'], 1),
    ('Which invention is credited to Ancient China?', ['The wheel only', 'Paper', 'The printing press in Europe', 'Modern electricity'], 1),
    ('Silk production was an important early industry in ___.', ['Ancient Egypt', 'Ancient China', 'Ancient Rome', 'Ancient Greece'], 1),
    ('The Great Wall of China was built mainly to ___.', ['Attract tourists', 'Help defend against invasions', 'Store grain', 'Provide irrigation'], 1),
    ('Why do historians study Ancient China\'s early inventions?', ['They influenced technology and trade for centuries afterward', 'They had no lasting impact', 'Ancient China invented nothing notable', 'Only modern inventions matter to historians'], 0)])]),

day(33, [
L('Writing: Formal and Informal Letters',
  'Ontario Grade 4 Writing strand: formal letters use polite, professional language for serious purposes (like a business), while informal letters use casual, friendly language for people you know well.',
  [('A formal letter is typically used for ___.', ['Writing to a close friend casually', 'Professional or serious purposes', 'Texting a sibling', 'Writing in a diary'], 1),
   ('Which greeting fits a formal letter?', ['Hey there!', 'Dear Sir or Madam,', 'Whats up,', 'Yo,'], 1),
   ('An informal letter is best suited for ___.', ['A job application', 'Writing to a close friend or family member', 'A formal complaint to a company', 'A legal document'], 1),
   ('Which closing best fits a formal letter?', ['See ya later', 'Sincerely,', 'Bye bye', 'Later,'], 1),
   ('Why does letter tone change between formal and informal writing?', ['To match the purpose and relationship with the reader', 'Tone never needs to change', 'All letters should sound the same', 'Formal letters are always shorter'], 0)]),
M('Mixed Numbers and Improper Fractions',
  'Ontario Grade 4 Number strand: a mixed number combines a whole number and a fraction (like 2 and 1/2), while an improper fraction has a numerator larger than its denominator (like 5/2), and the two can be converted between each other.',
  [('Which is a mixed number?', ['5/2', '2 and 1/2', '1/2', '2/5'], 1),
   ('Which is an improper fraction?', ['1/2', '2 and 1/4', '7/3', '3/7'], 2),
   ('Convert the mixed number 1 and 3/4 to an improper fraction.', ['7/4', '4/7', '3/4', '1/4'], 0),
   ('Convert the improper fraction 9/4 to a mixed number.', ['2 and 1/4', '4 and 1/4', '2 and 1/2', '9/4 cannot convert'], 0),
   ('In an improper fraction, the numerator is ___ the denominator.', ['Always smaller than', 'Equal to or larger than', 'Always exactly half of', 'Unrelated to'], 1)]),
Sc('Simple Machines: Levers and Inclined Planes',
   'Ontario Grade 4 Science Structures and Mechanisms strand: a lever uses a pivot point (fulcrum) to lift or move objects with less effort, while an inclined plane is a sloped surface that makes raising objects easier.',
   [('A lever uses a ___ to help lift or move objects.', ['Wheel', 'Fulcrum (pivot point)', 'Screw', 'Magnet'], 1),
    ('An inclined plane is best described as a ___.', ['Sloped surface', 'Spinning wheel', 'Vertical pole', 'Sealed container'], 0),
    ('Which is an everyday example of an inclined plane?', ['A seesaw', 'A ramp', 'A pulley', 'A wheel'], 1),
    ('A seesaw is an example of which simple machine?', ['Inclined plane', 'Lever', 'Screw', 'Wedge'], 1),
    ('Why do inclined planes make lifting heavy objects easier?', ['They spread the effort over a longer distance instead of lifting straight up', 'They eliminate gravity', 'They make objects lighter permanently', 'They have no real benefit'], 0)]),
SS('Early Societies: Daily Life and Social Roles',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: early societies such as Egypt, Greece, Rome, Mesopotamia, and China had structured daily lives, with different social roles for rulers, workers, farmers, and families.',
   [('In many early societies, social roles were often organized by ___.', ['Random daily selection', 'Class or status, such as rulers, workers, and farmers', 'No structure at all', 'Age only, with no other factors'], 1),
    ('Farmers in early societies were important because they ___.', ['Had no role in daily life', 'Produced food to support the population', 'Only built monuments', 'Ruled the government'], 1),
    ('Rulers in early civilizations often held responsibility for ___.', ['Nothing important', 'Leading the society and making major decisions', 'Only farming duties', 'Cooking for the population'], 1),
    ('Studying daily life in early societies helps us understand ___.', ['How people lived, worked, and organized their communities long ago', 'Nothing useful about history', 'Only modern life', 'Daily life was identical everywhere'], 0),
    ('Which role would likely have existed in most early societies?', ['Astronaut', 'Farmer', 'Software engineer', 'Airline pilot'], 1)])]),

day(34, [
L('Figurative Language: Idioms',
  'Ontario Grade 4 Reading strand: an idiom is a phrase whose meaning cannot be understood from the literal words alone, such as break the ice or it is raining cats and dogs.',
  [('An idiom is a phrase whose meaning ___.', ['Matches its literal words exactly', 'Cannot be understood from its literal words alone', 'Is always about weather', 'Has no meaning at all'], 1),
   ('What does the idiom break the ice mean?', ['To literally break frozen water', 'To ease tension and start a conversation', 'To finish a race', 'To clean a window'], 1),
   ('What does it is raining cats and dogs mean?', ['Animals are falling from the sky', 'It is raining very heavily', 'It is a sunny day', 'Pets are outside playing'], 1),
   ('Why can idioms be confusing for new readers?', ['Their meaning differs from what the individual words literally say', 'They are always easy to understand literally', 'They never appear in writing', 'They only exist in one language'], 0),
   ('Which is an example of an idiom?', ['The sky is blue.', 'Spill the beans', 'Two plus two equals four', 'The cat is sleeping'], 1)]),
M('Adding and Subtracting Decimals',
  'Ontario Grade 4 Number strand: adding and subtracting decimals requires lining up the decimal points so digits with the same place value are combined correctly.',
  [('What is 3.25 + 1.50?', ['4.75', '4.25', '3.75', '5.25'], 0),
   ('What is 6.80 minus 2.30?', ['4.50', '4.10', '3.50', '9.10'], 0),
   ('When adding decimals, it is important to ___.', ['Ignore the decimal point', 'Line up the decimal points', 'Always round first', 'Add only whole numbers'], 1),
   ('What is 5.05 + 2.95?', ['8.00', '7.00', '8.10', '7.90'], 0),
   ('What is 10.00 minus 4.35?', ['5.65', '6.65', '5.35', '6.35'], 0)]),
Sc('Structures: Load and Support',
   'Ontario Grade 4 Science Structures and Mechanisms strand: a load is the weight a structure must support, and good structural design distributes that load evenly to prevent collapse.',
   [('A load on a structure refers to ___.', ['The colour of the structure', 'The weight the structure must support', 'The structure\'s age', 'The material\'s smell'], 1),
    ('Why is it important for a structure to distribute load evenly?', ['To prevent weak points that could cause collapse', 'Even distribution has no benefit', 'It makes the structure heavier for no reason', 'It only matters for small structures'], 0),
    ('Which structural feature helps support heavy loads?', ['Thin, unsupported beams', 'Strong support columns or beams', 'No support at all', 'Decorative paint'], 1),
    ('A bridge is designed to safely support the load of ___.', ['Nothing at all', 'Vehicles, people, and its own weight', 'Only itself with nothing on it', 'Only light wind'], 1),
    ('What might happen if a structure\'s support cannot handle its load?', ['The structure could weaken or collapse', 'Nothing would happen', 'The structure would become stronger', 'The load would disappear'], 0)]),
SS('Early Societies: Beliefs and Traditions',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: early societies such as Egypt, Greece, Rome, Mesopotamia, and China developed belief systems, gods, and traditions that shaped their culture, art, and daily practices.',
   [('Many early societies developed belief systems that included ___.', ['No spiritual practices at all', 'Gods, traditions, and ceremonies', 'Only modern religions', 'Identical beliefs across all civilizations'], 1),
    ('Beliefs and traditions in early societies often influenced ___.', ['Nothing about daily life', 'Art, architecture, and daily practices', 'Only farming techniques', 'Only trade routes'], 1),
    ('Why do historians study the belief systems of early societies?', ['To better understand their culture, values, and way of life', 'Beliefs have no connection to culture', 'It has no historical value', 'Only written laws matter to historians'], 0),
    ('Which is an example of how belief systems shaped early societies?', ['Building temples and monuments for religious purposes', 'Beliefs had no effect on architecture', 'All societies built the same structures for the same reasons', 'Beliefs only affected modern societies'], 0),
    ('Comparing beliefs across early societies shows that ___.', ['Different societies expressed traditions in unique but sometimes similar ways', 'All beliefs were exactly identical worldwide', 'Beliefs never varied across regions', 'Only one early society had any beliefs'], 0)])]),

day(35, [
L('Reading: Making Predictions',
  'Ontario Grade 4 Reading strand: making predictions means using clues from the title, pictures, and text so far to thoughtfully guess what might happen next in a story.',
  [('Making a prediction while reading means ___.', ['Randomly guessing with no clues', 'Using clues from the text to thoughtfully guess what happens next', 'Skipping to the end of the book', 'Ignoring the story completely'], 1),
   ('Which is a good source of clues for making predictions?', ['The title and pictures', 'The price of the book', 'The font style', 'The publisher\'s name'], 0),
   ('Why do good readers make predictions while reading?', ['It keeps them thinking actively and engaged with the text', 'Predictions are not useful for reading', 'It replaces the need to read the rest of the story', 'It only works for non-fiction texts'], 0),
   ('If a story\'s cover shows dark clouds and a worried character, you might predict ___.', ['A cheerful, sunny beginning', 'Something tense or stormy may happen', 'The story is a cookbook', 'Nothing can be predicted from a cover'], 1),
   ('After making a prediction, good readers should ___.', ['Never think about it again', 'Check whether the story confirms or changes their prediction', 'Assume they are always correct', 'Stop reading immediately'], 1)]),
M('Classifying Triangles',
  'Ontario Grade 4 Geometry strand: triangles can be classified by their sides (equilateral, isosceles, scalene) and by their angles (right, acute, obtuse).',
  [('A triangle with all three sides equal is called ___.', ['Scalene', 'Isosceles', 'Equilateral', 'Right'], 2),
   ('A triangle with exactly two equal sides is called ___.', ['Equilateral', 'Isosceles', 'Scalene', 'Obtuse'], 1),
   ('A triangle with no equal sides is called ___.', ['Equilateral', 'Isosceles', 'Scalene', 'Right'], 2),
   ('A triangle with one 90-degree angle is called a ___ triangle.', ['Acute', 'Obtuse', 'Right', 'Equilateral'], 2),
   ('A triangle with all angles less than 90 degrees is called ___.', ['Obtuse', 'Right', 'Acute', 'Scalene'], 2)]),
Sc('Space: Constellations and the Night Sky',
   'Ontario Grade 4 Science Earth and Space Systems strand: constellations are patterns of stars that people have named and used for navigation and storytelling, appearing to shift position across the seasons.',
   [('A constellation is a ___.', ['Single bright star', 'Pattern of stars that has been named', 'Type of planet', 'Type of moon'], 1),
    ('Constellations have historically been used for ___.', ['Cooking recipes', 'Navigation and storytelling', 'Building materials', 'Measuring temperature'], 1),
    ('Which is a well-known constellation visible from Canada?', ['The Great Lakes', 'The Big Dipper', 'The Rocky Mountains', 'The Arctic Circle'], 1),
    ('Why do the visible constellations change with the seasons?', ['Earth\'s position in orbit around the Sun changes our view of the night sky', 'Stars physically move very quickly', 'Constellations disappear each season', 'The sky is different every night randomly'], 0),
    ('Constellations are best observed ___.', ['During the bright daytime', 'On a clear night away from bright city lights', 'Only during a full moon', 'Only in summer'], 1)]),
SS('Comparing Physical Regions of Canada',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada includes diverse physical regions, such as the Canadian Shield, the Prairies, the Rocky Mountains, and coastal areas, each with distinct landforms and climates.',
   [('Which physical region of Canada is known for flat, fertile farmland?', ['The Rocky Mountains', 'The Prairies', 'The Arctic', 'The Canadian Shield'], 1),
    ('The Canadian Shield is mainly made up of ___.', ['Sand dunes', 'Ancient rock, forests, and lakes', 'Tropical rainforest', 'Ocean floor'], 1),
    ('Which region features tall, rugged mountains in western Canada?', ['The Prairies', 'The Rocky Mountains', 'The St. Lawrence Lowlands', 'The Arctic tundra'], 1),
    ('Why do Canada\'s physical regions have different climates and landscapes?', ['Their location, landforms, and distance from oceans affect their climate', 'All regions of Canada have identical climates', 'Climate has no connection to landforms', 'Canada has only one physical region'], 0),
    ('Comparing physical regions helps students understand ___.', ['How geography shapes where and how people live', 'That geography has no effect on communities', 'That Canada is entirely flat', 'That climate is the same everywhere in Canada'], 0)])]),

day(36, [
L('Vocabulary: Homophones',
  'Ontario Grade 4 Language strand: homophones are words that sound the same but have different spellings and meanings, such as their/there/they are, or to/too/two.',
  [('Which set of words are homophones?', ['Big and small', 'Their, there, they are', 'Run and walk', 'Happy and sad'], 1),
   ('Choose the correct homophone: ___ going to the park.', ['Their', 'There', 'They are', 'They\'re'], 3),
   ('Choose the correct homophone: I left my book over ___.', ['their', 'there', 'they are', 'they\'re'], 1),
   ('Homophones are words that ___.', ['Are spelled the same but sound different', 'Sound the same but have different spellings and meanings', 'Always mean the exact same thing', 'Are never used in writing'], 1),
   ('Which is the correct use: I have ___ apples.', ['to', 'too', 'two', 'there'], 2)]),
M('Introducing Quadrilaterals',
  'Ontario Grade 4 Geometry strand: a quadrilateral is any shape with four sides, including squares, rectangles, rhombuses, and trapezoids, each with their own specific properties.',
  [('A quadrilateral always has how many sides?', ['Three', 'Four', 'Five', 'Six'], 1),
   ('Which shape is a quadrilateral with four equal sides and four right angles?', ['Trapezoid', 'Square', 'Triangle', 'Circle'], 1),
   ('A rectangle has ___ pairs of equal opposite sides.', ['Zero', 'One', 'Two', 'Four'], 2),
   ('A trapezoid has exactly how many parallel sides?', ['Zero', 'One pair', 'Two pairs', 'Four pairs'], 1),
   ('Which of these is NOT a quadrilateral?', ['Square', 'Rectangle', 'Triangle', 'Rhombus'], 2)]),
Sc('Weather Instruments and Measurement',
   'Ontario Grade 4 Science Earth and Space Systems strand: scientists use instruments such as thermometers, rain gauges, and wind vanes to measure and track weather conditions like temperature, precipitation, and wind direction.',
   [('A thermometer is used to measure ___.', ['Wind direction', 'Temperature', 'Rainfall amount', 'Air pressure only'], 1),
    ('A rain gauge is used to measure ___.', ['Temperature', 'The amount of precipitation', 'Wind speed', 'Cloud colour'], 1),
    ('A wind vane is used to determine ___.', ['Temperature', 'Wind direction', 'Rainfall totals', 'Humidity'], 1),
    ('Why do meteorologists use weather instruments?', ['To accurately measure and track weather conditions', 'Instruments provide no useful weather data', 'To guess randomly instead of measuring', 'Weather cannot be measured'], 0),
    ('Which instrument would help you know if a storm brought a lot of rain?', ['Wind vane', 'Rain gauge', 'Compass', 'Thermometer'], 1)]),
SS('Indigenous Peoples: Contributions to Canadian Society',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: Indigenous peoples have made significant and lasting contributions to Canadian society, including knowledge of the land, agriculture, medicine, governance, and culture.',
   [('Indigenous peoples have contributed knowledge about ___ to Canadian society.', ['Nothing of lasting value', 'The land, agriculture, and medicine', 'Only modern technology', 'Foreign countries only'], 1),
    ('Which crop, first cultivated by Indigenous peoples, remains important today?', ['Rice', 'Corn', 'Coffee', 'Bananas'], 1),
    ('Indigenous governance systems have influenced ideas about ___.', ['Nothing related to modern government', 'Cooperation and consensus-based decision making', 'Only ancient practices with no modern relevance', 'Foreign political systems only'], 1),
    ('Why is it important to recognize Indigenous contributions to Canada?', ['It provides a fuller, more accurate understanding of Canadian history and culture', 'Indigenous contributions are unimportant', 'Canadian history began only with European settlers', 'It has no educational value'], 0),
    ('Indigenous art, storytelling, and traditions continue to ___ Canadian culture today.', ['Have no influence on', 'Enrich and influence', 'Be completely separate from', 'Replace entirely'], 1)])]),

day(37, [
L('Writing: Poetry',
  'Ontario Grade 4 Writing strand: poetry uses rhythm, imagery, and sometimes rhyme to express ideas and feelings in a creative, condensed form, often organized into lines and stanzas.',
  [('A stanza in a poem is similar to a ___ in prose writing.', ['Chapter', 'Paragraph', 'Book title', 'Footnote'], 1),
   ('Poetry often uses ___ to create vivid mental pictures for the reader.', ['Only numbers', 'Imagery', 'Blank pages', 'Random letters'], 1),
   ('Rhyme in poetry means ___.', ['Words with the same ending sound', 'Words with opposite meanings', 'Random unrelated words', 'Only long words'], 0),
   ('Which is a common feature of poetry?', ['Rhythm and word choice for effect', 'Strict business formatting', 'No creativity allowed', 'Only true, factual statements'], 0),
   ('Why might a poet choose poetry instead of a regular paragraph to express an idea?', ['To use rhythm, imagery, and condensed language for creative effect', 'Poetry cannot express any real ideas', 'Paragraphs are not allowed to express feelings', 'There is no reason to choose poetry'], 0)]),
M('Factors and Multiples',
  'Ontario Grade 4 Number strand: a factor is a number that divides evenly into another number, while a multiple is the result of multiplying a number by a whole number.',
  [('Which is a factor of 12?', ['5', '4', '7', '9'], 1),
   ('Which is a multiple of 6?', ['15', '18', '20', '25'], 1),
   ('A factor of a number ___ evenly into it.', ['Divides', 'Never divides', 'Multiplies infinitely', 'Has no relationship'], 0),
   ('List the factors of 10.', ['1, 2, 5, 10', '1, 3, 5, 10', '2, 4, 5, 10', '1, 2, 4, 10'], 0),
   ('The first three multiples of 7 are ___.', ['7, 14, 21', '7, 8, 9', '1, 7, 14', '7, 17, 27'], 0)]),
Sc('Sound: How Sound Travels Through Materials',
   'Ontario Grade 4 Science Matter and Energy strand: sound is a vibration that travels through different materials -- solids, liquids, and gases -- typically fastest through solids and slowest through gases like air.',
   [('Sound travels as a type of ___.', ['Vibration', 'Light wave', 'Solid object', 'Chemical reaction'], 0),
    ('Sound generally travels fastest through ___.', ['Air', 'Water', 'Solids', 'A vacuum with nothing in it'], 2),
    ('Sound cannot travel through ___.', ['Air', 'Water', 'Metal', 'A complete vacuum (empty space)'], 3),
    ('Why can you sometimes hear sound better with your ear against a solid surface, like a table?', ['Sound travels efficiently through solid materials', 'Solids block all sound', 'Sound cannot travel through solids', 'It has nothing to do with vibrations'], 0),
    ('Which best describes how sound moves through air to reach our ears?', ['As vibrating air particles carrying the sound wave', 'Sound does not move at all', 'Only through complete silence', 'As a beam of light'], 0)]),
SS('Canada\'s Relationships with Other Countries',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada maintains relationships with other countries through trade, diplomacy, and international cooperation, which affect its economy and global connections.',
   [('Trade with other countries allows Canada to ___.', ['Only sell goods, never buy any', 'Exchange goods and services with the rest of the world', 'Avoid all international contact', 'Stop producing its own goods entirely'], 1),
    ('Diplomacy between countries generally involves ___.', ['Communication and cooperation between governments', 'Avoiding all communication', 'Only military action', 'Ignoring international issues'], 0),
    ('Which is an example of an item Canada might export to other countries?', ['Natural resources like lumber or minerals', 'Nothing, Canada exports no goods', 'Only imported goods', 'Items made exclusively in other countries'], 0),
    ('Why are international relationships important for Canada\'s economy?', ['They create trade opportunities that support jobs and economic growth', 'International relationships have no economic effect', 'Canada\'s economy operates in complete isolation', 'Trade only benefits other countries, never Canada'], 0),
    ('International cooperation between countries can help address ___.', ['Nothing of global importance', 'Shared challenges, such as environmental or economic issues', 'Only local town issues', 'Problems within a single country only'], 1)])]),

day(38, [
L('Media Literacy: Advertising Techniques',
  'Ontario Grade 4 Media Literacy strand: advertisers use techniques such as emotional appeals, celebrity endorsements, and repetition to persuade audiences to buy products or believe messages.',
  [('An emotional appeal in advertising tries to ___.', ['Present only statistics', 'Persuade by triggering feelings like excitement or happiness', 'Avoid influencing the audience at all', 'Only use plain black-and-white text'], 1),
   ('A celebrity endorsement in an ad means ___.', ['A famous person promotes the product', 'The product has no advertising at all', 'Only scientists appear in the ad', 'The ad contains no persuasive elements'], 0),
   ('Repetition in advertising is used to ___.', ['Make audiences forget the product', 'Help the audience remember the brand or message', 'Confuse viewers on purpose', 'Slow down the ad\'s pacing for no reason'], 1),
   ('Why should viewers think critically about advertising techniques?', ['To recognize persuasion methods and make informed decisions', 'Critical thinking is unnecessary for ads', 'All ads present only unbiased facts', 'Advertising has no techniques worth noticing'], 0),
   ('Which is an example of an advertising technique?', ['Using a catchy jingle or slogan', 'Providing no information about the product', 'Refusing to show the product', 'Avoiding any persuasive language'], 0)]),
M('Patterning: Input-Output Tables',
  'Ontario Grade 4 Algebra strand: an input-output table shows how a rule transforms an input number into an output number, helping students identify and apply numeric rules.',
  [('If the rule is add 5, what is the output when the input is 3?', ['8', '3', '5', '15'], 0),
   ('If the rule is multiply by 2, what is the output when the input is 6?', ['8', '12', '3', '6'], 1),
   ('In an input-output table, the input is ___.', ['The starting number before applying the rule', 'Always the final answer', 'Never used in the table', 'The name of the rule'], 0),
   ('If input 4 gives output 12, and input 5 gives output 15, what is the rule?', ['Add 8', 'Multiply by 3', 'Subtract 1', 'Divide by 3'], 1),
   ('Input-output tables are useful because they help you ___.', ['Identify and apply a consistent numeric rule', 'Guess randomly with no pattern', 'Avoid using any math rules', 'Replace the need for addition'], 0)]),
Sc('Light: Absorption and Colour',
   'Ontario Grade 4 Science Matter and Energy strand: objects appear a certain colour based on which wavelengths of light they reflect and which they absorb; a black object absorbs most light, while a white object reflects most light.',
   [('A black object appears black because it ___ most light.', ['Reflects', 'Absorbs', 'Creates', 'Ignores'], 1),
    ('A white object appears white because it ___ most light.', ['Absorbs', 'Reflects', 'Blocks completely', 'Destroys'], 1),
    ('An object appears a certain colour based on which light wavelengths it ___.', ['Reflects', 'Destroys permanently', 'Creates from nothing', 'Ignores entirely'], 0),
    ('On a sunny day, why might a black shirt feel hotter than a white shirt?', ['Black absorbs more light energy, which converts to heat', 'Black reflects all light energy away', 'Colour has no effect on heat absorption', 'White absorbs more heat than black'], 0),
    ('If an object reflects only green light and absorbs the rest, it will appear ___.', ['Red', 'Green', 'Blue', 'Black'], 1)]),
SS('Landforms and Bodies of Water in Canada',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada contains diverse landforms and bodies of water, including mountains, plains, rivers, and lakes, such as the Great Lakes and the St. Lawrence River.',
   [('Which are the five connected lakes on the Canada-United States border?', ['The Great Lakes', 'The Rocky Lakes', 'The Prairie Lakes', 'The Arctic Lakes'], 0),
    ('The St. Lawrence River is important because it ___.', ['Has no significance to Canada', 'Connects the Great Lakes to the Atlantic Ocean, supporting trade and travel', 'Is located entirely in another country', 'Is a small, unused stream'], 1),
    ('Which landform is a large, flat area often used for farming?', ['Mountain range', 'Plain', 'Canyon', 'Volcano'], 1),
    ('Studying Canada\'s landforms and water bodies helps us understand ___.', ['How geography influences where communities settle and how they live', 'That geography has no effect on daily life', 'That Canada has no significant water bodies', 'That all of Canada looks the same'], 0),
    ('Which is an example of a landform found in Canada?', ['Mountains', 'A skyscraper', 'A shopping mall', 'A highway'], 0)])]),

day(39, [
L('Grammar: Quotation Marks and Dialogue',
  'Ontario Grade 4 Writing strand: quotation marks show the exact words a person says in dialogue, with punctuation like commas and periods placed carefully to show who is speaking.',
  [('Quotation marks are used to show ___.', ['A character\'s thoughts only', 'The exact words someone says', 'The title of a chapter', 'A math equation'], 1),
   ('Which sentence correctly uses quotation marks?', ['Maria said, I am ready to go.', 'Maria said, “I am ready to go.”', 'Maria said I am ready to go.', '“Maria said I am ready to go'], 1),
   ('Dialogue in a story refers to ___.', ['The setting description', 'Conversation between characters', 'The book\'s cover art', 'The table of contents'], 1),
   ('In dialogue, a comma is often placed ___.', ['Outside the quotation marks always', 'Before the closing quotation mark, before the speaker tag', 'Never used in dialogue', 'Only at the end of the whole story'], 1),
   ('Why is dialogue useful in storytelling?', ['It shows characters\' personalities and moves the plot forward through their speech', 'Dialogue has no effect on a story', 'It is only used in non-fiction', 'It replaces the need for a plot'], 0)]),
M('Multi-Step Word Problems',
  'Ontario Grade 4 Number strand: multi-step word problems require identifying and completing more than one operation in the correct order to reach a final answer.',
  [('A store had 240 toys, sold 85, then received a shipment of 60 more. How many toys now?', ['215', '155', '385', '325'], 0),
   ('Liam saved $45, spent $18, then earned $12 more. How much does Liam have now?', ['$39', '$63', '$27', '$75'], 0),
   ('A school has 4 classes of 25 students each, and 10 students are absent today. How many are present?', ['110', '90', '100', '85'], 1),
   ('Solving a multi-step problem requires you to ___.', ['Use only one operation and ignore the rest', 'Complete each necessary step in the correct order', 'Guess the final number', 'Skip the information given'], 1),
   ('A baker made 150 muffins, sold 3 dozen, then baked 24 more. How many muffins are there now?', ['138', '186', '126', '150'], 0)]),
Sc('Electricity: Conductors and Insulators',
   'Ontario Grade 4 Science Matter and Energy strand: conductors, like most metals, allow electricity to flow through them easily, while insulators, like rubber and plastic, resist the flow of electricity and are used for safety.',
   [('A conductor is a material that ___.', ['Blocks electricity completely', 'Allows electricity to flow through it easily', 'Has no effect on electricity', 'Is always made of wood'], 1),
    ('An insulator is a material that ___.', ['Allows electricity to flow freely', 'Resists the flow of electricity', 'Is always metal', 'Creates electricity from nothing'], 1),
    ('Which material is typically a good conductor?', ['Rubber', 'Copper', 'Plastic', 'Wood'], 1),
    ('Why are electrical wires often covered in rubber or plastic?', ['To insulate them and prevent dangerous electric shocks', 'To make the wires conduct more electricity', 'Covering wires has no safety purpose', 'To make wires heavier'], 0),
    ('Which of these is typically used as an insulator?', ['Copper wire', 'Aluminum', 'Rubber', 'Steel'], 2)]),
SS('How Canada\'s Provinces and Territories Formed',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada\'s provinces and territories joined the country at different times in history, starting with Confederation in 1867 and continuing as new provinces and territories were added.',
   [('In what year did Confederation create the original Dominion of Canada?', ['1812', '1867', '1900', '1776'], 1),
    ('Canada\'s provinces and territories joined the country ___.', ['All at exactly the same time', 'At different times throughout history', 'Before Confederation only', 'They have never changed since 1867'], 1),
    ('How many provinces and territories make up Canada today?', ['Eight', 'Ten provinces and three territories', 'Five', 'Twenty'], 1),
    ('Why is it useful to learn how Canada\'s provinces and territories formed?', ['It helps explain Canada\'s history and how the country grew over time', 'It has no connection to understanding Canada today', 'Provinces have always existed exactly as they are now', 'This history has no educational value'], 0),
    ('Confederation in 1867 originally united which regions?', ['All ten current provinces at once', 'Ontario, Quebec, Nova Scotia, and New Brunswick', 'Only the territories', 'British Columbia and Alberta only'], 1)])]),

day(40, [
L('Reading: Determining Importance',
  'Ontario Grade 4 Reading strand: determining importance means identifying which details in a text are essential to understanding it, separating key information from interesting but less important details.',
  [('Determining importance while reading means ___.', ['Remembering every single detail equally', 'Identifying which details are most essential to understanding the text', 'Skipping the text entirely', 'Ignoring the main idea'], 1),
   ('Which is more likely to be an essential detail in an informational text?', ['A key fact directly supporting the main idea', 'An unrelated side comment', 'The font used in the book', 'The page number'], 0),
   ('Why is determining importance a useful reading strategy?', ['It helps readers focus on and remember the most meaningful information', 'It has no benefit while reading', 'It means ignoring the main idea', 'It replaces the need to read carefully'], 0),
   ('When summarizing a text, determining importance helps you ___.', ['Include every single detail from the text', 'Choose only the most essential information to include', 'Avoid understanding the text', 'Add unrelated new information'], 1),
   ('Which reading skill is closely related to determining importance?', ['Identifying the main idea', 'Ignoring punctuation', 'Skipping the title', 'Reading only the last page'], 0)]),
M('Coordinate Grids: Plotting Points',
  'Ontario Grade 4 Geometry strand: a coordinate grid uses a horizontal x-axis and vertical y-axis to locate points using ordered pairs, such as (3, 2), which means 3 units across and 2 units up.',
  [('In the ordered pair (3, 2), which number represents the horizontal position?', ['2', '3', 'Both equally', 'Neither'], 1),
   ('The horizontal axis on a coordinate grid is called the ___.', ['Y-axis', 'X-axis', 'Z-axis', 'Origin'], 1),
   ('The point where the x-axis and y-axis meet is called the ___.', ['Endpoint', 'Origin', 'Vertex', 'Coordinate'], 1),
   ('To plot the point (4, 1), you would move ___.', ['4 units up, 1 unit across', '4 units across, 1 unit up', '1 unit across, 4 units down', 'Nowhere, since the point does not exist'], 1),
   ('An ordered pair like (2, 5) is written in the order ___.', ['(y, x)', '(x, y)', 'Random order', 'Only y-values'], 1)]),
Sc('Erosion and Its Effects on Landforms',
   'Ontario Grade 4 Science Earth and Space Systems strand: erosion is the gradual wearing away and movement of soil and rock by wind, water, or ice, slowly shaping landforms like valleys and canyons over long periods of time.',
   [('Erosion is best described as the ___.', ['Sudden creation of new rock', 'Gradual wearing away and movement of soil and rock', 'Instant disappearance of mountains', 'Formation of clouds'], 1),
    ('Which of these can cause erosion?', ['Wind, water, and ice', 'Only bright sunlight', 'Only complete stillness', 'Nothing natural causes erosion'], 0),
    ('A river slowly carving out a canyon over time is an example of ___.', ['Erosion', 'Evaporation', 'Condensation', 'Combustion'], 0),
    ('Erosion typically occurs ___.', ['Instantly, within seconds', 'Gradually, often over long periods of time', 'Only underground', 'Only in outer space'], 1),
    ('Why might people plant vegetation along a riverbank?', ['Plant roots can help hold soil in place and reduce erosion', 'Plants speed up erosion significantly', 'Vegetation has no effect on erosion', 'To make erosion happen faster'], 0)]),
SS('My Role as a Canadian Citizen',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: being a Canadian citizen involves rights, such as voting when old enough, and responsibilities, such as respecting laws, the environment, and the wellbeing of the community.',
   [('A responsibility of Canadian citizens includes ___.', ['Ignoring community needs', 'Respecting laws and contributing to the community', 'Avoiding all civic participation', 'Breaking rules whenever convenient'], 1),
    ('Once old enough, Canadian citizens gain the right to ___.', ['Ignore all laws', 'Vote in elections', 'Avoid paying any attention to government', 'Skip all civic duties'], 1),
    ('Why might a student get involved in a local community project?', ['To practice being an active, responsible citizen', 'Community involvement has no value', 'Only adults can contribute to communities', 'It is required to skip school'], 0),
    ('Respecting the environment is considered part of good citizenship because ___.', ['Protecting shared resources benefits the whole community', 'The environment has no connection to citizenship', 'Only government workers must consider the environment', 'It has no lasting impact on anyone'], 0),
    ('Reflecting on your role as a citizen helps you understand ___.', ['How your actions can positively contribute to your community and country', 'That individual actions never matter', 'That citizenship applies only to adults', 'That being a citizen has no responsibilities'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260711):
    """Same technique used for the Grade 3 batches -- see
    gen_grade3_days31_40.py for the full rationale. Reassigns each
    question's correct-answer slot via a shuffled round-robin (even across
    0-3) and shuffles the wrong options into the remaining slots. Question
    and option TEXT is never changed. Mutates `days` in place."""
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
    _rebalance_answer_positions(g4_31_40)
    append_to(4, g4_31_40)
