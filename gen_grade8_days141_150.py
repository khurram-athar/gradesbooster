#!/usr/bin/env python3
"""Grade 8, Days 141-150 -- extends Grade 8 from 140 to 150 days. Topics
chosen after dumping the existing Day 1-140 title list (data/grade8.json)
in full to avoid any overlap: verb tense consistency, homophones and
commonly confused words, analyzing multiple points of view, the personal
essay, media framing and word choice, absolute phrases, eponyms,
analyzing nonlinear narrative structures, and the investigative report;
the Fundamental Theorem of Calculus, Fermats Little Theorem, the Poisson
distribution, Gaussian elimination, hyperbolic geometry, sum and
difference identities, continued fractions, regression analysis and
residuals, and eigenvalues and eigenvectors; ionic and covalent bonding,
pendulums and simple harmonic motion, glaciers and glacial landforms,
rocket propulsion, photosynthesis, the chemistry of combustion, plant
reproduction and pollination, hydroelectric power, and soil formation
and erosion; the 1911 reciprocity election, Ontario Regulation 17, the
Grand Trunk Pacific Railway, the Ontario Temperance Act, Nellie McClung,
the Canadian Wheat Board, the Bank Act, the Yukon Act of 1898, and
Canadian citizenship before 1947. Day 150 is a cross-subject review day
drawing on Days 141-149.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days131_140.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-history'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science and Technology',
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


g8_141_150 = [
day(141, [
L('Grammar: Verb Tense Consistency and Avoiding Tense Shifts',
  'Grade 8 Language strand: verb tense consistency requires that a writer maintain the same tense throughout a passage unless a genuine change in time occurs, since unnecessary shifts between past and present tense can confuse a reader about when events are taking place.',
  [('What does verb tense consistency require?', ['That a writer maintain the same tense throughout a passage unless time genuinely changes', 'That every sentence use a different tense', 'That a sentence never contain a verb', 'That verbs always appear in the future tense'], 0),
   ('Which sentence contains an unnecessary shift in verb tense?', ['She walked to the store and buys some milk.', 'She walked to the store and bought some milk.', 'She walks to the store and buys some milk.', 'She will walk to the store and will buy some milk.'], 0),
   ('Why can unnecessary tense shifts confuse a reader?', ['They make it unclear when events in a narrative are taking place', 'They always make a sentence easier to follow', 'Tense has no connection to when an event occurs', 'Readers never notice a shift in verb tense'], 0),
   ('When is switching tense within a passage appropriate?', ['When describing an event that genuinely happens at a different time than the surrounding text', 'Tense should never change under any circumstance', 'Switching tense is always considered an error', 'Only when a sentence contains no verb at all'], 0),
   ('Why is consistent verb tense particularly important in narrative writing?', ['It helps readers follow the sequence of events clearly without confusion', 'Consistent tense has no effect on narrative clarity', 'Narratives are not written using verbs', 'Readers prefer narratives with constantly changing tense'], 0)]),
M('Calculus Preview: The Fundamental Theorem of Calculus',
  'Grade 8 Math strand: the Fundamental Theorem of Calculus connects differentiation and integration by showing that a definite integral of a function can be evaluated using an antiderivative of that function, revealing that the two operations are inverse processes.',
  [('What does the Fundamental Theorem of Calculus connect?', ['Differentiation and integration, showing they are inverse processes', 'Addition and subtraction of whole numbers', 'The area of a circle and its circumference', 'Two entirely unrelated branches of mathematics'], 0),
   ('According to the theorem, how can a definite integral of a function often be evaluated?', ['By finding an antiderivative of the function and evaluating it at the intervals endpoints', 'By measuring the function with a ruler', 'By counting the number of terms in the function', 'Definite integrals can never be evaluated using an antiderivative'], 0),
   ('Why is the Fundamental Theorem of Calculus considered a major result in mathematics?', ['It links area under a curve and rate of change into a single unified framework', 'It has no connection between any two mathematical ideas', 'It proves that calculus cannot be used to solve real problems', 'It shows that integration and differentiation are entirely unrelated'], 0),
   ('If F is an antiderivative of f, what does the theorem say about the definite integral of f from a to b?', ['It equals F(b) minus F(a)', 'It always equals zero regardless of a and b', 'It equals F(a) multiplied by F(b)', 'It cannot be calculated using F at all'], 0),
   ('Why is this theorem useful for solving real-world problems, such as finding total distance from a velocity function?', ['It allows a quantity built up over time to be calculated directly from a single antiderivative', 'It requires adding infinitely many small pieces by hand with no shortcut', 'Velocity functions can never be integrated', 'It only applies to problems with no connection to motion'], 0)]),
Sc('Chemistry: Ionic and Covalent Bonding',
   'Grade 8 Science strand: chemical bonds form as atoms interact to reach a more stable arrangement of electrons, with ionic bonds forming when electrons transfer between atoms to create attracting charged ions, and covalent bonds forming when atoms share pairs of electrons.',
   [('What happens during the formation of an ionic bond?', ['Electrons transfer from one atom to another, creating oppositely charged ions that attract each other', 'Two atoms share a pair of electrons equally', 'No electrons are involved in the bond at all', 'Atoms repel each other permanently'], 0),
    ('What happens during the formation of a covalent bond?', ['Atoms share one or more pairs of electrons', 'Electrons are permanently transferred from one atom to another', 'Atoms exchange entire nuclei', 'No interaction between electrons occurs'], 0),
    ('Which type of bond typically forms between a metal and a nonmetal?', ['An ionic bond', 'A covalent bond', 'No bond ever forms between a metal and a nonmetal', 'A purely physical bond with no chemical interaction'], 0),
    ('Which type of bond typically forms between two nonmetal atoms?', ['A covalent bond', 'An ionic bond', 'A metallic bond', 'No stable bond can form between two nonmetals'], 0),
    ('Why do atoms form chemical bonds in the first place?', ['To achieve a more stable arrangement of electrons, often resembling a full outer shell', 'Atoms never form bonds under any circumstances', 'Bonding always makes an atom less stable', 'To eliminate all electrons from their outer shell'], 0)]),
H('Sir Wilfrid Lauriers Reciprocity Election of 1911',
  'Grade 8 History strand: in the 1911 federal election, Sir Wilfrid Lauriers Liberal government campaigned on a reciprocity, or free trade, agreement with the United States, but concerns about weakened ties to Britain helped defeat Laurier, ending his fifteen-year tenure as prime minister.',
  [('What trade policy did Lauriers government campaign on in the 1911 election?', ['A reciprocity, or free trade, agreement with the United States', 'A complete ban on all trade with the United States', 'A new trade agreement with France', 'A plan to eliminate all provincial taxes'], 0),
   ('What was one major concern opponents raised about reciprocity?', ['That it might weaken Canadas economic and political ties with Britain', 'That it would immediately end all Canadian exports', 'That it had no connection to trade with the United States', 'That it would eliminate the office of prime minister'], 0),
   ('What was the outcome of the 1911 election for Laurier?', ['His Liberal government was defeated, ending his time as prime minister', 'Laurier won by the largest margin in Canadian history', 'The election was postponed indefinitely', 'Laurier remained prime minister for another twenty years'], 0),
   ('Which party benefited from the defeat of Lauriers government in 1911?', ['The Conservative Party, led by Robert Borden', 'The Liberal Party gained even more seats', 'A newly formed party with no prior history', 'No party won any seats in the 1911 election'], 0),
   ('Why is the 1911 reciprocity election considered significant in Canadian history?', ['It shows how debates over trade with the United States and loyalty to Britain shaped early twentieth-century politics', 'It had no lasting effect on Canadian politics', 'It marked the only election Canada has ever held', 'It ended all future trade discussions between Canada and other countries'], 0)]),
]),
day(142, [
L('Vocabulary: Homophones and Commonly Confused Words',
  'Grade 8 Language strand: a homophone is a word that sounds like another word but differs in spelling and meaning, such as their and there, and confusing homophones during writing can change or obscure the meaning a writer intends to convey.',
  [('What is a homophone?', ['A word that sounds like another word but differs in spelling and meaning', 'A word that means the exact same thing as another word', 'A citation style used in research papers', 'A punctuation mark used to end a sentence'], 0),
   ('Which pair of words are homophones?', ['Their and there', 'Happy and sad', 'Run and walk', 'Big and small'], 0),
   ('Why can confusing homophones weaken a piece of writing?', ['Using the wrong spelling can change or confuse the intended meaning of a sentence', 'Homophones never affect the meaning of a sentence', 'Confusing homophones always improves clarity', 'Homophones do not exist in the English language'], 0),
   ('Which sentence correctly uses the homophone there?', ['The books are over there on the shelf.', 'Books are they are on the shelf.', 'The books are over they are shelf.', 'The books are over their on the shelf, referring to the shelf itself.'], 0),
   ('Why is proofreading for homophones an important editing step?', ['Spell-check programs often fail to catch homophone errors since the words are spelled correctly, just used incorrectly', 'Spell-check programs always catch every homophone error automatically', 'Homophones are never a source of writing errors', 'Proofreading has no connection to word choice'], 0)]),
M('Number Theory: An Introduction to Fermats Little Theorem',
  'Grade 8 Math strand: Fermats Little Theorem states that if p is a prime number, then for any integer a not divisible by p, a raised to the power of p minus 1 is congruent to 1 modulo p, a result widely used in cryptography and primality testing.',
  [('What does Fermats Little Theorem describe a relationship between?', ['A prime number, an integer not divisible by it, and modular arithmetic', 'Two unrelated even numbers', 'The area of a triangle and its perimeter', 'A fraction and its reciprocal only'], 0),
   ('According to Fermats Little Theorem, if p is prime and a is not divisible by p, what is a raised to the power of p minus 1 congruent to modulo p?', ['1', '0', 'p', 'a'], 0),
   ('In which modern field is Fermats Little Theorem particularly useful?', ['Cryptography and primality testing', 'Only in ancient farming calculations', 'Only in musical composition', 'Only in weather forecasting'], 0),
   ('Why must the integer a not be divisible by the prime p for the theorem to apply?', ['The theorem specifically describes integers that share no common factor with the prime', 'The theorem only applies when a is negative', 'Divisibility has no connection to the theorem', 'The theorem requires a to always equal p'], 0),
   ('Why is Fermats Little Theorem considered an important result in number theory?', ['It reveals a predictable pattern in modular exponentiation involving prime numbers', 'It has no practical or theoretical significance', 'It disproves the existence of prime numbers', 'It only applies to numbers less than ten'], 0)]),
Sc('Physics: Pendulums and Simple Harmonic Motion',
   'Grade 8 Science strand: a pendulum swings back and forth in a repeating pattern known as simple harmonic motion, with the period of a simple pendulum depending mainly on its length and the strength of gravity rather than on the mass of the bob.',
   [('What is the repeating back-and-forth motion of a pendulum an example of?', ['Simple harmonic motion', 'Random, unpredictable motion', 'Motion with no repeating pattern', 'Motion caused only by friction'], 0),
    ('What factor primarily determines the period of a simple pendulum?', ['The length of the pendulum and the strength of gravity', 'The colour of the pendulum bob', 'The material used to make the string only', 'The time of day the pendulum is observed'], 0),
    ('For small swings, how does the mass of the pendulum bob affect its period?', ['It has little to no effect on the period', 'A heavier bob always doubles the period', 'A heavier bob always halves the period', 'Mass is the only factor that determines the period'], 0),
    ('What happens to a pendulums period if its length is increased?', ['The period increases', 'The period always decreases', 'The period stays exactly the same regardless of length', 'The pendulum stops swinging entirely'], 0),
    ('Why do scientists and engineers study pendulum motion?', ['Understanding predictable periodic motion helps in designing clocks and studying other oscillating systems', 'Pendulum motion has no practical applications', 'Pendulums cannot be used to measure time', 'Studying pendulums has no connection to oscillating systems'], 0)]),
H('The Ontario Regulation 17 and the Fight for Franco-Ontarian Education',
  'Grade 8 History strand: Regulation 17, introduced by the Ontario government in 1912, restricted the use of French as a language of instruction in Ontario schools, provoking strong protest from Franco-Ontarian communities and becoming a lasting symbol of language rights struggles in Canada.',
  [('What did Ontarios Regulation 17, introduced in 1912, restrict?', ['The use of French as a language of instruction in Ontario schools', 'The use of English in Ontario government offices', 'The number of students allowed in a classroom', 'The construction of new schools in rural Ontario'], 0),
   ('How did Franco-Ontarian communities respond to Regulation 17?', ['With strong protest and resistance against the restriction', 'With immediate and complete acceptance of the new policy', 'By ending all French-language education voluntarily', 'They had no reaction to the regulation at all'], 0),
   ('What broader issue does Regulation 17 illustrate in Canadian history?', ['Ongoing tensions over French-language and minority education rights', 'A total absence of language-related conflict in Canadian history', 'A dispute over provincial tax rates', 'A disagreement about national holidays'], 0),
   ('Why is Regulation 17 still studied today?', ['It remains a significant symbol of the struggle for French-language rights outside Quebec', 'It has no continuing relevance to Canadian history', 'It was quickly forgotten and had no lasting impact', 'It only affected schools outside of Canada'], 0),
   ('Why might a provincial government restricting a minority language in schools create lasting political tension?', ['It can be seen as threatening a communitys cultural identity and access to education in their own language', 'Restricting a language in schools never creates any tension', 'Language policy has no connection to cultural identity', 'Minority communities are always unaffected by education policy'], 0)]),
]),
day(143, [
L('Reading: Analyzing Multiple Points of View in a Narrative',
  'Grade 8 Language strand: a narrative told through more than one characters point of view allows readers to compare differing perceptions, biases, and knowledge, deepening understanding of characters and revealing gaps between what different characters know or believe.',
  [('What can a narrative with multiple points of view allow readers to do?', ['Compare differing characters perceptions, biases, and knowledge of events', 'Understand only a single characters thoughts with no comparison', 'Avoid learning anything about the characters at all', 'Read the story in a completely random order every time'], 0),
   ('Why might an author choose to tell a story from more than one characters perspective?', ['To reveal information or bias that a single narrator might not be able to show alone', 'Multiple perspectives always make a story less interesting', 'A single narrator always reveals every possible detail', 'Authors are required to use only one point of view'], 0),
   ('What might a reader notice when comparing two characters accounts of the same event?', ['Differences in what each character knows, believes, or chooses to share', 'That both characters always describe the event identically', 'That point of view has no effect on how an event is described', 'That only one character is ever telling the truth'], 0),
   ('Which text structure would most likely use multiple points of view?', ['A novel with alternating chapters narrated by different characters', 'A dictionary entry defining a single word', 'A recipe listing cooking instructions', 'A single-page advertisement'], 0),
   ('Why is analyzing multiple points of view a valuable reading skill?', ['It helps readers recognize that a single perspective may not tell the whole story', 'This skill has no connection to understanding a text', 'Multiple points of view are never used in literature', 'It prevents readers from understanding any character at all'], 0)]),
M('Statistics: An Introduction to the Poisson Distribution',
  'Grade 8 Math strand: the Poisson distribution models the probability of a given number of events occurring in a fixed interval of time or space, given a known average rate, and is well suited to rare, independent events such as the number of calls a call centre receives in an hour.',
  [('What does the Poisson distribution model?', ['The probability of a given number of events occurring in a fixed interval, given a known average rate', 'The exact height of every value in a data set', 'The area under a triangle', 'A guarantee that an event will never occur'], 0),
   ('What kind of events is the Poisson distribution well suited to model?', ['Rare, independent events occurring at a known average rate', 'Events that always occur at exactly the same time', 'Events that are entirely dependent on one another', 'Events with no defined average rate'], 0),
   ('Which of these is an example of a situation the Poisson distribution might model?', ['The number of phone calls a call centre receives in an hour', 'The exact height of a single building', 'The colour of a randomly chosen car', 'The alphabetical order of a list of names'], 0),
   ('What key piece of information is needed to define a Poisson distribution?', ['The average rate at which events occur over the given interval', 'The exact outcome of every future event', 'The total population of a country', 'The colour associated with each event'], 0),
   ('Why is the Poisson distribution useful in fields like traffic engineering or biology?', ['It provides a way to estimate the likelihood of rare, countable events happening within a set period', 'It eliminates the need to collect any data', 'It can only be used to describe events that never happen', 'It has no real-world statistical applications'], 0)]),
Sc('Earth Science: Glaciers and Glacial Landforms',
   'Grade 8 Science strand: glaciers are large, slow-moving masses of ice formed from compacted snow, and as they advance and retreat they reshape the landscape, carving valleys and depositing sediment to create landforms such as moraines and fjords.',
   [('How do glaciers typically form?', ['From snow that becomes compacted into ice over long periods of time', 'From liquid water freezing instantly in a single day', 'From volcanic rock cooling rapidly', 'Glaciers do not form from snow or ice'], 0),
    ('What happens to the landscape as a glacier advances and retreats?', ['The glacier carves and reshapes the land, creating distinct landforms', 'The landscape remains completely unaffected by glacial movement', 'Glaciers only affect the ocean floor', 'Glacial movement destroys all landforms with no new ones created'], 0),
    ('What is a moraine?', ['A ridge of sediment deposited by a glacier', 'A type of volcanic rock', 'A body of water found only in deserts', 'A form of glacial ice that never moves'], 0),
    ('What is a fjord?', ['A deep, narrow coastal valley carved by glacial activity and later flooded by the sea', 'A shallow desert canyon with no connection to ice', 'A type of freshwater lake found only in the tropics', 'A landform created entirely by wind erosion'], 0),
    ('Why do scientists study glaciers when researching climate change?', ['Changes in glacier size can reveal information about long-term shifts in global temperature and precipitation', 'Glaciers have no connection to climate patterns', 'Glacier size never changes over time', 'Studying glaciers provides no scientific information'], 0)]),
H('The Grand Trunk Pacific Railway and Canadas Second Transcontinental Line',
  'Grade 8 History strand: in the early 1900s the Grand Trunk Pacific Railway was built as a second transcontinental line intended to open new areas of the Canadian west and north to settlement and trade, though it faced serious financial struggles and was eventually absorbed into the Canadian National Railway.',
  [('What was the Grand Trunk Pacific Railway intended to be?', ['A second transcontinental railway line across Canada', 'A short local railway serving a single city', 'A railway built entirely within the United States', 'A replacement for all Canadian roads and highways'], 0),
   ('What goal did the Grand Trunk Pacific Railway support in the Canadian west and north?', ['Opening new areas to settlement and trade', 'Ending all further settlement in the region', 'Preventing any future trade with other provinces', 'Closing off the region from the rest of Canada'], 0),
   ('What financial challenge did the Grand Trunk Pacific Railway eventually face?', ['Significant financial struggles and debt', 'An enormous and unexpected profit surplus', 'No financial challenges at any point', 'A complete absence of construction costs'], 0),
   ('What eventually happened to the Grand Trunk Pacific Railway?', ['It was absorbed into the Canadian National Railway', 'It was sold entirely to a foreign government', 'It remained fully independent for the next century', 'It was dismantled with no replacement built'], 0),
   ('Why did the Canadian government support the construction of a second transcontinental railway?', ['To encourage further settlement, resource development, and economic growth across the country', 'The government opposed all forms of railway construction', 'A second railway had no economic benefit to Canada', 'The government wanted to discourage westward settlement'], 0)]),
]),
day(144, [
L('Writing: The Personal Essay and Reflective Writing',
  'Grade 8 Language strand: a personal essay allows a writer to explore a meaningful experience or idea through a reflective, first-person voice, balancing storytelling with insight about what the experience taught the writer or how it shaped their perspective.',
  [('What voice does a personal essay typically use?', ['A reflective, first-person voice', 'A strictly third-person, impersonal voice', 'A voice that avoids the writers own experiences entirely', 'A voice used only in scientific reports'], 0),
   ('What does a personal essay balance alongside storytelling?', ['Insight about what the experience taught the writer or how it shaped their perspective', 'A complete absence of any personal reflection', 'A list of unrelated facts with no story', 'Instructions for completing an unrelated task'], 0),
   ('Why might a writer choose to write a personal essay about a specific memory?', ['To explore the deeper meaning or lasting impact of that memory', 'Personal essays never focus on a specific memory', 'To avoid any reflection on past experiences', 'To describe an experience that never actually happened'], 0),
   ('What distinguishes a personal essay from a simple retelling of events?', ['A personal essay includes reflection and analysis, not just a sequence of events', 'A personal essay never includes any events at all', 'There is no meaningful difference between the two', 'A personal essay must always be written in the third person'], 0),
   ('Why can personal essays be a powerful way to connect with readers?', ['Honest reflection on a real experience can help readers relate to universal feelings or lessons', 'Personal essays never connect with a readers own experiences', 'Readers are never interested in another persons reflections', 'Personal essays are only ever read by the writer'], 0)]),
M('Algebra: Solving Systems of Equations Using Gaussian Elimination',
  'Grade 8 Math strand: Gaussian elimination solves systems of linear equations by using row operations to transform an augmented matrix into a simpler triangular form, from which the full solution can be found through back-substitution.',
  [('What does Gaussian elimination use to transform a system of equations?', ['Row operations applied to an augmented matrix', 'Random guessing of possible solutions', 'A single division with no other steps', 'Graphing each equation with no algebraic steps'], 0),
   ('What form does Gaussian elimination aim to reduce a matrix into?', ['A triangular form', 'A perfectly circular form', 'A form with no numerical entries', 'A form identical to the original matrix'], 0),
   ('What technique is typically used after reaching triangular form to find the full solution?', ['Back-substitution', 'Random elimination of all variables', 'Ignoring the remaining equations entirely', 'Multiplying every entry by zero'], 0),
   ('Which of these is a valid row operation used in Gaussian elimination?', ['Adding a multiple of one row to another row', 'Deleting a row without replacing it', 'Changing the number of variables in the system', 'Converting the matrix into a single number'], 0),
   ('Why is Gaussian elimination useful for solving systems with more than two or three variables?', ['It provides a systematic method that can be applied consistently regardless of how many variables or equations are involved', 'It only works for systems with exactly one variable', 'Gaussian elimination cannot be used for more than two equations', 'Larger systems can never be solved using matrix methods'], 0)]),
Sc('Space Science: Rocket Propulsion and Space Travel',
   'Grade 8 Science strand: rockets move forward according to Newtons third law, expelling exhaust gas backward at high speed to generate thrust forward, a principle that must overcome both gravity and atmospheric resistance for a rocket to reach space.',
   [('Which law of motion explains how a rocket generates thrust?', ['Newtons third law of motion', 'Newtons first law of motion', 'The law of conservation of mass alone', 'A law that applies only to objects at rest'], 0),
    ('What does a rocket expel to generate forward thrust?', ['Exhaust gas, expelled backward at high speed', 'Solid rock, expelled forward', 'Water vapour, expelled sideways only', 'Nothing is expelled during rocket propulsion'], 0),
    ('What forces must a rocket overcome to reach space?', ['Gravity and atmospheric resistance', 'Only the force of magnetism', 'Only the force of friction on land', 'Rockets do not need to overcome any forces'], 0),
    ('Why do rockets carry both fuel and an oxidizer, unlike many engines on Earth?', ['Rockets often travel where there is no atmospheric oxygen available to burn fuel', 'Rockets never require oxygen at any stage of flight', 'Carrying an oxidizer has no connection to combustion', 'Earth-based engines never require any oxygen either'], 0),
    ('Why is rocket propulsion considered essential to modern space exploration?', ['It provides the only currently practical way to generate enough thrust to escape Earths gravity', 'Rockets have no role in reaching outer space', 'Spacecraft can escape gravity without any propulsion system', 'Rocket propulsion is only used for travel within the atmosphere'], 0)]),
H('The Ontario Temperance Act and the Prohibition Era in Canada',
  'Grade 8 History strand: passed in 1916, the Ontario Temperance Act banned the sale of alcoholic beverages in the province as part of a broader Canadian prohibition movement during World War I, though it was eventually repealed in the 1920s amid widespread bootlegging.',
  [('What did the Ontario Temperance Act of 1916 ban?', ['The sale of alcoholic beverages in the province', 'The sale of all imported goods', 'The construction of new factories', 'The publication of newspapers'], 0),
   ('During which broader conflict did prohibition gain support across Canada?', ['World War I', 'The War of 1812', 'World War II', 'The Korean War'], 0),
   ('What social movement influenced the passing of prohibition laws like the Ontario Temperance Act?', ['The temperance and social reform movement', 'A movement demanding more alcohol production', 'A movement focused solely on railway expansion', 'A movement opposed to all forms of social reform'], 0),
   ('What eventually happened to prohibition laws like the Ontario Temperance Act?', ['They were repealed in the 1920s amid widespread bootlegging', 'They remain in effect in Ontario today', 'They were strengthened and expanded after 1920', 'They were replaced immediately with no change in policy'], 0),
   ('Why did prohibition laws prove difficult to enforce?', ['Illegal production and sale of alcohol, or bootlegging, continued despite the legal ban', 'Prohibition laws were never actually challenged by anyone', 'Alcohol production stopped completely once the law passed', 'Enforcement was never attempted after the law was passed'], 0)]),
]),
day(145, [
L('Media Literacy: Analyzing Framing and Word Choice in News Reporting',
  'Grade 8 Language strand: framing refers to how a journalists choice of words, images, and emphasis can shape a readers interpretation of an event, with the same factual event potentially described very differently depending on the language and details a source chooses to include.',
  [('What does framing refer to in news reporting?', ['How word choice, images, and emphasis shape a readers interpretation of an event', 'The physical layout of a printed newspaper page', 'The exact date an article was published', 'The number of words used in an articles headline only'], 0),
   ('Why might two news outlets describe the same event very differently?', ['Each outlet may choose different words, images, and details to emphasize', 'News outlets are required by law to describe events identically', 'Framing has no influence on how an event is described', 'Only one outlet is ever allowed to report on a given event'], 0),
   ('Which word choice might indicate a more negative framing of a protest?', ['Describing protesters as a mob rather than as demonstrators', 'Describing protesters using entirely neutral language', 'Choosing not to mention the protest at all', 'Using the exact same wording as every other source'], 0),
   ('Why is recognizing framing an important media literacy skill?', ['It helps readers notice how language choices can subtly influence their opinion of an event', 'Framing has no effect on how a reader interprets a story', 'This skill has no connection to understanding the news', 'Recognizing framing prevents a reader from understanding any article'], 0),
   ('Why might comparing multiple sources on the same story help a reader identify framing?', ['Differences between sources can reveal how each outlet chose to emphasize or downplay certain details', 'Comparing sources always produces identical framing with no differences', 'Only a single source should ever be consulted for accuracy', 'Framing can only be identified by reading exactly one article'], 0)]),
M('Geometry: An Introduction to Hyperbolic Geometry',
  'Grade 8 Math strand: hyperbolic geometry is a non-Euclidean geometry in which, unlike flat Euclidean space, more than one line through a point can be drawn parallel to a given line, and the angles of a triangle always sum to less than 180 degrees.',
  [('What makes hyperbolic geometry a non-Euclidean geometry?', ['It does not follow all the traditional rules of flat, Euclidean space', 'It follows every rule of Euclidean geometry with no differences', 'It only applies to one-dimensional lines', 'It was developed before Euclidean geometry existed'], 0),
   ('In hyperbolic geometry, what is true about the angles of a triangle?', ['They always sum to less than 180 degrees', 'They always sum to exactly 180 degrees', 'They always sum to more than 180 degrees', 'Triangles cannot exist in hyperbolic geometry'], 0),
   ('In hyperbolic geometry, how many lines can be drawn through a point parallel to a given line?', ['More than one', 'Exactly one', 'Exactly zero', 'An undefined and meaningless number'], 0),
   ('How does hyperbolic geometry differ from spherical geometry in terms of curvature?', ['Hyperbolic geometry describes negatively curved space, while spherical geometry describes positively curved space', 'Both describe exactly the same type of curvature', 'Hyperbolic geometry describes flat, uncurved space', 'Spherical geometry describes negatively curved space instead'], 0),
   ('Why do mathematicians and scientists study non-Euclidean geometries like hyperbolic geometry?', ['They can more accurately describe certain curved surfaces and spaces that flat Euclidean geometry cannot model', 'Non-Euclidean geometries have no real mathematical applications', 'Euclidean geometry can already describe every curved surface perfectly', 'Hyperbolic geometry was proven to be entirely incorrect'], 0)]),
Sc('Biology: Photosynthesis and Energy Conversion in Plants',
   'Grade 8 Science strand: photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce glucose and oxygen, converting light energy into chemical energy stored in the bonds of sugar molecules.',
   [('What three ingredients do plants use during photosynthesis?', ['Sunlight, water, and carbon dioxide', 'Sunlight, salt, and iron', 'Only soil and sunlight', 'Only oxygen and nitrogen gas'], 0),
    ('What two main products does photosynthesis produce?', ['Glucose and oxygen', 'Carbon dioxide and nitrogen', 'Water and salt', 'Iron and hydrogen gas'], 0),
    ('What type of energy conversion occurs during photosynthesis?', ['Light energy is converted into chemical energy stored in glucose', 'Chemical energy is converted directly into sound', 'No energy conversion occurs during photosynthesis', 'Heat energy is converted into electrical energy'], 0),
    ('In which part of the plant cell does photosynthesis mainly take place?', ['The chloroplast', 'The nucleus', 'The mitochondria', 'The cell wall alone'], 0),
    ('Why is photosynthesis considered essential to most life on Earth?', ['It produces the oxygen many organisms need to breathe and forms the base of most food chains', 'Photosynthesis has no connection to the oxygen in the atmosphere', 'Most organisms do not rely on plants for food in any way', 'Photosynthesis only occurs in animals, not plants'], 0)]),
H('Nellie McClung and the Fight for Womens Rights in Canada',
  'Grade 8 History strand: Nellie McClung was a Canadian writer and politician who campaigned for womens suffrage in the early twentieth century and later joined the Famous Five in the 1929 Persons Case, helping secure legal recognition of women as persons under Canadian law.',
  [('What cause did Nellie McClung campaign for in the early twentieth century?', ['Womens suffrage, the right of women to vote', 'The abolition of all provincial governments', 'A ban on all forms of higher education', 'The elimination of the office of prime minister'], 0),
   ('What group did Nellie McClung join to challenge the legal definition of person in Canada?', ['The Famous Five', 'The Group of Seven', 'The Fathers of Confederation', 'The Royal Commission on Bilingualism'], 0),
   ('What legal case is Nellie McClung most closely associated with?', ['The Persons Case of 1929', 'The Pacific Scandal of 1873', 'The King-Byng Affair of 1926', 'The Alaska Boundary Dispute of 1903'], 0),
   ('What was the outcome of the Persons Case for women in Canada?', ['Women were legally recognized as persons under Canadian law', 'Women were barred from all political activity', 'The case had no impact on Canadian law', 'Women lost their existing legal rights entirely'], 0),
   ('Why is Nellie McClung considered an important figure in Canadian history?', ['Her activism helped advance both voting rights and legal recognition for women in Canada', 'She opposed all efforts to expand womens rights', 'She played no role in any womens rights movement', 'Her work had no lasting impact on Canadian law'], 0)]),
]),
day(146, [
L('Grammar: Absolute Phrases and Sentence Variety',
  'Grade 8 Language strand: an absolute phrase modifies an entire sentence rather than a single word, typically consisting of a noun followed by a participle, and adds descriptive detail or emphasis while creating more varied and sophisticated sentence structures.',
  [('What does an absolute phrase modify?', ['An entire sentence rather than a single word', 'Only a single verb within a sentence', 'Only the subject of a sentence', 'Nothing, since absolute phrases have no grammatical function'], 0),
   ('What structure does an absolute phrase typically consist of?', ['A noun followed by a participle', 'A verb followed by an adverb only', 'A preposition with no accompanying noun', 'A conjunction joining two complete sentences'], 0),
   ('Which sentence contains an absolute phrase?', ['Her hands trembling, she opened the letter.', 'She opened the letter quickly.', 'She and her sister opened the letter together.', 'The letter was opened by her.'], 0),
   ('Why might a writer use an absolute phrase?', ['To add descriptive detail and create more varied, sophisticated sentence structures', 'Absolute phrases always make writing less descriptive', 'To remove all detail from a sentence', 'Absolute phrases are grammatically forbidden in formal writing'], 0),
   ('How does using absolute phrases benefit a writers overall style?', ['It helps avoid repetitive sentence patterns and adds richer description', 'It forces every sentence to follow an identical pattern', 'It removes the need for any descriptive detail', 'Absolute phrases have no effect on sentence variety'], 0)]),
M('Trigonometry: Sum and Difference Identities',
  'Grade 8 Math strand: sum and difference identities allow the sine, cosine, or tangent of the sum or difference of two angles to be expressed in terms of the sines and cosines of the individual angles, useful for finding exact trigonometric values and simplifying expressions.',
  [('What do sum and difference identities allow a mathematician to express?', ['The sine, cosine, or tangent of a sum or difference of two angles in terms of the individual angles', 'The area of a triangle using only its base', 'The volume of a three-dimensional solid', 'A ratio with no connection to angles'], 0),
   ('Why are sum and difference identities useful for finding exact trigonometric values?', ['They allow angles that are not standard to be broken into combinations of familiar angles', 'They eliminate the need to ever calculate an angle', 'They only apply to angles measured in degrees, never radians', 'They can only be used with right triangles'], 0),
   ('Which expression correctly represents the identity for the cosine of a difference of two angles, cos(A-B)?', ['cos A cos B plus sin A sin B', 'cos A cos B minus sin A sin B', 'sin A cos B plus cos A sin B', 'sin A sin B minus cos A cos B'], 0),
   ('In what type of problems are sum and difference identities commonly applied?', ['Simplifying trigonometric expressions and solving trigonometric equations', 'Calculating the area of a rectangle', 'Balancing a chemical equation', 'Determining the mean of a data set'], 0),
   ('Why are these identities considered building blocks for other trigonometric identities, such as double-angle formulas?', ['Many other identities can be derived directly by applying the sum and difference identities to special cases', 'Double-angle formulas have no mathematical connection to these identities', 'Sum and difference identities cannot be used to derive any other formula', 'These identities are only used in a single, unrelated context'], 0)]),
Sc('Chemistry: The Chemistry of Combustion and Fire',
   'Grade 8 Science strand: combustion is a chemical reaction in which a fuel rapidly reacts with oxygen, releasing heat and light, and requires three components known as the fire triangle: fuel, oxygen, and heat.',
   [('What is combustion?', ['A chemical reaction in which a fuel rapidly reacts with oxygen, releasing heat and light', 'A physical change with no chemical reaction involved', 'A reaction that only occurs underwater', 'A process that absorbs heat rather than releasing it'], 0),
    ('What three components make up the fire triangle?', ['Fuel, oxygen, and heat', 'Water, salt, and sand', 'Light, sound, and pressure', 'Carbon dioxide, nitrogen, and hydrogen'], 0),
    ('What happens if one part of the fire triangle is removed?', ['The combustion reaction can no longer continue, and the fire goes out', 'The fire burns even more intensely', 'Removing any part has no effect on the fire', 'The fire triangle only applies to electrical fires'], 0),
    ('Why does blowing on a small flame sometimes put it out?', ['It can remove enough heat or disrupt the fuel and oxygen mixture to stop combustion', 'Blowing on a flame always makes it burn hotter', 'Air has no effect on a burning flame', 'Blowing adds additional fuel to the flame'], 0),
    ('Why is understanding the fire triangle useful for fire prevention and safety?', ['It helps people identify effective ways to prevent or extinguish fires by removing one of the three necessary components', 'The fire triangle has no practical safety applications', 'Fires cannot be prevented or extinguished using this concept', 'Understanding combustion has no connection to fire safety'], 0)]),
H('The Formation of the Canadian Wheat Board',
  'Grade 8 History strand: established in 1935, the Canadian Wheat Board was created to market and sell wheat on behalf of prairie farmers, aiming to stabilize prices and provide farmers with more predictable income after years of volatile markets during the Great Depression.',
  [('In what year was the Canadian Wheat Board established?', ['1935', '1867', '1905', '1949'], 0),
   ('What was the main purpose of the Canadian Wheat Board?', ['To market and sell wheat on behalf of prairie farmers', 'To eliminate all wheat production in Canada', 'To manage Canadas railway system', 'To regulate the fishing industry'], 0),
   ('What economic problem was the Canadian Wheat Board designed to address?', ['Volatile wheat prices and unpredictable farmer income', 'A sudden shortage of available farmland', 'An oversupply of manufactured goods', 'A lack of interest in prairie settlement'], 0),
   ('During what broader economic period was the Canadian Wheat Board created?', ['The Great Depression', 'World War II', 'The Cold War', 'The 1990s recession'], 0),
   ('Why might prairie farmers have supported the creation of a centralized wheat marketing board?', ['It offered more price stability and collective bargaining power than individual farmers had on their own', 'It reduced every farmers income significantly', 'Farmers had no interest in price stability', 'A centralized board offered no benefit to individual farmers'], 0)]),
]),
day(147, [
L('Vocabulary: Eponyms and Words Derived From Names',
  'Grade 8 Language strand: an eponym is a word derived from the name of a real or fictional person, place, or event, such as sandwich or boycott, and studying eponyms can reveal interesting historical or cultural origins behind everyday vocabulary.',
  [('What is an eponym?', ['A word derived from the name of a real or fictional person, place, or event', 'A word with no historical origin whatsoever', 'A grammatical rule about verb tense', 'A citation style used in academic writing'], 0),
   ('Which of these words is an eponym?', ['Sandwich', 'Table', 'Quickly', 'Beautiful'], 0),
   ('Why might studying eponyms be interesting to a reader?', ['It can reveal historical or cultural stories behind everyday words', 'Eponyms never have any connection to history or culture', 'Studying eponyms provides no insight into language', 'Eponyms are identical in meaning to every other word'], 0),
   ('Which type of source might an eponym commonly be derived from?', ['A persons name, such as an inventor or historical figure', 'A number with no connection to a name', 'A punctuation mark', 'A grammatical tense'], 0),
   ('Why do eponyms sometimes lose their connection to their original meaning over time?', ['As words become common in everyday use, their specific historical origin often fades from common knowledge', 'Eponyms always retain a clear connection to their origin forever', 'Words never change in meaning over time', 'Eponyms are created without any original meaning at all'], 0)]),
M('Number Theory: An Introduction to Continued Fractions',
  'Grade 8 Math strand: a continued fraction expresses a number as a whole number plus a fraction whose denominator is itself a whole number plus a fraction, and so on, providing an alternative way to represent and approximate both rational and irrational numbers.',
  [('How does a continued fraction express a number?', ['As a whole number plus a fraction whose denominator continues the same pattern', 'As a single whole number with no fractional part', 'As a percentage with no denominator', 'As a ratio of two unrelated shapes'], 0),
   ('What can continued fractions be used to approximate?', ['Both rational and irrational numbers', 'Only whole numbers with no decimal part', 'Only negative numbers', 'Numbers that do not exist on the number line'], 0),
   ('Why might a mathematician prefer a continued fraction representation over a decimal for certain irrational numbers?', ['Continued fractions can reveal patterns and provide very accurate rational approximations', 'Continued fractions are always less accurate than decimals', 'Decimals can never approximate irrational numbers', 'Continued fractions cannot represent irrational numbers at all'], 0),
   ('What happens when a continued fraction is truncated after a certain number of terms?', ['It produces a rational approximation of the original number', 'It always produces an exact, error-free value', 'The result is no longer a number at all', 'Truncating a continued fraction has no mathematical meaning'], 0),
   ('Why are continued fractions considered useful in advanced number theory?', ['They provide insight into the structure of numbers and can be used to solve certain types of equations efficiently', 'They have no applications in number theory', 'Continued fractions can only describe the number zero', 'They were proven to be mathematically invalid'], 0)]),
Sc('Biology: Plant Reproduction and Pollination',
   'Grade 8 Science strand: many flowering plants reproduce through pollination, the transfer of pollen from a flowers male structures to its female structures, often carried out by wind or animal pollinators such as bees, enabling fertilization and the production of seeds.',
   [('What is pollination?', ['The transfer of pollen from a flowers male structures to its female structures', 'The process by which a plant absorbs water through its roots', 'The process by which a seed germinates underground', 'A process that occurs only in animals, not plants'], 0),
    ('Which of these is a common animal pollinator?', ['Bees', 'Sharks', 'Wolves', 'Frogs'], 0),
    ('What process does pollination enable in flowering plants?', ['Fertilization and the production of seeds', 'The complete destruction of a flower', 'Photosynthesis occurring for the first time', 'The absorption of sunlight through the roots'], 0),
    ('Besides animals, what other natural force can carry pollen between flowers?', ['Wind', 'Sound waves', 'Electric currents', 'Magnetism'], 0),
    ('Why are pollinators considered essential to many ecosystems and agricultural systems?', ['Many food crops and wild plants depend on pollinators to reproduce successfully', 'Pollinators have no connection to plant reproduction', 'Most plants can reproduce without any pollination at all', 'Agricultural systems never rely on pollinators'], 0)]),
H('The Bank Act and the Development of Canadian Banking',
  'Grade 8 History strand: first passed in 1871 and renewed regularly since, the Bank Act established a federal framework regulating chartered banks in Canada, helping create a stable, unified national banking system rather than a patchwork of independent local banks.',
  [('In what year was the Bank Act first passed?', ['1871', '1867', '1905', '1935'], 0),
   ('What did the Bank Act establish?', ['A federal framework regulating chartered banks in Canada', 'A single provincial bank with no federal oversight', 'A total ban on all private banking in Canada', 'An agreement to eliminate paper currency'], 0),
   ('What kind of banking system did the Bank Act help create, compared to a patchwork of local banks?', ['A stable, unified national banking system', 'A system with no regulation at all', 'A system controlled entirely by foreign governments', 'A system that varied completely from town to town with no federal standard'], 0),
   ('How often has the Bank Act historically been reviewed and renewed?', ['Regularly, on a periodic basis', 'Only once, with no further review', 'Every single day since 1871', 'It has never been reviewed or renewed'], 0),
   ('Why is a stable, well-regulated banking system considered important for a growing national economy?', ['It helps maintain public confidence in financial institutions and supports consistent economic growth', 'A regulated banking system always harms economic growth', 'Banking regulation has no connection to public confidence', 'Unregulated banking systems are always more stable'], 0)]),
]),
day(148, [
L('Reading: Analyzing Nonlinear Narrative Structures and Timelines',
  'Grade 8 Language strand: a nonlinear narrative structure tells a story out of strict chronological order, using techniques such as multiple timelines or fragmented scenes, requiring readers to actively piece together the sequence of events and consider why an author chose that structure.',
  [('What defines a nonlinear narrative structure?', ['A story told out of strict chronological order', 'A story told in perfect chronological order with no exceptions', 'A story with no characters or events', 'A story that contains no structure at all'], 0),
   ('What might a nonlinear narrative use to present its story?', ['Multiple timelines or fragmented scenes', 'A single, uninterrupted timeline with no variation', 'A list of unrelated dictionary definitions', 'An index with no accompanying narrative'], 0),
   ('What must readers actively do when reading a nonlinear narrative?', ['Piece together the sequence of events themselves', 'Ignore the order of events completely', 'Assume every event happens simultaneously', 'Avoid drawing any conclusions about the story'], 0),
   ('Why might an author choose to structure a story nonlinearly rather than in strict chronological order?', ['To create suspense, emphasize a particular theme, or reveal information strategically', 'Nonlinear structures always confuse readers with no narrative purpose', 'Authors are never allowed to alter chronological order', 'Nonlinear structures remove all meaning from a story'], 0),
   ('Why is analyzing narrative structure a valuable literary skill?', ['It helps readers understand how an authors structural choices shape meaning and reader experience', 'Narrative structure has no effect on how a story is understood', 'This skill has no connection to literary analysis', 'Every narrative uses the exact same structure'], 0)]),
M('Statistics: An Introduction to Regression Analysis and Residuals',
  'Grade 8 Math strand: regression analysis models the relationship between variables by fitting a line or curve to data, and a residual measures the difference between an actual observed value and the value predicted by the regression model, helping assess how well the model fits the data.',
  [('What does regression analysis do?', ['Models the relationship between variables by fitting a line or curve to data', 'Randomly assigns numbers to a data set with no pattern', 'Removes all variables from a data set', 'Converts every data point into a whole number'], 0),
   ('What is a residual in regression analysis?', ['The difference between an actual observed value and the value predicted by the model', 'The total number of data points collected', 'The average of all values in a data set', 'A value that is always equal to zero'], 0),
   ('What does a small residual generally indicate about a regression models prediction for that point?', ['The predicted value was close to the actual observed value', 'The model completely failed to predict any value', 'The data point was removed from the data set', 'The residual has no connection to prediction accuracy'], 0),
   ('Why might a statistician examine a pattern in the residuals of a regression model?', ['A clear pattern in residuals can suggest the model does not fit the data well', 'Residual patterns are always meaningless and ignored', 'Residuals can never reveal information about a model', 'Examining residuals has no connection to model fit'], 0),
   ('Why is regression analysis widely used across fields such as economics and biology?', ['It provides a mathematical way to describe and predict relationships between variables based on real data', 'Regression analysis cannot be applied to real-world data', 'It has no practical use outside of pure mathematics', 'Economics and biology never involve relationships between variables'], 0)]),
Sc('Physics: Renewable Energy and Hydroelectric Power',
   'Grade 8 Science strand: hydroelectric power generates electricity by using the force of moving water, often controlled by a dam, to spin turbines connected to generators, offering a renewable energy source that does not directly release greenhouse gases during operation.',
   [('What force does hydroelectric power primarily rely on to generate electricity?', ['The force of moving water', 'The heat from burning coal', 'Wind blowing across open plains', 'Radioactive decay of uranium'], 0),
    ('What structure is commonly used to control and direct water flow in hydroelectric power generation?', ['A dam', 'A solar panel', 'A wind turbine tower', 'An oil refinery'], 0),
    ('What do turbines do in a hydroelectric power system?', ['Spin, connected to generators, to produce electricity', 'Store water for later agricultural use only', 'Convert electricity directly into heat with no other function', 'Filter pollutants out of the water supply'], 0),
    ('Why is hydroelectric power considered a renewable energy source?', ['It relies on the water cycle, which naturally replenishes the water supply', 'It relies on a fuel source that will eventually run out completely', 'Hydroelectric power requires burning fossil fuels', 'The water used is permanently destroyed and never replenished'], 0),
    ('Why might hydroelectric power be considered environmentally preferable to fossil fuels for generating electricity?', ['It does not directly release greenhouse gases into the atmosphere during operation', 'It releases more greenhouse gases than any fossil fuel', 'Hydroelectric power has no environmental impact of any kind', 'Fossil fuels produce electricity without releasing any emissions'], 0)]),
H('The Yukon Act of 1898 and the Creation of Yukon Territory',
  'Grade 8 History strand: passed in response to the rapid population growth of the Klondike Gold Rush, the Yukon Act of 1898 formally separated Yukon from the North-West Territories and created a distinct Yukon Territory with its own local government.',
  [('What rapid population change prompted the passing of the Yukon Act in 1898?', ['The Klondike Gold Rush', 'The construction of the Trans-Canada Highway', 'The signing of the Manitoba Act', 'The formation of the Supreme Court of Canada'], 0),
   ('What did the Yukon Act formally do?', ['Separated Yukon from the North-West Territories and created a distinct Yukon Territory', 'Merged Yukon permanently with British Columbia', 'Abolished all territorial governments in Canada', 'Transferred Yukon to the government of the United States'], 0),
   ('What did the newly created Yukon Territory receive as a result of the Yukon Act?', ['Its own local government', 'Full provincial status equal to Ontario', 'No government of any kind', 'Complete independence from Canada'], 0),
   ('Why might the rapid population growth caused by a gold rush prompt the creation of a new territory?', ['A sudden influx of people often requires more direct local governance and administration than a distant government can easily provide', 'Population growth never affects how a region is governed', 'Gold rushes always lead to a decrease in local population', 'New territories are created only when population declines'], 0),
   ('Why is the Yukon Act considered an important step in the political development of Northern Canada?', ['It formally established a distinct territorial identity and government structure for the Yukon region', 'It eliminated any form of government from the Yukon region', 'It had no lasting impact on Northern Canada', 'It merged the Yukon region into a single existing province'], 0)]),
]),
day(149, [
L('Writing: The Investigative Report and Data-Driven Journalism',
  'Grade 8 Language strand: an investigative report combines in-depth research, interviews, and data analysis to uncover and explain a significant issue, presenting evidence-based findings in a clear structure that often includes background context, data, and expert perspectives.',
  [('What does an investigative report combine to uncover a significant issue?', ['In-depth research, interviews, and data analysis', 'A single unsupported opinion with no research', 'A short list of unrelated facts', 'A collection of fictional stories'], 0),
   ('What might an investigative report include to support its findings?', ['Background context, data, and expert perspectives', 'No supporting evidence of any kind', 'Only the writers personal opinion', 'A summary of an unrelated topic'], 0),
   ('Why is evidence particularly important in an investigative report?', ['It supports the reports findings and helps establish credibility with readers', 'Evidence has no role in investigative journalism', 'Investigative reports are never expected to be credible', 'Readers never expect a report to include evidence'], 0),
   ('What distinguishes data-driven journalism from a purely opinion-based article?', ['Data-driven journalism relies primarily on collected data and evidence rather than personal opinion alone', 'Data-driven journalism never uses any data at all', 'There is no meaningful difference between the two', 'Opinion-based articles always contain more data than investigative reports'], 0),
   ('Why might an investigative report take longer to produce than a typical news article?', ['Thorough research, fact-checking, and data analysis often require significant time and effort', 'Investigative reports require no research at all', 'Typical news articles always take longer to produce', 'Fact-checking has no connection to how long a report takes'], 0)]),
M('Algebra: An Introduction to Eigenvalues and Eigenvectors',
  'Grade 8 Math strand: for a given square matrix, an eigenvector is a nonzero vector whose direction remains unchanged when the matrix is applied to it, and the eigenvalue is the scalar factor by which that eigenvector is stretched or shrunk.',
  [('What remains unchanged about an eigenvector when a matrix is applied to it?', ['Its direction', 'Its colour', 'Its name', 'Its position in the alphabet'], 0),
   ('What does an eigenvalue represent?', ['The scalar factor by which an eigenvector is stretched or shrunk', 'The total number of rows in a matrix', 'The sum of every entry in a matrix', 'A value that is always equal to one'], 0),
   ('What type of matrix must be used to find eigenvalues and eigenvectors?', ['A square matrix', 'A matrix with only one row', 'A matrix containing only zeros', 'Any shape of matrix, since shape is irrelevant'], 0),
   ('Why might a nonzero vector be required when defining an eigenvector?', ['A zero vector would trivially satisfy the equation without providing any meaningful direction information', 'Zero vectors are always the most meaningful choice', 'Eigenvectors are never allowed to have a direction', 'Nonzero vectors are never used in linear algebra'], 0),
   ('Why are eigenvalues and eigenvectors useful in fields like computer graphics and physics?', ['They help describe how a transformation stretches, shrinks, or rotates space along specific directions', 'They have no application outside of pure mathematics', 'Eigenvalues can only describe the colour of an image', 'Computer graphics never involve any form of transformation'], 0)]),
Sc('Earth Science: Soil Formation and Erosion',
   'Grade 8 Science strand: soil forms gradually through the weathering of rock combined with organic matter from decomposing plants and animals, while erosion, the movement of soil and rock by wind, water, or ice, can strip away this valuable layer if it is not properly protected.',
   [('What two main processes combine to form soil?', ['The weathering of rock and the addition of organic matter from decomposing plants and animals', 'The freezing of water and the melting of glaciers only', 'The burning of vegetation and the cooling of lava', 'The evaporation of ocean water alone'], 0),
    ('What is erosion?', ['The movement of soil and rock caused by wind, water, or ice', 'The process by which rock is created instantly', 'A process that only occurs deep underground', 'The chemical process of photosynthesis'], 0),
    ('Why can erosion be harmful to agricultural land?', ['It can strip away the nutrient-rich topsoil that plants need to grow', 'Erosion always adds more nutrients to farmland', 'Erosion has no effect on agricultural land', 'Erosion only affects land that is already barren'], 0),
    ('Which of these is a common method used to reduce soil erosion?', ['Planting vegetation to help hold soil in place', 'Removing all plant life from an area', 'Paving over soil with no drainage', 'Increasing water flow across bare soil'], 0),
    ('Why does soil formation typically take a very long time compared to how quickly erosion can occur?', ['Weathering rock and accumulating organic matter happens gradually, while wind and water can remove soil relatively quickly', 'Soil forms instantly while erosion takes centuries', 'Soil formation and erosion always occur at the exact same speed', 'Erosion never occurs faster than soil formation'], 0)]),
H('The Naturalization Act and Canadian Citizenship Before 1947',
  'Grade 8 History strand: before the Canadian Citizenship Act of 1947, people born in Canada were legally considered British subjects rather than Canadian citizens, with earlier naturalization laws governing how immigrants could gain British subject status within Canada.',
  [('Before 1947, what legal status did people born in Canada hold?', ['British subjects, rather than Canadian citizens', 'Citizens of the United States', 'Citizens with no legal status whatsoever', 'Citizens of France'], 0),
   ('What did earlier naturalization laws in Canada govern?', ['How immigrants could gain British subject status within Canada', 'How provinces could separate from Confederation', 'How railways were funded and built', 'How the Supreme Court of Canada was structured'], 0),
   ('What later law introduced the distinct legal status of Canadian citizenship?', ['The Canadian Citizenship Act of 1947', 'The British North America Act of 1867', 'The Statute of Westminster of 1931', 'The Manitoba Act of 1870'], 0),
   ('Why might it be significant that Canadians were legally British subjects rather than citizens before 1947?', ['It reflects how closely tied Canadas legal identity remained to Britain even decades after Confederation', 'It shows that Canada had no legal connection to Britain after 1867', 'It proves Canada was never part of the British Empire', 'It had no connection to Canadian identity at all'], 0),
   ('Why is understanding pre-1947 citizenship laws useful for studying Canadian identity?', ['It shows how Canadas sense of independent national identity developed gradually over time', 'Citizenship laws have no connection to national identity', 'Canadian identity has remained completely unchanged since 1867', 'Canada has never had any laws governing citizenship'], 0)]),
]),
day(150, [
L('Language Review: Grammar, Vocabulary, and Media Literacy (Days 141-149)',
  'Grade 8 Language strand review: students revisit verb tense consistency, homophones, multiple points of view, the personal essay, media framing, absolute phrases, eponyms, nonlinear narrative structures, and the investigative report.',
  [('What does verb tense consistency require?', ['That a writer maintain the same tense throughout a passage unless time genuinely changes', 'That every sentence use a different tense', 'That a sentence never contain a verb', 'That verbs always appear in the future tense'], 0),
   ('What is a homophone?', ['A word that sounds like another word but differs in spelling and meaning', 'A word that means the exact same thing as another word', 'A citation style used in research papers', 'A punctuation mark used to end a sentence'], 0),
   ('What voice does a personal essay typically use?', ['A reflective, first-person voice', 'A strictly third-person, impersonal voice', 'A voice that avoids the writers own experiences entirely', 'A voice used only in scientific reports'], 0),
   ('What does framing refer to in news reporting?', ['How word choice, images, and emphasis shape a readers interpretation of an event', 'The physical layout of a printed newspaper page', 'The exact date an article was published', 'The number of words used in an articles headline only'], 0),
   ('What defines a nonlinear narrative structure?', ['A story told out of strict chronological order', 'A story told in perfect chronological order with no exceptions', 'A story with no characters or events', 'A story that contains no structure at all'], 0)]),
M('Math Review: Calculus, Algebra, and Statistics (Days 141-149)',
  'Grade 8 Math strand review: students revisit the Fundamental Theorem of Calculus, Fermats Little Theorem, Gaussian elimination, sum and difference identities, and eigenvalues and eigenvectors.',
  [('What does the Fundamental Theorem of Calculus connect?', ['Differentiation and integration, showing they are inverse processes', 'Addition and subtraction of whole numbers', 'The area of a circle and its circumference', 'Two entirely unrelated branches of mathematics'], 0),
   ('According to Fermats Little Theorem, if p is prime and a is not divisible by p, what is a raised to the power of p minus 1 congruent to modulo p?', ['1', '0', 'p', 'a'], 0),
   ('What does Gaussian elimination use to transform a system of equations?', ['Row operations applied to an augmented matrix', 'Random guessing of possible solutions', 'A single division with no other steps', 'Graphing each equation with no algebraic steps'], 0),
   ('Which expression correctly represents the identity for the cosine of a difference of two angles, cos(A-B)?', ['cos A cos B plus sin A sin B', 'cos A cos B minus sin A sin B', 'sin A cos B plus cos A sin B', 'sin A sin B minus cos A cos B'], 0),
   ('What does an eigenvalue represent?', ['The scalar factor by which an eigenvector is stretched or shrunk', 'The total number of rows in a matrix', 'The sum of every entry in a matrix', 'A value that is always equal to one'], 0)]),
Sc('Science Review: Chemistry, Physics, and Earth Science (Days 141-149)',
   'Grade 8 Science strand review: students revisit ionic and covalent bonding, pendulums and simple harmonic motion, rocket propulsion, photosynthesis, and hydroelectric power.',
   [('What happens during the formation of an ionic bond?', ['Electrons transfer from one atom to another, creating oppositely charged ions that attract each other', 'Two atoms share a pair of electrons equally', 'No electrons are involved in the bond at all', 'Atoms repel each other permanently'], 0),
    ('What factor primarily determines the period of a simple pendulum?', ['The length of the pendulum and the strength of gravity', 'The colour of the pendulum bob', 'The material used to make the string only', 'The time of day the pendulum is observed'], 0),
    ('Which law of motion explains how a rocket generates thrust?', ['Newtons third law of motion', 'Newtons first law of motion', 'The law of conservation of mass alone', 'A law that applies only to objects at rest'], 0),
    ('What type of energy conversion occurs during photosynthesis?', ['Light energy is converted into chemical energy stored in glucose', 'Chemical energy is converted directly into sound', 'No energy conversion occurs during photosynthesis', 'Heat energy is converted into electrical energy'], 0),
    ('What force does hydroelectric power primarily rely on to generate electricity?', ['The force of moving water', 'The heat from burning coal', 'Wind blowing across open plains', 'Radioactive decay of uranium'], 0)]),
H('History Review: Early Twentieth-Century Canada (Days 141-149)',
  'Grade 8 History strand review: students revisit the 1911 reciprocity election, the Grand Trunk Pacific Railway, Nellie McClung and the Persons Case, the Bank Act, and the Yukon Act of 1898.',
  [('What trade policy did Lauriers government campaign on in the 1911 election?', ['A reciprocity, or free trade, agreement with the United States', 'A complete ban on all trade with the United States', 'A new trade agreement with France', 'A plan to eliminate all provincial taxes'], 0),
   ('What was the Grand Trunk Pacific Railway intended to be?', ['A second transcontinental railway line across Canada', 'A short local railway serving a single city', 'A railway built entirely within the United States', 'A replacement for all Canadian roads and highways'], 0),
   ('What group did Nellie McClung join to challenge the legal definition of person in Canada?', ['The Famous Five', 'The Group of Seven', 'The Fathers of Confederation', 'The Royal Commission on Bilingualism'], 0),
   ('What did the Bank Act establish?', ['A federal framework regulating chartered banks in Canada', 'A single provincial bank with no federal oversight', 'A total ban on all private banking in Canada', 'An agreement to eliminate paper currency'], 0),
   ('What rapid population change prompted the passing of the Yukon Act in 1898?', ['The Klondike Gold Rush', 'The construction of the Trans-Canada Highway', 'The signing of the Manitoba Act', 'The formation of the Supreme Court of Canada'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_141_150)
    append_to(8, g8_141_150)
