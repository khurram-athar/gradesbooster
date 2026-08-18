#!/usr/bin/env python3
"""Grade 5, Days 171-180 -- extends Grade 5 from 170 to 180 days. Modeled
exactly on gen_grade5_days161_170.py (itself modeled on the preceding
batches all the way back to gen_grade5_days141_150.py): same L/M/Sc/SS
helpers over gen_curriculum's sub()/day()/append_to(), same TVO Learn
placeholder resourceLabel/resourceUrl convention (videoUrl intentionally
left unset, filled in later by the daily curriculum-video-backfill
scheduled task), and the same _rebalance_answer_positions() post-processing
step.

Every existing (subject, title) pair across Grade 5 Days 1-170 was dumped
from data/grade5.json (680 entries, all unique) and checked against every
topic below before it was chosen -- Grade 5 already densely covers nearly
the entire elementary curriculum across all four subjects, so each new
topic here was picked specifically to avoid overlapping with any prior
day. New topics: reflexive and indefinite pronouns, writing a haiku,
acronyms and abbreviations, understanding subplot in a story, infographics
and data visuals, writing an acrostic poem, using articles correctly (a,
an, the), oral storytelling traditions, and recognizing a red herring in a
mystery for Language; line symmetry and mirror images, understanding pay
stubs and wages, palindromic numbers, nets of pyramids, converting between
square units of area, diagonals of polygons, an introduction to stocks and
investing, perfect numbers, and evaluating algebraic expressions by
substitution for Math; tsunamis, desert ecosystems, an introduction to
nuclear energy, refraction and lenses, fermentation, invasive species,
composting, water treatment, and wildfires and forest renewal for Science;
and the Privy Council, the Supreme Court of Canada, Statistics Canada, the
Sixties Scoop, voter turnout and civic engagement, Canada's manufacturing
industry, VIA Rail, international development and foreign aid, and the
World Trade Organization for Social Studies -- none of those exact ideas
appear in Days 1-170. Day 180 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch (drawing
one representative quiz question per subject from each of the first five
days of the batch, Days 171-175, exactly as Day 170 drew from Days
161-165). The four Day 180 review titles were checked against every
earlier review-day title in Days 1-170 and are textually distinct from all
of them.

No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the rest of Grade 5 Days 1-170 (e.g. "Canadas" not "Canada's", "countrys"
not "country's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science and Technology',
    'TVO Learn: Grade 5 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L5, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M5, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S5, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS5, q)


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


g5_171_180 = [
day(171, [
L('Grammar: Reflexive and Indefinite Pronouns',
  'Grade 5 Language strand: a reflexive pronoun refers back to the subject of a sentence, such as himself or themselves, while an indefinite pronoun refers to an unspecified person or thing, such as everyone or nothing.',
  [('What does a reflexive pronoun do?', ['Refers back to the subject of a sentence', 'Names a location', 'Joins two independent clauses', 'Shows possession only'], 0),
   ('Which of these is a reflexive pronoun?', ['Herself', 'She', 'Her', 'Hers'], 0),
   ('What does an indefinite pronoun refer to?', ['An unspecified person or thing', 'A specific, named person only', 'A single fixed location', 'A verb tense'], 0),
   ('Which of these is an indefinite pronoun?', ['Everyone', 'He', 'It', 'They'], 0),
   ('Why might a writer use the reflexive pronoun herself in the sentence She hurt herself while running?', ['To show the action refers back to the same person performing it', 'Reflexive pronouns never refer back to the subject', 'This concept has no connection to grammar', 'A reflexive pronoun always names a different person entirely'], 0)]),
M('Geometry: Line Symmetry and Mirror Images',
  'Grade 5 Math strand: a shape has line symmetry when a line can divide it into two matching mirror-image halves, and that line is called a line of symmetry.',
  [('What is a line of symmetry?', ['A line that divides a shape into two matching mirror-image halves', 'A line that always passes through only one corner of a shape', 'A line that measures the perimeter of a shape', 'A line that shows how a shape was rotated'], 0),
   ('How many lines of symmetry does a square have?', ['4', '1', '2', '0'], 0),
   ('Which shape always has at least one line of symmetry?', ['A rectangle', 'A scalene triangle', 'An irregular pentagon with no equal sides', 'A shape with no matching sides at all'], 0),
   ('Why might folding a paper shape in half help someone check for a line of symmetry?', ['Folding shows whether both halves match exactly when placed on top of each other', 'Folding paper never shows anything about a shapes symmetry', 'This concept has no connection to geometry', 'A folded shape always looks completely different on each side'], 0),
   ('Why does a scalene triangle usually have no lines of symmetry?', ['Its three sides and three angles are all different lengths and measures', 'All of its sides and angles are always exactly equal', 'This concept has no relevance to geometry', 'Every triangle automatically has at least one line of symmetry'], 0)]),
Sc('Tsunamis: Causes and Warning Systems',
   'Grade 5 Science strand: a tsunami is a series of powerful ocean waves usually triggered by an underwater earthquake, volcanic eruption, or landslide, and warning systems help coastal communities evacuate before the waves arrive.',
   [('What most commonly triggers a tsunami?', ['An underwater earthquake', 'A gentle ocean breeze', 'A change in the tide alone', 'A cloud passing over the ocean'], 0),
    ('What is the purpose of a tsunami warning system?', ['To alert coastal communities so they can evacuate before waves arrive', 'To prevent earthquakes from ever happening', 'To measure the temperature of the ocean', 'This concept has no connection to natural disasters'], 0),
    ('Besides an earthquake, what else might trigger a tsunami?', ['A volcanic eruption or underwater landslide', 'A light rain shower', 'A change in wind direction alone', 'This concept has no relevance to tsunamis'], 0),
    ('Why do tsunami waves often grow taller as they approach shallow coastal water?', ['The waves slow down and the water is pushed upward as the ocean floor rises', 'The waves always become smaller near the shore', 'This concept has no connection to science', 'Shallow water has no effect on wave height at all'], 0),
    ('Why is an early warning system important for coastal communities?', ['It gives people more time to move to higher ground before the waves arrive', 'Warning systems have no effect on how people respond to tsunamis', 'This concept has no relevance to science', 'Tsunamis always arrive with no possible warning at all'], 0)]),
SS('The Privy Council and Its Role in Canadian Government',
   'Grade 5 Social Studies strand: the Privy Council is a formal body that advises the Governor General, though in practice most of its authority is exercised by the Cabinet on behalf of the prime minister.',
   [('Who does the Privy Council formally advise?', ['The Governor General', 'The Supreme Court', 'A foreign government', 'A municipal council'], 0),
    ('In practice, who exercises most of the authority connected to the Privy Council?', ['The Cabinet, on behalf of the prime minister', 'The Speaker of the House of Commons alone', 'A single unelected official', 'This concept has no connection to Canadian government'], 0),
    ('What government office supports the daily work connected to the Privy Council?', ['The Privy Council Office', 'The Bank of Canada', 'The Supreme Court Registry', 'This concept has no relevance to Canadian government'], 0),
    ('Why might Canada keep a formal body like the Privy Council even though the Cabinet carries out most of its work?', ['It preserves a long-standing constitutional structure for advising the Crown', 'The Privy Council has no purpose in Canadian government at all', 'This concept has no connection to social studies', 'The Privy Council replaced the Cabinet entirely long ago'], 0),
    ('Why is understanding the Privy Council useful when learning about Canadian government?', ['It shows how formal and practical roles in government can differ from each other', 'The Privy Council has no connection to how Canada is governed', 'This concept has no relevance to social studies', 'Every part of Canadian government works in exactly the same way'], 0)]),
]),
day(172, [
L('Poetry: Writing a Haiku',
  'Grade 5 Language strand: a haiku is a short, unrhymed poem with three lines that traditionally follow a five, seven, five syllable pattern and often focuses on nature or a single vivid moment.',
  [('How many lines does a traditional haiku have?', ['3', '5', '4', '2'], 0),
   ('What syllable pattern does a traditional haiku follow?', ['Five, seven, five', 'Four, four, four', 'Six, six, six', 'Two, four, two'], 0),
   ('What subject does a haiku traditionally focus on?', ['Nature or a single vivid moment', 'A long, complicated adventure story', 'A detailed historical timeline', 'A persuasive argument'], 0),
   ('Why might counting syllables carefully matter when writing a haiku?', ['The traditional five, seven, five pattern gives the poem its structure', 'Syllable count never matters when writing a haiku', 'This concept has no connection to poetry', 'A haiku can have any number of lines and syllables'], 0),
   ('Why might a poet choose the haiku form to describe a falling leaf?', ['Its short, focused structure can capture a single vivid image or moment', 'A haiku is always too long to describe a single moment', 'This concept has no relevance to poetry', 'Haiku poems are never used to describe nature'], 0)]),
M('Financial Literacy: Understanding Pay Stubs and Wages',
  'Grade 5 Math strand: a pay stub shows how much money a worker earned, along with any amounts subtracted for taxes or other deductions, resulting in the net pay actually received.',
  [('What does a pay stub show?', ['How much money a worker earned and what was deducted', 'A list of items purchased at a store', 'A record of a persons daily schedule', 'A summary of a persons grades in school'], 0),
   ('What is net pay?', ['The amount of money actually received after deductions', 'The total amount earned before any deductions', 'The amount of tax owed only', 'A fee charged for using a bank account'], 0),
   ('If a worker earns 500 dollars and has 100 dollars deducted for taxes, what is the net pay?', ['400 dollars', '500 dollars', '600 dollars', '100 dollars'], 0),
   ('Why might understanding a pay stub be an important financial literacy skill?', ['It helps a person understand exactly how their earnings and deductions are calculated', 'Pay stubs never provide any useful financial information', 'This concept has no connection to financial literacy', 'Deductions never appear on a real pay stub'], 0),
   ('If a worker earns 20 dollars per hour and works 10 hours, what is the total pay before deductions?', ['200 dollars', '180 dollars', '220 dollars', '20 dollars'], 0)]),
Sc('Desert Ecosystems and Adaptations for Extreme Heat',
   'Grade 5 Science strand: a desert ecosystem receives very little rainfall, and the plants and animals that live there have special adaptations, such as water storage or nocturnal behaviour, that help them survive extreme heat and dryness.',
   [('What is a defining feature of a desert ecosystem?', ['Very little rainfall', 'Constant heavy rainfall', 'Extremely cold temperatures year-round', 'This concept has no connection to ecosystems'], 0),
    ('How do many desert plants, such as cacti, adapt to store water?', ['They store water in thick stems or leaves', 'They rely entirely on rainfall every single day', 'They never need water to survive', 'This concept has no relevance to desert ecosystems'], 0),
    ('Why do many desert animals become active mainly at night, a behaviour called being nocturnal?', ['It helps them avoid the extreme heat of the daytime sun', 'Nighttime activity has no connection to surviving in a desert', 'Desert animals are always active only during the hottest part of the day', 'This concept has no relevance to science'], 0),
    ('Why might a desert animal have large ears, such as a fennec fox?', ['Large ears can help release body heat and keep the animal cool', 'Large ears have no connection to surviving in a hot climate', 'This concept has no relevance to desert adaptations', 'Large ears always make an animal colder in every environment'], 0),
    ('Why are adaptations especially important for organisms living in a desert ecosystem?', ['They help organisms survive extreme heat and very limited water', 'Adaptations have no effect on survival in a desert', 'This concept has no relevance to science', 'Desert organisms never need any special adaptations to survive'], 0)]),
SS('The Supreme Court of Canada and Its Role',
   'Grade 5 Social Studies strand: the Supreme Court of Canada is the highest court in the country, making final decisions on legal disputes and interpreting how the Constitution and the Charter of Rights and Freedoms apply.',
   [('What is the Supreme Court of Canada?', ['The highest court in the country', 'A court that only handles municipal bylaws', 'A committee that writes new federal laws', 'A court found only in one province'], 0),
    ('What is one role of the Supreme Court of Canada?', ['Interpreting how the Constitution and the Charter of Rights and Freedoms apply', 'Collecting federal taxes', 'Running national elections', 'Managing the Canadian Armed Forces'], 0),
    ('Whose decisions can be appealed all the way up to the Supreme Court of Canada?', ['Decisions made by lower courts across the country', 'Decisions made only by municipal councils', 'Decisions made only by foreign governments', 'This concept has no connection to social studies'], 0),
    ('Why might having a single highest court be important for the country?', ['It provides a final, consistent interpretation of the law for all of Canada', 'A highest court has no effect on how laws are applied', 'This concept has no relevance to Canadian government', 'Every province could otherwise interpret national laws in a completely different way with no resolution'], 0),
    ('Why might the Supreme Court of Canada be considered especially important when a case involves the Charter of Rights and Freedoms?', ['Its rulings can determine how rights and freedoms are protected across the country', 'The Supreme Court has no connection to the Charter of Rights and Freedoms', 'This concept has no relevance to social studies', 'Charter cases are never reviewed by the Supreme Court'], 0)]),
]),
day(173, [
L('Vocabulary: Acronyms and Abbreviations',
  'Grade 5 Language strand: an acronym is a word formed from the first letters of a phrase and pronounced as a word, such as scuba, while an abbreviation is a shortened form of a word or phrase, such as Dr for doctor.',
  [('What is an acronym?', ['A word formed from the first letters of a phrase, pronounced as a word', 'A word that rhymes with another word', 'A word with an opposite meaning to another word', 'A word borrowed directly from another language'], 0),
   ('What is an abbreviation?', ['A shortened form of a word or phrase', 'A word with more than one meaning', 'A word that sounds like the sound it describes', 'A comparison between two unlike things'], 0),
   ('Which of these is an example of an acronym?', ['Scuba', 'Dr', 'St', 'Mr'], 0),
   ('Why might scuba be considered an acronym rather than just an abbreviation?', ['It is formed from initial letters and pronounced as a single word', 'It is never formed from the first letters of a phrase', 'This concept has no connection to vocabulary', 'Acronyms are always written with periods between every letter'], 0),
   ('Why might writers use abbreviations like Dr or St in everyday writing?', ['They save space and time while still being clearly understood', 'Abbreviations always make writing more difficult to understand', 'This concept has no relevance to vocabulary', 'Abbreviations are never used in real writing'], 0)]),
M('Number Sense: Palindromic Numbers',
  'Grade 5 Math strand: a palindromic number reads the same forward and backward, such as 121 or 3553, and exploring these numbers helps build number sense and pattern recognition.',
  [('What is a palindromic number?', ['A number that reads the same forward and backward', 'A number that is always divisible by 10', 'A number with only one digit', 'A number that can never be added to another number'], 0),
   ('Which of these is a palindromic number?', ['1221', '1234', '1023', '2001'], 0),
   ('Is the number 505 a palindromic number?', ['Yes, it reads the same forward and backward', 'No, it reads differently forward and backward', 'It cannot be determined without a calculator', 'This concept has no relevance to numbers'], 0),
   ('Why might exploring palindromic numbers help build number sense?', ['It encourages noticing patterns and structure within numbers', 'Palindromic numbers have no connection to number sense', 'This concept has no relevance to math', 'Palindromic numbers only exist in decimals, never whole numbers'], 0),
   ('What is the next palindromic number after 131?', ['141', '132', '140', '135'], 0)]),
Sc('Nuclear Energy: An Introduction',
   'Grade 5 Science strand: nuclear energy is produced by splitting atoms in a process called fission, releasing a large amount of heat that can be used to generate electricity without burning fossil fuels.',
   [('How is nuclear energy typically produced?', ['By splitting atoms in a process called fission', 'By burning coal in a large furnace', 'By capturing energy directly from sunlight', 'By spinning turbines using only wind'], 0),
    ('What does nuclear energy release that can be used to generate electricity?', ['A large amount of heat', 'A large amount of sunlight', 'A large amount of rainfall', 'This concept has no connection to energy'], 0),
    ('Why is nuclear energy sometimes described as a low-emission energy source?', ['It generates electricity without burning fossil fuels', 'It always requires burning large amounts of coal', 'This concept has no connection to nuclear energy', 'Nuclear energy always produces more smoke than any other energy source'], 0),
    ('Why might handling nuclear waste carefully be an important part of using nuclear energy?', ['Nuclear waste can remain radioactive and potentially harmful for a long time', 'Nuclear waste is never a concern connected to nuclear energy', 'This concept has no relevance to science', 'Nuclear waste disappears completely as soon as it is produced'], 0),
    ('Why might a country choose to include nuclear energy as part of its energy supply?', ['It can generate large amounts of electricity while producing very few emissions', 'Nuclear energy has no connection to generating electricity', 'This concept has no relevance to science', 'Nuclear energy is always the least efficient way to generate power'], 0)]),
SS('Statistics Canada and the Importance of Reliable Data',
   'Grade 5 Social Studies strand: Statistics Canada is the federal agency responsible for collecting and publishing data about the countrys population, economy, and society, helping governments and citizens make informed decisions.',
   [('What is Statistics Canada responsible for?', ['Collecting and publishing data about the countrys population, economy, and society', 'Enforcing municipal bylaws', 'Running the Canadian Armed Forces', 'Printing Canadian currency'], 0),
    ('Who might use the data collected by Statistics Canada?', ['Governments and citizens making informed decisions', 'Only foreign governments', 'Only large international corporations', 'This concept has no connection to social studies'], 0),
    ('Which large national survey does Statistics Canada conduct every five years?', ['The Census', 'A national spelling competition', 'A national art contest', 'This concept has no relevance to Statistics Canada'], 0),
    ('Why is reliable data important for governments planning public services?', ['Accurate information helps governments plan services that match peoples actual needs', 'Reliable data has no effect on how governments plan services', 'This concept has no relevance to social studies', 'Governments never use data when planning public services'], 0),
    ('Why might Statistics Canada be considered an important part of a well-informed democracy?', ['It provides trustworthy information that helps citizens and leaders make informed choices', 'Statistics Canada has no connection to how decisions are made in Canada', 'This concept has no relevance to social studies', 'Reliable data is never useful in a democratic society'], 0)]),
]),
day(174, [
L('Reading: Understanding Subplot in a Story',
  'Grade 5 Language strand: a subplot is a secondary storyline that runs alongside the main plot of a story, often involving a supporting character and adding depth to the overall narrative.',
  [('What is a subplot?', ['A secondary storyline that runs alongside the main plot', 'The very first event in a story', 'A summary of the entire story', 'The setting where a story takes place'], 0),
   ('Who is a subplot often centred around?', ['A supporting character', 'Only the main character', 'No characters at all', 'This concept has no connection to reading'], 0),
   ('What can a subplot add to a story?', ['Additional depth to the overall narrative', 'Nothing of any value to the story', 'Confusion with no clear purpose', 'This concept has no relevance to reading'], 0),
   ('Why might an author connect a subplot to the main plot by the end of a story?', ['Connecting the storylines can create a more satisfying and unified narrative', 'Subplots are never meant to connect to the main plot', 'This concept has no connection to reading', 'A subplot always replaces the main plot entirely'], 0),
   ('Why might identifying a subplot help a reader better understand a story?', ['It shows how secondary events and characters support the larger story', 'Subplots never provide any useful information about a story', 'This concept has no relevance to reading', 'A story can never contain more than one storyline'], 0)]),
M('Geometry: Nets of Pyramids',
  'Grade 5 Math strand: a net is a two-dimensional pattern that can be folded to form a three-dimensional shape, and the net of a pyramid includes a polygon base along with triangular faces that meet at a single point.',
  [('What is a net in geometry?', ['A two-dimensional pattern that can be folded into a three-dimensional shape', 'A tool used to measure angles', 'A type of graph used to display data', 'A line that divides a shape into equal halves'], 0),
   ('What shapes make up the net of a square-based pyramid?', ['One square base and four triangular faces', 'Six identical squares', 'Two triangular bases and three rectangles', 'One circle and one triangle'], 0),
   ('Where do the triangular faces of a pyramids net meet when folded?', ['At a single point, called the apex', 'They never meet at any point', 'Along the base only', 'This concept has no connection to geometry'], 0),
   ('Why might building a physical net of a pyramid help with understanding its shape?', ['Folding the net shows exactly how the flat faces come together to form the 3D shape', 'Building a net never helps with understanding a 3D shape', 'This concept has no relevance to geometry', 'A net always looks identical to the folded 3D shape'], 0),
   ('How many triangular faces does the net of a triangular-based pyramid have, not counting its base?', ['3', '4', '2', '6'], 0)]),
Sc('Refraction and How Lenses Bend Light',
   'Grade 5 Science strand: refraction is the bending of light as it passes from one material into another, such as from air into water or glass, and curved lenses use refraction to focus light and form clear images.',
   [('What is refraction?', ['The bending of light as it passes from one material into another', 'The bouncing of light off a mirror', 'The complete blocking of light by an object', 'This concept has no connection to light'], 0),
    ('When does light typically refract?', ['When it passes from one material into another, such as air into water', 'Only when it is completely dark', 'Only when it passes through a solid, opaque wall', 'This concept has no relevance to science'], 0),
    ('What do curved lenses use to help focus light and form an image?', ['Refraction', 'Reflection off a flat mirror', 'Absorption of all light', 'This concept has no connection to lenses'], 0),
    ('Why might a straw appear bent when placed in a glass of water?', ['Light refracts as it passes from the water into the air, changing how the straw appears', 'Light never changes direction when passing through water', 'This concept has no relevance to science', 'The straw actually becomes bent while inside the water'], 0),
    ('Why are curved lenses useful in tools like eyeglasses and magnifying glasses?', ['They can bend light in controlled ways to focus images clearly', 'Curved lenses have no effect on how light travels', 'This concept has no relevance to science', 'Lenses are never used to help people see more clearly'], 0)]),
SS('The Sixties Scoop and Its Impact on Indigenous Families',
   'Grade 5 Social Studies strand: the Sixties Scoop refers to a period when many Indigenous children in Canada were removed from their families and placed in non-Indigenous homes, disrupting their connection to their culture and communities.',
   [('What does the term Sixties Scoop refer to?', ['A period when many Indigenous children were removed from their families and placed in non-Indigenous homes', 'A national sports competition held in the 1960s', 'A program that built new highways across Canada', 'This concept has no connection to Canadian history'], 0),
    ('What was one major effect of the Sixties Scoop on Indigenous children?', ['A disrupted connection to their culture and communities', 'An improved connection to their culture and communities', 'No effect on their lives at all', 'This concept has no relevance to social studies'], 0),
    ('Around which decade did the Sixties Scoop primarily take place?', ['The 1960s and into later decades', 'The 1600s', 'The 1990s only', 'This concept has no connection to Canadian history'], 0),
    ('Why is learning about the Sixties Scoop considered important for understanding Canadian history?', ['It helps students understand the lasting impact of past policies on Indigenous families and communities', 'This event has no connection to Canadian history', 'This concept has no relevance to social studies', 'The Sixties Scoop had no lasting impact on anyone'], 0),
    ('Why might learning about the Sixties Scoop connect to broader lessons about reconciliation in Canada?', ['Understanding past harms can help support present-day efforts toward reconciliation', 'Reconciliation has no connection to past events like the Sixties Scoop', 'This concept has no relevance to social studies', 'The Sixties Scoop has no relationship to reconciliation efforts'], 0)]),
]),
day(175, [
L('Media Literacy: Understanding Infographics and Data Visuals',
  'Grade 5 Language strand: an infographic combines images, charts, and brief text to present information in a way that is quick to read and easy to understand at a glance.',
  [('What is an infographic?', ['A combination of images, charts, and brief text used to present information', 'A long, detailed essay with no visuals', 'A single photograph with no accompanying text', 'A list of unrelated random facts'], 0),
   ('Why might an infographic be considered quick to read?', ['It presents information visually, so it can be understood at a glance', 'Infographics always contain more text than a full essay', 'This concept has no connection to media literacy', 'Infographics never include any images or charts'], 0),
   ('What might a chart within an infographic help a reader do?', ['Compare data or see a trend quickly', 'Understand a topic that has no data connected to it at all', 'This concept has no relevance to media literacy', 'Charts are never included within an infographic'], 0),
   ('Why might a company or organization choose to present information as an infographic instead of a plain paragraph?', ['A visual format can make complex information easier and faster to understand', 'Infographics always make information harder to understand', 'This concept has no connection to media literacy', 'Plain paragraphs are always more engaging than any visual format'], 0),
   ('Why is it useful for readers to think critically about the data shown in an infographic?', ['Even visual data can be presented in a misleading or biased way', 'Data shown visually is always completely accurate and unbiased', 'This concept has no relevance to media literacy', 'Infographics never involve any interpretation of information'], 0)]),
M('Measurement: Converting Between Square Units of Area',
  'Grade 5 Math strand: converting between square units of area, such as square centimetres and square metres, requires accounting for the fact that area is measured in two dimensions, so the conversion factor must be squared.',
  [('What makes converting square units different from converting linear units?', ['Area is measured in two dimensions, so the conversion factor must be squared', 'Square units never need to be converted at all', 'Converting square units always uses the exact same factor as linear units', 'This concept has no connection to measurement'], 0),
   ('How many square centimetres are in a square metre, given that 1 metre equals 100 centimetres?', ['10000', '100', '1000', '10'], 0),
   ('If a rectangle has an area of 2 square metres, how many square centimetres is that?', ['20000', '200', '2000', '20'], 0),
   ('Why might a builder need to convert between square units of area when planning a project?', ['Materials or measurements may be listed in different units that need to match', 'Builders never need to compare measurements in different units', 'This concept has no relevance to measurement', 'Area measurements are never useful in construction'], 0),
   ('Why is it important to square the conversion factor when converting units of area rather than length?', ['Area covers two dimensions, so both the length and width conversions apply', 'Area only ever involves a single dimension', 'This concept has no connection to measurement', 'Squaring the conversion factor is never necessary for area'], 0)]),
Sc('Fermentation: How Yeast and Bacteria Transform Food',
   'Grade 5 Science strand: fermentation is a chemical process in which yeast or bacteria break down sugars in food, producing gases or acids that create new flavours and textures, as seen in bread, yogurt, and pickles.',
   [('What organisms are commonly involved in fermentation?', ['Yeast or bacteria', 'Only large mammals', 'Only fish', 'This concept has no connection to fermentation'], 0),
    ('What do yeast or bacteria break down during fermentation?', ['Sugars in food', 'Metal objects', 'Rocks and minerals', 'This concept has no relevance to fermentation'], 0),
    ('Which of these foods is commonly made using fermentation?', ['Yogurt', 'A fresh apple straight from a tree', 'Plain water', 'A raw carrot'], 0),
    ('Why does bread dough rise during fermentation?', ['Yeast produces gas bubbles as it breaks down sugars in the dough', 'Bread dough never changes during fermentation', 'This concept has no connection to science', 'Fermentation always makes dough flatter rather than causing it to rise'], 0),
    ('Why might fermentation be considered a chemical change rather than a physical change?', ['New substances, such as gases or acids, are produced that were not there before', 'Fermentation never produces any new substances', 'This concept has no relevance to science', 'Fermentation only changes the shape of the food involved'], 0)]),
SS('Voter Turnout and Civic Engagement in Canada',
   'Grade 5 Social Studies strand: voter turnout refers to the percentage of eligible voters who actually cast a ballot in an election, and civic engagement includes the many ways citizens participate in their communities and government beyond voting.',
   [('What does voter turnout measure?', ['The percentage of eligible voters who actually cast a ballot', 'The total population of a country', 'The number of political parties in an election', 'This concept has no connection to elections'], 0),
    ('What is civic engagement?', ['The many ways citizens participate in their communities and government', 'A rule that only applies to elected officials', 'A type of tax collected by the government', 'This concept has no relevance to social studies'], 0),
    ('Besides voting, which of these is an example of civic engagement?', ['Volunteering for a local community organization', 'Ignoring all local community events', 'Refusing to learn about local issues', 'This concept has no connection to civic engagement'], 0),
    ('Why might low voter turnout be a concern in a democracy?', ['Election results may not fully reflect the views of the entire eligible population', 'Voter turnout never affects how election results are viewed', 'This concept has no relevance to social studies', 'Every eligible voter always votes in every election'], 0),
    ('Why might schools encourage students to learn about civic engagement at a young age?', ['Early understanding can help build habits of active, informed participation later in life', 'Civic engagement has no connection to how communities function', 'This concept has no relevance to social studies', 'Learning about civic engagement has no value until adulthood'], 0)]),
]),
day(176, [
L('Writing: Writing an Acrostic Poem',
  'Grade 5 Language strand: an acrostic poem uses the letters of a word or name, arranged vertically, so that the first letter of each line spells out that word when read from top to bottom.',
  [('How is an acrostic poem arranged?', ['The letters of a word are arranged vertically, spelling it out down the page', 'The letters of a word are hidden randomly throughout the poem', 'The poem must always rhyme at the end of every line', 'This concept has no connection to poetry'], 0),
   ('What does the first letter of each line in an acrostic poem do?', ['Spells out a word or name when read from top to bottom', 'Has no connection to the poems overall topic', 'Must always be a vowel', 'This concept has no relevance to poetry'], 0),
   ('Why might a poet choose a topic word before writing an acrostic poem?', ['The chosen word determines the structure and starting letters of each line', 'The topic word has no effect on how the poem is written', 'This concept has no connection to writing', 'An acrostic poem never needs a chosen word at all'], 0),
   ('Why might writing an acrostic poem be a creative way to describe a topic, such as a season?', ['It challenges the writer to connect descriptive words to specific starting letters', 'Acrostic poems never require any creativity', 'This concept has no relevance to writing', 'The starting letters of an acrostic poem are always randomly chosen'], 0),
   ('What skill might a student practise while brainstorming words for each line of an acrostic poem?', ['Thinking of descriptive vocabulary that starts with a specific letter', 'Ignoring the topic of the poem completely', 'This concept has no connection to vocabulary', 'Acrostic poems never involve any vocabulary practice'], 0)]),
M('Geometry: Diagonals of Polygons',
  'Grade 5 Math strand: a diagonal is a line segment that connects two non-adjacent vertices of a polygon, and the number of diagonals a polygon has depends on how many sides it has.',
  [('What is a diagonal in a polygon?', ['A line segment connecting two non-adjacent vertices', 'A line segment connecting two adjacent vertices', 'A line that measures the perimeter of a shape', 'A curved line inside a shape'], 0),
   ('How many diagonals does a square have?', ['2', '4', '1', '0'], 0),
   ('Does a triangle have any diagonals?', ['No, because every pair of vertices in a triangle is adjacent', 'Yes, it always has exactly three diagonals', 'Yes, it always has exactly one diagonal', 'This concept has no connection to geometry'], 0),
   ('Why does a pentagon have more diagonals than a square?', ['A pentagon has more vertices, creating more possible non-adjacent connections', 'A pentagon always has fewer vertices than a square', 'This concept has no relevance to geometry', 'The number of diagonals has no connection to the number of sides'], 0),
   ('Why might drawing the diagonals of a polygon be useful when studying its properties?', ['Diagonals can help divide a shape into smaller, more familiar shapes like triangles', 'Diagonals never provide any useful information about a shape', 'This concept has no relevance to math', 'Diagonals can only be drawn on a circle, never a polygon'], 0)]),
Sc('Invasive Species and Their Impact on Ecosystems',
   'Grade 5 Science strand: an invasive species is a plant or animal introduced to a new environment where it has no natural predators, often allowing it to spread quickly and harm native species and ecosystems.',
   [('What is an invasive species?', ['A plant or animal introduced to a new environment where it has no natural predators', 'A species that has always lived in a particular ecosystem', 'A species that never reproduces in a new environment', 'This concept has no connection to ecosystems'], 0),
    ('Why might an invasive species spread quickly in a new environment?', ['It often has no natural predators to keep its population in check', 'Invasive species are always kept in check immediately', 'This concept has no relevance to invasive species', 'New environments always prevent any species from spreading'], 0),
    ('What impact can an invasive species have on native species?', ['It can outcompete native species for food and resources', 'It always helps native species thrive with no negative effects', 'This concept has no connection to ecosystems', 'Invasive species never interact with native species in any way'], 0),
    ('Why might people be asked not to release aquarium fish into local lakes or rivers?', ['Released fish could become an invasive species that harms the local ecosystem', 'Releasing aquarium fish never has any effect on a local ecosystem', 'This concept has no relevance to science', 'Local ecosystems are never affected by species introduced by people'], 0),
    ('Why do scientists closely monitor and try to control invasive species?', ['Uncontrolled invasive species can seriously disrupt the balance of an ecosystem', 'Invasive species never need to be monitored or controlled', 'This concept has no relevance to science', 'Invasive species always have a positive effect on every ecosystem'], 0)]),
SS('Canadas Manufacturing Industry and Its Regions',
   'Grade 5 Social Studies strand: manufacturing involves turning raw materials into finished products, and in Canada it is concentrated in certain regions, particularly parts of Ontario and Quebec, that produce goods such as automobiles and machinery.',
   [('What does manufacturing involve?', ['Turning raw materials into finished products', 'Growing crops on a farm', 'Collecting taxes for the government', 'This concept has no connection to industry'], 0),
    ('In which regions of Canada is manufacturing particularly concentrated?', ['Parts of Ontario and Quebec', 'Only in the northern territories', 'Only along the Pacific coast', 'This concept has no relevance to Canadian geography'], 0),
    ('Which of these is an example of a product commonly made in Canadas manufacturing industry?', ['Automobiles', 'Wild-caught fish straight from the ocean', 'Uncut forest timber', 'This concept has no connection to manufacturing'], 0),
    ('Why might a region with strong transportation links, such as highways and railways, attract manufacturing industries?', ['Good transportation makes it easier to move raw materials in and finished products out', 'Transportation links have no effect on where manufacturing takes place', 'This concept has no relevance to social studies', 'Manufacturing never depends on transportation of any kind'], 0),
    ('Why is manufacturing considered an important part of the Canadian economy?', ['It creates jobs and produces goods that can be sold within Canada and abroad', 'Manufacturing has no connection to the Canadian economy', 'This concept has no relevance to social studies', 'Manufacturing goods are never sold outside of Canada'], 0)]),
]),
day(177, [
L('Grammar: Using Articles Correctly — A, An, and The',
  'Grade 5 Language strand: articles are small words that come before a noun, with a used before consonant sounds, an used before vowel sounds, and the used when referring to a specific, already known noun.',
  [('What is an article in grammar?', ['A small word that comes before a noun', 'A word that shows an action', 'A word that describes a verb', 'A word that joins two sentences together'], 0),
   ('When is the article an typically used?', ['Before a word that begins with a vowel sound', 'Before every single noun, with no exceptions', 'Only before proper nouns', 'Only at the end of a sentence'], 0),
   ('Which article would correctly complete the sentence: I saw ___ elephant at the zoo?', ['an', 'a', 'the only', 'no article is needed'], 0),
   ('Why might a writer use the instead of a or an in a sentence?', ['The is used when referring to a specific, already known noun', 'The is always used before every noun in a sentence', 'This concept has no connection to grammar', 'A and an are always used for specific, known nouns'], 0),
   ('Why is it important to choose the correct article based on sound rather than just the first letter of a word, as in an hour?', ['Article choice depends on the actual sound a word begins with, not always its spelling', 'Article choice never depends on how a word sounds', 'This concept has no relevance to grammar', 'The word hour always requires the article a'], 0)]),
M('Financial Literacy: An Introduction to Stocks and Investing',
  'Grade 5 Math strand: a stock represents a small share of ownership in a company, and investing means putting money into something, such as stocks, with the goal of growing that money over time.',
  [('What does owning a stock represent?', ['A small share of ownership in a company', 'A loan given directly to a bank', 'A type of tax paid to the government', 'A coupon for a discount at a store'], 0),
   ('What is the main goal of investing?', ['Growing money over time', 'Spending money immediately on entertainment', 'Avoiding the use of money entirely', 'This concept has no connection to financial literacy'], 0),
   ('If the value of a stock increases after it is purchased, what generally happens to its worth to the owner?', ['The stocks value to the owner increases', 'The stocks value to the owner always decreases', 'The stocks value never changes for any reason', 'This concept has no relevance to investing'], 0),
   ('Why might investing be considered riskier than simply saving money in a bank account?', ['The value of an investment like a stock can go up or down over time', 'Investing always guarantees the exact same result as saving money', 'This concept has no connection to financial literacy', 'Stocks can never lose value under any circumstances'], 0),
   ('Why might understanding the basics of investing be a useful financial literacy skill?', ['It helps people understand one way that money can potentially grow over time', 'Investing has no connection to financial literacy at all', 'This concept has no relevance to math', 'Money can never grow through any form of investing'], 0)]),
Sc('Composting: Turning Waste Into Useful Soil',
   'Grade 5 Science strand: composting is a natural process in which decomposers break down food scraps and plant material into nutrient-rich soil, reducing waste while creating a useful resource for growing plants.',
   [('What is composting?', ['A natural process that breaks down food scraps and plant material into nutrient-rich soil', 'A process that turns soil into plastic', 'A method for freezing food to preserve it', 'This concept has no connection to science'], 0),
    ('What role do decomposers play in composting?', ['They break down food scraps and plant material', 'They prevent any breakdown of organic material', 'They have no role in the composting process', 'This concept has no relevance to composting'], 0),
    ('What is one benefit of composting food scraps instead of throwing them away?', ['It reduces waste while creating a useful resource for growing plants', 'It always increases the amount of waste sent to a landfill', 'This concept has no connection to science', 'Composting has no effect on the amount of waste produced'], 0),
    ('Why might gardeners add compost to their soil?', ['Compost adds nutrients that can help plants grow more healthily', 'Compost always harms the plants it is added to', 'This concept has no relevance to composting', 'Compost has no effect on soil quality at all'], 0),
    ('Why is composting considered an environmentally friendly practice?', ['It reduces the amount of organic waste sent to landfills and recycles nutrients naturally', 'Composting has no connection to environmental practices', 'This concept has no relevance to science', 'Composting always increases pollution in the environment'], 0)]),
SS('VIA Rail and Passenger Transportation in Canada',
   'Grade 5 Social Studies strand: VIA Rail is a Crown corporation that operates passenger train service across much of Canada, connecting cities and communities and playing a role in the countrys transportation history.',
   [('What type of organization is VIA Rail?', ['A Crown corporation', 'A private airline', 'A municipal bus service', 'This concept has no connection to transportation'], 0),
    ('What service does VIA Rail primarily provide?', ['Passenger train service across much of Canada', 'International air travel', 'Local city bus routes only', 'This concept has no relevance to social studies'], 0),
    ('What does VIA Rail help connect across the country?', ['Cities and communities', 'Only major international airports', 'Only ocean ports', 'This concept has no connection to Canadian transportation'], 0),
    ('Why might passenger train service be especially useful for connecting communities across a large country like Canada?', ['It can provide an affordable and reliable way to travel between distant places', 'Train service has no advantages for a large country', 'This concept has no relevance to social studies', 'Passenger trains only ever travel very short distances'], 0),
    ('Why might VIA Rail, as a Crown corporation, be considered part of Canadas transportation history?', ['It reflects how rail travel has long played a role in connecting Canadians across the country', 'Crown corporations have no connection to transportation history', 'This concept has no relevance to social studies', 'Rail travel has never been an important part of Canadian history'], 0)]),
]),
day(178, [
L('Oral Communication: Oral Storytelling Traditions',
  'Grade 5 Language strand: oral storytelling traditions pass down stories, history, and values through spoken word rather than writing, often using repetition, rhythm, and voice to help engage listeners and preserve memory.',
  [('What defines an oral storytelling tradition?', ['Stories, history, and values passed down through spoken word rather than writing', 'Stories that can only ever be written down', 'A tradition that has no connection to spoken language', 'A story told only through pictures with no words'], 0),
   ('Which technique might a storyteller use to help listeners remember a story?', ['Repetition and rhythm', 'Speaking as quietly and quickly as possible', 'Avoiding any changes in voice or tone', 'This concept has no connection to oral communication'], 0),
   ('Why might voice and tone be especially important in oral storytelling?', ['They can help bring characters and events to life for listeners', 'Voice and tone have no effect on how a story is understood', 'This concept has no relevance to oral communication', 'A storyteller should always speak in exactly the same tone throughout'], 0),
   ('Why have oral storytelling traditions been important for passing down history and values across generations?', ['They allow knowledge to be shared and remembered even without written records', 'Oral traditions have no connection to preserving history or values', 'This concept has no relevance to social studies', 'Oral traditions were never used before writing existed'], 0),
   ('Why might listening carefully be an especially important skill for someone experiencing oral storytelling?', ['The story exists only in the spoken words, without a written text to revisit', 'Listening has no importance in oral storytelling', 'This concept has no relevance to oral communication', 'Oral stories are always also available in written form at the same time'], 0)]),
M('Number Sense: Perfect Numbers',
  'Grade 5 Math strand: a perfect number is a whole number that equals the sum of its proper divisors, meaning all the numbers that divide it evenly except itself, such as 6, whose divisors 1, 2, and 3 add up to 6.',
  [('What is a perfect number?', ['A whole number that equals the sum of its proper divisors', 'A number that has no divisors at all', 'A number that is always divisible by 2', 'A number with exactly two digits'], 0),
   ('What are the proper divisors of 6?', ['1, 2, and 3', '1, 2, 3, and 6', '2 and 3 only', '1 and 6 only'], 0),
   ('Why is 6 considered a perfect number?', ['Its proper divisors 1, 2, and 3 add up to exactly 6', 'It has no proper divisors at all', 'This concept has no connection to perfect numbers', '6 cannot be divided evenly by any other number'], 0),
   ('What are the proper divisors of 28, the next perfect number after 6?', ['1, 2, 4, 7, and 14', '1, 2, and 4 only', '1 and 28 only', 'This concept has no relevance to math'], 0),
   ('Why might exploring perfect numbers be a good way to practise finding factors of a number?', ['Identifying all the proper divisors of a number requires careful factor exploration', 'Perfect numbers have no connection to finding factors', 'This concept has no relevance to number sense', 'Finding factors is never useful when exploring numbers'], 0)]),
Sc('Water Treatment: How Water Is Purified for Drinking',
   'Grade 5 Science strand: water treatment removes harmful substances and organisms from water through steps such as filtration and disinfection, making it safe for people to drink.',
   [('What is the main purpose of water treatment?', ['Removing harmful substances and organisms to make water safe to drink', 'Adding colour to water for decoration', 'Freezing water for long-term storage', 'This concept has no connection to science'], 0),
    ('What is filtration used for during water treatment?', ['Removing solid particles and impurities from water', 'Adding more particles into the water', 'Changing the temperature of the water', 'This concept has no relevance to water treatment'], 0),
    ('What is disinfection used for during water treatment?', ['Killing harmful organisms that could make people sick', 'Making water taste sweeter', 'Changing the colour of the water', 'This concept has no connection to science'], 0),
    ('Why is water treatment an important process for a community?', ['It helps ensure that drinking water is safe and does not spread disease', 'Water treatment has no effect on whether water is safe to drink', 'This concept has no relevance to science', 'Untreated water is always exactly as safe as treated water'], 0),
    ('Why might engineers design water treatment systems with multiple steps rather than just one?', ['Different steps can target different types of impurities and organisms', 'A single step always removes every possible impurity from water', 'This concept has no relevance to science', 'Multiple steps make water treatment systems completely unnecessary'], 0)]),
SS('Canadas Role in International Development and Foreign Aid',
   'Grade 5 Social Studies strand: international development and foreign aid involve Canada providing money, resources, or expertise to help other countries address challenges such as poverty, education, and health care.',
   [('What does foreign aid generally involve?', ['Providing money, resources, or expertise to help other countries', 'Collecting taxes from other countries', 'Building highways only within Canada', 'This concept has no connection to social studies'], 0),
    ('Which of these challenges might Canadian foreign aid help address in another country?', ['Poverty and access to health care', 'The design of a countrys national flag', 'The scheduling of a countrys sports events', 'This concept has no relevance to foreign aid'], 0),
    ('Which types of organizations might help carry out Canadas international development work?', ['Government agencies and non-governmental organizations', 'Only professional sports leagues', 'Only private individual citizens acting alone', 'This concept has no connection to international development'], 0),
    ('Why might a country like Canada choose to provide foreign aid to other nations?', ['To help address global challenges and support international cooperation', 'Foreign aid has no connection to international cooperation', 'This concept has no relevance to social studies', 'Countries never provide assistance to other nations'], 0),
    ('Why might learning about international development help students understand Canadas global role?', ['It shows how Canada engages with and supports other countries beyond its own borders', 'International development has no connection to Canadas global role', 'This concept has no relevance to social studies', 'Canada has no involvement in supporting other countries'], 0)]),
]),
day(179, [
L('Reading: Recognizing a Red Herring in a Mystery',
  'Grade 5 Language strand: a red herring is a clue or detail placed in a mystery story to mislead readers and distract them from the real solution, adding suspense and challenge to the plot.',
  [('What is a red herring in a mystery story?', ['A clue or detail placed to mislead readers away from the real solution', 'The correct clue that solves the mystery', 'A description of the setting only', 'This concept has no connection to reading'], 0),
   ('What effect might a red herring have on a reader?', ['It can distract the reader and add suspense to the plot', 'It always reveals the solution to the mystery immediately', 'It has no effect on how a reader experiences a story', 'This concept has no relevance to reading'], 0),
   ('Why might an author include a red herring in a mystery story?', ['To keep readers guessing and increase the challenge of solving the mystery', 'Red herrings are never included in mystery stories', 'This concept has no connection to reading', 'A red herring always makes a mystery easier to solve'], 0),
   ('Why might a careful reader try to separate red herrings from real clues while reading a mystery?', ['Identifying which details actually matter helps in solving the mystery accurately', 'Separating clues has no effect on understanding a mystery', 'This concept has no relevance to reading', 'Every clue in a mystery is always equally important to the solution'], 0),
   ('Why can red herrings make a mystery story more engaging for readers?', ['They add suspense by keeping the real solution uncertain for longer', 'Red herrings always make a mystery boring and predictable', 'This concept has no relevance to reading', 'Mysteries are never more engaging when they include misleading details'], 0)]),
M('Algebra: Evaluating Algebraic Expressions by Substitution',
  'Grade 5 Math strand: evaluating an algebraic expression means substituting a given value for the variable and then calculating the result, such as finding that 3x plus 2 equals 11 when x equals 3.',
  [('What does it mean to evaluate an algebraic expression?', ['Substituting a given value for the variable and calculating the result', 'Removing the variable from the expression entirely', 'Rewriting the expression without ever solving it', 'This concept has no connection to algebra'], 0),
   ('What is the value of 3x plus 2 when x equals 3?', ['11', '9', '8', '14'], 0),
   ('What is the value of 5x minus 4 when x equals 2?', ['6', '10', '2', '14'], 0),
   ('Why is substitution a useful strategy when evaluating an algebraic expression?', ['It replaces the unknown variable with a specific number so the expression can be calculated', 'Substitution never helps when evaluating an expression', 'This concept has no relevance to algebra', 'An algebraic expression can never be evaluated using substitution'], 0),
   ('What is the value of 4x plus 3x when x equals 2?', ['14', '10', '9', '16'], 0)]),
Sc('Wildfires and Forest Ecosystem Renewal',
   'Grade 5 Science strand: wildfires can be sparked by lightning or human activity, and while they can be destructive, some forest ecosystems depend on periodic fires to clear old growth, recycle nutrients, and trigger new plant growth.',
   [('What can spark a wildfire?', ['Lightning or human activity', 'Only heavy rainfall', 'Only cold temperatures', 'This concept has no connection to wildfires'], 0),
    ('What is one way some forest ecosystems benefit from periodic wildfires?', ['Old growth is cleared and nutrients are recycled into the soil', 'Wildfires always destroy an ecosystem with no possible benefit', 'This concept has no relevance to science', 'Wildfires never have any effect on soil nutrients'], 0),
    ('What might happen to certain seeds after a wildfire passes through a forest?', ['Some seeds are triggered by heat to open and begin new growth', 'All seeds are permanently destroyed with no chance of new growth', 'This concept has no connection to wildfires', 'Seeds are never affected in any way by fire'], 0),
    ('Why might forest managers sometimes use controlled, carefully planned burns?', ['Controlled burns can reduce the buildup of materials that fuel larger, more dangerous wildfires', 'Controlled burns always increase the risk of uncontrollable wildfires', 'This concept has no relevance to science', 'Forest managers never use fire as a management tool'], 0),
    ('Why is it important for scientists to understand the role of wildfires in forest ecosystems?', ['It helps them balance the destructive risks of fire with its natural ecological benefits', 'Wildfires have no ecological role in any forest ecosystem', 'This concept has no relevance to science', 'Understanding wildfires has no connection to managing forests'], 0)]),
SS('The World Trade Organization and Canadas Trade Policy',
   'Grade 5 Social Studies strand: the World Trade Organization is an international organization that sets rules for trade between countries, and Canada is a member that follows these rules while also negotiating its own trade agreements.',
   [('What does the World Trade Organization do?', ['Sets rules for trade between countries', 'Manages the currency of every country', 'Organizes international sports competitions', 'This concept has no connection to trade'], 0),
    ('What is Canadas relationship to the World Trade Organization?', ['Canada is a member that follows its rules for international trade', 'Canada has no connection to the World Trade Organization', 'Canada leads the organization on its own', 'This concept has no relevance to social studies'], 0),
    ('What might the World Trade Organization help resolve between countries?', ['Trade disputes between member countries', 'Disputes about national sports team rankings', 'Disagreements about weather forecasting', 'This concept has no connection to trade policy'], 0),
    ('Why might having shared international trade rules benefit countries like Canada?', ['Shared rules can make trade between countries fairer and more predictable', 'Shared trade rules have no benefit to any country', 'This concept has no relevance to social studies', 'Trade between countries never requires any agreed-upon rules'], 0),
    ('Why might Canada also negotiate its own separate trade agreements in addition to following World Trade Organization rules?', ['Separate agreements can address specific trading relationships with particular countries or regions', 'Canada never negotiates any trade agreements of its own', 'This concept has no relevance to social studies', 'World Trade Organization rules always replace the need for any other trade agreements'], 0)]),
]),
day(180, [
L('Language Review: Pronouns, Poetry Forms, and Media Literacy',
  'Grade 5 Language strand review: students revisit reflexive and indefinite pronouns, writing a haiku, acronyms and abbreviations, understanding subplot, and infographics and data visuals.',
  [('What does a reflexive pronoun do?', ['Refers back to the subject of a sentence', 'Names a location', 'Joins two independent clauses', 'Shows possession only'], 0),
   ('What syllable pattern does a traditional haiku follow?', ['Five, seven, five', 'Four, four, four', 'Six, six, six', 'Two, four, two'], 0),
   ('What is an acronym?', ['A word formed from the first letters of a phrase, pronounced as a word', 'A word that rhymes with another word', 'A word with an opposite meaning to another word', 'A word borrowed directly from another language'], 0),
   ('What is a subplot?', ['A secondary storyline that runs alongside the main plot', 'The very first event in a story', 'A summary of the entire story', 'The setting where a story takes place'], 0),
   ('What is an infographic?', ['A combination of images, charts, and brief text used to present information', 'A long, detailed essay with no visuals', 'A single photograph with no accompanying text', 'A list of unrelated random facts'], 0)]),
M('Math Review: Symmetry, Financial Literacy, and Number Sense',
  'Grade 5 Math strand review: students revisit line symmetry, understanding pay stubs and wages, palindromic numbers, nets of pyramids, and converting between square units of area.',
  [('What is a line of symmetry?', ['A line that divides a shape into two matching mirror-image halves', 'A line that always passes through only one corner of a shape', 'A line that measures the perimeter of a shape', 'A line that shows how a shape was rotated'], 0),
   ('What does a pay stub show?', ['How much money a worker earned and what was deducted', 'A list of items purchased at a store', 'A record of a persons daily schedule', 'A summary of a persons grades in school'], 0),
   ('What is a palindromic number?', ['A number that reads the same forward and backward', 'A number that is always divisible by 10', 'A number with only one digit', 'A number that can never be added to another number'], 0),
   ('What is a net in geometry?', ['A two-dimensional pattern that can be folded into a three-dimensional shape', 'A tool used to measure angles', 'A type of graph used to display data', 'A line that divides a shape into equal halves'], 0),
   ('What makes converting square units different from converting linear units?', ['Area is measured in two dimensions, so the conversion factor must be squared', 'Square units never need to be converted at all', 'Converting square units always uses the exact same factor as linear units', 'This concept has no connection to measurement'], 0)]),
Sc('Science Review: Natural Disasters, Ecosystems, and Energy',
   'Grade 5 Science strand review: students revisit tsunamis, desert ecosystems, nuclear energy, refraction and lenses, and fermentation.',
   [('What most commonly triggers a tsunami?', ['An underwater earthquake', 'A gentle ocean breeze', 'A change in the tide alone', 'A cloud passing over the ocean'], 0),
    ('What is a defining feature of a desert ecosystem?', ['Very little rainfall', 'Constant heavy rainfall', 'Extremely cold temperatures year-round', 'This concept has no connection to ecosystems'], 0),
    ('How is nuclear energy typically produced?', ['By splitting atoms in a process called fission', 'By burning coal in a large furnace', 'By capturing energy directly from sunlight', 'By spinning turbines using only wind'], 0),
    ('What is refraction?', ['The bending of light as it passes from one material into another', 'The bouncing of light off a mirror', 'The complete blocking of light by an object', 'This concept has no connection to light'], 0),
    ('What organisms are commonly involved in fermentation?', ['Yeast or bacteria', 'Only large mammals', 'Only fish', 'This concept has no connection to fermentation'], 0)]),
SS('SocialStudies Review: Government Institutions, Data, and Trade',
   'Grade 5 Social Studies strand review: students revisit the Privy Council, the Supreme Court of Canada, Statistics Canada, the Sixties Scoop, and voter turnout and civic engagement.',
   [('Who does the Privy Council formally advise?', ['The Governor General', 'The Supreme Court', 'A foreign government', 'A municipal council'], 0),
    ('What is the Supreme Court of Canada?', ['The highest court in the country', 'A court that only handles municipal bylaws', 'A committee that writes new federal laws', 'A court found only in one province'], 0),
    ('What is Statistics Canada responsible for?', ['Collecting and publishing data about the countrys population, economy, and society', 'Enforcing municipal bylaws', 'Running the Canadian Armed Forces', 'Printing Canadian currency'], 0),
    ('What does the term Sixties Scoop refer to?', ['A period when many Indigenous children were removed from their families and placed in non-Indigenous homes', 'A national sports competition held in the 1960s', 'A program that built new highways across Canada', 'This concept has no connection to Canadian history'], 0),
    ('What does voter turnout measure?', ['The percentage of eligible voters who actually cast a ballot', 'The total population of a country', 'The number of political parties in an election', 'This concept has no connection to elections'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_171_180)
    append_to(5, g5_171_180)
