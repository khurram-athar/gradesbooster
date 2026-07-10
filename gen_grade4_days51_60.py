#!/usr/bin/env python3
"""Phase 3 extension: Grade 4, Days 51-60 (first batch past the Day 50
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-50 set (see
data/grade4.json): reading connections, subject-verb agreement,
prime/composite numbers, angle measurement, rock classification,
balanced forces, and comparing government systems.

Subject keys for Grade 4 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 4 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


g4_51_60 = [
day(51, [
L('Reading: Making Connections (Text-to-Self, Text-to-Text, Text-to-World)',
  'Grade 4 Language strand: strong readers make connections between a text and their own life, other texts they have read, and events happening in the wider world.',
  [('A text-to-self connection is when a reader links a text to ___.', ['Their own life and experiences', 'A completely different book only', 'A concept unrelated to reading', 'The number of chapters in the book'], 0),
   ('A text-to-text connection compares a story to ___.', ['Another text the reader has read before', 'Nothing at all, since texts cannot be compared', 'A concept unrelated to reading comprehension', 'Only the cover illustration of the book'], 0),
   ('A text-to-world connection links a story to ___.', ['Events or issues happening in the wider world', 'A detail unrelated to the story itself', 'Only the page count of the text', 'Nothing, since stories have no connection to the world'], 0),
   ('Why do readers make connections while reading?', ['It helps deepen understanding and makes the text more meaningful', 'Making connections never helps a reader understand a text', 'This strategy has no connection to reading comprehension', 'Connections only distract readers from the story'], 0),
   ('If a story about moving to a new school reminds you of your own first day at school, what kind of connection is this?', ['A text-to-self connection', 'A text-to-text connection', 'A concept unrelated to connections', 'A text-to-world connection'], 0)]),
M('Multiplying Fractions by Whole Numbers',
  'Grade 4 Math strand: multiplying a fraction by a whole number means adding that fraction the given number of times, such as 3 times 1/4 equalling 3/4.',
  [('Multiplying a fraction by a whole number is the same as ___.', ['Adding that fraction the given number of times', 'Dividing the fraction into smaller unrelated parts', 'A concept unrelated to fractions', 'Subtracting the whole number from the fraction'], 0),
   ('What is 3 × 1/4?', ['3/4', '1/12', 'A value unrelated to the multiplication', '4/3'], 0),
   ('What is 2 × 2/5?', ['4/5', '2/10', 'A value unrelated to the multiplication', '5/2'], 0),
   ('When multiplying a fraction by a whole number, which part of the fraction changes?', ['The numerator, while the denominator stays the same', 'The denominator, while the numerator stays the same', 'A part unrelated to fractions', 'Neither part changes at all'], 0),
   ('What is 4 × 1/3?', ['4/3', '1/12', 'A value unrelated to the multiplication', '3/4'], 0)]),
Sc('Ecosystems: Interdependence of Living Things',
   'Grade 4 Science strand: living things in an ecosystem depend on each other and their environment in a web of interdependent relationships.',
   [('Interdependence in an ecosystem means living things ___.', ['Rely on each other and their environment to survive', 'Never interact with each other in any way', 'A concept unrelated to ecosystems', 'Live completely apart from their environment'], 0),
    ('Which is an example of interdependence in an ecosystem?', ['Bees pollinating flowers while flowers provide bees with nectar', 'A rock resting on the ground with no living connections', 'A concept unrelated to living things', 'Two organisms that never interact in any way'], 0),
    ('What might happen if one species disappeared from an ecosystem?', ['Other species that depended on it could also be affected', 'Nothing in the ecosystem would ever change', 'A concept unrelated to ecosystems', 'Every other species would automatically disappear too'], 0),
    ('Why do scientists study interdependence in ecosystems?', ['It helps them understand how changes affect the whole community of living things', 'Studying interdependence provides no useful scientific information', 'This concept has no connection to science', 'Ecosystems have no relationships worth studying'], 0),
    ('Which best describes a healthy, balanced ecosystem?', ['One where living things and their environment support each other', 'One where no living things ever interact', 'A concept unrelated to ecosystems', 'One where every species lives in complete isolation'], 0)]),
SS('Mapping Skills: Latitude and Longitude',
   'Grade 4 Social Studies strand: latitude and longitude are imaginary lines that form a grid on maps and globes, helping people locate exact places on Earth.',
   [('Latitude and longitude lines help people ___.', ['Locate exact places on Earth', 'Measure the temperature of a location', 'A concept unrelated to maps', 'Determine the population of a city'], 0),
    ('Lines of latitude run ___.', ['East to west, parallel to the equator', 'North to south, connecting the poles', 'A direction unrelated to mapping', 'Diagonally across every map'], 0),
    ('Lines of longitude run ___.', ['North to south, connecting the poles', 'East to west, parallel to the equator', 'A direction unrelated to mapping', 'Diagonally across every map'], 0),
    ('Why is a grid of latitude and longitude lines useful on maps?', ['It allows any location on Earth to be described with precise coordinates', 'It has no practical use for finding locations', 'A concept unrelated to geography', 'It only shows the colours of different countries'], 0),
    ('The equator is a line of ___.', ['Latitude', 'Longitude', 'A term unrelated to mapping', 'Elevation'], 0)])]),
day(52, [
L('Grammar: Subject-Verb Agreement',
  'Grade 4 Language strand: subject-verb agreement means matching a singular subject with a singular verb and a plural subject with a plural verb.',
  [('Subject-verb agreement means the subject and verb must ___.', ['Match in number (singular or plural)', 'Always be written in past tense', 'A concept unrelated to grammar', 'Be separated by a comma at all times'], 0),
   ('Which sentence shows correct subject-verb agreement?', ['The dog runs in the park.', 'The dog run in the park.', 'A sentence unrelated to subject-verb agreement', 'The dogs runs in the park.'], 0),
   ('Which sentence shows correct subject-verb agreement?', ['The children play outside.', 'The children plays outside.', 'A sentence unrelated to subject-verb agreement', 'The child play outside.'], 0),
   ('A singular subject like “she” should be paired with a verb like ___.', ['Walks', 'Walk', 'A verb form unrelated to agreement', 'Walking, with no other words needed'], 0),
   ('Why is subject-verb agreement important in writing?', ['It makes sentences grammatically correct and easier to understand', 'It has no effect on how a sentence reads', 'A concept unrelated to clear writing', 'It only matters in spoken language, never in writing'], 0)]),
M('Introduction to Prime and Composite Numbers',
  'Grade 4 Math strand: a prime number has exactly two factors (1 and itself), while a composite number has more than two factors.',
  [('A prime number has exactly ___ factors.', ['Two (1 and itself)', 'Zero factors', 'A number of factors unrelated to primes', 'Ten factors'], 0),
   ('Which of these is a prime number?', ['7', '8', 'A number unrelated to primes', '9'], 0),
   ('Which of these is a composite number?', ['12', '13', 'A number unrelated to composites', '17'], 0),
   ('Why is the number 1 neither prime nor composite?', ['It has only one factor, itself, not two or more', 'It has an unlimited number of factors', 'A reason unrelated to factors', '1 is always considered a prime number'], 0),
   ('Which of these numbers is prime?', ['11', '10', 'A number unrelated to primes', '15'], 0)]),
Sc('Rock and Mineral Classification: Igneous, Sedimentary, Metamorphic',
   'Grade 4 Science strand: rocks are classified into three types based on how they form -- igneous (from cooled magma), sedimentary (from compressed layers), and metamorphic (changed by heat and pressure).',
   [('Igneous rock forms when ___.', ['Melted magma cools and hardens', 'Layers of sediment are compressed over time', 'A process unrelated to rock formation', 'Existing rock is changed by heat and pressure'], 0),
    ('Sedimentary rock forms when ___.', ['Layers of sediment are compressed over time', 'Melted magma cools and hardens', 'A process unrelated to rock formation', 'Existing rock is changed by heat and pressure'], 0),
    ('Metamorphic rock forms when ___.', ['Existing rock is changed by heat and pressure', 'Melted magma cools and hardens', 'A process unrelated to rock formation', 'Layers of sediment are compressed over time'], 0),
    ('Which is an example of a way scientists classify rocks?', ['By how the rock was formed', 'By the colour of the rock alone, with no other criteria', 'A method unrelated to rock classification', 'By where the rock is displayed in a museum'], 0),
    ('Why do geologists classify rocks into these three types?', ['It helps them understand how each rock formed and what it can reveal about Earth’s history', 'Classifying rocks provides no useful scientific information', 'A reason unrelated to geology', 'Rocks are never classified into different types'], 0)]),
SS('Comparing Government Systems: Federal, Provincial, and Municipal',
   'Grade 4 Social Studies strand: Canada has three levels of government -- federal, provincial, and municipal -- each responsible for different services and decisions.',
   [('The federal government is responsible for issues that affect ___.', ['The whole country', 'Only a single city', 'A concept unrelated to government', 'Only a single street'], 0),
    ('The provincial government is responsible for issues such as ___.', ['Education and healthcare within the province', 'International trade agreements only', 'A concept unrelated to government', 'Decisions made only by other countries'], 0),
    ('The municipal government is responsible for issues such as ___.', ['Local roads, garbage collection, and community parks', 'National defence and foreign policy', 'A concept unrelated to government', 'International trade agreements'], 0),
    ('Why does Canada have three levels of government?', ['Different levels can focus on issues at the national, provincial, and local scale', 'Having multiple levels of government serves no useful purpose', 'A reason unrelated to government structure', 'Only one level of government is actually needed'], 0),
    ('Which level of government would most likely decide on a new local playground?', ['Municipal', 'Federal', 'A level unrelated to local decisions', 'Provincial'], 0)])]),
day(53, [
L('Vocabulary: Root Words',
  'Grade 4 Language strand: a root word is the base part of a word that carries its core meaning, and many other words can be built from it by adding prefixes or suffixes.',
  [('A root word is ___.', ['The base part of a word that carries its core meaning', 'A word with no meaning at all', 'A concept unrelated to vocabulary', 'Always the longest word in a sentence'], 0),
   ('What is the root word in “unhappiness”?', ['Happy', 'Un', 'A word unrelated to the root', 'Ness'], 0),
   ('What is the root word in “replayed”?', ['Play', 'Re', 'A word unrelated to the root', 'Ed'], 0),
   ('Knowing a root word can help a reader ___.', ['Figure out the meaning of related, unfamiliar words', 'Never understand the meaning of any word', 'A concept unrelated to vocabulary', 'Only memorize spelling patterns'], 0),
   ('What is the root word in “disagreement”?', ['Agree', 'Dis', 'A word unrelated to the root', 'Ment'], 0)]),
M('Measuring and Classifying Angles with a Protractor',
  'Grade 4 Math strand: a protractor is a tool used to measure the size of an angle in degrees, and angles can be classified as acute, right, obtuse, or straight.',
  [('A protractor is used to ___.', ['Measure the size of an angle in degrees', 'Measure the length of a line', 'A tool unrelated to angles', 'Measure the weight of an object'], 0),
   ('An angle less than 90 degrees is called ___.', ['Acute', 'Obtuse', 'A term unrelated to angles', 'Straight'], 0),
   ('An angle greater than 90 degrees but less than 180 degrees is called ___.', ['Obtuse', 'Acute', 'A term unrelated to angles', 'Right'], 0),
   ('An angle that measures exactly 90 degrees is called ___.', ['A right angle', 'An obtuse angle', 'A term unrelated to angles', 'A straight angle'], 0),
   ('An angle that measures exactly 180 degrees is called ___.', ['A straight angle', 'A right angle', 'A term unrelated to angles', 'An acute angle'], 0)]),
Sc('Waves and Vibrations: How Sound is Produced',
   'Grade 4 Science strand: sound is produced when an object vibrates, creating waves of energy that travel through air or another medium to our ears.',
   [('Sound is produced when an object ___.', ['Vibrates', 'Stays perfectly still', 'A process unrelated to sound', 'Changes colour'], 0),
    ('Sound waves travel through ___.', ['Air and other materials, such as water', 'A vacuum with no matter at all', 'A concept unrelated to sound', 'Only through solid metal'], 0),
    ('What happens to the vibration of a guitar string when it is plucked?', ['It vibrates back and forth, producing sound waves', 'It stops moving completely', 'A result unrelated to sound production', 'It changes into a different material'], 0),
    ('Why can we not hear sound in outer space?', ['There is no air or matter for sound waves to travel through', 'Sound only exists on Earth for no scientific reason', 'A reason unrelated to how sound travels', 'Sound waves travel faster in space, making them silent'], 0),
    ('Which best describes a sound wave?', ['A form of energy that travels through vibrations', 'A form of light that has no connection to vibration', 'A concept unrelated to sound', 'A solid object that can be touched'], 0)]),
SS('Canada’s Industries and Economic Regions',
   'Grade 4 Social Studies strand: different regions of Canada rely on different industries, such as fishing on the coasts, farming on the Prairies, and manufacturing in central Canada.',
   [('An industry is ___.', ['A type of economic activity that produces goods or services', 'A concept unrelated to the economy', 'Only a building where people live', 'A type of government department'], 0),
    ('Which industry is closely associated with the Prairie provinces?', ['Farming', 'Fishing', 'An industry unrelated to the Prairies', 'Only tourism'], 0),
    ('Which industry is closely associated with Canada’s coastal regions?', ['Fishing', 'Farming grain crops', 'An industry unrelated to coastal regions', 'Only mining'], 0),
    ('Why do different regions of Canada rely on different industries?', ['Each region’s geography and resources shape which industries can thrive there', 'Every region of Canada has identical industries', 'A reason unrelated to geography', 'Industries are assigned randomly to each region'], 0),
    ('Which industry is closely associated with central Canada?', ['Manufacturing', 'Only fishing', 'An industry unrelated to central Canada', 'Only forestry'], 0)])]),
day(54, [
L('Writing: Compare and Contrast Paragraphs',
  'Grade 4 Language strand: a compare and contrast paragraph explains how two subjects are similar and how they are different, often using words like “however” and “similarly.”',
  [('A compare and contrast paragraph explains how two subjects are ___.', ['Similar and different', 'Only similar, never different', 'A concept unrelated to writing', 'Only different, never similar'], 0),
   ('Which word signals a comparison (similarity) between two ideas?', ['Similarly', 'However', 'A word unrelated to comparison', 'Although'], 0),
   ('Which word signals a contrast (difference) between two ideas?', ['However', 'Similarly', 'A word unrelated to contrast', 'Likewise'], 0),
   ('Why might a writer compare and contrast two animals in an essay?', ['To help readers understand how the animals are alike and different', 'Comparing animals serves no purpose in writing', 'A reason unrelated to writing', 'To make the essay longer with no added meaning'], 0),
   ('What should a compare and contrast paragraph include?', ['Specific details about both similarities and differences', 'Details about only one of the two subjects', 'A concept unrelated to this type of writing', 'No details at all, only opinions'], 0)]),
M('Volume of Rectangular Prisms',
  'Grade 4 Math strand: the volume of a rectangular prism is found by multiplying its length, width, and height, and is measured in cubic units.',
  [('The volume of a rectangular prism is found by multiplying ___.', ['Length × width × height', 'Only length × width', 'A formula unrelated to volume', 'Only the height of the shape'], 0),
   ('What is the volume of a rectangular prism with length 4, width 3, and height 2?', ['24 cubic units', '9 cubic units', 'A value unrelated to the calculation', '14 cubic units'], 0),
   ('Volume is measured in ___.', ['Cubic units', 'Square units', 'A unit unrelated to volume', 'Linear units'], 0),
   ('What is the volume of a rectangular prism with length 5, width 2, and height 3?', ['30 cubic units', '10 cubic units', 'A value unrelated to the calculation', '20 cubic units'], 0),
   ('Why is volume measured in cubic units rather than square units?', ['Because volume describes a three-dimensional space, not a flat area', 'Cubic units have no real meaning in math', 'A reason unrelated to measurement', 'Square units are always used for volume instead'], 0)]),
Sc('Simple Circuits: Series vs Parallel',
   'Grade 4 Science strand: in a series circuit, components are connected in a single loop, while in a parallel circuit, components are connected along multiple paths.',
   [('In a series circuit, components are connected ___.', ['Along a single loop, one after another', 'Along multiple separate paths', 'A concept unrelated to circuits', 'With no connection between them at all'], 0),
    ('In a parallel circuit, components are connected ___.', ['Along multiple separate paths', 'Along a single loop only', 'A concept unrelated to circuits', 'With no connection between them at all'], 0),
    ('What happens to the other bulbs in a series circuit if one bulb burns out?', ['They all turn off, since the loop is broken', 'They stay lit with no change at all', 'A result unrelated to circuits', 'They become brighter than before'], 0),
    ('What happens to the other bulbs in a parallel circuit if one bulb burns out?', ['The others can stay lit, since each has its own path', 'They all turn off immediately', 'A result unrelated to circuits', 'The entire house loses power'], 0),
    ('Why might parallel circuits be used for household wiring?', ['So that one broken device does not turn off all the others', 'Parallel circuits have no practical advantage', 'A reason unrelated to circuits', 'Series circuits are always used in houses instead'], 0)]),
SS('Indigenous Governance and Traditional Knowledge',
   'Grade 4 Social Studies strand: many Indigenous peoples in Canada have long-standing governance systems and traditional knowledge that guide decision-making and care for the land.',
   [('Traditional knowledge refers to ___.', ['Wisdom and practices passed down through generations within a community', 'Knowledge that has no connection to any community', 'A concept unrelated to Indigenous peoples', 'Information found only in modern textbooks'], 0),
    ('Indigenous governance systems often emphasize ___.', ['Community decision-making and care for the land', 'Decisions made entirely without community input', 'A concept unrelated to governance', 'Ignoring the needs of the land and environment'], 0),
    ('Why is it important to learn about Indigenous governance systems?', ['It builds a fuller understanding of the diverse ways communities have organized themselves', 'Indigenous governance has no relevance to Canadian history', 'A reason unrelated to social studies', 'Only one type of governance system has ever existed'], 0),
    ('Traditional knowledge is often passed down through ___.', ['Storytelling, teachings from elders, and lived experience', 'Written government documents only', 'A method unrelated to traditional knowledge', 'Sources with no connection to community elders'], 0),
    ('Why might traditional knowledge be valuable for understanding the environment?', ['It reflects generations of careful observation and relationship with the land', 'Traditional knowledge has no connection to the environment', 'A reason unrelated to Indigenous knowledge', 'It is based on guesses with no real observation involved'], 0)])]),
day(55, [
L('Reading: Distinguishing Fact from Opinion',
  'Grade 4 Language strand: a fact is a statement that can be proven true, while an opinion is a personal belief or judgment that cannot be proven.',
  [('A fact is a statement that ___.', ['Can be proven true', 'Reflects only one person’s feelings', 'A concept unrelated to reading', 'Can never be proven either way'], 0),
   ('An opinion is a statement that ___.', ['Reflects a personal belief or judgment', 'Can always be proven true with evidence', 'A concept unrelated to reading', 'Is the same for every single reader'], 0),
   ('Which of these is a fact?', ['Water freezes at 0 degrees Celsius.', 'Winter is the best season of the year.', 'A statement unrelated to facts or opinions', 'Chocolate ice cream tastes better than vanilla.'], 0),
   ('Which of these is an opinion?', ['Dogs make the best pets.', 'A dog is a mammal.', 'A statement unrelated to facts or opinions', 'Dogs have four legs.'], 0),
   ('Why is it important for readers to distinguish fact from opinion?', ['It helps them evaluate information critically and avoid being misled', 'This skill has no use when reading any text', 'A concept unrelated to reading comprehension', 'Facts and opinions are always exactly the same thing'], 0)]),
M('Temperature and Thermometers (Celsius)',
  'Grade 4 Math strand: temperature is measured in degrees Celsius in Canada, using a thermometer, with 0°C as the freezing point and 100°C as the boiling point of water.',
  [('In Celsius, water freezes at ___.', ['0 degrees', '100 degrees', 'A temperature unrelated to freezing', '32 degrees'], 0),
   ('In Celsius, water boils at ___.', ['100 degrees', '0 degrees', 'A temperature unrelated to boiling', '32 degrees'], 0),
   ('A thermometer is used to measure ___.', ['Temperature', 'Length', 'A quantity unrelated to thermometers', 'Weight'], 0),
   ('Which temperature would most likely describe a warm summer day in Ontario?', ['28 degrees Celsius', '-15 degrees Celsius', 'A temperature unrelated to a warm day', '0 degrees Celsius'], 0),
   ('Which temperature would most likely describe a cold winter day in Ontario?', ['-10 degrees Celsius', '30 degrees Celsius', 'A temperature unrelated to a cold day', '100 degrees Celsius'], 0)]),
Sc('Forces: Balanced and Unbalanced Forces',
   'Grade 4 Science strand: balanced forces on an object result in no change in motion, while unbalanced forces cause an object to speed up, slow down, or change direction.',
   [('Balanced forces on an object result in ___.', ['No change in the object’s motion', 'The object always speeding up', 'A concept unrelated to forces', 'The object always changing direction'], 0),
    ('Unbalanced forces on an object can cause it to ___.', ['Speed up, slow down, or change direction', 'Remain in exactly the same state forever', 'A concept unrelated to forces', 'Disappear completely'], 0),
    ('If two people push equally hard on opposite sides of a box and it does not move, the forces are ___.', ['Balanced', 'Unbalanced', 'A term unrelated to forces', 'Nonexistent'], 0),
    ('If a soccer ball is kicked and starts rolling, what kind of force acted on it?', ['An unbalanced force', 'A balanced force', 'A concept unrelated to forces', 'No force at all'], 0),
    ('Why is it useful to understand balanced and unbalanced forces?', ['It helps explain why objects stay still or change their motion', 'This concept has no connection to how objects move', 'A reason unrelated to forces', 'Forces never affect the motion of objects'], 0)]),
SS('Settlement Patterns: Why Communities Grow Where They Do',
   'Grade 4 Social Studies strand: communities often form and grow near resources such as fresh water, fertile land, and transportation routes.',
   [('Communities often settle near fresh water because it provides ___.', ['Drinking water, transportation, and support for farming', 'No useful resources at all', 'A concept unrelated to settlement', 'Only recreational swimming opportunities'], 0),
    ('Fertile land is valuable to a community because it supports ___.', ['Farming and food production', 'Nothing related to daily life', 'A concept unrelated to settlement patterns', 'Only mining activities'], 0),
    ('Why might a community grow near a major transportation route, such as a river or railway?', ['It makes trade and travel to other places easier', 'Transportation routes have no effect on where communities grow', 'A reason unrelated to settlement patterns', 'Communities never consider transportation when settling'], 0),
    ('Which of these would most likely attract early settlers to an area?', ['Access to fresh water and fertile land', 'An area with no resources of any kind', 'A concept unrelated to settlement', 'The colour of the soil alone'], 0),
    ('Why do geographers study settlement patterns?', ['It helps explain why communities are located where they are', 'Settlement patterns provide no useful information', 'A reason unrelated to geography', 'Communities are located in completely random places'], 0)])]),
day(56, [
L('Figurative Language: Hyperbole',
  'Grade 4 Language strand: hyperbole is an extreme exaggeration used for effect, such as saying “I have a million things to do.”',
  [('Hyperbole is a figure of speech that uses ___.', ['Extreme exaggeration for effect', 'Only literal, exact statements', 'A concept unrelated to figurative language', 'Comparisons using “like” or “as”'], 0),
   ('Which sentence contains a hyperbole?', ['I am so hungry I could eat a horse.', 'I ate a small snack this afternoon.', 'A sentence unrelated to hyperbole', 'I had a sandwich for lunch today.'], 0),
   ('Why do writers use hyperbole?', ['To emphasize a feeling or idea in a dramatic, memorable way', 'Hyperbole is never used for any purpose in writing', 'A reason unrelated to figurative language', 'To describe something in a completely literal way'], 0),
   ('Which sentence contains a hyperbole?', ['This backpack weighs a million pounds!', 'This backpack is a bit heavy today.', 'A sentence unrelated to hyperbole', 'My backpack has three pockets.'], 0),
   ('Is hyperbole meant to be taken literally?', ['No, it is an exaggeration for effect', 'Yes, hyperbole is always literally true', 'A concept unrelated to hyperbole', 'Hyperbole has no real meaning at all'], 0)]),
M('Ratios and Simple Proportional Reasoning (Intro)',
  'Grade 4 Math strand: a ratio compares two quantities, such as 2 red marbles for every 3 blue marbles, and can be used to solve simple proportional problems.',
  [('A ratio is used to ___.', ['Compare two quantities', 'Add two quantities together', 'A concept unrelated to ratios', 'Measure the length of an object'], 0),
   ('If a recipe uses a ratio of 2 cups of flour for every 1 cup of sugar, how much flour is needed for 2 cups of sugar?', ['4 cups', '2 cups', 'An amount unrelated to the ratio', '1 cup'], 0),
   ('A ratio of 3:1 means that for every 3 of one item, there is/are ___ of the other.', ['1', '3', 'A number unrelated to the ratio', '4'], 0),
   ('If a class has a ratio of 2 boys for every 3 girls, and there are 6 boys, how many girls are there?', ['9', '6', 'A number unrelated to the ratio', '3'], 0),
   ('Why are ratios useful in everyday life?', ['They help compare quantities and scale recipes, maps, and mixtures accurately', 'Ratios have no practical use in daily life', 'A reason unrelated to ratios', 'Ratios can only be used in advanced mathematics'], 0)]),
Sc('States of Matter and the Particle Model',
   'Grade 4 Science strand: matter exists in solid, liquid, and gas states, and the particle model explains that particles in a solid are tightly packed, in a liquid can move past each other, and in a gas move freely.',
   [('In a solid, particles are ___.', ['Tightly packed and vibrate in place', 'Spread far apart and moving freely', 'A description unrelated to particles', 'Not present at all'], 0),
    ('In a liquid, particles ___.', ['Can move and slide past one another', 'Are completely fixed in place', 'A description unrelated to particles', 'Spread out infinitely in all directions'], 0),
    ('In a gas, particles ___.', ['Move freely and spread far apart', 'Are tightly packed together', 'A description unrelated to particles', 'Remain completely still'], 0),
    ('The particle model helps explain ___.', ['Why matter behaves differently as a solid, liquid, or gas', 'Nothing about how matter behaves', 'A concept unrelated to matter', 'Only the colour of different materials'], 0),
    ('Which state of matter has particles that are the most tightly packed?', ['Solid', 'Gas', 'A state unrelated to particle spacing', 'Liquid'], 0)]),
SS('The Fur Trade in Canadian History',
   'Grade 4 Social Studies strand: the fur trade was a major economic activity in early Canadian history, involving Indigenous peoples and European traders exchanging goods such as furs, tools, and cloth.',
   [('The fur trade primarily involved the exchange of ___.', ['Furs for European tools, cloth, and other goods', 'Only gold and silver coins', 'A concept unrelated to the fur trade', 'Modern manufactured electronics'], 0),
    ('Which group played a central role in the fur trade as both trappers and traders?', ['Indigenous peoples', 'A group unrelated to the fur trade', 'Only settlers who arrived after the fur trade ended', 'People with no connection to the fur trade at all'], 0),
    ('Why was the fur trade economically important in early Canada?', ['It was a major source of income and connected different regions through trade routes', 'The fur trade had no economic importance in Canadian history', 'A reason unrelated to the fur trade', 'It only involved a handful of people with no wider impact'], 0),
    ('Which animal’s fur was especially valuable during the fur trade?', ['Beaver', 'An animal unrelated to the fur trade', 'Elephant', 'Kangaroo'], 0),
    ('How did the fur trade affect relationships between Indigenous peoples and European traders?', ['It created important economic and social relationships, though they were not always equal', 'It had no effect on relationships between the two groups', 'A reason unrelated to the fur trade', 'Indigenous peoples and European traders never interacted'], 0)])]),
day(57, [
L('Spelling: Compound Words',
  'Grade 4 Language strand: a compound word is formed by joining two smaller words together, such as “sun” and “flower” combining to make “sunflower.”',
  [('A compound word is formed by ___.', ['Joining two smaller words together', 'Removing letters from a single word', 'A concept unrelated to spelling', 'Adding a prefix only, with no second word'], 0),
   ('Which of these is a compound word?', ['Basketball', 'Running', 'A word unrelated to compound words', 'Happiness'], 0),
   ('What two smaller words make up “rainbow”?', ['Rain and bow', 'Rain and boat', 'Two words unrelated to “rainbow”', 'Ran and bow'], 0),
   ('Which of these is a compound word?', ['Toothbrush', 'Brushed', 'A word unrelated to compound words', 'Brushing'], 0),
   ('Why is it useful to recognize compound words when spelling?', ['It helps break a longer word into two familiar, smaller words', 'Compound words cannot be broken into smaller parts', 'A concept unrelated to spelling strategies', 'Recognizing compound words never helps with spelling'], 0)]),
M('Translations, Reflections, and Rotations',
  'Grade 4 Math strand: a translation slides a shape, a reflection flips a shape like a mirror image, and a rotation turns a shape around a fixed point.',
  [('A translation moves a shape by ___.', ['Sliding it without flipping or turning it', 'Flipping it like a mirror image', 'A movement unrelated to transformations', 'Turning it around a fixed point'], 0),
   ('A reflection creates a shape that is ___.', ['A mirror image of the original shape', 'An exact copy with no changes at all', 'A movement unrelated to transformations', 'Always larger than the original shape'], 0),
   ('A rotation moves a shape by ___.', ['Turning it around a fixed point', 'Sliding it in a straight line', 'A movement unrelated to transformations', 'Flipping it like a mirror image'], 0),
   ('If you slide a triangle three squares to the right without flipping or turning it, this is an example of a ___.', ['Translation', 'Reflection', 'A term unrelated to transformations', 'Rotation'], 0),
   ('If you flip a shape over a line so it looks like a mirror image, this is an example of a ___.', ['Reflection', 'Translation', 'A term unrelated to transformations', 'Rotation'], 0)]),
Sc('Water Conservation and the Water Cycle in Communities',
   'Grade 4 Science strand: communities rely on the water cycle for fresh water, and conserving water helps protect this limited resource for future use.',
   [('Water conservation means ___.', ['Using water carefully to avoid wasting it', 'Using as much water as possible at all times', 'A concept unrelated to water', 'Removing water from the environment permanently'], 0),
    ('Which is an example of water conservation at home?', ['Turning off the tap while brushing your teeth', 'Leaving the tap running for no reason', 'A concept unrelated to conserving water', 'Watering the lawn during a rainstorm'], 0),
    ('Why is it important for communities to conserve fresh water?', ['Fresh water is a limited resource that must be shared and protected', 'Fresh water is an unlimited resource with no need for conservation', 'A reason unrelated to water conservation', 'Communities never need to think about their water use'], 0),
    ('How does the water cycle provide fresh water to communities?', ['Precipitation refills rivers, lakes, and groundwater that communities depend on', 'The water cycle has no connection to community water supplies', 'A reason unrelated to the water cycle', 'Communities create their own water with no natural cycle involved'], 0),
    ('Which of these actions helps conserve water in a community?', ['Fixing leaky pipes and faucets promptly', 'Leaving leaks unfixed indefinitely', 'A concept unrelated to conservation', 'Wasting water intentionally to test the pipes'], 0)]),
SS('Canada’s Relationship with the Commonwealth',
   'Grade 4 Social Studies strand: Canada is a member of the Commonwealth, a voluntary association of countries, most of which were once part of the British Empire, that cooperate on shared goals.',
   [('The Commonwealth is a voluntary association of countries that ___.', ['Cooperate on shared goals, such as democracy and development', 'Are required to follow identical laws with no independence', 'A concept unrelated to international relationships', 'Have no historical connection to one another'], 0),
    ('Many Commonwealth countries share a historical connection to ___.', ['The former British Empire', 'A country unrelated to the Commonwealth', 'Only ancient civilizations', 'No shared history at all'], 0),
    ('Is Canada required to follow the laws of other Commonwealth countries?', ['No, Canada remains an independent, self-governing country', 'Yes, Canada must follow every Commonwealth country’s laws', 'A concept unrelated to Canada’s independence', 'Canada has no independent government of its own'], 0),
    ('Why might countries choose to remain part of the Commonwealth?', ['To cooperate on shared goals like trade, education, and development', 'Membership provides no benefits of any kind', 'A reason unrelated to international cooperation', 'Countries are forced to join with no choice involved'], 0),
    ('Which of these is true about the Commonwealth?', ['It includes many countries that were once part of the British Empire', 'It includes only countries that have never had any historical connection', 'A statement unrelated to the Commonwealth', 'It has existed for less than one year'], 0)])]),
day(58, [
L('Writing: Personal Narratives and Journals',
  'Grade 4 Language strand: a personal narrative tells a true story from the writer’s own life, often written in first person and organized in the order events happened.',
  [('A personal narrative tells a story that is ___.', ['True and based on the writer’s own life', 'Always completely fictional', 'A concept unrelated to writing', 'Written about someone the writer has never met'], 0),
   ('A personal narrative is usually written in ___.', ['First person, using “I”', 'Third person only, using “they”', 'A point of view unrelated to personal narratives', 'Second person only, using “you”'], 0),
   ('Personal narratives are often organized ___.', ['In the order the events happened', 'With no order or structure at all', 'A concept unrelated to organizing a narrative', 'In reverse alphabetical order'], 0),
   ('Why might someone keep a journal?', ['To record personal thoughts, feelings, and experiences over time', 'Journals serve no purpose for writers', 'A reason unrelated to journaling', 'To write only about topics unrelated to their own life'], 0),
   ('Which is an example of a topic for a personal narrative?', ['A memorable trip you took with your family', 'A fictional story about dragons with no basis in real life', 'A concept unrelated to personal narratives', 'A set of instructions for building a model'], 0)]),
M('Circle Graphs (Pie Charts)',
  'Grade 4 Math strand: a circle graph, or pie chart, shows data as slices of a circle, where each slice represents a proportion of the whole.',
  [('A circle graph shows data as ___.', ['Slices of a circle representing proportions of a whole', 'A single straight line', 'A concept unrelated to circle graphs', 'A list of numbers with no visual representation'], 0),
   ('In a circle graph, a larger slice represents ___.', ['A greater proportion of the total data', 'A smaller proportion of the total data', 'A concept unrelated to circle graphs', 'No data at all'], 0),
   ('If a circle graph shows that 50% of students prefer summer, what fraction of the circle would represent summer?', ['Half of the circle', 'A quarter of the circle', 'A fraction unrelated to the data', 'The entire circle'], 0),
   ('Why might someone use a circle graph instead of a bar graph?', ['To show how parts relate to the whole as proportions', 'Circle graphs cannot display any type of data', 'A reason unrelated to graphing data', 'Bar graphs and circle graphs always show identical information'], 0),
   ('All of the slices in a circle graph should add up to ___.', ['100% of the data', '50% of the data', 'A percentage unrelated to circle graphs', '0% of the data'], 0)]),
Sc('Space: The Sun and Its Role in Our Solar System',
   'Grade 4 Science strand: the Sun is a star at the centre of our solar system, providing the light and heat energy that supports life on Earth.',
   [('The Sun is best described as a ___.', ['Star at the centre of our solar system', 'Planet that orbits the Earth', 'A concept unrelated to space', 'Moon that orbits another planet'], 0),
    ('The Sun provides Earth with ___.', ['Light and heat energy', 'No energy of any kind', 'A concept unrelated to the Sun', 'Only darkness'], 0),
    ('Why is the Sun important for life on Earth?', ['It provides the energy that plants and other living things depend on', 'The Sun has no connection to life on Earth', 'A reason unrelated to the Sun’s role', 'Life on Earth exists with no need for any energy source'], 0),
    ('All the planets in our solar system orbit ___.', ['The Sun', 'The Moon', 'A body unrelated to our solar system', 'Earth'], 0),
    ('Compared to the planets, the Sun is ___.', ['Far larger and is a source of its own light', 'Much smaller and reflects light from Earth', 'A description unrelated to the Sun', 'Exactly the same size as Earth'], 0)]),
SS('Comparing Urban, Suburban, and Rural Communities',
   'Grade 4 Social Studies strand: communities can be classified as urban (city), suburban (residential areas near a city), or rural (countryside), each with different features and ways of life.',
   [('An urban community is best described as ___.', ['A densely populated city area', 'An area with very few people and mostly farmland', 'A concept unrelated to communities', 'A community found only in the far north'], 0),
    ('A rural community is best described as ___.', ['A countryside area often used for farming, with a lower population', 'A densely populated downtown core', 'A concept unrelated to communities', 'An area with no land used for any purpose'], 0),
    ('A suburban community is best described as ___.', ['A residential area located near, but outside, a city’s downtown', 'The very centre of a large city', 'A concept unrelated to communities', 'An area used only for large-scale farming'], 0),
    ('Which of these might you expect to find more often in a rural community?', ['Large farms and open land', 'Tall skyscrapers and dense traffic', 'A feature unrelated to rural communities', 'Subway systems'], 0),
    ('Why is it useful to compare urban, suburban, and rural communities?', ['It helps show how geography and population shape different ways of life', 'These types of communities have no differences worth studying', 'A reason unrelated to social studies', 'All communities in Canada are identical'], 0)])]),
day(59, [
L('Reading: Using Graphic Organizers',
  'Grade 4 Language strand: graphic organizers, such as Venn diagrams and story maps, help readers visually organize information and ideas from a text.',
  [('A graphic organizer helps readers ___.', ['Visually organize information and ideas from a text', 'Memorize a text word for word', 'A concept unrelated to reading', 'Avoid reading the text at all'], 0),
   ('A Venn diagram is often used to show ___.', ['Similarities and differences between two things', 'The order of events in a single story only', 'A concept unrelated to graphic organizers', 'The page numbers of a book'], 0),
   ('A story map is often used to organize ___.', ['The characters, setting, problem, and events of a story', 'Only the title of a book', 'A concept unrelated to graphic organizers', 'The price of a book'], 0),
   ('Why might a reader use a graphic organizer before writing a summary?', ['It helps sort out the most important ideas and details first', 'Graphic organizers never help with understanding a text', 'A reason unrelated to reading strategies', 'It replaces the need to read the text at all'], 0),
   ('Which graphic organizer would best help compare two book characters?', ['A Venn diagram', 'A single unrelated list', 'A concept unrelated to graphic organizers', 'A number line'], 0)]),
M('Mean, Median, and Mode (Intro)',
  'Grade 4 Math strand: the mean is the average of a set of numbers, the median is the middle value when numbers are ordered, and the mode is the value that appears most often.',
  [('The mean of a set of numbers is found by ___.', ['Adding all the numbers and dividing by how many there are', 'Choosing the largest number in the set', 'A method unrelated to finding the mean', 'Choosing the smallest number in the set'], 0),
   ('The median of a set of numbers is ___.', ['The middle value when the numbers are placed in order', 'Always the first number listed', 'A value unrelated to the median', 'The sum of all the numbers'], 0),
   ('The mode of a set of numbers is ___.', ['The value that appears most often', 'The largest value in the set', 'A value unrelated to the mode', 'The average of all the values'], 0),
   ('What is the median of the set 2, 4, 6, 8, 10?', ['6', '4', 'A value unrelated to the median', '10'], 0),
   ('What is the mode of the set 3, 5, 5, 7, 9?', ['5', '3', 'A value unrelated to the mode', '9'], 0)]),
Sc('Energy Transformations in Everyday Devices',
   'Grade 4 Science strand: many everyday devices transform energy from one form to another, such as a toaster changing electrical energy into heat energy.',
   [('Energy transformation means energy ___.', ['Changes from one form into another', 'Disappears completely with no trace', 'A concept unrelated to energy', 'Stays in the exact same form forever'], 0),
    ('A toaster transforms electrical energy into ___.', ['Heat energy', 'Sound energy only', 'A form of energy unrelated to toasters', 'Light energy only'], 0),
    ('A light bulb transforms electrical energy into ___.', ['Light energy (and some heat energy)', 'Sound energy only', 'A form of energy unrelated to light bulbs', 'Chemical energy only'], 0),
    ('A speaker transforms electrical energy into ___.', ['Sound energy', 'Light energy only', 'A form of energy unrelated to speakers', 'Heat energy only'], 0),
    ('Why is it useful to understand energy transformations in devices?', ['It helps explain how everyday technology works and uses energy', 'Energy transformations have no connection to how devices work', 'A reason unrelated to energy', 'Devices never use or change energy in any way'], 0)]),
SS('Cultural Diversity and Multiculturalism in Canada',
   'Grade 4 Social Studies strand: Canada is home to people from many different cultural backgrounds, and multiculturalism celebrates and protects this diversity as an official policy.',
   [('Multiculturalism is a policy that ___.', ['Celebrates and protects Canada’s cultural diversity', 'Requires everyone to share the exact same culture', 'A concept unrelated to Canadian society', 'Ignores the cultural backgrounds of Canadians'], 0),
    ('Cultural diversity in a community means ___.', ['People from many different cultural backgrounds live together', 'Everyone in the community shares an identical background', 'A concept unrelated to communities', 'No cultural traditions are practiced at all'], 0),
    ('Which is an example of cultural diversity in a Canadian community?', ['Neighbours celebrating different cultural festivals throughout the year', 'A community where only one culture is ever represented', 'A concept unrelated to cultural diversity', 'A town with no cultural traditions of any kind'], 0),
    ('Why does Canada value multiculturalism?', ['It recognizes and respects the contributions of people from many backgrounds', 'Multiculturalism provides no value to Canadian society', 'A reason unrelated to Canadian identity', 'Canada requires all citizens to abandon their cultural traditions'], 0),
    ('How might multiculturalism be reflected in a Canadian city?', ['Through diverse foods, festivals, languages, and traditions', 'Through a complete absence of cultural variety', 'A concept unrelated to multiculturalism', 'Through laws banning cultural celebrations'], 0)])]),
day(60, [
L('Grammar: Capitalization Rules',
  'Grade 4 Language strand: capitalization rules include starting every sentence with a capital letter, capitalizing proper nouns, and capitalizing the pronoun “I.”',
  [('Every sentence should begin with ___.', ['A capital letter', 'A lowercase letter', 'A concept unrelated to capitalization', 'A number, with no letters at all'], 0),
   ('Proper nouns, such as names of people and places, should be ___.', ['Capitalized', 'Written entirely in lowercase', 'A concept unrelated to proper nouns', 'Underlined instead of capitalized'], 0),
   ('The pronoun “I” should always be ___.', ['Capitalized, no matter where it appears in a sentence', 'Written in lowercase at the start of a sentence', 'A concept unrelated to capitalization', 'Left out of formal writing entirely'], 0),
   ('Which sentence uses capitalization correctly?', ['My friend and I visited Toronto last summer.', 'my friend and i visited toronto last summer.', 'A sentence unrelated to capitalization', 'My friend and i visited Toronto last Summer.'], 0),
   ('Why are capitalization rules important in writing?', ['They help readers understand sentence boundaries and identify proper nouns', 'Capitalization has no effect on how writing is understood', 'A concept unrelated to grammar', 'Capital letters are only used to make writing look nicer'], 0)]),
M('Review: Fractions, Decimals, and Patterns',
  'Grade 4 Math strand: this review lesson revisits key ideas from Days 51-60, including multiplying fractions, angles, ratios, transformations, and mean/median/mode.',
  [('Multiplying a fraction by a whole number is the same as ___.', ['Adding that fraction the given number of times', 'Dividing the whole number by the fraction', 'A concept unrelated to fractions', 'Subtracting the fraction from the whole number'], 0),
   ('A protractor is used to measure ___.', ['Angles', 'Length', 'A quantity unrelated to protractors', 'Weight'], 0),
   ('A ratio is used to ___.', ['Compare two quantities', 'Measure the volume of a container', 'A concept unrelated to ratios', 'Round a number to the nearest ten'], 0),
   ('A translation moves a shape by ___.', ['Sliding it without flipping or turning it', 'Turning it around a fixed point', 'A movement unrelated to transformations', 'Flipping it like a mirror image'], 0),
   ('Why is it useful to review fractions, angles, ratios, and data together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Forces, Structures, and Systems',
   'Grade 4 Science strand: this review lesson revisits key ideas from Days 51-60, including ecosystems, rock classification, sound, circuits, balanced forces, states of matter, and energy transformations.',
   [('Interdependence in an ecosystem means living things ___.', ['Rely on each other and their environment to survive', 'Never interact with each other in any way', 'A concept unrelated to ecosystems', 'Live completely apart from their environment'], 0),
    ('Balanced forces on an object result in ___.', ['No change in the object’s motion', 'The object always speeding up', 'A concept unrelated to forces', 'The object always changing direction'], 0),
    ('In a series circuit, components are connected ___.', ['Along a single loop, one after another', 'Along multiple separate paths', 'A concept unrelated to circuits', 'With no connection between them at all'], 0),
    ('Energy transformation means energy ___.', ['Changes from one form into another', 'Disappears completely with no trace', 'A concept unrelated to energy', 'Stays in the exact same form forever'], 0),
    ('Why is it useful to review forces, circuits, and energy together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Culminating Task: Designing a Model Community',
   'Grade 4 Social Studies strand: this culminating task asks students to apply Days 51-60 learning about mapping, government, industries, settlement, and diversity to design a model community.',
   [('Why might a student consider access to fresh water when designing a model community?', ['Communities have historically settled near water for drinking, transportation, and farming', 'Fresh water has no connection to where communities are located', 'A reason unrelated to settlement patterns', 'Model communities never need to consider natural resources'], 0),
    ('Why might a student include all three levels of government when planning a model community?', ['Different levels of government are each responsible for different community needs', 'A community only ever needs a single level of government', 'A reason unrelated to Canadian government structure', 'Levels of government have no connection to community planning'], 0),
    ('Why might a student choose to include diverse cultural festivals in a model community?', ['It reflects the value of cultural diversity and multiculturalism seen in real Canadian communities', 'Cultural diversity has no relevance to designing a community', 'A reason unrelated to multiculturalism', 'Model communities should avoid representing any culture at all'], 0),
    ('Why might a student include local industries, such as farming or manufacturing, in a model community?', ['Industries reflect how a community’s geography supports its economy', 'Industries have no connection to how a community functions', 'A reason unrelated to economics', 'Every community relies on exactly the same industry'], 0),
    ('Why is a culminating task a valuable way to end this set of Social Studies lessons?', ['It lets students apply many ideas from the unit together in one project', 'Culminating tasks never help reinforce prior learning', 'A reason unrelated to social studies learning', 'Applying multiple ideas together provides no educational benefit'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260730):
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
    _rebalance_answer_positions(g4_51_60)
    append_to(4, g4_51_60)
