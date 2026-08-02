#!/usr/bin/env python3
"""Grade 8, Days 131-140 -- extends Grade 8 from 130 to 140 days. Topics
chosen after dumping the existing Day 1-130 title list (data/grade8.json)
in full to avoid any overlap: subject-verb agreement with collective and
indefinite pronouns, oxymorons, determining authors purpose and audience,
crafting a strong introduction and hook, media ownership and
consolidation, cause and effect structures in nonfiction, pronoun-
antecedent agreement, regionalisms and dialect, and the comparative book
review; an introduction to integrals, linear Diophantine equations,
confidence intervals, inverse matrices, graphing sine and cosine
functions, parametric equations, exponential and logarithmic equations,
chi-square tests, and taxicab geometry; the muscular system, the
chemistry of rust and corrosion, the lymphatic system, levers and
mechanical torque, the structure and function of chromosomes, solar
panels and photovoltaic cells, the human ear, freshwater ecosystems, and
comets/asteroids/meteors; British Columbia and Prince Edward Island
joining Confederation, the Manitoba Act of 1870, the British North
America Act of 1867, Sir John A. Macdonald, the formation of the Supreme
Court of Canada, the creation of the North-West Territories, Wilfrid
Laurier, and Alberta and Saskatchewan joining Confederation in 1905. Day
140 is a review day across all four subjects.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days121_130.py.
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


def _rebalance_answer_positions(days, seed=20260801):
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


g8_131_140 = [
day(131, [
L('Grammar: Subject-Verb Agreement with Collective and Indefinite Pronouns',
  'Grade 8 Language strand: subject-verb agreement requires that a verb match its subject in number, with collective nouns such as team or class often taking a singular verb and indefinite pronouns such as everyone or nobody also requiring singular verbs even when they suggest more than one person.',
  [('What does subject-verb agreement require?', ['That a verb match its subject in number', 'That every sentence use a plural verb', 'That a sentence never contain a subject', 'That verbs always precede their subjects'], 0),
   ('Which verb correctly completes: The team ___ practicing every day?', ['is', 'are', 'were', 'have'], 0),
   ('Which verb correctly completes: Everyone in the class ___ finished the assignment?', ['has', 'have', 'were', 'are'], 0),
   ('Why do indefinite pronouns like nobody or everyone typically take a singular verb?', ['They refer to a single, generalized person or thing even though they suggest a group', 'They always refer to exactly two people', 'Indefinite pronouns never affect verb choice', 'They are always plural in meaning'], 0),
   ('Why is correct subject-verb agreement important in formal writing?', ['Incorrect agreement can distract a reader and make writing appear less polished or clear', 'Agreement errors always improve clarity', 'Formal writing never requires grammatical accuracy', 'Subject-verb agreement only matters in spoken language'], 0)]),
M('Calculus Preview: An Introduction to Integrals and Area Under a Curve',
  'Grade 8 Math strand: an integral is a mathematical tool used to calculate the area between a curve and the x-axis, building on the idea of summing infinitely many infinitely thin rectangles beneath a function.',
  [('What does a definite integral commonly represent?', ['The area between a curve and the x-axis over a given interval', 'The slope of a line at a single point', 'A fixed number unrelated to area', 'The perimeter of a shape'], 0),
   ('What concept do integrals build upon, involving summing many thin slices?', ['Summing infinitely many infinitely thin rectangles beneath a curve', 'Multiplying two whole numbers together', 'Dividing a shape into two equal halves only', 'Counting the vertices of a polygon'], 0),
   ('How are integrals and derivatives related in calculus?', ['Integration and differentiation are inverse operations of each other', 'They are entirely unrelated operations', 'Integrals always equal zero when derivatives exist', 'Derivatives can only be found after integrating twice'], 0),
   ('If a function lies entirely above the x-axis, what does its definite integral over an interval represent?', ['A positive area between the curve and the x-axis', 'A negative, undefined area', 'The exact height of the curve at one point', 'The number of times the curve crosses the axis'], 0),
   ('Why are integrals useful in fields like physics and engineering?', ['They can calculate quantities such as total distance traveled from a velocity function', 'They have no real-world applications', 'Integrals can only be used with whole numbers', 'Physics never requires calculating area or accumulation'], 0)]),
Sc('The Muscular System: Types of Muscle and Movement',
   'Grade 8 Science strand: the muscular system is made up of skeletal, smooth, and cardiac muscle tissue, with skeletal muscles working in pairs to pull on bones and produce voluntary movement at the joints.',
   [('What are the three main types of muscle tissue in the body?', ['Skeletal, smooth, and cardiac muscle', 'Skeletal, elastic, and rigid muscle', 'Voluntary, involuntary, and stationary bone', 'Cardiac, digestive, and skeletal bone'], 0),
    ('Which type of muscle is responsible for voluntary movement, such as lifting an arm?', ['Skeletal muscle', 'Smooth muscle', 'Cardiac muscle', 'Connective tissue'], 0),
    ('How do skeletal muscles typically work together to move a joint?', ['They work in pairs, with one muscle contracting while its partner relaxes', 'A single muscle always works completely alone', 'Muscles never connect to bones at joints', 'Muscles only contract during sleep'], 0),
    ('Where is smooth muscle commonly found in the body?', ['In the walls of organs such as the stomach and intestines', 'Only in the heart', 'Only in the fingers and toes', 'Smooth muscle does not exist in the human body'], 0),
    ('Why is cardiac muscle uniquely suited to its function in the heart?', ['It can contract rhythmically and continuously without becoming fatigued the way skeletal muscle does', 'It never contracts at any point', 'It is identical in every way to skeletal muscle', 'Cardiac muscle requires conscious voluntary control to beat'], 0)]),
H('British Columbia Joins Confederation in 1871',
  'Grade 8 History strand: British Columbia joined Confederation in 1871 after the Canadian government promised to build a transcontinental railway connecting the Pacific coast to the rest of the country, a commitment that shaped decades of national infrastructure development.',
  [('In what year did British Columbia join Confederation?', ['1871', '1867', '1905', '1949'], 0),
   ('What promise from the Canadian government helped convince British Columbia to join Confederation?', ['A commitment to build a transcontinental railway to the Pacific coast', 'A promise to lower all provincial taxes', 'A guarantee of full independence within ten years', 'An agreement to relocate the national capital'], 0),
   ('Why was a railway connection especially important to British Columbia at the time?', ['It would link the isolated Pacific colony to markets and communities in eastern Canada', 'British Columbia had no interest in trade with the rest of Canada', 'Railways had no economic value in the 1870s', 'British Columbia already had a railway connecting it to the east'], 0),
   ('What broader Canadian goal did the promise of a Pacific railway support?', ['Uniting the country from coast to coast through transportation and trade', 'Dividing the country into separate independent nations', 'Ending all trade between provinces', 'Preventing further westward settlement'], 0),
   ('Why is British Columbias entry into Confederation considered significant in Canadian history?', ['It extended Canadian territory to the Pacific Ocean and helped justify major railway construction', 'It marked the end of Canadian expansion', 'It had no connection to later infrastructure projects', 'British Columbia left Confederation shortly afterward'], 0)]),
]),
day(132, [
L('Vocabulary: Oxymorons and Contradictory Phrases',
  'Grade 8 Language strand: an oxymoron is a figure of speech that combines two normally contradictory terms for effect, such as bittersweet or deafening silence, often used to capture complexity or create a striking image.',
  [('What is an oxymoron?', ['A figure of speech that combines two contradictory terms for effect', 'A word that means the exact same thing when repeated', 'A citation style used in research papers', 'A grammatical rule about verb tense'], 0),
   ('Which phrase is an example of an oxymoron?', ['Deafening silence', 'Bright sunshine', 'Tall building', 'Fast car'], 0),
   ('Why might a writer use an oxymoron in a poem or story?', ['To capture a complex or contradictory feeling in a striking, memorable way', 'Oxymorons always confuse readers with no purpose', 'Oxymorons are grammatically incorrect and should be avoided', 'Oxymorons only appear in scientific writing'], 0),
   ('What effect does combining contradictory words often create for a reader?', ['It draws attention to a tension or complexity within an idea', 'It always simplifies an idea completely', 'It removes all emotional meaning from a phrase', 'It has no effect on how a reader interprets a text'], 0),
   ('Why is recognizing oxymorons a useful skill when analyzing figurative language?', ['It helps readers notice when an author is emphasizing contradiction or nuance intentionally', 'Oxymorons never appear in literature', 'This skill has no connection to figurative language', 'Recognizing oxymorons prevents readers from understanding a text'], 0)]),
M('Number Theory: An Introduction to Linear Diophantine Equations',
  'Grade 8 Math strand: a linear Diophantine equation is an equation such as ax plus by equals c that is solved using only integer values, with solutions existing only when the greatest common divisor of a and b divides evenly into c.',
  [('What distinguishes a Diophantine equation from a typical algebraic equation?', ['Only integer solutions are considered valid', 'Only decimal solutions are considered valid', 'The equation must always equal zero', 'The equation can never have more than one variable'], 0),
   ('For the equation ax plus by equals c to have integer solutions, what condition must be true?', ['The greatest common divisor of a and b must divide evenly into c', 'The value of c must always be negative', 'The values of a and b must always be equal', 'The equation must contain no constant term'], 0),
   ('Which of these is an example of a linear Diophantine equation?', ['3x plus 5y equals 11, solved using only whole numbers', 'The area formula for a circle', 'A quadratic equation with irrational roots', 'An equation solved only with fractions'], 0),
   ('In what field are Diophantine equations particularly useful today?', ['Cryptography and computer science', 'Only ancient farming techniques', 'Only music composition', 'Only weather forecasting'], 0),
   ('Why are Diophantine equations named after an ancient mathematician?', ['They are named after Diophantus, who studied equations restricted to whole-number solutions', 'They were invented in the twentieth century with no historical connection', 'They have no historical origin at all', 'They were first studied by a mathematician who rejected the use of integers'], 0)]),
Sc('The Chemistry of Rust and Corrosion',
   'Grade 8 Science strand: rust forms when iron reacts with oxygen and water in a slow chemical process called oxidation, gradually weakening metal structures unless the reaction is prevented through protective coatings or alternative materials.',
   [('What chemical process causes iron to rust?', ['Oxidation, a reaction between iron, oxygen, and water', 'Freezing at low temperatures', 'A purely physical change with no chemical reaction', 'Exposure to sunlight alone'], 0),
    ('What two substances must be present for iron to rust?', ['Oxygen and water', 'Only heat and pressure', 'Only sunlight and wind', 'Only salt with no water present'], 0),
    ('Why does rust weaken metal structures over time?', ['The oxidation reaction gradually breaks down the metals structure, making it brittle and flaky', 'Rust makes metal permanently stronger', 'Rust has no effect on the physical structure of metal', 'Oxidation always strengthens the bonds within iron'], 0),
    ('What is one common method used to prevent rust from forming on metal?', ['Applying a protective coating, such as paint or galvanized zinc', 'Leaving the metal exposed to more water', 'Removing all oxygen from the surrounding air, which is always practical', 'Heating the metal constantly'], 0),
    ('Why might engineers choose corrosion-resistant materials, such as stainless steel, for structures exposed to moisture?', ['These materials resist the oxidation reactions that cause rust, extending the structures lifespan', 'Corrosion-resistant materials always rust faster than plain iron', 'Moisture has no effect on any metal structure', 'Stainless steel reacts more quickly with oxygen than plain iron'], 0)]),
H('Prince Edward Island Joins Confederation in 1873',
  'Grade 8 History strand: Prince Edward Island, though it hosted the 1864 Charlottetown Conference, initially declined to join Confederation and only entered in 1873 after facing serious railway debt, becoming Canadas smallest province by area.',
  [('In what year did Prince Edward Island join Confederation?', ['1873', '1864', '1867', '1905'], 0),
   ('What historic 1864 event took place on Prince Edward Island despite the province initially declining to join Confederation?', ['The Charlottetown Conference', 'The Quebec Conference', 'The Confederation of British Columbia', 'The signing of the Numbered Treaties'], 0),
   ('What financial problem helped push Prince Edward Island toward joining Confederation?', ['Serious debt from building a provincial railway', 'A surplus of unused government funds', 'A dispute over a national anthem', 'The discovery of large gold deposits'], 0),
   ('What is notable about Prince Edward Islands size compared to the other Canadian provinces?', ['It became Canadas smallest province by area', 'It became Canadas largest province by area', 'It has no defined provincial boundaries', 'It is larger than every other Maritime province'], 0),
   ('Why is it historically significant that Prince Edward Island hosted the Charlottetown Conference but joined Confederation nearly a decade later?', ['It shows that hosting early discussions did not guarantee immediate agreement to join a national union', 'It proves that Prince Edward Island joined Confederation before any other province', 'It shows the conference had no connection to Confederation at all', 'Prince Edward Island was forced to join immediately after the conference'], 0)]),
]),
day(133, [
L('Reading: Determining Authors Purpose and Audience',
  'Grade 8 Language strand: authors purpose refers to the primary reason a text was written, commonly to inform, persuade, entertain, or express an idea, while considering the intended audience helps explain the choices an author makes about tone, vocabulary, and content.',
  [('What does authors purpose refer to?', ['The primary reason a text was written, such as to inform, persuade, or entertain', 'The exact number of pages in a text', 'The name of the publishing company', 'The font used to print a text'], 0),
   ('Which purpose best matches a newspaper editorial arguing for a new city policy?', ['To persuade', 'To entertain only', 'To provide step-by-step instructions', 'To express personal grief only'], 0),
   ('Why is identifying the intended audience of a text useful to a reader?', ['It helps explain choices the author made about tone, vocabulary, and content', 'Audience has no effect on how a text is written', 'Every text is written for exactly the same audience', 'Identifying audience prevents a reader from understanding a text'], 0),
   ('Which text is most likely written primarily to inform?', ['A textbook chapter explaining how volcanoes form', 'A humorous short story about talking animals', 'A persuasive campaign speech', 'A poem expressing personal sadness'], 0),
   ('Why might an author adjust their vocabulary and tone when writing for a younger audience compared to an expert audience?', ['Matching language to an audiences background knowledge helps ensure the message is understood clearly', 'Vocabulary and tone should never change based on audience', 'Younger audiences always require more complicated vocabulary', 'Audience awareness has no connection to effective communication'], 0)]),
M('Statistics: An Introduction to Confidence Intervals',
  'Grade 8 Math strand: a confidence interval is a range of values, calculated from sample data, that is likely to contain the true value of a population parameter, with a stated confidence level such as ninety-five percent describing how reliable the estimate is.',
  [('What does a confidence interval provide?', ['A range of values likely to contain the true population parameter', 'A single exact value with no range at all', 'A list of every possible outcome in a population', 'A guarantee that a sample is completely error-free'], 0),
   ('What does a ninety-five percent confidence level generally describe?', ['The reliability of the method used to estimate the interval across repeated sampling', 'That there is a ninety-five percent chance the interval is exactly wrong', 'That only five percent of the population was studied', 'That the sample size must always equal ninety-five'], 0),
   ('Why might a wider confidence interval be considered less precise than a narrower one?', ['A wider range gives less specific information about where the true value likely falls', 'A wider interval always gives more precise information', 'Interval width has no connection to precision', 'Narrower intervals are always considered unreliable'], 0),
   ('What sample characteristic often affects the width of a confidence interval?', ['Sample size, since larger samples generally produce narrower intervals', 'The colour used to display the data', 'The day of the week the data was collected', 'The alphabetical order of the data values'], 0),
   ('Why are confidence intervals useful in scientific research and polling?', ['They allow researchers to express both an estimate and a measure of its uncertainty', 'They eliminate the need for any sample data', 'Confidence intervals are never used in real research', 'They provide no information about the reliability of an estimate'], 0)]),
Sc('The Lymphatic System and Fluid Balance',
   'Grade 8 Science strand: the lymphatic system is a network of vessels and nodes that collects excess fluid from body tissues, filters out pathogens and debris, and returns the fluid to the bloodstream, working closely with the immune system to fight infection.',
   [('What is the main function of the lymphatic system?', ['To collect excess fluid from tissues and return it to the bloodstream', 'To pump blood throughout the entire body', 'To digest food in the stomach', 'To produce sound for speech'], 0),
    ('What role do lymph nodes play in the body?', ['They filter lymph fluid and help trap pathogens and debris', 'They store excess bone marrow exclusively', 'They regulate body temperature directly', 'They have no connection to the immune system'], 0),
    ('How is the lymphatic system connected to the immune system?', ['It helps transport and filter fluid containing white blood cells that fight infection', 'The two systems operate in complete isolation from each other', 'The lymphatic system destroys the immune system', 'White blood cells are never found in lymphatic fluid'], 0),
    ('What might happen if excess fluid was not properly collected and returned to the bloodstream?', ['Swelling, known as edema, could occur in body tissues', 'The body would produce more bones instantly', 'Muscles would immediately become stronger', 'Blood pressure would always drop to zero'], 0),
    ('Why is the lymphatic system considered essential to maintaining fluid balance in the body?', ['It prevents fluid from building up excessively in tissues while also supporting immune defense', 'It has no role in maintaining any bodily balance', 'Fluid balance is controlled entirely by the skeletal system', 'The lymphatic system only operates during illness'], 0)]),
H('The Manitoba Act of 1870 and the Creation of Manitoba',
  'Grade 8 History strand: the Manitoba Act of 1870, passed following the Red River Resistance, created the province of Manitoba and included protections for the French language and Roman Catholic schools, reflecting the influence of the Metis-led provisional government.',
  [('What did the Manitoba Act of 1870 create?', ['The province of Manitoba', 'The province of Saskatchewan', 'The North-West Territories', 'The province of British Columbia'], 0),
   ('What earlier event directly led to the passing of the Manitoba Act?', ['The Red River Resistance', 'The Cypress Hills Massacre', 'The Pacific Scandal', 'The Klondike Gold Rush'], 0),
   ('What protections did the Manitoba Act originally include?', ['Protections for the French language and Roman Catholic schools', 'A ban on all religious institutions', 'A guarantee of free railway travel for all residents', 'The abolition of provincial governments'], 0),
   ('Whose influence helped shape the terms included in the Manitoba Act?', ['The Metis-led provisional government', 'A provisional government led entirely by British officials', 'The government of the United States', 'A provisional government with no connection to the Red River settlement'], 0),
   ('Why is the Manitoba Act considered historically significant?', ['It marked the first time a new province was created largely due to negotiations led by a Metis political movement', 'It had no lasting effect on Canadian provincial boundaries', 'It abolished the existing Red River settlement entirely', 'It prevented any new provinces from ever being created'], 0)]),
]),
day(134, [
L('Writing: Crafting a Strong Introduction and Hook',
  'Grade 8 Language strand: an effective introduction paragraph captures a readers attention with a hook, such as a surprising fact, question, or anecdote, and then narrows toward a clear thesis statement that previews the focus of the piece.',
  [('What is the purpose of a hook in an introduction paragraph?', ['To capture the readers attention at the very start of a piece of writing', 'To summarize the entire essay in one sentence', 'To conclude the argument before it begins', 'To list every source used in the essay'], 0),
   ('Which of these is an example of an effective hook?', ['A surprising statistic related to the essays topic', 'A random sentence unrelated to the topic', 'The final sentence of the conclusion', 'A list of unrelated vocabulary words'], 0),
   ('What should an introduction paragraph typically narrow toward by its final sentence?', ['A clear thesis statement previewing the focus of the piece', 'A completely unrelated new topic', 'A restatement of the hook with no further detail', 'A list of grammar rules'], 0),
   ('Why might a writer use a question as a hook?', ['A thought-provoking question can immediately engage a readers curiosity', 'Questions always confuse readers and should be avoided', 'Hooks are never allowed to be phrased as questions', 'Questions have no effect on reader engagement'], 0),
   ('Why is a strong introduction important for the rest of an essay?', ['It sets the tone and direction for the piece, helping readers understand what to expect', 'Introductions have no influence on how a reader understands an essay', 'A weak introduction always improves an essays overall quality', 'Readers never form an impression based on an introduction'], 0)]),
M('Algebra: An Introduction to Inverse Matrices',
  'Grade 8 Math strand: an inverse matrix, when multiplied by its original matrix, produces the identity matrix, and only square matrices with a nonzero determinant have an inverse, a property that allows systems of equations to be solved using matrix methods.',
  [('What does multiplying a matrix by its inverse produce?', ['The identity matrix', 'A matrix of all zeros', 'The original matrix squared', 'A matrix with no defined values'], 0),
   ('What type of matrix can have an inverse?', ['A square matrix with a nonzero determinant', 'Any matrix regardless of its dimensions', 'Only matrices containing solely negative numbers', 'Only matrices with a determinant equal to zero'], 0),
   ('What happens if a square matrixs determinant equals zero?', ['The matrix does not have an inverse', 'The matrix automatically becomes the identity matrix', 'The matrix always has exactly two inverses', 'The matrix becomes a scalar value instead'], 0),
   ('How can inverse matrices be used to solve a system of linear equations?', ['By multiplying the inverse of the coefficient matrix by the constant matrix', 'Inverse matrices can never be used to solve any equation', 'By always ignoring the coefficients entirely', 'By converting every equation into a single fraction'], 0),
   ('Why are inverse matrices useful in fields like computer graphics and engineering?', ['They allow transformations and systems of equations to be reversed or solved efficiently', 'Inverse matrices have no practical applications', 'Computer graphics never use matrix operations', 'Engineering problems can never involve matrices'], 0)]),
Sc('The Physics of Levers and Mechanical Torque',
   'Grade 8 Science strand: a lever is a simple machine that pivots around a fixed point called a fulcrum, and torque describes the rotational force produced when an applied force acts at a distance from that pivot point, allowing levers to multiply force.',
   [('What is the fixed point around which a lever pivots called?', ['The fulcrum', 'The axis', 'The load', 'The joint'], 0),
    ('What does torque describe?', ['The rotational force produced when a force acts at a distance from a pivot point', 'The total weight of an object at rest', 'The colour of a machine part', 'The temperature of a moving object'], 0),
    ('How can a lever help multiply the force applied by a person?', ['By positioning the fulcrum so a small input force can move a much larger load', 'Levers can never multiply any applied force', 'By eliminating the need for a fulcrum entirely', 'By reducing the distance between the force and the load to zero'], 0),
    ('What happens to the torque produced if the distance from the fulcrum to the applied force increases, while the force stays the same?', ['The torque increases', 'The torque always decreases', 'The torque becomes exactly zero', 'Torque is unaffected by distance from the fulcrum'], 0),
    ('Why are levers considered one of the fundamental simple machines studied in physics?', ['They demonstrate how force, distance, and a pivot point can work together to make tasks easier', 'Levers have no practical use in real machines', 'Levers require electricity to function', 'Levers only exist as abstract mathematical ideas with no physical form'], 0)]),
H('The British North America Act of 1867 and Canadas Constitution',
  'Grade 8 History strand: the British North America Act of 1867, passed by the British Parliament, formally created the Dominion of Canada by uniting the Province of Canada, Nova Scotia, and New Brunswick, and served as Canadas primary constitutional document until it was patriated and renamed in 1982.',
  [('What did the British North America Act of 1867 formally create?', ['The Dominion of Canada', 'The province of Manitoba', 'The North-West Territories', 'The Supreme Court of Canada'], 0),
   ('Which three colonies were united by the British North America Act?', ['The Province of Canada, Nova Scotia, and New Brunswick', 'British Columbia, Alberta, and Saskatchewan', 'Manitoba, Ontario, and Quebec', 'Prince Edward Island, Newfoundland, and Manitoba'], 0),
   ('Which government body passed the British North America Act?', ['The British Parliament', 'The Canadian House of Commons', 'The government of the United States', 'The Supreme Court of Canada'], 0),
   ('What eventually happened to the British North America Act in 1982?', ['It was patriated and renamed as part of Canadas Constitution', 'It was completely repealed with no replacement', 'It was transferred to the United States government', 'It was renamed the Numbered Treaties'], 0),
   ('Why is the British North America Act considered a foundational document in Canadian history?', ['It established the legal and constitutional framework for Canada as a self-governing dominion', 'It had no lasting legal significance for Canada', 'It only applied to a single Canadian city', 'It prevented Canada from ever expanding its territory'], 0)]),
]),
day(135, [
L('Media Literacy: Media Ownership and Consolidation',
  'Grade 8 Language strand: media ownership refers to the companies or individuals who control newspapers, television stations, and online platforms, and consolidation occurs when a small number of large corporations own many different media outlets, which can influence the range of perspectives an audience encounters.',
  [('What does media ownership refer to?', ['The companies or individuals who control media outlets such as newspapers or television stations', 'The number of employees at a single company', 'The physical size of a broadcasting building', 'The colour scheme used on a website'], 0),
   ('What is media consolidation?', ['When a small number of large corporations come to own many different media outlets', 'When every media outlet is owned by a separate individual', 'When governments ban all private media ownership', 'When media companies stop producing any content'], 0),
   ('Why might media consolidation affect the range of perspectives an audience encounters?', ['Fewer owners controlling more outlets can lead to less diversity in viewpoints being presented', 'Consolidation always increases the diversity of viewpoints presented', 'Ownership has no connection to the perspectives shared in media', 'Every media company presents identical content regardless of ownership'], 0),
   ('Why might a critical media consumer research who owns a news outlet?', ['Understanding ownership can help reveal potential biases or interests shaping the content', 'Ownership information is never relevant to understanding bias', 'Researching ownership always confuses a reader further', 'This information has no connection to fact-checking'], 0),
   ('Why is media literacy regarding ownership considered important in a democratic society?', ['A healthy variety of independently owned media sources can support access to diverse information and viewpoints', 'Democratic societies function better with a single media owner', 'Media ownership has no connection to the flow of information', 'Diverse ownership always leads to less accurate reporting'], 0)]),
M('Trigonometry: Graphing Sine and Cosine Functions',
  'Grade 8 Math strand: the graphs of sine and cosine functions form smooth, repeating waves with a defined amplitude, period, and midline, describing periodic behaviour that appears in contexts ranging from sound waves to seasonal temperature changes.',
  [('What shape do the graphs of sine and cosine functions form?', ['A smooth, repeating wave', 'A straight line', 'A single closed circle', 'A jagged, non-repeating zigzag'], 0),
   ('What term describes the maximum height a sine or cosine graph reaches above its midline?', ['Amplitude', 'Period', 'Frequency', 'Radius'], 0),
   ('What term describes the horizontal length of one complete cycle of a sine or cosine graph?', ['Period', 'Amplitude', 'Midline', 'Domain'], 0),
   ('What is the standard period of the basic sine and cosine functions, measured in radians?', ['Two pi', 'Pi divided by two', 'One radian', 'Ninety radians'], 0),
   ('Why are sine and cosine graphs useful for modeling real-world phenomena like sound waves or seasonal temperatures?', ['Their repeating, wave-like pattern closely matches naturally periodic behaviour', 'These graphs never repeat and cannot model periodic behaviour', 'Sound waves and temperatures never follow any repeating pattern', 'Sine and cosine functions can only describe straight-line motion'], 0)]),
Sc('Genetics: The Structure and Function of Chromosomes',
   'Grade 8 Science strand: chromosomes are tightly coiled structures made of DNA and protein found in the nucleus of a cell, with humans typically carrying twenty-three pairs, and they organize genetic information so it can be accurately copied and passed on during cell division.',
   [('What are chromosomes made of?', ['DNA and protein', 'Only water and salt', 'Only carbohydrates', 'Only red blood cells'], 0),
    ('Where in the cell are chromosomes typically found?', ['In the nucleus', 'In the cell membrane only', 'In the mitochondria only', 'Outside the cell entirely'], 0),
    ('How many pairs of chromosomes do humans typically carry?', ['Twenty-three pairs', 'Ten pairs', 'Forty-six individual unpaired chromosomes with no pairing', 'Twelve pairs'], 0),
    ('What is the main function of chromosomes during cell division?', ['To organize genetic information so it can be accurately copied and passed on', 'To destroy genetic information before division occurs', 'Chromosomes play no role in cell division', 'To convert genetic information into energy'], 0),
    ('Why is the tightly coiled structure of a chromosome important?', ['It allows a large amount of DNA to be compactly stored and organized within a small cell nucleus', 'Coiling has no effect on how DNA is stored', 'A tightly coiled structure prevents DNA from ever being used by the cell', 'Chromosomes are never coiled under any circumstances'], 0)]),
H('Sir John A. Macdonald: Canadas First Prime Minister',
  'Grade 8 History strand: Sir John A. Macdonald served as Canadas first prime minister following Confederation in 1867 and again in later years, playing a central role in national expansion projects such as the transcontinental railway while also being associated with controversial policies toward Indigenous peoples.',
  [('What position did Sir John A. Macdonald hold following Confederation in 1867?', ['Canadas first prime minister', 'Governor General of Canada', 'Premier of Ontario', 'Chief Justice of the Supreme Court'], 0),
   ('What major national infrastructure project is Macdonald closely associated with?', ['The transcontinental railway', 'The Trans-Canada Highway', 'The St. Lawrence Seaway', 'The Canadian National Railway of the 1920s'], 0),
   ('Besides his role in national expansion, what controversial aspect of Macdonalds legacy do historians also examine?', ['Policies that caused significant harm to Indigenous peoples', 'A complete absence of any controversial policies', 'Policies that had no effect on Indigenous communities', 'An exclusive focus on international trade with no domestic policy'], 0),
   ('Why is studying leaders like Macdonald important for understanding Canadian history critically?', ['It allows students to examine both nation-building achievements and harmful consequences of the same era', 'Historical figures should only ever be studied in a purely positive light', 'Critical examination has no value when studying history', 'Macdonalds policies had no lasting impact on Canada'], 0),
   ('Why is Macdonalds role in Confederation and expansion considered historically significant?', ['He helped shape the political structure and territorial growth of Canada in its earliest decades', 'He played no role in any Confederation-era events', 'Macdonald opposed the expansion of Canadian territory', 'He served only a single day as prime minister'], 0)]),
]),
day(136, [
L('Reading: Analyzing Cause and Effect Structures in Nonfiction',
  'Grade 8 Language strand: a cause and effect structure in nonfiction writing explains why an event happened and what resulted from it, often signaled by words such as because, therefore, consequently, and as a result, helping readers understand relationships between ideas.',
  [('What does a cause and effect structure explain in a nonfiction text?', ['Why an event happened and what resulted from it', 'The exact chronological order of unrelated events', 'A list of characters and their traits', 'A comparison between two unrelated topics'], 0),
   ('Which signal word often indicates a cause and effect relationship?', ['Consequently', 'Meanwhile', 'Similarly', 'Nevertheless'], 0),
   ('Why might an author use a cause and effect structure to organize an informational text?', ['It helps readers clearly understand how one event or condition leads to another', 'This structure always confuses readers with no benefit', 'Cause and effect structures are only used in fictional stories', 'This structure removes all logical connections between ideas'], 0),
   ('Which sentence demonstrates a clear cause and effect relationship?', ['Because the bridge was poorly maintained, it eventually collapsed', 'The bridge was built in 1950 and painted blue', 'The bridge is located near a river and a forest', 'The bridge has four lanes and two sidewalks'], 0),
   ('Why is recognizing cause and effect structures a useful nonfiction reading skill?', ['It helps readers evaluate whether an author has provided a logical explanation for an event', 'This skill has no connection to reading comprehension', 'Cause and effect relationships are never found in real texts', 'Recognizing this structure prevents readers from understanding a text at all'], 0)]),
M('Geometry: An Introduction to Parametric Equations',
  'Grade 8 Math strand: parametric equations describe the x and y coordinates of a curve separately in terms of a third variable, usually called a parameter such as t, allowing motion and complex curves to be modeled more flexibly than with a single equation in x and y.',
  [('What do parametric equations describe?', ['The x and y coordinates of a curve separately in terms of a third variable', 'Only a single fixed point with no motion', 'The area of a two-dimensional shape only', 'A relationship with no connection to coordinates'], 0),
   ('What is the third variable commonly used in parametric equations often called?', ['The parameter', 'The determinant', 'The radius', 'The coefficient'], 0),
   ('Why might parametric equations be useful for describing the motion of an object over time?', ['They can show how both position coordinates change independently as the parameter, often representing time, increases', 'They can only describe objects that never move', 'Parametric equations have no connection to motion', 'They eliminate the need to track more than one coordinate ever'], 0),
   ('How do parametric equations differ from a single equation written only in terms of x and y?', ['They separate x and y into two equations, both defined using an additional parameter', 'Parametric equations always combine x and y into a single unsolvable term', 'They cannot be graphed on a coordinate plane', 'They are identical in every way to a standard single equation'], 0),
   ('Why are parametric equations especially useful for modeling curves that a simple function of x cannot represent, such as a circle?', ['They can describe curves where a single x-value corresponds to more than one y-value', 'Parametric equations can never be used to describe a circle', 'Every curve can already be described easily using a single function of x', 'Parametric equations only apply to straight lines'], 0)]),
Sc('Renewable Energy: Solar Panels and Photovoltaic Cells',
   'Grade 8 Science strand: solar panels use photovoltaic cells to convert sunlight directly into electricity, a process that relies on light-sensitive materials such as silicon releasing electrons when struck by photons, offering a renewable alternative to fossil fuel energy sources.',
   [('What do photovoltaic cells convert into electricity?', ['Sunlight', 'Wind', 'Geothermal heat', 'Ocean waves'], 0),
    ('What light-sensitive material is commonly used in photovoltaic cells?', ['Silicon', 'Iron', 'Copper wire only', 'Rubber'], 0),
    ('What happens at the atomic level when light strikes a photovoltaic cell?', ['Photons cause electrons in the material to be released, generating an electric current', 'The material instantly melts with no electrical effect', 'Light has no interaction with the materials electrons', 'The cell absorbs sound waves instead of light'], 0),
    ('Why are solar panels considered a renewable energy source?', ['Sunlight is a naturally replenished resource that will not run out on a human timescale', 'Solar panels rely on burning fossil fuels', 'Sunlight is a limited resource that will soon be exhausted', 'Renewable energy sources always require fossil fuel backup'], 0),
    ('Why might a community choose to install solar panels instead of relying solely on fossil fuels?', ['Solar energy produces electricity without releasing the greenhouse gases associated with burning fossil fuels', 'Solar panels produce more greenhouse gases than coal plants', 'Fossil fuels are considered a renewable resource', 'Solar panels cannot generate any usable electricity'], 0)]),
H('The Formation of the Supreme Court of Canada in 1875',
  'Grade 8 History strand: the Supreme Court of Canada was established in 1875 as the countrys highest court of appeal, though for several decades afterward its rulings could still be appealed to a British court, reflecting Canadas gradual path toward full legal independence.',
  [('In what year was the Supreme Court of Canada established?', ['1875', '1867', '1920', '1982'], 0),
   ('What role does the Supreme Court of Canada serve?', ['The countrys highest court of appeal', 'A provincial trial court only', 'An international trade tribunal', 'A police oversight agency'], 0),
   ('For several decades after 1875, where could Supreme Court of Canada rulings still be appealed?', ['A British court', 'A court in the United States', 'A United Nations tribunal', 'No further appeal was ever possible after 1875'], 0),
   ('What does the continued ability to appeal to a British court reveal about Canada in the late 1800s?', ['Canada had not yet achieved full legal independence from Britain', 'Canada was already completely independent from Britain by 1875', 'Britain had no remaining legal connection to Canada', 'Canada had no court system of its own at the time'], 0),
   ('Why is the establishment of the Supreme Court of Canada considered an important step in Canadian legal history?', ['It created a national judicial institution that would eventually become the final legal authority in the country', 'It had no lasting impact on the Canadian legal system', 'The Supreme Court was abolished shortly after being created', 'It transferred all legal power permanently to Britain'], 0)]),
]),
day(137, [
L('Grammar: Pronoun-Antecedent Agreement and Clarity',
  'Grade 8 Language strand: pronoun-antecedent agreement requires that a pronoun match the number and gender of the noun it replaces, and unclear antecedents, where it is uncertain which noun a pronoun refers to, can confuse a reader about a sentences meaning.',
  [('What must a pronoun agree with according to pronoun-antecedent agreement?', ['The number and gender of the noun it replaces', 'The verb tense used earlier in the paragraph', 'The total number of sentences in a paragraph', 'The punctuation mark that follows it'], 0),
   ('Which sentence uses a pronoun that clearly agrees with its antecedent?', ['The dog wagged its tail happily.', 'The dog wagged their tail happily.', 'The dog wagged his tails happily.', 'The dogs wagged its tail happily.'], 0),
   ('What is an unclear antecedent?', ['A situation where it is uncertain which noun a pronoun refers to', 'A pronoun that always refers to the nearest verb', 'A sentence with no punctuation at all', 'A noun that never has a matching pronoun'], 0),
   ('Why can an unclear antecedent confuse a reader?', ['The reader may not be able to tell which noun the pronoun is meant to replace', 'Unclear antecedents always make a sentence easier to understand', 'Antecedents have no connection to pronoun meaning', 'Readers never notice unclear antecedents in a text'], 0),
   ('Why is pronoun-antecedent agreement important in formal writing?', ['It helps ensure that sentences are clear and free of confusing ambiguity', 'Agreement errors always make writing more precise', 'Formal writing never uses pronouns', 'This concept has no connection to clarity in writing'], 0)]),
M('Algebra: Solving Exponential and Logarithmic Equations',
  'Grade 8 Math strand: exponential equations, where a variable appears in the exponent, are often solved by rewriting both sides with a common base or by applying a logarithm to both sides, since logarithms and exponents are inverse operations of one another.',
  [('Where does the variable appear in an exponential equation?', ['In the exponent', 'Only in the base', 'Only in a coefficient', 'Exponential equations never contain a variable'], 0),
   ('What is one common strategy for solving an exponential equation?', ['Rewriting both sides of the equation with a common base', 'Removing all exponents from the equation entirely', 'Always ignoring the exponent and solving the base alone', 'Converting the equation into a fraction with no exponent'], 0),
   ('Why can logarithms be used to help solve exponential equations?', ['Logarithms and exponents are inverse operations of each other', 'Logarithms and exponents are entirely unrelated operations', 'Logarithms can only be applied to linear equations', 'Exponential equations can never be solved using logarithms'], 0),
   ('If two to the power of x equals eight, what is the value of x?', ['3', '2', '4', '8'], 0),
   ('Why are exponential and logarithmic equations important in real-world applications such as population growth or radioactive decay?', ['Many natural processes grow or shrink at rates proportional to their current size, which exponential functions model directly', 'Exponential functions never apply to any real-world process', 'Population growth and radioactive decay always follow a straight-line pattern', 'Logarithms have no real-world applications whatsoever'], 0)]),
Sc('The Human Ear and the Mechanics of Hearing',
   'Grade 8 Science strand: the human ear converts sound waves into electrical signals the brain can interpret, with the outer ear channeling sound to the eardrum, tiny bones in the middle ear amplifying the vibrations, and the inner ear translating them into nerve impulses.',
   [('What is the main function of the human ear?', ['To convert sound waves into signals the brain can interpret', 'To filter air before it reaches the lungs', 'To regulate body temperature', 'To produce saliva for digestion'], 0),
    ('What part of the ear does incoming sound first reach?', ['The outer ear', 'The inner ear', 'The brain directly', 'The eardrum before the outer ear'], 0),
    ('What happens at the eardrum when sound waves reach it?', ['It vibrates in response to the sound waves', 'It produces new sound waves independently', 'It absorbs all sound with no vibration', 'It converts sound directly into light'], 0),
    ('What is the role of the tiny bones in the middle ear?', ['To amplify the vibrations from the eardrum', 'To digest food particles', 'To filter dust from the air', 'To store excess fluid only'], 0),
    ('How does the inner ear contribute to hearing?', ['It translates vibrations into nerve impulses that travel to the brain', 'It has no role in the process of hearing', 'It converts nerve impulses back into sound waves', 'It stores sound permanently with no further processing'], 0)]),
H('The Creation of the North-West Territories and Territorial Government',
  'Grade 8 History strand: the North-West Territories were formally organized in 1870 to govern the vast lands acquired from the Hudsons Bay Company, and a territorial government was gradually established to administer the region before parts of it were later carved into new provinces.',
  [('In what year were the North-West Territories formally organized?', ['1870', '1867', '1905', '1920'], 0),
   ('From which company were the lands making up the North-West Territories acquired?', ['The Hudsons Bay Company', 'The Canadian Pacific Railway', 'The British East India Company', 'The North-West Mounted Police'], 0),
   ('What was the purpose of establishing a territorial government in the North-West Territories?', ['To administer and govern the vast newly acquired region', 'To immediately grant the region full provincial status', 'To transfer control of the region to the United States', 'To dissolve all existing Indigenous governance structures with no new administration'], 0),
   ('What eventually happened to parts of the North-West Territories in the following decades?', ['They were carved into new provinces, such as Manitoba, Alberta, and Saskatchewan', 'They remained completely unchanged for the next two centuries', 'They were returned entirely to the Hudsons Bay Company', 'They became part of the United States'], 0),
   ('Why is the organization of the North-West Territories considered an important step in Canadian expansion?', ['It established a framework for governing and eventually settling a vast portion of Canadian land', 'It had no connection to the later creation of new provinces', 'The territories were never actually governed by Canada', 'It marked the end of all Canadian westward expansion'], 0)]),
]),
day(138, [
L('Vocabulary: Regionalisms and Dialect in Literature',
  'Grade 8 Language strand: a regionalism is a word, phrase, or pronunciation specific to a particular geographic area, and authors often use dialect and regionalisms in dialogue to establish a characters background, setting, or cultural identity.',
  [('What is a regionalism?', ['A word, phrase, or pronunciation specific to a particular geographic area', 'A word used identically in every region of the world', 'A citation style used in essays', 'A grammatical rule about verb tense'], 0),
   ('Why might an author include dialect in a characters dialogue?', ['To establish the characters background, setting, or cultural identity', 'Dialect never has any purpose in dialogue', 'Authors are required to remove all dialect from dialogue', 'Dialect always confuses readers with no benefit to the story'], 0),
   ('Which of these is an example of a regionalism?', ['Using the word pop to mean a carbonated soft drink in some regions', 'Using standard grammar identical everywhere', 'A word invented entirely for a fantasy novel', 'A punctuation mark used in formal writing'], 0),
   ('Why might reading literature containing regionalisms and dialect be a valuable experience for readers?', ['It exposes readers to the diversity of language use across different communities and cultures', 'It has no educational value for readers', 'Regionalisms always make a text impossible to understand', 'Every region of the world uses identical language patterns'], 0),
   ('Why do authors sometimes balance authentic dialect with readability in their writing?', ['To capture a characters voice while still allowing a broad audience to understand the text', 'Readability is never a consideration for authors', 'Dialect must always be written exactly as spoken with no adjustment', 'Authentic dialect always makes a text completely unreadable'], 0)]),
M('Statistics: An Introduction to Chi-Square Tests',
  'Grade 8 Math strand: a chi-square test is a statistical method used to determine whether observed categorical data differs significantly from what would be expected, commonly applied to compare observed frequencies against a predicted distribution.',
  [('What type of data is commonly analyzed using a chi-square test?', ['Categorical data', 'Only continuous measurement data', 'Only data with negative values', 'Only data collected from a single individual'], 0),
   ('What does a chi-square test help determine?', ['Whether observed data differs significantly from expected data', 'The exact mean of a data set', 'The slope of a line of best fit', 'The volume of a three-dimensional solid'], 0),
   ('What two sets of values are typically compared in a chi-square test?', ['Observed frequencies and expected frequencies', 'Only two unrelated random numbers', 'The mean and the median of a data set', 'The largest and smallest values in a data set'], 0),
   ('Why might a researcher use a chi-square test when studying survey results?', ['To check whether differences between groups in the survey are statistically significant or simply due to chance', 'To calculate the average age of survey respondents', 'Chi-square tests are never used with survey data', 'To determine the exact wording of survey questions'], 0),
   ('Why is the chi-square test considered a useful tool in fields like biology and social science?', ['It provides a structured way to evaluate whether categorical patterns in data are meaningful', 'It has no application outside of pure mathematics', 'Chi-square tests can only be used with exactly two categories', 'The test eliminates the need for collecting any data at all'], 0)]),
Sc('Freshwater Ecosystems: Lakes, Rivers, and Wetlands',
   'Grade 8 Science strand: freshwater ecosystems, including lakes, rivers, and wetlands, support a wide diversity of plant and animal life adapted to varying water flow, depth, and nutrient levels, and are essential for filtering water and supporting biodiversity.',
   [('Which of these is an example of a freshwater ecosystem?', ['A wetland', 'A coral reef', 'The open ocean', 'A saltwater estuary exclusively'], 0),
    ('What environmental factors can vary significantly among different freshwater ecosystems?', ['Water flow, depth, and nutrient levels', 'Only air temperature above the water', 'Only the colour of the surrounding rocks', 'Freshwater ecosystems never vary in any way'], 0),
    ('Why are wetlands often considered important for filtering water?', ['Wetland vegetation and soil can trap sediment and absorb excess nutrients before water moves downstream', 'Wetlands always add pollutants directly into water sources', 'Wetlands have no effect on water quality', 'Filtering water is a function unique to oceans'], 0),
    ('Why do rivers typically support different species than still, slow-moving lakes?', ['Organisms in rivers are often adapted to flowing water, while lake organisms are adapted to calmer conditions', 'Rivers and lakes always contain identical species with no adaptation differences', 'Rivers never support any form of life', 'Lakes always have faster-moving water than rivers'], 0),
    ('Why are healthy freshwater ecosystems considered essential to biodiversity?', ['They provide habitat and resources for a wide range of plants, animals, and other organisms', 'Freshwater ecosystems have no connection to biodiversity', 'Only ocean ecosystems support biodiversity', 'Freshwater ecosystems are entirely lifeless environments'], 0)]),
H('Wilfrid Laurier and the Growth of Canada in the Early 1900s',
  'Grade 8 History strand: Sir Wilfrid Laurier, who served as prime minister from 1896 to 1911, presided over a period of rapid economic growth, western settlement, and immigration, famously predicting that the twentieth century would belong to Canada.',
  [('During which years did Sir Wilfrid Laurier serve as prime minister?', ['1896 to 1911', '1867 to 1873', '1920 to 1930', '1939 to 1945'], 0),
   ('What famous prediction is associated with Wilfrid Laurier regarding Canadas future?', ['That the twentieth century would belong to Canada', 'That Canada would never grow beyond its 1867 borders', 'That Canada would remain a British colony forever', 'That immigration to Canada would end entirely'], 0),
   ('What economic and demographic trends characterized Canada during Lauriers time in office?', ['Rapid economic growth, western settlement, and immigration', 'A sharp economic decline with no growth', 'A ban on all immigration to Canada', 'The complete abandonment of the western provinces'], 0),
   ('Why was western settlement particularly significant during the Laurier era?', ['It helped populate the prairies and expand Canadas agricultural economy', 'Western settlement had no economic impact on Canada', 'The prairies were already fully settled before Lauriers term', 'Settlement efforts were focused entirely on eastern Canada'], 0),
   ('Why is Laurier considered an important figure in Canadian history?', ['His leadership coincided with significant national growth and helped shape Canadas early twentieth-century development', 'He played no role in shaping Canadian policy', 'Laurier opposed all forms of immigration and settlement', 'His time in office had no lasting effect on Canada'], 0)]),
]),
day(139, [
L('Writing: The Comparative Book Review',
  'Grade 8 Language strand: a comparative book review evaluates and contrasts two related texts, examining shared themes, differing authorial choices, and overall effectiveness, while supporting judgments with specific evidence drawn from both works.',
  [('What does a comparative book review primarily do?', ['Evaluate and contrast two related texts', 'Summarize a single text with no evaluation', 'List unrelated books with no analysis', 'Provide only biographical details about an author'], 0),
   ('What might a comparative book review examine between two texts?', ['Shared themes and differing authorial choices', 'Only the number of pages in each book', 'Only the price of each book', 'Only the publication date with no further analysis'], 0),
   ('Why is specific evidence important when writing a comparative book review?', ['Evidence supports the reviewers judgments and makes the analysis more convincing', 'Evidence is never necessary in a book review', 'Reviews should rely only on personal opinion with no support', 'Specific evidence always weakens an argument'], 0),
   ('What is one benefit of comparing two texts rather than reviewing just one?', ['It can reveal insights about each work that might not be as visible when read in isolation', 'Comparing texts never reveals any new insights', 'A single text always provides more insight than two combined', 'Comparisons are only useful for entirely unrelated texts'], 0),
   ('Why might a reviewer discuss differing authorial choices, such as tone or structure, between two texts?', ['Highlighting these differences can show how each author achieves a distinct effect on readers', 'Authorial choices never affect how a reader experiences a text', 'Tone and structure are irrelevant to a books overall effect', 'All authors make identical choices regardless of the text'], 0)]),
M('Geometry: An Introduction to Taxicab Geometry',
  'Grade 8 Math strand: taxicab geometry is a system of geometry where distance between two points is measured by adding the horizontal and vertical distances traveled along a grid, similar to how a taxi must travel along city blocks rather than in a straight line.',
  [('How is distance measured in taxicab geometry?', ['By adding the horizontal and vertical distances traveled along a grid', 'By measuring a straight diagonal line between two points', 'By counting only the number of turns made', 'By ignoring all vertical movement entirely'], 0),
   ('What everyday situation does taxicab geometry get its name from?', ['A taxi traveling along city blocks rather than in a straight line', 'A boat sailing directly across open water', 'An airplane flying in a straight line', 'A train traveling on a single fixed track'], 0),
   ('How does taxicab distance between two points typically compare to standard straight-line distance?', ['Taxicab distance is usually greater than or equal to the straight-line distance', 'Taxicab distance is always exactly equal to the straight-line distance', 'Taxicab distance is always shorter than the straight-line distance', 'The two distances have no mathematical relationship'], 0),
   ('In taxicab geometry, how would you find the distance between the points (0,0) and (3,4)?', ['Add the horizontal distance of 3 and the vertical distance of 4 to get 7', 'Multiply 3 and 4 to get 12', 'Take the square root of the sum of the squares to get 5', 'Subtract 3 from 4 to get 1'], 0),
   ('Why might taxicab geometry be useful for modeling real-world situations like city navigation?', ['Movement in a city grid is often restricted to horizontal and vertical paths along streets', 'City streets are always arranged in a single straight diagonal line', 'Taxicab geometry has no real-world applications', 'Standard straight-line distance always matches real city travel exactly'], 0)]),
Sc('Space Science: Comets, Asteroids, and Meteors',
   'Grade 8 Science strand: comets, asteroids, and meteors are distinct types of small celestial bodies within the solar system, with comets composed largely of ice and dust that form glowing tails near the sun, asteroids being rocky remnants mostly found in the asteroid belt, and meteors being the streaks of light produced when debris burns up in Earths atmosphere.',
   [('What are comets largely composed of?', ['Ice and dust', 'Solid iron only', 'Liquid water only', 'Pure hydrogen gas'], 0),
    ('Where are most asteroids in the solar system primarily found?', ['The asteroid belt', 'Deep within the sun', 'On the surface of the moon', 'Inside Earths atmosphere permanently'], 0),
    ('What causes a meteor to produce a visible streak of light in the sky?', ['Debris burning up as it enters Earths atmosphere', 'A permanent glow with no connection to the atmosphere', 'Reflected sunlight bouncing off the moon', 'An electrical storm within outer space'], 0),
    ('Why do comets often develop a glowing tail as they approach the sun?', ['Heat from the sun causes ice within the comet to vaporize, releasing gas and dust', 'Comets are ignited by nearby stars', 'Tails form only when comets are farthest from the sun', 'Comets have no connection to heat or the sun'], 0),
    ('What is the key difference between an asteroid and a meteor?', ['An asteroid is a rocky body orbiting in space, while a meteor is the light produced when debris burns in the atmosphere', 'Asteroids and meteors are simply two different names for the exact same object', 'Meteors are always larger than asteroids', 'Asteroids only exist within Earths atmosphere'], 0)]),
H('Alberta and Saskatchewan Join Confederation in 1905',
  'Grade 8 History strand: Alberta and Saskatchewan were carved out of the North-West Territories and became provinces in 1905, a change driven by rapid population growth from prairie settlement and immigration in the preceding decades.',
  [('In what year did Alberta and Saskatchewan become provinces?', ['1905', '1870', '1885', '1920'], 0),
   ('From which existing territory were Alberta and Saskatchewan carved out?', ['The North-West Territories', 'Manitoba', 'British Columbia', 'Quebec'], 0),
   ('What population trend helped drive the creation of Alberta and Saskatchewan as provinces?', ['Rapid population growth from prairie settlement and immigration', 'A significant population decline across the prairies', 'A ban on any further immigration to Canada', 'A sudden decrease in agricultural activity'], 0),
   ('Why might rapid population growth lead a territory to be reorganized into a full province?', ['A larger population often requires greater local political representation and self-government', 'Population growth has no connection to provincial status', 'Provinces are created only when population decreases', 'Territories automatically become provinces regardless of population'], 0),
   ('Why are 1905 events involving Alberta and Saskatchewan considered significant in Canadian history?', ['They marked a major expansion in the number of Canadian provinces and reflected the growth of the prairie region', 'These events had no lasting impact on Canadas provincial structure', 'Alberta and Saskatchewan later left Confederation entirely', 'The prairie region remained unpopulated well into the twentieth century'], 0)]),
]),
day(140, [
L('Language Review: Grammar, Vocabulary, and Purpose (Days 131-139)',
  'Grade 8 Language strand review: students revisit subject-verb agreement, oxymorons, authors purpose, introductions and hooks, media ownership, cause and effect structures, pronoun-antecedent agreement, regionalisms, and comparative book reviews.',
  [('What does subject-verb agreement require?', ['That a verb match its subject in number', 'That every sentence use a plural verb', 'That a sentence never contain a subject', 'That verbs always precede their subjects'], 0),
   ('What is an oxymoron?', ['A figure of speech that combines two contradictory terms for effect', 'A word that means the exact same thing when repeated', 'A citation style used in research papers', 'A grammatical rule about verb tense'], 0),
   ('What does authors purpose refer to?', ['The primary reason a text was written, such as to inform, persuade, or entertain', 'The exact number of pages in a text', 'The name of the publishing company', 'The font used to print a text'], 0),
   ('What does a cause and effect structure explain in a nonfiction text?', ['Why an event happened and what resulted from it', 'The exact chronological order of unrelated events', 'A list of characters and their traits', 'A comparison between two unrelated topics'], 0),
   ('What does a comparative book review primarily do?', ['Evaluate and contrast two related texts', 'Summarize a single text with no evaluation', 'List unrelated books with no analysis', 'Provide only biographical details about an author'], 0)]),
M('Math Review: Calculus, Statistics, and Geometry (Days 131-139)',
  'Grade 8 Math strand review: students revisit integrals, linear Diophantine equations, inverse matrices, parametric equations, and taxicab geometry.',
  [('What does a definite integral commonly represent?', ['The area between a curve and the x-axis over a given interval', 'The slope of a line at a single point', 'A fixed number unrelated to area', 'The perimeter of a shape'], 0),
   ('What distinguishes a Diophantine equation from a typical algebraic equation?', ['Only integer solutions are considered valid', 'Only decimal solutions are considered valid', 'The equation must always equal zero', 'The equation can never have more than one variable'], 0),
   ('What does multiplying a matrix by its inverse produce?', ['The identity matrix', 'A matrix of all zeros', 'The original matrix squared', 'A matrix with no defined values'], 0),
   ('What do parametric equations describe?', ['The x and y coordinates of a curve separately in terms of a third variable', 'Only a single fixed point with no motion', 'The area of a two-dimensional shape only', 'A relationship with no connection to coordinates'], 0),
   ('How is distance measured in taxicab geometry?', ['By adding the horizontal and vertical distances traveled along a grid', 'By measuring a straight diagonal line between two points', 'By counting only the number of turns made', 'By ignoring all vertical movement entirely'], 0)]),
Sc('Science Review: Body Systems, Physics, and Earth Science (Days 131-139)',
   'Grade 8 Science strand review: students revisit the muscular system, the lymphatic system, chromosomes, the human ear, and comets, asteroids, and meteors.',
   [('What are the three main types of muscle tissue in the body?', ['Skeletal, smooth, and cardiac muscle', 'Skeletal, elastic, and rigid muscle', 'Voluntary, involuntary, and stationary bone', 'Cardiac, digestive, and skeletal bone'], 0),
    ('What is the main function of the lymphatic system?', ['To collect excess fluid from tissues and return it to the bloodstream', 'To pump blood throughout the entire body', 'To digest food in the stomach', 'To produce sound for speech'], 0),
    ('What are chromosomes made of?', ['DNA and protein', 'Only water and salt', 'Only carbohydrates', 'Only red blood cells'], 0),
    ('What is the main function of the human ear?', ['To convert sound waves into signals the brain can interpret', 'To filter air before it reaches the lungs', 'To regulate body temperature', 'To produce saliva for digestion'], 0),
    ('What are comets largely composed of?', ['Ice and dust', 'Solid iron only', 'Liquid water only', 'Pure hydrogen gas'], 0)]),
H('History Review: Confederation Expansion and Institutions (Days 131-139)',
  'Grade 8 History strand review: students revisit British Columbia and Prince Edward Island joining Confederation, the Manitoba Act, the British North America Act, Sir John A. Macdonald, the Supreme Court of Canada, the North-West Territories, Wilfrid Laurier, and Alberta and Saskatchewan joining Confederation.',
  [('In what year did British Columbia join Confederation?', ['1871', '1867', '1905', '1949'], 0),
   ('What did the Manitoba Act of 1870 create?', ['The province of Manitoba', 'The province of Saskatchewan', 'The North-West Territories', 'The province of British Columbia'], 0),
   ('What position did Sir John A. Macdonald hold following Confederation in 1867?', ['Canadas first prime minister', 'Governor General of Canada', 'Premier of Ontario', 'Chief Justice of the Supreme Court'], 0),
   ('In what year were the North-West Territories formally organized?', ['1870', '1867', '1905', '1920'], 0),
   ('In what year did Alberta and Saskatchewan become provinces?', ['1905', '1870', '1885', '1920'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_131_140)
    append_to(8, g8_131_140)
