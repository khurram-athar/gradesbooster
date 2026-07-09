#!/usr/bin/env python3
"""Phase 3: Grade 10, Days 41-50 (second Grade 10 batch). Topics chosen
to avoid any overlap with the existing Day 1-40 set (see
data/grade10.json): irony/symbolism, dystopian fiction, satire,
logarithms, vectors, standard deviation, titration, electric circuits,
plate tectonics, stoichiometry, and 20th-century Canadian history not
yet covered (Winnipeg General Strike, the Persons Case, October Crisis,
founding of Nunavut, the Oka Crisis, Canada and the UN).

Subject keys for Grade 10 are "English" and "History" (confirmed via
data/grade10.ts), same as gen_grade10_days31_40.py.

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option
text; apostrophes use the curly Unicode form (’).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


g10_41_50 = [
day(41, [
E('Reading: Irony and Symbolism in Fiction',
  'Grade 10 English strand: irony occurs when there is a contrast between expectation and reality, and symbolism uses objects or images to represent deeper ideas beyond their literal meaning.',
  [('Irony occurs when there is a contrast between ___.', ['Expectation and reality', 'Two identical, unrelated events', 'A character’s name and their age', 'A story’s setting and its length'], 0),
   ('Symbolism uses objects or images to represent ___.', ['Deeper ideas beyond their literal meaning', 'Only their literal, surface-level meaning', 'Nothing beyond their physical description', 'A concept unrelated to meaning'], 0),
   ('Which is an example of situational irony?', ['A fire station burning down', 'A firefighter putting out a fire', 'A character predicting an outcome that then happens exactly as expected', 'An event with no unexpected outcome at all'], 0),
   ('Why might an author use symbolism instead of stating an idea directly?', ['It can add layers of meaning and invite deeper reader interpretation', 'Symbolism always makes a story’s meaning less clear to readers', 'Authors use symbolism to avoid having any meaning at all', 'Direct statements are always more effective than symbolic ones'], 0),
   ('Why is recognizing irony important when analyzing a text?', ['It can reveal deeper commentary the author is making about a situation or character', 'Irony has no connection to an author’s intended meaning', 'Recognizing irony never affects how a text is interpreted', 'Ironic moments never carry any additional meaning'], 0)]),
M('Introduction to Logarithms',
  'Grade 10 Functions strand (extension): a logarithm answers the question of what exponent a given base must be raised to in order to produce a certain number, making it the inverse operation of exponentiation.',
  [('A logarithm answers the question of ___.', ['What exponent a base must be raised to in order to produce a given number', 'What number multiplied by itself equals zero', 'What the sum of two numbers equals', 'A question unrelated to exponents'], 0),
   ('A logarithm is the inverse operation of ___.', ['Exponentiation', 'Addition', 'Subtraction', 'An operation unrelated to exponents'], 0),
   ('If log base 2 of 8 equals 3, this means ___.', ['2 raised to the power of 3 equals 8', '2 multiplied by 3 equals 8', '8 divided by 2 equals 3', 'A relationship unrelated to exponents'], 0),
   ('Why might logarithms be useful for solving equations where the unknown is an exponent?', ['They allow you to isolate and directly solve for that exponent', 'Logarithms can never be used to solve for an exponent', 'This type of equation cannot be solved using any method', 'Logarithms only apply to equations with no exponents'], 0),
   ('Why are logarithms useful in fields like science for measuring things like earthquake intensity (the Richter scale)?', ['They can effectively represent very large ranges of values on a more manageable scale', 'Logarithms have no real-world scientific applications', 'This concept only applies to purely abstract mathematics', 'Logarithms make large values impossible to measure or compare'], 0)]),
Sc('Chemistry: Titration and Quantitative Analysis',
   'Grade 10 Chemistry strand: titration is a laboratory technique used to determine the concentration of an unknown solution by carefully reacting it with a solution of known concentration.',
   [('Titration is used to determine ___.', ['The concentration of an unknown solution', 'The colour of a solution only', 'The temperature of a solution only', 'A property unrelated to concentration'], 0),
    ('During a titration, a solution of known concentration is used to react with ___.', ['A solution of unknown concentration', 'Another solution of exactly the same known concentration', 'A solid with no connection to the reaction', 'A gas unrelated to the titration process'], 0),
    ('Why is titration considered a form of quantitative analysis?', ['It provides precise, measurable data about a solution’s concentration', 'Titration provides no measurable or precise data', 'This technique has no connection to quantitative measurement', 'Quantitative analysis never involves laboratory techniques like titration'], 0),
    ('Which tool is commonly used to carefully add a measured volume of solution during a titration?', ['A burette', 'A thermometer', 'A microscope', 'A tool unrelated to measuring volume'], 0),
    ('Why is titration considered a valuable skill in fields like pharmaceuticals or environmental testing?', ['Accurately determining concentration is essential for safety and quality in these fields', 'Titration has no practical use outside of a classroom setting', 'These fields never require precise concentration measurements', 'This technique has no connection to real-world applications'], 0)]),
H('Canada’s Role in the United Nations',
  'Grade 10 History strand: Canada has been a member of the United Nations since its founding in 1945, contributing to international peacekeeping, diplomacy, and humanitarian efforts through the organization.',
  [('The United Nations was founded in which year?', ['1945', '1919', '1867', '1989'], 0),
   ('Through the United Nations, Canada has contributed to ___.', ['International peacekeeping, diplomacy, and humanitarian efforts', 'No international efforts of any kind', 'Only domestic policy, with no international connection', 'A topic entirely unrelated to Canadian foreign policy'], 0),
   ('Why might a country choose to actively participate in an organization like the United Nations?', ['To collaborate with other nations on global issues like peace, security, and human rights', 'Participation in the UN provides no benefit to member countries', 'The United Nations has no connection to international cooperation', 'Countries gain nothing from engaging in diplomacy'], 0),
   ('Why is studying Canada’s involvement in the United Nations relevant to understanding its foreign policy?', ['It illustrates how Canada engages with global governance and international cooperation', 'Canada has no involvement with the United Nations', 'This topic has no connection to Canadian foreign policy', 'The United Nations has no role in shaping international relations'], 0),
   ('Which is an example of an area the United Nations works on?', ['Human rights and humanitarian aid', 'A topic entirely unrelated to global cooperation', 'Only issues within a single member country', 'An area with no international scope at all'], 0)])]),

day(42, [
E('Writing: The Persuasive Op-Ed',
  'Grade 10 English strand: an op-ed is a persuasive opinion piece that presents a clear argument on a current issue, supported by evidence and a compelling, direct writing style.',
  [('An op-ed is best described as ___.', ['A persuasive opinion piece on a current issue', 'A completely neutral summary with no opinion', 'A piece of writing unrelated to current issues', 'A purely factual report with no argument'], 0),
   ('Why should an op-ed include supporting evidence for its argument?', ['Evidence strengthens the credibility and persuasiveness of the argument', 'Evidence is unnecessary in this type of writing', 'An op-ed should never include any supporting evidence', 'Evidence always weakens a persuasive argument'], 0),
   ('Why might an op-ed use a direct, compelling writing style?', ['It helps effectively capture and hold the reader’s attention while making the argument', 'A direct writing style always weakens an op-ed’s argument', 'Op-eds are never written with a persuasive purpose', 'This style has no effect on how convincing the writing is'], 0),
   ('Which is an example of an appropriate topic for an op-ed?', ['A current, debatable issue affecting the community or society', 'A topic with no connection to any real issue', 'A purely factual, non-debatable topic', 'A subject with no relevance to readers at all'], 0),
   ('Why is it useful to consider counterarguments when writing an op-ed?', ['Addressing counterarguments can strengthen the overall persuasiveness of the piece', 'Counterarguments should never be mentioned in an op-ed', 'Considering opposing views always weakens an argument', 'Op-eds should ignore any perspective other than the writer’s own'], 0)]),
M('Logarithmic Functions and Their Graphs',
  'Grade 10 Functions strand (extension): a logarithmic function is the inverse of an exponential function, and its graph increases slowly and has a vertical asymptote at x equals zero.',
  [('A logarithmic function is the inverse of ___.', ['An exponential function', 'A linear function', 'A quadratic function', 'A function unrelated to exponents'], 0),
   ('The graph of a basic logarithmic function has a vertical asymptote at ___.', ['x equals zero', 'y equals zero', 'x equals one', 'A point unrelated to the origin'], 0),
   ('Compared to an exponential function, a logarithmic function’s graph tends to increase ___.', ['More slowly', 'At an identical rate', 'More quickly at every point', 'In a completely unpredictable way'], 0),
   ('Why is it useful to understand that logarithmic and exponential functions are inverses of one another?', ['It helps in converting between exponential and logarithmic forms when solving problems', 'These two function types have no mathematical relationship', 'Inverse functions have no practical use in mathematics', 'Exponential and logarithmic functions can never be related to each other'], 0),
   ('Why might a logarithmic scale be used on a graph representing a wide range of values?', ['It can make it easier to visually compare values that span several orders of magnitude', 'Logarithmic scales make data harder to interpret in every situation', 'This type of scale has no practical use for representing data', 'Logarithmic graphs can never represent a wide range of values'], 0)]),
Sc('Physics: Electric Circuits and Ohm’s Law',
   'Grade 10 Physics strand: Ohm’s Law describes the relationship between voltage, current, and resistance in an electric circuit, stating that voltage equals current multiplied by resistance.',
   [('Ohm’s Law describes the relationship between ___.', ['Voltage, current, and resistance', 'Only temperature and pressure', 'A relationship unrelated to electricity', 'Only mass and volume'], 0),
    ('According to Ohm’s Law, voltage equals ___.', ['Current multiplied by resistance', 'Current divided by resistance', 'Resistance minus current', 'A value unrelated to current or resistance'], 0),
    ('If resistance in a circuit increases while voltage stays the same, current will generally ___.', ['Decrease', 'Increase', 'Remain completely unchanged', 'Become impossible to determine'], 0),
    ('Why is Ohm’s Law useful for designing electrical circuits?', ['It allows engineers to predict and control the relationship between voltage, current, and resistance', 'Ohm’s Law has no practical application to circuit design', 'This law only applies to circuits with no electrical components', 'Electrical circuits never follow a predictable mathematical relationship'], 0),
    ('Which is an example of a component that adds resistance in a circuit?', ['A resistor', 'A wire with no resistance at all', 'A component unrelated to electrical circuits', 'An object that always increases current with no limit'], 0)]),
H('The Winnipeg General Strike and Labour Movements',
  'Grade 10 History strand: the 1919 Winnipeg General Strike was a major labour action in which workers demanded better wages and working conditions, becoming a landmark event in Canadian labour history.',
  [('The Winnipeg General Strike took place in which year?', ['1919', '1867', '1945', '1995'], 0),
   ('Workers involved in the Winnipeg General Strike were primarily demanding ___.', ['Better wages and working conditions', 'No specific changes at all', 'A topic entirely unrelated to labour rights', 'Reduced access to any workplace rights'], 0),
   ('Why is the Winnipeg General Strike considered a landmark event in Canadian labour history?', ['It represented a significant, large-scale action by workers demanding change', 'This event had no impact on Canadian labour history', 'The strike never actually involved any workers', 'This event has no connection to labour rights'], 0),
   ('Why might studying labour movements like the Winnipeg General Strike help explain later workplace protections in Canada?', ['These movements often contributed to public and political pressure for improved labour laws', 'Labour movements have no connection to later workplace protections', 'Workplace protections in Canada developed with no historical influence at all', 'This topic has no relevance to understanding Canadian labour law'], 0),
   ('A general strike, in this context, refers to ___.', ['A strike involving workers across many different industries or sectors', 'A strike involving only a single worker', 'An event unrelated to labour action', 'A strike that occurs with no organized workers involved'], 0)])]),

day(43, [
E('Literature: Dystopian Fiction and Social Commentary',
  'Grade 10 English strand: dystopian fiction imagines a troubled future society, often used by authors to comment critically on real-world social, political, or technological issues.',
  [('Dystopian fiction typically imagines ___.', ['A troubled future society', 'A perfect, conflict-free society', 'A setting with no connection to society at all', 'Only historical events with no future elements'], 0),
   ('Authors often use dystopian fiction to ___.', ['Comment critically on real-world social, political, or technological issues', 'Avoid any connection to real-world issues', 'Focus only on entertainment with no deeper message', 'Describe a setting with no relevance to readers’ lives'], 0),
   ('Which is a common theme explored in dystopian fiction?', ['The dangers of unchecked government or corporate power', 'A theme entirely unrelated to society or power', 'Only lighthearted, comedic subject matter', 'A topic unrelated to any real-world concern'], 0),
   ('Why might readers find dystopian fiction relevant to understanding current events?', ['It can reflect or exaggerate real societal concerns, prompting reflection', 'Dystopian fiction has no connection to real-world issues', 'This genre never engages with current or historical events', 'Readers gain no insight from this type of fiction'], 0),
   ('Why is social commentary an important element of many dystopian novels?', ['It allows authors to critique real issues through a fictional lens', 'Social commentary has no place in dystopian fiction', 'Dystopian novels never comment on real-world issues', 'This element removes all meaning from the story'], 0)]),
M('Standard Deviation and Normal Distribution',
  'Grade 10 Data Management strand: standard deviation measures how spread out data values are from the mean, and a normal distribution is a common, symmetric bell-shaped pattern seen in many data sets.',
  [('Standard deviation measures ___.', ['How spread out data values are from the mean', 'The exact total sum of all data values', 'The single highest value in a data set', 'A value unrelated to how data is spread'], 0),
   ('A normal distribution is typically described as having a ___ shape.', ['Symmetric, bell-shaped', 'Perfectly flat, with no variation', 'Random, with no discernible pattern', 'A shape unrelated to data distribution'], 0),
   ('A low standard deviation suggests that data values are ___.', ['Clustered closely around the mean', 'Spread very far apart from the mean', 'Completely unrelated to the mean', 'Impossible to measure accurately'], 0),
   ('Why is standard deviation a useful measure alongside the mean of a data set?', ['It provides additional context about how consistent or variable the data actually is', 'Standard deviation provides no additional useful information', 'The mean alone always fully describes a data set', 'This measure has no connection to interpreting data'], 0),
   ('Why might understanding normal distribution be useful in fields like standardized testing?', ['It helps interpret how an individual score compares to the overall distribution of scores', 'Normal distribution has no connection to interpreting test results', 'Standardized testing never involves any statistical analysis', 'This concept only applies to purely theoretical mathematics'], 0)]),
Sc('Biology: Population Ecology and Carrying Capacity',
   'Grade 10 Biology strand: population ecology studies how populations of organisms grow and interact with their environment, and carrying capacity refers to the maximum population size an environment can sustainably support.',
   [('Population ecology studies how populations ___.', ['Grow and interact with their environment', 'Have no connection to their environment', 'Remain completely unaffected by environmental factors', 'A field unrelated to living organisms'], 0),
    ('Carrying capacity refers to ___.', ['The maximum population size an environment can sustainably support', 'The minimum population size required for a species to exist', 'A concept unrelated to population size', 'An unlimited population size with no environmental constraints'], 0),
    ('Which factor might limit a population’s growth and contribute to its carrying capacity?', ['Availability of food and resources', 'A factor entirely unrelated to survival needs', 'The colour of the organisms in the population', 'A factor with no connection to the environment'], 0),
    ('Why might a population decline if it exceeds its environment’s carrying capacity?', ['Resources may become insufficient to support all individuals in the population', 'Exceeding carrying capacity always has no effect on a population', 'Populations can grow indefinitely with no environmental limits', 'This concept has no connection to resource availability'], 0),
    ('Why is understanding carrying capacity important for wildlife management and conservation?', ['It helps guide decisions to maintain sustainable population levels in an ecosystem', 'This concept has no relevance to conservation efforts', 'Wildlife management never considers population size', 'Carrying capacity has no connection to ecosystem health'], 0)]),
H('Women’s Suffrage and the Persons Case',
  'Grade 10 History strand: the Persons Case was a 1929 legal decision that established that women were considered “persons” under Canadian law and eligible for appointment to the Senate, a milestone in the fight for women’s rights.',
  [('The Persons Case was decided in which year?', ['1929', '1867', '1945', '1995'], 0),
   ('The Persons Case established that women were considered ___.', ['“Persons” under Canadian law, eligible for Senate appointment', 'Ineligible for any legal recognition under Canadian law', 'Excluded from all forms of public office', 'A group with no connection to Canadian legal history'], 0),
   ('Why is the Persons Case considered a milestone in the fight for women’s rights in Canada?', ['It legally recognized women’s eligibility for positions previously restricted to men', 'This case had no effect on women’s legal rights', 'The Persons Case reduced legal rights for women', 'This event has no connection to Canadian women’s history'], 0),
   ('The women who brought forward the Persons Case are sometimes referred to as ___.', ['The Famous Five', 'A group with no historical name', 'The Suffrage Six', 'A group unrelated to this case'], 0),
   ('Why might historians connect the Persons Case to the broader women’s suffrage movement?', ['Both reflect efforts to expand women’s legal rights and participation in public life', 'These two topics have no historical connection', 'The women’s suffrage movement had no connection to legal rights', 'The Persons Case occurred with no connection to women’s rights history'], 0)])]),

day(44, [
E('Media Studies: Analyzing News Broadcasts',
  'Grade 10 English strand: analyzing a news broadcast involves examining how visual presentation, tone, word choice, and story selection can shape audience perception of an event.',
  [('Analyzing a news broadcast involves examining how ___.', ['Visual presentation, tone, word choice, and story selection shape audience perception', 'Only the length of the broadcast affects audience perception', 'News broadcasts have no influence on audience perception', 'A factor entirely unrelated to media presentation'], 0),
   ('Why might the specific word choice used in a news report influence how a viewer perceives an event?', ['Certain words can carry emotional or connotative weight that shapes interpretation', 'Word choice has no effect on how information is perceived', 'All words used in news reports carry an identical, neutral meaning', 'This factor is irrelevant to media analysis'], 0),
   ('Why is story selection an important consideration when analyzing a news broadcast?', ['Which stories are chosen to be covered can shape what audiences see as important', 'Story selection has no effect on audience perception', 'All news broadcasts cover the exact same stories', 'This factor has no connection to media literacy'], 0),
   ('Which is an example of a visual element that might influence how a news story is perceived?', ['The choice of images or footage shown alongside the story', 'The exact time of day the broadcast airs', 'A factor entirely unrelated to visual presentation', 'The physical location of the television station'], 0),
   ('Why is developing skills to critically analyze news broadcasts considered an important media literacy skill?', ['It helps viewers recognize how media choices can shape understanding of events', 'Critical analysis of news has no value for media literacy', 'News broadcasts require no critical evaluation from viewers', 'This skill has no connection to understanding current events'], 0)]),
M('Vectors in Two Dimensions',
  'Grade 10 Geometry strand (extension): a vector represents a quantity with both magnitude and direction, often used to describe things like velocity or force in two-dimensional space.',
  [('A vector represents a quantity with ___.', ['Both magnitude and direction', 'Only magnitude, with no direction', 'Only direction, with no magnitude', 'Neither magnitude nor direction'], 0),
   ('Which is an example of a quantity that could be represented as a vector?', ['Velocity', 'Temperature', 'Mass', 'A quantity unrelated to direction'], 0),
   ('Why is direction an important component when representing a vector, unlike a plain number (scalar)?', ['It provides essential information about which way a quantity is acting, not just how much', 'Direction has no relevance to how a vector is used', 'Vectors never involve any directional component', 'A scalar and a vector are always identical to one another'], 0),
   ('In two-dimensional space, a vector can be described using ___.', ['Horizontal and vertical components', 'Only a single number with no components', 'A description unrelated to direction or magnitude', 'Three components instead of two'], 0),
   ('Why might vectors be useful for describing forces acting on an object in physics?', ['Multiple forces with different directions can be combined and analyzed using vector operations', 'Vectors have no practical use for describing physical forces', 'Forces never have a specific direction associated with them', 'This concept only applies to purely abstract mathematics'], 0)]),
Sc('Earth Science: Plate Tectonics and Natural Hazards',
   'Grade 10 Earth Science strand: plate tectonics describes the movement of large sections of Earth’s crust, which can result in natural hazards such as earthquakes and volcanic eruptions at plate boundaries.',
   [('Plate tectonics describes the movement of ___.', ['Large sections of Earth’s crust', 'Only ocean currents, with no connection to the crust', 'A concept unrelated to Earth’s structure', 'Only the atmosphere, with no connection to the crust'], 0),
    ('Which natural hazard is commonly associated with plate boundaries?', ['Earthquakes', 'Tornadoes', 'Blizzards', 'A hazard unrelated to Earth’s crust'], 0),
    ('Why do earthquakes often occur along plate boundaries?', ['Stress builds up as plates interact, and its release causes the ground to shake', 'Earthquakes occur completely randomly with no connection to plate boundaries', 'Plate boundaries have no relationship to earthquake activity', 'This hazard has no scientific explanation'], 0),
    ('Volcanic eruptions are often associated with ___.', ['Certain types of plate boundaries where magma can reach the surface', 'Locations with no connection to plate tectonics', 'A process entirely unrelated to Earth’s crust', 'Areas with no geological activity at all'], 0),
    ('Why is studying plate tectonics important for understanding and preparing for natural hazards?', ['It helps identify regions at higher risk, informing safety and preparedness efforts', 'Plate tectonics has no connection to natural hazards', 'This field of study provides no useful information for hazard preparedness', 'Natural hazards occur with no connection to geological activity'], 0)]),
H('The October Crisis and the War Measures Act',
  'Grade 10 History strand: the 1970 October Crisis, involving kidnappings by the FLQ in Quebec, led the federal government to invoke the War Measures Act, a controversial decision that expanded government powers.',
  [('The October Crisis took place in which year?', ['1970', '1919', '1945', '1995'], 0),
   ('The October Crisis involved kidnappings carried out by ___.', ['The FLQ', 'A group with no connection to Quebec history', 'A foreign military force', 'An organization unrelated to Canadian politics'], 0),
   ('In response to the October Crisis, the federal government invoked ___.', ['The War Measures Act', 'No formal legal or political action', 'A law unrelated to public safety', 'An act with no connection to expanded government powers'], 0),
   ('Why is the government’s use of the War Measures Act during the October Crisis considered controversial?', ['It significantly expanded government powers, raising concerns about civil liberties', 'This decision had no effect on government powers or civil liberties', 'The War Measures Act was never actually invoked', 'This action was universally supported with no debate or controversy'], 0),
   ('Why do historians continue to study the October Crisis today?', ['It raises important questions about balancing security and civil liberties during a crisis', 'This event has no lasting historical significance', 'The October Crisis has no connection to Canadian political history', 'This topic has no relevance to understanding Canadian civil liberties'], 0)])]),

day(45, [
E('Grammar: Parallel Structure and Sentence Variety',
  'Grade 10 English strand: parallel structure ensures that items in a list or series use a consistent grammatical form, while sentence variety involves using different sentence lengths and structures to improve writing flow.',
  [('Parallel structure ensures that items in a list use ___.', ['A consistent grammatical form', 'Completely inconsistent grammatical forms', 'Only single-word items, with no other structure allowed', 'No specific grammatical pattern at all'], 0),
   ('Which sentence demonstrates correct parallel structure?', ['She enjoys reading, writing, and hiking.', 'She enjoys reading, writing, and to hike.', 'She enjoys to read, writing, and hiking.', 'She enjoys reading, to write, and hiking.'], 0),
   ('Sentence variety involves using ___.', ['Different sentence lengths and structures', 'Only one single sentence length throughout a piece of writing', 'No variation in sentence structure at all', 'A concept unrelated to sentence construction'], 0),
   ('Why might a writer use sentence variety in a piece of writing?', ['It can improve the flow and keep the reader engaged', 'Sentence variety always makes writing harder to understand', 'Using varied sentence structures has no effect on writing quality', 'Writers should always use identical sentence structures throughout'], 0),
   ('Why is parallel structure important for clarity in writing?', ['Inconsistent structure in a list or series can be confusing or awkward to read', 'Parallel structure has no effect on how clearly a sentence reads', 'Grammatical consistency in a list is never important', 'This concept only applies to very short pieces of writing'], 0)]),
M('Combining Functions: Sum, Difference, and Composite',
  'Grade 10 Functions strand: functions can be combined through addition, subtraction, or composition, where the composite of two functions applies one function to the result of another.',
  [('The sum of two functions is found by ___.', ['Adding their outputs together for a given input', 'Multiplying their outputs together', 'Subtracting one function’s output from the other', 'A method unrelated to combining outputs'], 0),
   ('A composite function applies ___.', ['One function to the result of another function', 'Two completely unrelated, separate functions with no connection', 'Only a single function, with no combination involved', 'A method unrelated to functions'], 0),
   ('If f(x) = x + 2 and g(x) = 3x, what is f(g(x))?', ['3x + 2', 'x + 5', '3x - 2', '6x'], 0),
   ('Why might combining functions be useful for modelling a real-world situation with multiple related processes?', ['It allows a single expression to represent how multiple processes affect an outcome together', 'Combining functions has no useful real-world application', 'Real-world situations never involve more than one mathematical process', 'This concept only applies to purely abstract mathematics with no real-world use'], 0),
   ('Why is the order of functions important when finding a composite function?', ['Changing the order can produce a different result, since one function’s output becomes the other’s input', 'The order of functions never affects the result of a composite function', 'Composite functions can only be calculated in one specific, fixed order', 'This concept has no connection to how composite functions are calculated'], 0)]),
Sc('Chemistry: Organic Compounds and Functional Groups',
   'Grade 10 Chemistry strand: organic compounds are carbon-based molecules, and functional groups are specific arrangements of atoms within these molecules that determine their chemical properties and reactivity.',
   [('Organic compounds are best described as ___.', ['Carbon-based molecules', 'Molecules that contain no carbon at all', 'A category unrelated to chemistry', 'Only inorganic minerals'], 0),
    ('A functional group is best described as ___.', ['A specific arrangement of atoms that determines a molecule’s chemical properties', 'A group of unrelated molecules with no shared structure', 'A concept unrelated to chemical structure', 'A term with no connection to reactivity'], 0),
    ('Why do different functional groups give organic compounds different chemical properties?', ['The specific arrangement of atoms in a functional group influences how a molecule reacts', 'Functional groups have no effect on a molecule’s properties', 'All organic compounds behave in an identical way regardless of structure', 'This concept has no connection to chemical reactivity'], 0),
    ('Which is an example of an organic compound found in everyday life?', ['A sugar molecule', 'A pure metal with no carbon content', 'A substance entirely unrelated to carbon chemistry', 'A mineral with no organic origin'], 0),
    ('Why is the study of organic compounds and functional groups important in fields like medicine?', ['Many medications are organic compounds whose function depends on specific functional groups', 'Organic chemistry has no connection to medicine', 'Functional groups have no relevance to how medications work', 'This field of study has no practical, real-world applications'], 0)]),
H('Canada’s Space and Technology Achievements',
  'Grade 10 History strand: Canada has made significant contributions to space and technology, including the development of the Canadarm and Canadian astronauts’ participation in international space missions.',
  [('The Canadarm is a notable Canadian contribution to ___.', ['Space technology', 'A field entirely unrelated to technology', 'Only domestic transportation, with no connection to space', 'A topic unrelated to Canadian achievements'], 0),
   ('Canadian astronauts have participated in ___.', ['International space missions', 'No missions of any kind', 'Only missions unrelated to space exploration', 'A field with no connection to Canadian achievements'], 0),
   ('Why might a country’s achievements in space and technology be a significant point of national pride?', ['They can demonstrate scientific capability and international collaboration', 'These achievements have no connection to national identity', 'Space and technology achievements are never significant historically', 'This topic has no relevance to studying a country’s history'], 0),
   ('Why is international collaboration often important for major space missions?', ['Combining resources and expertise from multiple countries can make ambitious missions possible', 'International collaboration has no role in space exploration', 'Space missions are always conducted by a single country acting alone', 'This factor has no connection to the success of space missions'], 0),
   ('Why do historians consider Canada’s technological achievements alongside its political history?', ['They provide a fuller picture of Canada’s development and contributions on the world stage', 'Technological achievements have no connection to a country’s historical significance', 'Only political events are ever considered historically important', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(46, [
E('Writing: The Formal Letter and Professional Correspondence',
  'Grade 10 English strand: writing a formal letter or professional email requires a clear purpose, respectful and precise language, and an appropriate structure suited to the intended audience.',
  [('A formal letter or professional email should use ___.', ['Respectful and precise language', 'Casual, informal slang throughout', 'Language with no connection to the intended audience', 'Vague, unclear phrasing throughout'], 0),
   ('Why is it important to clearly state the purpose of a formal letter near its beginning?', ['It helps the reader quickly understand why they are receiving the correspondence', 'Purpose should always be hidden until the very end of the letter', 'A formal letter never needs to state its purpose', 'This structure has no effect on how the letter is received'], 0),
   ('Which is an example of an appropriate closing for a formal letter?', ['Sincerely,', 'See ya,', 'Later,', 'A closing with no connection to formal writing'], 0),
   ('Why might a writer adjust their tone when writing to a professional audience compared to a friend?', ['Professional correspondence typically calls for a more respectful and precise tone', 'Tone should always remain identical regardless of the audience', 'Professional writing never requires any adjustment in tone', 'Adjusting tone has no effect on how a message is received'], 0),
   ('Why is structure important in a formal letter or professional email?', ['A clear structure helps the reader follow the message’s purpose and key points', 'Structure has no effect on how clearly a message communicates', 'Formal letters should have no discernible structure at all', 'This element only matters in casual writing'], 0)]),
M('Conditional Probability and Independence',
  'Grade 10 Data Management strand (extension): conditional probability describes the likelihood of an event occurring given that another event has already occurred, and two events are independent when one does not affect the probability of the other.',
  [('Conditional probability describes the likelihood of an event occurring given that ___.', ['Another event has already occurred', 'No other events have ever occurred', 'A completely unrelated event has occurred', 'The two events can never be connected'], 0),
   ('Two events are considered independent when ___.', ['One event does not affect the probability of the other', 'One event always determines the outcome of the other', 'Neither event can ever occur', 'Both events always occur at the exact same time'], 0),
   ('If you draw a card from a deck without replacing it, and then draw again, are the two draws independent?', ['No, because the first draw affects what remains for the second draw', 'Yes, because every draw is always completely unrelated', 'Yes, because probability never changes based on prior events', 'This situation has no connection to conditional probability'], 0),
   ('Why is it useful to determine whether two events are independent before calculating their combined probability?', ['The correct method for calculating combined probability depends on whether the events affect each other', 'Independence has no effect on how probability should be calculated', 'All events are always treated as independent, regardless of the situation', 'This distinction has no relevance to probability calculations'], 0),
   ('Why might conditional probability be useful in real-world situations, like medical testing?', ['It can help determine the likelihood of a condition given a specific test result', 'Conditional probability has no real-world applications', 'Medical testing never involves any form of probability', 'This concept only applies to purely theoretical mathematics'], 0)]),
Sc('Physics: Applications of Radioactivity in Medicine',
   'Grade 10 Physics strand: radioactive isotopes are used in medicine for both diagnostic imaging and treatment, taking advantage of their predictable decay properties to benefit patient care.',
   [('Radioactive isotopes used in medicine take advantage of their ___.', ['Predictable decay properties', 'Complete lack of any measurable properties', 'Properties unrelated to radioactivity', 'Random, unpredictable behaviour with no scientific basis'], 0),
    ('Which is an example of a medical use of radioactivity?', ['Diagnostic imaging', 'A use entirely unrelated to medicine', 'Only agricultural applications, with no medical use', 'A process with no connection to isotopes'], 0),
    ('Why must medical professionals carefully control the dosage of radioactive materials used in treatment?', ['Radioactive materials can be harmful in excessive amounts, so careful control ensures patient safety', 'Dosage has no effect on how radioactive materials interact with the body', 'Radioactive materials are always completely safe regardless of dosage', 'This factor has no connection to medical safety practices'], 0),
    ('Why are radioactive isotopes useful for diagnostic imaging in medicine?', ['They can be tracked within the body, helping visualize internal structures or processes', 'Radioactive isotopes have no useful medical applications', 'Diagnostic imaging never involves the use of radioactive materials', 'This application has no connection to how isotopes decay'], 0),
    ('Why is understanding the science behind radioactivity important for professionals working in medical imaging?', ['It helps ensure the safe and effective use of these technologies for patient care', 'This scientific understanding has no relevance to medical imaging', 'Medical professionals never need to understand radioactivity', 'This field has no connection to patient safety'], 0)]),
H('The Founding of Nunavut',
  'Grade 10 History strand: Nunavut was created as a separate Canadian territory in 1999, established in part to provide the Inuit population with greater self-governance over their traditional lands.',
  [('Nunavut was created as a separate Canadian territory in which year?', ['1999', '1949', '1867', '1970'], 0),
   ('The creation of Nunavut was established in part to provide ___.', ['The Inuit population with greater self-governance', 'No connection to any specific population', 'Reduced self-governance for Inuit communities', 'A change unrelated to Indigenous self-governance'], 0),
   ('Why is the founding of Nunavut considered a significant event in Canadian history?', ['It reflects an important step in recognizing Indigenous self-governance and land rights', 'This event had no impact on Canadian history', 'Nunavut’s founding has no connection to Indigenous rights', 'This topic has no relevance to understanding Canadian territorial history'], 0),
   ('Why might self-governance be important for the Inuit population in Nunavut?', ['It allows greater control over decisions affecting their communities, land, and culture', 'Self-governance has no connection to community well-being', 'This concept has no relevance to Indigenous communities', 'Self-governance provides no benefit to any population'], 0),
   ('Why do historians study the process leading to the creation of Nunavut?', ['It illustrates negotiations and agreements between Indigenous peoples and the Canadian government', 'This process has no historical significance', 'Nunavut was created with no negotiation process involved', 'This topic has no connection to Canadian Indigenous history'], 0)])]),

day(47, [
E('Literature: Contemporary Indigenous Voices',
  'Grade 10 English strand: contemporary Indigenous literature offers powerful perspectives on identity, resilience, and connection to land and culture, often blending traditional storytelling with modern literary forms.',
  [('Contemporary Indigenous literature often explores themes of ___.', ['Identity, resilience, and connection to land and culture', 'A topic entirely unrelated to identity or culture', 'Only fictional worlds with no connection to real experiences', 'Grammar rules with no thematic content'], 0),
   ('Why might contemporary Indigenous authors blend traditional storytelling with modern literary forms?', ['It allows them to honour cultural traditions while reaching contemporary audiences', 'Blending these elements removes all meaning from a text', 'Traditional storytelling has no place in contemporary literature', 'Modern literary forms can never connect to traditional storytelling'], 0),
   ('Why is reading contemporary Indigenous literature valuable for building a fuller understanding of Canadian literature?', ['It offers important perspectives that broaden and enrich the overall literary landscape', 'This literature has no connection to Canadian literary history', 'Indigenous voices provide no unique perspective', 'Studying this literature narrows a reader’s understanding'], 0),
   ('Which is a common element found in many works of Indigenous literature?', ['A strong connection to land and place', 'A complete absence of any cultural connection', 'A setting with no relevance to identity', 'Themes entirely unrelated to community or culture'], 0),
   ('Why might resilience be a significant theme in much contemporary Indigenous writing?', ['It can reflect the strength and continuity of Indigenous communities and cultures over time', 'Resilience has no connection to Indigenous experiences', 'This theme is never explored in Indigenous literature', 'This topic has no relevance to contemporary literature'], 0)]),
M('Non-Right Triangle Applications in Three Dimensions',
  'Grade 10 Trigonometry strand: some three-dimensional problems require breaking a complex shape into non-right triangles and applying the sine law or cosine law to find unknown measurements.',
  [('Solving a 3D problem involving non-right triangles often requires applying ___.', ['The sine law or cosine law', 'Only the Pythagorean theorem, with no other trigonometric law', 'No trigonometric relationships at all', 'A method unrelated to triangle measurements'], 0),
   ('Why might a complex three-dimensional shape be broken down into smaller triangles to solve a problem?', ['It simplifies the shape into manageable parts that can be analyzed using known trigonometric relationships', 'Breaking a shape into triangles never simplifies a 3D problem', 'Trigonometric laws can never be applied to 3D situations', 'This approach has no connection to solving geometric problems'], 0),
   ('Which is an example of a real-world application involving non-right triangles in three dimensions?', ['Calculating the height of a structure using angles measured from two different points', 'A problem entirely unrelated to measurement or geometry', 'A situation involving no triangles at all', 'A calculation that requires no trigonometric relationships'], 0),
   ('Why is it useful to identify all known information (sides and angles) before choosing which law to apply?', ['It helps determine whether the sine law or cosine law is more appropriate for solving the problem', 'The known information has no effect on which method should be used', 'Both laws are always applied in every situation, regardless of known information', 'This step has no connection to solving triangle problems'], 0),
   ('Why are 3D triangle applications relevant to careers such as surveying or architecture?', ['These careers often require precise measurements of distances and angles across three-dimensional space', '3D triangle applications have no connection to these careers', 'Surveying and architecture never involve any measurement of angles', 'This mathematical skill has no practical use in these fields'], 0)]),
Sc('Biology: Homeostasis and Body Systems',
   'Grade 10 Biology strand: homeostasis is the process by which the body maintains a stable internal environment, coordinated by body systems working together despite changes in external conditions.',
   [('Homeostasis refers to the body’s ability to ___.', ['Maintain a stable internal environment', 'Constantly change its internal environment with no regulation', 'A process unrelated to internal body conditions', 'Remain completely unaffected by any internal processes'], 0),
    ('Which is an example of the body maintaining homeostasis?', ['Regulating body temperature despite changes in external weather', 'A process where body temperature is never regulated', 'An example unrelated to internal body regulation', 'A situation where the body has no response to external conditions'], 0),
    ('Homeostasis is coordinated by ___.', ['Body systems working together', 'A single body system acting entirely alone', 'No coordination between any body systems', 'A process unrelated to body systems'], 0),
    ('Why is homeostasis important for the survival of an organism?', ['A stable internal environment is necessary for cells and organs to function properly', 'Homeostasis has no connection to an organism’s survival', 'Organisms can survive with no regulation of their internal environment', 'This concept has no relevance to biological function'], 0),
    ('Why might illness or extreme external conditions challenge the body’s ability to maintain homeostasis?', ['These factors can place additional stress on the body’s regulatory systems', 'Illness has no effect on the body’s ability to maintain homeostasis', 'External conditions never impact internal body processes', 'This concept has no connection to health or illness'], 0)]),
H('Canada’s Auto Pact and Economic Development',
  'Grade 10 History strand: the 1965 Auto Pact was a trade agreement between Canada and the United States that significantly shaped Canada’s automotive industry and broader economic development.',
  [('The Auto Pact was a trade agreement between Canada and ___.', ['The United States', 'A country with no economic connection to Canada', 'The United Kingdom', 'A country unrelated to North American trade'], 0),
   ('The Auto Pact was signed in which year?', ['1965', '1919', '1867', '1995'], 0),
   ('The Auto Pact significantly shaped Canada’s ___.', ['Automotive industry and broader economic development', 'Agricultural industry only, with no connection to manufacturing', 'A sector entirely unrelated to trade or industry', 'Only its political system, with no economic impact'], 0),
   ('Why might a trade agreement like the Auto Pact be historically significant for a country’s economy?', ['It can shape the growth and structure of key industries over time', 'Trade agreements have no impact on a country’s economic development', 'The Auto Pact had no effect on Canada’s economy', 'This topic has no connection to Canadian economic history'], 0),
   ('Why do historians study economic agreements like the Auto Pact alongside political history?', ['Economic developments often significantly influence and are influenced by political relationships', 'Economic history has no connection to political history', 'Only political events are ever historically significant', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(48, [
E('Oral Communication: The Persuasive Speech',
  'Grade 10 English strand: a persuasive speech aims to convince an audience of a particular viewpoint, using strong evidence, confident delivery, and rhetorical techniques to strengthen the argument.',
  [('A persuasive speech aims to ___.', ['Convince an audience of a particular viewpoint', 'Simply inform an audience with no argument involved', 'Entertain an audience with no persuasive purpose', 'Avoid presenting any clear viewpoint at all'], 0),
   ('Why is confident delivery important when giving a persuasive speech?', ['It can help the speaker appear credible and convincing to the audience', 'Confident delivery has no effect on how persuasive a speech is', 'A persuasive speech should always be delivered with hesitation', 'Delivery style is irrelevant to a speech’s persuasive power'], 0),
   ('Which is an example of a rhetorical technique that might strengthen a persuasive speech?', ['Using a compelling personal story to connect with the audience', 'Avoiding any connection to the audience’s experiences', 'Using no evidence or examples at all', 'Reading a speech in a completely monotone voice'], 0),
   ('Why should a persuasive speech include strong supporting evidence?', ['Evidence adds credibility and helps convince the audience of the speaker’s argument', 'Evidence is unnecessary in a persuasive speech', 'Persuasive speeches should never include supporting evidence', 'Evidence always weakens the impact of a speech'], 0),
   ('Why might a speaker consider their audience’s perspective when preparing a persuasive speech?', ['Understanding the audience helps tailor the argument to be more convincing to them specifically', 'The audience’s perspective has no effect on how a speech should be prepared', 'Persuasive speeches should be identical regardless of the audience', 'Considering the audience has no connection to effective persuasion'], 0)]),
M('Operations with Complex Numbers',
  'Grade 10 Number strand (extension): complex numbers can be added, subtracted, and multiplied using rules similar to those for real numbers, while remembering that the imaginary unit i squared equals negative one.',
  [('When adding two complex numbers, you add their ___.', ['Real parts together and their imaginary parts together', 'Only the imaginary parts, ignoring the real parts entirely', 'Only the real parts, ignoring the imaginary parts entirely', 'Neither the real nor imaginary parts'], 0),
   ('What does i squared equal?', ['Negative one', 'One', 'Zero', 'A value that cannot be determined'], 0),
   ('What is the sum of (2 + 3i) and (4 + i)?', ['6 + 4i', '6 + 3i', '2 + 4i', '8 + 3i'], 0),
   ('Why is it important to remember that i squared equals negative one when multiplying complex numbers?', ['It allows any i-squared terms produced during multiplication to be simplified correctly', 'This rule has no effect on multiplying complex numbers', 'Multiplying complex numbers never produces any i-squared terms', 'This value has no connection to complex number operations'], 0),
   ('Why do operations with complex numbers follow rules similar to those used with real numbers, like the distributive property?', ['Complex numbers are structured as combinations of real and imaginary parts, allowing similar algebraic rules to apply', 'Complex numbers follow completely different rules with no connection to real number operations', 'The distributive property can never be applied to complex numbers', 'This concept has no relevance to how complex numbers behave'], 0)]),
Sc('Earth Science: Astronomy -- The Life Cycle of Stars',
   'Grade 10 Earth Science strand: stars go through a life cycle that includes formation from clouds of gas and dust, a stable main sequence phase, and an eventual end stage that depends on the star’s original mass.',
   [('Stars form from clouds of ___.', ['Gas and dust', 'Only solid rock, with no gas involved', 'A material unrelated to space', 'Pure water vapour'], 0),
    ('During the main sequence phase, a star is generally considered ___.', ['Stable', 'Completely inactive, with no processes occurring', 'In a constant state of explosive change', 'A phase unrelated to a star’s life cycle'], 0),
    ('A star’s eventual end stage largely depends on its ___.', ['Original mass', 'Colour, with no connection to any other factor', 'Distance from Earth only', 'A factor unrelated to the star itself'], 0),
    ('Which is a possible end stage for a very massive star?', ['A supernova explosion', 'A process identical to how all stars end, with no variation', 'An outcome unrelated to the star’s mass', 'A stage with no connection to a star’s life cycle'], 0),
    ('Why is studying the life cycle of stars important for understanding the broader universe?', ['It helps explain the formation of elements and the ongoing evolution of galaxies', 'The life cycle of stars has no connection to understanding the universe', 'Stars have no meaningful life cycle to study', 'This topic has no relevance to astronomy'], 0)]),
H('The Oka Crisis and Indigenous Land Rights',
  'Grade 10 History strand: the 1990 Oka Crisis was a land dispute between the Mohawk community and the town of Oka, Quebec, that drew national attention to Indigenous land rights and sovereignty in Canada.',
  [('The Oka Crisis took place in which year?', ['1990', '1970', '1945', '1919'], 0),
   ('The Oka Crisis was a land dispute involving the Mohawk community and ___.', ['The town of Oka, Quebec', 'A location entirely unrelated to Quebec', 'A dispute with no connection to land at all', 'A community unrelated to Indigenous land rights'], 0),
   ('The Oka Crisis drew national attention to ___.', ['Indigenous land rights and sovereignty in Canada', 'A topic entirely unrelated to Indigenous rights', 'Only local municipal issues, with no broader significance', 'An issue with no connection to Canadian history'], 0),
   ('Why is the Oka Crisis considered a significant event in the history of Indigenous rights in Canada?', ['It brought national and international attention to ongoing issues of land rights and sovereignty', 'This event had no impact on public awareness of Indigenous issues', 'The Oka Crisis has no connection to Indigenous land rights', 'This topic has no relevance to Canadian history'], 0),
   ('Why do historians continue to study events like the Oka Crisis today?', ['They highlight ongoing and unresolved questions about Indigenous land rights in Canada', 'This event has no lasting historical significance', 'Land rights issues were fully and permanently resolved by this event', 'This topic has no connection to understanding modern Canada'], 0)])]),

day(49, [
E('Writing: Satire and Social Critique',
  'Grade 10 English strand: satire uses humour, irony, or exaggeration to criticize and expose flaws in individuals, institutions, or society, often with the goal of encouraging change or reflection.',
  [('Satire uses humour, irony, or exaggeration to ___.', ['Criticize and expose flaws in individuals, institutions, or society', 'Avoid any critical commentary on society', 'Praise institutions with no critical perspective at all', 'Focus only on entertainment with no deeper purpose'], 0),
   ('Why might a writer choose satire instead of a direct, serious critique?', ['Humour and exaggeration can make a critique more engaging while still delivering a serious message', 'Satire always removes any meaningful message from a critique', 'A direct, serious critique is always more effective than satire', 'Satire has no connection to social or political commentary'], 0),
   ('Which is an example of a technique commonly used in satire?', ['Exaggerating a flaw to highlight its absurdity', 'Avoiding any exaggeration or irony whatsoever', 'Presenting information in a completely neutral, factual way with no criticism', 'A technique unrelated to humour or irony'], 0),
   ('Why is satire often considered an effective tool for encouraging social or political change?', ['It can draw attention to issues in a way that resonates with and engages audiences', 'Satire has no effect on how audiences think about social issues', 'This form of writing never leads to any reflection or change', 'Satire has no connection to social or political commentary'], 0),
   ('Why might understanding a satirical piece’s historical or cultural context be important for fully grasping its meaning?', ['The critique being made often relies on knowledge of the specific issue or figure being satirized', 'Context has no effect on understanding a satirical piece', 'Satire can always be understood with no additional context', 'This factor has no connection to interpreting satire'], 0)]),
M('Review: Logarithms, Vectors, and Probability',
  'Grade 10 Functions, Geometry, and Data Management strands review: this lesson revisits logarithms, logarithmic functions, vectors, combining functions, and conditional probability covered across recent lessons.',
  [('A logarithm answers the question of ___.', ['What exponent a base must be raised to in order to produce a given number', 'What number multiplied by itself equals zero', 'What the sum of two numbers equals', 'A question unrelated to exponents'], 0),
   ('A vector represents a quantity with ___.', ['Both magnitude and direction', 'Only magnitude, with no direction', 'Only direction, with no magnitude', 'Neither magnitude nor direction'], 0),
   ('A composite function applies ___.', ['One function to the result of another function', 'Two completely unrelated, separate functions with no connection', 'Only a single function, with no combination involved', 'A method unrelated to functions'], 0),
   ('Two events are considered independent when ___.', ['One event does not affect the probability of the other', 'One event always determines the outcome of the other', 'Neither event can ever occur', 'Both events always occur at the exact same time'], 0),
   ('Why is it useful to review logarithms, vectors, and probability together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Chemistry: Stoichiometry and Chemical Calculations',
   'Grade 10 Chemistry strand: stoichiometry uses the balanced equation of a chemical reaction to calculate the amounts of reactants and products involved, based on mole ratios.',
   [('Stoichiometry uses a balanced chemical equation to calculate ___.', ['The amounts of reactants and products involved', 'The exact colour of a chemical reaction', 'The temperature required for a reaction to occur', 'A value unrelated to chemical reactions'], 0),
    ('Stoichiometric calculations are based on ___.', ['Mole ratios from the balanced equation', 'Random guesses with no mathematical basis', 'A method unrelated to chemical equations', 'Only the mass of the reactants, with no other consideration'], 0),
    ('Why must a chemical equation be balanced before performing stoichiometric calculations?', ['A balanced equation ensures the correct mole ratios are used for accurate calculations', 'Balancing has no effect on the accuracy of stoichiometric calculations', 'Chemical equations never need to be balanced for these calculations', 'This step has no connection to determining reactant or product amounts'], 0),
    ('Why is stoichiometry useful in industrial chemical processes?', ['It helps determine the precise amounts of materials needed, improving efficiency and reducing waste', 'Stoichiometry has no practical application in industry', 'Industrial processes never require precise calculations of materials', 'This concept only applies to purely theoretical chemistry problems'], 0),
    ('If a balanced equation shows a 1:2 mole ratio between two reactants, and you have 3 moles of the first reactant, how many moles of the second reactant are needed?', ['6', '3', '1.5', '9'], 0)]),
H('Canada’s Response to Global Refugee Crises',
  'Grade 10 History strand: Canada has responded to various global refugee crises over recent decades by resettling refugees, reflecting the country’s evolving role in international humanitarian efforts.',
  [('Canada has responded to global refugee crises largely through ___.', ['Resettling refugees', 'Refusing to accept any refugees under any circumstances', 'A response entirely unrelated to refugees', 'Ignoring international humanitarian concerns'], 0),
   ('Canada’s responses to refugee crises reflect its role in ___.', ['International humanitarian efforts', 'A topic entirely unrelated to global cooperation', 'Only domestic policy, with no international connection', 'An area with no historical significance'], 0),
   ('Why might a country’s response to a refugee crisis be considered historically significant?', ['It can reflect broader values and priorities regarding humanitarian responsibility', 'This response has no connection to a country’s values or history', 'Refugee crises have no relevance to studying history', 'This topic has no historical significance whatsoever'], 0),
   ('Why is it useful to study how Canada’s refugee policies have evolved over time?', ['It shows changing approaches to humanitarian responsibility and international cooperation', 'Canada’s refugee policies have never changed throughout history', 'This topic has no relevance to understanding Canadian history', 'Refugee policy has no connection to international relations'], 0),
   ('Which is an example of a factor that might influence how a country responds to a refugee crisis?', ['Public opinion and government policy priorities', 'A factor entirely unrelated to government decision-making', 'The refugee crisis itself has no influence on any response', 'A factor unrelated to humanitarian considerations'], 0)])]),

day(50, [
E('Reading: Author’s Craft -- Voice and Style Analysis',
  'Grade 10 English strand: analyzing an author’s craft involves examining their distinctive voice and stylistic choices, such as word choice, sentence structure, and figurative language, to understand how meaning is created.',
  [('Analyzing an author’s craft involves examining their ___.', ['Distinctive voice and stylistic choices', 'Only the physical length of their book', 'A factor entirely unrelated to writing style', 'The publication date of their work only'], 0),
   ('Which is an element of an author’s style that might be analyzed?', ['Word choice and sentence structure', 'Only the price of the book', 'The font used in the printed edition', 'A factor unrelated to writing technique'], 0),
   ('Why might two authors writing about a similar topic have very different voices?', ['Each author brings distinct stylistic choices and perspectives to their writing', 'All authors always write with an identical voice and style', 'Voice has no connection to how an author writes', 'Style and voice are irrelevant to how a topic is presented'], 0),
   ('Why is analyzing an author’s use of figurative language valuable for understanding a text?', ['It can reveal deeper meaning and reinforce the author’s central ideas', 'Figurative language has no connection to a text’s meaning', 'This type of analysis provides no additional insight into a text', 'Figurative language should always be ignored during analysis'], 0),
   ('Why is developing skill in analyzing author’s craft valuable for readers and writers alike?', ['It deepens understanding of texts and can inform a writer’s own stylistic choices', 'This skill has no value for either readers or writers', 'Author’s craft has no connection to effective writing', 'This type of analysis is only useful for professional critics'], 0)]),
M('Review: Grade 10 Functions, Data, and Number Extensions',
  'Grade 10 comprehensive review: this lesson revisits sine and cosine law combinations, standard deviation, combining functions, complex number operations, and 3D non-right triangle applications from Days 41-49.',
  [('A normal distribution is typically described as having a ___ shape.', ['Symmetric, bell-shaped', 'Perfectly flat, with no variation', 'Random, with no discernible pattern', 'A shape unrelated to data distribution'], 0),
   ('What does i squared equal?', ['Negative one', 'One', 'Zero', 'A value that cannot be determined'], 0),
   ('Solving a 3D problem involving non-right triangles often requires applying ___.', ['The sine law or cosine law', 'Only the Pythagorean theorem, with no other trigonometric law', 'No trigonometric relationships at all', 'A method unrelated to triangle measurements'], 0),
   ('The sum of two functions is found by ___.', ['Adding their outputs together for a given input', 'Multiplying their outputs together', 'Subtracting one function’s output from the other', 'A method unrelated to combining outputs'], 0),
   ('Why is it valuable to review these connected mathematical concepts together at the end of a unit?', ['It reinforces how these skills build on and relate to one another', 'These concepts have no connection to each other', 'Review is never useful at the end of a unit', 'Each concept must be understood with no connection to the others'], 0)]),
Sc('Review: Earth Science, Chemistry, and Physics Applications',
   'Grade 10 Science review: this lesson revisits plate tectonics, organic compounds, radioactivity in medicine, the life cycle of stars, and stoichiometry covered across recent lessons.',
   [('Plate tectonics describes the movement of ___.', ['Large sections of Earth’s crust', 'Only ocean currents, with no connection to the crust', 'A concept unrelated to Earth’s structure', 'Only the atmosphere, with no connection to the crust'], 0),
    ('Organic compounds are best described as ___.', ['Carbon-based molecules', 'Molecules that contain no carbon at all', 'A category unrelated to chemistry', 'Only inorganic minerals'], 0),
    ('A star’s eventual end stage largely depends on its ___.', ['Original mass', 'Colour, with no connection to any other factor', 'Distance from Earth only', 'A factor unrelated to the star itself'], 0),
    ('Stoichiometric calculations are based on ___.', ['Mole ratios from the balanced equation', 'Random guesses with no mathematical basis', 'A method unrelated to chemical equations', 'Only the mass of the reactants, with no other consideration'], 0),
    ('Why is it valuable to review these connected science concepts together at the end of a unit?', ['It reinforces how these scientific ideas relate to and build on one another', 'These concepts have no connection to each other', 'Review is never useful at the end of a unit', 'Each concept must be understood with no connection to the others'], 0)]),
H('Review: Social Movements and Nation-Building in Canada',
  'Grade 10 History review: this lesson revisits the Winnipeg General Strike, the Persons Case, the October Crisis, the founding of Nunavut, the Oka Crisis, and Canada’s response to global refugee crises.',
  [('The Winnipeg General Strike took place in which year?', ['1919', '1867', '1945', '1995'], 0),
   ('The Persons Case established that women were considered ___.', ['“Persons” under Canadian law, eligible for Senate appointment', 'Ineligible for any legal recognition under Canadian law', 'Excluded from all forms of public office', 'A group with no connection to Canadian legal history'], 0),
   ('The Oka Crisis was a land dispute involving the Mohawk community and ___.', ['The town of Oka, Quebec', 'A location entirely unrelated to Quebec', 'A dispute with no connection to land at all', 'A community unrelated to Indigenous land rights'], 0),
   ('The creation of Nunavut was established in part to provide ___.', ['The Inuit population with greater self-governance', 'No connection to any specific population', 'Reduced self-governance for Inuit communities', 'A change unrelated to Indigenous self-governance'], 0),
   ('Why is it valuable to review these events of social movements and nation-building together?', ['It reinforces how these historical developments connect to shape modern Canadian society', 'These events have no meaningful connections to each other', 'Review is never useful in history', 'Each event must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260724):
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
    _rebalance_answer_positions(g10_41_50)
    append_to(10, g10_41_50)
