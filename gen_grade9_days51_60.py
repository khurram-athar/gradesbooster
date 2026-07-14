#!/usr/bin/env python3
"""Phase 3 extension: Grade 9, Days 51-60 (third Grade 9 batch, continuing
the 10-day pattern past the earlier Days 41-50 set). Topics chosen to avoid
any overlap with the existing Day 1-50 set (see data/grade9.json after the
Days 41-50 batch): foil characters, personal essays, conditional sentences,
function transformations, quadratic inequalities, the Law of Sines/Cosines,
buoyancy, redox reactions, genetic engineering, and geography extensions
(coastal geography, demographic transition, Indigenous self-government,
refugee settlement patterns).

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as the Days 41-50 batch; SocialStudies content is
geography-focused for Grade 9).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes and quotation marks use the curly Unicode form (’ “ ”) so they
never collide with the single-quoted Python string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-language'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science-and-technology'
SS9 = 'https://tvolearn.com/pages/grade-9-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 Language',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science & Technology',
    'TVO Learn: Grade 9 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


g9_51_60 = [
day(51, [
L('Reading: Analyzing Foil Characters',
  'Grade 9 Reading strand: a foil character is a character whose traits contrast sharply with those of another character, often a protagonist, highlighting specific qualities through that contrast.',
  [('A foil character is best described as ___.', ['A character whose contrasting traits highlight qualities in another character', 'A character who is identical to the protagonist in every way', 'A concept unrelated to characterization', 'A minor character who never interacts with the protagonist'], 0),
   ('Why might an author include a foil character in a story?', ['To emphasize specific traits of another character through contrast', 'Foil characters are never used intentionally by authors', 'This technique has no effect on how readers view a character', 'To make every character seem exactly the same'], 0),
   ('Which is an example of a foil relationship?', ['A cautious, careful character paired with a reckless, impulsive one', 'Two characters with identical personalities and no differences', 'A concept unrelated to character contrast', 'A character who never appears alongside another character'], 0),
   ('How does recognizing a foil character deepen a reader’s understanding of the protagonist?', ['The contrast can make the protagonist’s own traits and choices stand out more clearly', 'Foil characters have no connection to understanding a protagonist', 'This technique always confuses a reader rather than clarifying', 'A foil character removes the need to analyze the protagonist at all'], 0),
   ('Why might a foil character not need to be an antagonist?', ['A foil simply highlights contrast in traits, regardless of whether the character opposes the protagonist', 'All foil characters are automatically antagonists', 'Foils and antagonists are always the exact same role', 'A foil character can never share any traits with the protagonist'], 0)]),
M('Transformations of Functions (Vertical/Horizontal Shifts)',
  'Grade 9 Algebra strand (non-linear relations): a function can be transformed by shifting its graph vertically or horizontally, such as y equals f(x) plus k for a vertical shift or y equals f(x minus h) for a horizontal shift.',
  [('A vertical shift of a function’s graph is represented by adding a constant ___.', ['Outside the function, such as f(x) plus k', 'Inside the function’s input only', 'A change unrelated to the function’s graph', 'By multiplying the entire function by zero'], 0),
   ('A horizontal shift of a function’s graph is represented by changing the ___.', ['Input value, such as f(x minus h)', 'Output value only, with no change to input', 'A value unrelated to the function’s graph', 'The function’s domain to an empty set'], 0),
   ('If y equals f(x) plus 3, the graph of f(x) shifts ___.', ['Up by 3 units', 'Down by 3 units', 'Left by 3 units', 'A shift unrelated to the value 3'], 0),
   ('If y equals f(x minus 2), the graph of f(x) shifts ___.', ['Right by 2 units', 'Left by 2 units', 'Up by 2 units', 'A shift unrelated to the value 2'], 0),
   ('Why are function transformations useful for graphing related functions quickly?', ['They allow a new graph to be sketched based on a known graph’s shape, without recalculating every point', 'Transformations always require recalculating every point from scratch', 'Function transformations have no connection to graphing', 'Every transformed function must be graphed as a completely unrelated shape'], 0)]),
Sc('Density and Buoyancy: Archimedes’ Principle',
   'Grade 9 Science Physics strand: Archimedes’ principle states that an object submerged in a fluid experiences an upward buoyant force equal to the weight of the fluid it displaces, which determines whether it floats or sinks.',
   [('Archimedes’ principle states that a submerged object experiences a buoyant force equal to ___.', ['The weight of the fluid it displaces', 'The object’s own weight only, with no connection to fluid', 'A force unrelated to the surrounding fluid', 'The temperature of the fluid'], 0),
    ('An object will float in a fluid if its density is ___ the fluid’s density.', ['Less than', 'Greater than', 'Exactly equal in every case to', 'Unrelated to'], 0),
    ('Why does a large steel ship float, even though steel itself is denser than water?', ['The ship’s overall shape displaces enough water that its average density is less than water’s', 'Steel is always less dense than water', 'The ship’s shape has no effect on whether it floats', 'Buoyant force has no connection to displaced fluid'], 0),
    ('Which of these best demonstrates Archimedes’ principle?', ['A submarine adjusting its ballast tanks to control whether it rises or sinks', 'An object with no interaction with any surrounding fluid', 'A concept unrelated to buoyancy', 'An object that always sinks regardless of its density'], 0),
    ('Why is understanding buoyancy important in fields like engineering and shipbuilding?', ['It helps engineers design vessels and structures that float or submerge as intended', 'Buoyancy has no practical application in engineering', 'This concept only applies to objects that never touch water', 'Ship design has no connection to density or displaced fluid'], 0)]),
SS('Coastal Geography and Sea Level Rise',
   'Grade 9 Social Studies (Geography) strand: coastal geography examines the physical features and human activity along coastlines, and rising sea levels due to climate change pose growing risks to coastal communities and ecosystems.',
   [('Coastal geography examines the physical features and human activity found ___.', ['Along coastlines', 'Only in landlocked, inland regions', 'A concept unrelated to geography', 'Exclusively underwater, with no connection to land'], 0),
    ('Rising sea levels are primarily linked to ___.', ['Climate change, including melting ice and thermal expansion of water', 'A decrease in the size of the world’s oceans', 'A factor entirely unrelated to climate', 'A process unrelated to coastal regions'], 0),
    ('Which of these is a risk that rising sea levels pose to coastal communities?', ['Increased flooding and erosion of coastal land', 'A guaranteed decrease in coastal flooding', 'No risk of any kind to coastal areas', 'A risk unrelated to sea level or coastlines'], 0),
    ('Why might low-lying coastal regions be especially vulnerable to sea level rise?', ['Their limited elevation gives them little buffer against rising water levels', 'Elevation has no connection to vulnerability from rising seas', 'Low-lying regions are always the least affected by sea level rise', 'Coastal vulnerability has no relationship to a region’s elevation'], 0),
    ('Which strategy might a coastal community use to adapt to rising sea levels?', ['Building sea walls or restoring natural barriers like wetlands', 'Ignoring the risk of rising sea levels entirely', 'Removing all existing coastal infrastructure with no replacement plan', 'A strategy unrelated to coastal adaptation'], 0)])]),

day(52, [
L('Writing: The Personal Essay (College-Style)',
  'Grade 9 Writing strand: a college-style personal essay reflects on a meaningful experience or personal growth, using a specific narrative moment to reveal broader insight about the writer’s character or values.',
  [('A college-style personal essay is centred on ___.', ['A meaningful experience or moment of personal growth', 'A purely factual, impersonal report', 'A concept unrelated to personal reflection', 'A fictional story with no connection to the writer'], 0),
   ('Why might a personal essay focus on one specific, narrow moment rather than a writer’s entire life story?', ['A focused moment allows for deeper reflection and more vivid, meaningful detail', 'Focusing on a single moment always weakens a personal essay', 'Personal essays should never include specific details', 'Broad, unfocused essays are always considered stronger'], 0),
   ('Which is an example of a strong opening for a personal essay about overcoming a challenge?', ['The day my bike broke down miles from home, I learned something about asking for help.', 'This essay is about a challenge.', 'Some things are difficult sometimes.', 'A sentence with no connection to a specific challenge.'], 0),
   ('Why is reflection an essential part of a personal essay?', ['It shows how an experience shaped the writer’s understanding, values, or growth', 'Reflection has no role in personal essay writing', 'Personal essays should only describe events with no insight', 'Growth and insight are never relevant to this type of essay'], 0),
   ('Why might a personal essay reveal broader insight about a writer’s character through a single narrative moment?', ['A well-chosen specific moment can illustrate larger patterns in a person’s values or personality', 'A single moment can never reveal anything about a person’s character', 'Broader insight requires describing every event in a writer’s life', 'Personal essays never connect a specific moment to broader meaning'], 0)]),
M('Solving Quadratic Inequalities',
  'Grade 9 Algebra strand: solving a quadratic inequality involves finding the values of x for which a quadratic expression is greater than or less than zero, often using the roots of the related equation and a sign analysis.',
  [('Solving a quadratic inequality involves finding the values of x for which the expression is ___.', ['Greater than or less than zero', 'Equal to exactly one specific value only', 'A concept unrelated to quadratic expressions', 'Always equal to zero'], 0),
   ('A common first step in solving a quadratic inequality is to ___.', ['Find the roots of the related quadratic equation', 'Ignore the quadratic expression entirely', 'Immediately assume there are no solutions', 'Add an unrelated constant to both sides'], 0),
   ('For the inequality x squared minus 4 greater than 0, which values of x are part of the solution?', ['x less than negative 2 or x greater than 2', 'Only x equals 2', 'All real numbers with no restriction', 'x between negative 2 and 2 only'], 0),
   ('Why might a sign analysis (testing intervals) be useful when solving a quadratic inequality?', ['It helps determine which intervals between the roots satisfy the inequality', 'Sign analysis has no use in solving inequalities', 'Testing intervals always produces an incorrect result', 'Every interval always satisfies a quadratic inequality equally'], 0),
   ('Why might the solution to a quadratic inequality be a range of values rather than a single number?', ['A quadratic expression can be greater than or less than zero across a continuous interval', 'Quadratic inequalities always have exactly one solution', 'Ranges of values are never valid solutions to inequalities', 'This concept has no connection to quadratic expressions'], 0)]),
Sc('Redox Reactions: Oxidation and Reduction',
   'Grade 9 Science Chemistry strand: a redox reaction involves the transfer of electrons between substances, where oxidation is the loss of electrons and reduction is the gain of electrons.',
   [('A redox reaction involves the transfer of ___ between substances.', ['Electrons', 'Protons only, with no electron involvement', 'Neutrons', 'A particle unrelated to chemical reactions'], 0),
    ('Oxidation is defined as the ___ of electrons.', ['Loss', 'Gain', 'A process unrelated to electrons', 'Complete elimination'], 0),
    ('Reduction is defined as the ___ of electrons.', ['Gain', 'Loss', 'A process unrelated to electrons', 'Complete elimination'], 0),
    ('Why must oxidation and reduction always occur together in a redox reaction?', ['Electrons lost by one substance must be gained by another', 'Oxidation and reduction never occur within the same reaction', 'Electrons can be created or destroyed freely in these reactions', 'Reduction always occurs with no connection to oxidation'], 0),
    ('Which of these is an example of a redox reaction?', ['Iron rusting as it reacts with oxygen', 'Ice melting into liquid water', 'A process unrelated to electron transfer', 'Water evaporating into vapour'], 0)]),
SS('The Geography of Renewable vs Non-Renewable Resource Extraction',
   'Grade 9 Social Studies (Geography) strand: renewable resources, like wind and solar energy, can be replenished naturally, while non-renewable resources, like fossil fuels, exist in finite supply and take extraction methods with differing geographic impacts.',
   [('A renewable resource is best described as one that ___.', ['Can be replenished naturally over a relatively short period', 'Exists in a completely fixed and unchangeable supply', 'A concept unrelated to natural resources', 'Can never be used without immediately running out'], 0),
    ('A non-renewable resource is best described as one that ___.', ['Exists in a finite supply and is not naturally replenished on a human timescale', 'Can be replenished instantly with no limit', 'A concept unrelated to resource extraction', 'Is always more abundant than renewable resources'], 0),
    ('Which of these is an example of a renewable resource?', ['Solar energy', 'Coal', 'Natural gas', 'Crude oil'], 0),
    ('Why might the extraction of non-renewable resources, like fossil fuels, have significant geographic impact?', ['Mining and drilling can alter landscapes and affect local ecosystems', 'Extracting non-renewable resources never affects the surrounding land', 'Non-renewable resource extraction has no connection to geography', 'Fossil fuel extraction always improves the surrounding ecosystem'], 0),
    ('Why might a region rich in renewable resources, like consistent wind or sunlight, pursue that form of energy development?', ['It can provide a sustainable, locally available energy source suited to that region’s geography', 'Renewable resources are always unrelated to a region’s specific geography', 'Regions with abundant renewable resources should avoid using them', 'This decision has no connection to geographic factors'], 0)])]),

day(53, [
L('Grammar: Conditional Sentences and Mood Shifts',
  'Grade 9 Writing strand: conditional sentences express a condition and its result, often shifting verb mood -- for example, using the subjunctive in hypothetical conditions such as “if I were” rather than “if I was.”',
  [('A conditional sentence expresses ___.', ['A condition and its result', 'Only a simple command', 'A concept unrelated to grammar', 'A question with no connection to conditions'], 0),
   ('Which sentence correctly uses the subjunctive mood in a hypothetical condition?', ['If I were taller, I would join the team.', 'If I was taller, I would join the team.', 'If I am taller, I would join the team.', 'If I be taller, I would join the team.'], 0),
   ('A conditional sentence in the present real form typically uses ___.', ['The present tense in both clauses', 'The subjunctive mood in both clauses', 'A concept unrelated to conditional sentences', 'No verb at all in either clause'], 0),
   ('Why might a writer shift to the subjunctive mood in a conditional sentence?', ['To clearly signal that the condition is hypothetical or contrary to fact', 'The subjunctive mood is never used in conditional sentences', 'Mood shifts have no effect on the meaning of a sentence', 'The subjunctive mood is only used for factual statements'], 0),
   ('Which sentence demonstrates a conditional sentence describing a real, possible situation?', ['If it rains tomorrow, we will stay inside.', 'If it rained yesterday, we would have stayed inside.', 'If it were raining right now on the moon, we would stay inside.', 'A sentence with no condition or result at all.'], 0)]),
M('Rational Functions and Asymptotes (Intro)',
  'Grade 9 Algebra strand (non-linear relations): a rational function is a ratio of two polynomials, and it can have a vertical asymptote where the denominator equals zero and a horizontal asymptote describing its end behaviour.',
  [('A rational function is best described as ___.', ['A ratio of two polynomials', 'A single polynomial with no denominator', 'A concept unrelated to algebra', 'A function that never includes a fraction'], 0),
   ('A vertical asymptote of a rational function occurs where ___.', ['The denominator equals zero', 'The numerator equals zero', 'A concept unrelated to rational functions', 'The function’s value is always exactly one'], 0),
   ('A horizontal asymptote of a rational function describes ___.', ['The function’s end behaviour as x becomes very large or very small', 'The exact value of the function at x equals zero only', 'A concept unrelated to graphing', 'The function’s single highest point'], 0),
   ('For the rational function y equals 1 over (x minus 3), where is the vertical asymptote?', ['x equals 3', 'x equals negative 3', 'x equals 0', 'y equals 3'], 0),
   ('Why is identifying asymptotes useful when graphing a rational function?', ['They reveal values the graph approaches but never actually reaches, shaping its overall behaviour', 'Asymptotes have no connection to graphing rational functions', 'A rational function’s graph never approaches any particular value', 'Asymptotes only apply to linear functions, not rational ones'], 0)]),
Sc('The Water Cycle and Watershed Systems',
   'Grade 9 Science Earth and Space Systems strand: a watershed is an area of land where all surface water drains to a common point, and the water cycle moves water through this system via evaporation, precipitation, and runoff.',
   [('A watershed is best described as ___.', ['An area of land where all surface water drains to a common point', 'A single isolated body of water with no surrounding land', 'A concept unrelated to the water cycle', 'An area with no connection to precipitation or runoff'], 0),
    ('Runoff refers to water that ___.', ['Flows over the land’s surface toward a common drainage point', 'Evaporates directly into the atmosphere with no surface flow', 'A process unrelated to the water cycle', 'Remains frozen permanently with no movement'], 0),
    ('Why might human development, such as paving surfaces, affect a watershed’s natural water flow?', ['Impermeable surfaces can increase runoff and reduce natural water absorption into the ground', 'Human development never affects how water moves through a watershed', 'Paved surfaces always increase water absorption into the ground', 'Watersheds are entirely unaffected by human land use'], 0),
    ('Why is understanding watershed boundaries important for managing water quality?', ['Pollution entering anywhere within a watershed can eventually affect its shared water source', 'Watershed boundaries have no connection to water quality', 'Pollution in one part of a watershed never affects any other part', 'Water quality management never considers watershed systems'], 0),
    ('Which of these is a component of the water cycle within a watershed?', ['Precipitation feeding into rivers and groundwater', 'A component unrelated to water movement', 'A process that only occurs in the ocean, never on land', 'Water cycles that never involve any precipitation'], 0)]),
SS('Demographic Transition Model and Population Pyramids',
   'Grade 9 Social Studies (Geography) strand: the demographic transition model describes how a country’s birth and death rates change as it develops economically, and population pyramids visually represent a population’s age and sex structure.',
   [('The demographic transition model describes how ___ change as a country develops economically.', ['Birth and death rates', 'Only the total land area of a country', 'A factor unrelated to population', 'The exact temperature of a country’s climate'], 0),
    ('A population pyramid is used to visually represent a population’s ___.', ['Age and sex structure', 'Total land area only', 'A concept unrelated to demographics', 'Average income level exclusively'], 0),
    ('A population pyramid with a wide base and narrow top typically indicates ___.', ['A high birth rate and a relatively young population', 'A declining, aging population with very few young people', 'A concept unrelated to population structure', 'A population with no children at all'], 0),
    ('Why might death rates decline before birth rates during a country’s demographic transition?', ['Improvements in healthcare and sanitation often occur before significant shifts in family size', 'Death rates and birth rates always change at exactly the same time', 'Death rates have no connection to a country’s development', 'Birth rates always decline before death rates in every country'], 0),
    ('Why are population pyramids useful tools for geographers and policy planners?', ['They help predict future needs, such as schools, healthcare, or retirement services, based on age structure', 'Population pyramids provide no useful information for planning', 'Age structure has no connection to future population needs', 'This tool only applies to countries with no population growth'], 0)])]),

day(54, [
L('Vocabulary: Idioms and Figurative Language in Context',
  'Grade 9 Language strand: an idiom is a phrase whose meaning cannot be understood literally from its individual words, and recognizing idioms and other figurative language in context helps readers grasp a writer’s intended meaning.',
  [('An idiom is best described as a phrase whose meaning ___.', ['Cannot be understood literally from its individual words', 'Is always identical to its literal, word-for-word meaning', 'A concept unrelated to figurative language', 'Has no connection to how it is used in context'], 0),
   ('What does the idiom “break the ice” typically mean?', ['To ease tension or begin a conversation in an awkward situation', 'To literally shatter a piece of ice', 'A phrase with no figurative meaning', 'To end a conversation abruptly'], 0),
   ('Why might a reader need to rely on context to understand an unfamiliar idiom?', ['The surrounding sentences can offer clues to the idiom’s intended, non-literal meaning', 'Context never provides any useful clues about idioms', 'All idioms have identical meanings regardless of context', 'Idioms should always be interpreted literally, without context'], 0),
   ('Which of these is an example of an idiom?', ['It is raining cats and dogs.', 'The sky is grey and cloudy today.', 'The temperature dropped by ten degrees.', 'A sentence with no figurative meaning at all.'], 0),
   ('Why is recognizing idioms and figurative language an important reading skill?', ['Misreading figurative language literally can lead to significant misunderstanding of a text', 'Figurative language never affects how a text is understood', 'All figurative language means exactly what it literally states', 'This skill has no connection to reading comprehension'], 0)]),
M('The Law of Sines and Law of Cosines (Intro)',
  'Grade 9 Measurement/Geometry strand: the Law of Sines and Law of Cosines are used to solve for unknown sides or angles in non-right triangles, extending beyond the basic trigonometric ratios used for right triangles.',
  [('The Law of Sines and Law of Cosines are primarily used to solve for unknown parts of ___.', ['Non-right triangles', 'Only right triangles', 'A shape unrelated to triangles', 'Circles exclusively, with no connection to triangles'], 0),
   ('The Law of Sines relates the ratio of ___.', ['A side length to the sine of its opposite angle', 'Only two angles, with no connection to side lengths', 'The area of a triangle to its perimeter', 'A concept unrelated to triangle measurement'], 0),
   ('The Law of Cosines is especially useful when a triangle problem provides ___.', ['Two sides and the included angle between them', 'No information about the triangle at all', 'Only the triangle’s area, with no side or angle values', 'A concept unrelated to solving triangles'], 0),
   ('Why are the Law of Sines and Law of Cosines needed in addition to basic right-triangle trig ratios like sine, cosine, and tangent?', ['Basic trig ratios alone cannot solve triangles that do not contain a right angle', 'Basic trig ratios can always solve every possible triangle', 'These laws only apply to right triangles, just like basic trig ratios', 'Non-right triangles never require any trigonometric methods'], 0),
   ('Why might a surveyor use the Law of Sines or Law of Cosines in real-world work?', ['To calculate unknown distances or angles in irregularly shaped land areas', 'These laws have no practical, real-world applications', 'Surveying never involves any triangles or angle measurements', 'This concept applies only to theoretical, non-applied mathematics'], 0)]),
Sc('Kinetic and Potential Energy Transformations',
   'Grade 9 Science Physics strand: kinetic energy is the energy of motion, potential energy is stored energy based on position or condition, and energy can transform between these forms while total mechanical energy is conserved.',
   [('Kinetic energy is best described as ___.', ['The energy of motion', 'Stored energy based on an object’s position', 'A concept unrelated to physics', 'Energy that only exists in stationary objects'], 0),
    ('Potential energy is best described as ___.', ['Stored energy based on an object’s position or condition', 'The energy of motion only', 'A concept unrelated to energy', 'Energy that can never be transformed into another form'], 0),
    ('As a ball falls from a height, its potential energy generally ___ while its kinetic energy ___.', ['Decreases; increases', 'Increases; decreases', 'Remains exactly the same; remains exactly the same', 'Both decrease to zero immediately'], 0),
    ('Why is the law of conservation of energy relevant to kinetic and potential energy transformations?', ['Total mechanical energy remains constant, even as it shifts between kinetic and potential forms', 'Energy is created or destroyed freely during these transformations', 'Kinetic and potential energy have no relationship to conservation of energy', 'This law states that energy always increases without limit'], 0),
    ('Which is an example of potential energy being transformed into kinetic energy?', ['A roller coaster car descending from the top of a hill', 'A ball resting motionless on a flat, level surface', 'A concept unrelated to energy transformation', 'An object that never experiences any change in position'], 0)]),
SS('The Geography of Tourism and Its Economic Impact',
   'Grade 9 Social Studies (Geography) strand: tourism geography examines how natural and cultural attractions draw visitors to a region, and the resulting economic impact can bring both benefits, like jobs, and challenges, like environmental strain.',
   [('Tourism geography examines how natural and cultural attractions ___.', ['Draw visitors to a specific region', 'Have no connection to a region’s economy', 'A concept unrelated to geography', 'Always discourage visitors from a region'], 0),
    ('Which of these is a potential economic benefit of tourism for a region?', ['Job creation in hospitality and related industries', 'A guaranteed decrease in local employment', 'A concept unrelated to tourism’s economic impact', 'The complete elimination of a region’s economy'], 0),
    ('Which of these is a potential challenge associated with high levels of tourism?', ['Environmental strain on natural attractions from overuse', 'A guaranteed improvement to the local environment', 'A concept unrelated to tourism’s impact', 'Tourism always has no effect on the environment'], 0),
    ('Why might a region promote ecotourism as an alternative to conventional tourism development?', ['Ecotourism aims to minimize environmental impact while still generating economic benefits', 'Ecotourism always causes more environmental harm than conventional tourism', 'This form of tourism has no connection to environmental considerations', 'Ecotourism provides no economic benefit to a region'], 0),
    ('Why is understanding the geography of tourism valuable when studying a region’s economy?', ['It helps explain how natural and cultural features can shape economic activity and development', 'Tourism has no connection to a region’s economic activity', 'Geography never influences where tourism develops', 'This topic has no relevance to studying regional economies'], 0)])]),

day(55, [
L('Reading: Analyzing Frame Narratives',
  'Grade 9 Reading strand: a frame narrative is a story structure in which one story is told within the context of another, often using an outer story to introduce or provide perspective on an inner story.',
  [('A frame narrative is best described as a structure in which ___.', ['One story is told within the context of another', 'A story contains only a single, uninterrupted narrative', 'A concept unrelated to narrative structure', 'Two completely unrelated stories are told with no connection'], 0),
   ('The outer story in a frame narrative often serves to ___.', ['Introduce or provide context and perspective for the inner story', 'Have no connection to the inner story at all', 'Replace the need for an inner story entirely', 'Confuse the reader with no clear purpose'], 0),
   ('Why might an author choose to use a frame narrative structure?', ['It can add an additional layer of meaning or perspective to the central story', 'Frame narratives never add any meaning to a story', 'This structure is never used intentionally by authors', 'A frame narrative always removes meaning from a story'], 0),
   ('Which is an example of a frame narrative?', ['A grandparent telling a story about a past adventure to a grandchild in the present', 'A story with only one plotline and no narrator', 'A concept unrelated to frame narratives', 'A story told entirely in a single, unbroken scene'], 0),
   ('Why might recognizing a frame narrative help a reader understand a text’s deeper meaning?', ['It reveals how the outer story’s perspective shapes the reader’s understanding of the inner story', 'Frame narratives have no connection to a text’s meaning', 'Recognizing this structure never helps with reading comprehension', 'The outer story in a frame narrative is always irrelevant to the inner one'], 0)]),
M('Systems of Linear and Quadratic Equations',
  'Grade 9 Algebra strand: a system of a linear and a quadratic equation can be solved algebraically by substitution or graphically by finding the points where a line and a parabola intersect.',
  [('A system of a linear and a quadratic equation can be solved graphically by finding ___.', ['The points where a line and a parabola intersect', 'Only the vertex of the parabola, with no connection to the line', 'A concept unrelated to systems of equations', 'The single point where the parabola crosses the x-axis'], 0),
   ('A common algebraic method for solving a system of a linear and quadratic equation is ___.', ['Substitution', 'Ignoring one of the two equations entirely', 'A method unrelated to solving equations', 'Assuming there is always exactly one solution with no calculation'], 0),
   ('A system of a linear and a quadratic equation can have how many possible solutions?', ['Zero, one, or two', 'Always exactly three', 'Always exactly one, with no other possibility', 'An unlimited number in every case'], 0),
   ('Why might a system of a linear and a quadratic equation have zero solutions?', ['The line and the parabola may never intersect at any point', 'Every line and parabola must intersect at least once', 'Zero solutions is impossible for this type of system', 'This outcome has no connection to the shapes of the graphs involved'], 0),
   ('Why is solving systems involving both linear and quadratic equations a useful algebraic skill?', ['It builds the ability to analyze how different types of relations interact and intersect', 'This skill has no real-world or mathematical application', 'Linear and quadratic equations can never be solved as a system', 'Systems of equations only ever involve two linear equations'], 0)]),
Sc('Genetic Engineering and Biotechnology Applications',
   'Grade 9 Science Biology strand: genetic engineering involves directly modifying an organism’s DNA, and biotechnology applies these techniques in fields such as agriculture, medicine, and environmental science.',
   [('Genetic engineering involves directly modifying an organism’s ___.', ['DNA', 'Physical appearance only, with no connection to DNA', 'A concept unrelated to biology', 'Skeletal structure exclusively'], 0),
    ('Which is an example of a biotechnology application in agriculture?', ['Developing crops that are genetically modified for pest resistance', 'A technique with no connection to genetics or crops', 'Removing all genetic modification techniques from farming entirely', 'A process unrelated to biotechnology'], 0),
    ('Why might genetic engineering be used in medicine?', ['To help develop treatments, such as producing insulin using modified bacteria', 'Genetic engineering has no medical applications', 'Medicine never involves biotechnology of any kind', 'This technique is used only in agriculture, never in medicine'], 0),
    ('Why do some people raise ethical questions about genetic engineering?', ['Modifying DNA raises questions about safety, consent, and long-term ecological effects', 'Genetic engineering raises no ethical questions of any kind', 'Ethical questions have no connection to biotechnology', 'This technology has no potential risks or considerations'], 0),
    ('Why is biotechnology considered an important and expanding field of science?', ['It offers new tools for addressing challenges in health, food production, and the environment', 'Biotechnology has no real-world applications', 'This field has no connection to health or agriculture', 'Genetic engineering techniques are never used outside of theory'], 0)]),
SS('Deforestation and Land Degradation',
   'Grade 9 Social Studies (Geography) strand: deforestation is the large-scale removal of forests, often for agriculture or development, and it can contribute to land degradation, biodiversity loss, and changes in local and global climate patterns.',
   [('Deforestation is best described as ___.', ['The large-scale removal of forests', 'The planting of new forests with no removal involved', 'A concept unrelated to geography', 'A process that only occurs underwater'], 0),
    ('Deforestation is often driven by the need for ___.', ['Agricultural land or development', 'Increased forest protection with no land use change', 'A factor unrelated to land use', 'A decrease in human population'], 0),
    ('Land degradation refers to ___.', ['A decline in the quality and productivity of land, often due to overuse or poor management', 'An improvement in soil quality with no negative causes', 'A concept unrelated to land use', 'A process that only affects bodies of water, not land'], 0),
    ('Why might deforestation contribute to a loss of biodiversity in a region?', ['Removing forests destroys habitats that many plant and animal species depend on', 'Deforestation has no effect on species living in a forest', 'Biodiversity always increases as forests are removed', 'Habitat loss has no connection to deforestation'], 0),
    ('Which strategy might help address the effects of deforestation and land degradation?', ['Promoting reforestation and sustainable land management practices', 'Increasing the rate of deforestation with no restrictions', 'Ignoring land degradation entirely', 'A strategy unrelated to forests or land use'], 0)])]),

day(56, [
L('Writing: The Literary Analysis Thesis and Outline',
  'Grade 9 Writing strand: a literary analysis thesis presents a specific, arguable claim about a text, and an outline organizes supporting evidence and reasoning into a clear structure before drafting the full essay.',
  [('A literary analysis thesis should present ___.', ['A specific, arguable claim about a text', 'A simple summary of the text’s plot', 'A concept unrelated to literary analysis', 'A list of random facts with no central claim'], 0),
   ('An outline for a literary analysis essay is used to ___.', ['Organize supporting evidence and reasoning before drafting the full essay', 'Replace the need for any evidence in the final essay', 'A step that is never useful before writing an essay', 'List unrelated ideas with no connection to the thesis'], 0),
   ('Which is an example of an arguable literary analysis thesis?', ['Through its use of symbolism, the novel critiques the dangers of unchecked ambition.', 'The novel has characters and a plot.', 'This book was published in a particular year.', 'A statement with no arguable claim about the text.'], 0),
   ('Why should a literary analysis thesis avoid being simply a statement of fact?', ['A factual statement alone provides nothing for the essay to argue or prove', 'Facts are always considered strong, arguable theses', 'A thesis should never make any kind of claim', 'This distinction has no effect on the strength of an essay'], 0),
   ('Why is creating an outline before drafting a literary analysis essay considered good practice?', ['It helps ensure the essay’s evidence and reasoning are logically organized in support of the thesis', 'Outlines never improve the organization of an essay', 'Essays are always stronger when written with no planning at all', 'An outline has no connection to how well-organized an essay is'], 0)]),
M('Piecewise Functions',
  'Grade 9 Algebra strand (non-linear relations): a piecewise function is defined by different expressions over different intervals of its domain, allowing it to model situations that change behaviour under different conditions.',
  [('A piecewise function is defined by ___.', ['Different expressions over different intervals of its domain', 'A single expression that applies to its entire domain with no exceptions', 'A concept unrelated to functions', 'An expression with no defined domain at all'], 0),
   ('Piecewise functions are especially useful for modelling situations that ___.', ['Change behaviour under different conditions', 'Never change under any circumstances', 'A concept unrelated to real-world modelling', 'Always behave in exactly the same way regardless of input'], 0),
   ('Which is an example of a real-world situation that could be modelled by a piecewise function?', ['A shipping cost that changes based on different weight ranges', 'A cost that remains exactly the same regardless of any factors', 'A concept unrelated to piecewise functions', 'A situation involving no variation of any kind'], 0),
   ('When graphing a piecewise function, it is important to consider ___.', ['The specific domain interval each piece of the function applies to', 'Only a single piece of the function, ignoring the others', 'A factor unrelated to graphing piecewise functions', 'Removing all domain restrictions from the function'], 0),
   ('Why might a piecewise function be more useful than a single equation for modelling tax brackets?', ['Tax rates often change at specific income thresholds, matching the structure of a piecewise function', 'Tax brackets never involve any change in rate at different income levels', 'A single equation always models tax brackets more accurately', 'Piecewise functions have no real-world modelling applications'], 0)]),
Sc('Sound Waves and the Doppler Effect',
   'Grade 9 Science Physics strand: the Doppler effect describes the change in a sound wave’s perceived frequency when its source is moving relative to an observer, such as a siren sounding higher-pitched as it approaches.',
   [('The Doppler effect describes a change in a wave’s perceived ___ due to relative motion between source and observer.', ['Frequency', 'Colour', 'A property unrelated to sound waves', 'Only its speed of light'], 0),
    ('As a sound source moves toward an observer, the perceived pitch typically ___.', ['Increases', 'Decreases', 'Remains completely unaffected by the motion', 'Becomes completely silent'], 0),
    ('As a sound source moves away from an observer, the perceived pitch typically ___.', ['Decreases', 'Increases', 'Remains completely unaffected by the motion', 'Becomes completely silent'], 0),
    ('Which is a common real-world example of the Doppler effect?', ['A siren sounding higher-pitched as an ambulance approaches, then lower as it passes', 'A sound that never changes in pitch under any circumstances', 'A concept unrelated to sound waves', 'A stationary object producing a constantly increasing pitch'], 0),
    ('Why is the Doppler effect relevant beyond sound waves, such as in astronomy?', ['A similar shift can be observed in light waves, helping scientists study the motion of distant objects', 'The Doppler effect only applies to sound and has no other applications', 'This concept has no connection to any other type of wave', 'Astronomy never makes use of wave-related phenomena'], 0)]),
SS('The Geography of International Trade Agreements',
   'Grade 9 Social Studies (Geography) strand: international trade agreements establish rules for economic exchange between countries, often shaped by geographic factors such as shared borders, transportation routes, and regional proximity.',
   [('An international trade agreement establishes rules for ___.', ['Economic exchange between countries', 'A concept unrelated to international relationships', 'The complete elimination of all trade between countries', 'Only cultural exchange, with no economic component'], 0),
    ('Which geographic factor might influence which countries form a trade agreement together?', ['Shared borders or close regional proximity', 'A factor entirely unrelated to geography', 'The countries involved must always be on opposite sides of the world', 'Trade agreements never consider geographic factors'], 0),
    ('Why might trade agreements between neighbouring countries be easier to establish than those between distant countries?', ['Shorter transportation distances and existing regional ties can simplify trade logistics', 'Distance has no effect on the ease of establishing trade agreements', 'Neighbouring countries are always less likely to trade with each other', 'Trade logistics have no connection to geographic proximity'], 0),
    ('Which is a potential benefit of an international trade agreement for participating countries?', ['Reduced trade barriers, such as tariffs, that can increase economic activity', 'Trade agreements always increase trade barriers between countries', 'A benefit unrelated to economic activity', 'Trade agreements provide no benefit to any participating country'], 0),
    ('Why is studying trade agreements relevant to understanding global geography?', ['It shows how geographic and economic factors shape relationships between countries and regions', 'Trade agreements have no connection to geography', 'This topic has no relevance to understanding global patterns', 'Geography never influences international economic relationships'], 0)])]),

day(57, [
L('Media Literacy: Deepfakes and Synthetic Media',
  'Grade 9 Media Literacy strand: a deepfake is synthetic media created using artificial intelligence to convincingly alter or fabricate images, audio, or video, raising concerns about misinformation and trust in digital content.',
  [('A deepfake is best described as ___.', ['Synthetic media created using artificial intelligence to alter or fabricate content', 'A completely unedited, original video with no alterations', 'A concept unrelated to digital media', 'A term for any video shared on social media'], 0),
   ('Deepfakes are most commonly created using ___.', ['Artificial intelligence techniques', 'Simple text editing software only', 'A process unrelated to technology', 'Traditional hand-drawn illustration'], 0),
   ('Why do deepfakes raise concerns about misinformation?', ['They can convincingly present fabricated events or statements as if they were real', 'Deepfakes are always immediately obvious and easy to identify as fake', 'This technology has no connection to spreading false information', 'Deepfakes only affect written text, not audio or video'], 0),
   ('Which of these might help someone evaluate whether a video could be a deepfake?', ['Checking whether the footage can be verified through other credible sources', 'Assuming every video seen online is automatically authentic', 'Ignoring the source of a video entirely', 'A method unrelated to evaluating digital media'], 0),
   ('Why is understanding deepfakes an increasingly important media literacy skill?', ['As synthetic media becomes more realistic, distinguishing fact from fabrication becomes more challenging', 'Deepfakes have no real-world impact on how people understand media', 'This skill has no connection to evaluating digital content', 'Synthetic media has no effect on public trust in digital information'], 0)]),
M('Financial Literacy: Amortization and Loans',
  'Grade 9 Financial Literacy strand: amortization is the process of paying off a loan over time through regular payments that cover both principal and interest, with the interest portion typically decreasing as the loan balance is paid down.',
  [('Amortization refers to the process of ___.', ['Paying off a loan over time through regular payments', 'Immediately paying off an entire loan in a single payment', 'A concept unrelated to loans or borrowing', 'Increasing a loan’s total balance with no payments made'], 0),
   ('Each regular loan payment in an amortized loan typically covers ___.', ['Both principal and interest', 'Only interest, with no reduction of the principal', 'Only principal, with no interest included', 'Neither principal nor interest'], 0),
   ('As an amortized loan is paid down over time, the interest portion of each payment generally ___.', ['Decreases', 'Increases', 'Remains exactly the same throughout the entire loan', 'Becomes completely unrelated to the loan balance'], 0),
   ('Why might understanding amortization be useful when comparing loan options, such as a mortgage?', ['It helps borrowers understand the total cost of a loan and how payments are applied over time', 'Amortization has no effect on the total cost of a loan', 'Loan payments are always identical regardless of amortization schedule', 'This concept has no relevance to personal financial decisions'], 0),
   ('Why might a longer loan term generally result in more interest paid overall, even with smaller monthly payments?', ['Interest accumulates over a longer period, even if each individual payment is smaller', 'A longer loan term always reduces the total interest paid', 'Loan term length has no connection to the total interest paid', 'Smaller monthly payments always reduce the total cost of a loan'], 0)]),
Sc('Soil Science and Nutrient Cycling in Agriculture',
   'Grade 9 Science Biology strand: healthy soil relies on nutrient cycling, where organic matter decomposes and returns essential nutrients like nitrogen and phosphorus to the soil, supporting plant growth in agricultural systems.',
   [('Nutrient cycling in soil involves ___.', ['Organic matter decomposing and returning nutrients to the soil', 'Nutrients disappearing permanently once used by a plant', 'A concept unrelated to soil health', 'Only water moving through soil, with no nutrient involvement'], 0),
    ('Which of these is an essential nutrient commonly cycled through healthy soil?', ['Nitrogen', 'Helium', 'A substance unrelated to plant growth', 'Oxygen gas exclusively, with no other nutrients involved'], 0),
    ('Why is decomposition an important part of nutrient cycling in agricultural soil?', ['It breaks down organic matter, releasing nutrients back into the soil for future plant growth', 'Decomposition removes all nutrients from soil permanently', 'This process has no connection to soil health or plant growth', 'Decomposition only affects water content, not nutrient levels'], 0),
    ('Why might overuse of agricultural land without proper nutrient replenishment lead to reduced crop yields?', ['Continuously removing nutrients without replacing them can deplete the soil’s fertility over time', 'Soil nutrients are always replenished automatically with no management needed', 'Crop yields have no connection to soil nutrient levels', 'Overusing land always improves long-term soil fertility'], 0),
    ('Which of these is a practice farmers might use to support healthy nutrient cycling?', ['Rotating crops or adding compost to replenish soil nutrients', 'Removing all organic matter from farmland permanently', 'Ignoring soil health entirely when farming', 'A practice unrelated to nutrient cycling'], 0)]),
SS('Indigenous Self-Government and Land Governance in Canada',
   'Grade 9 Social Studies (Geography) strand: Indigenous self-government refers to the authority of Indigenous communities in Canada to govern their own affairs, including decisions related to land use and management within their territories.',
   [('Indigenous self-government refers to the authority of Indigenous communities to ___.', ['Govern their own affairs, including matters related to their land', 'Have no role in decisions affecting their own communities', 'A concept unrelated to governance', 'Be governed entirely by decisions made outside their communities'], 0),
    ('Land governance in the context of Indigenous self-government often involves decisions about ___.', ['Land use and resource management within Indigenous territories', 'A topic entirely unrelated to land or territory', 'Land that has no connection to any Indigenous community', 'Only land located outside of Canada'], 0),
    ('Why is Indigenous self-government significant in the context of Canadian geography and history?', ['It reflects the recognition of Indigenous authority over decisions affecting their own land and communities', 'Self-government has no connection to land or geography', 'This topic has no relevance to understanding Canada’s history', 'Indigenous communities have never sought authority over their own affairs'], 0),
    ('Which of these could be an outcome of an Indigenous self-government agreement?', ['An Indigenous community gaining greater control over local land use decisions', 'A complete removal of any Indigenous authority over local matters', 'An outcome unrelated to governance or land', 'A reduction in an Indigenous community’s decision-making authority in every case'], 0),
    ('Why might studying Indigenous self-government be relevant to understanding geography in Canada?', ['It connects land, governance, and geographic territory in ways that shape how regions are managed', 'Indigenous governance has no connection to geographic study', 'This topic has no relevance to studying land use in Canada', 'Governance and geography are always completely unrelated fields'], 0)])]),

day(58, [
L('Grammar: Correlative Conjunctions and Sentence Balance',
  'Grade 9 Writing strand: correlative conjunctions, such as “either…or” and “not only…but also,” work in pairs to connect balanced grammatical elements within a sentence.',
  [('Correlative conjunctions work in ___ to connect elements within a sentence.', ['Pairs', 'Groups of three or more only', 'A concept unrelated to conjunctions', 'Isolation, with no connection to other words'], 0),
   ('Which of these is an example of a correlative conjunction pair?', ['Either…or', 'And…and', 'A pair unrelated to correlative conjunctions', 'But…but'], 0),
   ('Which sentence correctly uses a correlative conjunction with balanced grammatical elements?', ['She wanted not only to travel but also to write about her experiences.', 'She wanted not only to travel but also writing about her experiences.', 'A sentence unrelated to correlative conjunctions.', 'She wanted not only travel but also to write about her experiences.'], 0),
   ('Why is grammatical balance important when using correlative conjunctions?', ['It ensures the two connected elements have a similar and consistent grammatical structure', 'Grammatical balance is never necessary in these sentences', 'Correlative conjunctions never require balanced structure', 'Balance has no effect on how a sentence reads'], 0),
   ('Which of these is another example of a correlative conjunction pair?', ['Neither…nor', 'If…then, only', 'A pair unrelated to correlative conjunctions', 'Because…since'], 0)]),
M('Geometric Sequences and Series (Intro)',
  'Grade 9 Number/Algebra strand: a geometric sequence is a list of numbers where each term is found by multiplying the previous term by a constant ratio, and a geometric series is the sum of the terms in such a sequence.',
  [('A geometric sequence is formed by ___.', ['Multiplying each term by a constant ratio to find the next term', 'Adding a constant value to each term to find the next term', 'A concept unrelated to sequences', 'Randomly generating each term with no consistent pattern'], 0),
   ('In the geometric sequence 2, 6, 18, 54, the common ratio is ___.', ['3', '4', 'A value unrelated to this sequence', '6'], 0),
   ('A geometric series refers to ___.', ['The sum of the terms in a geometric sequence', 'A single term within a geometric sequence', 'A concept unrelated to geometric sequences', 'A sequence with no defined common ratio'], 0),
   ('What is the next term in the geometric sequence 5, 10, 20, 40, ___?', ['80', '45', 'A value unrelated to this sequence', '60'], 0),
   ('Why might a geometric sequence be used to model situations like compound interest or population growth?', ['These situations often involve repeated multiplication by a consistent rate, matching a geometric pattern', 'Geometric sequences can never model real-world growth situations', 'Compound interest always follows a simple addition pattern instead', 'This concept has no connection to modelling real-world change'], 0)]),
Sc('Electric Fields and Static Discharge',
   'Grade 9 Science Physics strand: an electric field surrounds a charged object and exerts a force on other charges within it, and static discharge occurs when built-up static electricity suddenly transfers between objects.',
   [('An electric field surrounds a charged object and exerts a force on ___.', ['Other charges within that field', 'Only objects with no charge at all', 'A concept unrelated to electricity', 'Nothing, as electric fields exert no force'], 0),
    ('Static discharge occurs when ___.', ['Built-up static electricity suddenly transfers between objects', 'Electric charge is permanently trapped with no possible transfer', 'A concept unrelated to static electricity', 'An object loses all electrical properties permanently'], 0),
    ('Which of these is a common everyday example of static discharge?', ['Feeling a small shock after touching a doorknob on a dry day', 'A situation with no connection to static electricity', 'An object that never builds up any electric charge', 'A process unrelated to electric fields'], 0),
    ('Why might friction, such as rubbing a balloon on hair, cause a build-up of static charge?', ['Friction can transfer electrons between materials, leaving one object with excess charge', 'Friction never has any effect on electric charge', 'Static charge only occurs without any physical contact between objects', 'Electrons can never be transferred between materials through friction'], 0),
    ('Why is understanding electric fields important in fields like electronics engineering?', ['It helps explain how charged components interact and influence one another in a circuit or device', 'Electric fields have no relevance to electronics or engineering', 'This concept only applies to naturally occurring static electricity, not engineered devices', 'Electric fields never influence how electronic components function'], 0)]),
SS('Geography of Natural Disaster Preparedness and Resilience',
   'Grade 9 Social Studies (Geography) strand: disaster preparedness involves planning and infrastructure designed to reduce harm from natural hazards, and resilience refers to a community’s ability to recover and adapt after a disaster occurs.',
   [('Disaster preparedness involves planning and infrastructure designed to ___.', ['Reduce harm from natural hazards', 'Increase the impact of natural hazards on a community', 'A concept unrelated to natural disasters', 'Prevent any need for future infrastructure planning'], 0),
    ('Resilience, in the context of natural disasters, refers to a community’s ability to ___.', ['Recover and adapt after a disaster occurs', 'Avoid all natural disasters permanently', 'A concept unrelated to disaster response', 'Remain completely unaffected by any disaster'], 0),
    ('Which of these is an example of disaster preparedness infrastructure?', ['An early warning system for approaching severe storms', 'A structure with no connection to disaster response', 'Infrastructure designed to increase a community’s vulnerability', 'A system unrelated to natural hazards'], 0),
    ('Why might geographic location influence the types of natural disasters a region needs to prepare for?', ['Different regions face different hazards based on factors like climate, terrain, and proximity to fault lines or coastlines', 'Geographic location has no connection to the types of natural disasters a region faces', 'All regions face identical natural hazards regardless of location', 'Disaster preparedness never depends on a region’s geography'], 0),
    ('Why is community resilience an important factor in recovering from natural disasters?', ['Resilient communities are often better able to rebuild and adapt after a disaster’s impact', 'Resilience has no effect on how a community recovers from a disaster', 'Communities never need to adapt or recover after a natural disaster', 'This concept has no relevance to disaster geography'], 0)])]),

day(59, [
L('Reading: Evaluating Bias in Historical and Contemporary Texts',
  'Grade 9 Reading strand: bias in a text reflects a particular perspective or slant, and evaluating bias in both historical and contemporary texts involves considering the author’s background, purpose, and the historical or social context in which the text was created.',
  [('Bias in a text reflects ___.', ['A particular perspective or slant', 'A text with absolutely no perspective of any kind', 'A concept unrelated to reading analysis', 'Only factual, entirely objective information'], 0),
   ('When evaluating bias in a historical text, a reader should consider ___.', ['The author’s background, purpose, and the historical context in which it was written', 'Only the exact date the text was published, with no other factors', 'A concept unrelated to evaluating bias', 'Nothing about the author or the text’s context'], 0),
   ('Why might a text from a particular historical period reflect the biases common to that era?', ['Authors are often shaped by the social attitudes and assumptions of their time', 'Historical texts are always completely free of any bias', 'Time period has no connection to how a text is written', 'Authors are never influenced by the era in which they write'], 0),
   ('Why is it important to evaluate bias in contemporary texts, such as news articles, as well as historical ones?', ['Modern texts can also reflect a particular perspective or agenda that shapes how information is presented', 'Contemporary texts are always completely free of any bias', 'Bias only exists in historical texts, never in modern writing', 'Evaluating bias is unnecessary for texts written recently'], 0),
   ('Which of these might indicate potential bias in a text?', ['Presenting only one side of an issue while ignoring other credible perspectives', 'Presenting multiple credible perspectives on an issue', 'A concept unrelated to evaluating bias', 'Citing verifiable evidence from multiple credible sources'], 0)]),
M('Solving Absolute Value Equations and Inequalities',
  'Grade 9 Algebra strand: an absolute value represents a number’s distance from zero, so solving an absolute value equation or inequality typically requires considering both a positive and a negative case.',
  [('Absolute value represents a number’s ___.', ['Distance from zero', 'Exact sign, whether positive or negative', 'A concept unrelated to number values', 'Value multiplied by negative one in every case'], 0),
   ('Solving an absolute value equation typically requires considering ___.', ['Both a positive and a negative case', 'Only a single possible case, with no other consideration', 'A concept unrelated to absolute value', 'No cases at all, since there is never a solution'], 0),
   ('Solve for x: the absolute value of x equals 5.', ['x equals 5 or x equals negative 5', 'x equals 5 only', 'x equals negative 5 only', 'There is no possible solution'], 0),
   ('When solving an absolute value inequality such as the absolute value of x is less than 3, the solution represents ___.', ['All values of x between negative 3 and 3', 'Only the single value x equals 3', 'A concept unrelated to absolute value inequalities', 'All values of x that are greater than 3'], 0),
   ('Why must both cases be considered when solving an absolute value equation or inequality?', ['A quantity inside absolute value bars could originally have been either positive or negative', 'Absolute value equations only ever have one possible case to consider', 'Considering both cases never produces a valid additional solution', 'This concept has no connection to how absolute value is defined'], 0)]),
Sc('Ecological Succession',
   'Grade 9 Science Biology strand: ecological succession is the gradual process by which an ecosystem’s species composition changes over time, often beginning with pioneer species and progressing toward a more stable community.',
   [('Ecological succession describes the gradual process by which ___.', ['An ecosystem’s species composition changes over time', 'An ecosystem remains permanently unchanged over time', 'A concept unrelated to ecosystems', 'A single species remains the only one present forever'], 0),
    ('Pioneer species are typically ___.', ['The first species to colonize a previously disturbed or empty environment', 'The final, most established species in a mature ecosystem', 'A concept unrelated to ecological succession', 'Species that never appear in any ecosystem'], 0),
    ('Primary succession occurs in an environment that ___.', ['Previously had no soil or existing life, such as bare rock', 'Already has an established, mature ecosystem with rich soil', 'A concept unrelated to succession', 'Has been recently disturbed but still retains its soil'], 0),
    ('Secondary succession occurs in an environment that ___.', ['Has been disturbed but still retains its soil, such as after a forest fire', 'Never had any soil or previous life present', 'A concept unrelated to succession', 'Is entirely underwater with no land involved'], 0),
    ('Why is ecological succession considered an important process to understand in biology?', ['It explains how ecosystems recover and change following disturbances over time', 'Succession has no connection to how ecosystems change', 'Ecosystems never recover or change following a disturbance', 'This process has no relevance to studying biology'], 0)]),
SS('The Geography of Refugee Settlement Patterns',
   'Grade 9 Social Studies (Geography) strand: refugee settlement patterns are shaped by factors such as proximity to conflict zones, existing community networks, and the policies of host countries, resulting in varied geographic distributions.',
   [('Refugee settlement patterns are shaped by factors such as ___.', ['Proximity to conflict zones and the policies of host countries', 'Only random chance, with no identifiable factors', 'A concept unrelated to geography', 'Weather conditions exclusively, with no other influence'], 0),
    ('Why might refugees often initially settle in countries neighbouring a conflict zone?', ['Proximity can make immediate relocation more accessible during a crisis', 'Neighbouring countries are always the least accessible option available', 'Refugees never settle near the conflict zones they are fleeing', 'Proximity has no connection to refugee settlement patterns'], 0),
    ('Why might existing community networks influence where refugees choose to settle?', ['Established communities can provide support, language assistance, and a sense of familiarity', 'Community networks have no influence on settlement decisions', 'Refugees always avoid areas with existing community connections', 'This factor has no connection to geographic settlement patterns'], 0),
    ('How can the policies of a host country affect refugee settlement patterns?', ['Policies can determine where refugees are permitted to live or receive support services', 'Host country policies never have any influence on where refugees settle', 'Settlement patterns are entirely unrelated to government policy', 'All host countries have identical policies regarding refugee settlement'], 0),
    ('Why is studying refugee settlement patterns relevant to human geography?', ['It shows how geographic, social, and political factors interact to shape where and how people resettle', 'This topic has no connection to human geography', 'Refugee movement never involves any geographic considerations', 'Settlement patterns are entirely random with no explainable factors'], 0)])]),

day(60, [
L('Review: Foil Characters, Personal Essays, Frame Narratives, and Bias',
  'Grade 9 Reading and Writing strands review: this lesson revisits foil characters, the personal essay, conditional sentences, frame narratives, deepfakes, correlative conjunctions, and evaluating bias from Days 51-59.',
  [('A foil character is best described as ___.', ['A character whose contrasting traits highlight qualities in another character', 'A character who is identical to the protagonist in every way', 'A concept unrelated to characterization', 'A minor character who never interacts with the protagonist'], 0),
   ('A college-style personal essay is centred on ___.', ['A meaningful experience or moment of personal growth', 'A purely factual, impersonal report', 'A concept unrelated to personal reflection', 'A fictional story with no connection to the writer'], 0),
   ('A frame narrative is best described as a structure in which ___.', ['One story is told within the context of another', 'A story contains only a single, uninterrupted narrative', 'A concept unrelated to narrative structure', 'Two completely unrelated stories are told with no connection'], 0),
   ('A deepfake is best described as ___.', ['Synthetic media created using artificial intelligence to alter or fabricate content', 'A completely unedited, original video with no alterations', 'A concept unrelated to digital media', 'A term for any video shared on social media'], 0),
   ('Why is it useful to review reading and writing concepts like character analysis, narrative structure, and bias together?', ['These related literacy skills reinforce one another for stronger overall comprehension and communication', 'These topics have no meaningful connection to one another', 'Review is never useful for reading and writing skills', 'Each concept must always be studied in complete isolation'], 0)]),
M('Review: Functions, Inequalities, Systems, and Sequences',
  'Grade 9 Algebra strand review: this lesson revisits function transformations, quadratic inequalities, rational functions, systems of linear/quadratic equations, piecewise functions, and geometric sequences from Days 51-59.',
  [('A vertical shift of a function’s graph is represented by adding a constant ___.', ['Outside the function, such as f(x) plus k', 'Inside the function’s input only', 'A change unrelated to the function’s graph', 'By multiplying the entire function by zero'], 0),
   ('Solving a quadratic inequality involves finding the values of x for which the expression is ___.', ['Greater than or less than zero', 'Equal to exactly one specific value only', 'A concept unrelated to quadratic expressions', 'Always equal to zero'], 0),
   ('A rational function is best described as ___.', ['A ratio of two polynomials', 'A single polynomial with no denominator', 'A concept unrelated to algebra', 'A function that never includes a fraction'], 0),
   ('A geometric sequence is formed by ___.', ['Multiplying each term by a constant ratio to find the next term', 'Adding a constant value to each term to find the next term', 'A concept unrelated to sequences', 'Randomly generating each term with no consistent pattern'], 0),
   ('Why is it useful to review functions, inequalities, systems, and sequences together?', ['These related algebra concepts build on and reinforce one another for deeper understanding', 'These topics have no connection to each other', 'Review is never useful in mathematics', 'Each topic must be learned with no connection to the others'], 0)]),
Sc('Review: Buoyancy, Redox Reactions, Energy, and Ecological Succession',
   'Grade 9 Science strand review: this lesson revisits Archimedes’ principle, redox reactions, kinetic/potential energy, the Doppler effect, genetic engineering, and ecological succession from Days 51-59.',
   [('Archimedes’ principle states that a submerged object experiences a buoyant force equal to ___.', ['The weight of the fluid it displaces', 'The object’s own weight only, with no connection to fluid', 'A force unrelated to the surrounding fluid', 'The temperature of the fluid'], 0),
    ('A redox reaction involves the transfer of ___ between substances.', ['Electrons', 'Protons only, with no electron involvement', 'Neutrons', 'A particle unrelated to chemical reactions'], 0),
    ('Kinetic energy is best described as ___.', ['The energy of motion', 'Stored energy based on an object’s position', 'A concept unrelated to physics', 'Energy that only exists in stationary objects'], 0),
    ('Ecological succession describes the gradual process by which ___.', ['An ecosystem’s species composition changes over time', 'An ecosystem remains permanently unchanged over time', 'A concept unrelated to ecosystems', 'A single species remains the only one present forever'], 0),
    ('Why is it valuable to review physics, chemistry, and biology concepts like buoyancy, redox reactions, and succession together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: Coastal Geography, Trade, Governance, and Refugee Settlement',
   'Grade 9 Social Studies (Geography) review: this lesson revisits coastal geography and sea level rise, the demographic transition model, international trade agreements, Indigenous self-government, and refugee settlement patterns from Days 51-59.',
   [('Coastal geography examines the physical features and human activity found ___.', ['Along coastlines', 'Only in landlocked, inland regions', 'A concept unrelated to geography', 'Exclusively underwater, with no connection to land'], 0),
    ('The demographic transition model describes how ___ change as a country develops economically.', ['Birth and death rates', 'Only the total land area of a country', 'A factor unrelated to population', 'The exact temperature of a country’s climate'], 0),
    ('An international trade agreement establishes rules for ___.', ['Economic exchange between countries', 'A concept unrelated to international relationships', 'The complete elimination of all trade between countries', 'Only cultural exchange, with no economic component'], 0),
    ('Indigenous self-government refers to the authority of Indigenous communities to ___.', ['Govern their own affairs, including matters related to their land', 'Have no role in decisions affecting their own communities', 'A concept unrelated to governance', 'Be governed entirely by decisions made outside their communities'], 0),
    ('Why is it useful to review coastal geography, trade, governance, and settlement patterns together?', ['It reinforces how these interconnected geographic and social issues shape regions and communities', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260803):
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
    _rebalance_answer_positions(g9_51_60)
    append_to(9, g9_51_60)
