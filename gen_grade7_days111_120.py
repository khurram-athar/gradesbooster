#!/usr/bin/env python3
"""Grade 7, Days 111-120 -- extends Grade 7 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade7.json)
extensively to avoid any overlap: sentence fragments, portmanteau words,
extended metaphor, persuasive letters to local officials, clickbait
headlines, split infinitives/emphatic pronouns, foil characters, letters
of apology, loanwords from other languages; angle of elevation/depression,
dot plots, inflation and purchasing power, nets of 3D shapes, converting
among fractions/decimals/percents, precision/accuracy/significant
figures, multi-variable word problems, circle vocabulary (chord, radius,
diameter), weighted averages; the human eye and vision, wind power,
chemical changes in everyday life (rusting/cooking/baking), plant
reproduction (pollination/seed dispersal), bird adaptations and beak
types, the lymphatic system, hydroelectric power, roller coaster physics,
coral reefs; the Avro Arrow, the Regina Riot and On-to-Ottawa Trek, the
Korean War, the creation of Nunavut, D-Day/Operation Overlord, the
Continuous Journey Regulation, the Alaska Boundary Dispute, the Chanak
Crisis, and the Canadian Wheat Board.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science and Technology',
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


g7_111_120 = [
day(111, [
L('Grammar: Sentence Fragments and How to Fix Them',
  'Grade 7 Language strand: a sentence fragment is an incomplete sentence missing a subject, verb, or complete thought, and writers fix fragments by combining them with a nearby sentence or adding the missing element.',
  [('What is a sentence fragment?', ['An incomplete sentence missing a subject, verb, or complete thought', 'A sentence that is too long', 'A sentence with perfect grammar', 'A type of poem'], 0),
   ('Which of these is a sentence fragment?', ['Running down the street quickly.', 'She ran down the street quickly.', 'The dog barked loudly at the mail carrier.', 'They finished their homework before dinner.'], 0),
   ('What is one way to fix a sentence fragment?', ['Combine it with a nearby complete sentence', 'Add more commas only', 'Delete every word', 'Make it longer with no subject'], 0),
   ('Why do writers sometimes accidentally create fragments?', ['They separate a dependent clause or phrase from the sentence it belongs to', 'Fragments are always intentional in formal writing', 'Fragments are required in every paragraph', 'Fragments cannot be fixed'], 0),
   ('A complete sentence must have at least ___.', ['A subject and a verb expressing a complete thought', 'Only punctuation', 'Ten words', 'A rhyme'], 0)]),
M('Geometry: Angle of Elevation and Depression',
  'Grade 7 Math strand: the angle of elevation is the angle looking upward from a horizontal line to an object, while the angle of depression is the angle looking downward, both used to describe sightlines to distant objects.',
  [('What is the angle of elevation?', ['The angle looking upward from a horizontal line to an object', 'The angle looking straight down', 'The angle between two parallel lines', 'A type of right angle only'], 0),
   ('What is the angle of depression?', ['The angle looking downward from a horizontal line to an object', 'The angle looking straight up', 'An angle equal to zero always', 'A type of circle measurement'], 0),
   ('If you look up at the top of a tall building from the ground, you are measuring ___.', ['An angle of elevation', 'An angle of depression', 'A right angle only', 'A reflex angle only'], 0),
   ('Angle of elevation and depression problems are useful for finding ___.', ['Heights and distances of objects that are hard to measure directly', 'Only the colour of an object', 'The weight of an object', 'The temperature outside'], 0),
   ('Both angle of elevation and depression are measured from a ___ line.', ['Horizontal', 'Vertical', 'Diagonal only', 'Curved'], 0)]),
Sc('The Human Eye and Vision',
   'Grade 7 Science strand: the eye focuses light onto the retina, which converts light into signals sent to the brain, allowing us to see shapes, colours, and movement.',
   [('What does the eye focus light onto?', ['The retina', 'The eardrum', 'The stomach lining', 'The skin'], 0),
    ('What does the retina do with light?', ['Converts it into signals sent to the brain', 'Converts it into sound', 'Blocks all light completely', 'Produces heat only'], 0),
    ('Which part of the eye controls how much light enters?', ['The pupil', 'The eyelash', 'The eyebrow', 'The earlobe'], 0),
    ('Why might a person need glasses?', ['To help focus light correctly onto the retina', 'Glasses have no effect on vision', 'To block all light from entering the eye', 'To change eye colour permanently'], 0),
    ('Vision is processed and interpreted by which organ?', ['The brain', 'The lungs', 'The stomach', 'The liver'], 0)]),
SS('Social Studies: The Avro Arrow and Canadian Aerospace History',
   'Grade 7 Social Studies strand: the Avro Arrow was an advanced Canadian-built jet fighter from the 1950s whose cancellation in 1959 remains a debated moment in Canadian aerospace and technology history.',
   [('What was the Avro Arrow?', ['An advanced Canadian-built jet fighter', 'A type of train', 'A famous Canadian ship', 'A Canadian currency design'], 0),
    ('When was the Avro Arrow program cancelled?', ['In 1959', 'In 2005', 'In 1867', 'It was never cancelled'], 0),
    ('Why is the cancellation of the Avro Arrow still debated by historians?', ['Its cancellation affected Canadian aerospace jobs and technology development', 'It has no historical significance at all', 'It was immediately forgotten with no impact', 'It was replaced the same year with an identical program'], 0),
    ('The Avro Arrow is an example of Canadian achievement in which field?', ['Aerospace engineering and technology', 'Agriculture', 'Music composition', 'Textile manufacturing'], 0),
    ('Studying the Avro Arrow helps students understand ___.', ['How government decisions can shape technology and industry', 'Only sports history', 'Only ancient history', 'Nothing about Canadian history'], 0)]),
]),
day(112, [
L('Vocabulary: Portmanteau Words',
  'Grade 7 Language strand: a portmanteau word blends the sounds and meanings of two words into one, such as brunch (breakfast plus lunch) or smog (smoke plus fog).',
  [('What is a portmanteau word?', ['A word that blends the sounds and meanings of two words', 'A word with only one syllable', 'A word borrowed directly from another language unchanged', 'A punctuation mark'], 0),
   ('Which of these is a portmanteau word?', ['Brunch', 'Table', 'Quickly', 'Happiness'], 0),
   ('The word smog is a blend of which two words?', ['Smoke and fog', 'Small and dog', 'Sky and log', 'Sun and frog'], 0),
   ('Why do new portmanteau words often appear in language?', ['To describe new concepts by combining familiar words', 'Portmanteau words are never created anymore', 'They are always mistakes in writing', 'They replace all existing words'], 0),
   ('Which is an example of a modern portmanteau word?', ['Webinar (web plus seminar)', 'Table', 'Run', 'Blue'], 0)]),
M('Data Management: Constructing and Interpreting Dot Plots',
  'Grade 7 Math strand: a dot plot displays data along a number line, with a dot for each data value, making it easy to see the shape, clusters, and gaps in a small data set.',
  [('What does a dot plot use to represent data?', ['A dot for each data value along a number line', 'Bars of different heights', 'Slices of a circle', 'Coloured squares only'], 0),
   ('What can a dot plot help you easily see?', ['The shape, clusters, and gaps in a data set', 'Only the total sum of all values', 'The colour of the data', 'The alphabet order of items'], 0),
   ('Dot plots are most useful for what kind of data set?', ['A relatively small data set', 'Only data with millions of values', 'Only data with no numbers', 'Only categorical data with no order'], 0),
   ('If several dots stack up at one value on a dot plot, this shows ___.', ['That value occurs frequently in the data', 'An error in the data collection', 'That the value is impossible', 'Nothing meaningful'], 0),
   ('A gap in a dot plot indicates ___.', ['A range of values with no data points', 'The most common value', 'The total number of data points', 'An error that must be removed'], 0)]),
Sc('Renewable Energy: Wind Power Technology',
   'Grade 7 Science strand: wind turbines convert the kinetic energy of moving air into electricity, offering a renewable energy source that produces no direct emissions while operating.',
   [('What do wind turbines convert into electricity?', ['The kinetic energy of moving air', 'Sunlight', 'Chemical energy from fuel', 'Heat from the ground'], 0),
    ('Why is wind power considered a renewable energy source?', ['Wind is naturally replenished and does not run out', 'Wind is a limited, non-renewable resource', 'Wind power requires burning fossil fuels', 'Wind power creates large amounts of pollution while operating'], 0),
    ('What is one advantage of wind power over fossil fuels?', ['It produces no direct emissions while generating electricity', 'It is available in unlimited amounts everywhere on Earth', 'It never depends on weather conditions', 'It requires no technology to harness'], 0),
    ('What might affect how much electricity a wind turbine produces?', ['How strong and consistent the wind is', 'The colour of the turbine blades', 'The time of year only, with no other factor', 'The price of oil'], 0),
    ('Wind turbines are often grouped together in what is called a ___.', ['Wind farm', 'Solar farm', 'Power plant only', 'Water treatment facility'], 0)]),
SS('Social Studies: The Regina Riot and the On-to-Ottawa Trek',
   'Grade 7 Social Studies strand: during the Great Depression, unemployed workers organized the On-to-Ottawa Trek to demand better conditions, which ended in a violent clash known as the Regina Riot in 1935.',
   [('What was the On-to-Ottawa Trek?', ['A protest journey by unemployed workers during the Great Depression', 'A celebration of Confederation', 'A trade agreement', 'A type of railway construction project'], 0),
    ('What were the trekkers demanding?', ['Better conditions and jobs during the Great Depression', 'Lower taxes for wealthy citizens', 'A new national anthem', 'A new capital city'], 0),
    ('What event stopped the trek and turned violent in 1935?', ['The Regina Riot', 'The Halifax Explosion', 'The October Crisis', 'The Winnipeg General Strike'], 0),
    ('Why did the government intervene in the On-to-Ottawa Trek?', ['Officials feared the growing protest movement reaching Ottawa', 'The government fully supported the trek from the start', 'There was no government reaction at all', 'The trekkers were never near Ottawa'], 0),
    ('The Regina Riot and On-to-Ottawa Trek reflect the hardships of ___.', ['The Great Depression era in Canada', 'Modern Canadian history', 'The early colonial period', 'World War II'], 0)]),
]),
day(113, [
L('Reading: Analyzing Extended Metaphor',
  'Grade 7 Language strand: an extended metaphor develops a single comparison across multiple lines, sentences, or an entire text, deepening meaning by exploring the comparison from different angles.',
  [('What is an extended metaphor?', ['A comparison developed across multiple lines or an entire text', 'A comparison used only once in a single sentence', 'A literal statement with no comparison', 'A type of punctuation'], 0),
   ('How does an extended metaphor differ from a simple metaphor?', ['It continues and develops the comparison over a longer passage', 'It never uses any comparison at all', 'It always uses the word like or as', 'It is always exactly one word long'], 0),
   ('Why might an author use an extended metaphor?', ['To deepen meaning by exploring a comparison from different angles', 'To confuse the reader with unrelated ideas', 'To avoid making any point', 'To remove imagery from the text'], 0),
   ('Which is an example of the start of an extended metaphor?', ['Life is a journey, with winding roads and unexpected stops', 'The cat sat on the mat', 'Please close the door', 'Two plus two equals four'], 0),
   ('An extended metaphor can appear across ___.', ['An entire poem or passage', 'Only a single word', 'Only a title', 'Only a footnote'], 0)]),
M('Financial Literacy: Inflation and Purchasing Power',
  'Grade 7 Math strand: inflation is a general rise in prices over time, which reduces purchasing power, meaning the same amount of money buys fewer goods and services than before.',
  [('What is inflation?', ['A general rise in prices over time', 'A general fall in prices over time', 'A type of bank account', 'A fixed price that never changes'], 0),
   ('What happens to purchasing power when inflation occurs?', ['It decreases, so money buys less than before', 'It always increases significantly', 'It stays exactly the same', 'It becomes impossible to measure'], 0),
   ('If a toy cost $10 last year and $12 this year due to inflation, the price has ___.', ['Increased', 'Decreased', 'Stayed the same', 'Become free'], 0),
   ('Why might people want their savings to earn interest higher than the inflation rate?', ['So their money keeps or grows its real purchasing power over time', 'Interest rates never relate to inflation', 'Savings accounts are unaffected by prices', 'Purchasing power always increases automatically'], 0),
   ('Inflation is typically measured using changes in ___.', ['The average prices of goods and services', 'The weather', 'The number of people in a country', 'The length of the calendar year'], 0)]),
Sc('Chemical Changes in Everyday Life: Rusting, Cooking, and Baking',
   'Grade 7 Science strand: rusting, cooking, and baking are all examples of chemical changes, where new substances form and the change is generally difficult or impossible to reverse.',
   [('What type of change is rusting?', ['A chemical change', 'A physical change only', 'No change at all', 'A change in state only'], 0),
    ('Why is cooking an egg considered a chemical change?', ['New substances form and the change cannot easily be reversed', 'The egg simply changes shape with no other change', 'Nothing about the egg actually changes', 'The change can be easily reversed by cooling it'], 0),
    ('What causes metal to rust?', ['A chemical reaction between iron, oxygen, and water', 'Only exposure to sunlight', 'Freezing temperatures alone', 'Loud noises'], 0),
    ('Baking a cake involves a chemical change because ___.', ['New substances form that cannot be turned back into the original batter', 'The batter simply gets colder', 'Nothing changes chemically during baking', 'The cake can be un-baked back into batter'], 0),
    ('Which is a sign that a chemical change has occurred?', ['A new substance forms with different properties', 'The object only changes shape', 'The object only changes size', 'Nothing happens at all'], 0)]),
SS('Social Studies: Canadas Role in the Korean War',
   'Grade 7 Social Studies strand: Canada sent troops as part of a United Nations force during the Korean War (1950-1953) to help defend South Korea, marking an early Cold War military commitment.',
   [('What conflict did Canada send troops to as part of a UN force in the early 1950s?', ['The Korean War', 'World War I', 'The War of 1812', 'The Vietnam War'], 0),
    ('Which country was Canada helping to defend during the Korean War?', ['South Korea', 'North Korea', 'Japan', 'China'], 0),
    ('Roughly when did the Korean War take place?', ['1950 to 1953', 'In the 1700s', 'In the 1990s', 'It has not happened yet'], 0),
    ('The Korean War is often seen as an early example of what larger global conflict?', ['The Cold War', 'World War II', 'The French and Indian War', 'The Napoleonic Wars'], 0),
    ('Canadas involvement in the Korean War reflected its commitment to ___.', ['International cooperation through the United Nations', 'Isolation from world affairs', 'Avoiding all foreign conflicts', 'Only trade agreements'], 0)]),
]),
day(114, [
L('Writing: Writing a Persuasive Letter to a Local Official',
  'Grade 7 Language strand: a persuasive letter to a local official clearly states a concern or request, supports it with reasons and evidence, and uses a respectful, formal tone to encourage action.',
  [('What should a persuasive letter to a local official clearly state?', ['A concern or request', 'Nothing specific at all', 'Only a greeting', 'Only a signature'], 0),
   ('What tone should a letter to a local official generally use?', ['A respectful, formal tone', 'A casual, joking tone', 'An angry, insulting tone', 'No tone at all'], 0),
   ('Why should a persuasive letter include reasons and evidence?', ['To support the request and make it more convincing', 'Evidence is never needed in persuasive writing', 'To confuse the reader on purpose', 'To make the letter longer with no purpose'], 0),
   ('Which is an appropriate closing for a formal letter to an official?', ['Sincerely, followed by your name', 'See ya later', 'No closing is needed', 'A random emoji'], 0),
   ('What is the main goal of a persuasive letter to an official?', ['To encourage the official to take a specific action', 'To simply share random facts with no purpose', 'To avoid making any request', 'To criticize the official with no reasons given'], 0)]),
M('Geometry: Nets of 3D Shapes',
  'Grade 7 Math strand: a net is a two-dimensional pattern that can be folded to form a three-dimensional shape, helping visualize surface area and the structure of solids.',
  [('What is a net in geometry?', ['A two-dimensional pattern that folds into a 3D shape', 'A three-dimensional solid with no flat sides', 'A type of graph', 'A measurement of volume only'], 0),
   ('What can a net help you calculate?', ['The surface area of a 3D shape', 'Only the colour of a shape', 'The weight of an object', 'The temperature of a solid'], 0),
   ('How many rectangular faces does the net of a cube have?', ['Six squares', 'Four squares', 'Three rectangles', 'Two circles'], 0),
   ('What shape would the net of a cylinder typically include?', ['Two circles and one rectangle', 'Six squares', 'Four triangles', 'One pentagon only'], 0),
   ('Why are nets useful when learning about 3D shapes?', ['They help visualize the structure and surface area of solids', 'They have no practical use', 'They only apply to circles', 'They remove the need to understand shapes'], 0)]),
Sc('Plant Reproduction: Pollination and Seed Dispersal',
   'Grade 7 Science strand: plants reproduce through pollination, often with help from insects or wind, and then disperse their seeds by methods like wind, water, or animals to grow in new locations.',
   [('What is pollination?', ['The transfer of pollen that allows plants to reproduce', 'The process of a plant absorbing water', 'The process of a plant losing its leaves', 'A type of photosynthesis'], 0),
    ('What are two common ways pollen is transferred between plants?', ['Insects and wind', 'Only underground roots', 'Only human hands', 'Only rainfall'], 0),
    ('What is seed dispersal?', ['The spreading of seeds away from the parent plant', 'The process of a seed dissolving completely', 'The freezing of a seed', 'The photosynthesis process in leaves'], 0),
    ('Which of these is a method of seed dispersal?', ['Wind carrying seeds through the air', 'Seeds staying permanently attached to the parent plant', 'Seeds dissolving in soil instantly', 'Seeds being destroyed by sunlight'], 0),
    ('Why is seed dispersal important for a plant species?', ['It reduces competition and helps the species spread to new areas', 'It prevents the species from ever growing again', 'It has no benefit to the plant', 'It only happens to already-dead plants'], 0)]),
SS('Social Studies: The Creation of Nunavut in 1999',
   'Grade 7 Social Studies strand: Nunavut became Canadas newest territory in 1999, created through a land claim agreement to give Inuit people greater self-governance over their traditional homeland.',
   [('In what year was Nunavut created?', ['1999', '1867', '1949', '2020'], 0),
    ('What group gained greater self-governance through the creation of Nunavut?', ['Inuit people', 'French settlers', 'British colonists', 'American immigrants'], 0),
    ('How was Nunavut created?', ['Through a land claim agreement', 'By a foreign invasion', 'By a coin toss', 'By accident with no planning'], 0),
    ('What was Nunavut before it became its own territory?', ['Part of the Northwest Territories', 'Part of Quebec', 'Part of Ontario', 'An independent country'], 0),
    ('Why is the creation of Nunavut significant in Canadian history?', ['It represented a major step in Indigenous self-governance', 'It had no significance at all', 'It ended all territories in Canada', 'It was reversed the following year'], 0)]),
]),
day(115, [
L('Media Literacy: Analyzing Clickbait Headlines',
  'Grade 7 Language strand: clickbait headlines use sensational or exaggerated language to attract clicks, often promising more than the actual article delivers, so readers should evaluate headlines critically.',
  [('What is a clickbait headline designed to do?', ['Attract clicks using sensational or exaggerated language', 'Provide only calm, factual summaries', 'Discourage readers from clicking', 'Avoid any emotional language'], 0),
   ('What is a common problem with clickbait headlines?', ['They often promise more than the article actually delivers', 'They always perfectly match the article content', 'They never use exaggeration', 'They are required by law to be accurate'], 0),
   ('Which phrase sounds like typical clickbait?', ['You wont believe what happened next!', 'City council approves new budget', 'Weather forecast for Tuesday', 'Local library extends hours'], 0),
   ('Why should readers evaluate headlines critically?', ['To avoid being misled by exaggerated claims', 'Headlines are always completely trustworthy', 'Evaluating headlines is unnecessary', 'All headlines contain identical information'], 0),
   ('What skill helps readers avoid falling for clickbait?', ['Media literacy and critical thinking', 'Ignoring all news sources', 'Reading only headlines and nothing else', 'Believing every headline without question'], 0)]),
M('Measurement: Converting Among Fractions, Decimals, and Percents',
  'Grade 7 Math strand: fractions, decimals, and percents are different ways to represent the same value, and converting between them is a key skill for solving real-world problems involving parts of a whole.',
  [('What do fractions, decimals, and percents all represent?', ['Different ways to express the same value or part of a whole', 'Three completely unrelated concepts', 'Only whole numbers', 'Only negative numbers'], 0),
   ('What is 1/4 written as a decimal?', ['0.25', '0.4', '0.14', '1.4'], 0),
   ('What is 0.5 written as a percent?', ['50%', '5%', '0.5%', '500%'], 0),
   ('What is 75% written as a fraction in lowest terms?', ['3/4', '7/5', '75/10', '1/75'], 0),
   ('Why is it useful to convert between fractions, decimals, and percents?', ['Different situations and problems call for different representations', 'Conversion is never useful in real life', 'Only one form is ever allowed in math', 'Percentages cannot be converted to fractions'], 0)]),
Sc('Bird Adaptations and Beak Types',
   'Grade 7 Science strand: bird beaks are adapted to the type of food a species eats, such as strong hooked beaks for tearing meat or long thin beaks for probing flowers and insects.',
   [('What determines the shape of a birds beak?', ['The type of food the species typically eats', 'The colour of the birds feathers', 'The time of year only', 'The size of the birds nest'], 0),
    ('What kind of beak would a bird of prey, like a hawk, typically have?', ['A strong, hooked beak for tearing meat', 'A long, thin beak for sipping nectar', 'A flat, wide beak for filtering water', 'No beak at all'], 0),
    ('Why might a hummingbird have a long, thin beak?', ['To reach nectar deep inside flowers', 'To crack open hard seeds', 'To tear meat from prey', 'To dig through soil'], 0),
    ('Beak adaptations are an example of ___.', ['How species evolve traits suited to their environment and diet', 'Random changes with no purpose', 'Features that never affect survival', 'Traits found only in mammals'], 0),
    ('A short, strong, cone-shaped beak, like a finches, is well suited for ___.', ['Cracking open seeds', 'Catching fish underwater', 'Sipping nectar from flowers', 'Tearing large prey apart'], 0)]),
SS('Social Studies: Canadas Role in D-Day and Operation Overlord',
   'Grade 7 Social Studies strand: Canadian troops played a significant role landing at Juno Beach during the D-Day invasion of Normandy in 1944, part of the larger Allied effort known as Operation Overlord.',
   [('What major military operation did D-Day belong to?', ['Operation Overlord', 'The Manhattan Project', 'The Marshall Plan', 'The Berlin Airlift'], 0),
    ('Which beach did Canadian troops land on during D-Day?', ['Juno Beach', 'Omaha Beach', 'Utah Beach', 'Sword Beach'], 0),
    ('In what year did the D-Day invasion take place?', ['1944', '1918', '1929', '1867'], 0),
    ('What was the overall goal of Operation Overlord?', ['To liberate Western Europe from Nazi occupation during World War II', 'To explore the Arctic', 'To build a new railway', 'To establish a trade agreement'], 0),
    ('Why is Canadas role at Juno Beach significant in Canadian history?', ['It demonstrated Canadas major military contribution to World War II', 'It has no significance in Canadian history', 'Canada did not participate in World War II', 'It happened after the war had already ended'], 0)]),
]),
day(116, [
L('Grammar: Split Infinitives and Emphatic Pronouns',
  'Grade 7 Language strand: a split infinitive places a word between to and a verb, like to boldly go, while an emphatic pronoun, like myself or himself, adds emphasis to a noun or pronoun already mentioned.',
  [('What is a split infinitive?', ['A word placed between to and a verb, such as to boldly go', 'A sentence with no verb', 'A type of punctuation mark', 'A pronoun used incorrectly'], 0),
   ('Which sentence contains a split infinitive?', ['She wants to quickly finish her homework.', 'She wants to finish her homework quickly.', 'She finished her homework.', 'She will finish it.'], 0),
   ('What is an emphatic pronoun?', ['A pronoun like myself or himself that adds emphasis', 'A pronoun that replaces a verb', 'A punctuation mark', 'A type of conjunction'], 0),
   ('Which sentence correctly uses an emphatic pronoun?', ['I will do it myself.', 'I will do it him.', 'I will do it they.', 'I will do it we.'], 0),
   ('Is it always grammatically wrong to use a split infinitive?', ['No, many modern style guides accept it when it sounds natural', 'Yes, it is always incorrect in every case', 'Split infinitives do not exist', 'Only in poetry is it ever allowed'], 0)]),
M('Measurement: Precision, Accuracy, and Significant Figures',
  'Grade 7 Math strand: accuracy describes how close a measurement is to the true value, precision describes how consistent repeated measurements are, and significant figures indicate the reliable digits in a measurement.',
  [('What does accuracy describe in measurement?', ['How close a measurement is to the true value', 'How many times a measurement is repeated', 'The colour of the measuring tool', 'The cost of the measuring tool'], 0),
   ('What does precision describe?', ['How consistent repeated measurements are with each other', 'How close a measurement is to being true', 'The units used in a measurement', 'The size of the object only'], 0),
   ('Can a set of measurements be precise but not accurate?', ['Yes, if they are consistent but all far from the true value', 'No, precision and accuracy always mean the same thing', 'Only accuracy exists in measurement', 'Only precision exists in measurement'], 0),
   ('What do significant figures indicate in a measurement?', ['The reliable, meaningful digits in a number', 'Only the first digit of any number', 'The total number of digits after a decimal only', 'Nothing meaningful at all'], 0),
   ('Why do scientists care about precision and accuracy?', ['Reliable measurements are essential for valid conclusions', 'Measurements never need to be reliable', 'Only estimates are ever used in science', 'Precision and accuracy have no scientific use'], 0)]),
Sc('The Lymphatic System and Immunity',
   'Grade 7 Science strand: the lymphatic system helps defend the body against infection by producing and transporting white blood cells and filtering harmful substances through lymph nodes.',
   [('What is one main role of the lymphatic system?', ['Defending the body against infection', 'Digesting food', 'Pumping blood through the heart', 'Producing sound'], 0),
    ('What do lymph nodes do?', ['Filter harmful substances and support immune responses', 'Store extra fat', 'Produce sound waves', 'Control body temperature only'], 0),
    ('What type of cells does the lymphatic system help transport?', ['White blood cells', 'Red blood cells only', 'Skin cells only', 'Muscle cells only'], 0),
    ('Why might lymph nodes swell when a person is sick?', ['They are actively working to fight off infection', 'Swelling always means the lymphatic system has failed', 'Swelling is unrelated to illness', 'Lymph nodes cannot change size'], 0),
    ('The lymphatic system works closely with which other body system?', ['The circulatory system', 'The skeletal system only', 'The digestive system only', 'The reproductive system only'], 0)]),
SS('Social Studies: The Continuous Journey Regulation',
   'Grade 7 Social Studies strand: the Continuous Journey Regulation was a 1908 Canadian immigration law requiring immigrants to travel directly from their home country, effectively restricting immigration from India and other parts of Asia.',
   [('What did the Continuous Journey Regulation require of immigrants?', ['Traveling directly, without stops, from their home country', 'Nothing at all, since it applied to no one', 'Owning property in Canada before arrival', 'Speaking French fluently'], 0),
    ('What was the real effect of the Continuous Journey Regulation?', ['It restricted immigration from India and other parts of Asia', 'It encouraged immigration from around the world equally', 'It had no effect on immigration policy', 'It only applied to European immigrants'], 0),
    ('In what year was the Continuous Journey Regulation introduced?', ['1908', '1950', '1867', '1999'], 0),
    ('Which later event is connected to the Continuous Journey Regulation?', ['The Komagata Maru Incident', 'The Halifax Explosion', 'The October Crisis', 'The Klondike Gold Rush'], 0),
    ('Why do historians study laws like the Continuous Journey Regulation today?', ['To understand the history of discrimination in Canadian immigration policy', 'These laws have no historical relevance', 'They show only positive immigration history', 'They were never actually enforced'], 0)]),
]),
day(117, [
L('Reading: Analyzing Foil Characters in Literature',
  'Grade 7 Language strand: a foil character has traits that contrast sharply with a main character, and this contrast helps highlight and clarify the main characters own qualities.',
  [('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0),
   ('What is the purpose of a foil character?', ['To highlight and clarify the main characters qualities through contrast', 'To confuse the reader about the plot', 'To replace the main character entirely', 'To remove all conflict from the story'], 0),
   ('If a main character is shy, a foil character might be ___.', ['Outgoing and bold', 'Also shy in the exact same way', 'Nonexistent in the story', 'A narrator only'], 0),
   ('Foil characters are most useful for revealing ___.', ['Personality traits through comparison', 'Only the setting of a story', 'Only the time period of a story', 'Nothing about the characters'], 0),
   ('Which is an example of a foil relationship?', ['A reckless character paired with a cautious character', 'Two identical characters with no differences', 'A character and the weather', 'A character and a map'], 0)]),
M('Algebra: Solving Multi-Variable Word Problems',
  'Grade 7 Math strand: multi-variable word problems involve translating real-world situations with more than one unknown quantity into equations, then solving step by step to find each value.',
  [('What makes a word problem multi-variable?', ['It involves more than one unknown quantity', 'It has no numbers at all', 'It only involves one step', 'It cannot be solved with equations'], 0),
   ('What is the first step in solving a multi-variable word problem?', ['Translating the situation into one or more equations', 'Guessing the answer randomly', 'Ignoring the given information', 'Skipping straight to the final answer'], 0),
   ('If two numbers add to 20 and one is 8 more than the other, what are the numbers?', ['6 and 14', '10 and 10', '8 and 12', '5 and 15'], 0),
   ('Why is it helpful to define variables clearly before solving a word problem?', ['It keeps track of what each unknown quantity represents', 'Variables never need to be defined', 'Definitions make problems harder to solve', 'Only one variable is ever needed'], 0),
   ('After solving for the variables, what should you do?', ['Check that the answers make sense in the original problem', 'Ignore the original problem entirely', 'Immediately discard the answers', 'Assume the answers are always wrong'], 0)]),
Sc('Renewable Energy: Hydroelectric Power',
   'Grade 7 Science strand: hydroelectric power generates electricity by using the energy of flowing or falling water to spin turbines, making it a major renewable energy source in Canada.',
   [('What does hydroelectric power use to generate electricity?', ['The energy of flowing or falling water', 'Sunlight', 'Wind', 'Burning coal'], 0),
    ('What do turbines do in a hydroelectric power system?', ['Spin to convert water energy into electricity', 'Store water for drinking', 'Filter pollutants from water', 'Heat water for cooking'], 0),
    ('Why is hydroelectric power an important energy source in Canada?', ['Canada has many rivers and lakes suited to generating hydro power', 'Canada has no water resources at all', 'Hydro power is illegal in Canada', 'Canada relies only on solar power'], 0),
    ('What structure is often built to control water flow for hydroelectric power?', ['A dam', 'A greenhouse', 'A lighthouse', 'A windmill'], 0),
    ('Hydroelectric power is considered renewable because ___.', ['The water cycle continually replenishes the water supply', 'Water is used up permanently and cannot be replaced', 'It relies on burning fossil fuels', 'It requires mining for coal'], 0)]),
SS('Social Studies: The Alaska Boundary Dispute',
   'Grade 7 Social Studies strand: the Alaska Boundary Dispute was an early 20th-century disagreement between Canada and the United States over the border of the Alaska Panhandle, settled by a tribunal in 1903 in a decision many Canadians saw as unfair.',
   [('What was the Alaska Boundary Dispute about?', ['A disagreement over the border of the Alaska Panhandle', 'A dispute over fishing rights in the Pacific Ocean', 'A disagreement about a railway route', 'A dispute over the Great Lakes'], 0),
    ('Which two countries were involved in the Alaska Boundary Dispute?', ['Canada and the United States', 'Canada and Russia', 'Canada and Britain only', 'The United States and Mexico'], 0),
    ('When was the Alaska Boundary Dispute settled?', ['1903', '1867', '1950', '1999'], 0),
    ('How did many Canadians view the outcome of the dispute?', ['As unfair to Canadian interests', 'As entirely fair and favourable to Canada', 'As having no effect on Canada', 'As a complete victory for Canada'], 0),
    ('The Alaska Boundary Dispute is often cited as an example of ___.', ['Canadas limited independence in foreign affairs at the time', 'Canadas complete independence from Britain by 1903', 'A conflict resolved through war', 'An issue unrelated to Canadian sovereignty'], 0)]),
]),
day(118, [
L('Writing: Writing a Letter of Apology',
  'Grade 7 Language strand: a letter of apology clearly acknowledges a mistake, expresses genuine regret, and often includes a plan to make things right or avoid repeating the mistake.',
  [('What should a letter of apology clearly acknowledge?', ['The mistake that was made', 'Only unrelated topics', 'Nothing specific at all', 'Only the recipients own faults'], 0),
   ('What tone should a letter of apology typically have?', ['Sincere and genuine', 'Sarcastic and joking', 'Angry and blaming', 'Cold and indifferent'], 0),
   ('Why might a letter of apology include a plan to make things right?', ['It shows genuine commitment to correcting the mistake', 'Plans are never appropriate in an apology', 'It shifts all blame onto someone else', 'It replaces the need for an apology'], 0),
   ('Which is an example of a sincere apology statement?', ['I am sorry for missing our meeting, and I will confirm plans earlier next time.', 'It was not really my fault anyway.', 'Sorry, but you overreacted.', 'I do not need to apologize for anything.'], 0),
   ('A well-written apology letter helps to ___.', ['Repair trust and take responsibility', 'Avoid all responsibility', 'Blame someone else entirely', 'Ignore the mistake completely'], 0)]),
M('Geometry: Circle Vocabulary — Chord, Radius, and Diameter',
  'Grade 7 Math strand: a radius connects the centre of a circle to its edge, a diameter passes through the centre connecting two points on the edge, and a chord connects any two points on a circle without necessarily passing through the centre.',
  [('What is a radius?', ['A line from the centre of a circle to its edge', 'A line connecting any two points on a circle', 'The outer edge of a circle', 'The area inside a circle'], 0),
   ('What is a diameter?', ['A line passing through the centre, connecting two points on the edge', 'A line that never touches the circle', 'Half of the radius', 'The circles area'], 0),
   ('How does the diameter relate to the radius?', ['The diameter is twice the length of the radius', 'The diameter is half the radius', 'They are always unrelated', 'The diameter is always zero'], 0),
   ('What is a chord?', ['A line connecting any two points on a circle', 'The exact centre point of a circle', 'A measurement of a circles area', 'A type of angle only'], 0),
   ('Is every diameter also a chord?', ['Yes, because it connects two points on the circle', 'No, a diameter is never a chord', 'Only sometimes, depending on the day', 'A diameter is the same as a radius'], 0)]),
Sc('Physics of Roller Coasters: Energy Transformations',
   'Grade 7 Science strand: roller coasters convert potential energy at the top of hills into kinetic energy as cars speed downward, illustrating the transformation and conservation of mechanical energy.',
   [('What type of energy does a roller coaster car have at the top of a hill?', ['Potential energy', 'Only sound energy', 'Only chemical energy', 'No energy at all'], 0),
    ('What happens to potential energy as the car speeds down a hill?', ['It converts into kinetic energy', 'It disappears completely', 'It converts into sunlight', 'It stays exactly the same amount as potential energy'], 0),
    ('What is kinetic energy?', ['The energy of motion', 'The energy stored due to height', 'The energy of sound only', 'The energy of light only'], 0),
    ('Why do roller coasters usually have their highest hill first?', ['To build up the maximum potential energy needed for the ride', 'Height has no effect on the ride', 'To make the ride slower overall', 'To eliminate all kinetic energy'], 0),
    ('Roller coasters demonstrate what general scientific principle?', ['The conservation and transformation of energy', 'That energy can be created from nothing', 'That energy disappears permanently during motion', 'That motion requires no energy at all'], 0)]),
SS('Social Studies: The Chanak Crisis and Canadian Foreign Policy',
   'Grade 7 Social Studies strand: the 1922 Chanak Crisis, in which Britain asked Canada for military support without full consultation, led Canada to assert more independent control over its own foreign policy decisions.',
   [('What did Britain ask of Canada during the Chanak Crisis?', ['Military support in a conflict near Turkey', 'Financial aid for a railway', 'Support for a trade agreement', 'Help building a new capital city'], 0),
    ('When did the Chanak Crisis occur?', ['1922', '1867', '1999', '1950'], 0),
    ('How did Canada respond to Britains request during the Chanak Crisis?', ['Canada asserted the right to decide its own foreign policy rather than automatically agreeing', 'Canada immediately sent troops with no debate', 'Canada declared war on Britain', 'Canada ignored the request entirely with no response'], 0),
    ('Why is the Chanak Crisis considered important in Canadian history?', ['It was an early step toward greater Canadian independence in foreign affairs', 'It had no lasting impact on Canada', 'It ended all ties between Canada and Britain', 'It occurred after Canada already had full independence'], 0),
    ('The Chanak Crisis is often studied alongside which later milestone?', ['The Statute of Westminster', 'The Klondike Gold Rush', 'The Halifax Explosion', 'The building of the St. Lawrence Seaway'], 0)]),
]),
day(119, [
L('Vocabulary: Loanwords from Other Languages',
  'Grade 7 Language strand: a loanword is a word borrowed from another language and adopted into everyday use, such as ballet from French or tsunami from Japanese.',
  [('What is a loanword?', ['A word borrowed from another language and adopted into common use', 'A word invented entirely for a single story', 'A word with no meaning', 'A type of punctuation mark'], 0),
   ('Which English word is a loanword from French?', ['Ballet', 'Table', 'Happy', 'Quickly'], 0),
   ('Which English word is a loanword from Japanese?', ['Tsunami', 'House', 'Water', 'Friend'], 0),
   ('Why does English contain so many loanwords?', ['English has borrowed words through centuries of contact with other languages and cultures', 'English never borrows words from other languages', 'Loanwords are always removed from English', 'English has no history of language contact'], 0),
   ('Loanwords show that languages ___.', ['Influence and enrich each other over time', 'Never interact with one another', 'Are always identical to each other', 'Cannot change over time'], 0)]),
M('Data Management: Weighted Averages',
  'Grade 7 Math strand: a weighted average gives different values different levels of importance before averaging, used when some data points should count more than others, such as test scores worth different percentages.',
  [('What does a weighted average take into account that a regular average does not?', ['Different levels of importance for different values', 'Only the largest value in a data set', 'Only the smallest value in a data set', 'Nothing different from a regular average'], 0),
   ('When might a weighted average be more appropriate than a simple average?', ['When some values, like test scores, should count more than others', 'When every value is exactly equal in importance', 'Weighted averages are never useful', 'Only when there is a single data point'], 0),
   ('If a test is worth 70% of a grade and a quiz is worth 30%, this reflects ___.', ['A weighted average calculation', 'A simple, unweighted average', 'An irrelevant piece of information', 'A probability calculation'], 0),
   ('In a weighted average, values with a higher weight ___.', ['Have a greater effect on the final result', 'Are always ignored', 'Have no effect on the result', 'Cancel out other values completely'], 0),
   ('Weighted averages are commonly used to calculate ___.', ['Final course grades from multiple assessments', 'The colour of a graph', 'The shape of a triangle', 'The temperature outside'], 0)]),
Sc('Coral Reefs and Ocean Ecosystems',
   'Grade 7 Science strand: coral reefs are diverse underwater ecosystems built by tiny coral organisms, providing habitat for countless marine species while being sensitive to changes in ocean temperature and acidity.',
   [('What builds a coral reef?', ['Tiny coral organisms', 'Large fish only', 'Ocean currents alone', 'Underwater volcanoes only'], 0),
    ('Why are coral reefs considered important ecosystems?', ['They provide habitat for a huge diversity of marine species', 'They support no marine life at all', 'They exist only in freshwater lakes', 'They have no ecological importance'], 0),
    ('What environmental changes can harm coral reefs?', ['Rising ocean temperature and increased acidity', 'Cooler ocean temperatures only', 'Increased oxygen levels only', 'Decreased sunlight only, with no other cause'], 0),
    ('What is coral bleaching?', ['A stress response where coral loses its colour and often dies without recovery', 'A natural, harmless colour change with no consequences', 'A process that makes coral healthier', 'A type of coral reproduction'], 0),
    ('Coral reefs are sometimes called the rainforests of the sea because ___.', ['They support extremely high levels of biodiversity', 'They contain actual trees underwater', 'They have no living organisms', 'They are located on land'], 0)]),
SS('Social Studies: The Canadian Wheat Board and the Grain Industry',
   'Grade 7 Social Studies strand: the Canadian Wheat Board was a government-created organization that once controlled the marketing and sale of wheat and barley from Western Canadian farmers, playing a major role in the prairie grain industry for decades.',
   [('What did the Canadian Wheat Board historically control?', ['The marketing and sale of wheat and barley from Western Canadian farmers', 'The entire Canadian banking system', 'All immigration into Canada', 'The construction of national parks'], 0),
    ('Which region of Canada was most affected by the Canadian Wheat Board?', ['The Prairie provinces', 'The Atlantic provinces', 'Northern territories only', 'Southern Ontario only'], 0),
    ('Why might farmers have supported a single marketing organization like the Wheat Board?', ['It gave them collective bargaining power when selling their grain', 'It prevented farmers from ever selling their grain', 'It had no effect on farmers incomes', 'It only benefited large corporations, never farmers'], 0),
    ('The grain industry has historically been a major part of which sector of the Canadian economy?', ['Agriculture', 'Mining', 'Aerospace', 'Fishing'], 0),
    ('Studying the Canadian Wheat Board helps students understand ___.', ['The role of government in regulating agricultural economies', 'Only modern technology', 'Only Canadian foreign policy', 'Only urban city planning'], 0)]),
]),
day(120, [
L('Language Review: Grammar, Vocabulary, and Reading Strategies',
  'Grade 7 Language strand review: students revisit sentence fragments, portmanteau words, extended metaphor, clickbait headlines, split infinitives and emphatic pronouns, foil characters, and loanwords.',
  [('What is a sentence fragment?', ['An incomplete sentence missing a subject, verb, or complete thought', 'A sentence that is too long', 'A sentence with perfect grammar', 'A type of poem'], 0),
   ('What is a portmanteau word?', ['A word that blends the sounds and meanings of two words', 'A word with only one syllable', 'A word borrowed directly from another language unchanged', 'A punctuation mark'], 0),
   ('What is an extended metaphor?', ['A comparison developed across multiple lines or an entire text', 'A comparison used only once in a single sentence', 'A literal statement with no comparison', 'A type of punctuation'], 0),
   ('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0),
   ('What is a loanword?', ['A word borrowed from another language and adopted into common use', 'A word invented entirely for a single story', 'A word with no meaning', 'A type of punctuation mark'], 0)]),
M('Math Review: Geometry, Measurement, and Data',
  'Grade 7 Math strand review: students revisit angle of elevation and depression, dot plots, inflation, nets of 3D shapes, precision and significant figures, circle vocabulary, and weighted averages.',
  [('What is the angle of elevation?', ['The angle looking upward from a horizontal line to an object', 'The angle looking straight down', 'The angle between two parallel lines', 'A type of right angle only'], 0),
   ('What is inflation?', ['A general rise in prices over time', 'A general fall in prices over time', 'A type of bank account', 'A fixed price that never changes'], 0),
   ('What is a net in geometry?', ['A two-dimensional pattern that folds into a 3D shape', 'A three-dimensional solid with no flat sides', 'A type of graph', 'A measurement of volume only'], 0),
   ('What is a diameter?', ['A line passing through the centre, connecting two points on the edge', 'A line that never touches the circle', 'Half of the radius', 'The circles area'], 0),
   ('What does a weighted average take into account that a regular average does not?', ['Different levels of importance for different values', 'Only the largest value in a data set', 'Only the smallest value in a data set', 'Nothing different from a regular average'], 0)]),
Sc('Science Review: Body Systems, Energy, and Ecosystems',
   'Grade 7 Science strand review: students revisit the human eye, wind power, chemical changes, pollination and seed dispersal, bird beak adaptations, the lymphatic system, hydroelectric power, roller coaster energy, and coral reefs.',
   [('What does the eye focus light onto?', ['The retina', 'The eardrum', 'The stomach lining', 'The skin'], 0),
    ('What do wind turbines convert into electricity?', ['The kinetic energy of moving air', 'Sunlight', 'Chemical energy from fuel', 'Heat from the ground'], 0),
    ('What is pollination?', ['The transfer of pollen that allows plants to reproduce', 'The process of a plant absorbing water', 'The process of a plant losing its leaves', 'A type of photosynthesis'], 0),
    ('What does hydroelectric power use to generate electricity?', ['The energy of flowing or falling water', 'Sunlight', 'Wind', 'Burning coal'], 0),
    ('What builds a coral reef?', ['Tiny coral organisms', 'Large fish only', 'Ocean currents alone', 'Underwater volcanoes only'], 0)]),
SS('Social Studies Review: 20th-Century Canadian History',
   'Grade 7 Social Studies strand review: students revisit the Avro Arrow, the Regina Riot and On-to-Ottawa Trek, the Korean War, the creation of Nunavut, D-Day, the Continuous Journey Regulation, the Alaska Boundary Dispute, and the Chanak Crisis.',
   [('What was the Avro Arrow?', ['An advanced Canadian-built jet fighter', 'A type of train', 'A famous Canadian ship', 'A Canadian currency design'], 0),
    ('What event stopped the On-to-Ottawa Trek and turned violent in 1935?', ['The Regina Riot', 'The Halifax Explosion', 'The October Crisis', 'The Winnipeg General Strike'], 0),
    ('In what year was Nunavut created?', ['1999', '1867', '1949', '2020'], 0),
    ('Which beach did Canadian troops land on during D-Day?', ['Juno Beach', 'Omaha Beach', 'Utah Beach', 'Sword Beach'], 0),
    ('What did Britain ask of Canada during the Chanak Crisis?', ['Military support in a conflict near Turkey', 'Financial aid for a railway', 'Support for a trade agreement', 'Help building a new capital city'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_111_120)
    append_to(7, g7_111_120)
