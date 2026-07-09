#!/usr/bin/env python3
"""Phase 3: Grade 5, Days 31-40 (first Grade 5 batch, following the same
10-day pattern used for Grade 3 and Grade 4). Topics chosen to avoid any
overlap with the existing Day 1-30 set (see data/grade5.json) and to draw
on Ontario Grade 5 curriculum strands not yet covered: mixed-number
operations, percent and integers, the nervous/circulatory/respiratory
systems, and 19th-century Canadian history (War of 1812, Rebellions of
1837, Loyalists, the CPR) alongside government structure and civics
topics not already covered.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text (gen_curriculum.py's serializer
doesn't escape them); apostrophes use the curly Unicode form (’) so they
never collide with the single-quoted Python string literals used here.
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


g5_31_40 = [
day(31, [
L('Reading: Evaluating Sources for Reliability',
  'Ontario Grade 5 Reading and Media Literacy strands: evaluating a source means checking who wrote it, when it was published, and whether it is supported by evidence, before deciding whether to trust it.',
  [('Which is a key question when evaluating a source’s reliability?', ['What colour is the website?', 'Who wrote it, and are they a credible authority on the topic?', 'How long is the article?', 'Does it have pictures?'], 1),
   ('A reliable source is generally one that ___.', ['Has no author listed at all', 'Is supported by evidence and comes from a credible author or organization', 'Is the first result in any search', 'Contains only opinions with no facts'], 1),
   ('Why should readers check when a source was published?', ['Older information may be outdated on fast-changing topics', 'Publication date never matters', 'Only brand new sources are ever accurate', 'Dates have no connection to reliability'], 0),
   ('Which is a warning sign that a source might be unreliable?', ['It cites specific evidence and data', 'It presents only one extreme opinion with no evidence', 'It lists its author clearly', 'It was reviewed by experts'], 1),
   ('Comparing information across multiple credible sources helps readers ___.', ['Confirm whether the information is accurate and consistent', 'Guarantee that one source must be wrong', 'Avoid learning anything useful', 'Ignore the topic entirely'], 0)]),
M('Adding and Subtracting Mixed Numbers',
  'Ontario Grade 5 Number strand: adding or subtracting mixed numbers involves combining the whole numbers and the fractions separately, and regrouping when a fraction sum is improper.',
  [('What is 2 and 1/4 plus 1 and 2/4?', ['3 and 3/4', '3 and 1/4', '4 and 1/4', '3 and 2/4'], 0),
   ('What is 5 and 3/5 minus 2 and 1/5?', ['3 and 2/5', '3 and 4/5', '7 and 2/5', '2 and 2/5'], 0),
   ('When adding mixed numbers, you should add the ___ separately.', ['Whole numbers and fractions', 'Only the whole numbers', 'Only the fractions', 'Denominators only'], 0),
   ('What is 4 and 3/6 minus 1 and 5/6?', ['2 and 4/6', '3 and 2/6', '2 and 2/6', '3 and 4/6'], 0),
   ('If a fraction sum becomes improper, such as 1 and 5/4, you should ___.', ['Leave it as is', 'Regroup it into 2 and 1/4', 'Ignore the whole number', 'Round down to 1'], 1)]),
Sc('Levers and Mechanical Advantage',
   'Ontario Grade 5 Science Structures and Mechanisms strand: a lever provides mechanical advantage by multiplying the force applied, depending on where the fulcrum is placed relative to the load and effort.',
   [('Mechanical advantage refers to ___.', ['How a machine multiplies the force applied to it', 'The colour of a machine', 'How heavy a machine is', 'How many parts a machine has'], 0),
    ('On a lever, the fixed point it pivots around is called the ___.', ['Load', 'Fulcrum', 'Effort', 'Axle'], 1),
    ('Moving a lever’s fulcrum closer to the load generally ___ the mechanical advantage.', ['Decreases', 'Increases', 'Has no effect on', 'Eliminates'], 1),
    ('Which everyday tool uses lever action to provide mechanical advantage?', ['A pair of scissors', 'A flat table', 'A window pane', 'A brick'], 0),
    ('Why do engineers consider mechanical advantage when designing tools?', ['It helps tools accomplish tasks with less applied effort', 'Mechanical advantage has no practical use', 'It only matters for large machines', 'It always makes tools weaker'], 0)]),
SS('The War of 1812',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: the War of 1812 was fought between the United States and Britain (including its colonies in what is now Canada), with First Nations allies playing a significant role in defending Canadian territory.',
   [('The War of 1812 was fought mainly between which two sides?', ['Canada and France', 'The United States and Britain (including its Canadian colonies)', 'Canada and Britain', 'Spain and Portugal'], 1),
    ('Which group played a significant role in defending Canadian territory during the War of 1812?', ['First Nations allies', 'The Ancient Romans', 'Astronauts', 'No one else was involved'], 0),
    ('The War of 1812 took place mainly in what is now ___.', ['Modern-day Canada and parts of the United States', 'Ancient Egypt', 'South America', 'Australia'], 0),
    ('Why is the War of 1812 significant to Canadian history?', ['It helped shape early Canadian identity and border relations with the United States', 'It has no connection to Canadian history', 'It took place entirely in Europe', 'It occurred in modern times'], 0),
    ('Which historical figure is well known for their role defending Canada during the War of 1812?', ['Laura Secord', 'A modern astronaut', 'A fictional superhero', 'A recent prime minister'], 0)])]),

day(32, [
L('Grammar: Active and Passive Voice',
  'Ontario Grade 5 Writing strand: in active voice, the subject performs the action (the dog chased the ball), while in passive voice, the subject receives the action (the ball was chased by the dog).',
  [('Which sentence is written in active voice?', ['The ball was kicked by Sam.', 'Sam kicked the ball.', 'The ball is being kicked.', 'The ball had been kicked.'], 1),
   ('Which sentence is written in passive voice?', ['The cat chased the mouse.', 'The mouse was chased by the cat.', 'The cat is chasing the mouse.', 'The cat will chase the mouse.'], 1),
   ('In active voice, the subject of the sentence ___.', ['Receives the action', 'Performs the action', 'Is always missing', 'Never appears'], 1),
   ('Why do writers often prefer active voice?', ['It tends to be clearer and more direct', 'Active voice is always grammatically incorrect', 'Passive voice is always required', 'Active voice removes the subject entirely'], 0),
   ('Rewrite in active voice: The letter was written by Maria.', ['Maria wrote the letter.', 'The letter wrote Maria.', 'The letter is written.', 'Written was the letter by Maria.'], 0)]),
M('Dividing Fractions by Whole Numbers',
  'Ontario Grade 5 Number strand: dividing a fraction by a whole number means splitting that fraction into that many equal parts, which can be found by multiplying the denominator by the whole number.',
  [('What is 1/2 divided by 2?', ['1/4', '1/2', '2/2', '1/8'], 0),
   ('What is 3/4 divided by 3?', ['1/4', '3/12', '1/2', '9/4'], 0),
   ('To divide a fraction by a whole number, you can ___.', ['Multiply the numerator by the whole number', 'Multiply the denominator by the whole number', 'Add the whole number to the denominator', 'Subtract the whole number from the numerator'], 1),
   ('What is 2/3 divided by 2?', ['1/3', '4/3', '2/6', '1/6'], 0),
   ('What is 5/6 divided by 5?', ['1/6', '5/30', '1/30', '5/1'], 0)]),
Sc('Density and Buoyancy',
   'Ontario Grade 5 Science Matter and Energy strand: density is how tightly packed an object’s mass is within its volume, and buoyancy is the upward force that determines whether an object floats or sinks in a liquid.',
   [('Density is best described as ___.', ['How much mass is packed into a given volume', 'The colour of an object', 'How heavy an object feels only', 'The temperature of an object'], 0),
    ('An object will generally float in water if its density is ___ than water.', ['Greater', 'Less', 'Exactly equal in every case', 'Density has no effect on floating'], 1),
    ('Buoyancy refers to ___.', ['The force that pulls objects downward only', 'The upward force that can cause an object to float', 'A type of energy source', 'A property of solids only'], 1),
    ('Why does a large steel ship float, even though steel is denser than water?', ['Its overall shape displaces enough water to create sufficient buoyant force', 'Steel always floats regardless of shape', 'Ships are not actually made of steel', 'Buoyancy does not apply to ships'], 0),
    ('Which object would most likely sink in water?', ['A rock', 'A wooden log', 'An inflated balloon', 'A hollow plastic ball'], 0)]),
SS('The Rebellions of 1837',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: the Rebellions of 1837 in Upper and Lower Canada were uprisings by reformers seeking more democratic, accountable government, led in part by figures like William Lyon Mackenzie.',
   [('The Rebellions of 1837 mainly took place in ___.', ['Upper and Lower Canada', 'The United States', 'The Arctic', 'British Columbia'], 0),
    ('Reformers involved in the Rebellions of 1837 were seeking ___.', ['Less democratic government', 'More democratic, accountable government', 'No government at all', 'A return to earlier colonial rule with no changes'], 1),
    ('Which historical figure is associated with the Rebellions of 1837 in Upper Canada?', ['William Lyon Mackenzie', 'A modern politician', 'An ancient Roman leader', 'A fictional character'], 0),
    ('Why are the Rebellions of 1837 considered important to Canadian political history?', ['They contributed to later reforms toward more responsible government', 'They had no lasting effect on Canadian government', 'They led to no political change whatsoever', 'They occurred after Confederation'], 0),
    ('The term responsible government refers to ___.', ['A government accountable to elected representatives of the people', 'A government with no accountability at all', 'A government run entirely by one unelected ruler', 'A government located outside of Canada'], 0)])]),

day(33, [
L('Writing: Argumentative Essays',
  'Ontario Grade 5 Writing strand: an argumentative essay presents a clear position on an issue and supports it with logical reasons and evidence, while also acknowledging other viewpoints.',
  [('An argumentative essay is built around ___.', ['A clear position supported by reasons and evidence', 'A list of unrelated facts', 'Only the writer’s feelings with no support', 'A summary with no opinion'], 0),
   ('Why is it useful for an argumentative essay to acknowledge other viewpoints?', ['It shows the writer has considered the issue thoughtfully and strengthens the argument', 'Other viewpoints should always be ignored', 'Acknowledging other views weakens an essay', 'It replaces the need for evidence'], 0),
   ('Evidence in an argumentative essay might include ___.', ['Facts, statistics, or expert opinions', 'Only the writer’s favourite colour', 'Random unrelated stories', 'Nothing at all'], 0),
   ('A strong argumentative essay typically ends with ___.', ['A conclusion that restates the position and key reasons', 'No conclusion at all', 'A brand new, unrelated topic', 'A list of unrelated questions'], 0),
   ('Which is an example of a clear argumentative position?', ['Schools should have longer recess because it improves focus and health.', 'Recess happens at school.', 'Some schools have recess.', 'Recess can be long or short.'], 0)]),
M('Introducing Percentages',
  'Ontario Grade 5 Number strand: percent means out of 100, and percentages can be converted to and from fractions and decimals, such as 50 percent equalling 1/2 or 0.5.',
  [('What does 25 percent mean?', ['25 out of 100', '25 out of 10', '2.5 out of 100', '25 out of 1000'], 0),
   ('What is 50 percent as a decimal?', ['5.0', '0.5', '0.05', '50.0'], 1),
   ('What is 3/4 written as a percent?', ['34%', '75%', '43%', '25%'], 1),
   ('What is 10 percent of 200?', ['10', '20', '2', '100'], 1),
   ('What is 0.75 written as a percent?', ['0.75%', '7.5%', '75%', '750%'], 2)]),
Sc('The Nervous System',
   'Ontario Grade 5 Science Human Body Systems strand: the nervous system, made up of the brain, spinal cord, and nerves, controls the body by sending and receiving electrical signals throughout the body.',
   [('The nervous system is made up mainly of the ___.', ['Brain, spinal cord, and nerves', 'Heart and blood vessels only', 'Stomach and intestines', 'Lungs and diaphragm'], 0),
    ('The brain is considered the body’s ___.', ['Control centre', 'Digestive organ', 'Filter for blood', 'Storage for food'], 0),
    ('Nerves carry information through the body in the form of ___.', ['Electrical signals', 'Digested food', 'Air only', 'Bone tissue'], 0),
    ('The spinal cord’s main role is to ___.', ['Connect the brain to the rest of the body’s nerves', 'Digest food', 'Pump blood', 'Filter air'], 0),
    ('Why is the nervous system important for reacting quickly, such as pulling your hand away from something hot?', ['It sends rapid signals between the body and brain to trigger a fast response', 'The nervous system has no role in reactions', 'Reactions happen with no signals at all', 'Only the digestive system controls reactions'], 0)]),
SS('United Empire Loyalists and the Founding of Ontario',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: United Empire Loyalists were settlers who remained loyal to Britain during the American Revolution and moved north, playing a key role in founding early Ontario communities.',
   [('United Empire Loyalists were people who ___.', ['Supported the American Revolution', 'Remained loyal to Britain during the American Revolution', 'Had no connection to Britain at all', 'Immigrated from Asia'], 1),
    ('After the American Revolution, many Loyalists moved to ___.', ['What is now Ontario and other parts of British North America', 'South America', 'Europe permanently', 'Nowhere, they all stayed in the same place'], 0),
    ('Loyalist settlement played a key role in ___.', ['Founding many early Ontario communities', 'Preventing any settlement in Ontario', 'Ending all immigration to Canada', 'Founding cities in Europe'], 0),
    ('Why did Loyalists choose to leave the newly independent United States?', ['They wished to remain under British rule rather than join the new republic', 'They had no reason to leave', 'They were forced to leave by the British government', 'They were relocating for warmer weather'], 0),
    ('Studying the Loyalists helps explain ___.', ['Some of the early roots of settlement patterns in what became Ontario', 'Why Ontario has no early history', 'That Ontario was founded in modern times', 'That the American Revolution had no effect on Canada'], 0)])]),

day(34, [
L('Figurative Language: Hyperbole and Onomatopoeia',
  'Ontario Grade 5 Reading strand: hyperbole is an obvious exaggeration used for effect (I have a million things to do), while onomatopoeia is a word that imitates a sound (buzz, crash, sizzle).',
  [('Hyperbole is best described as ___.', ['An obvious exaggeration used for effect', 'A word that imitates a sound', 'A comparison using like or as', 'A rhyming pattern'], 0),
   ('Which sentence contains hyperbole?', ['I have a million things to do today.', 'I have three things to do today.', 'I finished my homework.', 'The sky is blue.'], 0),
   ('Onomatopoeia is best described as ___.', ['A word that imitates the sound it describes', 'An exaggerated statement', 'A comparison between two unlike things', 'A type of punctuation'], 0),
   ('Which word is an example of onomatopoeia?', ['Buzz', 'Happy', 'Quickly', 'Blue'], 0),
   ('Why might an author use hyperbole in writing?', ['To emphasize a feeling or idea in a dramatic, memorable way', 'To state only literal facts', 'To confuse the reader on purpose', 'Hyperbole has no purpose in writing'], 0)]),
M('Introducing Integers',
  'Ontario Grade 5 Number strand: integers include positive numbers, negative numbers, and zero, and are often used to represent values like temperatures below zero or elevations below sea level.',
  [('Which of these is a negative integer?', ['5', '0', '-3', '10'], 2),
   ('A temperature of 5 degrees below zero would be written as ___.', ['5', '-5', '0', '50'], 1),
   ('On a number line, negative integers are located ___.', ['To the right of zero', 'To the left of zero', 'Exactly at zero', 'Above zero only'], 1),
   ('Which integer is greater: -8 or -3?', ['-8', '-3', 'They are equal', 'Cannot be compared'], 1),
   ('An elevation of 50 metres below sea level could be represented as ___.', ['50', '-50', '0', '500'], 1)]),
Sc('The Circulatory and Respiratory Systems',
   'Ontario Grade 5 Science Human Body Systems strand: the circulatory system (heart, blood, and blood vessels) transports oxygen and nutrients through the body, while the respiratory system (lungs and airways) brings oxygen in and removes carbon dioxide.',
   [('The main organ of the circulatory system is the ___.', ['Heart', 'Lungs', 'Stomach', 'Brain'], 0),
    ('The circulatory system’s main job is to ___.', ['Transport oxygen and nutrients throughout the body', 'Digest food', 'Filter air only', 'Control body movement'], 0),
    ('The main organs of the respiratory system are the ___.', ['Lungs and airways', 'Heart and blood vessels', 'Stomach and intestines', 'Brain and spinal cord'], 0),
    ('The respiratory system removes ___ from the body.', ['Oxygen', 'Carbon dioxide', 'Water only', 'Nutrients'], 1),
    ('How do the circulatory and respiratory systems work together?', ['The respiratory system brings in oxygen, which the circulatory system then carries throughout the body', 'They have no connection to each other', 'The circulatory system brings in air directly', 'The respiratory system pumps blood'], 0)]),
SS('Building the Canadian Pacific Railway',
   'Ontario Grade 5 Social Studies People and Environments strand: the Canadian Pacific Railway, completed in 1885, connected Canada from coast to coast, relying heavily on the labour of Chinese immigrant workers who faced dangerous conditions and discrimination.',
   [('The Canadian Pacific Railway connected Canada ___.', ['From coast to coast', 'Only within one city', 'To the United States exclusively', 'Nowhere significant'], 0),
    ('In what decade was the Canadian Pacific Railway completed?', ['1850s', '1880s', '1920s', '1960s'], 1),
    ('Which group of workers played a major role in building the railway, often under dangerous conditions?', ['Chinese immigrant workers', 'No workers were needed', 'Only volunteers with no pay', 'Workers from Australia'], 0),
    ('Why is the completion of the railway considered historically significant for Canada?', ['It helped unite the country economically and geographically', 'It had no effect on Canada as a country', 'It disconnected regions of Canada from each other', 'It was built entirely outside of Canada'], 0),
    ('What is one challenge that Chinese railway workers faced during construction?', ['Dangerous working conditions and discrimination', 'Easy, safe working conditions with full recognition', 'No challenges at all', 'They were paid more than any other workers'], 0)])]),

day(35, [
L('Reading: Identifying Theme',
  'Ontario Grade 5 Reading strand: a theme is the underlying message or lesson of a story, often about life, human nature, or society, which is different from the plot itself.',
  [('A theme is best described as ___.', ['The exact sequence of events in a story', 'The underlying message or lesson of a story', 'The name of the main character', 'The title of the book'], 1),
   ('How is theme different from plot?', ['Plot is what happens; theme is the deeper message behind those events', 'Theme and plot are exactly the same thing', 'Plot is always about lessons; theme is about events', 'Theme only exists in nonfiction'], 0),
   ('Which is an example of a possible theme in a story?', ['Perseverance can help you overcome challenges.', 'The story is 200 pages long.', 'The main character is named Alex.', 'The book was published last year.'], 0),
   ('How can readers identify a story’s theme?', ['By considering what lesson or message the events of the story suggest', 'By counting the number of chapters', 'By ignoring the characters and plot entirely', 'By reading only the title'], 0),
   ('Why is identifying theme a valuable reading skill?', ['It helps readers understand the deeper meaning and purpose behind a story', 'Themes have no real value to readers', 'It replaces the need to understand the plot', 'Only poems have themes'], 0)]),
M('Mean, Median, and Mode',
  'Ontario Grade 5 Data Management strand: the mean is the average of a data set, the median is the middle value when data is ordered, and the mode is the value that appears most often.',
  [('What is the mean of the data set 2, 4, 6?', ['2', '4', '6', '12'], 1),
   ('What is the median of the data set 3, 7, 9?', ['3', '7', '9', '6'], 1),
   ('What is the mode of the data set 2, 2, 5, 7?', ['2', '5', '7', 'There is no mode'], 0),
   ('To find the mean, you ___.', ['Add all the values and divide by how many there are', 'Find the middle value only', 'Find the value that appears most often', 'Multiply all the values together'], 0),
   ('What is the median of the data set 1, 3, 5, 7, 9?', ['3', '5', '7', '9'], 1)]),
Sc('Ecosystems and Biomes of Canada',
   'Ontario Grade 5 Science Life Systems strand: Canada contains diverse biomes, such as boreal forest, tundra, and grassland, each with distinct plant and animal life adapted to that environment’s climate.',
   [('A biome is best described as ___.', ['A large region with a distinct climate and community of plants and animals', 'A single individual animal', 'A type of rock', 'A man-made structure'], 0),
    ('Canada’s boreal forest biome is characterized mainly by ___.', ['Coniferous trees and a cold climate', 'Cactus plants and desert sand', 'Coral reefs', 'Tropical rainforest plants'], 0),
    ('The tundra biome is known for its ___.', ['Warm, tropical climate', 'Cold temperatures and lack of trees', 'Dense rainforest vegetation', 'Coral reef ecosystems'], 1),
    ('Why do different biomes support different plants and animals?', ['Organisms adapt to the specific climate and conditions of their biome', 'All biomes have identical conditions', 'Plants and animals are randomly distributed with no pattern', 'Climate has no effect on which organisms live in an area'], 0),
    ('Grassland biomes in Canada are typically characterized by ___.', ['Open plains with grasses and few trees', 'Dense tropical jungle', 'Permanent ice cover', 'Underwater coral formations'], 0)]),
SS('The Structure of Canadian Courts',
   'Ontario Grade 5 Social Studies People and Environments strand: the Canadian court system includes different levels of courts, from provincial courts to the Supreme Court of Canada, which interpret and apply the law.',
   [('The highest court in Canada is the ___.', ['Supreme Court of Canada', 'Local municipal council', 'Provincial legislature', 'House of Commons'], 0),
    ('The main role of courts in Canada is to ___.', ['Interpret and apply the law', 'Write new laws from scratch', 'Collect taxes', 'Manage municipal garbage collection'], 0),
    ('Canadian courts are generally organized into ___.', ['A single court with no levels', 'Different levels, from provincial courts up to the Supreme Court', 'Courts that only exist in one province', 'No formal structure at all'], 1),
    ('Why is having a structured court system important in Canada?', ['It ensures laws are applied fairly and consistently, with the ability to appeal decisions', 'A structured system serves no real purpose', 'Courts have no role in Canadian government', 'All legal decisions are made by a single person with no appeals'], 0),
    ('A case that is appealed to a higher court is generally being reviewed because ___.', ['Someone believes the original decision should be reconsidered', 'Appeals are never allowed in Canada', 'Higher courts only handle unrelated matters', 'The case has already ended with no further options'], 0)])]),

day(36, [
L('Vocabulary: Root Words and Etymology',
  'Ontario Grade 5 Language strand: many English words share root words that come from Latin or Greek, and knowing these roots, along with a word’s etymology (origin), can help readers determine meaning.',
  [('A root word is ___.', ['A word’s ending sound only', 'The base part of a word that carries its core meaning', 'A punctuation mark', 'Always a whole sentence'], 1),
   ('Etymology refers to the study of ___.', ['A word’s origin and history', 'How to spell a word correctly', 'A word’s pronunciation only', 'Grammar rules for verbs'], 0),
   ('The root word tele- (as in telephone or television) relates to the meaning ___.', ['Small', 'Far or distant', 'Water', 'Fast'], 1),
   ('Knowing common root words can help readers ___.', ['Guess the meaning of unfamiliar words', 'Ignore unfamiliar words completely', 'Avoid reading new material', 'Change a word’s spelling randomly'], 0),
   ('Which word shares a root with biology (meaning study of life)?', ['Biography', 'Geography', 'Astronomy', 'Chronology'], 0)]),
M('Classifying Polyhedra',
  'Ontario Grade 5 Geometry strand: a polyhedron is a 3D shape with flat polygon faces, straight edges, and vertices, such as a cube, pyramid, or prism, classified by the number and shape of their faces.',
  [('A polyhedron is best described as a 3D shape with ___.', ['Only curved surfaces', 'Flat polygon faces, straight edges, and vertices', 'No edges at all', 'Only one face'], 1),
   ('How many faces does a cube have?', ['4', '6', '8', '12'], 1),
   ('A triangular prism has triangular ___ and rectangular side faces.', ['Vertices', 'Bases', 'Edges', 'Angles'], 1),
   ('A sphere is NOT considered a polyhedron because ___.', ['It has flat faces', 'It has curved surfaces, not flat polygon faces', 'It has no volume', 'It is too small'], 1),
   ('A square pyramid has how many faces in total, including its base?', ['4', '5', '6', '8'], 1)]),
Sc('Renewable Energy Technologies',
   'Ontario Grade 5 Science Matter and Energy strand: technologies such as solar panels, wind turbines, and hydroelectric dams convert renewable natural energy sources into usable electricity.',
   [('Solar panels convert ___ into usable electricity.', ['Wind energy', 'Sunlight', 'Coal', 'Ocean waves only'], 1),
    ('Wind turbines convert ___ into usable electricity.', ['Sunlight', 'The motion of wind', 'Coal', 'Underground heat only'], 1),
    ('Hydroelectric dams generate electricity using the movement of ___.', ['Water', 'Wind', 'Sunlight', 'Coal'], 0),
    ('Why are renewable energy technologies an important area of research?', ['They can generate electricity while reducing reliance on non-renewable resources', 'They have no benefits at all', 'Renewable technologies cannot generate any electricity', 'They increase pollution significantly'], 0),
    ('Which of these best fits the category of renewable energy technology?', ['A coal power plant', 'A wind turbine', 'An oil refinery', 'A natural gas furnace'], 1)]),
SS('Indigenous Self-Government and Modern Treaties',
   'Ontario Grade 5 Social Studies People and Environments strand: many Indigenous communities in Canada today exercise self-government through modern treaties and agreements that recognize their right to govern their own affairs.',
   [('Self-government for Indigenous communities generally means ___.', ['Having no say in their own affairs', 'Having the authority to govern their own community affairs', 'Being governed entirely by another country', 'Having no recognized rights at all'], 1),
    ('A modern treaty between a government and an Indigenous community typically addresses ___.', ['Nothing of importance', 'Rights, land, and governance arrangements', 'Only sports agreements', 'Only trade with other countries'], 1),
    ('Why is self-government important to many Indigenous communities?', ['It allows communities to make decisions that reflect their own needs, values, and traditions', 'Self-government has no real impact on communities', 'It removes all rights from Indigenous peoples', 'It has no connection to community wellbeing'], 0),
    ('Modern treaties differ from historical treaties in that they often ___.', ['Are negotiated to address more contemporary rights and governance issues', 'Have no legal significance at all', 'Cannot involve Indigenous communities in negotiations', 'Are identical to treaties signed centuries ago'], 0),
    ('Learning about Indigenous self-government helps students understand ___.', ['How Indigenous nations exercise rights and responsibilities today', 'That Indigenous governance ended in the past', 'That Indigenous communities have no role in modern Canada', 'That treaties are no longer relevant'], 0)])]),

day(37, [
L('Writing: Research Report Writing',
  'Ontario Grade 5 Writing strand: a research report organizes information gathered from multiple credible sources into a clear structure, typically with an introduction, body paragraphs by subtopic, and a conclusion.',
  [('A research report typically begins with ___.', ['A random unrelated fact', 'An introduction that presents the topic', 'Only a list of sources', 'The conclusion'], 1),
   ('Body paragraphs in a research report are usually organized by ___.', ['Random order with no structure', 'Subtopic', 'Alphabetical order of unrelated words', 'The length of each sentence'], 1),
   ('Why is it important to use multiple credible sources in a research report?', ['To gather accurate, well-supported information on the topic', 'Multiple sources are never necessary', 'Using more than one source always causes confusion', 'Credibility of sources does not matter'], 0),
   ('A research report’s conclusion should ___.', ['Introduce a completely new topic', 'Summarize the key findings from the report', 'Contain no information at all', 'Repeat the introduction word for word'], 1),
   ('Why should a research report cite its sources?', ['To give credit and allow readers to verify the information', 'Citing sources is unnecessary', 'It makes the report less trustworthy', 'Sources should always be hidden from the reader'], 0)]),
M('Solving Simple Equations',
  'Ontario Grade 5 Algebra strand: a simple equation with a missing value can be solved by using the inverse (opposite) operation to isolate the unknown, such as solving x + 5 = 12 by subtracting 5 from both sides.',
  [('Solve for x: x + 5 = 12.', ['x = 5', 'x = 7', 'x = 17', 'x = 12'], 1),
   ('Solve for y: y minus 4 = 10.', ['y = 6', 'y = 14', 'y = 10', 'y = 4'], 1),
   ('To solve x + 5 = 12, which operation should you use to isolate x?', ['Add 5 to both sides', 'Subtract 5 from both sides', 'Multiply both sides by 5', 'Divide both sides by 5'], 1),
   ('Solve for n: 3 times n = 21.', ['n = 3', 'n = 7', 'n = 18', 'n = 24'], 1),
   ('Solve for m: m divided by 4 = 6.', ['m = 1.5', 'm = 10', 'm = 24', 'm = 2'], 2)]),
Sc('Space: The Solar System and Beyond',
   'Ontario Grade 5 Science Earth and Space Systems strand: the solar system consists of the Sun and everything that orbits it, including eight planets, moons, and other bodies like asteroids and comets, within the much larger Milky Way galaxy.',
   [('The Sun is best described as a ___.', ['Planet', 'Star', 'Moon', 'Comet'], 1),
    ('How many planets are in our solar system?', ['Seven', 'Eight', 'Nine', 'Ten'], 1),
    ('Our solar system is located within the ___ galaxy.', ['Andromeda', 'Milky Way', 'Triangulum', 'Whirlpool'], 1),
    ('Which of these is a small icy body that orbits the Sun and can develop a visible tail?', ['A comet', 'A moon', 'A star', 'A planet'], 0),
    ('Why is the Sun considered the centre of our solar system?', ['Its gravity holds the planets and other bodies in orbit around it', 'The Sun has no connection to the other planets', 'The Sun orbits around Earth', 'The Sun is the smallest object in the solar system'], 0)]),
SS('Canada’s Role in the World Wars',
   'Ontario Grade 5 Social Studies Heritage and Identity strand: Canada played a significant role in both World War I and World War II, with Canadian soldiers contributing to major battles and the country’s involvement shaping its national identity.',
   [('Canada was involved in which two major global conflicts of the 20th century?', ['World War I and World War II', 'Only local skirmishes with no global conflicts', 'The War of 1812 twice', 'Conflicts that never happened'], 0),
    ('Canadian soldiers are remembered for their contributions to major battles during ___.', ['The World Wars', 'Ancient Roman times', 'The dinosaur era', 'A period with no recorded history'], 0),
    ('Canada’s involvement in the World Wars is often seen as having helped ___.', ['Shape a stronger sense of national identity', 'Erase Canada’s identity completely', 'Have no impact on Canada at all', 'Prevent Canada from ever having an army'], 0),
    ('Why do Canadians observe Remembrance Day?', ['To honour those who served and sacrificed during wartime', 'It has no connection to Canadian history', 'To celebrate a modern holiday unrelated to history', 'To mark the founding of a new country'], 0),
    ('Learning about Canada’s role in the World Wars helps students understand ___.', ['How historical events shaped Canada’s development and identity', 'That these wars had no effect on Canada', 'That Canada was not involved in any global conflicts', 'That history has no connection to identity'], 0)])]),

day(38, [
L('Media Literacy: Analyzing Advertisements',
   'Ontario Grade 5 Media Literacy strand: analyzing advertisements involves identifying the intended audience, the persuasive techniques used, and the underlying message the advertiser wants viewers to believe.',
   [('When analyzing an advertisement, it is useful to consider ___.', ['Only the colours used', 'The intended audience and persuasive techniques used', 'Nothing beyond the product name', 'The length of the advertisement only'], 1),
    ('The intended audience of an advertisement refers to ___.', ['The group of people the ad is designed to appeal to', 'The advertiser’s competitors', 'Random unrelated viewers only', 'People who dislike the product'], 0),
    ('Which is a common persuasive technique used in advertisements?', ['Presenting only balanced, neutral information', 'Using emotional appeals or catchy slogans', 'Avoiding any attempt to persuade the viewer', 'Refusing to mention the product at all'], 1),
    ('Why is it useful for viewers to analyze advertisements critically?', ['To understand how they are being persuaded and make informed choices', 'Critical analysis of ads serves no purpose', 'All advertisements present entirely objective information', 'Analyzing ads is only useful for advertisers'], 0),
    ('An advertisement’s underlying message is ___.', ['What the advertiser ultimately wants the viewer to believe or do', 'Always stated directly in plain text', 'Irrelevant to understanding the ad', 'The same in every advertisement'], 0)]),
M('Converting Units of Measurement',
  'Ontario Grade 5 Measurement strand: converting between metric units, such as centimetres to metres or grams to kilograms, involves multiplying or dividing by powers of ten based on the relationship between the units.',
  [('How many centimetres are in 1 metre?', ['10', '100', '1,000', '1'], 1),
   ('How many grams are in 1 kilogram?', ['10', '100', '1,000', '10,000'], 2),
   ('Convert 250 centimetres to metres.', ['2.5 m', '25 m', '0.25 m', '250 m'], 0),
   ('Convert 3 kilograms to grams.', ['30 g', '300 g', '3,000 g', '30,000 g'], 2),
   ('To convert a smaller unit to a larger unit, you typically ___.', ['Multiply', 'Divide', 'Always add 10', 'Always subtract 10'], 1)]),
Sc('Mixtures and Solutions',
   'Ontario Grade 5 Science Matter and Energy strand: a mixture combines two or more substances that keep their own properties, while a solution is a special type of mixture where one substance dissolves evenly into another.',
   [('A mixture is formed when ___.', ['Two or more substances combine but keep their own properties', 'A single substance changes into a different element', 'Nothing is combined at all', 'A substance disappears completely'], 0),
    ('A solution is a type of mixture where ___.', ['One substance dissolves evenly into another', 'Substances never combine', 'All substances turn into gas', 'The mixture always separates immediately'], 0),
    ('Which is an example of a solution?', ['Salt dissolved in water', 'Sand mixed with water', 'Oil floating on water', 'Rocks mixed with soil'], 0),
    ('Which is an example of a mixture that is NOT a solution?', ['Sugar dissolved in tea', 'Salt dissolved in water', 'Sand and gravel mixed together', 'Food colouring mixed into water'], 2),
    ('Why might a solution be described as evenly distributed?', ['The dissolved substance spreads uniformly throughout the other substance', 'Solutions always separate into visible layers', 'Solutions contain only one substance', 'Solutions cannot be mixed evenly'], 0)]),
SS('Economic Systems: Needs, Wants, and Resources',
   'Ontario Grade 5 Social Studies People and Environments strand: economic systems involve decisions about how to use limited resources to meet unlimited needs and wants, balancing production, distribution, and consumption of goods and services.',
   [('A need is best described as ___.', ['Something essential for survival, like food or shelter', 'Something entirely optional', 'The same thing as a want', 'Something with no importance'], 0),
    ('A want is best described as ___.', ['Something essential for survival', 'Something desired but not essential for survival', 'The exact same as a need', 'Something that never affects decisions'], 1),
    ('Economic systems must make decisions about resources because resources are generally ___.', ['Unlimited', 'Limited', 'Irrelevant to decision-making', 'Always identical everywhere'], 1),
    ('Which is an example of a resource used in producing goods?', ['Raw materials, like wood or metal', 'Nothing is needed to produce goods', 'Only imagination, with no physical resources', 'Only money, with no other resources'], 0),
    ('Why must societies make choices about how to use limited resources?', ['Because needs and wants can exceed what resources are available', 'Resources are always unlimited everywhere', 'Choices about resources are never necessary', 'Every society has identical, unlimited resources'], 0)])]),

day(39, [
L('Grammar: Complex and Compound Sentences',
  'Ontario Grade 5 Writing strand: a compound sentence joins two independent clauses with a conjunction (I like reading, and I like writing), while a complex sentence joins an independent clause with a dependent clause (Although it was raining, we went outside).',
  [('A compound sentence joins two ___ with a conjunction.', ['Dependent clauses', 'Independent clauses', 'Single words', 'Punctuation marks'], 1),
   ('A complex sentence joins an independent clause with a ___ clause.', ['Dependent', 'Second independent', 'Meaningless', 'Punctuation-only'], 0),
   ('Which sentence is a compound sentence?', ['I like reading, and I like writing.', 'Although it was raining, we went outside.', 'I like reading.', 'Reading is fun because it is relaxing.'], 0),
   ('Which sentence is a complex sentence?', ['I like reading, and I like writing.', 'Although it was raining, we went outside.', 'I read books.', 'The dog barked.'], 1),
   ('A dependent clause is a clause that ___.', ['Can stand alone as a complete sentence', 'Cannot stand alone as a complete sentence', 'Never appears in complex sentences', 'Is always the entire sentence'], 1)]),
M('Multi-Step Word Problems with Percent and Fractions',
  'Ontario Grade 5 Number strand: solving multi-step word problems involving percent and fractions requires identifying each step needed, such as first finding a percentage of a number, then adding or subtracting the result.',
  [('A $40 shirt is 25 percent off. What is the discount amount?', ['$4', '$10', '$25', '$15'], 1),
   ('A $40 shirt is 25 percent off. What is the final sale price?', ['$10', '$25', '$30', '$35'], 2),
   ('Maria read 1/4 of a 200-page book on Monday, then 1/2 of the remaining pages on Tuesday. How many pages did she read on Tuesday?', ['50', '75', '100', '150'], 1),
   ('Solving a multi-step problem with percent and fractions requires you to ___.', ['Complete each necessary step in order to reach the final answer', 'Skip steps to save time', 'Use only one operation regardless of the problem', 'Ignore the given information'], 0),
   ('A class of 30 students has 60 percent who prefer math. How many students prefer math?', ['12', '18', '20', '24'], 1)]),
Sc('Erosion, Weathering, and Landform Formation',
   'Ontario Grade 5 Science Earth and Space Systems strand: weathering breaks rock down into smaller pieces, while erosion moves those pieces elsewhere via wind, water, or ice, together gradually shaping landforms over time.',
   [('Weathering is the process of ___.', ['Breaking rock down into smaller pieces', 'Moving broken rock pieces to a new location', 'Creating brand new mountains instantly', 'Freezing water into ice permanently'], 0),
    ('Erosion is the process of ___.', ['Breaking rock into pieces only', 'Moving broken-down material to a new location', 'Only affecting rocks underground', 'Preventing any landform changes'], 1),
    ('Which of these can cause both weathering and erosion?', ['Wind, water, and ice', 'Only complete stillness', 'Only artificial materials', 'Nothing natural causes these processes'], 0),
    ('Over long periods of time, weathering and erosion together can ___.', ['Gradually shape landforms like valleys and canyons', 'Have no effect on the land', 'Instantly create new landforms in seconds', 'Only occur underwater'], 0),
    ('Why might a canyon take thousands of years to form?', ['Weathering and erosion typically occur gradually rather than instantly', 'Canyons are always formed in a single day', 'These processes have no connection to landform formation', 'Canyons cannot form through natural processes'], 0)]),
SS('Political Parties and How Laws Are Made',
   'Ontario Grade 5 Social Studies People and Environments strand: political parties represent different ideas about how the country should be run, and elected representatives from these parties debate and vote to turn proposed bills into laws.',
   [('A political party is best described as a group that ___.', ['Shares similar ideas about how the country should be governed', 'Has no political views at all', 'Only exists at the municipal level', 'Never participates in elections'], 0),
    ('A proposed law before it is passed is called a ___.', ['Bylaw', 'Bill', 'Treaty', 'Amendment only'], 1),
    ('For a bill to become law in Canada, it generally must be ___.', ['Ignored completely by all representatives', 'Debated and voted on by elected representatives', 'Written by a single citizen with no review', 'Approved without any discussion'], 1),
    ('Why do different political parties often have different positions on issues?', ['They represent different values, priorities, and approaches to governing', 'All political parties always agree on everything', 'Political parties have no real differences', 'Parties are randomly assigned positions with no reasoning'], 0),
    ('Why is it useful for citizens to understand how laws are made?', ['It helps them understand and participate in the democratic process', 'This knowledge has no value to citizens', 'Laws are made with no citizen relevance', 'Only elected officials need to understand this process'], 0)])]),

day(40, [
L('Reading: Analyzing Character Development',
  'Ontario Grade 5 Reading strand: character development is how a character changes or grows over the course of a story, often shown through their actions, decisions, and relationships with others.',
  [('Character development refers to ___.', ['How a character changes or grows over a story', 'The exact number of characters in a book', 'The book’s cover illustration', 'The font used to print the book'], 0),
   ('Which is a way authors often reveal character development?', ['Through a character’s actions and decisions over time', 'Only through the table of contents', 'Through the price listed on the book', 'Through the page numbers'], 0),
   ('A character who learns an important lesson by the end of a story shows an example of ___.', ['No development at all', 'Character development', 'A change in the book’s title', 'A change in the setting only'], 1),
   ('Why do readers pay attention to character development?', ['It deepens understanding of the story’s meaning and the character’s journey', 'Character development has no connection to a story’s meaning', 'It is not something authors intentionally include', 'Only the plot matters, never the characters'], 0),
   ('Which detail would best show a character’s growth in courage?', ['The character finally standing up for a friend despite feeling afraid', 'A description of the character’s house', 'The character’s favourite food', 'The time of day the story takes place'], 0)]),
M('Simple Interest and Saving',
  'Ontario Grade 5 Financial Literacy strand: simple interest is money earned or paid based on a percentage of an original amount saved or borrowed, calculated using the interest rate and the amount of time involved.',
  [('If you save $100 at a 5 percent simple interest rate for one year, how much interest do you earn?', ['$5', '$50', '$105', '$500'], 0),
   ('Simple interest is generally calculated based on ___.', ['The colour of the bank card used', 'A percentage of the original amount saved or borrowed', 'Nothing related to the amount saved', 'A fixed dollar amount unrelated to percentage'], 1),
   ('Why might someone choose to save money in an account that earns interest?', ['Their savings can grow over time through earned interest', 'Interest never adds any value to savings', 'Savings accounts always lose money', 'Interest is only relevant to borrowing, never saving'], 0),
   ('If you save $200 at a 10 percent simple interest rate for one year, what is your total after one year?', ['$200', '$210', '$220', '$180'], 2),
   ('Interest paid on borrowed money is generally an amount ___.', ['Owed in addition to the original amount borrowed', 'Subtracted from the amount borrowed', 'Unrelated to the amount borrowed', 'Always equal to zero'], 0)]),
Sc('Scientific Method and Experimental Design',
   'Ontario Grade 5 Science Inquiry strand: the scientific method involves asking a question, forming a hypothesis, testing it through a fair experiment, and analyzing results to draw a conclusion.',
   [('The scientific method typically begins with ___.', ['Drawing a final conclusion', 'Asking a question', 'Publishing results', 'Building a finished product'], 1),
    ('A hypothesis is best described as ___.', ['A proven fact that cannot be tested', 'A testable prediction about what might happen', 'The final step of an experiment', 'A random guess with no reasoning at all'], 1),
    ('Why do scientists analyze their results after an experiment?', ['To determine whether the results support or refute the hypothesis', 'Analysis of results is unnecessary', 'Results are always ignored in science', 'Only the experiment’s setup matters, not the results'], 0),
    ('A conclusion in the scientific method should be based on ___.', ['The evidence gathered during the experiment', 'Personal opinion with no evidence', 'What the scientist wished would happen', 'Random chance only'], 0),
    ('Why is the scientific method useful across many areas of science?', ['It provides a structured, reliable way to investigate questions and test ideas', 'It has no practical use in science', 'It only applies to one specific science topic', 'It replaces the need for any evidence'], 0)]),
SS('Canada’s National Parks and Protected Areas',
   'Ontario Grade 5 Social Studies People and Environments strand: Canada’s national parks and protected areas conserve important natural environments and wildlife habitats, balancing conservation with public access and recreation.',
   [('The main purpose of a national park is to ___.', ['Conserve natural environments and wildlife habitats', 'Build as many buildings as possible', 'Remove all wildlife from the area', 'Prevent any public access forever'], 0),
    ('Which organization manages many of Canada’s national parks?', ['Parks Canada', 'A private international company', 'A foreign government', 'No organization manages them'], 0),
    ('Protected areas help ___.', ['Preserve biodiversity and natural habitats', 'Eliminate biodiversity entirely', 'Increase pollution in natural areas', 'Encourage unlimited resource extraction'], 0),
    ('Why might a national park allow limited public access, like hiking trails?', ['To let people appreciate and connect with nature while minimizing environmental impact', 'Public access always destroys protected areas completely', 'National parks never allow any visitors', 'Public access has no connection to conservation goals'], 0),
    ('Why are national parks and protected areas important to Canada?', ['They help conserve natural heritage for future generations', 'They serve no meaningful purpose', 'They have no connection to environmental conservation', 'They exist only to generate profit with no other purpose'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260713):
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
    _rebalance_answer_positions(g5_31_40)
    append_to(5, g5_31_40)
