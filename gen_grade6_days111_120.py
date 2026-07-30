#!/usr/bin/env python3
"""Grade 6, Days 111-120 -- extends Grade 6 from 110 to 120 days. Modeled
exactly on gen_grade6_days101_110.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-110
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: writing a
haiku, onomatopoeia and alliteration, epistolary writing, frame
narratives, podcast scripts, straight news writing (inverted pyramid),
graphic organizers, texting language vs formal writing, and screenplay
scenes for Language; cone/pyramid volume, scatter plots, absolute value,
imperial/metric conversion, outliers, sphere surface area, rational vs
irrational numbers, credit cards and interest, and cross-multiplication
proportions for Math; the human ear, antibiotics, nutrition and food
groups, owls, bats and echolocation, groundwater/aquifers, sleep, battery
storage, and the human brain for Science; and the RCMP, the census,
sister cities, Terry Fox, the Franklin Expedition, the history of
Canadian currency, the Auditor General, the Magna Carta's influence on
Canadian law, and the Klondike Gold Rush for Social Studies -- none of
those exact ideas appear in Days 1-110. Day 120 is a review day across
all four subjects, matching the end-of-batch pattern used in every prior
10-day batch. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes are avoided or use
the curly Unicode form, matching the rest of Grade 6.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science and Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


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


g6_111_120 = [
day(111, [
L('Poetry: Writing a Haiku',
  'Grade 6 Language strand: a haiku is a three-line Japanese poem with a 5-7-5 syllable pattern, traditionally focused on nature or a single vivid moment.',
  [('How many lines does a haiku have?', ['Three', 'Two', 'Four', 'Five'], 0),
   ('What is the traditional syllable pattern of a haiku?', ['5-7-5', '4-4-4', '7-5-7', '3-3-3'], 0),
   ('What subject do haiku poems traditionally focus on?', ['Nature or a single vivid moment', 'Long historical events', 'Complex arguments', 'Grocery lists'], 0),
   ('Where does the haiku form originate from?', ['Japan', 'France', 'England', 'Egypt'], 0),
   ('Why might a haikus short length be challenging to write?', ['Every word must be chosen carefully to fit the syllable count', 'Length does not matter in a haiku', 'Haiku have no rules at all', 'Haiku must always rhyme'], 0)]),
M('Geometry: Volume of Cones and Pyramids',
  'Grade 6 Math strand: the volume of a cone or pyramid is one-third the volume of a cylinder or prism with the same base area and height.',
  [('The volume of a cone is what fraction of a cylinder with the same base and height?', ['One-third', 'One-half', 'Two-thirds', 'The same as the cylinder'], 0),
   ('The volume of a pyramid is what fraction of a prism with the same base and height?', ['One-third', 'One-half', 'Three-quarters', 'The same as the prism'], 0),
   ('If a cylinder has a volume of 120 cubic units, what is the volume of a cone with the same base and height?', ['40', '60', '80', '120'], 0),
   ('What two measurements are typically needed to find the volume of a pyramid?', ['Base area and height', 'Only the height', 'Only the base area', 'Only the radius'], 0),
   ('Volume of any 3D shape is expressed in ___.', ['Cubic units', 'Square units', 'Linear units only', 'No units at all'], 0)]),
Sc('The Human Ear and How We Hear',
   'Grade 6 Science strand: the ear collects sound vibrations and converts them into signals the brain interprets as sound, using structures like the eardrum and inner ear.',
   [('What does the ear collect and convert into signals?', ['Sound vibrations', 'Light waves', 'Chemical signals', 'Heat energy'], 0),
    ('What structure vibrates when sound waves enter the ear?', ['The eardrum', 'The pupil', 'The tongue', 'The nose'], 0),
    ('Where are these signals ultimately interpreted as sound?', ['The brain', 'The stomach', 'The lungs', 'The skin'], 0),
    ('Why is protecting our ears from very loud sounds important?', ['Loud sounds can damage hearing over time', 'Loud sounds always improve hearing', 'Ears cannot be damaged', 'Sound has no effect on ears'], 0),
    ('The ear is part of which body system?', ['The nervous system (sensory)', 'The digestive system', 'The skeletal system', 'The circulatory system'], 0)]),
SS('Social Studies: The RCMP — Canadas National Police Force',
   'Grade 6 Social Studies strand: the Royal Canadian Mounted Police, or RCMP, is Canadas national police force, responsible for enforcing federal laws and providing policing services across the country.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is the RCMPs main responsibility?', ['Enforcing federal laws across Canada', 'Teaching in schools', 'Running restaurants', 'Building bridges'], 0),
    ('What is the RCMP historically known for wearing?', ['A red serge uniform', 'A blue business suit', 'A firefighter helmet', 'A chefs apron'], 0),
    ('Why does Canada have both local police and a national police force?', ['Different levels of law enforcement handle different responsibilities', 'National police are unnecessary', 'Only cities need police', 'It replaces all city police'], 0),
    ('The RCMP is an example of a service provided at the ___ level of government.', ['Federal', 'Only municipal', 'Only provincial', 'International'], 0)]),
]),
day(112, [
L('Reading: Onomatopoeia and Alliteration as Sound Devices',
  'Grade 6 Language strand: onomatopoeia uses words that imitate sounds, like buzz or crash, while alliteration repeats beginning consonant sounds, both adding rhythm and vividness to writing.',
  [('What is onomatopoeia?', ['Words that imitate the sounds they describe', 'A type of punctuation', 'A grammar rule', 'A math term'], 0),
   ('Which word is an example of onomatopoeia?', ['Buzz', 'Happy', 'Quickly', 'Table'], 0),
   ('What is alliteration?', ['The repetition of beginning consonant sounds in nearby words', 'A type of rhyme scheme', 'A punctuation mark', 'A number pattern'], 0),
   ('Which phrase uses alliteration?', ['Slippery snakes slither silently', 'The dog ran fast', 'She opened the door', 'They walked home'], 0),
   ('Why do writers use onomatopoeia and alliteration?', ['To add rhythm and vividness to their writing', 'To confuse readers on purpose', 'To remove all sound imagery', 'To make writing purely factual'], 0)]),
M('Data Management: Scatter Plots and Line of Best Fit',
  'Grade 6 Math strand: a scatter plot shows pairs of related data as points, and a line of best fit is a straight line drawn to approximate the overall trend of the data.',
  [('What does a scatter plot show?', ['Pairs of related data as points on a graph', 'A single number', 'Only categories', 'A list of names'], 0),
   ('What is a line of best fit?', ['A line that approximates the overall trend of scattered data', 'A line connecting every single point exactly', 'A line with no relationship to the data', 'A curved line only'], 0),
   ('If data points trend upward together, the correlation is ___.', ['Positive', 'Negative', 'Nonexistent', 'Impossible'], 0),
   ('Why might a line of best fit be useful?', ['It helps predict values and see overall trends', 'It removes the need for any data', 'It always passes through every point', 'It has no practical use'], 0),
   ('A scatter plot with points scattered randomly with no pattern shows ___.', ['Little to no correlation', 'A strong positive correlation', 'A strong negative correlation', 'A perfect line'], 0)]),
Sc('Antibiotics — How They Fight Bacterial Infections',
   'Grade 6 Science strand: antibiotics are medicines that fight bacterial infections by killing bacteria or stopping their growth, but they do not work against viruses.',
   [('What do antibiotics fight?', ['Bacterial infections', 'Viral infections', 'Broken bones', 'Allergies only'], 0),
    ('How do antibiotics typically work?', ['They kill bacteria or stop their growth', 'They cure all illnesses instantly', 'They only treat viruses', 'They have no effect on bacteria'], 0),
    ('Do antibiotics work against viruses like the common cold?', ['No', 'Yes, always', 'Only sometimes with no explanation', 'Antibiotics only treat viruses'], 0),
    ('Why is it important to use antibiotics only when a doctor prescribes them?', ['Overuse can lead to antibiotic-resistant bacteria', 'Antibiotics have no risks', 'They should be used for every illness', 'Doctors are never needed'], 0),
    ('What is antibiotic resistance?', ['When bacteria evolve to survive antibiotics meant to kill them', 'When antibiotics become more effective over time', 'A type of vaccine', 'A kind of allergy'], 0)]),
SS('Social Studies: The Census — Counting Everyone in Canada',
   'Grade 6 Social Studies strand: a census is an official count of everyone living in Canada, conducted regularly to help the government plan services and understand demographic trends.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('Why does the Canadian government conduct a census?', ['To help plan services and understand demographic trends', 'To sell products', 'To have no reason', 'To confuse citizens'], 0),
    ('How often is the Canadian census typically taken?', ['At regular intervals, such as every five years', 'Every single day', 'Only once ever', 'Never'], 0),
    ('Which service might benefit from census information?', ['Planning new schools and hospitals', 'Painting a fence', 'Selling candy', 'Playing a game'], 0),
    ('A census helps a government understand ___.', ['How many people live in different areas', 'The weather forecast', 'Sports scores', 'Movie ratings'], 0)]),
]),
day(113, [
L('Writing: Epistolary Writing — Telling a Story Through Letters',
  'Grade 6 Language strand: epistolary writing tells a story through a series of letters, diary entries, or other documents, letting readers piece together events from multiple viewpoints.',
  [('What is epistolary writing?', ['A story told through letters or similar documents', 'A story with no characters', 'A type of poem only', 'A grammar rule'], 0),
   ('What might an epistolary story be composed of?', ['Letters or diary entries', 'Only pictures', 'Only numbers', 'Only dialogue tags'], 0),
   ('What can epistolary writing allow readers to do?', ['Piece together events from multiple viewpoints', 'See only one perspective forever', 'Skip the story entirely', 'Avoid understanding the plot'], 0),
   ('Which is an example of an epistolary approach?', ['A story told entirely through letters between two characters', 'A story with no writing at all', 'A textbook chapter', 'A dictionary entry'], 0),
   ('Why might a writer choose the epistolary form?', ['To create an intimate, personal feel to the storytelling', 'It removes all personal voice from the writing', 'It always confuses the reader', 'It has no unique effect'], 0)]),
M('Number Sense: Absolute Value',
  'Grade 6 Math strand: absolute value is the distance a number is from zero on a number line, always expressed as a positive value or zero, written as |n|.',
  [('What does absolute value represent?', ['The distance a number is from zero', 'The number itself with no change', 'Only negative numbers', 'A type of fraction'], 0),
   ('What is the absolute value of -7?', ['7', '-7', '0', '14'], 0),
   ('What is the absolute value of 5?', ['5', '-5', '0', '10'], 0),
   ('Can absolute value ever be negative?', ['No, it is always zero or positive', 'Yes, always', 'Only for odd numbers', 'Only for fractions'], 0),
   ('How is absolute value written using symbols?', ['|n|', '(n)', '[n]', '{n}'], 0)]),
Sc('Nutrition and the Food Groups',
   'Grade 6 Science strand: a balanced diet includes foods from different groups, such as fruits, vegetables, grains, and proteins, each providing nutrients the body needs to function well.',
   [('What does a balanced diet include?', ['Foods from different groups, like fruits, vegetables, grains, and proteins', 'Only one type of food', 'No food groups at all', 'Only sugary snacks'], 0),
    ('Why does our body need a variety of nutrients?', ['Different nutrients support different body functions', 'The body needs only one nutrient', 'Nutrients have no effect on the body', 'Variety has no benefit'], 0),
    ('Which food group is a source of protein?', ['Meat, beans, or eggs', 'Only candy', 'Only soda', 'Only chips'], 0),
    ('Why might eating too much sugary or fatty food be unhealthy over time?', ['It can contribute to health problems if not balanced with nutritious foods', 'Sugary food is always the healthiest choice', 'It has no health impact at all', 'The body needs only sugar'], 0),
    ('Nutrition education helps people make informed choices about ___.', ['What they eat to stay healthy', 'Only what they wear', 'Only how they exercise', 'Only how they sleep'], 0)]),
SS('Social Studies: Sister Cities — Twin Communities Around the World',
   'Grade 6 Social Studies strand: sister cities are communities in different countries that form a special partnership to share culture, ideas, and friendship, strengthening global connections.',
   [('What is a sister city?', ['A partner community in another country', 'A city with no people', 'A type of building', 'A kind of holiday'], 0),
    ('Why might two cities become sister cities?', ['To share culture, ideas, and friendship', 'To compete against each other', 'To ignore one another', 'To close their borders'], 0),
    ('What might sister cities share with each other?', ['Cultural events and ideas', 'Nothing at all', 'Only complaints', 'Weather patterns only'], 0),
    ('How can a sister city partnership benefit a community?', ['It builds global connections and cultural understanding', 'It has no benefits', 'It isolates the community further', 'It replaces local government'], 0),
    ('Sister city partnerships can help students learn about ___.', ['Other cultures and communities around the world', 'Only their own city', 'Nothing new', 'Weather forecasting'], 0)]),
]),
day(114, [
L('Reading: Frame Narratives — A Story Within a Story',
  'Grade 6 Language strand: a frame narrative is a story that contains another story inside it, using an outer story to introduce or provide context for the inner tale.',
  [('What is a frame narrative?', ['A story that contains another story inside it', 'A story with no beginning', 'A single-page poem', 'A grammar exercise'], 0),
   ('What does the outer story in a frame narrative usually do?', ['Introduces or provides context for the inner story', 'Has no connection to the inner story', 'Replaces the inner story entirely', 'Is always shorter than a sentence'], 0),
   ('Which is an example of a frame narrative structure?', ['A grandmother telling her grandchild a story from her past', 'A single unbroken scene with one event', 'A dictionary definition', 'A weather report'], 0),
   ('Why might an author use a frame narrative?', ['To add depth or context to the main story', 'To confuse the reader with no purpose', 'To remove the need for characters', 'To avoid telling any story'], 0),
   ('A frame narrative typically has ___.', ['An outer story and an inner story', 'Only one story with no structure', 'No characters at all', 'Only dialogue and no narration'], 0)]),
M('Measurement: Converting Between Imperial and Metric Units',
  'Grade 6 Math strand: students convert between imperial units (like inches, feet, and pounds) and metric units (like centimetres, metres, and kilograms) using approximate conversion factors.',
  [('Which of these is an imperial unit of length?', ['Inches', 'Centimetres', 'Metres', 'Kilometres'], 0),
   ('Which of these is a metric unit of length?', ['Centimetres', 'Inches', 'Feet', 'Miles'], 0),
   ('About how many centimetres are in one inch?', ['2.5', '1', '10', '100'], 0),
   ('Which unit system is used in most scientific work worldwide?', ['The metric system', 'The imperial system', 'Neither system', 'Both equally'], 0),
   ('Why is it useful to know how to convert between imperial and metric units?', ['Different countries and contexts use different systems', 'Conversions are never needed', 'All countries use identical units', 'Units never need to be compared'], 0)]),
Sc('Owls — Adaptations for Nighttime Hunting',
   'Grade 6 Science strand: owls are birds adapted for nighttime hunting, with excellent low-light vision, sensitive hearing, and silent flight feathers that help them catch prey.',
   [('When are owls typically active?', ['At night', 'Only at noon', 'Only underwater', 'Never'], 0),
    ('What adaptation helps owls fly without being heard by prey?', ['Silent flight feathers', 'Bright colours', 'Loud wingbeats', 'Long tails'], 0),
    ('Why is excellent hearing important for an owl?', ['It helps locate prey in the dark', 'It helps the owl swim', 'It helps the owl change colour', 'It has no purpose'], 0),
    ('What word describes an animal that is mainly active at night?', ['Nocturnal', 'Diurnal', 'Aquatic', 'Migratory'], 0),
    ('Owls adaptations are examples of features that help them ___.', ['Survive by hunting effectively', 'Avoid eating altogether', 'Live only underwater', 'Lose their ability to fly'], 0)]),
SS('Social Studies: Terry Fox — A Canadian Hero and His Marathon of Hope',
   'Grade 6 Social Studies strand: Terry Fox was a young Canadian who ran partway across Canada to raise money for cancer research, inspiring an annual tradition that continues today.',
   [('What did Terry Fox do to raise money for cancer research?', ['He ran across much of Canada', 'He wrote a book', 'He built a hospital himself', 'He painted a mural'], 0),
    ('What is the name of Terry Foxs journey called?', ['The Marathon of Hope', 'The Race for Life', 'The Cross-Canada Walk', 'The Great Run'], 0),
    ('What continues today in honour of Terry Fox?', ['An annual run raising money for cancer research', 'A national holiday with no purpose', 'A yearly parade with no cause', 'Nothing continues'], 0),
    ('Why is Terry Fox considered a Canadian hero?', ['He showed great courage and inspired others to help a cause', 'He was a famous actor', 'He was a hockey champion', 'He was a prime minister'], 0),
    ('The Terry Fox Run happening in schools across Canada shows ___.', ['Canadians coming together to support a cause', 'A random unrelated tradition', 'A rule with no meaning', 'A one-time-only event'], 0)]),
]),
day(115, [
L('Writing: Writing a Podcast Script',
  'Grade 6 Language strand: a podcast script organizes spoken content into segments, often including an introduction, main discussion points, and a conclusion, written to sound natural when read aloud.',
  [('What is a podcast script used for?', ['Organizing spoken content for an audio recording', 'Only for silent reading', 'For a printed newspaper', 'For a math worksheet'], 0),
   ('What should a podcast script sound like when read aloud?', ['Natural and conversational', 'Extremely formal legal language', 'A random list of words', 'Completely silent'], 0),
   ('What are common parts of a podcast script?', ['An introduction, main content, and a conclusion', 'Only a title', 'Only a single word', 'No structure at all'], 0),
   ('Why might a podcast script include notes about tone or pacing?', ['To help the speaker deliver the content effectively', 'Tone never matters in audio', 'Scripts should never include notes', 'Pacing has no effect on listeners'], 0),
   ('Which is an example of good podcast script planning?', ['Outlining segments before writing the full script', 'Recording with no planning at all', 'Skipping the introduction entirely', 'Avoiding any structure'], 0)]),
M('Data Management: Identifying Outliers in a Data Set',
  'Grade 6 Math strand: an outlier is a data value that is much higher or lower than the rest of the data, and identifying outliers can reveal errors or unusual results worth investigating.',
  [('What is an outlier?', ['A data value much higher or lower than the rest', 'The most common value', 'The middle value', 'The total of all values'], 0),
   ('In the data set 12, 14, 13, 15, 62, which value is the outlier?', ['62', '12', '13', '14'], 0),
   ('How can an outlier affect the mean of a data set?', ['It can pull the mean higher or lower than expected', 'It has no effect on the mean', 'It always makes the mean exactly zero', 'It removes all other data'], 0),
   ('Why is it important to notice outliers in data?', ['They may indicate an error or something unusual worth investigating', 'Outliers should always be ignored completely', 'Outliers are never meaningful', 'They automatically fix the data'], 0),
   ('Which measure of central tendency is often less affected by outliers than the mean?', ['The median', 'The mean', 'The range', 'The sum'], 0)]),
Sc('Bats and Echolocation',
   'Grade 6 Science strand: bats are the only flying mammals, and many species use echolocation, bouncing sound waves off objects, to navigate and find food in the dark.',
   [('What makes bats unique among mammals?', ['They are the only mammals that truly fly', 'They live underwater', 'They have no fur', 'They lay eggs'], 0),
    ('What is echolocation?', ['Using sound waves to locate objects', 'Using light to see', 'Using smell to hunt', 'Using taste to navigate'], 0),
    ('When are most bats active?', ['At night', 'At noon', 'Only in winter', 'Only underwater'], 0),
    ('How do bats use echolocation to find food?', ['They listen for sound bouncing back off insects', 'They smell insects from far away', 'They see insects glow in the dark', 'They taste the air'], 0),
    ('Bats are classified as ___.', ['Mammals', 'Birds', 'Insects', 'Reptiles'], 0)]),
SS('Social Studies: The Franklin Expedition — Arctic Exploration History',
   'Grade 6 Social Studies strand: the Franklin Expedition was a 19th-century voyage that attempted to navigate the Arctic and became a famous mystery when the ships were lost.',
   [('What was the Franklin Expedition trying to do?', ['Navigate a route through the Arctic', 'Explore the desert', 'Sail across the Pacific', 'Climb a mountain range'], 0),
    ('What happened to the Franklin Expeditions ships?', ['They became lost, creating a historical mystery', 'They arrived successfully with no issues', 'They never left port', 'They were never real ships'], 0),
    ('When did the Franklin Expedition take place?', ['In the 1800s', 'Last year', 'In ancient times', 'It has not happened yet'], 0),
    ('Why do historians and scientists remain interested in the Franklin Expedition?', ['It reveals details about Arctic exploration and history', 'It has no historical significance', 'It is a modern event', 'No evidence of it has ever been found'], 0),
    ('The Franklin Expedition is an example of ___.', ['Historical Arctic exploration', 'A modern space mission', 'A type of Canadian currency', 'A sport played in Canada'], 0)]),
]),
day(116, [
L('Writing: Writing a Straight News Article (The Inverted Pyramid)',
  'Grade 6 Language strand: a straight news article uses the inverted pyramid structure, presenting the most important information first, followed by supporting details in decreasing order of importance.',
  [('What structure do straight news articles typically follow?', ['The inverted pyramid', 'A strict rhyme scheme', 'A five-paragraph essay only', 'A random order'], 0),
   ('In the inverted pyramid structure, what comes first?', ['The most important information', 'The least important detail', 'A poem', 'The authors opinion only'], 0),
   ('Why do news articles present the most important information first?', ['So readers get key facts even if they stop reading early', 'To confuse the reader on purpose', 'Order does not matter in news writing', 'To hide the main point until the end'], 0),
   ('What questions does a news lead often answer?', ['Who, what, when, where, why, and how', 'Only who', 'Only when', 'None of these'], 0),
   ('Straight news writing differs from opinion writing because it ___.', ['Focuses on objective facts rather than personal opinions', 'Only shares personal opinions', 'Has no factual content', 'Is always written as a poem'], 0)]),
M('Number Sense: Rational vs Irrational Numbers',
  'Grade 6 Math strand: a rational number can be written as a fraction of two integers, while an irrational number, like pi, cannot be written as a simple fraction and has a non-repeating, non-ending decimal.',
  [('What is a rational number?', ['A number that can be written as a fraction of two integers', 'A number that never ends', 'Only a negative number', 'A number with no value'], 0),
   ('What is an irrational number?', ['A number that cannot be written as a simple fraction', 'Any number greater than zero', 'A number with only one digit', 'A number that is always negative'], 0),
   ('Which of these is a well-known irrational number?', ['Pi (3.14159...)', '1/2', '0.5', '4'], 0),
   ('Is the number 3/4 rational or irrational?', ['Rational', 'Irrational', 'Neither', 'Both'], 0),
   ('An irrational numbers decimal representation is ___.', ['Non-repeating and non-ending', 'Always a whole number', 'Always exactly two digits', 'Always zero'], 0)]),
Sc('Groundwater and Aquifers',
   'Grade 6 Science strand: groundwater is water that soaks into the ground and collects in layers of rock and soil called aquifers, an important source of fresh water for many communities.',
   [('What is groundwater?', ['Water that soaks into the ground and collects underground', 'Water in the ocean only', 'Water in the clouds', 'Water in a swimming pool'], 0),
    ('What is an aquifer?', ['An underground layer of rock or soil that holds water', 'A type of cloud', 'A kind of river', 'A weather instrument'], 0),
    ('Why is groundwater important?', ['It is a major source of fresh water for many communities', 'It has no importance', 'It only exists in oceans', 'It cannot be used by people'], 0),
    ('How does water typically get into an aquifer?', ['It soaks down through soil and rock', 'It falls directly from space', 'It is pumped in by machines only', 'It never enters an aquifer'], 0),
    ('Protecting groundwater from pollution is important because ___.', ['Many communities rely on it for drinking water', 'Groundwater is never used by people', 'Pollution never affects groundwater', 'Aquifers cannot be polluted'], 0)]),
SS('Social Studies: The History of Canadian Currency',
   'Grade 6 Social Studies strand: Canadian currency has evolved over centuries, from early trade using furs and wampum to todays coins and bills issued by the Bank of Canada.',
   [('What organization issues Canadas paper currency today?', ['The Bank of Canada', 'A private company', 'A foreign government', 'No organization'], 0),
    ('Before modern currency, what did early trade in Canada sometimes rely on?', ['Bartering goods like furs', 'Only credit cards', 'Only digital payments', 'Nothing was ever traded'], 0),
    ('Why does currency need to be trusted and standardized?', ['So people can reliably use it to trade goods and services', 'Trust does not matter for currency', 'Standardization has no purpose', 'Currency should change value randomly'], 0),
    ('How has Canadian currency changed over time?', ['It evolved from trade goods to standardized coins and bills', 'It has never changed at all', 'It was always identical to todays currency', 'It has only existed for one year'], 0),
    ('Studying the history of currency helps us understand ___.', ['How economies and trade have developed over time', 'Nothing about history', 'Only modern technology', 'Only foreign countries'], 0)]),
]),
day(117, [
L('Reading: Using Graphic Organizers to Plan Writing',
  'Grade 6 Language strand: graphic organizers, like webs, charts, and outlines, help writers visually plan and organize their ideas before drafting a piece of writing.',
  [('What is a graphic organizer?', ['A visual tool to plan and organize ideas', 'A type of punctuation', 'A grammar rule', 'A math formula'], 0),
   ('Why might a writer use a graphic organizer before drafting?', ['To visually plan and organize ideas first', 'To skip planning entirely', 'To confuse their own thinking', 'To avoid writing altogether'], 0),
   ('Which is an example of a graphic organizer?', ['A web diagram connecting related ideas', 'A dictionary definition', 'A single unrelated word', 'A blank page with no structure'], 0),
   ('Graphic organizers can help writers see ___.', ['Connections and structure between ideas', 'Nothing useful at all', 'Only spelling errors', 'Only punctuation mistakes'], 0),
   ('Using a graphic organizer before writing an essay can help with ___.', ['Organizing paragraphs logically', 'Avoiding all planning', 'Removing the need for a topic', 'Making writing less organized'], 0)]),
M('Financial Literacy: How Credit Cards and Interest Work',
  'Grade 6 Math strand: a credit card allows a person to borrow money to make purchases, but if the balance is not paid off, interest is charged on the amount owed.',
  [('What does a credit card allow a person to do?', ['Borrow money to make purchases', 'Only save money', 'Print their own currency', 'Avoid ever paying for anything'], 0),
   ('What happens if a credit card balance is not paid off in full?', ['Interest is charged on the amount owed', 'The balance automatically disappears', 'No consequences occur', 'The card stops working forever'], 0),
   ('Why is it important to understand how credit card interest works?', ['Unpaid balances can grow due to accumulating interest', 'Interest never affects what you owe', 'Credit cards have no fees ever', 'Interest always reduces what you owe'], 0),
   ('Which is a responsible way to use a credit card?', ['Paying off the balance in full each month when possible', 'Ignoring the balance completely', 'Never checking your spending', 'Spending far more than you can repay'], 0),
   ('A credit card is different from a debit card because it involves ___.', ['Borrowing money rather than spending your own funds directly', 'No money at all', 'Only cash transactions', 'Government-issued currency printing'], 0)]),
Sc('Sleep — Why Our Bodies and Brains Need Rest',
   'Grade 6 Science strand: sleep allows the brain and body to rest, repair, and consolidate memories, and getting enough quality sleep is essential for health and learning.',
   [('What does sleep allow the body and brain to do?', ['Rest, repair, and consolidate memories', 'Work harder than while awake', 'Stop growing permanently', 'Lose all memories'], 0),
    ('Why is sleep important for learning?', ['It helps consolidate and strengthen memories', 'Sleep has no effect on memory', 'Sleep erases all learning', 'Learning only happens while asleep'], 0),
    ('What might happen if a person consistently does not get enough sleep?', ['Difficulty concentrating and other health effects', 'No effects at all', 'Improved memory with no downsides', 'Instant improved health'], 0),
    ('Which organ is especially active in restoring itself during sleep?', ['The brain', 'The stomach only', 'The skin only', 'No organ is affected'], 0),
    ('Good sleep habits are considered part of ___.', ['Overall health and well-being', 'An unimportant daily activity', 'Something with no scientific basis', 'Something unrelated to the body'], 0)]),
SS('Social Studies: The Auditor General — Watching How Government Spends Money',
   'Grade 6 Social Studies strand: the Auditor General is an independent officer who reviews how the federal government spends public money, reporting on waste, mismanagement, or inefficiency.',
   [('What is the Auditor Generals main job?', ['Reviewing how the government spends public money', 'Teaching in schools', 'Running a business', 'Managing a hospital'], 0),
    ('Why is it important for the Auditor General to be independent?', ['So the review is unbiased and not controlled by the government being reviewed', 'Independence does not matter', 'The government should review itself only', 'Independence makes the reports less accurate'], 0),
    ('What might the Auditor Generals reports reveal?', ['Waste, mismanagement, or inefficiency in spending', 'Only good news', 'Nothing useful', 'Sports statistics'], 0),
    ('Who does the Auditor General typically report to?', ['Parliament', 'A single citizen', 'A private company', 'No one'], 0),
    ('Why might citizens care about the Auditor Generals reports?', ['They show how tax dollars are being used', 'Citizens have no interest in government spending', 'The reports are always secret', 'Reports never affect citizens'], 0)]),
]),
day(118, [
L('Grammar: Texting Language vs Formal Writing',
  'Grade 6 Language strand: texting language uses informal abbreviations and shortcuts appropriate for casual messages, but formal writing requires complete sentences and standard grammar.',
  [('What is texting language often characterized by?', ['Informal abbreviations and shortcuts', 'Strict formal grammar rules', 'Long, complex sentences only', 'No communication at all'], 0),
   ('Why is texting language usually inappropriate for a school essay?', ['Formal writing requires complete sentences and standard grammar', 'Texting language is always required in essays', 'Formal writing has no rules', 'Abbreviations are always formal'], 0),
   ('Which is an example of texting language?', ['BRB for be right back', 'A complete formal sentence', 'A properly cited research paper', 'A grammatically formal paragraph'], 0),
   ('Why is it useful to know when to use formal versus informal language?', ['Different situations call for different levels of formality', 'Formality never matters in writing', 'Only formal language should ever be used', 'Only informal language should ever be used'], 0),
   ('Which situation calls for formal writing?', ['A school research report', 'A quick text to a friend', 'A casual chat message', 'An informal social media comment'], 0)]),
M('Proportional Reasoning: Solving Proportions with Cross-Multiplication',
  'Grade 6 Math strand: cross-multiplication is a method for solving proportions by multiplying diagonally across the equals sign, useful for finding an unknown value in equivalent ratios.',
  [('What is cross-multiplication used for?', ['Solving proportions to find an unknown value', 'Adding fractions', 'Rounding decimals', 'Measuring angles'], 0),
   ('In the proportion 2/3 = x/12, what is the value of x after cross-multiplying?', ['8', '6', '9', '18'], 0),
   ('How does cross-multiplication work?', ['Multiply diagonally across the equals sign', 'Add the numerators together', 'Subtract the denominators', 'Divide both sides by zero'], 0),
   ('In the proportion 4/5 = 8/x, what is the value of x?', ['10', '9', '12', '20'], 0),
   ('Why is cross-multiplication a useful strategy?', ['It provides a reliable way to solve for unknowns in proportions', 'It never works for any proportion', 'It only works with whole numbers', 'It removes the need for ratios'], 0)]),
Sc('How a Battery Stores and Releases Energy',
   'Grade 6 Science strand: a battery stores chemical energy and converts it into electrical energy through a chemical reaction, releasing electricity to power devices.',
   [('What kind of energy does a battery store?', ['Chemical energy', 'Sound energy', 'Light energy only', 'No energy at all'], 0),
    ('How does a battery produce electricity?', ['Through a chemical reaction that converts stored energy into electrical energy', 'By capturing sunlight directly', 'By burning fuel inside it', 'By freezing water'], 0),
    ('What happens to a battery when it runs out of stored energy?', ['It can no longer power a device until recharged or replaced', 'It becomes more powerful', 'It generates unlimited energy forever', 'Nothing changes at all'], 0),
    ('Which of these commonly uses battery power?', ['A remote control', 'A wood-burning fireplace', 'A hand-crank pencil sharpener', 'A sundial'], 0),
    ('Why are batteries useful in portable devices?', ['They provide energy without needing a constant plug connection', 'They require constant plugging into a wall outlet', 'They only work when connected to solar panels', 'They cannot store any energy'], 0)]),
SS('Social Studies: The Magna Cartas Influence on Canadian Law',
   'Grade 6 Social Studies strand: the Magna Carta, signed in England in 1215, established early principles like the rule of law that influenced legal systems, including Canadas, centuries later.',
   [('What was the Magna Carta?', ['An early document establishing principles like the rule of law', 'A modern Canadian law', 'A type of currency', 'A national holiday'], 0),
    ('Roughly when was the Magna Carta signed?', ['In the 1200s', 'Last year', 'In the 1900s', 'It has not happened yet'], 0),
    ('What important principle did the Magna Carta help establish?', ['The rule of law, meaning even rulers must follow the law', 'That only kings make all decisions with no limits', 'That laws do not apply to anyone', 'That courts should not exist'], 0),
    ('How did the Magna Carta influence legal systems like Canadas?', ['Its principles shaped ideas about law and rights over centuries', 'It has no connection to modern law', 'Canada copied it word for word', 'It was immediately forgotten'], 0),
    ('Why do historians and legal scholars still study the Magna Carta today?', ['It laid early groundwork for modern legal principles', 'It has no historical significance', 'It was written very recently', 'It only applied for one day'], 0)]),
]),
day(119, [
L('Writing: Writing a Short Screenplay Scene',
  'Grade 6 Language strand: a screenplay uses a specific format with scene headings, action lines, and character dialogue, written to guide actors and filmmakers in bringing a story to life visually.',
  [('What does a screenplay use to describe where and when a scene happens?', ['A scene heading', 'A footnote', 'A glossary', 'A bibliography'], 0),
   ('What are action lines in a screenplay used for?', ['Describing what happens visually in a scene', 'Only listing character names', 'Only showing music notes', 'Replacing all dialogue'], 0),
   ('How is dialogue typically formatted in a screenplay?', ['Under the speaking characters name', 'Without any character names at all', 'In footnotes only', 'In a completely different language each time'], 0),
   ('Who uses a screenplay to help bring a story to life?', ['Actors and filmmakers', 'Only readers of novels', 'Only musicians', 'Only painters'], 0),
   ('Why does screenplay formatting matter?', ['It helps everyone involved in a production understand the story clearly', 'Formatting has no purpose in screenwriting', 'Screenplays are never formatted', 'Only novels need formatting'], 0)]),
M('Geometry: Surface Area of a Sphere',
  'Grade 6 Math strand: the surface area of a sphere is found using the formula 4 times pi times the radius squared, describing the total area covering the outside of the sphere.',
  [('What shape is a basketball an example of?', ['A sphere', 'A cube', 'A cylinder', 'A cone'], 0),
   ('What measurement is needed to find the surface area of a sphere?', ['The radius', 'Only the diameter squared with no radius', 'The volume only', 'The circumference alone'], 0),
   ('The formula for surface area of a sphere involves which constant?', ['Pi', 'Zero', 'One', 'Ten'], 0),
   ('If a spheres radius doubles, what generally happens to its surface area?', ['It increases significantly (by a factor of four)', 'It stays exactly the same', 'It decreases', 'It becomes zero'], 0),
   ('Surface area of a sphere is measured in ___.', ['Square units', 'Cubic units', 'Linear units only', 'No units at all'], 0)]),
Sc('The Human Brain — Structure and Function',
   'Grade 6 Science strand: the brain is the control centre of the nervous system, responsible for thinking, memory, movement, and interpreting information from the senses.',
   [('What is the brain often described as?', ['The control centre of the nervous system', 'A digestive organ', 'A type of muscle only', 'A blood vessel'], 0),
    ('What are some functions of the brain?', ['Thinking, memory, and movement control', 'Only digesting food', 'Only pumping blood', 'Only filtering air'], 0),
    ('How does the brain use information from the senses?', ['It interprets signals from the eyes, ears, and other senses', 'It ignores all sensory information', 'It only processes taste', 'It has no connection to the senses'], 0),
    ('Why is protecting the brain, such as with a helmet, important?', ['The brain is a vital and delicate organ', 'The brain cannot be injured', 'Protection is unnecessary', 'The brain regenerates instantly if injured'], 0),
    ('The brain sends and receives messages through the ___.', ['Nervous system', 'Digestive system', 'Skeletal system alone', 'Circulatory system alone'], 0)]),
SS('Social Studies: The Klondike Gold Rush',
   'Grade 6 Social Studies strand: the Klondike Gold Rush of the late 1890s brought thousands of prospectors to the Yukon in search of gold, shaping the development of northern Canada.',
   [('What did prospectors search for during the Klondike Gold Rush?', ['Gold', 'Oil', 'Diamonds', 'Silver only'], 0),
    ('In which Canadian territory did the Klondike Gold Rush mainly take place?', ['The Yukon', 'Nunavut', 'British Columbia', 'Ontario'], 0),
    ('Roughly when did the Klondike Gold Rush occur?', ['In the late 1890s', 'Last year', 'In the 1700s', 'It has not happened yet'], 0),
    ('How did the Klondike Gold Rush affect northern Canada?', ['It brought rapid population growth and development to the region', 'It had no effect on the region', 'It caused the region to disappear', 'It only affected southern Canada'], 0),
    ('Why do people still study the Klondike Gold Rush today?', ['It reveals important details about Canadian history and settlement', 'It has no historical value', 'It is a purely modern event', 'No records of it exist'], 0)]),
]),
day(120, [
L('Language Review: Poetry, Story Forms, and Writing Formats',
  'Grade 6 Language strand review: students revisit writing a haiku, onomatopoeia and alliteration, epistolary writing, frame narratives, podcast scripts, and screenplay scenes.',
  [('How many lines does a haiku have?', ['Three', 'Two', 'Four', 'Five'], 0),
   ('What is onomatopoeia?', ['Words that imitate the sounds they describe', 'A type of punctuation', 'A grammar rule', 'A math term'], 0),
   ('What is epistolary writing?', ['A story told through letters or similar documents', 'A story with no characters', 'A type of poem only', 'A grammar rule'], 0),
   ('What is a frame narrative?', ['A story that contains another story inside it', 'A story with no beginning', 'A single-page poem', 'A grammar exercise'], 0),
   ('What does a screenplay use to describe where and when a scene happens?', ['A scene heading', 'A footnote', 'A glossary', 'A bibliography'], 0)]),
M('Math Review: Geometry, Number Sense, and Financial Literacy',
  'Grade 6 Math strand review: students revisit cone and pyramid volume, scatter plots, absolute value, imperial/metric conversion, outliers, sphere surface area, and credit card interest.',
  [('The volume of a cone is what fraction of a cylinder with the same base and height?', ['One-third', 'One-half', 'Two-thirds', 'The same as the cylinder'], 0),
   ('What does absolute value represent?', ['The distance a number is from zero', 'The number itself with no change', 'Only negative numbers', 'A type of fraction'], 0),
   ('What is an outlier?', ['A data value much higher or lower than the rest', 'The most common value', 'The middle value', 'The total of all values'], 0),
   ('What is an irrational number?', ['A number that cannot be written as a simple fraction', 'Any number greater than zero', 'A number with only one digit', 'A number that is always negative'], 0),
   ('What happens if a credit card balance is not paid off in full?', ['Interest is charged on the amount owed', 'The balance automatically disappears', 'No consequences occur', 'The card stops working forever'], 0)]),
Sc('Science Review: The Human Body and Everyday Science',
   'Grade 6 Science strand review: students revisit the human ear, antibiotics, nutrition, owls, bats and echolocation, groundwater, sleep, batteries, and the human brain.',
   [('What does the ear collect and convert into signals?', ['Sound vibrations', 'Light waves', 'Chemical signals', 'Heat energy'], 0),
    ('What do antibiotics fight?', ['Bacterial infections', 'Viral infections', 'Broken bones', 'Allergies only'], 0),
    ('What is echolocation?', ['Using sound waves to locate objects', 'Using light to see', 'Using smell to hunt', 'Using taste to navigate'], 0),
    ('What is an aquifer?', ['An underground layer of rock or soil that holds water', 'A type of cloud', 'A kind of river', 'A weather instrument'], 0),
    ('What is the brain often described as?', ['The control centre of the nervous system', 'A digestive organ', 'A type of muscle only', 'A blood vessel'], 0)]),
SS('Social Studies Review: Canadian History, Government, and Institutions',
   'Grade 6 Social Studies strand review: students revisit the RCMP, the census, sister cities, Terry Fox, the Franklin Expedition, Canadian currency history, the Auditor General, the Magna Carta, and the Klondike Gold Rush.',
   [('What does RCMP stand for?', ['Royal Canadian Mounted Police', 'Royal Canadian Medical Program', 'Regional Canadian Municipal Patrol', 'Real Canadian Mail Post'], 0),
    ('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('What organization issues Canadas paper currency today?', ['The Bank of Canada', 'A private company', 'A foreign government', 'No organization'], 0),
    ('What was the Magna Carta?', ['An early document establishing principles like the rule of law', 'A modern Canadian law', 'A type of currency', 'A national holiday'], 0),
    ('In which Canadian territory did the Klondike Gold Rush mainly take place?', ['The Yukon', 'Nunavut', 'British Columbia', 'Ontario'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_111_120)
    append_to(6, g6_111_120)
