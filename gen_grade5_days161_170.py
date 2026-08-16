#!/usr/bin/env python3
"""Grade 5, Days 161-170 -- extends Grade 5 from 160 to 170 days. Modeled
exactly on gen_grade5_days151_160.py (itself modeled on
gen_grade5_days141_150.py): same L/M/Sc/SS helpers over gen_curriculum's
sub()/day()/append_to(), same TVO Learn placeholder resourceLabel/
resourceUrl convention (videoUrl intentionally left unset, filled in later
by the daily curriculum-video-backfill scheduled task), and the same
_rebalance_answer_positions() post-processing step.

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-160
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: comparative
and superlative adjectives, writing a weather report, circular and frame
narratives, building words with multiple affixes, recognizing product
placement in media, delivering an oral presentation with visual aids,
punctuating titles of books movies and songs, puns and wordplay, and
writing a persuasive poster or flyer for Language; classifying polygons as
regular or irregular, multiplying decimal numbers by two-digit whole
numbers, the distributive property, estimating and comparing mass with a
balance scale, calculating weighted averages, creating a simple invoice for
a small business, constructing circles with a compass, composite
transformations, and an introduction to bearings and navigation angles for
Math; ocean zones (sunlight, twilight, and midnight layers), mechanical
efficiency, chemical changes in cooking (baking soda and acids),
barometric pressure and storms, keystone species, how 3D printers build
objects, the nitrogen cycle, how helicopters fly, and plasma as the fourth
state of matter for Science; and the federal cabinet and the role of
ministers, the Speaker of the House of Commons, municipal bylaws, credit
unions and cooperatives, the Canadian Human Rights Commission, the St.
Lawrence Seaway, Canadian passports, Canadian embassies and consulates, and
access to information laws for Social Studies -- none of those exact ideas
appear in Days 1-160. Day 170 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch (drawing
one representative quiz question per subject from each of the first five
days of the batch, Days 161-165, exactly as Day 160 drew from Days
151-155). The four Day 170 review titles were checked against every
earlier review-day title in Days 1-160 and are textually distinct from all
of them.

No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the rest of Grade 5 Days 1-160 (e.g. "Canadas" not "Canada's", "governments"
not "government's").
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


def _rebalance_answer_positions(days, seed=20260813):
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


g5_161_170 = [
day(161, [
L('Grammar: Comparative and Superlative Adjectives',
  'Grade 5 Language strand: a comparative adjective compares two things, usually adding -er or the word more, while a superlative adjective compares three or more things, usually adding -est or the word most.',
  [('What does a comparative adjective do?', ['Compares two things', 'Compares three or more things', 'Names a single object', 'Shows an action'], 0),
   ('What does a superlative adjective do?', ['Compares three or more things', 'Compares only two things', 'Replaces a noun', 'Joins two sentences'], 0),
   ('Which sentence uses a comparative adjective correctly?', ['This book is longer than that one.', 'This book is longest than that one.', 'This book is long than that one.', 'This book is more longest than that one.'], 0),
   ('Which sentence uses a superlative adjective correctly?', ['She is the tallest student in the class.', 'She is the taller student in the class.', 'She is more tall in the class.', 'She is tall than the class.'], 0),
   ('Why might a writer choose more beautiful instead of beautifuller?', ['Longer adjectives usually use more rather than an -er ending', 'Every adjective must always add -er', 'Adjectives never change form when comparing things', 'This concept has no connection to grammar'], 0)]),
M('Geometry: Classifying Polygons — Regular and Irregular',
  'Grade 5 Math strand: a regular polygon has all sides and all angles equal, while an irregular polygon has sides or angles that are not all equal.',
  [('What is true about every side and angle of a regular polygon?', ['They are all equal', 'They are always different', 'Only the sides are equal, never the angles', 'A regular polygon has no straight sides'], 0),
   ('What describes an irregular polygon?', ['Its sides or angles are not all equal', 'All of its sides and angles are always equal', 'It always has exactly three sides', 'It can never be drawn on paper'], 0),
   ('Which shape is an example of a regular polygon?', ['A square', 'A rectangle that is not a square', 'A triangle with three different side lengths', 'A shape with sides of different lengths'], 0),
   ('Why might a rectangle that is not a square be considered irregular?', ['Its four angles are equal but its sides are not all the same length', 'All of its sides and angles are exactly equal', 'A rectangle can never be classified as a polygon', 'This concept has no connection to geometry'], 0),
   ('Why is classifying polygons as regular or irregular useful in geometry?', ['It helps describe and compare the properties of different shapes', 'Classifying shapes has no purpose in geometry', 'Every polygon is automatically regular', 'This concept has no relevance to math'], 0)]),
Sc('Ocean Zones: Sunlight, Twilight, and Midnight Layers of the Sea',
   'Grade 5 Science strand: the ocean is divided into layers based on how much sunlight reaches them, from the bright sunlight zone near the surface to the dark midnight zone in the deep sea.',
   [('What is the sunlight zone of the ocean?', ['The uppermost layer where enough light reaches for photosynthesis', 'The deepest, darkest part of the ocean', 'A layer found only in freshwater lakes', 'The layer with the coldest water temperature always'], 0),
    ('What happens to light as you move deeper into the twilight zone?', ['Light becomes dim and eventually disappears', 'Light becomes brighter the deeper you go', 'Light stays exactly the same at every depth', 'This concept has no connection to the ocean'], 0),
    ('What is the midnight zone of the ocean?', ['The deep, dark layer that receives no sunlight at all', 'The brightest layer near the surface', 'A shallow layer found only near beaches', 'This concept has no relevance to ocean science'], 0),
    ('Why might organisms in the midnight zone rely on bioluminescence?', ['Since no sunlight reaches that depth, producing their own light offers an advantage', 'Sunlight is always brightest in the midnight zone', 'Bioluminescence has no connection to deep-ocean life', 'This concept has no relevance to science'], 0),
    ('Why do scientists study the different zones of the ocean?', ['To better understand how light, pressure, and temperature affect ocean life', 'Ocean zones provide no useful scientific information', 'Every ocean zone has the exact same conditions', 'This concept has no connection to Earth science'], 0)]),
SS('The Federal Cabinet and the Role of Ministers',
   'Grade 5 Social Studies strand: the federal cabinet is a group of ministers, chosen by the prime minister, who each oversee a specific government department and help decide government policy.',
   [('Who chooses the members of the federal cabinet?', ['The prime minister', 'The Governor General alone', 'The Supreme Court', 'The Chief Electoral Officer'], 0),
    ('What does a cabinet minister typically oversee?', ['A specific government department', 'A single school in one city', 'A private business with no government connection', 'A professional sports league'], 0),
    ('What is one main role of the federal cabinet as a group?', ['Helping decide government policy', 'Deciding the outcome of court cases', 'Managing the affairs of individual municipalities only', 'Selecting the winners of national sports championships'], 0),
    ('Why might a prime minister choose ministers with different areas of expertise?', ['Different ministers can focus on different policy areas such as health or finance', 'Every minister must focus on the exact same department', 'Expertise has no connection to being a cabinet minister', 'This concept has no relevance to Canadian government'], 0),
    ('Why is the cabinet considered an important part of the federal government?', ['It helps develop and carry out government policy across many departments', 'The cabinet has no role in Canadian government at all', 'This concept has no connection to social studies', 'The cabinet only exists at the municipal level'], 0)]),
]),
day(162, [
L('Writing: Writing a Weather Report',
  'Grade 5 Language strand: a weather report presents current conditions and a forecast using clear, precise language and relevant details such as temperature, precipitation, and wind.',
  [('What is the main purpose of a weather report?', ['To present current conditions and a forecast clearly', 'To tell a fictional story with no factual details', 'To describe an imaginary place with no real information', 'To list random facts unrelated to weather'], 0),
   ('Which of these details would most likely appear in a weather report?', ['Expected temperature and chance of precipitation', 'The plot of a favourite movie', 'A list of unrelated historical dates', 'A description of a fictional character'], 0),
   ('Why might a weather report use precise numbers, such as a temperature in degrees?', ['Precise numbers help readers understand exactly what to expect', 'Precise numbers are never useful in a weather report', 'This concept has no connection to writing', 'Vague language is always clearer than precise numbers'], 0),
   ('Why might a writer organize a weather report from todays conditions to the upcoming forecast?', ['A clear order helps readers follow the information logically', 'Order never matters when writing a weather report', 'This concept has no relevance to writing', 'A weather report should never be organized in any order'], 0),
   ('Why is a weather report considered a useful type of nonfiction writing?', ['It communicates practical, factual information that affects daily plans', 'It has no connection to peoples daily lives', 'This concept has no relevance to writing', 'A weather report is always a form of fiction'], 0)]),
M('Number Sense: Multiplying Decimal Numbers by Two-Digit Whole Numbers',
  'Grade 5 Math strand: multiplying a decimal number by a two-digit whole number can be done by multiplying as if both numbers were whole numbers, then placing the decimal point correctly in the product.',
  [('What is one strategy for multiplying a decimal by a two-digit whole number?', ['Multiply as if both numbers were whole numbers, then place the decimal point', 'Always round both numbers to the nearest ten first', 'Ignore the decimal point completely', 'Add the two numbers together instead of multiplying'], 0),
   ('What is 2.5 multiplied by 12?', ['30', '25', '32', '20'], 0),
   ('What is 3.4 multiplied by 15?', ['51', '45', '54', '48'], 0),
   ('Why is it useful to estimate before multiplying a decimal by a two-digit number?', ['It provides a reasonable check for where the decimal point belongs in the answer', 'Estimating always gives the exact same value as the real product', 'Estimation is never useful when multiplying decimals', 'This concept has no connection to number sense'], 0),
   ('What is 1.2 multiplied by 20?', ['24', '22', '26', '20'], 0)]),
Sc('Mechanical Efficiency: Why Machines Are Never 100 Percent Efficient',
   'Grade 5 Science strand: mechanical efficiency compares the useful work a machine produces to the total energy put into it, and some energy is always lost to friction or heat, so no machine is perfectly efficient.',
   [('What does mechanical efficiency compare?', ['The useful work a machine produces to the total energy put into it', 'The colour of a machine to its size', 'The weight of a machine to its price', 'This concept has no connection to machines'], 0),
    ('Why is no machine perfectly efficient?', ['Some energy is always lost, often to friction or heat', 'Machines always convert all input energy into useful work', 'Efficiency has no connection to energy loss', 'This concept has no relevance to science'], 0),
    ('What commonly causes energy loss in a moving machine?', ['Friction between moving parts', 'Machines never lose any energy while running', 'Energy loss only happens in machines with no moving parts', 'This concept has no connection to mechanical efficiency'], 0),
    ('Why might engineers try to reduce friction in a machines design?', ['Reducing friction can improve efficiency by wasting less energy as heat', 'Friction always improves the efficiency of a machine', 'Reducing friction has no effect on efficiency at all', 'This concept has no relevance to engineering'], 0),
    ('Why is understanding mechanical efficiency useful when designing new machines?', ['It helps engineers create machines that waste less energy and perform better', 'Mechanical efficiency has no connection to designing machines', 'This concept has no relevance to science', 'Every machine is automatically perfectly efficient by design'], 0)]),
SS('The Speaker of the House of Commons',
   'Grade 5 Social Studies strand: the Speaker of the House of Commons is a Member of Parliament elected by other MPs to preside over debates, maintain order, and ensure the rules of Parliament are followed.',
   [('Who elects the Speaker of the House of Commons?', ['Other Members of Parliament', 'The Prime Minister alone', 'The Governor General alone', 'The Supreme Court'], 0),
    ('What is a main responsibility of the Speaker?', ['Presiding over debates and maintaining order', 'Writing every federal law personally', 'Managing the countrys currency', 'Leading the Canadian Armed Forces'], 0),
    ('Why is it important for the Speaker to remain impartial during debates?', ['Impartiality helps ensure fair and orderly discussion among all Members of Parliament', 'Impartiality has no connection to how debates are run', 'The Speaker is always a member of the governing party alone', 'This concept has no relevance to social studies'], 0),
    ('What might the Speaker do if Members of Parliament are not following the rules of debate?', ['Call them to order and enforce the rules of Parliament', 'Ignore any rule-breaking completely', 'Cancel the entire session of Parliament immediately', 'This concept has no connection to Canadian government'], 0),
    ('Why does the House of Commons need someone in the role of Speaker?', ['To help debates run fairly, calmly, and according to established rules', 'A Speaker has no useful role in Parliament', 'This concept has no relevance to Canadian government', 'Debates could never be organized without complete chaos regardless of a Speaker'], 0)]),
]),
day(163, [
L('Reading: Understanding Circular and Frame Narratives',
  'Grade 5 Language strand: a circular narrative ends where it began, bringing the story back to its starting point, while a frame narrative places one story inside another, often introduced by a narrator at the beginning and returned to at the end.',
  [('What happens in a circular narrative?', ['The story ends where it began', 'The story always ends in a completely different place with no connection', 'The story never has a beginning or an end', 'This concept has no connection to reading'], 0),
   ('What is a frame narrative?', ['A story placed inside another story', 'A story with no characters at all', 'A story told only through pictures', 'A story with no beginning or ending'], 0),
   ('Why might an author use a frame narrative structure?', ['It can provide context for the inner story through an outer narrator', 'Frame narratives are never used to add context', 'This concept has no connection to reading', 'A frame narrative always removes the need for a narrator'], 0),
   ('Why might a circular narrative structure feel satisfying to a reader?', ['Returning to the starting point can show how much has changed or been learned', 'Circular narratives never provide readers with any sense of closure', 'This concept has no relevance to reading', 'A circular narrative always confuses the reader with no purpose'], 0),
   ('What might signal the end of the outer story in a frame narrative?', ['The narrator returning to close out the story after the inner story ends', 'The story simply stopping without any conclusion', 'This concept has no connection to narrative structure', 'A frame narrative never includes an outer story'], 0)]),
M('Algebra: Understanding and Using the Distributive Property',
  'Grade 5 Math strand: the distributive property states that multiplying a number by a sum is the same as multiplying the number by each addend separately and then adding the products, such as 4 times the quantity 3 plus 5 equals 4 times 3 plus 4 times 5.',
  [('What does the distributive property allow you to do?', ['Multiply a number by a sum by multiplying each addend separately, then adding', 'Divide a number by zero', 'Ignore parentheses in an expression completely', 'Subtract a number from itself'], 0),
   ('Using the distributive property, what is 3 times the quantity 4 plus 2?', ['18', '14', '20', '16'], 0),
   ('Using the distributive property, what is 5 times the quantity 6 plus 3?', ['45', '40', '35', '50'], 0),
   ('Why might the distributive property be useful when multiplying mentally?', ['It can break a harder multiplication problem into two simpler ones', 'It always makes multiplication problems more difficult to solve', 'This concept has no connection to algebra', 'The distributive property only works with subtraction, never addition'], 0),
   ('Using the distributive property, what is 6 times the quantity 2 plus 5?', ['42', '35', '36', '40'], 0)]),
Sc('Chemical Changes in Cooking: How Baking Soda Reacts With Acids',
   'Grade 5 Science strand: baking soda is a base that reacts with acids, such as vinegar or lemon juice, producing carbon dioxide gas bubbles in a chemical change often used in cooking and baking.',
   [('What type of substance is baking soda?', ['A base', 'A metal', 'A gas with no other properties', 'A type of sugar'], 0),
    ('What gas is produced when baking soda reacts with an acid like vinegar?', ['Carbon dioxide', 'Pure oxygen', 'Helium', 'Nitrogen'], 0),
    ('Why is the reaction between baking soda and vinegar considered a chemical change?', ['A new substance, carbon dioxide gas, is produced that was not there before', 'No new substance is ever produced in this reaction', 'This concept has no connection to chemical changes', 'The reaction only changes the shape of the baking soda'], 0),
    ('Why might bakers add baking soda to a batter along with an acidic ingredient?', ['The reaction produces gas bubbles that help the batter rise', 'Baking soda always makes a batter denser and heavier', 'This concept has no connection to cooking or baking', 'Baking soda has no effect on batter at all'], 0),
    ('What might you observe if you mix baking soda with vinegar?', ['Fizzing and bubbling as gas is released', 'No change of any kind would ever occur', 'The mixture would instantly freeze solid', 'This concept has no relevance to science'], 0)]),
SS('Municipal Bylaws: Rules That Shape Local Communities',
   'Grade 5 Social Studies strand: municipal bylaws are local laws passed by city or town councils that regulate matters such as noise, parking, property standards, and animal control within a community.',
   [('Who passes municipal bylaws?', ['City or town councils', 'The federal Parliament', 'The Supreme Court', 'A private company'], 0),
    ('Which of these might a municipal bylaw regulate?', ['Noise levels in a neighbourhood', 'International trade agreements', 'Federal income tax rates', 'National immigration policy'], 0),
    ('Why might a community have a bylaw about noise levels at night?', ['To help residents get rest and maintain a peaceful neighbourhood', 'Noise bylaws have no connection to community life', 'This concept has no relevance to local government', 'Bylaws are never related to noise in a community'], 0),
    ('What might happen if a resident does not follow a municipal bylaw?', ['They could face a fine or other penalty set by the municipality', 'Nothing would ever happen since bylaws are optional', 'This concept has no connection to social studies', 'Only the federal government can enforce a municipal bylaw'], 0),
    ('Why are municipal bylaws considered an important part of local government?', ['They help address specific needs and concerns within a community', 'Bylaws have no real effect on how a community functions', 'This concept has no relevance to social studies', 'Bylaws are identical in every municipality across Canada'], 0)]),
]),
day(164, [
L('Vocabulary: Building Words with Multiple Affixes',
  'Grade 5 Language strand: some words combine more than one prefix or suffix, such as unbelievably, which adds the prefix un- and the suffixes -able and -ly to the root word believe.',
  [('What does it mean when a word has multiple affixes?', ['It combines more than one prefix or suffix', 'It has no root word at all', 'It uses only capital letters', 'It contains no vowels'], 0),
   ('Which word combines a prefix and two suffixes?', ['Unbelievably', 'Run', 'Happy', 'Cat'], 0),
   ('In the word unbelievably, what is the root word?', ['Believe', 'Un', 'Ably', 'Unbelieve'], 0),
   ('Why might understanding multiple affixes help a reader figure out a difficult word?', ['Breaking a word into its root and affixes can reveal its meaning', 'Affixes never provide any clues about a words meaning', 'This concept has no connection to vocabulary', 'A word with multiple affixes always has no meaning at all'], 0),
   ('Which word is built using a prefix and a suffix together?', ['Disagreement', 'Jump', 'Blue', 'Tree'], 0)]),
M('Measurement: Estimating and Comparing Mass Using a Balance Scale',
  'Grade 5 Math strand: a balance scale compares the mass of two objects by showing which side is heavier, and can be used with standard masses to estimate and measure the mass of an object.',
  [('What does a balance scale compare?', ['The mass of two objects', 'The colour of two objects', 'The length of two objects', 'The temperature of two objects'], 0),
   ('If one side of a balance scale tips downward, what does that indicate?', ['That side holds the object with greater mass', 'That side holds the object with less mass', 'Both sides always have equal mass', 'The scale is broken and cannot be trusted'], 0),
   ('How can standard masses be used with a balance scale?', ['They can be added to one side until the scale balances, showing the unknown mass', 'Standard masses are never used with a balance scale', 'This concept has no connection to measurement', 'Standard masses can only measure length, not mass'], 0),
   ('Why might estimating mass before measuring it be a useful strategy?', ['It gives a reasonable expectation to compare the actual measurement against', 'Estimating mass always matches the exact measurement perfectly', 'Estimation is never useful when measuring mass', 'This concept has no connection to measurement'], 0),
   ('What unit might commonly be used when measuring mass with a balance scale?', ['Grams or kilograms', 'Litres only', 'Degrees Celsius', 'Metres only'], 0)]),
Sc('Weather: How Barometric Pressure Helps Predict Storms',
   'Grade 5 Science strand: barometric pressure is the weight of the air pressing down on Earths surface, and a falling barometric pressure often signals that a storm is approaching.',
   [('What does barometric pressure measure?', ['The weight of the air pressing down on Earths surface', 'The temperature of the ocean', 'The speed of the wind only', 'The amount of snowfall in a season'], 0),
    ('What instrument is used to measure barometric pressure?', ['A barometer', 'A thermometer', 'A rain gauge', 'A compass'], 0),
    ('What does a falling barometric pressure often signal?', ['That a storm may be approaching', 'That the weather will always stay perfectly clear', 'That barometric pressure has no connection to weather', 'That temperatures will remain exactly the same'], 0),
    ('Why might meteorologists track changes in barometric pressure over time?', ['Changes in pressure can help forecast upcoming weather conditions', 'Barometric pressure never changes over time', 'This concept has no relevance to weather forecasting', 'Pressure changes have no connection to storms'], 0),
    ('What might rising barometric pressure often suggest about upcoming weather?', ['Clearer, more stable weather conditions', 'A storm is definitely about to arrive', 'Rising pressure always signals heavy rainfall', 'This concept has no connection to weather patterns'], 0)]),
SS('Credit Unions and Cooperatives: Banking Owned by Members',
   'Grade 5 Social Studies strand: a credit union is a financial cooperative owned and controlled by its members, who share in decision-making and any profits, unlike a bank owned by outside shareholders.',
   [('Who owns a credit union?', ['Its members', 'A single wealthy shareholder', 'Only the federal government', 'A foreign company'], 0),
    ('How does a credit union differ from a typical bank?', ['A credit union is owned by its members rather than outside shareholders', 'A credit union has no connection to banking services at all', 'A credit union is always owned by the federal government', 'This concept has no relevance to social studies'], 0),
    ('What might members of a credit union be able to do that shareholders of a typical bank cannot?', ['Take part more directly in decision-making about the cooperative', 'Members of a credit union have no say in how it operates', 'This concept has no connection to cooperatives', 'Only bank shareholders can ever vote on decisions'], 0),
    ('Why might some people choose to use a credit union instead of a large bank?', ['They may value being a member-owner with a voice in the organization', 'Credit unions never offer any banking services to their members', 'This concept has no relevance to financial literacy', 'Credit unions are identical in every way to large banks'], 0),
    ('What is one way that profits might be shared in a credit union?', ['They may be returned to members or reinvested in services', 'Profits are always kept by a single owner alone', 'A credit union never earns any profit', 'This concept has no connection to cooperatives'], 0)]),
]),
day(165, [
L('Media Literacy: Recognizing Product Placement in Media',
  'Grade 5 Language strand: product placement is when a brand or product appears within a movie, show, or video, often blending into the story rather than appearing as a separate advertisement.',
  [('What is product placement?', ['When a brand or product appears within a movie, show, or video', 'A separate commercial shown between segments of a program', 'A type of poster displayed outside a store', 'A written review of a product in a newspaper'], 0),
   ('How does product placement usually differ from a traditional advertisement?', ['It blends into the story rather than appearing as a separate ad', 'It always appears as a clearly labelled advertisement', 'It never involves showing a brand or product at all', 'This concept has no connection to media literacy'], 0),
   ('Why might companies use product placement instead of only traditional ads?', ['Viewers may be more receptive to a brand shown naturally within a story', 'Product placement is never effective at reaching viewers', 'This concept has no relevance to media literacy', 'Traditional advertisements are always more effective than product placement'], 0),
   ('Why is it useful for viewers to recognize product placement when watching media?', ['It helps them understand when they are being marketed to during a story', 'Recognizing product placement has no benefit to viewers', 'This concept has no connection to media literacy', 'Viewers never need to think critically about what they watch'], 0),
   ('Which of these is an example of product placement?', ['A character in a show visibly using a specific branded product', 'A commercial that airs during a break in a program', 'A billboard advertisement on the side of a road', 'A flyer mailed directly to someones home'], 0)]),
M('Data Management: Calculating Weighted Averages',
  'Grade 5 Math strand: a weighted average gives different amounts of importance to different values, such as when a test score counts more toward a final grade than a homework score.',
  [('What does a weighted average do differently from a regular average?', ['It gives different amounts of importance to different values', 'It always gives every value the exact same importance', 'It ignores some values completely', 'It can only be calculated using whole numbers'], 0),
   ('If a test score is worth twice as much as a homework score in a weighted average, what does that mean?', ['The test score counts for more of the final result', 'The homework score always counts for more of the final result', 'Both scores always count exactly the same amount', 'This concept has no connection to data management'], 0),
   ('Why might a teacher use a weighted average to calculate final grades?', ['It allows certain assignments, like tests, to count more than others', 'Weighted averages never affect how a final grade is calculated', 'This concept has no relevance to data management', 'Every assignment must always count the same amount'], 0),
   ('In which situation would a weighted average be more appropriate than a simple average?', ['When some values are more important to the final result than others', 'When every value is exactly equally important', 'A weighted average is never appropriate to use', 'This concept has no connection to math'], 0),
   ('Why is understanding weighted averages a useful real-world skill?', ['Many situations, like grading systems, rely on values counting differently', 'Weighted averages are never used outside of math class', 'This concept has no relevance to everyday life', 'All averages in real life are always simple averages'], 0)]),
Sc('Ecosystems: Keystone Species and Their Outsized Role',
   'Grade 5 Science strand: a keystone species has an unusually large effect on its ecosystem relative to its numbers, and removing it can cause major changes throughout the food web.',
   [('What is a keystone species?', ['A species with an unusually large effect on its ecosystem relative to its numbers', 'A species that has no effect on its ecosystem at all', 'The most numerous species in an ecosystem', 'A species that lives only in captivity'], 0),
    ('What might happen to an ecosystem if a keystone species is removed?', ['Major changes could occur throughout the food web', 'The ecosystem would remain exactly the same with no changes', 'Removing a keystone species always improves an ecosystem', 'This concept has no connection to ecosystems'], 0),
    ('Why is a keystone species effect on an ecosystem often described as outsized?', ['Its impact is much larger than its population size might suggest', 'Keystone species always have the largest population in an ecosystem', 'A keystone species has no measurable impact on its ecosystem', 'This concept has no relevance to science'], 0),
    ('Why might scientists pay close attention to keystone species when studying conservation?', ['Protecting a keystone species can help maintain the balance of an entire ecosystem', 'Keystone species have no connection to conservation efforts', 'This concept has no relevance to ecosystems', 'Conservation never depends on which species are present'], 0),
    ('Which of these best describes the role of a keystone species in a food web?', ['It helps hold the structure of the food web together', 'It plays no role in the food web at all', 'It only affects species located far outside its ecosystem', 'This concept has no connection to food webs'], 0)]),
SS('The Canadian Human Rights Commission and Its Role',
   'Grade 5 Social Studies strand: the Canadian Human Rights Commission investigates complaints of discrimination in federally regulated workplaces and services, working to promote equality across Canada.',
   [('What does the Canadian Human Rights Commission investigate?', ['Complaints of discrimination in federally regulated workplaces and services', 'The results of provincial sports competitions', 'The design of Canadian currency', 'International trade agreements'], 0),
    ('What is one goal of the Canadian Human Rights Commission?', ['Promoting equality across Canada', 'Eliminating all federal government departments', 'Setting the countrys interest rates', 'Managing national parks'], 0),
    ('Who might bring a complaint to the Canadian Human Rights Commission?', ['A person who believes they experienced discrimination in a federally regulated setting', 'Only members of Parliament', 'Only large corporations', 'Only foreign governments'], 0),
    ('Why might an independent commission be useful for addressing discrimination complaints?', ['Independence can help ensure complaints are reviewed fairly', 'Independence has no connection to reviewing complaints fairly', 'This concept has no relevance to social studies', 'Complaints are always reviewed unfairly regardless of independence'], 0),
    ('Why might learning about the Canadian Human Rights Commission be important for students?', ['It helps students understand how Canada works to protect equality and fairness', 'This organization has no connection to Canadian rights', 'This concept has no relevance to social studies', 'Human rights protections do not apply anywhere in Canada'], 0)]),
]),
day(166, [
L('Oral Communication: Delivering an Effective Oral Presentation with Visual Aids',
  'Grade 5 Language strand: an effective oral presentation combines clear speaking with visual aids, such as posters or slides, that support and reinforce the spoken information without overwhelming the audience.',
  [('What is one benefit of using a visual aid during a presentation?', ['It can support and reinforce the spoken information', 'Visual aids always distract from what a speaker is saying', 'A visual aid should always replace the spoken words entirely', 'This concept has no connection to oral communication'], 0),
   ('Why might a speaker avoid putting too much text on a single slide?', ['Too much text can overwhelm the audience and distract from the speaking', 'More text on a slide always makes a presentation clearer', 'This concept has no connection to oral communication', 'Audiences always prefer slides filled entirely with text'], 0),
   ('What is one way a speaker can make an oral presentation more effective?', ['Speaking clearly and making eye contact with the audience', 'Reading directly from notes without ever looking up', 'Speaking as quietly as possible throughout the presentation', 'Avoiding any visual aids under all circumstances'], 0),
   ('Why might practising a presentation beforehand improve its delivery?', ['Practice can help a speaker feel more confident and organized', 'Practising a presentation never improves how it is delivered', 'This concept has no relevance to oral communication', 'A speaker should never prepare in advance for a presentation'], 0),
   ('Why might a presenter use a chart instead of only spoken numbers to share data?', ['A chart can help the audience visualize the information more easily', 'Charts always make data harder to understand', 'This concept has no connection to oral communication', 'Spoken numbers are always clearer than a visual chart'], 0)]),
M('Financial Literacy: Creating a Simple Invoice for a Small Business',
  'Grade 5 Math strand: an invoice is a document that lists items or services provided, their prices, and the total amount owed, helping a small business keep track of sales and payments.',
  [('What is the main purpose of an invoice?', ['To list items or services provided, their prices, and the total owed', 'To describe a fictional story about a business', 'To list random facts unrelated to a sale', 'To record the weather on a given day'], 0),
   ('If a small business sells 3 items at 8 dollars each, what would the invoice total show before any tax?', ['24 dollars', '11 dollars', '8 dollars', '32 dollars'], 0),
   ('Why might a small business keep copies of every invoice it creates?', ['It helps track sales and confirm what customers were charged', 'Invoices are never useful for keeping business records', 'This concept has no connection to financial literacy', 'A business never needs to track its sales'], 0),
   ('If an invoice lists 2 items at 15 dollars each plus a 5 dollar delivery fee, what is the total?', ['35 dollars', '30 dollars', '20 dollars', '40 dollars'], 0),
   ('Why is it important for an invoice to clearly list each item and its price?', ['It helps both the business and the customer understand exactly what was charged', 'Listing individual items and prices is never useful on an invoice', 'This concept has no relevance to financial literacy', 'An invoice should never include any prices'], 0)]),
Sc('Technology and Design: How 3D Printers Build Objects Layer by Layer',
   'Grade 5 Science strand: a 3D printer builds a solid object by adding material one thin layer at a time, following a digital design, until the full three-dimensional shape is complete.',
   [('How does a 3D printer build an object?', ['By adding material one thin layer at a time', 'By carving material away from a solid block', 'By melting an entire object all at once', 'By printing only flat, two-dimensional images'], 0),
    ('What does a 3D printer follow in order to build an object?', ['A digital design', 'A random pattern with no plan', 'Only a sketch drawn by hand with no digital file', 'This concept has no connection to technology'], 0),
    ('Why might building an object layer by layer allow for complex shapes?', ['Each thin layer can be shaped precisely before the next one is added', 'Layer by layer building always produces the exact same simple shape', 'This concept has no connection to 3D printing', 'Complex shapes can never be created using a 3D printer'], 0),
    ('What might 3D printing be used for in real life?', ['Creating prototypes, tools, or replacement parts', 'Only printing flat photographs on paper', 'This concept has no real-world application', '3D printing can only be used to make food'], 0),
    ('Why might engineers use 3D printing to test a new design?', ['It allows them to quickly create and examine a physical model of their design', '3D printing has no connection to testing new designs', 'This concept has no relevance to technology and design', 'Engineers never need to test a design before finishing it'], 0)]),
SS('The St. Lawrence Seaway: A Waterway for Trade',
   'Grade 5 Social Studies strand: the St. Lawrence Seaway is a system of canals and locks that allows large ships to travel between the Atlantic Ocean and the Great Lakes, supporting trade across central Canada.',
   [('What does the St. Lawrence Seaway allow large ships to do?', ['Travel between the Atlantic Ocean and the Great Lakes', 'Travel only within a single small lake', 'Sail directly across the Pacific Ocean', 'This concept has no connection to Canadian geography'], 0),
    ('What are locks used for along the St. Lawrence Seaway?', ['Raising or lowering ships to different water levels', 'Preventing any ships from ever passing through', 'Measuring the temperature of the water', 'This concept has no connection to the Seaway'], 0),
    ('Why is the St. Lawrence Seaway important for trade in central Canada?', ['It allows goods to be shipped efficiently between the ocean and inland regions', 'It has no connection to how goods are transported', 'This concept has no relevance to social studies', 'Trade in central Canada never relies on waterways'], 0),
    ('Which body of water system does the St. Lawrence Seaway connect to the Atlantic Ocean?', ['The Great Lakes', 'The Arctic Ocean', 'The Pacific Ocean', 'The Hudson Bay only'], 0),
    ('Why might building canals and locks have been necessary to create the Seaway?', ['They help ships navigate around natural obstacles like rapids and changes in water level', 'Canals and locks have no purpose along a shipping route', 'This concept has no connection to Canadian geography', 'Ships never need help navigating water level changes'], 0)]),
]),
day(167, [
L('Grammar: Punctuating Titles of Books, Movies, and Songs',
  'Grade 5 Language strand: titles of longer works, such as books and movies, are usually italicized or underlined, while titles of shorter works, such as songs, poems, and articles, are placed in quotation marks.',
  [('How are titles of longer works, like books or movies, usually punctuated?', ['Italicized or underlined', 'Placed in parentheses', 'Written entirely in lowercase letters', 'Never given any special punctuation'], 0),
   ('How are titles of shorter works, like songs or poems, usually punctuated?', ['Placed in quotation marks', 'Italicized only', 'Written in all capital letters', 'Never punctuated in any way'], 0),
   ('Which of these is an example of a longer work that would typically be italicized?', ['A novel', 'A single song', 'A short poem', 'A magazine article'], 0),
   ('Which of these is an example of a shorter work that would typically use quotation marks?', ['A song title', 'A novel title', 'A movie title', 'A television series title'], 0),
   ('Why might consistent title punctuation matter in formal writing?', ['It helps readers quickly recognize what kind of work is being referenced', 'Title punctuation has no effect on how readers understand a text', 'This concept has no connection to grammar', 'Titles should never be punctuated differently from regular words'], 0)]),
M('Geometry: Constructing Circles Using a Compass',
  'Grade 5 Math strand: a compass is a tool used to construct an accurate circle by keeping one point fixed at the centre while the pencil point traces a curve at a constant distance, the radius.',
  [('What tool is commonly used to construct an accurate circle?', ['A compass', 'A protractor', 'A ruler alone', 'A calculator'], 0),
   ('What stays fixed when using a compass to draw a circle?', ['The centre point', 'The pencil point tracing the curve', 'The radius changes constantly while drawing', 'Nothing stays fixed while drawing a circle'], 0),
   ('What does the distance between the compass point and the pencil represent?', ['The radius of the circle', 'The diameter of the circle', 'The circumference of the circle', 'The area of the circle'], 0),
   ('Why is a compass useful for constructing a circle instead of drawing freehand?', ['It helps ensure every point on the circle is exactly the same distance from the centre', 'A compass makes it impossible to draw an accurate circle', 'This concept has no connection to geometry', 'Freehand drawing is always more accurate than using a compass'], 0),
   ('If you widen the opening of a compass before drawing, what happens to the circle?', ['The circle becomes larger, with a bigger radius', 'The circle becomes smaller, with a smaller radius', 'The circle stays exactly the same size', 'This concept has no connection to constructing circles'], 0)]),
Sc('The Nitrogen Cycle: How Nitrogen Moves Through Ecosystems',
   'Grade 5 Science strand: the nitrogen cycle describes how nitrogen moves between the atmosphere, soil, and living things, with bacteria converting nitrogen gas into forms that plants can use to grow.',
   [('What does the nitrogen cycle describe?', ['How nitrogen moves between the atmosphere, soil, and living things', 'How water moves between the ocean and the atmosphere', 'How rocks are formed underground over time', 'This concept has no connection to ecosystems'], 0),
    ('What role do certain bacteria play in the nitrogen cycle?', ['They convert nitrogen gas into forms that plants can use', 'They remove all nitrogen permanently from an ecosystem', 'Bacteria have no role in the nitrogen cycle at all', 'This concept has no relevance to science'], 0),
    ('Why do plants need nitrogen in a usable form?', ['Nitrogen helps plants grow and build important compounds', 'Plants never require nitrogen in any form', 'This concept has no connection to plant growth', 'Nitrogen is harmful to all plants in every form'], 0),
    ('Where is most of the nitrogen on Earth found?', ['In the atmosphere, as nitrogen gas', 'Only in ocean water', 'Only inside rocks deep underground', 'This concept has no connection to Earth science'], 0),
    ('Why is the nitrogen cycle considered important for ecosystems?', ['It helps ensure nitrogen is available in forms living things can use to grow', 'The nitrogen cycle has no effect on any ecosystem', 'This concept has no relevance to science', 'Nitrogen never needs to move through an ecosystem'], 0)]),
SS('Canadian Passports and International Travel',
   'Grade 5 Social Studies strand: a Canadian passport is an official government document that confirms a persons identity and citizenship, allowing them to travel internationally and receive consular assistance abroad.',
   [('What does a Canadian passport confirm about its holder?', ['Their identity and citizenship', 'Their favourite hobbies', 'Their school grades', 'Their employment history'], 0),
    ('Why might someone need a passport to travel internationally?', ['Many countries require official proof of identity and citizenship to enter', 'Passports are never required to travel between countries', 'This concept has no connection to international travel', 'A passport only allows travel within ones own country'], 0),
    ('Which level of government issues Canadian passports?', ['The federal government', 'Only municipal governments', 'Only provincial governments', 'A private international company'], 0),
    ('What might a Canadian embassy help provide to a passport holder travelling abroad?', ['Consular assistance if they encounter an emergency', 'A replacement for their home address', 'A new nationality while abroad', 'This concept has no connection to international travel'], 0),
    ('Why might a passport be considered an important form of identification?', ['It is widely recognized internationally as proof of identity and citizenship', 'A passport has no value as identification of any kind', 'This concept has no relevance to social studies', 'Passports are only used within a persons home country'], 0)]),
]),
day(168, [
L('Figurative Language: Puns and Wordplay',
  'Grade 5 Language strand: a pun is a form of wordplay that uses a words multiple meanings or similar-sounding words to create a humorous or clever effect.',
  [('What is a pun?', ['A form of wordplay using a words multiple meanings or similar sounds for humour', 'A word with only one possible meaning', 'A rule for capitalizing proper nouns', 'A type of punctuation mark'], 0),
   ('Which of these is an example of a pun?', ['I used to be a baker, but I could not make enough dough.', 'The sun rose over the quiet hills.', 'She ran quickly to catch the bus.', 'The tall building had many windows.'], 0),
   ('Why might a pun rely on a word having more than one meaning?', ['The double meaning creates the surprising or humorous connection', 'Puns never depend on a words multiple meanings', 'This concept has no connection to figurative language', 'A pun always uses only one clear meaning of a word'], 0),
   ('Why might an author use wordplay like a pun in a piece of writing?', ['To add humour or cleverness that engages the reader', 'Wordplay always makes writing more confusing and unclear', 'This concept has no relevance to figurative language', 'Puns are never intended to be humorous'], 0),
   ('What skill helps a reader understand and enjoy a pun?', ['Recognizing multiple meanings or similar sounds in words', 'Ignoring the meaning of every word in a sentence', 'This concept has no connection to reading', 'Puns can be understood without any knowledge of word meanings'], 0)]),
M('Geometry: Composite Transformations — Combining Translations, Reflections, and Rotations',
  'Grade 5 Math strand: a composite transformation applies more than one transformation, such as a translation followed by a reflection, to move a shape from its original position to a final position.',
  [('What is a composite transformation?', ['Applying more than one transformation to a shape', 'Applying only a single transformation to a shape', 'Removing a shape from a grid entirely', 'This concept has no connection to geometry'], 0),
   ('Which of these could be part of a composite transformation?', ['A translation followed by a reflection', 'Colouring a shape a different colour', 'Measuring the perimeter of a shape', 'Naming the vertices of a shape'], 0),
   ('What generally stays the same about a shape after a composite transformation of translations, reflections, and rotations?', ['Its size and shape', 'Its exact position on the grid', 'Its colour changes automatically', 'This concept has no connection to transformations'], 0),
   ('Why might a composite transformation be used instead of a single transformation?', ['It can move a shape through several steps to reach a specific final position', 'A composite transformation can never move a shape anywhere new', 'This concept has no relevance to geometry', 'Using more than one transformation always changes the size of a shape'], 0),
   ('If a shape is translated and then reflected, in what order do the transformations occur?', ['The translation happens first, followed by the reflection', 'The reflection always happens before the translation', 'Both transformations must happen at the exact same instant', 'This concept has no connection to composite transformations'], 0)]),
Sc('How Helicopters Fly: Rotors, Lift, and Control',
   'Grade 5 Science strand: a helicopter generates lift using spinning rotor blades shaped like airfoils, and pilots control direction and altitude by changing the angle and speed of the rotors.',
   [('What does a helicopter use to generate lift?', ['Spinning rotor blades', 'Fixed wings like an airplane', 'A large balloon filled with helium', 'This concept has no connection to flight'], 0),
    ('What shape are helicopter rotor blades designed with to help create lift?', ['An airfoil shape', 'A perfectly flat rectangle', 'A hollow sphere', 'This concept has no connection to how helicopters fly'], 0),
    ('How is a helicopter different from an airplane in how it generates lift?', ['A helicopter uses spinning rotors, while an airplane relies on fixed wings and forward motion', 'A helicopter and an airplane generate lift in exactly the same way', 'A helicopter never needs lift to fly', 'This concept has no relevance to science'], 0),
    ('How might a pilot control a helicopters direction?', ['By changing the angle and speed of the rotor blades', 'Direction can never be controlled once a helicopter is in the air', 'By changing the colour of the rotor blades', 'This concept has no connection to flight control'], 0),
    ('Why can a helicopter hover in place while an airplane generally cannot?', ['A helicopters rotors can generate lift without needing forward motion', 'Airplanes are always able to hover exactly like helicopters', 'This concept has no connection to how each aircraft flies', 'Helicopters can never remain still in the air'], 0)]),
SS('Canadian Embassies and Consulates: Representing Canada Abroad',
   'Grade 5 Social Studies strand: Canadian embassies and consulates represent Canada in other countries, supporting trade and diplomacy, and providing assistance to Canadian citizens travelling or living abroad.',
   [('What is the main purpose of a Canadian embassy in another country?', ['To represent Canada and support diplomacy and trade', 'To sell Canadian products directly to tourists', 'To manage a foreign countrys internal affairs', 'This concept has no connection to social studies'], 0),
    ('What might a Canadian consulate help provide to a Canadian citizen abroad?', ['Assistance in an emergency, such as a lost passport', 'A new passport from a foreign country', 'Free international transportation home', 'This concept has no connection to Canadian government'], 0),
    ('Why might Canada maintain embassies in many different countries?', ['To build diplomatic relationships and support Canadians and Canadian interests abroad', 'Embassies have no purpose in international relationships', 'This concept has no relevance to social studies', 'Canada only maintains an embassy in one country worldwide'], 0),
    ('What is one way an embassy might support trade between Canada and another country?', ['Helping connect Canadian businesses with opportunities in that country', 'Embassies are never involved in supporting trade', 'This concept has no connection to international relationships', 'Trade always happens with no government involvement whatsoever'], 0),
    ('Why might learning about embassies and consulates help students understand Canadas role internationally?', ['It shows how Canada builds relationships and supports citizens beyond its borders', 'Embassies have no connection to Canadas international role', 'This concept has no relevance to social studies', 'Canada has no diplomatic relationships with other countries'], 0)]),
]),
day(169, [
L('Writing: Writing a Persuasive Poster or Flyer',
  'Grade 5 Language strand: a persuasive poster or flyer uses bold visuals, a clear message, and concise, convincing language to encourage the audience to take a specific action.',
  [('What is the main purpose of a persuasive poster or flyer?', ['To encourage the audience to take a specific action', 'To tell a long, detailed fictional story', 'To present a neutral summary with no opinion', 'To describe an unrelated historical event'], 0),
   ('Why might a persuasive poster use bold visuals?', ['Bold visuals can quickly capture attention and support the message', 'Visuals are never useful on a persuasive poster', 'This concept has no connection to writing', 'A persuasive poster should never include any images'], 0),
   ('Why is concise language important on a persuasive flyer?', ['Readers often view a flyer quickly, so the message must be clear and brief', 'Longer, more detailed language is always more effective on a flyer', 'This concept has no relevance to writing', 'A flyer should always contain as much text as possible'], 0),
   ('What might a persuasive poster include to convince its audience to act?', ['A clear call to action, such as attend or donate', 'A summary with no clear request at all', 'A completely unrelated topic with no connection to the message', 'A list of random, unrelated facts'], 0),
   ('Why might a writer choose strong, positive words on a persuasive poster?', ['Strong, positive language can make the message more convincing and memorable', 'Word choice never affects how persuasive a message feels', 'This concept has no connection to persuasive writing', 'Negative language is always more effective than positive language'], 0)]),
M('Measurement: Introduction to Bearings and Navigation Angles',
  'Grade 5 Math strand: a bearing is a way of describing direction as an angle measured clockwise from north, commonly used in navigation to describe the direction of travel.',
  [('What is a bearing?', ['An angle measured clockwise from north, used to describe direction', 'A measurement of distance between two places', 'A unit used to measure temperature', 'A tool used to measure mass'], 0),
   ('From which direction are bearings typically measured?', ['North', 'South', 'East', 'West'], 0),
   ('In which direction are bearings typically measured around the compass?', ['Clockwise', 'Counterclockwise', 'Bearings are never measured in a consistent direction', 'This concept has no connection to navigation'], 0),
   ('What might a bearing of 090 degrees represent?', ['A direction pointing due east', 'A direction pointing due north', 'A direction pointing due south', 'A direction pointing due west'], 0),
   ('Why might bearings be useful for someone navigating a ship or aircraft?', ['They provide a precise way to describe and follow a specific direction', 'Bearings provide no useful information for navigation', 'This concept has no relevance to measurement', 'Bearings can only be used to measure distances, never directions'], 0)]),
Sc('States of Matter: Plasma — The Fourth State of Matter',
   'Grade 5 Science strand: plasma is a state of matter, along with solid, liquid, and gas, made of charged particles and found in extreme conditions such as lightning, stars, and neon signs.',
   [('Which of these is considered the fourth state of matter, alongside solid, liquid, and gas?', ['Plasma', 'Steam', 'Ice', 'Sand'], 0),
    ('What are plasma particles generally like compared with those of a regular gas?', ['They are charged, unlike the particles in a typical gas', 'They are identical in every way to particles in a typical gas', 'Plasma has no particles at all', 'This concept has no connection to states of matter'], 0),
    ('Which of these is an example of plasma found in nature?', ['Lightning', 'An ice cube', 'A puddle of water', 'A rock'], 0),
    ('Where else, besides lightning, might plasma be found?', ['Inside stars, including the sun', 'Only inside a household refrigerator', 'Only underground in caves', 'This concept has no real-world example'], 0),
    ('Why might scientists consider plasma to be different from the other three common states of matter?', ['Its particles are electrically charged, giving it unique properties', 'Plasma behaves in exactly the same way as a solid', 'This concept has no relevance to science', 'Plasma is never found anywhere in nature or technology'], 0)]),
SS('The Role of Access to Information Laws in Canadian Government',
   'Grade 5 Social Studies strand: access to information laws allow citizens to request records and documents from government institutions, helping keep government actions transparent and accountable to the public.',
   [('What do access to information laws allow citizens to do?', ['Request records and documents from government institutions', 'Vote in a federal election before the age of eighteen', 'Change a law without any government process', 'Run for a seat in the House of Commons at any age'], 0),
    ('What is one goal of access to information laws?', ['Keeping government actions transparent and accountable', 'Preventing citizens from ever learning about government decisions', 'Eliminating all forms of government record keeping', 'This concept has no connection to Canadian government'], 0),
    ('Why might a journalist use access to information laws?', ['To request government records that help inform public reporting', 'Journalists are never allowed to request government information', 'This concept has no relevance to social studies', 'Access to information laws only apply to elected officials'], 0),
    ('Why might transparency be considered important in a democratic government?', ['It helps citizens understand and hold their government accountable', 'Transparency has no connection to how a democracy functions', 'This concept has no relevance to Canadian government', 'Citizens never need to know about government decisions'], 0),
    ('What might happen if a government had no access to information laws at all?', ['Citizens might find it harder to learn about or question government actions', 'Nothing would change since these laws have no real purpose', 'This concept has no connection to social studies', 'Government transparency would automatically increase without these laws'], 0)]),
]),
day(170, [
L('Language Review: Comparative Grammar, Media Literacy, and Oral Communication',
  'Grade 5 Language strand review: students revisit comparative and superlative adjectives, writing a weather report, circular and frame narratives, building words with multiple affixes, and recognizing product placement.',
  [('What does a comparative adjective do?', ['Compares two things', 'Compares three or more things', 'Names a single object', 'Shows an action'], 0),
   ('What is the main purpose of a weather report?', ['To present current conditions and a forecast clearly', 'To tell a fictional story with no factual details', 'To describe an imaginary place with no real information', 'To list random facts unrelated to weather'], 0),
   ('What is a frame narrative?', ['A story placed inside another story', 'A story with no characters at all', 'A story told only through pictures', 'A story with no beginning or ending'], 0),
   ('What does it mean when a word has multiple affixes?', ['It combines more than one prefix or suffix', 'It has no root word at all', 'It uses only capital letters', 'It contains no vowels'], 0),
   ('What is product placement?', ['When a brand or product appears within a movie, show, or video', 'A separate commercial shown between segments of a program', 'A type of poster displayed outside a store', 'A written review of a product in a newspaper'], 0)]),
M('Math Review: Geometry, Algebra, Measurement, and Data',
  'Grade 5 Math strand review: students revisit classifying regular and irregular polygons, multiplying decimals by two-digit whole numbers, the distributive property, estimating mass with a balance scale, and weighted averages.',
  [('What is true about every side and angle of a regular polygon?', ['They are all equal', 'They are always different', 'Only the sides are equal, never the angles', 'A regular polygon has no straight sides'], 0),
   ('What is 2.5 multiplied by 12?', ['30', '25', '32', '20'], 0),
   ('What does the distributive property allow you to do?', ['Multiply a number by a sum by multiplying each addend separately, then adding', 'Divide a number by zero', 'Ignore parentheses in an expression completely', 'Subtract a number from itself'], 0),
   ('What does a balance scale compare?', ['The mass of two objects', 'The colour of two objects', 'The length of two objects', 'The temperature of two objects'], 0),
   ('What does a weighted average do differently from a regular average?', ['It gives different amounts of importance to different values', 'It always gives every value the exact same importance', 'It ignores some values completely', 'It can only be calculated using whole numbers'], 0)]),
Sc('Science Review: Ocean Zones, Machines, Weather, and Ecosystems',
   'Grade 5 Science strand review: students revisit ocean zones, mechanical efficiency, chemical changes in cooking, barometric pressure, and keystone species.',
   [('What is the sunlight zone of the ocean?', ['The uppermost layer where enough light reaches for photosynthesis', 'The deepest, darkest part of the ocean', 'A layer found only in freshwater lakes', 'The layer with the coldest water temperature always'], 0),
    ('Why is no machine perfectly efficient?', ['Some energy is always lost, often to friction or heat', 'Machines always convert all input energy into useful work', 'Efficiency has no connection to energy loss', 'This concept has no relevance to science'], 0),
    ('What gas is produced when baking soda reacts with an acid like vinegar?', ['Carbon dioxide', 'Pure oxygen', 'Helium', 'Nitrogen'], 0),
    ('What does barometric pressure measure?', ['The weight of the air pressing down on Earths surface', 'The temperature of the ocean', 'The speed of the wind only', 'The amount of snowfall in a season'], 0),
    ('What is a keystone species?', ['A species with an unusually large effect on its ecosystem relative to its numbers', 'A species that has no effect on its ecosystem at all', 'The most numerous species in an ecosystem', 'A species that lives only in captivity'], 0)]),
SS('SocialStudies Review: Government Institutions, Trade, and Global Connections',
   'Grade 5 Social Studies strand review: students revisit the federal cabinet, the Speaker of the House of Commons, municipal bylaws, credit unions and cooperatives, and the Canadian Human Rights Commission.',
   [('Who chooses the members of the federal cabinet?', ['The prime minister', 'The Governor General alone', 'The Supreme Court', 'The Chief Electoral Officer'], 0),
    ('Who elects the Speaker of the House of Commons?', ['Other Members of Parliament', 'The Prime Minister alone', 'The Governor General alone', 'The Supreme Court'], 0),
    ('Who passes municipal bylaws?', ['City or town councils', 'The federal Parliament', 'The Supreme Court', 'A private company'], 0),
    ('Who owns a credit union?', ['Its members', 'A single wealthy shareholder', 'Only the federal government', 'A foreign company'], 0),
    ('What does the Canadian Human Rights Commission investigate?', ['Complaints of discrimination in federally regulated workplaces and services', 'The results of provincial sports competitions', 'The design of Canadian currency', 'International trade agreements'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_161_170)
    append_to(5, g5_161_170)
