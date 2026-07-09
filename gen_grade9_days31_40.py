#!/usr/bin/env python3
"""Phase 3: Grade 9, Days 31-40 (first Grade 9 batch, continuing the
10-day pattern used for Grades 3-8). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade9.json): archetypes,
dramatic irony, filter bubbles, quadratic relations, exponent laws, the
mole concept, Newton's laws, and geography extensions (geopolitics,
climate migration, energy transition, GIS in disaster response).

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


g9_31_40 = [
day(31, [
L('Reading: Analyzing Archetypes in Literature',
  'Grade 9 Reading strand: an archetype is a recurring character type, symbol, or pattern found across many stories and cultures, such as the hero, the mentor, or the journey.',
  [('An archetype is best described as ___.', ['A recurring character type or pattern found across many stories', 'A completely unique element found in only one story ever written', 'A grammar rule', 'A type of punctuation mark'], 0),
   ('Which is an example of a common literary archetype?', ['The hero', 'A specific character’s exact birthday', 'A single unrelated punctuation mark', 'A random unrelated number'], 0),
   ('Why do archetypes appear across many different cultures and time periods?', ['They often reflect universal human experiences and themes', 'Archetypes only ever appear in one single culture', 'Archetypes have no connection to human experience', 'They are unique to a single story with no broader pattern'], 0),
   ('The mentor archetype typically ___.', ['Guides or teaches the main character', 'Has no role in a story’s plot', 'Always opposes the main character with no other function', 'Appears only in nonfiction texts'], 0),
   ('Why is recognizing archetypes considered a valuable literary analysis skill?', ['It helps readers see connections between different stories and understand broader patterns', 'This skill has no connection to literary analysis', 'Archetypes are irrelevant to understanding a story', 'Recognizing archetypes replaces the need to understand plot'], 0)]),
M('Introduction to Quadratic Relations',
  'Grade 9 Algebra strand: a quadratic relation, in the form y equals ax squared plus bx plus c, produces a U-shaped graph called a parabola, distinct from the straight-line graph of a linear relation.',
  [('A quadratic relation is written in the form ___.', ['y equals ax squared plus bx plus c', 'y equals mx plus b', 'y equals a divided by x', 'y equals a plus b'], 0),
   ('The graph of a quadratic relation is called a ___.', ['Parabola', 'Straight line', 'Circle', 'Hyperbola'], 0),
   ('How does a quadratic relation’s graph differ from a linear relation’s graph?', ['A quadratic graph is curved (U-shaped), while a linear graph is a straight line', 'They are always identical in shape', 'A quadratic relation never produces a graph', 'Linear relations always produce curved graphs'], 0),
   ('In the quadratic relation y equals x squared, what shape does the graph take?', ['A U-shape opening upward', 'A straight diagonal line', 'A perfect circle', 'A horizontal line'], 0),
   ('Why might quadratic relations be used to model real-world situations, like the path of a thrown object?', ['Their curved shape can represent situations that rise and then fall', 'Quadratic relations can never model real-world situations', 'Only straight-line graphs can represent motion', 'Parabolas have no practical applications'], 0)]),
Sc('The Mole Concept and Molar Mass',
   'Grade 9 Science Chemistry strand: a mole is a unit used to count extremely large numbers of particles, such as atoms or molecules, and molar mass relates the mass of a substance to the number of moles present.',
   [('A mole is a unit used to ___.', ['Count extremely large numbers of particles, like atoms or molecules', 'Measure temperature', 'Measure the volume of a solid object', 'Count the number of chemical elements only'], 0),
    ('Molar mass relates ___.', ['The mass of a substance to the number of moles present', 'Only the colour of a substance', 'The temperature of a substance to its volume', 'A substance’s mass to its exact age'], 0),
    ('Why is the mole considered a useful unit in chemistry?', ['It allows chemists to work with manageable numbers when counting extremely small particles', 'The mole has no practical use in chemistry', 'It only applies to liquids, never solids or gases', 'This unit is unrelated to counting particles'], 0),
    ('Molar mass is typically expressed in units of ___.', ['Grams per mole', 'Litres per second', 'Degrees Celsius', 'Metres per mole'], 0),
    ('Why might chemists need to convert between grams and moles when working with a chemical reaction?', ['It allows them to relate a measurable mass to the actual number of particles reacting', 'This conversion has no use in chemistry', 'Grams and moles are always exactly equal to each other', 'Chemical reactions never require this type of conversion'], 0)]),
SS('Geopolitics: Understanding Borders and Territorial Disputes',
   'Grade 9 Social Studies (Geography) strand: geopolitics examines how geography, borders, and territorial disputes influence political relationships and power between countries and regions.',
   [('Geopolitics examines how ___ influence political relationships between countries.', ['Geography, borders, and territory', 'Only music and art', 'Weather patterns exclusively, with no other factors', 'A topic unrelated to political relationships'], 0),
    ('A territorial dispute occurs when ___.', ['Two or more parties disagree over control of a particular area of land', 'All countries agree completely on every border', 'No disagreements about land ever occur', 'A dispute is unrelated to geography'], 0),
    ('Why might a natural resource located near a border contribute to geopolitical tension?', ['Multiple parties may have competing interests in accessing and controlling that resource', 'Natural resources never cause any political tension', 'Resources located near borders have no political significance', 'Borders have no connection to resource access'], 0),
    ('Why is understanding geopolitics valuable when studying world geography?', ['It helps explain how geographic factors shape international relationships and conflicts', 'Geopolitics has no connection to geography', 'Political relationships between countries are unrelated to geography', 'This topic has no relevance to studying the world'], 0),
    ('Which is an example of a factor that might influence a geopolitical relationship between two countries?', ['A shared border or contested territory', 'The colour of each country’s flag', 'An unrelated cultural tradition with no political relevance', 'A factor unrelated to geography or politics'], 0)])]),

day(32, [
L('Writing: The Literary Response Essay',
  'Grade 9 Writing strand: a literary response essay presents a reader’s interpretation of a text, supported by evidence and analysis, expressing a personal yet well-reasoned perspective.',
  [('A literary response essay presents ___.', ['A reader’s interpretation of a text, supported by evidence', 'Only a summary of the plot with no interpretation', 'A completely unrelated topic', 'An interpretation with no connection to the actual text'], 0),
   ('Why is textual evidence important in a literary response essay?', ['It supports the writer’s interpretation with specific, relevant examples', 'Evidence has no role in this type of essay', 'A literary response essay should never reference the text', 'Evidence always weakens a literary interpretation'], 0),
   ('A literary response essay is considered well-reasoned when it ___.', ['Connects the writer’s interpretation clearly to specific details in the text', 'Ignores the text completely', 'Contains no clear interpretation of any kind', 'Simply repeats the plot with no analysis'], 0),
   ('Why might two readers write different literary response essays about the same text?', ['Interpretation can vary based on the reader’s perspective and the evidence they emphasize', 'Every reader must always reach the exact same interpretation', 'Literary response essays never allow personal interpretation', 'Texts only ever have one single possible meaning'], 0),
   ('A strong literary response essay typically begins with ___.', ['A clear thesis about the writer’s interpretation of the text', 'No clear position on the text at all', 'A summary with no analytical claim', 'A discussion unrelated to the text being analyzed'], 0)]),
M('Solving Quadratic Equations by Factoring',
  'Grade 9 Algebra strand: solving a quadratic equation by factoring involves rewriting it as a product of two binomials, then using the zero product property to find the solutions.',
  [('The zero product property states that if two factors multiply to zero, then ___.', ['At least one of the factors must equal zero', 'Neither factor can ever equal zero', 'Both factors must always equal one', 'The factors have no relationship to zero'], 0),
   ('Solve by factoring: x squared plus 5x plus 6 equals zero.', ['x = -2 or x = -3', 'x = 2 or x = 3', 'x = 5 or x = 6', 'x = -5 or x = -6'], 0),
   ('Solve by factoring: x squared minus 9 equals zero.', ['x = 3 or x = -3', 'x = 9 or x = -9', 'x = 3 only', 'x = -9 only'], 0),
   ('Why does factoring help solve a quadratic equation?', ['It allows the zero product property to identify the specific solutions', 'Factoring never helps solve any type of equation', 'Factoring only applies to linear equations, not quadratics', 'This method has no connection to finding solutions'], 0),
   ('Solve by factoring: x squared plus 2x equals zero.', ['x = 0 or x = -2', 'x = 0 or x = 2', 'x = 2 or x = -2', 'x = 1 or x = -1'], 0)]),
Sc('Newton’s Three Laws of Motion',
   'Grade 9 Science Physics strand: Newton’s three laws of motion describe inertia, the relationship between force, mass, and acceleration, and the principle that every action has an equal and opposite reaction.',
   [('Newton’s first law describes the concept of ___.', ['Inertia', 'Only gravity, with no other forces considered', 'Chemical reactions', 'Genetic inheritance'], 0),
    ('Newton’s second law relates force to ___.', ['Mass and acceleration', 'Only colour and temperature', 'Genetic traits', 'Chemical composition'], 0),
    ('Newton’s third law states that for every action, there is ___.', ['An equal and opposite reaction', 'No reaction of any kind', 'A reaction unrelated to the original action', 'A reaction that is always significantly weaker'], 0),
    ('Which is an everyday example of Newton’s third law?', ['A swimmer pushing water backward to move forward', 'An object that never interacts with any force', 'A chemical reaction with no physical motion involved', 'A plant undergoing photosynthesis'], 0),
    ('Why are Newton’s laws considered foundational to the study of physics?', ['They provide a framework for understanding and predicting how objects move under various forces', 'These laws have no connection to understanding motion', 'They only apply to objects in outer space', 'Newton’s laws have been proven entirely incorrect'], 0)]),
SS('Sustainable Cities: Case Studies in Urban Planning',
   'Grade 9 Social Studies (Geography) strand: sustainable urban planning aims to balance growing populations with environmental protection, efficient transportation, and quality of life, illustrated through real-world city case studies.',
   [('Sustainable urban planning aims to balance population growth with ___.', ['Environmental protection and quality of life', 'No consideration of environmental impact', 'A single unrelated factor', 'The complete elimination of all city growth'], 0),
    ('Why might city planners study real-world case studies of sustainable cities?', ['To learn effective strategies that could be applied to other urban areas', 'Case studies provide no useful information for planning', 'Sustainable cities have never actually been studied', 'This research has no connection to urban planning'], 0),
    ('Which is an example of a sustainable urban planning strategy?', ['Expanding efficient public transportation systems', 'Eliminating all forms of public transportation', 'Ignoring environmental considerations entirely', 'Preventing any development of green spaces'], 0),
    ('Why is quality of life an important consideration in sustainable urban planning?', ['Well-planned cities aim to support residents’ health, wellbeing, and access to resources', 'Quality of life has no connection to urban planning', 'Urban planning never considers the needs of residents', 'Sustainable planning ignores resident wellbeing entirely'], 0),
    ('Why do rapidly growing cities face particular challenges in sustainable planning?', ['Balancing growth with resource and infrastructure needs becomes increasingly complex', 'Growing cities never face any planning challenges', 'Population growth has no connection to urban planning needs', 'Sustainable planning is only relevant to shrinking cities'], 0)])]),

day(33, [
L('Grammar: Advanced Sentence Fragments and Run-ons',
  'Grade 9 Writing strand: advanced correction of sentence fragments and run-ons requires recognizing subtle grammatical issues in complex sentences and applying appropriate punctuation or restructuring.',
  [('A sentence fragment lacks ___.', ['A complete subject, verb, or complete thought', 'Any punctuation at all', 'A title', 'A specific number of words'], 0),
   ('A run-on sentence incorrectly joins ___.', ['Two or more complete sentences without proper punctuation', 'A single short phrase with no other issues', 'Only correctly punctuated clauses', 'A sentence with no verb at all'], 0),
   ('Which is a common way to correct a run-on sentence?', ['Adding proper punctuation or splitting it into separate sentences', 'Removing all punctuation entirely', 'Making the sentence even longer', 'Ignoring the grammatical issue completely'], 0),
   ('Why might complex sentences be more prone to fragment or run-on errors?', ['Multiple clauses can create confusion about complete thoughts and proper punctuation', 'Complex sentences are never prone to these errors', 'Simple sentences are always more likely to contain these errors', 'Sentence complexity has no connection to these grammatical issues'], 0),
   ('Why is correcting fragments and run-ons important in formal writing?', ['It helps ensure clarity and proper sentence structure for the reader', 'These corrections have no effect on writing clarity', 'Formal writing should always include grammatical errors', 'Fragments and run-ons always improve a sentence’s clarity'], 0)]),
M('Exponent Laws: Power of a Power and Power of a Product',
  'Grade 9 Algebra strand: the power of a power rule states that (x to the a) to the b equals x to the (a times b), while the power of a product rule states that (xy) to the a equals x to the a times y to the a.',
  [('Simplify: (x squared) cubed.', ['x to the fifth power', 'x to the sixth power', 'x to the eighth power', 'x squared'], 1),
   ('Simplify: (xy) squared.', ['x squared times y squared', 'xy squared', 'x squared times y', 'x times y squared'], 0),
   ('The power of a power rule states that (x to the a) to the b equals ___.', ['x to the (a times b)', 'x to the (a plus b)', 'x to the (a minus b)', 'x to the (a divided by b)'], 0),
   ('Simplify: (2x cubed) squared.', ['4x to the sixth power', '2x to the sixth power', '4x to the fifth power', '2x to the fifth power'], 0),
   ('Why are exponent laws useful when simplifying algebraic expressions?', ['They provide consistent rules for combining and simplifying powers efficiently', 'Exponent laws have no practical use in algebra', 'These rules only apply to numbers, never variables', 'Simplifying expressions never requires exponent laws'], 0)]),
Sc('Work, Energy, and Power',
   'Grade 9 Science Physics strand: work is done when a force causes an object to move, energy is the capacity to do work, and power measures how quickly work is done.',
   [('Work is done when ___.', ['A force causes an object to move', 'An object remains completely stationary with no force applied', 'Energy is created from nothing', 'No force is involved at all'], 0),
    ('Energy is best described as ___.', ['The capacity to do work', 'A measurement of time only', 'A type of matter with no connection to work', 'A force unrelated to motion'], 0),
    ('Power measures ___.', ['How quickly work is done', 'The total distance an object travels', 'The colour of an object', 'The temperature of an object'], 0),
    ('If two people lift the same weight to the same height, but one does it faster, which person has exerted more power?', ['The person who did it faster', 'The person who did it slower', 'Both exert exactly equal power regardless of time', 'Power cannot be compared in this situation'], 0),
    ('Why are work, energy, and power considered closely connected concepts in physics?', ['Energy enables work to be done, and power describes the rate at which that work occurs', 'These three concepts have no relationship to each other', 'Only energy has any connection to physics', 'Work and power are identical concepts with no distinction'], 0)]),
SS('Climate Refugees and Environmental Migration',
   'Grade 9 Social Studies (Geography) strand: climate refugees are people forced to leave their homes due to environmental changes, such as rising sea levels, drought, or extreme weather, an increasingly significant global issue.',
   [('A climate refugee is someone forced to leave their home due to ___.', ['Environmental changes, such as rising sea levels or drought', 'A voluntary choice unrelated to the environment', 'A political election', 'A factor unrelated to climate or environment'], 0),
    ('Which is an example of an environmental factor that could displace a population?', ['Rising sea levels', 'A change in local fashion trends', 'A factor unrelated to climate or environment', 'A shift in local sports preferences'], 0),
    ('Why is environmental migration considered an increasingly significant global issue?', ['Climate-related environmental changes are affecting more communities worldwide', 'Environmental migration has no connection to global issues', 'This type of migration never actually occurs', 'Climate change has no effect on where people can live'], 0),
    ('Why might communities near coastlines be particularly vulnerable to climate-related displacement?', ['Rising sea levels can directly threaten coastal homes and infrastructure', 'Coastal communities are never affected by environmental changes', 'Sea level has no connection to coastal communities', 'This vulnerability has no connection to geography'], 0),
    ('Why is studying climate refugees relevant to understanding global geography?', ['It highlights how environmental changes are reshaping population patterns worldwide', 'This topic has no connection to global geography', 'Climate refugees have no impact on population patterns', 'Environmental migration is unrelated to geographic study'], 0)])]),

day(34, [
L('Vocabulary: Denotation and Connotation in Persuasive Texts',
  'Grade 9 Language strand: in persuasive writing, denotation (a word’s literal meaning) and connotation (its associated feeling) are both carefully chosen to influence how an audience responds to an argument.',
  [('In persuasive writing, connotation is used to ___.', ['Influence how an audience emotionally responds to an argument', 'Have no effect on the audience at all', 'Replace the need for any logical argument', 'Confuse readers with no clear purpose'], 0),
   ('Why might a persuasive writer choose the word reckless instead of bold, despite a similar denotation?', ['Reckless carries a more negative connotation, shaping a more critical perspective', 'The two words have completely different denotations', 'Word choice never affects a persuasive argument', 'Connotation has no role in persuasive writing'], 0),
   ('Denotation refers to ___.', ['A word’s literal, dictionary meaning', 'The feeling a word suggests', 'A word’s spelling only', 'A word’s pronunciation only'], 0),
   ('Why is understanding both denotation and connotation important when analyzing persuasive texts?', ['It helps readers recognize how word choice shapes the intended emotional impact', 'Denotation and connotation have no connection to persuasion', 'Only denotation matters in persuasive writing', 'Word choice never influences how an argument is received'], 0),
   ('Which word likely has a more positive connotation than stubborn, despite a similar meaning?', ['Determined', 'Careless', 'Foolish', 'Rude'], 0)]),
M('Financial Literacy: Understanding Credit and Debt',
  'Grade 9 Financial Literacy strand: credit allows borrowing money to be repaid later, often with interest, and understanding how debt accumulates is essential for making informed financial decisions.',
  [('Credit allows a person to ___.', ['Borrow money to be repaid later, often with interest', 'Receive money with no repayment required', 'Avoid ever needing to repay any borrowed money', 'A concept unrelated to borrowing money'], 0),
   ('Debt generally refers to ___.', ['Money that is owed and must be repaid', 'Money that has already been fully paid off with nothing owed', 'A concept unrelated to borrowing', 'Only money that has been saved'], 0),
   ('Why is understanding interest rates important when using credit?', ['Interest can significantly increase the total amount owed over time', 'Interest rates never affect the total amount owed', 'Interest has no connection to credit or debt', 'Understanding interest rates serves no practical purpose'], 0),
   ('Why might making only minimum payments on a debt lead to it taking longer to pay off?', ['Interest continues to accumulate on the remaining balance', 'Minimum payments always eliminate all interest immediately', 'Interest never accumulates on unpaid balances', 'Debt repayment time has no connection to payment amount'], 0),
   ('Why is understanding credit and debt considered an important financial literacy skill?', ['It helps individuals make informed decisions and avoid unnecessary financial strain', 'This understanding has no real-world financial benefit', 'Credit and debt have no connection to personal finances', 'Financial literacy has no relevance to using credit responsibly'], 0)]),
Sc('Genetic Mutations and Variation',
   'Grade 9 Science Biology strand: a genetic mutation is a change in an organism’s DNA sequence, which can introduce new variation into a population and may be neutral, harmful, or beneficial.',
   [('A genetic mutation is best described as ___.', ['A change in an organism’s DNA sequence', 'A change in an organism’s diet only', 'A process unrelated to genetics', 'A change that always immediately kills the organism'], 0),
    ('Mutations can introduce new ___ into a population.', ['Variation', 'Complete uniformity with no differences', 'A concept unrelated to genetics', 'Only harmful effects, with no other possible outcomes'], 0),
    ('A mutation that has no significant effect on an organism is considered ___.', ['Neutral', 'Always beneficial', 'Always harmful', 'Impossible to occur'], 0),
    ('Why are mutations considered an important source of genetic variation?', ['They introduce new traits that can be acted on by natural selection', 'Mutations have no connection to genetic variation', 'Variation in a population never comes from mutations', 'Mutations always eliminate all variation in a population'], 0),
    ('Why might some mutations be considered beneficial to an organism?', ['They may provide an advantage that improves survival or reproduction in a specific environment', 'Beneficial mutations have never actually occurred', 'All mutations are always harmful, with no exceptions', 'Mutations have no connection to an organism’s environment'], 0)]),
SS('Economic Geography: Trade Blocs and Global Markets',
   'Grade 9 Social Studies (Geography) strand: a trade bloc is a group of countries that agree to reduce trade barriers among themselves, shaping regional economic relationships and global market patterns.',
   [('A trade bloc is best described as ___.', ['A group of countries that agree to reduce trade barriers among themselves', 'A single country acting entirely alone', 'A group of countries that refuse to trade with each other', 'A concept unrelated to international trade'], 0),
    ('Why might countries choose to form a trade bloc?', ['To create more favourable trading conditions among member countries', 'Trade blocs provide no economic benefit to member countries', 'Forming a trade bloc always eliminates all trade', 'This arrangement has no connection to economic relationships'], 0),
    ('Which is a potential benefit of belonging to a trade bloc?', ['Easier access to markets in other member countries', 'Complete isolation from all other countries', 'The elimination of all economic activity', 'No connection to other member countries’ economies'], 0),
    ('Why might trade blocs affect global market patterns?', ['They can shift where goods are produced, bought, and sold among member countries', 'Trade blocs have no effect on global markets', 'Global markets are entirely unrelated to trade agreements', 'Trade blocs eliminate the need for any international markets'], 0),
    ('Why is understanding trade blocs useful when studying global economic geography?', ['It helps explain patterns in international trade and economic cooperation', 'Trade blocs have no connection to economic geography', 'This topic has no relevance to understanding global markets', 'Economic geography never considers international agreements'], 0)])]),

day(35, [
L('Reading: Analyzing Dramatic Irony',
  'Grade 9 Reading strand: dramatic irony occurs when the audience or reader knows something important that a character in the story does not, creating tension or anticipation.',
  [('Dramatic irony occurs when ___.', ['The audience knows something a character does not', 'A character knows everything the audience knows', 'No information is withheld from anyone in the story', 'Irony never appears in dramatic works'], 0),
   ('Why might an author use dramatic irony in a story?', ['To create tension, suspense, or anticipation for the audience', 'Dramatic irony always removes tension from a story', 'This technique has no effect on the audience’s experience', 'Dramatic irony is never used intentionally by authors'], 0),
   ('Which is an example of dramatic irony?', ['The audience knows a character is walking into danger, but the character does not', 'A character explains a plan directly to the audience with no hidden information', 'All characters and the audience share identical knowledge at all times', 'A story with no characters or plot at all'], 0),
   ('Why might dramatic irony create emotional engagement for readers or viewers?', ['Anticipating a character’s realization or reaction can heighten emotional investment', 'Dramatic irony has no emotional effect on an audience', 'This technique always removes the reader’s interest in a story', 'Dramatic irony is identical to a simple plot summary'], 0),
   ('Why is dramatic irony considered a distinct literary device from other forms of irony?', ['It specifically involves a gap in knowledge between characters and the audience', 'Dramatic irony is identical to every other form of irony', 'This device has no unique defining characteristics', 'Dramatic irony never involves any difference in knowledge'], 0)]),
M('Analytic Geometry: Parallel and Perpendicular Lines',
  'Grade 9 Analytic Geometry strand: parallel lines have the same slope, while perpendicular lines have slopes that are negative reciprocals of each other.',
  [('Parallel lines have ___.', ['The same slope', 'Slopes that are negative reciprocals', 'No defined slope at all', 'Slopes that are always exactly zero'], 0),
   ('Perpendicular lines have slopes that are ___.', ['Negative reciprocals of each other', 'Always exactly equal', 'Always exactly zero', 'Unrelated to each other'], 0),
   ('If one line has a slope of 2, what slope would a line perpendicular to it have?', ['Negative one-half', '2', 'Negative 2', 'One-half'], 0),
   ('If two lines both have a slope of 3, they are ___.', ['Parallel', 'Perpendicular', 'Impossible to compare', 'Always the same exact line'], 0),
   ('Why is understanding the relationship between slopes of parallel and perpendicular lines useful in geometry?', ['It helps determine the relationship between lines without needing to graph them', 'This relationship has no practical use in geometry', 'Slopes have no connection to whether lines are parallel or perpendicular', 'This concept only applies to curved lines, not straight ones'], 0)]),
Sc('Biomes and Global Ecosystem Patterns',
   'Grade 9 Science Biology strand: Earth’s major biomes, such as tropical rainforest, desert, and tundra, are shaped by climate patterns and support distinct plant and animal communities adapted to those conditions.',
   [('Biomes are shaped primarily by ___.', ['Climate patterns', 'Random chance with no identifiable pattern', 'Only the colour of the local soil', 'A factor unrelated to environmental conditions'], 0),
    ('Which biome is characterized by high biodiversity and a warm, wet climate?', ['Tropical rainforest', 'Desert', 'Tundra', 'Grassland'], 0),
    ('Organisms living in a particular biome typically show adaptations suited to ___.', ['That biome’s specific climate and conditions', 'No particular environmental conditions', 'A biome completely different from their own', 'Random, unrelated characteristics'], 0),
    ('Why might studying global biome patterns help scientists understand biodiversity?', ['Different biomes support distinct communities of organisms adapted to specific conditions', 'Biomes have no connection to biodiversity', 'All biomes support identical plant and animal life', 'This study has no scientific value'], 0),
    ('Why might climate change affect the distribution of Earth’s biomes over time?', ['Shifting climate patterns can alter the conditions that define and support each biome', 'Climate change has no effect on biome distribution', 'Biomes never change in response to environmental shifts', 'This topic has no connection to environmental science'], 0)]),
SS('Indigenous Land Claims and Geographic Justice',
   'Grade 9 Social Studies (Geography) strand: Indigenous land claims involve legal and political efforts to recognize rights to traditional territories, connecting geography with issues of justice and self-determination.',
   [('Indigenous land claims involve efforts to ___.', ['Recognize rights to traditional territories', 'Eliminate all Indigenous rights to land', 'A topic unrelated to geography or land', 'Remove all legal processes related to land'], 0),
    ('Geographic justice, in this context, connects issues of land with ___.', ['Rights and self-determination', 'No connection to justice or rights', 'A concept unrelated to Indigenous communities', 'Only economic factors, with no connection to rights'], 0),
    ('Why might land claims be an important part of Indigenous self-determination?', ['Control over traditional territory can be closely tied to cultural identity and autonomy', 'Land claims have no connection to self-determination', 'Traditional territory has no significance to Indigenous communities', 'Self-determination is entirely unrelated to land or geography'], 0),
    ('Why is studying Indigenous land claims relevant to geography education?', ['It connects geographic concepts of land and territory to real historical and legal issues', 'Land claims have no connection to geography', 'This topic is unrelated to geographic study', 'Geography never intersects with legal or political issues'], 0),
    ('Why might land claims processes be described as an ongoing aspect of geographic justice?', ['Many claims remain in progress, reflecting continuing efforts toward recognition and resolution', 'All land claims were fully resolved in the past with no ongoing processes', 'Land claims have no connection to justice', 'This process has no relevance to modern geography'], 0)])]),

day(36, [
L('Writing: Writing a Feature Article',
  'Grade 9 Writing strand: a feature article explores a topic in depth, often combining factual reporting with engaging storytelling techniques, unlike a straightforward news report.',
  [('A feature article typically ___.', ['Explores a topic in depth, combining facts with engaging storytelling', 'Reports only brief, surface-level facts with no depth', 'Contains no factual information at all', 'Is identical to a basic news report'], 0),
   ('Which is a storytelling technique a feature article might use?', ['A compelling anecdote to draw readers into the topic', 'Ignoring the reader’s interest entirely', 'Presenting only a bulleted list with no narrative', 'Avoiding any connection to the topic’s human interest'], 0),
   ('Why might a feature article include interviews or personal stories?', ['They can add depth, credibility, and a human perspective to the topic', 'Interviews have no place in feature writing', 'Personal stories always weaken a feature article', 'This type of writing should avoid any human perspective'], 0),
   ('How does a feature article typically differ from a standard news report?', ['A feature article often explores a topic in greater depth and with more narrative style', 'They are always identical in style and structure', 'A feature article never includes any factual information', 'News reports always include more depth than feature articles'], 0),
   ('Why might a feature article writer choose a strong, engaging opening?', ['To capture reader interest and draw them into exploring the topic further', 'Feature articles should always have a plain, unengaging opening', 'The opening of a feature article has no effect on reader interest', 'Engaging openings are never used in feature writing'], 0)]),
M('Optimization of Perimeter and Area',
  'Grade 9 Measurement strand: optimization problems involve finding the maximum or minimum value of a measurement, such as determining the shape that maximizes area for a given perimeter.',
  [('An optimization problem involves finding ___.', ['The maximum or minimum value of a measurement', 'A completely random measurement with no goal', 'A measurement unrelated to area or perimeter', 'Only the average of several unrelated values'], 0),
   ('For a fixed perimeter, which shape typically maximizes area among simple rectangles?', ['A square', 'A very long, thin rectangle', 'A shape with no defined sides', 'Any shape produces exactly the same area'], 0),
   ('Why might a fence-building problem be considered an optimization problem?', ['It often involves finding the dimensions that maximize enclosed area for a given amount of fencing', 'Fence-building problems never involve any mathematical optimization', 'Optimization has no connection to real-world measurement problems', 'This type of problem only involves perimeter, never area'], 0),
   ('If a rectangle has a fixed perimeter, increasing the length while decreasing the width will generally ___ the area, beyond a certain point.', ['Decrease', 'Always increase indefinitely with no limit', 'Have no effect on', 'Immediately double'], 0),
   ('Why are optimization problems considered useful in real-world design and planning?', ['They help identify the most efficient use of available materials or space', 'Optimization problems have no real-world applications', 'These problems only apply to theoretical, unrealistic scenarios', 'Efficient design has no connection to mathematical optimization'], 0)]),
Sc('Acids and Bases: Properties and Reactions',
   'Grade 9 Science Chemistry strand: acids and bases have distinct properties, measured using the pH scale, and react with each other in a neutralization reaction to produce water and a salt.',
   [('Acids generally have a pH ___.', ['Below 7', 'Above 7', 'Always exactly 7', 'That cannot be measured'], 0),
    ('Bases generally have a pH ___.', ['Above 7', 'Below 7', 'Always exactly 0', 'That cannot be measured'], 0),
    ('A neutralization reaction occurs when ___.', ['An acid and a base react to produce water and a salt', 'Two acids react with each other with no base involved', 'No chemical reaction takes place at all', 'A substance reacts with itself'], 0),
    ('Which is an example of a common acid?', ['Vinegar', 'Baking soda', 'Soap', 'Ammonia'], 0),
    ('Why is understanding acids and bases important in chemistry?', ['They are involved in many chemical reactions and everyday substances', 'Acids and bases have no real-world relevance', 'This topic has no connection to chemical reactions', 'The pH scale is unrelated to acids and bases'], 0)]),
SS('Geography of Energy Transition: Fossil Fuels to Renewables',
   'Grade 9 Social Studies (Geography) strand: the global energy transition involves shifting from fossil fuel dependence toward renewable energy sources, a process shaped by geography, technology, and economic factors.',
   [('The energy transition refers to ___.', ['A shift from fossil fuel dependence toward renewable energy sources', 'A complete elimination of all energy use', 'A shift toward greater fossil fuel dependence', 'A concept unrelated to energy production'], 0),
    ('Which geographic factor might influence a region’s ability to adopt solar energy?', ['The amount of available sunlight in that region', 'The region’s distance from the ocean, with no other relevant factors', 'A factor entirely unrelated to geography', 'The region’s population size alone'], 0),
    ('Why might the energy transition vary significantly between different countries?', ['Differences in geography, resources, technology, and economic priorities affect the pace of transition', 'All countries experience the exact same energy transition process', 'Geography has no connection to energy production choices', 'Energy transition occurs identically everywhere in the world'], 0),
    ('Why is the energy transition considered a significant global geographic issue?', ['It involves major shifts in resource use, economies, and environmental impact worldwide', 'This transition has no connection to global geography', 'Energy use has no relevance to geographic study', 'The energy transition affects no aspect of global patterns'], 0),
    ('Which is an example of a renewable energy source relevant to this transition?', ['Wind power', 'Coal', 'Oil', 'Natural gas'], 0)])]),

day(37, [
L('Media Literacy: Analyzing Social Media Algorithms and Filter Bubbles',
  'Grade 9 Media Literacy strand: social media algorithms curate content based on user behaviour, which can create filter bubbles that limit exposure to diverse perspectives and reinforce existing beliefs.',
  [('A social media algorithm curates content based on ___.', ['User behaviour and preferences', 'Completely random selection with no pattern', 'A factor entirely unrelated to the user', 'Only the exact time of day, with no other considerations'], 0),
   ('A filter bubble refers to ___.', ['A limited range of perspectives a user is exposed to based on algorithmic curation', 'Exposure to a wide range of completely random, unrelated content', 'A concept unrelated to social media', 'Content selected with no connection to user preferences'], 0),
   ('Why might filter bubbles reinforce existing beliefs?', ['Users are more likely to see content that aligns with what they already engage with', 'Filter bubbles always expose users to opposing viewpoints', 'This concept has no connection to belief reinforcement', 'Algorithms are designed to show only random, unrelated content'], 0),
   ('Why is understanding algorithms and filter bubbles considered an important media literacy skill?', ['It helps users recognize how their online experience may be shaped and limited', 'This understanding has no practical value', 'Filter bubbles have no effect on the content users see', 'Algorithms have no influence on social media experiences'], 0),
   ('Which strategy could help someone reduce the effects of a filter bubble?', ['Intentionally seeking out diverse sources and perspectives', 'Only ever engaging with content that confirms existing beliefs', 'Avoiding all forms of media entirely', 'Ignoring the existence of algorithms altogether'], 0)]),
M('Introduction to Standard Deviation and Normal Distribution',
  'Grade 9 Data Management strand: standard deviation measures the spread of data, and a normal distribution is a common, symmetric pattern where most data values cluster around the mean.',
  [('Standard deviation measures ___.', ['The spread of data around the mean', 'The exact middle value of a data set', 'The most frequently occurring value', 'The total number of values in a data set'], 0),
   ('A normal distribution is characterized by ___.', ['A symmetric pattern where most values cluster around the mean', 'All values being exactly identical', 'A pattern with no discernible structure', 'Data that is always skewed heavily to one side'], 0),
   ('In a normal distribution, most data values are located ___.', ['Close to the mean', 'Far from the mean, with very few values near it', 'Entirely at the extreme ends of the distribution', 'Randomly scattered with no pattern at all'], 0),
   ('Why might standard deviation be useful when analyzing test scores across a large group?', ['It shows how consistent or varied the scores are relative to the average', 'Standard deviation has no connection to analyzing test scores', 'It always equals the mean, providing no new information', 'This statistic should never be used with test score data'], 0),
   ('A normal distribution is often visually represented as a ___ shaped curve.', ['Bell', 'Straight, diagonal', 'Perfectly flat', 'Zigzag'], 0)]),
Sc('Waves: Properties and Behaviour',
   'Grade 9 Science Physics strand: waves transfer energy through a medium or space, with properties such as wavelength, frequency, and amplitude describing their characteristics and behaviour.',
   [('Waves are best described as a way of transferring ___.', ['Energy', 'Matter permanently from one place to another', 'Nothing at all', 'Only heat, with no other form of energy'], 0),
    ('Wavelength refers to ___.', ['The distance between two corresponding points on a wave, like crest to crest', 'The height of a wave only', 'The speed of a wave only', 'A concept unrelated to waves'], 0),
    ('Amplitude refers to ___.', ['The height of a wave from its resting position, related to its energy', 'The distance between two wave crests', 'The number of waves passing a point per second', 'A concept unrelated to waves'], 0),
    ('Frequency refers to ___.', ['The number of waves passing a point in a given amount of time', 'The exact height of a wave', 'The colour of a wave', 'A concept unrelated to wave behaviour'], 0),
    ('Why is understanding wave properties useful across many scientific fields, from sound to light?', ['These properties help explain and predict how different types of waves behave', 'Wave properties have no real-world scientific applications', 'Sound and light have no connection to wave behaviour', 'This topic only applies to a single narrow scientific field'], 0)]),
SS('Comparative Geography: Developed and Developing Regions',
   'Grade 9 Social Studies (Geography) strand: comparing developed and developing regions involves examining differences in economic development, infrastructure, and access to resources across the world.',
   [('Comparing developed and developing regions often involves examining differences in ___.', ['Economic development and infrastructure', 'Nothing measurable at all', 'Only the colour of national flags', 'A factor unrelated to geography or economics'], 0),
    ('Which is an example of an indicator that might be used to compare development between regions?', ['Access to healthcare and education', 'The exact number of national holidays', 'A factor unrelated to development', 'Only a country’s physical size'], 0),
    ('Why might infrastructure, such as roads and utilities, be relevant to comparing regions?', ['Infrastructure can significantly affect a region’s economic opportunities and quality of life', 'Infrastructure has no connection to regional development', 'Roads and utilities have no effect on economic opportunity', 'This factor is unrelated to comparative geography'], 0),
    ('Why is it important to consider multiple indicators, rather than just one, when comparing regions?', ['A single indicator may not fully capture the complexity of development in a region', 'Using multiple indicators always provides less accurate information', 'One single indicator always fully explains a region’s development', 'Comparing regions requires no supporting data at all'], 0),
    ('Why might comparative geography be considered a valuable field of study?', ['It helps identify patterns, disparities, and opportunities for addressing global inequalities', 'Comparative geography has no real-world value', 'This field has no connection to understanding global development', 'Regional comparisons provide no useful geographic insight'], 0)])]),

day(38, [
L('Grammar: Advanced Modifiers and Sentence Clarity',
  'Grade 9 Writing strand: advanced modifier issues, including dangling and misplaced modifiers in complex sentences, can create ambiguity, and identifying and correcting them improves overall sentence clarity.',
  [('A dangling modifier lacks ___.', ['A clear word in the sentence to describe', 'Any connection to grammar rules', 'A subject in every case', 'A verb in every case'], 0),
   ('A misplaced modifier is positioned ___.', ['Too far from the word it describes', 'Correctly next to the word it modifies', 'At the very beginning of every sentence', 'Nowhere near any part of the sentence'], 0),
   ('Why might modifier issues become more common in longer, more complex sentences?', ['More clauses and phrases increase the chances of unclear placement', 'Complex sentences are never prone to modifier errors', 'Simple sentences are always more likely to have these issues', 'Sentence length has no connection to modifier placement'], 0),
   ('Which sentence contains a misplaced modifier? Nearly finished, the report took hours to write.', ['This sentence', 'I nearly finished writing the report after hours.', 'The report took hours to write.', 'Writing the report took hours.'], 0),
   ('Why is correcting modifier errors especially important in formal or academic writing?', ['Clear, unambiguous sentences support the reader’s accurate understanding of complex ideas', 'Modifier placement has no effect on formal writing', 'Formal writing should always contain ambiguous sentences', 'These corrections have no impact on academic clarity'], 0)]),
M('Introduction to Exponential Growth',
  'Grade 9 Algebra strand (non-linear relations): exponential growth occurs when a quantity increases by a consistent percentage or factor over equal time periods, producing a curve that rises increasingly steeply.',
  [('Exponential growth occurs when a quantity increases by ___.', ['A consistent percentage or factor over equal time periods', 'A fixed amount added each time period', 'A completely random amount each time period', 'Nothing at all, since the quantity never changes'], 0),
   ('The graph of exponential growth typically ___.', ['Rises increasingly steeply over time', 'Forms a perfectly straight line', 'Decreases steadily over time', 'Remains completely flat'], 0),
   ('Which is an example of a real-world situation that models exponential growth?', ['A population doubling every certain number of years', 'A quantity that decreases by a fixed amount each year', 'A value that never changes over time', 'A straight-line increase by the same fixed amount each year'], 0),
   ('How does exponential growth differ from linear growth?', ['Exponential growth increases by a percentage or factor, while linear growth increases by a fixed amount', 'They are always identical patterns of growth', 'Linear growth always increases faster than exponential growth', 'Exponential growth never actually increases over time'], 0),
   ('Why might exponential growth eventually become unsustainable in a real-world context, like population growth?', ['Resources and space are often limited, which can eventually slow or limit growth', 'Exponential growth can continue indefinitely with no limiting factors', 'Real-world resources have no connection to population growth', 'This type of growth pattern never applies to real-world situations'], 0)]),
Sc('Nuclear Reactions: Fission and Fusion',
   'Grade 9 Science Physics strand: nuclear fission splits a large atomic nucleus into smaller parts, while nuclear fusion combines small nuclei into a larger one, both releasing significant amounts of energy.',
   [('Nuclear fission involves ___.', ['Splitting a large atomic nucleus into smaller parts', 'Combining small nuclei into a larger one', 'A process unrelated to atomic nuclei', 'No release of energy whatsoever'], 0),
    ('Nuclear fusion involves ___.', ['Combining small nuclei into a larger one', 'Splitting a large nucleus into smaller parts', 'A process unrelated to nuclear reactions', 'No release of energy whatsoever'], 0),
    ('Which process powers the Sun?', ['Nuclear fusion', 'Nuclear fission', 'A process unrelated to nuclear reactions', 'Simple chemical combustion'], 0),
    ('Which process is used in traditional nuclear power plants to generate electricity?', ['Nuclear fission', 'Nuclear fusion', 'A process unrelated to nuclear reactions', 'Simple chemical combustion'], 0),
    ('Why do both fission and fusion release significant amounts of energy?', ['Changes in the nucleus can convert a small amount of mass into a large amount of energy', 'Neither process actually releases any energy', 'These processes have no connection to energy production', 'Only chemical reactions can release significant energy'], 0)]),
SS('Geographic Information Systems in Disaster Response',
   'Grade 9 Social Studies (Geography) strand: Geographic Information Systems (GIS) are used during disaster response to map affected areas, track resources, and coordinate relief efforts efficiently.',
   [('GIS technology is used during disaster response to ___.', ['Map affected areas and coordinate relief efforts', 'Have no connection to disaster response', 'Prevent all forms of geographic mapping', 'Replace the need for any relief efforts'], 0),
    ('Why might mapping affected areas be important during a natural disaster?', ['It helps responders understand the scope of damage and where resources are most needed', 'Mapping has no benefit during a disaster response', 'This information has no connection to relief efforts', 'GIS technology cannot be applied to disaster situations'], 0),
    ('Which is an example of information GIS might track during a disaster response?', ['The location of damaged infrastructure', 'Information entirely unrelated to the disaster', 'Only historical weather data with no current relevance', 'A factor unrelated to disaster response planning'], 0),
    ('Why is coordinating resources efficiently important during disaster relief efforts?', ['Efficient coordination can help ensure resources reach the people who need them most quickly', 'Resource coordination has no effect on the success of relief efforts', 'Disaster response never requires any coordination', 'GIS technology has no connection to resource management'], 0),
    ('Why might GIS be considered a valuable tool for geographers and emergency responders alike?', ['It combines geographic data with practical applications for real-world decision-making', 'GIS technology has no practical applications', 'This technology has no connection to geography', 'Emergency response never benefits from geographic data'], 0)])]),

day(39, [
L('Writing: The Extended Metaphor in Creative Writing',
  'Grade 9 Writing strand: an extended metaphor develops a single comparison throughout a piece of writing, deepening meaning and creating a cohesive thread of imagery.',
  [('An extended metaphor is a comparison that ___.', ['Is developed and sustained throughout a piece of writing', 'Appears only once in a single sentence', 'Has no connection to the rest of the writing', 'Is never used in creative writing'], 0),
   ('Why might a writer use an extended metaphor instead of a single, brief comparison?', ['It can create a more cohesive and deeply developed sense of meaning throughout the piece', 'Extended metaphors always weaken a piece of writing', 'A brief comparison always creates more meaning than an extended one', 'Extended metaphors have no effect on a reader’s understanding'], 0),
   ('Which is an example of the beginning of an extended metaphor about life as a journey?', ['Life is a road, and we are all travellers navigating its twists and turns.', 'The weather was sunny that day.', 'This is a plain, literal statement with no comparison.', 'A sentence with no figurative language at all.'], 0),
   ('Why might an extended metaphor be considered more complex to write than a simple metaphor?', ['It requires maintaining the comparison consistently across multiple parts of the writing', 'Extended metaphors require no consistency or planning', 'A simple metaphor is always more difficult to write', 'This technique has no connection to complexity in writing'], 0),
   ('Why is imagery an important element of an effective extended metaphor?', ['Vivid imagery helps make the sustained comparison meaningful and engaging', 'Imagery has no connection to extended metaphors', 'Extended metaphors should always avoid descriptive imagery', 'Imagery only matters in nonfiction writing'], 0)]),
M('Trigonometry: Solving for Angles and Sides',
  'Grade 9 Geometry strand: applying sine, cosine, and tangent ratios allows you to solve for unknown angles or side lengths in right triangles when given sufficient information.',
  [('To find a missing side length in a right triangle when you know an angle and the hypotenuse, you might use ___.', ['Sine or cosine', 'Only addition, with no trigonometry involved', 'The area formula for a triangle', 'A method unrelated to trigonometric ratios'], 0),
   ('To find a missing angle when you know two side lengths of a right triangle, you would typically use ___.', ['An inverse trigonometric function', 'Only the Pythagorean theorem, with no trigonometry involved', 'A method with no connection to trigonometric ratios', 'The formula for a circle’s circumference'], 0),
   ('If the opposite side of a right triangle is 8 and the adjacent side is 6, which ratio could help find the angle?', ['Tangent', 'A ratio unrelated to trigonometry', 'Only the Pythagorean theorem', 'The formula for area'], 0),
   ('If an angle in a right triangle is 30 degrees and the hypotenuse is 10, which ratio would help find the length of the opposite side?', ['Sine', 'A ratio unrelated to trigonometry', 'Only addition, with no trigonometry involved', 'The formula for perimeter'], 0),
   ('Why are trigonometric ratios useful for solving real-world problems involving right triangles?', ['They allow indirect calculation of unknown angles or distances using known measurements', 'Trigonometric ratios have no real-world applications', 'These ratios only apply to shapes with no angles', 'This method requires physically measuring every side directly'], 0)]),
Sc('Environmental Science: Biomagnification and Bioaccumulation',
   'Grade 9 Science Biology strand: bioaccumulation is the buildup of a substance within an individual organism over time, while biomagnification describes how that substance becomes more concentrated at higher levels of a food chain.',
   [('Bioaccumulation refers to ___.', ['The buildup of a substance within an individual organism over time', 'A substance disappearing completely from an organism', 'A process unrelated to living organisms', 'The rapid removal of a substance from an ecosystem'], 0),
    ('Biomagnification describes how a substance becomes ___.', ['More concentrated at higher levels of a food chain', 'Less concentrated at higher levels of a food chain', 'Completely eliminated at higher levels of a food chain', 'Unrelated to food chains'], 0),
    ('Which type of organism in a food chain might experience the highest concentration of a biomagnified substance?', ['A top predator', 'A primary producer, such as a plant', 'An organism with no connection to the food chain', 'The very first organism to consume the substance, with no further transfer'], 0),
    ('Why are bioaccumulation and biomagnification considered important environmental concerns?', ['Harmful substances can become increasingly concentrated and dangerous as they move up a food chain', 'These processes have no effect on ecosystems', 'Substances always become less harmful as they move through a food chain', 'This topic has no connection to environmental science'], 0),
    ('Which is an example of a substance historically associated with biomagnification concerns?', ['Certain persistent pesticides', 'Plain drinking water with no other substances', 'Oxygen', 'A substance with no environmental impact'], 0)]),
SS('The Geography of Global Supply Chains',
   'Grade 9 Social Studies (Geography) strand: global supply chains involve the geographic network of production, transportation, and distribution that brings goods from raw materials to consumers around the world.',
   [('A global supply chain involves the geographic network of ___.', ['Production, transportation, and distribution of goods', 'A single unrelated activity with no connection to goods', 'Only local production with no international connections', 'A concept unrelated to geography or economics'], 0),
    ('Why might a product’s components be manufactured in multiple different countries?', ['Companies may choose locations based on resources, labour, and cost factors', 'Products are always manufactured entirely within a single country with no exceptions', 'Manufacturing location has no connection to geography or economics', 'Global supply chains never involve multiple countries'], 0),
    ('Which is an example of a factor that could disrupt a global supply chain?', ['A natural disaster affecting a key production or shipping region', 'A factor with no possible impact on supply chains', 'Supply chains are never affected by any external events', 'A change unrelated to production or transportation'], 0),
    ('Why is understanding global supply chains relevant to studying geography?', ['It shows how geographic location and connections shape the movement of goods worldwide', 'Supply chains have no connection to geographic study', 'This topic has no relevance to understanding global trade', 'Geography never influences how goods are produced or distributed'], 0),
    ('Why might disruptions to global supply chains have widespread economic effects?', ['Many industries and consumers around the world often depend on these interconnected networks', 'Supply chain disruptions never have any broader economic impact', 'Global supply chains have no connection to consumers', 'Economic effects are always limited to a single country'], 0)])]),

day(40, [
L('Reading: Analyzing an Author’s Craft Across a Text',
  'Grade 9 Reading strand: analyzing an author’s craft involves examining the deliberate choices a writer makes -- in structure, language, and literary devices -- and how those choices work together across an entire text.',
  [('Analyzing an author’s craft involves examining ___.', ['Deliberate choices in structure, language, and literary devices', 'Only a single isolated sentence from the text', 'The book’s cover design only', 'A factor unrelated to how the text was written'], 0),
   ('Why might an author’s choice of sentence structure affect a reader’s experience?', ['Structure can influence pacing, emphasis, and overall tone throughout a text', 'Sentence structure has no effect on a reader’s experience', 'All sentence structures create an identical reading experience', 'This choice has no connection to an author’s craft'], 0),
   ('Analyzing craft across an entire text, rather than a single passage, allows readers to ___.', ['Identify patterns and consistent techniques the author uses throughout the work', 'Understand only one isolated moment in the text with no broader connections', 'Ignore how different literary elements work together', 'Assume all authors use identical techniques throughout every text'], 0),
   ('Why is evaluating an author’s craft considered an advanced literary analysis skill?', ['It requires synthesizing multiple elements of writing to understand the author’s overall approach', 'This skill requires no analysis of the text’s language or structure', 'Only the plot needs to be considered when evaluating an author’s craft', 'Analyzing craft has no connection to understanding a text deeply'], 0),
   ('Which is an example of analyzing an author’s craft?', ['Examining how repeated imagery builds a theme across a novel', 'Only summarizing the plot with no analysis', 'Ignoring the author’s stylistic choices entirely', 'Focusing solely on the book’s price and page count'], 0)]),
M('Review: Quadratics, Exponents, Trigonometry, and Statistics',
  'Grade 9 Algebra and Geometry strands review: this lesson revisits quadratic relations, exponent laws, exponential growth, trigonometric ratios, and standard deviation from recent lessons.',
  [('The graph of a quadratic relation is called a ___.', ['Parabola', 'Straight line', 'Circle', 'Hyperbola'], 0),
   ('Simplify: (x squared) cubed.', ['x to the fifth power', 'x to the sixth power', 'x to the eighth power', 'x squared'], 1),
   ('Exponential growth occurs when a quantity increases by ___.', ['A consistent percentage or factor over equal time periods', 'A fixed amount added each time period', 'A completely random amount each time period', 'Nothing at all, since the quantity never changes'], 0),
   ('Standard deviation measures ___.', ['The spread of data around the mean', 'The exact middle value of a data set', 'The most frequently occurring value', 'The total number of values in a data set'], 0),
   ('Why is it useful to review quadratics, exponents, trigonometry, and statistics together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Physics, Chemistry, and Environmental Science',
   'Grade 9 Science review: this lesson revisits Newton’s laws, work and energy, the mole concept, acids and bases, nuclear reactions, and bioaccumulation and biomagnification covered across recent lessons.',
   [('Newton’s third law states that for every action, there is ___.', ['An equal and opposite reaction', 'No reaction of any kind', 'A reaction unrelated to the original action', 'A reaction that is always significantly weaker'], 0),
    ('A mole is a unit used to ___.', ['Count extremely large numbers of particles, like atoms or molecules', 'Measure temperature', 'Measure the volume of a solid object', 'Count the number of chemical elements only'], 0),
    ('Acids generally have a pH ___.', ['Below 7', 'Above 7', 'Always exactly 7', 'That cannot be measured'], 0),
    ('Nuclear fusion involves ___.', ['Combining small nuclei into a larger one', 'Splitting a large nucleus into smaller parts', 'A process unrelated to nuclear reactions', 'No release of energy whatsoever'], 0),
    ('Why is it valuable to review physics, chemistry, and environmental science together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: Global Geography and Geopolitical Issues',
   'Grade 9 Social Studies (Geography) review: this lesson revisits geopolitics, sustainable cities, climate refugees, trade blocs, Indigenous land claims, and global supply chains covered across recent lessons.',
   [('Geopolitics examines how ___ influence political relationships between countries.', ['Geography, borders, and territory', 'Only music and art', 'Weather patterns exclusively, with no other factors', 'A topic unrelated to political relationships'], 0),
    ('A climate refugee is someone forced to leave their home due to ___.', ['Environmental changes, such as rising sea levels or drought', 'A voluntary choice unrelated to the environment', 'A political election', 'A factor unrelated to climate or environment'], 0),
    ('A trade bloc is best described as ___.', ['A group of countries that agree to reduce trade barriers among themselves', 'A single country acting entirely alone', 'A group of countries that refuse to trade with each other', 'A concept unrelated to international trade'], 0),
    ('A global supply chain involves the geographic network of ___.', ['Production, transportation, and distribution of goods', 'A single unrelated activity with no connection to goods', 'Only local production with no international connections', 'A concept unrelated to geography or economics'], 0),
    ('Why is it useful to review global geography and geopolitical topics together?', ['It helps reinforce how these interconnected issues shape global patterns and relationships', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260721):
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
    _rebalance_answer_positions(g9_31_40)
    append_to(9, g9_31_40)
