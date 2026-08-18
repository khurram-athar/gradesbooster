#!/usr/bin/env python3
"""Grade 6, Days 171-180 -- extends Grade 6 from 170 to 180 days. Modeled
exactly on gen_grade6_days161_170.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-170
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: split
infinitives and common usage errors, understanding satire in literature,
writing an advice column, regional dialects and word variation, using
signposting language in oral presentations, recognizing stereotypes in
literature and media, ellipsis and its uses in writing, comparing
reporting across international news sources, and writing a toast or
special occasion speech for Language; introduction to binary numbers,
interpreting pictographs and symbol keys, the golden ratio in art and
architecture, the Fibonacci sequence in nature, using area models to
represent probability, logic puzzles and deductive reasoning, estimating
using order of magnitude, converting between Celsius and Fahrenheit
temperatures, and understanding Roman numerals for Math; hydrogen fuel
cells as an energy source, osmosis and diffusion in cells, cellular
respiration, the Doppler effect and changes in sound, black holes, caves
and how they form, solutions suspensions and colloids, how refrigerators
and heat pumps move heat, and the science of fermentation and yeast for
Science; and Sir John A. Macdonald as Canadas first prime minister, how
the provinces and territories joined confederation over time, the
North-West Rebellion and Louis Riel, the cod moratorium and the collapse
of Atlantic fisheries, the role of an ombudsman, the Royal Canadian Mint,
how a bill becomes a law in Canada, the CRTC and Canadian content rules,
and government borrowing and Canadas national debt for Social Studies --
none of those exact ideas appear in Days 1-170. Day 180 is a review day
across all four subjects, matching the end-of-batch pattern used in every
prior 10-day batch; its four review titles (Language Review: Grammar,
Genres, and Oral Presentation Skills / Math Review: Number Systems, Data,
and Geometric Patterns / Science Review: Energy Sources, Cells, and
Astronomy / Social Studies Review: Canadian Leaders, Confederation, and
Government Institutions) are worded distinctly from every earlier review
days titles even though all are review days. No embedded ASCII apostrophe
or double-quote characters are used anywhere in title/summary/question/
option text -- apostrophes are dropped entirely (e.g. "Canadas" not
"Canada's"), matching the rest of Grade 6.

Usage: python3 gen_grade6_days171_180.py
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


g6_171_180 = [
day(171, [
L('Grammar: Split Infinitives and Common Usage Errors',
  'Grade 6 Language strand: a split infinitive occurs when a word, often an adverb, is placed between to and the base verb, as in to quickly run, and while once considered incorrect, split infinitives are now widely accepted in modern English usage.',
  [('What is a split infinitive?', ['A word placed between to and the base verb of an infinitive', 'A verb with no subject at all', 'A sentence missing end punctuation', 'A word that has two opposite meanings'], 0),
   ('Which sentence contains a split infinitive?', ['He wants to boldly go where no one has gone before.', 'He wants to go boldly where no one has gone before.', 'Boldly, he wants to go where no one has gone before.', 'He boldly wants to go where no one has gone before.'], 0),
   ('How did traditional grammarians often view split infinitives?', ['As an error that careful writers should avoid', 'As the only correct way to form an infinitive', 'As a punctuation mark rather than a grammar issue', 'As something that only appears in questions'], 0),
   ('Why do many modern grammar guides now accept split infinitives?', ['Placing the adverb there can make a sentence sound more natural and clear', 'Split infinitives always make a sentence harder to understand', 'Modern guides no longer allow adverbs in any sentence', 'Infinitives can no longer be modified by adverbs at all'], 0),
   ('Why is it useful for a writer to recognize a split infinitive even though it is now widely accepted?', ['Recognizing the construction lets a writer choose word order deliberately for clarity or emphasis', 'Recognizing split infinitives has no effect on how a sentence is written', 'A writer should never use an infinitive of any kind', 'Split infinitives are the only acceptable way to build a sentence'], 0)]),
M('Number Sense: Introduction to Binary Numbers',
  'Grade 6 Math strand: the binary number system uses only two digits, 0 and 1, and each place value represents a power of two, forming the foundation of how digital devices store and process information.',
  [('What two digits are used in the binary number system?', ['0 and 1', '0 and 2', '1 and 2', '0, 1, and 2'], 0),
   ('What does each place value in a binary number represent?', ['A power of two', 'A power of ten', 'A power of five', 'A power of one hundred'], 0),
   ('What is the decimal value of the binary number 101?', ['5', '3', '10', '101'], 0),
   ('Why is the binary number system especially important for digital devices?', ['Digital circuits can easily represent two states, such as on and off, matching the two binary digits', 'Digital devices cannot process numbers written in binary', 'Binary numbers can only represent the digit zero', 'Computers use exactly ten digits to store information'], 0),
   ('Why might understanding binary help explain how computers store information?', ['It shows how combinations of just two digits can represent any number or piece of data', 'Binary numbers have no connection to how computers work', 'Computers store information using letters instead of numbers', 'Binary numbers can only be used for counting, never for storage'], 0)]),
Sc('Science: Hydrogen Fuel Cells as an Energy Source',
   'Grade 6 Science strand: a hydrogen fuel cell combines hydrogen and oxygen to produce electricity, with water as the only byproduct, offering a clean alternative to burning fossil fuels for power.',
   [('What two gases does a hydrogen fuel cell combine to produce electricity?', ['Hydrogen and oxygen', 'Hydrogen and nitrogen', 'Carbon dioxide and oxygen', 'Nitrogen and oxygen'], 0),
    ('What is the main byproduct produced by a hydrogen fuel cell?', ['Water', 'Carbon dioxide', 'Smoke', 'Ash'], 0),
    ('Why are hydrogen fuel cells considered a clean energy source?', ['They produce electricity without releasing pollutants such as carbon dioxide into the air', 'They release large amounts of smoke and ash into the air', 'They require burning coal to operate', 'They produce more pollution than fossil fuels'], 0),
    ('Why might hydrogen fuel cells be useful for powering vehicles?', ['They can generate electricity for a motor while producing only water as waste', 'They cannot generate enough electricity to power a motor', 'They require the vehicle to burn gasoline as well', 'They produce the same pollutants as a gasoline engine'], 0),
    ('Why is producing and storing hydrogen safely an important challenge for this technology?', ['Hydrogen gas is highly flammable and requires careful handling and storage', 'Hydrogen gas is completely inert and never requires any safety precautions', 'Hydrogen is not used at all in fuel cell technology', 'Storing hydrogen has no connection to the safety of a fuel cell system'], 0)]),
SS('Social Studies: Sir John A. Macdonald — Canadas First Prime Minister',
   'Grade 6 Social Studies strand: Sir John A. Macdonald became Canadas first prime minister in 1867 and played a leading role in negotiating Confederation and expanding the young country westward through projects such as the transcontinental railway.',
   [('What role did Sir John A. Macdonald hold beginning in 1867?', ['Canadas first prime minister', 'Canadas first governor general', 'The first premier of Ontario', 'The first mayor of Ottawa'], 0),
    ('What major role did Macdonald play in Canadian history before becoming prime minister?', ['Negotiating Confederation', 'Leading the League of Nations', 'Founding the United Nations', 'Signing the Statute of Westminster'], 0),
    ('What large infrastructure project did Macdonald support to help expand Canada westward?', ['A transcontinental railway', 'A national airline', 'A system of canals to Europe', 'An underground subway system'], 0),
    ('Why might a transcontinental railway have been important for a newly formed country like Canada?', ['It helped connect distant regions, encouraging settlement, trade, and a sense of national unity', 'Railways had no effect on connecting different regions of a country', 'Canada already had a fully connected transportation network in 1867', 'The railway was built only for scenic tourism purposes'], 0),
    ('Why do historians continue to study both the achievements and the controversies of Macdonalds time as prime minister?', ['A fuller picture of his policies and their consequences helps explain the founding and growth of Canada', 'Historians have found nothing significant to study about this period', 'Macdonalds prime ministership had no lasting effect on Canada', 'Only his personal life is considered historically important'], 0)]),
]),
day(172, [
L('Reading: Understanding Satire in Literature',
  'Grade 6 Language strand: satire is a literary technique that uses humour, irony, or exaggeration to criticize peoples foolishness or a societys flaws, often with the goal of encouraging change.',
  [('What is satire?', ['A literary technique that uses humour, irony, or exaggeration to criticize flaws', 'A type of poem with no hidden meaning', 'A factual report with no opinion included', 'A story written only for young children'], 0),
   ('What is one common tool used in satire?', ['Exaggeration', 'Strict factual accuracy only', 'Complete avoidance of humour', 'A formal bibliography'], 0),
   ('What is a common goal of satire?', ['Encouraging change by pointing out flaws in society or behaviour', 'Praising every aspect of society without criticism', 'Avoiding any commentary on human behaviour', 'Providing only technical instructions'], 0),
   ('Why might a writer choose satire instead of a direct, serious complaint to criticize something?', ['Humour and exaggeration can make a criticism more engaging and memorable for readers', 'Satire always makes a criticism less clear than a direct complaint', 'Readers never respond to humour in written criticism', 'A direct complaint is always more effective than satire'], 0),
   ('Why might a reader need background knowledge about a topic to fully understand a piece of satire?', ['Recognizing what is being exaggerated or mocked often depends on knowing the real situation being referenced', 'Satire never refers to any real situation or issue', 'Background knowledge always prevents a reader from understanding satire', 'Satire is always completely obvious without any context'], 0)]),
M('Data Management: Interpreting Pictographs and Symbol Keys',
  'Grade 6 Math strand: a pictograph uses repeated pictures or symbols to represent data, and a symbol key explains how many units of data each picture represents.',
  [('What does a pictograph use to represent data?', ['Repeated pictures or symbols', 'Only numbers with no images', 'A single unlabelled line', 'Coloured regions with no key'], 0),
   ('What does the symbol key on a pictograph explain?', ['How many units of data each picture represents', 'The title of the pictograph only', 'The names of the people who collected the data', 'The colour scheme used in the pictograph'], 0),
   ('If the key shows one symbol equals 5 items, and a row has 3 symbols, how many items does that row represent?', ['15', '8', '3', '5'], 0),
   ('Why might a pictograph use a symbol representing more than one unit, such as one symbol for 10 items?', ['It keeps the pictograph compact and readable when the data values are large', 'Using a symbol for more than one unit is never allowed', 'A pictograph can only display data using a scale of exactly one', 'Larger values always require removing the symbol key entirely'], 0),
   ('Why is it important to check the symbol key carefully before interpreting a pictograph?', ['Misreading the key can lead to significant errors when calculating the actual values shown', 'The symbol key never affects how the data should be interpreted', 'Every pictograph always uses the same key with no need to check it', 'Pictographs do not require any key to be understood correctly'], 0)]),
Sc('Science: Osmosis and Diffusion in Cells',
   'Grade 6 Science strand: diffusion is the movement of particles from an area of higher concentration to lower concentration, while osmosis is the diffusion of water specifically across a cells membrane.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from low to high concentration only', 'A process that only happens outside of living cells', 'The complete stopping of particle movement'], 0),
    ('What is osmosis?', ['The diffusion of water specifically across a cells membrane', 'The diffusion of solid particles through a rock', 'A process that only occurs in gases', 'The movement of light through a cell'], 0),
    ('Why does diffusion happen naturally without added energy?', ['Particles naturally move to spread out evenly from areas of high to low concentration', 'Particles always require an external energy source to move at all', 'Diffusion only occurs when a cell is not alive', 'Particles move randomly toward areas of higher concentration only'], 0),
    ('Why is osmosis important for a living cells survival?', ['It allows water to move into and out of a cell to help maintain proper internal conditions', 'Cells never need water to survive', 'Osmosis prevents any water from ever entering a cell', 'A cells membrane blocks all movement of water at all times'], 0),
    ('Why might a plant wilt if it does not receive enough water?', ['Without enough water entering its cells through osmosis, the cells lose the pressure that keeps the plant upright', 'Plants do not rely on water movement through their cells at all', 'Wilting has no connection to water movement inside plant cells', 'Osmosis only affects animal cells, never plant cells'], 0)]),
SS('Social Studies: How the Provinces and Territories Joined Confederation Over Time',
   'Grade 6 Social Studies strand: Canada began in 1867 with four provinces and grew over more than a century as additional provinces and territories joined, including Manitoba, British Columbia, Prince Edward Island, and eventually Newfoundland and Labrador in 1949.',
   [('How many provinces made up Canada at Confederation in 1867?', ['Four', 'Ten', 'Two', 'Seven'], 0),
    ('In what decade did British Columbia join Confederation?', ['The 1870s', 'The 1770s', 'The 1970s', 'The 1670s'], 0),
    ('Which province was the last to join Canada, doing so in 1949?', ['Newfoundland and Labrador', 'Alberta', 'Saskatchewan', 'Manitoba'], 0),
    ('Why did Canada continue to grow in size and number of provinces after 1867?', ['Additional colonies and territories negotiated their own terms to join Confederation over time', 'Every part of modern Canada joined Confederation on the exact same day in 1867', 'Canada has never added any new provinces since 1867', 'Provinces can only ever be removed from Canada, never added'], 0),
    ('Why might different provinces have joined Confederation for different reasons, such as economic benefits or railway promises?', ['Each colony weighed its own interests, so agreements often included specific incentives to encourage joining', 'Every province joined for the exact same single reason with no negotiation', 'Provinces never received any specific incentives to join Confederation', 'Confederation agreements were identical for every province with no variation'], 0)]),
]),
day(173, [
L('Writing: Writing an Advice Column',
  'Grade 6 Language strand: an advice column responds to a readers question or problem with thoughtful, practical suggestions, using a supportive tone appropriate for the person seeking help.',
  [('What does an advice column typically respond to?', ['A readers question or problem', 'A weather report', 'A sports score', 'A recipe request'], 0),
   ('What kind of suggestions should an advice column offer?', ['Thoughtful, practical suggestions', 'Suggestions with no connection to the question asked', 'Only vague statements with no useful detail', 'Suggestions copied directly from another persons letter'], 0),
   ('Why is tone especially important when writing an advice column?', ['A supportive tone helps the reader feel understood and more willing to accept the advice', 'Tone has no effect on how advice is received', 'An advice column should always sound harsh and critical', 'Readers never care about the tone of an advice column'], 0),
   ('Why might an advice columnist ask clarifying questions or consider multiple possible solutions before responding?', ['A well-considered response is more likely to genuinely help the person with their specific situation', 'Considering more than one solution always makes advice less helpful', 'Advice columns are never expected to be genuinely helpful', 'Clarifying questions have no value when giving advice'], 0),
   ('Why should an advice column balance honesty with kindness when addressing a sensitive problem?', ['Honest advice delivered with care is more likely to be both useful and respectfully received', 'Kindness should never be part of an advice column', 'Honesty always makes an advice column less useful', 'Sensitive problems should never be addressed in an advice column'], 0)]),
M('Geometry: The Golden Ratio in Art and Architecture',
  'Grade 6 Math strand: the golden ratio is a special number, approximately 1.618, that appears when a line is divided so the ratio of the whole to the larger part equals the ratio of the larger part to the smaller part, and it has been used by artists and architects for centuries.',
  [('What is the approximate value of the golden ratio?', ['1.618', '3.14', '2.718', '0.618 only'], 0),
   ('What does the golden ratio describe about a divided line?', ['The ratio of the whole to the larger part equals the ratio of the larger part to the smaller part', 'The line must always be divided into two equal halves', 'The golden ratio only applies to circles, never to lines', 'The larger part is always exactly twice the smaller part'], 0),
   ('Who has historically used the golden ratio in their work?', ['Artists and architects', 'Only professional athletes', 'Only musicians composing songs', 'Only weather forecasters'], 0),
   ('Why might a rectangle whose sides follow the golden ratio be considered visually pleasing by many people?', ['Its proportions create a sense of balance that many viewers find naturally appealing', 'Golden ratio rectangles are always considered unattractive', 'The golden ratio has no connection to how shapes appear to viewers', 'Only perfect squares can ever be visually pleasing'], 0),
   ('Why might the golden ratio also be connected to patterns found in nature, such as spiral shells?', ['Certain natural growth patterns happen to produce proportions close to the golden ratio', 'Nature never produces any mathematical patterns', 'The golden ratio only exists in human-made objects', 'Spiral shells always grow using a completely random, unrelated pattern'], 0)]),
Sc('Science: Cellular Respiration — How Cells Release Energy',
   'Grade 6 Science strand: cellular respiration is the process by which cells break down glucose using oxygen to release energy, producing carbon dioxide and water as byproducts.',
   [('What does cellular respiration break down to release energy?', ['Glucose', 'Oxygen only', 'Carbon dioxide only', 'Water only'], 0),
    ('What gas do cells use during cellular respiration?', ['Oxygen', 'Nitrogen', 'Hydrogen', 'Helium'], 0),
    ('What are the two main byproducts produced by cellular respiration?', ['Carbon dioxide and water', 'Oxygen and glucose', 'Nitrogen and hydrogen', 'Salt and sugar'], 0),
    ('Why do living organisms need cellular respiration to survive?', ['It provides the energy cells need to carry out their basic functions', 'Cells can function normally without any source of energy', 'Cellular respiration removes all energy from a cell', 'Living organisms never need energy from their cells'], 0),
    ('Why might cellular respiration be thought of as roughly the opposite process to photosynthesis?', ['Cellular respiration uses oxygen and glucose to release energy while producing carbon dioxide and water, while photosynthesis uses carbon dioxide and water to store energy while producing oxygen and glucose', 'Cellular respiration and photosynthesis are identical processes with no differences', 'Photosynthesis only occurs in animal cells, never in plants', 'Cellular respiration produces glucose instead of breaking it down'], 0)]),
SS('Social Studies: The North-West Rebellion and Louis Riel',
   'Grade 6 Social Studies strand: the North-West Rebellion of 1885, led in part by Louis Riel, arose from Metis and First Nations grievances over land rights and government treatment in the North-West Territories.',
   [('In what year did the North-West Rebellion take place?', ['1885', '1867', '1812', '1931'], 0),
    ('Who was a key leader associated with the North-West Rebellion?', ['Louis Riel', 'John A. Macdonald', 'Lester B. Pearson', 'David Thompson'], 0),
    ('What were among the main grievances that led to the North-West Rebellion?', ['Land rights and government treatment of Metis and First Nations peoples', 'A disagreement over international trade tariffs', 'A dispute about the location of the national capital', 'A disagreement over the design of the national flag'], 0),
    ('Why might unresolved land disputes have led to armed conflict in the North-West Territories?', ['When peaceful negotiations failed to address grievances, tensions escalated into open resistance', 'Land disputes in the region were always resolved through negotiation with no conflict', 'The government agreed immediately to every demand made by Metis leaders', 'The North-West Territories had no connection to land or settlement issues'], 0),
    ('Why does the North-West Rebellion remain an important event for understanding Metis history in Canada?', ['It highlights long-standing struggles over land, identity, and self-government that still resonate today', 'The rebellion had no lasting impact on Metis communities', 'Metis history has no connection to events in the North-West Territories', 'The event is remembered only for its effect on railway construction'], 0)]),
]),
day(174, [
L('Vocabulary: Regional Dialects and Word Variation',
  'Grade 6 Language strand: a dialect is a variety of a language spoken in a particular region or by a particular group, often featuring different vocabulary, pronunciation, or expressions for the same idea.',
  [('What is a dialect?', ['A variety of a language spoken in a particular region or group', 'A completely separate language with no connection to another', 'A type of punctuation mark', 'A word with only one possible meaning'], 0),
   ('What might differ between two dialects of the same language?', ['Vocabulary, pronunciation, or expressions', 'The alphabet used to write the language', 'Whether the language has any words at all', 'The number of speakers required to use it'], 0),
   ('Why might people from different regions use different words for the same object?', ['Regional history, culture, and influence from other languages can shape local vocabulary', 'All regions that speak the same language always use identical vocabulary', 'Word choice is never influenced by where a person lives', 'Regional dialects only affect written language, never spoken language'], 0),
   ('Why is it useful for a reader to recognize dialect differences when reading a story set in another region?', ['Recognizing dialect helps a reader understand characters and setting more fully, even when word choices are unfamiliar', 'Dialect differences never affect how a story should be understood', 'A story set in another region never uses any regional language', 'Readers should ignore all regional vocabulary while reading'], 0),
   ('Why might a dialect be an important part of a communitys identity?', ['Distinct ways of speaking can reflect shared history, culture, and belonging within a community', 'Dialects have no connection to community identity or culture', 'Every community in the world speaks in exactly the same way', 'A dialect is simply an incorrect way of speaking a language'], 0)]),
M('Patterning and Algebra: The Fibonacci Sequence in Nature',
  'Grade 6 Math strand: the Fibonacci sequence is a pattern of numbers where each term is the sum of the two terms before it, starting 0, 1, 1, 2, 3, 5, 8, and it appears in natural patterns such as the arrangement of seeds in a sunflower.',
  [('How is each term of the Fibonacci sequence calculated?', ['By adding the two terms that come before it', 'By multiplying the term before it by two', 'By subtracting one from the term before it', 'By dividing the previous term by two'], 0),
   ('What are the first six terms of the Fibonacci sequence starting from 0?', ['0, 1, 1, 2, 3, 5', '0, 1, 2, 3, 4, 5', '1, 2, 3, 5, 8, 13', '0, 2, 4, 6, 8, 10'], 0),
   ('What comes after 3, 5, 8 in the Fibonacci sequence?', ['13', '11', '10', '15'], 0),
   ('Where can the Fibonacci sequence be observed in nature?', ['In the arrangement of seeds in a sunflower', 'In the number of legs on every insect', 'In the exact temperature of ocean water', 'In the number of clouds in the sky'], 0),
   ('Why might scientists find it interesting that a mathematical pattern like the Fibonacci sequence appears repeatedly in living things?', ['It suggests that efficient natural growth patterns can align closely with simple mathematical rules', 'Mathematical patterns never appear anywhere in the natural world', 'The Fibonacci sequence has no connection to how plants grow', 'Living things grow using patterns that are always completely random'], 0)]),
Sc('Science: The Doppler Effect and Changes in Sound',
   'Grade 6 Science strand: the Doppler effect is the change in pitch heard when a sound source moves toward or away from a listener, such as a siren sounding higher as it approaches and lower as it moves away.',
   [('What is the Doppler effect?', ['The change in pitch heard when a sound source moves toward or away from a listener', 'A change in the volume of a sound with no connection to motion', 'The complete disappearance of sound over long distances', 'A change in the colour of light only'], 0),
    ('What happens to a sirens pitch as it approaches a listener?', ['It sounds higher', 'It sounds lower', 'It disappears completely', 'It stays exactly the same'], 0),
    ('What happens to a sirens pitch as it moves away from a listener?', ['It sounds lower', 'It sounds higher', 'It becomes silent instantly', 'It stays exactly the same'], 0),
    ('Why does the pitch of a moving sound source change for a listener?', ['The motion compresses or stretches the sound waves reaching the listener, changing their frequency', 'Sound waves never change based on the motion of their source', 'The listener always hears the exact same pitch regardless of motion', 'Pitch is determined only by the volume of a sound'], 0),
    ('Why is the Doppler effect useful for technologies such as weather radar or measuring the speed of vehicles?', ['Measuring the shift in frequency of reflected waves can reveal information about motion and speed', 'The Doppler effect has no practical application in technology', 'Weather radar never relies on any properties of sound or waves', 'The speed of a moving object cannot be measured using wave frequency'], 0)]),
SS('Social Studies: The Cod Moratorium and the Collapse of Atlantic Fisheries',
   'Grade 6 Social Studies strand: in 1992, the Canadian government declared a moratorium on cod fishing off Newfoundland after decades of overfishing caused fish populations to collapse, resulting in the loss of thousands of jobs in coastal communities.',
   [('In what year did Canada declare a moratorium on cod fishing off Newfoundland?', ['1992', '1867', '1931', '1949'], 0),
    ('What caused the collapse of cod fish populations off Newfoundland?', ['Decades of overfishing', 'A sudden drop in ocean temperature only', 'A single large oil spill', 'The construction of a new highway'], 0),
    ('What was the immediate effect of the moratorium on coastal communities?', ['The loss of thousands of fishing-related jobs', 'An immediate increase in fishing jobs', 'No effect on employment at all', 'A sudden rise in cod populations'], 0),
    ('Why might a government choose to halt an entire industry, such as cod fishing, despite the economic hardship it causes?', ['Allowing severely depleted fish populations to recover may be necessary to prevent permanent long-term collapse', 'Halting an industry always has no effect on the environment', 'Fish populations always recover on their own with no need for a moratorium', 'The moratorium was intended to permanently end fishing in Canada'], 0),
    ('Why does the cod moratorium remain an important lesson about managing natural resources?', ['It shows how overusing a resource without careful limits can devastate both an ecosystem and the communities that depend on it', 'The event proved that overfishing has no lasting effect on fish populations', 'Natural resources can never be depleted no matter how they are used', 'The moratorium had no connection to how resources are managed today'], 0)]),
]),
day(175, [
L('Oral Communication: Using Signposting Language in Presentations',
  'Grade 6 Language strand: signposting language consists of transitional words and phrases, such as first, next, in contrast, and to conclude, that help an audience follow the structure of a spoken presentation.',
  [('What is signposting language?', ['Transitional words and phrases that help an audience follow a presentations structure', 'Language used only in written essays, never in speech', 'A set of hand gestures used instead of words', 'Vocabulary that has no connection to organization'], 0),
   ('Which of these is an example of signposting language?', ['To conclude', 'Elephant', 'Backpack', 'Umbrella'], 0),
   ('Why might a speaker use the phrase in contrast during a presentation?', ['To signal that a different or opposing idea is about to be presented', 'To indicate that the presentation has ended', 'To introduce a completely unrelated topic with no connection', 'To repeat the exact same point already made'], 0),
   ('Why is signposting language especially helpful in a spoken presentation compared to a written text?', ['Listeners cannot reread a spoken presentation, so clear verbal cues help them follow the structure in real time', 'Signposting language is never useful during a spoken presentation', 'Listeners can always pause and reread spoken words just like a written text', 'Spoken presentations never need any indication of structure'], 0),
   ('Why might a presenter plan their signposting language in advance rather than choosing it randomly while speaking?', ['Planned transitions help ensure the presentation flows logically and stays organized', 'Randomly chosen transitions always make a presentation clearer', 'Planning transitions in advance has no effect on a presentations organization', 'Signposting language should never be planned before a presentation'], 0)]),
M('Probability: Using Area Models to Represent Probability',
  'Grade 6 Math strand: an area model represents probability using the area of a rectangle or square divided into regions, where the size of each region corresponds to the likelihood of an outcome.',
  [('What does an area model use to represent probability?', ['The area of a rectangle or square divided into regions', 'A single point plotted on a number line', 'A list of numbers with no visual representation', 'A single unlabelled circle with no divisions'], 0),
   ('In an area model, what does the size of a region represent?', ['The likelihood of that outcome occurring', 'The colour of the outcome only', 'The order in which outcomes occur', 'The name of the outcome only'], 0),
   ('If a rectangle is divided so that one region covers one-quarter of the total area, what is the probability represented by that region?', ['One-quarter', 'One-half', 'One-third', 'The entire probability'], 0),
   ('Why might an area model be useful for representing the probability of two combined events?', ['It can visually show how the sample space divides based on multiple possible outcomes happening together', 'Area models can only represent a single outcome at a time', 'Combined events can never be shown using an area model', 'An area model removes all information about probability'], 0),
   ('Why might a student prefer an area model over a written list when solving certain probability problems?', ['A visual model can make it easier to see how portions of the total probability relate to each other', 'A written list always provides more visual information than an area model', 'Area models cannot be used for any type of probability problem', 'Visual models never help with understanding probability'], 0)]),
Sc('Science: Black Holes — An Introduction',
   'Grade 6 Science strand: a black hole is a region of space with such strong gravitational pull that nothing, not even light, can escape from it, often forming when a massive star collapses at the end of its life.',
   [('What is a black hole?', ['A region of space with gravitational pull so strong that nothing can escape it', 'A bright star visible from Earth without a telescope', 'A type of planet found only in our solar system', 'A cloud of gas with no gravitational pull'], 0),
    ('What can escape from a black hole?', ['Nothing, not even light', 'Only light, but nothing else', 'Only sound waves', 'Everything can escape freely'], 0),
    ('How can a black hole form?', ['When a massive star collapses at the end of its life', 'When a small asteroid breaks apart', 'When two planets collide gently', 'When a comet passes near the sun'], 0),
    ('Why is it difficult for scientists to directly observe a black hole?', ['Because no light escapes a black hole, it cannot be seen directly and must be detected through its effects on nearby matter', 'Black holes emit extremely bright light that is easy to see with the naked eye', 'Scientists have never attempted to study black holes', 'Black holes have no effect on any surrounding matter or light'], 0),
    ('Why might studying black holes help scientists understand extreme conditions in the universe?', ['Black holes involve some of the strongest gravitational forces known, testing the limits of our understanding of physics', 'Black holes represent the weakest gravitational force found anywhere in space', 'Studying black holes provides no useful scientific information', 'Black holes are identical in every way to ordinary stars'], 0)]),
SS('Social Studies: The Role of an Ombudsman in Protecting Citizens Rights',
   'Grade 6 Social Studies strand: an ombudsman is an independent official who investigates complaints from citizens against government departments or organizations, working to resolve disputes fairly without taking sides.',
   [('What does an ombudsman investigate?', ['Complaints from citizens against government departments or organizations', 'Only complaints made by government employees', 'Weather-related emergencies', 'Traffic violations on public roads'], 0),
    ('What quality is important for an ombudsman to have while resolving disputes?', ['Independence and fairness, without taking sides', 'Loyalty to only one side of a dispute', 'The ability to ignore citizen complaints entirely', 'Authority to make new laws without government approval'], 0),
    ('Who can typically bring a complaint to an ombudsman?', ['A citizen who has a concern about a government department or organization', 'Only elected government officials', 'Only large businesses', 'Only foreign governments'], 0),
    ('Why might a government create an independent ombudsman role rather than relying only on internal government reviews?', ['An independent official can investigate complaints more impartially, without pressure from within the department being reviewed', 'Internal government reviews are always more fair than an independent investigation', 'An ombudsman has no advantage over an internal review process', 'Citizens never need an independent way to raise concerns about government actions'], 0),
    ('Why is the ombudsmans role considered an important part of government accountability?', ['It gives citizens a formal, independent channel to seek fair resolution when they believe they have been treated unfairly', 'The ombudsman has no connection to how citizens interact with government', 'Government accountability does not require any independent oversight', 'Citizens are never allowed to raise concerns about government departments'], 0)]),
]),
day(176, [
L('Reading: Recognizing Stereotypes in Literature and Media',
  'Grade 6 Language strand: a stereotype is an oversimplified and often inaccurate belief about a group of people, and recognizing stereotypes in literature and media helps readers think critically about how groups are represented.',
  [('What is a stereotype?', ['An oversimplified and often inaccurate belief about a group of people', 'A detailed and fully accurate description of one specific individual', 'A type of punctuation used in dialogue', 'A literary device used only in poetry'], 0),
   ('Why might recognizing stereotypes in a story be important for a reader?', ['It helps readers think critically about how different groups are represented', 'Stereotypes never appear in literature or media', 'Recognizing stereotypes always makes a story less meaningful', 'Readers never need to think critically about representation'], 0),
   ('What is one way a stereotype can affect how a character is portrayed in a story?', ['It can reduce a character to a single, oversimplified trait rather than showing complexity', 'It always makes a character more realistic and complex', 'Stereotypes have no effect on how characters are written', 'A stereotype guarantees that a character will be portrayed fairly'], 0),
   ('Why might authors sometimes intentionally use a stereotype and then challenge it within a story?', ['Subverting a stereotype can highlight its inaccuracy and encourage readers to question their assumptions', 'Authors never use stereotypes for any narrative purpose', 'Challenging a stereotype always confuses readers with no benefit', 'Stereotypes can never be challenged once they appear in a story'], 0),
   ('Why is it valuable to compare how different books or shows portray the same group of people?', ['Comparing multiple portrayals can reveal whether a group is being shown with variety and depth or through repeated stereotypes', 'Comparing portrayals across different works never reveals anything useful', 'Every book or show portrays the same group in an identical way', 'Media never influences how people think about different groups'], 0)]),
M('Math: Logic Puzzles and Deductive Reasoning',
  'Grade 6 Math strand: deductive reasoning uses given facts and logical steps to reach a certain conclusion, and logic puzzles often require organizing clues systematically, such as with a grid, to determine a unique solution.',
  [('What does deductive reasoning use to reach a conclusion?', ['Given facts and logical steps', 'Random guessing with no facts', 'Only personal opinions', 'A conclusion chosen before any facts are considered'], 0),
   ('What tool is often used to organize clues systematically when solving a logic puzzle?', ['A grid', 'A calculator only', 'A protractor', 'A thermometer'], 0),
   ('If all clues in a logic puzzle are true and used correctly, what should the solution be?', ['A unique solution that satisfies every clue', 'Several different solutions that all work equally well', 'No solution at all', 'A solution based only on guessing'], 0),
   ('Why is it useful to record what has already been ruled out while solving a logic puzzle?', ['Tracking eliminated possibilities helps narrow down the remaining valid options systematically', 'Ruling out possibilities always makes a puzzle more difficult to solve', 'Recording eliminated options has no effect on solving a logic puzzle', 'A logic puzzle can only be solved by ignoring earlier clues'], 0),
   ('Why might solving logic puzzles help build skills useful in mathematics and everyday problem solving?', ['Practising structured, step-by-step reasoning strengthens the ability to draw valid conclusions from given information', 'Logic puzzles have no connection to mathematical thinking', 'Deductive reasoning skills cannot be improved through practice', 'Problem solving in everyday life never relies on logical reasoning'], 0)]),
Sc('Science: Caves and How They Form',
   'Grade 6 Science strand: many caves form when slightly acidic water slowly dissolves soluble rock such as limestone over thousands of years, gradually carving out underground passages and chambers.',
   [('What type of rock is commonly dissolved to form caves?', ['Limestone', 'Granite', 'Obsidian', 'Basalt'], 0),
    ('What causes water to slowly dissolve rock in cave formation?', ['The water is slightly acidic', 'The water is extremely hot', 'The water contains no minerals at all', 'The water is completely frozen'], 0),
    ('About how long can it take for a large cave system to form?', ['Thousands of years', 'A single day', 'A few hours', 'One week'], 0),
    ('Why do many caves contain formations such as stalactites and stalagmites?', ['Minerals dissolved in dripping water are slowly deposited, building up rock formations over time', 'Stalactites and stalagmites form instantly with no mineral deposits involved', 'Cave formations are unrelated to water or minerals', 'Caves never contain any additional rock formations'], 0),
    ('Why might scientists study caves to learn about environmental conditions from long ago?', ['Layers of mineral deposits in caves can preserve a record of past climate and water conditions', 'Caves contain no information about environmental history', 'Cave formations always form in a single instant with no preserved record', 'Studying caves only reveals information about current temperatures'], 0)]),
SS('Social Studies: The Royal Canadian Mint and How Coins Are Made',
   'Grade 6 Social Studies strand: the Royal Canadian Mint is the federal Crown corporation responsible for producing Canadas circulation coins, using metal blanks that are stamped with official designs before being distributed for everyday use.',
   [('What is the Royal Canadian Mint responsible for producing?', ['Canadas circulation coins', 'Canadas paper banknotes', 'Canadas postage stamps', 'Canadas passports'], 0),
    ('What type of organization is the Royal Canadian Mint?', ['A federal Crown corporation', 'A private international bank', 'A provincial ministry', 'A foreign-owned company'], 0),
    ('What happens to metal blanks during the coin-making process?', ['They are stamped with official designs', 'They are melted into paper currency', 'They are shipped overseas without any design', 'They are used to print stamps'], 0),
    ('Why might a government choose to have a single official mint produce all of its circulation coins?', ['A centralized mint helps ensure consistency, security, and control over the currency supply', 'Having a single mint has no effect on the reliability of a countrys currency', 'Multiple unrelated organizations always produce a countrys coins with no oversight', 'Coins can be produced without any official design or standard'], 0),
    ('Why is it important for a countrys coins to include security features that are difficult to copy?', ['Security features help prevent counterfeiting and maintain public trust in the currency', 'Security features have no effect on preventing counterfeit coins', 'Counterfeiting coins is not considered a concern for a countrys currency', 'Coins do not require any special features to be trusted by the public'], 0)]),
]),
day(177, [
L('Grammar: Ellipsis and Its Uses in Writing',
  'Grade 6 Language strand: an ellipsis, written as three dots, can show that words have been omitted from a quotation, indicate a pause or trailing off in dialogue, or build suspense in a narrative.',
  [('How many dots make up an ellipsis?', ['Three', 'Two', 'Four', 'One'], 0),
   ('What can an ellipsis indicate when used in a quotation?', ['That words have been omitted from the original text', 'That the entire quotation is false', 'That the quotation must be read aloud', 'That the quotation has been translated into another language'], 0),
   ('What can an ellipsis show when used in dialogue?', ['A pause or trailing off in speech', 'That a character has stopped speaking permanently', 'That the sentence is a question', 'That the dialogue is written in the wrong tense'], 0),
   ('Why might a writer use an ellipsis to build suspense in a narrative?', ['A trailing pause can create anticipation about what a character will say or do next', 'An ellipsis always removes all suspense from a narrative', 'Ellipses can only be used in nonfiction writing', 'Suspense can never be created using punctuation of any kind'], 0),
   ('Why is it important to use an ellipsis carefully when shortening a quotation?', ['Removing words carelessly could change the original meaning of the quotation', 'An ellipsis can never affect the meaning of a quotation', 'Quotations should never be shortened for any reason', 'Using an ellipsis always makes a quotation more accurate'], 0)]),
M('Number Sense: Estimating Using Order of Magnitude',
  'Grade 6 Math strand: order of magnitude estimation involves rounding a number to the nearest power of ten to quickly compare sizes or check whether a calculated answer is reasonable.',
  [('What does order of magnitude estimation involve?', ['Rounding a number to the nearest power of ten', 'Rounding a number to the nearest whole number only', 'Ignoring all digits in a number', 'Multiplying a number by exactly one hundred'], 0),
   ('What is the order of magnitude of the number 4,700?', ['Thousands (10 to the power of 3)', 'Hundreds (10 to the power of 2)', 'Tens (10 to the power of 1)', 'Millions (10 to the power of 6)'], 0),
   ('Why might order of magnitude estimation be useful before performing a precise calculation?', ['It helps quickly check whether a final calculated answer is reasonable', 'It always produces a more accurate result than a precise calculation', 'It removes the need to ever calculate an exact answer', 'Order of magnitude estimation cannot be used to check calculations'], 0),
   ('Why might scientists use order of magnitude comparisons when discussing very large or very small quantities, such as distances in space?', ['It allows quick comparisons of scale without needing to work with extremely long precise numbers', 'Scientists never need to compare very large or very small quantities', 'Order of magnitude comparisons are only used for everyday shopping totals', 'Precise numbers are always easier to compare than order of magnitude estimates'], 0),
   ('Why could a calculated answer that is off by an entire order of magnitude suggest a mistake was made?', ['Such a large difference usually signals an error, such as a misplaced decimal point or incorrect operation', 'A difference of an entire order of magnitude is always considered a normal and expected result', 'Order of magnitude has no connection to identifying calculation errors', 'A correct calculation can never be reasonably estimated in advance'], 0)]),
Sc('Science: Solutions, Suspensions, and Colloids',
   'Grade 6 Science strand: a solution is a mixture where one substance dissolves completely into another, a suspension contains particles that will settle out over time, and a colloid contains particles spread evenly but not fully dissolved.',
   [('What happens to a substance that dissolves completely in a solution?', ['It spreads evenly throughout the other substance and does not settle out', 'It sinks immediately to the bottom of the container', 'It remains completely separate from the other substance', 'It evaporates instantly upon mixing'], 0),
    ('What happens to the particles in a suspension over time?', ['They settle out of the mixture', 'They dissolve completely and permanently', 'They immediately turn into a gas', 'They disappear without a trace'], 0),
    ('Which of these is an example of a suspension?', ['Muddy water with visible particles that settle', 'Salt fully dissolved in water', 'Sugar fully dissolved in tea', 'Air, which is a mixture of gases'], 0),
    ('Why might milk be classified as a colloid rather than a true solution?', ['Its particles are spread evenly throughout the liquid but are not fully dissolved at a molecular level', 'Milk contains no particles of any kind', 'Milk always settles completely into layers like a suspension', 'Colloids and solutions are always exactly the same type of mixture'], 0),
    ('Why is it useful to be able to classify a mixture as a solution, suspension, or colloid?', ['Understanding the type of mixture helps predict its behaviour, such as whether it will settle or stay evenly mixed', 'Classifying mixtures has no practical use in science', 'All mixtures behave in exactly the same way regardless of type', 'Solutions, suspensions, and colloids cannot be told apart in any way'], 0)]),
SS('Social Studies: How a Bill Becomes a Law in Canada',
   'Grade 6 Social Studies strand: a bill must pass through several stages, including readings and votes in the House of Commons and the Senate, before receiving royal assent and becoming a law in Canada.',
   [('What is a bill before it becomes a law?', ['A proposed piece of legislation', 'A completed law with no further steps needed', 'A tax receipt', 'A court ruling'], 0),
    ('Which two chambers must typically approve a bill before it can become law in Canada?', ['The House of Commons and the Senate', 'The Supreme Court and the House of Commons only', 'Only the provincial legislature', 'Only the municipal council'], 0),
    ('What must a bill receive after being passed by both chambers before it becomes law?', ['Royal assent', 'A public referendum vote', 'Approval from another country', 'A newspaper announcement'], 0),
    ('Why does a bill go through multiple readings and votes before becoming law?', ['This process allows for debate, review, and potential changes before a law takes effect', 'Multiple readings are just a formality with no real purpose', 'A bill becomes law immediately after being proposed, with no further steps', 'Debating a bill has no effect on the final law'], 0),
    ('Why might requiring approval from more than one legislative body help create more carefully considered laws?', ['Multiple levels of review can catch potential problems and encourage broader agreement before a law is finalized', 'Requiring more than one approval step always delays laws with no benefit', 'A single legislative body always produces the most carefully considered laws', 'Additional review steps have no effect on the quality of a law'], 0)]),
]),
day(178, [
L('Media Literacy: Comparing Reporting Across International News Sources',
  'Grade 6 Language strand: comparing how different countries news sources report on the same global event can reveal differences in emphasis, framing, and perspective shaped by each sources audience and context.',
  [('What can comparing international news sources about the same event reveal?', ['Differences in emphasis, framing, and perspective', 'That every news source always reports identical information', 'That international news never covers the same events', 'That comparing sources provides no useful information'], 0),
   ('What might shape how a news source frames a particular story?', ['Its intended audience and surrounding context', 'The time of day the story is published', 'The number of photographs included', 'The length of the headline only'], 0),
   ('Why might two countries news outlets report the same international event with different levels of detail?', ['Each outlet may consider certain details more relevant or important to its own audience', 'All news outlets around the world always include the exact same details', 'The amount of detail in a report never depends on the audience', 'International events are never reported with varying levels of detail'], 0),
   ('Why is it valuable for a critical reader to seek out multiple international perspectives on a major world event?', ['Multiple perspectives can provide a more complete and balanced understanding than any single source alone', 'Seeking multiple perspectives always creates more confusion with no benefit', 'A single international news source always provides a fully complete picture', 'Comparing sources from different countries has no value for understanding an event'], 0),
   ('Why might language and translation differences add another layer of complexity when comparing international reporting?', ['Subtle differences in word choice during translation can shift the tone or meaning conveyed to readers', 'Translation never changes the tone or meaning of a news report', 'All languages express ideas in exactly the same way with no variation', 'International news reporting never involves any translation at all'], 0)]),
M('Measurement: Converting Between Celsius and Fahrenheit Temperatures',
  'Grade 6 Math strand: Celsius and Fahrenheit are two temperature scales, and a temperature can be converted from Celsius to Fahrenheit using the formula F equals C multiplied by 9 over 5, plus 32.',
  [('What formula converts a temperature from Celsius to Fahrenheit?', ['F equals C multiplied by 9 over 5, plus 32', 'F equals C plus 32 only', 'F equals C divided by 2', 'F equals C multiplied by 100'], 0),
   ('What is 0 degrees Celsius converted to Fahrenheit?', ['32 degrees Fahrenheit', '0 degrees Fahrenheit', '100 degrees Fahrenheit', '212 degrees Fahrenheit'], 0),
   ('What is 100 degrees Celsius, the boiling point of water, converted to Fahrenheit?', ['212 degrees Fahrenheit', '100 degrees Fahrenheit', '32 degrees Fahrenheit', '180 degrees Fahrenheit'], 0),
   ('Why might it be useful to know how to convert between Celsius and Fahrenheit?', ['Different countries commonly use different temperature scales, so conversion helps with understanding weather or measurements abroad', 'Celsius and Fahrenheit always give the exact same numerical reading', 'Temperature conversion has no practical use in everyday life', 'Only scientists ever need to understand temperature scales'], 0),
   ('Why does the Celsius to Fahrenheit formula include both a multiplication and an addition step?', ['The scales have different starting points and different sized degree units, so both adjustments are needed for an accurate conversion', 'Only a single addition step is ever needed to convert between the two scales', 'Celsius and Fahrenheit use identical starting points and degree sizes', 'The formula for conversion never requires any multiplication'], 0)]),
Sc('Science: How Refrigerators and Heat Pumps Move Heat',
   'Grade 6 Science strand: a refrigerator uses a cycle of compressing and expanding a special fluid to absorb heat from inside its compartment and release that heat outside, a process similar to how a heat pump can warm or cool a building.',
   [('What does a refrigerator remove from the inside of its compartment?', ['Heat', 'Cold air only', 'Light', 'Sound'], 0),
    ('What kind of substance does a refrigerator use to absorb and release heat?', ['A special fluid called a refrigerant', 'Only ordinary tap water', 'Solid ice blocks only', 'Compressed air with no fluid involved'], 0),
    ('What is a heat pump able to do for a building?', ['Warm or cool it by moving heat rather than generating it directly', 'Only ever warm a building, never cool it', 'Only ever cool a building, never warm it', 'Create heat without moving it from anywhere'], 0),
    ('Why does a refrigerator feel warm on the outside, such as near its back panel, while the inside stays cold?', ['Heat removed from inside the refrigerator is released into the surrounding air outside', 'Refrigerators never produce any heat on their exterior surfaces', 'The inside and outside of a refrigerator are never at different temperatures', 'Heat is created inside the refrigerator rather than removed from it'], 0),
    ('Why might a heat pump be considered a more energy-efficient way to heat a building compared to some other heating methods?', ['Moving existing heat from one place to another can require less energy than generating new heat directly', 'Heat pumps always use more energy than any other heating method', 'Moving heat from place to place has no effect on energy efficiency', 'Generating new heat directly always uses less energy than moving existing heat'], 0)]),
SS('Social Studies: The CRTC and Canadian Content Rules in Broadcasting',
   'Grade 6 Social Studies strand: the Canadian Radio-television and Telecommunications Commission, or CRTC, regulates broadcasting in Canada, including rules that require a certain amount of Canadian content on radio and television.',
   [('What does the acronym CRTC stand for?', ['The Canadian Radio-television and Telecommunications Commission', 'The Canadian Rural Transportation and Trade Council', 'The Central Regional Television Coalition', 'The Canadian Research and Technology Committee'], 0),
    ('What does the CRTC regulate in Canada?', ['Broadcasting, including radio and television', 'Provincial highway construction', 'International trade tariffs', 'The Canadian court system'], 0),
    ('What do Canadian content rules require of broadcasters?', ['That a certain amount of Canadian content be included in programming', 'That all programming come exclusively from other countries', 'That broadcasters never air any Canadian-made content', 'That television stations broadcast only in one specific language'], 0),
    ('Why might a government create rules requiring a minimum amount of Canadian content in broadcasting?', ['Such rules can help support Canadian artists, storytellers, and industries while promoting Canadian culture', 'Content rules are intended to eliminate all Canadian-made programming', 'Broadcasting content has no connection to supporting a countrys culture or industries', 'Canadian content rules apply only to countries other than Canada'], 0),
    ('Why might regulating broadcasting be considered an important role for a government in the modern media landscape?', ['Broadcasting reaches large audiences and can shape public understanding, making oversight important for fairness and accountability', 'Broadcasting has no influence on how the public understands information', 'Government oversight of broadcasting was never considered necessary in Canada', 'Regulating broadcasting has no connection to protecting Canadian culture or industries'], 0)]),
]),
day(179, [
L('Writing: Writing a Toast or Special Occasion Speech',
  'Grade 6 Language strand: a toast or special occasion speech is a short, warm address given to celebrate an event or honour a person, often combining a brief story or memory with well wishes for the future.',
  [('What is the purpose of a toast or special occasion speech?', ['To celebrate an event or honour a person', 'To provide detailed technical instructions', 'To argue against an opposing point of view', 'To summarize a news report'], 0),
   ('What does a toast often combine with well wishes for the future?', ['A brief story or memory', 'A list of unrelated statistics', 'A detailed weather forecast', 'A set of legal terms'], 0),
   ('Why is it important for a toast or special occasion speech to be relatively short?', ['A concise speech helps hold the audiences attention and suits the celebratory mood of the occasion', 'Toasts are always expected to be extremely long and detailed', 'Length has no effect on how well an audience receives a speech', 'A short speech always fails to properly honour a person or event'], 0),
   ('Why might a speaker include a specific personal memory rather than only general praise in a toast?', ['A specific memory can make the speech feel more genuine, memorable, and personally meaningful', 'Specific memories always make a toast feel less sincere', 'General praise is always more meaningful than a specific memory', 'Personal memories have no place in a special occasion speech'], 0),
   ('Why should a speaker consider their audience and the tone of the occasion when writing a toast?', ['Matching the tone of the speech to the occasion helps ensure the message is well received by those listening', 'The audience and occasion never influence how a toast should be written', 'A toast should always use the same tone regardless of the event', 'Considering the occasion makes a speech less effective'], 0)]),
M('Number Sense: Understanding Roman Numerals',
  'Grade 6 Math strand: Roman numerals use letters such as I, V, X, L, C, D, and M to represent numbers, combining and sometimes subtracting values based on the order in which the letters appear.',
  [('Which letter represents the number 10 in Roman numerals?', ['X', 'I', 'V', 'L'], 0),
   ('What number does the Roman numeral IV represent?', ['4', '6', '9', '11'], 0),
   ('What number does the Roman numeral XII represent?', ['12', '8', '22', '2'], 0),
   ('Why does placing a smaller numeral before a larger one, such as in IX, indicate subtraction?', ['The Roman numeral system uses this placement rule to represent values that are one less than the larger numeral', 'Placing a smaller numeral before a larger one always means addition instead', 'The order of numerals never affects the value in Roman numerals', 'Roman numerals never use subtraction in their system'], 0),
   ('Why might Roman numerals still be used today, such as on clock faces or for naming events like the Olympics?', ['They provide a traditional, decorative way to display numbers even though the Hindu-Arabic system is used for calculations', 'Roman numerals are used today because they are easier to calculate with than modern numbers', 'Roman numerals have completely replaced the modern number system worldwide', 'Roman numerals are no longer used for any purpose in the modern world'], 0)]),
Sc('Science: The Science of Fermentation and Yeast',
   'Grade 6 Science strand: fermentation is a process in which microorganisms such as yeast break down sugars and release carbon dioxide and other byproducts, a reaction used in baking bread and producing certain foods.',
   [('What do microorganisms such as yeast break down during fermentation?', ['Sugars', 'Metals', 'Rocks', 'Plastics'], 0),
    ('What gas is released as a byproduct of fermentation by yeast?', ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Helium'], 0),
    ('How does fermentation help bread dough rise?', ['Carbon dioxide released during fermentation forms bubbles that expand the dough', 'Fermentation removes all the air from the dough', 'Yeast makes the dough colder, causing it to expand', 'Fermentation has no effect on bread dough at all'], 0),
    ('Why might warm temperatures speed up the fermentation process in bread making?', ['Yeast is more active and reproduces faster within a certain warm temperature range', 'Warm temperatures always stop yeast from functioning entirely', 'Fermentation only occurs at extremely cold temperatures', 'Temperature has no effect on how quickly yeast ferments sugar'], 0),
    ('Why is fermentation considered useful in food production beyond just baking bread?', ['It is also used to produce foods and beverages by breaking down sugars in controlled ways', 'Fermentation is only ever used for a single type of food product', 'Fermentation removes all nutritional value from food', 'Fermentation has no practical uses in food production'], 0)]),
SS('Social Studies: Government Borrowing and Canadas National Debt',
   'Grade 6 Social Studies strand: a government sometimes spends more money than it collects in revenue, borrowing funds to cover the difference, and the total amount owed over time is known as the national debt.',
   [('What is the national debt?', ['The total amount of money a government owes after borrowing over time', 'The amount of money citizens owe to each other', 'A tax collected only once per year', 'The total value of all goods produced in a country'], 0),
    ('Why might a government choose to borrow money?', ['It is spending more money than it currently collects in revenue', 'Governments never need to borrow any money', 'Borrowing money is required even when a government has a surplus', 'Borrowing is only done to reduce the amount of government spending'], 0),
    ('What term describes government spending exceeding its revenue in a single year?', ['A budget deficit', 'A budget surplus', 'A trade agreement', 'A tax refund'], 0),
    ('Why might a government choose to borrow money to fund large projects, such as building infrastructure, rather than waiting to collect enough revenue first?', ['Borrowing allows important projects to begin sooner, with the cost repaid gradually over time', 'Governments are never permitted to spend money on infrastructure projects', 'Borrowing money always eliminates the need to repay any of it', 'Waiting to collect revenue always allows projects to begin more quickly than borrowing'], 0),
    ('Why do economists often pay close attention to the size of a countrys national debt compared to the size of its economy?', ['This comparison helps indicate whether the debt level is manageable or could create future financial challenges', 'The size of a national debt has no connection to a countrys economic health', 'National debt is always considered equally serious regardless of the size of the economy', 'Economists never consider a countrys debt when studying its economy'], 0)]),
]),
day(180, [
L('Language Review: Grammar, Genres, and Oral Presentation Skills',
  'Grade 6 Language strand review: students revisit split infinitives, satire in literature, writing an advice column, regional dialects, and signposting language in presentations.',
  [('What is a split infinitive?', ['A word placed between to and the base verb of an infinitive', 'A verb with no subject at all', 'A sentence missing end punctuation', 'A word that has two opposite meanings'], 0),
   ('What is satire?', ['A literary technique that uses humour, irony, or exaggeration to criticize flaws', 'A type of poem with no hidden meaning', 'A factual report with no opinion included', 'A story written only for young children'], 0),
   ('What does an advice column typically respond to?', ['A readers question or problem', 'A weather report', 'A sports score', 'A recipe request'], 0),
   ('What is a dialect?', ['A variety of a language spoken in a particular region or group', 'A completely separate language with no connection to another', 'A type of punctuation mark', 'A word with only one possible meaning'], 0),
   ('What is signposting language?', ['Transitional words and phrases that help an audience follow a presentations structure', 'Language used only in written essays, never in speech', 'A set of hand gestures used instead of words', 'Vocabulary that has no connection to organization'], 0)]),
M('Math Review: Number Systems, Data, and Geometric Patterns',
  'Grade 6 Math strand review: students revisit binary numbers, pictographs, the golden ratio, the Fibonacci sequence, and area models for probability.',
  [('What two digits are used in the binary number system?', ['0 and 1', '0 and 2', '1 and 2', '0, 1, and 2'], 0),
   ('What does a pictograph use to represent data?', ['Repeated pictures or symbols', 'Only numbers with no images', 'A single unlabelled line', 'Coloured regions with no key'], 0),
   ('What is the approximate value of the golden ratio?', ['1.618', '3.14', '2.718', '0.618 only'], 0),
   ('How is each term of the Fibonacci sequence calculated?', ['By adding the two terms that come before it', 'By multiplying the term before it by two', 'By subtracting one from the term before it', 'By dividing the previous term by two'], 0),
   ('What does an area model use to represent probability?', ['The area of a rectangle or square divided into regions', 'A single point plotted on a number line', 'A list of numbers with no visual representation', 'A single unlabelled circle with no divisions'], 0)]),
Sc('Science Review: Energy Sources, Cells, and Astronomy',
   'Grade 6 Science strand review: students revisit hydrogen fuel cells, osmosis and diffusion, cellular respiration, the Doppler effect, and black holes.',
   [('What two gases does a hydrogen fuel cell combine to produce electricity?', ['Hydrogen and oxygen', 'Hydrogen and nitrogen', 'Carbon dioxide and oxygen', 'Nitrogen and oxygen'], 0),
    ('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from low to high concentration only', 'A process that only happens outside of living cells', 'The complete stopping of particle movement'], 0),
    ('What does cellular respiration break down to release energy?', ['Glucose', 'Oxygen only', 'Carbon dioxide only', 'Water only'], 0),
    ('What is the Doppler effect?', ['The change in pitch heard when a sound source moves toward or away from a listener', 'A change in the volume of a sound with no connection to motion', 'The complete disappearance of sound over long distances', 'A change in the colour of light only'], 0),
    ('What is a black hole?', ['A region of space with gravitational pull so strong that nothing can escape it', 'A bright star visible from Earth without a telescope', 'A type of planet found only in our solar system', 'A cloud of gas with no gravitational pull'], 0)]),
SS('Social Studies Review: Canadian Leaders, Confederation, and Government Institutions',
   'Grade 6 Social Studies strand review: students revisit Sir John A. Macdonald, the growth of Confederation, the North-West Rebellion, the cod moratorium, and the role of an ombudsman.',
   [('What role did Sir John A. Macdonald hold beginning in 1867?', ['Canadas first prime minister', 'Canadas first governor general', 'The first premier of Ontario', 'The first mayor of Ottawa'], 0),
    ('How many provinces made up Canada at Confederation in 1867?', ['Four', 'Ten', 'Two', 'Seven'], 0),
    ('In what year did the North-West Rebellion take place?', ['1885', '1867', '1812', '1931'], 0),
    ('In what year did Canada declare a moratorium on cod fishing off Newfoundland?', ['1992', '1867', '1931', '1949'], 0),
    ('What does an ombudsman investigate?', ['Complaints from citizens against government departments or organizations', 'Only complaints made by government employees', 'Weather-related emergencies', 'Traffic violations on public roads'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_171_180)
    append_to(6, g6_171_180)
