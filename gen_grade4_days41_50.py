#!/usr/bin/env python3
"""Phase 3: Grade 4, Days 41-50 (second batch for Grade 4, continuing the
10-day pattern established for Grade 3). Topics chosen to avoid any
overlap with the existing Day 1-40 set (see data/grade4.json after the
Days 31-40 batch) and to draw on Ontario Grade 4 curriculum strands not
yet covered: point of view, irregular verbs, personification, remainders,
symmetry, magnetism, decomposers, Ancient India, Canada's territories,
and municipal government.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded double-quote characters are used anywhere in
question/summary/option text (gen_curriculum.py's serializer doesn't
escape them); where a literal quotation mark is pedagogically needed,
curly Unicode quotes (“ ”) are used instead of ASCII double quotes.
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


g4_41_50 = [
day(41, [
L('Reading: Point of View',
  'Ontario Grade 4 Reading strand: point of view is the perspective from which a story is told, either first person (using I or we) or third person (using he, she, or they).',
  [('A story told using I or we is written in ___ point of view.', ['Second person', 'First person', 'Third person', 'No point of view'], 1),
   ('A story told using he, she, or they is written in ___ point of view.', ['First person', 'Third person', 'Second person', 'No point of view'], 1),
   ('Point of view refers to ___.', ['The book’s page count', 'The perspective from which a story is told', 'The font used in a book', 'The publisher of a book'], 1),
   ('Why does point of view matter to a reader?', ['It shapes what information and feelings the reader has access to', 'It has no effect on how a story is understood', 'It only affects the book’s cover', 'Point of view never changes a story'], 0),
   ('Which pronoun signals first-person point of view?', ['She', 'They', 'I', 'He'], 2)]),
M('Division with Remainders',
  'Ontario Grade 4 Number strand: when a number does not divide evenly, the amount left over is called the remainder, written as R after the quotient, such as 17 divided by 5 equals 3 remainder 2.',
  [('What is 17 divided by 5?', ['3 remainder 1', '3 remainder 2', '4 remainder 0', '3 remainder 3'], 1),
   ('A remainder is ___.', ['The amount left over after dividing evenly', 'Always zero', 'The same as the quotient', 'Only used in multiplication'], 0),
   ('What is 23 divided by 4?', ['5 remainder 3', '5 remainder 2', '6 remainder 0', '4 remainder 3'], 0),
   ('If a division problem has no remainder, the numbers divide ___.', ['Unevenly', 'Evenly', 'Incorrectly', 'Randomly'], 1),
   ('What is 29 divided by 6?', ['4 remainder 5', '5 remainder 4', '4 remainder 4', '5 remainder 5'], 0)]),
Sc('Life Cycles of Animals',
   'Ontario Grade 4 Science Life Systems strand: many animals go through distinct life cycle stages, such as egg, larva, pupa, and adult for insects, or birth, growth, and maturity for mammals.',
   [('Which is a typical life cycle stage for many insects?', ['Egg, larva, pupa, adult', 'Seed, sprout, flower', 'Only adult, with no other stages', 'Egg and adult only, with nothing between'], 0),
    ('A caterpillar is which stage in a butterfly’s life cycle?', ['Egg', 'Larva', 'Pupa', 'Adult'], 1),
    ('Mammals typically go through stages including ___.', ['Birth, growth, and maturity', 'Egg and pupa only', 'Only an adult stage', 'No identifiable stages'], 0),
    ('Why is studying life cycles useful in science?', ['It helps explain how living things grow, change, and reproduce over time', 'Life cycles have no scientific value', 'All animals have identical life cycles', 'Life cycles never change'], 0),
    ('The pupa stage in an insect’s life cycle is when ___.', ['The insect transforms into its adult form', 'The insect is first laid as an egg', 'The insect stops developing permanently', 'Nothing happens at all'], 0)]),
SS('Ancient India',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient India developed along the Indus River, and is known for early city planning, a written script, and significant early achievements in mathematics.',
   [('Ancient India developed along which river?', ['The Nile', 'The Indus River', 'The Amazon', 'The Tigris'], 1),
    ('Ancient Indian cities were known for early examples of ___.', ['Random, unplanned building', 'Organized city planning', 'No buildings at all', 'Only underground homes'], 1),
    ('Which subject did Ancient India make significant early contributions to?', ['Mathematics', 'Modern computer science', 'Space travel', 'Aviation'], 0),
    ('Why do historians consider Ancient India an early major civilization?', ['It developed advanced cities, writing, and knowledge systems early in history', 'It had no notable achievements', 'It developed no lasting inventions', 'It was identical to every other ancient civilization'], 0),
    ('Studying Ancient India alongside Egypt, China, and Mesopotamia helps us ___.', ['Compare how different early civilizations developed', 'Prove that only one civilization ever existed', 'Ignore historical differences between regions', 'Avoid learning about world history'], 0)])]),

day(42, [
L('Grammar: Irregular Verbs',
  'Ontario Grade 4 Writing strand: irregular verbs do not follow the usual pattern of adding -ed for the past tense, such as go becoming went or eat becoming ate.',
  [('What is the past tense of the irregular verb go?', ['Goed', 'Went', 'Gone', 'Going'], 1),
   ('What is the past tense of the irregular verb eat?', ['Eated', 'Ate', 'Eating', 'Eats'], 1),
   ('An irregular verb is one that ___.', ['Always adds -ed for the past tense', 'Does not follow the usual -ed pattern for the past tense', 'Has no past tense form', 'Is only used in questions'], 1),
   ('What is the past tense of the irregular verb see?', ['Seed', 'Saw', 'Seeing', 'Sees'], 1),
   ('Which of these is an irregular verb?', ['Walk', 'Jump', 'Break', 'Play'], 2)]),
M('Subtracting Fractions with the Same Denominator',
  'Ontario Grade 4 Number strand: to subtract fractions with the same denominator, subtract the numerators and keep the denominator the same, such as 5/8 minus 2/8 equals 3/8.',
  [('What is 5/8 minus 2/8?', ['3/8', '7/8', '3/16', '2/8'], 0),
   ('What is 7/10 minus 4/10?', ['11/10', '3/10', '3/20', '4/10'], 1),
   ('When subtracting fractions with the same denominator, you ___.', ['Subtract the denominators only', 'Subtract the numerators and keep the denominator the same', 'Add the numerators together', 'Change the denominator each time'], 1),
   ('What is 9/12 minus 5/12?', ['4/12', '14/12', '4/24', '5/12'], 0),
   ('What is 6/9 minus 6/9?', ['1', '0/9', '12/9', '6/0'], 1)]),
Sc('Classifying Materials: Natural and Synthetic',
   'Ontario Grade 4 Science Matter and Energy strand: natural materials come directly from nature, such as wood or cotton, while synthetic materials are human-made, such as plastic or nylon.',
   [('A natural material is one that ___.', ['Is entirely human-made in a factory', 'Comes directly from nature', 'Does not exist in the real world', 'Is always metal'], 1),
    ('A synthetic material is one that is ___.', ['Found only in forests', 'Human-made', 'Always liquid', 'Impossible to produce'], 1),
    ('Which of these is a natural material?', ['Plastic', 'Nylon', 'Cotton', 'Polyester'], 2),
    ('Which of these is a synthetic material?', ['Wood', 'Wool', 'Plastic', 'Cotton'], 2),
    ('Why might a designer choose a synthetic material over a natural one?', ['Synthetic materials can offer specific properties like durability or low cost', 'Synthetic materials never have any useful properties', 'Natural materials cannot be used for anything', 'There is never a reason to choose synthetic materials'], 0)]),
SS('Comparing Early Writing Systems',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations developed different writing systems, such as hieroglyphics in Egypt, cuneiform in Mesopotamia, and early script in the Indus Valley, to record information.',
   [('Hieroglyphics was the early writing system used in ___.', ['Ancient China', 'Ancient Egypt', 'Ancient Rome', 'Ancient Greece'], 1),
    ('Cuneiform was the early writing system used in ___.', ['Mesopotamia', 'Ancient Egypt', 'Ancient India', 'Ancient China'], 0),
    ('Early writing systems were mainly developed to ___.', ['Prevent communication between people', 'Record and communicate information', 'Replace spoken language entirely', 'Decorate buildings only'], 1),
    ('Why is the development of writing considered a major milestone in early civilizations?', ['It allowed information to be recorded and passed on more reliably', 'Writing had no effect on early societies', 'Early societies never needed to record information', 'Writing systems were identical across all civilizations'], 0),
    ('Comparing writing systems across civilizations shows that ___.', ['Different societies solved the need to record information in unique ways', 'Only one civilization ever developed writing', 'All early writing systems were exactly the same', 'Writing systems have no historical significance'], 0)])]),

day(43, [
L('Writing: Book Reviews',
  'Ontario Grade 4 Writing strand: a book review shares an opinion about a book, supported by reasons and details, and often includes a brief summary along with a recommendation.',
  [('A book review typically includes ___.', ['Only the book’s price', 'An opinion supported by reasons and a brief summary', 'A list of unrelated books', 'The author’s home address'], 1),
   ('Why should a book review include supporting reasons?', ['To help the reader understand why the reviewer feels that way', 'Reasons are not needed in a review', 'Reviews should never explain opinions', 'Supporting reasons make a review less convincing'], 0),
   ('A recommendation in a book review tells the reader ___.', ['Whether the reviewer thinks others should read the book', 'The exact page count', 'The publisher’s address', 'Nothing useful'], 0),
   ('Which is an example of a detail that could support a book review?', ['Describing an exciting scene from the book', 'Listing unrelated grocery items', 'Ignoring the book completely', 'Copying the entire book word for word'], 0),
   ('A well-written book review helps other readers ___.', ['Decide whether they might enjoy the book', 'Avoid all books permanently', 'Understand only the price of books', 'Skip reading altogether'], 0)]),
M('Comparing and Ordering Decimals',
  'Ontario Grade 4 Number strand: to compare decimals, line up the decimal points and compare digits from left to right, starting with the whole number, then tenths, then hundredths.',
  [('Which decimal is greater: 0.45 or 0.5?', ['0.45', '0.5', 'They are equal', 'Cannot be compared'], 1),
   ('Which decimal is smallest: 0.3, 0.25, or 0.35?', ['0.3', '0.25', '0.35', 'They are all equal'], 1),
   ('To compare decimals, you should first compare the ___.', ['Hundredths digit', 'Whole number part', 'Colour of the numbers', 'Number of digits after the decimal'], 1),
   ('Order these from least to greatest: 0.6, 0.06, 0.66.', ['0.06, 0.6, 0.66', '0.6, 0.06, 0.66', '0.66, 0.6, 0.06', '0.06, 0.66, 0.6'], 0),
   ('Which decimal is equivalent to 0.5?', ['0.05', '0.50', '0.005', '0.55'], 1)]),
Sc('Structures: Types of Bridges',
   'Ontario Grade 4 Science Structures and Mechanisms strand: different bridge designs, such as beam, arch, and suspension bridges, use different structural principles to support loads and span distances.',
   [('A beam bridge is supported mainly by ___.', ['Cables hanging from towers', 'A straight, rigid horizontal structure', 'A curved arch shape', 'Floating pontoons only'], 1),
    ('An arch bridge uses a curved shape to help ___.', ['Distribute weight along the curve', 'Eliminate all structural support', 'Float on water', 'Avoid supporting any load'], 0),
    ('A suspension bridge is supported mainly by ___.', ['Solid concrete blocks only', 'Cables hung from tall towers', 'A single wooden beam', 'Underground tunnels'], 1),
    ('Why might engineers choose different bridge designs for different locations?', ['Different designs suit different distances, loads, and terrain', 'All bridges must use the exact same design everywhere', 'Bridge design has no connection to location', 'Only one bridge design has ever been used'], 0),
    ('Which bridge type is well-suited for spanning very long distances, like across a wide river?', ['Beam bridge', 'Suspension bridge', 'A short wooden plank', 'None of these can span long distances'], 1)]),
SS('Early Societies: Trade and Economy',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations such as Egypt, Mesopotamia, China, and India developed trade networks to exchange goods like grain, textiles, and metals with neighbouring regions.',
   [('Trade in early societies mainly involved exchanging ___.', ['Nothing at all', 'Goods such as grain, textiles, and metals', 'Only modern currency', 'Only digital information'], 1),
    ('Why did early civilizations develop trade networks?', ['To obtain resources and goods not available locally', 'Trade served no useful purpose', 'Early societies were entirely self-sufficient with no needs', 'Trade networks did not exist in early history'], 0),
    ('A trade network connects ___.', ['A single isolated village with no outside contact', 'Different regions or civilizations exchanging goods', 'Nothing, since trade never happened historically', 'Only modern countries'], 1),
    ('Which might an early civilization export if it had abundant farmland?', ['Grain or other crops', 'Items it does not produce at all', 'Nothing, since exporting is impossible', 'Only imported goods'], 0),
    ('Studying early trade helps us understand ___.', ['How ancient economies and connections between regions developed', 'That ancient civilizations never interacted with each other', 'That trade began only in modern times', 'That economies have no historical importance'], 0)])]),

day(44, [
L('Figurative Language: Personification',
  'Ontario Grade 4 Reading strand: personification gives human qualities or actions to non-human things or ideas, such as saying the wind whispered or the sun smiled down.',
  [('Personification is when a writer gives ___.', ['Human qualities to non-human things', 'Numbers to letters', 'Colours to sounds', 'No meaning to a sentence'], 0),
   ('Which sentence is an example of personification?', ['The wind whispered through the trees.', 'The wind is made of moving air.', 'The wind speed was 20 kilometres per hour.', 'The wind comes from changes in air pressure.'], 0),
   ('Why do writers use personification?', ['To make descriptions more vivid and engaging', 'To confuse the reader on purpose', 'To remove all imagery from writing', 'Personification has no purpose in writing'], 0),
   ('Which phrase uses personification?', ['The flowers danced in the breeze.', 'The flowers are red and yellow.', 'The flowers grow in the garden.', 'The flowers need water and sunlight.'], 0),
   ('Personification is a type of ___.', ['Punctuation mark', 'Figurative language', 'Grammar rule', 'Spelling pattern'], 1)]),
M('Symmetry',
  'Ontario Grade 4 Geometry strand: a shape has line symmetry if it can be folded along a line so both halves match exactly, and that fold line is called a line of symmetry.',
  [('A shape has line symmetry if ___.', ['It can be folded so both halves match exactly', 'It has no straight edges', 'It cannot be folded at all', 'It has more than four sides'], 0),
   ('The line along which a symmetrical shape can be folded is called a ___.', ['Diagonal', 'Line of symmetry', 'Perimeter line', 'Coordinate'], 1),
   ('How many lines of symmetry does a square have?', ['One', 'Two', 'Four', 'Zero'], 2),
   ('Which letter of the alphabet has a vertical line of symmetry?', ['F', 'A', 'R', 'G'], 1),
   ('A circle has how many lines of symmetry?', ['Zero', 'One', 'Four', 'An infinite number'], 3)]),
Sc('Forces: Magnetism',
   'Ontario Grade 4 Science Structures and Mechanisms strand: magnetism is a force that attracts certain metals, such as iron, and every magnet has a north pole and a south pole.',
   [('Magnetism is a force that attracts ___.', ['All materials equally', 'Certain metals, such as iron', 'Only wood', 'Only liquids'], 1),
    ('Every magnet has ___.', ['Only a north pole', 'A north pole and a south pole', 'No poles at all', 'Three poles'], 1),
    ('What happens when two magnets’ like poles (north-north or south-south) are brought together?', ['They attract strongly', 'They repel each other', 'Nothing happens at all', 'They stick together permanently'], 1),
    ('What happens when two magnets’ opposite poles (north-south) are brought together?', ['They repel each other', 'They attract each other', 'Nothing happens', 'They cancel out completely'], 1),
    ('Which material would a magnet most strongly attract?', ['Plastic', 'Iron', 'Wood', 'Glass'], 1)]),
SS('Early Societies: Art and Architecture',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations expressed their culture and beliefs through art and architecture, such as Egyptian pyramids, Greek temples, and Chinese pottery.',
   [('Egyptian pyramids were primarily built as ___.', ['Shopping centres', 'Tombs for pharaohs', 'Modern apartments', 'Farming storage only'], 1),
    ('Greek temples were often built to honour ___.', ['Modern celebrities', 'Gods and goddesses', 'Sports teams', 'Foreign kings only'], 1),
    ('Art and architecture in early societies often reflected their ___.', ['Complete lack of culture', 'Beliefs, values, and technology', 'Random, meaningless choices', 'Only modern influences'], 1),
    ('Why do historians study ancient art and architecture?', ['It offers insight into how early societies lived and what they valued', 'Ancient art has no historical value', 'Architecture from the past teaches us nothing', 'Only written records matter to historians'], 0),
    ('Which is an example of early architecture still studied today?', ['The pyramids of Egypt', 'A modern shopping mall', 'A smartphone', 'A highway overpass'], 0)])]),

day(45, [
L('Reading: Cause and Effect',
  'Ontario Grade 4 Reading strand: a cause is why something happens, and an effect is what happens as a result, and identifying these relationships helps readers understand how events connect in a text.',
  [('A cause is best described as ___.', ['What happens as a result of something', 'The reason why something happens', 'A character’s name', 'The title of a story'], 1),
   ('An effect is best described as ___.', ['The reason something happens', 'What happens as a result of a cause', 'A random unrelated event', 'The setting of a story'], 1),
   ('In the sentence It rained, so the game was cancelled, what is the effect?', ['It rained', 'The game was cancelled', 'Neither is an effect', 'Both are causes'], 1),
   ('Why is understanding cause and effect useful when reading?', ['It helps readers see how events in a text are connected', 'It has no impact on understanding a text', 'Cause and effect never appears in stories', 'It replaces the need to read the whole text'], 0),
   ('Which phrase often signals a cause-and-effect relationship?', ['Once upon a time', 'Because of this', 'The end', 'In a faraway land'], 1)]),
M('Perimeter and Area of Irregular Shapes',
  'Ontario Grade 4 Geometry strand: irregular shapes can be broken into smaller regular shapes, like rectangles, to calculate their total perimeter or area by adding the parts together.',
  [('To find the area of an irregular shape, you can ___.', ['Ignore parts of the shape', 'Break it into smaller regular shapes and add their areas', 'Multiply only the longest side', 'Guess without calculating'], 1),
   ('An L-shaped figure can be split into how many rectangles to find its area?', ['Zero', 'One only', 'Two', 'It cannot be split'], 2),
   ('Perimeter is the measurement of ___.', ['The space inside a shape', 'The distance around the outside of a shape', 'The shape’s volume', 'The shape’s weight'], 1),
   ('If two rectangles that make up an irregular shape have areas of 12 and 8 square units, the total area is ___.', ['4 square units', '20 square units', '96 square units', '10 square units'], 1),
   ('Why is it useful to break an irregular shape into rectangles?', ['Rectangles are easier to measure and calculate area for', 'It makes the shape disappear', 'It is never useful', 'Rectangles cannot be measured'], 0)]),
Sc('Ecosystems: Producers, Consumers, and Decomposers',
   'Ontario Grade 4 Science Life Systems strand: in an ecosystem, producers (like plants) make their own food, consumers (like animals) eat other organisms, and decomposers (like fungi) break down dead material.',
   [('A producer in an ecosystem is an organism that ___.', ['Eats other organisms only', 'Makes its own food', 'Breaks down dead material', 'Does nothing in the ecosystem'], 1),
    ('A consumer in an ecosystem is an organism that ___.', ['Makes its own food using sunlight', 'Eats other organisms for energy', 'Breaks down dead material only', 'Has no role in the ecosystem'], 1),
    ('A decomposer’s role in an ecosystem is to ___.', ['Make food using sunlight', 'Break down dead plants and animals', 'Hunt other consumers', 'Produce oxygen only'], 1),
    ('Which of these is typically classified as a producer?', ['A mushroom', 'A plant', 'A wolf', 'A bird'], 1),
    ('Why are decomposers important to an ecosystem?', ['They recycle nutrients back into the soil for producers to use', 'They have no effect on the ecosystem', 'They prevent all growth in an ecosystem', 'They only consume other consumers'], 0)]),
SS('Canada’s Territories: Yukon, Northwest Territories, and Nunavut',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada’s three territories -- Yukon, the Northwest Territories, and Nunavut -- make up the northern part of the country and have unique geography, climate, and Indigenous communities.',
   [('How many territories does Canada have?', ['One', 'Two', 'Three', 'Five'], 2),
    ('Which of these is one of Canada’s three territories?', ['Alberta', 'Nunavut', 'Ontario', 'Quebec'], 1),
    ('Canada’s territories are located mainly in the ___ part of the country.', ['Southern', 'Northern', 'Eastern coastal', 'Western coastal only'], 1),
    ('The climate in Canada’s territories is generally ___.', ['Tropical and warm year-round', 'Cold, with long winters', 'Identical to southern Canada', 'Desert-like with no snow'], 1),
    ('Why is it important to learn about Canada’s territories?', ['They are a significant part of Canada’s geography, culture, and Indigenous communities', 'They have no significance to Canada', 'They are not actually part of Canada', 'They have no distinct geography or culture'], 0)])]),

day(46, [
L('Vocabulary: Multiple-Meaning Words',
  'Ontario Grade 4 Language strand: multiple-meaning words are spelled the same but can have different meanings depending on how they are used in a sentence, such as bat, bank, or watch.',
  [('The word bat can mean ___.', ['Only a flying animal', 'A flying animal or sports equipment, depending on context', 'Only a type of tree', 'Only a colour'], 1),
   ('In the sentence I watched the clock on my watch, the two uses of watch mean ___.', ['The exact same thing both times', 'Different things: looked at, and a wristwatch', 'Neither use makes sense', 'Both refer to a type of bird'], 1),
   ('A multiple-meaning word is one that ___.', ['Has only one possible meaning', 'Can have different meanings depending on context', 'Is always spelled differently for each meaning', 'Cannot be used in a sentence'], 1),
   ('The word bank can refer to ___.', ['Only a financial institution', 'A financial institution or the side of a river, depending on context', 'Only a type of fish', 'Only a type of vehicle'], 1),
   ('How can a reader figure out which meaning of a word is intended?', ['By using context clues from the surrounding sentence', 'By ignoring the rest of the sentence', 'Multiple-meaning words cannot be understood', 'By guessing randomly with no strategy'], 0)]),
M('24-Hour Clock (Military Time)',
  'Ontario Grade 4 Measurement strand: the 24-hour clock counts hours from 00:00 (midnight) to 23:59, avoiding the need for AM and PM, and is commonly used in schedules like transit and travel.',
  [('What time is 14:00 in standard 12-hour time?', ['2:00 AM', '2:00 PM', '4:00 PM', '12:00 PM'], 1),
   ('On the 24-hour clock, midnight is written as ___.', ['12:00', '00:00', '24:00 only', '1:00'], 1),
   ('What is 6:00 PM written in 24-hour time?', ['06:00', '18:00', '16:00', '20:00'], 1),
   ('The 24-hour clock is often used for ___.', ['Casual conversations only', 'Schedules such as transit and travel', 'Never used anywhere', 'Only cooking recipes'], 1),
   ('What is 09:00 in 24-hour time equivalent to in standard time?', ['9:00 AM', '9:00 PM', '7:00 AM', '11:00 AM'], 0)]),
Sc('Renewable and Non-Renewable Energy Sources',
   'Ontario Grade 4 Science Matter and Energy strand: renewable energy sources, like solar and wind, can be replenished naturally, while non-renewable sources, like coal and oil, take millions of years to form and can run out.',
   [('A renewable energy source is one that ___.', ['Can be replenished naturally over a short time', 'Takes millions of years to form', 'Can never be used again once used once', 'Always causes pollution'], 0),
    ('Which is an example of a renewable energy source?', ['Coal', 'Solar power', 'Oil', 'Natural gas'], 1),
    ('A non-renewable energy source is one that ___.', ['Can be replenished quickly', 'Takes an extremely long time to form and can run out', 'Never runs out', 'Comes only from the sun'], 1),
    ('Which is an example of a non-renewable energy source?', ['Wind power', 'Solar power', 'Coal', 'Hydroelectric power'], 2),
    ('Why is there growing interest in using more renewable energy sources?', ['They can be replenished naturally and often produce less pollution', 'Renewable sources are always worse for the environment', 'Non-renewable sources never run out', 'There is no benefit to renewable energy'], 0)]),
SS('Map Skills: Scale and Symbols',
   'Ontario Grade 4 Social Studies People and Environments strand: maps use a scale to show real-world distances in a smaller form, and symbols in a legend to represent features like cities, roads, or rivers.',
   [('A map scale helps show ___.', ['Real-world distances in a smaller form', 'The colour of the land', 'The population of a country', 'Nothing useful'], 0),
    ('Symbols on a map are explained in a ___.', ['Compass rose', 'Legend (or key)', 'Scale bar only', 'Title page'], 1),
    ('If a map scale shows 1 cm equals 10 km, a 3 cm distance on the map represents ___.', ['3 km', '10 km', '30 km', '13 km'], 2),
    ('Why do maps use symbols instead of writing out every detail?', ['Symbols make maps easier to read quickly', 'Symbols make maps impossible to understand', 'Maps are not allowed to use symbols', 'Symbols have no purpose on maps'], 0),
    ('Which might a map symbol commonly represent?', ['A city, road, or river', 'A random unrelated object', 'Nothing at all', 'Only the mapmaker’s name'], 0)])]),

day(47, [
L('Writing: Dialogue Writing',
  'Ontario Grade 4 Writing strand: dialogue writing brings characters to life through their spoken words, using quotation marks and a new paragraph each time the speaker changes.',
  [('Dialogue in a story refers to ___.', ['The setting description', 'The spoken words of characters', 'The chapter titles', 'The book’s illustrations'], 1),
   ('When writing dialogue, a new paragraph is usually started ___.', ['Never, all dialogue stays in one paragraph', 'Each time the speaker changes', 'Only at the very end of the story', 'Only when the setting changes'], 1),
   ('Why is dialogue useful in a story?', ['It reveals character personality and moves the plot forward', 'Dialogue slows down every story unnecessarily', 'Dialogue has no purpose in writing', 'Dialogue replaces the need for a plot'], 0),
   ('Which punctuation is typically used to show a character’s exact spoken words?', ['A colon', 'Quotation marks', 'A semicolon', 'Parentheses'], 1),
   ('Good dialogue should sound ___.', ['Exactly like a textbook', 'Natural, like how the character would actually speak', 'Completely random and unrelated to the character', 'Identical for every character in the story'], 1)]),
M('Pictographs',
  'Ontario Grade 4 Data Management strand: a pictograph uses pictures or symbols to represent data, with a key showing how many items each symbol stands for.',
  [('A pictograph uses ___ to represent data.', ['Only numbers written out', 'Pictures or symbols', 'Colours with no meaning', 'Random shapes with no key'], 1),
   ('The key in a pictograph tells you ___.', ['The title of the graph', 'How many items each symbol represents', 'The names of the people who made the graph', 'Nothing useful'], 1),
   ('If a pictograph key shows 1 symbol equals 5 students, and there are 4 symbols for Grade 4, how many Grade 4 students are there?', ['4', '9', '20', '5'], 2),
   ('Pictographs are especially useful for ___.', ['Making data more difficult to understand', 'Making data visually easy to compare at a glance', 'Hiding information from the reader', 'Replacing the need for any data at all'], 1),
   ('Half of a symbol in a pictograph usually represents ___.', ['Double the full value', 'Half of the value the full symbol represents', 'Zero', 'The exact same as a full symbol'], 1)]),
Sc('Simple Machines: Wheel and Axle, and Screw',
   'Ontario Grade 4 Science Structures and Mechanisms strand: a wheel and axle reduces the effort needed to move objects by rotating together, while a screw is a spiral inclined plane that converts turning motion into straight-line motion.',
   [('A wheel and axle work together by ___.', ['Rotating together to reduce the effort needed to move objects', 'Never moving at all', 'Only working separately, never together', 'Absorbing all force with no motion'], 0),
    ('A screw can be thought of as a type of ___ wrapped around a cylinder.', ['Lever', 'Inclined plane', 'Pulley', 'Wheel'], 1),
    ('Which everyday object uses a wheel and axle?', ['A doorknob', 'A flat table', 'A pane of glass', 'A brick'], 0),
    ('A screw converts ___ motion into straight-line motion.', ['Turning', 'No motion at all', 'Sliding', 'Bouncing'], 0),
    ('Why is a wheel and axle considered a simple machine?', ['It makes moving or lifting objects easier by reducing the effort required', 'It always makes tasks more difficult', 'It has no practical use', 'It only works underwater'], 0)]),
SS('Climate Zones of Canada',
   'Ontario Grade 4 Social Studies People and Environments strand: Canada spans several climate zones, from the cold Arctic in the north to milder, temperate zones in the south, influencing where people live and how they adapt.',
   [('Canada’s northern regions generally have a ___ climate.', ['Tropical', 'Cold, Arctic climate', 'Desert climate', 'Consistently warm climate'], 1),
    ('Southern Canada generally has a ___ climate compared to the north.', ['Colder', 'Milder, more temperate', 'Identical', 'Tropical'], 1),
    ('Climate zones influence ___.', ['Nothing about how people live', 'Where people settle and how they adapt their lifestyles', 'Only the colour of houses', 'Only what sports people play'], 1),
    ('Why might fewer people live in Canada’s far northern climate zones?', ['The harsh cold climate makes farming and travel more challenging', 'The north has no unique climate challenges', 'Climate has no effect on where people choose to live', 'The north is actually the warmest region in Canada'], 0),
    ('Studying climate zones helps students understand ___.', ['How geography and weather patterns vary across a large country like Canada', 'That all of Canada has the exact same weather year-round', 'That climate has no connection to geography', 'That Canada has only one climate zone'], 0)])]),

day(48, [
L('Media Literacy: Recognizing Bias in News',
  'Ontario Grade 4 Media Literacy strand: bias in news occurs when information is presented in a way that favours one side or opinion, and recognizing it helps readers evaluate sources critically.',
  [('Bias in news means the information is presented ___.', ['In a completely neutral, balanced way', 'In a way that favours one side or opinion', 'Without any point of view at all', 'Using only statistics'], 1),
   ('Why is it important for readers to recognize bias?', ['To think critically and evaluate information more carefully', 'Bias has no effect on how information is understood', 'Recognizing bias is unnecessary', 'All news is always completely unbiased'], 0),
   ('Which might be a sign of bias in a news story?', ['Presenting balanced viewpoints from multiple sources', 'Only presenting one side of an issue', 'Including verified facts and data', 'Citing multiple credible sources'], 1),
   ('Comparing multiple news sources on the same topic can help readers ___.', ['Get a more complete, balanced understanding', 'Become more confused with no benefit', 'Avoid learning anything useful', 'Guarantee that one source is entirely correct'], 0),
   ('A media-literate reader asks questions like ___.', ['What did I have for breakfast?', 'Who created this message, and why?', 'What colour is the website?', 'How long is this article?'], 1)]),
M('Predicting Outcomes with Probability',
  'Ontario Grade 4 Data Management strand: probability can be used to predict likely outcomes, such as predicting that rolling a die is more likely to land on a number 1 through 6 than any other value.',
  [('If a bag has 3 red marbles and 1 blue marble, which colour is more likely to be picked?', ['Blue', 'Red', 'Equally likely', 'Neither can be picked'], 1),
   ('Rolling a standard six-sided die, what is the chance of rolling a 7?', ['Certain', 'Impossible', 'Likely', 'Unlikely but possible'], 1),
   ('Predicting outcomes with probability means ___.', ['Guessing with no reasoning at all', 'Using known information to estimate what is likely to happen', 'Always being 100 percent certain', 'Ignoring the available data'], 1),
   ('If a spinner has 4 equal sections numbered 1 to 4, what is the chance of landing on 2?', ['1 out of 4', '2 out of 4', '4 out of 4', '1 out of 2'], 0),
   ('An outcome that is certain to happen has a probability of ___.', ['0 percent', '50 percent', '100 percent', 'It cannot be determined'], 2)]),
Sc('Recycling and Waste Reduction',
   'Ontario Grade 4 Science Earth and Space Systems strand: recycling and waste reduction help limit the amount of garbage sent to landfills by reusing materials and reducing unnecessary consumption.',
   [('Recycling helps reduce the amount of waste sent to ___.', ['The ocean only', 'Landfills', 'Space', 'Nowhere, recycling has no effect'], 1),
    ('Which is an example of waste reduction?', ['Buying more single-use items', 'Reusing containers instead of throwing them away', 'Throwing away recyclable materials', 'Ignoring how much waste is produced'], 1),
    ('Materials like paper, glass, and some plastics can often be ___.', ['Never reused in any way', 'Recycled into new products', 'Only thrown away', 'Destroyed completely with no benefit'], 1),
    ('Why is reducing waste important for the environment?', ['It helps conserve resources and limit pollution from landfills', 'Waste has no impact on the environment', 'Landfills have unlimited space', 'Reducing waste has no benefits'], 0),
    ('Which of the three Rs comes first in reducing environmental impact: reduce, reuse, or recycle?', ['Recycle', 'Reduce', 'Reuse', 'None of them matter'], 1)]),
SS('Canadian Identity: Symbols and Traditions',
   'Ontario Grade 4 Social Studies Heritage and Identity strand: Canadian identity is expressed through symbols and traditions such as the maple leaf, the national anthem, and celebrations that reflect the country’s diverse heritage.',
   [('Which is a well-known symbol of Canada?', ['The maple leaf', 'The cactus', 'The palm tree', 'The pine cone only'], 0),
    ('National symbols and traditions help express ___.', ['Nothing meaningful about a country', 'A country’s shared identity and values', 'Only one person’s personal opinion', 'A country’s exact population count'], 1),
    ('Canada’s national anthem is an example of a ___.', ['Type of food', 'National tradition and symbol', 'Sports event', 'Type of currency'], 1),
    ('Why does Canada celebrate diverse cultural traditions?', ['Canada is home to people from many different cultural backgrounds', 'Canada has only one culture', 'Cultural diversity has no connection to Canadian identity', 'Celebrations are not part of Canadian identity'], 0),
    ('Learning about Canadian symbols and traditions helps students understand ___.', ['What makes up a shared sense of Canadian identity', 'That Canada has no shared identity', 'That symbols have no meaning', 'That traditions are unimportant to a country'], 0)])]),

day(49, [
L('Grammar: Possessive Nouns and Apostrophes',
  'Ontario Grade 4 Writing strand: possessive nouns show ownership using an apostrophe, such as adding ’s for singular nouns (the dog’s bone) or just an apostrophe for plural nouns ending in s (the dogs’ bones).',
  [('Which shows correct singular possession?', ['The dogs bone', 'The dog’s bone', 'The dogs’s bone', 'The dog bone’s'], 1),
   ('How do you typically form the possessive of a plural noun ending in s?', ['Add ’s', 'Add just an apostrophe after the s', 'Remove the s entirely', 'Add nothing at all'], 1),
   ('Which sentence correctly shows plural possession?', ['The students’ books were on the desk.', 'The students book’s were on the desk.', 'The student’s’ books were on the desk.', 'The students books were on the desk.'], 0),
   ('An apostrophe in a possessive noun shows ___.', ['That a letter has been removed only', 'Ownership or belonging', 'A question is being asked', 'The end of a sentence'], 1),
   ('Which is the correct possessive form for a single cat named Max?', ['Maxs toy', 'Max’s toy', 'Maxes’ toy', 'Max toy’s'], 1)]),
M('Growing and Shrinking Patterns',
  'Ontario Grade 4 Algebra strand: a growing pattern increases by a consistent rule each step, while a shrinking pattern decreases by a consistent rule each step.',
  [('In the pattern 3, 6, 9, 12, what is the next number?', ['13', '14', '15', '16'], 2),
   ('In the pattern 50, 45, 40, 35, what is the next number?', ['25', '30', '32', '38'], 1),
   ('A growing pattern is one where the values ___.', ['Stay exactly the same', 'Increase by a consistent rule', 'Decrease by a consistent rule', 'Change randomly'], 1),
   ('A shrinking pattern is one where the values ___.', ['Increase by a consistent rule', 'Decrease by a consistent rule', 'Stay exactly the same', 'Change randomly with no rule'], 1),
   ('What is the rule for the pattern 2, 4, 8, 16?', ['Add 2 each time', 'Multiply by 2 each time', 'Subtract 2 each time', 'Divide by 2 each time'], 1)]),
Sc('Scientific Inquiry: Designing a Fair Test',
   'Ontario Grade 4 Science Inquiry strand: a fair test changes only one variable at a time while keeping all other conditions the same, so results can be reliably compared and attributed to that one change.',
   [('In a fair test, how many variables should typically be changed at a time?', ['As many as possible', 'Only one', 'None at all', 'It does not matter'], 1),
    ('Why is it important to keep other conditions the same in a fair test?', ['So any difference in results can be attributed to the one variable being tested', 'Keeping conditions the same makes the test less accurate', 'It is not important at all', 'Fair tests do not need consistent conditions'], 0),
    ('If testing how sunlight affects plant growth, what should stay the same between test plants?', ['Nothing needs to stay the same', 'Water, soil, and pot size', 'The amount of sunlight only', 'The plant species should be different each time'], 1),
    ('A variable in an experiment is ___.', ['A factor that can change and affect the results', 'The name of the scientist', 'The title of the experiment', 'Something that never changes'], 0),
    ('Why do scientists rely on fair tests?', ['To draw reliable, accurate conclusions from their results', 'Fair tests make conclusions less reliable', 'Fair testing is unnecessary in science', 'Fair tests are only used outside of science'], 0)]),
SS('Local Government: Municipal Roles',
   'Ontario Grade 4 Social Studies People and Environments strand: municipal (local) governments are responsible for community services such as roads, parks, garbage collection, and local bylaws, led by a mayor and council.',
   [('Which level of government is typically responsible for garbage collection?', ['Federal government', 'Municipal (local) government', 'Only the provincial government', 'No government handles this'], 1),
    ('A municipal government is usually led by a ___.', ['Prime Minister', 'Mayor and council', 'King or Queen', 'Premier only'], 1),
    ('Which is an example of a municipal responsibility?', ['Maintaining local roads and parks', 'Printing national currency', 'Managing the country’s military', 'Setting national trade policy'], 0),
    ('A local bylaw is ___.', ['A national law that applies to every country', 'A rule created by the municipal government for the local community', 'A rule with no legal effect', 'The same as a federal law'], 1),
    ('Why is municipal government important to daily life?', ['It manages many of the services communities rely on every day', 'It has no connection to daily life', 'Municipal government does not exist in Canada', 'It only matters once every four years'], 0)])]),

day(50, [
L('Reading: Reflecting and Responding to Texts',
  'Ontario Grade 4 Reading strand: reflecting on a text means thinking about how it connects to your own experiences, other texts, or the world, and forming a thoughtful personal response.',
  [('Reflecting on a text means ___.', ['Immediately forgetting what you read', 'Thinking about how the text connects to your experiences or the world', 'Only memorizing the text word for word', 'Ignoring your own thoughts about the text'], 1),
   ('A personal response to a text might include ___.', ['Only copying sentences from the text', 'Your own thoughts, feelings, or connections to the text', 'No opinions or thoughts at all', 'A list of unrelated topics'], 1),
   ('Connecting a text to your own experience is an example of a ___ connection.', ['Text-to-self', 'Text-to-nowhere', 'Random', 'Meaningless'], 0),
   ('Why is reflecting on a text a valuable reading habit?', ['It deepens understanding and makes reading more meaningful', 'Reflection has no benefit for readers', 'It replaces the need to read carefully', 'Reflection only applies to non-fiction'], 0),
   ('Which is an example of a text-to-text connection?', ['Comparing a story to another book you have read', 'Comparing a story to a math worksheet only', 'Ignoring all other texts', 'Only focusing on the cover of the book'], 0)]),
M('Budgeting Basics',
  'Ontario Grade 4 Financial Literacy strand: a budget is a plan for how to use money, balancing income (money coming in) with expenses (money going out), and setting aside savings when possible.',
  [('A budget is best described as ___.', ['A plan for how to use money', 'A type of bank account only', 'A list of things you already own', 'A rule that forbids spending money'], 0),
   ('Income refers to ___.', ['Money going out', 'Money coming in', 'Money that has been lost', 'A type of expense'], 1),
   ('An expense refers to ___.', ['Money coming in', 'Money going out for something purchased', 'Money saved only', 'A type of income'], 1),
   ('If Malik earns $20 in allowance and spends $12, how much is left to save?', ['$8', '$12', '$20', '$32'], 0),
   ('Why is it useful to set aside savings in a budget?', ['To have money available for future needs or goals', 'Savings serve no useful purpose', 'A budget should never include savings', 'Saving money is the same as spending it'], 0)]),
Sc('Review: Structures, Forces, and Simple Machines',
   'Ontario Grade 4 Science Structures and Mechanisms strand review: this lesson revisits structures, forces like magnetism and friction, and simple machines like levers, inclined planes, wheels and axles, and screws, from across the year.',
   [('Which is an example of a simple machine studied this year?', ['A lever', 'A cloud', 'A river', 'A mountain'], 0),
    ('A structure’s ability to support weight without collapsing depends on its ___.', ['Colour', 'Design and how it distributes load', 'Smell', 'Price'], 1),
    ('Magnetism is an example of a ___ studied in this unit.', ['Force', 'Type of rock', 'Writing style', 'Historical event'], 0),
    ('Which simple machine converts turning motion into straight-line motion?', ['Wheel and axle', 'Screw', 'Lever', 'Pulley'], 1),
    ('Why is it useful to review structures, forces, and simple machines together?', ['They are closely connected ideas that build a fuller understanding of mechanisms', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be learned in complete isolation'], 0)]),
SS('Culminating Task: Comparing an Early Society to Canada Today',
   'Ontario Grade 4 Social Studies culminating task: students compare daily life, government, and technology in an early society, such as Ancient Egypt or Mesopotamia, with life in Canada today.',
   [('Comparing an early society to Canada today can include looking at ___.', ['Only the weather', 'Daily life, government, and technology', 'Nothing meaningful', 'Only the colour of buildings'], 1),
    ('Which is a valid comparison between Ancient Egypt and Canada today?', ['Both have systems of government, though very different in structure', 'Neither society ever had any form of government', 'Ancient Egypt used smartphones', 'Canada today has pyramids as its main structures'], 0),
    ('Why is comparing past and present societies a valuable learning task?', ['It helps students understand how societies change and what stays similar over time', 'Comparing societies has no educational value', 'Past societies have no connection to life today', 'This kind of comparison is impossible to make'], 0),
    ('A culminating task is typically used to ___.', ['Introduce a brand new unit with no prior learning', 'Bring together and apply learning from throughout a unit or year', 'Replace the need for any learning at all', 'Test only unrelated content'], 1),
    ('Which skill is most useful when completing a comparison task like this?', ['Identifying similarities and differences with supporting evidence', 'Guessing randomly with no evidence', 'Ignoring one of the two things being compared', 'Copying text without analysis'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260712):
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
    _rebalance_answer_positions(g4_41_50)
    append_to(4, g4_41_50)
