#!/usr/bin/env python3
"""Grade 8, Days 111-120 -- extends Grade 8 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade8.json)
extensively to avoid any overlap: emphatic pronouns and intensifiers,
onomatopoeia, juxtaposition, eyewitness news reports, memes and internet
culture, ellipsis and omission, hyperbole/understatement/paradox,
Freytag's Pyramid, euphemisms and doublespeak; vectors (dot product),
matrix multiplication and determinants, modular exponentiation and
cryptography basics, Bayes' Theorem, graph theory, the fundamental
theorem of algebra, De Moivre's Theorem, an introduction to limits, and
proof by mathematical induction; the integumentary system, the excretory
system, antibiotic resistance, the chemistry of fireworks, the physics of
rainbows and light dispersion, bird migration and animal navigation,
desert ecosystems, the physics of friction, and genetic engineering in
agriculture; the internment of Ukrainian Canadians during WWI,
Newfoundland joining Confederation in 1949, Canada's separate 1939
declaration of war, the National Policy of 1879, the Royal Commission on
Bilingualism and Biculturalism, the Manitoba Schools Question, Canada and
the League of Nations, the Alberta Social Credit movement, and the Paris
Peace Conference of 1919.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
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


g8_111_120 = [
day(111, [
L('Grammar: Emphatic Pronouns and Intensifiers',
  'Grade 8 Language strand: emphatic pronouns like myself or himself add emphasis to a noun already mentioned, while intensifiers such as very or extremely strengthen the meaning of an adjective or adverb.',
  [('What is the purpose of an emphatic pronoun?', ['To add emphasis to a noun or pronoun already mentioned', 'To replace a verb entirely', 'To act as a question word', 'To function as a preposition'], 0),
   ('Which sentence correctly uses an emphatic pronoun?', ['The principal herself announced the news.', 'The principal announced herself the news.', 'Herself the principal announced the news.', 'The principal announced the news herself very.'], 0),
   ('What is an intensifier?', ['A word that strengthens the meaning of an adjective or adverb', 'A word that replaces a noun', 'A punctuation mark', 'A type of conjunction'], 0),
   ('Which word functions as an intensifier in the sentence She was extremely tired?', ['Extremely', 'Was', 'She', 'Tired'], 0),
   ('Why should writers use intensifiers sparingly in formal writing?', ['Overusing them can weaken the precision and impact of the writing', 'Intensifiers always strengthen writing no matter how often used', 'Formal writing requires intensifiers in every sentence', 'Intensifiers are grammatically forbidden in all writing'], 0)]),
M('Geometry: Introduction to Vectors — Addition and the Dot Product',
  'Grade 8 Math strand: a vector has both magnitude and direction, vectors can be added by combining their components, and the dot product multiplies two vectors to produce a single scalar value.',
  [('What two properties does a vector have?', ['Magnitude and direction', 'Only magnitude', 'Only direction', 'Neither magnitude nor direction'], 0),
   ('How are two vectors typically added when given in component form?', ['By adding their corresponding components', 'By multiplying their magnitudes only', 'By ignoring direction entirely', 'By subtracting their directions'], 0),
   ('What does the dot product of two vectors produce?', ['A single scalar value', 'A new vector with a different direction only', 'A matrix', 'An imaginary number'], 0),
   ('If vector A = (2, 3) and vector B = (1, 4), what is A + B?', ['(3, 7)', '(2, 12)', '(1, 1)', '(3, 3)'], 0),
   ('Vectors are useful for representing real-world quantities such as ___.', ['Force and velocity, which have both size and direction', 'Only temperature, which has no direction', 'Only time, which has no direction', 'Only mass, which has no direction'], 0)]),
Sc('The Integumentary System: Skin, Hair, and Nails',
   'Grade 8 Science strand: the integumentary system, made up of skin, hair, and nails, protects the body from injury and infection, regulates temperature, and provides sensory information.',
   [('What organs make up the integumentary system?', ['Skin, hair, and nails', 'The heart and lungs', 'The stomach and intestines', 'The brain and spinal cord'], 0),
    ('What is one major function of the skin?', ['Protecting the body from injury and infection', 'Pumping blood throughout the body', 'Digesting food', 'Producing sound'], 0),
    ('How does the integumentary system help regulate body temperature?', ['Through sweating and blood vessel changes near the skins surface', 'By producing digestive enzymes', 'By filtering air in the lungs', 'It has no role in temperature regulation'], 0),
    ('What sensory information can skin provide?', ['Touch, pressure, and temperature', 'Taste only', 'Sound only', 'Balance only'], 0),
    ('Why is the integumentary system considered the bodys largest organ system?', ['Skin covers the entire external surface of the body', 'It is located only in one small area', 'It has no measurable size', 'It is smaller than a single cell'], 0)]),
H('The Internment of Ukrainian Canadians During World War I',
  'Grade 8 History strand: during World War I, thousands of Ukrainian Canadians and other Eastern Europeans were classified as enemy aliens and interned in camps, an event now recognized as a violation of civil liberties.',
  [('What happened to many Ukrainian Canadians during World War I?', ['They were classified as enemy aliens and interned in camps', 'They were granted full citizenship immediately', 'They were elected to Parliament', 'Nothing changed for them at all'], 0),
   ('Under what law were Ukrainian Canadians interned during WWI?', ['The War Measures Act', 'The Indian Act', 'The Canadian Bill of Rights', 'The Multiculturalism Act'], 0),
   ('How is the internment of Ukrainian Canadians viewed by historians today?', ['As a violation of civil liberties', 'As a completely justified wartime policy with no controversy', 'As an event that never actually happened', 'As a policy that benefited those interned'], 0),
   ('Which other group experienced a similar internment policy during a later war?', ['Japanese Canadians during World War II', 'French Canadians during the 1960s', 'British immigrants during the 1920s', 'American immigrants during the 1980s'], 0),
   ('Why do students study events like the Ukrainian Canadian internment today?', ['To understand the impact of wartime policies on civil rights', 'These events have no relevance to modern Canada', 'To celebrate the internment policy', 'Because no records of it exist'], 0)]),
]),
day(112, [
L('Vocabulary: Onomatopoeia and Sound Devices',
  'Grade 8 Language strand: onomatopoeia uses words that imitate sounds, such as crash or hiss, and is one of several sound devices, including alliteration and assonance, that writers use to create rhythm and imagery.',
  [('What is onomatopoeia?', ['Words that imitate the sounds they describe', 'A type of punctuation', 'A grammar rule about verb tense', 'A citation style'], 0),
   ('Which word is an example of onomatopoeia?', ['Hiss', 'Table', 'Quickly', 'Beautiful'], 0),
   ('What is alliteration, another common sound device?', ['The repetition of beginning consonant sounds in nearby words', 'A word that imitates a sound', 'A type of rhyme scheme only', 'A citation format'], 0),
   ('What is assonance?', ['The repetition of vowel sounds within nearby words', 'The repetition of consonant sounds at the start of words', 'A punctuation mark', 'A type of paragraph structure'], 0),
   ('Why do writers use sound devices like onomatopoeia and alliteration?', ['To create rhythm and vivid imagery in their writing', 'To make writing more difficult to understand on purpose', 'Sound devices have no effect on writing', 'To remove all imagery from a text'], 0)]),
M('Algebra: Matrix Multiplication and Determinants',
  'Grade 8 Math strand: matrix multiplication combines rows and columns of two matrices to produce a new matrix, and the determinant of a 2x2 matrix is a single value calculated from its entries that indicates properties like invertibility.',
  [('What is required to multiply two matrices together?', ['The number of columns in the first matrix must match the number of rows in the second', 'The matrices must always be the same size', 'Matrices can never be multiplied together', 'Only square matrices can exist'], 0),
   ('What does the determinant of a matrix indicate?', ['Properties of the matrix, such as whether it can be inverted', 'The exact size of the matrix only', 'The colour used to represent the matrix', 'Nothing useful about the matrix'], 0),
   ('For a 2x2 matrix with entries a, b, c, d, how is the determinant calculated?', ['ad minus bc', 'a plus b plus c plus d', 'a times b times c times d', 'a minus b minus c minus d'], 0),
   ('If a matrixs determinant is zero, what does this typically indicate?', ['The matrix cannot be inverted', 'The matrix is always square', 'The matrix has no entries', 'The matrix is always the identity matrix'], 0),
   ('Matrix multiplication and determinants are used in fields such as ___.', ['Computer graphics and solving systems of equations', 'Only cooking and recipes', 'Only music composition', 'Only weather forecasting'], 0)]),
Sc('The Excretory System: Kidneys and Waste Removal',
   'Grade 8 Science strand: the excretory system, especially the kidneys, filters waste products and excess water from the blood, producing urine and helping maintain the bodys internal balance.',
   [('What is the main function of the excretory system?', ['Filtering waste products and excess water from the blood', 'Pumping blood throughout the body', 'Digesting food in the stomach', 'Producing sound for speech'], 0),
    ('Which organs are the primary filters in the excretory system?', ['The kidneys', 'The lungs', 'The liver only', 'The heart'], 0),
    ('What waste product do the kidneys help remove from the body?', ['Urine, containing filtered waste and excess water', 'Only carbon dioxide', 'Only sweat', 'Only saliva'], 0),
    ('Why is maintaining fluid balance in the body important?', ['It supports proper function of cells and organs', 'Fluid balance has no effect on the body', 'The body never needs to balance fluids', 'Only muscles are affected by fluid balance'], 0),
    ('The excretory system works to keep the bodys internal environment ___.', ['Stable and balanced (homeostasis)', 'Constantly changing with no regulation', 'Completely dependent on outside temperature', 'Unrelated to overall health'], 0)]),
H('Newfoundland Joins Confederation in 1949',
  'Grade 8 History strand: Newfoundland became Canadas tenth province in 1949 after a close referendum vote, joining Confederation over 80 years after the original four provinces united in 1867.',
  [('In what year did Newfoundland join Confederation?', ['1949', '1867', '1905', '1999'], 0),
   ('How did Newfoundland decide to join Canada?', ['Through a close referendum vote', 'Through a unilateral government decision with no vote', 'Through a military conflict', 'Through a coin flip'], 0),
   ('What number province did Newfoundland become?', ['The tenth province', 'The first province', 'The fifth province', 'The last territory'], 0),
   ('How many years after the original Confederation of 1867 did Newfoundland join?', ['Over 80 years later', 'Immediately in 1867', 'Only 5 years later', 'Over 200 years later'], 0),
   ('Why is Newfoundlands entry into Confederation historically significant?', ['It completed a major stage of Canadas territorial expansion', 'It had no impact on Canadian history', 'It caused Canada to lose a province', 'It happened before Canada existed'], 0)]),
]),
day(113, [
L('Reading: Analyzing Juxtaposition and Contrast',
  'Grade 8 Language strand: juxtaposition places two contrasting elements side by side in a text, highlighting their differences and creating deeper meaning or emphasis for the reader.',
  [('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('What effect does juxtaposition typically create?', ['It highlights differences and creates deeper meaning', 'It removes all meaning from a text', 'It always confuses the reader with no purpose', 'It eliminates the need for description'], 0),
   ('Which is an example of juxtaposition?', ['Describing a wealthy neighbourhood right next to a description of poverty', 'Describing only one setting throughout a story', 'Listing facts with no comparison', 'Using only dialogue with no description'], 0),
   ('Why might an author use juxtaposition when introducing two characters?', ['To emphasize how different the characters are from each other', 'To make the characters seem identical', 'To avoid describing either character', 'To remove conflict from the story'], 0),
   ('Juxtaposition can be used to explore contrasts such as ___.', ['Wealth and poverty, or hope and despair', 'Only numbers and equations', 'Only weather patterns', 'Only geographic locations with no meaning'], 0)]),
M('Number Theory: Modular Exponentiation and Cryptography Basics',
  'Grade 8 Math strand: modular exponentiation raises a number to a power and then finds the remainder after dividing by a modulus, a key operation used in modern cryptography to keep digital information secure.',
  [('What does modular exponentiation calculate?', ['A number raised to a power, then reduced by a modulus', 'Only the square root of a number', 'The sum of two numbers', 'The average of a data set'], 0),
   ('Why is modular exponentiation important in modern technology?', ['It underlies cryptographic methods used to keep digital information secure', 'It has no practical use', 'It is only used in ancient mathematics with no modern application', 'It replaces the need for passwords entirely'], 0),
   ('What is 2 to the power of 5, mod 7?', ['4', '32', '0', '7'], 0),
   ('What does the term modulus refer to?', ['The number by which another number is divided to find the remainder', 'The final answer in any equation', 'A type of matrix', 'A type of vector'], 0),
   ('Cryptography uses mathematical operations like modular exponentiation to ___.', ['Encrypt and protect sensitive information', 'Make all information public and unprotected', 'Slow down computers intentionally', 'Remove the need for the internet'], 0)]),
Sc('Antibiotic Resistance: A Modern Challenge',
   'Grade 8 Science strand: antibiotic resistance occurs when bacteria evolve to survive medicines designed to kill them, a growing global health challenge driven partly by the overuse and misuse of antibiotics.',
   [('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'When a medicine works better over time', 'When a virus becomes weaker over time', 'When bacteria disappear completely'], 0),
    ('What is one major cause of increasing antibiotic resistance?', ['The overuse and misuse of antibiotics', 'Using antibiotics too rarely', 'Eating a balanced diet', 'Regular exercise'], 0),
    ('Why is antibiotic resistance considered a global health challenge?', ['It makes some bacterial infections much harder to treat', 'It has no effect on human health', 'It only affects animals, never humans', 'It makes all infections easier to cure'], 0),
    ('What can individuals do to help reduce antibiotic resistance?', ['Only take antibiotics when prescribed and finish the full course', 'Take antibiotics for every illness, including viral infections', 'Share leftover antibiotics with others', 'Stop taking antibiotics as soon as symptoms improve'], 0),
    ('Antibiotic resistance is an example of what broader biological process?', ['Natural selection acting on bacterial populations', 'A process unrelated to evolution', 'A process that only affects humans', 'A permanently fixed, unchanging trait'], 0)]),
H('Canadas Separate Declaration of War in 1939',
  'Grade 8 History strand: unlike in 1914, Canada made its own separate declaration of war against Germany in September 1939, a week after Britain, reflecting its growing independence in foreign affairs.',
  [('What did Canada do differently in 1939 compared to 1914 regarding war?', ['Canada made its own separate declaration of war', 'Canada refused to join the war at all', 'Canada declared war before Britain did', 'Canada had no role in the decision'], 0),
   ('Roughly how long after Britain did Canada declare war in 1939?', ['About a week later', 'The same exact day', 'Several years later', 'Canada never declared war'], 0),
   ('What does Canadas separate declaration of war reflect?', ['Its growing independence in foreign affairs', 'Its complete lack of independence from Britain', 'A decision made entirely by the United States', 'A refusal to participate in international conflict'], 0),
   ('In 1914, how did Canada enter World War I?', ['Automatically, because Britain was at war', 'Through a separate declaration like in 1939', 'Canada did not participate in World War I', 'Only after being invaded'], 0),
   ('Why is the 1939 declaration considered a milestone in Canadian history?', ['It showed Canada acting as an independent nation on the world stage', 'It reversed all previous Canadian independence', 'It made Canada part of a different country', 'It had no connection to Canadian sovereignty'], 0)]),
]),
day(114, [
L('Writing: Writing an Eyewitness News Report',
  'Grade 8 Language strand: an eyewitness news report presents a firsthand account of an event, combining factual details with vivid, sensory description to help readers understand what the writer observed.',
  [('What does an eyewitness news report present?', ['A firsthand account of an event', 'A purely fictional story', 'A summary of unrelated events', 'A persuasive argument with no facts'], 0),
   ('What should an eyewitness report combine with factual details?', ['Vivid, sensory description', 'Only technical jargon', 'Only statistics with no description', 'Random unrelated opinions'], 0),
   ('Why is sensory description important in an eyewitness report?', ['It helps readers understand what the writer actually observed', 'Description is never necessary in news writing', 'It replaces the need for any facts', 'It confuses the reader on purpose'], 0),
   ('Which is an example of strong eyewitness detail?', ['The smoke curled upward as sirens wailed in the distance.', 'An event occurred.', 'Something happened somewhere.', 'No details are available.'], 0),
   ('An eyewitness report differs from an opinion piece because it focuses on ___.', ['What the writer directly observed and experienced', 'Only the writers personal opinions with no facts', 'Predicting future events with no basis', 'Fictional characters and settings'], 0)]),
M('Probability: An Introduction to Bayes Theorem',
  'Grade 8 Math strand: Bayes Theorem updates the probability of an event based on new information, combining prior knowledge with new evidence to calculate a more accurate conditional probability.',
  [('What does Bayes Theorem help calculate?', ['An updated probability based on new evidence', 'A fixed probability that never changes', 'The average of a data set', 'The volume of a 3D shape'], 0),
   ('What two things does Bayes Theorem combine?', ['Prior knowledge and new evidence', 'Only random guesses', 'Only historical data with no update', 'Only geometric shapes'], 0),
   ('Bayes Theorem is closely related to which earlier probability concept?', ['Conditional probability', 'The Pythagorean theorem', 'Surface area', 'Linear equations'], 0),
   ('Why is Bayes Theorem useful in fields like medicine?', ['It helps update the likelihood of a diagnosis as new test results come in', 'It has no real-world applications', 'It only applies to games of chance', 'It eliminates the need for any testing'], 0),
   ('If new evidence strongly supports an event, Bayes Theorem would typically ___.', ['Increase the probability estimate for that event', 'Always decrease the probability to zero', 'Have no effect on the probability at all', 'Make the event impossible'], 0)]),
Sc('The Chemistry of Fireworks',
   'Grade 8 Science strand: fireworks produce colour and light through chemical reactions involving metal compounds, each element burning to create a distinct colour, combined with oxidizers and fuel to power the explosion.',
   [('What causes the different colours seen in fireworks?', ['Different metal compounds burning during the chemical reaction', 'The shape of the firework container', 'The time of day the firework is launched', 'The temperature of the air alone'], 0),
    ('What is the role of an oxidizer in a firework?', ['It provides oxygen to help the firework burn', 'It cools down the reaction completely', 'It prevents any explosion from occurring', 'It has no chemical role at all'], 0),
    ('Which metal compound might produce a red colour in fireworks?', ['Strontium compounds', 'Only plain carbon', 'Only water', 'Only plain oxygen'], 0),
    ('Fireworks rely on what type of chemical reaction to produce light and sound?', ['Combustion reactions', 'Only physical changes with no reaction', 'Only freezing reactions', 'Only dissolving reactions'], 0),
    ('Why do chemists study the composition of fireworks?', ['To understand and control the colours, safety, and effects produced', 'Fireworks have no chemical composition', 'Chemistry has no connection to fireworks', 'Fireworks never involve any reactions'], 0)]),
H('The National Policy of 1879',
  'Grade 8 History strand: the National Policy of 1879, introduced by Prime Minister John A. Macdonald, used high tariffs on imported goods to protect Canadian manufacturing while encouraging western settlement and railway expansion.',
  [('Who introduced the National Policy of 1879?', ['Prime Minister John A. Macdonald', 'Prime Minister Pierre Trudeau', 'Prime Minister Wilfrid Laurier', 'Prime Minister Lester Pearson'], 0),
   ('What economic tool did the National Policy rely on?', ['High tariffs on imported goods', 'Free trade with no tariffs at all', 'A complete ban on all imports', 'Lower taxes on all foreign goods'], 0),
   ('What was one goal of the National Policy?', ['Protecting Canadian manufacturing from foreign competition', 'Eliminating all Canadian industry', 'Ending western settlement completely', 'Reducing railway construction'], 0),
   ('Besides tariffs, what else did the National Policy encourage?', ['Western settlement and railway expansion', 'The abandonment of the Prairies', 'A reduction in Canadas population', 'The closing of Canadian borders to trade entirely'], 0),
   ('Why is the National Policy considered a major economic strategy in Canadian history?', ['It shaped Canadas industrial and economic development for decades', 'It had no lasting economic effect', 'It was reversed within a single year', 'It only affected a small town'], 0)]),
]),
day(115, [
L('Media Literacy: Analyzing Memes and Internet Culture',
  'Grade 8 Language strand: memes spread ideas and humour quickly through images, text, and repetition, and analyzing them critically helps readers understand how internet culture shapes communication and public opinion.',
  [('What is a meme?', ['An image, video, or piece of text that spreads ideas or humour quickly online', 'A formal academic essay', 'A type of legal document', 'A printed newspaper article'], 0),
   ('How do memes typically spread?', ['Through sharing, repetition, and adaptation across the internet', 'Only through printed newspapers', 'They cannot spread at all', 'Only through formal presentations'], 0),
   ('Why is it useful to analyze memes critically?', ['To understand how internet culture shapes communication and opinion', 'Memes have no influence on culture or opinion', 'Critical analysis is never useful for internet content', 'Memes are always completely factual'], 0),
   ('What technique do memes often use to convey meaning quickly?', ['Combining a familiar image with concise text', 'Long, detailed paragraphs with no images', 'Complex legal language', 'Silence with no content at all'], 0),
   ('Memes can be considered a form of ___.', ['Modern digital communication and cultural commentary', 'Ancient handwritten manuscripts', 'Formal government documents', 'Scientific research papers only'], 0)]),
M('Discrete Math: Introduction to Graph Theory',
  'Grade 8 Math strand: graph theory studies networks made of nodes (or vertices) connected by edges, used to model relationships and connections in systems like social networks, maps, and computer networks.',
  [('What are the two basic components of a graph in graph theory?', ['Nodes (vertices) and edges', 'Only numbers', 'Only angles', 'Only fractions'], 0),
   ('What does an edge in a graph represent?', ['A connection between two nodes', 'A single isolated point', 'The colour of the graph', 'The total size of the graph'], 0),
   ('Which real-world system could be modeled using graph theory?', ['A social network showing connections between people', 'The freezing point of water', 'The colour of the sky', 'The taste of a food'], 0),
   ('In graph theory, a node with many connecting edges is often called ___.', ['A highly connected or high-degree node', 'An isolated node', 'A deleted node', 'An imaginary node'], 0),
   ('Graph theory is especially useful in fields such as ___.', ['Computer science and network design', 'Only painting and drawing', 'Only cooking and recipes', 'Only music composition'], 0)]),
Sc('The Physics of Rainbows and Light Dispersion',
   'Grade 8 Science strand: rainbows form when sunlight is refracted, reflected, and dispersed by water droplets in the air, splitting white light into its full spectrum of colours.',
   [('What causes a rainbow to form?', ['Sunlight being refracted, reflected, and dispersed by water droplets', 'Sunlight passing through solid glass only', 'Sound waves bending around clouds', 'Wind blowing dust into the air'], 0),
    ('What is light dispersion?', ['The splitting of white light into its full spectrum of colours', 'The complete disappearance of light', 'The blocking of all light entirely', 'The merging of colours into black'], 0),
    ('What does a water droplet do to sunlight to create a rainbow?', ['Refracts and reflects it, separating the colours', 'Absorbs all light with no reflection', 'Turns light into sound', 'Blocks light completely'], 0),
    ('What is the correct order of colours typically seen in a rainbow?', ['Red, orange, yellow, green, blue, indigo, violet', 'Black, white, grey, and brown only', 'Only red and blue', 'Random colours with no pattern'], 0),
    ('Why can rainbows sometimes be seen after rain on a sunny day?', ['Sunlight interacts with remaining water droplets in the air', 'Rainbows only occur at night', 'Rainbows require no water at all', 'Rainbows only form underwater'], 0)]),
H('The Royal Commission on Bilingualism and Biculturalism',
  'Grade 8 History strand: established in 1963, the Royal Commission on Bilingualism and Biculturalism examined the relationship between English and French Canadians, leading to major policies like the Official Languages Act.',
  [('When was the Royal Commission on Bilingualism and Biculturalism established?', ['1963', '1867', '1949', '1999'], 0),
   ('What relationship did the Commission examine?', ['The relationship between English and French Canadians', 'The relationship between Canada and the United States', 'The relationship between provinces and territories only', 'The relationship between Canada and Britain only'], 0),
   ('What major policy resulted from the Commissions recommendations?', ['The Official Languages Act', 'The Indian Act', 'The Multiculturalism Act', 'The Canadian Bill of Rights'], 0),
   ('Why was the Commission created during this period of Canadian history?', ['Growing concerns about French Canadian rights and national unity', 'To end all use of the French language in Canada', 'To eliminate the English language entirely', 'To create a new national anthem'], 0),
   ('The work of this Commission connects most closely to which other Canadian historical development?', ['Quebecs Quiet Revolution and growing calls for recognition', 'The Klondike Gold Rush', 'The building of the CPR', 'The Halifax Explosion'], 0)]),
]),
day(116, [
L('Grammar: Understanding Ellipsis and Omission in Writing',
  'Grade 8 Language strand: an ellipsis (...) shows an omission of words from a quotation or indicates a trailing off or pause in thought, and using it correctly helps writers condense or shape meaning without distorting the original text.',
  [('What does an ellipsis indicate when used in a direct quotation?', ['That words have been omitted from the original text', 'That the entire quotation is false', 'That the sentence has ended with a question', 'That the writer disagrees with the quotation'], 0),
   ('An ellipsis can also show what in dialogue?', ['A pause or trailing off in thought', 'A shout or exclamation only', 'A grammatical error', 'A complete stop with no further meaning'], 0),
   ('How many dots typically make up a standard ellipsis?', ['Three', 'Two', 'Five', 'One'], 0),
   ('Why must writers be careful when omitting words from a quotation with an ellipsis?', ['Omitting words could distort the original meaning if done carelessly', 'Ellipses always make quotations more accurate', 'Omitting words is never allowed under any circumstance', 'Ellipses have no effect on meaning'], 0),
   ('Which sentence correctly uses an ellipsis to show a trailing thought?', ['I was going to say... never mind.', 'I was going to say never mind', 'I was going to say, never, mind', 'I was going to say; never mind'], 0)]),
M('Algebra: The Fundamental Theorem of Algebra',
  'Grade 8 Math strand: the Fundamental Theorem of Algebra states that every polynomial equation of degree n has exactly n roots when counting complex and repeated roots, connecting algebra to the earlier study of complex numbers.',
  [('What does the Fundamental Theorem of Algebra state?', ['A polynomial of degree n has exactly n roots, counting complex and repeated roots', 'A polynomial always has zero roots', 'Only linear equations have any roots', 'Polynomials never have complex roots'], 0),
   ('How many roots does a degree-3 polynomial have according to this theorem?', ['Three', 'One', 'Zero', 'Infinite'], 0),
   ('What earlier math concept does this theorem connect to?', ['Complex and imaginary numbers', 'Only whole numbers', 'Only fractions', 'Only negative integers'], 0),
   ('Can a polynomials roots include complex numbers?', ['Yes, according to the Fundamental Theorem of Algebra', 'No, roots must always be whole numbers', 'No, roots must always be negative', 'Only irrational roots are allowed'], 0),
   ('Why is the Fundamental Theorem of Algebra considered important in mathematics?', ['It guarantees a predictable number of solutions for polynomial equations', 'It proves that polynomials have no solutions', 'It only applies to equations with no variables', 'It disproves the existence of complex numbers'], 0)]),
Sc('Bird Migration and Animal Navigation',
   'Grade 8 Science strand: many animals, especially migratory birds, travel long distances using cues like the position of the sun and stars, Earths magnetic field, and landmarks to navigate accurately.',
   [('What is bird migration?', ['The seasonal, long-distance travel of birds between habitats', 'A permanent move with no return', 'A type of hibernation', 'A method of finding food only within one location'], 0),
    ('What is one cue animals use to navigate during migration?', ['Earths magnetic field', 'The colour of nearby buildings', 'Random guessing with no cues', 'The price of local food sources'], 0),
    ('Why might birds migrate seasonally?', ['To find better food sources and breeding conditions', 'Migration serves no biological purpose', 'To avoid other birds entirely', 'To permanently leave their habitat forever'], 0),
    ('Besides Earths magnetic field, what other cues can animals use to navigate?', ['The position of the sun and stars', 'Only the colour of the sky', 'Only nearby traffic sounds', 'Only human-made maps'], 0),
    ('What term describes an animals ability to sense Earths magnetic field for navigation?', ['Magnetoreception', 'Echolocation', 'Photosynthesis', 'Osmosis'], 0)]),
H('The Manitoba Schools Question',
  'Grade 8 History strand: the Manitoba Schools Question was a major late 19th-century political and legal conflict over funding for French-language Catholic schools in Manitoba, highlighting tensions between English and French Canada.',
  [('What was the Manitoba Schools Question mainly about?', ['Funding for French-language Catholic schools in Manitoba', 'A dispute over railway construction', 'A disagreement about provincial borders', 'A conflict over fishing rights'], 0),
   ('What tension did the Manitoba Schools Question highlight?', ['Tensions between English and French Canada', 'Tensions between Canada and the United States', 'Tensions between Indigenous and settler communities only', 'Tensions between Canada and Britain only'], 0),
   ('Roughly when did the Manitoba Schools Question take place?', ['In the late 1800s', 'In the 1990s', 'In the 1600s', 'It has not happened yet'], 0),
   ('Why is the Manitoba Schools Question significant in Canadian history?', ['It reflects ongoing debates over minority language rights in Canada', 'It has no connection to Canadian identity', 'It resolved all language issues in Canada permanently', 'It only affected a single school'], 0),
   ('The Manitoba Schools Question is often studied alongside later debates about ___.', ['Bilingualism and minority language education rights', 'Canadas relationship with the United Nations', 'The construction of the Avro Arrow', 'The Klondike Gold Rush'], 0)]),
]),
day(117, [
L('Reading: Analyzing Hyperbole, Understatement, and Paradox',
  'Grade 8 Language strand: hyperbole exaggerates for effect, understatement deliberately downplays something significant, and a paradox presents a statement that seems contradictory but reveals a deeper truth.',
  [('What is hyperbole?', ['Exaggeration used for effect', 'A statement that deliberately downplays something', 'A contradictory statement revealing truth', 'A type of punctuation mark'], 0),
   ('Which sentence is an example of hyperbole?', ['I have told you a million times to clean your room.', 'It might rain later today.', 'The sky is blue.', 'She walked to school.'], 0),
   ('What is understatement?', ['Deliberately downplaying something significant', 'Exaggerating something beyond reality', 'A grammar rule about verb tense', 'A citation format'], 0),
   ('Which sentence is an example of understatement about a huge storm?', ['It was a bit windy outside.', 'It was the most catastrophic storm in history and destroyed everything.', 'The storm was extremely and incredibly powerful.', 'The storm was the biggest ever recorded.'], 0),
   ('What is a paradox?', ['A statement that seems contradictory but reveals a deeper truth', 'A statement that is always completely false', 'A type of onomatopoeia', 'A citation style used in essays'], 0)]),
M('Calculus Preview: An Introduction to Limits',
  'Grade 8 Math strand: a limit describes the value a function approaches as its input gets closer to a certain number, a foundational idea in calculus used to understand rates of change and continuity.',
  [('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('Limits are a foundational concept in which branch of mathematics?', ['Calculus', 'Basic arithmetic only', 'Geometry only', 'Number theory only'], 0),
   ('What might a limit help describe about a function?', ['Its behaviour as it approaches a certain point, even if undefined there', 'Only its colour on a graph', 'Only its name', 'Nothing meaningful about the function'], 0),
   ('As x approaches 2, if f(x) gets closer and closer to 5, what is the limit of f(x) as x approaches 2?', ['5', '2', '0', 'Undefined in all cases'], 0),
   ('Why are limits important for understanding rates of change?', ['They allow mathematicians to analyze values that a function approaches, even at points of change', 'They have no connection to rates of change', 'They only apply to whole numbers', 'They remove the need to study functions'], 0)]),
Sc('Desert Ecosystems and Adaptations',
   'Grade 8 Science strand: desert ecosystems receive very little precipitation, and the plants and animals that live there have special adaptations, such as water storage and nocturnal behaviour, to survive extreme conditions.',
   [('What defines a desert ecosystem?', ['Very little precipitation', 'Extremely high precipitation', 'Constant freezing temperatures only', 'No sunlight at all'], 0),
    ('What is one adaptation desert plants often have?', ['The ability to store water', 'The need for constant flooding', 'A requirement for extremely cold temperatures', 'An inability to survive any sunlight'], 0),
    ('Why might many desert animals be nocturnal?', ['To avoid the extreme heat of the day', 'Nocturnal behaviour has no survival advantage', 'To avoid finding food entirely', 'Because deserts have no daytime at all'], 0),
    ('Which of these is a well-known desert plant adaptation?', ['A cactuss thick, water-storing stem', 'A water lilys floating leaves', 'A pine trees needle-shaped leaves for cold climates', 'A palm trees tolerance for constant rain'], 0),
    ('Desert ecosystems can be found on which types of land?', ['Both hot and cold regions with low precipitation', 'Only underwater locations', 'Only areas with constant rainfall', 'Only areas near the equator'], 0)]),
H('Canada and the League of Nations',
  'Grade 8 History strand: Canada joined the League of Nations after World War I as an independent member separate from Britain, an early sign of its growing autonomy on the international stage.',
  [('What international organization did Canada join independently after World War I?', ['The League of Nations', 'The United Nations', 'NATO', 'NORAD'], 0),
   ('Why was Canadas independent membership in the League of Nations significant?', ['It signaled Canadas growing autonomy separate from Britain', 'It meant Canada had no international role at all', 'It ended all of Canadas ties to Britain immediately', 'It was identical to Canadas role before the war'], 0),
   ('What was the main purpose of the League of Nations?', ['To promote international cooperation and prevent future conflicts', 'To create a single global government', 'To eliminate all international trade', 'To reunite former colonies with their empires'], 0),
   ('When was the League of Nations formed?', ['After World War I', 'After World War II', 'Before Confederation', 'In the 21st century'], 0),
   ('What organization was later created after the League of Nations largely failed to prevent World War II?', ['The United Nations', 'The Commonwealth', 'NAFTA', 'The G7'], 0)]),
]),
day(118, [
L('Writing: Structuring a Plot Using Freytags Pyramid',
  'Grade 8 Language strand: Freytags Pyramid outlines a dramatic structure of exposition, rising action, climax, falling action, and resolution, helping writers organize tension and pacing throughout a story.',
  [('What does Freytags Pyramid outline?', ['A dramatic structure for organizing a stories tension and pacing', 'A type of grammar rule', 'A method for citing sources', 'A punctuation guideline'], 0),
   ('What is the first stage of Freytags Pyramid?', ['Exposition', 'Climax', 'Resolution', 'Falling action'], 0),
   ('What happens during the climax of a story?', ['The story reaches its point of highest tension or turning point', 'The story introduces the setting only', 'The conflict is fully resolved with no tension', 'Nothing significant happens'], 0),
   ('What comes after the climax in Freytags Pyramid?', ['Falling action', 'Exposition', 'Rising action', 'The introduction'], 0),
   ('Why is understanding Freytags Pyramid useful for writers?', ['It helps organize a story for maximum tension and reader engagement', 'It removes the need for any conflict in a story', 'It only applies to poetry, never prose', 'It has no effect on how a story is structured'], 0)]),
M('Algebra: An Introduction to Proof by Mathematical Induction',
  'Grade 8 Math strand: mathematical induction proves a statement is true for all natural numbers by showing it holds for a base case and then showing that if it holds for one case, it must hold for the next.',
  [('What does mathematical induction prove?', ['That a statement is true for all natural numbers', 'That a statement is always false', 'Only that a statement works for one specific number', 'Nothing about a mathematical statement'], 0),
   ('What is the first step in a proof by induction called?', ['The base case', 'The final case', 'The conclusion', 'The exception'], 0),
   ('What must be shown in the inductive step?', ['That if the statement holds for one case, it holds for the next', 'That the statement is false for every case', 'That no cases need to be checked', 'That the base case is irrelevant'], 0),
   ('Mathematical induction is often compared to which everyday analogy?', ['A row of falling dominoes', 'A single light switch', 'A locked door', 'A blank page'], 0),
   ('Why is mathematical induction a powerful proof technique?', ['It can prove a statement true for infinitely many cases using just two steps', 'It only proves statements for a single case', 'It cannot be used to prove anything', 'It requires testing every possible number individually'], 0)]),
Sc('The Physics of Friction and Wear',
   'Grade 8 Science strand: friction is a force that resists motion between two surfaces in contact, generating heat and gradually causing wear, though it is also essential for everyday actions like walking and braking.',
   [('What is friction?', ['A force that resists motion between two surfaces in contact', 'A force that always increases motion', 'A type of chemical reaction', 'A form of light energy'], 0),
    ('What is one effect friction can have on surfaces over time?', ['Gradual wear and heat generation', 'Instant freezing of the surfaces', 'No effect at all on the surfaces', 'Making the surfaces heavier'], 0),
    ('Why is friction essential for walking?', ['It allows shoes to grip the ground and prevent slipping', 'Friction makes walking completely impossible', 'Friction only affects vehicles, not people', 'Walking requires the complete absence of friction'], 0),
    ('How does friction help a car stop when braking?', ['It resists the motion of the wheels against the road', 'It has no role in braking at all', 'It speeds up the car instead of slowing it', 'It only works underwater'], 0),
    ('What might reduce friction between two surfaces?', ['Adding a lubricant, like oil, between them', 'Increasing the roughness of both surfaces', 'Pressing the surfaces together harder', 'Removing all lubrication'], 0)]),
H('The Alberta Social Credit Movement and the Great Depression',
  'Grade 8 History strand: the Social Credit movement gained strong support in Alberta during the Great Depression, promoting new economic ideas to address widespread poverty and eventually forming the provincial government in 1935.',
  [('During which period did the Social Credit movement gain strong support in Alberta?', ['The Great Depression', 'World War II', 'The 1990s', 'Confederation in 1867'], 0),
   ('What kind of ideas did the Social Credit movement promote?', ['New economic ideas to address widespread poverty', 'A return to the fur trade economy', 'The elimination of all government spending', 'A ban on all provincial elections'], 0),
   ('In what year did the Social Credit party form the Alberta provincial government?', ['1935', '1867', '1999', '1949'], 0),
   ('Why did movements like Social Credit gain popularity during the Great Depression?', ['Widespread economic hardship led people to seek new political solutions', 'The economy was thriving with no hardship at all', 'No one was affected by the Great Depression in Alberta', 'People were uninterested in economic policy'], 0),
   ('The rise of the Social Credit movement reflects a broader trend of ___.', ['New political movements emerging in response to economic crisis', 'Political stability with no new movements', 'A complete rejection of all political parties', 'Alberta separating from Canada entirely'], 0)]),
]),
day(119, [
L('Vocabulary: Euphemisms and Doublespeak',
  'Grade 8 Language strand: a euphemism replaces a harsh or blunt term with a gentler one, while doublespeak deliberately uses vague or misleading language to obscure an unpleasant truth, often for persuasive or political purposes.',
  [('What is a euphemism?', ['A gentler word or phrase used in place of a harsh or blunt one', 'A word that exaggerates the truth', 'A type of rhyme scheme', 'A citation format'], 0),
   ('Which phrase is an example of a euphemism?', ['Passed away, instead of died', 'Ran quickly', 'A large building', 'A red car'], 0),
   ('What is doublespeak?', ['Language deliberately used to obscure an unpleasant truth', 'Language that is always completely honest and direct', 'A grammar rule about pronouns', 'A type of punctuation'], 0),
   ('Why might doublespeak be used in politics or advertising?', ['To make an unpleasant reality sound more acceptable', 'To make communication perfectly clear and direct', 'Doublespeak is never used in real communication', 'To eliminate all persuasive language'], 0),
   ('Why is it useful for readers to recognize euphemisms and doublespeak?', ['To understand the real meaning behind carefully chosen language', 'Recognizing them has no practical benefit', 'These techniques are always meant to help the reader', 'They only appear in fictional stories'], 0)]),
M('Data Management: An Introduction to Bayesian Updating in Everyday Decisions',
  'Grade 8 Math strand: building on Bayes Theorem, Bayesian updating is the process of revising a probability estimate as new information becomes available, a strategy used in everyday decision-making and data analysis.',
  [('What is Bayesian updating?', ['The process of revising a probability estimate as new information arrives', 'A method that never changes any probability', 'A way to eliminate all uncertainty completely', 'A type of geometric proof'], 0),
   ('Why might someone use Bayesian updating in everyday decision-making?', ['To adjust their beliefs or predictions as new evidence appears', 'To ignore all new information completely', 'To make decisions with no information at all', 'To avoid ever changing an opinion'], 0),
   ('If new evidence makes an event seem more likely, a Bayesian update would ___.', ['Increase the estimated probability of that event', 'Always decrease the probability to zero', 'Have no effect on the estimate', 'Eliminate the event as a possibility'], 0),
   ('Bayesian updating relies on combining what two things?', ['A starting estimate and new evidence', 'Only random guesses with no data', 'Only past data with no new information', 'Only opinions with no mathematical basis'], 0),
   ('Which field commonly uses Bayesian updating to interpret new data?', ['Medical diagnosis and data science', 'Only ancient history', 'Only creative writing', 'Only music theory'], 0)]),
Sc('Genetic Engineering in Agriculture: An Introduction to GMOs',
   'Grade 8 Science strand: genetically modified organisms, or GMOs, are created by altering an organisms DNA to introduce desirable traits, such as pest resistance or improved crop yield, in modern agriculture.',
   [('What does GMO stand for?', ['Genetically modified organism', 'Generally moved organism', 'Growth management order', 'Green modified oxygen'], 0),
    ('How are GMOs created?', ['By altering an organisms DNA to introduce desirable traits', 'By exposing the organism to sunlight only', 'By changing the organisms diet with no genetic change', 'By freezing the organism permanently'], 0),
    ('What is one reason crops might be genetically modified?', ['To improve pest resistance or crop yield', 'To make the crop completely inedible', 'To eliminate the need for farming entirely', 'To remove all genetic material from the plant'], 0),
    ('Why is genetic engineering in agriculture a topic of ongoing debate?', ['People have different views on its safety, ethics, and environmental impact', 'Everyone agrees completely on every aspect of GMOs', 'GMOs have no effect on agriculture at all', 'The topic has no scientific basis'], 0),
    ('Genetic engineering in agriculture is an application of which broader scientific field?', ['Biotechnology', 'Astronomy', 'Meteorology', 'Geology'], 0)]),
H('Canada at the Paris Peace Conference of 1919',
  'Grade 8 History strand: Canada attended the Paris Peace Conference of 1919 and signed the Treaty of Versailles as a separate signatory from Britain, an important early step toward international recognition as an independent nation.',
  [('What major conference did Canada attend in 1919?', ['The Paris Peace Conference', 'The Congress of Vienna', 'The Yalta Conference', 'The Berlin Conference'], 0),
   ('What treaty did Canada sign separately from Britain at this conference?', ['The Treaty of Versailles', 'The Treaty of Paris', 'The Statute of Westminster', 'The North Atlantic Treaty'], 0),
   ('Why was Canadas separate signature on the treaty significant?', ['It was an early step toward international recognition as an independent nation', 'It meant Canada refused to participate in the treaty', 'It had no effect on Canadas international standing', 'It ended all of Canadas international relationships'], 0),
   ('What world event led to the Paris Peace Conference being held?', ['The end of World War I', 'The end of World War II', 'The Cold War', 'Confederation'], 0),
   ('Canadas role at the Paris Peace Conference is often linked to which later development?', ['Canadas separate membership in the League of Nations', 'The construction of the CPR', 'The Klondike Gold Rush', 'The Halifax Explosion'], 0)]),
]),
day(120, [
L('Language Review: Grammar, Vocabulary, and Reading Analysis',
  'Grade 8 Language strand review: students revisit emphatic pronouns, onomatopoeia, juxtaposition, eyewitness news reports, ellipsis, hyperbole/understatement/paradox, Freytags Pyramid, and euphemisms.',
  [('What is the purpose of an emphatic pronoun?', ['To add emphasis to a noun or pronoun already mentioned', 'To replace a verb entirely', 'To act as a question word', 'To function as a preposition'], 0),
   ('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('What does an ellipsis indicate when used in a direct quotation?', ['That words have been omitted from the original text', 'That the entire quotation is false', 'That the sentence has ended with a question', 'That the writer disagrees with the quotation'], 0),
   ('What is a paradox?', ['A statement that seems contradictory but reveals a deeper truth', 'A statement that is always completely false', 'A type of onomatopoeia', 'A citation style used in essays'], 0),
   ('What is a euphemism?', ['A gentler word or phrase used in place of a harsh or blunt one', 'A word that exaggerates the truth', 'A type of rhyme scheme', 'A citation format'], 0)]),
M('Math Review: Vectors, Matrices, and Advanced Concepts',
  'Grade 8 Math strand review: students revisit vectors and the dot product, matrix multiplication and determinants, modular exponentiation, Bayes Theorem, graph theory, the Fundamental Theorem of Algebra, limits, and induction.',
  [('What two properties does a vector have?', ['Magnitude and direction', 'Only magnitude', 'Only direction', 'Neither magnitude nor direction'], 0),
   ('What does the determinant of a matrix indicate?', ['Properties of the matrix, such as whether it can be inverted', 'The exact size of the matrix only', 'The colour used to represent the matrix', 'Nothing useful about the matrix'], 0),
   ('What does Bayes Theorem help calculate?', ['An updated probability based on new evidence', 'A fixed probability that never changes', 'The average of a data set', 'The volume of a 3D shape'], 0),
   ('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('What does mathematical induction prove?', ['That a statement is true for all natural numbers', 'That a statement is always false', 'Only that a statement works for one specific number', 'Nothing about a mathematical statement'], 0)]),
Sc('Science Review: Body Systems, Physics, and Genetics',
   'Grade 8 Science strand review: students revisit the integumentary and excretory systems, antibiotic resistance, the chemistry of fireworks, light dispersion, bird migration, desert ecosystems, friction, and GMOs.',
   [('What organs make up the integumentary system?', ['Skin, hair, and nails', 'The heart and lungs', 'The stomach and intestines', 'The brain and spinal cord'], 0),
    ('Which organs are the primary filters in the excretory system?', ['The kidneys', 'The lungs', 'The liver only', 'The heart'], 0),
    ('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'When a medicine works better over time', 'When a virus becomes weaker over time', 'When bacteria disappear completely'], 0),
    ('What is light dispersion?', ['The splitting of white light into its full spectrum of colours', 'The complete disappearance of light', 'The blocking of all light entirely', 'The merging of colours into black'], 0),
    ('What does GMO stand for?', ['Genetically modified organism', 'Generally moved organism', 'Growth management order', 'Green modified oxygen'], 0)]),
H('History Review: Canadian Independence and Identity',
  'Grade 8 History strand review: students revisit Ukrainian Canadian internment, Newfoundlands entry into Confederation, Canadas 1939 declaration of war, the National Policy, bilingualism, the Manitoba Schools Question, the League of Nations, Social Credit, and the Paris Peace Conference.',
  [('Under what law were Ukrainian Canadians interned during WWI?', ['The War Measures Act', 'The Indian Act', 'The Canadian Bill of Rights', 'The Multiculturalism Act'], 0),
   ('In what year did Newfoundland join Confederation?', ['1949', '1867', '1905', '1999'], 0),
   ('Who introduced the National Policy of 1879?', ['Prime Minister John A. Macdonald', 'Prime Minister Pierre Trudeau', 'Prime Minister Wilfrid Laurier', 'Prime Minister Lester Pearson'], 0),
   ('What international organization did Canada join independently after World War I?', ['The League of Nations', 'The United Nations', 'NATO', 'NORAD'], 0),
   ('What treaty did Canada sign separately from Britain at the Paris Peace Conference?', ['The Treaty of Versailles', 'The Treaty of Paris', 'The Statute of Westminster', 'The North Atlantic Treaty'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_111_120)
    append_to(8, g8_111_120)
