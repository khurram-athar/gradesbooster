#!/usr/bin/env python3
"""Grade 10, Days 121-130 -- extends Grade 10 from 120 to 130 days. Topics
chosen after grepping the existing Day 1-120 title list (data/grade10.json)
extensively to avoid any overlap: gerunds/infinitives/verbals, stream-of-
consciousness narration, the eulogy and commemorative writing, postmodern
fiction and metafiction, algorithmic bias and filter bubbles, pathetic
fallacy and personification, the investigative report, appositives and
nonrestrictive clauses, and the trickster figure in folklore; the product
and quotient rules for derivatives, the Euclidean Algorithm, hypothesis
testing, partial fraction decomposition, non-Euclidean geometry,
mathematical induction, scalar/vector projections, Bayes Theorem, and
roots of unity; the integumentary system, buffers and pH regulation,
glaciers and ice ages, semiconductors, coral reefs, fossil formation and
the geologic time scale, animal behaviour (instinct vs learning), the
Maillard reaction, and camouflage/mimicry; the 1919 Paris Peace Conference,
the King-Byng Affair of 1926, the Manitoba Act of 1870, the Canadian
Pacific Railway, the Rowell-Sirois Commission, the Manitoba Schools
Question, British Columbia joining Confederation, Prince Edward Island
joining Confederation, and the Halibut Treaty of 1923.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used anywhere
in title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-120 convention.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


def _rebalance_answer_positions(days, seed=20260730):
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


g10_121_130 = [
day(121, [
E('Grammar: Gerunds, Infinitives, and Verbals',
  'Grade 10 English strand: a gerund is a verb form ending in -ing that functions as a noun, an infinitive is the base form of a verb usually preceded by to, and both are verbals that let writers embed actions within noun phrases without a full clause.',
  [('What is a gerund?', ['A verb form ending in -ing that functions as a noun', 'A verb that shows past tense only', 'A word that replaces a pronoun', 'A type of conjunction'], 0),
   ('What is an infinitive?', ['The base form of a verb, usually preceded by to', 'A verb conjugated for third person singular', 'A noun with no verb qualities', 'A punctuation mark used in dialogue'], 0),
   ('In the sentence Swimming is her favourite hobby, what role does Swimming play?', ['It functions as the subject noun of the sentence', 'It functions as a verb showing present action', 'It functions as an adjective describing hobby', 'It functions as a preposition'], 0),
   ('Which sentence correctly uses an infinitive phrase?', ['She hopes to travel across Europe next summer.', 'She hopes traveling across Europe next summer.', 'She hopes travels across Europe next summer.', 'She hopes traveled across Europe next summer.'], 0),
   ('Verbals such as gerunds and infinitives are useful because they ___.', ['Allow writers to embed actions within noun or modifying phrases without a full clause', 'Always require a separate subject and predicate', 'Cannot appear at the beginning of a sentence', 'Function only as conjunctions'], 0)]),
M('Calculus Foundations: The Product and Quotient Rules for Derivatives',
  'Grade 10 Math strand: the product rule and quotient rule provide methods for differentiating a function formed by multiplying or dividing two other functions, extending the basic derivative rules introduced with limits and the power rule.',
  [('What does the product rule allow you to differentiate?', ['A function formed by multiplying two other functions together', 'Only a single constant term', 'A function formed by adding two constants', 'Only trigonometric ratios with no functions involved'], 0),
   ('What does the quotient rule allow you to differentiate?', ['A function formed by dividing one function by another', 'A function with no variables at all', 'Only whole numbers with no functions', 'A function multiplied by a constant only'], 0),
   ('The product and quotient rules build directly on which earlier calculus concept?', ['The basic derivative and the power rule', 'Only basic arithmetic with no calculus involved', 'The Pythagorean Theorem', 'The quadratic formula'], 0),
   ('Why are the product and quotient rules necessary in calculus?', ['Many functions cannot be differentiated using the power rule alone', 'They eliminate the need for the power rule entirely', 'They only apply to functions with no variables', 'They replace the need to ever find a derivative'], 0),
   ('Using differentiation rules like the product and quotient rules helps mathematicians analyze ___.', ['How more complex combined functions change and behave', 'Only the colour of a graph', 'Only whole number arithmetic', 'Only basic geometry with no functions'], 0)]),
Sc('The Human Skin: Structure and the Integumentary System',
   'Grade 10 Science strand: the skin is the largest organ of the human body and the primary component of the integumentary system, providing protection against pathogens and injury, regulating body temperature, and enabling sensation through specialized receptors.',
   [('What is the skin considered in relation to the human body?', ['The largest organ of the body', 'The smallest organ of the body', 'An organ found only in mammals with fur', 'A structure unrelated to any body system'], 0),
    ('What body system does the skin primarily belong to?', ['The integumentary system', 'The digestive system', 'The respiratory system', 'The skeletal system'], 0),
    ('What is one major function of the skin?', ['Protecting the body against pathogens and injury', 'Pumping blood throughout the body', 'Producing digestive enzymes', 'Filtering air before it enters the lungs'], 0),
    ('How does the skin help regulate body temperature?', ['Through processes like sweating and adjusting blood flow near the surface', 'By producing bile to break down fats', 'By storing large amounts of oxygen', 'By absorbing all incoming sunlight'], 0),
    ('What allows the skin to detect touch, pressure, and temperature?', ['Specialized sensory receptors', 'Digestive enzymes', 'Red blood cells only', 'Bone marrow'], 0)]),
H('The 1919 Paris Peace Conference and Canadas Independent Signature',
  'Grade 10 History strand: at the 1919 Paris Peace Conference following World War I, Canada signed the Treaty of Versailles as a separate signatory alongside Britain, an early assertion of Canadian autonomy in international affairs that built on the nations wartime contributions.',
  [('What major agreement was signed at the Paris Peace Conference in 1919?', ['The Treaty of Versailles', 'The Treaty of Ghent', 'The Statute of Westminster', 'The Balfour Declaration'], 0),
   ('How did Canada participate in signing the Treaty of Versailles?', ['As a separate signatory alongside Britain', 'Canada refused to participate in any way', 'Canada signed only as part of the United States delegation', 'Canada was excluded entirely from the conference'], 0),
   ('Why is Canadas separate signature considered historically significant?', ['It was an early assertion of Canadian autonomy in international affairs', 'It marked the end of all Canadian involvement in world affairs', 'It had no connection to Canadian independence', 'It occurred before Canada existed as a country'], 0),
   ('What Canadian contribution during World War I helped support this growing recognition?', ['Canadas significant military contributions and casualties during the war', 'Canadas complete absence from the war effort', 'A purely economic contribution with no military role', 'A contribution limited to naval forces only'], 0),
   ('The 1919 Paris Peace Conference is often studied alongside which other early 20th-century milestone in Canadian autonomy?', ['The Chanak Affair and the Statute of Westminster', 'The Confederation of 1867', 'The War of 1812', 'The Rebellions of 1837-38'], 0)]),
]),
day(122, [
E('Reading: Analyzing Stream-of-Consciousness Narration',
  'Grade 10 English strand: stream-of-consciousness narration attempts to capture the continuous, often unstructured flow of a characters thoughts and sensory impressions, immersing readers directly in a characters inner experience rather than presenting events through conventional plot structure.',
  [('What does stream-of-consciousness narration attempt to capture?', ['The continuous, often unstructured flow of a characters thoughts and impressions', 'A strictly chronological sequence of external events', 'Only dialogue spoken between characters', 'A formal summary of the plot'], 0),
   ('How does stream-of-consciousness narration typically differ from conventional narration?', ['It immerses readers directly in a characters inner experience rather than following a clear plot structure', 'It always follows strict chronological order with no digressions', 'It relies only on third-person objective description', 'It avoids depicting a characters thoughts entirely'], 0),
   ('Which of the following is a common feature of stream-of-consciousness writing?', ['Fragmented syntax and shifting, associative thoughts', 'Strict formal outlines with numbered sections', 'Only short, simple declarative sentences', 'Complete absence of any character perspective'], 0),
   ('Why might an author choose a stream-of-consciousness technique?', ['To reveal the complexity and immediacy of a characters mental and emotional life', 'To make the plot easier to summarize', 'To eliminate the need for any characters', 'To simplify the reading experience'], 0),
   ('Stream-of-consciousness narration is most closely associated with which literary movement?', ['Modernism', 'Medieval romance', 'Victorian melodrama', 'Classical epic poetry'], 0)]),
M('Number Theory: The Euclidean Algorithm and Greatest Common Divisor',
  'Grade 10 Math strand: the Euclidean Algorithm is an efficient method for finding the greatest common divisor of two integers by repeatedly applying the division algorithm, a technique with roots in ancient mathematics still used today in modern computing.',
  [('What does the Euclidean Algorithm calculate?', ['The greatest common divisor of two integers', 'The least common multiple of two fractions only', 'The square root of a number', 'The area of a rectangle'], 0),
   ('How does the Euclidean Algorithm work?', ['By repeatedly applying the division algorithm until a remainder of zero is reached', 'By listing every factor of both numbers individually', 'By multiplying the two numbers together', 'By guessing and checking randomly'], 0),
   ('What does GCD stand for?', ['Greatest common divisor', 'General coefficient distribution', 'Global calculation determinant', 'Grouped common denominator'], 0),
   ('Why is the Euclidean Algorithm considered efficient?', ['It finds the greatest common divisor without listing all possible factors', 'It requires listing every integer up to the two numbers', 'It only works for numbers less than 10', 'It cannot be applied to large numbers at all'], 0),
   ('The Euclidean Algorithm has practical applications in which modern field?', ['Computer science and cryptography', 'Only ancient astronomy with no modern use', 'Only basic arithmetic with no further application', 'Only art and design'], 0)]),
Sc('Chemistry: Buffers and pH Regulation in Biological Systems',
   'Grade 10 Science strand: a buffer is a solution that resists changes in pH when small amounts of acid or base are added, a property essential for maintaining stable conditions in biological systems such as human blood, which must remain within a narrow pH range to function properly.',
   [('What is a buffer solution?', ['A solution that resists changes in pH when acid or base is added', 'A solution that always becomes strongly acidic', 'A solution with no chemical properties', 'A pure solvent with no solute'], 0),
    ('Why are buffers important in biological systems?', ['They help maintain a stable pH necessary for proper cellular function', 'They eliminate the need for water in the body', 'They have no biological role whatsoever', 'They always raise the pH to 14'], 0),
    ('Human blood must remain within a narrow range of what property?', ['pH', 'Colour', 'Temperature only, with no relation to pH', 'Volume, unrelated to chemistry'], 0),
    ('What happens if a small amount of acid is added to an effective buffer solution?', ['The buffer resists a significant change in pH', 'The pH changes drastically and immediately', 'The solution instantly becomes a solid', 'The buffer stops functioning permanently'], 0),
    ('A buffer is typically made from ___.', ['A weak acid and its conjugate base, or a weak base and its conjugate acid', 'Only pure distilled water', 'Only a strong acid with nothing else', 'Only table salt dissolved in oil'], 0)]),
H('The King-Byng Affair of 1926 and the Constitutional Crisis',
  'Grade 10 History strand: the King-Byng Affair was a 1926 constitutional crisis in which Governor General Lord Byng refused Prime Minister Mackenzie Kings request to dissolve Parliament, raising lasting questions about the proper limits of the Governor Generals discretionary power in Canadian government.',
  [('Who were the two main figures involved in the King-Byng Affair?', ['Prime Minister Mackenzie King and Governor General Lord Byng', 'Prime Minister John A. Macdonald and Queen Victoria', 'Prime Minister Lester Pearson and a provincial premier', 'Prime Minister Pierre Trudeau and a foreign ambassador'], 0),
   ('What did Governor General Byng refuse to do in 1926?', ['Dissolve Parliament at Prime Minister Kings request', 'Sign the Treaty of Versailles', 'Approve the Balfour Declaration', 'Call a referendum on Confederation'], 0),
   ('What broader constitutional question did the King-Byng Affair raise?', ['The proper limits of the Governor Generals discretionary power', 'Whether Canada should adopt a new flag', 'Whether Quebec should separate from Canada', 'Whether Newfoundland should join Confederation'], 0),
   ('In what year did the King-Byng Affair occur?', ['1926', '1867', '1949', '1982'], 0),
   ('The King-Byng Affair is often discussed alongside which other 1926 milestone in Canadian constitutional history?', ['The Balfour Declaration', 'The Nisgaa Treaty', 'The Naval Service Act', 'The St. Lawrence Seaway'], 0)]),
]),
day(123, [
E('Writing: The Eulogy and Commemorative Writing',
  'Grade 10 English strand: a eulogy is a speech or piece of writing that honours and remembers a person, typically highlighting their character, achievements, and impact on others, and commemorative writing more broadly uses a respectful, reflective tone to mark significant people or events.',
  [('What is the primary purpose of a eulogy?', ['To honour and remember a person by highlighting their character and impact', 'To criticize a persons flaws in detail', 'To provide a strictly factual biography with no reflection', 'To entertain an audience with unrelated humour only'], 0),
   ('What tone does commemorative writing typically use?', ['A respectful and reflective tone', 'A sarcastic and dismissive tone', 'An angry and confrontational tone', 'A purely technical and clinical tone'], 0),
   ('Which detail would most likely appear in a well-written eulogy?', ['A specific memory that illustrates the persons kindness or character', 'An unrelated list of statistics', 'A detailed critique of the persons career failures', 'A summary of unrelated current events'], 0),
   ('Why do eulogies often include anecdotes?', ['Anecdotes bring a persons character to life for the audience', 'Anecdotes are required by law in formal speeches', 'Anecdotes replace the need for any structure', 'Anecdotes are only used in fictional writing'], 0),
   ('Commemorative writing can also be used to mark ___.', ['Significant historical events or achievements, not just individuals', 'Only birthdays with no other occasions', 'Only failures and setbacks', 'Nothing beyond a single specific person'], 0)]),
M('Statistics: An Introduction to Hypothesis Testing',
  'Grade 10 Math strand: hypothesis testing is a statistical method for evaluating whether observed data provides enough evidence to reject a null hypothesis, a default assumption of no effect or no difference, in favour of an alternative hypothesis.',
  [('What is a null hypothesis?', ['A default assumption of no effect or no difference', 'A hypothesis that is always proven true', 'A hypothesis with no possible outcome', 'A statement with no statistical meaning'], 0),
   ('What does hypothesis testing evaluate?', ['Whether observed data provides enough evidence to reject the null hypothesis', 'Whether a graph is drawn correctly', 'Whether a number is even or odd', 'Whether an equation has a solution'], 0),
   ('What is the alternative hypothesis?', ['The hypothesis proposing that an effect or difference does exist', 'A hypothesis identical to the null hypothesis in every case', 'A hypothesis with no relationship to the null hypothesis', 'A hypothesis used only in geometry'], 0),
   ('Why is hypothesis testing important in statistics?', ['It provides a structured method for making inferences from sample data', 'It guarantees results with complete certainty every time', 'It eliminates the need for any data collection', 'It only applies to whole numbers'], 0),
   ('A low p-value in hypothesis testing typically suggests ___.', ['Stronger evidence against the null hypothesis', 'That the null hypothesis is definitely true', 'That no data was collected', 'That the experiment must be repeated exactly'], 0)]),
Sc('Earth Science: Glaciers and Ice Ages',
   'Grade 10 Science strand: glaciers are large, slow-moving masses of ice formed by the accumulation and compaction of snow over long periods, and ice ages are extended periods of global cooling during which glaciers expand significantly, reshaping landscapes through erosion and deposition.',
   [('How do glaciers form?', ['Through the accumulation and compaction of snow over long periods', 'Through volcanic eruptions releasing ash', 'Through rapid evaporation of ocean water', 'Through sudden flooding events'], 0),
    ('What is an ice age?', ['An extended period of global cooling during which glaciers expand significantly', 'A brief period of extreme heat with no ice', 'A single day of unusually cold weather', 'A period when all ice on Earth melts completely'], 0),
    ('How do glaciers reshape landscapes?', ['Through processes of erosion and deposition as they move', 'Glaciers have no effect on landscapes', 'Only through volcanic activity', 'Only by melting instantly with no movement'], 0),
    ('What landform is commonly created by glacial deposition?', ['A moraine, a ridge of accumulated debris', 'A volcano formed from lava', 'A coral reef formed underwater', 'A sand dune formed only by wind'], 0),
    ('Glaciers are classified as which type of natural feature due to their movement?', ['Slow-moving masses of ice', 'Stationary rock formations with no movement', 'Fast-flowing liquid water bodies', 'Gas clouds in the atmosphere'], 0)]),
H('The Manitoba Act of 1870 and the Creation of Manitoba',
  'Grade 10 History strand: the Manitoba Act of 1870 created Canadas fifth province following the Red River Resistance led by Louis Riel, establishing provisions for bilingual government services and land grants for the Metis population of the Red River Settlement.',
  [('What did the Manitoba Act of 1870 create?', ['The province of Manitoba', 'The province of Saskatchewan', 'The province of Alberta', 'The Northwest Territories'], 0),
   ('What event preceded and influenced the Manitoba Act?', ['The Red River Resistance led by Louis Riel', 'The Klondike Gold Rush', 'The Battle of Vimy Ridge', 'The Halifax Explosion'], 0),
   ('What number province did Manitoba become?', ['The fifth province', 'The first province', 'The tenth province', 'The second province'], 0),
   ('What did the Manitoba Act include provisions for?', ['Bilingual government services and land grants for the Metis population', 'The complete removal of French language rights', 'The abolition of all provincial governments', 'An immediate declaration of independence from Canada'], 0),
   ('In what year was the Manitoba Act passed?', ['1870', '1867', '1905', '1949'], 0)]),
]),
day(124, [
E('Literature: Postmodern Fiction and Metafiction',
  'Grade 10 English strand: postmodern fiction often questions the reliability of narrative, blends genres, and uses metafiction, storytelling that draws attention to its own fictional nature, to challenge readers assumptions about truth, authorship, and the boundaries of a text.',
  [('What is metafiction?', ['Storytelling that draws attention to its own fictional nature', 'A story with no narrator or characters', 'A purely factual, non-fictional report', 'A subgenre of poetry only'], 0),
   ('What does postmodern fiction often question?', ['The reliability of narrative and traditional assumptions about truth', 'The existence of grammar rules only', 'The use of punctuation in dialogue', 'The length of chapters in a novel'], 0),
   ('Which technique might a metafictional novel use?', ['A narrator who directly addresses the reader and comments on the act of writing', 'A narrator who never acknowledges the reader exists', 'A strictly chronological, unbroken plot with no commentary', 'A complete absence of any narrator'], 0),
   ('Postmodern fiction often blends ___.', ['Multiple genres and styles within a single text', 'Only one genre with no variation ever', 'Only nonfiction reporting techniques', 'Only classical poetic forms'], 0),
   ('Why might an author use metafictional techniques?', ['To challenge readers assumptions about authorship and the boundaries of a text', 'To make the plot entirely predictable', 'To remove any thematic depth', 'To avoid any interaction with the reader'], 0)]),
M('Algebra: Partial Fraction Decomposition',
  'Grade 10 Math strand: partial fraction decomposition rewrites a complex rational expression as a sum of simpler fractions with lower-degree denominators, a technique useful for simplifying expressions and preparing them for further operations like integration.',
  [('What does partial fraction decomposition do?', ['Rewrites a complex rational expression as a sum of simpler fractions', 'Combines several fractions into one complicated fraction', 'Converts a fraction into a whole number only', 'Removes all variables from an expression'], 0),
   ('What kind of denominators do the resulting simpler fractions have?', ['Lower-degree denominators than the original expression', 'Denominators of infinitely high degree', 'No denominators at all', 'Denominators equal to zero'], 0),
   ('Partial fraction decomposition is especially useful in preparing expressions for ___.', ['Further operations such as integration', 'Simple counting with no further use', 'Only basic addition of whole numbers', 'Removing all fractions from mathematics permanently'], 0),
   ('What must be true about a rational expressions degree before typical partial fraction decomposition is applied?', ['The numerators degree should be less than the denominators degree', 'The numerator must always equal zero', 'The denominator must always be a single variable', 'The expression must have no numerator'], 0),
   ('Why might a mathematician decompose a complex fraction into partial fractions?', ['To make the expression easier to analyze, simplify, or integrate', 'To make the expression permanently unsolvable', 'To eliminate all mathematical meaning from the expression', 'To convert the expression into a whole number only'], 0)]),
Sc('Physics: Semiconductors and the Basics of Electronics',
   'Grade 10 Science strand: a semiconductor is a material with electrical conductivity between that of a conductor and an insulator, and its properties, which can be precisely controlled through doping, form the foundation of modern electronic devices like diodes and transistors.',
   [('What is a semiconductor?', ['A material with electrical conductivity between a conductor and an insulator', 'A material that always conducts electricity perfectly', 'A material that never conducts electricity at all', 'A material used only for insulation'], 0),
    ('What process is used to control a semiconductors properties?', ['Doping, or adding small amounts of other elements', 'Freezing the material to absolute zero', 'Melting the material completely', 'Removing all electrons from the material'], 0),
    ('Which of the following is a common example of a semiconductor material?', ['Silicon', 'Copper', 'Rubber', 'Pure distilled water'], 0),
    ('What basic electronic component is commonly made from semiconductors?', ['A transistor', 'A wooden beam', 'A glass window', 'A rubber band'], 0),
    ('Why are semiconductors important to modern technology?', ['They form the foundation of electronic devices used in computers and countless other technologies', 'They have no practical application in technology', 'They are only used in ancient tools', 'They prevent all electrical devices from functioning'], 0)]),
H('The Canadian Pacific Railway and National Unity',
  'Grade 10 History strand: completed in 1885, the Canadian Pacific Railway fulfilled a promise made to British Columbia upon joining Confederation, linking the country from coast to coast and playing a central role in national unity, western settlement, and economic development.',
  [('What promise did the Canadian Pacific Railway fulfill?', ['A promise made to British Columbia upon joining Confederation', 'A promise made to Newfoundland in 1949', 'A promise made during the War of 1812', 'A promise made to Quebec after the 1867 Confederation'], 0),
   ('In what year was the Canadian Pacific Railway completed?', ['1885', '1867', '1905', '1949'], 0),
   ('What role did the railway play in Canadian development?', ['It linked the country from coast to coast and supported western settlement', 'It had no effect on national development', 'It disconnected eastern and western Canada', 'It was used only for local city transportation'], 0),
   ('The construction of the Canadian Pacific Railway is often linked to which controversial labour practice?', ['The use of underpaid Chinese labourers under dangerous conditions', 'The exclusive use of volunteer labour with no pay disputes', 'A complete ban on all immigrant labour', 'The use of only unionized labour with full benefits'], 0),
   ('Why is the Canadian Pacific Railway considered significant to national unity?', ['It physically and economically connected the provinces of a vast country', 'It separated the provinces into isolated regions', 'It had no connection to economic development', 'It only served military purposes'], 0)]),
]),
day(125, [
E('Media Literacy: Algorithmic Bias and Filter Bubbles',
  'Grade 10 English strand: recommendation algorithms on social media and search platforms personalize content based on past behaviour, which can create filter bubbles that reinforce existing beliefs and limit exposure to diverse perspectives, an important concern in media literacy.',
  [('What is a filter bubble?', ['A state in which personalized algorithms limit exposure to diverse perspectives', 'A physical device used to filter internet traffic', 'A type of formal essay structure', 'A method of fact-checking news articles'], 0),
   ('How do recommendation algorithms typically personalize content?', ['By analyzing a users past behaviour and preferences', 'By randomly selecting content with no pattern', 'By showing every user identical content', 'By ignoring user activity entirely'], 0),
   ('Why are filter bubbles a concern in media literacy?', ['They can reinforce existing beliefs and reduce exposure to differing viewpoints', 'They guarantee complete objectivity in all content', 'They have no effect on how people understand issues', 'They eliminate the need for critical thinking entirely'], 0),
   ('What term describes systematic unfairness in how an algorithm ranks or recommends content?', ['Algorithmic bias', 'Algorithmic neutrality', 'Algorithmic transparency', 'Algorithmic redundancy'], 0),
   ('What is one strategy for countering the effects of filter bubbles?', ['Deliberately seeking out sources with differing perspectives', 'Only using a single platform for all information', 'Avoiding all forms of media entirely', 'Sharing content without reading it first'], 0)]),
M('Geometry: An Introduction to Non-Euclidean Geometry',
  'Grade 10 Math strand: non-Euclidean geometry explores geometric systems that reject Euclids parallel postulate, including spherical and hyperbolic geometry, revealing that the familiar rules of flat-plane geometry are not the only consistent geometric framework.',
  [('What does non-Euclidean geometry reject?', ['Euclids parallel postulate', 'The concept of a triangle entirely', 'All numerical measurement', 'The existence of angles'], 0),
   ('What are two major types of non-Euclidean geometry?', ['Spherical and hyperbolic geometry', 'Linear and quadratic geometry', 'Positive and negative geometry', 'Rational and irrational geometry'], 0),
   ('In spherical geometry, what happens to the sum of a triangles interior angles?', ['It is greater than 180 degrees', 'It always equals exactly 180 degrees', 'It is always less than 90 degrees', 'It equals zero degrees'], 0),
   ('Why is non-Euclidean geometry significant in mathematics?', ['It shows that flat-plane geometry is not the only consistent geometric system', 'It proves that all geometry is invalid', 'It has no real mathematical applications', 'It disproves the existence of shapes entirely'], 0),
   ('Non-Euclidean geometry has important applications in which modern scientific field?', ['General relativity and the study of curved spacetime', 'Basic arithmetic only', 'Elementary counting techniques', 'Simple linear equations only'], 0)]),
Sc('Biology: Coral Reefs and Marine Ecosystems',
   'Grade 10 Science strand: coral reefs are diverse marine ecosystems built by colonies of tiny animals called coral polyps, which form calcium carbonate skeletons that provide habitat for a vast range of marine species, though reefs remain highly sensitive to changes in ocean temperature and acidity.',
   [('What are coral reefs built by?', ['Colonies of tiny animals called coral polyps', 'Large solitary fish', 'Deposits of volcanic ash', 'Deep-sea plant colonies'], 0),
    ('What do coral polyps produce that forms the structure of a reef?', ['Calcium carbonate skeletons', 'Pure oxygen gas only', 'Large deposits of sand with no structure', 'Layers of ice'], 0),
    ('Why are coral reefs ecologically important?', ['They provide habitat for a vast range of marine species', 'They have no effect on marine biodiversity', 'They only support a single species of fish', 'They exist only in freshwater lakes'], 0),
    ('What environmental change can cause coral bleaching?', ['Rising ocean temperatures', 'A decrease in ocean salinity to zero', 'An increase in the number of coral polyps', 'A drop in atmospheric pressure only'], 0),
    ('In addition to temperature, what other ocean condition threatens coral reef health?', ['Increasing ocean acidity', 'Increasing oxygen levels only', 'Decreasing sunlight in deep trenches only', 'Increasing freshwater rainfall only'], 0)]),
H('The Rowell-Sirois Commission and Canadian Federalism',
  'Grade 10 History strand: established in the late 1930s during the Great Depression, the Rowell-Sirois Commission examined the financial relationship between the federal and provincial governments, recommending reforms that reshaped Canadian federalism and expanded the federal governments role in social welfare.',
  [('When was the Rowell-Sirois Commission established?', ['In the late 1930s, during the Great Depression', 'In the early 1800s', 'Immediately after Confederation in 1867', 'After World War II in the 1950s'], 0),
   ('What relationship did the Rowell-Sirois Commission examine?', ['The financial relationship between federal and provincial governments', 'The relationship between Canada and Britain only', 'The relationship between Canada and the United Nations', 'The relationship between two rival political parties'], 0),
   ('What broader system did the commissions recommendations help reshape?', ['Canadian federalism', 'The Canadian electoral map only', 'The structure of the British monarchy', 'International trade agreements with Europe'], 0),
   ('What government role expanded as a result of related reforms?', ['The federal governments role in social welfare', 'The provincial governments role in foreign policy', 'The municipal governments role in defence', 'The judicial branchs role in taxation only'], 0),
   ('The Rowell-Sirois Commission was formed in response to economic difficulties caused by ___.', ['The Great Depression', 'The Klondike Gold Rush', 'World War I', 'The 1918-1920 Spanish Flu Pandemic'], 0)]),
]),
day(126, [
E('Reading: Analyzing Pathetic Fallacy and Personification',
  'Grade 10 English strand: pathetic fallacy attributes human emotions to nature or the weather to mirror a characters mood, while personification more broadly gives human qualities to any nonhuman thing, and both devices deepen atmosphere and symbolic meaning in a text.',
  [('What is pathetic fallacy?', ['Attributing human emotions to nature or weather to reflect a characters mood', 'A logical error in an argument', 'A type of grammatical mistake', 'A method of citing sources'], 0),
   ('What is personification?', ['Giving human qualities to a nonhuman thing', 'Comparing two unlike things using like or as', 'Repeating a consonant sound for effect', 'Exaggerating a statement for emphasis'], 0),
   ('Which sentence is an example of pathetic fallacy?', ['The angry storm clouds gathered as the heros despair deepened.', 'The storm produced 50 millimetres of rainfall in one hour.', 'The character felt sad after losing the competition.', 'The weather forecast predicted rain for Tuesday.'], 0),
   ('Why might an author use pathetic fallacy?', ['To mirror and intensify a characters emotional state through the natural environment', 'To provide purely scientific weather data', 'To avoid describing any setting', 'To remove emotional tone from a scene'], 0),
   ('How does personification typically deepen a text?', ['By creating vivid imagery and symbolic meaning through humanlike nonhuman elements', 'By making a text purely literal with no symbolism', 'By eliminating the need for description', 'By replacing all characters with objects'], 0)]),
M('Discrete Math: The Principle of Mathematical Induction',
  'Grade 10 Math strand: mathematical induction is a proof technique used to establish that a statement holds true for every natural number by proving a base case and then showing that if the statement holds for one case, it must hold for the next.',
  [('What does the principle of mathematical induction prove?', ['That a statement holds true for every natural number', 'That a statement is true for only one specific number', 'That an equation has no solution', 'That a shape has a certain area'], 0),
   ('What are the two main steps in a proof by induction?', ['Proving a base case and proving the inductive step', 'Guessing the answer and checking with a calculator', 'Drawing a graph and measuring it', 'Listing every natural number individually'], 0),
   ('What is the inductive step in a proof by induction?', ['Showing that if the statement holds for one case, it must hold for the next', 'Proving the statement is false for every case', 'Proving the statement only for the number one', 'Skipping directly to the conclusion with no justification'], 0),
   ('Why is proving only the base case not sufficient for induction?', ['The statement must also be shown to hold for all subsequent cases', 'The base case alone always proves a statement for every number', 'Induction requires no base case at all', 'A single case can never be part of a proof'], 0),
   ('Mathematical induction is especially useful for proving statements about ___.', ['Sequences, sums, and other statements indexed by natural numbers', 'Only continuous, non-integer measurements', 'Only geometric shapes with no numbers', 'Only statements with no variables'], 0)]),
Sc('Earth Science: Fossil Formation and the Geologic Time Scale',
   'Grade 10 Science strand: fossils form when the remains or traces of organisms are preserved in sediment over long periods, and scientists use fossils alongside rock layers to construct the geologic time scale, a framework dividing Earths history into eras, periods, and epochs.',
   [('How do most fossils typically form?', ['Remains or traces of organisms are preserved in sediment over long periods', 'Organisms instantly turn to stone upon death', 'Fossils form only within a single day', 'Fossils are created by volcanic eruptions exclusively'], 0),
    ('What do scientists use fossils and rock layers to construct?', ['The geologic time scale', 'A weather forecasting model', 'A map of ocean currents', 'A periodic table of elements'], 0),
    ('What is the geologic time scale used for?', ['Dividing Earths history into eras, periods, and epochs', 'Measuring the temperature of the ocean', 'Predicting daily weather patterns', 'Calculating the speed of tectonic plates only'], 0),
    ('Why are fossils useful to scientists studying Earths history?', ['They provide evidence of past life forms and environmental conditions', 'Fossils provide no useful scientific information', 'Fossils only exist in modern rock layers', 'Fossils are unrelated to the study of evolution'], 0),
    ('What principle helps scientists determine the relative age of fossils in undisturbed rock layers?', ['Deeper layers are generally older than layers above them', 'All rock layers are exactly the same age', 'Fossils in higher layers are always older', 'Rock layer position has no relation to age'], 0)]),
H('The Manitoba Schools Question and Language Rights',
  'Grade 10 History strand: the Manitoba Schools Question was a major political controversy of the 1890s over the provinces decision to eliminate public funding for Catholic and French-language schools, a dispute that intensified debates over minority language rights across Canada.',
  [('What was the Manitoba Schools Question primarily about?', ['The elimination of public funding for Catholic and French-language schools', 'A dispute over provincial boundaries', 'A disagreement over railway construction routes', 'A conflict over agricultural land grants'], 0),
   ('In what decade did the Manitoba Schools Question arise?', ['The 1890s', 'The 1860s', 'The 1940s', 'The 1980s'], 0),
   ('What broader issue did the controversy intensify debate over?', ['Minority language rights across Canada', 'Canadian participation in the League of Nations', 'Canadas naval policy', 'Immigration quotas from Europe'], 0),
   ('Which two groups were most directly affected by the funding changes?', ['Catholic and Francophone communities in Manitoba', 'Protestant communities in British Columbia', 'Indigenous communities in the Arctic', 'English-speaking communities in Ontario'], 0),
   ('Why is the Manitoba Schools Question still studied today?', ['It illustrates long-standing tensions over language and religious rights in Canadian federalism', 'It had no lasting effect on Canadian politics', 'It was resolved with no controversy at the time', 'It only affected a single small town with no wider relevance'], 0)]),
]),
day(127, [
E('Writing: The Investigative Report',
  'Grade 10 English strand: an investigative report presents research findings on a specific issue through a clear structure, evidence-based analysis, and credible sourcing, aiming to inform readers and often to expose a problem or hold a subject accountable.',
  [('What is the main purpose of an investigative report?', ['To present research findings on an issue through evidence-based analysis', 'To express purely personal opinions with no evidence', 'To entertain readers with fictional events', 'To advertise a product or service'], 0),
   ('What is essential to an effective investigative report?', ['Credible sourcing and evidence-based analysis', 'Unverified rumours presented as fact', 'A complete absence of structure', 'Exclusively anonymous, unconfirmed claims'], 0),
   ('Investigative reports often aim to ___.', ['Expose a problem or hold a subject accountable', 'Avoid any conclusions or findings', 'Promote a single product exclusively', 'Ignore public interest entirely'], 0),
   ('Which is a key step in producing an investigative report?', ['Gathering and verifying evidence from multiple credible sources', 'Relying on a single unverified source', 'Skipping any fact-checking process', 'Writing the conclusion before any research begins'], 0),
   ('Why is clear structure important in an investigative report?', ['It helps readers follow the evidence and understand the findings logically', 'Structure has no impact on how readers understand a report', 'Investigative reports should avoid any organization', 'Structure only matters in fictional writing'], 0)]),
M('Vectors: Scalar and Vector Projections',
  'Grade 10 Math strand: the scalar projection of one vector onto another measures how much of the first vector points in the direction of the second, while the vector projection expresses that amount as a vector itself, both calculated using the dot product.',
  [('What does a scalar projection measure?', ['How much of one vector points in the direction of another', 'The total area between two vectors', 'The angle between two lines only', 'The number of dimensions in a vector space'], 0),
   ('How does a vector projection differ from a scalar projection?', ['A vector projection expresses the projected amount as a vector, not just a magnitude', 'A vector projection has no direction at all', 'A vector projection is always equal to zero', 'A vector projection ignores the direction of the original vector'], 0),
   ('What operation is used to calculate a projection between two vectors?', ['The dot product', 'The cross product only', 'Simple addition of the vectors', 'Division of the vectors magnitudes'], 0),
   ('If two vectors are perpendicular, what is the scalar projection of one onto the other?', ['Zero', 'Equal to the magnitude of the longer vector', 'Always a negative number', 'Undefined in every case'], 0),
   ('Vector projections are useful in physics for calculating ___.', ['The component of a force acting in a specific direction', 'The total colour of an object', 'The temperature of a system', 'The taste of a substance'], 0)]),
Sc('Biology: Animal Behaviour, Instinct and Learning',
   'Grade 10 Science strand: animal behaviour includes both instinctive actions, inherited and performed correctly without prior experience, and learned behaviours acquired through experience or observation, and understanding the balance between the two helps explain how species survive and adapt.',
   [('What is instinctive behaviour?', ['An inherited behaviour performed correctly without prior experience', 'A behaviour that must always be taught by a parent', 'A behaviour found only in plants', 'A random, meaningless action with no purpose'], 0),
    ('What is learned behaviour?', ['A behaviour acquired through experience or observation', 'A behaviour present at birth with no experience needed', 'A behaviour that never changes throughout an animals life', 'A behaviour unrelated to survival'], 0),
    ('Which of these is an example of instinctive behaviour?', ['A newborn sea turtle moving toward the ocean immediately after hatching', 'A dog learning to sit after repeated training', 'A bird learning a new song by mimicking another bird', 'A chimpanzee learning to use a tool after watching others'], 0),
    ('Why is learned behaviour advantageous for some species?', ['It allows animals to adapt their actions based on changing circumstances', 'It prevents animals from ever adapting to their environment', 'It has no effect on an animals survival', 'It is identical to instinctive behaviour in every way'], 0),
    ('Understanding the balance between instinct and learning helps scientists explain ___.', ['How different species survive and adapt to their environments', 'Only the physical appearance of animals', 'Only the diet of a single species', 'Nothing related to animal survival'], 0)]),
H('British Columbia Joins Confederation in 1871',
  'Grade 10 History strand: British Columbia joined Confederation in 1871 after negotiating key conditions with the federal government, most notably a promise to build a transcontinental railway connecting the province to the rest of Canada within ten years.',
  [('In what year did British Columbia join Confederation?', ['1871', '1867', '1905', '1949'], 0),
   ('What major condition did British Columbia negotiate for joining Confederation?', ['A promise to build a transcontinental railway within ten years', 'A guarantee of complete independence from Canada', 'A permanent exemption from federal taxes', 'A promise to remain a British colony forever'], 0),
   ('What number province did British Columbia become upon joining?', ['The sixth province', 'The first province', 'The tenth province', 'The third province'], 0),
   ('Which railway project fulfilled the promise made to British Columbia?', ['The Canadian Pacific Railway', 'The Trans-Canada Highway', 'The St. Lawrence Seaway', 'The Grand Trunk Railway exclusively'], 0),
   ('Why was British Columbias entry into Confederation significant for Canada?', ['It extended Canadian territory to the Pacific coast', 'It had no effect on Canadas geographic extent', 'It caused Canada to lose access to the Pacific Ocean', 'It marked the end of Confederation expansion permanently'], 0)]),
]),
day(128, [
E('Grammar: Appositives and Nonrestrictive Clauses',
  'Grade 10 English strand: an appositive renames or explains a nearby noun, and a nonrestrictive clause adds extra, non-essential information about a noun, both typically set off with commas since removing them would not change the sentences essential meaning.',
  [('What does an appositive do?', ['Renames or explains a nearby noun', 'Replaces a verb with a noun', 'Functions only as a preposition', 'Introduces a question'], 0),
   ('What is a nonrestrictive clause?', ['A clause that adds extra, non-essential information about a noun', 'A clause that is essential to identifying the noun it modifies', 'A clause that functions as the main verb', 'A clause with no grammatical function at all'], 0),
   ('How are appositives and nonrestrictive clauses typically punctuated?', ['They are set off with commas', 'They are never punctuated in any way', 'They always end with a question mark', 'They are set off with exclamation marks'], 0),
   ('Which sentence contains an appositive?', ['My teacher, a former Olympic athlete, inspired the class.', 'My teacher inspired the class.', 'The teacher who inspired the class was an athlete.', 'My teacher inspires the class every single day.'], 0),
   ('Why can a nonrestrictive clause be removed without changing a sentences essential meaning?', ['Because it provides supplementary rather than identifying information', 'Because it is always the main clause of the sentence', 'Because removing any clause never changes meaning', 'Because nonrestrictive clauses never contain any information'], 0)]),
M('Probability: An Introduction to Bayes Theorem',
  'Grade 10 Math strand: Bayes Theorem provides a method for updating the probability of an event based on new evidence, relating conditional probabilities to revise an initial estimate into a more accurate one as additional information becomes available.',
  [('What does Bayes Theorem allow you to do?', ['Update the probability of an event based on new evidence', 'Calculate the area of a triangle', 'Solve a quadratic equation', 'Find the derivative of a function'], 0),
   ('Bayes Theorem relates which type of probabilities?', ['Conditional probabilities', 'Only probabilities equal to exactly one', 'Only impossible events with probability zero', 'Only probabilities involving whole numbers'], 0),
   ('What is the initial estimate of a probability, before new evidence is considered, often called?', ['The prior probability', 'The final probability', 'The impossible probability', 'The irrelevant probability'], 0),
   ('Why is Bayes Theorem useful in real-world decision-making?', ['It allows estimates to be revised as new, relevant information becomes available', 'It guarantees a certain outcome with no uncertainty', 'It eliminates the need for any evidence', 'It only applies to events that never happen'], 0),
   ('Bayes Theorem is widely applied in fields such as ___.', ['Medical diagnosis and spam email filtering', 'Only ancient historical record-keeping', 'Only basic arithmetic with whole numbers', 'Only measuring physical distances'], 0)]),
Sc('Chemistry: The Maillard Reaction and the Chemistry of Cooking',
   'Grade 10 Science strand: the Maillard reaction is a chemical reaction between amino acids and reducing sugars that occurs when food is heated, producing the browning, aroma, and flavour changes seen in foods like toasted bread, seared meat, and roasted coffee.',
   [('What two components react in the Maillard reaction?', ['Amino acids and reducing sugars', 'Only water and salt', 'Only oxygen and carbon dioxide', 'Only fats and proteins with no sugars involved'], 0),
    ('What triggers the Maillard reaction in food?', ['Heat', 'Freezing temperatures', 'Complete darkness with no heat', 'Adding only cold water'], 0),
    ('What visible change does the Maillard reaction typically cause in food?', ['Browning of the surface', 'The food becomes completely transparent', 'The food turns permanently blue', 'The food loses all mass instantly'], 0),
    ('Which of these foods commonly shows the effects of the Maillard reaction?', ['Seared meat', 'Raw lettuce', 'Ice water', 'Uncooked rice grains'], 0),
    ('Besides browning, what other sensory changes does the Maillard reaction produce?', ['Changes in aroma and flavour', 'A complete loss of all smell and taste', 'An increase in the foods transparency only', 'A permanent change in the foods temperature only'], 0)]),
H('Prince Edward Island Joins Confederation in 1873',
  'Grade 10 History strand: Prince Edward Island joined Confederation in 1873, six years after the original union, after federal financial assistance helped resolve a long-standing land ownership dispute involving absentee landlords on the island.',
  [('In what year did Prince Edward Island join Confederation?', ['1873', '1867', '1905', '1949'], 0),
   ('What long-standing dispute affected Prince Edward Island before Confederation?', ['A land ownership dispute involving absentee landlords', 'A dispute over provincial borders with Quebec', 'A conflict over fishing rights with the United States', 'A disagreement over railway routes through the island'], 0),
   ('What helped resolve the land dispute and encourage Confederation?', ['Federal financial assistance', 'A military intervention by Britain', 'A treaty with the United States', 'A decision by the League of Nations'], 0),
   ('How many years after the original 1867 Confederation did Prince Edward Island join?', ['Six years', 'One year', 'Fifty years', 'Twenty years'], 0),
   ('What number province did Prince Edward Island become?', ['The seventh province', 'The first province', 'The tenth province', 'The third province'], 0)]),
]),
day(129, [
E('Literature: The Trickster Figure in Folklore and Fiction',
  'Grade 10 English strand: the trickster is a recurring archetype found across many cultures mythologies and folklore, a clever, boundary-crossing figure who uses wit and deception to challenge authority, expose hypocrisy, or bring about change.',
  [('What defines a trickster figure?', ['A clever, boundary-crossing character who uses wit and deception', 'A character who always follows every rule strictly', 'A character with no personality traits', 'A minor character who never affects the plot'], 0),
   ('What role does a trickster often play in a narrative?', ['Challenging authority or exposing hypocrisy through cunning', 'Enforcing strict order with no disruption', 'Remaining entirely passive throughout the story', 'Narrating events with no involvement in the plot'], 0),
   ('Trickster figures appear in ___.', ['Many different cultures mythologies and folklore traditions', 'Only a single specific culture with no other examples', 'Only modern fiction with no historical roots', 'Only nonfiction historical writing'], 0),
   ('Which quality is most closely associated with trickster characters?', ['Wit and cunning used to outsmart others', 'Complete honesty in every situation', 'An inability to speak or communicate', 'A total lack of intelligence'], 0),
   ('Why do trickster figures often bring about change in a story?', ['Their disruptive, boundary-crossing actions challenge the existing order', 'They strictly maintain the status quo at all times', 'They have no influence on other characters', 'They are always removed from the plot immediately'], 0)]),
M('Complex Numbers: Roots of Unity',
  'Grade 10 Math strand: the nth roots of unity are the complex solutions to the equation z^n = 1, evenly spaced points on the unit circle in the complex plane that can be found using De Moivres Theorem and reveal deep connections between algebra and geometry.',
  [('What equation defines the nth roots of unity?', ['z^n = 1', 'z^n = 0', 'z + n = 1', 'z^n = n'], 0),
   ('Where are the nth roots of unity located in the complex plane?', ['Evenly spaced points on the unit circle', 'Randomly scattered points with no pattern', 'Only on the real number line', 'Only at the origin'], 0),
   ('Which earlier theorem is used to find the roots of unity?', ['De Moivres Theorem', 'The Pythagorean Theorem', 'The Fundamental Theorem of Arithmetic', 'The Binomial Theorem'], 0),
   ('How many distinct nth roots of unity exist for a given positive integer n?', ['Exactly n', 'Exactly one, regardless of n', 'Infinitely many for every value of n', 'Exactly zero'], 0),
   ('The roots of unity reveal a connection between which two branches of mathematics?', ['Algebra and geometry', 'Only basic arithmetic and probability', 'Only statistics and data management', 'Only financial literacy and measurement'], 0)]),
Sc('Biology: Camouflage, Mimicry, and Predator-Prey Adaptations',
   'Grade 10 Science strand: camouflage allows organisms to blend into their surroundings to avoid detection, while mimicry involves one species evolving to resemble another, and both are adaptations shaped by natural selection that influence predator-prey relationships in an ecosystem.',
   [('What is camouflage?', ['An adaptation that allows organisms to blend into their surroundings', 'A method animals use to communicate through sound only', 'A process of digesting food quickly', 'A behaviour found only in plants'], 0),
    ('What is mimicry?', ['When one species evolves to resemble another species', 'When an animal changes colour randomly with no pattern', 'When a species loses all its distinguishing features', 'When two unrelated species merge into one organism'], 0),
    ('Why might a harmless species evolve to mimic a dangerous one?', ['To deter predators by appearing more threatening than it actually is', 'To attract more predators intentionally', 'Mimicry has no survival benefit', 'To become less visible to its own prey only'], 0),
    ('What evolutionary process shapes adaptations like camouflage and mimicry?', ['Natural selection', 'Random, purposeless mutation with no selection pressure', 'A process unrelated to survival', 'A process that only affects plants'], 0),
    ('How do camouflage and mimicry influence predator-prey relationships?', ['They shift the balance of detection and evasion between predators and prey', 'They have no effect on predator-prey interactions', 'They guarantee prey species always survive', 'They guarantee predator species always fail to find food'], 0)]),
H('The Halibut Treaty of 1923 and Early Canadian Autonomy in Foreign Affairs',
  'Grade 10 History strand: the Halibut Treaty of 1923 was the first international treaty negotiated and signed by Canada independently of Britain, a landmark step in the development of Canadian sovereignty in foreign affairs that paved the way for later milestones like the Balfour Declaration.',
  [('What made the Halibut Treaty of 1923 historically significant?', ['It was the first international treaty negotiated and signed by Canada independently of Britain', 'It ended all trade between Canada and the United States', 'It established the Royal Canadian Navy', 'It was the first treaty ever signed by any British colony'], 0),
   ('What was the subject of the Halibut Treaty?', ['Fishing rights and conservation in the Pacific', 'Railway construction rights', 'Immigration quotas', 'Military alliance terms'], 0),
   ('Which country did Canada sign the Halibut Treaty with?', ['The United States', 'France', 'Japan', 'Russia'], 0),
   ('In what year was the Halibut Treaty signed?', ['1923', '1867', '1949', '1905'], 0),
   ('How did the Halibut Treaty pave the way for later developments in Canadian autonomy?', ['It set a precedent for Canada acting independently in foreign affairs, later reinforced by the Balfour Declaration', 'It ended any further Canadian involvement in foreign affairs', 'It had no connection to later constitutional developments', 'It transferred all foreign policy control back to Britain permanently'], 0)]),
]),
day(130, [
E('English Review: Grammar, Style, and Contemporary Literacy',
  'Grade 10 English strand review: students revisit gerunds and infinitives, stream-of-consciousness narration, the eulogy, postmodern fiction and metafiction, algorithmic bias, pathetic fallacy and personification, the investigative report, appositives, and the trickster figure.',
  [('What is a gerund?', ['A verb form ending in -ing that functions as a noun', 'A verb that shows past tense only', 'A word that replaces a pronoun', 'A type of conjunction'], 0),
   ('What does stream-of-consciousness narration attempt to capture?', ['The continuous, often unstructured flow of a characters thoughts and impressions', 'A strictly chronological sequence of external events', 'Only dialogue spoken between characters', 'A formal summary of the plot'], 0),
   ('What is metafiction?', ['Storytelling that draws attention to its own fictional nature', 'A story with no narrator or characters', 'A purely factual, non-fictional report', 'A subgenre of poetry only'], 0),
   ('What is pathetic fallacy?', ['Attributing human emotions to nature or weather to reflect a characters mood', 'A logical error in an argument', 'A type of grammatical mistake', 'A method of citing sources'], 0),
   ('What defines a trickster figure?', ['A clever, boundary-crossing character who uses wit and deception', 'A character who always follows every rule strictly', 'A character with no personality traits', 'A minor character who never affects the plot'], 0)]),
M('Math Review: Derivatives, Number Theory, and Advanced Concepts',
  'Grade 10 Math strand review: students revisit the product and quotient rules, the Euclidean Algorithm, hypothesis testing, partial fraction decomposition, non-Euclidean geometry, mathematical induction, vector projections, Bayes Theorem, and roots of unity.',
  [('What does the product rule allow you to differentiate?', ['A function formed by multiplying two other functions together', 'Only a single constant term', 'A function formed by adding two constants', 'Only trigonometric ratios with no functions involved'], 0),
   ('What does the Euclidean Algorithm calculate?', ['The greatest common divisor of two integers', 'The least common multiple of two fractions only', 'The square root of a number', 'The area of a rectangle'], 0),
   ('What is a null hypothesis?', ['A default assumption of no effect or no difference', 'A hypothesis that is always proven true', 'A hypothesis with no possible outcome', 'A statement with no statistical meaning'], 0),
   ('What does the principle of mathematical induction prove?', ['That a statement holds true for every natural number', 'That a statement is true for only one specific number', 'That an equation has no solution', 'That a shape has a certain area'], 0),
   ('What does Bayes Theorem allow you to do?', ['Update the probability of an event based on new evidence', 'Calculate the area of a triangle', 'Solve a quadratic equation', 'Find the derivative of a function'], 0)]),
Sc('Science Review: Human Biology, Chemistry, and Earth Science',
   'Grade 10 Science strand review: students revisit the integumentary system, buffers and pH regulation, glaciers and ice ages, semiconductors, coral reefs, fossil formation and the geologic time scale, instinct versus learning, the Maillard reaction, and camouflage and mimicry.',
   [('What is the skin considered in relation to the human body?', ['The largest organ of the body', 'The smallest organ of the body', 'An organ found only in mammals with fur', 'A structure unrelated to any body system'], 0),
    ('What is a buffer solution?', ['A solution that resists changes in pH when acid or base is added', 'A solution that always becomes strongly acidic', 'A solution with no chemical properties', 'A pure solvent with no solute'], 0),
    ('What is a semiconductor?', ['A material with electrical conductivity between a conductor and an insulator', 'A material that always conducts electricity perfectly', 'A material that never conducts electricity at all', 'A material used only for insulation'], 0),
    ('What do scientists use fossils and rock layers to construct?', ['The geologic time scale', 'A weather forecasting model', 'A map of ocean currents', 'A periodic table of elements'], 0),
    ('What is camouflage?', ['An adaptation that allows organisms to blend into their surroundings', 'A method animals use to communicate through sound only', 'A process of digesting food quickly', 'A behaviour found only in plants'], 0)]),
H('History Review: Canadian Confederation and Constitutional Development',
  'Grade 10 History strand review: students revisit the 1919 Paris Peace Conference, the King-Byng Affair, the Manitoba Act, the Canadian Pacific Railway, the Rowell-Sirois Commission, the Manitoba Schools Question, British Columbia and Prince Edward Island joining Confederation, and the Halibut Treaty.',
  [('What major agreement was signed at the Paris Peace Conference in 1919?', ['The Treaty of Versailles', 'The Treaty of Ghent', 'The Statute of Westminster', 'The Balfour Declaration'], 0),
   ('What did Governor General Byng refuse to do in 1926?', ['Dissolve Parliament at Prime Minister Kings request', 'Sign the Treaty of Versailles', 'Approve the Balfour Declaration', 'Call a referendum on Confederation'], 0),
   ('What did the Manitoba Act of 1870 create?', ['The province of Manitoba', 'The province of Saskatchewan', 'The province of Alberta', 'The Northwest Territories'], 0),
   ('What promise did the Canadian Pacific Railway fulfill?', ['A promise made to British Columbia upon joining Confederation', 'A promise made to Newfoundland in 1949', 'A promise made during the War of 1812', 'A promise made to Quebec after the 1867 Confederation'], 0),
   ('What made the Halibut Treaty of 1923 historically significant?', ['It was the first international treaty negotiated and signed by Canada independently of Britain', 'It ended all trade between Canada and the United States', 'It established the Royal Canadian Navy', 'It was the first treaty ever signed by any British colony'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_121_130)
    append_to(10, g10_121_130)
