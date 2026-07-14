#!/usr/bin/env python3
"""Phase 3 extension: Grade 10, Days 51-60 (third Grade 10 batch, first
past the Day 50 milestone). Topics chosen to avoid any overlap with the
existing Day 1-50 set (see data/grade10.ts): the Bildungsroman, the
scholarship/college application essay, rhetorical devices, absurdist
fiction, documentary technique, epistolary narratives, the extended
definition essay, impromptu speaking, and war literature in English;
logarithmic equations, rational functions, 3D vectors, the binomial
theorem, piecewise functions, three-variable systems, permutations and
combinations, polynomial division, and rates of change in Math;
colligative properties, Mendelian genetics, projectile motion, polymer
chemistry, the nervous system, weathering and erosion, simple harmonic
motion, gas laws, and symbiotic community ecology in Science; and the
Halifax Explosion, the Korean War, the Avro Arrow, the Suez Crisis and
Pearson-era peacekeeping, the Employment Equity Act, same-sex marriage
legalization, the National Energy Program, Japanese Canadian internment
redress, and Canada in Afghanistan in History.

Subject keys for Grade 10 are "English" and "History" (confirmed via
data/grade10.ts), same as gen_grade10_days41_50.py.

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option
text; apostrophes and quotation marks use the curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
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


g10_51_60 = [
day(51, [
E('Reading: Analyzing the Bildungsroman (Coming-of-Age Novel)',
  'Grade 10 English strand: a bildungsroman is a coming-of-age novel that traces a protagonist’s psychological and moral growth from youth into maturity, often through a formative journey or series of challenges.',
  [('A bildungsroman is best described as a novel that traces ___.', ['A protagonist’s psychological and moral growth from youth into maturity', 'A single event with no connection to a character’s development', 'A protagonist who never changes throughout the story', 'A setting description with no focus on character at all'], 0),
   ('Which is a common feature of a bildungsroman?', ['A formative journey or series of challenges that shapes the protagonist', 'A protagonist who begins and ends the story completely unchanged', 'A structure unrelated to character development', 'A plot with no connection to growth or maturity'], 0),
   ('Why might a coming-of-age novel often include a mentor figure?', ['A mentor can guide the protagonist and help prompt their growth and self-understanding', 'Mentor figures are never included in this type of novel', 'A reason unrelated to character development', 'Mentors only appear in stories with no focus on growth'], 0),
   ('Why do readers often find bildungsroman novels relatable?', ['They reflect universal experiences of growing up, identity, and self-discovery', 'This type of novel has no connection to readers’ own experiences', 'A reason unrelated to reading comprehension', 'Coming-of-age stories never explore identity or self-discovery'], 0),
   ('Which of these would best signal a turning point in a bildungsroman?', ['A significant challenge that changes how the protagonist sees themselves or the world', 'A moment with no impact on the protagonist at all', 'A concept unrelated to this type of novel', 'An event that occurs with no connection to the plot'], 0)]),
M('Solving Logarithmic Equations',
  'Grade 10 Functions strand (extension): solving a logarithmic equation often involves using logarithm properties to combine terms, then rewriting the equation in exponential form to isolate the unknown variable.',
  [('Solving a logarithmic equation often involves rewriting it in ___.', ['Exponential form', 'Linear form only, with no other conversion possible', 'A form unrelated to exponents', 'Fraction form with no connection to exponents'], 0),
   ('If log base 2 of x equals 5, what is x?', ['32', '10', 'A value unrelated to the equation', '25'], 0),
   ('Why might logarithm properties, such as the product or quotient rule, be used before solving a logarithmic equation?', ['They can combine multiple logarithmic terms into a single term, simplifying the equation', 'These properties never simplify a logarithmic equation', 'Logarithm properties have no connection to solving equations', 'This step always makes an equation more difficult to solve'], 0),
   ('Why must the solution to a logarithmic equation be checked against the domain of the original logarithms?', ['A logarithm is only defined for positive arguments, so some solutions may be extraneous', 'Logarithms are defined for every possible number, so no checking is required', 'This step has no connection to solving logarithmic equations', 'Checking a solution never affects whether it is valid'], 0),
   ('Why are logarithmic equations useful for modelling situations like sound intensity or pH levels?', ['These situations involve quantities that change across a very wide range, which logarithms can represent efficiently', 'Logarithmic equations have no real-world applications', 'Sound intensity and pH levels never involve any mathematical modelling', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Colligative Properties of Solutions',
   'Grade 10 Chemistry strand: colligative properties, such as boiling point elevation and freezing point depression, depend on the number of dissolved particles in a solution rather than on the specific identity of the solute.',
   [('Colligative properties depend primarily on ___.', ['The number of dissolved particles in a solution', 'The specific colour of the solute', 'A factor unrelated to dissolved particles', 'The exact identity of the solute alone, with no connection to particle count'], 0),
    ('Boiling point elevation refers to ___.', ['An increase in a solution’s boiling point caused by a dissolved solute', 'A decrease in a solution’s boiling point caused by a dissolved solute', 'A concept unrelated to colligative properties', 'A property that never changes when a solute is added'], 0),
    ('Freezing point depression refers to ___.', ['A decrease in a solution’s freezing point caused by a dissolved solute', 'An increase in a solution’s freezing point caused by a dissolved solute', 'A concept unrelated to colligative properties', 'A property unaffected by dissolved particles'], 0),
    ('Which is a real-world application of freezing point depression?', ['Spreading salt on icy roads to lower the freezing point of water', 'Boiling water at a consistently higher temperature at high altitude', 'An application unrelated to colligative properties', 'Cooling a liquid with no connection to any dissolved substance'], 0),
    ('Why are colligative properties useful for estimating the concentration of a solution?', ['Measurable changes like boiling or freezing point shifts can be related back to the amount of dissolved particles', 'Colligative properties provide no information about a solution’s concentration', 'A reason unrelated to solution chemistry', 'Concentration can never be estimated using any physical property'], 0)]),
H('The Halifax Explosion and Its Aftermath',
  'Grade 10 History strand: the 1917 Halifax Explosion, caused by a collision between two ships in Halifax Harbour, was one of the largest artificial explosions in history prior to nuclear weapons and devastated much of the city.',
  [('The Halifax Explosion took place in which year?', ['1917', '1945', '1970', '1867'], 0),
   ('The Halifax Explosion was caused by ___.', ['A collision between two ships in Halifax Harbour', 'A natural disaster with no connection to ships', 'An event unrelated to Halifax', 'A planned military attack on the city'], 0),
   ('Why is the Halifax Explosion historically significant?', ['It was one of the largest artificial explosions in history prior to nuclear weapons, devastating the city', 'This event had no significant impact on Halifax', 'The explosion has no connection to Canadian history', 'This event occurred with no lasting consequences at all'], 0),
   ('Why might the response to the Halifax Explosion be studied alongside its causes?', ['The relief efforts and rebuilding reveal how communities and governments respond to large-scale disasters', 'The response to this disaster has no historical significance', 'Relief efforts never followed this event', 'This topic has no connection to understanding disaster response'], 0),
   ('Why do historians continue to study the Halifax Explosion today?', ['It offers insight into industrial-era hazards, disaster response, and community resilience', 'This event has no lasting relevance to Canadian history', 'The Halifax Explosion has been entirely forgotten with no historical record', 'This topic has no connection to understanding early 20th-century Canada'], 0)])]),

day(52, [
E('Writing: The College/Scholarship Application Essay',
  'Grade 10 English strand: a college or scholarship application essay presents a compelling personal narrative that highlights a student’s character, achievements, and goals within a concise, structured format.',
  [('A college or scholarship application essay is designed to present ___.', ['A compelling personal narrative highlighting character, achievements, and goals', 'A purely factual list with no personal reflection at all', 'A concept unrelated to personal writing', 'A generic essay with no connection to the writer’s own experiences'], 0),
   ('Why is it important for this type of essay to be concise and focused?', ['Application essays typically have strict word or length limits, requiring careful, purposeful writing', 'Length and focus never matter in this type of essay', 'A reason unrelated to application essays', 'Longer essays are always preferred regardless of any limits'], 0),
   ('Why might a specific, detailed anecdote be more effective than a general statement in this type of essay?', ['Specific details make the essay more memorable and help reveal genuine character', 'General statements are always more persuasive than specific details', 'Anecdotes have no place in an application essay', 'Detail and specificity never improve a piece of writing'], 0),
   ('Why is it important to carefully proofread a college or scholarship application essay?', ['Errors can distract from the content and create an unfavourable impression', 'Proofreading has no effect on how an essay is received', 'This type of essay does not require any proofreading', 'Errors in an application essay are never noticed by readers'], 0),
   ('Why might a writer reflect on personal growth or a challenge overcome in this type of essay?', ['It can demonstrate resilience and self-awareness valued by admissions or scholarship committees', 'Reflecting on personal growth has no place in this type of writing', 'A reason unrelated to application essays', 'Committees never consider personal growth when reviewing essays'], 0)]),
M('Rational Functions: Graphing and Asymptotes in Depth',
  'Grade 10 Functions strand (extension): graphing a rational function involves identifying vertical and horizontal asymptotes, which describe values the function approaches but never reaches.',
  [('A vertical asymptote of a rational function typically occurs where ___.', ['The denominator equals zero', 'The numerator equals zero', 'A location unrelated to the function’s denominator', 'The function crosses the x-axis'], 0),
   ('An asymptote describes a value that a function ___.', ['Approaches but never reaches', 'Always reaches and crosses repeatedly', 'A concept unrelated to rational functions', 'Reaches only at a single specific point and no other'], 0),
   ('For the function f(x) = 1/(x - 3), where is the vertical asymptote located?', ['x = 3', 'x = 0', 'A location unrelated to this function', 'x = -3'], 0),
   ('Why is it useful to identify a rational function’s asymptotes before graphing it?', ['Asymptotes provide key information about the function’s behaviour and shape near those values', 'Asymptotes provide no useful information about a function’s graph', 'Rational functions never have any asymptotes', 'Graphing a function never requires identifying asymptotes'], 0),
   ('Why might a rational function’s horizontal asymptote be useful in a real-world modelling context?', ['It can represent a long-term value or limit that a modelled quantity approaches over time', 'Horizontal asymptotes have no real-world interpretation', 'This concept only applies to purely abstract mathematics with no real-world use', 'Modelled quantities never approach a long-term limiting value'], 0)]),
Sc('Genetics: Mendelian Inheritance Patterns in Depth',
   'Grade 10 Biology strand: Mendelian inheritance describes how traits are passed from parents to offspring through dominant and recessive alleles, often illustrated using Punnett squares to predict genetic outcomes.',
   [('Mendelian inheritance describes how traits are passed from parents to offspring through ___.', ['Dominant and recessive alleles', 'A process unrelated to genetics', 'Random chance with no genetic basis at all', 'Environmental factors alone, with no connection to genes'], 0),
    ('A Punnett square is used to ___.', ['Predict the possible genetic outcomes of a cross between two parents', 'Measure the physical size of an organism', 'A tool unrelated to genetics', 'Determine the age of an organism'], 0),
    ('If both parents are heterozygous for a dominant trait, what fraction of their offspring would be expected to show the recessive trait?', ['One quarter', 'One half', 'A fraction unrelated to this cross', 'All of the offspring'], 0),
    ('A dominant allele is one that ___.', ['Is expressed in an organism’s traits when at least one copy is present', 'Is never expressed under any circumstances', 'A concept unrelated to inheritance patterns', 'Can only be expressed when two copies are present'], 0),
    ('Why is understanding Mendelian inheritance patterns useful in fields like agriculture or medicine?', ['It helps predict and understand how specific traits, including inherited conditions, are passed between generations', 'This concept has no practical application outside of a classroom', 'Mendelian inheritance has no connection to inherited traits', 'Genetics has no relevance to agriculture or medicine'], 0)]),
H('Canada’s Role in the Korean War',
  'Grade 10 History strand: Canada contributed troops and resources to the United Nations coalition during the 1950-1953 Korean War, marking a significant early Cold War military commitment.',
  [('The Korean War took place primarily between which years?', ['1950 and 1953', '1917 and 1919', '1970 and 1975', '1990 and 1995'], 0),
   ('Canada contributed troops and resources to the Korean War as part of ___.', ['The United Nations coalition', 'A conflict with no international involvement', 'An effort entirely unrelated to international cooperation', 'A purely domestic Canadian initiative'], 0),
   ('Why is Canada’s involvement in the Korean War considered historically significant?', ['It marked a significant early Cold War military commitment for Canada', 'Canada had no involvement in the Korean War', 'This event has no connection to Canada’s Cold War history', 'This topic has no relevance to understanding Canadian foreign policy'], 0),
   ('Why might studying the Korean War help explain Canada’s broader Cold War foreign policy?', ['It illustrates how Canada engaged militarily and diplomatically during early Cold War tensions', 'The Korean War has no connection to the Cold War', 'Canada’s foreign policy during this period had no international dimension', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians study Canada’s military contributions in conflicts like the Korean War?', ['They reveal how Canada’s role in international conflicts has evolved over time', 'Military contributions have no connection to a country’s historical development', 'Canada has never contributed troops to any international conflict', 'This topic has no relevance to Canadian history'], 0)])]),

day(53, [
E('Grammar: Rhetorical Devices in Argumentative Writing',
  'Grade 10 English strand: rhetorical devices, such as rhetorical questions, repetition, and the rule of three, are language techniques writers use to strengthen persuasion and emphasize key points in argumentative writing.',
  [('Rhetorical devices are language techniques used to ___.', ['Strengthen persuasion and emphasize key points', 'Weaken an argument’s overall persuasiveness', 'A concept unrelated to argumentative writing', 'Remove all emotional appeal from a piece of writing'], 0),
   ('A rhetorical question is a question that ___.', ['Is asked for effect rather than to receive a direct answer', 'Always requires a direct, factual answer from the reader', 'A concept unrelated to rhetorical devices', 'Has no persuasive purpose whatsoever'], 0),
   ('Which is an example of the rule of three as a rhetorical device?', ['“Government of the people, by the people, for the people.”', 'A single unrepeated statement with no listed items', 'A device unrelated to rhetorical technique', 'A statement using exactly two examples instead of three'], 0),
   ('Why might a writer use repetition as a rhetorical device in argumentative writing?', ['Repeating a key phrase can reinforce an idea and make it more memorable', 'Repetition always weakens the impact of an argument', 'This device has no place in argumentative writing', 'Repetition never affects how memorable an idea is'], 0),
   ('Why is it useful for readers to recognize rhetorical devices in a persuasive text?', ['It helps them critically evaluate how an argument is being constructed and its intended effect', 'Recognizing rhetorical devices never helps with understanding a text', 'A reason unrelated to reading comprehension', 'Rhetorical devices have no effect on how a reader interprets an argument'], 0)]),
M('Vectors in Three Dimensions',
  'Grade 10 Geometry strand (extension): a vector in three dimensions extends the two-dimensional concept by adding a third component, allowing magnitude and direction to be described in space rather than on a flat plane.',
  [('A vector in three dimensions extends the two-dimensional concept by adding ___.', ['A third component', 'An entirely new type of number system', 'A concept unrelated to vectors', 'A fourth and fifth component simultaneously'], 0),
   ('A three-dimensional vector can be described using components along the ___.', ['x, y, and z axes', 'x-axis only, with no other components', 'A description unrelated to spatial direction', 'Only two axes, identical to a 2D vector'], 0),
   ('Why might three-dimensional vectors be necessary for describing motion in real-world physical space?', ['Real-world motion often occurs across three spatial dimensions, not just a flat plane', 'Three-dimensional vectors have no practical use for describing motion', 'Motion in physical space never involves more than two dimensions', 'This concept only applies to purely abstract mathematics with no real-world use'], 0),
   ('Why is it useful to calculate the magnitude of a three-dimensional vector?', ['It provides the overall length or size of the vector, regardless of its individual components', 'Magnitude has no meaning for a three-dimensional vector', 'Three-dimensional vectors never have a measurable magnitude', 'This calculation has no connection to describing vectors'], 0),
   ('Why might three-dimensional vectors be relevant to fields like engineering or computer graphics?', ['These fields often require precisely modelling positions, forces, or movement in three-dimensional space', 'Three-dimensional vectors have no application in engineering or computer graphics', 'These fields never require any mathematical modelling of space', 'This concept has no relevance outside of a mathematics classroom'], 0)]),
Sc('Physics: Projectile Motion in Two Dimensions',
   'Grade 10 Physics strand: projectile motion describes the curved path of an object launched into the air, combining constant horizontal velocity with the effect of vertical acceleration due to gravity.',
   [('Projectile motion combines constant horizontal velocity with ___.', ['Vertical acceleration due to gravity', 'A second, separate horizontal acceleration', 'A concept unrelated to motion in the air', 'No vertical motion at all'], 0),
    ('The horizontal velocity of a projectile, ignoring air resistance, generally remains ___.', ['Constant throughout its flight', 'Constantly increasing throughout its flight', 'A value unrelated to projectile motion', 'Zero throughout its entire flight'], 0),
    ('Why does a projectile follow a curved, rather than straight-line, path?', ['Gravity continuously accelerates the object downward while it also moves horizontally', 'Projectiles never experience the effect of gravity', 'This path has no connection to the forces acting on the object', 'A curved path only occurs when horizontal velocity is zero'], 0),
    ('Which of these is an example of projectile motion?', ['A ball thrown at an angle into the air', 'An object sitting completely still on the ground', 'A concept unrelated to projectile motion', 'An object moving in a perfectly straight horizontal line with no vertical component'], 0),
    ('Why is understanding projectile motion useful in fields like sports science or engineering?', ['It helps predict and optimize the path of objects launched or thrown through the air', 'Projectile motion has no practical, real-world applications', 'These fields never involve analyzing the motion of objects', 'This concept only applies to purely theoretical physics problems'], 0)]),
H('The Avro Arrow Cancellation and Its Legacy',
  'Grade 10 History strand: the 1959 cancellation of the Avro Arrow, an advanced Canadian-designed fighter jet, remains a controversial decision often discussed in relation to Canada’s aerospace industry and sovereignty.',
  [('The Avro Arrow was cancelled in which year?', ['1959', '1919', '1945', '1970'], 0),
   ('The Avro Arrow was best described as ___.', ['An advanced Canadian-designed fighter jet', 'A type of civilian passenger aircraft', 'A concept unrelated to Canadian aerospace history', 'A ship built for the Canadian navy'], 0),
   ('Why is the cancellation of the Avro Arrow often considered controversial?', ['It ended a highly advanced Canadian aerospace project, raising questions about lost economic and technological opportunity', 'This decision was universally supported with no debate or controversy', 'The Avro Arrow’s cancellation had no significant effect on Canada', 'This event has no connection to Canadian aerospace history'], 0),
   ('Why might historians connect the Avro Arrow’s cancellation to discussions of Canadian sovereignty?', ['The decision raised questions about Canada’s independent technological and defence capabilities', 'The Avro Arrow has no connection to questions of sovereignty', 'This event has no relevance to Canadian defence policy', 'Sovereignty was never a topic of discussion in Canadian history'], 0),
   ('Why do historians and engineers continue to study the Avro Arrow program today?', ['It offers insight into Canada’s technological ambitions and the complexities of large defence decisions', 'This program has no lasting historical significance', 'The Avro Arrow has no connection to Canada’s aerospace industry', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(54, [
E('Literature: Exploring Absurdist Fiction',
  'Grade 10 English strand: absurdist fiction presents illogical or nonsensical situations to explore themes about the apparent meaninglessness or unpredictability of existence, often provoking reflection through its strangeness.',
  [('Absurdist fiction typically presents ___.', ['Illogical or nonsensical situations', 'Only strictly realistic, logical events', 'A concept unrelated to fiction', 'A setting with no unusual or unexpected elements'], 0),
   ('Absurdist fiction often explores themes related to ___.', ['The apparent meaninglessness or unpredictability of existence', 'Only lighthearted, comedic subject matter with no deeper meaning', 'A topic unrelated to existence or meaning', 'Strictly logical, orderly systems with no ambiguity'], 0),
   ('Why might an author use absurdist elements instead of a more realistic approach?', ['Strangeness or illogic can provoke reflection and highlight ideas that realism might not capture as effectively', 'Absurdist elements always make a story less meaningful', 'Realistic approaches are always superior to absurdist ones', 'Absurdist fiction has no connection to provoking reader reflection'], 0),
   ('Which is a common technique found in absurdist fiction?', ['Presenting a character in a bizarre situation with no clear logical explanation', 'Providing a clear, fully logical explanation for every event', 'A technique unrelated to absurdist fiction', 'Avoiding any strange or unexpected elements entirely'], 0),
   ('Why might absurdist fiction be considered a valuable lens for examining real-world uncertainty?', ['Its illogical scenarios can mirror feelings of confusion or unpredictability found in real life', 'Absurdist fiction has no connection to real-world experiences', 'This genre never engages with themes relevant to readers', 'Uncertainty is never a meaningful theme in literature'], 0)]),
M('The Binomial Theorem and Pascal’s Triangle',
  'Grade 10 Number strand (extension): the binomial theorem provides a method for expanding expressions like (a + b) raised to a power, and Pascal’s triangle offers a visual way to determine the coefficients used in that expansion.',
  [('The binomial theorem provides a method for expanding expressions like ___.', ['(a + b) raised to a power', 'A single variable with no exponent at all', 'A concept unrelated to algebraic expansion', 'Only expressions involving subtraction, with no addition'], 0),
   ('Pascal’s triangle can be used to determine the ___.', ['Coefficients used in a binomial expansion', 'Exact roots of any polynomial equation', 'A concept unrelated to binomial expansion', 'Only the exponents in an expression, with no connection to coefficients'], 0),
   ('In Pascal’s triangle, each number is found by ___.', ['Adding the two numbers directly above it', 'Multiplying the two numbers directly above it', 'A method unrelated to Pascal’s triangle', 'Subtracting the row number from itself'], 0),
   ('What are the coefficients for the expansion of (a + b) squared?', ['1, 2, 1', '1, 1, 1', 'A set of values unrelated to this expansion', '2, 2, 2'], 0),
   ('Why might the binomial theorem be useful in fields like probability?', ['It can help efficiently calculate the number of ways certain outcomes can occur', 'The binomial theorem has no connection to probability', 'This theorem only applies to purely abstract algebra with no other use', 'Probability calculations never involve expanding expressions'], 0)]),
Sc('The Chemistry of Polymers and Plastics',
   'Grade 10 Chemistry strand: polymers are large molecules made of repeating smaller units called monomers, and synthetic polymers like plastics are widely used but raise important questions about environmental sustainability.',
   [('A polymer is best described as a large molecule made of ___.', ['Repeating smaller units called monomers', 'A single, non-repeating unit with no smaller components', 'A concept unrelated to molecular structure', 'Only inorganic minerals with no organic connection'], 0),
    ('The smaller repeating units that make up a polymer are called ___.', ['Monomers', 'Isotopes', 'A term unrelated to polymer structure', 'Electrons'], 0),
    ('Which of these is an example of a synthetic polymer?', ['Plastic', 'A pure metal with no polymer structure', 'A substance entirely unrelated to polymer chemistry', 'A single, unbonded atom'], 0),
    ('Why do synthetic polymers like plastics raise concerns about environmental sustainability?', ['Many plastics take a very long time to break down, contributing to long-term pollution', 'Plastics have no connection to environmental concerns', 'All synthetic polymers break down immediately with no environmental impact', 'This topic has no relevance to chemistry or sustainability'], 0),
    ('Why is understanding polymer chemistry useful for developing more sustainable materials?', ['It can help chemists design polymers that break down more easily or use fewer harmful resources', 'Polymer chemistry has no connection to sustainability efforts', 'Sustainable materials can never be developed using chemistry', 'This field of study has no practical, real-world applications'], 0)]),
H('The Suez Crisis and the Birth of Peacekeeping (Lester Pearson)',
  'Grade 10 History strand: the 1956 Suez Crisis was a major international conflict during which Canadian diplomat Lester Pearson helped establish the first large-scale United Nations peacekeeping force, later earning him the Nobel Peace Prize.',
  [('The Suez Crisis took place in which year?', ['1956', '1919', '1970', '1995'], 0),
   ('Lester Pearson is closely associated with helping establish ___.', ['The first large-scale United Nations peacekeeping force', 'A conflict with no connection to peacekeeping', 'An organization unrelated to international diplomacy', 'A purely domestic Canadian policy initiative'], 0),
   ('Lester Pearson’s role during the Suez Crisis later earned him ___.', ['The Nobel Peace Prize', 'No international recognition of any kind', 'An award unrelated to peacekeeping or diplomacy', 'A prize unrelated to his diplomatic work'], 0),
   ('Why is the Suez Crisis considered significant in the history of international peacekeeping?', ['It led to the creation of a new model for United Nations peacekeeping missions', 'This event had no connection to the development of peacekeeping', 'Peacekeeping missions existed long before this event with no relation to it', 'This crisis has no lasting historical significance'], 0),
   ('Why might Canada’s role in the Suez Crisis be a significant point of national pride?', ['It highlighted Canada’s influence in shaping international diplomacy and peacekeeping', 'Canada had no meaningful role in the Suez Crisis', 'This event has no connection to Canadian foreign policy history', 'This topic has no relevance to understanding Canada’s global reputation'], 0)])]),

day(55, [
E('Media Literacy: Analyzing Documentary Filmmaking Techniques',
  'Grade 10 English strand: documentary filmmakers use techniques such as interviews, archival footage, narration, and editing choices to shape a persuasive or informative perspective on real events.',
  [('Documentary filmmakers often use techniques such as ___.', ['Interviews, archival footage, narration, and editing choices', 'Only completely unscripted, unedited footage with no other elements', 'A concept unrelated to documentary filmmaking', 'Purely fictional scenes with no connection to real events'], 0),
   ('Why might the specific editing choices in a documentary influence how a viewer interprets an event?', ['The order and selection of footage can shape which details and perspectives are emphasized', 'Editing has no effect on how a documentary is perceived', 'All documentaries present information in an identical, unedited way', 'This factor is irrelevant to understanding documentary film'], 0),
   ('Why is narration often an important element to analyze in a documentary?', ['The narrator’s tone and word choice can guide the audience toward a particular interpretation', 'Narration has no influence on how a documentary is understood', 'Documentaries never include any narration', 'This element has no connection to persuasive or informative filmmaking'], 0),
   ('Which is an example of a technique used to build credibility in a documentary?', ['Including interviews with relevant experts or eyewitnesses', 'Avoiding any interviews or outside perspectives entirely', 'A technique unrelated to building credibility', 'Presenting only unsupported personal opinions with no evidence'], 0),
   ('Why is it valuable to critically analyze documentary filmmaking techniques as a media literacy skill?', ['It helps viewers recognize how factual content can still be shaped by creative and persuasive choices', 'Critical analysis of documentaries has no value for media literacy', 'Documentaries always present information in a completely neutral way', 'This skill has no connection to understanding media today'], 0)]),
M('Piecewise and Step Functions',
  'Grade 10 Functions strand (extension): a piecewise function is defined by different expressions over different intervals of its domain, and a step function is a specific type of piecewise function whose graph looks like a series of horizontal steps.',
  [('A piecewise function is defined by ___.', ['Different expressions over different intervals of its domain', 'A single expression that applies across its entire domain', 'A concept unrelated to functions', 'No defined expression at all'], 0),
   ('A step function’s graph typically looks like a series of ___.', ['Horizontal steps', 'A single smooth, continuous curve', 'A concept unrelated to step functions', 'Diagonal lines with no flat sections'], 0),
   ('Which of these is a real-world example that could be modelled with a step function?', ['The cost of parking, which increases by a fixed amount for each additional hour', 'A quantity that changes smoothly and continuously with no sudden jumps', 'A concept unrelated to step functions', 'A situation with no connection to changing values'], 0),
   ('Why might a piecewise function be useful for modelling a situation where a rule changes under certain conditions?', ['It allows different expressions to apply depending on the specific interval or condition', 'Piecewise functions can never represent a rule that changes', 'This type of function has no real-world modelling use', 'A single expression can always represent any changing rule with no need for a piecewise function'], 0),
   ('Why is it important to pay attention to the domain restrictions when graphing a piecewise function?', ['Each piece of the function is only valid, and should only be graphed, within its specified interval', 'Domain restrictions have no effect on how a piecewise function is graphed', 'Piecewise functions never have any domain restrictions', 'Every piece of the function applies across the entire domain regardless of any restriction'], 0)]),
Sc('Biology: The Nervous System and Neurotransmission',
   'Grade 10 Biology strand: the nervous system coordinates the body’s responses using neurons that communicate through electrical and chemical signals, including neurotransmitters that cross the synapse between cells.',
   [('The nervous system coordinates the body’s responses using ___.', ['Neurons that communicate through electrical and chemical signals', 'A process unrelated to communication between cells', 'Only mechanical movement, with no signalling involved', 'A single organ with no connection to other body systems'], 0),
    ('Neurotransmitters are chemical messengers that ___.', ['Cross the synapse between neurons to transmit a signal', 'Have no role in communication between neurons', 'A concept unrelated to the nervous system', 'Only function within a single neuron, with no connection to other cells'], 0),
    ('The small gap between two neurons, across which a signal is transmitted, is called the ___.', ['Synapse', 'Cortex', 'A structure unrelated to neurons', 'Ventricle'], 0),
    ('Why is the nervous system essential for the body’s ability to respond to its environment?', ['It allows for rapid communication and coordination between different parts of the body', 'The nervous system has no connection to how the body responds to stimuli', 'The body can respond to its environment with no involvement from the nervous system', 'This concept has no relevance to biological function'], 0),
    ('Why might understanding neurotransmission be important for studying certain medical conditions?', ['Many conditions are linked to imbalances or disruptions in how neurotransmitters function', 'Neurotransmission has no connection to any medical conditions', 'Medical conditions are never related to the nervous system', 'This field of study has no relevance to human health'], 0)]),
H('The Employment Equity Act and Workplace Diversity',
  'Grade 10 History strand: the 1986 Employment Equity Act aimed to address workplace discrimination in Canada by promoting equal opportunity for groups historically underrepresented in the workforce, including women, Indigenous peoples, persons with disabilities, and visible minorities.',
  [('The Employment Equity Act was introduced in which year?', ['1986', '1919', '1945', '1970'], 0),
   ('The Employment Equity Act aimed to address ___.', ['Workplace discrimination and promote equal opportunity for underrepresented groups', 'A topic entirely unrelated to workplace conditions', 'Only issues affecting a single industry, with no broader application', 'A reduction in workplace protections for underrepresented groups'], 0),
   ('Which of these groups is specifically addressed by the Employment Equity Act?', ['Women, Indigenous peoples, persons with disabilities, and visible minorities', 'A group unrelated to workplace discrimination', 'Only a single demographic group, with no others considered', 'No specific groups are addressed by this legislation'], 0),
   ('Why is legislation like the Employment Equity Act considered historically significant?', ['It represented a formal effort to address systemic inequality in Canadian workplaces', 'This legislation had no impact on workplace conditions in Canada', 'The Employment Equity Act has no connection to addressing discrimination', 'This topic has no relevance to understanding Canadian labour history'], 0),
   ('Why do historians study legislation like the Employment Equity Act alongside broader social movements?', ['It shows how legal changes can both reflect and reinforce shifting social values around equity', 'Legislation has no connection to broader social movements', 'Social movements never influence the development of Canadian law', 'This topic has no relevance to Canadian history'], 0)])]),

day(56, [
E('Reading: Analyzing Epistolary Narratives (Letters and Diaries)',
  'Grade 10 English strand: an epistolary narrative tells a story through a series of documents, such as letters or diary entries, offering an intimate, first-person perspective shaped by the format itself.',
  [('An epistolary narrative tells a story through a series of ___.', ['Documents, such as letters or diary entries', 'Only third-person, objective narration', 'A concept unrelated to narrative structure', 'A single uninterrupted scene with no separate documents'], 0),
   ('Why might an epistolary format create a particularly intimate reading experience?', ['It presents a first-person perspective that can feel like a direct, personal window into a character’s thoughts', 'This format always creates emotional distance between the reader and the character', 'The epistolary format has no effect on how a reader experiences a story', 'A concept unrelated to narrative perspective'], 0),
   ('Which of these is a potential limitation of an epistolary narrative?', ['Readers only know what a character chooses to include in their letters or entries', 'This format always provides complete, objective information about every event', 'A limitation unrelated to epistolary narratives', 'Epistolary narratives have no potential limitations at all'], 0),
   ('Why might multiple correspondents’ letters be used together in a single epistolary novel?', ['It allows readers to see different perspectives on the same events', 'Using multiple correspondents never adds any additional perspective', 'A reason unrelated to epistolary narratives', 'This technique only works with a single narrator throughout'], 0),
   ('Why do some contemporary novels use modern formats, like text messages or emails, in an epistolary style?', ['They can update the traditional letter-based format to reflect how people communicate today', 'Modern communication formats can never be used in an epistolary narrative', 'This technique has no connection to the original epistolary tradition', 'Contemporary novels never experiment with narrative format'], 0)]),
M('Systems of Equations with Three Variables',
  'Grade 10 Algebra strand (extension): a system of equations with three variables can be solved by systematically eliminating variables through substitution or elimination until a single variable’s value is found.',
  [('A system of equations with three variables requires finding values that satisfy ___.', ['All of the equations in the system simultaneously', 'Only one of the equations, with no connection to the others', 'A concept unrelated to systems of equations', 'None of the equations in the system'], 0),
   ('Solving a three-variable system often involves systematically ___.', ['Eliminating variables until a single variable’s value is found', 'Ignoring two of the three variables entirely', 'A method unrelated to solving systems of equations', 'Adding a fourth variable to simplify the system'], 0),
   ('Why might elimination be a useful strategy for solving a three-variable system?', ['It can reduce the system to two equations with two variables, making it easier to solve', 'Elimination never simplifies a system of equations', 'This method has no connection to solving systems of equations', 'Elimination only works with a single-variable equation'], 0),
   ('Once the value of one variable is found in a three-variable system, what is typically done next?', ['That value is substituted back into other equations to solve for the remaining variables', 'The solving process is considered complete with no further steps needed', 'A step unrelated to solving systems of equations', 'The value is discarded and the system must be solved again from scratch'], 0),
   ('Why might a three-variable system be useful for modelling a real-world situation with multiple unknown quantities?', ['It allows several related unknowns to be solved for at the same time using multiple given relationships', 'Three-variable systems have no real-world modelling application', 'Real-world situations never involve more than one unknown quantity', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Earth Science: Weathering and Erosion Processes',
   'Grade 10 Earth Science strand: weathering breaks down rock and minerals in place, while erosion transports the resulting sediment elsewhere, together gradually reshaping Earth’s surface over time.',
   [('Weathering refers to the process of ___.', ['Breaking down rock and minerals in place', 'Transporting sediment from one location to another', 'A concept unrelated to Earth’s surface', 'Forming entirely new rock with no connection to existing material'], 0),
    ('Erosion refers to the process of ___.', ['Transporting sediment from one location to another', 'Breaking down rock and minerals in place, with no transportation involved', 'A concept unrelated to weathering', 'Forming mountains with no connection to sediment movement'], 0),
    ('Which of these is an example of a weathering process?', ['Ice expanding in the cracks of a rock, causing it to break apart', 'Wind carrying sand from one location to another', 'A process unrelated to breaking down rock', 'A river depositing sediment at its mouth'], 0),
    ('Why do weathering and erosion often work together to shape landscapes over time?', ['Weathering breaks down material that erosion then transports, gradually reshaping the land', 'Weathering and erosion never occur together in the same location', 'These two processes have no connection to one another', 'Landscapes are shaped with no involvement from either process'], 0),
    ('Why is understanding weathering and erosion important for managing land use, such as farming or construction?', ['It helps predict how landscapes may change and informs decisions about stable and sustainable land use', 'These processes have no connection to land use decisions', 'Weathering and erosion never affect how land can be used', 'This concept has no relevance to Earth science or geography'], 0)]),
H('Same-Sex Marriage Legalization in Canada',
  'Grade 10 History strand: Canada legalized same-sex marriage nationwide in 2005 through the Civil Marriage Act, making it one of the first countries in the world to do so, following a series of provincial court rulings.',
  [('Canada legalized same-sex marriage nationwide in which year?', ['2005', '1970', '1945', '1990'], 0),
   ('Same-sex marriage in Canada was legalized nationwide through ___.', ['The Civil Marriage Act', 'An act entirely unrelated to marriage rights', 'A decision made with no formal legislation at all', 'A law that had no connection to LGBTQ rights'], 0),
   ('Before nationwide legalization, same-sex marriage rights in Canada were first established through ___.', ['A series of provincial court rulings', 'No legal process at all', 'A method entirely unrelated to Canadian law', 'A single national referendum with no court involvement'], 0),
   ('Why is Canada’s legalization of same-sex marriage considered historically significant?', ['It made Canada one of the first countries in the world to legalize same-sex marriage nationwide', 'This event had no significance in Canadian legal history', 'Same-sex marriage has no connection to Canadian civil rights history', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians connect the legalization of same-sex marriage to broader human rights movements in Canada?', ['It reflects a continued expansion of legal rights and recognition for previously marginalized groups', 'This event has no connection to broader human rights movements', 'Human rights movements never influenced Canadian legislation', 'This topic has no relevance to Canadian legal or social history'], 0)])]),

day(57, [
E('Writing: The Extended Definition Essay',
  'Grade 10 English strand: an extended definition essay explores the full meaning of a complex or abstract term by using examples, comparisons, and context beyond a simple dictionary definition.',
  [('An extended definition essay explores the full meaning of a term by using ___.', ['Examples, comparisons, and context', 'Only a single, brief dictionary definition with no further explanation', 'A concept unrelated to defining a term', 'A definition with no connection to the term’s actual meaning'], 0),
   ('Why might a writer choose to write an extended definition essay about an abstract term, like “courage” or “success”?', ['Abstract terms often have complex, personal, or contested meanings that benefit from deeper exploration', 'Abstract terms never require any further explanation', 'This type of essay only works for simple, concrete terms', 'Abstract terms have no meaning worth exploring in an essay'], 0),
   ('Which is an example of a technique a writer might use in an extended definition essay?', ['Comparing the term to a related but distinct concept', 'Providing only a single sentence with no further elaboration', 'A technique unrelated to extended definition writing', 'Avoiding any examples or context entirely'], 0),
   ('Why might a writer include what a term does not mean as part of an extended definition essay?', ['Contrasting a term with what it is not can help clarify and sharpen its actual meaning', 'This approach never helps clarify a term’s meaning', 'A reason unrelated to extended definition writing', 'Only a term’s literal, dictionary definition should ever be discussed'], 0),
   ('Why is context especially important when writing an extended definition of a term?', ['A term’s meaning can shift depending on the situation or perspective in which it is used', 'Context never affects the meaning of a term', 'A term has exactly one meaning that never changes based on context', 'This factor has no connection to extended definition writing'], 0)]),
M('Permutations and Combinations: Advanced Applications',
  'Grade 10 Data Management strand (extension): a permutation counts the number of ways items can be arranged when order matters, while a combination counts the number of ways items can be selected when order does not matter.',
  [('A permutation counts the number of ways items can be arranged when ___.', ['Order matters', 'Order does not matter at all', 'A concept unrelated to counting arrangements', 'Only a single item is being arranged'], 0),
   ('A combination counts the number of ways items can be selected when ___.', ['Order does not matter', 'Order always matters', 'A concept unrelated to counting selections', 'No items are actually being selected'], 0),
   ('Which of these situations would use a combination rather than a permutation?', ['Selecting 3 students for a committee from a group of 10, with no distinct roles', 'Arranging 3 different trophies in a specific order on a shelf', 'A situation unrelated to counting outcomes', 'Assigning first, second, and third place in a race'], 0),
   ('Why is it important to determine whether order matters before solving a counting problem?', ['It determines whether a permutation or combination formula should be used, which can produce very different results', 'Order never affects which counting method should be used', 'Permutations and combinations always produce identical results', 'This distinction has no relevance to solving counting problems'], 0),
   ('Why are permutations and combinations useful in real-world situations, such as determining possible outcomes in a lottery or scheduling?', ['They provide an efficient way to count large numbers of possible outcomes without listing them all individually', 'These concepts have no real-world counting applications', 'Real-world scheduling and lottery problems never require any counting method', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Physics: Simple Harmonic Motion (Pendulums and Springs)',
   'Grade 10 Physics strand: simple harmonic motion describes a repeating back-and-forth movement, such as a swinging pendulum or an oscillating spring, where the restoring force is proportional to the displacement from equilibrium.',
   [('Simple harmonic motion describes a repeating movement that is best characterized as ___.', ['Back-and-forth around a central equilibrium point', 'A motion that only ever occurs in a single direction with no repetition', 'A concept unrelated to periodic motion', 'A completely random, unpredictable movement'], 0),
    ('Which of these is a common example of simple harmonic motion?', ['A pendulum swinging back and forth', 'An object moving in a perfectly straight line with no repeating pattern', 'A concept unrelated to simple harmonic motion', 'An object that remains completely stationary'], 0),
    ('In simple harmonic motion, the restoring force is proportional to ___.', ['The displacement from equilibrium', 'The colour of the oscillating object', 'A factor unrelated to the object’s position', 'The temperature of the surrounding environment'], 0),
    ('Why does a pendulum eventually slow down and stop swinging in a real-world setting?', ['Friction and air resistance gradually remove energy from the system', 'Pendulums never lose any energy while swinging', 'A reason unrelated to simple harmonic motion', 'A pendulum’s motion has no connection to energy at all'], 0),
    ('Why is understanding simple harmonic motion useful for designing devices like clocks or shock absorbers?', ['It helps engineers predict and control repeating, oscillating movement in these devices', 'Simple harmonic motion has no practical, real-world applications', 'These devices never rely on any repeating or oscillating motion', 'This concept only applies to purely theoretical physics problems'], 0)]),
H('The National Energy Program and Federal-Provincial Tension',
  'Grade 10 History strand: the 1980 National Energy Program was a federal policy aimed at increasing Canadian control over the oil industry, which created significant tension with western provinces, particularly Alberta.',
  [('The National Energy Program was introduced in which year?', ['1980', '1919', '1945', '1995'], 0),
   ('The National Energy Program was primarily aimed at increasing Canadian control over the ___.', ['Oil industry', 'Fishing industry, with no connection to energy', 'A sector entirely unrelated to energy policy', 'Automotive manufacturing industry'], 0),
   ('The National Energy Program created significant tension with ___.', ['Western provinces, particularly Alberta', 'No provinces at all', 'A region entirely unrelated to the energy sector', 'Only eastern Canadian provinces, with no involvement from the west'], 0),
   ('Why is the National Energy Program often cited as an example of federal-provincial tension in Canadian history?', ['It illustrates conflicts that can arise between federal economic policy and provincial resource interests', 'This policy had no effect on the relationship between federal and provincial governments', 'The National Energy Program has no connection to federal-provincial relations', 'This topic has no relevance to understanding Canadian political history'], 0),
   ('Why do historians continue to study the National Energy Program and its aftermath?', ['It offers insight into ongoing debates about regionalism and resource control in Canadian federalism', 'This policy has no lasting historical significance', 'Federal-provincial tension has never been a meaningful issue in Canadian history', 'This topic has no relevance to understanding modern Canada'], 0)])]),

day(58, [
E('Oral Communication: Impromptu Speaking Skills', 'Grade 10 English strand: impromptu speaking involves organizing and delivering a coherent response to a topic with little or no preparation time, relying on quick thinking and a clear structure.',
  [('Impromptu speaking involves delivering a response to a topic ___.', ['With little or no preparation time', 'After extensive research and days of preparation', 'A concept unrelated to public speaking', 'Only when a full written script is available in advance'], 0),
   ('Why might a speaker use a simple structure, such as stating a point and then giving a supporting reason, during an impromptu speech?', ['A clear structure helps organize thoughts quickly and keeps the response coherent under time pressure', 'Structure is never useful when speaking without preparation', 'A reason unrelated to impromptu speaking', 'Impromptu speeches are always more effective with no structure at all'], 0),
   ('Which is a useful strategy for managing nervousness during impromptu speaking?', ['Taking a brief moment to gather thoughts before beginning to speak', 'Speaking as quickly as possible with no pause at all', 'A strategy unrelated to managing nervousness', 'Avoiding eye contact with the audience entirely throughout the speech'], 0),
   ('Why is impromptu speaking considered a valuable skill beyond the classroom?', ['Many real-world situations, like interviews or meetings, require thinking and responding on the spot', 'This skill has no application outside of a classroom setting', 'Impromptu speaking is never a realistic or useful skill', 'A reason unrelated to public speaking or communication'], 0),
   ('Why might practising impromptu speaking regularly help build a speaker’s overall confidence?', ['Repeated practice can make organizing thoughts quickly feel more natural and less intimidating', 'Practice has no effect on a speaker’s confidence or ability', 'Impromptu speaking skills can never be improved through practice', 'This concept has no connection to developing communication skills'], 0)]),
M('Polynomial Division and the Remainder Theorem',
  'Grade 10 Number strand (extension): polynomial division follows a process similar to long division with numbers, and the remainder theorem states that dividing a polynomial by (x - a) gives a remainder equal to the polynomial evaluated at a.',
  [('Polynomial division follows a process similar to ___.', ['Long division with numbers', 'A method entirely unrelated to division', 'Simple multiplication with no connection to division', 'A process that only applies to single-term expressions'], 0),
   ('The remainder theorem states that dividing a polynomial by (x - a) gives a remainder equal to ___.', ['The polynomial evaluated at a', 'The value of a alone, with no connection to the polynomial', 'A concept unrelated to polynomial division', 'Zero, in every possible case'], 0),
   ('If a polynomial p(x) is divided by (x - 2) and p(2) = 0, what does this indicate about the division?', ['There is no remainder, meaning (x - 2) is a factor of the polynomial', 'The division is impossible to carry out', 'A conclusion unrelated to the remainder theorem', 'The remainder must be a very large number'], 0),
   ('Why is the remainder theorem a useful shortcut compared to performing full polynomial long division?', ['It allows the remainder to be found quickly by substituting a single value, without completing the entire division process', 'The remainder theorem never provides a shortcut for finding a remainder', 'This theorem has no connection to polynomial division', 'Full long division is always faster than using the remainder theorem'], 0),
   ('Why is polynomial division useful when working with more complex polynomial expressions?', ['It can help simplify or factor expressions that would otherwise be difficult to work with directly', 'Polynomial division has no useful application when working with complex expressions', 'Complex polynomial expressions never require any division or simplification', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Chemistry: Gas Laws (Boyle’s, Charles’s, Combined)',
   'Grade 10 Chemistry strand: gas laws describe the mathematical relationships between a gas’s pressure, volume, and temperature, including Boyle’s law (pressure and volume) and Charles’s law (volume and temperature).',
   [('Boyle’s law describes the relationship between a gas’s ___.', ['Pressure and volume', 'Mass and colour', 'A relationship unrelated to gas behaviour', 'Only its chemical formula, with no physical properties involved'], 0),
    ('Charles’s law describes the relationship between a gas’s ___.', ['Volume and temperature', 'Pressure and mass', 'A relationship unrelated to gas behaviour', 'Colour and density'], 0),
    ('According to Boyle’s law, if the volume of a gas decreases while temperature remains constant, its pressure will generally ___.', ['Increase', 'Decrease', 'Remain completely unchanged', 'Become impossible to determine'], 0),
    ('The combined gas law integrates the relationships between ___.', ['Pressure, volume, and temperature', 'Only pressure, with no other variables', 'A relationship unrelated to gas laws', 'Mass and density alone, with no connection to gas behaviour'], 0),
    ('Why are gas laws useful in real-world applications, such as scuba diving or weather forecasting?', ['They help predict how gases will behave under changing pressure, volume, or temperature conditions', 'Gas laws have no practical, real-world applications', 'These fields never involve any changes in pressure, volume, or temperature', 'This concept only applies to purely theoretical chemistry problems'], 0)]),
H('Japanese Canadian Internment: Redress and Legacy',
  'Grade 10 History strand: following the forced internment of Japanese Canadians during World War II, the Canadian government issued a formal apology and financial redress in 1988, acknowledging the injustice of these wartime policies.',
  [('The Canadian government issued a formal apology and financial redress for Japanese Canadian internment in which year?', ['1988', '1945', '1970', '1919'], 0),
   ('The redress for Japanese Canadian internment acknowledged the injustice of policies enacted during ___.', ['World War II', 'World War I', 'A conflict entirely unrelated to internment', 'The Cold War'], 0),
   ('Why is the redress for Japanese Canadian internment considered historically significant?', ['It represented a formal government acknowledgment of a serious historical injustice', 'This event had no significance in Canadian history', 'The redress has no connection to Japanese Canadian history', 'This topic has no relevance to understanding Canadian civil rights'], 0),
   ('Why might studying the redress movement help explain broader efforts toward historical accountability in Canada?', ['It illustrates how affected communities can advocate for formal recognition of past injustices', 'The redress movement has no connection to broader historical accountability efforts', 'Communities affected by historical injustice never advocate for recognition', 'This topic has no relevance to Canadian history'], 0),
   ('Why do historians continue to study the internment of Japanese Canadians and its redress today?', ['It offers important lessons about civil liberties, wartime policy, and the process of reconciliation', 'This topic has no lasting relevance to understanding Canadian history', 'The internment of Japanese Canadians has been entirely forgotten with no historical record', 'This event has no connection to Canadian civil rights history'], 0)])]),

day(59, [
E('Literature: War Literature and Testimony',
  'Grade 10 English strand: war literature and testimony present firsthand or fictionalized accounts of conflict, often exploring themes of trauma, survival, and the human cost of war through personal perspective.',
  [('War literature and testimony often present ___.', ['Firsthand or fictionalized accounts of conflict', 'Only purely statistical, impersonal reports of conflict', 'A concept unrelated to human experience', 'Accounts entirely unrelated to war or conflict'], 0),
   ('Which is a common theme explored in war literature?', ['The human cost of war and its impact on survivors', 'A theme entirely unrelated to conflict or its consequences', 'Only the technical details of military strategy, with no human element', 'A topic unrelated to trauma or survival'], 0),
   ('Why might a firsthand account, or testimony, be considered a particularly powerful form of war literature?', ['It offers a direct, personal perspective that can convey the emotional reality of experiencing conflict', 'Firsthand accounts are always less meaningful than fictionalized versions of events', 'Testimony has no connection to conveying the experience of war', 'A reason unrelated to war literature'], 0),
   ('Why might an author choose a fictionalized account rather than a strict historical record to explore a war experience?', ['Fiction can allow for exploring universal emotional truths that may not fit within a strict historical account', 'Fictionalized accounts are never used to explore real historical events', 'This choice has no connection to how war literature conveys meaning', 'A strict historical record is always the only valid way to represent war'], 0),
   ('Why is studying war literature and testimony considered valuable, even for readers with no direct experience of conflict?', ['It can build empathy and deepen understanding of the lasting human impact of war', 'This type of literature provides no meaningful insight for readers', 'War literature has no connection to broader human experience', 'A reason unrelated to reading and literary study'], 0)]),
M('Rates of Change: Average vs Instantaneous (Intro to Calculus Concepts)',
  'Grade 10 Functions strand (extension): the average rate of change measures how a quantity changes over an interval, while the instantaneous rate of change estimates how a quantity is changing at a single specific point.',
  [('The average rate of change measures how a quantity changes ___.', ['Over an interval', 'At a single specific point only', 'A concept unrelated to functions', 'Only when the quantity remains completely constant'], 0),
   ('The instantaneous rate of change estimates how a quantity is changing ___.', ['At a single specific point', 'Only across the entire domain of the function, with no connection to a specific point', 'A concept unrelated to rates of change', 'Over an extremely long, unspecified interval'], 0),
   ('The average rate of change between two points on a graph can be found using ___.', ['The slope of the line connecting those two points', 'Only the y-coordinate of a single point', 'A method unrelated to average rate of change', 'The sum of both x-coordinates alone'], 0),
   ('Why might the instantaneous rate of change be approximated using very small intervals around a point?', ['Using increasingly smaller intervals can give a closer estimate of the rate of change at that exact point', 'Smaller intervals never improve the accuracy of this type of estimate', 'This method has no connection to estimating instantaneous rate of change', 'Instantaneous rate of change can only ever be measured using a very large interval'], 0),
   ('Why are these introductory rate of change concepts considered a foundation for later calculus study?', ['They introduce the core idea of analyzing how a quantity changes, which calculus builds upon in greater depth', 'These concepts have no connection to calculus', 'Calculus never involves analyzing rates of change', 'This topic has no relevance to higher-level mathematics'], 0)]),
Sc('Biology: Symbiosis and Community Ecology',
   'Grade 10 Biology strand: community ecology examines how different species interact within a shared environment, including symbiotic relationships such as mutualism, commensalism, and parasitism, and how these interactions shape overall ecosystem structure.',
   [('Community ecology examines how different species ___.', ['Interact within a shared environment', 'Exist with no connection to one another', 'A concept unrelated to ecosystems', 'Remain entirely isolated from their environment'], 0),
    ('In a mutualistic relationship between species, ___.', ['Both species benefit from the interaction', 'Only one species benefits, while the other is harmed', 'A concept unrelated to symbiosis', 'Neither species is affected by the interaction'], 0),
    ('Which of these best describes a parasitic relationship?', ['One species benefits at the expense of the other', 'Both species benefit equally from the interaction', 'A concept unrelated to symbiotic relationships', 'Neither species is affected in any way'], 0),
    ('Why do symbiotic relationships play an important role in shaping overall ecosystem structure?', ['These close interactions can influence population sizes and the flow of energy and resources within a community', 'Symbiotic relationships have no effect on an ecosystem’s overall structure', 'A reason unrelated to community ecology', 'Species interactions never influence how an ecosystem functions'], 0),
    ('Why might scientists studying community ecology examine multiple types of species interactions together?', ['A fuller picture of interconnected relationships helps explain the overall stability and dynamics of an ecosystem', 'Studying multiple interactions together provides no additional scientific insight', 'Community ecology only ever considers a single type of interaction at a time', 'This concept has no connection to understanding ecosystems'], 0)]),
H('Canada’s Role in Afghanistan',
  'Grade 10 History strand: Canada participated in the military mission in Afghanistan from 2001 to 2014 as part of an international coalition, a commitment that involved significant Canadian casualties and public debate.',
  [('Canada’s military mission in Afghanistan lasted approximately from ___.', ['2001 to 2014', '1970 to 1980', '1945 to 1955', '1919 to 1929'], 0),
   ('Canada’s mission in Afghanistan was carried out as part of ___.', ['An international coalition', 'A purely independent Canadian operation with no international involvement', 'A mission entirely unrelated to military engagement', 'A domestic policy initiative with no connection to Afghanistan'], 0),
   ('Canada’s involvement in Afghanistan involved significant ___.', ['Canadian casualties and public debate', 'No casualties or public discussion of any kind', 'A topic entirely unrelated to Canadian military history', 'Universal, uncontested public support with no debate at all'], 0),
   ('Why is Canada’s role in Afghanistan often studied as an example of a significant modern military commitment?', ['It represented one of Canada’s largest and most sustained military engagements in recent history', 'This mission had no significant impact on Canadian military history', 'Canada’s involvement in Afghanistan has no connection to its foreign policy', 'This topic has no relevance to understanding recent Canadian history'], 0),
   ('Why do historians and policymakers continue to study Canada’s mission in Afghanistan?', ['It raises important questions about the costs, goals, and legacy of Canadian military engagement abroad', 'This mission has no lasting historical significance', 'Canada’s role in Afghanistan has been entirely forgotten with no historical record', 'This topic has no relevance to understanding Canadian foreign policy'], 0)])]),

day(60, [
E('Review: Narrative Forms, Rhetoric, and War Literature',
  'Grade 10 English strand: this review lesson revisits the bildungsroman, rhetorical devices, absurdist fiction, documentary technique, epistolary narratives, and war literature covered across Days 51-59.',
  [('A bildungsroman is best described as a novel that traces ___.', ['A protagonist’s psychological and moral growth from youth into maturity', 'A single event with no connection to a character’s development', 'A protagonist who never changes throughout the story', 'A setting description with no focus on character at all'], 0),
   ('Rhetorical devices are language techniques used to ___.', ['Strengthen persuasion and emphasize key points', 'Weaken an argument’s overall persuasiveness', 'A concept unrelated to argumentative writing', 'Remove all emotional appeal from a piece of writing'], 0),
   ('Absurdist fiction typically presents ___.', ['Illogical or nonsensical situations', 'Only strictly realistic, logical events', 'A concept unrelated to fiction', 'A setting with no unusual or unexpected elements'], 0),
   ('An epistolary narrative tells a story through a series of ___.', ['Documents, such as letters or diary entries', 'Only third-person, objective narration', 'A concept unrelated to narrative structure', 'A single uninterrupted scene with no separate documents'], 0),
   ('Why is it useful to review these varied literary forms and techniques together?', ['It reinforces how different narrative approaches and techniques shape meaning and reader experience', 'These topics have no connection to each other', 'Review is never useful in English studies', 'Each topic must be studied with no connection to the others'], 0)]),
M('Review: Logarithms, Rational Functions, and Counting Methods',
  'Grade 10 Math strand review: this lesson revisits logarithmic equations, rational functions, three-dimensional vectors, the binomial theorem, piecewise functions, and permutations and combinations covered across Days 51-59.',
  [('Solving a logarithmic equation often involves rewriting it in ___.', ['Exponential form', 'Linear form only, with no other conversion possible', 'A form unrelated to exponents', 'Fraction form with no connection to exponents'], 0),
   ('A vertical asymptote of a rational function typically occurs where ___.', ['The denominator equals zero', 'The numerator equals zero', 'A location unrelated to the function’s denominator', 'The function crosses the x-axis'], 0),
   ('Pascal’s triangle can be used to determine the ___.', ['Coefficients used in a binomial expansion', 'Exact roots of any polynomial equation', 'A concept unrelated to binomial expansion', 'Only the exponents in an expression, with no connection to coefficients'], 0),
   ('A permutation counts the number of ways items can be arranged when ___.', ['Order matters', 'Order does not matter at all', 'A concept unrelated to counting arrangements', 'Only a single item is being arranged'], 0),
   ('Why is it valuable to review these connected mathematical concepts together?', ['It reinforces how these skills build on and relate to one another', 'These concepts have no connection to each other', 'Review is never useful in math', 'Each concept must be understood with no connection to the others'], 0)]),
Sc('Review: Chemistry, Biology, and Physics Applications',
   'Grade 10 Science strand review: this lesson revisits colligative properties, Mendelian genetics, projectile motion, polymer chemistry, the nervous system, weathering and erosion, simple harmonic motion, gas laws, and community ecology covered across Days 51-59.',
   [('Colligative properties depend primarily on ___.', ['The number of dissolved particles in a solution', 'The specific colour of the solute', 'A factor unrelated to dissolved particles', 'The exact identity of the solute alone, with no connection to particle count'], 0),
    ('A Punnett square is used to ___.', ['Predict the possible genetic outcomes of a cross between two parents', 'Measure the physical size of an organism', 'A tool unrelated to genetics', 'Determine the age of an organism'], 0),
    ('Projectile motion combines constant horizontal velocity with ___.', ['Vertical acceleration due to gravity', 'A second, separate horizontal acceleration', 'A concept unrelated to motion in the air', 'No vertical motion at all'], 0),
    ('The small gap between two neurons, across which a signal is transmitted, is called the ___.', ['Synapse', 'Cortex', 'A structure unrelated to neurons', 'Ventricle'], 0),
    ('Why is it valuable to review these connected science concepts together?', ['It reinforces how these scientific ideas relate to and build on one another', 'These concepts have no connection to each other', 'Review is never useful at the end of a unit', 'Each concept must be understood with no connection to the others'], 0)]),
H('Review: Twentieth- and Twenty-First-Century Canadian History',
  'Grade 10 History strand review: this lesson revisits the Halifax Explosion, the Korean War, the Avro Arrow, the Suez Crisis, the Employment Equity Act, same-sex marriage legalization, the National Energy Program, Japanese Canadian redress, and Canada’s role in Afghanistan covered across Days 51-59.',
  [('The Halifax Explosion was caused by ___.', ['A collision between two ships in Halifax Harbour', 'A natural disaster with no connection to ships', 'An event unrelated to Halifax', 'A planned military attack on the city'], 0),
   ('Lester Pearson is closely associated with helping establish ___.', ['The first large-scale United Nations peacekeeping force', 'A conflict with no connection to peacekeeping', 'An organization unrelated to international diplomacy', 'A purely domestic Canadian policy initiative'], 0),
   ('Canada legalized same-sex marriage nationwide in which year?', ['2005', '1970', '1945', '1990'], 0),
   ('The Canadian government issued a formal apology and financial redress for Japanese Canadian internment in which year?', ['1988', '1945', '1970', '1919'], 0),
   ('Why is it valuable to review these events of 20th- and 21st-century Canadian history together?', ['It reinforces how these historical developments connect to shape modern Canadian identity and policy', 'These events have no meaningful connections to each other', 'Review is never useful in history', 'Each event must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260805):
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
    _rebalance_answer_positions(g10_51_60)
    append_to(10, g10_51_60)
