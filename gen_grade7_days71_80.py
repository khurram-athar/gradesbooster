#!/usr/bin/env python3
"""Phase 3 extension: Grade 7, Days 71-80 (third batch past the Day 70
milestone, continuing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-70 set (see data/grade7.json
and gen_grade7_days61_70.py): narrative point of view, decimals and
geometry, atoms and light, and formative episodes in Canadian and world
history through the dawn of the nuclear age.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science & Technology',
    'TVO Learn: Grade 7 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L7, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M7, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S7, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS7, q)


g7_71_80 = [
day(71, [
L('Point of View: First-Person, Third-Person Limited, and Omniscient Narration',
  'Grade 7 Language strand: point of view describes who is telling a story — first-person narrators use I, third-person limited narrators reveal one character’s thoughts, and third-person omniscient narrators know the thoughts of every character.',
  [('A first-person narrator tells a story using ___.', ['Pronouns such as I and we', 'Only third-person pronouns like he and she', 'A concept unrelated to point of view', 'No pronouns of any kind'], 0),
   ('A third-person limited narrator reveals the thoughts of ___.', ['Only one character', 'Every character in the story', 'A concept unrelated to third-person limited narration', 'No character at all'], 0),
   ('A third-person omniscient narrator ___.', ['Knows the thoughts and feelings of every character', 'Can only describe what one character sees', 'A concept unrelated to omniscient narration', 'Has no knowledge of any character’s thoughts'], 0),
   ('Which sentence is told from a first-person point of view?', ['I walked slowly toward the old house.', 'She walked slowly toward the old house.', 'A sentence unrelated to point of view', 'He and she walked toward the house together.'], 0),
   ('Why might an author choose a limited point of view instead of an omniscient one?', ['It can build suspense by keeping some information hidden from the reader', 'Point of view never affects how a reader experiences a story', 'A reason unrelated to point of view', 'Omniscient narration always reveals less information than limited narration'], 0)]),
M('Circle Graphs (Pie Charts): Constructing and Interpreting',
  'Grade 7 Math strand: a circle graph (pie chart) represents data as proportional slices of a circle, where each slice’s size corresponds to its percentage of the whole data set.',
  [('A circle graph represents data using ___.', ['Proportional slices of a circle', 'A single straight line', 'A concept unrelated to circle graphs', 'A grid of individual dots'], 0),
   ('In a circle graph, a larger slice represents ___.', ['A greater percentage of the total data', 'A smaller percentage of the total data', 'A concept unrelated to circle graphs', 'No connection to the data at all'], 0),
   ('If a circle graph shows that 50% of students chose pizza as their favourite food, that slice would take up ___ of the circle.', ['Half', 'A quarter', 'A value unrelated to the calculation', 'The entire circle'], 0),
   ('A full circle graph always represents ___.', ['100% of the data', '50% of the data', 'A value unrelated to circle graphs', '0% of the data'], 0),
   ('Why might a circle graph be a good choice for displaying survey results?', ['It clearly shows how each category compares as a proportion of the whole', 'Circle graphs never show proportions clearly', 'A reason unrelated to displaying data', 'Circle graphs can only display exactly two categories'], 0)]),
Sc('Introduction to Atoms, Elements, and the Periodic Table',
   'Grade 7 Science strand: atoms are the basic building blocks of matter, elements are pure substances made of only one type of atom, and the periodic table organizes all known elements by their properties.',
   [('An atom is ___.', ['The basic building block of matter', 'A mixture of two or more substances', 'A concept unrelated to atoms', 'A type of chemical reaction'], 0),
    ('An element is a pure substance made of ___.', ['Only one type of atom', 'Two or more different types of atoms combined', 'A concept unrelated to elements', 'No atoms at all'], 0),
    ('The periodic table organizes elements by their ___.', ['Properties, such as atomic structure and behaviour', 'Colour only', 'A concept unrelated to the periodic table', 'Alphabetical order only'], 0),
    ('Which of these is an example of an element?', ['Oxygen', 'Water', 'A substance unrelated to elements', 'Salt water'], 0),
    ('Why is the periodic table a useful tool for scientists?', ['It organizes elements in a way that reveals patterns in their properties', 'The periodic table provides no useful scientific information', 'A reason unrelated to the periodic table', 'Elements on the periodic table share no patterns at all'], 0)]),
SS('The Acadian Expulsion (Le Grand Dérangement)',
   'Grade 7 Social Studies strand: the Acadian Expulsion, known as Le Grand Dérangement, was the forced removal of thousands of Acadian settlers from their homes by the British in the 1750s.',
   [('The Acadian Expulsion involved the forced removal of ___.', ['Thousands of Acadian settlers from their homes', 'A small group of British soldiers', 'A concept unrelated to the Acadian Expulsion', 'No people at all'], 0),
    ('The Acadian Expulsion was carried out by ___.', ['The British', 'The French government alone', 'A group unrelated to the Acadian Expulsion', 'Indigenous nations acting alone'], 0),
    ('Le Grand Dérangement took place primarily during the ___.', ['1750s', '1950s', 'A time period unrelated to the Acadian Expulsion', '1850s'], 0),
    ('Many Acadians who were expelled were forced to ___.', ['Resettle in distant and unfamiliar regions', 'Remain safely in their original homes', 'A consequence unrelated to the Acadian Expulsion', 'Immediately return home within days'], 0),
    ('Why is the Acadian Expulsion an important event to study in Canadian history?', ['It highlights the impact of colonial conflict on the lives of settler communities', 'The Acadian Expulsion had no lasting impact on Canadian history', 'A reason unrelated to its historical significance', 'This event never actually took place'], 0)])]),
day(72, [
L('Writing: Writing a Short Story with a Clear Plot Arc',
  'Grade 7 Language strand: a short story with a clear plot arc follows a structure of exposition, rising action, climax, falling action, and resolution to build tension and satisfy the reader.',
  [('The exposition of a story introduces ___.', ['The characters, setting, and initial situation', 'The final resolution of the conflict', 'A concept unrelated to exposition', 'Only the story’s title'], 0),
   ('The climax of a story is ___.', ['The turning point or moment of highest tension', 'The very first event in the story', 'A concept unrelated to a story’s climax', 'A part of the story with no importance'], 0),
   ('Rising action refers to the events that ___.', ['Build tension and lead toward the climax', 'Happen after the story’s conflict is resolved', 'A concept unrelated to rising action', 'Occur only in the story’s final sentence'], 0),
   ('The resolution of a story typically ___.', ['Shows how the conflict is finally settled', 'Introduces the main characters for the first time', 'A concept unrelated to a story’s resolution', 'Builds tension toward the climax'], 0),
   ('Why is a clear plot arc useful when writing a short story?', ['It helps organize events so the story builds tension and feels satisfying to readers', 'A plot arc never affects how a story is experienced', 'A reason unrelated to writing a short story', 'Stories are always more effective with no structure at all'], 0)]),
M('Repeating and Terminating Decimals',
  'Grade 7 Math strand: a terminating decimal ends after a finite number of digits, while a repeating decimal has one or more digits that repeat infinitely, and both can result from converting fractions to decimal form.',
  [('A terminating decimal is a decimal that ___.', ['Ends after a finite number of digits', 'Repeats the same digits forever', 'A concept unrelated to terminating decimals', 'Has no digits after the decimal point'], 0),
   ('A repeating decimal is a decimal in which ___.', ['One or more digits repeat infinitely', 'The digits always end after two places', 'A concept unrelated to repeating decimals', 'No digits ever appear after the decimal point'], 0),
   ('Which fraction converts to a terminating decimal?', ['1/4', '1/3', 'A fraction unrelated to the calculation', '2/3'], 0),
   ('Which fraction converts to a repeating decimal?', ['1/3', '1/2', 'A fraction unrelated to the calculation', '3/4'], 0),
   ('Why is it useful to recognize whether a decimal terminates or repeats?', ['It helps identify patterns when converting between fractions and decimals', 'This distinction never matters when working with decimals', 'A reason unrelated to decimals', 'All decimals terminate after exactly one digit'], 0)]),
Sc('Static Electricity and Electric Charge',
   'Grade 7 Science strand: static electricity builds up when electric charges accumulate on the surface of an object, often due to friction, and can cause objects to attract or repel one another.',
   [('Static electricity builds up when ___.', ['Electric charges accumulate on the surface of an object', 'An object loses all of its mass', 'A concept unrelated to static electricity', 'A magnet is placed near metal'], 0),
    ('Static electricity is often caused by ___.', ['Friction between two objects', 'Objects being placed in water', 'A concept unrelated to static electricity', 'A decrease in temperature alone'], 0),
    ('Objects with the same electric charge will ___ each other.', ['Repel', 'Attract', 'A concept unrelated to electric charge', 'Have no effect on'], 0),
    ('Objects with opposite electric charges will ___ each other.', ['Attract', 'Repel', 'A concept unrelated to electric charge', 'Have no effect on'], 0),
    ('Why does rubbing a balloon on hair sometimes cause it to stick to a wall?', ['The friction transfers electric charge, creating an attraction between the balloon and the wall', 'Balloons always stick to walls regardless of electric charge', 'A reason unrelated to static electricity', 'Friction removes all electric charge from the balloon'], 0)]),
SS('The Underground Railroad and Its Connection to Canada',
   'Grade 7 Social Studies strand: the Underground Railroad was a secret network of routes and safe houses that helped freedom seekers escape enslavement in the United States, with many settling in British North America, including present-day Ontario.',
   [('The Underground Railroad was a secret network that helped ___.', ['Freedom seekers escape enslavement in the United States', 'Settlers travel to Europe for trade', 'A concept unrelated to the Underground Railroad', 'Soldiers move between military bases'], 0),
    ('Many freedom seekers who used the Underground Railroad settled in ___.', ['British North America, including present-day Ontario', 'A region unrelated to the Underground Railroad', 'The southern United States', 'Regions with no connection to freedom seekers'], 0),
    ('The Underground Railroad relied on ___.', ['Secret routes and safe houses run by helpers along the way', 'Official government railways with public schedules', 'A concept unrelated to the Underground Railroad', 'A single, well-known public road'], 0),
    ('Why did British North America become a destination for freedom seekers?', ['Slavery had been abolished there, offering greater safety and freedom', 'British North America required freedom seekers to remain enslaved', 'A reason unrelated to the Underground Railroad', 'British North America had no laws regarding slavery at all'], 0),
    ('Why is the Underground Railroad an important part of Canadian history?', ['It highlights Canada’s role as a destination for people escaping enslavement', 'The Underground Railroad has no connection to Canadian history', 'A reason unrelated to its historical significance', 'This network only ever operated within Canada’s borders'], 0)])]),
day(73, [
L('Grammar: Correcting Pronoun-Antecedent Agreement Errors',
  'Grade 7 Language strand: a pronoun must agree in number with its antecedent, the noun it replaces, to avoid confusing or grammatically incorrect sentences.',
  [('An antecedent is ___.', ['The noun that a pronoun refers back to', 'A type of punctuation mark', 'A concept unrelated to antecedents', 'A verb tense used in formal writing'], 0),
   ('Which sentence shows correct pronoun-antecedent agreement?', ['The girls packed their bags for the trip.', 'The girls packed her bags for the trip.', 'A sentence unrelated to pronoun-antecedent agreement', 'The girl packed their bags for the trip.'], 0),
   ('If the antecedent is singular, the pronoun that replaces it must also be ___.', ['Singular', 'Plural', 'A concept unrelated to pronoun-antecedent agreement', 'Written in all capital letters'], 0),
   ('Which sentence contains a pronoun-antecedent agreement error?', ['The book fell off their shelf and landed on the floor.', 'The book fell off its shelf and landed on the floor.', 'A sentence unrelated to pronoun-antecedent agreement', 'The books fell off their shelf and landed on the floor.'], 0),
   ('Why is it important to match a pronoun with its correct antecedent?', ['It helps readers clearly understand which noun the pronoun is referring to', 'Pronoun-antecedent agreement never affects how clear a sentence is', 'A reason unrelated to grammar', 'Antecedents have no connection to the pronouns used in a sentence'], 0)]),
M('The Cartesian Plane and Plotting in All Four Quadrants',
  'Grade 7 Math strand: the Cartesian plane is divided into four quadrants by a horizontal x-axis and vertical y-axis, and each point is located using an ordered pair (x, y).',
  [('The Cartesian plane is divided into ___ quadrants.', ['Four', 'Two', 'A number unrelated to the Cartesian plane', 'Eight'], 0),
   ('An ordered pair (x, y) identifies a point’s location using ___.', ['Its distance along the x-axis and y-axis', 'Only its distance from the origin', 'A concept unrelated to ordered pairs', 'The colour of the point'], 0),
   ('In which quadrant would the point (-3, 4) be located?', ['The second quadrant', 'The first quadrant', 'A quadrant unrelated to this point', 'The fourth quadrant'], 0),
   ('The point where the x-axis and y-axis intersect is called the ___.', ['Origin', 'Vertex', 'A term unrelated to the Cartesian plane', 'Median'], 0),
   ('Why is the Cartesian plane useful in mathematics?', ['It allows points, shapes, and relationships to be represented and analyzed visually', 'The Cartesian plane has no practical mathematical use', 'A reason unrelated to the Cartesian plane', 'Points can only be described using words, never a plane'], 0)]),
Sc('Light: Reflection and the Law of Reflection',
   'Grade 7 Science strand: reflection occurs when light bounces off a surface, and the law of reflection states that the angle at which light hits a surface equals the angle at which it bounces off.',
   [('Reflection occurs when ___.', ['Light bounces off a surface', 'Light bends as it passes through a new material', 'A concept unrelated to reflection', 'Light is completely absorbed by a surface'], 0),
    ('The law of reflection states that the angle of incidence ___.', ['Equals the angle of reflection', 'Is always greater than the angle of reflection', 'A concept unrelated to the law of reflection', 'Has no relationship to the angle of reflection'], 0),
    ('A smooth, shiny surface like a mirror produces a ___ reflection.', ['Clear', 'Scattered', 'A concept unrelated to reflection', 'Completely invisible'], 0),
    ('A rough surface, such as paper, produces a reflection that is ___.', ['Scattered in many directions', 'Perfectly clear and focused', 'A concept unrelated to reflection off rough surfaces', 'Completely absorbed with no light bouncing at all'], 0),
    ('Why can you see your reflection clearly in a mirror but not in a piece of paper?', ['A mirror’s smooth surface reflects light in an organized way, while paper scatters light in many directions', 'Paper reflects light exactly the same way a mirror does', 'A reason unrelated to reflection', 'Mirrors do not actually reflect any light'], 0)]),
SS('The Persons Case and Women’s Legal Rights in Canada',
   'Grade 7 Social Studies strand: the Persons Case was a 1929 legal ruling that recognized women as “persons” eligible to serve in the Canadian Senate, marking a major milestone in the fight for women’s legal rights.',
   [('The Persons Case was a legal ruling that recognized women as ___.', ['“Persons” eligible to serve in the Canadian Senate', 'Ineligible for any political involvement', 'A concept unrelated to the Persons Case', 'Persons only for the purpose of paying taxes'], 0),
    ('The Persons Case was decided in ___.', ['1929', '1867', 'A year unrelated to the Persons Case', '1982'], 0),
    ('Before the Persons Case, women were often excluded from ___.', ['Serving in the Canadian Senate', 'All forms of paid employment', 'A concept unrelated to the Persons Case', 'Attending public schools'], 0),
    ('The group of women who led the legal challenge in the Persons Case became known as ___.', ['The Famous Five', 'The Confederation Five', 'A group unrelated to the Persons Case', 'The Senate Six'], 0),
    ('Why is the Persons Case considered a significant milestone in Canadian history?', ['It expanded legal recognition and rights for women in Canadian public life', 'The Persons Case had no effect on women’s rights', 'A reason unrelated to its historical significance', 'The Persons Case reduced legal rights for women'], 0)])]),
day(74, [
L('Vocabulary: Etymology and Word Origins',
  'Grade 7 Language strand: etymology is the study of where words come from and how their meanings have changed over time, often tracing roots back to languages such as Latin or Greek.',
  [('Etymology is the study of ___.', ['Where words come from and how their meanings have changed over time', 'How to spell words correctly', 'A concept unrelated to etymology', 'The grammar rules of a language'], 0),
   ('Many English words trace their origins back to ___.', ['Languages such as Latin or Greek', 'Only modern English slang', 'A concept unrelated to word origins', 'Numbers and mathematical symbols'], 0),
   ('Knowing a word’s Greek or Latin root can help a reader ___.', ['Figure out the meaning of unfamiliar related words', 'Guess the exact spelling of any word', 'A concept unrelated to word origins', 'Determine the punctuation of a sentence'], 0),
   ('The word biology comes from Greek roots meaning ___.', ['The study of life', 'The study of numbers', 'A meaning unrelated to the word biology', 'The study of ancient buildings'], 0),
   ('Why is studying etymology useful for building vocabulary?', ['Recognizing common roots helps readers decode the meaning of many unfamiliar words', 'Word origins never help with understanding vocabulary', 'A reason unrelated to etymology', 'Every word in English has a completely unrelated, unique origin'], 0)]),
M('Congruence and Symmetry in 2D Shapes',
  'Grade 7 Math strand: congruent shapes are identical in size and shape, and a shape has line symmetry if it can be folded along a line so both halves match exactly.',
  [('Two shapes are congruent if they are ___.', ['Identical in size and shape', 'Similar in shape but different in size', 'A concept unrelated to congruence', 'Different in both size and shape'], 0),
   ('A shape has line symmetry if ___.', ['It can be folded along a line so both halves match exactly', 'It can never be folded to match on both sides', 'A concept unrelated to line symmetry', 'It has more than four sides'], 0),
   ('How many lines of symmetry does a square have?', ['Four', 'Two', 'A number unrelated to the calculation', 'Zero'], 0),
   ('Which shape is an example of two congruent triangles placed together?', ['A rectangle divided in half diagonally', 'A circle with no straight edges', 'A shape unrelated to congruent triangles', 'A single triangle with no division'], 0),
   ('Why is understanding congruence and symmetry useful in geometry?', ['It helps identify relationships and patterns between shapes', 'Congruence and symmetry have no practical use in geometry', 'A reason unrelated to this topic', 'All shapes are automatically congruent to one another'], 0)]),
Sc('Adaptations and Natural Selection: An Introduction',
   'Grade 7 Science strand: an adaptation is a trait that helps an organism survive in its environment, and natural selection is the process by which organisms with helpful adaptations are more likely to survive and reproduce.',
   [('An adaptation is a trait that ___.', ['Helps an organism survive in its environment', 'Always harms an organism’s chances of survival', 'A concept unrelated to adaptations', 'Has no effect on an organism’s survival'], 0),
    ('Natural selection is the process by which ___.', ['Organisms with helpful adaptations are more likely to survive and reproduce', 'All organisms survive and reproduce equally, regardless of traits', 'A concept unrelated to natural selection', 'Organisms lose all of their adaptations over time'], 0),
    ('Which is an example of a physical adaptation?', ['A polar bear’s thick fur for insulation in cold climates', 'A rock sitting in a cold climate', 'A concept unrelated to physical adaptations', 'An object with no living characteristics'], 0),
    ('A behavioural adaptation is best described as ___.', ['An action an organism takes to help it survive', 'A physical body part used for survival', 'A concept unrelated to behavioural adaptations', 'A trait with no connection to survival'], 0),
    ('Why do organisms with helpful adaptations tend to survive and reproduce more successfully over time?', ['Their traits make them better suited to overcome challenges in their environment', 'Adaptations never affect an organism’s chances of survival', 'A reason unrelated to natural selection', 'All organisms in an environment face identical challenges regardless of traits'], 0)]),
SS('The October Crisis and the War Measures Act',
   'Grade 7 Social Studies strand: the October Crisis of 1970 was a major political crisis centred in Quebec that led the federal government to invoke the War Measures Act, temporarily suspending certain civil liberties to respond to the emergency.',
   [('The October Crisis took place in ___.', ['1970', '1867', 'A year unrelated to the October Crisis', '1929'], 0),
    ('The War Measures Act, when invoked, allowed the federal government to ___.', ['Temporarily suspend certain civil liberties during an emergency', 'Immediately dissolve all provincial governments', 'A concept unrelated to the War Measures Act', 'Permanently remove a province from Confederation'], 0),
    ('The October Crisis was centred in the province of ___.', ['Quebec', 'Ontario', 'A province unrelated to the October Crisis', 'British Columbia'], 0),
    ('Invoking the War Measures Act during the October Crisis was controversial because it ___.', ['Limited civil liberties that Canadians normally have', 'Had no effect on the rights of Canadian citizens', 'A reason unrelated to the controversy', 'Only applied to citizens outside of Canada'], 0),
    ('Why do historians and students study the October Crisis today?', ['It raises important questions about balancing public safety with civil liberties during a crisis', 'The October Crisis has no connection to understanding Canadian history', 'A reason unrelated to its historical significance', 'This event never actually took place'], 0)])]),
day(75, [
L('Reading: Identifying Cause and Effect Relationships in Text',
  'Grade 7 Language strand: identifying cause and effect in a text involves recognizing how one event or action (the cause) leads directly to a result (the effect).',
  [('A cause-and-effect relationship shows how ___.', ['One event leads directly to a result', 'Two unrelated events happen at the same time', 'A concept unrelated to cause and effect', 'A story’s setting connects to its characters'], 0),
   ('In the sentence “Because it rained, the game was cancelled,” the cause is ___.', ['It rained', 'The game was cancelled', 'A concept unrelated to this sentence', 'Neither part of the sentence'], 0),
   ('Which signal word often introduces an effect in a sentence?', ['Therefore', 'Meanwhile', 'A word unrelated to cause and effect', 'Similarly'], 0),
   ('Which sentence shows a clear cause-and-effect relationship?', ['She forgot her umbrella, so she got soaked in the rain.', 'She has a red umbrella and a blue raincoat.', 'A sentence unrelated to cause and effect', 'The umbrella and the raincoat were both new.'], 0),
   ('Why is it useful for readers to identify cause-and-effect relationships in a text?', ['It helps readers understand why events happen and how ideas are connected', 'Cause-and-effect relationships never help readers understand a text', 'A reason unrelated to reading comprehension', 'Every event in a text happens for no reason at all'], 0)]),
M('Data: Constructing and Interpreting Stem-and-Leaf Plots',
  'Grade 7 Math strand: a stem-and-leaf plot organizes numerical data by splitting each value into a “stem” (leading digits) and a “leaf” (last digit), making it easy to see the shape and spread of a data set.',
  [('In a stem-and-leaf plot, the “stem” usually represents ___.', ['The leading digit or digits of a value', 'The final digit of a value', 'A concept unrelated to stem-and-leaf plots', 'The total number of data points'], 0),
   ('In a stem-and-leaf plot, the “leaf” usually represents ___.', ['The last digit of a value', 'The leading digit of a value', 'A concept unrelated to stem-and-leaf plots', 'The average of all values'], 0),
   ('For the value 47, which digit would typically be the stem?', ['4', '7', 'A digit unrelated to the calculation', '47'], 0),
   ('One advantage of a stem-and-leaf plot is that it ___.', ['Displays every individual data value while showing overall patterns', 'Hides all of the individual data values', 'A concept unrelated to stem-and-leaf plots', 'Only works with exactly two data points'], 0),
   ('Why might a stem-and-leaf plot be useful for analyzing a set of test scores?', ['It shows both the exact scores and the overall distribution at a glance', 'Stem-and-leaf plots cannot display exact data values', 'A reason unrelated to analyzing data', 'This type of plot only works with negative numbers'], 0)]),
Sc('Ocean Currents and Their Influence on Climate',
   'Grade 7 Science strand: ocean currents are large-scale movements of seawater driven by wind, temperature, and salinity differences, and they play a major role in distributing heat and shaping climate around the world.',
   [('Ocean currents are large-scale movements of ___.', ['Seawater', 'Only surface ice', 'A concept unrelated to ocean currents', 'Underground freshwater'], 0),
    ('Which of these can drive ocean currents?', ['Differences in wind, temperature, and salinity', 'The colour of the water', 'A concept unrelated to ocean currents', 'The number of fish in the ocean'], 0),
    ('Ocean currents play a major role in ___.', ['Distributing heat and shaping climate around the world', 'Preventing any heat from moving through the ocean', 'A concept unrelated to ocean currents', 'Keeping all regions of the world at the exact same temperature'], 0),
    ('A warm ocean current flowing toward a coastal region can cause that region’s climate to be ___.', ['Milder than it would otherwise be', 'Colder than it would otherwise be', 'A concept unrelated to ocean currents', 'Completely unaffected by the current'], 0),
    ('Why do scientists study ocean currents when trying to understand global climate patterns?', ['Ocean currents move large amounts of heat around the planet, directly influencing regional climates', 'Ocean currents have no connection to climate patterns', 'A reason unrelated to ocean currents', 'Ocean currents only affect a single, isolated location'], 0)]),
SS('Population Pyramids and Demographic Transition',
   'Grade 7 Social Studies strand: a population pyramid is a graph showing the age and sex distribution of a population, and demographic transition describes how birth and death rates change as a country develops economically.',
   [('A population pyramid displays a population’s distribution by ___.', ['Age and sex', 'Income level only', 'A concept unrelated to population pyramids', 'Favourite occupations'], 0),
    ('A population pyramid with a wide base typically indicates ___.', ['A high birth rate and a young population', 'A low birth rate and an aging population', 'A concept unrelated to population pyramids', 'No connection to birth rates at all'], 0),
    ('Demographic transition describes how ___.', ['Birth and death rates change as a country develops economically', 'A country’s borders change over time', 'A concept unrelated to demographic transition', 'A population’s culture disappears completely'], 0),
    ('A country with a narrowing pyramid base over time often reflects ___.', ['Declining birth rates', 'Rapidly increasing birth rates', 'A concept unrelated to population pyramids', 'No change in birth rates at all'], 0),
    ('Why are population pyramids useful tools for geographers and planners?', ['They help predict future needs for schools, healthcare, and other services', 'Population pyramids provide no useful information for planning', 'A reason unrelated to population pyramids', 'Population data never changes over time'], 0)])]),
day(76, [
L('Media Literacy: Analyzing Podcasts and Audio Storytelling',
  'Grade 7 Language strand: analyzing podcasts and audio storytelling involves considering how sound effects, music, tone of voice, and pacing are used to inform or engage a listening audience.',
  [('Audio storytelling relies on elements such as ___.', ['Sound effects, music, tone of voice, and pacing', 'Only written text with no sound at all', 'A concept unrelated to audio storytelling', 'Photographs and illustrations only'], 0),
   ('A podcast host’s tone of voice can help convey ___.', ['Emotion and emphasis about the topic being discussed', 'Nothing useful to the listener', 'A concept unrelated to tone of voice', 'Only the exact spelling of words being said'], 0),
   ('Why might a podcast use background music during a serious moment?', ['To help set an emotional mood for the listener', 'Music never affects how a listener feels', 'A reason unrelated to audio storytelling', 'Background music always distracts from the story with no purpose'], 0),
   ('Pacing in a podcast refers to ___.', ['The speed and rhythm at which information is delivered', 'The number of speakers involved', 'A concept unrelated to pacing', 'The length of the podcast’s title'], 0),
   ('Why is it important to critically analyze podcasts and other audio media?', ['It helps listeners understand how audio techniques shape their understanding of a topic', 'Audio media never influences how listeners understand a topic', 'A reason unrelated to media literacy', 'Critical analysis is only useful for written texts, not audio'], 0)]),
M('Estimation Strategies and Rounding for Real-World Problems',
  'Grade 7 Math strand: estimation strategies, such as rounding numbers to the nearest ten or hundred, help quickly approximate answers and check whether an exact calculation is reasonable.',
  [('Estimation is useful because it helps ___.', ['Quickly approximate an answer and check if an exact calculation is reasonable', 'Always produce the exact correct answer', 'A concept unrelated to estimation', 'Replace the need for exact calculations entirely'], 0),
   ('Rounded to the nearest ten, 47 becomes ___.', ['50', '40', 'A value unrelated to the calculation', '45'], 0),
   ('Rounded to the nearest hundred, 342 becomes ___.', ['300', '400', 'A value unrelated to the calculation', '350'], 0),
   ('Which situation would benefit most from an estimate rather than an exact answer?', ['Quickly checking if you have enough money for groceries', 'Calculating exact change owed at a cash register', 'A situation unrelated to estimation', 'Recording an exact measurement for a science experiment'], 0),
   ('Why is it useful to estimate before solving a problem exactly?', ['It helps identify whether the final exact answer is reasonable', 'Estimating never helps confirm whether an answer makes sense', 'A reason unrelated to estimation', 'Estimating always gives a more accurate result than exact calculation'], 0)]),
Sc('The Scientific Method: Variables and Designing a Fair Test',
   'Grade 7 Science strand: a fair test changes only one variable at a time while keeping all other conditions constant, allowing scientists to determine the true cause of a result.',
   [('A fair test changes ___.', ['Only one variable at a time', 'Every variable at the same time', 'A concept unrelated to a fair test', 'No variables at all'], 0),
    ('The variable that a scientist deliberately changes in an experiment is called the ___.', ['Independent variable', 'Dependent variable', 'A concept unrelated to experimental variables', 'Constant variable'], 0),
    ('The variable that is measured or observed as a result of an experiment is called the ___.', ['Dependent variable', 'Independent variable', 'A concept unrelated to experimental variables', 'Controlled variable'], 0),
    ('Keeping all other conditions the same during an experiment, except for the one variable being tested, helps ensure ___.', ['The results can be reliably attributed to the variable being tested', 'The experiment will always fail', 'A concept unrelated to fair testing', 'The results will always be inaccurate'], 0),
    ('Why is designing a fair test important in scientific investigations?', ['It allows scientists to determine the true cause of a result with confidence', 'Fair tests never affect the reliability of an experiment’s results', 'A reason unrelated to the scientific method', 'Changing multiple variables at once always produces clearer results'], 0)]),
SS('Fair Trade and Ethical Consumerism',
   'Grade 7 Social Studies strand: fair trade is a movement that aims to ensure producers in developing countries receive fair prices and working conditions, and ethical consumerism involves making purchasing choices based on their social and environmental impact.',
   [('Fair trade aims to ensure that producers in developing countries receive ___.', ['Fair prices and working conditions', 'The lowest possible price for their goods', 'A concept unrelated to fair trade', 'No compensation for their work'], 0),
    ('Ethical consumerism involves making purchasing choices based on ___.', ['A product’s social and environmental impact', 'Only the lowest possible price', 'A concept unrelated to ethical consumerism', 'Random selection with no consideration at all'], 0),
    ('Which of these might be a benefit of buying fair trade products?', ['Supporting better wages and working conditions for producers', 'Guaranteeing the lowest price for consumers', 'A concept unrelated to fair trade products', 'Reducing the quality of products being sold'], 0),
    ('A fair trade certification label on a product is meant to show that ___.', ['The product meets certain standards for fair pricing and labour practices', 'The product was made using child labour', 'A concept unrelated to fair trade certification', 'The product has no connection to its country of origin'], 0),
    ('Why might consumers choose to support fair trade and ethical consumerism?', ['To help promote fairer treatment of workers and more sustainable practices globally', 'Ethical consumerism has no effect on global trade practices', 'A reason unrelated to fair trade', 'Fair trade products always cost less than other products'], 0)])]),
day(77, [
L('Writing: Writing an Interview Script or Q&A Feature',
  'Grade 7 Language strand: an interview script or Q&A feature uses purposeful, open-ended questions to draw out detailed and informative responses from a subject.',
  [('An effective interview question is usually ___.', ['Open-ended, encouraging a detailed response', 'Closed, allowing only a yes or no answer', 'A concept unrelated to interview questions', 'Completely unrelated to the interview’s topic'], 0),
   ('Which is an example of an open-ended interview question?', ['What inspired you to pursue this career?', 'Do you like your job?', 'A question unrelated to open-ended interviewing', 'Are you busy today?'], 0),
   ('Before conducting an interview, it is helpful to ___.', ['Research the subject and prepare thoughtful questions', 'Avoid any preparation at all', 'A concept unrelated to interview preparation', 'Only ask questions the subject suggests'], 0),
   ('A Q&A feature typically presents information in the format of ___.', ['Questions followed by the subject’s direct responses', 'A single continuous paragraph with no structure', 'A concept unrelated to Q&A features', 'A list of unrelated facts with no questions'], 0),
   ('Why are follow-up questions useful during an interview?', ['They allow the interviewer to explore interesting details further', 'Follow-up questions never add useful information', 'A reason unrelated to interviewing', 'Interviews are always more effective with no follow-up questions'], 0)]),
M('Probability: Theoretical vs. Experimental Probability',
  'Grade 7 Math strand: theoretical probability predicts outcomes based on mathematical reasoning, while experimental probability is based on the actual results of repeated trials, and the two may differ.',
  [('Theoretical probability is based on ___.', ['Mathematical reasoning about possible outcomes', 'The actual results of trials that have occurred', 'A concept unrelated to theoretical probability', 'Guessing with no reasoning at all'], 0),
   ('Experimental probability is based on ___.', ['The actual results of repeated trials', 'Mathematical reasoning alone, with no trials', 'A concept unrelated to experimental probability', 'A single guess with no data'], 0),
   ('What is the theoretical probability of rolling a 4 on a fair six-sided die?', ['1/6', '1/4', 'A value unrelated to the calculation', '4/6'], 0),
   ('If a coin is flipped 20 times and lands on heads 13 times, the experimental probability of heads is ___.', ['13/20', '1/2', 'A value unrelated to the calculation', '7/20'], 0),
   ('Why might experimental probability differ from theoretical probability?', ['Random chance can cause actual results to vary from what is mathematically expected', 'Experimental and theoretical probability are always exactly the same', 'A reason unrelated to probability', 'Theoretical probability is always incorrect'], 0)]),
Sc('Renewable Resource Management: Forestry and Fisheries',
   'Grade 7 Science strand: renewable resource management involves practices such as sustainable forestry and fisheries quotas that allow resources like trees and fish populations to replenish over time.',
   [('Renewable resource management aims to ___.', ['Allow resources to replenish over time while still being used', 'Use up resources as quickly as possible', 'A concept unrelated to renewable resource management', 'Prevent any use of natural resources at all'], 0),
    ('Sustainable forestry practices might include ___.', ['Replanting trees after harvesting', 'Removing all trees from a forest with no replanting', 'A concept unrelated to sustainable forestry', 'Avoiding any use of forest resources'], 0),
    ('A fisheries quota is used to ___.', ['Limit the number of fish that can be caught to protect the population', 'Encourage catching as many fish as possible', 'A concept unrelated to fisheries quotas', 'Remove all fish from a body of water at once'], 0),
    ('Why might overfishing be a concern for ocean ecosystems?', ['It can reduce fish populations faster than they can naturally replenish', 'Overfishing has no effect on fish populations', 'A reason unrelated to overfishing', 'Fish populations always grow regardless of how many are caught'], 0),
    ('Why is renewable resource management important for both the environment and the economy?', ['It helps ensure resources like forests and fisheries remain available for future use', 'Resource management has no connection to the environment or economy', 'A reason unrelated to renewable resource management', 'Renewable resources never need to be managed carefully'], 0)]),
SS('The Role of Non-Governmental Organizations (NGOs) in Global Issues',
   'Grade 7 Social Studies strand: non-governmental organizations (NGOs) are independent groups that work to address global issues such as poverty, health, and human rights, often operating without direct government control.',
   [('A non-governmental organization (NGO) is best described as ___.', ['An independent group working to address global issues', 'A branch of a country’s official government', 'A concept unrelated to NGOs', 'A for-profit business with no social mission'], 0),
    ('NGOs often work to address global issues such as ___.', ['Poverty, health, and human rights', 'Only issues within a single company', 'A concept unrelated to the work of NGOs', 'Issues unrelated to communities or people'], 0),
    ('Which of these is an example of what an NGO might do?', ['Provide emergency relief supplies after a natural disaster', 'Pass new laws for a country', 'A concept unrelated to NGO activities', 'Control a country’s military'], 0),
    ('NGOs typically operate ___.', ['Independently, without direct government control', 'As an official part of every national government', 'A concept unrelated to NGOs', 'Only within a single city'], 0),
    ('Why are NGOs important players in addressing global issues?', ['They can mobilize resources and expertise to help communities facing challenges worldwide', 'NGOs have no meaningful impact on global issues', 'A reason unrelated to their role', 'NGOs only operate within one specific country and never globally'], 0)])]),
day(78, [
L('Grammar: Using Correct Verb Tense Consistency',
  'Grade 7 Language strand: verb tense consistency means keeping the same tense throughout a passage unless a shift in time genuinely requires a change, helping avoid confusing readers.',
  [('Verb tense consistency means ___.', ['Keeping the same tense throughout a passage unless a time shift requires a change', 'Using a different tense in every sentence', 'A concept unrelated to verb tense consistency', 'Avoiding verbs altogether in writing'], 0),
   ('Which sentence has a verb tense inconsistency?', ['She walked to the store and buys some milk.', 'She walked to the store and bought some milk.', 'A sentence unrelated to verb tense', 'She walks to the store and buys some milk.'], 0),
   ('If a paragraph is written in the past tense, most verbs should ___.', ['Also be in the past tense', 'Switch randomly to the future tense', 'A concept unrelated to verb tense consistency', 'Be written with no verbs at all'], 0),
   ('Which sentence correctly maintains consistent verb tense?', ['He finished his homework and then watched a movie.', 'He finished his homework and then watches a movie.', 'A sentence unrelated to verb tense consistency', 'He finishes his homework and then watched a movie.'], 0),
   ('Why can inconsistent verb tense confuse a reader?', ['It makes it unclear when the events in a passage are taking place', 'Verb tense never affects how a reader understands a timeline', 'A reason unrelated to grammar', 'Readers always understand a passage the same way regardless of tense'], 0)]),
M('Financial Literacy: Comparing Loan and Savings Options',
  'Grade 7 Math strand: comparing loan and savings options involves evaluating interest rates and terms to determine which option costs less when borrowing or earns more when saving.',
  [('When comparing loans, a lower interest rate generally means ___.', ['Less money paid in interest over time', 'More money paid in interest over time', 'A concept unrelated to comparing loans', 'No difference in the total amount paid'], 0),
   ('When comparing savings accounts, a higher interest rate generally means ___.', ['More money earned over time', 'Less money earned over time', 'A concept unrelated to comparing savings accounts', 'No difference in the total amount earned'], 0),
   ('If Loan A has a 4% interest rate and Loan B has a 7% interest rate on the same amount borrowed, which loan generally costs less overall?', ['Loan A', 'Loan B', 'A choice unrelated to the calculation', 'Both loans cost exactly the same'], 0),
   ('The term of a loan refers to ___.', ['The length of time given to repay it', 'The exact amount of money borrowed', 'A concept unrelated to loan terms', 'The name of the bank offering the loan'], 0),
   ('Why is it important to compare loan and savings options carefully before choosing one?', ['It helps ensure a person pays less in interest or earns more on their savings over time', 'Comparing these options never affects a person’s finances', 'A reason unrelated to financial literacy', 'All loans and savings accounts offer identical terms'], 0)]),
Sc('Weather Instruments and How Meteorologists Forecast',
   'Grade 7 Science strand: meteorologists use instruments such as thermometers, barometers, and anemometers to measure conditions like temperature, air pressure, and wind speed in order to forecast weather.',
   [('A thermometer is used to measure ___.', ['Temperature', 'Air pressure', 'An instrument unrelated to thermometers', 'Wind speed'], 0),
    ('A barometer is used to measure ___.', ['Air pressure', 'Temperature', 'An instrument unrelated to barometers', 'Humidity only'], 0),
    ('An anemometer is used to measure ___.', ['Wind speed', 'Rainfall amounts', 'An instrument unrelated to anemometers', 'Air pressure'], 0),
    ('A sudden drop in air pressure often signals that ___.', ['Stormy weather may be approaching', 'Clear, sunny weather is guaranteed', 'A concept unrelated to air pressure', 'Temperature will remain exactly the same'], 0),
    ('Why do meteorologists rely on multiple instruments to forecast weather?', ['Combining data on temperature, pressure, and wind gives a more accurate picture of upcoming conditions', 'A single instrument always provides a complete and accurate forecast', 'A reason unrelated to weather forecasting', 'Weather instruments provide no useful information for forecasting'], 0)]),
SS('Canada’s Official Languages: French and English Bilingualism',
   'Grade 7 Social Studies strand: Canada’s Official Languages Act, passed in 1969, established French and English as the country’s two official languages, reflecting its history and diverse linguistic heritage.',
   [('Canada’s Official Languages Act established ___ as the country’s official languages.', ['French and English', 'English and Spanish', 'A concept unrelated to Canada’s official languages', 'Only English'], 0),
    ('Canada’s Official Languages Act was passed in ___.', ['1969', '1867', 'A year unrelated to the Official Languages Act', '1929'], 0),
    ('The Official Languages Act reflects Canada’s ___.', ['History and diverse linguistic heritage', 'Complete rejection of its French heritage', 'A concept unrelated to the Official Languages Act', 'Adoption of a single national language only'], 0),
    ('Under the Official Languages Act, federal government services must generally be available in ___.', ['Both French and English', 'Only French', 'A concept unrelated to federal government services', 'Only Indigenous languages'], 0),
    ('Why is Canada’s bilingual policy significant to its national identity?', ['It reflects and protects the country’s dual linguistic heritage', 'Bilingualism has no connection to Canadian identity', 'A reason unrelated to its significance', 'The policy eliminated French as an official language'], 0)])]),
day(79, [
L('Reading: Analyzing Dialogue for Characterization',
  'Grade 7 Language strand: analyzing dialogue for characterization means examining what characters say and how they say it to understand their personality, motivations, and relationships with others.',
  [('Analyzing dialogue for characterization involves examining ___.', ['What characters say and how they say it', 'Only the setting described in a story', 'A concept unrelated to analyzing dialogue', 'The number of paragraphs in a story'], 0),
   ('A character’s word choice in dialogue can reveal ___.', ['Their personality, background, or emotional state', 'Nothing about who the character is', 'A concept unrelated to word choice in dialogue', 'Only the story’s setting'], 0),
   ('Which is an example of using dialogue to show a character’s personality?', ['A character speaking sharply and interrupting others often', 'A narrator describing the weather in detail', 'A concept unrelated to characterization through dialogue', 'A list of a character’s physical features'], 0),
   ('Dialogue tags, such as she whispered or he shouted, can help readers understand ___.', ['The tone or emotion behind a character’s words', 'The setting of the story', 'A concept unrelated to dialogue tags', 'The story’s overall theme'], 0),
   ('Why might an author give two characters noticeably different speech patterns?', ['To help distinguish their personalities and make them feel distinct', 'Speech patterns never affect how readers view a character', 'A reason unrelated to characterization', 'All characters in a story should sound exactly alike'], 0)]),
M('Complementary, Supplementary, and Vertical Angle Pairs',
  'Grade 7 Math strand: complementary angles add up to 90 degrees, supplementary angles add up to 180 degrees, and vertical angles, formed by intersecting lines, are always equal to each other.',
  [('Complementary angles add up to ___.', ['90 degrees', '180 degrees', 'A value unrelated to complementary angles', '360 degrees'], 0),
   ('Supplementary angles add up to ___.', ['180 degrees', '90 degrees', 'A value unrelated to supplementary angles', '45 degrees'], 0),
   ('Vertical angles, formed when two lines intersect, are always ___.', ['Equal to each other', 'Supplementary to each other', 'A concept unrelated to vertical angles', 'Complementary to each other'], 0),
   ('If one angle measures 35 degrees, its complementary angle measures ___.', ['55 degrees', '65 degrees', 'A value unrelated to the calculation', '145 degrees'], 0),
   ('Why are vertical angles always equal when two lines intersect?', ['They are formed by the same pair of intersecting lines and share the same angle measure by geometric definition', 'Vertical angles are only sometimes equal, depending on the shape', 'A reason unrelated to vertical angles', 'Vertical angles are always supplementary instead of equal'], 0)]),
Sc('Friction and Its Effects on Motion',
   'Grade 7 Science strand: friction is a force that opposes motion between two surfaces in contact, slowing down or preventing movement depending on how rough or smooth the surfaces are.',
   [('Friction is a force that ___.', ['Opposes motion between two surfaces in contact', 'Always speeds up motion between two surfaces', 'A concept unrelated to friction', 'Has no effect on moving objects'], 0),
    ('Rougher surfaces generally produce ___ friction than smoother surfaces.', ['More', 'Less', 'A concept unrelated to friction', 'The exact same amount of'], 0),
    ('Which of these would likely produce the least friction?', ['A smooth ice surface', 'A rough gravel surface', 'A surface unrelated to this comparison', 'Sandpaper'], 0),
    ('Why do cars use brakes that rely on friction?', ['Friction between the brake pads and wheels helps slow the car down', 'Friction has no effect on a car’s ability to slow down', 'A reason unrelated to friction', 'Brakes work by eliminating all friction on the road'], 0),
    ('Why might engineers try to reduce friction in machines with moving parts?', ['Reducing friction can decrease wear and improve the machine’s efficiency', 'Reducing friction always makes a machine less efficient', 'A reason unrelated to friction', 'Friction has no effect on how machines wear over time'], 0)]),
SS('The Manhattan Project and the Dawn of the Nuclear Age',
   'Grade 7 Social Studies strand: the Manhattan Project was a major scientific and military effort during World War II that developed the first nuclear weapons, marking the beginning of the nuclear age and changing global politics.',
   [('The Manhattan Project was a major effort during World War II to develop ___.', ['The first nuclear weapons', 'The first commercial airplanes', 'A concept unrelated to the Manhattan Project', 'A new global trade agreement'], 0),
    ('The Manhattan Project involved cooperation between ___.', ['Scientists, engineers, and government officials', 'Only a single individual working alone', 'A concept unrelated to the Manhattan Project', 'Groups with no scientific expertise at all'], 0),
    ('The completion of the Manhattan Project marked the beginning of ___.', ['The nuclear age', 'The end of all international conflict', 'A concept unrelated to the Manhattan Project', 'A period with no further scientific development'], 0),
    ('The development of nuclear weapons significantly changed ___.', ['Global politics and international relations', 'Nothing about international relations', 'A concept unrelated to the Manhattan Project’s impact', 'Only local weather patterns'], 0),
    ('Why do historians consider the Manhattan Project a turning point in world history?', ['It introduced a powerful new technology that reshaped global politics and security for decades', 'The Manhattan Project had no lasting effect on world history', 'A reason unrelated to its historical significance', 'The technology developed was never used or referenced again'], 0)])]),
day(80, [
L('Review: Language Skills (Days 71-79)',
  'Grade 7 Language strand: this review lesson revisits key ideas from Days 71-79, including point of view, plot arcs, pronoun-antecedent agreement, cause and effect, and interview writing.',
  [('A first-person narrator tells a story using ___.', ['Pronouns such as I and we', 'Only third-person pronouns like he and she', 'A concept unrelated to point of view', 'No pronouns of any kind'], 0),
   ('An antecedent is ___.', ['The noun that a pronoun refers back to', 'A type of punctuation mark', 'A concept unrelated to antecedents', 'A verb tense used in formal writing'], 0),
   ('A cause-and-effect relationship shows how ___.', ['One event leads directly to a result', 'Two unrelated events happen at the same time', 'A concept unrelated to cause and effect', 'A story’s setting connects to its characters'], 0),
   ('An effective interview question is usually ___.', ['Open-ended, encouraging a detailed response', 'Closed, allowing only a yes or no answer', 'A concept unrelated to interview questions', 'Completely unrelated to the interview’s topic'], 0),
   ('Why is it useful to review point of view, grammar, cause and effect, and interview writing together?', ['It reinforces how these language skills support clear reading and writing across different formats', 'These skills have no connection to each other', 'A reason unrelated to reviewing language skills', 'Review never helps strengthen understanding of language'], 0)]),
M('Review: Math Skills (Days 71-79)',
  'Grade 7 Math strand: this review lesson revisits key ideas from Days 71-79, including circle graphs, the Cartesian plane, stem-and-leaf plots, and theoretical probability.',
  [('A circle graph represents data using ___.', ['Proportional slices of a circle', 'A single straight line', 'A concept unrelated to circle graphs', 'A grid of individual dots'], 0),
   ('The Cartesian plane is divided into ___ quadrants.', ['Four', 'Two', 'A number unrelated to the Cartesian plane', 'Eight'], 0),
   ('In a stem-and-leaf plot, the “stem” usually represents ___.', ['The leading digit or digits of a value', 'The final digit of a value', 'A concept unrelated to stem-and-leaf plots', 'The total number of data points'], 0),
   ('Theoretical probability is based on ___.', ['Mathematical reasoning about possible outcomes', 'The actual results of trials that have occurred', 'A concept unrelated to theoretical probability', 'Guessing with no reasoning at all'], 0),
   ('Why is it useful to review data displays, coordinate geometry, probability, and financial literacy together?', ['It reinforces how these math concepts connect and apply to real-world situations', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of math'], 0)]),
Sc('Review: Science Skills (Days 71-79)',
   'Grade 7 Science strand: this review lesson revisits key ideas from Days 71-79, including atoms and elements, light reflection, ocean currents, and renewable resource management.',
   [('An atom is ___.', ['The basic building block of matter', 'A mixture of two or more substances', 'A concept unrelated to atoms', 'A type of chemical reaction'], 0),
    ('Reflection occurs when ___.', ['Light bounces off a surface', 'Light bends as it passes through a new material', 'A concept unrelated to reflection', 'Light is completely absorbed by a surface'], 0),
    ('Ocean currents are large-scale movements of ___.', ['Seawater', 'Only surface ice', 'A concept unrelated to ocean currents', 'Underground freshwater'], 0),
    ('Renewable resource management aims to ___.', ['Allow resources to replenish over time while still being used', 'Use up resources as quickly as possible', 'A concept unrelated to renewable resource management', 'Prevent any use of natural resources at all'], 0),
    ('Why is it useful to review matter, light, Earth systems, and resource management together?', ['It reinforces how these interconnected science concepts help explain the natural world', 'These topics have no connection to each other', 'A reason unrelated to reviewing science', 'Review is never useful in science'], 0)]),
SS('Review: Social Studies Skills (Days 71-79)',
   'Grade 7 Social Studies strand: this review lesson revisits key ideas from Days 71-79, including the Acadian Expulsion, the Persons Case, population pyramids, and non-governmental organizations.',
   [('The Acadian Expulsion involved the forced removal of ___.', ['Thousands of Acadian settlers from their homes', 'A small group of British soldiers', 'A concept unrelated to the Acadian Expulsion', 'No people at all'], 0),
    ('The Persons Case was a legal ruling that recognized women as ___.', ['“Persons” eligible to serve in the Canadian Senate', 'Ineligible for any political involvement', 'A concept unrelated to the Persons Case', 'Persons only for the purpose of paying taxes'], 0),
    ('A population pyramid displays a population’s distribution by ___.', ['Age and sex', 'Income level only', 'A concept unrelated to population pyramids', 'Favourite occupations'], 0),
    ('A non-governmental organization (NGO) is best described as ___.', ['An independent group working to address global issues', 'A branch of a country’s official government', 'A concept unrelated to NGOs', 'A for-profit business with no social mission'], 0),
    ('Why is it useful to review Canadian history, women’s rights, demographics, and global organizations together?', ['It reinforces how these interconnected historical and civic topics shape Canadian and global society', 'These topics have no connection to one another', 'A reason unrelated to reviewing social studies', 'Review is never useful when studying history and demographics'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260905):
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
    _rebalance_answer_positions(g7_71_80)
    append_to(7, g7_71_80)
