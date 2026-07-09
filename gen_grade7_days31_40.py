#!/usr/bin/env python3
"""Phase 3: Grade 7, Days 31-40 (first Grade 7 batch, continuing the
10-day pattern used for Grades 3-6). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade7.json): symbolism and
allegory, rhetorical appeals, multi-step equations, similar triangles,
cell division, plate tectonics, and 20th-century Canadian history (the
Great Depression, WWII, the Cold War, the Quiet Revolution) alongside
globalization, self-government, and comparative government systems.

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


g7_31_40 = [
day(31, [
L('Reading: Analyzing Symbolism and Allegory',
  'Ontario Grade 7 Reading strand: symbolism uses an object or image to represent a deeper idea, while an allegory is an entire story in which characters and events represent broader meanings, often moral or political.',
  [('An allegory is best described as ___.', ['A single symbolic object', 'An entire story where characters and events represent broader meanings', 'A type of punctuation mark', 'A grammar rule'], 1),
   ('Symbolism differs from allegory in that symbolism ___.', ['Usually involves a specific object or image representing an idea, rather than an entire story', 'Never appears in literature', 'Is always identical to allegory', 'Only applies to poetry'], 0),
   ('Which is an example of a common literary symbol?', ['A dove representing peace', 'A character’s exact height', 'The page number', 'The book’s publisher'], 0),
   ('Why might an author write an entire story as an allegory?', ['To convey a broader moral, political, or social message through the narrative', 'Allegories have no deeper meaning', 'To avoid having any characters', 'To make a story purely literal with no symbolism'], 0),
   ('Why is understanding symbolism and allegory considered an advanced reading skill?', ['It requires recognizing deeper meaning beyond the literal events of a story', 'It requires no interpretation at all', 'Symbolism and allegory are the simplest literary devices to identify', 'These devices never appear in complex texts'], 0)]),
M('Simplifying and Expanding Algebraic Expressions',
  'Ontario Grade 7 Algebra strand: simplifying an expression means combining like terms, while expanding involves using the distributive property to remove parentheses, such as 2(x + 3) becoming 2x + 6.',
  [('Simplify: 3x + 5x.', ['8x', '15x', '8x squared', '3x + 5'], 0),
   ('Expand: 2(x + 3).', ['2x + 3', '2x + 6', 'x + 6', '2x + 5'], 1),
   ('Simplify: 4x + 2y minus x + 3y.', ['3x + 5y', '5x + 5y', '3x + y', '4x + 5y'], 0),
   ('Like terms are terms that ___.', ['Have the same variable raised to the same power', 'Always have different variables', 'Can never be combined', 'Have no variables at all'], 0),
   ('Expand: 5(2x + 4).', ['10x + 4', '10x + 20', '7x + 20', '10x + 9'], 1)]),
Sc('Cell Division and Growth',
   'Ontario Grade 7 Science Life Systems strand: cell division allows organisms to grow, repair tissue, and reproduce, with mitosis producing two identical cells from one original cell.',
   [('Cell division allows organisms to ___.', ['Grow and repair tissue', 'Stop all biological processes', 'Shrink permanently', 'Lose all genetic material'], 0),
    ('Mitosis results in ___.', ['Two identical cells from one original cell', 'The complete destruction of a cell', 'No new cells being produced', 'A cell that immediately disappears'], 0),
    ('Why is cell division important for healing an injury, such as a cut?', ['New cells are produced to repair and replace damaged tissue', 'Cell division has no role in healing', 'Injuries heal with no biological process involved', 'Cell division only occurs before birth'], 0),
    ('Which process allows a single-celled organism to reproduce?', ['Cell division', 'Photosynthesis only', 'Digestion', 'Respiration only'], 0),
    ('Why do organisms need a reliable process like cell division to grow?', ['Growth requires producing new cells to increase the size and number of tissues', 'Growth never involves cells at all', 'Organisms do not actually grow over time', 'Cell division only occurs in plants, not animals'], 0)]),
SS('The Great Depression and Its Impact on Canada',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: the Great Depression of the 1930s brought severe economic hardship to Canada, including widespread unemployment, leading to major changes in government policy and social programs.',
   [('The Great Depression occurred mainly during which decade?', ['1890s', '1930s', '1950s', '1980s'], 1),
    ('A major effect of the Great Depression in Canada was ___.', ['Widespread unemployment and economic hardship', 'A booming economy with no challenges', 'No effect on Canadian society', 'Immediate prosperity for all Canadians'], 0),
    ('The hardships of the Great Depression led to changes in ___.', ['Government policy and social programs', 'Nothing related to government', 'Only sports rules', 'Foreign languages spoken in Canada'], 0),
    ('Why is the Great Depression considered a turning point in Canadian social policy?', ['It highlighted the need for government support systems during economic crises', 'It had no lasting effect on government policy', 'It occurred after all major social programs were created', 'It had no connection to unemployment or hardship'], 0),
    ('Which is an example of hardship faced by many Canadians during the Great Depression?', ['Widespread job loss and poverty', 'Unlimited access to jobs and wealth', 'No significant economic challenges', 'A rapidly growing, thriving economy'], 0)])]),

day(32, [
L('Writing: Literary Analysis Essay',
  'Ontario Grade 7 Writing strand: a literary analysis essay closely examines elements of a text, such as character, theme, or symbolism, supporting a clear interpretation with evidence from the text.',
  [('A literary analysis essay focuses on ___.', ['Closely examining elements of a text with supporting evidence', 'Only summarizing the plot with no analysis', 'Copying passages with no interpretation', 'Ignoring the text entirely'], 0),
   ('Which is an example of a literary element that might be analyzed in an essay?', ['Symbolism or theme', 'The book’s price', 'The publisher’s address', 'The font size'], 0),
   ('Why is textual evidence important in a literary analysis essay?', ['It supports the writer’s interpretation with specific examples from the text', 'Evidence is unnecessary in literary analysis', 'A literary analysis should never reference the text', 'Evidence makes an analysis less convincing'], 0),
   ('A strong thesis in a literary analysis essay should ___.', ['Present a clear, arguable interpretation of the text', 'Avoid taking any position at all', 'Simply restate the plot with no interpretation', 'Ignore the text’s themes entirely'], 0),
   ('Why might different readers write different literary analyses of the same text?', ['Interpretation can vary based on the reader’s perspective and the evidence they emphasize', 'Every reader must always reach the exact same interpretation', 'Literary analysis allows for no personal interpretation', 'Texts only ever have one single possible meaning'], 0)]),
M('Solving Multi-Step Equations',
  'Ontario Grade 7 Algebra strand: solving a multi-step equation involves combining like terms, using the distributive property if needed, and then applying inverse operations to isolate the variable.',
  [('Solve for x: 2x + 3x + 5 = 25.', ['x = 4', 'x = 5', 'x = 6', 'x = 20'], 0),
   ('Solve for y: 3(y + 2) = 21.', ['y = 5', 'y = 7', 'y = 9', 'y = 15'], 0),
   ('When solving a multi-step equation, which step is often completed first?', ['Combining like terms or expanding parentheses', 'Immediately guessing the answer', 'Ignoring one side of the equation', 'Multiplying both sides by zero'], 0),
   ('Solve for n: 4n minus 2n + 6 = 16.', ['n = 5', 'n = 10', 'n = 8', 'n = 2'], 0),
   ('Solve for m: 2(m + 4) minus 3 = 13.', ['m = 4', 'm = 6', 'm = 8', 'm = 3'], 1)]),
Sc('Photosynthesis and Cellular Respiration',
   'Ontario Grade 7 Science Life Systems strand: photosynthesis converts sunlight into stored energy in plants, while cellular respiration releases that stored energy for cells to use, forming a connected cycle.',
   [('Photosynthesis converts ___ into stored chemical energy.', ['Sunlight', 'Sound', 'Heat only', 'Electricity'], 0),
    ('Cellular respiration releases energy stored in ___.', ['Glucose', 'Rocks', 'Water only', 'Air alone'], 0),
    ('Photosynthesis and cellular respiration are considered connected because ___.', ['The products of one process are often used as inputs for the other', 'They have no relationship to each other', 'Only plants perform either process', 'Neither process involves energy'], 0),
    ('Which gas is taken in by plants during photosynthesis?', ['Carbon dioxide', 'Nitrogen only', 'Helium', 'Argon'], 0),
    ('Why is cellular respiration essential for living cells?', ['It provides the usable energy cells need to carry out their functions', 'Cellular respiration has no role in providing energy', 'Cells never require energy to function', 'Only photosynthesis provides usable energy for cells'], 0)]),
SS('Canada in World War II',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: Canada played a significant role in World War II, contributing troops, resources, and industrial production, which also led to major social changes at home.',
   [('Canada contributed to World War II through ___.', ['Troops, resources, and industrial production', 'No involvement at all', 'Only diplomatic letters with no other support', 'A single soldier with no broader involvement'], 0),
    ('World War II led to significant social changes in Canada, such as ___.', ['Increased roles for women in the workforce', 'No changes to Canadian society', 'A complete halt to all industry', 'The end of all international relationships'], 0),
    ('Why is Canada’s role in World War II considered historically significant?', ['It contributed to shaping Canada’s international reputation and domestic society', 'It had no lasting impact on Canada', 'Canada was not involved in World War II', 'It occurred before World War I'], 0),
    ('Canadian industry during World War II shifted to focus on ___.', ['Producing military supplies and equipment', 'Producing nothing of use to the war effort', 'Only agricultural products with no industrial output', 'Goods entirely unrelated to the war'], 0),
    ('Why do historians study the domestic changes in Canada during World War II?', ['To understand how wartime needs reshaped Canadian society and the economy', 'Domestic changes during the war had no lasting significance', 'Canadian society remained completely unchanged throughout the war', 'These changes have no connection to Canadian history'], 0)])]),

day(33, [
L('Grammar: Subjunctive Mood and Conditional Sentences',
  'Ontario Grade 7 Writing strand: the subjunctive mood expresses wishes, hypotheticals, or conditions contrary to fact, often seen in sentences like If I were taller, I would reach the shelf.',
  [('The subjunctive mood is often used to express ___.', ['Simple factual statements only', 'Wishes, hypotheticals, or conditions contrary to fact', 'Commands only', 'Questions only'], 1),
   ('Which sentence correctly uses the subjunctive mood?', ['If I was taller, I would reach the shelf.', 'If I were taller, I would reach the shelf.', 'If I am taller, I would reach the shelf.', 'If I will be taller, I would reach the shelf.'], 1),
   ('A conditional sentence typically includes ___.', ['An if clause and a result clause', 'No clauses at all', 'Only a single unrelated word', 'A command with no condition'], 0),
   ('Which sentence expresses a wish using the subjunctive mood?', ['I wish I were on vacation right now.', 'I wish I am on vacation right now.', 'I wish I was is on vacation right now.', 'I wish vacation.'], 0),
   ('Why might writers use the subjunctive mood in formal or literary writing?', ['To express hypothetical or unreal situations clearly', 'The subjunctive mood has no specific grammatical purpose', 'It is only used for factual statements', 'It replaces the need for verbs entirely'], 0)]),
M('Direct and Partial Variation',
  'Ontario Grade 7 Algebra strand: direct variation describes a relationship where one quantity is a constant multiple of another (y equals kx), while partial variation includes a fixed starting amount plus a variable rate (y equals kx plus b).',
  [('In direct variation, the relationship between x and y can be written as ___.', ['y equals kx', 'y equals kx plus b', 'y equals x minus k', 'y equals b'], 0),
   ('In partial variation, the relationship between x and y can be written as ___.', ['y equals kx', 'y equals kx plus b', 'y equals x divided by k', 'y equals 0'], 1),
   ('Which situation is an example of direct variation?', ['The total cost of apples, based only on price per apple times quantity, with no extra fee', 'A taxi fare with a flat starting fee plus a per-kilometre rate', 'A fixed monthly fee with no other charges', 'A situation with no relationship between two quantities'], 0),
   ('Which situation is an example of partial variation?', ['A phone plan with a flat monthly fee plus a per-text charge', 'A situation where cost is always exactly zero', 'A relationship with no constant rate at all', 'Buying items where total cost is exactly price times quantity, with no starting fee'], 0),
   ('In the equation y equals 3x plus 5, what does the 5 represent in a partial variation context?', ['The starting or fixed amount', 'The rate of change', 'An unrelated constant with no meaning', 'The value of x'], 0)]),
Sc('Plate Tectonics and Continental Drift',
   'Ontario Grade 7 Science Earth and Space Systems strand: plate tectonics explains how Earth’s crust is divided into large plates that move slowly over time, a process related to the theory of continental drift.',
   [('Plate tectonics explains how Earth’s crust is divided into ___.', ['Large plates that move slowly over time', 'A single, unmoving piece', 'Only ocean water', 'Layers of clouds'], 0),
    ('Continental drift is the theory that ___.', ['Continents have moved and shifted position over millions of years', 'Continents have always remained in the exact same position', 'Only oceans move, never land', 'Earth’s crust has no movement at all'], 0),
    ('Movement of tectonic plates can result in ___.', ['Earthquakes and volcanic activity', 'No geological activity at all', 'The complete disappearance of continents', 'Only changes in ocean colour'], 0),
    ('Evidence supporting continental drift includes ___.', ['Matching coastlines and fossil patterns across separated continents', 'No evidence exists to support this theory', 'Continents that have never been connected in any way', 'A complete absence of fossil evidence'], 0),
    ('Why is understanding plate tectonics important for studying natural disasters?', ['It helps explain the causes behind events like earthquakes and volcanic eruptions', 'Plate tectonics has no connection to natural disasters', 'Natural disasters occur with no geological cause', 'Plate tectonics only affects ocean currents'], 0)]),
SS('The Cold War and Canada’s Role',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: during the Cold War, Canada aligned with Western allies, participated in organizations like NATO, and played a role in international tensions between the United States and the Soviet Union.',
   [('During the Cold War, Canada generally aligned with ___.', ['Western allies', 'The Soviet Union exclusively', 'No other countries at all', 'Only isolated, unrelated nations'], 0),
    ('NATO is an organization that Canada participated in during ___.', ['The Cold War era', 'Ancient history', 'A period before Confederation', 'A time with no international alliances'], 0),
    ('The Cold War was primarily a period of tension between the United States and ___.', ['The Soviet Union', 'Canada', 'France', 'Japan'], 0),
    ('Why might Canada have chosen to participate in international alliances during the Cold War?', ['To align with allies and contribute to collective international security', 'Canada avoided all international involvement during this period', 'Alliances provided no benefit to Canada', 'Canada had no role in international relations at that time'], 0),
    ('Why is Canada’s role during the Cold War studied as part of Canadian history?', ['It shows how Canada positioned itself within global political tensions', 'Canada had no role in Cold War events', 'This period has no relevance to Canadian history', 'Canada was entirely disconnected from world events during the Cold War'], 0)])]),

day(34, [
L('Vocabulary: Connotation, Denotation, and Word Choice',
  'Ontario Grade 7 Language strand: denotation is a word’s literal meaning, connotation is the feeling or association it carries, and skilled writers choose words carefully based on both to create a desired effect.',
  [('Denotation refers to ___.', ['A word’s literal, dictionary meaning', 'The feeling a word suggests', 'A word’s spelling only', 'A word’s pronunciation only'], 0),
   ('Connotation refers to ___.', ['A word’s literal definition only', 'The feeling or association a word carries beyond its literal meaning', 'A word’s part of speech', 'The number of syllables in a word'], 1),
   ('Why might a writer choose the word slender instead of skinny, despite similar denotations?', ['Slender often carries a more positive connotation', 'The words have completely different denotations', 'Word choice never affects tone', 'Connotation has no effect on writing'], 0),
   ('Which word likely has a more negative connotation than confident, despite a similar meaning?', ['Arrogant', 'Assured', 'Self-assured', 'Capable'], 0),
   ('Why is understanding connotation especially important in persuasive writing?', ['Word choice can strongly influence how an audience feels about a topic', 'Connotation has no role in persuasion', 'Persuasive writing should avoid considering word choice', 'Connotation only matters in poetry'], 0)]),
M('Similar Triangles and Scale Factor',
  'Ontario Grade 7 Geometry strand: similar triangles have the same shape but not necessarily the same size, with corresponding sides in proportion according to a consistent scale factor.',
  [('Similar triangles have ___.', ['The same shape but not necessarily the same size', 'Different shapes and different sizes', 'Identical size but different shapes', 'No relationship to each other at all'], 0),
   ('If two triangles are similar with a scale factor of 2, and one side of the smaller triangle is 5 cm, the corresponding side of the larger triangle is ___.', ['2.5 cm', '5 cm', '10 cm', '7 cm'], 2),
   ('A scale factor describes ___.', ['The ratio between corresponding sides of similar shapes', 'The exact angle measurements only', 'A shape’s colour', 'The area of a triangle only'], 0),
   ('In similar triangles, corresponding angles are ___.', ['Equal', 'Always different', 'Impossible to compare', 'Irrelevant to similarity'], 0),
   ('If a triangle has sides of 3, 4, and 5, and is scaled by a factor of 3, what are the new side lengths?', ['6, 8, 10', '9, 12, 15', '3, 4, 5', '1, 4/3, 5/3'], 1)]),
Sc('Optics: Refraction and Lenses',
   'Ontario Grade 7 Science Matter and Energy strand: refraction is the bending of light as it passes between materials of different densities, a principle used in lenses to focus or spread out light.',
   [('Refraction occurs when light ___.', ['Bends as it passes between materials of different densities', 'Disappears completely', 'Always travels in a perfectly straight line with no change', 'Turns into sound'], 0),
    ('A lens uses refraction to ___.', ['Focus or spread out light', 'Block all light completely', 'Create sound waves', 'Prevent any light from passing through'], 0),
    ('A convex lens generally causes light rays to ___.', ['Converge (come together)', 'Always spread apart with no convergence', 'Disappear entirely', 'Reflect back with no refraction'], 0),
    ('Why does a straw in a glass of water sometimes appear bent?', ['Light refracts differently as it passes from air into water', 'The straw physically changes shape underwater', 'Refraction never affects visual appearance', 'Water has no effect on light'], 0),
    ('Which everyday device relies on lenses and refraction to function?', ['Eyeglasses', 'A wooden spoon', 'A cotton shirt', 'A rubber ball'], 0)]),
SS('Quebec’s Quiet Revolution and Canadian Federalism',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: the Quiet Revolution was a period of significant social, political, and economic change in Quebec during the 1960s, which influenced discussions about Canadian federalism.',
   [('The Quiet Revolution took place mainly during which decade?', ['1920s', '1960s', '1980s', '2000s'], 1),
    ('The Quiet Revolution brought significant change to which Canadian province?', ['Ontario', 'Quebec', 'British Columbia', 'Alberta'], 1),
    ('The Quiet Revolution involved changes in areas such as ___.', ['Social, political, and economic life in Quebec', 'No meaningful areas of life', 'Only sports and entertainment', 'Only weather-related policy'], 0),
    ('Why is the Quiet Revolution significant to discussions about Canadian federalism?', ['It shaped ongoing conversations about the relationship between Quebec and the rest of Canada', 'It had no connection to Canadian federalism', 'It ended all discussion of provincial and federal relationships', 'It was unrelated to Quebec’s political development'], 0),
    ('Canadian federalism refers to ___.', ['The division of powers and responsibilities between federal and provincial governments', 'A system with no provincial governments at all', 'A single, unified government with no divisions of power', 'A concept unrelated to Canadian government structure'], 0)])]),

day(35, [
L('Reading: Comparing Themes Across Genres',
  'Ontario Grade 7 Reading strand: comparing how a similar theme, such as courage or friendship, is explored differently across genres like poetry, fiction, and nonfiction reveals how form shapes meaning.',
  [('Comparing themes across genres involves examining ___.', ['How a similar theme is explored differently across different types of texts', 'Only one single text in isolation', 'Nothing related to meaning or form', 'Themes that never appear in more than one genre'], 0),
   ('Which is an example of comparing a theme across genres?', ['Examining how courage is portrayed in a poem versus a nonfiction article', 'Reading only one book and ignoring all others', 'Comparing two unrelated topics with no shared theme', 'Ignoring the text’s form entirely'], 0),
   ('Why might a theme be expressed differently in poetry compared to nonfiction?', ['Different genres use distinct techniques, such as imagery or structure, to convey ideas', 'All genres express themes in exactly the same way', 'Poetry never contains any identifiable themes', 'Genre has no connection to how a theme is presented'], 0),
   ('Why is comparing themes across genres considered a valuable literacy skill?', ['It deepens understanding of how form and structure shape meaning', 'This comparison has no educational value', 'Only one genre can ever explore meaningful themes', 'It replaces the need to understand any individual text'], 0),
   ('Which pairing would be useful for comparing how a theme like resilience is explored across genres?', ['A poem about resilience and a nonfiction article about resilience', 'Two unrelated math problems', 'A single grocery list', 'A blank page with no content'], 0)]),
M('Surface Area and Volume of Cylinders',
  'Ontario Grade 7 Geometry strand: the surface area of a cylinder includes its two circular bases plus the curved surface, while its volume is found by multiplying the area of its circular base by its height.',
  [('The volume of a cylinder is found using the formula ___.', ['Base area (a circle) times height', 'Length times width times height', 'Radius times height only', 'Diameter times circumference'], 0),
   ('A cylinder’s surface area includes ___.', ['Two circular bases plus the curved side surface', 'Only one flat face', 'No curved surfaces at all', 'Only the top circular base'], 0),
   ('If a cylinder’s circular base area is 20 square units and its height is 6 units, what is its volume?', ['26 cubic units', '120 cubic units', '20 cubic units', '3.3 cubic units'], 1),
   ('Why might engineers need to calculate the volume of a cylindrical tank?', ['To determine how much liquid or material the tank can hold', 'Volume calculations are unnecessary for tanks', 'Cylindrical tanks have no measurable volume', 'Only surface area matters for tanks, never volume'], 0),
   ('A cylinder’s two circular bases are ___ in size.', ['Different', 'Identical', 'Impossible to determine', 'Irrelevant to the shape'], 1)]),
Sc('Chemical Reactions: Types and Balancing',
   'Ontario Grade 7 Science Matter and Energy strand: chemical reactions can be classified into types such as synthesis and decomposition, and balancing a chemical equation ensures the same number of atoms appears on both sides.',
   [('A synthesis reaction occurs when ___.', ['Two or more substances combine to form a new substance', 'A single substance breaks apart into multiple substances', 'Nothing changes at all', 'Matter disappears completely'], 0),
    ('A decomposition reaction occurs when ___.', ['A single substance breaks down into two or more simpler substances', 'Substances combine to form something new', 'No chemical change occurs', 'Matter is created from nothing'], 0),
    ('Balancing a chemical equation ensures that ___.', ['The same number of atoms appears on both sides of the equation', 'The number of atoms can differ freely between sides', 'No atoms are involved in the reaction', 'Chemical equations never need to be balanced'], 0),
    ('Why is it important for a chemical equation to be balanced?', ['It reflects the law of conservation of mass, since matter is neither created nor destroyed', 'Balancing has no scientific basis', 'Chemical equations are never actually balanced in real reactions', 'It simply makes the equation look neater with no real purpose'], 0),
    ('Which is an example of a synthesis reaction?', ['Two elements combining to form a compound', 'A compound breaking into its individual elements', 'No reaction occurring at all', 'A substance disappearing without forming anything new'], 0)]),
SS('The Charter of Rights and Freedoms in Depth',
   'Ontario Grade 7 Social Studies People and Environments strand: the Canadian Charter of Rights and Freedoms, part of the Constitution since 1982, protects fundamental rights such as freedom of expression, equality rights, and legal rights for people in Canada.',
   [('The Canadian Charter of Rights and Freedoms became part of the Constitution in ___.', ['1867', '1931', '1982', '2000'], 2),
    ('The Charter protects fundamental rights such as ___.', ['Freedom of expression and equality rights', 'No rights at all', 'Only rights for elected officials', 'Only property rights'], 0),
    ('Legal rights protected under the Charter include protections related to ___.', ['Fair treatment within the justice system', 'No connection to the justice system', 'Only voting procedures', 'Only property ownership'], 0),
    ('Why is the Charter considered a significant part of Canadian law?', ['It establishes constitutionally protected rights and freedoms for people in Canada', 'It has no legal significance', 'It applies to no one in Canada', 'It was created before Canada became a country'], 0),
    ('Equality rights under the Charter are intended to protect against ___.', ['Discrimination based on factors like race or gender', 'Nothing related to fairness or discrimination', 'Only economic inequality', 'Discrimination that is fully permitted by law'], 0)])]),

day(36, [
L('Writing: Reflective Personal Essay',
  'Ontario Grade 7 Writing strand: a reflective personal essay explores a meaningful experience from the writer’s life and considers its lasting impact, insight, or lesson learned.',
  [('A reflective personal essay focuses on ___.', ['A meaningful experience and its lasting impact or lesson', 'A completely fictional, unrelated story', 'Only listing unrelated facts with no personal connection', 'Copying someone else’s writing'], 0),
   ('Why is insight or reflection important in this type of essay?', ['It shows deeper thinking about what the experience meant to the writer', 'Reflection has no value in personal writing', 'A reflective essay should avoid any personal insight', 'It replaces the need to describe the experience'], 0),
   ('Which is an example of reflective insight in a personal essay?', ['That challenge taught me to be more patient with myself and others.', 'I woke up. I ate breakfast. I went to school.', 'The weather was cold that day.', 'This essay has no connection to real experiences.'], 0),
   ('A strong reflective essay often connects a specific experience to ___.', ['A broader lesson or understanding about life', 'No broader meaning at all', 'An unrelated topic with no connection', 'Only a list of facts with no interpretation'], 0),
   ('Why might writers choose to write reflective personal essays?', ['To process and share meaningful experiences and what they learned from them', 'Personal reflection serves no purpose in writing', 'Reflective essays are never assigned in school', 'This type of writing avoids any personal connection'], 0)]),
M('Combined Probability Events',
  'Ontario Grade 7 Data Management strand: the probability of two independent events both occurring is found by multiplying their individual probabilities together.',
  [('If the probability of event A is 1/2 and event B is 1/3, what is the probability of both occurring, assuming independence?', ['1/5', '1/6', '2/5', '1/3'], 1),
   ('Two events are independent if ___.', ['The outcome of one does not affect the outcome of the other', 'They always affect each other completely', 'They can never both occur', 'They are always identical events'], 0),
   ('If a coin is flipped and a die is rolled, what is the probability of getting heads and rolling a 6?', ['1/6', '1/12', '1/2', '1/3'], 1),
   ('To find the probability of two independent events both happening, you should ___.', ['Multiply their individual probabilities', 'Add their individual probabilities', 'Subtract one probability from the other', 'Divide one probability by the other'], 0),
   ('If the probability of rain tomorrow is 1/4 and the probability of a specific team winning is 1/2, what is the probability of both events happening, assuming independence?', ['1/8', '3/4', '1/6', '1/2'], 0)]),
Sc('Electricity: Circuits and Ohm’s Law',
   'Ontario Grade 7 Science Structures and Mechanisms strand: Ohm’s Law describes the relationship between voltage, current, and resistance in an electrical circuit, expressed as voltage equals current times resistance.',
   [('Ohm’s Law is expressed as ___.', ['Voltage equals current times resistance', 'Voltage equals resistance divided by current', 'Current equals voltage times resistance', 'Resistance has no relationship to voltage or current'], 0),
    ('In a circuit, resistance refers to ___.', ['Opposition to the flow of electric current', 'The total voltage supplied', 'The amount of current only', 'A type of energy source'], 0),
    ('If voltage increases while resistance stays the same, current will generally ___.', ['Increase', 'Decrease', 'Stay exactly the same', 'Become zero'], 0),
    ('Which of these could increase the resistance in a simple circuit?', ['Using a longer or thinner wire', 'Using a wider, shorter wire', 'Removing all resistance from the circuit', 'Adding no components at all'], 0),
    ('Why is Ohm’s Law useful for understanding electrical circuits?', ['It helps predict how changes in voltage or resistance affect current flow', 'Ohm’s Law has no practical use in circuits', 'It only applies to circuits with no current', 'It describes relationships unrelated to electricity'], 0)]),
SS('Globalization and Its Critics',
   'Ontario Grade 7 Social Studies People and Environments strand: while globalization has increased international trade and connection, critics point to concerns such as economic inequality, loss of local industries, and environmental impact.',
   [('Critics of globalization often raise concerns about ___.', ['Economic inequality and environmental impact', 'No concerns exist regarding globalization', 'Only benefits, with no drawbacks discussed', 'Globalization having no effect on any country'], 0),
    ('One concern about globalization is that it can lead to ___.', ['The loss of local industries in some regions', 'The growth of local industries with no downsides', 'No economic changes anywhere', 'Complete economic isolation for every country'], 0),
    ('Why might some communities feel negatively impacted by globalization?', ['Increased international competition can affect local jobs and industries', 'Globalization has no effect on local communities', 'All communities benefit equally with no downsides', 'Globalization eliminates all economic challenges'], 0),
    ('Supporters and critics of globalization often disagree about ___.', ['Whether its benefits outweigh its potential downsides', 'Whether globalization exists at all', 'Nothing, since everyone agrees completely', 'Topics unrelated to trade or economics'], 0),
    ('Why is it useful to consider multiple perspectives on globalization?', ['It provides a more complete understanding of its complex effects', 'Considering multiple perspectives has no value', 'Only one perspective on globalization is ever valid', 'Globalization affects every country in an identical way'], 0)])]),

day(37, [
L('Media Literacy: Analyzing Propaganda Techniques',
  'Ontario Grade 7 Media Literacy strand: propaganda uses techniques such as name-calling, bandwagon appeal, and emotional language to influence public opinion, often simplifying complex issues.',
  [('Propaganda is designed to ___.', ['Influence public opinion, often through persuasive or misleading techniques', 'Present only neutral, unbiased information', 'Avoid persuading anyone of anything', 'Provide a fully balanced view of every issue'], 0),
   ('Bandwagon appeal is a propaganda technique that suggests ___.', ['You should do something because many other people are doing it', 'No one else agrees with the message', 'Facts are irrelevant to any argument', 'The audience should ignore popular opinion entirely'], 0),
   ('Name-calling as a propaganda technique involves ___.', ['Using negative labels to discredit an opposing person or idea', 'Presenting balanced, respectful language', 'Avoiding any judgment of people or ideas', 'Providing detailed, neutral facts only'], 0),
   ('Why might propaganda oversimplify complex issues?', ['To make a message easier to spread and more emotionally persuasive', 'Propaganda always presents highly detailed, nuanced arguments', 'Simplification has no persuasive effect', 'Propaganda avoids emotional appeals entirely'], 0),
   ('Why is it useful for citizens to recognize propaganda techniques?', ['It helps them think critically about messages instead of being easily influenced', 'Recognizing these techniques serves no purpose', 'Propaganda has no real influence on public opinion', 'Citizens should accept persuasive messages without question'], 0)]),
M('Compound Interest',
  'Ontario Grade 7 Financial Literacy strand: compound interest is calculated on both the original principal and any interest already earned, causing savings or debt to grow faster than with simple interest over time.',
  [('Compound interest is calculated based on ___.', ['The original amount plus any interest already earned', 'Only the original amount, with no interest added', 'A completely unrelated amount', 'Only amounts borrowed, never saved'], 0),
   ('Why does compound interest typically result in more growth over time than simple interest?', ['Interest is earned on previously earned interest as well as the original amount', 'Compound interest works exactly the same way as simple interest', 'Compound interest always results in less money over time', 'Interest rates are automatically lower with compound interest'], 0),
   ('If $100 earns 10 percent compound interest in the first year, how much interest is earned in year one?', ['$5', '$10', '$100', '$110'], 1),
   ('In year two of compound interest, interest is calculated on ___.', ['The original amount plus year one’s interest', 'Only the original amount from year one', 'A completely new, unrelated amount', 'Nothing at all'], 0),
   ('Why is understanding compound interest useful when considering long-term savings or loans?', ['It helps predict how savings or debt will grow significantly over time', 'Compound interest has no real-world financial impact', 'It only applies to very small amounts of money', 'Compound interest calculations are never used in real finance'], 0)]),
Sc('The Nitrogen Cycle',
   'Ontario Grade 7 Science Life Systems strand: the nitrogen cycle describes how nitrogen moves between the atmosphere, soil, and living things, with bacteria playing a key role in converting nitrogen into forms plants can use.',
   [('The nitrogen cycle describes how nitrogen moves between ___.', ['The atmosphere, soil, and living things', 'Only outer space', 'Nowhere, since nitrogen never moves', 'Only inside human bodies'], 0),
    ('Which organisms play a key role in converting nitrogen into forms plants can use?', ['Certain bacteria', 'Only large mammals', 'Only fish', 'No organisms are involved in this process'], 0),
    ('Nitrogen makes up a large portion of Earth’s ___.', ['Atmosphere', 'Oceans only', 'Rock layers only', 'Ice caps only'], 0),
    ('Why is nitrogen important for plant growth?', ['Plants need nitrogen in usable forms to build proteins and grow', 'Nitrogen has no role in plant growth', 'Plants never require nitrogen in any form', 'Nitrogen prevents plant growth entirely'], 0),
    ('Why is the nitrogen cycle considered an important natural process?', ['It supports life by making nitrogen available in forms living things can use', 'The nitrogen cycle has no ecological importance', 'Nitrogen is not actually found in nature', 'This cycle only affects non-living matter'], 0)]),
SS('Indigenous Self-Government and Modern Treaties',
   'Ontario Grade 7 Social Studies People and Environments strand: many Indigenous communities in Canada today exercise self-government through modern treaties and agreements that recognize their authority over their own affairs.',
   [('Self-government for Indigenous communities generally refers to ___.', ['Having authority to govern their own community affairs', 'Having no say in their own affairs', 'Being governed entirely by another country', 'Having no recognized rights at all'], 0),
    ('A modern treaty between a government and an Indigenous community often addresses ___.', ['Rights, land, and governance arrangements', 'Nothing of significance', 'Only unrelated sports agreements', 'Only trade with foreign countries'], 0),
    ('Why is self-government important to many Indigenous communities?', ['It allows communities to make decisions that reflect their own needs, values, and traditions', 'Self-government has no real impact on communities', 'It removes all rights from Indigenous peoples', 'It has no connection to community wellbeing'], 0),
    ('Modern treaties differ from many historical treaties in that they are often ___.', ['Negotiated to address more contemporary rights and governance issues', 'Identical to treaties signed centuries ago', 'Impossible to negotiate today', 'Void of any legal significance'], 0),
    ('Learning about Indigenous self-government helps students understand ___.', ['How Indigenous nations exercise rights and responsibilities today', 'That Indigenous governance ended in the past', 'That Indigenous communities have no role in modern Canada', 'That treaties are no longer relevant'], 0)])]),

day(38, [
L('Grammar: Using Passive Voice Effectively',
  'Ontario Grade 7 Writing strand: while active voice is often clearer, passive voice can be used effectively when the focus should be on the action or receiver rather than who performed it, such as in scientific writing.',
  [('Passive voice can be effective when ___.', ['The focus should be on the action or receiver rather than the doer', 'A sentence should always hide all information', 'Clarity is not a goal of the sentence', 'The subject must always be stated first'], 0),
   ('Which sentence uses passive voice effectively in a scientific context?', ['The solution was heated to 100 degrees Celsius.', 'I heated the solution to 100 degrees Celsius.', 'Someone heated the solution.', 'The solution heats itself.'], 0),
   ('Why might scientific writing often use passive voice?', ['To focus on the process or results rather than who performed the action', 'Passive voice is never used in scientific writing', 'Scientific writing should always use active voice exclusively', 'Passive voice makes scientific writing less accurate'], 0),
   ('Which is a potential drawback of overusing passive voice?', ['Sentences can become less direct or clear', 'Passive voice always makes writing clearer', 'There are no drawbacks to passive voice', 'It always shortens sentences significantly'], 0),
   ('Which sentence is written in active voice?', ['The ball was thrown by Sam.', 'Sam threw the ball.', 'The ball is thrown.', 'The ball had been thrown.'], 1)]),
M('Sampling and Bias in Data Collection',
  'Ontario Grade 7 Data Management strand: a sample should represent the larger population fairly, and bias in sampling occurs when certain groups are overrepresented or underrepresented, leading to inaccurate conclusions.',
  [('A sample in statistics refers to ___.', ['A smaller group selected to represent a larger population', 'The entire population being studied', 'A single random individual with no connection to a study', 'Data that has no connection to any population'], 0),
   ('Bias in sampling occurs when ___.', ['Certain groups are overrepresented or underrepresented', 'Every group is represented in exact proportion to the population', 'No data is collected at all', 'Sampling always produces perfectly accurate results'], 0),
   ('Why might surveying only students in one specific class about a school-wide issue introduce bias?', ['That group might not accurately represent the opinions of the entire school', 'Every class always has identical opinions', 'Bias never occurs in surveys', 'A single class always represents the whole school perfectly'], 0),
   ('A random sample is generally considered more reliable because ___.', ['It gives every member of the population a fair chance of being included', 'It always excludes certain groups intentionally', 'Randomness always leads to biased results', 'It never accurately represents a population'], 0),
   ('Why is recognizing bias in data collection important?', ['Biased data can lead to inaccurate or misleading conclusions', 'Bias has no effect on the accuracy of conclusions', 'Sampling bias is impossible to identify', 'Bias only affects opinions, never factual data'], 0)]),
Sc('Astronomy: Galaxies and the Universe',
   'Ontario Grade 7 Science Earth and Space Systems strand: a galaxy is a massive collection of stars, gas, and dust held together by gravity, and our solar system exists within the Milky Way galaxy, one of billions of galaxies in the universe.',
   [('A galaxy is best described as ___.', ['A massive collection of stars, gas, and dust held together by gravity', 'A single planet', 'A type of comet', 'A small cluster of rocks'], 0),
    ('Our solar system exists within which galaxy?', ['Andromeda', 'The Milky Way', 'Triangulum', 'Whirlpool'], 1),
    ('Scientists estimate that the universe contains ___.', ['Billions of galaxies', 'Only one galaxy', 'No galaxies at all', 'Exactly ten galaxies'], 0),
    ('What force holds a galaxy’s stars and matter together?', ['Gravity', 'Magnetism', 'Friction', 'Air pressure'], 0),
    ('Why do astronomers study galaxies beyond our own?', ['To better understand the structure, formation, and scale of the universe', 'Studying other galaxies serves no scientific purpose', 'Only our own galaxy is worth studying', 'Galaxies beyond our own have no connection to astronomy'], 0)]),
SS('Urban Planning and Sustainable Cities',
   'Ontario Grade 7 Social Studies People and Environments strand: urban planning involves designing cities to balance housing, transportation, and green space, with sustainable cities aiming to reduce environmental impact while supporting growing populations.',
   [('Urban planning involves designing cities to balance ___.', ['Housing, transportation, and green space', 'Nothing related to city design', 'Only building height with no other factors', 'A single unrelated factor'], 0),
    ('A sustainable city aims to ___.', ['Reduce environmental impact while supporting its population', 'Maximize pollution and resource waste', 'Ignore population growth entirely', 'Eliminate all green space'], 0),
    ('Which is an example of sustainable urban planning?', ['Expanding public transportation to reduce car dependency', 'Removing all parks and green spaces', 'Ignoring transportation needs entirely', 'Increasing pollution with no mitigation efforts'], 0),
    ('Why might urban planners prioritize green space in city design?', ['Green space can improve air quality and quality of life for residents', 'Green space has no benefits for a city', 'Green space always harms a city’s development', 'Urban planners never consider environmental factors'], 0),
    ('Why is sustainable urban planning becoming increasingly important?', ['Growing populations and environmental concerns require thoughtful, balanced city design', 'Cities never need to consider sustainability', 'Urban planning has no connection to environmental issues', 'Population growth has no effect on city planning needs'], 0)])]),

day(39, [
L('Writing: Formal Analytical Report',
  'Ontario Grade 7 Writing strand: a formal analytical report investigates a topic in depth, presenting findings with objective, well-organized evidence and a clear structure, often used in academic or professional contexts.',
  [('A formal analytical report typically presents ___.', ['Objective, well-organized evidence on a topic', 'Only the writer’s personal opinions with no evidence', 'Random unrelated information', 'A purely fictional story'], 0),
   ('Why is clear organization important in an analytical report?', ['It helps readers follow and understand the findings logically', 'Organization has no effect on how a report is understood', 'Reports should always be presented with no clear structure', 'Clear organization makes a report less credible'], 0),
   ('Which is a feature commonly found in a formal analytical report?', ['Headings that organize information by topic', 'No structure or headings of any kind', 'Only informal, casual language throughout', 'A complete absence of evidence'], 0),
   ('Why might an analytical report avoid overly casual language?', ['Formal language helps maintain credibility in an academic or professional context', 'Casual language always improves credibility', 'Language choice has no effect on a report’s tone', 'Reports are never expected to sound professional'], 0),
   ('An analytical report’s conclusion should typically ___.', ['Summarize key findings and their significance', 'Introduce entirely new, unrelated information', 'Contain no connection to the report’s findings', 'Be identical to the introduction'], 0)]),
M('Slope and Rate of Change',
  'Ontario Grade 7 Algebra strand: slope represents the rate of change between two variables on a graph, calculated as the vertical change (rise) divided by the horizontal change (run) between two points.',
  [('Slope is calculated as ___.', ['Rise divided by run', 'Run divided by rise', 'Rise times run', 'Rise plus run'], 0),
   ('If a line rises 6 units and runs 3 units, what is its slope?', ['2', '3', '0.5', '9'], 0),
   ('A steeper line on a graph generally indicates ___.', ['A greater rate of change', 'No rate of change at all', 'A smaller rate of change', 'A completely flat line'], 0),
   ('A horizontal line has a slope of ___.', ['1', '0', 'Undefined', '10'], 1),
   ('Why is slope a useful concept when analyzing graphs of real-world situations, such as speed over time?', ['It represents how quickly one quantity changes in relation to another', 'Slope has no real-world application', 'Slope only applies to graphs with no practical meaning', 'Rate of change cannot be represented graphically'], 0)]),
Sc('Environmental Toxicology and Pollution',
   'Ontario Grade 7 Science Earth and Space Systems strand: environmental toxicology studies how pollutants, such as chemicals released into air, water, or soil, affect living organisms and ecosystems.',
   [('Environmental toxicology studies how ___.', ['Pollutants affect living organisms and ecosystems', 'Living things have no connection to their environment', 'Pollution never has any measurable effects', 'Only weather patterns are studied, not pollution'], 0),
    ('Which is an example of a pollutant that could affect an ecosystem?', ['Chemicals released into a river', 'Clean, untreated rainwater', 'Fresh air with no contaminants', 'Naturally growing plants'], 0),
    ('Pollution entering a water source can affect ___.', ['Both aquatic organisms and the people who rely on that water', 'Nothing at all, since water is unaffected by pollutants', 'Only organisms living on land', 'Only the colour of the water, with no other effects'], 0),
    ('Why might scientists monitor pollution levels in ecosystems?', ['To assess risks to wildlife and human health and guide environmental protection', 'Monitoring pollution serves no scientific purpose', 'Pollution levels never change over time', 'Ecosystems are never affected by pollution'], 0),
    ('Which action could help reduce pollution’s impact on an ecosystem?', ['Properly treating wastewater before it enters natural water sources', 'Releasing untreated chemicals directly into rivers', 'Ignoring pollution sources entirely', 'Increasing the use of harmful chemicals with no regulation'], 0)]),
SS('Human Migration Patterns and Push-Pull Factors',
   'Ontario Grade 7 Social Studies People and Environments strand: human migration is often influenced by push factors, which encourage people to leave a place, and pull factors, which attract people to a new location.',
   [('A push factor in migration is something that ___.', ['Encourages people to leave a place', 'Attracts people to a new location', 'Has no influence on migration decisions', 'Only applies to animals, never humans'], 0),
    ('A pull factor in migration is something that ___.', ['Discourages people from leaving a location', 'Attracts people to a new location', 'Has no connection to migration', 'Only affects a single country'], 1),
    ('Which is an example of a push factor?', ['Conflict or economic hardship in a region', 'Job opportunities in a new country', 'Political stability in the current location', 'A strong existing economy at home'], 0),
    ('Which is an example of a pull factor?', ['Better job opportunities in a new location', 'War in a region', 'A natural disaster at home', 'Severe economic hardship at home'], 0),
    ('Why is it useful to study push and pull factors when learning about migration?', ['They help explain the reasons behind people’s decisions to move', 'These factors have no connection to migration patterns', 'Migration always occurs with no identifiable reasons', 'Push and pull factors only apply to a single historical era'], 0)])]),

day(40, [
L('Reading: Evaluating Rhetorical Appeals',
  'Ontario Grade 7 Reading strand: rhetorical appeals include ethos (credibility), pathos (emotion), and logos (logic), and identifying which appeals a text relies on helps readers evaluate how persuasion is being used.',
  [('Ethos as a rhetorical appeal relies on ___.', ['The credibility or trustworthiness of the speaker', 'Emotional language only', 'Logical reasoning only', 'Random unrelated facts'], 0),
   ('Pathos as a rhetorical appeal relies on ___.', ['Emotional connection with the audience', 'Only statistics with no emotional language', 'The speaker’s credentials only', 'Formal logic exclusively'], 0),
   ('Logos as a rhetorical appeal relies on ___.', ['Logical reasoning and evidence', 'Only emotional language', 'Only the speaker’s reputation', 'Random, unsupported claims'], 0),
   ('Which is an example of an appeal to ethos?', ['A doctor citing their medical expertise to support a health claim', 'A story designed only to make the audience feel sad', 'A statistic with no context', 'A random, unrelated fact'], 0),
   ('Why is it useful for readers to identify which rhetorical appeals a text uses?', ['It helps them critically evaluate how the text is attempting to persuade them', 'Rhetorical appeals have no effect on persuasion', 'Identifying appeals is not a useful reading skill', 'All persuasive texts use identical rhetorical strategies'], 0)]),
M('Number Theory: GCF and LCM',
  'Ontario Grade 7 Number strand: the greatest common factor (GCF) is the largest number that divides evenly into two or more numbers, while the least common multiple (LCM) is the smallest number that is a multiple of two or more numbers.',
  [('What is the GCF of 12 and 18?', ['3', '6', '9', '36'], 1),
   ('What is the LCM of 4 and 6?', ['10', '12', '24', '2'], 1),
   ('The GCF of two numbers is ___.', ['The largest number that divides evenly into both', 'The smallest number that is a multiple of both', 'Always equal to one of the two numbers', 'Impossible to calculate'], 0),
   ('The LCM of two numbers is ___.', ['The largest number that divides evenly into both', 'The smallest number that is a multiple of both', 'Always smaller than both numbers', 'The same as the GCF'], 1),
   ('What is the GCF of 20 and 30?', ['5', '10', '15', '60'], 1)]),
Sc('Scientific Literacy: Evaluating Scientific Claims',
   'Ontario Grade 7 Science Inquiry strand: evaluating a scientific claim involves checking whether it is supported by reliable evidence, tested through valid methods, and reviewed by other experts.',
   [('A reliable scientific claim is typically supported by ___.', ['Evidence gathered through valid, testable methods', 'Personal opinion with no evidence', 'Random guessing', 'Claims that cannot be tested in any way'], 0),
    ('Why is peer review important in evaluating scientific claims?', ['It allows other experts to check the accuracy and validity of the findings', 'Peer review has no role in science', 'Peer review always makes findings less accurate', 'Scientific claims should never be reviewed by anyone'], 0),
    ('Which is a warning sign that a scientific claim might be unreliable?', ['It lacks supporting evidence or has never been tested', 'It is supported by multiple independent studies', 'It has been reviewed by other scientists', 'It is based on carefully controlled experiments'], 0),
    ('Why might scientists want to repeat an experiment before fully accepting a claim?', ['Repeating results helps confirm that findings are consistent and reliable', 'Repeating experiments has no scientific value', 'A single experiment is always considered sufficient proof', 'Reliable claims never need to be tested more than once'], 0),
    ('Why is scientific literacy an important skill for evaluating information in daily life?', ['It helps people critically assess whether claims are based on sound evidence', 'Scientific literacy has no real-world application', 'All claims presented as scientific are automatically true', 'Evaluating claims is unnecessary in everyday life'], 0)]),
SS('Comparative Government Systems',
   'Ontario Grade 7 Social Studies People and Environments strand: comparing different government systems around the world, such as parliamentary democracies, republics, and monarchies, highlights different approaches to governance and representation.',
   [('A parliamentary democracy is a system where ___.', ['Citizens elect representatives who form a governing body', 'No elections take place at all', 'A single ruler has unlimited, unchecked power', 'Government decisions are made randomly'], 0),
    ('A republic is generally a system where ___.', ['The head of state is typically elected rather than hereditary', 'Only a king or queen can ever lead', 'There is no government structure at all', 'Citizens have no role in choosing leaders'], 0),
    ('Comparing government systems across countries helps students understand ___.', ['Different ways nations organize decision-making and representation', 'That all countries are governed identically', 'That government systems have no real differences', 'That comparison of government types is unnecessary'], 0),
    ('Why might different countries choose different systems of government?', ['Government systems often reflect a country’s unique history, values, and needs', 'All countries are required to use the same system', 'Government systems have no connection to history or culture', 'Choice of government system is always random'], 0),
    ('Studying comparative government systems can help citizens ___.', ['Better understand how their own government compares to others', 'Avoid learning about their own government', 'Conclude that comparison is unnecessary', 'Assume only one system has ever existed'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260717):
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
    _rebalance_answer_positions(g7_31_40)
    append_to(7, g7_31_40)
