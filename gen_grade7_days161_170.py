#!/usr/bin/env python3
"""Grade 7, Days 161-170 -- extends Grade 7 from 160 to 170 days. Topics
chosen after dumping the full (subject, title) list for Days 1-160 from
data/grade7.json (640 unique (subject, title) pairs, zero duplicates) and
grepping every candidate title/keyword below against that dump to confirm
zero overlap, since Grade 7's earlier 160 days already cover an
unusually exhaustive range of subject matter across all four subjects.

Fresh, non-duplicate topics picked this batch:
Language: the perfect verb tenses (present, past, future perfect),
restrictive and non-restrictive modifiers, compound words and how they
are formed, making inferences from text evidence, writing a travel
brochure or itinerary, analyzing tone shifts within a single text,
writing a fable with a clear moral, analyzing reality television and its
construction (media literacy), synonyms/antonyms and shades of meaning.
Math: point-slope form of a linear equation, elapsed time and 24-hour
clock conversions, understanding insurance and risk management (financial
literacy), prime factorization using factor trees, classifying triangles
by sides and angles, constructing and interpreting pictographs with
scaled symbols, translating words into algebraic expressions and
equations, calculating the area of composite 2D shapes, the law of large
numbers (probability).
Science: solar and lunar eclipses, the layers of the atmosphere, the law
of conservation of mass, the law of conservation of energy, how GPS and
satellite navigation work, vestigial structures and evidence of
evolution, measuring earthquakes (magnitude and seismographs), animal
classification (vertebrates and invertebrates), gravity and free fall.
SocialStudies: the founding of Halifax in 1749, Canadas immigration
points system of 1967, the Royal Canadian Mounted Police and Canadian
policing history, the Great Lakes (economic and ecological importance),
supply management in Canadian agriculture, the Canadian Senate
(structure, role, and reform debates), hockey and its role in Canadian
national identity, the Massey Commission and Canadian culture, the
Canadian Museum for Human Rights.

None of these titles or underlying topics duplicate anything appearing in
Days 1-160 of data/grade7.json (verified both by reading the full title
dump and by grepping every candidate title keyword against it before
writing this file). Day 170 is a cross-subject review day drawing quiz
content from Days 161-169 of this batch, with review titles kept
textually distinct from every earlier review day (including Day 160's
four review titles).

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py through gen_grade7_days151_160.py (e.g.
"Canadas" not "Canada's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days161_170.py
  cd ~/gradesbooster && python3 build_json.py --grade 7
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


g7_161_170 = [
day(161, [
L('Grammar: The Perfect Verb Tenses — Present, Past, and Future Perfect',
  'Grade 7 Language strand: the present perfect tense (has/have plus a past participle) shows an action begun in the past that still has relevance now, the past perfect tense (had plus a past participle) shows an action completed before another past action, and the future perfect tense (will have plus a past participle) shows an action that will be completed before a specific future time.',
  [('What does the present perfect tense generally show?', ['An action that started in the past and still has relevance now', 'An action that will never happen', 'A concept unrelated to grammar', 'An action that can only happen in the future'], 0),
   ('Which auxiliary verb is used to form the past perfect tense?', ['Had', 'Will', 'A concept unrelated to verb tenses', 'Is'], 0),
   ('Which sentence correctly uses the future perfect tense?', ['By next June, I will have finished my project.', 'By next June, I finish my project.', 'By next June, I finishing my project.', 'By next June, I am finish my project.'], 0),
   ('Why might a writer use the past perfect tense when describing two events that both happened in the past?', ['To show clearly which of the two events happened first', 'The past perfect tense can never describe more than one event', 'A concept unrelated to grammar', 'To make both events seem like they happen in the future'], 0),
   ('Which sentence correctly uses the present perfect tense?', ['She has visited that museum three times.', 'She visit that museum three times.', 'She having visited that museum three times.', 'She will visited that museum three times.'], 0)]),
M('Algebra: Point-Slope Form of a Linear Equation',
  'Grade 7 Math strand: point-slope form, written as y minus y1 equals m times the quantity x minus x1, lets a person write the equation of a line directly from its slope m and the coordinates of a single known point (x1, y1), which is especially useful when the y-intercept is not known.',
  [('What two pieces of information does point-slope form require to write the equation of a line?', ['The slope and the coordinates of one known point on the line', 'Only the y-intercept of the line', 'A concept unrelated to algebra', 'Two unrelated equations with no shared point'], 0),
   ('What is the general form of the point-slope equation?', ['y minus y1 equals m times the quantity x minus x1', 'y equals x plus m', 'A concept unrelated to point-slope form', 'm equals y1 minus x1'], 0),
   ('If a line has a slope of 3 and passes through the point (2, 5), what is its point-slope equation?', ['y minus 5 equals 3 times the quantity x minus 2', 'y minus 2 equals 3 times the quantity x minus 5', 'y minus 5 equals 2 times the quantity x minus 3', 'A concept unrelated to point-slope form'], 0),
   ('Why might point-slope form be more convenient than slope-intercept form when only a slope and one non-intercept point are known?', ['It lets you write the equation immediately without first solving for the y-intercept', 'Point-slope form can never be converted into slope-intercept form', 'A concept unrelated to algebra', 'Slope-intercept form never requires knowing the y-intercept'], 0),
   ('How can a point-slope equation be rewritten in slope-intercept form?', ['By expanding and isolating y on one side of the equation', 'Point-slope and slope-intercept forms can never describe the same line', 'A concept unrelated to linear equations', 'By deleting the slope value entirely'], 0)]),
Sc('Astronomy: Solar and Lunar Eclipses',
   'Grade 7 Science strand: a solar eclipse occurs when the moon passes directly between the sun and Earth, blocking some or all of the suns light, while a lunar eclipse occurs when Earth passes between the sun and the moon, causing Earths shadow to fall across the moons surface.',
   [('What happens during a solar eclipse?', ['The moon passes between the sun and Earth, blocking some or all sunlight', 'Earth passes between the sun and the moon', 'A concept unrelated to astronomy', 'The sun disappears permanently from the sky'], 0),
    ('What happens during a lunar eclipse?', ['Earth passes between the sun and the moon, casting its shadow on the moon', 'The moon passes between the sun and Earth', 'A concept unrelated to eclipses', 'The moon moves permanently out of orbit'], 0),
    ('Why do eclipses not happen every single month, even though the moon orbits Earth monthly?', ['The moons orbit is tilted slightly relative to Earths orbit around the sun, so perfect alignment is rare', 'Eclipses actually happen every single day', 'A concept unrelated to astronomy', 'The moon stops moving during most months'], 0),
    ('During a total solar eclipse, what can typically be seen from within the path of totality?', ['The suns outer atmosphere, or corona, briefly becomes visible', 'The moon becomes completely invisible in the sky', 'A concept unrelated to solar eclipses', 'The sun grows permanently brighter than usual'], 0),
    ('Why is it dangerous to look directly at the sun during a partial solar eclipse without proper eye protection?', ['Harmful sunlight can still damage the eyes even when much of the sun is blocked', 'Partial eclipses produce no sunlight at all', 'This concept has no relevance to science', 'Eye protection has no effect during any type of eclipse'], 0)]),
SS('Social Studies: The Founding of Halifax in 1749',
   'Grade 7 Social Studies strand: the British founded Halifax in 1749 as a fortified naval settlement on the Atlantic coast, intended to counterbalance the nearby French fortress of Louisbourg, and the city grew into a major port and naval base central to Atlantic Canadas history.',
   [('In what year was Halifax founded?', ['1749', '1867', '1917', '1608'], 0),
    ('Which European power founded Halifax?', ['Britain', 'France', 'A concept unrelated to Halifax', 'Spain'], 0),
    ('Why did the British want a fortified settlement at Halifax?', ['To counterbalance the nearby French fortress of Louisbourg', 'To eliminate all French presence from Europe entirely', 'A concept unrelated to Canadian history', 'Halifax was founded with no strategic purpose at all'], 0),
    ('What role did Halifax grow into over time?', ['A major Atlantic port and naval base', 'A landlocked farming settlement with no ocean access', 'A concept unrelated to the founding of Halifax', 'A city with no connection to shipping or the navy'], 0),
    ('Why was a coastal location strategically important for a settlement like Halifax?', ['It allowed ships and naval forces to be based there for defence and trade', 'Coastal location has no strategic value of any kind', 'This concept has no relevance to social studies', 'Halifax was built far from any coastline'], 0)]),
]),
day(162, [
L('Grammar: Restrictive and Non-Restrictive Modifiers',
  'Grade 7 Language strand: a restrictive modifier provides essential information needed to identify the noun it describes and is not set off by commas, while a non-restrictive modifier adds extra, non-essential information and is set off by commas.',
  [('What does a restrictive modifier do?', ['Provides essential information needed to identify the noun it describes', 'Adds information that could be removed with no change in meaning', 'A concept unrelated to grammar', 'Always begins a sentence with a comma'], 0),
   ('How is a non-restrictive modifier typically punctuated?', ['It is set off by commas', 'It is never separated from the rest of the sentence in any way', 'A concept unrelated to modifiers', 'It always ends with an exclamation mark'], 0),
   ('Which sentence uses a restrictive modifier correctly, without commas?', ['The book that is on the table belongs to me.', 'The book, that is on the table, belongs to me.', 'The book that, is on the table belongs, to me.', 'The, book that is on the table belongs to me.'], 0),
   ('Why might removing a non-restrictive modifier from a sentence leave the core meaning unchanged?', ['A non-restrictive modifier adds extra detail rather than identifying which noun is meant', 'Non-restrictive modifiers always change the entire meaning of a sentence', 'A concept unrelated to grammar', 'Removing any modifier always makes a sentence meaningless'], 0),
   ('Which sentence uses a non-restrictive modifier correctly, with commas?', ['My sister, who lives in Ottawa, is visiting this weekend.', 'My sister who lives in Ottawa is visiting this weekend and only her.', 'My, sister who lives in Ottawa, is visiting.', 'My sister who, lives in Ottawa is visiting.'], 0)]),
M('Measurement: Elapsed Time and 24-Hour Clock Conversions',
  'Grade 7 Math strand: elapsed time is found by subtracting a starting time from an ending time, and the 24-hour clock avoids the need for AM and PM by numbering the hours of the day from 0 to 23, a format commonly used in travel schedules and scientific records.',
  [('How is elapsed time generally calculated?', ['By subtracting the starting time from the ending time', 'By adding the starting time and ending time together', 'A concept unrelated to measurement', 'Elapsed time cannot be calculated in any way'], 0),
   ('What is 19:45 in 24-hour time converted to 12-hour time?', ['7:45 PM', '7:45 AM', '9:45 PM', '5:45 PM'], 0),
   ('If a train departs at 2:15 PM and arrives at 5:40 PM, how much time has elapsed?', ['3 hours and 25 minutes', '3 hours and 15 minutes', '2 hours and 40 minutes', '4 hours and 5 minutes'], 0),
   ('Why is the 24-hour clock often used in travel schedules and scientific records?', ['It avoids confusion between AM and PM times', 'It makes every schedule exactly one hour longer', 'A concept unrelated to measurement', 'It removes the need to track time at all'], 0),
   ('What time is 00:30 in 24-hour time when converted to 12-hour time?', ['12:30 AM', '12:30 PM', '1:30 AM', '11:30 PM'], 0)]),
Sc('Earth Science: The Layers of the Atmosphere',
   'Grade 7 Science strand: Earths atmosphere is divided into layers based on temperature and altitude, including the troposphere closest to the surface where weather occurs, the stratosphere containing the ozone layer, and the higher mesosphere, thermosphere, and exosphere.',
   [('In which layer of the atmosphere does most weather occur?', ['The troposphere', 'The stratosphere', 'A concept unrelated to earth science', 'The exosphere'], 0),
    ('Which layer of the atmosphere contains most of the ozone layer?', ['The stratosphere', 'The troposphere', 'A concept unrelated to atmospheric layers', 'The mesosphere'], 0),
    ('What is the outermost layer of Earths atmosphere, gradually fading into space?', ['The exosphere', 'The troposphere', 'A concept unrelated to the atmosphere', 'The stratosphere'], 0),
    ('How are the layers of the atmosphere generally distinguished from one another?', ['By differences in temperature and altitude', 'By differences in colour visible from the ground', 'A concept unrelated to earth science', 'Every layer of the atmosphere is identical'], 0),
    ('Why is the ozone layer within the stratosphere considered important for life on Earth?', ['It absorbs much of the suns harmful ultraviolet radiation', 'The ozone layer has no effect on radiation reaching Earth', 'This concept has no relevance to science', 'The ozone layer only exists at ground level'], 0)]),
SS('Social Studies: Canadas Immigration Points System of 1967',
   'Grade 7 Social Studies strand: introduced in 1967, Canadas immigration points system evaluates prospective immigrants using factors such as education, language ability, and work experience rather than country of origin, replacing earlier, more discriminatory immigration policies.',
   [('In what year was Canadas points-based immigration system introduced?', ['1967', '1917', '1949', '1982'], 0),
    ('What kinds of factors does the points system use to evaluate prospective immigrants?', ['Education, language ability, and work experience', 'Only the applicants country of origin', 'A concept unrelated to Canadian immigration policy', 'Only the applicants age'], 0),
    ('What earlier approach to immigration did the points system help move Canada away from?', ['Policies that favoured or excluded applicants based on country of origin', 'Canada had no immigration policy at all before 1967', 'A concept unrelated to social studies', 'Policies that considered only an applicants savings'], 0),
    ('Why might a points system be considered a more equitable approach to selecting immigrants?', ['It evaluates individual qualifications rather than background or origin', 'A points system always excludes every applicant automatically', 'A concept unrelated to immigration policy', 'It removes all criteria for evaluating applicants'], 0),
    ('How might language ability, as a points-system factor, benefit a newcomer settling in Canada?', ['It can help newcomers find work and integrate into their community more easily', 'Language ability has no connection to settling in a new country', 'This concept has no relevance to social studies', 'Language ability is never considered relevant to immigration'], 0)]),
]),
day(163, [
L('Vocabulary: Compound Words and How They Are Formed',
  'Grade 7 Language strand: a compound word is formed by joining two or more smaller words to create a new word with its own meaning, and compound words can be closed (notebook), hyphenated (well-known), or open with a space between the words (ice cream).',
  [('What is a compound word?', ['A word formed by joining two or more smaller words together', 'A word that can never be broken into smaller words', 'A concept unrelated to vocabulary', 'A word that always has exactly one syllable'], 0),
   ('Which of these is an example of a closed compound word?', ['Notebook', 'Well-known', 'A concept unrelated to compound words', 'Ice cream'], 0),
   ('Which of these is an example of an open compound word, written with a space?', ['Ice cream', 'Notebook', 'A concept unrelated to vocabulary', 'Sunflower'], 0),
   ('Which of these is an example of a hyphenated compound word?', ['Well-known', 'Notebook', 'A concept unrelated to hyphenation', 'Ice cream'], 0),
   ('Why might the meaning of a compound word differ from the meanings of its two smaller words combined literally?', ['Compound words sometimes take on a new meaning that is not obvious from each part alone', 'Compound words always mean exactly what each smaller word means added together', 'This concept has no relevance to vocabulary', 'A compound word can never carry any new meaning'], 0)]),
M('Financial Literacy: Understanding Insurance and Risk Management',
  'Grade 7 Math strand: insurance is a way of managing financial risk in which a person pays regular premiums to a company that agrees to cover certain losses, helping individuals and families protect themselves against large, unexpected costs.',
  [('What is insurance designed to help manage?', ['Financial risk from large, unexpected costs', 'Every single everyday household expense', 'A concept unrelated to financial literacy', 'The exact weather forecast for a given day'], 0),
   ('What does a person typically pay regularly to keep an insurance policy active?', ['A premium', 'A one-time fee that is never repeated', 'A concept unrelated to insurance', 'Nothing at all is ever paid for insurance'], 0),
   ('If a family pays 100 dollars a month for insurance, how much do they pay over one year?', ['1200 dollars', '100 dollars', '1000 dollars', '1100 dollars'], 0),
   ('Why might a family choose to purchase insurance even if they never end up needing to make a claim?', ['It provides financial protection in case an unexpected, costly event occurs', 'Insurance never provides any kind of financial protection', 'A concept unrelated to risk management', 'Insurance is only useful after an event has already happened'], 0),
   ('What is one reason insurance premiums might be higher for a higher-risk situation?', ['Higher risk increases the chance the insurance company will need to pay out a claim', 'Premiums are always identical regardless of risk level', 'This concept has no relevance to financial literacy', 'Risk level has no connection to insurance costs at all'], 0)]),
Sc('Chemistry: The Law of Conservation of Mass',
   'Grade 7 Science strand: the law of conservation of mass states that matter cannot be created or destroyed during a chemical reaction, meaning the total mass of the reactants must equal the total mass of the products.',
   [('What does the law of conservation of mass state?', ['Matter cannot be created or destroyed during a chemical reaction', 'Matter is always created during a chemical reaction', 'A concept unrelated to chemistry', 'Mass always disappears completely during a reaction'], 0),
    ('In a chemical reaction, how should the total mass of the reactants compare to the total mass of the products?', ['They should be equal', 'The products should always weigh less than the reactants', 'A concept unrelated to conservation of mass', 'The reactants should always weigh nothing at all'], 0),
    ('If 10 grams of one substance react completely with 5 grams of another, what should the total mass of the products equal?', ['15 grams', '5 grams', '10 grams', '50 grams'], 0),
    ('Why might a chemical reaction that produces a gas appear to lose mass if conducted in an open container?', ['The gas escapes into the air and its mass is no longer measured in the container', 'Gases never have any mass at all', 'A concept unrelated to chemistry', 'Mass is always destroyed whenever a gas forms'], 0),
    ('Why is the law of conservation of mass important when balancing chemical equations?', ['It ensures the same number and type of atoms appear on both sides of the equation', 'Balancing equations has no connection to conservation of mass', 'This concept has no relevance to science', 'Chemical equations never need to be balanced'], 0)]),
SS('Social Studies: The Royal Canadian Mounted Police and Canadian Policing History',
   'Grade 7 Social Studies strand: the Royal Canadian Mounted Police traces its origins to the North-West Mounted Police, formed in 1873 to bring law and order to the western territories, and later grew into a national police force closely associated with Canadian identity.',
   [('What was the RCMP originally known as when it was formed in 1873?', ['The North-West Mounted Police', 'The Royal Canadian Navy', 'A concept unrelated to Canadian policing', 'The Halifax Harbour Guard'], 0),
    ('What was one original purpose of the North-West Mounted Police?', ['To bring law and order to the western territories', 'To patrol the Atlantic coastline exclusively', 'A concept unrelated to the RCMP', 'To manage international trade agreements'], 0),
    ('How has the RCMPs role changed since its founding in the 1870s?', ['It grew from a regional force into a national police force', 'It has never changed in any way since 1873', 'A concept unrelated to social studies', 'It was eliminated entirely shortly after being founded'], 0),
    ('Why might the RCMP be closely associated with Canadian identity around the world?', ['Its distinctive uniform and history have become widely recognized national symbols', 'The RCMP has no recognizable symbols or uniform of any kind', 'A concept unrelated to policing history', 'The RCMP operates only outside of Canada'], 0),
    ('Why might a country establish a national police force in addition to local or provincial police services?', ['To provide law enforcement and coordination across larger or more remote areas', 'National police forces have no purpose distinct from local police', 'This concept has no relevance to social studies', 'A country can never have more than one police service'], 0)]),
]),
day(164, [
L('Reading: Making Inferences from Text Evidence',
  'Grade 7 Language strand: an inference is a conclusion a reader draws by combining clues and evidence stated directly in a text with their own background knowledge, since authors do not always state every detail explicitly.',
  [('What is an inference?', ['A conclusion drawn by combining text evidence with background knowledge', 'A fact that is always stated directly and explicitly in the text', 'A concept unrelated to reading', 'A random guess with no connection to the text at all'], 0),
   ('Why might a reader need to make an inference while reading a story?', ['Authors do not always state every detail directly, so readers must fill in gaps', 'Every detail in every story is always stated explicitly', 'A concept unrelated to reading', 'Inferences are never useful when reading any text'], 0),
   ('If a character slams a door and refuses to speak, what might a reader infer about their feelings?', ['The character is likely angry or upset', 'The character is definitely feeling calm and relaxed', 'A concept unrelated to making inferences', 'No inference can ever be made from this description'], 0),
   ('What two things does a reader typically combine to make a strong inference?', ['Evidence from the text and their own background knowledge', 'Two completely unrelated pieces of information', 'A concept unrelated to reading', 'A reader never needs any evidence to make an inference'], 0),
   ('Why is it important for a reader to be able to point to specific text evidence supporting an inference?', ['It shows the inference is reasonably supported rather than just a guess', 'Text evidence is never needed to support an inference', 'This concept has no relevance to reading', 'Inferences supported by evidence are always incorrect'], 0)]),
M('Number Theory: Prime Factorization Using Factor Trees',
  'Grade 7 Math strand: prime factorization means writing a whole number as a product of its prime factors, and a factor tree is a diagram that breaks a number down step by step into smaller factors until every branch ends in a prime number.',
  [('What does prime factorization mean?', ['Writing a whole number as a product of its prime factors', 'Writing a whole number as a sum of unrelated numbers', 'A concept unrelated to number theory', 'Dividing a number by zero repeatedly'], 0),
   ('What is the prime factorization of 12?', ['2 times 2 times 3', '2 times 6', '3 times 4', '1 times 12'], 0),
   ('In a factor tree, when does a branch stop being broken down further?', ['When it reaches a prime number', 'When it reaches any even number', 'A concept unrelated to factor trees', 'A factor tree never stops branching'], 0),
   ('What is the prime factorization of 30?', ['2 times 3 times 5', '2 times 15', '5 times 6', '3 times 10'], 0),
   ('Why is prime factorization useful when finding the greatest common factor of two numbers?', ['Comparing the prime factors of each number reveals which factors they share', 'Prime factorization has no connection to finding common factors', 'A concept unrelated to number theory', 'The greatest common factor can never be found using prime factors'], 0)]),
Sc('Physics: The Law of Conservation of Energy',
   'Grade 7 Science strand: the law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form into another, such as potential energy converting into kinetic energy, so the total energy in a closed system stays constant.',
   [('What does the law of conservation of energy state?', ['Energy cannot be created or destroyed, only transformed from one form to another', 'Energy is constantly being created out of nothing', 'A concept unrelated to physics', 'Energy always disappears completely over time'], 0),
    ('What happens to potential energy as an object falls?', ['It converts into kinetic energy', 'It disappears completely with no transformation', 'A concept unrelated to conservation of energy', 'It converts directly into mass'], 0),
    ('In a closed system with no energy entering or leaving, what happens to the total amount of energy?', ['It stays constant', 'It constantly increases without limit', 'A concept unrelated to physics', 'It constantly decreases to zero'], 0),
    ('Why might a swinging pendulum eventually slow down even though energy is conserved overall?', ['Some of its energy is transformed into heat and sound through friction and air resistance', 'Energy conservation means the pendulum can never slow down at all', 'A concept unrelated to conservation of energy', 'The pendulum loses energy that simply vanishes from existence'], 0),
    ('Why is the law of conservation of energy considered a fundamental principle in physics?', ['It applies to nearly every physical process and helps explain how energy moves and changes form', 'It applies only to a single, very specific type of machine', 'This concept has no relevance to science', 'It has been shown to be true only in outer space'], 0)]),
SS('Social Studies: The Great Lakes — Economic and Ecological Importance',
   'Grade 7 Social Studies strand: the five Great Lakes, Superior, Michigan, Huron, Erie, and Ontario, form the largest group of freshwater lakes by surface area in the world, supporting major shipping and trade routes, drinking water supplies, and diverse ecosystems, while also facing pollution and invasive species challenges.',
   [('How many Great Lakes are there?', ['Five', 'Three', 'A concept unrelated to the Great Lakes', 'Seven'], 0),
    ('What makes the Great Lakes significant on a global scale?', ['They form the largest group of freshwater lakes by surface area in the world', 'They contain no freshwater of any kind', 'A concept unrelated to social studies', 'They are located entirely outside of North America'], 0),
    ('What is one economic activity supported by the Great Lakes?', ['Shipping and trade', 'The Great Lakes support no economic activity of any kind', 'A concept unrelated to the Great Lakes', 'Only activities unrelated to water or transportation'], 0),
    ('What is one environmental challenge facing the Great Lakes?', ['Pollution and invasive species', 'The Great Lakes face no environmental challenges at all', 'A concept unrelated to ecology', 'Excessive ice cover every single day of the year'], 0),
    ('Why are the Great Lakes important as a source of drinking water for millions of people?', ['They hold a vast supply of accessible freshwater near many major cities', 'The Great Lakes contain no freshwater suitable for drinking', 'This concept has no relevance to social studies', 'Drinking water has no connection to the Great Lakes'], 0)]),
]),
day(165, [
L('Writing: Writing a Travel Brochure or Itinerary',
  'Grade 7 Language strand: a travel brochure or itinerary blends persuasive and descriptive writing to highlight a destinations attractions, using vivid sensory details and a clear structure, such as a day-by-day itinerary or organized thematic sections, to inform and persuade readers.',
  [('What two writing styles does a travel brochure typically blend?', ['Persuasive and descriptive writing', 'Only technical and scientific writing', 'A concept unrelated to writing', 'Only formal legal writing'], 0),
   ('Why might a travel brochure use vivid sensory details?', ['To help readers imagine the sights, sounds, and experiences of a destination', 'Sensory details are never included in a travel brochure', 'A concept unrelated to travel writing', 'To make the destination sound as boring as possible'], 0),
   ('What is one common way to organize a travel itinerary?', ['Day-by-day, listing planned activities for each day', 'With no organization or structure at all', 'A concept unrelated to writing an itinerary', 'By listing activities in a completely random order'], 0),
   ('Why might a travel brochure end with a persuasive call to action?', ['To encourage readers to actually visit the destination', 'Persuasive writing is never appropriate in a travel brochure', 'This concept has no connection to writing', 'A call to action always discourages readers from visiting'], 0),
   ('Which sentence sounds most like it belongs in a travel brochure?', ['Wander the cobblestone streets at sunset and taste fresh pastries from a corner bakery.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Geometry: Classifying Triangles by Sides and Angles',
  'Grade 7 Math strand: triangles can be classified by their side lengths as scalene (no equal sides), isosceles (two equal sides), or equilateral (three equal sides), and separately by their angle measures as acute, right, or obtuse.',
  [('What is a scalene triangle?', ['A triangle with no equal sides', 'A triangle with exactly two equal sides', 'A concept unrelated to geometry', 'A triangle with three equal sides'], 0),
   ('What is an isosceles triangle?', ['A triangle with exactly two equal sides', 'A triangle with no equal sides at all', 'A concept unrelated to classifying triangles', 'A triangle with three unequal angles only'], 0),
   ('What is an equilateral triangle?', ['A triangle with three equal sides', 'A triangle with no equal sides', 'A concept unrelated to triangles', 'A triangle that has four sides'], 0),
   ('What defines a right triangle?', ['It has one angle that measures exactly 90 degrees', 'It has no angles at all', 'A concept unrelated to classifying triangles by angle', 'It has three angles that are each greater than 90 degrees'], 0),
   ('What defines an obtuse triangle?', ['It has one angle greater than 90 degrees', 'It has one angle that measures exactly 90 degrees', 'A concept unrelated to triangles', 'It has three angles that are each less than 90 degrees and equal'], 0)]),
Sc('Technology: How GPS and Satellite Navigation Work',
   'Grade 7 Science strand: GPS satellites orbiting Earth continuously send timed signals to receivers on the ground, and a GPS device calculates its exact position by measuring the time delay of signals received from at least four satellites, a process called trilateration.',
   [('What do GPS satellites continuously send to receivers on the ground?', ['Timed signals', 'Physical packages', 'A concept unrelated to technology', 'Printed maps'], 0),
    ('How many satellites does a GPS receiver typically need signals from to determine its position?', ['At least four', 'Exactly one', 'A concept unrelated to GPS', 'Zero satellites are ever needed'], 0),
    ('What is the process of using signal timing from multiple satellites to determine position called?', ['Trilateration', 'Evaporation', 'A concept unrelated to satellite navigation', 'Photosynthesis'], 0),
    ('Why does a GPS device need to measure the time delay of a signal rather than just receiving it?', ['The time delay reveals the distance between the receiver and each satellite', 'Time delay has no connection to calculating distance', 'A concept unrelated to GPS', 'GPS devices never measure any kind of time delay'], 0),
    ('Why might GPS signals be weaker or less accurate inside a building or a dense forest?', ['Physical obstacles can block or interfere with the satellite signals', 'Buildings and forests always improve GPS signal accuracy', 'This concept has no relevance to science', 'GPS satellites stop transmitting signals near any obstacle'], 0)]),
SS('Social Studies: Supply Management in Canadian Agriculture',
   'Grade 7 Social Studies strand: Canadas supply management system for dairy, eggs, and poultry uses production quotas, pricing controls, and import tariffs to help stabilize farmer incomes and consumer prices, setting these sectors apart from the more open-market approach used for many other agricultural products.',
   [('Which sectors of Canadian agriculture are commonly associated with supply management?', ['Dairy, eggs, and poultry', 'Wheat and corn exclusively', 'A concept unrelated to Canadian agriculture', 'Only imported produce'], 0),
    ('What is one tool used within the supply management system?', ['Production quotas', 'Supply management uses no tools of any kind', 'A concept unrelated to social studies', 'Randomly assigned prices with no system behind them'], 0),
    ('What is one goal of the supply management system?', ['Stabilizing farmer incomes and consumer prices', 'Supply management has no goals connected to farming', 'A concept unrelated to agriculture', 'Eliminating all Canadian dairy and poultry farms'], 0),
    ('How does supply management differ from a fully open agricultural market?', ['It uses quotas and controls rather than leaving prices entirely to open competition', 'Supply management and an open market are always identical systems', 'A concept unrelated to supply management', 'An open market always involves production quotas as well'], 0),
    ('Why might import tariffs be used alongside supply management?', ['To help protect domestic producers from being undercut by cheaper imported goods', 'Import tariffs have no connection to domestic agriculture', 'This concept has no relevance to social studies', 'Tariffs are only ever applied to exported goods'], 0)]),
]),
day(166, [
L('Reading: Analyzing Tone Shifts Within a Single Text',
  'Grade 7 Language strand: tone is the attitude an author conveys toward a subject through word choice and style, and a tone shift occurs when that attitude changes partway through a text, often signaling a turning point, new information, or a change in the narrators perspective.',
  [('What is tone in a piece of writing?', ['The attitude an author conveys toward a subject', 'The exact number of words used in a text', 'A concept unrelated to reading', 'The font used to print a text'], 0),
   ('What is a tone shift?', ['A change in the authors attitude partway through a text', 'A text that has no attitude of any kind from beginning to end', 'A concept unrelated to tone shifts', 'A change in the physical size of the book'], 0),
   ('What might a sudden tone shift from lighthearted to serious signal in a story?', ['A turning point or significant new development in the plot', 'Tone shifts never signal anything meaningful in a story', 'A concept unrelated to reading', 'The story has ended and a new, unrelated story has begun'], 0),
   ('How can word choice help create a specific tone in a text?', ['Certain words carry emotional associations that shape how a passage feels', 'Word choice never has any effect on the tone of a text', 'This concept has no connection to reading', 'Every word in every language carries the exact same tone'], 0),
   ('Why might a reader pay close attention to tone shifts while reading a novel?', ['They can reveal important changes in mood, perspective, or plot direction', 'Tone shifts are always irrelevant to understanding a novel', 'This concept has no relevance to reading', 'Tone shifts only occur in poetry and never in novels'], 0)]),
M('Data Management: Constructing and Interpreting Pictographs with Scaled Symbols',
  'Grade 7 Math strand: a pictograph displays data using repeated symbols or icons, where each icon represents a set quantity called the scale, such as one icon equalling ten units, and a key or legend explains what the scale represents.',
  [('What does a pictograph use to represent data?', ['Repeated symbols or icons', 'Only numbers with no symbols at all', 'A concept unrelated to data management', 'Colours with no symbols involved'], 0),
   ('What is the scale of a pictograph?', ['The quantity that each symbol or icon represents', 'The total number of categories shown in the pictograph', 'A concept unrelated to pictographs', 'The physical size of the paper used'], 0),
   ('If each icon in a pictograph represents 10 books read, and a row shows 3 icons, how many books were read?', ['30 books', '3 books', '13 books', '10 books'], 0),
   ('What part of a pictograph explains what the scale represents?', ['The key or legend', 'The title alone, with no other explanation', 'A concept unrelated to pictographs', 'Pictographs never include any explanation of scale'], 0),
   ('Why might a half or partial icon appear in a pictograph?', ['To represent a quantity that falls between two full scale increments', 'Partial icons are never used in a pictograph', 'A concept unrelated to data management', 'A partial icon always represents zero'], 0)]),
Sc('Biology: Vestigial Structures and Evidence of Evolution',
   'Grade 7 Science strand: a vestigial structure is a body part that has lost most or all of its original function over the course of evolutionary history, such as the human appendix or wisdom teeth, and such structures provide evidence of an organisms evolutionary past.',
   [('What is a vestigial structure?', ['A body part that has lost most or all of its original function over time', 'A body part that has always served its current function perfectly', 'A concept unrelated to biology', 'A structure that appears only in newly evolved species'], 0),
    ('Which of these is often cited as an example of a vestigial structure in humans?', ['The appendix', 'The heart', 'A concept unrelated to vestigial structures', 'The lungs'], 0),
    ('What can vestigial structures provide evidence of?', ['An organisms evolutionary past', 'Nothing at all about an organisms history', 'A concept unrelated to evolution', 'Only an organisms current diet'], 0),
    ('Why might a structure become vestigial over many generations?', ['It is no longer needed for survival in a changing environment, so it gradually loses function', 'Vestigial structures always become more useful over time', 'A concept unrelated to biology', 'Structures never change in function across generations'], 0),
    ('Why do scientists consider vestigial structures useful when studying evolutionary relationships between species?', ['Similar vestigial structures in different species can suggest a shared evolutionary ancestor', 'Vestigial structures provide no useful information to scientists', 'This concept has no relevance to science', 'Vestigial structures are always unique to a single species with no relation to others'], 0)]),
SS('Social Studies: The Canadian Senate — Structure, Role, and Reform Debates',
   'Grade 7 Social Studies strand: the Senate is the upper house of Canadas Parliament, with senators appointed rather than elected, and it is intended to provide sober second thought by reviewing and revising legislation passed by the House of Commons, though its appointment process and role have long been the subject of reform debates.',
   [('How do senators typically join the Canadian Senate?', ['They are appointed rather than elected', 'They are elected directly by voters in a general election', 'A concept unrelated to the Canadian Senate', 'They inherit the position from a family member'], 0),
    ('What is the Senate often described as providing when reviewing legislation?', ['Sober second thought', 'No review of legislation at all', 'A concept unrelated to Canadian government', 'Final, unchangeable approval with no possibility of revision'], 0),
    ('Which body of Parliament typically passes legislation before it goes to the Senate?', ['The House of Commons', 'The Supreme Court', 'A concept unrelated to the Senate', 'A provincial legislature'], 0),
    ('What has long been a subject of debate regarding the Canadian Senate?', ['Its appointment process and overall role', 'The Senate has never been the subject of any debate', 'A concept unrelated to social studies', 'Whether Canada should have a House of Commons at all'], 0),
    ('Why might critics argue that an appointed Senate raises questions about democratic accountability?', ['Senators are not directly chosen by voters the way elected officials are', 'Appointed positions are always considered more democratic than elected ones', 'This concept has no relevance to social studies', 'Senators are never involved in reviewing legislation'], 0)]),
]),
day(167, [
L('Writing: Writing a Fable with a Clear Moral',
  'Grade 7 Language strand: a fable is a short story, often featuring animal characters with human traits, that teaches a specific lesson or moral, which may be stated directly at the end of the story or left for the reader to infer.',
  [('What is a fable?', ['A short story, often with animal characters, that teaches a lesson or moral', 'A lengthy novel with no clear lesson or purpose', 'A concept unrelated to writing', 'A story that must always be based on true events'], 0),
   ('What kind of characters do fables often feature?', ['Animal characters with human traits', 'Only human scientists and engineers', 'A concept unrelated to fables', 'Characters that never speak or interact'], 0),
   ('Where is the moral of a fable sometimes directly stated?', ['At the end of the story', 'A fable never includes a stated moral of any kind', 'A concept unrelated to writing a fable', 'Only in the very first sentence'], 0),
   ('Why might an author choose animal characters instead of human characters in a fable?', ['Animal characters can represent human traits in a simple, memorable way', 'Animal characters can never represent any human traits', 'This concept has no connection to writing', 'Fables are required to avoid using any characters at all'], 0),
   ('Which ending sounds most like the moral of a fable?', ['And so the tortoise learned that slow and steady effort can win in the end.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Algebra: Translating Words into Algebraic Expressions and Equations',
  'Grade 7 Math strand: translating a word problem into algebra involves identifying key words that signal an operation or an unknown quantity, such as sum, difference, product, or quotient, and then writing an algebraic expression or equation that matches the situation described.',
  [('Which word in a word problem often signals addition?', ['Sum', 'Quotient', 'A concept unrelated to algebra', 'Product'], 0),
   ('Which expression represents 5 more than a number x?', ['x plus 5', 'x minus 5', 'A concept unrelated to translating expressions', '5 minus x'], 0),
   ('Which expression represents the product of a number n and 7?', ['7 times n', 'n plus 7', 'A concept unrelated to algebra', 'n minus 7'], 0),
   ('Which equation represents the statement, three times a number is equal to 21?', ['3 times x equals 21', 'x plus 3 equals 21', 'A concept unrelated to translating word problems', '21 times x equals 3'], 0),
   ('Why is identifying key words an important first step when translating a word problem into algebra?', ['Key words reveal which operation and structure the algebraic expression should use', 'Key words never provide any useful information about a word problem', 'A concept unrelated to algebra', 'Word problems can never be translated into algebraic expressions'], 0)]),
Sc('Earth Science: Measuring Earthquakes — Magnitude and Seismographs',
   'Grade 7 Science strand: seismographs are instruments that detect and record ground motion during an earthquake, and magnitude scales measure the energy released by an earthquake, with each whole number increase on the scale representing a significantly larger release of energy.',
   [('What instrument is used to detect and record ground motion during an earthquake?', ['A seismograph', 'A barometer', 'A concept unrelated to earth science', 'A thermometer'], 0),
    ('What does an earthquakes magnitude measure?', ['The energy released by the earthquake', 'The exact number of buildings affected', 'A concept unrelated to measuring earthquakes', 'The temperature of the ground during the earthquake'], 0),
    ('What generally happens to the energy released as magnitude increases by a whole number on a magnitude scale?', ['The energy released becomes significantly larger', 'The energy released stays exactly the same', 'A concept unrelated to seismographs', 'The energy released always decreases'], 0),
    ('Why might scientists place seismographs in many different locations around the world?', ['To detect and compare ground motion from earthquakes across different regions', 'Seismographs are only ever useful in a single fixed location', 'A concept unrelated to earth science', 'Seismographs cannot function unless they are all in the same city'], 0),
    ('Why is it useful for engineers to understand earthquake magnitude when designing buildings in earthquake-prone areas?', ['It helps them design structures that can withstand the expected level of ground motion', 'Magnitude has no connection to how buildings are designed', 'This concept has no relevance to science', 'Buildings never need to account for earthquakes during construction'], 0)]),
SS('Social Studies: Hockey and Its Role in Canadian National Identity',
   'Grade 7 Social Studies strand: ice hockey has long been closely tied to Canadian culture, from community rinks and minor leagues to international competitions such as the Olympics, often serving as a unifying symbol of national pride across different regions of the country.',
   [('What winter sport has long been closely tied to Canadian culture?', ['Ice hockey', 'Cricket', 'A concept unrelated to Canadian identity', 'Rugby'], 0),
    ('Where does hockey in Canada often begin for many young players?', ['Community rinks and minor leagues', 'Hockey in Canada has no connection to local communities', 'A concept unrelated to hockey and identity', 'Only large professional stadiums are ever used'], 0),
    ('At what type of international event has Canadian hockey often been a source of national pride?', ['The Olympics', 'International trade summits', 'A concept unrelated to hockey', 'World literature conferences'], 0),
    ('Why might hockey be described as a unifying symbol across different regions of Canada?', ['It is widely followed and celebrated in communities across the country', 'Hockey is followed in only one small region of Canada', 'A concept unrelated to social studies', 'Hockey has no cultural significance anywhere in Canada'], 0),
    ('Why might a sport become closely connected to a countrys sense of national identity?', ['Shared enthusiasm for the sport can create a sense of common pride and belonging', 'Sports never have any connection to how people view their national identity', 'This concept has no relevance to social studies', 'National identity can never be expressed through cultural activities'], 0)]),
]),
day(168, [
L('Media Literacy: Analyzing Reality Television and Its Construction',
  'Grade 7 Language strand: although reality television appears unscripted, it is often shaped through editing, camera angles, and situations arranged by producers, so media-literate viewers should think critically about how the reality shown on screen has been constructed for entertainment.',
  [('What is one way reality television is often shaped by producers?', ['Through editing, camera angles, and arranged situations', 'Reality television is never shaped or influenced in any way', 'A concept unrelated to media literacy', 'Only by the unscripted choices of the people appearing on screen'], 0),
   ('Why might a media-literate viewer question how realistic a reality show truly is?', ['Editing and staged situations can shape what appears on screen', 'Reality shows are always filmed with absolutely no editing of any kind', 'A concept unrelated to reality television', 'Every moment shown is always exactly as it happened with no changes'], 0),
   ('What technique can editing use to shape how a viewer perceives a moment on a reality show?', ['Selecting and arranging footage to emphasize a particular story or emotion', 'Editing has no effect on how viewers perceive a scene', 'A concept unrelated to media literacy', 'Editing can only ever remove sound from a scene'], 0),
   ('Why might producers arrange certain situations on a reality show in advance?', ['To create more dramatic or entertaining moments for viewers', 'Producers are never involved in planning any part of a reality show', 'This concept has no connection to media literacy', 'Arranged situations always make a show less entertaining'], 0),
   ('Why is it useful for viewers to think critically about the construction of reality television?', ['It helps them understand that what they see has been shaped for entertainment rather than being purely spontaneous', 'Critical thinking has no value when watching any type of television', 'This concept has no relevance to media literacy', 'Reality television requires no thought or analysis of any kind'], 0)]),
M('Geometry: Calculating the Area of Composite 2D Shapes',
  'Grade 7 Math strand: the area of a composite two-dimensional shape can be found by breaking the figure into simpler shapes, such as rectangles, triangles, or circles, calculating the area of each simpler shape separately, and then adding or subtracting these areas as needed.',
  [('What is the first general step in finding the area of a composite 2D shape?', ['Break the figure into simpler shapes, such as rectangles or triangles', 'Immediately guess the total area with no calculation', 'A concept unrelated to geometry', 'Ignore the shape entirely and use a fixed formula'], 0),
   ('If a composite shape is made of a rectangle with area 24 square units and a triangle with area 6 square units added onto it, what is the total area?', ['30 square units', '18 square units', '24 square units', '6 square units'], 0),
   ('Why might subtracting an area be necessary when finding the area of some composite shapes?', ['A smaller shape, such as a hole or cutout, may need to be removed from a larger shape', 'Subtracting area is never necessary when working with composite shapes', 'A concept unrelated to composite 2D shapes', 'All composite shapes only ever require addition'], 0),
   ('If a square with area 16 square units has a circular hole with area 4 square units cut out of it, what is the remaining area?', ['12 square units', '20 square units', '16 square units', '4 square units'], 0),
   ('Why is breaking a composite shape into simpler shapes a useful problem-solving strategy?', ['It allows familiar area formulas to be applied to each simpler part', 'Composite shapes can never be broken into simpler shapes', 'A concept unrelated to geometry', 'Area formulas only ever apply to an entire composite shape at once'], 0)]),
Sc('Biology: Animal Classification — Vertebrates and Invertebrates',
   'Grade 7 Science strand: animals are broadly classified as vertebrates, which have a backbone, including mammals, birds, fish, reptiles, and amphibians, or invertebrates, which lack a backbone, including insects, worms, and mollusks, and invertebrates make up the vast majority of animal species on Earth.',
   [('What defines a vertebrate?', ['It has a backbone', 'It has no backbone at all', 'A concept unrelated to animal classification', 'It always lives exclusively underwater'], 0),
    ('What defines an invertebrate?', ['It lacks a backbone', 'It always has a backbone', 'A concept unrelated to biology', 'It is always larger than a vertebrate'], 0),
    ('Which of these groups is classified as vertebrates?', ['Mammals, birds, fish, reptiles, and amphibians', 'Insects, worms, and mollusks', 'A concept unrelated to vertebrate classification', 'Only single-celled organisms'], 0),
    ('Which of these is an example of an invertebrate?', ['An insect', 'A bird', 'A concept unrelated to animal classification', 'A mammal'], 0),
    ('Why might scientists say invertebrates make up the vast majority of animal species on Earth?', ['Groups like insects alone include an enormous number of distinct species', 'Vertebrates actually outnumber invertebrates by a wide margin', 'This concept has no relevance to science', 'Every animal species on Earth is classified as a vertebrate'], 0)]),
SS('Social Studies: The Massey Commission and Canadian Culture',
   'Grade 7 Social Studies strand: the Massey Commission, active from 1949 to 1951, studied the state of the arts, letters, and sciences in Canada, and its recommendations led to the creation of the Canada Council for the Arts and helped shape federal support for Canadian culture and broadcasting.',
   [('Roughly when was the Massey Commission active?', ['1949 to 1951', '1917 to 1919', 'A concept unrelated to Canadian history', '1982 to 1984'], 0),
    ('What areas did the Massey Commission study in Canada?', ['The arts, letters, and sciences', 'Only military spending', 'A concept unrelated to the Massey Commission', 'Only foreign trade policy'], 0),
    ('What organization was created as a result of the Massey Commissions recommendations?', ['The Canada Council for the Arts', 'The Bank of Canada', 'A concept unrelated to Canadian culture', 'The Royal Canadian Mint'], 0),
    ('What broader area of Canadian life did the Massey Commissions recommendations help shape?', ['Federal support for Canadian culture and broadcasting', 'The Massey Commission had no lasting effect on Canada', 'A concept unrelated to social studies', 'Only Canadas system of provincial taxation'], 0),
    ('Why might a government commission studying the arts lead to long-term support for Canadian culture?', ['Its recommendations can result in institutions and funding that continue to support culture for years afterward', 'Government commissions never lead to any lasting institutions or funding', 'This concept has no relevance to social studies', 'Studying the arts has no connection to how a government funds culture'], 0)]),
]),
day(169, [
L('Vocabulary: Synonyms, Antonyms, and Shades of Meaning',
  'Grade 7 Language strand: synonyms are words with similar meanings and antonyms are words with opposite meanings, and skilled writers choose among near-synonyms based on subtle shades of meaning, such as connotation, intensity, or formality, to communicate precisely.',
  [('What are synonyms?', ['Words with similar meanings', 'Words with completely opposite meanings', 'A concept unrelated to vocabulary', 'Words that are always spelled identically'], 0),
   ('What are antonyms?', ['Words with opposite meanings', 'Words with identical meanings', 'A concept unrelated to antonyms', 'Words that never appear in the same sentence'], 0),
   ('Which word could serve as an antonym for the word generous?', ['Stingy', 'Kind', 'A concept unrelated to antonyms', 'Giving'], 0),
   ('Why might a writer choose the word furious instead of the near-synonym annoyed?', ['Furious conveys a much stronger degree of anger than annoyed', 'Furious and annoyed always mean exactly the same thing with no difference', 'A concept unrelated to vocabulary', 'Word choice never affects the intensity conveyed in writing'], 0),
   ('Why is understanding shades of meaning among synonyms useful for precise writing?', ['It helps a writer select the word that most accurately conveys the intended tone and degree', 'Every synonym for a word conveys the exact same tone and degree', 'This concept has no relevance to vocabulary', 'Precise writing never depends on which synonym is chosen'], 0)]),
M('Probability: The Law of Large Numbers',
  'Grade 7 Math strand: the law of large numbers states that as the number of trials in a probability experiment increases, the experimental probability tends to get closer and closer to the theoretical probability.',
  [('What does the law of large numbers describe?', ['How experimental probability tends to approach theoretical probability as trials increase', 'A rule that only applies to numbers greater than one million', 'A concept unrelated to probability', 'A guarantee that any single trial will always match the theoretical probability'], 0),
   ('If you flip a fair coin many, many times, what does the law of large numbers predict about the proportion of heads?', ['It will get closer to 50 percent as the number of flips increases', 'It will always equal exactly 50 percent after just two flips', 'A concept unrelated to the law of large numbers', 'It will move further away from 50 percent as flips increase'], 0),
   ('Why might the experimental probability from only 5 coin flips differ noticeably from the theoretical probability?', ['A small number of trials is more likely to show random variation from the expected outcome', 'Small numbers of trials always exactly match theoretical probability', 'A concept unrelated to probability', '5 flips is already considered a very large number of trials'], 0),
   ('Why is the law of large numbers useful for insurance companies estimating risk?', ['Analyzing a very large number of cases helps produce more reliable probability estimates', 'The law of large numbers has no connection to estimating risk', 'A concept unrelated to probability', 'Insurance companies never rely on probability of any kind'], 0),
   ('What generally happens to the reliability of an experimental probability as the number of trials increases?', ['It generally becomes more reliable and closer to the theoretical probability', 'It generally becomes less reliable as trials increase', 'A concept unrelated to the law of large numbers', 'The number of trials has no effect on reliability at all'], 0)]),
Sc('Physics: Gravity and Free Fall',
   'Grade 7 Science strand: gravity is a force that pulls objects toward each other, and near Earths surface, objects in free fall accelerate toward the ground at a constant rate, regardless of their mass, as long as air resistance is ignored.',
   [('What is gravity?', ['A force that pulls objects toward each other', 'A force that only ever pushes objects apart', 'A concept unrelated to physics', 'A force that exists only in outer space'], 0),
    ('If air resistance is ignored, how does the acceleration of a falling object relate to its mass?', ['Objects accelerate at the same constant rate regardless of their mass', 'Heavier objects always accelerate much faster than lighter objects', 'A concept unrelated to gravity', 'Lighter objects always accelerate much faster than heavier objects'], 0),
   ('What term describes an object falling and accelerating due to gravity alone?', ['Free fall', 'Terminal stillness', 'A concept unrelated to gravity and free fall', 'Static motion'], 0),
   ('Why might a feather fall more slowly than a rock when dropped in normal air, even though gravity pulls on both equally?', ['Air resistance affects the feather more due to its shape and lower density', 'Gravity pulls harder on the rock than it does on the feather', 'A concept unrelated to physics', 'The feather is not actually affected by gravity at all'], 0),
   ('Why would a feather and a rock fall at the same rate if dropped together in a vacuum?', ['With no air resistance present, gravity alone determines the acceleration of both objects equally', 'A vacuum causes gravity to stop acting on objects entirely', 'This concept has no relevance to science', 'Only heavier objects are affected by gravity inside a vacuum'], 0)]),
SS('Social Studies: The Canadian Museum for Human Rights',
   'Grade 7 Social Studies strand: the Canadian Museum for Human Rights, which opened in Winnipeg in 2014, is dedicated to the exploration, education, and reflection on human rights themes, and it was the first Canadian national museum located outside of the Ottawa region.',
   [('In what city is the Canadian Museum for Human Rights located?', ['Winnipeg', 'Ottawa', 'A concept unrelated to Canadian museums', 'Halifax'], 0),
    ('In what year did the Canadian Museum for Human Rights open?', ['2014', '1949', '1982', '1917'], 0),
    ('What is the Canadian Museum for Human Rights dedicated to?', ['Exploration, education, and reflection on human rights themes', 'Displaying only historical military equipment', 'A concept unrelated to the museum', 'Promoting a single, unrelated industry'], 0),
    ('What made this museum notable among Canadian national museums when it opened?', ['It was the first Canadian national museum located outside of the Ottawa region', 'It was the very first museum ever built in Canada', 'A concept unrelated to social studies', 'It was built with no connection to any national theme'], 0),
    ('Why might a country choose to build a museum focused specifically on human rights?', ['To educate the public and encourage reflection on important human rights issues', 'Museums focused on human rights serve no educational purpose', 'This concept has no relevance to social studies', 'Human rights have no connection to museums or public education'], 0)]),
]),
day(170, [
L('Language Review: Verb Tenses, Inferences, and Media Literacy',
  'Grade 7 Language strand review: students revisit the perfect verb tenses, restrictive and non-restrictive modifiers, making inferences from text evidence, writing a fable with a clear moral, and analyzing reality television.',
  [('What does the present perfect tense generally show?', ['An action that started in the past and still has relevance now', 'An action that will never happen', 'A concept unrelated to grammar', 'An action that can only happen in the future'], 0),
   ('What does a restrictive modifier do?', ['Provides essential information needed to identify the noun it describes', 'Adds information that could be removed with no change in meaning', 'A concept unrelated to grammar', 'Always begins a sentence with a comma'], 0),
   ('What is an inference?', ['A conclusion drawn by combining text evidence with background knowledge', 'A fact that is always stated directly and explicitly in the text', 'A concept unrelated to reading', 'A random guess with no connection to the text at all'], 0),
   ('What is a fable?', ['A short story, often with animal characters, that teaches a lesson or moral', 'A lengthy novel with no clear lesson or purpose', 'A concept unrelated to writing', 'A story that must always be based on true events'], 0),
   ('What is one way reality television is often shaped by producers?', ['Through editing, camera angles, and arranged situations', 'Reality television is never shaped or influenced in any way', 'A concept unrelated to media literacy', 'Only by the unscripted choices of the people appearing on screen'], 0)]),
M('Math Review: Point-Slope Form, Probability, and Geometry',
  'Grade 7 Math strand review: students revisit point-slope form, elapsed time conversions, prime factorization, classifying triangles, and the law of large numbers.',
  [('What two pieces of information does point-slope form require to write the equation of a line?', ['The slope and the coordinates of one known point on the line', 'Only the y-intercept of the line', 'A concept unrelated to algebra', 'Two unrelated equations with no shared point'], 0),
   ('What is 19:45 in 24-hour time converted to 12-hour time?', ['7:45 PM', '7:45 AM', '9:45 PM', '5:45 PM'], 0),
   ('What is the prime factorization of 12?', ['2 times 2 times 3', '2 times 6', '3 times 4', '1 times 12'], 0),
   ('What is a scalene triangle?', ['A triangle with no equal sides', 'A triangle with exactly two equal sides', 'A concept unrelated to geometry', 'A triangle with three equal sides'], 0),
   ('What does the law of large numbers describe?', ['How experimental probability tends to approach theoretical probability as trials increase', 'A rule that only applies to numbers greater than one million', 'A concept unrelated to probability', 'A guarantee that any single trial will always match the theoretical probability'], 0)]),
Sc('Science Review: Eclipses, Atmosphere, and Conservation Laws',
   'Grade 7 Science strand review: students revisit solar and lunar eclipses, the layers of the atmosphere, the law of conservation of mass, the law of conservation of energy, and gravity and free fall.',
   [('What happens during a solar eclipse?', ['The moon passes between the sun and Earth, blocking some or all sunlight', 'Earth passes between the sun and the moon', 'A concept unrelated to astronomy', 'The sun disappears permanently from the sky'], 0),
    ('In which layer of the atmosphere does most weather occur?', ['The troposphere', 'The stratosphere', 'A concept unrelated to earth science', 'The exosphere'], 0),
    ('What does the law of conservation of mass state?', ['Matter cannot be created or destroyed during a chemical reaction', 'Matter is always created during a chemical reaction', 'A concept unrelated to chemistry', 'Mass always disappears completely during a reaction'], 0),
    ('What does the law of conservation of energy state?', ['Energy cannot be created or destroyed, only transformed from one form to another', 'Energy is constantly being created out of nothing', 'A concept unrelated to physics', 'Energy always disappears completely over time'], 0),
    ('If air resistance is ignored, how does the acceleration of a falling object relate to its mass?', ['Objects accelerate at the same constant rate regardless of their mass', 'Heavier objects always accelerate much faster than lighter objects', 'A concept unrelated to gravity', 'Lighter objects always accelerate much faster than heavier objects'], 0)]),
SS('Social Studies Review: Halifax, Policing, and Canadian Institutions',
   'Grade 7 Social Studies strand review: students revisit the founding of Halifax, the immigration points system, the RCMP and Canadian policing history, the Canadian Senate, and the Canadian Museum for Human Rights.',
   [('In what year was Halifax founded?', ['1749', '1867', '1917', '1608'], 0),
    ('In what year was Canadas points-based immigration system introduced?', ['1967', '1917', '1949', '1982'], 0),
    ('What was the RCMP originally known as when it was formed in 1873?', ['The North-West Mounted Police', 'The Royal Canadian Navy', 'A concept unrelated to Canadian policing', 'The Halifax Harbour Guard'], 0),
    ('How do senators typically join the Canadian Senate?', ['They are appointed rather than elected', 'They are elected directly by voters in a general election', 'A concept unrelated to the Canadian Senate', 'They inherit the position from a family member'], 0),
    ('In what city is the Canadian Museum for Human Rights located?', ['Winnipeg', 'Ottawa', 'A concept unrelated to Canadian museums', 'Halifax'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_161_170)
    append_to(7, g7_161_170)
