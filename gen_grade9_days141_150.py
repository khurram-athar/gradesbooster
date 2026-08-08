#!/usr/bin/env python3
"""Grade 9, Days 141-150 -- extends Grade 9 from 140 to 150 days. Topics
chosen after dumping and reading the full Day 1-140 title list (data/grade9.json)
to avoid any overlap, which by this point is exhaustive across all four
subjects: dangling and misplaced modifiers, polysemy, in medias res, writing
an investigative journalism article, analyzing data visualization and
infographics, reported (indirect) speech, the eulogy and tribute speech,
onomatopoeia and sound symbolism, and anachronism in literature; solving
exponential equations, Diophantine equations, the cross product of vectors,
Markov chains, confidence intervals, present and future value of annuities,
infinite geometric series, the definite integral, and converting between
polar and rectangular coordinates; acid-base titration and pH curves, fluid
pressure and Pascals Principle, the human reproductive system, glaciers and
glacial landforms, stellar nucleosynthesis, animal behaviour (instinct vs
learned), organic functional groups, rotational kinetic energy and angular
momentum, and rivers and fluvial landforms; the geography of landlocked
countries and transit corridors, geothermal energy resources, continental
shelves and maritime boundaries, sovereign wealth funds, green hydrogen,
UN peacekeeping and buffer zones, global currency unions, internet
governance and digital sovereignty, and sister cities and municipal
diplomacy. Day 150 is a cross-subject review day drawing quiz content from
Days 141-149 of this same batch.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches); SocialStudies
content is Geography-focused, matching the existing convention.

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided entirely (e.g.
"Pascals Principle" not "Pascal's Principle", "Earths" not "Earth's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


def _rebalance_answer_positions(days, seed=20260807):
    import random
    rng = random.Random(seed)
    quizzes = [sub_entry[5] for _, subs in days for sub_entry in subs]
    n = sum(len(q) for q in quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in quizzes:
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
    return days


g9_141_150 = [
day(141, [
L('Grammar: Dangling and Misplaced Modifiers',
  'Grade 9 Language strand: a dangling modifier fails to attach logically to any word in a sentence, while a misplaced modifier is placed too far from the word it is meant to describe, and both errors can confuse or unintentionally amuse a reader.',
  [('What is a dangling modifier?', ['A modifier that does not clearly and logically attach to any word in the sentence', 'A word that has no meaning at all', 'A punctuation mark that separates two clauses', 'A verb that has no subject'], 0),
   ('What is a misplaced modifier?', ['A modifier placed too far from the word it is meant to describe, creating confusion', 'A modifier that is always grammatically correct', 'A noun with no article in front of it', 'A sentence with no punctuation at all'], 0),
   ('Which sentence correctly avoids a dangling modifier?', ['While I was walking to school, the rain began to fall.', 'Walking to school, the rain began to fall.', 'Walking to school the rain, began to fall.', 'The rain, walking to school, began to fall.'], 0),
   ('Why should modifiers be placed near the word they describe?', ['To avoid confusing or unintentionally humorous readings of a sentence', 'Because word order never affects meaning in English', 'Because modifiers cannot appear anywhere else in a sentence', 'To make a sentence longer for no particular reason'], 0),
   ('How can a writer fix a dangling modifier?', ['By adding a clear subject for the modifier to describe, often by rewording the clause', 'By deleting every modifier from the sentence entirely', 'By moving the modifier to the very end of the paragraph', 'By replacing the modifier with a random noun'], 0)]),
M('Algebra: Solving Exponential Equations',
  'Grade 9 Math strand: an exponential equation has the variable in the exponent, and it can be solved by rewriting both sides with a common base and setting the exponents equal, or by applying logarithms when a common base cannot easily be found.',
  [('What defines an exponential equation?', ['An equation in which the variable appears in the exponent', 'An equation with no exponents of any kind', 'An equation that only involves whole number coefficients', 'An equation that cannot be graphed'], 0),
   ('If both sides of an exponential equation are rewritten with equal bases, what can then be done?', ['The exponents can be set equal to each other and solved directly', 'The bases must be multiplied together first', 'Nothing further can be done to solve the equation', 'The equation becomes impossible to solve'], 0),
   ('When the bases of an exponential equation cannot easily be made equal, what tool is commonly used instead?', ['Logarithms', 'Long division', 'The distributive property alone', 'A protractor'], 0),
   ('Solve for x: 2^x = 8.', ['x = 3', 'x = 4', 'x = 2', 'x = 8'], 0),
   ('Why must the base of an exponential equation be positive and not equal to one?', ['So the exponential function is well defined and produces a consistent, predictable output for each exponent', 'Because negative numbers cannot appear anywhere in mathematics', 'Because the base has no effect on the equations solutions', 'So the equation always has infinitely many solutions'], 0)]),
Sc('Chemistry: Acid-Base Titration and pH Curves',
   'Grade 9 Science strand: titration is a technique used to determine the unknown concentration of an acid or base by carefully adding a solution of known concentration until the reaction reaches its equivalence point, often tracked with an indicator or a pH curve.',
   [('What is the goal of an acid-base titration?', ['To determine the unknown concentration of an acid or base solution', 'To permanently change the colour of a solution with no other purpose', 'To measure the temperature of a chemical reaction only', 'To separate a mixture into its individual elements'], 0),
    ('What is the equivalence point in a titration?', ['The point at which the acid and base have reacted in exactly stoichiometric proportions', 'The point at which the reaction has not yet begun', 'The point at which the solution becomes solid', 'The point at which the container is completely empty'], 0),
    ('What tool can be used to signal the endpoint of a titration by changing colour?', ['An indicator', 'A thermometer', 'A microscope', 'A balance'], 0),
    ('What does a pH curve plot during a titration?', ['The pH of the solution against the volume of titrant added', 'The colour of the solution against the room temperature', 'The mass of the flask against the time of day', 'The volume of titrant against the size of the beaker'], 0),
    ('Why does the pH change rapidly near the equivalence point of a strong acid-strong base titration?', ['A small addition of titrant causes a large shift in the ratio of acid to base present, producing a steep pH change', 'The pH never changes at any point during a titration', 'The reaction stops completely before the equivalence point', 'Temperature is the only factor that affects pH during titration'], 0)]),
SS('Social Studies: The Geography of Landlocked Countries and Transit Trade Corridors',
   'Grade 9 Social Studies (Geography) strand: a landlocked country has no direct access to an ocean coastline, so it typically depends on transit trade corridors and agreements with neighbouring countries to move goods to and from global shipping routes.',
   [('What defines a landlocked country?', ['A country that has no direct access to an ocean coastline', 'A country located entirely on an island', 'A country with the longest coastline in the world', 'A country that has banned all forms of international trade'], 0),
    ('Why do landlocked countries often rely on transit trade agreements with neighbouring countries?', ['To gain access to ports and shipping routes through a neighbouring countrys territory', 'Because landlocked countries never engage in any international trade', 'Because neighbouring countries are never willing to cooperate', 'To avoid using any form of ocean shipping permanently'], 0),
    ('What economic challenge do many landlocked countries commonly face?', ['Higher transportation costs for imports and exports compared to coastal countries', 'Automatically lower transportation costs than any coastal country', 'A complete inability to trade with any other nation', 'No connection whatsoever to the global economy'], 0),
    ('What is a transit corridor?', ['A designated route, often crossing another countrys territory, used to move goods to and from a landlocked country', 'A type of mountain range found only near the equator', 'A river that never connects to any ocean', 'A border that cannot be crossed under any circumstances'], 0),
    ('Why might a landlocked countrys relationship with its neighbours be especially important economically?', ['Its access to global trade routes depends heavily on cooperation with the countries surrounding it', 'Landlocked countries have no need for any neighbouring cooperation', 'Its economy is entirely disconnected from its geographic location', 'Neighbouring countries have no influence on trade routes at all'], 0)]),
]),
day(142, [
L('Vocabulary: Polysemy and Words with Multiple Meanings',
  'Grade 9 Language strand: polysemy occurs when a single word carries two or more related meanings, and recognizing polysemy helps a reader determine which sense of a word fits the surrounding context.',
  [('What is polysemy?', ['When a single word has two or more related meanings', 'When a word has absolutely no meaning at all', 'When two unrelated words happen to be spelled identically', 'When a sentence contains no verbs whatsoever'], 0),
   ('How does polysemy differ from a homonym?', ['Polysemous meanings are historically related, while homonyms usually come from unrelated origins that happen to sound alike', 'Polysemy and homonyms are exactly the same concept with no difference', 'Homonyms always share a related historical origin, unlike polysemous words', 'Polysemy only applies to punctuation marks, never to words'], 0),
   ('The word head, meaning both a persons head and the head of a company, illustrates what concept?', ['Polysemy, since the meanings share a related core idea of a leading or top part', 'A grammatical error with no linguistic explanation', 'A punctuation rule about capitalization', 'A rule that applies only to proper nouns'], 0),
   ('Why is polysemy useful to understand when reading?', ['It helps a reader determine which related meaning of a word fits the surrounding context', 'It guarantees that every word has only one possible meaning', 'It eliminates the need to consider context while reading', 'It only applies to words found in poetry'], 0),
   ('Which resource can help identify the different senses of a polysemous word?', ['A dictionary entry listing multiple numbered definitions for one word', 'A map showing the geographic origin of a word', 'A calculator used to count syllables', 'A calendar showing when a word was first spoken'], 0)]),
M('Number Theory: An Introduction to Diophantine Equations',
  'Grade 9 Math strand: a Diophantine equation is an equation for which only integer solutions are sought, and a linear Diophantine equation of the form ax + by = c has an integer solution exactly when the greatest common divisor of a and b divides evenly into c.',
  [('What is a Diophantine equation?', ['An equation for which only integer solutions are sought', 'An equation that has no solutions of any kind', 'An equation that can only be solved using decimals', 'An equation with no variables whatsoever'], 0),
   ('A linear Diophantine equation ax + by = c has an integer solution only when what condition is met?', ['The greatest common divisor of a and b divides evenly into c', 'The variables a and b must both equal zero', 'The equation must contain no constant term at all', 'The value of c must always be a negative number'], 0),
   ('Why are Diophantine equations named after Diophantus?', ['He was an ancient mathematician known for studying equations restricted to integer solutions', 'He was a modern computer scientist who invented the calculator', 'He was a geographer who mapped the ancient world', 'He had no historical connection to mathematics at all'], 0),
   ('Which of these is an example of a linear Diophantine equation?', ['3x + 5y = 11', 'x^2 + y^2 = 11', 'sin(x) = 11', 'x/0 = 11'], 0),
   ('What real-world type of problem often requires a Diophantine equation?', ['A problem where only whole-number quantities make sense, such as counting items', 'A problem that only involves measuring continuous quantities like time', 'A problem that has no numerical component at all', 'A problem that can only be solved using irrational numbers'], 0)]),
Sc('Physics: Fluid Pressure and Pascals Principle',
   'Grade 9 Science strand: fluid pressure increases with depth, and Pascals Principle states that pressure applied to an enclosed fluid is transmitted equally in all directions, a concept used in hydraulic systems to multiply force.',
   [('What does Pascals Principle state?', ['Pressure applied to an enclosed fluid is transmitted equally in all directions throughout the fluid', 'Pressure applied to a fluid disappears instantly with no effect', 'Fluids can never transmit pressure of any kind', 'Pressure in a fluid only travels in a single fixed direction'], 0),
    ('What happens to fluid pressure as depth increases?', ['Fluid pressure increases with depth', 'Fluid pressure decreases with depth', 'Fluid pressure remains exactly zero at every depth', 'Depth has no effect on fluid pressure whatsoever'], 0),
    ('What everyday device relies on Pascals Principle to multiply force?', ['A hydraulic lift or hydraulic brake system', 'A simple pulley with no fluid involved', 'A magnifying glass', 'A tuning fork'], 0),
    ('What units are commonly used to measure pressure?', ['Pascals', 'Litres', 'Newtons per second', 'Degrees Celsius'], 0),
    ('In a hydraulic system, why does a small force on a small piston create a larger force on a larger piston?', ['Because pressure is transmitted equally, and force equals pressure multiplied by area, so a larger area produces a larger force', 'Because larger pistons always weigh less than smaller pistons', 'Because pressure decreases automatically as piston size increases', 'Because hydraulic fluid removes all force from the system'], 0)]),
SS('Social Studies: The Geography of Geothermal Energy Resources',
   'Grade 9 Social Studies (Geography) strand: geothermal energy harnesses heat stored beneath the Earths surface, and geothermal resources are most concentrated near tectonic plate boundaries and volcanically active regions, where the heat can be used for electricity and direct heating.',
   [('What is geothermal energy?', ['Energy harnessed from heat stored beneath the Earths surface', 'Energy generated exclusively from burning coal', 'Energy captured only from moving ocean waves', 'Energy created by reflecting sunlight off mirrors'], 0),
    ('Where are geothermal energy resources most commonly concentrated?', ['Near tectonic plate boundaries and volcanically active regions', 'Only in the centre of large, flat deserts', 'Only along the equator with no connection to geology', 'Only in regions with no volcanic history whatsoever'], 0),
    ('What are two common uses of geothermal energy?', ['Generating electricity and providing direct heating', 'Powering sailboats and printing newspapers', 'Building bridges and paving roads', 'Freezing water and cooling office buildings only'], 0),
    ('Why is geothermal energy generally considered a renewable resource?', ['The heat within the Earth is continuously replenished and available on a human timescale', 'It is mined once and then permanently used up', 'It depends entirely on daily weather conditions', 'It can only be used once before disappearing forever'], 0),
    ('Which country is well known for generating a large share of its electricity from geothermal sources due to its volcanic geology?', ['Iceland', 'Egypt', 'Mongolia', 'The Netherlands'], 0)]),
]),
day(143, [
L('Reading: Analyzing In Medias Res and Narrative Beginnings',
  'Grade 9 Language strand: in medias res means beginning a narrative in the middle of the action rather than at the start of events, often followed later by a flashback that fills in the missing earlier background.',
  [('What does in medias res mean?', ['Beginning a narrative in the middle of the action rather than at the start of events', 'Ending a narrative before any action has occurred', 'Telling a story entirely through dialogue with no narration', 'Skipping the ending of a story entirely'], 0),
   ('What technique often supplies the missing earlier events after a story opens in medias res?', ['Flashback used to fill in earlier background information', 'A glossary placed at the end of the book', 'A table of contents listing every character', 'A footnote citing an unrelated source'], 0),
   ('Why might an author choose to open a story in medias res?', ['To immediately capture the readers attention with tension or action', 'To make the story impossible for any reader to understand', 'To avoid including any characters in the story at all', 'To ensure the story has no identifiable setting'], 0),
   ('A story that opens with a characters birth and proceeds strictly in chronological order is an example of what?', ['Not starting in medias res', 'A classic example of in medias res', 'A story with no beginning at all', 'A purely nonlinear narrative structure'], 0),
   ('What risk does an author take by opening a story in medias res?', ['Readers may feel confused until enough context is revealed', 'Readers will always understand every detail immediately', 'The story becomes impossible to write in any language', 'The story can no longer contain any characters'], 0)]),
M('Geometry: The Cross Product of Vectors',
  'Grade 9 Math strand: the cross product of two vectors produces a new vector that is perpendicular to both original vectors, with a magnitude equal to the area of the parallelogram they form, distinguishing it from the dot product, which produces a scalar.',
  [('What kind of quantity results from taking the cross product of two vectors?', ['A new vector that is perpendicular to both original vectors', 'A single number with no direction at all', 'A colour representing the vectors', 'An angle measured in degrees only'], 0),
   ('How does the cross product differ from the dot product of two vectors?', ['The cross product produces a vector, while the dot product produces a scalar', 'The cross product always produces zero, while the dot product never does', 'The dot product produces a vector, while the cross product produces a scalar', 'There is no difference between the two operations at all'], 0),
   ('What does the magnitude of the cross product of two vectors represent geometrically?', ['The area of the parallelogram formed by the two vectors', 'The length of a single straight line segment only', 'The volume of a sphere with no connection to the vectors', 'The angle between the two vectors measured in radians'], 0),
   ('In three-dimensional space, the cross product of two parallel vectors produces what result?', ['A zero vector, since there is no unique perpendicular direction', 'A vector with infinite magnitude', 'The same two original vectors unchanged', 'A scalar equal to the sum of the two vectors'], 0),
   ('Which rule is commonly used to determine the direction of a cross product vector?', ['The right-hand rule', 'The Pythagorean theorem', 'The order of operations', 'The quadratic formula'], 0)]),
Sc('Biology: The Human Reproductive System and Human Development',
   'Grade 9 Science strand: the human reproductive system produces reproductive cells and supports the development of offspring, beginning with fertilization and continuing through the distinct stages of prenatal development inside the uterus.',
   [('What is the primary function of the human reproductive system?', ['To produce reproductive cells and support the development of offspring', 'To regulate body temperature exclusively', 'To digest food and absorb nutrients', 'To filter waste out of the bloodstream'], 0),
    ('What is fertilization?', ['The fusion of a sperm cell and an egg cell to form a zygote', 'The process of breaking down food into nutrients', 'The division of a single muscle cell into two identical cells', 'The process by which bones grow longer over time'], 0),
    ('What is gestation?', ['The period of development of an embryo and fetus inside the uterus before birth', 'The process of breathing in and out repeatedly', 'The circulation of blood through the heart', 'The process of digesting a meal after eating'], 0),
    ('Which structure in the female reproductive system is where fertilization typically occurs?', ['The fallopian tube', 'The stomach', 'The trachea', 'The liver'], 0),
    ('Why is prenatal development divided into distinct stages, such as embryonic and fetal periods?', ['Because different developmental processes, such as organ formation and growth, occur predominantly during each stage', 'Because prenatal development actually happens in a single instant with no stages', 'Because the stages have no biological basis and are purely arbitrary', 'Because only one stage of prenatal development has ever been observed'], 0)]),
SS('Social Studies: The Geography of Continental Shelves and Maritime Boundaries',
   'Grade 9 Social Studies (Geography) strand: a continental shelf is the shallow seabed extending from a coastline, and international agreements such as the United Nations Convention on the Law of the Sea establish exclusive economic zones and maritime boundaries governing resource rights over these often valuable areas.',
   [('What is a continental shelf?', ['The shallow, gently sloping seabed that extends outward from a coastline before dropping to the deep ocean floor', 'A mountain range located entirely inland with no connection to the coast', 'A type of river delta found only in tropical regions', 'A structure built entirely by human engineers to store water'], 0),
    ('What is an exclusive economic zone (EEZ)?', ['A maritime zone extending from a coastline in which a country has special rights over resource exploration and use', 'A zone where no country has any legal rights at all', 'A zone reserved exclusively for recreational swimming', 'A zone that applies only to landlocked countries'], 0),
    ('What international agreement establishes rules for maritime boundaries and ocean resource rights?', ['The United Nations Convention on the Law of the Sea (UNCLOS)', 'The Antarctic Treaty System', 'A single countrys domestic law with no international application', 'An agreement that governs only air travel routes'], 0),
    ('Why are continental shelves often economically valuable?', ['They frequently contain rich fishing grounds and deposits of oil and natural gas', 'They contain no natural resources of any kind', 'They are always too deep for any economic activity to occur', 'They have no connection to fishing or energy resources'], 0),
    ('Why can overlapping continental shelf claims lead to international disputes?', ['Multiple countries may claim rights to the same resource-rich seabed area', 'Continental shelves never overlap between different countries', 'International law has never addressed maritime boundaries', 'Seabed resources are always evenly divided with no possibility of dispute'], 0)]),
]),
day(144, [
L('Writing: Writing an Investigative Journalism Article',
  'Grade 9 Language strand: investigative journalism involves researching and exposing information that is often hidden, using verified evidence from multiple credible sources, and structuring an article around a clear, well-supported lede.',
  [('What is the primary goal of investigative journalism?', ['To research and expose information that is often hidden or not widely known, holding people or institutions accountable', 'To publish only opinions with no supporting evidence', 'To avoid researching any topic in depth', 'To repeat information exactly as given by a single source with no verification'], 0),
   ('What must a writer confirm before publishing a claim in an investigative article?', ['That the claim is supported by verified evidence from credible sources', 'That the claim sounds interesting, regardless of accuracy', 'That the claim has never been questioned by anyone', 'That the claim was made by a famous person'], 0),
   ('What is a lede in journalism?', ['The opening section of an article that summarizes the most important information', 'The final sentence of an article with no other purpose', 'A footnote citing a source at the bottom of the page', 'A photograph included without any caption'], 0),
   ('Why do investigative journalists often rely on multiple independent sources?', ['To confirm facts and reduce the risk of relying on a single, possibly biased, account', 'Because a single source is always considered sufficient evidence', 'Because multiple sources are required only for fictional stories', 'To make an article longer with no concern for accuracy'], 0),
   ('What ethical responsibility do investigative journalists carry?', ['To report accurately and fairly, avoiding unsupported claims that could harm someones reputation', 'To publish any claim regardless of whether it can be verified', 'To avoid fact-checking any information before publication', 'To favour one side of a story without providing any evidence'], 0)]),
M('Data Management: An Introduction to Markov Chains',
  'Grade 9 Math strand: a Markov chain models a sequence of states in which the probability of moving to the next state depends only on the current state, a memoryless property captured in a transition matrix of probabilities.',
  [('What is a defining feature of a Markov chain?', ['The probability of moving to the next state depends only on the current state, not on earlier history', 'Every future state depends equally on all previous states combined', 'A Markov chain can only ever have a single possible state', 'The probabilities in a Markov chain are always identical for every state'], 0),
   ('What is this memoryless property of a Markov chain often called?', ['The Markov property', 'The Pythagorean property', 'The commutative property', 'The associative property'], 0),
   ('What do the numbers in a transition matrix of a Markov chain represent?', ['The probabilities of moving from one state to each possible next state', 'The exact distance between two unrelated cities', 'The total population of a randomly chosen country', 'The temperature recorded at a specific location'], 0),
   ('Which of the following could be modeled using a Markov chain?', ['Predicting tomorrows weather based only on todays weather', 'Calculating the exact area of a triangle', 'Measuring the length of a straight line segment', 'Converting Fahrenheit to Celsius'], 0),
   ('In a transition matrix, what should the probabilities in each row sum to?', ['One', 'Zero', 'One hundred', 'Negative one'], 0)]),
Sc('Earth Science: Glaciers and Glacial Landforms',
   'Grade 9 Science strand: a glacier forms when accumulated snow compacts into dense ice that flows under its own weight, and as it moves it erodes and deposits material, carving landforms such as U-shaped valleys, moraines, and fjords.',
   [('How does a glacier form?', ['Snow accumulates and compacts over time into dense ice that begins to flow under its own weight', 'Ice forms instantly with no gradual accumulation of snow at all', 'A glacier forms only from ocean water freezing directly', 'A glacier forms exclusively through volcanic activity'], 0),
    ('What landform is created when a glacier carves a valley into a U-shape?', ['A glacial (U-shaped) valley', 'A river delta', 'A sand dune', 'A coral reef'], 0),
    ('What is a moraine?', ['A ridge of rock and sediment deposited by a glacier', 'A type of cloud found only over mountains', 'A warm ocean current near the equator', 'A crater formed by a meteorite impact'], 0),
    ('What is a fjord?', ['A deep, narrow coastal inlet carved by a glacier and later flooded by the sea', 'A flat, dry plain found in a desert', 'A tall, narrow waterfall with no connection to glaciers', 'A wide, shallow lake found only in tropical regions'], 0),
    ('Why can glaciers be considered powerful agents of erosion?', ['Their immense weight and slow movement can grind and reshape the underlying landscape over long periods of time', 'Glaciers never move and therefore cause no erosion at all', 'Glaciers only affect landscapes located far from any mountains', 'Glacial ice has no measurable weight or mass'], 0)]),
SS('Social Studies: The Geography of Sovereign Wealth Funds and Resource Wealth',
   'Grade 9 Social Studies (Geography) strand: a sovereign wealth fund is a state-owned investment fund, often built from resource revenue such as oil exports, that many resource-rich countries use to save and invest wealth for future generations rather than spending it all at once.',
   [('What is a sovereign wealth fund?', ['A state-owned investment fund, often built from revenue such as natural resource exports', 'A private savings account belonging to a single individual', 'A fund that only foreign corporations are legally allowed to use', 'A charity fund with no connection to any government'], 0),
    ('Why do many resource-rich countries establish sovereign wealth funds?', ['To save and invest resource revenue for future generations rather than spending it all immediately', 'To immediately spend all resource revenue with no long-term planning', 'Because international law requires every country to create one', 'To avoid ever investing in any financial asset'], 0),
    ('What type of resource revenue commonly funds many of the worlds largest sovereign wealth funds?', ['Oil and natural gas revenue', 'Revenue from tourism alone, with no other source', 'Revenue collected exclusively from parking fees', 'Revenue generated only from selling agricultural land'], 0),
    ('What is one benefit of a sovereign wealth fund during a period of low resource prices?', ['It can provide a financial buffer that helps stabilize government revenue', 'It guarantees resource prices will immediately rise again', 'It eliminates the need for any government budget planning', 'It has no effect whatsoever on a countrys finances'], 0),
    ('How can a sovereign wealth fund relate to the concept of the resource curse discussed earlier in this course?', ['A well-managed fund can help a country avoid over-reliance on volatile resource revenue, reducing the risk of the resource curse', 'A sovereign wealth fund always causes the resource curse to worsen', 'The resource curse and sovereign wealth funds are entirely unrelated concepts', 'Sovereign wealth funds can only exist in countries with no natural resources'], 0)]),
]),
day(145, [
L('Media Literacy: Analyzing Data Visualization and Infographics',
  'Grade 9 Language strand: infographics and charts present complex information visually, but a manipulated axis scale or cherry-picked data can mislead a viewer, so careful readers check a visualizations source, labels, and scale before trusting its message.',
  [('What is the purpose of a well-designed infographic?', ['To present complex information visually so it is easier to understand quickly', 'To make information as confusing as possible for the reader', 'To replace all written text in every document', 'To remove any need for accurate data entirely'], 0),
   ('How can a chart with a manipulated axis scale mislead a viewer?', ['It can exaggerate or minimize differences between data points, distorting the true pattern', 'A manipulated axis scale has no effect on how a chart is interpreted', 'It always makes a chart perfectly accurate regardless of scale', 'It automatically corrects any errors in the underlying data'], 0),
   ('What should a careful reader check when evaluating a data visualization?', ['Whether the data source is credited and whether the scale and labels are accurate', 'Only the colours used in the chart, with nothing else considered', 'Whether the chart contains any images at all', 'The font size used for the chart title only'], 0),
   ('What is cherry-picking data?', ['Selecting only the data that supports a specific claim while ignoring contradicting data', 'Using every available data point without any selection at all', 'A method for collecting data that guarantees complete accuracy', 'Randomly generating data with no real-world basis'], 0),
   ('Why is context important when interpreting a graph or chart?', ['Without context, a viewer may misunderstand what the data actually represents', 'Context has no bearing on how a graph should be interpreted', 'Every graph is equally clear regardless of the context provided', 'Context is only relevant to written text, never to visual data'], 0)]),
M('Statistics: An Introduction to Confidence Intervals',
  'Grade 9 Math strand: a confidence interval estimates a range of values likely to contain the true population parameter, and a stated confidence level, such as 95 percent, describes how often intervals built this way would capture the true value if the sampling process were repeated.',
  [('What does a confidence interval estimate?', ['A range of values likely to contain the true population parameter', 'The exact, single true value of a population parameter with certainty', 'The total number of people surveyed in a study', 'The colour associated with a particular data set'], 0),
   ('What does a 95 percent confidence level generally indicate?', ['If the sampling process were repeated many times, about 95 percent of the resulting intervals would contain the true parameter', 'The result is true with absolutely no possibility of error', 'Exactly 95 percent of the population was directly surveyed', 'The interval is guaranteed to be wrong 95 percent of the time'], 0),
   ('What generally happens to a confidence interval as the sample size increases, all else equal?', ['The confidence interval becomes narrower', 'The confidence interval becomes wider with no exceptions', 'The confidence interval disappears entirely', 'Sample size has no effect on a confidence interval at all'], 0),
   ('Why is a confidence interval more informative than a single point estimate alone?', ['It communicates the uncertainty and likely range around the estimated value', 'A point estimate always provides more information than any interval', 'A confidence interval removes the need for any sample data', 'It guarantees the exact true value with no uncertainty at all'], 0),
   ('Which statistical concept from an earlier lesson is directly used to construct many confidence intervals?', ['The z-score, since it standardizes distance from the mean', 'The Euclidean algorithm', 'The distributive property', 'Sigma notation alone, with no other concept involved'], 0)]),
Sc('Astronomy: Stellar Nucleosynthesis and the Life Cycle of Elements',
   'Grade 9 Science strand: stellar nucleosynthesis is the process by which stars fuse lighter elements into heavier ones in their cores, and a supernova explosion can disperse these newly formed heavy elements throughout space to later become part of new stars, planets, and living things.',
   [('What is stellar nucleosynthesis?', ['The process by which stars fuse lighter elements into heavier ones in their cores', 'The process by which a star instantly disappears with no trace', 'A process that only occurs on the surface of planets', 'A process unrelated to the formation of any chemical elements'], 0),
    ('Which element do most stars primarily fuse during the main part of their lives?', ['Hydrogen, fused into helium', 'Gold, fused into silver', 'Oxygen, fused into nitrogen', 'Iron, fused into hydrogen'], 0),
    ('What event can disperse heavy elements created inside a massive star throughout space?', ['A supernova explosion', 'A gentle breeze on a planets surface', 'A lunar eclipse', 'A tidal wave in an ocean'], 0),
    ('Why is it often said that living things are made of star stuff?', ['Many of the heavier elements found in living organisms were originally forged inside stars', 'Living organisms contain no elements that originated in stars', 'All elements on Earth were created only after life first appeared', 'Stars have no connection whatsoever to the chemistry of life'], 0),
    ('What generally happens to the elements a star produces as it undergoes fusion over its lifetime?', ['Progressively heavier elements are formed as lighter ones are fused together', 'Elements become progressively lighter throughout a stars entire lifetime', 'A star produces only a single unchanging element forever', 'No new elements are ever formed inside a star'], 0)]),
SS('Social Studies: The Geography of Green Hydrogen and the Future of Energy',
   'Grade 9 Social Studies (Geography) strand: green hydrogen is a fuel produced through electrolysis powered by renewable electricity, and regions with abundant sun or wind resources are increasingly seen as attractive locations for large-scale green hydrogen production aimed at industries that are difficult to electrify directly.',
   [('What is green hydrogen?', ['Hydrogen fuel produced using electrolysis powered by renewable electricity', 'Hydrogen extracted directly from burning coal', 'A synthetic gas with no connection to renewable energy', 'Hydrogen that occurs naturally without any production process'], 0),
    ('Why is green hydrogen considered cleaner than hydrogen produced from fossil fuels?', ['Its production process does not rely on burning fossil fuels, reducing associated greenhouse gas emissions', 'It produces significantly more greenhouse gas emissions than fossil fuel-based hydrogen', 'It is identical in every way to hydrogen produced from coal', 'It requires burning large amounts of oil to produce'], 0),
    ('What geographic factor makes a region attractive for large-scale green hydrogen production?', ['Abundant access to renewable energy sources, such as strong sun or wind', 'A complete absence of any energy resources', 'A location far from any electrical infrastructure', 'A climate with no wind or sunlight at any time of year'], 0),
    ('What industrial process is used to split water into hydrogen and oxygen using electricity?', ['Electrolysis', 'Photosynthesis', 'Distillation', 'Combustion'], 0),
    ('Which sector is often discussed as a promising future use for green hydrogen due to the difficulty of electrifying it directly?', ['Heavy industry and long-distance transportation, such as shipping', 'Household lighting exclusively, with no other application', 'Only recreational activities with no industrial use', 'Sectors that already run entirely on solar panels'], 0)]),
]),
day(146, [
L('Grammar: Reported (Indirect) Speech',
  'Grade 9 Language strand: reported, or indirect, speech relays what someone said without quoting their exact words, typically shifting the verb tense backward and adjusting pronouns so they reflect who is currently speaking.',
  [('What is reported (indirect) speech?', ['Relaying what someone said without quoting their exact words directly', 'Quoting a speaker word for word using quotation marks', 'A type of punctuation used only in poetry', 'A grammatical rule that applies only to questions'], 0),
   ('How does verb tense typically shift when converting direct speech to reported speech?', ['The verb tense generally shifts backward, such as present becoming past', 'The verb tense always shifts forward into the future tense', 'Verb tense never changes when using reported speech', 'All verbs are removed entirely from reported speech'], 0),
   ('Which sentence is an example of reported speech?', ['She said that she was tired.', 'She said, I am tired.', 'Is she tired, she asked?', 'Tired, she said, I am.'], 0),
   ('Why might pronouns change when converting a quotation into reported speech?', ['The pronouns must reflect who is now speaking rather than the original speaker', 'Pronouns are always deleted entirely in reported speech', 'Reported speech never uses pronouns of any kind', 'Pronouns must always be capitalized in reported speech'], 0),
   ('When is direct speech, marked with quotation marks, preferred over reported speech?', ['When the exact original wording of the speaker needs to be preserved', 'When the speakers exact words are considered unimportant', 'When a writer wants to avoid quoting anyone at all', 'When the tense of the original statement must be changed'], 0)]),
M('Financial Literacy: Present Value and Future Value of Annuities',
  'Grade 9 Math strand: an annuity is a series of equal payments made at regular intervals, and its future value represents the total accumulated amount including interest, while its present value represents the equivalent lump sum today.',
  [('What is an annuity in financial mathematics?', ['A series of equal payments made at regular intervals over time', 'A single one-time payment with no future obligations', 'A type of insurance that covers only property damage', 'A loan that never requires repayment of any kind'], 0),
   ('What does the future value of an annuity represent?', ['The total accumulated value of all payments, including interest, at a future date', 'The value of a single payment made many years in the past', 'The exact number of payments made in a single year', 'A value that ignores interest entirely'], 0),
   ('What does the present value of an annuity represent?', ['The single lump-sum amount today that is equivalent to a series of future payments', 'The total value of an annuity after every payment has stopped', 'A value that has no connection to future payments at all', 'The interest rate applied to a single payment only'], 0),
   ('Why does the future value of an annuity generally exceed the simple sum of its payments?', ['Because each payment earns interest over the time it remains invested', 'Because interest is never applied to any of the payments', 'Because payments made later are always worth more than earlier ones with no interest involved', 'Because the number of payments always decreases over time'], 0),
   ('Which financial product is a common real-world example of an annuity?', ['A retirement plan that pays a fixed amount at regular intervals', 'A single purchase made only once with no repeated payments', 'A coin collected as a one-time souvenir', 'A textbook purchased for a single course'], 0)]),
Sc('Biology: Animal Behaviour: Instinct and Learned Behaviour',
   'Grade 9 Science strand: instinctive behaviour is innate and genetically programmed, requiring no prior learning, while learned behaviour is acquired through experience or observation and can be adjusted as an animal encounters new situations.',
   [('What is an instinctive behaviour?', ['A behaviour that is innate and genetically programmed, requiring no prior learning', 'A behaviour that can only be acquired through years of formal training', 'A behaviour that never appears in any animal species', 'A behaviour that changes completely every single day'], 0),
    ('What is a learned behaviour?', ['A behaviour that an animal acquires through experience or observation', 'A behaviour that is present at birth with no need for experience', 'A behaviour that is identical across every animal species', 'A behaviour that cannot be influenced by an animals environment'], 0),
    ('Which of the following is an example of an instinctive behaviour?', ['A sea turtle hatchling moving toward the ocean immediately after hatching', 'A dog learning to sit after repeated training sessions', 'A parrot learning to mimic a new phrase after months of practice', 'A student memorizing a list of vocabulary words'], 0),
    ('Which of the following is an example of a learned behaviour?', ['A dog sitting on command after repeated training', 'A spider spinning its first web with no prior experience', 'A newborn mammal instinctively seeking its mothers milk', 'A bird building its very first nest using an inherited pattern'], 0),
    ('Why might learned behaviours offer an advantage over purely instinctive ones in a changing environment?', ['Learned behaviours can be adjusted based on new experiences, allowing an animal to adapt to changing conditions', 'Learned behaviours are always identical to instinctive behaviours', 'Instinctive behaviours are always more flexible than learned ones', 'Learned behaviours cannot be changed once they are acquired'], 0)]),
SS('Social Studies: The Geography of Peacekeeping Missions and UN Buffer Zones',
   'Grade 9 Social Studies (Geography) strand: United Nations peacekeeping missions are deployed to help maintain peace and stability in regions affected by conflict, often establishing a neutral buffer zone that separates opposing forces and helps monitor a ceasefire along a contested border.',
   [('What is the general purpose of a United Nations peacekeeping mission?', ['To help maintain peace and stability in a region affected by conflict', 'To permanently occupy a country and replace its government', 'To eliminate the need for any international cooperation', 'To ensure that conflicts never end anywhere in the world'], 0),
    ('What is a buffer zone in the context of peacekeeping?', ['A neutral area separating opposing forces to help prevent renewed conflict', 'An area with no connection to any conflict whatsoever', 'A zone reserved exclusively for tourism and recreation', 'A region where peacekeeping forces are strictly forbidden from entering'], 0),
    ('Why might peacekeeping forces be stationed along a contested border?', ['To monitor a ceasefire and reduce the likelihood of renewed fighting between opposing sides', 'To encourage further fighting between opposing sides', 'Because contested borders never require any form of monitoring', 'To permanently close the border to all forms of travel'], 0),
    ('What type of consent do peacekeeping missions typically require from the countries involved?', ['The consent of the host country or parties to the conflict', 'No consent of any kind is ever required', 'Consent from a single unrelated country with no connection to the conflict', 'Consent from every country in the world simultaneously'], 0),
    ('Why is the geographic placement of a peacekeeping mission carefully planned?', ['To effectively separate opposing forces and monitor the most sensitive or contested areas', 'Geographic placement has no effect on a peacekeeping missions effectiveness', 'Peacekeeping missions are always placed randomly with no planning at all', 'Geographic placement only matters for missions with no connection to conflict'], 0)]),
]),
day(147, [
L('Writing: The Eulogy and Tribute Speech',
  'Grade 9 Language strand: a eulogy honours and celebrates the life of someone who has died, usually delivered at a memorial service in a respectful and heartfelt tone, often organized around a few central themes and specific anecdotes that help an audience connect emotionally.',
  [('What is the main purpose of a eulogy?', ['To honour and celebrate the life of a person who has died, usually at a memorial service', 'To criticize a person publicly with no regard for their memory', 'To provide a purely factual, unemotional biography with no personal reflection', 'To advertise an unrelated product or event'], 0),
   ('What tone is typically appropriate for a eulogy?', ['A respectful and heartfelt tone, though it can include lighter personal anecdotes', 'A tone that is deliberately sarcastic and mocking throughout', 'A tone with absolutely no emotion of any kind', 'A tone appropriate only for a formal business report'], 0),
   ('Why do eulogies often include specific anecdotes about the person?', ['Specific stories help the audience connect emotionally and remember the person vividly', 'Specific anecdotes are strictly forbidden in a eulogy', 'Anecdotes make a eulogy less meaningful to the audience', 'A eulogy should never include any personal details at all'], 0),
   ('What is a tribute speech, more broadly?', ['A speech that honours the achievements or character of a specific person', 'A speech that only discusses unrelated historical events', 'A speech given exclusively at sporting events', 'A speech that criticizes a persons character in detail'], 0),
   ('Why might a eulogy be organized around a few central themes about the person?', ['Organizing around themes helps unify the speech and highlight the persons most meaningful qualities', 'Themes have no place in a eulogy and should always be avoided', 'A eulogy is more effective when it includes no clear organization at all', 'Themes are only appropriate in a formal debate speech'], 0)]),
M('Sequences and Series: Infinite Geometric Series and Convergence',
  'Grade 9 Math strand: an infinite geometric series converges to a finite sum, given by a divided by one minus r, whenever the absolute value of the common ratio r is less than one, and it diverges otherwise since the terms no longer shrink toward zero.',
  [('Under what condition does an infinite geometric series converge to a finite sum?', ['When the absolute value of the common ratio is less than one', 'When the common ratio is exactly equal to ten', 'When every term in the series is negative', 'When the first term of the series equals zero'], 0),
   ('What is the formula for the sum of a convergent infinite geometric series with first term a and common ratio r?', ['a divided by (1 minus r)', 'a multiplied by r squared', 'a plus r divided by two', 'a minus r multiplied by n'], 0),
   ('What happens to an infinite geometric series if the absolute value of the common ratio is greater than or equal to one?', ['The series diverges and has no finite sum', 'The series always converges to zero', 'The series instantly becomes a finite arithmetic series', 'The series always converges to exactly one'], 0),
   ('What is the sum of the infinite series 1 + 1/2 + 1/4 + 1/8 + ...?', ['2', '1', '4', 'Infinity'], 0),
   ('Why must the common ratio be strictly between negative one and one for convergence?', ['Outside that range, the terms do not shrink toward zero, so the partial sums never settle on a finite value', 'A common ratio outside that range always produces a sum of exactly zero', 'The common ratio has no effect whatsoever on convergence', 'Any common ratio always results in a convergent series'], 0)]),
Sc('Chemistry: Organic Functional Groups and Their Properties',
   'Grade 9 Science strand: a functional group is a specific group of atoms within an organic molecule that is largely responsible for its characteristic chemical reactions, with common examples including the hydroxyl group found in alcohols and the carboxyl group found in carboxylic acids.',
   [('What is a functional group in organic chemistry?', ['A specific group of atoms within a molecule responsible for characteristic chemical reactions', 'A group of atoms with no influence on a molecules chemical behaviour', 'A term used only to describe inorganic compounds', 'A type of chemical bond found exclusively in metals'], 0),
    ('Which functional group is found in alcohols?', ['The hydroxyl group', 'The carboxyl group', 'The amine group', 'The nitro group'], 0),
    ('Which functional group is characteristic of carboxylic acids?', ['The carboxyl group', 'The hydroxyl group alone, with no other atoms', 'The halide group', 'The ketone group'], 0),
    ('Why do organic chemists focus on identifying functional groups within a molecule?', ['Functional groups largely determine how a molecule will chemically react', 'Functional groups have no influence on a molecules reactivity', 'Identifying functional groups is only relevant to inorganic chemistry', 'Functional groups only affect the colour of a molecule'], 0),
    ('Two molecules with the same functional group tend to share what property?', ['Similar characteristic chemical reactions and behaviours', 'Identical molecular mass in every case', 'No chemical similarities whatsoever', 'The exact same physical state at room temperature in every case'], 0)]),
SS('Social Studies: The Geography of Global Currency Unions and Exchange Rate Zones',
   'Grade 9 Social Studies (Geography) strand: a currency union is a group of countries that share a single common currency, such as the Eurozone, offering benefits like reduced exchange costs and easier trade, while member countries also give up the ability to set independent monetary policy.',
   [('What is a currency union?', ['A group of countries that share a single common currency', 'A single country with two competing currencies at the same time', 'A group of countries that have banned all forms of currency', 'A trade agreement that has no connection to any currency at all'], 0),
    ('What is a well-known example of a currency union?', ['The Eurozone, where multiple European countries use the euro', 'A single city that uses its own unique currency', 'A currency used only by a single individual', 'An agreement with no member countries at all'], 0),
    ('What is one potential economic benefit of joining a currency union?', ['Reduced currency exchange costs and increased ease of trade between member countries', 'A guaranteed increase in a countrys population overnight', 'The elimination of all trade between member countries', 'A complete end to any form of international travel'], 0),
    ('What is one challenge that member countries of a currency union may face?', ['Individual countries lose the ability to set their own independent monetary policy', 'Member countries automatically gain unlimited monetary independence', 'Currency unions eliminate the need for any economic cooperation', 'Member countries are legally required to leave the union within one year'], 0),
    ('How does a currency union differ from simply having a fixed exchange rate between two currencies?', ['In a currency union, member countries actually share the same single currency rather than just maintaining a fixed conversion rate', 'A currency union and a fixed exchange rate are identical in every respect', 'A fixed exchange rate always requires countries to share a single currency', 'A currency union never involves any relationship between different countries'], 0)]),
]),
day(148, [
L('Vocabulary: Onomatopoeia and Sound Symbolism',
  'Grade 9 Language strand: onomatopoeia is a word that imitates or suggests the sound it describes, such as buzz or clang, and sound symbolism more broadly explores how certain sounds in language can evoke particular sensory impressions.',
  [('What is onomatopoeia?', ['A word that imitates or suggests the sound it describes', 'A word with no connection to any sound whatsoever', 'A punctuation mark used to end a question', 'A grammatical rule about verb tense'], 0),
   ('Which of the following is an example of onomatopoeia?', ['Buzz', 'Happy', 'Quickly', 'Blue'], 0),
   ('What is sound symbolism?', ['The idea that certain sounds in language can evoke particular sensory impressions or meanings', 'A rule stating that sounds have no connection to meaning at all', 'A term used only to describe silent reading', 'A type of formal citation format'], 0),
   ('Why might a poet use onomatopoeia in a poem?', ['To create a vivid sensory effect that helps a reader imagine a sound directly', 'To remove any sensory imagery from a poem entirely', 'Because onomatopoeia is required in every single sentence of formal writing', 'To avoid using any descriptive language at all'], 0),
   ('How does onomatopoeia differ from a typical descriptive adjective?', ['It imitates a sound directly rather than simply describing a quality', 'It never appears in written language of any kind', 'It always describes a colour rather than a sound', 'It has no relationship to sound or description whatsoever'], 0)]),
M('Calculus Preview: An Introduction to the Definite Integral',
  'Grade 9 Math strand: a definite integral represents the area under a curve between two boundaries, and it can be approximated using a Riemann sum, which adds up the areas of many thin rectangles and approaches the exact integral as the number of rectangles grows.',
  [('What does a definite integral generally represent geometrically?', ['The area under a curve between two specified boundaries', 'The slope of a single straight line', 'The exact location of a single point on a graph', 'The perimeter of a triangle drawn on a coordinate plane'], 0),
   ('What is a Riemann sum used for?', ['Approximating the area under a curve by summing the areas of many thin rectangles', 'Calculating the exact circumference of a circle', 'Finding the greatest common divisor of two integers', 'Measuring the angle between two intersecting lines'], 0),
   ('What happens to a Riemann sum approximation as the number of rectangles increases toward infinity?', ['The approximation approaches the exact value of the definite integral', 'The approximation becomes increasingly inaccurate with more rectangles', 'The approximation always equals zero regardless of the number of rectangles', 'The number of rectangles has no effect on the approximations accuracy'], 0),
   ('What two values define the boundaries of a definite integral?', ['The lower and upper limits of integration', 'The slope and the y-intercept of a line', 'The mean and the median of a data set', 'The radius and the diameter of a circle'], 0),
   ('Which earlier calculus preview concept is closely connected to defining the definite integral rigorously?', ['Limits', 'The Euclidean algorithm', 'The Pythagorean theorem', 'Sigma notation used only for finite sums'], 0)]),
Sc('Physics: Rotational Kinetic Energy and Angular Momentum',
   'Grade 9 Science strand: rotational kinetic energy is the energy an object possesses due to its rotational motion, and angular momentum, which depends on rotational inertia and angular velocity, remains conserved unless an external torque acts on the system.',
   [('What is rotational kinetic energy?', ['The energy an object possesses due to its rotational motion', 'The energy an object possesses only while it is completely at rest', 'A type of energy that applies only to objects moving in a straight line', 'The total mass of a rotating object'], 0),
    ('What is angular momentum?', ['A measure of an objects rotational motion, dependent on its rotational inertia and angular velocity', 'A measure of an objects temperature while spinning', 'A measure of the colour of a rotating object', 'A measure of the distance an object has travelled in a straight line'], 0),
    ('According to the conservation of angular momentum, what happens if a spinning objects rotational inertia decreases with no external torque?', ['Its angular velocity increases to keep angular momentum constant', 'Its angular velocity always decreases to zero immediately', 'Angular momentum disappears completely with no cause', 'The object stops spinning entirely with no explanation'], 0),
    ('Which everyday example illustrates conservation of angular momentum?', ['A figure skater spinning faster when pulling their arms inward', 'A ball resting motionless on a flat table', 'A book sitting closed on a shelf', 'A parked car with its engine turned off'], 0),
    ('What must be present to change an objects angular momentum?', ['An external torque', 'A change in the objects colour', 'A decrease in room temperature', 'The presence of a magnetic field with no torque involved'], 0)]),
SS('Social Studies: The Geography of Internet Governance and Digital Sovereignty',
   'Grade 9 Social Studies (Geography) strand: internet governance refers to the rules, institutions, and processes that shape how the global internet is managed, and digital sovereignty describes a countrys assertion of control over data, infrastructure, and online activity within its own borders.',
   [('What does internet governance refer to?', ['The rules, institutions, and processes that shape how the global internet is managed and operated', 'A single company that controls the entire global internet', 'A rule stating that the internet cannot be regulated in any way', 'An agreement that applies only to a single citys local network'], 0),
    ('What is digital sovereignty?', ['A countrys assertion of control over data, infrastructure, and online activity within its borders', 'A rule requiring every country to share all of its data publicly', 'A concept with no connection to national borders at all', 'A type of currency used only for online purchases'], 0),
    ('Why might a country pursue policies aimed at digital sovereignty?', ['To protect national security, privacy, or economic interests related to data and digital infrastructure', 'Because digital sovereignty has no effect on national security or privacy', 'To eliminate internet access within its own borders entirely', 'Because international law forbids any control over digital infrastructure'], 0),
    ('What is one example of a policy that reflects digital sovereignty?', ['A law requiring that citizens data be stored on servers located within the country', 'A law banning all citizens from using the internet permanently', 'A policy that has no connection to data storage at all', 'A rule that applies exclusively to postal mail delivery'], 0),
    ('Why can internet governance be considered a global geographic issue rather than a purely technical one?', ['Decisions about internet infrastructure and rules affect how people and economies connect across different countries and regions', 'Internet governance has no relationship to geography of any kind', 'The internet operates entirely independently of any physical infrastructure', 'Geography only applies to physical landforms, never to digital systems'], 0)]),
]),
day(149, [
L('Reading: Analyzing Anachronism in Literature',
  'Grade 9 Language strand: an anachronism is something placed in a time period where it does not chronologically belong, and an author may include one deliberately for artistic or comedic effect, or to comment on a modern issue through a historical lens.',
  [('What is an anachronism?', ['Something placed in a time period where it does not chronologically belong', 'A word that has only one possible meaning', 'A punctuation mark used exclusively in dialogue', 'A character who narrates an entire story'], 0),
   ('Why might an author deliberately include an anachronism in a story?', ['To create a specific artistic or comedic effect, or to comment on a modern issue through a historical lens', 'Because anachronisms are always accidental and never intentional', 'To make a story completely impossible for any reader to follow', 'Because every historical story is legally required to include one'], 0),
   ('An anachronism appearing in a historical film by accident, such as a modern object in an old setting, would generally be considered what?', ['A production error rather than an intentional device', 'A deliberate and celebrated artistic technique in every case', 'Evidence that the film is set in the present day', 'A type of literary device found only in poetry'], 0),
   ('Which is an example of an anachronism?', ['A wristwatch appearing in a story that is set in ancient Rome', 'A toga appearing in a story that is set in ancient Rome', 'A gladiator appearing in a story that is set in ancient Rome', 'A chariot appearing in a story that is set in ancient Rome'], 0),
   ('How can recognizing anachronisms help a reader analyze an authors intent?', ['It can reveal whether the author is intentionally blending time periods to make a thematic point', 'Recognizing anachronisms never provides any insight into an authors intent', 'Anachronisms only ever indicate a printing error with no deeper meaning', 'It proves that a story can never be set in the past'], 0)]),
M('Geometry: Converting Between Polar and Rectangular Coordinates',
  'Grade 9 Math strand: a point in polar coordinates can be converted to rectangular coordinates using x = r cos(theta) and y = r sin(theta), and rectangular coordinates can be converted back to polar form using r = sqrt(x^2 + y^2), since some curves and equations are simpler to express in one system than the other.',
  [('Which formula converts polar coordinates to rectangular x-coordinates?', ['x = r cos(theta)', 'x = r sin(theta)', 'x = r + theta', 'x = theta divided by r'], 0),
   ('Which formula converts polar coordinates to rectangular y-coordinates?', ['y = r sin(theta)', 'y = r cos(theta)', 'y = r minus theta', 'y = theta multiplied by two'], 0),
   ('How can the distance r be found from rectangular coordinates x and y?', ['r = sqrt(x^2 + y^2)', 'r = x + y', 'r = x multiplied by y', 'r = x minus y'], 0),
   ('Why might converting between polar and rectangular coordinates be useful?', ['Some equations or curves are far simpler to express in one coordinate system than the other', 'The two coordinate systems can never be converted between each other', 'Rectangular coordinates can only describe straight lines', 'Polar coordinates cannot be used to describe any curve'], 0),
   ('What does the angle theta represent in the conversion between the two coordinate systems?', ['The direction from the origin to the point, measured from the fixed reference axis', 'The exact distance from the origin to the point', 'The total area enclosed by a curve', 'The slope of a line drawn through the origin'], 0)]),
Sc('Earth Science: Rivers and Fluvial Landforms',
   'Grade 9 Science strand: fluvial geomorphology is the study of how rivers shape landforms through erosion and deposition, producing features such as winding meanders, flat floodplains, and deltas where sediment settles as a river slows upon entering a larger body of water.',
   [('What is fluvial geomorphology the study of?', ['How rivers shape landforms through erosion and deposition', 'How volcanoes form beneath the ocean floor', 'How glaciers move across a continent', 'How stars change over their lifetimes'], 0),
    ('What is a meander?', ['A winding curve or bend in a rivers course', 'A perfectly straight section of a river with no curves', 'A waterfall found only in mountainous regions', 'A type of dam built by human engineers'], 0),
    ('What is a floodplain?', ['The flat land bordering a river that is periodically covered by floodwater', 'A dry desert region with no connection to any river', 'A mountain peak located far from any river', 'A permanently frozen region near the poles'], 0),
    ('How does a river delta typically form?', ['Sediment carried by a river is deposited where the river slows upon entering a larger body of water', 'A delta forms only through volcanic eruptions', 'A delta forms when a river freezes completely solid', 'A delta forms without any connection to sediment or water flow'], 0),
    ('Why do rivers tend to erode more on the outside of a meander bend?', ['Water flows faster on the outside of the bend, increasing its erosive power', 'Water always flows slower on the outside of a bend', 'Erosion never occurs on the outside of a meander bend', 'The outside of a bend is always made of solid, unerodable rock'], 0)]),
SS('Social Studies: The Geography of Urban Twinning: Sister Cities and Municipal Diplomacy',
   'Grade 9 Social Studies (Geography) strand: a sister city relationship is a formal partnership between two municipalities in different countries, intended to foster cultural exchange and economic cooperation through a form of diplomacy conducted at the local, rather than national, government level.',
   [('What is a sister city relationship?', ['A formal partnership between two municipalities in different countries intended to foster cultural and economic ties', 'A rule requiring two cities in the same country to merge into one', 'An informal friendship between two individuals with no government involvement', 'A type of trade agreement that applies only to national governments'], 0),
    ('What is one common goal of city twinning agreements?', ['Encouraging cultural exchange and mutual understanding between residents of both cities', 'Eliminating all communication between the two partnered cities', 'Merging the governments of both cities into a single administration', 'Ending all trade and cooperation between the two cities'], 0),
    ('Besides cultural exchange, what other type of cooperation can sister city relationships support?', ['Economic cooperation, such as trade and business partnerships', 'Cooperation that is limited exclusively to sporting events', 'No other form of cooperation is ever possible between sister cities', 'Cooperation only related to weather forecasting'], 0),
    ('What term describes diplomacy conducted at the municipal or local government level, as seen in sister city relationships?', ['Municipal (or city) diplomacy', 'National military strategy', 'International currency exchange', 'Global environmental treaty negotiation'], 0),
    ('Why might two cities located in different countries choose to become sister cities?', ['They may share historical, cultural, or economic connections they wish to formally strengthen', 'Sister city relationships are always chosen entirely at random', 'They must be located in the exact same time zone with no exceptions', 'Two cities can only become sister cities if they share an identical population size'], 0)]),
]),
day(150, [
L('Language Review: Modifiers, Polysemy, In Medias Res, and Reported Speech',
  'Grade 9 Language strand review: students revisit dangling and misplaced modifiers, polysemy, in medias res, reported speech, and anachronism from Days 141-149.',
  [('What is a dangling modifier?', ['A modifier that does not clearly and logically attach to any word in the sentence', 'A word that has no meaning at all', 'A punctuation mark that separates two clauses', 'A verb that has no subject'], 0),
   ('What is polysemy?', ['When a single word has two or more related meanings', 'When a word has absolutely no meaning at all', 'When two unrelated words happen to be spelled identically', 'When a sentence contains no verbs whatsoever'], 0),
   ('What does in medias res mean?', ['Beginning a narrative in the middle of the action rather than at the start of events', 'Ending a narrative before any action has occurred', 'Telling a story entirely through dialogue with no narration', 'Skipping the ending of a story entirely'], 0),
   ('What is reported (indirect) speech?', ['Relaying what someone said without quoting their exact words directly', 'Quoting a speaker word for word using quotation marks', 'A type of punctuation used only in poetry', 'A grammatical rule that applies only to questions'], 0),
   ('What is an anachronism?', ['Something placed in a time period where it does not chronologically belong', 'A word that has only one possible meaning', 'A punctuation mark used exclusively in dialogue', 'A character who narrates an entire story'], 0)]),
M('Math Review: Exponential Equations, Cross Products, Markov Chains, and Series',
  'Grade 9 Math strand review: students revisit solving exponential equations, the cross product of vectors, Markov chains, infinite geometric series, and the definite integral from Days 141-149.',
  [('What defines an exponential equation?', ['An equation in which the variable appears in the exponent', 'An equation with no exponents of any kind', 'An equation that only involves whole number coefficients', 'An equation that cannot be graphed'], 0),
   ('What kind of quantity results from taking the cross product of two vectors?', ['A new vector that is perpendicular to both original vectors', 'A single number with no direction at all', 'A colour representing the vectors', 'An angle measured in degrees only'], 0),
   ('What is a defining feature of a Markov chain?', ['The probability of moving to the next state depends only on the current state, not on earlier history', 'Every future state depends equally on all previous states combined', 'A Markov chain can only ever have a single possible state', 'The probabilities in a Markov chain are always identical for every state'], 0),
   ('Under what condition does an infinite geometric series converge to a finite sum?', ['When the absolute value of the common ratio is less than one', 'When the common ratio is exactly equal to ten', 'When every term in the series is negative', 'When the first term of the series equals zero'], 0),
   ('What does a definite integral generally represent geometrically?', ['The area under a curve between two specified boundaries', 'The slope of a single straight line', 'The exact location of a single point on a graph', 'The perimeter of a triangle drawn on a coordinate plane'], 0)]),
Sc('Science Review: Titration, Fluid Pressure, Glaciers, and Animal Behaviour',
   'Grade 9 Science strand review: students revisit acid-base titration, fluid pressure and Pascals Principle, glaciers and glacial landforms, animal behaviour, and rivers and fluvial landforms from Days 141-149.',
   [('What is the goal of an acid-base titration?', ['To determine the unknown concentration of an acid or base solution', 'To permanently change the colour of a solution with no other purpose', 'To measure the temperature of a chemical reaction only', 'To separate a mixture into its individual elements'], 0),
    ('What does Pascals Principle state?', ['Pressure applied to an enclosed fluid is transmitted equally in all directions throughout the fluid', 'Pressure applied to a fluid disappears instantly with no effect', 'Fluids can never transmit pressure of any kind', 'Pressure in a fluid only travels in a single fixed direction'], 0),
    ('How does a glacier form?', ['Snow accumulates and compacts over time into dense ice that begins to flow under its own weight', 'Ice forms instantly with no gradual accumulation of snow at all', 'A glacier forms only from ocean water freezing directly', 'A glacier forms exclusively through volcanic activity'], 0),
    ('What is an instinctive behaviour?', ['A behaviour that is innate and genetically programmed, requiring no prior learning', 'A behaviour that can only be acquired through years of formal training', 'A behaviour that never appears in any animal species', 'A behaviour that changes completely every single day'], 0),
    ('What is fluvial geomorphology the study of?', ['How rivers shape landforms through erosion and deposition', 'How volcanoes form beneath the ocean floor', 'How glaciers move across a continent', 'How stars change over their lifetimes'], 0)]),
SS('Social Studies Review: Landlocked Nations, Geothermal Energy, Maritime Law, and Peacekeeping',
   'Grade 9 Social Studies (Geography) strand review: students revisit landlocked countries and transit corridors, geothermal energy, continental shelves and maritime boundaries, UN peacekeeping and buffer zones, and sister cities from Days 141-149.',
   [('What defines a landlocked country?', ['A country that has no direct access to an ocean coastline', 'A country located entirely on an island', 'A country with the longest coastline in the world', 'A country that has banned all forms of international trade'], 0),
    ('What is geothermal energy?', ['Energy harnessed from heat stored beneath the Earths surface', 'Energy generated exclusively from burning coal', 'Energy captured only from moving ocean waves', 'Energy created by reflecting sunlight off mirrors'], 0),
    ('What is a continental shelf?', ['The shallow, gently sloping seabed that extends outward from a coastline before dropping to the deep ocean floor', 'A mountain range located entirely inland with no connection to the coast', 'A type of river delta found only in tropical regions', 'A structure built entirely by human engineers to store water'], 0),
    ('What is the general purpose of a United Nations peacekeeping mission?', ['To help maintain peace and stability in a region affected by conflict', 'To permanently occupy a country and replace its government', 'To eliminate the need for any international cooperation', 'To ensure that conflicts never end anywhere in the world'], 0),
    ('What is a sister city relationship?', ['A formal partnership between two municipalities in different countries intended to foster cultural and economic ties', 'A rule requiring two cities in the same country to merge into one', 'An informal friendship between two individuals with no government involvement', 'A type of trade agreement that applies only to national governments'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_141_150)
    append_to(9, g9_141_150)
