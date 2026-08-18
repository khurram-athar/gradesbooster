#!/usr/bin/env python3
"""Grade 8, Days 171-180 -- extends Grade 8 from 170 to 180 days. Topics
chosen after dumping the existing Day 1-170 title list (data/grade8.json)
in full to avoid any overlap: prepositional phrases, acronyms and
initialisms, red herrings in mystery fiction, the process essay,
paywalls and the business of online news, commonly confused verbs (lie,
lay, sit, set), collective nouns for animals, epigraphs and their
function, and writing a letter to the editor; skewness and distribution
shape, triangular numbers, the isoperimetric problem, synthetic
division, the Birthday Paradox, palindromic numbers, sampling methods
and bias, geometric probability, and percentiles and quartiles; the
chemistry of sunscreen, the physics of roller coasters, cloud types and
weather prediction, osmosis and diffusion in cells, space debris and
satellite collisions, how noise-cancelling headphones work, the science
of food preservation, the human skin microbiome, and genetic testing
and personalized medicine; the introduction of the metric system in
Canada, the founding of the National Film Board in 1939, the creation
of the CRTC, the Order of Canada, the Canadian Human Rights Act of
1977, Expo 86, the Air India bombing of 1985, the development of the
Canadarm, and the Gouzenko Affair. None of these topics duplicate any
Day 1-170 subject or title. Day 180 is a cross-subject review day
drawing on Days 171-179; each review title includes the Days 171-179
range and uses wording distinct from every earlier review days title
(compare, e.g., Day 170s "Language Review: Grammar, Vocabulary, and
Descriptive Writing (Days 161-169)" against Day 180s "Language Review:
Grammar, Vocabulary, and Media Literacy (Days 171-179)").

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days161_170.py.
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


def _rebalance_answer_positions(days, seed=20260818):
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


g8_171_180 = [
day(171, [
L('Grammar: Prepositional Phrases and Their Function in a Sentence',
  'Grade 8 Language strand: a prepositional phrase begins with a preposition, such as in, on, or under, and ends with a noun or pronoun called the object of the preposition, functioning as an adjective or an adverb within a sentence.',
  [('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A conjunction', 'A comma'], 0),
   ('What is the noun or pronoun at the end of a prepositional phrase called?', ['The object of the preposition', 'The subject of the sentence', 'The main verb', 'The antecedent'], 0),
   ('Which of these is a prepositional phrase?', ['Under the old bridge', 'Quickly ran away', 'The tall boy', 'Sang very loudly'], 0),
   ('What two roles can a prepositional phrase play in a sentence?', ['Acting as an adjective or an adverb', 'Acting only as a subject', 'Acting only as a main verb', 'Acting only as a conjunction'], 0),
   ('Why is it useful to recognize prepositional phrases when finding the subject of a sentence?', ['The true subject of a sentence is never located inside a prepositional phrase', 'Prepositional phrases always contain the subject of a sentence', 'Prepositional phrases replace the need for a subject entirely', 'Every sentence must begin with a prepositional phrase'], 0)]),
M('Statistics: An Introduction to Skewness and Distribution Shape',
  'Grade 8 Math strand: skewness describes the asymmetry of a data distribution, with a right-skewed, or positively skewed, distribution having a longer tail toward higher values and a left-skewed distribution having a longer tail toward lower values.',
  [('What does skewness describe about a data distribution?', ['Its asymmetry, or how unevenly the data is spread', 'The exact number of data points collected', 'The colour used to display a graph', 'The units used to measure the data'], 0),
   ('What does a right-skewed, or positively skewed, distribution look like?', ['A longer tail stretching toward higher values', 'A longer tail stretching toward lower values', 'A perfectly symmetrical shape', 'A shape with no tail on either side'], 0),
   ('What does a left-skewed distribution look like?', ['A longer tail stretching toward lower values', 'A longer tail stretching toward higher values', 'An identical shape to a right-skewed distribution', 'A distribution with only one possible value'], 0),
   ('In a distribution with no skew, how do the mean and median typically compare?', ['They are approximately equal', 'The mean is always much larger than the median', 'The median is always much larger than the mean', 'They can never be calculated for the same data set'], 0),
   ('Why is it useful to check the skewness of a data set before choosing the mean or median to describe it?', ['A skewed distribution can make the mean a misleading measure of a typical value', 'Skewness has no effect on which measure best describes a data set', 'The mean is always the best choice regardless of skewness', 'Skewed data sets cannot have a mean or a median calculated'], 0)]),
Sc('Chemistry: The Chemistry of Sunscreen and UV Protection',
   'Grade 8 Science strand: sunscreen protects skin using chemical compounds that either absorb ultraviolet radiation and convert it into harmless heat or physically reflect and scatter UV rays away from the skin.',
   [('What does sunscreen protect the skin from?', ['Ultraviolet radiation from the sun', 'Visible light only', 'Extreme cold temperatures', 'Loud noise'], 0),
    ('What do chemical sunscreen compounds do to ultraviolet radiation?', ['Absorb it and convert it into harmless heat', 'Freeze it instantly', 'Turn it into visible light', 'Amplify its strength before it reaches the skin'], 0),
    ('How do physical, or mineral, sunscreens protect the skin?', ['By reflecting and scattering UV rays away from the skin', 'By absorbing all visible light', 'By cooling the skin directly', 'By blocking oxygen from reaching the skin'], 0),
    ('What does the SPF number on a sunscreen bottle generally indicate?', ['A measure of how well the product protects skin from UV-related burning', 'The exact temperature the sunscreen can withstand', 'The weight of the sunscreen bottle', 'The number of ingredients used in the product'], 0),
    ('Why is understanding the chemistry of sunscreen useful for protecting long-term skin health?', ['It helps explain how repeated UV exposure can be reduced through absorption or reflection of harmful rays', 'Sunscreen has no proven effect on skin health', 'UV radiation cannot damage skin cells in any way', 'Sunscreen works by removing oxygen from the skin'], 0)]),
H('The Introduction of the Metric System in Canada',
  'Grade 8 History strand: beginning in the early 1970s, the federal government led a gradual conversion from imperial to metric measurement, changing how Canadians reported weather, fuel prices, and product weights over the following decade.',
  [('In what decade did Canada begin its transition to the metric system?', ['The 1970s', 'The 1860s', 'The 1920s', 'The 1990s'], 0),
   ('What kind of measurement system did Canada convert away from during metrication?', ['The imperial system', 'The decimal currency system', 'The binary numbering system', 'The Roman numeral system'], 0),
   ('Which everyday measurement was among the first to be reported in metric units in Canada?', ['Weather temperature', 'The price of a house', 'The length of a school year', 'The number of provinces'], 0),
   ('Who led the process of converting Canada to the metric system?', ['The federal government', 'A single private company', 'A foreign government', 'An individual citizen acting alone'], 0),
   ('Why did some Canadians resist the switch to the metric system at the time?', ['Many people were accustomed to imperial units and found the change inconvenient', 'Nobody in Canada ever used the imperial system before this change', 'The metric system was completely unknown anywhere else in the world', 'The change had no effect on daily life at all'], 0)]),
]),
day(172, [
L('Vocabulary: Acronyms and Initialisms',
  'Grade 8 Language strand: an acronym forms a new pronounceable word from the first letters of a phrase, such as laser, while an initialism is read letter by letter, such as FBI, and both are common shortcuts in everyday and technical language.',
  [('What is an acronym?', ['A word formed from the first letters of a phrase that is pronounced as a word', 'A word that means the opposite of another word', 'A word borrowed unchanged from another language', 'A word with no vowels at all'], 0),
   ('How is an initialism different from an acronym?', ['An initialism is read letter by letter rather than pronounced as a word', 'An initialism is always longer than an acronym', 'An initialism never uses capital letters', 'An initialism and an acronym are always identical'], 0),
   ('Which of these is an example of an acronym?', ['Laser', 'FBI', 'CBC', 'USA'], 0),
   ('Which of these is an example of an initialism?', ['FBI', 'Laser', 'Scuba', 'Radar'], 0),
   ('Why have acronyms and initialisms become common in technical and scientific writing?', ['They provide a short, efficient way to refer to a long, repeated term', 'They make technical writing more difficult to understand on purpose', 'They are required by law in all formal documents', 'They replace the need for punctuation in a sentence'], 0)]),
M('Number Theory: An Introduction to Triangular Numbers',
  'Grade 8 Math strand: a triangular number is the sum of consecutive whole numbers starting from one, such as 1, 3, 6, and 10, and can be visualized as dots arranged in the shape of an equilateral triangle.',
  [('What is a triangular number?', ['A number formed by summing consecutive whole numbers starting from one', 'A number that is always divisible by three', 'A number that can only be an even number', 'A number with exactly three digits'], 0),
   ('Which of these is a triangular number?', ['10', '9', '8', '11'], 0),
   ('What shape can triangular numbers be arranged into using dots?', ['An equilateral triangle', 'A perfect square', 'A straight line only', 'A circle'], 0),
   ('What is the fourth triangular number, found by adding 1 + 2 + 3 + 4?', ['10', '9', '12', '8'], 0),
   ('Why are triangular numbers considered a useful introduction to figurate numbers in mathematics?', ['They show how a simple sum of consecutive numbers can correspond to a geometric pattern', 'They have no connection to any geometric shape', 'They can never be represented visually', 'They only apply to numbers greater than one hundred'], 0)]),
Sc('Physics: The Physics of Roller Coasters and Energy Conservation',
   'Grade 8 Science strand: a roller coaster relies on the conversion between gravitational potential energy at the top of a hill and kinetic energy as it descends, with the total mechanical energy remaining approximately constant throughout the ride.',
   [('What type of energy does a roller coaster car have at the top of a tall hill?', ['Gravitational potential energy', 'Only sound energy', 'Only chemical energy', 'Only thermal energy'], 0),
    ('What happens to potential energy as a roller coaster car descends a hill?', ['It converts into kinetic energy, increasing the cars speed', 'It disappears completely with no conversion', 'It converts entirely into sound with no motion produced', 'It increases without any corresponding change in speed'], 0),
    ('According to the law of conservation of energy, what happens to the total mechanical energy of an ideal roller coaster?', ['It remains approximately constant throughout the ride', 'It constantly increases with no limit', 'It disappears entirely at the first hill', 'It only exists at the very end of the ride'], 0),
    ('Why is the first hill of a roller coaster typically the tallest hill on the ride?', ['It must provide enough initial potential energy for the rest of the ride, since energy is gradually lost to friction and air resistance', 'Later hills always need to be taller than the first', 'The height of hills has no effect on a roller coasters speed', 'The first hill produces no potential energy at all'], 0),
    ('Why do roller coasters eventually slow down and require a motor to be lifted again?', ['Friction and air resistance gradually convert mechanical energy into heat and sound', 'Roller coasters never lose any energy during a ride', 'Motors are used only for decoration, not for lifting cars', 'Potential energy always increases as a coaster runs'], 0)]),
H('The Founding of the National Film Board of Canada in 1939',
  'Grade 8 History strand: established in 1939 under founding commissioner John Grierson, the National Film Board of Canada was created to produce and distribute documentary and animated films that would help interpret Canada to Canadians and to the world.',
  [('In what year was the National Film Board of Canada established?', ['1939', '1867', '1949', '1921'], 0),
   ('Who served as the founding commissioner of the National Film Board?', ['John Grierson', 'Tommy Douglas', 'Lester Pearson', 'William Lyon Mackenzie King'], 0),
   ('What type of films did the National Film Board primarily produce?', ['Documentary and animated films', 'Only feature-length action films', 'Only films made outside of Canada', 'Only silent films with no sound'], 0),
   ('What was one goal of creating the National Film Board?', ['To help interpret Canada to Canadians and to the world through film', 'To replace all Canadian newspapers', 'To end all forms of Canadian broadcasting', 'To prevent Canadian films from being shown internationally'], 0),
   ('Why is the National Film Board considered an important Canadian cultural institution?', ['It has produced influential documentary and animated works that reflect Canadian stories and perspectives', 'It has never produced any films of lasting significance', 'It only operated for a single year before closing', 'It focuses exclusively on foreign stories with no connection to Canada'], 0)]),
]),
day(173, [
L('Reading: Analyzing Red Herrings in Mystery and Detective Fiction',
  'Grade 8 Language strand: a red herring is a false clue or misleading detail that an author deliberately places in a mystery or detective story to distract readers from the true solution and build suspense.',
  [('What is a red herring in a mystery story?', ['A false clue deliberately placed to mislead the reader', 'A character who solves the crime', 'The final piece of evidence that solves the case', 'A summary of the story at its beginning'], 0),
   ('Why do authors of detective fiction use red herrings?', ['To distract readers from the true solution and build suspense', 'To make the ending completely predictable', 'To remove all mystery from the plot', 'To reveal the solution as early as possible'], 0),
   ('Which is an example of a red herring in a story?', ['A suspicious character who turns out to be innocent', 'The detective who solves the case', 'The narrator explaining the setting', 'A chapter title'], 0),
   ('What skill does identifying red herrings help readers develop?', ['Careful, critical reading and evaluation of evidence within a text', 'The ability to skip chapters without missing anything', 'The ability to memorize a story word for word', 'The ability to ignore all clues in a story'], 0),
   ('Why might a reader feel satisfied upon realizing a detail was a red herring?', ['Recognizing the misdirection shows a close, active reading of the text', 'Red herrings are always revealed on the first page', 'Red herrings guarantee the ending will be disappointing', 'A red herring means the mystery has no real solution'], 0)]),
M('Geometry: An Introduction to the Isoperimetric Problem',
  'Grade 8 Math strand: the isoperimetric problem asks which shape encloses the greatest area for a given perimeter, and among all shapes with the same perimeter, a circle always encloses the largest possible area.',
  [('What does the isoperimetric problem ask?', ['Which shape encloses the greatest area for a given perimeter', 'Which shape has the smallest possible perimeter for any area', 'How to calculate the volume of a sphere', 'How to convert a shape into a straight line'], 0),
   ('Among all shapes with the same perimeter, which shape encloses the largest area?', ['A circle', 'A square', 'A triangle', 'A rectangle'], 0),
   ('If a rectangle and a circle have the same perimeter, which generally has the greater area?', ['The circle', 'The rectangle', 'They are always exactly equal', 'Neither shape can have an area'], 0),
   ('Why might the isoperimetric problem be relevant to designing a fence around a garden?', ['Using the shape that encloses the most area can make the most efficient use of a fixed length of fencing', 'Fencing has no relationship to the shape of a garden', 'A square always uses less fencing than any other shape', 'The shape of a garden never affects how much area it can enclose'], 0),
   ('Why is the isoperimetric problem considered a classic question in geometry?', ['It connects perimeter and area in a way that has interested mathematicians since ancient times', 'It was only discovered within the past decade', 'It has no known solution of any kind', 'It only applies to three-dimensional solids, never flat shapes'], 0)]),
Sc('Earth Science: Types of Clouds and Weather Prediction',
   'Grade 8 Science strand: clouds are classified by their shape and altitude into families such as cirrus, cumulus, and stratus, and recognizing these cloud types helps meteorologists predict upcoming changes in weather.',
   [('What are clouds classified by?', ['Their shape and altitude', 'Their exact colour only', 'The number of birds flying near them', 'Their distance from the ocean'], 0),
    ('What do cumulus clouds typically look like?', ['Puffy, cotton-like clouds with flat bottoms', 'Thin, wispy streaks high in the sky', 'A flat, featureless grey layer covering the whole sky', 'A ring shape surrounding the sun'], 0),
    ('What do cirrus clouds typically indicate about their altitude?', ['They form high in the atmosphere and appear thin and wispy', 'They always form at ground level', 'They only appear during a thunderstorm', 'They form exclusively over oceans'], 0),
    ('What might the sudden appearance of tall, dark cumulonimbus clouds signal to a meteorologist?', ['An approaching thunderstorm', 'A guarantee of clear skies all day', 'No change in weather at all', 'The end of the current season'], 0),
    ('Why is learning to identify cloud types useful for predicting weather?', ['Different cloud types are associated with different atmospheric conditions and upcoming weather changes', 'Cloud shape has no connection to weather conditions', 'All clouds indicate exactly the same type of weather', 'Cloud identification can only be done using satellite imagery'], 0)]),
H('The Creation of the Canadian Radio-television and Telecommunications Commission',
  'Grade 8 History strand: established in 1968 to regulate Canadian broadcasting, the Canadian Radio-television and Telecommunications Commission, known as the CRTC, later gained authority over telecommunications in 1976, shaping Canadian media and content rules.',
  [('What does the abbreviation CRTC stand for?', ['Canadian Radio-television and Telecommunications Commission', 'Canadian Rural Transportation and Trade Council', 'Canadian Research and Technology Coordination Committee', 'Central Regional Telecommunications Control Centre'], 0),
   ('In what year was the CRTC established to regulate broadcasting?', ['1968', '1939', '1949', '1988'], 0),
   ('In what year did the CRTC gain authority over telecommunications?', ['1976', '1968', '1939', '1867'], 0),
   ('What is one area the CRTC regulates in Canada?', ['Canadian content rules for broadcasting', 'The construction of highways', 'The operation of national parks', 'The training of teachers'], 0),
   ('Why was a national regulator such as the CRTC considered important for Canadian broadcasting?', ['It helped ensure Canadian content and standards were maintained across radio, television, and telecommunications', 'It had no effect on what Canadians could watch or hear', 'It only applied to broadcasters outside of Canada', 'It eliminated all radio and television broadcasting in Canada'], 0)]),
]),
day(174, [
L('Writing: The Process Essay: Explaining How Something Works',
  'Grade 8 Language strand: a process essay explains how something works or how to complete a task by breaking it into clear, sequential steps, often using transitional words such as first, next, and finally to guide the reader.',
  [('What does a process essay explain?', ['How something works or how to complete a task, in clear steps', 'A single characters physical appearance', 'An unrelated series of historical events', 'The authors opinion with no supporting explanation'], 0),
   ('What kind of order does a process essay typically follow?', ['A clear, sequential, step-by-step order', 'A completely random order', 'Only the final step, with no earlier steps described', 'Alphabetical order of unrelated words'], 0),
   ('Which transitional words are commonly used in a process essay?', ['First, next, and finally', 'Once upon a time and the end', 'Meanwhile and elsewhere only', 'Never and always only'], 0),
   ('Why is precise, clear language especially important in a process essay?', ['A reader must be able to follow and repeat the steps accurately', 'Precision does not matter in this type of essay', 'A process essay is never meant to be understood by readers', 'Vague language makes a process easier to follow'], 0),
   ('Why might a diagram or illustration be a useful addition to a process essay?', ['It can help clarify a step that is difficult to describe using words alone', 'Diagrams always replace the need for written steps', 'A process essay is not allowed to include any images', 'Diagrams make a process essay less clear'], 0)]),
M('Algebra: An Introduction to Synthetic Division',
  'Grade 8 Math strand: synthetic division is a shortcut method for dividing a polynomial by a linear expression of the form x minus a number, using only the coefficients of the polynomial to quickly find the quotient and remainder.',
  [('What does synthetic division provide a shortcut for?', ['Dividing a polynomial by a linear expression', 'Multiplying two polynomials together', 'Finding the square root of a number', 'Graphing a quadratic function'], 0),
   ('What does synthetic division use to perform the division?', ['Only the coefficients of the polynomial', 'The exact graph of the polynomial', 'A calculator with a square root function', 'The polynomials degree measured in radians'], 0),
   ('What form must the divisor take for synthetic division to be used?', ['A linear expression such as x minus a number', 'Any polynomial of any degree', 'A fraction with no variable at all', 'A quadratic expression only'], 0),
   ('What two results does synthetic division produce?', ['A quotient and a remainder', 'Only a single sum', 'Two unrelated polynomials', 'A list of prime factors'], 0),
   ('Why do students often prefer synthetic division over long division for polynomials in this specific form?', ['It is generally faster and involves fewer written steps', 'It always produces a different, incorrect answer', 'It can only be used on numbers, never polynomials', 'It requires graphing the polynomial first'], 0)]),
Sc('Biology: The Process of Osmosis and Diffusion in Cells',
   'Grade 8 Science strand: diffusion is the movement of particles from an area of higher concentration to lower concentration, while osmosis is the diffusion of water specifically across a selectively permeable cell membrane.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from low to high concentration only', 'A process that only occurs in solid materials', 'A process that requires no concentration difference at all'], 0),
    ('What is osmosis?', ['The diffusion of water across a selectively permeable membrane', 'The diffusion of solid particles through a rigid wall', 'A process unrelated to concentration differences', 'The movement of energy through a cell'], 0),
    ('What kind of membrane allows osmosis to occur?', ['A selectively permeable membrane', 'A completely solid, impermeable membrane', 'A membrane that blocks all substances equally', 'A membrane found only in plant roots'], 0),
    ('What might happen to a plant cell placed in a very salty solution due to osmosis?', ['Water may leave the cell, causing it to shrink', 'The cell would immediately burst', 'The cell would remain completely unaffected', 'The cell would double in size instantly'], 0),
    ('Why are diffusion and osmosis essential processes for living cells?', ['They allow nutrients, water, and waste to move into and out of cells to maintain proper function', 'Cells can survive without ever exchanging any materials', 'Diffusion and osmosis only occur in dead cells', 'These processes prevent cells from ever receiving nutrients'], 0)]),
H('The Order of Canada and Its Founding in 1967',
  'Grade 8 History strand: created in 1967 as part of the centennial celebrations, the Order of Canada is a national honour that recognizes outstanding achievement and service, awarded at three levels: Companion, Officer, and Member.',
  [('In what year was the Order of Canada created?', ['1967', '1949', '1988', '1921'], 0),
   ('What event coincided with the creation of the Order of Canada?', ['Canadas centennial celebrations', 'The end of the Second World War', 'Confederation in 1867', 'The Klondike Gold Rush'], 0),
   ('What does the Order of Canada recognize?', ['Outstanding achievement and service', 'Only military service', 'Only political office held', 'Only athletic achievement'], 0),
   ('What are the three levels of the Order of Canada?', ['Companion, Officer, and Member', 'Gold, Silver, and Bronze', 'First, Second, and Third Class', 'Senior, Junior, and Honorary'], 0),
   ('Why is the Order of Canada considered an important national symbol?', ['It publicly honours individuals whose contributions have benefited Canadian society', 'It is awarded automatically to every Canadian citizen', 'It has no connection to Canadian identity or achievement', 'It was cancelled shortly after being created'], 0)]),
]),
day(175, [
L('Media Literacy: Understanding Paywalls and the Business of Online News',
  'Grade 8 Language strand: many online news organizations use a paywall, which limits free access to articles, to generate subscription revenue that funds professional journalism, raising questions about who can access reliable information.',
  [('What is a paywall?', ['A barrier that limits free access to online content until a reader pays or subscribes', 'A type of advertisement shown before a video', 'A tool that blocks all access to the internet', 'A method for translating an article into another language'], 0),
   ('Why do many news organizations use paywalls?', ['To generate subscription revenue that funds professional journalism', 'To prevent anyone from ever reading their articles', 'To give away all content for free permanently', 'To replace the need for journalists entirely'], 0),
   ('What concern do some media critics raise about paywalls?', ['They may limit access to reliable information for readers who cannot pay', 'Paywalls guarantee that all information becomes completely free', 'Paywalls have no effect on who can access the news', 'Paywalls only exist for entertainment websites'], 0),
   ('What is one alternative way some online news outlets fund their reporting?', ['Displaying advertisements alongside free articles', 'Refusing to publish any articles at all', 'Charging readers for using a search engine', 'Requiring readers to write their own articles'], 0),
   ('Why is understanding how news outlets are funded useful for a media-literate reader?', ['It helps a reader consider what influences might shape the coverage they read', 'Funding sources never influence how a story is reported', 'All news organizations are funded in exactly the same way', 'Media literacy has no connection to how journalism is funded'], 0)]),
M('Probability: An Introduction to the Birthday Paradox',
  'Grade 8 Math strand: the Birthday Paradox shows that in a group of just twenty-three people, there is a greater than fifty percent probability that at least two people share the same birthday, a result that surprises most people at first.',
  [('What does the Birthday Paradox describe?', ['A surprisingly high probability that two people in a group share a birthday', 'A rule for calculating everyones exact birthday', 'A method for predicting future birthdays', 'A proof that no two people can share a birthday'], 0),
   ('According to the Birthday Paradox, how many people are needed for a greater than fifty percent chance that two share a birthday?', ['Twenty-three', 'One hundred eighty-three', 'Three hundred sixty-five', 'Two'], 0),
   ('Why does the Birthday Paradox result often surprise people at first?', ['It seems like far more than twenty-three people should be needed, but the number of possible pairs grows quickly', 'The correct answer is always exactly 365 people', 'The result has been proven mathematically false', 'The paradox only applies to leap years'], 0),
   ('What grows quickly as more people are added to a group, explaining the surprising result?', ['The number of possible pairs of people who could share a birthday', 'The number of days in a year', 'The number of months in a year', 'The number of leap years in a century'], 0),
   ('Why is the Birthday Paradox a popular example in the study of probability?', ['It illustrates how intuition can underestimate the likelihood of a shared outcome in a group', 'It proves that probability calculations are always intuitive', 'It shows that larger groups always have fewer shared birthdays', 'It has no real mathematical basis'], 0)]),
Sc('Space Science: Space Debris and Satellite Collisions',
   'Grade 8 Science strand: space debris consists of defunct satellites, spent rocket stages, and fragments from past collisions that orbit Earth at high speed, posing a growing collision risk to active satellites and spacecraft.',
   [('What is space debris?', ['Defunct satellites, spent rocket stages, and fragments orbiting Earth', 'A type of natural asteroid belt', 'A cloud of gas found only near the Moon', 'A term for stars that have burned out'], 0),
    ('Why is space debris considered dangerous to active satellites?', ['It orbits Earth at extremely high speed and can cause serious collision damage', 'It moves too slowly to ever cause damage', 'Space debris cannot physically collide with anything', 'It only exists inside Earths atmosphere'], 0),
    ('What can cause an increase in the amount of space debris in orbit?', ['Collisions between existing objects that create many smaller fragments', 'A decrease in the number of satellites ever launched', 'Debris naturally disappearing within a few seconds', 'The absence of any rockets ever being launched'], 0),
    ('What strategy do space agencies use to reduce collision risk from debris?', ['Tracking known debris and adjusting satellite orbits to avoid it', 'Ignoring all debris regardless of its location', 'Launching more debris deliberately into orbit', 'Removing all satellites from orbit permanently'], 0),
    ('Why has space debris become a growing concern as more satellites are launched?', ['A greater number of objects in orbit increases the chances of future collisions and further debris', 'More satellites in orbit always reduces the total amount of debris', 'Space debris has no connection to the number of active satellites', 'Satellites launched today can never contribute to space debris'], 0)]),
H('The Canadian Human Rights Act of 1977',
  'Grade 8 History strand: passed in 1977, the Canadian Human Rights Act prohibited discrimination based on grounds such as race, sex, and disability within federally regulated sectors and established the Canadian Human Rights Commission to investigate complaints.',
  [('In what year was the Canadian Human Rights Act passed?', ['1977', '1867', '1949', '1988'], 0),
   ('What did the Canadian Human Rights Act prohibit?', ['Discrimination based on grounds such as race, sex, and disability', 'All forms of federal taxation', 'Immigration to Canada from any country', 'The formation of new political parties'], 0),
   ('What body did the Canadian Human Rights Act establish?', ['The Canadian Human Rights Commission', 'The Supreme Court of Canada', 'The Bank of Canada', 'The Canadian Radio-television and Telecommunications Commission'], 0),
   ('What sectors did the Canadian Human Rights Act apply to?', ['Federally regulated sectors', 'Only provincial school boards', 'Only municipal governments', 'Only privately owned small businesses'], 0),
   ('Why is the Canadian Human Rights Act considered a significant step in Canadian legal history?', ['It created a formal, national framework for identifying and addressing discrimination', 'It eliminated all provincial human rights laws', 'It had no effect on federal workplaces or services', 'It only applied for a single year before being repealed'], 0)]),
]),
day(176, [
L('Grammar: Commonly Confused Verbs: Lie, Lay, Sit, and Set',
  'Grade 8 Language strand: lie means to recline and never takes a direct object, while lay means to place something and requires a direct object; similarly, sit means to be seated, while set means to place an item somewhere.',
  [('What does the verb lie mean?', ['To recline or rest in a position', 'To place an object somewhere', 'To stand up quickly', 'To speak loudly'], 0),
   ('What does the verb lay require that the verb lie does not?', ['A direct object', 'A subject', 'A verb tense', 'A capital letter'], 0),
   ('Which sentence correctly uses the verb lay?', ['She will lay the book on the table.', 'She will lay down for a nap.', 'The dog lay the bone.', 'He lay the keys on the counter, then lie down.'], 0),
   ('Which sentence correctly uses the verb set?', ['He set the plate on the table.', 'He set down for dinner.', 'The cat set on the windowsill.', 'She will set for an hour.'], 0),
   ('Why do writers often confuse lie and lay, or sit and set?', ['The verbs have similar meanings and overlapping forms, making them easy to mix up', 'The four verbs are always used interchangeably with no rules', 'These verbs are spelled identically in every sentence', 'Only one of the four verbs exists in standard English'], 0)]),
M('Number Theory: An Introduction to Palindromic Numbers',
  'Grade 8 Math strand: a palindromic number reads the same forward and backward, such as 121 or 3553, and mathematicians study patterns in how palindromic numbers are distributed and how they behave under operations such as addition.',
  [('What is a palindromic number?', ['A number that reads the same forward and backward', 'A number that is always a multiple of ten', 'A number with exactly two digits', 'A number that can never repeat a digit'], 0),
   ('Which of these is a palindromic number?', ['3553', '3554', '3535', '3545'], 0),
   ('What happens if you reverse the digits of the palindromic number 121?', ['It stays exactly the same', 'It becomes 211', 'It becomes 112', 'It becomes a negative number'], 0),
   ('Is every single-digit number, such as 7, considered a palindromic number?', ['Yes, because it reads the same forward and backward by default', 'No, single-digit numbers can never be palindromes', 'No, only numbers with an even number of digits can be palindromes', 'Yes, but only if the digit is zero'], 0),
   ('Why do palindromic numbers interest mathematicians studying number patterns?', ['They reveal symmetry within the number system that can be explored through operations like addition', 'They have no mathematical properties worth studying', 'They only exist in bases other than base ten', 'They cannot be added to any other number'], 0)]),
Sc('Technology: How Noise-Cancelling Headphones Work',
   'Grade 8 Science strand: noise-cancelling headphones use a microphone to detect incoming sound waves and generate an inverted sound wave that combines with the original through destructive interference, reducing the noise a listener hears.',
   [('What do noise-cancelling headphones use to detect incoming sound?', ['A built-in microphone', 'A camera lens', 'A magnet attached to the ear', 'A radio antenna'], 0),
    ('What kind of sound wave do noise-cancelling headphones generate to reduce noise?', ['An inverted sound wave that opposes the incoming sound', 'An identical copy of the incoming sound wave', 'A completely silent wave with no properties', 'A wave with a much higher pitch than the original'], 0),
    ('What is the name of the process that occurs when two opposite sound waves combine and cancel each other out?', ['Destructive interference', 'Constructive interference', 'Refraction', 'Reflection'], 0),
    ('Why are noise-cancelling headphones generally more effective at reducing low, steady sounds, such as an airplane engine, than sudden sharp sounds?', ['Steady, repetitive sound waves are easier to predict and generate an opposing wave for', 'Sudden sharp sounds are always easier for the technology to detect', 'Low sounds cannot be detected by any microphone', 'Noise-cancelling technology only affects high-pitched sounds'], 0),
    ('Why is understanding destructive interference useful for engineers designing noise-reducing technology?', ['It provides the physical principle that allows an opposing wave to actively cancel unwanted sound', 'Destructive interference always makes sound louder', 'Sound waves can never interact with each other', 'Noise-cancelling technology does not rely on any physics principle'], 0)]),
H('Expo 86: The World Exposition in Vancouver',
  'Grade 8 History strand: held in Vancouver in 1986 under the theme of transportation and communication, Expo 86 attracted millions of visitors, showcased new technology, and helped spur major infrastructure development in British Columbia.',
  [('In what year was Expo 86 held?', ['1986', '1967', '1996', '1976'], 0),
   ('In which Canadian city was Expo 86 held?', ['Vancouver', 'Montreal', 'Toronto', 'Calgary'], 0),
   ('What was the theme of Expo 86?', ['Transportation and communication', 'Agriculture and farming', 'Space exploration only', 'Ancient history'], 0),
   ('What effect did Expo 86 have on the host city?', ['It helped spur major infrastructure development in the region', 'It caused the city to lose all of its existing infrastructure', 'It had no lasting impact on the city whatsoever', 'It resulted in the citys population permanently decreasing'], 0),
   ('Why is Expo 86 often compared to Expo 67 in Canadian history?', ['Both were major world expositions hosted in Canada that attracted large numbers of international visitors', 'Both events took place in exactly the same city', 'Neither event attracted any visitors at all', 'Expo 86 took place before Expo 67'], 0)]),
]),
day(177, [
L('Vocabulary: Collective Nouns for Groups of Animals',
  'Grade 8 Language strand: a collective noun names a group of people, animals, or things as a single unit, and English contains many specific, sometimes unusual, collective nouns for groups of animals, such as a murder of crows or a pod of whales.',
  [('What is a collective noun?', ['A noun that names a group of people, animals, or things as a single unit', 'A noun that can never be made plural', 'A noun that only names a single object', 'A noun used exclusively for describing colours'], 0),
   ('Which is the correct collective noun for a group of crows?', ['A murder', 'A pod', 'A pack', 'A herd'], 0),
   ('Which is the correct collective noun for a group of whales?', ['A pod', 'A murder', 'A flock', 'A gaggle'], 0),
   ('Which is the correct collective noun for a group of lions?', ['A pride', 'A litter', 'A colony', 'A troop'], 0),
   ('Why might a writer choose a specific, unusual collective noun rather than simply writing a group of?', ['It can add precision and vivid imagery to descriptive writing', 'It always makes a sentence grammatically incorrect', 'Specific collective nouns are never used in English', 'It removes all meaning from a sentence'], 0)]),
M('Statistics: An Introduction to Sampling Methods and Bias',
  'Grade 8 Math strand: a sample is a smaller group selected to represent a larger population, and the method used to choose that sample, such as random sampling or convenience sampling, can introduce bias that affects how well the results represent the whole population.',
  [('What is a sample in statistics?', ['A smaller group selected to represent a larger population', 'The entire population being studied', 'A single data point with no other information', 'A graph showing every possible outcome'], 0),
   ('What is random sampling designed to do?', ['Give every member of a population an equal chance of being selected', 'Guarantee that only one type of person is selected', 'Select only the easiest people to reach', 'Remove the need for any sample at all'], 0),
   ('What is convenience sampling?', ['Selecting whichever individuals are easiest to reach rather than a truly random group', 'Selecting a sample using a computer-generated random number list', 'Surveying every single member of a population', 'A method that always produces a perfectly unbiased sample'], 0),
   ('How can sampling bias affect the results of a survey?', ['It can make the results fail to accurately represent the larger population', 'It always makes results more accurate than a full survey', 'It has no effect on the reliability of survey results', 'Bias can only occur when sampling animals, not people'], 0),
   ('Why do statisticians carefully consider their sampling method before conducting a survey?', ['A poorly chosen sample can lead to conclusions that do not reflect the true population', 'Sampling methods never influence the outcome of a survey', 'Every sampling method always produces identical results', 'Sampling is only relevant when studying very large populations'], 0)]),
Sc('Chemistry: The Science of Food Preservation',
   'Grade 8 Science strand: food preservation methods such as refrigeration, drying, and canning slow or prevent the chemical and microbial processes that cause food to spoil, extending how long food remains safe to eat.',
   [('What is the main goal of food preservation methods?', ['To slow or prevent processes that cause food to spoil', 'To make food taste completely different', 'To remove all nutrients from food', 'To increase the speed of spoilage'], 0),
    ('How does refrigeration help preserve food?', ['It slows the growth of microorganisms that cause spoilage', 'It speeds up chemical reactions that cause spoilage', 'It removes all water from the food instantly', 'It has no effect on microorganisms at all'], 0),
    ('How does drying food help preserve it?', ['It removes moisture that microorganisms need to grow', 'It adds extra moisture to prevent spoilage', 'It increases the temperature of the food indefinitely', 'It has no connection to microbial growth'], 0),
    ('What happens to food during the canning process that helps preserve it?', ['It is heated to destroy microorganisms and then sealed in an airtight container', 'It is left open to the air to absorb oxygen', 'It is frozen solid before being left unsealed', 'It is exposed to sunlight for several days'], 0),
    ('Why is understanding food preservation important for reducing food waste and foodborne illness?', ['Proper preservation methods can extend how long food remains safe, reducing spoilage and health risks', 'Food preservation has no effect on food safety', 'All food spoils at exactly the same rate regardless of preservation', 'Preservation methods always make food unsafe to eat'], 0)]),
H('The Air India Bombing of 1985',
  'Grade 8 History strand: on June 23, 1985, a bomb planted by extremists based in Canada destroyed Air India Flight 182 over the Atlantic Ocean, killing 329 people, an event that remains the deadliest terrorist attack connected to Canada and led to major reforms in aviation security.',
  [('On what date did the Air India bombing occur?', ['June 23, 1985', 'July 1, 1967', 'September 11, 1985', 'December 6, 1985'], 0),
   ('What was the flight number of the aircraft destroyed in the bombing?', ['Air India Flight 182', 'Air Canada Flight 143', 'Air India Flight 101', 'Air Canada Flight 182'], 0),
   ('Approximately how many people died in the Air India bombing?', ['329', '100', '29', '929'], 0),
   ('What did the bombing lead to changes in?', ['Aviation security procedures', 'The design of Canadian currency', 'The structure of the Canadian Senate', 'The boundaries of Canadian provinces'], 0),
   ('Why is the Air India bombing considered a significant and tragic event in Canadian history?', ['It remains the deadliest terrorist attack connected to Canada and prompted major reforms in security and later investigations', 'It had no lasting impact on Canadian policy of any kind', 'It involved no Canadian citizens or connections whatsoever', 'It occurred entirely outside of any historical record'], 0)]),
]),
day(178, [
L('Reading: Analyzing Epigraphs and Their Function in a Text',
  'Grade 8 Language strand: an epigraph is a short quotation or phrase placed at the beginning of a text, chapter, or section that can hint at a central theme, set a tone, or offer a lens through which to interpret what follows.',
  [('What is an epigraph?', ['A short quotation or phrase placed at the start of a text or chapter', 'The final sentence of a novel', 'A footnote at the bottom of a page', 'A summary printed on the back cover of a book'], 0),
   ('What can an epigraph hint at before a reader begins a chapter or text?', ['A central theme or idea explored in the text that follows', 'The exact page count of the book', 'The authors home address', 'The price of the book'], 0),
   ('Where is an epigraph typically located in a text?', ['At the very beginning of a text, chapter, or section', 'Only in the final paragraph of a story', 'Inside the table of contents', 'On the spine of a book'], 0),
   ('Why might an author choose someone elses words as an epigraph rather than writing an original line?', ['A well-chosen quotation can connect the text to a larger idea, tradition, or conversation', 'Authors are required by law to include a quotation from another writer', 'An epigraph must always be written by the author of the text', 'Epigraphs are never allowed to quote another source'], 0),
   ('Why should a careful reader pause to consider an epigraph before reading further?', ['It may offer a useful lens for interpreting the theme or tone of what follows', 'Epigraphs are always unrelated to the rest of the text', 'Skipping an epigraph never affects understanding of a text', 'An epigraph always reveals the complete ending of a story'], 0)]),
M('Probability: An Introduction to Geometric Probability',
  'Grade 8 Math strand: geometric probability calculates the likelihood of an outcome using the ratio of a favourable area, length, or region to the total possible area, length, or region, rather than counting individual discrete outcomes.',
  [('What does geometric probability compare?', ['The ratio of a favourable area, length, or region to the total possible area, length, or region', 'The number of dice rolled in a single game', 'The exact number of coins flipped in an experiment', 'The colour of a randomly chosen shape'], 0),
   ('How does geometric probability differ from counting discrete outcomes, such as rolling a die?', ['It uses continuous measurements like area or length instead of counting separate outcomes', 'It can only be used with a standard six-sided die', 'It never involves any kind of ratio', 'It always produces a probability greater than one'], 0),
   ('Which situation could be modeled using geometric probability?', ['The chance that a randomly thrown dart lands within a specific region of a target', 'The chance of rolling a six on a single die', 'The chance of flipping heads on a single coin', 'The chance of drawing a specific card from a deck'], 0),
   ('In geometric probability, what happens to the calculated probability if the favourable region takes up half of the total region?', ['The probability is one half', 'The probability is always one', 'The probability is always zero', 'The probability cannot be calculated'], 0),
   ('Why is geometric probability useful in situations that counting alone cannot easily solve?', ['It allows probability to be calculated for continuous outcomes, such as a location within an area, rather than only separate, countable outcomes', 'It removes the need to ever calculate a ratio', 'It only applies to situations involving whole numbers', 'It cannot be applied to any real-world situation'], 0)]),
Sc('Biology: The Human Skin Microbiome',
   'Grade 8 Science strand: the skin microbiome is the community of bacteria, fungi, and other microorganisms that naturally live on human skin, many of which help protect against harmful pathogens and support healthy skin function.',
   [('What is the skin microbiome?', ['The community of microorganisms that naturally live on human skin', 'A layer of dead skin cells only', 'A type of sunscreen ingredient', 'A disease that affects only the hands'], 0),
    ('What types of organisms can be part of the skin microbiome?', ['Bacteria and fungi', 'Only viruses', 'Only insects', 'Only plant cells'], 0),
    ('What is one beneficial role that some skin microorganisms play?', ['Helping protect the skin against harmful pathogens', 'Causing every type of skin infection', 'Destroying the skins ability to heal', 'Removing all moisture from the skin permanently'], 0),
    ('What might happen to the skin microbiome after excessive use of harsh antibacterial products?', ['Beneficial microorganisms could be disrupted along with harmful ones', 'The skin microbiome would become permanently unaffected', 'All harmful bacteria would be destroyed with no other effect', 'The skin microbiome would immediately double in size'], 0),
    ('Why do scientists study the skin microbiome as part of understanding human health?', ['It may influence skin conditions and overall immune protection, making it relevant to health research', 'The skin microbiome has no connection to human health', 'Skin microorganisms are identical in every single person', 'Studying microorganisms provides no useful scientific information'], 0)]),
H('The Development of the Canadarm and Canadas Space Program',
  'Grade 8 History strand: first used on a NASA Space Shuttle mission in 1981, the Canadarm was a robotic arm designed and built by Canadian engineers, becoming a celebrated symbol of Canadian achievement in space technology and engineering.',
  [('In what year was the Canadarm first used on a Space Shuttle mission?', ['1981', '1967', '1949', '1999'], 0),
   ('What kind of device is the Canadarm?', ['A robotic arm', 'A type of rocket engine', 'A weather satellite', 'A space telescope'], 0),
   ('Who designed and built the Canadarm?', ['Canadian engineers', 'American astronauts only', 'A French aerospace company', 'The Soviet space program'], 0),
   ('What space program did the Canadarm operate as part of?', ['The NASA Space Shuttle program', 'The Apollo Moon landing program', 'A purely Canadian solo space mission', 'The International Space Station alone, before any shuttle existed'], 0),
   ('Why is the Canadarm considered an important symbol of Canadian achievement?', ['It demonstrated advanced Canadian engineering on the international stage of space exploration', 'It was never actually used in space', 'It was designed entirely by a country other than Canada', 'It had no connection to any space mission'], 0)]),
]),
day(179, [
L('Writing: Writing a Letter to the Editor',
  'Grade 8 Language strand: a letter to the editor is a brief, persuasive piece of writing sent to a newspaper or publication that responds to a current issue or article, stating a clear opinion and supporting it with reasons or evidence.',
  [('What is a letter to the editor?', ['A brief, persuasive letter sent to a newspaper responding to a current issue', 'A private letter never intended to be published', 'A formal legal document', 'A summary of a novel written for a class assignment'], 0),
   ('What should a letter to the editor clearly state?', ['A clear opinion supported by reasons or evidence', 'A list of unrelated facts with no opinion', 'Only a greeting with no further content', 'A complete biography of the writer'], 0),
   ('Why do letters to the editor typically stay brief and focused?', ['Newspapers have limited space and readers expect a concise argument', 'Newspapers never place any limit on how long a letter can be', 'Brevity makes an argument automatically weaker', 'Editors refuse to read any letter longer than one word'], 0),
   ('What often prompts someone to write a letter to the editor?', ['A response to a recent article or a current community issue', 'A requirement to summarize an unrelated novel', 'A desire to submit a piece of fiction', 'A request from a friend to write about the weather'], 0),
   ('Why can a well-written letter to the editor be an effective form of civic participation?', ['It allows a member of the public to share an opinion and potentially influence public discussion', 'Letters to the editor are never read by anyone', 'This form of writing has no connection to real community issues', 'Only elected officials are permitted to write to a newspaper'], 0)]),
M('Statistics: An Introduction to Percentiles and Quartiles',
  'Grade 8 Math strand: a percentile indicates the percentage of data values in a set that fall below a given value, and quartiles divide an ordered data set into four equal parts, with the second quartile equal to the median.',
  [('What does a percentile indicate?', ['The percentage of data values in a set that fall below a given value', 'The exact number of data points in a set', 'The largest value in a data set', 'The colour used in a graph of the data'], 0),
   ('How many equal parts do quartiles divide an ordered data set into?', ['Four', 'Two', 'Ten', 'One hundred'], 0),
   ('Which quartile is equal to the median of a data set?', ['The second quartile', 'The first quartile', 'The third quartile', 'The fourth quartile'], 0),
   ('If a students test score is at the 90th percentile, what does that mean?', ['The students score is higher than about ninety percent of other scores in the set', 'The student answered exactly ninety percent of the questions correctly', 'The student scored in the bottom ten percent of the class', 'The student is ninety years old'], 0),
   ('Why are percentiles and quartiles useful for interpreting a large data set?', ['They summarize how a specific value compares to the overall spread of the data', 'They eliminate the need to ever collect data', 'They always describe exactly the same information as the mean', 'They can only be used with data sets smaller than ten values'], 0)]),
Sc('Genetics: Genetic Testing and Personalized Medicine',
   'Grade 8 Science strand: genetic testing analyzes a persons DNA to identify markers linked to inherited conditions or drug responses, allowing personalized medicine to tailor treatments based on an individuals unique genetic profile.',
   [('What does genetic testing analyze?', ['A persons DNA to identify markers linked to inherited conditions', 'Only a persons blood pressure', 'Only a persons height and weight', 'A persons handwriting'], 0),
    ('What is personalized medicine designed to do?', ['Tailor medical treatment based on an individuals unique genetic profile', 'Provide the exact same treatment to every patient regardless of genetics', 'Eliminate the need for any medical treatment', 'Replace doctors with computers entirely'], 0),
    ('What might genetic testing reveal about how a person responds to certain medications?', ['Whether a specific drug is likely to be effective or cause side effects for that person', 'The exact price of every medication available', 'A persons favourite type of medication', 'Nothing useful about medication at all'], 0),
    ('What is one ethical consideration raised by widespread genetic testing?', ['Concerns about privacy and how genetic information might be used or shared', 'Genetic testing raises no ethical questions of any kind', 'Genetic testing is always required by law for every citizen', 'Genetic information can never be kept private under any system'], 0),
    ('Why is personalized medicine considered a significant shift in how healthcare can be delivered?', ['It moves away from a one-size-fits-all approach toward treatment based on an individuals biology', 'It guarantees that no patient will ever experience an illness again', 'It has no impact on how treatments are chosen', 'It requires removing genetics from medical decisions entirely'], 0)]),
H('The Gouzenko Affair and the Start of the Cold War in Canada',
  'Grade 8 History strand: in 1945, Soviet cipher clerk Igor Gouzenko defected in Ottawa with documents revealing a Soviet spy network operating in Canada, an event that heightened Cold War tensions and shaped Canadian and Western attitudes toward the Soviet Union.',
  [('In what year did the Gouzenko Affair take place?', ['1945', '1917', '1968', '1929'], 0),
   ('What was Igor Gouzenkos role before he defected?', ['A Soviet cipher clerk', 'The Prime Minister of Canada', 'A Canadian diplomat', 'A British spy'], 0),
   ('In which Canadian city did Gouzenko defect?', ['Ottawa', 'Toronto', 'Montreal', 'Halifax'], 0),
   ('What did the documents Gouzenko revealed expose?', ['A Soviet spy network operating in Canada', 'A plan to invade Canada militarily', 'A Canadian plan to spy on the United States', 'A trade agreement between Canada and Britain'], 0),
   ('Why is the Gouzenko Affair considered an important early moment in the Cold War?', ['It was one of the first public events to expose Soviet espionage in the West, heightening tensions between the Soviet Union and Western countries', 'It had no connection to relations between Canada and the Soviet Union', 'It ended all tension between Western countries and the Soviet Union', 'It took place many decades after the Cold War had already ended'], 0)]),
]),
day(180, [
L('Language Review: Grammar, Vocabulary, and Media Literacy (Days 171-179)',
  'Grade 8 Language strand review: students revisit prepositional phrases, acronyms and initialisms, red herrings in mystery fiction, the process essay, and paywalls and the business of online news.',
  [('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A conjunction', 'A comma'], 0),
   ('What is an acronym?', ['A word formed from the first letters of a phrase that is pronounced as a word', 'A word that means the opposite of another word', 'A word borrowed unchanged from another language', 'A word with no vowels at all'], 0),
   ('What is a red herring in a mystery story?', ['A false clue deliberately placed to mislead the reader', 'A character who solves the crime', 'The final piece of evidence that solves the case', 'A summary of the story at its beginning'], 0),
   ('What does a process essay explain?', ['How something works or how to complete a task, in clear steps', 'A single characters physical appearance', 'An unrelated series of historical events', 'The authors opinion with no supporting explanation'], 0),
   ('What is a paywall?', ['A barrier that limits free access to online content until a reader pays or subscribes', 'A type of advertisement shown before a video', 'A tool that blocks all access to the internet', 'A method for translating an article into another language'], 0)]),
M('Math Review: Probability, Number Theory, and Statistics (Days 171-179)',
  'Grade 8 Math strand review: students revisit skewness and distribution shape, triangular numbers, the isoperimetric problem, synthetic division, and the Birthday Paradox.',
  [('What does skewness describe about a data distribution?', ['Its asymmetry, or how unevenly the data is spread', 'The exact number of data points collected', 'The colour used to display a graph', 'The units used to measure the data'], 0),
   ('What is a triangular number?', ['A number formed by summing consecutive whole numbers starting from one', 'A number that is always divisible by three', 'A number that can only be an even number', 'A number with exactly three digits'], 0),
   ('What does the isoperimetric problem ask?', ['Which shape encloses the greatest area for a given perimeter', 'Which shape has the smallest possible perimeter for any area', 'How to calculate the volume of a sphere', 'How to convert a shape into a straight line'], 0),
   ('What does synthetic division provide a shortcut for?', ['Dividing a polynomial by a linear expression', 'Multiplying two polynomials together', 'Finding the square root of a number', 'Graphing a quadratic function'], 0),
   ('What does the Birthday Paradox describe?', ['A surprisingly high probability that two people in a group share a birthday', 'A rule for calculating everyones exact birthday', 'A method for predicting future birthdays', 'A proof that no two people can share a birthday'], 0)]),
Sc('Science Review: Chemistry, Physics, and Space Science (Days 171-179)',
   'Grade 8 Science strand review: students revisit the chemistry of sunscreen, the physics of roller coasters, cloud types and weather prediction, osmosis and diffusion, and space debris.',
   [('What does sunscreen protect the skin from?', ['Ultraviolet radiation from the sun', 'Visible light only', 'Extreme cold temperatures', 'Loud noise'], 0),
    ('What type of energy does a roller coaster car have at the top of a tall hill?', ['Gravitational potential energy', 'Only sound energy', 'Only chemical energy', 'Only thermal energy'], 0),
    ('What are clouds classified by?', ['Their shape and altitude', 'Their exact colour only', 'The number of birds flying near them', 'Their distance from the ocean'], 0),
    ('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from low to high concentration only', 'A process that only occurs in solid materials', 'A process that requires no concentration difference at all'], 0),
    ('What is space debris?', ['Defunct satellites, spent rocket stages, and fragments orbiting Earth', 'A type of natural asteroid belt', 'A cloud of gas found only near the Moon', 'A term for stars that have burned out'], 0)]),
H('History Review: Canadian Institutions and Modern Milestones (Days 171-179)',
  'Grade 8 History strand review: students revisit the introduction of the metric system, the founding of the National Film Board, the creation of the CRTC, the Order of Canada, and the Canadian Human Rights Act.',
  [('In what decade did Canada begin its transition to the metric system?', ['The 1970s', 'The 1860s', 'The 1920s', 'The 1990s'], 0),
   ('In what year was the National Film Board of Canada established?', ['1939', '1867', '1949', '1921'], 0),
   ('What does the abbreviation CRTC stand for?', ['Canadian Radio-television and Telecommunications Commission', 'Canadian Rural Transportation and Trade Council', 'Canadian Research and Technology Coordination Committee', 'Central Regional Telecommunications Control Centre'], 0),
   ('In what year was the Order of Canada created?', ['1967', '1949', '1988', '1921'], 0),
   ('In what year was the Canadian Human Rights Act passed?', ['1977', '1867', '1949', '1988'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_171_180)
    append_to(8, g8_171_180)
