#!/usr/bin/env python3
"""Grade 5, Days 121-130 -- extends Grade 5 from 120 to 130 days. Modeled
exactly on gen_grade5_days111_120.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-120
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: relative
pronouns, perfect verb tenses, writing an advertisement, suspense and
cliffhangers, collective nouns, interjections, climax and resolution,
public service announcements, and eponyms for Language; permutations,
currency exchange rates, simple inequalities on a number line, rotations,
Roman numerals, speed/distance/time, loans and repayment, complementary
and supplementary angles, and probability expressed as a fraction,
decimal, and percent for Math; geothermal and biomass power, the northern
lights, Newtons first law of motion, types of precipitation, the human
brain, nocturnal animals, the life cycle of a star, seed dispersal, and
thermal conductors and insulators for Science; and the role of the Prime
Minister, the House of Commons, the Numbered Treaties, the Great Canadian
Flag Debate of 1964, the Persons Case, Indigenous Elders and Knowledge
Keepers, the Ombudsman, trade surplus/deficit, and Canada and the Olympic
Games for Social Studies -- none of those exact ideas appear in Days
1-120. Day 130 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch. No embedded ASCII
double-quote characters are used anywhere in question/summary/option
text; apostrophes are dropped entirely, matching the rest of Grade 5
Days 101-120 (e.g. "Canadas" not "Canada's", "governments" not
"government's").
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


g5_121_130 = [
day(121, [
L('Grammar: Relative Pronouns and Relative Clauses',
  'Grade 5 Language strand: relative pronouns like who, which, and that introduce relative clauses, which add extra information about a noun in a sentence.',
  [('Which word is the relative pronoun in the sentence The book that I borrowed was excellent?', ['That', 'Book', 'Borrowed', 'Excellent'], 0),
   ('Which relative pronoun usually refers to a person?', ['Who', 'Which', 'Where', 'When'], 0),
   ('Which relative pronoun usually refers to a thing or object?', ['Which', 'Who', 'Whom', 'Why'], 0),
   ('In the sentence The dog, which was very old, slept all day, what does the clause which was very old describe?', ['The dog', 'The sleeping', 'The day', 'A concept unrelated to the sentence'], 0),
   ('Why do writers use relative clauses?', ['To add extra descriptive detail about a noun without starting a new sentence', 'To end a sentence abruptly', 'To remove information from a sentence', 'To replace all nouns with pronouns'], 0)]),
M('Data Management: Permutations — Counting Ordered Outcomes',
  'Grade 5 Math strand: a permutation counts the number of ways items can be arranged in order, meaning that changing the order of the same items creates a different permutation.',
  [('What does a permutation count?', ['The number of ordered arrangements of items', 'The number of ways to group items when order does not matter', 'A single fixed outcome', 'A type of fraction'], 0),
   ('In permutations, does arranging A then B count differently from arranging B then A?', ['Yes, they are different permutations', 'No, they are always the same', 'Only sometimes', 'It depends on the colour'], 0),
   ('How many ways can 3 different books be arranged in order on a shelf?', ['6', '3', '9', '1'], 0),
   ('How is a permutation different from a combination?', ['A permutation considers order, while a combination does not', 'A permutation never considers order', 'A combination always considers order', 'They are exactly the same thing'], 0),
   ('Which situation involves finding a permutation?', ['Assigning first, second, and third place in a race', 'Choosing 3 books to bring on a trip from a shelf of 5', 'Selecting a committee of 2 from 4 people', 'Picking 2 toppings from 4 options'], 0)]),
Sc('Renewable Energy in Focus: Geothermal and Biomass Power',
   'Grade 5 Science strand: geothermal power uses heat stored deep within the Earth, while biomass power burns organic material like wood waste or crops, both offering renewable alternatives to fossil fuels.',
   [('What does geothermal power use as its energy source?', ['Heat stored deep within the Earth', 'Sunlight', 'Wind', 'Ocean waves'], 0),
    ('What is biomass?', ['Organic material, such as wood waste or crops, used to produce energy', 'A type of metal', 'A form of solar panel', 'A kind of fossil fuel'], 0),
    ('Why is geothermal energy considered renewable?', ['The heat within the Earth is naturally replenished and will not run out', 'It requires burning coal', 'It only works during the day', 'It cannot be reused'], 0),
    ('Which of these could be used as a biomass fuel?', ['Wood waste or crop residue', 'Sunlight', 'Wind', 'Uranium'], 0),
    ('What is one advantage geothermal and biomass power share with solar, wind, and hydro power?', ['They all produce energy without permanently depleting fossil fuels', 'They only work underground', 'They require no energy source at all', 'They can never be used to generate electricity'], 0)]),
SS('The Role of the Prime Minister in Canadas Government',
   'Grade 5 Social Studies strand: the Prime Minister is the leader of the federal government, chosen from the political party with the most seats in the House of Commons, and oversees the countrys ministers and major policy decisions.',
   [('What is the Prime Ministers main role in Canadas government?', ['Leading the federal government', 'Representing the monarch ceremonially', 'Leading a provincial government', 'Serving as a judge on the Supreme Court'], 0),
    ('How does someone typically become Prime Minister of Canada?', ['By leading the political party with the most seats in the House of Commons', 'By being appointed directly by a foreign government', 'By winning a national popularity contest with no election', 'By inheriting the position'], 0),
    ('Who does the Prime Minister generally choose to lead different government departments?', ['Ministers', 'Senators only', 'Lieutenant Governors', 'Mayors'], 0),
    ('Why is the Prime Ministers role considered central to federal decision-making?', ['The Prime Minister leads Cabinet and helps set major national policy directions', 'The Prime Minister has no influence over government decisions', 'The role is purely ceremonial with no responsibilities', 'The Prime Minister only manages provincial affairs'], 0),
    ('How does the Prime Ministers role differ from that of the Governor General?', ['The Prime Minister leads government policy, while the Governor General performs ceremonial and constitutional duties', 'They perform identical duties', 'The Governor General leads government policy while the Prime Minister is ceremonial', 'Neither role has any real function'], 0)]),
]),
day(122, [
L('Grammar: Perfect Verb Tenses — Present Perfect and Past Perfect',
  'Grade 5 Language strand: the present perfect tense (has or have plus a past participle) describes an action connecting the past to the present, while the past perfect tense (had plus a past participle) describes an action completed before another past action.',
  [('Which sentence uses the present perfect tense?', ['She has finished her homework.', 'She finishes her homework.', 'She will finish her homework.', 'She finished her homework yesterday.'], 0),
   ('What helping verb often forms the present perfect tense?', ['Has or have', 'Will', 'Did', 'Is'], 0),
   ('Which sentence uses the past perfect tense correctly?', ['She had already left when I arrived.', 'She has already left when I arrived.', 'She leaves already when I arrived.', 'She will have left when I arrived yesterday.'], 0),
   ('What does the past perfect tense show?', ['An action completed before another action in the past', 'An action happening right now', 'An action that will happen in the future', 'An action with no connection to time'], 0),
   ('Why might a writer choose the present perfect tense instead of the simple past tense?', ['To show an action that connects the past to the present moment', 'Present perfect tense never connects to the present', 'This concept has no connection to grammar', 'The simple past and present perfect always mean the exact same thing'], 0)]),
M('Financial Literacy: Understanding Currency Exchange Rates',
  'Grade 5 Math strand: an exchange rate shows how much one countrys currency is worth compared to another, allowing travellers and businesses to convert amounts between currencies like Canadian and American dollars.',
  [('What does a currency exchange rate show?', ['How much one countrys currency is worth compared to another', 'The total population of a country', 'A type of tax rate', 'A single fixed price for every item'], 0),
   ('If 1 US dollar equals 1.35 Canadian dollars, how many Canadian dollars would 10 US dollars be worth?', ['13.50 Canadian dollars', '10 Canadian dollars', '1.35 Canadian dollars', '135 Canadian dollars'], 0),
   ('Why might a traveller need to check the exchange rate before a trip?', ['To understand how much their money is worth in another currency', 'Exchange rates never affect travel', 'This concept has no connection to money', 'Exchange rates only apply to businesses'], 0),
   ('Do exchange rates stay exactly the same every single day?', ['No, exchange rates can change daily', 'Yes, they never change', 'A concept unrelated to currency', 'Exchange rates only change once a century'], 0),
   ('Why is it useful for businesses that trade internationally to understand exchange rates?', ['It helps them calculate accurate costs and prices when buying or selling across borders', 'Exchange rates never affect international business', 'This concept has no relevance to financial literacy', 'Businesses never need to convert currency'], 0)]),
Sc('The Northern Lights — A Glow in the Night Sky',
   'Grade 5 Science strand: the northern lights, or aurora borealis, are colourful displays of light in the night sky caused by charged particles from the sun colliding with gases in Earths atmosphere, often visible in northern Canada.',
   [('What causes the northern lights?', ['Charged particles from the sun colliding with gases in Earths atmosphere', 'Reflections from the Moon', 'Light from distant stars only', 'City streetlights'], 0),
    ('What is another name for the northern lights?', ['Aurora borealis', 'Aurora australis', 'The Milky Way', 'A solar eclipse'], 0),
    ('Where in Canada are the northern lights most commonly visible?', ['In northern regions, such as the territories', 'Only in southern Ontario', 'Only over the ocean', 'Nowhere in Canada'], 0),
    ('What gases in the atmosphere help create the colours seen in the northern lights?', ['Gases such as oxygen and nitrogen', 'Only carbon dioxide', 'Only water vapour', 'Helium alone'], 0),
    ('Why do the northern lights appear more often in far northern regions of Earth?', ['Earths magnetic field guides charged particles toward the polar regions', 'The northern lights never appear near the poles', 'This concept has no relevance to science', 'Charged particles avoid the polar regions entirely'], 0)]),
SS('The House of Commons and How Laws Are Debated',
   'Grade 5 Social Studies strand: the House of Commons is the elected lower house of Canadas Parliament, where Members of Parliament debate, amend, and vote on proposed laws called bills.',
   [('What is the House of Commons?', ['The elected lower house of Canadas Parliament', 'An appointed upper house', 'A provincial legislature', 'A municipal council'], 0),
    ('Who sits in the House of Commons?', ['Elected Members of Parliament', 'Appointed senators only', 'Judges only', 'Mayors of every city'], 0),
    ('What is a proposed law called before it is passed?', ['A bill', 'A treaty', 'A referendum', 'A decree'], 0),
    ('What might Members of Parliament do to a bill before voting on it?', ['Debate and propose amendments to it', 'Ignore it completely', 'Destroy it immediately', 'Refuse to discuss it at all'], 0),
    ('Why is debate an important part of how the House of Commons works?', ['It allows different viewpoints to be considered before a law is passed', 'Debate never influences a final law', 'This concept has no relevance to Canadian government', 'Bills are never discussed before becoming law'], 0)]),
]),
day(123, [
L('Writing: Writing an Advertisement',
  'Grade 5 Language strand: an effective advertisement uses persuasive language, a catchy slogan, and a clear call to action to convince an audience to buy a product or support an idea.',
  [('What is the purpose of an advertisement?', ['To persuade an audience to buy a product or support an idea', 'To tell a neutral news story', 'To record historical events', 'To provide a dictionary definition'], 0),
   ('What is a slogan?', ['A short, catchy phrase that helps people remember a product or idea', 'A long paragraph of facts', 'A type of punctuation mark', 'A formal citation'], 0),
   ('What is a call to action in an advertisement?', ['A statement urging the audience to do something, such as buy or visit', 'A summary of unrelated facts', 'A question with no purpose', 'A footnote citing a source'], 0),
   ('Why might an advertisement use persuasive language?', ['To convince the audience that a product or idea is worth choosing', 'Persuasive language never influences an audience', 'This concept has no connection to writing', 'Advertisements never try to convince anyone'], 0),
   ('Which is an example of persuasive language in an advertisement?', ['This amazing product will change your life.', 'The product is grey and rectangular.', 'The item was manufactured in a factory.', 'The store opens at nine in the morning.'], 0)]),
M('Algebra: Introducing Simple Inequalities on a Number Line',
  'Grade 5 Math strand: an inequality, such as x is greater than 3, compares two values instead of showing them as equal, and can be represented as a shaded region on a number line.',
  [('What symbol means greater than?', ['>', '<', '=', '÷'], 0),
   ('What symbol means less than?', ['<', '>', '=', '+'], 0),
   ('On a number line, how would you show x is greater than 3?', ['Shading the line to the right of 3 with an open circle at 3', 'Shading the entire number line', 'Shading only the number 3', 'Shading to the left of 3'], 0),
   ('Which value would make the inequality x < 5 true?', ['3', '5', '6', '10'], 0),
   ('Why might an inequality be useful compared to an equation?', ['It can describe a whole range of possible values, not just one exact number', 'Inequalities never describe a range of values', 'This concept has no connection to algebra', 'An inequality always has exactly one solution like an equation'], 0)]),
Sc('Newtons First Law of Motion — Inertia in Everyday Life',
   'Grade 5 Science strand: Newtons first law explains that objects stay at rest or in motion unless acted on by a force, providing a foundation for understanding how forces like friction and gravity affect movement.',
   [('According to Newtons first law, what happens to an object at rest unless a force acts on it?', ['It stays at rest', 'It always starts moving on its own', 'It disappears', 'It doubles in size'], 0),
    ('According to Newtons first law, what happens to a moving object unless a force acts on it?', ['It continues moving at the same speed and direction', 'It immediately stops', 'It changes into a different object', 'It moves backward automatically'], 0),
    ('What do we call an objects tendency to resist a change in motion?', ['Inertia', 'Gravity', 'Friction', 'Velocity'], 0),
    ('Why does a rolling ball eventually stop on a flat surface?', ['Friction acts as a force that slows it down', 'No force ever acts on the ball', 'The ball loses its shape', 'Balls always stop after exactly one second'], 0),
    ('Why is understanding Newtons first law useful when thinking about seatbelts in a car?', ['Passengers keep moving forward when a car suddenly stops, unless a force like a seatbelt acts on them', 'Seatbelts have no connection to motion', 'This concept has no relevance to physical science', 'A stopped car has no effect on passengers inside it'], 0)]),
SS('The Numbered Treaties in Canadian History',
   'Grade 5 Social Studies strand: the Numbered Treaties were a series of agreements made between the Crown and First Nations between 1871 and 1921, outlining land use, rights, and promises that continue to affect Canadian law today.',
   [('What were the Numbered Treaties?', ['A series of agreements made between the Crown and First Nations', 'A set of provincial tax laws', 'A type of modern trade agreement', 'A collection of national holidays'], 0),
    ('Roughly during what period were the Numbered Treaties signed?', ['Between 1871 and 1921', 'In the year 2020', 'Before the year 1500', 'Only within the last five years'], 0),
    ('What did the Numbered Treaties often address?', ['Land use and rights between the Crown and First Nations', 'International trade tariffs', 'Provincial voting districts', 'National holidays'], 0),
    ('Why do the Numbered Treaties continue to affect Canadian law today?', ['Their terms and promises still influence rights and land agreements in the present', 'They were cancelled the year after being signed', 'They have no legal significance today', 'They were never written down'], 0),
    ('Why is it important for students to learn about the Numbered Treaties?', ['They help explain the historical relationship between First Nations and the Canadian government', 'They have no connection to Canadian history', 'This concept has no relevance to social studies', 'The treaties only affected people outside of Canada'], 0)]),
]),
day(124, [
L('Reading: Understanding Suspense and Cliffhangers',
  'Grade 5 Language strand: suspense is a feeling of tension and anticipation an author creates about what will happen next, often ending a chapter with a cliffhanger that leaves an important question unanswered.',
  [('What is suspense in a story?', ['A feeling of tension and anticipation about what will happen next', 'A summary of the entire plot', 'A type of punctuation', 'A rhyme scheme'], 0),
   ('What is a cliffhanger?', ['An ending that leaves an important question unanswered', 'A chapter that reveals every answer immediately', 'A type of nonfiction text feature', 'A grammar rule'], 0),
   ('Why might an author end a chapter with a cliffhanger?', ['To make readers want to keep reading to find out what happens next', 'Cliffhangers never affect a readers interest', 'This concept has no connection to reading', 'Authors never use cliffhangers on purpose'], 0),
   ('Which of these techniques might an author use to build suspense?', ['Withholding key information from the reader until later', 'Revealing the ending in the first sentence', 'Avoiding any conflict in the story', 'Summarizing the whole plot immediately'], 0),
   ('Why might pacing, such as short sentences, help build suspense in a scene?', ['Quick, short sentences can create a sense of urgency and tension', 'Pacing never affects how a reader feels about a scene', 'This concept has no relevance to reading', 'Long sentences always create more suspense than short ones'], 0)]),
M('Geometry: Transformations — Rotations and Angles of Turn',
  'Grade 5 Math strand: a rotation turns a shape around a fixed point by a certain angle, such as 90 or 180 degrees, without changing its size or shape.',
  [('What does a rotation do to a shape?', ['Turns it around a fixed point', 'Slides it in a straight line', 'Flips it over a line', 'Makes it larger'], 0),
   ('What do we call the fixed point a shape rotates around?', ['The centre of rotation', 'The vertex', 'The perimeter', 'The diameter'], 0),
   ('If a shape is rotated 180 degrees, how does it typically appear compared to the original?', ['Upside down or facing the opposite direction', 'Exactly the same as a 90-degree rotation', 'Twice the original size', 'Half the original size'], 0),
   ('Does a rotation change the size of a shape?', ['No, the size stays the same', 'Yes, it always doubles the size', 'Yes, it always shrinks the shape', 'Rotation removes the shape entirely'], 0),
   ('Why might a rotation of 360 degrees return a shape to its original position?', ['A full rotation completes an entire circle back to the starting angle', 'A 360-degree rotation always changes the shapes size', 'This concept has no connection to geometry', 'Rotating a shape never returns it to its original position'], 0)]),
Sc('Types of Precipitation — Rain, Snow, Sleet, and Hail',
   'Grade 5 Science strand: precipitation is water that falls from clouds to Earths surface in forms such as rain, snow, sleet, and hail, depending on temperature conditions in the atmosphere.',
   [('What is precipitation?', ['Water that falls from clouds to Earths surface', 'A type of rock', 'A form of soil', 'A kind of wind'], 0),
    ('Which of these is a form of precipitation?', ['Snow', 'Sunlight', 'Wind', 'Fog only'], 0),
    ('What weather condition typically causes precipitation to fall as snow instead of rain?', ['Cold temperatures throughout the atmosphere', 'Only warm temperatures near the ground', 'No temperature ever affects precipitation type', 'Only wind speed'], 0),
    ('What is sleet?', ['Partially frozen rain that falls as small ice pellets', 'A type of cloud', 'A form of lightning', 'A type of soil'], 0),
    ('Why might scientists study different types of precipitation?', ['To help predict weather and understand its effects on the environment', 'Precipitation has no connection to weather', 'This concept has no relevance to Earth science', 'Precipitation never changes based on temperature'], 0)]),
SS('The Great Canadian Flag Debate of 1964',
   'Grade 5 Social Studies strand: the Great Flag Debate of 1964 was a lengthy parliamentary discussion over adopting a new, distinctly Canadian flag, which resulted in the maple leaf design being officially raised in 1965.',
   [('What was the Great Flag Debate of 1964 about?', ['Whether Canada should adopt a new, distinctly Canadian flag', 'A debate about provincial borders', 'A discussion about national holidays', 'An argument over currency design'], 0),
    ('What design was chosen as a result of the flag debate?', ['The maple leaf flag', 'The Union Jack', 'A flag with only stripes', 'A flag featuring a beaver'], 0),
    ('In what year was Canadas new flag officially raised?', ['1965', '1867', '1920', '2000'], 0),
    ('Why might some Canadians have wanted a new flag distinct from Britains Union Jack?', ['To reflect a unique Canadian identity separate from British symbols', 'They wanted no flag at all', 'Canada never had a flag before 1965', 'Canadians were required to have the same flag as Britain'], 0),
    ('Why is the flag debate considered an important moment in Canadian history?', ['It reflected growing Canadian independence and national identity', 'It had no impact on Canadian identity', 'This concept has no relevance to social studies', 'The debate ended without any flag being chosen'], 0)]),
]),
day(125, [
L('Vocabulary: Collective Nouns',
  'Grade 5 Language strand: a collective noun names a group of people, animals, or things treated as a single unit, such as a flock of birds or a team of players.',
  [('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that names only one person', 'A word that shows possession', 'A type of adverb'], 0),
   ('Which of these is a collective noun?', ['Flock', 'Bird', 'Fly', 'Feather'], 0),
   ('What is the collective noun for a group of wolves?', ['A pack', 'A herd', 'A school', 'A colony'], 0),
   ('What is the collective noun for a group of fish?', ['A school', 'A pack', 'A flock', 'A pride'], 0),
   ('Why might writers use collective nouns instead of listing every individual member of a group?', ['It allows them to refer to a whole group efficiently and clearly', 'Collective nouns never refer to groups', 'This concept has no connection to vocabulary', 'Collective nouns always confuse a reader'], 0)]),
M('Number Sense: Roman Numerals',
  'Grade 5 Math strand: the Roman numeral system uses letters such as I, V, X, L, and C to represent numbers, combining and arranging them according to addition and subtraction rules.',
  [('What number does the Roman numeral X represent?', ['10', '5', '1', '50'], 0),
   ('What number does the Roman numeral V represent?', ['5', '10', '1', '100'], 0),
   ('How is the number 4 written in Roman numerals?', ['IV', 'IIII', 'VI', 'IX'], 0),
   ('What does it mean when a smaller Roman numeral appears before a larger one, as in IX?', ['Subtract the smaller value from the larger one', 'Add the smaller value to the larger one', 'Multiply the two values', 'Ignore the smaller value'], 0),
   ('Where might you still see Roman numerals used today?', ['On clock faces or to number movie sequels', 'Only in ancient Rome', 'Never in modern life', 'Only in mathematics textbooks about fractions'], 0)]),
Sc('The Human Brain — Control Centre of the Body',
   'Grade 5 Science strand: the brain is the control centre of the nervous system, coordinating thought, memory, movement, and the bodys responses to the environment.',
   [('What is the brain often described as?', ['The control centre of the nervous system', 'A type of muscle', 'A digestive organ', 'A part of the skeletal system'], 0),
    ('What is one important function of the brain?', ['Coordinating thought and memory', 'Pumping blood through the body', 'Digesting food', 'Filtering waste from blood'], 0),
    ('What protects the brain from injury?', ['The skull', 'The ribs', 'The spine alone', 'The skin'], 0),
    ('Why might scientists describe the brain as working closely with the rest of the nervous system?', ['The brain sends and receives signals through nerves to control the bodys actions', 'The brain never communicates with the rest of the body', 'This concept has no relevance to science', 'The brain and nervous system are completely unrelated'], 0),
    ('Why is protecting the brain, such as by wearing a helmet, considered important?', ['The brain controls essential functions and injury can seriously affect the whole body', 'The brain has no important functions', 'This concept has no connection to science', 'Helmets have no effect on protecting the brain'], 0)]),
SS('The Persons Case and Womens Rights in Canada',
   'Grade 5 Social Studies strand: the Persons Case of 1929 was a landmark legal decision that recognized women as persons eligible to be appointed to the Senate, marking an important step in the history of womens rights in Canada.',
   [('What did the Persons Case of 1929 decide?', ['That women were legally recognized as persons eligible for Senate appointment', 'That women could no longer vote', 'That only men could hold government positions', 'That Canada would adopt a new flag'], 0),
    ('Roughly when did the Persons Case take place?', ['1929', '1867', '2000', '1600'], 0),
    ('Why was the Persons Case an important step for womens rights in Canada?', ['It helped open the door for women to hold positions of political power', 'It reduced the rights women previously held', 'It had no effect on womens rights', 'It only applied to women outside of Canada'], 0),
    ('What group of women is often credited with bringing forward the case that became known as the Persons Case?', ['The Famous Five', 'The Group of Seven', 'The Fathers of Confederation', 'The United Empire Loyalists'], 0),
    ('Why do historians consider the Persons Case a milestone in Canadian legal history?', ['It changed how the law defined who could participate fully in government', 'It had no lasting legal impact', 'This concept has no relevance to social studies', 'It only affected a single individual with no broader significance'], 0)]),
]),
day(126, [
L('Grammar: Interjections and Their Punctuation',
  'Grade 5 Language strand: an interjection is a word or phrase that expresses strong emotion, such as wow or ouch, and is often followed by an exclamation mark or set off with a comma.',
  [('What is an interjection?', ['A word or phrase expressing strong emotion', 'A word that joins two clauses', 'A word that shows possession', 'A type of preposition'], 0),
   ('Which of these is an example of an interjection?', ['Wow', 'Running', 'Quickly', 'Table'], 0),
   ('What punctuation mark often follows a strong interjection?', ['An exclamation mark', 'A question mark', 'A colon', 'A hyphen'], 0),
   ('How might a mild interjection be punctuated within a sentence, as in Well, I suppose so?', ['Set off with a comma', 'Always followed by a period only', 'Never punctuated at all', 'Always written in capital letters'], 0),
   ('Why do writers use interjections in dialogue?', ['To show a characters strong feeling or reaction', 'Interjections never show emotion', 'This concept has no connection to grammar', 'Interjections always replace the main verb of a sentence'], 0)]),
M('Measurement: Speed, Distance, and Time Relationships',
  'Grade 5 Math strand: speed describes how fast an object moves, calculated by dividing the distance travelled by the time it took, such as kilometres per hour.',
  [('How is speed calculated?', ['Distance divided by time', 'Distance multiplied by time', 'Time divided by distance', 'Distance added to time'], 0),
   ('If a car travels 120 kilometres in 2 hours, what is its average speed?', ['60 kilometres per hour', '120 kilometres per hour', '240 kilometres per hour', '2 kilometres per hour'], 0),
   ('What unit might be used to describe the speed of a cyclist?', ['Kilometres per hour', 'Kilograms', 'Litres', 'Square metres'], 0),
   ('If you know the speed and time of a trip, how can you find the distance travelled?', ['Multiply speed by time', 'Divide speed by time', 'Subtract time from speed', 'Add speed and time'], 0),
   ('Why is understanding the relationship between speed, distance, and time useful in everyday life?', ['It helps estimate how long a trip will take or how far you can travel in a given time', 'This relationship never applies to real life', 'This concept has no connection to measurement', 'Speed, distance, and time are always unrelated values'], 0)]),
Sc('Nocturnal Animals and Their Adaptations',
   'Grade 5 Science strand: nocturnal animals are active mainly at night and have adaptations such as strong night vision, sensitive hearing, or a keen sense of smell that help them survive in the dark.',
   [('What does it mean for an animal to be nocturnal?', ['It is active mainly at night', 'It is active mainly during the day', 'It sleeps for an entire year', 'It never sleeps at all'], 0),
    ('Which adaptation might help a nocturnal animal see better in the dark?', ['Large eyes suited for low light', 'Bright feathers', 'A long tail only', 'A loud call'], 0),
    ('Name one example of a nocturnal animal.', ['An owl', 'A robin', 'A butterfly', 'A squirrel active only by day'], 0),
    ('Why might sensitive hearing be a useful adaptation for a nocturnal animal?', ['It helps the animal detect prey or danger when it is too dark to rely on sight alone', 'Sensitive hearing never helps in the dark', 'This concept has no relevance to science', 'Nocturnal animals never need to detect prey or danger'], 0),
    ('Why might being active at night help some animals avoid competition with daytime predators?', ['Being active when other predators sleep can reduce competition for food and safety', 'Nocturnal animals always compete more with daytime animals', 'This concept has no connection to life systems', 'Nighttime activity never provides any survival advantage'], 0)]),
SS('Indigenous Elders and Knowledge Keepers',
   'Grade 5 Social Studies strand: Elders and Knowledge Keepers hold important roles in Indigenous communities, passing down traditional knowledge, language, and teachings to younger generations.',
   [('What role do Elders often play in Indigenous communities?', ['Passing down traditional knowledge and teachings', 'Managing federal taxes', 'Running national elections', 'Building highways'], 0),
    ('What is a Knowledge Keeper?', ['A respected person who preserves and shares traditional knowledge', 'A type of government official', 'A federal tax collector', 'A type of judge'], 0),
    ('Why might traditional teachings be passed down orally by Elders?', ['Oral storytelling has long been an important way to preserve culture and history', 'Oral traditions have no value in preserving culture', 'This concept has no relevance to social studies', 'Written records were always the only method used'], 0),
    ('Why is it important for younger generations to learn from Elders and Knowledge Keepers?', ['It helps preserve cultural knowledge, language, and identity over time', 'Learning from Elders has no benefit to a community', 'This concept has no connection to Indigenous communities', 'Cultural knowledge is never passed between generations'], 0),
    ('How might schools show respect for the role of Elders and Knowledge Keepers?', ['By inviting them to share teachings and knowledge with students', 'By ignoring their contributions entirely', 'By excluding Indigenous perspectives from lessons', 'By replacing their role with textbooks only'], 0)]),
]),
day(127, [
L('Reading: Identifying Climax and Resolution in a Story',
  'Grade 5 Language strand: the climax is the most intense turning point of a story, and the resolution follows it, tying up the main conflict and showing how the story ends.',
  [('What is the climax of a story?', ['The most intense turning point of the story', 'The very first event in the story', 'A list of characters', 'The title of the story'], 0),
   ('What is the resolution of a story?', ['The part that ties up the main conflict and shows how the story ends', 'The very beginning of the story', 'A description of the setting only', 'A list of unrelated facts'], 0),
   ('Does the climax usually happen before or after the resolution?', ['Before the resolution', 'After the resolution', 'At the very beginning of the story', 'They always happen at the exact same moment'], 0),
   ('Why is the climax often considered the most exciting part of a story?', ['It represents the peak of tension before the conflict is resolved', 'The climax is always the least important part of a story', 'This concept has no connection to reading', 'A story never contains a climax'], 0),
   ('Why might identifying the resolution help a reader understand a stories overall meaning?', ['It shows how the conflict was ultimately resolved, revealing the storys outcome', 'The resolution never reveals anything about a story', 'This concept has no relevance to reading comprehension', 'A story never actually reaches a resolution'], 0)]),
M('Financial Literacy: Understanding Loans and Repayment',
  'Grade 5 Math strand: a loan is money borrowed that must be repaid over time, usually with added interest, meaning the total amount repaid is greater than the amount originally borrowed.',
  [('What is a loan?', ['Money borrowed that must be repaid over time', 'Money that never needs to be repaid', 'A type of savings account', 'A form of tax refund'], 0),
   ('Why is the total amount repaid on a loan usually more than the amount borrowed?', ['Interest is added to the amount owed over time', 'Loans never include any interest', 'This concept has no connection to financial literacy', 'The amount repaid is always exactly equal to the amount borrowed'], 0),
   ('If you borrow 100 dollars with 10 percent interest added, how much would you owe in total?', ['110 dollars', '100 dollars', '10 dollars', '90 dollars'], 0),
   ('Why might someone choose to take out a loan rather than wait and save money first?', ['To pay for something important sooner, accepting the cost of added interest', 'Loans always cost less than saving', 'There is never a reason to take out a loan', 'Loans remove the need to ever repay money'], 0),
   ('Why is it important to repay a loan on time?', ['Late or missed payments can add extra costs and affect future borrowing ability', 'Repayment timing never matters for a loan', 'This concept has no relevance to financial literacy', 'Loans disappear automatically if not repaid'], 0)]),
Sc('The Life Cycle of a Star',
   'Grade 5 Science strand: a star forms from a cloud of gas and dust, shines for millions or billions of years by fusing hydrogen, and eventually changes dramatically as it runs out of fuel.',
   [('What does a star form from?', ['A cloud of gas and dust', 'A solid rock', 'Ocean water', 'A comet'], 0),
    ('What process allows a star to shine for a very long time?', ['Fusing hydrogen for energy', 'Burning wood', 'Reflecting sunlight', 'Freezing gases'], 0),
    ('What might eventually happen to a star as it runs out of fuel?', ['It changes dramatically, possibly expanding or collapsing', 'It stays exactly the same forever', 'It turns into a comet', 'It disappears with no other change'], 0),
    ('Why do scientists study the life cycle of stars?', ['To better understand how stars form, change, and eventually end', 'Stars never change over time', 'This concept has no relevance to science', 'Studying stars has no scientific value'], 0),
    ('Why might our sun be considered a star currently in a stable stage of its life cycle?', ['It has been steadily fusing hydrogen for billions of years', 'The sun has already run out of fuel', 'The sun is not actually a star', 'Stars never go through different stages'], 0)]),
SS('The Ombudsman — Helping Citizens with Government Complaints',
   'Grade 5 Social Studies strand: an ombudsman is an independent official who investigates complaints from citizens about unfair treatment by government departments, helping ensure accountability and fairness.',
   [('What does an ombudsman generally do?', ['Investigates citizen complaints about unfair treatment by government', 'Collects federal taxes', 'Leads a political party', 'Manages national parks'], 0),
    ('Why is it important for an ombudsman to be independent from the government they investigate?', ['Independence helps ensure fair and unbiased investigations', 'Independence makes investigations less fair', 'Ombudsmen are never independent', 'This concept has no relevance to government'], 0),
    ('Who might file a complaint with an ombudsman?', ['A citizen who feels they were treated unfairly by a government department', 'Only elected officials', 'Only foreign governments', 'No one is ever allowed to file a complaint'], 0),
    ('Why might a government create an ombudsman position?', ['To give citizens a way to seek fair resolution of their concerns', 'Ombudsmen serve no useful purpose', 'This concept has no connection to social studies', 'Citizens never have any concerns about government services'], 0),
    ('How is the role of an ombudsman similar to the role of the Auditor General?', ['Both work independently to hold government accountable, though they focus on different areas', 'They perform the exact same identical duties', 'Neither role has anything to do with accountability', 'Only the Auditor General reviews government actions'], 0)]),
]),
day(128, [
L('Writing: Writing a Public Service Announcement',
  'Grade 5 Language strand: a public service announcement, or PSA, is a short piece of writing that informs or persuades an audience about an important issue, such as safety or the environment, often ending with a clear message.',
  [('What is the purpose of a public service announcement?', ['To inform or persuade an audience about an important issue', 'To sell a product for profit', 'To tell a personal fictional story', 'To provide a dictionary definition'], 0),
   ('Which topic might a public service announcement address?', ['Road safety or environmental protection', 'A made-up fairy tale', 'A grocery list', 'A private diary entry'], 0),
   ('What might a strong public service announcement include near the end?', ['A clear message or call to action', 'A confusing conclusion', 'No message at all', 'An unrelated joke'], 0),
   ('Why might a public service announcement use direct, clear language?', ['To make sure the audience understands the important message quickly', 'Clear language never helps communicate an important message', 'This concept has no connection to writing', 'PSAs are always intentionally confusing'], 0),
   ('Which is an example of a public service announcement topic?', ['Encouraging people to wear seatbelts', 'A story about a dragon', 'A recipe for cookies', 'A weather report'], 0)]),
M('Geometry: Complementary and Supplementary Angles',
  'Grade 5 Math strand: complementary angles add up to 90 degrees, while supplementary angles add up to 180 degrees, and these relationships help solve for missing angle measures.',
  [('What do complementary angles add up to?', ['90 degrees', '180 degrees', '360 degrees', '45 degrees'], 0),
   ('What do supplementary angles add up to?', ['180 degrees', '90 degrees', '360 degrees', '270 degrees'], 0),
   ('If one angle measures 30 degrees, what does its complementary angle measure?', ['60 degrees', '150 degrees', '90 degrees', '30 degrees'], 0),
   ('If one angle measures 110 degrees, what does its supplementary angle measure?', ['70 degrees', '90 degrees', '180 degrees', '110 degrees'], 0),
   ('Why might understanding complementary and supplementary angles help when solving geometry problems?', ['They allow you to calculate a missing angle when you know its paired angle', 'These relationships never help solve for angles', 'This concept has no connection to geometry', 'Complementary and supplementary angles are always identical'], 0)]),
Sc('How Seeds Are Dispersed',
   'Grade 5 Science strand: plants disperse their seeds through methods such as wind, water, and animals, helping new plants grow in locations away from the parent plant.',
   [('What does seed dispersal mean?', ['Spreading seeds to new locations away from the parent plant', 'Keeping seeds in one place forever', 'Destroying seeds completely', 'Preventing seeds from growing'], 0),
    ('Which of these is a method of seed dispersal?', ['Wind carrying light seeds through the air', 'Seeds refusing to move at all', 'Seeds dissolving in soil', 'Seeds turning into rocks'], 0),
    ('How might an animal help disperse a seed?', ['By eating a fruit and later depositing the seed elsewhere', 'Animals never interact with seeds', 'This concept has no relevance to science', 'Animals always destroy every seed they touch'], 0),
    ('Why might seeds with hooks or burrs be adapted for dispersal by animals?', ['They can attach to fur and be carried to new locations', 'Hooked seeds never attach to anything', 'This concept has no connection to life systems', 'Hooks prevent seeds from being dispersed at all'], 0),
    ('Why is seed dispersal important for a plant species?', ['It reduces competition with the parent plant and helps the species spread to new areas', 'Seed dispersal has no benefit to a plant', 'This concept has no relevance to science', 'Seeds always grow better directly beside the parent plant'], 0)]),
SS('Trade Surplus and Trade Deficit — Balancing What Canada Buys and Sells',
   'Grade 5 Social Studies strand: a trade surplus occurs when a country exports more than it imports, while a trade deficit occurs when it imports more than it exports, both affecting a countrys economy.',
   [('What is a trade surplus?', ['When a country exports more than it imports', 'When a country imports more than it exports', 'When trade is completely banned', 'A type of federal tax'], 0),
    ('What is a trade deficit?', ['When a country imports more than it exports', 'When a country exports more than it imports', 'When no trade occurs at all', 'A kind of national holiday'], 0),
    ('What does it mean to export a good?', ['To sell it to another country', 'To buy it from another country', 'To destroy it', 'To store it permanently'], 0),
    ('What does it mean to import a good?', ['To buy it from another country', 'To sell it to another country', 'To manufacture it domestically only', 'To throw it away'], 0),
    ('Why might understanding trade surpluses and deficits help explain a countrys economic relationships?', ['They show how much a country is buying from versus selling to other countries', 'Trade balances never affect a countrys economy', 'This concept has no relevance to social studies', 'Imports and exports are always exactly equal for every country'], 0)]),
]),
day(129, [
L('Vocabulary: Eponyms — Words That Come From Names',
  'Grade 5 Language strand: an eponym is a word derived from the name of a real or fictional person, such as sandwich, named after the Earl of Sandwich.',
  [('What is an eponym?', ['A word derived from the name of a person', 'A word with two opposite meanings', 'A word that sounds like its meaning', 'A type of punctuation mark'], 0),
   ('The word sandwich is an example of an eponym because it comes from ___.', ['The name of the Earl of Sandwich', 'A type of bread only', 'A scientific formula', 'A place name only'], 0),
   ('Why might a word become an eponym over time?', ['People began using a persons name to describe something associated with them', 'Eponyms are randomly assigned with no connection to a person', 'This concept has no connection to vocabulary', 'Eponyms never relate to real or fictional people'], 0),
   ('Which of these is most likely to be an example of an eponym?', ['A type of shoe named after its inventor', 'A word describing the colour blue', 'A common punctuation mark', 'A basic number word'], 0),
   ('Why might learning about eponyms help build vocabulary knowledge?', ['It shows how the history behind a word can reveal its meaning and origin', 'Eponyms never provide any useful information about a words meaning', 'This concept has no relevance to vocabulary', 'Word origins never connect to real people or stories'], 0)]),
M('Data Management: Expressing Probability as a Fraction, Decimal, and Percent',
  'Grade 5 Math strand: the probability of an event can be expressed as a fraction, a decimal, or a percent, all representing the same likelihood in different forms.',
  [('If a probability is expressed as 1/4, what is this as a percent?', ['25 percent', '50 percent', '75 percent', '4 percent'], 0),
   ('If a probability is expressed as 0.5, what is this as a fraction?', ['1/2', '1/4', '1/5', '1/10'], 0),
   ('What is the probability of flipping a coin and landing on heads, expressed as a fraction?', ['1/2', '1/4', '1/3', '1'], 0),
   ('Why might expressing the same probability in different forms, like a fraction and a percent, be useful?', ['Different forms can be easier to understand or compare in different situations', 'All forms of probability always mean completely different things', 'This concept has no connection to data management', 'Probability can never be expressed as a percent'], 0),
   ('If an event has a probability of 100 percent, what does this mean?', ['The event is certain to happen', 'The event will never happen', 'The event might happen', 'The event is impossible'], 0)]),
Sc('Thermal Conductors and Insulators',
   'Grade 5 Science strand: a thermal conductor, such as metal, allows heat to pass through it easily, while a thermal insulator, such as wood or foam, slows the transfer of heat.',
   [('What is a thermal conductor?', ['A material that allows heat to pass through it easily', 'A material that blocks all heat completely', 'A material that creates heat on its own', 'A material with no effect on heat'], 0),
    ('What is a thermal insulator?', ['A material that slows the transfer of heat', 'A material that speeds up heat transfer the most', 'A material that generates its own heat', 'A material unrelated to temperature'], 0),
    ('Which of these materials is generally a good thermal conductor?', ['Metal', 'Foam', 'Wood', 'Wool'], 0),
    ('Why might a cooking pot have a metal base but a plastic or wooden handle?', ['The metal conducts heat to cook food, while the handle insulates to stay cool to the touch', 'Metal never conducts heat', 'Plastic and wood always conduct heat better than metal', 'Handles are never designed with heat in mind'], 0),
    ('Why might builders use insulating materials in the walls of a house?', ['To slow the transfer of heat and help keep indoor temperatures stable', 'Insulating materials always increase heat loss', 'This concept has no relevance to science', 'Walls never need any insulation'], 0)]),
SS('Canada and the Olympic Games',
   'Grade 5 Social Studies strand: Canada has participated in the Olympic Games for over a century and has hosted the Games multiple times, including in Montreal, Calgary, and Vancouver, showcasing Canadian athletes and culture on a global stage.',
   [('Has Canada hosted the Olympic Games more than once?', ['Yes', 'No, only a single time', 'A concept unrelated to Canadian history', 'Canada has never hosted the Olympics'], 0),
    ('Name one Canadian city that has hosted the Olympic Games.', ['Vancouver', 'Halifax', 'Winnipeg', 'Regina'], 0),
    ('Why might hosting the Olympic Games be significant for a country like Canada?', ['It showcases Canadian culture and athletes on a global stage', 'Hosting the Olympics has no significance for a country', 'This concept has no relevance to social studies', 'The Olympics are never broadcast internationally'], 0),
    ('What do Olympic athletes represent when competing internationally?', ['Their home country', 'No particular group', 'Only their local city', 'A private company'], 0),
    ('Why might Canadians take pride in hosting or competing in the Olympic Games?', ['It highlights national achievement and unites people around shared events', 'National pride is never connected to sporting events', 'This concept has no connection to Canadian identity', 'The Olympics never involve any Canadian participation'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Writing Forms, and Vocabulary',
  'Grade 5 Language strand review: students revisit relative pronouns, perfect verb tenses, writing an advertisement, suspense and cliffhangers, and collective nouns.',
  [('Which word is the relative pronoun in the sentence The book that I borrowed was excellent?', ['That', 'Book', 'Borrowed', 'Excellent'], 0),
   ('Which sentence uses the present perfect tense?', ['She has finished her homework.', 'She finishes her homework.', 'She will finish her homework.', 'She finished her homework yesterday.'], 0),
   ('What is the purpose of an advertisement?', ['To persuade an audience to buy a product or support an idea', 'To tell a neutral news story', 'To record historical events', 'To provide a dictionary definition'], 0),
   ('What is a cliffhanger?', ['An ending that leaves an important question unanswered', 'A chapter that reveals every answer immediately', 'A type of nonfiction text feature', 'A grammar rule'], 0),
   ('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that names only one person', 'A word that shows possession', 'A type of adverb'], 0)]),
M('Math Review: Data, Algebra, and Geometry',
  'Grade 5 Math strand review: students revisit permutations, currency exchange rates, simple inequalities, rotations, and Roman numerals.',
  [('What does a permutation count?', ['The number of ordered arrangements of items', 'The number of ways to group items when order does not matter', 'A single fixed outcome', 'A type of fraction'], 0),
   ('What does a currency exchange rate show?', ['How much one countrys currency is worth compared to another', 'The total population of a country', 'A type of tax rate', 'A single fixed price for every item'], 0),
   ('What symbol means greater than?', ['>', '<', '=', '÷'], 0),
   ('What does a rotation do to a shape?', ['Turns it around a fixed point', 'Slides it in a straight line', 'Flips it over a line', 'Makes it larger'], 0),
   ('What number does the Roman numeral X represent?', ['10', '5', '1', '50'], 0)]),
Sc('Science Review: Energy, Earth and Space, and Life Systems',
   'Grade 5 Science strand review: students revisit geothermal and biomass power, the northern lights, Newtons first law of motion, types of precipitation, and the human brain.',
   [('What does geothermal power use as its energy source?', ['Heat stored deep within the Earth', 'Sunlight', 'Wind', 'Ocean waves'], 0),
    ('What causes the northern lights?', ['Charged particles from the sun colliding with gases in Earths atmosphere', 'Reflections from the Moon', 'Light from distant stars only', 'City streetlights'], 0),
    ('According to Newtons first law, what happens to an object at rest unless a force acts on it?', ['It stays at rest', 'It always starts moving on its own', 'It disappears', 'It doubles in size'], 0),
    ('What is precipitation?', ['Water that falls from clouds to Earths surface', 'A type of rock', 'A form of soil', 'A kind of wind'], 0),
    ('What is the brain often described as?', ['The control centre of the nervous system', 'A type of muscle', 'A digestive organ', 'A part of the skeletal system'], 0)]),
SS('Social Studies Review: Government, History, and Economy',
   'Grade 5 Social Studies strand review: students revisit the Prime Minister, the House of Commons, the Numbered Treaties, the Great Flag Debate, and the Persons Case.',
   [('What is the Prime Ministers main role in Canadas government?', ['Leading the federal government', 'Representing the monarch ceremonially', 'Leading a provincial government', 'Serving as a judge on the Supreme Court'], 0),
    ('What is the House of Commons?', ['The elected lower house of Canadas Parliament', 'An appointed upper house', 'A provincial legislature', 'A municipal council'], 0),
    ('What were the Numbered Treaties?', ['A series of agreements made between the Crown and First Nations', 'A set of provincial tax laws', 'A type of modern trade agreement', 'A collection of national holidays'], 0),
    ('What was the Great Flag Debate of 1964 about?', ['Whether Canada should adopt a new, distinctly Canadian flag', 'A debate about provincial borders', 'A discussion about national holidays', 'An argument over currency design'], 0),
    ('What did the Persons Case of 1929 decide?', ['That women were legally recognized as persons eligible for Senate appointment', 'That women could no longer vote', 'That only men could hold government positions', 'That Canada would adopt a new flag'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_121_130)
    append_to(5, g5_121_130)
