#!/usr/bin/env python3
"""Phase 5: Grade 8, Days 71-80 (fifth Grade 8 batch, extending the school
year past the Day 70 milestone). Topics chosen to avoid any overlap with
the existing Day 1-70 set (see data/grade8.ts): mood/tone, formal business
letters, verbals, fact-checking, unreliable narrators, shades of meaning,
procedural writing, characterization techniques, and sentence
fragments/run-ons in Language; prime factorization/GCF/LCM, systems of
equations by graphing, composite figures, two-way tables, percent change,
independent/dependent events, circle theorems, recursive/explicit
formulas, and lines of best fit in Math; structures and mechanisms,
elements/compounds/mixtures, Earth's internal layers, genetic mutations,
Newton's laws of motion, the carbon cycle, phases of the Moon, 3D
printing, and the nervous system in Science; and the Klondike Gold Rush
through the Boer War, the Quiet Revolution, the 1967 immigration points
system, the Japanese Canadian Redress Agreement, the Free Trade
Agreement, the cod moratorium, the creation of Nunavut, and NATO/NORAD in
History.

Grade 8's fourth subject key remains "History" (not "SocialStudies"),
consistent with the Days 31-40, 41-50, 51-60, and 61-70 batches and the
pre-existing data/grade8.ts.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes and quotation marks
use the curly Unicode form (’ “ ”) so they never collide with the
double-quoted TS string literals the generator embeds them in.
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-social-studies'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science & Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


g8_71_80 = [
day(71, [
L('Reading: Analyzing Mood and Tone',
  'Grade 8 Reading strand: mood is the emotional atmosphere a reader feels while reading a text, while tone is the author’s attitude toward the subject, often revealed through word choice, imagery, and sentence structure.',
  [('Mood in a text is best described as ___.', ['The emotional atmosphere a reader feels while reading', 'The exact number of characters in a story', 'A concept unrelated to mood', 'The physical setting where a story takes place'], 0),
   ('Tone in a text is best described as ___.', ['The author’s attitude toward the subject, revealed through word choice', 'The emotional atmosphere the reader feels, with no connection to the author', 'A concept unrelated to tone', 'The total number of pages in a text'], 0),
   ('Which word choice would most likely create a tense, uneasy mood?', ['Words like lurking, shadowy, and creeping', 'Words like sunny, cheerful, and bright', 'A set of words unrelated to mood', 'Words like calm, peaceful, and gentle'], 0),
   ('An author writing with a sarcastic tone about a topic is expressing ___.', ['Attitude that says the opposite of what is literally stated', 'Complete sincerity with no hidden meaning', 'A concept unrelated to tone', 'Total indifference toward the subject'], 0),
   ('Why is distinguishing between mood and tone useful when analyzing a text?', ['It helps a reader separate how a text feels from what the author’s attitude toward it is', 'Mood and tone are always identical with no distinction needed', 'A reason unrelated to reading comprehension', 'Neither mood nor tone affects how a reader interprets a text'], 0)]),
M('Number Theory: Prime Factorization, GCF, and LCM',
  'Grade 8 Math strand: prime factorization expresses a number as a product of prime numbers, and this factorization can be used to find the greatest common factor (GCF) and least common multiple (LCM) of two or more numbers.',
  [('Prime factorization expresses a number as ___.', ['A product of prime numbers', 'A sum of consecutive integers', 'A concept unrelated to prime factorization', 'The square root of the original number'], 0),
   ('The prime factorization of 12 is ___.', ['2 x 2 x 3', '2 x 6', 'A value unrelated to the calculation', '3 x 4'], 0),
   ('The greatest common factor (GCF) of 18 and 24 is ___.', ['6', '3', 'A value unrelated to the calculation', '9'], 0),
   ('The least common multiple (LCM) of 4 and 6 is ___.', ['12', '10', 'A value unrelated to the calculation', '24'], 0),
   ('Why is finding the GCF useful when simplifying a fraction?', ['Dividing both the numerator and denominator by the GCF reduces the fraction to its lowest terms', 'The GCF has no connection to simplifying fractions', 'A reason unrelated to prime factorization', 'Multiplying by the GCF always makes a fraction larger'], 0)]),
Sc('Structures and Mechanisms: Load, Stress, and Structural Strength',
   'Grade 8 Science strand: a structure must be designed to withstand different types of load and stress, such as compression, tension, and shear, and engineers select shapes and materials that distribute these forces effectively.',
   [('A load applied to a structure is best described as ___.', ['A force the structure must support or withstand', 'A colour applied to the surface of a structure', 'A concept unrelated to structural load', 'A measurement of a structure’s height only'], 0),
    ('Compression is a type of stress that occurs when a structure is ___.', ['Squeezed or pushed together', 'Stretched or pulled apart', 'A concept unrelated to compression', 'Twisted around its centre'], 0),
    ('Tension is a type of stress that occurs when a structure is ___.', ['Stretched or pulled apart', 'Squeezed or pushed together', 'A concept unrelated to tension', 'Left completely still with no force applied'], 0),
    ('Why do engineers often use triangular shapes in structural frameworks?', ['Triangles distribute force evenly and resist changing shape under load', 'Triangles are the weakest possible shape for supporting a load', 'A reason unrelated to structural design', 'Triangular shapes are chosen only for decoration'], 0),
    ('Why is understanding load and stress important when designing a bridge?', ['It ensures the bridge can safely support the forces acting on it without failing', 'Load and stress have no effect on whether a bridge can support weight', 'A reason unrelated to structures and mechanisms', 'Bridges never experience any force once they are built'], 0)]),
H('The Klondike Gold Rush',
  'Grade 8 History strand: the Klondike Gold Rush of 1896-99 drew tens of thousands of prospectors to the Yukon after gold was discovered near Dawson City, rapidly transforming the region and prompting Canada to establish stronger governance in the north.',
  [('The Klondike Gold Rush took place primarily in ___.', ['The Yukon', 'Southern Ontario', 'A region unrelated to the Klondike Gold Rush', 'Nova Scotia'], 0),
   ('The Klondike Gold Rush began after gold was discovered near ___.', ['Dawson City', 'Toronto', 'A location unrelated to the Klondike Gold Rush', 'Halifax'], 0),
   ('The Klondike Gold Rush primarily took place during ___.', ['1896-99', '1812-14', 'A time period unrelated to the Klondike Gold Rush', '1929-33'], 0),
   ('One effect of the Klondike Gold Rush on the Canadian government was that it ___.', ['Prompted Canada to establish stronger governance and infrastructure in the north', 'Caused Canada to abandon all interest in the northern territories', 'A result unrelated to the Klondike Gold Rush', 'Led to the immediate creation of the province of Yukon'], 0),
   ('Why is the Klondike Gold Rush considered a significant event in Canadian history?', ['It rapidly transformed the Yukon and drew national attention to Canada’s north', 'It had no lasting effect on the Yukon or Canada as a whole', 'A reason unrelated to its historical significance', 'It occurred entirely outside of Canadian territory'], 0)])]),
day(72, [
L('Writing: The Formal Business Letter and Email',
  'Grade 8 Writing strand: a formal business letter or email follows a professional structure — a clear subject line or heading, formal greeting, concise body, and polite closing — appropriate for communicating with an organization or unfamiliar recipient.',
  [('A formal business letter typically begins with ___.', ['A formal greeting addressing the recipient', 'An informal joke to open the message', 'A concept unrelated to business letters', 'A list of unrelated personal stories'], 0),
   ('Why might a formal email include a clear subject line?', ['It helps the recipient quickly understand the purpose of the message', 'Subject lines never provide any useful information', 'A reason unrelated to formal email writing', 'A subject line is only needed in a resume'], 0),
   ('Which closing is most appropriate for a formal business letter?', ['Sincerely', 'See ya', 'A closing unrelated to formal letters', 'Peace out'], 0),
   ('Why should a formal business letter avoid slang and casual language?', ['It maintains a professional and respectful tone for the recipient', 'Slang always makes a letter more professional', 'A reason unrelated to formal writing', 'Formal letters are never read by anyone important'], 0),
   ('Why is it important to proofread a formal email before sending it?', ['Errors can make the message appear less professional and harder to understand', 'Proofreading never changes how a message is received', 'A reason unrelated to formal writing', 'Formal emails are never checked for mistakes'], 0)]),
M('Algebra: Solving Systems of Equations by Graphing',
  'Grade 8 Math strand: solving a system of linear equations by graphing involves plotting both equations on the same coordinate plane, where the point of intersection represents the solution that satisfies both equations.',
  [('Solving a system of equations by graphing involves ___.', ['Plotting both equations and finding their point of intersection', 'Plotting only one equation and ignoring the other', 'A concept unrelated to solving systems by graphing', 'Adding the two equations together without graphing them'], 0),
   ('The point of intersection of two graphed lines represents ___.', ['The solution that satisfies both equations', 'A point that satisfies neither equation', 'A concept unrelated to systems of equations', 'The y-intercept of only one equation'], 0),
   ('If two lines in a system are parallel and never intersect, the system has ___.', ['No solution', 'Exactly one solution', 'A result unrelated to systems of equations', 'Infinitely many solutions'], 0),
   ('If two equations in a system graph as the exact same line, the system has ___.', ['Infinitely many solutions', 'No solution', 'A result unrelated to systems of equations', 'Exactly one solution'], 0),
   ('Why might solving a system by graphing be less precise than solving it algebraically?', ['Reading an exact intersection point from a graph can be difficult, especially with non-integer solutions', 'Graphing always produces a more precise answer than algebra', 'A reason unrelated to solving systems of equations', 'Graphing and algebraic methods always produce different, unrelated answers'], 0)]),
Sc('Chemistry: Elements, Compounds, and Mixtures',
   'Grade 8 Science strand: matter can be classified as an element, a pure substance made of only one type of atom, a compound, two or more elements chemically combined, or a mixture, two or more substances physically combined without a fixed ratio.',
   [('An element is a pure substance made of ___.', ['Only one type of atom', 'Two or more types of atoms chemically combined', 'A concept unrelated to elements', 'Substances combined in no fixed ratio'], 0),
    ('A compound is formed when ___.', ['Two or more elements are chemically combined in a fixed ratio', 'A single element exists on its own', 'A concept unrelated to compounds', 'Substances are physically mixed with no chemical bonding'], 0),
    ('A mixture is best described as ___.', ['Two or more substances physically combined without a fixed ratio', 'A single pure substance made of only one type of atom', 'A concept unrelated to mixtures', 'A substance that can never be separated into parts'], 0),
    ('Which of these is an example of a compound?', ['Water, made of hydrogen and oxygen chemically bonded', 'Oxygen gas on its own', 'A substance unrelated to compounds', 'A salad containing separate, unmixed ingredients'], 0),
    ('Why can a mixture, unlike a compound, generally be separated using physical methods?', ['The substances in a mixture are not chemically bonded together', 'Mixtures are always chemically bonded more strongly than compounds', 'A reason unrelated to mixtures and compounds', 'Compounds can always be separated more easily than mixtures'], 0)]),
H('Canada and the South African (Boer) War',
  'Grade 8 History strand: Canada sent volunteer troops to fight alongside Britain in the South African War of 1899-1902, marking the country’s first overseas military commitment and sparking early debate over Canada’s independence from British foreign policy.',
  [('The South African War, also known as the Boer War, took place from ___.', ['1899 to 1902', '1914 to 1918', 'A time period unrelated to the Boer War', '1867 to 1870'], 0),
   ('Canada’s involvement in the Boer War represented ___.', ['The country’s first overseas military commitment', 'Canada’s first war fought entirely on its own soil', 'A description unrelated to the Boer War', 'A conflict Canada refused to participate in at all'], 0),
   ('Canadian troops in the Boer War fought alongside ___.', ['Britain', 'The United States', 'A country unrelated to the Boer War', 'France'], 0),
   ('Debate over Canada’s participation in the Boer War centred on ___.', ['Whether Canada should follow British foreign policy or act independently', 'Whether Canada should join the war against Britain', 'A debate unrelated to the Boer War', 'Whether to abolish the Canadian military entirely'], 0),
   ('Why is the Boer War significant in the development of Canadian identity?', ['It raised early questions about how independently Canada should act from Britain', 'It had no connection to questions about Canadian independence', 'A reason unrelated to its historical significance', 'It ended Canada’s relationship with Britain immediately and completely'], 0)])]),
day(73, [
L('Grammar: Verbals — Gerunds, Participles, and Infinitives',
  'Grade 8 Grammar strand: a verbal is a word formed from a verb that functions as a different part of speech — a gerund acts as a noun, a participle acts as an adjective, and an infinitive can act as a noun, adjective, or adverb.',
  [('A gerund is a verb form ending in -ing that functions as a ___.', ['Noun', 'Adjective only', 'A part of speech unrelated to gerunds', 'Preposition'], 0),
   ('A participle is a verb form that functions as ___.', ['An adjective', 'A noun only', 'A part of speech unrelated to participles', 'A conjunction'], 0),
   ('An infinitive is typically formed using ___.', ['To plus the base form of a verb', 'Only the past tense of a verb', 'A form unrelated to infinitives', 'The verb with an -ed ending'], 0),
   ('In the sentence “Swimming is my favourite hobby,” the word swimming functions as a ___.', ['Gerund acting as the subject noun', 'Participle acting as an adjective', 'A part of speech unrelated to verbals', 'Preposition introducing a phrase'], 0),
   ('Why might a writer use verbals instead of separate simple sentences?', ['They can combine ideas smoothly and add variety to sentence structure', 'Verbals always make writing harder to understand with no benefit', 'A reason unrelated to grammar', 'Verbals can never be used in formal writing'], 0)]),
M('Geometry: Volume and Surface Area of Composite Figures',
  'Grade 8 Math strand: a composite figure is made by combining two or more simple three-dimensional shapes, and its volume or surface area can be found by calculating each individual shape’s measurement and combining the results.',
  [('A composite figure is a three-dimensional shape formed by ___.', ['Combining two or more simple shapes', 'Removing every face from a single shape', 'A concept unrelated to composite figures', 'A single shape with no other shapes involved'], 0),
   ('To find the volume of a composite figure, a student should ___.', ['Calculate the volume of each individual shape and add them together', 'Multiply the volumes of each shape together', 'A method unrelated to composite figures', 'Use only the volume of the largest shape and ignore the rest'], 0),
   ('A silo shaped like a cylinder topped with a hemisphere is an example of ___.', ['A composite figure', 'A single simple shape with no combination involved', 'A concept unrelated to composite figures', 'A two-dimensional shape only'], 0),
   ('When calculating the surface area of a composite figure, a student must be careful to ___.', ['Exclude any internal faces where two shapes are joined together', 'Include every face of every shape, even hidden internal ones', 'A concept unrelated to surface area of composite figures', 'Ignore all curved surfaces in the calculation'], 0),
   ('Why are composite figures commonly used in real-world architecture and design?', ['Combining simple shapes allows for more complex, functional, and creative structures', 'Composite figures are never used in real-world design', 'A reason unrelated to composite figures', 'Simple shapes alone can achieve every design goal with no combination needed'], 0)]),
Sc('Earth and Space: Earth’s Internal Layers and Heat Transfer',
   'Grade 8 Science strand: Earth is composed of distinct internal layers — the crust, mantle, outer core, and inner core — and heat generated in the core drives convection currents in the mantle that influence processes at the surface.',
   [('Earth’s outermost layer is called the ___.', ['Crust', 'Mantle', 'A layer unrelated to Earth’s structure', 'Inner core'], 0),
    ('Earth’s inner core is believed to be ___.', ['Solid, due to immense pressure despite extremely high temperatures', 'Liquid, and cooler than the outer core', 'A concept unrelated to Earth’s inner core', 'Made entirely of gas'], 0),
    ('Convection currents in the mantle are driven primarily by ___.', ['Heat generated within Earth’s core', 'Cold air currents from the atmosphere', 'A cause unrelated to convection currents', 'Ocean tides pulling on the mantle'], 0),
    ('Which layer of the Earth is where tectonic plates are located?', ['The crust', 'The inner core', 'A layer unrelated to tectonic plates', 'The outer core only'], 0),
    ('Why is understanding Earth’s internal heat important for explaining surface geological activity?', ['Convection currents driven by internal heat help move tectonic plates and shape the surface', 'Earth’s internal heat has no connection to surface geological activity', 'A reason unrelated to Earth’s structure', 'The crust moves completely independently of any internal heat or currents'], 0)]),
H('The Quiet Revolution in Quebec',
  'Grade 8 History strand: the Quiet Revolution was a period of rapid social, political, and economic change in Quebec during the 1960s, marked by the secularization of institutions, expansion of the provincial government, and the rise of Quebec nationalism.',
  [('The Quiet Revolution took place primarily during the ___.', ['1960s', '1930s', 'A time period unrelated to the Quiet Revolution', '1990s'], 0),
   ('The Quiet Revolution in Quebec involved the secularization of institutions, meaning ___.', ['The provincial government took over roles previously held by the Catholic Church', 'The Catholic Church gained even greater control over Quebec’s institutions', 'A meaning unrelated to secularization', 'Religious institutions were left completely unchanged'], 0),
   ('The Quiet Revolution contributed to a rise in ___.', ['Quebec nationalism', 'Support for a return to earlier, more traditional institutions', 'A concept unrelated to the Quiet Revolution', 'A decline in interest in Quebec’s provincial government'], 0),
   ('During the Quiet Revolution, the government of Quebec expanded its role in areas such as ___.', ['Education and healthcare', 'Only agriculture, with no other sectors affected', 'A sector unrelated to the Quiet Revolution', 'International military alliances'], 0),
   ('Why is the Quiet Revolution considered a turning point in Quebec’s history?', ['It rapidly modernized Quebec society and reshaped its political and cultural identity', 'It had no lasting effect on Quebec’s society or politics', 'A reason unrelated to its historical significance', 'It reversed all previous social and political change in Quebec'], 0)])]),
day(74, [
L('Media Literacy: Fact-Checking and Source Verification',
  'Grade 8 Media Literacy strand: fact-checking involves verifying claims against reliable, independent sources before accepting or sharing information, an essential skill for evaluating news and content encountered online.',
  [('Fact-checking involves ___.', ['Verifying claims against reliable, independent sources', 'Accepting every claim without question', 'A concept unrelated to fact-checking', 'Sharing information immediately with no review'], 0),
   ('Which of these is a sign that a source may be reliable?', ['The source cites evidence and is transparent about where information came from', 'The source provides no evidence and hides its author', 'A characteristic unrelated to reliable sources', 'The source only uses emotional language with no facts'], 0),
   ('Why is it useful to check multiple independent sources before believing a claim?', ['It helps confirm whether the claim is supported by consistent evidence', 'Checking multiple sources never changes how believable a claim is', 'A reason unrelated to fact-checking', 'A single source is always enough to confirm any claim'], 0),
   ('Which of these is a red flag when evaluating an online claim?', ['The claim has no cited evidence and cannot be verified elsewhere', 'The claim is supported by several credible, independent sources', 'A characteristic unrelated to evaluating claims', 'The source clearly explains its methodology and evidence'], 0),
   ('Why is fact-checking an important skill when using social media?', ['Misinformation can spread quickly, so verifying claims helps prevent sharing false information', 'Misinformation never appears on social media', 'A reason unrelated to media literacy', 'Fact-checking has no effect on what a person chooses to share'], 0)]),
M('Data Management: Two-Way Tables and Conditional Frequency',
  'Grade 8 Math strand: a two-way table organizes data by two categorical variables, allowing conditional frequencies to be calculated to compare how one variable relates to another within the data set.',
  [('A two-way table organizes data by ___.', ['Two categorical variables displayed in rows and columns', 'A single variable displayed in one row only', 'A concept unrelated to two-way tables', 'Numerical data with no categories involved'], 0),
   ('A conditional frequency describes ___.', ['The frequency of one variable given a specific condition of another variable', 'The total frequency of an entire data set with no conditions', 'A concept unrelated to conditional frequency', 'A frequency that never changes based on any condition'], 0),
   ('In a two-way table comparing favourite sport and grade level, the row totals typically represent ___.', ['The total count for each category in one variable', 'The total count for the entire table combined into one number', 'A concept unrelated to two-way tables', 'The percentage of students who dislike every sport listed'], 0),
   ('Why might a two-way table be useful for identifying a relationship between two variables?', ['It organizes the data so patterns and comparisons can be seen clearly', 'Two-way tables never reveal any relationship between variables', 'A reason unrelated to two-way tables', 'A two-way table can only display a single variable at a time'], 0),
   ('If 30 out of 50 students who play soccer also play basketball, what conditional frequency does this represent?', ['The frequency of playing basketball, given that a student plays soccer', 'The frequency of playing soccer, given that a student plays no other sport', 'A value unrelated to the calculation', 'The total number of students in the entire school'], 0)]),
Sc('Genetics: Mutations and Genetic Variation',
   'Grade 8 Science strand: a mutation is a change in an organism’s DNA sequence that can arise spontaneously or from environmental factors, and mutations are a key source of the genetic variation that natural selection acts upon.',
   [('A mutation is best described as ___.', ['A change in an organism’s DNA sequence', 'A trait that is always passed down unchanged for every generation', 'A concept unrelated to mutations', 'A process that only occurs in plants and never in animals'], 0),
    ('Mutations can be caused by ___.', ['Environmental factors such as radiation or certain chemicals', 'A complete absence of any environmental influence', 'A cause unrelated to mutations', 'Only deliberate actions taken by an organism'], 0),
    ('Mutations are considered a key source of ___.', ['Genetic variation within a population', 'Complete genetic uniformity within a population', 'A concept unrelated to mutations', 'The total elimination of all genetic differences'], 0),
    ('A mutation that occurs in a reproductive cell is significant because it ___.', ['Can be passed on to offspring', 'Can never be passed on to any future generation', 'A concept unrelated to mutations', 'Only affects the individual organism and no others'], 0),
    ('Why are mutations important to the process of natural selection?', ['They introduce new genetic variation that can be selected for or against based on the environment', 'Mutations have no connection to natural selection', 'A reason unrelated to genetics', 'Natural selection can only act on traits that never change'], 0)]),
H('The 1967 Immigration Points System',
  'Grade 8 History strand: in 1967, Canada introduced a points-based immigration system that evaluated applicants using factors such as education and skills rather than race or country of origin, replacing earlier discriminatory immigration policies.',
  [('The points-based immigration system was introduced by Canada in ___.', ['1967', '1900', 'A year unrelated to the immigration points system', '1945'], 0),
   ('The points system evaluated immigration applicants based primarily on ___.', ['Factors such as education and skills', 'Race and country of origin', 'A factor unrelated to the points system', 'Religious affiliation alone'], 0),
   ('The introduction of the points system replaced earlier immigration policies that were ___.', ['Discriminatory, often favouring applicants from specific countries or backgrounds', 'Already based entirely on education and skill, with no changes needed', 'A description unrelated to earlier immigration policies', 'Focused only on refugees, with no other immigration categories'], 0),
   ('A key goal of the 1967 points system was to make Canadian immigration policy ___.', ['More fair and objective by focusing on measurable qualifications', 'More restrictive toward every applicant regardless of qualifications', 'A goal unrelated to the points system', 'Entirely closed to new immigrants'], 0),
   ('Why is the 1967 points system considered a significant shift in Canadian immigration history?', ['It moved Canada away from race-based immigration policy toward a more merit-based system', 'It had no effect on how immigration applicants were evaluated', 'A reason unrelated to its historical significance', 'It reintroduced restrictions based on country of origin'], 0)])]),
day(75, [
L('Reading: Unreliable Narrators in Fiction',
  'Grade 8 Reading strand: an unreliable narrator is a storyteller whose credibility is compromised, whether by bias, limited knowledge, or dishonesty, requiring readers to question the narrator’s version of events.',
  [('An unreliable narrator is a storyteller whose ___.', ['Credibility is compromised, requiring readers to question their account', 'Account is always completely accurate and trustworthy', 'A concept unrelated to unreliable narrators', 'Perspective is identical to every other character in the story'], 0),
   ('Which of these might cause a narrator to be considered unreliable?', ['Personal bias that distorts their description of events', 'Complete honesty about every event in the story', 'A cause unrelated to unreliable narrators', 'Access to every character’s private thoughts with total accuracy'], 0),
   ('Why might an author choose to use an unreliable narrator?', ['To create suspense or encourage readers to think critically about the story', 'Unreliable narrators never add anything meaningful to a story', 'A reason unrelated to unreliable narrators', 'To make a story simpler and easier to follow'], 0),
   ('What reading strategy is useful when encountering a potentially unreliable narrator?', ['Looking for clues elsewhere in the text that confirm or contradict the narrator’s claims', 'Believing everything the narrator says without question', 'A strategy unrelated to unreliable narrators', 'Ignoring the narrator’s account entirely with no analysis'], 0),
   ('A young child narrator with limited understanding of adult events is an example of ___.', ['An unreliable narrator due to limited knowledge', 'A narrator who is always completely reliable', 'A concept unrelated to unreliable narrators', 'A narrator with no connection to the story at all'], 0)]),
M('Financial Literacy: Percent Change, Markup, and Discount',
  'Grade 8 Math strand: percent change describes how much a value has increased or decreased relative to its original amount, and this concept applies directly to calculating a markup added by a retailer or a discount subtracted during a sale.',
  [('Percent change describes ___.', ['How much a value has increased or decreased relative to its original amount', 'The exact dollar amount of an item with no percentage involved', 'A concept unrelated to percent change', 'A value that never changes regardless of price adjustments'], 0),
   ('A markup is ___.', ['An amount added to the cost of an item to determine its selling price', 'An amount subtracted from an item during a clearance sale', 'A concept unrelated to markup', 'A fixed tax applied equally to every product'], 0),
   ('An item that originally costs 40 dollars is discounted by 25 percent. What is the sale price?', ['30 dollars', '35 dollars', 'A value unrelated to the calculation', '10 dollars'], 0),
   ('A store buys a shirt for 20 dollars and sells it for 30 dollars. What is the percent markup?', ['50 percent', '30 percent', 'A value unrelated to the calculation', '150 percent'], 0),
   ('Why is understanding percent change useful when comparing sale prices at different stores?', ['It allows a shopper to calculate the actual savings and compare true value between offers', 'Percent change provides no useful information when shopping', 'A reason unrelated to percent change', 'Every percent discount always results in the exact same savings regardless of price'], 0)]),
Sc('Physics: Newton’s Laws of Motion',
   'Grade 8 Science strand: Newton’s three laws of motion describe how objects behave under forces — an object at rest or in motion maintains its state unless acted on by a force, force equals mass times acceleration, and every action has an equal and opposite reaction.',
   [('Newton’s First Law of Motion states that an object ___.', ['Remains at rest or in motion unless acted on by an unbalanced force', 'Always accelerates, even without any force applied', 'A concept unrelated to Newton’s First Law', 'Immediately stops moving once it starts, with no force required'], 0),
    ('Newton’s Second Law of Motion is often summarized by the formula ___.', ['Force equals mass times acceleration', 'Force equals distance divided by time', 'A formula unrelated to Newton’s Second Law', 'Force equals mass divided by acceleration'], 0),
    ('Newton’s Third Law of Motion states that ___.', ['For every action there is an equal and opposite reaction', 'Actions never produce any reaction at all', 'A concept unrelated to Newton’s Third Law', 'Reactions are always stronger than the original action'], 0),
    ('According to Newton’s Second Law, if the same force is applied to a heavier object, the acceleration will be ___.', ['Smaller, since mass and acceleration are inversely related for a given force', 'Larger, since heavier objects always accelerate faster', 'A result unrelated to Newton’s Second Law', 'Exactly the same, regardless of the object’s mass'], 0),
    ('Why is Newton’s Third Law used to explain how a rocket launches into space?', ['The rocket pushes gas downward, and the gas pushes the rocket upward with equal force', 'Rockets launch with no force acting on them at all', 'A reason unrelated to Newton’s laws', 'The rocket’s motion has no connection to any reaction force'], 0)]),
H('The Japanese Canadian Redress Agreement of 1988',
  'Grade 8 History strand: in 1988, the Canadian government formally apologized for the internment and mistreatment of Japanese Canadians during the Second World War and provided financial compensation as part of a redress agreement with the community.',
  [('The Japanese Canadian Redress Agreement was signed in ___.', ['1988', '1945', 'A year unrelated to the Redress Agreement', '1970'], 0),
   ('The Redress Agreement included a formal apology for ___.', ['The internment and mistreatment of Japanese Canadians during the Second World War', 'A conflict that had no connection to Japanese Canadians', 'A subject unrelated to the Redress Agreement', 'Actions taken entirely by a foreign government'], 0),
   ('In addition to an apology, the Redress Agreement provided ___.', ['Financial compensation to affected Japanese Canadians', 'No compensation of any kind', 'A provision unrelated to the Redress Agreement', 'New restrictions on Japanese Canadian communities'], 0),
   ('The Redress Agreement was reached following advocacy from ___.', ['Japanese Canadian community organizations seeking acknowledgment and justice', 'Foreign governments with no connection to Japanese Canadians', 'A group unrelated to the Redress Agreement', 'The organizations that originally supported internment'], 0),
   ('Why is the 1988 Redress Agreement considered an important step in Canadian history?', ['It formally acknowledged a past injustice and worked toward reconciliation with an affected community', 'It denied that any injustice had occurred', 'A reason unrelated to its historical significance', 'It had no connection to the internment of Japanese Canadians'], 0)])]),
day(76, [
L('Vocabulary: Synonyms, Antonyms, and Shades of Meaning',
  'Grade 8 Vocabulary strand: synonyms share similar meanings and antonyms have opposite meanings, but many synonyms carry subtly different shades of meaning that affect tone and precision in writing.',
  [('A synonym is a word that ___.', ['Has a similar meaning to another word', 'Has the exact opposite meaning of another word', 'A concept unrelated to synonyms', 'Sounds identical to another word but means something unrelated'], 0),
   ('An antonym is a word that ___.', ['Has the opposite meaning of another word', 'Has a similar meaning to another word', 'A concept unrelated to antonyms', 'Is always spelled the same as another word'], 0),
   ('Which pair of words are synonyms with slightly different shades of meaning?', ['Skinny and slender', 'Happy and sad', 'A pair unrelated to synonyms', 'Fast and slow'], 0),
   ('Why might a writer choose the word “frugal” instead of “stingy” when describing a careful spender?', ['Frugal carries a more positive shade of meaning than stingy', 'The two words always mean exactly the same thing in every context', 'A reason unrelated to word choice', 'Stingy always sounds more positive than frugal'], 0),
   ('Why is understanding shades of meaning important when choosing precise vocabulary?', ['It allows a writer to convey a more exact tone or attitude', 'Shades of meaning never affect how a word is understood', 'A reason unrelated to vocabulary', 'Every synonym conveys the exact same tone with no difference'], 0)]),
M('Probability: Independent and Dependent Events',
  'Grade 8 Math strand: two events are independent if the outcome of one does not affect the probability of the other, while two events are dependent if the outcome of one event changes the probability of the other occurring.',
  [('Two events are independent if ___.', ['The outcome of one event does not affect the probability of the other', 'The outcome of one event always determines the other completely', 'A concept unrelated to independent events', 'Both events must occur at the exact same time'], 0),
   ('Two events are dependent if ___.', ['The outcome of one event changes the probability of the other occurring', 'The two events have no relationship to each other whatsoever', 'A concept unrelated to dependent events', 'Both events always have an equal, unchanging probability'], 0),
   ('Flipping a coin and then rolling a die are examples of ___.', ['Independent events', 'Dependent events', 'A concept unrelated to probability', 'Events that cannot be assigned any probability'], 0),
   ('Drawing two cards from a deck without replacing the first card is an example of ___.', ['Dependent events, since removing a card changes the probabilities for the second draw', 'Independent events, since each draw has no effect on the other', 'A concept unrelated to probability', 'An event with no measurable probability at all'], 0),
   ('Why is it important to determine whether events are independent or dependent before calculating their combined probability?', ['It determines whether probabilities are multiplied using the same or adjusted values', 'The distinction never affects how a probability calculation is performed', 'A reason unrelated to probability', 'Dependent events always have exactly the same probability as independent events'], 0)]),
Sc('Environmental Science: The Carbon Cycle and the Greenhouse Effect',
   'Grade 8 Science strand: the carbon cycle describes how carbon moves between the atmosphere, oceans, land, and living things, and human activities that release additional carbon dioxide intensify the greenhouse effect, trapping more heat in the atmosphere.',
   [('The carbon cycle describes how carbon moves between ___.', ['The atmosphere, oceans, land, and living things', 'Only the atmosphere, with no other locations involved', 'A concept unrelated to the carbon cycle', 'A single, fixed location that never changes'], 0),
    ('Photosynthesis removes carbon dioxide from the atmosphere by ___.', ['Converting it into oxygen and stored carbon compounds in plants', 'Releasing it directly back into the atmosphere', 'A process unrelated to the carbon cycle', 'Destroying carbon dioxide completely with no byproduct'], 0),
    ('The greenhouse effect refers to ___.', ['Gases in the atmosphere trapping heat that would otherwise escape into space', 'A complete absence of heat in Earth’s atmosphere', 'A concept unrelated to the greenhouse effect', 'The atmosphere reflecting all incoming sunlight away from Earth'], 0),
    ('Which human activity significantly increases the amount of carbon dioxide in the atmosphere?', ['Burning fossil fuels such as coal, oil, and natural gas', 'Planting large numbers of trees across a region', 'An activity unrelated to increasing carbon dioxide', 'Reducing the use of vehicles and factories'], 0),
    ('Why is an intensified greenhouse effect a concern for scientists studying climate?', ['It traps additional heat in the atmosphere, contributing to rising global temperatures', 'An intensified greenhouse effect always cools the planet', 'A reason unrelated to the greenhouse effect', 'The greenhouse effect has no connection to global temperature'], 0)]),
H('The Canada-United States Free Trade Agreement',
  'Grade 8 History strand: the Canada-United States Free Trade Agreement, implemented in 1989, eliminated most tariffs between the two countries, sparking national debate over its economic impact and later expanding into the trilateral North American Free Trade Agreement.',
  [('The Canada-United States Free Trade Agreement was implemented in ___.', ['1989', '1960', 'A year unrelated to the Free Trade Agreement', '1920'], 0),
   ('The Free Trade Agreement primarily aimed to ___.', ['Eliminate most tariffs between Canada and the United States', 'Increase tariffs between Canada and the United States', 'A goal unrelated to the Free Trade Agreement', 'End all trade between Canada and the United States'], 0),
   ('The Free Trade Agreement was a significant topic of debate during the Canadian federal election of ___.', ['1988', '1867', 'A year unrelated to the Free Trade Agreement', '1945'], 0),
   ('The Canada-United States Free Trade Agreement later expanded into a trilateral agreement that included ___.', ['Mexico', 'Britain', 'A country unrelated to this trade agreement', 'Japan'], 0),
   ('Why did the Free Trade Agreement spark significant national debate in Canada?', ['Canadians disagreed over how it would affect jobs, industries, and economic sovereignty', 'The agreement had no effect on the Canadian economy', 'A reason unrelated to the Free Trade Agreement', 'Every Canadian agreed completely on its expected impact'], 0)])]),
day(77, [
L('Writing: The Instructional Guide (Procedural Writing)',
  'Grade 8 Writing strand: procedural writing gives clear, sequential instructions using numbered steps, precise language, and imperative verbs so that a reader can successfully complete a task or process.',
  [('Procedural writing is used to ___.', ['Give clear, sequential instructions for completing a task', 'Persuade a reader to agree with an opinion', 'A concept unrelated to procedural writing', 'Tell an entertaining story with no instructions'], 0),
   ('Which type of verb is commonly used in procedural writing?', ['Imperative verbs, such as mix or press', 'Verbs written only in the past tense', 'A type of verb unrelated to procedural writing', 'Verbs that only describe feelings'], 0),
   ('Why do instructional guides often use numbered steps?', ['They show the reader the exact order in which actions must be completed', 'Numbered steps make instructions harder to follow', 'A reason unrelated to procedural writing', 'Order never matters when completing a task'], 0),
   ('Why is precise language important in an instructional guide?', ['Vague instructions can cause a reader to complete a task incorrectly', 'Precise language never affects how well instructions are understood', 'A reason unrelated to procedural writing', 'Instructions are always understood correctly no matter the wording'], 0),
   ('Which of these is an example of a clear procedural instruction?', ['Preheat the oven to 180 degrees Celsius before baking', 'The oven was interesting to think about', 'A sentence unrelated to procedural writing', 'Ovens can sometimes be found in kitchens'], 0)]),
M('Geometry: Circle Theorems — Tangents and Inscribed Angles',
  'Grade 8 Math strand (pre-high-school extension): a tangent line touches a circle at exactly one point and is perpendicular to the radius at that point, while an inscribed angle is formed by two chords meeting at a point on the circle.',
  [('A tangent line to a circle touches the circle at ___.', ['Exactly one point', 'Two separate points', 'A concept unrelated to tangent lines', 'No points on the circle at all'], 0),
   ('At the point of tangency, a tangent line is always ___.', ['Perpendicular to the radius drawn to that point', 'Parallel to the radius drawn to that point', 'A concept unrelated to tangent lines', 'Passing directly through the centre of the circle'], 0),
   ('An inscribed angle is formed by ___.', ['Two chords meeting at a point on the circle', 'Two radii meeting at the centre of the circle', 'A concept unrelated to inscribed angles', 'A single line segment with no second chord involved'], 0),
   ('An inscribed angle is always equal to ___ the measure of its intercepted central angle.', ['Half', 'Double', 'A fraction unrelated to inscribed angles', 'The same as'], 0),
   ('Why are circle theorems, such as those involving tangents and inscribed angles, useful in fields like engineering and design?', ['They allow precise calculations of angles and distances in circular structures', 'Circle theorems have no practical use outside of a mathematics classroom', 'A reason unrelated to circle theorems', 'Tangents and inscribed angles cannot be measured or calculated'], 0)]),
Sc('Space Science: The Phases of the Moon and Eclipses',
   'Grade 8 Science strand: the Moon’s phases occur as it orbits Earth and different portions of its sunlit side become visible, while a solar eclipse occurs when the Moon passes between the Sun and Earth, and a lunar eclipse occurs when Earth passes between the Sun and Moon.',
   [('The phases of the Moon occur because ___.', ['Different portions of the Moon’s sunlit side are visible from Earth as it orbits', 'The Moon actually changes shape during its orbit', 'A concept unrelated to the phases of the Moon', 'The Moon produces its own light that changes in intensity'], 0),
    ('A solar eclipse occurs when ___.', ['The Moon passes between the Sun and Earth, blocking sunlight', 'Earth passes between the Sun and the Moon', 'A concept unrelated to solar eclipses', 'The Moon is at its farthest point from Earth'], 0),
    ('A lunar eclipse occurs when ___.', ['Earth passes between the Sun and the Moon, casting a shadow on the Moon', 'The Moon passes directly between the Sun and Earth', 'A concept unrelated to lunar eclipses', 'The Sun passes between Earth and the Moon'], 0),
    ('A full moon occurs when ___.', ['The entire sunlit side of the Moon faces Earth', 'None of the sunlit side of the Moon faces Earth', 'A concept unrelated to the phases of the Moon', 'The Moon is positioned directly between the Sun and Earth'], 0),
    ('Why do eclipses not occur every single month, even though the Moon orbits Earth monthly?', ['The Moon’s orbit is slightly tilted relative to Earth’s orbit around the Sun, so perfect alignment is rare', 'Eclipses actually occur every month without exception', 'A reason unrelated to eclipses', 'The Moon’s orbit has no tilt at all relative to Earth’s orbit'], 0)]),
H('The Atlantic Cod Moratorium of 1992',
  'Grade 8 History strand: in 1992, the Canadian government declared a moratorium on cod fishing off the coast of Newfoundland after decades of overfishing caused the collapse of cod stocks, resulting in the loss of tens of thousands of jobs in Atlantic Canada.',
  [('The Atlantic cod moratorium was declared in ___.', ['1992', '1960', 'A year unrelated to the cod moratorium', '2010'], 0),
   ('The cod moratorium was declared primarily because of ___.', ['The collapse of cod stocks caused by decades of overfishing', 'A sudden increase in the cod population that needed to be managed', 'A cause unrelated to the cod moratorium', 'A new law banning all fishing of every species'], 0),
   ('The cod moratorium had a major economic impact on ___.', ['Communities in Atlantic Canada, especially Newfoundland', 'Communities in the Canadian prairies', 'A region unrelated to the cod moratorium', 'Communities along the Pacific coast exclusively'], 0),
   ('As a direct result of the cod moratorium, tens of thousands of workers ___.', ['Lost their jobs in the fishing industry', 'Received significant pay increases in the fishing industry', 'A result unrelated to the cod moratorium', 'Were relocated permanently outside of Canada'], 0),
   ('Why is the cod moratorium often cited as a lesson in resource management?', ['It demonstrated the consequences of overfishing a resource without sustainable limits', 'It showed that overfishing never has any lasting effect on a resource', 'A reason unrelated to its historical significance', 'It proved that fish populations always recover immediately regardless of fishing practices'], 0)])]),
day(78, [
L('Reading: Direct and Indirect Characterization',
  'Grade 8 Reading strand: direct characterization occurs when an author explicitly states a character’s traits, while indirect characterization reveals traits through a character’s actions, dialogue, thoughts, and how other characters respond to them.',
  [('Direct characterization occurs when an author ___.', ['Explicitly states a character’s traits', 'Only reveals traits through a character’s actions', 'A concept unrelated to direct characterization', 'Never describes a character in any way'], 0),
   ('Indirect characterization reveals traits through ___.', ['A character’s actions, dialogue, and thoughts', 'A direct statement naming the trait explicitly', 'A concept unrelated to indirect characterization', 'The book’s cover illustration alone'], 0),
   ('Which sentence is an example of direct characterization?', ['Maria was a kind and patient person.', 'Maria smiled and helped the lost child find her way home.', 'A sentence unrelated to characterization', 'Maria walked quickly down the street.'], 0),
   ('Which sentence is an example of indirect characterization?', ['Jordan slammed the door and refused to speak to anyone.', 'Jordan was an angry and stubborn person.', 'A sentence unrelated to characterization', 'Jordan was described as difficult by the narrator.'], 0),
   ('Why might an author prefer indirect characterization over stating traits directly?', ['It allows readers to draw their own conclusions and become more engaged with the character', 'Indirect characterization always confuses readers with no benefit', 'A reason unrelated to characterization', 'Direct statements are always more engaging than showing traits through action'], 0)]),
M('Patterning: Recursive and Explicit Formulas for Sequences',
  'Grade 8 Math strand: a recursive formula defines each term in a sequence based on the previous term, while an explicit formula calculates any term directly using its position number in the sequence.',
  [('A recursive formula defines each term in a sequence based on ___.', ['The previous term in the sequence', 'Only the position number of the term', 'A concept unrelated to recursive formulas', 'A completely random value each time'], 0),
   ('An explicit formula allows a term to be calculated ___.', ['Directly using its position number, without knowing previous terms', 'Only by first calculating every previous term in the sequence', 'A concept unrelated to explicit formulas', 'By guessing randomly with no formula involved'], 0),
   ('For the sequence 3, 7, 11, 15, the recursive rule is ___.', ['Add 4 to the previous term', 'Multiply the previous term by 4', 'A rule unrelated to the sequence', 'Subtract 4 from the previous term'], 0),
   ('For the arithmetic sequence with first term 3 and common difference 4, the explicit formula for the nth term is ___.', ['3 + 4(n - 1)', '3 x 4n', 'A formula unrelated to the sequence', '4 + 3(n - 1)'], 0),
   ('Why might an explicit formula be more useful than a recursive formula when finding the 100th term of a sequence?', ['It calculates the term directly without needing to find all 99 previous terms', 'A recursive formula is always faster for finding distant terms', 'A reason unrelated to patterning', 'Explicit and recursive formulas always require the exact same amount of work'], 0)]),
Sc('Technology: 3D Printing and Additive Manufacturing',
   'Grade 8 Science strand: 3D printing, or additive manufacturing, builds objects layer by layer from a digital design, contrasting with traditional subtractive manufacturing, which removes material from a larger block to create a shape.',
   [('3D printing is also known as ___.', ['Additive manufacturing', 'Subtractive manufacturing', 'A concept unrelated to 3D printing', 'Traditional casting'], 0),
    ('Additive manufacturing builds objects by ___.', ['Adding material layer by layer based on a digital design', 'Removing material from a larger solid block', 'A concept unrelated to additive manufacturing', 'Melting an entire object into a single new shape at once'], 0),
    ('Subtractive manufacturing differs from 3D printing because it ___.', ['Removes material from a larger block to create a shape', 'Adds material layer by layer to create a shape', 'A concept unrelated to subtractive manufacturing', 'Uses no material of any kind'], 0),
    ('Which of these is a common advantage of 3D printing over traditional manufacturing?', ['It can create complex, customized shapes with relatively little material waste', 'It always produces more material waste than traditional methods', 'An advantage unrelated to 3D printing', '3D printing can never create a customized design'], 0),
    ('Why might 3D printing be useful in fields such as medicine, for creating custom prosthetics?', ['It allows objects to be precisely customized to an individual’s specific measurements', '3D printed objects can never be customized to an individual', 'A reason unrelated to 3D printing', 'Prosthetics can only be made using subtractive manufacturing'], 0)]),
H('The Creation of Nunavut',
  'Grade 8 History strand: in 1999, the territory of Nunavut was created out of the eastern portion of the Northwest Territories, establishing a homeland with Inuit self-government following decades of negotiation between Inuit leaders and the Canadian government.',
  [('The territory of Nunavut was officially created in ___.', ['1999', '1931', 'A year unrelated to the creation of Nunavut', '1867'], 0),
   ('Nunavut was created out of the eastern portion of ___.', ['The Northwest Territories', 'Quebec', 'A region unrelated to the creation of Nunavut', 'British Columbia'], 0),
   ('The creation of Nunavut established a homeland with significant self-government for ___.', ['The Inuit', 'The Métis', 'A group unrelated to the creation of Nunavut', 'European settlers exclusively'], 0),
   ('The creation of Nunavut followed decades of ___.', ['Negotiation between Inuit leaders and the Canadian government', 'A single, immediate decision made without any negotiation', 'A process unrelated to the creation of Nunavut', 'Conflict between Nunavut and the Northwest Territories over unrelated issues'], 0),
   ('Why is the creation of Nunavut considered a significant milestone in Indigenous self-governance in Canada?', ['It gave the Inuit greater control over their own land and government after years of advocacy', 'It removed all self-governance previously held by the Inuit', 'A reason unrelated to its historical significance', 'It had no connection to Inuit land or governance'], 0)])]),
day(79, [
L('Grammar: Sentence Fragments and Run-on Sentences',
  'Grade 8 Grammar strand: a sentence fragment is an incomplete sentence missing a subject, verb, or complete thought, while a run-on sentence incorrectly joins two or more complete sentences without proper punctuation or conjunctions.',
  [('A sentence fragment is an incomplete sentence that is missing ___.', ['A subject, verb, or complete thought', 'Only a title at the beginning', 'A concept unrelated to sentence fragments', 'A specific number of words'], 0),
   ('A run-on sentence occurs when ___.', ['Two or more complete sentences are joined without proper punctuation', 'A sentence contains only a single short word', 'A concept unrelated to run-on sentences', 'A sentence uses too many commas correctly'], 0),
   ('Which of these is a sentence fragment?', ['Running through the park every morning.', 'She runs through the park every morning.', 'A sentence unrelated to fragments', 'The dog barked loudly at the mail carrier.'], 0),
   ('Which of these correctly fixes a run-on sentence?', ['I finished my homework, and then I watched a movie.', 'I finished my homework I watched a movie.', 'A correction unrelated to run-on sentences', 'I finished my homework then I watched a movie no comma at all.'], 0),
   ('Why is it important to avoid sentence fragments and run-ons in formal writing?', ['They can confuse readers and make ideas harder to follow clearly', 'Fragments and run-ons always make writing clearer', 'A reason unrelated to grammar', 'Formal writing never requires complete, properly punctuated sentences'], 0)]),
M('Statistics: Line of Best Fit — Interpolation and Extrapolation',
  'Grade 8 Math strand: a line of best fit approximates the trend in a scatter plot, and it can be used for interpolation, estimating values within the range of the data, or extrapolation, estimating values beyond the range of the data.',
  [('A line of best fit is used to ___.', ['Approximate the overall trend shown in a scatter plot', 'Connect every single data point exactly with no approximation', 'A concept unrelated to lines of best fit', 'Remove all the data points from a scatter plot'], 0),
   ('Interpolation refers to estimating a value ___.', ['Within the range of the existing data', 'Far beyond the range of the existing data', 'A concept unrelated to interpolation', 'With no connection to any data at all'], 0),
   ('Extrapolation refers to estimating a value ___.', ['Beyond the range of the existing data', 'Only within the exact range of the existing data', 'A concept unrelated to extrapolation', 'That already appears directly in the data set'], 0),
   ('Which is generally considered less reliable, interpolation or extrapolation?', ['Extrapolation, since it assumes the trend continues beyond the known data', 'Interpolation, since it always ignores the known data points', 'A comparison unrelated to lines of best fit', 'Both are always equally reliable in every situation'], 0),
   ('Why is a line of best fit useful when analyzing a scatter plot of real-world data?', ['It helps identify trends and make predictions based on the overall pattern in the data', 'A line of best fit provides no useful information about a data set', 'A reason unrelated to statistics', 'Scatter plots never show any pattern that a line could approximate'], 0)]),
Sc('Health Science: The Nervous System and Reflex Actions',
   'Grade 8 Science strand: the nervous system transmits electrical signals between the brain, spinal cord, and body through neurons, and a reflex action is a rapid, automatic response to a stimulus that bypasses conscious thought in the brain.',
   [('The nervous system transmits signals through specialized cells called ___.', ['Neurons', 'Red blood cells', 'A type of cell unrelated to the nervous system', 'Muscle fibres'], 0),
    ('The two main components of the central nervous system are the ___.', ['Brain and spinal cord', 'Heart and lungs', 'A pair of organs unrelated to the nervous system', 'Stomach and liver'], 0),
    ('A reflex action is best described as ___.', ['A rapid, automatic response to a stimulus that bypasses conscious thought', 'A slow, carefully considered decision made by the brain', 'A concept unrelated to reflex actions', 'An action that never involves the nervous system at all'], 0),
    ('Pulling your hand away quickly after touching something hot is an example of ___.', ['A reflex action controlled by the spinal cord', 'A carefully planned decision made by the brain', 'A concept unrelated to reflex actions', 'An action with no connection to the nervous system'], 0),
    ('Why are reflex actions important for protecting the body from harm?', ['They allow a rapid response to danger before the brain fully processes the situation', 'Reflex actions always occur too slowly to provide any protection', 'A reason unrelated to reflex actions', 'The nervous system has no role in protecting the body'], 0)]),
H('Canada’s Role in NATO and NORAD',
  'Grade 8 History strand: Canada became a founding member of NATO in 1949 and later joined NORAD in 1958, two Cold War-era defence partnerships with the United States and other allied nations aimed at collective security and continental air defence.',
  [('Canada became a founding member of NATO in ___.', ['1949', '1918', 'A year unrelated to NATO', '1982'], 0),
   ('NATO was formed primarily to ___.', ['Provide collective security among member nations during the Cold War', 'End all military alliances between Western nations', 'A purpose unrelated to NATO', 'Focus exclusively on trade agreements'], 0),
   ('Canada joined NORAD, a joint continental air defence system, in ___.', ['1958', '1867', 'A year unrelated to NORAD', '2001'], 0),
   ('NORAD was established as a partnership between Canada and ___.', ['The United States', 'Britain', 'A country unrelated to NORAD', 'The Soviet Union'], 0),
   ('Why were NATO and NORAD significant for Canada’s role during the Cold War?', ['They demonstrated Canada’s commitment to collective defence alongside its allies', 'They had no connection to Canada’s foreign or defence policy', 'A reason unrelated to their historical significance', 'They ended Canada’s military cooperation with other nations entirely'], 0)])]),
day(80, [
L('Review: Days 71-79 Language Arts',
  'Grade 8 Language strand: this review lesson revisits mood and tone, formal business letters, verbals, fact-checking, unreliable narrators, shades of meaning, procedural writing, characterization, and sentence fragments/run-ons from recent lessons.',
  [('Mood in a text is best described as ___.', ['The emotional atmosphere a reader feels while reading', 'The exact number of characters in a story', 'A concept unrelated to mood', 'The physical setting where a story takes place'], 0),
   ('Fact-checking involves ___.', ['Verifying claims against reliable, independent sources', 'Accepting every claim without question', 'A concept unrelated to fact-checking', 'Sharing information immediately with no review'], 0),
   ('An unreliable narrator is a storyteller whose ___.', ['Credibility is compromised, requiring readers to question their account', 'Account is always completely accurate and trustworthy', 'A concept unrelated to unreliable narrators', 'Perspective is identical to every other character in the story'], 0),
   ('Indirect characterization reveals traits through ___.', ['A character’s actions, dialogue, and thoughts', 'A direct statement naming the trait explicitly', 'A concept unrelated to indirect characterization', 'The book’s cover illustration alone'], 0),
   ('Why is it useful to review reading, writing, grammar, and media literacy skills together?', ['It reinforces how these language and literacy skills connect and support one another', 'These topics have no connection to one another', 'A reason unrelated to reviewing language arts', 'Review never helps strengthen understanding of language skills'], 0)]),
M('Review: Days 71-79 Math Concepts',
  'Grade 8 Math strand review: this lesson revisits prime factorization and the GCF/LCM, solving systems of equations by graphing, composite figures, two-way tables, percent change, independent and dependent events, circle theorems, recursive and explicit formulas, and lines of best fit from recent lessons.',
  [('The greatest common factor (GCF) of 18 and 24 is ___.', ['6', '3', 'A value unrelated to the calculation', '9'], 0),
   ('The point of intersection of two graphed lines represents ___.', ['The solution that satisfies both equations', 'A point that satisfies neither equation', 'A concept unrelated to systems of equations', 'The y-intercept of only one equation'], 0),
   ('Two events are independent if ___.', ['The outcome of one event does not affect the probability of the other', 'The outcome of one event always determines the other completely', 'A concept unrelated to independent events', 'Both events must occur at the exact same time'], 0),
   ('An explicit formula allows a term to be calculated ___.', ['Directly using its position number, without knowing previous terms', 'Only by first calculating every previous term in the sequence', 'A concept unrelated to explicit formulas', 'By guessing randomly with no formula involved'], 0),
   ('Why is it useful to review number theory, algebra, geometry, data management, and probability together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other in mathematics', 'A reason unrelated to reviewing math', 'Review is never useful in math'], 0)]),
Sc('Review: Days 71-79 Science Concepts',
   'Grade 8 Science strand review: this lesson revisits structures and mechanisms, elements/compounds/mixtures, Earth’s internal layers, genetic mutations, Newton’s laws of motion, the carbon cycle, phases of the Moon, 3D printing, and the nervous system from recent lessons.',
   [('Compression is a type of stress that occurs when a structure is ___.', ['Squeezed or pushed together', 'Stretched or pulled apart', 'A concept unrelated to compression', 'Twisted around its centre'], 0),
    ('A compound is formed when ___.', ['Two or more elements are chemically combined in a fixed ratio', 'A single element exists on its own', 'A concept unrelated to compounds', 'Substances are physically mixed with no chemical bonding'], 0),
    ('Newton’s Second Law of Motion is often summarized by the formula ___.', ['Force equals mass times acceleration', 'Force equals distance divided by time', 'A formula unrelated to Newton’s Second Law', 'Force equals mass divided by acceleration'], 0),
    ('A reflex action is best described as ___.', ['A rapid, automatic response to a stimulus that bypasses conscious thought', 'A slow, carefully considered decision made by the brain', 'A concept unrelated to reflex actions', 'An action that never involves the nervous system at all'], 0),
    ('Why is it useful to review physics, chemistry, earth science, and life science topics together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing science', 'Each topic must be studied with no connection to the others'], 0)]),
H('Review: Days 71-79 Canadian History',
  'Grade 8 History strand review: this lesson revisits the Klondike Gold Rush, the Boer War, the Quiet Revolution, the 1967 immigration points system, the Japanese Canadian Redress Agreement, the Free Trade Agreement, the cod moratorium, the creation of Nunavut, and Canada’s role in NATO and NORAD from recent lessons.',
  [('The Klondike Gold Rush began after gold was discovered near ___.', ['Dawson City', 'Toronto', 'A location unrelated to the Klondike Gold Rush', 'Halifax'], 0),
   ('The Quiet Revolution took place primarily during the ___.', ['1960s', '1930s', 'A time period unrelated to the Quiet Revolution', '1990s'], 0),
   ('The points system evaluated immigration applicants based primarily on ___.', ['Factors such as education and skills', 'Race and country of origin', 'A factor unrelated to the points system', 'Religious affiliation alone'], 0),
   ('The creation of Nunavut established a homeland with significant self-government for ___.', ['The Inuit', 'The Métis', 'A group unrelated to the creation of Nunavut', 'European settlers exclusively'], 0),
   ('Why is it useful to review these events in Canadian history together?', ['It reinforces how these events shaped Canadian identity, governance, and international relationships over time', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history and policy'], 0)])]),
]


def _rebalance_answer_positions(days, seed=20260906):
    """Same technique used for the earlier Grade 8 batches -- reassigns
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
    _rebalance_answer_positions(g8_71_80)
    append_to(8, g8_71_80)
