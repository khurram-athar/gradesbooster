#!/usr/bin/env python3
"""Phase 3: Grade 9, Days 41-50 (second Grade 9 batch, continuing the
10-day pattern). Topics chosen to avoid any overlap with the existing Day
1-40 set (see data/grade9.json after the Days 31-40 batch): motif and
imagery, the quadratic formula, completing the square, stoichiometry,
momentum, cosmology, and further geography extensions (resource
conflict, pandemics geography, the Arctic, regional integration blocs).

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


g9_41_50 = [
day(41, [
L('Reading: Analyzing Motif and Recurring Imagery',
  'Grade 9 Reading strand: a motif is a recurring element, image, or idea that appears repeatedly throughout a text, helping to reinforce its central themes.',
  [('A motif is best described as ___.', ['A recurring element or image that appears throughout a text', 'A single event that occurs only once in a story', 'A grammar rule', 'A type of punctuation mark'], 0),
   ('Why might an author use a recurring motif throughout a text?', ['To reinforce and deepen the text’s central themes', 'A motif always weakens a text’s themes', 'Repetition of any kind has no effect on meaning', 'Motifs are never intentionally used by authors'], 0),
   ('Which is an example of a recurring motif?', ['Repeated imagery of light and darkness throughout a novel', 'A single sentence that appears only once', 'A random unrelated detail with no repetition', 'A character’s name, mentioned only in the title'], 0),
   ('How is a motif different from a theme?', ['A motif is a recurring element, while a theme is the deeper message it helps convey', 'A motif and a theme are always identical concepts', 'Themes are always more specific than motifs', 'A motif has no connection to a text’s meaning'], 0),
   ('Why is tracking motifs considered a valuable reading strategy?', ['It helps readers notice patterns that reveal deeper meaning across a text', 'Motifs have no connection to a text’s meaning', 'This strategy has no value for understanding a text', 'Recurring imagery should always be ignored while reading'], 0)]),
M('Solving Quadratic Equations Using the Quadratic Formula',
  'Grade 9 Algebra strand: the quadratic formula, x equals negative b plus or minus the square root of b squared minus 4ac, all over 2a, can solve any quadratic equation, including those that are difficult to factor.',
  [('The quadratic formula can be used to solve equations in the form ___.', ['ax squared plus bx plus c equals zero', 'ax plus b equals zero', 'a plus b equals c', 'a divided by b equals c'], 0),
   ('In the quadratic formula, the expression under the square root, b squared minus 4ac, is called the ___.', ['Discriminant', 'Coefficient', 'Constant', 'Base'], 0),
   ('Why might the quadratic formula be used instead of factoring?', ['It can solve any quadratic equation, even ones that are difficult or impossible to factor', 'It can only be used with equations that are already factored', 'The quadratic formula has no practical use in algebra', 'Factoring always works for every quadratic equation'], 0),
   ('For the equation x squared plus 4x plus 3 equals zero, what are the values of a, b, and c?', ['a = 1, b = 4, c = 3', 'a = 4, b = 3, c = 1', 'a = 3, b = 1, c = 4', 'a = 1, b = 3, c = 4'], 0),
   ('If the discriminant of a quadratic equation is negative, this generally indicates ___.', ['No real solutions', 'Exactly one real solution', 'Infinitely many real solutions', 'The equation cannot be a quadratic'], 0)]),
Sc('Stoichiometry: Introduction to Mole Ratios',
   'Grade 9 Science Chemistry strand: stoichiometry uses the mole ratios from a balanced chemical equation to calculate the amounts of reactants and products involved in a chemical reaction.',
   [('Stoichiometry uses mole ratios to calculate ___.', ['The amounts of reactants and products in a reaction', 'The colour of a chemical reaction', 'The exact temperature of a reaction', 'A value unrelated to chemical reactions'], 0),
    ('Mole ratios in stoichiometry come from ___.', ['The coefficients in a balanced chemical equation', 'A random, unrelated guess', 'The colour of the reactants', 'The temperature at which a reaction occurs'], 0),
    ('Why must a chemical equation be balanced before using it for stoichiometric calculations?', ['A balanced equation accurately reflects the actual mole ratios of reactants and products', 'Balancing has no effect on stoichiometric calculations', 'Unbalanced equations always provide accurate mole ratios', 'Stoichiometry does not require a balanced equation'], 0),
    ('Why is stoichiometry considered a practical application of chemistry?', ['It allows chemists to predict and measure the exact quantities involved in reactions', 'Stoichiometry has no real-world applications', 'This concept only applies to theoretical chemistry with no practical use', 'Mole ratios have no connection to actual chemical quantities'], 0),
    ('If a balanced equation shows a 1:2 mole ratio between two reactants, using 3 moles of the first reactant would require ___.', ['6 moles of the second reactant', '1.5 moles of the second reactant', '3 moles of the second reactant', '9 moles of the second reactant'], 0)]),
SS('Geography of Conflict: Resource Wars and Water Scarcity',
   'Grade 9 Social Studies (Geography) strand: competition over limited resources, such as water, can contribute to regional tensions and conflict, particularly in areas facing scarcity or shared access challenges.',
   [('A resource war generally involves conflict over ___.', ['Access to or control of limited resources', 'A topic entirely unrelated to resources', 'Only cultural traditions, with no resource connection', 'A conflict with no identifiable cause'], 0),
    ('Water scarcity can contribute to regional tension particularly when ___.', ['Multiple groups or countries share access to a limited water source', 'Water is equally abundant everywhere with no competing access', 'Scarcity has no connection to conflict', 'Only a single country ever depends on any water source'], 0),
    ('Why might climate change increase the risk of resource-related conflicts?', ['Changing conditions can further strain already limited resources like water and arable land', 'Climate change has no connection to resource availability', 'Resource-related conflict is entirely unrelated to environmental change', 'Climate change always increases resource availability everywhere'], 0),
    ('Why is understanding resource-related conflict relevant to studying global geography?', ['It highlights how geography and resource distribution can shape political relationships', 'This topic has no connection to geography', 'Resource distribution never affects political relationships', 'Global geography never considers conflict or scarcity'], 0),
    ('Which strategy might help reduce the risk of conflict over shared water resources?', ['Cooperative agreements on resource management between affected parties', 'Ignoring shared resource challenges entirely', 'Preventing all communication between affected parties', 'Resource conflicts can never be addressed through cooperation'], 0)])]),

day(42, [
L('Writing: The Rhetorical Analysis Essay',
  'Grade 9 Writing strand: a rhetorical analysis essay examines how a speaker or writer uses persuasive techniques, such as ethos, pathos, and logos, to achieve their purpose with a specific audience.',
  [('A rhetorical analysis essay examines ___.', ['How a speaker or writer uses persuasive techniques to achieve their purpose', 'Only the literal content of a text with no analysis of technique', 'A completely unrelated topic', 'The exact page count of a text'], 0),
   ('Which are the three classical rhetorical appeals often analyzed in this type of essay?', ['Ethos, pathos, and logos', 'Setting, plot, and character', 'Rhyme, rhythm, and meter', 'Subject, verb, and object'], 0),
   ('Why might a rhetorical analysis essay consider the intended audience of a text?', ['Persuasive techniques are often chosen specifically to appeal to that audience', 'The audience has no connection to how a text is written', 'Rhetorical analysis never considers audience', 'All audiences respond identically to persuasive techniques'], 0),
   ('A rhetorical analysis essay differs from a literary analysis essay in that it primarily focuses on ___.', ['Persuasive strategy and technique rather than literary themes', 'Exactly the same elements as a literary analysis essay', 'Only the physical appearance of the text', 'A topic with no connection to writing techniques'], 0),
   ('Why is analyzing rhetorical technique considered a valuable skill?', ['It helps readers understand how communication can be strategically shaped to persuade', 'This skill has no real-world application', 'Rhetorical technique has no connection to persuasion', 'Analyzing technique replaces the need to understand content'], 0)]),
M('Completing the Square',
  'Grade 9 Algebra strand: completing the square is a method for rewriting a quadratic expression in a form that reveals its vertex, useful for solving equations or graphing parabolas.',
  [('Completing the square is a method used to ___.', ['Rewrite a quadratic expression to reveal its vertex', 'Simplify a linear equation only', 'Solve for the perimeter of a shape', 'A method unrelated to quadratic expressions'], 0),
   ('Completing the square can help with ___.', ['Solving quadratic equations or graphing parabolas', 'Only measuring angles in a triangle', 'A task unrelated to quadratics', 'Simplifying fractions only'], 0),
   ('The vertex form of a quadratic equation, revealed by completing the square, is useful for identifying the parabola’s ___.', ['Minimum or maximum point', 'Exact colour', 'Total perimeter', 'A value unrelated to the graph’s shape'], 0),
   ('Why might completing the square be a useful alternative to factoring for solving a quadratic equation?', ['It works even when a quadratic expression cannot be factored using simple integers', 'Completing the square never works for quadratic equations', 'Factoring is always required before completing the square can be used', 'This method only applies to linear equations'], 0),
   ('Why is understanding multiple methods for solving quadratics, like factoring and completing the square, useful?', ['Different methods may be more efficient depending on the specific equation', 'Only one method should ever be learned for solving quadratics', 'These methods are always identical in approach', 'Multiple methods have no practical benefit'], 0)]),
Sc('Momentum and Collisions',
   'Grade 9 Science Physics strand: momentum is the product of an object’s mass and velocity, and the law of conservation of momentum states that total momentum remains constant in a closed system during a collision.',
   [('Momentum is calculated as ___.', ['Mass times velocity', 'Mass divided by velocity', 'Mass plus velocity', 'Velocity alone, with no connection to mass'], 0),
    ('The law of conservation of momentum states that total momentum in a closed system ___.', ['Remains constant', 'Always increases without limit', 'Always decreases to zero', 'Has no defined value'], 0),
    ('During a collision between two objects, momentum is generally ___.', ['Transferred between the objects', 'Instantly destroyed with no transfer', 'Unrelated to the objects’ mass or velocity', 'Only relevant to one of the two objects involved'], 0),
    ('Why might a heavier object require more force to stop than a lighter object moving at the same speed?', ['The heavier object has greater momentum due to its larger mass', 'Mass has no effect on an object’s momentum', 'Heavier objects always have less momentum than lighter ones', 'Momentum is unrelated to the force needed to stop an object'], 0),
    ('Why is understanding momentum useful in fields like vehicle safety design?', ['It helps engineers understand and manage the forces involved in collisions', 'Momentum has no connection to vehicle safety', 'This concept has no real-world engineering applications', 'Collisions never involve any measurable momentum'], 0)]),
SS('The Geography of Pandemics and Global Health',
   'Grade 9 Social Studies (Geography) strand: the spread of infectious diseases is influenced by geographic factors such as population density, travel networks, and access to healthcare, shaping global public health responses.',
   [('The spread of infectious diseases can be influenced by geographic factors such as ___.', ['Population density and travel networks', 'Only the colour of local buildings', 'A factor entirely unrelated to geography', 'Weather patterns exclusively, with no other influence'], 0),
    ('Why might densely populated urban areas experience faster disease transmission?', ['Closer and more frequent contact between people can make transmission easier', 'Population density has no connection to disease spread', 'Urban areas are always less affected than rural areas', 'Disease transmission is unrelated to human contact patterns'], 0),
    ('Global travel networks can affect pandemics by ___.', ['Enabling diseases to spread more quickly across regions and countries', 'Having no connection to how diseases spread', 'Always preventing the spread of disease entirely', 'Only affecting a single, isolated location'], 0),
    ('Why might access to healthcare vary the impact of a pandemic across different regions?', ['Regions with limited healthcare access may face greater challenges in treatment and containment', 'Healthcare access has no effect on pandemic outcomes', 'All regions have identical access to healthcare resources', 'Pandemics affect every region in an identical way regardless of healthcare'], 0),
    ('Why is studying the geography of pandemics valuable for public health planning?', ['It helps identify patterns and vulnerabilities that can inform more effective responses', 'This topic has no connection to public health', 'Geographic factors have no influence on health outcomes', 'Pandemic planning never considers geographic patterns'], 0)])]),

day(43, [
L('Grammar: Verb Mood (Indicative, Imperative, Subjunctive)',
  'Grade 9 Writing strand: verb mood indicates the speaker’s attitude toward a statement -- indicative for facts, imperative for commands, and subjunctive for wishes or hypotheticals.',
  [('The indicative mood is used to express ___.', ['Facts or statements', 'Commands only', 'Wishes or hypotheticals only', 'Questions only'], 0),
   ('The imperative mood is used to express ___.', ['Commands or requests', 'Only factual statements', 'Only hypothetical situations', 'Only questions'], 0),
   ('The subjunctive mood is used to express ___.', ['Wishes, hypotheticals, or conditions contrary to fact', 'Only simple factual statements', 'Only commands', 'Only past events'], 0),
   ('Which sentence is written in the imperative mood?', ['Close the door.', 'The door is closed.', 'If the door were closed, it would be quiet.', 'Is the door closed?'], 0),
   ('Why might understanding verb mood help a writer communicate more precisely?', ['It clarifies whether a statement is a fact, command, or hypothetical situation', 'Verb mood has no effect on how a sentence is understood', 'All verb moods communicate the exact same meaning', 'Precision in writing has no connection to verb mood'], 0)]),
M('Simplifying Rational Expressions',
  'Grade 9 Algebra strand: a rational expression is a fraction with polynomials in the numerator and denominator, and simplifying it involves factoring and cancelling common factors.',
  [('A rational expression is best described as ___.', ['A fraction with polynomials in the numerator and denominator', 'A whole number with no fractions involved', 'An expression with no variables at all', 'A fraction that can never be simplified'], 0),
   ('Simplifying a rational expression typically involves ___.', ['Factoring and cancelling common factors', 'Adding all terms together with no factoring', 'Ignoring the denominator entirely', 'Multiplying the numerator by an unrelated number'], 0),
   ('Simplify the rational expression (x squared minus 4) over (x minus 2).', ['x + 2', 'x - 2', 'x squared minus 2', '4'], 0),
   ('Why is it important to identify restrictions (values that make the denominator zero) when simplifying rational expressions?', ['Division by zero is undefined, so those values must be excluded from the domain', 'Restrictions have no relevance to rational expressions', 'The denominator can always safely equal zero', 'Simplifying never requires considering the denominator’s value'], 0),
   ('Why might factoring be a necessary first step before simplifying a rational expression?', ['It reveals common factors in the numerator and denominator that can be cancelled', 'Factoring has no connection to simplifying rational expressions', 'Rational expressions can only be simplified without factoring', 'Common factors are never present in these expressions'], 0)]),
Sc('The Endocrine System and Homeostasis',
   'Grade 9 Science Biology strand: the endocrine system releases hormones that help regulate the body’s internal balance, known as homeostasis, in response to internal and external changes.',
   [('Homeostasis refers to ___.', ['The body’s internal balance', 'A complete lack of any bodily regulation', 'A process unrelated to the body’s internal environment', 'Only external temperature, with no internal connection'], 0),
    ('The endocrine system helps maintain homeostasis by releasing ___.', ['Hormones', 'Only physical movement, with no chemical signals', 'Sound waves', 'Light signals'], 0),
    ('Why might the endocrine system respond to changes in the body’s external environment, like temperature?', ['Hormonal signals can help the body adjust and maintain internal stability', 'The endocrine system never responds to external changes', 'Homeostasis has no connection to hormonal signals', 'External changes have no effect on the body’s internal balance'], 0),
    ('Why is maintaining homeostasis important for an organism’s survival?', ['A stable internal environment supports proper functioning of body systems', 'Homeostasis has no connection to an organism’s health', 'The body functions identically regardless of internal balance', 'Maintaining internal balance serves no biological purpose'], 0),
    ('Which is an example of the endocrine system helping regulate the body?', ['Releasing hormones that help control blood sugar levels', 'A process entirely unrelated to hormone regulation', 'Only affecting external appearance, with no internal role', 'Preventing all forms of bodily regulation'], 0)]),
SS('Urban Sprawl and Its Environmental Costs',
   'Grade 9 Social Studies (Geography) strand: urban sprawl is the rapid, spread-out expansion of a city into surrounding areas, often associated with increased land use, traffic congestion, and environmental impact.',
   [('Urban sprawl refers to ___.', ['The rapid, spread-out expansion of a city into surrounding areas', 'A city that maintains a compact, unchanging size', 'A concept unrelated to city growth', 'The complete elimination of all urban development'], 0),
    ('Urban sprawl is often associated with increased ___.', ['Land use and traffic congestion', 'Environmental protection with no development impact', 'A decrease in land use', 'No connection to transportation patterns'], 0),
    ('Why might urban sprawl contribute to greater reliance on cars for transportation?', ['Spread-out development can make walking or public transit less practical', 'Urban sprawl always increases walkability and reduces car use', 'Sprawl has no connection to transportation patterns', 'Compact cities always require more car use than sprawling ones'], 0),
    ('Which is a potential environmental cost associated with urban sprawl?', ['Loss of natural habitat as land is developed', 'Increased protection of natural habitats with no land development', 'No effect on the surrounding environment', 'A reduction in land use overall'], 0),
    ('Why might city planners consider alternatives to urban sprawl, such as denser development?', ['Denser development can reduce environmental impact and support more efficient infrastructure use', 'Alternatives to sprawl provide no environmental or infrastructure benefits', 'Urban sprawl always has fewer environmental costs than denser development', 'Planning alternatives has no connection to environmental impact'], 0)])]),

day(44, [
L('Vocabulary: Precision in Word Choice for Technical Writing',
  'Grade 9 Language strand: technical writing requires precise, unambiguous word choice to clearly communicate specific information, avoiding vague or overly general language.',
  [('Technical writing requires word choice that is ___.', ['Precise and unambiguous', 'Vague and overly general', 'Unrelated to the specific topic', 'Entirely informal with no clarity required'], 0),
   ('Why might vague language cause problems in technical writing, such as instructions?', ['It can lead to confusion or errors when readers try to follow the information', 'Vague language always improves clarity in technical writing', 'Technical writing never requires precise language', 'Ambiguity has no effect on how instructions are understood'], 0),
   ('Which is an example of precise technical language?', ['Turn the dial exactly 90 degrees clockwise', 'Turn the dial a little bit', 'Turn the dial somewhat', 'Adjust the dial as needed, with no specific detail'], 0),
   ('Why might a technical writer avoid using words with multiple possible meanings?', ['Ambiguous words can create confusion about the intended, specific meaning', 'Words with multiple meanings always improve technical clarity', 'Technical writing should always use complex, ambiguous vocabulary', 'Multiple meanings have no effect on clarity in this context'], 0),
   ('Why is precision in word choice especially important in fields like engineering or medicine?', ['Miscommunication in these fields can lead to serious errors or safety issues', 'Precision has no importance in these professional fields', 'Vague language is always preferred in technical or medical writing', 'Word choice has no connection to safety or accuracy'], 0)]),
M('Financial Literacy: Investment and Compound Growth',
  'Grade 9 Financial Literacy strand: investing involves putting money into assets with the goal of growing wealth over time, often benefiting from compound growth, where returns are reinvested to generate further returns.',
  [('Investing generally involves ___.', ['Putting money into assets with the goal of growing wealth over time', 'Spending money with no consideration of future growth', 'A concept unrelated to personal finance', 'Only saving money with no potential for growth'], 0),
   ('Compound growth occurs when ___.', ['Investment returns are reinvested to generate further returns', 'Returns are never reinvested under any circumstances', 'Growth remains completely flat over time', 'A concept unrelated to investing'], 0),
   ('Why might starting to invest early provide a significant advantage over time?', ['Compound growth allows returns to build on themselves over a longer period', 'Starting early has no effect on investment growth', 'Compound growth only benefits investments made later in life', 'Investment timing has no connection to overall growth'], 0),
   ('Why is understanding investment risk important when making financial decisions?', ['Different investments carry different levels of potential risk and reward', 'All investments carry identical risk with no variation', 'Risk has no connection to investment decisions', 'Investment risk should never be considered when investing'], 0),
   ('Why might financial literacy about investing be valuable for young people?', ['It helps them make informed decisions that can support long-term financial goals', 'Investment knowledge has no relevance to young people', 'Financial literacy has no connection to long-term planning', 'Investing is only relevant to older individuals'], 0)]),
Sc('Cellular Respiration in Depth',
   'Grade 9 Science Biology strand: cellular respiration breaks down glucose in the presence of oxygen to release usable energy for cells, producing carbon dioxide and water as byproducts.',
   [('Cellular respiration breaks down ___ to release usable energy.', ['Glucose', 'Water only', 'Oxygen only', 'Carbon dioxide only'], 0),
    ('Cellular respiration typically requires ___.', ['Oxygen', 'Only sunlight, with no oxygen involved', 'No input substances at all', 'Only carbon dioxide, with no oxygen involved'], 0),
    ('Which are byproducts of cellular respiration?', ['Carbon dioxide and water', 'Oxygen and glucose', 'Only sunlight, with no other byproducts', 'Nitrogen and hydrogen'], 0),
    ('Why is cellular respiration essential for most living cells?', ['It provides the usable energy cells need to carry out their functions', 'Cellular respiration has no role in providing energy', 'Cells never require energy to function', 'This process has no connection to cellular energy production'], 0),
    ('How is cellular respiration related to photosynthesis?', ['Photosynthesis produces glucose and oxygen, which cellular respiration then uses', 'The two processes have no connection to each other', 'Cellular respiration produces the glucose used in photosynthesis', 'Only plants perform cellular respiration'], 0)]),
SS('Geography of Renewable Resource Management: Forestry and Fisheries',
   'Grade 9 Social Studies (Geography) strand: managing renewable resources like forests and fisheries sustainably requires balancing current use with the resource’s capacity to regenerate over time.',
   [('A renewable resource, such as a forest, can regenerate over time if it is ___.', ['Managed sustainably', 'Used with no consideration of regeneration', 'Depleted completely with no management', 'Unrelated to management practices'], 0),
    ('Sustainable fisheries management involves balancing ___.', ['Current fishing activity with the fish population’s ability to reproduce and recover', 'Unlimited fishing with no consideration of fish populations', 'A factor unrelated to fish populations', 'Complete elimination of all fishing activity'], 0),
    ('Why might overharvesting a renewable resource threaten its long-term availability?', ['Resources can be depleted faster than they are able to regenerate', 'Renewable resources can never be depleted under any circumstances', 'Overharvesting has no effect on a resource’s availability', 'Regeneration rates have no connection to resource management'], 0),
    ('Which is an example of a sustainable forestry practice?', ['Replanting trees after harvesting to support forest regeneration', 'Clear-cutting an entire forest with no plan for regeneration', 'Ignoring the long-term health of the forest ecosystem', 'Harvesting with no consideration of future forest growth'], 0),
    ('Why is geographic knowledge important for managing resources like forests and fisheries?', ['Understanding the specific geography and ecosystem helps inform effective, sustainable management', 'Geography has no connection to resource management', 'Resource management never depends on geographic factors', 'This knowledge has no relevance to sustainability efforts'], 0)])]),

day(45, [
L('Reading: Analyzing Non-Fiction Argument Structures',
  'Grade 9 Reading strand: non-fiction arguments are often structured with a claim, supporting evidence, and reasoning that connects the evidence to the claim, and analyzing this structure helps evaluate an argument’s strength.',
  [('A non-fiction argument typically includes ___.', ['A claim, supporting evidence, and reasoning', 'Only a random collection of unrelated facts', 'No identifiable structure at all', 'A claim with no supporting evidence'], 0),
   ('Reasoning in an argument serves to ___.', ['Connect the evidence to the claim being made', 'Replace the need for any evidence', 'Have no connection to the claim', 'Confuse the reader intentionally'], 0),
   ('Why is analyzing an argument’s structure useful for evaluating its strength?', ['It helps readers assess whether the evidence and reasoning actually support the claim', 'Structure has no connection to how strong an argument is', 'All arguments are equally strong regardless of their structure', 'This analysis has no value for readers'], 0),
   ('Which is a sign of a well-supported argument?', ['Evidence that is directly relevant and clearly connected to the claim', 'Evidence with no connection to the claim being made', 'A claim with no supporting evidence at all', 'Reasoning that contradicts the evidence provided'], 0),
   ('Why might a reader question an argument that provides a claim with little supporting evidence?', ['A claim without sufficient evidence may be less reliable or convincing', 'Claims never require any supporting evidence', 'Evidence has no connection to how convincing an argument is', 'Readers should accept all claims without question'], 0)]),
M('Introduction to the Equation of a Circle',
  'Grade 9 Analytic Geometry strand: the equation of a circle centred at the origin is x squared plus y squared equals r squared, where r represents the radius.',
  [('The equation of a circle centred at the origin is ___.', ['x squared plus y squared equals r squared', 'x plus y equals r', 'x squared minus y squared equals r', 'x times y equals r squared'], 0),
   ('In the equation of a circle, r represents the ___.', ['Radius', 'Diameter', 'Circumference', 'Area'], 0),
   ('What is the equation of a circle centred at the origin with a radius of 5?', ['x squared plus y squared equals 25', 'x squared plus y squared equals 5', 'x squared plus y squared equals 10', 'x plus y equals 25'], 0),
   ('If a point (x, y) satisfies the equation x squared plus y squared equals 16, that point lies on a circle with a radius of ___.', ['4', '8', '16', '2'], 0),
   ('Why is the equation of a circle considered a useful tool in analytic geometry?', ['It allows circles to be represented and analyzed algebraically on a coordinate plane', 'This equation has no practical use in geometry', 'Circles cannot be represented using equations', 'This equation only applies to squares, not circles'], 0)]),
Sc('Astronomy: Cosmology and the Big Bang Theory',
   'Grade 9 Science Earth and Space Systems strand: the Big Bang theory describes the origin of the universe from an extremely hot, dense state that began expanding roughly 13.8 billion years ago.',
   [('The Big Bang theory describes the origin of the universe as beginning from ___.', ['An extremely hot, dense state', 'A completely empty void with nothing present', 'A single planet expanding outward', 'A theory unrelated to the universe’s origin'], 0),
    ('According to current scientific estimates, the universe began expanding approximately ___ years ago.', ['13.8 billion', '4.5 billion', '100 million', '10,000'], 0),
    ('Cosmology is best described as the scientific study of ___.', ['The origin, structure, and evolution of the universe', 'Only the solar system, with no connection to the broader universe', 'A field unrelated to space science', 'Only Earth’s geological history'], 0),
    ('Which type of evidence supports the Big Bang theory?', ['The observed expansion of the universe', 'A complete absence of any observable evidence', 'Evidence unrelated to the universe’s origin', 'Evidence that the universe is not expanding at all'], 0),
    ('Why is the Big Bang theory considered a foundational concept in cosmology?', ['It provides a widely supported scientific explanation for the origin and expansion of the universe', 'This theory has no scientific support', 'Cosmology has no connection to the universe’s origin', 'The Big Bang theory has been proven entirely incorrect'], 0)]),
SS('The Arctic: Geopolitics and Climate Change',
   'Grade 9 Social Studies (Geography) strand: the Arctic region is experiencing significant environmental change due to climate change, while also becoming an increasingly important area of geopolitical interest due to resources and shipping routes.',
   [('The Arctic is experiencing significant environmental change primarily due to ___.', ['Climate change', 'No environmental changes of any kind', 'A factor unrelated to climate', 'A process unrelated to the region’s geography'], 0),
    ('The Arctic has become an area of increasing geopolitical interest partly due to ___.', ['Access to resources and shipping routes', 'A complete lack of any valuable resources', 'No connection to international interest', 'A topic unrelated to geopolitics'], 0),
    ('Why might melting Arctic ice increase interest in the region’s shipping routes?', ['Reduced ice coverage can make new routes more accessible for navigation', 'Melting ice has no effect on shipping routes', 'Ice melting always makes shipping routes less accessible', 'Shipping interest has no connection to ice coverage'], 0),
    ('Why is the Arctic considered particularly vulnerable to climate change?', ['The region is experiencing warming at a faster rate than many other parts of the world', 'The Arctic is entirely unaffected by climate change', 'Climate change has no connection to polar regions', 'The Arctic has the slowest rate of warming globally'], 0),
    ('Why might multiple countries have interest in Arctic geopolitics?', ['Several nations border or have claims related to Arctic territory and resources', 'No countries have any interest in the Arctic region', 'The Arctic has no connection to international relations', 'Only a single country has any geographic connection to the Arctic'], 0)])]),

day(46, [
L('Writing: The Editorial (Op-Ed)',
  'Grade 9 Writing strand: an editorial, or op-ed, presents a writer’s opinion on a current issue, supported by reasoning and evidence, often intended to persuade or inform public opinion.',
  [('An editorial is written to ___.', ['Present the writer’s opinion on a current issue', 'Report only neutral facts with no opinion', 'Avoid discussing any current issues', 'Copy information without any analysis'], 0),
   ('A strong editorial typically includes ___.', ['Reasoning and evidence to support the writer’s opinion', 'No supporting evidence at all', 'Only the writer’s name and nothing else', 'Random, unrelated information'], 0),
   ('Why might a writer choose to write an editorial about a current issue?', ['To persuade or inform public opinion on a topic they care about', 'Editorials never discuss real or current issues', 'Editorials are always purely factual with no opinion involved', 'Writing an editorial serves no persuasive purpose'], 0),
   ('Which is an example of a strong editorial opening?', ['Our city urgently needs improved public transportation, and here is why.', 'This is an article.', 'Some things happen sometimes.', 'This piece has no clear topic.'], 0),
   ('Why is it useful for an editorial to consider opposing viewpoints?', ['Addressing other perspectives can strengthen the credibility of the writer’s argument', 'Considering other viewpoints always weakens an editorial', 'Editorials should never mention any opposing views', 'This consideration has no effect on persuasive writing'], 0)]),
M('Two-Variable Statistics and Line of Best Fit',
  'Grade 9 Data Management strand: a scatter plot displays the relationship between two variables, and a line of best fit approximates that relationship, helping to identify trends and make predictions.',
  [('A scatter plot is used to display the relationship between ___.', ['Two variables', 'Only a single, isolated variable', 'No variables at all', 'A concept unrelated to data'], 0),
   ('A line of best fit is used to ___.', ['Approximate the overall trend in a scatter plot’s data', 'Connect every single data point exactly', 'Have no connection to the data shown', 'Replace the need for any data collection'], 0),
   ('If a scatter plot shows a line of best fit with a positive slope, this suggests ___.', ['As one variable increases, the other tends to increase as well', 'As one variable increases, the other tends to decrease', 'The two variables have no relationship at all', 'The data is unrelated to the line of best fit'], 0),
   ('Why might a line of best fit be useful for making predictions?', ['It provides a general model that can be used to estimate values beyond the collected data', 'It has no use in predicting any future values', 'A line of best fit only applies to past data with no predictive value', 'Predictions can never be made using this line'], 0),
   ('Why is it important to recognize that a line of best fit represents a general trend, not an exact match to every point?', ['Individual data points can vary above or below the general trend line', 'A line of best fit must always pass through every single data point exactly', 'General trends have no connection to individual data points', 'Data points never vary from the line of best fit'], 0)]),
Sc('Environmental Science: Invasive Species',
   'Grade 9 Science Biology strand: an invasive species is a non-native organism introduced to a new environment where it can cause significant harm to local ecosystems, often by outcompeting native species.',
   [('An invasive species is best described as ___.', ['A non-native organism that causes harm in a new environment', 'A native species that has always lived in that ecosystem', 'A species with no impact on its environment', 'An organism unrelated to any specific ecosystem'], 0),
    ('Invasive species often cause harm by ___.', ['Outcompeting native species for resources', 'Having no interaction with native species at all', 'Always benefiting the native species in that ecosystem', 'Remaining completely isolated from the local ecosystem'], 0),
    ('Why might an invasive species spread rapidly in a new environment?', ['It may lack natural predators or competitors that would normally limit its population', 'Invasive species always have more natural predators than native species', 'Invasive species never spread successfully in new environments', 'Spreading rapidly has no connection to a lack of natural predators'], 0),
    ('Which is an example of how an invasive species might be introduced to a new region?', ['Being accidentally transported through global trade or travel', 'Invasive species can never be introduced to a new region', 'Invasive species only appear through natural migration with no human involvement', 'This introduction always occurs with no identifiable cause'], 0),
    ('Why are invasive species considered a significant environmental concern?', ['They can disrupt local ecosystems and threaten native biodiversity', 'Invasive species have no effect on local ecosystems', 'This topic has no connection to environmental science', 'Native biodiversity is never affected by non-native species'], 0)]),
SS('Geography of Food Systems: From Farm to Table',
   'Grade 9 Social Studies (Geography) strand: a food system involves the geographic network of growing, processing, transporting, and distributing food, connecting rural agricultural regions with urban consumers.',
   [('A food system involves the geographic network of ___.', ['Growing, processing, transporting, and distributing food', 'A single unrelated activity with no connection to food', 'Only food consumption, with no other stages considered', 'A concept unrelated to geography'], 0),
    ('Why might the distance food travels from farm to consumer be a relevant geographic consideration?', ['Transportation distance can affect cost, freshness, and environmental impact', 'Distance has no connection to food systems', 'Food never needs to travel any distance before reaching consumers', 'Transportation has no effect on food quality or cost'], 0),
    ('Which is an example of a factor that could disrupt a food system?', ['A drought affecting a major agricultural region', 'A factor with no possible impact on food systems', 'Food systems are never affected by any external events', 'A change unrelated to agriculture or transportation'], 0),
    ('Why is understanding food systems relevant to studying geography?', ['It shows how geographic factors shape food production, distribution, and access', 'Food systems have no connection to geographic study', 'This topic has no relevance to understanding global patterns', 'Geography never influences food production or distribution'], 0),
    ('Why might access to fresh, local food vary between different regions?', ['Geographic factors like climate, infrastructure, and proximity to farms can all play a role', 'Access to food is always identical in every region', 'Geography has no connection to food access', 'Food access is entirely unrelated to a region’s characteristics'], 0)])]),

day(47, [
L('Media Literacy: Analyzing Podcasts and Audio Storytelling',
  'Grade 9 Media Literacy strand: podcasts use audio-specific techniques, such as tone of voice, sound effects, and pacing, to engage listeners and convey information or narrative in ways unique to the audio medium.',
  [('Podcasts often use techniques such as ___ to engage listeners.', ['Tone of voice, sound effects, and pacing', 'Only written text with no audio elements', 'No storytelling techniques at all', 'Visual elements exclusively, with no audio'], 0),
   ('Why might tone of voice be an important consideration in a podcast?', ['It can convey emotion and emphasis that written text alone cannot always capture', 'Tone of voice has no effect on how a podcast is understood', 'Podcasts never use vocal tone as a storytelling tool', 'Written text always conveys emotion more effectively than audio'], 0),
   ('Sound effects in a podcast might be used to ___.', ['Enhance the listener’s sense of setting or atmosphere', 'Have no connection to a podcast’s content', 'Replace the need for any spoken narration', 'Confuse the listener with no intended purpose'], 0),
   ('Why is pacing an important consideration in audio storytelling?', ['It can affect how information is absorbed and how engaged the listener remains', 'Pacing has no effect on a listener’s experience', 'All podcasts should be paced in exactly the same way', 'Pacing only matters in visual media, not audio'], 0),
   ('Why might analyzing podcasts be considered a valuable media literacy skill?', ['It helps listeners understand how audio-specific techniques shape meaning and persuasion', 'Podcasts require no critical analysis of technique', 'Audio storytelling has no connection to media literacy', 'This skill has no real-world application'], 0)]),
M('Introduction to Cubic Functions',
  'Grade 9 Algebra strand (non-linear relations): a cubic function, such as y equals x cubed, produces a curved graph distinct from both linear and quadratic relations, often with an S-shaped or inflected pattern.',
  [('A cubic function includes a variable raised to the power of ___.', ['Three', 'One', 'Two', 'Zero'], 0),
   ('The graph of a basic cubic function, such as y equals x cubed, is often described as having a ___ shape.', ['S-shaped or inflected', 'Perfectly straight', 'A simple U-shape identical to a parabola', 'A perfect circle'], 0),
   ('How does a cubic function’s graph generally differ from a quadratic function’s graph?', ['A cubic graph can have a different curve pattern, including an inflection point, unlike a parabola', 'They are always identical in shape', 'A cubic function never produces a curved graph', 'Quadratic functions always have more complex graphs than cubic functions'], 0),
   ('What is the value of y when x equals 2 in the function y equals x cubed?', ['8', '6', '4', '2'], 0),
   ('Why might cubic functions be used to model certain real-world situations?', ['Some real-world relationships involve more complex curvature than linear or quadratic models can capture', 'Cubic functions can never model any real-world situation', 'All real-world relationships are always linear', 'This type of function has no practical application'], 0)]),
Sc('Electromagnetism: Fields and Induction',
   'Grade 9 Science Physics strand: electromagnetism describes the relationship between electricity and magnetism, including how a changing magnetic field can induce an electric current, a principle used in generators.',
   [('Electromagnetism describes the relationship between ___.', ['Electricity and magnetism', 'Only sound and light, with no connection to electricity', 'A concept unrelated to physics', 'Only heat, with no connection to magnetism'], 0),
    ('Electromagnetic induction occurs when ___.', ['A changing magnetic field induces an electric current', 'A magnetic field has no effect on electric current', 'Electric current always exists with no external cause', 'A concept unrelated to magnetism or electricity'], 0),
    ('Which technology relies on the principle of electromagnetic induction?', ['A generator', 'A simple hand tool with no electrical components', 'An object with no connection to electricity or magnetism', 'A purely mechanical device with no electromagnetic components'], 0),
    ('Why is electromagnetism considered an important concept in physics and engineering?', ['It underlies many technologies that generate or use electricity', 'Electromagnetism has no real-world applications', 'This concept has no connection to technology or engineering', 'Electricity and magnetism have no relationship to each other'], 0),
    ('Why might moving a magnet near a coil of wire generate an electric current?', ['The changing magnetic field induces a current in the wire', 'Magnets have no effect on electric currents in nearby wires', 'This process requires no connection between magnetism and electricity', 'A stationary magnet would produce the exact same effect'], 0)]),
SS('Space and Place: How Geography Shapes Identity',
   'Grade 9 Social Studies (Geography) strand: the concept of space and place examines how physical location, environment, and community connections shape people’s sense of identity and belonging.',
   [('The concept of place, in geography, often refers to ___.', ['A specific location imbued with meaning and identity', 'A location with no connection to identity or meaning', 'Only geographic coordinates, with no cultural significance', 'A concept unrelated to community or belonging'], 0),
    ('How might a person’s connection to a specific place shape their identity?', ['Local traditions, community, and environment can influence values and a sense of belonging', 'Place has no connection to a person’s identity', 'Identity is entirely unrelated to geographic location', 'A person’s sense of self is never shaped by their surroundings'], 0),
    ('Why might people feel a strong attachment to a particular region or community?', ['Shared experiences, traditions, and relationships tied to that place can create meaningful connections', 'Attachment to place never develops for any reason', 'Geographic location has no emotional significance for people', 'Community connections have no relationship to a specific place'], 0),
    ('Why is studying space and place considered relevant to human geography?', ['It helps explain how geographic context influences culture, identity, and community', 'This concept has no connection to human geography', 'Geography never influences cultural or personal identity', 'Space and place are irrelevant to understanding communities'], 0),
    ('Which is an example of how geography might shape a community’s identity?', ['A coastal community’s traditions being closely tied to fishing and the ocean', 'A community with no connection between its geography and its traditions', 'Geographic location never influencing local traditions', 'Identity forming with no relationship to physical environment'], 0)])]),

day(48, [
L('Grammar: Active Reading of Complex Syntax',
  'Grade 9 Reading and Writing strands: complex syntax includes long or intricate sentence structures, and actively breaking these sentences into smaller parts helps readers accurately understand their meaning.',
  [('Complex syntax refers to ___.', ['Long or intricate sentence structures', 'Only very short, simple sentences', 'A concept unrelated to sentence structure', 'Sentences containing no punctuation at all'], 0),
   ('Why might breaking a complex sentence into smaller parts help with comprehension?', ['It can clarify the relationships between different ideas within the sentence', 'Breaking sentences apart always makes them harder to understand', 'Complex sentences never need to be broken down for comprehension', 'This strategy has no effect on reading comprehension'], 0),
   ('Which is a strategy for actively reading a complex sentence?', ['Identifying the main subject and verb before analyzing additional clauses', 'Ignoring the sentence’s structure entirely', 'Skipping any sentence that seems complex', 'Reading only the first few words of a long sentence'], 0),
   ('Why might authors use complex syntax in their writing?', ['To convey nuanced or interconnected ideas within a single sentence', 'Complex syntax is never used intentionally by authors', 'This structure always makes writing less meaningful', 'Complex sentences have no connection to nuanced ideas'], 0),
   ('Why is understanding complex syntax an important skill for reading advanced texts?', ['Many academic and literary texts rely on intricate sentence structures to convey meaning', 'Advanced texts never use complex syntax', 'This skill has no connection to comprehending difficult texts', 'Complex syntax only appears in overly simple texts'], 0)]),
M('Introduction to Sets and Venn Diagrams (Advanced)',
  'Grade 9 Number strand: a set is a collection of distinct objects, and a Venn diagram visually represents relationships between sets, such as intersections (shared elements) and unions (all elements combined).',
  [('A set is best described as ___.', ['A collection of distinct objects', 'A single isolated number', 'A concept unrelated to mathematics', 'Always an empty collection with no elements'], 0),
   ('The intersection of two sets includes ___.', ['Only the elements shared by both sets', 'Every element from both sets combined, with no overlap consideration', 'No elements at all, by definition', 'Only elements found in neither set'], 0),
   ('The union of two sets includes ___.', ['All elements from both sets combined', 'Only elements shared by both sets', 'No elements at all', 'Only elements found in exactly one of the sets, never both'], 0),
   ('A Venn diagram is used to ___.', ['Visually represent relationships between sets', 'Measure the exact length of a line segment', 'Calculate probability with no connection to sets', 'A tool entirely unrelated to sets'], 0),
   ('If Set A is {1, 2, 3} and Set B is {2, 3, 4}, what is the intersection of A and B?', ['{2, 3}', '{1, 2, 3, 4}', '{1, 4}', 'An empty set'], 0)]),
Sc('Organic Chemistry: An Introduction to Carbon Compounds',
   'Grade 9 Science Chemistry strand: organic chemistry is the study of carbon-based compounds, which form the basis of many essential molecules found in living organisms, such as carbohydrates and proteins.',
   [('Organic chemistry is the study of compounds based primarily on ___.', ['Carbon', 'Oxygen only', 'Helium', 'A concept unrelated to any specific element'], 0),
    ('Carbon-based compounds form the basis of many molecules essential to ___.', ['Living organisms', 'Only non-living materials, with no connection to life', 'A topic unrelated to biology or chemistry', 'Nothing of scientific significance'], 0),
    ('Which is an example of a carbon-based molecule essential to living organisms?', ['Carbohydrates', 'Pure oxygen gas', 'A molecule with no connection to carbon', 'Pure water, with no carbon involved'], 0),
    ('Why is carbon particularly well-suited to forming a wide variety of complex molecules?', ['Carbon atoms can form multiple stable bonds with other atoms, including other carbon atoms', 'Carbon cannot form bonds with other elements', 'Carbon is incapable of forming complex molecular structures', 'This property has no connection to carbon’s chemical behaviour'], 0),
    ('Why is organic chemistry considered foundational to understanding biology?', ['Many biological molecules and processes are based on carbon chemistry', 'Organic chemistry has no connection to biological processes', 'Biology never involves any carbon-based compounds', 'This field of study has no relevance to living organisms'], 0)]),
SS('The Geography of Technology and the Digital Divide',
   'Grade 9 Social Studies (Geography) strand: the digital divide refers to unequal access to technology and the internet across different regions and populations, shaped by geographic, economic, and infrastructure factors.',
   [('The digital divide refers to ___.', ['Unequal access to technology and the internet across regions and populations', 'Equal access to technology everywhere in the world', 'A concept unrelated to technology access', 'A divide unrelated to geography or economics'], 0),
    ('Which factor might contribute to the digital divide in a specific region?', ['Limited internet infrastructure in that area', 'Universal, equal access to technology everywhere', 'A factor entirely unrelated to infrastructure', 'The digital divide has no connection to infrastructure'], 0),
    ('Why might rural areas sometimes experience a more significant digital divide than urban areas?', ['Building internet infrastructure can be more challenging and costly in less densely populated areas', 'Rural areas always have identical internet access to urban areas', 'Infrastructure development has no connection to population density', 'The digital divide only affects urban areas, never rural ones'], 0),
    ('Why is the digital divide considered a significant geographic and social issue?', ['Unequal access to technology can affect education, economic opportunity, and communication', 'The digital divide has no real-world consequences', 'Technology access has no connection to opportunity or education', 'This issue has no relevance to geographic study'], 0),
    ('Which is an example of an effort to address the digital divide?', ['Expanding internet infrastructure to underserved areas', 'Restricting technology access even further in underserved areas', 'Ignoring disparities in technology access entirely', 'An effort with no connection to improving access'], 0)])]),

day(49, [
L('Writing: Writing a Monologue',
  'Grade 9 Writing strand: a monologue is an extended speech delivered by a single character, often revealing their inner thoughts, motivations, or emotional state to the audience.',
  [('A monologue is best described as ___.', ['An extended speech delivered by a single character', 'A conversation between multiple characters', 'A written description of a setting only', 'A summary of an entire play’s plot'], 0),
   ('A monologue often reveals a character’s ___.', ['Inner thoughts, motivations, or emotional state', 'Physical appearance only, with no connection to thoughts or feelings', 'Name and age only', 'The setting of the story, with no connection to character'], 0),
   ('Why might a playwright use a monologue at a key moment in a story?', ['To give the audience deeper insight into a character’s internal experience', 'Monologues never provide insight into a character', 'This technique has no effect on audience understanding', 'Monologues are only used to describe unrelated settings'], 0),
   ('Which is an example of a strong opening line for a monologue exploring regret?', ['I keep thinking about that one moment I wish I could take back.', 'The weather today is quite pleasant.', 'This is a random, unrelated statement.', 'A line with no emotional connection to the character.'], 0),
   ('Why does writing an effective monologue require careful attention to voice and tone?', ['The monologue should authentically reflect that specific character’s personality and emotional state', 'Voice and tone have no connection to writing a monologue', 'Monologues should always sound identical regardless of character', 'This type of writing requires no consideration of character'], 0)]),
M('Precision, Accuracy, and Error in Measurement',
  'Grade 9 Measurement strand: precision refers to how consistent repeated measurements are, accuracy refers to how close a measurement is to the true value, and error describes the difference between a measured and true value.',
  [('Precision in measurement refers to ___.', ['How consistent repeated measurements are with each other', 'How close a measurement is to the true value', 'A measurement with no connection to consistency', 'The exact colour of a measured object'], 0),
   ('Accuracy in measurement refers to ___.', ['How close a measurement is to the true value', 'How consistent repeated measurements are with each other', 'A concept unrelated to true values', 'Only the units used in a measurement'], 0),
   ('It is possible for a set of measurements to be precise but not accurate if they are ___.', ['Consistently close to each other but consistently far from the true value', 'Always exactly equal to the true value', 'Completely random with no consistency', 'Impossible to measure at all'], 0),
   ('Measurement error describes ___.', ['The difference between a measured value and the true value', 'A value that is always exactly zero', 'A concept unrelated to measurement', 'Only errors caused by faulty equipment, with no other causes'], 0),
   ('Why is distinguishing between precision and accuracy important in scientific measurement?', ['It helps scientists understand the reliability and validity of their data', 'These two concepts are always identical in meaning', 'Precision and accuracy have no connection to scientific measurement', 'This distinction has no practical use in science'], 0)]),
Sc('Population Ecology: Growth Models',
   'Grade 9 Science Biology strand: population ecology studies how populations change over time, using models such as exponential growth, which assumes unlimited resources, and logistic growth, which accounts for environmental limits.',
   [('Population ecology studies how ___ change over time.', ['Populations of organisms', 'Only individual organisms, with no connection to populations', 'A concept unrelated to biology', 'Only non-living systems'], 0),
    ('Exponential growth models assume ___.', ['Unlimited resources are available', 'Resources are always extremely limited', 'No population growth occurs at all', 'A concept unrelated to population size'], 0),
    ('Logistic growth models account for ___.', ['Environmental limits on population growth', 'Unlimited resources with no environmental constraints', 'A concept unrelated to population ecology', 'Only exponential increases with no limiting factors'], 0),
    ('Why might a population’s growth rate slow down as it approaches an environment’s carrying capacity?', ['Limited resources, such as food and space, can restrict further population growth', 'Carrying capacity has no effect on population growth rate', 'Populations always continue growing exponentially with no limits', 'Resource availability has no connection to population size'], 0),
    ('Why are population growth models useful in ecology?', ['They help predict and understand how populations might change under different conditions', 'These models have no scientific value', 'Population changes can never be predicted or modeled', 'This topic has no connection to understanding ecosystems'], 0)]),
SS('Regional Integration: Case Studies',
   'Grade 9 Social Studies (Geography) strand: regional integration occurs when countries in a geographic area, such as through the European Union or ASEAN, cooperate closely on economic and political matters.',
   [('Regional integration involves countries in a geographic area cooperating closely on ___.', ['Economic and political matters', 'No shared matters of any kind', 'A concept unrelated to international relationships', 'Only unrelated cultural traditions'], 0),
    ('Which is an example of a regional integration organization?', ['The European Union', 'A single, isolated country with no connections to others', 'An organization unrelated to regional cooperation', 'A concept that has never actually existed'], 0),
    ('Why might countries in a region choose to pursue closer economic integration?', ['It can create shared benefits like easier trade and coordinated economic policy', 'Regional integration provides no benefits to member countries', 'Countries never choose to cooperate on economic matters', 'Economic integration always harms every member country involved'], 0),
    ('Why is studying regional integration case studies valuable for understanding global geography?', ['It illustrates real-world examples of how countries cooperate across a shared region', 'Regional integration has no connection to geography', 'Case studies provide no useful insight into global cooperation', 'This topic has no relevance to understanding international relationships'], 0),
    ('Which is a potential challenge countries might face when pursuing regional integration?', ['Balancing shared goals with individual national interests', 'Regional integration never presents any challenges', 'Countries never have differing interests within a region', 'This process always proceeds with no complications'], 0)])]),

day(50, [
L('Reading: Synthesizing Across a Text Set',
  'Grade 9 Reading strand: a text set is a group of related texts on a common topic, and synthesizing across them involves combining ideas and evidence from each to form a broader, more complete understanding.',
  [('A text set is best described as ___.', ['A group of related texts on a common topic', 'A single isolated text with no connection to others', 'A collection of completely unrelated texts', 'A concept unrelated to reading comprehension'], 0),
   ('Synthesizing across a text set involves ___.', ['Combining ideas and evidence from multiple texts into a broader understanding', 'Reading only one text and ignoring all others in the set', 'Copying one text exactly with no analysis', 'Ignoring all texts in the set completely'], 0),
   ('Why might a teacher assign a text set on a single topic rather than just one text?', ['It allows students to build a more complete understanding through multiple perspectives', 'A single text always provides a complete understanding of any topic', 'Text sets have no educational value', 'Multiple texts on the same topic never add any useful insight'], 0),
   ('When synthesizing a text set, a reader should look for ___.', ['Connections, agreements, and disagreements across the texts', 'Only identical information repeated in every text', 'Nothing related to the texts’ content', 'Random, unrelated facts with no connections'], 0),
   ('Why is synthesizing across a text set considered an advanced literacy skill?', ['It requires comparing, connecting, and combining ideas from multiple sources into a new understanding', 'This skill requires no understanding of any individual text', 'It only involves reading a single sentence from one text', 'Synthesizing has no connection to critical thinking'], 0)]),
M('Review: Quadratics, Rational Expressions, and Non-Linear Relations',
  'Grade 9 Algebra strand review: this lesson revisits the quadratic formula, completing the square, simplifying rational expressions, the equation of a circle, and cubic functions from recent lessons.',
  [('The quadratic formula can be used to solve equations in the form ___.', ['ax squared plus bx plus c equals zero', 'ax plus b equals zero', 'a plus b equals c', 'a divided by b equals c'], 0),
   ('Completing the square is a method used to ___.', ['Rewrite a quadratic expression to reveal its vertex', 'Simplify a linear equation only', 'Solve for the perimeter of a shape', 'A method unrelated to quadratic expressions'], 0),
   ('The equation of a circle centred at the origin is ___.', ['x squared plus y squared equals r squared', 'x plus y equals r', 'x squared minus y squared equals r', 'x times y equals r squared'], 0),
   ('A cubic function includes a variable raised to the power of ___.', ['Three', 'One', 'Two', 'Zero'], 0),
   ('Why is it useful to review quadratics, rational expressions, and non-linear relations together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Chemistry, Physics, and Biology Concepts',
   'Grade 9 Science review: this lesson revisits stoichiometry, momentum, cellular respiration, organic chemistry, and population ecology covered across recent lessons.',
   [('Stoichiometry uses mole ratios to calculate ___.', ['The amounts of reactants and products in a reaction', 'The colour of a chemical reaction', 'The exact temperature of a reaction', 'A value unrelated to chemical reactions'], 0),
    ('Momentum is calculated as ___.', ['Mass times velocity', 'Mass divided by velocity', 'Mass plus velocity', 'Velocity alone, with no connection to mass'], 0),
    ('Cellular respiration breaks down ___ to release usable energy.', ['Glucose', 'Water only', 'Oxygen only', 'Carbon dioxide only'], 0),
    ('Organic chemistry is the study of compounds based primarily on ___.', ['Carbon', 'Oxygen only', 'Helium', 'A concept unrelated to any specific element'], 0),
    ('Why is it valuable to review chemistry, physics, and biology concepts together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: Global Geography, Resources, and Regional Cooperation',
   'Grade 9 Social Studies (Geography) review: this lesson revisits resource conflict, pandemic geography, the Arctic, food systems, the digital divide, and regional integration covered across recent lessons.',
   [('A resource war generally involves conflict over ___.', ['Access to or control of limited resources', 'A topic entirely unrelated to resources', 'Only cultural traditions, with no resource connection', 'A conflict with no identifiable cause'], 0),
    ('The Arctic has become an area of increasing geopolitical interest partly due to ___.', ['Access to resources and shipping routes', 'A complete lack of any valuable resources', 'No connection to international interest', 'A topic unrelated to geopolitics'], 0),
    ('A food system involves the geographic network of ___.', ['Growing, processing, transporting, and distributing food', 'A single unrelated activity with no connection to food', 'Only food consumption, with no other stages considered', 'A concept unrelated to geography'], 0),
    ('The digital divide refers to ___.', ['Unequal access to technology and the internet across regions and populations', 'Equal access to technology everywhere in the world', 'A concept unrelated to technology access', 'A divide unrelated to geography or economics'], 0),
    ('Why is it useful to review global geography, resources, and regional cooperation together?', ['It helps reinforce how these interconnected issues shape global patterns and relationships', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260722):
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
    _rebalance_answer_positions(g9_41_50)
    append_to(9, g9_41_50)
